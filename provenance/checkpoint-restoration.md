# Restored checkpoint results and proof dependencies

The early checkpoints contain complete constructions that were understated
by the later catalogue. This record connects those constructions to the
current proofs and distinguishes subsequent work from earlier results.
It accompanies the source manifests; it does not substitute a historical
status label for a mathematical argument.

## Original evidence

The recovery compared all **36 supplied ZIP archives**, comprising 5,382
extracted files. The 35 archives in the main archive manifest match their
recorded SHA-256 fingerprints; the X archive matches its separate import
manifest. The Markdown inventory has 605 distinct basenames and 736
distinct original byte contents. Repeated snapshots are evidence of
continuity, not additional independent proofs.

The [machine-readable recovery index](checkpoint-recovery.json) records
archive fingerprints, original file hashes, canonical destinations and
the disposition of earlier notes. It contains text and data only. Original
source hashes identify the supplied bytes; they do not assert byte equality
with the edited canonical manuscripts. The
[pre-consolidation tree](https://github.com/icekylinx/algorithm-frontier/tree/e4cd7e6050a9c80de6562ae1efc17f61ca3839be)
and the existing [canonical map](canonical-map.json) provide the earlier
repository paths.

## Completed constructions retained in the current catalogue

| Result | Earlier source evidence | Current realization and scope |
|---|---|---|
| Deterministic general-graph matching, four-fifths exponent | Revised 24 October matching checkpoint: quantitative composition, uniform source interfaces, raw lift, chronological repair, lifetime and finite-bit constructions | [Main proof, Section 11.6](../problems/general-matching/proof.md#116-deterministic-cycle-search-realization) realizes all five operation groups; Section 12 supplies the uniform parameter and first-failure argument. [Source map](../problems/general-matching/sources.md). |
| At most four times the matching number in retained vertices | `linear_vertex_kernel_refinement.md`, present in the 24 October direct checkpoint and retained in the fixed-epsilon and uniform checkpoints | [Cover-compression proof](../problems/general-matching/reference/cover-compression-proof.md). The preservation lemma is an earlier structural result. The later code, independent certificates and bipartite acceleration are subsequent contributions. |
| Static and fixed-threshold integral min-cost flow | Checkpoint A already contains the moving-box barrier proof and its two audits; the same source is carried through Q | [Flow proof](../problems/min-cost-flow/proof.md) and [source map](../problems/min-cost-flow/sources.md) instantiate the raw-cycle and lifetime interfaces. The incremental output contract is a fixed threshold. |
| Incremental SCC labels | Checkpoint B supplies the SCC construction and audit, retained through Q | [SCC proof](../problems/incremental-scc/proof.md) instantiates the exact base-register and retirement bridge. Topological ordering and within-component paths are not part of this interface. |
| Incremental SSSP and simple paths | A contains the frozen detector; B adds the complete outer and reporting refinements | [SSSP proof](../problems/incremental-sssp/proof.md) and [raw-cycle bridge](../manuscripts/graph-backends/raw-cycle-to-frozen-detector-bridge.md) provide the detector, exact retirement and path output. Integer zero-length handling remains explicit. |
| Fully dynamic APSP tradeoff | C and E contain the constructed curve and the same-stretch comparison; their audit records the closed interfaces | [APSP proof](../problems/apsp-frontier/proof.md) retains the parameter restrictions, amortized update guarantee and numerical query output. |
| Tracked-terminal and full-horizon spanners | F supplies the full-horizon five-sixths result; G supplies the tracked-terminal four-fifths result | [Spanner proof](../problems/dynamic-spanners/proof.md) keeps their different recourse guarantees and realizes the destructive-support and hierarchy interfaces. |
| Decremental strong forests and cut-equivalent trees | E contains the accepted no-reset Steiner-pool six-sevenths construction; B already supplies the fixed-k min-cut realization | [Forest and cut-tree proof](../problems/decremental-strong-forest/proof.md) uses the completed no-reset construction. A gap in an optional older ported-forest candidate does not apply to it. |
| Destructive path extraction, disjoint routing and expander packing | D supplies the extractor; E supplies the exact-size and route/conductance refinements | [Routing proof](../problems/strong-haxell-matching/routing.md) and [source map](../problems/strong-haxell-matching/sources.md) retain the real expansion, density and congestion promises. |
| Deterministic worst-case dynamic MSF baseline | F supplies the two-thirds public-theorem composition and formal pruning substitution | [MSF proof](../problems/dynamic-msf/proof.md) names the exact decomposition, pruning and recursive-reduction theorems. This is a derived public baseline. |
| Uniform fast and general low-space Subset Sum | The hash-matched original TeX and source status already contain the compiler, witness and storage proofs | [Fast proof](../problems/subset-sum-fast-deterministic/proof.md) and [low-space proof](../problems/subset-sum-low-space-deterministic/proof.md) retain the complete earlier arguments. The newer certified lookups and restricted-range algorithm have separately stated scopes. |

The Subset Sum comparison also checked every numbered source formula:
131 in the fast manuscript and 160 in the low-space manuscript, plus all
30 and 38 source section headings. Formula differences in that comparison
are notation normalization and whitespace. This source-preservation check
does not independently prove the formulas.

## What was corrected

The consolidation and a later implementation pass had treated the absence
of fast executable code as an unresolved mathematical premise. That was
incorrect for the constructions above. The present statements explicitly
join each generic interface to the already proved local realization, then
check its parameter range, initialization, updates, numerical model and
output contract.

The source maps continue to name published theorems used inside these
constructions. Input promises and oracle access remain part of the model.
An actually unproved assumption remains conditional. A paper depending on
proved local modules or identified published theorems can be ready for
mathematical review without a complete software implementation or a
proof-assistant formalization.

The [published-flow capacity adapter](../manuscripts/graph-backends/published-flow-capacity-scaling.md)
is an additional exact-flow route. It does not repair an allegedly absent
proof of the earlier local four-fifths flow result. Likewise, the newer
reference matching implementation is separate from the already completed
fast mathematical algorithm.

Earlier weaker warm-start bounds, superseded candidates and obstruction
notes retain their provenance without returning as competing headline
results. Their disposition is in the recovery index. Current review scopes
and executable coverage are maintained in the
[review registry](../reviews/README.md).
