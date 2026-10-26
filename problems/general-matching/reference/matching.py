#!/usr/bin/env python3
"""Deterministic, unconditional maximum-cardinality matching reference solver.

This is an ordinary polynomial-time Edmonds blossom implementation.  It does
not implement or inherit the manuscript's faster research backend.  Native
input records may contain loops, parallel edges, and user-supplied edge IDs.

Normal mode: O(n + m log(m+2) + sum_i k_i**3) operations.
Certificate mode has the same bound, with O(sum_i k_i**2) extra operations.
Here k_i is the retained kernel vertex count in original component i.
Storage is O(n+m), apart from the input/output label bytes.  Integer vertex
indices and IDs are charged by their representation size; see README.md.

Run ``python3 matching.py graph.json --certificate`` for JSON output.
Only the Python standard library is required.
"""

from __future__ import annotations

import argparse
import json
import sys
from collections import deque
from pathlib import Path
from typing import Iterable


def _input_records(
    n: int,
    edges: Iterable[tuple[int, int]],
    edge_ids: Iterable[int | str] | None,
) -> tuple[list[tuple[int, int]], list[int | str], list[tuple[int, int, int]]]:
    if type(n) is not int or n < 0:
        raise ValueError("n must be a nonnegative integer")
    native: list[tuple[int, int]] = []
    sortable: list[tuple[int, int, int]] = []
    for index, edge in enumerate(edges):
        if not isinstance(edge, (list, tuple)) or len(edge) != 2:
            raise ValueError(f"edge {index} must contain exactly two vertices")
        u, v = edge
        if type(u) is not int or type(v) is not int or not (0 <= u < n and 0 <= v < n):
            raise ValueError(f"edge {index} has a vertex outside 0,...,n-1")
        native.append((u, v))
        if u != v:
            sortable.append((min(u, v), max(u, v), index))

    labels = list(range(len(native))) if edge_ids is None else list(edge_ids)
    if len(labels) != len(native):
        raise ValueError("edge_ids must have one entry per input edge record")
    if any(type(label) not in (int, str) for label in labels):
        raise ValueError("edge IDs must be integers or strings (not booleans)")
    ordered_labels = sorted((0 if type(label) is int else 1, label) for label in labels)
    if any(a == b for a, b in zip(ordered_labels, ordered_labels[1:])):
        raise ValueError("edge IDs must be distinct")

    # Comparison sorting gives an explicit deterministic bound, without a
    # worst-case constant-time hash-table assumption.  The first native record
    # of each unordered nonloop pair supplies the public output identifier.
    sortable.sort()
    simple: list[tuple[int, int, int]] = []
    previous = (-1, -1)
    for u, v, index in sortable:
        if (u, v) != previous:
            simple.append((u, v, index))
            previous = (u, v)
    simple.sort(key=lambda edge: edge[2])
    return native, labels, simple


def _components(
    n: int, edges: list[tuple[int, int, int]]
) -> tuple[list[list[int]], list[list[tuple[int, int, int]]]]:
    adjacency: list[list[int]] = [[] for _ in range(n)]
    for u, v, _ in edges:
        adjacency[u].append(v)
        adjacency[v].append(u)
    component_of = [-1] * n
    vertices: list[list[int]] = []
    for root in range(n):
        if component_of[root] != -1 or not adjacency[root]:
            continue
        component = len(vertices)
        component_of[root] = component
        queue = deque([root])
        members: list[int] = []
        while queue:
            u = queue.popleft()
            members.append(u)
            for v in adjacency[u]:
                if component_of[v] == -1:
                    component_of[v] = component
                    queue.append(v)
        members.sort()
        vertices.append(members)
    records: list[list[tuple[int, int, int]]] = [[] for _ in vertices]
    for edge in edges:
        records[component_of[edge[0]]].append(edge)
    return vertices, records


