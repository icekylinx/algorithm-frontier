# Proof note

This file is the curated proof record for the result in `README.md`. The original source note follows.

**Original source:** `sources/checkpoint-o/shared_setup_routing_budget_corank_flow.md`

# Selected concurrent flow with one shared setup and routing budget

**25 October 2026. New extension manuscript; root and independent audit requested.**

This theorem combines a fixed admission fee for each selected commodity
with the variable cost of routing it, charging both to one exact total
budget. The algorithm selects exactly q-c commodities from an allowed
family and obtains a `(1-epsilon)` fraction of the optimal common
normalized rate in `Gamma(1/epsilon)^c poly(H)` time. All capacities and
any additional fixed nonnegative routing-only budgets remain exact.

The combinatorial interface is stronger than a restriction selector:
it must find an exact minimum-setup-cost permitted set inside every
allowed ground. Weighted matroid optimization supplies it for one
matroid basis or two common bases. A separate unrelated selection-cost
constraint is not silently added to that oracle.

The main new composition uses the adaptive residual-budget gap:
at each omission node, compute the cheapest available setup, reserve
its actual cost, and test service on the entire current ground with
the remaining routing budget. The same promised set stays feasible
in every region on a suitable surviving branch.

## 1. Network, selection and shared cost

Let G=(V,E) be a directed network with finite nonnegative rational
arc capacities u_e. There are q commodities P. Commodity i has
distinct terminals s_i,t_i and a positive rational demand scale d_i.
A normalized rate lambda means routing lambda*d_i units for every
selected commodity. Flows are splittable and nonnegative.

Let B be a family of r-element permitted commodity sets, with
1<=r<=q, and put c=q-r. Each admitted commodity incurs a nonnegative
rational setup fee sigma_i. For I in B define

\[
                           s(I)=\sum_{i\in I}\sigma_i.
 \tag{SF1}
\]

The fee is charged for membership in I, independently of its routed
amount. Let w^0_ie>=0 be a rational per-unit routing cost and require
one shared budget C>=0:

\[
                  s(I)+\sum_{i,e}w^0_{ie}x_{ie}\le C.
 \tag{SF2}
\]

In addition, any explicitly listed polynomial-size collection of
fixed routing-only constraints is allowed:

\[
                    \sum_{i,e}w^h_{ie}x_{ie}\le C_h
                    \quad(1\le h\le m),
                 \qquad w^h_{ie},C_h\ge0.
 \tag{SF3}
\]

The original capacities, conservation equations and all these rows
remain unchanged throughout the algorithm. Unselected commodities
have zero flow. All input numbers and counts of constraints are
included in the binary input length H.

For an undirected physical edge use two directional flow variables
per commodity and one capacity on their combined total. Its cost
rows are on those actual directional variables. This construction
does not give each direction an independent copy of the capacity.

## 2. The required exact minimum-setup restriction oracle

For every Q subseteq P, assume a polynomial-time oracle computes

\[
                 h(Q)=\min\{s(I):I\in\mathcal B,\ I\subseteq Q\}
 \tag{SF4}
\]

and returns an attaining permitted set I_Q, or reports that none
exists. The value and witness have uniform polynomial encoding.
This optimization requirement is substantive: an arbitrary
permitted subset of Q need not leave enough budget for its routing.

For bases of a single rank-r matroid, minimum-weight basis selection
in its restriction supplies SF4. For common bases of two rank-r
matroids, minimum-weight cardinality-r matroid intersection supplies
it, with setup fees as weights. Unrestricted cardinality selection
is the uniform-matroid special case. Other families are permitted
only when the stated exact optimizer is supplied and paid for.

An ordinary restriction selector alone does not imply SF4. In
particular, adding a second, unrelated linear selection-cost cap
to common bases while optimizing setup cost would require a
different constrained optimization oracle. This theorem does not
infer such an oracle from weighted matroid intersection. The shared
cap on the same setup objective is already handled by comparing
h(Q) with C.

Compute h(P) first. If no permitted set exists or h(P)>C, report
that no legal selected set can satisfy the shared budget, even at
zero rate. Otherwise the setup-feasible family

\[
                    \mathcal B_C=\{I\in\mathcal B:s(I)\le C\}
 \tag{SF5}
\]

