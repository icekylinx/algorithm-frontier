# Finite arithmetic for the Steiner-packing client, and the Li skeleton dependency

## Status and scope

This is an independent audit of two dependencies of the proposed
[gomory-hu-seven-eighths-dependency-audit.md](gomory-hu-seven-eighths-dependency-audit.md) application. It assumes an
explicit rooted multi-source forest satisfying the strong interface in
[separated-metric-forest-and-strong-sssp.md](separated-metric-forest-and-strong-sssp.md), with the rooted extraction
proved in [multisource-rooted-approximate-ball-forest.md](multisource-rooted-approximate-ball-forest.md).

The conclusions below concern finite arithmetic, update accounting, and
the skeleton construction. They do not replace the rooted-forest proof,
the bounded-degree adapter, or the complete Gomory--Hu reduction.

Write

```math
U=\log N,\qquad h=\log\log N,\qquad
 E=\exp O(U^{7/8}h^{1/8}).
```

Here $`N`$ is a polynomial master bound on the original input size,
including the number of records in any one packing instance. A fixed
power of $`E`$ is absorbed into $`E`$. The capacities in this section
are positive integers $`c_e\in[1,W]`$, where $`W\leq N^{C}`$ for a
fixed constant. The accuracy parameter $`\eta`$ is a sufficiently small
**fixed rational constant**. This is sufficient for the Gomory--Hu
client, which only needs a fixed constant approximation to Steiner
connectivity. No variable-accuracy claim is made here.

