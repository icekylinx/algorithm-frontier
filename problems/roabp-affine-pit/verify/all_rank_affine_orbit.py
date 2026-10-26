#!/usr/bin/env python3
"""Exact lazy prototype for the all-rank affine-orbit PIT candidate.

Promise: an n-variate scalar polynomial of known total degree <=D in
an unknown invertible affine orbit of a width-w ROABP, in one unknown
variable order. Local ranks, local degrees, and characteristic are
unrestricted. This program does not recognize that representation.

The proof is an internally audited candidate, not an external certificate.
The exact field implementation below is unchanged from the CP21 prototype.
Grid bounds are retained in factored form when expansion would be huge.
Only a complete traversal can return zero under the stated promise;
a query-limited traversal returns incomplete.
"""

from fractions import Fraction
from itertools import product
from math import isqrt, comb
import argparse
import json


def _trim(a):
    while a and a[-1] == 0:
        a.pop()
    return a


def _poly_rem(a, b, p):
    a = _trim(list(a))
    b = _trim(list(b))
    if not b:
        raise ZeroDivisionError("zero polynomial divisor")
    inverse = pow(b[-1], p - 2, p)
    while len(a) >= len(b):
        coefficient = a[-1] * inverse % p
        shift = len(a) - len(b)
        for i, value in enumerate(b):
            a[i + shift] = (a[i + shift] - coefficient * value) % p
        _trim(a)
    return a


def _poly_mul(a, b, p):
    if not a or not b:
        return []
    result = [0] * (len(a) + len(b) - 1)
    for i, left in enumerate(a):
        for j, right in enumerate(b):
            result[i + j] = (result[i + j] + left * right) % p
    return _trim(result)


def _poly_power(a, exponent, modulus, p):
    result = [1]
    while exponent:
        if exponent & 1:
            result = _poly_rem(_poly_mul(result, a, p), modulus, p)
        a = _poly_rem(_poly_mul(a, a, p), modulus, p)
        exponent >>= 1
    return result


def _poly_gcd(a, b, p):
    while b:
        a, b = b, _poly_rem(a, b, p)
    if not a:
        return []
    inverse = pow(a[-1], p - 2, p)
    return [(value * inverse) % p for value in a]


def _subtract_x(a, p):
    result = list(a) + [0] * max(0, 2 - len(a))
    result[1] = (result[1] - 1) % p
    return _trim(result)


def _irreducible(modulus, p):
    """Exact finite-field irreducibility test; intentionally elementary."""
    degree = len(modulus) - 1
    if degree == 1:
        return True
    x_power = [0, 1]
    for i in range(1, degree + 1):
        x_power = _poly_power(x_power, p, modulus, p)
        difference = _subtract_x(x_power, p)
        if i <= degree // 2 and len(_poly_gcd(modulus, difference, p)) > 1:
            return False
    return not difference


def _digits(value, p, length):
    result = []
    for _ in range(length):
        result.append(value % p)
        value //= p
    return result


class RationalField:
    characteristic = 0

    def element(self, value):
        return Fraction(value)

    def scalar(self, value):
        return Fraction(value)

    def add(self, a, b):
        return a + b

    def neg(self, a):
        return -a

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b

    def inv(self, a):
        return 1 / a

    def power(self, a, exponent):
        return a ** exponent

    def metadata(self):
        return {"field": "Q", "characteristic": 0}


