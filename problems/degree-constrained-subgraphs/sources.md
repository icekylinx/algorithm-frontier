# Sources and proof dependencies

## Canonical manuscripts

- [Exact degree-constrained subgraphs from the general matching backend](proof.md)
- [Linear-size selector from a named expander construction](linear-selector.md)

## What is proved and what is imported

**Self-contained reduction.** Theorem 1.1 and Sections 2–5 construct
the sparse selector, prove both directions of the perfect-matching
equivalence, handle interval bounds and parity, and encode exact/ranged
cardinality. The permutation-network routing proof is included. No
randomization or external numerical backend is used by these reductions.
The [finite checker](verify/check_reductions.py) tests the actual small
gadgets with independent exact methods.

**Optional linear-size selector.** Theorem 1.2 imports one precise mathematical fact: Gabber and Galil, [*Explicit Constructions of Linear-Sized Superconcentrators*](https://doi.org/10.1016/0022-0000(81)90040-4), Section 2, Theorem 2, for the five modular permutations stated in the [selector proof](linear-selector.md). Sections 2–4 of that proof derive the concentrator, recursive superconcentrator and deterministic linear enumeration. Sections 5–6 give the binary-fan adapter and the simple subcubic matching gadget. Thus the expansion theorem supplies a quantitative neighbor-set inequality; every construction and matching-interface step is explicit locally.

The finite cutoff uses the already implemented Beneš network. The constants <code>p=31</code>, cutoff <code>2^26</code> and contraction factor <code>63/64</code> are fixed; they make this an asymptotic size refinement rather than a measured practical speedup. The construction algorithm does not find the disjoint routes: their existence proves the gadget's extension direction. This respects the primary paper's separate linear-time routing question in Section 5, Problem 8. No Alon–Capalbo construction or unstated finite-ring enumeration is needed. The shipped solver continues to use Theorem 1.1.

**Classical reduction provenance.** The prescribed-degree selector is
the split-network form of Section 10 of the
[OpenAI matching manuscript](https://github.com/openai/math/blob/main/preprints/Almost-Linear-Time-Maximum-Cardinality-Matching-in-Sparse-General-Graphs-September-24-2026/build/sections/10-f-factors.tex).
The interval, parity and cardinality gadgets are elementary extensions;
no publication-priority claim is made for them.

**Proved quantitative input.** The fast running-time corollary
uses [the general-matching theorem](../general-matching/proof.md),
including its Section 2 published primitives and the deterministic
cycle-search realization in Theorem 11.6. That construction supplies the
interface used by the corollary; executable coverage is recorded separately.
Replacing that solver by any correct exact matching algorithm preserves
the reductions' correctness and changes their running time accordingly.
The repository now supplies both the
[unconditional exact matcher](../general-matching/reference/README.md)
and the [complete degree-subgraph reference solver](reference/README.md).
The latter constructs the sparse gadgets, decodes original IDs, checks
each matching NO certificate and supplies a final excluded-cardinality
interval for optimization. Its [implementation proof](reference/correctness.md)
has an ordinary polynomial bound and no external runtime package.
An arbitrary unsuccessful attempt to find a perfect matching cannot
serve as a NO certificate; the supplied matching must be maximum.

**Verification boundary.** The degree verifier checks native witnesses
directly and rebuilds the sparse reduction for a NO or optimality
certificate. It uses the independent matching certificate checker and
never runs matching search. The deterministic reduction builder is
shared code, not a second independent construction. The
[executable oracle suite](verify/check_reference.py) compares answers
against exhaustive original-edge subset enumeration.

**Public comparator.** Harold N. Gabow's
[*Maximum Cardinality `f`-Matching in Time `O(n^(2/3)m)`*](https://arxiv.org/abs/2311.14236v1)
Theorem 4.1 states the separate deterministic simple-graph and multigraph bounds
quoted in Section 7. It supplies a benchmark, not an assumption needed
to prove the gadgets or to implement the faster cycle-search machinery.

## Linked mathematical dependencies

These manuscripts contain the interfaces, auxiliary arguments or source
comparisons referenced by this result. Their graph models, parameter ranges
and output contracts remain part of each use. The matching realization
supplies the formerly abstract fast-solver interface.

- [A deterministic near-linear final maximum-matching verifier](../../manuscripts/graph-backends/deterministic-maximum-matching-verifier.md)
- [OpenAI baseline and exact imported interfaces](../../manuscripts/graph-backends/oai-baseline-and-imports.md)
- [A `4/5` research composition from sequential expander routing](../../manuscripts/graph-backends/quantitative-matching-4-5-composition.md)

## Evidence and provenance

The [verification note](verify/README.md) states the scope of executable evidence, the finite selector-adapter checks, and the exact published dependency of the linear-size variant. The
[import record](../../provenance/README.md) preserves source revisions,
canonical paths, attribution and applicable licenses.

**Attribution:** Yilin Liu · GPT-6 Astra Pro.
