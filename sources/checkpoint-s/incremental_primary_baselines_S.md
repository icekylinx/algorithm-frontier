# Incremental primary-source checks for checkpoint S

**Checked 25 October 2026.** This note records the comparison needed for the new support-pattern, density, and encoded-input results. It does not reproduce R's general baseline review and does not establish publication priority.

## 1. Coefficient-profile intersection is an antecedent

Eisenbrand, Rohwedder and Węgrzycki, *Sensitivity, Proximity and FPT Algorithms for Exact Matroid Problems*, arXiv:2404.03747v2:

https://arxiv.org/html/2404.03747v2

The introduction explicitly describes guessing multiplicities of distinct weight vectors and enforcing those counts through partition-matroid intersection. The paper's parameterized result concerns coefficient magnitude and dimension.

S therefore does not claim to invent coefficient-profile intersection. Its new proved parts are the support-sensitive counts, the useful-prefix/interval construction preserving the ORIGINAL support-pattern parameter for arbitrary mixed covers, the geometry-sensitive analysis, and the stated target calibrations of the lower families.

The number of positive supports is different from the number of distinct coefficient vectors. It can remain one while many different full positive vectors occur.

## 2. The hard intersection subclass already has a public antecedent

Doron-Arad, Kulik and Shachnai, *You (Almost) Can't Beat Brute Force for 3-Matroid Intersection*, arXiv:2412.02217v2:

https://arxiv.org/html/2412.02217v2

The full text's Section 1.3 explicitly combines one paving matroid with partition matroids. Section 3 permits selected balanced subsets through its G-matroid construction. These are direct antecedents for hiding a constrained candidate family in a resource matroid.

Thus even the broad special case of one arbitrary resource with partition-style constraints is not presented as a newly discovered hard setting. The manuscripts in S prove their concrete support/target parameters, explicit candidate ranking, and representation-specific computational statements.

## 3. SAT-encoded matroid decoders are also prior

Doron-Arad, Kulik and Shachnai, *Lower Bounds for Matroid Optimization Problems with a Linear Constraint*, full version arXiv:2307.07773v2:

https://arxiv.org/html/2307.07773v2

Section 4 already defines efficiently decoded SAT matroids. S credits this construction principle. Its new complete reductions show the relevant parameter relations and give all rank-query branches, including subsets larger than the prescribed rank.

The same full version's Section 5 announces a quantitative inverse-error quarter-power exponential observation. R already corrected its baseline to include that observation. S adds an encoded-model square-root inverse-accuracy consequence; it does not present the public record as merely qualitative.

## 4. Existing rank-FPT and kernel results are not new consequences

Huang and Ward, *FPT-Algorithms for the ell-Matchoid Problem with a Coverage Objective*, arXiv:2011.06268v3:

https://arxiv.org/pdf/2011.06268

Theorem 3.7 gives a deterministic weighted representative kernel with size bounded by a geometric sum in the matchoid participation and rank parameters, under independence-oracle access.

Huang, Kakimura, Kobayashi and Terao, *Polynomial Kernels with Reachability for Weighted d-Matroid Intersection*, arXiv:2603.17345v1:

https://arxiv.org/html/2603.17345v1

This primary paper gives randomized polynomial kernels for several cases with one arbitrary matroid and other structured matroids, including partition and transversal cases. These results preclude treating the mere existence of rank-parameterized algorithms in those settings as a new discovery.

S instead states the total numeric target and original support-pattern parameters, arbitrary binary capacities in one integral polymatroid, exact mixed inequalities, and its own deterministic polynomial-space implementation. Model and parameter changes are kept explicit.

## 5. Recent column-sparsity rounding permits additive violations

Bérczi, Liu, Reis and Tarnawski, *Weighted Equitability and Matroid-Constrained Discrepancy*, arXiv:2608.13983v1:

https://arxiv.org/html/2608.13983v1

The paper proves cost-preserving rounding of a fractional matroid basis with additive row error controlled by column sparsity and the largest matrix entry. It also studies weighted prefix discrepancy and proves a logarithmic discrepancy guarantee.

These are relevant current primary results, but their stated additive allowances do not certify the exact integer target constraints required in S. Conversely, S's parameterized exact algorithms do not prove a polynomial-time constant-discrepancy conjecture or a general identical-machine matroid-partition PTAS.

The resource distinction matters: assigning each original job once while imposing a separate matroid on each machine can require more than the single resource rank used here.

## 6. ETH is a computational hypothesis, not an oracle convention

Impagliazzo, Paturi and Zane, *Which Problems Have Strongly Exponential Complexity?*, Journal of Computer and System Sciences 63 (2001), 512–530:

https://courses.cs.washington.edu/courses/cse599i/24sp/papers/ImpagliazzoPaturiZane_2001_jcss.pdf

The reductions in S use the deterministic variable-count assumption that 3-SAT has no deterministic subexponential-time algorithm with a polynomial formula-length factor. Their rank circuits and all numerical descriptions are produced in polynomial time.

An algorithm is allowed to inspect the circuit and its embedded formula. The SAT reduction supplies the computational obstruction. Bounded-error randomized algorithms need the randomized version of the assumption separately.

## 7. Bounded new OpenAI index check

The public OpenAI mathematics manuscript index was opened at:

https://raw.githubusercontent.com/openai/math/main/CONTENTS.md

The retrieved version displayed 719 manuscripts covering 372 result families. Literal find checks for the phrases “support pattern”, “column sparsity”, “numeric target”, and “overlap density” returned no matching index text.

This is only a bounded check of that index text. It is not a search of every manuscript body, a claim about private OpenAI research, or proof that an equivalent theorem is absent under different terminology. The proofs in S stand on their explicit arguments and the stated primary antecedents, rather than an unqualified absence claim.

## 8. Interpretation of the new comparisons

The strongest internal improvement is now available for arbitrary mixed rows without a column-arity restriction: Q=O(T) gives a linear-in-T exponent instead of the earlier unrestricted T log T summary. The one-support lower family shows that this linear exponent is already necessary in the general oracle model when dimension grows.

The geometry-sensitive potential and component catalogue bounds can be much smaller than that worst-case envelope on specified inputs. Matching lower constructions are carefully labeled either as a parameter-budget worst case or as a particular family; they are not claims about every exact target vector or every explicit resource representation.

Nothing in these checks settles publication priority. They establish a current, bounded comparison and prevent several stronger but unsupported interpretations.