class FiniteField:
    """Exact small-field prototype with elementary primality validation.

    Elements are base-p encodings in a polynomial basis, not integers mod q.
    Use scalar(k) to embed an integer coefficient, and element(k) to enumerate
    field points.  The trial-division primality check is intended for small p.
    """

    def __init__(self, p, minimum_size):
        if p < 2 or any(p % divisor == 0 for divisor in range(2, isqrt(p) + 1)):
            raise ValueError("characteristic must be prime")
        self.characteristic = self.p = p
        self.degree = 1
        self.size = p
        while self.size < minimum_size:
            self.degree += 1
            self.size *= p
        if self.degree == 1:
            self.modulus = [0, 1]
        else:
            self.modulus = None
            for encoding in range(1, self.size):
                coefficients = _digits(encoding, p, self.degree)
                if coefficients[0] == 0:
                    continue
                candidate = coefficients + [1]
                if _irreducible(candidate, p):
                    self.modulus = candidate
                    break
            assert self.modulus is not None

    def element(self, index):
        """Enumerate distinct field elements; this is not scalar embedding."""
        if not 0 <= index < self.size:
            raise ValueError("field-element index out of range")
        return index

    def scalar(self, value):
        return value % self.p

    def _encode(self, coefficients):
        result = 0
        for value in reversed(coefficients):
            result = result * self.p + value
        return result

    def add(self, a, b):
        if self.p == 2:
            return a ^ b
        return self._encode([(x + y) % self.p for x, y in
                             zip(_digits(a, self.p, self.degree),
                                 _digits(b, self.p, self.degree))])

    def neg(self, a):
        return self._encode([(-x) % self.p for x in
                             _digits(a, self.p, self.degree)])

    def sub(self, a, b):
        return self.add(a, self.neg(b))

    def mul(self, a, b):
        if self.degree == 1:
            return a * b % self.p
        coefficients = _poly_mul(_digits(a, self.p, self.degree),
                                 _digits(b, self.p, self.degree), self.p)
        return self._encode(_poly_rem(coefficients, self.modulus, self.p))

    def power(self, a, exponent):
        result = 1
        while exponent:
            if exponent & 1:
                result = self.mul(result, a)
            a = self.mul(a, a)
            exponent >>= 1
        return result

    def inv(self, a):
        if not a:
            raise ZeroDivisionError("zero has no inverse")
        return self.power(a, self.size - 2)

    def metadata(self):
        return {"field": "finite extension", "characteristic": self.p,
                "size": self.size, "extension_degree": self.degree,
                "modulus_low_to_high": self.modulus,
                "element_encoding": "base-p polynomial coefficients"}


def rank_budgets(width):
    if width < 1:
        raise ValueError("width must be positive")
    levels = []
    for rank in range(1, width):
        compound_width = comb(width, rank)
        support_plus_two = rank + 2
        for s in range(rank + 2, width + 1):
            support_plus_two *= comb(s - 1, rank - 1) + 1
        support = support_plus_two - 2
        pairs = (compound_width ** 2 - 1) * (2 * support + 2)
        levels.append({"rank": rank, "compound_width": compound_width,
                       "chunk_support_bound": support, "pairs": pairs})
    return levels


