# Independent audit of corank packing and cost-preserving common bases

**25 October 2026. Fresh mathematical and primary-source audit.**

This note independently reviews `corank_packing_selection_oracle_extension.md`
(E1--E9) and `corank_degree_bounded_common_bases.md` (G1--G9). The positive
results pass the review below. The conclusion is an internal proof review,
not external peer review or a claim that the result has no prior analogue.

## 1. The selector abstraction is sufficient

Fix any family of sets of cardinality r with a polynomial restriction
selection oracle. At a current available ground Q, the oracle either
provides a permitted r-set contained in Q or rules out every such set.
Neither exchange properties nor hereditary closure of the family is used.

The packing constraints remain those of the original instance. If a row A
with capacity u_A is violated by b times the indicator of Q, put
S=A intersect Q and m=|S|. Since t>b>0 and u_A<bm, the integer

    ell = m - floor(u_A/t)

satisfies 1<=ell<=m. Every promised selected set I contained in Q has
t|I intersect S|<=u_A and consequently omits at least ell members of S.
If ell>|Q|-r, no promised set can remain. Otherwise, one of the enumerated
ell-subsets D of S is disjoint from a fixed promised I. On that child Q\D,
both the selector and the packing promise retain the same witness.

This proves the induction behind the gap procedure for arbitrary rational
quotas and capacities. A successful feasible b-indicator of Q also makes
every selected subset of Q feasible, by nonnegative packing coefficients.
The zero-rank case is correctly handled by testing the empty selected set.

It is essential that the separator sees all original rows. Restricting the
row list to rows contained in Q would be invalid for a general set system.
The manuscript uses the original rows and only intersects a returned row
with Q in the omission calculation, so it avoids this issue.

## 2. The single-exponential accounting survives the abstraction

For R=t/(t-b)>1, strict violation gives ell>m/R. The binomial bound from
the batch theorem therefore yields

    binom(m,ell) <= Gamma(R)^ell,
    Gamma(R) = R^R/(R-1)^(R-1).

Each attempted deletion child has remaining omission budget d-ell, where
d=|Q|-r. This includes children immediately rejected by the selector. Thus
the full attempted computation tree, rather than merely the successful
subtree, has at most (d+1)Gamma(R)^d nodes by induction. Polynomial work
per node gives the advertised running time; depth-first iteration over
combinations uses polynomial workspace.

No matroid-specific work is hidden inside the entropy estimate. The only
paid structural operations are the selector and the packing separator.
The capacities and exact rational floor calculations have polynomial bit
length. In particular, this is not an expansion into numerical units.

## 3. Resource augmentation and its feasibility semantics

With capacities multiplied by 1+epsilon and quotas t=1+epsilon, b=1,
every original-capacity solution is a promised solution. The output is
an exact allowed r-set whose original row loads satisfy the inflated
capacities. Failure implies that no original-capacity selected set exists.
Success does not certify original feasibility, as the manuscripts state.

The same reasoning allows implicit submodular rank rows, separated by
minimizing the scaled rank minus the indicator load. It also allows an
arbitrary fixed-cardinality family whose restriction oracle is polynomial.
Two common-basis matroids supply such an oracle through matroid
intersection. This does not supply an exact one-unit oracle for an extra
third matroid. The explicit warning against importing the integer
factor-two optimization wrapper is therefore necessary and correct.

## 4. Cost thresholds preserve the selector interface

For two rank-r matroids, a threshold W restricts the allowed family to
common bases with cost at most W. Weighted matroid intersection on Q
finds its cheapest cardinality-r common independent set. Comparing that
cost with W implements the exact restriction selector; no approximate
cost oracle is used.

Adding a common constant to each element cost adds the same constant
times r to every selected-set cost. Making all costs nonnegative is
therefore harmless, even when the original costs have either sign.
The final inequality translates back without change.

At a violated augmented row, the forced omission number simplifies to
|S|-floor(u_A), because both its capacity and the promise quota contain
the same factor 1+epsilon. This simplification does not weaken the
entropy ratio or change the guarantee.

## 5. The one-sided minimization search is correctly oriented

The sum of all shifted nonnegative costs is a known upper bound on every
common-basis cost. A target failure there proves original infeasibility;
a success gives a saved augmented-feasible basis. The lower grid index
-1 is an external infeasibility certificate because all shifted costs
are nonnegative.

On each trial, success lowers the upper endpoint and saves a basis whose
actual cost is at most that endpoint. Failure raises the lower endpoint
and certifies that every original-capacity feasible basis costs more.
When the endpoints become adjacent, the upper endpoint is at most the
integer-grid original optimum. Hence the saved basis costs at most that
optimum. This reasoning never assumes monotonicity of algorithmic
success and remains valid when the algorithm succeeds below the
original optimum by using its allowed capacity augmentation.

The zero-cost and empty-basis boundaries are explicitly handled. The
number of trials depends on the binary length of the cost range, not its
numerical magnitude.

## 6. Additional rank systems and bounded-capacity exactness

For every additional matroid, the guarantee is imposed on all of its
rank inequalities. A submodular minimization call separates the complete
scaled family; checking only its total-ground rank would not suffice.
Overlaps and the number of these additional matroids enter the polynomial
oracle work. The two primary matroids remain exact throughout.

For integer explicit capacities bounded by U_max, choosing
epsilon=1/(U_max+1) gives

    u_A <= (1+epsilon)u_A < u_A+1.

An integral selected set satisfying the augmented upper bound then
satisfies the original bound exactly. Any returned set is originally
feasible, and its cost at most original OPT makes it an exact optimum.
The resulting (O(U_max+2))^c running time keeps the maximum-capacity
dependence explicit. This does not imply an exact FPT algorithm in c
alone. Zero capacities and redundant capacities at least r cause no
exception.

## 7. Independent check of the two cited public comparisons

I opened the primary hosted texts on 25 October 2026.

* Kiraly, Lau and Singh, *Degree Bounded Matroids and Submodular Flows*,
  IPCO 2008, Theorem 2: for one matroid with upper subset bounds, a
  polynomial algorithm preserves the integer-optimum cost comparison
  and adds at most Delta-1 to each bound, where Delta is maximum listed
  set membership of an element. This agrees with the common-bases note.
  [Primary text](https://www.microsoft.com/en-us/research/wp-content/uploads/2017/01/degree_matroids.pdf).
* Linhares, Olver, Swamy and Zenklusen, *Approximate Multi-matroid
  Intersection via Iterative Refinement*, IPCO 2019, Theorem 2: the
  output preserves one distinguished matroid basis and the LP objective,
  while the other matroid rank systems are violated by specified integer
  factors q_i whose reciprocal overlap sum is at most one. This agrees
  with the stated comparison, including its stronger LP objective
  benchmark and different tradeoff.
  [Primary text](https://ir.cwi.nl/pub/28684/Linhares2019_Chapter_ApproximateMulti-matroidInters.pdf).

The new corank theorem preserves two exact matroids and permits a common
1+epsilon multiplicative violation in parameterized time, with cost
comparison against integer OPT. Neither of the cited polynomial results
is being presented as uniformly dominated. These source checks establish
the stated comparison, not exhaustive novelty of the parameterization.

## 8. Audit conclusion

The selector extension and minimum-cost common-bases application are
mathematically consistent with the accepted batched omission theorem.
Their scopes, feasibility semantics, numerical costs, and comparator
distinctions are correctly recorded. I found no substantive proof gap in
E1--E9 or G1--G9.
