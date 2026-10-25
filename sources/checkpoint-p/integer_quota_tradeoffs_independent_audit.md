# Independent audit of the integer-quota approximation/time tradeoffs

**25 October 2026. Full independent read of QT1--QT15: passes.**

This audit covers `integer_quota_approximation_time_tradeoffs.md` and checks
its exact small-target gates, quota ratio, cost-preserving integer recovery,
target optimization, full-machine scheduling dual, global time constants,
and binary-input scope. No substantive correction is required.

## 1. The worst remaining quota ratio is exactly the stated one

For fixed integer d>=2, the output count is b=ceil(K/d). The small-target
branch K<=d has b=1 and must be removed from the positive-gap analysis.
For K>=d+1, write K=jd+s with j>=1 and 1<=s<=d. Then b=j+1 and

\[
 \frac{K}{K-b}=
 \frac{jd+s}{j(d-1)+s-1}
 \le\frac{jd+1}{j(d-1)}
 \le\frac{d+1}{d-1}.
\]

For fixed j the ratio decreases with s, and its remaining excess above
d/(d-1) is 1/[j(d-1)]. Equality is attained at K=d+1. Every denominator in
this branch is positive. Since the derivative of log Gamma(R) is
log(R/(R-1))>0, the uniform time base is A_d=Gamma((d+1)/(d-1)).

The small-target gate is essential to this sharper constant. It is not
valid to leave K=2 in the generic quota recursion when d is large and
still quote A_d.

## 2. The one-unit gates have exactly the needed one-sided semantics

For one-value optional-basis allocation, minimum-cost intersection of the
parallel player matroid and the direct sum of Boolean resource matroids
finds the cheapest genuine basis receiving one original unit per player.
A full positive integer quota can be trimmed to one unit at every selected
player; nonnegative costs cannot increase. Thus failure of this gate
excludes every positive full target, including the queried K<=d.

Success need not show that K units are feasible. It gives exactly the
required weak quota ceil(K/d)=1. The manuscript states this distinction and
does not turn the gate into an incorrect exact K-unit test. Forced omitted
players are simply disallowed in the pair ground, so the same completeness
and polynomial-time bound hold after any admissible seed.

For compulsory two-value allocation, use all positive resource types and
the partition matroid imposing one unit on every player. If K=ceil(T/u)<=d,
then T<=du and one unit of value at least u supplies T/d. Trimming a full
positive allocation proves sound failure. The assignment costs remain the
original type-player costs throughout.

## 3. Integer recovery preserves the ceiling and the budget

At a fractional b-quota success, b is an integer. Discard outside counts
and trim each selected total to exactly b. The direct sum of the integral
recipient polymatroids intersects the per-player partition polymatroid
with cap b. The resulting maximum-total face of total br is nonempty and
integral. A minimum-cost integer optimum on that face costs no more than
the supplied fractional point. Its total forces every player quota to
equal b.

This proves the stronger ceiling guarantee ceil(K*/d), not merely a
fractional K*/d utility target. The proof uses an integral face and a
linear cost objective; it never assumes that imposing the budget row on
an integral polytope would retain integrality.

In the compulsory two-value adaptive core, the returned small set and heavy
assignment must be the pair attaining h_k(Q). Restricting and rounding the
small witness at budget C-h_k(Q), then adding this same assignment, costs
at most C. The protected original pair gives h_k(Q)<=c(H*) at every node
preserving its light set. The forced-omission cost is consequently
A_d^(k-|Z|) on all inputs, with all failed completion work charged.

## 4. Both allocation searches retain their full-target certificates

In the one-value model, an integer full target K implies the fractional
promise used by the positive-gap routine. Every failure therefore places
K strictly above the integer optimum. The external upper endpoint
floor(sum_j f_j(P)/r)+1 is valid even if it is never queried. At adjacent
integer endpoints, the saved nominal lower target L is at least K*, and
the saved allocation has ceil(L/d)>=ceil(K*/d) units. Nonmonotone successes
do not affect this argument.

For compulsory two-value allocation, the high-target condition is

\[
 T\ge\frac{d}{d-1}a.
\]

It gives T-a>=T/d after the established exact-cost lower rounding. Below
this threshold one has T<da, so one original heavy unit supplies more than
T/d and the adaptive count branch is applicable. The remaining small K
targets use the one-unit gate. These branches cover every positive target,
including equality at the high cutoff.

A full integer T-allocation supplies its actual heavy support k<=h_C;
retaining one original heavy assignment on that support and its original
small-only complement gives the required fixed-k promise. There is no
unpaid enlargement of the heavy support. If every k call fails, the
original full target is impossible. Common-grid one-sided maximization
then returns at least OPT_C/d.

