# Whole stabilizer-block sparsification in arbitrary local dimensions

**Abstract.** For arbitrary, possibly heterogeneous, local dimensions with total Hilbert dimension $`D`$, a positive weighted sum of whole stabilizer-block penalties admits an all-state spectral sparsifier on $`O(\log(2D)/\epsilon^2)`$ original blocks. A factorization-free randomized algorithm polynomial in the compact input retains $`O(\log(2D)\log(\log(2D)/\epsilon)/\epsilon^2)`$ blocks. The proof combines a uniform conflict gap, character duality, exact subgroup-order computation, and closure-preserving rationalization. A layered modular cut family gives the joint lower bound along powers of two.

## 1. Model and results

Let the local dimensions be arbitrary integers
```math
q_1,\ldots,q_n\ge2,\qquad
 D=\prod_{j=1}^n q_j,\qquad
 Q=2\mathrm{lcm}(q_1,\ldots,q_n).
 \tag{CB1}
```
In particular, $`Q\le2D`$, and its binary encoding has polynomial length in the input dimensions. Let $`\tau=e^{2\pi i/Q}`$. On factor $`j`$, use the shift and clock operators
```math
X_j|z\rangle=|z+1\rangle,\qquad
 Z_j|z\rangle=e^{2\pi iz/q_j}|z\rangle.
```
Each input Weyl check is specified by its compact phase and displacement data:
```math
U=\tau^c\bigotimes_{j=1}^n X_j^{a_j}Z_j^{b_j},
 \quad c\in\mathbb Z_Q,\quad a_j,b_j\in\mathbb Z_{q_j}.
 \tag{CB2}
```
Every such $`U`$ satisfies $`U^Q=I`$: each $`q_j`$ divides $`Q/2`$, so the phase produced by the $`Q`$-th power of a local shift-clock product also vanishes. A requested $`Q`$-th-root eigenvalue is absorbed into the phase so that acceptance always means eigenvalue one.

An original block $`e`$ is an arbitrary list of mutually commuting checks $`U_{e,1},\ldots,U_{e,k_e}`$. Define its joint acceptance projector and penalty by
```math
E_e=\prod_{a=1}^{k_e}\Pi_{U_{e,a},1},
 \qquad B_e=I-E_e,\qquad
 H=\sum_{e=1}^m w_e B_e,
 \tag{CB3}
```
with nonnegative rational weights. The joint projector is allowed to be zero because of inconsistent phases; then the original block is the constant penalty $`I`$. An empty list gives zero penalty. No rank, independence, locality, or block-size promise is imposed. Checks from different blocks may fail to commute.

The desired output is a nonnegative reweighting of **whole original blocks**:
```math
\widetilde H=\sum_e\widehat w_e B_e,\qquad
 (1-\epsilon)H\preceq\widetilde H\preceq(1+\epsilon)H.
 \tag{CB4}
```
Thus every quantum state's energy and the exact kernel are preserved within the stated relative guarantee.

Write $`\rho=\log_2(2D)`$.

**Theorem 1, optimal support.** For $`0<\epsilon<1`$, an output satisfying (CB4) exists with
```math
O\!\left(\min\left\{m,\frac{\rho}{\epsilon^2}\right\}\right)
 \tag{CB5}
```
original blocks. The proof gives a randomized construction polynomial in an explicit finite character table, and consequently in $`D`$ and the remaining input/accuracy parameters. This sharper construction is not claimed polynomial in the compact binary description of the quantum input.

**Theorem 2, compact algorithm without factoring.** There is a randomized algorithm, polynomial in the compact input length, the rational weight encoding length, and $`\epsilon^{-1}`$, that succeeds with probability at least $`2/3`$ and returns an output satisfying (CB4) with
```math
O\!\left(\min\left\{m,
 \frac{\rho\log(2\rho/\epsilon)}{\epsilon^2}\right\}\right)
 \tag{CB6}
```
original blocks. It does not factor any $`q_j`$, construct a $`D`$-dimensional matrix, or enumerate the physical joint spectrum.

