#!/usr/bin/env python3
"""Independently verify a universal mixed-failure matching kernel.

No matching algorithm is imported or called.  Local neighbor counts prove
the first reduction.  For every subsequent layer, a matching and an equally
large vertex cover prove maximum cardinality by elementary weak duality.
The layered replacement theorem then establishes all failure queries at once.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys


def _indices(value, upper: int, name: str) -> list[int]:
    if not isinstance(value, list):
        raise ValueError(f"{name} must be a sorted list")
    previous = -1
    for index in value:
        if type(index) is not int or not previous < index < upper:
            raise ValueError(f"{name} must contain distinct increasing indices in range")
        previous = index
    return value


def verify_failure_kernel(graph: dict, result: dict) -> dict:
    """Validate the exact certificate and return its mathematical scope."""
    if not isinstance(graph, dict) or not isinstance(result, dict):
        raise ValueError("graph and result must be objects")
    n, edges = graph.get("n"), graph.get("edges")
    if type(n) is not int or n < 0 or not isinstance(edges, list):
        raise ValueError("invalid graph size or edge list")
    m = len(edges)
    pairs = []
    for edge in edges:
        if not isinstance(edge, (list, tuple)) or len(edge) != 2:
            raise ValueError("each edge must have two vertices")
        u, v = edge
        if (type(u) is not int or type(v) is not int or not 0 <= u < n
                or not 0 <= v < n or u == v):
            raise ValueError("input must be loopless with in-range integer vertices")
        pairs.append((min(u, v), max(u, v)))
    pairs.sort()
    if any(a == b for a, b in zip(pairs, pairs[1:])):
        raise ValueError("input must be simple; native parallel edges cannot be normalized")
    labels = graph.get("edge_ids")
    if labels is None:
        labels = list(range(m))
    if not isinstance(labels, list) or len(labels) != m:
        raise ValueError("edge_ids must have one entry per input edge")
    if any(type(label) not in (int, str) for label in labels):
        raise ValueError("edge IDs must be integers or strings")
    ordered_labels = sorted((0 if type(label) is int else 1, label) for label in labels)
    if any(a == b for a, b in zip(ordered_labels, ordered_labels[1:])):
        raise ValueError("edge IDs must be distinct")
    f = result.get("failure_budget")
    if type(f) is not int or f < 0:
        raise ValueError("invalid failure budget")
    if (type(result.get("schema_version")) is not int or result["schema_version"] != 1
            or result.get("kind") != "mixed-failure-matching-kernel"
            or type(result.get("n")) is not int or result["n"] != n):
        raise ValueError("wrong kernel schema or graph size")

    cover = _indices(result.get("cover"), n, "cover")
    covered = [False] * n
    for u in cover:
        covered[u] = True
    if any(not covered[u] and not covered[v] for u, v in edges):
        raise ValueError("cover misses an input edge")
    c = len(cover)
    certificate = result.get("certificate")
    if not isinstance(certificate, dict):
        raise ValueError("missing certificate")
    initial_matching = certificate.get("greedy_matching_input_indices")
    matching_cover = initial_matching is not None
    if matching_cover:
        initial_matching = _indices(initial_matching, m, "initial matching")
        occupied = [False] * n
        for index in initial_matching:
            u, v = edges[index]
            if occupied[u] or occupied[v]:
                raise ValueError("initial edges are not a matching")
            occupied[u] = occupied[v] = True
        if occupied != covered:
            raise ValueError("initial matching does not have exactly the claimed cover endpoints")

    first = _indices(certificate.get("edge_kernel_input_indices"), m, "edge kernel")
    present = [False] * m
    first_degree = [0] * n
    full_degree = [0] * n
    used = covered.copy()
    for index in first:
        present[index] = True
        u, v = edges[index]
        used[u] = used[v] = True
        if covered[u] != covered[v]:
            first_degree[u if covered[u] else v] += 1
    for index, (u, v) in enumerate(edges):
        if covered[u] and covered[v]:
            if not present[index]:
                raise ValueError("edge kernel omitted a cover-internal edge")
        else:
            full_degree[u if covered[u] else v] += 1
    if any(first_degree[u] != min(c + f, full_degree[u]) for u in cover):
        raise ValueError("edge kernel violates the c+f distinct-neighbor rule")

    # Allocate only once on the original vertex universe, then keep each
    # layer's temporary arrays on the compact edge kernel.
    compact = [-1] * n
    vertices = [u for u in range(n) if used[u]]
    for index, u in enumerate(vertices):
        compact[u] = index
    side = [covered[u] for u in vertices]
    selected = side.copy()
    layers = certificate.get("layers")
    if not isinstance(layers, list) or len(layers) > f + 1:
        raise ValueError("invalid number of layers")
    for layer in layers:
        if not isinstance(layer, dict):
            raise ValueError("a layer must be an object")
        indices = _indices(layer.get("matching_input_indices"), m, "layer matching")
        minimum_cover = _indices(layer.get("minimum_cover"), n, "layer cover")
        if not indices or len(indices) != len(minimum_cover):
            raise ValueError("each nonempty layer needs a same-size matching and cover")
        in_cover = [False] * len(vertices)
        for u in minimum_cover:
            at = compact[u]
            if at == -1 or (not side[at] and selected[at]):
                raise ValueError("layer cover contains a vertex outside the residual crossing graph")
            in_cover[at] = True
        matched = [False] * len(vertices)
        right = []
        for index in indices:
            u, v = edges[index]
            if not present[index] or covered[u] == covered[v]:
                raise ValueError("layer matching is not in the crossing edge kernel")
            a, b = compact[u], compact[v]
            if not side[a]:
                a, b = b, a
            if selected[b] or matched[a] or matched[b]:
                raise ValueError("layer matching repeats a vertex or an earlier right endpoint")
            matched[a] = matched[b] = True
            right.append(b)
        for index in first:
            u, v = edges[index]
            if covered[u] == covered[v]:
                continue
            a, b = compact[u], compact[v]
            if not side[a]:
                a, b = b, a
            if not selected[b] and not in_cover[a] and not in_cover[b]:
                raise ValueError("layer cover misses a residual crossing edge")
        for at in right:
            selected[at] = True

    if len(layers) < f + 1:
        for index in first:
            u, v = edges[index]
            if covered[u] != covered[v] and not selected[compact[v if covered[u] else u]]:
                raise ValueError("fewer than f+1 layers leave an unprocessed crossing edge")
    retained_vertices = [u for u in vertices if selected[compact[u]]]
    if _indices(result.get("vertices"), n, "retained vertices") != retained_vertices:
        raise ValueError("retained vertices do not match the certified layer union")
    expected = [index for index in first
                if all(selected[compact[u]] for u in edges[index])]
    records = result.get("edges")
    if not isinstance(records, list) or len(records) != len(expected):
        raise ValueError("retained edges must induce the certified edge-kernel subgraph")
    for record, index in zip(records, expected):
        u, v = edges[index]
        if (not isinstance(record, dict) or type(record.get("input_index")) is not int
                or record["input_index"] != index or type(record.get("id")) is not type(labels[index])
                or record["id"] != labels[index] or type(record.get("u")) is not int
                or type(record.get("v")) is not int or record["u"] != u or record["v"] != v):
            raise ValueError("retained native edge record does not match the input")
    return {
        "universal_preservation_verified": True,
        "failure_budget": f,
        "retained_vertices": len(retained_vertices),
        "retained_edges": len(expected),
        "scope": "all cover subsets; at most f outside-vertex/crossing-edge failures; arbitrary cover deletions",
        "vertex_bound": "min((f+2)c,(f+3)nu(G))" if matching_cover else "(f+2)c",
        "matching_searches": 0,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("graph")
    parser.add_argument("kernel")
    args = parser.parse_args()
    try:
        graph = json.loads(Path(args.graph).read_text(encoding="utf-8"))
        result = json.loads(Path(args.kernel).read_text(encoding="utf-8"))
        report = verify_failure_kernel(graph, result)
    except (OSError, TypeError, ValueError) as error:
        parser.error(str(error))
    json.dump(report, sys.stdout, indent=2, ensure_ascii=False)
    sys.stdout.write("\n")


if __name__ == "__main__":
    main()
