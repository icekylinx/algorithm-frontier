"""Independent original-input allocation, profile and rounding checks.

Attribution: icekylinx and GPT-6 Astra Pro. Apache-2.0.
The finite original comparator uses no backend bin/LP/rounding helper.
"""
from dataclasses import replace
from fractions import Fraction as F
from itertools import combinations, product, islice
from pathlib import Path
import random
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1] / 'reference'))
import scheme as impl


def legal(rank,row):
    return all(x >= 0 for x in row) and all(sum(row[p] for p in range(len(row)) if s >> p & 1) <= bound for s,bound in enumerate(rank))


def original_answers(player,ranks,values,costs,setup,budget):
    q,m = len(values),len(ranks)
    for basis in combinations(range(q),player[-1]):
        if player[sum(1 << p for p in basis)] != len(basis) or sum(setup[p] for p in basis) > budget: continue
        vectors = [tuple(row for row in product(*(range(rank[1 << p]+1) if p in basis and values[p][j] is not None else (0,) for p in range(q))) if legal(rank,row)) for j,rank in enumerate(ranks)]
        for counts in product(*vectors):
            cost = sum(setup[p] for p in basis)+sum(costs[p][j]*counts[j][p] for p in basis for j in range(m))
            if cost <= budget:
                utility = min((sum((values[p][j] or 0)*counts[j][p] for j in range(m)) for p in basis),default=None)
                yield basis,counts,utility


def independent_verify(model,answer):
    if answer is None: return False
    basis,counts = answer.basis,answer.counts
    q,m = model.q,model.m
    return (len(set(basis)) == len(basis) == model.rank
            and model.player[sum(1 << p for p in basis)] == model.rank
            and len(counts) == m and all(len(row) == q and all(type(x) is int and x >= 0 and (not x or (p in basis and model.values[p][j] is not None)) for p,x in enumerate(row)) and legal(model.ranks[j],row) for j,row in enumerate(counts))
            and sum(model.setup[p] for p in basis)+sum(model.costs[p][j]*counts[j][p] for j in range(m) for p in range(q)) <= model.budget)


