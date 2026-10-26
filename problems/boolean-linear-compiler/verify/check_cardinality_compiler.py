#!/usr/bin/env python3
"""Exact checks of cardinality-conditioned and modal-normalized intervals.

Direct evaluation of original Boolean assignments is the reference.  The suite
checks the one-level rounding identity on actual frames, then independently
enumerates every packed assignment and projects to original item indices.
The separate exact-integer budget test includes budgets larger than the layer
slack count and time exponents above one.  No fast Subset Sum backend is run.
"""
from collections import Counter
from itertools import product
from math import prod
import json
import random
from check_interval_compiler import require, ceil_log2, subset_sums, slack_weights


def catalogue_fixed(row, lower, upper, k):
    n = len(row)
    require(0 <= k <= n, "cardinality range")
    if lower > upper:
        return [], []
    if not k or k == n:
        value = sum(row) if k else 0
        return ([(row, value, value)] if lower <= value <= upper else []), []
    support = sum(coefficient != 0 for coefficient in row)
    if not support:
        return ([(row, 0, 0)] if lower <= 0 <= upper else []), []
    cap = min(support, k, n - k)
    output = []
    trace = []
    while True:
        if upper - lower + 1 <= cap:
            output.append((row, lower, upper))
            return output, trace
        odd = sum(coefficient % 2 for coefficient in row)
        minimum = max(0, k + odd - n)
        maximum = min(k, odd)
        child_lower = -((-(lower - minimum)) // 2)
        child_upper = (upper - maximum) // 2
        boundaries = []
        right = min(upper, 2 * child_lower + maximum - 2)
        if lower <= right:
            boundaries.append((row, lower, right))
        left = max(lower, 2 * child_upper + minimum + 2)
        if left <= upper:
            boundaries.append((row, left, upper))
        trace.append((row, lower, upper, minimum, maximum, child_lower, child_upper, boundaries))
        output.extend(boundaries)
        if child_lower > child_upper:
            return output, trace
        row = tuple(coefficient // 2 for coefficient in row)
        lower, upper = child_lower, child_upper


def compile_layer(n, intervals, equalities, k, budgets, counts):
    require(0 < k < n, "nontrivial cardinality layer")
    catalogues = []
    q_values = []
    active_budgets = []
    for (row, lower, upper), budget in zip(intervals, budgets):
        if lower > upper:
            return set()
        support = sum(coefficient != 0 for coefficient in row)
        if not support:
            if not lower <= 0 <= upper:
                return set()
            continue
        catalogue, _ = catalogue_fixed(row, lower, upper, k)
        q = ceil_log2(min(upper - lower + 1, support, k, n - k))
        require(0 <= budget <= q, "cardinality slack budget")
        q_values.append(q)
        active_budgets.append(budget)
        catalogues.append(catalogue)
    choices = []
    for catalogue, budget in zip(catalogues, active_budgets):
        chunks = []
        for row, lower, upper in catalogue:
            for start in range(lower, upper + 1, 1 << budget):
                chunks.append((row, start, min(upper, start + (1 << budget) - 1)))
        choices.append(chunks)
    maximum_branches = prod(len(catalogue) for catalogue in catalogues) * (
        1 << (sum(q_values) - sum(active_budgets)))
    answers = set()
    branches = 0
    for chosen in product(*choices):
        branches += 1
        equations = [(list(row), target) for row, target in equalities]
        equations.append(([1] * n, k))
        variable_count = n
        for row, lower, upper in chosen:
            coins = slack_weights(upper - lower)
            coefficients = list(row) + [0] * (variable_count - n) + list(coins)
            variable_count += len(coins)
            equations.append((coefficients, upper))
        equations = [(tuple(row + [0] * (variable_count - len(row))), target)
                     for row, target in equations]
        require(variable_count <= n + sum(budgets), "layer variable budget")
        radix = 1 + max(sum(map(abs, row)) + abs(target) for row, target in equations)
        packed_row = tuple(sum(row[index] * radix ** j for j, (row, _) in enumerate(equations))
                           for index in range(variable_count))
        packed_target = sum(target * radix ** j for j, (_, target) in enumerate(equations))
        equation_values = [(subset_sums(row), target) for row, target in equations]
        for mask, value in enumerate(subset_sums(packed_row)):
            counts["packed_assignment_comparisons"] += 1
            packed_accepts = value == packed_target
            require(packed_accepts == all(values[mask] == target for values, target in equation_values),
                    "conditional signed radix equivalence")
            if packed_accepts:
                projection = mask & ((1 << n) - 1)
                require(projection.bit_count() == k, "cardinality guard retained")
                answers.add(projection)
        counts["packed_instances"] += 1
    require(branches <= maximum_branches, "conditional branch count")
    return answers


def check_budget_accounting():
    comparisons = 0
    for total_q in range(65):
        for layer_q in range(total_q + 1):
            for budget in range(total_q + 1):
                layer_budget = min(budget, layer_q)
                require(layer_q - layer_budget <= total_q - budget,
                        "uniform branch exponent")
                require(layer_budget <= budget, "uniform variable and space budget")
                for numerator, denominator in ((0, 1), (1, 3), (1, 2), (1, 1), (3, 2)):
                    actual = denominator * layer_q - (denominator - numerator) * layer_budget
                    claimed = denominator * total_q - (denominator - numerator) * budget
                    require(actual <= claimed, "exact rational uniform time exponent")
                    comparisons += 1
    return {"exact_exponent_comparisons": comparisons, "maximum_uniform_Q": 64}


def modal_shift(row, lower, upper, k):
    if not row:
        return row, lower, upper, 0, 0
    frequencies = Counter(row)
    common = min(frequencies, key=lambda c: (-frequencies[c], abs(c), c))
    centered = tuple(coefficient - common for coefficient in row)
    defect = len(row) - frequencies[common]
    require(sum(coefficient != 0 for coefficient in centered) == defect, 'exact modal defect')
    require(defect <= sum(coefficient != 0 for coefficient in row), 'defect no worse than support')
    return centered, lower - common * k, upper - common * k, common, defect


def check_one(row, lower, upper, k, counts, normalize=True):
    if normalize:
        centered, start, end, common, defect = modal_shift(row, lower, upper, k)
    else:
        centered, start, end, common = row, lower, upper, 0
        defect = sum(coefficient != 0 for coefficient in row)
    n = len(row)
    require(end - start == upper - lower, 'unchanged interval width')
    catalogue, trace = catalogue_fixed(centered, start, end, k)
    original_values = subset_sums(row)
    centered_values = subset_sums(centered)
    catalogue_values = [(subset_sums(a), left, right) for a, left, right in catalogue]
    for mask in range(1 << n):
        if mask.bit_count() != k:
            continue
        require(original_values[mask] == centered_values[mask] + common * k,
                'cardinality shift identity')
        accepts = any(left <= sums[mask] <= right for sums, left, right in catalogue_values)
        require(accepts == (lower <= original_values[mask] <= upper),
                'centered catalogue equals original interval')
        counts['original_assignment_comparisons'] += 1
    if 0 < k < n and defect and lower <= upper:
        cap = min(upper - lower + 1, defect, k, n-k)
        require(all(1 <= right-left+1 <= cap for _,left,right in catalogue), 'modal catalogue cap')
        require(len(catalogue) <= 2*ceil_log2(upper-lower+1)+1, 'modal catalogue count')
    if 0 < k < n and defect and lower <= upper:
        require(len(trace) <= ceil_log2(upper-lower+1), 'binary recursion depth')
    for current, left, right, minimum, maximum, child_left, child_right, boundaries in trace:
        odd = sum(coefficient % 2 for coefficient in current)
        width = maximum-minimum
        require(width == min(k,n-k,odd,n-odd), 'exact conditional remainder width')
        require(all(1 <= b-a+1 <= width for _,a,b in boundaries), 'boundary width')
        if not width:
            require(not boundaries,'constant remainder gives empty boundaries')
            counts['constant_remainder_frames'] += 1
        if minimum:
            counts['positive_lower_remainder_frames'] += 1
        if child_left > child_right:
            counts['empty_child_frames'] += 1
        else:
            require(child_right-child_left <= (right-left-width)//2, 'child width contracts')
        old_values = subset_sums(current)
        new_values = subset_sums(tuple(coefficient//2 for coefficient in current))
        for mask in range(1<<n):
            if mask.bit_count()!=k: continue
            old,new=old_values[mask],new_values[mask]
            require(minimum <= old-2*new <= maximum,'signed conditional remainder')
            accepts = child_left<=new<=child_right or any(a<=old<=b for _,a,b in boundaries)
            require(accepts == (left<=old<=right),'local guarded disjunction')
            counts['local_assignment_comparisons'] += 1
    if not defect:
        require(bool(catalogue) == (lower <= common*k <= upper), 'constant row handled exactly')
        counts['constant_rows'] += 1
    if common < 0:
        counts['negative_shifts'] += 1
    if defect < sum(coefficient != 0 for coefficient in row):
        counts['strict_support_improvements'] += 1
    counts['layer_intervals'] += 1


def check_rows():
    counts = {key:0 for key in ('coefficient_rows','additional_rows','layer_intervals',
        'original_assignment_comparisons','constant_rows','negative_shifts','strict_support_improvements',
        'constant_remainder_frames','positive_lower_remainder_frames','empty_child_frames','local_assignment_comparisons','raw_parity_fixtures')}
    for n in range(5):
        for row in product(range(-2,3),repeat=n):
            counts['coefficient_rows'] += 1
            low = sum(min(c,0) for c in row)-1
            high = sum(max(c,0) for c in row)+1
            for lower in range(low,high+1):
                for upper in range(lower,high+1):
                    for k in range(n+1):
                        check_one(row,lower,upper,k,counts)
    huge = 1<<511
    fixtures = [
        ((huge,)*7+(huge+3,), 3*huge+1, 3*huge+4),
        ((-huge,)*7+(-huge+3,), -3*huge+1, -3*huge+4),
        ((-huge,)*6, -4*huge, -2*huge),
        ((0,0,0,5,-5), -huge, huge),
        ((2,2,2,3), 7, 6),
    ]
    rng=random.Random(20261030)
    for _ in range(250):
        n=rng.randrange(2,8)
        common=rng.randrange(-100,101)
        row=tuple(common if rng.randrange(4) else rng.randrange(-100,101) for _ in range(n))
        lower,upper=sorted((rng.randrange(-500,501),rng.randrange(-500,501)))
        fixtures.append((row,lower,upper))
    for row,lower,upper in fixtures:
        counts['additional_rows'] += 1
        for k in range(len(row)+1):
            check_one(row,lower,upper,k,counts)
    # The theorem also permits skipping modal normalization. These fixtures
    # exercise constant parity remainders and long binary recursion directly.
    for row, lower, upper in (
        ((-3,1,5,7),-100,100),
        ((-4,2,8,12),-100,100),
        ((-1,)*4,-(1<<511),1<<511),
        ((1,0,-1,0,3),-8,9),
        ((1,3),1,2),
    ):
        for k in range(len(row)+1):
            check_one(row,lower,upper,k,counts,normalize=False)
            counts['raw_parity_fixtures']+=1
    return counts


def check_systems():
    counts = {key:0 for key in ('systems','layers','budget_profiles','packed_instances',
        'packed_assignment_comparisons','original_assignment_comparisons','whole_system_unions',
        'strict_q_reductions','constant_row_obstructions')}
    rng=random.Random(20261031)
    huge=1<<255
    cases=[
        (0,[],[]),
        (1,[((huge,),huge,huge)],[]),
        (5,[((huge,huge,huge,huge,huge+3),2*huge+1,2*huge+4)],[]),
        (5,[((-huge,-huge,-huge,-huge,-huge+3),-2*huge+1,-2*huge+4)],[]),
        (4,[((3,3,3,3),5,7)],[((1,-1,2,-2),0)]),
        (4,[((0,0,0,0),1,2)],[]),
    ]
    for index in range(300):
        n=rng.randrange(2,6)
        intervals=[]
        for _ in range(rng.randrange(1,4)):
            common=rng.randrange(-5,6)
            row=tuple(common if rng.randrange(4) else rng.randrange(-5,6) for _ in range(n))
            lower,upper=sorted((rng.randrange(-15,16),rng.randrange(-15,16)))
            intervals.append((row,lower,upper))
        equalities=[]
        for _ in range(rng.randrange(3)):
            row=tuple(rng.randrange(-4,5) for _ in range(n))
            target=subset_sums(row)[rng.randrange(1<<n)] if index%2 else rng.randrange(-6,7)
            equalities.append((row,target))
        cases.append((n,intervals,equalities))
    for n,intervals,equalities in cases:
        original={mask for mask in range(1<<n)
            if all(lower<=subset_sums(row)[mask]<=upper for row,lower,upper in intervals)
            and all(subset_sums(row)[mask]==target for row,target in equalities)}
        union=original & {0,(1<<n)-1}
        counts['systems']+=1
        for k in range(1,n):
            centered=[]
            ranges=[]
            old_q=0
            new_q=0
            for row,lower,upper in intervals:
                shifted,left,right,common,defect=modal_shift(row,lower,upper,k)
                centered.append((shifted,left,right))
                q=ceil_log2(min(upper-lower+1,defect,k,n-k)) if defect and lower<=upper else 0
                support=sum(c!=0 for c in row)
                old=ceil_log2(min(upper-lower+1,support,k,n-k)) if support and lower<=upper else 0
                require(q<=old,'rowwise nonincreasing slack budget')
                new_q+=q;old_q+=old
                if not defect and not left<=0<=right:
                    counts['constant_row_obstructions']+=1
                ranges.append(range(q+1))
            if new_q<old_q:
                counts['strict_q_reductions']+=1
            expected={mask for mask in original if mask.bit_count()==k}
            for budgets in product(*ranges):
                actual=compile_layer(n,centered,equalities,k,budgets,counts)
                require(actual==expected,'centered packed solution set equals original')
                counts['original_assignment_comparisons']+=1<<n
                counts['budget_profiles']+=1
                union|=actual
            counts['layers']+=1
        require(union==original,'centered union over all cardinalities')
        counts['whole_system_unions']+=1
    return counts


if __name__=='__main__':
    require(__debug__,'run without -O')
    print(json.dumps({'catalogues':check_rows(),'compilation':check_systems(),
                     'uniform_budget':check_budget_accounting()},indent=2,sort_keys=True))
