# Two explicit boundaries in the CHS routing reconstruction

This note concerns a proposed sequential use of
[Chang--Huang--Su, arXiv:2405.03908v1](https://arxiv.org/abs/2405.03908).
It records two implications that require additional proofs or modifications.
Neither affects the separate CS21-based construction. This is not a
disproof of the published top-level distributed routing theorem.

The independent polynomial-work repairs for leaf preprocessing and the
exhaustive energy-cut search are in
[sequential_leaf_routing_and_chs_work.md](sequential_leaf_routing_and_chs_work.md)
and [polynomial_energy_cut_player.md](polynomial_energy_cut_player.md).
They do not automatically resolve the interfaces below.

## 1. Terminal unions and induced expanders are different objects

CHS Appendix A, Step 3, identifies a successful parent \(X\) with a union of
terminal sets \(U_i^*=U_i\cup U_i'\), where \(U_i'\) consists of vertices
matched to \(U_i\). Its Property 3.1 requires the child parts to partition
\(X\), and associates the root with \(H_X=G[X]\).

The cited [Chang--Saranurak source, arXiv:2007.14898](https://arxiv.org/abs/2007.14898),
Section 4.3, Lemma 4.10, instead defines \(W^*\) to contain **all vertices used
by the embedded paths** of the surviving graphs \(H_i^*\). Its Lemma C.9 proves
expansion for \(G[W^*]\). It does not state that all internal path vertices
belong to the terminal union \(\bigcup_i U_i^*\).

### 1.1 An explicit distinction

Let \(U_1=\{a_1,a_2\}\) and \(U_2=\{b_1,b_2\}\), with each \(H_i\) a single
edge. Embed their edges by \(a_1-x_1-a_2\) and \(b_1-x_2-b_2\), and add genuine
edges \(a_1b_1,a_2b_2\). The host is a six-cycle. The child expanders have
expansion one, their embedding has dilation two and congestion one, and the
cut respecting the two terminal groups has outer expansion one.

The host induced by all embedding vertices has positive expansion.
In contrast, \(G[U_1\cup U_2]\) consists of two disjoint edges and has
expansion zero. Thus the hypotheses of the embedding-to-induced-expander
lemma do not permit replacing all path vertices by the terminal union.
This example refutes the implication; it is not asserted to be a complete
execution trace of the source cut-matching algorithm.

### 1.2 A possible repair changes the recursive interface

CS20 Lemma C.9's proof constructs a graph \(G_0\) on the terminal union:
retain genuine edges between terminal parts and replace each part's internal
graph by its expander \(H_i^*\). The proof establishes expansion for this
virtual graph and a controlled embedding into the parent host.

Using \(G_0\) is promising, but changes the recursive certificate. The
original cut player terminates with an induced expander in its current
matching-union graph. A virtual expander with an embedding is different.
A repair must preserve the child partition and simultaneous-embedding
bounds, rather than silently identify these objects.

Rebuilding a fresh hierarchy on each returned induced expander also needs a
new cost proof. Its expansion may already be \((\log n)^{-O(p)}\), where
\(p=1/\epsilon\). An inverse-expansion factor at every level could produce
\((\log n)^{O(p^2)}\), rather than \((\log n)^{O(p)}\).

## 2. Task 2's promise does not imply Task 3's promise

CHS Definition 3.7 sets
\[
 \rho_{\rm best}=\max_{Y\in\mathcal T}|Y|/|Y_{\rm best}|.
\]
Task 2, Definition 4.2, permits \(L\rho_{\rm best}\) tokens per best-vertex
destination. Marking destinations by a child part proves only
\[
 N_j\leq L\rho_{\rm best}|X_{\rm best}\cap X_j^*|.
 \tag{1}
\]
Task 3, Definition 4.3, assumes
\[
 N_j\leq L|X_j^*|.
 \tag{2}
\]
The global maximum inverse density does not turn (1) into (2).
Theorem 6.8 nevertheless invokes Task 3 with the same \(L\).

### 2.1 A uniform-depth toy hierarchy

Fix \(k\geq2\) and put \(h=k^4\). The root has \(k\) equal parts of size
\(2kh\), each entirely a good child. Each good child has \(k\) parts of size
\(2h\).

For all but one root child, every grandchild part is entirely good. For the
remaining root child, each grandchild part has a good leaf of size \(h\) and
\(h\) bad vertices, matched injectively to that leaf. All good leaves have
the same depth and sizes between \(k^4\) and \(2k^4\). The part-size and
good/bad counting conditions of Property 3.1 hold. Bounded-degree expanders
and matching links can be placed on these sets; disconnected good nodes are
not the reason for the example.

The root has \(n=2k^2h\) vertices. A high-density root child has \(2kh\)
best vertices, while the low-density child has \(kh\). Thus
\[
 \rho_{\rm best}=2,\qquad |X_{\rm best}|=n-kh.
 \tag{3}
\]
With \(L=1\), put \(2kh+1\) tokens at distinct root vertices and give all of
them destinations in one high-density child, with at most two per destination.
This satisfies Task 2 but violates Task 3:
\[
 N_j=2kh+1>2kh=|X_j^*|.
\]

This also interacts with the modular map in Appendix D. Order a high-density
child's best vertices first, and give the original vertices compact IDs
\(0,\ldots,n-1\). Under
\[
 h(v)=\mathrm{ID}(v)\bmod |X_{\rm best}|,
\]
the first \(kh=n-|X_{\rm best}|\) best ranks have two preimages.
One token created at every original vertex, as in the described preprocessing,
therefore gives \(3kh\) destinations in the first high-density child, which
has only \(2kh\) vertices. The missing inequality is relevant to a described
caller, not merely an arbitrary formal Task 2 instance.

### 2.2 What a repair would have to track

One possible strengthened invariant bounds destinations in every descendant
part. Another observation repairs a standalone Task 2 call: inflate its
initial active load once by \(\rho_{\rm best}\). The per-destination count is
then at most that active load, and recursive loads need not acquire another
\(\rho_{\rm best}\) factor solely for this reason.

That observation is not yet a complete accounting for the mutually recursive
routing, sorting, and preprocessing calls. Precompiled comparator routes and
all-to-best routes must be charged consistently. A proof cannot introduce a
new \(\rho_{\rm best}\) factor at every boundary and quote the old recurrence.

## 3. Current scope

The polynomial-work leaf router and energy-cut construction remain independent
lemmas. A sequential CHS-based theorem with
\(\log\Gamma=O(p\log\log n+\log\phi^{-1})\) still requires a complete hierarchy
and load-composition argument addressing Sections 1 and 2.
No improvement to the matching exponent is inferred from CHS here.
