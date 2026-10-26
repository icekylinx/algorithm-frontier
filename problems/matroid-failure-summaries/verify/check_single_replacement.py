#!/usr/bin/env python3
"""Verify the singleton replacement theorem without assuming its quotient.

The algorithm uses independence queries on accepted sets; its reference
uses complete original-prefix ranks. Other checks exhaust valid small
matroids, coarsen a nonrepresentable fixture, and validate the proposed
contraction even when some contracted items have failed.
"""
import json
import random
from collections import Counter
from functools import lru_cache
from itertools import combinations, product
from check_summaries import all_matroid_rank_tables
from check_weighted_obstruction import ITEMS, independent as obstruction_independent
from check_weighted_prefix import all_failures, bits, require, survivors


def blocks(n, edges, mask):
    """Compute blocks from edges by a depth-first low-link decomposition."""
    adjacency = [[] for _ in range(n)]
    for i, (u, v) in enumerate(edges):
        if mask >> i & 1:
            adjacency[u].append((v, i))
            adjacency[v].append((u, i))
    order = [-1] * n
    low = [0] * n
    stack, components = [], []
    clock = 0
    def dfs(u, parent_edge):
        nonlocal clock
        order[u] = low[u] = clock
        clock += 1
        for v, eid in adjacency[u]:
            if eid == parent_edge:
                continue
            if order[v] == -1:
                stack.append(eid)
                dfs(v, eid)
                low[u] = min(low[u], low[v])
                if low[v] >= order[u]:
                    block = []
                    while True:
                        take = stack.pop()
                        block.append(take)
                        if take == eid:
                            break
                    components.append(block)
            elif order[v] < order[u]:
                stack.append(eid)
                low[u] = min(low[u], order[v])
    for u in range(n):
        if order[u] == -1:
            dfs(u, -1)
    potential = 0
    for block in components:
        vertices = set(v for eid in block for v in edges[eid])
        assert len(block) == len(vertices) * (len(vertices) - 1) // 2
        potential += 2 * len(vertices) - 3
    return potential


def check_cut_process(n):
    """Enumerate every reachable graph, not only graphs assumed to be block graphs."""
    edges = tuple(combinations(range(n), 2))
    full = (1 << len(edges)) - 1
    operations = set()
    for protected in range(-1, n):
        for side in range(1, 1 << (n - 1)):
            cut = sum(1 << i for i, (u, v) in enumerate(edges)
                      if u != protected and v != protected
                      and ((side >> u) ^ (side >> v)) & 1)
            if cut:
                operations.add(cut)
    transitions = 0
    @lru_cache(None)
    def dp(mask):
        nonlocal transitions
        potential = blocks(n, edges, mask)
        maximum = 0
        for following in {mask & ~cut for cut in operations if mask & cut}:
            next_potential = blocks(n, edges, following)
            assert next_potential < potential
            maximum = max(maximum, 1 + dp(following))
            transitions += 1
        assert maximum <= potential
        return maximum
    maximum = dp(full)
    assert maximum == 2 * n - 3 if n >= 2 else maximum == 0
    return {'vertices': n, 'maximum_nonempty_operations': maximum,
            'reachable_graphs': dp.cache_info().currsize,
            'transitions': transitions, 'distinct_cut_operations': len(operations)}



def singleton_profile_summary(labels, order, independent):
    """Use only original-basis colors and the localized relevant pairs."""
    queries = 0
    def canonical_basis(failed):
        nonlocal queries
        basis = 0
        for e in order:
            if labels[e] & failed:
                continue
            queries += 1
            if independent(basis | (1 << e)):
                basis |= 1 << e
        return basis
    base = canonical_basis(0)
    touched = 0
    for e in bits(base):
        touched |= labels[e]
    first_bases = {label: canonical_basis(1 << label) for label in bits(touched)}
    retained = base
    for basis in first_bases.values():
        retained |= basis
    extras = retained & ~base
    if not extras:
        return retained, queries, 1 + len(first_bases)
    if extras.bit_count() != 1:
        return None
    protected = next(bits(extras))
    relevant_labels = [label for label, basis in first_bases.items()
                       if basis >> protected & 1]
    if labels[protected]:
        relevant_labels.append(labels[protected].bit_length() - 1)
    pair_count = 0
    for left, right in combinations(relevant_labels, 2):
        retained |= canonical_basis((1 << left) | (1 << right))
        pair_count += 1
    return retained, queries, 1 + len(first_bases) + pair_count


