# Sharp deterministic restrictions for sparse packing with an oracle matroid

## 1. The construction-time and retained-size tradeoff

Let $`E`$ be an explicitly listed item ground, let $`M`$ be an arbitrary
independence-oracle matroid, and let the packing constraints be

```math
|S\cap A_j|\le b_j,\qquad b_j\in\mathbb Z_{\ge0}.
\tag{SP1}
```

Feasible sets are independent in $`M`$ and have cardinality at most $`k`$.
The matroid is on the selectable items. Items may share the same packing
support, and the packing rows may overlap arbitrarily.

Remove loops and items in zero-capacity rows, and put
$`\kappa=\min\{k,r_M(E)\}`$ on the remaining ground. Rows with
$`b_j\ge\kappa`$ are redundant and may be removed. Write
$`\Lambda(e)=\{j:e\in A_j\}`$ and
$`\delta=\max_e|\Lambda(e)|`$ for this prepared row system.
The cases $`\kappa=0`$ and an empty ground return the empty set. If
$`\delta=0`$, ordinary ordered greedy gives at most $`\kappa`$ items and
preserves the best profit at every cardinality by no-worse-profit
replacements. If exactly equal-profit replacements are required, retain
one basis per profit class instead; its size is at most $`\sum_a r_a`$.

For the remaining cases, let $`h`$ be any valid bound on the number of
packing rows saturated by a feasible context of at most $`\kappa-1`$
items. The simple choice is

```math
h=\delta(\kappa-1).
\tag{SP2}
```

Section 3 gives a computable, sometimes much smaller, capacity-sensitive
choice. Define

```math
C=\binom{h+\delta}{\delta},\qquad
\Theta_{\kappa,h,\delta}
  =\sum_{i=0}^{h}(\delta\kappa)^i.
\tag{SP3}
```

**Theorem 1 (unweighted, sharp retained size).** There is a deterministic
algorithm retaining at most $`\min\{|E|,\kappa C\}`$ original items
with the following property: for every original feasible $`S`$ and every
$`e\in S`$, there is an $`f`$ in the retained ground, outside $`S-e`$, such
that $`S-e+f`$ is feasible. The construction uses

```math
O\!\left(|E|^2\Theta_{\kappa,h,\delta}\right)
\tag{SP4}
```

independence-oracle calls and parameter-polynomial bookkeeping per call.
In particular, the choice SP2 gives
$`2^{O(\delta\kappa\log(\delta\kappa+2))}|E|^{O(1)}`$
time in the oracle model. For fixed $`\delta`$, the retained size is
$`O_\delta(\kappa^{\delta+1})`$.

The size $`\kappa\binom{\delta\kappa}{\delta}`$ obtained from SP2 is
worst-case exact for this original-context single-replacement property,
even with a partition resource matroid and unit packing capacities.

**Theorem 2 (a bounded number of profit values).** Suppose items have fixed
signed rational profits taking $`q`$ distinct values. For each profit class
$`E_a`$, let $`r_a`$ be its rank in the rank-$`\kappa`$ truncation of $`M`$.
There is a deterministic restriction of size at most

```math
\min\left\{|E|,\ C\sum_a r_a\right\}
\le \min\{|E|,q\kappa C\}
\tag{SP5}
```

with the same call bound SP4. Every single replacement can have
**exactly the same profit** as the protected item. Consequently it
preserves the optimum fixed profit at every attainable cardinality up to
$`\kappa`$, including negative profits and arbitrary ties.

**Theorem 3 (arbitrary signed profits).** For any fixed signed rational
profits, define $`\Gamma(h,\delta)=(h+\delta)^{h+\delta}/(h^h\delta^\delta)`$
when $`h\delta>0`$, and $`\Gamma(h,\delta)=1`$ otherwise. A deterministic
restriction retains at most

```math
K=\min\{|E|,\lfloor\kappa\Gamma(h,\delta)\rfloor\}
\tag{SP5a}
```

original items. For every original feasible $`S`$ and every $`e\in S`$,
a retained item $`f\notin S-e`$ makes $`S-e+f`$ feasible and has profit
at least that of $`e`$. Thus the optimum profit is preserved at every
attainable cardinality, with no restriction on the number of distinct
profit values. The construction uses at most
$`|E|(K+1)\Theta_{\kappa,h,\delta}`$ independence queries after
sorting by nonincreasing profit and permanent ID. With SP2 and
$`\kappa\ge2`$, its support is at most

