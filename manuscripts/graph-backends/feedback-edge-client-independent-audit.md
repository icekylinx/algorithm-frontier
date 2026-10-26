# Independent audit: the feedback-edge one-sided client

**25 October 2026.** Audited in full:
[feedback-edge-one-sided-client.md](feedback-edge-one-sided-client.md), Sections 1--9.

**Verdict:** the parameterized client passes this audit. With the
entire ordinary allocation graph equal to a spanning forest plus at
most k chords, its exact conservative path query and simple-path
update cost `(k+1) polylog S`, plus register notifications. The
resulting static bound is `(m+nu(k+1)) polylog S`. The theorem does
not imply that k is small for general degree-three allocation graphs.

The numerical interface is the previously audited
[complete-unrestricted-forest-one-sided-client.md](complete-unrestricted-forest-one-sided-client.md); this audit checks
the new core reduction, represented-path simplification and their
interaction with that interface.

## 1. The compressed core preserves the relevant directed paths

Marking every chord endpoint leaves at most 2k marks. The minimal
marked subtrees, after suppression of unmarked degree-two vertices,
have O(k) retained vertices and virtual edges. Different virtual
edges have disjoint interiors, and every chord endpoint is retained.
Thus their expansion is a genuine subdivision of the virtual forest,
with no chord attached to an unrepresented interior vertex.

The topology uses hop counts, not numerical donor prices. Its
virtual paths remain valid while the numerical ledger changes.
Reading their two directed donor sums costs one dynamic-tree query
per direction. Distinct directions may have different costs; the
core must indeed be directed.

Every ordinary simple path that uses chords consists of an initial
tree segment, a sequence of chord and marked-subtree segments, and a
final tree segment. The interior sequence has an exact core
representation. The first and last chord endpoints are marks, so
source and exit offers are needed only at marks, even if the virtual
forest has other retained branching vertices.

## 2. The Dijkstra threshold has the right sign and converse

The tree queries give

```math
I_T(v)=\max_a\{\sigma_a-\bar L_T(a,v)\},\qquad
 O_T(v)=\max_b\{-\tau_b-\bar L_T(v,b)\}.
```

For A at least every source price, the artificial source length
`A-I_T(v)` is nonnegative. An exit at v is positive precisely when

```math
\mathrm{dist}(v)<A+O_T(v).
```

Indeed the corresponding score is
`I_T(s)-L_core(s,v)+O_T(v)`, for the chosen entry s. A positive
ordinary path gives a positive test because the offers can only
improve its two tree segments. Conversely a positive test gives a
represented directed walk with positive conservative endpoint score.

Zero-cost receiving arcs cause no difficulty: Dijkstra can retain a
simple predecessor tree by a fixed settled-order tie convention.
Any absent offer represented by minus infinity is omitted from the
artificial-source or exit list. In a settled spanning forest, a
component containing a chord incidence contains bins, but this
convention also makes the abstract query API cover isolated rows.

The best tree-only score is checked separately, so the k=0 case
does not require any core vertices.

## 3. The middle is simple, and two loop removals suffice

A simple core path expands to a simple ordinary path M. Repeated
vertices cannot hide inside a virtual edge because virtual interiors
are disjoint and contain no chord endpoint. This is stronger than a
mere bound on the number of represented pieces and is needed for
the following two-operation simplification.

Write A0 for the initial tree path a to the start s of M, and B0
for the final tree path from its end t to b. Choose z to be the last
vertex along M that lies on A0. Replace A0 followed by M by the
prefix of A0 ending at z and the suffix of M starting at z.
The removed segment is the directed closed walk z-to-s-to-z.
All its costs are nonnegative. The retained path Q is simple because
the remaining M suffix has no vertex on A0 after z.

Now choose y to be the last vertex along B0 that belongs to Q.
Keep Q only up to y and B0 from y onwards. This deletes another
directed closed walk y-to-t-to-y and leaves a simple a-to-b path.
Its score is at least that of the original represented walk.

Each last intersection is found by scanning O(k) represented pieces.
For a chord, only its endpoint vertices can intersect a tree path.
For two tree paths in the same T, projection of c onto T[a,b] is
at hop index

```math
[\mathrm{hop}(a,b)+\mathrm{hop}(a,c)
        -\mathrm{hop}(b,c)]/2.
```

The projections of the second path's endpoints delimit its
intersection when distinct. If they coincide at z, the intersection
is `{z}` exactly when z lies on the second path, tested by hop
distance additivity. These formulas also cover zero-edge paths.
Directional order is determined by the hop distance from the
relevant path's start. No long tree path is enumerated.

The physical source and target are preserved by both removals. A
positive result cannot reduce to a zero-edge a-to-a path because
the conservative source price is strictly below its same-bin exit
price.

## 4. Simultaneous coordinate changes and numerical history

After trimming, the represented pieces are physically edge-disjoint.
Apply the chosen eta with each piece's actual orientation, using
the forest watcher for tree coordinates and explicit scalar records
for chords. Every coordinate receives exactly one change.

Conservation is a statement about the complete transaction. A piece
may terminate at an internal row or bin, so no intermediate partially
updated state may be queried as if it were feasible. All guard checks
precede the commit; all pieces, endpoint slacks, register resets and
price notifications settle before the next query.

The accepted full path has positive conservative score and therefore
the same true one-sided margin as in the complete forest client.
The finite-grid step gives constant objective progress. Its total
negative allocation-log variation is bounded using the donor sum of
the entire simple path, rather than separately granting a constant
budget to every piece. Consequently the register count does not gain
a factor k. The minimum-slack argument and donor lower bound also
apply to this same path and exclude a static numerical-floor stall.

If the exact conservative query fails, there is no ordinary simple
path with true ratio above one half. In the sign-compatible comparison
circulation decomposition, a cycle that avoids the auxiliary slack
vertex has zero slack gain. A simple cycle through that vertex gives
an ordinary simple bin path. Thus full LOW follows on the graph with
chords; acyclicity of the ordinary graph was not used in this final
separation argument.

## 5. Work, structural changes and finite words

There are O(k) core arcs and offers, O(k) path-intersection queries,
and O(k) final piece updates per numerical step. The static
objective width gives `J=O(nu log S)`, and the unchanged register
bound gives `R=O(J+m log S)`. Initialization and native storage cost
`(m+nu) polylog S`, establishing the stated total.

When a tree edge is deleted, scanning all current chords finds a
replacement whenever the two new tree components remain connected
in the full graph. Only one replacement needs promotion. If none
exists, the ordinary graph itself has disconnected there. Each scan
costs `O(k polylog S)`. Coordinate ownership transfers with its
current value and persistent register; it is not a free register
reset. Endpoint reference counts change only constantly many mark
records per insertion, deletion or promotion.

The dynamic bound explicitly pays graph edits, externally changed
coordinates and slacks, and extra queries. It assumes the current
and intermediate feedback counts are bounded. It does not assume
that a numerical path is first installed into T through unpaid
basis pivots.

Core arc values are sums of polynomially bounded integer donor
prices over at most nu tree incidences. A simple core path has O(k)
arcs. Under the same master-size convention, their bit lengths are
O(log S). The original rounding count is applied to a hypothetical
simple strong path, or to the final trimmed path; it is never
incorrectly applied to an untrimmed repeated-edge walk.

The note's degree-three family has `4q+1` vertices, `5q` edges and
cycle rank q, and its alternating-chain plus cycle-perturbation
ledger preserves all row sums and bin loads. It therefore correctly
rules out using degree three alone to infer small k. General-graph
decomposition or pivot work remains a separate unresolved task.
