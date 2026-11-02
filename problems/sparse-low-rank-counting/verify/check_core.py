#!/usr/bin/env python3
"""Finite core checks. Copyright 2026 icekylinx and GPT-6 Astra Pro. Apache-2.0."""
from collections import defaultdict
from fractions import Fraction
from itertools import product
from math import factorial
from pathlib import Path
from random import Random
import json
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "reference"))
from reductions import (permanent, permanent_polynomial, permanent_functional,
                        hafnian, hafnian_polynomial, hafnian_functional)


def check_number_recovery():
    """Independent dense Fraction outputs versus integer-factor modular lift."""
    rng = Random(2026110207)
    counts = defaultdict(int)

    def denominators_product(tables):
        D = 1
        for table in tables:
            for row in table:
                for value in row:
                    D *= value.denominator
        return D

    def signed(residue, modulus):
        return residue if residue < modulus // 2 else residue - modulus

    def scaled(table, scale):
        return [[int(value * scale) for value in row] for row in table]

    for n in range(5):
        for r in range(3):
            rat = lambda: Fraction(rng.randrange(-4, 5), rng.randrange(1, 5))
            B = [[rat() if rng.randrange(3) == 0 else Fraction(0)
                  for _ in range(n)] for _ in range(n)]
            U = [[rat() for _ in range(r)] for _ in range(n)]
            V = [[rat() for _ in range(r)] for _ in range(n)]
            A = [[B[i][j] + sum(U[i][a] * V[j][a] for a in range(r))
                  for j in range(n)] for i in range(n)]
            D = denominators_product((B, U, V))
            Bi, Ui, Vi = scaled(B, D**2), scaled(U, D), scaled(V, D)
            # Bound from supplied integer factors, without forming the target A.
            b = max((abs(v).bit_length() for t in (Bi, Ui, Vi)
                     for row in t for v in row), default=0)
            magnitude = factorial(n) * (2**b + r * 2**(2*b))**n
            modulus = 1 << (2 * magnitude + 1).bit_length()
            residue = permanent_functional(
                permanent_polynomial(Bi, Ui, Vi, r, modulus), r, modulus)
            assert Fraction(signed(residue, modulus), D**(2*n)) == permanent(A)
            counts["rational_permanent_modular_lifts"] += 1

    for size in (0, 2, 4, 6):
        n = size // 2
        for r in range(3):
            rat = lambda: Fraction(rng.randrange(-4, 5), rng.randrange(1, 5))
            B = [[Fraction(0)] * size for _ in range(size)]
            for i in range(size):
                for j in range(i+1, size):
                    B[i][j] = B[j][i] = rat() if rng.randrange(3) == 0 else Fraction(0)
            U = [[rat() for _ in range(r)] for _ in range(size)]
            C = [[Fraction(0)] * r for _ in range(r)]
            for a in range(r):
                for b in range(a, r):
                    C[a][b] = C[b][a] = rat()
            A = [[B[i][j] + sum(U[i][a] * C[a][b] * U[j][b]
                               for a in range(r) for b in range(r))
                  for j in range(size)] for i in range(size)]
            D = denominators_product((B, U, C))
            Bi, Ui, Ci = scaled(B, D**3), scaled(U, D), scaled(C, D)
            b = max((abs(v).bit_length() for t in (Bi, Ui, Ci)
                     for row in t for v in row), default=0)
            pairings = 1
            for k in range(1, size, 2):
                pairings *= k
            magnitude = pairings * (2**b + r*r * 2**(3*b))**n
            modulus = 1 << (2 * magnitude + 1).bit_length()
            residue = hafnian_functional(
                hafnian_polynomial(Bi, Ui, r, modulus=modulus), Ci, modulus)
            assert Fraction(signed(residue, modulus), D**(3*n)) == hafnian(A)
            counts["rational_hafnian_modular_lifts"] += 1
            monomers = [rat() for _ in range(size)]
            D = denominators_product((B, U, C, [monomers]))
            Bi, Ui, Ci = scaled(B, D**6), scaled(U, D**2), scaled(C, D**2)
            li = scaled([monomers], D**3)[0]
            b = max((abs(v).bit_length() for t in (Bi, Ui, Ci, [li])
                     for row in t for v in row), default=0)
            H = max(1, 2**b + r*r * 2**(3*b), 2**b)
            magnitude = factorial(size) * H**size
            modulus = 1 << (2 * magnitude + 1).bit_length()
            residue = hafnian_functional(
                hafnian_polynomial(Bi, Ui, r, li, modulus), Ci, modulus)
            assert Fraction(signed(residue, modulus), D**(6*n)) == hafnian(A, monomers)
            counts["rational_monomer_modular_lifts"] += 1
    return counts


