#!/usr/bin/env python3
"""Finite native-query adapter checks; no fast hierarchy timing claim.

Check every simple graph through four vertices, every cover (and the default
greedy cover), and every mixed native failure set of size at most two.
An independent subset dynamic program computes each full residual optimum.
"""
from __future__ import annotations

from collections import Counter
from copy import deepcopy
from functools import lru_cache
from itertools import combinations
import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "reference"))
from failure_kernel import build_failure_kernel  # noqa: E402
from failure_query import solve_failure_query  # noqa: E402
from verify_certificate import verify_result  # noqa: E402


def optimum(n, edges):
    adjacency = [0] * n
    for u, v in edges:
        adjacency[u] |= 1 << v
        adjacency[v] |= 1 << u

    @lru_cache(None)
    def solve(mask):
        if not mask:
            return 0
        bit = mask & -mask
        u = bit.bit_length() - 1
        remaining = mask ^ bit
        answer = solve(remaining)
        neighbors = adjacency[u] & remaining
        while neighbors:
            other = neighbors & -neighbors
            neighbors ^= other
            answer = max(answer, 1 + solve(remaining ^ other))
        return answer

    return solve((1 << n) - 1)


def check_query(graph, kernel, vertices, indices, counts):
    labels = graph.get("edge_ids")
    if labels is None:
        labels = list(range(len(graph["edges"])))
    before = deepcopy((graph, kernel))
    result = solve_failure_query(graph, kernel, failed_vertices=iter(vertices),
                                 failed_edge_ids=(labels[i] for i in indices))
    assert (graph, kernel) == before
    residual = [edge for index, edge in enumerate(graph["edges"])
                if index not in indices and all(u not in vertices for u in edge)]
    assert result["cardinality"] == optimum(graph["n"], residual)
    verify_result(graph["n"], graph["edges"], result, labels, require_certificate=False)
    for record in result["matching"]:
        assert record["input_index"] not in indices
        assert record["u"] not in vertices and record["v"] not in vertices
    sub = result["subproblem"]
    lifted = result["subproblem_vertices"]
    assert lifted == [u for u in kernel["vertices"] if u not in vertices]
    expected = [record for record in kernel["edges"] if record["input_index"] not in indices
                and record["u"] not in vertices and record["v"] not in vertices]
    assert sub["n"] == len(lifted)
    assert [[lifted[u], lifted[v]] for u, v in sub["edges"]] == [
        [record["u"], record["v"]] for record in expected]
    assert [(type(label), label) for label in sub["edge_ids"]] == [
        (type(record["id"]), record["id"]) for record in expected]
    assert verify_result(sub["n"], sub["edges"], result["subproblem_result"],
                         sub["edge_ids"])["optimality_verified"] is True
    for native, local in zip(result["matching"], result["subproblem_result"]["matching"]):
        assert native["u"] == lifted[local["u"]]
        assert native["v"] == lifted[local["v"]]
        assert type(native["id"]) is type(local["id"]) and native["id"] == local["id"]
    covered = set(kernel["cover"])
    charge = sum(u not in covered for u in vertices)
    charge += sum((graph["edges"][i][0] in covered) != (graph["edges"][i][1] in covered)
                  for i in indices)
    assert result["charged_failures"] == charge
    counts["oracle_queries"] += 1


def main():
    if not __debug__:
        raise SystemExit("this checker requires assertions; do not use python -O")
    counts = Counter()
    for n in range(5):
        possible = list(combinations(range(n), 2))
        for mask in range(1 << len(possible)):
            edges = [(v, u) if i % 2 else (u, v)
                     for i, (u, v) in enumerate(possible) if mask & (1 << i)]
            graph = {"n": n, "edges": edges,
                     "edge_ids": [i if i % 2 == 0 else str(i - 1) for i in range(len(edges))]}
            covers = [None] + [[u for u in range(n) if subset & (1 << u)]
                              for subset in range(1 << n)
                              if all(subset & ((1 << u) | (1 << v)) for u, v in edges)]
            objects = [("v", u) for u in range(n)] + [("e", i) for i in range(len(edges))]
            for cover in covers:
                kernel = build_failure_kernel(n, edges, 2, graph["edge_ids"], cover=cover)
                for size in range(3):
                    for failures in combinations(objects, size):
                        vertices = [u for kind, u in failures if kind == "v"]
                        indices = [i for kind, i in failures if kind == "e"]
                        check_query(graph, kernel, vertices, indices, counts)
                counts["kernels"] += 1
            counts["graphs"] += 1

    # Arbitrarily many free cover deletions, zero budget, omitted/null IDs,
    # and sparse original vertex numbers exercise the adapter's exact scope.
    for labels in (None, list(range(6))):
        graph = {"n": 9, "edges": [[8, u] for u in range(6)], "edge_ids": labels}
        kernel = build_failure_kernel(9, graph["edges"], 0, labels, cover=range(9))
        check_query(graph, kernel, [0, 1, 2, 3, 8], list(range(6)), counts)
    graph = {"n": 8, "edges": [[7, 1], [7, 3], [7, 5]], "edge_ids": [1, "1", "last"]}
    kernel = build_failure_kernel(8, graph["edges"], 1, graph["edge_ids"], cover=[7])
    for index in range(3):
        check_query(graph, kernel, [], [index], counts)
    check_query(graph, kernel, [5], [], counts)  # A nonretained neighbor.
    check_query(graph, kernel, [0], [], counts)  # An omitted isolate still costs one.

    # Nontrivial compression and every budget boundary on a larger star.
    star = {"n": 10, "edges": [[9, u] for u in range(9)]}
    for budget in range(3):
        compressed = build_failure_kernel(10, star["edges"], budget, cover=[9])
        objects = [("v", u) for u in range(10)] + [("e", i) for i in range(9)]
        for size in range(3):
            for failures in combinations(objects, size):
                vertices = [u for kind, u in failures if kind == "v"]
                indices = [i for kind, i in failures if kind == "e"]
                if sum(u != 9 for u in vertices) + len(indices) <= budget:
                    check_query(star, compressed, vertices, indices, counts)

    def rejected(**kwargs):
        try:
            solve_failure_query(graph, kernel, **kwargs)
        except ValueError:
            counts["rejections"] += 1
        else:
            raise AssertionError(f"invalid query accepted: {kwargs}")

    for vertices in ([True], [-1], [8], [1, 1], [0, 2]):
        rejected(failed_vertices=vertices)
    for ids in ([True], [1.0], ["unknown"], ["1", "1"], [1, "1"]):
        rejected(failed_edge_ids=ids)
    rejected(failed_vertices=[1], failed_edge_ids=[1])  # Still two charged objects.
    bad = deepcopy(kernel)
    bad["vertices"] = []
    try:
        solve_failure_query(graph, bad)
    except ValueError:
        counts["rejections"] += 1
    else:
        raise AssertionError("tampered universal certificate accepted")
    empty = {"n": 0, "edges": []}
    check_query(empty, build_failure_kernel(0, [], 10**100), [], [], counts)
    print("PASS: native mixed-failure query adapter")
    print(json.dumps(dict(sorted(counts.items())), indent=2))
    print("Scope: finite query lifting, budget validation and residual certificates; no fast-backend claim.")


if __name__ == "__main__":
    main()
