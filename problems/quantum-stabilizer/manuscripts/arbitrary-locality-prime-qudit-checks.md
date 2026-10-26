# Arbitrary-locality prime-dimensional Weyl checks

**Abstract.** Positive eigenvalue-check Hamiltonians on prime-dimensional qudits admit whole-check spectral summaries independent of locality. The result is a direct corollary of the whole-block theorem. An independent projective-line averaging argument shows how an abelian Cayley sparsifier can retain whole check predicates. Compact construction and optimal support existence have distinct bounds.

## 1. Model and theorem

Let $p$ be prime, $\omega=e^{2\pi i/p}$, and let the Hilbert space be $(\mathbb C^p)^{\otimes n}$. A normalized Weyl operator has projective label in $\mathbb F_p^{2n}$, satisfies $U^p=I$, and any two such operators satisfy

$$
UV=\omega^{[u,v]}VU.
$$

Here $[u,v]$ is the standard symplectic form. For odd $p$, tensor products of the usual shift and clock operators, multiplied by a power of $\omega$, have this normalization. For $p=2$, use signed Hermitian Pauli strings; this includes the usual phase correction for $Y$.

An input check asks for the eigenvalue $\omega^{t_e}$ of a normalized Weyl operator $U_e$. Absorb the target into $V_e=\omega^{-t_e}U_e$, and define

$$
E_e=\Pi_{V_e,1}=\frac1p\sum_{j=0}^{p-1}V_e^j,
\qquad B_e=I-E_e,
\qquad H=\sum_{e=1}^m w_e B_e,
\quad w_e\ge0.
\tag{Q1}
$$

Thus $E_e$ is an orthogonal projection and $0\preceq B_e\preceq I$. Scalar Weyl operators are allowed: they give a zero check or the constant penalty $I$. Zero terms and zero weights may be discarded.

**Theorem Q.** For every $0<\epsilon<1$, there are nonnegative coefficients $c_e$, supported on

$$
O\!\left(\min\left\{m,\frac{(n+1)\log p}{\epsilon^2}\right\}\right)
\tag{Q2}
$$

original checks, such that

$$
(1-\epsilon)H\preceq\sum_e c_eB_e\preceq(1+\epsilon)H.
\tag{Q3}
$$

For rational input weights, a randomized algorithm using time polynomial in $n,m,\log p,\epsilon^{-1}$ and the weight encoding length constructs such an approximation, with success probability at least $2/3$, with the slightly larger support bound

$$
O\!\left(\min\left\{
m,\frac{n+1}{\epsilon^2}
\left[\log p+\log\!\left(\frac{n+2}{\epsilon}\right)\right]
\right\}\right).
\tag{Q4}
$$

The support in (Q4) has no dependence on the locality of a check or the dynamic range of the weights. The compact algorithm never constructs a $p^n$-dimensional matrix. Its constant-success contract is sufficient here; no unchanged-support arbitrary-confidence claim is made.

The inherited graph-cut lower bound gives $\Omega(n/\epsilon^2)$ necessary original checks when $0<\epsilon\le1/2$ and $n\ge2\lceil\epsilon^{-2}\rceil$. Thus for fixed prime $p$, the support in (Q2) is jointly sharp in $n,\epsilon$ in this regime. No matching lower bound for the displayed $\log p$ dependence is claimed.

## 2. Proof of Theorem Q

Regard every check as a block containing exactly one normalized Weyl generator. Its block penalty is exactly $B_e$, so it satisfies the input contract of [the prime-dimensional whole-block theorem](arbitrary-locality-stabilizer-block-sparsification.md), with no change in weights, physical dimension, locality, or item identities. The compact support bound (SB3) is exactly (Q4), and the whole-block support bound (SB4a) is exactly (Q2). Both outputs retain original checks. The whole-block theorem's two success events have total failure probability below $1/3$; its construction therefore proves the claimed compact randomized contract. $\square$

The argument can also be decomposed into three elementary steps. A conflicting pair of accepted-eigenvalue projectors obeys

$$
EFE=E/p,\qquad
 (I-E)+(I-F)\succeq(1-p^{-1/2})I.
 \tag{Q5}
$$

Indeed, every nonconstant power in the Fourier expansion of $F$ maps the accepted eigenspace of the other check to a distinct eigenspace. Balanced subtraction of equal coefficient mass from conflicting pairs then leaves one pairwise-commuting family. The removed positive part has a lower spectral bound equal to an absolute constant times its total coefficient, so coefficient-proportional sampling uses $O(n\log p/\epsilon^2)$ original checks at constant confidence. The commuting family is an affine linear-code objective on at most $n$ variables over $\mathbb F_p$. Its augmented row rank is at most $n+1$, and quotient resparsification uses $O((n+1)\log((n+2)/\epsilon)/\epsilon^2)$ coordinates. These two PSD approximations add without an additional relative-error factor.

