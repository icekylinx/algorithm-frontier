# Explicit sequential short-path packing for recursive expander construction

**Mathematical implementation lemma, 24 October 2026.** The sequential
construction does not need to simulate the distributed scheduling of the
nearly maximal flow subroutine in Chang--Saranurak,
[arXiv:2007.14898v1](https://arxiv.org/pdf/2007.14898), Appendix D.
An elementary decremental breadth-first-search implementation returns an
EXACT maximal packing of short vertex-disjoint paths. Its work replaces
the distributed-round bound, while its stronger output satisfies the
same interface used in Lemmas D.9, D.11, and D.12.

This note concerns construction of the hierarchy and its matching
embeddings. It is independent of the threshold token router used in
the 5/6 matching composition.

## 1. One source set and one sink set

Let $G=(V,E)$ be an unweighted undirected multigraph with explicit
edge IDs, $n=|V|$, and $m=|E|$. Let $S,T\subseteq V$
be disjoint, and let $d\geq1$ be an integer. There is a
deterministic algorithm returning vertex-disjoint $S$-to-$T$
paths of length at most $d$, such that no further such path is
vertex-disjoint from all returned paths. Its total work is

$$
O((n+m)(d+2))
 \tag{1}
$$

up to the stated word-operation cost. The output has at most
$n$ original vertex occurrences. There is NO exceptional set of
leftover vertices.

### Algorithm

Add a supersource $s_0$ and supersink $t_0$. Replace each
undirected edge by its two directed orientations, keeping the
original edge ID. Add arcs $s_0\to s$ for $s\in S$, and
$t\to t_0$ for $t\in T$. These attachment arcs have no
reverse orientation.

Maintain exact distances from $s_0$, truncated after depth
$d+2$, under deletions by an Even--Shiloach breadth-first-search
tree. Whenever $t_0$ has distance at most $d+2$, extract its
parent path. Delete its two attachment arcs from the reported path,
save the resulting original-edge path, and delete EVERY original
vertex on it from the maintained graph. Implement a vertex deletion
by deleting its incident arcs and attachment arcs. Continue until
$t_0$ is beyond the depth cap or unreachable.

The shortest parent path is simple. Its internal original segment
contains no additional source or sink vertex: such a vertex would
give a shorter supersource or supersink route. This observation is
not needed for maximality, but verifies that each returned path is a
legitimate matching path with one selected source and sink.

### Correctness and work

All extracted paths have at most $d$ original edges. Every
selected original vertex is deleted before the next query, so paths
are vertex-disjoint. At termination the residual graph contains no
$S$-to-$T$ path of length at most $d$; any path disjoint
from the output would still be a residual path. This is exactly the
claimed maximality.

The directed augmented graph has $O(n+m)$ arcs. Each is deleted
at most once. In the truncated decremental BFS implementation,
distance labels only increase and have at most $d+3$ distinct
finite/capped values. For each vertex and each label, scan its
incoming adjacency until finding a predecessor at the preceding
label, or increase its label and restart the scan. When a parent
arc or a predecessor label becomes invalid, queue the affected
vertex and finish all necessary increases before the next query.
Each arc is scanned at most a constant number of times per label.
Initialization and updates therefore take (1). This is the usual
Even--Shiloach accounting, supplied here to specify actual sequential
work rather than infer it from a distributed round count.

Extracted paths use disjoint original vertices, so their total
extraction and vertex-deletion list work is $O(n+m)$. If
$d\geq n$, one may cap the original path depth at $n-1$;
every simple path is already below that bound. Isolated input
vertices are retained at their actual $O(n)$ bookkeeping cost.

The source Lemma D.8 permits a leftover set $B$ of cardinality
at most $\beta n$. Our algorithm satisfies its conclusion for
EVERY $\beta>0$, using $B=\varnothing$. The subroutine's
work has no $\beta^{-1}$ factor.

## 2. Several colors in one packing round

Let $(S_1,T_1),\ldots,(S_k,T_k)$ be the disjoint terminal
pairs used in source Lemma D.12. Process the colors in a fixed order.
For color $i$, run Section 1 on the graph after removing every
vertex already used by earlier colors, using its still-present
source and sink vertices. Delete all vertices of the new paths as
well before moving to the next color.

The union $\mathcal P$ is vertex-disjoint across ALL colors,
and its paths have length at most $d$. For each color, there is
no length-$d$ or shorter path in the final residual graph:
maximality held when that color finished, and later processing only
deletes more vertices. A terminal removed by an earlier color is
already a member of $V(\mathcal P)$, so no unaccounted leftover
terminal is introduced.

Thus this one-round output satisfies the interface used in source
Lemma D.12 with every $B_i=\varnothing$. Its congestion is
literally ONE, independent of $k$. Initializing an actual
decremental BFS instance for each color costs

$$
O(k(n+m)(d+2)).
 \tag{2}
$$

This $k$ is a construction-work factor only. It does not
multiply path length, vertex congestion, or the later embedding
quality. The same graph and original-ID tables can be used with
generation marks; even a full actual-size scan per color is paid
by (2).

### 2.1 A complete empty-initial-cut progress-or-cut contract

The version with NO prior cut has a short direct proof. Let
$M=\sum_i|S_i|$, assume $|S_i|\leq|T_i|$, and let
$0<\psi\leq\Delta$. Choose
$d=\lceil c\Delta\psi^{-1}\log(n+2)\rceil$, with a
sufficiently large absolute constant $c$. Perform Section 2's
simultaneous packing. If

$$
|\mathcal P|\geq
                 \frac{\psi M}{100\Delta(d+1)},
 \tag{2a}
$$

return those paths. Otherwise put $W=V(\mathcal P)$. Then
$\Delta|W|<\psi M/100$. Remove the incident edges of $W$
but retain its vertices as isolated slots. Every original terminal
set is still a subset of this full vertex universe, and every
same-color source/sink distance is greater than $d$.

The following elementary distance-ball construction supplies a cut.
For one pair of nonempty terminal sets at distance greater than
$d$, their radius-$\lfloor d/2\rfloor$ balls are disjoint;
at least one ball has cardinality at most half the current universe.
Among its successive radii choose the minimum growth ratio. The
product of those ratios is at most $n$, so one radius has
relative growth $O(\log(n+2)/d)$. Its boundary is at most
$\Delta$ times the new layer cardinality. This gives a cut
separating the two sets with sparsity
$O(\Delta\log(n+2)/d)$. All radii, sizes, and candidate ratios
are obtained by BFS and integer comparisons. An empty terminal
set requires no new cut.

For several colors, start with an empty removed union and process
the pairs in order. In the graph induced by the remaining universe,
apply the preceding construction to the surviving parts of that
pair, and add its returned smaller-side cut to the removed union.
If the union first reaches one third of the original universe,
return it or its complement, whichever is smaller. Its cardinality
lies between one third and one half: immediately before the last
addition the union had size below one third, and the added set was
at most half the remainder. If no such crossing occurs, return the
final union.

The accumulated boundary is at most the common small sparsity
times the accumulated size; complementation at the first crossing
loses at most a fixed factor. If the final union is unbalanced,
it contains at least $\min\{|S_i|,|T_i|\}=|S_i|$ terminals
from every pair. To see this, if a previous union removed $a$
and $b$ terminals of the two sides, the next separating cut
contains at least $\min\{|S_i|-a,|T_i|-b\}$; adding
$a+b$ makes the total at least the original minimum. All pairs
are disjoint, so an unbalanced final cut has cardinality at least
$M$.

Choose the constant in $d$ so that this cut has sparsity at
most $\psi/4$ before restoring the edges incident to $W$.
Restoration adds at most $\Delta|W|<\psi M/100$ boundary
edges. For an unbalanced cut, $|C|\geq M$ pays this directly.
For a balanced cut, $|C|\geq n/3$ and $M\leq n/2$,
so $M\leq3|C|/2$ pays it with the same constant slack.
The final actual-host cut has sparsity at most $\psi/2$.

We have therefore proved, with no original-terminal clipping:
either (2a) vertex-disjoint short paths are returned, or an actual
cut of sparsity at most $\psi/2$ is returned that is balanced
or contains at least $|S_i|$ terminals of every color. Its
work is $O(k(n+m)(d+2))$. This is the clean empty-prior-cut
interface that can be called on an induced residual host by an
explicit outer adapter.

## 3. Simultaneous half-matching with fresh cuts

Use the complete empty-prior-cut interface of Section 2.1 and the
explicit repetition/union wrapper in
[sequential-fresh-cut-matching-adapter.md](sequential-fresh-cut-matching-adapter.md).
The GENERAL nonempty initial-cut implementation in the source's
abbreviated Lemma D.12 proof is not used. That proof restricts its
host to the complement of an old cut while still writing the
original terminal sets; the fresh-cut wrapper avoids that interface
rather than assuming the missing clipping charge.

For one simultaneous matching request, retain the original terminal
sets and repeat Section 2.1 on the FULL host, updating only matched
endpoints in those sets. Remove a color from the active requests
once it has received at least half its original source count. A
successful packing round reduces the active unmatched source total
by a fixed fraction. A cut round either is balanced or covers at
least half the original source count of every unfinished request.
With $b=\min_i|S_i^0|/n$, the number of rounds is
$$
d=O(\Delta\psi^{-1}\log(n+2)),\qquad
 R=O(\Delta^2\psi^{-2}\log(n+2)\log(2/b)).
 \tag{3}
$$
The explicit simultaneous embedding has dilation at most $d$,
vertex congestion at most $R$, and work at most
$$
O(k(n+m)(d+2)(R+1)).
 \tag{4}
$$
A color's returned paths are a matching because only unmatched
endpoints are used. Different rounds may reuse host vertices;
the round count, not the number of colors, bounds that reuse.

In outer KKOV matching round $j$, call this routine on the FULL
host with cutoff $\psi/(16j^2)$. Old failed cuts are bookkeeping
sets and are not removed from the host. Keep the union of fresh
failure cuts, stopping the weak cut routine at its fixed small
balance threshold. The convergent sum $\sum_j j^{-2}$ bounds
that union's actual sparsity, including overlapping cuts and a
possible final complementation. Every failed block contributes a
fixed fraction of its own terminals to the union. The surviving
blocks receive the required half-matchings. Every continuing game's
balanced cut has sparsity at most $1/8$, so the corrected argument in
[half-matching-entropy-progress.md](half-matching-entropy-progress.md)
gives constant-times-$n$ entropy progress. The source's printed
threshold-$1/2$ half-matching calculation is not used. Intermediate
game graphs retain every parallel matching-round occurrence as a
distinct edge ID.

There are $O(\log n)$ outer rounds, so their changing cutoffs
cost only fixed polylogarithmic factors in (3)--(4). The formula
for the cutoff is executable without knowing the hidden constant
in the round bound. In the hierarchy $b=\Omega(1/k)$, so the
only quality dependence on the number of colors is
$\log(2/b)=O(\log(k+2))$. The explicit factor $k$ in
construction work never enters the embedding quality.

## 4. Single-color covering matchings without residual exceptions

For the covering-matching step, the same replacement may be used in
source Lemma D.9. One can retain any positive allowed leftover
parameter and stop at its threshold. Alternatively, stop only when
no source remains, and return a cut whenever a round has too small
a packing. The latter has no exceptional leftover set.

Here is the work and progress check for the stronger version. In a
round with live unmatched sets $S_i,T_i$, either the packing has
size at least
$|S_i|/(d^2\log(n+2))$, or discard that round's tentative paths
and use the source distance-ball cut lemma after isolating all their
vertices. The number of isolated vertices is less than
$(d+1)|S_i|/(d^2\log(n+2))$. Restoring their incident edges
increases cut sparsity by at most this number times $\Delta/|S_i|$,
which is absorbed by choosing the fixed constant in
$d=O(\Delta\psi^{-1}\log(n+2))$ sufficiently large.

In a successful round, delete only the matched endpoints from the
terminal lists; the next round again uses the full original host.
Each round contributes vertex congestion at most one. Successful
rounds reduce $|S_i|$ by a fixed reciprocal polynomial in
$d$ and $\log n$, so there are
$O(d^2\log^2(n+2))$ rounds before every source is matched or a
cut is returned. This gives fixed-polynomial dependence on
$\Delta,\psi^{-1},\log n$ for both output quality and work.
If the host is an expander with sparsity strictly above the requested
cut threshold, the nonempty-cut alternative is impossible, so the
matching saturates all sources.

Using this stronger single-color version in the virtual-hierarchy
construction can make its tiny uncovered set $B$ empty. Keeping
the more conservative source leftover allowance is also valid and
does not change any envelope.

## 5. The hierarchy work recurrence

The new coarse merge in
[virtual-expander-hierarchy-reconstruction.md](virtual-expander-hierarchy-reconstruction.md)
uses a polynomial number of exact rational matrix operations on
$k$ blocks. Section 2 supplies the matching work on actual host
records. The base cut player there has at most $Ck^5\lambda_{\rm cap}^2$
actual vertices and polynomial work in $k$ and $\log n$. Thus local construction work has
the form

$$
(n+m)k^{c_1}\operatorname{poly}
            (\Delta,\psi_{\rm cut}^{-1},\log n),
 \tag{5}
$$

for one absolute exponent $c_1$. It is not a separate factor
$k^{c_1}$ on every recursive branch.

The polynomial in (5), and the final envelope (7), include the FULL
bit work of temporary exact rationals. The PSD matrices may use
$\operatorname{poly}(k,\log n,\log\psi^{-1})$-bit numbers.
The separate leaf moment computations can use the larger
$\operatorname{poly}(k,\psi^{-1},\log^{O(p)}n)$-bit numbers,
because their explicit lazy-walk length depends polynomially on the
leaf's inverse expansion. Their stated polynomial bit work is charged
to the same local construction envelope. These numbers are local
preprocessing state and are not tested against
a backend's smaller numerical length/gradient-label cap. Only finite
graph records, source vertex/edge IDs, and explicit unweighted path
lists leave this preprocessing routine. Those labels have
$O(\operatorname{poly}(\log n+\log\psi^{-1}))$ bits. The
overall guarded WORK allowance must pay for the temporary multiword
operations; treating them as constant-time arithmetic would not prove
(7).

Each simultaneous game invokes recursive cut routines on at most
$k$ disjoint terminal graphs of size $O(n/k)$, for
$O(\log n)$ game rounds. A fixed number of balance-improvement
calls multiplies this by another fixed factor. The total matching-
graph edge count per recursive family is $O(n\log n)$.
For recursion depth $d$, a safe work recurrence therefore has
the form

$$
T(n,d)\leq\operatorname{poly}(\log n)
       \sum_{i\leq k}T(O(n/k),d-1)
       +nk^{c_2}\operatorname{poly}
             (\Delta,\psi_{\rm cut}^{-1},\log n)
       +\text{explicit output-list work}.
 \tag{6}
$$

At every NONROOT call the cut threshold is an absolute constant
and the current matching-graph host has degree $O(\log n)$.
Only the root pays the original expander's inverse sparsity.
The virtual embedding is flattened only once as proved in the
linked hierarchy note. With $k$ within a fixed factor of
$n^{1/p}$, the recursion has depth $O(p)$, and (6) gives

$$
n^{1+O(1/p)}
                  \operatorname{poly}(\psi^{-1})
                  \log^{O(p)}n.
 \tag{7}
$$

All polynomial exponents outside $p$ are fixed. The same
envelope pays for the explicit root-embedding lists and for the
fixed-polynomial leaf preprocessing. No bound here charges an
exponential local search to zero distributed rounds.

Equation (7) is a construction-work statement for the reconstructed
hierarchy. It uses the corrected threshold-$1/8$ half-matching
entropy argument, the explicitly
proved empty-cut packing, and the fresh-cut adapter; it does not use
the ambiguous nonempty-initial-cut proof interface. It does not assert the
correctness of the full routing query recursion. That recursion,
its token loads, and its path reconstruction are separate interfaces.
