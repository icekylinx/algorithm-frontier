# A virtual-expander hierarchy with explicit terminal sets

**Separate reconstruction candidate, 24 October 2026.** This note addresses
one interface in the hierarchy discussed by Chang--Huang--Su,
[arXiv:2405.03908v1](https://arxiv.org/pdf/2405.03908), Appendix A.
It is independent of the threshold-routing construction and of the
5/6 matching composition.

The underlying source is Chang--Saranurak,
[arXiv:2007.14898v1](https://arxiv.org/pdf/2007.14898), Sections 4.1--4.3,
Appendix E.2, and Lemma C.9. That source distinguishes the union of
terminal sets from all vertices on their embedding paths. Its Lemma
C.9 proves expansion of the induced graph on the latter, larger set.
Expansion of the induced graph on the terminal union alone does not
follow. For example, two terminal vertices can be joined by an embedded
edge whose interior is outside the terminal set, while the induced
terminal graph has no edge.

The replacement below exports the explicit virtual graph used at the
start of the proof of Lemma C.9. It changes the ROOT type of the proposed
hierarchy. The root graph is a virtual expander with an explicit
embedding into the original graph, rather than an asserted induced
subgraph of that graph. Child graphs and the covering matchings are
literal subgraphs of their parent virtual graph.

This note proves the cut, balance, degree, and geometric-embedding
interfaces. It does not prove the complete CHS query algorithm or its
Task-2-to-Task-3 load reduction. It also does not by itself turn arbitrary
CONGEST round bounds into sequential work bounds. The source matching
and recursive cut procedures still require the separately audited
sequential implementation. The new local coarse-cut work here is
explicitly polynomial in the number of blocks.

## 1. A polynomial-work weighted coarse-cut primitive

Let a graph \(B\) have \(b\) vertices, positive integer vertex masses
\(w_i\), and nonnegative rational edge weights \(a_{ij}\). Parallel
weights may be summed. Assume

\[
                   \sum_j a_{ij}\leq\Delta w_i,
                   \qquad \Delta\geq1.
 \tag{1}
\]

For a nontrivial cut define its mass sparsity by

\[
 \Psi_w(S)=
 \frac{a(S,\overline S)}{\min\{w(S),w(\overline S)\}}.
 \tag{2}
\]

Given a rational \(0<\eta\leq1\), there is a deterministic algorithm,
polynomial in \(b\) and the input bit size, which returns either:

* a nonempty cut \(S\) of mass at most half the total, with
  \(a(S,\overline S)\leq\eta w(S)\); or
* the certificate that every cut has mass sparsity at least
  \(\eta^2/(16\Delta)\).

The certificate can be a positive-semidefiniteness result; no
transcendental calculation or enumeration of all block subsets occurs.
For one vertex the second alternative is vacuous.

### 1.1 Exact rational spectral test

Let \(L\) be the weighted Laplacian and \(W=\operatorname{diag}(w_i)\).
Set

\[
                         \theta=\eta^2/(8\Delta).
 \tag{3}
\]

Construct a rational basis for the subspace
\(\sum_iw_i x_i=0\); for example eliminate the last coordinate
using its positive mass. Test positive semidefiniteness of
\(L-\theta W\) on that subspace by exact symmetric elimination.
If it is positive semidefinite, every centered nonzero vector has
Rayleigh quotient at least \(\theta\).

For a cut \(S\), its centered indicator has Rayleigh quotient

\[
 a(S,\overline S)
       \left(\frac1{w(S)}+\frac1{w(\overline S)}\right)
 \leq 2\Psi_w(S).
 \tag{4}
\]

Therefore positive semidefiniteness implies
\(\Psi_w(S)\geq\theta/2\) for all cuts, as required.

Otherwise exact symmetric elimination gives a rational centered vector
\(x\neq0\) with

\[
                    x^{\mathsf T}Lx<\theta x^{\mathsf T}Wx.
 \tag{5}
\]

One implementation successively eliminates positive diagonal pivots.
A negative pivot supplies a negative vector. A zero diagonal with a
nonzero off-diagonal entry supplies a negative vector on those two
coordinates; a zero row can be removed. Back substitution produces
the full vector. Thus this is a finite rational algorithm. Fraction-free
elimination, or ordinary elimination with numerator/denominator reduction,
has polynomial bit complexity: all relevant values are ratios of minors
of a rational matrix whose dimension is \(b-1\), and determinant-size
bounds are polynomial in that dimension and its input bit size.

These are TEMPORARY LOCAL rational numbers. They can have
\(\operatorname{poly}(k,\log n,\log\psi^{-1})\) bits, much more
than the numerical backend's length/gradient-label cap. Their full
multiword arithmetic is charged to the polynomial-block preprocessing
work. They are not exported as edge weights, gradients, route
coefficients, or numerical labels. The exported result of this step
is only a block subset or a Boolean expansion certificate; graph
edge IDs, vertex IDs, and explicit unweighted path lists retain
\(O(\operatorname{poly}(\log n+\log\psi^{-1}))\)-bit records.

### 1.2 A weighted-median sweep

Choose a weighted median \(m\) of the coordinates of \(x\). Put
\(y^+_i=\max\{x_i-m,0\}\) and
\(y^-_i=\max\{m-x_i,0\}\). Each support has mass at most half
the total. Centering gives

\[
 \|x-m\mathbf1\|_W^2\geq\|x\|_W^2,
 \qquad
 (y^+)^{\mathsf T}Ly^+ +(y^-)^{\mathsf T}Ly^-
       \leq x^{\mathsf T}Lx.
 \tag{6}
\]

Hence one nonzero part \(y\) has Rayleigh quotient below
\(\theta\). For its level sets \(S_z=\{i:y_i^2>z\}\),

\[
 \begin{aligned}
 \int_0^\infty a(S_z,\overline S_z)\,dz
 &=\sum_{ij\in E(B)}a_{ij}|y_i^2-y_j^2|\\
 &\leq
 \sqrt{y^{\mathsf T}Ly}
 \sqrt{\sum_{ij\in E(B)}a_{ij}(y_i+y_j)^2}\\
 &\leq\sqrt{2\Delta\,y^{\mathsf T}Ly\,\|y\|_W^2}.
 \end{aligned}
 \tag{7}
\]

Also \(\int_0^\infty w(S_z)\,dz=\|y\|_W^2\). A nonempty
level set therefore has boundary-to-mass ratio at most
\(\sqrt{2\Delta\theta}=\eta/2\). Examine the at most \(b\)
distinct level sets and choose the best exact rational ratio.
This proves the first alternative, with slack. This argument also
handles disconnected graphs and unequal block masses.

### 1.3 Removing coarse cuts until a large core remains

Starting with total mass \(W_0\), repeatedly apply this primitive
to the remaining coarse graph, removing the returned smaller-side
cut. Stop if the removed union \(C_2\) has mass at least \(W_0/4\),
or if the remaining graph is certified.

The boundary of the removed union in the INITIAL coarse graph is
at most \(\eta w(C_2)\): sum the boundaries at the moments of
removal, and observe that edges between removed pieces no longer
cross the final union. Before the last removal its mass is below
\(W_0/4\), and a removed cut is at most half the remaining mass.
Thus the final union has mass below \(5W_0/8\).

If the first stopping condition occurs, the smaller side of this
cut has mass at least \(W_0/4\) and sparsity at most \(2\eta\).
If the second occurs, the removed union has mass below \(W_0/4\),
and the remaining coarse graph has sparsity at least
\(\eta^2/(16\Delta)\). At most \(b-1\) nonempty removals occur.
The entire procedure is polynomial in \(b\) and the input bit size.

More generally, its stopping mass can be any fixed
\(0<\beta\leq1/4\) times \(W_0\). At the first crossing, the
removed union has mass in
\([\beta W_0,(1+\beta)W_0/2)\). After possible complementation,
the smaller side has mass at least \(\beta W_0\) and sparsity
at most \(2\eta\). If certification occurs first, the remaining
mass is at least \((1-\beta)W_0\). The weak spectral leaf below
uses this variant with \(\beta=1/1000\).

## 2. Virtual merging of internally expanding blocks

Let \(U_1^*,\ldots,U_t^*\) be disjoint sets. On each block there
is a virtual graph \(H_i^*\) of edge sparsity at least
\(0<\psi_{\rm in}\leq1\). Let \(G\) be an actual host of maximum
degree at most \(\Delta\), and assume its interblock edges have
outer sparsity at least \(0<\psi_{\rm out}\leq1\): every cut
respecting the blocks has boundary at least \(\psi_{\rm out}\)
times its smaller vertex-side cardinality.

Define the EXPLICIT virtual graph

\[
 G_0=
 \left(\bigcup_i H_i^*\right)
 \cup\{e\in E(G):\text{the ends of }e\text{ lie in different blocks}}.
 \tag{8}
\]

No internal path vertex is added to its vertex set. Its degree satisfies

\[
             \Delta(G_0)\leq\max_i\Delta(H_i^*)+\Delta.
 \tag{9}
\]

It has sparsity

\[
              \Psi(G_0)\geq
          \frac{\psi_{\rm in}\psi_{\rm out}}{4(\Delta+1)}.
 \tag{10}
\]

Here is a direct proof, which does not use induced expansion of the
terminal union. For a cut \(S\), round each block to its majority
side and call the resulting union \(T\). Let \(z\) be the sum
of the minority cardinalities in the blocks, and let
\(w=\min\{|S|,|\overline S|\}\). The internal block graphs
contribute at least \(\psi_{\rm in}z\) crossing edges. The
interblock host edges contribute at least

\[
                 \psi_{\rm out}(w-z)-\Delta z.
 \tag{11}
\]

Indeed the rounded cut has smaller side at least \(w-z\), and
changing the side of \(z\) vertices alters at most \(\Delta z\)
host edge crossings. If
\(z\geq\psi_{\rm out}w/(2(\Delta+\psi_{\rm out}))\), use
the internal contribution. Otherwise use (11). Both cases imply
(10).

If the \(H_i^*\) already have simultaneous embeddings into \(G\)
of congestion at most \(c\) and dilation at most \(d\), then
\(G_0\) has an explicit embedding into \(G\) with congestion
at most \(c+1\) and dilation at most \(\max\{d,1\}\).
Its interblock host edges use their own singleton paths. The graph
\(G_0\) is precisely the virtual graph at the start of the proof
of CS20 Lemma C.9; we export it rather than replace it by an induced
graph on an incorrectly smaller vertex set.

## 3. Modified success type for the recursive cut player

Replace the success alternative of the recursive cut routine by:

> Return a terminal set \(X\), an explicit virtual expander \(H_X\)
> with vertex set exactly \(X\), and an explicit embedding into the
> current host. Return the same actual sparse-cut certificate as before
> whenever the cut alternative occurs.

Use a balanced-cut sparsity threshold of AT MOST \(1/8\) in every
NONROOT recursive cut-player call. This is necessary when the
matching player saturates only half the requested sources.
The corrected entropy argument in
[half_matching_entropy_progress.md](half_matching_entropy_progress.md)
proves an \(\Omega(n)\) increase per continuing round at that
threshold, and hence \(O(\log n)\) rounds. The printed CS20
threshold-\(1/2\) half-matching calculation is not imported.

A virtual-expander success ends the game instead of requesting
another matching, so the corrected entropy proof needs only the
actual balanced cut and half-matching on continuing rounds.
The intermediate game graph is the MULTIGRAPH union of those
matchings, with a fresh edge ID for every round occurrence.
Parallel repetitions are not deduplicated: the entropy cut-mass
bound counts all previous crossing matching occurrences.
This graph has degree \(O(\log n)\). The returned virtual graph
is NOT inserted back into an unfinished game graph.

Suppose the current actual host has \(N\) vertices and maximum
degree \(\Delta\), and partition its vertices, in ID order, into
\(k\) blocks \(V_i\) of sizes \(\lfloor N/k\rfloor\) or
\(\lceil N/k\rceil\). Run the simultaneous cut-matching construction
with the explicit
[fresh-cut matching adapter](sequential_fresh_cut_matching_adapter.md).
Every matching request is made on the full current host with EMPTY
initial cut; old failed cuts are bookkeeping only. The cutoff in
outer round \(j\) is \(\psi/(16j^2)\), so overlapping cut unions
retain the required sparsity. This replaces the source's general
nonempty-\(C_{\rm in}\) implementation. On a successful block, the recursive routine now
returns a virtual graph \(H_i\) on \(U_i\subseteq V_i\), with
\(|U_i|\geq2|V_i|/3\), rather than requiring an induced subgraph of
the intermediate matching graph.

The exact sequential covering-matching step in Section 5 of the
same adapter, with the structural role of CS20 Lemma 4.6, produces disjoint
\(U_i^*=U_i\cup U_i'\), with a matching from \(U_i'\) into \(U_i\)
saturating \(U_i'\). Put \(H_i^*=H_i\cup M_i^*\). Then

\[
 |U_i'|\leq|U_i|,\quad
 \Delta(H_i^*)\leq\Delta(H_i)+1,\quad
 \Psi(H_i^*)\geq c\min\{\Psi(H_i),1\}
 \tag{12}
\]

for an absolute constant \(c>0\). The last assertion follows
directly as follows. For a cut with smaller side \(w\), let \(b\)
be the number of separated matched pairs. If \(b\geq w/2\),
the matching itself supplies the bound. Otherwise move each separated
bad vertex to its good partner's side. This changes at most \(b\)
vertices, so the rounded cut has smaller side at least \(w-b\).
Every good vertex has at most one bad partner; hence each side has
at least \((w-b)/2\) good vertices. The internal graph supplies
at least \(\Psi(H_i)(w-b)/2\geq\Psi(H_i)w/4\) crossing edges.
Taking \(c=1/4\) after truncating expansion at one suffices. This
does not require paths of the matching embedding to stay within
\(U_i^*\).

All cut certificates up to this point are cuts of the current
host. They depend on the sets, matchings, and their failed flow
requests, not on whether a successful child is an induced subgraph.
They are retained with fixed constant slack in their sparsity
thresholds.

### 3.1 An explicit coarse merge with constant slack

The source merge has the following two possibilities before its final
coarse-cut step. Either an actual sparse cut of fixed positive balance
has already been returned, or:

* fewer than a fixed small fraction of the \(V_i\) failed;
* \(V'=\bigcup_iU_i^*\) covers all but a small cut \(C_1\), or
  all but a set \(B\) of cardinality at most
  \(\psi\lfloor N/k\rfloor/(1000\Delta)\);
* in the first case \(V\setminus V'\subseteq C_1\) and
  \(|\partial C_1|\leq(\psi/100)|C_1|\).

The PRIMARY exact sequential covering routine supplies the first
case with no uncovered set outside \(C_1\), so \(B=\varnothing\).
The small-\(B\) alternative below is only a harmless weaker
compatibility case; the reconstruction does not need a tiny-leftover
parameter or its running-time dependence.

Use sufficiently smaller fixed thresholds in the source matching
calls to obtain these displayed constants. This changes no parameter
exponent. Return any cut of size at least \(\beta N\), with
\(\beta=1/1000\), as a cut-only answer; do not also retain its
candidate expander.

At a recursion leaf with at most
\(C k^5\lambda_{\rm cap}^2\) actual vertices, where
\(\lambda_{\rm cap}\) is the explicit polylogarithmic shuffler cap
defined in Section 4 and \(C\) is one fixed constant, the
same spectral procedure gives an explicit polynomial-work WEAK cut
player without further recursion. Give every vertex mass one, use a
sufficiently small fixed multiple of the weak requested cut threshold
for \(\eta\), and run the Section 1.3 variant that stops at removed
mass \(\beta N\), NOT \(N/4\). After possible complementation a
returned cut has smaller side between \(\beta N\) and \(N/2\).
Otherwise the remaining induced subgraph has at least
\((1-\beta)N\) vertices and sparsity
\(\Omega(\psi_{\rm cut}^2/(\Delta+1))\). It is a valid successful
virtual graph with the identity embedding. Its work is polynomial
in \(k\) and the input bit size. This is only a base cut player;
routing queries in a successful leaf are the separate leaf-router
obligation.
Use this fixed polynomial leaf threshold in the reconstruction instead
of relying on the source's separate leaf-trimming description. Every
remaining internal part has at least a fixed multiple of
\(k^4\lambda_{\rm cap}^2\) vertices, so the shuffler's later
token-error inequalities have their required slack even if \(k\)
is constant. The larger fixed polynomial does not alter the allowed
\(k^{O(1)}\operatorname{polylog}n\) preprocessing envelope.

Contract each \(U_i^*\) to a coarse vertex of mass \(|U_i^*|\),
keeping only actual host edges between blocks. Condition (1) holds
with the actual host degree \(\Delta\). Apply Section 1.3 with
\(\eta=\psi/1000\). If it returns a balanced coarse cut, or if
its removed union together with \(C_1\) or \(B\) has size at least
\(\beta N\), return a cut-only answer. Otherwise keep all the
remaining blocks and use (8) as the successful virtual graph.

For clarity, the conversion from a coarse cut to a host cut has no
hidden boundary assumption. If \(V\setminus V'\subseteq C_1\),
then

\[
 |\partial_G(C_1\cup C_2)|
       \leq|\partial_G C_1|+|\partial_{G[V']}C_2|.
 \tag{13}
\]

If instead \(C_1=\varnothing\) and the uncovered set is \(B\),
use \(B\cup C_2\). For nonempty \(C_2\), at least one block
has been removed. When \(N/k>7\), its size is at least
\(\lfloor N/k\rfloor/3\), and therefore

\[
 \Delta|B|\leq (3\psi/1000)|C_2|.
 \tag{14}
\]

Together with the accumulated coarse boundary bound, (13)--(14)
give host sparsity strictly below \(\psi\). If the union exceeds
half the host, use its complement; its size is still below
\(2N/3\) before complementation, so at most a fixed factor is
lost. If \(C_1=C_2=\varnothing\), return the virtual core without
a cut; the uncovered \(B\) is the allowed small leftover.

On a successful answer, the remaining coarse graph has outer
sparsity at least

\[
                       \Omega(\psi^2/\Delta).
 \tag{15}
\]

Consequently (10) multiplies the child expansion by only
\(\psi^2/\operatorname{poly}(\Delta+1)\). The source's
\(2^{O(k)}\) search for a maximum coarse cut is not used. There
are at most \(k\) exact spectral sweeps on \(k\)-vertex graphs,
with \(O(\log N+\log\psi^{-1})\)-bit input coefficients.

Every successful internal weak call has the same
\((1-\beta)\)-coverage guarantee as the corrected weak leaf:
all uncovered vertices are in \(C_1\cup C_2\), and its cardinality
is below \(\beta N\) on success. This remains true when \(C_1\)
overlaps the retained terminal set. The primary construction
uses exact covering and requires no optional leftover \(B\).

### 3.2 Balance improvement retains one successful hierarchy

Use the complete proof in
[explicit_virtual_cut_balance_wrapper.md](explicit_virtual_cut_balance_wrapper.md).
For an original \(N_0\)-vertex host and target threshold \(\psi\),
call the weak procedure with \(\psi_{\rm w}=\psi/2\) on the
CURRENT induced host outside the accumulated disjoint cut pieces.
Stop when their union reaches \(N_0/4\), or on a weak success.

Before the last cut addition the union has size below \(N_0/4\).
The added smaller side is at most half the current remaining host,
so the union at its first crossing has size below \(5N_0/8\).
After possible complementation, the returned cut has smaller side
in \([N_0/4,N_0/2]\). Its original boundary is at most
\(\psi_{\rm w}\) times the uncomplemented union size, by summing
boundaries in the successive CURRENT induced hosts.
Complementation loses less than \(5/3\), so its sparsity is below
\(\psi\).

Otherwise the final active host has more than \(3N_0/4\)
vertices. Both weak internal successes and weak spectral leaves
cover at least a \((1-\beta)\) fraction, hence their terminal set
has more than \((1-\beta)3N_0/4>2N_0/3\) vertices.
There are only \(O(1/\beta)\) weak calls, a fixed constant.
Retain only the hierarchy from the ONE final successful call;
its embedding already lies in an induced subgraph of the original
wrapper host. This adds no geometric composition.

This explicit wrapper replaces reliance on the source's leftover
notation. In particular a weak leaf reached after prior removals
must use the \((1-\beta)\)-coverage variant above; a bare
three-quarter-coverage leaf would not suffice for this composition.

At a promised-expander ROOT, the wrapper's exact-coverage proof
uses the first proposed removal. Every fresh matching or covering
failure cut is certified in the unchanged full root host and is
impossible below its expansion. Exact covering therefore gives
\(V'=V\) and \(C_1=\varnothing\). The first coarse cut is then
exactly a true-host cut respecting a full partition and is likewise
impossible. Thus \(C_2=\varnothing\), not just small. A root
spectral leaf cannot make its first removal either. The detailed
argument is in the wrapper's Section 4; it uses no optional
leftover \(B\). Nonroot abstract cut-player calls may still return
proper-subset successes, whose omitted root vertices are recovered
by the root's exact covering step.

## 4. The hierarchy's sets and local graph degrees

For an actual root graph with \(n\) vertices and an integer parameter
\(p\geq1\), put
\[
 u=\lceil\log_2(n+2)\rceil,\qquad
 k=2^{\max\{5,\lceil u/p\rceil\}},\qquad
 \lambda_{\rm cap}=10^7(u+1)^2.
 \tag{15a}
\]
All recursion calls use this same \(k\) and this same cap. The cap
dominates the explicitly proved \(O(\log(k+2)\log(n+2))\) energy
shuffler length after fixing its absolute constants; its finite
stopping condition is also checked. Use the actual-size leaf test
\(N\leq Ck^5\lambda_{\rm cap}^2\), never an allocation of that many
vertices. The constant \(C\) can be chosen once so that every
internal node satisfies
\[
 \min_i|U_i^*|\geq8\lambda_{\rm cap}t^2,\qquad
 6|X|/k\geq\lambda_{\rm cap}t^2.
 \tag{15b}
\]
These are the size conditions used by the explicit sequential
scatter router. They replace the old sufficient conditions
\(k\geq c\lambda\) and the CHS range restriction on \(\epsilon\).
The present reconstruction is sequential and does not use that
distributed parameter clipping.

In a successful weak call write \(\tau=N/k\). Its good children
are the selected sets \(U_i\), and its bad children are \(U_i'\).
The parent terminal set is exactly

\[
                   X=\bigcup_{i\text{ selected}}(U_i\cup U_i').
 \tag{16}
\]

Thus children really partition the parent; embedding interiors do
not silently enlarge it. The children obey

\[
 \frac23(\tau-1)\leq|U_i^*|\leq2(\tau+1),
 \qquad
 \frac{|X|}{3k}\leq|U_i^*|\leq\frac{6|X|}{k},
 \tag{17}
\]

for the stated internal-node size threshold. The order of the good
children follows the original ID-ordered \(V_i\), since
\(U_i\subseteq V_i\). Bad-child IDs need not be ordered.

Here are explicit counts for the number of children. Before a
successful answer, the failed-part cut has size below \(\beta N\).
Each failed part has at least \(|V_i|/8\) vertices in that cut.
For \(\tau>7\), fewer than \(16\beta k\) parts failed.
Every whole block removed by the coarse procedure has size at least
\(\tau/3\). Its removed union lies in the final small cut, so
fewer than \(3\beta k\) further blocks are removed. With
\(\beta=1/1000\), the number \(t\) of good children satisfies

\[
                              2k/3\leq t\leq k.
 \tag{18}
\]

If no coarse block is removed and only a tiny uncovered \(B\)
remains, the same count follows from the failed-part count alone.
The final successful host used by the balance wrapper can be smaller
than its original input, but it still has a constant fraction of that
input. Formula (17) uses that successful host's \(\tau\), and remains
\(\Theta(|X|/k)\).

Each recursive child input has at most \(\lceil N/k\rceil\)
vertices, while its successful parent terminal set has a fixed
fraction of \(N\). For \(k\geq24\), recursion therefore has
depth \(O(\log n/\log k)\). The choice (15a) gives depth \(O(p)\)
even when its fixed minimum \(k=32\) is active. All size
rounding and small-host thresholds are explicit integer tests.

At a nonroot recursive cut-player call, the actual host is a union
of \(O(\log n)\) matchings, regardless of the degrees of successful
virtual outputs. Thus its host degree is \(O(\log n)\).
Writing \(d\) for the number of recursive cut-player levels left,
(9) and (12) give

\[
              \Delta(H_X)\leq O((d+1)\log n).
 \tag{19}
\]

This is a polylogarithmic degree bound, not the literal
\(O(\log n)\) bound claimed for an induced matching subgraph.
All subsequent uses must allow this explicit larger degree. For
\(d\leq\operatorname{polylog}n\), it changes a fixed polynomial
degree factor only by a polylogarithm. A port-splitting wrapper is
also available if a downstream primitive needs constant degree.

Most importantly, every child virtual graph \(H_{U_i}\) and every
covering matching \(M_i^*\) is a literal subgraph of its parent
graph \(H_X\). Their child-to-parent embedding is the identity.
Do not instead lift each child's graph afresh through all older
hosts when servicing a query.

In fact \(H_X[U_i]=H_{U_i}\) as a graph with edge IDs. Parent-level
host edges are added only BETWEEN the blocks \(U_j^*\), while a
covering-matching edge has one endpoint outside \(U_i\). Thus no
new parent-level edge has both endpoints in the good child \(U_i\).
Inductively, every good-node graph is induced in the ROOT VIRTUAL
graph. This is a statement about (8), not about the original physical
graph. It permits shared edge records and ordinary vertex-subset
views without recursively duplicating physical path lists.

## 5. Expansion and ONE root embedding

Let \(u=\log(n+2)\). Use sparse-cut threshold \(1/8\) in
every nonroot recursive cut-player call, with smaller fixed
thresholds inside its balance/merge wrappers. At the original root use a threshold a fixed factor
below the original graph's sparsity \(\psi\).

Let \(\sigma_d\) be a lower bound for nonroot virtual expansion
with at most \(d\) remaining recursive levels. Equations
(10), (12), and (15) yield

\[
                     \sigma_d\geq u^{-c}\sigma_{d-1}
 \tag{20}
\]

for an absolute constant \(c\). The spectral base just described
has expansion at least \(u^{-O(1)}\) on a nonroot matching-graph
host, so the same recurrence starts with that bound. Therefore

\[
 \Psi(H_X)\geq u^{-O(d)}
 \quad\hbox{off the root},\qquad
 \Psi(H_{\rm root})\geq
              \operatorname{poly}(\psi)\,u^{-O(d)}.
 \tag{21}
\]

The degree in the loss (10) is the degree of the CURRENT HOST's
interblock edges, not an uncontrolled degree of the entire recursively
flattened graph. This is why (20) uses a fixed polynomial per level.

Let \(E_d\) bound the simultaneous edge congestion and dilation
of the successful virtual output into its current host. At one
level, child virtual graphs first embed into their disjoint
intermediate matching graphs with quality \(E_{d-1}\). The
union of those matching graphs embeds into the current host with
quality

\[
               B=\operatorname{poly}(\Delta,\psi_{\rm cut}^{-1},u),
 \tag{22}
\]

by the source matching construction, including its
\(O(\log n)\) matching rounds. The covering matching costs at
most another \(B\), while new interblock host edges are singleton
paths. Hence

\[
                            E_d\leq cB(E_{d-1}+1).
 \tag{23}
\]

Every nonroot \(B\) is a fixed polynomial in \(u\). The root
has the only original \(\psi^{-1}\) factor. The resulting ONE
embedding

\[
                  f_0:H_{\rm root}\longrightarrow G
 \tag{24}
\]

has quality

\[
                       \operatorname{poly}(\psi^{-1})\,
                                         u^{O(d)}.
 \tag{25}
\]

This can be constructed with explicit route lists by postorder
substitution. Each output edge has at most the length in (25),
and all occurrences are charged to those lists. One need not
materialize a separate original-graph expansion for every ancestor
copy of the same edge.

Because all hierarchy graphs are literal subgraphs of the root
virtual graph, a collection of paths in any of them can first be
viewed as paths in \(H_{\rm root}\) without any geometric expansion.
Only then is \(f_0\) applied. Thus the root embedding is charged
ONCE. Repeatedly multiplying \(E_d,E_{d-1},\ldots\) during query
flattening would be a different, unnecessarily expensive algorithm
and would lose the desired depth dependence.

An original expander cannot return any nonempty root cut below its
sparsity. With the PRIMARY exact covering routine, all root games
succeed, the covering matching leaves no uncovered vertex, and a
nonempty respecting coarse cut would itself be an impossible sparse
cut of the original host. Consequently the primary root terminal
set is actually ALL of \(V(G)\). No outside-root token delegation
is needed. The root graph is still the virtual graph \(G_0\), not
an assertion about an induced physical graph.

If a compatible weaker covering routine with a tiny leftover is
used instead, the earlier \(2|V(G)|/3\) root bound still suffices,
and an additional covering matching in the original graph handles
the outside vertices. This weaker variant is not required by the
primary sequential reconstruction.

### 5.1 Provider for the full router's flattened-family hypothesis

Combine this hierarchy with
[the polynomial energy cut player](polynomial_energy_cut_player.md),
the exact saturation routine in
[the fresh-cut adapter](sequential_fresh_cut_matching_adapter.md),
and
[the explicit leaf circuits](sequential_leaf_routing_and_chs_work.md).
At each internal \(X\), the energy cut produces physical terminal
sets of unequal sizes with the smaller side able to be saturated.
Call exact saturation in the CURRENT virtual graph \(H_X\), using
a cutoff below its certified sparsity. Thus each shuffler matching
has explicit virtual paths with length and congestion bounded by
\[
          \operatorname{poly}(\Delta(H_X),\Psi(H_X)^{-1},u).
 \tag{26}
\]
There are at most \(\lambda_{\rm cap}=\operatorname{poly}(u)\)
such matchings per node. Every covering-matching edge already is
an edge of its parent virtual graph. Leaf circuit paths have the
separately proved fixed-polynomial dependence on leaf inverse
expansion and \(\log n\).

Good-node vertex sets at ONE depth are disjoint. Since their graphs
are induced subgraphs of \(H_{\rm root}\), their virtual host edge
sets are disjoint too. Therefore taking the union of all primitive
paths at one depth uses the maximum of their individual congestion
bounds, not their number. Unioning the \(O(p)\) depths and the
polynomially many circuit/shuffler layers gives virtual congestion
and maximum virtual path length at most
\[
                    \operatorname{poly}(\psi^{-1})u^{O(p)}.
 \tag{27}
\]
The original \(\psi^{-1}\) appears only at the root; all nonroot
expansion certificates use constant cut thresholds.

Apply the ONE map \(f_0\) to this union of virtual paths.
Multiplying (27) by (25) still gives
\[
                        A=\operatorname{poly}(\psi^{-1})u^{O(p)}
 \tag{28}
\]
for both physical edge congestion and maximum physical path length.
The exponents hidden in \(O(p)\) are fixed constants. No node's
entire ancestor embedding is applied a second time.

Equation (28) is precisely the flattened primitive-family condition
in
[conditional_full_router_from_shufflers.md](conditional_full_router_from_shufflers.md).
Its partition, injective folding, normalization, mixing, and size
conditions follow respectively from (16)--(18), (12), the literal
\(n'_X=6|X|/k\), the energy lemma, and (15b). With the primary exact
root coverage, this router's root already contains every original
vertex.

Preprocessing uses the ACTUAL virtual records. At any depth their
total edge count is at most the root virtual edge count
\(O(np\log n)\). Exact shuffler saturation and path output have
the fixed-polynomial work bound corresponding to (26); the energy
and leaf arithmetic have the local multiword bounds already stated.
Together with the hierarchy construction recurrence, all work fits
\[
              n^{1+O(1/p)}
                 \operatorname{poly}(\psi^{-1})\log^{O(p)}n.
 \tag{29}
\]
For the actual-size rule (15a), \(k^{O(1)}\) is
\(n^{O(1/p)}\) times a fixed constant, even when \(k=32\).
No leaf is padded to \(Ck^5\lambda_{\rm cap}^2\).

These are provider and accounting statements. Correctness of the
subsequent scatter/meeting/reversal QUERY is the separate induction
in the full-router note; (28) is not a substitute for that induction.

## 6. What this resolves, and what it does not

The construction resolves the terminal/interior mismatch by changing
the exported object explicitly. It gives:

* exact partitioning of every parent terminal set by good/bad children;
* actual sparse-cut certificates and the source balance guarantees;
* an explicit polynomial-block-work coarse merge;
* polylogarithmic virtual degrees and the expansion recurrence (21);
* identity child and covering-matching embeddings;
* one root embedding of quality
  \(\operatorname{poly}(\psi^{-1})\log^{O(d)}n\).

The explicit sequential replacement for inherited short-path packing,
and the resulting hierarchy work recurrence, are supplied in
[sequential_short_path_matching.md](sequential_short_path_matching.md).
The corresponding
[fresh-cut matching adapter](sequential_fresh_cut_matching_adapter.md)
proves the repeated half-matching, failure-cut union, and covering
interfaces using only the fully proved empty-cut primitive.
The source's general nonempty-initial-cut proof is not used.
Temporary rational matrix work here is
charged there as local multiword preprocessing. It never changes the
numeric-label word guard of a recursive matching backend.

The direct query induction and explicit route extraction are proved
separately in
[conditional_full_router_from_shufflers.md](conditional_full_router_from_shufflers.md),
using the provider conditions established in Section 5.1. That
induction deliberately avoids the source's Task-2-to-Task-3 load
reduction and its best-leaf density parameter. The polynomial energy
cut player and constructive leaf router supply their own stated
interfaces; the query proof must use those exact interfaces rather
than follow from the hierarchy geometry alone.

In particular this is not a reinterpretation that silently declares
the original terminal union to induce an expander. The exported root
graph and its map (24) are part of the new interface and must be passed
to every downstream caller that uses them.
