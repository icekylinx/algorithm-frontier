#!/usr/bin/env python3
"""Finite independent checks of the tree-segment reporting construction.

Checks every pair of labeled trees rooted at vertex zero on subsets of four vertices,
including unequal vertex sets, against explicit path intersections. It then
checks segment-level loop removal on short walks and a long discarded path.
The reference index uses the manuscript's sparse dyadic cells. No shortest-
path detector, raw-cycle backend, or dynamic time bound is certified here.
"""
from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from itertools import combinations, product


class Tree:
    def __init__(self, parent):
        self.parent = dict(parent)
        self.children = {v: [] for v in parent}
        for v, p in parent.items():
            if p is not None:
                self.children[p].append(v)
        self.tin, self.tout, self.depth = {}, {}, {}
        root = next(v for v, p in parent.items() if p is None)
        stack = [(root, 0, False)]
        while stack:
            v, depth, done = stack.pop()
            if done:
                self.tout[v] = len(self.tin) - 1
                continue
            self.tin[v] = len(self.tin)
            self.depth[v] = depth
            stack.append((v, depth, True))
            stack.extend((w, depth + 1, False) for w in sorted(self.children[v], reverse=True))

    def contains(self, a, b, v):
        return (
            v in self.parent
            and self.tin[a] <= self.tin[v] <= self.tin[b]
            and self.tout[v] >= self.tin[b]
        )

    def vertices(self, a, b):
        result = [b]
        while result[-1] != a:
            result.append(self.parent[result[-1]])
        return tuple(reversed(result))

    def paths(self):
        return tuple(
            (a, b) for a in self.parent for b in self.parent
            if self.tin[a] <= self.tin[b] <= self.tout[a]
        )


def trees_on(vertices):
    """Enumerate labeled trees by Prüfer words, then root each at zero."""
    if len(vertices) == 1:
        yield Tree({0: None})
        return
    for word in product(vertices, repeat=len(vertices) - 2):
        degree = {v: 1 for v in vertices}
        for v in word:
            degree[v] += 1
        adjacency = {v: [] for v in vertices}
        for v in word:
            leaf = min(w for w in vertices if degree[w] == 1)
            adjacency[v].append(leaf)
            adjacency[leaf].append(v)
            degree[v] -= 1
            degree[leaf] -= 1
        a, b = (v for v in vertices if degree[v] == 1)
        adjacency[a].append(b)
        adjacency[b].append(a)
        parent = {0: None}
        queue = deque([0])
        while queue:
            v = queue.popleft()
            for w in adjacency[v]:
                if w not in parent:
                    parent[w] = v
                    queue.append(w)
        yield Tree(parent)


def ancestors(value, universe):
    length = 1
    while length <= universe:
        yield value // length * length, length
        length *= 2


def dyadic_cover(low, high):
    while low <= high:
        length = low & -low if low else 1 << ((high - low + 1).bit_length() - 1)
        while low + length - 1 > high:
            length //= 2
        yield low, length
        low += length


class IntersectionIndex:
    def __init__(self, first, second):
        self.first, self.second = first, second
        self.universe = 1 << (max(len(first.parent), len(second.parent)) - 1).bit_length()
        self.cells = {}
        for v in first.parent.keys() & second.parent.keys():
            coordinates = (first.tin[v], first.tout[v], second.tin[v], second.tout[v])
            for cell in product(*(ancestors(x, self.universe) for x in coordinates)):
                previous = self.cells.get(cell)
                if previous is None:
                    self.cells[cell] = (v, v, v, v)
                else:
                    self.cells[cell] = self.combine(previous, (v, v, v, v))

    def combine(self, a, b):
        return (
            min((a[0], b[0]), key=lambda v: (self.first.depth[v], v)),
            max((a[1], b[1]), key=lambda v: (self.first.depth[v], v)),
            min((a[2], b[2]), key=lambda v: (self.second.depth[v], v)),
            max((a[3], b[3]), key=lambda v: (self.second.depth[v], v)),
        )

    def query(self, a, b, c, d):
        first, second = self.first, self.second
        intervals = (
            (first.tin[a], first.tin[b]), (first.tin[b], self.universe - 1),
            (second.tin[c], second.tin[d]), (second.tin[d], self.universe - 1),
        )
        result = None
        for cell in product(*(dyadic_cover(lo, hi) for lo, hi in intervals)):
            found = self.cells.get(cell)
            if found is not None:
                result = found if result is None else self.combine(result, found)
        return result


@dataclass(frozen=True)
class Piece:
    a: int
    b: int
    tree: Tree | None = None

    def contains(self, v):
        return v in (self.a, self.b) if self.tree is None else self.tree.contains(self.a, self.b, v)

    def rank(self, v):
        return int(v == self.b) if self.tree is None else self.tree.depth[v]

    def vertices(self):
        return (self.a, self.b) if self.tree is None else self.tree.vertices(self.a, self.b)


