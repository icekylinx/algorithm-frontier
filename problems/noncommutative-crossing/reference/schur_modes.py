#!/usr/bin/env python3
# Copyright 2026 Yilin Liu. AI contribution identifier: GPT-6 Astra Pro.
# SPDX-License-Identifier: Apache-2.0
"""Exact finite Schur-mode arithmetic for the denominator-one crossing.

All calculations use rational power-sum coordinates. Schur functions are
constructed independently by Jacobi--Trudi, and source modes use the
literal normal-ordered definition. This finite evaluator uses dense
dictionaries and memoization. It does not implement the polynomial-space
coefficient algorithm proved in ../manuscripts/coefficient-computation.tex,
the asymptotically fast matrix schemes or the SAT algorithm.
"""

from collections import Counter, defaultdict
from fractions import Fraction
from functools import lru_cache
from itertools import permutations
from math import comb, factorial, prod


@lru_cache(None)
def partitions(total, ceiling=None):
    if total < 0:
        return ()
    if total == 0:
        return ((),)
    ceiling = min(total, ceiling if ceiling is not None else total)
    return tuple((first,) + rest
                 for first in range(ceiling, 0, -1)
                 for rest in partitions(total-first, first))


@lru_cache(None)
def z_factor(partition):
    return prod(k**m * factorial(m) for k, m in Counter(partition).items())


def clean(poly):
    return {key: value for key, value in poly.items() if value}


def add(left, right, scale=1):
    result = defaultdict(Fraction, left)
    for key, value in right.items():
        result[key] += scale * value
    return clean(result)


def multiply(left, right):
    result = defaultdict(Fraction)
    for a, ca in left.items():
        for b, cb in right.items():
            result[tuple(sorted(a+b, reverse=True))] += ca * cb
    return clean(result)


@lru_cache(None)
def complete(index):
    if index < 0:
        return {}
    return {part: Fraction(1, z_factor(part)) for part in partitions(index)}


@lru_cache(None)
def schur(partition):
    length = len(partition)
    if not length:
        return {(): Fraction(1)}
    result = {}
    for perm in permutations(range(length)):
        sign = (-1)**sum(perm[i] > perm[j] for i in range(length) for j in range(i+1, length))
        term = {(): Fraction(sign)}
        for i, j in enumerate(perm):
            term = multiply(term, complete(partition[i]-i+j))
        result = add(result, term)
    return result


def hall(left, right):
    return sum((coefficient * right.get(part, 0) * z_factor(part)
                for part, coefficient in left.items()), Fraction(0))


def schur_coordinates(poly, weight):
    return {partition: hall(poly, schur(partition)) for partition in partitions(weight)}


def transform(poly):
    result = {}
    for partition, coefficient in poly.items():
        term = {(): coefficient}
        for n in partition:
            image = {(j,): Fraction((-1)**(n-1) * comb(n, j)) for j in range(1, n+1)}
            term = multiply(term, image)
        result = add(result, term)
    return result


@lru_cache(None)
def integer_binomial(top, bottom):
    if bottom < 0:
        return 0
    if top >= 0:
        return comb(top, bottom) if bottom <= top else 0
    return (-1)**bottom * comb(-top+bottom-1, bottom)


@lru_cache(None)
def monomial_mode(state, argument, shift):
    """Apply the literal modes in ../manuscripts/finite-crossing.tex."""
    output_weight = sum(argument) + shift
    if output_weight < 0:
        return ()
    if not state:
        return ((argument, 1),) if shift == 0 else ()
    multiplicities = Counter(argument)
    positive = sorted(multiplicities)
    options = []
    for part in state:
        modes = []
        for mode in positive + list(range(-output_weight, 0)):
            coefficient = integer_binomial(-mode-1, part-1)
            if coefficient:
                modes.append((mode, coefficient))
        options.append(modes)
    result = defaultdict(int)

    def visit(index, mode_sum, scalar, derivatives, creations):
        if index == len(state):
            if mode_sum != -shift:
                return
            out = Counter(multiplicities)
            factor = scalar
            for k, count in derivatives.items():
                factor *= k**count * factorial(multiplicities[k]) // factorial(multiplicities[k]-count)
                out[k] -= count
            out.update(creations)
            partition = tuple(sorted((k for k, count in out.items() for _ in range(count)), reverse=True))
            result[partition] += factor
            return
        for mode, coefficient in options[index]:
            if mode > 0:
                if derivatives[mode] >= multiplicities[mode]:
                    continue
                derivatives[mode] += 1
                visit(index+1, mode_sum+mode, scalar*coefficient, derivatives, creations)
                derivatives[mode] -= 1
            else:
                creations[-mode] += 1
                visit(index+1, mode_sum+mode, scalar*coefficient, derivatives, creations)
                creations[-mode] -= 1

    visit(0, 0, 1, Counter(), Counter())
    return tuple((partition, value) for partition, value in result.items() if value)


def mode(state, argument, shift):
    result = defaultdict(Fraction)
    for mu, a in state.items():
        for sigma, b in argument.items():
            for output, value in monomial_mode(mu, sigma, shift):
                result[output] += a*b*value
    return clean(result)


def weighted_state(state, h, index):
    return clean({partition: coefficient*comb(h+sum(partition), index)
                  for partition, coefficient in state.items()
                  if index <= h+sum(partition)})


def crossing_piece(a, b, argument, h, location):
    result = {}
    for index in range(2*h+1):
        inner = mode(b, argument, h-location-index)
        outer = mode(weighted_state(a, h, index), inner, location-h+index)
        result = add(result, outer, (-1)**index)
    return result
