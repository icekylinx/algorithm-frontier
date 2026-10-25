# Checkpoint U — sparse exact quotas and deterministic ground kernels

**25 October 2026. Increment only after checkpoint T. English research checkpoint.**

This archive contains eight new mathematical manuscripts and three new editorial/source documents. It contains no earlier manuscript, earlier archive, executable, formal-verification bundle, PDF, or internal review log. Frozen checkpoint T is an external dependency where named. The original matching-exponent project is not reopened.

The new results have complete manuscript-level proofs and independent internal review. This is not formal verification, external peer review, or a publication-priority certificate. The public ingredients and closest checked model-specific baselines are credited in the manuscripts and the new source note.

## 1. Main increments

| Increment | New guarantee | Model restrictions that remain essential |
|---|---|---|
| Sparse mixed numeric quotas, two proofs | Deterministic time \(2^{O(\Delta B_0\log(\Delta B_0B+2))}\operatorname{poly}(H)\), polynomial binary space | One integral-polymatroid resource; nonnegative integer rows; every quota-active coordinate has positive root charge; one exact signed scalar |
| Sharp disjoint-row lower bound | \(2^{\Omega(B\log B)}\) rank-oracle lower bound already at frequency one; matching deterministic ETH time barrier for readable rank programs | Disjoint weighted equalities, \(B=B_0+1\); pure feasibility, optional or mandatory resource |
| Laminar exponent refinement | \(2^{O(B^2)}\operatorname{poly}(H)\), explicitly \(2^{4B^2+O(B\log(B+1))}\operatorname{poly}(H)\) | Common nonnegative weights, laminar mixed rows, root cap \(B\), arbitrary true zero-coordinate costs |
| Sparse zero-one packing kernel | \(O_\delta(k^{2\delta+1})\) retained items; \(O_\delta(k^{2\delta})\) for distinct supports | One arbitrary item matroid, upper packing, at most \(k\) items, column frequency \(\delta\) |
| Several coverable matroids | \(k d![k(1+\sum_i g_i)]^d\) retained items | One arbitrary matroid and \(d\) additional matroids satisfying the stated original-closure class bound |
| Explicit transversal systems | \(O_d(k^{2d+1})\) retained original items, with uniform polynomial preprocessing even for variable \(d\) | One arbitrary matroid and \(d\) explicitly represented transversal matroids |
| Sparse numeric positive-capacity kernel | Total retained positive capacity \((\Delta B_0B+2)^{O(\Delta)}\), constructed in uniform polynomial time | Same root-charged model as the sparse time theorem; all zero coordinates and the original completion oracle remain available |

In the sparse numeric rows, \(B_0\) is the distinguished root cap, \(B\) bounds it and every finite target, and \(\Delta\ge1\) bounds nonroot positive incidences per column. An original equality/interval is counted once; an upper/lower split changes frequency by at most a factor two. In the ordinary packing and matroid kernels, \(k\) bounds selected cardinality. The symbols \(d\) and \(\delta\) in the table belong to their respective models, not to one universal parameterization.

## 2. Arbitrary overlap, unequal coefficients, and exact completion

The sparse theorem drops the laminar geometry of T. Nonroot rows may overlap arbitrarily and have different nonnegative integer coefficients at different rows. It keeps both lower and upper requirements, including equalities, and exact optimization of one arbitrary signed rational scalar. Binary resource totals are not expanded.

The valued proof, BF, preserves the full optimum cost of completing a protected positive set to the original resource total. Its hash catalogue separates all relevant upper-row IDs and bounds admissible replacement coefficients. The direct proof, HP, instead hashes rows, sums coefficients within each color, enumerates feasible numeric type counts, and solves one shared-resource/partition problem. HP avoids both positive-unit expansion and the valuated-matroid theorem. These are two complete proofs of the same full model, not an unproved reduction between them.

The root-zero condition is substantive: a coordinate of zero root charge must be zero in every other numeric row. Its scalar cost may still be arbitrary. Without that condition the proposed root-only parameterization has an oracle obstruction, recorded in BF. Both proofs retain the original mandatory total after masks; optional use is handled by a zero-scalar disposal coordinate.

## 3. A sharp frequency-one boundary

DR uses \(d\) disjoint blocks, root cardinality cap \(2d\), and one weighted equality of target \(2d+1\) in each block. Each block needs at least two selected items. The root forces exactly two, and the equality forces a complementary pair. There are exactly \(d^d\) numeric-feasible choices.

These choices form a one-exchange-stable family of rank-sized sets. A valid sparse-paving resource hides one of them, so an exact decision procedure must discover the hidden choice. The numeric constraints force full cardinality even for an optional independent-set instance; no scalar objective or additional cardinality equality is used.

The companion readable-rank construction decodes a Boolean assignment from the pair tuple, giving the deterministic ETH calibration \(B\log B=\Theta(\nu)\). The unconditional oracle lower bound and the representation-dependent ETH statement are distinct claims. The underlying hidden-family and SAT-decoder methods are publicly established; the new note supplies the exact disjoint-row/root-target realization.

