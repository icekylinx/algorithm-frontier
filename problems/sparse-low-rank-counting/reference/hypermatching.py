#!/usr/bin/env python3
"""Finite hypermatching moments. Copyright 2026 icekylinx and GPT-6 Astra Pro. Apache-2.0.

This is a finite reduction validator, not the asymptotic crossing algorithm.
"""
from collections import defaultdict
from functools import lru_cache
from itertools import combinations, permutations, product
from math import comb, factorial


def add(out, poly, scale=1):
    for alpha, value in poly.items():
        out[alpha] += scale * value


def times_linear(poly, weights, offset=0):
    out = defaultdict(int)
    for alpha, value in poly.items():
        for a, weight in enumerate(weights):
            beta = list(alpha)
            beta[offset + a] += 1
            out[tuple(beta)] += value * weight
    return {a: v for a, v in out.items() if v}


def perfect_hypermatching(weights, vertices, k):
    @lru_cache(None)
    def rec(remaining):
        if not remaining:
            return 1
        if len(remaining) % k:
            return 0
        first, rest = remaining[0], remaining[1:]
        total = 0
        for partners in combinations(rest, k - 1):
            edge = (first,) + partners
            unused = tuple(v for v in rest if v not in partners)
            total += weights.get(edge, 0) * rec(unused)
        return total
    return rec(tuple(range(vertices)))


def sparse_polynomial(B, U, r, k):
    @lru_cache(None)
    def rec(remaining):
        if not remaining:
            return {(0,) * r: 1}
        first, rest = remaining[0], remaining[1:]
        out = defaultdict(int)
        add(out, times_linear(rec(rest), U[first]))
        for partners in combinations(rest, k - 1):
            edge = (first,) + partners
            if B.get(edge, 0):
                unused = tuple(v for v in rest if v not in partners)
                add(out, rec(unused), B[edge])
        return {a: v for a, v in out.items() if v}
    return rec(tuple(range(len(U))))


def core_moments(C, r, k):
    partner_histograms = []
    for word in combinations(range(r + k - 2), k - 1):
        # Combinations with repetition through stars-and-bars indexing.
        colors = tuple(word[j] - j for j in range(k - 1))
        beta = tuple(colors.count(a) for a in range(r))
        partner_histograms.append((beta, colors))

    @lru_cache(None)
    def rec(alpha):
        size = sum(alpha)
        if size == 0:
            return 1
        if size % k:
            return 0
        i = next(i for i, count in enumerate(alpha) if count)
        available = list(alpha)
        available[i] -= 1
        total = 0
        for beta, colors in partner_histograms:
            if any(beta[j] > available[j] for j in range(r)):
                continue
            multiplicity = 1
            for j in range(r):
                multiplicity *= comb(available[j], beta[j])
            left = tuple(available[j] - beta[j] for j in range(r))
            total += multiplicity * C[tuple(sorted((i,) + colors))] * rec(left)
        return total
    return rec


def partite_permanent(A, n, k):
    value = 0
    for bijections in product(tuple(permutations(range(n))), repeat=k - 1):
        term = 1
        for i in range(n):
            edge = (i,) + tuple(p[i] for p in bijections)
            term *= A[edge]
        value += term
    return value


def partite_polynomial(B, factors, n, r, k, modulus=None, cap=None):
    def trim(poly):
        return {a: (v if modulus is None else v % modulus)
                for a, v in poly.items()
                if (cap is None or all(x < cap for x in a))
                and (v if modulus is None else v % modulus)}

    @lru_cache(None)
    def rec(i, used):
        if i == n:
            ans = {(0,) * (k * r): 1}
            for q in range(1, k):
                for j in range(n):
                    if not ((used[q - 1] >> j) & 1):
                        ans = trim(times_linear(ans, factors[q][j], q * r))
            return ans
        out = defaultdict(int)
        add(out, times_linear(rec(i + 1, used), factors[0][i]))
        for tail in product(range(n), repeat=k - 1):
            if any((used[q] >> tail[q]) & 1 for q in range(k - 1)):
                continue
            edge = (i,) + tail
            if B.get(edge, 0):
                nxt = tuple(used[q] | (1 << tail[q]) for q in range(k - 1))
                add(out, rec(i + 1, nxt), B[edge])
        return trim(out)
    return rec(0, (0,) * (k - 1))


def partite_functional(poly, r, k):
    total = 0
    for alpha, value in poly.items():
        first = alpha[:r]
        if any(alpha[q * r:(q + 1) * r] != first for q in range(1, k)):
            continue
        for a in first:
            value *= factorial(a) ** (k - 1)
        total += value
    return total
