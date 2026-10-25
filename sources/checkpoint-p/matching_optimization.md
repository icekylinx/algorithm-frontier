# Continuing the arbitrary-general-matching 4/5 route

**Research continuation, 25 October 2026.** The target of this note is
still deterministic exact explicit maximum matching in arbitrary general
graphs. None of the partial results below changes the currently assembled
4/5 running-time exponent. The new shortest-path applications do not
silently replace this original target.

This continuation focuses on removing the serial repair depth from raw
cycle quality. It records three new, concrete conclusions:

1. The positive-auxiliary freezing argument used by the new distance
   detector does not transfer to ordinary circulation coordinates without
   a new comparator-extension theorem. A three-edge instance already
   shows the failure.
2. A native shortcut can safely improve a returned raw cycle without
   adding a selected child membership. The exact acceptance inequality is
   given below. However, even exhaustive shortcut improvement confined to
   the one returned terminal cycle can retain an exponential quality gap.
3. The serial-quality counterexample can be strengthened to a bipartite
   graph with **every real edge satisfying** \(g_e=\ell_e>0\), with
   constant integer labels before a standard port expansion. All local
   correction gradients vanish, the root optimum is \(3/5\), and the
   terminal optimum is exponentially small. Thus positivity and the
   one-sided logarithmic relation alone do not remove the factor.

The last example is an interface counterexample. It is not claimed to be
a reachable state of the full OAI ledger trajectory or the exact selected
support produced by the present repair code.

## 1. The specific cost that has to change

Use \(U=\log M\), \(h=\Theta(\log(U+4))\), static structural
logarithm \(g=O((p+r)h)\), local repair depth \(K\), reduction
parameter \(k=2^x\), and recursive depth \(d=O(U/x)\).

The current local provider has

\[
\begin{aligned}
 \log P&=O(U/K+g+h),\\
 \log W&=O(x+U/K+f+Kg+h),\\
 \log Q_{\rm local}&=O(Kg+h),
\end{aligned}
 \tag{1}
\]

where \(P\) bounds propagated selected changes and pool occurrences,
\(W\) bounds local work, and \(Q_{\rm local}\) is the inverse raw
cycle quality. The costly quality contribution is \(dKg\).

The present continuation does not try to make ordinary reparenting of
the same chronological windows look like a shorter dependency. The
actual first-touched validity certificate inherits the preceding
window, as proved in
`current_checkpoint/repair_window_depth_tradeoff.md`. It also does not
infer route-change notifications or ambient congestion from the already
proved small central-ID recourse of a greedy native spanner.

## 2. Why the successful auxiliary freezing proof is special

In the distance detector, retiring an auxiliary coordinate has a semantic
meaning: its vertex is reported and removed from the remaining distance
obligations. The comparison flow can retain that auxiliary's current
value. Deleting its positive barrier contribution then gives a genuine
potential charge for this operation.

An ordinary flow or matching-exchange coordinate has no such automatic
permission. A target comparison may need to change it. Keeping its exact
cost and divergence in an external register does not restore the lost
direction.

### A minimal exact counterexample

Take a directed three-edge cycle. Every edge has capacity one, lower
bound zero, and cost \(-1\). The prescribed demand is zero. Thus every
feasible flow is

\[
                          f=(z,z,z),\qquad 0\leq z\leq1.
 \tag{2}
\]

The exact optimum is \(z=1\), of cost \(-3\). Let the current flow
be \(z=\eta\), where \(0<\eta<1/10\), and consider the feasible
target cost \(F=-2\). With a small lower pad, its lower-bound barrier
price can be arbitrarily large as \(\eta\) tends to zero.

Freeze just the first ordinary edge at \(\eta\), retaining its exact
cost and divergence. Conservation forces both remaining flows also to
equal \(\eta\). The active graph is a path and has no nonzero
circulation direction. A perfect active-coordinate cycle oracle returns
LOW, even though the original target \(F=-2\) is feasible.

This failure occurs after one freeze. A bound on the number of freezes,
or a potential decrease paying for them, cannot repair correctness.
The large lower-bound price does not imply that the edge can safely be
fixed near zero; here every successful comparison increases it almost
to one.

