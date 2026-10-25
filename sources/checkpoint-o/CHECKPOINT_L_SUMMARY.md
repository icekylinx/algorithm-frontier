# Checkpoint L: constructive scheduling transfers and computable allocation relaxations

**25 October 2026. English research checkpoint.**

The active task is to transfer the techniques to related problems.
Further work on lowering the original general-graph matching exponent
has stopped at the user's request. Its earlier 4/5 archive is retained
only as research history. This checkpoint adds results for max-min
allocation, scheduling with job polymatroids, and the fractional
relaxations underlying the allocation guarantees.

The results below have complete mathematical derivations and independent
internal reviews. They are research claims, without formal verification,
external peer review or an exhaustive publication-priority determination.
All stated algorithms are deterministic. Oracle costs and binary
arithmetic are included; numerical capacities are not expanded.

## 1. What is new and what the parameters mean

Let q denote the number of explicit potential players or machines.
In allocation, r is the rank of the player-selection matroid. In
scheduling, h is the number of largest-band job units, after their
recipient constraints are aggregated. A selectable budget k controls
the number of remaining large-job positions handled by the nonlinear
search. H pays the explicit and numerical input, supplied and derived
oracles, deterministic submodular minimization, matroid operations,
decomposition, rounding and target search.

The principal completed results are:

| Problem or interface | Guarantee | Time and scope |
|---|---|---|
| Two-size job-polymatroid scheduling | Actual schedule of makespan at most 5 OPT/3 | `2^{O(h)} poly(H)`; arbitrary integral job polymatroids |
| Two-size scheduling with k residual positions | `max(alpha_k OPT, a+lambda_k)`, with alpha_k=3/2 for k<=2 and 5/3 otherwise | `2^{O(k)} poly(H)`; lambda_k is a computed bottleneck, with no target cap |
| Arbitrarily many smaller sizes | `max(beta(D) OPT+u, a+lambda_k)` | Exact or rank-quasipolynomial dependence on k; beta(D)=max(3/2,2-1/D) |
| Several near-equal large sizes | `max(beta(D,R) OPT+u, B_k)` | Same rank dependence; beta(D,R)=max(1+R/2,2-1/(DR)) |
| Strong residual configuration LP | Factor `4-3/r` or `4-3/r+eta` comparison for the allocation algorithm | Existing rank-exponential or rank-quasipolynomial search; no LP solve required |
| Bounded-support residual LP, count-box players | Fractional target at least `(1-epsilon) OPT_LP` | `(q+1)^{O(r)} poly(H,1/epsilon)` for support `2(r-1)` |
| Full residual configuration LP | Same weak fractional optimization, and an explicit remaining gap of two | `2^{O(q)} poly(H,1/epsilon)`; gap example uses a sum of two uniform ranks |

The scheduling bounds with a bottleneck term are unconditional bounds
on each instance, but a small multiplicative approximation factor
requires that term to be sufficiently small. The many-size results
also retain the explicit +u rounding term. The public polynomial
schedule can always be run too and the better actual output returned.

## 2. The constructive two-size scheduling theorem

There are two positive job sizes u<a. Each size class is represented
by an arbitrary normalized monotone integral submodular rank function
on the machines. A schedule is an integral base of each job polymatroid.
All ranks and counts may be binary encoded. Put h=f_b(P), the total
number of a-sized units.

The new construction gives

\[
             C_{\max}\le\frac53\mathrm{OPT}
       \quad\text{in }2^{O(h)}\operatorname{poly}(H).
 \tag{L1}
\]

This is an actual integral schedule, compared with the original
integer optimum. The coefficient 5/3 already occurs in public work
on ordinary two-size restricted assignment; the contribution claimed
here is the explicit parameter dependence and arbitrary integral
job-polymatroid scope, together with the complete construction.

