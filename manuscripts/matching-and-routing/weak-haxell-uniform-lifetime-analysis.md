# A uniform parameter analysis of the public weak-Haxell algorithm

**Research reanalysis, 25 October 2026. Historical-certificate and
birth-growth prerequisites audited in the current-blocker proof.**

This note finishes the proposed transfer of the weighted lifetime-tree
count to Annamalai's weak-Haxell augmenting algorithm. It also gives a
shorter, length-aware count of the original signature vectors yielding
the same quantitative rate. Thus the rate is a **public-algorithm
reanalysis**, not an advantage exclusive to a new operation sequence.
It is not a general-graph maximum-matching result.

The primary source is Annamalai,
[*Finding Perfect Matchings in Bipartite Hypergraphs*,
arXiv:1509.07007v2](https://arxiv.org/html/1509.07007v2),
Sections 2--5; the [official history](https://arxiv.org/abs/1509.07007)
lists v2 as its latest version. Theorem 1.3 is polynomial for fixed
rank and slack, and Theorem 5.4 already has a certifying alternative.
The source does not display the uniform bound proved below.

## 1. Statement and conventions

An `r`-uniform bipartite hypergraph has one left vertex and `r-1`
right resources in each edge. Here `r` is the **whole-edge** size;
it differs by one from the right-rank convention in the strong-Haxell
notes. Let `n=|A|`, let `p=sum_e |e|` be the explicit incidence
volume, and let `P=p+|A|+|B|+2`. Fix rational `0<epsilon<1` and
integer `r>=2`. Write `b_epsilon` for the bit length of that rational.

The algorithm described below returns either a matching covering `A`,
or a nonempty `S subset A` and an explicit `C subset B` such that

$$
C\cap e\ne\varnothing\quad\text{for every }e\in E_S,
 \qquad |C|\le(2r-3+\epsilon)(|S|-1).                   \tag{1}
$$

Its uniform running-time upper bound is

$$
P\,(n+1)^{\,O((r^2/\epsilon)\log(2+r/\epsilon))}
       \operatorname{poly}(b_\epsilon+\log P).          \tag{2}
$$

In particular, it finds a perfect matching under the promise

$$
\tau(E_S)>(2r-3+\epsilon)(|S|-1)
                      \quad\text{for all nonempty }S\subseteq A.
                                                               \tag{3}
$$

The certificate (1) violates this sufficient condition. It need not
certify that no perfect matching exists. The algorithm never tests
(3) by enumerating subsets. Unused resources may be removed after
their input lists are read. Empty left sets and isolated left vertices
are handled directly.

## 2. Public operations and the one indexing convention

Use the source's parameters

$$
\mu=\epsilon^2/(10r^2),\quad Q=\lceil1/\mu\rceil,
 \quad\delta=\epsilon/(5r^2).                           \tag{4}
$$

Start one augmenting call from a single unmatched left root. A layer
is a set `X_i` of pairwise right-disjoint nonmatching edges and their
current matching blockers `Y_i`; each blocker meets exactly one
selected edge. Different layers have disjoint right supports. The
dummy layer has `Y_0={root}` and empty right support.

Greedily build the next layer from left vertices of the last blocker
layer, avoiding the lower forbidden right support, with at most `Q`
selected edges per active left vertex. Collapse only the last layer,
and only when more than a `mu` fraction of its selected edges are
unblocked. Swap at most one such edge per active left identity, discard
that last layer, and try a greedy extension of its parent. Adopt the
extension only if its selected count grows by at least `1+mu`.

When extending layer `i`, the lower-prefix argument to the greedy
routine is the prefix **strictly below** `i`; the current `(X_i,Y_i)`
is supplied as its initial candidate. This makes explicit the intended
active set `A(Y_(i-1))` in the source's abbreviated superposition
notation. It does not add a different operation to the algorithm.

At every main-loop boundary all surviving positive layers are
noncollapsible, so

$$
|Y_i|\ge(1-\mu)|X_i|.                 \tag{5}
$$

The source's matching and alternating-tree invariants prove this
without a growth assumption. The new certifying version checks the
birth-growth inequality in Section 4 after each build and stops with
(1) if it fails.

## 3. Historical certificates avoid a hypothetical future rerun

For a live layer `i`, retain the result `(Xhat_i,Yhat_i)` of its
most recent **actual** greedy attempt. At birth this is the initial
build. After an adopted extension it is the current layer. After a
rejected extension,

$$
\widehat X_i=X_i\mathbin{\dot\cup}E_i,
                  |E_i|<\mu|X_i|.                     \tag{6}
$$

Until the next direct-child collapse, the lower prefix, `X_i`, and
the blockers `Y_i` of `X_i` remain fixed. Higher matching swaps use
edges avoiding this prefix and cannot create or remove its blockers.
A direct-child collapse immediately triggers a new actual attempt.
Consequently the recorded candidate always contains the support of
the current layer. Its extra resources, even if their old matching
owners later retire, can be kept as fixed physical ghost resources.

Let `F_i` be the active left identities that have reached cap `Q`
in the recorded candidate, and set

$$
C_i=B(\widehat X_i\cup\widehat Y_i).
$$

Greedy maximality gives a persistent statement: every input edge
for an active identity outside `F_i` meets the lower forbidden prefix
or `C_i`. These are fixed resource sets, so later changes of the
matching outside the layer do not invalidate that statement. Moreover,

$$
|F_i|\le|\widehat X_i|/Q,\qquad
 B(X_i\cup Y_i)\subseteq C_i,
 \qquad
 |C_i\setminus B(X_i\cup Y_i)|\le(r-1)^2|E_i|.          \tag{7}
$$

For the last estimate, one newly selected edge has `r-1` resources,
and each of its at most `r-1` blockers contributes at most `r-2`
additional resources. Repeated resources only reduce the union.

This also covers edges that were themselves in the matching when
the attempt ran. For a non-root active left vertex, its own matching
edge lies in the lower prefix and already meets the forbidden set.
The root was unmatched. Hence the certificate hits all incident
hyperedges, not merely the then-unmatched edges.

The argument does not assert that rerunning greedy under a later
matching returns the same candidate. Only the certificate produced
by the actual old computation is reused.

## 4. Birth growth, with an explicit certificate if it fails

At a main-loop boundary let

$$
q=|Y_{\le\ell}|=1+\sum_{i=1}^{\ell}|Y_i|,
 \qquad X_{old}=\sum_{i=1}^{\ell}|X_i|.
$$

By (5), `X_old <= (q-1)/(1-mu)`. Build layer `ell+1`, and
suppose

$$
|X_{new}|\le\delta q.          \tag{8}
$$

Use its actual output as its candidate. Remove the union of all
candidate-full sets `F_i` from the `q` active left identities, and
call the remainder `S`. The active sets of distinct layers are
disjoint. Let `C` be the union of all the recorded `C_i`, including
the new one. Each lower forbidden prefix is contained in earlier
candidate supports, so (7) proves that `C` hits all of `E_S`.

Put `T=sum_(old i)|Xhat_i|+|X_new|`. Then

$$
T\le\frac{1+\mu}{1-\mu}(q-1)+\delta q,
 \qquad |S|\ge q-T/Q.                                  \tag{9}
$$

The current old layers have a sharper right-support bound than the
rank-squared estimate. A blocked selected edge with `b>=1` matching
blockers uses at most `(r-1)+(r-2)b <= (2r-3)b` resources. Each
blocker belongs to exactly one selected edge. Immediately addable
old selected edges number at most `mu X_old`. Combining this count,
the new layer, and the historical extras yields

$$
|C|\le(2r-3)(q-1)
       +\frac{\mu r(r-1)}{1-\mu}(q-1)
       +\delta(r-1)^2q.                                 \tag{10}
$$

### 4.1 Small prefixes

If `q<1/delta`, (8) forces `X_new` to be empty. Also

$$
\mu X_{old}<\frac{\mu}{\delta(1-\mu)}
            =\frac{\epsilon}{2(1-\mu)}<1.
$$

Integer counts therefore force every old immediately addable set
and every historical extra set to be empty. No candidate has `Q`
selected edges. Thus `S` consists of all `q` active identities and
`|C| <= (2r-3)(q-1)`, proving (1). This includes `q=1`, where
the certificate is a single isolated left vertex and the empty set.

### 4.2 Large prefixes

Suppose `q>=1/delta`. Since `mu<=1/40` and `delta<=1/20`,

$$
\frac{T/Q}{q-1}
 \le\mu\left(\frac{1+\mu}{1-\mu}
                  +\frac{\delta}{1-\delta}\right)
 \le\frac{10}{9}\mu.                                   \tag{11}
$$

In particular `S` is nonempty. Subtract the upper bound (10) from
`(2r-3+epsilon)(|S|-1)`, using (9)--(11). Divided by `q-1`,
the difference is at least

$$
\epsilon-
 \left[
  (2r-3+\epsilon)\frac{10}{9}\mu
  +\frac{\mu r(r-1)}{1-\mu}
  +\frac{\delta(r-1)^2}{1-\delta}
 \right].                                               \tag{12}
$$

The three bracketed terms, divided by `epsilon`, are at most
`1/18`, `4/39`, and `4/19`, respectively. Their sum is less
than `2/5`. For the first term use `2r-3+epsilon<=2(r-1)`
and `(r-1)/r^2<=1/4`. Hence (12) is positive, proving (1)
again.

Under promise (3), neither case can occur. Therefore each successful
birth satisfies

$$
|X_i|>\delta|Y_{<i}|.             \tag{13}
$$

The lower prefix remains fixed while layer `i` is alive, and `X_i`
only grows. Thus (13) continues to hold throughout its lifetime.

## 5. A uniform weighted lifetime-tree count

Fix one augmenting call. For a positive-index layer instance set
`W_i=|Y_<i|`; it is fixed during that instance's lifetime. At birth,
`|X_i|>delta W_i`, whereas always

$$
|X_i|\le Q|Y_{i-1}|\le QW_i.
$$

Each adopted superposition multiplies `|X_i|` by at least `1+mu`.
There are therefore at most

$$
J=1+O\bigl(\mu^{-1}\log(Q/\delta)\bigr)                \tag{14}
$$

epochs of direct children with no adopted superposition between
them. A rejected attempt changes neither the selected parent edges
nor its post-collapse matching blockers.

Collapsing a direct child swaps more than `mu|X_child|/Q` distinct
left identities. Thus within one epoch the prefix sizes at successive
child births decrease by at least a factor `1-tau`, where

$$
\tau=\mu\delta/Q,
 \qquad\tau\ge\frac{\mu^2\delta}{2}
                   =\frac{\epsilon^5}{1000r^6}.         \tag{15}
$$

At a child birth the parent is noncollapsible, so (5) and (13) give

$$
W_{child}\ge\kappa W_i,
                \qquad\kappa=1+(1-\mu)\delta.          \tag{16}
$$

Choose

$$
\lambda=C\delta^{-1}\log(2+r/\epsilon)
      =O((r^2/\epsilon)\log(2+r/\epsilon)),              \tag{17}
$$

for a sufficiently large absolute constant `C`, and give a layer
weight `W_i^(-lambda)`. In any finite execution prefix, the children
born in one epoch have geometrically decreasing prefix sizes. Summing
their weights in reverse order gives total at most

$$
\frac{\kappa^{-\lambda}}
      {1-(1-\tau)^\lambda}\ W_i^{-\lambda}.
$$

The same bound includes a final still-live child. Since
`log kappa >= c delta`, `log J=O(log(2+r/epsilon))`, and
`log(1/tau)=O(log(2+r/epsilon))`, choosing `C` large makes

$$
J\frac{\kappa^{-\lambda}}
         {1-(1-\tau)^\lambda}\le\tfrac12.               \tag{18}
$$

For example, use
`1-(1-tau)^lambda >= c min(1,tau lambda)` and `lambda>=1`.
All constants are uniform in `r`, `epsilon`, and input size.

There is only one first positive layer in an augmenting call: its
collapse matches the unmatched root and terminates that call. Its
prefix size is one. Summing (18) over the finite lifetime tree bounds
the total weight of all born layers by two. Each layer has `W_i<=n`,
so there are at most `2(n+1)^lambda` layer instances. There is at
most one attempted parent extension per collapse, and one collapse
per born layer. This proves a uniform bound on every finite execution
prefix, hence termination; it does not assume termination in order
to count the lifetime tree.

## 6. Explicit input and exact arithmetic

One greedy attempt can be implemented by a single scan of the explicit
edge list. During that attempt the matching is fixed, the forbidden
right set only grows, and active left counters only approach their
caps. A rejected edge never becomes eligible later in that scan.
Owner arrays identify all blockers by scanning the edge's resources.
Each newly encountered matching blocker is marked once.

Copying a candidate, rejecting it, or adopting it costs `O(p)`.
Layer removal and swaps cost at most the current incidence inventory.
Maintain reference counts for the union of historical supports so
that replacing a candidate or discarding a layer costs its own
explicit support size. At a failed growth test, output `S,C` by
enumerating marked identities and resources; verification of hitting
and cardinality uses one input scan.

There is no need to allocate a full resource array separately for
every live historical certificate. Store each candidate by its input
edge identities and keep global resource reference counts. Active
left sets of different live layers are disjoint, so the selected
candidate identities are distinct across layers and use at most
`p` incidences in total. Within one candidate each recorded blocker
meets a selected edge, so the total number of recorded blocker
identities, counting occurrences across candidates, is also at most
`p`. The same blocker identity may appear in several historical
candidates; it is a reference to its immutable input resource list,
not a fresh copy of that list. Replacing one candidate touches at
most `p` incidences, since its then-blockers formed a matching.
Global resource counts and left-cap marks therefore support the
stated per-attempt and final-output bounds without an extra factor
equal to the number of layers.

All loops are controlled by actual edge or resource counts, not by
the possibly very large numerical cap `Q`. The cap, rational
threshold comparisons, and counters use
`poly(b_epsilon+log P)` arithmetic. No numerical value proportional
to `1/epsilon` is silently allocated. At most `n` augmenting calls
are needed, and their extra factor is absorbed in the exponent of
(2). The fixed-layer word arrays and candidate supports also fit the
same bound.

## 7. The original signatures already imply the same rate after a sharper count

The source's signature proof gives at most

$$
L=\lceil C_0\delta^{-1}\log(n+1)\rceil
$$

layers. With base `b=(1-mu^3)^(-1)`, the absolute value of every
finite coordinate is at most

$$
H=O\left(\mu^{-3}
       [L\log(1/\delta)+\log((n+1)Q)]\right).           \tag{19}
$$

Coordinates have a fixed sign pattern and nondecreasing absolute
values. The termination sentinel is fixed. For each length at most
`2L`, the number of weakly increasing coordinate lists in `[0,H]`
is bounded by a binomial coefficient, and summing lengths gives at
most `(2L+1) binom(H+2L+1,2L)`.

Here `Q<=delta^(-2)` up to a fixed factor. Thus
`H/L=O(mu^(-3) log(2+r/epsilon))`, uniformly even when the actual
tree is much shallower than the displayed upper bound `L`. Therefore

$$
\log\!\left[(2L+1){H+2L+1\choose2L}\right]
   =O\bigl(\delta^{-1}\log(2+r/\epsilon)\log(n+1)\bigr).
                                                               \tag{20}
$$

The same rate (2) follows. No tiny-instance exception is required:
overcounting signatures using the upper bound `L` is valid when
`L>n`. The paper itself mentions a strictly increasing subset encoding;
retaining the encoded subset's bounded cardinality gives this count.

For contrast, directly expanding the paper's unrestricted partition
bound yields the weaker uniform exponent
`O(r^5 epsilon^(-4) sqrt(log(2+r/epsilon)))` on `n+1`.
That expression is a coarse derivation here, not a displayed runtime
claimed by the source. Equation (20) explains why the weighted count
must not be advertised as an exclusive algorithmic improvement over
every analysis of the public algorithm.

## 8. What this transfer does and does not add

The useful outcome is a complete uniform parameter bound and a
historical-certificate justification of the needed growth invariant,
with a certificate alternative on arbitrary inputs. Qualitative
polynomial time for fixed rank and slack, and a certifying outcome,
were already established by Annamalai.

The source's actual operations suffice after clarifying the extension
indexing and retaining optional proof metadata. The lifetime-tree
method and the elementary length-aware signature count agree.
This audit has not located a published theorem spelling out the
uniform rate (2), but does not claim that no prior analysis contains
it implicitly. For `r=2`, ordinary bipartite graph matching algorithms
are much faster; (2) is not a replacement for them. No general-graph
matching exponent is improved by this note.
