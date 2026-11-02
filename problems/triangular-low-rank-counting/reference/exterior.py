"""Division-free exterior endpoint evaluation on a supplied decomposition.

Authors: icekylinx and GPT-6 Astra Pro. SPDX-License-Identifier: Apache-2.0
Adapted from the checkpoint's check_dag_endpoint_set_dp.py exterior routine.
Uses ordinary Python ring operations, or reduces integer coefficients modulo
``modulus``. Sparse zero omission is an implementation optimization; the proof
unrolls every structurally permitted state into a uniform arithmetic circuit.
"""
from itertools import permutations
from math import comb


def _add(destination, polynomial, multiplier, reduce):
    for masks, coefficient in polynomial.items():
        value = reduce(destination.get(masks, 0) + multiplier * coefficient)
        if value != 0:
            destination[masks] = value
        else:
            destination.pop(masks, None)


def _wedge(polynomial, vector, color, reduce):
    """Append vector on the right; basis vectors are in increasing order."""
    answer = {}
    for masks, coefficient in polynomial.items():
        mask = masks[color]
        for coordinate, entry in enumerate(vector):
            if (mask >> coordinate) & 1:
                continue
            sign = -1 if (mask >> (coordinate + 1)).bit_count() & 1 else 1
            next_masks = list(masks)
            next_masks[color] |= 1 << coordinate
            key = tuple(next_masks)
            value = reduce(answer.get(key, 0) + sign * coefficient * entry)
            if value != 0:
                answer[key] = value
            else:
                answer.pop(key, None)
    return answer


def evaluate(bmat, u, v, order, colors, *, root=None, modulus=None, weights=None):
    """Return (value, finite statistics).

    With no weights, returns per_{-colors}(B+UV^T), or the rooted polynomial
    G_colors if ``root`` is a vertex. With ``weights=(t_1,...,t_q)``, returns
    sum_ordered_partitions product_s t_s^|J_s| det(A[J_s]); root must be None.
    Weights may themselves be elements of an explicit polynomial ring.
    ``order`` is a simultaneous row/column triangular order, not relabeling
    of just one factor. The diagonal of B is allowed to be nonzero.
    """
    n = len(bmat)
    assert n >= 1 and colors >= 1 and sorted(order) == list(range(n))
    assert len(u) == len(v) == n
    width = len(u[0])
    assert all(len(row) == n for row in bmat)
    assert all(len(row) == width for row in u + v)
    position = {vertex: index for index, vertex in enumerate(order)}
    assert all(bmat[i][j] == 0 for i in range(n) for j in range(n)
               if position[i] > position[j])
    assert root is None or 0 <= root < n
    assert weights is None or (root is None and len(weights) == colors)
    assert modulus is None or modulus >= 2
    reduce = (lambda x: x) if modulus is None else (lambda x: x % modulus)
    zero = (0,) * colors
    states = {(): {zero: 1}}
    transitions = 0
    maximum_states = maximum_coefficients = 1
    for vertex in order:
        updated = {}
        for endpoints, polynomial in states.items():
            loop_colors = 1 if vertex == root else colors
            multiplier = (-loop_colors if weights is None else sum(weights)) * bmat[vertex][vertex]
            _add(updated.setdefault(endpoints, {}), polynomial, multiplier, reduce)
            transitions += 1
            for color in ((0,) if vertex == root else range(colors)):
                started = _wedge(polynomial, v[vertex], color, reduce)
                new_endpoints = endpoints + ((vertex, color),)
                multiplier = 1 if weights is None else weights[color]
                _add(updated.setdefault(new_endpoints, {}), started, multiplier, reduce)
                transitions += 1
            for index, (last, color) in enumerate(endpoints):
                if vertex == root and color != 0:
                    continue
                later = sum(other_color == color for _, other_color in endpoints[index + 1:])
                multiplier = bmat[last][vertex] * (-1 if later & 1 else 1)
                if weights is not None:
                    multiplier *= -weights[color]
                new_endpoints = endpoints[:index] + endpoints[index + 1:] + ((vertex, color),)
                _add(updated.setdefault(new_endpoints, {}), polynomial, multiplier, reduce)
                transitions += 1
        states = {state: poly for state, poly in updated.items() if poly}
        maximum_states = max(maximum_states, len(states))
        maximum_coefficients = max(maximum_coefficients, sum(map(len, states.values())))
        assert all(sum(color == s for _, color in state) <= width
                   for state in states for s in range(colors))
    result = 0
    for endpoints, start_wedge in states.items():
        end_wedge = {zero: 1}
        for vertex, color in endpoints:
            end_wedge = _wedge(end_wedge, u[vertex], color, reduce)
        coefficient = sum(value * end_wedge.get(mask, 0) for mask, value in start_wedge.items())
        exponent = 0 if weights is not None else len(endpoints) + (root is not None)
        result = reduce(result + (-1 if exponent & 1 else 1) * coefficient)
    return result, {'transitions': transitions, 'maximum_endpoint_states': maximum_states,
                    'maximum_coefficient_entries': maximum_coefficients}


def hamiltonian_prime_power(bmat, u, v, order, prime, precision, *, root=0):
    """Exact integer matrix HC modulo prime**precision, using <=prime*precision colors.

    The caller supplies a prime; primality testing/factorization are outside the
    algorithm. The finite-difference identity also holds for composite bases.
    """
    assert prime >= 2 and precision >= 1
    modulus = prime ** precision
    result = 0
    for j in range(1, precision + 1):
        value, _ = evaluate(bmat, u, v, order, prime * j, root=root, modulus=modulus)
        result += (-1) ** (j - 1) * comb(precision, j) * value
    return result % modulus


def extract_immanant(marked_coefficients, partition, colors):
    """Extract Imm_{partition'} from H by the integral alternant formula.

    ``partition`` has at most ``colors`` parts; the output immanant therefore
    has diagram width at most ``colors``. No Vandermonde division is used.
    """
    assert len(partition) <= colors
    partition = tuple(partition) + (0,) * (colors - len(partition))
    target = tuple(partition[i] + colors - 1 - i for i in range(colors))
    result = 0
    for p in permutations(range(colors)):
        sign = (-1) ** sum(p[i] > p[j] for i in range(colors) for j in range(i + 1, colors))
        exponent = tuple(target[i] - (colors - 1 - p[i]) for i in range(colors))
        if min(exponent, default=0) >= 0:
            result += sign * marked_coefficients.get(exponent, 0)
    return result
