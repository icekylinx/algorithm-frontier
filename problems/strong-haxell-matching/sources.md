# Proofs and dependencies

The canonical manuscripts below contain the mathematical arguments. Computational evidence and its limits are recorded separately in [Verification](verify/README.md).

## Canonical manuscripts

- [A faster certifying algorithm for explicit hypergraph matching under strong Haxell conditions](proof.md)
- [Edge-disjoint spanning expander packing: a direct routing corollary](expander-packing.md)
- [Certified layers without superposition for disjoint-path routing](routing.md)

## Strongest retained quantitative bound

The [rank-sensitive layer count](../../manuscripts/matching-and-routing/rank-sensitive-layer-count.md), Sections 1–4, strengthens the rank-free weighted bound for the same explicit certifying algorithm. It keeps the logarithmic root factor and uses the full listed hyperedge incidence volume. Its constant-rank consequence is <code class="math">p\log(p+4)\exp O_r(1/\epsilon)</code> when <code class="math">\Delta\ge p^\epsilon</code>, plus unused vertex-list reading. Section 5 gives the separate linear greedy and classical rank-one endpoints. These existing refinements were retained in the repository and are now displayed in the main theorem and problem card; this restoration is not a new discovery claim.

The same rate applies to the reanalyzed public **explicit** BHHS operation sequence, whose adopted resets form at most 26 epochs per layer. It does not assume the separate, still-conditional approximate-extension observation. An implicit routing application must retain the destructive extractor's full per-build work and its effective path rank; explicit incidence <code class="math">p</code> cannot be replaced silently by a graph edge count.

## Mathematical dependencies

The routing theorem first states a generic destructive-distance
interface. Its concrete instantiation is supplied by the path-support
extractor below, Sections 2–4, using APSP Corollary 2.2, local shortest-path
trees and the metric forest lift. It charges actual support occurrences
and temporary updates without an additional multiplicative stretch
factor. Thus the routing and packing parameter substitutions use a
constructed interface; their hitting-number, conductance and density
conditions remain genuine input promises.

- [Destructive path-support extraction from the APSP hierarchy](../../manuscripts/graph-backends/destructive-apsp-path-support-extractor.md)
- [The same sharper rate for the existing BHHS explicit-hypergraph algorithm](../../manuscripts/matching-and-routing/public-hypergraph-algorithm-weighted-reanalysis.md)
- [Rank-sensitive counting for certified Haxell layers](../../manuscripts/matching-and-routing/rank-sensitive-layer-count.md)
- [Fully dynamic all-pairs distances: a time–stretch theorem](../apsp-frontier/proof.md)

## Primary references

- [*Finding Perfect Matchings in Bipartite Hypergraphs*](https://arxiv.org/html/1509.07007v2)
- [*Disjoint Paths in Expanders in Deterministic Almost-Linear Time via Hypergraph Perfect Matching*](https://arxiv.org/html/2511.02214v1)
- [*A Deterministic Algorithm for Balanced Cut with Applications to Dynamic Connectivity, Flows, and Beyond*](https://arxiv.org/html/1910.08025v2)

## Executable evidence

No result-specific executable check is registered. The mathematical proof and the repository document checks have separate roles.

The [verification note](verify/README.md) states which obligations remain symbolic. Import origins and retained notices are recorded in [provenance](../../provenance/README.md).

**Attribution:** icekylinx and GPT-6 Astra Pro.
