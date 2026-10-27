"""Width-two oracle gate. Attribution: Yilin Liu and GPT-6 Astra Pro.

Apache-2.0. Deterministic polynomial-oracle matching terminal, degree branching,
and explicit all-input width-violation outcome. No higher-quota solver.
"""
from collections import deque
from dataclasses import dataclass
from itertools import combinations


def intersection(ground, independent1, independent2):
    """Maximum common independent set via shortest exchange augmentations."""
    ground = tuple(ground)
    chosen = frozenset()
    while True:
        outside = tuple(x for x in ground if x not in chosen)
        sources = tuple(x for x in outside if independent1(chosen | {x}))
        targets = {x for x in outside if independent2(chosen | {x})}
        previous = {x: None for x in sources}
        queue = deque(sources)
        end = None
        while queue:
            x = queue.popleft()
            if x in targets:
                end = x
                break
            if x in chosen:
                adjacent = (y for y in outside if independent1((chosen - {x}) | {y}))
            else:
                adjacent = (y for y in sorted(chosen) if independent2((chosen - {y}) | {x}))
            for y in adjacent:
                if y not in previous:
                    previous[y] = x
                    queue.append(y)
        if end is None:
            return chosen
        path = set()
        while end is not None:
            path.add(end)
            end = previous[end]
        chosen = chosen.symmetric_difference(path)
        if not independent1(chosen) or not independent2(chosen):
            raise RuntimeError('matroid augmentation invariant violated')


@dataclass(frozen=True)
class Outcome:
    status: str  # SUCCESS, INFEASIBLE, WIDTH VIOLATION
    selected: tuple = ()
    witnesses: tuple = ()
    scenario: int | None = None
    certificate: tuple = ()
    nodes: int = 0


def solve(q, rank, rank_oracle, scenarios, forced=()):
    """Exact unit gate with paid original matroid rank and unit-test callbacks.

    scenario(C) returns an actual unit witness or None for infeasibility.
    Each callback must define a hereditary family containing the empty set.
    Original player rank, resource constraints and budgets remain fixed.
    """
    if type(q) is not int or type(rank) is not int or not 0 <= rank <= q:
        raise ValueError('invalid ground or rank')
    scenarios = tuple(scenarios)
    if not scenarios or any(not callable(test) for test in scenarios):
        raise ValueError('nonempty unit-test callback list required')
    ground = frozenset(range(q))
    forced = frozenset(forced)
    if any(type(x) is not int or x not in ground for x in forced):
        raise ValueError('invalid forced omission')
    if rank_oracle(ground) != rank:
        raise ValueError('supplied rank differs from original oracle')
    corank = q-rank
    # Dual independent iff removing these elements preserves original rank.
    def independent(omitted):
        return rank_oracle(ground - omitted) == rank
    if len(forced) > corank or not independent(forced):
        return Outcome('INFEASIBLE')
    failed = set()
    edges = []
    for player in range(q):
        if any(test(frozenset((player,))) is None for test in scenarios):
            failed.add(player)
    for u,v in combinations(range(q),2):
        if any(test(frozenset((u,v))) is None for test in scenarios):
            edges.append((u,v))
    initial = forced | failed
    if not independent(initial):
        return Outcome('INFEASIBLE')
    stack = [frozenset(initial)]
    nodes = 0
    solution = None
    while stack:
        omitted = stack.pop()
        nodes += 1
        residual = [(u,v) for u,v in edges if u not in omitted and v not in omitted]
        adjacency = {}
        for u,v in residual:
            adjacency.setdefault(u,set()).add(v)
            adjacency.setdefault(v,set()).add(u)
        vertex = next((v for v in sorted(adjacency) if len(adjacency[v]) >= 2), None)
        if vertex is not None:
            # Push neighbor branch first so the singleton branch is processed first.
            for added in (frozenset(adjacency[vertex]),frozenset((vertex,))):
                child = omitted | added
                if independent(child):
                    stack.append(child)
            continue
        # Matching terminal: one representative per disjoint edge, then extend.
        endpoints = tuple(sorted(adjacency))
        def partition_independent(chosen):
            return all(not (u in chosen and v in chosen) for u,v in residual)
        representatives = intersection(endpoints,
                                       lambda chosen: independent(omitted | chosen),
                                       partition_independent)
        if len(representatives) != len(residual):
            continue
        completion = omitted | representatives
        for player in range(q):
            if player not in completion and independent(completion | {player}):
                completion = completion | {player}
        if len(completion) != corank:
            raise RuntimeError('dual basis extension invariant violated')
        solution = tuple(sorted(ground-completion))
        break
    if solution is None:
        return Outcome('INFEASIBLE',nodes=nodes)
    selected = frozenset(solution)
    witnesses = []
    for index,test in enumerate(scenarios):
        witness = test(selected)
        if witness is not None:
            witnesses.append(witness)
            continue
        certificate = selected
        for player in solution:
            if test(certificate - {player}) is None:
                certificate = certificate - {player}
        if len(certificate) < 3:
            raise RuntimeError('scenario heredity or callback consistency violated')
        return Outcome('WIDTH VIOLATION',scenario=index,
                       certificate=tuple(sorted(certificate)),nodes=nodes)
    return Outcome('SUCCESS',solution,tuple(witnesses),nodes=nodes)
