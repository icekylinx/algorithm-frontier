#!/usr/bin/env python3
"""Deterministic, unconditional maximum-cardinality matching reference solver.

This ordinary polynomial-time solver uses Hopcroft--Karp on bipartite
retained graphs and Edmonds blossom otherwise.  It does not implement or
inherit the manuscript's faster research backend.  Native input records may
contain loops, parallel edges, and user-supplied edge IDs.

Default modes: O(n + m log(m+2) + sum_i nu_i**p_i), including certificates,
where nu_i is the maximum matching size of original component i (not an
input), and p_i is 5/2 if its first kernel is bipartite and 3 otherwise.
Without kernels, bipartite components cost O((n_i+m_i)*sqrt(nu_i+1));
other components retain the ordinary cubic component-vertex bound.
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


def _bipartition(adjacency: list[list[int]]) -> list[bool] | None:
    """Return a deterministic left-side mask, or None after an odd conflict."""
    color = [-1] * len(adjacency)
    for root in range(len(adjacency)):
        if color[root] != -1:
            continue
        color[root] = 0
        queue = deque([root])
        while queue:
            u = queue.popleft()
            for v in adjacency[u]:
                if color[v] == -1:
                    color[v] = 1 - color[u]
                    queue.append(v)
                elif color[v] == color[u]:
                    return None
    return [value == 0 for value in color]


def _hopcroft_karp(
    adjacency: list[list[int]],
    left: list[bool],
    *,
    statistics: dict[str, int] | None = None,
) -> list[int]:
    """Exact bipartite matching in O((k+h)*sqrt(nu+1)) operations.

    Only adjacency lists on ``left`` are read.  A phase freezes its starting
    matching, takes a maximal set of vertex-disjoint shortest augmenting
    paths, and flips them.  Explicit DFS stacks avoid recursion-depth limits.
    Here nu is the unknown maximum matching size, not the vertex count.
    """
    order = len(adjacency)
    if len(left) != order:
        raise RuntimeError("bipartite side mask has the wrong length")
    left_vertices = [u for u in range(order) if left[u]]
    for u in left_vertices:
        if any(left[v] for v in adjacency[u]):
            raise RuntimeError("bipartite matching received a same-side edge")
    mate = [-1] * order
    if statistics is not None:
        statistics["hopcroft_karp_calls"] = statistics.get("hopcroft_karp_calls", 0) + 1
    while True:
        if statistics is not None:
            statistics["hopcroft_karp_bfs"] = statistics.get("hopcroft_karp_bfs", 0) + 1
        distance = [-1] * order
        queue: deque[int] = deque()
        for u in left_vertices:
            if mate[u] == -1:
                distance[u] = 0
                queue.append(u)
        terminal_level = order + 1
        while queue:
            u = queue.popleft()
            if distance[u] > terminal_level:
                continue
            for v in adjacency[u]:
                if v == mate[u]:
                    continue
                partner = mate[v]
                if partner == -1:
                    terminal_level = distance[u]
                elif distance[u] < terminal_level and distance[partner] == -1:
                    distance[partner] = distance[u] + 1
                    queue.append(partner)
        if terminal_level == order + 1:
            return mate
        if statistics is not None:
            statistics["hopcroft_karp_phases"] = statistics.get("hopcroft_karp_phases", 0) + 1
        phase_mate = mate.copy()
        cursor = [0] * order
        unavailable = [False] * order
        gains = 0
        for root in left_vertices:
            if phase_mate[root] != -1 or unavailable[root]:
                continue
            path_left = [root]
            path_right: list[int] = []
            found = False
            while path_left and not found:
                u = path_left[-1]
                while cursor[u] < len(adjacency[u]):
                    v = adjacency[u][cursor[u]]
                    cursor[u] += 1
                    if v == phase_mate[u] or unavailable[v]:
                        continue
                    partner = phase_mate[v]
                    if partner == -1:
                        if distance[u] != terminal_level:
                            continue
                        path_right.append(v)
                        for a, b in zip(path_left, path_right):
                            mate[a] = b
                            mate[b] = a
                            unavailable[a] = unavailable[b] = True
                        gains += 1
                        found = True
                        break
                    if (distance[u] < terminal_level
                            and distance[partner] == distance[u] + 1
                            and not unavailable[partner]):
                        path_right.append(v)
                        path_left.append(partner)
                        break
                else:
                    # A failed node stays dead: later paths only remove more
                    # vertices from this fixed layered graph.
                    unavailable[u] = True
                    path_left.pop()
                    if path_right:
                        path_right.pop()
        if gains == 0:
            raise RuntimeError("a reachable bipartite phase found no augmenting path")
        if statistics is not None:
            statistics["hopcroft_karp_augmentations"] = statistics.get("hopcroft_karp_augmentations", 0) + gains


def _bipartite_barrier(
    adjacency: list[list[int]],
    mate: list[int],
    left: list[bool],
    statistics: dict[str, int] | None = None,
) -> list[int]:
    """Return a minimum vertex cover, also a tight odd-component barrier."""
    order = len(adjacency)
    if len(mate) != order or len(left) != order:
        raise RuntimeError("bipartite certificate arrays have different lengths")
    for u, neighbors in enumerate(adjacency):
        if any(left[u] == left[v] for v in neighbors):
            raise RuntimeError("bipartite certificate received a same-side edge")
        v = mate[u]
        if v != -1 and (not 0 <= v < order or mate[v] != u or v not in neighbors):
            raise RuntimeError("bipartite certificate received an invalid matching")
    reached = [False] * order
    queue: deque[int] = deque()
    for u in range(order):
        if left[u] and mate[u] == -1:
            reached[u] = True
            queue.append(u)
    while queue:
        u = queue.popleft()
        for v in adjacency[u]:
            if v == mate[u] or reached[v]:
                continue
            reached[v] = True
            partner = mate[v]
            if partner == -1:
                raise RuntimeError("bipartite certificate found an augmenting path")
            if not reached[partner]:
                reached[partner] = True
                queue.append(partner)
    barrier = [u for u in range(order) if left[u] != reached[u]]
    removed = [False] * order
    for u in barrier:
        removed[u] = True
    if (len(barrier) != _matching_size(mate)
            or any(not removed[u] and not removed[v]
                   for u, neighbors in enumerate(adjacency) for v in neighbors)):
        raise RuntimeError("bipartite cover does not certify this matching")
    if statistics is not None:
        statistics["bipartite_certificate_searches"] = statistics.get("bipartite_certificate_searches", 0) + 1
    return barrier


def _compress_cover(
    adjacency: list[list[int]], cover: list[bool],
    *, statistics: dict[str, int] | None = None,
) -> tuple[list[int], list[list[int]]]:
    """Preserve all cover subsets using the right ends of a maximum crossing matching.

    The input is the already sparse c-neighbor kernel, with k=O(c**2)
    vertices and h=O(c**2) edges.  The crossing matching has size at most c,
    so Hopcroft--Karp costs O((k+h)*sqrt(c+1))=O(c**(5/2)).  The induced
    output has at most 2c vertices.
    """
    order = len(adjacency)
    crossing: list[list[int]] = [[] for _ in range(order)]
    for u, neighbors in enumerate(adjacency):
        if cover[u]:
            crossing[u] = [v for v in neighbors if not cover[v]]
        elif any(not cover[v] for v in neighbors):
            raise RuntimeError("compression requires a vertex cover")
    crossing_mate = _hopcroft_karp(crossing, cover, statistics=statistics)
    retained = [u for u in range(order) if cover[u] or crossing_mate[u] != -1]
    index_of = [-1] * order
    for index, u in enumerate(retained):
        index_of[u] = index
    reduced: list[list[int]] = [
        [index_of[v] for v in adjacency[u] if index_of[v] != -1]
        for u in retained
    ]
    return retained, reduced


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
    """Return a tight barrier in O(h+k*(nu+1)) additional work.

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
    certificate within the same componentwise time bound.  ``use_kernel``
    enables both the c-neighbor edge kernel and crossing-endpoint compression.
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
        "cover_vertices": 0,
        "solver_vertices": 0,
        "blossom_vertices": 0,
        "bipartite_vertices": 0,
        "bipartite_components": 0,
        "hopcroft_karp_calls": 0,
        "hopcroft_karp_phases": 0,
        "hopcroft_karp_bfs": 0,
        "hopcroft_karp_augmentations": 0,
        "matching_calls": 0,
        "certificate_searches": 0,
        "bipartite_certificate_searches": 0,
        "blossom_contractions": 0,
        "augmentations": 0,
    }
    selected: list[int] = []
    certified_components: list[dict] = []
    for vertices, component_edges in zip(components, records):
        compact, adjacency, kept, cover = _kernel(vertices, component_edges, index_of, use_kernel)
        statistics["kernel_vertices"] += len(compact)
        statistics["kernel_edges"] += len(kept)
        statistics["cover_vertices"] += len(cover)
        left = _bipartition(adjacency)
        if use_kernel:
            covered = [False] * len(compact)
            for vertex in cover:
                covered[index_of[vertex]] = True
            solve_vertices, solve_adjacency = _compress_cover(adjacency, covered, statistics=statistics)
        else:
            solve_vertices, solve_adjacency = list(range(len(compact))), adjacency
        statistics["solver_vertices"] += len(solve_vertices)
        if left is None:
            statistics["blossom_vertices"] += len(solve_vertices)
            small_mate = _blossom(solve_adjacency, statistics=statistics)
        else:
            statistics["bipartite_vertices"] += len(solve_vertices)
            statistics["bipartite_components"] += 1
            statistics["matching_calls"] += 1
            small_mate = _hopcroft_karp(solve_adjacency, [left[u] for u in solve_vertices], statistics=statistics)
            statistics["augmentations"] += _matching_size(small_mate)
        mate = [-1] * len(compact)
        for u, v in enumerate(small_mate):
            if v != -1:
                mate[solve_vertices[u]] = solve_vertices[v]
        for u, v, native_index in kept:
            if mate[index_of[u]] == index_of[v]:
                selected.append(native_index)
        if certificate:
            barrier = (_barrier(adjacency, mate, statistics) if left is None
                       else _bipartite_barrier(adjacency, mate, left, statistics))
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
    parser.add_argument("--certificate", action="store_true", help="emit a verifiable optimality certificate (same componentwise bound)")
    parser.add_argument("--no-kernel", action="store_true", help="disable both compression stages; solve full normalized components")
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
