# Sharp matroid and submodular failure summaries

## 1. Statements and distinction of models

Each element of a rank-$r$ matroid has at most $d$ failure labels. A query fails a set $F$ of at most $h$ labels and retains $E_F=\{e:\Lambda(e)\cap F=\varnothing\}$. Put $C=\binom{h+d}{d}$.

**Theorem 1 (represented, fixed cost).** A rational or explicitly represented finite-field matroid admits a deterministic uniformly polynomial construction retaining at most $\min\{N,rC\}$ original elements. The restriction preserves the span at every surviving prefix of one fixed cost order and contains the canonical minimum-cost basis after every failure, including rank drops.

**Theorem 2 (arbitrary oracle, rank).** Every inclusion-minimal restriction preserving all surviving ranks has at most $rC$ elements. One can construct such a restriction in deterministic $f(r,h,d)N^{O(1)}$ independence-oracle time. Direct failure enumeration is an XP alternative. The final deletion step preserves rank and feasibility, without an arbitrary-cost-prefix claim.

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

Encode the current labels as low-degree polynomials over a prime field of size $q=O(dh\log(L+1)+1)$. Some evaluation separates any disjoint own-label set of size at most $d$ from a failed-label set of size at most $h$: their pairwise-difference product is nonzero and has degree below $q$.

For each evaluation and each palette of at most $d$ field values, retain a basis of the pool whose label images all lie in that palette. The union has size at most $rq(q+1)^d$. A separating pool contains any protected survivor and no failed item, so the union spans every survivor after every query. This property composes through repeated restrictions.

On a current ground of size $s$, the bound is $B(\log(s+2))^{d+1}$, with $B$ depending only on $r,h,d$. Above an effective parameter-only threshold it is at most $s/2$. Repeat to that threshold, then run exact reverse deletion enumerating all bounded-ground failure sets. The result proves Theorem 2. The rank is part of the parameter.

## 5. Submodular and entropy consequences

For monotone submodular $f$, write $H_e=\{x:A_x\cap B_e=\varnothing\}$ and $\delta_e=f(H_e)-f(H_e-e)$. The same permutation method gives
$$
\sum_e\frac{\delta_e}{\binom{|A_e|+|B_e|}{|A_e|}}\le f(H)-f(\varnothing).
$$
Indeed, order selected elements by their last own-label. Earlier selected elements lie in $H_e-e$, so diminishing returns gives marginal at least $\delta_e$. Sum the marginals and take expectations.

If $f$ is integer-valued with range $R=f(E)-f(\varnothing)$, an inclusion-minimal exact failure-value summary has at most $RC$ items. Replace each pool basis by a value-increasing subset to obtain the analogous fixed-parameter construction. Without integrality, the valid cardinality-free conclusion is
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

## Complete proofs

[Represented lift and field construction](manuscripts/sharp-represented-matroid-failure-summaries.md); [arbitrary-matroid and submodular proofs](manuscripts/arbitrary-matroid-and-submodular-failure-summaries.md).

**Attribution:** Yilin Liu and GPT-6 Astra Pro.
