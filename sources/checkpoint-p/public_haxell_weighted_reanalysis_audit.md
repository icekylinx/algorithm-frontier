# The weighted layer count also applies to the public BHHS algorithm

**Independent baseline audit, 25 October 2026.**  
**Status:** passed. The sharper explicit-hypergraph running-time dependence
must be treated as a derived public-algorithm baseline, rather than an
exclusive capability of the new no-superposition implementation.

Primary source: Bucić, He, Huang, and Saranurak,
[*Disjoint Paths in Expanders in Deterministic Almost-Linear Time via
Hypergraph Perfect Matching*](https://arxiv.org/html/2511.02214v1),
Algorithms 1--3 and Section 5.2. The source's printed iteration estimate is
weaker. This note supplies a new quantitative analysis of its existing exact
build-and-superpose algorithm. It does not assert that this sharper estimate
was stated in the source.

## 1. What has to be checked before comparing algorithms

The public exact algorithm builds layers greedily, swaps free selected
hyperedges into the matching, and removes only the currently last layer.
After that removal, it attempts a greedy extension of the new last layer.
It adopts this candidate only if the selected set grows by a factor at least
`1.1`. Otherwise it keeps the previous selected set and its updated blockers.
These are the operations used below.

Write `mu=1/10`, let the strong-Haxell assumption be

\[
                  \tau(E_S)\ge\Delta r^2|S|,
                  \qquad\Delta\ge4,
\]

and let `q=|A|`. The important question is whether successful superpositions
can destroy the weighted layer-birth argument. They can increase the current
blocker count, but the number of such increases in one layer's lifetime is
bounded by an absolute constant.

There is a second issue: a hypothetical greedy extension recomputed against
the current matching need not be the same object as an extension considered
earlier. Historical physical certificates give a direct growth proof that
does not require this identification.

## 2. A positive-index layer has a fixed lower prefix

For one instance of layer `i`, put

\[
                     W_i=|Y_{<i}|.
\]

Its complete lower prefix is fixed until the instance is discarded. To alter
`Y_j` for `j<i`, the public algorithm must collapse layer `j+1`. Because it
only collapses the current last layer, layer `i` must already have disappeared
before this can occur.

A superposition affecting layer `i` is attempted only immediately after its
direct child has been discarded. It changes neither the lower prefix nor the
active left-vertex set `A(Y_(i-1))`. At all times within the lifetime,

\[
                    |X_i|\le\Delta |Y_{i-1}|
                           \le\Delta W_i.
\]

The selected set `X_i` never shrinks. A failed extension leaves it unchanged;
an adopted extension adds hyperedges. All its hyperedges remain outside the
matching until the instance's own collapse.

The matching changes made by a higher collapse cannot create new blockers of
an older selected set: the inserted hyperedges avoid the entire lower prefix
in their right coordinates. In particular, between successful superpositions,
`Y_i` only decreases through direct-child swaps.

## 3. Historical greedy candidates supply the needed growth proof

For each surviving layer, retain conceptually the latest candidate produced
by an actual greedy build or attempted superposition. Call it
`(Xhat_i,Yhat_i)`. This is an analytical historical object; the original
promise algorithm need not store it after a failed attempt.

If the candidate was adopted, `Xhat_i=X_i` at that time. Otherwise it failed
the adoption test. Consequently, before the next attempt at this same layer,

\[
                 |\widehat X_i|\le1.1|X_i|.
\]

Record the fixed physical resource set

\[
                     C_i=B(\widehat X_i\cup\widehat Y_i),
\]

and the set `F_i` of active left identities whose candidate counter equals
`Delta`. The candidate is a valid greedy maximal layer, so

\[
 |F_i|\le|\widehat X_i|/\Delta,
 \qquad |C_i|\le r^2|\widehat X_i|,
 \qquad B(X_i\cup Y_i)\subseteq C_i.
\]

Every input hyperedge of an active identity outside `F_i` meets the lower
physical prefix or `C_i`. This statement remains true even if a matching
hyperedge used to define `C_i` later leaves the matching. It concerns the old
resource identities. The lower prefix is fixed, so no reinterpretation is
needed.

On a direct-child collapse, the algorithm immediately attempts a new
superposition and this history record is replaced by the resulting candidate,
whether adopted or rejected. Between such attempts, the current `X_i,Y_i`
continue to be covered. Thus there is no gap between a matching change at the
parent and its next certificate.

Now consider a fresh layer `ell+1`. Let

\[
 W=|Y_{\le\ell}|>0,
 \qquad T_{\rm hist}=|X_{\ell+1}|
                    +\sum_{i=1}^{\ell}|\widehat X_i|.
\]

Assume for contradiction that `|X_(ell+1)|<=Delta W/10`. The old layers are
noncollapsible, hence `|X_i|<=10|Y_i|/9`. Therefore

\[
                    T_{\rm hist}
                           \le(\Delta/10+11/9)W.
\]

Remove the full-counter sets from the union of the active identities. The
remaining set `S` has size at least

\[
              |S|\ge W-T_{\rm hist}/\Delta
                        \ge(9/10-11/(9\Delta))W.
\]

The union of historical resource certificates hits every hyperedge incident
to `S`: earlier prefix resources are covered by earlier certificates. Its
size is at most `r^2 T_hist`. Strong Haxell instead gives a lower bound of

\[
                    r^2(9\Delta/10-11/9)W.
\]

The difference between this lower coefficient and the upper coefficient is

\[
                       4\Delta/5-22/9>0
                         \qquad(\Delta\ge4).
\]

This contradiction proves the desired birth inequality

\[
                       |X_i|>\Delta W_i/10.
\]

It persists thereafter: `X_i` can only grow and `W_i` is fixed. This argument
uses candidates actually produced by the public algorithm, rather than an
unperformed re-evaluation of maximality in a changed matching state. It is
enough for the following runtime analysis without changing the algorithm's
operations.

## 4. Only constantly many superposition epochs are possible

At birth, `|X_i|>Delta W_i/10`; throughout its lifetime,
`|X_i|<=Delta W_i`. Every adopted superposition multiplies `|X_i|` by at least
`1.1`. Since `1.1^25>10`, there can be at most 24 such adoptions.

For convenience, use the looser bound of at most 26 epochs, where an epoch
begins at the layer's birth or after an adopted superposition. In an epoch,
`X_i` is fixed. A failed superposition computes a candidate but does not
commit any of its new selected hyperedges or blockers. It does not alter the
matching either. Hence it cannot reset the current blocker count upward.

A child whose collapse triggers a successful superposition is assigned to
the epoch in which that child was born. Its successor, if any, belongs to the
new epoch. This convention makes the needed monotonicity exact.

## 5. Weighted children contract after absorbing the constant epoch count

At each direct child's birth, the parent is noncollapsible. Thus

\[
  W_{\rm child}=W_i+|Y_i|
       >\left(1+\frac{9\Delta}{100}\right)W_i
       =\kappa W_i.
\]

Within a fixed epoch, direct-child birth values decrease by a factor at most
`rho=0.99` between consecutive births. The intervening child collapse removes
at least a one-percent fraction of `W_i+|Y_i|`, by its persistent growth
inequality and the degree cap `Delta`.

For any positive `lambda`, the sum of the weights `W_child^(-lambda)` of
children in one epoch is at most

\[
                \frac{\kappa^{-\lambda}}{1-\rho^\lambda}
                            W_i^{-\lambda}.
\]

Summing over at most 26 epochs multiplies this expression only by an absolute
constant. With `s=log Delta`, choose

\[
                   \lambda=C\frac{\log(2+s)}s
\]

for a sufficiently large absolute constant `C`. Since
`log kappa>=s/5` for `Delta>=4`, this ensures

\[
                  26\frac{\kappa^{-\lambda}}{1-\rho^\lambda}
                               \le\frac12.
\]

The root has no superposition. Its successive child birth values are the
positive unmatched counts, again decreasing geometrically. Their total
weight is at most `1/(1-rho^lambda)`.

Now apply these inequalities to any finite tree of already born layer
instances, allowing the last direct child of each epoch to remain alive.
The total nonroot node weight is at most `2/(1-rho^lambda)`. Each node has
`W_i<=q`, hence weight at least `q^(-lambda)`. Therefore

\[
 \#\text{fresh builds}
       \le\frac{2q^\lambda}{1-\rho^\lambda}
       =\exp O\left(
            \frac{U\log(2+s)}s
                   \right),
 \quad U=\log(p+4),\quad s=\log\Delta.
\]

As usual, isolated left vertices violate the promise immediately, unused
right vertices can be removed once, and a nonempty promised instance has
`Delta r^2<=|B_used|<=p`. Thus `s<=U`, which absorbs the displayed denominator
into the exponent. The finite-prefix proof does not assume prior termination.

## 6. Work and baseline classification

On an explicitly listed hypergraph, each exact greedy build or attempted
superposition costs `O(p)` using monotone forbidden flags and left counters.
A matching hyperedge is scanned at most once during one such call. Every
superposition attempt follows a layer collapse, and each collapse removes a
previously born layer. Hence the number of attempted superpositions is no
greater than the number of fresh builds. Ordinary swap and layer bookkeeping
also fit `O(p)` per such event.

The existing public exact algorithm therefore admits the derived bound

\[
 \boxed{\quad
 O(|A|+|B|)+p\exp O\left(
       \frac{\log(p+4)\log(2+\log\Delta)}{\log\Delta}
                         \right)
 \quad}
\]

under the same strong-Haxell promise. In particular, the polylogarithmic
overhead when `Delta>=p^epsilon` and the rank-independent improvement when
`Delta` is a power of `log p` are not exclusive advantages of the
no-superposition algorithm.

The new fixed-certificate implementation remains a valid simpler algorithm,
and its routing-or-hitting-witness interface is separately useful. More
substantively, its destructive approximate-distance build can supply short
path certificates without implementing the public superposition oracle.
Those interface advantages must be stated separately from the public
algorithm's newly derived iteration rate.

**Conclusion:** adopt the boxed rate as an optimized, reconstructed public
explicit-hypergraph baseline. Credit the sharper proof as a present
reanalysis, but do not label it a strict algorithmic improvement over that
public framework.