At a hard target `a<=T<2a`, any target-feasible schedule uses at most
one large unit per machine. The Boolean cap of the large-job rank
therefore gives a player matroid of rank h. Cap the small-job counts
at `c=floor(T/u)` and complement this capped polymatroid. A target
schedule supplies at least

\[
                  K=c-\left\lfloor\frac{T-a}{u}\right\rfloor
\]

dual units on a large-recipient basis. The exact unit allocation
theorem returns at least `ceil(K/3)` units per selected recipient.
Extend to a dual base, complement to the original small base, and
put one large unit on each selected machine. The load bound is 5T/3.
For T>=2a, classical additive rounding already gives at most 3T/2.

The finite-rank quota is more precisely

\[
       b_k(K)=\left\lfloor\frac{kK+2k-2}{3k-2}\right\rfloor.
 \tag{L2}
\]

At k=1,2 this gives a hard-branch bound at most 3T/2. At every
k>=3, the case K=3 still permits only one output unit under this
certificate. The uniform exact 5/3 bound therefore cannot be lowered
merely by ignoring the quota rounding. A fine-original-unit promise
supports the separate quasipolynomial branch recorded in the notes.

Primary manuscript: `two_size_makespan_few_large_jobs_transfer.md`.
Its independent and root audits accompany it.

## 3. A stronger rank reduction: commit positions and charge their final loads

The earlier private-slack approach required a target-dependent rank
cap. A new proof removes that cap by assigning a separate load bound
to the committed machines.

For a largest size a, define each machine's maximum possible smaller
workload from the original singleton constraints:

\[
                     W_p=\sum_{j:p_j<a}p_j f_j(\{p\}).
\]

Let M be the Boolean largest-job matroid of rank h. For a chosen
1<=k<=h, select an M-independent set F0 of h-k machines minimizing
its largest W_p. Call the optimum bottleneck lambda_k. Sorting the
W_p and matroid greedy compute the whole profile in polynomial time.

Contract F0 **only in the player matroid**, and restrict the dual
recipient polymatroid to the other machines. An optimum basis spans
the player contraction, so some contracted basis retains the full
K-unit resource promise. Run the unit core at rank k. Extend its
resource vector by zero on F0, then to a full dual base. Zero insertion
requires no private-capacity hypothesis.

After reconstruction and any smaller-job rounding, every original
job component still obeys `x_j(p)<=f_j({p})`. Thus a committed
machine's **final integral** load is at most a+W_p. No extra +u is
needed on that term. Only the other selected machines need the dual
quota and the per-machine rounding charge.

For exactly two sizes this proves

\[
 C_{\max}\le\max\{\alpha_k\mathrm{OPT},a+\lambda_k\},\qquad
 \alpha_k=\begin{cases}3/2,&k\le2,\\5/3,&k\ge3.\end{cases}
 \tag{L3}
\]

The nonlinear time is in k, even when h and q are much larger.
Lambda is already measured in workload units; it must not be
multiplied by u again. All target rejections are now genuine original
infeasibility rejections. Ordinary one-sided grid search compares
directly with OPT and needs no cap threshold in its guarantee.

If the Boolean large rank is less than h, then OPT>=2a and additive
rounding already gives a polynomial 3/2 approximation. That case is
handled separately rather than inventing a finite bottleneck.

Read `scheduling_bottleneck_commitment_rank_reduction.md` and its
three independent review notes. The earlier private-slack files are
retained because they give a useful intermediate theorem and its
precise capped-target search; the new commitment bound is stronger.

## 4. Arbitrarily many small sizes and exact finite-rank coefficients

Let u be the largest job size strictly below the largest size a.
All smaller types may have different sizes and arbitrary integral
job-polymatroid constraints. Aggregate their workload as

\[
                      F(S)=\sum_{j:p_j<a}(p_j/\Delta)f_j(S),
\]

where Delta is a fine rational quantum. This is an integral
polymatroid with binary ranks. Its units are conceptual workload,
not indivisible original jobs.

