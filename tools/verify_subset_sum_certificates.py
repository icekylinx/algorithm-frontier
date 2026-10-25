#!/usr/bin/env python3
"""Exhaustively replay the finite Subset Sum decision/witness contract.

This validates only the public card's input/output contract on small signed
instances; it is not a verification of the asymptotic algorithms.
"""
from __future__ import annotations

from itertools import combinations, product


def solve(weights: tuple[int, ...], target: int) -> tuple[bool, tuple[int, ...]]:
    states: dict[int, tuple[int, ...]] = {0: ()}
    for index, value in enumerate(weights):
        for total, witness in list(states.items()):
            candidate = total + value
            if candidate not in states:
                states[candidate] = witness + (index,)
    witness = states.get(target)
    return (witness is not None, witness or ())


def brute(weights: tuple[int, ...], target: int) -> bool:
    for mask in range(1 << len(weights)):
        if sum(weights[i] for i in range(len(weights)) if mask >> i & 1) == target:
            return True
    return False


def main() -> None:
    cases = 0
    for n in range(0, 7):
        for weights in product(range(-2, 3), repeat=n):
            for target in range(-6, 7):
                expected = brute(weights, target)
                answer, witness = solve(weights, target)
                if answer != expected:
                    raise AssertionError((weights, target, answer, expected))
                if answer:
                    if len(set(witness)) != len(witness) or any(i < 0 or i >= n for i in witness):
                        raise AssertionError(f"invalid witness: {weights}, {target}, {witness}")
                    if sum(weights[i] for i in witness) != target:
                        raise AssertionError(f"wrong witness sum: {weights}, {target}, {witness}")
                cases += 1
    print(f"subset-sum finite certificate checks passed ({cases} cases)")


if __name__ == "__main__":
    main()
