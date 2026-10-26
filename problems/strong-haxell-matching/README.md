# Certifying matching under a strong Haxell condition

| Field | Result |
|---|---|
| **Guarantee** | Returns a left-perfect hypergraph matching, or a nonempty $S\subseteq A$ and a right-vertex hitting set $C$ with $\lvert C\rvert<\Delta r^2\lvert S\rvert$. Under $\tau(E_S)\ge\Delta r^2\lvert S\rvert$ for every $S$, the matching outcome is guaranteed. |
| **Objective and output** | Find a matching covering every left vertex, or return the stated directly checkable hitting-set obstruction. |
| **Time** | $O(\lvert A\rvert+\lvert B\rvert)+p\exp\bigl(O(U\log(2+s)/s)\bigr)$, where $p=\sum_e\lvert e\rvert$, $U=\log(p+4)$, and $s=\log\Delta$. |
| **Space** | $O(\lvert A\rvert+\lvert B\rvert+p(1+U/s))$ words with explicit layered certificates. Both outputs are checkable in $O(p+\lvert A\rvert+\lvert B\rvert)$ time. |
| **Parameters** | Each hyperedge contains one left vertex and between one and $r$ right vertices; integer $\Delta\ge4$. Prechecks handle $\Delta>p$. Vertex identities and counters use input-size words. |
| **Model and representation** | An explicitly listed bipartite hypergraph, with parallel edge identities allowed; the hitting number uses right vertices only. |
| **Lower-bound scope** | No lower bound is claimed. A hitting-set certificate refutes the strong Haxell promise but need not prove absence of all left-perfect matchings. |
| **Review status** | The [verification note](verify/README.md) records the proof scope, executable evidence and remaining conditions. No proof-assistant verification or external peer review is claimed. |
| **Source** | [Manuscript and proof](proof.md), with [dependencies and verification sources](sources.md). |

The same sharper asymptotic rate also follows from the documented weighted reanalysis of the public BHHS operation sequence. The proof does not claim an exclusive speed advantage over that reanalysis.

## Certified routing and expander packing

The [routing theorem](routing.md) uses a destructive-support distance interface with stretch $\Gamma$ and aggregate cost $(n+m+q)\exp(O(B))$. For short-path comparison length $h_0$, put $R=\lceil\Gamma h_0\rceil$. If the demand-path hypergraph satisfies $\tau(E_S)\ge\Psi\lvert S\rvert$ and $\Psi\ge\Delta R^2$, $\Delta\ge4$, the algorithm returns all demanded edge-disjoint simple paths in

$$
(n+m+q)\exp\left(O\left(B+\frac{U\log(2+s)}s\right)\right),\qquad s=\log\Delta.
$$

For an expander of conductance $\phi$ and minimum degree $\delta$, the [packing corollary](expander-packing.md) constructs $K$ edge-disjoint connected spanning subgraphs when

$$
\phi^3\delta\ge C K\Delta\Gamma^2\log^2N.
$$

Each has conductance $\Omega(\phi/(\Gamma\log N))$, and the total construction time is $(n+m)\exp(O(B+U\log(2+s)/s))$. All copies share one routing instance, so there is no hidden leading factor $K$. The corollary credits the existing auxiliary-expander reduction and states the quantitative interface substitution separately.

**Attribution.** Yilin Liu · GPT-6 Astra Pro
