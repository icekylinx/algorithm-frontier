# Input-linear scans for the independent-transversal layer primitives

**Implementation refinement; independent and root audits passed, 25 October 2026.**

This note changes no combinatorial operation or signature argument in
[independent transversal proof](../../problems/independent-transversal/proof.md). It records the
explicit-input cost of implementing the public layer operations with
adjacency lists. In particular, the source's coarse `P^4` multiplier
need not be paid when the number of classes is small relative to the
graph input. Section 8 of
[Current blocker growth for independent transversals](../../problems/independent-transversal/proof.md)
records the independent review; the main statement now includes this
refinement.

Let `q` be the number of nonempty classes and
`P=|V|+|E|+q+2`. Work in the graph with within-class edges removed.
Graph vertices, classes, the current partial independent transversal
`M`, and each layer's selected and blocker sets have explicit IDs and
membership flags. Parallel edges can be deduplicated at input, or kept
with counters; either convention is covered by input-linear scans.

## 1. A single BuildLayer call costs O(P)

The source operation is [Graf--Haxell, Section 4.1 and Definition
11](https://arxiv.org/html/1811.02687v2). During one call, the matching,
the lower prefix, and the set of active classes are fixed. The candidate
sets `X,Y` only grow.

Initialize the following scratch data in `O(P)` work:

* a bit for whether a class is active;
* the current selected count in every class;
* flags for the exact explicit exclusion set `Y_last union X union Y`;
* for every graph vertex, the number of its neighbours in
  `Z=X_prefix union Y_prefix union X union Y`.

The neighbour counts can be initialized by marking the distinct
vertices of `Z` and scanning their adjacency lists. A vertex is
addable precisely when its class is active, it is not explicitly
excluded, its class count is below the cap, and its neighbour count
is zero.

Scan all vertices once in a fixed ID order. Add an addable vertex `v`
to `X`. Find its current matching neighbours by scanning its adjacency
list, add them to `Y`, and activate `v` and every newly added blocker
in `Z`. Activation increments the neighbour count of every adjacent
vertex. A vertex already activated is never activated again.

Every failed addability test remains failed for the rest of the call:
active classes are fixed; exclusions and neighbour counts only grow;
class counts only grow. Thus no vertex needs to be revisited, and the
completed pass has exactly the maximality property required by the
public greedy routine. Choosing the least currently addable ID gives
the same operation sequence as the scan.

Each selected vertex's adjacency list is scanned once to identify its
matching neighbours. Each activated vertex's list is scanned once to
update counts. These two totals are each at most the entire adjacency
volume. This proves `O(P)` work per call. There is no array or loop of
length equal to the numerical cap `Q`.

The returned candidate is retained as lists of selected and blocker
vertex IDs. Copying one such candidate costs at most `O(P)`. Keeping
the latest actual candidate for at most `q+1` live layers uses at most
`O(P(q+1))` space by a deliberately simple implementation; no
near-linear space claim is needed here.

## 2. SuperposedBuild and one main-loop iteration

One SuperposedBuild call visits each surviving layer at most once,
and adoption only truncates the remaining suffix. There are at most
`q+1` layers, so its cost is `O(P(q+1))`.

For a collapse, scan the last selected set's adjacency lists to
determine which selected vertices are currently unblocked. Choose one
per relevant class, perform the public matching swaps, remove the
corresponding blockers from the preceding layer, and discard the last
layer. All these bookkeeping operations can conservatively be done
in `O(P(q+1))` work, or less with persistent membership flags.

Every iteration of the inner collapse loop strictly decreases the
layer count: it first removes the last layer, and the following
SuperposedBuild can only truncate it further. Consequently there are
at most `q+1` collapses during one outer GrowTransversal iteration.
This bound does not depend on the numerical sizes of `mu`, `rho`,
or `Q`. Including all its SuperposedBuild calls, one outer iteration
costs

```math
O(P(q+1)^2).
```

This count permits a newly built final layer with no blockers. Every
older continuing layer is noncollapsible and hence contains at least
one blocker, so there cannot be more than `q` such layers.

## 3. Both certificate exits fit the same bound

For the current-blocker exit, iterate through the stored candidate
lists to obtain their extras, full classes, selected union, and blocker
union. Mark the excluded classes. The sum of at most `q+1` list
lengths is `O(P(q+1))`. The current unblocked selected vertices can
be found by adjacency scans, after which one stored original neighbour
per such vertex completes total domination. Extracting the induced
star constellation uses the current layer and blocker lists.

For the source's original small-birth exit, use the explicit
construction in its Lemma 15: rerun at most one BuildLayer per live
prefix, form the listed unions and deleted classes, and build its
neighbour-completion set. The same adjacency-list and set-membership
operations cost at most `O(P(q+1)^2)`. This deliberately loose bound
also permits separately checking the returned certificate against
the original graph.

Checking the new prefix inequalities costs `O(q+1)` per continuing
boundary. A certificate is built only when the algorithm is about to
return it. No universal domination promise is tested.

## 4. Resulting total input dependence

Let

```math
\lambda=\epsilon^{-1}\log(2+r/\epsilon).
```

The current-blocker signature proof bounds the number of iterations
per augmentation by `(q+1)^{O(lambda)}`. There are at most `q`
augmentations. The polynomial factors in `q+1` above are absorbed
in that exponent because `lambda` is bounded below by a positive
absolute constant. Hence the implementation yields

```math
\boxed{\quad
 P\,(q+1)^{O(\epsilon^{-1}\log(2+r/\epsilon))}
       \mathrm{poly}(b_\epsilon+\log P).
 \quad}
```

The same implementation applies to the named derived-public baseline,
with the older exponent
`O((r/epsilon) log(2+r/epsilon))`. Thus this improvement of the
explicit-input multiplier is common implementation work, not an
additional advantage assigned only to the current-blocker method.

The signature coordinates and logarithms are used only in the proof;
the algorithm does not compute them. Threshold comparisons use
rational arithmetic on counts of actual vertices. After replacing
`r` by `min(r,q+1)`, all those counts and parameters have bit length
`O(b_epsilon+log P)` if the supplied integer claw bound is already
clipped. With an arbitrarily long unbounded encoding of that integer,
add its input-reading cost before clipping. This accounts for the displayed bit factor
without a numerical `1/epsilon` loop or storage allocation.