Choose rational `D>=D_k=3-2/k`. Writing D=A/B and setting
`Delta=g/A`, for an original value quantum g, makes both
`K=a/Delta` and `b=K/D` integral. At actual core rank k,
`D_k b<=K` satisfies the strict unit quota condition. For
`D=D_k+eta`, the relative growth slack exceeds eta/2, with no
original-small-unit assumption.

Decompose the returned workload base into scaled original components
and divide by their scaling factors. These are fractional original
job bases. A direct integral-polymatroid-intersection construction
then rounds them with load increase at most u **on each machine**.
This is why the following additive term must remain:

\[
 C_{\max}\le
 \max\left\{\max\{3/2,2-1/D\}\mathrm{OPT}+u,
             a+\lambda_k\right\}.
 \tag{L4}
\]

At exact D_k, the coefficients are 3/2 for k=1,2, 11/7 for k=3,
8/5 for k=4, and `(5k-4)/(3k-2)` for k>=2. The time is
`2^{O(k)} poly(H)`. At `D=D_k+eta`, it is

\[
 \operatorname{poly}(H)
 \min\{2^{O(k)},(k+1)^{O((1+\eta^{-1})\log(k+1))}\}.
 \tag{L5}
\]

Artificial subdivision makes the fractional quota convenient, but
cannot erase the +u needed to restore original job integrality.
When u<=epsilon OPT and the bottleneck term is inactive, this gives
the displayed coefficient plus epsilon as a multiplicative ratio.

The per-machine rounding proof uses a polynomial ground set of
machine/type pairs and nested ceiling bounds on sorted job counts.
It does not expand binary multiplicities. See
`many_small_sizes_workload_makespan_transfer.md`, its two audits,
and `many_small_sizes_private_slack_deficiency.md` for the exact
finite-rank quota calculation.

## 5. Several near-equal large sizes

The largest band may itself contain many sizes. Let a_- and a_+ be
its actual minimum and maximum positive-rank sizes, let
`R=a_+/a_-<2`, and let every remaining size be at most u<a_-.
The Boolean matroid now comes from aggregating all large types.

At a feasible hard target `a_+<=T<2a_-`, a machine receives at most
one large unit, and its dual promise is at least a_-/Delta. The final
large unit may have size as large as a_+. This gives

\[
 \beta(D,R)=\max\{1+R/2,2-1/(DR)\}.
\]

For a sharper bottleneck, let a_p be the largest large size with
positive singleton capacity at machine p, and assign it cost
`C_p=W_p+a_p`. Select h-k independent positions minimizing their
maximum C_p; call this value B_k. Do not fix their individual large
types in advance. The final aggregate basis is decomposed into
original type bases only after its positions have been chosen.

The schedule satisfies

\[
                   C_{\max}\le
                    \max\{\beta(D,R)\mathrm{OPT}+u,B_k\}
 \tag{L6}
\]

with the same exact or positive-error rank dependence. At k=0,
balancing the smaller workload independently gives the polynomial
endpoint `max(OPT+u,B_0)`. A single greedy order supplies the
bottleneck profile, and all top-size suffixes can be tried in
polynomially many band choices.

For `D=3+eta`, `R<=1+tau`, and `u<=epsilon OPT`, the full-rank
choice k=h yields ratio at most

\[
                    \frac53+\frac\eta9+\frac\tau3+\epsilon.
 \tag{L7}
\]

This is a stated size-band regime. The public ordinary restricted-
assignment algorithm of Jansen--Rohwedder gives an unconditional
constructive `11/6+epsilon` in quasipolynomial time. The new bound
improves that number in suitable banded regimes and has the broader
oracle job-polymatroid model; it does not dominate the public theorem
on every instance. Enumerating all h large placements gives the
stronger-quality `OPT+u` baseline in `q^{O(h)}` time, with an exponent
depending on h. That XP baseline is also retained explicitly.

