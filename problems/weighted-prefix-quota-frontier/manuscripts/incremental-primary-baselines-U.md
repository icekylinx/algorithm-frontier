# Primary baselines and method credits for increment U

**25 October 2026. New comparisons for the sparse-quota and deterministic-kernel increments.**

This note records directly checked primary antecedents and the limits of the comparisons. It is not an exhaustive literature survey. The new manuscript proofs, rather than a missing search result, support their mathematical conclusions.

## 1. Reachable kernels: determinism versus output size

Huang, Kakimura, Kobayashi and Terao, *Polynomial Kernels with Reachability for Weighted d-Matroid Intersection*, arXiv:2603.17345v1, is the closest checked kernel comparator. Its Theorems 1–3 and Corollary 2 give randomized small grounds for partition, coverable, and explicitly represented transversal systems. Theorem 5 treats matching with an edge matroid. Theorem 6 gives a deterministic $`k^2(g(k)+1)`$ ground for one arbitrary and one coverable matroid. Section 7 states deterministic single exchangeability; Lemma 2 supplies the greedy replacement property.

<https://arxiv.org/html/2603.17345v1>

Translated into **one arbitrary matroid plus $`d`$ additional matroids**, its partition/transversal size is $`\widetilde O(k^{d+1})`$, and its coverable size is $`\widetilde O(k\prod_i g_i(k))`$. The graph-matching size is $`\widetilde O(k^3)`$. These degrees are smaller than U's deterministic bounds. The one-additional-coverable endpoint of CK equals its deterministic bound. No improvement of that endpoint is claimed.

TR explicitly credits the same source's Section 4 matching-witness lift. Its own neighborhood-truncation and threshold argument establishes the stated uniform implementation. Nonunit partition capacities are already included by the public result and are not a new scope distinction on their own.

## 2. The layer and sunflower antecedents

Fomin, Golovach, Korhonen and Saurabh, *Stability in Graphs with Matroid Constraints*, SWAT 2024, Theorem 4, takes disjoint greedy independent layers and uses a bounded-conflict argument to obtain a $`k^2D`$-vertex reduction on conflict graphs of maximum degree $`D`$.

<https://drops.dagstuhl.de/storage/00lipics/lipics-vol294-swat2024/LIPIcs.SWAT.2024.22/LIPIcs.SWAT.2024.22.pdf>

The journal version appeared on 9 May 2026 in *Theory of Computing Systems* 70, Article 33; its bounded-degree layer result is Theorem 5. The theorem numbers above refer specifically to the SWAT 2024 version.

<https://link.springer.com/article/10.1007/s00224-026-10277-8>

SK uses that established layer mechanism inside a support sunflower. Its local petal-conflict bound applies even when the complete conflict graph has unbounded degree. The SWAT 2024 version's Theorem 2 contains the complement-pair product hidden family used in DR. DR's contribution is its exact encoding by disjoint weighted quota equalities and the root/target calibration, with a complete rank-program argument.

Erdős and Rado, *Intersection Theorems for Systems of Sets* (1960), supplies the sunflower framework. SK includes the constructive support induction. VS proves the more specific coefficient-consistent real-support induction needed for its numeric columns; an ordinary flower on row/value pairs is insufficient.

<https://www.renyi.hu/~p_erdos/1960-04.pdf>

## 3. Exact sparse quota algorithms have important existing endpoints

Huang and Ward, *FPT-Algorithms for the ell-Matchoid Problem with a Coverage Objective*, develops deterministic representatives for general oracle matchoids. Zero-one upper rows are uniform-matroid constraints on their incident items, so bounded selected cardinality and bounded incidence already have a representative-family FPT antecedent. General numeric lower/equality rows are not such independence systems.

<https://www.di.ens.fr/~cchuang/work/matchoid.pdf>

Van Bevern, Tsidulko and Zschoche, *Representative families for matroid intersections, with applications to location, packing, and covering problems*, full version v4, gives perfect-hash and matroid-intersection constructions, including an arbitrary-oracle facility setting. Its separate general packing theorem requires linear representations and a matroid on the union of packed resources; that is a different ground model from an arbitrary matroid on chosen items.

<https://arxiv.org/html/1806.11527v4>

A direct standard-framework deduction for unit-capacity packing hashes the resources touched by a size-$`k`$ solution, enumerates disjoint slot color patterns, and intersects the resource matroid with the slot partition matroid. This already yields a deterministic $`2^{O((\Delta+1)k\log((\Delta+1)k+2))}`$ exact endpoint. Consequently neither that order for matroid-constrained matching nor color coding itself is claimed new in BF or HP.

