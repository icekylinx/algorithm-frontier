# Exact membership and conditional-sign proofs

## 1. Exact compact-code membership

For homogeneous binary checks $`b_e(y)=\mathbf1[a_e\cdot y\ne0]`$, positive rational weights $`w_e`$, and $`a=1/4`$, define

```math
Q_a=\left\{z\in[-1,1]^m:
\left|\sum_ew_ez_eb_e(y)\right|\le a\sum_ew_eb_e(y)
\text{ for every }y\right\}.
```

**Theorem 1.** Deciding membership in $`Q_{1/4}`$ is coNP-complete even when every check has arity at most two and the supplied vector is in $`\{0,1/2\}^m`$.

**Proof.** Start with a weighted Max-Cut instance with nonnegative integer edge weights $`\lambda_{uv}`$, threshold $`K`$, and maximum weighted degree $`M>0`$. On binary variables $`x_1,\ldots,x_n,t`$, put

```math
F(x,t)=\sum_{uv}\lambda_{uv}(x_u\oplus x_v)
-\frac M2\sum_v\bigl(x_v+(x_v\oplus t)\bigr)
+\left(\frac{Mn}{2}-K\right)t.
```

For $`t=0`$, $`F(x,0)=\mathrm{cut}(x)-M|\{v:x_v=1\}|\le0`$. For $`t=1`$, it equals $`\mathrm{cut}(x)-K`$. Therefore $`F\le0`$ on every assignment if and only if the maximum cut is at most $`K`$.

Write the displayed signed sum as $`\sum_ec_eb_e`$, retain separate item identities, and omit zero coefficients. Set $`w_e=4|c_e|`$ and $`z_e=(1+\mathrm{sign}c_e)/4`$. Then

```math
\sum_ew_e(z_e-1/4)b_e(y)=F(y).
```

Thus the upper inequality defining $`Q_{1/4}`$ is exactly $`F(y)\le0`$; the lower inequality is automatic because $`z_e,w_e,b_e`$ are nonnegative. All checks have arity at most two, all data have polynomial bit length, and $`z_e\in\{0,1/2\}`$. This proves coNP-hardness. Nonmembership has a polynomially checkable violating assignment or cube coordinate, proving membership in coNP. $`\square`$

The [complete reduction](manuscripts/exact-separation-for-compact-codes.md) identifies the classical Max-Cut source. This theorem concerns exact membership/separation for this body. It is compatible with efficient graph sparsification methods that do not solve that oracle problem.

## 2. Exact non-Fano probability

Let

```math
A=\begin{pmatrix}
1&0&0&1&1&0&1\\
0&1&0&1&0&1&1\\
0&0&1&0&1&1&1
\end{pmatrix}\in\mathbb F_3^{3\times7},
\qquad a=(6,5,3,5,5,5,6).
```

**Theorem 2.** For independent uniform signs $`\sigma_e`$,

```math
\Pr\left[\sum_ea_e\sigma_e\mathbf1[(xA)_e\ne0]\le0
\text{ for all }x\in\mathbb F_3^3\right]
=15/128<2^{-3}.
```

**Proof.** The first three columns show that the rank is three. The 26 nonzero row-space queries give thirteen distinct nonempty supports. They are listed with exact total amplitudes in [the source proof](manuscripts/non-fano-obstruction-to-fixed-amplitude-bound.md).

For a positive-sign set $`P`$, a query support $`Q`$ is accepted exactly when $`2\sum_{e\in P\cap Q}a_e\le\sum_{e\in Q}a_e`$. The empty set, seven singleton sets, six pairs $`\{3,i\}`$ with $`i\ne3`$, and the pair $`\{2,6\}`$ satisfy every inequality. Every other pair has an explicitly listed violating query. Positivity makes every superset of an invalid pair invalid. The graph of valid pairs is a star centered at 3 plus edge $`26`$; its only triangle is $`236`$. That triangle violates query support $`12367`$, with positive weight 13 and total weight 25. No larger clique exists. These observations exclude every other positive-sign set, leaving exactly fifteen out of 128. $`\square`$

A direct sum of $`k`$ copies has rank $`3k`$. Its complete sign event is the intersection of the $`k`$ independent copy events: restricting queries to one block proves necessity, and summing the nonpositive block inequalities proves sufficiency. Its probability is therefore exactly $`(15/128)^k`$.

This disproves the exact fixed-amplitude lower bound $`2^{-r}`$. It does not disprove a lower bound with a different exponential constant or a Gaussian bound in which the amplitudes themselves are random.

**Attribution:** Yilin Liu and GPT-6 Astra Pro.
