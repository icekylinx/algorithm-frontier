#!/usr/bin/env python3
"""Exercise the complete short-range construction against exhaustive search.

The reference implementation keeps half lists, row cursors and the current
quotient arrays.  It covers both scale regimes, signed normalization and
indexed witness recovery.  Python integer multiplication is used for exact
packed convolution; this script does not certify its asymptotic bit cost.
The manuscript proves a separate elementary transform with the required
asymptotic convolution bound.
"""
from __future__ import annotations

import argparse
from bisect import bisect_left, bisect_right
from dataclasses import dataclass
from heapq import heapify, heappop, heappush
from itertools import groupby, product
import json
from math import gcd, isqrt
from pathlib import Path
from typing import Iterator


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def masks(weights: tuple[int, ...]) -> Iterator[tuple[int, int]]:
    """Enumerate indexed occurrences, without storing the full block list."""
    for mask in range(1 << len(weights)):
        yield sum(w for i,w in enumerate(weights) if mask >> i & 1), mask


class RawBlock:
    def __init__(self, weights: tuple[int, ...], offset: int = 0):
        self.weights = weights
        self.offset = offset
        self.split = len(weights)//2
        self.left = list(masks(weights[:self.split]))
        self.right = [(w,mask << self.split)
                      for w,mask in masks(weights[self.split:])]

    def occurrences(self) -> Iterator[tuple[int, int]]:
        for w,mask in masks(self.weights):
            yield w+self.offset,mask

    def nested(self, q1: int, q2: int) -> Iterator[tuple[int, int]]:
        """Stream by (weight mod q1, weight mod q2, weight, mask).

        Each row rotates primary groups and, inside each primary group,
        secondary groups of one shared sorted right list.  No row is copied.
        """
        require(q1 > 0 and q2 % q1 == 0, 'nested positive moduli')
        ordered = sorted(self.right, key=lambda r:(r[0]%q1,r[0]%q2,r[0],r[1]))
        primary: list[int] = []
        secondary: list[list[tuple[int,int,int]]] = []
        i = 0
        while i < len(ordered):
            p = ordered[i][0]%q1
            primary.append(p)
            groups = []
            while i < len(ordered) and ordered[i][0]%q1 == p:
                s = ordered[i][0]%q2
                begin = i
                while i < len(ordered) and ordered[i][0]%q1 == p and ordered[i][0]%q2 == s:
                    i += 1
                groups.append((s,begin,i))
            secondary.append(groups)
        secondary_keys = [[s for s,_,_ in groups] for groups in secondary]
        require(sum(map(len,secondary)) <= len(self.right), 'shared group directory')

        def row(lw: int, lm: int) -> Iterator[tuple[int,int]]:
            shift = lw+self.offset
            first = bisect_left(primary,(-shift)%q1)
            for step in range(len(primary)):
                pi = (first+step)%len(primary)
                groups = secondary[pi]
                pivot = bisect_left(secondary_keys[pi],(-shift)%q2)
                for turn in range(len(groups)):
                    _,lo,hi = groups[(pivot+turn)%len(groups)]
                    for ri in range(lo,hi):
                        rw,rm = ordered[ri]
                        yield shift+rw,lm|rm

        rows = [row(w,m) for w,m in self.left]
        heap = []
        for ri,it in enumerate(rows):
            w,m = next(it)
            heap.append((w%q1,w%q2,w,m,ri))
        heapify(heap)
        while heap:
            _,_,w,m,ri = heappop(heap)
            yield w,m
            nxt = next(rows[ri],None)
            if nxt is not None:
                w,m = nxt
                heappush(heap,(w%q1,w%q2,w,m,ri))

    def query(self, modulus: int, residue: int, low: int, high: int) -> Iterator[tuple[int,int]]:
        """Report a congruence and closed interval using only half lists."""
        ordered = sorted((w%modulus,w,m) for w,m in self.right)
        for lw,lm in self.left:
            shift = lw+self.offset
            wanted = (residue-shift)%modulus
            lo = bisect_left(ordered,(wanted,low-shift,-1))
            hi = bisect_right(ordered,(wanted,high-shift,1 << len(self.weights)))
            for _,rw,rm in ordered[lo:hi]:
                yield shift+rw,lm|rm