### The exact missing semantic condition

For a frozen set \(Z\), one would need a constructive statement of the
following form:

> Whenever the original comparison target is feasible, there is a target
> comparison agreeing with the current flow on every edge of \(Z\),
> and its difference from the current state is a circulation entirely
> on active coordinates.

For arbitrary ordinary coordinates this statement is false by (2).
For matching ledgers, an analogous restriction must be justified by the
actual structural action, such as an exact locked projection or a
proved tight-set contraction. Backend route length or route congestion
does not by itself provide such a structural certificate.

This distinguishes **freezing a numerical variable** from keeping a
short direct route permanently available. The latter preserves the
original optimization problem and is examined next.

## 3. A positive local shortcut lemma

Consider a current native circulation represented as an oriented closed
walk with positive raw charge \(C\) and improving numerator \(N>0\).
Its ratio is \(\beta=N/C\). Suppose one occurrence of a subwalk
\(P:u\leadsto v\) is replaced by a current native edge or walk
\(Q:u\leadsto v\) with exactly the same immediate native endpoints.
All lengths, gradients, and physical lifts use current lifetime metadata.

Let

\[
 D=C(P)-C(Q)>0,
 \qquad \Delta=g^{\mathsf T}Q-g^{\mathsf T}P.
 \tag{3}
\]

The new object is again a native circulation. Its numerator and charge
are \(N+\Delta\) and \(C-D\). Direct cross-multiplication gives

\[
 \frac{N+\Delta}{C-D}\geq\frac NC
       \quad\Longleftrightarrow\quad
                    \Delta\geq-\beta D.
 \tag{4}
\]

Thus the replacement is certified safe whenever (4) holds. In
particular, if \(P-Q\) has zero gradient, every genuine reduction in
raw charge improves the ratio. The test uses the sum of charged
traversals before cancellation; it does not substitute a net physical
norm for that charge.

If \(Q\) is an unselected original central edge, its normal stable-core
lift is already a valid real-edge-plus-tree-path object. Using it in
this returned parent circulation does not require inserting its ID into
the persistent selected child graph. The replacement is therefore
compatible with the existing raw-answer interface, provided its native
location in the returned walk and its complete current lift are supplied.
It is not a claim that all useful replacements can be discovered within
the required time.

This is a genuine local improvement mechanism. It can reverse a
particular unnecessary route expansion and can be applied repeatedly.
The next two sections show precisely why it is not yet a new worst-case
quality theorem.

## 4. A bipartite positive-gradient serial-quality example

Fix an odd integer \(b\geq3\) and a depth \(K\geq1\). Let
\(N=b^K\). Make vertices

\[
                       v_0,v_1,\ldots,v_N,z_1,z_2.
 \tag{5}
\]

Give \(v_j\) the row color for even \(j\) and the bin color for odd
\(j\). Let \(z_1\) have the bin color and \(z_2\) the row color.
Include the base path \(v_0v_1\cdots v_N\), the three-edge return
path \(v_0z_1z_2v_N\), and the shortcut edges

\[
 e_{i,r}=v_{r b^{K-i}}v_{(r+1)b^{K-i}},
 \qquad 0\leq i<K,\quad0\leq r<b^i.
 \tag{6}
\]

Every span in (6) is odd, so the graph is bipartite. It is simple:
the spans are at least three, all shortcut pairs are distinct, and the
return path uses new internal vertices. The total number of vertices
and edges is \(O(N)\).

Orient every edge from its row endpoint to its bin endpoint. Give
every base or shortcut edge gradient and length one. The outer two
return edges also have gradient and length one; the middle return
edge \(z_2\to z_1\) has gradient and length seven. Therefore

\[
                            g_e=\ell_e>0
                       \quad\text{for every edge }e,
 \tag{7}
\]

and all labels belong to \(\{1,7\}\).

On the graph excluding the return path, \(g\) is the exact vertex
potential difference for
\(p(\text{row})=0\), \(p(\text{bin})=1\).

