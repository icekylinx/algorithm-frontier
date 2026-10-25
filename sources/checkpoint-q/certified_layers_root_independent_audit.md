# Root independent audit: physical certificates and layer lifetimes

**25 October 2026. Status: the constructive interfaces and the stronger
branching argument pass this audit.** This note independently checks
`destructive_apsp_path_support_extractor.md` and
`certified_no_superpose_haxell_path_routing.md`, including the proposed
explicit-hypergraph specialization. It is a mathematical review of the
research assembly, not an external certification or implementation.

The original general-graph maximum-matching bound is unchanged. The
new routing and hypergraph results have their own explicitly stated
length, density, or strong-Haxell assumptions.

## 1. What is new and what is imported

The distance data structure and arbitrary-forest lift are the named
research components from the current checkpoint. The alternating-layer
organization and the older signature count are drawn from BHHS,
[*Disjoint Paths in Expanders in Deterministic Almost-Linear Time via
Hypergraph Perfect Matching*](https://arxiv.org/html/2511.02214v1),
Sections 3 and 5. Their complete approximate-half-layer theorem is
not the black box being substituted into here.

The new bridge retains an actual set of original edge identities from
each successful query, and then consumes that entire set. The new outer
argument retains these identities as fixed hitting certificates, even
when the matching paths responsible for some of them later change.
This permits every layer's selected set to stay fixed during its
lifetime. The resulting tree of layer lifetimes has a smaller explicit
branching bound than the older generic signature argument alone.

## 2. The path representation really covers all numerical queries

A numerical APSP query can terminate inside a strict pivot ball at an
intermediate level. Its middle path therefore need not be a path of the
nearest-pivot forest. The extra all-source strict-ball trees are required,
in addition to the nearest-pivot forests and the exact base forests.

The pointwise copy bound for these trees follows from the **inverse
cluster** guarantee, not merely from the fact that each ball has few
vertices. Every internal vertex of a shortest path to a strict-ball
member remains in the same strict ball. Thus a vertex appears in at
most `|C(v,A)|+1` such trees. The retained center construction bounds
both balls and inverse clusters by `k polylog N`. Initial component
cases obey the same coarse bound.

A useful failed counterexample is a weighted tree with many small balls
all containing one central vertex. It refutes an inference from ball
size alone. It does not satisfy the center construction's inverse-cluster
bound and hence does not refute the present family. The proof correctly
uses the stronger contract. Nearest-pivot boundary legs are stored in
one shared nearest-pivot forest, rather than separately appended to every
strict-ball tree.

At equal distance a later-promoted center must not replace an older
center merely because of its identifier. Giving centers their immutable
birth priority ensures that an existing pivot changes only when a new
center is strictly nearer. The affected vertices then belong to the
old inverse cluster. Consistent internal shortest-path ties remain a
separate deterministic choice.

Local forest families are born once at their own levels and lifted
through their ancestors. Their aggregate recurrence is

\[
             G_j\le b_*+P(G_{j-1}+1),\qquad
             b_*=k^{O(1)}\operatorname{poly}(U).
\]

This is an additive local family term, not multiplication by `b_*`
at every level. It gives `G_j <= k^{O(1)} P^{O(j)} poly(U)`.
The coupled initialization/update accounting retains late initial
child credit; the larger local family changes the coefficient of
`x=log k`, not the number of multiplicative depth terms. Consequently
the logarithmic work envelope remains

\[
                B=O(x+f+Kg+d\log P+h).
\]

A returned descriptor has at most two pivot legs per level and one
terminating middle path, with current forest-local handles. It denotes
a genuine original walk of length no greater than the reported metric
estimate after all scale divisions.

## 3. Distinct-support extraction and its limits

Dynamic-tree aggregate weights equal one exactly on occurrences of an
original edge not yet consumed in the current oracle invocation.
Typed null edges and external incidence-tree connectors have weight
zero. On the first occurrence of an original identifier, marking all
of its registered occurrences prevents later repetitions of that
identifier from being read again. Every allocated occurrence is marked
at most once during its lifetime; a later occurrence inherits the
identifier's flag.

The full descriptor is consumed before graph topology changes. An
undirected search on the collected support produces a simple path.
Positive original lengths give

\[
 |S|\le\sum_{e\in S}\ell_e\le\operatorname{len}(W).
\]

Deleting **all** of `S`, including edges discarded by that search,
is essential. It yields `sum |S| <= m` across the invocation. The
procedure does not prove a final-output-sensitive ordinary path query
for an unchanged graph.

Each new outer layer build creates a fresh oracle invocation and fresh
seen registry. Earlier layers retain only their original-edge
certificates. Carrying seen flags across separate builds would be wrong,
because an edge consumed in one private subgraph can be needed in a
later private subgraph. The corrected notes make this explicit.

For an arbitrary half-layer state, a demand's own matched path is
excluded by temporarily removing one of its edges at a time. A failed
trial remains failed as the permanent base graph shrinks. All failures
sum to at most the total size of the disjoint matching paths, while
all successes consume a new edge. Materializing the successful support
before restoration is necessary because restoration can invalidate
forest handles. This gives `O(m+q)` edits and queries without a hidden
path-length multiplier.

The standalone half-layer approximation is `R+1`. Its sharper charge
uses singleton edges outside the matching and entire matched paths as
resource atoms. Each comparison half layer can meet one such atom in
at most one path. This proof remains valid with a vector of residual
per-demand quotas, although the new outer algorithm does not need
superpose calls at all.

## 4. Why actual blockers belong to the physical certificate

At the birth of a new layer the initial forbidden set is the union of
all earlier selected paths and their matching blockers. Suppose a
current matching path `Q` actually blocks a newly selected path but
also intersects that initial forbidden set.

If it intersects an earlier matching path, disjointness of the matching
implies it is that path and was entirely forbidden. If it intersects
an earlier selected path, exactness of the earlier blocker set again
puts all of `Q` into the forbidden set. Either alternative makes it
impossible for `Q` to block a newly selected path in the remaining
graph. Therefore every actual new blocker is outside the initial
forbidden set and is completely included in the newly stored
certificate. This supplies

\[
                       B(X_i\cup Y_i)\subseteq C_i
\]

even though `C_i` excludes initial forbidden deletions.

For one accepted support, deleting all matching paths it touches
costs at most `R |S| <= R^2` different edges in the size analysis.
The actual certificate is nevertheless a subset of the `m` original
edges. It is materialized in `O(m)` total work per build, not in
`O(m R^2)` work.

## 5. Certificate lifetime and matching changes

Only the last layer is collapsed. While layer `i` survives, no lower
prefix can change: changing layer `i-1` requires the prior collapse
and removal of layer `i`. The selected set `X_i` itself is fixed.
Its actual blocker set `Y_i` can only lose members.

A newly inserted matching path chosen from a deeper layer avoided all
lower selected paths at its birth. Those paths are still fixed, so the
new matched path cannot create a new blocker for a lower selected set.
Old blockers can disappear, but the physical edge identities that they
contributed to a certificate remain elements of the fixed input graph.
Thus the hitting certificate remains valid independently of later
matching ownership.

At level one, active demands are unmatched. At higher levels an active
demand's own matching path is in the forbidden prefix. Rejected queries
therefore certify that **all** short paths for an unsaturated active
demand hit the prefix or its newly consumed certificate, including the
own-path case. A generic arbitrary-state half-layer approximation
alone would not establish this stronger hitting statement.

## 6. The growth inequality and a constructive failure witness

Let `W=|Y_0|+...+|Y_ell|` before a new layer, and let
`T=sum_(i=1)^(ell+1) |X_i|`. Old layers are noncollapsible, so
`|Y_i| >= 9|X_i|/10`. If the new layer has at most `Delta W/10`
selected paths, then

\[
 T\le(\Delta/10+10/9)W.
\]

Remove all quota-full active identities. The remaining set `S_*`
has size at least

\[
             (9/10-10/(9\Delta))W>0.
\]

Every short hyperedge incident to `S_*` meets the union `C_*`
of the retained physical certificates. The forbidden prefixes are
covered by earlier certificates. Consequently

\[
 |C_*|\le R^2(\Delta/10+10/9)W
        <\Delta R^2|S_*|\qquad(\Delta\ge4).
\]

Under the strong-Haxell assumption this is a contradiction. Without
that assumption it is an explicit violation witness. The algorithm
can check the growth inequality at birth and return this pair if it
fails. It need not run forever on an input violating the promise.
The certificate rejects the stated strong-Haxell condition; it does
not assert that no perfect matching exists.

## 7. The stronger branching count has no termination circularity

For a surviving positive-index layer, write
`W=|Y_(<i)|`. This positive prefix count is fixed throughout its
lifetime. Initially,

\[
 |Y_i|\le R|X_i|\le R\Delta |Y_{i-1}|\le R\Delta W.
\]

A direct child that collapses has more than a tenth of its selected
paths free. The per-demand quota and the checked growth inequality
show that at least `(W+|Y_i|)/100` distinct matching identities are
removed from `Y_i`. The child's lower prefix has stayed fixed
throughout its own lifetime, so its birth inequality is still valid
at its collapse. Thus `z=W+|Y_i|` contracts by at least one percent
per completed child. Since `W <= z <= (1+R Delta)W` at the relevant
endpoints, there are at most `O(log(1+R Delta))` completed children.

In any finite execution prefix there can be one extra living child.
A parent cannot create a second living child or disappear through an
ancestor collapse while its first living child remains. The artificial
root has `O(log(q+1))+1` children, because each completed child reduces
the unmatched count by a constant fraction or empties it.

Depth is `O(1+log N/log Delta)` from the checked layer growth and
noncollapsibility. Every finite execution prefix therefore has a
uniformly bounded creation tree. This proves termination directly;
it does not first assume that every child will eventually return.
Writing `U=log N` and `s=log Delta`, the number of builds is at most

\[
 \exp O\left(\log(U+4)+
     \frac{U}{s}\log(2+\log R+s)\right).
\]

The older partition-signature proof is also valid after the
superpose case is removed. One may take the smaller of its
`exp O(U/sqrt(s))` bound and the branching bound. The finite
`Delta R^2 > |B|` case has an immediate singleton violation witness,
so the nontrivial range naturally has `s <= U`.

For an explicit `r`-bounded bipartite hypergraph, a greedy layer scan
reads each input hyperedge once and each touched matched hyperedge
once. Its cost is linear in explicit input volume. Replacing `R` by
`r` in the same argument gives the improved strong-Haxell parameter
dependence; no distance oracle is needed for this specialization.

### 7.1 Final refinement: a weighted count removes the rank term

The updated main notes replace the coarse branching estimate by a stronger
weighted argument. I checked this argument independently against the
actual collapse order.

Let \(W_i=|Y_{<i}|\) for a positive-index layer instance. Its prefix is
fixed while it lives. A child can be born only when the parent is
noncollapsible, so

\[
 W_{\mathrm{child}}\ge(1+0.09\Delta)W_i=\kappa W_i.
\]

Successive direct children have prefix sizes \(z_j\) satisfying
\(z_{j+1}\le0.99z_j\). This uses the child's birth growth inequality
at its eventual collapse, which is legitimate because that child's
lower prefix has not changed in the meantime. The last child in any
finite execution prefix may still be alive; the same inequalities
still include it.

For \(s=\log\Delta\) and
\(\lambda=100\log(2+s)/s\), assign weight \(W_i^{-\lambda}\).
The child weights increase geometrically in creation order. Summing
from the last child backwards bounds their sum by

\[
 \frac{\kappa^{-\lambda}}{1-0.99^\lambda}\,W_i^{-\lambda}
 \le\frac12W_i^{-\lambda}.
\]

Here \(\kappa\ge\Delta^{1/5}\) for \(\Delta\ge4\), and
\(1-0.99^\lambda\ge\min\{1/100,\lambda/200\}\). The root's
children have a total weight at most \(1/(1-0.99^\lambda)\).
The total weight of every finite layer forest is consequently at
most \(2/(1-0.99^\lambda)\). Every node weighs at least
\(q^{-\lambda}\), giving at most

\[
 \frac{2q^\lambda}{1-0.99^\lambda}
 =\exp O\!\left(\frac{U\log(2+s)}s\right)
\]

builds. The prefactor is absorbed since \(s\le U\). This argument
needs no upper bound on the parent's initial blocker count and
therefore has no additional rank or path-length term. It proves
termination through finite prefixes, without presuming that a
currently living child will eventually collapse.

For an explicit hypergraph, the linear-time build and the same
certificate alternative give
\(O(|A|+|B|)+p\exp O(U\log(2+\log\Delta)/\log\Delta)\).
I also checked the full explicit-input proof, including the immediate
certificate when \(\Delta r^2>|B_{\rm used}|\), isolated left vertices,
the linear verification procedure, and the separation of this promise
from unrestricted general-graph maximum matching.

## 8. The multigraph hitting lemma is self-contained

The revised routing note uses original graph volume
`mu(v)=deg_G(v)` and `T=2m`. After deleting `f<=phi T/64` edges,
repeatedly peel a smaller-volume set whose residual boundary is less
than `(phi/4)` times its original volume. For the accumulated peeled
set `P`,

\[
                  |\partial_G P|\le f+(\phi/4)\mu(P).
\]

As long as `mu(P)<=T/2`, conductance gives
`mu(P)<=4f/(3phi)`. At a first crossing of `T/2`, the smaller-side
rule gives `mu(P)<=T/2+2f/(3phi)`. Combining its complementary
conductance lower bound with the displayed upper bound would imply
`f>=9phi T/44`, contrary to the assumed `phi T/64`. Thus a crossing
never occurs.

The surviving graph has expansion at least `phi/4` relative to
original volume. Its BFS balls grow by a factor at least `1+phi/4`
until they exceed half of surviving volume, giving diameter
`O(log(m+2)/phi)`. This argument counts parallel edges correctly.
It avoids a potentially false replacement of `log m` by `log n`
in an unrestricted multigraph.

Choosing disjoint-endpoint demand pairs greedily, then applying the
volume bound to the peeled vertices, gives strong hitting parameter
`phi delta/(64k)` at comparison length `O(log N/phi)`. The
resulting sufficient routing condition is

\[
             \phi^3\delta\ge Ck\Delta\Gamma^2\log^2 N.
\]

The pruning construction is used only to prove a structural existence
statement; the algorithm does not enumerate sparse cuts. The explicit
algorithm is the certified layer procedure. Its work is charged by
actual consumed supports and does not gain an unmentioned polynomial
factor in `1/phi`.

## 9. Scope of the accepted conclusions

This audit accepts the destructive packing theorem on arbitrary
undirected positive-integer-length graphs, the certified routing theorem
under strong short-path hitting, the stated expander specialization,
and the explicit-hypergraph branching implication, relative to their
named metric/lifting interfaces where used.

The public BHHS theorem already gives qualitative deterministic
almost-linear routing and strong-Haxell hypergraph matching. The new
content is the explicit dependence, the physical-certificate outer
construction, and the stronger lifetime count. Priority relative to
every possible unpublished or retuned public construction has not been
established. Ordinary unrestricted path-reporting, fully dynamic
hypergraph recourse, and a better general-graph maximum-matching
exponent remain separate questions.
