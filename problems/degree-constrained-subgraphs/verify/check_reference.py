#!/usr/bin/env python3
"""Finite oracle checks of the unconditional degree-constrained solver.

Enumerate original edge subsets independently of every reduction and matching
routine. Check all small interval/cardinality requests, optimization answers,
native parallel IDs, malformed inputs and corrupted certificates. No external
package is required. This validates finite instances, not asymptotic proofs.
"""
from __future__ import annotations

import argparse
from copy import deepcopy
from itertools import combinations, product
import json
from pathlib import Path
import random
import subprocess
import sys
import tempfile

REFERENCE = Path(__file__).resolve().parents[1] / "reference"
sys.path.insert(0, str(REFERENCE))
from degree_reduction import normalize, reduce_interval
from degree_subgraph import degree_subgraph
from verify_degree import verify_degree_result


def original_subsets(n, edges):
    output = []
    for mask in range(1 << len(edges)):
        degree = [0]*n
        for index, (u, v) in enumerate(edges):
            if mask >> index & 1:
                degree[u] += 1
                degree[v] += 1
        output.append((mask.bit_count(), degree))
    return output


def feasible_sizes(subsets, lower, upper, interval):
    return {size for size, degree in subsets
            if interval[0] <= size <= interval[1]
            and all(g <= d <= f for g, d, f in zip(lower, degree, upper))}


def check_one(n, edges, lower, upper, interval, objective, counters, subsets=None, ids=None):
    subsets = original_subsets(n, edges) if subsets is None else subsets
    expected = feasible_sizes(subsets, lower, upper, interval)
    result = degree_subgraph(n, edges, lower, upper, ids, interval, objective)
    assert (result['status'] == 'YES') == bool(expected), (n, edges, lower, upper, interval, objective)
    if expected:
        actual = result['cardinality']
        assert actual in expected
        if objective == 'minimum':
            assert actual == min(expected)
        if objective == 'maximum':
            assert actual == max(expected)
    report = verify_degree_result(n, edges, result, lower, upper, ids, interval, objective)
    assert report['verified']
    counters['solves'] += 1
    counters['matching_calls'] += result['statistics']['matching_calls']
    counters['no_results'] += result['status'] == 'NO'
    counters['optimization_results'] += result['status'] == 'YES' and objective != 'feasible'
    return result


def reject(call):
    try:
        call()
    except ValueError:
        return
    raise AssertionError('malformed input or corrupted certificate was accepted')


