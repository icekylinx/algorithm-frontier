#!/usr/bin/env python3
"""Independent finite checks of the certified mixed-failure matching kernel.

The default exhaustive suite covers every simple graph through four vertices,
every vertex cover, both nontrivial input orders, and every budget from zero
through two.  It checks every permitted outside-vertex/crossing-edge failure,
every surviving left subset, and every subset of cover-internal edges.  Thus
cover-vertex and cover-internal-edge deletions are not charged to the budget.

All optimization answers come from an independent subset dynamic program.
The production constructor and its solver-free universal certificate verifier
are exercised directly.  Seeded larger cases, exact sharp examples, large
encoded budgets, native identities and invalid inputs complete the suite.
"""
from __future__ import annotations

import argparse
from collections import Counter
from copy import deepcopy
from functools import lru_cache
from itertools import combinations
import json
from pathlib import Path
import random
import subprocess
import sys
import tempfile

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "reference"))
from failure_kernel import build_failure_kernel  # noqa: E402
from verify_failure_kernel import verify_failure_kernel  # noqa: E402


def oracle(n: int, edges: list[tuple[int, int]]):
    """Return exact matching cardinalities on arbitrary induced vertex sets."""
    adjacency = [0] * n
    for u, v in edges:
        adjacency[u] |= 1 << v
        adjacency[v] |= 1 << u

    @lru_cache(maxsize=None)
    def solve(vertices: int) -> int:
        if not vertices:
            return 0
        bit = vertices & -vertices
        u = bit.bit_length() - 1
        remaining = vertices ^ bit
        answer = solve(remaining)
        neighbors = adjacency[u] & remaining
        while neighbors:
            other = neighbors & -neighbors
            neighbors ^= other
            answer = max(answer, 1 + solve(remaining ^ other))
        return answer

    return solve


def subsets(mask: int):
    """Enumerate all subsets of the original mask, including zero."""
    value = mask
    while True:
        yield value
        if not value:
            return
        value = (value - 1) & mask


def native_graph(n: int, edges: list[tuple[int, int]]) -> dict:
    # Reverse some endpoint orientations independently of input ordering.
    native = [(v, u) if index % 2 else (u, v)
              for index, (u, v) in enumerate(edges)]
    labels = [-(index + 1) if index % 2 == 0 else f"native:{index}"
              for index in range(len(native))]
    return {"n": n, "edges": native, "edge_ids": labels}


def checked_kernel(graph: dict, f: int, cover, counts: Counter) -> dict:
    n, edges = graph["n"], graph["edges"]
    result = build_failure_kernel(n, edges, f, graph.get("edge_ids"), cover=cover)
    # The certificate is a public JSON object, so inspect that actual form.
    result = json.loads(json.dumps(result))
    report = verify_failure_kernel(graph, result)
    assert report["universal_preservation_verified"] is True
    assert report["matching_searches"] == 0
    assert report["failure_budget"] == f
    counts["certified_kernels"] += 1

    c = len(result["cover"])
    retained = set(result["vertices"])
    layers = result["certificate"]["layers"]
    first = result["certificate"]["edge_kernel_input_indices"]
    left = set(result["cover"])
    selected_right: set[int] = set()
    rank_sum = 0
    optimum = oracle(n, edges)((1 << n) - 1)
    assert len(retained) <= min(n, (f + 2) * c)
    assert len(layers) <= min(f + 1, n - c)
    if cover is None:
        assert c <= 2 * optimum
        assert len(retained) <= (f + 3) * optimum
        assert report["vertex_bound"] == "min((f+2)c,(f+3)nu(G))"
    else:
        assert result["cover"] == sorted(cover)
        assert report["vertex_bound"] == "(f+2)c"
    assert len(first) <= c * (c - 1) // 2 + c * (c + f)
    for layer in layers:
        residual = [(u, v) for index in first for u, v in [edges[index]]
                    if (u in left) != (v in left)
                    and (v if u in left else u) not in selected_right]
        rank = oracle(n, residual)((1 << n) - 1)
        assert len(layer["matching_input_indices"]) == rank <= optimum
        assert len(layer["minimum_cover"]) == rank
        rank_sum += rank
        counts["maximum_layers"] += 1
        for index in layer["matching_input_indices"]:
            u, v = edges[index]
            outside = v if u in left else u
            assert outside not in selected_right
            selected_right.add(outside)
    assert retained == left | selected_right
    assert len(retained) == c + rank_sum
    expected = [index for index in first if all(u in retained for u in edges[index])]
    assert [record["input_index"] for record in result["edges"]] == expected
    labels = graph.get("edge_ids")
    if labels is None:
        labels = list(range(len(edges)))
    for record, index in zip(result["edges"], expected):
        assert (record["u"], record["v"]) == tuple(edges[index])
        assert type(record["id"]) is type(labels[index]) and record["id"] == labels[index]
    assert result["statistics"]["layers"] == len(layers)
    assert result["statistics"]["retained_vertices"] == len(retained)
    assert result["statistics"]["retained_edges"] == len(expected)
    return result


