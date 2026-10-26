#!/usr/bin/env python3
"""Independent finite checks for dominant-weight laminar recovery."""
from __future__ import annotations

from collections import Counter
from fractions import Fraction
from itertools import combinations, product
from pathlib import Path
import json
import random
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / 'matroid-failure-summaries' / 'verify'))
from check_summaries import all_matroid_rank_tables


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def bits(mask):
    while mask:
        bit = mask & -mask
        yield bit.bit_length() - 1
        mask ^= bit


def total_on(mask, values):
    return sum(values[e] for e in bits(mask))


class CountSystem:
    """Compressed interval extension and grouped-copy greedy rank oracle."""
    def __init__(self, caps, rows, total):
        self.caps = tuple(caps)
        self.n = len(caps)
        self.total = total
        self.root = (1 << self.n) - 1
        self.rows = dict(rows)
        self.invalid = total < 0
        if 0 in self.rows:
            lo, hi = self.rows.pop(0)
            self.invalid |= not lo <= 0 <= hi
        for e, cap in enumerate(caps):
            node = 1 << e
            lo, hi = self.rows.get(node, (0, cap))
            self.rows[node] = (lo, min(hi, cap))
        lo, hi = self.rows.get(self.root, (0, sum(caps)))
        self.rows[self.root] = (max(lo, total), min(hi, total))
        self.nodes = tuple(sorted(self.rows, key=int.bit_count))
        require(all(not a & b or a & ~b == 0 or b & ~a == 0
                    for a in self.nodes for b in self.nodes), 'count rows are laminar')
        self.children = {
            node: tuple(child for child in self.nodes
                        if child != node and child & ~node == 0
                        and not any(middle not in (child, node)
                                    and child & ~middle == 0 and middle & ~node == 0
                                    for middle in self.nodes))
            for node in self.nodes
        }
        self.extension_cache = {}
        self.rank_cache = {}

    def extends(self, forced):
        forced = tuple(forced)
        if forced in self.extension_cache:
            return self.extension_cache[forced]
        if self.invalid or any(value < 0 or value > cap for value, cap in zip(forced, self.caps)):
            self.extension_cache[forced] = False
            return False
        intervals = {}
        for node in self.nodes:
            if node.bit_count() == 1:
                e = node.bit_length() - 1
                low, high = forced[e], self.caps[e]
            else:
                low = sum(intervals[child][0] for child in self.children[node])
                high = sum(intervals[child][1] for child in self.children[node])
            low = max(low, self.rows[node][0])
            high = min(high, self.rows[node][1])
            if low > high:
                self.extension_cache[forced] = False
                return False
            intervals[node] = (low, high)
        self.extension_cache[forced] = True
        return True

    def rank(self, subset):
        if subset in self.rank_cache:
            return self.rank_cache[subset]
        require(self.extends((0,) * self.n), 'rank oracle requires a nonempty base family')
        forced = [0] * self.n
        for e in bits(subset):
            low, high = 0, min(self.caps[e], self.total)
            while low < high:
                middle = (low + high + 1) // 2
                forced[e] = middle
                if self.extends(forced):
                    low = middle
                else:
                    high = middle - 1
            forced[e] = low
        answer = sum(forced)
        self.rank_cache[subset] = answer
        return answer


