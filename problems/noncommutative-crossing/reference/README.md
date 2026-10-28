# Finite native Schur crossing components

These exact Python components construct finite normalization-one integral
crossing factors and evaluate their ordered contraction. They realize local
algebraic components of the [proof](../proof.md); the asymptotic theorem also
uses the proved shared-product construction and cited matrix machinery.

`schur_modes.py` implements rational power-sum polynomials, Jacobi–Trudi Schur
functions, the Hall pairing, the triangular state transform, literal normal
ordering and Schur-coordinate conversion. Its finite implementation uses
dense dictionaries and memoization. It does not implement the streaming
coefficient algorithm's asymptotic time and workspace guarantees.

`integral_crossing.py` provides `mixed_factors(h, energy)` for positive integer
weights. The factors are triples `(orientation, left, right)` whose dictionaries
map pairs of partition indices to integer coefficients. All rational
construction finishes before evaluation in a target ring, and integrality
is checked explicitly. The output satisfies the full integer crossing
identity. Optional `orientation="row"` or `"column"` selects one orientation;
`location=s` selects an individual finite crossing piece.

`ordered_evaluation(factors, xs, ys, zero=..., add=..., mul=..., scale=...)`
evaluates those factors with caller-supplied ring operations. `mul` preserves
argument order, and `scale` means central multiplication by an integer.
Callbacks must not mutate their arguments. The returned value is the sum
of `X[x]*Y[y]*X[x]*Y[y]` for a complete crossing. Column-oriented factors
retain their middle `Y[y]*X[v]` order, between the outer `X[x]` and `Y[u]`.

For a small importable example, run from the repository root:

```sh
python3 -B - <<'PY'
import sys
sys.path.insert(0, 'problems/noncommutative-crossing/reference')
from integral_crossing import mixed_factors
from schur_modes import partitions
factors = mixed_factors(2, 2)
print('partition dimensions:', len(partitions(2)), len(partitions(2)))
print('finite nonzero factors:', len(factors))
PY
```

The [verification note](../verify/README.md) gives all runnable checks. Their
references are the literal crossing tensor and direct original ordered
products, including noncommutative matrices over integers and composite
residue rings. No full asymptotic circuit generator or fast matrix backend
is claimed implemented by these finite routines.

**Attribution:** icekylinx and GPT-6 Astra Pro. Apache License 2.0.
