# Deterministic FPT construction of weighted oracle failure summaries

## 1. The retained size and construction time

Let $M$ be an arbitrary independence-oracle matroid on an explicitly
listed ground $E$ of size $N$ and rank $r$. Each item $e$ has a set
$\Lambda(e)$ of at most $d$ labels. A failure set $F$ deletes every item
whose label set intersects $F$; write $X_F$ for the survivors in $X$.
The failure budget is $|F|\le h$. Fix one total item order, for example
nondecreasing signed rational cost followed by a permanent item ID.
Let $P_i$ be its first $i$ items.

Define

$$
\Gamma(h,d)=
\begin{cases}
\dfrac{(h+d)^{h+d}}{h^h d^d},&h,d>0,\\
1,&hd=0,
\end{cases}
\qquad
S(a,h)=\sum_{j=0}^{h}a^j,
\quad 0^0=1.
\tag{WP1}
$$

**Theorem 1.** A deterministic algorithm returns the unique smallest
original-item set $H$ such that

$$
r_M(H\cap(P_i)_F)=r_M((P_i)_F)
\quad\text{for every }i\text{ and every }|F|\le h.
\tag{WP2}
$$

The set $H$ is exactly the union of the canonical greedy bases of $E_F$
over all allowed $F$. In particular, it contains the canonical
minimum-cost surviving basis, including when the surviving rank drops.
Its size is at most

$$
K=\min\{N,\lfloor r\Gamma(h,d)\rfloor\}.
\tag{WP3}
$$

After sorting the items, the algorithm uses at most

$$
N(K+1)S(dr,h)
\tag{WP4}
$$

independence queries. Explicit label bookkeeping requires
$O((d+1)N(K+1)S(dr,h))$ ordinary operations after labels have been
indexed. A depth-first implementation uses
$O((h+1)(K+1))$ item IDs as search workspace, in addition to the input,
label records and retained output. One may clip $h$ to the number of
occurring labels. The algorithm does not need to know $r$ or $K$ in
advance.