def _kernel(
    vertices: list[int],
    edges: list[tuple[int, int, int]],
    index_of: list[int],
    use_kernel: bool,
) -> tuple[list[int], list[list[int]], list[tuple[int, int, int]], list[int]]:
    for index, vertex in enumerate(vertices):
        index_of[vertex] = index
    covered = [False] * len(vertices)
    for u, v, _ in edges:
        a, b = index_of[u], index_of[v]
        if not covered[a] and not covered[b]:
            covered[a] = covered[b] = True
    cover = [vertex for vertex in vertices if covered[index_of[vertex]]]
    cutoff = len(cover)
    outside_kept = [0] * len(vertices)
    kept: list[tuple[int, int, int]] = []
    incident = [False] * len(vertices)
    for u, v, native_index in edges:
        a, b = index_of[u], index_of[v]
        keep = not use_kernel or (covered[a] and covered[b])
        if not keep:
            cover_end = a if covered[a] else b
            if not covered[cover_end]:
                raise RuntimeError("greedy matching failed to produce a vertex cover")
            if outside_kept[cover_end] < cutoff:
                keep = True
                outside_kept[cover_end] += 1
        if keep:
            kept.append((u, v, native_index))
            incident[a] = incident[b] = True
    compact = [vertex for vertex in vertices if incident[index_of[vertex]]]
    for index, vertex in enumerate(compact):
        index_of[vertex] = index
    adjacency: list[list[int]] = [[] for _ in compact]
    for u, v, _ in kept:
        a, b = index_of[u], index_of[v]
        adjacency[a].append(b)
        adjacency[b].append(a)
    return compact, adjacency, kept, cover


def _blossom(
    adjacency: list[list[int]],
    *,
    excluded: int = -1,
    statistics: dict[str, int] | None = None,
) -> list[int]:
    """Array-based Edmonds search on a simple graph; -1 denotes a free vertex.

    ``excluded`` is treated as an isolated vertex.  Ordinary solving and
    certificate extraction leave this diagnostic parameter at its default.
    No search-state flags are interpreted as an optimality certificate.
    """
    size = len(adjacency)
    mate = [-1] * size
    if statistics is not None:
        statistics["matching_calls"] += 1

    # A deterministic maximal matching saves searches on easy components.
    for u in range(size):
        if u == excluded or mate[u] != -1:
            continue
        for v in adjacency[u]:
            if v != excluded and mate[v] == -1:
                mate[u], mate[v] = v, u
                break

    def search(root: int) -> bool:
        parent = [-1] * size
        base = list(range(size))
        outer = [False] * size
        outer[root] = True
        queue = deque([root])

        def common_base(a: int, b: int) -> int:
            seen = [False] * size
            while True:
                a = base[a]
                seen[a] = True
                if mate[a] == -1:
                    break
                a = parent[mate[a]]
                if a == -1:
                    raise RuntimeError("broken alternating-tree ancestry")
            while True:
                b = base[b]
                if seen[b]:
                    return b
                if mate[b] == -1 or parent[mate[b]] == -1:
                    raise RuntimeError("outer vertices have no common root")
                b = parent[mate[b]]

        def mark_branch(a: int, blossom_base: int, toward: int, marked: list[bool]) -> None:
            while base[a] != blossom_base:
                partner = mate[a]
                if partner == -1:
                    raise RuntimeError("a blossom branch reached a free nonbase vertex")
                marked[base[a]] = marked[base[partner]] = True
                parent[a] = toward
                toward = partner
                a = parent[partner]
                if a == -1:
                    raise RuntimeError("a blossom branch left its alternating tree")

        while queue:
            u = queue.popleft()
            for v in adjacency[u]:
                if v == excluded or base[u] == base[v] or mate[u] == v:
                    continue
                if v == root or (mate[v] != -1 and parent[mate[v]] != -1):
                    blossom_base = common_base(u, v)
                    marked = [False] * size
                    mark_branch(u, blossom_base, v, marked)
                    mark_branch(v, blossom_base, u, marked)
                    for w in range(size):
                        if marked[base[w]]:
                            base[w] = blossom_base
                            if not outer[w]:
                                outer[w] = True
                                queue.append(w)
                    if statistics is not None:
                        statistics["blossom_contractions"] += 1
                elif parent[v] == -1:
                    parent[v] = u
                    if mate[v] == -1:
                        # Rewritten parent links already expand the relevant
                        # alternating routes through every contracted blossom.
                        endpoint = v
                        while endpoint != -1:
                            predecessor = parent[endpoint]
                            if predecessor == -1:
                                raise RuntimeError("augmenting path has no predecessor")
                            following = mate[predecessor]
                            mate[endpoint] = predecessor
                            mate[predecessor] = endpoint
                            endpoint = following
                        if statistics is not None:
                            statistics["augmentations"] += 1
                        return True
                    outer[mate[v]] = True
                    queue.append(mate[v])
        return False

    for root in range(size):
        if root != excluded and mate[root] == -1:
            search(root)
    return mate


