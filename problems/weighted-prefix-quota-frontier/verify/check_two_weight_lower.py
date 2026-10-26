#!/usr/bin/env python3
"""Independent finite checks of the two-positive-weight laminar lower family."""
from __future__ import annotations
from collections import Counter
from itertools import combinations
from math import comb
import json


def require(ok, message):
    if not ok:
        raise AssertionError(message)


def bits(mask):
    while mask:
        bit=mask & -mask
        yield bit.bit_length()-1
        mask ^= bit


def candidate(d, selected):
    return sum((3 if selected >> i & 1 else 4) << (3*i) for i in range(d))


def numerical(mask, d):
    return all((mask >> (3*i) & 1) + (mask >> (3*i+1) & 1)
               + 2*(mask >> (3*i+2) & 1) == 2 for i in range(d))


def formula_rank(mask, rank, forbidden):
    size=mask.bit_count()
    return min(size, rank) - (size == rank and mask in forbidden)


def lex_rank(selected, d, t):
    ordered=tuple(bits(selected))
    require(len(ordered) == t, 'decoder input has t selected blocks')
    answer=0
    previous=-1
    for index, chosen in enumerate(ordered):
        for skipped in range(previous+1, chosen):
            answer += comb(d-skipped-1, t-index-1)
        previous=chosen
    return answer


def literal_rank_table(n, rank, forbidden, counts):
    bases=tuple(sum(1 << e for e in chosen) for chosen in combinations(range(n), rank)
                if sum(1 << e for e in chosen) not in forbidden)
    base_set=set(bases)
    require(bases, 'nonempty base family')
    independent={0}
    for base in bases:
        subset=base
        while subset:
            independent.add(subset)
            subset=(subset-1) & base
    values=[]
    for subset in range(1 << n):
        value=subset.bit_count() if subset in independent else max((values[subset ^ (1 << e)] for e in bits(subset)), default=0)
        values.append(value)
        require(value == formula_rank(subset, rank, forbidden), 'closed rank formula equals literal bases')
        counts['literal_rank_comparisons'] += 1
    for left in bases:
        for right in bases:
            targets=tuple(bits(right & ~left))
            for e in bits(left & ~right):
                require(any((left ^ (1 << e) ^ (1 << f)) in base_set for f in targets), 'ordinary basis exchange')
                counts['basis_exchange_conditions'] += 1
    counts['rank_models'] += 1
    return tuple(values)


def check_families():
    counts=Counter()
    for d in range(2, 5):
        t=d//2
        r=d+t
        n=3*d
        chosen_blocks=tuple(sum(1 << i for i in selected) for selected in combinations(range(d), t))
        hidden=tuple(candidate(d, mask) for mask in chosen_blocks)
        hidden_set=set(hidden)
        require(len(hidden_set) == comb(d,t), 'candidate count')
        for mask in range(1 << n):
            require((numerical(mask,d) and mask.bit_count()==r) == (mask in hidden_set), 'exact numeric-base family')
            counts['numeric_family_comparisons'] += 1
        for left,right in combinations(hidden, 2):
            require((left & right).bit_count() <= r-3, 'three-element separation of candidate bases')
            counts['candidate_separation_comparisons'] += 1
        for index, mask in enumerate(chosen_blocks):
            require(lex_rank(mask,d,t)==index, 'combinatorial rank equals independent lex enumeration')
            counts['decoder_rank_comparisons'] += 1
        subfamilies=range(1 << len(hidden)) if d<=3 else (0, (1 << len(hidden))-1, *(1 << i for i in range(len(hidden))))
        reference=None
        for admitted in subfamilies:
            forbidden={mask for i,mask in enumerate(hidden) if not admitted >> i & 1}
            values=literal_rank_table(n,r,forbidden,counts)
            feasible=tuple(mask for mask in range(1 << n) if numerical(mask,d) and values[mask]==mask.bit_count())
            actual=max(map(int.bit_count,feasible),default=None)
            require(actual==(r if admitted else r-1), 'optional all-one objective has the claimed gap')
            require(any(mask.bit_count()==r for mask in feasible)==bool(admitted), 'mandatory feasibility equals a nonempty admitted family')
            counts['optimum_comparisons'] += 1
            if not admitted:
                reference=values
            if admitted and admitted & (admitted-1)==0:
                require(reference is not None, 'reference table evaluated first')
                restored=hidden[admitted.bit_length()-1]
                differences=tuple(mask for mask in range(1 << n) if reference[mask] != values[mask])
                require(differences==(restored,), 'one restored basis changes exactly one rank answer')
                counts['single_restore_rank_comparisons'] += 1 << n
    return dict(counts)


def check_decoder():
    counts=Counter()
    # Enumerate complete truth tables for small SAT-decoder targets. The
    # decoder is verified independently against explicit admitted sets.
    for variables in range(1, 4):
        d=2*variables
        t=variables
        r=3*variables
        selected=tuple(sum(1 << i for i in subset) for subset in combinations(range(d), t))
        require(comb(d,t)>=1 << variables, 'all assignments fit in the candidate family')
        for allowed in range(1 << (1 << variables)):
            explicit={candidate(d,subset) for index,subset in enumerate(selected)
                      if index < 1 << variables and allowed >> index & 1}
            for index, subset in enumerate(selected):
                decoded=lex_rank(subset,d,t)
                accepted=decoded < 1 << variables and bool(allowed >> decoded & 1)
                require(accepted==(candidate(d,subset) in explicit), 'encoded accepting predicate equals literal admitted set')
                counts['decoder_membership_comparisons'] += 1
            require(bool(explicit)==bool(allowed), 'encoded feasibility equals truth-table satisfiability')
            counts['decoder_truth_tables'] += 1
    return dict(counts)


def main():
    require(__debug__, 'run without -O; mathematical assertions must be enabled')
    print(json.dumps({'status':'passed','two_weight_lower':check_families(),
                      'encoded_decoder':check_decoder()}, indent=2, sort_keys=True))

if __name__=='__main__':
    main()
