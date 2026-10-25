# Independent audit of certified layers without superposition

**Date:** 25 October 2026.  
**Status:** passed, including the stronger layer-birth counting argument.  
**Audited construction:** `certified_no_superpose_haxell_path_routing.md`.  
**Imported primitive:** `destructive_apsp_path_support_extractor.md`, separately
audited in `destructive_apsp_independent_audit.md`.

This is an independent argument check, rather than an invocation of an
approximate-half-layer theorem. I found no remaining gap in the fixed physical
certificate, alternating-layer, growth, termination, storage, or expander
reduction arguments. The input graph is static; all graph modifications made
while building a layer belong to that layer's temporary distance instance.

The important new counting fact is that the same algorithm also admits a bound
on the tree of layer births. This can improve the signature bound without
changing the sufficient strong-hitting assumption. The proof below is valid
for every finite execution prefix and therefore does not assume termination.

## 1. Exact scope of the statement

Let the physical resource set consist of the original edge identities of an
undirected unweighted graph. Parallel edges are separate resources. Demand
identities are distinct even when their endpoint pairs coincide. Equal-endpoint
demands are removed and satisfied by empty paths before the nontrivial
construction begins.

For the remaining demands, let the comparison family contain all simple paths
of length at most `h0`. Assume its transversal number obeys

\[
             \tau(E_S)\ge\Psi |S|\qquad(S\subseteq A).
\]

The distance primitive accepts paths only when its returned numerical value is
at most `Gamma h0`. It supplies a support with at most
`R=ceil(Gamma h0)` original edges, and a simple path within that support. A
failed query certifies the absence of an `h0`-short path in the current
temporary graph. The proof never needs an accepted query to be exact.

The hypothesis checked here is

\[
                 \Psi\ge\Delta R^2,\qquad\Delta\ge4.
\]

For nonempty `A`, taking a singleton demand in the strong-hitting condition
also gives `Psi <= m`. Consequently `Delta R^2 <= m`, in particular
`log Delta <= log N`. This useful boundary prevents spurious regimes in the
depth estimates. The case `A=empty` terminates immediately.

The output is a complete set of edge-disjoint simple demand paths of length
at most `R`. This is neither a maximum matching theorem for unrestricted
general graphs nor an unconditional disjoint-paths theorem without the
strong-hitting hypothesis.

## 2. The lifetime invariant really fixes the lower prefix

A layer `i` is removed only when it is the last layer and its own collapse
operation is executed. The algorithm does not discard an arbitrary suffix
without executing those collapses one layer at a time.

While layer `i` remains present, changing `Y_j` for any `j<i` would require a
collapse at level `j+1`. Before such a collapse can be performed, every higher
layer, including `i`, must already have been removed. Thus the lower prefix
`L_0,...,L_(i-1)` is fixed throughout layer `i`'s lifetime. This statement
includes the physical paths represented in the lower `Y_j`, not merely their
demand identities or cardinalities.

A collapse at `i+1` can remove paths from `Y_i`. It does not change `X_i` or
any lower layer. Hence, for one surviving instance of layer `i`:

* its active demand set at birth, `A(Y_(i-1))`, is fixed;
* its forbidden prefix `F0_i` is a fixed set of physical resources;
* its selected set `X_i` is fixed;
* its actual blocker set `Y_i` only shrinks;
* its full-counter identities `F_i` and physical certificate `C_i` stay fixed.

There is no mismatch between a certificate's birth-time active set and the
current active set needed by the growth proof. An old certificate for an active
set that has changed cannot survive that change.

## 3. Why changing the matching cannot add a lower blocker

At the birth of layer `t`, every edge in every lower `X_j` or `Y_j` is deleted
from the layer's temporary graph. Each path later inserted into the matching
by collapsing `t` is an element of this fixed `X_t`. It therefore avoids all
lower selected paths, including their complete original-edge representations.

