# Sources and proof dependencies: Quantum stabilizer sparsification and witnesses

[Result statements](README.md) · [Main proof](proof.md) · [Verification and scope](verify/README.md)

The main proof gives the family-level theorem composition. The following canonical manuscripts contain the detailed arguments and the hypotheses of each algorithmic interface.

## Audited witness scope

The deterministic witness results have a separate proof route from the
sparsification theorems. [Theorem 5 of the main proof](proof.md#5-a-classical-stabilizer-witness)
and [Theorem 1 and Corollary 2 of the witness manuscript](manuscripts/commuting-surrogates-and-stabilizer-energy-witnesses.md)
use balanced peeling, phase-aware symplectic elimination, and pinching in a
complete stabilizer basis. Their operator comparisons follow from the
displayed anticommuting-involution identities and Weyl projector overlap
calculation. The exact parity or finite-field objective includes its scalar
term, and enumeration gives the stated stabilizer tableau in polynomial
space.

This scope uses standard compact Pauli/Weyl and stabilizer linear algebra,
with Hostens--Dehaene--De Moor as the algebraic reference below. It does not
invoke Quanrud, rational quotient ranks, Gaussian partial coloring, adaptive
resparsification, or correlated importance pools. Readiness for this witness
scope therefore does not depend on certifying those separate sparsification
backends. It also does not establish a polynomial-time ground-state optimizer
or an optimal universal stabilizer approximation factor.

## Canonical manuscripts

| Manuscript | Proof role |
|---|---|
| [Positive Pauli Hamiltonians](manuscripts/arbitrary-locality-pauli-sparsification.md) | Locality-independent support, exact coefficient total, and a separate correlated-clause-failure theorem. |
| [Prime-dimensional Weyl checks](manuscripts/arbitrary-locality-prime-qudit-checks.md) | Individual checks as a whole-block corollary and the independent projective-line proof. |
| [Prime-dimensional stabilizer blocks](manuscripts/arbitrary-locality-stabilizer-block-sparsification.md) | Whole-block optimal support and the sharper additive-logarithm compact bound. |
| [Arbitrary-dimensional Weyl checks](manuscripts/arbitrary-dimension-weyl-checks.md) | Individual-check consequences in general local dimensions. |
| [Commuting surrogates and energy witnesses](manuscripts/commuting-surrogates-and-stabilizer-energy-witnesses.md) | Operator comparison, stabilizer witnesses, and the separate exponential objective search. |
| [Heterogeneous whole stabilizer blocks](manuscripts/arbitrary-dimension-whole-stabilizer-blocks.md) | Physical character torsors, exact subgroup orders, compact construction, and joint lower bounds. |

## Shared proof dependencies

| Result | Role |
|---|---|
| [Whole subgroup sparsification](../group-metric-constraints/manuscripts/optimal-whole-subgroup-constraints.md) | The optimal-support commuting-block theorem. |
| [Affine group compilation](../group-metric-constraints/manuscripts/affine-constraints-over-arbitrary-finite-groups.md) | The physical character-coset formulation for whole blocks. |
| [Rational quotient ranks](../group-metric-constraints/manuscripts/rational-quotient-ranks-from-weak-oracles.md) | The exact closure-preserving oracle for compact logarithmic subgroup ranks. |
| [Adaptive quotient resparsification](../label-block-cut/manuscripts/adaptive-quotient-resparsification.md) | The compact constructive support bound. |
| [Globally commuting failure summaries](../label-block-cut/manuscripts/exact-label-whole-blocks-and-hyperedges.md) | The distinct common-eigenbasis theorem for correlated failures of whole stabilizer blocks. |
| [Correlated importance pools](../correlated-spectral-regression/manuscripts/correlated-failure-spectral-and-regression-summaries.md) | The hereditary-importance argument for Pauli clause failures, separate from the ordinary noncommuting decomposition. |

## External inputs

- Quanrud's quotient theorem and the internal adaptive and rational-rank lemmas supply compact construction: <https://kentq.s3.amazonaws.com/submodular-sparsification.pdf>.
- Tropp, *An Introduction to Matrix Concentration Inequalities*: <https://arxiv.org/abs/1501.01571>. Matrix concentration is applied to the uniformly positive part; the algorithm does not compute its whitening.
- Hostens, Dehaene, and De Moor, arbitrary-dimensional Weyl/stabilizer algebra: <https://arxiv.org/abs/quant-ph/0408190>.
- Kannan–Bachem integer normal forms provide exact compact subgroup orders: <https://doi.org/10.1137/0208040>.
- Basu, Kothari, Meka, and Tudose, optimal weighted abelian Cayley support: <https://arxiv.org/html/2607.08261v1>. This supplies the alternative binary/single-check support proof.

**Attribution:** Yilin Liu and GPT-6 Astra Pro.
