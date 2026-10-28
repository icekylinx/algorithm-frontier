"""Native binary workload decomposition and per-machine upper rounding.

Attribution: icekylinx and GPT-6 Astra Pro. Apache-2.0.
Generic mandatory-base LP primitives are imported from the intrinsic reference;
its allocation, disposal and lower-rounding interfaces are not used. Streamed
active-system and selected-basis enumeration costs remain explicit.
"""
from dataclasses import dataclass
from fractions import Fraction as F
from itertools import combinations
from math import lcm
from pathlib import Path
import importlib.util
import sys


def load(name, relative):
    if name not in sys.modules:
        spec = importlib.util.spec_from_file_location(name, Path(__file__).resolve().parents[2] / relative)
        module = importlib.util.module_from_spec(spec)
        sys.modules[name] = module
        spec.loader.exec_module(module)
    return sys.modules[name]


linear = load('_many_workload_intrinsic', 'intrinsic-values-near-two/reference/intrinsic.py')
tables = load('_many_workload_counts', 'recipient-polymatroid/reference/counts.py')
corank = load('_many_workload_corank', 'two-size-scheduling/reference/corank.py')


def exact(value):
    if type(value) not in (int, F):
        raise ValueError('use exact int or Fraction data')
    return F(value)


def validated(ranks, q):
    if type(q) is not int or q < 0:
        raise ValueError('nonnegative explicit physical-machine count required')
    return tuple(tables.RankTable(q, tuple(row)).values for row in ranks)


def base(rank, vector):
    return (len(rank) == 1 << len(vector) and all(exact(x) >= 0 for x in vector)
            and sum(vector, F(0)) == rank[-1] and linear.feasible(rank, vector))


def decompose(ranks, multipliers, workload):
    """Return integer bases of multiplier[j]*rank[j] summing to workload.

    One variable per original machine/type coordinate; no multiplier copies.
    """
    workload, multipliers = tuple(workload), tuple(multipliers)
    q = len(workload)
    ranks = validated(ranks, q)
    if (len(ranks) != len(multipliers) or any(type(v) is not int or v < 1 for v in multipliers)
            or any(type(v) is not int or v < 0 for v in workload)):
        raise ValueError('positive binary multipliers and nonnegative integer workload required')
    aggregate = tuple(sum(multiplier*rank[s] for rank, multiplier in zip(ranks, multipliers))
                      for s in range(1 << q))
    if not base(aggregate, workload):
        raise ValueError('workload is not an aggregate base')
    scaled = tuple(tuple(multiplier*v for v in rank) for rank, multiplier in zip(ranks, multipliers))
    system = linear.BaseLP(scaled, q)
    rows = system.rows()
    for p, cap in enumerate(workload):
        rows.append(system.reduce(((j, p, 1) for j in range(len(ranks))), cap))
    point = linear.vertex(rows, system.dimension)
    if point is None:
        raise RuntimeError('integral workload decomposition face is empty')
    output = system.expand(point)
    if any(x.denominator != 1 for row in output for x in row):
        raise RuntimeError('integral workload decomposition returned a fractional vertex')
    output = tuple(tuple(int(x) for x in row) for row in output)
    if (any(not base(rank, row) for rank, row in zip(scaled, output))
            or any(sum(row[p] for row in output) != workload[p] for p in range(q))):
        raise RuntimeError('decomposition lost an original component or machine total')
    return output


