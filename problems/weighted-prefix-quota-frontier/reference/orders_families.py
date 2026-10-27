"""Exact two-order and variable-family mixed prefix quota clients.

Copyright 2026 Yilin Liu. Authored by GPT-6 Astra Pro. Apache-2.0.
Both clients reuse original-subset resource recovery from prefix.py. Family
chains and occupied profiles are streamed, without resource-unit expansion.
"""
from dataclasses import dataclass
from fractions import Fraction as F
from itertools import permutations, product
from prefix import Prefix, Solution, recover_original, occupied


@dataclass(frozen=True)
class Plan:
    copies: tuple  # (original owner, marking label); owner n denotes disposal
    classes: tuple  # (charged positive mass, complete row column, copy indices)
    zero: tuple
    cap: int
    chain: tuple = ()


def _plan(copies, columns, masses, colors, cap, chain=()):
    groups, zero = {}, []
    for i, (column, mass, color) in enumerate(zip(columns, masses, colors)):
        if not any(column): zero.append(i)
        else:
            if mass <= 0: raise RuntimeError('nonzero column requires positive charged mass')
            groups.setdefault((color, mass, column), []).append(i)
    classes = tuple((mass, column, tuple(group)) for (_, mass, column), group in sorted(groups.items()))
    return Plan(tuple(copies), classes, tuple(zero), cap, tuple(chain))


class _Profiles:
    def _initialize(self, rank, costs, rows, mandatory, allowed, maximize, count):
        rank = tuple(rank)
        n = len(rank).bit_length()-1
        base = Prefix(rank, (0,)*max(0, n), costs, mandatory=mandatory, allowed=allowed, maximize=maximize)
        self.n, self.rank, self.costs = base.n, base.rank, base.costs
        self.allowed, self.total = base.allowed, base.total
        self.mandatory, self.maximize = base.mandatory, base.maximize
        self.rows = tuple(tuple(row) for row in rows)
        if any(len(row) != 4 or type(row[0]) is not int or not 0 <= row[0] < count
               or type(row[1]) is not int or not 0 <= row[1] <= self.n
               or row[2] not in ('<=', '=', '>=') or type(row[3]) is not int or row[3] < 0
               for row in self.rows):
            raise ValueError('original order/family index, prefix length, relation and target required')
        self.bound = max((b for _, _, _, b in self.rows), default=0)
        self.last_trace = {}

    def _prepare(self, count):
        uppers, lowers = [dict() for _ in range(count)], [dict() for _ in range(count)]
        for index, endpoint, relation, target in self.rows:
            if relation in ('<=', '='):
                upper = uppers[index]; upper[endpoint] = min(upper.get(endpoint, target), target)
            if relation in ('>=', '='):
                lower = lowers[index]; lower[endpoint] = max(lower.get(endpoint, target), target)
        self.impossible = any(lower.get(0, 0) > 0 for lower in lowers)
        self.eligible = tuple(e for e in range(self.n) if e in self.allowed and self.rank[1 << e]
                              and not any(e in self._order(i)[:end] and self._weights(i)[e] > target
                                          for i, upper in enumerate(uppers) for end, target in upper.items()))
        if self.mandatory and self.rank[sum(1 << e for e in self.eligible)] < self.total:
            self.impossible = True
        prepared = []
        self.cover = []
        for i, (upper, lower) in enumerate(zip(uppers, lowers)):
            kept, best = [], None
            for end in sorted(upper, reverse=True):
                target = upper[end]
                if target > 0 and (best is None or target < best): kept.append((i, end, '<=', target))
                best = target if best is None else min(best, target)
            prepared.extend(reversed(kept))
            best = 0
            for end in sorted(lower):
                if lower[end] > best:
                    prepared.append((i, end, '>=', lower[end])); best = lower[end]
            self.cover.append(best)
        self.cover = tuple(self.cover)
        self.prepared = tuple(prepared)
        self.prefixes = tuple(frozenset(self._order(i)[:end]) for i, end, _, _ in self.prepared)

    def profiles(self, plan):
        if not plan.classes or not plan.cap:
            yield (0,)*len(plan.classes)
            return
        yield from occupied.profile_counts(tuple(F(mass, plan.cap) for mass, _, _ in plan.classes), self.total)

    def _filter(self, plan, profile):
        for j, (_, _, relation, target) in enumerate(self.prepared):
            value = sum(column[j]*h for (_, column, _), h in zip(plan.classes, profile))
            if (relation == '<=' and value > target) or (relation == '>=' and value < target): return False
        return True

    def realize(self, plan, profile):
        """Internal exact recovery for a plan emitted by this instance."""
        profile = tuple(profile)
        if (len(profile) != len(plan.classes) or any(type(h) is not int or h < 0 for h in profile)
                or sum(profile) > self.total
                or sum(mass*h for (mass, _, _), h in zip(plan.classes, profile)) > plan.cap):
            raise ValueError('valid original-count/mass profile required')
        if not self._filter(plan, profile): return None
        x = recover_original(self.rank, tuple(e for e, _ in plan.copies),
                             tuple(group for _, _, group in plan.classes)+(plan.zero,),
                             profile+(self.total-sum(profile),), self.costs, self.maximize)
        if x is None: return None
        result = [0]*self.n
        for (e, _), h in zip(plan.copies, x):
            if e < self.n: result[e] += h
        result = tuple(result)
        answer = Solution(result, sum((c*h for c, h in zip(self.costs, result)), F(0)))
        if not self.verify(answer): raise RuntimeError('profile failed original multi-prefix verification')
        return answer

    def verify(self, solution):
        try:
            if (type(solution) is not Solution or type(solution.counts) is not tuple
                    or len(solution.counts) != self.n or type(solution.cost) not in (int, F)):
                return False
            x = solution.counts
            if any(type(h) is not int or h < 0 or (e not in self.allowed and h) for e, h in enumerate(x)): return False
            if self.mandatory and sum(x) != self.total: return False
            if any(sum(x[e] for e in range(self.n) if s >> e & 1) > b for s, b in enumerate(self.rank)): return False
            for index, end, relation, target in self.rows:
                value = sum(self._weights(index)[e]*x[e] for e in self._order(index)[:end])
                if (relation in ('<=', '=') and value > target) or (relation in ('>=', '=') and value < target): return False
            return solution.cost == sum((c*h for c, h in zip(self.costs, x)), F(0))
        except (AttributeError, TypeError, ValueError, IndexError):
            return False

    def solve(self):
        self.last_trace = dict(plans=0, profiles=0, row_rejections=0, empty_faces=0, recovered=0,
                               max_copies=0, max_classes=0)
        best = None
        for plan in self.plans():
            self.last_trace['plans'] += 1
            self.last_trace['max_copies'] = max(self.last_trace['max_copies'], len(plan.copies))
            self.last_trace['max_classes'] = max(self.last_trace['max_classes'], len(plan.classes))
            for profile in self.profiles(plan):
                self.last_trace['profiles'] += 1
                if not self._filter(plan, profile):
                    self.last_trace['row_rejections'] += 1; continue
                answer = self.realize(plan, profile)
                if answer is None:
                    self.last_trace['empty_faces'] += 1; continue
                self.last_trace['recovered'] += 1
                if best is None or (answer.cost > best.cost if self.maximize else answer.cost < best.cost): best = answer
        return best


