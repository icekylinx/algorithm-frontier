#!/usr/bin/env python3
# Copyright 2026 Yilin Liu and GPT-6 Astra Pro
# SPDX-License-Identifier: Apache-2.0
"""Independent finite checks of the ordered subset-zeta construction.

The comparison oracle enumerates injective row assignments or disjoint
subset triples directly.  The candidate route builds block subset tables,
applies an upper zeta transform, and contracts role-marker profiles as
ordinary ordered matrix products.  Matrix multiplication is deliberately
naive here: these checks do not implement or certify its asymptotic bound.
"""

from collections import Counter
from datetime import datetime, timezone
import hashlib
from itertools import combinations, permutations, product
import json
from pathlib import Path
import random
import time


ZERO = (0, 0, 0, 0)
ONE = (1, 0, 0, 1)
COUNTS = Counter()


class MatrixRing:
    def __init__(self, modulus):
        self.modulus = modulus

    def reduce(self, x):
        return tuple(v % self.modulus for v in x) if self.modulus else tuple(x)

    def add(self, x, y):
        return self.reduce(tuple(a + b for a, b in zip(x, y)))

    def mul(self, x, y):
        a, b, c, d = x
        e, f, g, h = y
        return self.reduce((a*e+b*g, a*f+b*h, c*e+d*g, c*f+d*h))

    def scale(self, scalar, x):
        return self.reduce(tuple(scalar*v for v in x))

    def total(self, values):
        result = ZERO
        for value in values:
            result = self.add(result, value)
        return result


def check(category, condition):
    COUNTS[category] += 1
    assert condition, category


def masks(n, size, excluded=0):
    available = [i for i in range(n) if not (excluded >> i) & 1]
    return [sum(1 << i for i in choice) for choice in combinations(available, size)]


def block_table(rows, n, ring):
    """All terminal subset values using shared ordered prefix DP."""
    values = {0: ONE}
    for size, row in enumerate(rows, 1):
        for mask in masks(n, size):
            if size == 1:
                values[mask] = row[mask.bit_length() - 1]
            else:
                values[mask] = ring.total(
                    ring.mul(values[mask ^ (1 << i)], row[i])
                    for i in range(n) if (mask >> i) & 1)
    return {mask: values[mask] for mask in masks(n, len(rows))}


def upper_zeta(table, n, degree, ring):
    values = {mask: table.get(mask, ZERO)
              for size in range(degree + 1) for mask in masks(n, size)}
    keys = tuple(values)
    for i in range(n):
        bit = 1 << i
        for mask in keys:
            if mask & bit:
                values[mask ^ bit] = ring.add(values[mask ^ bit], values[mask])
    return values


def direct_disjoint(tables, ring):
    answer = ZERO
    for a, x in tables[0].items():
        for b, y in tables[1].items():
            if a & b:
                continue
            for c, z in tables[2].items():
                if not ((a | b) & c):
                    answer = ring.add(answer, ring.mul(ring.mul(x, y), z))
    return answer


def marker_expansion(zeta, n, ring):
    answer = ZERO
    # Independent per-column expansion: none, AB, AC, BC, ABC.
    for roles in product(range(5), repeat=n):
        a = b = c = g = 0
        scalar = 1
        for i, role in enumerate(roles):
            bit = 1 << i
            if role == 1:
                a |= bit; scalar = -scalar
            elif role == 2:
                b |= bit; scalar = -scalar
            elif role == 3:
                c |= bit; scalar = -scalar
            elif role == 4:
                g |= bit; scalar *= 2
        x = zeta[0].get(a | b | g, ZERO)
        y = zeta[1].get(a | c | g, ZERO)
        z = zeta[2].get(b | c | g, ZERO)
        answer = ring.add(answer, ring.scale(scalar, ring.mul(ring.mul(x, y), z)))
    return answer


def grouped_triangle(zeta, n, lengths, ring, reverse_last=False):
    answer = ZERO
    l1, l2, l3 = lengths
    for g in range(min(lengths) + 1):
        for fixed in masks(n, g):
            for a in range(min(l1, l2) - g + 1):
                for b in range(min(l1 - g - a, l3 - g) + 1):
                    for c in range(min(l2 - g - a, l3 - g - b) + 1):
                        aa, bb, cc = masks(n, a, fixed), masks(n, b, fixed), masks(n, c, fixed)
                        # First factor has indices (B,A), second (A,C).
                        left = {(j, i): zeta[0].get(i | j | fixed, ZERO)
                                if not i & j else ZERO for j in bb for i in aa}
                        middle = {(i, t): zeta[1].get(i | t | fixed, ZERO)
                                  if not i & t else ZERO for i in aa for t in cc}
                        value = ZERO
                        for j in bb:
                            for t in cc:
                                if j & t:
                                    continue
                                entry = ring.total(ring.mul(left[j, i], middle[i, t]) for i in aa)
                                right = zeta[2].get(j | t | fixed, ZERO)
                                value = ring.add(value, ring.mul(right, entry) if reverse_last
                                                 else ring.mul(entry, right))
                        scalar = (-1 if (a+b+c) % 2 else 1) * 2**g
                        answer = ring.add(answer, ring.scale(scalar, value))
    return answer


