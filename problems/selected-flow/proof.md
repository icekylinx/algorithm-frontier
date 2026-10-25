# Proof note

This file is the curated proof record for the result in `README.md`. The original source note follows.

**Original source:** `sources/checkpoint-p/selected_multicommodity_flow_corank_scheme.md`

# Near-optimal concurrent flow with few rejected commodities and exact selection constraints

**25 October 2026. New research manuscript; root and independent review requested.**

This note gives a direct network-flow application of the independently
reviewed weighted prefix-free omission theorem. In a directed or
undirected capacitated network, select exactly r of q commodities
from a family with a polynomial restriction selector, and maximize
their common normalized throughput. Put c=q-r. For every rational
epsilon in (0,1), the algorithm obtains

\[
                (1-\epsilon)\mathrm{OPT}
       \quad\hbox{in time}\quad
                \Gamma(1/\epsilon)^c\operatorname{poly}(H),
       \qquad
                \Gamma(R)=\frac{R^R}{(R-1)^{R-1}},
 \tag{F1}
\]

with polynomial workspace. It preserves the selected family, all
edge capacities, and any explicitly listed polynomial-size collection
of nonnegative total routing budgets exactly. Flow is splittable;
no rounding loss occurs. The selector may impose an exact matroid
basis or two exact common
bases, as well as one linear selection-cost bound when weighted
matroid intersection implements that selector.

The sharper base uses exact reoptimization and the independently
reviewed rational-comparator lemma in
`rational_comparator_gap_optimization.md`. The earlier relative-search
route with Gamma(2/epsilon)^c remains in Section 7.1 as an alternative.
The proof includes a finite, explicit LP that separates the projected
service region by nonnegative packing rows. Thus it does not assume
that an arbitrary convex projection comes equipped with the needed
kind of separator. The public comparison in Section 9 is bounded
and makes no publication-priority claim.

## 1. Model and comparators

Let G=(V,E) be a finite directed network with nonnegative rational
arc capacities u_e. Commodity i in P={1,...,q} has distinct terminals
s_i and t_i and a positive rational demand scale d_i. A common
normalized rate lambda means routing lambda*d_i units for every
selected commodity. All these quantities are binary encoded.

A feasible routing consists of nonnegative arc flows x_ie satisfying
the usual flow-conservation equations and the shared capacities
sum_i x_ie<=u_e. Optionally impose an explicit collection of s
nonnegative routing budgets

\[
                         \sum_{i,e}w_{hie}x_{ie}\le C_h
                         \quad(1\le h\le s),
                   \qquad w_{hie}\ge0,\quad C_h\ge0,
 \tag{F2}
\]

for given rational per-commodity arc costs or resource charges.
Common arc costs are a special case. Unused network capacity is
allowed. These budgets are on actual fractional routing, and are
distinct from any cost constraint on the chosen commodity set.
The complete encoding of all s rows is included in H; s=0 is allowed.

Let B be a nonempty family of r-element subsets of P, with r>=1.
Its restriction selector, on Q subseteq P, returns a member of B
contained in Q or correctly reports that none exists. Every call
has paid polynomial time and encoding bounds. Define

\[
 \mathrm{OPT}=\max_{I\in\mathcal B}\max\{\lambda\ge0:
       \lambda d_i\text{ can be routed simultaneously for all }i\in I
       \text{ subject to (F2) and the original capacities}\}.
 \tag{F3}
\]

This comparator chooses one actual permitted set I. It does not
fractionally average selection sets. The routing within I is
fractional, as required by the splittable-flow model.

Finite capacities and distinct terminals make OPT finite. The
network may be disconnected, have zero capacities, or have C_h=0;
zero routing is always feasible. The selector first checks that B
is nonempty. Rank-zero selection is returned separately as the
empty routing, without asserting a finite minimum over no selected
commodities. The theorem concerns r>=1.

