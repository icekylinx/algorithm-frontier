#!/usr/bin/env python3
# Copyright 2026 icekylinx and GPT-6 Astra Pro. Apache-2.0.
# Adapted from tcs_research_checkpoint.zip: verification/circuit_frontier/check_interleaved_composition.py
"""Exact factor certificates for sums with different interleaved scopes.

This closes the gap between checking the canonical-orientation bijection
and checking the actual matrix factors when product partitions vary.
The small integral I_4 crossing identity is used, not the asymptotic
Schur construction. NumPy object arrays retain exact integer arithmetic.
"""

from itertools import product
from pathlib import Path
import json
import math
import random
import time

import numpy as np


def partial_transpose(matrix, dimensions, mask):
    size = math.prod(dimensions)
    count = len(dimensions)
    axes = list(range(2 * count))
    for site in range(count):
        if mask >> site & 1:
            axes[site], axes[count + site] = axes[count + site], axes[site]
    return matrix.reshape(tuple(dimensions) * 2).transpose(axes).reshape(size, size)


def random_matrix(generator, rows, columns):
    return np.array([[generator.randrange(-2, 3) for _ in range(columns)]
                     for _ in range(rows)], dtype=object)


def embed_vector(vector, dimensions, first, second):
    order = tuple(first) + tuple(second)
    axes = [order.index(site) for site in range(len(dimensions))]
    return vector.reshape(tuple(dimensions[site] for site in order)).transpose(axes).reshape(-1)


def embed_matrix(matrix, dimensions, first, second):
    order = tuple(first) + tuple(second)
    count = len(dimensions)
    axes = [order.index(site) for site in range(count)]
    axes += [axis + count for axis in axes]
    shape = tuple(dimensions[site] for site in order) * 2
    size = math.prod(dimensions)
    return matrix.reshape(shape).transpose(axes).reshape(size, size)


def lift_mask(mask, scope):
    return sum(((mask >> index) & 1) << site for index, site in enumerate(scope))


def child_factors(generator, dimensions):
    size = math.prod(dimensions)
    factors = {mask: (random_matrix(generator, size, 2),
                      random_matrix(generator, size, 2))
               for mask in range(0, 1 << len(dimensions), 2)}
    matrix = np.zeros((size, size), dtype=object)
    for mask, (left, right) in factors.items():
        matrix += partial_transpose(left @ right.T, dimensions, mask)
    return matrix, factors


def certificate(generator, dimensions, scopes):
    size = math.prod(dimensions)
    count = len(dimensions)
    masks = list(range(0, 1 << count, 2))
    direct = np.zeros((size, size), dtype=object)
    factors = {mask: [] for mask in masks}
    left_identity = np.array([1, 0, 0, 1], dtype=object)
    right_identity = np.array([0, 1, -1, 0], dtype=object)
    local = (left_identity, right_identity)
    wrong = {mask: np.zeros((size, size), dtype=object) for mask in masks}

    for first in scopes:
        first = tuple(sorted(first))
        assert first and first[0] == 0
        second = tuple(site for site in range(count) if site not in first)
        assert second
        dim_first = [dimensions[site] for site in first]
        dim_second = [dimensions[site] for site in second]
        matrix_first, factors_first = child_factors(generator, dim_first)
        matrix_second, factors_second = child_factors(generator, dim_second)
        direct += embed_matrix(np.kron(matrix_first, matrix_second), dimensions,
                               first, second)
        seen = set()
        for alpha, beta, epsilon in product(factors_first, factors_second, [0, 1]):
            ua, va = factors_first[alpha]
            ub, vb = factors_second[beta]
            global_mask = lift_mask(alpha, first) | lift_mask(beta, second)
            if epsilon:
                global_mask ^= sum(1 << site for site in second)
            assert global_mask in factors and global_mask not in seen
            seen.add(global_mask)
            right_child_left, right_child_right = ((ub, vb) if epsilon == 0 else (vb, ub))
            left = embed_vector(np.kron(ua, right_child_left) @ local[epsilon],
                                dimensions, first, second)
            right = embed_vector(np.kron(va, right_child_right) @ local[epsilon],
                                 dimensions, first, second)
            factors[global_mask].append((left, right))

            # Negative control: omit the required left/right interchange
            # on the second child when the whole second scope is transposed.
            bad_left = embed_vector(np.kron(ua, ub) @ local[epsilon],
                                    dimensions, first, second)
            bad_right = embed_vector(np.kron(va, vb) @ local[epsilon],
                                     dimensions, first, second)
            wrong[global_mask] += np.outer(bad_left, bad_right)
        assert seen == set(masks)

    reconstructed = np.zeros((size, size), dtype=object)
    wrong_reconstruction = np.zeros_like(reconstructed)
    for mask in masks:
        assert len(factors[mask]) == len(scopes)
        left = np.column_stack([entry[0] for entry in factors[mask]])
        right = np.column_stack([entry[1] for entry in factors[mask]])
        reconstructed += partial_transpose(left @ right.T, dimensions, mask)
        wrong_reconstruction += partial_transpose(wrong[mask], dimensions, mask)
    assert np.array_equal(direct, reconstructed)
    assert not np.array_equal(direct, wrong_reconstruction)
    modular_checks = 0
    for modulus in [2, 3, 4, 6, 8, 101]:
        assert np.array_equal(direct % modulus, reconstructed % modulus)
        modular_checks += 1
    return {"dimensions": dimensions,
            "first_scopes": [list(sorted(scope)) for scope in scopes],
            "orientations": len(masks),
            "columns_per_orientation": len(scopes),
            "integer_entry_checks": size * size,
            "modular_matrix_checks": modular_checks,
            "missing_covariance_swap_rejected": True}


def main():
    start = time.monotonic()
    generator = random.Random(202611020413)
    specifications = [
        ([2, 2, 2, 2], [{0, 1}, {0, 2}, {0, 3}]),
        ([2, 3, 2, 2], [{0}, {0, 2}, {0, 1, 3}]),
        ([2, 2, 2, 2, 2], [{0, 1}, {0, 3}, {0, 2, 4}, {0}]),
    ]
    records = [certificate(generator, dimensions, scopes)
               for _ in range(8) for dimensions, scopes in specifications]
    report = {"status": "passed", "seed": 202611020413,
              "certificates": len(records),
              "integer_entry_checks": sum(item["integer_entry_checks"] for item in records),
              "modular_matrix_checks": sum(item["modular_matrix_checks"] for item in records),
              "negative_controls_rejected": len(records),
              "arithmetic": "exact integers; reductions modulo 2, 3, 4, 6, 8, 101",
              "scope": "Finite matrix-factor checks; not an asymptotic rank proof.",
              "elapsed_seconds": round(time.monotonic() - start, 6),
              "records": records}
    output = Path(__file__).with_name("interleaved_composition_results.json")
    output.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({key: value for key, value in report.items() if key != "records"}, indent=2))


if __name__ == "__main__":
    main()
