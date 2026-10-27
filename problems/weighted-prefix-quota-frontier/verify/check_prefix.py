"""Original-input one-order prefix optima versus native profile recovery.

Copyright 2026 Yilin Liu. Authored by GPT-6 Astra Pro. Apache-2.0.
Small integer count enumeration occurs only in this independent checker.
"""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
from random import Random
import json
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'reference'))
from prefix import Prefix, Solution

if not __debug__:
    raise SystemExit('Run this finite checker with assertions enabled.')


def original(rank, weights, costs, rows, mandatory, allowed):
    n = len(weights)
    result = []
    for x in product(*(range(rank[1 << e]+1) if e in allowed else (0,) for e in range(n))):
        if mandatory and sum(x) != rank[-1]: continue
        if any(sum(x[e] for e in range(n) if s >> e & 1) > cap for s, cap in enumerate(rank)): continue
        passed = True
        for end, relation, target in rows:
            value = sum(w*y for w, y in zip(weights[:end], x[:end]))
            if (relation in ('<=', '=') and value > target) or (relation in ('>=', '=') and value < target):
                passed = False; break
        if passed: result.append((x, sum((c*y for c, y in zip(costs, x)), F(0))))
    return result


def marked_profile(solver, x):
    """Independent binary bulk form of the conceptual first-reaching mark."""
    credit = max((target for _, relation, target in solver.prepared if relation == '>='), default=0)
    active = [0]*solver.n
    for e in range(solver.n):
        weight = min(solver.weights[e], solver.bound)
        if weight and credit > 0:
            active[e] = min(x[e], (credit+weight-1)//weight)
            credit -= active[e]*weight
    copied = tuple((active[e] if bit else x[e]-active[e]) if e < solver.n else solver.total-sum(x)
                   for e, bit in solver.copies)
    assert all(v >= 0 for v in copied) and sum(copied) == solver.total
    profile = tuple(sum(copied[i] for i in group) for _, _, group in solver.classes)
    assert sum(weight*h for (weight, _, _), h in zip(solver.classes, profile)) <= solver.mass_cap
    assert solver._filter(profile)
    return profile


fixtures = [
    ((0,), (), (), ()),
    ((0, 2), (0,), (F(-3),), ()),
    ((0, 3), (7,), (F(2, 3),), ((1, '>=', 2),)),
    ((0, 3), (7,), (F(-1),), ((1, '<=', 2),)),
    ((0, 0, 2, 2), (0, 2), (F(-7), F(1)), ((0, '>=', 1),)),
    ((0, 3, 2, 4), (1, 0), (F(4), F(-2)), ((1, '>=', 1), (2, '<=', 2))),
    ((0, 2, 2, 4), (0, 3), (F(-2), F(1)), ((1, '<=', 0), (2, '>=', 2))),
    ((0, 1, 1, 1), (1, 2), (F(0), F(0)), ((1, '>=', 1), (2, '<=', 0))),
    ((0, 2, 2, 4), (1, 1), (F(1), F(-2)),
     ((1, '<=', 0), (1, '<=', 2), (2, '<=', 3), (1, '>=', 0), (2, '>=', 1))),
]
rng = Random(20261027)
for n in (1, 2, 3):
    for seed in range(45):
        if seed % 2:
            caps = tuple(1+(e+seed) % 2 for e in range(n))
            rank = tuple(min(1+seed % sum(caps), sum(caps[e] for e in range(n) if s >> e & 1))
                         for s in range(1 << n))
        else:
            features = tuple((1 << e) | (1 << ((e+seed) % n)) for e in range(n))
            rank = tuple(sum(1+(h+seed) % 2 for h in range(n)
                             if any(s >> e & 1 and features[e] >> h & 1 for e in range(n)))
                         for s in range(1 << n))
        weights = tuple(rng.randrange(5) for _ in range(n))
        costs = tuple(F(rng.randrange(-4, 5), rng.randrange(1, 4)) for _ in range(n))
        rows = tuple((rng.randrange(n+1), rng.choice(('<=', '=', '>=')), rng.randrange(5))
                     for _ in range(seed % 5))
        fixtures.append((rank, weights, costs, rows))

checks = dict(instances=0, exact_solves=0, original_vectors=0, marked_profiles=0,
              profiles=0, row_rejections=0, empty_faces=0, recovered=0,
              binary_checks=0, invalid_rejections=0)
for rank, weights, costs, rows in fixtures:
    n = len(weights)
    eligibility = (tuple(range(n)), tuple(e for e in range(n) if e % 2 == 0))
    for allowed in sorted(set(eligibility)):
        for mandatory in (False, True):
            actual = original(rank, weights, costs, rows, mandatory, allowed)
            checks['original_vectors'] += len(actual)
            for maximize in (False, True):
                solver = Prefix(rank, weights, costs, rows, mandatory, allowed, maximize)
                answer = solver.solve()
                expected = (max if maximize else min)((cost for _, cost in actual), default=None)
                assert (answer is None) == (expected is None)
                if answer is not None:
                    assert solver.verify(answer) and answer.cost == expected and (answer.counts, answer.cost) in actual
                for key in ('profiles', 'row_rejections', 'empty_faces', 'recovered'):
                    checks[key] += solver.last_trace[key]
                # Every original feasible vector has a legal marked profile
                # whose recovered signed optimum is at least as good.
                for x, cost in actual:
                    profile = marked_profile(solver, x)
                    recovered = solver.realize(profile)
                    assert recovered is not None
                    assert recovered.cost >= cost if maximize else recovered.cost <= cost
                    checks['marked_profiles'] += 1
                # Independent profile count/mass traversal on small alphabets.
                if len(solver.classes) <= 5 and not solver.impossible:
                    caps = tuple(min(solver.total, solver.mass_cap//w) for w, _, _ in solver.classes)
                    expected_profiles = {h for h in product(*(range(cap+1) for cap in caps))
                                         if sum(h) <= solver.total and
                                         sum(w*x for (w, _, _), x in zip(solver.classes, h)) <= solver.mass_cap}
                    native_profiles = tuple(solver.profiles())
                    assert len(native_profiles) == len(set(native_profiles)) and set(native_profiles) == expected_profiles
                checks['exact_solves'] += 1
            checks['instances'] += 1

# Original total and signed real zero-column costs survive binary-large
# eligibility masks and disposal; no count enumeration is used below.
huge = 10**100
rank = (0, huge, huge, huge)
for mandatory in (False, True):
    solver = Prefix(rank, (0, 1), (F(-1, 10**110), 1), ((2, '<=', 0),), mandatory)
    answer = solver.solve()
    assert answer.counts == (huge, 0) and answer.cost == -F(huge, 10**110)
    checks['binary_checks'] += 1
solver = Prefix(rank, (0, 1), (F(1), F(-1)), ((2, '<=', 0),), True, allowed=(1,))
assert solver.solve() is None  # Masking cannot lower a mandatory original total.
checks['binary_checks'] += 1
solver = Prefix((0, huge), (huge+1,), (F(1, 3),), ((1, '>=', huge),), True)
answer = solver.solve()
assert answer.counts == (huge,) and answer.cost == F(huge, 3)
assert solver.last_trace['profiles'] <= 2 and len(solver.copies) == 2
checks['binary_checks'] += 1
solver = Prefix((0, huge), (huge+1,), (F(1, 3),), ((1, '>=', huge),), False)
assert solver.solve().counts == (1,)
checks['binary_checks'] += 1
solver = Prefix((0, huge), (huge,), (F(-1, 10**110),), ((1, '<=', huge),), True)
assert solver.solve() is None and len(solver.copies) == 1
checks['binary_checks'] += 1

valid = Prefix((0, 2), (1,), (F(1),), ((1, '<=', 1),), mandatory=False)
bad = [lambda: Prefix((0, 1, 1), (1,), (0,)),
       lambda: Prefix((0, 1), (-1,), (0,)), lambda: Prefix((0, 1), (1,), (0.5,)),
       lambda: Prefix((0, 1), (True,), (0,)), lambda: Prefix((0, 1), (1,), (0,), ((2, '<=', 1),)),
       lambda: Prefix((0, 1), (1,), (0,), ((1, '<', 1),)),
       lambda: Prefix((0, 1), (1,), (0,), ((1, '<=', -1),)),
       lambda: Prefix((0, 1), (1,), (0,), mandatory=1),
       lambda: Prefix((0, 1), (1,), (0,), allowed=(0, 0)),
       lambda: valid.realize((-1,)), lambda: valid.realize((3,))]
for call in bad:
    try: call()
    except ValueError: checks['invalid_rejections'] += 1
    else: raise AssertionError('malformed original quota input accepted')
assert valid.verify(Solution((1,), F(1)))
assert not valid.verify(Solution((2,), F(2)))
assert not valid.verify(Solution((1,), F(0)))
print(json.dumps({'status': 'PASS', **checks}, sort_keys=True))
