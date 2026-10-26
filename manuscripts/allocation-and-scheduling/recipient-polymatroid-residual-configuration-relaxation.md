# Residual-capacity cuts restore a configuration comparator for general polymatroids

The exact subset description is in
[recipient-polymatroid-subset-cut-compression.md](recipient-polymatroid-subset-cut-compression.md). For coordinate-box
local families, the subsequent
[residual-configuration-bounded-support-xp-solver.md](residual-configuration-bounded-support-xp-solver.md) computes the
fractional full comparator in singly exponential q time, or its
support-2(r-1) version in q^{O(r)} time. These separate solver results
do not assume that the allocation algorithm solves the LP.

The direct aggregate configuration LP for recipient polymatroids can
have a gap approaching the player-selection rank. This note strengthens
that relaxation by explicit, valid residual-capacity inequalities. The
existing compressed prefix algorithm then has factor 4-3/r, or that
factor plus eta in rank-quasipolynomial time, against the strengthened
relaxation for **arbitrary integral recipient polymatroids**.

The algorithm does not solve this LP. Polynomial separation of all the
new inequalities is not established. The cut family, its validity,
the lower-cover proof and its preservation by the fat reduction are
proved below. On a supplied scaled matroid type f=c r_R, the cuts are
already implied by the existing component configuration constraints.

## 1. Model and the finite strengthened LP

Use the model and binary encoding of
[recipient polymatroid proof](../../problems/recipient-polymatroid/proof.md): a player
matroid M of rank r on q explicit players; resource types j with common
rational unit values v_j; integral monotone submodular ranks f_j; and
type-symmetric downward-closed local count families F_p. Counts of type
j are bounded by f_j({p}) for player p. The exact or factor-lambda
available-count oracle is paid, and lambda is a rational certified
guarantee. Put tau=1/lambda and rho=(r-1)/r.

For target T, let C_p(T) be the finite family of local feasible integer
count vectors n in F_p with v dot n>=T. A configuration variable mu_pn
is nonnegative. Define

$$
x_p=\sum_{n\in C_p(T)}\mu_{pn},\qquad
 y_{pj}=\sum_{n\in C_p(T)}\mu_{pn}n_j.
 \tag{L1}
$$

The ordinary aggregate constraints are

$$
x\in P_{\mathcal B(M)},\qquad
 y_{\cdot j}\in P(f_j)\quad\text{for every }j.
 \tag{L2}
$$

For an arbitrary integral feasible reserved vector z in P(f_j), define
its individual residual capacity at player p by

$$
a_{pj}(z)=\max\{a\in\mathbb Z_{\ge0}:z+a e_p\in P(f_j)\}
          =\min_{S\ni p}\{f_j(S)-z(S)\}.
 \tag{L3}
$$

The last equality follows by checking exactly the rank inequalities
containing p. All terms are integral and nonnegative because z is
feasible. The singleton inequality bounds a_pj by f_j({p})-z_p.
This quantity is computable by deterministic submodular minimization
with p forced into the set.

Add, for every resource j and every such z, the inequality

$$
\boxed{
 \sum_p\sum_{n\in C_p(T)}\mu_{pn}\bigl(n_j-a_{pj}(z)\bigr)_+
                  \le z(P).
 }
 \tag{L4}
$$

Here (u)_+=max(u,0). For a fixed z, (L4) is a linear inequality in
the configuration variables, with nonnegative integer coefficients.
Call (L1)--(L4) the residual-capacity configuration relaxation.

The family is finite: each coordinate of a feasible z lies between zero
and f_j({p}). The number of vectors and configurations can be enormous
in the binary input length. This definition does not assert a polynomial
size formulation or a separation algorithm.

## 2. Every integral allocation satisfies every new cut

Fix a resource and omit its index. Let z and n be arbitrary integral
vectors in P(f). Form the natural matroid on player-copy blocks and
choose an independent copy set Z with counts z. A set N with counts n
is also independent. Extend Z to a maximal independent subset of
Z union N. It has rank at least |N|, so the added set H from N minus Z
has at least |N|-|Z| elements.

The block-count vector h of H satisfies 0<=h<=n. Because Z union H
is independent, h_p<=a_p(z) for every p. It follows that

