#!/usr/bin/env python3
# Copyright 2026 icekylinx and GPT-6 Astra Pro. Apache-2.0.
# Adapted from tcs_research_checkpoint.zip: verification/circuit_frontier/check_homogeneous_projection.py
"""Exact homogeneous-frontier and lazy squarefree-projection checks.

Unlike the set-multilinear validator, these circuits may reuse the same
variable block within a product or square a shared subcircuit. The tests
also allow zero gates carrying a positive formal homogeneous degree.
"""
from dataclasses import dataclass
from datetime import datetime, timezone
from itertools import combinations
from pathlib import Path
import json
import random
import time

from check_circuit_frontier import add_poly


def multiply(left, right, modulus=None):
    answer = {}
    for a, ca in left.items():
        for b, cb in right.items():
            monomial = tuple(sorted(a + b))
            coefficient = answer.get(monomial, 0) + ca * cb
            if modulus is not None:
                coefficient %= modulus
            if coefficient:
                answer[monomial] = coefficient
            else:
                answer.pop(monomial, None)
    return answer


def squarefree_projection(polynomial, blocks):
    blocks = frozenset(blocks)
    return {monomial: coefficient for monomial, coefficient in polynomial.items()
            if len(monomial) == len(blocks)
            and frozenset(t for t, _ in monomial) == blocks}


@dataclass
class Node:
    operation: str
    degree: int
    children: tuple
    data: object
    value: dict


class Circuit:
    def __init__(self):
        self.nodes = []

    def append(self, node):
        assert all(len(monomial) == node.degree for monomial in node.value)
        self.nodes.append(node)
        return len(self.nodes) - 1

    def scalar(self, value):
        return self.append(Node("scalar", 0, (), value,
                                {(): value} if value else {}))

    def zero(self, degree):
        return self.append(Node("zero", degree, (), None, {}))

    def variable(self, block, coordinate):
        return self.append(Node("variable", 1, (), (block, coordinate),
                                {((block, coordinate),): 1}))

    def add(self, left, right):
        a, b = self.nodes[left], self.nodes[right]
        assert a.degree == b.degree
        return self.append(Node("add", a.degree, (left, right), None,
                                add_poly(a.value, b.value)))

    def multiply(self, left, right):
        a, b = self.nodes[left], self.nodes[right]
        return self.append(Node("multiply", a.degree + b.degree,
                                (left, right), None,
                                multiply(a.value, b.value)))

    def scale(self, root, value):
        return self.multiply(self.scalar(value), root)


def frontier(circuit, root):
    old_size = len(circuit.nodes)
    degree = circuit.nodes[root].degree
    assert degree >= 2
    contexts = {root: circuit.scalar(1)}
    factors = []

    def send(child, context):
        assert circuit.nodes[context].degree == degree - circuit.nodes[child].degree
        if child in contexts:
            contexts[child] = circuit.add(contexts[child], context)
        else:
            contexts[child] = context

    for gate in range(old_size - 1, -1, -1):
        if gate not in contexts:
            continue
        node = circuit.nodes[gate]
        context = contexts[gate]
        assert circuit.nodes[context].degree == degree - node.degree
        if node.operation == "zero":
            continue
        if 3 * node.degree <= 2 * degree:
            assert degree <= 3 * node.degree
            factors.append((gate, context))
        elif node.operation == "add":
            for child in node.children:
                send(child, context)
        else:
            assert node.operation == "multiply"
            left, right = node.children
            if circuit.nodes[left].degree < circuit.nodes[right].degree:
                left, right = right, left
            send(left, circuit.multiply(context, right))
    assert len(circuit.nodes) <= 4 * old_size + 1
    total = {}
    for left, right in factors:
        total = add_poly(total, multiply(circuit.nodes[left].value,
                                        circuit.nodes[right].value))
    assert total == circuit.nodes[root].value
    return factors, old_size


