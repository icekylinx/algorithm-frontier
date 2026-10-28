#!/usr/bin/env python3
"""Original-input finite oracle, independent of masks, dummy and producers.
Attribution: icekylinx and GPT-6 Astra Pro. Apache-2.0.
"""
from fractions import Fraction as F
from itertools import product,combinations
from pathlib import Path
import importlib.util
import random
import sys


def load():
    spec = importlib.util.spec_from_file_location('_check_joint_native',Path(__file__).resolve().parents[1]/'reference/joint.py')
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


native = load()


def physical(rank,row):
    return all(sum(row[p] for p in range(len(row)) if s >> p & 1) <= bound for s,bound in enumerate(rank))


def integer_options(rank,q):
    return tuple(row for row in product(*(range(rank[1 << p]+1) for p in range(q))) if physical(rank,row))


def original(instance):
    best = None
    for s,rank in enumerate(instance.player):
        if s.bit_count() != instance.rank or rank != instance.rank: continue
        basis = tuple(p for p in range(instance.q) if s >> p & 1)
        for counts in product(*(integer_options(rank,instance.q) for rank in instance.ranks)):
            if any(row[p] and p not in basis for row in counts for p in range(instance.q)): continue
            cost = sum((instance.setup[p] for p in basis),F(0))+sum((instance.costs[j][p]*row[p] for j,row in enumerate(counts) for p in range(instance.q)),F(0))
            if cost > instance.budget: continue
            value = min((sum((instance.values[j][p]*counts[j][p] for j in range(len(counts))),F(0)) for p in basis),default=F(0))
            if best is None or value > best: best = value
    return best


def check_output(instance,answer):
    assert native.Joint.verify(instance,answer)
    selected = set(answer.basis)
    assert len(selected) == instance.rank and instance.player[sum(1 << p for p in selected)] == instance.rank
    assert all(physical(rank,row) and all(type(x) is int and x >= 0 and (p in selected or not x) for p,x in enumerate(row))
               for rank,row in zip(instance.ranks,answer.counts))
    actual = sum((instance.setup[p] for p in selected),F(0))+sum((instance.costs[j][p]*row[p] for j,row in enumerate(answer.counts) for p in range(instance.q)),F(0))
    assert actual <= instance.budget


