# Sources and scope of the exterior endpoint family

Authors: icekylinx and GPT-6 Astra Pro. Apache-2.0.

[Result statement](README.md) · [Complete proof](proof.md) · [Executable coverage](verify/README.md)

## Checkpoint provenance

The source is the 2 November 2026 `tcs_research_checkpoint.zip`, kept locally under `.local/checkpoints/`. It is not included in the publication. The following paths are members under its `tcs_research_checkpoint/` prefix. These are source SHA-256 values, not hashes of the edited target files.

| Source member | SHA-256 | Curated use |
|---|---|---|
| `manuscripts/exterior_endpoint_algorithms.md` | `f2704e2540abfa62a0783cc23e7ea71a93f20b6e61a673ce65afc72fce158882` | Main proof, including the exterior invariant, entropy bound, integral precision extraction, and bit realization; diagonal-loop signs expanded explicitly. |
| `manuscripts/triangular_immanants.md` | `d5c4ca062c84b6076e8119ee7e1f51d7861c54a64c320a585b1f169d768c7f78` | Final proof section completing the marked interface through classical Schur extraction; no separate result family. |
| `verification/structured_counting/check_dag_endpoint_set_dp.py` | `7ad9838097bfb5406f929c0e443ef7a8890c645cd8d3f810d29efce52cefc526` | Exterior recurrence adapted into `reference/exterior.py`; exact and modular independent oracles adapted into `verify/check.py`. The older factorial recurrence is omitted. |
| `verification/structured_counting/check_triangular_immanant_extraction.py` | `b17fb61ddc591d10495ffaf1897b968391ee7eb5bb783815c60b942186b76658` | Alternant extraction in the reference module and determinant-partition/extraction oracle in the checker. |
| `verification/low_rank_cycles/check_low_rank_modular_immanants.py` | `1d2b53adc145a535d1a934e0cd9c2d53df10e23f056cef0d8ad6e43b2ae0a664` | Independent Murnaghan--Nakayama character oracle only. Its separate low-rank vanishing claims are not imported. |

The curated reference accepts exact Python ring elements as well as optional modular integer reduction. Its sparse implementation omits coefficients found equal to zero; equality testing is an optimization of this implementation. The theorem unrolls all structurally permitted states and uses no ring identity test. New checks evaluate the full marked polynomial and its immanants end to end, and include rational and nonreduced coefficient rings.

## Classical mathematical inputs and comparisons

- Harry Crane, [*Some algebraic identities for the alpha-permanent*](https://arxiv.org/pdf/1304.1772), Theorem 1.1. Its parameters `alpha=-1`, `beta=q` yield the determinant-color identity after the displayed global sign. The identity is independently proved by coloring permutation cycles in the local proof. Its universal integer coefficients justify specialization to every commutative ring.
- Anna Knezevic and Greg Cohen, [*Some Facts on Permanents in Finite Characteristics*, 2019 PDF](https://vixra.rxiv.org/pdf/1908.0355v1.pdf), Theorem II.3.2.1(2), PDF page 20 (zero-based page 19). It explicitly states the rooted partition identity with composite characteristic permitted. Only this elementary identity, independently proved locally, is used. The related [arXiv record](https://arxiv.org/abs/1710.01783) credits Anna Knezevic, Greg Cohen, and Marina Domanskaya in its 2020 revision. No unrestricted algorithmic claim from that preprint is assumed.
- I. P. Goulden and D. M. Jackson, [*Immanants, Schur Functions, and the MacMahon Master Theorem*](https://uwaterloo.ca/math/sites/default/files/uploads/documents/gjpams1992.pdf), Proceedings of the AMS 115(3), 605–612, 1992, Theorem 2.1 and equation (9). This supplies the classical squarefree Schur/immanant coefficient bridge. Together with dual Cauchy and the alternant identity it completes the marked algorithm over integers, without factorial or character-dimension normalization and without division in small characteristic.
- Stephan Mertens and Cristopher Moore, [*The Complexity of the Fermionant and Immanants of Constant Width*](https://theoryofcomputing.org/articles/v009a006/), Theory of Computing 9(6), 2013. Their general-matrix hardness for fixed fermionant parameters concerns a different input class. The supplied triangular decomposition and factor width are essential to the retained algorithm.
- Samir Datta and Kishlaya Jaiswal, [*Parallel Polynomial Permanent Mod Powers of 2 and Shortest Disjoint Cycles*](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.MFCS.2021.36), MFCS 2021, Article 36. Fixed-power-of-two permanent tractability already holds for unrestricted matrices; it is not advertised here as a new structural tractability result.

The primary publications/preprints above were inspected on 2 November 2026. Bounded searches for triangular-plus-low-rank permanents, fermionants, immanants, and Hamiltonian counting did not identify the exact colored endpoint algorithm and its entropy bound. This supports an explicit, limited novelty boundary; it does not establish exhaustive priority.

## Selected contribution and exclusions

The selected mathematical work is the constructive exterior endpoint state, its changing-order sign invariant, the resulting rank-dependent entropy bound, and the integral prime-power extraction using at most `pt` colors. Classical determinant coloring, Cauchy--Binet, low-rank vanishing, and symmetric-function extraction are credited antecedents. The immanant completion is retained to document and test the full marked interface of this one family.

The older factorial coefficient-algebra route in `manuscripts/triangular_modular_counting.md` and `research_notes/dense_dag_modular_counting.md` is dominated for Hamiltonian evaluation by the exterior route and is not copied. Its permanent variants, cycle-hitting-set corollaries, and source result dumps are not separate retained results. Positive-target rank-one observations, unrestricted dense permanent routes, growing-modulus exact Hamiltonian recovery, Fock/contraction assumptions, and incomplete general-case algorithms are excluded.

The ready-for-review status records a complete local mathematical deduction and executable finite verification. External peer review, proof-assistant verification, and a publication-level literature-priority audit remain outside that status.
