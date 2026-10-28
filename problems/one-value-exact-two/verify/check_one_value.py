"""Independent original-input checks of shared-budget one-value clients.

Copyright 2026 icekylinx. Authored by GPT-6 Astra Pro. Apache-2.0.
Finite count enumeration is confined to this checker, never the backend.
"""
from fractions import Fraction as F
from itertools import combinations, product
from pathlib import Path
import json
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'reference'))
from one_value import OneValue, Allocation


def uniform(q, rank, cap=1):
    return tuple(min(rank, cap*s.bit_count()) for s in range(1 << q))


def vectors(q, rank):
    return tuple(row for row in product(*(range(rank[1 << p]+1) for p in range(q)))
                 if all(sum(row[p] for p in range(q) if s >> p & 1) <= bound
                        for s, bound in enumerate(rank)))


def original(q, player, resources, costs, setup, budget):
    """Original bases and actual resource vectors; no derived LP/gate oracles."""
    answers = []
    for basis in combinations(range(q), player[-1]):
        if any(sum(1 for p in basis if s >> p & 1) > bound for s, bound in enumerate(player)):
            continue
        paid = sum((setup[p] for p in basis), F(0))
        if paid > budget: continue
        columns = tuple(tuple(row for row in vectors(q, rank)
                              if all(row[p] == 0 for p in range(q) if p not in basis))
                        for rank in resources)
        for rows in product(*columns):
            cost = paid+sum((x*c for row, charges in zip(rows, costs) for x, c in zip(row, charges)), F(0))
            if cost <= budget:
                quota = min((sum(row[p] for row in rows) for p in basis), default=None)
                answers.append((tuple(basis), tuple(rows), quota, cost))
    return answers


fixtures = [
    (0, (0,), (), (), (), F(0)),
    (2, (0, 0, 0, 0), (uniform(2, 2),), ((F(0), F(1)),), (F(0), F(0)), F(0)),
    (2, uniform(2, 1), (), (), (F(1), F(2)), F(0)),
    (2, uniform(2, 1), (), (), (F(0), F(1)), F(0)),
    (2, uniform(2, 1), (uniform(2, 8, 4),), ((F(0), F(100)),), (F(3), F(0)), F(3)),
    (3, (0, 1, 0, 1, 1, 1, 1, 1), ((0, 2, 4, 6, 0, 2, 4, 6),),
     ((F(1, 3), F(0), F(2)),), (F(0), F(0), F(1)), F(2, 3)),
    (3, tuple(min(1, (s & 3).bit_count())+bool(s & 4) for s in range(8)),
     (uniform(3, 4, 2), uniform(3, 1)),
     ((F(0), F(3, 2), F(1, 3)), (F(1), F(0), F(2))),
     (F(1), F(0), F(1, 2)), F(3)),
]
for q in (1, 2, 3):
    for seed in range(9):
        player = uniform(q, 1+seed % q)
        first = uniform(q, 1+seed % (2*q), 1+seed % 2)
        # Weighted coverage, including nonuniform singleton capacities.
        sets = tuple((1 << p) | (1 << ((p+seed) % q)) for p in range(q))
        second = tuple(sum(1+(h+seed) % 2 for h in range(q)
                           if any(s >> p & 1 and sets[p] >> h & 1 for p in range(q)))
                       for s in range(1 << q))
        costs = tuple(tuple(F((p+2*j+seed) % 4, 1+(p+j) % 2) for p in range(q)) for j in range(2))
        setup = tuple(F((2*p+seed) % 3, 2) for p in range(q))
        fixtures.append((q, player, (first, second), costs, setup, F(seed % 6)))
# Four nonloop players exercise the actual logarithmic-block cover.
fixtures.append((4, uniform(4, 2), (uniform(4, 4),), ((F(0),)*4,), (F(0),)*4, F(0)))

checks = dict(instances=0, target_calls=0, optimizations=0, prescribed_optima=0,
              fixed_quota_tests=0, original_allocations=0, service_tests=0,
              protected_nodes=0, packing_rows=0, whole_ground_calls=0,
              binary_checks=0, invalid_rejections=0)
