# Root audit: local eligibility padding and safe machine contraction

**25 October 2026. Completed internal mathematical review.**

This audit accepts the full compositions in
`machine_eligibility_padding_and_collision_makespan_draft.md` and
`safe_machine_contraction_rank_kernel_draft.md`. Their historical
draft filenames do not indicate an outstanding proof gap. Separate
independent full audits accompany both files. The statements remain
conditional on their explicitly computed bottleneck certificates;
neither is an unconditional improvement for every size distribution.

## 1. The collision threshold uses feasible units, not nominal sizes

For each machine, retain at most two copies of every eligible large
type's size, respecting its singleton rank. The two cheapest entries
give its least possible two-unit collision; C2 is the minimum over
machines. A selected pair is independently feasible in the relevant
type polymatroids and extends to their bases. Thus the calculation
has the stated exact pair interpretation. Only its lower-bound
direction is needed for the approximation theorem.

Every target below C2 has distinct large recipients. If the large
Boolean cap loses total rank, OPT>=C2, so largest-job additive
rounding is an appropriate easy branch. If C2 is infinite, every
aggregate singleton rank is at most one and the large resource is
already a matroid. There is no Boolean rank loss in this case.
Moreover each eligible machine has only one eligible large size,
so its eligibility width is zero. If C2<a_plus, the hard target
interval is empty; the theorem remains valid through its easy branch.

## 2. Independent position commitments preserve a residual promise

An arbitrary independent commitment F0 of size h-k may differ from
the unknown optimal large-recipient basis I*. Nevertheless I* spans
the contraction by F0. Therefore I* minus F0 contains a residual
basis J*. Restricting the original optimal workload-dual vector to
J* preserves feasibility and its per-machine lower promise.

Only the player matroid is contracted here. The workload dual is
formed on the full original machine ground, then restricted to the
residual player set. Its original singleton eligibility bounds remain
valid. No preliminary large-type assignment to F0 or J* is assumed.

## 3. Padding withdrawal and the final load bound

Let A be the largest residual eligible size and H_width the largest
within-machine size width. Then L=A-H_width>=a_minus>0. The grid
Delta=g/A_D for rational D=A_D/B_D makes K=L/Delta and b=K/D
positive integers. Private capacities d_p=(L-ell_p)_+/Delta are
also integers and turn the nonuniform promise into K units.

Withdrawal is a full rank proof: for y in P(f+d), any S has
E={p in S:y_p>d_p}, and

    (y-d)_+(S)=y(E)-d(E)<=f(E)<=f(S).

Consequently the returned b units leave original dual workload
at least max(0,L/D-(L-ell_p)_+) on p. If ell_p>=L, the load
overhead is at most A-L/D. If ell_p<L, it is at most
H_width+(1-1/D)L. These coincide, giving

    E_D=((D-1)A+H_width)/D.

This estimate remains valid when the retained workload truncates
to zero. Completing the original dual base, complementing, then
decomposing and rounding the small workloads adds at most the
largest small size u at each residual machine. On a committed
machine, the final actual singleton-rank bound W_p+a_p applies
after rounding, so an additional u must not be added there.

The hard-target guarantee is therefore

    max{T+E_D+u, B(F0)}.

The unconditional coefficient is the maximum of the hard coefficient
1+E_D/a_plus and the easy coefficient 1+a_plus/C2. The original
public additive schedule remains an independent candidate. The
separate term B(F0) cannot be suppressed without an additional
certificate. Every failed target is original integer infeasibility,
so the finite-grid one-sided minimization search is sound.

## 4. Exact scalar padding optimization and its limitation

For arbitrary padding scale L0 the retained workload is

    w_p(L0)=max(0,min(L0/D,ell_p-(1-1/D)L0)).

At a proposed overhead C<A, only machines with a_p>C constrain
L0. The simultaneous interval is

    D(A-C)<=L0<=D(C-H_active(C))/(D-1),

