"""Pure input normalization and the proved sparse degree-to-matching map.

This module performs no matching search. Both the solver and certificate
verifier rebuild the same deterministic reduction from the original request.
The reduction's mathematical proof is in ../proof.md, Sections 2--5.
"""
from __future__ import annotations

from dataclasses import dataclass
from functools import lru_cache
import importlib.util
from pathlib import Path
from typing import Iterable


FORMAT = "algorithm-frontier-degree-v1"
OBJECTIVES = ("feasible", "minimum", "maximum")


@dataclass
class Problem:
    n: int
    edges: list[tuple[int, int]]
    labels: list[int | str]
    lower: list[int]
    upper: list[int]
    low: int
    high: int
    objective: str
    active: list[int]
    active_edges: list[tuple[int, int]]
    failure: dict | None


@dataclass
class Reduction:
    n: int
    edges: list[tuple[int, int]]
    native_index: list[int | None]
    failure: dict | None = None


def normalize(n: int, edges: Iterable[tuple[int, int]],
              lower: Iterable[int] | None = None,
              upper: Iterable[int] | None = None,
              edge_ids: Iterable[int | str] | None = None,
              cardinality: tuple[int, int] | list[int] | None = None,
              objective: str = "feasible") -> Problem:
    if type(n) is not int or n < 0:
        raise ValueError("n must be a nonnegative integer")
    if objective not in OBJECTIVES:
        raise ValueError("objective must be feasible, minimum or maximum")
    native = []
    degree = [0] * n
    for index, edge in enumerate(edges):
        if not isinstance(edge, (list, tuple)) or len(edge) != 2:
            raise ValueError(f"edge {index} must contain two endpoints")
        u, v = edge
        if type(u) is not int or type(v) is not int or not (0 <= u < n and 0 <= v < n):
            raise ValueError(f"edge {index} has an invalid vertex")
        if u == v:
            raise ValueError("the degree-factor reduction requires a loopless graph")
        native.append((u, v))
        degree[u] += 1
        degree[v] += 1
    labels = list(range(len(native))) if edge_ids is None else list(edge_ids)
    if len(labels) != len(native) or any(type(x) not in (int, str) for x in labels):
        raise ValueError("edge_ids must give one integer or string per edge record")
    ordered = sorted((0 if type(x) is int else 1, x) for x in labels)
    if any(a == b for a, b in zip(ordered, ordered[1:])):
        raise ValueError("edge IDs must be distinct")
    g = [0] * n if lower is None else list(lower)
    requested_upper = degree.copy() if upper is None else list(upper)
    if len(g) != n or len(requested_upper) != n:
        raise ValueError("lower and upper must each have n entries")
    if any(type(x) is not int or x < 0 for x in g + requested_upper):
        raise ValueError("degree bounds must be nonnegative integers")
    f = [min(bound, available) for bound, available in zip(requested_upper, degree)]
    if cardinality is None:
        lo, hi = 0, len(native)
    else:
        if (not isinstance(cardinality, (list, tuple)) or len(cardinality) != 2
                or any(type(x) is not int for x in cardinality)):
            raise ValueError("cardinality must be a pair of integer endpoints")
        lo, hi = max(0, cardinality[0]), min(len(native), cardinality[1])
    failure = None
    for vertex, (needed, available) in enumerate(zip(g, f)):
        if needed > available:
            failure = dict(reason="required_degree_exceeds_upper", vertex=vertex,
                           required=needed, available=available)
            break
    if failure is None and lo > hi:
        failure = dict(reason="empty_cardinality_interval", low=lo, high=hi)
    active = [v for v, d in enumerate(degree) if d]
    local = [-1] * n
    for index, vertex in enumerate(active):
        local[vertex] = index
    active_edges = [(local[u], local[v]) for u, v in native]
    return Problem(n, native, labels, g, f, lo, hi, objective,
                   active, active_edges, failure)


def from_json(request: dict) -> Problem:
    if not isinstance(request, dict) or "n" not in request or "edges" not in request:
        raise ValueError("input must be an object containing n and edges")
    return normalize(request["n"], request["edges"], request.get("lower"),
                     request.get("upper"), request.get("edge_ids"),
                     request.get("cardinality"), request.get("objective", "feasible"))