$$
\sum_p(n_p-a_p(z))_+
       \le\sum_p(n_p-h_p)
       \le |Z|=z(P).
 \tag{L5}
$$

The same conclusion follows from the earlier contraction-and-box loss
lemma: a subvector h of n can be placed in the contraction by Z while
losing at most z(P) units.

Now take an integer target allocation on a basis of M and give each
selected player mass one on its actual configuration. At resource j,
the left side of (L4) is exactly the left side of (L5) for that legal
recipient-count vector. Thus the integer allocation satisfies every
cut. Convex combinations of integer target allocations also satisfy
them. The new LP is a genuine relaxation of the integer problem.

## 3. Dependent algorithm reservations have the same cut as a feasible vector

The actual algorithm reserves W_j, the union of current selected and
designated matching service copies. It need not be independent. Its
rank is R_j, and the algorithm's available count is

$$
A_{pj}=r_j(W_j\cup E_{pj})-r_j(W_j).
 \tag{L6}
$$

Choose any basis Z_j of W_j and let z^j be its block counts. Then
z^j is integral and belongs to P(f_j), and z^j(P)=R_j. Since Z_j spans
W_j,

$$
a_{pj}(z^j)=r_j(Z_j\cup E_{pj})-r_j(Z_j)=A_{pj}
                    \quad\text{for every }p.
 \tag{L7}
$$

Therefore (L4), for this feasible z^j, has exactly the residual
capacities used in the algorithm and right side r_j(W_j). It is not
necessary to add separate cuts for dependent reserved multisets.

The basis counts can, if a concrete certificate is desired, be found
without listing copies: maximize a count vector of P(f_j) under the
coordinate box given by W_j, using the integral box-restricted
polymatroid rank and greedy optimization. This takes polynomially many
paid submodular-minimization operations. Any resulting maximum-sum
subvector is realized by a basis of W_j and has the same residual
capacities (L7).

## 4. The strict lower cover against the new LP

At a completed failed search state, let E=P minus cl_M(J) be its
eligible players and w=r-r_M(J)>0. For every original count
configuration n of player p, truncate it coordinatewise to

$$
n'_j=\min(n_j,A_{pj}).
 \tag{L8}
$$

It remains in F_p by downward closure and satisfies the actual
availability box. If the unchanged-state available oracle returned
value below B, then its true available optimum is below tau B.
Consequently every truncated configuration for an eligible player has
value strictly below tau B.

For x_p>0, mixing configurations gives retained expected value

$$
H_p=\sum_n\mu_{pn}\sum_jv_j\min(n_j,A_{pj})<\tau Bx_p.
 \tag{L9}
$$

The original configurations have value at least T, so their expected
value is at least Tx_p. Their exact lost value is

$$
\sum_jv_j\sum_n\mu_{pn}(n_j-A_{pj})_+.
$$

Apply (L4) using (L7), sum over j with weights v_j, and use
nonnegativity to restrict the left side to eligible players. Since
x(E)>=w and there is positive eligible mass,

$$
\boxed{\Phi=\sum_jv_jr_j(W_j)>(T-\tau B)w}
                       \qquad(T\ge\tau B).
 \tag{L10}
$$

This is the exact strict lower-cover interface required by the
prefix-normalized local search. Its upper cover, all-subsets
reservations, eager release, old-prefix preservation and signature
do not change. The algorithm neither knows the LP point nor computes
its configuration variables.

## 5. Fat splitting preserves all residual cuts

Let the fat threshold be B0. For every configuration containing a fat
unit, select one such unit. Let f^j_p be its one-service marginal of
fat type j and let f_p=sum_j f^j_p. Then f^j<=y_.j and f<=x<=1.
By down-closure,

$$
f^j\in P(f_j)\cap[0,1]^P.
$$

This is the independent-set polytope of the Boolean restriction
matroid N_j, whose rank is

$$
r_{N_j}(S)=\min_{A\subseteq S}\{f_j(A)+|S\setminus A|\}.
 \tag{L11}
$$

Locally infeasible singleton recipients are excluded by matroid
restriction. The selected fat marginal is automatically supported on
the remaining players because the original local family is downward
closed. Union the fat N_j and take U=M* vee N, as in the established
fat reduction.

