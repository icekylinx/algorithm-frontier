# Exact sensitivity, flow, and matching — checkpoint X draft

**Status: Draft checkpoint X.** This family-level card is a review handle; it is not a promoted result.

| Field | Candidate statement |
|---|---|
| **Guarantee** | Source-specific one-failure summaries cover two-matroid and valuated-matroid intersection, minimum-cost arborescences, unit-capacity minimum-cost flow, internally vertex-disjoint paths, general-graph matching, and one-element price changes. Displayed supports include `O(k^(3/2))`, `O(n^(3/2))`, `O(n^(3/2) lambda^(1/4))`, `O(mu)`, and `O(N+r sqrt(min{N,r^2}))`; these are separate theorems. |
| **Objective and output** | Return an exact surviving optimum or a compact sensitivity report after one permitted deletion/change, with the output format stated separately in each payload. |
| **Time** | Deterministic polynomial preprocessing with independence/value/residual oracles. The drafts expose soft-`O(mn)` arithmetic for arborescence and flow, output-sensitive `O(k)` or `O(n)` reports, and `O(mu)` matching queries. Exact rational bit costs and value-oracle output length remain review parameters. |
| **Space** | Displayed support bounds are record counts. Construction workspace, oracle storage, reporting pointers, and exact-arithmetic workspace are separate. |
| **Parameters** | `k` is common rank; `n,m` are vertex/arc counts; `lambda` is flow value; `mu` is maximum matching size; `N,r` are price-sensitivity parameters. Costs and valuations have explicit encoding length. |
| **Model and representation** | Separate models: two independence-oracle matroids; fixed-rank valuated matroids; directed nonnegative-cost unit-capacity flow/arborescence; loopless general graphs; and matroid-intersection price changes. One failure/change is allowed. |
| **Lower-bound scope** | Inherited distance-preserver and matching obstructions are model-specific. Two-failure quadratic statements and arborescence lower bounds are not merged. |
| **Review status** | Proof, algorithm, and source review are pending; formal verification is not claimed. |
| **Source** | Payloads `01`, `09`, `10`, `12`, `13`, `14`, and `16` in the checkpoint-X source tree. |

**Attribution:** Yilin Liu and GPT-6 Astra Pro.
