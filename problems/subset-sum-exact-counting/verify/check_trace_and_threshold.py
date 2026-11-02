#!/usr/bin/env python3
# Copyright 2026 icekylinx and GPT-6 Astra Pro.
# SPDX-License-Identifier: Apache-2.0
"""Finite checks of trace recovery and the disjoint threshold recursion.

These checks do not implement or validate the asymptotic checksum estimator.
Only Python's standard library is required. All randomness is reproducible.
"""
from collections import Counter
from itertools import product
import cmath
import math
import random


def subset_sums(weights):
    out = [0]
    for w in weights:
        out += [s + w for s in out]
    return out


def prime(q):
    return q >= 2 and all(q % d for d in range(2, math.isqrt(q) + 1))


def trace_checks(rng):
    checked = 0
    numerical = 0
    all_zero_control = False
    for n in range(0, 10):
        for trial in range(16):
            weights = [rng.randrange(-8, 9) for _ in range(n)]
            sums = subset_sums(weights)
            target = rng.choice(sums + [1000])
            family = [mask for mask, s in enumerate(sums) if s == target]
            z = len(family)
            for q in [2, 3, 5, 7, 11, 17, 31]:
                phases = [rng.randrange(q) for _ in range(n)]
                hist = [0] * q
                for mask in family:
                    e = sum(phases[i] for i in range(n) if mask >> i & 1) % q
                    hist[e] += 1
                trace = (q - 1) * hist[0] - sum(hist[1:])
                assert trace == q * hist[0] - z
                assert (-trace) % q == z % q
                checked += 1
                # Independently evaluate every conjugate and perturb each by
                # an error of modulus <=1/(16q); rounding must still succeed.
                conjugates = []
                for j in range(1, q):
                    val = sum(c * cmath.exp(2j * math.pi * j * a / q)
                              for a, c in enumerate(hist))
                    angle = rng.random() * 2 * math.pi
                    val += cmath.exp(1j * angle) / (16 * q)
                    conjugates.append(val)
                recovered = round(sum(conjugates).real)
                assert recovered == trace
                assert abs(sum(conjugates).imag) < 0.2
                numerical += 1
                if z > 0:
                    # Must-fail control: the negative trace is not the
                    # integer count before reduction modulo q.
                    bad_trace = (q - 1) * z  # all phases zero
                    if -bad_trace != z:
                        all_zero_control = True
    assert all_zero_control
    return checked, numerical


def crt(residues, moduli):
    x, modulus = 0, 1
    for r, q in zip(residues, moduli):
        x += ((r - x) * pow(modulus, -1, q) % q) * modulus
        modulus *= q
    return x, modulus


def crt_checks(rng):
    checks = 0
    for n in range(0, 40):
        qs = []
        p = 2
        prod_q = 1
        while prod_q <= 2 ** n:
            if prime(p):
                qs.append(p)
                prod_q *= p
            p += 1
        for _ in range(20):
            z = rng.randrange(2 ** n + 1)
            residues = []
            for q in qs:
                n0 = rng.randrange(z + 1)
                tr = q * n0 - z
                residues.append(-tr % q)
            value, modulus = crt(residues, qs)
            assert modulus > 2 ** n and value == z
            checks += 1
    return checks


def deterministic_tag_checks(rng):
    """Check the literal source-format bins without any isolated witness."""
    subset_checks = 0
    trace_checks_count = 0
    multiple_same_bin = False
    for n in range(1, 10):
        tag_range = 1
        while tag_range < 12 * n:
            tag_range *= 2
        assert 12 * n <= tag_range < 24 * n
        base = 1 + n * tag_range
        for trial in range(12):
            weights = ([1] * n if trial == 0 else
                       [rng.randrange(1, 16) for _ in range(n)])
            sums = subset_sums(weights)
            target = n // 2 if trial == 0 else rng.choice(sums + [1000])
            transformed = [base * a + 1 for a in weights]
            transformed_sums = subset_sums(transformed)
            bins = Counter()
            for mask, (original, encoded) in enumerate(zip(sums, transformed_sums)):
                s = encoded - base * target
                is_bin_member = 0 <= s <= n * tag_range
                assert is_bin_member == (original == target)
                if is_bin_member:
                    assert s == mask.bit_count() <= n
                    bins[s] += 1
                subset_checks += 1
            assert sum(bins.values()) == sums.count(target)
            if any(count > 1 for count in bins.values()):
                multiple_same_bin = True
            # The multiplicity-aware preliminary join counts every bin.
            half = n // 2
            left = Counter(subset_sums(transformed[:half]))
            right = Counter(subset_sums(transformed[half:]))
            for s in range(n + 1):
                joined = sum(mult * right[base * target + s - value]
                             for value, mult in left.items())
                assert joined == bins[s]
            # Reconstruct each bin's residue before adding them.
            for q in [3, 5, 7]:
                phases = [rng.randrange(q) for _ in range(n)]
                zero_counts = Counter()
                for mask, original in enumerate(sums):
                    if original == target:
                        e = sum(phases[i] for i in range(n)
                                if mask >> i & 1) % q
                        if e == 0:
                            zero_counts[mask.bit_count()] += 1
                recovered = sum(-(q * zero_counts[s] - bins[s]) % q
                                for s in range(n + 1)) % q
                assert recovered == sums.count(target) % q
                trace_checks_count += 1
    assert multiple_same_bin
    return subset_checks, trace_checks_count


