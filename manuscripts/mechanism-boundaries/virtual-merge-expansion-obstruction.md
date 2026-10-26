# Concentrated boundary vertices can force a degree loss in a virtual merge

**Separate mathematical follow-up, 24 October 2026.** This note does not
change the reviewed sequential router or any matching checkpoint. It
gives a simple-graph family showing that one degree-dependent loss in
the current virtual-merge lemma is real under that lemma's hypotheses.
It is not a lower bound for deterministic routing, and it does not
assert that a repeated version is reachable by the complete recursive
cut-matching construction.

## 1. The interface being tested

The merge in
[../graph-backends/virtual-expander-hierarchy-reconstruction.md](../graph-backends/virtual-expander-hierarchy-reconstruction.md),
Section 2, has disjoint blocks $U_i$, an internal graph $H_i$ on
each block, and genuine host edges between blocks. Assume that

* every $H_i$ has edge sparsity at least $\sigma$;
* every cut respecting whole blocks has boundary at least its
  smaller vertex mass, so the coarse outer sparsity is at least one;
* the host has maximum degree $\Delta$.

The direct majority-rounding argument gives merged sparsity
$\Omega(\sigma/(\Delta+1))$. The following construction shows that
the factor $\Delta$ cannot simply be removed from this interface,
even when every child embedding is the identity.

All sparsities below use vertex cardinality, rather than degree
volume:
$$
\Psi(H)=\min_{\varnothing\ne S\subsetneq V(H)}
   \frac{|\partial_H S|}{\min\{|S|,|V(H)\setminus S|\}}.
$$

## 2. Explicit simple-graph construction

Choose integers
$$
D\geq4,\qquad a\geq D,\qquad 1\leq r\leq a,
             \qquad \sigma_0=r/a.
$$
There are two equal blocks
$$
U_1=P_1\mathbin{\dot\cup}C_1,\qquad
 U_2=P_2\mathbin{\dot\cup}C_2,
 \qquad |P_i|=a,\quad |C_i|=(D-1)a.
 \tag{1}
$$
Thus each block has $Da$ vertices. The sets $P_i$ are the
boundary vertices; the larger $C_i$ have no edge to the other block.

