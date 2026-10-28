"""Exact rational product-feature restrictions; original item IDs are never merged.

Copyright 2026 icekylinx. Authored by GPT-6 Astra Pro.
SPDX-License-Identifier: Apache-2.0
"""
from dataclasses import dataclass
from fractions import Fraction
from itertools import combinations


@dataclass(frozen=True)
class Item:
    support: tuple[int, ...]
    cost: Fraction | int
    labels: tuple[tuple[int, ...], ...] = ()


@dataclass(frozen=True)
class Summary:
    retained: tuple[int, ...]
    dimension_bound: int  # Saturated at the number of input items.
    gated: bool
    feature_rank: int | None  # None means features were not constructed.
    resource_rank: int | None


def _integer(value):
    if type(value) is not int or value < 0:
        raise ValueError("expected a nonnegative integer")
    return value


def _rational(value):
    if type(value) not in (int, Fraction):
        raise ValueError("costs and resource entries must be exact integers or Fractions")
    return Fraction(value)


def _set(values):
    values = tuple(values)
    for x in values:
        _integer(x)
    if len(set(values)) != len(values):
        raise ValueError("duplicate support or label entry")
    return tuple(sorted(values))


class _Basis:
    def __init__(self):
        self.rows = {}

    def insert(self, vector):
        vector = list(map(Fraction, vector))
        for pivot, row in sorted(self.rows.items()):
            if vector[pivot]:
                scale = vector[pivot]
                vector = [a - scale * b for a, b in zip(vector, row)]
        pivot = next((i for i, x in enumerate(vector) if x), None)
        if pivot is None:
            return False
        scale = vector[pivot]
        self.rows[pivot] = [x / scale for x in vector]
        return True


def _det(matrix):
    matrix = [list(map(Fraction, row)) for row in matrix]
    result = Fraction(1)
    for j in range(len(matrix)):
        pivot = next((i for i in range(j, len(matrix)) if matrix[i][j]), None)
        if pivot is None:
            return Fraction(0)
        if pivot != j:
            matrix[j], matrix[pivot] = matrix[pivot], matrix[j]
            result = -result
        value = matrix[j][j]
        result *= value
        for i in range(j + 1, len(matrix)):
            scale = matrix[i][j] / value
            for k in range(j + 1, len(matrix)):
                matrix[i][k] -= scale * matrix[j][k]
    return result


def _exponents(dimension, degree):
    # Avoid recursion-depth dependence on explicit list size.
    stack = [((), degree)]
    while stack:
        prefix, remaining = stack.pop()
        if len(prefix) == dimension:
            yield prefix
        else:
            for power in range(remaining, -1, -1):
                stack.append((prefix + (power,), remaining - power))


def _label_feature(labels, codes, degree, exponents):
    coefficients = [1]
    for root in [codes[x] for x in labels] + [0] * (degree - len(labels)):
        new = [0] * (len(coefficients) + 1)
        for i, value in enumerate(coefficients):
            new[i] -= root * value
            new[i + 1] += value
        coefficients = new
    output = []
    for powers in exponents:
        value = 1
        for c, power in zip(coefficients[:-1], powers):
            value *= c ** power
        output.append(value)
    return output


def _binomial_capped(n, k, cap):
    k = min(k, n - k)
    result = 1
    for i in range(1, k + 1):
        result = result * (n - k + i) // i
        if result >= cap:
            return cap
    return result


def summarize(items, cardinality, universe_failures=0, label_failures=(),
              resource_columns=None):
    """Return original item IDs preserving all allowed fixed-cost queries.

    Label IDs and universe IDs are nonnegative integers; only explicitly
    occurring IDs matter. Cost ties use input positions. Resource columns
    represent the full original resource over Q, not a query contraction.
    Output does not optimize a later extension or enumerate failure queries.
    """
    cardinality = _integer(cardinality)
    universe_failures = _integer(universe_failures)
    budgets = tuple(_integer(x) for x in label_failures)
    items = tuple(Item(_set(x.support), _rational(x.cost),
                       tuple(_set(labels) for labels in x.labels)) for x in items)
    if any(len(x.labels) != len(budgets) for x in items):
        raise ValueError("each item must supply one label list per failure budget")
    n = len(items)
    resource = None
    rank = None
    if resource_columns is not None:
        resource = tuple(tuple(_rational(x) for x in c) for c in resource_columns)
        if len(resource) != n or len({len(c) for c in resource}) > 1:
            raise ValueError("resource matrix must have one equal-length column per item")
        rows = tuple(zip(*resource))
        basis = _Basis()
        selected = [row for row in rows if basis.insert(row)]
        rank = len(selected)
        resource = tuple(tuple(row[i] for row in selected) for i in range(n))
    if not n or not cardinality or rank == 0:
        return Summary((), 0, False, 0, rank)
    cardinality = min(cardinality, n)
    universe = sorted({x for item in items for x in item.support})
    universe_failures = min(universe_failures, len(universe))
    p = max(1, max(len(x.support) for x in items))
    t = p * cardinality + universe_failures
    palettes = [sorted({label for item in items for label in item.labels[j]})
                for j in range(len(budgets))]
    budgets = tuple(min(h, len(palette)) for h, palette in zip(budgets, palettes))
    degrees = [max(len(item.labels[j]) for item in items) for j in range(len(budgets))]
    dimension = rank if rank is not None else 1
    dimension = min(n, dimension * _binomial_capped(t, p, n))
    for h, d in zip(budgets, degrees):
        dimension = min(n, dimension * _binomial_capped(h + d, d, n))
    if dimension >= n:
        return Summary(tuple(range(n)), n, True, None, rank)
    # No exterior coordinates or coefficient monomials are listed before the gate.
    codes = {x: i + 1 for i, x in enumerate(universe)}
    next_dummy = len(universe) + 1
    padded = []
    for item in items:
        points = [codes[x] for x in item.support]
        points.extend(range(next_dummy, next_dummy + p - len(points)))
        next_dummy += p - len(item.support)
        padded.append(tuple(points))
    coordinates = tuple(combinations(range(t), p))
    label_codes = [{x: i + 1 for i, x in enumerate(palette)} for palette in palettes]
    monomials = [tuple(_exponents(d, h)) for d, h in zip(degrees, budgets)]
    basis = _Basis()
    retained = []
    for i in sorted(range(n), key=lambda i: (items[i].cost, i)):
        points = padded[i]
        vector = [_det([[x ** row for x in points] for row in rows])
                  for rows in coordinates]
        for j, d in enumerate(degrees):
            feature = _label_feature(items[i].labels[j], label_codes[j], d, monomials[j])
            vector = [a * b for a in vector for b in feature]
        if resource is not None:
            vector = [a * b for a in resource[i] for b in vector]
        assert len(vector) == dimension
        if basis.insert(vector):
            retained.append(i)
    return Summary(tuple(retained), dimension, False, len(retained), rank)
