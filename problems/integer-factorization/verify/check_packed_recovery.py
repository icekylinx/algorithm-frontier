#!/usr/bin/env python3
"""Finite checks for the packed square-zero reduction (not a fast factoring backend).

Research attribution: Yilin Liu / GPT-6 Astra Pro.
SPDX-License-Identifier: Apache-2.0
All arithmetic here is exact.  GF(16), small matrices, and exhaustive small
root sets check the algebra/recovery interfaces; they do not test the external
tensor-contraction theorem, asymptotic complexity, or the full verifier graph.
"""

from itertools import combinations, product
from math import comb


R = 4
FIELD_SIZE = 1 << R
K = 4
Q_BITS = 3  # 2**Q_BITS = 2K moments
MASKS = 1 << Q_BITS
DIMENSION = R * MASKS


def mul(a, b):
    """GF(16) in the polynomial basis modulo X^4 + X + 1."""
    answer = 0
    while b:
        if b & 1:
            answer ^= a
        b >>= 1
        a <<= 1
        if a & FIELD_SIZE:
            a ^= 0b10011
    return answer


def power(a, exponent):
    answer = 1
    while exponent:
        if exponent & 1:
            answer = mul(answer, a)
        a = mul(a, a)
        exponent >>= 1
    return answer


def inverse(a):
    assert a
    return power(a, FIELD_SIZE - 2)


def trim(p):
    p = list(p)
    while p and p[-1] == 0:
        p.pop()
    return p


def poly_add(p, q):
    result = [0] * max(len(p), len(q))
    for i, a in enumerate(p):
        result[i] ^= a
    for i, a in enumerate(q):
        result[i] ^= a
    return trim(result)


def poly_mul(p, q):
    if not p or not q:
        return []
    result = [0] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            result[i + j] ^= mul(a, b)
    return trim(result)


def poly_divmod(p, q):
    p, q = trim(p), trim(q)
    assert q
    quotient = [0] * max(0, len(p) - len(q) + 1)
    leading_inverse = inverse(q[-1])
    while p and len(p) >= len(q):
        shift = len(p) - len(q)
        c = mul(p[-1], leading_inverse)
        quotient[shift] ^= c
        for i, a in enumerate(q):
            p[shift + i] ^= mul(c, a)
        p = trim(p)
    return trim(quotient), p


def poly_gcd(p, q):
    while q:
        p, q = q, poly_divmod(p, q)[1]
    if not p:
        return []
    c = inverse(p[-1])
    return [mul(a, c) for a in p]


def rank_and_solve(matrix, right=None):
    """Return rank and, for a nonsingular square matrix, its solution."""
    a = [list(row) + ([] if right is None else [right[i]])
         for i, row in enumerate(matrix)]
    rows = len(a)
    columns = len(matrix[0]) if rows else 0
    pivot_row = 0
    for column in range(columns):
        pivot = next((i for i in range(pivot_row, rows) if a[i][column]), None)
        if pivot is None:
            continue
        a[pivot_row], a[pivot] = a[pivot], a[pivot_row]
        c = inverse(a[pivot_row][column])
        a[pivot_row] = [mul(c, x) for x in a[pivot_row]]
        for i in range(rows):
            if i != pivot_row and a[i][column]:
                c = a[i][column]
                a[i] = [x ^ mul(c, y) for x, y in zip(a[i], a[pivot_row])]
        pivot_row += 1
        if pivot_row == rows:
            break
    solution = None
    if right is not None:
        assert rows == columns == pivot_row
        solution = [row[-1] for row in a]
    return pivot_row, solution


def trace_polynomial(beta, modulus):
    term = poly_divmod([0, beta], modulus)[1]
    answer = []
    for _ in range(R):
        answer = poly_add(answer, term)
        term = poly_divmod(poly_mul(term, term), modulus)[1]
    return answer


