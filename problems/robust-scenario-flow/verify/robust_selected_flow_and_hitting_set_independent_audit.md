# Verification note

**Curated source path:** `sources/checkpoint-p/robust_selected_flow_and_hitting_set_independent_audit.md`

The source audit follows.

# Independent audit: robust selected flow and two exact-admission reductions

**25 October 2026. Fresh full reads of**

- `robust_scenario_selected_flow_corank.md`, Sections 1--6;
- `exact_multi_budget_flow_hitting_set_reduction.md`, Sections 1--4.

I also read the full rational-comparator optimization lemma and the
single-scenario flow model, service separator, and gap construction
on which the robust result depends. Both requested manuscripts pass
independent mathematical review. Their positive and negative scopes
are kept distinct.

## 1. The robust service region is exactly the stated intersection

The selected commodity set is shared, while each explicitly listed
scenario may choose its own routing after that scenario is known.
With no omitted cross-scenario coupling, a nonnegative service
vector is feasible precisely when it belongs to every scenario's
service projection. Their intersection is bounded, convex and
downward, and contains zero.

Checking scenarios in deterministic order either produces all
routing witnesses or finds a failed scenario. Its nonnegative
packing certificate is valid for the intersection. This gives a
polynomial separator in the total explicit scenario description.
The q-coordinate commodity ground is unchanged throughout omission,
so the exponent remains the one selection corank q-r rather than
a scenario-multiplied quantity.

## 2. Nonnegative flow rows and exact budgets

The single-scenario separator has the required sign for a concrete
reason. Nonnegative capacity and routing-budget multipliers yield
nonnegative arc lengths. A Farkas potential with a negative terminal
gap can be replaced for that commodity by zero: the arc inequalities
remain valid and its contribution to a nonnegative service query
does not decrease. Normalizing the split potential and multiplier
variables gives a bounded explicit certificate LP with polynomial
bit length.

Every listed routing budget remains a linear constraint in a
continuous flow LP. There is no integral rounding step that could
violate it. Arbitrarily many explicit nonnegative routing rows
therefore affect polynomial input size, not the corank exponent.
This does not create a restriction selector for an arbitrary
collection of *selection* budgets, which the manuscript correctly
separates from routing budgets.

## 3. Rational recovery removes only search error

For a fixed permitted commodity set, all scenario flow variables
and a single shared normalized rate form one bounded rational LP.
The rate bound from any one scenario is valid: at each distinct
source, net outgoing flow is at most total incident/outgoing
capacity, and a nonempty selected set has rate no greater than
the largest of the individual upper bounds. Shared undirected
edge capacities are counted once per physical edge as stipulated.

The uniform coefficient bound and polynomial dimension give the
same Cramer denominator bound D for every fixed-set optimum,
including lower-dimensional feasible polytopes. The optimum over
the finite selected family equals one of these rational optima.

For alpha=A/B=1-epsilon, grid delta=1/(2BD^2), and an external
upper endpoint, one-sided search gives L>OPT-delta and a saved
set whose exact optimum is at least alpha*L. Reoptimizing that
set with the original target-independent LP is essential. If
its actual optimum were below alpha*OPT, the positive rational
gap would be at least 1/(BD^2)=2delta, contradicting the search
inequality. Thus the stated Gamma(1/epsilon)^c base is justified
without an extra relative-search loss or an epsilon-zero claim.

## 4. The scenario Hitting Set construction has the required routes

For every nonempty set S, the scenario enables the private arc
s_i to t_i for i outside S and the three-arc route through x,y
for i in S. A selected member of S has no other path to its own
sink. Entering a different commodity's sink cannot help because
that sink has no outgoing arc and has zero prescribed imbalance
for the commodity in question. Thus every such selected unit
uses the central arc of capacity |S|-1.

Consequently full unit service on a selected set I is possible
in that scenario exactly when |I intersection S|<=|S|-1. The
private paths and central paths construct a valid simultaneous
routing whenever that inequality holds. The set of rejected
commodities, of fixed size k, must therefore hit every source
set S. A source hitting set of size at most k can be padded to
size exactly k under the stated k<q preprocessing.

The reduction preserves c=k and has polynomial explicit size.
Its common directed topology is acyclic. After zero-capacity
arcs are removed, each scenario has a central double-star
component and isolated private edges, or two separate stars
when the central capacity is zero. The underlying positive-
capacity graph is indeed a forest.

## 5. The one-scenario many-budget reduction is separately correct

The companion network has just the distinct private unit arcs.
Conservation forces a selected commodity's unit demand to use
its own arc. The explicit nonnegative routing row for a source
set S is exactly its selected count on S, bounded by |S|-1.
It is therefore equivalent to requiring the rejected k-set to
intersect S. Necessity and sufficiency follow without any
integral-routing assumption: fractional flows cannot change the
forced unit on a commodity's only arc.

This gives a polynomial parameter-preserving reduction with one
scenario and many budget rows. It does not prove the analogous
statement with one budget or without budgets. The scenario
reduction achieves no-budget hardness by using a different
explicit scenario for every source row. Neither is substituted
for the other.

## 6. The primary hardness baseline was checked directly

I freshly opened the publisher's primary article page for Bart
Jansen, [*On Structural Parameterizations of Hitting Set: Hitting
Paths in Graphs Using 2-SAT*](https://jgaa.info/index.php/jgaa/article/view/paper413),
JGAA 21(2), 219--243 (2017), DOI 10.7155/jgaa.00413. Its abstract
explicitly records W[2]-completeness of Hitting Set parameterized
by the solution cardinality. This supports the source-problem
baseline used by both reductions. The reductions themselves are
proved directly in the manuscripts rather than attributed to
that paper as prior constructions.

## 7. The limitations are stated at the correct precision

A YES hitting instance has concurrent optimum one. A NO instance
forces at least one fully selected set S and a rate at most
(|S|-1)/|S|. That loss can vanish as the input grows. Thus the
reductions obstruct exact F(c)*poly(H) admission under FPT!=W[2],
but not the fixed-positive-epsilon approximation scheme and not
an arbitrary constant factor. Their simple routing structures
do not turn this into a fixed approximation gap.

The robust algorithm assumes a total explicit scenario encoding;
an implicit exponentially large uncertainty family would need a
new separation and bit-complexity argument. Its routings are
adaptive, not oblivious. The statements do not infer hardness
for only individual-edge-failure scenarios, or for single-scenario
unbudgeted admission, without another reduction.

No substantive gap was found in the requested manuscripts. This
is internal independent mathematical review, without a claim of
formal verification, external peer review, or exhaustive novelty.


---

**Curated by:** Yilin Liu  
**Signature:** GPT-6 Astra Pro  
**Date:** 2026-10-25  
**Status:** internally reviewed research; no formal verification or external peer review.
