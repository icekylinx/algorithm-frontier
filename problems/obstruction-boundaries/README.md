# Exact separation and a conditional-sign obstruction

These are two proved boundary results with different meanings: a compact membership problem is coNP-complete, and a finite represented-matroid example refutes one exact probability inequality.

## Results

| Problem | Conclusion | Exact scope | Proof |
|---|---|---|---|
| Membership in the binary-code relative-error body $Q_a$, with $a=1/4$ | coNP-complete | Homogeneous binary checks of arity at most two, positive rational weights, and supplied vector in $\{0,1/2\}^m$ | [Proposition 1](manuscripts/exact-separation-for-compact-codes.md) |
| Fixed-amplitude one-sided sign-cone probability for the listed rank-three non-Fano representation over $\mathbb F_3$ | Exactly $15/128<2^{-3}$ | Seven columns and amplitude vector $(6,5,3,5,5,5,6)$; all ternary row-space queries | [Proposition 1](manuscripts/non-fano-obstruction-to-fixed-amplitude-bound.md) |
| Direct sum of $k$ copies of the same representation | Rank $3k$, probability $(15/128)^k$ | Independent signs and fixed amplitudes on disjoint coordinate blocks | [Direct-sum corollary](manuscripts/non-fano-obstruction-to-fixed-amplitude-bound.md) |

## Contract

| Field | Statement |
|---|---|
| **Objective and output** | Classify exact membership in a compact partial-coloring body and give an exact counterexample to the proposed fixed-amplitude sign bound. |
| **Time** | The membership classification uses a polynomial reduction from weighted Max-Cut. The seven-element count is verified by finite exact enumeration, with a complete combinatorial proof in the manuscript. |
| **Space** | The reduction has polynomial description length. The fixed counterexample requires no asymptotic workspace claim. |
| **Parameters** | Binary-code dimension and number of checks for the reduction; represented rank three, field $\mathbb F_3$, and seven positive amplitudes for the obstruction. |
| **Model and representation** | Exact rational membership and independent uniform signs at fixed amplitudes. The Gaussian amplitude distribution is a different model. |
| **Lower-bound scope** | Exact compact separation would imply $\mathsf{P}=\mathsf{NP}$. The non-Fano example refutes the coefficient one in $2^{-r}$ for conditional signs. Neither result proves that compact optimal sparsifiers are impossible or disproves a Gaussian $\exp(-Cr)$ estimate. |
| **Review status** | The [verification note](verify/README.md) records the proof scope, executable evidence and remaining conditions. No proof-assistant verification or external peer review is claimed. |
| **Source** | [Proofs](proof.md), [source map](sources.md), [model review](verify/README.md), [finite replay](verify/README.md). |

**Attribution:** Yilin Liu and GPT-6 Astra Pro.