def split_by_traces(polynomial):
    factors = [polynomial]
    for u in range(R):
        trace = trace_polynomial(1 << u, polynomial)
        refined = []
        for factor in factors:
            zero = poly_gcd(factor, trace)
            one = poly_gcd(factor, poly_add(trace, [1]))
            assert poly_mul(zero, one) == factor
            refined.extend(part for part in (zero, one) if len(part) > 1)
        factors = refined
    assert all(len(factor) == 2 and factor[1] == 1 for factor in factors)
    return sorted(factor[0] for factor in factors)


def e_vector(a):
    return [power(a, mask) for mask in range(MASKS)]


def algebra_mul(a, b):
    """Independent square-zero monomial multiplication over GF(16)."""
    answer = [0] * MASKS
    for s, left in enumerate(a):
        for t, right in enumerate(b):
            if not s & t:
                answer[s | t] ^= mul(left, right)
    return answer


def bits_of_algebra(coefficients):
    return [(coefficient >> u) & 1
            for coefficient in coefficients for u in range(R)]


def matrix_columns(a):
    """Literal 0/1 regular representation; lists of nonzero row indices."""
    columns = []
    for s in range(MASKS):
        for u in range(R):
            column = []
            for t in range(MASKS):
                if s & t != s:
                    continue
                coefficient = mul(1 << u, power(a, t ^ s))
                for v in range(R):
                    if coefficient >> v & 1:
                        column.append(R * t + v)
            columns.append(column)
    return columns


MATRICES = [matrix_columns(a) for a in range(FIELD_SIZE)]


def integer_chain(groups, inspect_paths=False):
    # Columns are lifted to ordinary integers before this multiplication.
    counts = [0] * DIMENSION
    counts[0] = 1
    path_layers = {(0, 0): 1} if inspect_paths else None
    for a in groups:
        next_counts = [0] * DIMENSION
        for source, count in enumerate(counts):
            for target in MATRICES[a][source]:
                next_counts[target] += count
        counts = next_counts
        if inspect_paths:
            next_layers = {}
            for (source, strict), count in path_layers.items():
                for target in MATRICES[a][source]:
                    source_mask, target_mask = source // R, target // R
                    assert source_mask & target_mask == source_mask
                    if source_mask == target_mask:
                        assert source == target
                    changed = strict + (source_mask != target_mask)
                    assert changed <= Q_BITS
                    key = (target, changed)
                    next_layers[key] = next_layers.get(key, 0) + count
            path_layers = next_layers
    return counts


def ceil_log(value):
    assert value > 0
    return (value - 1).bit_length()


def guard_width(group_count):
    kappa = K.bit_length() - 1
    return (kappa + ceil_log(Q_BITS + 1)
            + Q_BITS * (ceil_log(group_count + 1) + ceil_log(DIMENSION)) + 3)


