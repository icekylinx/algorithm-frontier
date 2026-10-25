# An elementary exponential fallback for the full transversal certificate

**Derived public baseline, 25 October 2026.**

The elementary procedure in [Graf--Haxell,
arXiv:1811.02687v2, Section 2, proof sketch of Theorem
2](https://arxiv.org/html/1811.02687v2) already supplies an exponential
algorithm for the exact domination/constellation alternative.
The following composition count makes its dependence on the number of
classes explicit and independent of the claw or slack parameters.
This is a public baseline, not a separate new algorithmic result.

Let `q` be the number of nonempty classes and
`P=|V|+|E|+q+2`. Remove within-class edges. The algorithm returns
either an independent transversal or a nonempty class set `S` and a
constellation `K` induced in `G_S`, such that `D=V(K)` totally
dominates `G_S` and

\[
                    |D|\le2(|S|-1).
\]

Consequently it satisfies the full approximate certificate contract
for every positive `epsilon`, with no excess vertices outside `K`.
Its running time is

\[
                         P\exp(O(q)).
\]

## 1. The elementary operation and its stable states

Fix a current partial independent transversal `M` and an unmatched
root class. Maintain selected centres `x_1,...,x_t` and their
pairwise disjoint current blocker sets `N_M(x_i)`. The induced graph
on all these vertices is a disjoint union of stars. The active class
set consists exactly of the root and the distinct classes represented
by the current blockers.

At a **stable state** every centre has at least one blocker. If the
star forest totally dominates the union of the active classes, return
that forest as the certificate. Otherwise choose a vertex `x` in an
active class with no neighbour in the current forest.

If `x` has matching blockers, append `x` and all its blockers as
a new star. Every new blocker lies outside the current active classes:
their current matching representatives already belong to the old
forest, which `x` avoids. Thus the new blocker classes are distinct
and the forest remains induced.

If `x` is unblocked, swap it into the matching for its class, or
augment if it belongs to the unmatched root. In the non-root case,
the removed matching representative was a leaf of one uniquely
identified earlier star. Truncate the forest after that star; its
blocker count drops by one. The newly inserted matching vertex has
no neighbours in the retained forest, so no new blockers are created
there.

If the last retained star now has zero blockers, prioritize its free
centre for the next swap, and continue. This is a legitimate choice
in the source procedure: a free centre has no neighbour in the current
forest. Each such zero-blocker cascade moves strictly to an earlier
star or augments at the root, so it has at most `q` steps. Between
macroscopic steps the maintained state again has only nontrivial
stars. This priority convention avoids counting intermediate zero
centres as stable nontrivial stars.

## 2. At most exponentially many stable signatures

At a stable state write

\[
               (d_1,\ldots,d_t,\infty),\qquad
               d_i=|N_M(x_i)|>0.
\]

The blocker sets are disjoint subsets of `M`, so

\[
                        \sum_i d_i\le|M|\le q-1.
\]

Appending a star replaces the terminal infinity by a positive finite
coordinate. A swap followed by its zero-blocker cascade decreases an
earlier retained finite coordinate and truncates everything above it,
or terminates the augmentation. Therefore the signature strictly
decreases lexicographically at every continuing macroscopic step.

Positive integer lists of sum exactly `s` are compositions of `s`,
of which there are `2^{s-1}` for `s>=1`. Including the empty list,
the total number of lists of sum at most `q-1` is `2^{q-1}` for
`q>=1`. Thus there are at most `2^{q-1}` stable signatures per
augmentation. The argument bounds every finite execution prefix,
so termination is not assumed in the count.

At a certificate exit, let `s=sum_i d_i`. Its active class set has
size `s+1`, while `K` has `s+t<=2s` vertices. Each star has a
nonempty leaf set, and the leaves form a partial independent
transversal of all but the root class. Thus this is precisely the
required constellation, with total domination tested in the working
interclass graph. The same edges certify domination in the original
graph. The constellation itself uses the source's within-class-edge
deletion convention.

## 3. Explicit-input cost and use as a fallback

Selecting an undominated active-class vertex, finding its matching
neighbours, and updating the explicit forest can each be implemented
by adjacency and vertex scans. Even recomputing all needed flags
after each step costs `O(P(q+1))` per macroscopic step including
its cascade. There are at most `q` augmentations. The resulting
`P poly(q) 2^q` bound is `P exp(O(q))`.

For an unbounded rational slack input, this algorithm does not need
to use its numerical value. Add its input-reading cost if required;
the returned exact certificate is valid for every positive slack.

Both the named public layer baseline and the new current-blocker
construction can therefore be combined with this fallback. Equivalently,
run the two algorithms in alternating work budgets until one returns
a result; both outputs have directly checkable certificates. The new
rate becomes

\[
 P\min\left\{\exp(O(q)),\,
      (q+1)^{O(\epsilon^{-1}\log(2+r/\epsilon))}\right\}
      \operatorname{poly}(b_\epsilon+\log P),
\]

whereas the named derived-public layer rate has the exponent
`O((r/epsilon) log(2+r/epsilon))` in its second term. For fixed
slack and unrestricted `r<=q+1`, the current-blocker term is
quasipolynomial in `q` and improves the exponential fallback for
large `q`. For very small slack the elementary algorithm can be
the stronger option. It must not be omitted from a uniform comparison.

