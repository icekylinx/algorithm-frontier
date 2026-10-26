# Proofs for exact correlated-failure quotient summaries

## 1. Model and theorem

Let each original item $e$ be a subspace $B_e$ given by explicit columns over a rational or finite field, with weight $w_e\ge0$. Let $A$ concatenate all columns and have rank $r$. Row $i$ carries labels $R_i$, while all columns of item $e$ carry labels $S_e$. Assume every nonzero incidence satisfies

$$
R_i\subseteq S_e,\qquad |S_e\setminus R_i|\le k.
$$

A failed label set $F$, of size at most $h$, deletes the entire item whenever $S_e\cap F\ne\varnothing$.

**Theorem 1.** With constant success probability, one randomized preprocessing algorithm returns nonnegative coefficients on

$$
O\!\left(\min\left\{m,
\frac{D\log(2D/\epsilon)}{\epsilon^2}\right\}\right),
\qquad D=r\binom{h+k}{k},
$$

original items, preserving

$$
\sum_{e:S_e\cap F=\varnothing}w_e\mathbf1[B_e\not\subseteq W]
$$

within $1\pm\epsilon$, simultaneously for every allowed $F$ and every linear subspace $W$. Construction is polynomial in explicit compact input length and $\epsilon^{-1}$.

## 2. Exact common-scalar decoding

**Proof.** Select $r$ independent original rows, with selector $P$, and write $A=C(PA)$. Keep their original row labels. Choose distinct field points $\alpha_0,\ldots,\alpha_L$, where label zero is a dummy that never fails; extend a finite field if needed. Define

$$
\ell_c(z)=\sum_{j=0}^h\alpha_c^jz_j,
\qquad
p_T(z)=\left(\prod_{c\in T}\ell_c(z)\right)\ell_0(z)^{k-|T|}.
$$

Homogeneous degree-$k$ polynomials in $h+1$ variables have coefficient dimension $\binom{h+k}{k}$. Lift selected-row entry $(PA)_{ie}$ to its product with the coefficient vector of $p_{S_e\setminus R_i}$. This defines a lifted vector for every original column and a lifted subspace $\widehat B_e$ for each item.

For a failure set $F$, write

$$
q_F(t)=\prod_{f\in F}\frac{t-\alpha_f}{\alpha_0-\alpha_f}
=\sum_{j=0}^h\theta_jt^j,
\qquad
\gamma_F(S)=\prod_{c\in S}q_F(\alpha_c).
$$

It has $q_F(\alpha_0)=1$ and vanishes precisely at failed label points. Evaluate each row's polynomial block at $\theta$ and multiply by $\gamma_F(R_i)$. This linear map $T_F$ satisfies, for every column $a_{e,j}$ and its lift $z_{e,j}$,

$$
CT_Fz_{e,j}=\gamma_F(S_e)a_{e,j}.
$$

The scalar is identical for every column of a whole item and is zero exactly when the item fails. For the lifted subspace $U=(CT_F)^{-1}(W)$, therefore,

$$
\widehat B_e\not\subseteq U
\quad\Longleftrightarrow\quad
S_e\cap F=\varnothing\text{ and }B_e\not\subseteq W.
\tag{1}
$$

This identity holds for every failure set and every subspace. Its decoder need not be constructed by preprocessing.

## 3. Quotient sparsification and the error ledger

On the original item identifiers, define the integer polymatroid

$$
f(T)=\dim\sum_{e\in T}\widehat B_e\le D.
$$

For any subspace $U$, the set $Z_U=\{e:\widehat B_e\subseteq U\}$ is closed: every block already spanned by these blocks remains inside $U$. Thus its complement is a quotient of $f$. Quanrud's theorem preserves every quotient with $O(D\log(2mD)/\eta^2)$ support.

The [adaptive quotient theorem](manuscripts/adaptive-quotient-resparsification.md) removes the ground-set logarithm. Its restriction step is exact: if $S$ is closed in the original rank and $T$ is retained, every $e\in T\setminus S$ has positive marginal already at $S$, and diminishing returns gives a positive marginal at $S\cap T$. Hence $S\cap T$ remains closed.

