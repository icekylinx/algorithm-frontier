"""Native signed-cost unit flows, general balances and compact deletion reports.

Copyright 2026 icekylinx. Authored by GPT-6 Astra Pro. Apache-2.0.
Original arcs may be loops or parallel records. Integral supplies remain binary.
"""
from bisect import bisect_left
from fractions import Fraction as F
from heapq import heappush, heappop
from certify_flow import balance_feasibility
from flow_certificates import (FlowCertificate, MaximumCertificate, _instance,
                               _balances, verify_flow, verify_maximum, verify_infeasible)
from unit_flow import Residual, CompactPaths


def minimum_balance(n, arcs, balances, failed=None):
    """Return (original optimum certificate, None) or (None, violated cut)."""
    arcs, balances = tuple(arcs), tuple(balances)
    _instance(n, arcs, failed)
    _balances(n, balances)
    feasible, cut = balance_feasibility(n, arcs, balances, failed)
    if feasible is None:
        if not verify_infeasible(n, arcs, balances, cut, failed):
            raise RuntimeError('original infeasibility certificate failed')
        return None, cut
    # Saturating every negative-cost arc and complementing its variable makes
    # every transformed forward cost nonnegative, including isolated cycles.
    desired = list(balances)
    negative = [False]*len(arcs)
    original = [None]*len(arcs)
    source, target = n, n+1
    adjacency = [[] for _ in range(n+2)]
    edges = []

    def insert(u, v, capacity, cost):
        index = len(edges)
        edges.extend([[u,v,capacity,F(cost)],[v,u,0,-F(cost)]])
        adjacency[u].append(index)
        adjacency[v].append(index+1)
        return index

    for i,arc in enumerate(arcs):
        if i == failed:
            continue
        if arc.cost < 0:
            negative[i] = True
            desired[arc.tail] -= 1
            desired[arc.head] += 1
            original[i] = insert(arc.head,arc.tail,1,-arc.cost)
        else:
            original[i] = insert(arc.tail,arc.head,1,arc.cost)
    for v,b in enumerate(desired):
        if b > 0:insert(source,v,b,0)
        elif b < 0:insert(v,target,-b,0)
    required = sum(max(b,0) for b in desired)
    if required > len(arcs):
        raise RuntimeError('feasible transformed unit flow exceeds its arc count')
    potential = [F(0)]*(n+2)
    sent = 0
    while sent < required:
        distance = [None]*(n+2)
        parent = [None]*(n+2)
        distance[source] = (F(0),0)
        queue = [(F(0),0,source)]
        while queue:
            cost,hops,u = heappop(queue)
            if distance[u] != (cost,hops):
                continue
            for index in adjacency[u]:
                _,v,capacity,weight = edges[index]
                if not capacity:
                    continue
                reduced = weight+potential[u]-potential[v]
                if reduced < 0:
                    raise RuntimeError('negative reduced cost before Dijkstra')
                candidate = (cost+reduced,hops+1)
                if distance[v] is None or candidate < distance[v]:
                    distance[v] = candidate
                    parent[v] = index
                    heappush(queue,(*candidate,v))
        if distance[target] is None:
            raise RuntimeError('original feasible flow lost its transformed completion')
        cap_distance = distance[target][0]
        for v,d in enumerate(distance):
            potential[v] += cap_distance if d is None else min(d[0],cap_distance)
        path, v = [], target
        while v != source:
            index = parent[v]
            if index is None or len(path) >= n+2:
                raise RuntimeError('invalid shortest augmenting path')
            path.append(index)
            v = edges[index][0]
        amount = min(required-sent,*(edges[index][2] for index in path))
        # Every simple super-source/sink path uses an original unit arc.
        if amount != 1:
            raise RuntimeError('transformed augmentation must have unit bottleneck')
        for index in path:
            edges[index][2] -= amount
            edges[index^1][2] += amount
        sent += amount
    used = []
    for i,index in enumerate(original):
        if index is not None:
            transformed = edges[index][2] == 0
            if transformed != negative[i]:used.append(i)
    certificate = FlowCertificate(tuple(used),sum((F(arcs[i].cost) for i in used),F(0)),tuple(potential[:n]))
    if not verify_flow(n,arcs,balances,certificate,failed):
        raise RuntimeError('native optimum failed its independent original-input certificate')
    return certificate,None


def minimum_maximum(n, arcs, source, target, failed=None):
    """Maximum nonnegative source flow, then minimum signed cost including cycles."""
    arcs = tuple(arcs)
    _instance(n,arcs,failed)
    if (type(source) is not int or type(target) is not int or source == target
            or not 0 <= source < n or not 0 <= target < n):
        raise ValueError('distinct original terminals required')
    low,high = 0,len(arcs)+1
    while high-low > 1:
        value = (low+high)//2
        balances = [0]*n
        balances[source],balances[target] = value,-value
        used,_ = balance_feasibility(n,arcs,balances,failed)
        if used is None:high=value
        else:low=value
    balances = [0]*n
    balances[source],balances[target] = low,-low
    flow,_ = minimum_balance(n,arcs,balances,failed)
    used = set(flow.used)
    adjacency = [[] for _ in range(n)]
    for i,arc in enumerate(arcs):
        if i != failed:
            u,v = (arc.head,arc.tail) if i in used else (arc.tail,arc.head)
            adjacency[u].append(v)
    reached = [False]*n
    reached[source] = True
    queue = [source]
    for u in queue:
        for v in adjacency[u]:
            if not reached[v]:reached[v]=True;queue.append(v)
    certificate = MaximumCertificate(low,flow,tuple(v for v in range(n) if reached[v]))
    if not verify_maximum(n,arcs,source,target,certificate,failed):
        raise RuntimeError('native maximum certificate failed')
    return certificate