class TwoOrders(_Profiles):
    def __init__(self, rank, weights, costs, orders, rows=(), mandatory=True, allowed=None, maximize=False):
        self.weights = tuple(weights)
        self.orders = tuple(tuple(order) for order in orders)
        self._initialize(rank, costs, rows, mandatory, allowed, maximize, 2)
        if (len(self.weights) != self.n or any(type(w) is not int or w < 0 for w in self.weights)
                or len(self.orders) != 2
                or any(any(type(e) is not int for e in order) or sorted(order) != list(range(self.n)) for order in self.orders)):
            raise ValueError('two original coordinate orders and one common integer weight vector required')
        self._prepare(2)

    def _order(self, i): return self.orders[i]
    def _weights(self, i): return self.weights

    def plans(self):
        if self.impossible: return
        copies, columns, masses = [], [], []
        for e in self.eligible:
            for bits in product(*((0, 1) if self.weights[e] and c else (0,) for c in self.cover)):
                weight = min(self.weights[e], self.bound)
                column = tuple(weight if e in members and (rel == '<=' or bits[i]) else 0
                               for (i, _, rel, _), members in zip(self.prepared, self.prefixes))
                copies.append((e, bits)); columns.append(column); masses.append(weight if any(column) else 0)
        if not self.mandatory:
            copies.append((self.n, (0, 0))); columns.append((0,)*len(self.prepared)); masses.append(0)
        cap = sum(self.bound+max(c-1, 0) for i, c in enumerate(self.cover)
                  if any(j == i for j, _, _, _ in self.prepared))
        yield _plan(copies, columns, masses, (0,)*len(copies), cap)


class Families(_Profiles):
    def __init__(self, rank, weights, costs, rows=(), mandatory=True, allowed=None, maximize=False):
        self.weights = tuple(tuple(row) for row in weights)
        self._initialize(rank, costs, rows, mandatory, allowed, maximize, len(self.weights))
        if any(len(row) != self.n or any(type(w) is not int or w < 0 for w in row) for row in self.weights):
            raise ValueError('explicit common-order nonnegative integer weight families required')
        self._prepare(len(self.weights))

    def _order(self, i): return tuple(range(self.n))
    def _weights(self, i): return self.weights[i]

    def plans(self):
        if self.impossible: return
        covering = tuple(i for i, c in enumerate(self.cover) if c)
        endpoints = tuple(sorted({end for _, end, _, _ in self.prepared}))
        for chain in permutations(covering):
            copies, columns, masses, colors = [], [], [], []
            for e in self.eligible:
                segment = sum(end <= e for end in endpoints)
                for layer in range(len(chain)+1):
                    active = frozenset(chain[layer:])
                    template = tuple(e in members and (rel == '<=' or i in active)
                                     for (i, _, rel, _), members in zip(self.prepared, self.prefixes))
                    collapsed = tuple(min(weight[e], self.bound)
                                      if any(on and index == i for on, (index, _, _, _) in zip(template, self.prepared)) else 0
                                      for i, weight in enumerate(self.weights))
                    column = tuple(collapsed[i] if on else 0 for on, (i, _, _, _) in zip(template, self.prepared))
                    copies.append((e, layer)); columns.append(column); masses.append(sum(collapsed)); colors.append((layer, segment))
            if not self.mandatory:
                copies.append((self.n, 0)); columns.append((0,)*len(self.prepared)); masses.append(0); colors.append((-1, -1))
            yield _plan(copies, columns, masses, colors, len(self.weights)*max(0, 2*self.bound-1), chain)
