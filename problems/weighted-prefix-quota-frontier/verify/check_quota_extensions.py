#!/usr/bin/env python3
"""Independent checks of projected coloring, histogram accounting and compatible-cut quotas."""
from collections import Counter
from fractions import Fraction
from itertools import combinations, product
import json
import random


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def bits(mask):
    while mask:
        bit = mask & -mask
        yield bit.bit_length() - 1
        mask ^= bit


def mass(mask, weights):
    return sum(weights[e] for e in bits(mask))


def prepare_upper(weights, rows):
    active = sum(1 << e for e in range(len(weights))
                 if all(not node >> e & 1 or weights[e] <= upper for node, upper in rows.items()))
    merged = {}
    for node, upper in rows.items():
        projected = node & active
        if projected:
            merged[projected] = min(upper, merged.get(projected, upper))
    retained = {node: upper for node, upper in merged.items()
                if not any(node != ancestor and node & ~ancestor == 0 and cap <= upper
                           for ancestor, cap in merged.items())}
    return active, retained


def depth(nodes, ground):
    return max((sum(bool(node >> e & 1) for node in nodes) for e in bits(ground)), default=0)


def check_certificates():
    rng = random.Random(2026102603)
    counts = Counter()
    families = ((1, 3, 7, 15), (3, 12, 15), (1, 3, 7, 15, 31, 63),
                (3, 7, 24, 56, 63), (3, 12, 48, 63))
    for serial in range(1500):
        topology = families[serial % len(families)]
        n = max(topology).bit_length()
        full = (1 << n) - 1
        weights = tuple(rng.randrange(1, 5) for _ in range(n))
        budget = rng.randrange(1, 11)
        original = {node: (budget if node == full else rng.randrange(1, budget + 1))
                    for node in topology}
        lower_nodes = tuple(node for node in topology if rng.randrange(2))
        active, upper = prepare_upper(weights, original)
        original_depth = depth(upper, active)
        require(original_depth <= budget, 'prepared upper depth is bounded by the root cap')
        for chosen in range(1 << n):
            literal = all(mass(chosen & node, weights) <= cap for node, cap in original.items())
            prepared = not chosen & ~active and all(mass(chosen & node, weights) <= cap for node, cap in upper.items())
            require(literal == prepared, 'preparation preserves every original upper-feasible set')
            counts['upper_preparation_comparisons'] += 1
            if not literal:
                continue
            counts['feasible_sets'] += 1
            for protected in bits(chosen):
                w = weights[protected]
                pool_class = sum(1 << f for f in bits(active) if weights[f] == w
                                 and all(bool(node >> f & 1) == bool(node >> protected & 1)
                                         for node in lower_nodes))
                projections = {node & pool_class for node in upper} - {0}
                local_depth = depth(projections, pool_class)
                require(local_depth <= original_depth and len(projections) <= len(upper),
                        'projection only decreases depth and coloring IDs')
                counts['strict_depth_reductions'] += local_depth < original_depth
                counts['strict_identity_reductions'] += len(projections) < len(upper)
                reduced = chosen ^ (1 << protected)
                blockers = {node for node, cap in upper.items() if cap >= w and mass(reduced & node, weights) + w > cap}
                maximal = {node for node in blockers if not any(node != other and node & ~other == 0 for other in blockers)}
                require(all(not a & b for a, b in combinations(maximal, 2)), 'original maximal blockers are disjoint')
                red = {node & pool_class for node in maximal} - {0}
                green = {node & pool_class for node in upper if node >> protected & 1}
                require(red.isdisjoint(green), 'merged coloring identities have no conflicting prescriptions')
                require(all(not a & b for a, b in combinations(red, 2)), 'projected red blockers remain disjoint')
                require(len(green) <= local_depth and len(red) <= chosen.bit_count() - 1,
                        'projected certificate uses the claimed number of IDs')
                require(len(red | green) <= min(len(projections), local_depth + chosen.bit_count() - 1),
                        'full projected prescription bound')
                forbidden = 0
                for node in red:
                    forbidden |= node
                pool = pool_class & ~forbidden
                require(pool >> protected & 1, 'protected item remains in the colored pool')
                for replacement in bits(pool & ~reduced):
                    after = reduced | (1 << replacement)
                    require(all(mass(after & node, weights) <= cap for node, cap in original.items()),
                            'all projected-pool replacements satisfy every original upper row')
                    require(all(mass(after & node, weights) == mass(chosen & node, weights) for node in lower_nodes),
                            'all original lower totals remain exactly unchanged')
                    require(mass(after, weights) == mass(chosen, weights), 'root mass is unchanged')
                    counts['replacement_comparisons'] += 1
                counts['projected_certificates'] += 1
        counts['instances'] += 1
    return dict(counts)


