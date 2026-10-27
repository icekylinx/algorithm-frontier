"""Exact-table activation adapter with original totals and one shared budget.

Attribution: Yilin Liu and GPT-6 Astra Pro. Apache-2.0.
Setup and binary greedy feasibility are exact. Positive-target recovery reuses
canonical scheduling LP/count primitives with their finite enumeration costs.
"""
from dataclasses import dataclass
from fractions import Fraction as F
from itertools import combinations, product
from math import gcd, lcm
from pathlib import Path
import importlib.util
import sys


def _load(name, relative):
    if name not in sys.modules:
        path = Path(__file__).resolve().parents[2] / relative
        spec = importlib.util.spec_from_file_location(name, path)
        module = importlib.util.module_from_spec(spec)
        sys.modules[name] = module
        spec.loader.exec_module(module)
    return sys.modules[name]


core = _load('_algorithm_frontier_general_processing_profiles',
             'arbitrary-processing-scheduling/reference/profiles.py')
buckets = _load('_algorithm_frontier_processing_buckets',
                'processing-bucket-tradeoff/reference/buckets.py')
Instance = core.Instance

# (big intervals, small fractional-load cap), normalized by the target.
SIX = (
    (((F(1, 2), F(3, 4)),), F(1, 2)),
    (((F(3, 4), F(1)),), F(1, 4)),
    (((F(1, 4), F(3, 8)), (F(1, 2), F(5, 8))), F(1, 4)),
    (((F(1, 4), F(3, 8)), (F(5, 8), F(3, 4))), F(1, 8)),
    (((F(3, 8), F(1, 2)), (F(1, 2), F(5, 8))), F(1, 8)),
)


class SixBackend(core.JointBackend):
    """Actual six-profile client on the original nonactivated scheduling model."""
    factor = F(3, 2)

    def plan(self, target, labels):
        target = core.shared.exact(target)
        labels = tuple(labels)
        if (target <= 0 or len(labels) != self.q
                or any(type(i) is not int or not 0 <= i < 6 for i in labels)):
            raise ValueError('positive target and one six-profile label per machine required')
        allowed, counts, loads = set(), [], []
        for p, label in enumerate(labels):
            groups = () if label == 0 else SIX[label-1][0]
            small_cap = F(1) if label == 0 else SIX[label-1][1]
            small_limit = F(1, 2) if label == 0 else F(1, 4)
            small, big = [], [[] for _ in groups]
            for j, value in enumerate(self.instance.times[p]):
                if value is None:
                    continue
                if value <= small_limit*target:
                    small.append((p, j))
                else:
                    for i, (lo, hi) in enumerate(groups):
                        if lo*target < value <= hi*target:
                            big[i].append((p, j))
                            break
            allowed.update(small)
            for group in big:
                allowed.update(group)
                counts.append((tuple(group), 1))
            loads.append((tuple(small), small_cap*target))
        return core.Plan(frozenset(allowed), tuple(counts), tuple(loads))

    def plans(self, target):
        for labels in product(range(6), repeat=self.q):
            yield self.plan(target, labels)

    def target(self, target, _search_dispatch=2):
        target = core.shared.exact(target)
        if target < 0:
            raise ValueError('nonnegative target required')
        if target == 0:
            return core.shared.Backend.target(self, 0, 2)
        return self.try_plans(target, self.plans(target), self.factor)


@dataclass(frozen=True)
class ActivatedResult:
    basis: tuple
    counts: tuple  # original physical-machine/type order, including inactive zeros


