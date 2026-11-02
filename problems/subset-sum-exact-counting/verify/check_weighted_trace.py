#!/usr/bin/env python3
# Copyright 2026 icekylinx and GPT-6 Astra Pro.
# SPDX-License-Identifier: Apache-2.0
"""Finite exact and numerical controls for unit-weighted trace formulas.

These checks concern reconstruction identities and second moments only;
they do not implement the asymptotic Fourier checksum estimator.
"""
from fractions import Fraction
from itertools import product
import cmath
import math
import random


def subsets(n):
    return range(1 << n)


def sums(weights):
    out = [0]
    for weight in weights:
        out += [value + weight for value in out]
    return out


def signs(weights):
    out = [1]
    for weight in weights:
        out += [value * weight for value in out]
    return out


def signed_checks(rng):
    checked = 0
    for n in range(9):
        for _ in range(12):
            a = [rng.randrange(-7, 8) for _ in range(n)]
            sigma = [rng.choice([-1, 1]) for _ in range(n)]
            a_sum, sigma_product = sums(a), signs(sigma)
            target = rng.choice(a_sum + [99])
            family = [mask for mask in subsets(n) if a_sum[mask] == target]
            wanted = sum(sigma_product[mask] for mask in family)
            for q in [2, 3, 5, 11, 17]:
                phi_sum = sums([rng.randrange(q) for _ in range(n)])
                histogram = [0] * q
                for mask in family:
                    histogram[phi_sum[mask] % q] += sigma_product[mask]
                trace = q * histogram[0] - sum(histogram)
                assert (-trace) % q == wanted % q
                # The signs must remain fixed as j varies.
                numerical = sum(
                    sum(histogram[b] * cmath.exp(2j * math.pi * j * b / q)
                        for b in range(q))
                    for j in range(1, q))
                assert round(numerical.real) == trace
                assert abs(numerical.imag) < 1e-7
                checked += 1
    return checked


def color_checks(rng):
    checked = 0
    for n in range(8):
        for m in range(1, 8):
            a = [rng.randrange(-5, 6) for _ in range(n)]
            colors = [rng.randrange(m) for _ in range(n)]
            a_sum, color_sum = sums(a), sums(colors)
            target = rng.choice(a_sum + [100])
            family = [mask for mask in subsets(n) if a_sum[mask] == target]
            for q in [2, 3, 5, 11]:
                phi_sum = sums([rng.randrange(q) for _ in range(n)])
                counts, zero_phase = [0] * m, [0] * m
                for mask in family:
                    b = color_sum[mask] % m
                    counts[b] += 1
                    zero_phase[b] += phi_sum[mask] % q == 0
                exact = [q * zero_phase[b] - counts[b] for b in range(m)]
                traces = []
                for ell in range(m):
                    value = 0j
                    for j in range(1, q):
                        value += sum(cmath.exp(2j * math.pi * (
                            ell * color_sum[mask] / m + j * phi_sum[mask] / q))
                            for mask in family)
                    traces.append(value)
                for b in range(m):
                    value = sum(cmath.exp(-2j * math.pi * ell * b / m)
                                * traces[ell] for ell in range(m)) / m
                    assert round(value.real) == exact[b]
                    assert abs(value.imag) < 1e-7
                    assert (-exact[b]) % q == counts[b] % q
                    checked += 1
    return checked


def second_moment_checks(rng):
    checked = 0
    for n in range(6):
        for q in [2, 3, 5]:
            # General integer coefficients verify more than product signs.
            coefficient = [rng.randrange(-4, 5) for _ in subsets(n)]
            mean = (q - 1) * coefficient[0]
            total_square = 0
            for phi in product(range(q), repeat=n):
                phi_sum = sums(phi)
                zero_sum = sum(coefficient[mask] for mask in subsets(n)
                               if phi_sum[mask] % q == 0)
                trace = q * zero_sum - sum(coefficient)
                total_square += (trace - mean) ** 2
            variance = Fraction(total_square, q ** n)
            expected = (q - 1) * sum(value ** 2 for value in coefficient[1:])
            assert variance == expected, (n, q, variance, expected)
            checked += 1
    return checked


def main():
    rng = random.Random(20261102)
    signed = signed_checks(rng)
    color = color_checks(rng)
    moments = second_moment_checks(rng)
    print(f"PASS: {signed} signed-count trace identities")
    print(f"PASS: {color} finite-color coefficient extractions")
    print(f"PASS: {moments} exhaustive exact trace second moments")
    print("Scope: weighted trace identities and finite moments only; no asymptotic estimator implementation.")


if __name__ == "__main__":
    main()
