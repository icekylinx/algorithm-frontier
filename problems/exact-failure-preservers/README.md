# Exact single-failure preservers

Sparse original-element restrictions and output-sensitive reporting for exact weighted matroid intersection and rooted arborescences.

[Proof](proof.md) · [Sources](sources.md)

| Field | Statement |
|---|---|
| **Guarantee** | Preserve a minimum-cost prescribed-rank solution after every deletion of one original element, and the no-failure optimum; report infeasibility when that rank becomes unavailable. |
| **Objective and output** | An exact common basis, a rooted spanning arborescence, or an infeasibility answer. Reporting makes no independence or valuation calls. |
| **Time** | Deterministic polynomial preprocessing. Beyond a baseline common optimum: $O(Nk)$ independence/value tests and $O(Nk^2+k^3)$ arithmetic work. Arborescences: $\widetilde O(mn)$ arithmetic preprocessing. Query: $O(k)$, or $O(n)$ for arborescences. |
| **Space** | $O(k^{3/2})$ retained original elements and reporting records; $O(n^{3/2})$ for arborescences. Exact values are charged by their actual bit length. |
| **Parameters** | $N$ is original ground size; $k$ is prescribed common rank; $n,m$ are directed vertex and arc counts. All costs and valuations remain fixed between independent queries. |
| **Model and representation** | Ordinary matroids use independence oracles. Valuated matroids additionally require one supplied finite-valued basis per effective domain, or independence access obtaining it, as well as rational value evaluations. Graph costs are nonnegative rational numbers. |
| **Lower-bound scope** | Inherited directed-distance constructions give $\Omega(k^{4/3})$ for weighted two-matroid restrictions and $\Omega(n^{4/3})$ for arborescences. Two failures require quadratic original support; approximation lower bounds allow the stated exponential cost aspect ratio. |
| **Review status** | The [verification note](verify/README.md) records the proof scope, executable evidence and remaining conditions. No proof-assistant verification or external peer review is claimed. |
| **Source** | [Complete proof](proof.md) and [canonical manuscript map](sources.md). |

## Results

| Problem | Retained support / records | Query output | Additional scope |
|---|---|---|---|
| Minimum-cost common $k$-set, two arbitrary matroids | $O(k^{3/2})$ | $O(k)$ | Fixed linear costs; one element deletion |
| Two fixed-rank valuated matroids | $O(k^{3/2})$ | $O(k)$ | Effective-domain initialization is supplied; no smaller-rank valuation is inferred |
| Rooted minimum-cost spanning arborescence | $O(n^{3/2})$ | $O(n)$ | Directed graph, one arc deletion; $\widetilde O(mn)$ preprocessing |
| Minimum-cost maximum-cardinality common set | $O(r^{3/2})$ | $O(r)$ | Union of the $r$ and $r-1$ constructions; ordinary linear costs |
| Two-failure exact matching/arborescence obstruction | $\Omega(r^2)$ / $\Omega(n^2)$ | Lower bound | Retained original elements/arcs |
| Two-failure approximate arborescence obstruction | $\Omega(n^2)$ | Lower bound | Every fixed multiplicative factor; polynomial-bit costs with exponential aspect ratio |

**Attribution:** Yilin Liu and GPT-6 Astra Pro.