class HittingGrid:
    """Moment curve plus K(w) pairs; use the smaller of two proved grids.

    The one-variable case is simplified to ordinary univariate interpolation.
    Large exact counts stay factored to avoid allocating an enormous integer.
    """

    def __init__(self, n, total_degree, width, characteristic=0):
        if n < 1 or total_degree < 1 or width < 1:
            raise ValueError("use one direct evaluation for constant models")
        self.n, self.total_degree_bound, self.width = n, total_degree, width
        self.levels = rank_budgets(width)
        self.theorem_pairs = sum(level["pairs"] for level in self.levels)
        self.pairs = 0 if n == 1 else self.theorem_pairs
        self.t_length = n * total_degree + 1
        self.amplitude_length = total_degree + 1
        self.basic_direction_length = (n - 1) * total_degree + 1
        self.refined_direction_length = (n - 1) * (n + 2) * (n + 3) // 2 + 1
        self.direction_length = min(self.basic_direction_length, self.refined_direction_length)
        self.direction_method = ("scalar-degree grid" if self.basic_direction_length <=
                                 self.refined_direction_length else "interval-family direction grid")
        self.field = (RationalField() if characteristic == 0 else
                      FiniteField(characteristic, self.t_length))
        self.nodes = [self.field.element(i) for i in range(n)]
        self._direction_cache = {}

    def query_count(self):
        factors = {"curve_grid": self.t_length, "amplitude_grid": self.amplitude_length,
                   "direction_grid": self.direction_length, "pair_count": self.pairs,
                   "formula": "curve_grid * (amplitude_grid * direction_grid)^pair_count"}
        bit_bound = (self.t_length.bit_length() + self.pairs *
                     (self.amplitude_length.bit_length() + self.direction_length.bit_length()))
        if bit_bound <= 8192:
            factors["exact_integer"] = (self.t_length *
                (self.amplitude_length * self.direction_length) ** self.pairs)
        else:
            factors["exact_integer"] = None
            factors["reason_not_expanded"] = "exact factored bound retained; expansion is unnecessary"
        return factors

    def lagrange(self, y):
        field = self.field
        values = []
        for i, node in enumerate(self.nodes):
            numerator = denominator = field.element(1)
            for j, other in enumerate(self.nodes):
                if i != j:
                    numerator = field.mul(numerator, field.sub(y, other))
                    denominator = field.mul(denominator, field.sub(node, other))
            values.append(field.mul(numerator, field.inv(denominator)))
        return values

    def evaluate_map(self, t, directions, amplitudes):
        if len(directions) != self.pairs or len(amplitudes) != self.pairs:
            raise ValueError("the map requires exactly its stated number of seed pairs")
        field = self.field
        point = [field.power(t, i + 1) for i in range(self.n)]
        for y, z in zip(directions, amplitudes):
            if z == 0:
                continue
            point = [field.add(x, field.mul(z, value))
                     for x, value in zip(point, self.lagrange(y))]
        return point

    def points(self):
        field = self.field
        for ti in range(self.t_length):
            base = [field.power(field.element(ti), i + 1) for i in range(self.n)]
            for directions in product(range(self.direction_length), repeat=self.pairs):
                for amplitudes in product(range(self.amplitude_length), repeat=self.pairs):
                    point = list(base)
                    for yi, zi in zip(directions, amplitudes):
                        if zi == 0:
                            continue
                        if yi not in self._direction_cache:
                            self._direction_cache[yi] = self.lagrange(field.element(yi))
                        z = field.element(zi)
                        point = [field.add(x, field.mul(z, value)) for x, value in
                                 zip(point, self._direction_cache[yi])]
                    yield (ti, directions, amplitudes), point

    def test(self, oracle, max_queries=None):
        if max_queries is not None and max_queries < 0:
            raise ValueError("max_queries must be nonnegative")
        if max_queries == 0:
            return {"status": "incomplete", "queries": 0, "query_bound": self.query_count()}
        count = 0
        for seeds, point in self.points():
            if max_queries is not None and count >= max_queries:
                return {"status": "incomplete", "queries": count, "query_bound": self.query_count()}
            value = oracle(point, self.field)
            count += 1
            if value != 0:
                return {"status": "nonzero", "queries": count, "seed_indices": seeds,
                        "point": point, "value": value}
        return {"status": "zero_under_all_rank_affine_orbit_candidate_theorem",
                "queries": count, "query_bound": self.query_count(), "completed_grid": True}

    def metadata(self):
        return {**self.field.metadata(), "variables": self.n,
                "scalar_total_degree_bound": self.total_degree_bound,
                "width_bound": self.width, "local_rank_restriction": None,
                "local_degree_bound_required": False,
                "theorem_pair_bound": self.theorem_pairs, "used_pairs": self.pairs,
                "one_variable_interpolation_simplification": self.n == 1,
                "parameter_count": 2 * self.pairs + 1,
                "initial_curve": "(t,t^2,...,t^n) in every characteristic",
                "rank_stage_budgets": self.levels,
                "direction_method": self.direction_method,
                "query_bound": self.query_count(),
                "proof_status": "internally audited candidate; no external certification"}


