"""Exact scenario tests. Attribution: icekylinx and GPT-6 Astra Pro. Apache-2.0."""
from dataclasses import replace
from fractions import Fraction as F
from itertools import combinations, product
from pathlib import Path
from types import SimpleNamespace
import importlib.util
import random
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'reference'))
import scenarios as impl

# This independent path builder/active-set solver calls no backend optimizer.
_check_path = Path(__file__).resolve().parents[2] / 'selected-flow/verify/check_concurrent.py'
_spec = importlib.util.spec_from_file_location('_independent_flow_paths', _check_path)
_paths = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_paths)


def subsets(q):
    return [frozenset(i for i in range(q) if mask >> i & 1) for mask in range(1 << q)]


def reduction(q, blocked):
    x, y = 2*q, 2*q+1
    edges = []
    for i in range(q):
        edges.extend(((2*i, 2*i+1, int(i not in blocked)),
                      (2*i, x, int(i in blocked)), (y, 2*i+1, int(i in blocked))))
    edges.append((x, y, len(blocked)-1))
    return impl.Scenario(impl.Network(2*q+2, tuple(edges), tuple((2*i,2*i+1,1) for i in range(q))))


def check_routing(scenario, selected, primal, rate):
    # Independently read native endpoints, capacities and budgets.
    net = scenario.network
    arcs = [(u,v,e) for e,(u,v,_) in enumerate(net.edges) for u,v in
            (((u,v),(v,u)) if net.undirected else ((u,v),))]
    assert primal[0] == rate and len(primal) == 1+len(selected)*len(arcs)
    assert all(x >= 0 for x in primal)
    loads = [F(0)]*len(net.edges)
    charge = [F(0)]*len(scenario.budgets)
    for k,i in enumerate(selected):
        balances = [F(0)]*net.vertices
        for j,(u,v,e) in enumerate(arcs):
            value = primal[1+k*len(arcs)+j]
            balances[u] += value; balances[v] -= value; loads[e] += value
            for h,(costs,_) in enumerate(scenario.budgets): charge[h] += value*costs[i][j]
        source,target,demand = net.commodities[i]
        assert balances == [rate*demand*((v == source)-(v == target)) for v in range(net.vertices)]
    assert all(load <= cap for load,(_,_,cap) in zip(loads,net.edges))
    assert all(cost <= cap for cost,(_,cap) in zip(charge,scenario.budgets))