for D>1. This proves the stated breakpoint algorithm, including
strict treatment of a_p=C. The refined grid g/(A_D B_D) makes
all engineered quotas integral. For D=1 the minimum overhead is
H_width directly.

The manuscript correctly limits the significance of this scalar
refinement. For 1<=D<=3, strict improvement forces a maximum-width
machine inactive. It then witnesses C2<=2E_D-H_width. Writing
x=H_width/A and e=E_D/A, one has x<=e<=(2+x)/3, hence

    e(2e-x)<=((2+x)(4-x))/9<=1.

It follows that the old easy coefficient already dominates the old
hard coefficient. Thus scalar optimization alone does not improve
the unconditional maximum in this range, although it sharpens the
conditional additive certificate. This limitation is retained.

## 5. Safe absorption is a different contraction operation

Safe machine absorption assigns the full current marginal of every
type to a removed machine p. Its load is

    c_p(F)=sum_j p_j [f_j(F+p)-f_j(F)],

which decreases as the removed set F grows. For each type the
recorded assignments form a greedy base on F. The residual rank
is the actual contraction f_j/F on P minus F. Unlike position
commitment, this operation may absorb many large units on one
machine, and no original Boolean-rank hypothesis is needed.

Any base a of f|F and any base b of f/F combine to an original
base. For U subset F and V disjoint from F,

    a(U)+b(V)<=f(U)+f(F union V)-f(F)<=f(U union V).

The final inequality is submodularity. The total counts telescope
to f(P), so there is no hidden compatibility condition between
the committed base and the chosen residual base.

## 6. The original optimum dominates a residual optimum

For every original integer base x, the contracted resource g=f/F
has an integer base z<=x restricted to Q=P minus F. The box-rank
formula proves this because, for all A subset Q,

    g(A)+x(Q minus A)>=f(P)-f(F)=g(Q),

with equality at A=Q. The manuscript's alternative union-of-tight-
sets proof also establishes existence directly. Applying the lemma
independently to each job type gives OPT_F<=OPT. This proof does
not require the committed greedy counts to agree with an optimum.
The any-base combination lemma handles precisely that distinction.

Thus a residual guarantee alpha_F OPT_F+e_F combines with a safe
load bound B as max{B,alpha_F OPT+e_F}. Both terms are necessary.

## 7. Threshold closure and all-budget certificates

At threshold B, absorb any machine with c_p(F)<=B until none is
left. The final set is independent of choices: if one legal prefix
is contained in another terminal set G, its next chosen p cannot
lie outside G, since diminishing marginals would give
c_p(G)<=c_p(F)<=B and contradict terminality. Reversing the
comparison proves uniqueness; comparing thresholds proves nesting.

One minimum-current-marginal order computes all these closed sets.
The individual recorded costs may decrease, so the correct
nondecreasing profile is their prefix maximum B_i. A threshold
closure is the longest prefix with B_i<=B. For a desired remaining
large rank k, take the first prefix reaching that rank and complete
its entire equal-B_i plateau. Its bottleneck beta_k is the smallest
threshold for this rule. The computation uses O(q^2 t) original
rank queries for t explicit types and polynomial binary arithmetic.

The optimality statement applies only to full-marginal threshold
absorption. It does not claim optimal machine preassignment under
a load budget. Original h>q with one common large size already
admits a public three-halves guarantee via OPT>=2a, so merely
displaying a five-thirds residual bound there would not establish
a numerical improvement. Zero-large-rank, favorable bottleneck,
and local-eligibility cases retain their separate useful guarantees.

## 8. Conclusion of review

Both complete compositions pass. Their nontrivial correctness
points are the full-ground dual, globally feasible padding withdrawal,
post-rounding commitment bound, dominated contracted base, and
order-independent threshold closure. Binary capacities remain
compressed throughout. These proofs supplement the accepted
allocation and scheduling core; they are not a substitute for the
stronger newly reviewed corank theorems.
