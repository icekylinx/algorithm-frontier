# Checkpoint M: single-exponential corank algorithms with matched oracle thresholds

**25 October 2026. English intermediate research checkpoint.**

The active direction is entirely the transfer to related optimization
problems. The original general-graph matching 4/5 bound is preserved
as history and has not been further optimized. This checkpoint adds
three complete allocation and scheduling algorithms, a stronger
single-exponential search analysis, and reviewed structural scheduling
extensions. It preserves checkpoint L's notes and earlier provenance.

All new headline proofs have completed root and independent internal
mathematical review. This is not external peer review, formal
verification, an implementation, or an exhaustive novelty claim.
The ZIP contains English mathematical notes and a manifest only.

## 1. The principal results

Let H denote the full encoded input and paid oracle/bit complexity.
All numerical capacities and output counts remain binary encoded.
All algorithms below are deterministic and use polynomial workspace.

| Problem | Output guarantee | Parameter and all-input branches | Running time |
|---|---|---|---|
| Unit-value allocation, arbitrary player matroid M and arbitrary integral recipient polymatroid f | each selected basis member receives at least ceil(OPT/2) units | c = number of nonloops of M minus rank M | (27/4)^c poly(H) |
| Two-size makespan, arbitrary integral job polymatroids | makespan at most 3 OPT/2, exactly, without an additive smaller-job term | if the large Boolean cap retains large total rank h, c = number of eligible large positions minus h; otherwise a polynomial easy branch applies | (27/4)^c poly(H), or polynomial in the easy branch |
| Two-value allocation, arbitrary integral recipient polymatroids, every player compulsory | every player receives value at least OPT/2 | nu = maximum number of distinct players simultaneously coverable by one large unit each | (27/4)^nu poly(H) |

For the fixed four-unit-promise/two-unit-output core, the sharper
time is 4^c poly(H). For compulsory two-value allocation, the number
of large-cap coloops can be subtracted from nu in the nonempty core.

The approximation thresholds are matched by self-contained
value-oracle lower bounds: any strictly smaller uniform factor
requires binomially many queries and cannot have F(parameter)
times a polynomial input bound with a uniform polynomial degree.
This does not prove optimality of the exponential bases. It also
does not give hardness for ordinary assignment instances represented
by explicit lists.

These corank regimes complement the earlier rank-based algorithms.
For example, a large-recipient basis may be very large while leaving
few eligible positions unused. The earlier five-thirds scheduling
algorithm instead depends on the number h of large units. Neither
parameter is automatically small when the other is small.

## 2. The new mechanism: branch on a required omission batch

The central promise problem is to find a basis receiving b units
per selected player, or prove that no basis can receive t units,
where t>b>=1 are integers. At a current player ground Q retaining
rank r, let d=|Q|-r. Separate the candidate b*1_Q against the
recipient polymatroid by deterministic submodular minimization.

If there is no violated rank inequality, every player in Q could
receive b units, so any player basis inside Q is a valid output.
Otherwise, for a deficient set S, let

    m=|S|,     ell=m-floor(f(S)/t).

Every t-unit basis omits at least ell elements of S. Since the
whole ground contains only d omitted positions, ell>d soundly
rejects the target. This guard is tested before enumerating anything
and is essential for the running time on unpromised inputs.

In the remaining case, branch on all ell-subsets D of S and delete
D. At least one branch preserves any fixed promised basis. Each
branch spends ell units of corank, and the deficiency implies

    ell > m/R,      R=t/(t-b).

The finite binomial estimate gives

    binom(m,ell) <= Gamma(R)^ell,
    Gamma(R)=R^R/(R-1)^(R-1).

Counting even candidate deletions rejected by rank tests, the entire
computation tree has at most (c+1)Gamma(R)^c nodes. This improves
the earlier single-deletion R^c c! estimate to a single-exponential
bound for each fixed quota gap. Depth-first subset enumeration uses
polynomial space. All recursive resource queries are restrictions
of one fixed original resource; they are never undocumented
contractions or newly recomputed duals.

