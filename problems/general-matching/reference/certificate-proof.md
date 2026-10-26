# A quadratic extraction of a matching optimality certificate

This note proves the certificate extraction implemented by
`_failed_search_forest` and `_barrier` in [matching.py](matching.py).
Given a maximum matching on a $`k`$-vertex simple graph, extraction takes
$`O(k^2)`$ additional work. Consequently the reference solver's normal and
certificate modes share the same cubic bound. The certificate is checked
by the [independent verifier](verify_certificate.py), which performs no
blossom search.

The construction is a classical alternating-forest method. The resulting
sets give the Gallai–Edmonds decomposition, whose historical source is
[Gallai (1964), Theorem (E.1)](https://real.mtak.hu/189486/1/cut_MATKUTINT_1964_3_pp401_-_413.pdf).
The proof below establishes the required extraction and upper-bound
equality directly; it does not assume that decomposition theorem.

## 1. Statement and algorithm

Fix a maximum matching $`M`$ of the simple graph $`H`$. Let $`f`$ be
the number of vertices exposed by $`M`$, meaning unmatched by it. Start
one Edmonds alternating forest with all exposed vertices as roots. Keep
$`M`$ fixed throughout the search.

Every root is initially **outer**. An edge from an outer vertex to an
unreached matched vertex grows the forest by that **inner** vertex and its
matched outer child. An edge between different outer blocks in the same
tree contracts the usual odd blossom. Every original vertex in the new
block becomes outer; newly outer vertices enter the scan queue. An edge
between outer vertices in different trees would give an augmenting path,
so the implementation rejects that state as inconsistent with a maximum
input matching.

After exhausting the queue, let $`O`$ be the set of all original outer
vertices and $`I`$ the remaining inner vertices. Return $`A=I`$.

**Theorem 1.** The algorithm leaves $`M`$ unchanged and returns a set
$`A`$ satisfying

```math
2|M|=|V(H)|-o(H-A)+|A|,
```

where $`o(H-A)`$ is the number of odd connected components after deleting
$`A`$. It uses $`O(k^2+|E(H)|)=O(k^2)`$ time and
$`O(k+|E(H)|)`$ storage. Moreover,

```math
O=\{v:\nu(H-v)=\nu(H)\},
\qquad I=N_H(O)\setminus O.
```

The implementation first tests $`A=\varnothing`$ and skips the forest
search when that set already gives the displayed equality. This shortcut
returns a valid barrier, although it need not be the particular set
$`N_H(O)\setminus O`$. The theorem describes the forest search when it
is used; the independent verifier accepts either tight barrier.

## 2. Invariants of the contracted forest

A **block** is either a singleton or the set of original vertices inside
a current contracted blossom. The quotient graph has one vertex per
block. At every stage the search maintains these invariants:

1. Each outer block is connected, has odd order, and is factor-critical:
   deleting any prescribed vertex leaves a perfect matching inside that
   block. Its current $`M`$-edges form a near-perfect internal matching
   whose only internally exposed vertex is the block's base.
2. **Only the base can have a matched edge leaving an outer block.** A
   nonroot outer block's base is matched to its inner parent. A root block
   has no external matched edge and contains exactly one original exposed
   vertex of $`M`$.
3. Every inner vertex is a singleton and has exactly one matched outer
   child. Thus every nonroot outer block has one inner parent, and every
   inner vertex has one such child. There is one more outer block than
   inner vertices in each quotient tree.
4. The original members of different blocks are disjoint. Every original
   member of an outer block is marked outer and has its adjacency scanned
   once after receiving that mark.

These statements initially hold for the singleton roots. Growing a tree
adds one inner singleton and its matched outer child, preserving the
matching structure and the difference between the two node counts.

For a contraction, take an edge between outer blocks in the same tree.
The least common tree ancestor of its endpoints is outer: an inner
vertex has only one child and cannot be the branching ancestor. The
two paths to this ancestor, together with the new edge, form an odd
cycle in the quotient, with one more outer block than inner singleton.
If the cycle contains $`a`$ outer blocks, it contains $`a-1`$ inner
vertices. Replacing them by one outer block removes $`a-1`$ of each
type, preserving the count exactly.

The new block is factor-critical. More generally, consider an odd cycle
of disjoint odd factor-critical blocks joined by selected connecting
edges. After deleting a vertex in one block, match that punctured block
internally. Pair the remaining even number of blocks around the cycle.
For each pair use its connecting edge, and match both blocks internally
after deleting the connecting endpoints. This is a perfect matching of
the union minus the prescribed vertex. The argument applies recursively
to nested blossoms and uses only actual graph edges.

The fixed matching also has the required base property after contraction.
Each inner vertex on the alternating cycle is matched to its outer child
on that cycle. Each constituent outer block is internally matched except
at its base. Consequently all bases on the cycle are matched internally
to the new block except the ancestor block's base. That base retains its
previous external matched edge, if any. No second external matched edge
appears.

For the array implementation, `base[v]` identifies the current quotient
block. To climb from an outer block to its outer grandparent, first use
the matched edge at its base and then the `parent` edge of that inner
vertex. These are exactly the two steps used in `common_base`.
`mark_branch` rewrites the alternating routes along the two cycle
branches; the later scan identifies all their blocks with the ancestor
base. The ancestor's external matched edge is unchanged. Tree branches
attached to the contracted cycle remain attached to its new block.
The root label `owner` remains unchanged within that tree. This maintains
the quotient forest and the unique external matched-edge invariant
through every parent rewrite.

## 3. Lifting paths through the blocks

Every vertex of an outer block can be exposed by a matching of the same
cardinality as $`M`$, preserving the other roots. To see this, follow the
quotient tree path from its root block to the target block. Remove the
matched edge from each inner vertex to the next block base, and add the
preceding unmatched tree edge into that inner vertex.

In each nonfinal block on this path, the new crossing edge uses one known
attachment vertex $`x`$. Replace the internal matching by a perfect
matching of that block minus $`x`$, using factor-criticality. In the
final block leave the prescribed target vertex exposed. Other blocks and
off-path matching edges stay as they were. Exactly one original root
has been matched and the target has been exposed; cardinality is unchanged.

The symmetric difference with $`M`$ contains a simple even alternating
path from that root to the target. Its first edge is unmatched by $`M`$
and its last edge is matched by $`M`$; a zero-length path is allowed.
This is the required lifting argument. It does not assume that an
arbitrary projected walk through nested blossoms is already simple.

If an edge joined outer vertices in different trees, the two lifted
paths would be vertex-disjoint because their trees have disjoint blocks.
Joining them by that edge gives an augmenting path between two exposed
roots. Such a path would increase $`|M|`$, contradicting maximal
cardinality. This proves that the explicit cross-tree rejection cannot
occur for a correct maximum matching.

## 4. Exhaustion gives a tight odd-component bound

Let $`b`$ be the number of final outer blocks. Summing the quotient-tree
count over all $`f`$ roots gives

```math
b=|I|+f.
```

There is no edge between distinct final outer blocks. Such an edge would
have been scanned when its later-labelled endpoint became outer. It
would contract blocks within a tree or give an augmenting path between
trees. Later contractions only merge blocks.

Also $`N_H(O)\setminus O=I`$. An unreached neighbor would grow a tree,
while every inner vertex has an outer parent. Let
$`U=V(H)\setminus(O\cup I)`$. Every vertex in $`U`$ is matched by
$`M`$ to another vertex of $`U`$: all exposed vertices were roots, and
every reached matched pair lies inside an outer block or is an
inner/outer parent-child pair. Hence $`M`$ restricted to $`U`$ is
a perfect matching.

After deleting $`I`$, the components are the $`b`$ connected odd outer
blocks and the components of $`H[U]`$. Each latter component has a
perfect matching and therefore even order. It follows that

```math
o(H-I)=b=|I|+f.
```

Since $`2|M|=k-f`$, this proves the equality in Theorem 1.

For completeness, the equality is a self-contained optimality certificate.
For any proposed set $`A`$, each odd component of $`H-A`$ needs either
an unmatched vertex or a matching edge to $`A`$. At most $`|A|`$
components can use such matching edges. Therefore every matching has size
at most $`(k-o(H-A)+|A|)/2`$. A feasible matching attaining that bound
is maximum. The independent verifier uses only this argument and the
separately proved exact kernel conditions.

## 5. Why the outer set is exactly the exposable set

Section 3 shows that every vertex of $`O`$ can be exposed by a maximum
matching. Conversely, any matching leaves at least $`b-|I|=f`$
vertices of $`O`$ unmatched: each odd outer block needs an unmatched
vertex or a distinct matching endpoint in $`I`$. A maximum matching
has exactly $`f`$ exposed vertices in the whole graph, so it cannot
expose a vertex outside $`O`$. Thus $`O`$ is exactly the set of
vertices exposable by a maximum matching.

A vertex is exposable by a maximum matching precisely when
$`\nu(H-v)=\nu(H)`$. Equivalently it is the endpoint of a simple even
$`M`$-alternating path from an exposed root. One implication follows by
flipping that path; the other follows by taking the symmetric difference
of $`M`$ with a maximum matching that exposes the vertex. Both matchings
are maximum, so their path components cannot augment either matching.
This proves the remaining claims of Theorem 1 without invoking an
external decomposition theorem.

## 6. Cost and executable evidence

Every vertex becomes outer at most once and has its adjacency scanned
once. Every contraction merges current blocks, so at most $`k`$
contractions occur. Ancestor walks, branch rewrites and the full-array
contraction scan each cost $`O(k)`$. The total is
$`O(k^2+|E(H)|)`$, with linear additional storage. Constructing $`I`$
and checking its odd-component count takes $`O(k+|E(H)|)`$ work.

The [dedicated search checker](../verify/check_certificate_search.py)
compares the actual production function against the deletion-defined
exposable set using independent subset dynamic programming. It checks
all simple graphs through six vertices and 500 seeded graphs on seven
through thirteen vertices. It also verifies the terminal count, the
factor-criticality of each outer block, its unique external matched
edge, the perfect matching on $`U`$, and the exact odd-component count.
For graphs through nine vertices it independently enumerates simple
even alternating paths. Rejection of a nonmaximum input matching uses
explicit production exceptions and remains active under optimized Python.

The [full reference test suite](../verify/check_reference.py) additionally
checks every public solver result with the independent certificate
verifier, including native loops, parallel records, isolated vertices,
invalid certificates and CLI execution. These are finite implementation
checks supporting the proof and review; they are not proof-assistant
formalization.
