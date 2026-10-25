# Independent audit of corank packing and cost-preserving common bases

**25 October 2026. Full independent mathematical review of E1--E9 and G1--G9.**

Reviewed manuscripts:

* `corank_packing_selection_oracle_extension.md`;
* `corank_degree_bounded_common_bases.md`.

Both arguments pass. The abstract theorem needs only an exact
restriction selector for a fixed-cardinality family and a separator
for nonnegative subset-capacity rows. Its cost-preserving application
to two exact matroids has the correct negative-cost treatment,
one-sided target search, implicit-row extension, and integer-capacity
boundary. The public comparison statements were freshly checked in
the two primary sources identified below.

## 1. The abstract proof uses no hidden matroid exchange property

Let B be any family of r-element subsets. At a current ground Q,
the selector either returns an allowed member inside Q or soundly
reports none. If one exists, d=|Q|-r is nonnegative. No closure,
exchange, or matroid property of B is needed after this point.

The query vector b*1_Q is tested against every original packing
row. If it is feasible, the selected I subseteq Q is also feasible
at quota b because all row coefficients are nonnegative. This is
downward closure of the packing region, not downward closure of B.
The fixed cardinality of B remains essential for the omission budget.

If a row A is violated, its intersection S=A intersection Q has
m=|S| and u_A<bm. Because u_A>=0 and t>b>0,

\[
        1\le\ell=m-\lfloor u_A/t\rfloor\le m.
\]

For any t-feasible member I* contained in Q, the same original
row gives |I* intersection S|<=floor(u_A/t). Thus I* omits at
least ell elements of S. Its total complement inside Q has size
d, so ell>d soundly rejects the stronger promise. Otherwise
some enumerated ell-subset D of S consists entirely of omitted
elements. The same I* belongs to B inside Q minus D, and the
exact selector cannot reject that branch. Induction proves the
failure implication.

Rational quotas cause no problem: floor(u_A/t) is computed exactly
from polynomial-bit numerators and denominators. Integrality is
used only for the cardinalities of selected sets and omission
batches, not for the values of t, b, or the capacities.

## 2. Full original rows and all attempted children are required

The argument correctly separates b*1_Q against the original full
row system. In a general set-packing system, discarding every row
not contained in Q would be invalid: a row meeting both Q and its
complement still constrains the selected coordinates in Q. The
manuscript instead uses S=A intersection Q only to calculate the
omission batch, retaining the original capacity u_A.

Let R=t/(t-b)>1. Violation implies

\[
                 \ell\ge m-u_A/t>m/R.
\]

The entropy bound binom(m,ell)<=Gamma(R)^ell follows as in the
independently audited batch theorem. The ell>d guard is tested
before enumeration, so m<Rd on every branching node, even when
the stronger promise is false.

Each attempted D is counted as a child. A selector rejection is
a terminal child of remaining budget d-ell. This charges all
enumeration and oracle work, including a node whose every attempted
deletion is rejected. The same induction bounds the augmented tree
by (c+1)Gamma(R)^c. The proof uses no promised solution in this
runtime estimate. Depth-first search, polynomial-delay subset
generation and polynomial-space oracles establish the space bound.

If r=0, the selector must first confirm that the empty member is
permitted; all nonnegative packing capacities then make it feasible.
If c=0, the only possible r-set is the full ground. Both boundaries
are explicitly separated in the manuscript.

## 3. Resource augmentation has exact set feasibility

Scale every capacity by 1+epsilon and choose t=1+epsilon, b=1.
An original-capacity member I obeys
t*1_I in the scaled packing region. A success is therefore an
exact member of B whose incidence vector obeys all augmented
capacities, while a failure proves original infeasibility.

The branch ratio is (1+epsilon)/epsilon. Capacity scaling can be
implemented by scaling the query vector for an original packing
separator; explicit rows and submodular-rank rows also admit the
direct separators described in the manuscripts. The separator must
support these exact rational query vectors, as stipulated by the
packing interface.

There is no cardinality approximation and no loss of membership in
B. The procedure only relaxes the capacities. In particular, it
does not invoke an exact t=b routine. This explains why the result
extends to a selector that itself enforces two exact matroids,
even though adding an exact third matroid would not be justified
by ordinary matroid intersection.

The explicit warning about integer unit-value optimization is
correct. That different wrapper needs an exact one-unit gate; a
common-basis selector for two matroids does not supply exact
feasibility in a third recipient Boolean matroid. The abstract
gap theorem alone does not remove that gate.

## 4. Negative rational costs are handled by a common fixed-rank shift

For the common-basis application, choose
K=max{0,-min_p w_p} and set w'_p=w_p+K. Every selected common
basis has exactly r elements, so

\[
                       w'(I)=w(I)+rK.
\]

The same constant shifts the optimum. Therefore proving
w'(I)<=OPT' proves w(I)<=OPT even when the original optimum is
negative. The shifted costs are nonnegative and have polynomial
binary length. This shift would not be valid without a common
cardinality, but the model fixes both matroid ranks to r.

For a threshold W, the permitted family B_W consists of common
bases with shifted cost at most W. On Q, weighted matroid
intersection finds a minimum-cost common independent set of
cardinality r, or proves no such set exists. Since both original
matroid ranks are r, a size-r common independent set is a basis
of both. Comparing its exact rational cost to W gives precisely
the required restriction selector for B_W.

