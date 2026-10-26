# Deterministic selection of one weighted path from each token family

**Auxiliary mathematical construction, 24 October 2026.** This note
gives a sparse conditional-expectation algorithm. Its input is an
EXPLICIT family of candidate paths; it does not construct those
paths. In particular, it does not assert that a distributed routing
algorithm has an efficient sequential implementation.

The result explains how an appropriate token-routing primitive could
remove the input-path-length factor from an ambient-congestion
sparsification bound. The currently established 6/7 research
construction is unchanged.

## 1. Discrete selection problem

There is a finite set of resources $X$ and a collection of groups
$\mathcal G$. Group $g$ has exactly $Q_g\geq1$ options.
Option $j\in[Q_g]$ specifies nonnegative integer multiplicities
$a_{g,j,x}$ on resources $x$. Multiplicities may be supplied as
repeated entries and aggregated deterministically by sorting.

Let $S$ be the explicit input-list size, including group and option
headers and every resource occurrence. Thus the number of groups,
options, nonzero group-resource pairs, and used resources are all at
most $S$. Define
$$
\mu_x=\sum_{g}\sum_{j=1}^{Q_g} a_{g,j,x},\qquad
 B=\max_{g,j,x}Q_ga_{g,j,x}.
 \tag{1}
$$
If all multiplicities are zero, choose any option in each group.
Otherwise $B\geq1$, and the algorithm below chooses one $j(g)$
per group so that
$$
\boxed{
 \sum_g Q_g a_{g,j(g),x}
 \leq 2\mu_x+B\log(8|X|+8)
 \quad\hbox{for every used resource }x.
 }
 \tag{2}
$$
A harmless increase of the numerical constant accommodates the
finite-precision implementation described below. In particular,
one may use the convenient bound
$4\mu_x+4B\log(2|X|+2)$.

The total number of scalar operations is
$S\operatorname{polylog}(S+2)$. Resource-ID comparisons additionally
use the given ID word size. All mantissas and binary exponents have
$O(\log(S+2))$ bits; there is no least-common-denominator computation.

If the application assigns a real or rational weight
$0<w_g\leq Q_g$ to group $g$, the same selected options satisfy
(2) with $Q_g$ in the load replaced by $w_g$.

## 2. Exponential potential

Independently choose a uniformly random option in each unprocessed
group only for the analysis. For a group and resource define
$$
E_{g,x}
   =\frac1{Q_g}\sum_{j=1}^{Q_g}
       \exp(Q_ga_{g,j,x}/B).
 \tag{3}
$$
Every exponent in (3) is between zero and one. Since
$e^u\leq1+(e-1)u$ for $0\leq u\leq1$,
$$
E_{g,x}\leq
 1+\frac{e-1}{B}\sum_j a_{g,j,x}.
 \tag{4}
$$

For current selected load $b_x$, maintain the conditional potential
$$
W_x=\exp((b_x-2\mu_x)/B)
                 \prod_{\text{unprocessed }g} E_{g,x}.
 \tag{5}
$$
Initially (4) and $e-1<2$ give $W_x\leq1$, so
$$
\sum_xW_x\leq |X|.
 \tag{6}
$$
After choosing option $j$ of group $g$, the potential changes by
$$
W'_x=W_x\exp(Q_ga_{g,j,x}/B)/E_{g,x}.
 \tag{7}
$$
Its expectation over a uniform option is exactly $W_x$.
Thus some option does not increase the total potential.

## 3. Finding that option with sparse positive sums

One must not scan every resource for every candidate option.
Let $X_g$ be the union of resources appearing in group $g$'s
options. For fixed $g$, the potential resulting from candidate
option $j$ is
$$
\sum_x\frac{W_x}{E_{g,x}}
 +\sum_{x:a_{g,j,x}>0}
       \frac{W_x}{E_{g,x}}
                \bigl(\exp(Q_ga_{g,j,x}/B)-1\bigr).
 \tag{8}
$$
The first sum is common to all candidates. It is never necessary
to compute it. Choose a minimum candidate using only the second
sum, whose terms are nonnegative. Evaluating every candidate uses
the explicit resource occurrences of group $g$, once.

