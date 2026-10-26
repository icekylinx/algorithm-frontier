# Sharp matroid and submodular failure summaries

## 1. Statements and distinction of models

Each element of a rank-$r$ matroid has at most $d$ failure labels. A query fails a set $F$ of at most $h$ labels and retains $E_F=\{e:\Lambda(e)\cap F=\varnothing\}$. Put $C=\binom{h+d}{d}$.

**Theorem 1 (represented, fixed cost).** A rational or explicitly represented finite-field matroid admits a deterministic uniformly polynomial construction retaining at most $\min\{N,rC\}$ original elements. The restriction preserves the span at every surviving prefix of one fixed cost order and contains the canonical minimum-cost basis after every failure, including rank drops.

**Theorem 2 (arbitrary oracle, rank).** Every inclusion-minimal restriction preserving all surviving ranks has at most $rC$ elements. One can construct such a restriction in deterministic $f(r,h,d)N^{O(1)}$ independence-oracle time. Direct failure enumeration is an XP alternative. The final deletion step preserves rank and feasibility, without an arbitrary-cost-prefix claim.

The explicit construction uses at most
$N(N+1)\sum_{i=0}^{h}(dr)^i$ independence queries. It needs no linear
representation or separating-family construction.
Section 4.2 improves this to a linear dependence on $N$ for fixed
$r,h,d$ by first constructing a bounded weighted-prefix summary.

**Theorem 3 (one failed label, arbitrary oracle and fixed cost).** For
$h=1$, the sharp weighted-prefix guarantee also holds for arbitrary
independence-oracle matroids: at most $(d+1)r$ elements, constructed with
at most $(1+dr)N$ independence queries in uniform polynomial time. The
same weighted oracle bound with $h\ge2$ is false in general, as follows.

**Theorem 4 (weighted representation boundary).** For every $h\ge2$
there is a rank-four arbitrary-oracle matroid, with one label per element,
whose exact minimum-cost surviving bases force $4(h+1)+1$ retained
elements. Thus the weighted bound $r\binom{h+d}{d}$ cannot extend to
all oracle matroids even at $d=1$. Section 6 gives the construction.

**Theorem 5 (arbitrary-budget weighted oracle construction).** Put

$$
\Gamma(h,d)=
\begin{cases}
(h+d)^{h+d}/(h^h d^d),&h,d>0,\\
1,&hd=0,
\end{cases}
\qquad K=\min\{N,\lfloor r\Gamma(h,d)\rfloor\}.
$$

The unique minimum restriction preserving every surviving prefix of
one fixed order has at most $K$ elements. It can be constructed
deterministically with at most
$N(K+1)\sum_{i=0}^{h}(dr)^i$ independence queries, after sorting.
The size factor is the existing project W–LF bound; the new construction
uses explicit bounded-depth witness searches on retained prefixes.
Its proof and distinction from the sharp represented bound are in the
[weighted oracle construction](manuscripts/weighted-oracle-prefix-fpt-construction.md).

## 2. Proof of the represented theorem

Choose distinct field points $a_0,a_\lambda$, with $a_0$ never failing. For element $e$, define
$$
g_e(T)=(T-a_0)^{d-|\Lambda(e)|}\prod_{\lambda\in\Lambda(e)}(T-a_\lambda)
=T^d+\sum_{j<d}b_j(e)T^j.
$$
Let $\phi(e)$ list all monomials of total degree at most $h$ in the $d$ coefficients. Its dimension is $C$. For each query,
$$
\prod_{\lambda\in F}g_e(a_\lambda)=\ell_F(\phi(e))
$$
is a linear functional of those monomials, zero exactly when $e$ fails.

After compressing the original representation to rank $r$, retain a fixed-order greedy basis of $v_e\otimes\phi(e)$. Every omitted column is a linear combination of earlier retained columns. Applying $I\otimes\ell_F$ kills failed columns and maps survivors to nonzero scalar multiples of their original columns. Division by the protected column's scalar proves equality of surviving prefix spans. An element accepted by canonical greedy cannot be omitted, since it would already lie in the span of earlier retained survivors. This proves Theorem 1. $\square$

Compute $rC$ with saturation before enumerating features; if $rC\ge N$, return the input. Otherwise the lift has fewer than $N$ rows. Rational feature bit lengths are polynomial. If a finite field is too small, use an extension with at least $L+1$ elements; when an extension is needed its size can be kept below $(L+1)^2$, permitting deterministic enumeration of irreducible polynomials. Extending scalars preserves original ranks.

## 3. Circuit-blocking set-pair lemma

