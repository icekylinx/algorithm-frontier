# Component-sensitive exact numeric-target catalogues

**25 October 2026. Complete incremental proof corollary; root and independent full mathematical reviews passed.**

This note refines the count in
[row-overlap-density-numeric-target-refinement.md](row-overlap-density-numeric-target-refinement.md). Numeric coefficient
profiles factor over connected components of the row-support graph even
when the resource is one arbitrary global polymatroid. Resource recovery
is still one global integral-intersection problem.

The result combines three useful counts on a component: the ordinary
partition bound for a single row, the fixed-dimensional anisotropic
bound with its dimension constant written explicitly, and the
support-pattern bound. It can prove a substantially smaller exponent
than applying the total-target density estimate to the entire input.

## 1. Model and component parameters

Use the mixed nonnegative-integer target model of RD: one integral
polymatroid `F` on an explicit coordinate ground, optional integer vectors
in `P(F)` or mandatory vectors in the original base `B(F)`, binary ranks,
arbitrary rational scalar minimization or maximization, and numeric rows
with relations independently chosen from `{<=,=,>=}`. The scalar may be
signed and is separate from the target parameters.

Apply the reviewed zero-target and eligibility preprocessing. Optional
vectors use a free zero-row, zero-scalar disposal coordinate; mandatory
bases retain their original total. Assume every surviving coordinate is
positive in at most two target rows. The at most four charged local cover
copies from RD preserve the scalar and shared resource. Cover credits
range from their target through twice their target minus one.

Let `G` be the simple row-support graph, with one vertex per surviving
positive-target row and one edge for every positive two-row support.
For a connected component `C`, define

$$
d_C=|C|,\qquad T_C=\sum_{j\in C}T_j,\qquad
U_j=\begin{cases}T_j,&\rho_j\in\{\le,=\},\\
2T_j-1,&\rho_j=\ge,\end{cases}\qquad
U_C=\sum_{j\in C}U_j.
\tag{CP1}
$$

Let `m_C` be its number of interaction edges and `Q_C` the number of
actual nonempty exact support patterns of copied coefficient vectors
inside `C`. Local copying only deletes cover components, so

$$
T_C\le U_C\le2T_C,\qquad Q_C\le d_C+m_C\le T_C+m_C.
\tag{CP2}
$$

Every nonzero copied coefficient vector belongs to exactly one component.
All zero vectors, including passive copies and disposal, are retained in
one global zero group. No corresponding decomposition of `F` is assumed.

Define the anisotropic quantity and its explicit dimension constant by

$$
K_C=\max_{\varnothing\ne S\subseteq C}
       \left(\prod_{j\in S}U_j\right)^{1/(|S|+1)},
\qquad A_d=d+2(2^d-1).
\tag{CP3}
$$

For a component with a nonempty coefficient support, put

$$
B_C=\min\left\{
 \exp(A_{d_C}K_C),\quad
 2^{U_C}\binom{Q_C+U_C}{U_C}
\right\}.
\tag{CP4}
$$

If `Q_C=0`, put `B_C=1`: that component has only its empty nonzero
profile, and its row filters decide whether this profile is acceptable.

**Theorem.** Exact scalar optimization, including infeasibility reporting,
takes

$$
\boxed{\left(\prod_C B_C\right)\mathrm{poly}(H)}
\tag{CP5}
$$

time and polynomial binary workspace. The polynomial factor is uniform
in the number and sizes of the components. The exponential dependence
on a varying component dimension is explicitly present in `A_d`; it is
not hidden in an allegedly uniform constant.

For an isolated row, `K_C=sqrt(U_j)` and `A_1=3`, so its contribution is
at most `exp(3 sqrt(U_j))`. If all component dimensions are bounded by a
fixed constant `D`, the first alternative gives
`exp(O_D(sum_C K_C)) poly(H)`. If dimensions vary, CP4 retains the actual
`A_(d_C)` and can use the support-pattern alternative instead.

## 2. The component catalogue bounds

For a component `C`, consider all multiplicities of its actual nonzero
coefficient vectors satisfying the component upper allowances `U_j`.
Ignore the resource and global count cap for the moment. Write `P_C` for
the number of these profiles, including the empty profile.

