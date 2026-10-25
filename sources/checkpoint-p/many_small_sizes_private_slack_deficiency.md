# Workload scheduling with private slack and an exact finite-rank coefficient

**25 October 2026. New refinement; the workload transfer and private-coordinate lemma have separate independent reviews.**

This note combines the workload construction in
`many_small_sizes_workload_makespan_transfer.md` with the private-coordinate
contraction in `two_size_makespan_private_slack_deficiency.md`. It also
chooses the artificial workload quantum to make the desired output
quota exactly integral. This removes a quota ceiling loss in the
finite-rank coefficient. The final schedule still pays the largest
smaller-job size u for restoring original job integrality.

## 1. Model, workload statistics and the parameter

Use the arbitrary integral job-polymatroid model from the workload
note. All largest-size units have size a and aggregate rank f_b.
Let h=f_b(P)>0. Every other job type j has size p_j<a and rank f_j;
put u=max_j p_j, with the one-size case handled exactly if this set
is empty. Define the total possible small workload at each machine
by the singleton statistic

\[
                       W_p=\sum_{j:p_j<a}p_j f_j(\{p\}).
 \tag{P1}
\]

These rational values are obtained directly by rank queries. They
can be much larger than the actual load of any feasible schedule;
they are used only as a sufficient guaranteed-slack test.

Fix a rank budget k>=1 and a rational divisor D satisfying

\[
                         D\ge D_k:=3-2/k.
 \tag{P2}
\]

For targets a<=T<2a, let M be the unit-box cap of the largest-job
polymatroid. If its rank is h, define

\[
 F_D(T)=\{p:W_p\le T-a/D\},
 \qquad
 \delta_D(T)=h-r_M(F_D(T)).
 \tag{P3}
\]

This deficit is nonincreasing in T. The cap for budget k holds when
delta_D(T)<=k, holds automatically for T>=2a, and fails for T<a.
If the Boolean matroid has rank less than h, it fails throughout the
hard interval and first holds at 2a. Let Theta_(k,D) be the first
target passing this cap. Define

\[
                         \beta(D)=\max\{3/2,\ 2-1/D\}.
 \tag{P4}
\]

The construction below returns a legal integral schedule satisfying

\[
 \boxed{\quad
 C_{\max}\le \beta(D)\max\{\mathrm{OPT},\Theta_{k,D}\}+u.
 \quad}
 \tag{P5}
\]

For D=D_k its time is 2^{O(k)}poly(H). For D=D_k+eta, where
0<eta<=1, its time is

\[
 \operatorname{poly}(H)
 \min\{2^{O(k)},(k+1)^{O((1+\eta^{-1})\log(k+1))}\}.
 \tag{P6}
\]

All arithmetic, oracle operations, decomposition and rounding are paid
in H. The guarantee is against OPT itself when OPT passes the cap.
A failed cap does not certify original infeasibility.

## 2. An artificial quantum makes K/D an integer

Choose a common original quantum g=1/Q such that all original sizes
are integer multiples of g. Write D=A/B in lowest positive integer
terms and set

\[
                    \Delta=g/A,
 \qquad K=a/\Delta,
 \qquad b=K/D.
 \tag{P7}
\]

If a=A_0 g, then K=A_0 A and b=A_0 B are positive integers.
Every m_j=p_j/Delta is also a positive integer. Choose targets on
the finer Delta-grid, which still contains every original integral
schedule load and OPT. For all queried targets c=T/Delta is integral.

Use the workload rank

\[
                        F(S)=\sum_{j:p_j<a}m_j f_j(S).
 \tag{P8}
\]

The binary lengths of A, B, Delta and all derived ranks are polynomial
in H, including the descriptions of k and D. The scaling does not
enumerate A, K, or any job multiplicity. In particular, for the exact
choice D=D_k one may simply use Delta=g/(3k-2), even without reducing
the fraction; then K/D_k is automatically integral.

