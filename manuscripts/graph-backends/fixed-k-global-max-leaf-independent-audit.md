# Independent audit of the global-max leaf repair

**Status: the complete adapter passes this independent audit.** The
complete algorithm and inventory proof are in
[deterministic-fixed-k-tree-mincut-adapter.md](deterministic-fixed-k-tree-mincut-adapter.md), which was read after
the independent derivation below. This document isolates the correctness
argument, including two base-case and guide-tree details that are easy
to miss. It does not silently import the incompatible contractions from
the two source presentations.

Primary references are AKL+, [arXiv:2507.20354v1, Section 5.1]
(https://arxiv.org/html/2507.20354v1), Zhang,
[arXiv:2112.01042v1, Sections 2.2--2.4]
(https://arxiv.org/html/2112.01042v1), and the alternative algorithm of
AKL+, [arXiv:2111.04958v3, Section 2]
(https://arxiv.org/pdf/2111.04958). The repair below is an additional
argument, not a claim that the displayed source pseudocode already
contains it.

## 1. The leaf contract and notation

The graph is undirected with nonnegative capacities. Its guide tree
$T$ spans an arbitrary subset of graph vertices. The source $s$
is a leaf, with unique neighbor $p$. A leaf call must return values
$\mu(t)$ satisfying

$$
\lambda_G(s,t)\leq\mu(t)\leq\eta_{G,T,k}(s,t),
$$

where $\eta$ is the minimum capacity of an $(s,t)$-cut that
crosses $sp$ and at most $k$ guide edges. Every returned upper
bound is the capacity of an actual separating graph cut, so the lower
inequality is automatic under contractions and minimum updates.

Take a centroid $c$. For a nonconstant-size leaf call, $c\ne s$.
Let $T_0$ be the component of $T-c$ containing $s$, and
$T_1,\ldots,T_l$ the other components. Compute disjoint isolating
regions $W_0,W_1,\ldots,W_l$ for

$$
V(T_0)\setminus\{s\},\quad V(T_1),\ldots,V(T_l),
 \quad\{s\},\quad\{c\}.
$$

Empty groups are omitted. In particular, every $W_i$ is disjoint
from $s,c$. The unused parts of $V$ may be arbitrarily large;
no correctness or inventory argument assumes that the $W_i$ cover
the graph.

Before selecting a same-$k$ branch, complete all these operations:

1. Compute $\lambda(s,c)$.
2. For an ordered-pair separating family of retained outside branches,
   keep $T_0,c$, prune the other outside branches, and run the
   main or leaf procedure with $k-1$. Include the choice that
   prunes **all** outside branches.
3. Form $T^-$ by deleting $T_0\setminus\{s\}$, deleting
   the old source-arm edges, and attaching $s$ directly to $c$.
   Run the main procedure on $(G,T^-,s,k-1)$.

The empty retained set in item 2 matters even when $l=1$: ordered
pair separation alone is then a vacuous condition. Bit positions and
their complementary classes, plus the empty set, give
$O(\log(l+2))$ deterministic calls.

Now choose a maximizer

$$
z\in\operatorname*{arg\,max}_{v\in V(T)\setminus\{s,c\}}
                              \mu(v).
 \tag{1}
$$

The maximization includes the source component $T_0$. This is the
essential change from maximizing over outside components alone.

## 2. The two possible recursive configurations

If $z\in T_0$, make **one** same-$k$ leaf call. Contract

$$
\{c\}\cup\bigcup_{i\geq1}W_i
$$

to $c$, retain $s$ separately, and use guide
$T_0\cup\{c\}$ with its original attachment to $c$.
Call this the full source-component child. Its graph retains the
uncovered Steiner region, but that region is not duplicated into a
second same-$k$ child.

If $z\in T_j$, $j>0$, make these two children:

* **Restricted source child:** contract $V\setminus W_0$ to the
  source and use guide $T_0$ itself. In particular, delete the old
  attachment to $c$; do not use a quotient guide that identifies
  both ends of the source arm. The retained $sp$ edge is still the
  unique source edge. If $T_0=\{s\}$, this child has no target
  and is omitted.
* **Selected outside child:** contract
  $\{c\}\cup\bigcup_{i\ne j}W_i$ to $c$, retain $s$
  separately, and use guide $\{s,c\}\cup T_j$, with source edge
  $sc$ and the original $c$-to-$T_j$ attachment.

The uncontracted regions of these two graphs are respectively
$W_0$ and
$V\setminus(\{c\}\cup\bigcup_{i\ne j}W_i)$. They are
disjoint. This is the place where the previously duplicated uncovered
Steiner region is assigned to only one child.

## 3. Same-side uncrossing preserves the entire guide pattern

Let $A$ be a feasible constrained cut of minimum capacity for a
target. If a complete isolating terminal group lies in $A$, then
$A\cap W_i$ is a feasible isolating cut for that group. Therefore

$$
c(\partial W_i)\leq c(\partial(A\cap W_i)),
 \qquad
 c(\partial(A\cup W_i))\leq c(\partial A).
 \tag{2}
$$

Moreover, $A\cup W_i$ has exactly the same memberships on all
guide vertices as $A$. It remains feasible for the constrained
cut problem, so equality holds in the second inequality. If the group
lies in the complement of $A$, apply the same argument to that
complement. Repeating this over disjoint regions preserves the full
guide cut pattern and capacity, while placing each entire region on
its group's side.

This argument applies to minimum **constrained** cuts, not only to
unconstrained graph mincuts. That distinction is needed for the strong
inductive leaf contract.

## 4. Targets in the source component

Fix $t\in T_0\setminus\{s\}$ and a minimizing leaf cut
$A$, oriented with $s\notin A$ and $p,t\in A$. Write
$a=c(\partial A)$. If an outside component has an incident cut
edge, pruning that component gives a $(k-1)$-respecting cut while
retaining $t,sp$. The earlier calls already ensure $\mu(t)\leq a$.

It remains to consider cuts whose cut edges are all incident to
$T_0$. Every outside component is then on the same side as $c$.
There are two subcases.

### 4.1 The centroid lies on the source side

Here $c\notin A$, so every outside guide vertex is outside $A$.
The set $A\cap W_0$ has the same guide memberships as $A$.
Submodularity with the isolating cut $W_0$ shows that it has
capacity $a$. Hence the restricted source child preserves the cut.
Dropping the old boundary attachment to $c$ only decreases the
number of cut edges and does not delete $sp$.

If the selected configuration instead uses the full source child,
equation (2) moves every outside $W_i$ to the centroid side while
preserving the cut. Thus either configuration handles this subcase.

### 4.2 The centroid lies on the target side

Here every outside guide vertex is in $A$. In $T^-$, the
same graph cut crosses exactly one guide edge, namely $sc$.
For $k\geq2$, the earlier main $(k-1)$ call therefore gives

$$
\mu(v)\leq a
       \quad\text{for every outside }v\in T_1\cup\cdots\cup T_l.
 \tag{3}
$$

If $\mu(t)>a$, the global maximizer (1) must consequently lie in
$T_0$. The algorithm uses the full source child. Applying (2) to
the outside regions puts all of them on the centroid side, without
merging $s$ and $c$, and preserves this cut. This is precisely
the case for which an unconditional contraction of
$V\setminus W_0$ was invalid.

## 5. Targets in an outside component

Fix $t\in T_i$, $i>0$, and a minimizing leaf cut $A$
with $s\notin A$, $p,t\in A$, of capacity $a$.

If another outside component has an incident cut edge, a pruning call
retains $T_i$ and removes such a component. It already returns
$\mu(t)\leq a$. Assume henceforth that outside cut edges occur
only at $T_i$.

If $c\notin A$, then removing the source component removes at
least the forced edge $sp$, while the replacement $sc$ is
uncut. The main $(k-1)$ call on $T^-$ handles the target. If
$c\in A$ and at least two source-component edges are cut,
replacing them by the single cut edge $sc$ also lowers the cut
count by at least one. This case is handled as well.

Thus an unresolved target has the following pattern:

* $sp$ is the only cut edge incident to $T_0$;
* every vertex of $T_0\setminus\{s\}$, the centroid, and all
  outside components other than $T_i$ lie in $A$;
* at least one cut edge is incident to $T_i$, since otherwise
  $T^-$ has only the cut edge $sc$, already handled for
  $k\geq2$.

Pruning $T_i$ gives a forced-source $(k-1)$-respecting cut for
every target in $T_0\setminus\{s\}$. For any other outside
component, a pruning choice retains that component while removing
$T_i$. Consequently

$$
\mu(v)\leq a
        \quad\text{for every }v\notin T_i\cup\{s,c\}.
 \tag{4}
$$

If $\mu(t)>a$, the global maximizer must lie in $T_i$.
The algorithm therefore selects exactly this outside component.
Equation (2) absorbs $W_0$ and every other outside $W_j$
into the centroid side, preserving the complete guide pattern and
capacity. After contraction the source edge is $sc$, which is
cut, and the original $sp$ plus target-component pattern becomes
the same-size or smaller cut pattern in the selected child.

This also proves that choosing the full source child cannot abandon an
unresolved outside target: such a target would force the maximizer
into its own outside component.

## 6. Base cases and the main procedure

For a leaf call with $k=1$, the only permissible guide pattern is
$s$ on one side and every other guide vertex on the other. One
deterministic minimum cut separating $\{s\}$ from
$V(T)\setminus\{s\}$ gives exactly the constrained value for
every target. Its graph vertices outside the guide remain unrestricted.

For a main call with $k=1$, direct physical-edge summation along
the guide is generally invalid, because the guide need not span the
whole graph. Instead use the repaired main procedure's same-$k$
children, without any lower-$k$ or leaf calls. A one-respecting cut
has its unique cut edge in one centroid component, so the main
procedure's single-component case already covers every target.

In detail, the main source-component child contracts
$\{c\}\cup\bigcup_{i\geq1}W_i$ to $c$, with guide
$T_0\cup\{c\}$. This removes redundant quotient-guide cycles
and preserves every source-component-only cut by (2). The child's
answer for the contracted centroid is a valid upper bound for every
outside guide target represented by that supernode, and must be
propagated to those targets when needed. Other main children contract
the complement of their isolating region to the source. The graph
regions for those children are disjoint from the uncontracted region
of the source-component child.

Consequently the same-$k$ children have
$\sum_i(n_i-1)\leq n-1$, and each guide has at most
$|T|/2+1$ vertices. Their repeated recursion has polynomial
logarithmic aggregate maxflow input size. If $c=s$, omit the
source-component child and keep just the other children. This supplies
a self-contained main $k=1$ base. An alternative safe base is the
deterministic $k=1$ portion of AKL+22 Section 2, Steps 1--4, which
isolates entire centroid components, including $s$ in its own
component, and introduces a complement port in each child.

## 7. Scope of the audit

No probabilistic cut-threshold routine is needed by this repair.
The alternative AKL+22 algorithm has a valid disjoint-region inventory,
but its general $k>1$ Step 6 uses an exact maximum-connectivity
routine obtained from randomized cut threshold. That step is not
imported here, and the self-contained base above also avoids needing
its $k=1$ portion.

The selection proof and all relevant contractions pass this audit.
The companion construction also supplies the required inventory
argument, which independently checks as follows:

* Main children satisfy $\sum_i(n_i-1)\leq n-1$.
* The single full leaf child satisfies $n_0-1\leq n-1$.
* The two leaf children satisfy
  $(n_0-1)+(n_1-1)=n-1-\sum_{i>0,i\ne j}|W_i|\leq n-1$.
* All these same-type child guides shrink to at most $|T|/2+2$.
  The one main-to-leaf transition at the same respect parameter does
  not need to shrink the guide: solve the leaf recurrence using
  parameter $k-1$ first, then solve the main recurrence using that
  leaf bound. This adds polynomial logarithms, not an exponential in
  centroid depth.
* Uncontracted physical regions, rather than merely guide target
  sets, are disjoint. Marking every newly contracted port, including a
  port reusing the old centroid name, leaves $O(k\log n)$ marked
  vertices along a recursion branch. After parallel-edge aggregation,
  their edge inventory is charged by the vertex inventory times this
  polynomial logarithm.
* Candidate vectors are local to each call; non-source supernode
  broadcasts are performed only one recursion level upward. Thus a
  singleton centroid value is never misused as a cut value for a
  larger contracted target set, and no hidden repeated top-level
  label expansion occurs.

Accordingly the maxflow instances have aggregate size
$(m+n)\log^{O(k+1)}(n+4)$. For fixed $k$, this adds no new
subpolynomial exponent to the Gomory--Hu application. This audit is a
mathematical proof review of the specified adapter, not a claim that
the unmodified source pseudocode already supplied the repaired
contraction and inventory argument.
