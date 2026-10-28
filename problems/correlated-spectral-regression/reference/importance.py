"""Exact rational PSD importance, supplied-pool scores and certificates.

Copyright 2026 icekylinx. Authored by GPT-6 Astra Pro.
SPDX-License-Identifier: Apache-2.0

No random pools or sparsifier are sampled here. Singular PSD matrices use a
certified rational generalized inverse, not floating-point pseudoinverses.
"""
from dataclasses import dataclass
from fractions import Fraction as Q
from math import comb


def rational(x):
    if type(x) not in (int, Q):
        raise ValueError("exact integer/Fraction data required")
    return Q(x)


def square(rows, size=None):
    rows = tuple(tuple(rational(x) for x in row) for row in rows)
    n = len(rows) if size is None else size
    if len(rows) != n or any(len(row) != n for row in rows):
        raise ValueError("inconsistent square matrix dimensions")
    return rows


def zero(n):
    return tuple((Q(0),) * n for _ in range(n))


def add(a, b, scale=1):
    return tuple(tuple(x + scale * y for x, y in zip(row, other))
                 for row, other in zip(a, b))


def multiply(a, b):
    n = len(a)
    return tuple(tuple(sum((a[i][k] * b[k][j] for k in range(n)), Q(0))
                       for j in range(n)) for i in range(n))


def trace_product(a, b):
    return sum((a[i][j] * b[j][i] for i in range(len(a)) for j in range(len(a))), Q(0))


def psd_pivots(a):
    """Exact symmetric Schur elimination, rejecting every indefinite input."""
    a = square(a)
    n = len(a)
    if any(a[i][j] != a[j][i] for i in range(n) for j in range(n)):
        raise ValueError("matrix must be symmetric")
    residual, pivots = [list(row) for row in a], []
    for j in range(n):
        pivot = residual[j][j]
        if pivot < 0:
            raise ValueError("matrix is not positive semidefinite")
        if not pivot:
            if any(residual[j][i] for i in range(j + 1, n)):
                raise ValueError("zero PSD pivot has a nonzero residual row")
            continue
        pivots.append(j)
        for u in range(j + 1, n):
            for v in range(j + 1, n):
                residual[u][v] -= residual[u][j] * residual[j][v] / pivot
    return tuple(pivots)


def solve(a, rhs):
    """Exact consistent square system with one/multiple RHS columns; free=0."""
    a = square(a)
    rhs = tuple(tuple(rational(x) for x in row) for row in rhs)
    n = len(a)
    if len(rhs) != n or (rhs and any(len(row) != len(rhs[0]) for row in rhs)):
        raise ValueError("inconsistent right-hand-side dimensions")
    width = len(rhs[0]) if rhs else 0
    rows = [list(row) + list(other) for row, other in zip(a, rhs)]
    pivots = []
    for j in range(n):
        found = next((i for i in range(len(pivots), n) if rows[i][j]), None)
        if found is None:
            continue
        p = len(pivots)
        rows[p], rows[found] = rows[found], rows[p]
        scale = rows[p][j]
        rows[p] = [x / scale for x in rows[p]]
        for i in range(n):
            if i != p:
                scale = rows[i][j]
                rows[i] = [x - scale * y for x, y in zip(rows[i], rows[p])]
        pivots.append(j)
    if any(any(row[n:]) for row in rows[len(pivots):]):
        raise ValueError("inconsistent linear system")
    output = [[Q(0)] * width for _ in range(n)]
    for i, j in enumerate(pivots):
        output[j] = rows[i][n:]
    return tuple(tuple(row) for row in output)


def generalized_inverse(a):
    """A rational PSD G satisfying A G A=A, using a PD principal minor."""
    pivots = psd_pivots(a)
    r, n = len(pivots), len(a)
    minor = tuple(tuple(a[i][j] for j in pivots) for i in pivots)
    inverse = solve(minor, tuple(tuple(Q(i == j) for j in range(r)) for i in range(r)))
    output = [list(row) for row in zero(n)]
    for i, u in enumerate(pivots):
        for j, v in enumerate(pivots):
            output[u][v] = inverse[i][j]
    return tuple(tuple(row) for row in output)


def _labels(values):
    values = frozenset(values)
    if any(type(x) is not int or x < 0 for x in values):
        raise ValueError("nonnegative original label IDs required")
    return values


def _ids(values, n):
    values = tuple(values)
    if (len(set(values)) != len(values)
            or any(type(i) is not int or not 0 <= i < n for i in values)):
        raise ValueError("distinct original item IDs required")
    return values


@dataclass(frozen=True)
class MassCertificate:
    items: tuple
    inverse: tuple
    masses: tuple

    @property
    def total(self):
        return sum(self.masses, Q(0))


@dataclass(frozen=True)
class OneFailure:
    labels: tuple
    scenarios: tuple  # no failure first, then one deletion for each listed label
    scores: tuple
    accounting_bound: Q