The selector enforces the cost budget exactly, throughout all
branches. The cost row is not a packing capacity being augmented.
Thus every success has cost at most W and preserves both matroids
exactly. Every failure rules out an original-capacity basis with
cost at most W.

## 5. The omission calculation survives fractional capacities

For a violated augmented row, the target ratio cancels exactly:

\[
        \ell=|A_i\cap Q|-
          \left\lfloor\frac{(1+\epsilon)u_i}{1+\epsilon}\right\rfloor
            =|A_i\cap Q|-\lfloor u_i\rfloor.
\]

This is the necessary number of omissions for the original rational
upper bound, since row cardinalities are integers. The augmented
violation m>(1+epsilon)u_i implies
ell>m*epsilon/(1+epsilon), exactly the ratio used by Theorem G.

Capacity zero is also covered: a violated zero-capacity row has
ell=m, so the whole row intersection must be deleted. If m>d,
original feasibility is impossible. Otherwise the batch has only
one choice, consistent with the entropy bound at ell=m.

## 6. The minimization search proves a cost bound against integer OPT

Choose a common rational quantum gamma for the shifted costs.
All common-basis costs are grid values. Their nonnegativity makes
W_hi=sum_p w'_p an upper bound on the cost of every common basis.

The algorithm calls the gap procedure at W_hi. A failure soundly
proves that no original-capacity common basis exists, since none
could have cost above this universal upper bound. A success records
a valid augmented-capacity basis. When original capacities are
infeasible, success is still allowed; the algorithm never mistakes
it for an original-feasibility certificate.

The lower index -1 is certified impossible by nonnegative costs.
During bisection, a failed midpoint moves the lower endpoint and
a successful midpoint moves the upper endpoint with its actual
basis. If original OPT' is finite, every failed lower threshold
is strictly below OPT'. At adjacent integer indices U=L+1,
grid integrality gives gamma U<=OPT'. The saved basis has cost
at most gamma U, establishing the required cost inequality.

No monotonicity of algorithmic success is required. The lower
infeasibility implication is sufficient. All-zero shifted costs
give initial upper index zero and require no midpoint calls.
The r=0 case returns the empty common basis before this search.

After the cost shift is undone, the output satisfies the stated
original rational-cost comparison. It is a comparison with the
optimum integer basis under the original capacities; no LP-optimum
cost preservation is derived by this argument.

## 7. Implicit rows preserve every rank inequality

For an additional matroid N_j on a subset P_j, minimizing
(1+epsilon)r_(N_j)(S)-|Q intersection S| over S subseteq P_j
separates the augmented rank system. A negative minimizer returns
the original subset row S and its rank capacity. The same operation
works for an additional nonnegative recipient-polymatroid rank.

Checking all such rank systems costs polynomially many paid
submodular-minimization calls per node. Their number and overlaps
enter the polynomial input cost, not the exponent c. The output
satisfies the factor-1+epsilon inequality on every subset S,
not merely the total-rank constraint on P_j. The first two
matroids remain exact because they are enforced by the selector.

## 8. The exact bounded-integer-capacity endpoint is correctly limited

If every explicit capacity is an integer at most U_max, taking
epsilon=1/(U_max+1) gives

\[
                 u_i\le(1+\epsilon)u_i<u_i+1.
\]

Integer row counts then meet the original capacities exactly.
Every returned basis is an original-feasible basis of cost at most
OPT, hence actually optimal. Conversely, the initial failure is
an exact infeasibility conclusion. The ratio is R=U_max+2,
so time is Gamma(U_max+2)^c poly(H), within the stated
(O(U_max+2))^c bound.

For U_max=0, epsilon=1 works and zero rows can also be eliminated
directly before weighted matroid intersection. Rows with capacity
at least r are redundant for any r-element common basis. Removing
them is valid before calculating U_max.

This is a joint dependence on c and the numerical bound U_max.
The manuscript does not turn it into fixed-parameter exact
feasibility in c alone or suppress the numerical capacity from
the exponential factor.

## 9. Primary comparisons and final outcome

The following primary statements were freshly checked:

* Kiraly, Lau and Singh, [Degree Bounded Matroids and Submodular
  Flows, Theorem 2](https://www.microsoft.com/en-us/research/wp-content/uploads/2017/01/degree_matroids.pdf),
  preserves a basis of one matroid with cost no greater than the
  original optimum and upper-bound error at most Delta-1, where
  Delta measures element overlap in the listed constraints.
* Linhares, Olver, Swamy and Zenklusen, [Approximate Multi-matroid
  Intersection via Iterative Refinement, IPCO 2019, Theorem 2](https://ir.cwi.nl/pub/28684/Linhares2019_Chapter_ApproximateMulti-matroidInters.pdf),
  keeps a basis of one matroid and the LP weight guarantee while
  allowing integer multiplicative factors q_j in the others,
  subject to the stated reciprocal-overlap condition. Negating
  weights gives the corresponding minimization comparison.

The new application has two exact matroids, a common 1+epsilon
violation for all remaining rank systems, an integer-OPT cost
comparator, and parameterized time. These are distinct tradeoffs;
the manuscript makes no unsupported polynomial-time domination
or first-publication claim.

No gap was found in either manuscript. The full-row separator,
fixed-cardinality selector, rational floors, off-promise runtime,
negative-cost shift, cost-search orientation, and bounded-capacity
endpoint are all accounted for. This is independent internal
mathematical review, not formal verification or external peer review.
