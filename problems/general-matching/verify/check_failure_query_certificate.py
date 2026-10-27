#!/usr/bin/env python3
"""Adversarial checks for the independent composite query certificate."""
from copy import deepcopy
import json
from pathlib import Path
import subprocess
import sys

REFERENCE = Path(__file__).resolve().parents[1] / "reference"
sys.path.insert(0, str(REFERENCE))
from failure_kernel import build_failure_kernel
from failure_query import solve_failure_query
from verify_failure_query import verify_failure_query


def main():
    if not __debug__:
        raise SystemExit("this checker requires assertions; do not use python -O")
    graph = {"n": 8, "edges": [[7, 1], [7, 3], [7, 5]],
             "edge_ids": [1, "1", "last"]}
    kernel = build_failure_kernel(8, graph["edges"], 1, graph["edge_ids"], cover=[7])
    result = solve_failure_query(graph, kernel, failed_edge_ids=[1])
    accepted = verify_failure_query(graph, kernel, result, failed_edge_ids=[1])
    assert accepted["optimality_verified"] and accepted["cardinality"] == 1
    rejected = 0

    def reject(candidate=result, *, supplied_kernel=kernel, vertices=(), ids=(1,)):
        nonlocal rejected
        before = deepcopy((graph, supplied_kernel, candidate))
        try:
            verify_failure_query(graph, supplied_kernel, candidate,
                                 failed_vertices=vertices, failed_edge_ids=ids)
        except ValueError:
            rejected += 1
        else:
            raise AssertionError("tampered query certificate accepted")
        assert (graph, supplied_kernel, candidate) == before

    for field in result:
        bad = deepcopy(result)
        del bad[field]
        reject(bad)
    for field, value in (("cardinality", True), ("charged_failures", True),
                         ("charged_failures", 0), ("subproblem_vertices", [])):
        bad = deepcopy(result)
        bad[field] = value
        reject(bad)
    for field, value in (("n", True), ("n", 0), ("edges", []), ("edge_ids", [1])):
        bad = deepcopy(result)
        bad["subproblem"][field] = value
        reject(bad)
    bad = deepcopy(result)
    bad["subproblem"]["edges"][0][0] = bool(bad["subproblem"]["edges"][0][0])
    reject(bad)
    bad = deepcopy(result)
    del bad["subproblem_result"]["certificate"]
    reject(bad)
    bad = deepcopy(result)
    bad["matching"] = [{"u": 7, "v": 1, "id": 1, "input_index": 0}]
    reject(bad)  # Feasible in the original graph, but uses a failed edge.
    bad = deepcopy(result)
    bad["matching"] = []
    bad["cardinality"] = 0
    reject(bad)  # Feasible but not maximum.
    bad_kernel = deepcopy(kernel)
    bad_kernel["vertices"] = []
    reject(supplied_kernel=bad_kernel)
    for ids in ([True], [1.0], ["unknown"], [1, 1], [1, "1"]):
        reject(ids=ids)
    for vertices in ([True], [-1], [8], [0, 0], [1]):
        reject(vertices=vertices)
    reject(ids=["1"])  # A certificate for another query is not interchangeable.

    # Full-graph feasibility plus equal optimum is sufficient: a different
    # optimal native matching need not be the producer's particular lift.
    alternative = deepcopy(result)
    alternative["matching"] = [{"u": 7, "v": 5, "id": "last", "input_index": 2}]
    assert verify_failure_query(graph, kernel, alternative,
                                failed_edge_ids=[1])["optimality_verified"]

    # A fresh interpreter blocks every solver/producer import before loading
    # the verifier. This establishes an executable dependency boundary.
    payload = json.dumps([graph, kernel, result])
    script = '''
import json, sys
sys.path.insert(0, sys.argv[1])
class BlockProducer:
    def find_spec(self, fullname, path=None, target=None):
        if fullname in {"matching", "failure_query", "failure_kernel"}:
            raise AssertionError("verifier imported a producer: " + fullname)
sys.meta_path.insert(0, BlockProducer())
from verify_failure_query import verify_failure_query
graph, kernel, result = json.load(sys.stdin)
assert verify_failure_query(graph, kernel, result, failed_edge_ids=[1])["optimality_verified"]
'''
    subprocess.run([sys.executable, "-B", "-c", script, str(REFERENCE)],
                   input=payload, text=True, check=True)
    print(f"PASS: {rejected} composite-certificate rejections, alternative native optimum, producer-free verification")


if __name__ == "__main__":
    main()
