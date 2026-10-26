# Universal packing summaries under failures

## 1. Theorem

Each explicit item $e$ has a packing set $S_e$ of size at most $p$, fixed signed rational cost, and at most $d_j$ labels in each failure system $j$. Positive solutions contain at most $K$ items with pairwise disjoint packing sets. A query fails at most $h_v$ universe elements and $h_j$ labels in system $j$. An optional resource matroid is supplied by a rational or finite-field representation of full rank $r$.

There is a deterministic uniformly polynomial restriction of size at most
$$
\min\{N,D\},\qquad
D=r\binom{pK+h_v}{p}\prod_j\binom{h_j+d_j}{d_j}.
$$
Omit $r$ when no resource is present. It preserves minimum fixed positive cost for every prescribed positive cardinality up to $K$, all allowed failures, and every fixed quota-free background in a later matroid extension. The extension must restrict to the original positive matroid; it need not be represented.

## 2. Construction

Normalize $p$ to $\max\{1,\max_e|S_e|\}$, then pad every set to size $p$ using private never-failing dummies. This keeps padding polynomial and prevents duplicate use of initially empty items.

Put $t=pK+h_v$. Represent padded universe elements by Vandermonde columns $u_x\in\mathbb F^t$ at distinct field points. Any at most $t$ distinct columns are independent. Define
$$
a_e=\bigwedge_{x\in S_e}u_x\in\bigwedge^p\mathbb F^t.
$$
For each failure system, use the coefficient feature $\phi_j(e)$ of dimension $\binom{h_j+d_j}{d_j}$, with query functional zero exactly on failed items. Retain a cost-ordered greedy basis of
$$
z_e=v_e\otimes a_e\otimes\bigotimes_j\phi_j(e).
$$
Without a resource, omit $v_e$. The dimension is $D$.

## 3. Replacement proof

Fix a later extension $M^+$, an independent context $T$, and a protected live positive item $e\in T$. Keep its background fixed. Set
$$
C=V_f\cup\bigcup_{a\in(T\cap E)-e}S_a,\qquad
A=E\cap\operatorname{cl}_{M^+}(T-e).
$$
The set $A$ is an original-matroid flat excluding $e$. Therefore the original representation supplies a functional $L_A$ zero on $A$ and nonzero on $v_e$; no representation of $M^+$ is required.

The sets $S_e,C$ are disjoint, and $|C|\le p(K-1)+h_v$. Hence
$$
a_e\wedge\bigwedge_{x\in C}u_x\ne0.
$$
A coordinate functional of that exterior product defines $L_C$, nonzero on the protected item and zero on every packing conflict or failed-universe item.

Apply
$$
L_A\otimes L_C\otimes\bigotimes_j\ell_{F_j}
$$
to the greedy relation expressing $z_e$ through no-more-expensive retained columns. Its left side is nonzero, so a retained $f$ has all factors nonzero. It is outside the closure of $T-e$, avoids its packing conflicts and all failures, and costs at most $e$. It therefore replaces $e$, preserving background and positive cardinality.

Without a resource, private padding ensures that an already selected item conflicts with $C$. Thus the same argument avoids duplicates. Replacing omitted items one at a time terminates because every step reduces their number. This proves the theorem. $\square$

## 4. Matching and representation accounting

For graph matching, use endpoint sets and $p=2$. Individual edge IDs form a degree-one failure system. The no-resource bound is
$$
(h_e+1)\binom{2K+h_v}{2},
$$
capped by the edge count; multiply by $r$ when a represented resource is present. Whole risk-label systems contribute their separate binomial factors. Parallel edge IDs remain distinct.

The dimension gate precedes all feature enumeration. If $D\ge N$, return the original items. Otherwise the lift and $O(ND^2)$ Gaussian elimination are polynomial in the explicit input. Resource rank is not recomputed after a future context.

For rational arithmetic, a Vandermonde coordinate has degree at most $t-1$, so a $p$-minor requires
$$
O\bigl(pt\log(|U'|+2)+p\log(p+2)\bigr)
$$
bits, in addition to resource and label-feature terms. This ambient-degree factor is essential. The output size counts original IDs, separately from tensor and elimination workspace.

## Complete proof

[Resource-packing theorem, bit accounting, and representative-family sources](manuscripts/represented-resource-packing-transfer.md).

**Attribution:** Yilin Liu and GPT-6 Astra Pro.
