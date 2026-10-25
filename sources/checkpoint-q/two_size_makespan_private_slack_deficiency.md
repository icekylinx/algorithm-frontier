# Two-size scheduling with a private-slack rank deficit

**25 October 2026. New parameter refinement of the internally reviewed scheduling transfer.**

The exponential parameter in the two-size job-polymatroid scheduling
theorem can be smaller than the number of large job units. Machines
whose small-job capacity already leaves enough space for the required
large-job output may be committed by matroid greedy. Only the rank
deficit left after these commitments enters the unit-quota algorithm.

The proof uses the exact unit-core theorem in
`unit_quota_three_transfer_and_discrete_time_gate.md` and the scheduling
duality in `two_size_makespan_few_large_jobs_transfer.md`. All counts
are binary encoded and no job-slot expansion is used. The model remains
arbitrary integral job polymatroids supplied by rank-value oracles.

## 1. Model and the target-dependent parameter

Let P be q machines. The two positive sizes satisfy 0<u<a. A schedule
is a pair of integral bases of P(f_s) and P(f_b), where f_s and f_b
are normalized monotone integral submodular rank functions on P. Its
load at p is u x_s(p)+a x_b(p). Put h=f_b(P). Empty or zero-size
classes are removed or handled separately; assume h>0 below.

For a target T with a<=T<2a, let M be the matroid whose independent
polytope is P(f_b) intersected with the unit box. The hard branch is
possible only when rank(M)=h. Define the integers

\[
 c(T)=\lfloor T/u\rfloor,
 \qquad d(T)=\lfloor (T-a)/u\rfloor,
 \qquad K(T)=c(T)-d(T)>0.
 \tag{D1}
\]

For the uniform factor-three unit quota, write

\[
 b(T)=\lceil K(T)/3\rceil,
 \qquad L(T)=c(T)-b(T)
            =\left\lfloor\frac{2c(T)+d(T)}3\right\rfloor.
 \tag{D2}
\]

Define the directly computable machine set and rank deficit

\[
 F(T)=\{p\in P:f_s(\{p\})\le L(T)\},
 \qquad
 \delta(T)=h-r_M(F(T)).
 \tag{D3}
\]

Since L(T) is nondecreasing in T, F(T) expands and delta(T) is
nonincreasing throughout this hard interval. The matroid M does not
change with T there. Computing F and its matroid rank requires only
singleton rank queries and matroid greedy, after the Boolean-cap oracle
has been constructed.

For a fixed integer budget k>=0, define a monotone cap condition:

* T<a: the cap fails.
* a<=T<2a: the cap holds exactly when rank(M)=h and delta(T)<=k.
* T>=2a: the cap holds automatically, because the polynomial additive
  scheduling branch applies.

Let Theta_k be the smallest nonnegative target at which this cap holds.
It lies in [a,2a], is attained, and is defined without referring to an
unknown optimal schedule. If the Boolean rank is less than h, then
Theta_k=2a. The main guarantee is

\[
 \boxed{\quad
 C_{\max}\le\frac53\max\{\mathrm{OPT},\Theta_k\}
 \quad\text{in }2^{O(k)}\operatorname{poly}(H).
 \quad}
 \tag{D4}
\]

Here H pays for all original input and numerical bits, value-oracle
calls, deterministic submodular minimization, matroid operations and
integral base decomposition. Thus a full 5/3 approximation to OPT is
obtained whenever OPT>=2a, or when a<=OPT<2a and delta(OPT)<=k.
For k>=h the cap adds no restriction on originally feasible targets,
so (D4) contains the earlier h-parameter theorem. A failed large Boolean
rank can still make the cap fail below 2a, but every such target is
already originally infeasible.

**A cap failure is not a certificate that the original target is
infeasible.** It only says that this requested runtime parameter cannot
be used at that target. Section 6 gives the precise optimization search.

## 2. A private-coordinate lemma for arbitrary polymatroids

Let f be any integral polymatroid rank function on a ground set P.
Set

\[
                   \sigma_p=f(P)-f(P\setminus\{p\}).
 \tag{D5}
\]

Submodularity gives, for every S not containing p,

\[
               f(S\cup\{p\})-f(S)\ge\sigma_p.
 \tag{D6}
\]

In particular, f minus the modular function sigma is still normalized,
monotone, integral and submodular. Every base x of P(f) has x_p>=sigma_p.
More usefully, if F_0 is any set, y belongs to P(f restricted to
P\\F_0), and integers z_p obey 0<=z_p<=sigma_p for p in F_0, then

