# Verification and scope

[Main proof](../proof.md) · [Source dependencies](../sources.md)

## Manuscript readiness in a named scope

**Partially ready for review: deterministic stabilizer witnesses.** The
bounded manuscript audit of 2026-10-27 reconstructs the Pauli surrogate and
witness theorem in [main-proof Theorem 5](../proof.md#5-a-classical-stabilizer-witness)
and the prime-dimensional individual-check extension in
[witness-manuscript Corollary 2](../manuscripts/commuting-surrogates-and-stabilizer-energy-witnesses.md#6-prime-dimensional-weyl-checks).
For the Pauli theorem it checks every pairwise PSD comparison, the commuting
residual, complete-basis pinching, equality of original and surrogate energy
on basis states, and the ground-energy implication. For the prime-dimensional
extension it checks the constant-angle projector identity, both pinching
cases, and the resulting factor calculation. In both cases it checks the
exact scalar-plus-affine objective, phase-aware tableau output, exponential
enumeration time, and polynomial workspace. These are manuscript arguments;
the shared arithmetic checker below is not evidence for these quantum
conclusions.

The Pauli reduction is polynomial time and its exact objective search takes
the stated exponential time in the number of independent diagonal labels.
The prime-dimensional reduction is polynomial in the compact input and its
search enumerates the complete finite-field basis assignments. Neither
statement asserts polynomial-time minimization of the remaining classical
objective. Standard compact symplectic linear algebra is identified in the
[witness dependency map](../sources.md#audited-witness-scope).

This audit does not mark the full sparsification family ready. The sharp
whole-block support theorem also uses the shared subgroup/affine-group
Gaussian construction; the compact theorem uses the subgroup-order oracle,
rational quotient surrogate, and adaptive resparsification; the two failure
theorems have separate importance or global-commutation dependencies. Those
full dependency chains and the joint lower bounds were not reconstructed in
this bounded witness audit. They retain their stated theorems and named
dependencies; exclusion here is an audit boundary, not a finding that those
proofs are incomplete. External peer review and proof-assistant verification
are not claimed.

## Available finite arithmetic evidence

The shared [composite-modulus quotient-rounding checker](../../group-metric-constraints/verify/check_quotient_rounding.py) can be run from the repository root:

~~~sh
python3 problems/group-metric-constraints/verify/check_quotient_rounding.py
~~~

It enumerates six fixed whole blocks in <code class="math">\mathbb Z_6^3</code>, all 64 subsets, and all 4,096 ordered subset pairs. It checks rational logarithm enclosures, fixed-denominator rounding, preservation of zero marginals, positive gaps, and submodularity.

This exercises a finite arithmetic component of the compact rank interface. It does not certify HNF subgroup orders, test the quantum operator identities, or establish the all-state sparsification theorem. There is no dedicated executable for those general quantum claims.

## Symbolic operator identities

The quantum arguments do not depend on numerical diagonalization.

- For anticommuting involutions,
  <!-- math-display: 39213bfa2a144044a4183a1f
  (aP+bQ)^2=(a^2+b^2)I.
  -->
  ![Formula](../../../assets/math/39213bfa2a144044a4183a1f.svg)
  This gives the pair eigenvalue bounds and commuting-surrogate constants.
- If <code class="math">UV=\zeta VU</code>, sandwiching by the accepted-eigenvalue projector <code class="math">P</code> gives <code class="math">PV^jP=0</code> unless the commutator order divides <code class="math">j</code>. The surviving Fourier terms give projector overlap at most <code class="math">1/\sqrt2</code> for a conflicting pair, including composite and heterogeneous local dimensions.
- Character orthogonality and the trace-zero property of non-scalar Weyl operators give the common multiplicity <code class="math">D&#124;\mathcal C&#124;/&#124;\mathcal H&#124;</code> for a commuting subgroup. The scalar subgroup <code class="math">\mathcal C</code> is part of the formula.

Every output coefficient belongs to a whole original block. Balanced removal of conflicting pairs merges coefficients on shared original blocks; it does not turn block generators into separate selectable items.

## Compact algebra and construction

The physical commuting spectrum is a character torsor with size dividing <code class="math">D</code>. The compact order oracle multiplies the displacement-image order by the scalar-relation order. Omitting the latter would lose inconsistent-phase information. Integer relation lattices, modular products, and gcd computations require no factoring oracle.

The logarithmic rank is passed through an exact rational surrogate before applying the value-oracle backend. The prime-field theorem retains its separate, sometimes smaller, additive <code class="math">\log p</code> dependence. Optimal support and the compact randomized support with logarithmic overhead remain distinct guarantees.

## Energy witnesses and failures

The witness argument uses a complete maximal isotropic space. Pinching fixes its diagonal Paulis and erases the others while preserving every resulting basis-state energy. The classical parity objective is optimized by the stated exponential enumeration; polynomial construction of a commuting surrogate is not polynomial optimization of that objective.

The ordinary theorem allows noncommuting original blocks. Its decomposition is not reused after arbitrary clause deletion. Correlated Pauli failures use a separate hereditary-importance argument, while the exact-label whole-block failure theorem requires global commutation. These are clause deletions as defined in the respective manuscripts, not physical loss of a quantum subsystem.

## Original-input compact Pauli witness checks

```sh
python3 -B problems/quantum-stabilizer/verify/check_witness.py
```

The [checker](check_witness.py) covers 143 original positive-Pauli instances,
532 complete-basis states and 292 independent dense-projector comparisons.
It checks 203 balanced pair records, 148 forged energy/tableau claims and six malformed
inputs. Phase-dependent commuting relations, signed identities, empty inputs
and 100-digit exact weights are included. An 80-qubit rank-one parity objective
uses only two assignments; its original witness verifier still passes with
the producer, optimizer and producer algebra disabled. The independent dense
checks use exact dyadic complex entries. The approximation factor follows
from the [symbolic proof](../reference-realization.md), not finite numerical
spectral experiments. No quantum sparsification backend is implied.

**Attribution:** icekylinx and GPT-6 Astra Pro.
