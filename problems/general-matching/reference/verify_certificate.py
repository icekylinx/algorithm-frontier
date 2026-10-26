#!/usr/bin/env python3
"""Check a native matching and its kernel/Tutte--Berge certificate.

This verifier never imports or runs the blossom solver.  It checks input
normalization, a vertex cover and its retained-neighbor conditions, native
matching feasibility, and one odd-component upper bound per component.
Comparison sorting plus graph scans cost O(n + m log(m+2)) operations and
O(n+m) storage, apart from label bytes and the certificate's encoded length.

Usage: python3 verify_certificate.py graph.json matching-result.json
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Iterable


def _integer(value: object, limit: int, name: str) -> int:
    if type(value) is not int or not 0 <= value < limit:
        raise ValueError(f"{name} is not an integer in the required range")
    return value


def verify_result(
    n: int,
    edges: Iterable[tuple[int, int]],
    result: dict,
    edge_ids: Iterable[int | str] | None = None,
    *,
    require_certificate: bool = True,
) -> dict:
    """Raise ValueError on rejection, otherwise return the verified scope.

    A feasibility-only call does not establish optimality.  Statistics in the
    proposed result are informational and are never used as proof evidence.
    """
    if type(n) is not int or n < 0:
        raise ValueError("n must be a nonnegative integer")
    if type(require_certificate) is not bool:
        raise ValueError("require_certificate must be a boolean")
    native = list(edges)
    for index, edge in enumerate(native):
        if not isinstance(edge, (list, tuple)) or len(edge) != 2:
            raise ValueError(f"invalid input edge {index}")
        _integer(edge[0], n, f"edge {index} endpoint")
        _integer(edge[1], n, f"edge {index} endpoint")
    labels = list(range(len(native))) if edge_ids is None else list(edge_ids)
    if len(labels) != len(native) or any(type(label) not in (int, str) for label in labels):
        raise ValueError("input IDs must be integer/string labels, one per record")
    ordered = sorted((0 if type(label) is int else 1, label) for label in labels)
    if any(a == b for a, b in zip(ordered, ordered[1:])):
        raise ValueError("input IDs are not distinct")
    if not isinstance(result, dict) or not isinstance(result.get("matching"), list):
        raise ValueError("result must contain a matching list")
    cardinality = result.get("cardinality")
    if type(cardinality) is not int or cardinality != len(result["matching"]):
        raise ValueError("cardinality differs from the matching list length")
    used_vertex = [False] * n
    selected = [False] * len(native)
    for item in result["matching"]:
        if not isinstance(item, dict):
            raise ValueError("each matching record must be an object")
        index = _integer(item.get("input_index"), len(native), "matching input index")
        u, v = native[index]
        if type(item.get("u")) is not int or type(item.get("v")) is not int or (item["u"], item["v"]) != (u, v):
            raise ValueError("matching endpoints differ from the native record")
        if type(item.get("id")) is not type(labels[index]) or item["id"] != labels[index]:
            raise ValueError("matching ID differs from the native record")
        if u == v or selected[index] or used_vertex[u] or used_vertex[v]:
            raise ValueError("proposed edges do not form a matching")
        selected[index] = True
        used_vertex[u] = used_vertex[v] = True
    report = {"matching_feasible": True, "optimality_verified": False, "cardinality": cardinality}
    if not require_certificate:
        return report

    certificate = result.get("certificate")
    if not isinstance(certificate, dict) or certificate.get("format") != "algorithm-frontier-matching-v1":
        raise ValueError("a supported optimality certificate is required")
    certified = certificate.get("components")
    if not isinstance(certified, list):
        raise ValueError("certificate components must be a list")

    # Independently reconstruct the simple graph and earliest native records.
    pairs = sorted((min(u, v), max(u, v), i) for i, (u, v) in enumerate(native) if u != v)
    representative = [False] * len(native)
    simple: list[tuple[int, int, int]] = []
    previous = (-1, -1)
    adjacency: list[list[int]] = [[] for _ in range(n)]
    for u, v, index in pairs:
        if (u, v) == previous:
            continue
        previous = (u, v)
        representative[index] = True
        simple.append((u, v, index))
        adjacency[u].append(v)
        adjacency[v].append(u)
    component_of = [-1] * n
    components: list[list[int]] = []
    for root in range(n):
        if component_of[root] != -1 or not adjacency[root]:
            continue
        component_id = len(components)
        component_of[root] = component_id
        stack = [root]
        vertices: list[int] = []
        while stack:
            u = stack.pop()
            vertices.append(u)
            for v in adjacency[u]:
                if component_of[v] == -1:
                    component_of[v] = component_id
                    stack.append(v)
        components.append(vertices)
    if len(certified) != len(components):
        raise ValueError("certificate omits or adds a nonempty input component")
    component_edges: list[list[tuple[int, int, int]]] = [[] for _ in components]
    for edge in simple:
        component_edges[component_of[edge[0]]].append(edge)
    match_count = [0] * len(components)
    for index, chosen in enumerate(selected):
        if chosen:
            match_count[component_of[native[index][0]]] += 1
    local_index = [-1] * n
    retained_global = [False] * len(native)
    total_vertices = total_edges = 0

    for component_id, (vertices, cert, original_edges) in enumerate(zip(components, certified, component_edges)):
        if not isinstance(cert, dict) or type(cert.get("root")) is not int or cert["root"] != vertices[0]:
            raise ValueError("certificate components must use increasing minimum-vertex roots")
        for index, vertex in enumerate(vertices):
            local_index[vertex] = index
        order = len(vertices)
        cover = [False] * order
        for field in ("cover", "retained_input_indices", "barrier"):
            if not isinstance(cert.get(field), list):
                raise ValueError(f"component certificate needs a {field} list")
        for vertex in cert["cover"]:
            _integer(vertex, n, "cover vertex")
            if component_of[vertex] != component_id or cover[local_index[vertex]]:
                raise ValueError("cover vertices must be distinct members of their component")
            cover[local_index[vertex]] = True
        cutoff = len(cert["cover"])
        retained_adjacency: list[list[int]] = [[] for _ in vertices]
        incident = [False] * order
        for index in cert["retained_input_indices"]:
            _integer(index, len(native), "retained input index")
            u, v = native[index]
            if not representative[index] or component_of[u] != component_id or retained_global[index]:
                raise ValueError("retained records must be distinct normalized edges of their component")
            retained_global[index] = True
            a, b = local_index[u], local_index[v]
            retained_adjacency[a].append(b)
            retained_adjacency[b].append(a)
            incident[a] = incident[b] = True
        outside_degree = [0] * order
        outside_kept = [0] * order
        for u, v, index in original_edges:
            a, b = local_index[u], local_index[v]
            if not cover[a] and not cover[b]:
                raise ValueError("the proposed cover leaves an edge uncovered")
            if cover[a] and cover[b]:
                if not retained_global[index]:
                    raise ValueError("the kernel omitted an edge inside the cover")
            else:
                endpoint = a if cover[a] else b
                outside_degree[endpoint] += 1
                outside_kept[endpoint] += retained_global[index]
            if selected[index] and not retained_global[index]:
                raise ValueError("a matching edge is absent from its retained kernel")
        for vertex in range(order):
            if cover[vertex] and outside_kept[vertex] < min(cutoff, outside_degree[vertex]):
                raise ValueError("the kernel retained too few distinct outside neighbors")

        removed = [not active for active in incident]
        for vertex in cert["barrier"]:
            _integer(vertex, n, "barrier vertex")
            if component_of[vertex] != component_id or removed[local_index[vertex]]:
                raise ValueError("barrier vertices must be distinct retained vertices")
            removed[local_index[vertex]] = True
        seen = removed.copy()
        odd = 0
        for root in range(order):
            if seen[root]:
                continue
            seen[root] = True
            stack = [root]
            component_order = 0
            while stack:
                u = stack.pop()
                component_order += 1
                for v in retained_adjacency[u]:
                    if not seen[v]:
                        seen[v] = True
                        stack.append(v)
            odd += component_order % 2
        retained_order = sum(incident)
        upper_twice = retained_order - odd + len(cert["barrier"])
        if 2 * match_count[component_id] != upper_twice:
            raise ValueError("matching size does not meet its Tutte--Berge upper bound")
        total_vertices += retained_order
        total_edges += len(cert["retained_input_indices"])

    # Even a parallel nonrepresentative cannot be silently substituted in this
    # certificate format.  Scan once globally, not once per input component.
    if any(chosen and not retained_global[index] for index, chosen in enumerate(selected)):
        raise ValueError("matching record is not a retained representative")
    report.update({
        "optimality_verified": True,
        "checked_components": len(components),
        "retained_vertices": total_vertices,
        "retained_edges": total_edges,
    })
    return report


def main() -> None:
    if not __debug__:
        raise SystemExit("Run this mathematical checker without -O or PYTHONOPTIMIZE.")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", help="input graph JSON")
    parser.add_argument("result", help="solver result JSON")
    parser.add_argument("--feasibility-only", action="store_true", help="check edge validity only; does not certify optimality")
    args = parser.parse_args()
    try:
        graph = json.loads(Path(args.input).read_text(encoding="utf-8"))
        result = json.loads(Path(args.result).read_text(encoding="utf-8"))
        if not isinstance(graph, dict) or "n" not in graph or "edges" not in graph:
            raise ValueError("input must be an object containing n and edges")
        report = verify_result(graph["n"], graph["edges"], result, graph.get("edge_ids"), require_certificate=not args.feasibility_only)
    except (OSError, TypeError, ValueError) as error:
        parser.error(str(error))
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
