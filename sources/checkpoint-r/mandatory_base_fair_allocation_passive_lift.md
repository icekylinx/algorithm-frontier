# Mandatory-base fair allocation through a charged passive-coordinate lift

**25 October 2026. Complete theorem. Root, allocation_four and
transfer_frontier have independently passed the full manuscript.
The two separate reviews are mandatory_base_passive_allocation_four_audit.md
and mandatory_base_passive_transfer_audit.md.**

The independent-resource allocation scheme can discard units to obtain
a bounded big-value profile. A mandatory resource base cannot be
trimmed that way. The following construction preserves every resource
unit and its real cost: each original coordinate has an active copy
and a passive copy, which share the original capacity. Passive units
contribute zero only to the auxiliary utility used by the algorithm.
They remain assigned, are charged their original costs, and are
merged back into the output.

This gives a deterministic (1-epsilon)-approximation for max-min
utility over a mandatory base of one arbitrary integral polymatroid,
including an optional actual player-matroid basis and one exact
shared setup-plus-assignment budget. The time is

    binomial(q,r) exp(O(r/epsilon)) poly(H_epsilon),              (PB1)

and space is polynomial in the full binary input. For one utility
block, it gives a 2^{O(1/epsilon)} scheme for maximum-value matroid
or integral-polymatroid base under one exact upper budget. A single
lower-bound side row is handled by reversing the rounding objective.

## 1. Model and original mandatory total

Let E be an explicit ground partitioned into q recipient blocks
E_p, p in P. Let F be a normalized monotone integral submodular
rank on E, with original rank

    R=F(E).                                                     (PB2)

A resource allocation is an integer vector x in B(F): x is
nonnegative, x(S)<=F(S) for every S, and x(E)=R. This full base
is mandatory.

The selected recipients form an actual basis B of an original
player matroid M of rank r>=1 on P. A given eligibility mask is
A_0 subset E. Counts must be supported on

    A_B=A_0 intersect union_(p in B) E_p.                       (PB3)

Original M-loops are never selected, but their removal from
available assignments never changes the original R. Every target
and every selected-set restriction retains PB2.

Coordinate e has nonnegative rational value v_e and assignment
cost c_e. Recipient p has nonnegative rational setup fee sigma_p.
The original budget is

    sigma(B)+c*x<=C,       C>=0.                                (PB4)

The objective is to maximize

    min_(p in B) sum_(e in E_p) v_e x_e.                        (PB5)

Let OPT denote its integer optimum on the original feasible
family. This model does not permit unused resource units. If
F is a direct sum of type ranks, x(E)=R forces every original
type base. For a general F, only its actual rank constraints and
global base total are imposed; extra named type totals are not
automatically implied.

H includes the explicit coordinates, partition, numerical data
and paid polynomial rank, SFM, LP and polymatroid-intersection
work. For rational 0<epsilon<=1, put

    H_epsilon=H+size(epsilon).                                  (PB6)

All multiplicities and the full accuracy numerator/denominator
are binary encoded.

## 2. Exact feasibility must precede the target search

An affordable setup basis alone need not support the mandatory
resource base. Enumerate all r-subsets of P, retaining only actual
M-bases. For each B:

1. Reject it if sigma(B)>C.
2. Form A_B and reject if F(A_B)<R.
3. Minimize actual assignment cost on P(F restricted to A_B)
   with total R, and reject if the minimum exceeds C-sigma(B).

The base polytope is integral, so a feasible candidate gives an
actual integer base x_0. If all candidates fail, the original
instance is infeasible, even at zero requested utility. Otherwise
save one complete pair (B_0,x_0) as the nominal target-zero output.
It may already have positive utility, but nonnegative utility is
all the initialization invariant needs.

This is an explicit binomial(q,r) enumeration. No polynomial
simultaneous selection oracle is presumed. In particular, a
minimum-setup basis can fail the resource-rank check even when a
more expensive selected basis is feasible.

If R=0, every feasible resource vector is zero and the initialized
solution is optimal. If all eligible original values are zero,
the same holds. For player rank zero, the selected set is empty:
resource feasibility requires R=0, and the empty-set objective
convention is handled separately from PB5.

At later target attempts the setup and rank checks are recomputed.
No exponentially large list of feasible bases is stored.

## 3. The active/passive lift preserves the resource exactly

Fix a candidate B that passed the setup and rank checks. On the
real ground A=A_B, let F_A be the restriction of F. Its rank is
still R. Replace every real coordinate e by two coordinates
e^a and e^p in the same recipient block, and let pi map each copy
to e. Define

    D=A x {a,p},
    Fup(S)=F_A(pi(S))       for S subset D.                    (PB7)

