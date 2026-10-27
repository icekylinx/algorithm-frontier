"""Exact rational whole-item incidence-label compiler and decoder.

Copyright 2026 Yilin Liu. Authored by GPT-6 Astra Pro.
SPDX-License-Identifier: Apache-2.0

This is the deterministic algebraic interface, not a quotient sampler. The
default dimension gate returns FULL_INPUT before materializing a large lift.
Original item IDs, selected original row IDs and their labels are preserved.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as Q
from itertools import combinations_with_replacement
from math import comb
from pathlib import Path
import importlib.util
import sys


_name = "_algorithm_frontier_exact_features"
if _name not in sys.modules:
    _path = (Path(__file__).resolve().parents[2]
             / "persistence-failure-certificates/reference/feature_summary.py")
    _spec = importlib.util.spec_from_file_location(_name, _path)
    _module = importlib.util.module_from_spec(_spec)
    sys.modules[_name] = _module
    _spec.loader.exec_module(_module)
_features = sys.modules[_name]


def rational(value):
    if type(value) not in (int, Q):
        raise ValueError("matrix entries and weights must be exact integers/Fractions")
    return Q(value)


def labels(values):
    values = frozenset(values)
    if any(type(x) is not int or x < 0 for x in values):
        raise ValueError("labels must be nonnegative original integer IDs")
    return values


def _inverse(matrix):
    n = len(matrix)
    rows = [list(row) + [Q(i == j) for j in range(n)]
            for i, row in enumerate(matrix)]
    for j in range(n):
        pivot = next((i for i in range(j, n) if rows[i][j]), None)
        if pivot is None:
            raise ValueError("singular compression minor")
        rows[j], rows[pivot] = rows[pivot], rows[j]
        scale = rows[j][j]
        rows[j] = [x / scale for x in rows[j]]
        for i in range(n):
            if i != j:
                scale = rows[i][j]
                rows[i] = [x - scale * y for x, y in zip(rows[i], rows[j])]
    return tuple(tuple(row[n:]) for row in rows)


def _compression(rows, selected):
    """Return C with A=C(PA), retaining the original selected row IDs."""
    r = len(selected)
    if not r:
        return tuple(() for _ in rows)
    width = len(rows[0])
    independent = _features.Echelon(r, _features.Field())
    columns = []
    for j in range(width):
        if independent.insert([rows[i][j] for i in selected]):
            columns.append(j)
    inverse = _inverse(tuple(tuple(rows[i][j] for j in columns) for i in selected))
    return tuple(tuple(sum((row[columns[t]] * inverse[t][j] for t in range(r)), Q(0))
                       for j in range(r)) for row in rows)


def _monomials(variables, degree):
    for indices in combinations_with_replacement(range(variables), degree):
        exponent = [0] * variables
        for i in indices:
            exponent[i] += 1
        yield tuple(exponent)


def _polynomial(difference, points, h, k):
    """Ordinary monomial coefficients of p_T; dummy point zero gives l_0=z_0."""
    initial = (k - len(difference),) + (0,) * h
    coefficients = {initial: Q(1)}
    for label in sorted(difference):
        powers = [points[label] ** j for j in range(h + 1)]
        output = {}
        for exponent, coefficient in coefficients.items():
            for j, power in enumerate(powers):
                term = list(exponent)
                term[j] += 1
                term = tuple(term)
                output[term] = output.get(term, Q(0)) + coefficient * power
        coefficients = output
    return coefficients


def _contains(space, vector):
    residual = list(vector)
    for pivot in sorted(space.rows):
        scale = residual[pivot]
        if scale:
            residual = [x - scale * y for x, y in zip(residual, space.rows[pivot])]
    return not any(residual)


@dataclass(frozen=True)
class Compilation:
    mode: str  # LIFT, FULL_INPUT, ZERO
    blocks: tuple
    row_labels: tuple
    item_labels: tuple
    weights: tuple
    failures: int
    effective_failures: int
    deficit: int
    selected_rows: tuple
    compression: tuple
    points: dict
    feature_count: int
    dimension: int
    monomials: tuple
    lifted: tuple | None

    @property
    def rank(self):
        return len(self.selected_rows)

    @property
    def original_ids(self):
        return tuple(range(len(self.blocks)))

    def _failed(self, failed):
        raw = tuple(failed)
        checked = labels(raw)
        if len(raw) != len(checked) or len(checked) > self.failures:
            raise ValueError("repeated failures or failure budget exceeded")
        # Unused original label IDs have no effect, but count toward the budget.
        return checked & self.points.keys()

    def _evaluation(self, failed):
        failed = self._failed(failed)
        coefficients = [Q(1)]
        # q_F(t) = product(1-t/alpha_f); its value at dummy point zero is one.
        for label in sorted(failed):
            result = [Q(0)] * (len(coefficients) + 1)
            for j, value in enumerate(coefficients):
                result[j] += value
                result[j + 1] -= value / self.points[label]
            coefficients = result
        coefficients += [Q(0)] * (self.effective_failures + 1 - len(coefficients))
        evaluations = {label: sum((value * point ** j
                                  for j, value in enumerate(coefficients)), Q(0))
                       for label, point in self.points.items()}
        return tuple(coefficients), evaluations

    def scalars(self, failed=()):
        """One exact scalar per original item, common to all its columns."""
        _, evaluations = self._evaluation(failed)
        return tuple(_product(evaluations[label] for label in item)
                     for item in self.item_labels)

    def decoder(self, failed=()):
        """Explicit C T_F matrix; FULL_INPUT has no materialized lift."""
        if self.mode == "FULL_INPUT":
            raise ValueError("dimension gate returned input without materializing a lift")
        theta, evaluations = self._evaluation(failed)
        evaluation = tuple(_product(theta[j] ** power
                                    for j, power in enumerate(exponent))
                           for exponent in self.monomials)
        row_factors = tuple(_product(evaluations[label] for label in self.row_labels[i])
                            for i in self.selected_rows)
        return tuple(tuple(coefficient * row_factors[j] * x
                           for j, coefficient in enumerate(row) for x in evaluation)
                     for row in self.compression)

    def decode(self, failed=()):
        """Apply C T_F to every lifted column; returns original-dimensional vectors."""
        matrix = self.decoder(failed)
        return tuple(tuple(tuple(sum((a * b for a, b in zip(row, column)), Q(0))
                                 for row in matrix) for column in block)
                     for block in self.lifted)

    def rank_on(self, item_ids):
        """Exact integer rank oracle on original item IDs for a future sampler."""
        if self.mode == "FULL_INPUT":
            raise ValueError("no lifted rank oracle was materialized")
        ids = tuple(item_ids)
        if (len(ids) != len(set(ids))
                or any(type(i) is not int or not 0 <= i < len(self.blocks) for i in ids)):
            raise ValueError("invalid original item IDs")
        echelon = _features.Echelon(self.dimension, _features.Field())
        for i in ids:
            for column in self.lifted[i]:
                echelon.insert(column)
        return echelon.rank

    def value(self, subspace=(), failed=(), weights=None):
        """Whole-block subspace-complement objective, charging each item once.

        LIFT evaluates the compiled preimage. FULL_INPUT uses the exact
        surviving original items. Caller-supplied weights are original-ID
        indexed; their approximation quality is not certified by this API.
        """
        space = _features.Echelon(len(self.row_labels), _features.Field())
        for column in subspace:
            column = tuple(rational(x) for x in column)
            space.insert(column)
        weights = self.weights if weights is None else tuple(rational(x) for x in weights)
        if len(weights) != len(self.blocks) or any(x < 0 for x in weights):
            raise ValueError("invalid nonnegative original-item reweighting")
        if self.mode == "FULL_INPUT":
            failed = self._failed(failed)
            return sum((weight for item, block, weight
                        in zip(self.item_labels, self.blocks, weights)
                        if not item & failed and any(not _contains(space, c) for c in block)), Q(0))
        return sum((weight for block, weight in zip(self.decode(failed), weights)
                    if any(not _contains(space, column) for column in block)), Q(0))


def _product(values):
    result = Q(1)
    for value in values:
        result *= value
    return result


def compile_blocks(blocks, row_labels, item_labels, failures, weights=None, deficit=None):
    """Compile explicit rational blocks or return exact whole-input fallback.

    Each block is a tuple of original column vectors; all its columns carry
    one original item-label set. On nonzero incidences, row labels must be a
    subset of item labels. An optional deficit is checked, then replaced by
    the maximum actual deficit. Positive-rank lifts of dimension >= item
    count are never materialized. No sparsification or sampling is performed.
    """
    if type(failures) is not int or failures < 0:
        raise ValueError("invalid failure budget")
    if deficit is not None and (type(deficit) is not int or deficit < 0):
        raise ValueError("invalid incidence deficit bound")
    row_labels = tuple(labels(item) for item in row_labels)
    item_labels = tuple(labels(item) for item in item_labels)
    n = len(row_labels)
    blocks = tuple(tuple(tuple(rational(x) for x in column) for column in block)
                   for block in blocks)
    if len(item_labels) != len(blocks) or any(len(c) != n for b in blocks for c in b):
        raise ValueError("inconsistent block dimensions or item-label count")
    weights = ((Q(1),) * len(blocks) if weights is None
               else tuple(rational(x) for x in weights))
    if len(weights) != len(blocks) or any(x < 0 for x in weights):
        raise ValueError("invalid nonnegative original weights")
    actual_deficit = 0
    for block, item in zip(blocks, item_labels):
        for column in block:
            for i, value in enumerate(column):
                if value:
                    if not row_labels[i] <= item:
                        raise ValueError("nonzero incidence omits a row label")
                    actual_deficit = max(actual_deficit, len(item - row_labels[i]))
    if deficit is not None and actual_deficit > deficit:
        raise ValueError("actual incidence deficit exceeds supplied bound")
    universe = sorted(set().union(*item_labels)) if item_labels else []
    points = {label: Q(i + 1) for i, label in enumerate(universe)}
    h, k = min(failures, len(universe)), actual_deficit
    columns = tuple(c for b in blocks for c in b)
    rows = tuple(tuple(c[i] for c in columns) for i in range(n))
    selected = _features.independent_row_indices(rows, _features.Field())
    r = len(selected)
    features = comb(h + k, k)
    dimension = r * features
    common = dict(blocks=blocks, row_labels=row_labels, item_labels=item_labels,
                  weights=weights, failures=failures, effective_failures=h,
                  deficit=k, selected_rows=selected, points=points,
                  feature_count=features, dimension=dimension)
    if r and dimension >= len(blocks):
        return Compilation(mode="FULL_INPUT", compression=(), monomials=(),
                           lifted=None, **common)
    compression = _compression(rows, selected)
    if not r:
        return Compilation(mode="ZERO", compression=compression, monomials=(),
                           lifted=tuple(tuple(() for _ in b) for b in blocks), **common)
    monomials = tuple(_monomials(h + 1, k))
    cache = {}
    output = []
    for block, item in zip(blocks, item_labels):
        lifted = []
        for column in block:
            vector = []
            for i in selected:
                if not column[i]:
                    vector.extend([Q(0)] * features)
                    continue
                difference = item - row_labels[i]
                if difference not in cache:
                    coefficients = _polynomial(difference, points, h, k)
                    cache[difference] = tuple(coefficients.get(e, Q(0)) for e in monomials)
                vector.extend(column[i] * coefficient for coefficient in cache[difference])
            lifted.append(tuple(vector))
        output.append(tuple(lifted))
    return Compilation(mode="LIFT", compression=compression, monomials=monomials,
                       lifted=tuple(output), **common)