def verify(rank, labels, order, counts, sharp=False):
    n = len(labels)
    ground = (1 << n) - 1
    full_rank = rank(ground)
    universe = 0
    for label in labels:
        universe |= label
    def greedy(failed):
        prefix = basis = 0
        for e in order:
            if labels[e] & failed:
                continue
            enlarged = prefix | (1 << e)
            if rank(enlarged) > rank(prefix):
                basis |= 1 << e
            prefix = enlarged
        return basis
    base = greedy(0)
    single = {label: greedy(1 << label) for label in bits(universe)}
    h1 = base
    for basis in single.values():
        h1 |= basis
    if (h1 & ~base).bit_count() > 1:
        return
    h2 = h1
    basis_by_failure = {}
    for failed in all_failures(universe):
        if failed.bit_count() <= 2:
            basis_by_failure[failed] = greedy(failed)
            h2 |= basis_by_failure[failed]
    answer = singleton_profile_summary(labels, order, lambda mask: rank(mask) == mask.bit_count())
    require(answer is not None, 'observed profile belongs to the algorithm domain')
    retained, queries, scans = answer
    require(retained == h2, 'localized pair algorithm returns the exact canonical union')
    require(queries <= n * scans, 'one independence query per surviving item per scan')
    counts['profile_algorithm_queries'] += queries
    counts['profile_algorithm_scans'] += scans
    counts['all_profile_instances'] += 1
    base_colors = set(labels[e] for e in bits(base)) - {0}
    if h1 == base:
        require(h2 == base, 'zero replacement profile needs no two-failure extras')
        require(scans == 1 + len(base_colors), 'zero profile scan bound')
        counts['zero_extra_instances'] += 1
        return
    x = next(bits(h1 & ~base))
    witness_labels = tuple(label for label, basis in single.items() if basis >> x & 1)
    total = len(witness_labels)
    require(total > 0, 'positive singleton multiplicity')
    pair_labels = total + bool(labels[x])
    require(scans == 1 + len(base_colors) + pair_labels * (pair_labels - 1) // 2,
            'profile-sensitive scan bound')
    bound = full_rank + 2 * total
    if not labels[x]:
        bound = full_rank + 1 + max(0, 2 * total - 3)
    require(h2.bit_count() <= bound, 'singleton replacement size theorem')
    if sharp:
        require(h2 == ground and h2.bit_count() == bound, 'sharp singleton fixture')
        counts['sharp_instances'] += 1
    extras = [e for e in order if h2 >> e & 1 and not h1 >> e & 1]
    require(all(order.index(e) > order.index(x) for e in extras), 'no pair-only item before x')
    promoted = tuple(bits(base)) + tuple(e for e in order if not base >> e & 1)
    for failed, old_basis in basis_by_failure.items():
        prefix = new_basis = 0
        for e in promoted:
            if labels[e] & failed:
                continue
            enlarged = prefix | (1 << e)
            if rank(enlarged) > rank(prefix):
                new_basis |= 1 << e
            prefix = enlarged
        require(new_basis == old_basis, 'promoting the always-accepted base changes no query basis')
        counts['promotion_queries'] += 1
    circuit = [e for e in bits(base) if rank((base ^ (1 << e)) | (1 << x)) == full_rank]
    representatives = {}
    for label in witness_labels:
        representatives[label] = next(e for e in circuit if labels[e] == 1 << label)
    selected = sum(1 << e for e in representatives.values())
    contracted = base & ~selected
    quotient_circuit = selected | (1 << x)
    for e in bits(quotient_circuit):
        require(rank(contracted | (quotient_circuit ^ (1 << e))) == full_rank,
                'contracted core is a circuit')
    vertex_labels = list(witness_labels)
    if labels[x]:
        vertex_labels.append(labels[x].bit_length() - 1)
    edge_vertices = tuple(combinations(range(len(vertex_labels)), 2))
    failures = tuple((1 << vertex_labels[a]) | (1 << vertex_labels[b]) for a, b in edge_vertices)
    relevant = set(failures)
    for failed, basis in basis_by_failure.items():
        require(not basis & ~h1 or failed in relevant, 'only relevant pairs can add new items')
        require((basis & ~h1).bit_count() <= 1, 'each pair has at most one later winner')
    for failed in failures:
        original_core = survivors(h1, labels, failed)
        quotient_core = contracted | survivors(quotient_circuit, labels, failed)
        counts['failed_contracted_item_queries'] += bool(contracted & ~survivors(contracted, labels, failed))
        for e in bits(ground & ~h1):
            if labels[e] & failed:
                continue
            original_increment = rank(original_core | (1 << e)) > rank(original_core)
            quotient_increment = rank(quotient_core | (1 << e)) > rank(quotient_core)
            require(original_increment == quotient_increment, 'pair witness survives contracting possibly failed items')
            counts['quotient_equivalences'] += 1
    unresolved = (1 << len(failures)) - 1
    old_potential = blocks(len(vertex_labels), edge_vertices, unresolved)
    for e in extras:
        winners = 0
        for edge, failed in enumerate(failures):
            if not unresolved >> edge & 1 or labels[e] & failed:
                continue
            core = survivors(h1, labels, failed)
            if rank(core | (1 << e)) > rank(core):
                winners |= 1 << edge
        require(winners, 'every pair-only item wins an unresolved query')
        unresolved &= ~winners
        next_potential = blocks(len(vertex_labels), edge_vertices, unresolved)
        require(next_potential < old_potential, 'clique-block potential decreases')
        old_potential = next_potential
        counts['graph_potential_steps'] += 1
    counts['instances'] += 1
    counts['unlabelled_replacement_instances'] += labels[x] == 0
    counts['repeated_base_label_instances'] += any(sum(labels[e] == 1 << label for e in bits(base)) >= 2 for label in bits(universe))


