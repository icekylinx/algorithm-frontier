# The same sharper rate for the existing BHHS explicit-hypergraph algorithm

**Baseline audit and new analysis, 25 October 2026.** The sharper
strong-Haxell running-time dependence in
`explicit_hypergraph_matching_branching_improvement.md` is not
exclusive to the no-superposition operation sequence. This note
shows that the existing explicit-hypergraph algorithm of BHHS also
admits that rate after a new analysis of its actual superposition
attempts. The distinction matters for novelty and baseline claims.

The published source is Bucić--He--Huang--Saranurak,
[*Disjoint Paths in Expanders in Deterministic Almost-Linear Time
via Hypergraph Perfect Matching*](https://arxiv.org/html/2511.02214v1),
SODA 2026. The source statements used below are Algorithm 1,
Algorithms 2--3, Proposition 5.6, and the growth conclusion of
Lemma 5.8. We give a historical-certificate proof of the growth
conclusion rather than relying on a potentially stale interpretation
of a hypothetical superpose rerun in Proposition 5.7.

## 1. Statement and exact status

Let `H=(A,B,E)` be an explicit `r`-bounded bipartite hypergraph,
let `p=sum_e |e|`, and assume

\[
 \tau(E_S)\ge\Delta r^2|S|
       \quad\text{for all }S\subseteq A,
       \qquad\Delta\ge4.
 \tag{1}
\]

Use the original BHHS operations with `mu=1/10`: extend a
layer greedily subject to its per-left cap `Delta`, collapse
only the last layer, and after a collapse attempt to extend the
parent. Adopt that extension only if its selected edge count
increases by a factor at least `1.1`.

These operations find a left-perfect matching in time

\[
 O(|A|+|B|)+
 p\exp O\!\left(
       \frac{\log(p+4)\log(2+\log\Delta)}{\log\Delta}
       \right).
 \tag{2}
\]

BHHS Theorem 1.5 displays the weaker rate
`p exp O(log(p+4)/sqrt(log Delta))`. Equation (2) is a
derivation in this research round, not a claimed quotation or
an already located published theorem. It shows that the faster
rate is also a new analysis of an existing public algorithm.
It must not be presented as an advantage exclusive to the new
no-superposition implementation.

## 2. Actual attempted extensions give persistent certificates

Fix a live positive-index layer `i`. Let its prefix through
`i-1` be the lower prefix. It remains fixed while layer `i`
survives. The current `X_i` can only grow through an adopted
superposition; `Y_i` can shrink only when its direct child
collapses, immediately followed by a fresh superposition attempt.
Other changes to the matching occur above the layer and cannot
create new blockers of its fixed selected edges.

For each layer retain, for analysis, the complete output
`(Xhat_i,Yhat_i)` of the latest actual extension attempt for
that layer. At its creation this is the original greedy build.
If an extension was adopted, `Xhat_i=X_i` just after adoption.
If it was rejected, the adoption rule gives

\[
                      |\widehat X_i|<1.1|X_i|.
 \tag{3}
\]

Until the next direct-child collapse and immediate new attempt,
the lower prefix, `X_i`, and `Y_i` are unchanged. The actual
matching outside those sets can change, but all right resources
in the recorded candidate remain fixed input vertices.

Let `F_i` be the active left vertices that reached degree
`Delta` in that recorded candidate, and let

\[
                  C_i=B(\widehat X_i\cup\widehat Y_i).
\]

The greedy build was maximal at the time it ran. Therefore every
input edge for an active vertex outside `F_i` meets the fixed
lower forbidden prefix or `C_i`. This assertion remains true
later, even if some recorded matching blockers are no longer in
the current matching. Also

\[
 |F_i|\le|\widehat X_i|/\Delta,
 \qquad B(X_i\cup Y_i)\subseteq C_i,
 \qquad |C_i|\le r^2|\widehat X_i|.
 \tag{4}
\]

The source's actual greedy extension uses residual degree
counters and respects the cap on the union. It is Algorithm 1,
not the differently formulated approximate extension interface
of Definition 5.9. No approximate half-layer assumption is used.

## 3. Recovering the public growth conclusion from those certificates

At a main-loop boundary all old layers are noncollapsible, so
`|Y_i|>=.9|X_i|`. Build layer `ell+1` and put
`W=|Y_(<=ell)|`. If its selected count were at most
`Delta W/10`, then, with the new layer using its own exact
candidate,

\[
 T=|X_{\ell+1}|+\sum_{i=1}^{\ell}|\widehat X_i|
      \le(\Delta/10+11/9)W.
 \tag{5}
\]

Remove all full-counter sets `F_i` from the active left
identities represented in `Y_(<=ell)`, and call the remainder
`S`. Their active sets are disjoint across layers, so

\[
 |S|\ge W-T/\Delta
       \ge(9/10-11/(9\Delta))W.
\]

The union of all recorded physical `C_i` hits every edge of
`E_S`. Earlier forbidden prefixes are already covered by
earlier certificates, using (4). Hence

\[
 \tau(E_S)\le r^2T
       \le r^2(\Delta/10+11/9)W.
\]

Assumption (1) gives the opposing lower bound
`r^2(9Delta/10-11/9)W`. It is strictly larger because
`4Delta/5>22/9` for every `Delta>=4`. Thus

\[
                    |X_i|>\Delta|Y_{<i}|/10
 \tag{6}
\]

at a layer's birth. Its lower prefix stays fixed while it
survives, and its selected edge count only grows, so (6)
persists. This proves the needed Lemma 5.8 conclusion directly
from actual historical builds.

The argument avoids asserting that a hypothetical new greedy
extension has the same size as a previously rejected extension
after the matching outside the layer has changed. Only the
physical hitting assertion from the actual old computation is
used.

## 4. Only constantly many adopted resets per layer

For one positive-index layer instance let `W=|Y_<i|`, fixed
through its lifetime. The degree cap gives

\[
 |X_i|\le\Delta|Y_{i-1}|\le\Delta W,
\]

whereas (6) gives an initial count exceeding `Delta W/10`.
Each adopted superposition increases `|X_i|` by at least the
factor `1.1`. Therefore fewer than `log_(1.1)(10)` such
adoptions can occur during that layer's lifetime. Using a safe
integer upper bound, its child sequence splits into at most
`J=26` epochs separated by adopted superpositions.

Within an epoch no selected edge is added to the parent. Each
direct-child collapse removes at least one percent of
`W+|Y_i|`; a rejected attempted extension changes neither
`X_i` nor the post-swap `Y_i`. Thus the fixed prefix sizes
of the children created within that epoch decrease geometrically
by a factor at most `rho=.99`.

At every child birth the parent is noncollapsible. By (6),

\[
 W_{child}\ge\kappa W,
 \qquad\kappa=1+9\Delta/100.
 \tag{7}
\]

An adopted extension can increase `Y_i` and break the geometric
sequence, but it causes only a new epoch. There are at most the
constant `J` such sequences, independent of `r`, `p`, and
`Delta`.

## 5. Weighted counting with a constant number of epochs

Put `s=log Delta` and
`lambda=C log(2+s)/s`, for a sufficiently large absolute
constant `C`. Weight a positive-index layer instance by
`W_i^(-lambda)`. In each epoch, (7) and the geometric
child-size sequence bound the child weights by

\[
 \frac{\kappa^{-\lambda}}{1-\rho^\lambda}
       W_i^{-\lambda}.
\]

Over all epochs the factor is at most
`J kappa^(-lambda)/(1-rho^lambda)`. Choose `C` large
enough that this is at most `1/2` for all `s>=log4`.
For example, `kappa>=Delta^(1/5)` and
`1-rho^lambda>=min{1/100,lambda/200}` make a uniform
constant choice immediate.

The root has no superposition operation. Its child prefix sizes
are the positive unmatched counts and decrease geometrically
after every completed child. Their weights sum to at most
`1/(1-rho^lambda)`. Summing the contraction over the tree
of layer instances in any finite execution prefix bounds total
weight by twice that quantity. Every node has weight at least
`|A|^(-lambda)`. There are at most

\[
                 2|A|^\lambda/(1-\rho^\lambda)
\]

created layers. As in the companion weighted proof, its
logarithm is `O(U log(2+s)/s)`, where `U=log(p+4)`.
This proves termination and the required build count without
assuming termination in advance.

## 6. Work and interpretation

An explicit greedy extension can be implemented by a single
input-edge scan. The forbidden right set only grows during
that scan, and degree counters only approach their caps.
Every current matching edge is scanned for marking at most
once. Thus an original build or a superposition attempt costs
`O(p)` after one-time removal of unused vertices. There is
at most one attempted superposition per collapse, and at most
one collapse per created layer. All scans and swap bookkeeping
therefore fit (2).

The historical sets in Section 2 may be regarded purely as
proof objects already produced by the actual computation.
Retaining them explicitly would cost `O(p)` per attempt and
`O(pD)` live storage, so even a certifying implementation does
not change the stated rate. A certifying variant would add an
explicit growth test; that extra outcome is not claimed to be
part of the unmodified public algorithm.

The new no-superposition algorithm is still useful: its selected
sets remain fixed outright, its certificate proof is shorter,
and it accepts the destructive approximate path-support oracle
without the public approximate-superposition interface. For
explicit hypergraphs, however, the strongest comparison now
includes this equally fast reanalysis of the existing public
operation sequence. The quantitative improvement is over the
published displayed analysis; it is not an exclusive speed
advantage of a different explicit-hypergraph algorithm.

### Conditional counting observation for approximate extensions

The bounded-reset counting argument itself needs only the birth
growth inequality, the per-left cap on the entire selected layer,
noncollapsibility at child births, the specified swaps, and
multiplicative growth at adopted resets. Therefore it would also
apply to an approximate-extension outer algorithm once these
invariants are validly established, for example if one has a
sound implementation and proof of the conclusion required in
BHHS Lemma 5.12. The number of adopted resets remains constant,
and the weighted iteration bound is unchanged.

This observation is not a proof of the public approximate
oracle interface. In particular it does not establish that a
full degree cap can be passed unchanged to an extension when
the old selected layer has already consumed part of that cap,
or that a comparison in the style of Proposition 5.11 persists
after unrelated changes to the matching. Historical physical
certificates must be justified for the actual approximate
implementation, or another valid growth proof must be supplied.
The completed explicit-hypergraph reanalysis above uses actual
maximal greedy extensions and does not depend on those unresolved
approximate-extension statements.
