"""Independent original-table allocation and derived-basis checks.

Attribution: icekylinx and GPT-6 Astra Pro. Apache-2.0.
No native union/dual/workload/LP helper is used by the exhaustive oracle.
"""
from dataclasses import replace
from fractions import Fraction as F
from itertools import combinations, product
from pathlib import Path
import random
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1] / 'reference'))
import intrinsic as impl


def subsets(q):
    return tuple(frozenset(p for p in range(q) if s >> p & 1) for s in range(1 << q))


def mask(selected):
    return sum(1 << p for p in selected)


def legal(rank,row):
    return all(sum(row[p] for p in range(len(row)) if s >> p & 1) <= value for s,value in enumerate(rank))


def covers(ranks,heavy,selected,q):
    owners = tuple(sorted(selected))
    for assignment in product(heavy,repeat=len(owners)):
        if all(legal(ranks[j],tuple(int(p in owners and assignment[owners.index(p)] == j) for p in range(q))) for j in heavy):
            return True
    return False


def original_bases(player,q):
    rank = player[-1]
    return tuple(s for s in subsets(q) if len(s) == rank and player[mask(s)] == rank)


def original_optimum(player,ranks,values,q,light=None,basis=None):
    bases = original_bases(player,q) if basis is None else (frozenset(basis),)
    if not player[-1] and basis is None:
        return None
    types = tuple(range(len(ranks))) if light is None else tuple(light)
    vectors = [tuple(row for row in product(*(range(ranks[j][1 << p]+1) for p in range(q))) if legal(ranks[j],row)) for j in types]
    best = F(0)
    for allocation in product(*vectors):
        utility = tuple(sum((values[j]*allocation[h][p] for h,j in enumerate(types)),F(0)) for p in range(q))
        for chosen in bases:
            best = max(best,min((utility[p] for p in chosen),default=F(0)))
    return best


def brute_geometry(player,ranks,heavy,q):
    allsets = subsets(q)
    rank = player[-1]
    independent_cover = {s for s in allsets if covers(ranks,heavy,s,q)}
    common = max((len(s) for s in independent_cover if player[mask(s)] == len(s)),default=0)
    derived_rank = rank-common
    bases = tuple(s for s in allsets if len(s) == derived_rank and
                  any(s <= basis and basis-s in independent_cover for basis in original_bases(player,q)))
    table = tuple(max((len(s & basis) for basis in bases),default=0) for s in allsets)
    nonloops = frozenset().union(*bases) if bases else frozenset()
    cover_table = tuple(max((len(t) for t in independent_cover if t <= s),default=0) for s in allsets)
    return derived_rank,len(nonloops)-derived_rank,bases,table,cover_table


def pool_rank(q,pools):
    return tuple(sum(cap for players,cap in pools if any(s >> p & 1 for p in players)) for s in range(1 << q))


