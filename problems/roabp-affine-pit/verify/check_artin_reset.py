#!/usr/bin/env python3
"""Exact, small Artin-ring stress tests; no symbolic package or sampling.

Two independently constructed examples test future-dependent reset controls
and a tight same-width source restart. Arithmetic is over Q and F_2 in
explicit monomial quotients. This is a finite verification of examples,
not a substitute for the general argument in the companion report.
"""
from fractions import Fraction
import argparse
from itertools import combinations, permutations
from pathlib import Path
import json


class Ring:
    def __init__(self, names, caps, characteristic=0):
        self.names, self.caps, self.p = tuple(names), tuple(caps), characteristic
        self.zero_exp = (0,) * len(caps)

    def scalar(self, a):
        return int(a) % self.p if self.p else Fraction(a)

    def const(self, a):
        a = self.scalar(a)
        return {self.zero_exp: a} if a else {}

    def var(self, i):
        e = list(self.zero_exp)
        e[i] = 1
        return {tuple(e): self.scalar(1)}

    def add(self, *polys):
        out = {}
        for poly in polys:
            for e, c in poly.items():
                out[e] = self.scalar(out.get(e, 0) + c)
                if not out[e]:
                    del out[e]
        return out

    def neg(self, poly):
        return {e: self.scalar(-c) for e, c in poly.items()}

    def mul(self, a, b):
        out = {}
        for e, c in a.items():
            for f, d in b.items():
                g = tuple(x + y for x, y in zip(e, f))
                if any(x > bound for x, bound in zip(g, self.caps)):
                    continue
                out[g] = self.scalar(out.get(g, 0) + c * d)
                if not out[g]:
                    del out[g]
        return out

    def product(self, *polys):
        out = self.const(1)
        for poly in polys:
            out = self.mul(out, poly)
        return out

    def inv_scalar(self, a):
        return pow(int(a), -1, self.p) if self.p else Fraction(1, 1) / a

    def inv_unit(self, poly):
        c = poly.get(self.zero_exp, self.scalar(0))
        assert c
        ci = self.inv_scalar(c)
        tail = self.mul(self.const(ci), self.add(poly, self.const(-c)))
        term, out = self.const(1), self.const(1)
        for _ in range(sum(self.caps) + 1):
            term = self.mul(term, self.neg(tail))
            out = self.add(out, term)
        assert not term
        out = self.mul(self.const(ci), out)
        assert self.mul(poly, out) == self.const(1)
        return out

    def describe(self, poly):
        records = []
        for e, c in sorted(poly.items()):
            monomial = '*'.join(
                name if power == 1 else f'{name}^{power}'
                for name, power in zip(self.names, e) if power
            ) or '1'
            records.append({'monomial': monomial, 'coefficient': str(c),
                            'support': sum(power > 0 for power in e)})
        return records


def diag(R, entries):
    return [[R.const(a if i == j else 0) for j in range(len(entries))]
            for i, a in enumerate(entries)]


def mmul(R, A, B):
    assert len(A[0]) == len(B)
    return [[R.add(*(R.mul(A[i][k], B[k][j]) for k in range(len(B))))
             for j in range(len(B[0]))] for i in range(len(A))]


def mprod(R, matrices):
    out = diag(R, [1] * len(matrices[0]))
    for A in matrices:
        out = mmul(R, out, A)
    return out


def det(R, A):
    n = len(A)
    out = {}
    for perm in permutations(range(n)):
        inversions = sum(perm[i] > perm[j] for i in range(n) for j in range(i+1, n))
        out = R.add(out, R.product(R.const((-1) ** inversions),
                                   *(A[i][perm[i]] for i in range(n))))
    return out


def field_rank(R, rows):
    if not rows:
        return 0
    A = [[R.scalar(c) for c in row] for row in rows]
    at = 0
    for j in range(len(A[0])):
        pivot = next((i for i in range(at, len(A)) if A[i][j]), None)
        if pivot is None:
            continue
        A[at], A[pivot] = A[pivot], A[at]
        ci = R.inv_scalar(A[at][j])
        A[at] = [R.scalar(ci*c) for c in A[at]]
        for i in range(len(A)):
            if i != at and A[i][j]:
                c = A[i][j]
                A[i] = [R.scalar(x-c*y) for x, y in zip(A[i], A[at])]
        at += 1
        if at == len(A):
            break
    return at


def coefficient_rows(R, A):
    rows = []
    for row in A:
        monomials = set().union(*(set(poly) for poly in row))
        for e in sorted(monomials):
            values = tuple(poly.get(e, R.scalar(0)) for poly in row)
            if any(values):
                rows.append(values)
    return rows


def span_contains(R, spanning, tested):
    return field_rank(R, spanning + tested) == field_rank(R, spanning)