\[
                   y+z\in P(f).
 \tag{D7}
\]

To prove (D7), for any S use y(S\\F_0)<=f(S\\F_0), and add the
members of S intersected with F_0 one at a time in (D6). This proves
f(S)>=f(S\\F_0)+sum_{p in S intersect F_0} sigma_p, which bounds
the claimed vector on S. These coordinates therefore can be inserted
without reducing any feasible allocation on the other coordinates.

The same conclusion does not hold for arbitrary available units or
for an arbitrary independent preassignment. The special minimum
marginals (D5) are what justify avoiding a resource contraction.

## 3. Contracting only the player matroid preserves the full promise

Consider a unit-value allocation instance with player matroid M of
rank h, one arbitrary recipient polymatroid P(f), and a promised
M-basis I* that receives at least K integer units per member. Fix an
output quota b>=1 and let F={p:sigma_p>=b}.

Take a maximum M-independent subset F_0 of F by greedy, and put
Q=P\\F_0. Contract F_0 in the player matroid. The contracted matroid
M/F_0 has rank

\[
                       \delta=h-r_M(F).
 \tag{D8}
\]

Because I* spans M, its image spans M/F_0. Hence there is a basis
J subset of I*\\F_0 of M/F_0. Restricting the promised recipient
allocation to J preserves feasibility in P(f restricted to Q) and
still gives each member of J at least K units. Thus the residual
unit-core instance has the same K-unit promise and player rank delta.

Run the unit-quota algorithm on this residual instance. Its output is
a basis J of M/F_0 and an independent vector y on Q supplying b units
per member of J. Equation (D7) allows insertion of b units at every
member of F_0. Consequently F_0 union J is a basis of M and every
member receives at least b units in P(f). If delta=0, the core call is
empty and this last insertion already completes the construction.

The argument does not assume F_0 is contained in the unknown optimum
basis. It also does not assume F_0 has K private units. The committed
machines only need to meet the output quota b; the full K-unit promise
is retained on an appropriate basis of the contracted player matroid.

## 4. The dual small-job polymatroid has explicit private coordinates

For the hard scheduling target, box-restrict P(f_s) to coordinate cap
c and call the resulting rank function g_s. Check g_s(P)=f_s(P).
As in the earlier scheduling note, failure certifies OPT>T. The large
Boolean-cap check is similarly a genuine target infeasibility test.

The dual small-job rank function is

\[
                 f(S)=c|S|+g_s(P\setminus S)-g_s(P).
 \tag{D9}
\]

Its private marginal is particularly simple:

\[
 \begin{split}
 \sigma_p
   &=f(P)-f(P\setminus\{p\})\\
   &=c-g_s(\{p\})\\
   &=c-\min\{c,f_s(\{p\})\}.
 \end{split}
 \tag{D10}
\]

Since b>=1, the condition sigma_p>=b is exactly
f_s({p})<=c-b. Thus the set F from the abstract private-coordinate
lemma is precisely the directly computed set (D3).

A target-feasible schedule gives an M-basis of large-job recipients,
and its dual small counts are at least

\[
 K=c-\left\lfloor\frac{T-a}{u}\right\rfloor
   =\left\lceil\frac{a+cu-T}{u}\right\rceil
 \tag{D11}
\]

on every member. This is the required K-unit promise in Section 3.
Apply the unit theorem with b=ceil(K/3) and residual rank delta.
The total unit-core time is 2^{O(delta)}poly(H).

Extend the resulting dual vector coordinatewise to a dual base and
take its complement c*1-y for the small-job base. Assign one large
unit to each member of F_0 union J. The output is legal in the original
polymatroids because both capped total ranks were preserved.

## 5. Makespan bound and a concrete parameter separation

Put t=a+cu-T. In the hard branch 0<t<=a<=T, and K=ceil(t/u).
Every selected large-job machine receives at least b dual units, so
its actual load is at most

\[
                   a+(c-b)u=T+t-bu
                         \le T+\frac23t\le\frac53T.
 \tag{D12}
\]

Other machines have load at most cu<=T. For T>=2a the public additive
rounding branch returns load at most T+a<=3T/2. This proves the
fixed-target guarantee under the cap.

The parameter improvement can be large even when h grows with q.
For example, let the large-job matroid be uniform of rank h on q
machines. Suppose h-k machines have total eligible small-job capacity
at most L(T), while all remaining machines have larger such capacity.
Then those h-k machines belong to F(T), and delta(T)<=k regardless of
h. The large jobs need not be attached to designated machine labels:
matroid greedy chooses a maximum independent low-small-capacity set.