def _network(size: int):
    """A recursive rearrangeable network; size is a positive power of two."""
    next_position = 0
    arcs: list[tuple[int, int]] = []

    def allocate(count):
        nonlocal next_position
        block = list(range(next_position, next_position + count))
        next_position += count
        return block

    def build(width):
        if width == 1:
            only = allocate(1)
            return only, only
        inputs, outputs = allocate(width), allocate(width)
        first_in, first_out = build(width // 2)
        second_in, second_out = build(width // 2)
        for pair in range(width // 2):
            for endpoint in inputs[2*pair:2*pair+2]:
                arcs.extend(((endpoint, first_in[pair]), (endpoint, second_in[pair])))
            for endpoint in outputs[2*pair:2*pair+2]:
                arcs.extend(((first_out[pair], endpoint), (second_out[pair], endpoint)))
        return inputs, outputs

    inputs, outputs = build(size)
    return next_position, arcs, inputs, outputs


def reduce_interval(problem: Problem, low: int, high: int) -> Reduction:
    """Encode the given cardinality subinterval; all original IDs stay passive."""
    if problem.failure is not None:
        return Reduction(0, [], [], problem.failure)
    if not (problem.low <= low <= high <= problem.high):
        raise ValueError("reduction interval must be a nonempty subset of the request")
    edges = problem.active_edges.copy()
    original = list(range(len(edges)))
    lower = [problem.lower[v] for v in problem.active]
    upper = [problem.upper[v] for v in problem.active]

    # First hub: cardinality becomes a degree interval at one new vertex.
    if (low, high) != (0, len(problem.edges)):
        total = sum(upper)
        deficit = sum(f-g for g, f in zip(lower, upper))
        hub_low, hub_high = max(0, total-2*high), min(deficit, total-2*low)
        if hub_low > hub_high:
            return Reduction(0, [], [], dict(reason="empty_cardinality_hub_interval",
                                             low=hub_low, high=hub_high))
        hub = len(lower)
        for vertex, (g, f) in enumerate(zip(lower, upper)):
            for _ in range(f-g):
                edges.append((vertex, hub))
                original.append(None)
        lower, upper = [*upper, hub_low], [*upper, hub_high]

    # Second hub and private triangles convert all intervals to exact degrees.
    if lower != upper:
        hub = len(lower)
        deficit = sum(f-g for g, f in zip(lower, upper))
        target = deficit + ((sum(upper)-deficit) % 2)
        for vertex, (g, f) in enumerate(zip(lower, upper)):
            for _ in range(f-g):
                edges.append((vertex, hub))
                original.append(None)
        prescribed = [*upper, target]
        for _ in range(target // 2):
            p, q = len(prescribed), len(prescribed)+1
            prescribed.extend((1, 1))
            edges.extend(((hub, p), (p, q), (q, hub)))
            original.extend((None, None, None))
    else:
        prescribed = upper
    if sum(prescribed) % 2:
        return Reduction(0, [], [], dict(reason="odd_prescribed_degree_sum"))

    ports: list[list[int]] = [[] for _ in prescribed]
    reduced_edges = []
    native_index = []
    for index, (u, v) in enumerate(edges):
        left, right = 2*index, 2*index+1
        ports[u].append(left)
        ports[v].append(right)
        reduced_edges.append((left, right))
        native_index.append(original[index])
    next_vertex = 2*len(edges)
    for vertex, (incidences, required) in enumerate(zip(ports, prescribed)):
        degree = len(incidences)
        if not 0 <= required <= degree:
            return Reduction(0, [], [], dict(reason="augmented_degree_shortage",
                                             vertex=vertex, required=required, available=degree))
        local_count = degree-required
        if local_count == 0:
            # The count identity forces all ports to use cross edges. The
            # omitted selector would consist solely of its idle matching.
            continue
        width = 1 << (degree-1).bit_length()
        count, arcs, inputs, outputs = _network(width)
        offset = next_vertex
        next_vertex += 2*count
        for position in range(count):
            reduced_edges.append((offset+2*position, offset+2*position+1))
        for u, v in arcs:
            reduced_edges.append((offset+2*u+1, offset+2*v))
        for port, position in zip(incidences, inputs):
            reduced_edges.append((port, offset+2*position))
        for position in outputs[:local_count]:
            reduced_edges.append((offset+2*position+1, next_vertex))
            next_vertex += 1
    native_index.extend([None] * (len(reduced_edges)-len(native_index)))
    return Reduction(next_vertex, reduced_edges, native_index)


@lru_cache(maxsize=2)
def matching_module(name: str):
    if name not in ("matching", "verify_certificate"):
        raise ValueError("unsupported reference module")
    path = Path(__file__).resolve().parents[2] / "general-matching" / "reference" / (name+".py")
    spec = importlib.util.spec_from_file_location("degree_reference_"+name, path)
    if spec is None or spec.loader is None:
        raise ImportError(f"cannot load the local matching module: {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module