**Lemma 3.1.** Give each $e\in H$ disjoint label sets $A_e,B_e$, and assume
$$
e\notin\mathrm{cl}\{f\in H-e:A_f\cap B_e=\varnothing\}.
$$
Then
$$
\sum_{e\in H}\binom{|A_e|+|B_e|}{|A_e|}^{-1}\le r(H).
$$

**Proof.** Uniformly order the labels and select $e$ when every $A_e$-label precedes every $B_e$-label. The selection probability is the reciprocal binomial coefficient. If a selected circuit existed, choose $e$ whose last own-label is latest. The hypothesis supplies another circuit element $f$ with a label in $A_f\cap B_e$. Its position is no later than the last $A_e$-label, contradicting selection of $e$. Empty own-label sets are placed first. Hence every selected set is independent; take expectations. $\square$

For an inclusion-minimal rank-preserving restriction, each $e$ has a failure witness $F_e$ under which it is a coloop. Apply the lemma with $A_e=\Lambda(e)$, $B_e=F_e$. Both sizes are bounded by $d,h$, so $|H|\le rC$.

For tightness, use $r$ parallel classes. In each class, create one element for every $d$-subset $A$ of an $(h+d)$-label universe, with labels $A$. Failing the complement of $A$ isolates that element in its class; all $rC$ elements are necessary.

## 4. Fixed-parameter construction

To decide whether a current element $e$ can be deleted, search for at most
$h$ failed labels avoiding $\Lambda(e)$ under which $e$ becomes a coloop.
At a search node, let $Y$ be the surviving restriction and compute a basis
$B$ of $Y-e$. If $B+e$ is independent, the labels already failed are a
valid witness. Otherwise $B$ spans $e$. Any remaining successful failure
must hit a label of $B$: if all of $B$ survives, it still spans $e$.
Branch on every label in $\Lambda(B)\setminus\Lambda(e)$, delete its entire
class, and decrease the remaining budget. Return no witness when the
budget is exhausted or every child fails. Induction on the budget proves
completeness, with at most $dr$ children per node.

Process the original elements once, deleting $e$ exactly when the search
finds no witness. Every deletion preserves all ranks. A witness that keeps
$e$ remains valid after later deletions, because taking a subset cannot
make $e$ enter its closure. The result is inclusion-minimal, so Section 3
gives size $rC$. Each search uses at most $\sum_{i=0}^{h}(dr)^i$ nodes and
at most $N+1$ independence queries per node, proving Theorem 2 with the
explicit bound above. Rank is part of the parameter.

### 4.1 Sharp weighted oracle construction for one failure

Let $B_0$ be the canonical greedy basis in one fixed total cost order.
For every label $\lambda$ occurring on $B_0$, compute the canonical basis
$B_\lambda$ after that label fails. Retain their union with $B_0$.
A surviving element accepted by the original greedy scan remains accepted
after deletions: its earlier set has only shrunk. Thus, writing
$D_\lambda$ for the failed class, $B_0\setminus D_\lambda\subseteq B_\lambda$.
Since $|B_\lambda|\le r$,

$$
|B_\lambda\setminus B_0|\le|B_0\cap D_\lambda|,
\qquad
\left|B_0\cup\bigcup_\lambda B_\lambda\right|
 \le r+\sum_{e\in B_0}|\Lambda(e)|\le(d+1)r.
$$

A failed label missing $B_0$ leaves that entire canonical basis unchanged.
Every other query has its canonical basis included in the retained union.
Canonical greedy basis elements in each prefix span that prefix, so this
containment preserves every prefix rank, including prefixes within ties.
At most $dr+1$ greedy scans give the construction cost. The lower example
of Section 3 with $h=1$ proves sharpness. This proves Theorem 3, including
signed costs and rank drops.

### 4.2 Linear input dependence for the sharp rank construction

First apply Theorem 5 using the input order; no cost sorting is needed.
Its output $Q$ has at most $K$ items and preserves every surviving rank.
Run the reverse deletion of Section 4 only on $Q$. The final restriction
still preserves the ranks of the original ground and has the sharp
size $rC$. The total number of independence queries is at most

$$
(N+K)(K+1)\sum_{i=0}^{h}(dr)^i.
$$

The first pass only scans the current retained prefix inside each witness
search; the final pass only scans $Q$. Thus this bound requires no hidden
rescans of the original $N$ items. Sparse lists of original item IDs give
$O((d+1)(N+K)(K+1)\sum_{i=0}^{h}(dr)^i)$ ordinary bookkeeping
operations after explicit label indexing. For fixed $r,h,d$ the oracle
query count is linear in $N$. The direct quadratic construction remains
a transparent alternative with the same sharp output bound.

