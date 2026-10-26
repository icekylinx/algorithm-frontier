# An elementary balanced weighted witness from a hypercube

**Optional local replacement, 24 October 2026.** This note replaces
the fixed-expander-family call used to construct a balanced weighted
witness in the static routing sparsifier. It loses only polynomial
logarithmic factors. It does not change the 4/5 quantitative rate.
The existing constant-degree witness remains a valid alternative.

The only graph fact used is the elementary cube cut induction in
[hypercube-port-adapter.md](hypercube-port-adapter.md), Section 2:
every cut of the $q$-dimensional cube has at least its smaller
vertex-side cardinality many crossing edges.

## 1. Literal weighted interface

Let $V$ have at least two vertices. Suppose the explicitly given
positive rational weights satisfy
$$
w_v\geq1,\qquad
             w_v\leq\sum_{u\ne v}w_u
                         \quad(v\in V).
 \tag{1}
$$
Put $W=\sum_v w_v$. There is a deterministic construction of
a loopless undirected multigraph $F$, on vertex set exactly
$V$, such that
$$
\begin{split}
       w_v\leq\deg_F(v)&\leq4q\,w_v,\\
                    \Phi(F)&\geq1/q,\\
                    |E(F)|&=O(W\log(W+2)),
 \end{split}
 \tag{2}
$$
where $q=\lceil\log_2\sum_v\lceil w_v\rceil\rceil\geq1$.
The work is $O(W\log(W+2))$ elementary record operations,
plus the bit cost of the explicit input and integer arithmetic.
Every parallel output edge retains its own ID. There are no
output self-loops.

The balance condition is automatic for the weights
$$
w_v=\deg_J(v)/\rho
 \tag{3}
$$
of a loopless native graph, whenever $\rho>0$ is no larger
than its minimum positive degree. Indeed every edge incident
to $v$ contributes the same degree mass at another vertex.
The isolated-vertex cases are omitted before making this call.

## 2. Rounding the port count without an oversized fiber

Let
$$
p_v=\lceil w_v\rceil,\qquad N=\sum_v p_v,\qquad
                   M=2^{\lceil\log_2 N\rceil}.
 \tag{4}
$$
Rounding preserves balance:
$$
p_v\leq\left\lceil\sum_{u\ne v}w_u\right\rceil
                      \leq\sum_{u\ne v}\lceil w_u\rceil .
 \tag{5}
$$
Thus $p_v\leq N/2$. We will allocate integer group sizes
$$
p_v\leq p'_v\leq\min\{2p_v,M/2\},
                 \qquad \sum_vp'_v=M .
 \tag{6}
$$
Such sizes always exist. Their lower bounds sum to $N\leq M$.
To check that their upper bounds sum to at least $M$, consider
the number of indices with $p_v>M/4$.

* With none, the upper bounds sum to $2N\geq M$.
* With at least two, their two upper bounds already sum to $M$.
* With exactly one, say $v$, the sum is
  $$
M/2+2(N-p_v)\geq M/2+N\geq M,
$$
  using $p_v\leq N/2$ and $N\geq M/2$.

Start with $p'_v=p_v$ and distribute the remaining $M-N$
ports in a fixed order, up to the displayed integer capacities.
This is a linear scan of the actual vertex inventory. No
unassigned dummy group remains. In particular every final group
has at most half of the cube's ports.

## 3. The witness graph and its proof

Construct the $q=\log_2 M$ dimensional cube on its $M$
bit strings. Partition these vertices into groups of sizes
$p'_v$, in a fixed order. Contract each group to $v$,
discard every cube edge whose two endpoints belong to the
same group, and retain all other cube edges with distinct IDs.
This defines $F$.

For one group, the cube cut inequality and (6) give
$$
\deg_F(v)\geq p'_v\geq p_v\geq w_v.
 \tag{7}
$$
Its degree is at most the total degree of its ports, namely
$$
\deg_F(v)\leq q p'_v
               \leq2q\lceil w_v\rceil\leq4q w_v .
 \tag{8}
$$
The last inequality uses $w_v\geq1$.

