# Exact separation and a conditional-sign obstruction

These are two proved boundary results with different meanings: a compact membership problem is coNP-complete, and a finite represented-matroid example refutes one exact probability inequality.

## Results

**Membership in the binary-code relative-error body <code class="math">Q_a</code>, with <code class="math">a=1/4</code>**

**Conclusion.** coNP-complete

**Exact scope.** Deterministic polynomial reduction; homogeneous binary checks of arity at most two, positive rational weights, and supplied vector in <code class="math">\{0,1/2\}^m</code>

**Proof.** [Proposition 1](manuscripts/exact-separation-for-compact-codes.md)

**Fixed-amplitude one-sided sign-cone probability for the listed rank-three non-Fano representation over <code class="math">\mathbb F_3</code>**

**Conclusion.** Exactly <code class="math">15/128&lt;2^{-3}</code>

**Exact scope.** Deterministic exact count on seven columns and amplitude vector <code class="math">(6,5,3,5,5,5,6)</code>; all ternary row-space queries. The displayed probability belongs to the mathematical random-sign model, not an algorithm's failure event

**Proof.** [Proposition 1](manuscripts/non-fano-obstruction-to-fixed-amplitude-bound.md)

**Direct sum of <code class="math">k</code> copies of the same representation**

**Conclusion.** Rank <code class="math">3k</code>, probability <code class="math">(15/128)^k</code>

**Exact scope.** Independent signs and fixed amplitudes on disjoint coordinate blocks; a deterministic direct-sum construction and exact probability identity

**Proof.** [Direct-sum corollary](manuscripts/non-fano-obstruction-to-fixed-amplitude-bound.md)

## Contract

**Objective and output**

Classify exact membership in a compact partial-coloring body and give an exact counterexample to the proposed fixed-amplitude sign bound.

**Randomness**

Deterministic reductions, explicit constructions and exhaustive exact verification. The non-Fano sign probability describes a mathematical random-sign experiment, not a randomized algorithm or algorithm failure probability.

**Time**

The membership classification uses a polynomial reduction from weighted Max-Cut. The seven-element count is verified by finite exact enumeration, with a complete combinatorial proof in the manuscript.

**Space**

The reduction has polynomial description length. The fixed counterexample requires no asymptotic workspace claim.

**Parameters**

Binary-code dimension and number of checks for the reduction; represented rank three, field <code class="math">\mathbb F_3</code>, and seven positive amplitudes for the obstruction.

**Model and representation**

Exact rational membership and independent uniform signs at fixed amplitudes. The Gaussian amplitude distribution is a different model.

**Lower-bound scope**

Exact compact separation would imply <code class="math">\mathsf{P}=\mathsf{NP}</code>. The non-Fano example refutes the coefficient one in <code class="math">2^{-r}</code> for conditional signs. Neither result proves that compact optimal sparsifiers are impossible or disproves a Gaussian <code class="math">\exp(-Cr)</code> estimate.

**Review status**

The [verification note](verify/README.md) records the proof scope, executable evidence and remaining conditions. No proof-assistant verification or external peer review is claimed.

**Source**

[Proofs](proof.md), [source map](sources.md), [model review](verify/README.md), [finite replay](verify/README.md).

**Attribution:** Yilin Liu and GPT-6 Astra Pro.
