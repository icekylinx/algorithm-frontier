# Audit of the certified-layer / flat-support interface

**25 October 2026. Status: passes.** This audit checks the connection
between `destructive_apsp_path_support_extractor.md` and
`certified_no_superpose_haxell_path_routing.md`, together with the
quantitative expander substitution. The outer note supplies its own
layer-growth and signature proof; this audit does not treat the BHHS
approximate-half-layer theorem as a replacement for that new proof.

## 1. The seen registry is fresh for each build

The static input graph is reused by many outer layer builds. Each build
creates its own temporary graph instance, deletes its current forbidden
prefix, and initializes its own occurrence registry and original-edge
seen flags. The seen flags are global only inside this one build.

Within a build, a consumed edge never returns. Across two builds, the same
original physical edge may be available again. Reinitializing and consuming
it again is paid by the number-of-builds multiplier. A seen flag from an
earlier build must not suppress its occurrences in a later build.

The only persistent output of a destroyed build instance is its selected
simple path set and its physical edge-identifier certificate. Neither
retains handles to the retired flat forests. Both main notes now state this
fresh-registry rule explicitly.

## 2. No uncharged path-length or conductance multiplier

For one build let \(S_j\) be its accepted distinct-edge supports. Each is
permanently removed before the next accepted query, so

\[
                   \sum_j |S_j|\le m.
\]

The flat dynamic-tree aggregate skips connector/null paths and repeated
occurrences of an already seen original edge. The total occurrence
marking, topology changes, and registry updates are bounded by the
allocated flat representation's lifetime inventory. The independent
destructive-support audit establishes this as
\((n+m+q)\exp O(B)\), including all local ball trees, base shortest-path
trees, and late child-edit credit.

Each accepted query produces a nonempty support, so there are at most
\(m\) successes. Each active named demand has at most one final rejected
query in the certified build. Its counter may be as large as \(\Delta\),
but the algorithm does not issue \(q\Delta\) unsuccessful queries.
Thus there are \(O(m+q)\) queries in a build.

The current matching consists of edge-disjoint literal paths. A physical
edge-to-matching-path ownership table is built in \(O(m)\) work. When a
support touches a matching path, that entire matching path is removed once
in this build. All such additional removals total at most \(m\) edges.
The source forest update cost is charged by those actual deletions, not by
the symbolic upper bound on their possible lengths.

These facts establish

\[
                  \widehat T=(n+m+q)\exp O(B)
\]

even when the comparison path bound \(h_0\) is polynomially large. There
is no layered graph with \(h_0\) copies, no traversal of \(h_0\) edges
per failed query, and no running-time multiplication by \(1/\phi\).
Only the length/rank and strong-hitting hypotheses depend on those values.

For an unweighted graph, \(h_0\) may be capped at \(n-1\) without
changing the set of comparison simple paths. In the expander application
the displayed \(18\log n/\phi\) is already representable with
\(O(\log N)\) bits: positive conductance in a finite unweighted graph is
at least an inverse polynomial in its edge count. Neither choice changes
the backend's input lengths, which remain one before its ordinary positive
connector scales.

## 3. The oracle's arbitrary-state exception is absent in these calls

The standalone half-layer oracle must prevent a query from returning its
own demand's current matching path. The companion extractor handles that
using a temporary deletion scan, with \(O(m+q)\) total trials.

The certified-layer algorithm has a simpler input invariant. At the first
layer its active demands are unmatched. At a later layer its active set is
\(A(Y_\ell)\), and its initial forbidden set contains the complete
physical supports of \(Y_\ell\). Therefore the own matching path is
already unavailable. No temporary exclusion is required in these calls.

This is relevant to the hitting certificate. A rejected query then rules
out **every** comparison-length path for that active demand in the
residual graph. The conclusion is not restricted to paths other than one
possibly still-present matching path. The outer proof explicitly uses the
valid-state property rather than importing the standalone approximation
inequality as if it were a hitting certificate.

The fully dynamic distance backend is still an appropriate source: its
degree adapter and internal hierarchy can perform insertions while encoding
the original deletions and rebalancing auxiliary trees. The theorem does
not silently substitute a decremental-only auxiliary API.

## 4. Certificate size versus actual storage

