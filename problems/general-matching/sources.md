# Sources and proof dependencies

## Canonical manuscripts

- [Deterministic Exact General Matching through Persistent Integral Carriers and Normalized Routing](proof.md)

## Dependency status

**Unconditional executable solver.** The
[reference implementation](reference/README.md) uses only Python's standard
library. Its cubic-per-kernel blossom search implements the classical method
of [Edmonds, *Paths, Trees, and Flowers* (1965), Section 4](https://doi.org/10.4153/CJM-1965-045-4).
Its optional certificate uses one failed alternating forest, adding only
quadratic work per kernel. The [complete extraction proof](reference/certificate-proof.md)
establishes its tight odd-component bound and exposable set locally;
[Gallai (1964), Theorem (E.1)](https://real.mtak.hu/189486/1/cut_MATKUTINT_1964_3_pp401_-_413.pdf)
is historical provenance, not an assumed extraction theorem. The certificate's
sufficiency also has an elementary proof, and its verifier imports no
matching implementation. There is no external runtime package or
unimplemented cycle-search dependency in this reference solver.

**Unconditional local reductions.** Lemmas 3.1–3.2 prove the exact
matching-size kernel, its componentwise form and the subcubic gadget.
The companion's [mixed-failure theorem](../../manuscripts/graph-backends/matching-size-kernel-corollary.md#4-one-kernel-for-mixed-vertex-and-edge-failures)
extends exact preservation to every mixture of at most $`f`$ native
vertex/edge failures in a fixed simple graph. These reductions need no
external matching algorithm, random sampling or raw-cycle interface.
The [finite reduction checker](verify/check_reductions.py)
tests their small instances independently of the proposed backend.

**Explicit unresolved implementation hypothesis.** [the required deterministic cycle-search implementation](proof.md#116-explicit-raw-backend-realization-contract)
is required for the four-fifths logarithmic overhead. Its five clauses
specify raw geometric quality, chronological construction/recourse,
occurrence retirement, finite-bit weighted-tree realization, and uniform
executable bounds. This remains an unimplemented research requirement.
Section 11.6 compares it explicitly with the published deterministic
distance-oracle cycle construction and states the required direction of
the physical path-length certificate. A citation to that construction
does not establish the stronger parameters and lifetime operations.

**Imported matching framework.** Section 2.2 imports the OpenAI
matching-state identities, bounded objectives and localized exchange/lock
interfaces. The current proof changes the integral carrier, optimum-gap
driver, numerical parameters and recovery. It does not re-prove every
inherited state invariant.

**Imported data structures and geometry.** The dynamic-forest operations
of AHLT, the bounded-volume one-edge-out discovery of CHHIP, the
stable-forest geometry of KMPG/CKL/AN, and the balanced-cut and
hierarchy primitives of CGLNPS/CS/CHS/KMPS retain their source hypotheses.
In particular, a real-arithmetic weighted-tree theorem alone does not
discharge the finite-bit realization requirement.

**Acceptance inside the faster theoretical composition.** The single augmenting-path search in
[the verifier interface](../../manuscripts/graph-backends/deterministic-maximum-matching-verifier.md)
is based on Mehlhorn–Nobahari's account of Gabow's algorithm,
[arXiv:2603.22909v2](https://arxiv.org/html/2603.22909v2), Sections 2.3 and 4.
It certifies the optimality of an accepted output. It supplies neither
the proposed backend nor its time bound. The classical fallback gives
termination independently of the favorable fast branch. This theoretical
near-linear acceptance interface is distinct from the executable reference
solver and its separately constructed certificate; the reference's cubic
computation is not silently charged as near-linear work.

## Linked mathematical dependencies

These manuscripts contain the interfaces, auxiliary arguments or source
comparisons referenced by this result. Their stated hypotheses remain
part of each use; an interface analysis does not supply an omitted backend.

- [A classical independent optimality verifier for general matching](../../manuscripts/graph-backends/classical-matching-optimality-verifier.md)
- [A deterministic near-linear final maximum-matching verifier](../../manuscripts/graph-backends/deterministic-maximum-matching-verifier.md)
- [An exact matching-size kernel and the current time corollary](../../manuscripts/graph-backends/matching-size-kernel-corollary.md)
- [Executable exact matching and its independent certificate](reference/README.md)
- [A 4/5 research composition from sequential expander routing](../../manuscripts/graph-backends/quantitative-matching-4-5-composition.md)
- [Exact general-graph matching](README.md)

## Primary references

The manuscripts identify the theorem and version used at each import.
Direct external references appearing in this reading path are:

- [Edmonds (1965): classical blossom search](https://doi.org/10.4153/CJM-1965-045-4)
- [Gallai (1964), Theorem (E.1): historical decomposition reference](https://real.mtak.hu/189486/1/cut_MATKUTINT_1964_3_pp401_-_413.pdf)
- <https://arxiv.org/abs/1703.03998v1>
- <https://arxiv.org/abs/1705.10709v1>
- <https://arxiv.org/abs/1910.08025v2>
- <https://arxiv.org/abs/2007.14898v1>
- <https://arxiv.org/abs/2009.08479v1>
- <https://arxiv.org/abs/2203.00671v1>
- <https://arxiv.org/abs/2311.06402v1>
- <https://arxiv.org/abs/2311.18295v1>
- <https://arxiv.org/abs/2405.03908v1>
- <https://arxiv.org/abs/2609.23852v1>
- <https://arxiv.org/abs/cs/0310065v2>
- <https://doi.org/10.1137/17M1115575>
- <https://github.com/openai/math/tree/main/preprints/Almost-Linear-Time-Maximum-Cardinality-Matching-in-Sparse-General-Graphs-September-24-2026>

## Evidence and provenance

The [verification note](verify/README.md) states the scope of executable
evidence and the remaining mathematical dependencies. The
[import record](../../provenance/README.md) preserves source revisions,
canonical paths, attribution and applicable licenses.

**Attribution:** Yilin Liu · GPT-6 Astra Pro.