After selection, update (7) only on $X_g$; all other factors are
one. The factors themselves can be constructed sparsely as
$$
E_{g,x}
  =1+\frac1{Q_g}
       \sum_{j:a_{g,j,x}>0}
          \bigl(\exp(Q_ga_{g,j,x}/B)-1\bigr).
 \tag{9}
$$
The sum of $|X_g|$ over all groups is at most $S$.
Computing all factors, initializing their products in (5), evaluating
all candidates, and applying all updates therefore takes
$S\operatorname{polylog}(S+2)$ operations.

With exact arithmetic the total potential never increases, so the
final value $\exp((b_x-2\mu_x)/B)\leq|X|$ proves the slightly
stronger exact-arithmetic form of (2).

## 4. Finite-word implementation

The exponential expressions are not stored as exact transcendental
numbers. Use binary floating-point values with an explicitly signed
integer exponent, and a sufficiently large fixed multiple of
$\log(S+2)$ mantissa bits.

All quantities in (3) and (9) lie in $[1,e]$. Their nonzero
increments have magnitude at least a polynomial reciprocal in $S$:
$Q_ga_{g,j,x}/B\geq1/B$ and $B\leq S^2$.
Taylor expansion on $[0,1]$, followed by positive sums and ordinary
division, computes them and their positive increments to any
relative accuracy $(S+2)^{-c}$ in
$\operatorname{polylog}(S+2)$ scalar work.

For initialization, the exponent $-2\mu_x/B$ has absolute value at
most $2S$. Compute its exponential by scaling into $[-1,0]$,
using the reciprocal of a positive Taylor series there, and then
repeated squaring with enough extra guard bits. Only $O(\log S)$
squarings are needed. Every exact intermediate $W_x$ is between
$\exp(-O(S))$ and $\exp(O(S))$, because there are at most $S$
groups and each update factor in (7) lies in $[e^{-1},e]$.
Its binary exponent therefore needs only $O(\log(S+2))$ bits,
even when its numerical value is exponentially small.

Choose the elementary relative error below
$(S+2)^{-c}$ for a sufficiently large fixed $c$, and round only
positive values. Products, divisions, and the positive sums in (8)
then have total relative error less than $1/(100(S+1))$ per
group decision, including accumulated representation error. Choosing
the minimum APPROXIMATE positive score gives a true score at most
$1+1/(20(S+1))$ times the true minimum.

The common term in (8) is nonnegative. Thus this approximate choice
increases the true total potential by at most the same multiplicative
factor. Across at most $S$ choices, the total increase is less than
two; allowing another fixed factor for initialized and final
representations gives a final potential at most $8(|X|+1)$.
This proves (2) with the displayed slack.

No cancellation of nearly equal positive numbers is used in selecting
an option. In particular, the algorithm computes
$\exp(u)-1$ directly by its positive series and does not obtain it
by subtracting rounded numbers close to one. It never materializes
products of unrelated rational denominators.

## 5. Application to weighted witness paths

Let $J$ be an unweighted demand graph embedded into an ambient graph
$H'$. First replace every $\Pi(e)$ by a SIMPLE ambient path with
the same endpoints, by loop erasure. This costs the already explicit
path-list work and does not increase length or congestion.
Write $C=C(\Pi)$ for its ambient vertex congestion.
Loop erasure compares the actual IMMEDIATE vertex lifetime IDs of
$H'$. It never identifies vertices merely because they have the
same eventual physical image under a later projection. In particular,
an open path through two different aliases of one physical root
cannot be erased as a closed walk. A zero physical image does not
make an edge or path a true null object in the immediate graph.
The normalized route table is part of the output type; the
congestion conclusion below applies to that table.

Let $W$ be a sparse weighted witness on $V(J)$, with positive
edge weights $w_g$. For each witness edge $g$, suppose a separate
procedure supplies $Q_g=\lceil w_g\rceil$ unit-token paths in $J$.
Suppose each token path is simple and has at most $D_{\rm route}$
edges, and the entire unit-token family uses each edge of $J$ at
most $T_{\rm route}$ times.

For each token path, take its composed ambient vertex-occurrence
list through $\Pi$. These lists define the options in Section 1.
They may be walks; multiplicities are retained. Because each
individual $\Pi(e)$ is simple,
$$
a_{g,j,x}\leq 2(D_{\rm route}+1)
 \tag{10}