def upper_round(ranks, sizes, fractional, q):
    """Original mandatory bases with per-machine added load <= largest size."""
    ranks = validated(ranks, q)
    sizes = tuple(exact(value) for value in sizes)
    fractional = tuple(tuple(exact(x) for x in row) for row in fractional)
    if (len(ranks) != len(sizes) or len(ranks) != len(fractional) or any(v <= 0 for v in sizes)
            or any(len(row) != q or not base(rank, row) for rank, row in zip(ranks, fractional))):
        raise ValueError('positive common sizes and original fractional type bases required')
    active = tuple(j for j, rank in enumerate(ranks) if rank[-1])
    order = tuple(sorted(active, key=lambda j: (-sizes[j], j)))
    system = linear.BaseLP(ranks, q)
    rows = system.rows()
    for p in range(q):
        for h in range(1, len(order)+1):
            prefix = order[:h]
            total = sum((fractional[j][p] for j in prefix), F(0))
            rows.append(system.reduce(((j, p, 1) for j in prefix), -(-total//1)))
    point = linear.vertex(rows, system.dimension)
    if point is None:
        raise RuntimeError('joint upper-prefix face is empty')
    output = system.expand(point)
    if any(x.denominator != 1 for row in output for x in row):
        raise RuntimeError('integral upper-prefix face returned a fractional vertex')
    output = tuple(tuple(int(x) for x in row) for row in output)
    if any(not base(rank, row) for rank, row in zip(ranks, output)):
        raise RuntimeError('upper rounding lost an original type base')
    largest = max((sizes[j] for j in active), default=F(0))
    for p in range(q):
        before = sum((size*row[p] for size, row in zip(sizes, fractional)), F(0))
        after = sum((size*row[p] for size, row in zip(sizes, output)), F(0))
        if after > before+largest:
            raise RuntimeError('per-machine additive upper rounding bound failed')
    return output


@dataclass(frozen=True)
class State:
    quantum: F
    cap: int
    multipliers: tuple
    workload: tuple
    boxed: tuple
    dual: tuple
    full_quota: int


@dataclass(frozen=True)
class Outcome:
    counts: tuple | None
    failure: str | None = None  # 'infeasible' or 'cap'; only cap changes benchmark


class WorkloadBackend:
    def __init__(self, q, ranks, sizes, eta=F(1)):
        self.ranks = validated(ranks, q)
        self.q = q
        self.sizes = tuple(exact(value) for value in sizes)
        self.eta = exact(eta)
        if len(self.ranks) != len(self.sizes) or any(v <= 0 for v in self.sizes) or not 0 < self.eta <= 1:
            raise ValueError('positive common sizes and rational 0 < eta <= 1 required')
        self.active = tuple(j for j, rank in enumerate(self.ranks) if rank[-1])
        self.a = max((self.sizes[j] for j in self.active), default=F(0))
        self.big = tuple(j for j in self.active if self.sizes[j] == self.a)
        self.small = tuple(j for j in self.active if self.sizes[j] < self.a)
        self.u = max((self.sizes[j] for j in self.small), default=F(0))
        self.large = tuple(sum(self.ranks[j][s] for j in self.big) for s in range(1 << q))
        self.h = self.large[-1]
        self.player = corank.box_rank(self.large, 1)
        self.grid = F(1, lcm(*(value.denominator for value in self.sizes)))
        self.refinement = -(-(F(18)/self.eta)//1)
        self.quantum = self.grid/self.refinement
        self.alpha = 2-1/(3+self.eta)
        self.last_trace = {}

    def verify(self, counts):
        try:
            return (type(counts) is tuple and len(counts) == len(self.ranks)
                    and all(type(row) is tuple and len(row) == self.q
                            and all(type(x) is int and x >= 0 for x in row) and base(rank, row)
                            for rank, row in zip(self.ranks, counts)))
        except (TypeError, ValueError, IndexError):
            return False

    def load(self, counts):
        if not self.verify(counts):
            raise ValueError('original integer job bases required')
        return max((sum((size*row[p] for size, row in zip(self.sizes, counts)), F(0))
                    for p in range(self.q)), default=F(0))

    def initial(self):
        return tuple(corank.complete_base(rank, (0,)*self.q) for rank in self.ranks)

    def fractional_target(self, target):
        """Original all-job relaxation followed by joint upper rounding."""
        system = linear.BaseLP(self.ranks, self.q)
        rows = system.rows()
        for p in range(self.q):
            rows.append(system.reduce(((j, p, self.sizes[j]) for j in range(len(self.ranks))), target))
        point = linear.vertex(rows, system.dimension)
        return None if point is None else upper_round(self.ranks, self.sizes, system.expand(point), self.q)

    def state(self, target, quantum):
        """Fixed full-machine workload dual; None is original rank failure."""
        target, quantum = exact(target), exact(quantum)
        if target < 0 or quantum <= 0 or (target/quantum).denominator != 1 or (self.a/quantum).denominator != 1:
            raise ValueError('positive common quantum dividing target and largest size required')
        if self.player[-1] != self.h:
            return None
        ratios = tuple(self.sizes[j]/quantum for j in self.small)
        if any(value.denominator != 1 for value in ratios):
            raise ValueError('quantum must divide every smaller size')
        multipliers = tuple(int(value) for value in ratios)
        workload = tuple(sum(multiplier*self.ranks[j][s] for j, multiplier in zip(self.small, multipliers))
                         for s in range(1 << self.q))
        cap = int(target/quantum)
        boxed = corank.box_rank(workload, cap)
        if boxed[-1] != workload[-1]:
            return None
        full = (1 << self.q)-1
        dual = tuple(cap*s.bit_count()+boxed[full ^ s]-workload[-1] for s in range(1 << self.q))
        return State(quantum, cap, multipliers, workload, boxed, dual, int(self.a/quantum))

    def select(self, state, quota, committed=()):
        """Finite complete-table weak-basis selector; not the rank-local search."""
        committed = tuple(committed)
        if (type(quota) is not int or quota < 1 or len(set(committed)) != len(committed)
                or any(type(p) is not int or not 0 <= p < self.q for p in committed)):
            raise ValueError('positive integer quota and distinct committed original IDs required')
        fixed = sum(1 << p for p in committed)
        if self.player[fixed] != len(committed):
            raise ValueError('committed player set must be independent')
        if self.player[-1] != self.h:
            return None
        allowed = tuple(p for p in range(self.q) if p not in committed)
        self.last_trace['candidate_bases'] = 0
        for residual in combinations(allowed, self.h-len(committed)):
            self.last_trace['candidate_bases'] += 1
            selected = fixed | sum(1 << p for p in residual)
            if self.player[selected] != self.h:
                continue
            lower = tuple(quota if p in residual else 0 for p in range(self.q))
            if linear.feasible(state.dual, lower):
                return residual
        return None

    def reconstruct(self, state, lower, large_counts):
        """Generic reconstruction also usable when committed players get no quota."""
        lower, large_counts = tuple(lower), tuple(large_counts)
        if (len(lower) != self.q or len(large_counts) != self.q
                or any(type(x) is not int for x in (*lower, *large_counts))
                or not base(self.large, large_counts)):
            raise ValueError('original large base and integral full-machine lower vector required')
        y = corank.complete_base(state.dual, lower)
        workload = tuple(state.cap-v for v in y)
        scaled = decompose(tuple(self.ranks[j] for j in self.small), state.multipliers, workload)
        fractional = tuple(tuple(F(value, multiplier) for value in row)
                           for row, multiplier in zip(scaled, state.multipliers))
        small = upper_round(tuple(self.ranks[j] for j in self.small),
                            tuple(self.sizes[j] for j in self.small), fractional, self.q)
        big = decompose(tuple(self.ranks[j] for j in self.big), (1,)*len(self.big), large_counts)
        result = [(0,)*self.q for _ in self.ranks]
        for j, row in zip(self.small, small): result[j] = row
        for j, row in zip(self.big, big): result[j] = row
        result = tuple(result)
        if not self.verify(result):
            raise RuntimeError('workload reconstruction lost an original job base')
        self.last_trace.update(workload=workload, fractional_small=fractional,
                               rounded_small=small, dual_base=y)
        return result

    def threshold(self, budget, divisor):
        divisor = self.private_parameters(budget, divisor)
        if self.player[-1] < self.h:
            return 2*self.a
        if budget >= self.h:
            return self.a
        values = tuple(sum((self.sizes[j]*self.ranks[j][1 << p] for j in self.small), F(0))
                       for p in range(self.q))
        for value in sorted(set(values)):
            subset = sum(1 << p for p in range(self.q) if values[p] <= value)
            if self.player[subset] >= self.h-budget:
                return min(2*self.a, max(self.a, value+self.a/divisor))
        raise RuntimeError('private bottleneck rank threshold was not attained')

    @staticmethod
    def private_parameters(budget, divisor):
        divisor = exact(divisor)
        if type(budget) is not int or budget < 1 or divisor < 3-F(2, budget):
            raise ValueError('integer budget >=1 and divisor >=3-2/budget required')
        return divisor

    def target(self, target, *, budget=None, divisor=None):
        target = exact(target)
        if target < 0:
            raise ValueError('nonnegative target required')
        private = budget is not None or divisor is not None
        if private:
            if budget is None or divisor is None:
                raise ValueError('supply both private rank budget and divisor')
            divisor = self.private_parameters(budget, divisor)
            quantum = self.grid/divisor.numerator
        else:
            quantum = self.quantum
        target = (target//quantum)*quantum
        self.last_trace = dict(branch='empty', quantum=quantum, candidate_bases=0)
        if not self.active:
            return Outcome(self.initial())
        if not self.small:
            self.last_trace['branch'] = 'one-size'
            boxed = corank.box_rank(self.large, target//self.a)
            if boxed[-1] != self.h:
                return Outcome(None, 'infeasible')
            largest = corank.complete_base(boxed, (0,)*self.q)
            big = decompose(tuple(self.ranks[j] for j in self.big), (1,)*len(self.big), largest)
            result = [(0,)*self.q for _ in self.ranks]
            for j, row in zip(self.big, big): result[j] = row
            return Outcome(tuple(result))
        if target < self.a:
            self.last_trace['branch'] = 'below-largest'
            return Outcome(None, 'infeasible')
        if target >= 2*self.a:
            self.last_trace['branch'] = 'fractional-upper'
            result = self.fractional_target(target)
            return Outcome(result, None if result is not None else 'infeasible')
        state = self.state(target, quantum)
        if state is None:
            self.last_trace['branch'] = 'rank-loss'
            return Outcome(None, 'infeasible')
        committed = ()
        if private:
            quota = int(F(state.full_quota)/divisor)
            values = tuple(sum((self.sizes[j]*self.ranks[j][1 << p] for j in self.small), F(0))
                           for p in range(self.q))
            fixed = 0
            for p in range(self.q):
                if values[p] <= target-self.a/divisor and self.player[fixed | (1 << p)] > self.player[fixed]:
                    fixed |= 1 << p
            committed = tuple(p for p in range(self.q) if fixed >> p & 1)
            if self.h-len(committed) > budget:
                self.last_trace['branch'] = 'private-cap'
                return Outcome(None, 'cap')
        else:
            quota = -(-(F(state.full_quota)/(3+self.eta))//1)
        self.last_trace.update(branch='workload', full_quota=state.full_quota,
                               weak_quota=quota, committed=committed, state=state)
        selected = self.select(state, quota, committed)
        if selected is None:
            return Outcome(None, 'infeasible')
        recipients = frozenset((*committed, *selected))
        lower = tuple(quota if p in recipients else 0 for p in range(self.q))
        largest = tuple(int(p in recipients) for p in range(self.q))
        result = self.reconstruct(state, lower, largest)
        factor = max(F(3, 2), 2-1/divisor) if private else self.alpha
        if self.load(result) > factor*target+self.u:
            raise RuntimeError('workload approximation lost its additive-term ledger')
        return Outcome(result)

    def _search(self, decision, quantum, upper):
        saved = self.initial()
        low, high = 0, int(upper/quantum)
        while high-low > 1:
            mid = (high+low)//2
            outcome = decision(mid*quantum)
            if outcome.counts is None:
                low = mid
            else:
                high, saved = mid, outcome.counts
        return saved

    def fallback(self):
        if not self.active:
            return self.initial()
        def decision(target):
            output = self.fractional_target(target)
            return Outcome(output, None if output is not None else 'infeasible')
        return self._search(decision, self.grid, self.load(self.initial()))

    def optimize(self, *, budget=None, divisor=None, with_fallback=True):
        if not self.active:
            return self.initial()
        private = budget is not None or divisor is not None
        if private:
            if budget is None or divisor is None:
                raise ValueError('supply both private rank budget and divisor')
            divisor = self.private_parameters(budget, divisor)
        quantum = self.grid/divisor.numerator if private else self.grid
        upper = max(self.load(self.initial()), 2*self.a) if private else self.load(self.initial())
        result = self._search(lambda target: self.target(target, budget=budget, divisor=divisor), quantum, upper)
        if with_fallback:
            candidate = self.fallback()
            if self.load(candidate) < self.load(result): result = candidate
        return result
