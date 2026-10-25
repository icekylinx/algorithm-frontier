# Locality-independent sparsification of positive Pauli Hamiltonians

*Incremental English research draft, 25 October 2026. The proposed new ingredient is a weighted decomposition into a commuting Pauli Hamiltonian and a uniformly positive part. It removes the locality dependence from the known Pauli sparsification reduction. Established binary-code sparsifiers then give near-linear support with preprocessing polynomial in the compact Pauli input, and linear support with a slower construction. The last section records a separate correlated-deletion extension. Priority remains subject to external review.*

## 1. Main theorem and exact model

Let
\[
 H=\sum_{e=1}^{m}w_e L_{P_e},\qquad
 L_P=I-P,\qquad w_e>0,
 \tag{1}
\]
where \(P_e\) is a Hermitian signed Pauli string on \(n\geq1\) qubits: a tensor product of \(I,X,Y,Z\), with an overall sign in \(\{+1,-1\}\). Thus \(P_e^2=I\) and \(0\preceq L_{P_e}\preceq2I\). A string may act on every qubit. The input gives each string by \(O(n)\) bits and each weight as a positive rational. Repeated strings are allowed, \(P=-I\) is allowed, and zero terms with \(P=I\) may be discarded.

A sparsifier uses original indices with nonnegative output coefficients \(\widehat w_e\) and satisfies
\[
 (1-\epsilon)H\preceq
 \widehat H:=\sum_e\widehat w_e L_{P_e}
 \preceq(1+\epsilon)H.
 \tag{2}
\]
Equivalently it gives a fixed nonnegative multiplier \(\widehat w_e/w_e\) for each retained input clause. The guarantee holds for every quantum state, including entangled states, and preserves the kernel exactly.

**Theorem 1 (arbitrary locality).** For every input (1) and \(\epsilon\in(0,1)\):

1. There exists a sparsifier (2) with
   \[
   O\!\left(\min\{m,(n+1)/\epsilon^2\}\right)
   \tag{3}
   \]
   original terms. A randomized construction is polynomial in \(2^n,m,\epsilon^{-1}\), and the rational input bit length.

2. There is a randomized classical construction polynomial in \(n,m,\epsilon^{-1}\), and the rational input bit length, with
   \[
   O\!\left(\min\left\{m,\,
       \frac{(n+1)\log((n+2)/\epsilon)}{\epsilon^2}
       \right\}\right)
   \tag{4}
   \]
   original terms and constant success probability. There is no locality factor and no support dependence on the input weight ratio or original term count. The efficient classical backend is Quanrud's quotient sparsifier with the adaptive resparsification observation proved in the companion note.

Both versions may additionally preserve the total coefficient exactly:
\[
 \sum_e\widehat w_e=\sum_ew_e,
\]
where the sums refer to the nonzero clauses after discarding \(P_e=I\). This adds no retained items.

The distinction between (3) and (4) is computational. The July 2026 optimal weighted binary-code theorem gives the linear support in (3), but its supplied construction can be exponential in the code dimension. Quanrud's quotient theorem and adaptive resparsification give (4). This note does not claim a compact-input polynomial-time construction with the exact support (3).

The support in (3) is jointly optimal in \(n\) and \(\epsilon\) in the natural regime \(0<\epsilon\le1/2\), \(n\ge2\lceil\epsilon^{-2}\rceil\), already for commuting two-local clauses. This is an inherited classical cut lower bound, not a new Pauli lower-bound phenomenon. Put \(s=\lceil\epsilon^{-2}\rceil\), \(B=n-s\ge s\), and use
\[
 H=\sum_{uv\in E(K_{s,B})}(I-Z_uZ_v).
\]
On a computational basis state its energy is twice the corresponding cut value. Any nonnegative original-term spectral sparsifier therefore yields a weighted cut sparsifier of \(K_{s,B}\). The direct cut inequality (EC15) in the companion exact-label-cut note gives support
\[
 t\ge\frac{(1-\epsilon)^2sB}
              {(1+3\sqrt2\,\epsilon\sqrt{s})^2}
   =\Omega(n/\epsilon^2).
\]
For every fixed \(\epsilon<1\), the elementary input \(\sum_{j=1}^n(I-Z_j)\) also requires all \(n\) clauses: omit clause \(j\), and the computational basis state whose sole negative \(Z\)-eigenvalue is at \(j\) changes from energy \(2\) to \(0\). No claim is made that the first lower-bound regime covers every relation between \(n\) and \(\epsilon\).