For undirected edges, use two opposite directed flow variables per
commodity and constrain their combined total on that physical edge
by its one capacity. All arguments below continue with that shared
edge row; they do not give each direction a separate full capacity.

## 2. A fixed downward service region

For a vector z>=0, let z_i denote the normalized service rate of
commodity i. Define U to be the set of all such z for which there
are nonnegative flows satisfying

\[
 \begin{aligned}
 B_G x_i&=d_i z_i(\mathbf1_{s_i}-\mathbf1_{t_i})
                         &&(i\in P),\\
 \sum_i x_{ie}&\le u_e &&(e\in E),\\
 \sum_{i,e}w_{hie}x_{ie}&\le C_h &&(1\le h\le s).
 \end{aligned}
 \tag{F4}
\]

Here B_G has +1 at an arc's tail and -1 at its head. The budget rows
are omitted when s=0.

This region contains zero, is convex and is downward closed. To
reduce the service of one commodity, scale all of its flow by the
same factor in [0,1]. Its conservation equations remain valid and
nonnegative shared loads and every routing charge decrease. Applying
this operation independently to the commodities proves the downward
property.

The region is bounded: at each source,
d_i z_i<=sum_{e out of s_i}u_e. The arc flows are also bounded by
the physical capacities. Hence U is a compact rational polytope,
being the projection of a bounded explicit rational flow polytope.
All feasibility and witness-reconstruction problems in (F4) are
ordinary polynomial-size rational LPs.

The original q-commodity region U remains fixed during omission
branching. A query on a smaller ground Q means the vector b*1_Q
with zero service outside Q, using (F4) on the original network.
It does not rebuild the region or change any capacity or budget.

## 3. Nonnegative packing rows from arc potentials

Choose nonnegative lengths ell_e, nonnegative budget multipliers
kappa_h, and one real potential pi_i(v) per commodity and vertex.
Require

\[
        \pi_i(v)-\pi_i(w)\le\ell_e+\sum_h\kappa_h w_{hie}
                         \quad(e=(v,w),\ i\in P),
        \qquad
        \pi_i(s_i)-\pi_i(t_i)\ge0.
 \tag{F5}
\]

Set

\[
       a_i=d_i(\pi_i(s_i)-\pi_i(t_i))\ge0,
        \qquad H_0=\sum_e u_e\ell_e+\sum_h C_h\kappa_h\ge0.
 \tag{F6}
\]

Every z in U satisfies the nonnegative packing inequality

\[
                              \sum_i a_i z_i\le H_0.
 \tag{F7}
\]

Indeed, conservation and telescoping give

\[
 \begin{aligned}
 \sum_i a_i z_i
   &=\sum_{i,e=(v,w)}x_{ie}(\pi_i(v)-\pi_i(w))\\
   &\le\sum_{i,e}x_{ie}(\ell_e+\sum_h\kappa_h w_{hie})\\
   &\le\sum_e u_e\ell_e+\sum_h C_h\kappa_h.
 \end{aligned}
 \tag{F8}
\]

This proof permits arbitrary nonnegative per-commodity routing
charges and does not require integer demands, equal demands or a no-bottleneck
assumption. For an undirected edge, the same ell_e appears in both
directional potential inequalities and in the one shared capacity
term.

These are metric-type inequalities: suitable potentials encode
shortest-path lower bounds under lengths ell_e+sum_h kappa_h*w_hie.
Using potentials directly also handles unreachable terminals without an
infinite-distance convention.

## 4. Exact separation with a finite bounded LP

Fix a queried z>=0. Rational Farkas duality applied to (F4) says
that infeasibility is equivalent to the existence of ell>=0,
kappa_h>=0 and real pi_i satisfying the arc inequalities in (F5)
and

\[
 \sum_i d_i z_i(\pi_i(s_i)-\pi_i(t_i))
                     -\sum_e u_e\ell_e-\sum_h C_h\kappa_h>0.
 \tag{F9}
\]

