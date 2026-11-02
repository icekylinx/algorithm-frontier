#!/usr/bin/env python3
# Copyright 2026 icekylinx and GPT-6 Astra Pro.
# SPDX-License-Identifier: Apache-2.0
"""Exact finite checks of the variable-preserving weighted-count reduction.

The #Subset Sum oracle is replaced by exhaustive enumeration. The code
validates the reduction, not the asymptotic running-time theorem.
"""
from collections import Counter
import math
import random


def prime(p):
    return p >= 2 and all(p % k for k in range(2, math.isqrt(p) + 1))


def primitive_root(p):
    for g in range(1, p):
        if len({pow(g, r, p) for r in range(p - 1)}) == p - 1:
            return g
    raise AssertionError("The finite multiplicative group must be cyclic.")


def subset_sums(weights):
    out = [0]
    for weight in weights:
        out += [value + weight for value in out]
    return out


def exhaustive_weighted(a, target, u, v):
    answer = 0
    for mask in range(1 << len(a)):
        if sum(a[i] for i in range(len(a)) if mask >> i & 1) != target:
            continue
        weight = 1
        for i in range(len(a)):
            weight *= v[i] if mask >> i & 1 else u[i]
        answer += weight
    return answer


def weighted_residue(a, target, u, v, p):
    kept, activities, prefactor = [], [], 1
    for ai, ui, vi in zip(a, u, v):
        ui, vi = ui % p, vi % p
        if ui == 0 and vi == 0:
            return 0, 0
        if ui == 0:
            target -= ai
            prefactor = prefactor * vi % p
        elif vi == 0:
            prefactor = prefactor * ui % p
        else:
            prefactor = prefactor * ui % p
            kept.append(ai)
            activities.append(vi * pow(ui, -1, p) % p)
    g = primitive_root(p)
    log_table = {pow(g, r, p): r for r in range(p - 1)}
    colors = [log_table[w] for w in activities]
    color_total = sum(colors)
    base = color_total + 1
    packed = [base * ai + ri for ai, ri in zip(kept, colors)]
    oracle = Counter(subset_sums(packed))
    value = sum(pow(g, s, p) * oracle[base * target + s]
                for s in range(color_total + 1)) % p
    return value * prefactor % p, color_total + 1


def reconstruct(a, target, u, v):
    bound = math.prod(abs(ui) + abs(vi) for ui, vi in zip(u, v))
    if bound == 0:
        return 0, 0
    value, modulus, p, calls = 0, 1, 2, 0
    while modulus <= 2 * bound:
        if prime(p):
            residue, cost = weighted_residue(a, target, u, v, p)
            value += ((residue - value) * pow(modulus, -1, p) % p) * modulus
            modulus *= p
            calls += cost
        p += 1
    if value > modulus // 2:
        value -= modulus
    assert -bound <= value <= bound
    return value, calls


def main():
    rng = random.Random(20261102)
    residues, reconstructions, maximum_calls = 0, 0, 0
    for n in range(10):
        for _ in range(40):
            a = [rng.randrange(-9, 10) for _ in range(n)]
            u = [rng.randrange(-7, 8) for _ in range(n)]
            v = [rng.randrange(-7, 8) for _ in range(n)]
            target = rng.choice(subset_sums(a) + [123])
            wanted = exhaustive_weighted(a, target, u, v)
            for p in [2, 3, 5, 7, 11, 13, 17]:
                got, calls = weighted_residue(a, target, u, v, p)
                assert got == wanted % p, (a, target, u, v, p, got, wanted)
                residues += 1
            got, calls = reconstruct(a, target, u, v)
            assert got == wanted
            maximum_calls = max(maximum_calls, calls)
            reconstructions += 1
    print(f"PASS: {residues} exact prime-residue reductions")
    print(f"PASS: {reconstructions} signed weighted CRT reconstructions")
    print(f"Maximum exhaustive-oracle calls in a checked reconstruction: {maximum_calls}")
    print("Scope: reduction identities only; no asymptotic checksum implementation.")


if __name__ == "__main__":
    main()
