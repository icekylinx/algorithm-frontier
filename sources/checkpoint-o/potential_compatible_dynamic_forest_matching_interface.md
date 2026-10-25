# Local forest repairs for the one-sided matching threshold

**Research interface, 25 October 2026. Root and independent mathematical
and data-structure reviews completed.**

This note extends the operative conservative-price interface in
any_source_fixed_tree_matching_interface.md from a fixed directed
out-forest to a dynamically maintained directed forest. Its underlying
undirected graph must remain acyclic. The forest may have several
incoming and outgoing arcs at a vertex; there is no fixed-root
ancestor restriction in this extension.

A caller may supply ordinary-arc cuts and compatible ordinary-arc
links. These edits, all-pairs directed path search inside the forest,
and an accepted implicit allocation transfer cost polynomial
logarithmic time plus the discovered register events.

The construction does not find a useful replacement arc in the
ambient allocation graph. It does not bound the number of supplied
repairs or old-potential refreshes. In particular, it does not improve
the four-fifths general-matching exponent.

## 1. Fixed semantic interval and admissible forest edits

Fix one interval with no structural ledger changes. The row/bin
allocation graph, its coordinate lifetimes, and its guarded dyadic
grid are fixed. A row has a fixed allocation sum, and the bin
equations couple allocation load to a positive slack. Use all
constants, step sizes, and semantic comparisons of the conservative
version of any_source_fixed_tree_matching_interface.md.

For each incidence e keep its current allocation x_e and persistent
register ell_e. In every settled state,

\[
 \ell_e<x_e<2\ell_e,\qquad
 \bar c_e=\left\lceil H/(4\ell_e)\right\rceil .
 \tag{1}
\]

The complete directed allocation graph contains a zero-length
receiving arc row-to-bin and a donor arc bin-to-row of length
bar c_e for each incidence. At bin v put

\[
 \sigma_v=\left\lfloor3H/(4s_v)\right\rfloor,\qquad
 \tau_v=\left\lceil5H/(4s_v)\right\rceil .
 \tag{2}
\]

There is also an artificial source with an arc of length A-sigma_v
to every bin. H is a fixed sufficiently large power of two, and A
is the fixed valid offset of the preceding interface.

Let D be fixed integer labels feasible for this complete threshold
graph, and assume that D and A have O(log S)-bit magnitude. They
need not remain exact. One permissible initialization is
the exact conservative-price SPT from the preceding note, whose
nonnegative integer distances obey that magnitude bound. Feasibility
means, in particular,

\[
 D(d)\le D(r)\le D(d)+\bar c_e,\qquad
 D(d)\le A-\sigma_d
 \tag{3}
\]

for every incidence e=(r,d).

The maintained ordinary forest F has native row and bin vertices.
It obeys the following contract.

1. Its underlying undirected multigraph is a forest.
2. A live allocation-coordinate ID occurs on at most one live
   forest edge. This is an identity requirement, not just a
   statement about endpoint names or the absence of cycles.
3. Every forest edge is one chosen direction of its physical
   incidence. Its donor or receiver role belongs to the physical
   directed arc and does not change when a dynamic-tree
   implementation changes its internal root.
4. Every selected receiving arc r-to-d is D-tight:
   D(r)=D(d). A selected donor needs only (3).

The following supplied edits are supported:

* cut a currently selected incidence;
* link an unselected incidence in one chosen direction, provided
  its endpoints are in different underlying components, its
  coordinate ID is not already selected, and a receiving link
  is D-tight;
* change an incidence's selected direction by a cut followed by
  a permissible link.

Connectivity and identity checks are part of the interface. The
caller is not allowed to duplicate one allocation coordinate in
different logical aliases and then apply a separate transfer to
each occurrence. That would invalidate both the conservation
equations and the path-lazy update described below.

Forest edits change neither the allocation vector nor D. They do
not by themselves reset ell_e. A bulk change of D, a ledger
contraction/expansion, and a numerical external assignment are not
free forest edits under this statement.

## 2. The path objective on an arbitrary directed forest

For bins a,b, let F[a,b] be the unique underlying forest path when
they are connected. It is admissible only if every edge points
from a toward b. Define

\[
 \bar L_F(a,b)=\sum_{e\text{ donor on }F[a,b]}\bar c_e,\qquad
 \mathcal{Q}(a,b)=\sigma_a-\tau_b-\bar L_F(a,b).
 \tag{4}
\]

The search returns a pair with maximum Q over all admissible
ordered bin pairs. Its threshold answer is positive exactly when
this maximum is positive. The pair a=b has score sigma_a-tau_a<0
and can never be accepted.

