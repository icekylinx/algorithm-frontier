"""Binary full-marginal machine absorption and certified original-base lifting.

Copyright 2026 Yilin Liu. Authored by GPT-6 Astra Pro. Apache-2.0.
Complete rank tables have explicit costs; no individual job copies are built.
"""
from dataclasses import dataclass
from fractions import Fraction as F
from pathlib import Path
import importlib.util
import sys


def _core():
    name = '_algorithm_frontier_recipient_counts'
    if name not in sys.modules:
        path = Path(__file__).resolve().parents[2] / 'recipient-polymatroid/reference/counts.py'
        spec = importlib.util.spec_from_file_location(name, path)
        module = importlib.util.module_from_spec(spec)
        sys.modules[name] = module
        spec.loader.exec_module(module)
    return sys.modules[name]


RankTable = _core().RankTable


def rational(value):
    if type(value) not in (int, F):
        raise ValueError('exact rational required')
    return F(value)


def _box_base(rank, box):
    """Greedy base of a box-restricted polymatroid; no copy expansion."""
    n = rank.n
    box = tuple(box)
    if len(box) != n or any(type(v) is not int or v < 0 for v in box):
        raise ValueError('nonnegative original-coordinate box required')
    output, prefix, previous = [], 0, 0
    for p in range(n):
        prefix |= 1 << p
        s, best = prefix, None
        while True:
            value = rank.values[s] + sum(box[v] for v in range(n)
                                        if prefix >> v & 1 and not s >> v & 1)
            best = value if best is None else min(value, best)
            if not s:
                break
            s = (s - 1) & prefix
        output.append(best - previous)
        previous = best
    return tuple(output)


@dataclass(frozen=True)
class Closure:
    removed: tuple
    remaining: tuple
    committed: tuple  # original physical-machine rows; zeros outside removed
    ranks: tuple      # contracted RankTable objects on remaining order
    bottleneck: F
    residual_large: int


class Absorption:
    def __init__(self, ranks, sizes, large):
        self.ranks = tuple(ranks)
        if not self.ranks or any(type(f) is not RankTable for f in self.ranks):
            raise ValueError('at least one validated original rank table required')
        self.n, self.m = self.ranks[0].n, len(self.ranks)
        if any(f.n != self.n for f in self.ranks):
            raise ValueError('original physical dimensions differ')
        self.sizes = tuple(rational(p) for p in sizes)
        if len(self.sizes) != self.m or any(p <= 0 for p in self.sizes):
            raise ValueError('one positive common size per original job type required')
        self.large = tuple(large)
        if (not self.large or any(type(j) is not int or not 0 <= j < self.m for j in self.large)
                or len(set(self.large)) != len(self.large)):
            raise ValueError('distinct original distinguished type IDs required')
        order, rows, loads, bottlenecks = [], [(0,)*self.m for _ in range(self.n)], [], [F(0)]
        residual = [sum(self.ranks[j].values[-1] for j in self.large)]
        mask = 0
        for _ in range(self.n):
            candidates = []
            for p in range(self.n):
                if not mask >> p & 1:
                    counts = tuple(f.values[mask | 1 << p]-f.values[mask] for f in self.ranks)
                    load = sum((v*s for v,s in zip(counts,self.sizes)),F(0))
                    candidates.append((load,p,counts))
            load,p,counts = min(candidates)
            order.append(p);rows[p]=counts;loads.append(load)
            bottlenecks.append(max(bottlenecks[-1],load))
            mask |= 1 << p
            residual.append(sum(self.ranks[j].values[-1]-self.ranks[j].values[mask] for j in self.large))
        self.order,self.rows,self.loads = tuple(order),tuple(rows),tuple(loads)
        self.bottlenecks,self.residual = tuple(bottlenecks),tuple(residual)

    def closure(self, threshold):
        threshold = rational(threshold)
        if threshold < 0:
            raise ValueError('nonnegative load threshold required')
        length = max(i for i,b in enumerate(self.bottlenecks) if b <= threshold)
        removed = self.order[:length]
        chosen = frozenset(removed)
        remaining = tuple(p for p in range(self.n) if p not in chosen)
        mask = sum(1 << p for p in removed)
        maps = tuple(sum(1 << p for i,p in enumerate(remaining) if s >> i & 1)
                     for s in range(1 << len(remaining)))
        ranks = tuple(RankTable(len(remaining),tuple(f.values[mask | s]-f.values[mask] for s in maps))
                      for f in self.ranks)
        committed = tuple(row if p in chosen else (0,)*self.m for p,row in enumerate(self.rows))
        return Closure(removed,remaining,committed,ranks,self.bottlenecks[length],self.residual[length])

    def for_budget(self, budget):
        if type(budget) is not int or budget < 0:
            raise ValueError('nonnegative binary residual-rank budget required')
        index = next(i for i,r in enumerate(self.residual) if r <= budget)
        return self.closure(self.bottlenecks[index])

    def _checked_closure(self, result):
        if type(result) is not Closure or result != self.closure(result.bottleneck):
            raise ValueError('canonical original-input closure required')

    def _schedule(self, ranks, rows):
        rows = tuple(tuple(row) for row in rows)
        n = ranks[0].n
        if len(rows) != n or any(len(row) != self.m for row in rows):
            raise ValueError('one row per physical machine required')
        for j,rank in enumerate(ranks):
            x = tuple(row[j] for row in rows)
            if not rank.independent(x) or sum(x) != rank.values[-1]:
                raise ValueError('every original resource base is mandatory')
        return rows

    def lift(self, closure, residual_rows):
        self._checked_closure(closure)
        residual_rows = self._schedule(closure.ranks,residual_rows)
        result = list(closure.committed)
        for p,row in zip(closure.remaining,residual_rows):
            result[p] = row
        return self._schedule(self.ranks,result)

    def dominated(self, closure, original_rows):
        """Produce an actual contracted base dominated by an original schedule."""
        self._checked_closure(closure)
        original_rows = self._schedule(self.ranks,original_rows)
        columns = []
        for j,rank in enumerate(closure.ranks):
            box = tuple(original_rows[p][j] for p in closure.remaining)
            h = _box_base(rank,box)
            if sum(h) != rank.values[-1]:
                raise AssertionError('original base failed contraction domination')
            columns.append(h)
        return self._schedule(closure.ranks,tuple(tuple(column[i] for column in columns)
                                                 for i in range(len(closure.remaining))))


