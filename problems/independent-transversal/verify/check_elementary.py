#!/usr/bin/env python3
"""Independent exhaustive witnesses, stable invariants, and signature bounds.
Copyright 2026 Yilin Liu. Authored by GPT-6 Astra Pro. Apache-2.0.
"""
from dataclasses import replace
from itertools import combinations, product
from pathlib import Path
import random
import subprocess
import sys
REFERENCE = Path(__file__).resolve().parents[1] / 'reference'
sys.path.insert(0, str(REFERENCE))
from elementary import solve
from transversal_certificates import Constellation, Transversal, verify

counts = dict(instances=0, stable_states=0, transversals=0, constellations=0,
              existing_transversal_with_certificate=0, cascade_transitions=0,
              within_class_invariance=0, rejected=0)


def need(condition, message):
    if not condition:
        raise AssertionError(message)


def check(classes, edges, invariance=False):
    q, n = len(classes), sum(map(len, classes))
    owner = {v:i for i, group in enumerate(classes) for v in group}
    links = {frozenset((u,v)) for u,v in edges if owner[u] != owner[v]}
    adjacent = lambda u,v: frozenset((u,v)) in links
    independent = lambda vertices: all(not adjacent(u,v) for u,v in combinations(vertices,2))
    seen = {}
    previous_matching = {}
    def observe(root, matching, stars):
        counts['stable_states'] += 1
        need(root not in {owner[v] for v in matching}, 'matched root')
        need(independent(matching) and len({owner[v] for v in matching}) == len(matching), 'matching invariant')
        centers = [c for c,_ in stars]
        leaves = [v for _, group in stars for v in group]
        need(len(set(centers+leaves)) == len(centers+leaves), 'repeated forest vertex')
        need(len({owner[v] for v in leaves}) == len(leaves), 'repeated leaf class')
        active = {root} | {owner[v] for v in leaves}
        for c, group in stars:
            need(group and owner[c] in active, 'empty star or external center')
            need(set(group) == {v for v in matching if adjacent(c,v)}, 'current blockers')
            for v in centers+leaves:
                need(adjacent(c,v) == (v in group), 'noninduced star')
        need(independent(leaves), 'adjacent leaves')
        signature = tuple(len(group) for _,group in stars)+(q+1,)
        history = seen.setdefault(root,[])
        need(not history or signature < history[-1], 'signature not decreasing')
        history.append(signature)
        need(len(history) <= 2**max(q-1,0), 'composition bound')
        if root in previous_matching and len(set(matching)-previous_matching[root]) >= 2:
            counts['cascade_transitions'] += 1
        previous_matching[root] = set(matching)
    answer = solve(classes,edges,observe)
    need(verify(classes,edges,answer), 'verifier rejected answer')
    exists = any(independent(vertices) for vertices in product(*classes))
    if type(answer) is Transversal:
        need(exists and len(answer.vertices) == q and independent(answer.vertices), 'invalid transversal')
        need({owner[v] for v in answer.vertices} == set(range(q)), 'missing class')
        counts['transversals'] += 1
    else:
        need(type(answer) is Constellation, 'unknown answer')
        selected = set(answer.classes)
        leaves = [v for _,group in answer.stars for v in group]
        all_vertices = [v for c,group in answer.stars for v in (c,*group)]
        need(len(set(all_vertices)) == len(all_vertices), 'duplicate certificate')
        need(len({owner[v] for v in leaves}) == len(selected)-1, 'leaf class count')
        need(len(all_vertices) <= 2*(len(selected)-1), 'size bound')
        need(all(any(adjacent(v,u) for u in all_vertices) for i in selected for v in classes[i]), 'not total domination')
        star_edges = {frozenset((c,v)) for c,group in answer.stars for v in group}
        induced = {e for e in links if e <= set(all_vertices)}
        need(star_edges == induced, 'not induced constellation')
        counts['constellations'] += 1
        counts['existing_transversal_with_certificate'] += exists
    if invariance:
        extended = list(edges)+[pair for group in classes for pair in combinations(group,2)]
        need(solve(classes,extended) == answer and verify(classes,extended,answer), 'within-class edges changed output')
        counts['within_class_invariance'] += 1
    counts['instances'] += 1


def hostile():
    classes, edges = ((0,),(1,)), ((0,1),)
    valid = Constellation((0,1),((0,(1,)),))
    malformed = [None, {}, Transversal((0,1)), Transversal((0,)), Transversal((False,1)),
                 replace(valid,classes=(0,)), replace(valid,classes=(0,0)),
                 replace(valid,classes=(0,2)), replace(valid,stars=()),
                 replace(valid,stars=((0,()),)), replace(valid,stars=((0,(0,1)),)),
                 replace(valid,stars=((0,(1,1)),)), replace(valid,stars=((True,(0,)),)),
                 replace(valid,stars=((0,(1,)),(1,(0,))))]
    for bad in malformed:
        need(not verify(classes,edges,bad), 'accepted hostile witness')
        counts['rejected'] += 1
    for cs, es in [(((0,),()),()), (((0,),(0,)),()), (((1,),),()),
                   (((True,),),()), (classes,((0,0),)), (classes,((0,2),)),
                   (classes,((0,False),)), (classes,((0,),))]:
        need(not verify(cs,es,valid), 'malformed input accepted by verifier')
        try:
            solve(cs,es)
        except ValueError:
            pass
        else:
            raise AssertionError('malformed input accepted by producer')
        counts['rejected'] += 1
    need(not verify(classes,(),valid), 'self-domination accepted')
    counts['rejected'] += 1
    code = '''
import sys
sys.modules['elementary'] = None
from transversal_certificates import Constellation,Transversal,verify
if not verify(((0,),(1,)),((0,1),),Constellation((0,1),((0,(1,)),))):
 raise SystemExit('constellation verifier needs search')
if not verify(((0,),(1,)),(),Transversal((0,1))):
 raise SystemExit('transversal verifier needs search')
'''
    subprocess.run([sys.executable,'-B','-c',code],cwd=REFERENCE,check=True)


if __name__ == '__main__':
    check((),())
    for sizes in ((1,),(3,),(1,1),(2,2),(1,2,2),(2,2,2)):
        groups, start = [], 0
        for size in sizes:
            groups.append(tuple(range(start,start+size))); start += size
        pairs = [(u,v) for i,g in enumerate(groups) for h in groups[i+1:] for u in g for v in h]
        for mask in range(1<<len(pairs)):
            check(groups,[p for i,p in enumerate(pairs) if mask>>i&1],True)
    rng = random.Random(271028)
    for _ in range(400):
        q = rng.randrange(3,8)
        groups, start = [], 0
        for _ in range(q):
            size = rng.randrange(1,4)
            groups.append(tuple(range(start,start+size))); start += size
        edges = [p for p in combinations(range(start),2) if rng.randrange(5) == 0]
        check(groups,edges)
    hostile()
    need(counts['cascade_transitions'] > 0, 'missing cascade coverage')
    need(counts['existing_transversal_with_certificate'] > 0, 'missing nondisproof certificate case')
    print('PASS elementary transversal:',counts)
