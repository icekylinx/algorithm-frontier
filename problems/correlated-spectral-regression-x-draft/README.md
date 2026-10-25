# Correlated spectral, regression, and seminorm summaries — checkpoint X draft

**Status: Draft checkpoint X.** Family-level review handle; not promoted.

| Field | Candidate statement |
|---|---|
| **Guarantee** | One fixed reweighting is proposed for every allowed correlated label failure in PSD sums, graph spectra, graded incidence operators, weak convex regression, and whole-block seminorm sums. Existential, randomized compact, and deterministic constructions remain distinct. |
| **Objective and output** | Preserve all stated quadratic, seminorm, spectral, or weak-regression objectives after every failure scenario using the same original items and coefficients. |
| **Time** | The graph rows state an `O_{a,b}(min{m, r h^(a+b) log^(a+b)(2L) / epsilon^(a+b+2)})` spectral branch and a separate exact cut branch. Regression and seminorm rows retain backend-dependent logarithms and oracle assumptions. |
| **Space** | Support and lifted feature dimension are separate. Random-code storage, PSD-sparsifier workspace, response-subspace data, and finite-precision evaluation remain open accounting items. |
| **Parameters** | `r` is rank; `h` is the failure budget; `a,b` bound vertex/edge label degree; `L` is the label universe; `epsilon` is relative error. Regression rows add response dimension, regularization, and inverse-accuracy parameters. |
| **Model and representation** | Correlated label failures with a fixed filtration/query family; finite-field or real PSD models; weak convex regression with supplied response/penalty structure; arbitrary seminorms only with the stated evaluation or existence contract. |
| **Lower-bound scope** | Lower examples are model-specific and do not transfer automatically across spectral, cut, regression, and seminorm objectives. |
| **Review status** | Proof, algorithm, and source review are pending; formal verification is not claimed. |
| **Source** | Payloads `03`, `11`, `15`, `17`, `18`, `19`, and `26` in `sources/checkpoint-x/`. |

**Attribution:** Yilin Liu and GPT-6 Astra Pro.
