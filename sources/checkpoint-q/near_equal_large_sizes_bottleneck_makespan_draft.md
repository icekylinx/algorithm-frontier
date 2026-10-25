# Near-equal large job sizes with a bottleneck rank budget

**25 October 2026. Root and independent mathematical audits completed.**

The reviews are `near_equal_large_sizes_bottleneck_root_audit.md` and
`near_equal_large_sizes_bottleneck_independent_audit.md`. They check
(H1)--(H16), including the convention that a_- and a_+ are the actual
extrema of the positive-rank large types. This convention is needed
for the target infeasibility check and the exact rational grid. The
historical filename remains stable. These are internal mathematical
reviews, not formal verification or external peer review.

This extends the workload scheduling transfer to several different
large sizes. It also gives an unconditional rank-budget guarantee:
preassign many large-job positions to machines with a small worst-case
load, run the unit algorithm only on the remaining contracted rank,
and charge the preassigned positions by a separate computable
bottleneck. No target-dependent cap or cap-failure search is needed.

The derivation uses the already reviewed unit theorem, workload
aggregation, integral base decomposition, and per-machine small-job
rounding. Its comparison with OPT includes the explicit additive
largest-small-job size. This term is retained throughout.

## 1. Model and the two size bands

Each job type j has a positive rational size p_j and an integral
polymatroid rank f_j on the q machines P. A legal schedule chooses
an integer base x_j of every f_j. Drop zero-rank types. Fix a nonempty
set of the largest job types, called the large band, such that

\[
 a_-\le p_j\le a_+\quad(j\text{ large}),
 \qquad p_j\le u<a_-\quad(j\text{ smaller}).
 \tag{H1}
\]

The smaller band may contain arbitrarily many different values.
If it is empty, take u=0 and its workload rank zero. The endpoints
a_- and a_+ are, by definition, the minimum and maximum sizes among
the positive-rank large types, rather than loose interval bounds.
Thus both endpoints are attained original job sizes. Define

\[
        R=a_+/a_-,\qquad f_b=\sum_{j\text{ large}}f_j,
        \qquad h=f_b(P)>0.
 \tag{H2}
\]

The useful near-equal regime is 1<=R<2. In this regime a target
T<2a_- can contain at most one large unit on any machine, whereas
T>=2a_- admits the public additive approximation branch. For R>=2
the latter crude coefficient reaches two and the claimed new bound
does not improve the public two-approximation in general.

Let M be the unit-box cap of P(f_b). First check whether r_M(P)=h.
If it fails, every schedule has two large units on some machine,
so OPT>=2a_-. The ordinary additive algorithm then already gives

\[
               C_{\max}\le\mathrm{OPT}+a_+
                         \le(1+R/2)\mathrm{OPT}.
 \tag{H3}
\]

Thus the rank-budget construction below is needed only when M has
rank h. In particular h<=q in every branch using the unit core.

## 2. A directly computable bottleneck for committed positions

For each machine define its maximum permitted smaller workload and
maximum possible large-unit size by

\[
 W_p=\sum_{j\text{ smaller}}p_j f_j(\{p\}),
 \qquad
 a_p=\max\{p_j:j\text{ large},\ f_j(\{p\})\ge1\}.
 \tag{H4}
\]

Take a_p=0 on a machine that is a loop of M. Such a machine is never
chosen for a large unit. Put C_p=W_p+a_p. Every legal final schedule
that assigns exactly one large unit to p has load at most C_p,
regardless of the way its smaller jobs are rounded: each final
integer component obeys x_j(p)<=f_j({p}).

For an integer budget 0<=k<=h, choose an M-independent set F_0 of
size h-k minimizing its maximum C_p, and let

\[
          B_k=\min_{F_0\in\mathcal I(M),\ |F_0|=h-k}
                         \max_{p\in F_0} C_p.
 \tag{H5}
\]

Use maximum over the empty set equal to zero, so B_h=0. The selected
F_0 and B_k are found by sorting C_p and applying matroid greedy.
Indeed, a threshold z permits h-k independent choices precisely when
the rank of {p:C_p<=z} is at least h-k. One sorted greedy basis gives
the entire sequence B_0,...,B_h, with B_k nonincreasing in k.

