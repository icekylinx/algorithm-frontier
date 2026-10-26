# Two integrality gaps for recipient-polymatroid configuration relaxations

The first construction has a gap approaching the selected-player rank
for the aggregate configuration LP. The second has an exact gap of two
even after every residual-capacity cut is added. Both use explicit
cardinality rank functions; neither is a computational hardness claim.

## 1. The two relaxations

Let $`M`$ be the player-selection matroid. At target $`T`$, player $`p`$
puts nonnegative mass $`\mu_{pn}`$ on its locally legal integral
configurations $`n`$ of value at least $`T`$. Write
```math
x_p=\sum_n\mu_{pn},\qquad y_{pj}=\sum_n\mu_{pn}n_j.
```
The aggregate relaxation requires
```math
x\in B(M),\qquad y_{\cdot j}\in P(f_j)\quad\text{for every type }j.
 \tag{G1}
```
It retains only the summed recipient rank $`f_j`$; it does not retain a
separate column for each component of a decomposition of that rank.

For a single resource $`f`$, a feasible integral reserve $`z\in P(f)`$
has residual singleton capacity
```math
a_p(z)=\min_{A\ni p}\{f(A)-z(A)\}.
```
The full residual relaxation adds every inequality
```math
\sum_{p,n}\mu_{pn}(n_j-a_p(z))_+\le z(P).
 \tag{G2}
```
The following equivalent subset form makes the second construction
checkable without enumerating numerical reserve counts:
```math
\sum_{p,n}\mu_{pn}(n_j-m_p(S))_+\le f(S),\qquad
 m_p(S)=f(S\cup\{p\})-f(S).
 \tag{G3}
```

**Lemma 1.** The full families (G2) and (G3) are equivalent.

**Proof.** Define the violation of (G2) for every real $`z\in P(f)`$
by subtracting $`z(P)`$ from its left side. Each hinge equals
```math
(n_j-a_p(z))_+
 =\max\{0,\max_{A\ni p}(n_j-f(A)+z(A))\},
```
so the violation is a convex function of $`z`$. Its maximum is attained
at a polymatroid vertex. Every such vertex is a greedy vector on an
ordered subset $`S`$, has total $`f(S)`$, and spans the full conceptual
owner blocks of $`S`$ in the natural matroid. Therefore its residual
capacity at $`p`$ is exactly $`m_p(S)`$. Its reserve inequality is
(G3). Convexity now shows that all subset cuts imply all reserve cuts.
Conversely, a greedy base on any $`S`$ is an integral feasible reserve
whose inequality is that subset cut. $`\square`$

These are valid inequalities for integral allocations. Indeed, for a
feasible resource count vector $`n`$, let $`A=\{p:n_p>m_p(S)\}`$.
Submodularity and feasibility give
```math
n(A)\le f(A)\le f(S\cup A)
       \le f(S)+\sum_{p\in A}m_p(S),
```
which proves the corresponding hinge inequality.

## 2. A gap approaching the selection rank

**Theorem 2.** For every $`r\ge2`$, the aggregate relaxation has
instances with gap arbitrarily close to $`r`$.

**Proof.** Choose integers $`D\ge r`$ and $`q=Dr`$. Use the uniform
player matroid $`U_{r,q}`$, one unit-valued resource, and
```math
f(\varnothing)=0,\qquad f(S)=|S|+D\quad(S\ne\varnothing).
 \tag{G4}
```
This is the sum of the free-matroid rank and $`D`$ rank-one
uniform-matroid ranks, so it is normalized, monotone, integral, and
submodular.

At each player put mass $`1/D`$ on its legal configuration of $`D+1`$
units. Then $`x_p=1/D`$, $`\sum_px_p=r`$, and $`y_p=(D+1)/D`$.
For every nonempty $`S`$ of size $`s`$,
```math
y(S)=s+s/D\le s+D=f(S),
```
because $`s\le Dr\le D^2`$. Thus the target $`D+1`$ is feasible.

