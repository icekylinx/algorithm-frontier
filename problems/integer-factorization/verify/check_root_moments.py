#!/usr/bin/env python3
"""Independent finite checks of root-moment factoring reductions.

Enumerates original integers and roots, evaluates the literal truncated-ring
weights, and checks signed carries and finite-field DFTs. This is neither a
fast factoring implementation nor a validation of the external contraction
theorem, its asymptotic complexity, or novelty. Standard library only.

Authors: icekylinx and GPT-6 Astra Pro.
SPDX-License-Identifier: Apache-2.0
"""
from __future__ import annotations

from collections import Counter
from math import gcd, isqrt


def prime_powers(number: int) -> list[tuple[int, int]]:
    """Deliberately elementary oracle for these finite verification cases."""
    result = []
    divisor = 2
    while divisor * divisor <= number:
        power = 1
        while number % divisor == 0:
            number //= divisor
            power *= divisor
        if power > 1:
            result.append((divisor, power))
        divisor += 1
    if number > 1:
        result.append((number, number))
    return result


def is_prime(number: int) -> bool:
    return number >= 2 and all(number % d for d in range(2, isqrt(number) + 1))


def selected_roots(number: int) -> list[int]:
    return [r for r in range(2, number - 1, 2) if (r * r - 1) % number == 0]


def multiply(left: dict[int, int], right: dict[int, int], ell: int,
             modulus: int) -> dict[int, int]:
    result: dict[int, int] = {}
    for a, u in left.items():
        for b, v in right.items():
            if a + b < ell:
                result[a + b] = (result.get(a + b, 0) + u * v) % modulus
    return {a: value for a, value in result.items() if value}


def factorial_bound(number: int) -> int:
    value, index = 1, 1
    while value * (index + 1) <= number:
        index += 1
        value *= index
    return index - 1


