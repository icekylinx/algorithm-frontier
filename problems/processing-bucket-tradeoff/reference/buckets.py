"""Bucket-label client using the canonical general-processing joint backend.

Attribution: icekylinx and GPT-6 Astra Pro. Apache-2.0.
The exact-table LP and integer recovery have explicit enumeration costs.
"""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import importlib.util
import sys

_name = '_algorithm_frontier_general_processing_profiles'
if _name not in sys.modules:
    _path = Path(__file__).resolve().parents[2] / 'arbitrary-processing-scheduling/reference/profiles.py'
    _spec = importlib.util.spec_from_file_location(_name, _path)
    _module = importlib.util.module_from_spec(_spec)
    sys.modules[_name] = _module
    _spec.loader.exec_module(_module)
core = sys.modules[_name]
Instance = core.Instance


class BucketBackend(core.JointBackend):
    def __init__(self, instance, depth):
        if type(depth) is not int or depth < 0:
            raise ValueError('validated general Instance and integer depth >=0 required')
        self.depth = depth
        denominator = (1 << (depth+1))-1
        self.factor = F(3*(1 << depth)-1, denominator)
        self.endpoints = ((F(1),) if depth == 0 else
                          tuple(F((1 << depth)+(1 << i)-1, denominator) for i in range(depth+1)))
        super().__init__(instance)

    def plan(self, target, labels):
        target = core.shared.exact(target)
        labels = tuple(labels)
        if (target <= 0 or len(labels) != self.q
                or any(type(v) is not int or not 0 <= v <= self.depth for v in labels)):
            raise ValueError('positive target and one valid label per machine required')
        allowed, counts, loads = set(), [], []
        for p, label in enumerate(labels):
            small, big = [], []
            for j, value in enumerate(self.instance.times[p]):
                if value is None:
                    continue
                if label == 0:
                    if value <= self.endpoints[0]*target:
                        small.append((p, j))
                elif value <= (1-self.endpoints[label-1])*target:
                    small.append((p, j))
                elif self.endpoints[label-1]*target < value <= self.endpoints[label]*target:
                    big.append((p, j))
            allowed.update(small)
            allowed.update(big)
            if label:
                counts.append((tuple(big), 1))
            loads.append((tuple(small), target if label == 0 else (1-self.endpoints[label-1])*target))
        return core.Plan(frozenset(allowed), tuple(counts), tuple(loads))

    def plans(self, target):
        # range objects hold binary counters; product materializes only the
        # depth+1 label alphabet, whose numeric size is charged by AB's H+k.
        for labels in product(range(self.depth+1), repeat=self.q):
            yield self.plan(target, labels)

    def target(self, target, _search_dispatch=2):
        target = core.shared.exact(target)
        if target < 0:
            raise ValueError('nonnegative target required')
        if target == 0:
            return core.shared.Backend.target(self, 0, 2)
        return self.try_plans(target, self.plans(target), self.factor)
