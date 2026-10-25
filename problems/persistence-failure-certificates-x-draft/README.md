# Persistent-homology failure certificates — checkpoint X draft

**Status: Draft checkpoint X.** This source-linked candidate remains under proof, algorithm, and source review.

| Field | Candidate statement |
|---|---|
| **Guarantee** | For a `p`-dimensional simplicial complex over a specified coefficient field, retain at most `min(N, r * binom(h + a + b, a + b))` original top-dimensional simplices while preserving every allowed correlated-failure persistence module through dimension `p - 1`. |
| **Objective and output** | Given at most `h` failed labels, remove failed vertices, cofaces, and labelled top simplices; the retained subcomplex should induce the same boundary spaces at every filtration threshold. A separate cost-ordered construction preserves the canonical minimum-cost surviving boundary basis. |
| **Time** | Uniform deterministic polynomial time in the explicit complex and field representation, subject to the source feature-construction and exact linear-algebra model. No near-linear bound is claimed. |
| **Space** | The displayed bound counts retained top simplices only. It does not bound all retained faces, encoded bits, or Gaussian-elimination workspace. |
| **Parameters** | `N` is the number of top simplices; `r` is the rank of the top boundary matrix; `p` is the complex dimension; `a` bounds failure labels per vertex; `b` bounds extra labels per top simplex; `h` is the failed-label budget. |
| **Model and representation** | Explicit finite simplicial complex; coefficients over the rationals or an explicitly represented finite field. Filtration order and cost order are separate constructions unless they coincide. |
| **Lower-bound scope** | The draft gives matching constructions for the stated original-cell envelope and attributes ordinary no-failure bounds to prior sources. It does not claim preservation of top-dimensional homology, torsion, homotopy type, or an unconditional literature priority. |
| **Review status** | Draft checkpoint X. Proof, algorithm, and source review are pending; formal verification is not claimed. See the [checkpoint X backlog](../../reviews/backlog/checkpoint-x-drafts.md). |
| **Source** | [Correlated-failure boundary draft](../../sources/checkpoint-x/03_correlated_fault_boundary_and_persistence_sparsifiers.md). |

**Attribution:** Yilin Liu and GPT-6 Astra Pro.
