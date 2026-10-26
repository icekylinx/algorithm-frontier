# Sources and proof dependencies

## Canonical manuscripts

- [Exact degree-constrained subgraphs from the general matching backend](proof.md)

## What is proved and what is imported

**Self-contained reduction.** Theorem 1.1 and Sections 2–5 construct
the sparse selector, prove both directions of the perfect-matching
equivalence, handle interval bounds and parity, and encode exact/ranged
cardinality. The permutation-network routing proof is included. No
randomization or external numerical backend is used by these reductions.
The [finite checker](verify/check_reductions.py) tests the actual small
gadgets with independent exact methods.

**Classical reduction provenance.** The prescribed-degree selector is
the split-network form of Section 10 of the
[OpenAI matching manuscript](https://github.com/openai/math/blob/main/preprints/Almost-Linear-Time-Maximum-Cardinality-Matching-in-Sparse-General-Graphs-September-24-2026/build/sections/10-f-factors.tex).
The interval, parity and cardinality gadgets are elementary extensions;
no publication-priority claim is made for them.

**Conditional quantitative input.** Only the fast running-time corollary
uses [the general-matching theorem](../general-matching/proof.md),
including its Section 2 published primitives and Section 11.6 requirements
for a deterministic cycle-search implementation.
Replacing that solver by any correct exact matching algorithm preserves
the reductions' correctness and changes their running time accordingly.
The repository now supplies one such
[unconditional reference solver](../general-matching/reference/README.md)
with original edge IDs and an independently verified optimality certificate.
The full sparse degree-constrained gadget construction is still a
mathematical reduction, separately exercised by its finite checker.
An arbitrary unsuccessful attempt to find a perfect matching cannot
serve as a NO certificate; the supplied matching must be maximum.

**Public comparator.** Gabow's
[*Maximum Cardinality f-Matching in Time O(n^(2/3)m)*](https://arxiv.org/abs/2311.14236v1)
states the separate deterministic simple-graph and multigraph bounds
quoted in Section 7. It supplies a benchmark, not an assumption needed
to prove the gadgets or to implement the faster cycle-search machinery.

## Linked mathematical dependencies

These manuscripts contain the interfaces, auxiliary arguments or source
comparisons referenced by this result. Their stated hypotheses remain
part of each use; an interface analysis does not supply an omitted backend.

- [A deterministic near-linear final maximum-matching verifier](../../manuscripts/graph-backends/deterministic-maximum-matching-verifier.md)
- [OpenAI baseline and exact imported interfaces](../../manuscripts/graph-backends/oai-baseline-and-imports.md)
- [A 4/5 research composition from sequential expander routing](../../manuscripts/graph-backends/quantitative-matching-4-5-composition.md)

## Evidence and provenance

The [verification note](verify/README.md) states the scope of executable
evidence and the remaining mathematical dependencies. The
[import record](../../provenance/README.md) preserves source revisions,
canonical paths, attribution and applicable licenses.

**Attribution:** Yilin Liu · GPT-6 Astra Pro.