def _matching_size(mate: list[int]) -> int:
    return sum(u < v for u, v in enumerate(mate))


def _odd_components(adjacency: list[list[int]], removed: list[bool]) -> int:
    seen = removed.copy()
    count = 0
    for root in range(len(adjacency)):
        if seen[root]:
            continue
        seen[root] = True
        stack = [root]
        order = 0
        while stack:
            u = stack.pop()
            order += 1
            for v in adjacency[u]:
                if not seen[v]:
                    seen[v] = True
                    stack.append(v)
        count += order % 2
    return count


def _failed_search_forest(
    adjacency: list[list[int]],
    mate: list[int],
    statistics: dict[str, int] | None = None,
) -> tuple[list[bool], list[int], list[int]]:
    """Exhaust one alternating forest rooted at all exposed vertices.

    ``mate`` must be maximum and is never modified.  Every original member
    of an outer blossom is marked outer.  The returned outer, base and
    parent arrays have the explicit invariants proved in the companion
    certificate proof; they are not incidental flags from a prior search.
    """
    order = len(adjacency)
    parent = [-1] * order
    base = list(range(order))
    outer = [partner == -1 for partner in mate]
    owner = [vertex if outer[vertex] else -1 for vertex in range(order)]
    queue = deque(vertex for vertex in range(order) if outer[vertex])
    if statistics is not None:
        statistics["certificate_searches"] += 1

    def common_base(a: int, b: int) -> int:
        seen = [False] * order
        while True:
            a = base[a]
            seen[a] = True
            if mate[a] == -1:
                break
            a = parent[mate[a]]
            if a == -1:
                raise RuntimeError("broken certificate-tree ancestry")
        while True:
            b = base[b]
            if seen[b]:
                return b
            if mate[b] == -1 or parent[mate[b]] == -1:
                raise RuntimeError("certificate branches have no common root")
            b = parent[mate[b]]

    def mark_branch(a: int, ancestor: int, toward: int, marked: list[bool]) -> None:
        while base[a] != ancestor:
            partner = mate[a]
            if partner == -1:
                raise RuntimeError("a certificate blossom reached a nonbase root")
            marked[base[a]] = marked[base[partner]] = True
            parent[a] = toward
            toward = partner
            a = parent[partner]
            if a == -1:
                raise RuntimeError("a certificate blossom left its tree")

    while queue:
        u = queue.popleft()
        for v in adjacency[u]:
            if base[u] == base[v] or mate[u] == v:
                continue
            if outer[v]:
                if owner[u] != owner[v]:
                    raise RuntimeError("an augmenting path joins certificate roots; matching is not maximum")
                ancestor = common_base(u, v)
                marked = [False] * order
                mark_branch(u, ancestor, v, marked)
                mark_branch(v, ancestor, u, marked)
                for vertex in range(order):
                    if marked[base[vertex]]:
                        base[vertex] = ancestor
                        owner[vertex] = owner[ancestor]
                        if not outer[vertex]:
                            outer[vertex] = True
                            queue.append(vertex)
                if statistics is not None:
                    statistics["blossom_contractions"] += 1
            elif parent[v] == -1:
                if mate[v] == -1 or outer[mate[v]]:
                    raise RuntimeError("invalid matching or certificate-tree labels")
                parent[v] = u
                owner[v] = owner[mate[v]] = owner[u]
                outer[mate[v]] = True
                queue.append(mate[v])
    return outer, base, parent