The cases t=4,b=2 and b=ceil(t/2) give Gamma(2)=4 and at most
Gamma(3)=27/4, respectively. The exact one-unit Boolean-matroid
intersection handles t=b=1 separately.

Principal notes:

* `unit_quota_corank_gap_branching.md`;
* `unit_quota_corank_batch_branching_improvement.md`;
* `corank_quota_and_three_halves_independent_audit.md`;
* `corank_quota_batch_and_scheduling_second_audit.md`;
* `corank_batch_allocation_scheduling_root_audit.md`.

## 3. Why the scheduling guarantee is exactly three halves

For job sizes a>u>0 and a target a<=T<2a, every feasible schedule
has at most one large unit on a machine. Cap the small-job resource
at C=floor(T/u), first verifying preservation of its full rank s.
Form its complement dual on all original machines P:

    f_T(S)=C|S|+g(P minus S)-s.

Only then restrict the player ground to eligible large positions.
A target schedule gives a large-recipient basis with at least

    K=C-floor((T-a)/u)=ceil((a+Cu-T)/u)

dual units per selected machine. The corank routine supplies
b=ceil(K/2). Zero extension, integer dual-base completion and
complementing in C*1 give an original integer small-job base.
Writing delta=a+Cu-T, one has 0<delta<=a<=T, and each selected
machine's load is at most

    T+delta-bu <= T+delta/2 <= 3T/2.

The counts remain integral throughout, so this branch has no
additional +u. Targets at least 2a use public largest-job additive
rounding. If the original large Boolean cap loses rank, every
schedule has a collision and OPT>=2a, so that same polynomial
additive algorithm already gives three halves.

The target search is a one-sided search on the exact rational size
grid. It does not assume monotone success. Failed targets are below
OPT; adjacent endpoints force the final successful target at most
OPT. Machines excluded from large-job selection are still present
in the original small resource and reconstruction.

The complete manuscript is
`two_size_makespan_corank_three_halves_transfer.md`.

## 4. A second factor-two application: compulsory two-value allocation

Let N be the Boolean cap of the large-valued recipient resource.
Any feasible target allocation has a large-recipient support R
independent in N. Extend R to an N-basis F. Its complement is an
N*-basis consisting only of players who received no large unit in
the original target allocation. They each had at least ceil(T/u)
small units.

For 0<T<=2a, apply the unit corank theorem to this dual player
matroid. Give the returned basis half the promised small quota,
rounded upward, and its complementary large basis one large unit
per player. Every player gets at least T/2. For T>2a, the public
all-player additive allocation primitive gives T-a>T/2 from a
feasible fractional assignment. A failed branch certifies original
target infeasibility, permitting the exact-grid optimization search.

This theorem is for compulsory players. The easy additive branch
does not automatically extend to arbitrary optional player
selection. The unit-value theorem above does permit that more
general selection model. Keeping these two scopes separate is part
of the proof, not a cosmetic distinction.

Read `two_value_allocation_large_cover_two_transfer.md` and
`two_value_large_cover_factor_two_independent_audit.md`.

## 5. The matched oracle thresholds

For an unknown r-set A among q players, use the rank oracle

    f_A(S)=min(2|S|,2r)-1[|S|=r]+1[S=A].

The manuscript proves this is a valid integral polymatroid. Every
r-player basis can get one unit, and a basis can get two units
only if it is A. The oracle differs from its symmetric reference
at just that query. Thus a deterministic below-two algorithm
requires at least binom(q,r)-1 queries. Writing c=q-r gives the
same bound binom(q,c)-1 in corank.

Dualizing this resource in the all-twos box gives a two-size
scheduling instance with OPT=2. A factor strictly below three
halves must output integral loads at most two and identify A.
For compulsory allocation, add a large-value-two uniform resource
covering q-r players. A value at least two for every player again
reveals the same hidden small-only set. Its large-cover parameter
is nu=q-r, matching the positive theorem's parameter.

