# Independent audit of the adaptive residual-budget gap

**25 October 2026. Reviewer: the allocation/corank branch.**

I read `adaptive_residual_budget_corank_gap.md`, RB1--RB12 and all
interface and scope conditions. The theorem passes this independent
audit. A globally fixed packing region is not necessary for this
extension, because the proof establishes the stronger local invariant
needed for each visited node. The same promised selected set and its
same completion witness remain feasible on a suitable surviving
branch.

## 1. The minimum must be exact and attained

For any node Q containing a promised selected set I*, its fixed
completion W* is a candidate in the minimum defining h(Q). Hence
h(Q)<=h(W*). This fact requires neither an exchange argument nor
an extension of W*. A polynomially computed lower bound without
an attaining completion would not suffice for the output step;
an approximate minimum might exceed h(W*) and would not suffice
for promise preservation. The statement requires both exactness
and an attaining pair.

At a successful node, the algorithm uses that very pair (I_Q,W_Q).
Serving all of Q at budget C-h(Q), then restricting to I_Q, costs
at most C-h(Q). Its completion costs exactly h(Q), so the actual
sum is at most C. Replacing I_Q by an arbitrary permitted subset
could require a more expensive completion and would invalidate
this argument. The manuscript does not make that replacement.

## 2. One fixed witness survives the changing regions

Fix a promised pair (I*,W*) and a node with I* subseteq Q. Exact
minimum completion and budget monotonicity give

    t*1_(I*) in U_(C-h(W*)) subseteq U_(C-h(Q)).

Thus its full target belongs to the particular region separated
at this node. For a violated nonnegative row, with W=a(Q),

    t*a(I*) <= u < b*W,
    a(Q\I*) > (1-b/t)*W = W/R.

The same fixed omission set Q\I* therefore has a first prefix whose
omission density crosses 1/R. Deleting that prefix's one-positions
keeps I*, and at the child the same argument applies using the
original W*. No claim that an earlier row describes the later
region is needed or used.

At deficit zero, a surviving Q equals I*, and downward closure
forces the weak query b*1_Q to be feasible. The promised branch
cannot reject there. This closes total-failure soundness, including
the cases in which other branches lose every promised pair.

The regions happen to shrink as Q shrinks, but that fact alone
would not preserve a feasible witness. The explicit comparison to
h(W*) is the substantive invariant, and it is present at every
recursive level.

## 3. The weighted enumeration analysis is unchanged

Once a valid local violated row is obtained, branch certificates
depend only on its nonnegative order, the fixed ratio R and the
current omission deficit d. Their prefix-free Bernoulli accounting
and the bounded-ones/zeros generator are exactly those already
proved in the weighted prefix-free theorem.

In particular, both the weighted branch sum at most one and the
local `(q+1)*Gamma(R)^d` state bound remain true when different
nodes obtain rows from different regions. The recurrence pays
local generation and oracle work before summing over every
attempted child, including children rejected by a completion or
budget test. Induction using |certificate|>=1 yields the stated
polynomial factor times `(d+1)*Gamma(R)^d` total cost.

The uniform polynomial bit bound for h(Q) is important: residual
budgets are formed afresh from original data and an actual minimum,
rather than by successively manipulating previously separated
coefficients. The stated hypothesis prevents recursive encoding
growth. The explicit ground caps both recursion depth and local
word depth, so depth-first implementation has polynomial storage.

## 4. The interface boundaries are substantive

The proof permits one shared scalar budget between service and
completion, together with other fixed constraints that are already
part of every service region. It does not justify independently
minimizing several completion-cost coordinates: one actual
completion need not attain all componentwise minima.

Service feasibility must interact with the completion only through
the stated relation and budget. In the intended allocation transfer,
heavy and light are disjoint original intrinsic-value type classes.
For recipient-dependent heavy/light classification, one original
resource could be used on both sides. The minimum-cost completion
might then consume light capacity needed by the promised witness,
and the budget comparison would not prove inclusion of that witness
in the current service region. The main note explicitly excludes
that unsupported transfer.

The service witness must also be safely restrictable at no increased
cost. This is true for independent recipient allocations and for
splittable routing with nonnegative charges, but not automatically
for mandatory full-base allocation on a newly restricted support.
The statement includes this condition rather than assuming it.

## 5. Result of the review

The proof supplies a valid new interface for dynamic residual
budgets, not a silent invocation of the older fixed-region lemma.
Its full-target failure guarantee, relaxed constructive success,
single-exponential corank time and polynomial space are consistent.
No substantive mathematical correction is requested.

Two minor wording edits were sent to the author: remove a stray
plus sign before "reconstruction" in Section 6, and describe stack
entry size rather than search-tree width when stating polynomial
space. These do not affect the proof. This is an internal
mathematical audit, without formal-verification or publication-
priority claims.