As before, a positive answer has true one-sided ratio greater
than one quarter. A forest path of true ratio greater than one
half has positive score. If nu is the number of row/bin vertices,
one can impose

\[
 H\min_d(1/s_d)\ge8(\nu+2)
 \tag{5}
\]

along with the semantic rounding-error requirement. This pays at
most nu donor ceilings and the two endpoint rounding operations.
All choices of H remain polynomial under the explicit guard
bounds. There is no dependence on the number of earlier pivots.

Every directed bin-to-bin path is an exact ledger direction:
each internal row loses eta on its incoming donor and gains eta
on its outgoing receiver; each internal bin has zero net load
change; its starting slack increases by eta and its terminal
slack decreases by eta. No rooted-tree orientation is used in
this argument.

## 3. Edge-local endpoint prices

A direct top-tree cache of mutable vertex endpoint scores is
unsafe at a high-degree boundary vertex: that vertex can occur
on the boundary of many clusters. Avoid that problem entirely.

Attach two new degree-one terminals to each bin v:

* a source terminal v_in with an arc v_in-to-v of score +sigma_v;
* a target terminal v_out with an arc v-to-v_out of score -tau_v.

Only source terminals may start a scored path, and only target
terminals may finish one. An ordinary donor arc has score -bar c_e;
an ordinary receiving arc has score zero. The augmented underlying
graph is still a forest and has O(nu) vertices and edges.

Every directed source-terminal to target-terminal path corresponds
to exactly one ordered ordinary bin path in (4), with the same
score. A degree-one terminal cannot be an internal vertex of a
simple path. Thus no unrequested endpoint or intermediate price
is introduced by the gadget.

All changing endpoint prices now live on individual edges.
The source/target terminal flags are immutable. A price edit
changes one top-tree leaf edge and its O(log nu) ancestors, not
all clusters incident to a bin.

Negative edge scores cause no difficulty. This data structure
maximizes the score of the unique directed path in an underlying
tree. It is not running a shortest-path algorithm on a graph with
negative cycles.

## 4. Constant-size directed top-tree state

For an edge-induced connected top-tree cluster C with at most two
boundary vertices, store the following entries.

* For ordered boundary vertices u,v, W_C(u,v) is the score of
  their unique C-path when it is directed from u to v, and is
  minus infinity otherwise. Put W_C(v,v)=0.
* I_C(v) is the best score of a directed path from a source
  terminal in C to boundary v.
* O_C(v) is the best score of a directed path from boundary v
  to a target terminal in C.
* F_C is the best score of a directed path from a source terminal
  in C to a target terminal in C.

An absent candidate has value minus infinity. Boundary entries
whose boundary does not exist are omitted. Terminal membership
is immutable, so it is safe to include a terminal endpoint even
when an expose operation makes it a boundary vertex.

Each maximum also stores its source terminal, target terminal,
or pair as appropriate. Break ties by fixed terminal IDs.
The path itself is represented by its endpoints and the current
forest; it is not expanded while recomputing a cluster.

### 4.1 Join formulas

Suppose C_1 and C_2 meet at their common boundary v and are joined
to form C. The internal best score is

\[
 F_C=\max\{
 F_{C_1},F_{C_2},
 I_{C_1}(v)+O_{C_2}(v),
 I_{C_2}(v)+O_{C_1}(v)
 \}.
 \tag{6}
\]

For a retained boundary b in C_1 other than v,

\[
\begin{aligned}
 I_C(b)&=\max\{
 I_{C_1}(b),\ I_{C_2}(v)+W_{C_1}(v,b)
 \},\\
 O_C(b)&=\max\{
 O_{C_1}(b),\ W_{C_1}(b,v)+O_{C_2}(v)
 \}.
\end{aligned}
 \tag{7}
\]

Use the symmetric formulas for a boundary in C_2. If v itself
is retained, I_C(v) and O_C(v) are the respective maxima of the
two child entries.

A retained boundary path that crosses from C_1 to C_2 has score

\[
 W_C(b_1,b_2)=W_{C_1}(b_1,v)+W_{C_2}(v,b_2).
 \tag{8}
\]

If both endpoints lie in one child, use that child's path entry;
the other child cannot create a second path in a tree. The
same convention covers an endpoint equal to v.

These formulas use a constant number of integer additions,
comparisons, and metadata combinations. They are valid because
any path crossing the two children passes through v exactly
once. Conversely, a finite cross term concatenates paths in
edge-disjoint subtrees that share only v, so it is a valid
directed simple path.

