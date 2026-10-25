# Increment: the exact separation bottleneck in compact code partial coloring

*Mathematical scope note, 25 October 2026. This is a barrier for one implementation route, not a lower bound on the complexity of constructing sparsifiers.*

## 1. Statement

Let \(b_e:\mathbb F_2^d\to\{0,1\}\) be homogeneous binary linear-check predicates
\[
b_e(y)=\mathbf1[a_e\cdot y\ne0],
\]
with positive rational weights \(w_e\). For \(0<a\le1/2\), write
\[
W(y)=\sum_e w_e b_e(y),
\qquad
Q_a=
\left\{z\in[-1,1]^m:
\left|\sum_e w_ez_e b_e(y)\right|
\le aW(y)\ \text{for every }y\in\mathbb F_2^d
\right\}.
\tag{1}
\]
This is the symmetric perturbation body used by the Gaussian whole-subgroup sparsification argument.

**Proposition.** At the fixed value \(a=1/4\), deciding whether a specified rational vector belongs to \(Q_a\) is coNP-complete. This holds when every \(a_e\) has Hamming weight at most two and the specified vector belongs to \(\{0,1/2\}^m\).

Consequently a general exact polynomial-time separation oracle for the compactly represented bodies (1) would imply \(\mathrm P=\mathrm{NP}\). Enumerating all \(2^d\) query vectors supplies an exact oracle, but is exponential in the compact dimension.

## 2. Reduction

Start with an instance of weighted Max-Cut: an undirected graph on \(n\) vertices, nonnegative integer edge weights \(\lambda_{uv}\), and a threshold \(K\). Let
\[
M=\max_v\sum_{u:uv\in E}\lambda_{uv}.
\]
The edgeless case is trivial, so take \(M>0\). Introduce binary variables \(x_1,\ldots,x_n,t\). Consider the signed sum of homogeneous linear-check predicates
\[
\begin{split}
F(x,t)
={}&\sum_{uv\in E}\lambda_{uv}(x_u\mathbin{\oplus}x_v)\\
&-\frac M2\sum_{v=1}^n
\bigl(x_v+(x_v\mathbin{\oplus}t)\bigr)
+\left(\frac{Mn}{2}-K\right)t.
\end{split}
\tag{2}
\]
Here the binary quantities are interpreted as real \(0/1\) numbers. Every summand is a homogeneous linear-check predicate on at most two coordinates.

If \(t=0\) and \(S=\{v:x_v=1\}\), then
\[
F(x,0)=\operatorname{cut}_\lambda(S)-M|S|
\le0,
\tag{3}
\]
because every cut edge incident to \(S\) is counted in the weighted-degree sum of \(S\). If \(t=1\), then \(x_v+(x_v\oplus1)=1\), so
\[
F(x,1)=\operatorname{cut}_\lambda(S)-K.
\tag{4}
\]
Thus
\[
F(y)\le0\ \text{for every }y\in\mathbb F_2^{n+1}
\quad\Longleftrightarrow\quad
\operatorname{MaxCut}_\lambda(G)\le K.
\tag{5}
\]

Write (2) as \(F(y)=\sum_e c_e b_e(y)\), keeping each displayed term as its own input item and dropping zero coefficients. Set
\[
a=\frac14,\qquad
w_e=\frac{|c_e|}{a}=4|c_e|,
\qquad
z_e=a(1+\operatorname{sign}c_e).
\tag{6}
\]
All weights are positive rationals, and \(z_e\in\{0,1/2\}\). Moreover,
\[
\sum_e w_e(z_e-a)b_e(y)=F(y).
\tag{7}
\]
The upper inequality in (1) is therefore exactly the left side of (5). The lower inequality in (1) is automatic: \(z_e\ge0\) and \(b_e(y)\ge0\), so the perturbed sum is nonnegative. The cube constraint is also automatic. Hence
\[
z\in Q_{1/4}
\quad\Longleftrightarrow\quad
\operatorname{MaxCut}_\lambda(G)\le K.
\tag{8}
\]
The construction has polynomial size and rational bit complexity.

This proves coNP-hardness. Nonmembership lies in NP because a violating query \(y\), or a violated cube coordinate, is a polynomially checkable certificate. Therefore membership is coNP-complete. \(\square\)

## 3. What the barrier does and does not say

The optimal-support subgroup theorem gives \(O(d/\epsilon^2)\) support for binary linear checks. Its generic constructive proof uses partial coloring and a separation oracle for a body of the form (1). Proposition 1 shows why simply declaring that oracle efficient on compact code input is invalid, even when every check has arity at most two.

This is **not** evidence that optimal-support code sparsifiers cannot be constructed in compact polynomial time. Indeed, the arity-two setting in the reduction also has special graph structure, and graph spectral sparsification has efficient optimal-support methods that avoid this exact query-separation problem. A new code-specific partial-coloring implementation, a suitable relaxation, or a different constructive argument could likewise circumvent the obstruction.

The proposition addresses exact separation. It does not establish a hardness factor for every possible weak oracle or relaxation. No claim about approximate separation is needed for the algorithmic distinction in the companion drafts.

For whole finite-field block queries, the available compact construction in this checkpoint instead applies Quanrud's weighted quotient-sparsification theorem with adaptive resparsification. It returns
\[
O\!\left(d\log(2d/\epsilon)/\epsilon^2\right)
\]
original blocks in randomized polynomial time. The new Gaussian proof gives the smaller \(O(d\log q/\epsilon^2)\) support bound with a construction polynomial in an explicitly listed \(q^d\)-row query table. These are different algorithmic guarantees.

## 4. Sources and attribution

- Richard M. Karp, **Reducibility Among Combinatorial Problems** (1972), supplies the standard NP-completeness baseline for weighted Max-Cut. Primary publication: <https://doi.org/10.1007/978-1-4684-2001-2_9>. A scan of the original chapter is available at <https://www.cs.mun.ca/~kol/courses/6743-w15/papers/karp.pdf>.
- Reis--Rothvoss, **Vector Balancing in Lebesgue Spaces**, supplies the general partial-coloring framework used by the companion argument: <https://arxiv.org/abs/2007.05634>.
- Brakensiek--Guruswami--Putterman, **Multiplicative error set system sparsification: A simpler proof via chain length contraction** (May 2026), Theorem 1.2 gives the stronger general set-system existence baseline with overhead \(\log^2(d/\epsilon)(\log\log(d/\epsilon))^2\), and explicitly does not claim an efficient implementation for arbitrary implicit set systems: <https://arxiv.org/abs/2605.01508>.
- Kent Quanrud, **Quotient sparsification for submodular functions**, SODA 2024, is the classical compact algorithmic backend: <https://kentq.s3.amazonaws.com/submodular-sparsification.pdf>.
- Companion proofs: 30_optimal_whole_subgroup_constraints.md, 27_adaptive_quotient_resparsification.md, and 23_arbitrary_locality_stabilizer_block_sparsification.md.

The reduction above records the precise obstruction relevant to this checkpoint. No priority claim for hardness of Max-Cut separation in related convex bodies is intended.