Initially Farkas imposes no sign on a commodity's terminal gap.
If a gap is negative, replace that commodity's entire potential by
zero. The arc inequalities remain valid because
ell_e+sum_h kappa_h*w_hie>=0. Its objective contribution changes
from a nonpositive number to zero because z_i>=0, so strict separation
is preserved. Thus (F9) has a witness satisfying the terminal-gap
nonnegativity in (F5).

Split pi into nonnegative variables pi^+ and pi^- and impose

\[
     \sum_e\ell_e+\sum_h\kappa_h+
            \sum_{i,v}(\pi_i^+(v)+\pi_i^-(v))\le1.
 \tag{F10}
\]

Any nonzero certificate can be scaled into this normalization
without changing the strict sign in (F9). Conversely every feasible
normalized point produces a valid row (F7). Consequently the LP
that maximizes the left side of (F9), subject to (F5), (F10) and
nonnegativity of the split variables, has a positive optimum exactly
when z is outside U. Zero is always feasible, and the LP is bounded.

This is an explicit LP with O(q|V|+|E|+s) variables and O(q|E|+q)
constraints, plus the nonnegativity and normalization rows. All
coefficients have polynomial binary length in the network data and
z. An exact rational optimizer supplies a polynomial-bit extremal
certificate, by the usual determinant bound for a bounded rational
LP. The resulting a and H_0 therefore have polynomial encoding. If
the optimum is zero, Farkas proves membership in U; an actual flow
is obtained by solving the primal system (F4).

No exponentially described set of routing paths and no projected
facet enumeration occurs. In particular, the separator's returned
row has nonnegative coefficients for the reason just proved, not
merely because the projection happened to be convex. All returned
rows belong to the same globally valid family (F5)--(F7).

Without routing budgets, omit all kappa variables and associated
terms. Zero budgets need no exceptional division or preprocessing;
the same primal and dual systems are exact. The number of budget
rows affects only the polynomial input size, not the corank exponent.

## 5. The fixed-target corank gap

The weighted prefix-free theorem applies directly to the fixed
packing representation of U. At a target T>0 and loss parameter
beta in (0,1), set

\[
                 t=T,\qquad b=(1-\beta)T,
                  \qquad R=\frac{t}{t-b}=1/\beta.
 \tag{F11}
\]

It deterministically returns one of the following:

* a permitted set I in B for which b*1_I belongs to U;
* a correct statement that no permitted set has T*1_I in U.

Its running time is Gamma(1/beta)^c poly(H), with polynomial
workspace, including all failed branches on unpromised inputs.
The polynomial-bit separator in Section 4 pays the required oracle
cost. The exact selector keeps I a genuine permitted r-set.

For clarity, a violated packing row at a current ground Q has
nonnegative coefficients a_i. Any promised set I* contained in Q
must omit more than a 1/R fraction of the row's total weight on Q.
Ordering the weights forces a prefix whose omitted-element density
first exceeds 1/R. Those first-crossing binary words are prefix
free. Their Gamma-weighted branch sum is at most one, and the
complete deterministic enumerator has polynomial space. This is
the reviewed mechanism from `corank_weighted_prefix_free_batching.md`;
no graph-specific exchange property is assumed here.

A successful membership test may have been on b*1_Q for a larger
current ground Q. Its selector's I is a subset of Q. Dropping all
other commodity flows preserves the selected rates and cannot
increase capacity loads or any routing charge. Alternatively solve
(F4) directly at b*1_I. Either construction gives an explicit legal routing.

This fixed-target statement already gives a useful admission gap:
if some permitted q-c commodities can each receive their full
specified demand, the algorithm routes exactly q-c permitted
commodities at least a (1-beta) fraction of each demand, without
capacity or budget violation, in Gamma(1/beta)^c poly(H) time.

## 6. Detecting zero optimum and constructing a positive scale

For each commodity i, compute the maximum singleton normalized
rate

\[
                   \rho_i=\max\{z_i:z_i\mathbf1_i\in U\}
 \tag{F12}
\]