def main():
    rng = random.Random(271034)
    geometry_cases = completions = allocations = near_checks = exact_checks = roundings = 0
    fixtures = []
    for q in range(1,5):
        for case in range(8):
            rank = rng.randrange(q+1)
            if case % 3:
                player = tuple(min(s.bit_count(),rank) for s in range(1 << q))
            else:
                # Partition player matroid, with an original loop at the final ID.
                player = tuple(sum(min(1,sum(bool(s >> p & 1) for p in range(q-1) if p % 2 == block)) for block in (0,1))
                               for s in range(1 << q))
            ranks = tuple(pool_rank(q,[(tuple(p for p in range(q) if p % 2 == block),rng.randrange(3)) for block in (0,1)]) for _ in range(2))
            values = (F(1),F(3))
            native = impl.Intrinsic(player,ranks,values)
            for geometry in native.splits():
                d,c,bases,table,cover = brute_geometry(player,ranks,geometry.heavy,q)
                assert geometry.rank == d and geometry.corank == c and geometry.player == table and geometry.cover == cover
                for basis in bases:
                    original,assignment = native.completion(geometry,basis)
                    assert frozenset(original) in original_bases(player,q) and basis <= set(original)
                    assert set(p for p,_ in assignment) == set(original)-basis
                    assert all(j in geometry.heavy for _,j in assignment)
                    for j in geometry.heavy:
                        row = tuple(sum(p == owner and typ == j for owner,typ in assignment) for p in range(q))
                        assert legal(ranks[j],row)
                    completions += 1
                geometry_cases += 1
            if q <= 2:
                fixtures.append((player,ranks,values))
    # More varied values, nonmodular resource ranks and explicit zero types.
    tables = tuple((0,a,b,n) for n in range(3) for a in range(n+1) for b in range(n+1) if a+b >= n)
    for _ in range(18):
        player = rng.choice(((0,1,1,1),(0,1,1,2),(0,1,0,1)))
        values = rng.choice(((F(1),F(2)),(F(2,3),F(7,4)),(F(0),F(1))))
        fixtures.append((player,(rng.choice(tables),rng.choice(tables)),values))
    fixtures.extend((((0,0),((0,2),),(F(1),)),
                     ((0,1),((0,2),(0,1)),(F(2,3),F(7,4))),
                     ((0,1,1,1,1,1,1,1),((0,2,2,3,2,3,3,3),),(F(1),)),
                     ((0,1,1,2),(),()),
                     ((0,),(),())))
    for player,ranks,values in fixtures:
        q = len(player).bit_length()-1
        native = impl.Intrinsic(player,ranks,values)
        optimum = original_optimum(player,ranks,values,q)
        for budget in range(q+1):
            exact = native.exact_two(budget)
            assert native.verify(exact)
            exact_checks += 1
            if optimum is not None and optimum > 0:
                heavy = tuple(j for j,v in enumerate(values) if v >= optimum/2 and ranks[j][-1])
                _,c,_,_,_ = brute_geometry(player,ranks,heavy,q)
                if c <= budget:
                    assert native.minimum(exact) >= optimum/2
            for epsilon in (F(1,2),F(1,3)):
                output = native.near(epsilon,budget)
                assert native.verify(output)
                near_checks += 1
                if optimum is None:
                    assert native.minimum(output) is None
                elif optimum == 0:
                    assert native.minimum(output) >= 0
                else:
                    theta = (1-epsilon)*optimum/2
                    heavy = tuple(j for j,v in enumerate(values) if v >= theta and ranks[j][-1])
                    _,c,_,_,_ = brute_geometry(player,ranks,heavy,q)
                    if c <= budget:
                        assert native.minimum(output) >= theta
                    # The same call gives the quantified exact-half endpoint.
                    heavy_half = tuple(j for j,v in enumerate(values) if v >= optimum/2 and ranks[j][-1])
                    _,c_half,_,_,_ = brute_geometry(player,ranks,heavy_half,q)
                    largest = max((v for j,v in enumerate(values) if j not in heavy_half and ranks[j][-1]),default=F(0))
                    if c_half <= budget and largest <= (F(1,2)-epsilon)*optimum:
                        assert native.minimum(output) >= optimum/2
            allocations += 1
        for geometry in native.splits():
            if not geometry.rank or not geometry.light:
                continue
            _,_,bases,_,_ = brute_geometry(player,ranks,geometry.heavy,q)
            for basis in bases:
                target = native.light_optimum(geometry,tuple(sorted(basis)))
                fractional = native.fractional(geometry,tuple(sorted(basis)),target)
                rounded = native.round_light(geometry,fractional)
                order = sorted(range(len(geometry.light)),key=lambda h:(-values[geometry.light[h]],geometry.light[h]))
                for h,j in enumerate(geometry.light):
                    assert legal(ranks[j],fractional[h]) and legal(ranks[j],rounded[h])
                    assert sum(rounded[h]) == sum(fractional[h]) == ranks[j][-1]
                for p in range(q):
                    for end in range(1,len(order)+1):
                        before = sum((fractional[h][p] for h in order[:end]),F(0))
                        assert sum(rounded[h][p] for h in order[:end]) >= before.numerator//before.denominator
                roundings += 1
    # Hidden rank has free Boolean cap and refined corank zero, yet factor<2
    # requires its special basis. Reference correctly returns legal one-unit data.
    q,r,hidden = 4,2,frozenset((0,1))
    resource = tuple(min(2*s.bit_count(),2*r)-int(s.bit_count() == r)+int(s == mask(hidden)) for s in range(1 << q))
    optional = impl.Intrinsic(tuple(min(s.bit_count(),r) for s in range(1 << q)),(resource,),(1,))
    compulsory = impl.Intrinsic(tuple(s.bit_count() for s in range(1 << q)),(resource,tuple(min(s.bit_count(),r) for s in range(1 << q))),(1,2))
    for native in (optional,compulsory):
        geometry = native.geometry(native.active)
        assert geometry.rank == geometry.corank == 0
        output = native.near(F(1,3),0)
        assert native.verify(output) and native.minimum(output) >= 1
    # Exact two-unit cover augmentation counterexample on actual coverage ranks.
    neighborhoods = ({0,1,2,3},{0,1,2,3},{0,1,2,4},{0,1,2,5})
    rank = tuple(len(set().union(*(neighborhoods[p] for p in range(4) if s >> p & 1))) for s in range(16))
    two = lambda chosen:legal(rank,tuple(2*int(p in chosen) for p in range(4)))
    assert two({0,1}) and two({0,2,3}) and not two({0,1,2}) and not two({0,1,3})
    # Binary multiplicities and values use only rational/count records, not loops.
    huge = 1 << 100
    native = impl.Intrinsic((0,1,1,2),((0,huge,huge,huge),),(F(7,3),))
    output = native.near(F(1,2),0)
    exact = native.exact_two(0)
    assert native.verify(output) and native.verify(exact) and native.minimum(exact) >= huge*F(7,12)
    assert native.last_trace['gap_calls'] < 500
    # A supplied fallback is retained by actual original value, never by a skip.
    original = impl.Intrinsic((0,1,1,1),((0,1,1,1),),(1,))
    fallback = impl.Allocation((0,),((1,0),))
    assert original.minimum(original.near(F(1,2),0,lambda model:fallback)) >= original.minimum(fallback)
    assert not original.verify(replace(fallback,basis=(0,0)))
    assert not original.verify(replace(fallback,counts=((1.0,0),)))
    saved = impl.Intrinsic.completion,impl.Intrinsic.fractional,impl.Intrinsic.round_light,impl.prefix.gap
    def unavailable(*args,**kwargs):
        raise AssertionError('output verifier called a producer')
    try:
        impl.Intrinsic.completion = impl.Intrinsic.fractional = impl.Intrinsic.round_light = impl.prefix.gap = unavailable
        assert original.verify(fallback) and original.minimum(fallback) == 1
    finally:
        impl.Intrinsic.completion,impl.Intrinsic.fractional,impl.Intrinsic.round_light,impl.prefix.gap = saved
    invalid = 0
    for thunk in (lambda:impl.Intrinsic((0,2),((0,1),),(1,)),
                  lambda:impl.Intrinsic((0,1,1,1),((0,1,1,3),),(1,)),
                  lambda:impl.Intrinsic((0,1),((0,1),),(0.5,)),
                  lambda:original.near(0,1),lambda:original.exact_two(-1),
                  lambda:original.completion(original.geometry(()),(0,1)),
                  lambda:original.near(F(1,2),0,lambda model:impl.Allocation((0,),((2,0),)))):
        try: thunk()
        except ValueError: invalid += 1
        else: raise AssertionError('invalid input accepted')
    print(f'PASS: {geometry_cases} original-input dual-union rank geometries; {completions} protected light-basis completions; {allocations} original allocation/parameter cases; {near_checks} near-two/separated calls; {exact_checks} XP/zero-corank calls; {roundings} fractional/native joint-prefix roundings; hidden-zero and two-unit nonmatroid boundaries; 101-bit counts; fallback retention; producer-disabled verifier; two forged outputs; {invalid} malformed inputs.')


if __name__ == '__main__':
    main()
