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
| [Import manifests](imports/) | Additional numerical, quota and sparsification increments, plus the Subset Sum source snapshot |
| [Matching provenance](matching.md) | The matching manuscript's source-to-section map and the precise remaining Contract R dependency |
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
It does not compare edited manuscripts with historical hashes or certify
their mathematical claims.

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
