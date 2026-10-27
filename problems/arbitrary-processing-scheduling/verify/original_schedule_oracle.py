"""Independent finite original-pair schedule enumeration for scheduling checks.

Attribution: Yilin Liu and GPT-6 Astra Pro. Apache-2.0.
This module imports no scheduling backend or rank/LP/contraction helpers.
"""
from fractions import Fraction as F
from itertools import product


def schedules(instance):
    q, m = len(instance.times), len(instance.ranks)
    result = {}
    bounds = [range(instance.ranks[j][1 << p]+1) for p in range(q) for j in range(m)]
    for x in product(*bounds):
        if any(sum(x[p*m+j] for p in range(q)) != instance.ranks[j][-1] for j in range(m)):
            continue
        if any(x[p*m+j] and instance.times[p][j] is None for p in range(q) for j in range(m)):
            continue
        if any(sum(x[p*m+j] for p in range(q) if mask >> p & 1) > instance.ranks[j][mask]
               for j in range(m) for mask in range(1 << q)):
            continue
        cost = sum(instance.costs[p][j]*x[p*m+j] for p in range(q) for j in range(m))
        load = max((sum(instance.times[p][j]*x[p*m+j] for j in range(m)
                        if instance.times[p][j] is not None) for p in range(q)), default=F(0))
        result[tuple(x)] = F(cost), F(load)
    return result


def uniform(q, n):
    return tuple(0 if not s else n for s in range(1 << q))
