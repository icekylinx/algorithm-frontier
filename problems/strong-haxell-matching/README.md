# Strong Haxell hypergraph matching

| Field | Curated statement |
|---|---|
| **Guarantee** | Returns a matching covering every left vertex, or a directly checkable hitting-set obstruction under the strong Haxell condition. |
| **Objective and output** | Find a left-perfect hypergraph matching; on failure output the explicit set `S` and hitting set `C`. |
| **Time** | `O(|A|+|B|) + p * exp(O(U log(2+s)/s))`, where `p=sum_e |e|`, `U=log(p+4)`, and `s=log Delta`. |
| **Space** | Linear in the explicit edge list plus word-sized counters and matching state. Both outputs are checkable in `O(p+|A|+|B|)` time. |
| **Parameters** | `H=(A,B,E)` is bipartite; each hyperedge contains one left vertex and between one and `r` right vertices; `Delta >= 4`; `p` is total incidence volume; `U` and `s` are as above. |
| **Model and representation** | Explicit hypergraph with parallel hyperedge identities allowed; the strong Haxell promise is the incidence condition stated in the lower-bound-scope row. |
| **Lower-bound scope** | No lower bound is claimed; the result is a certifying upper-bound algorithm under the displayed promise. |
| **Scope** | Under `tau(E_S) >= Delta r^2 |S|` for every `S`, the algorithm necessarily returns a left-perfect matching; otherwise a certificate need not prove impossibility of all matchings. |
| **Review status** | Internally reviewed research; no formal verification or external peer review is claimed. See the [matching-certificate review](../../reviews/backlog/matching-certificate-records.md). |
| **Source** | [Explicit strong-Haxell theorem](../../sources/checkpoint-o/explicit_hypergraph_matching_branching_improvement.md). |

**Attribution.** Yilin Liu · GPT-6 Astra Pro