def convolution(left: list[int|None], right: list[int|None]) -> list[int]:
    """No coefficient carry: each byte field has base greater than C."""
    capacity = max(len(left),len(right))
    width = (capacity.bit_length()+7)//8
    a = bytearray(width*len(left))
    b = bytearray(width*len(right))
    for i,mask in enumerate(left):
        a[width*i] = int(mask is not None)
    for i,mask in enumerate(right):
        b[width*i] = int(mask is not None)
    value = int.from_bytes(a,'little')*int.from_bytes(b,'little')
    raw = value.to_bytes(width*(len(left)+len(right)),'little')
    return [int.from_bytes(raw[width*i:width*(i+1)],'little')
            for i in range(len(left)+len(right)-1)]


def convolution_witness(left: list[int|None], right: list[int|None], total: int) -> tuple[int,int]:
    for i,lmask in enumerate(left):
        j = total-i
        if lmask is not None and 0 <= j < len(right) and right[j] is not None:
            return lmask,right[j]  # type: ignore[return-value]
    raise AssertionError('positive convolution coefficient has a witness')


@dataclass
class Normalized:
    block: RawBlock
    scale: int
    width: int
    complement: int
    offset: int
    original_side: int


def normalize(weights: tuple[int,...], scale: int, side: int) -> Normalized:
    require(scale > 0 and all(w%scale == 0 for w in weights),'positive valid lattice scale')
    return Normalized(RawBlock(tuple(abs(w)//scale for w in weights)),scale,
                      sum(abs(w)//scale for w in weights),
                      sum(1 << i for i,w in enumerate(weights) if w < 0),
                      sum(w for w in weights if w < 0),side)


def quotient_blocks(block: RawBlock, modulus: int, width: int, capacity: int):
    key = lambda rec:(rec[0]%modulus,(rec[0]//modulus)//capacity)
    for (residue,index),records in groupby(block.nested(modulus,modulus),key):
        start = index*capacity
        length = min(capacity,(width-residue)//modulus+1-start)
        slots: list[int|None] = [None]*length
        for value,mask in records:
            position = value//modulus-start
            if slots[position] is None:
                slots[position] = mask
        yield residue,start,slots


def full_a_classes(a: Normalized, alpha: int, beta: int, capacity: int):
    scaled = RawBlock(tuple(alpha*w for w in a.block.weights))
    for primary,records in groupby(scaled.nested(beta,beta),lambda rec:rec[0]%beta):
        first = next(records)
        x0 = (first[0]//alpha)%beta
        length = (a.width-x0)//beta+1
        require(length <= capacity,'large-scale A quotient class fits')
        slots: list[int|None] = [None]*length
        slots[(first[0]//alpha)//beta] = first[1]
        for value,mask in records:
            position = (value//alpha)//beta
            if slots[position] is None:
                slots[position] = mask
        yield primary,x0,slots


def b_batches(b: Normalized, alpha: int, capacity: int):
    if alpha <= capacity:
        for residue in range(min(alpha,b.width+1)):
            length = (b.width-residue)//alpha+1
            for start in range(0,length,capacity):
                yield {residue:(start,[None]*min(capacity,length-start))}
    else:
        batch = {}
        size = 0
        for residue in range(min(alpha,b.width+1)):
            length = (b.width-residue)//alpha+1
            require(length <= capacity,'large-scale B quotient class fits')
            if size+length > 2*capacity:
                require(size > capacity,'all nonfinal packed batches are large')
                yield batch
                batch,size = {},0
            batch[residue] = (0,[None]*length)
            size += length
        if batch:
            yield batch


def solve(a_weights: tuple[int,...], b_weights: tuple[int,...], d_weights: tuple[int,...],
          target: int, ga: int, gb: int, capacity: int) -> tuple[tuple[int,int,int]|None,dict[str,int|str]]:
    a,b = normalize(a_weights,ga,0),normalize(b_weights,gb,1)
    require(capacity > 0 and capacity*capacity >= max(a.width+1,b.width+1),'range capacity')
    g = gcd(ga,gb)
    alpha,beta = ga//g,gb//g
    adjusted = target-a.offset-b.offset
    d = RawBlock(tuple(-w for w in d_weights),adjusted)
    stats: dict[str,int|str] = {'mode':'small','convolutions':0,'batches':0,'reports':0}

    def answer(am: int,bm: int,dm: int):
        result = [0,0,dm]
        result[a.original_side] = am ^ a.complement
        result[b.original_side] = bm ^ b.complement
        return tuple(result),stats

    if alpha <= capacity and beta <= capacity:
        modulus = g*alpha*beta
        for x0,sa,left in quotient_blocks(a.block,beta,a.width,capacity):
            for y0,sb,right in quotient_blocks(b.block,alpha,b.width,capacity):
                coeff = convolution(left,right)
                stats['convolutions'] += 1  # type: ignore[operator]
                base = g*(alpha*x0+beta*y0)
                low = base+modulus*(sa+sb)
                high = low+modulus*(len(coeff)-1)
                for z,dm in d.query(modulus,base%modulus,low,high):
                    stats['reports'] += 1  # type: ignore[operator]
                    position = (z-low)//modulus
                    if coeff[position]:
                        am,bm = convolution_witness(left,right,position)
                        return answer(am,bm,dm)
    else:
        if beta <= capacity:
            a,b = b,a
            alpha,beta = beta,alpha
        stats['mode'] = 'large_segmented' if alpha <= capacity else 'large_packed'
        for batch in b_batches(b,alpha,capacity):
            stats['batches'] += 1  # type: ignore[operator]
            require(sum(len(slots) for _,slots in batch.values()) <= 2*capacity,'bounded B batch')
            for y,bm in b.block.occurrences():
                entry = batch.get(y%alpha)
                if entry is not None:
                    start,slots = entry
                    position = y//alpha-start
                    if 0 <= position < len(slots) and slots[position] is None:
                        slots[position] = bm
            ac = full_a_classes(a,alpha,beta,capacity)
            current = next(ac,None)
            old_group = None
            coeff = None
            for z,dm in d.nested(g*beta,g*alpha*beta):
                stats['reports'] += 1  # type: ignore[operator]
                primary = z%(g*beta)
                if primary%g:
                    continue
                primary //= g
                while current is not None and current[0] < primary:
                    current = next(ac,None)
                if current is None:
                    break
                if current[0] != primary:
                    continue
                _,x0,left = current
                secondary = z%(g*alpha*beta)
                group = (primary,secondary)
                if group != old_group:
                    old_group,coeff = group,None
                    numerator = secondary//g-alpha*x0
                    require(numerator%beta == 0,'secondary residue exact division')
                    y0 = (numerator//beta)%alpha
                    entry = batch.get(y0)
                if entry is None:
                    continue
                sb,right = entry
                numerator = z//g-alpha*x0-beta*y0
                require(numerator%(alpha*beta) == 0,'target quotient exact division')
                position = numerator//(alpha*beta)-sb
                if not 0 <= position < len(left)+len(right)-1:
                    continue
                if coeff is None:
                    coeff = convolution(left,right)
                    stats['convolutions'] += 1  # type: ignore[operator]
                if coeff[position]:
                    am,bm = convolution_witness(left,right,position)
                    return answer(am,bm,dm)
        limit = 2 if alpha <= capacity else 1
        require(stats['convolutions'] <= limit*(1 << len(d_weights)),'charged lazy activations')
        require(stats['batches'] <= 2*capacity,'bounded B batch count')
    return None,stats


def verify() -> dict:
    counts = {'nested_streams':0,'interval_queries':0,'solver_instances':0,'targets':0,
              'small':0,'large_segmented':0,'large_packed':0,'yes':0,'no':0}
    for weights in [(),(-2,),(-2,0,2),(-3,1,1,4),(0,0,0,0),(-7,-3,2,5,5)]:
        for offset in (-13,0,17):
            block = RawBlock(weights,offset)
            raw = [(w+offset,m) for w,m in masks(weights)]
            for q1,q2 in [(1,1),(1,17),(2,14),(5,35),(1000003,1000036000099)]:
                expected = sorted(raw,key=lambda r:(r[0]%q1,r[0]%q2,r[0],r[1]))
                require(list(block.nested(q1,q2))==expected,'complete nested-residue stream')
                counts['nested_streams'] += 1
            for q in (1,3,17,1000003):
                for residue in sorted({w%q for w,_ in raw}|{0}):
                    for lo,hi in [(-100,100),(offset,offset),(offset-4,offset+4)]:
                        expected = sorted(r for r in raw if r[0]%q==residue and lo<=r[0]<=hi)
                        require(sorted(block.query(q,residue,lo,hi))==expected,'closed interval and residue query')
                        counts['interval_queries'] += 1

    cases = []
    small = list(product((-1,0,1),repeat=2))
    for a in small:
        for b in small:
            cases.append((a,b,(-2,0,3),1,1))
    for ga,gb in [(1,101),(101,1),(101,103),(6,10),(2**70,3*2**70),
                  (2**80+7,2**80+9)]:
        for a,b,d in [((-2,0,3),(-1,1,2),(-7,0,11)),
                      ((0,0),(0,0),(-1,1)),
                      ((-1,1),(-1,1),(0,0)),
                      ((),(-2,2),(-3,5))]:
            cases.append((tuple(ga*w for w in a),tuple(gb*w for w in b),d,ga,gb))
    cases += [((),(),(),1,1),((1,),(),(-1,),1,1),
              ((1,1,1,1),(1,1,1,1),(-5,0,7,7),1,1),
              ((101,202,303),(309,515,721),(-13,0,17),101,103),
              ((4,12,16),(10,15,15),(-7,0,11),4,5)]
    for a,b,d,ga,gb in cases:
        weights = a+b+d
        exhaustive = {w for w,_ in masks(weights)}
        targets = exhaustive | {min(exhaustive)-1,max(exhaustive)+1,-1,0,1}
        if max(abs(w) for w in weights or (0,)) < 1000:
            targets |= set(range(min(exhaustive)-1,max(exhaustive)+2))
        else:
            targets |= {w+1 for w in exhaustive}
        span = max(sum(abs(w)//ga for w in a)+1,sum(abs(w)//gb for w in b)+1)
        c = isqrt(span-1)+1
        counts['solver_instances'] += 1
        for target in sorted(targets):
            witness,stats = solve(a,b,d,target,ga,gb,c)
            require((witness is not None)==(target in exhaustive),'decision agrees with exhaustive masks')
            if witness is not None:
                total = 0
                for ws,mask in zip((a,b,d),witness):
                    require(0 <= mask < 1 << len(ws),'indexed witness mask range')
                    total += sum(w for i,w in enumerate(ws) if mask >> i & 1)
                require(total==target,'restored original indexed witness')
            counts['targets'] += 1
            counts[str(stats['mode'])] += 1
            counts['yes' if witness is not None else 'no'] += 1
    require(all(counts[k] for k in ('small','large_segmented','large_packed','yes','no')),
            'both scale regimes and positive/negative decisions exercised')
    return {'status':'PASS','checks':counts,
            'scope':'Full finite short-range solver, indexed witnesses, nested residue streams and interval queries; exhaustive comparison. The asymptotic convolution and arbitrary-input resource bounds remain manuscript proofs.'}


def main() -> None:
    if not __debug__:
        raise SystemExit('Run with assertions enabled (without -O or PYTHONOPTIMIZE).')
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path)
    args = parser.parse_args()
    receipt = verify()
    if args.output:
        args.output.write_text(json.dumps(receipt,indent=2)+'\n')
    print(json.dumps(receipt,indent=2))


if __name__=='__main__':
    main()