For a nontrivial vertex cut $A\subset V$, let
$P_A=\sum_{v\in A}p'_v$. Its boundary in $F$ is
exactly the boundary in the cube of the corresponding port
union, so it is at least $\min\{P_A,M-P_A\}$.
On the other hand
$$
\min\{\operatorname{vol}_F(A),
             \operatorname{vol}_F(V\setminus A)\}
                 \leq q\min\{P_A,M-P_A\}.
 \tag{9}
$$
This proves conductance at least $1/q$.
In particular the witness is connected and has no isolates.

Finally $M<2N\leq4W$, with the harmless equality cases
handled by the same upper bound. Enumerating each cube edge
once by bit flips costs $O(Mq)$. This is
$O(W\log(W+2))$, and bounds the number of retained IDs too.
The graph is generated at its actual port count, never padded
to an unrelated master bound.

## 4. Quantitative use in the linear-parameter static sparsifier

The existing degree-band witness uses balanced weights (3)
with $w_v\geq1$. In
[linear-parameter-static-sparsifier.md](linear-parameter-static-sparsifier.md),
replace its constant upper-degree multiplier $D_w$ by
$$
D_w=4q=O(U).
 \tag{10}
$$
The actual weight inventories there obey
$\log(W+2)=O(U)$. The witness size and its weighted edge
mass gain at most the same $O(U)$ factor:
$$
\sum |E(F)|\leq O(U)\sum O(W),\qquad
 \sum\rho\,|E(F)|\leq O(U)\sum O(|E(J)|).
 \tag{11}
$$
Its inverse conductance is now $q=O(U)$, rather than a
fixed constant.

Forward token loading on the native component acquires the
factor $D_w=O(U)$. Reverse token loading still uses the
lower degree inequality $\deg_F(v)\geq w_v$, so the
same reverse load bound is valid; its total query volume
only gains the witness's $O(U)$ edge-volume factor.
Routing inside $F$ pays a fixed polynomial of $q$.
The normalized weighted path selection and its input
congestion accounting are unchanged except for these
explicit polynomial factors.

More explicitly, write $m_J,n_J$ for the original static
instance and $\phi$ for its common band conductance. The
three sums displayed in the existing constant-$D_w$ proof
become the conservative bounds
$$
\begin{split}
 \sum_i|E(F_i)|&=O(n_J\phi^{-1}U^2),\\
 \sum_i|E(F_i)|&=O(m_J\phi^{-1}U),\\
 \sum_i\rho_i|E(F_i)|&=O(m_JU).
 \end{split}
 \tag{11a}
$$
For forward witness tokens the executable endpoint-load
parameter is $D_{1,i}=\lceil2D_{w,i}/\phi\rceil
=O(U/\phi)$. Its aggregate full-host query volume is
$O(m_JU/\phi)$. The actual forward-token count satisfies
the same bound, by
$\lceil\rho_i\rceil\leq\rho_i+1$ and (11a).
For reverse routing keep
$D_{2,i}=\max\{1,\lceil\rho_i\rceil\}$; then
$$
\sum_i|E(F_i)|D_{2,i}
          \leq\sum_i(\rho_i+1)|E(F_i)|
                      =O(m_JU/\phi).
 \tag{11b}
$$
There is still one preprocessing call per actual witness
component, not one call per load unit.

With a common simple-path quality bound $Q$, the forward
candidate occurrence load on $J$ is now $O(UQ/\phi)$.
After the immediate ambient normalization it gives expected
resource load $O(UQC_0/\phi)$. A single candidate's weighted
resource increment is still at most
$O((\Delta(J)+1)(Q+1))$; the changed witness degree does
not increase the edge weight $\rho_i$. The path-selection
bound therefore acquires the displayed polynomial $U$
factor in its $C_0$ term, while retaining the ADDITIVE
dependence on $C_0+\Delta(J)$. This is the precise place
where (10), rather than an unchanged absolute constant,
enters the congestion proof.

Since $h=\lceil\log_2(U+4)\rceil$, all these factors fit
$$
\Gamma=\exp O((p+r)h)
 \tag{12}
$$
and the existing local construction factor. The powers of
$U$ have fixed exponents independent of $p,r$.
They do not introduce $p^2$, a new repair-depth factor,
or a dependence on the length of an ambient route into
the congestion guarantee.

This is a proof of one optional local replacement. Applying
it to an already delivered checkpoint would require a new
version explicitly using (10), rather than silently treating
the former $D_w$ as an absolute constant.