For a uniform composite dimension $`q`$, these bounds are respectively
```math
O(n\log(2q)/\epsilon^2)
 \quad\text{and}\quad
 O\!\left(
 \frac{n\log(2q)}{\epsilon^2}
 \log\frac{2n\log(2q)}{\epsilon}
 \right).
 \tag{CB7}
```
They are independent of how many checks occur inside one original block. The support statements always include the cap by $`m`$.

## 2. A constant gap from any conflicting pair

The prime-dimensional overlap argument has the following general form.

**Lemma 3.** Suppose $`U^Q=V^Q=I`$ and $`UV=\zeta VU`$, where $`\zeta\ne1`$ has order $`t\mid Q`$. For $`P=\Pi_{U,1}`$ and $`R=\Pi_{V,1}`$,
```math
PRP
 =\frac1tP\Pi_{V^t,1}P
 \preceq\frac1tP.
 \tag{CB8}
```
Consequently $`\|PR\|\le1/\sqrt t\le1/\sqrt2`$.

**Proof.** If $`Uz=z`$, then $`U(V^az)=\zeta^aV^az`$. Thus $`PV^aP=0`$ unless $`t\mid a`$. Average the $`Q`$ powers of $`V`$:
```math
PRP=\frac1Q\sum_{\ell=0}^{Q/t-1}PV^{t\ell}P
 =\frac1tP\left(\frac{t}{Q}
 \sum_{\ell=0}^{Q/t-1}(V^t)^\ell\right)P.
```
The parenthesis is the indicated orthogonal projector. This includes zero eigenspace projectors. $`\square`$

If block $`e`$ contains $`U`$ and block $`f`$ contains $`V`$, then $`E_e\preceq P`$, $`E_f\preceq R`$, and
```math
\|E_eE_f\|=\|E_ePR E_f\|\le\|PR\|\le1/\sqrt2.
```
For two orthogonal projectors, $`E+F\preceq(1+\|EF\|)I`$. Hence
```math
B_e+B_f\succeq(1-1/\sqrt2)I.
 \tag{CB9}
```
This depends on the order of the nontrivial commutator, not on how close its phase is to one. It concerns eigenvalue-check projectors, not the different penalty $`I-\mathrm{Re}U`$.

For the compact representation (CB2), commutation and all products are computed by modular phase arithmetic:
```math
(\tau^cX^aZ^b)(\tau^dX^uZ^v)
 =
 \tau^{c+d+\sum_j(Q/q_j)b_ju_j}
 X^{a+u}Z^{b+v}.
 \tag{CB10}
```
Thus the conflict test requires no cyclotomic-number approximation.

## 3. Balanced splitting

Maintain residual block coefficients $`r_e=w_e`$ and removed coefficients $`d_e=0`$. Whenever two positive residual blocks contain a noncommuting generator pair, let $`s=\min(r_e,r_f)`$, subtract $`s`$ from both residual coefficients, and add $`s`$ to both removed coefficients.

At least one residual block disappears at each step, so at most $`m`$ steps occur. At termination, every generator in the residual family commutes with every other generator. Define
```math
H_{\mathrm{gap}}=\sum_e d_eB_e,\qquad
 H_{\mathrm{com}}=\sum_e r_eB_e,\qquad
 W_{\mathrm{gap}}=\sum_e d_e.
 \tag{CB11}
```
Then $`H=H_{\mathrm{gap}}+H_{\mathrm{com}}`$, and (CB9) gives
```math
\gamma W_{\mathrm{gap}}I
 \preceq H_{\mathrm{gap}}
 \preceq W_{\mathrm{gap}}I,\qquad
 \gamma=\frac{1-1/\sqrt2}{2}.
 \tag{CB12}
```

If $`W_{\mathrm{gap}}>0`$, sample original indices independently with probabilities $`d_e/W_{\mathrm{gap}}`$, assigning weight $`W_{\mathrm{gap}}/k`$ to each occurrence. Standard matrix Chernoff gives a relative $`\eta`$-approximation using
```math
k=O\!\left(
 \frac{\log(2D)+\log(1/\delta)}{\eta^2}
 \right)
 \tag{CB13}
```
samples with failure probability at most $`\delta`$. Indeed, whitening for the analysis gives summands of norm at most $`1/\gamma`$. The algorithm only samples rational coefficients and does not perform the whitening. Repeated sampled indices are merged. If $`W_{\mathrm{gap}}=0`$, this part is absent.

