# Checkpoint S — new support-sensitive exact algorithms and lower bounds

**Increment only; 25 October 2026.**

Parent: deterministic_related_problems_increment_20261025_R.zip.
Parent SHA-256: c5a0cacff1e0ab9283da4e6214d7f80ced7fc46cc3b15e5700dc9098bf7e3bf4.

This archive contains only manuscripts added after R. It does not repack R or the earlier full checkpoint Q. Proof dependencies from R are named below. No Lean, PDF, executable verification package, or duplicate internal review log is included.

## 1. Main new result: original support patterns, without an arity restriction

Consider one normalized monotone integral polymatroid on an explicit coordinate ground. Counts and ranks are binary encoded. The resource is either its independent region or its original-total base. There are nonnegative integer target rows, independently oriented as upper bounds, equalities, or covers, and one arbitrary signed rational scalar is optimized exactly.

Let T be the sum of the numeric targets. After the stated zero-target and eligibility preprocessing, let Q count the distinct nonempty sets of rows in which an original coordinate has a positive coefficient. Positive magnitudes can vary within one such support pattern. In particular, Q does not bound how many rows a coordinate may meet.

The new deterministic bound is

\[
 \boxed{
 2^{\,O(T\log(2+Q/T))}\operatorname{poly}(H)
 }
 \qquad(T>0),
\]

with polynomial binary workspace, uniformly in the row count and the column support size. For pure upper/equality rows there is the explicit profile bound

\[
 2^T\binom{Q+T}{T}\operatorname{poly}(H).
\]

Thus Q=O(T) removes the logarithm in the preceding unrestricted total-target exponent, even if a single coordinate participates in every row. The resource remains one arbitrary globally coupled polymatroid.

The proof is in [UP: unrestricted support patterns](unrestricted_support_pattern_numeric_targets.md).

### What makes unrestricted mixed covers work

Local subset copying would create exponentially many supports when a coordinate touches many cover rows. The new construction instead orders original support blocks. In a feasible witness, a unit is useful only while it reduces an unfinished integral covering demand. At most T_C such units are useful, where T_C is the total covering demand.

Within each support block the useful units form a prefix. Guess its binary length, and each cover row's first-reaching positive-occurrence ordinal. Only the stopping positions split a block. At most Q_C+s binary-length intervals are needed, where s is the number of cover rows.

One exact count row per interval controls its length. All coordinates assigned to that interval have one common auxiliary support. The resulting bounded-credit instance has at most 2Q+s support patterns and total upper allowance at most 3T. It is solved directly by the finite profile primitive, without another cover-marking wrapper.

All remaining original units use charged passive copies. Their resource use and scalar contributions are preserved. There is no enumeration of unit orders within an interval and no expansion of a binary resource count.

## 2. A sharp two-parameter worst-case classification

Dovetail the new algorithm with R's unrestricted total-target algorithm. Define, for positive integer budgets t and q,

\[
 f(t,q)=t\log_2\!\left(2+\min\left\{\frac qt,t\right\}\right).
\]

The per-instance upper bound is

\[
 2^{O(f(T,Q))}\operatorname{poly}(H)
\]

with polynomial space.

Conversely, for every sufficiently large target budget t and every support-pattern budget q>=1, there are instances with actual target sum at most t, actual pattern count at most q, and polynomial-size explicit coefficient data requiring

\[
 2^{\Omega(f(t,q))}
\]

rank queries. This lower statement permits bounded-error randomized decision. It is a worst-case classification under parameter upper budgets; it does not say that every exact pair of parameter values or every given support geometry is equally hard.

The proof is in [BC: budget classification](support_pattern_budget_complexity_classification.md).

Two constructions fill the full range.

- At q=1, positive hypercube labels and unions of complementary pairs give exponentially many nonadjacent equal-sum bases. Every coefficient is one or two, and every column has the same full support. The explicit ground is polynomial in T. This proves a 2^{Omega(T)} query lower bound at the single-pattern endpoint.
- At larger q, disjoint even cliques give perfect-matching families with Q proportional to T times the clique order. Their candidate count has logarithm of order T log(2+Q/T), up to the unrestricted T log T saturation.

The one-pattern proof is in [OS](one_support_pattern_target_lower_bounds.md). It also supplies a polynomial-size readable rank-program reduction showing that deterministic ETH excludes 2^{o(T)} poly(H) at this endpoint. Its row count and targets grow; it is not a fixed-dimensional lower bound.

## 3. Geometry and unequal targets can give much smaller exponents

The worst-case budget envelope deliberately forgets the actual geometry and distribution of targets. The following new bounds retain them.

| Structure | New exact upper estimate, times a polynomial input factor | Meaning |
|---|---|---|
| Each coordinate meets at most one numeric row | exp(3 sum_j sqrt(U_j)) <= exp(3T) | Mixed orientations, one exact signed scalar |
| Each coordinate meets at most two rows; m distinct interacting row pairs | exp(O(T log(2+m/T))) | Linear m gives a linear-in-T exponent, even for high-degree stars |
| Several row-support components | Product of the best component catalogue bounds | Only the profile catalogue factors; the resource stays global |
| Connected star, k unit-target leaves and center target B, no center-only positive columns | exp(O(k log(2+B/k))) | Covers allowed at the center; leaves are upper/equality rows |

Here U_j=T_j for an upper/equality row and U_j=2T_j-1 for a positive cover row.

