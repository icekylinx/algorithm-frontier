#!/usr/bin/env python3
"""Independent original integer/fractional common-basis finite checks.
Attribution: Yilin Liu and GPT-6 Astra Pro. Apache-2.0.
"""
from fractions import Fraction as F
from itertools import product,combinations
from pathlib import Path
import importlib.util
import sys


spec = importlib.util.spec_from_file_location('_check_robust_native',Path(__file__).resolve().parents[1]/'reference/robust.py')
native = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = native
spec.loader.exec_module(native)
joint = native.joint


def solve(rows):
    n = len(rows)
    matrix = [list(map(F,a))+[F(b)] for a,b in rows]
    for col in range(n):
        pivot = next((r for r in range(col,n) if matrix[r][col]),None)
        if pivot is None: return None
        matrix[col],matrix[pivot] = matrix[pivot],matrix[col]
        value = matrix[col][col]
        matrix[col] = [x/value for x in matrix[col]]
        for r in range(n):
            if r == col: continue
            value = matrix[r][col]
            matrix[r] = [x-value*y for x,y in zip(matrix[r],matrix[col])]
    return tuple(row[-1] for row in matrix)


def fractional_scenario(scenario,basis):
    # Build RA16 directly from original data, with a separate Gaussian solver.
    keys = tuple((j,p) for j in range(len(scenario.ranks)) for p in basis)
    n = len(keys)+1
    rows = []
    for i in range(n): rows.append((tuple(F(-1 if h == i else 0) for h in range(n)),F(0)))
    for j,rank in enumerate(scenario.ranks):
        for s,bound in enumerate(rank): rows.append((tuple(F(h == j and bool(s >> p & 1)) for h,p in keys)+(F(0),),F(bound)))
    rows.append((tuple(scenario.costs[j][p] for j,p in keys)+(F(0),),scenario.budget-sum((scenario.setup[p] for p in basis),F(0))))
    for p in basis: rows.append((tuple(-scenario.values[j][p] if owner == p else F(0) for j,owner in keys)+(F(1),),F(0)))
    rows = tuple(sorted(set(rows)))
    best = None
    for active in combinations(rows,n):
        point = solve(active)
        if point is not None and all(sum((a*x for a,x in zip(row,point)),F(0)) <= b for row,b in rows):
            if best is None or point[-1] > best: best = point[-1]
    return best


def physical(rank,row):
    return all(sum(row[p] for p in range(len(row)) if s >> p & 1) <= bound for s,bound in enumerate(rank))


def integer_scenario(scenario,basis):
    options = []
    for rank in scenario.ranks:
        options.append(tuple(row for row in product(*(range(rank[1 << p]+1) if p in basis else (0,) for p in range(scenario.q))) if physical(rank,row)))
    best = None
    for counts in product(*options):
        cost = sum((scenario.setup[p] for p in basis),F(0))+sum((scenario.costs[j][p]*row[p] for j,row in enumerate(counts) for p in basis),F(0))
        if cost <= scenario.budget:
            value = min(sum((scenario.values[j][p]*counts[j][p] for j in range(len(counts))),F(0)) for p in basis)
            if best is None or value > best: best = value
    return best


def bases(instance):
    return tuple(tuple(p for p in range(instance.q) if s >> p & 1) for s,value in enumerate(instance.player)
                 if s.bit_count() == instance.rank and value == instance.rank)


def check(instance,answer,required=None):
    assert instance.verify(answer)
    for scenario,counts in zip(instance.scenarios,answer.scenarios):
        assert all(physical(rank,row) for rank,row in zip(scenario.ranks,counts))
        cost = sum((scenario.setup[p] for p in answer.basis),F(0))+sum((scenario.costs[j][p]*row[p] for j,row in enumerate(counts) for p in range(instance.q)),F(0))
        assert cost <= scenario.budget
        for p in answer.basis:
            assert all(type(row[p]) is int and row[p] >= 0 for row in counts)
            utility = sum((scenario.values[j][p]*counts[j][p] for j in range(len(counts))),F(0))
            if required is not None:
                largest = max((scenario.values[j][p] for j,rank in enumerate(scenario.ranks) if rank[1 << p]),default=F(0))
                assert utility >= max(0,required-largest)


