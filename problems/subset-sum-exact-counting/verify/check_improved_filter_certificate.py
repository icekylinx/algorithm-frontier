# Copyright 2026 icekylinx and GPT-6 Astra Pro.
# SPDX-License-Identifier: Apache-2.0
"""Exact outward-rounded certificate for a modest counting exponent refinement.

No floating point is used in an assertion. The arithmetic reconstructs the
source's 64-point grid from rational Taylor series. Analytic quadrature and
node-score error bounds are the explicitly cited unchanged source bounds.
The changed parameters are checked against those analytic bounds and the
complete combinatorial exponent ledger.
"""
from fractions import Fraction as F
from math import factorial
from pathlib import Path
import json

SCALE = 1 << 160


def down(x):
    return F((x.numerator * SCALE) // x.denominator, SCALE)


def up(x):
    return -down(-x)


class I:
    def __init__(self, lo, hi=None):
        self.lo = down(F(lo))
        self.hi = up(F(lo if hi is None else hi))
        assert self.lo <= self.hi

    @staticmethod
    def make(x):
        return x if isinstance(x, I) else I(x)

    def __add__(self, other):
        o = self.make(other)
        return I(self.lo + o.lo, self.hi + o.hi)

    __radd__ = __add__

    def __neg__(self):
        return I(-self.hi, -self.lo)

    def __sub__(self, other):
        return self + -self.make(other)

    def __rsub__(self, other):
        return self.make(other) + -self

    def __mul__(self, other):
        o = self.make(other)
        candidates = [self.lo * o.lo, self.lo * o.hi,
                      self.hi * o.lo, self.hi * o.hi]
        return I(min(candidates), max(candidates))

    __rmul__ = __mul__

    def __truediv__(self, other):
        o = self.make(other)
        assert o.lo * o.hi > 0
        return self * I(1 / o.hi, 1 / o.lo)

    def __pow__(self, power):
        assert isinstance(power, int) and power >= 0
        ans, base = I(1), self
        while power:
            if power & 1:
                ans = ans * base
            power //= 2
            if power:
                base = base * base
        return ans

    def radius_bound(self):
        return max(abs(self.lo), abs(self.hi))


def exp_interval(value):
    value = I.make(value)
    divisions = 0
    while value.radius_bound() > 4:
        value = value / 2
        divisions += 1
    term = total = I(1)
    for j in range(1, 80):
        term = term * value / j
        total = total + term
    t = value.radius_bound()
    remainder = t ** 80 / F(factorial(80)) / (1 - t / 81)
    total = total + I(-remainder, remainder)
    for _ in range(divisions):
        total = total * total
    return total


def log_interval(value):
    value = I.make(value)
    assert value.lo > 0
    d = (value - 1) / (value + 1)
    t = d.radius_bound()
    assert t < 1
    term = d
    total = I(0)
    square = d * d
    for j in range(80):
        total = total + term * F(2, 2 * j + 1)
        term = term * square
    remainder = 2 * t ** 161 / F(161) / (1 - t * t)
    return total + I(-remainder, remainder)


LN2 = log_interval(2)


def exp2(value):
    return exp_interval(I.make(value) * LN2)


def log2(value):
    return log_interval(value) / LN2


def arctan_rational(x):
    total = F(0)
    for j in range(100):
        total += (-1) ** j * x ** (2 * j + 1) / (2 * j + 1)
    error = x ** 201 / 201
    return I(total - error, total + error)


PI = 4 * (arctan_rational(F(1, 2)) + arctan_rational(F(1, 3)))


def cosine(value):
    value = I.make(value)
    term = total = I(1)
    square = value * value
    for j in range(1, 40):
        term = -term * square / ((2 * j - 1) * (2 * j))
        total = total + term
    rem = value.radius_bound() ** 80 / F(factorial(80))
    return total + I(-rem, rem)


def exact_decimal_outward(value, digits=14):
    """Print a proven upper decimal bound, without converting to float."""
    value = F(value)
    scale = 10 ** digits
    q = -((-value.numerator * scale) // value.denominator)
    sign = '-' if q < 0 else ''
    q = abs(q)
    return f'{sign}{q // scale}.{q % scale:0{digits}d}'


def main():
    ngrid = 64
    cosines = []
    for j in range(ngrid):
        if j in (0, 16, 32, 48):
            cosines.append(I({0: 1, 16: 0, 32: -1, 48: 0}[j]))
        else:
            jj = j if j <= 32 else j - 64
            cosines.append(cosine(PI * F(jj, 32)))
    rr = list(map(F, ['.851', '.466', '.325', '.253', '.224', '-.314']))
    ss = list(map(F, ['1.281', '-.938', '.731', '-.559', '.391', '.110']))
    r = [sum((rr[t - 1] * cosines[(t * j) % ngrid]
              for t in range(1, 7)), I(0)) for j in range(ngrid)]
    s = [sum((ss[t - 1] * cosines[(t * j) % ngrid]
              for t in range(1, 7)), I(0)) for j in range(ngrid)]
    kappa = F('1.0315')
    ff, gg = [exp2(x) for x in r], [exp2(x) for x in s]
    zf, zg = sum(ff, I(0)) / 64, sum(gg, I(0)) / 64
    zfk = sum((exp2(kappa * x) for x in r), I(0)) / 64
    zgk = sum((exp2(kappa * x) for x in s), I(0)) / 64
    hk = log2(zfk) + log2(zgk)

    tau, eta = F('.48982'), F('.51785')
    mu, gamma = F('.0574'), F('.4895')
    delta, alpha = F('.01019'), F('.01046')
    preliminary_cap = F('.48983')
    gap, budget = eta - tau, 2 * tau - eta
    ratio = gap / budget
    averages = [I(0), I(0)]
    max_u_error = F('0.0000002')
    max_v_error = F('0.000003')
    nodes = []
    for j in range(ngrid):
        products = [ff[(j + i) % ngrid] * gg[i] for i in range(ngrid)]
        pp = sum(products, I(0)) / 64
        yy = sum((products[i] * (r[(j + i) % ngrid] + s[i])
                  for i in range(ngrid)), I(0)) / 64
        raw_mean = yy / pp
        logp = log2(pp)
        uu = (kappa - 1) * raw_mean + logp - hk
        vv = (2 - kappa) * raw_mean - 2 * logp + hk
        magnitude_squared = 2 + 2 * cosines[j]
        # Source inner-quadrature score errors, propagated explicitly.
        assert max_u_error > F('1e-7') + (kappa - 1) * F('2e-6') + F('5e-9')
        assert max_v_error > 2 * F('1e-7') + (2 - kappa) * F('2e-6') + F('5e-9')
        x1 = magnitude_squared * exp2(F('8.5') * (gap - uu + max_u_error))
        x2 = magnitude_squared * exp2(F('8.3') * (ratio * (vv + max_v_error) - uu + max_u_error))
        averages[0] = averages[0] + x1 / 64
        averages[1] = averages[1] + x2 / 64
        nodes.append({'j': j, 'u_lower': exact_decimal_outward(-uu.lo),
                      'v_upper': exact_decimal_outward(vv.hi)})

    # The source analytic strip and normalizer bounds concern unchanged
    # densities. Verify that the new exponents still fit its same 2^20 bound.
    bb, ll, hh = F(13) / F('.46'), F('1.121'), F('.016')
    strip_e1 = F('8.5') * (gap + ll + (kappa - 1) * bb + hh)
    strip_e2 = F('8.3') * ((1 + 2 * ratio) * ll
                            + abs(ratio * (2 - kappa) - (kappa - 1)) * bb
                            + (1 + ratio) * hh)
    assert strip_e1 < F('17.6') and strip_e2 < F('17.6')
    assert (F('4.16') * exp2(F('17.6'))).hi < 2 ** 20
    error_interval = I(2 ** 21) / (exp_interval(F('24.32')) - 1)
    assert error_interval.hi < F('.00007')
    outer_error = F('.00007')
    integrals = [x.hi + outer_error for x in averages]
    continuous_rate = F('.5175')
    threshold = exp2(continuous_rate)
    assert all(x < threshold.lo for x in integrals)

    hquarter = -F(1, 4) * log2(F(1, 4)) - F(3, 4) * log2(F(3, 4))
    assert hquarter.hi < F('.81128')
    hbound = F('.81128')
    bit_guard_rate = F('.00001')
    list_rate = F('.5') + (hbound - F('.5') - gamma) * mu
    pair_rate = 1 + (2 * hbound - 1 - gamma) * mu - eta + bit_guard_rate
    setup_rate = F('.25') + mu
    assert list_rate < tau and pair_rate < tau and setup_rate < tau
    assert 17 * mu < 1 and delta < 17 * mu * alpha and gamma < F('.5') - alpha
    hmu = -mu * log2(mu) - (1 - mu) * log2(1 - mu)
    sparse_support_rate = hmu + mu
    assert sparse_support_rate.hi < F('.40')
    distinction_rate = sparse_support_rate + bit_guard_rate
    assert distinction_rate.hi < eta
    assert F('.5') - F('.01018') < preliminary_cap
    assert delta > F('.01018')
    assert eta / 2 < tau
    assert tau + 20 * F('1e-8') < F('.48984')
    assert preliminary_cap < F('.48984') < F('.48985') < F('.48986')

    report = {
        'status': 'PASS',
        'arithmetic': 'Exact Fraction interval arithmetic, rounded outward to 160 binary fractional bits',
        'parameters': {k: str(v) for k, v in dict(tau=tau, eta=eta, mu=mu,
                    gamma=gamma, delta=delta, alpha=alpha,
                    preliminary_cap=preliminary_cap).items()},
        'continuous_integral_upper_bounds': [exact_decimal_outward(x) for x in integrals],
        'continuous_rate': str(continuous_rate),
        'threshold_lower_bound_numerator': str(threshold.lo.numerator),
        'threshold_lower_bound_denominator': str(threshold.lo.denominator),
        'strip_exponent_upper_bounds': [exact_decimal_outward(strip_e1), exact_decimal_outward(strip_e2)],
        'outer_quadrature_error_upper': exact_decimal_outward(error_interval.hi),
        'list_rate_upper': str(list_rate),
        'pair_rate_upper_including_bit_guard': str(pair_rate),
        'generation_rate': str(setup_rate),
        'all_sparse_support_rate_upper': exact_decimal_outward(sparse_support_rate.hi),
        'prime_distinction_rate_upper_including_bit_guard': exact_decimal_outward(distinction_rate.hi),
        'scope': 'Validates the new fixed numerical certificate and exponent ledger; imports the named source analytic strip/inner error bounds and the general algorithm proofs, not their implementation.',
        'source_commit': '4eaee87548250b2682affda7d05d947c05554bae',
        'source_numerical_blob_sha': 'd9b2531441fcd7ac10b434746088de7d6d4e7576'
    }
    output = Path(__file__).with_name('improved_filter_results.json')
    output.write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
