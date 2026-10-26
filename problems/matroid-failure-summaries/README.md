# Sharp matroid and submodular failure summaries

Exact binomial-size restrictions under correlated label failures, with separate weighted represented and rank-only oracle models.

[Proof](proof.md) · [Sources](sources.md)

| Field | Statement |
|---|---|
| **Guarantee** | For $C=\binom{h+d}{d}$, represented matroids preserve every surviving fixed-cost prefix with at most $\min\{N,rC\}$ items. Arbitrary matroids preserve surviving rank with at most $rC$ items. |
| **Objective and output** | Original-element restrictions, canonical minimum-cost surviving bases in the represented case, and exact surviving ranks/values in the oracle cases. |
| **Time** | Represented: uniform deterministic polynomial preprocessing, with $O(ND^2)$ field operations for elimination at gated dimension $D=rC$, plus feature construction and rank compression. Oracle rank: $f(r,h,d)N^{O(1)}$; direct alternative $O\!\left(N^2\sum_{i\le h}\binom{L}{i}\right)$ independence queries. |
| **Space** | Output counts original IDs. The $O(D^2)$ elimination workspace and oracle representation are separate. No bit-kernel bound for arbitrary oracles is asserted. |
| **Parameters** | $N$ is element count; $r$ is rank; $h$ is failed-label budget; $d$ is actual maximum labels per item; $L$ is the explicit label universe; $R$ is the numerical submodular value range. |
| **Model and representation** | Rational or explicit finite-field columns for weighted-prefix preservation. Independence oracles for rank-only matroid preservation; value oracles for integer-valued monotone submodular functions. |
| **Lower-bound scope** | The $rC$ and $RC$ retained-size bounds are exact in the worst case via labeled parallel classes or coverage functions. Rank-only oracle preservation does not imply weighted-prefix preservation. |
| **Review status** | The [verification note](verify/README.md) records the proof scope, executable evidence and remaining conditions. No proof-assistant verification or external peer review is claimed. |
| **Source** | [Complete proof](proof.md) and [canonical manuscript map](sources.md). |

## Results

| Result | Exact bound | Construction / interpretation |
|---|---|---|
| Represented fixed-cost matroid summary | $\min\left\{N,r\binom{h+d}{d}\right\}$ items | Uniform deterministic polynomial preprocessing |
| Arbitrary-matroid rank summary | $r\binom{h+d}{d}$ items | Deterministic FPT in $r+h+d$; XP in $h$ by direct enumeration |
| Integral monotone-submodular failure-value summary | $R\binom{h+d}{d}$ items | Deterministic FPT in $R+h+d$; $R=f(E)-f(\varnothing)$ |
| Worst surviving final-marginal sum | $\sum_e\sigma_e\le\binom{h+d}{d}\,[f(E)-f(\varnothing)]$ | Real-valued monotone submodular $f$; sharp |
| Correlated-erasure conditional entropy | $\sum_e\max_F H(X_e\mid X_{E_F\setminus\{e\}})\le\binom{h+d}{d}H(X_E)$ | Finite joint Shannon entropy; sharp |
| Represented completion and mergeability | Same $r\binom{h+d}{d}$ size | Fixed original linear representation and common feature assignment; arbitrary later matroid extensions preserve the original restriction |

**Attribution:** Yilin Liu and GPT-6 Astra Pro.
