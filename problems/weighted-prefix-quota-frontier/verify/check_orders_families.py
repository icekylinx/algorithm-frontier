"""Independent original-count optima, two-order marks and family stop chains.

Copyright 2026 icekylinx. Authored by GPT-6 Astra Pro. Apache-2.0.
The small count enumeration below is not part of the native clients.
"""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
from random import Random
import json
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'reference'))
from orders_families import TwoOrders, Families
from prefix import Solution
if not __debug__: raise SystemExit('Run with assertions enabled.')


def originals(solver):
    result = []
    for x in product(*(range(solver.rank[1 << e]+1) if e in solver.allowed else (0,) for e in range(solver.n))):
        if solver.mandatory and sum(x) != solver.total: continue
        if any(sum(x[e] for e in range(solver.n) if s >> e & 1) > cap for s, cap in enumerate(solver.rank)): continue
        for index, end, relation, target in solver.rows:
            weights, order = solver._weights(index), solver._order(index)
            value = sum(weights[e]*x[e] for e in order[:end])
            if (relation in ('<=', '=') and value > target) or (relation in ('>=', '=') and value < target): break
        else:
            result.append((x, sum((c*h for c, h in zip(solver.costs, x)), F(0))))
    return result


def two_marks(solver, plan, x):
    active = []
    for i, need in enumerate(solver.cover):
        row = [0]*solver.n
        for e in solver.orders[i]:
            w = min(solver.weights[e], solver.bound)
            if w and need > 0:
                row[e] = min(x[e], (need+w-1)//w); need -= row[e]*w
        assert need <= 0
        active.append(row)
    copied = []
    for e, bits in plan.copies:
        if e == solver.n: copied.append(solver.total-sum(x)); continue
        a, b = active[0][e], active[1][e]
        values = {(1, 1): min(a, b), (1, 0): max(0, a-b),
                  (0, 1): max(0, b-a), (0, 0): x[e]-max(a, b)}
        copied.append(values[bits])
    return tuple(copied)


def family_marks(solver, x):
    stops = {}
    for i, need in enumerate(solver.cover):
        if not need: continue
        before = 0
        for e in range(solver.n):
            w = min(solver.weights[i][e], solver.bound)
            if w and need <= w*x[e]:
                stops[i] = before+(need+w-1)//w; break
            need -= w*x[e]; before += x[e]
        assert i in stops
    chain = tuple(sorted(stops, key=lambda i: (stops[i], i)))
    plan = next(plan for plan in solver.plans() if plan.chain == chain)
    bounds = (0,)+tuple(stops[i] for i in chain)+(solver.total,)
    starts = tuple(sum(x[:e]) for e in range(solver.n))
    copied = tuple(solver.total-sum(x) if e == solver.n else
                   max(0, min(starts[e]+x[e], bounds[layer+1])-max(starts[e], bounds[layer]))
                   for e, layer in plan.copies)
    return plan, copied


def profile_of(solver, plan, copied):
    assert all(h >= 0 for h in copied) and sum(copied) == solver.total
    profile = tuple(sum(copied[i] for i in group) for _, _, group in plan.classes)
    assert sum(mass*h for (mass, _, _), h in zip(plan.classes, profile)) <= plan.cap
    assert solver._filter(plan, profile)
    return profile


counts = dict(two_instances=0, family_instances=0, exact_solves=0, original_vectors=0,
              marked_recoveries=0, plans=0, profiles=0, row_rejections=0,
              empty_faces=0, recovered=0, binary_checks=0, invalid_rejections=0)
rng = Random(20261028)
fixtures = []
for n in range(4):
    for seed in range(18):
        caps = tuple(1+(seed+e) % 2 for e in range(n))
        rank = tuple(min(1+seed % 3, sum(caps[e] for e in range(n) if s >> e & 1)) for s in range(1 << n))
        cost = tuple(F(rng.randrange(-3, 4), rng.randrange(1, 4)) for _ in range(n))
        weights = tuple(rng.randrange(4) for _ in range(n))
        order = list(range(n)); rng.shuffle(order)
        rows = tuple((rng.randrange(2), rng.randrange(n+1), rng.choice(('<=', '>=', '=')), rng.randrange(4))
                     for _ in range(seed % 4))
        fixtures.append(('two', rank, weights, cost, (tuple(range(n)), tuple(order)), rows))
        families = tuple(tuple(rng.randrange(4) for _ in range(n)) for _ in range(1+seed % 3))
        rows = tuple((rng.randrange(len(families)), rng.randrange(n+1), rng.choice(('<=', '>=', '=')), rng.randrange(4))
                     for _ in range(seed % 4))
        fixtures.append(('family', rank, families, cost, (), rows))
# Distinct cuts inside one coordinate, zero family entries, tied stopping
# positions, nontrivial reversed order and a mandatory zero-cost completion.
fixtures.extend([
    ('two', (0, 3), (2,), (F(-1),), ((0,), (0,)), ((0, 1, '>=', 1), (1, 1, '>=', 3))),
    ('two', (0, 2, 2, 3, 2, 3, 3, 3), (1, 0, 2), (F(2), F(-1), F(1, 2)),
     ((0, 1, 2), (2, 1, 0)), ((0, 3, '>=', 2), (1, 1, '<=', 2))),
    ('family', (0, 3), ((1,), (1,), (2,)), (F(-2),), (),
     ((0, 1, '>=', 1), (1, 1, '>=', 1), (2, 1, '>=', 3))),
    ('family', (0, 2, 2, 3), ((1, 0), (0, 2), (0, 0)), (F(-1), F(2)), (),
     ((0, 2, '>=', 1), (1, 2, '>=', 2), (2, 1, '<=', 0))),
    ('family', (0, 2), (), (F(-1),), (), ()),
])
for kind, rank, weights, cost, orders, rows in fixtures:
    n = len(cost)
    for mandatory in (False, True):
        for allowed in sorted({tuple(range(n)), tuple(e for e in range(n) if e % 2 == 0)}):
            for maximize in (False, True):
                args = (rank, weights, cost, orders, rows) if kind == 'two' else (rank, weights, cost, rows)
                solver = (TwoOrders if kind == 'two' else Families)(*args, mandatory=mandatory, allowed=allowed, maximize=maximize)
                actual = originals(solver)
                expected = (max if maximize else min)((c for _, c in actual), default=None)
                answer = solver.solve()
                assert (answer is None) == (expected is None)
                if answer is not None: assert solver.verify(answer) and answer.cost == expected and (answer.counts, answer.cost) in actual
                for key in ('plans', 'profiles', 'row_rejections', 'empty_faces', 'recovered'):
                    counts[key] += solver.last_trace[key]
                for x, c in actual:
                    if kind == 'two':
                        plan = next(solver.plans()); copied = two_marks(solver, plan, x)
                    else: plan, copied = family_marks(solver, x)
                    assert tuple(sum(h for (e, _), h in zip(plan.copies, copied) if e == p) for p in range(n)) == x
                    profile = profile_of(solver, plan, copied)
                    recovered = solver.realize(plan, profile)
                    assert recovered is not None and (recovered.cost >= c if maximize else recovered.cost <= c)
                    counts['marked_recoveries'] += 1
                counts['exact_solves'] += 1
                if not maximize: counts['original_vectors'] += len(actual)
            counts['two_instances' if kind == 'two' else 'family_instances'] += 1

huge = 10**100
for constructor in (TwoOrders, Families):
    for mandatory in (False, True):
        if constructor is TwoOrders:
            solver = constructor((0, huge), (huge+1,), (F(1, 10**110),), ((0,), (0,)),
                                 ((0, 1, '>=', huge), (1, 1, '>=', huge)), mandatory=mandatory)
        else:
            solver = constructor((0, huge), ((huge+1,), (huge+2,)), (F(1, 10**110),),
                                 ((0, 1, '>=', huge), (1, 1, '>=', huge)), mandatory=mandatory)
        answer = solver.solve()
        assert answer.counts == (huge if mandatory else 1,)
        assert solver.verify(answer) and solver.last_trace['max_copies'] <= 5 and solver.last_trace['profiles'] < 100
        counts['binary_checks'] += 1
# Large explicit family table with zero targets uses one layer, not 2^p.
solver = Families((0, huge), ((0,),)*1100, (F(-1),), ((1099, 1, '<=', 0),), mandatory=True)
assert solver.solve().counts == (huge,) and solver.last_trace['max_copies'] == 1
counts['binary_checks'] += 1
# Masking in one family excludes the original coordinate globally and cannot
# replace a mandatory original total by the restricted rank.
solver = Families((0, huge, huge, huge), ((0, 1), (1, 0)), (F(-1), F(-2)),
                  ((0, 2, '<=', 0),), allowed=(1,), mandatory=True)
assert solver.solve() is None
counts['binary_checks'] += 1

bad = [lambda: TwoOrders((0, 1), (1,), (0,), ((0,), (0, 0))),
       lambda: TwoOrders((0, 1), (-1,), (0,), ((0,), (0,))),
       lambda: TwoOrders((0, 1), (1,), (0,), ((0,), (0,)), ((2, 1, '<=', 1),)),
       lambda: Families((0, 1), ((1, 2),), (0,)), lambda: Families((0, 1), ((True,),), (0,)),
       lambda: Families((0, 1), (), (0,), ((0, 1, '>=', 1),)),
       lambda: Families((0, 1), ((1,),), (0,), ((0, 2, '>=', 1),)),
       lambda: Families((0, 1), ((1,),), (0,), ((0, 1, '<', 1),)),
       lambda: Families((0, 1), ((1,),), (0,), ((0, 1, '<=', -1),)),
       lambda: Families((0, 1), ((1,),), (0.5,)),
       lambda: Families((0, 1), ((1,),), (0,), allowed=(0, 0))]
for call in bad:
    try: call()
    except ValueError: counts['invalid_rejections'] += 1
    else: raise AssertionError('malformed original multi-prefix input accepted')
valid = Families((0, 2), ((1,),), (F(1),), ((0, 1, '<=', 1),), mandatory=False)
assert valid.verify(Solution((1,), F(1)))
assert not valid.verify(Solution((2,), F(2))) and not valid.verify(Solution((1,), F(0)))
print(json.dumps({'status': 'PASS', **counts}, sort_keys=True))
