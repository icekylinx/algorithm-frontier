# Root audit: unrelated values, shared setup, and the current transfer boundary

**25 October 2026. Full mathematical reading completed by the root reviewer.**

This audit records the accepted scope of the new joint-role allocation
results and their supporting transfers. It is an internal mathematical
review, not formal verification, external peer review, or an exhaustive
publication-priority determination. The original matching exponent is
outside the active research objective.

## 1. Arbitrary unrelated values: the shared-resource issue is resolved

The complete J1--J19 manuscript in
`unrelated_values_joint_role_near_two_allocation.md` passes this review.
Two distinct full independent reviews are retained in
`unrelated_values_joint_role_independent_audit.md` and
`unrelated_values_joint_role_second_audit.md`.

The essential change from the intrinsic-value theorem is to mask
player-type pairs, not entire resource types. A type may be light for
one player and heavy for another. Both roles use the same original
recipient-polymatroid constraint inside one joint LP and one rounding
operation. Treating the two roles as independent copies would duplicate
capacity and is not part of the accepted algorithm.

At a candidate light ground Q, real light pairs are allowed only in Q,
real heavy pairs only outside Q, and every outside player has total
count exactly one. The projected light-service region is tested for
nonemptiness before a support separator is requested. When nonempty
it is compact, downward, and contains zero. Normalized nonnegative
support separation is valid; membership corresponds to a nonpositive
support gap, including negative optimum values. The optimizer and row
encoding bounds come from fixed bounded rational inner LPs, not from
an assumed small support of the projected region.

A fixed full witness survives every protected omission: keep its full
light allocation, keep one heavy unit at still-heavy positions, and
discard newly light heavy recipients. Original costs are nonnegative
and resource feasibility is downward. The weighted first-crossing
certificate therefore contains a child avoiding the same protected
light set. The analysis bounds the complete recursion on all inputs,
including failed children and forced global-cover seeds.

Rounding uses the full prefix of each player's ordered pairs as well
as its proper prefixes. The resulting floor of total count guarantees
an integer heavy unit at outside positions. Light utility loses at
most the largest allowed light value. The same integer point preserves
the single assignment-cost objective. Exact masks prevent forbidden
pairs from reappearing. The optimization argument enumerates every
exact heavy count, handles the all-heavy case separately, and uses
one-sided searches without assuming successful calls are monotone.

The optional player-matroid adapter in J is valid only after integral
dummy recovery: remove the integral dual-matroid dummy support and
extract an actual original basis from its complement. Fractional dummy
support does not justify that extraction. The high-value adapter is
not a two-valued-instance preservation argument.

## 2. The shared setup and assignment budget

The complete SD1--SD15 manuscript in
`unrelated_allocation_shared_setup_budget.md` passes this review and
the two full reviews in
`unrelated_allocation_shared_setup_second_audit.md` and
`unrelated_allocation_shared_setup_polymatroid_audit.md`.

Here the original basis is selected and paid for. A persistent
zero-service resource with rank M* represents omitted players. Its
affine budget is

    real assignment cost + sum_p sigma_p - sum_p sigma_p y_p <= C.

The auxiliary dummy has negative linear cost and zero utility. It
must remain available in Q as well as outside Q. In particular it
cannot be discarded by the usual rule for zero-valued original pairs.
The protected full optimum retains its entire canonical dummy basis
while only nonnegative-cost original assignments are discarded.

The complementary full-face rounding proof optimizes an arbitrary
linear objective, so the signed auxiliary coefficients are legitimate.
After rounding, let D be the integral dummy support. It is independent
in M*. Consequently P minus D contains an original M-basis B. The
actual setup fee of B is at most the fee of all dummy-free players,
and its actual original assignment cost is at most the cost of all
original assignments. This converts the rounded affine budget into
the exact original budget. No negative-cost original instance is
claimed, and no negative dummy credit is removed prematurely.

Initial zero feasibility is checked by a minimum-setup original
basis. The role search adjoins zero to an empty positive-role benchmark
and retains that separately valid zero solution. This avoids assuming
that a zero-service witness exists in every role LP. The empty light
role is handled by an integral all-heavy/dummy quota face, not by an
unbounded light-service maximum.

For fixed rational R>1, both J and SD have approximation factor
2R/(R-1), whole-q time

    (2 - 1/Gamma(R))^q * 2^{O(q log log(q+2)/log(q+2))} * poly(H),
    Gamma(R) = R^R/(R-1)^(R-1),

and polynomial workspace. In SD, q is the number of nonloop candidate
players of the original M. All encoded resource ranks, costs, values,
fees, LP operations and paid rank-oracle operations belong to H.

## 3. Exact factor two at the enumeration endpoint

`exact_two_global_enumeration_unrelated_allocation.md` passes the root
review and the independent review
`exact_two_global_unrelated_transfer_audit.md`.

For each pair mask and light-role set, maximize full common real
service exactly in the signed-dummy joint LP and round once. The
optimal original allocation, at threshold OPT/2, supplies an enumerated
case with full light service at least OPT. Every light value is strictly
below OPT/2 and every heavy value is at least OPT/2. The recovered
original basis therefore has value at least OPT/2 and its original
combined budget is exact. The empty light role has its separate gate.

Streaming the 2^q role sets gives time 2^q poly(H) and polynomial
space. This is not a substitution of zero accuracy into the positive
gap formula. An exact factor-two algorithm with a uniform base below
two for arbitrary unrelated values remains unproved. The existing
strictly-below-two-approximation oracle lower bound does not settle
this endpoint.