Together with BF or HP, this closes the worst-case exponent order for fixed positive frequency and \(B_0=\Theta(B)\). It does not prove optimal dependence on variable frequency or on every joint choice of \(B_0,B\).

## 4. Laminar time improvement

LC improves T's arbitrary-completion-cost laminar theorem by replacing the recursive blocker catalogue with universal two-color pools. A protected replacement needs the ancestors of its removed unit green and the maximal disjoint blocking nodes red. Only \(O(B)\) node IDs require prescribed colors.

Polynomial-remainder hashing and the classical AGHP powering construction provide the required family. The full-cost overlap oracle then supplies a safe nonworse replacement. Enumerating at most \(B\) emitted positions yields the displayed quadratic parameter exponent, with a separate binary-large-cap branch preserving polynomial space.

The small-bias construction and Fourier conversion are explicitly credited to their public antecedents. The improvement is their application to the bounded laminar certificate and completed-cost interface. The previous exponential lower bound remains smaller; no optimality conclusion for the quadratic exponent is claimed.

## 5. Deterministic candidate reduction

SK establishes a strong original-context exchange guarantee: for every original feasible \(S\) and every \(e\in S\), a retained \(f\notin S-e\) can replace \(e\) without decreasing its signed profit. The rest of \(S\) may contain items removed much earlier.

The proof first thins identical supports, then finds a support sunflower and takes disjoint greedy layers from it. The original context touches only a bounded number of petal rows, leaving a safe resource-valid replacement. Each deletion preserves that external-context invariant, so reductions compose.

An immediate graph specialization is a deterministic \(O(k^4)\)-edge ground for matching, or vertex-capacitated \(b\)-matching, in a loopless simple general graph with an arbitrary matroid on its edges. Parallel edges give the general \(O(k^5)\) bound. The graph need not be bipartite. The resource matroid is on selectable edges, not on the union of their endpoints.

CK uses original parallel-class IDs as features for several additional coverable matroids. It obtains \(O_d(k^{3d+1})\) for \(d\) graphic matroids and \(O_d(k^{2d+1})\) for \(d\) cographic matroids, together with the arbitrary resource. The one-additional-matroid endpoint agrees with the cited public deterministic bound and is not a new endpoint claim.

TR uses the public matching-witness lift for explicit transversal matroids. A new implementation argument retains any \(k\) neighbors per left item, preserving every matching on at most \(k\) left items by Hall's criterion. If the original ground is already below the kernel bound, it is returned immediately. Otherwise the product of all truncated witness choices has fewer than \(n^2\) tuples. The lifted resource is a parallel extension, ensuring that projection of a replacement cannot duplicate an unchanged original owner.

These are oracle **ground** kernels. The original oracles and profit encodings remain accessible. Their deterministic guarantees have larger polynomial degrees than the checked public randomized kernels in common special cases.

## 6. Numeric coefficients and binary positive-capacity reduction

VS replaces ordinary greedy exchange by the full-cost valuation overlap lemma. Its sunflower is a sunflower of real row supports whose coefficients agree on the common core. A sunflower merely on \((\text{row},\text{value})\) labels would not justify the proof: two different values of the same real row would falsely appear disjoint.

Within one replacement class, more than
\(\delta![A_0(L-1)]^\delta\) distinct numeric columns force the required coefficient-consistent flower. The constructive induction follows one popular actual row/value pair and never enumerates all values up to binary \(A_0\). Disjoint overlap layers then preserve feasibility and full valuation against every original context.

For the root-cap application, large \(B_0\) does not trigger a unit expansion: if \(B_0\ge n\), all binary positive caps together are already at most \(B_0^2\). Otherwise there are fewer than \(n^2\) positive copies and fewer than \(n\) cardinality domains. Their kernels are united and identical-owner copies are merged back into binary caps. All quota-free coordinates and their exact optimal completion remain in the original oracle.

This is stronger preprocessing than the earlier FPT time statement, but it is not a full-input bit kernel and it does not improve the sparse theorem's exponential order. The result preserves the specified scalar objective, rather than every possible later change of objective.

## 7. Dependencies and unresolved boundaries

Frozen T contributes the completed-cost valuation and compressed two-rank oracle from `laminar_valuated_zero_completion_fpt.md`, and the prepared laminar geometry where LC cites it. Their files are not duplicated here. The current archive includes both full new sparse proofs, the sharper lower construction, and all new kernel proofs.

Open questions left by this increment include the laminar quadratic-exponent gap, smaller deterministic kernel degrees, mixtures of additional-matroid systems outside the stated adapters, and deterministic laminar-matroid ground kernels beyond the sparse-feature formulation. CK already allows heterogeneous collections of matroids satisfying its closure-class hypothesis. No broader mixture is silently asserted. Subsequent work will be recorded in separate increments.