def check_separation(number: int, m: int, counts: Counter) -> None:
    n = number.bit_length()
    b = (n + m - 1) // m
    base = 1 << b
    roots = selected_roots(number)
    components = prime_powers(number)
    k, total = len(components), len(roots)
    assert total == (1 << (k - 1)) - 1
    assert k <= factorial_bound(number)
    digits = [[r // base**j % base for j in range(m)] for r in roots]
    moments = [sum(row[j] * r for row, r in zip(digits, roots)) for j in range(m)]
    signs = [[1 if r % q == 1 else -1 for r in roots] for _, q in components]
    signed = [[sum(row[j] * sign for row, sign in zip(digits, signs[i]))
               for j in range(m)] for i in range(k)]
    for i, (prime, power) in enumerate(components):
        assert all((moments[j] - signed[i][j]) % power == 0 for j in range(m))
        for h in range(k):
            if i == h:
                continue
            identity = sum(base**j * (signed[i][j] - signed[h][j]) for j in range(m))
            assert identity % prime == (1 << (k - 1)) % prime
            assert any((signed[i][j] - signed[h][j]) % prime for j in range(m))
            counts['ordered_prime_pair_separations'] += 1
    second = [[sum(row[j] * row[l] for row in digits) for l in range(m)]
              for j in range(m)]
    assert all(moments[j] == sum(base**l * second[j][l] for l in range(m))
               for j in range(m))
    bound = (base - 1) * total
    blocks = [number]
    for moment in moments:
        for shift in range(-bound, bound + 1):
            divisor = gcd(number, moment - shift)
            saturated = gcd(number, pow(divisor, n, number))
            assert all(saturated % q == 0 or saturated % p != 0
                       for p, q in components)
            next_blocks = []
            for block in blocks:
                common = gcd(block, saturated)
                next_blocks.extend(x for x in (common, block // common) if x > 1)
            blocks = next_blocks
            counts['gcd_scan_candidates'] += 1
    assert sorted(blocks) == sorted(q for _, q in components)
    counts['root_moment_parameter_cases'] += 1
    counts['selected_root_observations'] += total
    if k == 1:
        counts['prime_power_parameter_cases'] += 1


def check_first_moment_ring(number: int, m: int, counts: Counter) -> None:
    n = number.bit_length()
    b = (n + m - 1) // m
    base, ell = 1 << b, 2 * m + 1
    precision = n + b + factorial_bound(number) + 2
    modulus = 1 << precision
    contraction: Counter = Counter()
    roots = selected_roots(number)
    for root in roots:
        markers = {0: 1}
        # Explicit two-state transfer-chain evaluation, including final weights.
        state = [{0: 1}, {}]
        for i in range(n):
            bit, block = root >> i & 1, i // b
            markers = multiply(markers, {0: 1, m + 1 + block: (1 << (i % b)) * bit},
                               ell, modulus)
            transitioned = multiply(state[0], {0: (1 << i) * bit}, ell, modulus)
            state[1] = dict(Counter(state[1]) + Counter(transitioned))
        chain = dict(Counter(state[1]) + Counter(multiply(state[0], {m: 1}, ell, modulus)))
        value = multiply(markers, chain, ell, modulus)
        contraction.update(value)
    expected = {0: sum(roots), m: len(roots)}
    for j in range(m):
        expected[m + 1 + j] = sum(root * (root // base**j % base) for root in roots)
    assert dict(+contraction) == {a: x for a, x in expected.items() if x}
    assert all(x < modulus for x in contraction.values())
    counts['first_moment_ring_contractions'] += 1


def sidon_parameters(m: int) -> tuple[list[int], int]:
    prime = next(p for p in range(max(3, m), max(10, 2 * m + 2)) if is_prime(p))
    q = 2 * prime * prime
    shift = 2 * q + 1
    exponents = [shift + j + 2 * prime * (j * j % prime) for j in range(m)]
    return exponents, 2 * shift + 2 * q + 1


def check_second_moment_ring(number: int, counts: Counter) -> None:
    n = number.bit_length()
    m = isqrt(n - 1) + 1
    b = (n + m - 1) // m
    base = 1 << b
    exponents, ell = sidon_parameters(m)
    roots = selected_roots(number)
    k = len(prime_powers(number))
    # K=k is a verified upper bound in these local ring checks; the full
    # algorithm obtains a bound from trial division, checked separately below.
    modulus = 1 << (2 * b + k + 3)
    contraction: Counter = Counter()
    for root in roots:
        value = {0: 1}
        for i in range(n):
            weight, bit = 1 << (i % b), root >> i & 1
            a = exponents[i // b]
            unary = {0: 1, a: 2 * weight * bit, 2 * a: 2 * weight * weight * bit}
            value = multiply(value, unary, ell, modulus)
        contraction.update(value)
        counts['second_moment_root_polynomials'] += 1
    expected = {0: len(roots)}
    digits = [[r // base**j % base for j in range(m)] for r in roots]
    for j in range(m):
        expected[exponents[j]] = 2 * sum(row[j] for row in digits)
        for l in range(j, m):
            expected[exponents[j] + exponents[l]] = (2 if j == l else 4) * sum(
                row[j] * row[l] for row in digits)
    assert dict(+contraction) == {a: x for a, x in expected.items() if x}
    assert all(x < modulus for x in contraction.values())
    counts['second_moment_ring_contractions'] += 1


def dft(values: list[int], omega: int, prime: int) -> list[int]:
    length = len(values)
    return [sum(value * pow(omega, j * k, prime) for j, value in enumerate(values)) % prime
            for k in range(length)]


def grouped_dft(values: list[int], omega: int, prime: int) -> list[int]:
    length, width = len(values), isqrt(len(values))
    zeta = pow(omega, width, prime)
    middle = [[sum(values[j1 + width * j2] * pow(zeta, j2 * k1, prime)
                   for j2 in range(width)) % prime for k1 in range(width)]
              for j1 in range(width)]
    result = [0] * length
    for k1 in range(width):
        for k2 in range(width):
            result[k1 + width * k2] = sum(middle[j1][k1] * pow(omega, j1 * k1, prime)
                                         * pow(zeta, j1 * k2, prime)
                                         for j1 in range(width)) % prime
    return result


def check_fft(number: int, counts: Counter) -> None:
    n = number.bit_length()
    u = n.bit_length() - 1
    base, t = 1 << u, (n + u - 1) // u
    length = 1
    while length < 2 * t:
        length *= 4
    progression = 1
    while progression <= 8 * t * base**2 or progression % length:
        progression *= 2
    multiplier = 1
    while not is_prime(1 + multiplier * progression):
        multiplier += 1
    prime = 1 + multiplier * progression
    nonresidue = next(g for g in range(2, prime)
                      if pow(g, (prime - 1) // 2, prime) == prime - 1)
    omega = pow(nonresidue, (prime - 1) // length, prime)
    assert pow(omega, length, prime) == 1 and pow(omega, length // 2, prime) != 1

    def digits(value: int) -> list[int]:
        return [value // base**i % base for i in range(t)] + [0] * (length - t)

    def convolution(left: list[int], right: list[int]) -> list[int]:
        return [sum(left[j] * right[i - j] for j in range(i + 1)) for i in range(length)]

    for root in selected_roots(number):
        quotient = (root * root - 1) // number
        r, q, known = map(digits, (root, quotient, number))
        square, product = convolution(r, r), convolution(q, known)
        carries = [0]
        bound = t * (base - 1) + 1
        for i in range(length):
            difference = square[i] - product[i] - (i == 0) + carries[-1]
            assert difference % base == 0
            carries.append(difference // base)
            assert abs(carries[-1]) <= bound
        assert carries[-1] == 0
        vectors = [r, q, known, carries[:-1]]
        transformed = [dft(vector, omega, prime) for vector in vectors]
        assert all(grouped_dft(vector, omega, prime) == transform
                   for vector, transform in zip(vectors, transformed))
        R, Q, N, E = transformed
        assert all((R[k]**2 - Q[k] * N[k] - 1
                    - (base * pow(omega, (-k) % length, prime) - 1) * E[k]) % prime == 0
                   for k in range(length))
        # One perturbed internal carry must be rejected by the frequency sinks.
        wrong = carries[:-1].copy()
        wrong[1] += 1
        wrong_E = dft(wrong, omega, prime)
        assert any((R[k]**2 - Q[k] * N[k] - 1
                    - (base * pow(omega, (-k) % length, prime) - 1) * wrong_E[k]) % prime
                   for k in range(length))
        counts['signed_carry_dft_root_cases'] += 1
        counts['rejected_perturbed_carries'] += 1


def check_tiny_carry_relation(number: int, counts: Counter) -> None:
    """Exhaust both n-bit inputs, including nonroots and incorrect quotients."""
    n = number.bit_length()
    u = n.bit_length() - 1
    base, t = 1 << u, (n + u - 1) // u
    length = 1
    while length < 2 * t:
        length *= 4
    bound = t * (base - 1) + 1
    for root in range(1 << n):
        for quotient in range(1 << n):
            r = [root // base**i % base for i in range(t)]
            q = [quotient // base**i % base for i in range(t)]
            known = [number // base**i % base for i in range(t)]
            carry, accepted = 0, True
            for i in range(length):
                square = sum(r[j] * r[i - j] for j in range(t) if 0 <= i - j < t)
                product = sum(q[j] * known[i - j] for j in range(t) if 0 <= i - j < t)
                numerator = square - product - (i == 0) + carry
                if numerator % base:
                    accepted = False
                    break
                carry = numerator // base
                if abs(carry) > bound:
                    accepted = False
                    break
            accepted = accepted and carry == 0
            assert accepted == (root * root == 1 + quotient * number)
            counts['exhaustive_tiny_carry_assignments'] += 1


def main() -> None:
    counts: Counter = Counter()
    numbers = list(range(3, 802, 2)) + [945, 1155, 1575, 2835, 3465, 10395, 11025]
    for number in numbers:
        n = number.bit_length()
        for m in sorted({1, 2, min(n, (n - 1).bit_length()), n}):
            check_separation(number, m, counts)
        counts['distinct_original_odd_inputs'] += 1
        # Check the actual rough-residual bound, without treating arbitrary
        # small examples as if their small prime factors had been removed.
        h = isqrt(n - 1) + 1
        residual = number
        for candidate in range(2, (1 << h) + 1):
            while residual % candidate == 0:
                residual //= candidate
        if residual > 1:
            n_prime = residual.bit_length()
            K = (n_prime + h - 1) // h
            assert sum(next(e for e in range(1, n_prime + 1) if p**e == q)
                       for p, q in prime_powers(residual)) <= K
            assert K <= isqrt(n_prime - 1) + 1
            counts['nonempty_rough_residuals'] += 1
    for m in range(1, 51):
        exponents, ell = sidon_parameters(m)
        pair_sums = [exponents[j] + exponents[l] for j in range(m) for l in range(j, m)]
        assert len(set(pair_sums)) == len(pair_sums)
        assert max(exponents) < min(pair_sums) <= max(pair_sums) < ell
        assert 3 * min(exponents) >= ell
        counts['sidon_exponent_sets'] += 1
    for number in [3, 9, 15, 45, 105, 385, 945, 1155, 11025]:
        for m in [1, 2, min(4, number.bit_length())]:
            check_first_moment_ring(number, m, counts)
        check_second_moment_ring(number, counts)
        check_fft(number, counts)
    for number in [3, 5, 9, 15]:
        check_tiny_carry_relation(number, counts)
    print('PASS: independent finite checks; external contraction theorem and asymptotic solver not tested.')
    for key in sorted(counts):
        print(f'{key}: {counts[key]}')


if __name__ == '__main__':
    main()