The matching paths removed by this collapse belong to `Y_(t-1)`. They cannot
belong to another `Y_j`, because distinct layers have distinct matched demand
identities and the matching has only one path per demand. The newly inserted
paths are free of the entire current matching and pairwise edge-disjoint.
Removing the previous paths before insertion therefore preserves feasibility.

No newly inserted matching path can become a blocker of a lower `X_j`.
Updating `Y_(t-1)` by deleting the removed paths thus preserves the assertion
that every surviving `Y_j` is exactly the current blocker set of `X_j`.

This also proves the distinctness of demand identities between layers
inductively: a new `X_i` avoids every prior matched path `Y_j`, and so none of
its blockers can be one of those paths. An unmatched identity has no path in
the matching at all.

## 4. The certificate excludes initial deletions, but still covers blockers

There is one implicit detail worth making explicit. `C_i` counts only physical
edges deleted after the initial forbidden prefix `F0_i`; nevertheless the
proof uses

\[
                     B(X_i\cup Y_i)\subseteq C_i.
\]

This inclusion is valid. If a current matching path `Q` intersects an earlier
`X_j`, it belongs to the earlier blocker set `Y_j`, and all of `Q` has already
been removed in `F0_i`. If it intersects an earlier `Y_j`, edge-disjointness of
the matching implies that it is that same matching path, again wholly removed.
Thus any matching path with even one edge in `F0_i` is wholly removed from the
temporary graph. Such a path cannot touch a new accepted support.

Consequently every actual new blocker has all its edges outside `F0_i`, and
all of them are counted in `C_i` when that blocker is first touched. The same
observation applies to a matching path touched only by the support and not by
the extracted simple path.

For an accepted support `S`, at most `|S|` matching paths are touched because
the matching paths are edge-disjoint. Their union with `S` has size at most

\[
 |S|+(R-1)\,\#\{Q\in M:Q\cap S\ne\varnothing\}
                       \le R|S|\le R^2.
\]

Overlaps between successive deletion sets only help. Therefore
`|C_i| <= R^2 |X_i|`. The actual stored certificate has size at most `m`,
regardless of how large this numerical upper bound is.

For each active demand whose counter is not full, the rejected query proves
that every short path meets `F0_i union C_i`. All subsequent operations within
that build only delete more edges, so the assertion remains valid at the end.
Later matching changes do not alter this statement about fixed edges of the
static input graph. In particular, a retired matching path contributes its
old physical edges, not a mutable reference to a new path with the same
demand identity.

## 5. Independent recomputation of layer growth

Consider the creation of layer `ell+1`, and let

\[
 W=|Y_{\le\ell}|>0,
 \qquad T=\sum_{i=1}^{\ell+1}|X_i|.
\]

At a main-loop boundary, no old layer is collapsible. Since different selected
paths have disjoint blocker sets, this implies
`|Y_i| >= (9/10)|X_i|`. Under the contrary assumption
`|X_(ell+1)| <= Delta W/10`, it follows that

\[
                 T\le(\Delta/10+10/9)W.
\]

Remove all full-counter identities from the union of the active sets of these
layers. The remaining set `S_*` has size at least

\[
 |S_*|\ge W-T/\Delta
              \ge(9/10-10/(9\Delta))W.
\]

Every short path for one of these remaining identities meets its layer's
forbidden prefix or its certificate. Each earlier prefix edge lies in an
earlier certificate, by the inclusion proved above. Hence the union of all
`C_i` hits all short paths incident to `S_*` and has size at most `R^2 T`.

The strong-hitting lower bound is at least

\[
 R^2(9\Delta/10-10/9)W,
\]

whereas the certificate upper bound is at most

\[
 R^2(\Delta/10+10/9)W.
\]

The lower bound is strictly larger for every `Delta>=4`, since the coefficient
difference is `4 Delta/5 - 20/9 > 0`. Thus

