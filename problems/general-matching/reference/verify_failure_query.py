#!/usr/bin/env python3
"""Verify an entire native mixed-failure answer without running a solver.

The query is supplied independently of the answer. Universal preservation,
the exact residual subproblem, its optimum, and native feasibility are each
checked; no producer-reported graph or failure count is trusted.
"""
from __future__ import annotations

from bisect import bisect_left
from typing import Iterable

from verify_certificate import verify_result
from verify_failure_kernel import verify_failure_kernel


def _same_data(actual, expected):
    """Strict JSON data equality, in particular rejecting bool-as-int."""
    if type(actual) is not type(expected):
        return False
    if isinstance(expected, list):
        return len(actual) == len(expected) and all(
            _same_data(a, b) for a, b in zip(actual, expected))
    if isinstance(expected, dict):
        return actual.keys() == expected.keys() and all(
            _same_data(actual[key], value) for key, value in expected.items())
    return actual == expected


def verify_failure_query(
    graph: dict,
    kernel: dict,
    result: dict,
    *,
    failed_vertices: Iterable[int] = (),
    failed_edge_ids: Iterable[int | str] = (),
) -> dict:
    """Raise ValueError on rejection; otherwise certify the full residual optimum.

    The universal kernel verifier supplies the preservation theorem's finite
    premises. The ordinary certificate verifier proves the compact optimum.
    This routine checks their composition and the native answer independently
    of the query adapter, without importing matching or kernel constructors.
    """
    verify_failure_kernel(graph, kernel)
    if not isinstance(result, dict):
        raise ValueError("query result must be an object")
    n, edges = graph["n"], graph["edges"]
    labels = graph.get("edge_ids")
    if labels is None:
        labels = list(range(len(edges)))
    cover = [False] * n
    for vertex in kernel["cover"]:
        cover[vertex] = True
    absent = [False] * n
    charge = 0
    for vertex in failed_vertices:
        if type(vertex) is not int or not 0 <= vertex < n or absent[vertex]:
            raise ValueError("invalid or repeated failed vertex")
        absent[vertex] = True
        charge += not cover[vertex]
    ordered = sorted((0 if type(label) is int else 1, label, index)
                     for index, label in enumerate(labels))
    keys = [(tag, label) for tag, label, _ in ordered]
    removed = [False] * len(edges)
    for label in failed_edge_ids:
        if type(label) not in (int, str):
            raise ValueError("invalid failed edge ID type")
        key = (0 if type(label) is int else 1, label)
        position = bisect_left(keys, key)
        if position == len(keys) or keys[position] != key:
            raise ValueError("unknown failed edge ID")
        index = ordered[position][2]
        if removed[index]:
            raise ValueError("repeated failed edge ID")
        removed[index] = True
        u, v = edges[index]
        charge += cover[u] != cover[v]
    if charge > kernel["failure_budget"]:
        raise ValueError("failure query exceeds the universal certificate budget")
    if type(result.get("charged_failures")) is not int or result["charged_failures"] != charge:
        raise ValueError("incorrect failure charge")

    vertices = [vertex for vertex in kernel["vertices"] if not absent[vertex]]
    if not _same_data(result.get("subproblem_vertices"), vertices):
        raise ValueError("incorrect compact vertex map")
    compact = [-1] * n
    for index, vertex in enumerate(vertices):
        compact[vertex] = index
    retained = [record for record in kernel["edges"]
                if not removed[record["input_index"]]
                and not absent[record["u"]] and not absent[record["v"]]]
    expected = {
        "n": len(vertices),
        "edges": [[compact[record["u"]], compact[record["v"]]] for record in retained],
        "edge_ids": [record["id"] for record in retained],
    }
    if not _same_data(result.get("subproblem"), expected):
        raise ValueError("reported subproblem differs from the certified residual kernel")
    local = verify_result(expected["n"], expected["edges"],
                          result.get("subproblem_result"), expected["edge_ids"])
    native = verify_result(n, edges, result, labels, require_certificate=False)
    for record in result["matching"]:
        if removed[record["input_index"]] or absent[record["u"]] or absent[record["v"]]:
            raise ValueError("native matching uses a failed object")
    if native["cardinality"] != local["cardinality"]:
        raise ValueError("native matching does not attain the certified residual optimum")
    return {
        "matching_feasible": True,
        "optimality_verified": True,
        "cardinality": native["cardinality"],
        "charged_failures": charge,
        "scope": "original graph after the supplied native vertex and edge failures",
    }