For the lower bound, take one commuting check $I-\Pi_{Z_uZ_v^{-1},1}$ per edge of $K_{s,B}$, with $s=\lceil\epsilon^{-2}\rceil$ and $B=n-s\ge s$. On computational-basis symbols in $\{0,1\}$, its penalty is exactly the corresponding Boolean cut indicator. Equation (EC15) of [the cut theorem](../../label-block-cut/manuscripts/exact-label-cut-and-matroid-quotient-sparsification.md) requires $\Omega(n/\epsilon^2)$ original checks. This proves the stated fixed-prime joint lower bound; it does not establish necessity of the $\log p$ factor.

## 3. An independent support proof by projective-line averaging

Here is the additional argument needed to obtain (Q2) without replacing a check by independently weighted powers of its Weyl operator.

After the commuting reduction in [the whole-block theorem](arbitrary-locality-stabilizer-block-sparsification.md), let $r\le n$ be its projective rank and set $d=r+1$ and $G=\mathbb F_p^d$. First merge collinear nonzero rows $g_e$: multiplying a row by a nonzero scalar leaves its nonzero predicate unchanged. Let a projective line $\ell$ have total residual weight $v_\ell$. For every nonzero $s\in\ell$, give the Cayley generator $s$ weight $v_\ell/p$. This is a symmetric weighted generating set. At the character indexed by $y\in G$, the contribution of the line to its Laplacian eigenvalue is

$$
\frac{v_\ell}{p}\sum_{t\in\mathbb F_p^*}
\left(1-\omega^{t(g_\ell\cdot y)}\right)
=v_\ell\mathbf1[g_\ell\cdot y\ne0].
\tag{Q12}
$$

The weighted abelian Cayley theorem supplies a relative sparsifier with
$O(d\log p/\epsilon^2)$ generators. Let its nonnegative weights be $\rho_s$. It need not initially assign equal weights to generators on the same projective line.

For each $\alpha\in\mathbb F_p^*$, conjugate this sparsifier by the group automorphism $z\mapsto\alpha z$, then average all $p-1$ conjugates. The input Cayley Laplacian is invariant under every such automorphism, so averaging preserves the same relative Loewner inequalities. The averaged output assigns every nonzero generator on a line $\ell$ the common weight

$$
\frac1{p-1}\sum_{s\in\ell}\rho_s.
$$

Consequently it is exactly the code/check sparsifier with coefficient

$$
c_\ell=\frac{p}{p-1}\sum_{s\in\ell}\rho_s
\tag{Q13}
$$

on one representative original check of each retained line. The number of retained lines is at most the number of generators before averaging. All nonzero scalar multiples of $g_e$ describe the same operator on the physical affine slice, so selecting a representative original check is valid.

Thus the commuting part has an original-check sparsifier of size $O((r+1)\log p/\epsilon^2)$. The current Cayley construction takes time polynomial in $|G|=p^{r+1}$, rather than polynomial in $r,\log p$. This averaging argument is used for support existence and the exponential construction only.

## 4. References

1. **Khanna, Putterman, Sudan, STOC 2025, _Efficient Algorithms and New Characterizations for CSP Sparsification_.** Section 5 explicitly treats arbitrary weighted generating matrices. Theorem 5.19 and Claim 5.18 provide the earlier weighted-code backend; its two-pass final algorithm removes the original code-length logarithm. Primary source: <https://arxiv.org/html/2404.06327v2>.

2. **Basu, Kothari, Meka, Tudose, July 2026, _Optimal Sparsifiers for Abelian Cayley Graphs_.** Theorem 1.5 covers arbitrary weighted abelian Cayley graphs with $O(\epsilon^{-2}\log|G|)$ generators and a randomized algorithm polynomial in $|G|$. The projective-line averaging in Section 5 above is the transfer used here to preserve whole check terms. Primary source: <https://arxiv.org/pdf/2607.08261v1>.

3. **Basu, Brakensiek, Putterman, May 2026, _Many Hamiltonians Are Sparsifiable_.** Theorem 3.5 proves near-linear support for fixed-locality qubit Pauli penalties, with locality-dependent bounds and preprocessing; Theorem 2.11 explicitly records the weighted binary-code primitive. The present statement permits unbounded locality and prime-dimensional check projectors, with no locality factor. It is not a claim to improve their fixed-locality bound as a function of $n$. Primary source: <https://arxiv.org/html/2605.02211v1>.

4. **Hostens, Dehaene, De Moor, 2005, _Stabilizer states and Clifford operations for systems of arbitrary dimensions, and modular arithmetic_.** This supplies standard compact Weyl/stabilizer representation background. The pair-gap calculation, balanced decomposition, and projective-line averaging are proved directly above. Primary source: <https://arxiv.org/abs/quant-ph/0408190>.

5. **Tropp, _An Introduction to Matrix Concentration Inequalities_.** Matrix Chernoff is used only for the uniformly gapped peeled part. Primary source: <https://arxiv.org/abs/1501.01571>.

6. **Quanrud, SODA 2024, _Quotient sparsification for submodular functions_.** Theorem 1.1 and its linear-matroid application give the weighted subspace-complement primitive. Adaptive resparsification, proved in 27_adaptive_quotient_resparsification.md, removes the original ground-set logarithm and yields the explicit compact bound (Q4). Primary source: <https://kentq.s3.amazonaws.com/submodular-sparsification.pdf>.
