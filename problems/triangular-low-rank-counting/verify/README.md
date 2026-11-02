# Verification of the exterior endpoint algorithm

Run from the repository root:

```sh
PYTHONDONTWRITEBYTECODE=1 python3 problems/triangular-low-rank-counting/verify/check.py
```

The checker uses only Python's standard library and rewrites the compact [results.json](results.json). It executes the actual [reference recurrence](../reference/exterior.py); it does not substitute an unimplemented asymptotic contraction routine.

The recorded run passed:

| Checked output | Count | Independent comparison |
|---|---:|---|
| Exact integer negative-alpha evaluation | 54 | All permutations grouped by cycle type |
| Exact rooted cycle polynomial | 135 | Cycle-type sums, roots at beginning/middle/end of shuffled order |
| Modular Hamiltonian evaluation | 126 | Single-cycle permutation sums; 54 nonzero outputs |
| Prime-power Hamiltonian evaluation | 25 | Single-cycle sums, with 60 separately checked rooted components |
| Complete marked polynomial | 30 | Ordered color partitions and principal determinants |
| End-to-end integer immanant | 78 | Murnaghan--Nakayama characters and permutation sums |
| Modular immanant extraction control | 390 | Reductions of the exact coefficient table and character output |
| Rational cycle output | 72 | Exhaustive permutation sums over exact fractions |
| Nonreduced-ring cycle output | 72 | Exhaustive sums over `(Z/4Z)[epsilon]/epsilon^2` |
| Nonreduced-ring Hamiltonian output | 12 | Single-cycle sums in that ring |

Additional controls check 105 diagonal deletions, 18 determinants, 18 width-zero outputs, and six nonzero pure-low-rank boundary examples. Matrix orders reach six; supplied widths include zero, one, two, and boundary width three. The triangular order is shuffled and the triangular part is dense with signed entries and nonzero diagonals. Tested fixed moduli are 2, 3, 4, 5, 6, 8, and 9; the prime-power tests reach 16. The run executes 1,901,265 exterior transitions, with at most 167,027 observed endpoint states and 1,007,413 observed coefficient entries.

The modular-extraction controls reduce an already checked exact marked table; they are not additional modular DP executions. The rational and nonreduced tests do execute the generic-ring DP. Rooted component and explicit prime-power wrapper evaluations are both compared with the oracle; transition statistics count the directly instrumented recurrence calls.

The independent character oracle is adapted from the checkpoint's Murnaghan--Nakayama implementation. The principal-determinant oracle enumerates permutations and shares neither endpoint states nor wedge signs with the reference algorithm. The complete marked-table test joins the checkpoint's formerly separate algorithm and Schur-extraction checks.

These are finite software checks. The proof establishes the all-ring identities, state sufficiency, asymptotic running time, and circuit uniformity. No benchmark, formal proof, exhaustive priority search, or unrestricted dense counting result is inferred from the recorded run.

Authors: icekylinx and GPT-6 Astra Pro. Apache-2.0.