def run():
    rng = random.Random(4817)
    ranks = tuple((0,a,b,c) for a in range(3) for b in range(3) for c in range(max(a,b),a+b+1))
    instances = []
    for i in range(32):
        player = (0,1,1,1) if i % 2 else (0,1,1,2)
        instances.append(native.Joint(player,(rng.choice(ranks),),
                                      (tuple(rng.choice((0,1,3,F(3,2))) for _ in range(2)),),
                                      (tuple(F(rng.randrange(3),2) for _ in range(2)),),F(rng.randrange(7),2),
                                      tuple(F(rng.randrange(3),2) for _ in range(2))))
    # A shared type has opposite roles at different owners. Independent role
    # capacity copies would incorrectly provide two units when rank is one.
    instances += [native.Joint((0,1,1,2),((0,1,1,1),),((1,3),),((0,0),),0),
                  native.Joint((0,1,1,1),((0,1,1,1),),((2,4),),((0,0),),1,(10,1)),
                  native.Joint((0,0,1,1),((0,2,2,2),),((9,3),),((0,1),),2,(100,0)),
                  native.Joint((0,1,1,1),(),(),(),0),
                  native.Joint((0,0,0,0),((0,1,1,1),),((1,2),),((1,1),),0),
                  native.Joint((0,1,1,2),((0,1,1,1),(0,1,1,1)),((1,4),(4,1)),((1,0),(0,1)),1),
                  native.Joint((0,1),((0,2),(0,1)),((1,),(4,)),((F(1,2),),(2,)),1)]
    exact = near = covers = 0
    for i,instance in enumerate(instances):
        optimum = original(instance)
        answer = instance.exact_two()
        if optimum is None: assert answer is None
        else:
            check_output(instance,answer)
            if instance.rank: assert instance.minimum(answer) >= optimum/2
        exact += 1
        if i < 12 or 32 <= i < 37:
            answer = instance.near(F(1,2))
            if optimum is None: assert answer is None
            else:
                check_output(instance,answer)
                if instance.rank: assert instance.minimum(answer) >= optimum/4
            near += 1
        if i in (0,3,32,33):
            answer = instance.near(F(1,2),global_base=4)
            if optimum is None: assert answer is None
            else: check_output(instance,answer)
            covers += 1
    # Direct signed rounding: original feasible averages, heterogeneous owner
    # value orders, persistent negative dummy credit and every count prefix.
    rounding = 0
    for q in (1,2):
        for h in range(6):
            rank = tuple(min(s.bit_count(),1+h % 2) for s in range(1 << q))
            rr = (rank,rank)
            values = tuple(tuple(F((j+1)*(p+1) % 5) for p in range(q)) for j in range(2))
            costs = tuple(tuple(F((-1 if j else 1)*(h+p+1),2) for p in range(q)) for j in range(2))
            options = integer_options(rank,q)
            first,last = options[h % len(options)],options[-1-h % len(options)]
            fractional = (tuple(F(a+b,2) for a,b in zip(first,last)),tuple(F(2*a+b,3) for a,b in zip(first,last)))
            rounded = native.round_counts(q,rr,values,costs,fractional)
            assert all(physical(rank,row) for row in rounded)
            before = sum((costs[j][p]*fractional[j][p] for j in range(2) for p in range(q)),F(0))
            after = sum((costs[j][p]*rounded[j][p] for j in range(2) for p in range(q)),F(0))
            assert after <= before
            for p in range(q):
                order = sorted(range(2),key=lambda j:(-values[j][p],j))
                for length in range(1,3):
                    total = sum((fractional[j][p] for j in order[:length]),F(0))
                    assert sum(rounded[j][p] for j in order[:length]) >= total.numerator//total.denominator
            rounding += 1
    # Nonnegative separator checked against every original integer vertex:
    # budget zero and modular ranks make this test region itself integral.
    shared = native.Joint((0,1,1,2),((0,2,2,2),),((1,3),),((0,0),),0)
    region = shared.role_region(2,(0,))
    row,_ = region.separate((0,),(F(3),F(0)))
    assert row is not None and row.capacity >= 0 and all(a >= 0 for a in row.coefficients)
    for counts in integer_options(shared.ranks[0],2):
        if counts[1] == 1:
            assert row.coefficients[0]*counts[0] <= row.capacity
    # First-crossing recursion truly deletes; early successes keep all of Q.
    three = native.Joint((0,1,1,2,1,2,2,3),((0,1,1,1,1,1,1,1),),((1,1,1),),((0,0,0),),0)
    witness = three.gap(2,2,2,1)
    assert witness is None and three.last_trace['certificates'] > 0
    early = native.Joint((0,1,1,2,1,2,2,3),((0,1,1,2,1,2,2,3),),((1,1,4),),((0,0,0),),0)
    witness = early.gap(2,2,1,F(1,2))
    assert witness is not None and witness.allowed == (0,1)
    assert all(witness.counts[0][p] >= F(1,2) for p in witness.allowed)
    check_output(early,early.recover(2,witness))
    # q=4 enters the actual logarithmic-block cover branch, including failure.
    four_player = tuple(s.bit_count() for s in range(16))
    empty_cover = native.Joint(four_player,(),(),(),0)
    assert empty_cover.gap(1,2,2,1,global_base=4) is None
    covers += 1
    # A 101-bit count has no unit-sized loop in LP, prefix or output.
    huge = 1 << 100
    binary = native.Joint((0,1),((0,huge),),((F(3,2),),),((0,),),0)
    output = binary.exact_two()
    check_output(binary,output)
    assert binary.minimum(output) == F(3,2)*huge
    # Safe varying-accuracy cover validation must avoid numeric-size powers.
    ratio = F((1 << 120)+1,1 << 119)
    assert native.admissible(3*ratio,ratio) == 3*ratio
    # Compulsory two-value quota branches independently compared with OPT.
    quota_calls = 0
    mixed = native.Joint((0,1,1,2),((0,4,1,5),),((1,10),),((1,0),),3)
    answer = mixed.quota_target(3)
    check_output(mixed,answer)
    assert mixed.minimum(answer) >= F(3,2)
    quota_calls += 1
    for rank in ranks[::3]:
        for values in ((1,3),(3,1),(1,1),(3,3),(0,3)):
            instance = native.Joint((0,1,1,2),(rank,),(values,),((1,0),),2)
            optimum = original(instance)
            for d in (2,3,4):
                for target in (F(1),F(5,2),F(5),F(7)):
                    answer = instance.quota_target(target,d)
                    if answer is None: assert optimum < target
                    else:
                        check_output(instance,answer)
                        assert instance.minimum(answer) >= target/d
                    quota_calls += 1
    # Producer-disabled verifier and strict record boundary.
    good = instances[33].exact_two()
    persistent = instances[33].role_region(5,(0,1)).feasible(((0,F(1)),(1,F(1))))
    assert persistent is not None and persistent[-1][0] == 1
    saved = native.Joint.role_region
    native.Joint.role_region = lambda *args: (_ for _ in ()).throw(AssertionError('producer used'))
    try: assert instances[33].verify(good)
    finally: native.Joint.role_region = saved
    class Duck:
        basis,counts = good.basis,good.counts
    assert not instances[33].verify(Duck())
    assert not instances[33].verify(native.Allocation(good.basis,((0,F(1)),)))
    invalid = 0
    for thunk in (lambda:native.Joint((0,1,1,0),(),(),(),0),
                  lambda:native.Joint((0,1),((0,F(1,2)),),((1,),),((0,),),0),
                  lambda:native.Joint((0,1),((0,1),),((1.0,),),((0,),),0),
                  lambda:instances[0].near(0),lambda:instances[0].near(F(1,2),global_base=2),
                  lambda:instances[0].quota_target(1,1)):
        try: thunk()
        except ValueError: invalid += 1
        else: raise AssertionError('invalid input accepted')
    print(f'PASS joint: {exact} original optima, {near} near calls, {covers} streamed covers, '
          f'{rounding} signed prefix roundings, {quota_calls} quota targets, 101-bit counts, '
          f'producer-disabled verifier, 2 forged and {invalid} malformed cases')


if __name__ == '__main__': run()
