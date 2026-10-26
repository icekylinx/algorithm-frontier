# Exact selected flow with many routing budgets: a Hitting Set reduction

**25 October 2026. Companion limitation for the selected-flow scheme;
independent review requested.**

The selected splittable-flow approximation theorem allows any explicit
polynomial-size collection of nonnegative routing budgets. In that
scope, demanding exact full service is already W[2]-hard in the number
of rejected commodities. The reduction below is elementary and uses
disjoint unit-capacity arcs. It is a precise boundary, not a claim of
a new complexity classification in the literature.

This statement concerns many routing budgets. It does not establish
the same hardness with one budget or with no routing budgets, and it
does not give a lower bound for any fixed positive approximation loss.

## 1. Source problem and harmless preprocessing

Hitting Set has a universe U of q elements, a family S of subsets of
U, and an integer k. It asks for a set D of at most k elements meeting
every member of S. Parameterization by k is W[2]-complete; a primary
source recording this baseline is Bart M. P. Jansen, *On Structural
Parameterizations of Hitting Set: Hitting Paths in Graphs Using 2-SAT*,
Journal of Graph Algorithms and Applications 21(2), 219--243 (2017),
[publisher article](https://jgaa.info/index.php/jgaa/article/view/paper413),
[DOI](https://doi.org/10.7155/jgaa.00413).

The reduction may assume all input sets are nonempty and 0<=k<q.
An empty set makes the instance immediately negative; k>=q with no
empty set makes it immediately positive. Such cases can be decided
directly or mapped to fixed yes/no instances with a bounded parameter.
The empty family is likewise immediate. The hard instances remain
under these standard exclusions.

A hitting set of size less than k can be padded to size exactly k
when k<q: adding elements does not destroy an intersection. Thus
using exactly k rejected commodities does not change the source
decision problem.

## 2. Network and budgets

For each element i in U create distinct vertices s_i and t_i and
one private directed arc e_i=(s_i,t_i) of capacity one. There are no
other arcs. Commodity i has terminals s_i,t_i and demand scale one.
All selected commodities will be required to receive normalized
service rate one.

The selection family is the uniform matroid basis family of size
r=q-k. Its restriction selector is elementary. For every nonempty
input set S, impose the routing budget

$$
\sum_{i\in S} x_{i,e_i}\le |S|-1.
\tag{H1}
$$

This is a nonnegative routing-budget row in the flow model: its
coefficient is one on each listed private commodity arc and zero
on every other commodity-arc coordinate. Its capacity is a
nonnegative integer. The number of budgets is the number of input
sets, and their explicit total encoding is polynomial in the
Hitting Set instance length. The network is a disjoint union of
one-arc DAGs, with no need for splitting or alternative routes.

## 3. Exact equivalence and parameter preservation

For any chosen set I of q-k commodities, a unit-rate routing must
put exactly one unit on e_i for i in I. All other commodities can
be assigned zero flow. Consequently H1 is equivalent to

$$
|I\cap S|\le |S|-1
       \quad\Longleftrightarrow\quad
                      (U\setminus I)\cap S\ne\varnothing.
\tag{H2}
$$

The chosen I satisfies every budget at full rate if and only if
its complement D is a hitting set of cardinality k. Conversely,
given such a D, routing one unit on each selected private arc
satisfies every capacity and every H1 row. Thus the source instance
is positive exactly when the selected-flow instance has optimum
common rate one. Its optimum cannot exceed one because each
selected private arc has unit capacity and r>=1.

The flow selection corank is

$$
c=q-r=k.
\tag{H3}
$$

This is a polynomial parameter-preserving reduction. Therefore an
exact full-rate admission algorithm with time F(c)poly(H) for this
many-routing-budget model would yield an FPT algorithm for Hitting
Set. Under FPT!=W[2], such an exact algorithm does not exist.

The output network and all budgets are explicit; this is a
parameterized complexity reduction, unlike the value-oracle
indistinguishability lower bound for optional active machines.

## 4. Why the approximation scheme is consistent with the reduction

If a rejected set misses S, all |S| commodities from that set are
selected. They can receive a common normalized rate at most

$$
1-\frac1{|S|}
\tag{H4}
$$

under its budget. This rate can approach one as |S| grows. A fixed
loss epsilon therefore need not distinguish yes and no instances.
An accuracy smaller than the reciprocal of the largest input set
size would depend on the original input magnitude, and the
approximation theorem's factor Gamma(1/epsilon)^c would then not
be an FPT(c) exact algorithm.

The rational comparator recovery lemma uses a positive epsilon;
it removes only an additional search error. It does not turn the
gap routine into an epsilon-zero optimizer. There is consequently
no contradiction with this reduction.

No optimal exponential-base conclusion follows. The theorem does
not claim that every constant-factor improvement is hard, that
one-scenario unbudgeted routing has this reduction, or that the
same obstruction applies to the single-budget assignment-rounding
models in the allocation manuscripts.

An independently developed companion in the robust-scenario note
encodes one Hitting Set row per explicit network scenario and uses
no routing budgets. That is a different extended model and keeps
its own scenario parameter and recourse assumptions explicit.