@dataclass(frozen=True)
class PositionCommitment:
    committed: tuple
    remaining: tuple  # original nonloops after contracting committed
    rank: RankTable
    bottleneck: F


def position_commitment(rank, weights, budget):
    """Minimize maximum committed weight for a prescribed residual rank."""
    if type(rank) is not RankTable or any(c > 1 for c in rank.caps):
        raise ValueError('ordinary original-player matroid required')
    weights = tuple(rational(w) for w in weights)
    if len(weights) != rank.n or any(w < 0 for w in weights):
        raise ValueError('nonnegative original-player bottleneck weights required')
    if type(budget) is not int or not 0 <= budget <= rank.values[-1]:
        raise ValueError('residual rank must lie between zero and original rank')
    chosen, mask = [], 0
    need = rank.values[-1]-budget
    for p in sorted(range(rank.n),key=lambda p:(weights[p],p)):
        if len(chosen)==need:
            break
        enlarged=mask|1<<p
        if rank.values[enlarged]>rank.values[mask]:
            chosen.append(p);mask=enlarged
    remaining=tuple(p for p in range(rank.n) if not mask>>p&1
                    and rank.values[mask|1<<p]>rank.values[mask])
    maps=tuple(sum(1<<p for i,p in enumerate(remaining) if s>>i&1)
               for s in range(1<<len(remaining)))
    contracted=RankTable(len(remaining),tuple(rank.values[mask|s]-len(chosen) for s in maps))
    return PositionCommitment(tuple(chosen),remaining,contracted,
                              max((weights[p] for p in chosen),default=F(0)))


def padding_scale(pairs, coefficient):
    """Exact minimax scalar padding certificate for positive eligibility pairs.

    Each pair is (minimum eligible size, maximum eligible size). This optimizes
    the stated scalar load bound, not an underlying scheduling objective.
    """
    pairs=tuple(tuple(map(rational,pair)) for pair in pairs)
    coefficient=rational(coefficient)
    if (not pairs or coefficient<1 or any(len(pair)!=2 or not 0<pair[0]<=pair[1] for pair in pairs)):
        raise ValueError('nonempty positive eligibility pairs and coefficient at least one required')
    maximum=max(a for _,a in pairs)
    width=max(a-lo for lo,a in pairs)
    if coefficient==1:
        return width,maximum-width
    boundaries=sorted({F(0),*(a for _,a in pairs)})
    for lower,upper in zip(boundaries,boundaries[1:]):
        active_width=max(a-lo for lo,a in pairs if a>lower)
        cost=max(lower,((coefficient-1)*maximum+active_width)/coefficient)
        if cost<upper:
            scale=coefficient*(maximum-cost)
            return cost,scale
    raise AssertionError('positive eligible minimum must admit an overhead below maximum')


@dataclass(frozen=True)
class Eligibility:
    lower: tuple
    upper: tuple
    small_exposure: tuple
    collision: F | None  # None denotes no possible two-large-unit collision
    large_recipients: RankTable


def eligibility(engine):
    """Original singleton size intervals, collision threshold and Boolean rank."""
    if type(engine) is not Absorption:
        raise ValueError('validated original scheduling instance required')
    large=frozenset(engine.large)
    lower,upper,exposure,collisions=[],[],[],[]
    for p in range(engine.n):
        sizes=[]
        for j in large:
            sizes.extend([engine.sizes[j]]*min(2,engine.ranks[j].values[1<<p]))
        sizes.sort()
        lower.append(sizes[0] if sizes else None)
        upper.append(sizes[-1] if sizes else None)
        if len(sizes)>1:collisions.append(sizes[0]+sizes[1])
        exposure.append(sum((engine.sizes[j]*rank.values[1<<p]
                             for j,rank in enumerate(engine.ranks) if j not in large),F(0)))
    aggregate=tuple(sum(engine.ranks[j].values[s] for j in large) for s in range(1<<engine.n))
    boolean=[]
    for s in range(1<<engine.n):
        a,best=s,None
        while True:
            value=aggregate[a]+(s^a).bit_count()
            best=value if best is None else min(best,value)
            if not a:break
            a=(a-1)&s
        boolean.append(best)
    return Eligibility(tuple(lower),tuple(upper),tuple(exposure),min(collisions,default=None),
                       RankTable(engine.n,tuple(boolean)))
