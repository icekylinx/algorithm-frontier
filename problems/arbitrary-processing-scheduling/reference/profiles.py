"""Exact occupied-profile client for arbitrary processing times.

Attribution: icekylinx and GPT-6 Astra Pro. Apache-2.0.
Reuses the canonical two-time table/LP/count primitives. Profile generation
is streamed; the inherited vertex/count solver has separate enumeration costs.
"""
from dataclasses import dataclass
from fractions import Fraction as F
from pathlib import Path
import importlib.util
import sys

_name = '_algorithm_frontier_two_time_scheduling'
if _name not in sys.modules:
    _path = Path(__file__).resolve().parents[2] / 'two-time-scheduling/reference/scheduling.py'
    _spec = importlib.util.spec_from_file_location(_name, _path)
    _module = importlib.util.module_from_spec(_spec)
    sys.modules[_name] = _module
    _spec.loader.exec_module(_module)
shared = sys.modules[_name]


@dataclass(frozen=True)
class Instance:
    ranks: tuple
    times: tuple
    costs: tuple
    budget: object

    def __post_init__(self):
        # Only the validation proxy has zero times. Backend receives the real
        # times below; the canonical two-time model is not broadened silently.
        proxy = tuple(tuple(None if v is None else 0 for v in row) for row in self.times)
        shared.Instance(self.ranks, proxy, self.costs, self.budget)
        for row in self.times:
            for value in row:
                if value is not None and shared.exact(value) < 0:
                    raise ValueError('nonnegative exact processing times required')


@dataclass(frozen=True)
class Plan:
    allowed: frozenset
    counts: tuple  # (tuple of machine/type coordinates, integer cap)
    loads: tuple   # (tuple of machine/type coordinates, fractional load cap)