The theorem concerns the positive clauses in (1). Expanding an arbitrary Hamiltonian in the signed Pauli basis does not automatically put it in this model while preserving its reference energy: the identity shifts in \(I-P_e\) are part of the supplied positive Hamiltonian.

## 2. Public and OAI-assisted baselines

Basu, Brakensiek, and Putterman, *Many Hamiltonians Are Sparsifiable*, arXiv:2605.02211v1, May 2026, Theorem 3.5, already give \(\widetilde O_r(n/\epsilon^2)\) original terms for an arbitrarily weighted **fixed-\(r\)-local** positive Pauli Hamiltonian, with randomized classical preprocessing polynomial in \(m,n,O_r(1)\). Their introduction explicitly treats \(r\) as constant. The proof partitions into \(3^r\) Pauli patterns and then into \(r\)-partite subinstances; each resulting commuting family becomes a classical parity instance. Their Section 3.2 extends that argument to fixed predicates admitting positive Pauli decompositions.

The proposed change is the replacement of those locality-dependent partitions by the two-part decomposition in Section 3 below. The commuting part can involve arbitrary high-locality, overlapping Pauli strings. The other part is sampled using a uniform spectral lower bound. Consequently the support and compact-input runtime have no hidden \(O_r(1)\) or \(3^r\) dependence.

The ordinary classical ingredients are public results and are not claimed new:

- Quanrud, *Quotient sparsification for submodular functions*, SODA 2024, Theorem 1.1, gives \(O(r\log(mr)/\epsilon^2)\) support for rank-\(r\) weighted polymatroid quotients. The companion note `27_adaptive_quotient_resparsification.md` gives the adaptive repeated-application argument reducing this to \(O(r\log(2r/\epsilon)/\epsilon^2)\), with constant success probability. It uses only restrictions of the original rank function; explicit finite-field ranks and rational weights satisfy its polynomial-bit implementation contract. Applied to a binary row matroid, every zero set of a linear query is closed, so this backend preserves all weighted codeword support sizes. The resparsification is treated as an ordinary-backend observation, separate from the proposed quantum decomposition.

- Khanna–Putterman–Sudan, *Efficient Algorithms and New Characterizations for CSP Sparsification*, STOC 2025, arXiv:2404.06327v2, Section 5, Theorem 5.19 and Claim 5.18. Their input is an arbitrary possibly weighted generator matrix. For binary code dimension \(d\), the resulting support is \(\widetilde O(d/\epsilon^2)\) and preprocessing is polynomial in \(d,m,\epsilon^{-1}\). The two-pass reduction removes dependence on the initial code length from the support. Basu–Brakensiek–Putterman Theorem 2.11 explicitly restates the arbitrary-weight binary case.
- Basu–Kothari–Meka–Tudose, *Optimal Sparsifiers for Abelian Cayley Graphs*, arXiv:2607.08261v1, July 2026, Theorem 1.5 and Remark 1.6. These give \(O(d/\epsilon^2)\) support for weighted binary linear codes, via the group \(\mathbb F_2^d\), with randomized computation polynomial in the explicit group size \(2^d\). Its Section 5 acknowledges sequential ChatGPT-5.5-Plus sessions for the key volume argument. This is a concrete public OAI-assisted ingredient of the sharp support corollary, not a result being rediscovered here.