The all-heavy k=q branch is direct minimum-cost coverage. Empty classes,
zero optimum, zero budget, and the compulsory one-value exact algorithm
are kept separate. No high-target LP for unknown optional player bases
is asserted.

## 5. The scheduling transfer keeps the physical dual fixed

In the rank-retained branch, the player matroid is the Boolean large-job
matroid of rank h, restricted to its nonloops. Its selected bases identify
one large unit on h machines. The small-resource box rank and its dual are
formed on all original physical machines after checking that the box
retains the full original small rank.

At a target a<=T<2a, write

\[
 C_T=\lfloor T/u\rfloor,\quad
 \delta_T=a+C_Tu-T,\quad
 K_T=C_T-\lfloor(T-a)/u\rfloor.
\]

Because u<a, the rounding remainder T-C_Tu is in [0,u), so
0<delta_T<=a. Also

\[
 K_Tu=\delta_T+
 [(T-a)-u\lfloor(T-a)/u\rfloor]\ge\delta_T.
\]

The full target supplies K_T units of the fixed dual on a large-job basis.
For K_T<=d, exact one-unit matroid intersection supplies b_T=1 or soundly
rejects. For larger K_T, the quota ratio above applies. Candidate deletions
restrict only large positions; they do not re-dualize the small resource
on a smaller machine ground.

After zero extension, completion to an integer full dual base, and
complementing back, the large machines have load at most

\[
 a+C_Tu-b_Tu
 \le T+(1-1/d)\delta_T
 \le (2-1/d)T.
\]

The other machines have load at most T. This includes the small-quota
gate and has no additive u loss. Original small and large aggregate bases
are recovered by the established integral decompositions.

The high-target additive-a rounding works at the same cutoff
d*a/(d-1), because T+a<=(2-1/d)T. This cutoff is at most 2a, so every
remaining hard target satisfies the one-large-unit premise. Targets below
a fail when a large unit exists. The original grid and one-sided
minimization search thus give (2-1/d)OPT, with a stored legal schedule at
every successful endpoint.

If the Boolean large rank is smaller than the large total h, every full
schedule has makespan at least 2a. The established additive-a branch then
gives 3/2, which is no worse than 2-1/d. The h=0 one-size problem is exact.
No assignment-budget preservation is claimed for this scheduling transfer.

## 6. The global constants, space, and numerical scope check

The forced-omission interfaces above satisfy the accepted block wrapper
on every input. The same original targets are used once in every extension
call, so the wrapper does not compound approximation losses. The explicit
ground is q players or the nonloop large-position ground P+, respectively;
it is never silently replaced by a compressed count of a binary-expanded
slot system.

The constants in the table are correct:

| d | A_d | Global base | Allocation | Scheduling |
| --- | --- | --- | --- | --- |
| 2 | 27/4 | 50/27 | 2 | 3/2 |
| 3 | 4 | 7/4 | 3 | 5/3 |
| 4 | (3125/108)^(1/3) | 2-(108/3125)^(1/3) | 4 | 7/4 |
| 5 | 3 sqrt(3)/2 | 2-2/(3 sqrt(3)) | 5 | 9/5 |

For fixed rational R=a/b, Gamma(R)^b is rational with the stated formula.
The fixed-d local comparisons are therefore exact algebraic comparisons
implemented by a fixed power. When d is binary input, the core only uses
rational quotas and threshold comparisons; it need not expand powers with
numeric exponent d. The manuscript correctly separates that analytical
bound from implementing the sharp global base, and provides the admissible
rational fallback 3R_d.

The optional profile-sensitive bound applies at each fixed corank, or at
each fixed heavy support k in the compulsory loop. The binomial fallback
uses only zero-deficit gap calls. All targets, counts, rank totals, and cost
coefficients remain binary; none of the procedures enumerates numerical
resource units. Depth-first recursion and streamed block products retain
polynomial workspace.

## 7. Disposition and public scope

QT1--QT15 pass. The improvement is a valid approximation/time tradeoff,
especially the exact factor-three allocation and factor-five-thirds
scheduling guarantees at global base 7/4. Its integer-quota gates explain
why this constant differs from the general arbitrary-value near-two
rounding tradeoff.

The generic global base transformation remains attributed to monotone
local search, and the costed count projection, adaptive invariant, integer
recovery, and scheduling dual retain their separate assumptions. This
audit does not make an exhaustive novelty claim or extend the one-unit
gate to a selection family whose required weighted intersection is not
polynomially available.
