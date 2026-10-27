"""Exact complete-table intrinsic-value reference, with actual light omission.

Attribution: Yilin Liu and GPT-6 Astra Pro. Apache-2.0.
Derived union/completion and prefix search use canonical exact primitives.
Light realization/rounding streams rational LP vertices: that finite basis
count is separate from the theorem's paid polynomial LP/intersection work.
The public constant-factor fallback is not implemented here.
"""
from dataclasses import dataclass
from fractions import Fraction as F
from itertools import combinations
from math import lcm
from pathlib import Path
import importlib.util
import sys


def load(name,path):
    if name not in sys.modules:
        spec = importlib.util.spec_from_file_location(name,Path(__file__).resolve().parents[2] / path)
        module = importlib.util.module_from_spec(spec)
        sys.modules[name] = module
        spec.loader.exec_module(module)
    return sys.modules[name]


weighted = load('_intrinsic_weighted','robust-bounded-certificates/reference/bounded.py')
prefix = load('_intrinsic_prefix','whole-ground-allocation/reference/selection.py')
linear = load('_intrinsic_linear','two-time-scheduling/reference/scheduling.py')


def subsets(mask):
    current = mask
    while True:
        yield current
        if not current:
            break
        current = (current-1) & mask


def mask_of(players,q):
    players = tuple(players)
    if (any(type(p) is not int or not 0 <= p < q for p in players)
            or len(set(players)) != len(players)):
        raise ValueError('distinct original owner IDs required')
    return sum(1 << p for p in players)


def members(mask,q):
    return tuple(p for p in range(q) if mask >> p & 1)


def dual(rank):
    full = len(rank)-1
    return tuple(s.bit_count()+rank[full ^ s]-rank[full] for s in range(len(rank)))


def box(rank):
    return tuple(min(rank[t]+(s ^ t).bit_count() for t in subsets(s)) for s in range(len(rank)))


def union(first,second):
    return tuple(min((s ^ t).bit_count()+first[t]+second[t] for t in subsets(s)) for s in range(len(first)))


def greedy_basis(rank,allowed):
    chosen = 0
    for p in range(allowed.bit_length()):
        if allowed >> p & 1 and rank[chosen | (1 << p)] > rank[chosen]:
            chosen |= 1 << p
    return chosen


def feasible(rank,counts):
    return (all(weighted.rational(x) >= 0 for x in counts)
            and all(sum((counts[p] for p in range(len(counts)) if s >> p & 1),F(0)) <= bound
                    for s,bound in enumerate(rank)))


def vertex(rows,dimension):
    """Stream a bounded LP's active bases; return the first feasible vertex."""
    rows = tuple(sorted(set((tuple(map(F,a)),F(b)) for a,b in rows)))
    if dimension == 0:
        return () if all(b >= 0 for _,b in rows) else None
    for active in combinations(rows,dimension):
        point = linear.solve_square(active)
        if point is not None and all(sum((a*x for a,x in zip(row,point)),F(0)) <= b for row,b in rows):
            return point
    return None


class BaseLP:
    """Original type bases, eliminating each last-owner coordinate exactly."""
    def __init__(self,ranks,q):
        self.ranks,self.q = tuple(ranks),q
        self.m = len(self.ranks)
        self.dimension = self.m*max(0,q-1)
        self.totals = tuple(row[-1] for row in self.ranks)

    def reduce(self,terms,bound):
        row = [F(0)]*self.dimension
        constant = F(0)
        for j,p,value in terms:
            value = F(value)
            if p == self.q-1:
                constant += value*self.totals[j]
                for u in range(self.q-1): row[j*(self.q-1)+u] -= value
            else:
                row[j*(self.q-1)+p] += value
        return tuple(row),F(bound)-constant

    def rows(self):
        rows = []
        for j,rank in enumerate(self.ranks):
            for p in range(self.q): rows.append(self.reduce(((j,p,-1),),0))
            for s,bound in enumerate(rank):
                rows.append(self.reduce(((j,p,1) for p in range(self.q) if s >> p & 1),bound))
        return rows

    def expand(self,point):
        return tuple(tuple(point[j*(self.q-1)+p] if p < self.q-1 else
                           self.totals[j]-sum(point[j*(self.q-1):(j+1)*(self.q-1)],F(0))
                           for p in range(self.q)) for j in range(self.m))


