# A time--stretch tradeoff for deterministic fully dynamic APSP

**Research proof assembly and baseline audit, 25 October 2026.** This
note separates the running time of the current distance hierarchy from
its approximation factor. It is a consequence of the local metric,
update, and degree-reset interfaces proved in
`separated_metric_forest_and_strong_sssp.md`, Sections 2--7, with the
named static-provider and normalization imports retained there.

**Stronger comparison added in checkpoint E.** Jointly reconstructing the
public static provider and repair hierarchy gives amortized overhead
`exp O(U^(6/7) h^(1/7))` at stretch
`exp O(U^(5/7) h^(2/7))`. At that same stretch scale, the research
construction below gives `exp O(U^(23/28) h^(5/28))` overhead. This
replaces `59/63` as the strongest public-framework comparison established
by the present audit. The reconstruction, its independent audit, and
the matched comparison are in `public_apsp_joint_retuning_audit.md`,
`public_apsp_joint_retuning_independent_audit.md`, and
`same_stretch_apsp_comparison_and_root_audit.md`. These are derived
research consequences of public ingredients, not printed theorem
statements. The earlier points (1)--(2) remain valid.

The clean fixed-stretch point is

\[
 \boxed{\quad
 \text{amortized update factor }\exp O(U^{11/14}),\qquad
 \text{stretch }\exp O(U^{6/7}h),
 \quad U=\log(N+4),\ h=\log(U+4).
 \quad}
 \tag{1}
\]

Here \(N\) bounds the initial graph inventory plus the number of
elementary updates in the sequence. Distance queries take
\(\operatorname{polylog}N\) time. The algorithm is fully dynamic,
deterministic, and applies to arbitrary-degree undirected graphs with
positive integer lengths in \([1,N^{O(1)}]\), using the explicit
positive-length degree adapter in Section 5.

There is also a faster point with a coarser, still subpolynomial,
approximation:

\[
 \boxed{\quad
 \text{amortized update factor }
          \exp O(U^{3/4}h^{1/2}),\qquad
 \text{stretch }\exp O(U/h).
 \quad}
 \tag{2}
\]

Neither statement is an exact matching exponent, a constant-factor
APSP approximation, nor a worst-case update guarantee. They do not
automatically improve the strong \((1+\epsilon)\) decremental forest:
that application additionally pays for the larger metric stretch in
its covering and hopset construction.

## 1. Input, output, and honest scope

Let \(m_0+n_0\) be the initial graph inventory, and let \(Q\) count
edge insertions/deletions and isolated vertex insertions/deletions.
Set \(N\geq m_0+n_0+Q+4\). Repeated insertion of the same edge
counts as a new physical lifetime. One may use a known bound \(N\),
or restart at doubled bounds; the sum of restart inventories is paid
by the usual geometric accounting. No large master-sized graph is
allocated to a small local instance.

After every complete external update, a query returns

\[
 d_G(u,v)\leq\widehat d(u,v)\leq\gamma\,d_G(u,v),
 \tag{3}
\]

with infinity for disconnected pairs and zero for equal endpoints.
For the selected point, initialization plus all updates cost

\[
                  (m_0+n_0+Q)\exp O(B).
 \tag{4}
\]

The explicit record-change bound refers to the hierarchy's own
recursive graph/forest records. It does **not** refer to an explicitly
maintained table of all \(n^2\) pairwise answers; one graph edit can
change that many answers.

The numerical distance interface (3) is the principal theorem here.
The existing hierarchy also stores lifting witnesses, but this note
does not strengthen a walk-extraction bound into a simple-path bound
measured solely by the final projected path size. Such a strengthening
requires its own representation and loop-erasure accounting.

## 2. The separated local envelopes

Use the current static distance provider with

\[
 g=\log\Gamma=O((p+r)h),\qquad
 f=\log F_{\rm stat}
       =O(U/p+U/r+r^2h+(p+r)h).
 \tag{5}
\]

Let \(K\) be the local repair depth, let \(k=2^x\) be the
size-reduction parameter, and let \(d=O(U/x)\) be the number of
recursive levels. The already established degree-reset interface gives

