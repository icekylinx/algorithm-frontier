# Minimum-cost common bases with degree capacities: a corank augmentation scheme

**25 October 2026. Concrete application of the generic packing theorem;
independent audit requested. No priority claim.**

This note applies [corank-packing-selection-oracle-extension.md](corank-packing-selection-oracle-extension.md) to
minimum-cost common bases of two arbitrary oracle matroids with
additional subset-capacity constraints. The selected set remains an
exact common basis, its cost does not exceed the original constrained
optimum, and each upper capacity is multiplied by at most
1+epsilon. The algorithm has single-exponential parameter dependence
on the common-basis corank and the requested accuracy.

## 1. Model and theorem

Let M_1 and M_2 be matroids of common rank r on a q-element ground
set P, given by independence or rank oracles. Let w_p be rational
costs. Let A_i subseteq P and u_i>=0 be rational upper capacities,
initially given as an explicit list. The original problem is

$$
\begin{array}{ll}
 \text{minimize}&w(I)=\sum_{p\in I}w_p,\\
 \text{subject to}&I\text{ is a basis of both }M_1\text{ and }M_2,\\
                  &|I\cap A_i|\le u_i\quad\text{for every }i.
 \end{array}
 \tag{G1}
$$

Its optimum, when feasible, is OPT. Put c=q-r. Elements known to
belong to no common basis may be removed first, reducing q and c;
the theorem does not require that preprocessing. H contains the
original ground set, listed subsets, all numerical bits, and the
paid oracle costs.

**Theorem G.** For any rational epsilon>0, if (G1) is feasible,
there is a deterministic algorithm returning a common basis I with

$$
w(I)\le\mathrm{OPT},\qquad
             |I\cap A_i|\le(1+\epsilon)u_i
                                      \quad\text{for every }i,
 \tag{G2}
$$

in time

$$
\Gamma\!\left(\frac{1+\epsilon}{\epsilon}\right)^c
                                \mathrm{poly}(H)
       \le\left(\frac{e(1+\epsilon)}{\epsilon}\right)^c
                                \mathrm{poly}(H),
 \tag{G3}
$$

and polynomial workspace. Here Gamma(R)=R^R/(R-1)^(R-1), and H
includes the bit encoding of epsilon. If the original problem is
infeasible, the algorithm may still return a common basis obeying
the augmented capacities; any reported failure soundly proves
original infeasibility.

Only the capacity guarantee is relaxed. There is no cardinality or
matroid-independence loss and no multiplicative cost loss. The cost
comparator in this theorem is the optimum integer common basis of
(G1), not an asserted relaxation optimum.

## 2. A cost threshold is part of the selection oracle

Because every selected set has cardinality r, adding the same
constant to every w_p shifts all feasible costs by the same amount.
Thus costs may be made nonnegative with polynomial-bit arithmetic,
without changing comparisons or the conclusion w(I)<=OPT. Work
with these shifted nonnegative costs in the algorithm.

Fix a rational threshold W>=0, and define

$$
\mathcal B_W=\{I:\ I\text{ is a common basis of }M_1,M_2,
                                                   \ w(I)\le W\}.
 \tag{G4}
$$

This is a fixed-cardinality family. On a restricted ground Q,
weighted matroid intersection finds a minimum-cost common
independent set of cardinality r, or certifies that no such set
exists. Comparing its cost with W either returns a member of B_W
contained in Q or certifies that none exists. This is exactly the
restriction selection oracle needed by Theorem E. Its cost is
polynomial in H, including all failed restriction calls.

For the explicit rows A_i, separate a proposed incidence vector
from the augmented capacities by computing all its row sums. Apply
Theorem E with capacities u'_i=(1+epsilon)u_i, t=1+epsilon and b=1.
The result is a one-sided target procedure:

- success returns a common basis of cost at most W satisfying all
  augmented capacities;
- failure proves that no original-capacity common basis has cost
  at most W.

If a violated augmented row is A_i, the branching algorithm uses
S=A_i intersect Q and

$$
\ell=|S|-\left\lfloor\frac{(1+\epsilon)u_i}{1+\epsilon}\right\rfloor
                         =|S|-\lfloor u_i\rfloor.
 \tag{G5}
$$

Any original-capacity witness must omit at least ell elements of S.
The violation |S|>(1+epsilon)u_i implies
ell>|S|*epsilon/(1+epsilon), supplying the exact entropy ratio in
(G3). A branch with ell>|Q|-r is rejected before enumerating subsets.
Every attempted deletion subset, including a selector rejection,
is charged in the augmented computation-tree bound.

## 3. One-sided cost-grid optimization

Choose a positive rational gamma of polynomial bit length such that
all shifted w_p are nonnegative integer multiples of gamma. A common
denominator of the q rational costs suffices; its bit length is at
most the sum of their input denominator lengths. Every common-basis
cost, and OPT when finite, lies on this grid.

Use the explicit upper threshold

$$
W_{\rm hi}=\sum_{p\in P}w_p.
 \tag{G6}
$$

All common bases have cost at most W_hi. Call the target procedure
there. A failure proves that (G1) is infeasible. A success supplies
the first recorded augmented-capacity basis. Use grid index -1 as
the initial lower endpoint: nonnegative costs prove that no common
basis has cost at most -gamma.

At each integer midpoint, success updates the upper endpoint and
its recorded basis; failure updates the lower endpoint. The lower
endpoint always lies strictly below the cost of every feasible
original-capacity common basis. At adjacent endpoints U=L+1,
integrality gives gamma U<=OPT whenever OPT is finite. The recorded
basis has cost at most gamma U and thus at most OPT. The procedure
does not assume monotonicity of algorithmic success.