def packed_decode(counts, width, n):
    lanes = (DIMENSION + n - 1) // n
    ell = (DIMENSION + lanes - 1) // lanes
    precision = lanes * width
    assert ell <= n
    coefficients = [0] * ell
    for i, count in enumerate(counts):
        coefficients[i // lanes] += count << ((i % lanes) * width)
    # This is the literal (Z/2^P)[V]/(V^ell) output, with no field extension.
    coefficients = [c % (1 << precision) for c in coefficients]
    decoded = [(coefficients[i // lanes] >> ((i % lanes) * width))
               & ((1 << width) - 1) for i in range(DIMENSION)]
    return decoded


def check():
    for a in range(1, FIELD_SIZE):
        assert mul(a, inverse(a)) == 1
    cauchy_checks = 0
    for translation in range(1, FIELD_SIZE):
        for bit in range(R):
            if not (translation >> bit) & 1:
                continue
            half = [x for x in range(FIELD_SIZE) if not (x >> bit) & 1]
            cauchy = [[inverse(translation ^ x ^ y) for y in half] for x in half]
            rank, _ = rank_and_solve(cauchy)
            assert rank == FIELD_SIZE // 2
            cauchy_checks += 1
    identity_checks = 0
    for a, b in product(range(FIELD_SIZE), repeat=2):
        assert algebra_mul(e_vector(a), e_vector(b)) == e_vector(a ^ b)
        identity_checks += 1

    column_checks = 0
    for a in range(FIELD_SIZE):
        for source, column in enumerate(MATRICES[a]):
            basis = [0] * MASKS
            basis[source // R] = 1 << (source % R)
            expected = bits_of_algebra(algebra_mul(basis, e_vector(a)))
            assert column == [i for i, bit in enumerate(expected) if bit]
            column_checks += 1

    sequences = [groups for length in range(1, 4)
                 for groups in product(range(4), repeat=length)]
    sequences.extend([(1,) * 8, (1, 2, 4, 8) * 2, tuple(range(8))])
    for groups in sequences:
        counts = integer_chain(groups, inspect_paths=True)
        bound = sum(comb(len(groups), j) * DIMENSION ** j
                    for j in range(min(Q_BITS, len(groups)) + 1))
        assert max(counts) <= bound
        assert max(counts) < 1 << guard_width(len(groups))
        total = 0
        for a in groups:
            total ^= a
        assert [count & 1 for count in counts] == bits_of_algebra(e_vector(total))

    # Unguarded one-bit lanes lose parity through carries.  Two equal inputs
    # cancel in characteristic two but retain even integer matrix-path counts.
    carry_counts = integer_chain((1, 1))
    assert max(carry_counts) >= 2
    assert ([v & 1 for v in packed_decode(carry_counts, 1, 4)]
            != [v & 1 for v in carry_counts])

    # Each 4-bit element is an injective root encoding; groups use disjoint
    # input basis bits, as in the actual reduction.  Enumerate all sets <= K.
    root_counts = [integer_chain(tuple((x & (1 << i)) for i in range(R)))
                   for x in range(FIELD_SIZE)]
    root_sets = 0
    packing_checks = 0
    trace_checks = 0
    for size in range(K + 1):
        for roots in combinations(range(FIELD_SIZE), size):
            root_sets += 1
            counts = [sum(root_counts[x][i] for x in roots)
                      for i in range(DIMENSION)]
            width = guard_width(R)
            assert max(counts) < 1 << width
            for n in range(1, 10):
                assert packed_decode(counts, width, n) == counts
                packing_checks += 1
            moments = [0] * (2 * K)
            parity = [count & 1 for count in counts]
            for v in range(2 * K):
                moments[v] = sum(parity[v * R + u] << u for u in range(R))
                direct = 0
                for x in roots:
                    direct ^= power(x, v)
                assert moments[v] == direct
            hankel = [[moments[i + j] for j in range(K)] for i in range(K)]
            rank, _ = rank_and_solve(hankel)
            assert rank == size
            if not size:
                assert not any(moments)
                continue
            leading = [[moments[i + j] for j in range(size)] for i in range(size)]
            _, coefficients = rank_and_solve(leading, moments[size:2 * size])
            polynomial = coefficients + [1]
            direct_polynomial = [1]
            for x in roots:
                direct_polynomial = poly_mul(direct_polynomial, [x, 1])
            assert polynomial == direct_polynomial
            assert split_by_traces(polynomial) == list(roots)
            trace_checks += 1

    print(f"PASS: {identity_checks} square-zero group identities; "
          f"{column_checks} regular-representation columns; "
          f"{len(sequences)} integer-path/monotonicity cases")
    print(f"PASS: {root_sets} distinct-root sets (including empty sets, zero "
          f"roots, and even cardinalities); {packing_checks} guarded packings; "
          f"{trace_checks} Hankel/polynomial/trace recoveries")
    print("PASS: one-bit unguarded-lane carry counterexample detected")
    print(f"PASS: {cauchy_checks} characteristic-two Cauchy half-grid ranks "
          f"equal {FIELD_SIZE // 2} (full-grid template only)")
    print("Scope: GF(16), K=4; finite algebra/recovery checks only. "
          "No external contraction backend or asymptotic claim is tested.")


if __name__ == "__main__":
    check()
