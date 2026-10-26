# Proofs for finite-group, affine, and metric sparsification

This manuscript records the theorem composition used by the family. Full analytic and arithmetic arguments are linked at the lemma that supplies them. The retained objects are always original items, with one nonnegative coefficient each.

## 1. Arbitrarily weighted Cayley generators

**Theorem 1.** For a finite group of order $N\ge2$, every nonnegative weighted sum of regular-representation generator Laplacians has a $(1\pm\epsilon)$ spectral approximation on $O(\epsilon^{-2}\log^3(2N))$ original generator items. A deterministic construction has polynomial bit complexity in the explicit rational permutation-matrix input and $\epsilon^{-1}$.

**Proof.** Write $L_g=(I-U_g)^*(I-U_g)/2$ and $q=\lceil\log_2N\rceil$. In any $q+1$ selected items, order their positive weights increasingly. Two of the $2^{q+1}$ ordered subset products coincide. Cancel their common prefix and take their first differing index $i$. The resulting word expresses $g_i$ using later, at least as heavy, generators; its length is at most $2q$, and each later generator appears at most twice. For unitary matrices,

$$
\|(V_1\cdots V_\ell-I)x\|^2
\le\ell\sum_{j=1}^{\ell}\|(V_j-I)x\|^2.
$$

Hence the weighted item $A_i$ satisfies $A_i\preceq4q\sum_{j\ne i}A_j$. This conclusion holds under every positive rescaling and every restriction.

For completeness, if a PSD family has the property that every positively rescaled subfamily of size at least $k$ contains an $\alpha$-dominated item, its total operator importance is at most $4(k-1)/\alpha$. To prove this, whiten the total matrix so that $\sum_iC_i=I$, put $\tau_i=\|C_i\|$, and set $D_i=C_i/\tau_i$. Choose a unit vector $x_i$ with $x_i^*D_ix_i=1$. Independently include $i$ with probability $\alpha\tau_i/2$. Conditional on inclusion, the expected competing quadratic mass at $x_i$ is at most $\alpha/2$. With probability at least $1/2$, it is strictly less than $\alpha$. In every outcome the set of such good items has size at most $k-1$, since none is dominated by the others. Taking expectations gives the importance bound.

Use $k=q+1$, $\alpha=1/(4q)$, obtaining total importance at most $16q^2$. Matrix Chernoff sampling then needs $O(q^2\log(2N)/\epsilon^2)$ items. The two-sided trace-exponential estimator derandomizes the experiment. Rational upper estimates of the importance scores and a fixed estimator slack suffice; the complete polynomial-bit argument and the explicit estimator are in [Sections 3–5 of the Cayley manuscript](manuscripts/arbitrary-group-cayley-sparsification.md). The zero-range case is trivial, and all other calculations take place on the range of the PSD sum. $\square$

The same importance proof in an action of dimension $d$ replaces the final concentration logarithm by $\log(2d)$. The regular representation also intertwines with every unitary representation, so its weights give a simultaneous representation-independent output. This does not turn an arbitrary implicitly supplied unitary action into a rational-input computational model.

## 2. Whole subgroups and arbitrary cosets

**Lemma 2 (Gaussian-section sparsification).** Suppose nonnegative functions $b_e$ on a finite query set satisfy, after every item restriction and every positive reweighting,

$$
\Pr_{\xi\sim N(0,I)}
\left[\sum_e w_e\xi_eb_e(x)\le0\text{ for all }x\right]\ge p.
$$

Then one nonnegative reweighting on $O(\log(2/p)/\epsilon^2)$ original functions preserves their weighted sum for every query.

**Proof.** The [Gaussian hereditary-section lemma](manuscripts/optimal-whole-subgroup-constraints.md), Lemma 3, gives constant-exponential volume for the symmetric relative-error body when the current item count is at least $C\log(2/p)/a^2$. The Reis–Rothvoss large-volume theorem produces a partial coloring in a fixed dilation of this body. Choose its sign to remove at least one quarter of the items and update each weight to $w_e(1+z_e)$. At current support size $m_t$, take $a_t=\sqrt{C\log(2/p)/m_t}$. Because support decreases geometrically, the errors sum to at most a constant times $\sqrt{\log(2/p)/M}$ before the stopping threshold $M$. Set $M=C'\log(2/p)/\epsilon^2$ and choose the constant so this sum is at most $\epsilon/4$. Multiplying the one-stage bounds proves the claim. The internal Gaussian lemma supplies the complete section, midpoint-reflection, and correlation proof; the external partial-coloring theorem is explicitly identified there. $\square$

**Theorem 3.** Weighted complements of arbitrary subgroups or cosets of a finite group $G$ admit support $O(\log(2|G|)/\epsilon^2)$. The same coefficients preserve every original query.

**Proof for subgroups.** For subgroups $H_e$, let $b_e(g)=\mathbf1[g\notin H_e]$. Independently assign a standard Gaussian $T_{e,C}$ to every left coset and put

$$
F_g=2^{-1/2}\sum_e w_eT_{e,gH_e},\qquad
Y_g=F_1-F_g,\qquad Z_g=\sum_e w_e\xi_eb_e(g).
$$

