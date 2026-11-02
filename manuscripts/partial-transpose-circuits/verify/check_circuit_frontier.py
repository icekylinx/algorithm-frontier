#!/usr/bin/env python3
# Copyright 2026 icekylinx and GPT-6 Astra Pro. Apache-2.0.
# Adapted from tcs_research_checkpoint.zip: verification/circuit_frontier/check_circuit_frontier.py
"""Exact checks of the balanced marked-DAG frontier identity.

The tests exercise the new context construction, not the asymptotic
crossing-rank theorem. Only the Python standard library is required.
"""
from collections import Counter
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
import json
import random
import time


def add_poly(left, right, modulus=None):
    answer = dict(left)
    for monomial, coefficient in right.items():
        value = answer.get(monomial, 0) + coefficient
        if modulus is not None:
            value %= modulus
        if value:
            answer[monomial] = value
        else:
            answer.pop(monomial, None)
    return answer


def mul_poly(left, right, modulus=None):
    answer = {}
    for monomial_a, coefficient_a in left.items():
        scope_a = {t for t, _ in monomial_a}
        for monomial_b, coefficient_b in right.items():
            assert scope_a.isdisjoint(t for t, _ in monomial_b)
            monomial = tuple(sorted(monomial_a + monomial_b))
            value = answer.get(monomial, 0) + coefficient_a * coefficient_b
            if modulus is not None:
                value %= modulus
            if value:
                answer[monomial] = value
            else:
                answer.pop(monomial, None)
    return answer


@dataclass
class Node:
    operation: str
    scope: frozenset
    children: tuple
    data: object
    value: dict


class Circuit:
    def __init__(self):
        self.nodes = []
        self.scalar_cache = {}
        self.variables = {}

    def append(self, node):
        for monomial in node.value:
            assert frozenset(t for t, _ in monomial) == node.scope
        self.nodes.append(node)
        return len(self.nodes) - 1

    def scalar(self, value):
        if value not in self.scalar_cache:
            self.scalar_cache[value] = self.append(Node(
                "scalar", frozenset(), (), value,
                {(): value} if value else {}))
        return self.scalar_cache[value]

    def variable(self, block, coordinate):
        key = (block, coordinate)
        if key not in self.variables:
            self.variables[key] = self.append(Node(
                "variable", frozenset([block]), (), key, {(key,): 1}))
        return self.variables[key]

    def add(self, left, right):
        a, b = self.nodes[left], self.nodes[right]
        assert a.scope == b.scope
        return self.append(Node("add", a.scope, (left, right), None,
                                add_poly(a.value, b.value)))

    def multiply(self, left, right):
        a, b = self.nodes[left], self.nodes[right]
        assert a.scope.isdisjoint(b.scope)
        return self.append(Node("multiply", a.scope | b.scope,
                                (left, right), None,
                                mul_poly(a.value, b.value)))

    def scale(self, root, scalar):
        return self.multiply(self.scalar(scalar), root)


def marked_frontier(circuit, root):
    """Build all contexts using shared circuit gates, in reverse DAG order."""
    original_size = len(circuit.nodes)
    universe = circuit.nodes[root].scope
    dimension = len(universe)
    assert dimension >= 2
    contexts = {root: circuit.scalar(1)}
    frontier = []
    traversed = 0

    def propagate(child, context):
        assert circuit.nodes[context].scope == universe - circuit.nodes[child].scope
        if child in contexts:
            contexts[child] = circuit.add(contexts[child], context)
        else:
            contexts[child] = context

    for gate in range(original_size - 1, -1, -1):
        if gate not in contexts:
            continue
        node = circuit.nodes[gate]
        context = contexts[gate]
        assert circuit.nodes[context].scope == universe - node.scope
        traversed += 1
        if 3 * len(node.scope) <= 2 * dimension:
            assert dimension <= 3 * len(node.scope)
            frontier.append((gate, context))
        elif node.operation == "add":
            for child in node.children:
                propagate(child, context)
        else:
            assert node.operation == "multiply"
            first, second = node.children
            if len(circuit.nodes[first].scope) < len(circuit.nodes[second].scope):
                first, second = second, first
            propagate(first, circuit.multiply(context, second))
    assert frontier
    assert len(frontier) <= original_size
    assert len(circuit.nodes) <= 4 * original_size + 1
    total = {}
    for gate, context in frontier:
        total = add_poly(total, mul_poly(circuit.nodes[gate].value,
                                         circuit.nodes[context].value))
    assert total == circuit.nodes[root].value
    return frontier, original_size, traversed


