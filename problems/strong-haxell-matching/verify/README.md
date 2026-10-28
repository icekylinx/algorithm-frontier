# Verification and scope

The evidence for this result consists of its [mathematical proof](../proof.md) and the following companion manuscripts:

- [Edge-disjoint spanning expander packing: a direct routing corollary](../expander-packing.md)
- [Certified layers without superposition for disjoint-path routing](../routing.md)

## Mathematical evidence

- Current layers retain failed-extension and maximality certificates. Weighted signatures count attempted operations, epochs and stored layer data.
- The output is an explicit left-perfect matching or a right-vertex hitting set refuting the quantified strong promise.
- Routing states a generic destructive-distance interface and instantiates it with the [constructed support extractor](../../../manuscripts/graph-backends/destructive-apsp-path-support-extractor.md) and [APSP oracle](../../apsp-frontier/proof.md). Expander packing retains its density hypothesis and charges one shared routing instance.
- The same sharper rate is derived for the public explicit BHHS operation sequence by weighted reanalysis.
- The [retained rank-sensitive proof](../../../manuscripts/matching-and-routing/rank-sensitive-layer-count.md), Sections 1–4, bounds child births by the ratio of their allowed sizes and includes the possible last living child. The root contributes a separate logarithmic factor. The proof works on every finite execution prefix and does not assume termination.
- Its explicit-input cost includes every listed hyperedge incidence, matching-blocker scan, actual certificate resource and output. Unused declared vertices are read once. Constant-rank and linear greedy endpoints retain their exact parameter conditions.

## Executable evidence

No result-specific executable check is supplied. The arguments are complete mathematical proofs with directly checkable output specifications; a full executable hypergraph solver and result-specific automated validator are not supplied.

## Model and verification boundaries

The hypergraph is explicitly listed and hitting sets use right vertices. A failed-promise certificate need not exclude every left-perfect matching. Routing and packing use the named local constructions and public algorithms, with their stated numerical, hitting and density conditions. No exclusive speed advantage over the public reanalysis, full executable implementation, or automated validator is claimed. The companion’s active-scan example is a lower bound for that particular scanning rule only; its own family admits the separate linear greedy preprocessing, so it is not a task lower bound.

The [source map](../sources.md) identifies the actual proof dependencies. Repository checks validate the registry, links, notation and generated catalogue; those checks do not establish mathematical correctness. Proof-assistant verification and external peer review are not claimed.

**Attribution:** icekylinx and GPT-6 Astra Pro.
