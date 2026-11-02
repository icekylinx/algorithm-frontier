# Local source inputs

Original checkpoint ZIPs are local research inputs. They belong in
`.local/checkpoints/`, which is ignored by Git. Publish only selected,
reviewed proofs and programs in canonical problem or manuscript directories,
plus their source identities in `provenance/imports/`.

The local `index.json` lists filenames, sizes and SHA-256 hashes. It is an
inventory of the available inputs, not an independent proof certificate or
a replacement for the committed source manifests. Archive bytes are preserved
when moved from the repository root; no older archive is discarded merely
because a newer checkpoint exists. Unselected research routes remain in
those original ZIPs rather than as duplicate published source trees.

The SAT, factorization and later checkpoint import checks accept the organized
location and the earlier root location. An original ZIP is optional in a
fresh clone: metadata and canonical-target checks still run, while original
member replay runs only when that exact local ZIP is available. Each checker
reports whether it replayed original bytes.

When adding a checkpoint:

1. Place the untouched original ZIP in `.local/checkpoints/`.
2. Extract it to a temporary review directory, rejecting unsafe paths.
3. Compare candidate theorems with current results and cited primary sources.
   Keep substantive, complete results in their declared models; reject
   unresolved routes, dominated versions and routine direct consequences.
4. Record every member's identity and selection disposition. Map retained
   content to its canonical targets, preserving source and license credits.
5. Run the changed checks and affected metadata checks before committing.

Attribution: icekylinx and GPT-6 Astra Pro. Apache-2.0.
