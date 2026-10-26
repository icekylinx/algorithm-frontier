#!/usr/bin/env python3
"""Independent finite evidence for the unconditional blossom reference solver.

All simple graphs through six vertices are compared to a subset-DP oracle in
both kernel and full-graph modes.  Every result also has its optimality
certificate checked by the separate, solver-free verifier.  Native-record
cases add loops, reversed parallel records, isolated vertices and mixed ID
types.  Seeded larger graphs, invalid certificates, and CLI round trips cover
interfaces that the exhaustive simple-graph family does not exercise.

Finite evidence supports review of this implementation; it is not a formal
proof of the code or a realization of the manuscript's faster graph backend.
The production solver is deterministic; randomness is used only to select
reproducible supplemental test inputs.  Python standard library only.
"""

from __future__ import annotations

import argparse
import copy
import json
import random
import subprocess
import sys
import tempfile
from functools import lru_cache
from itertools import combinations
from pathlib import Path


REFERENCE = Path(__file__).resolve().parents[1] / "reference"
sys.path.insert(0, str(REFERENCE))
from matching import maximum_matching  # noqa: E402
from verify_certificate import verify_result  # noqa: E402


def oracle(n: int, edges: list[tuple[int, int]]) -> int:
    """Enumerate all possibilities for the first remaining vertex.

    This uses no normalization, component kernel, augmenting paths, blossoms,
    or Tutte--Berge information from the implementation under test.
    """
    adjacency = [0] * n
    for u, v in edges:
        if u != v:
            adjacency[u] |= 1 << v
            adjacency[v] |= 1 << u

    @lru_cache(maxsize=None)
    def optimum(available: int) -> int:
        if not available:
            return 0
        first = available & -available
        u = first.bit_length() - 1
        remainder = available ^ first
        answer = optimum(remainder)
        neighbors = adjacency[u] & remainder
        while neighbors:
            last = neighbors & -neighbors
            neighbors ^= last
            answer = max(answer, 1 + optimum(remainder ^ last))
        return answer

    return optimum((1 << n) - 1)


def check_instance(n: int, edges: list[tuple[int, int]], edge_ids=None) -> tuple[int, int]:
    expected = oracle(n, edges)
    contractions = augmentations = 0
    for use_kernel in (True, False):
        answer = maximum_matching(n, edges, edge_ids, use_kernel=use_kernel, certificate=True)
        assert answer["cardinality"] == expected, (n, edges, use_kernel, answer, expected)
        verified = verify_result(n, edges, answer, edge_ids)
        assert verified["optimality_verified"] and verified["cardinality"] == expected
        assert verified["retained_vertices"] == answer["statistics"]["kernel_vertices"]
        assert verified["retained_edges"] == answer["statistics"]["kernel_edges"]
        contractions += answer["statistics"]["blossom_contractions"]
        augmentations += answer["statistics"]["augmentations"]
    return contractions, augmentations


def exhaustive(max_n: int) -> tuple[int, int, int]:
    graphs = contractions = augmentations = 0
    for n in range(max_n + 1):
        possible = list(combinations(range(n), 2))
        for mask in range(1 << len(possible)):
            edges = [edge for bit, edge in enumerate(possible) if mask & (1 << bit)]
            c, a = check_instance(n, edges)
            contractions += c
            augmentations += a
            graphs += 1
    return graphs, contractions, augmentations


def native_cases() -> int:
    count = 0
    for n in range(5):
        possible = list(combinations(range(n), 2))
        for mask in range(1 << len(possible)):
            simple = [edge for bit, edge in enumerate(possible) if mask & (1 << bit)]
            records = [(vertex, vertex) for vertex in range(n + 2)]
            for u, v in simple:
                records.extend([(v, u), (u, v), (v, u)])
            for ordered in (records, list(reversed(records))):
                labels = [f"native-{i}" if i % 2 else -i - 1 for i in range(len(ordered))]
                check_instance(n + 2, ordered, labels)
                count += 1
    return count


