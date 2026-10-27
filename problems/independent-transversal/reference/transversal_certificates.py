"""Search-free certificates for independent transversals and constellations.

Copyright 2026 Yilin Liu. Authored by GPT-6 Astra Pro.
SPDX-License-Identifier: Apache-2.0
"""
from dataclasses import dataclass


@dataclass(frozen=True)
class Transversal:
    vertices: tuple[int, ...]


@dataclass(frozen=True)
class Constellation:
    classes: tuple[int, ...]
    stars: tuple[tuple[int, tuple[int, ...]], ...]


def instance(classes, edges):
    classes = tuple(tuple(group) for group in classes)
    n = sum(map(len, classes))
    flat = [v for group in classes for v in group]
    if (any(not group for group in classes)
            or any(type(v) is not int or not 0 <= v < n for v in flat)
            or len(set(flat)) != n):
        raise ValueError('nonempty classes must partition original vertex IDs')
    owner = [None] * n
    for i, group in enumerate(classes):
        for v in group:
            owner[v] = i
    adjacent = [set() for _ in range(n)]
    for edge in edges:
        if len(edge) != 2:
            raise ValueError('undirected pairs required')
        u, v = edge
        if type(u) is not int or type(v) is not int or not 0 <= u < n or not 0 <= v < n or u == v:
            raise ValueError('invalid loopless original edge')
        if owner[u] != owner[v]:
            adjacent[u].add(v)
            adjacent[v].add(u)
    return classes, owner, adjacent


def _ids(values, limit):
    return (type(values) is tuple and all(type(v) is int and 0 <= v < limit for v in values)
            and len(set(values)) == len(values))


def verify(classes, edges, witness):
    """Verify the elementary exact alternative, never run a search.

    A constellation is a domination witness, not proof of nonexistence of a
    transversal. Within-class edges are removed for the constellation check.
    """
    try:
        classes, owner, adjacent = instance(classes, edges)
        q, n = len(classes), len(owner)
        if type(witness) is Transversal:
            vertices = witness.vertices
            if not _ids(vertices, n) or len(vertices) != q or len({owner[v] for v in vertices}) != q:
                return False
            chosen = set(vertices)
            return all(not (adjacent[v] & chosen) for v in chosen)
        if type(witness) is not Constellation or not _ids(witness.classes, q) or not witness.classes:
            return False
        if type(witness.stars) is not tuple or not witness.stars:
            return False
        selected_classes = set(witness.classes)
        all_vertices, leaves, expected = set(), [], {}
        for star in witness.stars:
            if type(star) is not tuple or len(star) != 2:
                return False
            center, group = star
            if type(center) is not int or not 0 <= center < n or not _ids(group, n) or not group:
                return False
            vertices = {center, *group}
            if len(vertices) != len(group)+1 or all_vertices & vertices:
                return False
            if any(owner[v] not in selected_classes for v in vertices):
                return False
            all_vertices.update(vertices)
            leaves.extend(group)
            expected[center] = set(group)
            for v in group:
                expected[v] = {center}
        if (len(leaves) != len(selected_classes)-1
                or len({owner[v] for v in leaves}) != len(leaves)
                or len(all_vertices) > 2*(len(selected_classes)-1)):
            return False
        if any(adjacent[v] & all_vertices != expected[v] for v in all_vertices):
            return False
        return all(adjacent[v] & all_vertices for i in selected_classes for v in classes[i])
    except (TypeError, ValueError, AttributeError, IndexError):
        return False
