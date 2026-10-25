# Independent audit of the separated strong-forest construction

**25 October 2026.** This is an independent review of
`separated_metric_forest_and_strong_sssp.md`. The review concerns the
bounded-degree, positive-length, decremental undirected interface
stated there. It does not certify a general Gomory--Hu corollary and
does not claim external verification of the research construction.

The audit found no new asymptotic obstruction after the anchor,
permanent-canonical-node, root-only-null-quotient, and positive
core-contraction repairs described below. The resulting leading
overhead is

\[
       \exp O(U^{7/8}h^{1/8}),\qquad
       U=\log(n+m+4),\quad h=\log(U+4).
 \tag{1}
\]

The most significant quantitative point is that metric stretch,
simultaneous forest congestion, and construction work have different
bounds. They enter different parts of the covering and flattening
proof. Replacing all three by one common factor loses the displayed
exponent.

## 1. Imports and the statement actually audited

The public outer construction is Kyng--Meierhans--Probst Gutenberg
(KMG), [arXiv:2311.06402v1](https://arxiv.org/pdf/2311.06402).
Relevant source locations are Theorem 3.1's local metric and exact
nearest-pivot properties, Lemma 3.21's flat-forest lift, Theorem 4.7's
marked-tree operations, the construction of Theorem 4.9, Theorem 5.3,
Theorems 5.12 and 5.14, and Algorithm 10 with Claim 5.15.

The new local provider is the checkpoint's explicitly parameterized
static routing, normalized repair, selected-degree feedback, and
degree-reset construction. The audit treats its earlier proof notes
as named imports. It does not apply the old complete KMG dynamic
spanner theorem outside its stated parameter range. This distinction
is necessary because the repair depth used here is larger than the
printed range of that old complete theorem.

The output contract has two different vertex maps:

\[
 \iota:V(G)\hookrightarrow V(F),\qquad
 \pi:V(F)\to V(G),\qquad \pi\circ\iota=\mathrm{id}.
 \tag{2}
\]

The distinguished node \(\iota(v)\) remains fixed throughout the
physical vertex's lifetime. Each auxiliary forest node also keeps its
physical image fixed during its own lifetime. The map \(\pi\) may
have many preimages. Every final forest edge is one copy of a current
physical original edge, and simultaneous edge and vertex occurrences
are both bounded. These facts are stronger than either a numerical
distance estimate or a representation of one useful cycle.

The theorem currently covers constant physical degree, positive
polynomial-aspect integer lengths, fixed original vertices, and edge
deletions. The low-diameter instances used inside covers can retire
their current terminal vertices, and their internal fully dynamic
backends process the emitted updates. The proof does not silently
extend the root null-quotient argument to a high-degree physical graph.

## 2. Local metric preservation and the port reset

Write the static structural and work logarithms as

\[
 g=O((p+r)h),\qquad
 f=O(U/p+U/r+r^2h+(p+r)h).
 \tag{3}
\]

With local repair depth \(K\), one parent instance exports a
selected graph that preserves distances between its logical pivots
within a factor \(\rho\), where

\[
                   \log\rho=O(Kg+h).
 \tag{4}
\]

The needed metric statement concerns every pair of pivots, not every
auxiliary core root. The argument is by replacing each positive demand
edge on a native core walk by its endpoint-preserving selected route.
Route-gradient identities and min-ratio-cycle quality are not used.
An exported edge length dominates its literal parent walk, so this
replacement also gives the lower, noncontracting metric inequality.

The binary port tree has stable root \(q(v)\), at most \(C\) leaves,
unit connector lengths, and real selected-edge lengths multiplied by
a power of two \(H\geq4(\log_2 C+1)\). A simple selected path
uses at most \(2\log_2 C\) connectors per edge. Since each selected
edge has length at least one,

\[
 d_S(v,w)\leq H^{-1}d_B(q(v),q(w))\leq2d_S(v,w).
 \tag{5}
\]

Port connectors contribute no physical parent length. This fact is
only a one-level projection statement; the proof keeps a typed null
record until the final root quotient rather than identifying all equal
physical images at every recursive level.

Ordinary recursive APSP queries terminate in a strict pivot ball or
continue through one pivot per endpoint. For the latter case the two
nearest-pivot legs and the distance between the two pivots cost at most
a constant multiple of the original endpoint distance. Combining this
with (4)--(5) over depth \(d\) gives

\[
                 a_{\rm APSP}=O(dKg+dh).
 \tag{6}
\]

There is no metric factor \(k\) at each level. The \(k\)-dependent
cost of exposing strict balls and updating nearest-pivot forests is
local work. It does not appear in the length of an individual query.

## 3. Why the anchor repair is needed and sufficient

One cannot infer a low-diameter child graph from (4). An extra core
root can have a long physical attachment even when the original
terminal graph has small diameter. Thus an unanchored proof that takes
an arbitrary spanning tree of the final auxiliary graph can fail.

The proposed repair chooses an original anchor \(s_0\), promotes it
to a pivot, and forces the chain

\[
                         s_{i+1}=q(s_i)
 \tag{7}
\]

to remain pivots in the successive instances. Let
\(\sigma_i=\prod_{j<i}H_j\). For an original terminal \(v=v_0\),
define \(v_{i+1}=q(p_i(v_i))\) and

\[
                  D_i=\sigma_i^{-1}d_{G_i}(v_i,s_i).
 \tag{8}
\]

Since \(s_i\) is an available pivot, the nearest-pivot leg has length
at most \(d_{G_i}(v_i,s_i)\). The two pivots \(p_i(v_i)\) and
\(s_i\) are separated by at most twice that distance. Equations
(4)--(5) therefore imply

\[
                         D_{i+1}\leq4\rho D_i.
 \tag{9}
\]

At the actual-size base, use an exact shortest-path tree rooted at its
anchor. Summing the nearest-pivot legs in root units and then the
base path bounds the assembled terminal-to-anchor path by

\[
                    (d+1)(4\rho)^d d_G(v,s_0).
 \tag{10}
\]

This proves the required diameter guarantee in a connected terminal
instance. It bounds only chains that start at original terminals.
Far auxiliary roots and unused port ghosts do not enter (8)--(10).
Thus

\[
                    a_{\rm diam}=O(dKg+dh).
 \tag{11}
\]

The factor four in (9) is needed: two comes from the pivot triangle
inequality and two from the positive port reset. Changing it to another
absolute constant would not affect the exponent, but omitting a
factor from the actual inequality would be a proof error.

### Charging forced promotions

An anchor is promoted through the constructive endpoint/root promotion
routine used by the stable core-forest provider. A positive self-loop
is only an alternative implementation if it actually reaches that
routine. A separate loop heap that consumes the loop first would not
promote the endpoint.

One external anchor deletion creates at most one new forced promotion
per level. Process the parent promotion, settle its ordinary child
transcript, and then promote the newly determined child canonical root.
This adds \(O(d)\) explicitly charged elementary operations. It does
not send all nearest-pivot forest changes as additional child graph
updates. The latter changes remain local work.

When a parent period restarts, initialization receives the then-current
anchor and includes its fiber in the actual initial child inventory.
At a nonbase instance that extra fiber has size \(O(P)\), absorbed
by \(O(m_iP/k)\) because \(m_i\geq k\). At a base instance the
anchor is handled exactly. No extra uncharged \(k\) factor is created
by either event.

## 4. Arbitrary child forests, not just special cycle answers

The lift pools stable physical core trees by root. Each child vertex
occurrence gets a distinct pool-root handle. A real child edge creates
one connecting record between the appropriate interior pool nodes;
a connector creates one typed null link. Contracting every assigned
pool tree recovers the child forest, so the lift is acyclic.

The pool path between two incident connecting edges is no longer than
their charged root legs. Consequently, a terminal-to-terminal path
in the lift has no greater physical length than the child path divided
by the local port scale. This is an arbitrary-forest statement. It
cannot be replaced by a claim that one returned raw cycle has a good
projection.

For a common child-size, update, and one-level occurrence factor \(P\),

\[
 \log P=O(U/K+g+h),\qquad
 \log W=O(x+U/K+f+Kg+h),\quad k=2^x,
 \tag{12}
\]

the occurrence recurrence is

\[
                      G_j\leq P(G_{j-1}+1).
 \tag{13}
\]

This includes dormant pool roots, isolates, and unused port records.
Bounding only edge congestion would leave an isolated-vertex hole.
Claiming or releasing one child occurrence changes its pool index;
it does not copy an entire nearest-pivot component. Changes to the
underlying stable physical forests are separately charged to all their
pool copies.

## 5. Permanent canonical nodes and the root-only null quotient

The distinguished root terminal \(\iota(v)\) is the permanent
level-zero nearest-pivot-forest node for physical \(v\). Hierarchy
restarts reuse those root records. All higher-level occurrences have
separate identities. Thus a rebuild does not rename a canonical node.

An intermediate quotient would be unsafe. Distinct child terminals can
have the same parent physical image. Merging them and later splitting
them would demand incompatible fixed distinguished-node identities.
The corrected construction leaves every intermediate typed-null forest
uncontracted.

Only at the final physical root are true-null components contracted.
Every such component has a single physical image and contains at most
one root distinguished node. If it has one, that permanent node is the
quotient representative. Otherwise a new auxiliary representative can
be used and retired when a later split requires it.

If edge and vertex congestion are both at most \(\Gamma_F\), a null
component has at most \(\Gamma_F\) nodes. Constant physical degree
bounds its real incident records by \(O(\Gamma_F)\). A changed null
link can therefore trigger a complete local component rebuild and all
incident endpoint corrections in \(\Gamma_F\operatorname{poly}(U)\)
work. Even a conservative fixed power of \(\Gamma_F\) is absorbed
in the logarithmic envelope used here.

Contraction preserves acyclicity and terminal-path lengths. It never
merges disconnected components merely because their physical images
agree. Distinct forest copies of the same physical vertex may remain
distinct after the quotient.

This proof explicitly uses bounded physical degree. A later general-
degree application needs its own degree-reduction or quotient adapter.

## 6. Coupled work recurrences and late initial credit

For one parent period of initial size \(m_0\), a prefix of \(z\)
edits emits at most \(O(m_0P/k+Pz)\) child records and edits. The
initial term may be used late in the period. Therefore it cannot be
discarded once child initialization has finished.

The safe normalized recurrences are

\[
\begin{aligned}
 G_j&\leq P(G_{j-1}+1),\\
 J_j&\leq W+P(G_{j-1}+1)
              +(P/k)(J_{j-1}+T_{j-1}),\\
 T_j&\leq O(kW+kP(G_{j-1}+1))
              +O(P)(J_{j-1}+T_{j-1}).
\end{aligned}
 \tag{14}
\]

In particular, the \(T_{j-1}\) term is present in the initialization
line. Let \(Z_j=J_j+T_j/k\). Since
\(J_{j-1}+T_{j-1}\leq kZ_{j-1}\), (14) gives

\[
 Z_j\leq O(W+P(G_{j-1}+1)+PZ_{j-1}).
 \tag{15}
\]

Together with (13), this yields a fixed polynomial in \(k\) times
\(W(cP)^{O(j)}\). The nearest-pivot logs, marked-diameter data,
anchor operations, and root quotient all fit this bound. Thus at
depth \(d=O(U/x)\),

\[
\begin{aligned}
 a&=O(dKg+dh),\\
 c&=O(d\log P+dh),\\
 B&=O(x+f+Kg+d\log P+h).
\end{aligned}
 \tag{16}
\]

Here \(a\) bounds both metric stretches, \(c\) bounds simultaneous
congestion, and \(B\) bounds work and explicit recourse. It is enough
to choose \(x\) a sufficiently large multiple of \(\log P\), so
child inventories contract at the declared recursion scale.

Short integer or dyadic length labels remain of polynomial bit length.
The accumulated local port rescalings and finite sums of physical path
lengths create \(O(Ud)\) bits under a generous bound. A polynomial
in this bit count contributes only logarithmic terms to (16), since
the selected \(d\) is itself polylogarithmic. No denominator formed
from unrelated exact reciprocals is introduced.

## 7. The core-contraction call in the cover construction

The cover routine calls APSP both on its current induced cover graph
and on the quotient that contracts its current core. The second graph
does not automatically have bounded degree or positive lengths under
a naive implementation.

The proposed adapter uses a fixed binary tree with one leaf per
initial core vertex and an extra edge from each current core vertex
to its leaf. Give all auxiliary edges a common positive dyadic length
\(\delta\ll n^{-3}\). A vertex leaves the contracted core by
deleting its one attachment. All original incidences remain at their
original bounded-degree vertex records. Queries and marks for a
current core vertex refer to the auxiliary root, with one current
original core vertex stored as a witness.

A simple path in the zero-length quotient visits its contracted node
at most once. Its corresponding auxiliary-tree detour costs
\(O(\log n)\delta\). Every nonzero quotient distance is at least
one before scaling, so the adapter overestimates it by a
\(1+o(1)\) factor. Core-to-core queries return zero explicitly.
Conversely, contracting the positive auxiliary tree and dropping its
nonnegative lengths maps every adapter walk to a valid quotient walk.
Thus the two-sided distance comparison is valid.

Scaling by \(\delta^{-1}\) gives positive integer lengths with a
fixed polynomial aspect ratio. The extra tree has size linear in the
actual cover instance, and each uncontracted vertex costs a constant
number of local graph and mark updates. These changes stay within the
cover's total actual-record accounting. Auxiliary edges are used only
for numerical quotient-diameter calls; they are not exposed as physical
edges in the final strong forest.

The initial source-reachable set is another small boundary. A top
approximate-ball forest may initially omit unreachable original
vertices. If the theorem promises a canonical node for every original
vertex, add permanent isolated nodes for the omitted vertices. In the
decremental setting those initially unreachable vertices cannot become
reachable later. This costs only \(O(n)\) at the top level.

## 8. The outer construction uses three different parameters

Choose

\[
 \log\gamma_{\rm cover}=O(a+h),\qquad
 \gamma_{\rm cover}\geq
       \max\{2\gamma_{\rm APSP}^2,\gamma_{\rm diam}\}
       \operatorname{poly}(U).
 \tag{17}
\]

For cover parameter \(K_{\rm cov}\), the overlap logarithm is

\[
                   \log\Delta=O(U/K_{\rm cov}+h).
 \tag{18}
\]

The cover instances are charged by their total initialization and
update inventory. Accordingly, amortized local APSP work suffices;
the proof does not require the old worst-case deamortization factor.
Their aggregate work has logarithm \(B+O(U/K_{\rm cov}+h)\).

With hopset parameter \(\Lambda\), the public scale condition is

\[
             K_{\rm cov}\Lambda(a+O(h))\leq c_0U
 \tag{19}
\]

for a sufficiently small fixed \(c_0\). Internal accuracy
\(\epsilon/O(\Lambda)\) remains inverse polylogarithmic. The
hopset and approximate-ball construction contributes
\(O(U/\Lambda+U/K_{\rm cov}+h)\) to logarithmic work.

When a cover-center occurrence is flattened, the length replacement
uses \(\gamma_{\rm diam}\), which is absorbed in (17). The number
of copies created uses \(\gamma_{\rm cong}\) instead. The
one-level occurrence recurrence is

\[
 A_i\leq (1+\Delta^2+\Delta\gamma_{\rm cong})A_{i+1}.
 \tag{20}
\]

This counts old occurrences, approximate-ball-tree occurrences, and
low-diameter-forest occurrences. It does not count the time spent
constructing the local forests. The latter is paid once per real
instance and then each explicit update is forwarded to its allocated
copies. Fixed distinguished maps make this forwarding possible without
remapping every endpoint on a local restart.

The final logarithmic overhead is therefore

\[
 B+O\!\left(U/\Lambda+U/K_{\rm cov}
               +\Lambda U/K_{\rm cov}+\Lambda c+h\right).
 \tag{21}
\]

These are the locations where a hidden repeated work factor or a
confusion between metric stretch and congestion would change the
result. Re-reading the actual flattening recurrence supports the
separation in (19)--(21).

## 9. The 7/8 balance, and a lower bound for this charged model

Set

\[
 t=(U/h)^{1/8},\quad p=r=\Theta(t),\quad
 K=\Theta(t^3),\quad x=\Theta(t^7h),\quad d=O(t).
 \tag{22}
\]

Then

\[
 g=O(th),\quad f=O(t^7h),\quad
 \log P=O(t^5h),\quad
 a=O(t^5h),\quad c=O(t^6h),\quad B=O(t^7h).
 \tag{23}
\]

Choose \(K_{\rm cov}=\alpha t^2\) and
\(\Lambda=\beta t\), rounded to positive integers, for sufficiently
small fixed constants \(\alpha,\beta\). The left side of (19) is
at most a constant times \(\alpha\beta t^8h=\alpha\beta U\).
The largest terms in (21) are \(t^7h\), establishing (1).

There is also a useful optimization boundary. Treat the displayed
positive terms as mandatory charges, and suppose their common target
is \(A\). The static work term \(U/p\) and the hierarchy scale
give \(p\gtrsim U/A\) and \(d\gtrsim U/A\). Hence

\[
       a\gtrsim U^2Kh/A^2,
       \qquad c\gtrsim U^2/(AK).
 \tag{24}
\]

The outer work terms force
\(\Lambda\gtrsim U/A\) and
\(K_{\rm cov}\gtrsim\Lambda U/A\gtrsim U^2/A^2\).
Combining these with the scale constraint (19) gives

\[
                         K\lesssim A^5/(U^4h).
 \tag{25}
\]

The flattening term \(\Lambda c\lesssim A\) gives

\[
                         K\gtrsim U^3/A^3.
 \tag{26}
\]

Thus any choice within this charged model satisfies

\[
                              A^8\gtrsim U^7h.
 \tag{27}
\]

The balance (22) attains this model bound. Equation (27) is not an
algorithmic lower bound: a different construction might remove one of
these charges. It says that further tuning the displayed parameters
alone cannot improve the leading 7/8 exponent.

## 10. Multi-source roots and application boundaries

The independent note
`multisource_rooted_approximate_ball_forest.md` gives a source-rooted
strengthening of the approximate-ball forest. It checks BGS's actual
MES parent invariant and combines nested scale labels by taking the
minimum, with ties resolved toward the smallest scale. The tie rule
excludes the internal dummy-source edges to smaller-ball vertices.
The resulting real parent edges strictly decrease a global label, so
each finite component contains exactly one current source.

This property survives KMG's per-occurrence tree substitutions. It
allows a top call with a source set instead of a single physical
super-source with zero-length star edges. The strengthening preserves
the work and recourse exponent. It is useful for a possible
Gomory--Hu application, but it does not settle all its other factors.

The public printed strong-forest factor is 83/84. Before claiming a
separating quantitative baseline, its public free parameters must also
be reoptimized; the printed value is not automatically best within
the old framework. The present audit establishes the new construction
and its charged-model optimum, while the public-only reoptimization
is a separate calculation.

For Gomory--Hu, the remaining independent obligations include the
quantitative skeleton bound and mincut value, guide-tree packing and
SSMC dependencies, arbitrary original degrees, length increases, and
the use of exact flow or cut verifiers. The bounded-degree theorem
reviewed here should not be stated as a general Gomory--Hu theorem
until those checks are complete.