The remaining issue is therefore the commuting family, while retaining each whole block as one item.

## 4. The exact physical spectrum is a small character torsor

Let $`\mathcal H`$ be the finite abelian group of actual Weyl operators generated by all residual checks. Let $`\mathcal C\le\mathcal H`$ be its subgroup of scalar operators, and let
```math
\chi_0:\mathcal C\longrightarrow\mathbb C^\times
```
be the physical scalar character: $`\chi_0(\alpha I)=\alpha`$.

Every non-scalar Weyl operator has trace zero. A scalar $`c\in\mathcal C`$ has trace $`D\chi_0(c)`$. For a character $`\chi\in\widehat{\mathcal H}`$, its multiplicity in the physical representation is therefore
```math
\begin{aligned}
 m_\chi
 &=\frac1{|\mathcal H|}
 \sum_{h\in\mathcal H}\overline{\chi(h)}\,\mathrm{tr}(h)\\
 &=\frac{D}{|\mathcal H|}
 \sum_{c\in\mathcal C}\overline{\chi(c)}\chi_0(c)\\
 &=
 \begin{cases}
 D|\mathcal C|/|\mathcal H|,
    &\chi|_{\mathcal C}=\chi_0,\\
 0,&\text{otherwise}.
 \end{cases}
\end{aligned}
 \tag{CB14}
```
This is the ordinary character-orthogonality calculation for a commuting stabilizer group.

At least one physical character $`\chi_*`$ occurs, by simultaneous diagonalization. All extensions of $`\chi_0`$ are then
```math
\chi_*\mathcal A,\qquad
 \mathcal A=
 \{\psi\in\widehat{\mathcal H}:\psi|_{\mathcal C}=1\}
 \cong\widehat{\mathcal H/\mathcal C}.
 \tag{CB15}
```
Every one of them occurs by (CB14), with the same positive integer multiplicity. In particular,
```math
|\mathcal A|=|\mathcal H/\mathcal C|\mid D,
 \qquad |\mathcal A|\le D.
 \tag{CB16}
```
Thus the actual joint eigenpatterns form an affine torsor with at most $`D`$ points. This step does not assume that a module over a composite modulus has a field basis.

For block $`e`$, let $`J_e\le\mathcal H`$ be generated by its original checks. On the character $`\chi_*\psi`$, its acceptance is
```math
\chi_*(U_{e,a})\psi(U_{e,a})=1
 \qquad\text{for every internal check }a.
 \tag{CB17}
```
These are homomorphism equations in $`\psi\in\mathcal A`$. Their solution set is either a coset of a subgroup of $`\mathcal A`$ or empty. An empty set gives the constant-one block penalty, including internally inconsistent blocks.

The affine-group theorem in [../../group-metric-constraints/manuscripts/affine-constraints-over-arbitrary-finite-groups.md](../../group-metric-constraints/manuscripts/affine-constraints-over-arbitrary-finite-groups.md) preserves all these original coset-complement items with
```math
O(\log(2|\mathcal A|)/\eta^2)
 \le O(\log(2D)/\eta^2)
 \tag{CB18}
```
blocks. The guarantee on all physical characters is exactly the desired Loewner guarantee for $`H_{\mathrm{com}}`$, because it is diagonal in their simultaneous eigenspaces.

Combine (CB18) with the gapped sample (CB13), add the two PSD inequalities, and merge coefficients assigned to the same original block. This proves Theorem 1.

The explicit-table construction has a finite bound even with heterogeneous dimensions. Since $`|\mathcal C|\mid Q`$ and (CB16) holds,
```math
|\mathcal H|\mid DQ,\qquad
 |\mathcal H|\le DQ\le2D^2.
 \tag{CB19}
```
One can enumerate this finite operator group, compute its abelian character presentation, and list the physical acceptance table in time polynomial in $`D`$ and the remaining input length. This is an explicit-dimension algorithm, not the compact algorithm below.

## 5. A compact exact subgroup-order oracle