General finite-group Cayley sparsification already supplies weaker locality-independent polynomial support through the finite Pauli group. Thus the claim is not that polynomial-size Pauli sparsifiers were previously impossible. The intended increment is the linear support and near-linear compact-input construction for arbitrary locality.

Basu–Brakensiek–Kothari–Putterman, *Quantum Cut Sparsifiers*, June 2026, also give near-linear support for their special two-local Quantum Cut operators. That specialized theorem and the fixed-locality Pauli theorem remain separate antecedents. Neither is a theorem for all arbitrary-locality positive Pauli clauses by its stated reduction.

## 3. Weighted anticommuting-pair decomposition

Two Pauli strings either commute or anticommute. If Hermitian \(P,Q\) anticommute, then
\[
 (P+Q)^2=2I,\qquad
 (I-P)+(I-Q)\succeq(2-\sqrt2)I.
 \tag{5}
\]

Start with residual coefficients \(a_e=w_e\) and peeled coefficients \(b_e=0\). While there are two positive-residual clauses \(e,f\) with \(P_eP_f=-P_fP_e\), put
\[
 d=\min\{a_e,a_f\},
 \quad
 a_e\leftarrow a_e-d,\quad a_f\leftarrow a_f-d,
 \quad
 b_e\leftarrow b_e+d,\quad b_f\leftarrow b_f+d.
 \tag{6}
\]
Each iteration makes at least one residual coefficient zero, so there are at most \(m\) iterations. At termination the positive-residual strings commute pairwise.

Define
\[
 H_{\rm com}=\sum_ea_eL_{P_e},\qquad
 H_{\rm gap}=\sum_eb_eL_{P_e},\qquad
 W_{\rm gap}=\sum_eb_e.
 \tag{7}
\]
Then \(H=H_{\rm com}+H_{\rm gap}\). Every peeling operation contributes a balanced pair \(d(L_P+L_Q)\). Consequently, with the absolute constant \(\gamma=1-1/\sqrt2>0\),
\[
 \boxed{\quad
 \gamma W_{\rm gap}I\preceq H_{\rm gap}
       \preceq2W_{\rm gap}I.
 \quad}
 \tag{8}
\]
If no pair was peeled, \(H_{\rm gap}=0\). The lower bound follows by summing (5), since \(W_{\rm gap}=2\sum_{\rm peeling\ steps}d\). It does not require the pairs from different iterations to commute or to be disjoint.

This entire decomposition is computed from binary Pauli descriptions and rational weights. A symplectic inner product tests anticommutation in polynomial time. Straightforward pair searches already give polynomial preprocessing; no fast implementation claim is needed. Exact rational subtraction and addition have polynomial bit complexity in the total supplied rational encoding length.

One original term may contribute to both parts, or to several peeled pairs. This causes no problem: its final coefficients are added, and the delivered operator is still a nonnegative multiple of that original \(I-P_e\).

## 4. Sparsifying the uniformly positive part

If \(W_{\rm gap}>0\), sample indices independently with probabilities
\[
 p_e=b_e/W_{\rm gap}.
\]
Each sampled occurrence contributes \((W_{\rm gap}/k)L_{P_e}\), where \(k\) is the number of samples. In particular the coefficients of this sample sum add exactly to \(W_{\rm gap}\).

For analysis only, whiten \(H_{\rm gap}\). Each unscaled sampled matrix is
\[
 X_e=W_{\rm gap}H_{\rm gap}^{-1/2}
                    L_{P_e}H_{\rm gap}^{-1/2}.
\]
Its expectation is identity and, by (8),
\[
 0\preceq X_e\preceq(2/\gamma)I.
 \tag{9}
\]
Standard matrix Chernoff in dimension \(2^n\) therefore gives
\[
 (1-\epsilon)H_{\rm gap}\preceq\widehat H_{\rm gap}
       \preceq(1+\epsilon)H_{\rm gap}
 \tag{10}
\]
with failure probability at most \(\delta\) using
\[
 k=O\!\left(\epsilon^{-2}
                 [n+\log(2/\delta)]\right).
 \tag{11}
\]

