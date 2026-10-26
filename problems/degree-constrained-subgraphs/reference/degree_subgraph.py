#!/usr/bin/env python3
"""Unconditional deterministic degree-interval/cardinality reference solver.

Use the locally proved sparse reduction and the repository's exact matching
solver. Original parallel edge records remain separately selectable. Every
NO has a checked maximum-matching certificate or an explicit local bound.
Minimum/maximum outputs also certify the exclusion of every better size.
This is an ordinary polynomial-time solver, not the fast research backend.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
from degree_reduction import FORMAT, Problem, from_json, matching_module, normalize, reduce_interval
from verify_degree import verify_problem_result


def solve_problem(problem: Problem) -> dict:
    statistics = dict(matching_calls=0, feasibility_queries=0,
                      maximum_reduced_vertices=0, maximum_reduced_edges=0)

    def feasible(low, high):
        statistics["feasibility_queries"] += 1
        if problem.failure is None:
            if low == 0 and not any(problem.lower[v] for v in problem.active):
                return [], None
            if high == len(problem.edges):
                degree = [0]*len(problem.active)
                for u, v in problem.active_edges:
                    degree[u] += 1
                    degree[v] += 1
                if all(degree[i] <= problem.upper[v] for i, v in enumerate(problem.active)):
                    return list(range(len(problem.edges))), None
        reduced = reduce_interval(problem, low, high)
        if reduced.failure is not None:
            return None, dict(kind="local", reason=reduced.failure)
        statistics["matching_calls"] += 1
        statistics["maximum_reduced_vertices"] = max(statistics["maximum_reduced_vertices"], reduced.n)
        statistics["maximum_reduced_edges"] = max(statistics["maximum_reduced_edges"], len(reduced.edges))
        matching = matching_module("matching").maximum_matching(reduced.n, reduced.edges,
                                                                 certificate=True)
        report = matching_module("verify_certificate").verify_result(
            reduced.n, reduced.edges, matching, require_certificate=True)
        if 2*report["cardinality"] != reduced.n:
            return None, dict(kind="matching", matching_result=matching)
        selected = [reduced.native_index[record["input_index"]]
                    for record in matching["matching"]
                    if reduced.native_index[record["input_index"]] is not None]
        selected.sort()
        return selected, None

    selected, failure = feasible(problem.low, problem.high)
    certificate = dict(format=FORMAT)
    if selected is None:
        certificate["infeasibility"] = failure
        result = dict(status="NO", objective=problem.objective, cardinality=None,
                      selected_edges=[], degrees=None, certificate=certificate,
                      statistics=statistics)
        verify_problem_result(problem, result)
        return result
    if problem.objective != "feasible":
        low, high = problem.low, problem.high
        boundary_failure = None
        boundary_interval = None
        while low < high:
            if problem.objective == "maximum":
                midpoint = (low+high+1)//2
                candidate, failure = feasible(midpoint, problem.high)
                if candidate is None:
                    high = midpoint-1
                    boundary_failure, boundary_interval = failure, [midpoint, problem.high]
                else:
                    low, selected = midpoint, candidate
            else:
                midpoint = (low+high)//2
                candidate, failure = feasible(problem.low, midpoint)
                if candidate is None:
                    low = midpoint+1
                    boundary_failure, boundary_interval = failure, [problem.low, midpoint]
                else:
                    high, selected = midpoint, candidate
        if len(selected) != low:
            raise RuntimeError("the optimality boundary disagrees with the returned native size")
        endpoint = problem.high if problem.objective == "maximum" else problem.low
        if low == endpoint:
            certificate["optimality"] = dict(kind="endpoint")
        else:
            expected = ([low+1, problem.high] if problem.objective == "maximum"
                        else [problem.low, low-1])
            if boundary_interval != expected or boundary_failure is None:
                raise RuntimeError("binary search did not retain the final excluded interval")
            certificate["optimality"] = dict(kind="excluded", cardinality=expected,
                                              infeasibility=boundary_failure)
    degrees = [0]*problem.n
    for index in selected:
        u, v = problem.edges[index]
        degrees[u] += 1
        degrees[v] += 1
    result = dict(status="YES", objective=problem.objective, cardinality=len(selected),
                  selected_edges=[dict(input_index=i, id=problem.labels[i],
                                       u=problem.edges[i][0], v=problem.edges[i][1]) for i in selected],
                  degrees=degrees, certificate=certificate, statistics=statistics)
    verify_problem_result(problem, result)
    return result


def degree_subgraph(n, edges, lower=None, upper=None, edge_ids=None,
                    cardinality=None, objective="feasible"):
    """Return a checked YES/NO result for loopless explicit native records."""
    return solve_problem(normalize(n, edges, lower, upper, edge_ids, cardinality, objective))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", nargs="?", default="-", help="request JSON file; - reads stdin")
    args = parser.parse_args()
    try:
        source = sys.stdin.read() if args.input == "-" else Path(args.input).read_text(encoding="utf-8")
        result = solve_problem(from_json(json.loads(source)))
    except (OSError, TypeError, ValueError) as error:
        parser.error(str(error))
    json.dump(result, sys.stdout, indent=2, ensure_ascii=False)
    sys.stdout.write("\n")


if __name__ == "__main__":
    main()