While current support $m_i$ exceeds a fixed polynomial in $D/\epsilon$, choose an error proportional to $\epsilon\sqrt{\log(2D/\epsilon)/\log m_i}$. The next support is at most $\sqrt{m_i}$. These preliminary errors sum geometrically, independently of the initial $m$. One final call at constant-times-$\epsilon$ error gives $O(D\log(2D/\epsilon)/\epsilon^2)$ support. Fixed inverse-power failure bounds per call also sum to a constant, read backward along the size sequence. The cited proof supplies explicit constants and the rational bit-length ledger.

Applying this one all-quotient event to (1) proves the simultaneous approximation. No union bound over failures is used, and coefficients never change at query time. $\square$

## 4. Uniform polynomial construction

The field points and polynomial coefficients have polynomial bit complexity. If $D\ge m$, retain the input before materializing any lifted vectors; binomial coefficients can be computed with that cap. In the remaining branch the feature dimension is below the input item count, and the original block-column count is part of the explicit input. Rank queries are therefore polynomial.

For a finite field of size $q_0<L+1$, choose the least extension degree $t$ with $q_0^t\ge L+1$. There are fewer than $q_0(L+1)\le(L+1)^2$ monic candidate polynomials of degree $t$, so deterministic enumeration with irreducibility testing has polynomial cost in the explicit label universe. Extension preserves original linear dependences and membership in original-field subspaces. Rational matrices instead use integer label points. Zero-rank and zero-weight items are handled directly.

## 5. Graph and whole-object consequences

For an oriented graph incidence matrix, the rank is $n-c$. An edge $uv$ has labels $R_u\cup R_v\cup T_e$. On an incident row $u$, at most $a+b$ labels are absent, giving $k=a+b$. A Boolean cut vector $x$ has $x^Ta_e\ne0$ exactly for crossing edges, so take $W=\ker(x^T)$. Theorem 1 gives the graph result.

A hyperedge of size at most $t$ is represented by the span of its pair differences, using a star basis. Its label deficit is at most $a(t-1)+b$, and its block leaves a cut kernel exactly when the hyperedge crosses. The decoder deletes the entire hyperedge when any incident vertex fails. For partitions, use the subspace spanned by within-part differences; a block lies in it precisely when the hyperedge lies within a single part. A hedge is the span of the differences of all its constituent hyperedges, with external item labels.

For globally commuting prime-dimensional stabilizer blocks, phase-aware elimination gives an affine block predicate on at most $n$ variables. Homogenize with one coordinate and apply Theorem 1 to its row space. Because every surviving Hamiltonian is diagonal in the same basis, simultaneous block-predicate preservation is exactly simultaneous Loewner preservation. Global commutation is used here; applying a single noncommuting pair split before arbitrary failures would not establish this conclusion.

## 6. Joint support lower bounds

For a cut sparsifier of $K_{s,B}$, let $W$ be its nonnegative weighted adjacency matrix and $E=W-\mathbf1$. Cut constraints imply

$$
|\sigma^TE\tau|\le3\epsilon sB
\quad\text{for all sign vectors }\sigma,\tau.
$$

Choose $\tau$ according to $E^T\sigma$ and average independent signs $\sigma$. Khintchine's inequality gives $\sum_j\|E_{\cdot j}\|_2\le3\sqrt2\epsilon sB$. If column $j$ uses $t_j$ edges, its singleton cut gives

$$
\|E_{\cdot j}\|_2\ge(1-\epsilon)s/\sqrt{t_j}-\sqrt s.
$$

Jensen's inequality yields

$$
\sum_jt_j\ge
\frac{(1-\epsilon)^2sB}{(1+3\sqrt2\epsilon\sqrt s)^2}.
$$

Take $s=\lceil\epsilon^{-2}\rceil$, and index disjoint left blocks by all $k$-subsets of an $(h+k)$-label universe. Give one block precisely its labels, split between vertex and edge labels as required. Failing the complementary $h$-set isolates that block, so each block separately needs $\Omega(B/\epsilon^2)$ retained edges. With a sufficiently large common right part, the total vertex count is $\Theta(B)$. This forces $\Omega(n\binom{h+k}{k}/\epsilon^2)$ support in the stated size regime.

The [hyperedge proof](manuscripts/exact-label-whole-blocks-and-hyperedges.md) uses core vertices and a rectangle-discrepancy version of the same inequality to realize $k=a(t-1)+b$. The same labeled-copy construction on commuting cut checks gives the quantum lower bound while sharing the same physical qudits.

**Attribution:** Yilin Liu and GPT-6 Astra Pro.