The support-pattern argument from RD applies within `C`. If a profile
uses `h` support patterns, there are `binom(Q_C,h)` choices. Their
positive total entry weights summing to at most `U_C` have
`binom(U_C,h)` choices. For one exact support of fixed size, canonically
ordering its vector occurrences and concatenating their positive entries
injects its weight-`w` profiles into compositions of `w`; there are at
most `2^(w-1)` such profiles. Multiplying these bounds and summing gives

$$
P_C\le2^{U_C}\sum_h\binom{Q_C}{h}\binom{U_C}{h}
     =2^{U_C}\binom{Q_C+U_C}{U_C}.
\tag{CP6}
$$

For completeness, the other alternative has a dimension-explicit proof.
Count instead all multisets of arbitrary nonzero vectors in
`N^(d_C)` whose component sums are bounded by `U_j`. For positive
analysis parameters `t_j`, the multivariate generating function gives

$$
\log P_C\le \sum_{j\in C}t_jU_j
 +\sum_{\ell\ge1}\frac1\ell
   \left[\prod_{j\in C}(1-e^{-\ell t_j})^{-1}-1\right].
\tag{CP7}
$$

Using `(1-e^(-x))^(-1)<=1+1/x`, expanding the product, and
`sum_(ell>=1) ell^(-(|S|+1))<=2` for each nonempty `S`, we obtain

$$
\log P_C\le\sum_{j\in C}t_jU_j
      +2\sum_{\varnothing\ne S\subseteq C}
                        \prod_{j\in S}t_j^{-1}.
\tag{CP8}
$$

Set `t_j=K_C/U_j`. The first term is `d_C K_C`. By the definition of
`K_C`, every product in the second term is at most `K_C`. There are
`2^(d_C)-1` such products, proving

$$
P_C\le\exp(A_{d_C}K_C).
\tag{CP9}
$$

For one row this is exactly the ordinary cumulative-partition bound
`exp(3 sqrt(U_j))`. For larger components it retains the anisotropic
dependence rather than replacing the targets by their sum.

These are alternative analyses of the same catalogue, not separate
enumeration routines requiring a choice of parameters. Neither irrational
analysis parameters nor an exponentially large list of subsets is
computed by the algorithm. The minimum in CP4 therefore introduces no
unaccounted optimization or dimension-dependent enumeration overhead.

## 3. One global recovery and all-input traversal

Concatenate the lists of occupied nonzero vector classes from all
components. Traverse their count multiplicities depth first, maintaining
all component allowances and the global count cap

$$
\sum_{b\ne0}h_b\le R,
\tag{CP10}
$$

where `R` is the required total in the prepared base representation.
The zero-vector group gets the single remainder
`R-sum_(b!=0) h_b`. There is no guessed per-component resource total or
per-component zero remainder.

At each full profile, apply every exact upper, equality or credited-cover
filter. Intersect the shared copied resource with the partition-count
polymatroid of all classes, and require total `R`. Since the class caps
sum to `R`, the full-total face forces all caps to equality. This face is
integral, and optimizing the original scalar on it returns an integer
solution when the face is nonempty. Aggregation preserves resource
feasibility and scalar value; credited covers imply true covers.

The resource can couple coordinates from different components in any
way. It is neither restricted and solved separately on components nor
replaced by a direct sum. The only factorization used is the count of
candidate coefficient profiles before the shared resource test.

For the time bound, each partial count state has a zero completion on
all remaining nonzero classes satisfying all component upper allowances
and the global count cap. At a fixed depth distinct states have distinct
such completions. The complete upper-cap profiles form a subfamily of
the Cartesian product of the component catalogues. Thus, including
every final-filter and resource failure, the number of visited states is
at most occupied depth times `prod_C P_C`. CP6 and CP9 prove CP5.

The traversal stores only one binary count vector, its component sums,
the one global remainder, and one integral-intersection subproblem.
The local cover lift has at most four copies per original coordinate.
There is no stored catalogue, rank-sized unit expansion, or target-sized
array. These facts prove the uniform polynomial-space claim.

## 4. Useful readable consequences

Applying the density estimate separately on each nontrivial component
gives, with `I` the isolated rows,

$$
\exp\!\left(
 3\sum_{j\in I}\sqrt{U_j}
 +O\!\left(\sum_{C:\,d_C\ge2}
      T_C\log\left(2+\frac{m_C}{T_C}\right)\right)
\right)\mathrm{poly}(H).
\tag{CP11}
$$

