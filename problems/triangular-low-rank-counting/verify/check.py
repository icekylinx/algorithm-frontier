"""Independent finite oracles for the actual exterior endpoint algorithm.

Authors: icekylinx and GPT-6 Astra Pro. SPDX-License-Identifier: Apache-2.0
Reference DP adapted from check_dag_endpoint_set_dp.py; character oracle from
check_low_rank_modular_immanants.py and check_triangular_immanant_extraction.py.
Run with PYTHONDONTWRITEBYTECODE=1; no dependencies beyond Python's library.
"""
from collections import Counter, defaultdict
from fractions import Fraction
from functools import lru_cache
from itertools import permutations, product
from math import comb, factorial
from pathlib import Path
from random import Random
import json
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'reference'))
from exterior import evaluate, extract_immanant, hamiltonian_prime_power


def sign(p):
    return (-1) ** sum(p[i] > p[j] for i in range(len(p)) for j in range(i + 1, len(p)))


def cycle_type(p):
    seen, result = set(), []
    for vertex in range(len(p)):
        if vertex in seen:
            continue
        length = 0
        while vertex not in seen:
            seen.add(vertex)
            length += 1
            vertex = p[vertex]
        result.append(length)
    return tuple(sorted(result, reverse=True))


def class_sums(matrix):
    answer = defaultdict(int)
    for p in permutations(range(len(matrix))):
        term = 1
        for i, j in enumerate(p):
            term *= matrix[i][j]
        answer[cycle_type(p)] += term
    return answer


def cycle_value(classes, colors, rooted=False):
    return sum((-colors) ** (len(typ) - int(rooted)) * value for typ, value in classes.items())


def determinant(matrix, subset):
    answer = 0
    for p in permutations(range(len(subset))):
        term = sign(p)
        for i, j in enumerate(p):
            term *= matrix[subset[i]][subset[j]]
        answer += term
    return answer


def direct_marked(matrix, colors):
    answer = defaultdict(int)
    for assignment in product(range(colors), repeat=len(matrix)):
        blocks = [[i for i, s in enumerate(assignment) if s == color] for color in range(colors)]
        term = 1
        for block in blocks:
            term *= determinant(matrix, block)
        answer[tuple(map(len, blocks))] += term
    return {degree: value for degree, value in answer.items() if value}


@lru_cache(None)
def partitions(n, largest=None):
    if n == 0:
        return ((),)
    largest = min(n, n if largest is None else largest)
    return tuple((k,) + tail for k in range(largest, 0, -1) for tail in partitions(n - k, k))


@lru_cache(None)
def rim_hooks(shape, length):
    result = []
    for smaller in partitions(sum(shape) - length):
        if len(smaller) > len(shape) or any((smaller[i] if i < len(smaller) else 0) > x
                                           for i, x in enumerate(shape)):
            continue
        cells = {(i, j) for i, x in enumerate(shape)
                 for j in range(smaller[i] if i < len(smaller) else 0, x)}
        if len(cells) != length or any((i + 1, j) in cells and (i, j + 1) in cells
                                      and (i + 1, j + 1) in cells for i, j in cells):
            continue
        reached = {next(iter(cells))}
        pending = list(reached)
        while pending:
            i, j = pending.pop()
            for adjacent in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                if adjacent in cells and adjacent not in reached:
                    reached.add(adjacent)
                    pending.append(adjacent)
        if reached == cells:
            result.append((smaller, (-1) ** (len({i for i, j in cells}) - 1)))
    return tuple(result)


@lru_cache(None)
def character(shape, typ):
    if not typ:
        return int(not shape)
    return sum(height_sign * character(smaller, typ[1:])
               for smaller, height_sign in rim_hooks(shape, typ[0]))


class Polynomial:
    """Small explicit Z[t_1,...,t_k] for checking complete marked output."""
    def __init__(self, colors, terms):
        self.colors = colors
        self.terms = {degree: value for degree, value in terms.items() if value}

    def coerce(self, other):
        return other if isinstance(other, Polynomial) else Polynomial(self.colors, {(0,) * self.colors: other})

    def __add__(self, other):
        other = self.coerce(other)
        result = dict(self.terms)
        for degree, value in other.terms.items():
            result[degree] = result.get(degree, 0) + value
        return Polynomial(self.colors, result)

    __radd__ = __add__

    def __neg__(self):
        return Polynomial(self.colors, {degree: -value for degree, value in self.terms.items()})

    def __mul__(self, other):
        other = self.coerce(other)
        result = defaultdict(int)
        for a, x in self.terms.items():
            for b, y in other.terms.items():
                result[tuple(i + j for i, j in zip(a, b))] += x * y
        return Polynomial(self.colors, result)

    __rmul__ = __mul__

    def __eq__(self, other):
        other = self.coerce(other)
        return self.colors == other.colors and self.terms == other.terms