Base clusters are individual scored directed edges. Their
entries are obtained by checking the two endpoints, their
immutable terminal flags, and the one permitted direction.
Include the zero-edge path: a source terminal has I=0 at
itself, and a target terminal has O=0 at itself when the
corresponding boundary entry exists.
Split discards the derived state; join recomputes it by
(6)--(8).

### 4.2 Dynamic support and component maxima

Use the top-tree interface of Alstrup, Holm, de Lichtenberg and
Thorup, Maintaining Information in Fully-Dynamic Trees with
Top Trees, arXiv:cs/0310065v2, Theorem 1 and Section 2.1:

https://arxiv.org/html/cs/0310065v2

That interface supplies logarithmic-height clusters and
O(log nu) local joins/splits for a link, cut or expose.
Our augmentation performs constant work per such operation.
An edge-score point update changes only its base cluster and
ancestors. Equivalently, isolate and rebuild that edge through
the supported local update discipline.

Keep the F value and maximizing pair of every ordinary component
in a deterministic maximum dictionary. Before a public edit or
query transaction, remove its O(1) affected settled component
records. After all internal splits, joins and point updates,
use the original operation's endpoints to identify the O(1)
resulting settled components and insert their records. The
wrapper does not insert transient split clusters into that
dictionary. Isolated row vertices have no candidate.
An ordinary isolated bin still has its two attached price leaves
and a negative self-pair.

All changed maxima carry newly computed witness metadata.
Numerical equality alone is not a reason to retain an old pair.
The resulting search returns its maximizing bin IDs in
polynomial logarithmic time, and its forest path remains implicit.

The immutable terminal flags and edge-local prices explicitly
avoid the mutable boundary-vertex issue identified in the
source's Theorem 7.

## 5. A separate lazy allocation watcher

Maintain a second dynamic-tree representation of the ordinary
forest, without the price leaves. It shares ordinary vertex and
edge IDs with the scored forest. Apply every ordinary link/cut
to both structures before answering another external operation.

For a selected donor incidence retain

\[
 w_e=x_e-\ell_e,\qquad g_e=x_e-\chi_e,
 \tag{9}
\]

and for a selected receiving incidence retain

\[
 w_e=2\ell_e-x_e,\qquad g_e=U_e-x_e.
 \tag{10}
\]

Here chi_e,U_e are the fixed guard bounds of the numerical
interval. Along an accepted directed ordinary path, a transfer
eta decreases both w_e and g_e by exactly eta, for either role.
Maintain their path minima and a lazy additive tag, as well as
the integer sum of donor costs on a path.

The path-add/minimum operations are the ordinary exposed-path
top-tree augmentation of the source's Theorems 2--3 and
Section 2.5. Lazy tags propagate only to path children when a
cluster is split. A minimizing edge is recovered by descending
through those path children. Ordinary internal rerooting does
not change a physical incidence's donor/receiver role.

Expose exactly the ordinary a-to-b path. Therefore:

* no off-path branch receives the lazy tag;
* no endpoint-price edge receives it;
* no other occurrence of an allocation ID receives it.

Before a proposed step, query the minimum guard buffer and check
the two endpoint slack guards. A failed guard check returns its
concrete edge or endpoint witness without committing the step.

After a successful path update, repeatedly locate a nonpositive
register buffer. Recover its exact current x_e from (9) or (10),
set ell_e=3x_e/4, and replace its register buffer. The new buffer
is x_e/4 for a donor and x_e/2 for a receiver. A donor reset
updates the one scored ordinary edge and its path-sum cost;
a receiver reset changes only its off-forest reverse donor
price, not a scored forest edge.

Between register events the scored top tree is unchanged by
the implicit allocation update. This separation is essential:
the path-lazy arithmetic does not claim to recompute a global
maximum-path DP after changing every edge price individually.
Only a reported conservative-price event is a DP price edit.

### 5.1 Coordinate ownership under a cut or link

Before cutting a selected incidence, point-query its watcher
entry, pushing only the logarithmically many tags necessary to
recover its current value. Store that value in its native
allocation record, then remove the edge from both forests.
Other coordinates remain represented lazily.

To link an unselected incidence, read its explicit native
allocation record and its existing register. Initialize (9)
or (10) for its new role. The ell value is reused; a role
change is not an anchor reset. If the same physical edge is
reversed after a cut, it still needs the receiving-tightness
check when its new direction is receiving.

The selected/unselected ownership table ensures that a native
record and a lazy watcher are never simultaneously treated as
independent authoritative copies of one allocation.

## 6. Numerical validity and preservation of the old labels