A simpler, slightly weaker expression is
B_k<=a_++lambda_k, where lambda_k is the minimum possible maximum
W_p on an independent set of size h-k. In the homogeneous large-size
case a_p=a on every nonloop, equality B_k=a+lambda_k holds for k<h.

No particular large-type decomposition of F_0 is fixed. Such a
decomposition might obstruct a later extension. F_0 is fixed only as
an independent set of the aggregate recipient matroid M, and the
large-type assignments are recovered after the final M-basis is known.

## 3. Main guarantee for positive residual rank

Fix 1<=k<=h and a rational D>=D_k:=3-2/k. Define

\[
                 \beta(D,R)=\max\left\{1+R/2,
                                      2-\frac1{DR}\right\}.
 \tag{H6}
\]

The resulting schedule satisfies

\[
 \boxed{\quad
             C_{\max}\le
                 \max\{\beta(D,R)\,\mathrm{OPT}+u,\ B_k\}.
 \quad}
 \tag{H7}
\]

At D=D_k the deterministic runtime is 2^{O(k)}poly(H). At
D=D_k+eta, for rational 0<eta<=1, it is

\[
 \operatorname{poly}(H)
 \min\{2^{O(k)},(k+1)^{O((1+\eta^{-1})\log(k+1))}\}.
 \tag{H8}
\]

The choice D=3+eta also has the bound (H8), since its excess over
D_k is at least eta. H includes all input and numerical bits,
derived oracle operations, deterministic submodular minimization,
matroid operations, decompositions and rounding. All counts remain
binary encoded. This is not exponential in q unless the chosen rank
budget itself is comparable to q.

Taking k=h gives B_h=0 and the full-rank guarantee
beta(D_h,R) OPT+u in 2^{O(h)}poly(H), or
beta(3+eta,R) OPT+u in rank-quasipolynomial time. Other budgets can
be much faster when low-load machines cover all but k independent
large-job positions.

## 4. Exact artificial quota and the target promise

Let g=1/Q divide every original job size. For D=A/B in positive
integer terms, take Delta=g/A. Then

\[
       K=a_-/\Delta,\qquad b=K/D,
       \qquad m_j=p_j/\Delta\quad(j\text{ smaller})
 \tag{H9}
\]

are integers, with K,b positive. Use targets on the Delta-grid and
set c=T/Delta. The smaller-workload rank is
F=sum_(j smaller) m_j f_j. Cap P(F) at c on every machine, giving
rank G, and require G(P)=F(P). A failed check certifies original
target infeasibility. All these quantities and rank computations
have polynomial bit length; no numerical workload unit is expanded.

Consider a hard target a_+<=T<2a_-. In an original feasible schedule,
the large recipients form a basis I* of M: the aggregate large count
is Boolean and has total h. On each such recipient p, its actual
large job has size at least a_-, so its smaller workload is at most
T-a_-. The complement in the dual rank

\[
                       f(S)=c|S|+G(P\setminus S)-G(P)
 \tag{H10}
\]

therefore supplies at least K dual workload units on every member
of I*. The variation between the large sizes causes no loss in this
promise; only their minimum a_- is used here.

## 5. Contracting F_0 needs no private-resource hypothesis

The precomputed set F_0 is independent in M. The contracted player
matroid M/F_0 has rank k. Restrict the recipient rank f to
Q=P\\F_0; do not contract f by any preallocation.

Because I* spans M, its image spans M/F_0. It consequently contains
a contracted basis J subset of I*\\F_0. The original dual allocation
restricted to J is feasible in P(f restricted to Q) and retains at
least K units on every member. This supplies the full K-unit promise
at player rank k, even when F_0 is disjoint from the unknown optimum
basis.

Run the unit algorithm with quota b. Its strict condition is

\[
                        D_k b<K+1+(k-1)/k.
 \tag{H11}
\]

Since D b=K and D>=D_k, this condition holds. If D=D_k+eta,
the slack is eta*b+1+(k-1)/k, whose ratio to the cover coefficient
2b-1 is greater than eta/2. The accepted growth proof then gives
(H8), without a large-K ceiling-loss assumption.

The output is a basis J of M/F_0 with b dual units per member. Lift
its independent dual vector to P by inserting zero on F_0. This is
always feasible: for each set S, its value is at most
f(S\\F_0)<=f(S). Extend to an integral base of P(f), preserving the
quota on J, and complement to a workload base w.