Read `near_equal_large_sizes_bottleneck_makespan_draft.md` and its
root and independent audits. The historical draft filename is retained;
its stated theorem has passed the recorded internal reviews.

## 6. Strengthening the allocation comparator

For arbitrary recipient polymatroids, the simple aggregate
configuration LP can have a gap growing with r. A new valid cut family
restores the comparison used by the allocation algorithm. For a
resource rank f_j and subset S, put

\[
 m_{pj}(S)=f_j(S\cup\{p\})-f_j(S).
\]

The strengthened configuration relaxation includes

\[
 \sum_{p,n}\mu_{pn}(n_j-m_{pj}(S))_+\le f_j(S).
 \tag{L8}
\]

These cuts are valid for every integral allocation. They are exactly
equivalent to the earlier family indexed by all feasible integral
reserve vectors. The proof views violation as a convex function of
the reserve; its maximum occurs at a greedy polymatroid vertex, which
spans the copy blocks of a subset S and gives precisely the displayed
marginals. Reserving at most s player coordinates is exactly equivalent
to imposing only cuts with |S|<=s.

The algorithm's normalized states need only s=2(r-1). The existing
factor `4-3/r`, or `4-3/r+eta`, now holds against this stronger
configuration comparator as proved in the residual-cut note. The
algorithm itself does not solve the LP. Scaled matroid components keep
their already proved separate-component comparator.

Read `recipient_polymatroid_residual_configuration_relaxation.md`,
`recipient_polymatroid_subset_cut_compression.md`, and their root and
independent reviews. The fat-cover-deficit parameter theorem in
`fat_deficiency_parameter_allocation.md` supplies an additional
rank reduction with its explicitly capped maximization guarantee.

## 7. The new LP benchmark can be computed

When a player's local configurations are integer coordinate boxes,
the full strengthened LP admits a weak fractional optimizer in
`2^{O(q)} poly(H,1/epsilon)`. More strongly, an arbitrary explicitly
retained list of m residual cuts admits one in
`poly(H,m,1/epsilon)` while keeping all aggregate resource and
player-base constraints implicit.

The latter procedure uses support optimization of
`B(M) times product_j P(f_j)` by greedy. A compact Farkas formulation
has signed aggregate prices and nonnegative hinge prices. Each local
pricing problem is convex in the counts. Its nonpositive marginal-cost
prefix can be selected first, leaving a binary knapsack with positive
costs and an exact shifted budget. Profit scaling loses only objective
value. An exact rational cost grid enforces strict dual violations.

A positive direction in this particular split-variable dual gives
a uniform interior ball whenever a finite primal is infeasible.
Ellipsoid volume exhaustion, retaining both generated configurations
and actual aggregate vertices, then extracts a feasible explicit
finite primal. This avoids an unproved lower-dimensional certification
step or a hidden second implicit LP.

For all cuts with support at most `2(r-1)`, the result is

\[
 (q+1)^{O(r)}\operatorname{poly}(H,\epsilon^{-1}),
 \qquad\text{value at least }(1-\epsilon)\mathrm{OPT}_{LP}.
 \tag{L9}
\]

This is an XP computation of the sufficient support-restricted
relaxation, not an FPT optimizer and not optimization of the full
cut family in rank-XP time. Output space is polynomial in the listed
cut count, which can be larger than the original input. The result
is fractional and does not remove the integer approximation loss.

The pricing proof also permits nonnegative player-dependent linear
values in this fractional computation. The allocation factor-four
theorem still requires common intrinsic resource values.

Read `residual_configuration_bounded_support_xp_solver.md` and its
two audits. The earlier fully enumerated-row solver and its audits
are included as a separate, simpler proof path.

## 8. Remaining limits are proved or explicitly left open

Even every residual cut together leaves a gap of two. For r>=3,
take 2r players, player matroid U_(r,2r), and one unit-valued rank

\[
                  f(S)=\min(|S|,r-1)+\min(|S|,r+1).
\]