def supplemental_cases(number: int) -> tuple[int, int, int]:
    randomizer = random.Random(0xB10550)
    cases: list[tuple[int, list[tuple[int, int]]]] = []
    # Odd cycles, a chain of touching blossoms, and the Petersen graph.
    for n in (3, 5, 7, 9, 11):
        cases.append((n, [(v, (v + 1) % n) for v in range(n)]))
    cases.extend([
        (10, [(0, 1), (1, 2), (2, 0), (2, 3), (3, 4), (4, 2),
              (4, 5), (5, 6), (6, 4), (6, 7), (7, 8), (8, 6), (8, 9)]),
        (10, [(v, (v + 1) % 5) for v in range(5)] +
             [(v, v + 5) for v in range(5)] +
             [(v + 5, (v + 2) % 5 + 5) for v in range(5)]),
        (12, [(0, v) for v in range(1, 12)]),
        (12, list(combinations(range(12), 2))),
        (12, [(v, v + 1) for v in range(11)]),
    ])
    for index in range(number):
        n = 7 + index % 6
        threshold = (index % 9 + 1) / 10
        edges = [edge for edge in combinations(range(n), 2) if randomizer.random() < threshold]
        randomizer.shuffle(edges)
        if index % 3 == 0:
            edges += [(v, v) for v in range(n)]
            edges += [(v, u) for u, v in edges[:len(edges) // 3]]
        cases.append((n, edges))
    contractions = augmentations = 0
    for n, edges in cases:
        c, a = check_instance(n, edges)
        contractions += c
        augmentations += a
        # Certificate generation must not change the selected matching.
        plain = maximum_matching(n, edges)
        certified = maximum_matching(n, edges, certificate=True)
        assert plain["matching"] == certified["matching"]
        assert verify_result(n, edges, plain, require_certificate=False)["optimality_verified"] is False
    return len(cases), contractions, augmentations


def expect_rejection(function, *args, **kwargs) -> None:
    try:
        function(*args, **kwargs)
    except (TypeError, ValueError):
        return
    raise AssertionError("invalid input or certificate was accepted")


def rejection_cases() -> int:
    edges = [(0, vertex) for vertex in range(1, 6)]
    answer = maximum_matching(6, edges, certificate=True)
    variants = []

    def changed():
        value = copy.deepcopy(answer)
        variants.append(value)
        return value

    changed()["cardinality"] += 1
    changed()["matching"][0]["id"] = "incorrect"
    changed()["matching"][0]["u"] = True
    changed()["matching"].append(copy.deepcopy(answer["matching"][0]))
    changed()["certificate"]["format"] = "unsupported"
    changed()["certificate"]["components"] = []
    changed()["certificate"]["components"][0]["root"] = 1
    changed()["certificate"]["components"][0]["cover"] = []
    changed()["certificate"]["components"][0]["cover"] += [0]
    changed()["certificate"]["components"][0]["retained_input_indices"].pop()
    changed()["certificate"]["components"][0]["retained_input_indices"].pop(0)
    changed()["certificate"]["components"][0]["retained_input_indices"] += [0]
    changed()["certificate"]["components"][0]["barrier"] = []
    changed()["certificate"]["components"][0]["barrier"] = [0, 0]
    changed()["certificate"]["components"][0]["barrier"] = [5]
    value = changed()
    value["matching"] = []
    value["cardinality"] = 0
    for value in variants:
        expect_rejection(verify_result, 6, edges, value)

    parallel = [(0, 1), (1, 0), (2, 2)]
    value = maximum_matching(3, parallel, certificate=True)
    value["matching"] = [{"input_index": 1, "id": 1, "u": 1, "v": 0}]
    # Feasibility is true, but this certificate format binds native records.
    assert verify_result(3, parallel, value, require_certificate=False)["matching_feasible"]
    expect_rejection(verify_result, 3, parallel, value)
    value["matching"] = [{"input_index": 2, "id": 2, "u": 2, "v": 2}]
    expect_rejection(verify_result, 3, parallel, value)

    invalid = [
        (-1, [], None), (True, [], None), (2.0, [], None),
        (2, [(0, 2)], None), (2, [(0, True)], None), (2, [(0,)], None),
        (2, [(0, 1)], []), (2, [(0, 1)], [True]),
        (2, [(0, 1), (1, 0)], ["same", "same"]),
    ]
    for n, records, labels in invalid:
        expect_rejection(maximum_matching, n, records, labels)
    expect_rejection(maximum_matching, 2, [(0, 1)], use_kernel=1)
    expect_rejection(verify_result, 6, edges, answer, require_certificate=1)
    return len(variants) + 2 + len(invalid) + 2


def scale_and_cli_cases() -> int:
    # Many disconnected components expose accidental scans of the entire
    # matching once per component.  A large star exercises real kernel removal.
    pairs = [(u, u + 1) for u in range(0, 2400, 2)]
    answer = maximum_matching(2600, pairs, certificate=True)
    assert answer["cardinality"] == 1200
    assert verify_result(2600, pairs, answer)["checked_components"] == 1200
    star = [(0, vertex) for vertex in range(1, 2001)]
    answer = maximum_matching(2500, star, certificate=True)
    assert answer["cardinality"] == 1
    assert answer["statistics"]["kernel_vertices"] == 4
    assert answer["statistics"]["kernel_edges"] == 3
    assert answer["statistics"]["solver_vertices"] == 3
    assert answer["statistics"]["blossom_vertices"] == 0
    assert verify_result(2500, star, answer)["optimality_verified"]

    # The first kernel can retain c+c^2 vertices while the second stage
    # leaves at most 2c.  Certificates must still describe the first kernel.
    cover_size = 20
    pairs_first = [(u, u + 1) for u in range(0, cover_size, 2)]
    linking_edges = [(u, u + 1) for u in range(1, cover_size - 1, 2)]
    private_leaves = [(u, cover_size + cover_size * u + offset)
                      for u in range(cover_size) for offset in range(cover_size)]
    leaf_path = pairs_first + linking_edges + private_leaves
    order = cover_size + cover_size * cover_size
    answer = maximum_matching(order, leaf_path, certificate=True)
    assert answer["cardinality"] == cover_size
    assert answer["statistics"]["cover_vertices"] == cover_size
    assert answer["statistics"]["kernel_vertices"] == order
    assert answer["statistics"]["kernel_edges"] == len(leaf_path) == 419
    assert answer["statistics"]["solver_vertices"] == 2 * cover_size
    assert answer["statistics"]["blossom_vertices"] == 0
    verified = verify_result(order, leaf_path, answer)
    assert verified["optimality_verified"] and verified["retained_vertices"] == order

    graph = {"n": 7, "edges": [[0, 0], [1, 0], [0, 1], [1, 2], [2, 3], [4, 5]],
             "edge_ids": ["loop", "first", "parallel", 8, 9, "separate"]}
    with tempfile.TemporaryDirectory(prefix="matching-reference-") as directory:
        input_path = Path(directory) / "graph.json"
        result_path = Path(directory) / "answer.json"
        input_path.write_text(json.dumps(graph), encoding="utf-8")
        process = subprocess.run([sys.executable, "-B", str(REFERENCE / "matching.py"), str(input_path), "--certificate"],
                                 capture_output=True, text=True, check=True)
        result_path.write_text(process.stdout, encoding="utf-8")
        verified = subprocess.run([sys.executable, "-B", str(REFERENCE / "verify_certificate.py"), str(input_path), str(result_path)],
                                  capture_output=True, text=True, check=True)
        assert json.loads(verified.stdout)["optimality_verified"]
        assert json.loads(process.stdout)["cardinality"] == oracle(graph["n"], graph["edges"])
        rejected = subprocess.run([sys.executable, "-B", "-O", str(REFERENCE / "verify_certificate.py"), str(input_path), str(result_path)],
                                  capture_output=True, text=True)
        assert rejected.returncode != 0 and "without -O" in rejected.stderr
        # Production computations contain no assert-dependent correctness.
        optimized = subprocess.run([sys.executable, "-B", "-O", str(REFERENCE / "matching.py"), str(input_path), "--certificate"],
                                   capture_output=True, text=True, check=True)
        assert json.loads(optimized.stdout) == json.loads(process.stdout)
    return 4


def main() -> None:
    if not __debug__:
        raise SystemExit("Run this mathematical checker without -O or PYTHONOPTIMIZE.")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-n", type=int, default=6, choices=range(7))
    parser.add_argument("--random-cases", type=int, default=250)
    args = parser.parse_args()
    if args.random_cases < 0:
        parser.error("--random-cases must be nonnegative")
    graphs, contractions, augmentations = exhaustive(args.max_n)
    native = native_cases()
    extra, c, a = supplemental_cases(args.random_cases)
    contractions += c
    augmentations += a
    rejected = rejection_cases()
    scale = scale_and_cli_cases()
    assert contractions > 0 and augmentations > 0
    print(f"PASS: {graphs} simple graphs in both modes ({2 * graphs} certified solves)")
    print(f"PASS: {native} native-record and {extra} supplemental instances in both modes")
    print(f"PASS: {rejected} rejection checks; {scale} scale/CLI cases")
    print(f"Coverage: {contractions} blossom contractions (including certificates); {augmentations} matching augmentations")
    print("Scope: exact finite oracle comparison and independent certificate verification; no fast-backend claim.")


if __name__ == "__main__":
    main()
