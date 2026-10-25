# Exact label cuts, quotient resparsification, and whole blocks — checkpoint X draft

**Status: Draft checkpoint X.** Family-level review handle; not promoted.

| Field | Candidate statement |
|---|---|
| **Guarantee** | Exact label annihilation is proposed for correlated-failure cuts, matroid quotients, hyperedges, hedges, whole linear blocks, and globally commuting stabilizer blocks, with an adaptive resparsification accounting note. |
| **Objective and output** | Preserve every allowed cut, quotient, partition-crossing, or whole-block query after label failures with one fixed coefficient per original item. |
| **Time** | The exact cut branch states `D=(n-components) binom(h+a+b,a+b)` and support `O(min{m, D log(2D/epsilon)/epsilon^2})`; whole-block rows add arity and item-label parameters. Adaptive quotient support is `O(r log(2r/epsilon)/epsilon^2)`. |
| **Space** | Lifted rank, original support, adaptive error state, query decoding, and integer-rank storage are distinct. No query-dependent reweighting is assumed. |
| **Parameters** | `n` is dimension; `h` is failure budget; `a,b` bound label degrees; `r` is lifted rank; `epsilon` is error; `t` is maximum arity; `d` is item-label budget. |
| **Model and representation** | Exact homogeneous polynomial label features, quotient/rank backends, colored cuts, hyperedges, hedges, represented blocks, and globally commuting stabilizer blocks as stated. |
| **Lower-bound scope** | Cut and whole-block lower constructions are conditional on their incidence and size regimes; they do not apply to arbitrary sparsifiers or positive operators. |
| **Review status** | Proof, algorithm, and source review are pending; formal verification is not claimed. |
| **Source** | Payloads `27`, `28`, and `29` in the checkpoint-X source tree. |

**Attribution:** Yilin Liu and GPT-6 Astra Pro.