def check_count_bases():
    counts = Counter()
    checked_families = set()
    configurations = [
        ((1,), ()),
        ((1, 1), ()),
        *(( (1, 1, 1), internal) for internal in ((), (3,), (5,), (6,))),
        *(( (1, 1, 1, 1), internal) for internal in ((), (3,), (7,), (3, 7), (3, 12))),
        *((caps, (3,)) for caps in ((2, 1, 2), (2, 2, 2), (0, 2, 1))),
    ]
    for caps, internal in configurations:
        n = len(caps)
        root = (1 << n) - 1
        nodes = tuple(sorted(({1 << e for e in range(n)} | set(internal)) - {root}))
        intervals = [tuple((lo, hi) for lo in range(total_on(node, caps) + 1)
                           for hi in range(lo, total_on(node, caps) + 1)) for node in nodes]
        vectors = tuple(product(*(range(cap + 1) for cap in caps)))
        for bounds in product(*intervals):
            rows = dict(zip(nodes, bounds))
            for target in range(sum(caps) + 1):
                system = CountSystem(caps, rows, target)
                bases = tuple(vector for vector in vectors
                              if sum(vector) == target and all(lo <= total_on(node, vector) <= hi
                                                              for node, (lo, hi) in rows.items()))
                for forced in vectors:
                    reference = any(all(a <= b for a, b in zip(forced, base)) for base in bases)
                    require(system.extends(forced) == reference, 'interval extension matches literal bases')
                    counts['extension_comparisons'] += 1
                counts['count_systems'] += 1
                if not bases:
                    counts['empty_count_systems'] += 1
                    continue
                ranks = tuple(system.rank(subset) for subset in range(1 << n))
                for subset, actual in enumerate(ranks):
                    expected = max(total_on(subset, base) for base in bases)
                    require(actual == expected, 'binary grouped-copy rank equals literal maximum')
                    counts['rank_comparisons'] += 1
                for vector in vectors:
                    inequalities = sum(vector) == target and all(total_on(subset, vector) <= ranks[subset]
                                                                for subset in range(1 << n))
                    require(inequalities == (vector in bases), 'coordinate-rank bases equal literal count bases')
                    counts['rank_base_comparisons'] += 1
                signature = (caps, bases)
                if signature in checked_families:
                    continue
                checked_families.add(signature)
                for left in range(1 << n):
                    for right in range(1 << n):
                        require(ranks[left] + ranks[right] >= ranks[left & right] + ranks[left | right],
                                'coordinate rank is submodular')
                        counts['rank_submodularity_comparisons'] += 1
                # Expand only this finite fixture, never the algorithm. Check
                # ordinary basis exchange on all distinguishable unit copies.
                owners = tuple(e for e, cap in enumerate(caps) for _ in range(cap))
                clone_bases = set()
                for mask in range(1 << len(owners)):
                    vector = tuple(sum(owners[item] == e for item in bits(mask)) for e in range(n))
                    if vector in bases:
                        clone_bases.add(mask)
                for left in clone_bases:
                    for right in clone_bases:
                        for e in bits(left & ~right):
                            require(any(((left ^ (1 << e)) | (1 << f)) in clone_bases
                                        for f in bits(right & ~left)), 'ordinary unit-copy basis exchange')
                            counts['ordinary_basis_exchange_conditions'] += 1
    counts['distinct_nonempty_base_families'] = len(checked_families)
    return dict(counts)


def check_binary_large_rank():
    caps = (1 << 40, 1 << 40, 1 << 45, 1 << 45)
    first_total, second_total = (1 << 40) + 3, (1 << 45) + 7
    total = first_total + second_total
    rows = {3: (first_total, first_total), 12: (second_total, second_total)}
    system = CountSystem(caps, rows, total)
    require(system.extends((0, 0, 0, 0)), 'large binary count face is nonempty')
    for subset in range(16):
        expected = min(first_total, total_on(subset & 3, caps)) + min(second_total, total_on(subset & 12, caps))
        require(system.rank(subset) == expected, 'large binary rank has independent partition formula')
    require(not system.extends((caps[0], caps[1], 0, 0)), 'large forced overflow is rejected')
    call_bound = 1 + 16 * len(caps) * (max(caps).bit_length() + 1)
    require(len(system.extension_cache) <= call_bound, 'rank access uses logarithmic searches, not unit expansion')
    return {'rank_comparisons': 16, 'largest_capacity_bits': max(caps).bit_length(),
            'total_bits': total.bit_length(), 'distinct_interval_queries': len(system.extension_cache)}


def eta(weights):
    ordered = sorted(set(weights))
    return max((Fraction(i - 1, sum(ordered[:i])) for i in range(2, len(ordered) + 1)), default=Fraction(0))


def check_histograms():
    counts = Counter()
    for support_size in range(1, 7):
        for weights in combinations(range(1, 9), support_size):
            fraction = eta(weights)
            require(fraction <= Fraction(1, 3), 'universal exception fraction')
            for histogram in product(range(4), repeat=support_size):
                mass = sum(w * count for w, count in zip(weights, histogram))
                exceptions = sum(histogram) - max(histogram)
                require(3 * exceptions <= mass, 'dominant weight leaves at most B/3 exceptions')
                require(exceptions <= mass - sum(histogram), 'cardinality refines the exception count')
                require(exceptions <= fraction * mass, 'actual-weight exception fraction')
                counts['histograms'] += 1
                counts['sharp_one_third_histograms'] += exceptions > 0 and 3 * exceptions == mass
                counts['sharp_actual_weight_histograms'] += exceptions > 0 and exceptions == fraction * mass
    return dict(counts)