def modular_values(circuit, modulus):
    values = []
    for node in circuit.nodes:
        if node.operation == "zero":
            values.append({})
        elif node.operation == "scalar":
            value = node.data % modulus
            values.append({(): value} if value else {})
        elif node.operation == "variable":
            values.append({(node.data,): 1})
        elif node.operation == "add":
            a, b = node.children
            values.append(add_poly(values[a], values[b], modulus))
        else:
            a, b = node.children
            values.append(multiply(values[a], values[b], modulus))
    return values


def verify(circuit, root, blocks):
    blocks = frozenset(blocks)
    assert len(blocks) == circuit.nodes[root].degree
    factors, old_size = frontier(circuit, root)
    projections = 0
    overlapping_products = 0
    for modulus in [None, 2, 3, 101]:
        values = ([node.value for node in circuit.nodes] if modulus is None
                  else modular_values(circuit, modulus))
        ordinary = {}
        projected_sum = {}
        for left, right in factors:
            product = multiply(values[left], values[right], modulus)
            ordinary = add_poly(ordinary, product, modulus)
            if any(len({t for t, _ in monomial}) < len(monomial)
                   for monomial in product):
                overlapping_products += 1
            expected = squarefree_projection(product, blocks)
            actual = {}
            k = circuit.nodes[left].degree
            for subset in combinations(sorted(blocks), k):
                first = frozenset(subset)
                second = blocks - first
                # Projection itself discards all variables outside the
                # target scope, exactly as restriction followed by SF.
                a = squarefree_projection(values[left], first)
                b = squarefree_projection(values[right], second)
                actual = add_poly(actual, multiply(a, b, modulus), modulus)
            assert actual == expected
            projected_sum = add_poly(projected_sum, actual, modulus)
            projections += 1
        assert ordinary == values[root]
        assert projected_sum == squarefree_projection(values[root], blocks)
    return factors, old_size, projections, overlapping_products


def restricted_copy(circuit, blocks):
    """Retain formal degrees when variables outside a scope become zero."""
    blocks = frozenset(blocks)
    copied = Circuit()
    for node in circuit.nodes:
        if node.operation == "zero":
            copied.zero(node.degree)
        elif node.operation == "scalar":
            copied.scalar(node.data)
        elif node.operation == "variable":
            block, coordinate = node.data
            if block in blocks:
                copied.variable(block, coordinate)
            else:
                copied.zero(1)
        elif node.operation == "add":
            copied.add(*node.children)
        else:
            copied.multiply(*node.children)
    return copied


