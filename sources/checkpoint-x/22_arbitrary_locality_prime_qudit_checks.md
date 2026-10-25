# Increment: sparsifying arbitrary-locality qudit stabilizer checks

## Status and scope

This is a rough mathematical extension of the anticommuting-pair decomposition for qubit Pauli Hamiltonians. It treats **individual generalized-Pauli eigenvalue checks** on prime-dimensional qudits, with arbitrary positive weights and arbitrary locality. The original check terms, rather than their individual Fourier components, are the objects retained and reweighted.

The main new ingredient is that two noncommuting check projectors have a uniformly bounded overlap. Balanced removal of their weights splits the entire Hamiltonian into a uniformly gapped part and a commuting part. The latter is a weighted affine linear-code instance over the prime field.

Two construction guarantees are kept separate:

* A randomized algorithm polynomial in the compact input size obtains explicit near-linear support using Quanrud's quotient theorem and adaptive resparsification. The earlier Khanna--Putterman--Sudan weighted-code backend is also credited below.
* An existential bound without the extra polylogarithms follows from the July 2026 optimal abelian Cayley theorem, together with an orbit-averaging argument that restores whole check terms. Its currently invoked construction is exponential in the number of qudits.

This is a statement about the penalties below. For \(p>2\), they are generally different from \(I-(U+U^*)/2\). No result for arbitrary positive semidefinite local terms is asserted.

## 1. Model and theorem

Let \(p\) be prime, \(\omega=e^{2\pi i/p}\), and let the Hilbert space be \((\mathbb C^p)^{\otimes n}\). A normalized Weyl operator has projective label in \(\mathbb F_p^{2n}\), satisfies \(U^p=I\), and any two such operators satisfy

\[
UV=\omega^{[u,v]}VU.
\]

Here \([u,v]\) is the standard symplectic form. For odd \(p\), tensor products of the usual shift and clock operators, multiplied by a power of \(\omega\), have this normalization. For \(p=2\), use signed Hermitian Pauli strings; this includes the usual phase correction for \(Y\).

An input check asks for the eigenvalue \(\omega^{t_e}\) of a normalized Weyl operator \(U_e\). Absorb the target into \(V_e=\omega^{-t_e}U_e\), and define

\[
E_e=\Pi_{V_e,1}=\frac1p\sum_{j=0}^{p-1}V_e^j,
\qquad B_e=I-E_e,
\qquad H=\sum_{e=1}^m w_e B_e,
\quad w_e\ge0.
\tag{Q1}
\]

Thus \(E_e\) is an orthogonal projection and \(0\preceq B_e\preceq I\). Scalar Weyl operators are allowed: they give a zero check or the constant penalty \(I\). Zero terms and zero weights may be discarded.

**Theorem Q.** For every \(0<\epsilon<1\), there are nonnegative coefficients \(c_e\), supported on

\[
O\!\left(\min\left\{m,\frac{(n+1)\log p}{\epsilon^2}\right\}\right)
\tag{Q2}
\]

original checks, such that

\[
(1-\epsilon)H\preceq\sum_e c_eB_e\preceq(1+\epsilon)H.
\tag{Q3}
\]

For rational input weights, a randomized algorithm using time polynomial in \(n,m,\log p,\epsilon^{-1}\) and the weight encoding length constructs such an approximation, with success probability at least \(2/3\), with the slightly larger support bound

\[
O\!\left(\min\left\{
m,\frac{n+1}{\epsilon^2}
\left[\log p+\log\!\left(\frac{n+2}{\epsilon}\right)\right]
\right\}\right).
\tag{Q4}
\]

The support in (Q4) has no dependence on the locality of a check or the dynamic range of the weights. The compact algorithm never constructs a \(p^n\)-dimensional matrix. Its constant-success contract is sufficient here; no unchanged-support arbitrary-confidence claim is made.

The inherited graph-cut lower bound gives \(\Omega(n/\epsilon^2)\) necessary original checks when \(0<\epsilon\le1/2\) and \(n\ge2\lceil\epsilon^{-2}\rceil\). Thus for fixed prime \(p\), the support in (Q2) is jointly sharp in \(n,\epsilon\) in this regime. No matching lower bound for the displayed \(\log p\) dependence is claimed.

## 2. Noncommuting checks have a constant pair gap

**Lemma Q1.** If \(UV=\omega^aVU\) with \(a\ne0\) in \(\mathbb F_p\), and \(E=\Pi_{U,1},F=\Pi_{V,1}\), then