The constant in this density `O` is universal. Every component may instead
use its explicit anisotropic alternative from CP4. Thus a large isolated
target incurs a square-root exponent, and a small fixed-dimensional
component can retain its own anisotropic exponent even if many unrelated
rows occur elsewhere in the input.

This improves the certified bound from combining all targets and all
interaction edges first. It does not assert that the earlier enumeration
must actually spend its coarser upper bound on every such instance.

The catalogue and shared-recovery argument itself applies to any explicit
prepared coefficient ground whose vectors lie inside the stated row
components. The support-two assumption supplies the reviewed uniform
polynomial-sized lift for arbitrary mixed covers. An unrestricted
subset-copy lift is not silently declared polynomial-space here.

## 5. A coupled family with a substantially smaller exponent

Let `k>=4` be even. Take a core of `k` rows with equality target one,
and one coordinate per edge of a complete graph on those rows, with its
endpoint-incidence coefficients. Its profile parameters satisfy
`T_core=U_core=k` and `m_core=binom(k,2)`.

Add one isolated row with scalar labels `1,...,n`, where `n=k^2`, on
`n` new coordinates. Let `r_0=n/2`, and choose a largest family
`H_0` of rank-`r_0` subsets of these labels with the same sum `alpha`.
Use equality target `alpha` for the isolated row. Elementary bounds give

$$
\alpha=\Theta(n^2)=\Theta(k^4),\qquad
|H_0|\ge\frac{2^n}{(n+1)n^2}
       =\exp(\Omega(k^2)).
\tag{CP12}
$$

The ground has polynomial size in `k`; the largest class and its target
can also be found by the ordinary cardinality/sum counting DP. The
combined target sum is `T=alpha+k=Theta(k^4)` and the total interaction
edge count is `Theta(k^2)`. Applying the coarser total-target density
bound gives `exp(O(T))`. In contrast CP5 gives

$$
\exp\!\left(O\left(k\log k+\sqrt\alpha\right)\right)
       \mathrm{poly}(H)
   =\exp(O(\sqrt T))\mathrm{poly}(H).
\tag{CP13}
$$

There is a matching-order oracle family with a single globally coupled
resource. Let `H_core` be all perfect matchings of the core, and let

$$
\mathcal H=\{A_{\rm core}\mathbin{\dot\cup}A_0:
       A_{\rm core}\in H_{\rm core},\ A_0\in H_0\},
\qquad r=k/2+r_0.
\tag{CP14}
$$

All members of this family have rank size `r` and the same full row-sum
vector. No two are one-exchange neighbors, since every coordinate has a
different full coefficient vector. Declare all sets smaller than `r`
independent and all rank-sized sets outside `H` bases. This is the valid
reference paving matroid; a hidden instance also admits one member
`A in H`. The standard two-augmentation argument proves validity, and
the rank oracles differ only on the hidden query.

On bases, the core equalities force a perfect matching, after which the
global cardinality forces exactly `r_0` isolated-row elements. Its sum
constraint then forces membership in `H_0`. Thus the reference problem
is infeasible and the hidden problem has its unique hidden feasible
base. The size of the hidden family is

$$
|\mathcal H|=(k-1)!!\,|H_0|
      =\exp(\Theta(k\log k+k^2)).
\tag{CP15}
$$

Consequently exact decision with bounded error at most one third requires
`|H|/3` worst-case rank queries by the balanced reference/hidden
distribution. This matches CP13 in exponent order along the family.
The resource is the single global paving matroid just constructed, not
the direct sum of separate core and isolated-row matroids. In particular,
its independence below rank does not impose the proposed component ranks
separately.

This lower statement is for the base subclass and general rank oracles.
It does not claim that the row graph describes a graphic resource or
that every prescribed component-target vector has a matching lower
bound. It demonstrates that the component-sensitive estimate is useful
even in the globally coupled resource model.

## 6. Attribution and relationship to the other increments

The profile-intersection method and the paving hiding framework have
public antecedents already recorded in the RD, MD and VT notes. This
increment concerns the component product, its dimension-explicit menu,
the all-input traversal accounting, and the coupled example. It makes
no first-use or publication-priority claim.

A separate actual-support multivariate potential may strengthen
the bounds within a connected component. CP5 does not reproduce that
potential or require a convex optimization routine: its catalogue bounds
are explicit expressions justified above. Any independently proved
smaller bound on a component's same catalogue can be substituted in the
product without changing the global resource recovery.
