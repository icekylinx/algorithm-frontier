#!/usr/bin/env python3
# Copyright 2026 Yilin Liu. AI contribution identifier: GPT-6 Astra Pro.
# SPDX-License-Identifier: Apache-2.0
"""Exact finite integrality, Hall duality and crossing checks; writes no files."""
from collections import Counter
from fractions import Fraction
from pathlib import Path
import json
import sys
import time
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "reference"))
from schur_modes import (partitions, schur, hall, transform, schur_coordinates,
                         add, mode, crossing_piece)

def main():
    if not __debug__:
        raise SystemExit("Run without -O: this checker uses assertions")
    started = time.monotonic()
    checks = Counter()

    # Independent Jacobi--Trudi construction and Hall orthonormality.
    for weight in range(7):
        for left in partitions(weight):
            for right in partitions(weight):
                assert hall(schur(left), schur(right)) == int(left == right)
                checks["hall_orthonormality"] += 1

    # T preserves the integral Schur lattice, despite rational power sums.
    for weight in range(1, 5):
        for partition in partitions(weight):
            transformed = transform(schur(partition))
            reconstructed = {}
            for target_weight in range(weight+1):
                homogeneous = {p: c for p, c in transformed.items() if sum(p) == target_weight}
                for target, coefficient in schur_coordinates(homogeneous, target_weight).items():
                    assert coefficient.denominator == 1
                    reconstructed = add(reconstructed, schur(target), coefficient)
                    checks["integral_T_coordinates"] += 1
            assert reconstructed == transformed

    # Every requested source-mode column is integral in the Schur basis.
    for weight in range(1, 5):
        for partition in partitions(weight):
            for state in (schur(partition), transform(schur(partition))):
                for input_weight in range(5):
                    for argument_partition in partitions(input_weight):
                        argument = schur(argument_partition)
                        for output_weight in range(7):
                            value = mode(state, argument, output_weight-input_weight)
                            reconstructed = {}
                            for target, coefficient in schur_coordinates(value, output_weight).items():
                                assert coefficient.denominator == 1, (partition, argument_partition,
                                                                      output_weight, target, coefficient)
                                reconstructed = add(reconstructed, schur(target), coefficient)
                                checks["integral_mode_coordinates"] += 1
                            assert reconstructed == value
                            checks["mode_columns"] += 1

    # The leading pairing is exactly identity, with no h! scalar.
    for h in range(1, 5):
        for left in partitions(h):
            for right in partitions(h):
                value = mode(transform(schur(left)), schur(right), -h)
                expected = {(): Fraction(1)} if left == right else {}
                assert value == expected, (h, left, right, value)
                checks["denominator_one_duality"] += 1

    # Check the actual full crossing sum in the smallest unequal spaces.
    for h in (1, 2):
        for input_weight in range(3):
            for left in partitions(h):
                for right in partitions(h):
                    for input_partition in partitions(input_weight):
                        a, b, argument = transform(schur(left)), schur(right), schur(input_partition)
                        total = {}
                        for location in range(-input_weight-h, input_weight+h+1):
                            piece = crossing_piece(a, b, argument, h, location)
                            assert all(value.denominator == 1 for value in
                                       schur_coordinates(piece, input_weight).values())
                            total = add(total, piece)
                            checks["integral_crossing_pieces"] += 1
                        assert total == (argument if left == right else {})
                        checks["full_denominator_one_crossings"] += 1

    result = {
        "status": "PASS",
        "maximum_state_weight": 4, "maximum_input_weight": 4, "maximum_output_weight": 6,
        "checks": dict(checks), "total_checks": sum(checks.values()),
        "seconds": time.monotonic()-started,
        "arithmetic": "Exact fractions in the power-sum basis; independent Jacobi--Trudi Schur construction.",
        "mode_definition": "Literal normal-ordered source equation (47), with derivatives applied before creation.",
        "limitations": "Finite integrality/duality/crossing checks only; no asymptotic rank, circuit-size or SAT verification.",
    }
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