def check_cardinality_accounting():
    counts = Counter()
    for budget in range(1, 121):
        for depth in range(budget + 1):
            for cardinality in range(1, budget + 1):
                exceptions = min(budget // 3, budget - cardinality)
                exponent = 2 * (depth + cardinality - 1) * exceptions
                require(9 * exponent <= 6 * budget * depth + 4 * budget * budget,
                        'depth-aware ten-ninths accounting')
                require(9 * exponent <= 10 * budget * budget,
                        'universal ten-ninths coefficient')
                counts['cardinality_depth_comparisons'] += 1
    for budget in range(1, 71):
        for fraction in (Fraction(0), Fraction(1, 3), Fraction(1, 4), Fraction(1, 5),
                         Fraction(2, 7), Fraction(2, 9), Fraction(3, 11)):
            exception_cap = int(fraction * budget)
            for depth in (0, 1, budget // 2, budget):
                for rows in sorted({depth, max(depth, 1), depth + budget // 2, depth + budget}):
                    exponents = [2 * min(rows, depth + cardinality - 1)
                                 * min(exception_cap, budget - cardinality)
                                 for cardinality in range(1, budget + 1)]
                    exact = max(exponents)
                    closed = (2 * exception_cap * min(rows, depth + budget - exception_cap - 1)
                              if exception_cap else 0)
                    require(exact == closed, 'exact integer maximum is at B minus exception cap')
                    continuous = 2 * fraction * budget * depth + 2 * fraction * (1 - fraction) * budget**2
                    require(exact <= continuous, 'actual-weight continuous bound dominates the integer maximum')
                    counts['actual_weight_maximum_comparisons'] += 1
    return dict(counts)


def resource_bases(values):
    n = (len(values) - 1).bit_length()
    caps = tuple(values[1 << e] for e in range(n))
    return tuple(vector for vector in product(*(range(cap + 1) for cap in caps))
                 if sum(vector) == values[-1]
                 and all(total_on(subset, vector) <= values[subset] for subset in range(1 << n)))


def recover_by_two_ranks(values, weights, costs, rows, budget, counts):
    n = len(weights)
    positive = tuple(e for e in range(n) if weights[e])
    zero = tuple(e for e in range(n) if not weights[e])
    owners = tuple(e for e in positive for _ in range(min(values[1 << e], budget // weights[e])))
    p = len(owners)
    mixed_owners = owners + zero
    mixed_size = len(mixed_owners)
    total = values[-1]
    resource = []
    for subset in range(1 << mixed_size):
        zero_mask = sum(1 << mixed_owners[e] for e in bits(subset) if e >= p)
        candidates = []
        for chosen in range(1 << len(positive)):
            coordinate_mask = sum(1 << positive[i] for i in bits(chosen))
            outside = sum(not coordinate_mask >> owners[e] & 1 for e in bits(subset & ((1 << p) - 1)))
            candidates.append(values[zero_mask | coordinate_mask] + outside)
        resource.append(min(candidates))
    occurring = tuple(sorted({weights[e] for e in owners}))
    exception_limit = int(eta(occurring) * budget)
    best = None
    best_vector = None
    # None is the separate zero-only case. The positive cases use all
    # original prepared copies as a valid superset of any catalogue.
    for chosen_weight in (None,) + occurring:
        other = tuple(i for i, owner in enumerate(owners) if weights[owner] != chosen_weight)
        exception_sets = ((),) if chosen_weight is None else (
            selected for size in range(min(exception_limit, len(other)) + 1)
            for selected in combinations(other, size)
        )
        for selected in exception_sets:
            fixed = sum(1 << item for item in selected)
            fixed_count = len(selected)
            if resource[fixed] != fixed_count or fixed_count > total:
                continue
            remaining_positive = tuple(i for i, owner in enumerate(owners)
                                       if weights[owner] == chosen_weight)
            indices = remaining_positive + tuple(range(p, mixed_size))
            remaining_total = total - fixed_count
            caps = (1,) * len(remaining_positive) + (remaining_total,) * len(zero)
            reduced_rows = {}
            invalid = False
            for original_set, (lower, upper) in rows.items():
                fixed_mass = sum(weights[owners[item]] for item in selected if original_set >> owners[item] & 1)
                if chosen_weight is None:
                    invalid |= not lower <= fixed_mass <= upper
                    continue
                lower_count = max(0, (lower - fixed_mass + chosen_weight - 1) // chosen_weight)
                upper_count = (upper - fixed_mass) // chosen_weight
                projection = sum(1 << new for new, old in enumerate(remaining_positive)
                                 if original_set >> owners[old] & 1)
                old_lower, old_upper = reduced_rows.get(projection, (0, sum(caps)))
                reduced_rows[projection] = (max(lower_count, old_lower), min(upper_count, old_upper))
            if invalid:
                continue
            system = CountSystem(caps, reduced_rows, remaining_total)
            if not system.extends((0,) * len(indices)):
                counts['empty_homogeneous_count_faces'] += 1
                continue
            contracted = []
            count_rank = []
            for subset in range(1 << len(indices)):
                original_subset = fixed | sum(1 << indices[e] for e in bits(subset))
                contracted.append(resource[original_subset] - fixed_count)
                count_rank.append(system.rank(subset))
            counts['two_rank_recovery_models'] += 1
            if contracted[-1] < remaining_total:
                continue
            ranges = tuple(range(min(cap, contracted[1 << e]) + 1) for e, cap in enumerate(caps))
            for vector in product(*ranges):
                if sum(vector) != remaining_total:
                    continue
                intersection = all(total_on(subset, vector) <= min(contracted[subset], count_rank[subset])
                                   for subset in range(1 << len(indices)))
                counts['literal_two_rank_vectors'] += 1
                original = [0] * n
                for item in selected:
                    original[owners[item]] += 1
                for new, old in enumerate(indices):
                    original[mixed_owners[old]] += vector[new]
                literal = (sum(original) == total
                           and all(total_on(subset, original) <= values[subset] for subset in range(1 << n))
                           and all(lower <= sum(weights[e] * original[e] for e in bits(row)) <= upper
                                   for row, (lower, upper) in rows.items()))
                require(intersection == literal, 'two-rank face exactly equals original fixed-exception allocations')
                if intersection:
                    value = sum(c * x for c, x in zip(costs, original))
                    if best is None or value < best:
                        best, best_vector = value, tuple(original)
    return best, best_vector


def check_recovery():
    counts = Counter()
    matroids = list(all_matroid_rank_tables(4))
    rng = random.Random(20261026)
    for serial in range(600):
        first, second = rng.choice(matroids), rng.choice(matroids)
        values = tuple(a + b for a, b in zip(first, second))
        all_bases = resource_bases(values)
        require(all_bases, 'integer polymatroid fixture has a base')
        weights = (rng.randint(1, 3), rng.randint(1, 3), 0, 0)
        costs = tuple(rng.randint(-5, 5) for _ in range(4))
        if serial % 2:
            chosen = rng.choice(all_bases)
            mass = sum(w * x for w, x in zip(weights, chosen))
            budget = mass + rng.randrange(3)
        else:
            chosen = rng.choice(all_bases)
            budget = rng.randrange(9)
        topology = (1, 3, 15) if serial % 3 else (3, 12, 15)
        rows = {}
        for node in topology:
            if node == 15:
                rows[node] = (0, budget)
                continue
            if serial % 2:
                mass = sum(weights[e] * chosen[e] for e in bits(node))
                rows[node] = (max(0, mass - rng.randrange(3)), mass + rng.randrange(3))
            else:
                lower = rng.randrange(budget + 2)
                upper = rng.randrange(budget + 2)
                rows[node] = (min(lower, upper), max(lower, upper))
        feasible = tuple(vector for vector in all_bases
                         if all(lower <= sum(weights[e] * vector[e] for e in bits(node)) <= upper
                                for node, (lower, upper) in rows.items()))
        reference = min((sum(c * x for c, x in zip(costs, vector)) for vector in feasible), default=None)
        actual, output = recover_by_two_ranks(values, weights, costs, rows, budget, counts)
        require(actual == reference, 'dominant-weight recovery preserves the exact signed optimum')
        require(output is None or output in feasible, 'recovered original allocation is feasible')
        counts['instances'] += 1
        counts['infeasible_instances'] += reference is None
        counts['nonuniform_zero_cost_instances'] += costs[2] != costs[3]
        counts['negative_zero_cost_instances'] += min(costs[2:]) < 0
        counts['zero_root_budget_instances'] += budget == 0
        counts['one_positive_weight_instances'] += weights[0] == weights[1]
    return dict(counts)


def main():
    require(__debug__, 'run without -O; mathematical assertions must be enabled')
    result = {'status':'passed', 'count_bases':check_count_bases(),
              'histograms':check_histograms(), 'cardinality_accounting':check_cardinality_accounting(), 'binary_large_rank':check_binary_large_rank(), 'recovery':check_recovery()}
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
