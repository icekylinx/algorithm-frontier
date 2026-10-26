# Explicit sequential preprocessing for the leaf routing step

This note isolates a constructive repair to one sequential-work boundary in
[Chang--Huang--Su, arXiv:2405.03908v1](https://arxiv.org/abs/2405.03908).
It does not infer sequential work by multiplying the stated CONGEST round
bound by the number of edges.

The source's Section 6.4 gathers the topology of a leaf graph and then computes
an embedded sorting network using unrestricted local computation. Appendix B.1
has a separate exhaustive cut-player search. The lemma below replaces the leaf
step by a polynomial-work construction. A complete sequential interpretation
also needs a constructive replacement for Appendix B.1 and an explicit work
account for the inherited hierarchy.

## 1. A small-graph permutation-routing lemma

Let $H$ be a connected loopless undirected multigraph with $h\geq2$ vertices,
maximum degree at most $\Delta$, and edge expansion at least $\psi>0$:
$$
|\partial_H X|\geq\psi\min\{|X|,h-|X|\}.
$$
Parallel edges retain distinct IDs. Suppose a list of demands has at most
$b=O(1)$ occurrences of each vertex as a source and as a destination.

There is a deterministic algorithm, polynomial in
$h,\Delta,\psi^{-1}$ and the bit size of the stated lower bound $\psi$,
that produces an explicit path for each demand with
$$
\operatorname{length}\leq 2T,\qquad
 \operatorname{edge\ congestion}=O(bT\log(h+\Delta+2)),
 \tag{1}
$$
where
$$
T=O(\Delta^2\psi^{-2}\log(h+2)).
 \tag{2}
$$
The polynomial has fixed degree. In particular, it does not enumerate paths or
cuts exponentially in $h$.

### 1.1 A finite rational distribution of short walks

Let $D$ be a power of two satisfying
$\max\{1,\Delta\}\leq D<2\max\{1,\Delta\}$. Define a symmetric lazy transition
matrix $P$ by assigning probability $1/(2D)$ to each oriented genuine edge
ID and using the remaining probability at each vertex as a holding step.
Holding steps are bookkeeping, not extra genuine graph edges.

The stationary distribution is uniform. The conductance of this chain is at
least $\psi/(2D)$. The usual elementary conductance-to-spectral-gap bound,
followed by the spectral expansion of the symmetric lazy matrix, gives
$$
P^T(u,v)\geq\frac1{2h}\quad\hbox{for every }u,v
 \tag{3}
$$
when $T$ is a sufficiently large integer multiple of
$D^2\psi^{-2}\lceil\log_2(2h)\rceil$.
Equivalently, (3) may be checked directly by exact matrix multiplication while
doubling $T$; the bound (2) controls how many such doublings are necessary.
Thus the algorithm does not need an exact eigenvalue computation.

For a demand $a\to b'$, choose an intermediate vertex $z$ uniformly from
$V(H)$. Choose a length-$T$ $P$-walk from $a$ conditioned on ending at
$z$, and independently such a walk from $b'$ to $z$. Concatenate the first
walk and the reversal of the second. This is a distribution on walks of length
at most $2T$ after holding steps are omitted.

The marginal distribution of either half has density at most two relative to
an unconditioned $T$-step walk: a walk ending at $z$ is reweighted by
$$
\frac{1}{hP^T(a,z)}\leq2.
 \tag{4}
$$
For any fixed genuine undirected edge ID $e$, $b$ walks started at each
vertex have total expected traversals of $e$ at most $bT/D$, since $P$ is
doubly stochastic. Applying (4) to both halves gives
$$
\sum_{\text{demands }d}\mathbb E[N_e(d)]\leq 4bT/D.
 \tag{5}
$$
Here $N_e(d)$ counts repeated traversals, so this estimate does not confuse
edge occurrence congestion with the number of distinct paths using an edge.

### 1.2 Deterministic conditional expectations

Choose all demand walks independently for the analysis and put
$$
q=1+\frac1{2T},\qquad
 \Phi=\sum_{e\in E(H)}q^{\sum_d N_e(d)}.
 \tag{6}
$$
For $0\leq x\leq2T$, convexity gives
$$
q^x\leq 1+\frac{x}{2T}(q^{2T}-1)
       \leq1+\frac{(e-1)x}{2T}.
 \tag{7}
$$
Independence, (5), and $1+x\leq e^x$ imply
$$
\mathbb E[\Phi]\leq |E(H)|\exp(2b(e-1)/D).
 \tag{8}
$$
Fix first an intermediate vertex and then the two walks, one next-step choice
at a time, always choosing a positive-probability option whose conditional
expectation is no larger than the current one. Such an option exists by
averaging. A next-step choice specifies an oriented genuine edge ID or the
holding symbol, rather than only a neighboring vertex; this preserves the
separate congestion accounting for parallel IDs. At the end, (8) and
$\log(1+1/(2T))\geq1/(4T)$ prove (1).

Every conditional expectation in this procedure is computable in polynomial
time with exact rational arithmetic. For a fixed edge ID $e$, let $P_e$
be $P$ with that edge's two oriented contributions multiplied by $q$.
If the intermediate vertex is not fixed, the moment for a demand is
$$
\mathbb E[q^{N_e(d)}]
 =\frac1h\sum_z
   \frac{P_e^T(a,z)}{P^T(a,z)}
   \frac{P_e^T(b',z)}{P^T(b',z)}.
 \tag{9}
$$
After fixing an intermediate vertex and a prefix, the corresponding factor is
the known prefix factor times
$$
\frac{P_e^{\,T-j}(v,z)}{P^{\,T-j}(v,z)}.
 \tag{10}
$$
Zero-probability choices are omitted. Products of these factors over the
unfixed independent demands, followed by a sum over edge IDs, evaluate (6).
Parallel edge IDs are weighted separately in $P_e$.

The matrices in (9)--(10) have rational entries with numerators and
denominators of $O(T\log(DT))$ bits before sums and products. Even using
unsophisticated exact rational operations, all subsequent bit lengths are
polynomial in $h,\Delta,T$. There are only polynomially many choices and
matrix computations. This is sufficient for the small-graph application; no
near-linear local matrix algorithm is claimed.

Finally erase holding steps and erase cycles from each selected walk by a
stack traversal. Endpoints are preserved, and both length and every
edge-occurrence load can only decrease. The returned routes are actual simple
paths with original edge IDs. A demand with identical endpoints uses the empty
path from the outset.

## 2. A constructive leaf sorting network

Replace the source's existential embedded AKS network by a standard
constructible bitonic sorting network. It has $O(\log^2(h+2))$ comparator
layers. Padding to a power of two creates fewer than $2h$ positions; assign
at most two positions to any physical vertex. Consequently each layer is a
demand list with the constant endpoint multiplicity allowed above.

Preprocess each layer using Section 1. The resulting explicit route inventory
has polynomial size and is computed in fixed polynomial time in
$h,\Delta,\psi^{-1}$. Its union congestion and concatenated path lengths are
bounded by a fixed polynomial in
$\Delta,\psi^{-1},\log(h+2)$.

For blocks of $L$ tokens at a position, initially sort each local block and
then implement a comparator by merging its two sorted blocks and returning
the smaller and larger halves. This takes linear work in the block size per
comparator after the initial local sorts. Moving blocks uses the precomputed
paths; reversing a previous route is explicit. All real and dummy token
trajectories needed by the meet-in-the-middle construction can therefore be
recorded and subsequently reversed with work proportional to their recorded
lengths. The logarithmic-depth AKS property is unnecessary: replacing it by
the extra logarithmic factor of a bitonic network remains inside the source's
polylogarithmic factors.

For completeness, the compare-split block implementation is correct for the
bitonic network by the usual zero-one induction. After fixing any threshold,
a bitonic input has its zeros in one cyclic interval. At a bitonic-merge
stage, pairing opposite blocks and placing the smaller $L$ entries first
folds that interval into two bitonic halves. If the total number of zeros is
at most half the total number of positions, the second half has no zeros;
if it is at least half, the first half consists entirely of zeros. Recursing
on the halves therefore sorts the zero-one sequence. This holds for every
threshold, and hence for the original ordered keys. Padding tokens use a
sentinel larger than every genuine key.

In CHS Section 6.4 the leaf size is $h=O(k^4)$, with
$k=n^{1/p}$, and the leaf's expansion lower bound has inverse
$\operatorname{poly}(\psi_{\rm root}^{-1},(\log n)^p)$.
Thus the replacement costs
$$
\operatorname{poly}(k,\psi_{\rm root}^{-1},(\log n)^p)
 \tag{11}
$$
per leaf, with fixed polynomial degree. Leaf vertex sets are disjoint.
Even the deliberately loose sum of (11) over at most $n$ leaves is
$$
n\exp\!\left(O\!\left(\frac{\log n}{p}
               +p\log\log(n+2)+\log\psi_{\rm root}^{-1}\right)\right).
 \tag{12}
$$
The query path length and congestion contain no polynomial $k$ factor.

## 3. What this establishes, and what it does not

The leaf topology gathering and zero-round embedding sentence in CHS can be
replaced by a uniform deterministic polynomial-work procedure with explicit
short route lists. This does not by itself establish the sequential work of
the complete CHS router.

The separate Appendix B.1 cut-player search needs replacement. In particular,
its condition concerns squared-distance energy for every map from one
cluster set to the other, not merely the existence of a balanced sparse cut.
The printed random-projection calculation must not be treated as a sequential
algorithm.

The inherited Chang--Saranurak hierarchy has a more favorable explicit
source boundary: [arXiv:2007.14898](https://arxiv.org/abs/2007.14898), Section 4.3,
contains a paragraph titled “A note on local computation time” replacing its
own $2^{O(k)}$ coarse-cut search by a polynomial-$k$ approximate balanced-cut
algorithm. Its conclusion also discusses deterministic PRAM work, rather than
round complexity alone. A complete parameterized work proof should use that
replacement and account for the matching/path primitives and virtual-graph
simulation explicitly. It should not silently apply the same replacement to
CHS's different Appendix B.1 energy condition.