\[
EFE=\frac1pE,
\qquad \|EF\|=p^{-1/2},
\qquad (I-E)+(I-F)\succeq(1-p^{-1/2})I.
\tag{Q5}
\]

**Proof.** For \(1\le j\le p-1\), the vector \(V^jz\), for \(z\) in the \(1\)-eigenspace of \(U\), belongs to its \(\omega^{aj}\)-eigenspace. Primality gives \(\omega^{aj}\ne1\), so \(EV^jE=0\). Expanding \(F\) proves \(EFE=E/p\). The operators here are non-scalar Weyl operators, so \(E\ne0\), and the projection identity gives \(\|EF\|^2=\|EFE\|=1/p\).

For any two orthogonal projections, \(E+F\preceq(1+\|EF\|)I\). One proof applies the estimate
\(\|Ex+Fy\|^2\le(1+\|EF\|)(\|x\|^2+\|y\|^2)\)
to the operator \([E\ F]\). Subtract from \(2I\). \(\square\)

## 3. Balanced peeling and elementary sampling

Initialize residual weights \(r_e=w_e\) and peeled weights \(b_e=0\). While two positive residual checks \(i,j\) have noncommuting Weyl labels, set

\[
d=\min(r_i,r_j),\qquad
(r_i,r_j)\leftarrow(r_i-d,r_j-d),\qquad
(b_i,b_j)\leftarrow(b_i+d,b_j+d).
\tag{Q6}
\]

Each step removes at least one positive residual weight. Hence there are at most \(m\) steps, found using symplectic inner products in \(\mathbb F_p^{2n}\). The remaining positive-weight Weyl operators commute pairwise. Write

\[
H=H_{\rm com}+H_{\rm gap},\qquad
H_{\rm com}=\sum_e r_eB_e,\qquad
H_{\rm gap}=\sum_e b_eB_e,
\qquad W=\sum_e b_e.
\]

Summing (Q5) over all balanced pairs yields

\[
H_{\rm gap}\succeq\beta_p W I,
\qquad \beta_p=\frac{1-p^{-1/2}}2
\ge\frac{1-2^{-1/2}}2>0.
\tag{Q7}
\]

If \(W=0\), omit this part. Otherwise sample \(k\) independent original checks with probabilities \(b_e/W\), assigning coefficient \(W/k\) to each draw and adding coefficients of repeated draws. The estimator is unbiased and its total coefficient is exactly \(W\).

For analysis only, whiten by \(H_{\rm gap}^{-1/2}\). Each sampled summand has norm at most \(1/(\beta_pk)\), and the expected sum is the identity on dimension \(p^n\). Matrix Chernoff gives a relative \(1\pm\epsilon\) approximation with failure at most \(\delta\) for

\[
k=O\!\left(\frac{n\log p+\log(1/\delta)}{\epsilon^2}\right).
\tag{Q8}
\]

Whitening, eigenvectors, and quantum states are absent from the algorithm. Taking \(\delta=1/10\) suffices for both the existence statement and the compact theorem after combining the two components' success events.

## 4. The commuting part is a weighted affine code

Select original commuting Weyl operators \(Q_1,\ldots,Q_r\) whose projective labels are a basis for the remaining labels. Their span is isotropic in \(\mathbb F_p^{2n}\), so \(r\le n\). Finite-field elimination, with scalar phases tracked, expresses every residual check as

\[
V_e=\omega^{s_e}\prod_{j=1}^r Q_j^{a_{ej}}.
\tag{Q9}
\]

There is no scalar ambiguity beyond a power of \(\omega\): both sides have \(p\)-th power \(I\). For a simultaneous eigenvalue assignment \(Q_j=\omega^{x_j}\), the penalty is exactly

\[
B_e(x)=\mathbf1[a_e\cdot x+s_e\ne0].
\tag{Q10}
\]

Every \(x\in\mathbb F_p^r\) occurs. Indeed, expansion of its joint eigenspace projection has trace \(p^{n-r}\), since every nontrivial product of the projectively independent \(Q_j\)'s is a traceless non-scalar Weyl operator. Only simultaneous diagonalization and the evaluation formula are needed for the transfer.

Homogenize with one coordinate: \(g_e=(a_e,s_e)\in\mathbb F_p^{r+1}\). On \(y=(x,1)\), (Q10) is \(\mathbf1[g_e\cdot y\ne0]\). A weighted sparsifier for the linear code