In ordinary restricted assignment, f_s({p}) equals the number of
small jobs eligible at p, with multiplicities if encoded in types.
The condition has the direct meaning that even the maximum possible
small-job load at p leaves the certified output space for a large job.
For arbitrary polymatroids the same interpretation is expressed by
the singleton rank, without an explicit list of eligible job copies.

This example explains the parameter separation; it does not claim
that the illustrated simple family needs an exponential algorithm.

## 6. Monotone cap, finite arithmetic, and optimization

Choose a common positive rational quantum g such that a/g and u/g
are integers. The binary representation of g has polynomial length.
Every integral schedule load lies on g times the nonnegative integers.
The functions c(T) and d(T) change only at multiples of u and at a
plus multiples of u. Thus all cap changes, a, and 2a lie on this same
grid, and Theta_k is an attained grid value.

The set of targets that are both originally feasible and pass the
cap is exactly

\[
                 [\max\{\mathrm{OPT},\Theta_k\},\infty).
 \tag{D13}
\]

The algorithm need not recognize this set exactly. It uses the
following one-sided target procedure:

1. If T<a, reject because h>0.
2. If T>=2a, use the additive assignment relaxation and rounding.
3. Otherwise check the two total-rank conditions. Their failure
   certifies original infeasibility.
4. If delta(T)>k, report cap failure, without claiming original
   infeasibility.
5. Run the rank-delta unit core and reconstruct the schedule. A core
   failure is a valid original infeasibility certificate by Section 3.

Any failure at a grid target T proves that no capped feasible target
is at most T: either original feasibility fails at T, or the monotone
cap fails there. A success supplies a directly evaluable integral
schedule of load at most (5/3)T, and may occur below the original OPT.
The success set itself need not be monotone.

Obtain arbitrary feasible bases and let V be their actual maximum
load. Use upper endpoint max{V,2a}, which is originally feasible and
automatically passes the cap; the additive branch therefore succeeds.
The grid point zero is a sound lower failure because h>0. Binary
search keeps a failed lower and successful upper endpoint, and retains
the best returned schedule. Until they become adjacent, query an
intermediate grid point. The lower endpoint is always strictly below
T*=max{OPT,Theta_k}. Since T* is grid-valued, adjacency implies that
the final successful upper endpoint is at most T*. This proves (D4).

The search has polynomially many queries in the bit length of V/g.
No pseudo-polynomial scan over targets or ranks is used. If one wants
Theta_k explicitly, first sort the singleton values f_s({p}) and
find the smallest threshold whose eligible set has M-rank at least
h-k; then solve the monotone inequality L(T) at least that threshold
on the same grid, clipped at 2a. This is also a polynomial-bit search.

## 7. Exact finite-rank quotas and the limit of the coefficient

For a player rank r>=1 and integer K, the exact quota condition is

\[
                  (3r-2)b<rK+2r-1.
 \tag{D14}
\]

Since the two sides are integers, its largest certified quota is

\[
             b_r(K)=\left\lfloor
                         \frac{rK+2r-2}{3r-2}
                       \right\rfloor.
 \tag{D15}
\]

For a fixed cap k>=1, use b=b_k(K), define F={p:sigma_p>=b}, and
require delta=h-r_M(F)<=k. The unit condition for rank k implies
the condition for the actual rank delta, because (delta-1)/delta
is nondecreasing in delta; delta=0 is handled directly. The whole
private-coordinate proof remains unchanged.

The stronger quota gives the exact target bound

\[
                    \max\{T,\ a+(c-b_k(K))u\}.
 \tag{D16}
\]

It also preserves cap monotonicity, because

\[
 c-b_k(c-d)
 =\left\lceil
    \frac{(2k-2)c+kd-2k+2}{3k-2}
   \right\rceil,
 \tag{D17}
\]

whose coefficients of c and d are nonnegative. The cap threshold for
this stronger quota must be recomputed; it can be larger than Theta_k
from (D2). It must not be silently replaced by the factor-three cap.

For k=1 the quota is K, giving an exact hard-target schedule. For
k=2 it is ceil(K/2), giving a hard-target bound at most 3T/2. The easy
branch is also at most 3T/2. Thus the corresponding strengthened cap
gives

\[
 C_{\max}\le\frac32\max\{\mathrm{OPT},\Theta^{(2)}_2\}
 \quad\text{in polynomial time},
 \tag{D18}
\]

where Theta^(2)_2 denotes the cap threshold with b=ceil(K/2). This
may apply with arbitrarily many large units; it requires residual
rank at most two under the stronger private-unit requirement.

