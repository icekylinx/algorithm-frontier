#!/usr/bin/env python3
"""Independent original-box pricing and explicit residual-LP checks.
Attribution: icekylinx and GPT-6 Astra Pro. Apache-2.0.
"""
from dataclasses import replace
from fractions import Fraction as F
from itertools import combinations,product
from pathlib import Path
import importlib.util
import random
import sys


spec = importlib.util.spec_from_file_location('_check_fractional',Path(__file__).resolve().parents[1]/'reference/fractional.py')
native = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = native
spec.loader.exec_module(native)


def raw_cost(vector,linear,hinges):
    return sum((linear[j]*n+sum((weight*max(0,n-breakpoint) for breakpoint,weight in hinges[j]),F(0))
                for j,n in enumerate(vector)),F(0))


def solve(rows):
    n = len(rows)
    matrix = [list(map(F,a))+[F(b)] for a,b in rows]
    for col in range(n):
        pivot = next((i for i in range(col,n) if matrix[i][col]),None)
        if pivot is None: return None
        matrix[col],matrix[pivot] = matrix[pivot],matrix[col]
        factor = matrix[col][col]
        matrix[col] = [v/factor for v in matrix[col]]
        for i in range(n):
            if i == col: continue
            factor = matrix[i][col]
            matrix[i] = [v-factor*w for v,w in zip(matrix[i],matrix[col])]
    return tuple(row[-1] for row in matrix)


def columns(instance,target):
    return tuple((p,n) for p in range(instance.q) for n in product(*(range(cap+1) for cap in instance.quotas[p]))
                 if sum((v*x for v,x in zip(instance.values[p],n)),F(0)) >= target)


def original_feasible(instance,target):
    """Enumerate original box configurations; derive every original LP row.

    This oracle does not use native prices, columns, vertices, Farkas or LP.
    Eliminate the last mass using sum(mu)=original rank, then enumerate bases.
    """
    configs = columns(instance,target)
    if not configs: return instance.rank == 0
    rows = []
    for s,bound in enumerate(instance.player.values):
        rows.append((tuple(F(bool(s >> p & 1)) for p,_ in configs),F(bound)))
    for j,resource in enumerate(instance.resources):
        for s,bound in enumerate(resource.values):
            rows.append((tuple(F(n[j] if s >> p & 1 else 0) for p,n in configs),F(bound)))
    for j,s in instance.cuts:
        rank = instance.resources[j].values
        rows.append((tuple(F(max(0,n[j]-(rank[s | 1 << p]-rank[s]))) for p,n in configs),F(rank[s])))
    for i in range(len(configs)):
        rows.append((tuple(F(-1 if i == h else 0) for h in range(len(configs))),F(0)))
    reduced = tuple(sorted(set((tuple(a-a_last for a in row[:-1]),b-row[-1]*instance.rank)
                              for row,b in rows for a_last in (row[-1],))))
    dimension = len(configs)-1
    if not dimension: return all(b >= 0 for _,b in reduced)
    for active in combinations(reduced,dimension):
        point = solve(active)
        if point is not None and all(sum((a*x for a,x in zip(row,point)),F(0)) <= bound for row,bound in reduced):
            return True
    return False


def original_optimum(instance):
    values = sorted({F(0)}|{sum((v*x for v,x in zip(instance.values[p],n)),F(0))
                           for p in range(instance.q) for n in product(*(range(cap+1) for cap in instance.quotas[p]))})
    low,high = 0,len(values)
    while high-low > 1:
        middle = (low+high)//2
        if original_feasible(instance,values[middle]): low = middle
        else: high = middle
    return values[low]