```math
\kappa\left(
\frac{\kappa^\kappa}{(\kappa-1)^{\kappa-1}}
\right)^\delta
\le e^\delta\kappa^{\delta+1}.
\tag{SP5b}
```

The worst-case exponent $`\delta+1`$ is exact for the original-context
replacement property, by the SP10 construction below. The Bernoulli
constant in SP5a is not asserted to be optimal. Theorem 2 still gives
exactly equal-profit replacements and can have a smaller support when
there are few profit classes.

These are fixed-parameter constructions. They do not replace the
[uniform polynomial-time sunflower reduction](deterministic-sparse-packing-oracle-kernel.md)
as a uniform polynomial-time guarantee. That reduction retains
$`O_\delta(\kappa^{2\delta+1})`$ items, or
$`O_\delta(\kappa^{2\delta})`$ for distinct supports. Here the smaller
ground is obtained by allowing the explicit exponential preprocessing
factor SP4. Both outputs keep the original resource oracle and item
encodings; neither is a parameter-only bit kernel.

## 2. The exact failure-summary primitive

The prerequisite is the arbitrary-matroid theorem in
[Sharp matroid and submodular failure summaries](../../matroid-failure-summaries/proof.md).
For a rank-$`r`$ oracle matroid whose elements have at most $`d`$ labels, it
retains at most $`r\binom{h+d}{d}`$ original elements and preserves rank
after every deletion of at most $`h`$ label classes. A rank equality between
a restriction and its parent is also equality of their matroid closures.

For clarity, its deterministic construction does not need to enumerate
all label subsets. To decide whether an element $`e`$ is necessary in a
current restriction, search for at most $`h`$ labels disjoint from
$`\Lambda(e)`$ whose removal leaves $`e`$ outside the closure of all other
survivors. At a search node choose a basis $`B`$ of the other current
survivors. If $`B`$ does not span $`e`$, the current failed labels are a
witness. Otherwise every possible witness must fail a label on $`B`$:
if $`B`$ survives intact, it continues to span $`e`$.

Branch on those labels, excluding labels on $`e`$, and reduce the remaining
failure budget by one. There are at most $`dr`$ branches per level and
depth at most $`h`$. Every node needs a greedy basis computation and one
independence test. Thus one deletion test costs
$`O(|E|\sum_{i=0}^{h}(dr)^i)`$ oracle calls. A single reverse-deletion
pass suffices: a witness protecting a retained element persists under
later deletions of other elements. The resulting restriction is
inclusion-minimal, and the circuit-blocking set-pair inequality in the
cited proof gives the exact binomial size. The search is exhaustive and
deterministic, with no random coloring, field representation, or
unimplemented separation oracle.

A depth-first implementation stores only the current branch and its
current surviving grounds. The budget is clipped to the number of
occurring labels, so this uses polynomial input workspace; an exponential
memoization table is unnecessary.

For Theorem 2 run this procedure separately inside each profit class,
using the rank-$`\kappa`$ truncation of the original resource matroid.
Each class has rank at most $`\kappa`$, and
$`\sum_a |E_a|^2\le |E|^2`$, giving SP4 and SP5. Restrictions are only
used inside the summary construction; all replacement contexts in the
next section belong to the original resource matroid.

### The ordered primitive for arbitrary profits

For Theorem 3 use the
[deterministic weighted oracle prefix construction](../../matroid-failure-summaries/manuscripts/weighted-oracle-prefix-fpt-construction.md)
on the whole rank-$`\kappa`$ truncation, with item order given by
nonincreasing profit and permanent ID. It preserves the closure of
every surviving prefix after every failure set of size at most $`h`$.
Its output is exactly the union of the canonical greedy bases under
those failures, and its size is at most
$`\kappa\Gamma(h,\delta)`$.

The construction processes items in that fixed order. To decide whether
to retain the next item, run the same failure-witness search against the
already retained earlier items. Induction on all failure queries shows
that the retained and original earlier prefixes have equal closure.
Thus the test keeps the item exactly when it has a nonclosure witness
in an original surviving prefix. Each test scans at most $`K`$ earlier
items, giving the stated $`|E|(K+1)\Theta_{\kappa,h,\delta}`$ query
bound. No randomness or representation is used by the algorithm.

For completeness, the size factor is the existing Bernoulli bound.
If an item has a witness $`F_e`$, independently failing every label with
probability $`p`$ makes it a greedy rank increment whenever all labels
of $`F_e`$ fail and all labels on the item survive. This event has
probability at least $`p^h(1-p)^\delta`$. The expected total rank is at
most $`\kappa`$, even though the random failure set used in this proof
may exceed $`h`$. Choosing $`p=h/(h+\delta)`$ gives SP5a. For SP2,
the expression simplifies to SP5b, using
$`(1+1/(\kappa-1))^{\kappa-1}\le e`$.

