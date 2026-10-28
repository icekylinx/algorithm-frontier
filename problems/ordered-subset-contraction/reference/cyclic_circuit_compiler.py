#!/usr/bin/env python3
# Copyright 2026 icekylinx and GPT-6 Astra Pro
# SPDX-License-Identifier: Apache-2.0
"""Compile all cyclic derivatives of a shared ordered arithmetic circuit.

The input is JSON with a nonempty topologically ordered ``nodes`` list and an
integer ``output`` index. Operations are var, const, add, sub, neg, and mul.
Only literal constants 0, 1, and -1 are allowed. Every multiplication retains
its operand order. No polynomial expansion or SAT solver is used.

Example:
  python3 reference/cyclic_circuit_compiler.py examples/cyclic_shared_input.json \
      --output work/cyclic_shared_compiled.json

For a selected row family, --rotate-row may be repeated. A sufficient
syntactic degree check must certify exactly one selected-row occurrence per
monomial. Cancellation can make this check conservative, never permissive.

The source checkpoint contains separate Lean proofs; those proofs are not imported here. This JSON adapter is
reference code, independently tested on exact finite ordered polynomials; it
is not itself extracted from Lean and does not implement a fast crossing
circuit or the announced subexponential SAT algorithm.
"""

from __future__ import annotations

import argparse
from copy import deepcopy
import json
from pathlib import Path
from typing import Any, Callable


def validate(document: dict[str, Any]) -> tuple[list[dict[str, Any]], int]:
    if not isinstance(document, dict):
        raise ValueError("The input must be a JSON object.")
    nodes = document.get("nodes")
    if not isinstance(nodes, list) or not nodes:
        raise ValueError("nodes must be a nonempty list.")
    arity = {"add": 2, "sub": 2, "mul": 2, "neg": 1}
    for index, node in enumerate(nodes):
        if not isinstance(node, dict):
            raise ValueError(f"Node {index} must be an object.")
        op = node.get("op")
        if not isinstance(op, str):
            raise ValueError(f"Node {index}: op must be a string.")
        if op == "var":
            if not isinstance(node.get("name"), str) or not node["name"]:
                raise ValueError(f"Node {index} needs a nonempty variable name.")
        elif op == "const":
            if type(node.get("value")) is not int or node["value"] not in (-1, 0, 1):
                raise ValueError(f"Node {index}: only literal constants 0, 1, -1 are allowed.")
        elif op in arity:
            args = node.get("args")
            if not isinstance(args, list) or len(args) != arity[op]:
                raise ValueError(f"Node {index}: {op} requires {arity[op]} predecessors.")
            if any(type(j) is not int or not 0 <= j < index for j in args):
                raise ValueError(f"Node {index}: every predecessor must be an earlier index.")
        else:
            raise ValueError(f"Node {index}: unsupported operation {op!r}.")
    output = document.get("output")
    if type(output) is not int or not 0 <= output < len(nodes):
        raise ValueError("output must name an existing node.")
    return deepcopy(nodes), output


def arithmetic_cost(nodes: list[dict[str, Any]]) -> int:
    """Charge addition, negation, and ordered multiplication separately."""
    return sum(2 if n["op"] == "sub" else
               1 if n["op"] in ("add", "mul", "neg") or
               (n["op"] == "const" and n["value"] == -1) else 0
               for n in nodes)


def row_degrees(nodes: list[dict[str, Any]], selected: set[str]) -> list[set[int]]:
    """An upper set of possible degrees, with all degrees >=2 represented by2."""
    degrees: list[set[int]] = []
    for node in nodes:
        op = node["op"]
        if op == "var":
            value = {int(node["name"] in selected)}
        elif op == "const":
            value = set() if node["value"] == 0 else {0}
        elif op == "neg":
            value = set(degrees[node["args"][0]])
        else:
            left, right = (degrees[j] for j in node["args"])
            value = ({min(2, a+b) for a in left for b in right}
                     if op == "mul" else left | right)
        degrees.append(value)
    return degrees


