# Proof note

This file is the curated proof record for the result in `README.md`. The original source note follows.

**Original source:** `sources/checkpoint-q/six_sevenths_strong_forest_and_gomory_hu_checkpoint.md`

# Checkpoint E: a six-sevenths strong forest and exact Gomory--Hu consequence

**Research proof assembly, 25 October 2026.** The root and two independent
agents have read the complete no-recursive-reset construction and its
interfaces. This is an internally audited mathematical construction with
named imported theorems. It is not an implementation, a formal proof
artifact, or external certification.

The main unrestricted exact general-graph matching result remains
\[
 O(n+m)+(m_s+1)
   \exp O\!\left((\log(m_s+2))^{4/5}
                     (\log\log(m_s+4))^{1/5}\right).
\]
The new improvement concerns a different general-graph problem:
exact deterministic cut-equivalent trees, through a stronger explicit
decremental shortest-path forest.

## 1. Current result and the fair comparison

Put \(U=\log(N+4)\), \(h=\log(U+4)\), and
\[
                         E_6(N)=\exp O(U^{6/7}h^{1/7}).
\]
Here \(N\) is a polynomial upper bound on the actual input and necessary
update history. Initializations are always charged to actual inventories;
the numerical bound does not permit master-sized padding.

| Construction | Logarithm of the overhead factor | Status |
|---|---|---|
| Public KMG strong-forest specialization | \(O(U^{83/84}h)\) | Printed public theorem |
| Strongest public reconstruction established in this checkpoint | \(O(U^{8/9}h^{1/9})\) | Our reanalysis of public ingredients |
| Previous research strong forest | \(O(U^{7/8}h^{1/8})\) | Earlier internally audited construction |
| Uncontracted compressed cores and colored pools | \(O(U^{6/7}h^{1/7})\) | New construction audited in checkpoint E |

The \(8/9\) comparison is essential. It improves earlier restricted
public comparisons by tracking input forest **nodes** directly in the
existing public copy construction. That accounting insight alone is
not an exclusive advantage of the new pool mechanism.