class Dual:
    """The nonreduced ring (Z/4Z)[epsilon]/epsilon^2, not a field."""
    def __init__(self, constant, tangent=0):
        self.constant, self.tangent = constant % 4, tangent % 4

    @staticmethod
    def coerce(other):
        return other if isinstance(other, Dual) else Dual(other)

    def __add__(self, other):
        other = self.coerce(other)
        return Dual(self.constant + other.constant, self.tangent + other.tangent)

    __radd__ = __add__

    def __mul__(self, other):
        other = self.coerce(other)
        return Dual(self.constant * other.constant,
                    self.constant * other.tangent + self.tangent * other.constant)

    __rmul__ = __mul__

    def __neg__(self):
        return Dual(-self.constant, -self.tangent)

    def __eq__(self, other):
        other = self.coerce(other)
        return (self.constant, self.tangent) == (other.constant, other.tangent)


def instance(rng, n, width, ring=int):
    order = list(range(n))
    rng.shuffle(order)
    bmat = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i, n):
            bmat[order[i]][order[j]] = ring(rng.choice((-2, -1, 1, 2)))
    u = [[ring(rng.randrange(-2, 3)) for _ in range(width)] for _ in range(n)]
    v = [[ring(rng.randrange(-2, 3)) for _ in range(width)] for _ in range(n)]
    return bmat, u, v, order


def expanded(bmat, u, v):
    return [[bmat[i][j] + sum(a * b for a, b in zip(u[i], v[j]))
             for j in range(len(bmat))] for i in range(len(bmat))]