The full sparse model proved here additionally handles unequal nonnegative integer coefficients, mixed exact and lower targets, binary polymatroid counts, original-total completion, and arbitrary signed cost on quota-free coordinates. Its two complete proofs are stated with those precise interfaces. VS adds polynomial-time positive-capacity preprocessing to the same model.

## 4. Weighted rows and exactness are separate issues

Ahmadian and Friggstad, *Further Approximations for Demand Matching: Matroid Constraints and Minor-Closed Graphs*, ICALP 2017, studies unequal endpoint demands with an arbitrary matroid on edges. Its approximation and capacity-augmentation guarantees are a model antecedent, not the exact parameterized mixed-quota theorem proved here.

<https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ICALP.2017.55>

Eisenbrand, Rohwedder and Węgrzycki, *Sensitivity, Proximity and FPT Algorithms for Exact Matroid Problems*, arXiv:2404.03747v2, parameterizes vector-weight exact basis problems by row dimension and coefficient size. Column frequency does not bound the number of upper rows in BF/HP, so that theorem cannot be substituted without an additional reduction.

<https://arxiv.org/html/2404.03747v2>

Bérczi, Liu, Reis and Tarnawski, *Weighted Equitability and Matroid-Constrained Discrepancy*, arXiv:2608.13983v1, supplies a recent cost-preserving weighted sparse rounding baseline. It permits bounded discrepancy; U requires exact integer quotas. The two guarantees answer different questions.

<https://arxiv.org/html/2608.13983v1>

## 5. Valued completion and universal colorings

Husić, Loho, Smith and Végh, *On complete classes of valuated matroids*, TheoretiCS 3 (2024), Definition 1.1 and Theorem 2.9, gives weighted Rado/network induction. Frozen VZ establishes the exact minimum-cost sign convention and the compressed implementation needed by BF, LC, and VS. The public induction theorem does not authorize constructing an exponentially large binary-resource expansion as an algorithm.

<https://theoretics.episciences.org/14792/pdf>

Alon, Goldreich, Håstad and Peralta, *Simple Constructions of Almost k-wise Independent Random Variables*, Section 5, Construction 3 and Proposition 3, gives the powering small-bias family. Its Lemma 1 records the Fourier passage to prescribed patterns. After an invertible change of seed coordinates, this is exactly the trace family used in LC, not a new derandomization construction. LC's mathematical increment is its application to the short laminar ancestor/blocker certificate and completed-cost replacement.

<https://web.math.princeton.edu/~nalon/PDFS/aghp4.pdf>

## 6. Hidden-family and readable-program lower bounds

Doron-Arad, Kulik and Shachnai, *You (Almost) Can't Beat Brute Force for 3-Matroid Intersection*, arXiv:2412.02217v2, Section 3, provides the G-matroid hidden-family mechanism. Their *The Fine-Grained Complexity of Matroid Problems* provides the SAT-to-readable-oracle framework. DR explicitly defines its valid rank on every query size and its tuple-to-assignment decoder instead of assuming that an arbitrary hidden family already has a short description.

<https://arxiv.org/html/2412.02217v2>

<https://arxiv.org/html/2307.07773v2>

The unconditional query lower bound applies to black-box rank access. The ETH lower applies to polynomially encoded valid rank programs and charges their description length. Deterministic ETH and randomized ETH are separate assumptions. These distinctions remain explicit throughout U.

## 7. Bounded OpenAI catalogue check

The official OpenAI math overview was freshly opened and its matroid/kernel entries inspected; direct searches for the terms “laminar” and “quota” returned no text matches in that overview. The surfaced matroid entries concern other models, including prophet inequalities and infinite matroid intersection. Kernel word matches in unrelated mathematical senses are not algorithmic kernel competitors.

<https://github.com/openai/math/blob/main/overview.tex>

This is an overview-level observation. It is not a claim to have read every manuscript in the repository, not a guarantee that no equivalent theorem appears there, and not a correctness endorsement of every catalogue entry. The source-specific comparisons above provide the usable baseline evidence for this increment.

## 8. Claims supported by this comparison

U gives self-contained deterministic algorithms and candidate reductions in the models stated by its manuscripts. The clearest improvements over the preceding checkpoint are arbitrary sparse row geometry, the frequency-one sharp target boundary, the removal of the laminar exponent's logarithmic factor, and deterministic polynomial ground/positive-capacity preprocessing with original-context exchange.

The comparison does not support a first-ever deterministic-kernel claim, an optimum kernel degree, an improvement over every public randomized bound, a full-bit kernel for arbitrary oracles, or a theorem for unrestricted additional oracle matroids. Those stronger assertions are not made.