## 3. Saturated-row accounting and the replacement proof

Fix an original feasible $`S`$ and a protected item $`e\in S`$. Put
$`I=S-e`$, and let

```math
F_I=\{j:|I\cap A_j|=b_j\}
\tag{SP6}
```

be the saturated rows. All remaining capacities are positive. Each row
in $`F_I`$ contains at least one context item, so
$`|F_I|\le\delta|I|\le\delta(\kappa-1)`$. Feasibility of $`I+e`$
implies $`F_I\cap\Lambda(e)=\varnothing`$.

Apply the failure summary to the profit class containing $`e`$ (or to all
items in the unweighted case). The surviving retained items span $`e`$
in the rank-$`\kappa`$ truncation. But $`e`$ is outside the closure of $`I`$
there: $`I+e`$ is independent and has size at most $`\kappa`$. If every
retained survivor belonged to the closure of $`I`$, so would $`e`$.
Therefore a retained survivor $`f`$ lies outside that closure. It is
outside $`I`$, and $`I+f`$ is independent in the original matroid.

Since $`f`$ has no label in $`F_I`$, adding it does not use a saturated
packing row. Every other integer packing row has at least one unit of
slack, so SP1 remains feasible. The class construction also makes
$`c(f)=c(e)`$. This proves the original-context replacement property.
It is not necessary for $`I`$ to lie in the summary or in an intermediate
restriction.

Replacing omitted items one at a time terminates: each proper replacement
inserts a retained item outside the current set and removes an omitted
one. Cardinality and profit remain unchanged throughout. This proves the
optimization consequences without treating a rank-only summary as a
cost-prefix summary.

For Theorem 3, let $`P_e`$ be the ordered prefix ending at the protected
item. The surviving retained items in $`P_e`$ span $`e`$, by the ordered
primitive. The same closure argument gives a retained survivor
$`f\in P_e`$ outside the closure of $`I`$. Its position guarantees that
its profit is at least the profit of $`e`$. It also avoids every saturated
row, so the original-context replacement remains feasible. Iteration
preserves cardinality and never decreases profit. A restriction cannot
improve the original optimum, so the best retained profit equals the
original optimum at every cardinality. This applies to signed profits
and does not require dropping negative-profit items.

### A computable capacity-sensitive budget

Define the exact rational row load of an item by

```math
\rho(e)=\sum_{j\in\Lambda(e)}\frac1{b_j}.
\tag{SP7}
```

Let $`H_{\kappa-1}`$ be the sum of the largest at most $`\kappa-1`$
such loads in the prepared ground. Then one may choose

```math
h=\min\left\{L,\lfloor H_{\kappa-1}\rfloor\right\},
\tag{SP8}
```

where $`L`$ is the number of occurring row labels. Indeed,

```math
|F_I|
 =\sum_{j\in F_I}\frac{|I\cap A_j|}{b_j}
 \le\sum_j\frac{|I\cap A_j|}{b_j}
 =\sum_{e\in I}\rho(e)
 \le H_{\kappa-1}.
\tag{SP9}
```

Sorting these rational loads and taking their sum has polynomial bit
complexity; binary capacities are never expanded. If every retained row
has capacity at least $`b`$, this gives
$`h\le\lfloor\delta(\kappa-1)/b\rfloor`$. The smaller budget improves
both the support SP3 and the branching time SP4. It also improves the
sunflower reduction's layer count to $`h+1`$, as its deletion proof uses
only an upper bound on the number of saturated rows.

## 4. Exact worst-case sharpness

Assume $`\kappa,\delta\ge1`$. Take a row universe $`U`$ of size
$`\delta\kappa`$, with capacity one in every row. Use $`\kappa`$
resource classes, each with partition-matroid capacity one. For every
class $`i`$ and every $`\delta`$-subset $`A\subseteq U`$, introduce one
item $`(i,A)`$ incident with exactly the rows of $`A`$. All profits are zero.

There are exactly

```math
\kappa\binom{\delta\kappa}{\delta}
\tag{SP10}
```

