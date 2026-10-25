# Root audit: current-blocker growth under weak Haxell

**25 October 2026. Mathematical reanalysis accepted after root and
independent internal audits.**

This audit covers **weak_haxell_current_blocker_growth.md**, its
birth-growth and historical-certificate prerequisite
**weak_haxell_uniform_lifetime_analysis.md**, and the named-source
comparison in **weak_haxell_public_parameter_comparison.md**.
The independent check is
**weak_haxell_current_blocker_independent_audit.md**.

The underlying algorithm and qualitative matching/certificate theorem
are Annamalai's. The present contribution is an explicit quantitative
reanalysis. This is an internal mathematical audit, not a formal or
external verification, and not a general-graph matching improvement.

## 1. Exact accepted contract

An r-uniform bipartite hyperedge has one left vertex and r-1 right
resources. Let n be the number of left vertices, P the explicit
incidence and vertex-list volume plus two, and let 0<epsilon<1 be a
rational number of input bit length b_epsilon. Under

\[
 \tau(E_S)>(2r-3+\epsilon)(|S|-1)
            \quad\text{for every nonempty }S\subseteq A,
\]

the reanalyzed deterministic algorithm finds a left-perfect matching
in time

\[
 P(n+1)^{O((r/\epsilon)\log(2+r/\epsilon))}
                  \operatorname{poly}(b_\epsilon+\log P).
\]

On an arbitrary input, the certifying version returns either that
matching or nonempty S and an explicit right-resource set C hitting
all of E_S with |C| <= (2r-3+epsilon)(|S|-1). It does not require
an oracle that checks the promise. The bound is uniform in r and
epsilon; it is not polynomial in 1/epsilon, and it gives no claim
at epsilon=0. Ordinary bipartite graph matching for r=2 has stronger
algorithms.

## 2. Public operations and historical certificates

