# Deterministic algorithm research: allocation and scheduling transfers

**Checkpoint Q — 25 October 2026. English research notes.**

## Start here: checkpoint Q

Read CHECKPOINT_Q_SUMMARY.md for deterministic arbitrary-accuracy
allocation and scheduling with full recipient-polymatroid constraints,
binary counts, exact scalar budgets and polynomial workspace. The
allocation scheme permits an actual optional player basis and shared
setup/assignment fees; its time is binom(q,r) exp(O(r/epsilon)) times
polynomial work. The scheduling scheme preserves every original job
base and has time 2^{O(q/epsilon)} times polynomial work. Machine
activation with a shared setup/assignment budget is separately proved.

For arbitrary processing times the explicit curve includes 5/3 in
2^q, 11/7 in 3^q and exact 3/2 in 6^q. With two positive processing
times per machine, the pair may vary between machines and the exact
3/2 guarantee has base 50/27 with the stated subexponential overhead.

The robust results include guarded bounded-obstruction unit gates,
the width-two Fibonacci improvement, a common-setup additive theorem,
and two distinct whole-ground/corank impossibility boundaries. The
root audit and independent full reviews state each result's scope.
The primary baseline note credits existing ordinary approximation
schemes and exact-cost rounding; no first-scheme or formal/external
verification claim is made. Full accuracy encoding is charged.

The Q documents govern current accepted claims. Earlier start sections
and checkpoints below are retained as history. New manuscripts still
awaiting complete review are not part of the frozen Q result ledger.
The historical matching 4/5 exponent remains outside the active target.

## Start here: checkpoint P

Read CHECKPOINT_P_SUMMARY.md for the accepted arbitrary unrelated-value
allocation theorem with an optional original player-matroid basis and
one exact shared budget for setup and assignment costs. Fixed factor
2+eta has the explicit whole-player base below two; exact factor two
has a separate 2^q polynomial-space endpoint. Pair masks share the
original resources and the persistent zero-service dummy preserves
setup credits through integral recovery.

The new quota tradeoffs cover optional one-value allocation with that
same shared budget, compulsory unrelated two-valued allocation, and
the separately scoped two-size scheduling model. Actual sparse
separators yield smaller proved bases, including the golden-ratio
corank bound for the stated support-three packing application.

Robust integer unit allocation now has both a positive high-quota
result and an explicit low-quota Hitting Set obstruction. Multiple
exact budgets on one integer allocation have a separate hardness
boundary. The public baseline audit explicitly credits the existing
ordinary unrelated player-parameterized approximation scheme.

The P summary, full manuscripts and recorded root/independent reviews
govern current claims. The retained O and earlier sections below are
historical snapshots. The original matching 4/5 exponent is not an
active optimization target. No publication-priority or formal/external
verification claim is made.

## Start here: checkpoint O

Read CHECKPOINT_O_SUMMARY.md for the all-instance global allocation,
scheduling and selected-flow theorems. Arbitrary assignment costs now
require no proportionality or price-diversity assumption. Exact
factor-two one-value optional-basis allocation and compulsory
two-value allocation, and exact three-halves two-size scheduling,
have deterministic time (50/27)^(q+o(q)) poly(H) and polynomial space.

General intrinsic-value allocation with an original player matroid
and one exact cost budget has factor 2+eta at the explicitly stated
global base; factors 4, 3 and 5/2 have bases 7/4, 50/27 and
5994/3125. Every support cardinality is processed, so no small-corank
or heavy-support promise remains in these whole-ground statements.

Selected splittable flow, explicit robust scenarios and a shared
setup/routing budget have relative-loss algorithms with exact routing
constraints. A rational-comparator recovery removes an extra accuracy
loss. The archive distinguishes the known monotone-local-search base
formula from the separately proved polynomial-space construction and
application interfaces.

The O summary and its root/independent audits govern the new claims.
All retained earlier sections are historical. The original matching
4/5 result is not being optimized. Stronger unrelated-value transfers
remain separately under investigation and are not assumed by O.

## Start here: checkpoint N

Read `CHECKPOINT_N_SUMMARY.md` for the accepted weighted corank
selection theorem and its new allocation and scheduling transfers.
The weighted first-crossing method handles arbitrary nonnegative
rational packing rows in `Gamma(t/(t-b))^c poly(H)` deterministic
time, with a polynomial restriction selector and polynomial space.

The new applications include arbitrary intrinsic-value allocation
with an arbitrary selected player-matroid basis at factor `2+eta`
under a precisely defined derived-corank bound; unrelated values
with pointwise additive loss of one largest unit; the same additive
guarantee under one exact assignment-cost budget; exact-cost common
bases with capacity augmentation; and a compressed largest-job-slot
scheduling bound `(1+epsilon)OPT+u` with binary multiplicities.

All parameters, comparators, additive terms and model restrictions
are stated in the N summary. The exact-two general-value FPT gate
remains open, with proved zero-corank, XP and separated-value cases.
The ordinary Santa Claus source update distinguishes a newer
university announcement from a complete checked algorithm proof.
No first-publication claim is made.

Checkpoint M's exact factor-two and three-halves results remain
accepted. The original matching 4/5 direction remains historical
and is not being optimized. The following sections preserve earlier
chronology; the N summary and named audits govern the current claims.

## Start here: checkpoint M

Read `CHECKPOINT_M_SUMMARY.md` for the new single-exponential corank
algorithms and their complete review status. The new core gives a
four-unit-promise/two-unit-output basis in `4^c poly(H)` time. It
also gives exact factor-two unit-value allocation and exact
three-halves two-size job-polymatroid scheduling in
`(27/4)^c poly(H)` time, with polynomial workspace. A further
composition gives exact factor-two compulsory-player two-value
allocation in `(27/4)^nu poly(H)`, where nu is the large-cover rank.

Self-contained value-oracle lower bounds match these approximation
thresholds in their stated parameterizations. They do not prove
optimal exponential bases or explicit-input hardness. The full
proofs and two independent core audits are accompanied by
`corank_batch_allocation_scheduling_root_audit.md`.

This snapshot also accepts local eligibility padding, actual large
collision thresholds, and safe full-machine contraction. Their
bottleneck terms, additive losses, and public comparison limits are
stated in the M summary. The active direction remains entirely
related optimization problems; the original matching 4/5 result is
history and no attempt to lower it is made.

The following sections preserve checkpoint L and earlier chronology.
Their earlier best-result language is superseded by the M summary
only in the precise corank and large-cover regimes stated above.

## Start here: checkpoint L

Read `CHECKPOINT_L_SUMMARY.md` for the current results, proof ideas,
time and model distinctions, source-version audit, and remaining gates.
The active direction is entirely the transfer to related problems.
The original general-graph matching 4/5 research bound is retained
as history; no further lowering of that exponent is attempted here.

The main new constructive theorem is a deterministic 5/3 approximation
for two-size scheduling with arbitrary integral job polymatroids in
`2^{O(h)} poly(H)` time, where h is the number of large job units.
A stronger bottleneck commitment theorem reduces the searched rank
to a selectable budget k and gives

\[
 C_{\max}\le\max\{\alpha_k\mathrm{OPT},a+\lambda_k\},\qquad
 \alpha_k=\begin{cases}3/2,&k\le2,\\5/3,&k\ge3.\end{cases}
\]

Here lambda_k is a polynomially computed workload bottleneck for
h-k committed independent machines. This guarantee uses original
OPT, with no target cap. It is a small constant approximation when
the separate commitment term is sufficiently small. The algorithm
can always return the better public polynomial schedule too.

For arbitrarily many smaller sizes, a workload construction supplies
the bound `max(beta(D) OPT+u,a+lambda_k)`, where u is the maximum
smaller size and `beta(D)=max(3/2,2-1/D)`. At `D=3-2/k` the
coefficient is 11/7 for k=3 and 8/5 for k=4; the explicit +u remains.
At `D=3-2/k+eta`, the nonlinear time becomes rank quasipolynomial.
A further reviewed extension handles near-equal heterogeneous large
bands and a sharper machine-eligibility bottleneck B_k.

The general-recipient allocation comparator is also stronger than in
K: valid residual configuration cuts recover the factor-four bound
against a specified strengthened LP. These cuts are exactly equivalent
to subset-marginal cuts. The support `2(r-1)` sufficient for the
algorithm admits a fractional weak optimizer in
`(q+1)^{O(r)} poly(H,1/epsilon)` for count-box players; the full LP
admits `2^{O(q)} poly(H,1/epsilon)` computation. These are fractional
results, not integer approximation schemes. An explicit gap of two
survives all residual cuts and is included with an independent audit.

Recommended reading order:

1. `CHECKPOINT_L_SUMMARY.md` — all current theorem statements and limits.
2. `two_size_makespan_few_large_jobs_transfer.md` and
   `scheduling_bottleneck_commitment_rank_reduction.md` — the principal
   exact scheduling transfers and their accompanying audits.
3. `many_small_sizes_workload_makespan_transfer.md`,
   `many_small_sizes_private_slack_deficiency.md`, and
   `near_equal_large_sizes_bottleneck_makespan_draft.md` — the workload,
   finite-rank and heterogeneous-band extensions. The historical draft
   filename is retained despite its completed internal reviews.
4. `recipient_polymatroid_residual_configuration_relaxation.md` and
   `recipient_polymatroid_subset_cut_compression.md` — the stronger
   allocation comparator and exact reserve/subset equivalence.
5. `residual_configuration_bounded_support_xp_solver.md` and its root
   and independent audits — the compact dual and complete fractional
   optimization procedure.
6. `full_residual_configuration_gap_two.md`,
   `recipient_polymatroid_below_two_oracle_barrier.md`, and
   `critical_unit_quota_global_free_pool.md` — comparator limits,
   oracle limits and the precisely unresolved small-quota time gate.
7. `current_public_version_and_dependency_recheck.md` — current primary
   versions and which public ingredients the new proofs actually use.
8. `prefix_core_adversarial_collapse_audit.md` — a fresh adversarial
   review of collapse, all-center normalization, every internal prefix,
   same-owner records and exact-signature time, including explicit
   counterexamples to two tempting weakened variants.

Current source comparison distinguishes the corrected DRZ v3/v4
one-fifth / six route from its superseded v2 one-third / four claim.
Ordinary restricted Santa Claus independently has polynomial
`4+delta` via Cheng--Mao. BLMRS's own stated recipient-polymatroid
8/4 and two-size scheduling 7/4 theorems remain separate baselines.
All quality improvements here retain their different time regimes,
model scopes, comparator restrictions and additive losses.