and retain a corresponding routing. This is a bounded single-
commodity rational flow LP with the same routing budgets. The
value and a rational witness have polynomial encoding. Let
P_+={i:rho_i>0}.

If no permitted set is contained in P_+, OPT=0: every permitted
set contains a commodity of individually impossible positive
service. Output any permitted set with zero routing.

Otherwise the selector supplies I_0 subseteq P_+. Average the r
singleton routings for i in I_0, each with coefficient 1/r. Shared
loads and every budgeted charge remain at most their original bounds,
and commodity i receives normalized rate rho_i/r. Reduce individual
commodity flows as necessary to obtain the common rate

\[
                      \lambda_0=\frac{\min_{i\in I_0}\rho_i}{r}>0.
 \tag{F13}
\]

Thus lambda_0 is a constructed feasible lower bound on OPT. Its
bit length is polynomial, including when costs are large, the
budgets are tiny, or the nonzero capacities are very small. The
construction works with zero budgets as well: a positive singleton
LP witness already has zero charge in each zero-budget row.

Commodities outside P_+ can now be removed from the selection ground
because no positive-rate solution uses them. The remaining deficit
|P_+|-r is at most the original c, so this only improves the bound.
The flow region and its row interpretation still use zero insertion
into the original commodity coordinates.

Finally let rho_max=max_i rho_i. Every common rate on a nonempty
selected set is at most rho_max. The value
rho_max+lambda_0 is therefore a strictly infeasible external upper
target, independent of the behavior of any gap algorithm there.

## 7. Rational comparator recovery gives the sharper exponent

For a fixed permitted set I, let lambda_I be its exact maximum
concurrent rate, under all the original capacities and routing
budgets. It is computed by a polynomial-size rational arc-flow LP
with lambda as one variable. Impose lambda>=0 and the redundant
bound lambda<=rho_max, and set outside-I flows to zero. The LP is
bounded and nonempty. Its row data are original input rationals
and the already computed polynomial-bit bound rho_max.

Let n_0 be a uniform bound on its number of variables, and L_0 a
known uniform bound on the binary lengths of its rational row
coefficients and right sides. Both are polynomially bounded from
the explicit network input. Rowwise denominator clearing followed
by Cramer's rule gives the computable integer bound

\[
            D=n_0!\left(2^{(n_0+2)L_0}\right)^{n_0}
 \tag{F14}
\]

on the reduced denominator of every lambda_I. Padding smaller
formulations by zero-fixed variables makes the common dimension
literal. The bound is valid for lower-dimensional feasible LPs
as well. Its binary length is polynomial. Because the permitted
family is finite, OPT is one of these lambda_I values and has the
same denominator bound.

Write alpha=1-epsilon=A/B in lowest terms and use the grid

\[
                  \delta=\frac1{2BD^2}.
 \tag{F15}
\]

Start at lower target zero with any permitted set saved and at a
grid endpoint strictly above rho_max. Run the gap routine with
its full requested loss beta=epsilon: a success at T certifies
lambda_I>=alpha*T and moves the lower target to T; a failure
certifies T>OPT and moves the upper target to T. At adjacent grid
endpoints the lower target satisfies L>OPT-delta.

Now optimize the original fixed-I flow LP of the saved set exactly.
Its true optimum is at least alpha*L. If it were smaller than
alpha*OPT, the two denominator bounds would force

\[
                \alpha\mathrm{OPT}-\lambda_I
                    \ge\frac1{BD^2}=2\delta,
 \tag{F16}
\]

whereas lambda_I>=alpha*L>alpha*OPT-alpha*delta gives a smaller
gap than delta. This contradiction proves lambda_I>=alpha*OPT.
The exact optimizer returns routing attaining that value.

This is the rational-comparator lemma in
`rational_comparator_gap_optimization.md`, specialized to the
explicit flow LP. Reoptimization is essential: it is the optimum
lambda_I of the original fixed-set problem, not an arbitrary
target witness, whose denominator is bounded by D. The permitted
family and all routing budgets are fixed during the search.

