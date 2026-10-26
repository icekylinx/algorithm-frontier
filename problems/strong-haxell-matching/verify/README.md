# Verification and scope

The evidence for this result consists of its [mathematical proof](../proof.md) and the following companion manuscripts:

- [Edge-disjoint spanning expander packing: a direct routing corollary](../expander-packing.md)
- [Certified layers without superposition for disjoint-path routing](../routing.md)

## Mathematical evidence

- Current layers retain failed-extension and maximality certificates. Weighted signatures count attempted operations, epochs and stored layer data.
- The output is an explicit left-perfect matching or a right-vertex hitting set refuting the quantified strong promise.
- Routing states its destructive-distance backend and stretch conditions; expander packing retains its density hypothesis and charges one shared routing instance.
- The same sharper rate is derived for the public BHHS operation sequence by weighted reanalysis.

## Executable evidence

No result-specific executable check is supplied. The argument above is a mathematical proof, not an executable certificate or a complete solver.

## Model and verification boundaries

The hypergraph is explicitly listed and hitting sets use right vertices. A failed-promise certificate need not exclude every left-perfect matching. Routing and packing retain their named backend and density hypotheses. No exclusive speed advantage over the public reanalysis, implementation, or executable validator is claimed.

The [source map](../sources.md) identifies the actual proof dependencies. Repository checks validate the registry, links, notation and generated catalogue; those checks do not establish mathematical correctness. Proof-assistant verification and external peer review are not claimed.

**Attribution:** Yilin Liu and GPT-6 Astra Pro.
