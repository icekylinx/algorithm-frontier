# New primary-source comparisons for checkpoint T

**Checked 25 October 2026. This note records only the comparisons added for the prefix and laminar directions.**

## 1. Exact profiles and weighted prefix discrepancy

Eisenbrand, Rohwedder and Węgrzycki, *Sensitivity, Proximity and FPT Algorithms for Exact Matroid Problems*, arXiv:2404.03747v2, are a primary antecedent for exact vector-weight matroid problems and recovery by weight profiles and a partition constraint. Their Theorem 3 and the discussion around arbitrary-objective optimization must be kept separate from the present exact signed-scalar theorem.

<https://arxiv.org/html/2404.03747v2>

The current prefix analysis uses maximum cumulative target and order geometry to bound useful mass and incidence colors. It is not a claim to have introduced profile enumeration or partition recovery.

Bérczi, Liu, Reis and Tarnawski, *Weighted Equitability and Matroid-Constrained Discrepancy*, arXiv:2608.13983v1, study additive discrepancy and cost-aware rounding under matroid constraints. Their weighted-prefix theorem in Section 6 is a relevant comparison, but an additive-discrepancy conclusion is not an exact numeric-quota FPT theorem.

<https://arxiv.org/html/2608.13983v1>

The present exact prefix result does not settle a constant-discrepancy conjecture or improve that paper's discrepancy bound.

## 2. Huang–Ward is the representative-method antecedent

Huang and Ward, *FPT-Algorithms for the ell-Matchoid Problem with a Coverage Objective*, Definition 3.1, Algorithm 1, and Theorem 3.6, give oracle joint representatives using highest-weight candidates and independent closure tests. Their stated size bound has the form

\[
 \Gamma_{\ell,k}=\sum_{j=0}^{(k-1)\ell}\ell^j.
\]

The definition permits a candidate subset and signed real element weights. These statements and the associated closure-path proof were checked directly.

<https://arxiv.org/pdf/2011.06268>

<https://www.di.ens.fr/~cchuang/work/matchoid.pdf>

The basic laminar proof adapts this recursion, keeping the actual sum d of test ranks instead of the coarser product bound. Its candidate count is \(\sum_{j=0}^{d}\ell^j\). It is a total-rank refinement and an application, not a new general representative-set paradigm.

For precision, there is also a formal way to invoke the published theorem after the new blocker reduction. Give each independent test set private copies in its own auxiliary matroid, parallel to the corresponding candidate elements. A protected context then has size at most d+1. Applying the published theorem gives \(\Gamma_{\ell,d+1}\), with depth d ell. In the laminar application ell is O(B) and d is O(B). This would give a \(2^{O(B^2\log B)}\) catalogue and a weaker derived \(2^{O(B^3\log B)}\) algorithm after selecting B candidates.

That last deduction is our inference using the proved laminar blocker structure; it is not a theorem about weighted quotas stated in the source. Tracking the actual total ranks directly yields the smaller \(2^{O(B^2\log B)}\) running time in LM.

## 3. The 2026 reachable kernels do not directly solve the weighted-quota model

Huang, Kakimura, Kobayashi and Terao, *Polynomial Kernels with Reachability for Weighted d-Matroid Intersection*, arXiv:2603.17345v1, give randomized reachable kernels for one arbitrary matroid and specified simpler matroids. The relevant statements are Definition 1, Theorems 1–4, the laminar discussion in Section 5, and the separate deterministic results in Section 7.

<https://arxiv.org/html/2603.17345v1>

Three model distinctions matter.

- A common-weight upper quota is not generally a matroid. With capacity two and element weights 2,1,1, a feasible singleton of weight two cannot be augmented by either element of a feasible two-element set.
- The depth partitions in LM/VZ are tests for one proposed exchange. The original selected set need not be independent in them.
- Fixed-d and randomized guarantees cannot silently become a uniform deterministic guarantee with d growing with B.