This is a normalized monotone integral submodular rank. For the
submodularity check,

    pi(S union T)=pi(S) union pi(T),
    pi(S intersect T) subset pi(S) intersect pi(T).

Submodularity and monotonicity of F_A then give
Fup(S)+Fup(T)>=Fup(S union T)+Fup(S intersect T).

For any nonnegative copy vector z, define its aggregate by

    x_e=z_(e^a)+z_(e^p).                                      (PB8)

There is an exact feasibility equivalence

    z in P(Fup)  iff  x in P(F_A).                             (PB9)

In one direction, apply the lifted inequality to the full preimage
pi^(-1)(T) of any T subset A. In the other, for any S subset D,
z(S)<=x(pi(S))<=F_A(pi(S))=Fup(S).

The totals in PB8 agree. Therefore

    z in B(Fup)  iff  x in B(F_A).                             (PB10)

Every integer split of an integer original base is a lifted
integer base, and aggregating any lifted integer base gives an
original integer base. The two copies do not have independent
resource capacities. A coordinate with original capacity k can
use at most k units in total across its two copies.

Both copies receive the same actual cost c_e. Thus

    sum_(d in D) c_(pi(d)) z_d = c*x.                          (PB11)

The same identity holds for any other supplied scalar side-weight
vector. Only the auxiliary utility distinguishes the two copies.
There are 2|A| encoded coordinates, not R unit copies.

## 4. Target utilities and the bounded active profile

Fix T>0. Active coordinate e^a has capped auxiliary value

    w_(e^a)=min(v_e,T),       w_(e^p)=0.                       (PB12)

The original utility of the aggregate is at least the auxiliary
active utility. A unit of original value at least T supplies T
after capping, so full *integer* target feasibility is preserved.
No claim is made for every fractional target witness.

Take

    delta=epsilon/3, J=floor(1/delta), K=ceil(1/delta),
    b=ceil((1-delta)/delta^2).                                  (PB13)

Active coordinates with capped value at most delta*T are small.
The other active normalized values lie in disjoint intervals

    (lambda_i,mu_i],
    lambda_i=delta+i*delta^2,
    mu_i=min(1,delta+(i+1)*delta^2),       0<=i<b.                (PB14)

All passive coordinates are retained with auxiliary value zero.
So are original zero-value active coordinates. They cannot be
deleted from a mandatory-base model merely because they have
zero utility.

At each selected player enumerate integer active big-bin counts

    h_i>=0,  sum_i h_i<=K,
    L=sum_i lambda_i h_i<=2,
    U=sum_i mu_i h_i.                                          (PB15)

Only occupied active big bins are stored. Passive copies create
no additional positive bin or player block.

## 5. A full target base can be relabeled without deleting any unit

Suppose an original integer base x* on B* gives every selected
player utility at least T. Capping its values retains this target.
At one player, consider its original assigned big units.

If their total capped value is at least T, mark active the first
prefix of any unit order that reaches T. Mark all remaining units
passive. The active big total is below 2T. Before its final unit,
the sum is below T, so the active count is at most ceil(1/delta).

If big total is below T, mark every big unit and the original
small units active. The big count is again at most K, and the
original small units supply the remaining target. Any additional
zero-valued units can be assigned either label.

Perform these relabelings at all selected players. By PB10, the
result is still a full lifted resource base. By PB11, its actual
cost is unchanged. No original assigned unit, resource dependence
or side-weight contribution has been removed.

Its active big counts satisfy PB15. In the first case U>=1 and
no active small utility is needed. In the second, U*T bounds the
actual active big utility from above, so active small utility is
at least max(0,1-U)T.

The reference to unit orders is only an existence proof of a
bounded active count pattern. The algorithm never enumerates
individual units or their identities.

## 6. The fixed-profile LP remains a mandatory lifted base

For a fixed B and its profiles, solve one rational LP with

    z in B(Fup),
    sum_(e^a in big bin i of p) z_(e^a)=h_(p,i),
    active small utility at p >=max(0,1-U_p)T,
    sum_(d in D)c_(pi(d))z_d<=C-sigma(B).                       (PB16)

Every passive coordinate is an ordinary, costed coordinate of
this base LP. The total remains R; unused capacity is not sent
to a free disposal location. By Section 5, some enumerated LP
contains the relabeled original full-target witness.

