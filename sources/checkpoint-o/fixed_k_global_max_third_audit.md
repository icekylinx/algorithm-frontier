# Third independent audit of the deterministic fixed-k mincut adapter

**Status: the repaired main/leaf interface passes this audit.**

This audit independently checks the construction in
`deterministic_fixed_k_tree_mincut_adapter.md`, including its actual
physical-graph inventory. It does not infer the inventory from terminal
counts. The guide tree may omit arbitrarily many physical vertices.

The audited public starting point is the centroid/pruning framework in
AKL+, [arXiv:2507.20354v1, Section 5.1]
(https://arxiv.org/html/2507.20354v1). The different source contractions,
and the reason they cannot simply be interchanged, are recorded in
`fixed_k_tree_mincut_source_interface_audit.md`. The global maximizer and
conditional source-arm contraction below are the repair being audited;
they are not attributed to the displayed public pseudocode.

## 1. Contracts and proof order

The main routine returns, for every current guide target,

\[
 \lambda_G(s,t)\leq \mu(t)\leq \lambda_{T,k}(s,t).
\]

The leaf routine has the same lower bound, and the upper bound is the
minimum cut crossing at most \(k\) guide edges and also the unique
source-leaf edge \(sp\). Both are *sandwich* contracts. An exact
ordinary source-target mincut is therefore a valid answer for either
routine, even if that cut has the wrong guide pattern.

The induction is well founded in this order:

1. prove both routines at smaller \(k\);
2. prove the leaf routine at the current \(k\), by shrinking guide size;
3. prove the main routine at the current \(k\), by shrinking guide size,
   using the already proved leaf routine.

The main-to-leaf call need not shrink the guide. There is no reverse
same-\(k\) leaf-to-main call. A typed recursion branch therefore has
only one such transition before its respect parameter decreases.

Candidate values must belong to their current physical graph. A value
for an original vertex is not automatically a value for a supervertex
which later contains that vertex. Infinity is the usual no-candidate
sentinel; each finite candidate has an actual separating-cut witness.

## 2. The uncrossing facts have exactly the required hypotheses

Let \(A\) be the target side of a cut, with \(s\notin A\). Let
\(W_i\) be a minimum isolating region for a terminal block \(B_i\),
containing that block and no other guide vertex. Distinct regions are
disjoint.

If \(B_i\subseteq A\), then \(A\cap W_i\) is an isolating cut
for \(B_i\). Submodularity gives

\[
 c(\partial(A\cup W_i))\leq c(\partial A).
 \tag{1}
\]

If \(B_i\cap A=\varnothing\), apply the same argument to the
complement, or use posimodularity, to obtain

\[
 c(\partial(A\setminus W_i))\leq c(\partial A).
 \tag{2}
\]

Both changes preserve every guide vertex's side. They may consequently
be used for a constrained guide-cut optimum, rather than only for an
ordinary minimum cut. Optimality is not needed to show nonincrease.

A different fact is needed for a restricted child. If all target-side
guide vertices belong to \(B_i\), then \(A\cup W_i\) is a feasible
isolating cut for \(B_i\), even if some vertices of \(B_i\) are
outside \(A\). Thus

\[
 c(\partial(A\cap W_i))\leq c(\partial A).
 \tag{3}
\]

Again the guide pattern is unchanged. For the source arm, hypothesis
(3) holds when the centroid is on the source side. It need not hold
when the centroid is on the target side. The repair uses precisely
this distinction.

## 3. The global maximizer covers both leaf hard cases

Let \(c\ne s\) be a centroid. Let \(T_0\) contain \(s\), and
let \(T_1,\ldots,T_l\) be the outside components of \(T-c\).
The source block is \(B_0=V(T_0)\setminus\{s\}\). The isolating
regions exclude both \(s\) and \(c\).

Complete the lower-\(k\) pruning calls and the main lower-\(k\)
call on \(T^+\), which deletes the source arm except for \(s\)
and adds \(sc\). Only then maximize the current candidate over

\[
                 V(T)\setminus\{s,c\}.
 \tag{4}
\]

The pruning family must contain the empty retained set. Bit classes
and their complements give the retain-one/prune-another property, but
that property alone is vacuous when there is only one outside branch.

Fix a minimizing feasible leaf cut \(A\), put
\(a=c(\partial A)\), and suppose its target remains unresolved:
\(\mu(t)>a\). Since \(sp\) crosses, \(p\in A\).

### 3.1 Target in the source arm

If an outside branch has a cut edge, prune it while retaining the
source arm. This removes a crossing and preserves \(sp\), contradicting
the assumption that the target is unresolved. Hence every cut edge is
incident to \(T_0\), and all outside guide vertices have the same
side as \(c\).

If \(c\notin A\), all target-side guide vertices lie in \(B_0\).
Equation (3) confines the cut to \(W_0\). It survives the restricted
source child which contracts \(V\setminus W_0\) to the source.
Dropping the old source-arm attachment to the centroid cannot increase
the cut count, and it does not delete \(sp\). The full source child
also preserves this case, using (2) on the outside regions.

If \(c\in A\), every outside guide target lies in \(A\). On
\(T^+\) the cut crosses exactly \(sc\), so for \(k\geq2\) the
earlier main lower-\(k\) call bounds every outside candidate by \(a\).
The unresolved source-arm target has candidate greater than \(a\).
The global maximizer (4) must therefore lie in the source arm. The
algorithm makes only the full source child, retaining \(s\) separately
and contracting \(c\) together with the outside regions. Equation
(1) makes that contraction safe.

This is the cut pattern lost by the old unconditional restricted
source-arm contraction. The new maximizer rule specifically prevents
that loss.

### 3.2 Target in an outside branch

Let \(t\in T_i\). A cut-bearing outside branch other than \(T_i\)
can be pruned while retaining \(T_i\), so no such branch remains in
an unresolved case.

Let \(q_0\) count crossings incident to the source arm, including
its old attachment to \(c\). If \(c\notin A\), replacing the
source arm by \(sc\) removes at least one crossing and adds none.
If \(c\in A\) and \(q_0\geq2\), it removes at least two and
adds one. Both cases were handled by the main lower-\(k\) call.

Consequently an unresolved case has

\[
 c\in A,\qquad q_0=1,
 \qquad\text{all outside crossings lie in the branch }T_i.
 \tag{5}
\]

There is at least one crossing in \(T_i\), since otherwise
\(T^+\) has just its one source edge crossing and is already handled.
Because \(sp\) is the only source-arm crossing, every guide vertex
in \(B_0\), and every other outside branch, lies in \(A\).

Pruning \(T_i\) gives a lower-\(k\) leaf cut for each source-arm
target; the empty retained set supplies this call. A bit separator
retains any chosen other outside branch while pruning \(T_i\).
Hence every candidate outside \(T_i\cup\{s,c\}\) is at most
\(a\). The unresolved target has a larger candidate. The global
maximizer is forced into \(T_i\).

The selected outside child thus uses the correct branch. By (1), the
regions for \(B_0\) and all other outside branches can be moved
wholly to the centroid side. They can be contracted together with
\(c\), while \(s\) stays separate. The old one source-arm crossing
becomes the new mandatory edge \(sc'\). The branch's remaining
crossings are unchanged, so the child satisfies the leaf constraint.

This proves both directions needed by the branch decision: a full
source-arm child cannot discard an unresolved outside target, and a
restricted source-arm child is never relied upon for an unresolved
source-arm cut that places the centroid opposite the source.

## 4. Main-routine broadcasting is necessary and valid

If all cut edges lie in the source arm, all outside branches are
uniformly on the centroid side. Equations (1)--(2) permit contracting

\[
                    \{c\}\cup\bigcup_{i>0}W_i
 \tag{6}
\]

to the non-source child target \(c'\). An outside parent target is
represented by \(c'\), even though it is no longer an individual
child guide vertex. A valid child source--\(c'\) cut separates the
parent source from every parent target in (6). Broadcasting its value
is therefore valid and is needed to prove the main contract for these
outside targets.

This broadcast must use the child's *call-local* returned candidate.
The exact parent value \(\lambda_G(s,c)\) only separates the source
from the single centroid; it does not automatically separate the
source from all vertices in (6).

When a child contracts a region to its source, no analogous broadcast
is justified or performed. Its surviving targets still receive valid
answers. When \(c=s\), the source-arm child is absent and the
outside-region children suffice.

The other main cases are exhaustive: a single cut-bearing outside
branch uses (3); multiple outside branches use pruning; and a cut
bearing both the source arm and one target branch either loses a
crossing on \(T^+\), or becomes a valid leaf cut on \(T^+\).

## 5. Parameter-one bases are valid with Steiner vertices

For a leaf guide, crossing \(sp\) and at most one guide edge puts
every non-source guide vertex on the opposite side from \(s\).
A single set-terminal mincut therefore computes the constrained leaf
value for all targets. Physical vertices omitted by the guide remain
free on either side. Summing physical edges along the guide would not
have this property and is not used.

For the main routine with \(k=1\), each feasible cut has its unique
guide crossing in one centroid branch. The same-\(k\) children and
the exact centroid cut handle precisely these single-branch cases.
The source-arm child uses the broadcast from Section 4 when the target
is outside the source arm. No lower-\(k\) or leaf transition is
needed. Guide size shrinks, so this is a complete recursion, not an
appeal to a missing parameter-zero routine.

Constant-size guide bases may compute ordinary source-target mincuts
directly. This is compatible with both sandwich contracts and adds
only a constant number of maxflow inputs, regardless of the number
of Steiner vertices.

## 6. Actual physical inventory, including edges

Write \(n\) for the physical vertex count at a call, including
existing supervertices. A child obtained by contracting \(X\) has
\(n_{\rm child}-1=n-|X|\).

For the main routine, the source-arm child has

\[
 n_0-1=n-1-\sum_{i>0}|W_i|,
\]

and the outside child \(i\) has \(n_i-1=|W_i|\). Their sum is
\(n-1\). If \(c=s\), the outside children give an inequality in
the same direction.

For the leaf routine, a source-arm maximizer produces only one child.
An outside maximizer \(j\) produces the restricted source child and
the selected outside child, whose masses sum to

\[
 |W_0|+
 \left(n-1-|W_0|-\sum_{i>0,\ i\ne j}|W_i|\right)
 \leq n-1.
 \tag{7}
\]

Their uncontracted physical regions are disjoint. Arbitrarily many
uncovered Steiner vertices can survive in the outside child, but none
of them also survive in the restricted source child. Including the
centroid in the contracted set is what gives the \(n-1\) inventory.

The edge argument requires an additional invariant, not literal edge
disjointness of child graphs. Mark every newly created supervertex,
even when it reuses an old vertex's name. Keep these marks throughout
the recursive computation. A root edge with two still-unmarked
endpoints survives as such in at most one same-\(k\) child, because
the children have disjoint uncontracted regions. A crossing edge can
occur in two children, but then it is incident to a marked supervertex
in each affected copy and is charged separately.

Every typed branch has \(O(k\log N)\) contraction steps: logarithmic
same-\(k\) guide depth, at most one same-\(k\) main-to-leaf
transition, and at most \(k\) respect-parameter phases. After
combining parallel edges, the number of edges incident to marked
vertices in an instance with \(n_*\) vertices is at most

\[
                         O(n_* k\log N).
 \tag{8}
\]

Thus the aggregate vertex inventory pays for these edges with only a
polynomial logarithm. Edges whose endpoints remain unmarked are
charged to the aggregate root-edge inventory. This handles the
potentially duplicated crossing edges without assuming that the
physical graph has bounded degree or that isolating regions cover it.

All children have guide size at most \(|T|/2+2\). Above a fixed
base threshold this gives a fixed-factor decrease. There are
\(O(\log N)\) lower-\(k\) pruning calls per node. The stated
recurrences

\[
 H_k\leq C L(1+L H_{k-1}+F_{k-1}),\qquad
 F_k\leq C L(1+L F_{k-1}+H_k)
\]

with \(L=C\log(N+4)\) therefore yield
\(F_k,H_k\leq L^{O(k+1)}\). They can first be applied to vertex
mass and unmarked-edge mass; (8) then accounts for marked-edge work
over the complete recursion. This avoids repeatedly reclassifying
old supervertices as new unmarked root vertices.

Broadcasting is only one level upward and has linear guide-size cost
per family of same-\(k\) children. The lower-\(k\) families add
their already charged logarithmic factor. The deterministic isolating
cut reduction adds another polynomial logarithm. Consequently total
exact-flow input size and non-flow work are

\[
                    (m+n)\log^{O(k+1)}(N+4).
\]

Every current recursive graph is a quotient of the physical root
graph. Each combined capacity is bounded by the root's total capacity;
polynomially bounded integer capacities remain polynomially bounded.

## 7. Outcome and retained scope

No counterexample remains in the four designated audit targets:
global-max leaf selection, the two-child uncontracted inventory,
Main contracted-target propagation, and the parameter-one bases.
The repaired fixed-\(k\) adapter is a deterministic construction
with a fixed polynomial-logarithmic overhead for constant \(k\).

This audit closes that particular Gomory--Hu dependency. It does not
replace the separate proof imports for the strong decremental forest,
packing, skeleton, finite arithmetic, or the exact flow engine.