The remaining sections preserve previous checkpoints. In particular,
K's integer-only row for arbitrary recipient polymatroids is extended
by the newly proved residual-LP comparator; its rejection of the
weaker aggregate LP remains correct. All results are internally
reviewed research derivations, not external peer review or formal
verification. The deliverable has English Markdown and a manifest,
with no Lean, PDF, implementation or test bundle.

## New in checkpoint K: factor four for general recipient polymatroids

The active research direction is now the transfer to related problems.
At the user's request, further attempts to lower the original general-
matching exponent have stopped. Its previous 4/5 research bound remains
unchanged. The material below records a substantial improvement in the
separate max-min allocation problem, with the original matching archive
retained for provenance.

### Principal theorem and comparison guarantees

Choose a basis of an arbitrary player-selection matroid M of rank r.
For each resource type j, legal integral recipient counts satisfy an
arbitrary integral polymatroid rank function f_j on the players. Unit
values are common intrinsic nonnegative rationals. Capacities and output
counts are binary; resource rank functions are supplied by value oracles.
No recipient rank bound, decomposition into matroids, explicit copy
universe, laminar representation, or linear representation is assumed.

Let H pay the full explicit and numerical input, original and derived
oracle costs, deterministic submodular minimization, and target search.
For exact available-bundle optimization and r>=1, the internally reviewed
result is

\[
 \boxed{\text{factor }4-3/r\text{ in }
                    2^{O(r)}\operatorname{poly}(H)}
 \tag{K1}
\]

or, for any positive rational eta,

\[
 \boxed{\text{factor }4-3/r+\eta\text{ in }
 \operatorname{poly}(H)
 \min\{2^{O(r)},(r+1)^{O((1+\eta^{-1})\log(r+1))}\}.}
 \tag{K2}
\]

Space is polynomial, plus supplied oracle workspace. The number q of
potential players can be much larger than the selected rank r. The
factor tends to four with growing rank; it is not a uniform constant
strictly below four. A paid lambda-approximate local available-count
oracle replaces 4-3/r by lambda^-1+3-3/r. Such a local family must be
downward closed and its availability interface explicitly justified.

The comparison guarantee depends on the resource model:

| Resource model | Comparator for (K1)--(K2) | Numerical representation |
|---|---|---|
| Arbitrary recipient matroids, one service per player-resource pair | Coupled configuration LP | Explicit resource bundles |
| Supplied type j with f_j=c_j r_Rj, arbitrary matroid R_j and binary c_j | Separate-component count-configuration LP | Polynomial count state; no copy-pattern table |
| Arbitrary integral recipient polymatroids | Integer optimum | Polynomial count state and paid submodular minimization |

The last row intentionally has a different comparator. A natural
aggregate polymatroid configuration LP can have a gap tending to r;
the explicit construction and its proof are part of this checkpoint.
It is therefore incorrect to claim that its fractional comparison
follows from the new integer-optimum theorem.

### What changed mathematically

The new search maintains rank additivity for **every ordered center
prefix**, including prefixes ending inside a layer. Its unmarked current
matching copies are independent after contracting the selected and
designated prefix. A new center marks all unmarked records at resources
where its whole service block is dependent on the full current matching
and selected state.

A stored center whose block has become independent over its preceding
prefix and current group is now processed immediately as strongly free.
The prefix invariant proves that it is independent over the actual
matching and every retained earlier center. Eager release is an ordinary
earliest player-circuit exchange with truncation, so the previous integer
signature still decreases. It is not a standalone deletion of a center
or a free reassignment of blockers.

After this normalization every surviving center has a **current** rank
dependency. Telescoping the rank cover over the ordered prefixes saves
one shared resource value for a singleton blocker group, and pays larger
groups by their size. The resulting sharp coefficient is

\[
 \Phi\le\max\{u,2B+\min(u,B)\}|Y|,
 \tag{K3}
\]

which leads to (K1)--(K2). The earlier birth-time-saving shortcut is
explicitly refuted by a legal operation history; the new algorithm
repairs precisely the missing current-invariant step.

For arbitrary polymatroids, the natural matroid is only conceptual.
Its rank on count vector z is min_S[f_j(S)+z(P-S)]. The whole-block
available count is its rank increment on adding all copies of one
player. A contraction-and-box argument removes at most the reserved
rank from a fixed integral optimum at each resource. This recovers the
needed lower cover while avoiding the invalid aggregate-LP argument.

For a scaled recipient matroid f=c r_R, a separate fractional lemma
restores the stronger comparison: for every independent I of R,
sum_{p in I}(c-a_p)<=rank(W), where a_p is residual availability.
Convex combination with y/c in P_I(R) pays the fractional loss. The
algorithm still stores only binary record counts, so this theorem has
no recipient-rank or exponential copy-pattern surcharge.

### Reading order and audit status

1. `general_resource_prefix_additivity_four_candidate.md` — the main
   recipient-matroid factor-four construction. Its historical filename
   is retained; root and independent mathematical reviews now pass.
2. `general_resource_prefix_additivity_root_audit.md` and
   `general_resource_prefix_additivity_independent_audit.md` — detailed
   independent checks of every internal prefix, current rank saving,
   eager exchange, old maximality, and progress.
3. `general_recipient_polymatroid_integer_optimum_transfer.md` — the
   compressed natural-matroid implementation and integer loss lemma;
   its preliminary factor five is superseded by the next note.
4. `general_recipient_polymatroid_prefix_four_transfer.md` — whole-block
   prefix normalization, the factor-four theorem, and the precise unit
   quota consequence.
5. `general_recipient_polymatroid_root_audit.md`,
   `general_recipient_polymatroid_independent_audit.md`, and
   `general_recipient_polymatroid_prefix_four_independent_audit.md` —
   independent reviews of the numerical representation, loss bound,
   prefix refinement, fat wrapper, and integer arithmetic.
6. `scaled_recipient_matroids_binary_configuration_transfer.md` and its
   two configuration audits — the binary supplied-copy model with its
   stronger fractional comparator and unchanged rank-quasipolynomial time.
7. `recipient_polymatroid_aggregate_configuration_gap.md` and
   `general_resource_birth_saving_current_cover_obstruction.md` — the
   two explicit obstructions that delimit and motivate the new proof.

These are internally reviewed research derivations, with complete
proofs and paid interfaces. They have not received external peer review
or formal verification. The deliverable contains English Markdown
research notes and a manifest, with no Lean, PDF, implementation, or
test bundle.

### Public baseline and limits of downstream claims

