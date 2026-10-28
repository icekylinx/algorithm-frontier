"""Exact explicit-table scheduling baseline.

Attribution: icekylinx and GPT-6 Astra Pro. Apache-2.0.
Vertex, role and integer-count enumeration do not realize Theorem HT's time.
All numerical operations use integers or Fraction; no external LP is required.
"""
from dataclasses import dataclass
from fractions import Fraction as F
from itertools import combinations, product
from math import gcd, lcm


def exact(value):
    if type(value) not in (int, F):
        raise ValueError('use int or Fraction data')
    return F(value)


def dot(a, b):
    return sum((x*y for x, y in zip(a, b)), F(0))


def solve_square(rows):
    """Unique solution of square rational equalities, or None."""
    n = len(rows)
    a = [[F(v) for v in (*row, rhs)] for row, rhs in rows]
    for j in range(n):
        pivot = next((i for i in range(j, n) if a[i][j]), None)
        if pivot is None:
            return None
        a[j], a[pivot] = a[pivot], a[j]
        scale = a[j][j]
        a[j] = [v/scale for v in a[j]]
        for i in range(n):
            if i != j:
                scale = a[i][j]
                a[i] = [v-scale*w for v, w in zip(a[i], a[j])]
    return tuple(a[i][-1] for i in range(n))


def vertices(rows, dimension):
    """Enumerate vertices of a bounded inequality system a*x <= rhs."""
    rows = sorted(set((tuple(map(F, a)), F(b)) for a, b in rows))
    if dimension == 0:
        return [()] if all(b >= 0 for _, b in rows) else []
    result = set()
    for active in combinations(rows, dimension):
        x = solve_square(active)
        if x is not None and all(dot(a, x) <= b for a, b in rows):
            result.add(x)
    return sorted(result)


@dataclass(frozen=True)
class Instance:
    """Ranks by type/subset; times and costs by machine/type; None forbids."""
    ranks: tuple
    times: tuple
    costs: tuple
    budget: object

    def __post_init__(self):
        q, m = len(self.times), len(self.ranks)
        if q < 1 or len(self.costs) != q:
            raise ValueError('machine dimensions')
        if any(len(row) != m for row in (*self.times, *self.costs)):
            raise ValueError('type dimensions')
        if exact(self.budget) < 0:
            raise ValueError('negative budget')
        for row in self.costs:
            if any(exact(v) < 0 for v in row):
                raise ValueError('negative cost')
        for row in self.times:
            positive = set()
            for v in row:
                if v is not None:
                    if exact(v) < 0:
                        raise ValueError('negative time')
                    if v > 0:
                        positive.add(v)
            if len(positive) > 2:
                raise ValueError('more than two positive times on a machine')
        for rank in self.ranks:
            if (len(rank) != 1 << q or rank[0] != 0
                    or any(type(v) is not int or v < 0 for v in rank)):
                raise ValueError('normalized integral rank table required')
            for a in range(1 << q):
                for b in range(1 << q):
                    if a & b == a and rank[a] > rank[b]:
                        raise ValueError('nonmonotone rank')
                    if rank[a]+rank[b] < rank[a | b]+rank[a & b]:
                        raise ValueError('nonsubmodular rank')


