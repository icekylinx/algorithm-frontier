# Formal pruning substitution in the public NSW MSF framework

**Focused source audit, 25 October 2026.**

The weak residual-connectivity condition is a sufficient pruning
interface for the **actual weighted NSW construction**, although it
is insufficient for the simplified sketch in the CGLN overview.
This note checks the formal substitution and gives a conservative
deterministic decomposition implementation. Together they support
the derived-public worst-case update envelope

```math
\exp O(U^{2/3}h^{1/3}),\qquad
 U=\log(N+4),\quad h=\log(U+4).
 \tag{1}
```

The result is an analysis of public ingredients. It is not a new
advantage of the research matching router. The separate October
2026 reduction is unnecessary for this MSF bound.

## 1. Sources and the distinction that matters

The primary sources are:

* [NSW, arXiv:1708.03962v2](https://arxiv.org/pdf/1708.03962),
  Theorem 5.1, Theorem 7.1, Theorem 8.3, Definition 9.5,
  Claims 9.18--9.19, Proposition 9.13, and Lemmas 9.20--9.28.
* [CGLNPS, arXiv:1910.08025v2](https://arxiv.org/html/1910.08025v2),
  Corollary 6.1 and Section 6.2.
* [MGS, arXiv:2504.00544v1](https://arxiv.org/html/2504.00544v1),
  Theorem 6.4 and its initialization in Section 6.2.

The CGLN overview's expression consisting of the initial MSF plus
edges incident to the published set is not a standalone valid MSF
certificate under residual connectivity alone. For example, start
with the light tree path $`1-2-3-4`$ and the heavier edge $`1-4`$.
After deleting $`2-3`$, publishing $`P=\{2,3\}`$ leaves the
connected residual graph on $`\{1,4\}`$, but that simplified
certificate omits the necessary edge $`1-4`$.

NSW's actual certificate additionally contains MSFs of three
compressed-cluster graphs at every large cluster, together with
the original versions of reweighted edges and retained retired
edges. It is this certificate that must be used below.

## 2. Exact formal pruning contract

For each initially connected bounded-degree cluster $`C`$, the
formal pruning interface needs a set $`P_C`$ satisfying:

1. $`P_C`$ starts empty and only grows.
2. Every deletion is processed and its new published vertices are
   reported in at most $`\pi`$ time, so at most $`\pi`$ new
   vertices are published in one call.
3. At every supported time, there is some $`W_C\subseteq P_C`$
   for which $`C[V(C)\setminus W_C]`$ is connected.

Theorem 5.1 states precisely this contract, for its own stated
horizon. NSW's Section 9 uses the analogous failure-detecting
Theorem 6.1 only because its decomposition was randomized. A
deterministically certified expanding cluster can instead use a
deterministic implementation of the three conditions above.

Only **non-root large clusters** receive pruning instances. This is
the convention in NSW Section 9.1. The root represents the entire
current input and need not be an expander; no pruning or expansion
promise is imposed on it. Root-level parent-owned and reweighted
edges are handled by the ordinary weighted certificate.

There is no required upper bound on the boundary of $`P_C`$, no
rank condition on published vertices, and no demand that the
algorithm identify $`W_C`$. Publication work and the bounded
native degree pay for incident edges. We may use linear times a
fixed polynomial in the parameters for initialization: the
preprocessing recurrence explicitly pays this work.

## 3. Why these conditions suffice for weighted MSF correctness

Keep NSW's MSF hierarchy and its reweighted graph. The needed
structural invariant is that, after every deletion set, every
child-cluster MSF is a subset of the parent-cluster MSF. This is
Theorem 8.3(3), established using the initial MSF clusters and the
ordered weight bands. It is not a property of an arbitrary
expander decomposition.

At a large parent $`C`$, first replace each small child by its
current MSF. For each large child, the vertices outside its
$`W`$ lie in one current child connected component. Contracting
these subsets is therefore refined by contracting all current
child connected components. Under fixed distinct edge weights,
the edges of an MSF after further contraction were already MSF
edges before that contraction. This gives Claim 9.18's inclusion
for the parent-owned edges after adding back edges incident to
$`W`$.

Now replace $`W`$ by the published superset $`P`$. The newly
removed parent-owned edges are all published explicitly. For
any graph $`X`$ and extra edges $`D`$,

```math
\mathrm{MSF}(X\cup D)
 \subseteq \mathrm{MSF}(X)\cup D.
 \tag{2}
```

Applying (2) to each of the three compressed graphs proves the
transition from $`W`$ to $`P`$, exactly the role of Claim 9.19.
Thus arbitrary additional publication remains sound in the real
certificate. The retired-edge sets only enlarge that certificate;
they prevent publication-induced removals from propagating as
many recursive deletions.

This checks the entire correctness use of pruning in Section 9.2.
The counterexample in Section 1 does not apply because it omits
the compressed-cluster MSFs on which this proof depends.

## 4. A literal connectivity adapter for modern pruning

MGS maintains $`A`$ with positive residual conductance, with
$`\mathrm{polylog}(N)\phi^{-2}`$ worst-case work and
vertex recourse. Conductance alone can ignore isolated vertices,
so use the following conservative publication rule on the
initial degree-three cluster:

```math
P=A\cup N_{C_0}(A)\cup\{\text{endpoints of deleted edges}\}.
 \tag{3}
```

The initial graph is connected and nontrivial, so $`P`$ starts
empty. Each new member of $`A`$ has at most three initial
neighbors. Thus (3) has only a constant factor more publication
and work than MGS, plus constant work per physical deletion.
Its extra published vertices are not deleted from MGS's input.

Let $`I`$ be the isolated vertices of the current residual
$`C[V\setminus A]`$. Every $`v\in I`$ either lost an
incident physical edge or had a neighbor enter $`A`$; hence
$`I\subseteq P`$. All positive-volume vertices of that residual
lie in one connected component, by its positive conductance.
If that component is nonempty, take $`W=A\cup I`$. Otherwise
$`P=V`$, and take $`W=V\setminus\{v\}`$ for any one
vertex. In either case $`W\subseteq P`$ leaves a connected
induced graph. No search for $`I`$ or $`W`$ is needed by the
algorithm.

Singleton initial clusters are handled directly. Initialization
of the MGS flow and graph structures is covered by
$`m_C\mathrm{poly}(1/\phi,U)`$, a deliberately loose
bound sufficient for the preprocessing account.

## 5. Conservative deterministic weighted decomposition

This section spells out a wrapper rather than applying a
bounded-degree decomposition lemma to a contracted graph of
unbounded degree.

Choose an integer scale $`\gamma\ge 4`$. Let
$`\Gamma=\exp O(r^2h)`$ be a common quality loss of CGLN
Corollary 6.1 and require $`\Gamma\le\gamma`$. Its total
static work factor at crossing budget
$`\epsilon=c\gamma^{-2}`$ is polynomial in $`\gamma`$
provided

```math
U/r+r^2h+h\le c_1\log\gamma.
 \tag{4}
```

Every call uses its actual contracted input size. If that input has
$`m'`$ edges, replace the cut-player parameter by
$`r'=\min\{r,\lfloor c_0\log(m'+2)\rfloor\}`$, with a
sufficiently small fixed $`c_0>0`$ and a constant-size direct base
case. Thus the source condition $`r'\le c_0\log(m'+2)`$
holds even deep inside the hierarchy. The quality loss only improves.
For a truncated parameter, $`\log(m'+2)/r'=O(1)`$; otherwise
it is at most $`O(U/r)`$. Also $`(r')^2\log\log(m'+4) \le O(r^2h)`$. Hence each such call still costs its actual input
size times a fixed polynomial in $`\gamma`$. No tiny instance is
padded to the master size, and no exponential-in-$`m'`$ solver is
used except on a fixed constant-size base.

Partition the initial MSF into connected blocks of size between
$`s/3`$ and $`s`$, where $`s=\Theta(\gamma)`$, as in
NSW Lemma 8.9. All block-tree edges remain protected from
reweighting and from removal into weight bands. Use
$`d=\Theta(\gamma)`$ ordered bands and stop a hierarchy
branch once its graph has at most $`n/\Theta(\gamma)`$
edges, with sufficiently generous fixed constants.

At level $`i`$, first remove the current weight band $`E_i`$
from the graph supplied to decomposition. Its protected block
trees remain present. Contract those blocks, discard loops, and
run CGLN Corollary 6.1 with crossing budget $`c\gamma^{-2}`$.
The contracted graph has actual $`O(|V(C)|)`$ edges because
the uncontracted input is degree three; its own degree need not
be bounded. Split off any isolated contracted vertices. Every
remaining output block is connected and has edge expansion at
least its conductance, which is
$`\Omega(\gamma^{-2}/\Gamma)`$, hence
$`\Omega(\gamma^{-3})`$.

Uncontract the protected blocks. NSW Lemma 8.8, with block size
$`s=O(\gamma)`$ and original degree three, gives connected
children of conductance at least

```math
\phi_0=\Omega(\gamma^{-5}).
 \tag{5}
```

A singleton contracted output corresponds to one connected
protected block, and also satisfies (5). The decomposition may
be run separately on disconnected components before contraction;
each contains at least one entire protected block.

The number of lower-band crossing edges in one call is at most
$`O(|V(C)|/\gamma^2)`$. Make the parent own its current band
and those crossing edges. Raise only the latter to a value
between the current and next weight bands. Over $`d`$ levels,
only $`O(n/\gamma)`$ edges are reweighted. The number of
parent-owned edges at any fixed level is also $`O(n/\gamma)`$:
the current band has this size, and lower-band crossings add
$`O(n/\gamma^2)`$.

The protected initial-MSF edges remain safe under arbitrary
deletions: they are never made heavier, while other edges are
only made heavier. After including surviving protected edges,
Kruskal processes child nonprotected edges before parent-owned
edges. This proves the child-MSF inclusion from Section 3 under
every future deletion set. After the last weight band, only
protected block trees remain, so the depth is at most $`d+O(1)`$.
Every leaf contains at least $`s/3`$ vertices. All these are
the properties used in NSW Section 9.

**Ordering clarification.** The displayed NSW Algorithm 8.1
lists decomposition and subsequent removal of $`E_i`$ in that
order, while its conductance proof treats children as direct
decomposition outputs. The explicit order above removes $`E_i`$
before decomposition. It preserves the protected-block input,
the ordered-band correctness argument, the depth, and every
size bound just proved. We do not infer that conductance
survives an arbitrary uncharged post-decomposition deletion.

Each hierarchy level has disjoint actual vertex inventories.
Its work is $`n\mathrm{poly}(\gamma)`$, and there are
$`O(\gamma)`$ levels. Initialization of all pruning instances
adds only $`n\mathrm{poly}(\gamma)`$. The larger fixed
power in (5), compared with the informal $`\gamma^{-3}`$
description, changes no final logarithmic exponent.

## 6. The finite pruning horizon needs no completion trick

Every pruned non-root large cluster has initially
$`m_C\ge n/(C\gamma)`$ edges. The modern supported horizon
is at least $`c\phi_0m_C/Q`$, for a fixed polynomial
$`Q=U^{O(1)}`$. From (5), this is at least
$`c'n/(\gamma^6Q)`$.

Inflate the per-call work/publication allowance to

```math
\pi=\gamma^{12}Q',\qquad
 T(n)=\left\lfloor\frac{n}{C\pi d\gamma}\right\rfloor,
 \tag{6}
```

where $`Q'`$ dominates the fixed logarithmic factors.
Actual pruning work is only $`\gamma^{10}U^{O(1)}`$, so
this allowance is safe. The complete decremental period has
$`T(n)\ll n/(\gamma^6Q)`$ updates; each individual cluster
sees no more than this. No instance reaches the MGS horizon.
There is therefore no final burst or all-vertices completion
operation to justify. Instances below a fixed polynomial in
$`\gamma`$ are solved directly, so floors and zero-length
periods cause no exceptional cost.

## 7. Size and worst-case time depend only polynomially on pi

The source's pruning size argument uses precisely

```math
\sum_C |P_C|\le T\pi d=O(n/\gamma).
 \tag{7}
```

Degree three turns this into the same bound for published
parent-owned incidences. The lower leaf-size bound, the bound
on reweighted edges, and the ordered hierarchy give the other
terms in NSW Lemma 9.20. Thus the maintained sketch has only
$`O(n/\gamma)`$ non-tree edges.

Proposition 9.13 retains edges retired from compressed-cluster
MSFs. As a result, one actual deletion causes at most two
deletions of sketch edges, while causing
$`B=O(\pi d)=O(\pi\gamma)`$ insertions. Lemma 9.27 pays
$`\mathrm{poly}(\gamma)\pi`$ work for these local
changes; it never recursively treats every publication as a
deletion.

The explicit theorem for batch insertions, NSW Theorem 7.1,
charges a recursive decremental instance of size $`O(k)`$,
$`k=O(n/\gamma)`$, through

```math
O\left(
 \frac{B\log k}{k}\,t_{\rm pre}(O(k))
 +B\log^2n+\frac{k\log k}{T(k)}
 +\log k\,t_u(O(k))
 \right).
 \tag{8}
```

This is a worst-case interface. Preprocessing satisfies the
source recurrence with additive
$`n\mathrm{poly}(\gamma)`$; its constant branching
factor after normalization gives at worst
$`\exp O(U/\log\gamma)`$ extra overhead. With (6), all
nonrecursive terms in (8) are
$`\mathrm{poly}(\gamma,U)`$ times that harmless
overhead. The only recursive update multiplier is $`O(\log n)`$.

For a global master bound $`N`$, use the same $`\gamma`$
until actual-size base cases. Solving the update recurrence gives

```math
\log t_u(N)
 =O\left(\log\gamma+\frac{Uh}{\log\gamma}+h\right).
 \tag{9}
```

Theorem 7.1 supplies the same bound for fully dynamic updates,
including the background rebuild cost already present in (8).
Distinct ranks can be obtained by fixed edge-ID tie breaking;
each private decremental rebuild sorts its actual edge weights.
All additional ranks and thresholds have polynomially many bits.

Finally choose $`r=\Theta((U/h)^{1/3})`$ and
$`\log\gamma=\Theta(U/r+r^2h+h)`$ with a sufficiently
large fixed constant. Then (4) holds and
$`\log\gamma=\Theta(U^{2/3}h^{1/3})`$. The second term
in (9) is only $`O(U^{1/3}h^{2/3})`$. This proves the
quantitative envelope (1) for the stated public construction.

The substantive correction to the earlier baseline note is the
formal weighted certificate, not a stronger hypothetical pruning
property. The extra decomposition ordering and fixed-power
losses are made explicit above so that no informal overview is
being used as a theorem.
