#!/usr/bin/env python3
"""Verify native degree witnesses and certified NO/optimality decisions.

No matching search is imported or run. Reconstruct the deterministic sparse
reduction and use only the independent general-matching certificate verifier.
The reduction builder is shared proof code, not a second implementation.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
from degree_reduction import FORMAT, Problem, from_json, matching_module, normalize, reduce_interval


def _infeasible(problem: Problem, low: int, high: int, evidence: object) -> None:
    if not isinstance(evidence, dict):
        raise ValueError("an infeasibility certificate is required")
    reduced = reduce_interval(problem, low, high)
    if reduced.failure is not None:
        if evidence.get("kind") != "local" or evidence.get("reason") != reduced.failure:
            raise ValueError("local infeasibility evidence does not match the input")
        return
    if evidence.get("kind") != "matching":
        raise ValueError("a matching optimality certificate is required")
    matching = evidence.get("matching_result")
    report = matching_module("verify_certificate").verify_result(
        reduced.n, reduced.edges, matching, require_certificate=True)
    if 2*report["cardinality"] >= reduced.n:
        raise ValueError("the certified matching does not rule out a perfect matching")


def check_native(problem: Problem, result: dict) -> int:
    """One original-record scan; no gadget or matching algorithm is involved."""
    selected = result.get("selected_edges")
    cardinality = result.get("cardinality")
    if not isinstance(selected, list) or type(cardinality) is not int or cardinality != len(selected):
        raise ValueError("selected_edges and cardinality disagree")
    used = [False]*len(problem.edges)
    degree = [0]*problem.n
    for record in selected:
        if not isinstance(record, dict):
            raise ValueError("selected edge records must be objects")
        index = record.get("input_index")
        if type(index) is not int or not 0 <= index < len(problem.edges) or used[index]:
            raise ValueError("selected input indices must be valid and distinct")
        u, v = problem.edges[index]
        if (type(record.get("u")) is not int or type(record.get("v")) is not int
                or (record["u"], record["v"]) != (u, v)):
            raise ValueError("selected endpoints do not match the native record")
        if type(record.get("id")) is not type(problem.labels[index]) or record["id"] != problem.labels[index]:
            raise ValueError("selected ID does not match the native record")
        used[index] = True
        degree[u] += 1
        degree[v] += 1
    reported = result.get("degrees")
    if (not isinstance(reported, list) or any(type(d) is not int for d in reported)
            or reported != degree):
        raise ValueError("reported native degrees are incorrect")
    if not all(g <= d <= f for g, d, f in zip(problem.lower, degree, problem.upper)):
        raise ValueError("selected native edges violate a vertex-degree interval")
    if not problem.low <= cardinality <= problem.high:
        raise ValueError("selected cardinality violates the requested interval")
    return cardinality


def verify_problem_result(problem: Problem, result: dict) -> dict:
    if not isinstance(result, dict) or result.get("objective") != problem.objective:
        raise ValueError("result objective differs from the request")
    certificate = result.get("certificate")
    if not isinstance(certificate, dict) or certificate.get("format") != FORMAT:
        raise ValueError("a supported degree-result certificate is required")
    if result.get("status") == "NO":
        if result.get("selected_edges") != [] or result.get("cardinality") is not None or result.get("degrees") is not None:
            raise ValueError("a NO result must not include a selected subgraph")
        _infeasible(problem, problem.low, problem.high, certificate.get("infeasibility"))
        return dict(verified=True, status="NO", feasibility_verified=True, optimality_verified=False)
    if result.get("status") != "YES":
        raise ValueError("status must be YES or NO")
    if problem.failure is not None:
        raise ValueError("a locally impossible request cannot have a YES witness")
    cardinality = check_native(problem, result)
    optimum = problem.objective != "feasible"
    if optimum:
        evidence = certificate.get("optimality")
        if not isinstance(evidence, dict):
            raise ValueError("an optimality certificate is required")
        endpoint = problem.high if problem.objective == "maximum" else problem.low
        if cardinality == endpoint:
            if evidence.get("kind") != "endpoint":
                raise ValueError("a cardinality-endpoint certificate is required")
        else:
            interval = ([cardinality+1, problem.high] if problem.objective == "maximum"
                        else [problem.low, cardinality-1])
            if evidence.get("kind") != "excluded" or evidence.get("cardinality") != interval:
                raise ValueError("the certificate must exclude every better cardinality")
            _infeasible(problem, *interval, evidence.get("infeasibility"))
    return dict(verified=True, status="YES", feasibility_verified=True,
                optimality_verified=optimum, cardinality=cardinality)


def verify_degree_result(n, edges, result, lower=None, upper=None, edge_ids=None,
                         cardinality=None, objective="feasible"):
    problem = normalize(n, edges, lower, upper, edge_ids, cardinality, objective)
    return verify_problem_result(problem, result)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", help="original degree-request JSON")
    parser.add_argument("result", help="solver result JSON")
    args = parser.parse_args()
    try:
        problem = from_json(json.loads(Path(args.input).read_text(encoding="utf-8")))
        result = json.loads(Path(args.result).read_text(encoding="utf-8"))
        report = verify_problem_result(problem, result)
    except (OSError, TypeError, ValueError) as error:
        parser.error(str(error))
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