## 5. Submodular and entropy consequences

For monotone submodular $f$, write $H_e=\{x:A_x\cap B_e=\varnothing\}$ and $\delta_e=f(H_e)-f(H_e-e)$. The same permutation method gives
$$
\sum_e\frac{\delta_e}{\binom{|A_e|+|B_e|}{|A_e|}}\le f(H)-f(\varnothing).
$$
Indeed, order selected elements by their last own-label. Earlier selected elements lie in $H_e-e$, so diminishing returns gives marginal at least $\delta_e$. Sum the marginals and take expectations.

If $f$ is integer-valued with range $R=f(E)-f(\varnothing)$, an inclusion-minimal exact failure-value summary has at most $RC$ items. The witness search extends directly: a positive current marginal for $e$ is a witness. Otherwise greedily form $B\subseteq Y-e$ with $f(B)=f(Y-e)=f(Y)$ and $|B|\le R$. Since $f(B+e)=f(B)$, any failure preserving $B$ keeps the marginal of $e$ zero by diminishing returns. Branch on the at most $dR$ labels on $B$ that avoid $e$. The same induction and reverse deletion use $O(N(N+1)\sum_{i=0}^{h}(dR)^i)$ value queries. Without integrality, the valid cardinality-free conclusion is
$$
\sum_e\max_{\substack{|F|\le h\\\Lambda(e)\cap F=\varnothing}}
 [f(E_F)-f(E_F-e)]\le C R.
$$
For finite joint Shannon entropy this becomes
$$
\sum_e\max_{\substack{|F|\le h\\\Lambda(e)\cap F=\varnothing}}
 H(X_e\mid X_{E_F-e})\le C H(X_E).
$$
Copies of independent variables indexed by the $d$-subsets attain equality.

The [ordered value-summary construction](manuscripts/weighted-oracle-prefix-fpt-construction.md#7-integral-submodular-prefix-values)
also permits the two-stage improvement above. With
$K_f=\min\{N,\lfloor R\Gamma(h,d)\rfloor\}$, first form that
prefix summary, then apply value-preserving reverse deletion to it.
This retains at most $RC$ items with
$O((N+K_f)(K_f+1)\sum_{i=0}^{h}(dR)^i)$ value queries.
The numerical range $R$ is a parameter; this is not a bound polynomial
in the binary length of $R$.

## 6. The weighted boundary is an explicit obstruction

Start with a rank-four matroid on eight classes: every four-set is a basis
except $\{0,1,2,3\}$, $\{0,1,4,5\}$, $\{0,1,6,7\}$,
$\{2,3,4,5\}$ and $\{2,3,6,7\}$. Different forbidden sets intersect
in at most two elements, so among two or more one-element exchanges
sharing a three-set at most one is forbidden. This proves basis exchange.

The [explicit 13-item parallel extension](manuscripts/weighted-oracle-two-failure-obstruction.md#3-the-13-ordered-colored-items)
assigns one of four labels and cost $2^{i-1}$ to item $i$. Its six
two-label-failure optima are unique and their union is all 13 elements.
Each omitted element therefore destroys some exact minimum-cost value,
although $r\binom31=12$. The full table and its short greedy traces
are in the linked proof; the exact checker separately enumerates every
surviving basis and optimum.

For any $h\ge2$, prepend $h-2$ copies of an underlying four-element
basis, each with its own new single label and earlier costs. Every item
in block $j$ is forced after the earlier block labels fail. Each original
item is forced after all block labels and its two original witness labels
fail. There are $4(h-2)+13=4(h+1)+1$ forced elements and the rank stays
four. All allowed failures still leave a basis. Direct sums give
$r(h+1)+r/4$ for $r$ divisible by four. This proves Theorem 4.

The represented lift is unaffected; the underlying eight-class matroid is
not representable over any field, as proved in the obstruction manuscript.
The rank-only theorem is also unaffected: the same 13-item example has a
nine-item restriction preserving every required surviving rank.

## Complete proofs

[Represented lift and field construction](manuscripts/sharp-represented-matroid-failure-summaries.md); [arbitrary-matroid and submodular proofs](manuscripts/arbitrary-matroid-and-submodular-failure-summaries.md); [weighted oracle FPT construction](manuscripts/weighted-oracle-prefix-fpt-construction.md); [weighted two-failure obstruction](manuscripts/weighted-oracle-two-failure-obstruction.md).

**Attribution:** Yilin Liu and GPT-6 Astra Pro.
