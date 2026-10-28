#!/usr/bin/env python3
"""Independent finite checks for the supplied-baseline arborescence backend.

Copyright 2026 icekylinx. Authored by GPT-6 Astra Pro.
SPDX-License-Identifier: Apache-2.0

Exhaustive tree enumeration supplies small baselines and failure optima; it
does not use the exchange graph. Larger bidirected-path fixtures have direct
forced-parent optimum formulas and exercise actual hub-tree reporting.
"""
from fractions import Fraction
from itertools import combinations
import json
from math import isqrt
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "reference"))
import arborescence_reporting as backend
from arborescence_reporting import Arc, build


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def tree(n, root, arcs, selected):
    if len(selected) != n - 1 or len(set(selected)) != n - 1:
        return False
    indegree = [0] * n
    adjacency = [[] for _ in range(n)]
    for i in selected:
        a = arcs[i]
        indegree[a.head] += 1
        adjacency[a.tail].append(a.head)
    if indegree[root] != 0 or any(indegree[v] != 1 for v in range(n) if v != root):
        return False
    reached, pending = {root}, [root]
    while pending:
        for v in adjacency[pending.pop()]:
            if v not in reached:
                reached.add(v)
                pending.append(v)
    return len(reached) == n


def forest(arcs, selected, n):
    """Direct graphic-matroid test, independent of tree paths and HLD."""
    parent = list(range(n))

    def find(v):
        while parent[v] != v:
            v = parent[v]
        return v

    for i in selected:
        a = arcs[i]
        u, v = find(a.tail), find(a.head)
        if u == v:
            return False
        parent[u] = v
    return True


def all_trees(n, root, arcs):
    eligible = [i for i, a in enumerate(arcs) if a.head != root and a.head != a.tail]
    return [(sum((arcs[i].cost for i in chosen), Fraction(0)), chosen)
            for chosen in combinations(eligible, n - 1) if tree(n, root, arcs, chosen)]


def audit_auxiliary(n, root, arcs, baseline, counts):
    nodes, auxiliary, minus, plus = backend._auxiliary(n, root, arcs, baseline)
    require(nodes == max(0, 4 * (n - 1) - 1), "unexpected auxiliary node count")
    incoming = {arcs[i].head: i for i in baseline}
    by_tail = [[] for _ in range(nodes)]
    for a in auxiliary:
        by_tail[a.tail].append(a)
    for removed in baseline:
        reached, pending = {plus[removed]}, [plus[removed]]
        while pending:
            for a in by_tail[pending.pop()]:
                if a.label is None and a.head not in reached:
                    reached.add(a.head)
                    pending.append(a.head)
        actual = {(a.label, a.head) for a in auxiliary
                  if a.label is not None and a.tail in reached}
        expected = set()
        for i, a in enumerate(arcs):
            if i not in baseline and a.head != root and a.tail != a.head:
                candidate = tuple(j for j in baseline if j != removed) + (i,)
                if forest(arcs, candidate, n):
                    expected.add((i, minus[incoming[a.head]]))
        require(actual == expected, "HLD graphic/partition transitions differ")
        counts["baseline_transition_rows"] += 1
    return nodes


def audit_report(oracle, arcs, n, root, failed, expected, counts, min_added=None):
    answer = oracle.query(failed)
    counts["queries"] += 1
    if expected is None:
        require(answer is None and oracle.optimum_cost(failed) is None,
                "infeasibility mismatch")
        counts["infeasible_queries"] += 1
        return
    require(answer is not None and tree(n, root, arcs, answer), "report is not a tree")
    require(failed is None or failed not in answer, "failed original arc was reported")
    require(set(answer) <= set(oracle.support), "report escaped retained support")
    require(sum((arcs[i].cost for i in answer), Fraction(0)) == expected,
            "report is not independently optimal")
    require(oracle.optimum_cost(failed) == expected, "stored objective mismatch")
    if min_added is not None:
        require(len(set(answer) - set(oracle.baseline)) == min_added,
                "minimum-hop update has too many outside labels")
    if failed in oracle.routes:
        route = oracle.routes[failed]
        path = oracle._report(route)
        vertices = [route.source] + [a.head for a in path]
        require(all(a.head == b.tail for a, b in zip(path, path[1:])),
                "reporting path is discontinuous")
        require(len(vertices) == len(set(vertices)) <= oracle.auxiliary_nodes,
                "reporting path repeats an auxiliary vertex")
        require(vertices[-1] == route.target, "reporting path has wrong target")
        labels = [a.label for a in path if a.label is not None]
        removed = [a.removed for a in path if a.removed is not None]
        require(len(labels) == len(set(labels)) == len(removed) == len(set(removed)),
                "literal update repeats an original label or removal")
        require(failed in removed, "reported cycle avoids the failure")
        counts["hub_reports" if route.hub is not None else "explicit_reports"] += 1
    counts["feasible_queries"] += 1


