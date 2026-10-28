"""Polynomial certificate generation for supplied optimum unit-flow supports.

This does not optimize an arbitrary support. An invalid or nonoptimal support
raises ValueError. The independent verifier imports none of this module.

Copyright 2026 icekylinx. Authored by GPT-6 Astra Pro.
SPDX-License-Identifier: Apache-2.0
"""
from fractions import Fraction
from flow_certificates import (FlowCertificate, MaximumCertificate, _instance,
                               _ids, _balances, verify_flow, verify_maximum)


def certify_flow(n, arcs, balances, used, failed=None):
    _instance(n, arcs, failed)
    _balances(n, balances)
    used = tuple(used)
    selected = _ids(used, len(arcs))
    if failed in selected:
        raise ValueError('failed arc in support')
    residual = []
    cost = Fraction(0)
    divergence = [0] * n
    for i, a in enumerate(arcs):
        if i == failed:
            continue
        if i in selected:
            residual.append((a.head, a.tail, -a.cost))
            cost += a.cost
            divergence[a.tail] += 1
            divergence[a.head] -= 1
        else:
            residual.append((a.tail, a.head, a.cost))
    if divergence != list(balances):
        raise ValueError('infeasible supplied support')
    # A zero-edge super-source reaches every component, including isolated
    # negative cycles that a source-only shortest-path scan would miss.
    potential = [Fraction(0)] * n
    for iteration in range(n):
        changed = False
        for u, v, c in residual:
            if potential[v] > potential[u] + c:
                potential[v] = potential[u] + c
                changed = True
        if not changed:
            break
        if iteration == n - 1:
            raise ValueError('nonoptimal support: negative residual cycle')
    certificate = FlowCertificate(used, cost, tuple(potential))
    if not verify_flow(n, arcs, balances, certificate, failed):
        raise ValueError('certificate construction failed')
    return certificate


def certify_maximum(n, arcs, source, target, used, failed=None):
    _instance(n, arcs, failed)
    if (type(source) is not int or type(target) is not int or source == target
            or not 0 <= source < n or not 0 <= target < n):
        raise ValueError('distinct original terminals required')
    used = tuple(used)
    selected = _ids(used, len(arcs))
    value = sum((a.tail == source) - (a.head == source) for i, a in enumerate(arcs) if i in selected)
    if value < 0:
        raise ValueError('negative source flow')
    balances = [0] * n
    balances[source], balances[target] = value, -value
    flow = certify_flow(n, arcs, balances, used, failed)
    adjacent = [[] for _ in range(n)]
    for i, a in enumerate(arcs):
        if i == failed:
            continue
        u, v = (a.head, a.tail) if i in selected else (a.tail, a.head)
        adjacent[u].append(v)
    reached, queue = {source}, [source]
    for u in queue:
        for v in adjacent[u]:
            if v not in reached:
                reached.add(v)
                queue.append(v)
    certificate = MaximumCertificate(value, flow, tuple(sorted(reached)))
    if not verify_maximum(n, arcs, source, target, certificate, failed):
        raise ValueError('supplied flow is not maximum')
    return certificate


def balance_feasibility(n, arcs, balances, failed=None):
    """Return (used_ids, None) or (None, violated_cut) for integral balances.

    Costs are deliberately ignored. Binary supplies remain numerical residual
    capacities, never lists of units. This is not minimum-cost optimization.
    """
    _instance(n, arcs, failed)
    _balances(n, balances)
    total = sum(max(b, 0) for b in balances)
    if total > len(arcs) - (failed is not None):
        return None, tuple(v for v, b in enumerate(balances) if b > 0)
    start, end = n, n + 1
    adjacent = [[] for _ in range(n + 2)]
    edges = []

    def insert(u, v, capacity):
        i = len(edges)
        edges.extend([[u, v, capacity], [v, u, 0]])
        adjacent[u].append(i)
        adjacent[v].append(i + 1)
        return i

    original = {i: insert(a.tail, a.head, 1) for i, a in enumerate(arcs) if i != failed}
    for v, b in enumerate(balances):
        if b > 0:
            insert(start, v, b)
        elif b < 0:
            insert(v, end, -b)
    sent = 0
    while sent < total:
        parent = [None] * (n + 2)
        parent[start] = -1
        queue = [start]
        for u in queue:
            for i in adjacent[u]:
                _, v, capacity = edges[i]
                if capacity > 0 and parent[v] is None:
                    parent[v] = i
                    queue.append(v)
        if parent[end] is None:
            return None, tuple(v for v in range(n) if parent[v] is not None)
        amount = total - sent
        v = end
        while v != start:
            i = parent[v]
            amount = min(amount, edges[i][2])
            v = edges[i][0]
        v = end
        while v != start:
            i = parent[v]
            edges[i][2] -= amount
            edges[i ^ 1][2] += amount
            v = edges[i][0]
        sent += amount
    return tuple(i for i, edge in original.items() if edges[edge][2] == 0), None