Apply exactly the finite-grid step of the preceding interface.
For the accepted pair, put

\[
 V_{\rm up}=1/s_a+1/s_b+4\bar L_F(a,b)/H
\]

and choose a guarded grid step with

\[
             1/512\le\eta V_{\rm up}\le1/256.
 \tag{11}
\]

Its existence on the fixed grid, constant positive increase of
sum log s_d, and one-sided ratio guarantee use only the directed
path, its donor-cost sum, and its two endpoint slacks. They do
not use a fixed forest root or an ancestor relation.

The proof that D remains feasible also extends without change.

* A donor allocation decreases, so its register price can only
  increase at that step.
* A receiving allocation increases. Its reverse donor price can
  decrease, but its selected receiving arc was D-tight, making
  that reverse price decrease harmless.
* Other ordinary coordinates do not change.
* The source cost at a increases. At b, pre-step feasibility and
  acceptance imply

\[
 D(b)\le D(a)+\bar L_F(a,b)
       \le A-\sigma_a+\bar L_F(a,b)<A-\tau_b .
 \tag{12}
\]

  The resulting source slack is more than tau_b-sigma_b, at
  least H/(2s_b), and pays the small terminal price increase
  including rounding.

The same maximum-reciprocal argument as before keeps A valid.
The source and terminal price edges at a and b are updated
after the transfer. This is a constant number of point edits.
No row or bin label in D changes.

The conservative semantic quantity

\[
          E=\sum_d\left(s_d(A-D(d))/H-5/4\right)_+
 \tag{13}
\]

therefore remains valid. Its two changed slack terms are updated
directly. E<=5N is the same safe semantic LOW screen, under the
rounding budget fixed in the preceding interface.

FOREST-EMPTY is distinct from LOW: the former says only that
this maintained forest has no passing directed bin pair. At
fresh initialization from the exact conservative SPT, empty
search implies E<=N by the previous proof. After supplied
pivots and numerical evolution, no analogous implication is
claimed without a new completeness argument.

## 7. Complexity and history-wide register accounting

Let J be the number of accepted numerical path steps, P the
number of supplied ordinary link/cut edits, Q the number of
additional queries, and R the number of discovered register
resets in the interval.

After D and a compatible initial forest have been supplied,
the total local data-structure work is

\[
       (\nu+J+P+Q+R)\operatorname{polylog} S .
 \tag{14}
\]

Initialization of the full ambient graph and computation of
D are separate supplied costs. Space is linear in the ambient
coordinate records plus the current forest, up to the usual
linear dynamic-tree state. All scored entries have O(log S)
bits: a path has O(nu) edges, each stored integer price is
polynomially bounded, and all guard/register arithmetic uses
the fixed dyadic denominator.

The register-event argument is unaffected by forest repairs.
Immediately after a reset ell=3x/4, another reset requires x
to fall by a factor at least 4/3 or rise by a factor at least
3/2. Each later event pays a constant amount of absolute log
variation of that coordinate. A cut, link, role change, or
internal dynamic-tree reroot does not erase this history.

For each accepted step the sum of negative allocation log
variation is O(1), by (11). The accounting potential sum log x
bounds total positive variation by total negative variation
plus O((N+A_ext)log S) over explicit coordinate births,
deletions and external assignments. Consequently, across all
such intervals,

\[
       R=O\bigl(J+(N+A_{\rm ext})\log S\bigr)
 \tag{15}
\]

under the same accounting convention as the fixed-tree note.
This bound is independent of P. It pays register notifications,
not the external work of choosing useful forest edits.

## 8. What has been reduced to a separate problem

The local numerical interface no longer requires rebuilding a
static heavy-light decomposition whenever a caller supplies
one ordinary forest-edge replacement. It also searches all
directed paths in the maintained forest, including paths that
are not ancestor paths under any chosen implementation root.

The next sufficient theorem would supply, at controlled total
cost, a sequence of compatible forest repairs or potential
refreshes whenever the current forest is empty and E>5N.
It must include:

* discovery of useful ambient arcs;
* the number of actual cuts and links;
* treatment of a useful receiving arc that is not tight in D;
* any changes to D and the resulting compatibility checks;
* guard repairs and structural ledger edits.

No such theorem follows from (14)--(15). In particular, the
existing global bound on register events is not a bound on
ambient shortest-path work or on how many repair attempts fail.
This note supplies a concrete implementation target for local
repair, while leaving the global deterministic matching bound
at four fifths.

The completed reviews are recorded in
`potential_compatible_dynamic_forest_independent_audit.md` and
`potential_compatible_dynamic_forest_root_audit.md`.