def independent_verify(instance,point):
    x = [F(0)]*instance.q
    y = [[F(0)]*instance.q for _ in instance.resources]
    for mass in point.masses:
        p,n,w = mass.configuration.owner,mass.configuration.counts,mass.weight
        assert type(p) is int and 0 <= p < instance.q and w > 0
        assert len(n) == instance.m and all(type(a) is int and 0 <= a <= cap for a,cap in zip(n,instance.quotas[p]))
        assert sum((a*v for a,v in zip(n,instance.values[p])),F(0)) >= point.target
        x[p] += w
        for j,a in enumerate(n): y[j][p] += w*a
    assert sum(x,F(0)) == instance.rank
    assert all(sum(x[p] for p in range(instance.q) if s >> p & 1) <= rank for s,rank in enumerate(instance.player.values))
    for resource,row in zip(instance.resources,y):
        assert all(sum(row[p] for p in range(instance.q) if s >> p & 1) <= rank for s,rank in enumerate(resource.values))
    for j,s in instance.cuts:
        rank = instance.resources[j].values
        left = sum((mass.weight*max(0,mass.configuration.counts[j]-(rank[s | 1 << mass.configuration.owner]-rank[s]))
                    for mass in point.masses),F(0))
        assert left <= rank[s]
    assert instance.verify(point)