The vector 1-x+f belongs to the union independence polytope. Extend it
coordinatewise to a U-base vector and complement, obtaining a U*-base
vector x'<=h=x-f. The vector h_p is precisely the total mass of p's
all-small configurations. Discard every fat-containing configuration,
and scale each retained configuration of player p by x'_p/h_p, taking
zero when h_p=0. Every remaining configuration still has value at least
T and belongs to its small-resource local family.

Each small resource's aggregate marginal only decreases, preserving
P(f_j). More importantly, every left side of every residual cut (L4)
only decreases: configuration masses have been discarded or multiplied
by factors at most one, and all cut coefficients are nonnegative.
The rank function, feasible reserved vectors, residual capacities and
right sides for that small resource are unchanged. Therefore **all
residual cuts survive the fat reduction**.

Thus feasibility of the new LP at target T supplies the same new-LP
promise for the derived small-player matroid, of rank at most r. The
usual reverse union reconstruction combines small and fat allocations
into a basis of M. No new coupling constraint is lost in this step.

## 6. Result and runtime

The lower cover (L10) and the proved current upper cover give

$$
\Phi\le\max\{u,2B+\min(u,B)\}|Y|,
$$

with sufficient condition tau B+rho max{u,2B+min(u,B)}<=T.
Use B0=T/(tau+3rho), classify fat units at B0, and use the same
exact or positive-error search parameters as in the prefix theorem.
It follows that the deterministic approximation factor against the
residual-capacity configuration optimum is

$$
d=\tau+3-3/r\quad\text{in }2^{O(r)}\operatorname{poly}(H),
 \tag{L12}
$$

or d+eta, for positive rational eta, in

$$
\operatorname{poly}(H)
 \min\{2^{O(r)},(r+1)^{O((1+\eta^{-1})\log(r+1))}\}.
 \tag{L13}
$$

All the binary encoding, finite-grid target search, deterministic
submodular-minimization, local-oracle and polynomial-space qualifications
of the existing algorithm remain in force. No work is added to solve
or separate this strengthened LP. A failed search is sound against
it, and a successful search returns an actual integral allocation.
The positive integer optimum is at most the LP optimum, so the earlier
integer-optimum result is retained as a consequence.

For exact availability this proves a constructive integrality-gap bound
4-3/r for the specified strengthened relaxation. This is not a claim
about the weaker aggregate relaxation or about polynomial-time LP
optimization.

## 7. Bounded-support reserved vectors already suffice

One may keep only the cuts (L4) whose feasible reserved vector has at
most 2(r-1) positive coordinates. Indeed, a normalized completed state
has at most r-1 matching records and at most as many selected records
as current blockers. Its reserved set therefore has at most 2(r-1)
distinct owners. A basis of that set has no larger owner support.
Those are exactly the cuts used in (L7)--(L10).

The derived small-player rank never exceeds r, so the same fixed
support bound still covers every inner search state. Discarding and
downscaling configurations preserves this restricted cut family as
well. For r=1 the support bound is zero; direct rank-one local
optimization handles that case.

This optional weaker relaxation has the same approximation theorem.
The observation does not establish efficient separation: selecting a
support from q players and selecting large binary counts remain tasks
that the allocation algorithm itself does not need to perform.

## 8. On scaled matroid types the new cuts are redundant

Suppose f=c r_R for one supplied type, c>0. For a feasible reserve z
write a_p for its residual capacity. The independently audited scaled
matroid loss lemma gives, for every y/c in P_I(R),

$$
\sum_p(1-a_p/c)y_p\le z(P).
 \tag{L14}
$$

Every local count n satisfies 0<=n_j<=c at a nonloop. For every such
integer n_j and 0<=a_p<=c,

$$
(n_j-a_p)_+\le(1-a_p/c)n_j.
 \tag{L15}
$$

If n_j<=a_p this is immediate. Otherwise it is equivalent to
a_p n_j/c<=a_p, which follows from n_j<=c. Loop coordinates have
zero configurations counts. Averaging (L15) and applying (L14)
proves (L4) from the ordinary component column constraint alone.

Consequently the strengthened relaxation coincides with the existing
component configuration relaxation when every supplied type is a
scaled matroid rank. The new theorem unifies that stronger fractional
result with arbitrary recipient polymatroids. Merging components with
different recipient matroids can make the residual cuts genuinely new.

