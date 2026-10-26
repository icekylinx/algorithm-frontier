# Verification and review scope

The main mathematical theorem is justified symbolically by the canonical [TeX proof](../manuscripts/self_concordant_sparsification.tex); it is not inferred from numerical experiments.

The source research package of October 26, 2026 records two independent research-session proof audits, one of which fingerprints a pre-clarification snapshot. Both reported no substantive gap in the checked arguments. Clarifications to the final source explicitly assume positive ambient dimension and state the supplied parameter-upper-bound requirement for the oracle algorithm. The final TeX source's SHA-256 is `e0aeb9e93cced63a452c85de0fe48e2327c5c9f565b96ce5156482fdb61e336a`. These reports are internal; none is external peer review, formal verification or a novelty certificate.

The proof imports three Reis--Rothvoss theorems. Their exact statements, and Saunderson's baseline, were checked against the primary arXiv versions cited in [sources](../sources.md). The proof is an existence theorem; the paper's algorithm uses a randomized strong separation-oracle model, not a shipped arbitrary-cone Turing implementation. There is no universal-cone finite test suite because such checks cannot establish the theorem.

The source package separately contains checks for single-edge-failure matching, finite-menu rebalancing and Boolean-slice rigidity. Those are independent companion results and their finite receipts do not verify the conic sparsification theorem. They are not misrepresented as checks of this family.

Local source build (when a TeX distribution is installed):

```sh
cd problems/conic-barrier-sparsification/manuscripts
pdflatex -interaction=nonstopmode -halt-on-error self_concordant_sparsification.tex
pdflatex -interaction=nonstopmode -halt-on-error self_concordant_sparsification.tex
```

Do not interpret repository structural CI as proof-assistant verification. In particular, the source package's reported seven-page rendered-PDF review and mathematical audits are scoped to the research session; this repository commits the editable source, not a new externally reviewed paper.
