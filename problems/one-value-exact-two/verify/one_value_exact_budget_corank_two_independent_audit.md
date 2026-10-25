# Verification note

**Curated source path:** `sources/checkpoint-o/one_value_exact_budget_corank_two_independent_audit.md`

The source audit follows.

# Independent audit: exact two for one-value budgeted allocation

**25 October 2026. Fresh full read of
`one_value_exact_budget_corank_two_allocation.md`, O1--O16.**

The theorem passes substantive mathematical review. Its important
distinction is that a fractional *integer count quota* on one genuine
selected basis can be recovered at no greater cost with no unit loss.
That recovery would not hold for arbitrary unrelated weighted utility
quotas, which explains why the one-value scope matters.

## 1. Budgeted count projection

The fractional resource and cost region is compact, nonempty and
rational. Its lower count projection is convex and downward.
The support oracle is an exact rational LP with original resource
separation and one explicit budget row. Its vertex coefficients
have a uniform polynomial-bit bound from the polynomial dimension,
binary rank values and rational cost row. Consequently the outer
normalized nonnegative support LP has a polynomial exact separator.

The membership branch must accept a **nonpositive** outer optimum,
not just a zero optimum. For example a one-dimensional count region
[0,10] at query zero has normalized support-gap optimum -10.
I reported this wording correction to the author, who applied it.
The actual
positive-part separation proof establishes the nonpositive branch:
any point outside a compact downward region has a strictly positive
normalized nonnegative separating gap.

## 2. The selected-set promise and weighted gap

An integer K-service basis supplies a fractional K-service witness
in that fixed region. For K>=2, the output quota ceil(K/2) is
strictly smaller, and K/(K-ceil(K/2))<=3. The original M restriction
selector therefore gives the claimed Gamma(3)^c bound through the
weighted prefix-free theorem. The resource/cost region stays fixed
on the original ground during omissions. A terminal witness basis
inside a larger feasible queried ground inherits service by
downward closure, after which its allocation is explicitly
reconstructed.

## 3. Exact quota recovery is valid

Discarding counts outside the chosen basis and trimming each
selected player's total to integer b reduces coordinates and cost.
The resulting fractional point lies in the intersection of the
direct-sum original resource polymatroid and the partition rank
allowing b units at each selected player. Its total br saturates
the latter rank. Thus the full-total face is nonempty and integral.

Minimizing the original linear assignment cost on this face has an
integer optimum of no greater cost than the supplied fractional
point. The total equation forces exactly b units at each player.
The author correctly optimizes cost on an integral face rather
than claiming that intersecting it with an arbitrary cost budget
preserves integrality. Counts stay binary encoded and the product
ground is polynomial.

## 4. The exact one-unit gate

The K=1 gate uses precisely two matroids: the direct sum of the
Boolean recipient matroids on type-player pairs and the parallel
lift of original M. A size-r common independent set chooses distinct
players forming an M-basis and one resource unit at each. Weighted
matroid intersection finds the true minimum assignment cost. Any
positive integer quota can be reduced to one unit per selected
player, so failure is sound. No unprovided three-matroid selector
is hidden in this step.

## 5. Optimization and the parameter boundary

The external integer upper bound floor(total resource rank/r)+1
is above K*. Every later failed target remains above K*, although
successful targets need only deliver their half quotas. At adjacent
endpoints the saved lower target is at least K*, proving output
ceil(K*/2). Only logarithmically many target calls in binary rank
size are needed; zero optimum and an empty resource set are handled.

The hidden f_A instance with zero costs is a valid included subclass.
For optimum count two, any factor strictly below two must supply
at least two integer units on its r selected players, uniquely
identifying A. The oracle transcript yields binom(q,c)-1 queries,
excluding every uniform F(c)*poly(H) bound below two by fixing c
larger than its polynomial degree. This does not claim hardness
for ordinary explicit eligibility or optimality of base 27/4.

With the nonpositive-branch wording correction, no gap remains in
O1--O16. This is independent internal mathematical review rather
than formal verification or external peer review.


---

**Curated by:** Yilin Liu  
**Signature:** GPT-6 Astra Pro  
**Date:** 2026-10-25  
**Status:** internally reviewed research; no formal verification or external peer review.