def random_circuit(rng, degree, trial):
    circuit = Circuit()
    by_degree = {}
    universe = frozenset(range(1, degree + 1))

    def build(k):
        previous = by_degree.get(k, [])
        if previous and rng.random() < 0.4:
            return rng.choice(previous)
        if rng.random() < 0.07:
            root = circuit.zero(k)
        elif k == 1:
            root = circuit.variable(rng.randrange(degree + 2), rng.randrange(3))
            if rng.random() < 0.7:
                other = circuit.variable(rng.randrange(degree + 2), rng.randrange(3))
                root = circuit.add(root, circuit.scale(other, rng.choice([-2, -1, 1, 2])))
        elif k % 2 == 0 and rng.random() < 0.45:
            child = build(k // 2)
            root = circuit.multiply(child, child)
        else:
            first = rng.randrange(1, k)
            root = circuit.multiply(build(first), build(k - first))
            if rng.random() < 0.4:
                first = rng.randrange(1, k)
                other = circuit.multiply(build(first), build(k - first))
                root = circuit.add(root, circuit.scale(other, rng.choice([-1, 1, 2])))
        by_degree.setdefault(k, []).append(root)
        return root

    root = build(degree)
    # Plant a squarefree monomial so that overlap tests are not confined
    # to instances with an identically zero squarefree component.
    planted = circuit.scalar(1)
    for block in sorted(universe):
        planted = circuit.multiply(planted, circuit.variable(block, trial % 3))
    root = circuit.add(root, planted)
    shared = root
    for _ in range(3 + trial % 7):
        root = circuit.add(root, circuit.scale(shared, rng.choice([-2, -1, 0, 1, 2])))
    if trial % 13 == 0:
        root = circuit.add(root, circuit.scale(root, -1))
    return circuit, root, universe


def characteristic_two_square_control():
    circuit = Circuit()
    a, b = circuit.variable(0, 0), circuit.variable(1, 0)
    child = circuit.add(a, b)
    root = circuit.multiply(child, child)
    factors, _, _, _ = verify(circuit, root, {0, 1})
    assert len(factors) == 1
    integer_projection = squarefree_projection(circuit.nodes[root].value, {0, 1})
    assert integer_projection == {((0, 0), (1, 0)): 2}
    assert not squarefree_projection(modular_values(circuit, 2)[root], {0, 1})
    # A positive-degree zero leaf must be skipped, not treated as a
    # scalar of degree zero or descended into as a product gate.
    zero = Circuit()
    zero_root = zero.zero(5)
    empty_factors, _, _, _ = verify(zero, zero_root, set(range(5)))
    assert empty_factors == []


def main():
    if not __debug__:
        raise SystemExit("Run without -O: these checks use assertions.")
    started = time.monotonic()
    rng = random.Random(202611020350)
    cases = calls = projections = overlaps = 0
    nonzero_squarefree = zero_squarefree = 0
    maximum_size = maximum_frontier = 0
    restricted_calls = 0
    for degree in range(2, 7):
        for trial in range(32):
            circuit, root, blocks = random_circuit(rng, degree, trial)
            if squarefree_projection(circuit.nodes[root].value, blocks):
                nonzero_squarefree += 1
            else:
                zero_squarefree += 1
            factors, old_size, count, overlap_count = verify(circuit, root, blocks)
            projections += count
            overlaps += overlap_count
            calls += 1
            maximum_size = max(maximum_size, old_size)
            maximum_frontier = max(maximum_frontier, len(factors))
            candidates = [factor for pair in factors for factor in pair
                          if circuit.nodes[factor].degree >= 2]
            if candidates:
                factor = rng.choice(candidates)
                k = circuit.nodes[factor].degree
                chosen_blocks = frozenset(rng.sample(sorted(blocks), k))
                restricted = restricted_copy(circuit, chosen_blocks)
                _, _, count, overlap_count = verify(restricted, factor, chosen_blocks)
                projections += count
                overlaps += overlap_count
                calls += 1
                restricted_calls += 1
            cases += 1
    characteristic_two_square_control()
    assert nonzero_squarefree and zero_squarefree and overlaps
    report = {
        "status": "PASS",
        "run_utc": datetime.now(timezone.utc).isoformat(),
        "elapsed_seconds": round(time.monotonic() - started, 6),
        "homogeneous_shared_dag_instances": cases,
        "frontier_calls": calls,
        "recursive_restricted_factor_calls": restricted_calls,
        "coefficient_rings": ["integers", "F2", "F3", "F101"],
        "exact_frontier_identities": 4 * calls,
        "exact_product_projection_identities": projections,
        "products_with_repeated_blocks_checked": overlaps,
        "nonzero_squarefree_roots": nonzero_squarefree,
        "zero_squarefree_roots": zero_squarefree,
        "maximum_original_gate_count": maximum_size,
        "maximum_frontier_size": maximum_frontier,
        "controls": ["Shared square (x+y)^2 has squarefree coefficient 2 over integers and 0 over F2.",
                     "Positive-degree zero leaves are skipped correctly."],
        "scope": "Finite homogeneous DAG frontier, context-degree, lazy squarefree projection, restriction and characteristic-two identities. Does not certify any asymptotic rank bound or complexity-class separation.",
    }
    path = Path(__file__).resolve().parent / "projection_results.json"
    path.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