The relevant public interfaces are Abboud et al.,
[arXiv:2507.20354v1](https://arxiv.org/html/2507.20354v1),
Algorithms 2--3, Claims 4.10 and 4.13, and Theorems 4.11, 4.22--4.23.
The finite-grid implementation below is a new derivation of the same
packing guarantee; it does not assume exact real exponentiation.

## 1. Common-grid packing values and exact loads

Let $`\kappa\leq E`$ be a fixed upper bound on the number of current
auxiliary-graph occurrences of any physical edge. Choose a power of two
$`\alpha`$ with

```math
8\kappa\leq\alpha<16\kappa.
```

In outer iteration $`j`$, the maintained terminal subtree projects to
a connected Steiner multigraph $`H_j`$. Write $`k_{j,e}\leq\kappa`$
for the multiplicity of physical edge $`e`$, and use packing increment

```math
\Delta_j={\min_{e:k_{j,e}>0}c_e\over\alpha}.
             \tag{1}
```

Every increment, pending value, and cumulative flushed load is therefore
an integer multiple of $`1/\alpha`$. The conceptual full load is

```math
L_e=\sum_j k_{j,e}\Delta_j=a_e+b_e,
 \tag{2}
```

where $`a_e`$ is the load already flushed to its price and $`b_e`$ is
the sum still held on current occurrences. Before an occurrence is
retired its pending value is transferred to $`a_e`$; the transfer must
occur before its mapping record disappears. A new occurrence starts
with pending value zero. These rules preserve (2) exactly.

Give every occurrence of $`e`$ threshold $`c_e/\alpha`$. After all
threshold events have been settled,

```math
0\leq b_e<{\kappa c_e\over\alpha}\leq c_e/8.
 \tag{3}
```

A whole outer iteration adds at most
$`\kappa\Delta_j\leq c_e/8`$ to any edge. Thus throughout its
subsequent settlement, including retirements,

```math
0\leq b_e\leq c_e/4.
              \tag{4}
```

No packing increment is made in the middle of structural settlement.
This atomicity is needed both for (4) and for the capacity bound below.

## 2. Monotone dyadic prices with no accumulated error

Choose an integer

```math
B\geq {10\log(2m)\over\eta\log 2},
 \qquad \delta=2^{-B}.
 \tag{5}
```

Since $`\eta`$ is fixed, $`B=O(U)`$. Define conceptual prices

```math
q_e={\delta\over c_e}\exp(\eta a_e/c_e),
 \qquad
 Q_e={\delta\over c_e}\exp(\eta L_e/c_e).
 \tag{6}
```

Only $`a_e`$, not $`L_e`$, has to be explicitly available during
the algorithm. The full price $`Q_e`$ is used for analysis.

Let $`\nu=\eta/1000`$, and choose a common dyadic grid $`g`$ with

```math
0<g\leq {\nu\delta\over4W}.
             \tag{7}
```

On each price refresh, compute a certified upper approximation to
$`q_e`$, round upward to the grid, and ensure the resulting value
$`\widehat q_e`$ lies in $`[q_e,q_e+2g]`$. Set

```math
p_e\leftarrow\max\{p_e,\widehat q_e\}.
                  \tag{8}
```

The previous price also lies below $`q_e+2g`$, because the exact
$`q_e`$ is monotone. Consequently, at every settled or intermediate
price refresh,

```math
q_e\leq p_e\leq q_e+2g\leq(1+\nu)q_e.
       \tag{9}
```

There is no multiplicative error per update. Recomputing from the exact
load $`a_e`$, instead of multiplying the last rounded price, is the
essential step. Monotonicization in (8) does not accumulate error.

From (3)--(4),

```math
q_e\leq Q_e\leq e^{\eta/4}q_e,
 \qquad
 {Q_e\over e^{\eta/4}}\leq p_e\leq(1+\nu)Q_e.
 \tag{10}
```

At the beginning of a settled outer iteration, the exponent
$`\eta/4`$ in the upper bound on $`Q_e/q_e`$ improves to
$`\eta/8`$.

All tests use the exact dyadic sum

```math
D_p=\sum_e c_ep_e.
                         \tag{11}
```

The outer loop continues while $`D_p<1`$. There is no floating-point
comparison with an uncertain stopping threshold.

## 3. Stopping, last-iteration overshoot, and feasible scaling

Let $`D_Q=\sum_e c_eQ_e`$. At the start of the last outer iteration,
(3) and (9) imply $`D_Q\leq e^{\eta/8}D_p<e^{\eta/8}`$. The
iteration increases every exponent in (6) by at most $`\eta/8`$.
Hence, at its end,

```math
{1\over1+\nu}\leq D_Q<e^{\eta/4}.
             \tag{12}
```

The lower bound follows from the final condition $`D_p\geq1`$ and
(9). Flushing changes $`a_e`$ and $`b_e`$ but leaves $`L_e`$, and
therefore $`D_Q`$, unchanged. It cannot create an additional overshoot.

For every physical edge,

```math
\delta\exp(\eta L_e/c_e)=c_eQ_e\leq D_Q<e^{\eta/4},
```

so

```math
{L_e\over c_e}<{B\log2+\eta/4\over\eta}.
                  \tag{13}
```

Compute once a rational number $`S`$ satisfying

```math
{B\log2+\eta\over\eta}
 \leq S\leq
 {B\log2+2\eta\over\eta}.
 \tag{14}
```

An upward dyadic approximation to $`\log2`$ with error at most
$`\eta/(2B)`$ suffices. Divide every packing value by $`S`$. By
(13), the result is exactly capacity feasible. The scaling number has
$`O(U)`$ bits, and an interval algorithm for $`\log2`$ computes it
in $`\mathrm{poly}(U)`$ bit operations.

## 4. The packing value remains $`\lambda(U)/(4+O(\eta))`$

Let $`P^*`$ denote the optimum fractional packing value of Steiner
trees; the standard packing/cut bound used by the public reduction is
$`P^*\geq\lambda(U)/2`$. For every positive length vector $`z`$,
averaging a feasible optimum packing gives

```math
\min_H z(H)\leq {\sum_e c_ez_e\over P^*}.
          \tag{15}
```

Assume the forest/MSF construction returns a
$`\gamma=2+O(\eta)`$ approximate Steiner multigraph under $`p`$,
counting every occurrence separately. Any constant geometric rounding
loss used by its length-increase adapter is included in $`\gamma`$.
By (10), the same multigraph is a

```math
\rho=\gamma(1+\nu)e^{\eta/8}=2+O(\eta)
                  \tag{16}
```

approximation under the full prices $`Q`$ at a settled iteration
start.

For $`x\in[0,\eta/8]`$, $`e^x-1\leq e^{\eta/8}x`$. Therefore

```math
\begin{split}
 D_{Q,j+1}-D_{Q,j}
 &\leq \eta e^{\eta/8}\Delta_j
             \sum_e k_{j,e}Q_{j,e}\\
 &\leq {\eta e^{\eta/8}\rho\Delta_j\over P^*}\,D_{Q,j}.
\end{split}
\tag{17}
```

Starting from $`D_{Q,0}=m\delta`$, iterating (17), and using (12)
at termination yields

```math
\sum_j\Delta_j\geq
 {P^*\over\eta e^{\eta/8}\rho}
 \bigl(B\log2-\log m-\log(1+\nu)\bigr).
 \tag{18}
```

The choice (5) makes $`\log m/(B\log2)=O(\eta)`$. Dividing
(18) by the rational scaling factor in (14) gives

```math
{\sum_j\Delta_j\over S}
       \geq {P^*\over\rho}(1-O(\eta))
       \geq {\lambda(U)\over4+O(\eta)}.
 \tag{19}
```

Taking a sufficiently small fixed rational $`\eta`$ gives the
$`4.1`$ packing/sparsifier factor used in the guide-tree reduction.
The inequalities have strict constant slack; exact transcendentals are
unnecessary.

## 5. Update counts, including retirement flushes

An outer iteration has a minimum-capacity witness edge $`e`$ whose
full normalized load $`L_e/c_e`$ increases by at least
$`1/\alpha`$. Equation (13) bounds its final normalized load by
$`O(U)`$. Charging each iteration to one deterministic witness gives

```math
T=O(m\alpha U).
                       \tag{20}
```

A threshold-triggered flush has pending load at least
$`c_e/\alpha`$, and hence increases $`a_e/c_e`$ by at least
$`1/\alpha`$. The same argument bounds these flushes by
$`O(m\alpha U)`$. This proof does not require the rounded price
itself to increase by a visible multiplicative amount on every flush.

Retirement flushes may contain arbitrarily small pending loads. They
are charged instead to actual deletions of occurrence records in
$`A`$. This charge is safe under the following architecture:

1. The strong forest receives only monotone **geometric level** changes
   in physical lengths. Each physical edge has $`O(U)`$ such changes.
2. Fine-grid updates of $`p_e`$ refresh its current auxiliary
   occurrences and the MSF keys, but do not by themselves submit a new
   structural forest update.
3. Changes to the MSF and its terminal subtree do not modify the
   underlying auxiliary graph $`A`$. They only change the dynamic-tree
   and Euler-tour state.
4. Before deleting an $`A`$ occurrence, flush its value while its
   physical mapping is still present. Enqueue a geometric level change
   if and only if a new level has been crossed, and settle the resulting
   queue before the next packing increment.

The number of structural forest updates is thus bounded independently
of the number of retirement flushes. If its explicit recourse is
$`R\leq mE`$, retirement flushes cost $`O(R)`$ refresh events.
Refreshing all current occurrences multiplies this by at most
$`\kappa\leq E`$. Dynamic MSF, Steiner-subtree, and Euler-tour work
have only polylogarithmic additional overhead. This avoids a circular
argument in which a tiny retirement flush is assumed to pay for the
structural changes that caused it.

The auxiliary native-edge keys also depend on endpoint distance
estimates. Consequently, the rooted forest interface must supply an
explicit bounded inventory of **estimate changes**, not merely forest
edge changes. The public approximate-ball labels provide this inventory
when exposed as in the rooted multi-source note. With bounded or
polylogarithmic physical degree, each such change affects only a
polylogarithmic number of native-edge keys. Recomputing every descendant
distance after each forest edit would not satisfy the claimed bound.

## 6. Polynomial structural aspect ratio and bit complexity

Equations (9) and (12)--(13) imply, throughout the execution,

```math
\delta/W\leq p_e<2.
                      \tag{21}
```

Every $`p_e`$ is a multiple of the common dyadic grid $`g`$.
Therefore the integer lengths $`p_e/g`$ lie in

```math
[1,2/g]\subseteq[1,N^{C_1}],
                       \tag{22}
```

for a fixed constant $`C_1`$. This is a bound on the actual
**structural aspect ratio**, not just on the number of bits used to
write an arbitrary rational length. It removes the need for a separate
optimal-Steiner-length epoch scheme in this fixed-accuracy application.

For geometric deletion copies, one may use exact integer levels: keep
all integers up to $`\lceil1/\eta\rceil`$, and subsequently use
$`z_{i+1}=\lceil(1+\eta)z_i\rceil`$. Above the initial range,
successive ratios are at most $`1+2\eta`$, and there are $`O(U)`$
levels. Each level value has $`O(U)`$ bits. Retire copies below the
current integer length; the smallest surviving copy is within a
$`1+O(\eta)`$ factor of that length.

This creates a polylogarithmic degree increase. The strong-forest
adapter must either explicitly allow that increase, paying the degree
factor at its bounded-degree uses, or supply a fixed port expansion.
It must not silently call a strict degree-three interface on the
parallel-copy graph. The degree/port lemma is audited separately from
the numerical argument here.

All exact loads have common denominator $`\alpha`$; their numerators
are at most $`\alpha W\,O(U)`$. The exponent $`\eta a_e/c_e`$
is therefore a rational with $`O(U)`$ bits and magnitude $`O(U)`$.
Certified evaluation of its exponential to absolute error $`g`$
uses $`\mathrm{poly}(U)`$ bit operations, for example by range
reduction and interval Taylor arithmetic. The output accuracy needs
only $`\log(1/g)=O(U)`$ bits. This remains true for every refresh;
there is no growing product denominator.

## 7. The output sparsifier can be made an integer graph

Every Euler-tour accumulation used to extract the vertex sparsifier
is a sum of increments (1). Its raw edge weights are integer multiples
of $`1/(2\alpha)`$. After feasible scaling by $`S`$, a produced
edge has weight

```math
{z_e\over2\alpha S},
                           \qquad z_e\in\mathbb Z_{\geq0}.
                           \tag{23}
```

Discard zero weights. Rather than repeatedly rationalizing these
values, run the skeleton algorithm on the graph whose capacities are
the integers $`z_e`$. This graph is exactly the produced vertex
sparsifier multiplied by the one common factor $`2\alpha S`$.
All cut ratios, near-mincut sets, and guide-tree conclusions are
unchanged.

From (20), every $`z_e`$ is at most a polynomial in
$`T,\alpha,W`$, and hence at most $`N^{C_2}`$ for a fixed
constant. The graph has $`mE`$ records. Thus the skeleton input has
polynomial integer weights relative to the master bound. No least
common multiple of many unrelated denominators is needed.

## 8. Li's corrected skeleton theorem and the near-mincut extension

The current primary source is Jason Li,
[arXiv:2106.05513v2](https://arxiv.org/html/2106.05513v2),
Theorem 1.5, Claim 3.6, Sections 3.4--3.5. Its accuracy dependence is
$`\varepsilon^{-7}`$, replacing the older
$`\varepsilon^{-4}`$ quoted in the Gomory--Hu paper. Write

```math
F_5(N)=\exp O(U^{5/6}h^{O(1)}).
```

For a fixed constant $`c>1`$, the following adaptation is valid.
Multiply the unbalanced-cut parameter by a sufficiently large
constant depending on $`c`$. The canonical-decomposition estimate
then covers every cut of weight at most $`c\lambda`$, and the
sampling error plus the light lossy overlay gives relative error
$`\varepsilon`$ on these cuts. In the large-edge preprocessing,
clip at **$`c\widetilde\lambda`$**, where
$`\widetilde\lambda\in[\lambda,3\lambda]`$. This leaves all
cuts of weight at most $`c\lambda`$ unchanged, preserves the global
mincut, and increases the splitting inventory only by a constant.

The resulting unweighted multigraph $`H`$ has

```math
\begin{split}
 m_H&\leq m'\varepsilon^{-7}F_5(N),\\
 W_H&\geq \varepsilon^7\lambda/F_5(N),\\
 \lambda_H&\leq (1+\varepsilon)\lambda/W_H
          \leq O(\varepsilon^{-7}F_5(N)).
\end{split}
\tag{24}
```

Here $`m'`$ is the vertex-sparsifier input inventory. Every cut has
$`W_H|\partial_HS|\geq(1-\varepsilon)\lambda`$, and cuts of
weight at most $`c\lambda`$ satisfy the required upper bound.
The adjustment of the unbalanced parameter affects only fixed
constants in $`F_5`$. In particular, the corrected
$`\varepsilon^{-7}`$ does not change the leading exponent at the
constant accuracy used by guide trees.

The original clipping threshold $`\widetilde\lambda`$ is
insufficient for this extension: it can change a cut of size between
$`\lambda`$ and $`c\lambda`$. This is why the threshold change
above is an actual proof obligation.

## 9. Both skeleton size and tree-packing size are paid

The guide-tree construction uses $`\widetilde O(m_H\lambda_H)`$
time. Substituting both bounds in (24) yields

```math
\widetilde O(m_H\lambda_H)
           \leq m'\varepsilon^{-14}F_5(N)^2
                    \mathrm{poly}(U).
       \tag{25}
```

Thus one cannot count only the skeleton construction while treating
its unweighted mincut as a constant. Nevertheless, for fixed
$`\varepsilon`$, (25) remains below the proposed strong-forest
envelope: every fixed $`U^{5/6}h^C`$ is
$`o(U^{7/8}h^{1/8})`$. If $`m'\leq mE`$, the whole
skeleton/tree-packing stage is $`mE`$.

## 10. Audit conclusion

The numerical implementation and the corrected Li dependency preserve
the proposed $`7/8`$ envelope. The conclusion requires the explicit
interfaces listed above: atomic occurrence retirement, monotone
geometric structural updates, a bounded distance-label transcript, and
a valid bounded-degree or polylog-degree adapter. Under those
interfaces, neither exact real arithmetic, unbounded denominators,
hidden length aspect ratio, nor the skeleton's tree-packing inventory
introduces a larger exponent.