The implementation merely samples the rational coefficient distribution and counts occurrences. No Hilbert-space matrices, eigenvectors, or matrix inverses are computed. The dimension \(2^n\) appears only in the proof through its logarithm.

## 5. The commuting remainder is an affine binary code

Let the remaining positive-residual strings be pairwise commuting. Modulo phase, a Pauli string is a vector in \(\mathbb F_2^{2n}\), and commutation is orthogonality under the standard nondegenerate symplectic form. Their span is isotropic and hence has dimension \(d\leq n\).

Choose projectively independent commuting strings \(Q_1,\ldots,Q_d\) from the residual family. Binary Gaussian elimination and exact Pauli phase tracking write every residual term as
\[
 P_e=(-1)^{s_e}\prod_{j=1}^{d}Q_j^{v_{e,j}},
 \qquad v_e\in\mathbb F_2^d,\quad s_e\in\mathbb F_2.
 \tag{12}
\]
The product is Hermitian, so the remaining phase is a real sign. The constant \(P_e=-I\) is represented by \(v_e=0,s_e=1\).

There is a common eigenbasis in which \(Q_j\) has eigenvalue \((-1)^{x_j}\), \(x\in\mathbb F_2^d\). In fact every pattern occurs: its common spectral projector
\[
 \Pi_x=2^{-d}\prod_{j=1}^{d}(I+(-1)^{x_j}Q_j)
\]
has trace \(2^{n-d}>0\), since every nonempty product of the projectively independent generators is a nonidentity, traceless Pauli. Thus the eigenvalue of \(L_{P_e}\) on that joint eigenspace is
\[
 1-(-1)^{s_e+v_e\cdot x}
 =2\,\mathbf1[s_e+v_e\cdot x=1].
 \tag{13}
\]

Form the binary generator matrix whose row indexed by \(e\) is \((v_e,s_e)\in\mathbb F_2^{d+1}\), with row weight \(a_e\). A weighted binary-code sparsifier preserves
\[
 \sum_ea_e\,\mathbf1[(v_e,s_e)\cdot y=1]
 \tag{14}
\]
for every \(y\in\mathbb F_2^{d+1}\). Taking \(y=(x,1)\), it preserves all the eigenvalues in (13). Therefore it yields a Loewner sparsifier \(\widehat H_{\rm com}\) of the commuting Hamiltonian. The extra homogeneous coordinate is only a classical code coordinate; it does not introduce an extra physical qubit.

For the efficient construction, use the rank function of the augmented binary row vectors. For every \(y\), the rows annihilating \(y\) form a closed set: every row in their span is also annihilated. Its complement is a matroid quotient. Quanrud's theorem followed by the companion adaptive resparsification argument therefore preserves (14), with
\[
 O\!\left(\frac{(d+1)\log((d+2)/\epsilon)}{\epsilon^2}\right)
\]
terms and polynomial time in the compact rational input. The earlier KPS routine remains a valid alternative with its stated polylogarithmic factors, but is not needed for this explicit single-logarithm bound. With the July 2026 optimal weighted code theorem, this part instead has \(O((d+1)/\epsilon^2)\) terms with an explicit-group polynomial, potentially exponential-in-\(d\), construction.

**Exact total coefficient.** Every augmented row \((v_e,s_e)\) is nonzero: a zero row would represent the discarded operator \(P_e=I\). Averaging the code approximation over all \(y\in\mathbb F_2^{d+1}\) therefore shows that the sum \(\widehat W_{\rm com}\) of its output coefficients lies in \((1\pm\eta)W_{\rm com}\), where \(W_{\rm com}=\sum_ea_e\) and \(\eta\) is the code accuracy. Rescale those coefficients by \(W_{\rm com}/\widehat W_{\rm com}\). The total becomes exactly \(W_{\rm com}\), while the spectral factors become \((1-\eta)/(1+\eta)\) and \((1+\eta)/(1-\eta)\). Choosing \(\eta=\epsilon/4\) puts them within \(1\pm\epsilon\), with the same asymptotic support. An empty commuting part needs no normalization. If a failed code run returns total zero for a nonempty commuting part, detect this and declare preprocessing failure before division.

