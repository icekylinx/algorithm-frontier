#!/usr/bin/env python3
"""Exact all-characteristic affine-orbit hitting-set prototype.

Promise: a width-w ROABP with local generic ranks one or w, arbitrary
local degree, and unknown invertible affine input map and variable order.
The constructor uses a KNOWN SCALAR TOTAL DEGREE bound D. It does not
recognize the promise. The result holds over every characteristic.

The map uses a derivative-separating curve plus b(w) SV pairs, where
b(1)=0 and b(w)=max_k(binomial(w-2,k-1)+k-1). Finite grids have
n^(2b) (rho*D+1) (D+1)^b points. Enumeration is lazy; a partial traversal
returns incomplete, never a zero certificate. Extension-field oracle
evaluation must be supported when the base field is insufficient.

The field implementation is copied unchanged from the audited CP19
prototype; this file is standalone and requires only the standard library.
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


def exponents(n, characteristic):
    if characteristic < 0 or characteristic == 1:
        raise ValueError("characteristic must be zero or prime")
    chosen = []
    candidate = 1
    while len(chosen) < n:
        if not characteristic or candidate % characteristic:
            chosen.append(candidate)
        candidate += 1
    return chosen


def digit_bound(width):
    if width < 1:
        raise ValueError("width must be positive")
    if width == 1:
        return 0
    return max(comb(width - 2, k - 1) + k - 1
               for k in range(1, width))


class HittingGrid:
    """b(w) SV pairs plus a separating curve; exact lazy finite grid."""

    def __init__(self, n, total_degree, width, characteristic=0):
        if n < 1 or total_degree < 1 or width < 1:
            raise ValueError("use one direct evaluation for constant models")
        self.n, self.total_degree_bound, self.width = n, total_degree, width
        self.pairs = digit_bound(width)
        self.exponents = exponents(n, characteristic)
        self.t_length = self.exponents[-1] * total_degree + 1
        self.direction_length = n * n
        self.amplitude_length = total_degree + 1
        required_size = max(n, self.t_length, self.direction_length,
                            self.amplitude_length)
        self.field = (RationalField() if characteristic == 0 else
                      FiniteField(characteristic, required_size))
        self.nodes = [self.field.element(i) for i in range(n)]
        self.query_bound = (self.t_length * self.direction_length ** self.pairs *
                            self.amplitude_length ** self.pairs)
        self._directions = None

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
        """Accept actual field elements, not integer point indices."""
        if len(directions) != self.pairs or len(amplitudes) != self.pairs:
            raise ValueError("exactly b(width) directions and amplitudes are required")
        field = self.field
        point = [field.power(t, exponent) for exponent in self.exponents]
        for y, z in zip(directions, amplitudes):
            point = [field.add(x, field.mul(z, value))
                     for x, value in zip(point, self.lagrange(y))]
        return point

    def points(self):
        field = self.field
        if self._directions is None:
            self._directions = [self.lagrange(field.element(y))
                                for y in range(self.direction_length)]
        for ti in range(self.t_length):
            base = [field.power(field.element(ti), exponent)
                    for exponent in self.exponents]
            for ys in product(range(self.direction_length), repeat=self.pairs):
                selected = [self._directions[y] for y in ys]
                for zs in product(range(self.amplitude_length), repeat=self.pairs):
                    point = list(base)
                    for direction, zi in zip(selected, zs):
                        amplitude = field.element(zi)
                        point = [field.add(x, field.mul(amplitude, value))
                                 for x, value in zip(point, direction)]
                    yield (ti, *ys, *zs), point

    def metadata(self):
        return {**self.field.metadata(), "variables": self.n,
                "scalar_total_degree_bound": self.total_degree_bound,
                "initial_curve_exponents": self.exponents,
                "width_bound": self.width,
                "local_rank_promise": "one or full width",
                "digit_degree_bound": self.pairs,
                "parameter_count": 2 * self.pairs + 1,
                "t_grid_length": self.t_length,
                "each_direction_grid_length": self.direction_length,
                "each_amplitude_grid_length": self.amplitude_length,
                "query_bound": self.query_bound,
                "query_formula": "n^(2b(w)) (rho*D+1) (D+1)^b(w)"}

    def test(self, oracle, max_queries=None):
        if max_queries is not None and max_queries < 0:
            raise ValueError("max_queries must be nonnegative")
        count = 0
        for seeds, point in self.points():
            if max_queries is not None and count >= max_queries:
                return {"status": "incomplete", "queries": count,
                        "query_bound": self.query_bound}
            value = oracle(point, self.field)
            count += 1
            if value != 0:
                return {"status": "nonzero", "queries": count,
                        "seed_indices_t_ys_zs": seeds, "point": point,
                        "value": value}
        return {"status": "zero_under_rank_one_or_full_affine_orbit_promise",
                "queries": count, "query_bound": self.query_bound,
                "completed_grid": True}


def frobenius_example(point, field):
    """An actual width4 invertible word with local degree >= characteristic.

    The first two nilpotents are N1=E12+E34, the last two N2=E13+E24.
    Each local matrix is I+Y_i^q N_i, q=p in characteristic p and q=2
    over Q. Every determinant is one. The scalar degree is 2q, which
    is used as D rather than the larger n*q bound from local entries.
    """
    q = field.characteristic or 2
    ys = [field.add(point[i], point[i+1]) for i in range(3)] + [point[3]]
    powers = [field.power(y,q) for y in ys]
    zero, one = field.element(0), field.element(1)
    row = [one, zero, zero, zero]
    for index,value in enumerate(powers):
        matrix = [[one if i == j else zero for j in range(4)] for i in range(4)]
        for i,j in ([(0,1),(2,3)] if index < 2 else [(0,2),(1,3)]):
            matrix[i][j] = value
        row = [sum_field((field.mul(row[i],matrix[i][j]) for i in range(4)),field)
               for j in range(4)]
    closed = field.mul(field.add(powers[0],powers[1]),
                       field.add(powers[2],powers[3]))
    assert row[3] == closed
    return row[3]


def sum_field(values, field):
    result = field.element(0)
    for value in values:
        result = field.add(result,value)
    return result


def self_check():
    records = []
    for characteristic in (0,2,3,5):
        q = characteristic or 2
        grid = HittingGrid(4,2*q,4,characteristic)
        field = grid.field
        for j,node in enumerate(grid.nodes):
            assert grid.lagrange(node) == [field.element(int(i == j)) for i in range(4)]
        witness = grid.test(frobenius_example,max_queries=3000)
        assert witness['status'] == 'nonzero' and witness['value'] == field.element(1)
        partial = grid.test(lambda x,f:f.element(0),max_queries=17)
        assert partial['status'] == 'incomplete' and partial['queries'] == 17
        tiny = HittingGrid(1,1,4,characteristic)
        full = tiny.test(lambda x,f:f.element(0))
        assert full['completed_grid'] and full['queries'] == tiny.query_bound == 16
        records.append({'grid':grid.metadata(),'frobenius_word_witness':witness,
                        'partial_zero':partial,'one_variable_complete_zero':full})
    small_degree = HittingGrid(5,1,4,2)
    assert small_degree.field.size >= 25
    linear_witness = small_degree.test(lambda x,f:x[0],max_queries=3)
    assert linear_witness['status'] == 'nonzero'
    width_five = HittingGrid(1,1,5,2)
    width_five_zero = width_five.test(lambda x,f:f.element(0))
    assert width_five_zero['queries'] == width_five.query_bound == 64
    scalar = HittingGrid(3,6,1,2)
    scalar_witness = scalar.test(lambda x,f:f.power(f.mul(f.mul(x[0],x[1]),x[2]),2))
    assert scalar_witness['status'] == 'nonzero' and scalar.pairs == 0
    return {'status':'exact_all_characteristic_rank_one_or_full_checks_passed',
            'cases':records,
            'known_D_smaller_than_n':{'grid':small_degree.metadata(),
                                     'linear_witness':linear_witness},
            'width_five_complete_zero':width_five_zero,
            'width_one_curve_only':scalar_witness,
            'scope':'Arithmetic, examples and grid semantics only; the general theorem requires its proof.'}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--self-check',action='store_true')
    parser.add_argument('--variables',type=int,default=4)
    parser.add_argument('--total-degree',type=int,default=4)
    parser.add_argument('--width',type=int,default=4)
    parser.add_argument('--characteristic',type=int,default=0)
    args=parser.parse_args()
    result=self_check() if args.self_check else HittingGrid(
        args.variables,args.total_degree,args.width,args.characteristic).metadata()
    print(json.dumps(result,indent=2,default=str))


if __name__ == '__main__':
    main()
