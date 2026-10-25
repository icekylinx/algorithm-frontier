# A lower update-time curve for fully dynamic approximate APSP

**Auxiliary research derivation, 25 October 2026.** The main theorem,
arbitrary-degree implementation, and public comparison are now in
`apsp_time_stretch_tradeoff.md`, with the independent interface audit in
`apsp_tradeoff_independent_audit.md`. Use those files for the current
statement. This note retains the initial parameter derivation and uses the already
separated metric, work, and recourse expressions of
`separated_metric_forest_and_strong_sssp.md`. It changes the target
tradeoff: the metric stretch may have a larger logarithm than the
update time. It does not change the 7/8 strong-forest/Gomory--Hu
optimization, whose outer covering condition charges that stretch.

The quantitative candidate is a fully dynamic APSP oracle with
subpolynomial stretch, polynomial logarithmic query time, and an
amortized update factor with leading logarithmic power arbitrarily
close to 3/4. The public-baseline audit for this precise work/stretch
tradeoff is in the main note cited above.

## 1. The audited local envelope

Put \(U=\log(N+4)\), \(h=\log(U+4)\). The master inventory cap
\(N\) is used only to choose numerical parameters. Actual work is
charged to actual instance sizes and actual updates.

Use local parameters \(p,r,K\), degree-reset branching
\(k=2^x\), and depth \(d=O(U/x)\). The previously audited
expressions are

\[
 \begin{split}
 g&=O((p+r)h),\\
 f&=O(U/p+U/r+r^2h+(p+r)h),\\
 \log P&=O(U/K+g+h),\\
 B&=O(x+f+Kg+d\log P+h),\\
 a&=O(dKg+dh).
 \end{split}
 \tag{1}
\]

Here \(\exp O(B)\) bounds work and explicit local representation
recourse, while \(\exp O(a)\) is the all-pairs metric stretch.
The pivot query visits one vertex at each level and uses exact
precomputed base APSP, so its time is
\(O(d\operatorname{poly}(U))\), not \(k^{O(1)}\).

The construction-level chronological update bound, including late
spending of initial selected-edge credit, is already part of the
derivation of \(B\). It is not replaced here by a worst-case update
claim. The present update bound is amortized.

## 2. A one-parameter tradeoff

Choose, up to sufficiently large fixed constants and integer rounding,

\[
       p=r=t,\qquad K=t^2,\qquad x=U/t,
       \qquad d=O(t).
 \tag{2}
\]

For \(t\to\infty\), the required dominance
\(x\gg\log P\) holds throughout the range below. Fixed small
parameter cases are handled separately by the actual-size base
algorithm.

Substituting (2) into (1) gives

\[
 \begin{split}
  f&=O(U/t+t^2h),\\
  \log P&=O(U/t^2+th),\\
  B&=O(U/t+t^3h),\\
  a&=O(t^4h).
 \end{split}
 \tag{3}
\]

The corresponding one-level forest occurrence recurrence would give
\(\log\gamma_{\rm cong}=O(U/t+t^2h)\), but the standalone distance
oracle does not require exposing a final low-congestion forest.

In particular, for

\[
                 1\ll t\le (U/h)^{1/4},
 \tag{4}
\]

the work term simplifies to \(B=O(U/t)\). Thus the distance oracle
has the curve

\[
 \boxed{
   \text{amortized work factor }\exp O(U/t),\qquad
   \text{stretch }\exp O(t^4h),\qquad
   \text{query time }\operatorname{poly}(U).
 }
 \tag{5}
\]

Its initialization work is the actual initial size times the work
factor. A finite update history of length \(z\) adds
\(z\exp O(U/t)\) amortized work. The graph model and local update
encoding remain those of the audited fully dynamic distance hierarchy.

The familiar equal-factor choice is
\(t=(U/h)^{1/5}\), for which work and stretch both have logarithm
\(O(U^{4/5}h^{1/5})\). Equality of the two factors is a choice of
objective, not a requirement of the APSP query proof.

## 3. Subpolynomial stretch with a 3/4 leading work power

For any fixed constant \(C>0\), set

\[
                  t=(U/h^{C+1})^{1/4}.
 \tag{6}
\]

Then (5) becomes

\[
 \boxed{
  \begin{array}{ll}
  \text{work factor:}&
    \exp O\bigl(U^{3/4}h^{(C+1)/4}\bigr),\\[2mm]
  \text{metric stretch:}&
    \exp O(U/h^C)=N^{O(1/h^C)},\\[2mm]
  \text{query time:}&\operatorname{poly}(U).
  \end{array}}
 \tag{7}
\]