def check_small(counts):
    n, root = 4, 0
    possible = [(u, v) for u in range(n) for v in range(1, n) if u != v]
    profiles = [tuple(0 for _ in possible), tuple(1 for _ in possible),
                tuple((i * i + 3 * i + 1) % 7 for i in range(len(possible))),
                tuple(Fraction((5 * i + 2) % 9, (i % 3) + 1)
                      for i in range(len(possible))),
                tuple(i % 2 for i in range(len(possible)))]
    for mask in range(1 << len(possible)):
        counts["four_vertex_graphs"] += 1
        for costs in profiles:
            arcs = tuple(Arc(u, v, costs[i]) for i, (u, v) in enumerate(possible)
                         if mask >> i & 1)
            candidates = all_trees(n, root, arcs)
            if not candidates:
                counts["no_baseline_instances"] += 1
                continue
            optimum, baseline = min(candidates)
            counts["feasible_instances"] += 1
            oracle = build(n, root, arcs, baseline)
            audit_auxiliary(n, root, arcs, baseline, counts)
            for failed in (None, *range(len(arcs)), len(arcs) + 17):
                surviving = [(c, chosen) for c, chosen in candidates
                             if failed is None or failed not in chosen]
                expected = min((c for c, _ in surviving), default=None)
                min_added = (min(len(set(chosen) - set(baseline))
                                 for c, chosen in surviving if c == expected)
                             if expected is not None else None)
                audit_report(oracle, arcs, n, root, failed, expected, counts, min_added)
            # Every retained-support optimum is independently witnessed, not
            # merely a numerical distance equality in the exchange graph.
            counts["four_vertex_profile_instances"] += 1


def check_long(counts):
    for n in (10, 25, 65):
        for outside_cost in (0, Fraction(2, 3)):
            k = n - 1
            arcs = tuple([Arc(v - 1, v, 0) for v in range(1, n)]
                         + [Arc(v, v - 1, outside_cost) for v in range(2, n)]
                         + [Arc(0, k, outside_cost)])
            baseline = tuple(range(k))
            oracle = build(n, 0, arcs, baseline)
            audit_auxiliary(n, 0, arcs, baseline, counts)
            counts["long_path_instances"] += 1
            # A surviving root-to-f path must travel 0->k and then backward
            # to f. The other vertices keep their zero-cost forward parents.
            # For positive outside cost this is the unique cheapest split;
            # for zero costs it is still the split with fewest added arcs.
            for failed in (None, *range(len(arcs)), len(arcs) + 1):
                expected = (outside_cost * (k - failed)
                            if failed in baseline else Fraction(0))
                min_added = k - failed if failed in baseline else 0
                audit_report(oracle, arcs, n, 0, failed, expected, counts, min_added)
            require(oracle.hubs, "long fixture did not exercise hub-tree reporting")
            require(oracle.record_count <= 64 * oracle.auxiliary_nodes
                    * (isqrt(k) + 1) + 10 * k,
                    "unexpected record accounting")
            counts["maximum_auxiliary_nodes"] = max(counts["maximum_auxiliary_nodes"],
                                                    oracle.auxiliary_nodes)


def check_boundaries(counts):
    fixtures = [
        (1, 0, (Arc(0, 0, 0),), ()),
        (3, 2, (Arc(2, 0, Fraction(1, 2)), Arc(0, 1, 0),
                Arc(2, 1, 2), Arc(0, 1, 1), Arc(1, 2, 0), Arc(0, 0, 0)), (0, 1)),
    ]
    for n, root, arcs, baseline in fixtures:
        oracle = build(n, root, arcs, baseline)
        candidates = all_trees(n, root, arcs)
        for failed in (None, *range(len(arcs)), len(arcs) + 1):
            expected = min((c for c, chosen in candidates if failed not in chosen),
                           default=None)
            audit_report(oracle, arcs, n, root, failed, expected, counts)
        counts["boundary_instances"] += 1
    invalid = [
        (0, 0, (), ()),
        (2, 2, (Arc(0, 1, 1),), (0,)),
        (2, 0, (Arc(0, 1, 0.5),), (0,)),
        (2, 0, (Arc(0, 1, -1),), (0,)),
        (2, 0, (Arc(0, 2, 0),), (0,)),
        (3, 0, (Arc(1, 2, 0), Arc(2, 1, 0)), (0, 1)),
        (2, 0, (Arc(1, 0, 0),), (0,)),
        (2, 0, (Arc(0, 1, 0),), (0, 0)),
        (2, 0, (Arc(0, 1, 2), Arc(0, 1, 1)), (0,)),
    ]
    for args in invalid:
        try:
            build(*args)
        except ValueError:
            counts["rejected_inputs"] += 1
        else:
            raise AssertionError("invalid input or suboptimal baseline accepted")
    # Queries have no dependency on input lists or preprocessing routines.
    original = [Arc(0, 1, 0), Arc(0, 1, 1)]
    oracle = build(2, 0, original, (0,))
    original.clear()
    names = ("build", "_auxiliary", "_distances", "_sparsify")
    saved = {name: getattr(backend, name) for name in names}

    def unavailable(*args, **kwargs):
        raise AssertionError("query invoked preprocessing")

    try:
        for name in names:
            setattr(backend, name, unavailable)
        require(oracle.query(0) == (1,) and oracle.query(1) == (0,),
                "query depends on original input storage")
    finally:
        for name, function in saved.items():
            setattr(backend, name, function)
    counts["isolated_reporting_checks"] += 2


def main():
    names = ("four_vertex_graphs", "no_baseline_instances", "feasible_instances",
             "four_vertex_profile_instances", "baseline_transition_rows", "queries",
             "feasible_queries", "infeasible_queries", "hub_reports", "explicit_reports",
             "long_path_instances", "maximum_auxiliary_nodes", "boundary_instances",
             "rejected_inputs", "isolated_reporting_checks")
    counts = dict.fromkeys(names, 0)
    check_small(counts)
    check_long(counts)
    check_boundaries(counts)
    require(counts["hub_reports"] > 0 and counts["explicit_reports"] > 0,
            "both reporting representations must be exercised")
    print(json.dumps({"status": "pass", "arborescence_reporting": counts}, indent=2))


if __name__ == "__main__":
    main()