No simultaneous diagonalizing matrix needs to be constructed. The input to the code routine is only the polynomial-size binary matrix and rational weight list.

## 6. Combining the pieces, accuracy, and computational scope

Sparsify the gapped part at accuracy \(\epsilon\), and the commuting code at accuracy \(\epsilon/4\) followed by the optional exact-total normalization above. Add the two output coefficients for each original index. On the two success events,
\[
 (1-\epsilon)(H_{\rm com}+H_{\rm gap})
 \preceq\widehat H_{\rm com}+\widehat H_{\rm gap}
 \preceq(1+\epsilon)(H_{\rm com}+H_{\rm gap}).
 \tag{15}
\]
Thus the errors add as PSD inequalities; no additional relative-error loss is introduced by the decomposition. The total support is at most the sum of the two supports. Their total coefficients are exactly \(W_{\rm gap}\) and \(W_{\rm com}\), respectively, so the final total is the original \(\sum_ew_e\). Choose constant failure budgets for the two subroutines to obtain constant success probability; more precise success parameters are inherited from the selected public code routine and (11).

For (3), use the optimal weighted-code existence theorem and a constant-probability sample for the gapped part. Their union has \(O((n+1)/\epsilon^2)\) terms. The public optimal-code algorithm supplies the stated explicit-Hilbert-size construction. For (4), use the resparsified matroid-quotient backend instead. Its exact integer-rank and rational-weight implementation is detailed in the companion note; no implicit real-valued oracle is needed here.

All output coefficients are nonnegative. Repeated sampled occurrences and repeated uses of an original clause can be merged by adding coefficients. If any advertised bound is at least the number of supplied clauses, retaining the input is an available trivial branch.

The input may have a large weight ratio, arbitrary locality, and a nontrivial kernel. The support bounds do not depend on a spectral gap or on that weight ratio. Polynomial bit complexity assumes the usual rational-weight input model, including the total input bit length. No near-linear time, quantum speedup, or deterministic compact-input near-linear-support construction is asserted.

## 7. A separate all-deletions extension

The preceding two-part decomposition is tailored to one Hamiltonian. It is not automatically a common summary for every deletion scenario: removing one side of a peeled pair can destroy the spectral lower bound (8). The following independent operator-importance argument gives a rigorous shared-summary extension.

Attach a label set \(\Lambda(e)\), \(|\Lambda(e)|\leq d_0\), to each original term, using \(L\) labels in total. A query \(F\), \(|F|\leq h\), deletes every term carrying a label of \(F\). Let \(E_F\) be the survivors and \(H_F=\sum_{e\in E_F}B_e\), where \(B_e=w_eL_{P_e}\). Here a summary must use one fixed multiplier per original item and satisfy (2) for every \(H_F\). Different label lists are not merged.

### 7.1 Hereditary operator-importance bound

For any PSD family \(A_i\) with sum \(M\), write
\[
 \tau_i=\inf\{t:A_i\preceq tM\}.
\]
The all-positive-rescalings lemma in the companion Cayley draft says: if every positively rescaled subfamily of size at least \(k\) has an item \(\alpha A_i\preceq\sum_{j\ne i}A_j\), then
\[
 \sum_i\tau_i\leq4(k-1)/\alpha.
 \tag{16}
\]
Its proof whitens \(M\), normalizes each item by its operator norm, and samples it with probability proportional to that norm. An eigenvector witness and Markov's inequality produce an expected \((\alpha/4)\sum_i\tau_i\) non-dominated items, whereas the hypothesis permits at most \(k-1\).