The grid upper index W_hi/gamma has polynomial bit length, so the
number of calls is polynomial in H. Every call has the uniform
bound (G3), proving Theorem G. If all costs are zero, the initial
upper index is zero and no midpoint calls are needed. If r=0, the
empty common basis has cost zero and satisfies every nonnegative
upper capacity; it can be returned immediately.

## 4. Implicit rows and several approximate matroid constraints

The proof uses only a separation oracle for the upper capacities.
It therefore extends to a polynomially separable implicit family
with succinct rational violated rows, as specified in Theorem E.

For example, keep two matroids exact and let additional matroids
N_1,...,N_k on possibly overlapping subsets P_j impose rows

$$
|I\cap S|\le r_{N_j}(S)
                                 \quad(S\subseteq P_j).
 \tag{G7}
$$

Each augmented family is separated by minimizing
(1+epsilon)r_(N_j)(S)-|Q intersect S|. Deterministic submodular
minimization performs this in polynomial time. The output is an
exact common basis of M_1,M_2 and satisfies, for every j and every
S subseteq P_j,

$$
|I\cap S|\le(1+\epsilon)r_{N_j}(S).
 \tag{G8}
$$

The cost is at most the optimum common basis satisfying all these
constraints exactly. The number and overlaps of these additional
matroids affect the polynomial input cost, not the exponential
factor in (G3). The same conclusion holds for additional recipient
polymatroids instead of matroids.

The guarantee in (G8) applies to every rank inequality; a bound only
on |I intersect P_j| would be weaker and is not what is proved.
No exact common-basis algorithm for three or more unrestricted
matroids is being assumed.

## 5. An exact bounded-capacity corollary with a sharper direct bound

Suppose the explicit upper capacities are nonnegative integers
bounded by U_max. There is a direct exact algorithm, with preserved
minimum cost, in

$$
(U_{\max}+1)^c\mathrm{poly}(H).
 \tag{G10}
$$

To prove this, retain the cost-threshold restriction selector of
Section 2 and use the original capacities without inflation. If
1_Q satisfies every upper row, return the selector's common basis
inside Q. Otherwise choose a violated row A_i, and choose any
u_i+1 elements of Q intersect A_i. Every feasible common basis
omits at least one of these elements. Branch on deleting each of
them, charging failed selector calls as terminal attempted children.
The complement budget drops by one, and the branching factor is at
most U_max+1. A witness-preserving branch always exists on a
feasible target, so this is an exact target decision procedure.

For U_max>=1 its computation tree has at most
sum_(d=0)^c (U_max+1)^d<=2(U_max+1)^c nodes. If U_max=0, each
violated row forces one deletion, so the depth is at most c and
the work is polynomial. A zero remaining budget with a violated
row is rejected immediately. The same one-sided cost-grid search
then finds an exact minimum-cost feasible common basis, or correctly
reports that none exists. Polynomial workspace is retained.

This direct argument improves the bound obtained by specializing
the augmentation theorem; the latter remains a useful independent
derivation of exactness, recorded next.

If the explicit upper capacities are nonnegative integers bounded
by an integer U_max, take epsilon=1/(U_max+1). Then

$$
u_i\le(1+\epsilon)u_i<u_i+1.
 \tag{G9}
$$

The integer output must therefore satisfy |I intersect A_i|<=u_i
exactly. Theorem G alone gives the weaker
(O(U_max+2))^c poly(H) bound; the direct branching above gives
(G10). Both are joint-parameter consequences. They do not remove
dependence on the maximum bound or give an exact algorithm with
a fixed-parameter bound in c alone.

If U_max=0, the same argument uses epsilon=1, or more simply deletes
every element in a zero-capacity row before weighted matroid
intersection. Capacities at least r are automatically satisfied by
every common basis and may be discarded before defining U_max.

## 6. Primary-source comparison and limits of the comparison

For **one** exact matroid and explicit upper subset bounds, Kiraly,
Lau and Singh's *Degree Bounded Matroids and Submodular Flows*,
Theorem 2, gives a polynomial-time algorithm with cost at most the
original optimum and additive capacity error at most Delta-1, where
Delta is the largest number of listed constraint sets containing
one element. Their theorem covers arbitrary upper-bound overlap.
Primary author/publisher-hosted text:
<https://www.microsoft.com/en-us/research/wp-content/uploads/2017/01/degree_matroids.pdf>.
Our one-matroid specialization offers tunable multiplicative error
epsilon*u_i in corank-parameterized time; these are different
tradeoffs, and neither statement uniformly dominates the other.

For approximate multi-matroid feasibility, Linhares, Olver, Swamy
and Zenklusen's *Approximate Multi-matroid Intersection via Iterative
Refinement*, Theorem 2 of the IPCO 2019 version, preserves a basis
of one matroid and the LP objective while allowing integer
multiplicative violations q_j of the other matroids, provided
sum_(j:p in P_j) 1/q_j<=1 for every element p. The corank theorem
instead preserves two exact player matroids and obtains a common
1+epsilon violation for all remaining rank systems, with a cost
comparison against integer OPT and parameterized running time.
Primary text:
<https://ir.cwi.nl/pub/28684/Linhares2019_Chapter_ApproximateMulti-matroidInters.pdf>.
The journal version is recorded at
<https://ir.cwi.nl/pub/30178>.

These two primary baselines make the resource-augmentation
application concrete. They do not establish a first-ever result
for the corank parameter. Searches for degree-bounded matroid
intersection, corank/co-rank, and resource augmentation did not
locate a directly matching parameterized theorem in this pass;
that limited search is not a proof of absence. A dedicated novelty
review remains necessary before any priority claim.
