#!/usr/bin/env python3
# Copyright 2026 icekylinx and GPT-6 Astra Pro
# SPDX-License-Identifier: Apache-2.0
"""Check the reusable JSON compiler against an independent ordered-word oracle."""
from collections import Counter
from datetime import datetime, timezone
from hashlib import sha256
from pathlib import Path
import json
import random
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "reference"))
from cyclic_circuit_compiler import compile_document, evaluate_nodes
from cyclic_word_oracle import add, mul, cyclic, residue, var

COUNTS = Counter()


def check(value, category):
    assert value, category
    COUNTS[category] += 1


def evaluate(document):
    names = {n["name"] for n in document["nodes"] if n["op"] == "var"}
    return evaluate_nodes(document["nodes"], {n: var(n) for n in names},
                          zero={}, one={(): 1}, plus=add,
                          negate=lambda p: {w: -c for w, c in p.items()}, times=mul)


def verify(document, selected=None):
    original = evaluate(document)[document["output"]]
    compiled = compile_document(document, selected)
    values = evaluate(compiled)
    check(values[compiled["outputs"]["original"]] == original, "forward_output")
    for name, index in compiled["outputs"]["cyclic_derivatives"].items():
        expected = cyclic(original, name)
        check(values[index] == expected, "actual_ordered_derivative")
        for modulus in (2, 4, 6):
            check(residue(values[index], modulus) == residue(expected, modulus),
                  "small_characteristic_derivative")
    check(compiled["cost"]["compiled_arithmetic_operations"] <=
          6*len(document["nodes"]) + 2*len(set(selected or [])), "charged_gate_bound")
    if selected:
        target = {}
        for word, coefficient in original.items():
            positions = [j for j, name in enumerate(word) if name in selected]
            check(len(positions) == 1, "literal_row_occurrence")
            j = positions[0]
            rotated = word[j+1:] + word[:j] + word[j:j+1]
            target = add(target, {rotated: coefficient})
        check(values[compiled["outputs"]["row_rotation"]] == target, "literal_word_rotation")
    return compiled, values


def main():
    shared = json.loads((ROOT / "examples/cyclic_shared_input.json").read_text())
    compiled, values = verify(shared)
    gx = values[compiled["outputs"]["cyclic_derivatives"]["x"]]
    gy = values[compiled["outputs"]["cyclic_derivatives"]["y"]]
    check(gx == {("y", "x", "y"): 2, (): -1}, "shared_repeated_input_formula")
    check(gy == {("x", "y", "x"): 2}, "shared_repeated_operand_formula")
    check(residue(gx, 2) == {(): 1} and residue(gy, 2) == {}, "mod_two_multiplicity_guard")
    row = json.loads((ROOT / "examples/cyclic_row_input.json").read_text())
    rotated, rv = verify(row, ["z"])
    check(rv[rotated["outputs"]["row_rotation"]] == {("b", "a", "z"): 1},
          "noncommutative_rotation_direction")

    rng = random.Random(2710260545)
    for _ in range(30):
        nodes = [{"op": "var", "name": name} for name in ("x", "y", "z", "x")]
        nodes += [{"op": "const", "value": n} for n in (0, 1, -1)]
        degrees = [1, 1, 1, 1, 0, 0, 0]
        for _gate in range(24):
            op = rng.choice(("add", "sub", "neg", "mul"))
            a = rng.randrange(len(nodes))
            b = a if rng.randrange(3) == 0 else rng.randrange(len(nodes))
            if op == "mul" and degrees[a]+degrees[b] > 6:
                op = "sub"
            nodes.append({"op": op, "args": [a] if op == "neg" else [a, b]})
            degrees.append(degrees[a] if op == "neg" else
                           degrees[a]+degrees[b] if op == "mul" else max(degrees[a], degrees[b]))
        verify({"nodes": nodes, "output": len(nodes)-1})

    bad_inputs = [
        {"nodes": [], "output": 0},
        {"nodes": [{"op": "const", "value": 2}], "output": 0},
        {"nodes": [{"op": "const", "value": True}], "output": 0},
        {"nodes": [{"op": "var", "name": "x"}], "output": -1},
        {"nodes": [{"op": "var", "name": "x"}], "output": True},
        {"nodes": [{"op": "mul", "args": [0, 0]}], "output": 0},
        {"nodes": [{"op": "var", "name": "x"}, {"op": "neg", "args": [-1]}], "output": 1},
        {"nodes": [{"op": "var", "name": "x"}, {"op": "add", "args": [True, 0]}], "output": 1},
        {"nodes": [{"op": [], "args": []}], "output": 0},
        {"nodes": [{"op": "divide", "args": []}], "output": 0},
    ]
    for bad in bad_inputs:
        try:
            compile_document(bad)
        except ValueError:
            check(True, "malformed_input_rejection")
        else:
            raise AssertionError("An invalid circuit was accepted.")
    for source, selected in [(shared, ["x"]), (row, ["missing"]), (row, ["a", "z"])]:
        try:
            compile_document(source, selected)
        except ValueError:
            check(True, "invalid_row_claim_rejection")
        else:
            raise AssertionError("An invalid row-rotation claim was accepted.")

    with tempfile.TemporaryDirectory(prefix="cyclic-compiler-") as directory:
        target = Path(directory) / "compiled.json"
        result = subprocess.run([sys.executable, str(ROOT / "reference/cyclic_circuit_compiler.py"),
                                 str(ROOT / "examples/cyclic_row_input.json"),
                                 "--output", str(target), "--rotate-row", "z"],
                                cwd=ROOT, capture_output=True, text=True)
        check(result.returncode == 0, "actual_cli_execution")
        check(json.loads(target.read_text()) == rotated, "cli_serialization_roundtrip")

    record = {
        "status": "PASS", "utc": datetime.now(timezone.utc).isoformat(),
        "scope": "Reusable JSON compiler checked against independent free-word cyclic derivatives, "
                 "repeated names/operands, characteristic-two cancellation, row-order semantics, "
                 "input guards and an actual CLI round trip. No asymptotic fast-crossing implementation.",
        "assertions": sum(COUNTS.values()), "counts": dict(COUNTS),
        "compiler_sha256": sha256((ROOT / "reference/cyclic_circuit_compiler.py").read_bytes()).hexdigest(),
        "checker_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
        "statistical_trials": False,
    }
    (ROOT / "results/cyclic_compiler_interface_checks.json").write_text(json.dumps(record, indent=2)+"\n")
    print(json.dumps(record, indent=2))


if __name__ == "__main__":
    main()
