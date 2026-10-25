# Verification note

**Curated source path:** `sources/checkpoint-p/selected_flow_and_global_conversion_root_audit.md`

The source audit follows.

# Root audit: selected flow, exact rational optimization and global time

**25 October 2026. Full root read and independent reviews passed.**

This audit accepts the selected concurrent-flow theorem, its explicit
scenario and shared-budget extensions, the rational-comparator recovery,
the polynomial-space global gap conversion, and all applications in
the global transfer manuscript. These are mathematical derivations with
internal review, not formal verification or external peer review.

## 1. Accepted dependency chain

The main files read in full are:

- selected_multicommodity_flow_corank_scheme.md;
- robust_scenario_selected_flow_corank.md;
- shared_setup_routing_budget_corank_flow.md;
- exact_multi_budget_flow_hitting_set_reduction.md;
- rational_comparator_gap_optimization.md;
- polynomial_space_global_gap_conversion.md;
- global_gap_corank_profile_bound.md;
- global_exponential_allocation_flow_transfers.md.

The allocation and exact-budget prerequisites have a separate complete
root audit in unrestricted_budget_allocation_root_audit.md. The earlier
two-size scheduling theorem and weighted prefix-free gap theorem have
their own root and independent audits in checkpoints M and N.

## 2. Continuous selected flow has the required packing interface

For a fixed network and all original commodities, the normalized service
projection is downward closed. Reducing one commodity's service and
scaling its route cannot increase any nonnegative capacity or routing
budget use. Several routing budget rows remain permissible: they are
linear inequalities in a continuous LP, with no integer rounding step.

The explicit Farkas construction is essential. Edge-capacity and budget
multipliers are nonnegative, and each commodity has a potential. A
negative terminal gap is removed by replacing that commodity's entire
potential with zero. Because every edge right-hand side is nonnegative,
this replacement preserves the potential inequalities while increasing
the separation objective. The resulting service coefficients and row
capacity are nonnegative. A bounded normalized LP produces a strict
separator whenever the service query is infeasible.

The construction does not enumerate paths or assert that a projection
oracle automatically reconstructs a route. A separate direct flow LP
recovers actual flows after membership succeeds. Undirected arcs share
the capacity of their original physical edge. All supplied routing
budgets are respected by the recovered route.

The selector must return an actual permitted selected set. One or two
matroid bases and the stated single selection-cost threshold have the
necessary polynomial restriction implementation. Arbitrarily many
selection-budget constraints do not acquire such an implementation
merely because many routing-only constraints are permitted.

## 3. Exact rational recovery removes the second accuracy loss

For each fixed selected set I, let its original LP optimum be lambda_I.
The family and fixed-set objectives are independent of the queried
target. A uniform denominator bound D follows from the original bounded
rational LP coefficients, including the implicit integer rank rows when
they are present. The number of variables and the coefficient bit bound
are polynomial. A lower-dimensional feasible polytope still has a
vertex specified by a full-rank active subsystem on its ambient variables.

For a rational desired factor alpha=A/B in (0,1), use grid spacing
delta=1/(2BD^2). A gap success at T saves an actual set whose LP optimum
is at least alpha*T; a failure excludes any full-target optimum at T.
A finite external upper bound supplies one-sided grid search. The final
saved target exceeds the true optimum minus delta, even though successes
need not be monotone or certify full-target feasibility.

Reoptimize the saved actual set in its original LP. If its optimum were
strictly below alpha times the global optimum, the denominator bounds
would force a positive gap of at least 1/(BD^2), contradicting the saved
target guarantee. This establishes exactly the intended alpha, including
zero optimum, without assuming a positive starting scale.

The original LP is indispensable. A fine-grid routing witness itself
need not have the original denominator bound. Similarly, the argument
cannot be applied to a target-dependent family without a separate fixed
benchmark proof. For selected flow and the accepted fractional allocation
comparator, the corank base is consequently Gamma(1/epsilon), not the
earlier safe Gamma(2/epsilon).

## 4. Shared setup and routing preserve one protected witness

With setup charges sigma_i and a shared total budget C, the correct
restriction primitive is the exact minimum setup sum h(Q), accompanied
by an attaining permitted set I_Q. A feasibility-only selector is
insufficient. The node's routing region uses residual budget C-h(Q).

If a protected full-target set I* survives in Q, then h(Q) is at most
its setup cost. Its original full routing therefore remains feasible
under the current residual budget. At a successful node, restricting
the recovered flows to the attaining I_Q and paying its actual setup
cost meets C exactly. The optimizer is recomputed after every restriction;
a cheaper setup choice at an ancestor is not reused.

Before any rate search, the global minimum setup cost must be at most C.
Otherwise even zero service is infeasible. This is different from the
allocation model without setup charges, where zero counts on any legal
basis are free. Additional fixed routing-only budget rows remain valid,
but unrelated simultaneous setup objectives have no common attaining
scalar optimizer here.

## 5. Robust scenarios and exact-rate limitations

For an explicit nonempty scenario list, the service region is the
intersection of all scenario service regions. A nonnegative row from
one violated scenario is valid for the intersection. The selected set
is shared, while actual routing is allowed to adapt to the scenario.
The fixed-set optimization LP includes the full scenario list, giving
the same rational recovery and the same exponential parameter.

The independent Hitting Set reductions correctly establish separate
exact-admission obstructions. One uses many explicit scenarios and no
routing budgets; another uses one scenario and many routing budget
rows. Their chosen set has size q-k, so its complement is a hitting set
of size k. Padding a smaller hitting set to k preserves hitting.

