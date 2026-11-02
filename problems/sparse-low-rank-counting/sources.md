# Sources, dependency interface and selection boundary

[Statement](README.md) · [Complete composition](proof.md) · [Finite checks](verify/README.md)

The selected construction composes a sparse matching partition function with
explicit low-rank completion moments, using total-degree truncation rather
than a rectangular exponent grid. Its substantive scope is the joint sparse
and low-rank algorithm, the whole `r=o(n)` regime and finite bit recovery.
The moment identities alone, pure low-rank permanent algorithms and routine
sparse counting consequences are not separate selected contributions.
Historical priority for this composition has not been established.

## Actual quantitative contraction premise

Anthropic, [*A `2^{o(n)}` Time Algorithm for 3-SAT*, version 1](https://hexagonmath.org/pdf/2610.00577v1),
Appendix A, Definition 7, Lemma 8 and Theorem A, part (b), supplies the quantitative
clique recursion. The primary PDF was checked on 2 November 2026, especially
pages 27–29 and equations (40)–(44). The recursion uses finite integer crossing
pieces, bit-width factorizations, succinct entry queries, deterministic grouping
search and final division by a scalar normalizer. The local
[ring-contraction proof](manuscripts/ring-contraction.md) specializes it to
normalizer one and checks finite coefficient construction, all Boolean wires
and grouped entry-query costs. Its arithmetic lift is a local deduction,
not the literal statement of the source theorem.

This package assumes the cited quantitative recursion as a mathematical
result. It supplies the division-free adaptation and complete downstream
reductions, with explicit finite coefficient arrays. It does not infer an
arithmetic theorem by running a bit algorithm symbolically, independently
re-prove the external recursion, or import a formal build certificate.

## Existing integral prerequisite and acyclic use

The checkpoint pins the finite Schur primitive to
[commit 2658b60c9d032611492792718bd9d39f721de09f](https://github.com/icekylinx/algorithm-frontier/tree/2658b60c9d032611492792718bd9d39f721de09f/problems/noncommutative-crossing).
The local [finite operator proof](../noncommutative-crossing/manuscripts/finite-crossing.tex),
[integral Schur proof](../noncommutative-crossing/manuscripts/integral-pieces.tex)
and [coefficient construction](../noncommutative-crossing/manuscripts/coefficient-computation.tex)
are the exact dependency. They construct integer pieces with normalizer
one, integer factorizations, polynomial bit height and effective finite
entry queries. The [retained prerequisite audit](manuscripts/integral-dependency-audit.md)
explains the state-weight indexing, finite Laurent extraction and integrality.
These algebraic arguments precede and do not depend on matrix exponents,
ordered insertion or SAT/counting consequences. No downstream assertion is
used to prove its own crossing primitive.

The [integer-factorization contract](../integer-factorization/sources.md)
concerns a different OpenAI theorem with the literal ring
`(Z/2^P Z)[V]/(V^ell)`, linear precision/truncation allowances and a Boolean
edge budget. It does not authorize an arbitrary ring lift and is not a
premise of this package. In particular, the exponentially many coordinates
of a moment algebra are explicitly paid for here rather than hidden in that
literal-ring interface.

## Prior work and bounded comparison

[Barvinok, *Two Algorithmic Results for the Traveling Salesman Problem* (1996)](https://doi.org/10.1287/moor.21.1.65)
proves polynomial-time permanent evaluation for fixed rank.
[Arvind, Chatterjee, Datta and Mukhopadhyay (FSTTCS 2018)](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.FSTTCS.2018.7)
give an `n^{O(r)}` permanent algorithm over every field. Both primary
publication records were checked on 2 November 2026. They establish that
the pure low-rank case is prior work; the joint sparse-support entropy bound
is the selected composition. No exhaustive literature novelty claim follows.

The checkpoint also compares squarefree-coefficient methods of Björklund,
Kaski, Koana and Nederlof, ICALP 2026, Article 36. That DOI did not resolve
through the browser during this review. It remains an attributed contextual
reference in the supplied proof, with no priority or separation conclusion
made solely from that unavailable text.

## Exact archive-to-package transformations

Source: the supplied `tcs_research_checkpoint.zip`, member prefix
`tcs_research_checkpoint/`. The committed [import manifest](../../provenance/imports/tcs-research-20261102.json)
records each original member's byte count, SHA-256 and selection disposition.

| Original checkpoint member | Retained destination | Transformation |
|---|---|---|
| `manuscripts/structured_exact_counting.md` | [proof.md](proof.md) | Part I complete; mixed overview and exceptional-vertex/acyclic/content branches omitted. Local links and attribution normalized; monomer numeric accounting stated explicitly. |
| `research_notes/universal_ring_contraction.md` | [ring-contraction.md](manuscripts/ring-contraction.md) | Complete general contraction theorem and proof retained; routine sparse corollaries/dense-bottleneck discussion omitted; exact finite Schur interface and acyclic dependency explanation added. |
| `manuscripts/structured_hypermatching.md` | [hypermatching.md](manuscripts/hypermatching.md) | Complete proof retained as supporting composition context, not a separate card; local links/attribution normalized. |
| `audits/integral_fock_dependency_audit.md` | [integral-dependency-audit.md](manuscripts/integral-dependency-audit.md) | Algebraic audit sections 1–6 retained; historical execution counts replaced with an explicit boundary and existing checker links. |
| `verification/structured_counting/check_sparse_low_rank.py` | [reference/reductions.py](reference/reductions.py), [verify/check_core.py](verify/check_core.py) | Reference identities separated from checker; unrelated exceptional-vertex branch removed; independent rational modular-lift checks added. |
| `verification/structured_counting/check_hypermatching.py` | [reference/hypermatching.py](reference/hypermatching.py), [verify/check_hypermatching.py](verify/check_hypermatching.py) | Definitions separated from checks; arithmetic and finite coverage preserved. |

The fixed-characteristic Hamiltonian branch, exceptional-set branches and
standalone routine sparse-counting corollaries are outside the selected
card. Supporting hypermatching proofs do not imply a general dense-input
improvement. No blanket `VP=VNP` conclusion, all-input decomposition algorithm,
implementation speed claim, external review or formal verification is made.

**Attribution:** icekylinx and GPT-6 Astra Pro. Apache-2.0 under the
[repository license](../../LICENSE); external results retain their named
attribution.
