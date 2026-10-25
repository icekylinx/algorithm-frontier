# Increment: arbitrary-dimensional Weyl eigenvalue checks

*Rough mathematical draft, 25 October 2026. This extends the prime-qudit check result to every integer local dimension, including even and composite dimensions. Its additional ingredients are a commutator-order projector bound and an explicit Hermite-normal-form encoding of a commuting family. The latter deliberately includes more eigenvalue patterns than occur physically; this avoids assuming that a module over a composite modulus has a field basis. The compact algorithm uses a published classical code backend. A later increment in Section 5.1 invokes the companion Gaussian subgroup theorem to improve support existence by one logarithm in the modulus, while keeping the two algorithmic guarantees separate.*

**Later, stronger whole-block increment.** The companion `34_arbitrary_dimension_whole_stabilizer_blocks.md` subsumes the input model here and permits arbitrary joint stabilizer blocks and heterogeneous local dimensions. Writing \(D=q^n\) in the present uniform-dimensional model, it gives a factorization-free compact construction with \(O(\log(2D)\log(\log(2D)/\epsilon)/\epsilon^2)\) whole original blocks, optimal \(O(\log(2D)/\epsilon^2)\) support existence, and a matching joint worst-case lower bound along \(q=2^k\). The earlier code-based bound (C4) below remains an explicitly credited alternative construction; it has not been silently replaced inside Theorem C.

## 1. Statement and compact input model

Let \(q\ge2\) be an arbitrary integer, let \(Q=2q\), and set

\[
 \omega=e^{2\pi i/q},\qquad \tau=e^{2\pi i/Q}.
\]

On one \(q\)-dimensional register define \(X|z\rangle=|z+1\rangle\) and \(Z|z\rangle=\omega^z|z\rangle\), with arithmetic modulo \(q\). On \(n\) registers an input Weyl operator is specified compactly by

\[
 U_e=\tau^{c_e}X^{a_e}Z^{b_e},\qquad
 a_e,b_e\in\mathbb Z_q^n,\quad c_e\in\mathbb Z_Q.
\tag{C1}
\]

The vectors in (C1) describe tensor products. The target eigenvalue of a check can be absorbed into its scalar phase whenever the target is a \(Q\)-th root of unity. Every operator in (C1) satisfies \(U_e^Q=I\), including when \(q\) is even. Define

\[
 P_e=\Pi_{U_e,1}=\frac1Q\sum_{j=0}^{Q-1}U_e^j,
 \qquad B_e=I-P_e,\qquad
 H=\sum_{e=1}^m w_e B_e,
\tag{C2}
\]

where the weights are arbitrary nonnegative rationals. The projector in (C2) is allowed to be zero, in which case the check is the constant penalty \(I\). The identity operator gives a zero penalty. Thus no promise that each requested eigenspace is nonempty is necessary.

**Theorem C.** There is a randomized algorithm, polynomial in \(n,m,\log q,\epsilon^{-1}\) and the rational input encoding length, which returns nonnegative coefficients \(\widehat w_e\) on original checks such that, with the success guarantee of the weighted-code backend cited below,

\[
 (1-\epsilon)H\preceq\sum_e\widehat w_e B_e
 \preceq(1+\epsilon)H,
\tag{C3}
\]

and the number of nonzero coefficients is

\[
 \widetilde O\!\left(\min\left\{m,
        \frac{(n+1)\log^2(2q)}{\epsilon^2}\right\}\right).
\tag{C4}
\]

The hidden logarithms depend on \(n+2,\log q+2,\epsilon^{-1}+2\); there is no locality factor or weight-range factor in the support bound. No \(q^n\)-dimensional matrix is formed. No factorization of \(q\) is required. The algorithm retains and reweights whole original checks, even if one check has order strictly smaller than \(Q\).

The invoked KPS algorithm has its stated high-probability contract. An arbitrary external failure parameter is not silently available at unchanged support: the elementary sampling part below allows any failure probability, while the code part inherits the published backend's guarantee. At fixed \(q\) and fixed accuracy, the support has optimal exponent one in \(n\); the \(n\) individual checks \(Z_i=1\) give the usual linear lower bound. No sharp dependence on \(q\) is asserted.