def eta(weights):
    return max((Fraction(i - 1, sum(weights[:i])) for i in range(2, len(weights) + 1)), default=Fraction(0))


def histograms(weights, budget):
    counts = [0] * len(weights)
    def visit(index, remaining):
        if index == len(weights):
            yield tuple(counts)
            return
        for amount in range(remaining // weights[index] + 1):
            counts[index] = amount
            yield from visit(index + 1, remaining - amount * weights[index])
        counts[index] = 0
    yield from visit(0, budget)


def check_histogram_profiles():
    counts = Counter()
    for budget in range(1, 13):
        for size in range(1, 5):
            for weights in combinations(range(1, min(6, budget) + 1), size):
                generated = tuple(histograms(weights, budget))
                independent = {histogram for histogram in product(*(range(budget // w + 1) for w in weights))
                               if sum(w * a for w, a in zip(weights, histogram)) <= budget}
                require(set(generated) == independent and len(generated) == len(independent),
                        'streaming histogram enumeration is complete without duplicates')
                require(len(generated) <= 2**budget, 'composition bound on histogram enumeration')
                fraction = eta(weights)
                for histogram in generated:
                    cardinality = sum(histogram)
                    if not cardinality:
                        continue
                    exception_cap = min(int(fraction * budget), budget - cardinality)
                    for difficulties in product(range(4), repeat=size):
                        total = sum(a * h for a, h in zip(histogram, difficulties))
                        saved = max(a * h for a, h in zip(histogram, difficulties))
                        profile = total - saved
                        global_depth = max(difficulties)
                        require(profile <= global_depth * exception_cap,
                                'weighted catalogue saving never worsens the scalar exception bound')
                        best_weight = max((i for i, amount in enumerate(histogram) if amount),
                                          key=lambda i: histogram[i] * difficulties[i])
                        explicit = sum(amount * h for i, (amount, h) in enumerate(zip(histogram, difficulties))
                                       if i != best_weight)
                        require(explicit == profile, 'chosen homogeneous weight attains the profile expression')
                        counts['weighted_histogram_profiles'] += 1
                counts['histogram_instances'] += 1
    return dict(counts)


def total_on(mask, values):
    return sum(values[e] for e in bits(mask))


def cross_free(left, right, full):
    return not left & right or left & ~right == 0 or right & ~left == 0 or left | right == full


def laminar(left, right):
    return not left & right or left & ~right == 0 or right & ~left == 0


def orient(rows, full, anchor, mass):
    answer = {}
    for node, (lower, upper) in rows.items():
        if node >> anchor & 1:
            node, lower, upper = full ^ node, mass - upper, mass - lower
        lower = max(0, lower)
        before_lower, before_upper = answer.get(node, (0, mass))
        answer[node] = max(before_lower, lower), min(before_upper, upper)
    return answer


def check_cross_free_orientation():
    rng = random.Random(2026102604)
    counts = Counter()
    for n in range(1, 5):
        full = (1 << n) - 1
        proper = tuple(range(1, full))
        incompatible = {(left, right) for left in proper for right in proper
                        if left < right and not cross_free(left, right, full)}
        for family_mask in range(1 << len(proper)):
            nodes = tuple(proper[i] for i in bits(family_mask))
            if any(left in nodes and right in nodes for left, right in incompatible):
                continue
            counts['cross_free_families'] += 1
            weights = tuple(rng.randrange(4) for _ in range(n))
            budget = rng.randrange(1, 8)
            rows = {node: tuple(sorted((rng.randrange(budget+1), rng.randrange(budget+1))))
                    for node in nodes}
            rows[full] = (0, budget)
            for anchor in range(n):
                projected = {full ^ node if node >> anchor & 1 else node for node in nodes}
                require(all(laminar(left, right) for left in projected for right in projected),
                        'anchored compatible cuts form a laminar family')
                counts['oriented_families'] += 1
                for mass in range(budget+1):
                    transformed = orient(rows, full, anchor, mass)
                    for vector in product(range(2), repeat=n):
                        values = tuple(w * x for w, x in zip(weights, vector))
                        literal = total_on(full, values) == mass and all(lower <= total_on(node, values) <= upper
                                                                     for node, (lower, upper) in rows.items())
                        mapped = total_on(full, values) == mass and all(lower <= total_on(node, values) <= upper
                                                                    for node, (lower, upper) in transformed.items())
                        require(literal == mapped, 'fixed-mass complement bounds preserve every numeric vector')
                        counts['numeric_equivalence_comparisons'] += 1
    return dict(counts)


def main():
    require(__debug__, 'run without -O; mathematical assertions must be enabled')
    print(json.dumps({'status': 'passed', 'projection': check_certificates(),
                      'histograms': check_histogram_profiles(),
                      'cross_free_orientation': check_cross_free_orientation()}, indent=2, sort_keys=True))

if __name__ == '__main__':
    main()
