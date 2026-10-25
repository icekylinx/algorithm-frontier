# Verification note

**Curated source path:** `sources/checkpoint-o/shared_setup_routing_budget_independent_audit.md`

The source audit follows.

# Independent audit of shared setup-plus-routing selected flow

**25 October 2026. Full independent read of SF1--SF15 in
`shared_setup_routing_budget_corank_flow.md`.**

The theorem passes. Given an exact minimum-setup-cost restriction
optimizer, selected splittable concurrent flow with one shared
setup-plus-routing budget admits the stated deterministic
`Gamma(1/epsilon)^c poly(H)` relative scheme with polynomial space.
All edge capacities and every additional listed nonnegative routing-only
budget remain exact. The selected set is integral and has the required
cardinality; its routing is fractional.

This audit checks the composition of the adaptive budget lemma, the
explicit nonnegative flow separator, and rational-comparator recovery.
The stronger selection interface and zero-rate feasibility distinction
are essential and are present in the manuscript.

## 1. The combinatorial optimizer has precisely the required strength

For every allowed ground Q, the oracle computes the minimum actual
setup fee over permitted r-sets contained in Q and returns an attaining
set I_Q. Minimum-weight matroid basis selection supplies this for one
matroid; minimum-weight cardinality-r intersection supplies it for
common bases of two rank-r matroids. The finite list of setup fees is
the original weight vector in both constructions.

A feasibility selector alone would not suffice: a returned feasible set
could cost more than a full-target witness and leave too little routing
budget. Likewise, a lower bound on the minimum setup cost without an
attaining selected set would not justify the final combined cost. Both
the exact value and its attaining set are supplied here.

The same setup cap does not add a further combinatorial optimization
constraint; the algorithm simply compares the minimum h(Q) with C.
A separate unrelated selection-cost cap would change the optimization
problem and is explicitly excluded unless a corresponding stronger
oracle is available. Weighted intersection by itself is not claimed to
optimize one objective subject to another arbitrary hard budget.

All setup fees are nonnegative, and each returned h(Q) is a sum of at
most r original rational fees. Thus these values have uniform polynomial
encoding, independently of the omission history. Restricting Q only
removes available selected sets; it never changes an individual set's
original setup fee.

## 2. The service region and its direct separator are valid

For a fixed nonnegative residual bound B_0, the flow variables satisfy
the original conservation equations, capacity rows, routing-only budget
rows, and the shared budget's routing-cost row with right side B_0.
All costs are nonnegative. Scaling down one commodity's entire flow
decreases its service and cannot increase any of these loads. The
projected service region is therefore downward and is monotone in B_0.
It contains zero, including when some or all budgets are zero.

Every individual arc-flow coordinate is bounded by a finite capacity.
For each commodity, demand times normalized service is its source's
net outflow, which is at most its total source outflow and hence at most
the sum of physical capacities. Positive demand and distinct terminals
therefore bound service as well. The primal feasible set and projected
service region are bounded rational polytopes.

For lengths ell, budget multipliers kappa, and potentials pi satisfying
the stated arc inequalities, multiplying conservation by pi and summing
gives

\[
 \sum_i d_i(\pi_i(s_i)-\pi_i(t_i))z_i
 \le \sum_e u_e\ell_e+B_0\kappa_0+
                    \sum_{h\ge1}C_h\kappa_h.
\]

The signs match the tail-positive incidence convention. The row is valid
for every feasible service vector. Farkas duality supplies a strict
violating certificate for an infeasible query. If a commodity's terminal
potential gap is negative, replacing its *entire* potential by zero
preserves its arc inequalities because their right sides are nonnegative,
and increases or preserves the separating objective at a nonnegative
query. Thus all final service coefficients can be nonnegative.

After splitting real potentials into positive and negative parts, the
homogeneous certificate can be normalized by the sum of all lengths,
multipliers, and split-potential coordinates. The resulting explicit LP
is bounded. Its optimal excess is positive exactly for an infeasible
query; zero is always feasible. Exact rational optimization yields the
required strict nonnegative row. No positive lower bound on a budget or
capacity, or on an available path cost, is assumed.

At recursive nodes, the changing B_0 is C minus a sum of original setup
fees. Thus all separator LP descriptions have a common polynomial bit
bound. The polynomial number of additional fixed routing-only budgets
increases only the LP size and does not affect this argument.

For an undirected edge, the two directional variables share one capacity
on their sum. The same physical-edge length multiplies that capacity in
both directional arc inequalities. This correctly prevents an unintended
doubling of available capacity.

## 3. The changing residual budget preserves one fixed promised set

Fix a full-target witness consisting of a permitted set I* and its
routing, with actual combined cost at most C. At every recursive ground
Q containing I*, its original setup fee is still an available candidate.
Hence

\[
 h(Q)\le s(I^*),\qquad C-h(Q)\ge C-s(I^*).
\]

Its unchanged full-target routing therefore belongs to the *current*
service region. This is the needed paired-witness invariant. The proof
does not assume that the routing budget is constant throughout the tree.

If the weak query alpha*T on all members of Q violates the nonnegative
row a*z<=H_0, then

\[
 T a(I^*)\le H_0<\alpha T a(Q),\qquad
 a(Q\setminus I^*)>(1-\alpha)a(Q).
\]

The weighted first-crossing construction consequently enumerates a
deletion certificate wholly inside Q\I*. Its child retains I*, and the
same original setup-and-routing witness implies the invariant there.
At deficit zero, Q=I*, so downward closure makes the weak query feasible.
This proves that total failure excludes every full-T selected routing.

