#!/usr/bin/env python3
"""Construct a certified exact matching kernel for mixed native failures.

Input graphs must be simple and loopless: native edge failures cannot be
silently normalized.  A supplied vertex cover is optional.  The default
cover is the endpoints of a deterministic greedy maximal matching.

The kernel keeps at most (f+2)c vertices for a cover of size c, and at most
(f+3)nu(G) with the default cover.  Its certificate is a c+f-neighbor edge
kernel followed by consecutive maximum crossing matchings with disjoint
right endpoint sets.  Each maximum matching has a same-size vertex cover;
verify_failure_kernel.py checks the universal guarantee without a solver.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys
from typing import Iterable

from matching import _bipartite_barrier, _hopcroft_karp, _input_records


def build_failure_kernel(
    n: int,
    edges: Iterable[tuple[int, int]],
    failure_budget: int,
    edge_ids: Iterable[int | str] | None = None,
    *,
    cover: Iterable[int] | None = None,
) -> dict:
    """Return a fixed subgraph and a certificate for all permitted failures.

    Arbitrarily many cover vertices or cover-internal edges may be deleted.
    At most ``failure_budget`` outside vertices and crossing edges may be
    deleted in total.  In particular this includes every mixed native
    vertex/edge failure set of that total size.
    """
    if type(failure_budget) is not int or failure_budget < 0:
        raise ValueError("failure_budget must be a nonnegative integer")
    native, labels, simple = _input_records(n, edges, edge_ids)
    if len(simple) != len(native):
        raise ValueError("failure kernels require a simple loopless input graph")

    covered = [False] * n
    greedy_indices: list[int] | None = None
    if cover is None:
        greedy_indices = []
        for u, v, index in simple:
            if not covered[u] and not covered[v]:
                covered[u] = covered[v] = True
                greedy_indices.append(index)
    else:
        for u in cover:
            if type(u) is not int or not 0 <= u < n or covered[u]:
                raise ValueError("cover must contain distinct vertices in 0,...,n-1")
            covered[u] = True
        if any(not covered[u] and not covered[v] for u, v, _ in simple):
            raise ValueError("the supplied cover does not cover every edge")
    cover_vertices = [u for u in range(n) if covered[u]]
    c = len(cover_vertices)

    # The clipped budget affects work counters only.  No graph has more
    # native objects than n+m, and no unused f-sized array is allocated.
    budget = min(failure_budget, n + len(simple))
    cutoff = c + budget
    outside_counts = [0] * n
    first: list[tuple[int, int, int]] = []
    used = covered.copy()
    for u, v, index in simple:
        keep = covered[u] and covered[v]
        if not keep:
            left = u if covered[u] else v
            if outside_counts[left] < cutoff:
                keep = True
                outside_counts[left] += 1
        if keep:
            first.append((u, v, index))
            used[u] = used[v] = True

    vertices = [u for u in range(n) if used[u]]
    compact = [-1] * n
    for index, u in enumerate(vertices):
        compact[u] = index
    side = [covered[u] for u in vertices]
    active = [not flag for flag in side]
    selected = side.copy()
    statistics: dict[str, int] = {}
    layers = []
    outside_count = sum(active)
    # If fewer than f+1 layers exist, all crossing edges are exhausted.
    # Stopping here avoids work proportional to a very large encoded f.
    for _ in range(min(budget + 1, outside_count)):
        adjacency: list[list[int]] = [[] for _ in vertices]
        for u, v, _ in first:
            if covered[u] == covered[v]:
                continue
            a, b = (compact[u], compact[v]) if covered[u] else (compact[v], compact[u])
            if active[b]:
                adjacency[a].append(b)
                adjacency[b].append(a)
        mate = _hopcroft_karp(adjacency, side, statistics=statistics)
        if not any(mate[u] != -1 for u in range(len(vertices)) if side[u]):
            break
        minimum_cover = _bipartite_barrier(adjacency, mate, side, statistics)
        matching_indices = []
        for u, v, index in first:
            if covered[u] != covered[v] and mate[compact[u]] == compact[v]:
                matching_indices.append(index)
        right = [u for u in range(len(vertices)) if not side[u] and mate[u] != -1]
        layers.append({
            "matching_input_indices": matching_indices,
            "minimum_cover": [vertices[u] for u in minimum_cover],
        })
        for u in right:
            active[u] = False
            selected[u] = True
        if not any(active):
            break

    kept = [(u, v, index) for u, v, index in first
            if selected[compact[u]] and selected[compact[v]]]
    output_vertices = [u for u in vertices if selected[compact[u]]]
    statistics.update({
        "cover_vertices": c,
        "edge_kernel_vertices": len(vertices),
        "edge_kernel_edges": len(first),
        "retained_vertices": len(output_vertices),
        "retained_edges": len(kept),
        "layers": len(layers),
    })
    return {
        "schema_version": 1,
        "kind": "mixed-failure-matching-kernel",
        "n": n,
        "failure_budget": failure_budget,
        "cover": cover_vertices,
        "vertices": output_vertices,
        "edges": [{"input_index": index, "id": labels[index],
                   "u": native[index][0], "v": native[index][1]}
                  for _, _, index in kept],
        "certificate": {
            "greedy_matching_input_indices": greedy_indices,
            "edge_kernel_input_indices": [index for _, _, index in first],
            "layers": layers,
        },
        "statistics": statistics,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", nargs="?", default="-", help="graph JSON; - reads stdin")
    parser.add_argument("--failures", type=int, required=True, help="nonnegative failure budget")
    args = parser.parse_args()
    try:
        source = sys.stdin.read() if args.input == "-" else Path(args.input).read_text(encoding="utf-8")
        graph = json.loads(source)
        if not isinstance(graph, dict) or "n" not in graph or "edges" not in graph:
            raise ValueError("input must contain n and edges")
        result = build_failure_kernel(graph["n"], graph["edges"], args.failures,
                                      graph.get("edge_ids"), cover=graph.get("cover"))
    except (OSError, TypeError, ValueError) as error:
        parser.error(str(error))
    json.dump(result, sys.stdout, indent=2, ensure_ascii=False)
    sys.stdout.write("\n")


if __name__ == "__main__":
    main()
