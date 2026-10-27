"""Exact rational activation-matrix certificates for vertex-color failures.
Copyright 2026 Yilin Liu. Authored by GPT-6 Astra Pro.
SPDX-License-Identifier: Apache-2.0
"""
from dataclasses import dataclass
from fractions import Fraction


@dataclass(frozen=True)
class Edge:
    u: int
    v: int
    weight: int | Fraction


class _DSU:
    def __init__(self, size):
        self.parent = list(range(size))
        self.size = [1] * size

    def root(self, x):
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def join(self, u, v):
        u, v = self.root(u), self.root(v)
        if u == v:
            return False
        if self.size[u] < self.size[v]:
            u, v = v, u
        self.parent[v] = u
        self.size[u] += self.size[v]
        return True


@dataclass(frozen=True)
class Certificate:
    colors: tuple[int, ...]
    records: tuple[tuple[int, Edge], ...]
    failures: int
    support_bound: int

    def forest(self, failed_colors=()):
        """Return canonical MSF original IDs, using only retained records."""
        failed = tuple(failed_colors)
        if (any(type(c) is not int or c < 0 for c in failed)
                or len(set(failed)) != len(failed) or len(failed) > self.failures):
            raise ValueError("invalid color-failure set or budget exceeded")
        failed = frozenset(failed)
        dsu = _DSU(len(self.colors))
        return tuple(i for i, edge in self.records
                     if self.colors[edge.u] not in failed
                     and self.colors[edge.v] not in failed
                     and dsu.join(edge.u, edge.v))


def build(colors, edges, failures):
    """Construct the componentwise sharp fixed-order vertex-color certificate.

    Original IDs are input positions. Self-loops are ignored; parallel edges
    remain distinct. Costs must be exact integers/Fractions and may be signed.
    Colors are explicit nonnegative integer IDs, including unused large IDs.
    """
    colors = tuple(colors)
    if type(failures) is not int or failures < 0:
        raise ValueError("failures must be a nonnegative integer")
    if any(type(c) is not int or c < 0 for c in colors):
        raise ValueError("colors must be nonnegative integer IDs")
    n = len(colors)
    records = []
    components = _DSU(n)
    for i, edge in enumerate(edges):
        if (not isinstance(edge, Edge) or type(edge.u) is not int or type(edge.v) is not int
                or not 0 <= edge.u < n or not 0 <= edge.v < n
                or type(edge.weight) not in (int, Fraction)):
            raise ValueError("invalid edge endpoints or inexact weight")
        if edge.u != edge.v:
            record = Edge(edge.u, edge.v, Fraction(edge.weight))
            records.append((i, record))
            components.join(edge.u, edge.v)
    groups = {}
    for v in range(n):
        groups.setdefault(components.root(v), []).append(v)
    positions, dimensions, bases = {}, {}, {}
    support_bound = 0
    for root, vertices in groups.items():
        k = min(failures + 1, len({colors[v] for v in vertices}))
        dimensions[root] = k
        positions.update({v: i for i, v in enumerate(vertices)})
        bases[root] = {}
        support_bound += len(vertices) * k - k * (k + 1) // 2
    codes = {c: i + 1 for i, c in enumerate(sorted(set(colors)))}
    retained = []
    for i, edge in sorted(records, key=lambda pair: (pair[1].weight, pair[0])):
        root = components.root(edge.u)
        k = dimensions[root]
        column = [Fraction(0)] * (len(groups[root]) * k)
        for j in range(k):
            column[positions[edge.u] * k + j] = Fraction(codes[colors[edge.v]] ** j)
            column[positions[edge.v] * k + j] = -Fraction(codes[colors[edge.u]] ** j)
        basis = bases[root]
        for pivot, row in sorted(basis.items()):
            factor = column[pivot]
            if factor:
                column = [a - factor * b for a, b in zip(column, row)]
        pivot = next((j for j, value in enumerate(column) if value), None)
        if pivot is not None:
            divisor = column[pivot]
            basis[pivot] = [x / divisor for x in column]
            retained.append((i, edge))
    assert len(retained) <= support_bound
    return Certificate(colors, tuple(retained), failures, support_bound)