The checked Bamas--Lindermayr--Megow--Rohwedder--Schloeter
[Theorem 4](https://arxiv.org/html/2307.08453v1) gives polynomial
8+epsilon for general recipient matroid/polymatroid allocation and
polynomial 4+epsilon for two values. Its dual dummy-resource adapter
supplies the integer guarantee for arbitrary player selection. The
new general theorem improves approximation quality in a different time
regime; it does not retain the public polynomial runtime. Ordinary
physical-item quasipolynomial factor four is already public and is
not claimed as a new result here. No exhaustive priority claim is made.

For equal unit values the new current charge is 2b-1 for bundle quota
b. Together with exact integer failed-scan values, this proves output
ceil(t/3) from an integer target t in rank-exponential time. It does
not automatically imply a uniform near-three quasipolynomial result:
t=4 and b=2 leave a margin of only 3/r. Two-value and makespan transfers
must keep that arithmetic and their stronger derived special-case
baselines explicit. They are not substituted for the general result.

The remaining sections preserve the earlier checkpoints as research
history. Their factor-five headlines and former exclusion of general
recipient polymatroids are superseded by the reviewed K results above.

## New in checkpoint J: arbitrary recipient matroids

The original goal remains deterministic exact maximum-cardinality
matching on arbitrary general graphs. Its accepted research bound is
still

\[
 O(n+m)+(m_s+1)\exp O\!\left(
   (\log(m_s+2))^{4/5}(\log\log(m_s+4))^{1/5}\right).
\]

The new principal result is a transfer to a second problem. Both sides
now have arbitrary matroid constraints: choose a basis of a player
matroid M, and for every resource j require its receiving-player set
to be independent in its own arbitrary matroid R_j. Resources have
common intrinsic rational values and may each serve multiple players,
with at most one service per player-resource pair. All matroids are
accessed by independence oracles. No laminarity, transversal slot
representation, small recipient rank or vector representation is
assumed in the principal theorem.

Let r>=1 be the player-matroid rank, H the full input and numerical
encoding, and eta>0. The internally reviewed result is

\[
 \boxed{\text{factor }5-4/r\text{ in }
          2^{O(r)}\operatorname{poly}(H)}
 \tag{J1}
\]

and

\[
 \boxed{\text{factor }5-4/r+\eta\text{ in }
 \operatorname{poly}(H)
 \min\{2^{O(r)},(r+1)^{O((1+\eta^{-1})\log(r+1))}\}.}
 \tag{J2}
\]

The guarantee compares against the natural coupled configuration LP,
without solving it or enumerating its configurations. The number q
of potential players can greatly exceed r. Original matroid, derived
dual/union, decomposition and target-search costs are all paid. Rank
one is exact in the unrestricted available-bundle model. The finite-rank
factor tends to five; it is not a uniform constant below five at
unbounded ranks.

### The step that removes the apparent exponential resource oracle

The central invariant reserves capacity for every subset of selected
centers after removing its own designated blocker groups. Initially
this suggested an explicit 2^r subset enumeration. The new completion
rule instead designates all currently unmarked matching bundles as
conservative blockers of a new center. After removing them, every old
reservation consists only of receivers in X_j union Y_j. The new
owner is chosen outside that resource closure, so every reservation
extends independently at once.

This is an inductive proof of a universal property. The algorithm
never enumerates its subsets. When a group's last blocker disappears,
the same invariant proves its center is free jointly with all
retained centers. Earliest player-circuit exchange preserves lower
player flats, and the lower resource-closure inputs remain literally
unchanged. These facts repair the hidden-new-blocker failure of a
naive resource-circuit transfer.

Artificial blockers need not share a resource with their center.
The main proof therefore uses the honest coarse charge
Phi(X,Y)<=sum v(X)+sum v(Y)<=2(B+u)|Y|. This suffices for (J1)--(J2)
after the fat-resource matroid-union reduction. It does not silently
import the sharper physical-item star coefficient.

Primary reading order:

1. `general_resource_all_remaining_blockers.md` — model, algorithm,
   universal reservations, strict cover, time, fat reduction and LP.
2. `general_resource_all_remaining_root_audit.md` — main root review.
3. `general_resource_all_remaining_blockers_exchange_audit.md` —
   independent record-level exchange, cascade and signature review.
4. `general_resource_all_remaining_source_audit.md` — independent
   proof and source-interface review.
5. `general_resource_relevant_blocker_addendum.md` and
   `general_resource_relevant_blocker_source_audit.md` — a more
   selective completion recovers the sharp compact coefficient
   without subset enumeration; the main arbitrary-size factor stays five.
6. `general_resource_matroid_public_parameter_comparison.md` —
   named public comparison, special cases and limits of retuning.

### Public comparison and proof status

Bamas, Lindermayr, Megow, Rohwedder and Schloeter,
[arXiv:2307.08453v1, Theorem 4](https://arxiv.org/html/2307.08453v1),
give polynomial 8+epsilon for general resource matroids and
polymatroids, and polynomial 4+epsilon for two values. Adding a large
dual-player-matroid resource gives a named public polynomial
8+epsilon consequence for arbitrary player selection as well. Thus
(J2) improves the quality in a different time regime; it is not the
first constant approximation or a polynomial-time domination claim.
The public unit-value selection and all-player two-value special cases
can be stronger. Ordinary all-player allocation also has public
parameterized approximation schemes in the number of player types.

The comparison checks the source's certificate and value-reduction
constants, not only its abstract. A pure slowdown or direct
overprovisioning retuning of the named positive certificate does not
give the near-five bound. No directly matching public theorem was
verified in that source search, but exhaustive publication priority
is not asserted.

The new results have internal root and independent mathematical
reviews, with assumptions and imports recorded. They have not received
formal verification or external peer review. The ZIP contains English
research notes and the manifest, including failed routes and their
corrected scope. No Lean, PDF, implementation or test bundle is supplied.

### Further completed extensions in this checkpoint

| Resource model | Available-bundle interface | Reviewed factor before positive error |
|---|---|---|
| Ordinary physical items, arbitrary selection M | Exact player-local downward-closed optimization | 4-3/r |
| Ordinary physical items, arbitrary selection M | Certified lambda-approximate local optimization | lambda^-1+3-3/r |
| Binary supplies with type-symmetric local count families | Exact or lambda-approximate count oracle | lambda^-1+3-3/r |
| Arbitrary recipient matroids and arbitrary selection M | Exact or lambda-approximate local optimization | lambda^-1+4-4/r |

Each row has an exact-boundary rank-exponential branch and its stated
positive-error rank-quasipolynomial branch. Oracle runtime, precision
and workspace are paid. A guarantee relative to an approximate oracle
uses that oracle's proved approximation contract.

The binary representation has no dependence on the expanded number
of units. A player's own integral polymatroid over types has an exact
available oracle via box-restricted polymatroid greedy and deterministic
submodular minimization. Binary bounded knapsack has the stated
profit-scaling approximate oracle. These player-local constraints are
different from a resource polymatroid on recipient counts.

Supporting files include the local, capacity and approximate-oracle
notes and audits; `type_symmetric_downward_closed_binary_allocation.md`;
`type_symmetric_binary_allocation_independent_audit.md`; and
`laminar_and_symmetric_counts_root_audit.md`. The laminar token
construction is a complete alternative representation, now within
the broader general-recipient theorem. The explicit subset algorithm
remains valid. The relevant-blocker refinement also recovers its sharp
compact certificate without enumerating subsets. Its earlier
enumeration cost is not a lower bound or a remaining requirement of
the principal algorithm.

### Matching progress and the remaining general-support gate

The exact forest and feedback-edge numerical clients from checkpoint I
remain valid. New notes give a finite signed-witness bucket structure
on a supplied bounded-interface edge-partition hierarchy. Old path
tags are pushed through old composition maps before witness changes;
new groups are rebuilt from child groups without materializing long
paths. This gives a complete static parameterized client with paid
exponential width dependence, not a general-graph exponent improvement.

The forestification audit now includes a valid strong two-incidence
numerical step after which every margin-preserving forestification
has linear additional allocation-log motion. A separate tree-supported
example disproves a universal constant heavy-edge threshold preserving
a row matching. These are explicit barriers to proposed accounting
shortcuts, not lower bounds against every pivot policy. Their proofs
and physical matching scopes are recorded in
`forest_pivots_and_bounded_witness_root_audit.md` and its source notes.

The remaining main matching task is to pay for general-support route
discovery and all resulting numerical/structural updates. The resource
allocation transfer does not discharge that task. Integer recipient
polymatroids with multiple services per player are also outside the
new general-resource theorem unless separately proved.

## New in checkpoint I: rank-sensitive matroid allocation

The original goal remains deterministic exact maximum matching in
arbitrary general graphs. Its accepted research exponent is still
**4/5**. The main new transfer in this checkpoint concerns a different
general selection problem: max-min resource allocation to a basis of
an arbitrary player matroid. The matroid is given by an independence
oracle, and resources have intrinsic values with arbitrary explicit
player liking sets. Their values need not be small or equal.

Let r be the player-matroid rank, q the number of eligible players,
P the explicit input volume, and OPT the original integral optimum.
The completed matroid-union construction gives

\[
 \boxed{\text{approximation factor }4-3/r}
 \quad\text{in}\quad 2^{O(r)}\operatorname{poly}(P,b)
 \tag{I1}
\]

time, and, for any rational eta>0,

\[
 \boxed{\text{approximation factor }4-3/r+\eta}
\]
\[
 \text{in }\operatorname{poly}(P,b+\operatorname{bits}(\eta))
 \min\{2^{O(r)},(r+1)^{O((1+\eta^{-1})\log(r+1))}\}.
 \tag{I2}
\]

These are rank-parameterized bounds: q can be much larger than r.
The derived dual and union oracles, the final basis decomposition,
fat-resource matching, and the rational target search are all paid.
The polynomial input factor in this wrapper is intentional. The
largest-item additive loss is absent. Rank one is exact.

The independently checked
**matroid_union_configuration_lp_addendum.md** strengthens this
comparison further: (I1)--(I2) also hold relative to the natural
configuration-LP optimum for the same arbitrary player matroid.
The algorithm still needs neither a fractional solution nor
enumeration of configurations. Its checkable failure certificate
implies that the original configuration LP is infeasible at T.
This stronger comparator is distinct from the unconditioned compact
player-basis LP with unrestricted item sizes.

The factor in (I1) tends to four as r grows. This is a finite-rank
improvement, not a fixed constant improvement below four uniformly
over unbounded ranks. For example, the exact factors at ranks two,
three and ten are 5/2, 3 and 37/10 respectively. It also does not
improve the known polynomial 4+eta algorithm on the ordinary special
case where all players must be allocated resources.

### The compact-LP theorem behind the reduction

For the player-basis compact relaxation Q(T), with y_pj<=x_p,
the core construction initially gives (T-u)/3-epsilon T, where u
is the largest resource value. Its complexity is

\[
 P\min\{2^{O(r)},(r+1)^{O(\epsilon^{-1}\log(r+1))}\}
             \operatorname{poly}(b+\log P).
 \tag{I3}
\]

At epsilon zero the same algorithm attains the exact additive
boundary in rank-exponential time. It requires no fractional solution
as input and returns either the basis allocation or an explicit,
oracle-checkable certificate of infeasibility of Q(T).

The sharper completed refinement sets

\[
 C(B,u)=\max\{u,2B+\min(u,B)\},\qquad \rho=(r-1)/r,
\]

and permits every positive B with B+rho C(B,u)<=T in the exact
rank-exponential algorithm. For r>=2, define d=4-3/r. The largest
target supplied by this analysis is

\[
 B_r^*(T,u)=
 \begin{cases}
 [rT-(r-1)u]/(3r-2),&u\le T/d,\\
 T/d,&T/d\le u\le3T/d,\\
 T-(r-1)u/r,&3T/d\le u<rT/(r-1).
 \end{cases}
 \tag{I4}
\]

Subtracting epsilon T gives the quasipolynomial bound (I3).
For rank one take B=T. The positive domain has a real LP obstruction
at its endpoint: r players sharing only r-1 resources can be
fractionally supplied but not all receive positive integral value.

The proof uses individual matroid eligibility and exchanges one free
bundle at a time. Choosing the earliest fundamental-circuit layer
preserves the closure defining every retained lower layer. Its
eligibility and forbidden-resource set are therefore unchanged;
only the last surviving layer must be refreshed. Current star value
accounting forces current blocker growth. An integer signature pays
for every candidate addition, exchange and free-center cascade.
The sums of its counts are bounded by r, giving both time bounds.

For arbitrary resource sizes, form the union of the original dual
player matroid and the fat-resource transversal matroid. Allocate
small resources to a basis of its dual. An original optimal allocation
supplies the required small-instance feasibility witness. A union
decomposition and extension to an original dual basis recover the
desired original player basis. This is an integer-OPT reduction;
it does not claim rounding of an arbitrary original Q(T) point with
large items.

### Fair public comparison and proof status

| Result or consequence | Comparator | Quality and time |
|---|---|---|
| DRZ v4, displayed Theorem 2 | Player-basis compact Q(T) | (T-u)/5-epsilon T, polynomial for fixed epsilon |
| Same displayed public theorem plus the explicit union wrapper | General player-basis integer OPT | 6+eta, polynomial for fixed eta |
| Current-blocker construction and sharp-star refinement | Same player-basis Q(T) | (I4), exact rank-exponential or minus epsilon T in rank-quasipolynomial time |
| Current-blocker theorem plus union wrapper | General player-basis integer OPT | (I1)--(I2), with arbitrary resource sizes |

DRZ's older versions did claim a one-third coefficient and factor four;
the revised source explains why its earlier birth-layer growth proof
needed correction. Those historical claims are recorded, not omitted
or treated as separately repaired contemporary results. A proposed
stronger algebraic retuning of the public framework is retained as
an explicitly unclosed interface question. No claim that the current
printed theorem is false is made.

Other primary comparisons include ordinary Santa Claus algorithms,
approximation schemes parameterized by all valuation types, and the
broader resource-matroid model. These have different selection or
LP contracts. In particular, allocating to a fixed set of players
already admits stronger T-u assignment rounding; the present gain
is not claimed on that special case. The literature check supports
the named comparison above, not a universal priority assertion.

Start with **matroid_union_fat_resource_allocation.md** and
**matroid_allocation_sharp_star_rank_quality.md**. The full core is
**matroid_allocation_current_blocker_quasipolynomial.md**. Root and
two independent mathematical reviews cover exchanges, current
maximality, rank counting, rational arithmetic, oracle substitution
and target search. The corresponding audit files and
**matroid_allocation_public_comparison_and_version_audit.md** are
included. This is not formal verification, external peer review,
or an implementation benchmark.

### Progress toward the original general-matching target

The matching route now has directed and bidirectional dynamic-forest
interfaces with persistent price registers. A separate complete
one-sided numerical client works when the **entire ordinary allocation
support** is a forest: it permits all receiving directions, separates
all feasible comparisons by sign-compatible cycle decomposition,
and has total static work (m+nu) polylog S. Its dynamic extension
charges every supplied structural, allocation and slack record.

A general matching expansion can create an ordinary cycle, so this
forest result does not solve the original unrestricted problem.
Keeping only a spanning forest would omit possible receiving
directions. The complete ambient-forest proof and two independent
audits are included under **complete_unrestricted_forest_***.

The complete client also extends to an ordinary graph with k
nonforest incidences, in total static work
(m+nu(k+1)) polylog S. An O(k)-size directed virtual-tree core
searches every path, and two represented-path intersection trims
remove possible repeated vertices without enumerating long tree
segments. Atomic multi-piece updates preserve the same global
price-event bound. **feedback_edge_one_sided_client.md** and its
two independent audits give the full argument and dynamic transcript
bound. A subcubic positive-ledger example has k=Theta(nu), so this
parameterization still does not supply the unrestricted improvement.

Within one fixed-potential interval, the full tight-arc graph is a
deletion-only DAG. Its source-reachable parent forest admits O(m+nu)
total repairs, with numerical transactions completed before topology
changes. Separate reachable examples show why a literal directed
old-tree epoch or permanently frozen receiving compatibility cannot
be assumed complete. They give no running-time lower bound.

An explicit bin-label batch has a necessary-and-sufficient feasibility
test and a history budget when every changed bin loses a fixed
fraction of its old potential. A reverse residual-ball primitive can
find a label repair or a tight passing path, but its boundary-search
work is not yet paid. These claims are local, with their unpaid
discovery and cross-interval obligations stated explicitly.

The implicit minimal-bundle independent-transversal implementation
also closes a representation gap without enumerating configurations
or assuming an NP-hard arbitrary-neighbor oracle. Integer layer
counts remove all unblocked certificate vertices, giving D=V(K).
The distinction S subset S_0 remains and prevents an automatic
below-four Santa Claus deduction from that certificate alone.

### Explicit correction to checkpoint H

**checkpoint_H_eligibility_threshold_erratum.md** records a localized
error in the old-root obstruction's preparation: H used actual slack
3C as an expansion trigger, whereas the client requires cached slack
at least 4C. The corrected preparation maintains exact eligibility
caches, crosses 4C, and uses revised constant margins. The reachable
obstruction survives. The immutable H archive has not been rewritten.
This correction does not change the transversal theorem, the local
forest interfaces, or the accepted matching exponent 4/5.

## New in checkpoint H: a general-partition transversal certificate

The original unrestricted deterministic exact general-graph matching
objective remains at exponent **four-fifths**. Checkpoint G's direct
four-fifths dynamic spanner and the earlier five-sixths low-recourse
spanner remain valid with their different contracts. The new result
in H extends the current-blocker method to a separate general graph
problem: independent transversals with a full domination certificate.

Let a graph's vertices be partitioned into q nonempty classes and set
P=|V|+|E|+q+2. For rational 0<epsilon<1, the algorithm returns an
independent transversal, or explicit class and vertex sets S,D and a
constellation K for a class set S_0 containing S, such that

\[
 |D|<(2+\epsilon)(|S|-1),\qquad
 V(K)\subseteq D,\qquad
 |D\setminus V(K)|<\epsilon(|S|-1).
\]

D totally dominates every vertex of the target classes: each has an
adjacent vertex in D, including those that themselves belong to D.
K is induced in G_(S_0), with within-class edges deleted, and consists
of nontrivial stars whose leaves form a partial independent transversal
of all but one class of S_0. This is the full public Graf--Haxell
certificate contract. Such a certificate can coexist with an
independent transversal, so the task is a certifying alternative,
not exact unrestricted independent-transversal decision.

If no vertex has r independent neighbours in distinct classes, the
new uniform time is

\[
 \boxed{\quad
 P\min\left\{\exp O(q),\,
       (q+1)^{O(\epsilon^{-1}\log(2+r/\epsilon))}\right\}
              \operatorname{poly}(b_\epsilon+\log P).
 \quad}
\]

Every arbitrary vertex-partitioned graph permits r=q+1. Therefore,
for fixed epsilon, the new second term is **quasipolynomial in q**,
with a linear explicit-graph-input multiplier up to bit complexity.
This specialization imposes no degree, class-size, or local-sparsity
promise on the input graph. A smaller supplied valid r sharpens the
parameter bound.

The fair comparison includes two public consequences established here:

| Construction for the same full certificate contract | Uniform time, omitting the common bit factor |
|---|---|
| Public single-vertex procedure, counting compositions of blocker counts | P exp O(q) |
| Public layered procedure with a length-aware signature count | P (q+1)^(O((r/epsilon) log(2+r/epsilon))) |
| New current-blocker stopping certificate with the retained public signature | P (q+1)^(O(epsilon^(-1) log(2+r/epsilon))) |

Both layered methods may use the elementary exponential fallback,
which is especially useful for very small slack. The input-linear
adjacency-list implementation is also common to both. The new gain
is the removal of the external r factor from the layered exponent.
For unrestricted r and fixed positive slack, it improves the checked
exponential-in-q public fallback to a quasipolynomial-in-q envelope.

The source's qualitative alternative and signature mechanism are
credited to Graf--Haxell. The new certificate uses actual current
greedy candidates and their present matching blockers, excludes both
full classes and classes containing extra selected vertices, and adds
one neighbour per current unblocked selected vertex. It proves
current blocker growth Omega(epsilon) per prefix, independent of r,
while preserving total domination and the constellation excess bound.
The resulting shorter signature has only O(epsilon^(-1) log q) layers.

The complete new proof and audits are:

* **independent_transversal_current_blocker_growth.md**;
* **independent_transversal_current_blocker_independent_audit.md**;
* **independent_transversal_current_blocker_root_audit.md**;
* **independent_transversal_input_linear_iteration_implementation.md**;
* **independent_transversal_elementary_exponential_fallback.md**;
* **independent_transversal_public_uniform_baseline_audit.md**.

Deterministic polynomial-time algorithms already solve stronger
degree/block-size promises, including blocks of size at least
(2+epsilon)Delta. They are included in the public comparison and are
better on that domain. The new result is compared with the named full
certificate framework; no global priority or optimality claim is made.
Its weak-Haxell specialization is the same mechanism as G's rank-linear
hypergraph analysis, not an unrelated second matching breakthrough.

**transversal_log_rank_signature_boundary.md** explains why merely
counting the old signature container still incurs the remaining
logarithmic claw dependence. Its realizable family ranges over
different inputs and states; it is not a running-time lower bound
for one input or for a different algorithm.

### Original matching route: a constructive fixed-forest interface

The new **any_source_fixed_tree_matching_interface.md** allows every
ancestor bin of a supplied directed threshold forest to act as a fresh
source. A constant-size max-plus heavy-light program finds a passing
ancestor-to-descendant path. Lazy path buffers apply the primal
allocation change and discover both price-register and guard events.
Persistent hysteresis gives a price-event count across all epochs,
without paying a fresh logarithmic price budget for every new tree.

Initialization and search use the same conservative donor prices.
The corresponding feasible-potential screen is E<=5N; the older
true-price screen E<=6N remains a separate interface. This distinction
fixes a real initialization mismatch found during independent review.
A fresh conservative shortest-path forest that has no passing path
already satisfies E<=N and can safely report LOW.

The completed checks are
**any_source_fixed_tree_matching_independent_audit.md** and
**any_source_fixed_tree_matching_root_audit.md**. A separate reachable
example and root audit are
**root_only_sp_tree_epoch_counterexample.md** and
**root_only_sp_tree_epoch_root_audit.md**. They show that the older
rule restricting starts to the tree's original source children can
exhaust a linear-size tree after only logarithmic progress. The new
any-source interface escapes that example.

The remaining global problem is the cost of repairing or supplying
new forests after later TREE-EMPTY with E>5N. The bounded price-event
count does not pay for whole-tree construction, and no such total
repair bound is claimed. All magnitude guards and structural ledger
changes remain explicitly charged imports. The matching exponent is
therefore unchanged.

A further public spanner check is included as
**dynamic_spanner_krampl_2026_baseline_audit.md**. Krampl's July 2026
thesis provides deterministic weighted worst-case guarantees with
small stretch, but its displayed update formulas retain a linear
vertex factor. It is a relevant separate tradeoff and does not imply
the subpolynomial amortized time or insertion-independent recourse
of the checkpoint constructions. The official PDF's theorem statements
and limitations were checked directly.

These are internally audited research constructions and analyses.
No formal verification, external review, or implementation performance
measurement is claimed. Unclosed subsequent repair proposals are not
part of the accepted results in this snapshot.

## New in checkpoint G: a direct four-fifths dynamic spanner

The original objective remains deterministic exact maximum matching
in arbitrary general graphs. Its accepted research bound still has
the **four-fifths** exponent. The new result below is a separate,
fully dynamic general-graph spanner transfer.

Write U=log(N+4), h=log(U+4), and
\[
                         E_4=\exp O(U^{4/5}h^{1/5}).
\]
For an arbitrary-degree undirected graph on n fixed original vertices,
with m_0 actual initial edges, I subsequent insertions, and D deletions,
the new direct construction has:

* multiplicative stretch E_4;
* at most n E_4 current output edges, all actual current original edges;
* total initialization and update work (n+m_0+I+D) E_4;
* safe total output recourse (n+m_0+I+D) E_4.

The work is amortized over any history within the declared polynomial
cap N. Parallel edge lifetimes and disconnected graphs are allowed.
Unweighted dyadic classes extend the result to positive polynomial-
range integer lengths with only polynomial logarithmic factors and
a factor two in stretch. The current output count uses the original
n vertices, not the larger number of degree-reduction ports. This
makes the result nontrivial on polynomially dense arbitrary graphs.
The whole-input exact spanner remains the baseline whenever it already
fits the allowed output size.

The mechanism tracks at most n original query traces per hierarchy
level, marks their local source trees, and maintains the compressed
subtrees joining those marks in the already lifted forest family.
It exposes only compressed edges whose represented path is short.
Every short query witness is automatically covered, without storing
or updating a witness for every input edge. The dynamic compression
works for links, cuts, mark changes, and nonnegative length changes.

The lower exponent comes with a different recourse guarantee from F:

| Accepted construction | Logarithmic time/stretch/density envelope | Safe total output recourse |
|---|---|---|
| New direct tracked-forest spanner | O(U^(4/5) h^(1/5)) | (n+m_0+I+D) exp O(U^(4/5) h^(1/5)) |
| Checkpoint F batching spanner | O(U^(5/6) h^(1/6)) | (n+D) exp O(U^(5/6) h^(1/6)) |

In particular, the new theorem does not inherit F's independence from
the insertion count. Initial provider credit may produce later forest
edits, so m_0 is retained in the safe general recourse bound. For an
initially empty graph the new bound is (n+I+D) E_4.

The main proof and completed internal audits are:

* **tracked_terminal_flat_spanner_four_fifths.md**;
* **tracked_terminal_flat_spanner_independent_audit.md**;
* **tracked_terminal_flat_spanner_root_audit.md**;
* **dynamic_marked_forest_short_path_union.md**;
* **tracked_terminal_spanner_public_flat_comparator_audit.md**.

The same observer can also be applied to the reconstructed public
APSP provider. Its full-tree-copy interface needs an explicit elementary
zero-link extension for projected port connectors and inherited nulls.
This adapter is included and audited; it is not attributed to the
printed source's original contract. Incoming node occurrences retain
independent assigned copies, so a child edge edit costs O(1) records
and does not multiply by the full occurrence budget. The comparison
does not use the new colored-pool construction for the public provider.

At the common finer logarithmic stretch A_0=U^(5/7)h^(2/7), the
matched comparison is:

| Provider with the same tracked-forest observer | Logarithmic total-work and output-density overhead |
|---|---|
| Reconstructed public provider and explicit plain-copy adapter | O(U^(6/7) h^(1/7)) |
| Research provider | O(U^(23/28) h^(5/28)) |

These are derived compositions, not printed spanner theorem exponents
or a claim that every public dynamic-spanner approach has been optimized.
The new 4/5 point allows a larger stretch than A_0. At the finer point,
the density overhead is 23/28, not 5/7, because the local source-tree
mark inventory is paid explicitly.

**direct_spanner_budget_and_recourse_obstructions.md** explains why
nonuniform retuning alone does not reduce 4/5 in this particular
positive-accounting formula, and why exact short-path-union changes
can require a full path's output. Neither observation is an algorithmic
lower bound. A faster or lower-recourse support rule remains open.
The additional completed **clipped_reporting_independent_audit.md**
checks the distinct clipped-walk interface used by F.

### A second accepted transfer: rank-linear weak-Haxell analysis

The same current-size and lifetime accounting viewpoint also yields a
sharper uniform analysis of Annamalai's public augmenting algorithm.
Here a bipartite r-uniform hyperedge has one left vertex and r-1 right
resources; n is the number of left vertices, P is explicit input volume,
and rational 0<epsilon<1 has bit length b_epsilon. Under

\[
 \tau(E_S)>(2r-3+\epsilon)(|S|-1)
              \quad\text{for every nonempty }S\subseteq A,
\]

the resulting time is

\[
 P(n+1)^{O((r/\epsilon)\log(2+r/\epsilon))}
                    \operatorname{poly}(b_\epsilon+\log P).
\]

The certifying algorithm returns a left-perfect matching or an explicit
violating S with a right hitting set of size at most
(2r-3+epsilon)(|S|-1). That qualitative algorithm and certificate
alternative are already public. The new proof improves the uniform
parameter analysis: the length-aware count of the checked source
formulas gives a rank-squared exponent, whereas a new bound on every
surviving layer's current blockers gives the rank-linear exponent above.
Both a weighted lifetime count and the public signature with its shorter
length give the same bound.

The historical greedy candidate is retained as a physical hitting
certificate, including blockers that subsequently leave the matching.
Its support is paid by the current blocker count using the source's
overlap savings. Birth-selected growth is retained separately to pay
for newly built layers that collapse immediately. This separation
prevents a false monotonicity argument about shrinking blocker sets.

The complete proof, source comparison, and internal audits are:

* **weak_haxell_uniform_lifetime_analysis.md**;
* **weak_haxell_current_blocker_growth.md**;
* **weak_haxell_current_blocker_independent_audit.md**;
* **weak_haxell_current_blocker_root_audit.md**;
* **weak_haxell_public_parameter_comparison.md**.

Graf--Haxell's later independent-transversal algorithm is included in
the same-promise comparison using its constellation certificate.
The stronger-expansion almost-linear hypergraph theorem has a different
promise. This result does not solve the exact epsilon=0 boundary,
give polynomial dependence on 1/epsilon, improve ordinary bipartite
matching, or change the unrestricted general-graph matching exponent.

All newly accepted results in this snapshot are research proof
assemblies with completed internal mathematical audits. They are not
formally verified, externally reviewed, or experimentally benchmarked.
Unclosed follow-up constructions are excluded from this snapshot.
Earlier ZIP snapshots remain immutable; their contents are retained
below with their original result boundaries.

## New in checkpoint F: a full-horizon dynamic spanner

The original unrestricted deterministic exact general-graph matching
bound remains **four-fifths**. This checkpoint adds a separate transfer:
a deterministic explicit dynamic spanner for arbitrary undirected
graphs, including arbitrary degree and polynomially dense inputs.

Let U=log(N+4), h=log(U+4), and
\[
                   E_5(N)=\exp O(U^{5/6}h^{1/6}).
\]
For a fixed n-vertex set, an actual initial graph with m_0 edges, and
any subsequent sequence of I insertions and D deletions within the
declared polynomial history cap, the maintained spanner has:

* multiplicative stretch at most E_5;
* at most n E_5 current edges, each an actual current input edge;
* total initialization and update work at most (n+m_0+I+D) E_5;
* total output recourse at most (n+D) E_5.

The time guarantee is amortized. All guarantees hold after settled
external updates. Parallel edge identities and disconnected graphs
are allowed. Separate unweighted dyadic classes extend the result to
positive polynomial-range integer lengths. The result does not claim
ordinary simple-path output sensitivity or a worst-case per-update
time/recourse bound.

The new path interface expands a represented walk only after its
numerical estimate passes a length threshold. Positivity and nonempty
parent-path witnesses pay every expansion record. Loop erasure then
returns a literal simple path. The public KMZ batching construction
is rebuilt here with nested integer deletion clocks and exact seeding
accounts, so the result covers arbitrary insertion/deletion sequences.
It does not reset a dense graph after every n deletions.

The main exponent uses the conservative already-audited repair bound;
it does not require a new high-degree extension of normalized repair.
Its proof and completed audits are:

* **fully_dynamic_spanner_five_sixths.md**;
* **fully_dynamic_spanner_independent_audit.md**;
* **fully_dynamic_spanner_root_audit.md**;
* **clipped_walk_queries_and_dynamic_spanner.md**;
* **dynamic_spanner_public_baseline_audit.md**.

The public comparison is optimized at the same final output scale:

| Construction | Logarithmic amortized time overhead | Common logarithmic stretch, density, and recourse overhead |
|---|---|---|
| Reconstructed public APSP and public KMZ batching | O(U^(31/36) h^(5/36)) | O(U^(5/6) h^(1/6)) |
| Research provider, positive witnesses, and the same batching | O(U^(5/6) h^(1/6)) | O(U^(5/6) h^(1/6)) |

The public pipeline also has a balanced six-sevenths point at a larger
output scale. These are derived comparisons with the named public
framework, not printed exponents or a proof of global optimality over
all public spanner algorithms. The audit includes the formal ICALP 2025
version, which has material absent from arXiv v1, and the different
scope of newer randomized and worst-case results.

The elementary H=G baseline is explicit: if the live graph is already
within the permitted output density, it is an exact spanner with
constant maintenance work. The nontrivial scope of the new result
includes graphs of polynomial density whose input is larger than
n E_5. No improvement over keeping the input is claimed in the range
where it already satisfies all output requirements.

### A stronger public MSF baseline, not an exclusive new transfer

A formal source audit also establishes the derived-public deterministic
worst-case dynamic exact MSF envelope
\[
                         \exp O(U^{2/3}h^{1/3}).
\]
It combines deterministic static decomposition, modern deterministic
expander pruning, and the explicit weighted NSW contraction/batching
framework. The root rejected the standalone informal connectivity
sketch and checked the actual weighted compressed-cluster certificate.
The corrected construction removes a weight band before decomposition,
handles residual isolates, and ends each period before any pruning
horizon. Its operative proofs are
**dynamic_msf_formal_pruning_substitution_audit.md** and
**dynamic_msf_public_baseline_root_audit.md**.

This strengthens the comparator. It is not an exclusive application
of the matching router, not a deterministic polynomial-logarithmic
worst-case result, and not an improvement over classical polynomial-
logarithmic amortized MSF. The tagged-triangle alternative remains
outside the accepted new results in this checkpoint.

The previous checkpoint E strong-forest and exact cut-tree result,
all earlier transfer proofs, and the original matching objective remain
as described below. Earlier ZIP snapshots are immutable.

## New in checkpoint E: six-sevenths strong forests and exact cut-equivalent trees

The unrestricted deterministic exact general-graph maximum-matching
bound remains
\[
 O(n+m)+(m_s+1)\exp O\!\left(
  (\log(m_s+2))^{4/5}(\log\log(m_s+4))^{1/5}\right).
\]
Here \(m_s\) is the edge count after the original simplification.
The improvements below concern separate problems or proof interfaces.
They do not change that exponent.

### Strong decremental SSSP and exact Gomory--Hu trees

The main new construction replaces recursive high-degree contracted
roots by uncontracted selected edges and compressed stable-tree paths.
Colored full-forest pools lift the resulting paths with small vertex
occurrence, while keeping fixed canonical node identities and paying
every unused copy. Recursive native degree grows only by a polynomial
logarithmic factor per level, so no recursive port reset is required.

With \(U=\log(N+4)\) and \(h=\log(U+4)\), the resulting bound is
\[
                        E_6(N)=\exp O(U^{6/7}h^{1/7}).
\]
It gives a strong decremental \((1+\varepsilon)\)-SSSP flat forest
in total \(O((n+m)E_6)\) time on the bounded-degree native interface,
for positive polynomial-range lengths and constant or inverse-
polylogarithmic accuracy. All canonical nodes, edge embeddings,
vertex/edge occurrences, and forest changes are included.

The separately audited application reduction consequently gives an
**exact deterministic Gomory--Hu tree for an arbitrary undirected
graph** in \(O(n+m)+(m+1)E_6(n+m)\) time, with positive polynomial-range
integer capacities. Parallel edges and disconnected components are
allowed. The cut-equivalent output is exact even though the internal
distance forests are approximate.

| Strong-forest/Gomory--Hu comparison | Logarithmic overhead |
|---|---|
| Public KMG printed forest specialization | \(O(U^{83/84}h)\) |
| Strongest public reconstruction established here | \(O(U^{8/9}h^{1/9})\) |
| Previous research construction | \(O(U^{7/8}h^{1/8})\) |
| New internally audited construction | \(O(U^{6/7}h^{1/7})\) |

The \(8/9\) row is a strengthened analysis of public algorithms:
their original forest lift can count input nodes directly and avoid
an unnecessary edge-to-vertex degree multiplication. The new gain
comes from also controlling native degree through the uncontracted
compressed graph and realizing its paths by dynamic full-forest pools.
The comparison therefore includes the stronger public reanalysis.

The primary proof is **steiner_pool_no_reset_strong_forest.md**.
The two completed independent audits are
**compressed_steiner_pool_independent_audit.md** and
**steiner_pool_metric_inventory_focused_audit.md**.
**six_sevenths_strong_forest_and_gomory_hu_checkpoint.md** states
the exact output contracts, application dependencies, and comparison.
**public_forest_direct_vertex_inventory.md** proves the public row.

The no-reset proof is the accepted implementation. The older ported
pool draft remains an optional candidate and is not needed for this
result. The new nonuniform \(6/7\) budget statement is an obstruction
only for its specified positive accounting model, not an algorithmic
lower bound.

### Fully dynamic APSP at a common stretch scale

The new source reconstruction substantially strengthens the public
comparison. Write \(U=\log(N+4)\) and \(h=\log(U+4)\), where \(N\)
counts actual graph inventory and update history. For deterministic
numerical APSP in arbitrary undirected graphs, at the common stretch
scale \(\exp O(U^{5/7}h^{2/7})\), the bounds now compared are:

| Construction | Amortized initialization/update overhead |
|---|---|
| Joint reconstruction from public primitives | \(\exp O(U^{6/7}h^{1/7})\) |
| Current research construction | \(\exp O(U^{23/28}h^{5/28})\) |

Both support polynomial logarithmic numerical queries and positive
polynomial-range integer lengths. The public row is a newly derived
consequence, not a printed theorem. It retains the public
ambient-length congestion loss. The research row uses the new static
provider and normalized repair interface. The same-scale leading
power comparison is \(24/28\) versus \(23/28\). The earlier \(11/14\)
and \(3/4\) time--stretch points remain valid.

The source reconstruction pays the small-instance BFS fallback,
actual-size loopless degree bands, weighted witness ports,
construction work in deamortization, and recursive query labels.
Its proof and two independent reviews are
**public_apsp_joint_retuning_audit.md**,
**public_apsp_joint_retuning_independent_audit.md**, and
**same_stretch_apsp_comparison_and_root_audit.md**. The old \(59/63\)
comparison is retained as historical analysis of a more restricted
composition, not as the strongest comparison established here.

### Rank-sensitive certified hypergraph matching

Let \(q=|A|\), let \(r\) be the maximum number of right resources
in one hyperedge, and let \(p\) be explicit edge volume. Under the
same strong Haxell condition with parameter \(\Delta\ge4\), put
\[
 s=\log\Delta,\qquad
 a=\min\{\log(2+s),\log(2+\log(r+2))\}.
\]
The number of layer builds is at most
\[
 O\!\left(\min\{\log(q+1),1+s/a\}\right)
       \exp O\!\left(\frac{a\log(q+1)}s\right).
\]
For fixed rank this removes a logarithmic factor from the exponent
in checkpoint D's count. For example,
\(\Delta\ge\exp((\log p)^\beta)\) gives overhead
\(\log(p+4)\exp O((\log p)^{1-\beta})\), for fixed \(0<\beta<1\).
The count also applies to the original BHHS operations; it is a new
analysis of that public algorithm as well as of the simpler variant.

The baseline corrections are part of this result. A single greedy
scan already suffices when \(q\le\Delta r\), and after the whole-set
certificate check it also suffices when
\(\Delta^2r^3\ge |B_{\rm used}|\). In particular
\(\Delta\ge\sqrt p\) is an elementary linear-time regime.
For rank one, the ordinary Hopcroft--Karp expansion argument gives
the stronger \(O(p(1+\log(q+1)/\log\Delta))\) bound.
The nontrivial constant-rank comparison is therefore for \(r\ge2\)
outside those elementary regimes. See **rank_sensitive_layer_count.md**.

The new **edge_disjoint_spanning_expander_packing_corollary.md**
also spells out the public routing-to-packing reduction with the
current quantitative factors. All demand pairs are routed in one
instance, so it does not allocate a copy of the graph per output
expander. The reduction itself is credited to the public work.

### A narrower numerical oracle for general matching

**matching_semantic_oracle_and_contact_reserve.md** separates a
matching-specific stopping certificate from a generic small-cycle
oracle. Cheap feasible-gain upper bounds can certify that the phase
has no target-sized matching improvement without finding every
high-ratio circulation. A concrete legal expansion example rules
out merely freezing one comparison allocation as a contact reserve.

**slack_only_one_sided_matching_client.md** proves that keeping only
slack logarithms in the objective still yields a constant-ratio
direction from an actual matching gap. Its exact threshold test is
nonnegative directed SSSP. Along a sufficiently small exact
shortest-path step, all previous distance labels remain feasible
and true distances are nondecreasing, despite some edge-cost
decreases. A finite-word integer formulation is included.

These are positive reductions, not a faster matching algorithm.
The dynamic path-reporting and implicit repricing interface still
needs a proof. The literal serial-route example shows why the old
generic cycle obstruction alone does not exclude this semantic route.

**slack_potential_semantic_certificate.md** adds a maintained scalar
certificate \(E=\sum_d(s_d\pi_d-5/4)_+\). A feasible integer potential
with \(E\le6N\), and the explicitly budgeted rounding error at most
\(N\), certifies matching LOW. A current threshold-passing path in
one fixed old shortest-path tree preserves its labels and yields a
monotone numerical epoch. The number of necessary tree refreshes
remains unbounded by the present proof.

**coarse_directed_paths_for_slack_matching.md** proves that a suitable
source-bucket, set-to-set directed path provider of factor \(\Gamma\)
would already give a direction ratio at least \(1/(8+6\Gamma)\).
It states the required witness and target-search interface explicitly.
An arbitrary approximate path does not automatically preserve the
old potential's tight receiving arcs.

At checkpoint E, the dynamic-MSF and weak-Haxell working notes retained
their candidate/source-audit status. Checkpoint F's formal public MSF
audit supersedes that MSF status as stated above; neither is counted
as an exclusive improvement from the research router.

All results retain their named imports and internal-audit status.
No externally reviewed theorem or implemented running-time benchmark
is claimed. Earlier ZIP checkpoints are immutable.

## New in checkpoint D: fixed certificates and a sharper hypergraph time bound

This checkpoint adds a deterministic **matching-or-certificate algorithm for
explicit bipartite hypergraphs**. Each hyperedge contains one left vertex
and between one and \(r\) right vertices. Let \(p\) be the explicit edge
volume, \(U=\log(p+4)\), and let \(\Delta\ge4\). The algorithm returns
either a matching covering the whole left side, or a nonempty left set
\(S\) and a right set \(C\) hitting every edge incident to \(S\), with
\(|C|<\Delta r^2|S|\), in time

\[
 O(|A|+|B|)+p\exp O\!\left(
       \frac{U\log(2+\log\Delta)}{\log\Delta}\right).
 \tag{D1}
\]

It therefore finds a left-perfect matching under the strong Haxell
condition \(\tau(E_S)\ge\Delta r^2|S|\) for every left set \(S\).
The alternative certificate refutes this sufficient condition, not
the existence of a perfect matching. Either output is independently
checkable in linear time on the explicit input.

For the same condition, the checked BHHS SODA 2026 theorem has displayed
overhead \(\exp O(U/\sqrt{\log\Delta})\). Formula (D1) improves this
quantitative dependence for every \(\Delta\) tending to infinity. If
\(\Delta\ge p^\epsilon\), for fixed \(\epsilon>0\), the new time is
\(O(|A|+|B|)+p(\log p)^{O(1/\epsilon)}\). If
\(\Delta\ge\exp(U^\beta)\), for fixed \(0<\beta<1\), the overhead is
\(\exp O(U^{1-\beta}\log U)\). The comparison is to a named public
theorem, not an exhaustive optimization of every public framework.

**Stronger public-framework comparison.** This round also derives (D1)
for the original BHHS maximal-layer algorithm. Its successful
superposition steps multiply a layer's size by at least \(1.1\), while
that size remains between \(\Delta W/10\) and \(\Delta W\). There are
only a constant number of such resets per layer. Splitting its lifetime
into those epochs extends the weighted count to the public algorithm.
Historical certificates from its last actual build justify the growth
analysis without requiring a fresh hypothetical maximality claim.
Thus the improved quantitative bound is also a **new analysis of a
public algorithm**, not an asymptotic advantage exclusive to the
no-superposition variant. The baseline note and its independent audit
make this distinction explicit.

Our simpler variant retains the original resource identities consumed while
building a layer. This fixed hitting certificate survives changes in
matching ownership. No surviving layer needs repeated supplementation.
A contracting weight on the tree of layer lifetimes then proves the
new iteration bound without an additional rank dependence. The complete
explicit-input argument is **explicit_hypergraph_matching_branching_improvement.md**;
it needs no shortest-path structure. The general construction and audits
are **certified_no_superpose_haxell_path_routing.md**,
**fixed_certificate_branching_count_independent_audit.md**, and
**certified_layer_outer_independent_audit.md**. Annamalai's earlier work
already includes a qualitative matching-or-Haxell-violation alternative;
here that alternative accompanies the sharper time bound.

The second addition is a **destructive path-support extractor** from
checkpoint C's numerical APSP interface. On arbitrary undirected graphs,
it supports length-bounded disjoint-path packing and the required
half-layer states. It charges original edges when their support is
consumed, avoiding the expansion of a walk whose cycles would then be
discarded. **destructive_apsp_path_support_extractor.md** proves the
occurrence budget, fresh per-call reset, and own-matched-path handling.

Together these mechanisms give all-demand edge-disjoint routing under
the stated short-path hitting condition. For expanders the sufficient
condition is explicitly
\(\phi^3\delta\ge Ck\Delta\Gamma^2\log^2N\), with path length
\(O(\Gamma\log N/\phi)\). Here \(\phi\) is conductance, \(\delta\)
minimum degree, \(k\) endpoint load, and \(\Gamma\) distance stretch.
This inherits the \(11/14\) and \(3/4\) time--stretch points below,
with every density and path-length factor retained. Parallel edges
are allowed; the structural diameter proof uses graph volume.

These are research proofs with named imports and internal mathematical
audits, without external review or implementation benchmarks. The
original **unrestricted general-graph exact maximum-matching** exponent
remains **\(4/5\)**. The promised hypergraph and expander results do
not change that statement. Checkpoints A, B, and C remain unchanged.
This archive contains English notes, without Lean, PDF, or test bundles.

## New in checkpoint C: fully dynamic distances

Checkpoint C adds a separately audited time--stretch tradeoff for
**deterministic fully dynamic numerical APSP in arbitrary undirected graphs**.
Let `N` bound the initial graph inventory plus the update count,
`U = log(N+4)`, and `h = log(U+4)`. Positive integer lengths have a fixed
polynomial range. Parallel edges, arbitrary degree, and arbitrary density
are allowed. Numerical distance queries take `polylog N` worst-case time.

| Amortized initialization/update overhead | Distance stretch |
|---|---|
| `exp O(U^(11/14))` | `exp O(U^(6/7) h)` |
| `exp O(U^(3/4) h^(1/2))` | `exp O(U/h)` |

The first point preserves the displayed stretch scale of the public KMG
APSP theorem. The second uses a coarser, still subpolynomial stretch.
Initialization plus all updates costs the actual initial inventory plus
the update count, multiplied by the chosen overhead. These guarantees
concern numerical distances and amortized maintenance; they do not claim
constant approximation, worst-case update time, or a lower exact matching
exponent.

The proof separates local maintenance from cumulative metric distortion:
with `p = r = t`, `K = t^2`, and `x = Theta(U/t)`, the logarithmic time
budget is `O(U/t + t^3 h)`, whereas logarithmic stretch is `O(t^4 h)`.
An actual-incidence balanced tree implements arbitrary degree with a
permanent query handle per original vertex. Its connector lifetimes and
all internal reset scales are explicitly charged.

The primary files are `apsp_time_stretch_tradeoff.md`,
`apsp_tradeoff_independent_audit.md`, and
`apsp_public_parameter_and_query_audit.md`. The comparison includes both
the printed KMG `20/21` worst-case update bound and a derived public
`59/63` amortized composite using the old KMG local theorem and ordinary
binary-tree degree reduction. It also records a stronger retuning of the
independent public KMZ construction, with logarithmic update envelope
`O(U log(h+4)/h)`, and the admissible parameters and query costs of HLS
and CZ. The checkpoint does not claim to optimize every public framework.

`nonuniform_parameter_budget_frontiers.md` and its independent audit
prove a narrower but useful conclusion: allowing different parameters at
different hierarchy levels does not improve the `11/14`, matching `4/5`,
or strong-forest `7/8` balances **inside the specified positive accounting
model**. This is not a lower bound on graph algorithms. It identifies
which charged interfaces must change to obtain another exponent gain.

All results retain the research-proof status and named imports stated
below. The destructive extraction and fixed-certificate applications
completed after checkpoint C are described above.

## Current result

The first main new result of this round is a proof candidate for **deterministic
incremental single-source distances and approximate simple paths in arbitrary
directed graphs**.
It transfers the four-fifths raw-cycle backend developed for general maximum
matching without the exponent deterioration caused by the previous distance
detector's reporting bound.

Let `N` be a power-of-two master bound for `n+m`, let `U=log N`, and let
`h=log(U+4)`. For positive integral edge lengths bounded by a fixed polynomial
in `N`, the candidate maintains an explicit array satisfying

\[
 d(s,v)\leq\widetilde d(v)\leq(1+\varepsilon)d(s,v)
\]

under arbitrary online edge insertions, with total time

\[
 O(n+m)+(n+m)\exp O\!\left(
 U^{4/5}h^{1/5}+\sqrt{U\bigl(h+\log(1/\varepsilon)\bigr)}
 \right).                                                   \tag{A}
\]

For constant or inverse-polylogarithmic accuracy this is

\[
 O(n+m)+(n+m)\exp O\!\left(U^{4/5}h^{1/5}\right).             \tag{B}
\]

The same envelope holds whenever
`log(1/epsilon)=O(U^(3/5) h^(2/5))`, subject to the eventual fixed-constant
parameter guards stated in the main proof. Unreachable vertices are
identified exactly. Parallel edges, arbitrary degree, arbitrary density,
and adaptive online updates are allowed. A decreased weight can be supplied
as a new parallel-edge version, counted as another update record.

The nonnegative integral-weight case also follows: add one tiny common
dyadic positive offset to each edge and rescale to positive integers.
Flooring the rescaled upper estimate returns every zero distance exactly,
while the perturbation is absorbed in the accuracy budget for every
positive integral distance. Section 10.1 of the main theorem gives the
full reduction.

The structure now also reports an explicit approximate **simple directed
path** in `O((k+1) poly(log N))` time, where `k` counts the root edges
actually returned. The added construction represents the initial walk
as `O(log N)` native tree segments and single edges, finds path
intersections with a static four-dimensional index, and deletes whole
cyclic segments before enumerating the retained edges. It does not pay
for the length of an expanded walk that is later discarded. The full
proof is `simple_path_reporting_from_tree_segments.md`; its preprocessing
adds only polynomial logarithmic work to (A).

The proof is complete **relative to the named constructive raw-backend and
dynamic-tree interfaces**. The detector, its outer recursion, and its
integer-price adapter have undergone separate internal mathematical audits.
This is a research proof assembly, not a peer-reviewed theorem, a formal
verification, or a running-time benchmark of an implemented solver. The
archive contains no Lean, PDF, or experimental verification package.

The second main transfer is a deterministic **exact Gomory--Hu tree for
arbitrary undirected graphs with positive polynomially bounded integer
capacities**, with the checkpoint E research bound

\[
 O(n+m)+(m+1)\exp O\!\left(U^{6/7}h^{1/7}\right).
 \tag{C}
\]

Parallel edges, arbitrary degrees, and disconnected inputs are included.
Disconnected components are joined by zero-weight tree edges. This is
an exact cut tree; only the internal metric and packing computations
are approximate. The result uses the separate strong-forest construction
and a newly explicit fixed-parameter guide-tree mincut recursion, as
described below. It has the same research-proof status as (A), rather
than the status of an implemented or externally verified algorithm.

## Why the new mechanism changes the exponent

The starting point is Liu's modified interior-point detector for decreasing
source distances. Its auxiliary edge to each target starts with one unit
of flow. A high-power barrier makes an auxiliary edge expensive when the
target's old distance estimate has become inaccurate.

The new operation freezes such an auxiliary coordinate at its exact current
value. Its flow and cost remain part of the full conserved state, but the
coordinate is removed from future circulation updates and its **positive
barrier contribution is deleted**. The residual-demand comparison direction
and the dual certificate for every unreported vertex remain valid.

If `M` is one detector's logical inventory allowance, `alpha` its phase
threshold, and `sigma` its accuracy, its complete lifetime has only

\[
 O(\alpha M U^2/\sigma)
\]

frozen units. This follows by charging the deleted positive barrier to the
potential budget `O(MU)`. In particular, the count contains **no inverse
oracle-accuracy factor**. Numerical work still depends on that factor.

Separate unit copies pay each reported vertex's full incoming and outgoing
degree. A child inventory quota pays later incident insertions and new
vertices. The sum of child allowances per parent is then at most a factor
`poly(U,1/epsilon)` times the parent allowance. This factor, rather than the
raw backend's larger overhead, is propagated through the recursion.

The general transfer formula is

\[
 (n+m)\exp O\!\left(\log E(N)
        +\sqrt{U\bigl(h+\log(1/\varepsilon)\bigr)}\right),
\]

for a raw interface whose quality, work, copy counts, and callback factors
are fixed powers of `E(N)`. The four-fifths specialization is (A).

## Baseline corrections made during this round

The comparison has been deliberately strengthened as the audit progressed.
The main baseline file is `transfer_public_baselines.md`.

| Problem or composition | Quantitative exponent | Status |
|---|---:|---|
| Liu's incremental SSSP, final explicit bound in Section 4 | `335/336` | Printed public result |
| Public September 2026 raw-cycle engine in the original Liu detector | `41/42` | Derived public composition, with its raw interface made explicit |
| Our four-fifths engine in that unmodified detector | `9/10` | Straight composition; superseded here |
| New frozen-barrier detector with the public `20/21` engine | `20/21` | New client specialization, subject to the exact retirement adapter |
| New frozen-barrier detector with the matching backend | `4/5` | Main candidate of this checkpoint |
| Static deterministic min-cost flow in the printed FO24 specialization | `5/6` | Printed public result |
| Retuned public dual tree-cut framework | `4/5` | Derived and independently audited public-framework comparison |

The static-flow correction is important: this round found that keeping
construction work separate from exported recourse and quality lets the
existing public dual construction also reach four fifths. Therefore the
new primal static-flow route is **not presented as uniquely beating every
public-framework consequence**. The new incremental distance detector has
a distinct reporting argument and does not follow automatically from the
static dual theorem.

An October 2026 preprint by Hanqing Li already gives almost-linear
decremental directed distance estimates via cut balance. That paper concerns
the opposite update direction and supplies numerical estimates rather than
fast path reporting. It must be included when considering decremental
transfers; an old open-problem remark in Liu's 2025 paper is no longer an
adequate baseline. The accompanying baseline note records its scope.

Primary starting points:

* Liu, *Incremental Shortest Paths in Almost Linear Time via a Modified
  Interior Point Method*, <https://arxiv.org/html/2506.19207v1>.
* Kyng, Meierhans, Probst Gutenberg, and Sulser, *A Simpler and Faster
  Min-Cost Flow Solver via Min-Ratio Cycles from Distance Oracles*,
  <https://arxiv.org/html/2609.23852v1>.
* van den Brand et al., *Almost-Linear Time Algorithms for Decremental
  Graphs: Min-Cost Flow and More via Duality*,
  <https://arxiv.org/html/2407.10830v1>.
* Li, *Almost-Linear Decremental Single-Source Distance Estimates in
  Directed Graphs via Cut Balance*, <https://arxiv.org/html/2610.07468v1>.

## Additional completed transfer: a moving-box min-cost-flow client

`moving_box_log_barrier_flow.md` develops a separate numerical client using
two-sided logarithmic barriers and tiny outward-moving bounds. Its useful
features are a constant-ratio comparison direction, exact dyadic flow
increments, a fixed-cost aggregate on raw paths, complete retirement
bookkeeping, and integer recovery through cost-nonincreasing rounding.

Together with the same raw backend it gives the candidate envelope
`m E(m)^O(1)` for exact static directed min-cost flow and for incremental
fixed-threshold crossing with fixed demands and polynomially bounded
integral data. The latter improves the compared public incremental
`20/21` envelope to four fifths. It is a threshold-crossing interface,
not exact dynamic maintenance of the optimum after every insertion.

The static route includes an independent primal/residual-potential
acceptance check. A verifier protects the accepted output; it does not
prove the proposed fast time. In particular a static verification portfolio
cannot be substituted for the sound LOW decisions needed online.

Supporting notes cover arbitrary demands, infeasibility, lower bounds,
integrality, and the polynomial-bit alternative for the older power-barrier
client. Two independent audits of the moving-box proof are retained.

## Additional transfer: exact incremental strongly connected components

`log_barrier_incremental_scc.md` gives a particularly small numerical
client for arbitrary incremental directed graphs. It maintains the exact
SCC partition, with explicit component identifiers, in total time

\[
 O(n+m)+(m+1)\exp O\!\left(U^{4/5}h^{1/5}\right).
\]

This uses the same raw-backend assumptions as the distance result. The
potential consists only of one-sided logarithmic barriers
`-sum_e log(f_e+delta_e)` on an exactly conserved signed circulation.
A directed cycle always supplies a ratio of minus one. A sound LOW
answer therefore certifies that the current quotient is a DAG.

An edge whose positive flow exceeds the total permitted negative flow
must have both endpoints in one true SCC. Merging its endpoint blocks
is safe, preserves circulation after internal edges are removed, and
deletes nonnegative barrier terms. Every original edge contributes only
`O(U)` positive potential on birth. Endpoint replacements retain the
same flow and offset and are charged by small-to-large merging; they
are not counted as fresh barrier births.

The high-flow contraction principle is public, from CKLMP24. The new
contribution is the pure logarithmic client and its explicit numerical,
retirement, and endpoint accounting with the four-fifths backend. The
public September 2026 raw-cycle engine gives a stronger comparison than
the original 2024 exponent; that comparison is `20/21`, not a polynomial
bound. `log_barrier_scc_independent_audit.md` records a separate audit.

This also gives incremental directed cycle detection; an explicit first
cycle can be recovered by one linear-time DFS. It does not give fast
paths inside arbitrary SCCs or dynamic topological ordering. The latter
requires a constructive dual-potential interface that is not supplied
by the current raw-cycle oracle. The exact gap is documented in
`topological_order_transpose_interface_gap.md`.

## Additional consequences for general degree-constrained subgraphs

`general_degree_constrained_subgraphs.md` transfers the matching bound to
exact prescribed-degree factors, interval-degree feasibility, and
minimum or maximum cardinality subject to those degree intervals in
arbitrary loopless undirected multigraphs. Each explicitly listed edge
has capacity one. The bound is

\[
 O(n+m)+(m+1)\exp O\!\left(
   (\log(m+4))^{4/5}(\log\log(m+16))^{1/5}\right).
\]

The prescribed-degree reduction uses the OpenAI paper's Beneš-network
construction, whose logarithmic expansion and maximum degree three are
proved again with original edge IDs retained. The interval reduction
uses one degree-balancing hub and parity-adjusting triangles. Optimizing
cardinality becomes a sequence of monotone interval-feasibility tests;
it does not assume that all intermediate exact cardinalities are
attainable. `degree_constrained_subgraph_independent_audit.md` checks the
construction, including rejection of impossible required lower bounds.

These are consequences of the current general matching candidate. They
do not establish an arbitrary weighted-matching algorithm, arbitrary
allowed-degree sets, or a bound independent of a compressed edge
multiplicity. The original prescribed-degree reduction is credited to
OpenAI rather than presented as a new reduction of this round.

## Second main transfer: a quantified exact Gomory--Hu tree

The strong metric construction keeps three quantities separate:
distance distortion, simultaneous forest congestion, and construction
work. An anchor forced through the hierarchy bounds the paths that
start at actual terminals without incorrectly asserting that every
auxiliary child vertex has small diameter. The forest lift retains
permanent canonical vertices and delays true-null contraction until
the final physical root. A joint choice of the local repair, hierarchy,
cover, and hopset parameters, now using uncontracted compressed cores
and colored full-forest pools, gives the `6/7` factor in (C).

The resulting strong forest is initially a bounded-degree decremental
interface. To obtain a **general-graph** cut-tree theorem, every
guide-packing call first expands its current arbitrary-degree graph
into a degree-three graph with sufficiently high-capacity connectors.
All terminal minimum cuts are preserved exactly. This is repeated at
each call because later contractions can create high degrees.

The application also supplies a source-rooted multi-source forest, an
explicit distance-label transcript, a positive-length geometric-copy
adapter for length increases, and a finite MWU implementation on one
common dyadic grid. The output sparsifier has a common capacity scale,
so the skeleton construction receives polynomially bounded integers.
Both the skeleton size and its unweighted minimum-cut value are paid
before running tree packing.

One additional construction was needed during the audit. Directly
transferring the guide-tree mincut source routines did not justify the
claimed aggregate inventory: two leaf-recursion children could both
retain the same uncovered Steiner vertices. The new routine maximizes
the current candidate value over the source arm as well as the outside
branches. It then makes either one child retaining that region, or two
children with disjoint uncontracted regions. The accompanying proof
checks every constrained-cut case, the parameter-one base, contracted
target propagation, and the aggregate maxflow input size.

The comparison is stronger than the original printed exponent:

| Strong-forest comparison | Logarithmic overhead | Status |
|---|---|---|
| KMG printed specialization | `O(U^(83/84) h)` | Public theorem |
| Joint public reconstruction with direct vertex inventory | `O(U^(8/9) h^(1/9))` | Derived public-framework baseline |
| Earlier separated and anchored construction | `O(U^(7/8) h^(1/8))` | Previous research bound |
| Uncontracted compressed cores and full-forest pools | `O(U^(6/7) h^(1/7))` | Current internally audited research bound |

The current `8/9` comparison supersedes the earlier restricted
`62/63` retuning and does not claim optimality over all public
reanalyses. For the full
cut-tree composition, the external fixed-parameter adapter is stated
and proved explicitly. Two later-looking polylog-maxflow reductions
were withdrawn in April 2026 because their runtime arguments had gaps;
their claimed times are not used as established comparisons or imports.

The relevant English notes are
`six_sevenths_strong_forest_and_gomory_hu_checkpoint.md`,
`steiner_pool_no_reset_strong_forest.md`,
`public_forest_direct_vertex_inventory.md`, and the retained
application notes
`separated_metric_forest_and_strong_sssp.md`,
`gomory_hu_seven_eighths_dependency_audit.md`,
`deterministic_fixed_k_tree_mincut_adapter.md`, and
`public_strong_forest_retuning_baseline.md`. The independent forest,
multi-source, numerical, general-degree, and fixed-parameter audits
are included beside them.

## General maximum matching remains the original unrestricted target

The previous checkpoint's fastest bound remains

\[
 O(n+m)+(m_s+1)\exp O\!\left(
  (\log(m_s+2))^{4/5}(\log\log(m_s+4))^{1/5}\right),
\]

for an explicit exact maximum-cardinality matching in an arbitrary
undirected general graph, where `m_s` counts distinct nonloop edges.
It has not been replaced by a bipartite, approximate, regular, sparse-only,
or perfect-matching promise. There is no newly proved exponent below four
fifths for this original problem in the current checkpoint.

Its source is the OpenAI general-matching preprint and its deterministic
state interfaces, combined with the reconstructed carrier, projection,
router, and raw-cycle proofs. The exact provenance and remaining imports
are in `current_checkpoint/oai_baseline_and_imports.md`. The historical
directory name containing the word `Sparse` does not change the stated
general-graph scope.

The previous 107-note checkpoint is preserved under `current_checkpoint/`.
Its README and older exponent notes describe their own chronology; the
present README governs the new transfer claims. Historical approaches and
counterexamples are retained as dependency and boundary records, not as
additional current fastest results.

## Reading order and dependency map

For checkpoint F, first read **fully_dynamic_spanner_five_sixths.md**,
then **fully_dynamic_spanner_root_audit.md** and
**fully_dynamic_spanner_independent_audit.md**. The clipped-path
interface and fair current-source comparison are in their companion
notes listed in the opening section.

For the checkpoint E strong-forest and cut-tree improvement, first read
**six_sevenths_strong_forest_and_gomory_hu_checkpoint.md**, then
**steiner_pool_no_reset_strong_forest.md** and its two independent
audit notes. The public comparison is in
**public_forest_direct_vertex_inventory.md**.

For the earlier incremental directed SSSP transfer, read these files in order:

1. `transfer_public_baselines.md` — printed results, derived public
   comparisons, and attribution boundaries.
2. `frozen_barrier_distance_detector.md` — full single-lifetime potential,
   freezing, comparison, LOW, births, and numerical accounting.
3. `raw_cycle_to_frozen_detector_bridge.md` — integer prices, connectors,
   raw thresholds, exact cost, dyadic steps, and positive-flow retirement.
   `small_local_detector_exact_solver.md` supplies a direct exact
   negative-cycle solver below the actual-size hierarchy threshold.
4. `frozen_detector_incremental_sssp.md` — normalization, arbitrary degrees,
   births, child quotas, phase counts, explicit outputs, and the exponent.
5. `simple_path_reporting_from_tree_segments.md` — active tree versions,
   sparse path-intersection indices, segment-level cycle deletion, and
   output-sensitive simple paths up to logarithmic factors.
6. `frozen_barrier_detector_independent_audit.md` and
   `frozen_sssp_outer_independent_audit.md` — independent checks of the two
   mathematical layers, including the edge cases corrected during review.

For the numerical flow transfer, read `moving_box_log_barrier_flow.md`,
then its two independent audit notes and
`exact_flow_acceptance_and_reductions.md`.

For the corrected static comparison, read `public_dual_reoptimization.md`
and `public_dual_uniform_wrapper_audit.md`. The imported refining
partition, vertex-split, self-loop, and numerical source implementations
remain explicitly identified there.

For the raw backend, the principal retained files are
`current_checkpoint/quantitative_matching_4_5_composition.md`,
`current_checkpoint/sequential_expander_routing_tradeoff.md`,
`current_checkpoint/linear_parameter_static_sparsifier.md`,
`current_checkpoint/uniform_source_interfaces_for_4_5.md`, and the
raw-lift/lifetime/numerical-client notes they name.

## Work continuing after this checkpoint

This is an intermediate checkpoint. Further work concerns avoiding
the cumulative stretch loss in dynamic spanner sparsification,
complete path separation on cyclic matching allocation graphs,
payable potential-repair discovery, and further improvement of the
original matching backend. On the allocation route, the remaining
questions include stronger resource constraints and quality beyond
the current star certificate. The accepted rank-dependent factor
does not supply a uniform constant below four.
Neither a faster distance-only parameter choice nor a special-family
representative-maintenance lemma is automatically a faster matching
algorithm. Any provisional exponent for those directions is excluded
from the completed claims above until its complete interface and
accounting have been audited.
