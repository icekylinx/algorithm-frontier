# Entropy progress for balanced cuts and half-matchings

**Mathematical replacement lemma, 24 October 2026.** This note proves
the exact cut-matching progress statement needed by the sequential
virtual hierarchy. A continuing cut player is required to return a
balanced cut of sparsity at most $`1/8`$. The matching player need
only match half of its source side. Both constants are absolute.
No induced-subgraph property of a successful terminal object is used.

This small threshold change repairs a literal error in the half-matching
calculation in Chang--Saranurak,
[arXiv:2007.14898v1](https://arxiv.org/pdf/2007.14898), Appendix F.2.
Their displayed total-mass estimate uses the full source cardinality
where the half-matching assumption gives only half. The replacement
below supplies a complete proof at the threshold actually used by the
new construction.

## 1. Exact combinatorial interface

Fix $`N`$ abstract vertices. Let $`M_1,\ldots,M_{i-1}`$ be previously
added matchings; parallel occurrences in different rounds have
distinct edge IDs. Let $`H_{i-1}`$ be their multigraph union. A
continuing cut player returns $`S\subseteq V`$, $`T=V\setminus S`$,
with
```math
N/4\leq s:=|S|\leq N/2,\qquad
                    |\partial_{H_{i-1}}S|\leq \eta s,
                    \quad 0\leq\eta\leq1/8.
 \tag{1}
```
Do not deduplicate equal endpoint pairs during the game: its cut
boundary counts every past matching occurrence.
The next matching $`M_i`$ joins $`S`$ to $`T`$ and has size at
least $`s/2`$. Write $`S_*\subseteq S`$, $`T_*\subseteq T`$ for
its endpoints. Its edges give a bijection $`k\mapsto\ell(k)`$
from $`S_*`$ to $`T_*`$.

Let $`F_{i-1}`$ be the transition matrix obtained by successively
averaging the two coordinates of every edge of
$`M_1,\ldots,M_{i-1}`$. Equivalently, at each matching a walk
stays or crosses its matching edge with probability $`1/2`$.
Write $`p(j,k)`$ for the probability of being at $`k`$ when
starting at $`j`$. The matrix is doubly stochastic.

Define the entropy, using natural logarithms and $`0\log(1/0)=0`$,
by
```math
{\cal E}_{i-1}
                  =\sum_{j,k}p(j,k)\log(1/p(j,k)).
 \tag{2}
```
It is always in $`[0,N\log N]`$.

**Lemma.** Every continuing round satisfying (1) increases (2)
by at least $`5N/1024`$. Consequently there are at most
$`(1024/5)\log N`$ such rounds.

## 2. The cross-cut mass bound

Initially place one unit of load at every vertex of $`S`$, and
zero outside $`S`$. Apply the previous matching averages.
All loads stay in $`[0,1]`$. An occurrence of an edge crossing
$`(S,T)`$ can increase the total load in $`T`$ by at most $`1/2`$.
Counting every previous crossing occurrence therefore gives
```math
\sum_{j\in S,k\in T}p(j,k)
                         \leq\frac12|\partial_{H_{i-1}}S|
                         \leq\frac{\eta s}{2}.
 \tag{3}
```
Starting instead with unit loads on $`T`$ proves
```math
\sum_{j\in T,k\in S}p(j,k)
                         \leq\frac{\eta s}{2}.
 \tag{4}
```
These statements hold for any earlier matching sequence, even
if edges or endpoint pairs have been repeated.

## 3. Enough matched mass has a nontrivial imbalance

For $`j\in S`$ and $`k\in S_*`$, call the triple
$`(j,k,\ell(k))`$ good when
```math
p(j,k)\geq2p(j,\ell(k)).
 \tag{5}
```
The total $`p(j,k)`$ mass over all these triples is
```math
\begin{split}
 \sum_{j\in S,k\in S_*}p(j,k)
   &=|S_*|-\sum_{j\in T,k\in S_*}p(j,k)\\
   &\geq\left(\frac12-\frac{\eta}{2}\right)s.
 \end{split}
 \tag{6}
```
The term $`|S_*|\geq s/2`$, rather than $`s`$, is essential.
Over bad triples the total is bounded by
```math
\begin{split}
 \sum_{\rm bad}p(j,k)
    &\leq2\sum_{j\in S,\ell\in T_*}p(j,\ell)\\
    &\leq\eta s.
 \end{split}
 \tag{7}
```
Subtracting yields
```math
\sum_{\rm good}p(j,k)
             \geq\left(\frac12-\frac{3\eta}{2}\right)s
             \geq\frac{5s}{16}
             \geq\frac{5N}{64}.
 \tag{8}
```
Thus the claimed positive mass follows from an absolute threshold
strictly below $`1/3`$. The chosen $`1/8`$ leaves substantial slack.

## 4. Entropy gained by one good pair

Let $`a,b\geq0`$, and average the two masses to $`(a+b)/2`$.
With $`h(z)=z\log(1/z)`$, concavity always gives
```math
2h((a+b)/2)-h(a)-h(b)\geq0.
 \tag{9}
```
If $`b\leq a/2`$, the gain is at least
```math
\frac{a}{16}.
 \tag{10}
```
For $`a>0`$, put $`u=b/a`$. The gain divided by $`a`$ is
```math
f(u)=(1+u)\log2-(1+u)\log(1+u)+u\log u.
 \tag{11}
```
Its derivative is $`\log(2u/(1+u))\leq0`$ on $`0<u\leq1/2`$.
Hence its minimum there is
```math
f(1/2)=\tfrac12\log(32/27)
       \geq\tfrac12\frac{5}{32}
       =\frac5{64}>\frac1{16},
 \tag{12}
```
using $`\log(1+x)\geq x/(1+x)`$. The case $`a=0`$ is immediate.

For each starting vertex $`j`$, the new matching averages the
disjoint coordinate pairs $`(k,\ell(k))`$. Apply (10) to
every good triple, and (9) to all remaining pairs and starts.
Equation (8) gives
```math
{\cal E}_i-{\cal E}_{i-1}
                      \geq\frac1{16}\frac{5N}{64}
                      =\frac{5N}{1024}.
 \tag{13}
```
Since $`{\cal E}_0=0`$ and $`{\cal E}_i\leq N\log N`$,
the lemma follows.

## 5. A literal obstruction to the old threshold

The same per-round assertion is false with threshold $`1/2`$
and only half-matching. Let $`N`$ be divisible by four, choose
$`|S|=|T|=N/2`$, and let $`M`$ be a matching of size $`N/4`$
from $`S`$ to $`T`$. After one round $`H_1=M`$, so
```math
|\partial_{H_1}S|=|S|/2.
 \tag{14}
```
The same cut is allowed by the threshold $`1/2`$, and a second
round may choose the same matched pairs, with new edge occurrence
IDs. Averaging on those pairs is idempotent, so $`F_2=F_1`$
and the entropy increase is zero.

This example concerns the asserted PER-ROUND proof. It does not
claim that every weaker global conclusion in the source is false.
The new construction uses (1)--(13) directly and therefore does
not require such a conclusion.

## 6. Use by the sequential virtual hierarchy

At every nonroot recursive cut-player call, set the requested
balanced-cut sparsity threshold to at most $`1/8`$, rather than
$`1/2`$. The strong balance wrapper still returns either a cut
with smaller side in $`[N/4,N/2]`$, or a successful virtual
expander on at least $`2N/3`$ vertices. Changing one absolute
threshold preserves every stated polynomial-work and expansion
recurrence.

A successful virtual output stops that abstract game. It is not
inserted into the previous matching graph. The proof above uses
only continuing cuts and matchings, so it imposes no inducedness
requirement on the success object. Abstract matching endpoints
must be distinct within a round; physical embedding paths may
overlap according to their separately charged congestion.

An executable round cap of
```math
512\lceil\log_2(N+2)\rceil
 \tag{15}
```
is more than sufficient. The implementation need not compute
entropy; (2) is only an analytical potential.

The outer full-host matching adapter uses cutoffs
$`\psi/(16j^2)`$ to control failure-cut unions in its CURRENT
embedding host. That parameter is distinct from the $`1/8`$
threshold of a recursive cut player on an abstract matching
graph. Both interfaces now have their own explicit proofs.

The earlier 5/6 threshold-router composition uses the
Chuzhoy--Saranurak decremental path oracle and its CGLN
decomposition dependencies. It does not use this new
Chang--Saranurak sequential hierarchy or the half-matching
entropy assertion repaired here. The threshold change is
therefore part of the additional 4/5 route.
