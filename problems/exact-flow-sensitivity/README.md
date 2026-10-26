# Exact flow, matching, and price sensitivity

Original-subinstance certificates and reporting structures for independent single failures or single price changes.

[Proof](proof.md) · [Sources](sources.md)

| Field | Statement |
|---|---|
| **Guarantee** | Exact surviving optimum or cardinality for each model below; each row has its own failure/change semantics and parameters. |
| **Objective and output** | Minimum-cost unit flows and path packings; exact cardinality matchings; common independent sets; and exact prescribed-rank price-change optima. |
| **Time** | Flow and vertex-disjoint paths: deterministic $\widetilde O(mn)$ arithmetic preprocessing. General matching and oracle matroids: deterministic polynomial preprocessing. Price sensitivity beyond a baseline optimum uses $O(Nr)$ independence tests and $O(Nr^2+r^3)$ arithmetic work. Query bounds are listed separately. |
| **Space** | Support and reporting records are in the table. Rational values occupy their actual bit length; construction workspace and external oracle storage are separate. |
| **Parameters** | $n,m$ are graph sizes; $\lambda$ is a feasible flow value; $s_x$ is a fixed optimum flow support; $\mu$ is graph matching number; $N,r$ are matroid ground size and prescribed rank. |
| **Model and representation** | Simple directed unit-capacity graphs with nonnegative rational costs for the uniform flow exponent; loopless undirected general graphs for cardinality matching; independence-oracle matroids for intersection. All queries are independent relative to the preprocessed input. |
| **Lower-bound scope** | General-matching certificates preserve cardinality, not every increased replacement cost. Integrality alone does not imply a linear certificate: the manuscript gives a quadratic retained-vertex obstruction for maximum independent set even in perfect graphs. |
| **Review status** | The [verification note](verify/README.md) records the proof scope, executable evidence and remaining conditions. No proof-assistant verification or external peer review is claimed. |
| **Source** | [Complete proof](proof.md) and [canonical manuscript map](sources.md). |

## Results

| Problem | Retained support / records | Query time or report |
|---|---|---|
| Fixed optimal unit flow of support $s_x$, general balances/signed costs | $O(s_x+n\sqrt{s_x})$ | $O(n)$ difference; $O(s_x+n)$ full support |
| Min-cost $\lambda$-flow, simple nonnegative-cost digraph | $O(n^{3/2}\lambda^{1/4})$ | $O(n)$ difference; $O(n\sqrt{\lambda})$ full support |
| Cost-only $\lambda$-flow sensitivity | $O(n\sqrt{\lambda})$ | $O(\log(n+1))$ |
| Min-cost maximum flow | $O(n^{3/2}\lambda^{1/4})\le O(n^{7/4})$ | Two consecutive flow-value structures |
| Min-cost maximum internally vertex-disjoint $s$–$t$ paths | $O(n^{3/2})$ | $O(n)$ full output; one arc or one internal vertex failure |
| General matching, one edge failure | At most $4\mu+2$ edges | $O(\mu)$ via one blossom-aware augmentation |
| General matching, one edge or one vertex failure | At most $6\mu+2$ edges | $O(\mu)$; alternative single failures |
| Two arbitrary matroids, cardinality only | At most $2r+k\le3r$ elements | Optimize on retained ground using original oracles; $k$ avoidable baseline elements |
| One-element price change, two matroids | $O(N+r\sqrt{\min\{N,r^2\}})$ | $O(r)$ exact output, no query oracle calls |
| Arbitrary new arborescence arc, prescribed spanning size | $O(n^2)$ records | $O(\log^2 n)$ gap evaluation; $O(n+\log^2 n)$ full output |

The weighted two-matroid and arborescence single-deletion theorems have their own [preserver card](../exact-failure-preservers/). Supplied-catalog insertion in the price structure keeps rank fixed; it does not handle an insertion that increases maximum rank.

**Attribution:** Yilin Liu and GPT-6 Astra Pro.