def evaluate_modulo(circuit, prime):
    values = []
    for node in circuit.nodes:
        if node.operation == "scalar":
            value = node.data % prime
            values.append({(): value} if value else {})
        elif node.operation == "variable":
            values.append({(node.data,): 1})
        elif node.operation == "add":
            left, right = node.children
            values.append(add_poly(values[left], values[right], prime))
        else:
            left, right = node.children
            values.append(mul_poly(values[left], values[right], prime))
    return values


def verify_frontier(circuit, root):
    frontier, original_size, traversed = marked_frontier(circuit, root)
    for prime in [2, 3, 101]:
        values = evaluate_modulo(circuit, prime)
        total = {}
        for gate, context in frontier:
            total = add_poly(total, mul_poly(values[gate], values[context], prime), prime)
        assert total == values[root]
    return frontier, original_size, traversed


def random_shared_circuit(rng, dimension, trial):
    circuit = Circuit()
    by_scope = {}

    def build(scope):
        scope = frozenset(scope)
        existing = by_scope.get(scope, [])
        if existing and rng.random() < 0.45:
            return rng.choice(existing)
        ordered = sorted(scope)
        if len(scope) == 1:
            root = circuit.variable(ordered[0], rng.randrange(4))
            if rng.random() < 0.6:
                other = circuit.variable(ordered[0], rng.randrange(4))
                root = circuit.add(root, circuit.scale(other, rng.choice([-2, -1, 0, 1, 2])))
        else:
            shuffled = ordered[:]
            rng.shuffle(shuffled)
            cut = rng.randrange(1, len(shuffled))
            root = circuit.multiply(build(shuffled[:cut]), build(shuffled[cut:]))
            if rng.random() < 0.45:
                rng.shuffle(shuffled)
                cut = rng.randrange(1, len(shuffled))
                other = circuit.multiply(build(shuffled[:cut]), build(shuffled[cut:]))
                root = circuit.add(root, circuit.scale(other, rng.choice([-2, -1, 0, 1, 2])))
        if rng.random() < 0.35:
            root = circuit.scale(root, rng.choice([-2, -1, 0, 1, 2, 3]))
        by_scope.setdefault(scope, []).append(root)
        return root

    root = build(range(dimension))
    # Repeated references, long sum chains and characteristic-sensitive
    # cancellations are intentionally present in every test family.
    shared = root
    for _ in range(3 + trial % 9):
        root = circuit.add(root, circuit.scale(shared, rng.choice([-2, -1, 0, 1, 2, 3])))
    if trial % 11 == 0:
        root = circuit.add(root, circuit.scale(root, -1))
        assert not circuit.nodes[root].value
    return circuit, root


def negative_frontier_control():
    circuit = Circuit()
    roots = [circuit.variable(t, 0) for t in range(4)]
    left = circuit.multiply(roots[0], roots[1])
    right = circuit.multiply(roots[2], roots[3])
    root = circuit.multiply(left, right)
    # Taking BOTH balanced children with their full contexts gives 2f.
    bad = add_poly(mul_poly(circuit.nodes[left].value, circuit.nodes[right].value),
                   mul_poly(circuit.nodes[right].value, circuit.nodes[left].value))
    assert bad != circuit.nodes[root].value
    assert not {m: c % 2 for m, c in bad.items() if c % 2}
    assert circuit.nodes[root].value
    frontier, _, _ = verify_frontier(circuit, root)
    assert len(frontier) == 1