def main():
    rng = random.Random(29042)
    pricing = strict = 0
    for i in range(100):
        m = 1+i % 3
        caps = tuple(rng.randrange(5) for _ in range(m))
        profits = tuple(F(rng.randrange(5),2) for _ in caps)
        linear = tuple(F(rng.randrange(-4,4),2) for _ in caps)
        hinges = tuple(tuple((rng.randrange(cap+2),F(rng.randrange(4),3)) for _ in range(2)) for cap in caps)
        budget = F(rng.randrange(-6,13),3)
        domain = tuple(product(*(range(cap+1) for cap in caps)))
        feasible = tuple(n for n in domain if raw_cost(n,linear,hinges) <= budget)
        optimum = max((sum((v*x for v,x in zip(profits,n)),F(0)) for n in feasible),default=None)
        for epsilon in (F(1,2),F(1,3)):
            answer = native.price(caps,profits,linear,hinges,budget,epsilon)
            if optimum is None: assert answer is None
            else:
                assert answer is not None and answer.counts in domain
                assert answer.cost == raw_cost(answer.counts,linear,hinges) <= budget
                assert answer.value == sum((v*x for v,x in zip(profits,answer.counts)),F(0)) >= (1-epsilon)*optimum
            pricing += 1
        for threshold in (F(-1,2),F(0),F(1,3),F(3,2)):
            target = F(1+i % 6)
            answer = native.strict_price(caps,profits,linear,hinges,threshold,target,F(1,3))
            if answer is None:
                assert not any(raw_cost(n,linear,hinges) < threshold and sum((v*x for v,x in zip(profits,n)),F(0)) >= target for n in domain)
            else:
                assert answer.counts in domain and raw_cost(answer.counts,linear,hinges) < threshold
                assert sum((v*x for v,x in zip(profits,answer.counts)),F(0)) >= F(2,3)*target
            strict += 1
    assert native.strict_price((1,),(1,),(1,),((),),1,1,F(1,2)) is None
    assert native.strict_price((1,),(1,),(-1,),((),),-1,1,F(1,2)) is None
    assert native.strict_price((1,),(1,),(-1,),((),),F(-1,2),1,F(1,2)).counts == (1,)
    # Natural reserve basis and all residual cuts: count enumeration is confined
    # to this small independent oracle, never used by the native implementation.
    basis_checks = residual_checks = scaled = 0
    tables = tuple((0,a,b,c) for a in range(3) for b in range(3) for c in range(max(a,b),a+b+1))
    for table in tables:
        instance = native.Residual((0,1,1,1),(table,),(1,))
        resource = instance.resources[0]
        vectors = tuple(product(*(range(cap+1) for cap in resource.caps)))
        for reserved in vectors:
            basis = instance.reserved_basis(0,reserved)
            assert all(a <= b for a,b in zip(basis,reserved)) and resource.independent(basis)
            assert sum(basis) == resource.rank(reserved)
            assert resource.availability(basis) == resource.availability(reserved)
            basis_checks += 1
        # Arbitrary explicit mass lists need not be feasible. Convexity says
        # every reserve violation is dominated by some subset violation.
        masses = tuple(native.Mass(native.Configuration(p,(resource.caps[p],)),F(2,3)) for p in range(2))
        point = native.Point(F(0),masses)
        subset_max = max(sum((mass.weight*max(0,mass.configuration.counts[0]-(table[s | 1 << mass.configuration.owner]-table[s]))
                             for mass in masses),F(0))-table[s] for s in range(4))
        for reserved in vectors:
            if not resource.independent(reserved): continue
            availability = tuple(min(table[s]-sum(reserved[p] for p in range(2) if s >> p & 1) for s in range(4) if s >> owner & 1) for owner in range(2))
            violation = sum((mass.weight*max(0,mass.configuration.counts[0]-availability[mass.configuration.owner]) for mass in masses),F(0))-sum(reserved)
            assert violation <= subset_max
            residual_checks += 1
    for matroid in ((0,1,1,1),(0,1,1,2),(0,1,0,1)):
        for multiplicity in (1,2,3):
            resource = native.counts.RankTable(2,tuple(multiplicity*x for x in matroid))
            feasible = tuple(n for n in product(*(range(cap+1) for cap in resource.caps)) if resource.independent(n))
            for reserved in product(*(range(cap+1) for cap in resource.caps)):
                a = resource.availability(reserved)
                for first,last in zip(feasible,reversed(feasible)):
                    y = tuple(F(x+z,2) for x,z in zip(first,last))
                    assert sum((F(multiplicity-a[p],multiplicity)*y[p] for p in range(2)),F(0)) <= resource.rank(reserved)
                    scaled += 1
    # Signed aggregate support is independently maximized over all integral
    # original bases and resource vectors, including negative completion weights.
    sample = native.Residual((0,1,1,1),((0,2,1,2),),(1,))
    aggregate = tuple(tuple(int(p == chosen) for p in range(2))+n for chosen in (0,1)
                      for n in product(range(3),range(2)) if sample.resources[0].independent(n))
    greedy = 0
    for alpha in product((-2,0,3),repeat=4):
        vertex = sample.aggregate_vertex(alpha)
        assert vertex in aggregate
        assert sum(a*b for a,b in zip(alpha,vertex)) == max(sum(a*b for a,b in zip(alpha,v)) for v in aggregate)
        greedy += 1
    # Complete original fractional LP comparators for full, restricted and
    # arbitrary cut lists; no native column or oracle enters the comparator.
    instances = []
    for i,table in enumerate(tables[::3]):
        instances.append(native.Residual((0,1,1,1),(table,),(F(1+i % 2),),support=i % 3))
    instances += [native.Residual((0,1,1,2),((0,1,1,1),),(1,)),
                  native.Residual((0,1,1,1),((0,2,2,2),),((F(1,2),),(F(3,2),)),quotas=((1,),(2,)),cut_sets=()),
                  native.Residual((0,1),((0,2),(0,1)),(1,F(3,2))),
                  native.Residual((0,1,1,2),((0,1,1,1),(0,1,1,1)),(1,2),quotas=((1,1),(1,0)))]
    targets = optimizations = 0
    for instance in instances:
        optimum = original_optimum(instance)
        for target in (F(1,2),F(1),F(2),F(4)):
            point = instance.weak_target(target,F(1,3))
            if point is None: assert not original_feasible(instance,target)
            else:
                independent_verify(instance,point)
                assert point.target == F(2,3)*target
            targets += 1
        point = instance.optimize(F(1,3))
        independent_verify(instance,point)
        assert point.target >= F(2,3)*optimum
        optimizations += 1
    # Aggregate gap is rejected by one subset; full residual gap is genuinely
    # fractional even when every subset cut is verified on original tables.
    q,r,d = 6,2,3
    player = tuple(min(s.bit_count(),r) for s in range(1 << q))
    rank = tuple(s.bit_count()+d if s else 0 for s in range(1 << q))
    aggregate_only = native.Residual(player,(rank,),(1,),cut_sets=())
    full = native.Residual(player,(rank,),(1,))
    bad = native.Point(F(d+1),tuple(native.Mass(native.Configuration(p,(d+1,)),F(1,d)) for p in range(q)))
    independent_verify(aggregate_only,bad)
    assert not full.verify(bad) and full.separate_subsets(bad) is not None
    r = 3
    rank = tuple(min(s.bit_count(),r-1)+min(s.bit_count(),r+1) for s in range(1 << q))
    full_gap = native.Residual(tuple(min(s.bit_count(),r) for s in range(1 << q)),(rank,),(1,))
    gap = native.Point(F(2),tuple(native.Mass(native.Configuration(p,(2,)),F(1,2)) for p in range(q)))
    independent_verify(full_gap,gap)
    assert all(rank[sum(1 << p for p in basis)] < 2*r for basis in combinations(range(q),r))
    # Actual generation must extract genuinely fractional masses, rather than
    # returning an integral basis whenever the small toy examples allow one.
    # This support-zero relaxation retains all original aggregate rank rows.
    q,r = 4,2
    rank = tuple(min(s.bit_count(),r-1)+min(s.bit_count(),r+1) for s in range(1 << q))
    mixed = native.Residual(tuple(min(s.bit_count(),r) for s in range(1 << q)),(rank,),(1,),support=0)
    point = mixed.weak_target(2,F(1,3))
    assert point is not None and any(mass.weight.denominator > 1 for mass in point.masses)
    independent_verify(mixed,point)
    assert mixed.last_trace['columns'] >= 3 and mixed.last_trace['vertices'] > 1
    # Binary supply, strict prices and full accuracy encoding do not construct
    # unit lists or accuracy-length tables for a near-half encoded epsilon.
    huge = 1 << 100
    answer = native.price((huge,),(F(3,2),),(1,),((),),huge//2,F(1,3))
    assert answer.cost <= huge//2 and answer.value >= F(2,3)*F(3,2)*(huge//2)
    encoded = F((1 << 120)-1,1 << 121)
    answer = native.price((4,),(1,),(-1,),(((2,3),),),0,encoded)
    assert answer is not None and answer.cost <= 0
    binary = native.Residual((0,1),((0,huge),),(1,))
    point = binary.weak_target(huge,F(1,3))
    independent_verify(binary,point)
    # Empty resources and rank-zero conventions are explicit.
    empty = native.Residual((0,1),(),())
    assert empty.weak_target(1,F(1,3)) is None and empty.verify(empty.optimize(F(1,3)))
    rank_zero = native.Residual((0,0),((0,1),),(1,))
    assert rank_zero.verify(rank_zero.optimize(F(1,3)))
    # Standalone original verifier remains usable with every producer disabled.
    saved = native.Residual.weak_target,native.Residual.column,native.Residual.aggregate_vertex,native.price
    def unavailable(*args,**kw): raise AssertionError('producer used by verifier')
    try:
        native.Residual.weak_target=native.Residual.column=native.Residual.aggregate_vertex=native.price=unavailable
        assert full_gap.verify(gap)
    finally:
        native.Residual.weak_target,native.Residual.column,native.Residual.aggregate_vertex,native.price=saved
    class Duck:
        target,masses = gap.target,gap.masses
    forged = (Duck(),replace(gap,target=3),replace(gap,masses=(replace(gap.masses[0],weight=F(-1)),)),
              replace(gap,masses=(native.Mass(native.Configuration(True,(2,)),F(1)),)))
    assert not any(full_gap.verify(point) for point in forged)
    invalid = 0
    for thunk in (lambda:native.Residual((0,2),(),()),
                  lambda:native.Residual((0,1),((0,F(1,2)),),(1,)),
                  lambda:native.Residual((0,1),((0,1),),(1.0,)),
                  lambda:native.Residual((0,1),((0,1),),(1,),quotas=((2,),)),
                  lambda:native.Residual((0,1),((0,1),),(1,),support=-1),
                  lambda:sample.weak_target(-1,F(1,3)),lambda:sample.optimize(0),
                  lambda:native.price((1,),(1,),(0,),(((0,-1),),),0,F(1,3))):
        try: thunk()
        except ValueError: invalid += 1
        else: raise AssertionError('malformed input accepted')
    print(f'PASS fractional: {pricing} signed convex prices, {strict} strict weak prices, '
          f'{basis_checks} dependent reserve bases, {residual_checks} reserve/subset comparisons, '
          f'{scaled} scaled fractional losses, {greedy} signed aggregate maxima, '
          f'{len(instances)} original LP instances/{targets} weak targets/{optimizations} optimizations, '
          f'two configuration gaps and actual fractional-mass extraction, 101-bit supply/121-bit accuracy, producer-disabled verifier, '
          f'{len(forged)} forged and {invalid} malformed cases')


if __name__ == '__main__': main()