def failure_choices(objects: list[tuple[str, int]], f: int, exhaustive: bool,
                    randomizer: random.Random):
    if exhaustive:
        for size in range(min(f, len(objects)) + 1):
            yield from combinations(objects, size)
        return
    choices = {()}
    # Small seeded cases still include every single native object failure.
    if f:
        choices.update((item,) for item in objects)
    for _ in range(16):
        size = randomizer.randrange(min(f, len(objects)) + 1)
        choices.add(tuple(sorted(randomizer.sample(objects, size))))
    yield from sorted(choices)


def internal_choices(indices: list[int], exhaustive: bool, randomizer: random.Random):
    if exhaustive:
        for mask in range(1 << len(indices)):
            yield {index for bit, index in enumerate(indices) if mask & (1 << bit)}
        return
    choices = {(), tuple(indices)}
    if indices:
        choices.add(tuple(indices[::2]))
        choices.add(tuple(indices[1::2]))
    for _ in range(2):
        choices.add(tuple(index for index in indices if randomizer.randrange(2)))
    for choice in sorted(choices):
        yield set(choice)


def check_queries(graph: dict, result: dict, exhaustive: bool,
                  randomizer: random.Random, counts: Counter) -> None:
    n, edges, f = graph["n"], graph["edges"], result["failure_budget"]
    full = (1 << n) - 1
    left = set(result["cover"])
    left_mask = sum(1 << u for u in left)
    outside_mask = full ^ left_mask
    retained_mask = sum(1 << u for u in result["vertices"])
    retained_edges = {record["input_index"] for record in result["edges"]}
    crossing = [index for index, (u, v) in enumerate(edges) if (u in left) != (v in left)]
    internal = [index for index, (u, v) in enumerate(edges) if u in left and v in left]
    objects = [("v", u) for u in range(n) if u not in left]
    objects += [("e", index) for index in crossing]
    left_subsets = list(subsets(left_mask))
    for failed in failure_choices(objects, f, exhaustive, randomizer):
        removed_vertices = sum(1 << index for kind, index in failed if kind == "v")
        removed_edges = {index for kind, index in failed if kind == "e"}
        surviving_right = outside_mask & ~removed_vertices
        current = [index for index in crossing if index not in removed_edges
                   and not any(removed_vertices & (1 << u) for u in edges[index])]
        old_cross = oracle(n, [edges[index] for index in current])
        new_cross = oracle(n, [edges[index] for index in current if index in retained_edges])
        counts["charged_failure_scenarios"] += 1
        for surviving_left in left_subsets:
            old = old_cross(surviving_left | surviving_right)
            new = new_cross(surviving_left | (surviving_right & retained_mask))
            assert old == new, ("left-subset", graph, result, failed, surviving_left, old, new)
            counts["left_subset_rank_comparisons"] += 1

        # Keep an arbitrary subset of cover-internal edges without spending
        # failure budget.  Every left subset independently deletes the other
        # cover vertices, again without spending failure budget.
        for surviving_internal in internal_choices(internal, exhaustive, randomizer):
            original_edges = [edges[index] for index in current]
            original_edges += [edges[index] for index in surviving_internal]
            kernel_edges = [edges[index] for index in current if index in retained_edges]
            kernel_edges += [edges[index] for index in surviving_internal if index in retained_edges]
            old_general = oracle(n, original_edges)
            new_general = oracle(n, kernel_edges)
            for surviving_left in left_subsets:
                old = old_general(surviving_left | surviving_right)
                new = new_general(surviving_left | (surviving_right & retained_mask))
                assert old == new, ("general", graph, result, failed,
                                    surviving_internal, surviving_left, old, new)
                counts["general_matching_comparisons"] += 1


