# Unrelated-value allocation with additive loss

| Field | Curated statement |
|---|---|
| **Guarantee** | Returns an original player-matroid basis and an integral allocation with utility at least `max(0,(1-epsilon) OPT-u_p)` for each selected player; the minimum utility is at least `max(0,(1-epsilon) OPT-u)`. |
| **Objective and output** | Maximize minimum player-dependent utility under recipient polymatroids; output the basis and resource counts. |
| **Time** | `Gamma(1/epsilon)^c poly(H)` against the integer optimum; the fractional-basis comparator variant uses `Gamma(2/epsilon)^c poly(H)`. |
| **Space** | Polynomial in the complete binary input, rational accuracy, and paid rank/SFM/LP work. |
| **Parameters** | `q` is the nonloop player count; `r` is the player-matroid rank; `c=q-r`; `epsilon` is rational accuracy; `u_p=max_j v_pj` and `u=max_p u_p`; `H` includes all binary values, ranks, and oracle descriptions. |
| **Model and representation** | Integral recipient polymatroids, nonnegative player-dependent values, and an actual original player-matroid basis; unused resources are allowed. |
| **Lower-bound scope** | No lower bound is claimed; the guarantee is additive and comparator-specific. |
| **Scope** | This is an additive guarantee. It does not imply a constant multiplicative approximation for unrelated values without a small-unit hypothesis. |
| **Review status** | Internally reviewed research; no formal verification or external peer review is claimed. |
| **Source** | [Corank additive allocation theorem](../../sources/checkpoint-o/unrelated_values_corank_additive_allocation.md). |

**Attribution.** Yilin Liu · GPT-6 Astra Pro
