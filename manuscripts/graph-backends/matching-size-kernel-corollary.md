# An exact matching-size kernel and the current time corollary

**Unconditional deterministic reduction; conditional fast composition.**
The kernel proof below is independent of the matching phase and the
numerical backend. It preserves maximum matching exactly in linear
preprocessing time. If the explicit raw-backend assumptions of the
[main theorem](../../problems/general-matching/proof.md) hold, its solve
time becomes

```math
O(n+m)+(h+1)\exp\!\left[O\!\left(
  (\log(h+2))^{4/5}(\log\log(h+4))^{1/5}
\right)\right],\qquad h=O(\min\{m_s,\nu(G)^2\}).
```

Here m_s is the number of distinct nonloop edges after cleanup. The
kernel itself is unconditional; the improved solve time retains the
proof status and dependencies in [Deterministic Exact General Matching through Persistent Integral Carriers and Normalized Routing](../../problems/general-matching/proof.md).
No publication-priority claim is made for this elementary reduction.

## 1. A linear-time quadratic edge kernel

First scan the input, discard loops and duplicate edge copies if needed,
and construct any deterministic maximal matching `F` by greedy edge
order. Retain original edge identifiers. Let

    C = V(F),     c = |C| = 2|F|,     U = V\C.

If `F` is empty, there are no useful edges. Otherwise `c>=2`. Maximality
implies that `U` is independent, so `C` is a vertex cover. Therefore

```math
|F|\le\nu\le c=2|F|\le2\nu.      \tag{2}
```

Construct a subgraph `H` retaining:

1. every edge with both endpoints in `C`;
2. for each `u in C`, any `min(deg_U(u),c)` incident edges to distinct
   vertices of `U`.

All choices use fixed edge order. Scanning adjacency lists constructs
`H` in `O(n+m)` time. Its edge count `m_H` obeys

```math
m_H\le \min\left\{m_s,\binom c2+c^2\right\}
      =O(\min\{m_s,\nu^2\}).                        \tag{3}
```

Delete isolated vertices of `H`; its remaining vertex count `n_H` is
at most `2m_H`.

### Exact matching preservation

Every matching has at most `c` edges, since `C` is a vertex cover. Take
any maximum matching `M` of the original graph. If an edge `uv` of `M`
was omitted from `H`, it must have `u in C` and `v in U`, because all
`C-C` edges were retained. Temporarily remove `uv`. The vertex `u` has
`c` retained neighbors in `U`, and at most `c-1` vertices of `U` are
matched by the remaining matching. One retained neighbor `w` is therefore
unused. Replace `uv` by `uw`.

The replacement keeps the matching cardinality, creates no conflict,
and decreases the number of edges outside `H`. Repeat until no omitted
edge remains. This is an existence proof; the algorithm does not need
to know `M` or perform these replacements. Since `H` is a subgraph,
it follows that

```math
\nu(H)=\nu(G).         \tag{4}
```

Every edge of the greedy matching `F` belongs to `H`, because its
endpoints lie in `C`. Thus all bounds in (2) remain valid for `H`.

### Why the cutoff cannot be reduced to c-1

For even $`c\geq2`$, take $`K_{c,c}`$ with parts $`C,U`$ and add a perfect
matching on $`C`$. The added edges form a valid initial maximal matching.
The original graph has matching number $`c`$. If every vertex of $`C`$
retains the same $`c-1`$ vertices of $`U`$, then the kernel has only $`2c-1`$
nonisolated vertices. Its matching number is exactly $`c-1`$. Thus a
universal arbitrary-choice cutoff below $`c`$ cannot preserve exactness.

## 2. Composition and independent acceptance

Build and compact $`H`$ once. Its nonempty compact size is
$`q_H=n_H+m_H=\Theta(m_H)`$, and all retained edges carry original IDs.
Apply the exact odd-path degree reduction and uniform solver in
Sections 3.2 and 12 of the main theorem. The solver's geometric,
lifetime, initialization and finite-arithmetic assumptions remain
explicit premises of the displayed fast bound.

Every branch of the uniform program shares the same read-only H.
Validate a proposed matching and search for an augmenting path in H.
Absence of an augmenting path proves optimality in H; the independent
identity nu(H)=nu(G) then proves optimality in G. The verifier need not
rescan the original graph on each proposal. Map the final matching's
edge IDs back once, after acceptance.

The uniform instruction scheduler and its independent acceptance check
are already charged in Section 12 of the main theorem. Cleanup, greedy
construction, kernelization and final translation are charged once in
$`O(n+m)`$. No correctness or running-time property of the required cycle-search implementation follows
from kernelization itself.