The compact construction does not enumerate characters. For a collection $`S`$ of residual blocks, define
```math
\mathcal H_S=\langle J_e:e\in S\rangle.
 \tag{CB20}
```
We compute $`|\mathcal H_S|`$ exactly with integer normal forms and greatest common divisors, without factoring.

Collect the $`s`$ checks in those blocks. Let $`A_S`$ be the integer $`2n\times s`$ matrix of their projective displacement columns, and let
```math
M=\mathrm{diag}(q_1,\ldots,q_n,q_1,\ldots,q_n).
```
The projective displacement image is
```math
\mathcal P_S=(A_S\mathbb Z^s+M\mathbb Z^{2n})/M\mathbb Z^{2n}.
```
If $`D_S`$ is a column Hermite-normal-form basis of the full-rank lattice in the numerator, then
```math
|\mathcal P_S|=\frac{\det M}{|\det D_S|}
 =\frac{D^2}{|\det D_S|}.
 \tag{CB21}
```

Next compute an integer basis of the relation lattice
```math
\mathcal R_S=\{z\in\mathbb Z^s:A_Sz\in M\mathbb Z^{2n}\}.
 \tag{CB22}
```
This is obtained from an integer kernel basis of $`[A_S\ -M]`$ by projecting onto its first $`s`$ coordinates. The projection is injective on that kernel, since the remaining coordinates are uniquely determined by $`z`$. Standard Hermite/Smith normal-form algorithms produce such bases and transformation matrices with polynomial bit complexity.

For each basis relation $`z`$, evaluate the compact operator
```math
\prod_{i=1}^s U_i^{z_i}=\tau^{\kappa_z}I.
 \tag{CB23}
```
All the $`U_i`$ commute, so this is a homomorphism from the additive relation lattice to the scalar phase group. Its image is exactly the scalar subgroup $`\mathcal C_S`$ of $`\mathcal H_S`$. Therefore
```math
|\mathcal C_S|
 =\frac{Q}{\gcd(Q,\{\kappa_z:z\text{ is a basis relation}\})},
 \qquad
 |\mathcal H_S|=|\mathcal P_S|\,|\mathcal C_S|.
 \tag{CB24}
```
For an empty relation list, the gcd is interpreted as $`Q`$. Products and powers are computed by (CB10), with exponents reduced modulo $`Q`$ when convenient. Large integer kernel coefficients therefore cause no expansion of a matrix or a word.

Equations (CB21)--(CB24) give an exact polynomial-bit order oracle. They also show why retaining only the projective displacement span would be insufficient: nontrivial scalar relations encode inconsistent targets and must be counted.

## 6. Compact quotient sparsification without factoring

On the residual block ground set, consider
```math
f(S)=\log_2|\mathcal H_S|.
 \tag{CB25}
```
The ambient group $`\mathcal H`$ is abelian. Its subgroup product/intersection identity shows that $`f`$ is normalized, monotone, and submodular. Every positive marginal is at least one because a proper subgroup inclusion has index at least two. By (CB19),
```math
f([m])\le\log_2(DQ)\le2\log_2D+1.
 \tag{CB26}
```
If this rank is zero, all residual checks are the identity, every residual penalty is zero, and the residual output is empty. Assume below that the residual rank is positive.

For any physical character $`\chi`$, the zero-block set
```math
Z_\chi=\{e:J_e\subseteq\ker\chi\}
 \tag{CB27}
```
is closed for this rank. Indeed, all subgroups generated by its members lie in $`\ker\chi`$. If adding a block has zero marginal, that block's subgroup is already contained in the generated subgroup and also lies in $`\ker\chi`$. Thus $`[m]\setminus Z_\chi`$, the set of violated original blocks, is a quotient of $`f`$.

Quanrud's theorem mathematically applies to (CB25): it permits real-valued submodular ranks with positive marginals at least one. For a compact binary-input algorithm, however, an exact polynomial-bit value oracle cannot simply be assumed for logarithms and their subsequent optimization arithmetic.