\[
\{(g_e\cdot y)_e:y\in\mathbb F_p^{r+1}\}
\tag{Q11}
\]

therefore approximates \(H_{\rm com}\) in Loewner order.

For the improved compact bound, use the linear-matroid rank function
\[
f(T)=\dim_{\mathbb F_p}\operatorname{span}\{g_e:e\in T\}.
\]
For every \(y\), the zero set \(\{e:g_e\cdot y=0\}\) is closed, because its span remains in \(y^\perp\). Its complement is therefore a quotient. Quanrud's Theorem 1.1, followed by the adaptive resparsification argument in 27_adaptive_quotient_resparsification.md, gives one nonnegative reweighting of
\[
O\!\left(
\frac{(r+1)\log(2(r+1)/\epsilon)}{\epsilon^2}
\right)
\]
original coordinates preserving all the queries (Q11). The entire classical procedure can have success probability above \(9/10\). Its computation uses finite-field rank queries and rational scalar weights; the companion gives the accumulated error, confidence, and polynomial-bit ledger.

The earlier KPS weighted-code backend also applies, giving
\(\widetilde O((r+1)\log^2p/\epsilon^2)\) coordinates in compact randomized polynomial time. The quotient formulation above supplies the sharper explicit bound used in (Q4). Neither compact route expands a check into its \(p-1\) Fourier components.

Scalar constant penalties have \(a_e=0,s_e\ne0\) and are covered by the extra coordinate. Zero penalties have \(g_e=0\) and may be removed. For \(p=2\), this is precisely the affine XOR reduction.

## 5. Optimal abelian Cayley support can retain whole checks

Here is the additional argument needed to obtain (Q2) without replacing a check by independently weighted powers of its Weyl operator.

Set \(d=r+1\) and \(G=\mathbb F_p^d\). First merge collinear nonzero rows \(g_e\): multiplying a row by a nonzero scalar leaves its nonzero predicate unchanged. Let a projective line \(\ell\) have total residual weight \(v_\ell\). For every nonzero \(s\in\ell\), give the Cayley generator \(s\) weight \(v_\ell/p\). This is a symmetric weighted generating set. At the character indexed by \(y\in G\), the contribution of the line to its Laplacian eigenvalue is

\[
\frac{v_\ell}{p}\sum_{t\in\mathbb F_p^*}
\left(1-\omega^{t(g_\ell\cdot y)}\right)
=v_\ell\mathbf1[g_\ell\cdot y\ne0].
\tag{Q12}
\]

The weighted abelian Cayley theorem supplies a relative sparsifier with
\(O(d\log p/\epsilon^2)\) generators. Let its nonnegative weights be \(\rho_s\). It need not initially assign equal weights to generators on the same projective line.

For each \(\alpha\in\mathbb F_p^*\), conjugate this sparsifier by the group automorphism \(z\mapsto\alpha z\), then average all \(p-1\) conjugates. The input Cayley Laplacian is invariant under every such automorphism, so averaging preserves the same relative Loewner inequalities. The averaged output assigns every nonzero generator on a line \(\ell\) the common weight

\[
\frac1{p-1}\sum_{s\in\ell}\rho_s.
\]

Consequently it is exactly the code/check sparsifier with coefficient

\[
c_\ell=\frac{p}{p-1}\sum_{s\in\ell}\rho_s
\tag{Q13}
\]

on one representative original check of each retained line. The number of retained lines is at most the number of generators before averaging. All nonzero scalar multiples of \(g_e\) describe the same operator on the physical affine slice, so selecting a representative original check is valid.

Thus the commuting part has an original-check sparsifier of size \(O((r+1)\log p/\epsilon^2)\). The current Cayley construction takes time polynomial in \(|G|=p^{r+1}\), rather than polynomial in \(r,\log p\). This averaging argument is used for support existence and the exponential construction only.

## 6. Combining the parts, edge cases, and lower bound

Use accuracy \(\epsilon\) for both PSD parts. Their two relative inequalities add directly to (Q3). If an original check was split between both parts, add its two output coefficients. This is still one nonnegative coefficient on the original term. No term decomposition survives in the output. Taking the smaller of the constructed summary and the original instance gives the displayed minimum with \(m\).

For (Q4), the commuting contribution is \(O((n+1)\log((n+2)/\epsilon)/\epsilon^2)\), while (Q8) contributes \(O((n\log p+1)/\epsilon^2)\). Their sum is the claimed bound. A union bound over the classical procedure and the gapped sample, each with failure at most \(1/10\), gives success probability greater than \(2/3\).