def check_sharp_examples(counts: Counter) -> None:
    for f in range(4):
        for components in (1, 2):
            for default in (False, True):
                leaves = f + (2 if default else 1)
                n = components * (leaves + 1)
                centers = [component * (leaves + 1) for component in range(components)]
                edges = [(center, center + offset) for center in centers
                         for offset in range(1, leaves + 1)]
                graph = native_graph(n, edges)
                result = checked_kernel(graph, f, None if default else centers, counts)
                optimum = oracle(n, edges)((1 << n) - 1)
                assert optimum == components
                assert len(result["certificate"]["layers"]) == f + 1
                assert len(result["vertices"]) == n
                assert n == ((f + 3) * optimum if default else (f + 2) * len(centers))
                counts["sharp_star_examples"] += 1

    graph = native_graph(8, [(0, u) for u in range(1, 8)])
    huge = 10 ** 1000
    for cover in (None, [0]):
        result = checked_kernel(graph, huge, cover, counts)
        assert result["failure_budget"] == huge
        assert len(result["vertices"]) == 8 and len(result["edges"]) == 7
        assert len(result["certificate"]["layers"]) == (6 if cover is None else 7)
        counts["huge_budget_examples"] += 1

    # Distinguish integer and string labels with equal printed characters;
    # keep large signed identifiers and input endpoint orientation exactly.
    graph = {"n": 5, "edges": [(1, 0), (0, 2), (3, 0), (0, 4)],
             "edge_ids": [1, "1", -(10 ** 100), "edge:4"]}
    result = checked_kernel(graph, 9, [0], counts)
    assert [record["id"] for record in result["edges"]] == graph["edge_ids"]
    counts["native_identity_examples"] += 1

    # The constructor accepts both omitted IDs and explicit JSON null as
    # the default original input indices; the verifier must agree.
    for explicit_null in (False, True):
        graph = {"n": 3, "edges": [(1, 0), (0, 2)]}
        if explicit_null:
            graph["edge_ids"] = None
        result = checked_kernel(graph, 2, [0], counts)
        assert [record["id"] for record in result["edges"]] == [0, 1]
        counts["native_identity_examples"] += 1