class BalanceOracle:
    """Compact fixed-balance single-original-arc deletion reports.

    Construct through build_balance_oracle. Negative residual tags are baseline
    positions, positive tags are original arc IDs; these are internal records.
    """
    def __init__(self,n,arcs,certificate):
        self.baseline = certificate.used  # sorted by the native producer
        self.baseline_cost = certificate.cost
        self._paths = None
        self._values = ()
        self.support = self.baseline
        if not self.baseline:
            return
        position = {arc:i for i,arc in enumerate(self.baseline)}
        residual = tuple(Residual(arc.head,arc.tail,-arc.cost,1,position[i],-1)
                         if i in position else Residual(arc.tail,arc.head,arc.cost,1,i,1)
                         for i,arc in enumerate(arcs))
        demands = {j:(arcs[i].tail,arcs[i].head) for j,i in enumerate(self.baseline)}
        paths = CompactPaths(n,residual,demands)
        values = []
        for j,i in enumerate(self.baseline):
            path = paths.report(j)
            values.append(None if path is None else certificate.cost-arcs[i].cost+sum((a.cost for a in path),F(0)))
        retained = set(self.baseline)
        retained.update(a.original for a in paths.retained_residuals() if a.sign > 0)
        self.support = tuple(sorted(retained))
        self._values = tuple(values)
        # Dense baseline-position indexing removes hash tables from query work.
        paths.descriptors = tuple(paths.descriptors[j] for j in range(len(self.baseline)))
        self._paths = paths

    def _index(self,failed):
        if failed is not None and type(failed) is not int:
            raise ValueError('one original integer arc ID or None required')
        if failed is None:
            return None
        index = bisect_left(self.baseline,failed)
        return index if index<len(self.baseline) and self.baseline[index]==failed else None

    def value(self,failed=None):
        index = self._index(failed)
        return self.baseline_cost if index is None else self._values[index]

    def query(self,failed=None):
        index = self._index(failed)
        if index is None:
            return self.baseline
        path = self._paths.report(index)
        if path is None:
            return None
        removed = [False]*len(self.baseline)
        removed[index] = True
        added = []
        for arc in path:
            if arc.sign < 0:removed[arc.original]=True
            else:added.append(arc.original)
        return tuple(i for j,i in enumerate(self.baseline) if not removed[j])+tuple(added)

    def record_count(self):
        if self._paths is None:return 1
        paths = self._paths
        return (2+len(paths.phase_counts)+len(self.baseline)+len(self.support)+len(self._values)+len(paths.descriptors)
                +2*paths.n*len(paths.hubs)
                +sum(len(d[1]) if d is not None and d[0]=='short' else 0 for d in paths.descriptors))


def build_balance_oracle(n,arcs,balances):
    """Return (oracle, None), or (None, original infeasibility cut)."""
    arcs,balances = tuple(arcs),tuple(balances)
    certificate,cut = minimum_balance(n,arcs,balances)
    return ((None,cut) if certificate is None else (BalanceOracle(n,arcs,certificate),None))


class MaximumBalanceOracle:
    """Signed minimum-cost maximum flow after one independent original deletion.

    Two initialized balance levels suffice because a unit-capacity deletion
    decreases the maximum value by at most one. Neither level retains input.
    """
    def __init__(self,n,arcs,source,target):
        arcs=tuple(arcs)
        certificate=minimum_maximum(n,arcs,source,target)
        self.maximum=certificate.value
        self.upper=BalanceOracle(n,arcs,certificate.flow)
        self.lower=None
        if self.maximum:
            balances=[0]*n
            balances[source],balances[target]=self.maximum-1,1-self.maximum
            self.lower,cut=build_balance_oracle(n,arcs,balances)
            if self.lower is None:
                raise RuntimeError('lower consecutive flow level must be feasible')
        self.support=tuple(sorted(set(self.upper.support)|set(self.lower.support if self.lower is not None else ())))

    def query(self,failed=None):
        used=self.upper.query(failed)
        if used is not None:
            return self.maximum,self.upper.value(failed),used
        if self.lower is None:
            raise RuntimeError('zero-value feasibility cannot be lost')
        used=self.lower.query(failed)
        if used is None:
            raise RuntimeError('one unit deletion lost two flow values')
        return self.maximum-1,self.lower.value(failed),used

    def record_count(self):
        return 1+len(self.support)+self.upper.record_count()+(self.lower.record_count() if self.lower is not None else 0)