The search takes a polynomial number of calls because the grid
denominator has polynomial binary length; it does not enumerate
D or all grid values. Every call has R=1/epsilon, giving exactly
the headline Gamma(1/epsilon)^c poly(H) bound. The positive scale
of Section 6 is useful but no longer necessary for this search.
Singleton LPs still give the convenient finite rho_max bound and
the optional safe reduction of the selection ground to P_+.

### 7.1. The earlier relative-search proof remains an alternative

One can avoid the denominator bound by using beta=epsilon/2 and
the positive lower scale lambda_0 from Section 6. Initialize
L=lambda_0 with its feasible routing and U=rho_max+lambda_0. At a
midpoint, success saves a routing of rate (1-beta)T and raises L;
failure gives T>OPT and lowers U. The invariants are U>OPT and
a saved permitted routing of rate at least (1-beta)L. They require
no success monotonicity and allow L>OPT.

Stop at U-L<=beta*lambda_0. Then
L>OPT-beta*lambda_0>=(1-beta)OPT, so the saved rate is at least
(1-beta)^2 OPT>=(1-epsilon)OPT. There are
O(log(1+rho_max/(epsilon*lambda_0))) midpoint steps and all targets
have polynomial encoding. This earlier route gives the weaker
Gamma(2/epsilon)^c poly(H) bound and is retained for completeness;
the main theorem uses the rational recovery above.

Both searches have polynomial workspace. The omission stack has
depth at most c<=q, its local enumerators have polynomial storage,
and the exact LP routines use polynomial workspace. An explicit
rational routing has at most q|E| arc-flow coordinates. If paths
are desired, ordinary flow decomposition provides a polynomial-size
path representation after discarding cycles, which cannot raise
any routing charge because every charge is nonnegative.

## 8. Exact selection constraints and the quantitative improvement

For unrestricted selection of r=q-c commodities, the selector only
tests |Q|>=r and chooses any r elements. For a rank-r matroid, it
finds a basis inside Q. For two rank-r matroids, matroid intersection
finds a common basis inside Q or proves there is none.

One linear bound on selection costs can be included by minimizing
that cost over common bases and comparing the minimum with the
bound. Rational costs may have either sign because all selected
sets have cardinality r; a common shift reduces them to nonnegative
costs if an implementation requires it. This exact selection bound
is independent of, and can coexist with, all the exact routing
budgets in (F2). No assertion is made that several arbitrary extra
selection budgets retain a polynomial restriction selector.

For the same selected-set problem, a direct exact baseline is to
enumerate the binom(q,c) omitted sets, retain those whose complements
are permitted, and solve the resulting fixed-set flow LPs exactly.
This takes q^{O(c)} poly(H) time and polynomial space. Membership
of an r-set is itself testable with the restriction selector: its
only possible contained r-set is itself. Thus the XP baseline is
valid even for the generic selector model.

The new guarantee replaces that growing polynomial degree by
(O(1/epsilon))^c and a fixed polynomial in the entire network size,
while losing only epsilon of optimal common service. In particular
there is no exponent depending on the number of arcs, the number
of vertices, row overlap, demand ratios, or capacity ratios. This
is a parameter tradeoff for almost-all commodity selection, not an
improvement to the time for the already polynomial fixed-commodity
flow LP. When c=0 the unique selected set can be optimized exactly
by that LP.

The theorem retains arbitrary directed routing and arbitrary
nonnegative rational data. It does not impose graph planarity,
bounded treewidth, a single source, equal demands, or a small number
of network constraints. It does require splittable flows; none of
the argument supplies integral, unsplittable or bounded-path-count
routes.

## 9. Bounded primary-source comparison

The following checks were made on 25 October 2026. They establish
relevant public baselines and the comparator distinctions; they do
not establish that this is the first corank-parameter formulation.