\[
 \log P=O(U/K+g+h),
 \tag{6}
\]

where \(P\) bounds child inventory and encoded child edits. The
hierarchy work and explicit record changes have logarithmic envelope

\[
 B=O(x+f+Kg+d\log P+h).
 \tag{7}
\]

The distance approximation satisfies independently

\[
                    \log\gamma=O(dKg+dh).
 \tag{8}
\]

The important distinction is that \(Kg\), rather than \(dKg\),
appears in the local maintenance part of (7). Recursion amplifies
maintenance through \(P\); it does not multiply the complete static
construction work by another exponential at every level. Conversely,
metric approximation multiplies across the \(d\) pivot reductions,
and therefore has the factor \(d\) in (8).

These formulas require \(x\) to exceed a sufficiently large constant
times \(\log P\). Local instances smaller than the declared
size-reduction threshold terminate in the exact base case. The local
initialization allowance that later becomes child edits is included
in (7); it is not discarded in this substitution.

## 3. A one-parameter family

Choose a growing parameter \(t\), round it to an integer, and set

\[
                 p=r=\Theta(t),\quad
                 K=\Theta(t^2),\quad
                 x=\Theta(U/t),\quad d=O(t).
 \tag{9}
\]

Constants in \(x\) are chosen large enough for size shrink and the
local work bounds. Substitution gives

\[
\begin{aligned}
g&=O(th),\\
f&=O(U/t+t^2h),\\
Kg&=O(t^3h),\\
d\log P&=O(U/t+t^2h),\\
B&=O(U/t+t^3h),\\
\log\gamma&=O(t^4h).
\end{aligned}
 \tag{10}
\]

For all choices below, \(t\to\infty\),
\(x/(U/K) = \Theta(t)\to\infty\), and
\(x/(th)=\Theta(U/(t^2h))\to\infty\). Hence the shrink condition
is satisfied. All finitely many small values of \(N\) are handled by
the exact base algorithm.

### 3.1 Keeping the printed KMG stretch scale

Set \(t=\Theta(U^{3/14})\). Then

\[
\begin{array}{c|c}
\text{term}&\text{bound}\\ \hline
x, U/p, U/r & O(U^{11/14})\\
r^2h & O(U^{3/7}h)\\
Kg & O(U^{9/14}h)\\
d\log P & O(U^{11/14}+U^{3/7}h)\\
dKg & O(U^{6/7}h).
\end{array}
\tag{11}
\]

The terms with smaller powers of \(U\) absorb their displayed
\(h\) factors into \(O(U^{11/14})\). This proves (1).

### 3.2 A \(3/4\) time exponent with subpolynomial stretch

Set

\[
                  t=\Theta\bigl((U/h^2)^{1/4}\bigr).
 \tag{12}
\]

Then

\[
 U/t=\Theta(U^{3/4}h^{1/2}),\qquad
 t^3h=\Theta(U^{3/4}h^{-1/2}),\qquad
 t^4h=\Theta(U/h).
 \tag{13}
\]

Equation (2) follows. Since \(U/h=o(U)\), its stretch is
\(N^{o(1)}\), with the explicit upper envelope
\(N^{O(1/\log\log N)}\).

### 3.3 Other points

For any fixed \(0<a<1\), setting
\(t=\Theta((U^a/h)^{1/4})\) gives

\[
       B=O(U^{1-a/4}h^{1/4}),\qquad
       \log\gamma=O(U^a).
 \tag{14}
\]

More generally, let \(\omega(U)\to\infty\) sufficiently slowly
and put \(t=(U/h)^{1/4}/\omega(U)\). As long as \(t\to\infty\),
the formulas give

\[
 B=O(U^{3/4}h^{1/4}\omega(U)),\qquad
 \log\gamma=O(U/\omega(U)^4).
 \tag{15}
\]

These are construction tradeoffs. They are not lower bounds against
other algorithms or claims of an optimal Pareto frontier.

## 4. Why the query remains small