is nonempty, and I_P with zero routing is a legal initial output.
This distinction matters because zero routing does not waive the
setup fee. Rank-zero selection is handled separately by an empty
output, without assigning a finite minimum to no commodities.

## 3. Comparator and theorem

For I in B_C let lambda_I be the maximum common normalized rate
that its commodities can attain under the original capacities,
SF2 and SF3. Define

\[
                       \Lambda=\max_{I\in\mathcal B_C}\lambda_I.
 \tag{SF6}
\]

The selected set is an actual integral permitted set. Only its
flows are fractional. Because capacities are finite, demands are
positive and terminals are distinct, every lambda_I is finite.
The optima are attained by bounded rational flow LPs.

**Theorem SF.** For every rational epsilon in (0,1), a deterministic
algorithm either detects that B_C is empty as above or returns a
permitted set and explicit splittable routing of common rate at
least

\[
                 (1-\epsilon)\Lambda
        \quad\text{in time}\quad
                 \Gamma(1/\epsilon)^c\operatorname{poly}(H),
          \qquad \Gamma(R)=\frac{R^R}{(R-1)^{R-1}},
 \tag{SF7}
\]

using polynomial workspace. Its shared setup-plus-routing cost
is at most C, every routing-only budget is respected, and no
edge capacity is exceeded. Zero optimum is allowed.

This is an admission/common-rate theorem for splittable flow.
It does not supply unsplittable paths, integer multicommodity flow,
or paid installation of selected network edges. The physical graph
and capacities are fixed input data.

## 4. Residual-budget service regions and their separator

For B_0>=0, let U_(B_0) be the nonnegative normalized service vectors
z for which there are flows on the original q commodities satisfying

\[
 \begin{aligned}
 B_Gx_i&=d_i z_i(\mathbf1_{s_i}-\mathbf1_{t_i}) &&(i\in P),\\
 \sum_i x_{ie}&\le u_e &&(e\in E),\\
 \sum_{i,e}w^0_{ie}x_{ie}&\le B_0,\\
 \sum_{i,e}w^h_{ie}x_{ie}&\le C_h &&(1\le h\le m).
 \end{aligned}
 \tag{SF8}
\]

B_G is tail-positive. These are bounded explicit rational LPs.
The regions contain zero, are downward in service, and increase
with B_0. To reduce a commodity's service, scale its entire flow
down; every nonnegative capacity load and routing charge decreases.

The direct nonnegative separator from the selected-flow theorem
applies with SF8's current B_0. For completeness, take nonnegative
arc lengths ell_e, nonnegative multipliers kappa_0,...,kappa_m,
and real potentials pi_i satisfying

\[
 \pi_i(v)-\pi_i(w)
       \le\ell_e+\sum_{h=0}^m\kappa_h w^h_{ie}
                    \quad(e=(v,w)),\qquad
 \pi_i(s_i)-\pi_i(t_i)\ge0.
 \tag{SF9}
\]

Then the valid packing row has coefficients and capacity

\[
 a_i=d_i(\pi_i(s_i)-\pi_i(t_i))\ge0,\qquad
 H_0=\sum_eu_e\ell_e+B_0\kappa_0+
                      \sum_{h=1}^m C_h\kappa_h\ge0,
             \qquad a\cdot z\le H_0.
 \tag{SF10}
\]

Multiplying conservation by the potentials proves validity.
Farkas duality gives a strict certificate for every infeasible
nonnegative query. A negative terminal-gap commodity can have
its entire potential replaced by zero, preserving every arc
inequality and not decreasing the separating objective. This
proves that the coefficients may be chosen nonnegative.

Splitting potentials into positive and negative parts and bounding
the sum of all their coordinates, lengths and budget multipliers
by one gives the explicit bounded separator LP. Its maximum
excess is positive exactly for an infeasible query; zero is
always a feasible certificate. Exact rational optimization gives
polynomial-bit row coefficients. A feasible query is reconstructed
by the direct primal LP SF8.

This is the already independently reviewed finite Farkas interface
of `selected_multicommodity_flow_corank_scheme.md`. Every varying
B_0 below equals C minus an actual sum of original setup fees,
so the same uniform polynomial coefficient bounds apply. Additional
routing-only rows affect only the polynomial LP size.