\[
                  |X_{\ell+1}|>\Delta W/10.
\]

Because the lower prefix and `X_i` stay fixed for the lifetime of layer `i`,
this is a persistent growth inequality. The changing blocker set `Y_i` need
not remain equal to its value at birth.

## 6. Signature bound and terminal boundaries

At nonterminal main-loop boundaries, `Y_0` is nonempty and every positive
layer has both `X_i` and `Y_i` nonempty. The signature in the main note is
therefore well-defined. When `Y_0` becomes empty the algorithm terminates
before assigning another signature; no `log 0` convention is needed for it.
The formally empty `X_0` coordinate is assigned zero explicitly.

For the smallest collapsed level `t`, there are more than `|X_t|/10` free
selected paths, with at most `Delta` belonging to one demand. The swap removes
more than `|X_t|/(10 Delta)` distinct paths from `Y_(t-1)`, or unmatched tokens
from `Y_0` when `t=1`. Growth gives a reduction exceeding
`|Y_{<t}|/100`, and therefore exceeding one percent of `|Y_(t-1)|`.
All earlier signature coordinates and `X_(t-1)` are unchanged. The relevant
base-`1.01` logarithm decreases by at least one.

Without a collapse, the new finite pair precedes the old infinity sentinel,
again decreasing the signature. The absolute coordinates are nondecreasing:
the scale factor five dominates the within-layer `9/10` loss and the
between-layer `Delta/10 >= 2/5` factor.

All noncollapsible layers satisfy

\[
 |Y_i|>(9\Delta/100)|Y_{<i}|.
\]

Their demand identities are disjoint, so the depth is
`D=O(log N/log Delta)`. There may be one additional freshly built layer before
its collapse test. Since `log Delta <= log N`, this additive one is absorbed.
The signature is encoded by an integer partition of size
`O(D^2+D log N)`, giving

\[
       \#\text{builds}\le
       \exp O\left(\frac{\log N}{\sqrt{\log\Delta}}\right).
\]

The use of signatures and the associated partition bound follow the strategy
in BHHS Sections 5.4--5.5. The lifetime and certificate arguments above supply
the prerequisites for this changed algorithm; no superposition lemma is used.

## 7. Stronger count by the tree of layer births

This additional argument has also passed independent scrutiny.

Fix one positive-index layer instance `i`. Put

\[
                  P=|Y_{<i}|>0,
                  z=P+|Y_i|.
\]

The quantity `P` is fixed for that instance's lifetime. Every completed direct
child collapse, at level `i+1`, reduces `|Y_i|` by more than one percent of the
value of `z` immediately before that child's birth. The parent does not change
while the child survives, so this is also the value just before its collapse.
Consequently each such completed child reduces `z` by a factor less than
`0.99`.

At the parent's birth, each selected path has at most `R` actual blockers,
and each active demand has at most `Delta` selected paths. Thus

\[
 |Y_i|\le R|X_i|
       \le R\Delta |Y_{i-1}|
       \le R\Delta P,
 \qquad z\le(1+R\Delta)P.
\]

At every later time, `z>=P`. Therefore an instance has only
`O(log(1+R Delta))` completed direct children. In any finite execution prefix
there can be one additional child that is still alive. The total number of
children born so far is at most

\[
                    b=O(1+\log(1+R\Delta)).
\]

The artificial root represents the unmatched set `Y_0`. Each completed
level-one collapse shrinks this set by at least a factor `0.99`, unless it
empties it and terminates. Its number of child births in any execution prefix
is at most `b_0=O(1+log(q+1))`, again allowing the one currently live child.

Create a rooted tree with one node per born layer instance and an edge from
the layer that was last immediately before its birth. The depth bound proved
above applies to every execution prefix. Bounded depth and bounded branching
therefore give a uniform bound on the number of nodes ever born in that
prefix:

\[
 \log(1+\#\text{builds})
 =O\left(
      \log\log N+
      \frac{\log N}{\log\Delta}
           \log(2+\log R+\log\Delta)
    \right).
\]

This is not a circular termination argument. If an execution had not
terminated, another finite build would be possible while `Y_0` remained
nonempty. An arbitrarily long sequence would contradict the bound that
already holds for each of its finite prefixes.

Taking the better of this bound and the signature count is valid. Since
`R^2 Delta <= m <= N`, a convenient coarser statement is

\[
 \log(1+\#\text{builds})
 =O\left(
 \min\left\{
   \frac{U}{\sqrt{\log\Delta}},\;
   h+\frac{Uh}{\log\Delta}
 \right\}\right),
 \quad U=\log N,\quad h=\log(U+4).
\]

The count depends crucially on retaining a fixed `X_i` and deleting a layer
only through its own collapse. An implementation that discards an arbitrary
suffix without the intervening swaps would not inherit this proof.

### 7.1 A stronger weighted count removes rank entirely

The preceding uniform branching bound is valid but unnecessarily pays for
`log R`. The following refinement was derived independently during this audit
and agrees with a separately derived refinement of the main construction.

For each positive-index layer instance `i`, define its fixed prefix size

\[
                         P_i=|Y_{<i}|\in[1,q].
\]

When that layer creates a direct child, it is noncollapsible. Its persistent
growth inequality therefore implies

\[
 P_{\rm child}=P_i+|Y_i|
       >\left(1+\frac{9\Delta}{100}\right)P_i
       =\kappa P_i.
\]

If its direct children, in birth order, have prefix sizes `P_1,...,P_b`, then
the completed previous child's collapse gives

\[
                         P_{j+1}\le\rho P_j,
                         \qquad\rho=99/100.
\]

The last child may still be alive. That does not change either assertion.
For any `lambda>0`, read this geometric sequence backwards from its last
term to obtain

\[
 \sum_{j=1}^b P_j^{-\lambda}
       \le\frac{P_b^{-\lambda}}{1-\rho^\lambda}
       \le\frac{\kappa^{-\lambda}}{1-\rho^\lambda}
                        P_i^{-\lambda}.
\]

Put `s=log Delta` using natural logarithms, and choose

\[
                      \lambda=50\,\frac{\log(2+s)}s.
\]

This concrete constant suffices uniformly for all `Delta>=4`. Indeed
`log(1+0.09 Delta)>=s/5`: the difference is positive at `Delta=4` and its
derivative is positive thereafter. Thus
`kappa^lambda >= (2+s)^10`. If `lambda>=1`, then
`1-rho^lambda>=0.01`. If `lambda<1`, then
`1-rho^lambda>=0.005 lambda`. In both cases

\[
              \frac{\kappa^{-\lambda}}{1-\rho^\lambda}
                           \le\frac12.
\]

Give each layer node weight `P_i^(-lambda)`. For every nonroot node, the sum
of the weights of its already born direct children is at most half its own
weight. The artificial root's child prefix sizes are the successive positive
unmatched counts. They also decrease geometrically by factor at most `rho`,
and their last value is at least one. The total weight of those root children
is therefore at most `1/(1-rho^lambda)`.

For an arbitrary finite execution prefix, summing the parent-child inequality
over the finite birth tree gives

\[
 \sum_{\text{all born layers }i}P_i^{-\lambda}
                         \le\frac2{1-\rho^\lambda}.
\]

Every layer has `P_i<=q`, and hence weight at least `q^(-lambda)`. Therefore

\[
             \#\text{builds}
                  \le\frac{2q^\lambda}{1-\rho^\lambda}.
\]

Taking logarithms and using `s<=U=log N` absorbs the denominator into the
main term and yields

\[
 \boxed{\quad
        \#\text{builds}
          \le\exp O\left(
                    \frac{U\log(2+s)}s
                  \right),\qquad s=\log\Delta.
        \quad}
\]

For example, the denominator contributes only
`O(log(1+1/lambda))=O(log(2+s))`, while
`U log(2+s)/s >= log(2+s)`. There is no dependence on rank in this count.
It applies equally to the path construction, where rank is `R`, and the
explicit hypergraph construction, where rank is `r`.

The proof does not rely on the algorithm already having terminated. All its
inequalities apply to already born children in an arbitrary finite execution
prefix, including the currently live child and the last child that may fail
the growth test. The uniform node bound forces termination exactly as before.

This refined estimate improves the signature and coarse birth-tree estimates
up to absolute constants and may replace them in the theorem. For the
explicit hypergraph specialization it gives

\[
 O(|A|+|B|)+
 p\exp O\left(
       \frac{\log(p+4)\,\log(2+\log\Delta)}{\log\Delta}
         \right).
\]

In particular, `Delta >= (log p)^c` for fixed `c>0` gives overhead
`exp O(log p * log log log p / log log p)` with **no restriction on `r`**.
The earlier condition `r <= (log p)^{O(1)}` was needed only by the coarse
unweighted branching estimate and can be removed from that example.

## 8. Work and explicit storage

One build has at most `m` successful extractions: every accepted support
contains at least one fresh real edge. It has at most one rejection per active
demand. All deletions, including deletion of an entire touched matching path,
are charged to distinct physical edges. Initializing its fresh distance
instance and fresh seen registry is part of the imported per-build bound.

The selected paths in all currently surviving `X_i` are edge-disjoint across
layers, and `M` is separately edge-disjoint. Their total explicit length is
`O(m)`, with `O(q)` identity records. One full scan of these objects finds free
paths and updates the actual blockers in `O(m+q)` work per collapse.

An individual `C_i` is a subset of the `m` input resources, constructed from
actual deletion events. Storing all currently active certificates takes
`O(mD)` space. Their creation and deletion costs `O(m)` per build and collapse.
No `m R^2` materialization is required. There are no more collapses than
builds, since every collapse removes one previously born layer.

Thus the outer factor multiplies the certified per-build work, with no extra
path-length, rank, degree-cap, or number-of-demands multiplier.

For an explicitly represented bipartite hypergraph of resource-rank at most
`r`, the same proof works with an ordinary greedy edge scan. During a build,
eligibility only decreases: forbidden resources grow and counters increase.
Scanning each hyperedge once and marking its resource incidences therefore
costs `O(p+|A|+|B|)`, where `p` is total explicit incidence volume. Unused
isolated resources can be removed once. The same `r^2 |X|` fixed-certificate
bound and the stronger birth-tree count then apply. This is a mathematical
corollary of the construction, without a claim here to an exhausted public
literature comparison for that corollary.

### 8.1 The added certificate-or-routing alternative

The subsequently added growth test also passes this audit. Run the algorithm
without a hitting promise, but stop immediately after a newly built layer
fails `|X_new|>Delta |Y_prefix|/10`. All old layers have passed their tests,
and the same certificate calculation then supplies a nonempty `S_*` and a
physical set `C_*` such that

\[
       C_*\text{ hits every comparison path incident to }S_* ,
       \qquad |C_*|<\Delta R^2 |S_*|.
\]

This witnesses failure of the chosen strong-hitting condition. It does not
assert that a complete routing is impossible. If no test fails, the
depth and layer-birth arguments use only the tests that passed and still
force termination within the same running-time bound.

For nonempty `A` and `Delta R^2>m`, any singleton demand and all physical edges
already form such a witness. Since endpoints are distinct, every comparison
path is nonempty; if none exists, the hitting assertion is vacuous. This
handles the large-parameter regime without assuming the strong condition in
order to derive `log Delta<=log N`.

The graph certificate's hitting assertion is justified by the recorded failed
distance calls and the proof above. Fast independent verification of all
length-restricted paths is not silently assumed. In an explicitly listed
hypergraph, one scan of the edge list does verify the asserted transversal.

## 9. Independent check of the expander-to-hitting argument

Use original degrees throughout: `mu(v)=deg_G(v)` and `T=2m`. Suppose a set
`F` of `f<=phi T/64` physical edges is removed. Iteratively prune a nonempty
set of at most half the remaining original volume when its remaining cut has
size less than `(phi/4)` times its original volume.

For every partial removed union `P`, summing the cuts at their removal times
gives

\[
                  |\partial_G P|\le f+(\phi/4)\mu(P).
\]

As long as `mu(P)<=T/2`, original conductance implies
`mu(P)<=D0=4f/(3phi)`. At a first crossing of half volume, the new union has
volume at most `T/2+D0/2`, because the last pruned set had at most half the
remaining volume. Its complement then has volume at least `T/2-D0/2`.
Applying conductance to that complement and the preceding cut upper bound
forces

\[
 \phi(T/2-D0/2)
       \le f+(\phi/4)(T/2+D0/2),
 \qquad f\ge 9\phi T/44.
\]

This contradicts `f<=phi T/64`. Thus the process always retains a core and
removes original volume at most `4f/(3phi)`.

Within the surviving core, a breadth-first ball of at most half the surviving
original volume grows by a factor at least `1+phi/4`: the original degree
volume of the newly reached vertices dominates the number of boundary edges.
Every nonempty ball starts with volume at least one. Two balls of radius
`ceil(8 log(2m)/phi)` each have more than half the surviving original volume,
and hence intersect. The surviving diameter is at most the chosen
`h0=ceil(32 log(2N)/phi)`.

From a demand subset `A_*`, greedily select a vertex-disjoint subfamily of
`c>=|A_*|/(2k)` pairs. If a hitting set had
`f<phi delta |A_*|/(64k)`, then

\[
 f<\phi\delta c/32\le\phi T/64,
 \qquad |P|\le\mu(P)/\delta<c/24.
\]

Fewer than `c` deleted vertices cannot meet every one of the `c`
vertex-disjoint endpoint pairs. One pair survives wholly in the core and has
an `h0`-short simple path avoiding `F`, a contradiction. This proves

\[
                   \Psi=\phi\delta/(64k).
\]

All cut counts and degree volumes count parallel edge identities with their
multiplicity. No step requires a simple input graph. The pruning process is
only an existence argument and is never implemented, so it contributes no
algorithmic work.

Substitution into `Psi>=Delta R^2`, including the ceiling in `R`, yields the
stated sufficient condition

\[
        \phi^3\delta\ge Ck\Delta\Gamma^2\log^2 N
\]

for a sufficiently large absolute constant. Under this condition
`q<=nk/2<=m k/delta=O(m)`. Positive conductance and minimum degree permit the
dyadic lower-bound normalization in the main note; it keeps `h0` polynomially
bounded. No polynomial factor in `1/phi` is introduced into the build work.

## 10. Public reference and conclusion

The relevant primary source is Bucić, He, Huang, and Saranurak,
[*Disjoint Paths in Expanders in Deterministic Almost-Linear Time via
Hypergraph Perfect Matching*](https://arxiv.org/html/2511.02214v1), especially
Sections 3, 4.1, and 5.4--5.5. The source supplies the alternating-layer and
signature strategy and the expansion-to-hitting perspective. The present
audit verifies the changed fixed-certificate construction directly, and does
not use its approximate-half-layer reduction or a superposition interface.

**Conclusion.** The local destructive-support primitive and this outer
construction compose under the stated interfaces. The complete-path result,
the conductance dependence, the explicit inventory, and both iteration bounds
are supported by the proofs above. The stronger layer-birth bound is also
valid and may be used in the quantitative theorem. Any separate claim about
general-graph matching, dynamic low-recourse assignment, or optimal public
parameter baselines requires its own argument.