A distance query has one pair of current vertices at each hierarchy
level. It either finishes using one stored local exact distance, or
adds the two nearest-pivot legs and recurses on the corresponding
canonical child roots. At every internal degree reset, divide the child
answer by that reset's stored positive scale before adding the parent
legs. The exact base instance maintains its full distance table after
each settled encoded update, so a query reads one table entry rather
than running a base shortest-path computation. It uses \(O(d)\) local query steps, each with
polynomial logarithmic arithmetic and lookup overhead. This proves
\(\operatorname{polylog}N\) query time for (9)--(15).

Every summand represents an actual lifted walk, establishing the
lower bound in (3). The pivot detour inequalities and the per-level
metric bound establish (8). Positive port connectors only change the
absolute constant in that bound.

If the marked-diameter interface from the companion construction is
used, its local enumeration costs \(k^{O(1)}\operatorname{poly}(U)\)
per maintained witness and is already included in (7). This is separate
from materializing all distance answers.

## 5. Arbitrary degree without master-sized padding

For each current original vertex \(v\), keep a permanent query handle
\(q_v\) for that vertex's lifetime. Attach it to the root of a
leaf-oriented balanced binary search tree whose leaves are the actual
current edge incidences at \(v\). Give every connector length one.
An original edge \(uv\) of length \(\ell\ge1\) becomes an edge
between its two incidence leaves, of length \(H\ell\), where
\(H\) is a fixed power of two at least \(C\log N\).

The external query handle has degree at most one, internal binary-tree
vertices degree at most three, and an incidence leaf degree at most
two. Rotations change only a constant number of connector edges each;
an insertion or deletion performs \(O(\log N)\) elementary graph
edits. Leaf identities remain attached to their edge lifetimes while
internal nodes rotate. If a tree root changes, update its edge to the
unchanged \(q_v\).

The trees use only current incidence leaves and internal nodes.
Insertion creates \(O(1)\) nodes per incidence; rotations create no
new nodes. The total number of vertex births is
\(O(m_0+n_0+Q)\). Connector rewiring creates new edge lifetimes;
their total births and the edit transcript have size
\(O((m_0+n_0+Q)\log N)\). Isolated original vertices retain their
one query handle. In particular, this is not a tree with \(N\) leaves
allocated separately to every vertex.

Use a polynomially larger history cap, for example \(N^2\), for the
encoded hierarchy. Its logarithm is \(\Theta(U)\), so this correction
does not change any displayed exponent.