## 5. The adaptive fixed-target algorithm

Fix a positive target T and put alpha=1-epsilon. At a recursive
allowed ground Q, let d=|Q|-r. Reject if d<0. Compute h(Q) and
an attaining I_Q through SF4; reject if no set exists or h(Q)>C.
Otherwise form the current residual budget

\[
                              B_Q=C-h(Q).
 \tag{SF11}
\]

Query the service vector alpha*T*1_Q in U_(B_Q). If feasible,
restrict its flows to I_Q and return that attaining set and
routing. The routing cost is at most B_Q, and its setup fee is
exactly h(Q). Thus their actual sum is at most C. All other
routing-only budgets and capacities survive restriction.

If infeasible, use SF10's nonnegative violated row. Enumerate
the weighted first-crossing omission certificates with ratio
R=1/epsilon and recurse on the remaining grounds, exactly as
in `adaptive_residual_budget_corank_gap.md`. If every child fails,
return full-target failure. At deficit zero a failed service
query is an immediate rejection.

The completion oracle and routing budget are recomputed at each
child. The attaining I_Q is retained for a successful node;
using a different permitted subset could have a larger setup
fee and would not justify this budget calculation.

## 6. Why an optimal selected set survives

Suppose some permitted I* has a full-T routing satisfying the
shared budget. Fix that set and routing throughout the proof.
At every recursive Q containing I*,

\[
                    h(Q)\le s(I^*),\qquad
                    C-h(Q)\ge C-s(I^*).
 \tag{SF12}
\]

Its original full-T routing therefore belongs to the current
U_(B_Q), even though B_Q can change later. For a violated row
a*z<=H_0 at the weak query alpha*T*1_Q,

\[
 T a(I^*)\le H_0<\alpha T a(Q),
       \qquad a(Q\setminus I^*)>\epsilon a(Q).
 \tag{SF13}
\]

The first-crossing argument supplies an enumerated deletion
certificate contained wholly in Q\I*. Its child retains I*,
so SF12 applies again with the new minimum setup cost. At
deficit zero Q=I*, and downward closure forces the weak service
query to succeed. Thus total failure soundly certifies that no
permitted set supports the full target T under the shared budget.

The local prefix-free branch mass and the full unfinished-word
enumerator depend only on R and d. The adaptive residual-budget
theorem therefore gives this target gap in
`Gamma(1/epsilon)^c poly(H)` time and polynomial space, including
off-promise inputs and failed minimum-setup calls.

## 7. Rational optimization preserves the full accuracy parameter

Once I in B_C is fixed, its exact optimum lambda_I is an ordinary
flow LP: set outside-I flows to zero, maximize lambda, and use
the residual routing bound C-s(I) in SF8. Its family B_C and
its objective are independent of every queried target.

A convenient uniform finite rate bound is

\[
                     V_0=\frac{\sum_{e\in E}u_e}{\min_i d_i}.
 \tag{SF14}
\]

For undirected networks the sum is over physical edges. Source
outflow bounds every normalized rate by V_0. If V_0=0 the legal
zero routing is already optimal. Otherwise impose lambda<=V_0
as a redundant bound in every fixed-I LP. All arc-flow variables
are bounded by capacities, so these LPs are bounded and nonempty.

Their common dimension n_0 and a uniform rational row-bit bound
L_0 are computable from the input. The only set-dependent right
side is C-s(I), a sum or difference of at most q+1 original
input rationals, whose binary length has a uniform polynomial
bound. Rowwise denominator clearing and Cramer's rule therefore
give the known denominator bound

\[
                 D=n_0!\left(2^{(n_0+2)L_0}\right)^{n_0}
 \tag{SF15}
\]

for every exact optimum lambda_I. Its encoding is polynomial.
Padding smaller formulations by zero-fixed variables handles
their dimension uniformly, including lower-dimensional faces.
Because B_C is finite, Lambda is one of these lambda_I and obeys
the same bound.

Write alpha=A/B in lowest terms and use target grid
delta=1/(2*B*D^2). Start at zero with the cheapest setup-feasible
set and zero routing. Use a grid upper endpoint strictly above
V_0. A successful target gap saves its actual set and moves the
lower endpoint; a failure puts its target strictly above Lambda
and moves the upper endpoint. No monotonicity of successes is
assumed.

