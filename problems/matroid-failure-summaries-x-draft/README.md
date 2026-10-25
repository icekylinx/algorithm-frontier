# Matroid failure summaries — checkpoint X draft

**Status: Draft checkpoint X.** The two rows below have different representation and objective scopes and must not be merged into one theorem.

| Field | Candidate statement |
|---|---|
| **Guarantee** | Represented matroids: retain at most `min(N, r * binom(h + d, d))` items while preserving every surviving cost prefix. Arbitrary matroids: retain at most `r * binom(h + d, d)` items for rank-only summaries, with a deterministic FPT construction. |
| **Objective and output** | For an explicit linear representation, preserve spans and canonical minimum-cost bases after every allowed label failure, including rank drops. For an independence-oracle matroid, preserve only surviving rank and feasibility; the source does not claim arbitrary fixed-cost or cost-prefix preservation. |
| **Time** | Represented case: deterministic polynomial field operations with lifted dimension `D = r * binom(h + d, d)` and an input-size gate. Arbitrary-oracle case: `f(r,h,d) * |E|^O(1)` oracle time, with a direct `|E|^O(h)` alternative. |
| **Space** | Represented case retains `O(D)` original items; the source lifted linear-algebra workspace is separate. The arbitrary-oracle statement is a ground-size bound, not a bit-kernel claim. |
| **Parameters** | `N = |E|`; `r` is matroid rank; `h` is failed-label budget; `d` is labels per item; `L` is the number of distinct input labels. Costs and labels are fixed during preprocessing. |
| **Model and representation** | First row: rational or explicitly represented finite-field columns. Second row: arbitrary matroid independence oracle. The polynomial lift is not asserted for an oracle-only matroid. |
| **Lower-bound scope** | The represented bound is claimed sharp via zero-cost partition and graphic examples. The arbitrary-matroid draft includes a rank-only set-pair bound and a submodular extension; no broad complexity lower bound is promoted. |
| **Review status** | Draft checkpoint X. Proof, algorithm, and source review are pending; formal verification is not claimed. |
| **Source** | [Represented-matroid draft](../../sources/checkpoint-x/04_sharp_represented_matroid_failure_summaries.md) and [arbitrary-matroid/submodular draft](../../sources/checkpoint-x/06_arbitrary_matroid_and_submodular_failure_summaries.md). |

**Attribution:** Yilin Liu and GPT-6 Astra Pro.