def test():
    rng = Random(20261102)
    counts = defaultdict(int)
    for n in range(7):
        for r in range(4):
            for _ in range(4):
                B = [[rng.randint(-2, 2) if rng.randrange(3) == 0 else 0
                      for _ in range(n)] for _ in range(n)]
                U = [[rng.randint(-2, 2) for _ in range(r)] for _ in range(n)]
                V = [[rng.randint(-2, 2) for _ in range(r)] for _ in range(n)]
                A = [[B[i][j] + sum(U[i][a] * V[j][a] for a in range(r))
                      for j in range(n)] for i in range(n)]
                expected = permanent(A)
                assert permanent_functional(permanent_polynomial(B, U, V, r), r) == expected
                counts["integer_permanent_identities"] += 1
                for p in (2, 3, 4, 6, 101):
                    P = permanent_polynomial(B, U, V, r, modulus=p)
                    assert permanent_functional(P, r, p) == expected % p
                    counts["modular_permanent_identities"] += 1
                for p in (2, 3):
                    P = permanent_polynomial(B, U, V, r, modulus=p, cap=p)
                    assert permanent_functional(P, r, p) == expected % p
                    counts["frobenius_truncation_identities"] += 1
                bound = factorial(n) * max(1, max((abs(x) for row in A for x in row), default=0)) ** n
                modulus = 1 << (2 * bound + 1).bit_length()
                residue = permanent_functional(
                    permanent_polynomial(B, U, V, r, modulus=modulus), r, modulus)
                recovered = residue if residue < modulus // 2 else residue - modulus
                assert recovered == expected
                counts["signed_modular_reconstructions"] += 1

    for size in (0, 2, 4, 6, 8):
        for r in range(4):
            for _ in range(3):
                B = [[0] * size for _ in range(size)]
                for i in range(size):
                    for j in range(i + 1, size):
                        B[i][j] = B[j][i] = rng.randint(-2, 2) if rng.randrange(3) == 0 else 0
                U = [[rng.randint(-2, 2) for _ in range(r)] for _ in range(size)]
                C = [[0] * r for _ in range(r)]
                for a in range(r):
                    for b in range(a, r):
                        C[a][b] = C[b][a] = rng.randint(-2, 2)
                A = [[B[i][j] + sum(U[i][a] * C[a][b] * U[j][b]
                                      for a in range(r) for b in range(r))
                      for j in range(size)] for i in range(size)]
                for loops in (False, True):
                    monomers = [rng.randint(-2, 2) for _ in range(size)] if loops else None
                    expected = hafnian(A, monomers)
                    poly = hafnian_polynomial(B, U, r, monomers)
                    assert hafnian_functional(poly, C) == expected
                    counts["integer_hafnian_or_loop_identities"] += 1
                    for p in (2, 3, 4, 6, 101):
                        poly = hafnian_polynomial(B, U, r, monomers, p)
                        assert hafnian_functional(poly, C, p) == expected % p
                        counts["modular_hafnian_or_loop_identities"] += 1

    # Explicitly sum hidden Boolean chain states, checking the arity reduction.
    for degree in range(7):
        for bits in product((0, 1), repeat=degree):
            for monomer in (-2, 0, 3):
                total = 0
                for states in product((0, 1), repeat=degree):
                    prev = 0
                    valid = True
                    for x, nxt in zip(bits, states):
                        if nxt != prev + x:
                            valid = False
                            break
                        prev = nxt
                    if valid:
                        total += monomer if prev == 0 else 1
                expected = monomer if sum(bits) == 0 else int(sum(bits) == 1)
                assert total == expected
                counts["chain_tensor_identities"] += 1

    counts.update(check_number_recovery())
    return {
        "status": "PASS",
        "seed": 20261102,
        "checks": dict(counts),
        "total_checks": sum(counts.values()),
        "scope": "Exact algebraic reductions over integers and rings of moduli 2,3,4,6,101; not an implementation or benchmark of the asymptotic contraction engine.",
    }


if __name__ == "__main__":
    result = test()
    target = Path(__file__).with_name("sparse_low_rank_results.json")
    target.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