def check_unit_rank(R, A):
    n = len(A)
    constant = [[p.get(R.zero_exp, R.scalar(0)) for p in row] for row in A]
    s = field_rank(R, constant)
    if s == 0:
        assert all(not p for row in A for p in row)
        return 0
    unit_found = False
    for rows in combinations(range(n), s):
        for cols in combinations(range(n), s):
            minor = det(R, [[A[i][j] for j in cols] for i in rows])
            if minor.get(R.zero_exp, 0):
                R.inv_unit(minor)
                unit_found = True
    assert unit_found
    if s < n:
        for rows in combinations(range(n), s+1):
            for cols in combinations(range(n), s+1):
                assert not det(R, [[A[i][j] for j in cols] for i in rows])
    return s


def interval_checks(R, matrices):
    records = []
    for i in range(len(matrices)):
        for j in range(i, len(matrices)):
            product = mprod(R, matrices[i:j+1])
            records.append({'first': i+1, 'last': j+1,
                            'unit_rank': check_unit_rank(R, product)})
    return records


def future_control_case(characteristic):
    R = Ring(['x', 'y'], [1, 2], characteristic)
    x, y = R.var(0), R.var(1)
    A1 = diag(R, [1, 1, 0])
    A1[0][1] = x
    A2 = [[R.const(1), {}, y],
          [y, {}, R.mul(y, y)],
          [{}, {}, R.const(1)]]
    P = mmul(R, A1, A2)
    intervals = interval_checks(R, [A1, A2])
    assert [v['unit_rank'] for v in intervals] == [2, 1, 2]
    B0 = [[R.const(1), {}, {}]]
    passive = [[{}, R.const(1), {}]]
    control = R.neg(R.mul(mmul(R, passive, P)[0][0], R.inv_unit(P[0][0])))
    assert control == R.add(R.neg(y), R.product(x, y, y))
    controlled_initial = [[control, R.const(1), {}]]
    state1 = mmul(R, controlled_initial, A1)
    state2 = mmul(R, state1, A2)
    assert all(not p for row in state2 for p in row)
    assert state1 == [[control, R.add(R.const(1), R.neg(R.mul(x, y))), {}]]
    actual1 = mmul(R, B0 + passive, A1)
    S1 = coefficient_rows(R, actual1)
    assert field_rank(R, S1) == 2
    assert span_contains(R, S1, coefficient_rows(R, state1))
    passive_state = [[{}, state1[0][1], state1[0][2]]]
    assert span_contains(R, [(0, 1, 0)], coefficient_rows(R, passive_state))
    assert any(e[1] for poly in state1[0] for e in poly)
    return {'field': 'Q' if not characteristic else f'F_{characteristic}',
            'ring_caps': R.caps, 'interval_checks': intervals,
            'control': R.describe(control),
            'controlled_state_after_first_layer': [R.describe(p) for p in state1[0]],
            'actual_prefix_coefficient_span_rank': field_rank(R, S1),
            'future_variables_really_occur': True,
            'coefficientwise_prefix_membership': True,
            'passive_remainder_membership': True,
            'final_controlled_output_zero': True}


def tight_source_case(characteristic):
    R = Ring(['a', 'b', 'x', 'y', 'c', 'd'], [1] * 6, characteristic)
    a, b, x, y, c, d = [R.var(i) for i in range(6)]
    matrices = [diag(R, [1, 1, 0]), diag(R, [1, 1, 0]),
                diag(R, [1, 0, 0]), diag(R, [1, 0, 0]),
                diag(R, [1, 1, 0]), diag(R, [1, 1, 0])]
    for A, i, j, variable in zip(matrices, [2, 1, 2, 0, 2, 1],
                                 [1, 2, 0, 2, 1, 2], [a,b,x,y,c,d]):
        A[i][j] = variable
    intervals = interval_checks(R, matrices)
    u = [[{}, {}, R.const(1)]]
    output = mmul(R, u, mprod(R, matrices))[0]
    expected = [R.product(a,b,x), R.product(a,b,x,y,c), R.product(a,b,x,y,c,d)]
    assert output == expected
    assert [max(sum(v > 0 for v in e) for e in p) for p in output] == [3,5,6]
    assert field_rank(R, coefficient_rows(R, [output])) == 3
    B = [[R.const(1), {}, {}]]
    passive_source = [[{}, {}, R.const(1)]]
    suffix = mprod(R, matrices[4:])
    response = mmul(R, passive_source, suffix)[0]
    assert response == [{}, c, R.mul(c, d)]
    stable_output = mmul(R, B, mprod(R, matrices[3:]))[0]
    assert stable_output == [R.const(1), R.mul(y,c), R.product(y,c,d)]
    for endpoint in [5,6]:
        restart_rows = mmul(R, B + passive_source, mprod(R, matrices[4:endpoint]))
        active_rows = [[row[0]] for row in restart_rows]
        assert field_rank(R, coefficient_rows(R, active_rows)) == 1
    passive_constant_product = [[R.const(1), {}], [{}, {}]]
    assert check_unit_rank(R, passive_constant_product) == 1
    return {'field': 'Q' if not characteristic else f'F_{characteristic}',
            'ring_caps': R.caps, 'all_interval_checks': intervals,
            'row_output': [R.describe(p) for p in output],
            'first_scalar_monomial_support': 6,
            'general_row_bound_R_3_1': 6,
            'stable_phase_output': [R.describe(p) for p in stable_output],
            'source_cost': 1, 'passive_suffix_response': [R.describe(p) for p in response],
            'largest_needed_suffix_support': 2,
            'weighted_budget_g_2': 3,
            'same_width_restart_active_space_preserved': True,
            'restart_suffix_passive_constant_rank': 1}


