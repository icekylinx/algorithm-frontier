# Root audit: exact compression of residual configuration cuts

**25 October 2026. Independent mathematical audit of the supplied derivation.**

The root reviewer read the complete C1--C10 derivation in
`recipient_polymatroid_subset_cut_compression.md`. The equivalence and
the stated enumeration costs pass this review. This is an internal
mathematical review, not a formal verification or an exhaustive novelty
determination.

## 1. Validity does not rely on the approximation algorithm

For an integral feasible recipient vector n and a fixed subset S, put
`m_p = f(S+p)-f(S)` and `A = {p : n_p > m_p}`. The chain

\[
n(A)\le f(A)\le f(S\cup A)
\le f(S)+\sum_{p\in A}m_p
\]

proves the hinge inequality directly. The last inequality is precisely
diminishing returns when the members of A outside S are inserted after
S; members already in S have marginal zero. Selecting configurations
for the chosen player basis therefore gives a feasible point of every
new subset cut. This is a valid relaxation of integer allocation.

## 2. The direction of the convexity argument is correct

For arbitrary nonnegative configuration weights, the violation

\[
F(z)=\sum_{p,n}\mu_{pn}(n_j-a_p(z))_+-z(P),\qquad
a_p(z)=\min_{T\ni p}(f(T)-z(T)),
\]

is a convex function of the feasible reserve z. Each hinge term is a
maximum of affine functions, and the last term is affine. A convex
combination of vertices consequently satisfies
`F(z) <= sum alpha_v F(v)`. Checking nonpositive violations at all
vertices is sufficient. The proof does not reverse Jensen's inequality
or assume the violation is submodular in the subset index.

## 3. Vertex reserves give exactly subset marginals

A greedy vertex supported on an ordered subset A has total f(A). Its
natural-matroid copy set is independent and has the full rank of the
union of all player blocks in A. It is therefore a basis of that union
and spans it. The number of further units available at p is exactly
`f(A+p)-f(A)`, and the reserve total on the right side is f(A).

Zero greedy increments cause no problem: the basis may have support
strictly smaller than A but still spans all of A's copy blocks.
Conversely, choosing a greedy basis of any subset S produces the
corresponding valid integral reserve. This proves both implications
of the full equivalence, rather than just domination of one cut family.

## 4. The support parameter is preserved

Restricting feasible reserves to a fixed coordinate set J produces
the polymatroid of the restricted rank function. Its vertices arise
from subsets of J. Hence reserves with at most s nonzero coordinates
need exactly the subset cuts with at most s elements. Conversely, the
greedy reserve of any such subset has at most s nonzero coordinates.

In particular, the completed-state reserve support bound `2(r-1)` in
the allocation proof transfers without a hidden numerical-capacity
factor. The same reasoning applies with `2(k-1)` when the actual
derived player rank is capped by k. This does not dispense with the
separate fat-deficit cap in the target search.

## 5. Computational interpretation and limitations

For an explicitly supported fractional configuration point, each cut
needs q+1 rank-value queries and a sum over its supplied support. Full
enumeration has `2^q poly(H, support)` cost. Enumeration of subsets of
size at most `2r-2` has XP cost `q^{O(r)} poly(H, support)`.

These bounds are independent of numerical capacities except through
their bit lengths. They do not give a rank-only fixed-parameter
separator, a polynomial-time separator, or an implicit-configuration
optimizer for arbitrary local families. The allocation algorithm's
stronger rank-parameter bound does not require solving this relaxation.

The ordinary aggregate resource inequalities are implied by the full
subset family: the S-cut contains all recipient mass on S, since its
inside marginals are zero, and has only nonnegative additional terms.
This implication need not hold if only small subsets are retained;
aggregate columns must remain in that weaker formulation when needed.

## Verdict

The exact equivalence, bounded-support equivalence, and explicit-point
separation bounds are accepted within their stated scope. No numerical
unit expansion, interchange of convexity directions, or implicit
pricing assumption was found.