For every k>=3, K=3 still yields b_k(K)=1. Setting T=a=3u gives
t=T and the bound (D16) can equal 5T/3. Therefore this integer quota
certificate alone does not improve the worst-case uniform 5/3
coefficient for k>=3. This is a limit of the displayed bound, not
an impossibility theorem for the algorithm or the scheduling problem.

At large K, put D_k=3-2/k. Equation (D15) gives
b_k(K)>(K-1)/D_k. Hence the hard-target load is strictly below

\[
                 (2-1/D_k)T+u/D_k,
 \qquad 2-1/D_k=\frac{5k-4}{3k-2}.
 \tag{D19}
\]

The additive u term is material at small quotas and cannot be omitted.

## 8. Fine small units and rank-quasipolynomial deficit dependence

Fix 0<eta<=1. Under u<=eta T/18, the hard branch has
K>=2(3+eta)/eta as proved in the earlier scheduling note. Use the
output quota

\[
                       b=\lceil K/(3+\eta)\rceil.
 \tag{D20}
\]

Define F, delta and the fixed-budget cap with this b. The relative
growth margin is Omega(eta), so the time becomes

\[
 \operatorname{poly}(H)
 \min\{2^{O(k)},(k+1)^{O((1+\eta^{-1})\log(k+1))}\}.
 \tag{D21}
\]

Rank zero uses only the direct insertion. The reconstructed load is
at most (2-1/(3+eta))T. Its cap is still monotone, because

\[
 c-\lceil(c-d)/(3+\eta)\rceil
   =\left\lfloor\frac{(2+\eta)c+d}{3+\eta}\right\rfloor.
 \tag{D22}
\]

For optimization, restrict targets to grid values T>=18u/eta. If
the instance is promised to have u<=eta OPT/18, this restriction does
not remove OPT. The same one-sided capped search proves ratio
2-1/(3+eta) against max{OPT,Theta_(k,eta)}, where Theta_(k,eta) is
the unrestricted cap threshold for quota (D20). An upper endpoint
at least max{V,2a,18u/eta}, rounded up to the grid, guarantees success.
The initial lower endpoint is the grid point immediately below the
restricted range; all genuine core calls satisfy the size promise.

A finite-k variant uses b=ceil(K/(D_k+eta)), with the cap defined for
that larger quota. Since delta<=k, its unit-core slack is no smaller
than the rank-k calculation. The same sufficient small-unit condition
applies. The ratio is

\[
               \max\{3/2,\ 2-1/(D_k+\eta)\}.
 \tag{D23}
\]

Cap monotonicity follows from
c-b=floor(((D_k+eta-1)c+d)/(D_k+eta)); all coefficients are
nonnegative. This gives a strict improvement over 5/3 when k is finite,
eta<2/k, and the fine-small-unit promise holds. It does not resolve
the small-quota growth gate for a uniform near-5/3 quasipolynomial
algorithm without a size promise.

## 9. Relation to public baselines and current proof status

The public primitive source is Bamas, Lindermayr, Megow, Rohwedder and
Schloeter, arXiv:2307.08453v1, particularly aggregation, box/dual
operations, and the additive scheduling rounding used in the easy
branch: <https://arxiv.org/html/2307.08453v1>.
Their polynomial guarantee for the two-size job-polymatroid model is
7/4+epsilon. The present note refines the parameter of the internally
proved constructive 5/3 transfer; it does not establish a polynomial
5/3 algorithm for unrestricted instances.

For ordinary two-size restricted assignment, a public 5/3 estimation
and configuration-LP gap bound appears in Jansen, Land and Maack,
SWAT 2016:
<https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.SWAT.2016.24>.
The repository abstract of Sengupta's 2025 thesis reports a
non-polynomial constructive 5/3 local search, polynomial at fixed
machine count: <https://www.ideals.illinois.edu/items/139520>.
These numerical baselines are recorded explicitly in the earlier
scheduling note. No direct public theorem with the private-slack
rank deficit (D3), full arbitrary job-polymatroid scope and the
displayed fixed-parameter runtime has been verified. This is a
bounded literature-check statement, not a claim of exhaustive priority.

The elementary scheduling approximation scheme exponential in all q
machines remains a separate baseline. Its count enumeration does not
yield the dependence in (D4) when delta is much smaller than q or h.
The key new proof steps here are the private-coordinate extension
(D7), retention of a full K-unit promise after contracting F_0 only
in the player matroid, and the monotone threshold needed to turn a
target-dependent rank into a correct optimization guarantee.
