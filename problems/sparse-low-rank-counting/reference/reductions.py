#!/usr/bin/env python3
"""Exact finite moment reductions. Copyright 2026 icekylinx and GPT-6 Astra Pro. Apache-2.0.

Subset and matching recurrences here are exponential reference evaluators,
not an implementation of the cited asymptotic contraction engine.
"""
from collections import defaultdict
from functools import lru_cache
from itertools import permutations, product
from math import factorial


def clean(poly, modulus=None):
    if modulus is None:
        return {a: c for a, c in poly.items() if c}
    return {a: c % modulus for a, c in poly.items() if c % modulus}


def add_scaled(out, poly, scale=1):
    for a, c in poly.items():
        out[a] += scale * c


def multiply_linear(poly, coeffs, offset, variables, modulus=None, cap=None,
                    constant=0):
    out = defaultdict(int)
    if constant:
        add_scaled(out, poly, constant)
    for a, c in poly.items():
        for j, weight in enumerate(coeffs):
            if not weight:
                continue
            b = list(a)
            b[offset + j] += 1
            if cap is not None and b[offset + j] >= cap:
                continue
            out[tuple(b)] += c * weight
    return clean(out, modulus)


def permanent_polynomial(B, U, V, r, modulus=None, cap=None):
    n = len(B)
    zero = (0,) * (2 * r)

    @lru_cache(None)
    def rec(i, used):
        if i == n:
            ans = {zero: 1}
            for j in range(n):
                if not (used >> j) & 1:
                    ans = multiply_linear(ans, V[j], r, 2 * r, modulus, cap)
            return ans
        out = defaultdict(int)
        add_scaled(out, multiply_linear(rec(i + 1, used), U[i], 0, 2 * r,
                                        modulus, cap))
        for j in range(n):
            if not (used >> j) & 1 and B[i][j]:
                add_scaled(out, rec(i + 1, used | (1 << j)), B[i][j])
        return clean(out, modulus)

    return rec(0, 0)


def permanent_functional(poly, r, modulus=None):
    value = 0
    for a, c in poly.items():
        if a[:r] == a[r:]:
            for v in a[:r]:
                c *= factorial(v)
            value += c
    return value if modulus is None else value % modulus


def permanent(A):
    n = len(A)
    value = 0
    for perm in permutations(range(n)):
        term = 1
        for i, j in enumerate(perm):
            term *= A[i][j]
        value += term
    return value


def hafnian_polynomial(B, U, r, monomers=None, modulus=None):
    size = len(B)
    zero = (0,) * r
    monomers = monomers if monomers is not None else [0] * size

    @lru_cache(None)
    def rec(mask):
        if not mask:
            return {zero: 1}
        bit = mask & -mask
        i = bit.bit_length() - 1
        rest = mask ^ bit
        out = defaultdict(int)
        add_scaled(out, multiply_linear(rec(rest), U[i], 0, r, modulus,
                                        constant=monomers[i]))
        for j in range(i + 1, size):
            if (rest >> j) & 1 and B[i][j]:
                add_scaled(out, rec(rest ^ (1 << j)), B[i][j])
        return clean(out, modulus)
    return rec((1 << size) - 1)


def gaussian_moments(C, modulus=None):
    @lru_cache(None)
    def rec(a):
        if not any(a):
            return 1
        if sum(a) % 2:
            return 0
        i = next(i for i, v in enumerate(a) if v)
        ans = 0
        for j, count in enumerate(a):
            multiplicity = count - int(i == j)
            if multiplicity <= 0:
                continue
            b = list(a)
            b[i] -= 1
            b[j] -= 1
            ans += multiplicity * C[i][j] * rec(tuple(b))
        return ans if modulus is None else ans % modulus
    return rec


def hafnian_functional(poly, C, modulus=None):
    moment = gaussian_moments(C, modulus)
    ans = sum(c * moment(a) for a, c in poly.items())
    return ans if modulus is None else ans % modulus


def hafnian(A, monomers=None):
    size = len(A)
    monomers = monomers if monomers is not None else [0] * size

    @lru_cache(None)
    def rec(mask):
        if not mask:
            return 1
        bit = mask & -mask
        i = bit.bit_length() - 1
        rest = mask ^ bit
        ans = monomers[i] * rec(rest)
        for j in range(i + 1, size):
            if (rest >> j) & 1:
                ans += A[i][j] * rec(rest ^ (1 << j))
        return ans
    return rec((1 << size) - 1)