def check_optimized_cli(counts: Counter) -> None:
    """Execute the real JSON commands with Python assertions disabled."""
    reference = Path(__file__).resolve().parents[1] / "reference"
    constructor = [sys.executable, "-O", str(reference / "failure_kernel.py"),
                   "-", "--failures", "2"]
    graph = {"n": 6, "edges": [[u, 0] for u in range(1, 6)],
             "cover": [0], "edge_ids": None}
    made = subprocess.run(constructor, input=json.dumps(graph), text=True,
                          capture_output=True, check=True)
    result = json.loads(made.stdout)
    assert [record["id"] for record in result["edges"]] == [0, 1, 2]
    with tempfile.TemporaryDirectory(prefix="matching-failure-check-") as directory:
        graph_path = Path(directory) / "graph.json"
        kernel_path = Path(directory) / "kernel.json"
        graph_path.write_text(json.dumps(graph), encoding="utf-8")
        kernel_path.write_text(json.dumps(result), encoding="utf-8")
        command = [sys.executable, "-O", str(reference / "verify_failure_kernel.py"),
                   str(graph_path), str(kernel_path)]
        verified = subprocess.run(command, text=True, capture_output=True, check=True)
        report = json.loads(verified.stdout)
        assert report["universal_preservation_verified"] is True
        assert report["matching_searches"] == 0
        counts["optimized_cli_roundtrips"] += 1
        result["edges"][0]["id"] = "tampered"
        kernel_path.write_text(json.dumps(result), encoding="utf-8")
        rejected = subprocess.run(command, text=True, capture_output=True)
        assert rejected.returncode != 0 and "native edge record" in rejected.stderr
        counts["optimized_cli_corruption_rejections"] += 1
    invalid = subprocess.run(constructor, input=json.dumps({"n": 1, "edges": [[0, 0]]}),
                             text=True, capture_output=True)
    assert invalid.returncode != 0 and "simple loopless" in invalid.stderr
    counts["optimized_cli_input_rejections"] += 1


def expect_rejection(call, counts: Counter, key: str) -> None:
    try:
        call()
    except (TypeError, ValueError):
        counts[key] += 1
    else:
        raise AssertionError(f"invalid input accepted in {key}")


def check_rejections(counts: Counter) -> None:
    constructor_bad = [
        (True, [], 0, None, None), (-1, [], 0, None, None),
        (2, [(0, 0)], 1, None, None),
        (2, [(0, 1), (1, 0)], 1, None, None),
        (2, [(0, 2)], 1, None, None), (2, [(False, 1)], 1, None, None),
        (2, [(0, 1, 0)], 1, None, None),
        (2, [(0, 1)], -1, None, None), (2, [(0, 1)], True, None, None),
        (2, [(0, 1)], 1.5, None, None),
        (2, [(0, 1)], 1, [], None), (2, [(0, 1)], 1, [True], None),
        (3, [(0, 1), (0, 2)], 1, ["same", "same"], None),
        (2, [(0, 1)], 1, None, []),
        (2, [(0, 1)], 1, None, [0, 0]),
        (2, [(0, 1)], 1, None, [2]),
        (2, [(0, 1)], 1, None, [False]),
    ]
    for n, edges, f, ids, cover in constructor_bad:
        expect_rejection(lambda n=n, edges=edges, f=f, ids=ids, cover=cover:
                         build_failure_kernel(n, edges, f, ids, cover=cover),
                         counts, "constructor_rejections")

    graph = native_graph(8, [(0, u) for u in range(1, 8)])
    valid = checked_kernel(graph, 2, [0], counts)
    corruptions = []

    def corrupt(path, replacement):
        bad = deepcopy(valid)
        target = bad
        for part in path[:-1]:
            target = target[part]
        target[path[-1]] = replacement
        corruptions.append(bad)

    corrupt(["schema_version"], True)
    corrupt(["schema_version"], 2)
    corrupt(["kind"], "matching")
    corrupt(["n"], 7)
    corrupt(["failure_budget"], -1)
    corrupt(["failure_budget"], True)
    corrupt(["failure_budget"], 3)
    corrupt(["cover"], [1])
    corrupt(["cover"], [0, 0])
    corrupt(["certificate", "greedy_matching_input_indices"], [0])
    corrupt(["certificate", "edge_kernel_input_indices"], [0, 1])
    corrupt(["certificate", "edge_kernel_input_indices"], [1, 0, 2])
    corrupt(["certificate", "layers"], valid["certificate"]["layers"][:-1])
    corrupt(["certificate", "layers"], valid["certificate"]["layers"] * 2)
    corrupt(["certificate", "layers", 0, "matching_input_indices"], [0, 0])
    corrupt(["certificate", "layers", 0, "minimum_cover"], [])
    corrupt(["certificate", "layers", 1, "matching_input_indices"], [0])
    corrupt(["certificate", "layers", 1, "minimum_cover"], [1])
    corrupt(["certificate", "layers", 1, "minimum_cover"], [7])
    corrupt(["vertices"], valid["vertices"][1:])
    corrupt(["vertices"], list(reversed(valid["vertices"])))
    corrupt(["edges"], valid["edges"][:-1])
    corrupt(["edges", 0, "id"], str(valid["edges"][0]["id"]))
    corrupt(["edges", 0, "input_index"], False)
    corrupt(["edges", 0, "u"], valid["edges"][0]["v"])
    for bad in corruptions:
        expect_rejection(lambda bad=bad: verify_failure_kernel(graph, bad),
                         counts, "certificate_rejections")

    other = native_graph(4, [(0, 1), (0, 2), (1, 3)])
    certified = checked_kernel(other, 1, [0, 1], counts)
    bad = deepcopy(certified)
    bad["certificate"]["edge_kernel_input_indices"].remove(0)
    expect_rejection(lambda: verify_failure_kernel(other, bad), counts, "certificate_rejections")

    malformed_graphs = [
        {"n": True, "edges": []}, {"n": 2, "edges": [(0, 0)]},
        {"n": 2, "edges": [(0, 1), (1, 0)]},
        {"n": 2, "edges": [(0, 2)]}, {"n": 2, "edges": [(0, False)]},
        {"n": 2, "edges": [(0, 1)], "edge_ids": [True]},
        {"n": 3, "edges": [(0, 1), (0, 2)], "edge_ids": [1, 1]},
        {"n": 2, "edges": [(0, 1)], "edge_ids": []},
        {"n": 2, "edges": [(0, 1, 2)]},
    ]
    for malformed in malformed_graphs:
        expect_rejection(lambda malformed=malformed: verify_failure_kernel(malformed, valid),
                         counts, "verifier_input_rejections")