def main():
    rng = random.Random(112703)
    constructions = attempts = feasible_targets = sound_failures = optimizations = direct = profiles_checked = 0
    fixtures = [((0,1),((0,2),),((F(2),),),((F(1,2),),),(F(1,3),),F(4,3)),
                ((0,1,1,2),((0,1,1,1),),((2,),(3,)),((0,),(0,)),(0,0),0),
                ((0,1,0,1),((0,2,2,2),),((1,),(9,)),((0,),(0,)),(0,0),0),
                ((0,1,1,1),((0,2,2,2),),((1,),(3,)),((1,),(4,)),(0,1),2),
                ((0,1,1,2),((0,1,1,2),),((F(1,2),),(F(2,3),)),((1,),(1,)),(2,2),3)]
    tables = tuple((0,a,b,n) for n in range(3) for a in range(n+1) for b in range(n+1) if a+b >= n)
    for _ in range(16):
        player = rng.choice(((0,1,1,1),(0,1,1,2),(0,1,0,1)))
        ranks = (rng.choice(tables),rng.choice(tables))
        values = tuple(tuple(rng.choice((None,F(0),F(1,2),F(1),F(3))) for j in ranks) for p in range(2))
        costs = tuple(tuple(F(rng.randrange(3),2) for j in ranks) for p in range(2))
        setup = (F(rng.randrange(3),2),F(rng.randrange(3),2))
        fixtures.append((player,ranks,values,costs,setup,F(rng.randrange(7),2)))
    for data in fixtures:
        for epsilon in (F(1),F(1,2)):
            model = impl.Scheme(*data,epsilon)
            answers = tuple(original_answers(*data))
            optimum = max((value for _,_,value in answers),default=None)
            zero = model.zero()
            assert (zero is None) == (not answers)
            if zero is not None: assert independent_verify(model,zero)
            for target in (F(0),F(1,2),F(1),F(2)):
                answer = model.target(target)
                attempts += 1
                if answer is None:
                    assert not any(value >= target for _,_,value in answers)
                    sound_failures += 1
                else:
                    assert independent_verify(model,answer)
                    assert model.minimum(answer) >= (1-epsilon)*target
                    feasible_targets += 1
            answer = model.optimize()
            if answers:
                assert independent_verify(model,answer) and model.minimum(answer) >= (1-epsilon)*optimum
            else: assert answer is None
            optimizations += 1
            # Inspect each feasible one-owner profile; preserve all lower prefixes
            # and actual original cost at the same integral recovery point.
            for basis in combinations(range(model.q),model.rank):
                if model.player[sum(1 << p for p in basis)] != model.rank or model.fee(basis) > model.budget: continue
                groups = model.grouping(basis,F(1))
                for plan in model.plans(basis,F(1)):
                    profiles_checked += 1
                    witness = model.fractional(plan)
                    if witness is None: continue
                    answer = model.recover(plan,witness)
                    assert independent_verify(model,answer)
                    assert model.assignment_cost(answer.counts) <= model.assignment_cost(witness)
                    for group in groups:
                        order = tuple(j for b in reversed(group.bins) for j in b.types)+tuple(sorted(group.small,key=lambda j:(-model.values[group.owner][j],j)))
                        for h in range(1,len(order)+1):
                            total = sum((witness[j][group.owner] for j in order[:h]),F(0))
                            assert sum(answer.counts[j][group.owner] for j in order[:h]) >= total.numerator//total.denominator
                    direct += 1
            constructions += 1
    # Independent uncompressed vertex oracle checks exact fixed-coordinate
    # substitution, lower-dimensional faces, linear optima and contradictions.
    lp_checks = 0
    for fixed in range(3):
        for direction in (-1,0,1):
            rows = []
            for i in range(3):
                a = tuple(int(i == j) for j in range(3))
                rows.extend(((a,2),(tuple(-x for x in a),0)))
            a = tuple(int(j == fixed) for j in range(3))
            rows.extend(((a,1),(tuple(-x for x in a),-1),((1,1,1),4)))
            objective = (F(direction),F(2),F(-1))
            candidates = impl.intrinsic.linear.vertices(rows,3)
            got = impl.active_vertex(rows,3,objective)
            expected_value = min(sum(x*y for x,y in zip(objective,p)) for p in candidates)
            assert sum(x*y for x,y in zip(objective,got)) == expected_value
            assert impl.active_vertex(rows+[(a,0)],3) is None
            lp_checks += 2
    # Bin boundaries: small equality, internal equality in preceding bin,
    # target equality in final bin, and arbitrarily high original value capped.
    delta = F(1,6)
    values = ((delta,delta+delta*delta,delta+2*delta*delta,F(1),F(1000)),)
    boundary = impl.Scheme((0,1),((0,2),)*5,values,((0,)*5,),(0,),0,F(1,2))
    groups = boundary.grouping((0,),1)[0]
    assert groups.small == (0,) and groups.bins[0].index == 0 and groups.bins[0].types == (1,)
    assert groups.bins[1].index == 1 and groups.bins[1].types == (2,)
    assert groups.bins[-1].index == boundary.bin_count-1 and groups.bins[-1].types == (3,4)
    # Independent occupied-profile enumeration, including the lower-sum cap.
    lower = (F(1,6),F(1,2),F(5,6))
    expected = {v for v in product(range(7),repeat=3) if sum(v) <= 6 and sum(x*y for x,y in zip(lower,v)) <= 2}
    actual = tuple(impl.profiles.profile_counts(tuple(x/2 for x in lower),6))
    assert len(actual) == len(set(actual)) and set(actual) == expected
    # Large original values have no generic largest-unit rounding charge:
    # one big unit plus a fractional small unit is rounded at exact cost.
    special = impl.Scheme((0,1),((0,1),(0,2)),((100,F(1,10)),),((1,0),),(F(1,3),),F(4,3),F(1,2))
    answer = special.target(1)
    assert independent_verify(special,answer) and special.minimum(answer) >= 1
    # One fractional point needs both big-bin equality and genuine small
    # service; cost recovery must choose the cheaper original big type.
    mix = impl.Scheme((0,1),((0,1),(0,1),(0,3)),((F(4,5),F(4,5),F(1,10)),),((5,1,0),),(0,),3,F(1,2))
    plan = impl.Plan((0,),F(1),((1,),))
    witness = ((F(1,2),F(1,2)),(F(1,2),F(1,2)),(F(2),F(1)))
    recovered = mix.recover(plan,witness)
    assert independent_verify(mix,recovered) and mix.assignment_cost(recovered.counts) <= 3
    assert recovered.counts[0][0] == 0 and recovered.counts[1][0] >= 1 and recovered.counts[2][0] >= 2
    # Two original players share each original unit. A single joint rounding
    # repairs the fractional diagonal and exact budget together.
    joint = impl.Scheme((0,1,1,2),((0,1,1,1),)*2,((F(1),F(1)),)*2,((0,1),(1,0)),(0,0),1,F(1,2))
    joint_plan = impl.Plan((0,1),F(1),((1,),(1,)))
    joint_witness = ((F(1,2),F(1,2),F(0)),)*2
    recovered = joint.recover(joint_plan,joint_witness)
    assert independent_verify(joint,recovered) and joint.assignment_cost(recovered.counts) == 0
    assert recovered.counts == ((1,0),(0,1))
    # Capping is deliberately not fractional-target equivalent: x=1/100
    # meets original value 1 but capped value only 1/100.
    assert F(1,100)*100 == 1 and F(1,100)*min(100,1) < 1
    # Very large supplies and accuracy indices: no capacity/accuracy table.
    huge = 1 << 100
    large = impl.Scheme((0,1),((0,huge),),((F(2,3),),),((0,),),(0,),0,F(1,2))
    answer = large.optimize()
    assert independent_verify(large,answer) and large.minimum(answer) >= huge*F(1,3)
    tiny = impl.Scheme((0,1),((0,1),),((1,),),((0,),),(0,),0,F(1,1 << 120))
    group = tiny.grouping((0,),1)[0]
    assert len(group.bins) == 1 and group.bins[0].index == tiny.bin_count-1
    assert tuple(islice(tiny.plans((0,),1),2))[-1].counts == ((1,),)
    # The canonical occupied iterator and global iterator avoid recursion depth.
    deep = tuple(islice(impl.profiles.profile_counts((F(1,2),)*1100,0),1))
    assert deep == ((0,)*1100,)
    empty = impl.Scheme((0,),(),(),(),(),0,F(1,2))
    assert empty.verify(empty.optimize()) and empty.minimum(empty.optimize()) is None
    no_types = impl.Scheme((0,1),(),((),),((),),(0,),0,F(1,2))
    assert no_types.minimum(no_types.optimize()) == 0 and no_types.target(1) is None
    # Verifier is producer independent; corrupt original budgets/IDs/masks fail.
    model = impl.Scheme((0,1),((0,2),),((1,),),((1,),),(1,),2,F(1,2))
    good = impl.Allocation((0,),((1,),))
    assert model.verify(good)
    saved = impl.Scheme.target,impl.Scheme.fractional,impl.Scheme.recover,impl.active_vertex
    def unavailable(*a,**kw): raise AssertionError('verifier called producer')
    try:
        impl.Scheme.target=impl.Scheme.fractional=impl.Scheme.recover=impl.active_vertex=unavailable
        assert model.verify(good) and model.minimum(good)==1
    finally:
        impl.Scheme.target,impl.Scheme.fractional,impl.Scheme.recover,impl.active_vertex=saved
    forged = (replace(good,basis=(0,0)),replace(good,counts=((2,),)),replace(good,counts=((1.0,),)),replace(good,counts=((-1,),)))
    assert not any(model.verify(a) for a in forged)
    rejected = 0
    for thunk in (lambda:impl.Scheme((0,2),((0,1),),((1,),),((0,),),(0,),0,F(1,2)),
                  lambda:impl.Scheme((0,1),((0,1),),((1.0,),),((0,),),(0,),0,F(1,2)),
                  lambda:impl.Scheme((0,1),((0,1),),((1,),),((-1,),),(0,),0,F(1,2)),
                  lambda:impl.Scheme((0,1),((0,1),),((1,),),((0,),),(0,),0,0),
                  lambda:model.target(-1),lambda:model.grouping((0,0),1),
                  lambda:model.fractional(impl.Plan((0,),F(1),((-1,),))),
                  lambda:model.recover(impl.Plan((0,),F(1),((1,),)),((F(1,2),F(3,2)),))):
        try: thunk()
        except ValueError: rejected += 1
        else: raise AssertionError('invalid input accepted')
    print(f'PASS: {constructions} original instances/accuracies; {attempts} target calls ({feasible_targets} outputs, {sound_failures} sound failures); {optimizations} original-grid optimizations; {profiles_checked} inspected profiles; {direct} direct all-prefix/cost recoveries; {len(expected)} independent occupied profiles; {lp_checks} uncompressed LP comparisons; 2 mixed-small/shared-resource joint recoveries; endpoint/capping/shared-budget cases; 101-bit supply; 121-bit accuracy; deep iterator; rank-zero/empty types; producer-disabled verifier; {len(forged)} forged outputs; {rejected} malformed inputs.')


if __name__ == '__main__': main()
