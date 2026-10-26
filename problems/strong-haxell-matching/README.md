# Certifying matching under a strong Haxell condition

**Guarantee**

Returns a left-perfect hypergraph matching, or a nonempty <code class="math">S\subseteq A</code> and a right-vertex hitting set <code class="math">C</code> with <code class="math">\lvert C\rvert&lt;\Delta r^2\lvert S\rvert</code>. Under <code class="math">\tau(E_S)\ge\Delta r^2\lvert S\rvert</code> for every <code class="math">S</code>, the matching outcome is guaranteed.

**Objective and output**

Find a matching covering every left vertex, or return the stated directly checkable hitting-set obstruction.

**Randomness**

Deterministic certifying hypergraph matching. The routing and expander-packing transfers additionally require the supplied deterministic destructive-support distance interface.

**Time**

<code class="math">O(\lvert A\rvert+\lvert B\rvert)+p\exp\bigl(O(U\log(2+s)/s)\bigr)</code>, where <code class="math">p=\sum_e\lvert e\rvert</code>, <code class="math">U=\log(p+4)</code>, and <code class="math">s=\log\Delta</code>.

**Space**

<code class="math">O(\lvert A\rvert+\lvert B\rvert+p(1+U/s))</code> words with explicit layered certificates. Both outputs are checkable in <code class="math">O(p+\lvert A\rvert+\lvert B\rvert)</code> time.

**Parameters**

Each hyperedge contains one left vertex and between one and <code class="math">r</code> right vertices; integer <code class="math">\Delta\ge4</code>. Prechecks handle <code class="math">\Delta&gt;p</code>. Vertex identities and counters use input-size words.

**Model and representation**

An explicitly listed bipartite hypergraph, with parallel edge identities allowed; the hitting number uses right vertices only.

**Lower-bound scope**

No lower bound is claimed. A hitting-set certificate refutes the strong Haxell promise but need not prove absence of all left-perfect matchings.

**Review status**

The [verification note](verify/README.md) records the proof scope, executable evidence and remaining conditions. No proof-assistant verification or external peer review is claimed.

**Source**

[Manuscript and proof](proof.md), with [dependencies and verification sources](sources.md).

The same sharper asymptotic rate also follows from the documented weighted reanalysis of the public BHHS operation sequence. The proof does not claim an exclusive speed advantage over that reanalysis.

## Certified routing and expander packing

The [routing theorem](routing.md) uses a destructive-support distance interface with stretch <code class="math">\Gamma</code> and aggregate cost <code class="math">(n+m+q)\exp(O(B))</code>. For short-path comparison length <code class="math">h_0</code>, put <code class="math">R=\lceil\Gamma h_0\rceil</code>. If the demand-path hypergraph satisfies <code class="math">\tau(E_S)\ge\Psi\lvert S\rvert</code> and <code class="math">\Psi\ge\Delta R^2</code>, <code class="math">\Delta\ge4</code>, the algorithm returns all demanded edge-disjoint simple paths in

<!-- math-display: 2f1f766aa4ba196913a1f619
(n+m+q)\exp\left(O\left(B+\frac{U\log(2+s)}s\right)\right),\qquad s=\log\Delta.
-->
![Formula](../../assets/math/2f1f766aa4ba196913a1f619.svg)

For an expander of conductance <code class="math">\phi</code> and minimum degree <code class="math">\delta</code>, the [packing corollary](expander-packing.md) constructs <code class="math">K</code> edge-disjoint connected spanning subgraphs when

<!-- math-display: ec30d904a722d58ec88361db
\phi^3\delta\ge C K\Delta\Gamma^2\log^2N.
-->
![Formula](../../assets/math/ec30d904a722d58ec88361db.svg)

Each has conductance <code class="math">\Omega(\phi/(\Gamma\log N))</code>, and the total construction time is <code class="math">(n+m)\exp(O(B+U\log(2+s)/s))</code>. All copies share one routing instance, so there is no hidden leading factor <code class="math">K</code>. The corollary credits the existing auxiliary-expander reduction and states the quantitative interface substitution separately.

**Attribution.** Yilin Liu · GPT-6 Astra Pro
