# Independent audit of clipped numerical path reporting

**25 October 2026. Targeted mathematical audit completed.**

This audit covers Sections 1--2, 4 and 8 of
`clipped_walk_queries_and_dynamic_spanner.md`. It does not duplicate the
independent nested-clock audit of `fully_dynamic_spanner_five_sixths.md`.
The result is a bounded-length reporting interface, not a query bound
depending only on the length of the final loop-erased path.

## 1. Positive no-reset expansion

The numerical graphs in the no-reset Steiner hierarchy contain selected
parent edges at their physical endpoints and compressed nonempty paths
in parent forests. Typed null edges of the arbitrary-forest lift are not
numerical edges. Consequently every numerical edge occurrence above the
root has at least one child occurrence when expanded one level.

The local descriptor family is sufficient: nearest-pivot trees provide
the two pivot legs, a distinct strict-ball shortest-path tree provides
a strict-ball terminal leg, and exact base tables retain paths as well
as numbers. The strict-ball tree cannot in general be replaced by the
nearest-pivot tree. The audited ball and inverse-cluster guarantees pay
for maintaining these local trees; the numerical query does not search
the whole ball afresh.

A query has at most two local legs per level plus one terminal leg.
Expand all their edge occurrences into a forest whose leaves are
root-edge occurrences. At any fixed depth, distinct internal
occurrences have disjoint descendant leaf-occurrence sets. Charging
each internal occurrence to one descendant leaf at that depth is
therefore injective. Every leaf receives at most one charge per level.
For depth d, there are at most (d+1) times as many expansion records
as root-edge occurrences, plus O(d) descriptor headers. Physical edges
may repeat; this argument counts occurrences, so it does not assume
their disjointness.

If root lengths are positive integers and the accepted estimate is at
most R, the represented root walk has at most R edge occurrences.
Thus its complete expansion costs (R+1) polylog(N). Stack-based loop
erasure has the same bound and returns a literal simple path no longer
than the estimate. A much shorter final simple path does not make the
expanded walk free.

## 2. Lifetimes and output consistency

Every numerical edge has a lifetime ID. A compressed path whose
underlying path changes must retire its old ID and obtain a new one.
Selected original edges retain their original lifetime identity.
Query descriptors are read and enumerated in one settled version;
there is no concurrent structural update. Metadata needed by retiring
records remains available until that retirement transaction finishes.

These rules suffice. They do not require retaining all historical
forests, and they do not permit reusing a descriptor after its version
has been retired. In particular, the path is materialized before the
spanner algorithm changes saturation eligibility.

## 3. One arbitrary-degree root adapter

The current-incidence binary-tree adapter uses a permanent root handle
per original vertex, unit positive connector edges, and a length-H edge
for each unweighted original edge, with H a sufficiently large
polynomial logarithmic scale. It allocates records for actual incidences,
not a master-sized port tree at each vertex. Balanced-tree changes use
polynomially many logarithmic native edits; retired isolated records are
charged to actual births and replacements.

Projection deletes connectors and divides real-edge lengths by H. A
simple original b-edge path lifts through O(b log N) connectors, so
the native distance divided by H lies between the original distance
and twice that distance. A scaled accepted estimate R therefore
requires enumerating at most HR positive native length. H is
polylogarithmic and preserves the clipped bound. Projecting before
loop erasure handles repeated original vertex images safely.

There is no need to enumerate arbitrary unused branches or scan the
adjacency list of a high-degree original vertex during a path query.

## 4. Positive-port hierarchies need a different argument

The research normalized positive-port hierarchy and the reconstructed
public positive-port hierarchy have native connector edges whose parent
projection is empty. The nonempty-expansion proof in Section 1 does not
apply to them.

At boundary j let H_j be its positive scale, and write
sigma_j for the product of preceding scales. An accepted estimate is
the sum of local positive query-leg lengths divided by their respective
sigma_j. A child edge projects to a parent walk of length at most its
label divided by H_j; empty connector projection only decreases that
length. Inductively, the total native walk expanded at level j,
including its local legs, has length at most sigma_j R. Positive
integer native lengths bound its number of occurrences by that same
quantity. Therefore the total cost is

    (R+1) exp(O(d log log N)) polylog(N).

This counts connectors at their own level even when they later vanish.
No root-real-edge charging is applied to those empty projections.

The required selected-core witnesses are genuine parent paths no
longer than their labels. This is the retained KMG metric interface,
not an assumption that metric distortion is free. The source numerical
query is KMG Algorithm 6 and Claim 4.4; its local legs and selected-edge
identities give the descriptors. The exact base requires paths or
next-hop information, which can be constructed within its already
allowed polynomial local work.

## 5. Threshold and public comparison

The acceptance threshold uses the actual numerical stretch gamma_0.
The additional reporting multiplier Q_path enters running time. A
larger envelope Gamma >= gamma_0 max(1,Q_path) may summarize the final
bounds, but it is not substituted for gamma_0 in the girth test.
The audited clipped note states this distinction explicitly.

At all parameter points used by the companion spanner theorems,
d log log N is dominated by the stated logarithmic stretch/work
envelopes. Thus the reconstructed public hierarchy receives a valid
clipped reporting interface as well. A comparison cannot exclude it
merely because its principal theorem was numerical APSP.

The unrestricted-deletion five-sixths construction deliberately uses
the conservative no-reset K-squared local repair cost. Its reporting
argument does not depend on the unresolved possibility of applying the
normalized repair interface at growing native degrees. The sharper
deletion-bounded curve uses the already audited positive-port normalized
provider and pays its explicit Q_path factor.

## 6. Conclusion and remaining scope

No gap was found in these reporting interfaces. Their combination with
the separately audited spanner reduction is valid as a research proof
assembly. This audit does not establish ordinary output-sensitive path
queries, a smaller general-matching exponent, or the subsequent proposed
direct flat-forest spanner construction; those require separate proofs.