$$
under a convention that safely counts shared endpoints twice.
Furthermore,
$$
\mu_x\leq 2T_{\rm route}C.
 \tag{11}
$$
The factors of two only reconcile endpoint conventions.

Apply (2) with
$$
B\leq 2(D_{\rm route}+1)
                 \max_g\lceil w_g\rceil.
 \tag{12}
$$
Choose one token path for each witness edge and assign that selected
path its original weight $w_g$. Its composed ambient congestion is
at most
$$
O\!\left(
  T_{\rm route}C+
  D_{\rm route}(\max_g w_g+1)\log(|V(H')|+2)
 \right).
 \tag{13}
$$
The bound has NO factor $L(\Pi)$. Its work does depend on the
explicit composed path-list size, which is necessary and permitted.

In the usual degree-band witness construction,
$w_g\leq\Delta(J)/\phi$. If
$D_{\rm route},T_{\rm route},\phi^{-1}$ are bounded by a common
factor $\Gamma_0$, then (13) is
$$
\Gamma_0^{O(1)}\operatorname{polylog}M
                         \bigl(C+\Delta(J)\bigr).
 \tag{14}
$$
Selecting one path per witness edge preserves sparsity:
the retained subgraph of $J$ has at most
$|E(W)|D_{\rm route}$ edges. If a subsequent embedding from $J$
to $W$ has weighted edge congestion at most $\Gamma_1$, the
standard composition bound multiplies (14) by $\Gamma_1$.

### Why simple preliminary paths are essential

Without loop erasure of the individual input images, one edge of
$J$ might already visit an ambient vertex $L(\Pi)$ times.
Then (10) would contain that factor, and the intended improvement
would disappear. This normalization is legitimate for a distance
spanner and for the touched-set construction: erasing a closed walk
from a projected edge's preliminary route leaves a path in the old
lower layers together with, at most, its own central original edge.
If erasure removes the central edge, selecting that central ID is
merely unnecessary; it is still a valid bounded-size selection.

Individual edge gradients are not asserted to be preserved by this
distance normalization. The cycle construction must keep its
explicit correction circulation $e-\Pi(e)$, as in the existing
distance backend. A gradient-preserving application that lacks those
corrections cannot use this argument without a separate proof.

## 6. Elementary batching of token demands

Here is a separate useful reduction for supplying the paths.
For a routing host $G$, distribute each vertex's token starts and
token destinations cyclically over its $\deg_G(v)$ incidence ports.
Let the maximum resulting port load be $D$. Make the bipartite
multigraph whose left and right vertices are source and destination
ports and whose edges are the token IDs. Its maximum degree is
at most $D$.

This graph can be split into at most
$2^{\lceil\log_2D\rceil}\leq2D$ matchings in
$O(M_{\rm tok}\log(D+2))$ work. At each step, decompose every
component into trails with odd-degree vertices as endpoints and
alternate the two colors along each trail. Closed tours have even
length because the graph is bipartite. Each color has maximum
degree at most the ceiling of half the old maximum. Recurse until
the maximum degree is one. Temporary trail-completion edges are
discarded and are not token demands.

Each resulting batch has at most one source token and one destination
token per port. Therefore a routing primitive on the host's
constant-degree expander-split graph can be used with its ordinary
one-token-per-node guarantee. Preprocess the routing host once, then
answer every batch. A token's path length is bounded by one QUERY's
dilation; it is not multiplied by the number of batches.

The total sequential work of this reduction still requires a bound
on the actual routing primitive's sequential work. A bound on
distributed rounds alone is insufficient.

## 7. Current boundary

The sparse path-selection algorithm and the elementary batching
argument above are independent of a fast expander router. They
establish what can be done with explicit candidate token paths.

Chang--Huang--Su,
[arXiv:2405.03908v1](https://arxiv.org/abs/2405.03908v1),
give a deterministic distributed preprocessing/query tradeoff that
would be promising for the application. Its literal construction
has local-computation steps for which a suitable sequential work
bound is not supplied: the cut-player search in Appendix B.1 and
the leaf sorting-network embedding in Section 6.4 require further
constructive replacements. This note neither assumes that those
steps are cheap nor derives a new matching exponent from them.