Thus the paper is a significant nearby baseline, but no direct model-preserving substitution giving a smaller deterministic theorem was established in the inspected statements. This is a bounded comparison, not an exhaustive absence claim.

## 4. Optimal zero completion uses an established valuation theorem

Husić, Loho, Smith and Végh, *On complete classes of valuated matroids*, TheoretiCS 3 (2024), Article 24, provide the precise interface used in VZ. Definition 1.1 defines weighted R-minor valuations by full-basis matchings, equation (1b) gives valuated exchange, and Theorem 2.9 states weighted network induction, attributed there to Murota's theorem. Contraction fixes the mandatory dummy left vertices.

<https://theoretics.episciences.org/14792/pdf>

For our mapping, positive copies have private matching edges and R-k conceptual dummy vertices can match any zero-weight unit. Negating true scalar costs makes the induced value the negative of the best zero-completion cost. This mapping supplies the public exchange theorem with its actual hypotheses.

The new algorithmic composition then proves the overlap-first replacement lemma and implements each required optimization on a compressed mixed ground. It uses one box-truncated shared rank and one two-group partition, with individual unit caps on positive copies and binary counts on zero coordinates. The public valuation closure alone does not provide those implementation or laminar-quota arguments.

The conceptual Rado graph may be numerically enormous. It is never built and is not part of the algorithm's time or workspace.

## 5. Lower-bound antecedents and scope

Doron-Arad, Kulik and Shachnai, *You (Almost) Can't Beat Brute Force for 3-Matroid Intersection*, arXiv:2412.02217v2, explicitly discuss one paving-type resource with additional partition constraints and selected acceptable rank-sized families. Their Section 3 is a direct antecedent for the hidden-resource constructions.

<https://arxiv.org/html/2412.02217v2>

Their *Lower Bounds for Matroid Optimization Problems with a Linear Constraint*, arXiv:2307.07773v2, Definitions 4.4–4.5 and Lemma 4.6, supplies a primary precedent for SAT-encoded valid matroid decoders.

<https://arxiv.org/html/2307.07773v2>

The new lower contributions in T are the maximum-target/order calibration, the actual-support budget envelopes, and the joint p-family/B-prefix construction. They are not claims to have introduced paving or SAT-matroid lower methods.

The encoded reductions include all rank-query sizes and a validity proof for every supplied formula. Reading the rank program is allowed. Deterministic ETH and randomized ETH are distinguished; query indistinguishability is not used as a substitute for a computational assumption on readable programs.

## 6. The row-dependent boundary

Lin, Ren, Sun and Wang, *Constant Approximating Parameterized k-SetCover is W[2]-hard*, arXiv:2202.04377v2, identify exact k-SetCover as the standard W[2]-complete parameterized problem. The introduction and the statement context were checked.

<https://arxiv.org/html/2202.04377v2>

RW uses only this exact-decision baseline. Its coefficient-1/2 full-prefix reduction yields W[2]-hardness in the largest target when weight vectors can vary arbitrarily by row. The paper's approximation and stronger quantitative conclusions are not imported into RW.

## 7. Additional OpenAI-index check

The public index was reopened:

<https://raw.githubusercontent.com/openai/math/main/CONTENTS.md>

For this increment, exact term searches for laminar, valuated, matchoid, and quota found no matching index text. Prefix hits referred to other subjects and did not identify this exact quota model. The index's matroid descriptions include different online, counting, and infinite-matroid topics.

This check concerns the index and displayed descriptions only. It does not establish that no linked manuscript contains a relevant lemma, nor that the new theorem is absent from unpublished work. The current proofs do not assume a new unverified OpenAI lemma about prefix or laminar quotas.

## 8. Status of the claims

Checkpoint T contains complete internally reviewed derivations, with its mathematical dependencies and remaining gaps explicit. Internal review is not formal verification or external peer review. The documents distinguish proved constructions from primary antecedents and from incomplete prospective extensions.

No priority claim, exhaustive literature-absence claim, or improved general-matching exponent is made in this increment.