## 4. Integer quota tradeoffs and the stronger one-value setup theorem

The complete quota proof
`integer_quota_approximation_time_tradeoffs.md`, its independent audit,
the unrelated-pair extension
`unrelated_two_value_integer_tradeoffs.md`, and its independent audit
all pass. For a fixed integer d>=2, set

    R_d = (d+1)/(d-1),  A_d = Gamma(R_d),  B_d = 2 - 1/A_d.

For K>=d+1 and b=ceil(K/d), the exact inequality
K/(K-b)<=R_d is valid. The targets K<=d use a separate exact one-unit
gate; they are not forced through a degenerate positive-gap call.
Exact integer quota recovery is optimization on an integral face,
not intersection with a budget row followed by an integrality claim.

The compulsory unrelated two-valued result includes pair values
{0,u,a} even when one resource type has different positive values for
different players. Its mixed count face preserves the same resource
capacity and the one exact assignment budget. The optional M adapter
does not automatically preserve this two-valued structure.

The stronger optional one-value setup theorem
`one_value_shared_setup_assignment_budget_tradeoff.md` passes the root
and full independent audit
`one_value_shared_setup_budget_transfer_audit.md`. It returns at least
ceil(K*/d) units under one combined setup and assignment budget.
At each restriction Q it queries the residual assignment region with
budget C-h(Q), where h(Q) is an attained exact minimum setup cost.
The returned basis is that same attaining basis. A protected full
basis has setup at least h(Q), so its full count allocation survives.
For the small-target gate, pair weight sigma_p+c_pj pays each selected
player's fee exactly once. This avoids an unsupported third matroid.

The two-size scheduling consequence of the quota theorem has factor
2-1/d and the same A_d-corank or B_d-global time. It keeps the full
physical ground in the small-job dual rank, even when large-job
positions are omitted. The accepted scheduling statement has no
arbitrary assignment-cost budget.

## 5. Sparse actual separators

`attained_set_sparse_separator_gap.md` and its independent full review
pass. Its width assumption concerns the support of every separator
actually returned on the tested attaining set, including forced seeds
and unpromised inputs. Sparsity of input constraints alone does not
imply sparse support after projection.

The finite-word recurrence defines beta(R,w), and its output-sensitive
prefix generator bounds work by actual children. An old generator that
still enumerated Gamma(R)^d prefixes would not establish the sharper
bound. For R=2,w=3 the recurrence is beta^(-1)+beta^(-2)=1, hence
beta is the golden ratio. The global base becomes (5-sqrt(5))/2.
For beta=1 the extension is directly polynomial; the global formula
need not be used outside its stated A>1 hypothesis.

The explicit application has two matroids, one exact selected-set
cost bound, and nonnegative packing rows of support at most three.
Capacity factor two has corank base phi and whole-q base
(5-sqrt(5))/2. It is a separate bicriteria packing theorem; it is not
an exact-budget arbitrary-value allocation theorem at that base.

## 6. Robust integer service: the positive result and its limit

The negative manuscript
`robust_unit_allocation_corank_obstruction.md` and its independent
audit pass. A fresh element makes the original player matroid
U_(q-k,q) nonempty in rank. A scenario indexed by S has the explicit
rank |A minus S|+min(|A intersect S|,|S|-1). A common basis has positive
integer service in every scenario exactly when its k-element
complement hits every source set. The optimum is zero or one.
Thus every finite multiplicative corank-FPT guarantee would imply
FPT=W[2]. This is an unbounded explicit-scenario statement, not a
whole-q lower bound or a rank-oracle information bound.

The positive companion
`robust_unit_allocation_additive_and_promised_two.md` and its full
independent audit also pass. For every K>=2, intersection of scenario
count regions permits the same positive gap and exact quota recovery,
performed separately in each scenario on the same selected basis.
Different budgets constrain different adaptive allocations.
The nominal K=1 call is a legal zero weak success, not a failure.
One-sided search therefore returns floor(K*/2) unconditionally, and
ceil(K*/2) whenever K*>=2. A supplied actual one-unit robust witness
fills the optimum-one case and gives the full factor-two guarantee.
The certificate is not an assumed polynomial solver for finding it.

## 7. Several exact costs on one integer allocation

`multiple_exact_assignment_budgets_obstruction.md` and its independent
review pass. One player, unit resources indexed by graph vertices,
and exact pair budgets x_u+x_v<=1 encode Maximum Independent Set.
The corank is zero. With an input-sized collection of such budgets,
an arbitrary fixed multiplicative guarantee in F(q) poly(H) time would
contradict the cited deterministic constant-approximation hardness
under P!=NP. A complete graph also provides an unconditional growing
fractional integrality gap. These statements do not rule out fixed
two-budget results, budget augmentation, or separate scenario-adaptive
budgets.

## 8. Baselines, attribution and remaining claims

`unrelated_allocation_primary_baselines.md` records the directly read
primary sources. In particular, the Jansen--Maack approximation scheme
already gives player-parameterized approximation in the ordinary
unbudgeted unrelated model. The current theorem is not the first
constant-factor FPT approximation by player count. The public
cost-preserving rounding results and monotone-local-search base
conversion are also credited separately.

What has been established internally is a broader exact-budget input
model and explicit exponential-time/quality tradeoffs, plus the
specified positive and negative transfer theorems. The ordinary-item
public baselines, the stronger arbitrary-rank oracle model, continuous
selected flow, integer allocation, and augmented-capacity packing
remain separate claims with separate hypotheses. No private OpenAI
baseline or unexamined manuscript is presumed validated.
