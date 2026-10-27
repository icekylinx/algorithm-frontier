"""Exact whole-coset compilation in one common finite wreath product.

The wreath-subgroup construction is established algebra; this is a new local
implementation for original-item constraint evaluation and verification.
Copyright 2026 Yilin Liu. Authored by GPT-6 Astra Pro. Apache-2.0.
"""
from dataclasses import dataclass
from fractions import Fraction


@dataclass(frozen=True)
class Group:
    table: tuple
    identity: int = 0

    def __post_init__(self):
        table = tuple(tuple(row) for row in self.table)
        n, e = len(table), self.identity
        if (not n or type(e) is not int or not 0 <= e < n
                or any(len(row) != n for row in table)
                or any(type(v) is not int or not 0 <= v < n for row in table for v in row)):
            raise ValueError('invalid finite multiplication table')
        if any(table[e][v] != v or table[v][e] != v for v in range(n)):
            raise ValueError('invalid identity')
        inverse = []
        for v in range(n):
            u = next((u for u in range(n) if table[u][v] == e == table[v][u]), None)
            if u is None:
                raise ValueError('missing inverse')
            inverse.append(u)
        for x in range(n):
            for y in range(n):
                for z in range(n):
                    if table[table[x][y]][z] != table[x][table[y][z]]:
                        raise ValueError('nonassociative multiplication')
        object.__setattr__(self, 'table', table)
        object.__setattr__(self, 'inverse', tuple(inverse))

    def element(self, g):
        if type(g) is not int or not 0 <= g < len(self.table):
            raise ValueError('invalid original group element')
        return g

    def generated(self, generators):
        generators = tuple(self.element(g) for g in generators)
        steps = tuple(dict.fromkeys(generators + tuple(self.inverse[g] for g in generators)))
        reached, queue = {self.identity}, [self.identity]
        for x in queue:
            for g in steps:
                y = self.table[x][g]
                if y not in reached:
                    reached.add(y); queue.append(y)
        return frozenset(reached)

    def wreath_element(self, element):
        if (type(element) is not tuple or len(element) != 3
                or type(element[2]) is not int or element[2] not in (0, 1)):
            raise ValueError('wreath elements are (x, y, parity) tuples')
        return self.element(element[0]), self.element(element[1]), element[2]

    def wreath_multiply(self, left, right):
        x, y, parity = self.wreath_element(left)
        u, v, bit = self.wreath_element(right)
        if parity:
            u, v = v, u
        return self.table[x][u], self.table[y][v], parity ^ bit

    def query(self, g):
        g = self.element(g)
        return g, self.inverse[g], 1


@dataclass(frozen=True)
class Coset:
    anchor: int
    generators: tuple[int, ...]


@dataclass(frozen=True)
class CompiledItem:
    original: int
    anchor: int | None
    subgroup: frozenset
    group: Group

    def accepts_original(self, g):
        g = self.group.element(g)
        if self.anchor is None:
            return False
        return self.group.table[self.group.inverse[self.anchor]][g] in self.subgroup

    def contains(self, element):
        x, y, bit = self.group.wreath_element(element)
        group, a = self.group, self.anchor
        e = group.identity
        if a is None:
            return (x, y, bit) == (e, e, 0)
        inv, table, h = group.inverse[a], group.table, self.subgroup
        if bit:
            return table[inv][x] in h and table[y][a] in h
        return table[table[inv][x]][a] in h and y in h

    def generators(self):
        group, a = self.group, self.anchor
        e = group.identity
        if a is None:
            return ()
        inverse = group.inverse[a]
        return tuple((group.table[group.table[a][h]][inverse], e, 0) for h in sorted(self.subgroup)) + tuple((e, h, 0) for h in sorted(self.subgroup)) + ((a, inverse, 1),)


def compile_cosets(group, items):
    """None denotes an empty accepting set; every other item is a Coset.

    All output items use the SAME implicit wreath group. Original positions
    and whole predicates are retained; this routine does not sample items.
    """
    if type(group) is not Group:
        raise ValueError('validated Group required')
    result = []
    for i, item in enumerate(items):
        if item is None:
            result.append(CompiledItem(i, None, frozenset(), group))
        elif type(item) is Coset:
            anchor = group.element(item.anchor)
            result.append(CompiledItem(i, anchor, group.generated(item.generators), group))
        else:
            raise ValueError('Coset or None required')
    return tuple(result)


def verify_coefficients(group, items, weights, coefficients, epsilon, exact_total=False):
    """Exact explicit-query check of whole-original-item relative approximation.

    Recompile from original predicates; never trust a supplied compiled item.
    Optional exact_total includes even identically-zero predicate items.
    """
    try:
        compiled = compile_cosets(group, items)
        weights, coefficients = tuple(weights), tuple(coefficients)
        if len(weights) != len(compiled) or len(coefficients) != len(compiled):
            return False
        if (type(exact_total) is not bool or type(epsilon) not in (int, Fraction)
                or not 0 <= epsilon < 1
                or any(type(x) not in (int, Fraction) or x < 0 for x in weights + coefficients)):
            return False
        if exact_total and sum(w*c for w,c in zip(weights,coefficients)) != sum(weights):
            return False
        for g in range(len(group.table)):
            original = sum(w for item,w in zip(compiled,weights) if not item.accepts_original(g))
            reduced = sum(w*c for item,w,c in zip(compiled,weights,coefficients) if not item.contains(group.query(g)))
            if not (1-epsilon)*original <= reduced <= (1+epsilon)*original:
                return False
        return True
    except (TypeError, ValueError, AttributeError, IndexError):
        return False