This zero insertion is the distinction from the private-slack cap
construction. F_0 is not promised any dual quota. Its final load
will instead be bounded directly by B_k. Thus there are no cap failures
and no target-dependent parameter assumptions in (H7).

## 6. Recovering all job types and the three load bounds

The union I=F_0 union J is a basis of M. Decompose its Boolean vector
1_I as a sum of integer bases of the original large-type ranks f_j.
Every p in I receives exactly one large unit. Such a decomposition
exists by the aggregate polymatroid base identity and preserves every
original type's required total rank. Its assigned size at p is at
most a_p, and in particular at most a_+.

Decompose w into integer bases of the scaled smaller ranks m_j f_j,
divide each by m_j to get fractional original smaller-job bases, and
apply the separately proved per-machine additive rounding lemma.
This restores integral original smaller-job assignments, raising each
machine's smaller workload by at most u. The three kinds of machine
then obey:

* If p is in J, its load is at most T+a_+-a_-/D+u.
* If p is in F_0, its final load is at most C_p<=B_k. This bound
  already holds after rounding and has no additional +u term.
* If p is outside I, its load is at most T+u.

For a hard target, T>=a_+ and a_+-a_-/D>=0. Therefore

\[
                 T+a_+-a_-/D
                    \le\left(2-\frac1{DR}\right)T.
 \tag{H12}
\]

For an easy target T>=2a_-, round all jobs directly to load at most
T+a_+<=(1+R/2)T. Combining these cases gives the fixed-target bound
max{beta(D,R) T+u,B_k}. A target T<a_+ is genuinely infeasible,
since the largest positive-rank job type needs a unit of size a_+.

## 7. Optimization, grid precision and the zero-rank budget

The positive-k target procedure only has genuine infeasibility failures:
a size check, a necessary workload/Boolean rank check, an infeasible
assignment relaxation, or failure of the contracted K-unit promise.
Every target-feasible schedule supplies the contracted promise by
Section 5. Thus failure always implies OPT>T.

All possible original integral loads lie on the original g-grid and
therefore on the finer Delta-grid. Start with a zero failed lower
target and upper target max{V,2a_-}, where V is the load of arbitrary
feasible original bases. The upper target is originally feasible and
uses the successful easy branch. One-sided binary search on the
Delta-grid ends with a successful target no larger than OPT, without
assuming the success set is monotone. The bound
max{beta(D,R)T+u,B_k} is monotone in T, yielding (H7). The number of
trials is polynomial in the binary target range.

There is also a useful polynomial k=0 endpoint. Choose a bottleneck
basis F_0 of M, with value B_0. Balance the aggregate smaller workload
fractionally without regard to the large jobs, then round the smaller
components per machine. The fractional smaller optimum is at most
OPT, since deleting large jobs from an original optimal schedule
provides a feasible fractional smaller allocation. Decompose 1_F0
into original large bases. On F_0 the final load is at most B_0;
elsewhere it is at most OPT+u. Hence

\[
                C_{\max}\le\max\{\mathrm{OPT}+u,B_0\}
                        \quad\text{in polynomial time}.
 \tag{H13}
\]

One can obtain this endpoint by a polynomial-bit workload target
search or the standard assignment LP. It does not invoke a rank-zero
formula D_0. It applies when the largest-band Boolean matroid has
full rank; the rank-failure case is already handled by (H3).

For a maximum allowed budget K_0, run every 0<=k<=min{K_0,h} and
return the best actual schedule, also comparing with the public
two-approximation. The runtime remains within the largest displayed
budget up to polynomial factors. This gives the envelope of all
corresponding bounds, rather than requiring advance knowledge of which
bottleneck term is active at the unknown OPT.

## 8. A simple near-equal corollary

Take D=3+eta and suppose R<=1+tau with 0<=tau<1. The hard coefficient
satisfies

\[
 2-\frac1{(3+\eta)(1+\tau)}
   \le\frac53+\frac\eta9+\frac\tau3.
 \tag{H14}
\]

The easy coefficient obeys
1+(1+tau)/2<=5/3+tau/3 for tau<=1. Hence

