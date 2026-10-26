# Degree-constrained subgraphs

**Guarantee**

Finds an exact feasible degree-constrained edge subset, or correctly reports that none exists. A standard-library reference solver and a separate decision/certificate verifier are available.

**Objective and output**

Supports f-factors, interval degree bounds, exact or ranged cardinality constraints, and cardinality optimization; outputs original edge identifiers and treats each parallel edge record as a separate selectable item.

**Randomness**

Deterministic reductions and exact algorithms. The faster bound invokes the proved deterministic general-matching construction and its named published dependencies; the shipped reference solver has its own polynomial cost.

**Time**

The executable reference uses `O(n+H^3)` time for feasibility, including exact/ranged cardinality, and `O(n+H^3 log(m+2))` for optimization, where `H=1+m log(m+2)`. Certificates and native output checks are included.

The reduction builds an <code class="math">O(m\log(m+2))</code>-size simple subcubic graph. Substituting the proved deterministic matching construction gives <code class="math">O(n+m)+(m+1)\exp\!\left(O((\log(m+2))^{4/5}(\log\log(m+4))^{1/5})\right)</code> time, with its named local and published proof dependencies.

**Space**

The reference solver uses `O(n+H)` storage, including the explicit reduction and retained certificate, plus the actual label-encoding space. Oversized upper bounds are clipped before any dummy edges are allocated.

**Parameters**

<code class="math">n</code> is the vertex count; <code class="math">m</code> is the explicit edge-record count; <code class="math">g(v)</code> and <code class="math">f(v)</code> are lower and upper degree bounds.

**Model and representation**

Loopless undirected multigraph with capacity one per edge record. The card does not extend the result to arbitrary weighted or binary-multiplicity variants.

**Lower-bound scope**

No new lower bound is claimed; this is a deterministic transfer from the matching backend.

**Review status**

**Ready for review.** The complete sparse reductions for prescribed degrees, degree intervals and exact/ranged cardinality, with extension, native decoding and the fast matching substitution. The shipped native-record solver handles feasibility, minimum and maximum cardinality. Its independent verifier checks YES witnesses and local or matching-based NO/optimality certificates without a matching search.

**Conditions and remaining work.** The reference implementation has its own polynomial bounds and shares the proved deterministic reduction builder with the verifier. Input is a loopless multigraph with capacity one per explicit record. Binary multiplicities and arbitrary edge-weight optimization are outside this implementation.

The [verification note](verify/README.md) identifies executable coverage. This status does not claim external peer review or proof-assistant verification.

**Source**

[Reference solver and usage](reference/README.md), [certificate proof](reference/correctness.md), [complete reduction theorem](proof.md), [dependencies and primary sources](sources.md).

**Attribution.** Yilin Liu · GPT-6 Astra Pro
