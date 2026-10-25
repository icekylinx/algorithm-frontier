# Independent audit of the robust integer-unit corank obstruction

**25 October 2026. Full independent read of H1--H5 and every section
of `robust_unit_allocation_corank_obstruction.md`.**

The reduction and its finite-factor consequence pass. The constructed
scenario ranks are explicit matroids, the corank is exactly the Hitting
Set budget on nontrivial instances, and the robust integer optimum is
exactly zero or one. The fractional triangle example is also correct.

## 1. Preprocessing and parameter preservation

An empty source set makes Hitting Set negative; an empty source family
is positive. With a nonempty family of nonempty sets, k=0 is immediately
negative. If k exceeds the source universe size, all original elements
hit every nonempty set, so the instance is positive. These cases can
be decided directly or mapped to fixed positive/negative robust
instances with bounded corank.

For the remaining 1<=k<=|U| cases, add one fresh element outside every
source set. Then q=|U|+1>k and the uniform player rank r=q-k is positive.
The selection corank is exactly q-r=k. The added element cannot create
a hitting set that did not exist: remove it from any hitting set on
the enlarged ground to obtain an original hitting set of no larger
size. Conversely every original hitting set remains valid.

A solution of size at most k can be padded to exactly k because the
enlarged ground has more than k elements, and adding elements cannot
destroy an existing intersection. This justifies using complements
of bases of one exact cardinality. The case k=|U| is valid too; the
fresh element keeps the selected rank at one rather than zero.

## 2. Every scenario rank is a valid explicitly represented matroid

For a nonempty source set S, the function

\[
 f_S(A)=|A\setminus S|+
                \min\{|A\cap S|,|S|-1\}
\]

is the direct sum of a free matroid on P\S and a uniform matroid of
rank |S|-1 on S. It is therefore normalized, monotone, integral, and
submodular. Its full rank is q-1 and every singleton rank is at most
one. When S is a singleton, its one element is a loop; no rank formula
or feasibility argument assumes otherwise.

Membership can be expressed as coordinate caps one together with the
one nontrivial cap on the S part. The representation stores just S
and its size; queries require only intersections and cardinalities.
All ranks have O(log q) bits and the total explicit scenario description
is polynomial in the source instance. The single unit-valued resource
per scenario is an allowed recipient matroid, not an expanded collection
of hidden resource units. Costs and budgets are identically zero.

## 3. Positive integer service is equivalent to hitting every source set

For an actual selected basis I, its complement D has exactly k elements.
With one unit-valued resource and singleton caps at most one, positive
integer utility at each selected player forces count one there. If a
legal allocation has other counts as well, downward feasibility lets
them be discarded. Thus positive service on I is possible exactly when
the indicator 1_I is independent in the scenario matroid.

The free part imposes no further restriction on I. Independence in the
uniform S part is precisely |I intersect S|<=|S|-1, equivalent to
D intersect S being nonempty. The same selected set can have positive
service in every scenario if and only if its complement hits all the
source sets.

On a positive source instance, allocate exactly 1_I in every scenario
to obtain robust utility one. Singleton caps prohibit robust utility
above one. On a negative source instance, every basis has a scenario
where at least one selected player must get zero, so every legal integer
output has robust value zero. The zero allocation is always feasible.
This proves the exact zero/one optimum statement H5, without treating
a zero optimum as an infeasible optimization instance.

Adaptive scenario allocations cannot avoid this argument. The target
of positive integer utility forces the same necessary indicator vector
on the common first-stage selected basis in every scenario.

## 4. Any finite multiplicative factor yields an exact decision

For an optimum-one instance, a finite positive approximation factor
requires strictly positive returned robust utility. Since utility is
integer and at most one here, that output must have value one. For an
optimum-zero instance, no legal output can be positive. The output's
selected set and the explicit scenarios can be checked in polynomial
time, so such an approximation decides the source problem.

The approximation factor need not be a fixed constant to obtain this
consequence. Any finite claimed factor on these instances still forces
strict positivity. What matters for the parameterized conclusion is
the stipulated uniform running-time form F(c)*poly(H), with a polynomial
degree independent of c. Since c=k, a deterministic algorithm of that
form would give an FPT algorithm for Hitting Set.

I freshly checked the primary source records for Bart Jansen's
[*On Structural Parameterizations of Hitting Set: Hitting Paths in
Graphs Using 2-SAT*](https://arxiv.org/abs/1507.05890) and Inamdar et al.'s
[*Fixed-Parameter Algorithms for Fair Hitting Set Problems*](https://drops.dagstuhl.de/storage/00lipics/lipics-vol272-mfcs2023/LIPIcs.MFCS.2023.55/LIPIcs.MFCS.2023.55.pdf).
The former's abstract and the latter's Section 1.1 explicitly record
W[2]-completeness of Hitting Set parameterized by solution cardinality.
They support the stated conditional consequence under FPT!=W[2].

## 5. The fractional half-service example checks at every subset constraint

For any scenario with |S|>=2 and any selected set I, the vector
(1/2)*1_I respects every coordinate cap. Its total on S is at most
|S|/2<=|S|-1. These constraints characterize the direct-sum scenario
matroid polytope, so the vector satisfies all its subset inequalities,
not merely one necessary inequality on S itself.

For source sets {1,2}, {2,3}, and {1,3}, no single element hits all
three; the fresh fourth element hits none. With k=1 the selected rank
is three, so the integer robust optimum is zero. Nevertheless half
service on every selected three-set is feasible in every scenario.
In fact each such three-set contains at least one of the three source
pairs, whose cap one bounds its common fractional rate by one half.
The fractional optimum in this particular example is therefore exactly
one half.

This is a rounding obstruction at the unit positivity boundary. It does
not invalidate fractional scenario-by-scenario separation. An additive
largest-unit guarantee may return zero on the example, whereas every
finite multiplicative integer guarantee would have to distinguish the
Hitting Set answer.

## 6. Accepted scope and conclusion

All H1--H5 claims pass. The reduction uses an input-sized number of
explicit scenarios and one common selected basis, while allowing
adaptive allocations after the scenario is known. It does not establish
the same hardness for a fixed number of scenarios, nor a whole-q
exponential-base lower bound or an unconditional rank-query obstruction.

The model is simpler than the general positive allocation setting in
costs, values, and resource representation. Its obstruction comes from
requiring one selected basis to pass every integer one-unit gate. The
continuous robust flow results do not perform that integer recovery
and remain consistent with this reduction.
