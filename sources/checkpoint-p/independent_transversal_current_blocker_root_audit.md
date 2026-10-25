# Root audit: a uniform current-blocker transversal algorithm

**25 October 2026. Root mathematical and implementation audit completed.**

The audited proof is **independent_transversal_current_blocker_growth.md**.
Its independent check is
**independent_transversal_current_blocker_independent_audit.md**,
its adjacency-list implementation is
**independent_transversal_input_linear_iteration_implementation.md**,
and its literature comparison is
**independent_transversal_public_uniform_baseline_audit.md**.
The root read the full proof and implementation and directly checked
the relevant definitions, operations, and signature interfaces in
[Graf--Haxell, arXiv:1811.02687v2](https://arxiv.org/html/1811.02687v2).

The accepted result is a sharper uniform analysis with a new certified
stopping rule in a named public algorithm. The qualitative output
alternative is public. This is internal mathematical review, not formal
verification, external review, or a benchmark.

## 1. Accepted contract, including arbitrary partitions

Let G be a loopless graph whose vertices are partitioned into q nonempty
classes. Write P=|V|+|E|+q+2 and assume partition-relative r-claw-freeness:
no vertex has r independent neighbours in distinct classes. Let
0<epsilon<1 be rational, with bit length b_epsilon. The algorithm returns
an independent transversal, or an explicit class set S, vertex set D,
and constellation K on a class set S_0 containing S, with

\[
 |D|<(2+\epsilon)(|S|-1),\qquad
 V(K)\subseteq D,\qquad
 |D\setminus V(K)|<\epsilon(|S|-1).
\]

D totally dominates every vertex in the classes of S: membership in D
does not substitute for an adjacent vertex in D. D may contain vertices
outside those target classes. K is induced in G_(S_0), meaning the
graph restricted to S_0 with all within-class edges deleted. It is not
claimed to be induced in the original graph before that deletion.
Its components are nontrivial stars, and its leaves form an independent
transversal of all but one class of S_0.

The uniform explicit-input time is

\[
 P(q+1)^{O(\epsilon^{-1}\log(2+r/\epsilon))}
                 \operatorname{poly}(b_\epsilon+\log P).
\]

The supplied claw parameter can be capped at q+1, with its input
encoding read separately if necessary. Hence every arbitrary
vertex-partitioned graph has the specialization

\[
 P(q+1)^{O(\epsilon^{-1}\log(2+q/\epsilon))}
                 \operatorname{poly}(b_\epsilon+\log P).
\]

For fixed epsilon this is quasipolynomial in the number of classes
and linear in explicit graph input up to the displayed bit factor.
The alternative certificate can coexist with an independent
transversal. Therefore this is not an algorithm for exact unrestricted
independent-transversal decision, nor a claim about the unrestricted
general-graph maximum-matching exponent.

## 2. Preprocessing and feasible parameters

Deleting within-class edges changes no independent transversal and
no adjacency between vertices in distinct classes. It preserves the
partition-relative claw condition and agrees with the constellation
definition. Repeatedly choosing an isolated vertex and removing its
class is safe: it is independent of all then-remaining classes, and
the chosen vertices can be restored to the final transversal. A later
certificate uses unchanged remaining classes and lifts to the original
graph with the stated G_(S_0) convention. A degree queue implements
this preprocessing within the input scan allowance.

Use mu=rho=epsilon/(100r) and Q=ceil(1/mu). Direct substitution in
Definition 10 verifies all source feasibility inequalities. In
particular mu<=1/200, 1/Q<=mu, and the common bracket after multiplying
by 1-mu is at least 1-3mu-mu^2. The constant 100 leaves more than
enough slack in both error inequalities. No numerical-Q allocation
or loop is necessary.

The original small-birth stopping rule and its full source certificate
are retained. Thus the original birth-selected growth remains available
for lexicographic decrease, including immediately collapsing layers.

## 3. Fresh current candidates and the induced-star invariant

After every change to the partial independent transversal M, the
actual SuperposedBuild visits all layers that survive it. An adoption
at layer j deletes every higher layer. Consequently each surviving
layer has a greedy candidate built with the current M and its unchanged
lower prefix, or M has not changed since that candidate was built.
If an extension was rejected, its extra selected set E_j has size
less than mu|X_j|. If adopted, its current extra set is empty.

The actual operations also prove anticompleteness between current
layers. A newly selected vertex avoids all existing selected and
blocker vertices. Any new matching blocker adjacent to an earlier
selected vertex would already be an earlier blocker and would have
prevented that selection. Matching blockers are mutually independent.
Adoption truncates higher layers, and collapse removes blockers.
Thus the current blocked selected vertices and their blockers induce
disjoint stars. Vertex-disjoint layer supports alone would not prove
this property; the actual selection rule is essential.

These facts justify using current candidates directly. The proof does
not infer maximality from an unexecuted hypothetical rerun. It also
does not transplant the simpler weak-Haxell lifetime tree, since here
an adoption can discard many higher layers without their collapse.

## 4. The complete certificate from a slow-growing prefix

For a surviving prefix through i put

\[
 W=1+\sum_{j<i}|Y_j|,\qquad
 T=\sum_{j\le i}|Y_j|=W-1+|Y_i|.
\]

Its active class identities are the unmatched root class and the
distinct matching-representative classes below i. Remove classes full
in their actual candidates and all classes containing candidate-extra
selected vertices. Let S be what remains. Let D contain all candidate
selected and blocker vertices, plus one arbitrary neighbour of each
currently unblocked selected vertex.

For a vertex in a retained class, a current selected vertex is adjacent
to its blocker or the added neighbour. A candidate blocker is adjacent
to a candidate selected vertex. A candidate-extra selected vertex
cannot be in a retained class. Every remaining vertex would still be
addable unless it had a neighbour in the candidate or lower prefix.
The actual greedy maximality therefore proves total domination. This
case split includes a class's current M representative and vertices
that themselves belong to D.

Noncollapsibility gives sum|X_j| <= T/(1-mu). An extra selected vertex
has at most r-1 matching neighbours, using partition-relative
claw-freeness. With

\[
 \eta=\frac{\mu(r+2)}{1-\mu},\qquad
 f=\frac{\mu+(1+\mu)/Q}{1-\mu},
\]

the root independently obtains

\[
 |D|\le(2+\eta)T,\qquad
 |D\setminus V(K)|\le\eta T,\qquad
 |S|\ge W-fT.
\]

Here K consists of the current blocked selected vertices and their
current blockers. The latter are its T independent leaves in distinct
classes. Adding the root class gives S_0 with exactly T+1 classes;
all centres lie in S_0, and S is contained in S_0. The r+2 in eta
pays candidate extras and their blockers, currently unblocked
selected vertices, and their chosen neighbours. It does not pay for
all vertices of any excluded class.

For the chosen parameters,
eta<epsilon/40, f<epsilon/90, and
eta+(2+epsilon)f<epsilon/10. If W>=2 and |Y_i|<=epsilon W/10,
then T<=(1+epsilon/5)(W-1). Substitution gives

\[
 |D|<(2+13\epsilon/25)(W-1)-(2+\epsilon)fT
        <(2+\epsilon)(|S|-1).
\]

Also |S|-1 >= (1-epsilon/75)(W-1)>0 and
|D\setminus V(K)| <= 3epsilon(W-1)/100
<epsilon(|S|-1). Thus the failure case supplies the complete
domination and constellation contract. When W=1, the retained birth
check and noncollapsibility force a nonempty blocker set directly.

Every continuing boundary therefore has

\[
 |Y_i|>\frac{\epsilon}{10}
                 \left(1+\sum_{j<i}|Y_j|\right).
\]

This is current blocker growth, not a monotonicity assertion about a
layer's birth blockers. Its coefficient no longer contains r.

## 5. The signature argument is retained and counted more tightly

The original continuing operations, birth-selected growth, and
adoption/collapse rules retain the source's lexicographic decrease
and nondecreasing absolute signature coordinates. The new certificate
only adds a possible exit. The current-blocker inequality bounds the
number of surviving positive layers by
L=O(epsilon^{-1} log(q+1)).

The original logarithmic base is b=Q/(Q-mu rho), with
log b=Theta(mu^3). The largest finite coordinate is at most

\[
 H=O\left(\mu^{-3}
      [L\log(1/\rho)+L\mu+\log(q+1)]\right).
\]

There are at most 2L finite coordinates of fixed signs and weakly
increasing absolute values. The count by height and length is
exp O(L log(2+H/L)), giving
(q+1)^{O(epsilon^{-1} log(2+r/epsilon))}. Using an upper L larger
than the actual possible number of layers only overcounts. Trivial
instances with at most one remaining class are handled directly.

This count applies to every finite continuing execution prefix, so
it proves termination. It does not assume the augmenting call has
already finished. The logarithms in the signature are proof devices;
the operational algorithm only compares rational multiples of integer
counts.

## 6. The linear explicit-input multiplier is justified

During one BuildLayer call, M, the lower prefix, and the active classes
are fixed, while candidate X,Y and all exclusion/neighbour counters
only grow. A failed addability test stays failed. Therefore a single
fixed-ID pass over vertices implements the same permitted greedy
routine. Each selected vertex's adjacency is scanned once to find
its matching neighbours, and each activated vertex's adjacency is
scanned once to update exclusion counts. The cost is O(P), including
scratch initialization and copying the resulting candidate.

A SuperposedBuild invokes at most q+1 such calls. Each collapse
strictly decreases the layer count before any further truncation.
There are at most q+1 collapses in one outer iteration, so a safe
cost is O(P(q+1)^2). Both the original small-birth certificate and
the new current-blocker certificate fit that allowance. Retaining
at most q+1 candidate lists uses the explicitly allowed O(P(q+1))
space; no input-linear space bound is claimed.

The at most q augmenting calls and polynomial powers of q+1 are
absorbed in the signature exponent. Rational comparisons and common
input encodings account for the bit factor. This proves the stated
P multiplier, rather than the source's coarse per-iteration |V|^4
implementation bound.

The same adjacency-list implementation applies to the named public
baseline. It is common implementation work, not an extra advantage
given only to the new current-blocker rule.

## 7. Fair public comparison and final scope

Counting the original source signature by both length and height
already gives the stronger derived-public baseline

\[
 P(q+1)^{O((r/\epsilon)\log(2+r/\epsilon))}
                \operatorname{poly}(b_\epsilon+\log P).
\]

This is not the exponent printed in the theorem. The new certificate
removes the factor r outside the logarithm by shortening the maximum
surviving signature. The full arbitrary-partition specialization is
quasipolynomial for fixed epsilon because r<=q+1 can always be used.

The root also checked [Harris, arXiv:1909.08065v6](https://arxiv.org/html/1909.08065v6),
Theorem 1.5(1). It already gives deterministic polynomial-time weighted
independent transversals for blocks of size at least (2+epsilon)Delta.
That algorithm is stronger on its degree/block-size promise. It does
not state the arbitrary-partition total-domination and constellation
alternative audited here. The comparison must not describe that
special-case line as merely randomized.

The accompanying literature audit checks further primary sources but
does not establish global priority or optimality. The safe accepted
claim is a sharper quantitative construction for this full certificate
contract. Its weak-Haxell specialization is the same mechanism as the
rank-linear hypergraph reanalysis, not an unrelated second matching
breakthrough. No polynomial reciprocal-slack bound, exact IT decision
algorithm, or smaller general-graph matching exponent follows.

## 8. The elementary exponential fallback is also part of the comparison

The source's elementary single-vertex procedure has a useful stronger
count than a separate upper bound of r on every coordinate. The
complete argument is
**independent_transversal_elementary_exponential_fallback.md**,
which the root read and independently checked.

At a stable state its selected centres have disjoint, nonempty current
blocker sets. Their positive counts form a list of total sum at most
q-1. Appending a blocked centre decreases the lexicographic list
terminated by infinity. Swapping in an unblocked vertex removes a
blocker from its unique earlier parent and truncates later stars.
If that parent becomes unblocked, immediately swap in its free centre
and continue toward an earlier parent. This zero-blocker cascade has
at most q steps and either augments or ends at a smaller stable list.

There are exactly 2^{q-1} positive integer lists of total sum at most
q-1, including the empty list. Hence there are at most that many
stable steps per augmentation, up to the explicitly charged cascade.
Adjacency scans give total P exp O(q) work. At a failed search, the
induced star forest K totally dominates its active classes S and
has at most 2(|S|-1) vertices. Taking D=V(K) satisfies the full
approximate contract for every positive epsilon. A certificate exit
has at least two classes, so the desired strict inequality follows.

This is a public fallback, not a separate new result. The accepted
research time may therefore be written

\[
 P\min\left\{\exp O(q),\,
       (q+1)^{O(\epsilon^{-1}\log(2+r/\epsilon))}\right\}
                 \operatorname{poly}(b_\epsilon+\log P).
\]

The named public layer baseline receives the same fallback, with
its older exponent in the second term. Alternating the two algorithms'
work budgets achieves the minimum up to a constant factor without
needing to compare unknown asymptotic constants in advance. For fixed
epsilon and unrestricted r<=q+1, the new second term is quasipolynomial
in q, while the elementary fallback is exponential in q. For very
small epsilon the fallback may be better and must remain visible.