These prove W[2]-hardness of the stated exact-rate decisions under the
usual parameterized interpretation, using the standard solution-size
Hitting Set baseline. They do not prove hardness for a fixed positive
relative error, a single unconstrained scenario, a single shared routing
budget, or only one-edge-failure scenarios.

## 6. The global conversion counts every seed and uses polynomial space

The conversion requires a full-target/relaxed-target extension interface:
for every forced omission Z, the subroutine has an all-input bound
A^(c-|Z|) times a uniform polynomial and cannot fail when an original
full-target witness survives. It may output any valid relaxed solution.
The protected selected set alone is restricted by Z; original heavy
options and physical resource data are retained.

For a logarithmic block of size n with p omitted positions, choose k
minimizing

\[
 T_{n,p}(k)=\frac{\binom nk}{\binom pk}A^{p-k}.
\]

The exact weighted average with weights
binom(p,k)(A-1)^k/A^p is at most (2-1/A)^n.
A greedy cover of all p-subsets by contained k-subsets needs at most
(n+2) binom(n,k)/binom(p,k) members. Since each block has at most
floor(log_2 q) positions, its entire cover construction has polynomial
time and storage.

All omitted-count profiles are enumerated, and each Cartesian product
of local covers is streamed. The true omitted set has one profile, and
some product seed lies inside it. The corresponding extension cannot
fail. Multiplying cover sizes by each residual extension cost bounds
every call, including unsuccessful seeds:

\[
 (2-1/A)^q
 2^{O(q\log\log(q+2)/\log(q+2))}\operatorname{poly}(H).
\]

Only polynomial local tables, counters and one reused extension
workspace are stored. The small-ground case enumerates complete omitted
sets and invokes deficit-zero extensions. It does not hide a numerically
large A in the base case.

The corank-sensitive refinement uses the same local minima and the same
algorithm. For every analytical x>=0 their common upper bound multiplies
to [A/(1+x)]^c[1+x/A]^q. Optimizing gives exactly the two cases in P10.
No random balancing, Stirling substitution or interchange of an unknown
profile with an algorithmic minimum is needed. Complete c-set enumeration
likewise uses deficit-zero gap calls, not an unstated exact fixed-set solver.

For fixed rational accuracy, the constant comparisons are exact algebraic
comparisons of bounded degree. For varying binary accuracy, the safe
rational A=3R supplies the explicitly stated uniform version; expansion
of numbers with a numerical-size exponent is not hidden in poly(H).

## 7. All-instance applications preserve their complete algorithm bounds

The exact factor-two one-value and compulsory two-value allocation
algorithms and exact three-halves two-size scheduling use A=27/4,
giving base 50/27. General intrinsic allocation uses A=Gamma(R), giving
factor 2R/(R-1). Every heavy support cardinality and every value split
is processed, so these global guarantees require no small-support
promise. The optional raw-corank fallback is omitted or separately
globalized; executing it unchanged could spoil the displayed base.

Forced light omissions retain every original heavy recipient pair.
An omitted position can still be a heavy recipient in the completion.
This is not a deletion of the whole original player.

In scheduling, the small-job complement rank is built on all physical
machines before restriction to eligible large positions. A forced
omission only forbids a large position. Small jobs may still be placed
there, and the integral complement is completed on the full original
machine set. The exponent counts the explicit eligible large-position
ground, bounded by the number of physical machines; it never counts
binary expanded slots as if they were machines.

The balanced hidden-set constructions show a nearly 2^q deterministic
rank-query requirement for factors strictly better than two in the
specified allocation models and strictly better than three halves in
the specified scheduling model. They do not prove that the base 50/27
is optimal at the threshold factor, and do not imply ordinary explicit
item-eligibility hardness.

## 8. Public attribution and current disposition

The numerical conversion A^k to (2-1/A)^(q+o(q)) is public monotone
local search, due to Fomin, Gaspers, Lokshtanov and Saurabh:
[author manuscript](https://sites.cs.ucsb.edu/~daniello/papers/monotoneLocalSearch19.pdf)
and [arXiv record](https://arxiv.org/abs/1512.01621).
Its permissive-extension discussion is relevant. Its conclusion states
a subexponential-space overhead for its presented derandomization;
polynomial space here rests on the separate block proof just audited.
No claim of priority for that space refinement is made.

For ordinary Budgeted Santa Claus, the checked public comparison is
Rohwedder, Rouhani and Wennmann,
[ICALP 2025](https://doi.org/10.4230/LIPIcs.ICALP.2025.127):
a randomized polynomial logarithmic approximation with exact cost.
Our constant guarantees have a different, exponential time regime and
the explicitly stated polymatroid and selection scope. Bamas et al.,
[arXiv:2307.08453](https://arxiv.org/abs/2307.08453), supplies the
public scheduling fractional relaxation and additive-largest-job
rounding used in the easy branch.

The exact-admission reductions use the standard Hitting Set baseline
recorded in [Jansen, JGAA 2017](https://jgaa.info/index.php/jgaa/article/view/paper413).
The earlier bounded public OpenAI index audit remains an index-level
comparison, not access to an unpublished internal baseline.

All named results above are accepted for checkpoint O. Extensions beyond
their stated input models remain separate research tasks. In particular,
the unrelated-value multiplicative route under current investigation is
not assumed anywhere in these accepted proofs.


---

**Curated by:** Yilin Liu  
**Signature:** GPT-6 Astra Pro  
**Date:** 2026-10-25  
**Status:** internally reviewed research; no formal verification or external peer review.
