#!/usr/bin/env python3
"""Answer a native failure query using a verified fixed matching kernel.

This adapter uses the ordinary polynomial reference matching solver.  It
does not implement the fast research hierarchy or a dynamic query bound.
"""
from __future__ import annotations

from bisect import bisect_left
from typing import Iterable

from matching import maximum_matching
from verify_failure_kernel import verify_failure_kernel


def solve_failure_query(
    graph: dict,
    kernel: dict,
    *,
    failed_vertices: Iterable[int] = (),
    failed_edge_ids: Iterable[int | str] = (),
) -> dict:
    """Return a maximum surviving matching in original native coordinates.

    Verify the universal kernel certificate on every call.  Charge each
    failed outside vertex and each failed crossing edge once, including
    edges incident to failed vertices and objects absent from the kernel.
    Cover vertices and cover-internal edges are free.  Reject duplicates,
    unknown objects, booleans and queries exceeding the certified budget.

    ``subproblem`` uses compact vertices and original native edge IDs;
    ``subproblem_result`` includes its independently checkable optimality
    certificate.  Its input indices are local to the subproblem.  Only the
    top-level ``matching`` has original input indices and vertex numbers.
    """
    verify_failure_kernel(graph, kernel)
    n, edges = graph["n"], graph["edges"]
    labels = graph.get("edge_ids")
    if labels is None:
        labels = list(range(len(edges)))
    covered = [False] * n
    for u in kernel["cover"]:
        covered[u] = True
    deleted_vertices = [False] * n
    charged = 0
    for u in failed_vertices:
        if type(u) is not int or not 0 <= u < n or deleted_vertices[u]:
            raise ValueError("failed_vertices must contain distinct original vertices")
        deleted_vertices[u] = True
        charged += not covered[u]

    # Tagged comparison keys keep integer 1 distinct from string "1" and
    # avoid a hash-table complexity assumption for arbitrary native labels.
    ordered = sorted((0 if type(label) is int else 1, label, index)
                     for index, label in enumerate(labels))
    keys = [(tag, label) for tag, label, _ in ordered]
    deleted_edges = [False] * len(edges)
    for label in failed_edge_ids:
        if type(label) not in (int, str):
            raise ValueError("failed edge IDs must be integers or strings, not booleans")
        key = (0 if type(label) is int else 1, label)
        at = bisect_left(keys, key)
        if at == len(keys) or keys[at] != key:
            raise ValueError("unknown failed native edge ID")
        index = ordered[at][2]
        if deleted_edges[index]:
            raise ValueError("failed edge IDs must be distinct")
        deleted_edges[index] = True
        u, v = edges[index]
        charged += covered[u] != covered[v]
    if charged > kernel["failure_budget"]:
        raise ValueError("query exceeds the certified outside-vertex/crossing-edge budget")

    vertices = [u for u in kernel["vertices"] if not deleted_vertices[u]]
    compact = [-1] * n
    for at, u in enumerate(vertices):
        compact[u] = at
    surviving = [record for record in kernel["edges"]
                 if not deleted_edges[record["input_index"]]
                 and not deleted_vertices[record["u"]]
                 and not deleted_vertices[record["v"]]]
    subproblem = {
        "n": len(vertices),
        "edges": [[compact[record["u"]], compact[record["v"]]] for record in surviving],
        "edge_ids": [record["id"] for record in surviving],
    }
    solved = maximum_matching(subproblem["n"], subproblem["edges"],
                              subproblem["edge_ids"], certificate=True)
    matching = [dict(surviving[record["input_index"]]) for record in solved["matching"]]
    return {
        "cardinality": solved["cardinality"],
        "matching": matching,
        "charged_failures": charged,
        "subproblem_vertices": vertices,
        "subproblem": subproblem,
        "subproblem_result": solved,
    }