def run():
    # Asymmetric values/costs and one attained common setup scalar; cheapest
    # bases change under restriction. A whole unit can exceed a residual
    # budget but must remain in the fractional comparator.
    specifications = (
        (((0,2,2,2),),((1,3),),((1,2),),2),
        (((0,2,1,2),),((4,1),),((3,1),),2),
    )
    instances = [native.Robust((0,1,1,1),specifications,(0,F(1,2))),
                 native.Robust((0,1,1,1),tuple((r,v,c,0) for r,v,c,_ in specifications),(0,1)),
                 native.Robust((0,1,1,1),((((0,1,1,1),),((1,3),),((0,0),),0),(((0,2,2,2),),((3,1),),((0,0),),0))),
                 native.Robust((0,1,1,2),((((0,2,2,3),),((1,3),),((1,1),),2),(((0,2,2,3),),((3,1),),((1,1),),2))),
                 native.Robust((0,1,1,1),specifications,(3,4)),
                 native.Robust((0,1,1,1),(((),(),(),0),),None)]
    fixed = gates = optimum_calls = 0
    for i,instance in enumerate(instances):
        values = []
        for basis in bases(instance):
            if any(sum((instance.setup[p] for p in basis),F(0)) > scenario.budget for scenario in instance.scenarios): continue
            truth = min(fractional_scenario(scenario,basis) for scenario in instance.scenarios)
            value,counts = instance.fractional(basis)
            assert value == truth
            rounded = instance.recover(basis,counts)
            check(instance,rounded,value)
            values.append((basis,value))
            fixed += 1
        fopt = max((value for _,value in values),default=None)
        for target in (F(1,2),F(1),F(2),F(4)):
            for forced in ((),(0,)):
                if len(forced) > instance.q-instance.rank: continue
                result = instance.gap(target,target/2,forced)
                promised = max((value for basis,value in values if not set(basis)&set(forced)),default=None)
                if result is None: assert promised is None or promised < target
                else:
                    value,counts = instance.fractional(result.selected)
                    assert value >= target/2
                    check(instance,instance.recover(result.selected,counts),value)
                gates += 1
        if i in (0,2,3,4,5):
            answer = instance.optimize(F(1,2),global_base=4 if i == 2 else None)
            if fopt is None: assert answer is None
            else: check(instance,answer,fopt/2)
            optimum_calls += 1
    # Role disagreement is legal because each scenario allocates independently
    # AFTER selection. These are exactly the common-role counterexample data.
    one = native.Robust((0,1),((((0,1),),((2,),),((0,),),0),(((0,3),),((F(3,4),),),((0,),),0)))
    value,counts = one.fractional((0,))
    assert value == 2
    check(one,one.recover((0,),counts),value)
    # Zero/one common-selection obstruction: no common integral positive basis,
    # despite feasible shared fractional dummy and identical all-heavy roles.
    q = 4
    player = tuple(min(s.bit_count(),2) for s in range(1 << q))
    pairs = tuple(combinations(range(q),2))
    scenarios = []
    for pair in pairs:
        pairmask = sum(1 << p for p in pair)
        rank = tuple((s & ~pairmask).bit_count()+min((s & pairmask).bit_count(),1) for s in range(1 << q))
        scenarios.append(((rank,),((1,)*q,),((0,)*q,),0))
    obstruction = native.Robust(player,scenarios)
    for basis in bases(obstruction):
        assert min(integer_scenario(scenario,basis) for scenario in obstruction.scenarios) == 0
        value,counts = obstruction.fractional(basis)
        assert value == F(1,2)
        check(obstruction,obstruction.recover(basis,counts),value)
    # Binary supply and rank-zero conventions; no numeric enumeration here.
    huge = 1 << 100
    binary = native.Robust((0,1),((((0,huge),),((F(3,2),),),((0,),),0),))
    value,counts = binary.fractional((0,))
    assert value == F(3,2)*huge
    check(binary,binary.recover((0,),counts),value)
    empty = native.Robust((0,0),((((0,1),),((1,),),((0,),),0),))
    assert empty.minimum(empty.optimize(F(1,2))) is None
    four = native.Robust(tuple(min(s.bit_count(),2) for s in range(16)),(((),(),(),0),))
    assert four.gap(2,1,global_base=4) is None
    gates += 1
    # Original verifier must not call any LP, recursion or rounding producer.
    instance = instances[0]
    value,counts = instance.fractional((0,))
    output = instance.recover((0,),counts)
    saved = native.Robust.region
    native.Robust.region = lambda *args: (_ for _ in ()).throw(AssertionError('producer used'))
    try: assert instance.verify(output)
    finally: native.Robust.region = saved
    class Duck:
        basis,scenarios = output.basis,output.scenarios
    assert not instance.verify(Duck())
    assert not instance.verify(native.Allocation(output.basis,output.scenarios[:-1]))
    invalid = 0
    for thunk in (lambda:native.Robust((0,1),()),lambda:instance.optimize(1),
                  lambda:instance.optimize(F(1,2),global_base=3),
                  lambda:native.Robust((0,1),((((0,1),),((1,),),((-1,),),0),))):
        try: thunk()
        except ValueError: invalid += 1
        else: raise AssertionError('malformed input accepted')
    print(f'PASS robust unrelated: {fixed} independent original fixed-basis LPs/recoveries, '
          f'{gates} forced/common-basis gaps, {optimum_calls} rational/global optimizations, '
          f'one role-disagreement and 6 zero/one obstruction bases, 101-bit counts, '
          f'producer-disabled verifier, 2 forged and {invalid} malformed cases')


if __name__ == '__main__': run()