Unlike a ceiling quota, this exact quota needs no separate lower bound
on K to absorb rounding. The positive growth margin in Section 4
will follow algebraically from the excess D-D_k.

## 3. Private slack and the contracted K-unit promise

In the hard branch a<=T<2a, perform the two total-rank checks from the
workload note: cap the largest-job rank at one per machine, and cap
the workload rank F at c. Let G be the latter capped rank. A failure
of either check certifies original target infeasibility.

Dualize G to

\[
                    f(S)=c|S|+G(P\setminus S)-G(P).
 \tag{P9}
\]

The private coordinate of f at p is

\[
 \sigma_p=f(P)-f(P\setminus\{p\})
         =c-\min\{c,F(\{p\})\}.
 \tag{P10}
\]

Because b>=1 and Delta F({p})=W_p, the condition sigma_p>=b is
exactly W_p<=T-b Delta=T-a/D. Hence (P3) is the private set for
quota b, with no numerical slack in the threshold.

Choose a maximum independent F_0 subset of F_D(T) in M. Contract
F_0 only in the player matroid and restrict the dual recipient
polymatroid f to P\\F_0. Its player rank is delta_D(T).

If a target-T schedule exists, its largest-unit basis I* has K dual
workload units on every member. As I* spans M, it contains a basis
J of M/F_0 after discarding F_0. The old dual allocation restricted
to J preserves all K units per selected member. Thus the residual
core has the full K-unit promise.

After the core supplies b units on its contracted basis, add b units
at each member of F_0. This is feasible because every marginal of
f at p is at least sigma_p: any feasible vector supported off F_0
can be combined with any coordinatewise bounded vector z<=sigma
supported on F_0. The resulting selected basis of M receives b
dual workload units everywhere. If the residual rank is zero, the
private insertion itself completes the construction.

The private-coordinate lemma and basis-spanning proof are given in
Sections 2--4 of the separately reviewed private-slack scheduling note.
No original K-unit promise is assumed for F_0, and no capacity is
subtracted from the residual resource restriction.

## 4. Exact quota, finite-rank inequality and positive growth

Let r=delta_D(T)>=1 be the actual contracted rank, with r<=k. Its
unit-quota contradiction condition is

\[
                   (3-2/r)b<K+1+(r-1)/r.
 \tag{P11}
\]

Since D>=D_k>=3-2/r and D b=K, its left side is at most K.
Thus (P11) is strict for every finite r. The exact signature theorem
therefore returns b units or soundly rejects the K-unit promise in
2^{O(r)}poly(H) time.

If D=D_k+eta, write rho=(r-1)/r. The exact slack is

\[
 \begin{split}
 \Gamma
   &=K+1+\rho-(3-2/r)b\\
   &=(D-(3-2/r))b+1+\rho\\
   &\ge\eta b+1+\rho.
 \end{split}
 \tag{P12}
\]

The cover coefficient is C=2b-1. Consequently Gamma/C>eta/2.
The accepted growth argument may use, for example, gamma=eta/24.
This proves (P6) without a large-K rounding proviso. The reason is
the engineered equality D b=K; applying the same conclusion to an
arbitrary original indivisible quota would be invalid.

## 5. Reconstruction and objective bound

Extend the independent dual vector to a dual base and complement to
a workload base w. Selected largest-job machines have smaller-job
workload at most

\[
                            \Delta w_p\le T-a/D.
 \tag{P13}
\]

Decompose w into integer bases of m_j f_j, divide the jth component
by m_j, and obtain fractional original smaller-job bases. Apply the
per-machine rounding lemma proved in
`many_small_sizes_workload_independent_audit.md`; it increases each
machine's smaller-job load by at most u. Keep the largest assignment
fixed and integral.

The final load is at most T+u on other machines and at most

\[
                         T+(1-1/D)a+u
                              \le(2-1/D)T+u
 \tag{P14}
\]