def bin_index(time, target, delta):
    time, target, delta = map(shared.exact, (time, target, delta))
    if not (target > 0 and 0 < delta <= F(1, 2) and delta*target < time <= target):
        raise ValueError('big time in (delta*T,T] required')
    return -(-((time/target-delta)/(delta*delta))//1)-1


def profile_counts(lower_endpoints, count_cap):
    """Stream exactly sum h<=K, sum lambda*h<=1, without an accuracy table."""
    lower = tuple(map(shared.exact, lower_endpoints))
    if type(count_cap) is not int or count_cap < 0 or any(v <= 0 or v > 1 for v in lower):
        raise ValueError('nonnegative count cap and positive endpoints <=1 required')
    current = [0]*len(lower)
    if not lower:
        yield ()
        return

    def frame(i, used, load):
        return [i, used, load, 0, min(count_cap-used, (1-load)//lower[i])]

    # One frame per occupied coordinate, without Python call-stack dependence.
    stack = [frame(0, 0, F(0))]
    while stack:
        state = stack[-1]
        i, used, load, value, maximum = state
        if value > maximum:
            stack.pop()
            continue
        state[3] += 1
        current[i] = value
        if i+1 == len(lower):
            yield tuple(current)
        else:
            stack.append(frame(i+1, used+value, load+value*lower[i]))


class JointBackend(shared.Backend):
    """Original-total joint LP and one minimum-cost integer recovery."""

    def __init__(self, instance):
        instance = Instance(instance.ranks, instance.times, instance.costs, instance.budget)
        super().__init__(instance)

    def validate_plan(self, plan):
        seen = set()
        for coordinates, cap in (*plan.counts, *plan.loads):
            if shared.exact(cap) < 0 or len(coordinates) != len(set(coordinates)):
                raise ValueError('nonnegative caps and disjoint coordinates required')
            if coordinates and len({p for p, _ in coordinates}) != 1:
                raise ValueError('each machine group belongs to one machine')
            for p, j in coordinates:
                if (type(p) is not int or type(j) is not int
                        or not 0 <= p < self.q or not 0 <= j < self.m
                        or self.instance.times[p][j] is None or (p, j) in seen):
                    raise ValueError('invalid or overlapping machine groups')
                seen.add((p, j))
        if seen != set(plan.allowed) or any(type(cap) is not int for _, cap in plan.counts):
            raise ValueError('groups must partition allowed pairs with integral count caps')

    def fixed_vertices(self, plan):
        self.validate_plan(plan)
        rows = self.resource_rows(plan.allowed)
        rows += [self.reduce(self.coefficient((p, j, 1) for p, j in group), cap)
                 for group, cap in plan.counts]
        rows += [self.reduce(self.coefficient((p, j, self.instance.times[p][j])
                                              for p, j in group), cap)
                 for group, cap in plan.loads]
        a = self.coefficient((p, j, self.instance.costs[p][j])
                             for p in range(self.q) for j in range(self.m))
        rows.append(self.reduce(a, self.instance.budget))
        return shared.vertices(rows, self.dimension)

    def recover(self, plan, witness):
        self.validate_plan(plan)
        rows = self.resource_rows(plan.allowed)
        rows += [self.reduce(self.coefficient((p, j, 1) for p, j in group), cap)
                 for group, cap in plan.counts]
        for group, _ in plan.loads:
            order = sorted(group, key=lambda pair: (-self.instance.times[pair[0]][pair[1]], pair))
            for h in range(1, len(order)+1):
                prefix = order[:h]
                value = sum((witness[p*self.m+j] for p, j in prefix), F(0))
                rows.append(self.reduce(self.coefficient((p, j, 1) for p, j in prefix), -(-value//1)))
        output = self.minimum_integer(rows)
        if output is None or self.cost(output) > self.cost(witness):
            raise AssertionError('joint minimum-cost recovery failed')
        return output

    def try_plans(self, target, plans, factor):
        self.last_plans = 0
        for plan in plans:
            self.last_plans += 1
            points = self.fixed_vertices(plan)
            if points:
                output = self.recover(plan, self.expand(points[0]))
                if self.load(output) > factor*target or self.cost(output) > self.instance.budget:
                    raise AssertionError('recovered schedule violates target contract')
                return output
        return None

    def optimize(self):
        # The canonical search only uses sound failure, saved actual upper
        # outputs and the original load grid. Its factor is supplied by target.
        return shared.Backend.optimize(self, 2)


class ProfileBackend(JointBackend):
    def __init__(self, instance, epsilon):
        self.epsilon = shared.exact(epsilon)
        if not 0 < self.epsilon <= 1:
            raise ValueError('rational 0 < epsilon <= 1 required')
        self.delta = self.epsilon/2
        self.count_cap = 1//self.delta
        self.bin_count = -(-((1-self.delta)/(self.delta*self.delta))//1)
        super().__init__(instance)

    def grouping(self, target):
        target = shared.exact(target)
        if target <= 0:
            raise ValueError('positive target required')
        machines = []
        for p, row in enumerate(self.instance.times):
            small, bins = [], {}
            for j, value in enumerate(row):
                if value is None or value > target:
                    continue
                if value <= self.delta*target:
                    small.append((p, j))
                else:
                    index = bin_index(value, target, self.delta)
                    bins.setdefault(index, []).append((p, j))
            machines.append((tuple(small), tuple((i, tuple(bins[i])) for i in sorted(bins))))
        return tuple(machines)

    def plans(self, target):
        machines = self.grouping(target)
        allowed = frozenset(pair for small, bins in machines
                            for group in (small, *(group for _, group in bins)) for pair in group)
        counts, loads = [], []
        lower = tuple(tuple(self.delta+i*self.delta*self.delta for i, _ in bins)
                      for _, bins in machines)

        def frame(p):
            return p, iter(profile_counts(lower[p], self.count_cap)), len(counts), len(loads)

        # Paused machine iterators are explicit frames, not recursive generators.
        stack = [frame(0)]
        while stack:
            p, iterator, count_start, load_start = stack[-1]
            del counts[count_start:]
            del loads[load_start:]
            try:
                vector = next(iterator)
            except StopIteration:
                stack.pop()
                continue
            small, bins = machines[p]
            value = sum((v*c for v, c in zip(lower[p], vector)), F(0))
            counts.extend((group, cap) for (_, group), cap in zip(bins, vector))
            loads.append((small, (1-value)*target))
            if p+1 == self.q:
                yield Plan(allowed, tuple(counts), tuple(loads))
            else:
                stack.append(frame(p+1))

    def target(self, target, _search_dispatch=2):
        target = shared.exact(target)
        if target < 0:
            raise ValueError('nonnegative target required')
        if target == 0:
            return shared.Backend.target(self, 0, 2)
        return self.try_plans(target, self.plans(target), 1+self.epsilon)
