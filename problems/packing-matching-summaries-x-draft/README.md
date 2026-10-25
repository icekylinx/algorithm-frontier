# Packing and matching failure summaries — checkpoint X draft

**Status: Draft checkpoint X.** This candidate requires an explicitly represented positive resource matroid whenever the resource factor `r` is present.

| Field | Candidate statement |
|---|---|
| **Guarantee** | For packing items of support size at most `p`, matching/packing cardinality at most `K`, vertex-failure budget `h_v`, and label systems `(h_j, d_j)`, the draft claims a deterministic restriction of size at most `r * binom(pK + h_v, p) * product_j binom(h_j + d_j, d_j)`. Without a represented resource matroid, omit `r`. |
| **Objective and output** | Preserve minimum positive cost, feasibility, and prescribed positive cardinality under allowed packing and label failures, with replacement items retaining original IDs. A later arbitrary-matroid extension/background remains fixed in the replacement statement. |
| **Time** | Uniform deterministic polynomial preprocessing in the explicit item, packing, label, and represented-resource input, with an input-size dimension gate. No faster unrestricted matching algorithm is claimed. |
| **Space** | The displayed quantity counts retained original items. Product-space and resource-representation workspace are separate. |
| **Parameters** | `p` is item-support size; `K` is positive cardinality; `h_v` is the failed packing-universe budget; `h_j` and `d_j` are label budgets; `r` is full represented resource rank. |
| **Model and representation** | Explicit items with pairwise-disjoint packing supports, fixed signed linear costs, and optional rational or finite-field represented resource columns. Ordinary matching is the no-resource specialization. |
| **Lower-bound scope** | The source compares with an arbitrary-oracle bound under a stronger represented-resource assumption. It does not claim a new matching lower bound or improvement for arbitrary independence-oracle resources. |
| **Review status** | Draft checkpoint X. Proof, algorithm, and source review are pending; formal verification is not claimed. |
| **Source** | [Represented resource-packing draft](../../sources/checkpoint-x/07_represented_resource_packing_transfer.md). |

**Attribution:** Yilin Liu and GPT-6 Astra Pro.