**Fixed commodities.** Mądry's primary manuscript,
[Faster Approximation Schemes for Fractional Multicommodity Flow
Problems via Dynamic Graph Algorithms](https://madry.mit.edu/docs/multiflow.pdf),
explicitly defines both maximum concurrent flow and its nonnegative
routing-cost-budget version. Its introduction states that these
fixed-commodity problems have exact polynomial LP formulations and
studies faster approximation schemes. The selection problem here
adds a discrete choice of one permitted q-c commodity set; its
contribution is not a new continuous-flow solver.

**All-or-nothing admission.** Chekuri, Khanna and Shepherd,
[The All-or-Nothing Multicommodity Flow Problem](https://chekuri.cs.illinois.edu/papers/anflow-sicomp.pdf),
SIAM Journal on Computing 42(4), 2013, maximize the number or weight
of fully served requests. Theorem 1.1 gives an
O(log^3 n log log n) approximation against the natural LP for the
undirected unit-demand problem; Theorem 1.2 extends under the
no-bottleneck condition. The paper also explicitly notes that
feasibility for a fixed chosen subset is polynomial by LP. Its
throughput objective and unrestricted rejection count differ from
the exact-cardinality/common-rate objective (F3).

**Arbitrary directed demands with congestion.** Chaturvedi, Chekuri,
Liu, Richa, Rost, Schmid and Weber,
[Improved Throughput for All-or-Nothing Multicommodity Flows with
Arbitrary Demands](https://arxiv.org/html/2005.04533v7), version 7
of 26 July 2022, allow arbitrary directed networks and demands.
Theorem 2.6 gives near-optimal admitted throughput with a
logarithmic-over-log-log type congestion factor; Theorem 6.2 gives
a deterministic specialization with throughput factor 1-1/m and
congestion 3(1.85)ln(m)/ln ln(m), for m>=9. Our exact capacities and
exact selected family accompany a different guarantee: nearly
optimal common service when the number rejected is a parameter.
Neither result uniformly dominates the other.

The bounded search included concurrent flow with outliers, rejected
demands, commodity selection, matroid constraints, admission control,
and corank. It did not identify a checked primary theorem giving
the exact statement (F1) in this combined selector/budget scope.
That is a search outcome, not a proof of priority or completeness.
In particular, similarly named parameterized “All-or-Nothing Flow”
problems can mean an edge-flow zero-or-capacity constraint, and
integer multicommodity-flow hardness concerns a different routing
model; those results are not used as hardness claims here.

An index-level check of the official
[OpenAI mathematics manuscript map](https://raw.githubusercontent.com/openai/math/main/CONTENTS.md)
found the nearby multicommodity entry 089 concerning bounded
flow--cut gaps from graph-metric embeddings. That scope does not
provide the selected-demand concurrent-flow theorem above. No
claim about uninspected full manuscripts, and no dependency on
that index's mathematical claims, is intended.

## 10. What is proved and what is not imported

The new application has a complete chain: the explicit flow LP
defines one bounded downward service region; finite normalized
Farkas certificates give nonnegative polynomial-bit packing rows;
weighted first-crossing omissions solve its fixed-target selection
gap; the exact fixed-set LP gives a uniform rational denominator
bound; and reoptimization after a one-sided grid search yields the
relative guarantee. Singleton routing LPs also provide a positive
lower scale for the alternative search. All routing and selection
constraints stated in the theorem are
verified by its final constructive output.

The theorem uses no factor-four allocation core, no approximate
configuration-LP solver, no item-size rounding, and no assumption
that every downward family is a matroid. Its substantive internal
dependencies are the independently reviewed generic weighted
prefix-free omission theorem and rational comparator recovery.
The remaining external ingredients
are ordinary exact rational linear programming, Farkas duality,
and the paid exact restriction selector.


---

**Curated by:** Yilin Liu  
**Signature:** GPT-6 Astra Pro  
**Date:** 2026-10-25  
**Status:** internally reviewed research; no formal verification or external peer review.
