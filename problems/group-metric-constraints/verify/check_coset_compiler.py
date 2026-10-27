#!/usr/bin/env python3
"""Independent native group/permutation checks for whole-coset compilation.
Copyright 2026 Yilin Liu. Authored by GPT-6 Astra Pro. Apache-2.0.
"""
from fractions import Fraction as F
from itertools import permutations, product
from pathlib import Path
import random
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'reference'))
from coset_compiler import Group,Coset,compile_cosets,verify_coefficients

counts = dict(groups=0, subgroups=0, nonnormal=0, items=0,
              wreath_memberships=0, original_queries=0, weighted_checks=0,
              rejected=0, nonhomomorphic_pairs=0)


def need(condition,message):
    if not condition:
        raise AssertionError(message)


def inverse(elements,operation,identity,x):
    return next(y for y in elements if operation(x,y)==identity==operation(y,x))


def native_subgroups(elements,operation,identity):
    others = [x for x in elements if x != identity]
    for bits in product((0,1),repeat=len(others)):
        subset = {identity} | {x for x,b in zip(others,bits) if b}
        if all(operation(x,y) in subset for x in subset for y in subset):
            yield subset


def check(elements,operation,identity):
    elements = list(elements)
    random.Random(len(elements)+91).shuffle(elements)
    ids = {g:i for i,g in enumerate(elements)}
    n = len(elements)
    group = Group(tuple(tuple(ids[operation(g,h)] for h in elements) for g in elements),ids[identity])
    # Faithful action on two original regular G-sets, derived without using
    # the compiler's wreath multiplication or membership formulas.
    def action(element):
        a,b,bit = element
        return tuple((side^bit)*n+ids[operation(elements[a if side^bit == 0 else b],g)]
                     for side in range(2) for g in elements)
    def compose(a,b):
        return tuple(a[b[i]] for i in range(2*n))
    ambient = tuple(product(range(n),range(n),(0,1)))
    actions = {x:action(x) for x in ambient}
    for x in ambient:
        for y in ((ids[identity],ids[identity],0),group.query(0),group.query(n-1)):
            need(actions[group.wreath_multiply(x,y)]==compose(actions[x],actions[y]),'wrong multiplication')
    descriptors, direct = [None], [set()]
    for h in native_subgroups(elements,operation,identity):
        counts['subgroups'] += 1
        if any({operation(operation(a,x),inverse(elements,operation,identity,a)) for x in h} != h for a in elements):
            counts['nonnormal'] += 1
        for a in elements:
            descriptors.append(Coset(ids[a],tuple(sorted(ids[x] for x in h))))
            direct.append({ids[operation(a,x)] for x in h})
    compiled = compile_cosets(group,descriptors)
    for i,item in enumerate(compiled):
        need(item.original==i and item.group is group,'original item/ambient identity')
        generators = tuple(actions[x] for x in item.generators())
        identity_action = tuple(range(2*n))
        closure,queue = {identity_action},[identity_action]
        for old in queue:
            for generator in generators:
                new = compose(old,generator)
                if new not in closure:
                    closure.add(new); queue.append(new)
        for x in ambient:
            need(item.contains(x)==(actions[x] in closure),'wrong subgroup membership')
            counts['wreath_memberships'] += 1
        for g in range(n):
            expected = g in direct[i]
            need(item.accepts_original(g)==expected==item.contains(group.query(g)),'coset query changed')
            counts['original_queries'] += 1
        counts['items'] += 1
    # Query embedding is deliberately not a homomorphism: multiplying two
    # odd query images gives even parity. No algorithm assumes otherwise.
    for g,h in product(range(n),repeat=2):
        need(group.wreath_multiply(group.query(g),group.query(h)) != group.query(group.table[g][h]),'unexpected parity')
        counts['nonhomomorphic_pairs'] += 1
    rng = random.Random(112+n)
    for _ in range(50):
        chosen = [rng.randrange(len(descriptors)) for _ in range(5)]
        items = tuple(descriptors[i] for i in chosen)
        weights = tuple(F(rng.randrange(5),rng.randrange(1,4)) for _ in chosen)
        coefficients = tuple(F(rng.randrange(5),2) for _ in chosen)
        epsilon = F(rng.randrange(4),4)
        for exact_total in (False,True):
            expected = not exact_total or sum(w*c for w,c in zip(weights,coefficients))==sum(weights)
            for g in range(n):
                original = sum(w for i,w in zip(chosen,weights) if g not in direct[i])
                reduced = sum(w*c for i,w,c in zip(chosen,weights,coefficients) if g not in direct[i])
                expected = expected and (1-epsilon)*original<=reduced<=(1+epsilon)*original
            need(verify_coefficients(group,items,weights,coefficients,epsilon,exact_total)==expected,'weighted verifier')
            counts['weighted_checks'] += 1
        need(verify_coefficients(group,items,weights,(1,)*5,0,True),'identity weights')
    counts['groups'] += 1


def hostile():
    group=Group(((0,1),(1,0)))
    item=Coset(0,())
    for coefficients,epsilon in [((-1,),F(1,2)),((1.0,),F(1,2)),((True,),F(1,2)),((1,),1),((1,),-1),((1,),0.5),((),0)]:
        need(not verify_coefficients(group,(item,),(1,),coefficients,epsilon),'malformed coefficient')
        counts['rejected'] += 1
    for bad in [Coset(True,()),Coset(2,()),Coset(0,(-1,)),Coset(0,(False,)),object()]:
        try: compile_cosets(group,(bad,))
        except ValueError: pass
        else: raise AssertionError('malformed coset')
        counts['rejected'] += 1
    for table,e in [((),0),(((0,),),True),(((0,1),(1,1)),0),(((0,True),(1,0)),0),(((0,1),(1,)),0),(((1,0),(0,1)),0)]:
        try: Group(table,e)
        except ValueError: pass
        else: raise AssertionError('malformed group')
        counts['rejected'] += 1
    for value in [(0,0,True),(0,2,1),(0,0,2),[0,0,1]]:
        try: group.wreath_element(value)
        except ValueError: pass
        else: raise AssertionError('malformed wreath element')
        counts['rejected'] += 1


if __name__=='__main__':
    for n in range(1,7):
        check(range(n),lambda a,b,n=n:(a+b)%n,0)
    for k in (3,4):
        check(list(product(range(k),(0,1))),lambda a,b,k=k:((a[0]+(-1 if a[1] else 1)*b[0])%k,a[1]^b[1]),(0,0))
    ps=tuple(permutations(range(3)))
    check(ps,lambda a,b:tuple(a[b[i]] for i in range(3)),(0,1,2))
    hostile()
    need(counts['nonnormal']>0,'no nonnormal fixture')
    print('PASS whole-coset compiler:',counts)