def binary_rank(vectors):
    @lru_cache(None)
    def rank(mask):
        pivots = {}
        for e in bits(mask):
            vector = vectors[e]
            while vector:
                pivot = vector.bit_length() - 1
                if pivot in pivots:
                    vector ^= pivots[pivot]
                else:
                    pivots[pivot] = vector
                    break
        return len(pivots)
    return rank


def main():
    require(__debug__, 'do not disable assertions')
    small = Counter()
    for n in range(5):
        for ranks in all_matroid_rank_tables(n):
            for labels in product((0,1,2,4), repeat=n):
                verify(ranks.__getitem__, labels, tuple(range(n)), small)
    n = len(ITEMS)
    ranks = [0] * (1 << n)
    for mask in range(1, len(ranks)):
        ranks[mask] = mask.bit_count() if obstruction_independent(mask) else max(ranks[mask ^ (1 << e)] for e in bits(mask))
    original_colors = tuple(ord(color)-ord('A') for _, color in ITEMS)
    fixture = Counter()
    natural = tuple(range(n))
    orders = {natural[shift:] + natural[:shift] for shift in range(n)}
    orders |= {tuple(reversed(order)) for order in tuple(orders)}
    for mapping in product((0,1,2,4), repeat=4):
        labels = tuple(mapping[color] for color in original_colors)
        for order in sorted(orders):
            verify(ranks.__getitem__, labels, order, fixture)
    rng = random.Random(20261026)
    for _ in range(4000):
        labels = tuple(rng.choice((0,1,2,4,8,16)) for _ in range(n))
        order = list(natural)
        rng.shuffle(order)
        verify(ranks.__getitem__, labels, tuple(order), fixture)
    constructed = Counter()
    for total in range(1,9):
        for extra_coloops in range(4):
            vectors = [1 << i for i in range(total + extra_coloops)]
            labels = [1 << i for i in range(total)] + [0] * extra_coloops
            xcolor = 1 << total
            vectors.append((1 << total) - 1)
            labels.append(xcolor)
            for i in range(total - 1):
                vectors.append(1 << i)
                labels.append(xcolor)
            for i in range(total):
                vectors.append(1 << i)
                labels.append(1 << ((i+1)%total) if total >= 2 else 1 << (total+1))
            verify(binary_rank(tuple(vectors)), tuple(labels), tuple(range(len(vectors))), constructed, sharp=True)
    # Rank drops with several original basis items of each failed color;
    # contraction includes some of the actually failed items.
    for sizes in ((2,2),(1,2,3),(3,2,2,1)):
        groups, offset = [], 0
        for size in sizes:
            groups.append(sum(1 << i for i in range(offset,offset+size)))
            offset += size
        total = len(groups)
        for labelled_x in (False, True):
            vectors = [1 << i for i in range(offset)]
            labels = [1 << j for j,size in enumerate(sizes) for _ in range(size)]
            xcolor = 1 << total
            vectors.append((1 << offset)-1)
            labels.append(xcolor if labelled_x else 0)
            for j, group in enumerate(groups):
                vectors.append(group)
                labels.append(xcolor if labelled_x else 1 << ((j+1)%total))
            for j, group in enumerate(groups):
                vectors.append(group)
                labels.append(1 << ((j+1)%total))
            verify(binary_rank(tuple(vectors)), tuple(labels), tuple(range(len(vectors))), constructed)
    print(json.dumps({'status':'passed','small_matroids':dict(small),'nonrepresentable_coarsenings_and_samples':dict(fixture),'linear_constructions':dict(constructed),'graph_cut_process':[check_cut_process(n) for n in range(2,7)]}, indent=2))

if __name__ == '__main__':
    main()