Place a fixed-degree simple edge expander on each of the four sets.
There are absolute constants $\alpha>0$ and $d_0$ for which all
four internal graphs have sparsity at least $\alpha$ and maximum
degree at most $d_0$. One can use the deterministic arbitrary-size
construction in
[Chuzhoy et al., arXiv:1910.08025v2, Theorem 2.4](https://arxiv.org/pdf/1910.08025).
Removing loops and retaining one copy of each parallel pair loses
only a constant expansion factor because its maximum degree is an
absolute constant. Small constant-size cases can be fixed separately.
Decrease $\alpha$ if necessary so that $\alpha\leq1$.

Inside each $U_i$, add $r$ independent edges between $P_i$ and
$C_i$. This is possible since $r\leq a$. Let $H_i$ be the
resulting graph. Its maximum degree is at most $d_0+1$.

Label both $P_1$ and $P_2$ by residues modulo $a$. Add the
following genuine interblock edges:
$$
xy\quad\Longleftrightarrow\quad
     x\in P_1,\ y\in P_2,\quad
     y-x\pmod a\in\{0,1,\ldots,D-1\}.
 \tag{2}
$$
Because $D\leq a$, (2) is a simple $D$-regular bipartite graph.
The final host and the virtual merge are the same graph:
$$
G_0=G=H_1\cup H_2\cup E_{\rm cross}.
 \tag{3}
$$
The children embed into it by literal inclusion, with dilation and
congestion one. All graphs in this construction are loopless and
simple; no multiplicity convention is needed.

The maximum degree of $G$ is between $D$ and $D+d_0+1$, hence
$$
\Delta=\Theta(D).
 \tag{4}
$$
There are exactly $Da$ interblock edges. The only nontrivial cut
respecting the two blocks has smaller mass $Da$, so its outer
sparsity is exactly one.

## 3. Child sparsity is $\Theta(r/a)$

The cut $P_i$ has exactly $r$ crossing edges and smaller side
$a$, proving $\Psi(H_i)\leq\sigma_0$. We prove the matching
lower bound without assuming anything about the positions of the
$r$ independent connecting edges.

Fix $H_i$, and take a smaller cut side $S$, with
$$
w=|S|\leq Da/2,\qquad
 x=|S\cap C_i|,\qquad y=|S\cap P_i|.
$$

If $x>|C_i|/2$, then
$$
|C_i|-x\geq(D/2-1)a\geq w/2,
$$
where the second inequality uses $D\geq4$ and $w\leq Da/2$.
The core expander alone contributes at least $\alpha w/2$.

Suppose next that $x\leq|C_i|/2$. If $y\leq a/2$, the two
internal expanders contribute at least $\alpha(x+y)=\alpha w$.
If $y>a/2$ and $x\geq a$, the core contributes at least
$\alpha x\geq\alpha w/2$.

The remaining case is $y>a/2$ and $x<a$, so $w<2a$. Put
$$
z=x+(a-y).
 \tag{5}
$$
The internal expanders give at least $\alpha z$ crossing edges.
If $z\geq r/2$, this is at least
$$
\alpha r/2\geq(\alpha/4)\sigma_0 w.
 \tag{6}
$$
If $z<r/2$, at most $x+(a-y)=z$ of the $r$ independent
connecting edges can fail to cross from $S\cap P_i$ to
$C_i\setminus S$: every such failure uses a distinct endpoint in
$S\cap C_i$ or $P_i\setminus S$. Consequently more than $r/2$
of them cross, again giving at least $\sigma_0 w/4$.

All cases imply
$$
\frac{\alpha}{4}\sigma_0
                        \leq\Psi(H_i)\leq\sigma_0.
 \tag{7}
$$

## 4. The merged graph loses a factor $\Theta(D)$

Consider the cut $C_1$ in $G$. Its only crossing edges are the
$r$ independent edges from $C_1$ to $P_1$. The other block is
accessible only through the small boundary set $P_1$. Since
$|C_1|=(D-1)a<|V(G)|/2=Da$,
$$
\Psi(G)\leq\frac{r}{(D-1)a}
                      =\frac{\sigma_0}{D-1}.
 \tag{8}
$$
Equations (4), (7), and (8) give
$$
\Psi(G)=O\!\left(\frac{\min_i\Psi(H_i)}{\Delta}\right).
 \tag{9}
$$
The lower bound of the existing majority-rounding merge lemma
shows that this order is also sufficient for this family, up to
absolute constants.

Thus excellent coarse expansion and perfect child embeddings do
not force the fine graph to retain a constant fraction of child
expansion. Coarse edges can be concentrated on a $1/D$ fraction
of each block. A cut can then retain almost an entire child while
avoiding all coarse edges.

## 5. Consequences and precise limits

The current hierarchy has matching-host degree
$\Delta=O(\log n)$. The example shows that its stated merge
hypotheses alone cannot replace a per-merge inverse polynomial
in $\log n$ by a fixed constant. A stronger invariant would be
needed, such as a suitable distribution of cross-block incidences
relative to every potentially weak child cut.

This is only a one-merge obstruction. It establishes none of the
following:

* a lower bound on the depth dependence of every router;
* a matching hierarchy for which this loss compounds at every level;
* reachability of this exact graph by the particular deterministic
  cut-player and matching-player choices;
* a lower bound for a construction allowed to change its virtual
  cross edges or reroute them through children.

Replacing concentrated cross edges by better distributed virtual
edges is a possible algorithmic direction. It requires an explicit
embedding with controlled congestion. Routing those new edges
inside a child using only its current expansion guarantee can pay
an inverse-child-expansion factor, so that operation needs its own
cost proof. Merely assigning larger weights or multiplicities to
internal child edges moves the burden to the root embedding and
does not by itself improve the physical routing bound.

The reviewed $4/5$ composition and its actual sequential router
remain unchanged by this follow-up.