For distinct connected vertices, let \(G'\) be the expanded graph.
Projection drops connectors and divides real lengths by \(H\), so

\[
 d_G(u,v)\leq H^{-1}d_{G'}(q_u,q_v).
\]

A simple original shortest path with \(b\ge1\) edges lifts using
\(O((b+1)\log N)=O(b\log N)\) connectors. Since its original
length is at least \(b\), choosing \(H\ge C\log N\) yields

\[
 H^{-1}d_{G'}(q_u,q_v)\leq2d_G(u,v).
 \tag{16}
\]

Using the bounded-degree distance structure on \(G'\), and dividing
its answer by \(H\), thus loses only a constant factor in stretch.
The extra logarithm in update count is absorbed by (1) and (2). Equal
endpoints return zero directly. Unreachable pairs remain unreachable.
Rotations are processed as an atomic external update, with deleted
connectors removed before new connectors are added; the bounded-degree
algorithm may see intermediate disconnected states, and user queries
see the settled state.

The binary-tree degree reduction is already a public standard
construction; for example KMZ explicitly states it in Section 2.6 of
its ESA 2025 paper. The positive connector scaling and permanent query
handle above spell out its use under the positive-length interface.

## 6. Public baselines and comparison limits

The following are primary-source checks, not a claim that every
possible retuning of every public construction has been optimized.
The companion `apsp_public_parameter_and_query_audit.md` records
the exact query interfaces, actual-size parameter checks, version
history, and the stronger retuned KMZ comparison described below.

### 6.1 The directly comparable KMG headline

KMG, *A Dynamic Shortest Paths Toolbox*,
[arXiv:2311.06402v1](https://arxiv.org/pdf/2311.06402), Theorem 4.1,
gives fully dynamic deterministic APSP with stretch
\(\exp O(U^{6/7}h)\), initialization factor and **worst-case** update
factor \(\exp O(U^{20/21}h)\), and logarithmic distance queries.
Remark 4.2 supplies its path query. Its printed inner choices are
\(d=U^{1/21}\), \(K=U^{3/21}\).

Our point (1) keeps the displayed stretch scale and lowers the
**amortized** update envelope. It does not dominate the public
worst-case guarantee as an identical interface. The distinction remains
material even though every worst-case bound is also an amortized bound.

There is a source inconsistency worth recording accurately: the
heading of KMG Claim 4.6 prints \(14/15\), while Theorem 4.1 and
the proof of that claim repeatedly use \(20/21\). Its displayed
parameters yield \(20/21\). This note therefore uses the theorem and
its supported calculation rather than treating the isolated heading as
a proved stronger bound.

### 6.2 A stronger derived public composite

The KMG local Theorem 3.1 can itself be combined with the public
binary-tree degree reduction at every recursive boundary, without the
new static provider or normalized repair of this checkpoint. Set

\[
                 g_0=O(U^{2/3}h),\qquad
                 q=O(U/K+g_0+h).
\]

With bounded degree restored at each child, the local KMG theorem gives
child expansion and recourse \(e^{O(q)}\), local work
\(\exp O(x+q+K^2g_0)\), and local metric stretch
\(\exp O(Kg_0)\). The same elementary initialization/update
recurrence yields the **amortized** public-composite envelopes

\[
 B_{\rm pub}=O(U/d+K^2g_0+dq),\qquad
 a_{\rm pub}=O(dKg_0+dh).
 \tag{17}
\]

Choose

\[
              d=\Theta(U^{4/63}),\quad
              K=\Theta(U^{8/63}),\quad
              x=\Theta(U^{59/63}).
 \tag{18}
\]

Then

\[
 B_{\rm pub}=O(U^{59/63}),\qquad
 a_{\rm pub}=O(U^{6/7}h).
 \tag{19}
\]

Indeed the potentially close term is
\(K^2g_0=O(U^{58/63}h)=o(U^{59/63})\). KMG's declared local
range \(K=o(U^{1/6}/h)\) is satisfied because \(8/63<1/6\).
For actual-size base instances the same range remains valid until the
chosen base threshold: \(\log m_{\rm local}\ge x\), and
\(x^{1/6}=\Theta(U^{59/378})\) has a larger power than
\(U^{8/63}\).
Below that threshold the exact base is used.

Over the hierarchy, positive scaling and core-path labels have only
\(O(Ud)\) bits. At every nonbase instance this is a fixed polynomial
in its logarithmic size. The local pivot operations use arithmetic on
these labels, while weighted sparsification uses their logarithmic
number of length buckets. Paying the resulting polynomial logarithms
does not alter (19); no unbounded-precision arithmetic is assumed.

This is a derived baseline, not a printed theorem. It is deliberately
included so that the comparison is not restricted to the old printed
\(20/21\). It still lies strictly above \(11/14\) at the same
displayed stretch scale. It also does not prove that \(59/63\) is the
best possible reanalysis of the public framework.

### 6.3 Other public deterministic tradeoffs

* **KMZ, ESA 2025:** [conference paper](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ESA.2025.113),
  with full version [arXiv:2408.11375v1](https://arxiv.org/html/2408.11375v1), Theorem 1.1 and its Section
  4.4 proof. It gives deterministic amortized \(N^{o(1)}\) updates
  and subpolynomial approximation using an independent bootstrapping
  construction. The displayed choice has
  \(k=\exp(U/h^{1/4})\), \(K=h^{3/4}\), and depth
  \(h^{1/4}\); its logarithmic update envelope is
  \(O(U/h^{1/4})\), with substantially finer stretch than (2).
  It is not an \(U^{3/4}\) or \(U^{11/14}\) time bound. The
  full version's arXiv history currently lists only v1; the conference
  version points to that full version. A further legal retuning of
  its own recurrence gives the stronger derived public update
  envelope \(O(U\log(h+4)/h)\), with
  \(\log\gamma\le U^{a_0}\) for any fixed chosen
  \(0<a_0<1\), and polynomial logarithmic numerical queries.
  The companion audit proves this using
  \(D=\Theta(h/\log h)\), \(K=D^3\), and
  \(\log k=\Theta(U/D)\). Thus the printed KMZ parameters are
  not treated as its best directly available public comparison.
* **Haeupler--Long--Saranurak, FOCS 2024:**
  [arXiv:2402.18541v2](https://arxiv.org/pdf/2402.18541), Theorems
  1.3 and 12.1, gives worst-case \(n^\epsilon\) updates and
  \(2^{\operatorname{poly}(1/\epsilon)}\) approximation, for
  \(\epsilon\ge\log^{-c}n\) with an unspecified sufficiently
  small constant \(c>0\). Section 3.3 explicitly uses that restriction
  to absorb \((\log n)^{\operatorname{poly}(1/\epsilon)}\)
  factors. Its precise numerical query bound is
  \(O(\log\log n/\epsilon^4)\). One cannot substitute
  \(\epsilon=U^{-3/14}\) into that
  headline without proving its numerical admissibility and unbundling
  those factors. This is an important independent public tradeoff; a
  complete optimization of all of its local parameters has not been
  performed here.
* **Chuzhoy--Zhang, STOC 2023:**
  [arXiv:2304.09321](https://arxiv.org/pdf/2304.09321), Corollary
  1.5 and its appendix, gives a different approximation-versus-update
  tradeoff. Its source requires
  \(\epsilon>\log^{-1/200}n\), and the approximation has doubly
  exponential dependence on an inverse power of \(\epsilon\).
  The numerical query bound also retains
  \(2^{O(1/\epsilon)}\log n\log\log L\); this is not
  polynomial logarithmic for an arbitrary inverse-polylogarithmic
  choice of \(\epsilon\).
  It therefore cannot be cited as a uniform
  \(\epsilon=U^{-3/14}\) substitute from the printed theorem.
* **Chuzhoy--Parter, January 2026 full version:**
  [arXiv:2601.20718v1](https://arxiv.org/html/2601.20718v1) gives
  dynamic spanners through low-diameter router decompositions. Its
  declared range is \(512\le k\le(\log n)^{1/49}\) and
  \(1/k\le\delta\le1/400\), with worst-case update
  \(n^{O(\delta)}\). It is a relevant new sparsification primitive,
  but this stated range is not a faster uniform substitution at the
  update exponents in (1) or (2). The September 2026 journal article
  [*New Tradeoffs for Decremental Approximate All-Pairs Shortest Paths*](https://link.springer.com/article/10.1007/s00453-026-01407-2)
  has randomized, oblivious-adversary, decremental guarantees and does
  not change the deterministic fully dynamic comparison.

The appropriate claim is a new explicit point, and the full curve
(10), for the specified deterministic distance hierarchy, with a
substantial improvement over the directly quantified KMG comparison.
This audit does not establish a globally optimal deterministic APSP
time--stretch frontier across all public frameworks.

## 7. Consequences that are not claimed

The matching and exact-flow clients pay for cycle quality in addition
to maintenance work. The high APSP stretch in (1) or (2) cannot be
ignored in those clients, so this note yields no \(11/14\) or
\(3/4\) exact-matching bound. Similarly, the strong decremental
forest's outer scale constraint depends on metric stretch. The
separately audited \(7/8\) strong-forest and Gomory--Hu compositions
retain their own parameter choices.

For the distance oracle itself, the result requires no raw min-ratio
cycle query. It uses the current static distance provider, normalized
repair, stable local metric interfaces, and the constructive hierarchy
recurrence (5)--(8). Those named proof imports remain part of its
research-checkpoint status.