At stage \(i\), remove the shortcuts of level \(i\) and route each
through its \(b\) consecutive children, or through \(b\) base edges
at the final stage. All other edges keep their identity routes. This
is an endpoint-preserving simple route of stretch \(b\). Because
both the shortcut and its route lie in the same potential subgraph,

\[
                 g^{\mathsf T}\bigl(e-R_i(e)\bigr)=0
                      \quad\text{for every }i,e.
 \tag{8}
\]

The same holds for a composite correction from an original edge to
its fully expanded route. Splitting these corrections into simple
cycles cannot produce a nonzero gradient, since every such cycle lies
entirely inside the potential subgraph.

### Root and terminal optima

Traversing the return path from \(v_0\) to \(v_N\) has gradient
\(1-7+1=-5\) and length nine. Any nonreturn path between those
vertices has gradient one. Thus every simple cycle with nonzero
gradient uses the entire return path and has absolute gradient six.

At the root, the top shortcut has length one. The best cycle therefore
has

\[
                          \beta_0=\frac6{1+9}=\frac35.
 \tag{9}
\]

After all shortcuts are removed, the graph has a single nontrivial
cycle, consisting of the base path and the return path. Its optimum is

\[
                          \beta_K=\frac6{N+9}.
 \tag{10}
\]

The exact loss is \((N+9)/10=\Theta(b^K)\). Equations (7)--(10)
show that an all-positive gradient equal to the price length, together
with a root comparator above the matching client's constant LOW
threshold, does not remove the serial product at this abstract route
interface.

The example does not specify the numerical row sums, bin capacities,
or past trajectory of the full matching ledger. A theorem exploiting
those additional facts remains possible. The statement refuted here
uses only positivity, \(g=\ell\), and local route comparison.

### Bounded-degree and port form

Replace each vertex by a complete binary incidence tree of the same
sufficient height \(a=O(\log(K+2))\). Its leaves contain all old
incidences; unused leaves may remain. The maximum degree is three.
Choosing the same height at every vertex preserves bipartiteness.

Multiply each old real length and gradient by
\(H\geq100(a+1)\). Give every incidence-tree connector length one
and gradient zero. Extend the old potential constantly over each
fiber. Route substitutions still have zero correction gradient and
constant one-stage stretch \(O(b)\), including the connector walks.

The root cycle has numerator \(6H\) and length at most
\(10H+8a\), so its ratio remains above \(1/2\). Every terminal
nonzero circulation has ratio at most \(6/(N+9)\). This is the same
positive-real-edge/zero-gradient-port form used by a numerical degree
reduction. Native endpoints and lifetimes remain literal; no aliases
are identified merely because their physical images agree.

## 5. Why repairing only the returned terminal cycle is insufficient

In the preceding example, if the terminal cycle itself is supplied,
the shortcut rule of Section 3 can recognize complete expanded
shortcut subpaths and recover the short root cycle. This is useful,
but it does not give a universal reduction from a terminal ratio oracle.

For an explicit obstruction, call that graph \(A\), take
\(N\geq128\), and add a disjoint four-cycle \(B\). Orient \(B\)
according to its bipartition. Give three of its edges equal gradient
and length

\[
                          L=\lfloor N/64\rfloor
 \tag{11}
\]

and give the fourth gradient and length \(L+1\). Its unique cycle
has absolute gradient one and ratio

\[
                              \beta_B=\frac1{4L+1}.
 \tag{12}
\]

For these choices \(\beta_B>6/(N+9)\) and
\(\beta_B=\Theta(1/N)\). Keep every edge of \(B\) at every
stage. If a connected input is required, join one vertex of \(A\)
to one vertex of \(B\) by a single bridge, choosing compatible
bipartition colors. The bridge belongs to no circulation and changes
none of the ratios.

Every exact terminal ratio oracle now returns a cycle in \(B\),
since it is strictly better than the terminal cycle in \(A\).
All separate local correction scores are still zero. A procedure that
only shortens subwalks of the returned \(B\)-cycle has no opportunity
to introduce the missing \(A\)-cycle. Even an exact optimization over
the returned cycle's induced component or support has value
\(\Theta(1/N)\), while the root optimum remains at least \(3/5\).