def mixed_rank_example(point, field, shear=False):
    """Actual width4 word with rank3 and rank4 locals, scalar degree8.

    Four edge macros on E14,E42,E24,E43 each use distinct variables
    x_e at index2e-1 and y_e at index4e-2. Replace z_e by x_e^2-y_e.
    Split each macro into two original-field univariate factors. Unused
    coordinates use identity factors. Optional invertible input shear
    sets latent coordinate i to X_i+X_(i+1), preserving the model.
    """
    latent = ([field.add(point[i], point[i + 1]) for i in range(len(point) - 1)]
              + [point[-1]]) if shear else point
    zero, one = field.element(0), field.element(1)
    row = [one, zero, zero, zero]
    closed = one
    for edge, (i, j) in enumerate(((0, 3), (3, 1), (1, 3), (3, 2)), start=1):
        x, y = latent[2 * edge - 2], latent[4 * edge - 3]
        x_squared = field.power(x, 2)
        closed = field.mul(closed, field.sub(x_squared, y))
        rank_factor = [[one if a == b and a < 3 else zero for b in range(4)]
                       for a in range(4)]
        rank_factor[i][j] = x_squared
        shear_factor = [[one if a == b else zero for b in range(4)] for a in range(4)]
        shear_factor[i][j] = field.neg(y)
        factors = (rank_factor, shear_factor) if i < 3 else (shear_factor, rank_factor)
        for matrix in factors:
            new_row = []
            for column in range(4):
                value = zero
                for a in range(4):
                    value = field.add(value, field.mul(row[a], matrix[a][column]))
                new_row.append(value)
            row = new_row
    assert row[2] == closed
    return row[2]


def self_check():
    assert [sum(x["pairs"] for x in rank_budgets(w)) for w in range(1, 7)] == [0, 12, 128, 1500, 23718, 553854]
    cases = []
    for characteristic in (0, 2, 3, 5):
        grid = HittingGrid(14, 8, 4, characteristic)
        field = grid.field
        for j, node in enumerate(grid.nodes):
            assert grid.lagrange(node) == [field.element(int(i == j)) for i in range(grid.n)]
        curve_one = [field.element(1)] * 14
        assert mixed_rank_example(curve_one, field) == 0
        witnesses = []
        for shear in (False, True):
            found = None
            for yi in range(grid.n, grid.direction_length):
                directions = [field.element(0)] * grid.pairs
                directions[0] = field.element(yi)
                for zi in range(grid.amplitude_length):
                    amplitudes = [field.element(0)] * grid.pairs
                    amplitudes[0] = field.element(zi)
                    point = grid.evaluate_map(field.element(0), directions, amplitudes)
                    value = mixed_rank_example(point, field, shear)
                    if value != 0:
                        found = {"input_shear": shear, "curve_index": 0,
                                 "only_nonzero_amplitude_pair": 0,
                                 "direction_index": yi, "amplitude_index": zi,
                                 "value": value, "point": point}
                        break
                if found:
                    break
            assert found is not None
            witnesses.append(found)
        partial_grid = HittingGrid(2, 1, 4, characteristic)
        partial = partial_grid.test(lambda x, f: f.element(0), max_queries=17)
        assert partial["status"] == "incomplete" and partial["queries"] == 17
        tiny = HittingGrid(1, 3, 4, characteristic)
        complete = tiny.test(lambda x, f: f.element(0))
        assert complete["completed_grid"] and complete["queries"] == 4
        refined = HittingGrid(2, 20, 2, characteristic)
        assert refined.direction_length == 11 and refined.direction_method == "interval-family direction grid"
        cases.append({"field": field.metadata(), "mixed_rank_witnesses": witnesses,
                      "partial_traversal": partial, "complete_univariate_zero": complete,
                      "refined_direction_grid": refined.metadata()})
    return {"status": "exact prototype checks passed", "cases": cases,
            "scope": "Arithmetic, actual mixed-rank witnesses, parameters, and traversal semantics; not a proof certificate or exhaustive large-grid test."}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--self-check", action="store_true")
    parser.add_argument("--variables", type=int, default=4)
    parser.add_argument("--total-degree", type=int, default=4)
    parser.add_argument("--width", type=int, default=4)
    parser.add_argument("--characteristic", type=int, default=0)
    args = parser.parse_args()
    result = self_check() if args.self_check else HittingGrid(
        args.variables, args.total_degree, args.width, args.characteristic).metadata()
    print(json.dumps(result, indent=2, default=str))


if __name__ == "__main__":
    main()