If nu=0, the greedy scan finds no nonloop edge and returns the empty
matching. The added one in the displayed expressions handles this
case uniformly. No supplied value or estimate of nu is needed: c is
computed by the greedy matching and lies between nu and 2nu.

## 3. Independent components

Kernelizing nonempty connected components separately retains
$`h_i=O(\min\{m_i,\nu_i^2\})`$ edges in component $`i`$. The preprocessing
still totals $`O(n+m)`$, and the solver cost is the sum of its costs on
the individual $`h_i`$. The union of their maximum matchings is maximum
in the original graph. This can improve the parameter bound from
$`(\sum_i\nu_i)^2`$ to $`\sum_i\nu_i^2`$, as well as reducing the
logarithmic overhead to each component's actual size.

## 4. One kernel for mixed vertex and edge failures

This extension uses a **fixed simple loopless graph**. A failure removes
one native vertex or one native edge; it is not an arbitrary label that
may remove many edges at once. In particular, discarding parallel edge
records before a record-level failure query is not justified by ordinary
matching-preserving normalization.

**Theorem 4.1 (simultaneous mixed-failure preservation).** Let $`C`$ be any
vertex cover of size $`c`$, let $`I=V\setminus C`$, and let $`f\geq0`$ be an
integer failure budget. Retain every edge inside $`C`$. At each $`u\in C`$,
retain any $`\min\{c+f,|N(u)\cap I|\}`$ edges to distinct vertices of $`I`$.
Call the resulting subgraph $`H_f`$. Then

```math
|E(H_f)|\leq\min\left\{m,\binom c2+c(c+f)\right\},
```

and, simultaneously for every vertex set $`X`$ and edge set $`F`$ with
$`|X|+|F|\leq f`$,

```math
\nu(H_f-X-F)=\nu(G-X-F).
```

The graph $`H_f`$ is constructed deterministically in $`O(n+m)`$ time and
retains original identifiers. Taking the endpoints of a greedy maximal
matching gives $`c\leq2\nu(G)`$ without knowing $`\nu(G)`$. The budget
can be clipped to $`n+m`$; reading a longer binary encoding is charged
separately. The construction never allocates unused slots up to $`f`$.

**Proof.** Fix any permitted failure pair $`(X,F)`$ and a maximum matching
$`M`$ of $`G-X-F`$. Since $`I`$ is independent, $`|M|\leq c`$. If an edge
$`uv\in M`$ is absent from $`H_f`$, it has $`u\in C\setminus X`$ and
$`v\in I\setminus X`$, and $`u`$ originally retained $`c+f`$ distinct
outside neighbors. A deleted outside vertex removes at most one of
these choices. A failed retained edge also removes at most one choice.
A deleted cover vertex other than $`u`$ removes none of them; $`u`$ itself
is not deleted because $`uv\in M`$. Counting all failures, including
any overlap, therefore leaves at least $`c`$ retained choices alive.

Remove $`uv`$ temporarily. At most $`c-1`$ outside vertices are matched,
so one of those $`c`$ surviving choices is free. Matching $`u`$ to it
restores cardinality and decreases the number of edges outside $`H_f`$.
Repeat until all matching edges lie in $`H_f-X-F`$. The opposite
inequality follows from the subgraph relation. The argument applies to
every failure pair for this one fixed $`H_f`$; no random choice or
query-dependent reconstruction is used. The edge and construction
bounds follow by scanning adjacency lists. ∎

**Sharpness of the local cutoff.** For even $`c\geq2`$, take $`K_{c,c+f}`$
with left side $`C`$ and add a perfect matching inside $`C`$. Let every
cover vertex retain the same $`c+f-1`$ outside neighbors. Delete any $`f`$
of those neighbors. The original surviving graph still has a matching
of size $`c`$, but the retained graph has only $`2c-1`$ nonisolated vertices
and matching number $`c-1`$. Thus the cutoff $`c+f`$ is necessary for
arbitrary independent neighbor choices in the mixed-failure model.

This theorem is a size and exact-preservation guarantee. Computing a
maximum matching after a query still requires a solver on the retained
graph; the theorem does not supply a constant-time sensitivity oracle.

## 5. Finite evidence

The independent exhaustive checker
[check_reductions.py](../../problems/general-matching/verify/check_reductions.py)
compares matching numbers before and after the kernel on all simple
graphs of at most six vertices, checks both fixed edge orders, and
verifies the sharp-cutoff example. It also checks the separate subcubic
gadget on small graphs and all mixed failures of total size at most two
on every graph through four vertices, in both fixed edge orders.
These checks cover the listed finite instances;
the proofs above establish the general statements.