For Pauli clauses one can take \(k=n+2,\alpha=1/4\). Sort \(n+2\) clauses by increasing positive weight. If the last \(n+1\) contain an anticommuting pair, (5) lets that heavier pair dominate one quarter of the globally lightest clause. Otherwise the last \(n+1\) commute and have a nonempty signed product relation \(\pm I\). A \(+I\) relation dominates its lightest term by the rest, using
\[
 I-\prod_jP_j\preceq\sum_j(I-P_j)
\]
for commuting involutions. A \(-I\) relation has sum at least \(2I\), so it dominates the globally lightest excluded term. Weight order preserves each inequality.

This argument holds under arbitrary further positive rescaling. Therefore, for every subfamily \(X\),
\[
 \sum_{e\in X}
 \|H_X^{\dagger/2}B_eH_X^{\dagger/2}\|
 \leq16(n+1).
 \tag{17}
\]
This remains valid for noncommuting, frustrated, singular, and arbitrarily weighted inputs.

### 7.2 Cheap dominating sets and scores in the compact model

A polynomial-time subroutine finds at most \(n+1\) clauses \(S\) satisfying
\[
 B_e\preceq4H_S\quad\text{for every term }e.
 \tag{18}
\]

Process terms in decreasing weight order, maintaining a projectively independent commuting Pauli basis. Add an independent commuting term. Skip a term that equals a positive product of the selected terms, since its clause is dominated by those earlier heavier clauses. At the first anticommuting term, add it and stop. At the first term that is the negative of a selected product, add it and stop. An anticommuting stopping pair has sum at least \((2-\sqrt2)wI\), and a negative-product stopping relation has sum at least \(2wI\), where \(w\) is the new term's weight. Every later term has weight at most \(w\) and is therefore dominated by four times the selected sum. Earlier skipped terms remain dominated. If no stopping event occurs, every unselected item was skipped with a valid positive-relation witness.

Repeatedly remove such sets to form disjoint layers \(S_1,S_2,\ldots\). For \(e\in S_i\), summing its domination by earlier layers gives
\[
 \tau_e\leq t_e:=
 \begin{cases}
 1,&i=1,\\
 \min\{1,4/(i-1)\},&i\geq2.
 \end{cases}
 \qquad
 \sum_et_e=O((n+1)\log(2m)).
 \tag{19}
\]
Only binary elimination, phase tracking, and weight comparisons are required. The same upper-score bound holds on every subfamily, with \(\log(2m)\) using the original count.

### 7.3 Uniform correlated-failure summaries

Clip \(h\) to \(L\), and put
\[
 Q=\sum_{j=0}^{h}\binom Lj,\qquad
 \Gamma(h,d_0)=\frac{(h+d_0)^{h+d_0}}{h^h d_0^{d_0}}
 \tag{20}
\]
for positive \(h,d_0\), and \(\Gamma=1\) otherwise.

The monotone-importance pool argument from the companion robust-spectral draft, with (17), yields one fixed-weight summary of size
\[
 O\!\left(\min\left\{m,\,
 \frac{\Gamma(n+1)}{\epsilon^2}
      \left[n+\log\frac{2Q}{\delta}\right]\right\}\right)
 \tag{21}
\]
valid simultaneously for every \(|F|\leq h\), with probability at least \(1-\delta\). This version has preprocessing polynomial in the explicit Hilbert-space dimension. Using the cheap scores (19) instead gives compact-input polynomial randomized preprocessing and size
\[
 O\!\left(\min\left\{m,\,
 \frac{\Gamma(n+1)\log(2m)}{\epsilon^2}
      \left[n+\log\frac{2Q}{\delta}\right]\right\}\right).
 \tag{22}
\]

