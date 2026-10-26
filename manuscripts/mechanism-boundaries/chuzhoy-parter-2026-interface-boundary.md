# The Chuzhoy–Parter 2026 spanner interface and the ambient-route boundary

**Scoped source comparison, 24 October 2026.** This note concerns
[Chuzhoy–Parter, arXiv:2601.20718v1](https://arxiv.org/html/2601.20718v1),
especially Theorem 1.3 and Section 9.1. It supplies no new matching
exponent and is not a dependency of the current 4/5 construction.

## 1. The exported object

Theorem 1.3 maintains a deterministic subgraph on a fixed vertex set,
initially with no edges and remaining simple, under at most n^2 edge
updates. Its parameter range is

$$
512\le k\le(\log n)^{1/49},\qquad
1/k\le\delta<1/400,\qquad \Delta\ge n^{20/k}.
$$

Corollary 9.6 adds length buckets and states

$$
\begin{aligned}
|E(H)|&\le n^{1+O(1/k)}\Delta(1+\log L),\\
d&=k^{19}2^{O(\delta^{-6})},\\
\eta&\le n^{O(1/k)}\max\{\Delta_{\max}(G)/\Delta,1\}.
\end{aligned}
$$

Here eta is NATIVE EDGE congestion. Update time is n^{O(delta)};
selected-edge recourse is n^{O(1/k)}. The embedding in Lemma 9.4 is
existential, proved by fractional routing and randomized rounding.
No path-reporting or demand-route notification contract accompanies
Corollary 9.6. This is consistent with deterministic maintenance of H.
The harmless 1+log L convention counts the single unit-length bucket.

Section 2.8's vertex splitting is a static incidence-moving operation,
costing the number moved. The explicit output-sensitive path query in
Theorem 2.8 applies to a special decremental well-connected support
graph. It is not a query interface for H.

## 2. What native congestion implies after an ambient lift

The distinction above has an exact mathematical consequence. Suppose
J is a projected graph, each of whose genuine edges e has an explicit
ambient walk pi(e). Define its ambient occurrence load at z by

$$
C_0(z)=\sum_{e\in E(J)}\mathrm{occ}_z(\pi(e)),
 \qquad C_0=\max_z C_0(z).
$$

Suppose a chosen subgraph H is equipped with paths Q(e) routing all
J edges and having native edge congestion at most eta. Composing walks
gives only

$$
\begin{aligned}
 C_{\rm comp}(z)
 &\le\sum_{f\in E(H)}
       \#\{e:f\in Q(e)\}\mathrm{occ}_z(\pi(f))\\
 &\le\eta\sum_{f\in E(H)}\mathrm{occ}_z(\pi(f))
 \le\eta C_0(z).
\end{aligned}                                                    \tag{1}
$$

Repeated route occurrences are counted with multiplicity. Loop erasure
can only decrease this upper bound; it does not establish a smaller
general bound automatically.

Substituting the source's eta into (1) gives a product involving
Delta_max(J), C_0, and the density parameter Delta. It does not give the
current static primitive's additive form

$$
\Gamma\bigl(C_0+\Delta_{\max}(J)\bigr)
                                                               \tag{2}
$$

at its stated sparse-support size. Setting Delta at least the entire
native maximum degree removes one multiplier from (1), but also raises
the support allowance to n Delta times its subpolynomial factor.
That is a different size/congestion tradeoff. There is no contradiction:
the current ambient primitive makes choices using ambient resources,
whereas (1) is the generic conclusion from a native routing certificate.

The explicit congested-greedy examples elsewhere in these notes show
why cancellation is not a substitute for such a proof. They do not
refute the existence of better ambient-aware choices in the present
paper's subgraph.

## 3. Exact missing algorithmic operations

Even if (2) were proved separately, three executable interfaces would
still need construction.

* A deterministic path-producing procedure must be attached to the
  current selected H. A conditional-expectation rounding lemma applies
  only after the candidate flows or finite path distributions have
  actually been produced and represented within the work bound.
* A native split must move its partition of old input IDs while charging
  selected endpoint changes and invalidated route records. Replacing a
  split of s incidences by s edge deletions and insertions spends s input
  updates. That is precisely the multiplier the current recursive
  sparsifier avoids.
* A correction-cycle owner needs to learn which of its routes changed,
  even when H itself did not change. A bound on selected-edge recourse
  alone supplies no list of those owners.

These requirements concern the intended application, not the validity
of maintaining a subgraph possessing the stated existential property.
They are not supplied by the occurrence of the word “split” in an
internal static construction or by an unrelated support-graph query.

## 4. The stated parameter envelope gives no quantitative improvement

Put u=log n. The positive expressions entering the published bounds
include delta u and u/k. Throughout their permitted parameter range,

$$
u/k\ge u^{48/49},\qquad
                   \delta u\ge u/k.                           \tag{3}
$$

Consequently optimizing THESE GUARANTEED EXPRESSIONS cannot certify
an overhead exp(O(u^(4/5) polylog u)), even before paying for any missing
interface above. Equation (3) is not a lower bound on the algorithm's
actual runtime or on what a different reconstruction might achieve.

The special nice-router algorithm in Section 4 is constructive, but
requires its prescribed router rather than an arbitrary input graph.
Its demand-call cost includes an extra router-side power, and using it
here would still require a new embedding, update, and ambient-resource
analysis. The source's explicit support-graph path routine likewise
retains its own parameter restrictions. No stronger tradeoff follows
by substituting either name for the current primitive.

The useful conclusion is therefore precise: this paper offers a
different deterministic maintained subgraph with strong routing
properties, but its stated Section 9.1 interface neither replaces the
current ambient-route module nor improves the current guaranteed
quantitative envelope.