## 9. A single cut excludes the earlier rank-gap point

In the explicit example with q=Dr players, D>=r>=2,
f(S)=|S|+D for nonempty S, and configuration D+1 at every player with
mass 1/D, reserve z=(D+1)e_a at any one player a. This is feasible,
and z(P)=D+1. Its residual capacities are a_a=0 and a_p=1 for p!=a.
The left side of (L4) is

$$
\frac{D+1}{D}+(q-1)\frac{D}{D}
                         =q+\frac1D>D+1.
$$

Thus even a support-one residual cut rejects the aggregate gap point.
This does not mean all fractional points are integral; it demonstrates
that the additional inequalities repair the exact failure encountered
in the attempted naive polymatroid configuration transfer.

## 10. Separation, sources and claim boundaries

For a fixed proposed feasible z and an explicitly represented finite
configuration point, evaluating its cut is polynomial in the explicit
support and numerical bits, using the value oracle and deterministic
submodular minimization. Finding a violated cut among all z is a
different problem. No polynomial or rank-quasipolynomial separation
algorithm is proved here. Neither is efficient configuration pricing
under arbitrary dual weights and arbitrary local families.

The allocation algorithm needs neither operation: it generates its own
reserved vectors through the already paid search and uses only the
promised available-count oracle. One must not convert (L12)--(L13) into
an assertion that the displayed LP itself can be optimized in those
times without another argument.

The public source Bamas, Lindermayr, Megow, Rohwedder and Schloeter,
[*Santa Claus meets Makespan and Matroids: Algorithms and Reductions*,
arXiv:2307.08453v1](https://arxiv.org/html/2307.08453v1), Section 1.2,
already discusses a large configuration-LP gap in a related polymatroid
capture and the need for another infeasibility certificate. The present
explicit rank-gap construction is not claimed to be the first discovery
of that general phenomenon. The contribution claimed for this note is
the fully specified residual cut family, its preservation by the
fractional fat reduction, and its compatibility with the new compressed
prefix algorithm. No exhaustive publication-priority claim is made.

## 11. Integer quotas against the residual-capacity comparator

**Corollary.** Consider the unit-value model of the exact prefix-quota
algorithm, with integer configuration target $t$ and requested integer
output quota $1\le b\le t$. Suppose the residual-capacity configuration relaxation
(L1)--(L4) is feasible at target $t$. In every normalized state in which
the exact available-count scan fails for all eligible players, its resource
cover satisfies

$$
\Phi\ge(t-b+1)w,
\qquad w=r-r_M(J)>0.
\tag{L16}
$$

Consequently the proved unit-quota algorithm may use this relaxation as
its comparator under the same quota and growth conditions as its original
prefix theorem. This transfer does not assert polynomial-time optimization
of the relaxation.

**Proof.** Let $E=P\setminus\operatorname{cl}_M(J)$ be the eligible set.
Clip a configuration $n\in C_p(t)$ at the actual residual capacities
$a_{pj}(z^j)$ from (L7). The clipped count vector remains in the player's
downward-closed local family. A failed exact scan implies that its total
integer count is at most $b-1$; otherwise it contains an available
$b$-unit bundle. Since the original configuration has at least $t$ units,
its lost count is at least $t-b+1$.

Averaging over configurations gives lost mass at least
$(t-b+1)x_p$ for each $p\in E$. Summing the corresponding residual cuts
over resource types bounds that lost mass by their total reserved rank
$\Phi$. The player-base constraint gives
$x(E)\ge r-r_M(J)=w$. Therefore

$$
\Phi
\ge\sum_{p\in E}\sum_{n\in C_p(t)}
       \mu_{pn}\sum_j(n_j-a_{pj}(z^j))_+
\ge(t-b+1)x(E)
\ge(t-b+1)w.
$$

This is precisely the lower-cover input to the integer quota proof.
The normalized upper-cover coefficient remains $2b-1$, and the
fractional fat reduction preserves all residual cuts by Section 5.
Thus the original exact rank-exponential factor-three quota guarantee
inherits the stronger comparator. In particular, the critical
$t=4$, $b=2$ quasipolynomial growth boundary is unchanged: (L16) is
non-strict and does not supply an additional uniform growth margin.
$\square$