All preprocessing uses finite-field arithmetic, scalar phase arithmetic, and rational weight operations. The balanced subtraction sequence has at most \(m\) steps; rational encoding lengths grow by at most a polynomial in the total input length. The quoted compact running time includes that length and the code backend's dependence on \(\epsilon^{-1}\). The quantum dimension appears only inside the logarithm in the sampling proof.

For necessity of linear support at fixed \(p\), take the \(n\) commuting checks that demand eigenvalue \(1\) for \(Z_i\) on each separate qudit. The computational basis state with its only nonzero coordinate at position \(i\) violates exactly check \(i\). Omitting it makes the sparsifier's energy zero on this state and the input energy positive. Thus all \(n\) original checks are required whenever \(\epsilon<1\).

The stronger joint bound is inherited directly from cut sparsification. Let \(s=\lceil\epsilon^{-2}\rceil\), \(B=n-s\ge s\), and use the two-local commuting check \(I-\Pi_{Z_uZ_v^{-1},1}\) for each edge \(uv\) of \(K_{s,B}\), with unit input weights. Restrict computational basis symbols to \(\{0,1\}\subseteq\mathbb F_p\). The check penalty is then exactly the Boolean cut indicator of \(uv\). Every spectral check sparsifier therefore gives a cut sparsifier of \(K_{s,B}\). The direct cut calculation in Section 6 of 28_exact_label_cut_and_matroid_quotient_sparsification.md, equation (EC15), forces \(\Omega(B/\epsilon^2)=\Omega(n/\epsilon^2)\) retained edges/checks for \(0<\epsilon\le1/2\). This is an application of a classical cut lower bound, not a separate quantum lower-bound priority claim.

## 7. Public inputs and comparison

1. **Khanna, Putterman, Sudan, STOC 2025, _Efficient Algorithms and New Characterizations for CSP Sparsification_.** Section 5 explicitly treats arbitrary weighted generating matrices. Theorem 5.19 and Claim 5.18 provide the earlier weighted-code backend; its two-pass final algorithm removes the original code-length logarithm. Primary source: <https://arxiv.org/html/2404.06327v2>.

2. **Basu, Kothari, Meka, Tudose, July 2026, _Optimal Sparsifiers for Abelian Cayley Graphs_.** Theorem 1.5 covers arbitrary weighted abelian Cayley graphs with \(O(\epsilon^{-2}\log|G|)\) generators and a randomized algorithm polynomial in \(|G|\). The projective-line averaging in Section 5 above is the transfer used here to preserve whole check terms. Primary source: <https://arxiv.org/pdf/2607.08261v1>.

3. **Basu, Brakensiek, Putterman, May 2026, _Many Hamiltonians Are Sparsifiable_.** Theorem 3.5 proves near-linear support for fixed-locality qubit Pauli penalties, with locality-dependent bounds and preprocessing; Theorem 2.11 explicitly records the weighted binary-code primitive. The present statement permits unbounded locality and prime-dimensional check projectors, with no locality factor. It is not a claim to improve their fixed-locality bound as a function of \(n\). Primary source: <https://arxiv.org/html/2605.02211v1>.

4. **Hostens, Dehaene, De Moor, 2005, _Stabilizer states and Clifford operations for systems of arbitrary dimensions, and modular arithmetic_.** This supplies standard compact Weyl/stabilizer representation background. The pair-gap calculation, balanced decomposition, and projective-line averaging are proved directly above. Primary source: <https://arxiv.org/abs/quant-ph/0408190>.

5. **Tropp, _An Introduction to Matrix Concentration Inequalities_.** Matrix Chernoff is used only for the uniformly gapped peeled part. Primary source: <https://arxiv.org/abs/1501.01571>.

6. **Quanrud, SODA 2024, _Quotient sparsification for submodular functions_.** Theorem 1.1 and its linear-matroid application give the weighted subspace-complement primitive. Adaptive resparsification, proved in 27_adaptive_quotient_resparsification.md, removes the original ground-set logarithm and yields the explicit compact bound (Q4). Primary source: <https://kentq.s3.amazonaws.com/submodular-sparsification.pdf>.

The primary-source check located the fixed-locality qubit theorem and the classical sparsification inputs, but no matching arbitrary-locality prime-qudit check theorem. That is a limited comparison of the checked sources, not a completed priority claim.