For completeness, independently include each label in a pool \(R\) with probability \(d_0/(h+d_0)\), and include an item in \(X_R\) exactly when all of its labels lie in \(R\). For every surviving pair \((e,F)\), with probability at least \(1/\Gamma\), the pool includes all labels of \(e\) and none of \(F\). Then \(e\in X_R\subseteq E_F\), so true importance in \(X_R\) dominates its value in \(E_F\).

Take \(J=O(\Gamma\log(2mQ/\delta))\) independent pools. With high probability, every surviving item/query pair has at least \(J/(2\Gamma)\) separating pools. Let \(u_e(X)\) be either its exact importance on \(X\), or the computable upper bound (19), and define
\[
 \widehat\sigma_e=u_e(E)+
       \frac{2\Gamma}{J}\sum_{j:e\in X_{R_j}}u_e(X_{R_j}).
 \tag{23}
\]
These scores dominate all surviving-scenario importances. Their total mass is \(O(\Gamma(n+1))\) for exact scores, or \(O(\Gamma(n+1)\log(2m))\) for cheap scores, on every pool outcome. Importance sampling with these scores and matrix Chernoff, followed by a union bound over \(Q\) scenarios, proves (21)–(22). The upper scores themselves need not be monotone; their domination of the true monotone importance is sufficient.

Before generating pools, compare the target with \(m\) and return the whole input if it is larger. In the nontrivial branch \(\Gamma\) is polynomially bounded by \(m\), while \(\log Q\leq L\log2\). Thus the compact-model construction is uniformly polynomial even when \(h,d_0\) are input parameters and \(Q\) is exponential. No query-dependent reweighting is used.

The correlated-failure result is separate from the near-linear ordinary theorem. Its extra factors, including \(\log Q\), are not suppressed as if they were free. Failure means deletion of specified Hamiltonian clauses, not tracing out or physically losing a quantum subsystem.

## 8. Sources and precise remaining questions

1. Basu–Brakensiek–Putterman. *Many Hamiltonians Are Sparsifiable*, Theorem 2.11, Theorem 3.5, and Section 3. https://arxiv.org/html/2605.02211v1
2. Khanna–Putterman–Sudan. *Efficient Algorithms and New Characterizations for CSP Sparsification*, Section 5, Theorem 5.19, Claim 5.18. https://arxiv.org/html/2404.06327v2
3. Basu–Kothari–Meka–Tudose. *Optimal Sparsifiers for Abelian Cayley Graphs*, Theorem 1.5, Remark 1.6, and Section 5. https://arxiv.org/html/2607.08261v1
4. Basu–Brakensiek–Kothari–Putterman. *Quantum Cut Sparsifiers*. https://arxiv.org/html/2606.09728v1
5. Basu–Kothari–Liu–Meka. *Sparsifying Sums of Positive Semidefinite Matrices*. https://arxiv.org/html/2508.08169v2
6. Gottesman. *Stabilizer Codes and Quantum Error Correction*. https://arxiv.org/abs/quant-ph/9705052
7. Aaronson–Gottesman. *Improved Simulation of Stabilizer Circuits*. https://arxiv.org/abs/quant-ph/0406196
8. Quanrud. *Quotient sparsification for submodular functions*, Theorem 1.1 and Section 3. https://kentq.s3.amazonaws.com/submodular-sparsification.pdf

The constant-gap decomposition uses only the elementary anticommuting-pair inequality. The potential novelty is its use to isolate one commuting weighted remainder, eliminating locality-dependent partitions in the all-state spectral approximation problem. Ordinary code sparsification, stabilizer linear algebra, and matrix Chernoff are established ingredients.

A compact-input polynomial-time algorithm with the exact \(O(n/\epsilon^2)\) support is not supplied, because the analogous sharp binary-code construction is not available from the cited efficient theorem. The ordinary decomposition also does not directly survive correlated deletion; Section 7 is the valid, quantitatively weaker shared-summary construction. Further work should distinguish improvements to these two remaining limitations from restatements of the existing fixed-locality results.
