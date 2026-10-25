# Two-size makespan scheduling

| Field | Curated statement |
|---|---|
| **Guarantee** | The corank branch gives an exact factor three-halves schedule; the separate large-unit branch gives factor five-thirds. These are distinct parameter regimes. |
| **Objective and output** | Minimize makespan for two positive job sizes and output integral bases for both aggregate job polymatroids, decomposed back to original assignments. |
| **Time** | In the corank branch, exponential in the number of surplus eligible large-job positions, times polynomial work. The large-unit construction has its own exponential parameter and is not silently merged. |
| **Space** | Polynomial in the complete binary input and the selected branch state; binary job counts are not expanded. |
| **Parameters** | `q` is the machine count; `h` and `s` are aggregate large- and small-job ranks; `r_b` is the Boolean-cap rank; `c` counts surplus eligible large-job positions; `u` and `a` are the two job sizes. |
| **Model and representation** | Arbitrary integral job polymatroids with two positive sizes, binary-encoded ranks, and the standard integral decomposition primitive. The Boolean-rank failure case is handled separately. |
| **Lower-bound scope** | The corank branch retains its matching strict-below-three-halves obstruction in the full value-oracle model; no broader lower bound is claimed. |
| **Review status** | Internally reviewed research; no formal verification or external peer review is claimed. See the [backlog review](../../reviews/backlog/legacy-result-cards.md) and [review registry](../../reviews/README.md). |
| **Source** | [Two-size corank source](../../sources/checkpoint-o/two_size_makespan_corank_three_halves_transfer.md) and the verification paths in `sources.md`. |

**Attribution.** Yilin Liu · GPT-6 Astra Pro