For any selected $`r`$-set $`I`$, integer feasibility requires
$`n(I)\le r+D`$. Consequently
```math
\mathrm{OPT}_{\rm int}\le1+\lfloor D/r\rfloor.
```
Equality is attained by giving that many units to each selected
player: for every $`A\subseteq I`$,
```math
n(A)=|A|+|A|\lfloor D/r\rfloor\le |A|+D.
```
Adding unselected players to the tested set cannot decrease its rank.
Therefore the gap is at least
```math
\frac{D+1}{1+\lfloor D/r\rfloor},
 \tag{G5}
```
which tends to $`r`$ along $`D=rL`$, $`L\to\infty`$.
No target exceeds $`D+1`$, the singleton capacity. $`\square`$

Keeping the free component and the $`D`$ rank-one components separate
excludes the displayed point: a $`D+1`$-unit configuration must use all
$`D`$ rank-one services, forcing expected total $`Dr>D`$ from components
whose combined capacity is $`D`$. The integer feasible count vectors
are unchanged by merging, but their configuration relaxation changes.

## 3. Exact gap two after all residual cuts

**Theorem 3.** For every $`r\ge3`$, there is an explicit single-resource
instance whose integer optimum is one and whose full residual
configuration optimum is two.

**Proof.** Set $`q=2r`$, $`M=U_{r,2r}`$, and
```math
f(S)=\min\{|S|,r-1\}+\min\{|S|,r+1\}.
 \tag{G6}
```
It is the sum of two uniform-matroid ranks. Every selected $`r`$-set
can receive one unit per player. Two units per selected player violate
its own rank inequality, since $`f(I)=2r-1<2r`$. Hence the integer
optimum is exactly one.

Put mass $`1/2`$ on configuration $`n=2`$ at every player. Then
$`x_p=1/2`$, $`y_p=1`$, and $`x\in B(U_{r,2r})`$.
The inequality $`f(S)\ge|S|`$ verifies every aggregate recipient row.
For a subset $`S`$ of size $`s`$, its inside players have marginal zero
and every outside player has the same next marginal $`m(s)`$. The
left side of (G3) is
```math
L(s)=s+\frac{2r-s}{2}(2-m(s))_+.
```
The following four cases exhaust all subsets:

| Subset size | Outside marginal | Left side $`L(s)`$ | Slack $`f(S)-L(s)`$ |
|---|---:|---:|---:|
| $`0\le s\le r-2`$ | $`2`$ | $`s`$ | $`s`$ |
| $`s=r-1`$ | $`1`$ | $`(3r-1)/2`$ | $`(r-3)/2`$ |
| $`s=r`$ | $`1`$ | $`3r/2`$ | $`(r-2)/2`$ |
| $`r+1\le s\le2r`$ | $`0`$, or no outside player | $`2r`$ | $`0`$ |

All slacks are nonnegative for $`r\ge3`$. Lemma 1 therefore verifies
every feasible-reserve cut, with arbitrary support. The singleton
capacity is two, so no configuration target above two exists. Thus
```math
\mathrm{OPT}_{\rm full\ residual\ LP}=2,\qquad
 \mathrm{OPT}_{\rm int}=1.
 \qquad\square
```

The two component resources have recipient matroids
$`U_{r-1,2r}`$ and $`U_{r+1,2r}`$. Integral polymatroid decomposition
shows that their summed integer counts are exactly the integer points
of $`P(f)`$. In their separate-component configuration relaxation,
every target strictly above one requires one service from each
component. Total player mass $`r`$ would demand $`r`$ services from
the first component, exceeding its rank $`r-1`$. Target one is feasible
integrally using the larger component, so that relaxation has optimum
exactly one.

## 4. Consequences

Theorem 2 excludes a rank-independent constant guarantee against the
unstrengthened aggregate LP. Theorem 3 excludes a factor strictly below
two against the full residual LP, even with unlimited computation.
These statements do not lower-bound approximation against integer
optimum, and they do not establish that factor two is achievable.
The [recipient-polymatroid algorithm](../recipient-polymatroid/proof.md)
uses the integral-comparator loss lemma and remains consistent with both
constructions.

**Attribution:** Yilin Liu and GPT-6 Astra Pro.
