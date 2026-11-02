#!/usr/bin/env python3
"""Finite hypermatching checks. Copyright 2026 icekylinx and GPT-6 Astra Pro. Apache-2.0."""
from collections import defaultdict
from itertools import combinations, product
from pathlib import Path
from random import Random
import json
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "reference"))
from hypermatching import (perfect_hypermatching, sparse_polynomial, core_moments,
                           partite_permanent, partite_polynomial, partite_functional)


def main():
    rng = Random(202611020524)
    counts = defaultdict(int)
    for k in (2, 3, 4):
        for blocks in range(3):
            N = k * blocks
            for r in range(4):
                for _ in range(3):
                    U = [[rng.randrange(-2, 3) for _ in range(r)] for _ in range(N)]
                    C = {tuple(sorted(colors)): rng.randrange(-2, 3)
                         for colors in product(range(r), repeat=k)}
                    edges = tuple(combinations(range(N), k))
                    B = {e: rng.randrange(-2, 3) for e in edges if rng.randrange(3) == 0}
                    A = {}
                    for e in edges:
                        total = B.get(e, 0)
                        for colors in product(range(r), repeat=k):
                            value = C[tuple(sorted(colors))]
                            for vertex, color in zip(e, colors):
                                value *= U[vertex][color]
                            total += value
                        A[e] = total
                    expected = perfect_hypermatching(A, N, k)
                    P = sparse_polynomial(B, U, r, k)
                    moments = core_moments(C, r, k)
                    actual = sum(value * moments(alpha) for alpha, value in P.items())
                    assert actual == expected, (k, N, r, actual, expected)
                    counts['integer_symmetric_hypermatching_identities'] += 1
                    for modulus in (2, 3, 4, 6, 101):
                        reduced_C = {a: v % modulus for a, v in C.items()}
                        reduced_moments = core_moments(reduced_C, r, k)
                        reduced_value = sum((value % modulus) * reduced_moments(alpha)
                                            for alpha, value in P.items()) % modulus
                        assert reduced_value == expected % modulus
                        counts['modular_symmetric_hypermatching_identities'] += 1

    for k in (2, 3):
        for n in range(5):
            for r in range(3):
                for _ in range(3):
                    factors = [[[rng.randrange(-2, 3) for _ in range(r)]
                                for _ in range(n)] for _ in range(k)]
                    edges = tuple(product(range(n), repeat=k))
                    B = {e: rng.randrange(-2, 3) for e in edges if rng.randrange(3) == 0}
                    A = {}
                    for e in edges:
                        total = B.get(e, 0)
                        for a in range(r):
                            value = 1
                            for q in range(k):
                                value *= factors[q][e[q]][a]
                            total += value
                        A[e] = total
                    expected = partite_permanent(A, n, k)
                    P = partite_polynomial(B, factors, n, r, k)
                    assert partite_functional(P, r, k) == expected
                    counts['integer_partite_identities'] += 1
                    for modulus in (2, 3, 4, 6, 101):
                        Pmod = partite_polynomial(B, factors, n, r, k, modulus)
                        assert partite_functional(Pmod, r, k) % modulus == expected % modulus
                        counts['modular_partite_identities'] += 1
                    for p in (2, 3):
                        Pmod = partite_polynomial(B, factors, n, r, k, p, p)
                        assert partite_functional(Pmod, r, k) % p == expected % p
                        counts['prime_truncation_partite_identities'] += 1

    report = {
        'status': 'PASS',
        'arithmetic': 'Exact integer arithmetic and modular reductions',
        'scope': 'Finite validation of the new hypermatching reductions; not the asymptotic contraction engine',
        'counts': dict(counts),
        'total_checks': sum(counts.values()),
        'parameters': {'symmetric_k': [2, 3, 4], 'symmetric_N': '0,k,2k',
                       'symmetric_r': [0, 1, 2, 3], 'partite_k': [2, 3],
                       'partite_n': [0, 1, 2, 3, 4], 'partite_r': [0, 1, 2]}
    }
    Path(__file__).with_name('hypermatching_results.json').write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
