"""Actual prefix-free weighted omission and streamed containment covers.

Attribution: Yilin Liu and GPT-6 Astra Pro. Apache-2.0.
Oracle costs remain paid. Native flow LPs use the canonical finite simplex,
whose potentially exponential bound is separate from the recursion's bound.
"""
from dataclasses import dataclass
from fractions import Fraction as F
from itertools import combinations, product
from math import comb
from pathlib import Path
import importlib.util
import sys


def rational(value):
    if type(value) not in (int,F):
        raise ValueError('exact int or Fraction required')
    return F(value)


def ids(values,q):
    return (type(values) is tuple and all(type(i) is int and 0 <= i < q for i in values)
            and len(set(values)) == len(values))


def first_crossings(order, ratio, deficit, counts=None):
    """Budget-pruned DFS of first-crossing words, not all omitted subsets."""
    order = tuple(order)
    ratio = rational(ratio)
    if (ratio <= 1 or type(deficit) is not int or not 0 <= deficit <= len(order)
            or any(type(i) is not int for i in order) or len(set(order)) != len(order)):
        raise ValueError('invalid first-crossing input')
    if not deficit:
        return
    quantity = (ratio-1)*deficit
    zeros = -(-quantity.numerator // quantity.denominator)-1
    # (position, ones, zeros, deleted IDs, word), one pending sibling per depth.
    stack = [(0,0,0,(),())]
    while stack:
        position,one,zero,deleted,word = stack.pop()
        if counts is not None:
            counts['prefix_states'] = counts.get('prefix_states',0)+1
        if ratio*one > position:
            if counts is not None:
                counts['certificates'] = counts.get('certificates',0)+1
            yield deleted,word
            continue
        if position == len(order):
            continue
        if zero < zeros:
            stack.append((position+1,one,zero+1,deleted,word+(0,)))
        if one < deficit:
            stack.append((position+1,one+1,zero,deleted+(order[position],),word+(1,)))


@dataclass(frozen=True)
class Choice:
    selected: tuple
    context: object = None


@dataclass(frozen=True)
class Row:
    coefficients: tuple
    capacity: F


@dataclass(frozen=True)
class GapResult:
    choice: Choice
    counts: dict


def gap(q, rank, full, weak, prepare, separate, forced=(), observe=None, counts=None):
    """Fixed or protected-witness adaptive weighted packing gap.

    prepare(Q) returns an attaining Choice or None. separate(Q,choice,rates)
    returns a valid strictly violated nonnegative Row, or None for membership.
    Adaptive callers must establish the original protected-witness invariant.
    """
    full,weak = rational(full),rational(weak)
    forced = tuple(forced)
    if (type(q) is not int or type(rank) is not int or not 1 <= rank <= q
            or not full > weak > 0 or not ids(forced,q)):
        raise ValueError('invalid weighted gap input')
    if len(forced) > q-rank:
        return None
    ratio = full/(full-weak)
    if counts is None:
        counts = {}
    counts.update(nodes=0,selector_rejections=0,zero_deficit_rejections=0,
                  prefix_states=0,certificates=0)
    stack = [{'allowed':frozenset(range(q))-frozenset(forced),'children':None}]
    while stack:
        frame = stack[-1]
        allowed = frame['allowed']
        if frame['children'] is None:
            counts['nodes'] += 1
            choice = prepare(allowed)
            if choice is None:
                counts['selector_rejections'] += 1
                if observe is not None: observe(allowed,None,None)
                stack.pop()
                continue
            if (type(choice) is not Choice or not ids(choice.selected,q)
                    or len(choice.selected) != rank or not set(choice.selected) <= allowed):
                raise ValueError('invalid restriction selector output')
            rates = tuple(weak if i in allowed else F(0) for i in range(q))
            row = separate(allowed,choice,rates)
            if observe is not None: observe(allowed,choice,row)
            if row is None:
                return GapResult(choice,counts)
            if type(row) is not Row:
                raise ValueError('canonical nonnegative packing Row required')
            coefficients = tuple(rational(a) for a in row.coefficients)
            capacity = rational(row.capacity)
            if (len(coefficients) != q or min(coefficients,default=F(0)) < 0 or capacity < 0
                    or sum((a*z for a,z in zip(coefficients,rates)),F(0)) <= capacity):
                raise ValueError('row is not a strict nonnegative separator')
            deficit = len(allowed)-rank
            if not deficit:
                counts['zero_deficit_rejections'] += 1
                stack.pop()
                continue
            order = tuple(sorted(allowed,key=lambda i:(-coefficients[i],i)))
            frame['children'] = first_crossings(order,ratio,deficit,counts)
        try:
            deleted,_ = next(frame['children'])
        except StopIteration:
            stack.pop()
        else:
            stack.append({'allowed':allowed-frozenset(deleted),'children':None})
    return None


def explicit_separator(rows,q):
    """A fixed explicit packing oracle, retaining every original coordinate."""
    rows = tuple(Row(tuple(rational(a) for a in row.coefficients),rational(row.capacity)) for row in rows)
    if any(len(row.coefficients) != q or row.capacity < 0 or any(a < 0 for a in row.coefficients) for row in rows):
        raise ValueError('invalid explicit packing rows')
    def separate(allowed,choice,rates):
        return next((row for row in rows if sum((a*z for a,z in zip(row.coefficients,rates)),F(0)) > row.capacity),None)
    return separate


def uniform_selector(rank,costs=None,budget=None):
    """Actual minimum additive-cost unrestricted rank-subset selector."""
    costs = None if costs is None else tuple(rational(c) for c in costs)
    budget = None if budget is None else rational(budget)
    def prepare(allowed):
        if len(allowed) < rank:
            return None
        selected = tuple(sorted(sorted(allowed,key=lambda i: ((costs[i] if costs is not None else F(0)),i))[:rank]))
        cost = sum((costs[i] for i in selected),F(0)) if costs is not None else F(0)
        return None if budget is not None and cost > budget else Choice(selected,cost)
    return prepare


def common_matroid_selector(rank,independent1,independent2,costs,budget=None):
    """Paid polynomial exact weighted restriction via the canonical core."""
    module = _load('_algorithm_frontier_bounded', 'robust-bounded-certificates/reference/bounded.py')
    costs = tuple(rational(c) for c in costs)
    budget = None if budget is None else rational(budget)
    def prepare(allowed):
        first = lambda selected: selected <= allowed and independent1(selected)
        second = lambda selected: selected <= allowed and independent2(selected)
        certificate = module.minimum_cost(first,second,costs,rank)
        if len(certificate.chosen) != rank:
            return None
        cost = sum((costs[i] for i in certificate.chosen),F(0))
        if budget is not None and cost > budget:
            return None
        return Choice(certificate.chosen,(cost,certificate))
    return prepare


def local_cover(n,p,base):
    """Exact minimizing seed size and deterministic greedy containment cover."""
    base = rational(base)
    if type(n) is not int or type(p) is not int or not 0 <= p <= n or base <= 1:
        raise ValueError('invalid local cover input')
    k = min(range(p+1),key=lambda k:(F(comb(n,k),comb(p,k))*base**(p-k),k))
    universe = {sum(1 << i for i in chosen) for chosen in combinations(range(n),p)}
    candidates = tuple(sum(1 << i for i in chosen) for chosen in combinations(range(n),k))
    result = []
    while universe:
        chosen = max(candidates,key=lambda candidate:sum(candidate & target == candidate for target in universe))
        result.append(chosen)
        universe = {target for target in universe if chosen & target != chosen}
    return k,tuple(result)


def cover_seeds(q,corank,base,counts=None):
    """Stream the actual logarithmic-block covers, including every profile."""
    base = rational(base)
    if type(q) is not int or type(corank) is not int or not 0 <= corank < q or base <= 1:
        raise ValueError('invalid whole-ground input')
    if q < 4:
        for chosen in combinations(range(q),corank):
            if counts is not None: counts['seeds'] = counts.get('seeds',0)+1
            yield chosen
        return
    length = q.bit_length()-1
    blocks = tuple(tuple(range(start,min(q,start+length))) for start in range(0,q,length))
    tables = {(n,p):local_cover(n,p,base) for n in {len(block) for block in blocks} for p in range(n+1)}
    if counts is not None:
        counts['local_records'] = sum(len(cover) for _,cover in tables.values())
    for profile in product(*(range(len(block)+1) for block in blocks)):
        if counts is not None: counts['profile_states'] = counts.get('profile_states',0)+1
        if sum(profile) != corank:
            continue
        if counts is not None: counts['profiles'] = counts.get('profiles',0)+1
        for masks in product(*(tables[len(block),p][1] for block,p in zip(blocks,profile))):
            seed = tuple(v for block,mask in zip(blocks,masks) for i,v in enumerate(block) if mask >> i & 1)
            if counts is not None: counts['seeds'] = counts.get('seeds',0)+1
            yield seed


def whole_ground(q,rank,base,extension,counts=None):
    """Preserve the exact full-target/weak-output contract of extension(Z)."""
    if type(q) is not int or type(rank) is not int or not 1 <= rank <= q:
        raise ValueError('nonempty selected cardinality required')
    for seed in cover_seeds(q,q-rank,base,counts):
        answer = extension(seed)
        if answer is not None:
            return answer
    return None


@dataclass(frozen=True)
class RationalResult:
    choice: object
    value: F
    witness: object
    calls: int
    lower: F


def rational_optimize(alpha,denominator_bound,upper,initial,gap_oracle,reoptimize):
    """Full-accuracy fixed-family search followed by ORIGINAL reoptimization."""
    alpha,upper = rational(alpha),rational(upper)
    if (not 0 < alpha < 1 or type(denominator_bound) is not int
            or denominator_bound < 1 or upper < 0):
        raise ValueError('invalid rational comparator parameters')
    delta = F(1,2*alpha.denominator*denominator_bound**2)
    low,high = 0,-(-(upper/delta).numerator // (upper/delta).denominator)+1
    saved,calls = initial,0
    while high-low > 1:
        mid = (low+high)//2
        result = gap_oracle(mid*delta)
        calls += 1
        if result is None:
            high = mid
        else:
            low,saved = mid,result
    value,witness = reoptimize(saved)
    value = rational(value)
    if not 0 <= value <= upper or value.denominator > denominator_bound or value < alpha*low*delta:
        raise ValueError('fixed-family reoptimization contract violated')
    return RationalResult(saved,value,witness,calls,low*delta)


def _load(name,relative):
    if name not in sys.modules:
        path = Path(__file__).resolve().parents[2] / relative
        spec = importlib.util.spec_from_file_location(name,path)
        module = importlib.util.module_from_spec(spec)
        sys.modules[name] = module
        spec.loader.exec_module(module)
    return sys.modules[name]


def flow_gap(network,rank,full,weak,budgets=(),setup=None,forced=(),selector=None):
    """Native fixed/adaptive flow client using actual first-crossing omission.

    An external setup selector must attain minimum setup on its fixed family.
    The default is the unrestricted rank-subset minimum-fee selector.
    """
    flow = _load('_algorithm_frontier_concurrent','selected-flow/reference/concurrent.py')
    q = len(network.commodities)
    budgets = tuple((tuple(tuple(rational(x) for x in row) for row in charges),rational(cap))
                    for charges,cap in budgets)
    if setup is not None:
        fees,charges,cap = setup
        setup = (tuple(rational(x) for x in fees),
                 tuple(tuple(rational(x) for x in row) for row in charges),rational(cap))
    if not q:
        raise ValueError('nonempty original commodity ground required')
    flow.formulation(network,(0,),budgets,setup)
    if selector is None:
        selector = uniform_selector(rank,None if setup is None else setup[0])
    def prepare(allowed):
        choice = selector(allowed)
        if choice is None:
            return None
        if type(choice) is not Choice:
            raise ValueError('canonical selector Choice required')
        residual = None if setup is None else rational(setup[2])-sum((rational(setup[0][i]) for i in choice.selected),F(0))
        return None if residual is not None and residual < 0 else Choice(choice.selected,residual)
    def separate(allowed,choice,rates):
        rows = budgets if setup is None else budgets+((setup[1],choice.context),)
        row = flow.separate(network,rates,rows)
        return None if row is None else Row(row.coefficients,row.capacity)
    answer = gap(q,rank,full,weak,prepare,separate,forced)
    if answer is None:
        return None
    certificate = flow.optimize_fixed(network,answer.choice.selected,budgets,setup)
    if certificate is None or certificate.rate < weak:
        raise RuntimeError('native flow recovery violated weak service')
    return answer,certificate