def main():
    rng = Random(20261102537)
    counts = Counter()
    covered_moduli = set()
    total_transitions = maximum_states = maximum_coefficients = 0

    def run(parts, colors, **kwargs):
        nonlocal total_transitions, maximum_states, maximum_coefficients
        value, stats = evaluate(*parts, colors, **kwargs)
        total_transitions += stats['transitions']
        maximum_states = max(maximum_states, stats['maximum_endpoint_states'])
        maximum_coefficients = max(maximum_coefficients, stats['maximum_coefficient_entries'])
        return value

    # Exact coefficient-ring evaluation, all roots including middle/last,
    # shuffled orders, dense triangular parts, signed factors, and width zero.
    for n in range(1, 7):
        for width in (0, 1, 2):
            parts = instance(rng, n, width)
            matrix = expanded(*parts[:3])
            classes = class_sums(matrix)
            for colors in (1, 2, 3):
                got = run(parts, colors)
                assert got == cycle_value(classes, colors)
                counts['exact_integer_negative_alpha'] += 1
                if colors == 1:
                    assert got == (-1) ** n * determinant(matrix, list(range(n)))
                    counts['determinant_controls'] += 1
                if width == 0:
                    counts['zero_width_controls'] += 1
                for root in sorted({parts[3][0], parts[3][n // 2], parts[3][-1]}):
                    got = run(parts, colors, root=root)
                    assert got == cycle_value(classes, colors, rooted=True)
                    counts['exact_rooted_cycle_polynomials'] += 1
            for modulus in (2, 3, 4, 5, 6, 8, 9):
                root = parts[3][-1]
                got = run(parts, modulus, root=root, modulus=modulus)
                assert got == classes.get((n,), 0) % modulus
                counts['modular_hamiltonian'] += 1
                counts['nonzero_modular_hamiltonian'] += got != 0
                covered_moduli.add(modulus)
                if n >= 2:
                    b, u, v, order = parts
                    no_diagonal = [[0 if i == j else b[i][j] for j in range(n)] for i in range(n)]
                    assert run((no_diagonal, u, v, order), modulus, root=root, modulus=modulus) == got
                    counts['diagonal_independence_controls'] += 1

    for prime, precision in ((2, 1), (2, 2), (2, 3), (2, 4), (3, 2)):
        for n in range(1, 6):
            parts = instance(rng, n, 1 + n % 2)
            classes = class_sums(expanded(*parts[:3]))
            modulus = prime ** precision
            combined = 0
            for j in range(1, precision + 1):
                value = run(parts, prime * j, root=parts[3][-1], modulus=modulus)
                assert value == cycle_value(classes, prime * j, rooted=True) % modulus
                combined += (-1) ** (j - 1) * comb(precision, j) * value
                counts['prime_power_component_evaluations'] += 1
            expected = classes.get((n,), 0) % modulus
            assert combined % modulus == expected
            assert hamiltonian_prime_power(*parts, prime, precision, root=parts[3][-1]) == expected
            counts['prime_power_hamiltonian'] += 1

    # Actual full marked exterior DP, followed by integral extraction; this
    # extends the checkpoint's scalar weighted checks and separate extraction.
    for n in range(1, 7):
        for colors in range(1, min(n, 3) + 1):
            for width in (1, 2):
                parts = instance(rng, n, width)
                matrix = expanded(*parts[:3])
                weights = [Polynomial(colors, {tuple(int(i == s) for i in range(colors)): 1})
                           for s in range(colors)]
                marked = run(parts, colors, weights=weights)
                actual = marked.terms if isinstance(marked, Polynomial) else {}
                assert actual == direct_marked(matrix, colors)
                counts['complete_marked_polynomials'] += 1
                classes = class_sums(matrix)
                for lam in partitions(n):
                    if len(lam) > colors:
                        continue
                    shape = tuple(sum(x >= j for x in lam) for j in range(1, max(lam) + 1))
                    expected = sum(character(shape, typ) * value for typ, value in classes.items())
                    assert extract_immanant(actual, lam, colors) == expected
                    counts['end_to_end_integer_immanants'] += 1
                    for modulus in (2, 3, 4, 6, 101):
                        modular = {degree: value % modulus for degree, value in actual.items()}
                        assert extract_immanant(modular, lam, colors) % modulus == expected % modulus
                        counts['modular_extraction_controls'] += 1

    for ring, name in ((lambda x: Fraction(x, 3), 'rational_ring'),
                       (lambda x: Dual(x, rng.randrange(4)), 'nonreduced_ring')):
        for n in range(1, 5):
            for width in (0, 1, 2):
                parts = instance(rng, n, width, ring=ring)
                classes = class_sums(expanded(*parts[:3]))
                for colors in (1, 2, 3):
                    assert run(parts, colors) == cycle_value(classes, colors)
                    assert run(parts, colors, root=parts[3][-1]) == cycle_value(classes, colors, True)
                    counts[name] += 2
                if name == 'nonreduced_ring':
                    assert run(parts, 4, root=parts[3][-1]) == classes.get((n,), 0)
                    counts['nonreduced_hamiltonian'] += 1

    # Nonzero controls at the pure low-rank HC boundary n=p*r.
    for prime, width in ((2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (5, 1)):
        types = [(a, a) for a in range(width) for _ in range(prime - 1)]
        types += [(a, (a + 1) % width) for a in range(width)]
        n = len(types)
        u = [[int(a == c) for c in range(width)] for a, _ in types]
        v = [[int(b == c) for c in range(width)] for _, b in types]
        parts = ([[0] * n for _ in range(n)], u, v, list(reversed(range(n))))
        value = run(parts, prime, root=0, modulus=prime)
        assert value == class_sums(expanded(*parts[:3])).get((n,), 0) % prime
        assert value == pow(factorial(prime - 1), width, prime) != 0
        counts['nonzero_pure_rank_boundary_controls'] += 1

    assert counts['nonzero_modular_hamiltonian'] > 0
    report = {'status': 'PASS', 'seed': 20261102537, 'counts': dict(sorted(counts.items())),
              'tested_moduli': sorted(covered_moduli), 'actual_dp_transitions': total_transitions,
              'largest_observed_endpoint_state_count': maximum_states,
              'largest_observed_coefficient_entry_count': maximum_coefficients,
              'scope': 'Finite exact checks of the implemented algorithm against permutation, determinant-partition, and Murnaghan--Nakayama oracles; not asymptotic or formal verification.'}
    Path(__file__).with_name('results.json').write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