The primary source is [Annamalai, arXiv:1509.07007v2](https://arxiv.org/html/1509.07007v2),
Sections 2--5, including Theorems 1.3 and 5.4. A layer extension uses
the prefix strictly below that layer, initialized with the current
selected and blocker sets. This is the convention consistent with
the source's active-left set and layer invariant; a literal inclusive
prefix call would select the wrong active layer and is not assumed.

Retain the latest candidate from an actual greedy build or extension,
whether accepted or rejected. A rejected candidate adds fewer than
mu times the current selected-set size. While the layer survives,
its lower prefix is fixed. A swap strictly above its direct child
does not meet this layer's right support. A direct-child collapse
can change its blockers but is immediately followed by a new actual
extension attempt. Thus the most recent candidate always contains
the current support at a main-loop boundary.

Extra candidate blockers that later leave the matching remain fixed
physical resources in the certificate. They are not treated as still
matched. Greedy maximality says that all edges of an active left
identity outside the candidate-full set hit the lower forbidden
prefix or the retained candidate support. Its own matching edge, if
any, is already in the lower prefix. This covers all incident edges,
including those not eligible for the source's nonmatching greedy step.

These observations justify persistence without an imagined rerun of
greedy maximality in a later matching state.

## 3. Birth-selected growth remains a separate lemma

With the original parameters

\[
 \mu=\epsilon^2/(10r^2),\quad Q=\lceil1/\mu\rceil,
 \quad\delta_X=\epsilon/(5r^2),
\]

every layer born above a prefix of size W has |X|>delta_X W.
The audit checked the companion proof's explicit hitting certificate,
the loss from full active identities, the small-prefix integrality
case, and the large-prefix slack. The dummy root has no right support
and contributes the necessary subtraction of one in the certificate.

This birth bound applies to immediately collapsing new layers. It
persists because X can only grow while its lower prefix remains fixed.
It must not be replaced by the new current-blocker bound in a collapse
that occurs before the new layer survives a main-loop boundary.

## 4. Current blockers pay for all historical support

Let Y_j be the current matching blockers of a noncollapsible layer.
Its selected edges are right-disjoint, and each matching blocker
meets exactly one selected edge. Therefore

\[
 |B(X_j\cup Y_j)|\le(r-1)|X_j|+(r-2)|Y_j|.
\]

Every extra candidate selected edge with its then-blockers adds at
most (r-1)^2 resources. Noncollapsibility gives
|X_j| <= |Y_j|/(1-mu). Combining these facts, the retained candidate
support C_j and candidate-full active set F_j satisfy

\[
 |C_j|\le(a+\eta)|Y_j|,\qquad |F_j|\le f|Y_j|,
\]

where a=2r-3,

\[
 \eta=\frac{\mu r(r-1)}{1-\mu},\qquad
 f=\frac{\mu(1+\mu)}{1-\mu}.
\]

Both bounds use the current blocker count, not a possibly larger
birth count. For a prefix through layer i, write W=|Y_<i|, including
the dummy root, and Y=|Y_i|. Removing the candidate-full identities
from its W active left identities gives S; uniting the C_j gives a
right hitting set C. Then

\[
 |C|\le(a+\eta)(W-1+Y),\qquad
 |S|\ge W-f(W-1+Y).
\]

For r>=2 and epsilon<1, mu<=1/40 and

\[
 \eta+(a+\epsilon)f
       \le(121/780)\epsilon^2<\epsilon/5.
\]

If W>=2 and Y<=epsilon W/(10r), then Y/(W-1)<=epsilon/(5r).
Substitution bounds the certificate coefficient by
a+31epsilon/50<a+epsilon. The removed fraction is less than 0.028W,
so S is nonempty and the certificate violates the promise. For W=1,
the birth bound and noncollapsibility force both X and Y to be
nonempty. Thus every surviving layer has

\[
                        |Y_i|>\frac{\epsilon}{10r}|Y_{<i}|.
\]

The root independently checked these inequalities, including the
small-prefix and strict-inequality cases.

## 5. Two valid counts yield the same exponent

For the weighted-lifetime count, a layer with fixed lower-prefix
size W has at most
J=1+O(mu^{-1} log(Q/delta_X)) epochs separated by adopted
extensions. Within one epoch, each collapsed child removes more than
tau times its own prefix size from the parent blockers, where

\[
 \tau=\mu\delta_X/Q\ge\epsilon^5/(1000r^6).
\]

This uses the birth-selected bound and the cap Q to count distinct
active left identities. At a child birth the parent is a surviving
noncollapsible layer, so the new current-blocker bound gives
W_child >= (1+delta_Y)W_parent, delta_Y=epsilon/(10r).
For lambda=C delta_Y^{-1} log(2+r/epsilon), a sufficiently large
absolute C ensures

\[
 J\frac{(1+\delta_Y)^{-\lambda}}
          {1-(1-\tau)^\lambda}\le\frac12.
\]

Weighting births by W^{-lambda}, and summing children in reverse
chronological order within each epoch, bounds their total weight by
half their parent's weight. A possible last living child is included.
There is one first positive child per augmenting call. In every finite
execution prefix the total birth weight is at most two. Since W<=n,
the number of births is at most 2(n+1)^lambda. This proves termination
rather than assuming it.

Independently, the public signature still decreases with the same
operation sequence. The new current-blocker growth bounds its length
by O(delta_Y^{-1} log(n+1)). Its maximum coordinate is that length
times a fixed polynomial in r/epsilon and a logarithm in r/epsilon.
Counting bounded-length nondecreasing integer coordinates by a
binomial coefficient, rather than all partitions of their sum, gives
the same logarithmic count O(lambda log(n+1)). This second route
does not need the weighted-lifetime argument.

## 6. Actual work and certificates

A greedy attempt scans explicit input incidences with resource-owner
and cap counters. It does not allocate a Q-sized table or iterate Q
times merely because Q is numerically large. The same scan maintains
the retained candidate support and candidate-full identities. Exact
rational threshold comparisons have polynomial overhead in
b_epsilon+log P.

The certifying implementation checks birth growth whenever a layer
is built, and current-blocker growth for the last affected surviving
layer at a main-loop boundary. Lower layers remain unchanged. Failed
checks return the explicit S,C already justified by candidate
maximality and the prefix bounds. Aggregate candidate reference counts
allow the final certificate to be materialized from explicit input
resources. No global promise test is needed. The n augmenting calls
and polynomial scalar bookkeeping are absorbed in the displayed
uniform exponent.

## 7. Comparison and attribution

The checked public baseline is stronger than a coarse all-partitions
count. A length-aware count of Annamalai's original signature already
gives exponent O((r^2/epsilon) log(2+r/epsilon)). Its printed theorem
states polynomial time for fixed parameters, not that explicit
uniform formula.

[Graf--Haxell, arXiv:1811.02687v2](https://arxiv.org/html/1811.02687v2),
Theorem 4 and Section 7.1, also applies under the same hypergraph
promise. Its constellation overlap saves a right resource per leaf;
charging every dominating vertex separately would incorrectly lose
the 2r-3 threshold. With its displayed feasible parameters and
epsilon'=epsilon/(r-1), a length-aware count has the same rank-squared
order. The authors do not claim optimized parameter dependence.

Accordingly the accepted improvement is a new current-blocker lemma
and a sharper uniform analysis of a named public algorithm. No claim
is made that all possible public reanalyses or all algorithms have
been optimized. The stronger-expansion almost-linear hypergraph
results have a different promise and are not substitutes for this
near-threshold comparison.