def direct_rows(rows, n, ring):
    answer = ZERO
    for columns in permutations(range(n), len(rows)):
        term = ONE
        for row, column in zip(rows, columns):
            term = ring.mul(term, row[column])
        answer = ring.add(answer, term)
    return answer


def main():
    start = time.monotonic()
    rng = random.Random(2026102709)
    for a, b, c in product((0, 1), repeat=3):
        check('local_integer_indicator', 1-a*b-a*c-b*c+2*a*b*c == int(a+b+c <= 1))

    reversed_order_failures = 0
    cases = [(3, (1, 1, 0)), (3, (1, 1, 1)), (4, (2, 1, 1)),
             (4, (1, 2, 1)), (4, (2, 2, 0)), (4, (2, 2, 1)),
             (5, (2, 2, 1)), (6, (2, 2, 2))]
    for modulus in (0, 2, 4, 6):
        ring = MatrixRing(modulus)
        for n, lengths in cases:
            rows = [[ring.reduce(tuple(rng.randrange(-2, 3) for _ in range(4)))
                     for _ in range(n)] for _ in range(sum(lengths))]
            tables = []
            offset = 0
            for length in lengths:
                tables.append(block_table(rows[offset:offset+length], n, ring))
                offset += length
            zeta = [upper_zeta(table, n, length, ring)
                    for table, length in zip(tables, lengths)]
            for table, transformed in zip(tables, zeta):
                for required, value in transformed.items():
                    direct = ring.total(v for mask, v in table.items() if mask & required == required)
                    check('upper_zeta_against_direct_supersets', value == direct)
            oracle = direct_rows(rows, n, ring)
            check('ordered_block_subset_dp', direct_disjoint(tables, ring) == oracle)
            check('integer_marker_identity', marker_expansion(zeta, n, ring) == oracle)
            check('actual_ordered_triangle_profiles', grouped_triangle(zeta, n, lengths, ring) == oracle)
            if sum(lengths) > n:
                check('more_rows_than_columns', oracle == ZERO)
            if n <= 4 and all(lengths):
                reversed_order_failures += grouped_triangle(zeta, n, lengths, ring, True) != oracle

    # Arbitrary block weights ensure the identity does not depend on DP structure.
    ring = MatrixRing(4)
    n, lengths = 5, (2, 1, 2)
    tables = [{mask: tuple(rng.randrange(4) for _ in range(4)) for mask in masks(n, length)}
              for length in lengths]
    zeta = [upper_zeta(table, n, length, ring) for table, length in zip(tables, lengths)]
    oracle = direct_disjoint(tables, ring)
    check('arbitrary_noncommutative_block_weights', grouped_triangle(zeta, n, lengths, ring) == oracle)
    check('arbitrary_block_marker_identity', marker_expansion(zeta, n, ring) == oracle)
    check('ordered_multiplication_guard', reversed_order_failures > 0)

    class EvenMatrixRing(MatrixRing):
        """The nonunital subring 2 M_2(Z), with checked multiplication inputs."""
        def mul(self, x, y):
            assert all(v % 2 == 0 for v in x+y), 'unit escaped into nonunital computation'
            return super().mul(x, y)

    ring = EvenMatrixRing(0)
    n, lengths = 4, (1, 1, 2)
    rows = [[tuple(2*rng.randrange(-2, 3) for _ in range(4)) for _ in range(n)]
            for _ in range(sum(lengths))]
    tables = [block_table(rows[:1], n, ring), block_table(rows[1:2], n, ring),
              block_table(rows[2:], n, ring)]
    zeta = [upper_zeta(table, n, length, ring) for table, length in zip(tables, lengths)]
    check('nonunital_even_integer_matrix_ring',
          grouped_triangle(zeta, n, lengths, ring) == direct_rows(rows, n, MatrixRing(0)))
    result = {'status': 'PASS', 'utc': datetime.now(timezone.utc).isoformat(),
              'assertions': sum(COUNTS.values()), 'counts': dict(COUNTS),
              'rings': '2-by-2 matrices over Z and Z/mZ for m=2,4,6; also the nonunital subring 2 M_2(Z)',
              'row_cases': len(cases)*4, 'reversed_order_counterexamples': reversed_order_failures,
              'seed': 2026102709, 'elapsed_seconds': round(time.monotonic()-start, 6),
              'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'scope': 'Finite exact identities and actual ordered profile contraction only. Naive matrix multiplication is used; no asymptotic speed benchmark or priority certification.',
              'statistical_trials': False}
    destination = Path(__file__).resolve().parents[1]/'results/ordered_disjoint_triple_checks.json'
    destination.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