The support-one/support-two boundary is proved in [CS](column_support_numeric_target_dichotomy.md), and the density refinement in [RD](row_overlap_density_numeric_target_refinement.md). Complete matching-order query families are included.

The component bound [CP](component_sensitive_numeric_target_catalogues.md) keeps all dimension constants explicit. Its globally coupled example has a dense small core and a large isolated target. It improves the certified total-target estimate from exp(O(T)) to exp(O(sqrt(T))), with a matching-order oracle family.

### The actual-support potential

On a prepared coefficient ground, let S be its actual nonempty support catalogue and U_j its finite row allowances. The number N of upper-cap profiles satisfies

\[
 \log N\le
 \inf_{t_j>0}
 \left\{
 \sum_jU_jt_j+
 2\sum_{A\in S}\prod_{j\in A}(e^{t_j}-1)^{-1}
 \right\}.
\]

This is dimension-uniform and convex in the analysis variables. The exact algorithm does not need to solve that convex minimization: every choice of positive t gives a valid analysis of the same streamed enumeration.

For the connected star, this potential yields the bound in the table. At B=k squared, total target T is of order k squared, and the time is exp(O(sqrt(T) log(T+2))). A composition family has a matching exponent order. Its polynomial ranking also gives the corresponding ETH lower bound for readable rank programs.

All details are in [SP: support potential and the star family](support_sensitive_partition_potential_and_star_targets.md).

## 4. Conditional computational lower bounds now accompany the oracle results

The new encoded reductions do not assume that the rank function is opaque. An algorithm may inspect the whole supplied rank program or circuit, including the formula data. Every produced program evaluates the full rank function in polynomial time and is proved to define a valid matroid for every formula.

| New encoded family | Exponent excluded under deterministic ETH |
|---|---|
| Fixed dimension d, balanced numeric equality targets | o(T^{d/(d+1)}) |
| Arbitrary dimension, unit targets | o(T log(T+2)) |
| Disjoint-clique density families | o(T log(2+m/T)), uniformly across the stated regimes |
| One full positive support pattern, coefficients one/two | o(T) |
| Connected star with center target k squared | o(sqrt(T) log(T+2)) |

The entries mean that a deterministic 2^{o(the displayed scale)} poly(H) algorithm is excluded in the specified rank-program/circuit model. They are not lower bounds for graphic matroids, explicit linear representations, or ordinary graph matching.

[FE](fixed_dimension_encoded_matroid_eth_lower.md) additionally transfers the square-root inverse-accuracy obstruction to all seven single-matroid variants under ETH. This is a new representation-level lower statement; it does not improve R's approximation upper bound or close its remaining accuracy gap.

[ET](conditional_lower_bound_encoded_target_matroids.md) gives the dense unit-target reduction. [ED](encoded_overlap_density_eth_lower_bound.md) supplies the uniform density tradeoff, product matching decoder, and zero-overlap endpoint. Randomized algorithms require randomized ETH separately; ordinary deterministic ETH is not used to exclude them.

## 5. Exact nonlinear transfer and a signed-scalar extension

The new density estimates extend through the compressed common-marginal-band representation:

- Convex nondecreasing target functions are upper-bounded.
- Concave nondecreasing target functions are lower-bounded.
- Equality rows remain linear.
- A convex scalar is minimized, or a concave scalar is maximized.

For this exact scalar optimization, marginal signs may be arbitrary. The repacking argument uses the order of the scalar marginals, and the linear primitive accepts signed rational weights.

The incidence and support parameters must be measured on the actual refined band columns. A single original coordinate can affect several functions even though different bands affect disjoint row groups. Counting only original function dependencies can therefore miss the useful sparsity.

[ND](aligned_nonlinear_overlap_density_transfer.md) proves the precise density adapter, signed-scalar extension, exact equality of optima, and the nonlinear-equality boundary. UP also gives the unrestricted-support interface with Q measured on eligible band columns.

## 6. Correctness and comparison boundaries

All included theorem manuscripts received a complete root review and a separate complete internal mathematical review. Those reviews are not formal verification or external peer review. The archive contains the proofs and source comparison, rather than the duplicate review logs.

The following conditions remain explicit throughout:

- A mandatory base keeps the original total after every genuine eligibility or domain restriction.
- Optional disposal is confined to the optional-vector model.
- A profile is recovered by one resource rank and one partition-count rank; no unproved intersection of three unrelated polymatroids is used.
- The scalar optimization is one functional. A threshold can concern that same scalar; another unrelated objective-plus-side-constraint pair is not silently added.
- Numeric row coefficients are nonnegative integers. Target sums are numeric parameters, not bit lengths or approximation accuracy.
- Binary counts, marginal lengths, and ranks are never expanded into unit lists.

The new source comparison is [incremental_primary_baselines_S.md](incremental_primary_baselines_S.md). It credits the established count-profile/intersection and paving/SAT-decoder antecedents, distinguishes recent additive-discrepancy results from exact target feasibility, and records the limited new OpenAI index check. It does not assert publication priority.

## 7. Dependencies on R

The preceding archive supplies the exact-profile intersection framework, the original unrestricted chain algorithm, the fixed-dimensional anisotropic estimate, and the compressed nonlinear band rank:

- fixed_dimensional_mixed_numeric_targets.md
- variable_dimension_total_target_classification.md
- mixed_target_cover_chain_compression.md
- compressed_nonlinear_marginal_band_transfers.md
- aligned_nonlinear_mixed_numeric_targets.md
- single_matroid_accuracy_lower_bound_audit.md

They are dependencies, not duplicated payload entries in this increment.