def compile_document(document: dict[str, Any], rotate_row: list[str] | None = None
                     ) -> dict[str, Any]:
    nodes, output = validate(document)
    original = deepcopy(nodes)
    count = len(original)
    first_input: dict[str, int] = {}
    for index, node in enumerate(original):
        if node["op"] == "var":
            first_input.setdefault(node["name"], index)
    selected = list(dict.fromkeys(rotate_row or []))
    if any(name not in first_input for name in selected):
        raise ValueError("Every selected row variable must occur in the input circuit.")
    if selected and not row_degrees(original, set(selected))[output] <= {1}:
        raise ValueError("Cannot certify exactly one selected-row occurrence per monomial. "
                         "The conservative syntactic check may fail after cancellations.")

    def emit(op: str, *args: int) -> int:
        nodes.append({"op": op, "args": list(args)})
        return len(nodes)-1

    zero = len(nodes)
    nodes.append({"op": "const", "value": 0})
    one = len(nodes)
    nodes.append({"op": "const", "value": 1})
    adjoints = [zero] * count
    adjoints[output] = one
    gradients = {name: zero for name in first_input}

    for index in reversed(range(count)):
        node = original[index]
        op, seed = node["op"], adjoints[index]
        if op == "const":
            continue
        if op == "var":
            name = node["name"]
            gradients[name] = emit("add", gradients[name], seed)
            continue
        if op == "neg":
            child = node["args"][0]
            update = emit("neg", seed)
            adjoints[child] = emit("add", adjoints[child], update)
            continue
        left, right = node["args"]
        if op == "mul":
            # Freeze both contributions before either accumulator is updated.
            # This is essential when the two predecessor indices are equal.
            left_update = emit("mul", right, seed)
            right_update = emit("mul", seed, left)
        else:
            left_update = seed
            right_update = seed if op == "add" else emit("neg", seed)
        adjoints[left] = emit("add", adjoints[left], left_update)
        adjoints[right] = emit("add", adjoints[right], right_update)

    outputs: dict[str, Any] = {"original": output, "cyclic_derivatives": gradients}
    if selected:
        rotated = zero
        for name in selected:
            term = emit("mul", gradients[name], first_input[name])
            rotated = emit("add", rotated, term)
        outputs["row_rotation"] = rotated

    cost = arithmetic_cost(nodes)
    bound = 6*count + 2*len(selected)
    assert cost <= bound, (cost, bound)
    return {
        "format": "ordered-cyclic-circuit-v1",
        "nodes": nodes,
        "outputs": outputs,
        "cost": {
            "model": "Each addition, negation, and ordered multiplication costs one. "
                     "Subtraction costs two; literal minus-one costs one negation. "
                     "Zero, one, input references, and fan-out have no arithmetic cost.",
            "source_nodes": count,
            "source_arithmetic_operations": arithmetic_cost(original),
            "compiled_nodes": len(nodes),
            "compiled_arithmetic_operations": cost,
            "proved_construction_bound": bound,
            "forward_computation_included": True,
        },
        "selected_row": selected,
        "row_occurrence_syntactically_certified": bool(selected),
        "scope": "Actual cyclic derivatives in the free associative algebra over the "
                 "integers, evaluable in any associative unital ring. Literal constants "
                 "are 0,1,-1. Row rotation requires the recorded row-degree certificate. "
                 "The JSON adapter is tested reference code, not Lean-extracted code.",
    }


def evaluate_nodes(nodes: list[dict[str, Any]], variables: dict[str, Any], *,
                   zero: Any, one: Any, plus: Callable, negate: Callable,
                   times: Callable) -> list[Any]:
    """Evaluate with caller-supplied ring operations; times must preserve order."""
    values: list[Any] = []
    for node in nodes:
        op = node["op"]
        if op == "var":
            value = variables[node["name"]]
        elif op == "const":
            value = zero if node["value"] == 0 else one if node["value"] == 1 else negate(one)
        elif op == "neg":
            value = negate(values[node["args"][0]])
        else:
            left, right = (values[j] for j in node["args"])
            value = (times(left, right) if op == "mul" else
                     plus(left, right) if op == "add" else plus(left, negate(right)))
        values.append(value)
    return values


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--rotate-row", action="append", default=[])
    args = parser.parse_args()
    try:
        document = json.loads(args.input.read_text())
        compiled = compile_document(document, args.rotate_row)
    except (ValueError, OSError) as error:
        parser.error(str(error))
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(compiled, indent=2) + "\n")
    print(json.dumps({"status": "PASS", "output": str(args.output),
                      "cost": compiled["cost"],
                      "derivative_outputs": list(compiled["outputs"]["cyclic_derivatives"]),
                      "row_rotation": bool(args.rotate_row)}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