def _barrier(
    adjacency: list[list[int]], mate: list[int], statistics: dict[str, int]
) -> list[int]:
    """Return a tight odd-component barrier in O(k**2) additional work.

    An exhausted forest has b=|I|+f odd outer blocks, where I is its inner
    set and f the number of exposed roots.  Unreached vertices are perfectly
    matched and N(outer) minus outer equals I.  Thus odd(H-I)=b, proving the
    required equality directly.  The final equality is also checked here.
    """
    order = len(adjacency)
    size = _matching_size(mate)
    if 2 * size == order - _odd_components(adjacency, [False] * order):
        return []
    outer, _, parent = _failed_search_forest(adjacency, mate, statistics)
    barrier = [vertex for vertex in range(order) if not outer[vertex] and parent[vertex] != -1]
    removed = [False] * order
    for vertex in barrier:
        removed[vertex] = True
    for vertex, neighbors in enumerate(adjacency):
        if not outer[vertex] and any(outer[neighbor] for neighbor in neighbors) != removed[vertex]:
            raise RuntimeError("certificate outer-neighbor and inner sets differ")
    if 2 * size != order - _odd_components(adjacency, removed) + len(barrier):
        raise RuntimeError("the extracted barrier does not certify this matching")
    return barrier


def maximum_matching(
    n: int,
    edges: Iterable[tuple[int, int]],
    edge_ids: Iterable[int | str] | None = None,
    *,
    use_kernel: bool = True,
    certificate: bool = False,
) -> dict:
    """Return an exact maximum matching as original edge IDs and input indices.

    Vertices are 0,...,n-1.  ``edges`` contains pairs; loops are ignored and
    parallel records are represented by their earliest input occurrence.
    IDs default to input indices and, when supplied, must be distinct ints
    or strings.  ``certificate=True`` adds a separately checkable optimality
    certificate with O(sum_i k_i**2) extra work after the cubic solve.
    """
    if type(use_kernel) is not bool or type(certificate) is not bool:
        raise ValueError("use_kernel and certificate must be booleans")
    native, labels, simple = _input_records(n, edges, edge_ids)
    components, records = _components(n, simple)
    index_of = [-1] * n
    statistics = {
        "input_vertices": n,
        "input_records": len(native),
        "simple_edges": len(simple),
        "nonempty_components": len(components),
        "kernel_vertices": 0,
        "kernel_edges": 0,
        "matching_calls": 0,
        "certificate_searches": 0,
        "blossom_contractions": 0,
        "augmentations": 0,
    }
    selected: list[int] = []
    certified_components: list[dict] = []
    for vertices, component_edges in zip(components, records):
        compact, adjacency, kept, cover = _kernel(vertices, component_edges, index_of, use_kernel)
        statistics["kernel_vertices"] += len(compact)
        statistics["kernel_edges"] += len(kept)
        mate = _blossom(adjacency, statistics=statistics)
        for u, v, native_index in kept:
            if mate[index_of[u]] == index_of[v]:
                selected.append(native_index)
        if certificate:
            barrier = _barrier(adjacency, mate, statistics)
            certified_components.append({
                "root": vertices[0],
                "cover": cover,
                "retained_input_indices": [index for _, _, index in kept],
                "barrier": [compact[index] for index in barrier],
            })
    selected.sort()
    answer = {
        "cardinality": len(selected),
        "matching": [
            {"input_index": index, "id": labels[index], "u": native[index][0], "v": native[index][1]}
            for index in selected
        ],
        "statistics": statistics,
    }
    if certificate:
        answer["certificate"] = {
            "format": "algorithm-frontier-matching-v1",
            "components": certified_components,
        }
    return answer


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", nargs="?", default="-", help="graph JSON file; - reads stdin")
    parser.add_argument("--certificate", action="store_true", help="emit a verifiable optimality certificate (same cubic bound)")
    parser.add_argument("--no-kernel", action="store_true", help="solve full normalized components")
    args = parser.parse_args()
    try:
        source = sys.stdin.read() if args.input == "-" else Path(args.input).read_text(encoding="utf-8")
        graph = json.loads(source)
        if not isinstance(graph, dict) or "n" not in graph or "edges" not in graph:
            raise ValueError("input must be an object containing n and edges")
        result = maximum_matching(
            graph["n"], graph["edges"], graph.get("edge_ids"),
            use_kernel=not args.no_kernel, certificate=args.certificate,
        )
    except (OSError, TypeError, ValueError) as error:
        parser.error(str(error))
    json.dump(result, sys.stdout, indent=2, ensure_ascii=False)
    sys.stdout.write("\n")


if __name__ == "__main__":
    main()