Every integer basis can receive one unit per player, but cannot
receive two because its r-set rank is 2r-1. Putting mass 1/2 on
each player's two-unit configuration satisfies all subset cuts and
has LP target two. The full residual LP therefore has optimum two
while integer OPT is one. If the two uniform components are retained
as distinct one-service resources, their configuration LP has optimum
one. Residual cuts do not recover every detail lost by merging them.
See `full_residual_configuration_gap_two.md` and its audit.

There are also separate value-oracle lower bounds: arbitrary-recipient
allocation below factor two and two-size job-polymatroid scheduling
below factor 3/2 require `binom(q,r)-1` or `binom(q,h)-1` queries
on the explicit hidden-set families. These bounds concern the oracle
model, not ordinary explicitly listed restricted-assignment jobs.
They do not rule out the critical four-unit to two-unit promise.

The unit-core global-free-pool lemma shows that a stalled critical
state has globally resource-free owners of rank at least the current
player-rank deficit. Owners outside the unmarked player span permit
an immediately paid augmentation or marked exchange. If all free
owners lie inside that span, exchanges may preserve the old signature
without decreasing it. A new bounded progress argument is still
needed for a uniform polynomial or rank-quasipolynomial four-to-two
algorithm. The checkpoint does not claim that gate has been closed.

A fresh adversarial audit also supplies a reachable six-player
collapse history. If normalization checks only the center whose
group changed, it misses a different center that has become free:
the weighted cover would be 63 while its claimed bound is only 58.
The specified algorithm's all-center scan catches this state before
any charge and augments. A separate linear countermodel shows why
rank additivity must hold inside layers, not just at their boundaries.
The audit rederives old maximality, same-owner record handling and
every charged signature event. See
`prefix_core_adversarial_collapse_audit.md`. These counterexamples
invalidate weakened variants and substantiate the precise operations
required by the current proof.

## 9. Current public sources and proof status

The primary-source recheck distinguishes the following results:

* [BLMRS, arXiv:2307.08453v1](https://arxiv.org/html/2307.08453v1),
  Theorem 4: polynomial `8+epsilon` for general recipient-polymatroid
  values and `4+epsilon` for two values; Corollary 5: `7/4+epsilon`
  for two-size job-polymatroid scheduling; Theorem 23: largest-job
  additive rounding. Its official history currently lists only v1.
* [DRZ, arXiv:1807.07189v4](https://arxiv.org/html/1807.07189v4),
  4 January 2026: the corrected compact player-matroid guarantee is
  one-fifth and its Santa Claus corollary is `6+epsilon`. The older
  one-third / four claim was v2; v3 already contained the correction.
* [Cheng--Mao, arXiv:1905.06084](https://arxiv.org/abs/1905.06084):
  independent polynomial `4+delta` for ordinary restricted Santa
  Claus. The DRZ correction does not change this separate baseline.
* [Jansen--Land--Maack, SWAT 2016](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.SWAT.2016.24):
  ordinary two-size 5/3 estimation and configuration-LP gap. The
  checked 2025 Sengupta thesis abstract additionally reports a
  nonpolynomial constructive 5/3 local search; its full thesis was
  not accessed and is not treated as fully reviewed.
* [Jansen--Rohwedder, arXiv:1701.07208v2](https://arxiv.org/html/1701.07208v2):
  constructive `11/6+epsilon` for ordinary restricted assignment
  in quasipolynomial time.

The detailed version/dependency inspection is in
`current_public_version_and_dependency_recheck.md`. The new prefix
algorithm maintains current invariants and revisits retained centers;
it does not import the corrected DRZ birth-time growth assertion.
Its larger runtime regime is stated throughout. The scheduling
rounding and LP extraction interfaces have independent direct proofs.

The ZIP contains English Markdown research notes and a hash manifest.
No Lean, PDF, implementation or test bundle is included. Earlier
checkpoint material is preserved for provenance; this summary and
the new reviewed manuscripts identify the current claims.