@dataclass(frozen=True)
class Geometry:
    heavy: tuple
    light: tuple
    cover: tuple
    union: tuple
    player: tuple
    nonloops: tuple
    rank: int
    corank: int


@dataclass(frozen=True)
class Allocation:
    basis: tuple
    counts: tuple  # original type-major integral owner vectors


class Intrinsic:
    def __init__(self,player_rank,resource_ranks,values):
        self.player = tuple(player_rank)
        length = len(self.player)
        if not length or length & (length-1):
            raise ValueError('complete player rank table required')
        self.q = length.bit_length()-1
        self.ranks = tuple(tuple(row) for row in resource_ranks)
        self.values = tuple(weighted.rational(v) for v in values)
        if len(self.ranks) != len(self.values) or any(v < 0 for v in self.values):
            raise ValueError('invalid intrinsic values')
        # The canonical validator checks all original polymatroid axioms.
        weighted.table_scenario((self.player,)+self.ranks,
                                tuple((F(0),)*(len(self.ranks)+1) for _ in range(self.q)),0)
        if any(value > s.bit_count() for s,value in enumerate(self.player)):
            raise ValueError('player rank is not a matroid rank')
        self.rank = self.player[-1]
        self.dual = dual(self.player)
        self.active = tuple(j for j,v in enumerate(self.values) if v > 0 and self.ranks[j][-1] > 0)
        self.last_trace = {}

    def verify(self,allocation):
        try:
            if type(allocation) is not Allocation or type(allocation.basis) is not tuple:
                return False
            selected = mask_of(allocation.basis,self.q)
            if selected.bit_count() != self.rank or self.player[selected] != self.rank:
                return False
            if type(allocation.counts) is not tuple or len(allocation.counts) != len(self.ranks):
                return False
            return all(type(row) is tuple and len(row) == self.q
                       and all(type(x) is int and x >= 0 and (selected >> p & 1 or x == 0)
                               for p,x in enumerate(row)) and feasible(rank,row)
                       for rank,row in zip(self.ranks,allocation.counts))
        except (ValueError,TypeError,AttributeError,IndexError):
            return False

    def minimum(self,allocation):
        if not self.verify(allocation):
            raise ValueError('invalid original allocation')
        return min((sum((self.values[j]*allocation.counts[j][p] for j in range(len(self.ranks))),F(0))
                    for p in allocation.basis),default=None)

    def zero(self):
        basis = members(greedy_basis(self.player,len(self.player)-1),self.q)
        return Allocation(basis,tuple((0,)*self.q for _ in self.ranks))

    def geometry(self,heavy):
        heavy = tuple(heavy)
        if (any(type(j) is not int or j not in self.active for j in heavy)
                or len(set(heavy)) != len(heavy)):
            raise ValueError('distinct positive original heavy type IDs required')
        light = tuple(j for j in self.active if j not in heavy)
        aggregate = tuple(sum(self.ranks[j][s] for j in heavy) for s in range(1 << self.q))
        cover = box(aggregate)
        combined = union(self.dual,cover)
        derived = dual(combined)
        nonloops = tuple(p for p in range(self.q) if derived[1 << p])
        return Geometry(heavy,light,cover,combined,derived,nonloops,derived[-1],len(nonloops)-derived[-1])

    def splits(self):
        values = sorted({self.values[j] for j in self.active})
        yield self.geometry(self.active)
        for value in values:
            yield self.geometry(tuple(j for j in self.active if self.values[j] > value))

    def completion(self,geometry,light_basis):
        light = mask_of(light_basis,self.q)
        if light.bit_count() != geometry.rank or geometry.player[light] != geometry.rank:
            raise ValueError('light set is not an actual derived basis')
        complement = (len(self.player)-1) ^ light
        # Real matroid-union decomposition via owner-colour pair intersection.
        pairs = tuple((p,colour) for p in members(complement,self.q) for colour in (0,1))
        def first(chosen):
            left = sum(1 << pairs[i][0] for i in chosen if pairs[i][1] == 0)
            right = sum(1 << pairs[i][0] for i in chosen if pairs[i][1] == 1)
            return self.dual[left] == left.bit_count() and geometry.cover[right] == right.bit_count()
        second = lambda chosen: len({pairs[i][0] for i in chosen}) == len(chosen)
        decomposition = weighted.minimum_cost(first,second,(0,)*len(pairs),complement.bit_count())
        if len(decomposition.chosen) != complement.bit_count():
            raise RuntimeError('union-basis decomposition failed')
        omitted = sum(1 << pairs[i][0] for i in decomposition.chosen if pairs[i][1] == 0)
        for p in members(complement,self.q):
            if self.dual[omitted | (1 << p)] > self.dual[omitted]: omitted |= 1 << p
        if self.dual[omitted] != self.dual[-1]:
            raise RuntimeError('union basis did not span original dual')
        original = (len(self.player)-1) ^ omitted
        heavy_owners = members(original ^ light,self.q)
        scenario = weighted.table_scenario(tuple(self.ranks[j] for j in geometry.heavy),
                                          tuple((0,)*len(geometry.heavy) for _ in range(self.q)),0)
        witness = scenario(heavy_owners)
        if witness is None:
            raise RuntimeError('original heavy type realization failed')
        assignment = tuple((p,geometry.heavy[j]) for p,j in witness.assignment)
        return members(original,self.q),assignment

    def fractional(self,geometry,light_basis,target):
        ranks = tuple(self.ranks[j] for j in geometry.light)
        system = BaseLP(ranks,self.q)
        rows = system.rows()
        for p in light_basis:
            rows.append(system.reduce(((j,p,-self.values[original]) for j,original in enumerate(geometry.light)),-target))
        point = vertex(rows,system.dimension)
        if point is None:
            raise RuntimeError('workload promise has no original fractional realization')
        return system.expand(point)

    def round_light(self,geometry,fractional):
        ranks = tuple(self.ranks[j] for j in geometry.light)
        caps = tuple(tuple(row[1 << p] for p in range(self.q)) for row in ranks)
        duals = tuple(tuple(row[(len(row)-1)^s]+sum(caps[j][p] for p in range(self.q) if s >> p & 1)-row[-1]
                            for s in range(len(row))) for j,row in enumerate(ranks))
        system = BaseLP(duals,self.q)
        rows = system.rows()
        order = tuple(sorted(range(len(ranks)),key=lambda j:(-self.values[geometry.light[j]],geometry.light[j])))
        for p in range(self.q):
            for h in range(1,len(order)+1):
                chosen = order[:h]
                total = sum((caps[j][p]-fractional[j][p] for j in chosen),F(0))
                bound = -(-total.numerator//total.denominator)
                rows.append(system.reduce(((j,p,1) for j in chosen),bound))
        point = vertex(rows,system.dimension)
        if point is None:
            raise RuntimeError('complement-prefix intersection is empty')
        output = tuple(tuple(F(caps[j][p])-y for p,y in enumerate(row)) for j,row in enumerate(system.expand(point)))
        if any(x.denominator != 1 for row in output for x in row):
            raise RuntimeError('integral intersection returned a fractional vertex')
        output = tuple(tuple(int(x) for x in row) for row in output)
        if any(not feasible(rank,row) for rank,row in zip(ranks,output)):
            raise RuntimeError('rounded counts violate an original resource')
        largest = max((self.values[j] for j in geometry.light),default=F(0))
        for p in range(self.q):
            before = sum((self.values[j]*fractional[h][p] for h,j in enumerate(geometry.light)),F(0))
            after = sum((self.values[j]*output[h][p] for h,j in enumerate(geometry.light)),F(0))
            if after < before-largest:
                raise RuntimeError('joint lower rounding inequality failed')
        return output

    def realize(self,geometry,light_basis,target):
        original,heavy = self.completion(geometry,light_basis)
        if not light_basis:
            counts = [[0]*self.q for _ in self.ranks]
            for p,j in heavy: counts[j][p] += 1
            answer = Allocation(original,tuple(tuple(row) for row in counts))
            if not self.verify(answer):
                raise RuntimeError('pure-heavy recovery violated original input')
            return answer
        fractional = self.fractional(geometry,light_basis,target)
        light = self.round_light(geometry,fractional)
        counts = [[0]*self.q for _ in self.ranks]
        for j,row in zip(geometry.light,light):
            for p in original: counts[j][p] = row[p]
        for p,j in heavy: counts[j][p] += 1
        answer = Allocation(original,tuple(tuple(row) for row in counts))
        if not self.verify(answer):
            raise RuntimeError('realization violated original input')
        largest = max((self.values[j] for j in geometry.light),default=F(0))
        if any(sum((self.values[j]*counts[j][p] for j in range(len(counts))),F(0)) < target-largest for p in light_basis):
            raise RuntimeError('largest-light lower rounding bound failed')
        return answer

    def light_optimum(self,geometry,light_basis):
        if not light_basis:
            raise ValueError('nonempty light basis required')
        selected = mask_of(light_basis,self.q)
        return min(sum((self.values[j]*self.ranks[j][s] for j in geometry.light),F(0))
                   / (s & selected).bit_count() for s in range(1 << self.q) if s & selected)

    def near(self,epsilon,budget,fallback=None):
        epsilon = weighted.rational(epsilon)
        if not 0 < epsilon < 1 or type(budget) is not int or budget < 0:
            raise ValueError('positive accuracy and nonnegative corank budget required')
        best = self.zero()
        if not self.rank:
            return best
        trace = dict(processed=0,skipped=0,pure_heavy=0,gap_calls=0,gap_nodes=0)
        quantum = F(1,lcm(*(self.values[j].denominator for j in self.active)))
        for geometry in self.splits():
            if not geometry.rank:
                candidate = self.realize(geometry,(),0)
                trace['pure_heavy'] += 1
            elif geometry.corank > budget:
                trace['skipped'] += 1
                continue
            else:
                trace['processed'] += 1
                ground = frozenset(geometry.nonloops)
                forced = tuple(p for p in range(self.q) if p not in ground)
                def prepare(allowed):
                    mask = mask_of(allowed,self.q)
                    if geometry.player[mask] < geometry.rank:
                        return None
                    return prefix.Choice(members(greedy_basis(geometry.player,mask),self.q))
                rows = tuple(prefix.Row(tuple(int(s >> p & 1) for p in range(self.q)),
                                       sum((self.values[j]*self.ranks[j][s] for j in geometry.light),F(0)))
                             for s in range(1 << self.q))
                separate = prefix.explicit_separator(rows,self.q)
                initial = prepare(ground)
                def oracle(target):
                    counts = {}
                    result = prefix.gap(self.q,geometry.rank,target,(1-epsilon)*target,prepare,separate,forced,counts=counts)
                    trace['gap_calls'] += 1
                    trace['gap_nodes'] += counts.get('nodes',0)
                    return None if result is None else result.choice
                upper = sum((self.values[j]*self.ranks[j][-1] for j in geometry.light),F(0))
                optimum = prefix.rational_optimize(1-epsilon,max(1,self.q*quantum.denominator),upper,initial,oracle,
                                                  lambda choice:(self.light_optimum(geometry,choice.selected),None))
                candidate = self.realize(geometry,optimum.choice.selected,optimum.value)
            if self.minimum(candidate) > self.minimum(best): best = candidate
        if fallback is not None:
            candidate = fallback(self)
            if not self.verify(candidate):
                raise ValueError('fallback returned an invalid original allocation')
            if self.minimum(candidate) > self.minimum(best): best = candidate
        self.last_trace = trace
        return best

    def exact_two(self,budget,fallback=None):
        if type(budget) is not int or budget < 0:
            raise ValueError('nonnegative derived-corank budget required')
        best = self.zero()
        if not self.rank:
            return best
        for geometry in self.splits():
            if not geometry.rank:
                candidates = ((),)
            elif geometry.corank > budget:
                continue
            else:
                candidates = (tuple(p for p in geometry.nonloops if p not in omitted)
                              for omitted in combinations(geometry.nonloops,geometry.corank))
            for light in candidates:
                mask = mask_of(light,self.q)
                if geometry.player[mask] != geometry.rank:
                    continue
                target = self.light_optimum(geometry,light) if light else F(0)
                candidate = self.realize(geometry,light,target)
                if self.minimum(candidate) > self.minimum(best): best = candidate
        if fallback is not None:
            candidate = fallback(self)
            if not self.verify(candidate):
                raise ValueError('invalid fallback allocation')
            if self.minimum(candidate) > self.minimum(best): best = candidate
        return best
