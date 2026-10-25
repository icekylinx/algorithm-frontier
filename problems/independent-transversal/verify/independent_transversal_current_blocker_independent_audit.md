# Verification note

**Curated source path:** `sources/checkpoint-o/independent_transversal_current_blocker_independent_audit.md`

The source audit follows.

# Independent audit of the current-blocker transversal transfer

**25 October 2026. Mathematical and source-interface audit passed.**

Audited note: independent_transversal_current_blocker_growth.md.
The primary source was checked directly:
[Graf--Haxell, Finding Independent Transversals Efficiently, arXiv:1811.02687v2](https://arxiv.org/html/1811.02687v2),
Definitions 3 and 7--12, the three algorithms in Section 4,
Lemmas 13--20, and Theorem 4.

The source already provides the qualitative independent-transversal
or domination/constellation alternative. The audited contribution is
a sharper uniform parameter analysis with an additional certified
stopping test. This is separate from arbitrary general-graph matching.

## 1. The output contract is the source's stronger certificate

The candidate uses total domination: a vertex in the target classes
must have an adjacent vertex in D even if it itself lies in D.
The constellation is induced in the graph on its class set with
within-class edges deleted. Its nonempty stars have leaves forming
a partial independent transversal of all but one of those classes.
D can use vertices outside the target class set. These conventions
agree with the source's Theorem 4.

Deleting within-class edges preserves independent transversals and
the partition-relative claw promise. Choosing an isolated vertex and
removing its whole class can be repeated safely: previously chosen
vertices have no neighbours among the then-remaining classes.
Any later certificate uses unchanged remaining classes and remains
valid in the original graph; its constellation is interpreted with
the source's within-class-edge deletion convention.

## 2. Actual candidates are fresh after matching changes

SuperposedBuild visits surviving layers in increasing order. If
an attempt is adopted, it truncates the stack immediately above that
layer. Otherwise it proceeds to the next layer. Every matching
change is followed by this routine before a continuing main-loop
boundary. Thus every surviving layer has an actual candidate made
under the current matching, or the matching has not changed since
that candidate was made.

A surviving layer's lower prefix is unchanged: modifying or
collapsing a lower layer discards this layer. Birth of a later layer
does not alter its prefix. An adopted maximal candidate is itself
maximal as the new current layer. A rejected candidate has fewer
than mu times the current selected count in additional vertices.
Hence the freshness assertion does not rely on an unjustified
hypothetical greedy rerun.

The distinction from the simpler weak-Haxell lifetime-tree proof is
real. A successful extension here may discard higher layers without
each of them collapsing. The candidate correctly retains the source's
signature proof, which already handles that event.

## 3. Why the current constellation is induced

The source's layer definition and actual operations give the
needed invariant. It should not be justified merely by citing
vertex-disjoint layer supports: disjointness alone would not rule
out edges between stars.

When a new selected vertex is added, it has no neighbour in the
earlier selected or blocker sets. If one of its new matching
blockers were adjacent to an earlier selected vertex, that blocker
would already be in the earlier blocker set and would be forbidden
to the new selected vertex. Matching blockers are mutually
nonadjacent because the matching object is a partial independent
transversal. Within a layer, every blocker has exactly one selected
neighbour by the build rule.

These facts establish anticompleteness of different current layers
and independence of the union of their selected sets. An adopted
extension retains this invariant below the adopted layer and discards
everything above it. Removing matched blockers cannot add an edge.
Consequently deleting currently unblocked selected vertices from
the current prefix leaves exactly an induced disjoint union of
nontrivial stars. Their leaves are the current distinct matching
representatives, so the class-count requirement for K follows.

This actual-operation argument has been sent to the author of the
main note as an explicit clarification.

## 4. Total domination and the cardinality bounds

For a prefix through i, put

\[
 W=1+\sum_{j<i}|Y_j|,\qquad
 T=\sum_{j\le i}|Y_j|=W-1+|Y_i|.
\]

The active W classes are distinct: matching representatives occupy
distinct classes and the root is unmatched. Remove candidate-full
classes and classes containing any extra selected candidate vertex.
The latter removal is necessary because an extra selected vertex
with no blocker would not otherwise dominate itself.

Let D contain every actual candidate and one chosen neighbour for
each currently unblocked selected vertex. Such a neighbour exists
after isolated-class preprocessing. A target-class vertex is then
covered as follows. A current selected vertex has a blocker or its
newly added neighbour. A candidate blocker has a selected neighbour.
A candidate-extra selected vertex cannot be in a retained target
class. Every remaining vertex lies outside the relevant excluded
candidate/prefix sets and is in a non-full class; if it had no
neighbour there, greedy construction would not have terminated.
This proves total domination, including vertices that themselves
belong to D.

The claw promise bounds a candidate extra's matching neighbours by
r-1. Current noncollapsibility gives
sum |X_j| <= T/(1-mu). Thus, with

\[
 \eta=\frac{\mu(r+2)}{1-\mu},\qquad
 f=\frac{\mu+(1+\mu)/Q}{1-\mu},
\]

the derived bounds are

\[
 |D|\le(2+\eta)T,\qquad
 |D\setminus V(K)|\le\eta T,\qquad
 |S|\ge W-fT.
\]

The extra coefficient r+2 has three sources: candidate extras and
their blockers, currently unblocked selected vertices, and their
chosen neighbours. Current blocked selected vertices and matching
representatives form K. No entire-class cardinality enters these
estimates.

## 5. Constants and the new current-Y test

For mu=rho=epsilon/(100r) and Q=ceil(1/mu), Definition 10's
three feasibility inequalities hold with substantial slack.
Multiplying their common bracket by 1-mu leaves at least
1-3mu-mu^2; substitution verifies the two error bounds in the
main note uniformly for r>=2 and 0<epsilon<1.

The convenient estimates

\[
 \eta<\epsilon/40,\quad f<\epsilon/90,\quad
 \eta+(2+\epsilon)f<\epsilon/10
\]

are valid. If W>=2 and |Y_i|<=epsilon W/10, then
T<=(1+epsilon/5)(W-1). Substituting in the preceding three bounds
gives

\[
 |D|<(2+\epsilon)(|S|-1),\qquad
 |D\setminus V(K)|<\epsilon(|S|-1).
\]

In particular |S|-1 is at least
(1-epsilon/75)(W-1)>0, so the returned class set is nonempty.
The constant 13/25 in the intermediate size estimate follows from
(2+epsilon/10)(1+epsilon/5)<=2+13epsilon/25.

For W=1, the old birth check ensures a nonempty selected set;
noncollapsibility then forces at least one blocker. This proves the
current-Y growth directly and does not misuse the source's empty
dummy Y_0 as a matching representative.

Thus either the valid full certificate is output or all surviving
layers satisfy

\[
 |Y_i|>\frac{\epsilon}{10}
                  \left(1+\sum_{j<i}|Y_j|\right).
\]

## 6. Signature length and uniform count

The new check adds a certified stop and changes no continuing
operation. The original birth-selected growth still holds whenever
the algorithm continues, including when a newly born layer collapses
immediately. It remains available to the source's lexicographic
decrease argument and to its proof that absolute signature
coordinates are nondecreasing.

The new current-Y growth bounds the number of surviving layers by
L=O(epsilon^{-1} log(q+1)). The source's unchanged signature base
b=Q/(Q-mu rho) has log b=Theta(mu^3). Its last finite coordinate
is at most

\[
 H=O\bigl(\mu^{-3}
   [L\log(1/\rho)+L\mu+\log(q+1)]\bigr).
\]

There are at most 2L finite coordinates with a prescribed sign
pattern and nondecreasing absolute values. Counting bounded-length
nondecreasing integer lists gives exp(O(L log(2+H/L))) signatures.
Since log(2+H/L)=O(log(2+r/epsilon)), this is

\[
 (q+1)^{O(\epsilon^{-1}\log(2+r/\epsilon))}.
\]

It is valid to use this upper L even when it exceeds q. The count
then overestimates, rather than underestimates, the possible lists.
The signatures are an analysis device; the algorithm need not
evaluate these real logarithms or allocate arrays of numerical
size Q. Its operational comparisons are rational count comparisons
with the stated input bit complexity.

Retaining the source's safe polynomial per-iteration cost, the
additional certificate checks, and the at most q augmenting calls
gives the claimed conservative P^4 factor times that class exponent.

## 7. Verdict and limitations

No counterexample was found in the candidate freshness, current
blocker charge, total domination, induced constellation, or shortened
signature count. The result is a valid research strengthening of the
specified public certifying construction after the explicit induced-
star invariant is included.

This does not assert the fastest algorithm under specialized maximum-
degree or class-size promises, and does not establish polynomial
dependence on reciprocal slack. Its hypergraph consequence overlaps
the independently established rank-linear weak-Haxell analysis and
should not be counted as an unrelated second breakthrough.

## 8. The input-linear layer implementation also passes

The subsequent implementation refinement
independent_transversal_input_linear_iteration_implementation.md
has also been read and independently checked. In one BuildLayer
call the partial transversal, lower prefix and active classes are
fixed. Candidate membership, forbidden neighbour counts, and
selected class counts only increase. Each failed addability
predicate is therefore permanent for that call. A fixed-ID
single scan produces the same choices as repeatedly selecting the
least currently addable ID.

Each newly selected vertex is scanned once for its matching
neighbours. Each vertex activated into the forbidden union has
its adjacency list scanned once. Initializing the prefix and
candidate flags also takes O(P): the current layer supports
are disjoint, even though separately retained rejected candidates
need not be. Thus one BuildLayer call costs O(P), not a cost
proportional to the numerical cap Q.

SuperposedBuild makes at most q+1 such calls. Every collapse
iteration first removes its last layer, and SuperposedBuild only
truncates further. Therefore a single outer iteration makes at
most q+1 collapses, including a possible newly built blocker-free
last layer. The safe bound is O(P(q+1)^2). Both the new certificate
exit and the original small-birth certificate fit this bound;
retained candidate lists contribute at most O(P(q+1)) volume.

The extra q augmentations and fixed class powers are absorbed
in the already positive exponent. The sharper complete bound is
therefore

\[
 P(q+1)^{O(\epsilon^{-1}\log(2+r/\epsilon))}
       \operatorname{poly}(b_\epsilon+\log P).
\]

The same input-linear implementation applies to the derived-public
baseline with its older class exponent, so it is not an asymmetric
comparison advantage. Signature logarithms remain analysis-only.
Replacing r by min(r,q+1) is safe because a set of neighbours in
distinct classes has at most q vertices; this also gives the stated
parameter bit bound.

## 9. The elementary same-contract fallback passes as well

The separate note
independent_transversal_elementary_exponential_fallback.md
was checked against the source's Section 2 procedure. At a stable
state, every selected centre has a nonempty blocker set. Thus every
existing centre and leaf is already dominated within its star.
A newly chosen undominated active-class vertex is outside those
stars. Its matching blockers belong to new classes, because each
old active non-root class already has its representative among the
old leaves.

An unblocked choice swaps out one leaf and truncates at its unique
parent star. If that star loses its last leaf, its centre is itself
an unblocked undominated legal next choice. The centre's class is
represented by a strictly earlier leaf, unless it is the root
class. Prioritizing this choice gives a cascade of at most q steps
that either augments or returns to a stable nontrivial-star state.
The inserted vertices create no new neighbours in the retained
forest. The retained centres' class closure is preserved by
truncation.

Every continuing macroscopic step strictly decreases the positive
blocker-list signature ending in infinity. Its finite entries have
sum at most q-1. Including the empty list, the number of such
compositions is exactly 2^(q-1). With explicit scans and at most q
augmentations, the resulting time is P exp(O(q)).

At a certificate exit K=D is the induced current star forest, and
its leaves cover precisely all active classes except the root.
The tested total domination and |D|<=2(|S|-1) are sufficient.
A nonempty totally dominating star forest has |S|>=2, so every
positive epsilon also gives both strict approximate inequalities,
including zero excess outside K. This is the same output contract
as the current-blocker theorem. The fallback therefore legitimately
enters the minimum for both new and derived-public layer rates.



---

**Curated by:** Yilin Liu  
**Signature:** GPT-6 Astra Pro  
**Date:** 2026-10-25  
**Status:** internally reviewed research; no formal verification or external peer review.
