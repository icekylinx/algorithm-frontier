# A deterministic fixed-k guide-tree mincut adapter

**Research proof assembly, 25 October 2026.** This note supplies the
constructive fixed-parameter interface needed by the quantified
Gomory--Hu transfer. It keeps the centroid and pruning framework of
the public reductions, but changes the leaf routine's maximizer and
its same-parameter children. The change makes the correctness cases and
the aggregate instance inventory hold simultaneously.

The primary source framework is AKL+,
[arXiv:2507.20354v1](https://arxiv.org/html/2507.20354v1), Section 5.1,
and Zhang,
[arXiv:2112.01042v1](https://arxiv.org/pdf/2112.01042), Sections
2.1--2.4. The audit motivating the change is recorded in
[fixed-k-tree-mincut-source-interface-audit.md](fixed-k-tree-mincut-source-interface-audit.md). This note proves the
modified interface directly; it does not assume that the two source
contraction variants have identical runtime recurrences.

## 1. The interface

Let $G$ be a connected undirected graph with positive integer
capacities, and let $T$ be an abstract tree whose vertex set is a
subset of $V(G)$. A guide-tree edge need not be an edge of $G$.
Fix a source $s\in V(T)$ and an integer $k\ge0$.

Write $\lambda_G(s,t)$ for the ordinary minimum cut value and
$\lambda_{T,k}(s,t)$ for the minimum value of an $(s,t)$-cut
crossing at most $k$ edges of $T$. An empty feasible family has
value infinity.

The main routine returns values satisfying

$$
\lambda_G(s,t)\le\mu(t)\le\lambda_{T,k}(s,t),
       \qquad t\in V(T)\setminus\{s\}.
 \tag{1}
$$

The leaf routine additionally assumes that $s$ is a leaf of $T$
with incident edge $sp$. Let $\eta_{T,k}(s,t)$ restrict the
right side to cuts that also cross $sp$. It returns

$$
\lambda_G(s,t)\le\mu(t)\le\eta_{T,k}(s,t).
 \tag{2}
$$

For every fixed $k$, both routines are deterministic reductions to
exact maxflow on graphs of aggregate size

$$
(m+n)\log^{O(k+1)}(n+4),
 \tag{3}
$$

with the same bound on work outside maxflow, up to fixed polynomial
logarithmic factors. Capacities in these flow instances remain
polynomially bounded integers when the input capacities are so bounded.

Thus an exact maxflow factor $E_{\rm flow}(N)$, monotone in a common
size bound $N$, gives time
$(m+n)E_{\rm flow}(N)\operatorname{polylog}N$ for fixed $k$.
In the Gomory--Hu application $k=16$, so all logarithmic exponents
are fixed constants.

## 2. Local candidate values and target propagation

Each call owns a candidate vector on its current guide-tree vertices,
initially infinity. Updating a candidate means taking its minimum with
a returned valid upper bound. Candidate vectors belonging to different
contracted physical graphs are not silently identified.

Suppose a child contracts a physical set $X$ to a guide vertex
$x$, and $x$ is **not** that child's source. A cut separating
the child source from $x$ is a cut separating the parent source from
every parent guide target in $X$. Therefore a returned value for
$x$ is safely broadcast to all those parent guide targets. If the
contracted vertex is the child source, no such broadcast is made.

This propagation is performed only one recursion level upward. A parent
stores its own vector; it does not repeatedly expand a nested aggregate
all the way to the original top-level targets. The total broadcast
cost of the same-k children of a call is $O(|V(T)|)$. Combining
the lower-k calls costs $O(|V(T)|\log n)$, which is already charged
by their branching count.

In particular, a value previously computed for the single target
$c$ must not be used as though it were a value for a new contracted
target $c'$ containing $c$ and many other vertices. These are
different cut constraints.

## 3. Centroid blocks and isolating regions

Choose a centroid $c$ of $T$; every component of $T-c$ has
at most $|V(T)|/2$ vertices. If $s\ne c$, let $T_0$ be
the component containing $s$, and let $T_1,\ldots,T_l$ be the
other components. Thus $T_0$ includes $s$, while no component
includes $c$. If $s=c$, there is no $T_0$, and all
components are indexed $i>0$.

For $s\ne c$, use the disjoint terminal blocks

$$
B_0=V(T_0)\setminus\{s\},\quad
  B_i=V(T_i)\ (i>0),\quad \{s\},\quad\{c\}.
 \tag{4}
$$

Omit an empty $B_0$. When $s=c$, use just the $B_i$ and
$\{s\}$. The deterministic isolating-cut primitive returns
pairwise disjoint regions $W_i$ for the nonempty branch blocks.
They contain their own block and no other guide-tree vertex. Put
$W_0=\emptyset$ when $B_0$ is empty.

Every call also computes an exact $(s,c)$-mincut when $s\ne c$,
updating $\mu(c)$. A set-terminal mincut is implemented by
contraction or by sufficiently large common-capacity forcing edges.
The isolating-cut construction is a deterministic reduction to maxflow
on total size $(m+n)\operatorname{polylog}n$.

### 3.1 The two uncrossing facts used below

Let $A$ be the target side of a cut, so $s\notin A$.

First, if all guide vertices of $B_i$ lie in $A$, then replacing
$A$ by $A\cup W_i$ does not increase cut capacity. Indeed,
$A\cap W_i$ is a feasible isolating cut for $B_i$, and
submodularity compares its capacity with that of $W_i$. If all
guide vertices of $B_i$ lie outside $A$, the analogous
posimodular argument permits replacement by $A\setminus W_i$.
Both changes preserve the side of every guide vertex. Applied to
disjoint $W_i$'s, they place a whole isolating region on the side
already occupied by its branch block.

Second, suppose all guide vertices on the target side lie in one block
$B_i$. Then $A\cup W_i$ is a feasible isolating cut for
$B_i$, so submodularity gives

$$
c(\partial(A\cap W_i))\le c(\partial A).
 \tag{5}
$$

This intersection preserves every guide vertex's side. The hypothesis
is essential: for the source arm it applies when the centroid is on
the source side, not automatically when the centroid is on the target
side.

If $A$ is optimal among a constrained guide-cut family and the
modification preserves that family, its capacity in fact stays equal.
For the induction below, nonincrease is already sufficient.

## 4. Deterministic pruning

The prunable objects are $T_1,\ldots,T_l$. The source arm and the
centroid are never pruned. Use a family of retained index sets with the
following two properties:

1. For every distinct $i,j>0$, some set retains $i$ and omits
   $j$.
2. The empty retained set is present.

Both orientations of each bit position of the branch index, together
with the empty set, give $O(\log(n+4))$ choices. The empty set
matters when there is only one outside branch.

For a chosen retained set, delete all other outside branches from the
guide tree only; the physical graph is unchanged. A retained target
stays connected to the source in the guide tree. Pruning cannot add a
guide-tree cut edge, and removes at least one whenever a cut-bearing
branch is pruned. In the leaf routine the edge $sp$ remains.

## 5. The main routine

For $k=0$, return infinity for every target. For a fixed small
guide tree, compute all its source-target mincuts exactly and return
them. Exact answers satisfy (1), whether or not a constrained cut
exists.

For a larger tree, form the centroid blocks and regions above, and
perform the following operations.

### 5.1 Same-k source-arm child

If $s\ne c$, contract

$$
\{c\}\cup\bigcup_{i>0}W_i
 \tag{6}
$$

to one vertex $c'$. Use guide tree $T_0$ together with $c'$
and the original attachment to the centroid. The source remains $s$.
Run the main routine with parameter $k$. Propagate its values for
surviving targets, and broadcast its value for $c'$ to every parent
guide target merged into (6).

Including $c$ in (6) makes the guide an ordinary tree and is also
needed for the clean inventory equality below.

### 5.2 Same-k outside children

For each $i>0$, contract $V(G)\setminus W_i$ to a source
vertex. The guide is $T_i$ with that source attached at its former
centroid edge. Run the main routine with parameter $k$, and
propagate the values for targets in $T_i$.

### 5.3 Lower-k and leaf calls

When $k\ge2$, call the main routine with parameter $k-1$ on
every pruned guide from Section 4. If $s\ne c$, also form

$$
T^+=T-(V(T_0)\setminus\{s\})+\{sc\},
 \tag{7}
$$

where an already present $sc$ edge is retained only once. Run the
main routine on $T^+$ with parameter $k-1$, and the leaf routine
on $T^+$ with parameter $k$. Combine their values for retained
targets. The physical graph in these calls is unchanged.

For $k=1$, omit these lower-k and leaf calls. The same-k children
and the exact centroid cut already cover every one-respecting cut.

### 5.4 Correctness of the main routine

Fix a target and an optimal cut $A$ for the right side of (1).
The centroid target is handled exactly. If all guide cut edges are
incident to the source arm, every outside branch is uniformly on the
centroid's side. The first uncrossing fact puts each $W_i$,
$i>0$, on that same side, permitting contraction (6). A target
inside $T_0$ survives. Any outside target is represented by $c'$
and receives the child answer by broadcast. The cut still crosses at
most $k$ child-guide edges.

If all cut edges are incident to one outside branch $T_i$, every
guide target on the opposite side from $s$ lies in $T_i$.
Equation (5) confines the cut to $W_i$, so the corresponding
outside child preserves it.

Otherwise, if the target lies in $T_0$, prune one outside
cut-bearing branch. If the target lies in $T_i$ and another
outside branch is cut-bearing, retain $T_i$ and prune one such
other branch. These calls leave a feasible cut with at most $k-1$
guide edges.

The only remaining case has a target in $T_i$, cut edges incident
to both $T_i$ and $T_0$, and no other cut-bearing outside
branch. In $T^+$, if $s,c$ are on the same side, the new
edge does not cross and at least one old cut edge is removed. If they
are on opposite sides and at least two old source-arm edges cross,
the new crossing edge replaces at least two. Both cases are covered
by the main lower-k call. Otherwise exactly one source-arm edge is
replaced by the crossing edge $sc$. The cut has at most $k$
guide edges and crosses the new source-leaf edge, so the leaf call
covers it. This last case has at least two total cut edges and cannot
occur when $k=1$.

All returned values are capacities of valid cuts in the current graph
or in its contractions. Their lower bound in (1) follows immediately.

## 6. The modified leaf routine

The source $s$ is a leaf, and $sp$ is its only guide edge.
Use the same small-tree and $k=0$ bases as above.

For $k=1$, every allowed cut separates $s$ from every other
guide vertex. One exact set mincut between $\{s\}$ and
$V(T)\setminus\{s\}$ therefore gives the value
$\eta_{T,1}(s,t)$ for every target. Return that value for all
targets. This does not identify a physical guide subtree with a cut
shore when Steiner vertices are present.

Assume now $k\ge2$ and the guide is larger than the fixed base
size. Its centroid is not the source leaf. Form $T_0,T_i,W_i$
and compute the centroid cut as in Section 3.

### 6.1 Complete all lower-k information first

For every pruned guide of Section 4, run the leaf routine with parameter
$k-1$, combining its answers. Also run the **main** routine on
$T^+$ from (7), with parameter $k-1$, and combine its answers.

Only after these calls finish, choose

$$
z\in\arg\max_{v\in V(T)\setminus\{s,c\}}\mu(v),
 \tag{8}
$$

breaking ties deterministically. The maximization includes the entire
source arm $V(T_0)\setminus\{s\}$. Restricting it to outside
branches would lose the argument below.

### 6.2 If the maximizer is on the source arm

If $z\in V(T_0)\setminus\{s\}$, create **one** same-k child:
the full source-arm child (6), with guide $T_0+c'$ and source
$s$. Call the leaf routine on it with parameter $k$.
Propagate surviving-target values and broadcast the non-source target
$c'$ as described in Section 2. There is no second same-k child.

### 6.3 If the maximizer is on an outside branch

If $z\in V(T_j)$, create the following two same-k children.

**Restricted source-arm child.** If $W_0\ne\emptyset$, contract
$V(G)\setminus W_0$ to a source vertex $s'$. Use the tree
$T_0$, with its source $s$ relabeled $s'$. Equivalently,
after quotienting the full guide, delete its old attachment from
$T_0$ to $c$; keep the edge $sp$. The result is an ordinary
tree in which the source is still a leaf. Call the leaf routine with
parameter $k$, propagating the values for the targets of
$T_0\setminus\{s\}$.

**Selected outside child.** Contract

$$
\{c\}\cup W_0\cup
                         \bigcup_{i>0,\ i\ne j}W_i
 \tag{9}
$$

to $c'$. The source $s$ is not contracted. Use guide tree
$\{s,c'\}+T_j$, with source edge $sc'$ and the original
attachment of $T_j$ to $c'$. Call the leaf routine with
parameter $k$. Propagate its surviving-target values and broadcast
its non-source target $c'$.

## 7. Correctness of the modified leaf routine

Fix a target $t\ne s,c$, and let $A$ be an optimal cut for
$\eta_{T,k}(s,t)$, with $s\notin A$. The mandatory edge
implies $p\in A$. Write $w=c(\partial A)$. If the candidate
after Section 6.1 is already at most $w$, nothing remains to prove.
Assume it is larger than $w$.

### 7.1 A target on the source arm

If $t\in T_0\setminus\{s\}$ and an outside branch is
cut-bearing, pruning that branch gives a feasible leaf cut with at most
$k-1$ guide edges. This would already bound $\mu(t)$ by $w$.
Thus an unresolved target here has every cut edge incident to $T_0$.

If $c\notin A$, all target-side guide vertices lie in
$B_0$. Equation (5) confines the cut to $W_0$, preserving
the source-leaf edge. It is feasible in the restricted source-arm
child. It is also feasible in the full source-arm child, after putting
all outside $W_i$'s on the centroid's side by the first
uncrossing fact. Hence this case is covered whichever branch (8)
chooses.

If $c\in A$, every outside guide vertex lies in $A$. In
$T^+$, the same physical cut crosses only the edge $sc$.
Since $k\ge2$, the main lower-k call in Section 6.1 bounds
$\mu(v)\le w$ for **every** outside guide vertex $v$.
Because $\mu(t)>w$, the global maximizer in (8) must be on the
source arm. The algorithm therefore chooses the full source-arm child.
All outside branches are uniformly on the centroid's side; the first
uncrossing fact permits (6), retaining $s$ separately from $c'$.
This preserves the required cut and its mandatory leaf edge.

This is exactly the case for which the unrestricted use of
$G/(V\setminus W_0)$ would identify opposite sides of the cut.
The maximizer rule ensures that this restricted child is not relied on
for such a target.

### 7.2 A target on an outside branch

Let $t\in T_i$. If another outside branch $T_j$ is
cut-bearing, a pruning call retaining $T_i$ and pruning $T_j$
already provides the required answer. Assume no such branch exists.

Let $q_0$ be the number of cut edges incident to the source arm.
It is at least one because $sp$ crosses. If $c\notin A$,
the tree $T^+$ removes at least one crossing edge and adds no
crossing edge. If $c\in A$ and $q_0\ge2$, it removes at
least two and adds one. Either case is covered by the main lower-k
call. Thus an unresolved target must satisfy

$$
c\in A,\qquad q_0=1,\qquad
      \text{all outside cut edges are incident to }T_i.
 \tag{10}
$$

If $T_i$ has no cut edge, the cut crosses only the new $sc$
edge in $T^+$, and is again handled by the main lower-k call.
Therefore $T_i$ is cut-bearing.

For every guide vertex $v$ outside $T_i$ and different from
$s,c$, a pruning call can keep $v$ and remove $T_i$:
use the empty retained family member for source-arm vertices, or a
bit separator for another outside branch. The cut then has at most
$k-1$ guide edges and still crosses $sp$. Hence

$$
\mu(v)\le w\quad
                 (v\notin T_i,\ v\ne s,c).
 \tag{11}
$$

The unresolved target has $\mu(t)>w$, so (8) forces
$z\in T_i$. The selected outside child is therefore the one
indexed by $i$.

Because the source arm has only the cut edge $sp$, all guide
vertices in $B_0$ are on the centroid's side $A$. Every
outside branch other than $T_i$ is also uniformly on that side.
The first uncrossing fact puts $W_0$ and those outside $W_j$'s
wholly in $A$, permitting contraction (9). The source $s$
stays separate. The old single source-arm crossing is represented by
the new mandatory edge $sc'$; no other crossing is added. The
selected child consequently has a feasible cut of value at most $w$
with at most $k$ crossings and the required source edge.

These cases cover every target. The lower bound in (2) follows because
all candidate values come from valid current-graph cuts or cuts in its
contractions. Broadcasts are valid by Section 2. This completes the
correctness induction, taking the leaf routine at parameter $k$
before the main routine at parameter $k$: every call from the leaf
routine to the main routine has parameter $k-1$.

## 8. Same-k inventory and depth

Let $n$ be the current physical vertex count, including any existing
contraction vertices. Distinct $W_i$'s are disjoint and exclude
$s,c$.

For the main routine with $s\ne c$, its source-arm child has

$$
n_0-1=n-1-\sum_{i>0}|W_i|.
 \tag{12}
$$

Its outside child $i$ has $n_i-1=|W_i|$. Summing gives
$\sum_i(n_i-1)=n-1$. When $s=c$, the outside children alone
give at most $n-1$.

In the leaf routine's source-arm-maximizer case there is only one
same-k child, with $n_0-1\le n-1$. In its outside-maximizer case,
the restricted child has $n_0-1=|W_0|$. The selected child has

$$
n_1-1=n-1-|W_0|-
                               \sum_{i>0,\ i\ne j}|W_i|.
 \tag{13}
$$

Therefore

$$
(n_0-1)+(n_1-1)
                  =n-1-\sum_{i>0,\ i\ne j}|W_i|
                  \le n-1.
 \tag{14}
$$

The uncontracted regions of those two children are disjoint:
$W_0$ for the first, and a subset of its complement for the second.
The uncovered Steiner region is never duplicated into both of them.

Every same-k child guide has at most $|T|/2+2$ vertices. For
$|T|$ above the fixed base threshold, this is at most
$0.9|T|$. The main routine also calls one leaf routine at the same
parameter without necessarily reducing guide size. A typed recursion
branch can make this main-to-leaf transition at most once before
$k$ decreases. A leaf call never calls a main routine with the
same $k$.

## 9. Solving the aggregate recurrences

Let $L=C\log(n_{\rm root}+4)$ dominate the pruning family size,
the centroid depth, and all fixed overheads. For one fixed respect
parameter, equations (12)--(14) allow the costs of same-k descendants
to be summed by their actual vertex or uncontracted-edge mass, with
only a factor $O(L)$ over one centroid-depth traversal.

Write $F_k$ and $H_k$ for normalized aggregate inventory factors
of the main and leaf routines. Their recurrences have the form

$$
\begin{split}
 H_k&\le C L\bigl(1+L H_{k-1}+F_{k-1}\bigr),\\
 F_k&\le C L\bigl(1+L F_{k-1}+H_k\bigr).
 \end{split}
 \tag{15}
$$

The finite bases are polynomial logarithmic. Induction gives
$F_k,H_k\le L^{O(k+1)}$. This proves the aggregate vertex bound
and the corresponding bound for original edges not incident to any
new contraction vertex.

Every physical contraction creates a marked contraction vertex, even
if an implementation reuses an old vertex name. Along any recursion
branch there are $O(kL)$ such vertices: there are at most $k$
respect-parameter phases and logarithmic same-k depth in each. Combine
parallel physical edges whenever they arise. At an instance with
$n_*$ vertices, edges incident to marked contraction vertices then
number at most $O(n_*kL)$. Summing this using the already proved
vertex inventory gives another fixed polynomial logarithm. Ordinary
graph construction, broadcasting, and candidate merging have the same
bound.

The exact centroid and set-mincut calls add only a fixed number of
maxflow instances per recursion node. The isolating-cut reduction adds
a polynomial logarithm to their aggregate size. This proves (3).
It multiplies the exact maxflow factor once, rather than raising that
factor to the centroid depth.

## 10. Consequence for the quantified application

The preceding argument is the missing fixed-k construction interface.
Together with the other named public reductions audited in
[gomory-hu-external-factors-except-fixed-k.md](gomory-hu-external-factors-except-fixed-k.md), and the strong-forest,
packing, finite-arithmetic, and skeleton adapters in
[gomory-hu-seven-eighths-dependency-audit.md](gomory-hu-seven-eighths-dependency-audit.md), it supplies the intended
exact Gomory--Hu composition, subject to the separately stated local
strong-forest proof imports.

The changes that must be preserved are specific: include the centroid
in each full source-arm contraction; maximize over all non-source,
non-centroid targets after every lower-k call; use only one same-k
child when that maximizer is on the source arm; preserve the source
leaf edge in the restricted child; broadcast non-source contracted
targets; and use the set-mincut base for leaf parameter one. Omitting
any of these can invalidate either the cut argument or the inventory.

Additional source comparisons are recorded in the [guide-tree analysis](fixed-k-global-max-leaf-independent-audit.md). Marked contraction identities
persist throughout the entire recursion of one adapter invocation;
entering a lower-k call does not turn old contraction vertices back
into unmarked original vertices for the edge-inventory proof.
