#!/usr/bin/env python3
"""Independent finite checks for rank-dependent failure-summary construction.

The reference uses a product frontier and incremental echelon rows. This
checker explicitly enumerates small monomial matrices and uses separate
full Gaussian elimination, then enumerates original failure/prefix queries.
No numerical tolerance or randomized correctness test is used. Random seeds
only select reproducible finite examples.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
from itertools import combinations, product
from math import comb
from pathlib import Path
import random
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "reference"))
from feature_summary import (Field, evaluation_module, monic_label_coefficients,
                             normalized_label_coefficients, persistence_summary,
                             represented_summary)


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def value(x, modulus):
    x = Fraction(x)
    if modulus is None:
        return x
    return x.numerator * pow(x.denominator, -1, modulus) % modulus


def reduce_value(x, modulus):
    return x if modulus is None else x % modulus


def rank(rows, modulus):
    """Full Gaussian elimination, independently of the reference reducer."""
    if not rows:
        return 0
    matrix = [[value(x, modulus) for x in row] for row in rows]
    height, width = len(matrix), len(matrix[0])
    pivot_row = 0
    for col in range(width):
        chosen = next((j for j in range(pivot_row, height) if matrix[j][col]), None)
        if chosen is None:
            continue
        matrix[pivot_row], matrix[chosen] = matrix[chosen], matrix[pivot_row]
        inverse = (1 / matrix[pivot_row][col] if modulus is None
                   else pow(matrix[pivot_row][col], -1, modulus))
        matrix[pivot_row] = [reduce_value(x * inverse, modulus)
                             for x in matrix[pivot_row]]
        for j in range(pivot_row + 1, height):
            coefficient = matrix[j][col]
            if coefficient:
                matrix[j] = [reduce_value(x - coefficient * y, modulus)
                             for x, y in zip(matrix[j], matrix[pivot_row])]
        pivot_row += 1
        if pivot_row == height:
            break
    return pivot_row


def prefix_pivots(rows, modulus, width):
    previous = 0
    pivots = []
    for end in range(1, width + 1):
        current = rank([row[:end] for row in rows], modulus)
        if current > previous:
            pivots.append(end - 1)
        previous = current
    return tuple(pivots)


def exponents(coordinates, degree):
    if not coordinates:
        yield ()
        return
    for head in range(degree + 1):
        for tail in exponents(coordinates - 1, degree - head):
            yield (head,) + tail


def monomial_rows(coords, degree, width, modulus):
    rows = []
    for alpha in exponents(len(coords), degree):
        row = []
        for e in range(width):
            x = value(1, modulus)
            for coordinate, power in zip(coords, alpha):
                x = reduce_value(x * value(coordinate[e], modulus) ** power, modulus)
            row.append(x)
        rows.append(row)
    return rows


def direct_module(initial, coords, degree, width, modulus):
    return [[reduce_value(value(x, modulus) * y, modulus) for x, y in zip(row, feature)]
            for row in initial for feature in monomial_rows(coords, degree, width, modulus)]


def check_module(initial, coords, degree, width, modulus):
    result = evaluation_module(initial, coords, degree, Field(modulus))
    explicit = direct_module(initial, coords, degree, width, modulus)
    expected_rank = rank(explicit, modulus)
    require(result.rank == expected_rank, "module rank differs from explicit monomials")
    require(rank(explicit + result.vectors, modulus) == expected_rank,
            "generated module has different row space")
    require(result.pivots == prefix_pivots(explicit, modulus, width),
            "module pivots do not give the canonical original columns")
    expected_initial = rank(initial, modulus)
    require(result.initial_rank == expected_initial, "initial rank mismatch")
    require(result.candidates == len(initial) + len(coords) * result.expanded,
            "frontier candidate accounting mismatch")
    if degree:
        previous = rank(direct_module(initial, coords, degree - 1, width, modulus), modulus)
        require(result.expanded == previous, "expanded frontier is not W_(h-1)")
    require(max(result.degrees, default=0) <= min(degree, expected_rank - expected_initial),
            "accepted degree exceeds its rank bound")


def failures(labels, budget):
    universe = sorted(set().union(*(set(x) for x in labels))) if labels else []
    for size in range(min(budget, len(universe)) + 1):
        for chosen in combinations(universe, size):
            yield set(chosen)


def check_surviving_prefixes(columns, labels, budget, retained, order, modulus):
    retained = set(retained)
    states = 0
    for failed in failures(labels, budget):
        original, restricted = [], []
        canonical = []
        previous = 0
        for e in order:
            if not set(labels[e]) & failed:
                original.append(columns[e])
                if e in retained:
                    restricted.append(columns[e])
                current = rank(original, modulus)
                if current > previous:
                    canonical.append(e)
                previous = current
            require(rank(original, modulus) == rank(restricted, modulus),
                    "a surviving prefix lost original span")
            states += 1
        require(set(canonical) <= retained, "canonical surviving basis is not contained")
    return states


def original_boundary(vertices, simplices, modulus):
    """Construct the oriented boundary independently as columns."""
    facets = sorted({tuple(v for v in simplex if v != removed)
                     for simplex in simplices for removed in simplex})
    columns = []
    for simplex in simplices:
        entries = {tuple(v for v in simplex if v != removed): (-1) ** j
                   for j, removed in enumerate(simplex)}
        columns.append([value(entries.get(facet, 0), modulus) for facet in facets])
    return facets, columns


def full_contractions(facets, simplices, features, modulus):
    rows = []
    for feature in features:
        for facet in facets:
            row = []
            for simplex in simplices:
                missing = [v for v in simplex if v not in facet]
                if len(missing) == 1 and len(facet) + 1 == len(simplex):
                    v = missing[0]
                    sign = (-1) ** simplex.index(v)
                    row.append(reduce_value(sign * feature[v], modulus))
                else:
                    row.append(value(0, modulus))
            rows.append(row)
    return rows


def check_represented(columns, labels, budget, order, modulus):
    result = represented_summary(columns, labels, budget, modulus, order)
    coords = monic_label_coefficients([labels[e] for e in order], Field(modulus))
    rows = [[columns[e][i] for e in order] for i in range(len(columns[0]))]
    explicit = direct_module(rows, coords, budget, len(columns), modulus)
    expected = [order[e] for e in prefix_pivots(explicit, modulus, len(columns))]
    require(result["retained"] == expected, "packed matroid basis differs from explicit lift")
    require(result["rank"] <= result["formal_rows"], "formal rank bound violated")
    return check_surviving_prefixes(columns, labels, budget, result["retained"], order, modulus)


def check_persistence(vertices, simplices, labels, budget, order, modulus):
    result = persistence_summary(vertices, simplices, labels, budget, modulus, order)
    coords = normalized_label_coefficients(labels, Field(modulus))
    features = monomial_rows(coords, budget, vertices, modulus)
    expected_s = rank(features, modulus)
    require(result["feature_rank"] == expected_s, "vertex feature rank mismatch")
    require(rank(features + result["shifted_rows"], modulus) == expected_s,
            "nonvanishing shifts changed the feature row space")
    require(all(all(row) for row in result["shifted_rows"]), "a shifted vertex feature vanishes")
    facets, columns = original_boundary(vertices, simplices, modulus)
    full = full_contractions(facets, simplices, features, modulus)
    ordered_full = [[row[e] for e in order] for row in full]
    expected = [order[e] for e in prefix_pivots(ordered_full, modulus, len(simplices))]
    require(result["retained"] == expected, "compressed contractions changed column dependencies")
    if simplices:
        top_size = len(simplices[0])
        remaining = vertices - expected_s
        envelope = comb(vertices, top_size) - (comb(remaining, top_size) if remaining >= top_size else 0)
        require(result["rank"] <= min(len(simplices), expected_s * rank(columns, modulus), envelope),
                "intrinsic/exterior retained-size bound failed")
    column_labels = [set().union(*(set(labels[v]) for v in simplex)) for simplex in simplices]
    return check_surviving_prefixes(columns, column_labels, budget,
                                   result["retained"], order, modulus)


def large_dimension_examples():
    """The formal dimension is huge; exact checks use independent structures."""
    label_types = [set(range(12 * t, 12 * (t + 1))) for t in range(4)]
    labels = [label_types[t] for t in range(4) for _ in range(10)]
    columns = [[1, 0] if t < 2 else [0, 1] for t in range(4) for _ in range(10)]
    order = list(range(0, 40, 2)) + list(range(1, 40, 2))
    result = represented_summary(columns, labels, 12, 101, order)
    require(result["formal_rows"] == 2 * comb(24, 12), "wrong large tensor dimension")
    require(result["rank"] == 4, "large tensor lift failed to retain its exact rank four")
    require(result["candidates"] <= 2 + 12 * 4, "packed frontier exceeded actual-rank count")
    for mask in range(16):
        failed = {12 * t for t in range(4) if mask >> t & 1}
        full, reduced = [], []
        for e in order:
            if not labels[e] & failed:
                full.append(columns[e])
                if e in result["retained"]:
                    reduced.append(columns[e])
            require(rank(full, 101) == rank(reduced, 101), "large represented prefix failed")

    n = 18
    vertex_labels = [label_types[v // 6] for v in range(n)]
    edges = list(combinations(range(n), 2))
    result = persistence_summary(n, edges, vertex_labels, 12, 101)
    require(result["formal_features"] == comb(24, 12), "wrong large vertex feature dimension")
    require(result["feature_rank"] == 3, "repeated-pattern feature rank is not three")
    require(result["rank"] == 3 * n - 6, "complete exterior rank differs from sharp envelope")
    require(result["feature_candidates"] <= 1 + 12 * 3, "vertex frontier exceeded rank count")
    # For p=1, equality of component partitions is an independent span test.
    retained = set(result["retained"])
    for failed_mask in range(8):
        parent_a, parent_b = list(range(n)), list(range(n))

        def root(parent, vertex):
            while parent[vertex] != vertex:
                vertex = parent[vertex]
            return vertex

        for e, (u, v) in enumerate(edges):
            if not (failed_mask >> (u // 6) & 1 or failed_mask >> (v // 6) & 1):
                parent_a[root(parent_a, u)] = root(parent_a, v)
                if e in retained:
                    parent_b[root(parent_b, u)] = root(parent_b, v)
            for x in range(n):
                for y in range(x):
                    require((root(parent_a, x) == root(parent_a, y)) ==
                            (root(parent_b, x) == root(parent_b, y)),
                            "large persistence prefix changed connectivity")
    return {"formal_vertex_features": comb(24, 12), "actual_vertex_features": 3,
            "top_simplices": len(edges), "retained_top_simplices": result["rank"],
            "formal_represented_rows": 2 * comb(24, 12), "retained_represented_columns": 4}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--full", action="store_true", help="expand finite random fixture counts")
    args = parser.parse_args()
    rng = random.Random(20261026)
    module_cases = represented_cases = persistence_cases = prefix_states = 0

    binary_rows = list(product(range(2), repeat=3))
    for initial in binary_rows:
        for coordinates in product(binary_rows, repeat=2):
            for degree in range(4):
                check_module([initial], coordinates, degree, 3, 2)
                module_cases += 1
    for trial in range(240 if args.full else 90):
        modulus = (None, 2, 3, 7)[trial % 4]
        width = rng.randrange(1, 8)
        count = rng.randrange(1, 4)
        dimensions = rng.randrange(4)
        degree = rng.randrange(4)
        entries = [Fraction(rng.randrange(-3, 4), rng.randrange(1, 4))
                   if modulus is None else rng.randrange(modulus)
                   for _ in range((count + dimensions) * width)]
        rows = [entries[i * width:(i + 1) * width] for i in range(count + dimensions)]
        check_module(rows[:count], rows[count:], degree, width, modulus)
        module_cases += 1
    saturated = evaluation_module([[1] * 4], [[0, 1, 2, 3]], 10**9, Field())
    require(saturated.rank == 4 and saturated.candidates == 5,
            "large encoded degree did not stop at the evaluation rank")

    for trial in range(240 if args.full else 72):
        modulus = (None, 7, 11)[trial % 3]
        n = rng.randrange(1, 9)
        dimension = rng.randrange(1, 4)
        columns = [[rng.randrange(-2, 3) for _ in range(dimension)] for _ in range(n)]
        labels = [{label for label in range(4) if rng.randrange(3) == 0} for _ in range(n)]
        budget = rng.randrange(3)
        order = list(range(n))
        rng.shuffle(order)
        prefix_states += check_represented(columns, labels, budget, order, modulus)
        represented_cases += 1

    all_edges = list(combinations(range(4), 2))
    label_options = [set(), {0}, {1}, {0, 1}, {2}, {0, 2}]
    for mask in range(1 << len(all_edges)):
        edges = [edge for i, edge in enumerate(all_edges) if mask >> i & 1]
        labels = [label_options[(mask + 3 * v) % len(label_options)] for v in range(4)]
        for modulus in (None, 5):
            budget = mask % 3
            order = list(reversed(range(len(edges))))
            prefix_states += check_persistence(4, edges, labels, budget, order, modulus)
            persistence_cases += 1
    for trial in range(180 if args.full else 54):
        modulus = (None, 7, 11)[trial % 3]
        n = 5 if trial % 2 else 6
        size = 3 if trial % 2 else 4
        universe = list(combinations(range(n), size))
        simplices = [s for s in universe if rng.randrange(3) != 0]
        labels = [{label for label in range(3) if rng.randrange(3) == 0} for _ in range(n)]
        budget = trial % 3
        order = list(range(len(simplices)))
        rng.shuffle(order)
        prefix_states += check_persistence(n, simplices, labels, budget, order, modulus)
        persistence_cases += 1

    require(persistence_summary(0, [], [], 0)["retained"] == [], "empty complex failed")
    require(represented_summary([], [], 0)["retained"] == [], "empty matroid failed")
    large = large_dimension_examples()
    print(f"Feature construction passed: {module_cases} exact module comparisons; "
          f"{represented_cases} represented-matroid and {persistence_cases} simplicial instances; "
          f"{prefix_states} exhaustive surviving-prefix states.")
    print("Large formal-dimension fixtures: " + "; ".join(f"{key}={value}" for key, value in large.items()))


if __name__ == "__main__":
    main()