on selected machines. Here D>=1, so replacing a by T is valid.
The easy branch T>=2a uses the public all-job additive rounding and
has load at most 3T/2. These two bounds give beta(D)T+u.

Both original job-polymatroid integrality and all original types are
restored. The added u is the paid difference between this workload
result and the indivisible two-size result without an additive term.

## 6. Closed-form cap threshold and correct optimization

Suppose the largest Boolean matroid has rank h. If k>=h, put
Theta_(k,D)=a. Otherwise define the bottleneck workload threshold

\[
 \lambda_k=\min\{z:r_M(\{p:W_p\le z\})\ge h-k\}.
 \tag{P15}
\]

Sorting the W_p values and using matroid greedy computes lambda_k
in polynomial time. The cap first holds at

\[
           \Theta_{k,D}=\min\{2a,\ \max\{a,\lambda_k+a/D\}\}.
 \tag{P16}
\]

If the Boolean matroid has rank less than h, define Theta_(k,D)=2a
instead. Such a failure already implies OPT>=2a, because every
smaller target would require a Boolean base of size h.

Every W_p is an integer multiple of g, and a/D=b Delta is an integer
multiple of Delta. Thus (P16) is an attained Delta-grid value. Both
the original feasibility condition and the cap are monotone in T.
The targets satisfying both begin exactly at
T*=max{OPT,Theta_(k,D)}, which is also on the Delta-grid.

Use a one-sided target procedure: genuine rank/core/LP failures prove
original infeasibility; cap failure says only T<Theta_(k,D); and
success returns a schedule of load at most beta(D)T+u. Any failure
excludes every capped feasible target at most T. Take an upper
endpoint max{V,2a}, where V is the load of arbitrary feasible bases;
this endpoint is originally feasible and passes the cap. Zero is a
failed lower endpoint when h>0. Binary search on the Delta-grid,
retaining the best actual schedule, ends with a successful target
at most T*. This proves (P5) and takes polynomially many target
calls in the bit length of the range. No monotonicity of successful
algorithm outputs is assumed.

## 7. Quantitative consequences and scope

For the exact finite-rank choice D=D_k, the coefficients are:

| Cap budget k | D_k | beta(D_k) |
|---:|---:|---:|
| 1 | 1 | 3/2 |
| 2 | 2 | 3/2 |
| 3 | 7/3 | 11/7 |
| 4 | 5/2 | 8/5 |
| 5 | 13/5 | 21/13 |
| k tending to infinity | tending to 3 | tending to 5/3 |

For k>=2 the exact formula is (5k-4)/(3k-2). For all k, the cap
threshold in (P16) belongs to that k and D; a stronger desired
coefficient requires more private slack and can increase the cap
threshold. If OPT passes this cap and u<=epsilon OPT, the displayed
coefficient plus epsilon is an approximation factor to OPT.

Taking k=h eliminates the cap restriction on originally feasible
targets and gives an exact-signature h-parameter consequence:

\[
 C_{\max}\le
 \max\{3/2,(5h-4)/(3h-2)\}\,\mathrm{OPT}+u
 \quad\text{in }2^{O(h)}\operatorname{poly}(H).
 \tag{P17}
\]

Taking D=D_k+eta gives its rank-quasipolynomial coefficient
max{3/2,2-1/(3-2/k+eta)} and the same explicit additive u.
For eta<2/k this coefficient is below 5/3. This refinement does
not prove uniform near-5/3 or near-3/2 scheduling without the
additive term, an appropriate size gap, or the displayed cap promise.

The public baseline and source status remain those in the workload
note: general job-polymatroid scheduling has a polynomial two-
approximation; ordinary two-size 5/3 estimation is an existing public
number; no exhaustive publication priority claim is made here. The
new derivation concerns the combination of exact finite-rank quota,
private-slack deficit, binary workload scaling and per-machine
integral rounding.