Resource separation uses Fup(S)=F_A(pi(S)), one rank-oracle
evaluation after forming an image set. The objective and bin
coefficients are rational with polynomial encoding. Counts are
bounded by original singleton ranks, so feasible rational witnesses
have polynomial bit length in the stated exact LP model.

## 7. Direct base complementation and the correct cost objective

Let z be a feasible fractional point of PB16. Define

    d_f=Fup({f}),
    G(S)=Fup(D minus S)+d(S)-R.                                (PB17)

This is a normalized monotone integral submodular rank, and

    y=d-z in B(G)  iff  z in B(Fup).                           (PB18)

The proof is the direct base-complement identity: singleton
bounds ensure nonnegativity, the total is d(D)-R, and inequalities
on complementary sets give the required rank inequalities. A
marginal of G is d_f minus a marginal of Fup and is nonnegative.

For each selected player order its active big bins by decreasing
surrogate lambda_i*T, then all remaining coordinates by decreasing
auxiliary small value. All passive and original zero-value
coordinates remain at value zero in this order. Put big coordinates
first when the last big surrogate ties a small value.

Impose ceiling-prefix caps ceil(y(S)) in every player's order.
The maximum-prefix ranks form one integral player-side polymatroid
K_player, and it contains y. The intersection

    P(G) intersect P(K_player) intersect {y'(D)=G(D)}            (PB19)

is a nonempty integral maximum-total face. Maximize the true lifted
cost vector c^up on y' over this face. Take an integral maximizer
and complement it back to z'=d-y'. Then z' is still a full
lifted base, and

    c^up*z' = c^up*d-c^up*y' <= c^up*d-c^up*y = c^up*z.          (PB20)

For every player prefix S,

    z'(S)>=d(S)-ceil(y(S))=floor(z(S)).                         (PB21)

The full base, every prefix bound and the cost comparison hold
at the same integer point. There is no disposal coordinate and
no post-round deletion of real active or passive coordinates.

Aggregate both copies using PB8. The result is an original
integer base of total R, supported on the same selected B, with
actual assignment cost no larger than the LP cost. Its setup
fee has not changed. Hence PB4 holds exactly.

## 8. The large-value boundary errors vanish

Use surrogate lambda_i*T on active big bin i, true capped values
on active small coordinates, and zero on passive coordinates.
This is the nonincreasing order used in Section 7.

For ordered surrogates s_1>=...>=s_m>=0, summation by parts and
PB21 give

    s*z' >= s*z
       -sum_h (s_h-s_(h+1))*(Z_h-floor(Z_h)),                  (PB22)

where Z_h is the fractional prefix count and s_(m+1)=0.

Inside an active big bin the value difference is zero. At the
end of a big bin, the prefix is a sum of the integer active
bin counts h_i specified in PB16. Its fractional part is zero.
This includes the boundary from the last active big bin to the
small group. Passive units all lie later at auxiliary value zero
and do not disturb these integer prefixes.

Only small-group differences can contribute loss, and they
telescope to at most delta*T. Meanwhile fractional surrogate
utility at p is at least [L_p+max(0,1-U_p)]T, and

    0<=U_p-L_p<=K*delta^2.

Therefore the integer auxiliary utility is at least

    (1-delta-K*delta^2)T >=(1-epsilon)T.                        (PB23)

Indeed K<=1/delta+1 and
delta+K*delta^2<=2delta+delta^2<=7epsilon/9<=epsilon.
After aggregation, original utility is at least active surrogate
utility, because all original values are nonnegative and passive
copies regain their original values in the output.

No exact active-bin count is required after rounding. The prefix
inequalities already prove PB23. Retaining the passive units and
their real cost is what makes the same argument compatible with
mandatory bases.

## 9. Complete theorem, enumeration and exact target search

**Theorem PB.** For rational 0<epsilon<=1, the algorithm detects
original infeasibility or returns a genuine selected M-basis and
an original integer resource base satisfying PB4 with utility
at least (1-epsilon)OPT. Its time obeys both

    binomial(q,r) binomial(b+K,K)^r poly(H_epsilon),
    binomial(q,r) exp(4r(J+1)) poly(H_epsilon),                 (PB24)

with the parameters in PB13, and its space is polynomial.

For each basis, occupied active-bin profiles are streamed using
the same monotone count/lower-load pruning as PA. A partial
profile always has an all-zero completion. The weighted partition
injection maps h_i to h_i parts of size J+i, of total at most
floor(2/delta^2)<2(J+1)^2. The cumulative partition product
bound is exp(4(J+1)) per selected player. Thus all bad candidate
bases, failed profile LPs and traversal overhead are included
in PB24.

The lift doubles the coordinate dimension but leaves the number
of player blocks and active positive bins unchanged. Complement
rank values are at most 2|E|R and remain binary. Only the current
basis, current profile counters, one exact solver state and the
best actual original solution are stored.

A full integer target supplies a successful basis/profile attempt
by Sections 5–6. Conversely, every success is a legal original
base with utility at least (1-epsilon)T. Exhaustive failure
therefore implies T>OPT.

Choose a rational grid g dividing all positive original values.
Every integer utility and OPT lies on it. The global bound

    V=R*max_(e in E) v_e                                       (PB25)

is finite, is a grid value, and upper-bounds OPT. If there are
no positive values, the original feasible initializer is optimal
at zero. Otherwise initialize nominal L=0 with that actual
mandatory base and external U=V+g. Complete failure at T lowers
U; success raises L and saves its actual output. U remains
strictly greater than OPT. At U=L+g, grid integrality gives
L>=OPT, proving the claimed guarantee without additional loss.

No weak-success monotonicity is assumed. The number of targets
is polynomial in the original binary encoding. In particular,
this is an exact target-grid proof for MAX-base variants and
does not require estimating an unknown positive optimum first.

## 10. One exact scalar lower side row

For fixed recipient blocks, the same proof supports a single
nonnegative side-weight condition

    w*x>=L                                                     (PB26)

in place of the upper cost budget. There is no simultaneous
additional arbitrary cost budget in this corollary.

Give active and passive copies the same weight w_e. Relabeling
a target witness leaves its side-weight value unchanged. In the
fixed-profile LP impose PB26. On the complement face PB19,
**minimize** w^up*y', so that

    w^up*z'=w^up*d-w^up*y' >= w^up*d-w^up*y=w^up*z>=L.

The lower-prefix and utility proofs are otherwise unchanged.
Initial feasibility is determined by maximizing w over the
original allowed base. An attaining base of weight at least L
is a legal nominal zero-target initializer. If none exists,
the original constrained family is empty.

In the one-block case, PB24 and PB26 therefore give both
maximum-value base variants with one exact scalar side row,

    max v*x over x in B(F), with w*x<=C or w*x>=L,

in 2^{O(1/epsilon)} poly(H_epsilon) time and polynomial space.
For a matroid rank, this includes the corresponding matroid
basis problems. The ordinary independent-set variants can be
completed to a base with a free zero-value, zero-side-weight
disposal coordinate before this construction; that auxiliary
completion serves optional resources, whereas the passive
copies here always retain their original real weights.

## 11. Robust mandatory-base fair allocation

The proof also composes over a nonempty explicit scenario list
with one common selected M-basis and adaptive scenario allocations.
Each scenario may have its own global F_omega, original mandatory
rank R_omega, values, assignment costs, setup vector and exact
combined upper budget.

Enumerate B once and initialize only if every scenario passes
its original-rank and minimum-cost base check. At a target T,
run the fixed-B passive-lift routine separately in each scenario.
If any scenario fails, discard B; if all succeed, keep that same
B and their separate original full-base outputs. A robust full-T
witness supplies a protected profile in every scenario. Thus
the robust target gate has the same one-sided semantics.

The scenario searches add, not multiply. Using a common original
value grid and the minimum of the scenario total-value upper
bounds gives a robust (1-epsilon) integer-OPT guarantee with
the same PB24 profile factor and polynomial dependence on the
complete scenario input. The explicitly many output vectors
have polynomial total encoding. No single integer allocation
is required to satisfy several independent cost budgets.

## 12. Scope and relation to the other profile results

This note strengthens global independent-resource allocation to
mandatory global bases. It also includes ordinary recipient-type
bases by taking F to be their direct sum. In that special case
every original type total remains mandatory, including units
marked passive in the analysis.

The lift has no new independent capacity, no cost-free reassignment
of real units, no uncharged passive resource, and no shared
fractional selected-basis relaxation. The original selected basis
is fixed before each LP and before rounding.

Objective blocks are still disjoint. Extra named type equalities
must be encoded in the resource rank when F is not a direct sum.
Multiple exact side rows on the same integer vector, or an
intersection of unrelated global resource polymatroids, are not
covered by this scalar-objective integral-face proof.

The public budgeted-matroid and fixed-player approximation-scheme
comparisons are recorded in
`global_polymatroid_profile_transfers.md` and
`recent_profile_scheme_baseline_audit.md`. This manuscript proves
the new mandatory-base interface directly. It does not assert
publication priority or formal verification.