At adjacent grid endpoints the lower L satisfies L>Lambda-delta,
and the saved set has lambda_I>=alpha*L. Reoptimize that fixed set
exactly. If lambda_I were below alpha*Lambda, rational separation
of two values with denominators at most D would force a difference
at least 1/(B*D^2), larger than the possible error alpha*delta.
Thus lambda_I>=alpha*Lambda. Return this exact fixed-set optimizer's
flows, which obey every original constraint.

This is the independently reviewed rational-comparator lemma.
Reoptimization is necessary because a target witness can have a
denominator depending on the artificial grid, whereas the original
fixed-set optimum has the uniform SF15 bound. The number of calls
is polynomial in the encoding of V_0, D and epsilon, and every
call uses the full requested ratio R=1/epsilon.

## 8. Feasibility, zero rates and storage

No positive initial rate is required for Section 7. If affordable
selected sets exist but all have rate zero, the saved setup-feasible
set and zero routing satisfy the theorem. Disconnected terminals,
zero capacities, zero shared budget and zero extra routing budgets
are all covered by the same primal/dual formulations.

The recursive stack has depth at most c<=q. Every local certificate
word has length at most q and polynomial-size counters. Minimum
setup optimization, exact flow LPs and fixed-set reoptimization
have polynomial-size data and workspace. No setup-cost split,
capacity, denominator or routed unit is enumerated numerically.

The output arc representation contains at most q times the number
of directed arcs coordinates. If a path representation is wanted,
standard flow decomposition and cycle removal preserve all
nonnegative charges and the common rate. This does not restrict
the output to one path per commodity.

## 9. Why the residual budget must be updated

A small example illustrates the shared-budget issue. There are two
commodities on disjoint arcs of capacity 100, both of unit demand,
and exactly one must be selected. Their setup fees are 0 and 80,
their per-unit route costs are respectively 100 and 1, and C=100.
The first commodity's maximum rate is one; the second's is twenty.

At the full candidate ground, h(P)=0. Once a branch keeps only
the second commodity, its attainable setup minimum becomes 80
and its remaining routing budget is twenty. Continuing to use
the initial remaining budget of 100 would permit a routing whose
actual setup-plus-route cost exceeds C. The algorithm recomputes
h(Q) and uses its attaining set, so it handles this interaction
without guessing or enumerating a numerical budget partition.

## 10. Scope and primary comparison

The fixed-commodity continuous baseline is classical. Mądry's
primary [*Faster Approximation Schemes for Fractional Multicommodity
Flow Problems via Dynamic Graph Algorithms*](https://madry.mit.edu/docs/multiflow.pdf)
defines concurrent flow with a routing-cost budget and notes its
polynomial LP formulation. Once the admitted set here is specified,
its setup fee is a constant and the same type of LP applies.

For the present combined selection problem, enumerating every
omitted c-set and optimizing its surviving permitted set exactly
gives a direct `q^{O(c)} poly(H)` baseline. The theorem instead
has a fixed polynomial degree and a single-exponential accuracy/
corank dependence, at the price of the stated relative rate loss.
It preserves the full combined budget rather than choosing two
independently supplied setup and route caps.

The general selected-flow theorem with routing-only budgets had
needed only a polynomial restriction selector. Sharing a budget
with setup fees requires the stronger exact minimum-setup
restriction optimizer specified in Section 2. One or two matroid
bases satisfy it; arbitrary extra exact selection constraints
cannot be imported without checking that stronger interface.

Only one scalar setup objective is optimized. Several fixed
routing-only budgets are safe because they are enforced throughout
all service LPs. Several unrelated setup-cost vectors would require
a common attaining completion or another argument; minimizing
them separately is not justified here.

The proof does not claim an approximation scheme for fixed-charge
network design, where selecting paid edges changes available
routing capacity. Here setup fees belong to admitted commodities
and do not change the physical network. A bounded source check
does not establish publication priority for this exact combined
parameterized theorem. The result is submitted for internal
mathematical audit, without formal-verification or external
peer-review claims.


---

**Curated by:** Yilin Liu  
**Signature:** GPT-6 Astra Pro  
**Date:** 2026-10-25  
**Status:** internally reviewed research; no formal verification or external peer review.