class Backend:
    def __init__(self, instance):
        self.instance = instance
        self.q, self.m = len(instance.times), len(instance.ranks)
        self.totals = tuple(r[-1] for r in instance.ranks)
        self.dimension = self.m*(self.q-1)
        self.size = self.q*self.m

    def coefficient(self, pairs):
        a = [F(0)]*self.size
        for p, j, value in pairs:
            a[p*self.m+j] += value
        return tuple(a)

    def reduce(self, a, rhs):
        # x(last,j)=n_j-sum_{p<last}x(p,j), never a masked total.
        last = (self.q-1)*self.m
        c = sum((a[last+j]*self.totals[j] for j in range(self.m)), F(0))
        return (tuple(a[p*self.m+j]-a[last+j]
                      for j in range(self.m) for p in range(self.q-1)), F(rhs)-c)

    def expand(self, x):
        return tuple(x[j*(self.q-1)+p] if p < self.q-1
                     else self.totals[j]-sum(x[j*(self.q-1):(j+1)*(self.q-1)])
                     for p in range(self.q) for j in range(self.m))

    def cost(self, x):
        return sum((self.instance.costs[p][j]*x[p*self.m+j]
                    for p in range(self.q) for j in range(self.m)), F(0))

    def load(self, x):
        return max((sum((self.instance.times[p][j]*x[p*self.m+j]
                         for j in range(self.m)
                         if self.instance.times[p][j] is not None), F(0))
                    for p in range(self.q)), default=F(0))

    def resource_rows(self, allowed):
        rows = []
        for p in range(self.q):
            for j in range(self.m):
                a = self.coefficient([(p, j, 1)])
                rows.append(self.reduce(tuple(-v for v in a), 0))
                if (p, j) not in allowed:
                    rows.append(self.reduce(a, 0))
        for j, rank in enumerate(self.instance.ranks):
            for mask, rhs in enumerate(rank):
                a = self.coefficient((p, j, 1) for p in range(self.q) if mask >> p & 1)
                rows.append(self.reduce(a, rhs))
        return rows

    def integers(self, rows):
        # Numeric ranges are intentional: this is a finite baseline, not bit-polynomial.
        ranges = [range(n+1) for n in self.totals for _ in range(self.q-1)]
        for x in product(*ranges):
            if all(dot(a, x) <= rhs for a, rhs in rows):
                yield self.expand(x)

    def minimum_integer(self, rows):
        return min(self.integers(rows), key=lambda x: (self.cost(x), x), default=None)

    def classify(self, target, d):
        classes = []
        for row in self.instance.times:
            values = sorted({F(v) for v in row if v is not None and 0 < v <= target})
            if not values:
                classes.append(('empty',))
            elif len(values) == 1:
                classes.append(('single', values[0], target//values[0]))
            else:
                u, a = values
                cap = target//u
                quota = cap-(target-a)//u
                if a <= F(d-1, d)*target:
                    classes.append(('easy', u, a))
                elif quota <= d:
                    classes.append(('small', u, a, cap, quota))
                else:
                    classes.append(('role', u, a, cap, quota, -(-quota//d)))
        return tuple(classes)

    def node(self, target, d, selected, weak=True, budget=True):
        """Return original-resource and machine rows for X_Q or its weak query."""
        classes = self.classify(target, d)
        allowed = {(p, j) for p, row in enumerate(self.instance.times)
                   for j, v in enumerate(row) if v is not None and v <= target
                   and not (classes[p][0] == 'role' and p not in selected and v == classes[p][2])}
        rows = self.resource_rows(allowed)
        machine = []
        for p, group in enumerate(classes):
            kind = group[0]
            positive = [(p, j, 1) for j, v in enumerate(self.instance.times[p])
                        if (p, j) in allowed and v > 0]
            if kind == 'single':
                machine.append((self.coefficient(positive), group[2]))
            elif kind == 'easy':
                machine.append((self.coefficient((p, j, self.instance.times[p][j])
                                                 for _, j, _ in positive), target))
            elif kind in ('small', 'role'):
                large = [(p, j, 1) for _, j, _ in positive if self.instance.times[p][j] == group[2]]
                machine.append((self.coefficient(large), 1))
                if kind == 'small':
                    machine.append((self.coefficient(positive), group[3]))
                else:
                    small = [(p, j, 1) for _, j, _ in positive if self.instance.times[p][j] == group[1]]
                    cap = group[3]-(group[5] if weak and p in selected else 0)
                    machine.append((self.coefficient(small), cap))
        rows += [self.reduce(a, b) for a, b in machine]
        if budget:
            a = self.coefficient((p, j, self.instance.costs[p][j])
                                 for p in range(self.q) for j in range(self.m))
            rows.append(self.reduce(a, self.instance.budget))
        return rows, classes, allowed

    def recover(self, target, d, selected, witness):
        rows, classes, allowed = self.node(target, d, selected, budget=False)
        # Replace each easy weighted-load row by integer upper-prefix caps.
        for p, group in enumerate(classes):
            if group[0] != 'easy':
                continue
            old = self.reduce(self.coefficient((p, j, self.instance.times[p][j])
                              for j in range(self.m) if (p, j) in allowed
                              and self.instance.times[p][j] > 0), target)
            rows.remove(old)
            order = sorted((j for j in range(self.m) if (p, j) in allowed
                            and self.instance.times[p][j] > 0),
                           key=lambda j: (-self.instance.times[p][j], j))
            for h in range(1, len(order)+1):
                prefix = order[:h]
                count = sum((witness[p*self.m+j] for j in prefix), F(0))
                rows.append(self.reduce(self.coefficient((p, j, 1) for j in prefix), -(-count//1)))
        output = self.minimum_integer(rows)
        if output is None or self.cost(output) > self.cost(witness):
            raise AssertionError('joint integral recovery failed')
        if self.load(output) > F(2*d-1, d)*target:
            raise AssertionError('load guarantee failed')
        return output

    def separator(self, target, d, selected):
        """Exact normalized nonnegative support row, or None for membership.

        An empty X_Q raises ValueError; it is a separate feasibility gate.
        """
        target = exact(target)
        selected = sorted(selected)
        rows, classes, _ = self.node(target, d, selected, weak=False)
        points = vertices(rows, self.dimension)
        if not points:
            raise ValueError('empty X_Q')
        if not selected:
            return None
        if any(classes[p][0] != 'role' for p in selected):
            raise ValueError('selected coordinates must be role machines')
        spare = []
        for point in points:
            x = self.expand(point)
            spare.append(tuple(classes[p][3]-sum((x[p*self.m+j]
                         for j in range(self.m) if self.instance.times[p][j] == classes[p][1]), F(0))
                         for p in selected))
        h = len(selected)
        # Variables are lambda[0:h-1], W; lambda[-1]=1-sum(lambda[:-1]).
        outer = []
        for i in range(h-1):
            a = [F(0)]*h
            a[i] = -1
            outer.append((tuple(a), 0))
        outer.append((tuple([F(1)]*(h-1)+[F(0)]), 1))
        outer.append((tuple([F(0)]*(h-1)+[F(-1)]), 0))
        outer.append((tuple([F(0)]*(h-1)+[F(1)]), max(classes[p][3] for p in selected)))
        for v in spare:
            outer.append((tuple([s-v[-1] for s in v[:-1]]+[F(-1)]), -v[-1]))
        b = [classes[p][5] for p in selected]
        objective = tuple([v-b[-1] for v in b[:-1]]+[F(-1)])
        opt = max(vertices(outer, h), key=lambda v: dot(objective, v))
        if b[-1]+dot(objective, opt) <= 0:
            return None
        normal = tuple(opt[:-1])+(1-sum(opt[:-1]),)
        return normal, opt[-1]

    def target(self, target, d=2):
        target = exact(target)
        if type(d) is not int or d < 2 or target < 0:
            raise ValueError('nonnegative target and integer d >= 2 required')
        if target == 0:
            allowed = {(p, j) for p, row in enumerate(self.instance.times)
                       for j, v in enumerate(row) if v == 0}
            output = self.minimum_integer(self.resource_rows(allowed))
            return output if output is not None and self.cost(output) <= self.instance.budget else None
        roles = [p for p, c in enumerate(self.classify(target, d)) if c[0] == 'role']
        for mask in range(1 << len(roles)):
            selected = {p for i, p in enumerate(roles) if mask >> i & 1}
            rows, _, _ = self.node(target, d, selected)
            points = vertices(rows, self.dimension)
            if points:
                return self.recover(target, d, selected, self.expand(points[0]))
        return None

    def optimize(self, d=2):
        if type(d) is not int or d < 2:
            raise ValueError('integer d >= 2 required')
        allowed = {(p, j) for p, row in enumerate(self.instance.times)
                   for j, v in enumerate(row) if v is not None}
        saved = self.minimum_integer(self.resource_rows(allowed))
        if saved is None or self.cost(saved) > self.instance.budget:
            return None
        zero = self.target(0, d)
        if zero is not None:
            return zero
        values = [F(v) for row in self.instance.times for v in row if v is not None and v > 0]
        denominator = lcm(*(v.denominator for v in values))
        grid = F(gcd(*(int(v*denominator) for v in values)), denominator)
        low, high = 0, int(self.load(saved)/grid)
        while high-low > 1:
            mid = (high+low)//2
            output = self.target(mid*grid, d)
            if output is None:
                low = mid
            else:
                high, saved = mid, output
        return saved