Fixing the parameter above any proposed uniform polynomial degree
proves the stated FPT-oracle impossibility below the thresholds.
The results say nothing about the best exponential base at the
threshold, ordinary NP-hardness, or explicit special representations.
The construction and all boundaries are in
`recipient_polymatroid_below_two_oracle_barrier.md`.

## 6. Structural extensions also completed in this checkpoint

### Local eligibility and actual collision thresholds

The reviewed padding theorem uses the smallest and largest large
sizes eligible at each residual machine, ell_p and a_p. Let
A=max a_p, H_width=max(a_p-ell_p), and L=A-H_width>0. Private
modular dual capacity turns the nonuniform ell_p promise into a
uniform L promise. Withdrawal is globally valid because

    y in P(f+d) implies (y-d)_+ in P(f).

For a unit-core loss D, the hard-target load overhead becomes
E_D=((D-1)A+H_width)/D, plus the explicitly retained largest-small-
job loss u. It also uses the exact smallest possible two-large-unit
collision C2. This can exploit small within-machine size ambiguity
even when global large sizes have a wide spread. A committed
machine set retains its separate absolute bottleneck B(F0).

The resulting guarantee is

    max{ max(1+a_plus/C2,1+E_D/a_plus) OPT+u, B(F0) }.

An optional polynomial scalar optimization sharpens the hard-target
certificate. The manuscript also proves a limitation: for the
stated D<=3 range, a strict scalar improvement alone cannot reduce
the unconditional maximum, because the easy collision coefficient
already dominates. This prevents an overstated numerical claim.

### Safe full-machine contraction

A second reduction absorbs whole machines, assigning all current
rank marginals of every job type at a certified load. The resulting
contracted instance has OPT_F<=OPT: each original base dominates
a contracted base on the remaining machines. Any committed
restricted base combines with any contracted base.

Diminishing marginal loads make threshold closure order-independent.
One minimum-marginal greedy order computes every closure and the
smallest threshold beta_k for reducing remaining large rank to k
under this particular rule. A residual algorithm with guarantee
alpha_F OPT_F+e_F therefore gives

    max{beta_k,alpha_F OPT+e_F}.

The bottleneck is essential. The reduction is not asserted optimal
over arbitrary preassignments, and no unfounded worst-case quality
improvement is inferred when beta_k is large.

The two main files, their independent audits, and
`local_eligibility_and_safe_contraction_root_audit.md` are included.

## 7. Public and OpenAI comparison

The public polymatroid framework provides polynomial factors
4+epsilon for compulsory two-value allocation and 7/4+epsilon
for two-size scheduling, together with the additive primitives
used here. These are quality/runtime comparisons in different
parameter regimes. Current-source qualifications and the corrected
DRZ version history are retained from L.

The official OpenAI collection index was rechecked. Its nearby
common-polymatroid-base counting and three-machine precedence
scheduling entries have different stated objectives and constraints.
General integer points of a scaled player-base polytope do not
impose the all-or-nothing quota condition. A bounded index search
does not establish absence of every related result or publication
priority. Details and primary links are in
`corank_public_and_oai_baseline_recheck.md`.

## 8. Continuing work, kept outside this snapshot

Two active extensions are being separately written and reviewed:
arbitrary-value allocation through workload aggregation and lower
rounding, and generic packing-capacity selection through a
restriction oracle. They are not needed for the three accepted
headline theorems and are not promoted by this snapshot. Their
completed statements, if accepted, will appear in a later checkpoint.

The preserved L material includes the general-value factor-four
rank-based algorithm, stronger residual-configuration comparator,
fractional XP optimizer, full-cut gap example, and detailed
adversarial review of the earlier ordered-layer core. They remain
useful in regimes not covered efficiently by the new corank bounds.
