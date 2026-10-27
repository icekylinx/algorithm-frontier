"""Native ordinary fixed-rank price changes and supplied-catalog insertions.
Copyright 2026 Yilin Liu. Authored by GPT-6 Astra Pro. Apache-2.0.
Final records use the proved O(N+r^2) all-pairs alternative. Queries are
independent and use no original oracle, input cost list or optimizer.
"""
from dataclasses import dataclass
from fractions import Fraction as F
from pathlib import Path
import importlib.util
import sys


def load(name,path):
    if name not in sys.modules:
        spec=importlib.util.spec_from_file_location(name,Path(__file__).resolve().parents[2]/path)
        module=importlib.util.module_from_spec(spec)
        sys.modules[name]=module;spec.loader.exec_module(module)
    return sys.modules[name]


weighted=load('_price_weighted','robust-bounded-certificates/reference/bounded.py')
reporting=load('_price_paths','exact-failure-preservers/reference/arborescence_reporting.py')


@dataclass(frozen=True)
class Descriptor:
    gap: F
    starter: object


class PriceOracle:
    def __init__(self,baseline,cost,states,descriptors,first):
        self.baseline,self.baseline_cost=tuple(baseline),cost
        self.states,self.descriptors=tuple(states),tuple(descriptors)
        self.first=tuple(tuple(row) for row in first)

    def query(self,element,delta=0):
        if type(element) is not int or not 0<=element<len(self.states):raise ValueError('original catalog ID required')
        delta=weighted.rational(delta)
        inside=self.states[element]
        descriptor=self.descriptors[element]
        default=self.baseline_cost+(delta if inside else 0)
        candidate=None if descriptor is None else self.baseline_cost+descriptor.gap+(0 if inside else delta)
        if candidate is None or default<=candidate:return default,self.baseline
        arc=descriptor.starter
        removed=[False]*len(self.baseline)
        added=[]
        removed[arc.tail]=True;added.append(arc.label)
        source,target=arc.head,arc.tail
        while source!=target:
            arc=self.first[source][target]
            removed[arc.tail]=True;added.append(arc.label)
            source=arc.head
        chosen=tuple(e for j,e in enumerate(self.baseline) if not removed[j])+tuple(added)
        return candidate,chosen

    def record_count(self):
        # Conservative count including every starter and matrix-referenced arc.
        r=len(self.baseline)
        return 8+r+12*len(self.states)+10*r*r


def build_price(costs,rank,independent1,independent2,active=None):
    costs=tuple(weighted.rational(w) for w in costs);n=len(costs)
    if type(rank) is not int or rank<0 or not callable(independent1) or not callable(independent2):
        raise ValueError('nonnegative fixed rank and two matroid oracles required')
    if active is None:active=tuple(range(n))
    else:active=tuple(active)
    if len(set(active))!=len(active) or any(type(e) is not int or not 0<=e<n for e in active):
        raise ValueError('distinct original active IDs required')
    active=frozenset(active)
    first_oracle=lambda chosen:chosen<=active and independent1(chosen)
    second_oracle=lambda chosen:chosen<=active and independent2(chosen)
    if rank>len(active):return None
    certificate=weighted.minimum_cost(first_oracle,second_oracle,costs,rank)
    if not weighted.verify_intersection(first_oracle,second_oracle,costs,rank,certificate):
        raise RuntimeError('original restricted initialization certificate failed')
    if len(certificate.chosen)<rank:return None
    baseline=certificate.chosen;chosen=frozenset(baseline)
    best={};eligible={}
    for e in range(n):
        if e in chosen:continue
        left=tuple(j for j,a in enumerate(baseline) if independent1((chosen-{a})|{e}))
        right=tuple(j for j,a in enumerate(baseline) if independent2((chosen-{a})|{e}))
        eligible[e]=(left,right)
        if e not in active:continue
        for a in left:
            for b in right:
                arc=reporting._AuxArc(a,b,(costs[e]-costs[baseline[a]],1),label=e)
                old=best.get((a,b))
                if old is None or (arc.length,e)<(old.length,old.label):best[a,b]=arc
    arcs=tuple(best.values())
    distances,first,last=reporting._distances(rank,arcs)
    descriptors=[None]*n
    def select(e,starters):
        optimum=None;selected=None
        for arc in starters:
            distance=distances[arc.head][arc.tail]
            if distance is None:continue
            key=(arc.length[0]+distance[0],arc.length[1]+distance[1],arc.tail,arc.head,arc.label)
            if optimum is None or key<optimum:optimum,selected=key,arc
        if selected is not None:descriptors[e]=Descriptor(optimum[0],selected)
    for a,e in enumerate(baseline):select(e,(arc for arc in arcs if arc.tail==a))
    for e,(left,right) in eligible.items():
        select(e,(reporting._AuxArc(a,b,(costs[e]-costs[baseline[a]],1),label=e) for a in left for b in right))
    return PriceOracle(baseline,sum((costs[e] for e in baseline),F(0)),[e in chosen for e in range(n)],descriptors,first)