class ActivatedBackend:
    def __init__(self, jobs, activation_rank, setup, method='profiles', epsilon=F(1, 2), depth=1):
        self.jobs = Instance(jobs.ranks, jobs.times, jobs.costs, jobs.budget)
        self.q, self.m = len(self.jobs.times), len(self.jobs.ranks)
        self.activation_rank = tuple(activation_rank)
        Instance((self.activation_rank,), ((0,),)*self.q, ((0,),)*self.q, 0)
        if any(self.activation_rank[1 << p] > 1 for p in range(self.q)):
            raise ValueError('activation table must be an ordinary matroid rank')
        self.rank = self.activation_rank[-1]
        self.setup = tuple(core.shared.exact(v) for v in setup)
        if len(self.setup) != self.q or any(v < 0 for v in self.setup):
            raise ValueError('one nonnegative exact setup fee per original machine required')
        self.method, self.epsilon, self.depth = method, core.shared.exact(epsilon), depth
        if method not in ('profiles', 'six', 'buckets'):
            raise ValueError('unknown scheduling method')
        if method == 'profiles' and not 0 < self.epsilon <= 1:
            raise ValueError('rational 0 < epsilon <= 1 required')
        if method == 'buckets' and (type(depth) is not int or depth < 0):
            raise ValueError('nonnegative integer bucket depth required')
        self.factor = (1+self.epsilon if method == 'profiles' else F(3, 2) if method == 'six'
                       else F(3*(1 << depth)-1, (1 << (depth+1))-1))
        self.last_active_sizes = ()
        self.last_solver_calls = 0

    def bases(self):
        for basis in combinations(range(self.q), self.rank):
            mask = sum(1 << p for p in basis)
            if self.activation_rank[mask] == self.rank:
                yield basis

    def cost(self, result):
        return sum((self.setup[p] for p in result.basis), F(0)) + sum(
            (self.jobs.costs[p][j]*result.counts[p*self.m+j]
             for p in range(self.q) for j in range(self.m)), F(0))

    def load(self, result):
        return max((sum((self.jobs.times[p][j]*result.counts[p*self.m+j]
                         for j in range(self.m) if self.jobs.times[p][j] is not None), F(0))
                    for p in range(self.q)), default=F(0))

    def restricted(self, basis, zero_only=False):
        """Internal restriction on a validated genuine original activation basis."""
        basis = tuple(basis)
        if (len(basis) != self.rank or len(set(basis)) != len(basis)
                or any(type(p) is not int or not 0 <= p < self.q for p in basis)
                or self.activation_rank[sum(1 << p for p in basis)] != self.rank):
            raise ValueError('a genuine original activation basis is required')
        fee = sum((self.setup[p] for p in basis), F(0))
        if fee > self.jobs.budget:
            return None
        masks = tuple(sum(1 << p for i, p in enumerate(basis) if s >> i & 1)
                      for s in range(1 << len(basis)))
        tables = []
        for j, rank in enumerate(self.jobs.ranks):
            eligible = sum(1 << p for p in basis if self.jobs.times[p][j] is not None
                           and (not zero_only or self.jobs.times[p][j] == 0))
            # This comparison precedes constructing a restricted full-rank field.
            if rank[eligible] != rank[-1]:
                return None
            tables.append(tuple(rank[mask & eligible] for mask in masks))
        if not basis:
            return None  # rank zero is handled before requesting a q>=1 solver
        times = tuple(tuple(value if not zero_only or value == 0 else None
                            for value in self.jobs.times[p]) for p in basis)
        return Instance(tuple(tables), times, tuple(self.jobs.costs[p] for p in basis),
                        self.jobs.budget-fee)

    @staticmethod
    def minimum_assignment(instance):
        """Internal binary greedy on valid retained-rank, already-masked tables."""
        q, m = len(instance.times), len(instance.ranks)
        if any(instance.times[p][j] is None and rank[1 << p] != 0
               for j, rank in enumerate(instance.ranks) for p in range(q)):
            raise ValueError('ineligible coordinates must already be rank loops')
        output = [0]*(q*m)
        for j, rank in enumerate(instance.ranks):
            prefix = 0
            for p in sorted(range(q), key=lambda p: (instance.costs[p][j], p)):
                enlarged = prefix | (1 << p)
                output[p*m+j] = rank[enlarged]-rank[prefix]
                prefix = enlarged
        cost = sum((instance.costs[p][j]*output[p*m+j] for p in range(q) for j in range(m)), F(0))
        return tuple(output), cost

    def extend(self, basis, local):
        output = [0]*(self.q*self.m)
        for i, p in enumerate(basis):
            output[p*self.m:(p+1)*self.m] = local[i*self.m:(i+1)*self.m]
        return ActivatedResult(tuple(basis), tuple(output))

    def feasible(self, zero_only=False):
        if not self.rank:
            return (ActivatedResult((), (0,)*(self.q*self.m))
                    if all(rank[-1] == 0 for rank in self.jobs.ranks) else None)
        for basis in self.bases():
            instance = self.restricted(basis, zero_only)
            if instance is None:
                continue
            local, cost = self.minimum_assignment(instance)
            if cost <= instance.budget:
                return self.extend(basis, local)
        return None

    def make_solver(self, instance):
        if self.method == 'profiles':
            return core.ProfileBackend(instance, self.epsilon)
        if self.method == 'buckets':
            return buckets.BucketBackend(instance, self.depth)
        return SixBackend(instance)

    def target(self, target):
        target = core.shared.exact(target)
        if target < 0:
            raise ValueError('nonnegative target required')
        self.last_active_sizes = ()
        self.last_solver_calls = 0
        if target == 0 or not self.rank:
            return self.feasible(zero_only=(target == 0))
        for basis in self.bases():
            instance = self.restricted(basis)
            if instance is None:
                continue
            _, cost = self.minimum_assignment(instance)
            if cost > instance.budget:
                continue
            solver = self.make_solver(instance)
            self.last_solver_calls += 1
            self.last_active_sizes = (solver.q,)
            local = solver.target(target)
            if local is not None:
                result = self.extend(basis, local)
                if self.cost(result) > self.jobs.budget or self.load(result) > self.factor*target:
                    raise AssertionError('activated target contract violated')
                return result
        return None

    def optimize(self):
        saved = self.feasible()
        if saved is None or self.load(saved) == 0:
            return saved
        zero = self.target(0)
        if zero is not None:
            return zero
        values = [F(v) for row in self.jobs.times for v in row if v is not None and v > 0]
        denominator = lcm(*(v.denominator for v in values))
        grid = F(gcd(*(int(v*denominator) for v in values)), denominator)
        low, high = 0, int(self.load(saved)/grid)
        while high-low > 1:
            mid = (high+low)//2
            result = self.target(mid*grid)
            if result is None:
                low = mid
            else:
                high, saved = mid, result
        return saved
