# Checkpoint X draft intake and review backlog

**Status: draft intake only.** No checkpoint X claim has been promoted to a stable result card. The source files are preserved under [`sources/checkpoint-x/`](../../sources/checkpoint-x/), with the archive inventory recorded in [`MANIFEST.json`](../../sources/checkpoint-x/MANIFEST.json).

## Provenance

- Archive: `checkpoint_X_incremental_drafts_2026-10-25.zip`
- Archive size: 76,990 bytes
- Stated repository reference: `icekylinx/algorithm-frontier` at `37b31138bf102a83d9efb2cbe44437eec45ae3c2`
- Stated attribution: Yilin Liu and GPT-6 Astra Pro
- Source maturity: rough English research drafts for external review; no formal verification, exhaustive priority clearance, or external peer review
- Parent archive: not declared in the upload; do not infer a parent ZIP or copy inherited manuscripts into this increment

## Candidate families and review gates

| Family | Payload | Candidate headline (still draft) | Proof review | Algorithm review | Source review |
|---|---|---|---|---|---|
| Exact sensitivity preservation | `01_exact_single_failure_arborescences_and_matroid_intersection.md` | Two arbitrary matroids: `O(k^(3/2))` retained original elements and `O(k)` single-failure reporting; directed minimum-cost arborescence specialization claims `O(n^(3/2))` arcs, `~O(mn)` arithmetic preprocessing, and `O(n)` output. | Audit tangent-direction and cycle/replacement lemmas, repeated labels, negative exchange lengths, distance-preserver reduction, and rank-drop union. | Recheck oracle calls, exact-rational bit cost, path-reporting records, and arborescence segment-tree construction. | Verify the Dey--Kavitha comparator and ensure the open-problem comparison is scoped to the checked source. |
| Exact sensitivity preservation | `09_valuated_matroid_intersection.md` | Fixed-rank two-valuated-matroid intersection: `O(k^(3/2))` records and `O(k)` query output with value oracles. | Check joint convex decomposition, valued exchange matching, minimum-hop cycle update, and cost signs. | Confirm value-oracle preprocessing and no hidden rank-drop objective. | Check representative-family antecedents and separate the inherited ordinary result from the valued increment. |
| Subset Sum | `02_deterministic_subset_sum_increment.md` | Conditional deterministic signed-binary exponent `149809813343531/301825962128739` (approximately `0.4963450204`), with indexed witness recovery. | Recompute all contact inequalities and the complete piecewise profile. | Verify circuit menu, compiler transfer, startup constant, bit-model charges, and witness indexing. | Pin the imported fast-time proof and distinguish the result from the independent low-space card and randomized `0.49` comparator. |
| Boundary and persistence certificates | `03_correlated_fault_boundary_and_persistence_sparsifiers.md` | Candidate `r * binom(h+a+b, a+b)` top-simplex restriction preserving all allowed correlated-failure persistence queries over a specified field; one-color vertex envelope is stated separately. | Check linear activation, incidence lift, rank/nullspace count, lower skeleton, and simultaneous filtration statement. | Verify field construction, threshold order, retained-face representation, and whether the cost and filtration constructions are separate. | Check Kalai/exterior-algebra antecedents and sharpness claims in the stated original-cell model. |
| Boundary and graph certificates | `05_colored_graph_and_vertex_failure_certificates.md` | Candidate exact weighted-prefix connectivity/MSF certificate for vertex color failures with `sum_C(n_C*k_C - binom(k_C+1, 2))` edges, plus mixed/list variants. | Check activation matrix, rank saving, color/list quantifiers, and lower-bound constructions. | Verify polynomial construction, parallel-edge/loop handling, signed weights, and query interface. | Audit the Sorkin--Steger--Zenklusen and spanner baselines; keep inherited individual-failure results distinct. |
| Matroid failure summaries | `04_sharp_represented_matroid_failure_summaries.md` | Explicitly represented matroid: `r * binom(h+d, d)` retained items, preserving every surviving cost prefix, deterministic polynomial preprocessing. | Check polynomial feature lift, field gate, basis projection, and sharpness examples. | Verify dimension gate, bit complexity, fixed costs/labels, and no oracle-only extension. | Check representative-family antecedents and the graph connectivity comparison. |
| Matroid failure summaries | `06_arbitrary_matroid_and_submodular_failure_summaries.md` | Arbitrary matroid rank-only summary of size `r * binom(h+d, d)`, with deterministic FPT construction; monotone-submodular extension is separate. | Check circuit-blocking set-pair inequality, tightness, separating family, and final search. | Verify the FPT/XP parameter boundary and that arbitrary costs/prefixes are not claimed. | Audit the Bentert--Fomin--Golovach--Morelle and Dey--Kavitha comparisons and exact parameter conventions. |
| Packing and matching summaries | `07_represented_resource_packing_transfer.md` | Represented-resource packing bound `r * binom(pK+h_v, p) * product_j binom(h_j+d_j, d_j)`; ordinary matching specialization is a represented/unconstrained comparison. | Check packing exterior product, unknown-extension quantifier, and protected-item replacement. | Verify original-ID treatment, dimension gate, field model, and cardinality/objective scope. | Check representative-family antecedents and keep arbitrary-oracle resource results separate. |
| Boolean linear optimisation | `08_boolean_linear_optimization_compiler.md` | Support-sensitive interval/slack compiler with `T_B <= poly(L) * (product_i p_i) * 2^(alpha*n+Q-(1-alpha)*B)`, conditional on a supplied Subset Sum backend. | Check interval catalogue exactness and slack-bit encoding. | Verify parameter `Q`, equality handling, optimization/witness recovery, and backend space contract. | Check Nederlof--van Leeuwen--van der Zwaan and Bansal--Garg--Nederlof--Vyas credits; do not advertise universal dominance. |

## Promotion rule

A family can receive a public result card only after the three review roles have written reports covering the gates above. Until then, any card must say `Draft checkpoint X`, link the exact source payload, and state `formal verification: not claimed`. A finite script can support a local identity or example but cannot promote a theorem.

The source-only import deliberately does not modify the prior checkpoint bodies, overwrite existing result cards, or combine claims across incompatible models. In particular, the arborescence, boundary-matrix, represented-matroid, arbitrary-oracle, and Subset Sum rows use different input representations and parameter conventions; they must remain separate during curation.

## Suggested next passes

1. Proof pass: reproduce each headline lemma in a short reviewer note and mark any missing quantifier or rank assumption.
2. Algorithm pass: charge preprocessing, query, output, and exact-arithmetic costs separately; record all dimension gates and fixed-order assumptions.
3. Source pass: re-open every primary comparator and replace bounded-search language with exact citations only where the source supports it.
4. Verification pass: add small finite checks only for identities with a clear exhaustive domain; record them as evidence, never as formal verification.
