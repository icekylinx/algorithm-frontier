"""Exact rational supplied-response ridge core, with original row labels.

Copyright 2026 icekylinx. Authored by GPT-6 Astra Pro.
SPDX-License-Identifier: Apache-2.0

This solves unconstrained quadratic objectives. It is not a solver for the
manuscript's arbitrary convex constraints/penalties or a coreset sampler.
"""
from fractions import Fraction as Q
from importance import PSDInstance, rational, solve


def rectangular(rows, count=None):
    rows = tuple(tuple(rational(x) for x in row) for row in rows)
    if count is not None and len(rows) != count:
        raise ValueError("inconsistent row count")
    width = len(rows[0]) if rows else 0
    if any(len(row) != width for row in rows):
        raise ValueError("ragged rational matrix")
    return rows


class Regression:
    def __init__(self, design, response_basis, labels, base_regularization=0):
        self.design = rectangular(design)
        self.response_basis = rectangular(response_basis, len(self.design))
        self.base_regularization = rational(base_regularization)
        if self.base_regularization < 0:
            raise ValueError("nonnegative base regularization required")
        self.p = len(self.design[0]) if self.design else 0
        self.q = len(self.response_basis[0]) if self.response_basis else 0
        augmented = tuple(a + b for a, b in zip(self.design, self.response_basis))
        matrices = tuple(tuple(tuple(x * y for y in row) for x in row) for row in augmented)
        n = self.p + self.q
        background = tuple(tuple(self.base_regularization if i == j and i < self.p else Q(0)
                                 for j in range(n)) for i in range(n))
        self.psd = PSDInstance(matrices, tuple(labels), background)

    def _query(self, transform, regularization, failed, weights):
        transform = rectangular(transform, self.q)
        regularization = rational(regularization)
        if regularization < self.base_regularization:
            raise ValueError("regularization is below the supplied lower endpoint")
        width = len(transform[0]) if transform else 0
        responses = tuple(tuple(sum((b[j] * transform[j][k] for j in range(self.q)), Q(0))
                                for k in range(width)) for b in self.response_basis)
        selected = self.psd.survivors(failed)
        weights = ((Q(1),) * len(self.design) if weights is None
                   else tuple(rational(x) for x in weights))
        if len(weights) != len(self.design) or any(x < 0 for x in weights):
            raise ValueError("nonnegative original-row weights required")
        return responses, regularization, selected, weights, width

    def normal_equations(self, transform, regularization, failed=(), weights=None):
        responses, regularization, selected, weights, width = self._query(
            transform, regularization, failed, weights)
        hessian = tuple(tuple((regularization if u == v else Q(0))
                              + sum((weights[i] * self.design[i][u] * self.design[i][v]
                                     for i in selected), Q(0))
                              for v in range(self.p)) for u in range(self.p))
        rhs = tuple(tuple(sum((weights[i] * self.design[i][u] * responses[i][k]
                               for i in selected), Q(0)) for k in range(width))
                    for u in range(self.p))
        return hessian, rhs

    def solve(self, transform, regularization, failed=(), weights=None):
        return solve(*self.normal_equations(transform, regularization, failed, weights))

    def verify_solution(self, coefficients, transform, regularization, failed=(), weights=None):
        """Search-free exact global optimum certificate for this ridge query."""
        try:
            hessian, rhs = self.normal_equations(transform, regularization, failed, weights)
            coefficients = rectangular(coefficients, self.p)
            width = len(rhs[0]) if rhs else (len(transform[0]) if transform else 0)
            if any(len(row) != width for row in coefficients):
                return False
            return all(sum((hessian[i][j] * coefficients[j][k] for j in range(self.p)), Q(0))
                       == rhs[i][k] for i in range(self.p) for k in range(width))
        except (ValueError, TypeError, AttributeError, IndexError):
            return False

    def objective(self, coefficients, transform, regularization, failed=(), weights=None):
        responses, regularization, selected, weights, width = self._query(
            transform, regularization, failed, weights)
        coefficients = rectangular(coefficients, self.p)
        if any(len(row) != width for row in coefficients):
            raise ValueError("inconsistent coefficient dimensions")
        return (sum((weights[i] * (sum((self.design[i][j] * coefficients[j][k]
                                        for j in range(self.p)), Q(0)) - responses[i][k]) ** 2
                     for i in selected for k in range(width)), Q(0))
                + regularization * sum((x * x for row in coefficients for x in row), Q(0)))