Primary public sources are [KMG, arXiv:2311.06402v1]
(https://arxiv.org/pdf/2311.06402v1), especially Sections 3--5, and
the deterministic Gomory--Hu reduction [arXiv:2507.20354v1]
(https://arxiv.org/html/2507.20354v1). The latter already establishes
deterministic almost-linear exact cut-equivalent trees. This checkpoint
improves an explicit subpolynomial factor; it does not claim the first
almost-linear algorithm for that problem.

## 2. Strong decremental SSSP contract

For an undirected bounded-degree graph with a fixed native vertex set,
positive polynomial-range integer lengths, fixed source \(s\), and
edge deletions, maintain an explicit flat forest \(F\), fixed canonical
node injection \(\iota\), vertex-image map \(\pi\), and original-edge
embedding \(\eta\). For constant or inverse-polylogarithmic
\(\varepsilon>0\), the properties are:

1. Each living original vertex \(v\) has a permanent node
   \(\iota(v)\), and \(\pi(\iota(v))=v\). Every other forest node
   also has a fixed physical image during its lifetime.
2. Every exposed forest edge is a copy of a currently present native
   edge with its actual length. Intermediate true-null edges are
   contracted before this final interface is published.
3. A reachable \(v\) has its canonical node in the source's tree,
   and the forest path has physical length at most
   \((1+\varepsilon)d_G(s,v)\). Its projection is a valid native
   walk. Unreachable canonical nodes are retained.
4. Vertex and edge occurrence, total explicit forest size, and total
   map/forest recourse fit fixed powers of \(E_6\).
5. Initialization and the entire deletion sequence take
   \(O((n+m)E_6)\) total work, absorbing fixed powers into its
   constant exponent. A dynamic tree reports the current forest
   path with polynomial-logarithmic overhead per reported edge.

This is a total-time decremental result, not a new worst-case
per-update theorem. Reporting the projected walk and erasing its
loops takes time proportional to that reported walk. An ordinary
simple-path query bound depending only on the final erased path
is not asserted here.

The bounded-degree condition belongs to the native strong-forest
interface. Arbitrary-degree application graphs use the previously
audited actual-size degree adapter. Pointwise native vertex congestion
is not silently claimed to remain unchanged when many port vertices
are later regarded as one original high-degree vertex.

The complete new construction is
**steiner_pool_no_reset_strong_forest.md**. It replaces only the
inner low-diameter forest interface of the existing outer cover,
ball, hopset, and flattening construction.

## 3. What changes in the construction

An old selected core edge is represented at contracted stable-tree
roots. Those roots can have large selected degree even when the
physical graph has small degree.

The new child puts each selected edge back at its actual physical
endpoints. In every stable core forest it marks active roots and
selected endpoints, then suppresses unmarked degree-two paths.
Every compressed edge keeps an exact dynamic-tree path description.
A mark insertion/deletion or physical core cut changes only
constantly many compressed records; a long path is not enumerated.

If the parent native degree is \(\Delta_j\), the next child degree is
at most \(\operatorname{poly}(U)\Delta_j\). The hierarchy therefore
needs no recursive port reset:
\[
                  \log\Delta_j=O(jh).
\]
Native child names inject into parent names. An isolated inactive name
can stay for the current period without creating many aliases at the
same physical point. The entire private generation retires at a
rebuild, while original canonical identifiers survive.

For a flat or typed-null input forest with at most \(C\) nodes per
child vertex, a fixed virtual edge has at most \(2C-1\) occurrences.
Color the compressed core forest with \(2\Delta_j-1\) base colors,
and give those occurrences separate slots in \(1,\ldots,2C\).
Each pair consisting of a base color and a slot receives a copy of
the full stable core forest.

In a pool, cut one stored physical key edge on every unused virtual
path. Paths used in one pool are vertex-disjoint, and any two of
them would be separated by an unused path's key cut. Each attached
component therefore realizes just one input edge, with harmless
hanging branches. The union is a forest because contracting its
used routes recovers the original input forest.

All unused pool nodes are counted. The simultaneous occurrence
recurrence is
\[
 C_j\le \operatorname{poly}(U)\Delta_j(C_{j+1}+1).
\]
It is linear in the incoming occurrence capacity and independent
of the large selected-update factor \(P\). The latter is still
paid in update work and explicit recourse.

## 4. The parameter calculation with the necessary separation

Write \(k=e^x\), \(d=O(U/x)\), and
\[
\begin{aligned}
 g&=O((p+r)h),&
 f&=O(U/p+U/r+r^2h+(p+r)h),\\
 \log P&=O(U/K+g+h).
\end{aligned}
\]
The three inner quantities are different:
\[
\begin{aligned}
 a&=O(dKg+dh) &&\text{metric log-distortion},\\
 c&=O(d^2h+h) &&\text{vertex/edge log-occurrence},\\
 B&=O(x+f+K^2g+d\log P+d^2h+h)
                       &&\text{log-work and explicit recourse}.
\end{aligned}
\]
Even the conservative older \(K^2g\) repair term fits. The stronger
normalized repair is useful elsewhere but is not necessary for
this particular strong-forest balance.

The public outer construction requires
\[
 K_{\mathrm{cov}}\Lambda(a+O(h))\le c_0U
\]
and has logarithmic total work
\[
 O\!\left(B+U/\Lambda+U/K_{\mathrm{cov}}
                 +\Lambda U/K_{\mathrm{cov}}+\Lambda c+h\right).
\]
KMG's copy count uses vertex occurrence \(e^c\). Local construction
and its larger edit transcript \(e^B\) are paid once and forwarded
through those copies; the entire local algorithm is not rerun at
every outer copy level.

Take \(U=t^7h\), \(p=r=d=\Lambda=\Theta(t)\),
\(K=K_{\mathrm{cov}}=\Theta(t^2)\), and \(x=\Theta(U/t)\).
Then
\[
 a=O(t^4h),\qquad c=O(t^2h),\qquad B=O(t^6h).
\]
The cover product is \(O(t^7h)\), and fixed constants satisfy
its required inequality. The outer work is \(O(t^6h)\), which
is the \(6/7\) exponent in \(E_6\).

## 5. Exact deterministic Gomory--Hu trees

For an arbitrary undirected graph, including parallel edges and
disconnected components, with positive polynomial-range integer
capacities on nonloop edges, the audited deterministic reduction
now gives an exact cut-equivalent tree in
\[
                      O(n+m)+(m+1)E_6(n+m).
\]
Loops are irrelevant to cuts and may be removed. Component trees
can be joined by zero-weight tree edges. Thus for every pair of
original vertices, the minimum edge weight on their tree path
equals their exact minimum-cut value, including zero across
different connected components.

The reduction previously consumed the \(7/8\) strong-forest
interface only through fixed polynomial powers of its work,
size, occurrence, recourse, and canonical-map bounds. The new
interface supplies the same objects with \(E_6\). The original
application audits still pay for:

* actual-size bounded-degree expansion and artificial root edges;
* multi-source extraction from an explicit flat forest;
* finite-precision multiplicative-weights arithmetic and its
  number of distance/forest operations;
* Li's skeleton size and its cut-value growth, both with the
  explicitly checked \(5/6\) scale;
* fixed-\(k\) guide trees and the global maximum over all leaf
  gadgets, including the source-arm cases;
* all graph contractions, guide-family inventory, recursion,
  and final exact tree construction.

The separately audited exact flow factor is at most the \(4/5\)
scale. The skeleton factor has leading power \(5/6\). Both are
asymptotically absorbed by \(E_6\), even with fixed powers and
fixed polylogarithmic factors. Replacing the forest interface
therefore introduces no new larger term.

This is a substitution of a fully specified strong forest,
not a claim that faster static maximum flow alone yields the
Gomory--Hu improvement. The relevant existing application notes are
**gomory_hu_seven_eighths_dependency_audit.md**,
**gomory_hu_adapter_independent_audit.md**,
**finite_mwu_and_li_skeleton_independent_audit.md**,
**gomory_hu_external_factors_except_fixed_k.md**,
**fixed_k_tree_mincut_source_interface_audit.md**,
**fixed_k_global_max_leaf_independent_audit.md**, and
**fixed_k_global_max_third_audit.md**.

## 6. Audit resolutions that matter to correctness

The completed construction includes several details that a parameter
table alone would miss.

Initially small disconnected components keep their common roots
private until an actual native event or explicit anchor promotion
activates them. Otherwise one would export linearly many child
roots and lose the required size reduction. A promotion counts even
when it causes no physical cut.

The input to a recursive lift includes typed true-null edges with
no ambient edge identity. Forwarding them explicitly closes the
interface under composition. Contracting all physical coincidences
would incorrectly merge different input nodes.

The palettes count \(2C-1\) possible occurrences of a fixed edge,
not only \(C\). Every full unused forest copy is charged. New key
cuts are installed before old masks are restored, and deleted
physical keys are never revived.

KMG Definition 5.2 bounds cover overlap over all times. A native
birth-cover ghost therefore still has a charged historical owner
after it leaves the active cover. This avoids inventing an
unsupported vertex-deletion operation in the public native provider.

The initialization recurrence retains child updates emitted from
initial credit at a later time. Original canonical identifiers
survive whole-period replacements. The metric proof uses only
pivot pairs and a forced anchor; it imposes no finite-diameter
requirement on arbitrary unused Steiner components.

The two completed independent reviews are
**compressed_steiner_pool_independent_audit.md** and
**steiner_pool_metric_inventory_focused_audit.md**. The root
independently proved the marked-Steiner local lemma, the pool
connectivity/count argument, and reread the complete final
construction and relevant public copy/cover statements.

## 7. What remains open

The matching exponent is unchanged. Its raw-cycle quality still
contains the accumulated metric/correction loss; the new forest
occurrence bound does not remove that charge.

The new \(6/7\) balance also has a nonuniform positive-budget
obstruction, proved in **nonuniform_parameter_budget_frontiers.md**:
combining the remaining inner metric/work tradeoff with the outer
scale condition yields \(Z^7=\Omega(U^6h)\) in that specified
accounting model. This is not an algorithmic lower bound.

Further work is testing bounded-length path reporting for dynamic
spanner clients, the matching-specific potential certificate and
coarse directed-path interface, and other transfers with fully
checked baselines. Unfinished MSF and weak-Haxell notes are not
additional proved improvements in this checkpoint.


---

**Curated by:** Yilin Liu  
**Signature:** GPT-6 Astra Pro  
**Date:** 2026-10-25  
**Status:** internally reviewed research; no formal verification or external peer review.