def main():
    if not __debug__:
        raise SystemExit('Run this mathematical checker without -O or PYTHONOPTIMIZE.')
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--checkpoint', type=Path)
    parser.add_argument('--random-cases', type=int, default=120)
    args = parser.parse_args()
    if args.random_cases < 0:
        raise ValueError('random case count must be nonnegative')
    counters = dict(solves=0, matching_calls=0, no_results=0,
                    optimization_results=0, sparse_reductions=0,
                    rejected_inputs=0, rejected_certificates=0, cli_cases=0)

    def checkpoint(phase):
        if args.checkpoint:
            args.checkpoint.write_text(json.dumps(dict(status=phase, **counters), indent=2)+'\n')

    graphs = []
    for n in range(4):
        possible = list(combinations(range(n), 2))
        for mask in range(1 << len(possible)):
            graphs.append((n, [edge for index, edge in enumerate(possible) if mask >> index & 1]))
    graphs.extend(((2, [(0,1),(0,1)]), (3, [(0,1),(0,1),(1,2)])))
    for n, edges in graphs:
        degree = [0]*n
        for u, v in edges:
            degree[u] += 1
            degree[v] += 1
        subsets = original_subsets(n, edges)
        choices = [[(g,f) for f in range(d+1) for g in range(f+1)] for d in degree]
        ids = [f'record-{i}' if i % 2 else -i-1 for i in range(len(edges))]
        for bounds in product(*choices):
            lower, upper = [g for g,_ in bounds], [f for _,f in bounds]
            for objective in ('feasible', 'minimum', 'maximum'):
                check_one(n, edges, lower, upper, (0,len(edges)), objective, counters, subsets, ids)
            for low in range(len(edges)+1):
                for high in range(low, len(edges)+1):
                    check_one(n, edges, lower, upper, (low,high), 'feasible', counters, subsets, ids)
                    reduced = reduce_interval(normalize(n, edges, lower, upper, ids, (low,high)), low, high)
                    if reduced.failure is None:
                        pairs = [tuple(sorted(edge)) for edge in reduced.edges]
                        assert len(pairs) == len(set(pairs))
                        assert all(u != v for u,v in pairs)
                        reduced_degree = [0]*reduced.n
                        for u,v in reduced.edges:
                            reduced_degree[u] += 1
                            reduced_degree[v] += 1
                        assert max(reduced_degree, default=0) <= 3
                        assert len(reduced.native_index) == len(reduced.edges)
                        counters['sparse_reductions'] += 1
    checkpoint('exhaustive_small_requests_complete')

    rng = random.Random(0xDE6E2026)
    for index in range(args.random_cases):
        n = 2 + index % 6
        edges = []
        for _ in range(index % 11):
            u, v = rng.sample(range(n), 2)
            edges.append((u,v))
        degree = [0]*n
        for u,v in edges:
            degree[u] += 1
            degree[v] += 1
        upper = [rng.randrange(d+3) for d in degree]
        lower = [rng.randrange(f+1) for f in upper]
        low, high = sorted((rng.randrange(-1,len(edges)+2), rng.randrange(-1,len(edges)+2)))
        ids = [f'edge:{index}:{i}' if i%2 else -(10**40+i) for i in range(len(edges))]
        subsets = original_subsets(n, edges)
        for objective in ('feasible','minimum','maximum'):
            check_one(n, edges, lower, upper, (low,high), objective, counters, subsets, ids)
    checkpoint('native_seeded_requests_complete')

    # Every simple four-vertex graph, with four independent degree requests.
    possible = list(combinations(range(4),2))
    for mask in range(1 << len(possible)):
        edges = [edge for i,edge in enumerate(possible) if mask >> i & 1]
        degree = [sum(v in edge for edge in edges) for v in range(4)]
        subsets = original_subsets(4, edges)
        for _ in range(4):
            upper = [rng.randrange(d+1) for d in degree]
            lower = [rng.randrange(f+1) for f in upper]
            for objective in ('feasible','minimum','maximum'):
                check_one(4, edges, lower, upper, (0,len(edges)), objective, counters, subsets)
    checkpoint('four_vertex_graphs_complete')

    # Large isolated universe and long numeric encodings never enter a selector.
    result = degree_subgraph(10001, [(0,1),(0,1)], upper=[1,1]+[0]*9999,
                             edge_ids=['first','second'], objective='maximum')
    assert result['cardinality'] == 1
    assert result['statistics']['maximum_reduced_vertices'] < 1000
    verify_degree_result(10001, [(0,1),(0,1)], result, upper=[1,1]+[0]*9999,
                         edge_ids=['first','second'], objective='maximum')
    check_one(3, [(0,1),(1,2)], [0,0,0], [1<<500]*3, (0,2), 'maximum', counters)
    check_one(3, [(0,1)], [0,0,1<<500], [1<<600]*3, (0,1), 'feasible', counters)

    malformed = [
        dict(n=True, edges=[]), dict(n=-1, edges=[]), dict(n=1, edges=[(0,0)]),
        dict(n=2, edges=[(0,2)]), dict(n=2, edges=[(False,1)]),
        dict(n=2, edges=[(0,)]), dict(n=2, edges=[(0,1)], lower=[0]),
        dict(n=2, edges=[(0,1)], upper=[1,-1]),
        dict(n=2, edges=[(0,1)], lower=[False,0]),
        dict(n=2, edges=[(0,1)], edge_ids=[True]),
        dict(n=2, edges=[(0,1),(0,1)], edge_ids=['same','same']),
        dict(n=2, edges=[(0,1)], edge_ids=[]),
        dict(n=2, edges=[(0,1)], cardinality=[0,True]),
        dict(n=2, edges=[(0,1)], cardinality=[0]),
        dict(n=2, edges=[(0,1)], objective='weighted'),
    ]
    for request in malformed:
        reject(lambda request=request: degree_subgraph(**request))
        counters['rejected_inputs'] += 1

    # This maximum has an interior optimum and a nontrivial matching NO proof.
    request = dict(n=4, edges=[(0,1),(0,2),(0,3)], lower=[0]*4, upper=[1]*4,
                   edge_ids=['a','b','c'], objective='maximum')
    valid = degree_subgraph(**request)
    assert valid['certificate']['optimality']['infeasibility']['kind'] == 'matching'
    mutations = []
    def changed(edit):
        copy = deepcopy(valid)
        edit(copy)
        mutations.append(copy)
    changed(lambda x: x.update(cardinality=2))
    changed(lambda x: x.update(degrees=[0]*4))
    changed(lambda x: x.update(objective='minimum'))
    changed(lambda x: x['selected_edges'][0].update(id='wrong'))
    changed(lambda x: x['selected_edges'][0].update(input_index=True))
    changed(lambda x: x['selected_edges'][0].update(u=3))
    changed(lambda x: x['certificate'].update(format='unknown'))
    changed(lambda x: x['certificate'].pop('optimality'))
    changed(lambda x: x['certificate'].update(optimality={'kind':'endpoint'}))
    changed(lambda x: x['certificate']['optimality'].update(cardinality=[3,3]))
    changed(lambda x: x['certificate']['optimality'].pop('infeasibility'))
    changed(lambda x: x['certificate']['optimality']['infeasibility']['matching_result'].update(cardinality=0))
    changed(lambda x: x['certificate']['optimality']['infeasibility']['matching_result']['certificate'].update(components=[]))
    for corrupted in mutations:
        reject(lambda corrupted=corrupted: verify_degree_result(result=corrupted, **request))
        counters['rejected_certificates'] += 1

    # Repeated records are invalid even when their endpoints legitimately repeat.
    duplicate_request = dict(n=2, edges=[(0,1),(0,1)], lower=[2,2], upper=[2,2])
    duplicate_result = degree_subgraph(**duplicate_request)
    duplicate_result['selected_edges'][1] = deepcopy(duplicate_result['selected_edges'][0])
    reject(lambda: verify_degree_result(result=duplicate_result, **duplicate_request))
    counters['rejected_certificates'] += 1
    local_request = dict(n=3, edges=[(0,1)], lower=[0,0,1])
    local_result = degree_subgraph(**local_request)
    local_result['certificate']['infeasibility']['reason'] = {'reason':'fabricated'}
    reject(lambda: verify_degree_result(result=local_result, **local_request))
    counters['rejected_certificates'] += 1

    # Production acceptance uses explicit checks and works with assertions off.
    with tempfile.TemporaryDirectory() as temporary:
        directory = Path(temporary)
        graph_path, result_path = directory/'input.json', directory/'result.json'
        graph_path.write_text(json.dumps(request))
        output = subprocess.run([sys.executable,'-O',str(REFERENCE/'degree_subgraph.py'),str(graph_path)],
                                 text=True, capture_output=True, check=True)
        result_path.write_text(output.stdout)
        checked = subprocess.run([sys.executable,'-O',str(REFERENCE/'verify_degree.py'),
                                  str(graph_path),str(result_path)],
                                 text=True, capture_output=True, check=True)
        assert json.loads(checked.stdout)['optimality_verified']
        counters['cli_cases'] += 2
    checkpoint('PASS')
    print('PASS:', json.dumps(counters, sort_keys=True))
    print('Scope: finite original-edge-subset oracles and certificate rejection; no fast-backend claim.')


if __name__ == '__main__':
    main()