def positive_threshold_count(weights, target):
    """Use the proposed disjoint recurrence, with exhaustive #SS oracles."""
    if target < 0:
        return 0, 0
    if not any(weights):
        return 2 ** len(weights), 0
    n = len(weights)
    quotients = [a // 2 for a in weights]
    remainders = [a % 2 for a in weights]
    lower = (target - n) // 2
    upper = target // 2
    value, calls = positive_threshold_count(quotients, lower)
    base = n + 1
    encoded = [base * u + r for u, r in zip(quotients, remainders)]
    counts = Counter(subset_sums(encoded))
    for s in range(max(0, lower + 1), upper + 1):
        for k in range(min(n, target - 2 * s) + 1):
            value += counts[base * s + k]
            calls += 1
    return value, calls


def signed_threshold_count(weights, target):
    # Globally complement choices attached to negative weights.
    shifted = target - sum(w for w in weights if w < 0)
    return positive_threshold_count([abs(w) for w in weights], shifted)


def threshold_checks(rng):
    checked = 0
    max_calls = 0
    for n in range(0, 10):
        for _ in range(40):
            weights = [rng.randrange(-60, 61) for _ in range(n)]
            sums = subset_sums(weights)
            target = rng.randrange(min(sums) - 4, max(sums) + 5)
            got, calls = signed_threshold_count(weights, target)
            want = sum(s <= target for s in sums)
            assert got == want, (weights, target, got, want)
            max_calls = max(max_calls, calls)
            checked += 1
    return checked, max_calls


def low_deficiency_control():
    # The block (1,3,9,13) has exactly one collision: {1,3,9} and {13}.
    block = [1, 3, 9, 13]
    all_sums = subset_sums(block)
    assert len(set(all_sums)) == 15
    assert all_sums.count(13) == 2
    for mask in range(15):
        chosen = [a for i, a in enumerate(block) if mask >> i & 1]
        assert len(set(subset_sums(chosen))) == 2 ** len(chosen)
    # Two separated blocks have four witnesses and independent supports.
    weights = block + [100 * a for a in block]
    sums = subset_sums(weights)
    assert sums.count(1313) == 4
    assert len(set(sums)) == 15 ** 2
    return True


def ceil_half(x):
    return -((-x) // 2)


def disjoint_interval_queries(weights, lo, hi):
    n = len(weights)
    total = sum(weights)
    lo, hi = max(lo, 0), min(hi, total)
    if lo > hi:
        return []
    if lo == 0 and hi == total:
        return [(tuple([0] * n), 0)]
    if hi - lo <= 2 * n:
        return [(tuple(weights), t) for t in range(lo, hi + 1)]
    v = [a // 2 for a in weights]
    r = [a % 2 for a in weights]
    lower = ceil_half(lo)
    upper = (hi - n) // 2
    assert lower <= upper
    out = disjoint_interval_queries(v, lower, upper)
    base = n + 1
    encoded = tuple(base * a + b for a, b in zip(v, r))
    boundary = list(range(ceil_half(lo - n), lower))
    boundary += list(range(upper + 1, hi // 2 + 1))
    assert len(boundary) <= n + 2
    for s in boundary:
        if not 0 <= s <= sum(v):
            continue
        for k in range(max(0, lo - 2 * s), min(n, hi - 2 * s) + 1):
            out.append((encoded, base * s + k))
    return out


def interval_checks(rng):
    checked = 0
    max_queries = 0
    for n in range(0, 10):
        for _ in range(32):
            weights = [rng.randrange(0, 301) for _ in range(n)]
            lo = rng.randrange(-5, sum(weights) + 6)
            hi = rng.randrange(lo, sum(weights) + 6)
            queries = disjoint_interval_queries(weights, lo, hi)
            sums = subset_sums(weights)
            multiplicities = [0] * (2 ** n)
            for w, t in queries:
                for mask, val in enumerate(subset_sums(w)):
                    multiplicities[mask] += val == t
            for mask, val in enumerate(sums):
                assert multiplicities[mask] == int(lo <= val <= hi), (
                    weights, lo, hi, mask, multiplicities[mask])
                checked += 1
            max_queries = max(max_queries, len(queries))
    return checked, max_queries


def main():
    rng = random.Random(20261102)
    trace, numeric = trace_checks(rng)
    crt_count = crt_checks(rng)
    threshold, max_calls = threshold_checks(rng)
    interval, max_queries = interval_checks(rng)
    tagged_subsets, tagged_traces = deterministic_tag_checks(rng)
    assert low_deficiency_control()
    print(f"PASS: {trace} exact trace identities")
    print(f"PASS: {numeric} noisy conjugate-rounding checks")
    print(f"PASS: {crt_count} CRT reconstructions")
    print(f"PASS: {threshold} threshold-recursion checks; max oracle calls={max_calls}")
    print(f"PASS: {interval} per-subset disjoint interval identities; max queries={max_queries}")
    print(f"PASS: {tagged_subsets} deterministic-tag disjoint identities; {tagged_traces} binwise trace reconstructions")
    print("PASS: false direct-trace control and low-deficiency many-solution control")
    print("Scope: finite algebra/control flow only; no asymptotic estimator implementation.")


if __name__ == '__main__':
    main()