items. Fix any protected $`(i,A)`$. Partition $`U\setminus A`$ into
$`\kappa-1`$ disjoint $`\delta`$-sets, and assign one to each resource
class other than $`i`$. Their items form a feasible context $`I`$.
Any item extending $`I`$ in the resource matroid must belong to class $`i`$.
Its support must avoid every occupied row in $`U\setminus A`$, hence
be a $`\delta`$-subset of $`A`$. Its support is therefore exactly $`A`$,
so it is the protected item itself.

Every original item is forced by some original feasible context. Thus
every restriction with the single-replacement property must retain all
SP10 items. This proves exact sharpness for that property. It is not a
lower bound for preserving only one no-failure optimum: in an unweighted
instance, one maximum feasible solution alone would preserve that much
weaker objective.

## 5. Useful specializations

For a graph matching with an arbitrary matroid on original edge records,
delete graph loops and put a capacity-one packing row at each vertex. Every edge has two labels,
so the unweighted restriction has at most

```math
\kappa\binom{2\kappa}{2}=O(\kappa^3)
\tag{SP11}
```

original edges, in deterministic
$`2^{O(\kappa\log(\kappa+2))}|E|^{O(1)}`$ oracle time. The graph may
be nonbipartite and may have parallel records. The resource is on edges,
not on their endpoints. With $`q`$ fixed profit values multiply the support
bound by $`q`$ if exactly equal-profit replacements are desired.
For arbitrary signed profits, Theorem 3 gives at most
$`e^2\kappa^3`$ original edges with no-worse-profit replacements and
the same FPT parameter dependence. The same argument treats hyperedge
records of maximum size $`\delta`$ and arbitrary positive integer vertex
capacities.

When SP8 gives $`h\le1`$, an additional stronger endpoint is available.
The arbitrary-matroid one-label-failure theorem preserves fixed cost
prefixes in uniform polynomial time and uses at most $`(\delta+1)r`$
elements. Apply it once to the entire rank-$`\kappa`$ resource in
nonincreasing profit order. Its surviving earlier-prefix closure supplies
a no-worse-profit replacement by the same proof as Section 3. Thus

```math
|R|\le(\delta+1)\kappa
\tag{SP12}
```

holds with arbitrary many signed profit values and uniform polynomial
preprocessing in this bounded-conflict case. If $`h=0`$, ordinary ordered
greedy improves SP12 to $`\kappa`$. The special one-failure prefix theorem
has a better support and a uniform polynomial construction; for $`h\ge2`$
Theorem 3 instead uses the Bernoulli support with FPT preprocessing.
The exact-binomial weighted extension is false for arbitrary matroids,
as the [two-failure obstruction](../../matroid-failure-summaries/manuscripts/weighted-oracle-two-failure-obstruction.md)
shows. That obstruction does not invalidate SP5a.

## 6. Evidence, dependencies, and comparison

The [finite checker](../verify/check_sharp_packing.py) implements the
deterministic deletion-witness search as an oracle procedure and compares
its output with exhaustive original feasible contexts. It separately
checks the ordered arbitrary-profit reduction, the forcing construction,
and the capacity-load inequality. The
[weighted-prefix checker](../../matroid-failure-summaries/verify/check_weighted_prefix.py)
tests the new ordered primitive against complete rank tables, including
the nonrepresentable two-failure example. These are finite correctness
checks; the statements for arbitrary input sizes are proved above and
in the cited failure-summary theorems.

The mathematical prerequisites are the matroid rank/closure axioms, the
internally proved circuit-blocking summary theorem, and its one-failure
ordered-greedy endpoint. The arbitrary-profit version additionally uses
the internally proved retained-prefix witness construction and the
existing Bernoulli size bound. No external algorithmic implementation
is required beyond the stated original independence oracle.

Huang, Kakimura, Kobayashi and Terao,
[*Polynomial Kernels with Reachability for Weighted d-Matroid
Intersection*, arXiv:2603.17345v1](https://arxiv.org/html/2603.17345v1),
gives randomized polynomial-time reachable kernels, including
$`\widetilde O(\kappa^3)`$ for matching with an edge matroid. Its
deterministic and randomized guarantees, construction times, and
reachability quantifiers are recorded in the
[sunflower manuscript](deterministic-sparse-packing-oracle-kernel.md).
The present results supply an exact binomial unweighted bound, an
$`O_\delta(\kappa^{\delta+1})`$ arbitrary-profit bound, and deterministic
original-context replacements with explicitly exponential preprocessing.
They do not assert a uniform-polynomial derandomization of that paper or
a new lower bound for ordinary optimization kernels.

**Attribution:** Yilin Liu and GPT-6 Astra Pro.
