# A quantified Gomory--Hu transfer of the strong forest

**Research proof assembly, 25 October 2026.** This note completes the
application interfaces that are deliberately kept separate in
[separated-metric-forest-and-strong-sssp.md](separated-metric-forest-and-strong-sssp.md). It uses a strong
decremental forest with overhead

$$
E(N)=\exp O\bigl((\log(N+4))^{7/8}
                         (\log\log(N+16))^{1/8}\bigr).
 \tag{1}
$$

The resulting research theorem is a deterministic exact Gomory--Hu tree
for a general undirected graph with polynomially bounded positive integer
capacities, in

$$
O(n+m)+(m+1)E(m+n).
 \tag{2}
$$

As usual, constants in the exponent absorb a fixed power of $E$.
This is a proof assembly from named public constructions and the new
strong-forest construction, not an implemented or externally certified
algorithm. The public Gomory--Hu theorem already has almost-linear
running time. The proposed gain concerns its explicit subpolynomial
factor. The baseline comparison includes a public parameter retuning to
$62/63$, rather than using only the printed $83/84$ forest
exponent.

**Construction status.** Sections 2--8, including the rooted forest,
degree adapters, terminal sparsifier, finite arithmetic, and Li
skeleton, have independent construction audits. The remaining
fixed-parameter mincut interface is now supplied by the new global-max
leaf construction in [deterministic-fixed-k-tree-mincut-adapter.md](deterministic-fixed-k-tree-mincut-adapter.md).
Its correctness and aggregate inventory have separate independent
audits. Thus no unresolved application interface remains in (2), beyond
the explicitly named component constructions in the strong-forest
proof. This status is a completed mathematical proof assembly, not an
external certification of a newly established research theorem.

The construction here avoids a physical zero-length super-source. It
also avoids feeding an arbitrary long rational expansion into the
shortest-path oracle. Both distinctions matter to the claimed bound.

## 1. The application dependency chain