def nonzero_reset_case(characteristic, epsilon):
    R = Ring(['x', 'y'], [1, 2], characteristic)
    x, y = R.var(0), R.var(1)
    A1 = [[R.const(1), {}, x, {}],
          [{}, R.const(1), {}, x],
          [{}, {}, {}, {}], [{}, {}, {}, {}]]
    A2 = [[R.const(1), {}, {}, {}],
          [y, {}, {}, {}],
          [R.mul(R.const(epsilon), y), {}, R.const(1), {}],
          [{}, {}, y, {}]]
    intervals = interval_checks(R, [A1, A2])
    assert [v['unit_rank'] for v in intervals] == [2, 1, 2]
    P = mmul(R, A1, A2)
    control = R.neg(R.mul(y, R.inv_unit(P[0][0])))
    expected_control = R.add(R.neg(y), R.product(R.const(epsilon), x, y, y))
    assert control == expected_control
    B0 = [[R.const(1), {}, {}, {}]]
    p = [[{}, R.const(1), {}, {}]]
    initial = [[control, R.const(1), {}, {}]]
    state1 = mmul(R, initial, A1)
    state2 = mmul(R, state1, A2)
    assert all(not poly for row in state2 for poly in row)
    assert state1 == [[control, R.const(1), R.neg(R.mul(x,y)), x]]
    actual1 = coefficient_rows(R, mmul(R, B0+p, A1))
    assert span_contains(R, actual1, coefficient_rows(R, state1))
    F1 = [[R.const(1), {}, x], [{}, {}, {}], [{}, {}, {}]]
    F2 = [[{}, {}, {}], [{}, R.const(1), {}], [{}, y, {}]]
    Z1 = [[{}, x, {}]]
    left = mmul(R, [[R.const(1), {}, {}]], mmul(R, F1, F2))
    source_tail = mmul(R, Z1, F2)
    right = [[R.neg(R.mul(control, poly)) for poly in source_tail[0]]]
    assert left == right == [[{}, R.mul(x,y), {}]]
    assert any(poly for row in left for poly in row)
    assert span_contains(R, coefficient_rows(R, source_tail), coefficient_rows(R, left))
    source = [[{}, {}, R.const(1), {}]]
    restarted = mmul(R, B0+source, A2)
    global_final = coefficient_rows(R, mmul(R, B0+p, P))
    assert span_contains(R, global_final, coefficient_rows(R, restarted))
    assert field_rank(R, coefficient_rows(R, [[row[0]] for row in restarted])) == 1
    # The epsilon=1 variant uses the full Artin hypothesis, not a stable
    # polynomial lift: before imposing x^2=0 its indicated minor is x^2y^2.
    lift = Ring(['x', 'y'], [2, 2], characteristic)
    xl, yl = lift.var(0), lift.var(1)
    lift_minor = lift.add(lift.product(lift.add(lift.const(1),
                         lift.product(lift.const(epsilon), xl, yl)), xl, yl),
                         lift.neg(lift.mul(xl, yl)))
    assert lift_minor == lift.product(lift.const(epsilon), xl, xl, yl, yl)
    return {'field': 'Q' if not characteristic else f'F_{characteristic}',
            'epsilon': epsilon, 'ring_caps': R.caps,
            'interval_checks': intervals, 'control': R.describe(control),
            'controlled_state_after_first_layer': [R.describe(p) for p in state1[0]],
            'nonzero_reset_left_and_right': [R.describe(p) for p in left[0]],
            'one_block_source_tail': [R.describe(p) for p in source_tail[0]],
            'unweighted_span_inclusion': True,
            'actual_same_width_restart_is_reachable': True,
            'restart_active_projection_rank': 1,
            'minor_before_imposing_x_squared_zero': lift.describe(lift_minor),
            'original_polynomial_lift_rank_stable': epsilon == 0}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = {'status': 'all exact assertions passed',
              'method': 'sparse monomial-quotient arithmetic; exact field elimination; no sampling',
              'future_control': [future_control_case(p) for p in [0,2]],
              'tight_source_restart': [tight_source_case(p) for p in [0,2]],
              'nonzero_reset': [nonzero_reset_case(p, e) for p in [0,2] for e in [0,1]]}
    if args.output:
        args.output.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({'status': result['status'], 'certificate': str(args.output) if args.output else None,
                      'fields': ['Q', 'F_2'], 'interval_checks_per_field': 30}))


if __name__ == '__main__':
    main()