\[
                 \beta(3+\eta,R)
                       \le\frac53+\frac\eta9+\frac\tau3.
 \tag{H15}
\]

In particular, for k=h and u<=epsilon OPT, the algorithm returns
an integral schedule of ratio at most

\[
                         \frac53+\frac\eta9
                                    +\frac\tau3+\epsilon
 \tag{H16}
\]

in rank-quasipolynomial time in h. For a smaller k, the same statement
holds whenever B_k is at most that bound times OPT; otherwise (H7)
still reports the unconditional, explicitly computable bottleneck
term. The exact finite-k choice D_k can further improve the coefficient.

For example, the exact k=3 hard coefficient is 2-3/(7R). Its full
coefficient beta(D_3,R) is below 5/3 when R<9/7. The additive u
and bottleneck B_3 remain necessary in that statement. These are
explicit regimes, not an unconditional sub-5/3 result for unrestricted
job sizes.

The large band need not be supplied as extra information. It can be
chosen from every suffix of the sorted positive-rank size values with
a_+/a_-<2. For a fixed maximum rank budget, run the construction for
each such suffix and return the best actual schedule, together with
the public additive candidate. There are only polynomially many
suffixes, so this adds a polynomial factor to the runtime and obtains
the best of their proved bounds. It accepts arbitrary size instances,
but its bound is strictly below two only when one of the stated
size/bottleneck tradeoffs makes it so.

## 9. Public comparison and an elementary alternative

Bamas et al., *Santa Claus meets Makespan and Matroids*, provide the
general job-polymatroid aggregation and additive rounding primitives,
and the public polynomial two-approximation in the arbitrary-value
model: <https://arxiv.org/html/2307.08453v1>.
Their two-value 7/4+epsilon statement cannot be used as the general
many-value baseline for the model in (H1).

For ordinary restricted assignment, Jansen and Rohwedder provide an
unconditional constructive 11/6+epsilon approximation in time
n^{O(epsilon^-1 log n)}; the primary full version is
<https://arxiv.org/html/1701.07208v2>, Section 4 and Lemma 14.
Consequently (H16) improves that numerical guarantee in the stated
banded regime when eta/9+tau/3+epsilon<1/6. It also makes the nonlinear
time depend on h or a smaller chosen k rather than the entire input
size. The public theorem has the advantage of needing no size-band
or small-job promise. The arbitrary oracle-polymatroid scope of this
draft is a separate model distinction.

A related banded result is Huang and Ott, *A Combinatorial Approximation
Algorithm for Graph Balancing with Light Hyper Edges*, ESA 2016:
<https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ESA.2016.49>.
It gives polynomial 3/2 approximation for two sizes, and a
5/3+beta/3 guarantee when large sizes lie in (beta W,W] with
4/7<=beta<1. Its essential additional restriction is that each heavy
job has at most two eligible machines. That restriction is absent
from this draft. Its beta is a size threshold, not the spread tau
used in (H14)--(H16); the similar-looking constants are not the same
parameterized claim.

An elementary algorithm can enumerate the placements of all h large
units, test their original polymatroid constraints, solve the remaining
fractional small-workload problem and round it. This yields the stronger
quality OPT+u with a dependence of the form q^{O(h)} times polynomial
input factors. It is a genuine comparison: the present result trades
quality for a polynomial degree independent of h. Enumeration of the
unknown h recipient machines must not be counted as an FPT procedure.

The numerical constant 5/3 already occurs publicly for ordinary
two-size estimation and constructive local search; its value alone
is not a novelty claim. This draft instead proves a rank-budget,
bottleneck-sensitive constructive guarantee for near-equal large
sizes and arbitrarily many smaller values, with all rounding losses
stated. No exhaustive publication-priority claim is made.

The current search also checked the 2026 primary preprint
*From Estimates to Schedules: Learning-Augmented Restricted Assignment*,
<https://arxiv.org/html/2606.08377v1>. Its repair parameter is moved
load or the number of moved jobs relative to a supplied prediction,
and its exact repair procedure has input-size exponent depending on
that error. It does not supply the fixed-parameter h or bottleneck
theorem asserted here. No non-prediction near-equal-band competitor
with the same oracle model and runtime was verified in this bounded
search; this statement is not an exhaustive absence claim.