The companion [../../group-metric-constraints/manuscripts/rational-quotient-ranks-from-weak-oracles.md](../../group-metric-constraints/manuscripts/rational-quotient-ranks-from-weak-oracles.md) resolves this issue. Fix an integer $`R\ge\log_2(DQ)`$ with $`R=O(\log(2D))`$, for example the bit length of $`DQ`$. Let
```math
\phi(t)=t-\frac{t^2}{4R}.
```
For every integer order $`N`$, deterministically approximate $`\phi(\log_2N)`$ to error at most $`1/(64R)`$ with one fixed dyadic denominator $`O(R)`$, assigning exactly zero to $`N=1`$. Multiplying these approximations by four produces an **exact rational** monotone submodular function $`F`$, with:

- exactly the same zero marginals and closed sets as $`f`$;
- every positive marginal at least one;
- rank at most $`4R`$;
- polynomial-bit values and evaluation, using the integer order from Section 5.

The proof creates a submodularity slack of at least $`1/(2R)`$ whenever both relevant rank increments are positive. If either increment vanishes, the values are equal in pairs, and the deterministic order-based approximations cancel exactly. This is why ordinary numerical approximation is sufficient here; no factorization or exact comparison of transcendental expressions is required.

Apply Quanrud's quotient sparsifier and the adaptive resparsification consequence in [../../label-block-cut/manuscripts/adaptive-quotient-resparsification.md](../../label-block-cut/manuscripts/adaptive-quotient-resparsification.md) to this exact rational rank. It retains
```math
O\!\left(
 \frac{R\log(2R/\eta)}{\eta^2}
 \right)
 \tag{CB28}
```
whole residual blocks while preserving every quotient, hence every physical character query (CB27).

Keep the same rational rank and common denominator through all restrictions. The fixed-denominator extension of the companion bit ledger gives polynomial accumulated weight encoding length. Submodular minimization now receives exact rational values. The denominator is not multiplied into the rank parameter of the support analysis.

Finally, sample the gapped part at error $`\eta\le\epsilon`$ and failure probability $`1/10`$, and set the classical procedure's constant success probability above $`9/10`$. Add the two relative PSD approximations and merge duplicate original indices. The combined success probability exceeds $`2/3`$; (CB13) and (CB28) prove Theorem 2.

All quantum algebra, block-conflict tests, normal forms, order evaluations, rational surrogate evaluations, and weight arithmetic are polynomial in the compact input. The Hilbert dimension enters the sample count only through $`\log D`$.

## 7. A matching multilevel lower bound

The modulus logarithm is necessary in the worst case, even for commuting two-local single-check blocks.

Let
```math
q=2^k,\quad k\ge1,\qquad
 0<\epsilon\le1/4,\qquad
 s=\lceil(2\epsilon)^{-2}\rceil,\quad B\ge s,\quad n=s+B.
```
Use $`n`$ registers of local dimension $`q`$, so $`D=q^n`$. For every edge $`uv`$ of $`K_{s,B}`$, and every level $`j=0,\ldots,k-1`$, include the original block
```math
B_{j,uv}
 =I-\Pi_{(Z_uZ_v^{-1})^{2^j},1},
 \qquad w_{j,uv}=3^j.
 \tag{CB29}
```
All checks commute. The level is part of the original item identity. The largest weight uses $`O(k)`$ bits.

Fix any Boolean cut vector $`b\in\{0,1\}^n`$. For
$`\ell=0,\ldots,k`$, use the computational basis assignment
```math
x_v=2^{k-\ell}b_v\pmod{2^k},
```
where $`\ell=0`$ is the all-zero assignment. The check at level $`j`$ violates exactly when $`uv`$ crosses the cut and $`j<\ell`$. Thus its original energy is
```math
W_\ell\,\mathrm{cut}_{K_{s,B}}(b),
 \qquad W_\ell=\sum_{j<\ell}3^j=\frac{3^\ell-1}{2}.
 \tag{CB30}
```