On success, the weak routing serves every member of Q. Restricting it to
the particular attaining set I_Q leaves rate alpha*T on that set and
cannot increase any capacity or nonnegative routing charge. Its setup
fee is exactly h(Q), so the actual combined cost is at most
h(Q)+(C-h(Q))=C. A different feasible selected set would not supply this
budget equality; the manuscript consistently uses the attaining one.

The provided example correctly identifies why the residual budget must
be recomputed: deleting a cheap setup alternative can raise h(Q).
Continuing to spend the initial larger routing budget could overrun the
shared cap. Recomputing h(Q) at each child resolves this while preserving
the original protected witness.

## 4. Time accounting includes failed and unpromised calls

The target gap uses the original ground cardinality deficit c=q-r and
ratio R=1/epsilon. The local first-crossing certificate family and its
prefix-free charge depend only on this ratio and the remaining deficit.
They do not depend on a fixed routing polytope or a fixed residual budget.

Every node's completion optimization, separator, and reconstruction has
a uniform polynomial input length and cost. The accepted weighted
prefix-free recurrence therefore applies unchanged, including nodes
where no permitted selected set remains or h(Q)>C. It bounds a complete
target call by Gamma(1/epsilon)^c times a polynomial. The number of
additional routing-only budgets is paid inside that polynomial.

Each recursive deletion removes at least one commodity, so the stack
depth is at most c<=q. Local certificate words have at most q bits,
and all exact LPs and optimization witnesses have polynomial encoding.
Depth-first traversal consequently uses polynomial space. Numeric setup
amounts, routed units, and capacities are not enumerated.

## 5. The fixed original comparator permits full-accuracy recovery

First restrict the comparator to the fixed family B_C of permitted
r-sets with setup fee at most C. This family is independent of every
queried target. For a specified I in B_C, its original fixed-set problem
is an exact flow LP with routing budget C-s(I), all original capacities
and fixed extra routing budgets, and a single common rate variable.
It is nonempty at zero and bounded.

The finite bound V_0=sum_e u_e/min_i d_i is valid even with cycles,
because net source outflow is at most total outgoing flow. In the
undirected representation the sum is over physical capacities, as
required by the shared directional constraint. If V_0=0, every possible
positive service is excluded and zero routing is optimal.

A common ambient formulation can keep all commodity-flow coordinates
and fix the outside-I coordinates to zero. The number of variables is
therefore uniformly bounded. Every set-dependent residual budget is a
sum or difference of at most q+1 original rationals. This gives a known
uniform row-bit bound L_0, not merely a bound on queried separator output.
Rowwise denominator clearing and Cramer's rule give the displayed
D=n_0!*(2^((n_0+2)L_0))^n_0 bound on every fixed-set optimum's denominator.
Zero-fixed padding and active equality rows cover lower-dimensional
feasible polytopes.

Because B_C is finite, its optimum Lambda is one of those fixed-set
optima and satisfies the same denominator bound. For alpha=A/B, the
delta=1/(2BD^2) grid search has an external upper bound above V_0.
Only sound failures lower the upper endpoint, so the final lower target
L obeys L>Lambda-delta. Its saved set has lambda_I>=alpha*L, regardless
of whether gap successes are monotone or exceed Lambda as nominal targets.

Exactly optimizing the *original* fixed-set LP of the saved I returns a
value with denominator at most D. If it were below alpha*Lambda, their
positive difference would be at least 1/(BD^2), contradicting the error
smaller than alpha*delta. This proves the stated (1-epsilon) ratio with
Gamma(1/epsilon)^c, without spending a second part of epsilon on target
search. Reoptimizing an LP that still includes the artificial target
would not establish this denominator claim; the manuscript uses the
correct original problem.

The number of target calls is logarithmic in V_0/delta+2 and hence
polynomial in the input bit length, log D, and the accuracy encoding.
There is no loop proportional to the numeric denominator D.

## 6. Zero-rate and infeasible-setup cases are properly distinguished

Membership in the selected family incurs setup fees even at zero rate.
If h(P)>C or no permitted set exists, no legal selected r-set can be
returned and the theorem correctly reports infeasibility. If h(P)<=C,
the attaining set with zero routing is legal and supplies the initial
search witness. This remains true when all possible concurrent rates
are zero, and rational recovery does not require a separately computed
positive rate scale.

Disconnected terminals, zero capacities, zero shared budget and zero
extra routing budgets are handled by the exact primal and separator
formulations. If selection rank is zero, the explicit empty-output
convention avoids assigning a finite minimum rate to an empty set.
The theorem itself uses positive selection rank.

## 7. Accepted scope

The complete composition passes. It preserves one shared scalar
setup-plus-routing cap and any fixed polynomial-size list of nonnegative
routing-only caps. One or two matroid bases supply the required exact
minimum-setup oracle. Extra selection constraints are allowed only if
that stronger oracle remains available.

Several unrelated setup objectives cannot be minimized independently
and combined: their minima may be attained by different sets. No such
extension is claimed. Setup charges here belong to admitted commodities
and do not change the physical network; the proof is not a fixed-charge
network-design algorithm. It returns splittable fractional routing,
not an unsplittable or integral multicommodity solution.

The direct exact enumeration of omitted c-sets remains a q^{O(c)}
baseline for this model. The proved improvement is the stated fixed
polynomial degree with single-exponential accuracy/corank dependence
under a relative rate guarantee. This audit makes no publication-priority
claim beyond the manuscript's bounded primary-source comparison.


---

**Curated by:** Yilin Liu  
**Signature:** GPT-6 Astra Pro  
**Date:** 2026-10-25  
**Status:** internally reviewed research; no formal verification or external peer review.