The size factor $\Gamma$ is the prior project W--LF baseline, already
recorded in the [arbitrary-matroid comparison](arbitrary-matroid-and-submodular-failure-summaries.md#8-antecedents-and-comparison-to-public-results)
and the [represented comparison](sharp-represented-matroid-failure-summaries.md#8-baselines-and-attribution-boundaries).
The contribution here is a complete deterministic FPT construction of
the canonical prefix summary, with oracle work depending on the retained
prefix size. Section 3 reproves the size bound so the algorithm does not
depend on an unavailable historical checkpoint. No priority claim for
the factor or its probabilistic proof is made.

The parameters in WP4 include $r,h,d$. This is an FPT oracle algorithm;
it is not a uniform polynomial-time algorithm when all three parameters
are unrestricted. The output retains the original oracle and item
encodings, so WP3 is an item-count bound, not a parameter-only bit kernel.

## 2. Exact prefix witnesses

For an item $e_i$ at position $i$, call $F$ a prefix witness if
$|F|\le h$, $F\cap\Lambda(e_i)=\varnothing$, and

$$
e_i\notin\mathrm{cl}_M((P_{i-1})_F).
\tag{WP5}
$$

An item belongs to the canonical greedy basis of $E_F$ exactly when it
survives and increases the rank of the earlier surviving prefix. Thus
the union $H_*$ of all these bases consists precisely of the items with
a prefix witness.

Every set satisfying WP2 must contain every item of $H_*$. If $e_i$ is
omitted, its witness gives a strict rank increase from $(P_{i-1})_F$ to
$(P_i)_F$, while the restricted prefix contains only earlier items.
Conversely, $H_*$ contains the full canonical basis for every $F$, and
the portion of that basis in $P_i$ is a basis of $(P_i)_F$. Therefore
$H_*$ satisfies WP2. It is the unique minimum set for this simultaneous
prefix requirement, not merely an inclusion-minimal output.

This optimality concerns preserving every prefix of this one fixed order.
It does not claim minimum cardinality among summaries preserving only
final ranks, or among restrictions preserving only one optimum-cost
value when several bases have tied costs.

## 3. The existing Bernoulli size bound

For each $e_i\in H_*$ choose a prefix witness $F_i$. Independently fail
each occurring label with probability $p\in(0,1)$, giving a random
failure set $Z$. In this proof $Z$ may contain more than $h$ labels;
the rank bound $r_M(E_Z)\le r$ holds for all $Z$.

The event

$$
F_i\subseteq Z,
\qquad Z\cap\Lambda(e_i)=\varnothing
\tag{WP6}
$$

has probability $p^{|F_i|}(1-p)^{|\Lambda(e_i)|}$, at least
$p^h(1-p)^d$. On this event $e_i$ survives and its earlier surviving
prefix is contained in $(P_{i-1})_{F_i}$. A smaller set cannot span an
item that the larger set does not span. Thus $e_i$ contributes one to
the greedy rank of $E_Z$.

Summing the rank contributions and taking expectations gives the useful
nonuniform inequality

$$
\sum_{e_i\in H_*}
p^{|F_i|}(1-p)^{|\Lambda(e_i)|}
\le \mathbb E[r_M(E_Z)]\le r.
\tag{WP7}
$$

For $h,d>0$, choose $p=h/(h+d)$ to obtain
$|H_*|\le r\Gamma(h,d)$. If $h=0$ or $d=0$, there is only one
effective surviving ground, and $H_*$ is its ordinary canonical basis.
This proves WP3 in every case.

No random choices are used by the construction. The product measure
only bounds the size of its deterministic output. In particular, the
proof does not enumerate or sample failure sets in the implementation.

## 4. A complete failure-witness search

Suppose $Q$ is an earlier retained prefix and $e$ is the next item.
We test whether some $F$ of at most $h$ labels, avoiding $\Lambda(e)$,
makes $e\notin\mathrm{cl}_M(Q_F)$. At a search node let $Y$ be the
surviving part of $Q$, $F_0$ the labels already failed, and $t$ the
remaining budget.

1. Compute any greedy basis $B$ of $Y$.
2. If $B+e$ is independent, return $F_0$.
3. If $t=0$, return `NONE`.
4. For each label $\lambda$ on $B$ that is not on $e$, recurse on
   $Y_{\{\lambda\}}$, $F_0\cup\{\lambda\}$, and $t-1$.
   Return the first witness found, or `NONE` if every child fails.

The fixed input order specifies every basis scan and branch order, so
the search is deterministic. Already failed labels cannot occur on $B$.
Each branch spends one new failure, and no branch deletes $e$.

**Completeness.** If step 2 fails, $B$ spans $e$. Any successful further
failure must hit a label on $B$: otherwise all of $B$ survives and still
spans $e$. Such a label cannot be on $e$. Hence every valid witness has
a first branch in step 4, and induction on $t$ proves that the search
returns a witness exactly when one exists. This is the
[rank-summary witness search](arbitrary-matroid-and-submodular-failure-summaries.md#5-a-deterministic-failure-witness-search)
applied to a protected next item and an earlier prefix.

The basis has at most $r$ items, so there are at most $dr$ branches per
node and at most $S(dr,h)$ nodes. A node uses at most $|Q|+1$
independence queries. No enumeration of the full label universe or
exponential memoization table is required.

## 5. Retain only the necessary earlier prefix

Start with $H_0=\varnothing$. Process $e_1,\ldots,e_N$ in the fixed
order. Run the search in Section 4 with $Q=H_{i-1}$ and protected item
$e_i$. Keep $e_i$ exactly when the search returns a witness; otherwise
set $H_i=H_{i-1}$.

The invariant is

$$
\mathrm{cl}_M((H_i)_F)
 =\mathrm{cl}_M((P_i)_F)
\quad\text{for every }|F|\le h.
\tag{WP8}
$$

It is true at $i=0$. At the next step, WP8 for $i-1$ makes a witness
against the retained earlier prefix equivalent to a witness against the
original earlier prefix. If there is a witness, the algorithm keeps the
item, and adjoining the same surviving item to sets with equal closure
preserves closure equality. If there is no witness, $e_i$ is spanned by
the retained earlier survivors for every allowed failure that does not
delete it. Omitting it therefore preserves the invariant in this case
as well. Failures that delete $e_i$ require no change.

It follows that the algorithm keeps exactly the items with original
prefix witnesses, hence returns $H_*$. This explains why it is safe to
query only retained prefixes. Merely applying rank-only reverse deletion
to the entire ground would not give this property.

At every step $|H_{i-1}|\le |H_*|\le K$. There are $N$ searches,
each using at most $(K+1)S(dr,h)$ queries, proving WP4. The same count
with $N+1$ in place of $K+1$ gives a simpler alternative implementation
that always tests the complete original earlier prefix. An input already
presented in the specified order can be processed in one pass, since
future items are never inspected by the search. This is an ordered-input
statement, not a dynamic-update or arbitrary-order streaming guarantee.

For a query $F$, filter $H$ and run ordinary greedy in the fixed order.
This uses at most $|H|$ independence queries and returns exactly the
canonical greedy basis that would be obtained on $E_F$.

## 6. Sharp endpoints and the obstruction

When $h=1$, use the separate
[one-failure construction](arbitrary-matroid-and-submodular-failure-summaries.md#7-weighted-oracle-summaries-for-one-label-failure).
It gives the same canonical-basis union, has the sharper size
$(d+1)r$, and uses at most $(1+dr)N$ independence queries in uniform
polynomial time. When a linear representation is supplied, the
[polynomial feature construction](sharp-represented-matroid-failure-summaries.md)
attains $r\binom{h+d}{d}$ in uniform polynomial time for every $h$.

The [weighted oracle obstruction](weighted-oracle-two-failure-obstruction.md)
shows why WP3 is not simply replaced by this exact binomial expression
for arbitrary matroids: rank four, one label per item, and two failures
can force 13 retained items, exceeding $4\binom{3}{1}=12$. Its amplified
examples fail the proposed sharp weighted formula for every $h\ge2$.
The exact optimal universal weighted-oracle size between that lower
bound and WP3 remains outside the claims here.

For sparse packing with item-label degree $\delta$ and solution bound
$\kappa$, the saturated-row budget $h=\delta(\kappa-1)$ gives

$$
\kappa\Gamma(\delta(\kappa-1),\delta)
 =\kappa\left(
 \frac{\kappa^\kappa}{(\kappa-1)^{\kappa-1}}
 \right)^\delta
 \le e^\delta\kappa^{\delta+1}
\quad (\kappa\ge2).
\tag{WP9}
$$

Using nonincreasing profit order now gives no-worse-profit replacements
for arbitrary many signed profit values. The full original-context
packing transfer is in the
[sparse-packing manuscript](../../weighted-prefix-quota-frontier/manuscripts/sharp-sparse-packing-fpt-restrictions.md).
The exact-binomial rank-only and equal-profit-class alternatives remain
useful when their stronger constants or equality requirements apply.

## 7. Integral-submodular prefix values

There is an analogous construction for an integer-valued monotone
submodular function $f$, with
$R=f(E)-f(\varnothing)$. Keep an item precisely when some allowed
failure gives it a positive marginal on its earlier surviving prefix.
The resulting unique smallest prefix-value preserver has at most
$R\Gamma(h,d)$ items. Indeed, on WP6 its marginal is still positive
by diminishing returns, hence at least one by integrality. The sum of
all surviving prefix marginals telescopes to
$f(E_Z)-f(\varnothing)\le R$, giving WP7 with $R$.

Use the [value-witness search](arbitrary-matroid-and-submodular-failure-summaries.md#9-monotone-submodular-functions):
at a zero-marginal node choose a value-spanning set $B$ of the earlier
survivors by keeping only positive marginal items. It has at most $R$
items. Every successful witness must delete a label on $B$ that is not
on the protected item, so branching has at most $dR$ choices. The
search uses $O(N(K_f+1)S(dR,h))$ value queries, where
$K_f=\min\{N,\lfloor R\Gamma(h,d)\rfloor\}$.

The retained-prefix invariant is exact value equality. For
$A\subseteq B$ with $f(A)=f(B)$, monotonicity and diminishing returns
give $f(A+e)=f(B+e)$ for every item $e$. Thus tests against retained
and original earlier prefixes agree. The numerical range $R$, rather
than its bit length, is part of the parameter. This statement preserves
values of one ordered prefix sequence under failures; it does not claim
an exact coreset for arbitrary minimum-cost submodular cover.

## 8. Verification and dependency scope

The [finite checker](../verify/check_weighted_prefix.py) independently
enumerates canonical bases and all prefix ranks from complete matroid
rank tables. It compares their exact union with the output of the
retained-prefix witness algorithm, verifies each necessity witness and
the explicit oracle-call bound, and checks the Bernoulli event implication
also on failure sets larger than the requested budget. It includes all
labeled matroids on at most four items and the nonrepresentable
13-item obstruction. These are finite checks, not a proof for all
matroids; the general proof is Sections 2--5. The integral-submodular
corollary is proved in Section 7 and is not covered by that checker.

The construction requires only the original independence oracle,
finite explicit label lists and the fixed item order. There is no field
representation, randomization, separator implementation or external
solver dependency.

**Attribution:** Yilin Liu and GPT-6 Astra Pro.