Let $`\widehat G_j`$ be the nonnegative weighted graph consisting of the output coefficients at level $`j`$. The spectral guarantee on these basis states implies
```math
\left|
 \sum_{j<\ell}\mathrm{cut}_{\widehat G_j}(b)
 -W_\ell\mathrm{cut}_{K_{s,B}}(b)
 \right|
 \le\epsilon W_\ell\mathrm{cut}_{K_{s,B}}(b).
 \tag{CB31}
```
Subtract the estimates for $`\ell=j+1`$ and $`\ell=j`$. Since
```math
W_{j+1}+W_j=2\cdot3^j-1<2\cdot3^j,
```
we obtain
```math
\left|
 \mathrm{cut}_{\widehat G_j}(b)
 -3^j\mathrm{cut}_{K_{s,B}}(b)
 \right|
 \le2\epsilon\,3^j\mathrm{cut}_{K_{s,B}}(b).
 \tag{CB32}
```
After division by $`3^j`$, each level is independently a weighted $`(1\pm2\epsilon)`$ cut sparsifier of $`K_{s,B}`$.

The complete-bipartite cut lower bound (EC15) in the companion exact-label-cut manuscript forces
$`\Omega(n/\epsilon^2)`$ retained original edges in **each** level. Therefore every successful output needs
```math
\Omega(nk/\epsilon^2)
 =\Omega(\log D/\epsilon^2)
 =\Omega(n\log q/\epsilon^2)
 \tag{CB33}
```
whole original blocks.

This allows arbitrary nonnegative output weights. It establishes the joint worst-case support order for composite dimensions along powers of two, in the regime $`n\ge2\lceil(2\epsilon)^{-2}\rceil`$. It does not assert that every fixed prime dimension needs an extra $`\log q`$ factor. The graph-cut lower bound is classical; the layered modular construction transfers it to this whole-check model.

## 8. Baselines and boundaries

**Companion results.** The prime-dimension whole-block theorem and the arbitrary-composite single-check theorem are the direct starting points. The present result permits entire joint acceptance projectors at arbitrary and heterogeneous local dimensions, proves the compact factorization-free construction through rationalized subgroup ranks, and supplies the joint modulus lower bound. The order oracle accounts for scalar relations rather than assuming a field basis.

**Quanrud, SODA 2024.** *Quotient Sparsification for Submodular Functions*, Theorem 1.1, already permits real-valued normalized monotone submodular ranks with all positive marginals at least one, and gives $`O(r\log(mr)/\epsilon^2)`$ support. Its entropy corollary is also explicit. The adaptive $`O(r\log(2r/\epsilon)/\epsilon^2)`$ consequence and finite-precision surrogate are stated in separate companion notes; they are not attributed as a new theorem of Quanrud. [Primary source](https://kentq.s3.amazonaws.com/submodular-sparsification.pdf).

**Basu--Brakensiek--Putterman, May 2026.** *Many Hamiltonians Are Sparsifiable* gives sparsification results for fixed-locality qubit Pauli terms and other local PSD classes. It is the checked quantum sparsification baseline. The present operator class consists of arbitrary-locality complements of joint Weyl acceptance spaces, with composite or heterogeneous local dimensions. A block is penalized once when any internal check fails, so replacing it by the sum of its check penalties changes the objective and output model. [Primary source](https://arxiv.org/html/2605.02211v1).

**Hostens--Dehaene--De Moor, 2005.** *Stabilizer States and Clifford Operations for Systems of Arbitrary Dimensions, and Modular Arithmetic* is standard background for compact arbitrary-dimensional Weyl and stabilizer algebra. The trace/character calculation and integer normal forms used here are classical tools. [Primary source](https://arxiv.org/abs/quant-ph/0408190).

**Kannan--Bachem, 1979.** *Polynomial Algorithms for Computing the Smith and Hermite Normal Forms of an Integer Matrix* supplies the polynomial-bit normal forms and transformation matrices used by the order oracle. [Primary source](https://doi.org/10.1137/0208040).

**Tropp, matrix concentration.** The gapped-component sampling is ordinary matrix Chernoff; it is not a new concentration theorem. [Primary source](https://arxiv.org/abs/1501.01571).

The sharper support theorem depends on the new whole-subgroup/affine-group Gaussian backend. The compact theorem depends instead on the rational quotient surrogate and the existing quotient-sparsification machinery. Neither theorem is a ground-state optimization algorithm, and neither extends to arbitrary projector-complement Hamiltonians lacking the Weyl overlap and subgroup structure.