Left translation preserves the law of $F$; hence the identity is a global minimum with probability at least $1/|G|$. The coordinates of $Y$ and $Z$ have equal variances. For each item their off-diagonal covariance contribution is zero if either query belongs to $H_e$, and otherwise is $w_e^2(1+\mathbf1[gH_e=hH_e])/2$ for $Y$, at most the contribution $w_e^2$ for $Z$. Slepian comparison at threshold zero gives the event in Lemma 2 with $p=1/|G|$. Restriction and reweighting do not affect the argument. Lemma 2 proves the support bound. The number of distinct coset tuples is $[G:\bigcap_eH_e]$, giving the sharper parameter. $\square$

**Proof for cosets.** For $C=aH$, work in the common group $\widetilde G=(G\times G)\rtimes C_2$. Let $\tau$ swap the factors and define

$$
K_C=((aHa^{-1})\times H)\rtimes\langle(a,a^{-1})\tau\rangle.
$$

The displayed involution normalizes the product subgroup, so this is a subgroup. Its odd elements are $(ah_1,h_2a^{-1})\tau$, with $h_1,h_2\in H$. Consequently

$$
(g,g^{-1})\tau\in K_C\quad\Longleftrightarrow\quad g\in aH.
$$

Apply the subgroup theorem in $\widetilde G$, whose order is $2|G|^2$, and restrict to these embedded queries. The support remains $O(\log(2|G|)/\epsilon^2)$. Empty accepting sets are constant penalties and can be combined into one original item. No common accepting query, normality, or commutativity is needed. $\square$

[The affine manuscript](manuscripts/affine-constraints-over-arbitrary-finite-groups.md) proves the exact-total-weight variant, group-derived Mal'tsev characterization, group-code corollary, and the joint graph-cut lower bound.

## 3. Hilbert metric sums

**Theorem 4.** If one transitive action on an $N$-point space preserves each Hilbertian pseudometric $d_e$ individually, their weighted sum has a whole-item relative-error sparsifier of size $O(\log(2N)/\epsilon^2)$.

**Proof.** Center an embedding of each item to obtain vectors $u_e(x)$. Its Gram matrix is determined by the squared distances and is invariant under the action. Thus $F_x=\sum_e w_e\langle T_e,u_e(x)\rangle$, for independent standard Gaussian vectors $T_e$, is stationary. For an anchor $o$, the event $F_o\le F_x$ for all $x$ has probability at least $1/N$. Put $Y_x=F_o-F_x$ and $Z_x=\sum_e w_e\xi_ed_e(o,x)$. Variances coincide, and Cauchy–Schwarz gives $\operatorname{Cov}(Y_x,Y_y)\le\operatorname{Cov}(Z_x,Z_y)$. Slepian comparison proves Lemma 2's hereditary hypothesis with $p=1/N$. The resulting weights preserve every anchor distance. Any pair can be translated to an anchor pair without changing any individual metric, proving all-pairs preservation. $\square$

For two-anchor losses $\|u_e-\rho_e(g)v_e\|$, the swap representation on $V_e\oplus V_e$ sends the vector $(u_e,v_e)/\sqrt2$ through $(g,g^{-1})\tau$ by exactly that orbit distance. This gives the finite-group alignment corollary. If there are $k$ action orbits, transitive ordered tuples with one point from each orbit have size $k!\prod_jN_j$; direct-sum Euclidean embeddings encode every original pair up to the same scalar for every item. These arguments and the Bernstein-transform closure are proved in [the transitive](manuscripts/transitive-metrics-and-group-alignment.md) and [few-orbit](manuscripts/hilbert-metric-sums-with-few-orbits.md) manuscripts.

## 4. Affine modular blocks and exact rational rank access

**Theorem 5.** Let $H$ be the subgroup generated by all augmented block rows over $\mathbb Z_q$, and let $r=\log_2|H|>0$. Whole affine blocks admit support $O(r/\epsilon^2)$ existentially and $O(r\log(2r/\epsilon)/\epsilon^2)$ by a factorization-free compact randomized algorithm.

**Proof.** A block's row subgroup $J_e\le H$ annihilates exactly a subgroup of $\widehat H$. Every augmented query $(x,1)$ defines a character, so Theorem 3 on $\widehat H$ proves the existential bound.

For construction, define $f(S)=\log_2|\sum_{e\in S}J_e|$. The finite-abelian subgroup order identity proves submodularity, and every positive marginal is at least one. The blocks annihilating any query form a closed set. Integer Hermite normal form computes the subgroup orders exactly without factoring $q$.

Choose an integer $R\in[r,r+1]$ and transform by $\phi(t)=t-t^2/(4R)$. Use identical rounded values for identical integer-order keys, with error at most $1/(64R)$, then multiply by four. A nonzero nested rank increase changes $\phi$ by at least $1/2$. In a submodularity comparison with both increments positive, the transformed slack is at least $1/(2R)$; four rounding errors cost at most $1/(16R)$. If an increment is zero, equality of the corresponding nested orders makes the rounded terms cancel exactly. The result is an exact rational monotone submodular rank with the same closures, positive marginals at least one, total value at most $4R$, and one denominator $O(R)$.

Quanrud's theorem and adaptive quotient resparsification now apply to an exact polynomial-bit oracle. They preserve every original active-block query with the claimed support. The same function and denominator are retained under every restriction. Full rounding, bit-length, and lower-bound proofs appear in [the rational-rank theorem](manuscripts/rational-quotient-ranks-from-weak-oracles.md) and [the modular-block theorem](manuscripts/affine-modular-blocks-and-sharp-modulus-dependence.md). $\square$

**Attribution:** Yilin Liu and GPT-6 Astra Pro.
