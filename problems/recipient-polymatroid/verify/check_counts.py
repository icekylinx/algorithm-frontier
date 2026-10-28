#!/usr/bin/env python3
"""Independent original-inequality enumeration for binary-count interfaces.

Copyright 2026 icekylinx. Authored by GPT-6 Astra Pro. Apache-2.0.
"""
import importlib.util
from pathlib import Path
import sys
from itertools import product
from fractions import Fraction as F
from functools import reduce

path = Path(__file__).resolve().parents[1] / 'reference' / 'counts.py'
spec = importlib.util.spec_from_file_location('recipient_counts', path)
m = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = m
spec.loader.exec_module(m)


def feasible(f, x):
    return all(sum(v for p, v in enumerate(x) if s >> p & 1) <= limit
               for s, limit in enumerate(f))


def vectors(caps):
    return tuple(product(*(range(c + 1) for c in caps)))


fixtures = {(0,)}
for n in range(1, 4):
    for caps in product(range(3), repeat=n):
        for rank in range(sum(caps) + 1):
            fixtures.add(tuple(min(rank, sum(c for p, c in enumerate(caps) if s >> p & 1))
                               for s in range(1 << n)))
    # Nonseparable coverage ranks: original players share service features.
    for owners in product(range(4), repeat=n):
        fixtures.add(tuple((reduce(int.__or__,
                           (owners[p] for p in range(n) if s >> p & 1), 0)).bit_count()
                           for s in range(1 << n)))
counts = dict(tables=0, ranks=0, availability=0, recoveries=0, minimal=0, rejected=0)
for f in sorted(fixtures, key=lambda f: (len(f), f)):
    n = len(f).bit_length() - 1
    table = m.RankTable(n, f)
    all_counts = vectors(table.caps)
    independent = tuple(x for x in all_counts if feasible(f, x))
    # Native feasible allocations are the oracle, not the rank minimization formula.
    native_rank = {z: max(sum(x) for x in independent if all(a <= b for a, b in zip(x, z)))
                   for z in all_counts}
    counts['tables'] += 1
    for z in all_counts:
        assert table.rank(z) == native_rank[z]
        counts['ranks'] += 1
        g = tuple(native_rank[tuple(table.caps[p] if s >> p & 1 else z[p]
                                    for p in range(n))] - native_rank[z]
                  for s in range(1 << n))
        assert table.contracted(z) == g
        availability = table.availability(z)
        for p in range(n):
            assert availability[p] <= table.caps[p] - z[p]
            for a in range(table.caps[p] - z[p] + 1):
                more = tuple(v + (a if q == p else 0) for q, v in enumerate(z))
                assert native_rank[more] - native_rank[z] == min(a, availability[p])
                counts['availability'] += 1
        for original in independent:
            h = table.recover_comparator(z, original)
            retained = [x for x in vectors(original) if feasible(g, x)]
            assert feasible(g, h) and all(a <= b for a, b in zip(h, original))
            assert sum(h) == max(map(sum, retained))
            assert sum(original) - sum(h) <= native_rank[z]
            counts['recoveries'] += 1
for original in product(range(4), repeat=3):
    for values in [(F(0),F(1,3),F(2,3)), (F(1,2),F(3,2),F(5,3))]:
        utility = sum(n*v for n,v in zip(original,values))
        for threshold in [F(1,3),F(1),F(2),utility]:
            if 0 < threshold <= utility:
                h = m.minimal_bundle(original,values,threshold)
                total = sum(n*v for n,v in zip(h,values))
                assert total >= threshold and all(a <= b for a,b in zip(h,original))
                assert all(total-v < threshold for n,v in zip(h,values) if n)
                counts['minimal'] += 1
# Binary counts remain numerical in all loops, even with two huge owner blocks.
large = 10**100
big = m.RankTable(2,(0,large,large,large))
assert big.rank((large,large)) == large
assert big.availability((large//3,large//3)) == (large-2*(large//3),)*2
assert big.recover_comparator((large,0),(0,large)) == (0,0)
assert m.minimal_bundle((large,large),(F(1,3),F(0)),F(7,3)) == (7,0)
invalid = [lambda: m.RankTable(1,(1,1)),lambda: m.RankTable(1,(0,-1)),
           lambda: m.RankTable(2,(0,1,1,3)),lambda: m.RankTable(2,(0,2,1,1)),
           lambda: big.rank((large+1,0)),lambda: big.rank((True,0)),
           lambda: big.recover_comparator((0,0),(large,large)),
           lambda: m.minimal_bundle((1,),(0.5,),1),
           lambda: m.minimal_bundle((1,),(1,),2),
           lambda: m.minimal_bundle((1,),(1,),0)]
for call in invalid:
    try:
        call()
    except ValueError:
        counts['rejected'] += 1
    else:
        raise AssertionError('malformed input accepted')
print('PASS original-polymatroid count interfaces:',counts,'; 100-digit count guards')