Thus postprocessing one best terminal answer is not enough. A useful
new theorem must either expose more global candidates, change the
terminal objective so that the hidden short cycle is selected, or
control the composition quality before the terminal query. This is
different from merely improving the local safe-shortcut implementation.

## 6. A sufficiently weak new lemma that would improve matching

The needed improvement can be stated without demanding a faster
static construction or a better bound on local ambient congestion.
Keep the existing actual-size initialization, selected-only child
transcript, stable lifetimes, degree feedback, and local work
\(\exp O(x+U/K+f+Kg+h)\).

A new **one-period cycle-comparison** lemma would suffice if, at every
settled parent state, each original circulation \(c\) admits an exact
decomposition into available local correction answers and lifted
recursive circulation answers whose total positive raw charge is at
most

\[
          \Gamma^{O(\sqrt K)}\operatorname{poly}(U)
                         \|\ell c\|_1.
 \tag{13}
\]

The available family must be maintained with the same prescribed child
prefix and work bounds; an exponentially large uncharged family does
not satisfy this requirement. The numerical numerator must telescope
exactly. Equivalently, a new direct route provider with length
\(\Gamma^{O(\sqrt K)}\) and the same metadata and work bounds
would be a stronger sufficient statement.

The comparison form (13) is weaker than an edgewise short-route
guarantee. It allows a small deterministic family of maps or a
comparator-sensitive decomposition, provided the whole available family
is maintained and queried within the bound. It leaves local congestion
as large as \(k\Gamma^{O(K)}\); that cost is already permitted by
the local work envelope.

With (13), choose

\[
 t=(U/h)^{1/4},\qquad p=r=\Theta(t),\qquad
 K=\Theta(t^2),\qquad x=\Theta(U/t),\qquad d=O(t).
 \tag{14}
\]

Then the local work, propagated selected recourse, and accumulated
quality all fit \(\exp O(U^{3/4}h^{1/4})\). This is a conditional
consequence, not an algorithm or an asserted matching theorem. The
missing substance is (13), not the balancing of (14).

One promising stronger route-level target is to keep the original
short route table throughout a parent period, maintain its current
first-touched projection, and select central native IDs with the
existing sparse prefix bound. Initial-route anchor updates already
have a paid local-work bound. What remains is sparse selected-ID
maintenance under **multiple-origin incidence extraction**, together
with actual ambient route records. This is more general than native
splits, as the explicit example in
`current_checkpoint/initial_route_projection_updates.md` shows.

## 7. What the freeze potential would have to pay for on the router side

Keeping a direct central ID alive is semantically safe, unlike freezing
an ordinary flow coordinate. But a per-demand potential does not
automatically give a small child graph. The native input can have
\(m\) demand IDs while the permitted selected child has only about
\(m/k\) vertices and a subpolynomial factor more edges. Paying one
new selected ID for each individually retired long route can use
\(\Theta(m)\) IDs even when many of those routes are parallel and
one shared central representative would suffice.

Therefore a useful router-freezing theorem needs a **grouped selected-
support charge**, not just a bound on the number of expensive demand
routes. Its budget must be proportional to actual new touched anchors
and the allowed one-time initial selected credit. It must also pay for
the ensuing native-degree feedback and report the changed route owners.
Deleting a positive term from a potential does not establish those
properties by itself.

The earlier central greedy lemma already supplies small membership
recourse for actual native splits. Its missing clauses remain ambient
congestion, explicit current-route notification, and fast discovery.
The current investigation has not found a recent primary-source theorem
that supplies all of them at a quantitatively useful rate. The January
2026 Chuzhoy--Parter dynamic low-congestion spanner remains a distinct
interface: its published parameter range, existential native embedding,
and lack of the needed split/ambient/notification clauses are recorded in
`current_checkpoint/chuzhoy_parter_2026_interface_boundary.md`.

The next substantive advance must prove a comparison such as (13), or
the grouped fixed-base maintenance statement just described. Neither
the new auxiliary freeze potential nor local shortcut recovery currently
does so. The accepted arbitrary-general-graph matching exponent remains
4/5.