@dataclass(frozen=True)
class PoolScores:
    failures: int
    pools: tuple
    baseline: MassCertificate
    certificates: tuple
    scores: tuple
    gamma: Q

    @property
    def total(self):
        return sum(self.scores, Q(0))


@dataclass(frozen=True)
class Plan:
    mode: str  # EMPTY, FULL_INPUT, POOLS_NEEDED, ORDINARY_SCORES
    gamma: Q
    scenarios: int
    pool_count: int
    sample_cap: int
    weights: tuple | None


@dataclass(frozen=True)
class PSDInstance:
    matrices: tuple
    labels: tuple
    background: tuple | None = None

    def __post_init__(self):
        matrices = tuple(square(a) for a in self.matrices)
        labels = tuple(_labels(item) for item in self.labels)
        n = len(matrices[0]) if matrices else (len(self.background) if self.background is not None else 0)
        if len(labels) != len(matrices) or any(len(a) != n for a in matrices):
            raise ValueError("inconsistent item dimensions or label count")
        background = zero(n) if self.background is None else square(self.background, n)
        for a in (*matrices, background):
            psd_pivots(a)
        object.__setattr__(self, "matrices", matrices)
        object.__setattr__(self, "labels", labels)
        object.__setattr__(self, "background", background)

    @property
    def dimension(self):
        return len(self.background)

    @property
    def universe(self):
        return tuple(sorted(set().union(*self.labels))) if self.labels else ()

    def survivors(self, failed=()):
        failed = _labels(failed)
        return tuple(i for i, item in enumerate(self.labels) if not item & failed)

    def total(self, items=None, weights=None):
        items = tuple(range(len(self.matrices))) if items is None else _ids(items, len(self.matrices))
        weights = ((Q(1),) * len(self.matrices) if weights is None
                   else tuple(rational(x) for x in weights))
        if len(weights) != len(self.matrices) or any(x < 0 for x in weights):
            raise ValueError("nonnegative original-item weights required")
        answer = zero(self.dimension)
        for i in items:
            answer = add(answer, self.matrices[i], weights[i])
        return answer

    def masses(self, items=None):
        items = tuple(range(len(self.matrices))) if items is None else _ids(items, len(self.matrices))
        inverse = generalized_inverse(add(self.background, self.total(items)))
        selected = frozenset(items)
        masses = tuple(trace_product(a, inverse) if i in selected else Q(0)
                       for i, a in enumerate(self.matrices))
        return MassCertificate(items, inverse, masses)

    def verify_masses(self, certificate):
        """Search-free check: original sum, A G A=A and every trace value."""
        try:
            if type(certificate) is not MassCertificate:
                return False
            items = _ids(certificate.items, len(self.matrices))
            if type(certificate.items) is not tuple:
                return False
            inverse = square(certificate.inverse, self.dimension)
            if any(inverse[i][j] != inverse[j][i]
                   for i in range(self.dimension) for j in range(self.dimension)):
                return False
            a = add(self.background, self.total(items))
            if multiply(multiply(a, inverse), a) != a:
                return False
            selected = frozenset(items)
            expected = tuple(trace_product(b, inverse) if i in selected else Q(0)
                             for i, b in enumerate(self.matrices))
            return (type(certificate.masses) is tuple
                    and tuple(rational(x) for x in certificate.masses) == expected
                    and all(x >= 0 for x in expected))
        except (ValueError, TypeError, AttributeError, IndexError):
            return False

    def one_failure(self):
        universe = self.universe
        baseline = self.masses()
        scenarios = (baseline,) + tuple(self.masses(self.survivors((c,))) for c in universe)
        scores = tuple(max(c.masses[i] for c in scenarios) for i in range(len(self.matrices)))
        bound = (baseline.total + sum((len(item) * t for item, t in zip(self.labels, baseline.masses)), Q(0))
                 - sum((baseline.total - c.total for c in scenarios[1:]), Q(0)))
        return OneFailure(universe, scenarios, scores, bound)

    def verify_one_failure(self, certificate):
        try:
            if (type(certificate) is not OneFailure or certificate.labels != self.universe
                    or len(certificate.scenarios) != len(self.universe) + 1):
                return False
            expected_items = (tuple(range(len(self.matrices))),) + tuple(
                self.survivors((c,)) for c in self.universe)
            if any(c.items != items or not self.verify_masses(c)
                   for c, items in zip(certificate.scenarios, expected_items)):
                return False
            baseline = certificate.scenarios[0]
            expected_scores = tuple(max(c.masses[i] for c in certificate.scenarios)
                                    for i in range(len(self.matrices)))
            bound = (baseline.total + sum((len(item) * t for item, t in zip(self.labels, baseline.masses)), Q(0))
                     - sum((baseline.total - c.total for c in certificate.scenarios[1:]), Q(0)))
            return (type(certificate.scores) is tuple
                    and tuple(rational(x) for x in certificate.scores) == expected_scores
                    and rational(certificate.accounting_bound) == bound
                    and sum(expected_scores, Q(0)) <= bound
                    <= (1 + max(map(len, self.labels), default=0)) * baseline.total)
        except (ValueError, TypeError, AttributeError, IndexError):
            return False

    def pool_scores(self, failures, pools):
        gamma, _, _ = parameters(self.labels, failures)
        pools = tuple(_labels(pool) for pool in pools)
        if not pools:
            raise ValueError("a nonempty supplied pool list is required")
        baseline = self.masses()
        certificates = tuple(self.masses(tuple(i for i, item in enumerate(self.labels) if item <= pool))
                             for pool in pools)
        scores = tuple(baseline.masses[i] + 2 * gamma / len(pools)
                       * sum((c.masses[i] for c in certificates), Q(0))
                       for i in range(len(self.matrices)))
        return PoolScores(failures, pools, baseline, certificates, scores, gamma)

    def verify_pool_scores(self, certificate):
        try:
            if type(certificate) is not PoolScores or not certificate.pools:
                return False
            gamma, _, _ = parameters(self.labels, certificate.failures)
            if (gamma != rational(certificate.gamma) or len(certificate.pools) != len(certificate.certificates)
                    or certificate.baseline.items != tuple(range(len(self.matrices)))
                    or not self.verify_masses(certificate.baseline)):
                return False
            for pool, c in zip(certificate.pools, certificate.certificates):
                pool = _labels(pool)
                ids = tuple(i for i, item in enumerate(self.labels) if item <= pool)
                if c.items != ids or not self.verify_masses(c):
                    return False
            expected = tuple(certificate.baseline.masses[i] + 2 * gamma / len(certificate.pools)
                             * sum((c.masses[i] for c in certificate.certificates), Q(0))
                             for i in range(len(self.matrices)))
            return (type(certificate.scores) is tuple
                    and tuple(rational(x) for x in certificate.scores) == expected
                    and sum(expected, Q(0)) <= (1 + 2 * gamma) * certificate.baseline.total)
        except (ValueError, TypeError, AttributeError, IndexError):
            return False

    def verify_embedding(self, weights, failed=(), error=Q(1, 4)):
        """Exact all-vector check for this explicitly supplied failure scenario."""
        try:
            error = rational(error)
            if not 0 < error < 1:
                return False
            ids = self.survivors(failed)
            original = add(self.background, self.total(ids))
            selected = add(self.background, self.total(ids, weights))
            psd_pivots(add(selected, original, -(1 - error)))
            psd_pivots(add(original, selected, -1 / (1 + error)))
            return True
        except (ValueError, TypeError, AttributeError, IndexError):
            return False

    def plan(self, failures, error, failure_probability):
        """Conservative exact preflight; POOLS_NEEDED is not a sampled summary."""
        error, delta = rational(error), rational(failure_probability)
        if not 0 < error < 1 or not 0 < delta < 1:
            raise ValueError("accuracy/confidence must lie strictly between zero and one")
        gamma, scenarios, h = parameters(self.labels, failures)
        rho = self.masses().total
        count = len(self.matrices)
        if not count or rho <= error:
            return Plan("EMPTY", gamma, scenarios, 0, 0, (Q(0),) * count)
        log_bound = _ceil_log2(Q(4 * max(1, self.dimension) * scenarios) / delta)
        cap = _ceil(48 * gamma * rho * log_bound / (error * error))
        if cap >= count:
            return Plan("FULL_INPUT", gamma, scenarios, 0, cap, (Q(1),) * count)
        if not h or not any(self.labels):
            return Plan("ORDINARY_SCORES", gamma, scenarios, 0, cap, None)
        pools = _ceil(8 * gamma * _ceil_log2(Q(4 * count * scenarios) / delta))
        return Plan("POOLS_NEEDED", gamma, scenarios, pools, cap, None)


def parameters(labels, failures):
    if type(failures) is not int or failures < 0:
        raise ValueError("nonnegative integer failure budget required")
    universe = set().union(*labels) if labels else set()
    h, d = min(failures, len(universe)), max(map(len, labels), default=0)
    gamma = Q((h + d) ** (h + d), h ** h * d ** d) if h and d else Q(1)
    return gamma, sum(comb(len(universe), j) for j in range(h + 1)), h


def _ceil(x):
    return -(-x.numerator // x.denominator)


def _ceil_log2(x):
    """Positive integer upper bound on ln(x), computed with rational shifts."""
    if x <= 1:
        return 1
    exponent = max(0, x.numerator.bit_length() - x.denominator.bit_length())
    if x.denominator << exponent < x.numerator:
        exponent += 1
    return max(1, exponent)