Write \(R=\lceil\Gamma h_0\rceil\). Every accepted support has at most
\(R\) edges. If it touches \(b\) matching paths, then \(b\le|S|\)
and every touched path has length at most \(R\). The union newly removed
on that step has size at most

\[
             |S|+(R-1)b\le R|S|\le R^2.
\]

The subtraction of one per touched path is legitimate: each such path
contains an edge of \(S\), and different matching paths are edge-disjoint.
Consequently the whole build certificate obeys

\[
                    |C_i|\le R^2|X_i|.
\]

It is also literally a subset of the static \(m\)-edge universe, so
\(|C_i|\le m\). The proof uses the former bound to obtain layer growth
and uses the latter to store or discard the certificate. It never allocates
\(R^2|X_i|\) slots when that exceeds the actual edge universe.

The exact blockers \(Y_i\) may be a proper subset of all matching paths
touched by the larger supports. The certificate includes the latter's
physical edge identifiers anyway. This is why it remains a hitting set
after some of those paths leave the matching. Its meaning does not depend
on dereferencing a mutable matching-path object.

## 5. Lifetime check for the outer certificate proof

While layer \(i\) survives, its selected paths \(X_i\) are fixed. Its
blockers \(Y_i\) can shrink when layer \(i+1\) collapses. The prefix
through \(i-1\) cannot change while \(i\) survives: changing
\(Y_{i-1}\) requires collapsing and discarding layer \(i\) first.

Thus the active demand set and forbidden prefix at the birth of a surviving
layer remain appropriate for its fixed certificate. The inclusion
\(B(X_i\cup Y_i)\subseteq C_i\) persists when \(Y_i\) shrinks.
Every current active demand belongs to the active set of one uniquely
corresponding surviving/new layer. The union of those physical certificates
therefore hits all short hyperedges incident to the nonsaturated demand
set used in the growth argument.

I also checked the numerical margins in the growth and signature proof.
With \(\mu=1/10\) and \(\Psi\ge\Delta R^2\), the contradiction is
\(4\Delta/5>20/9\), valid for \(\Delta\ge4\). The smallest collapsed
index changes the preceding blocker count by at least a \(1/100\)
fraction while all earlier coordinates and its selected set stay fixed.
This makes the stated base-\(1.01\) signature strictly decrease. The
weighted absolute coordinates are nondecreasing, with the factors of five
covering the lower growth constants. The integer-partition count gives the
claimed
\(\exp O(\log N/\sqrt{\log\Delta})\) number of builds.

## 6. Quantitative expander substitution

BHHS Lemma 4.2 supplies the sole graph-theoretic black box:

\[
 h_0=\lceil18\log n/\phi\rceil,
 \qquad \Psi\ge\frac{\phi\delta}{32k}.
\]

Using a ceiling only enlarges the short-path hypergraph relative to the
source's floor convention and cannot reduce its hitting parameter. The
new condition \(\Psi\ge\Delta R^2\) follows from

\[
                \phi^3\delta
                   \ge Ck\Delta\Gamma^2\log^2 n.
\]

Here \(C\) is a sufficiently large fixed constant and the declared
\(\Gamma\) includes the external degree adapter. The output length is
\(O(\Gamma\log n/\phi)\). Since each demand uses two endpoint
incidences, \(q\le nk/2\); the density condition implies \(k\le\delta\)
up to a harmless fixed factor, so \(q=O(n\delta)=O(m)\).

Let \(a=\log\Gamma\) and \(s=\log\Delta\). The full formula is

\[
\begin{aligned}
 T&=(m+n)\exp O(B+U/\sqrt{s}),\\
 \text{path length}&=O(\exp(a)\log n/\phi),\\
 \phi^3\delta/k&\ge\log^2n\,\exp O(s+2a).
\end{aligned}
\]

For the separated APSP curve, choose
\(B=O(U/t+t^3h)\), \(a=O(t^4h)\), and
\(s=\Theta(t^2)\). The outer iteration cost is \(O(U/t)\), while
\(s+2a=O(t^4h)\). Thus the two explicit time/length/density points in
the outer main note follow with all external factors included.

This is an explicit quantitative improvement route under the specified
expansion and density promise. The public BHHS theorem already states a
qualitative deterministic almost-linear result, and the new application
must not be described as the first such qualitative theorem. Its novel
pieces here are the explicit curve, the destructive flat-support oracle,
and the fixed-certificate outer construction.
