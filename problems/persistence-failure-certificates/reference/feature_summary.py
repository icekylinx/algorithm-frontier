#!/usr/bin/env python3
"""Exact reference constructions for evaluation-rank failure summaries.

The implementation supports Q and a caller-supplied prime field. It does not
construct finite-field extensions. The checker independently expands small
feature matrices and enumerates failure/prefix queries.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from math import comb
from typing import Iterable, Sequence


class Field:
    """Exact arithmetic; modulus is None or a supplied prime."""

    def __init__(self, modulus: int | None = None):
        if modulus is not None and modulus < 2:
            raise ValueError("the supplied prime must be at least two")
        self.modulus = modulus
        self.zero = self.value(0)
        self.one = self.value(1)

    def value(self, x):
        if self.modulus is None:
            return Fraction(x)
        x = Fraction(x)
        return x.numerator * pow(x.denominator, -1, self.modulus) % self.modulus

    def add(self, x, y):
        return x + y if self.modulus is None else (x + y) % self.modulus

    def sub(self, x, y):
        return x - y if self.modulus is None else (x - y) % self.modulus

    def mul(self, x, y):
        return x * y if self.modulus is None else x * y % self.modulus

    def inv(self, x):
        if not x:
            raise ZeroDivisionError
        return 1 / x if self.modulus is None else pow(x, -1, self.modulus)


class Echelon:
    """Row space with earliest-coordinate pivots and no probabilistic tests."""

    def __init__(self, width: int, field: Field):
        self.width = width
        self.field = field
        self.rows: dict[int, list] = {}

    def insert(self, vector: Sequence) -> bool:
        if len(vector) != self.width:
            raise ValueError("inconsistent vector width")
        f = self.field
        row = [f.value(x) for x in vector]
        for pivot in sorted(self.rows):
            if row[pivot]:
                multiplier = row[pivot]
                basis_row = self.rows[pivot]
                for j in range(pivot, self.width):
                    row[j] = f.sub(row[j], f.mul(multiplier, basis_row[j]))
        pivot = next((j for j, x in enumerate(row) if x), None)
        if pivot is None:
            return False
        inverse = f.inv(row[pivot])
        self.rows[pivot] = [f.mul(x, inverse) for x in row]
        return True

    @property
    def rank(self) -> int:
        return len(self.rows)

    @property
    def pivots(self) -> tuple[int, ...]:
        return tuple(sorted(self.rows))


@dataclass
class ModuleBasis:
    vectors: list[list]
    degrees: list[int]
    pivots: tuple[int, ...]
    initial_rank: int
    candidates: int
    expanded: int

    @property
    def rank(self) -> int:
        return len(self.vectors)


def evaluation_module(initial_rows: Sequence[Sequence],
                      coordinate_rows: Sequence[Sequence], degree: int,
                      field: Field) -> ModuleBasis:
    """Generate only independent products, in nondecreasing total degree.

    Initial rows need not be independent in this reference function; all of
    them are counted in candidates. With independent initial rows, the count
    is exactly r + d * expanded, and expanded = dim(W_{degree-1}).
    """
    if degree < 0:
        raise ValueError("negative degree")
    rows = list(initial_rows)
    if not rows:
        return ModuleBasis([], [], (), 0, 0, 0)
    width = len(rows[0])
    if any(len(row) != width for row in rows):
        raise ValueError("inconsistent evaluation widths")
    # Every strictly growing degree increases rank, which is at most width.
    # Capping makes all queue bookkeeping independent of a huge encoded h.
    degree = min(degree, width)
    echelon = Echelon(width, field)
    vectors: list[list] = []
    degrees: list[int] = []
    candidates = 0
    for row in rows:
        candidates += 1
        original = [field.value(x) for x in row]
        if echelon.insert(original):
            vectors.append(original)
            degrees.append(0)
    initial_rank = len(vectors)
    if not initial_rank:
        return ModuleBasis([], [], (), 0, candidates, 0)
    coords = [[field.value(x) for x in row] for row in coordinate_rows]
    if any(len(row) != width for row in coords):
        raise ValueError("inconsistent evaluation widths")
    next_index = 0
    expanded = 0
    while next_index < len(vectors):
        index = next_index
        next_index += 1
        if degrees[index] == degree:
            continue
        expanded += 1
        for coordinate in coords:
            candidates += 1
            candidate = [field.mul(x, y)
                         for x, y in zip(vectors[index], coordinate)]
            if echelon.insert(candidate):
                vectors.append(candidate)
                degrees.append(degrees[index] + 1)
    return ModuleBasis(vectors, degrees, echelon.pivots, initial_rank,
                       candidates, expanded)


def independent_row_indices(rows: Sequence[Sequence], field: Field) -> tuple[int, ...]:
    """Select independent original rows by scanning matrix columns."""
    if not rows:
        return ()
    width = len(rows[0])
    if any(len(row) != width for row in rows):
        raise ValueError("ragged matrix")
    echelon = Echelon(len(rows), field)
    for e in range(width):
        echelon.insert([row[e] for row in rows])
    return echelon.pivots


def _order(size: int, order: Sequence[int] | None) -> list[int]:
    result = list(range(size)) if order is None else list(order)
    if sorted(result) != list(range(size)):
        raise ValueError("order must be a permutation of element IDs")
    return result


def _label_points(labels: Sequence[Iterable[int]], field: Field) -> dict:
    universe = sorted(set().union(*(set(x) for x in labels))) if labels else []
    if field.modulus is not None and field.modulus <= len(universe):
        raise ValueError("the supplied field needs distinct nonzero label points")
    return {label: field.value(i + 1) for i, label in enumerate(universe)}


def _multiply_linear(coefficients: Sequence, constant, linear, field: Field) -> list:
    result = [field.zero] * (len(coefficients) + 1)
    for j, x in enumerate(coefficients):
        result[j] = field.add(result[j], field.mul(constant, x))
        result[j + 1] = field.add(result[j + 1], field.mul(linear, x))
    return result


def monic_label_coefficients(labels: Sequence[Iterable[int]], field: Field) -> list[list]:
    """Coefficient rows b_0,...,b_{d-1}; the dummy point is zero."""
    labels = [set(x) for x in labels]
    points = _label_points(labels, field)
    degree = max(map(len, labels), default=0)
    rows = [[] for _ in range(degree)]
    for item in labels:
        coefficients = [field.one]
        for label in sorted(item):
            coefficients = _multiply_linear(
                coefficients, field.sub(field.zero, points[label]), field.one, field)
        for _ in range(degree - len(item)):
            coefficients = _multiply_linear(coefficients, field.zero, field.one, field)
        for j in range(degree):
            rows[j].append(coefficients[j])
    return rows


def normalized_label_coefficients(labels: Sequence[Iterable[int]], field: Field) -> list[list]:
    """Rows b_1,...,b_a of product (1-T/x_label), padded with zeros."""
    labels = [set(x) for x in labels]
    points = _label_points(labels, field)
    degree = max(map(len, labels), default=0)
    rows = [[] for _ in range(degree)]
    for item in labels:
        coefficients = [field.one]
        for label in sorted(item):
            coefficients = _multiply_linear(
                coefficients, field.one,
                field.sub(field.zero, field.inv(points[label])), field)
        coefficients.extend([field.zero] * (degree + 1 - len(coefficients)))
        for j in range(degree):
            rows[j].append(coefficients[j + 1])
    return rows


def represented_summary(columns: Sequence[Sequence], labels: Sequence[Iterable[int]],
                        failures: int, modulus: int | None = None,
                        order: Sequence[int] | None = None) -> dict:
    """Original IDs of the canonical basis of the conceptual tensor lift."""
    if failures < 0 or len(columns) != len(labels):
        raise ValueError("invalid failure budget or label count")
    labels = [frozenset(item) for item in labels]
    f = Field(modulus)
    ids = _order(len(columns), order)
    if not columns:
        return {"retained": [], "rank": 0, "original_rank": 0,
                "formal_rows": 0, "candidates": 0}
    dimension = len(columns[0])
    if any(len(col) != dimension for col in columns):
        raise ValueError("inconsistent column dimensions")
    rows = [[f.value(columns[e][i]) for e in ids] for i in range(dimension)]
    selected_rows = independent_row_indices(rows, f)
    initial = [rows[i] for i in selected_rows]
    coords = monic_label_coefficients([labels[e] for e in ids], f)
    universe = set().union(*(set(x) for x in labels))
    failures = min(failures, len(universe))
    module = evaluation_module(initial, coords, failures, f)
    return {"retained": [ids[j] for j in module.pivots], "rank": module.rank,
            "original_rank": len(selected_rows), "candidates": module.candidates,
            "expanded": module.expanded, "degrees": module.degrees,
            "formal_rows": len(selected_rows) * comb(failures + len(coords), len(coords))}


def boundary_matrix(vertices: int, top_simplices: Sequence[Sequence[int]],
                    field: Field) -> tuple[list[tuple[int, ...]], list[list]]:
    """Oriented simplicial boundary, including exactly its potentially nonzero rows."""
    simplices = [tuple(simplex) for simplex in top_simplices]
    if simplices:
        dimension = len(simplices[0])
        if dimension < 2:
            raise ValueError("top dimension must be at least one")
        if any(len(s) != dimension or tuple(sorted(set(s))) != s or
               any(v < 0 or v >= vertices for v in s) for s in simplices):
            raise ValueError("simplices must be sorted vertex tuples of one dimension")
        if len(set(simplices)) != len(simplices):
            raise ValueError("duplicate top simplices")
    faces = sorted({s[:j] + s[j + 1:] for s in simplices for j in range(len(s))})
    face_index = {face: i for i, face in enumerate(faces)}
    rows = [[field.zero] * len(simplices) for _ in faces]
    for e, s in enumerate(simplices):
        for j in range(len(s)):
            rows[face_index[s[:j] + s[j + 1:]]][e] = field.value((-1) ** j)
    return faces, rows


def boundary_row_basis(vertices: int, top_simplices: Sequence[Sequence[int]],
                       field: Field) -> tuple[list[tuple[int, ...]], tuple[int, ...]]:
    """Select original boundary rows with one m-coordinate column at a time.

    The facet index is combinatorial data. Field workspace is one column
    plus at most r echelon columns; no m by N boundary matrix is stored.
    """
    simplices = [tuple(simplex) for simplex in top_simplices]
    if simplices:
        dimension = len(simplices[0])
        if dimension < 2:
            raise ValueError("top dimension must be at least one")
        if any(len(s) != dimension or tuple(sorted(set(s))) != s or
               any(v < 0 or v >= vertices for v in s) for s in simplices):
            raise ValueError("simplices must be sorted vertex tuples of one dimension")
        if len(set(simplices)) != len(simplices):
            raise ValueError("duplicate top simplices")
    faces = sorted({s[:j] + s[j + 1:] for s in simplices for j in range(len(s))})
    face_index = {face: i for i, face in enumerate(faces)}
    echelon = Echelon(len(faces), field)
    for simplex in simplices:
        column = [field.zero] * len(faces)
        for j in range(len(simplex)):
            column[face_index[simplex[:j] + simplex[j + 1:]]] = field.value((-1) ** j)
        echelon.insert(column)
    return faces, echelon.pivots


def persistence_summary(vertices: int, top_simplices: Sequence[Sequence[int]],
                        labels: Sequence[Iterable[int]], failures: int,
                        modulus: int | None = None,
                        order: Sequence[int] | None = None) -> dict:
    """Intrinsic-feature-rank construction with no extra top-simplex labels.

    The full original lower skeleton is implicitly retained. The reference
    requires a prime larger than vertices and the label count; the manuscript
    gives the general extension-field implementation.
    """
    if vertices < 0 or len(labels) != vertices or failures < 0:
        raise ValueError("invalid vertex labels or failure budget")
    labels = [frozenset(item) for item in labels]
    f = Field(modulus)
    if modulus is not None and modulus <= vertices:
        raise ValueError("the supplied field needs n+1 distinct shift candidates")
    ids = _order(len(top_simplices), order)
    faces, selected_rows = boundary_row_basis(vertices, top_simplices, f)
    rank = len(selected_rows)
    coords = normalized_label_coefficients(labels, f)
    universe = set().union(*(set(x) for x in labels)) if labels else set()
    failures = min(failures, len(universe))
    module = evaluation_module([[f.one] * vertices] if vertices else [],
                               coords, failures, f)
    shifted = []
    for i, row in enumerate(module.vectors):
        shift = f.zero
        if i:
            # Candidate shifts are the distinct field values 0,...,n.
            # Mark their exact indices instead of relying on hash-table
            # membership for the deterministic comparison bound.
            blocked = [False] * (vertices + 1)
            for x in row:
                negative = f.sub(f.zero, x)
                if f.modulus is None:
                    if negative.denominator != 1:
                        continue
                    candidate = negative.numerator
                else:
                    candidate = negative
                if 0 <= candidate <= vertices:
                    blocked[candidate] = True
            shift = f.value(next(c for c, is_blocked in enumerate(blocked)
                                 if not is_blocked))
        shifted.append([f.add(x, shift) for x in row])
    selected_faces = {faces[row]: i for i, row in enumerate(selected_rows)}
    echelon = Echelon(rank * module.rank, f)
    retained = []
    for e in ids:
        if not rank:
            break
        simplex = tuple(top_simplices[e])
        column = [f.zero] * (rank * module.rank)
        for j, vertex in enumerate(simplex):
            facet = simplex[:j] + simplex[j + 1:]
            if facet not in selected_faces:
                continue
            row = selected_faces[facet]
            sign = f.value((-1) ** j)
            for i, feature in enumerate(shifted):
                column[i * rank + row] = f.mul(sign, feature[vertex])
        if echelon.insert(column):
            retained.append(e)
    return {"retained": retained, "rank": len(retained), "original_rank": rank,
            "feature_rank": module.rank, "feature_candidates": module.candidates,
            "feature_degrees": module.degrees, "feature_rows": module.vectors,
            "shifted_rows": shifted, "selected_original_rows": selected_rows,
            "formal_features": comb(failures + len(coords), len(coords))}