def varying_partition_orientation_control():
    # Three distinct pair partitions on the same four-site coefficient
    # matrix. Each contributes exactly once to every global orientation.
    universe = set(range(4))
    counts = Counter()
    for first in [{0, 1}, {0, 2}, {0, 3}]:
        second = universe - first
        local_seen = Counter()
        for alpha in range(16):
            if alpha & 1 or any(alpha >> t & 1 for t in second):
                continue
            for beta in range(16):
                if beta >> min(second) & 1 or any(beta >> t & 1 for t in first):
                    continue
                for epsilon in [0, 1]:
                    second_mask = sum(1 << t for t in second)
                    parent = alpha | (beta ^ (epsilon * second_mask))
                    assert not parent & 1
                    local_seen[parent] += 1
        assert len(local_seen) == 8 and set(local_seen.values()) == {1}
        counts.update(local_seen)
    assert len(counts) == 8 and set(counts.values()) == {3}
    return 24


def main():
    if not __debug__:
        raise SystemExit("Run without -O: these exact checks use assertions.")
    started = time.monotonic()
    rng = random.Random(202611020349)
    cases = 0
    zero_roots = 0
    nonzero_roots = 0
    frontier_calls = 0
    max_original_size = 0
    max_frontier = 0
    total_context_gates = 0
    for dimension in range(2, 7):
        for trial in range(32):
            circuit, root = random_shared_circuit(rng, dimension, trial)
            original_nodes = len(circuit.nodes)
            candidates = [i for i in range(original_nodes)
                          if len(circuit.nodes[i].scope) >= 2]
            selected = [root] + rng.sample(candidates, min(2, len(candidates)))
            for selected_root in selected:
                frontier, original_size, _ = verify_frontier(circuit, selected_root)
                frontier_calls += 1
                max_original_size = max(max_original_size, original_size)
                max_frontier = max(max_frontier, len(frontier))
                total_context_gates += len(circuit.nodes) - original_size
                if circuit.nodes[selected_root].value:
                    nonzero_roots += 1
                else:
                    zero_roots += 1
            # Exercise recursive contexts: a factor's root has a
            # nonconsecutive sub-scope, and its circuit contains shared
            # old coefficients and newly created context gates.
            candidates = [v for pair in frontier for v in pair
                          if len(circuit.nodes[v].scope) >= 2]
            if candidates:
                verify_frontier(circuit, rng.choice(candidates))
                frontier_calls += 1
            cases += 1
    negative_frontier_control()
    orientations = varying_partition_orientation_control()
    assert zero_roots and nonzero_roots
    report = {
        "status": "PASS",
        "run_utc": datetime.now(timezone.utc).isoformat(),
        "elapsed_seconds": round(time.monotonic() - started, 6),
        "shared_dag_instances": cases,
        "frontier_calls": frontier_calls,
        "coefficient_rings_per_call": ["integers", "F2", "F3", "F101"],
        "exact_ring_identities": 4 * frontier_calls,
        "zero_root_checks": zero_roots,
        "nonzero_root_checks": nonzero_roots,
        "maximum_original_gate_count": max_original_size,
        "maximum_frontier_size": max_frontier,
        "created_context_gates_in_primary_checks": total_context_gates,
        "different_partition_orientation_cases": orientations,
        "negative_control": "Naively taking both balanced product children gives 2f, not f; detected over integers and F2.",
        "scope": "Exact finite frontier identities, context scope invariants, O(S) context-size bound, and differing-partition orientation uniqueness. Does not establish the asymptotic crossing theorem or any circuit lower bound.",
    }
    directory = Path(__file__).resolve().parent
    (directory / "frontier_results.json").write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