Since \(h\to\infty\), the stretch is \(N^{o(1)}\). The leading
power in the logarithm of the update factor is 3/4, with an explicit
iterated-logarithm factor.

More generally, choose any sufficiently slowly growing
\(\omega(U)\to\infty\), and set

\[
 t=(U/h)^{1/4}/\omega(U),
 \quad B=O(U^{3/4}h^{1/4}\omega(U)),
 \quad a=O(U/\omega(U)^4).
 \tag{8}
\]

As long as \(t\to\infty\), this also has subpolynomial stretch.
No finite claim that the stretch is constant or polylogarithmic follows
from (7) or (8). The stretch is larger than at the equal 4/5 point;
the update factor is smaller.

For a chosen logarithmic stretch budget \(Q=t^4h\), the same curve
can be written

\[
                    B=O\bigl((U^4h/Q)^{1/4}\bigr).
 \tag{9}
\]

## 4. Query paths and finite arithmetic

The distance query is the pivot chain of the main strong-forest note.
Exact local legs and a recursively returned child walk are concatenated
with the stored normalized routes. Its numerical estimate is always an
upper bound on the length of a valid physical walk and has the stretch
in (5). These stored lifting witnesses prove existence and metric
domination. This auxiliary note does not assert a reporting bound in
terms only of the final projected walk or simple-path size: internal
connector expansion and subsequent loop erasure need their own
accounting. The numerical distance query does not enumerate the walk.

At most \(d=O(t)\) length scales are composed. The conservative
bit bound \(O(Ud)\) from the polynomial-bit forest adapter remains
polynomial in \(U\), since \(t\le U^{1/4}\). Its arithmetic and
weighted-instance factors are included in polynomial logarithms. No
new long-denominator numerical operation is introduced by the choice
of parameters.

## 5. General physical degrees for a distance oracle

The metric hierarchy's bounded-degree input can be obtained for a
general graph without exposing a flat forest on that graph. For a
finite update history cap \(N\), attach a fixed-height virtual binary
port tree to each actual vertex. Allocate only the nodes on paths to
ports actually used by edge incidences. One newly allocated incidence
uses \(O(\log N)\) nodes and edges; a removed incidence may leave its
allocated connector paths as ghosts until the next global rebuild.

Give connector edges length one and each original positive edge length
\(\ell_e\) a proxy length \(H\ell_e\), with
\(H\ge C\log N\). The roots are the query representatives. The
proxy has degree at most three. Projecting a proxy walk discards its
connector edges, and lifting a physical walk adds only \(O(\log N)\)
connector length per physical edge. Since every physical length is at
least one,

\[
        d_G(u,v)\le d_{\rm proxy}(q(u),q(v))/H
                         \le 2d_G(u,v).
 \tag{10}
\]

Only \(O((m_0+z)\log N)\) nodes and edges are allocated for an
initial graph of size \(m_0\) and \(z\) updates; a virtual tree with
\(N\) leaves is never materialized at every vertex. Isolated original
vertices are answered directly and do not pad the active hierarchy.
Each original edge update becomes a polynomial logarithmic number of
bounded-degree proxy edits. A physical length replacement is encoded
as deletion and insertion of the corresponding real proxy edge.

For distance queries this wrapper needs no contraction of every
physical null fiber. It simply divides the proxy estimate by \(H\),
and projects a reported walk. Therefore a large original physical
degree does not reappear as a cost for rebuilding a flat forest's null
component. This is a difference from the stronger forest interface,
whose general-degree cut application uses the dedicated degree-three
capacity expansion.

The finite-history formulation is sufficient for the current theorem
assembly. A maximum-live-size formulation can use periodic rebuilds and
port-pool resets, but that lifetime bookkeeping should be stated and
charged separately rather than assumed for free.

## 6. Scope and remaining comparison

This note is a parameter corollary of the audited metric hierarchy.
The leading 3/4 work power does not improve the 7/8 strong-forest or
Gomory--Hu theorem by substitution: their covering constraint depends
on \(a\), and the larger stretch in (7) correspondingly restricts
their outer parameters.

The exact public comparison for fully dynamic APSP at the stretch in
(7) still needs to be checked. In particular, an old theorem bundling
work and approximation into one common factor may admit a useful
retuning. The claim here is the explicit feasible curve (5), not an
unverified statement that every point on it is unprecedented.
