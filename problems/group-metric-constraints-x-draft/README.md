# Finite-group, affine, and metric sparsification — checkpoint X draft

**Status: Draft checkpoint X.** Family-level review handle; not promoted.

| Field | Candidate statement |
|---|---|
| **Guarantee** | Drafts cover arbitrary-group Cayley spectral sparsifiers, whole subgroup/coset constraints, transitive and few-orbit Hilbert metric sums, affine modular blocks, and rational quotient-rank closures. |
| **Objective and output** | Preserve subgroup-complement, affine-coset, metric, modular, or quotient predicates with one coefficient per original item. |
| **Time** | Displayed supports include `O(min{m, epsilon^(-2) log^3(2|G|)})` for arbitrary weighted Cayley generators, `O(log(2|G|)/epsilon^2)` for whole subgroup constraints, and `O(r log(2r/epsilon)/epsilon^2)` compact modular branches. Compact access is not polynomial in `log|G|` without a succinct group oracle. |
| **Space** | Support, group-operation tables, quotient-rank keys, and partial-coloring query tables are separate. The exact-separation payload rules out one compact route, not every efficient construction. |
| **Parameters** | `G` is finite; `m` is item count; `epsilon` is error; `r` is subgroup/modular rank; orbit counts and sizes appear in few-orbit metrics; modulus and bit length are explicit. |
| **Model and representation** | Groups may be nonabelian and cosets need not be normal. Metric rows require itemwise action or the stated few-orbit completion. Modular rows use `Z_q` without factoring assumptions. |
| **Lower-bound scope** | The coNP result and non-Fano calculation are barriers for specified models, not general sparsification lower bounds. |
| **Review status** | Proof, algorithm, and source review are pending; formal verification is not claimed. |
| **Source** | Payloads `20`, `30`, `31`, `32`, `33`, `35`, `36`, `37`, and `38` in the checkpoint-X source tree. |

**Attribution:** Yilin Liu and GPT-6 Astra Pro.