def main():
    rng = random.Random(271029)
    native = queries = mutations = 0
    for _ in range(24):
        scenarios = []
        for omega in range(2 + rng.randrange(2)):
            undirected = bool(rng.randrange(2))
            edges = tuple((u,v,F(rng.randrange(4),2)) for u,v in ((0,1),(1,2),(0,2)) if rng.randrange(2))
            net = impl.Network(3,edges,((0,2,F(rng.randrange(1,4),2)),(1,2,F(rng.randrange(1,4),2))),undirected)
            costs = tuple(tuple(F(rng.randrange(3),2) for _ in net.arcs()) for _ in range(2))
            budgets = ((costs,F(rng.randrange(4),2)),) if omega % 2 else ()
            scenarios.append(impl.Scenario(net,budgets))
        for rank in (1,2):
            best = impl.optimize_selected(scenarios,rank)
            expected = max(min(_paths.path_opt(s.network,selected,s.budgets) for s in scenarios)
                           for selected in combinations(range(2),rank))
            assert best.rate == expected and impl.verify_fixed(scenarios,best)
            for scenario, routing in zip(scenarios,best.routings()):
                check_routing(scenario,best.selected,routing,best.rate)
            # Missing/reordered commodity certificates cannot assert a shared choice.
            assert not impl.verify_fixed(scenarios,replace(best,certificates=best.certificates[:-1]))
            bad = replace(best.certificates[0],primal=(best.certificates[0].rate+1,)+best.certificates[0].primal[1:])
            assert not impl.verify_fixed(scenarios,replace(best,certificates=(bad,)+best.certificates[1:]))
            mutations += 2; native += 1
            for rate in (F(0),best.rate,best.rate+F(1,7)):
                rates = tuple(rate if i in best.selected else F(0) for i in range(2))
                result = impl.separate(scenarios,rates)
                assert (result is None) == (rate <= best.rate)
                if result is not None:
                    row = result.row
                    assert all(x >= 0 for x in row.coefficients)
                    assert sum(a*z for a,z in zip(row.coefficients,rates)) > row.capacity
                    # Same row must be valid at a known robust feasible point.
                    assert sum(row.coefficients[i]*best.rate for i in best.selected) <= row.capacity
                queries += 1
    # Each scenario alone can select a rate-ten commodity; no common choice can.
    scenarios = tuple(impl.Scenario(impl.Network(4,((0,1,a),(2,3,b)),((0,1,1),(2,3,1))))
                      for a,b in ((10,1),(1,10)))
    best = impl.optimize_selected(scenarios,1)
    assert best.rate == 1 and best.selected == (0,)
    mixed = impl.Certificate((0,),tuple(impl.flow.optimize_fixed(s.network,(i,),s.budgets) for i,s in enumerate(scenarios)))
    assert mixed.rate == 10 and not impl.verify_fixed(scenarios,mixed)
    assert impl.optimize_selected(scenarios,1,lambda selected: selected == (1,)).rate == 1
    assert impl.optimize_selected(scenarios,1,lambda selected: False) is None
    # Adaptive routing changes with topology: opposite two-edge paths remain legal.
    adaptive = tuple(impl.Scenario(impl.Network(4,edges,((0,3,1),))) for edges in
                     (((0,1,2),(1,3,2)),((0,2,3),(2,3,3))))
    cert = impl.optimize_fixed(adaptive,(0,))
    assert cert.rate == 2 and impl.verify_fixed(adaptive,cert)
    forged = SimpleNamespace(selected=cert.selected, certificates=cert.certificates, rate=F(100))
    assert not impl.verify_fixed(adaptive,forged)
    forged_inner = SimpleNamespace(selected=cert.selected, primal=cert.certificates[0].primal,
                                   dual=cert.certificates[0].dual, rate=F(100))
    assert not impl.verify_fixed(adaptive,replace(cert,certificates=(forged_inner,)+cert.certificates[1:]))
    for s,routing in zip(adaptive,cert.routings()): check_routing(s,(0,),routing,F(2))
    # The verifier performs no optimization.
    saved = impl.flow.simplex
    impl.flow.simplex = lambda *args: (_ for _ in ()).throw(AssertionError('search called'))
    assert impl.verify_fixed(adaptive,cert)
    impl.flow.simplex = saved
    networks = identities = 0
    for q in range(1,4):
        sets = subsets(q)
        for blocked in sets[1:]:
            scenario = reduction(q,blocked)
            # Union-find directly checks the positive-capacity undirected forest.
            parent = list(range(scenario.network.vertices))
            def root(v):
                while parent[v] != v: v = parent[v]
                return v
            for u,v,cap in scenario.network.edges:
                if cap:
                    ru,rv = root(u),root(v)
                    assert ru != rv
                    parent[ru] = rv
            for selected in sets[1:]:
                count = len(selected & blocked)
                expected = min(F(1), F(len(blocked)-1,count)) if count else F(1)
                actual = impl.optimize_fixed((scenario,),tuple(sorted(selected)))
                assert actual.rate == expected and impl.verify_fixed((scenario,),actual)
                check_routing(scenario,actual.selected,actual.routings()[0],expected)
                networks += 1
        for family_mask in range(1 << (len(sets)-1)):
            family = [s for j,s in enumerate(sets[1:]) if family_mask >> j & 1]
            for omitted in sets[:-1]:
                selected = sets[-1]-omitted
                assert all(len(selected & s) <= len(s)-1 for s in family) == all(omitted & s for s in family)
                identities += 1
    invalid = 0
    for thunk in (lambda: impl.optimize_fixed((),(0,)),
                  lambda: impl.optimize_fixed((adaptive[0],scenarios[0]),(0,)),
                  lambda: impl.optimize_selected(adaptive,0),
                  lambda: impl.optimize_fixed(adaptive,()),
                  lambda: impl.Scenario(impl.Network(2,(),())),
                  lambda: impl.Scenario(adaptive[0].network,(((),0),))):
        try: thunk()
        except ValueError: invalid += 1
        else: raise AssertionError('invalid input accepted')
    print(f'PASS: {native} independent native robust path optima; {queries} scenario separation queries; {mutations} mutated certificates; 2 forged certificate types; {networks} Hitting Set network optima and forests; {identities} family admission identities; {invalid} malformed inputs; adaptive/common-choice fixtures; search-free verifier.')


if __name__ == '__main__':
    main()
