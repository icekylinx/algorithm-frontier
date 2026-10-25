# Exact single-failure preservers — checkpoint X draft

**Status: Draft checkpoint X.** This source-linked candidate remains under proof, algorithm, and source review.

| Field | Candidate statement |
|---|---|
| **Guarantee** | For two arbitrary matroids with a common rank-`k` solution, the draft claims an exact single-element-failure restriction with `O(k^(3/2))` original elements and an `O(k)` output-sensitive query. A separate fixed-rank valuated-matroid draft states the analogous guarantee with value-oracle access. |
| **Objective and output** | Return a minimum-cost surviving common independent set of the prescribed rank after one original-element deletion, or report infeasibility. The arborescence specialization reports a minimum-cost rooted spanning arborescence after one arc failure. The valuated extension is fixed rank `k`; no rank-drop valuation is inferred. |
| **Time** | General two-matroid construction: deterministic polynomial time with independence oracles, with the draft's compressed exchange construction using `O(|E| k)` tests and conservative `O(k^3)` arithmetic post-processing. Directed arborescence specialization: `tilde-O(m n)` arithmetic operations as stated in the source. Query output time `O(k)`, or `O(n)` for an arborescence. Exact rational bit cost is additional. |
| **Space** | `O(k^(3/2))` records for the general preserver and valued variant; `O(n^(3/2))` original-arc records for the arborescence specialization, including reporting pointers and identifiers. |
| **Parameters** | `k` is the prescribed common-set rank; `|E|` is the original ground size; `m` and `n` are the arborescence arc and vertex counts. Costs are fixed rational numbers. |
| **Model and representation** | Two independence-oracle matroids for the ordinary result; two fixed-rank valuated matroids with value oracles for the valued result; directed rooted graphs with nonnegative rational arc costs for the arborescence specialization. One failure is allowed. |
| **Lower-bound scope** | The source includes an inherited pairwise-distance lower-bound equivalence and a two-failure quadratic obstruction for the general matching reduction. Those bounds are not automatically arborescence lower bounds. No new lower bound is promoted here. |
| **Review status** | Draft checkpoint X. Proof, algorithm, and source review are pending; formal verification is not claimed. See the [checkpoint X backlog](../../reviews/backlog/checkpoint-x-drafts.md). |
| **Source** | [Ordinary two-matroid/arborescence draft](../../sources/checkpoint-x/01_exact_single_failure_arborescences_and_matroid_intersection.md) and [valuated extension](../../sources/checkpoint-x/09_valuated_matroid_intersection.md). |

The arborescence comparison to Dey--Kavitha is a bounded source comparison in the draft and must be rechecked before any headline promotion.

**Attribution:** Yilin Liu and GPT-6 Astra Pro.