for q, player, resources, costs, setup, budget in fixtures:
    solver = OneValue(player, resources, costs, budget, setup, value=F(7, 3))
    actual = original(q, player, resources, costs, setup, budget)
    checks['original_allocations'] += len(actual)
    opt = max((row[2] for row in actual if row[2] is not None), default=0)
    zero = solver.zero()
    assert (zero is not None) == bool(actual)
    protected = next((row for row in actual if row[2] == opt), None)
    def observe(allowed, basis, residual, row):
        paid = sum(setup[p] for p in basis)
        assert residual == budget-paid >= 0
        if protected is not None and set(protected[0]) <= set(allowed):
            assert paid <= sum(setup[p] for p in protected[0])
            assert protected[3]-sum(setup[p] for p in protected[0]) <= residual
            checks['protected_nodes'] += 1
        if row is not None:
            checks['packing_rows'] += 1
            # Independent original allocations under the current ASSIGNMENT
            # budget, without setup and without restricting recipients to Q.
            for rows in product(*(vectors(q, rank) for rank in resources)):
                cost = sum((x*c for column, charge in zip(rows, costs) for x, c in zip(column, charge)), F(0))
                if cost <= residual:
                    service = tuple(sum(column[p] for column in rows) for p in range(q))
                    assert sum(a*x for a, x in zip(row.coefficients, service)) <= row.capacity
    if solver.rank:
        for basis in combinations(range(q), solver.rank):
            if player[sum(1 << p for p in basis)] != solver.rank: continue
            candidates = [row for row in actual if row[0] == basis]
            fixed_opt = max((row[2] for row in candidates), default=None)
            answer = solver.optimize_fixed(basis)
            assert (answer is None) == (fixed_opt is None)
            if answer is not None:
                assert solver.verify(answer) and solver.minimum(answer) == F(7, 3)*fixed_opt
            checks['prescribed_optima'] += 1
            for quota in range(5):
                answer = solver.fixed_quota(basis, quota)
                assert (answer is not None) == any(row[2] >= quota for row in candidates)
                if answer is not None:
                    assert all(sum(column[p] for column in answer.counts) == quota for p in basis)
                    assert solver.cost(answer) == min(row[3] for row in candidates if row[2] >= quota)
                checks['fixed_quota_tests'] += 1
    for d in (2, 3, 5):
        for whole in (False, True):
            for full in sorted({0, 1, d, d+1, opt, opt+1, solver.upper+1}):
                answer = solver.target(full, d, whole_ground=whole, observe=observe)
                if answer is None:
                    assert not actual or (solver.rank and opt < full)
                else:
                    assert solver.verify(answer)
                    if solver.rank:
                        assert solver.minimum(answer) >= F(7, 3)*((full+d-1)//d)
                checks['target_calls'] += 1
                checks['whole_ground_calls'] += int(whole)
            answer = solver.optimize(d, whole_ground=whole)
            assert (answer is None) == (not actual)
            if answer is not None and solver.rank:
                assert solver.minimum(answer) >= F(7, 3)*((opt+d-1)//d)
            checks['optimizations'] += 1
    # Direct membership and separator validity, including zero-budget rows.
    for level in (F(0), F(1, 2), F(2), F(9)):
        rates = (level,)*q
        row, witness = solver.service(rates, budget)
        if row is None:
            assert all(sum(column[p] for column in witness) == level for p in range(q))
            assert sum((c*x for column, charge in zip(witness, costs) for x, c in zip(column, charge)), F(0)) <= budget
            assert all(all(x >= 0 for x in column)
                       and all(sum(column[p] for p in range(q) if s >> p & 1) <= cap
                               for s, cap in enumerate(rank)) for column, rank in zip(witness, resources))
        else:
            assert min(row.coefficients, default=F(0)) >= 0 and row.capacity >= 0
            assert sum(a*t for a, t in zip(row.coefficients, rates)) > row.capacity
        checks['service_tests'] += 1
    checks['instances'] += 1

# This node changes its attaining setup basis after a violated budget row.
solver = OneValue(uniform(2, 1), (uniform(2, 8, 4),), ((0, 100),), 3, (3, 0))
answer = solver.target(4)
assert answer.basis == (0,) and solver.cost(answer) == 3 and solver.last_trace['nodes'] > 1
# Omission seeds restrict candidate bases, never the original resource rank.
for forced in ((), (0,), (1,), (0, 1)):
    answer = solver.target(4, forced=forced)
    assert (answer is not None) == (0 not in forced)
    if answer is not None: assert not set(answer.basis) & set(forced)

# More than 330-bit quotas and supplies go through actual optimization/LP;
# no checker count enumeration is used on these fixtures.
huge = 10**100
solver = OneValue((0, 1), ((0, huge),), ((F(2, 7),),), F(2*huge, 7)+F(1, 3), (F(1, 3),))
assert solver.optimize_fixed((0,)).counts == ((huge,),)
assert solver.fixed_quota((0,), huge+1) is None
checks['binary_checks'] += 1

# A full unit is unaffordable on this original coordinate; its half-unit
# fractional assignment must remain available in the count-service LP.
fractional = OneValue((0, 1), ((0, 3),), ((2,),), 1)
row, witness = fractional.service((F(1, 2),), 1)
assert row is None and witness == ((F(1, 2),),)
row, witness = fractional.service((F(1),), 1)
assert witness is None and row.capacity < row.coefficients[0]
answer = solver.optimize(d=2)
assert solver.minimum(answer) >= (huge+1)//2 and solver.verify(answer)
checks['binary_checks'] += 1
solver = OneValue((0, 1), ((0, huge),), ((F(0),),), 0)
answer = solver.optimize(d=huge, whole_ground=True)
assert answer.counts == ((1,),)
checks['binary_checks'] += 1
row, _ = solver.service((F(huge)+F(1, 10**90),), 0)
assert row is not None and row.capacity == huge
checks['binary_checks'] += 1

bad = [lambda: OneValue((0, 2), (), (), 0),
       lambda: OneValue((0, 1), ((0, 1),), ((-1,),), 0),
       lambda: OneValue((0, 1), ((0, 1),), ((0.5,),), 0),
       lambda: OneValue((0, 1), (), (), -1),
       lambda: OneValue((0, 1), (), (), 0, value=0),
       lambda: solver.target(2, d=1), lambda: solver.target(F(2)),
       lambda: solver.target(2, forced=(0, 0)),
       lambda: solver.target(2, forced=(0,), whole_ground=True),
       lambda: solver.target(2, whole_ground=True, cover_base=2),
       lambda: solver.fixed_quota((), 1), lambda: solver.fixed_quota((0,), -1),
       lambda: solver.service((1,), -1)]
for call in bad:
    try: call()
    except ValueError: checks['invalid_rejections'] += 1
    else: raise AssertionError('malformed original input accepted')
print(json.dumps({'status': 'PASS', **checks}, sort_keys=True))
