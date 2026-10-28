# Copyright 2026 Yilin Liu and GPT-6 Astra Pro
# SPDX-License-Identifier: Apache-2.0
"""Exact free-word oracle, adapted from the checkpoint cyclic-derivative checks."""
from __future__ import annotations

Poly = dict[tuple[str, ...], int]


def add(a: Poly, b: Poly, sign: int = 1) -> Poly:
    out = dict(a)
    for word, coefficient in b.items():
        value = out.get(word, 0) + sign * coefficient
        if value:
            out[word] = value
        else:
            out.pop(word, None)
    return out


def mul(a: Poly, b: Poly) -> Poly:
    out: Poly = {}
    for left, x in a.items():
        for right, y in b.items():
            word = left + right
            out[word] = out.get(word, 0) + x * y
    return {word: value for word, value in out.items() if value}


def var(name: str) -> Poly:
    return {(name,): 1}


def cyclic(a: Poly, name: str) -> Poly:
    out: Poly = {}
    for word, coefficient in a.items():
        for position, letter in enumerate(word):
            if letter == name:
                rotated = word[position + 1:] + word[:position]
                out[rotated] = out.get(rotated, 0) + coefficient
    return {word: value for word, value in out.items() if value}


def residue(a: Poly, modulus: int) -> Poly:
    return {word: value % modulus for word, value in a.items()
            if value % modulus}
