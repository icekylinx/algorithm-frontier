# Sources, attribution and canonical paths

The mathematical manuscripts are maintained in `problems/` and
`manuscripts/`. This directory records their origin and preserves imported
license boundaries. There is one current copy of each retained manuscript.

## Records

| Record | What it identifies |
|---|---|
| [Canonical map](canonical-map.json) | Every original source path, its retained destination or integration target, and the disposition of redundant material |
| [Archive manifest](archive-manifest.json) | The supplied archive inventory and archive-level fingerprints |
| [Checkpoint file manifest](checkpoint-files.json) | The original checkpoint payload inventory and recorded hashes |
| [Import manifests](imports/) | Additional numerical, quota, sparsification and algebraic-complexity increments, plus the Subset Sum source snapshot |
| [Affine ROABP PIT import](imports/roabp-affine-pit.json) | Exact reviewed source identities and reversible publication edits for the fixed-width all-characteristic PIT package |
| [Matching provenance](matching.md) | The matching manuscript's source-to-section map and the realized cycle-search dependency chain |
| [Checkpoint restoration](checkpoint-restoration.md) | Earlier completed results, their original archive evidence, current realizing proofs and attribution corrections |
| [Subset Sum source manifest](imports/subset-sum/source-manifest.json) | The imported Subset Sum material and source-project revision |

The original pre-consolidation tree is available in repository history at
[e4cd7e6](https://github.com/icekylinx/algorithm-frontier/tree/e4cd7e6050a9c80de6562ae1efc17f61ca3839be).
Historical source filenames in the manifests identify that material; they
are not current navigation paths.

## Reading the canonical map

Each entry has one of three dispositions.

- **Moved:** the manuscript or metadata has a canonical destination.
- **Integrated:** its mathematical content was incorporated into the linked
  main proof or companion, so a separate copy is unnecessary.
- **Removed:** a superseded overview, duplicate review, process log, broken
  wrapper or other redundant artifact was removed after its substantive
  content and dependencies were considered.

The `source_revision_sha256` field fingerprints the source bytes at the
consolidation step. Some of those bytes already include mathematical edits.
It is neither an original-upload fingerprint nor a promise that the current
canonical file will never change. Original-import hashes remain in their
respective manifests; commits identify later revisions.

The additional `retired_canonical_paths` map records later consolidation
within the semantic manuscript tree. These superseded paths must be absent;
their retained destination identifies the integrated mathematical content.

`python3 tools/check_provenance.py` checks unique original paths, valid
dispositions, retained target existence and required license boundaries.
It also checks the recovery index against the original archive manifests,
its inventory counts and its canonical targets. The archived ZIPs are not
shipped as duplicate source trees, so ordinary CI does not replay their
extraction or compare edited manuscripts with historical bytes. These
metadata checks do not certify mathematical claims.

The affine ROABP package has an additional
[source-binding check](../problems/roabp-affine-pit/verify/check_source_bindings.py).
It reverses the explicitly recorded publication edits and verifies the
original mathematical-source hashes, without keeping duplicate checkpoint
trees. Each record identifies either an exact member of the frozen
checkpoint-22 archive or a later session source with its own hash; the
archive is not represented as containing the later additions.
Native-TeX PDF bindings and visual-review evidence are checked
separately. Neither check is an external review or a mathematical certificate.

## Licenses and third-party attribution

The repository's [Apache-2.0 license](../LICENSE) and
[citation protocol](../PROTOCOL.md) apply to its original material.
The Subset Sum import retains its original
[license](imports/subset-sum/licenses/LICENSE),
[NOTICE](imports/subset-sum/licenses/NOTICE),
[author record](imports/subset-sum/licenses/AUTHORS.md) and
[source status](imports/subset-sum/licenses/STATUS.json).

The retained NOTICE is a historical document from the source project.
References inside it to that project's baseline trees, local archives or
checker layout describe the imported project, not files asserted to exist
in this repository. Current proof dependencies and runnable certificates
are listed on the
[faster-time](../problems/subset-sum-fast-deterministic/sources.md) and
[low-space](../problems/subset-sum-low-space-deterministic/sources.md)
source maps. The consolidation preserves third-party credits and does not
attribute imported constructions to the repository's continuation work.

The [evidence registry](../reviews/README.md) distinguishes manuscript
arguments, exact computational certificates and finite regression checks.
Historical internal-review statements do not constitute external peer review
or proof-assistant verification.

## Integer factorization imports

The [factoring import record](imports/integer-factorization.json) identifies
both supplied archives and all 31 original members. Nineteen retained members
map to 18 canonical English targets; 12 excluded members have metadata only.
The [selected conditional theorem](../problems/integer-factorization/) and
[retained direct research branch](../manuscripts/integer-factoring-research/)
have separate review scopes. Original ZIPs remain ignored. The factoring
import checker replays their exact bytes when they are locally available.

## Selective SAT research import

The [SAT import manifest](imports/sat-research.json) records all 1,069 original
member identities, with 22 selected members adapted into 20 proof and code
targets. The [selection summary](../docs/SAT-RESEARCH.md) identifies the two
substantive algorithm families and explains the exclusion of incomplete
routes, dominated results, theorem reconstruction and direct corollaries.
Reader guides and wrappers are current curation work. Excluded payloads are
not copied into the repository.

`python3 tools/verify_sat_import.py` checks selected targets and cleanup
metadata, and replays original member bytes when the ignored ZIP is locally
available. Historical source hashes do not freeze edited manuscripts. This
is provenance evidence, not mathematical or proof-assistant certification.