def last_intersection(new, old, indices):
    if new.tree is not None and old.tree is not None:
        key = (new.tree, old.tree)
        if key not in indices:
            indices[key] = IntersectionIndex(*key)
        answer = indices[key].query(new.a, new.b, old.a, old.b)
        return None if answer is None else answer[1]
    candidates = (new.a, new.b) if new.tree is None else (old.a, old.b)
    common = [v for v in candidates if new.contains(v) and old.contains(v)]
    return max(common, key=new.rank) if common else None


def remove_loops(pieces, source, indices):
    """The query never expands a piece until all segment deletions finish."""
    current = []
    endpoint = source
    for new in pieces:
        assert new.a == endpoint
        vertex, owner = endpoint, len(current) - 1
        for i, old in enumerate(current):
            candidate = last_intersection(new, old, indices)
            if candidate is not None and new.rank(candidate) > new.rank(vertex):
                vertex, owner = candidate, i
        if owner < 0:
            current = []
        else:
            old = current[owner]
            current = current[:owner]
            if old.a != vertex:
                current.append(Piece(old.a, vertex, old.tree))
        if vertex != new.b:
            current.append(Piece(vertex, new.b, new.tree))
        endpoint = new.b
    output, enumerated = [source], 0
    for piece in current:
        vertices = piece.vertices()
        assert vertices[0] == output[-1]
        output.extend(vertices[1:])
        enumerated += len(vertices) - 1
    return tuple(output), enumerated


def all_walks(source, length, n):
    if length == 0:
        yield (source,)
        return
    for tail in all_walks(source, length - 1, n):
        for vertex in range(n):
            if vertex != tail[-1]:
                yield (*tail, vertex)


def main():
    if not __debug__:
        raise SystemExit("This checker requires assertions; run Python without -O.")
    trees = [
        tree for count in range(4) for subset in combinations(range(1, 4), count)
        for tree in trees_on((0, *subset))
    ]
    indices, intersection_queries = {}, 0
    for first, second in product(trees, repeat=2):
        index = IntersectionIndex(first, second)
        indices[first, second] = index
        for (a, b), (c, d) in product(first.paths(), second.paths()):
            common = set(first.vertices(a, b)) & set(second.vertices(c, d))
            predicate = {
                v for v in first.parent.keys() & second.parent.keys()
                if first.contains(a, b, v) and second.contains(c, d, v)
            }
            assert predicate == common
            expected = None if not common else (
                min(common, key=first.depth.__getitem__), max(common, key=first.depth.__getitem__),
                min(common, key=second.depth.__getitem__), max(common, key=second.depth.__getitem__),
            )
            assert index.query(a, b, c, d) == expected
            intersection_queries += 1

    native_paths = {}
    for tree in trees:
        for a, b in tree.paths():
            native_paths.setdefault(tree.vertices(a, b), Piece(a, b, tree))
    walks_checked = 0
    for length in range(1, 6):
        for walk in all_walks(0, length, 4):
            for boundaries in range(1 << (length - 1)):
                pieces, start = [], 0
                for end in range(1, length + 1):
                    if end == length or boundaries & (1 << (end - 1)):
                        part = walk[start:end + 1]
                        if end - start == 1:
                            pieces.append(Piece(*part))
                        elif part in native_paths:
                            pieces.append(native_paths[part])
                        else:
                            break
                        start = end
                else:
                    output, enumerated = remove_loops(pieces, 0, indices)
                    assert output[0] == walk[0] and output[-1] == walk[-1]
                    assert len(set(output)) == len(output)
                    input_edges = list(zip(walk, walk[1:]))
                    output_edges = list(zip(output, output[1:]))
                    assert all(edge in input_edges for edge in output_edges)
                    # Include zero-cost edges, so positivity is not silently used.
                    cost = lambda e: (7 * e[0] + 3 * e[1]) % 5
                    assert sum(map(cost, output_edges)) <= sum(map(cost, input_edges))
                    assert enumerated == len(output_edges)
                    walks_checked += 1

    last = 10000
    long_tree = Tree({0: None, **{v: v - 1 for v in range(1, last + 1)}})
    pieces = [Piece(0, last, long_tree), Piece(last, 1), Piece(1, last + 1)]
    output, enumerated = remove_loops(pieces, 0, indices)
    assert output == (0, 1, last + 1) and enumerated == 2
    print(f"Intersection index: {len(trees)} tree versions rooted at zero; {intersection_queries} exact clipped-path queries.")
    print(f"Loop removal: {walks_checked} walk/segmentation cases, with nonnegative costs.")
    print("Discarded long path: 10002 represented edges, exactly 2 output edges enumerated.")
    print("PASS: finite tree-segment evidence; no raw detector or dynamic-backend certification.")


if __name__ == "__main__":
    main()