def main() -> None:
    if not __debug__:
        raise SystemExit("Run without -O or PYTHONOPTIMIZE.")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-n", type=int, default=4, choices=range(6))
    parser.add_argument("--random-cases", type=int, default=48)
    args = parser.parse_args()
    if args.random_cases < 0:
        parser.error("--random-cases must be nonnegative")
    counts: Counter = Counter()
    randomizer = random.Random(0xFA17C0A3)
    for n in range(args.max_n + 1):
        possible = list(combinations(range(n), 2))
        for mask in range(1 << len(possible)):
            edges = [edge for index, edge in enumerate(possible) if mask & (1 << index)]
            orders = [edges] if len(edges) < 2 else [edges, list(reversed(edges))]
            counts["exhaustive_graphs"] += 1
            for order in orders:
                graph = native_graph(n, order)
                covers = [None]
                covers.extend([u for u in range(n) if candidate & (1 << u)]
                              for candidate in range(1 << n)
                              if all(candidate & ((1 << u) | (1 << v)) for u, v in order))
                for cover in covers:
                    for f in range(3):
                        result = checked_kernel(graph, f, cover, counts)
                        check_queries(graph, result, True, randomizer, counts)
    for case in range(args.random_cases):
        n = 5 + case % 5
        cover = [u for u in range(n) if randomizer.random() < 0.55]
        edges = [(u, v) for u, v in combinations(range(n), 2)
                 if (u in cover or v in cover) and randomizer.random() < (case % 7 + 2) / 10]
        randomizer.shuffle(edges)
        graph = native_graph(n, edges)
        for chosen_cover in (None, cover):
            for f in range(3):
                result = checked_kernel(graph, f, chosen_cover, counts)
                check_queries(graph, result, False, randomizer, counts)
        counts["seeded_graphs"] += 1
    check_sharp_examples(counts)
    check_optimized_cli(counts)
    check_rejections(counts)
    print("PASS: certified mixed-failure matching kernel")
    print(json.dumps(dict(sorted(counts.items())), indent=2))
    print("Scope: exact native failure preservation and universal certificates; no fast-backend claim.")


if __name__ == "__main__":
    main()
