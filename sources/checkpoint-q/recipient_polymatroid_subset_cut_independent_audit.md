# Independent audit of subset compression for the residual configuration cuts

**25 October 2026. C1--C10 reviewed successfully.**

The reviewed manuscript is
`recipient_polymatroid_subset_cut_compression.md`. Its equivalence proof
removes numerical reserve-vector enumeration from the description and
explicit-point separation of the strengthened comparator. It does not
change the already audited allocation algorithm or establish an implicit
LP optimizer. This is an internal mathematical review, not external
peer review or formal verification.

## 1. The subset inequalities are valid directly

For fixed S, let m_p(S)=f(S union {p})-f(S). If n is a feasible integral
recipient vector, take A={p:n_p>m_p(S)}. Then

\[
 n(A)\le f(A)\le f(S\cup A)
                  \le f(S)+\sum_{p\in A}m_p(S).
\]

The final bound is diminishing returns, and remains valid for elements
already in S because their displayed marginal is zero. Subtraction
proves sum_p(n_p-m_p(S))_+<=f(S). Thus every integral allocation, and
every convex combination of them, satisfies the corresponding linear
configuration cut.

## 2. Convexity correctly reduces all reserve cuts to vertices

For real feasible z, individual residual capacity is the minimum of
the affine slacks f(T)-z(T) over sets containing p. Consequently

\[
 (n_j-a_p(z))_+
    =\max\{0,\max_{T\ni p}(n_j-f(T)+z(T))\}
\]

is convex in z. Nonnegative configuration masses preserve convexity
under summation, and subtracting z(P) is affine. The resulting violation
function F is therefore convex on the compact polymatroid P(f).

For any convex combination of vertices, F(z) is at most the same
combination of their F values. Thus all vertex inequalities imply every
feasible reserve inequality. This direction uses convexity with the
correct sign; it does not mistakenly minimize a convex function at
vertices. Integral f makes all vertices integral, so they belong to
the original reserve-cut index family.

## 3. A vertex's cut depends only on its greedy subset

Every vertex of an independent polymatroid is a greedy vector on an
ordered subset A: its positive-objective coordinates receive successive
rank differences and other coordinates receive zero. The usual greedy
optimization for every linear objective proves that these vectors
include all vertices. Zero rank increments cause no difficulty.

Such a vector is feasible, supported on A, and has total f(A). It is
therefore a basis of the natural-matroid union E_A of whole player
blocks. It spans E_A, regardless of the chosen order. For every player p,
its residual capacity is consequently

\[
                r(E_A\cup E_p)-r(E_A)
                         =f(A\cup\{p\})-f(A).
\]

Its right side is the total f(A). The vertex reserve cut is exactly the
subset cut indexed by A. Conversely, a greedy basis on any subset S
is an integral feasible reserve whose cut is that subset inequality.
This proves equivalence in both directions. No decomposition of f
into matroid rank functions is assumed.

## 4. The support restriction is preserved exactly

A reserve vector supported on J, |J|<=s, belongs to the coordinate
restriction of P(f) to J. Its vertices are greedy vectors on subsets
A of J. Applying the same convexity argument therefore uses only
subset cuts of size at most s. Conversely, a greedy basis of such an
A has at most s nonzero coordinates, so its cut belongs to the original
bounded-support family.

The two bounded families are thus exactly equivalent, not merely one
stronger than the other. At a completed normalized rank-r search state,
s=2(r-1) is sufficient by the existing record-count argument. The
fat-reduction preservation proof still applies because all cut
coefficients are nonnegative. A deficit parameter k uses s=2(k-1)
when k>=1; if k=0, no small-player search is needed.

## 5. The stated explicit separation cost is accurate

For fixed S, its marginal coefficients require only f(S) and the q
values f(S union {p}). Given an explicit list of configuration variables
and rational masses, the left side is then evaluated by polynomial
arithmetic in that explicit representation. Submodular minimization and
numerical capacity enumeration are unnecessary for this particular cut.

Enumerating all subsets gives a 2^q explicit separation bound. Enumerating
subsets of size at most 2(r-1) gives q^{O(r)} times polynomial explicit-
support work, with numerical capacities entering only through their
binary arithmetic. This is an XP bound in r, not an f(r)poly(q) bound.
The manuscript correctly separates it from the allocation algorithm's
rank-quasipolynomial guarantee.

The available-count oracle optimizes common intrinsic value under
coordinate caps. It need not price configurations under arbitrary dual
weights and hinge penalties from these cuts. Therefore explicit-point
separation alone does not supply a full implicit LP optimizer. The
manuscript preserves this limitation rather than charging such work
to an oracle that was never assumed.

## 6. Compatibility with the earlier examples

For the aggregate rank-gap example, S={a} has rank D+1, zero marginal
at a and marginal one elsewhere, reproducing the previously verified
support-one violated cut. For a scaled matroid type c r_R, the earlier
fractional-loss lemma and hinge inequality imply all residual cuts;
equivalence consequently implies all subset cuts are redundant in that
component model. The compression neither weakens that established
special-case result nor reintroduces the false aggregate comparator.
