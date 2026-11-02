# Exact finite circuit and orientation checks

[Statement](../README.md) · [Proof](../proof.md) · [Complete mathematical source](../circuits.tex) · [Source map](../sources.md)

Run from the repository root with Python 3.10 or later, without `-O` because assertions are part of the validators:

```sh
python3 -B manuscripts/partial-transpose-circuits/verify/check_circuit_frontier.py
python3 -B manuscripts/partial-transpose-circuits/verify/check_homogeneous_projection.py
python3 -B manuscripts/partial-transpose-circuits/verify/check_interleaved_composition.py
```

All three use only the Python standard library. The composition checker uses explicit coordinate permutations and integer-list matrices, including for unequal local dimensions. It can run with `python3 -I -S -B` to exclude installed third-party packages. All three were executed successfully on November 2, 2026. Each regenerates its adjacent JSON receipt; timestamps and elapsed times are informational, while counts and fixed seeds describe the reproducible finite workload.

| Native check | Executed scope |
|---|---|
| [Shared frontier](check_circuit_frontier.py), [receipt](frontier_results.json) | 160 shared set-multilinear DAGs, 576 frontier calls and 2,304 identities over the integers and the fields of orders 2, 3 and 101. Checks balanced factors, complementary context scopes and an explicit linear bound on added context gates. A separate 24-case control checks orientation uniqueness across differing partitions. The incorrect doubling construction is rejected over the integers and characteristic two. |
| [Lazy projection](check_homogeneous_projection.py), [receipt](projection_results.json) | 160 ordinary homogeneous DAGs and 128 recursively restricted factor calls; 1,152 frontier identities and 1,832 product-projection identities in the same four rings. Includes 403 products with repeated blocks, shared squares and formal positive-degree zero gates. The squarefree coefficient of a shared square distinguishes integers from characteristic two. |
| [Interleaved composition](check_interleaved_composition.py), [receipt](interleaved_composition_results.json) | 24 actual matrix-factor certificates with differing interleaved scopes and unequal local dimensions, checking 14,848 integer entries and 144 whole-matrix reductions modulo 2, 3, 4, 6, 8 and 101. Every orientation gets one factor column from each product. All 24 controls omitting the required left/right covariance interchange fail. |

The frontier programs retain an equivalent balanced-child stopping convention from the archive, while the manuscript proves the marked-product convention explicitly. They both combine incoming contexts in a shared DAG. The composition program uses the elementary integral identity on two latent dimensions to isolate the new orientation machinery. It does not implement the asymptotic Schur construction; that primitive has its own canonical [source proof and finite checks](../../../problems/noncommutative-crossing/verify/README.md).

These exact finite identities supplement the mathematical proof. They do not certify the partition asymptotic, asymptotic complexity, all arithmetic circuits, arbitrary coefficient evaluation, geometric closure or publication priority. No formal verification or external peer review is claimed. The retained TeX has no unresolved local labels or bibliography references; no PDF build is claimed.

**Attribution:** icekylinx and GPT-6 Astra Pro. Apache-2.0 under the repository [license](../../../LICENSE).