Write AKL+ for Abboud, Kyng, Li, Panigrahi, Probst Gutenberg, Saranurak,
W. Yuan, and W. Yuan,
[arXiv:2507.20354v1](https://arxiv.org/html/2507.20354v1).
The public components used are identified below, rather than treated as
one unspecified $m^{1+o(1)}$ black box.

| Component | Source location | Cost charged here |
|---|---|---|
| Implicit Steiner packing and terminal sparsifier | AKL+ Section 4.1 and its augmented dynamic trees in Section 4.2 | A fixed power of the strong-forest overhead, times the input size and a polynomial logarithm |
| Deterministic unweighted skeleton | Li, arXiv:2106.05513v2, Theorem 1.5 and Sections 3.4--3.5; AKL+ Theorem 4.22 uses an earlier version | $F_L=\exp O(U^{5/6}h^{O(1)})$ in both work and reciprocal skeleton scale |
| Tree packing | AKL+ Theorem 4.23 | $\widetilde O(m_H\lambda_H)$, with $\lambda_H\le F_L$ at constant accuracy |
| Mincuts respected by one guide tree | New global-max leaf adapter in [deterministic-fixed-k-tree-mincut-adapter.md](deterministic-fixed-k-tree-mincut-adapter.md), using the public centroid framework | A fixed polynomial logarithm times deterministic exact maxflow, with proved aggregate actual-instance inventory |
| Partial to full single-source mincuts | AKL+ Algorithm 8 | $O(\log(nW))$ partial calls |
| Terminal expander decomposition | AKL+ Appendix A | Work and structural factor $\exp O(U^{4/5}h^{O(1)})$ |
| Terminal selection and cut decomposition | AKL+ Section 6 | Fixed powers of the preceding factors, of $\psi^{-1}$, and of logarithms |
| Final Gomory--Hu recursion | AKL+ Lemma 6.32 and Claim 6.33 | Polylogarithmic total instance inventory |

Here $U=\log(N+4)$, $h=\log(U+4)$, and $N$ is a common
upper bound on the actual record inventories in the application. It is
polynomially related to the original input size. A small recursive call
is charged by its actual size, never padded to $N$.

The deterministic exact maxflow used in this table can be the
independently audited public $4/5$ retuning in
[public-dual-reoptimization.md](public-dual-reoptimization.md) and
[public-dual-uniform-wrapper-audit.md](public-dual-uniform-wrapper-audit.md). The static $4/5$ flow result
is not counted as a new separation in this application.

## 2. A cut-preserving bounded-degree input for each packing call

The strong-forest proof requires bounded physical degree. A degree bound
on the initial Gomory--Hu input would not suffice, because subsequent
cut contractions create high-degree vertices. We therefore perform the
following linear-size expansion separately at the entrance to each
terminal-sparsifier or guide-packing call.

Let the current undirected graph be $G=(V,E,c)$, with terminal set
$S$. Work on its connected components; if distinct terminals lie in
different components, the zero terminal cuts are handled directly. For
each vertex $v$, replace its $d(v)$ edge incidences by ports in a
path. Attach each original edge to its corresponding port. Connect
successive ports by edges of capacity

$$
C=1+\sum_{e\in E}c_e.
 \tag{3}
$$

Use one permanent designated port $q(v)$ for each original vertex.
Degree-zero vertices receive an isolated designated node; degree-one
vertices need no connector. The resulting graph $G^\circ$ has
maximum degree three and $O(n+m)$ vertices and edges. Its capacities
remain positive polynomially bounded integers.

**Cut preservation.** Every original cut lifts by putting all ports of
a vertex on the same side. The lifted cut has the same capacity. Every
cut that splits a port path has capacity at least $C$, whereas the
minimum cut separating any two original terminals has capacity at most
$\sum_e c_e<C$. Consequently,

$$
\lambda_{G^\circ}(q(u),q(v))=\lambda_G(u,v)
 \quad (u,v\in S),\qquad
 \lambda_{G^\circ}(q(S))=\lambda_G(S).
 \tag{4}
$$

Run the terminal-sparsifier construction on
$(G^\circ,q(S))$. Its output has only the designated terminals as
vertices. Rename them back to $S$. Its lower terminal-cut guarantee
uses (4). Its upper bound for a cut $X\subseteq V(G)$ follows by
applying that guarantee to the whole-fiber lift of $X$; the lift
has exactly $c_G(\partial X)$ capacity. Thus the output satisfies
the original terminal-sparsifier contract on the current general-degree
graph. The rest of the Gomory--Hu recursion can operate on its ordinary
unexpanded graphs.

This per-call expansion is intentional. No claim is made that a single
initial expansion keeps all recursively contracted inputs bounded in
degree. The public recursive inventory bound pays for the linear-size
expansion at every actual call.

All physical null contractions described below take place relative to
this bounded-degree $G^\circ$, not relative to the original graph
whose degrees may be arbitrarily large.

## 3. The rooted multi-source and explicit-label interface

For a fixed nonempty terminal set $S$ in a connected positive-length
graph, the forest oracle used here maintains the following objects.

* A flat forest $F$ whose edges map to current physical edges.
* A permanent canonical node $\iota(v)$ for every physical vertex.
* A stable physical-image map for every auxiliary occurrence.
* An explicit upper distance estimate $\widehat d(v)$ satisfying
  $d(v,S)\le\widehat d(v)\le(1+\epsilon_0)d(v,S)$.
* In the component of each source-reachable canonical vertex, exactly
  one **canonical** member of $S$. The path to it has physical
  length at most $(1+\epsilon_0)d(v,S)$.
* Total work, forest changes, vertex/edge occurrence congestion, and
  explicit distance-label changes at most $mE^{O(1)}$.

Unreachable canonical vertices are retained as permanent isolated nodes.
An auxiliary alias of a source is not another canonical source.

The construction-level proof is
[multisource-rooted-approximate-ball-forest.md](multisource-rooted-approximate-ball-forest.md). It exposes BGS's
nested monotone ES candidates, selects the minimum label, and breaks a
tie in favor of the smallest distance scale. A positive dummy-source
shortcut cannot be selected: if it won, a smaller-scale candidate would
attain the same label. Every selected nonsource parent is therefore a
real positive-length original or hopset edge along which the global
selected label strictly decreases. This gives one source per finite
component. KMG's independent tree substitutions preserve that component
property while flattening the hopsets.

The explicit labels come from those candidate heaps. We do not obtain
them by recomputing all root-path lengths whenever a forest edge moves.
Every candidate-label or selected-parent change is already charged by
the approximate-ball construction, with an additional polynomial
logarithmic heap cost. This is essential: forest recourse by itself
would not bound the number of vertex-distance updates.

At the end of a settled update, both forest and label changes are
reported. Since the current physical graph is $G^\circ$ of degree
three, one changed label alters only a constant number of the helper
edge keys used in Section 5.

## 4. Length increases through fixed positive-length copies

We first give this adapter for positive integer target lengths in
$[1,N^b]$, where $b$ is any fixed constant. Section 7 supplies
exactly this range to the application.

Fix a small constant $\eta>0$. Choose an integer $D\ge4/\eta$,
put $a_0=D$, and define

$$
a_{j+1}=a_j+\max\{1,\lfloor\eta a_j\rfloor\}.
 \tag{5}
$$

Continue until $a_Q\ge DN^b(1+\eta)$. The ratio of consecutive
terms lies between $1+\eta/2$ and $1+\eta$. Hence
$Q=O(\eta^{-1}\log N)$, and every threshold is a polynomially
bounded integer.

For every physical edge $e$, preallocate one edge copy at every
threshold $a_j$. At current target length $\ell_e$, retain
precisely the copies with $a_j\ge D\ell_e$. Increasing
$\ell_e$ only deletes copies. The minimum live copy satisfies

$$
D\ell_e\le \min\{a_j:a_j\ge D\ell_e\}
                 \le(1+\eta)D\ell_e.
 \tag{6}
$$

There are $O(mQ)$ copy deletions over the entire length-increase
sequence. A target update that crosses no threshold makes no structural
change. Locating its threshold costs a polynomial logarithm even when
the numerical update sequence is much longer than $mQ$.

### 4.1 Fixed port trees restore degree three

The parallel copies would raise physical degree to $O(Q)$. Replace
each physical vertex's copy incidences by a fixed balanced binary port
tree, retaining its root as the canonical representative $q(v)$.
Every original copy attaches to a separate leaf. Give port-tree edges
length one, and give a real copy of threshold $a_j$ length
$Ha_j$, where

$$
H\ge c_0\eta^{-1}\log(Q+2)
 \tag{7}
$$

is an integer. The resulting graph has maximum degree three and actual
size $O(mQ+n)$. Every length is a positive integer of polynomial
size. The fixed port trees are never deleted. Only real copies are
deleted.

Projecting a proxy walk to the physical graph discards its port edges
and maps a real copy to its physical edge. Consequently its proxy
length divided by $HD$ is at least the physical target length of
the projected walk. Conversely, lift a simple physical shortest path
using the cheapest live real copy at each edge and the corresponding
port-tree paths. The extra connector length per physical edge is
$O(\log Q)$, and its real length is at least $HD$. Equations
(6)--(7) therefore give, for canonical vertices,

$$
d_G(u,v)\le \frac{d_{\rm proxy}(q(u),q(v))}{HD}
           \le(1+O(\eta))d_G(u,v).
 \tag{8}
$$

Apply the strong forest to this decremental proxy, with source set
$q(S)$ and a suitably smaller internal accuracy. Its explicit
labels divided by $HD$ give the estimates needed in Section 3.
The forest's real-copy edges project to physical edges. Its port edges
become typed true-null edges.

### 4.2 Projecting back without moving canonical nodes

Keep internal typed-null edges until the final physical projection.
Among proxy canonical vertices, only $q(v)$, one for each physical
vertex $v$, is a distinguished final canonical vertex. All other
proxy canonical vertices become ordinary auxiliary occurrences.

Every connected true-null component has one physical image and contains
at most one distinguished final canonical node. Contract that component,
choosing this node as its representative when it is present. Otherwise
use a deterministic auxiliary representative. When a component splits,
the piece containing a distinguished node keeps it. This is the
root-only null-quotient construction of the strong-forest proof.

An original edge has $O(Q)$ real-copy types, so simultaneous physical
edge and vertex occurrence counts increase by only a polynomial
logarithm. The current physical graph is the degree-three expansion of
Section 2. Rebuilding the incidences of an affected physical null fiber
therefore costs a fixed power of its occurrence bound, rather than an
unbounded original degree. All map changes, forest changes, and label
changes remain bounded by $mE^{O(1)}$.

This also preserves the source-root property. Contracting existing null
edges cannot merge different forest components. There is still only one
distinguished canonical source in each relevant component.

## 5. A Steiner helper graph without a zero-source assumption

Use the multi-source forest of Section 3 directly. Give its edges
**helper length zero**, while retaining their positive physical lengths
in the augmented dynamic-tree records. Add, for every physical edge
$e=uv$, a helper edge between $\iota(u)$ and $\iota(v)$
with key

$$
\widehat d(u)+\ell_e+\widehat d(v).
 \tag{9}
$$

Let $A$ be this helper graph and $M$ a minimum spanning forest
of $A$. A minimum spanning forest contains all zero-length edges of
$F$: they are acyclic, and every additional helper edge has positive
key. After contracting each relevant component of $F$, its
nonzero edges form a minimum spanning tree on the canonical sources.
Let $M^S$ be the minimal subtree connecting those canonical sources.

Here and below an auxiliary component containing no canonical physical
vertex may remain in the maintained forest. It has no role in $M^S$
and does not affect the argument.

### 5.1 Helper cost versus the minimum Steiner cost

For any bipartition $(B,S\setminus B)$, take a shortest physical
path between the two parts. Along this path, the forest's canonical
source assignment changes sides at some physical edge $uv$.
For that edge, using the prefix to one endpoint terminal and the suffix
to the other gives

$$
\widehat d(u)+\ell(uv)+\widehat d(v)
       \le (1+\epsilon_0)\operatorname{dist}_G(B,S\setminus B).
 \tag{10}
$$

Thus the helper graph's minimum crossing key is no larger than the
corresponding metric-closure minimum crossing key times
$1+\epsilon_0$. Equivalently, at each Kruskal threshold its terminal
components can only coalesce earlier than in that rescaled metric
closure. Integrating the component count, or applying the ordinary MST
cut-exchange argument, gives

$$
\operatorname{key}(M^S)
 \le (1+\epsilon_0)\operatorname{MST}_{d_G}(S)
 \le 2(1+\epsilon_0)\operatorname{OPT}_{\rm Steiner}(G,S).
 \tag{11}
$$

### 5.2 The physical cost of the maintained Steiner tree

For every nonzero helper edge, add the forest paths from its endpoints
to their unique canonical roots. Their physical length is at most
$(1+\epsilon_0)(\widehat d(u)+\widehat d(v))$. The union of
these paths and the physical helper edges contains $M^S$, possibly
counting some physical edges more than once. Therefore

$$
\operatorname{len}_{\rm physical}(M^S)
 \le(1+\epsilon_0)\operatorname{key}(M^S)
 \le(2+O(\epsilon_0))\operatorname{OPT}_{\rm Steiner}.
 \tag{12}
$$

Its projection is an allowed physical multigraph. Its multiplicity on
each edge is at most the forest occurrence bound plus one. Choose an
integer cap $\alpha$ larger than that bound once for this packing
run.

This proof does not claim that a zero-length path between two aliases
of physical super-source neighbors has one edge. The exact rooted
component property replaces that unsupported inference.

## 6. Counts in the implicit packing

Fix a sufficiently small positive **constant** $\epsilon$. Choose
$\alpha$ to be a power of two bounding all physical edge
multiplicities in the helper graph, with generous constant slack. Then
$\alpha=E^{O(1)}$ and $\log\alpha=O(U^{7/8}h^{1/8})$.
At every packing iteration add

$$
v=\frac{\min\{c_e:e\text{ occurs in }M^S\}}{\alpha}.
 \tag{13}
$$

Every physical normalized load increases by at most one. At least one
minimum-capacity witness increases by at least $1/\alpha$.
The monotone MWU potential bounds every edge's total normalized load by
$O(\log(NW)/\epsilon^2)$. Hence the number of packing iterations is

$$
I\le m\alpha\operatorname{poly}(U).
 \tag{14}
$$

Store pending load separately on each helper occurrence, exactly as in
the public augmented-tree construction. Flush an occurrence when its
pending load reaches $c_e/(C_1\alpha)$, with $C_1$ a sufficiently
large fixed constant. Charge a threshold flush to that much new physical
load. Thus there are at most
$m\alpha\operatorname{poly}(U)$ threshold flushes. An occurrence
retired by a forest or helper edit is also flushed, but that flush is
charged to the explicit deletion record rather than to a threshold.

Recomputing a physical price may require updating every current copy of
that physical edge. This costs $\alpha$ times a polynomial
logarithm. Paying this factor explicitly is harmless:
$m\alpha^2\operatorname{poly}(U)$ is still $mE^{O(1)}$.

There is no uncharged feedback loop between retirement flushes and the
forest. The forest sees only deletions of the fixed geometric copies
from Section 4. Their total number is $O(m\operatorname{poly}(U))$,
regardless of how adaptively the numerical prices are chosen. All
resulting forest recourse is already bounded by the decremental oracle.
An MST change changes the maintained $M$ and $M^S$, but does not
by itself change the underlying graph $A$ or create a new physical
price. During a settled-update transaction, no new packing load is
inserted. Flushes merely move existing load from pending to flushed.

The helper keys also receive explicit updates whenever a canonical
distance label changes. By Section 3 and physical degree three, these
cost at most $mE^{O(1)}$. The augmented dynamic trees, deterministic
dynamic MST, and Euler-tour sparsifier extraction then incur only fixed
polynomial logarithmic factors in their actual update counts.

The terminal sparsifier consequently has at most $mE^{O(1)}$ edges
and is constructed within the same bound. This accounting does not
replace all public $m^{o(1)}$ terms by $E$ without examining their
role: iteration count, copy count, label recourse, retirement flushes,
and dynamic-tree updates have each been charged separately.

## 7. Finite arithmetic on one common load grid

The most convenient implementation does not store a product such as
$(1+\eta)^j$ exactly. That product can have far more bits than its
numerical magnitude suggests.

### 7.1 Exact loads and bounded accumulators

All physical capacities are positive polynomially bounded integers.
Since $\alpha$ in (13) is a fixed power of two, every inserted load
lies on the common grid $1/\alpha$. The Euler-tour terminal-edge
weights before final normalization lie on $1/(2\alpha)$.
By (14), every accumulator numerator has
$O(\log(IW)+\log\alpha)=O(U+\log\alpha)$ bits. Dynamic-tree
lazy sums, pending loads, flush totals, and the packed output therefore
have polynomial logarithmic bit length.

Let

$$
\delta=2^{-b},\qquad
 b=\left\lceil C_2\log_2(2N)/\epsilon\right\rceil,
 \tag{15}
$$

where $C_2$ is a sufficiently large absolute constant. Since
$\epsilon$ is fixed for this application, $\delta=N^{-O(1)}$.
For analysis, if $L_e$ is the exact total physical load already
inserted, define the conceptual price

$$
Q_e=\frac{\delta}{c_e}
                    \exp(\epsilon L_e/c_e).
 \tag{16}
$$

Only the exact flushed total $A_e\le L_e$ is used to recompute the
stored price. Per-occurrence thresholds and the multiplicity cap keep
$L_e-A_e\le C_3c_e$ for a sufficiently small fixed $C_3$, apart
from the bounded one-step overshoot processed atomically. Thus the
flushed conceptual price and $Q_e$ differ by $e^{O(\epsilon)}$.

### 7.2 Certified exponential approximations with no drift

Choose one global dyadic quantum

$$
0<g\le\frac{\epsilon\delta}{C_4 W},
     \qquad \log(1/g)=O(U),
 \tag{17}
$$

where $W$ bounds capacities of the current degree-three input.
At a flush, compute a certified upper approximation to
$(\delta/c_e)\exp(\epsilon A_e/c_e)$, with additive error at
most a fixed multiple of $g$, expressed on the grid $g$.
Set the stored price to the maximum of its old value and this new
upper approximation.

Because $A_e$ is nondecreasing, the maximum operation preserves the
same upper-error bound. It also makes the stored price monotone. There
is no multiplication of old approximation errors: each value is
recomputed from the exact cumulative flushed load. Since the exact
price is at least $\delta/W$, (17) bounds its relative numerical
error by $O(\epsilon/C_4)$.

A certified interval is enough. The implementation need not decide
which side of an arbitrarily close transcendental grid boundary an
exact exponential lies on. An interval of width $g/10$, followed by
rounding its upper endpoint upward, supplies the required approximation.
The exponent is a rational of polynomial logarithmic bit length and
has magnitude $O(U)$. Standard range reduction and a Taylor series
with a certified tail compute such an interval using polynomial
logarithmic bit work.

### 7.3 Termination, feasibility, and quality under numerical error

Let $D_Q=\sum_e c_eQ_e$, and let $D_p$ be the same sum using
stored prices. Pending-load lag and (17) give

$$
e^{-O(\epsilon)}D_Q
                     \le D_p\le e^{O(\epsilon)}D_Q.
 \tag{18}
$$

Run while $D_p<1$, processing all associated forest and flush
changes before the next iteration. A single iteration changes every
normalized load by at most one, so it multiplies $D_Q$ by at most
$e^\epsilon$. At termination,

$$
e^{-O(\epsilon)}\le D_Q\le e^{O(\epsilon)}.
 \tag{19}
$$

Let $P^*$ be the optimum fractional Steiner packing, and let
$V=\sum_t v_t$ be the unscaled inserted value. The public
Steiner-packing mincut relation gives $P^*\ge\lambda(S)/2$.
The selected physical multigraph is a
$(2+O(\epsilon))$-approximate minimum-price Steiner subgraph under
the stored prices, and hence also under $Q$ by (18). Writing that
factor as $\gamma=2+O(\epsilon)$, the elementary MWU estimate is

$$
D_Q^{\rm next}-D_Q
 \le(\epsilon+O(\epsilon^2))v_t
                      \sum_e a_{t,e}Q_e
 \le(\epsilon+O(\epsilon^2))\gamma v_tD_Q/P^*.
 \tag{20}
$$

Here $a_{t,e}\le\alpha$ is the physical multiplicity. Summing
logarithmic increases, using initial $D_Q=m\delta$, and using
(19) yields

$$
V\ge\frac{P^*}{\gamma(\epsilon+O(\epsilon^2))}
                  \bigl(\log(1/(m\delta))-O(\epsilon)\bigr).
 \tag{21}
$$

Equation (16) and the upper bound in (19) give
$L_e/c_e\le (\log(1/\delta)+O(\epsilon))/\epsilon$.
Choose a common rational upper approximation $Z$ to this last
quantity, with an additional $1+O(\epsilon)$ relative slack, and
scale every packed weight by $1/Z$. Then the packing is feasible.
Taking $C_2$ sufficiently large in (15) makes the ratio of the two
logarithms in (21) at least $1-O(\epsilon)$. The feasible output
value is therefore

$$
V/Z\ge\lambda(S)/(4+O(\epsilon)).
 \tag{22}
$$

A fixed sufficiently small $\epsilon$ gives the $4.1$-type
constant used by the guide-tree argument. The rational $Z$ can be
computed from $b\log 2$ with polynomial logarithmic precision;
no exact logarithm is stored.

### 7.4 Structural length range and integer skeleton input

Throughout the computation, (19) and the same pre-termination estimate
give $p_e\le2$, after increasing the harmless fixed bound if
necessary. Also $p_e\ge\delta/W$. Consequently every oracle
length

$$
p_e/g
 \tag{23}
$$

is a positive integer in $[1,N^{O(1)}]$. This is an explicit
common-grid aspect-ratio proof, not an inference from the magnitude of
an exact rational product. The geometric-copy adapter therefore has
only $O(\log N)$ levels. Its structural $\log L$ is $O(U)$
and never receives an $E$-bit denominator.

The fixed accuracy is useful here. The original public implementation
rounds lengths relative to the current Steiner optimum because its
quoted oracle uses the narrower interval $[1,n^4]$. Our oracle
accepts every fixed polynomial aspect ratio; the fixed constant in
(15) may be large, without changing the exponent in (1). No optimum
scale epochs are needed for this application.

Every final terminal-sparsifier edge has weight

$$
b_e/(2\alpha Z)
 \tag{24}
$$

for a nonnegative polynomially bounded integer $b_e$. Supply the
integer graph with weights $b_e$ to Li's skeleton construction.
This is one common rescaling of every capacity. It preserves all
relative cut statements and near-mincut families. There is no product
of unrelated denominators. The scale is tracked symbolically only when
the final cut guarantees are interpreted.

## 8. Li's skeleton and the size of the guide family

Use the updated primary source
[Li, arXiv:2106.05513v2](https://arxiv.org/pdf/2106.05513),
Theorem 1.5. Its quantitative factor is

$$
F_L=\exp O(U^{5/6}h^{O(1)}),
 \tag{25}
$$

with $\epsilon^{-7}$ work and scale factors. AKL+'s earlier quoted
$\epsilon^{-4}$ dependence should not be substituted for that
updated theorem. Accuracy is a fixed constant here, so the difference
does not change the leading logarithmic power.

Two construction-level modifications justify the fixed
$c$-near-mincut version needed by AKL+.

1. In Li's unbalanced-cut analysis, increase the threshold $\tau$
   by a fixed factor $c$. The bound on canonical volumes is linear
   in the cut capacity, so cuts of capacity at most $c\lambda$
   satisfy the required unbalanced condition with the same asymptotic
   factor.
2. In the final weight preprocessing, clip an edge at
   $c\widetilde\lambda$, not merely at $\widetilde\lambda$.
   This leaves every cut of capacity at most $c\lambda$
   unchanged. The edge-splitting count increases by only the fixed
   factor $c$.

The second change is necessary: clipping at a lower threshold could
change a near-mincut even though it preserves the minimum cut itself.
For the guide application $c$ is an absolute constant, so both
changes are absorbed into (25).

Let $m'\le mE^{O(1)}$ be the terminal-sparsifier size and let
$H$ be the unweighted skeleton. The scale guarantee gives

$$
m_H\le m'F_L^{O(1)},\qquad
                \lambda_H\le F_L^{O(1)}.
 \tag{26}
$$

The second estimate must be retained: the guide-tree family size and
the deterministic tree-packing time depend on $\lambda_H$, not
only on $m_H$. AKL+ Theorem 4.23 therefore costs at most

$$
\widetilde O(m_H\lambda_H)
                    \le mE^{O(1)}F_L^{O(1)}.
 \tag{27}
$$

Since $5/6<7/8$, every fixed power of (25) is absorbed by (1),
even with an unspecified fixed power of $h$. In particular, the
skeleton is not an exponent bottleneck in this transfer.

## 9. The fixed-parameter mincut adapter and the outer reductions

The respect parameter is a fixed absolute constant (the guide
construction uses 16). The new construction in
[deterministic-fixed-k-tree-mincut-adapter.md](deterministic-fixed-k-tree-mincut-adapter.md) proves the needed
$(m+n)\log^{O(k+1)}n$ aggregate maxflow inventory. Its leaf routine
chooses its maximizer over all guide targets after completing the
lower-k calls. It uses one full source-arm child when the maximizer is
on that arm, and otherwise two children with disjoint uncontracted
regions. This preserves the required source-arm cuts while preventing
duplication of an uncovered Steiner region. Non-source contraction
targets are broadcast to their original parent targets, and parameter
one has a separate set-mincut leaf base.

These are new construction arguments in this research assembly. We do
not treat them as an automatic consequence of the public theorem
statement. The proof separately establishes cut preservation and
$\sum_i(n_i-1)\le n-1$ for same-parameter children. Lower-k
branching is only $O(\log n)$, so the fixed-k cost is a polynomial
logarithm times exact maxflow. The maxflow factor is not raised to the
centroid depth.

The remaining source factors are quantified in
[gomory-hu-external-factors-except-fixed-k.md](gomory-hu-external-factors-except-fixed-k.md). In particular, the
weighted expander primitive uses the uniform parameter $r$ in
Li--Saranurak's original theorem, rather than substituting a vanishing
accuracy into a statement phrased only for fixed constants.

Running it for all guide trees contributes the factor in (26).
Algorithm 8 adds $O(\log(nW))$ calls. The terminal-selection and
cut-decomposition stages in Section 6 use the explicit expander factor

$$
\gamma_{\rm exp}
                   =\exp O(U^{4/5}h^{O(1)}).
 \tag{28}
$$

Their choice of $\psi$ has reciprocal bounded by a fixed power of
$\gamma_{\rm exp}$ and logarithms. The hit-and-miss calls in these
stages use a fixed hit-set cardinality two; their size and construction
time are polynomial in the miss parameter $L$, with
$L=\widetilde O(\psi^{-1})$. Thus these calls contribute a fixed
power of (28), not an exponential in $\psi^{-1}$.

The resulting work for one actual recursive input of size $m_*$ is

$$
m_*\operatorname{poly}(U)\,
       E(N)^{C_5}F_L(N)^{C_6}
       \gamma_{\rm exp}(N)^{C_7}E_{\rm flow}(N)^{C_8},
 \tag{29}
$$

where all $C_i$ are fixed constants and
$\log E_{\rm flow}=O(U^{4/5}h^{O(1)})$. Small recursive instances
may use their own smaller oracle parameters; (29) is simply a uniform
upper envelope multiplied by their actual size.

AKL+ Lemma 6.32 bounds the sum of all recursive edge inventories by a
polynomial logarithm times the original size, because the terminal
recursion depth is $O(\log n)$. Summing (29), and using
$4/5,5/6<7/8$, yields (2). Disconnected inputs are handled component
by component and joined with zero-weight tree edges. Isolated vertices
cost only their input/output size.

## 10. Audit status and statements not implied by this note

The strong-forest proof and the following application adapters are
separate, inspectable obligations:

* source-rooted multi-source parent selection, including the smaller
  scale tie rule and explicit label-change inventory;
* per-packing degree-three cut expansion;
* fixed positive-length geometric copies, binary port trees, and final
  root-only null contraction;
* the helper-MST argument under the actual multi-source contract;
* MWU iteration, threshold-flush, retirement, copy-update, and label
  counts;
* common-grid finite arithmetic and one common output capacity scale;
* the updated Li skeleton factor, its fixed-near-mincut extension, and
  the guide-family size;
* the new global-max leaf mincut construction, its contracted-target
  broadcasts, and its disjoint same-parameter inventory;
* fixed-power external overheads in the SSMC and Gomory--Hu reductions.

An independent audit of the first item is in
[multisource-rooted-approximate-ball-forest.md](multisource-rooted-approximate-ball-forest.md). The companion
[finite-mwu-and-li-skeleton-independent-audit.md](finite-mwu-and-li-skeleton-independent-audit.md) records an independent
check of the numerical and skeleton items. The strong-forest arithmetic
and map construction are independently checked in
[Separating metric stretch, forest congestion, and work](separated-metric-forest-and-strong-sssp.md).
The global-max construction is independently checked in
[fixed-k-global-max-leaf-independent-audit.md](fixed-k-global-max-leaf-independent-audit.md) and
[A deterministic fixed-k guide-tree mincut adapter](deterministic-fixed-k-tree-mincut-adapter.md); the primary source
interface issue and its resolution are retained in
[fixed-k-tree-mincut-source-interface-audit.md](fixed-k-tree-mincut-source-interface-audit.md).

The result is not obtained from faster numerical distance labels alone,
nor from a faster static flow oracle alone. It requires the explicit
rooted forest, its low simultaneous congestion, its stable canonical
nodes, and its bounded representation recourse. The claim is an exact
cut tree for general weighted undirected graphs; only internal metric
and packing computations are approximate.

The current public baseline audit is
[public-strong-forest-retuning-baseline.md](public-strong-forest-retuning-baseline.md). Retuning only the outer
public parameters already gives
$\exp O(U^{62/63}h^{1/3})$ for the strong forest, improving its
printed $83/84$ bound. That is the conservative audited comparison
for the new strong forest. It is not asserted to optimize all possible
public combinations. The exact Gomory--Hu composition includes the new
Section 9 construction as an explicit contribution, and remains labeled
as a research proof assembly when reporting the result.