**Theorem C' (improved support existence).** For the same arbitrary composite-dimensional input, there exists an output satisfying (C3) with
\[
 O\!\left(\min\left\{m,
       \frac{(n+1)\log(2q)}{\epsilon^2}\right\}\right)
 \tag{C4'}
\]
original checks. This uses the companion whole-subgroup sparsification theorem, proved by Gaussian comparison and Gaussian symmetrization. It is not the support bound of the compact polynomial-time algorithm above. Enumerating the classical query table gives a randomized construction in \(q^{O(n)}\) times a polynomial in the remaining encoding and accuracy parameters; no compact polynomial-time implementation of (C4') is claimed.

## 2. A projector overlap bound without a prime assumption

The following lemma applies more generally to any finite-order projectively commuting unitaries.

**Lemma C1.** Suppose \(U^Q=V^Q=I\) and \(UV=\zeta VU\), where the scalar \(\zeta\ne1\) has order \(t\mid Q\). Let \(P=\Pi_{U,1}\) and \(R=\Pi_{V,1}\). Then

\[
 PRP=\frac1t P\Pi_{V^t,1}P\preceq\frac1tP,
 \qquad \|PR\|\le t^{-1/2}\le2^{-1/2},
\tag{C5}
\]

and consequently

\[
 (I-P)+(I-R)\succeq(1-2^{-1/2})I.
\tag{C6}
\]

**Proof.** For a vector \(z\) in the \(1\)-eigenspace of \(U\), the vector \(V^jz\) belongs to the \(\zeta^j\)-eigenspace of \(U\). Therefore \(PV^jP=0\) unless \(t\mid j\). Averaging the \(Q\) powers in \(R\) gives

\[
 PRP=\frac1Q\sum_{\ell=0}^{Q/t-1}PV^{t\ell}P
      =\frac1tP\left(\frac{t}{Q}
          \sum_{\ell=0}^{Q/t-1}(V^t)^\ell\right)P.
\]

The parenthesized operator is \(\Pi_{V^t,1}\), proving (C5). For orthogonal projectors \(P,R\), one has \(P+R\preceq(1+\|PR\|)I\). Subtracting from \(2I\) yields (C6). This proof includes zero eigenspace projectors. \(\square\)

For (C1), the projective commutator is

\[
 U_eU_f=\omega^{b_e\cdot a_f-b_f\cdot a_e}U_fU_e.
\tag{C7}
\]

Thus every noncommuting pair satisfies the lemma, regardless of the order of its nontrivial commutator. In particular, a small commutator angle at a large composite modulus does not create a small gap for these eigenvalue-check penalties. The claim concerns \(I-\Pi_{U,1}\), not \(I-(U+U^*)/2\).

## 3. Balanced peeling leaves a commuting family

Start with residual weights \(r_e=w_e\) and peeled weights \(d_e=0\). While two positive residual items \(e,f\) do not commute, transfer

\[
 s=\min(r_e,r_f)
\]

from each of \(r_e,r_f\) to \(d_e,d_f\). Each transfer eliminates at least one positive residual item, so there are at most \(m\) transfers. Commutation is tested using (C7), with modular arithmetic only.

Let

\[
 H_{\rm gap}=\sum_e d_eB_e,\quad
 H_{\rm com}=\sum_e r_eB_e,\quad W=\sum_e d_e.
\]

The residual Weyl operators commute pairwise and \(H=H_{\rm gap}+H_{\rm com}\). By (C6),

\[
 \gamma W I\preceq H_{\rm gap}\preceq W I,
 \qquad \gamma=\frac{1-2^{-1/2}}2.
\tag{C8}
\]

If \(W>0\), sample \(k\) independent indices according to \(d_e/W\), placing coefficient \(W/k\) on each occurrence. Repeated occurrences are merged. Matrix Chernoff, applied only for analysis to the dimension-\(q^n\) operator, gives relative error at most \(\eta\) with failure probability at most \(\delta\), for

\[
 k=O\!\left(\eta^{-2}
          [n\log q+\log(1/\delta)]\right).
\tag{C9}
\]

Indeed, after whitening \(H_{\rm gap}\), an unaveraged random summand has expectation \(I\) and norm at most \(1/\gamma\). This sampling algorithm uses only the rational coefficients \(d_e\); it never computes the whitening or an eigenvector. If \(W=0\), this part is absent.

## 4. Compact encoding of the commuting family

This section supplies the extra argument needed at a composite modulus. An isotropic submodule of \(\mathbb Z_q^{2n}\) need not admit the field-basis description used at prime \(q\).

Let \(E_0\) be the positive residual items. Form the integer matrix \(A\) whose columns are representatives of their projective labels

\[
 v_e=(a_e,b_e)\in\{0,\ldots,q-1\}^{2n}.
\]

Define the full-rank lattice

\[
 \mathcal L=A\mathbb Z^{|E_0|}+q\mathbb Z^{2n}
 \subseteq\mathbb Z^{2n}.
\tag{C10}
\]

Compute a column Hermite-normal-form basis \(D\in\mathbb Z^{2n\times2n}\) of this lattice, together with an integer transformation matrix expressing each column of \(D\) as a combination of columns of \([A\ qI]\). Such bases and transformations have polynomial bit complexity by the standard integer normal-form algorithms. Write

\[
 D_j=\sum_{e\in E_0} s_{ej}v_e+qz_j.
\]

Lift each basis column to an actual commuting Weyl operator

\[
 V_j=\prod_{e\in E_0}U_e^{s_{ej}},\qquad j=1,\ldots,2n.
\tag{C11}
\]

Its projective label is \(D_j\bmod q\). All \(V_j\) commute, because they are products of the commuting residual operators, and every \(V_j^Q=I\). Products and powers in (C11) are evaluated on the compact phase-and-label representation; huge products are not expanded.

For each residual input label \(v_e\in\mathcal L\), compute its integer lattice coordinates

\[
 t_e=D^{-1}v_e\in\mathbb Z^{2n}.
\]

Then \(U_e\prod_jV_j^{-t_{ej}}\) has zero projective label. It is therefore a scalar \(Q\)-th root of unity, which can be found exactly by modular phase arithmetic. We have computed

\[
 U_e=\tau^{\sigma_e}\prod_{j=1}^{2n}V_j^{t_{ej}}.
\tag{C12}
\]

The modulus of every exponent in (C12) may now be reduced to \(Q\). The number \(2n\) of lifted operators suffices even though some may be scalar, some may be redundant, and their actual orders may differ. No freeness or independence of a composite-modulus module is used.

Because the \(V_j\) are commuting normal operators, there is a simultaneous eigenbasis. In any actual eigenpattern write \(V_j=\tau^{x_j}\), where \(x_j\in\mathbb Z_Q\). Formula (C12) shows that

\[
 B_e(x)=\mathbf1\!\left[
       \sigma_e+\sum_{j=1}^{2n}t_{ej}x_j\not\equiv0\pmod Q
                              \right].
\tag{C13}
\]

Some vectors \(x\in\mathbb Z_Q^{2n}\) may not occur physically. This is harmless: a guarantee for every such vector includes every actual joint eigenpattern. This deliberate over-parameterization removes any need to enumerate the joint spectrum or to solve its consistency relations.

## 5. Invoke the published weighted-code theorem

Homogenize each affine row from (C13) to

\[
 g_e=(t_{e1},\ldots,t_{e,2n},\sigma_e)
      \in\mathbb Z_Q^{2n+1}.
\tag{C14}
\]

Apply Khanna--Putterman--Sudan, Theorem 5.19, to the weighted linear code

\[
 \mathcal C=\{(g_e\cdot y)_{e\in E_0}:
                       y\in\mathbb Z_Q^{2n+1}\},
\]

with coordinate weight \(r_e\). This theorem explicitly allows composite moduli and arbitrary positive weights, returns original code coordinates, and gives

\[
 \widetilde O\!\left((n+1)\log^2Q/\eta^2\right)
\tag{C15}
\]

coordinates in randomized time polynomial in the compact matrix size, \(\log Q\), and \(\eta^{-1}\). Multiple identical rows may first be merged; after sparsification their combined coefficient can be assigned to one original representative. The weighted form handles arbitrary coefficient ratios without expanding them into unit copies.

Restrict its all-query guarantee to \(y=(x,1)\). Equation (C13) gives the diagonal entries of \(H_{\rm com}\), so this is exactly a \(1\pm\eta\) Loewner approximation to \(H_{\rm com}\), supported on original checks. Scalar penalties are automatically included through the last coordinate of (C14).

Combine this with (C9). The relative inequalities for the two PSD summands add. If a single original item appeared in both pieces, add its two output coefficients. Choose \(\eta\le\epsilon\), with any desired constant slack for implementation. When the promised support is larger than \(m\), simply return the input. This proves (C3)--(C4).

All lattice normal forms, phase products, and peeling arithmetic have polynomial bit complexity. For example,

\[
 (\tau^cX^aZ^b)(\tau^dX^uZ^v)
   =\tau^{c+d+2b\cdot u}X^{a+u}Z^{b+v},
\]

so multiplication and exponentiation require no algebraic-number approximation. The only randomized analytic ingredient outside the cited code algorithm is coefficient-proportional sampling. The proof's matrix dimension \(q^n\) appears only as \(\log(q^n)=n\log q\).

### 5.1 Removing the modulus logarithm in the support theorem

Retain the same peeling and HNF construction. The commuting part is a weighted sum of the predicates
\[
 \mathbf1[g_e\cdot y\ne0\pmod Q],
 \qquad y\in\mathbb Z_Q^{2n+1}.
\]
Each zero set is a subgroup of the finite additive group
\(\mathbb Z_Q^{2n+1}\). The companion draft
*Optimal-support sparsification of whole subgroup constraints* proves that such original predicates can be sparsified with
\[
 O\!\left(
 \frac{\log|\mathbb Z_Q^{2n+1}|}{\eta^2}\right)
 =
 O\!\left(\frac{(n+1)\log Q}{\eta^2}\right)
 \tag{C16}
\]
coordinates. The theorem includes arbitrary positive weights and arbitrary finite groups; it has no primality assumption.

Again restrict to \(y=(x,1)\), including all physical joint eigenpatterns. This gives (C16) for \(H_{\rm com}\). The gapped part already has \(O(n\log q/\eta^2)\) support by (C9), at constant success probability. Add the two PSD approximations and merge repeated original indices. Taking \(\eta\) a sufficiently small constant multiple of \(\epsilon\) proves Theorem C'.

The new subgroup support theorem supplies an explicit-table partial-coloring algorithm. In this application that table has \(Q^{2n+1}\) rows, which explains the exponential construction bound and the distinction from the KPS-based compact algorithm. Neither result requires factoring \(q\).

## 6. Relation to the prime result and checked sources

The prime-qudit draft obtains \(O((n+1)\log p/\epsilon^2)\) support by applying the optimal abelian Cayley theorem and averaging scalar automorphisms over a projective line. That particular argument does not directly establish the same bound for composite \(q\): unit multiplication has several orbits among the nonzero multiples of a modular row. The Gaussian whole-subgroup method in Section 5.1 bypasses this obstruction by retaining each modular predicate as one item. The support theorem (C4') and compact construction (C4) should be reported separately.

1. **Khanna, Putterman, Sudan, _Efficient Algorithms and New Characterizations for CSP Sparsification_, STOC 2025.** Section 5 treats weighted codes over arbitrary \(\mathbb Z_q\); Theorem 5.19 gives the support and Claim 5.18 the compact polynomial runtime used above. <https://arxiv.org/html/2404.06327v2>.

2. **Kannan and Bachem, _Polynomial Algorithms for Computing the Smith and Hermite Normal Forms of an Integer Matrix_, SIAM Journal on Computing 8(4), 1979.** The basis and multiplier matrices in Section 4 are standard polynomial-time integer linear algebra. <https://doi.org/10.1137/0208040>; primary paper copy: <https://people.tamu.edu/~rojas/kannanbachemhermitesmith79.pdf>.

3. **Hostens, Dehaene, De Moor, _Stabilizer states and Clifford operations for systems of arbitrary dimensions, and modular arithmetic_, Physical Review A 71, 042315, 2005.** Standard arbitrary-dimensional Weyl/stabilizer representation background. Our proof only needs the multiplication law and provides its own commuting-family encoding. <https://arxiv.org/abs/quant-ph/0408190>.

4. **Basu, Brakensiek, Putterman, _Many Hamiltonians Are Sparsifiable_, May 2026.** Theorem 1.1/3.5 gives a near-linear bound for fixed-locality qubit Pauli penalties, with locality-dependent factors. It does not state the present arbitrary-locality composite-dimensional check theorem. Its uniformly gapped sampling arguments and the ordinary code inputs are antecedents, not new ingredients here. <https://arxiv.org/html/2605.02211v1>.

5. **Tropp, _An Introduction to Matrix Concentration Inequalities_.** Matrix Chernoff supplies (C9); the matrix is not explicitly built by the algorithm. <https://arxiv.org/abs/1501.01571>.

The additional contributions relative to the preceding checkpoint drafts are the removal of the prime-dimension hypothesis while keeping compact polynomial time, and the sharper support existence bound obtained from the later Gaussian subgroup theorem. The primary-source search did not locate an identical Weyl-check sparsification theorem, but this is not a completed publication-priority claim.
