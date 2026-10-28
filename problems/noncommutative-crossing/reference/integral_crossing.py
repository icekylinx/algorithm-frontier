#!/usr/bin/env python3
# Copyright 2026 Yilin Liu. AI contribution identifier: GPT-6 Astra Pro.
# SPDX-License-Identifier: Apache-2.0
"""Exact finite Schur crossing factors and ordered evaluation.

The factor generator uses rational power-sum coordinates and verifies that
every final Schur coordinate is an integer before returning it. This is a
native finite component, not a generator for the asymptotically fast matrix
circuits in the theorem. No target-ring division occurs during evaluation.
"""

from functools import lru_cache
from schur_modes import (partitions, schur, transform, weighted_state, mode,
                         schur_coordinates)


@lru_cache(None)
def matrix_column(h, state_index, transformed, index, input_partition, shift):
    """One integral Schur mode column; internal inputs are exact indices."""
    state = schur(partitions(h)[state_index])
    if transformed:
        state = weighted_state(transform(state), h, index)
    value = mode(state, schur(input_partition), shift)
    output_weight = sum(input_partition) + shift
    result = schur_coordinates(value, output_weight)
    if not all(c.denominator == 1 for c in result.values()):
        raise ArithmeticError("nonintegral Schur coordinate")
    return {p: int(c) for p, c in result.items() if c}


def mixed_factors(h, energy, orientation="mixed", *, location=None):
    """Return (orientation, left, right) integer factors for weights h,E.

    `mixed` chooses the smaller certified intermediate dimension separately
    at every location; `row` and `column` expose either complete orientation
    for exact comparison. Optional `location` selects one crossing piece.
    Without it the returned list sums to delta(x,v)*delta(y,u).
    Coefficient dictionaries use zero-based partition indices.
    """
    if type(h) is not int or type(energy) is not int or min(h, energy) < 1:
        raise ValueError("h and energy must be positive integers")
    if orientation not in ("mixed", "row", "column"):
        raise ValueError("orientation must be mixed, row or column")
    if location is not None and (type(location) is not int or not -energy-h <= location <= energy+h):
        raise ValueError("location must be an integer in the finite crossing range")
    hp, ep = partitions(h), partitions(energy)
    factors = []
    locations = range(-energy-h, energy+h+1) if location is None else (location,)
    for current in locations:
        row_rank = sum(len(partitions(energy+current-h+i)) for i in range(2*h+1))
        col_rank = sum(len(partitions(energy+h-current-i)) for i in range(2*h+1))
        chosen = ("row" if row_rank <= col_rank else "column") if orientation == "mixed" else orientation
        for i in range(2*h+1):
            shift = current-h+i
            intermediate = energy+shift if chosen == "row" else energy-shift
            for middle in partitions(intermediate):
                left, right = {}, {}
                if chosen == "row":
                    for x in range(len(hp)):
                        for y, argument in enumerate(ep):
                            c = matrix_column(h, x, True, i, argument, shift).get(middle, 0)
                            if c:
                                left[x, y] = (-1)**i*c
                    for v in range(len(hp)):
                        output = matrix_column(h, v, False, 0, middle, -shift)
                        for u, target in enumerate(ep):
                            if output.get(target, 0):
                                right[v, u] = output[target]
                else:
                    for x in range(len(hp)):
                        output = matrix_column(h, x, True, i, middle, shift)
                        for u, target in enumerate(ep):
                            if output.get(target, 0):
                                left[x, u] = (-1)**i*output[target]
                    for v in range(len(hp)):
                        for y, argument in enumerate(ep):
                            c = matrix_column(h, v, False, 0, argument, -shift).get(middle, 0)
                            if c:
                                right[v, y] = c
                if left and right:
                    factors.append((chosen, left, right))
    return factors


def ordered_evaluation(factors, xs, ys, *, zero, add, mul, scale):
    """Contract actual factors with X_x Y_y X_v Y_u in the stated order.

    Callbacks provide ring addition, ordered multiplication and central
    integer scaling. They must not mutate their arguments. The callback
    interface permits noncommutative rings and rings with zero divisors.
    All integer factor construction occurs before these callbacks run.
    """
    def linear_form(coefficients, reverse=False):
        value = zero
        for (x, y), c in coefficients.items():
            term = mul(ys[y], xs[x]) if reverse else mul(xs[x], ys[y])
            value = add(value, scale(c, term))
        return value

    value = zero
    for orientation, left, right in factors:
        if orientation == "row":
            term = mul(linear_form(left), linear_form(right))
            value = add(value, term)
        elif orientation == "column":
            interior = linear_form(right, reverse=True)
            for (x, u), c in left.items():
                value = add(value, scale(c, mul(mul(xs[x], interior), ys[u])))
        else:
            raise ValueError("factor orientation must be row or column")
    return value
