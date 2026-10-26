# Verification and scope

[Main proof](../proof.md) · [Source dependencies](../sources.md)

## Exact finite quotient replay

Run the local [quotient-rounding checker](check_quotient_rounding.py) from the repository root:

~~~sh
python3 problems/group-metric-constraints/verify/check_quotient_rounding.py
~~~

The checker independently enumerates generated subgroups of six explicit whole blocks in $`\mathbb Z_6^3`$. Its subgroup enumeration does not call an HNF implementation.

| Finite domain | Checked quantity |
|---|---:|
| Subsets of the six blocks | 64 |
| Ordered subset pairs | 4,096 |
| Full generated subgroup order | 216 |

For every subset it computes certified rational logarithm intervals and applies the fixed-denominator concave rounding. It checks normalization, monotonicity, exact preservation of zero marginals, and a unit gap for positive marginals. Every ordered pair satisfies both integer-order and rounded submodularity.

This is finite arithmetic evidence for the composite-modulus rounding mechanism and canonical-key cancellation. It is not certification of general subgroup-order computation or the arbitrary-ground-set rationalization theorem. No sampling experiment establishes the Gaussian or universal group bounds.

## Analytic and combinatorial interfaces

| Proof step | Required implication and scope |
|---|---|
| Weight-ordered subset products | First-difference cancellation uses later, at least as heavy, generators. It requires no commutativity; the explicit group order remains in the bound. |
| Total operator importance | The redundancy premise is applied after each whitened item is divided by its own norm. Uniformity under every positive rescaling is essential. |
| Gaussian subgroup comparison | Coordinate variances agree and covariances have the required order. Stationarity yields the reciprocal-query-count bound, including zero variance and ties. |
| Gaussian symmetrization | Dyadic sections, reflection, log-concavity, and Gaussian correlation yield the symmetric-volume bound. The constant dilation in partial coloring is charged to the approximation error. |
| Coset compilation | The swap element normalizes the product subgroup and embedded membership equals the original coset predicate. Neither normality nor a common satisfying assignment is assumed. |
| Metric extension | One action preserves every item's centered Gram matrix. Invariance of only the sum is insufficient. The stated metric theorem concerns unsquared Hilbert distances. |
| Rational ranks | Positive-increment slack dominates rounding errors; zero-increment comparisons cancel through canonical keys. One fixed rank oracle and denominator are used under every restriction. |
| Modular lower bound | Geometric prefixes isolate valuation layers within twice the target error. Powers of two and the stated large-dimension/accuracy regime remain part of the lower bound. |

The quotient backend permits real normalized submodular ranks with positive marginals at least one. The partial-coloring backend requires its stated separation interface. A construction polynomial in the full explicit query table is not thereby polynomial in a compact presentation of the group. Compact modular construction is the separate exact-rank-oracle result.

**Attribution:** Yilin Liu and GPT-6 Astra Pro.
