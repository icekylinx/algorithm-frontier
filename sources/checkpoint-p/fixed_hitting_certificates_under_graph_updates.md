# Fixed path-hitting certificates under insertions and deletions

**Partial transfer lemma, 25 October 2026.** This note records a
positive persistence property of the physical certificates used in
the certified layer algorithm. It does not by itself give a fully
dynamic disjoint-path or hypergraph-matching algorithm.

## 1. A single historical path certificate

Let \(G_0\) be an undirected graph with permanent edge-lifetime
identities and positive lengths. Fix a set \(A_0\) of named demand
pairs, a comparison length \(h_0\), and a physical edge set \(C\)
which intersects every \(h_0\)-short path for every demand in \(A_0\).

Form a current graph \(G\) by deleting edges, increasing old edge
lengths, and inserting edge lifetimes. Let \(I\) contain every
inserted edge lifetime still relevant to this comparison; retaining
already deleted insertion identities in \(I\) is harmless.
Then

\[
                       C\cup I
\]

hits every current \(h_0\)-short path for every demand in \(A_0\).
Indeed, a current path that avoids \(I\) uses only old surviving
edges. Its length in \(G_0\) is at most its current length, so the
old hitting property applies. A path using an inserted edge is
already hit by \(I\).

A length decrease can be charged in exactly the same manner:
include the decreased edge identity in \(I\), or retire the old
lifetime and insert a new one. Endpoint retargeting must likewise
be represented as a new lifetime. This assertion is about fixed
demand endpoints; adding new demands does not make an old
certificate cover those new demands automatically.

## 2. One shared update set for many layers

Suppose several surviving layer certificates were built at different
times. Let \(I\) contain all edge insertions or decreases after the
oldest relevant birth. A certificate born later can also be enlarged
by this same \(I\); it merely contains some redundant identities.
Consequently the union certificate is

\[
                   C_{\rm all}\cup I,
       \qquad C_{\rm all}=\bigcup_i C_i,
\]

and its cardinality is bounded by
\(\sum_i|C_i|+|I|\). The insertion charge appears once, not once
per surviving layer.

The same observation holds in an explicit hypergraph. If newly
introduced hyperedges have a known hitting set \(J\), enlarge the
old certificates by \(J\). Picking one right resource from each
new nonempty hyperedge is a simple choice, although a smaller
shared \(J\) can be preferable. For implicitly represented path
hyperedges, one newly inserted graph edge hits every newly created
path that uses it; enumerating the new paths is unnecessary.

## 3. A quantitative growth margin

Use the notation of the no-superposition layer theorem:
\(\Delta\ge4\), selected rank at most \(R\), a fixed lower
prefix of total blocker count \(W>0\), and the strong condition

\[
                  \tau(E_S)\ge\Delta R^2|S|.
\]

Assume all the layer-state invariants still hold: old selected
objects are valid, exact blocker ownership is correct, lower
prefixes and active left sets retain their stated meanings, and
old layers are noncollapsible. These are separate requirements,
not consequences of the hitting lemma.

If a fresh build had \(|X_{\rm new}|\le\Delta W/10\), put
\(T=\sum_i|X_i|\), including this new layer. The existing growth
proof gives

\[
 T\le(\Delta/10+10/9)W,\qquad
 |S|\ge(9/10-10/(9\Delta))W.
\]

The updated union certificate has size at most \(R^2T+|I|\).
The difference between the promised lower bound and the old
certificate-size upper bound is at least

\[
 \Delta R^2|S|-R^2T
 \ \ge\
 R^2(4\Delta/5-20/9)W
 \ >\ \frac15\Delta R^2W
       \qquad(\Delta\ge4).
\]

Therefore the same strict growth contradiction remains valid
whenever

\[
                         |I|\le\frac15\Delta R^2W.
\]

In particular, a shared insertion budget of at most
\(\Delta R^2/5\) suffices at every nonterminal build boundary
with integer \(W\ge1\), provided the other stated invariants
are preserved. One can use a smaller constant to leave further
implementation margins.

## 4. What this lemma does and does not maintain

Inserting graph edges does not invalidate an already selected
path or change which current matching paths intersect it in
physical edge identities. Thus the certificate persistence
claim is compatible with those fixed objects. Deleting an edge
outside all selected and matched paths also leaves those objects
valid, while deletion only strengthens old path-hitting statements.

Deleting an edge used by a selected or matched path can invalidate
the layer state. A path-length increase can also violate a
previous output-length bound even though the hitting assertion
remains true. New demand arrivals can increase the root's
unmatched count. None of these events is paid for by the simple
certificate cardinality estimate above.

In particular, the static weighted lifetime proof assumes that
layers disappear through their own charged collapses and that
the root's unmatched count decreases. Arbitrary invalidation,
rollback, or new-demand insertion need not satisfy either
assumption. Reusing the static proof without charging these
events would be incorrect.

The present lemma isolates a useful positive interface: a large
implicit family of new paths can be covered by the small set
of graph edges that created them, with a single shared update
charge across all historical certificates. A dynamic algorithm
would additionally need a repair and discovery bound for
selected objects, matching recourse, and layer invalidations.
