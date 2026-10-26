# Compact and optimal-support sparsification of whole stabilizer-check blocks

**Abstract.** Positive Hamiltonians whose original items are complements of prime-dimensional stabilizer acceptance spaces admit support $`O((n+1)\log p/\epsilon^2)`$ existentially. A compact randomized algorithm retains $`O((n+1)[\log p+\log((n+2)/\epsilon)]/\epsilon^2)`$ whole blocks, independent of locality and internal block size. A constant conflict gap permits balanced splitting into a uniformly positive part and a commuting finite-field block objective.

The [arbitrary-dimensional theorem](arbitrary-dimension-whole-stabilizer-blocks.md) also handles composite and heterogeneous dimensions. The prime-dimensional compact bound here remains a separate result: its additive dependence on $`\log p`$ can be smaller than the product of logarithms in the general-dimensional construction.

## Main result

Let $`p`$ be a prime. On $`n`$ qudits of local dimension $`p`$, let each input block specify an arbitrary finite collection of mutually commuting normalized Weyl checks. Their joint accepting subspace has orthogonal projection $`E_e`$. The input Hamiltonian is

```math
H=\sum_{e=1}^{m} w_e B_e,\qquad B_e=I-E_e,\qquad w_e\ge0.
\tag{SB1}
```

The penalty of a block is zero when **all** checks in that block are satisfied and one otherwise. Blocks may overlap arbitrarily, checks in different blocks need not commute, their locality is unrestricted, and a block can contain up to $`n`$ independent checks. The output must retain and reweight **whole original blocks**.

**Theorem SB.** For $`0<\epsilon<1`$, there is a randomized algorithm, polynomial in the compact input length, $`\epsilon^{-1}`$, and the rational weight encoding length, which succeeds with probability at least $`2/3`$ and returns nonnegative coefficients $`c_e`$ such that

```math
(1-\epsilon)H
\preceq \widetilde H:=\sum_e c_eB_e
\preceq(1+\epsilon)H,
\tag{SB2}
```

with support

```math
O\!\left(
\min\!\left\{
m,\,
\frac{n+1}{\epsilon^2}
\left[\log p+\log\!\left(\frac{n+2}{\epsilon}\right)\right]
\right\}
\right).
\tag{SB3}
```

No $`p^n`$-dimensional matrices or quantum states are constructed. For qubits, and more generally any fixed prime $`p`$, the bound is

```math
O\!\left(\frac{(n+1)\log((n+2)/\epsilon)}{\epsilon^2}\right).
\tag{SB4}
```

This extends the earlier single-check Pauli result to arbitrary stabilizer-subspace complements, with no factor for the number of checks within a block. The classical backend is an application of **Quanrud's existing quotient-sparsification theorem**, with the adaptive resparsification argument in 27_adaptive_quotient_resparsification.md. No new hedgegraph or classical code-sparsification priority claim is made.

The theorem deliberately states constant success probability. Stronger confidence can be obtained by adjusting the invoked sampling bounds, but no unchanged-support arbitrary-confidence claim is needed here.

**Theorem SB, optimal-order existence bound for fixed prime dimension.** Under the identical hypotheses, there also exists a nonnegative reweighting of whole original blocks satisfying (SB2) with support

```math
O\!\left(
\min\!\left\{m,\frac{(n+1)\log p}{\epsilon^2}\right\}
\right).
\tag{SB4a}
```

For fixed prime $`p`$, this is $`O(n/\epsilon^2)`$, matching the inherited joint lower bound in Section 7. The construction supplied by the proof of (SB4a) is polynomial in an explicitly listed $`p^{n+1}`$-row classical query table; no algorithm polynomial in the compact quantum input is claimed for this sharper bound. The compact polynomial-time guarantee remains (SB3).

The additional input is the **whole-subgroup sparsification theorem** proved in 30_optimal_whole_subgroup_constraints.md. Its Gaussian symmetrization argument retains entire block predicates. It does not expand a block into separately weighted characters or individual check penalties.

## 1. Compact model and preprocessing

A normalized Weyl operator $`U`$ has a label $`u\in\mathbb F_p^{2n}`$, satisfies $`U^p=I`$, and obeys

```math
UV=\omega^{[u,v]}VU,\qquad \omega=e^{2\pi i/p},
\tag{SB5}
```

where $`[u,v]`$ is the symplectic form. For odd $`p`$, use shift-clock tensor products with their scalar phase tracked modulo $`p`$. For $`p=2`$, use signed Hermitian Pauli strings, including the standard phase correction for $`Y`$. The representation is symbolic; roots of unity need not be numerically expanded.

Absorb each required eigenvalue $`\omega^a`$ into its check by replacing $`U`$ with $`\omega^{-a}U`$. For block $`e`$, with its mutually commuting normalized checks $`U_{e,1},\ldots,U_{e,k_e}`$, set

```math
E_e=\prod_{j=1}^{k_e}\Pi_{U_{e,j},1},
\qquad
\Pi_{U,1}=\frac1p\sum_{a=0}^{p-1}U^a.
\tag{SB6}
```

Finite-field elimination with phase tracking removes redundant checks. A dependency that produces a nonidentity scalar makes $`E_e=0`$, so $`B_e=I`$. All constant blocks can be represented exactly by one original constant block with their summed coefficient. A block with $`E_e=I`$ has zero penalty and is discarded. Every other block has a nonempty accepting subspace and at most $`n`$ projectively independent generators.

These operations, including testing whether two blocks contain a pair of noncommuting generators, require only polynomially many operations on $`O(n\log p)`$-bit Weyl labels. Scalar phases are computed by modular Weyl multiplication and repeated squaring, so the running time is polynomial in $`\log p`$, not in $`p`$.

## 2. Noncommuting blocks have a constant spectral gap

**Lemma SB1.** Suppose block $`e`$ contains a check $`U`$ and block $`f`$ contains a check $`V`$ with $`UV=\omega^aVU`$, $`a\ne0`$. Then

```math
\|E_eE_f\|\le p^{-1/2},
\qquad
B_e+B_f\succeq(1-p^{-1/2})I.
\tag{SB7}
```

**Proof.** Write $`P=\Pi_{U,1}`$ and $`Q=\Pi_{V,1}`$. For $`1\le j<p`$, the operator $`V^j`$ maps the $`1`$-eigenspace of $`U`$ into its $`\omega^{aj}`$-eigenspace. Thus $`PV^jP=0`$, and

```math
PQP=P/p,\qquad \|PQ\|=p^{-1/2}.
```

The accepting spaces of the two blocks lie in these individual eigenspaces. Hence

```math
E_eE_f=E_ePQE_f,\qquad \|E_eE_f\|\le\|PQ\|.
```

For orthogonal projections $`E,F`$, $`E+F\preceq(1+\|EF\|)I`$. Applying this inequality to $`E_e,E_f`$ and subtracting from $`2I`$ proves (SB7). $`\square`$

The bound depends on the prime dimension, but is bounded below by the absolute constant $`1-2^{-1/2}`$, independently of how many generators a block contains.

## 3. Balanced splitting leaves a commuting family of blocks

Maintain residual coefficients $`r_e=w_e`$ and peeled coefficients $`b_e=0`$. While two positive residual blocks contain a noncommuting pair of generators, let $`d=\min(r_e,r_f)`$, subtract $`d`$ from both residual coefficients, and add $`d`$ to both peeled coefficients.

Each step eliminates at least one positive residual coefficient, so at most $`m`$ steps occur. At termination, **every generator in every positive residual block commutes with every generator in every other residual block**. Write

```math
H=H_{\rm com}+H_{\rm gap},\qquad
H_{\rm com}=\sum_e r_eB_e,\quad
H_{\rm gap}=\sum_e b_eB_e,\quad W=\sum_e b_e.
\tag{SB8}
```

The exactly retained constant blocks may be added to $`H_{\rm com}`$. Summing Lemma SB1 over all balanced pairs gives

```math
H_{\rm gap}\succeq \beta_p W I,
\qquad
\beta_p=\frac{1-p^{-1/2}}2
\ge \frac{1-2^{-1/2}}2.
\tag{SB9}
```

Since $`0\preceq B_e\preceq I`$, the gapped part is easy to sample. If $`W>0`$, draw $`k`$ original block indices independently with probabilities $`b_e/W`$, assigning coefficient $`W/k`$ to every draw. Matrix Chernoff, applied only in the proof after whitening by $`H_{\rm gap}^{-1/2}`$, gives a relative $`1\pm\epsilon`$ approximation with failure probability at most $`\delta`$ when

```math
k=O\!\left(\frac{n\log p+\log(1/\delta)}{\epsilon^2}\right).
\tag{SB10}
```

For clarity, the normalized norm of each draw is at most $`1/(\beta_pk)`$, and the expected sum is the identity on dimension $`p^n`$. The algorithm uses only the scalar weights $`b_e`$, and never performs this whitening. If $`W=0`$, this component is absent.

## 4. The commuting blocks are affine linear-algebra queries

Choose a projectively independent basis $`Q_1,\ldots,Q_r`$ from all generators of the commuting residual family. Their projective span is isotropic, so $`r\le n`$. Each residual generator is exactly a scalar power of $`\omega`$ times a product of powers of these basis generators.

On a joint eigenvalue assignment $`Q_j=\omega^{x_j}`$, $`x\in\mathbb F_p^r`$, each block is represented by a matrix $`A_e`$ and a vector $`s_e`$, and has penalty

```math
B_e(x)=\mathbf1[A_ex+s_e\ne0].
\tag{SB11}
```

The right side is one if at least one equation in the block fails. Every simultaneous assignment occurs: expansion of the joint eigenspace projection has trace $`p^{n-r}`$, since nontrivial products of projectively independent Weyl operators are traceless. In particular, preserving the scalar functions (SB11) preserves the entire commuting Hamiltonian in Loewner order.

Homogenize by setting $`y=(x,1)`$ and $`M_e=[\,A_e\ \ s_e\,]`$. Let

```math
S_e=\mathrm{rowspan}_{\mathbb F_p}(M_e)
\subseteq\mathbb F_p^{d},\qquad d=r+1\le n+1.
\tag{SB12}
```

Then (SB11) is $`\mathbf1[M_ey\ne0]`$. Different blocks can have different numbers of rows and different row ranks.

The following entirely classical consequence of quotient sparsification is the backend.

## 5. Classical backend: quotient sparsification and resparsification

**Lemma SB2 (finite-field block queries).** Given arbitrary matrices $`M_e`$ with $`d`$ columns over $`\mathbb F_p`$ and arbitrary nonnegative weights $`w_e`$, there is a compact randomized polynomial-time algorithm returning nonnegative coefficients $`c_e`$, with

```math
\sum_e c_e\mathbf1[M_ey\ne0]
\in(1\pm\epsilon)\sum_e w_e\mathbf1[M_ey\ne0]
\quad\text{for every }y\in\mathbb F_p^d,
\tag{SB13}
```

and support

```math
O\!\left(
\frac{d\log(2d/\epsilon)}{\epsilon^2}
\right).
\tag{SB14}
```

Neither the number of rows within a block nor the field size appears in the support bound. Both contribute to the input reading and rank-query costs.

**Proof.** Remove zero matrices. On the original block ground set, define the integer-valued monotone submodular rank function

```math
f(T)=\dim_{\mathbb F_p}\left(\sum_{e\in T}S_e\right).
\tag{SB15}
```

Its rank is at most $`d`$, and its value oracle is ordinary finite-field elimination. For any query $`y`$, its zero-block set

```math
Z_y=\{e:M_ey=0\}
```

is closed for this rank function. Indeed, the span of the row spaces of zero blocks lies in $`y^\perp`$; any block contained in that span also vanishes on $`y`$. Therefore the active set $`\{e:M_ey\ne0\}`$ is a quotient, meaning the complement of a closed set.

Quanrud's Theorem 1.1 gives an $`O(d\log(2md)/\eta^2)`$-support sparsifier preserving the weight of **every quotient**, for arbitrary nonnegative input weights, in randomized polynomial time with oracle access to $`f`$. Every $`Z_y`$ intersected with a retained ground set remains closed by the identical row-span argument. Thus successive calls preserve all the same scalar queries.

Apply the adaptive resparsification lemma in 27_adaptive_quotient_resparsification.md. For completeness, while the current size $`m_i`$ exceeds a fixed polynomial in $`d/\epsilon`$, choose a pass error proportional to
```math
\epsilon\sqrt{\frac{\log(2d/\epsilon)}{\log m_i}}.
```
The next size is $`O(d\epsilon^{-2}(\log m_i)^2/\log(2d/\epsilon))`$, which is at most $`\sqrt{m_i}`$ above a sufficiently large polynomial threshold. The preliminary errors sum to less than $`\epsilon/8`$, because they increase geometrically as $`\log m_i`$ decreases. One final call at error $`\epsilon/4`$ gives (SB14), with total relative error at most $`\epsilon`$.

The cited companion provides the exact threshold, the error product, and the confidence ledger. Preliminary call failures are bounded by fixed inverse powers of $`m_i`$; their sum is bounded by a geometric series read backward through the square-root shrinkage. Together with the final call, the whole classical procedure can be set to succeed with probability above $`9/10`$.

Every call uses a polynomial-time finite-field rank oracle. No vectors $`y`$, failure scenarios, or row spaces absent from the input are enumerated. The number of calls is $`O(\log\log(2m))`$, and the rational threshold weights have polynomial accumulated bit length, as detailed in the companion. If the support bound exceeds the number of input blocks, retain them all. $`\square`$

**Attribution.** The rank-function quotient reduction and resparsification consequence are stated here to make the imported backend precise. In particular, a near-linear hedgegraph sparsifier is already known from the 2025 hedgegraph-polymatroid work; this lemma is not used to claim an improvement for hedgegraph cuts.

### 5.1 An alternative backend for the sharper existence bound

**Lemma SB3 (whole-block support existence).** For the same weighted matrices $`M_e`$, there are coefficients satisfying (SB13) on

```math
O\!\left(\min\{m,d\log p/\epsilon^2\}\right)
\tag{SB16}
```

whole original blocks.

**Proof.** Take the additive group $`G=\mathbb F_p^d`$ and the subgroup $`H_e=\ker M_e`$ for each block. Then
$`\mathbf1[M_ey\ne0]=\mathbf1[y\notin H_e]`$.
The whole-subgroup theorem applies to arbitrary subgroups and arbitrary nonnegative input weights, and gives support $`O(\log(2|G|)/\epsilon^2)=O(d\log p/\epsilon^2)`$ for $`d\ge1`$. Zero blocks are discarded. Every retained item is an original matrix block, irrespective of its rank. The affine restriction $`y=(x,1)`$ in Section 4 is a subset of the queries already preserved. $`\square`$

The companion proves the needed theorem using a hereditary one-sided Gaussian bound of $`1/|G|`$, Gaussian symmetrization, and ordinary partial coloring. With all $`p^d`$ query rows listed, its separation oracle scans the defining inequalities. This is the source of the exponential-in-$`d\log p`$ table in the stated construction. Lemma SB3 is not substituted for Lemma SB2 in the compact polynomial-time algorithm.

## 6. Completing the quantum algorithm

Apply Lemma SB2 to the commuting residual family using its original block identities. Restrict (SB13) to $`y=(x,1)`$ and simultaneously diagonalize the commuting generators to obtain a relative spectral approximation of $`H_{\rm com}`$.

Independently sample the gapped part with $`\delta=1/10`$ in (SB10). Set the entire classical procedure's success probability above $`9/10`$. A union bound gives overall success greater than $`2/3`$.

The relative inequalities for the two positive semidefinite components add directly. When a block was split between the two components, add its two output coefficients. Hence the output is a nonnegative reweighting of **whole original blocks**, as required.

The commuting support from (SB14) is

```math
O\!\left(
\frac{(n+1)\log((n+2)/\epsilon)}{\epsilon^2}
\right).
```

Adding (SB10) proves (SB3). The remaining $`\log p`$ contribution comes entirely from matrix concentration for the noncommuting component. One exactly retained constant block is absorbed by the $`n+1`$ term.

All Weyl algebra and all rank computations take place over compact finite-field labels. Each block's independent generators are computable in polynomial time. There are at most $`m`$ balanced subtraction steps, and the rational weights produced by them have polynomial encoding length. The classical calls use weighted, integer-rank instances of Quanrud's theorem. Standard rational implementations can use slack in $`\epsilon`$ when choosing sampling thresholds; their arithmetic involves rank values and scalar weights, not matrices over a cyclotomic field of dimension $`p`$.

To prove the stronger existence bound (SB4a), keep the same balanced splitting and the same $`O(n\log p/\epsilon^2)`$-term gapped-component sample, and use Lemma SB3 for the commuting residual family. Its homogeneous dimension is $`d\le n+1`$, so its support is $`O((n+1)\log p/\epsilon^2)`$. The two relative semidefinite inequalities again add, and coefficients on duplicate original blocks again merge. This proves (SB4a). The sharper classical backend affects only the commuting component; all block identities and the whole-block output requirement remain intact.

## 7. Lower bounds and model scope

For fixed prime dimension, the theorem gives $`O(n\log(n/\epsilon)/\epsilon^2)`$ retained blocks uniformly over unrestricted locality and unrestricted internal block size. The distinction from single Pauli checks is substantive: a block is penalized once when any of its internal equations fails, and its individual check penalties cannot be substituted for the block while preserving the original operator or output model.

Even individual commuting checks can require all $`n`$ terms: the $`n`$ separate requirements $`Z_i=1`$ are individually witnessed by computational basis states violating just one requirement.

There is also an inherited joint lower bound $`\Omega(n/\epsilon^2)`$, for $`0<\epsilon\le1/2`$ and $`n\ge2\lceil\epsilon^{-2}\rceil`$. Put $`s=\lceil\epsilon^{-2}\rceil`$, $`B=n-s\ge s`$, and assign one single-generator block $`I-\Pi_{Z_uZ_v^{-1},1}`$ to each edge $`uv`$ of $`K_{s,B}`$. On computational basis symbols restricted to $`\{0,1\}\subseteq\mathbb F_p`$, each block is exactly that edge's Boolean crossing indicator. Therefore any spectral whole-block sparsifier is also a cut sparsifier of $`K_{s,B}`$; equation (EC15) in 28_exact_label_cut_and_matroid_quotient_sparsification.md forces $`\Omega(B/\epsilon^2)=\Omega(n/\epsilon^2)`$ original blocks. All these checks commute and are two-local. This is the inherited classical cut lower bound. Thus for fixed $`p`$, (SB4a) is jointly optimal in $`n`$ and $`\epsilon`$ in this regime, whereas the compact polynomial-time support is optimal up to its logarithm. No matching lower bound for the $`\log p`$ factor is asserted.

This does not imply sparsifiability of arbitrary projector-complement Hamiltonians. The argument uses both the constant overlap gap between conflicting stabilizer checks and the finite-field description of the commuting residual family. It also does not produce a ground-state optimizer.

The earlier $`O(n/\epsilon^2)`$ existential bound for single qubit checks therefore extends to whole stabilizer-subspace-complement blocks, with no internal-block-size loss. The compact algorithm also extends to this larger operator class, at its stated logarithmic overhead.

## 8. Primary sources and baseline boundary

* **Kent Quanrud, SODA 2024, _Quotient sparsification for submodular functions_.** Theorem 1.1: arbitrary weighted integral monotone submodular rank $`r`$, ground-set size $`m`$, support $`O(r\log(mr)/\epsilon^2)`$, randomized polynomial time with a value oracle. This is the classical sparsification input to Lemma SB2. Primary manuscript: <https://kentq.s3.amazonaws.com/submodular-sparsification.pdf>. Publication: <https://doi.org/10.1137/1.9781611977912.187>.

* **Chandrasekaran, Chekuri, Wang, Zhu, 2025, _Hedgegraph Polymatroids_.** Theorem 7 already supplies weighted hedgegraph partition sparsifiers with $`O(n\log n/\epsilon^2)`$ support in randomized polynomial time. Section 6 makes explicit the quotient-sparsification connection. Primary source: <https://arxiv.org/html/2510.25043v1>.

* **Basu, Brakensiek, Putterman, May 2026, _Many Hamiltonians Are Sparsifiable_.** Theorem 3.5 gives fixed-locality qubit Pauli sparsification; the result here uses arbitrary stabilizer-block complements and has no locality parameter. The individual penalties and output model should be compared literally, without treating a sum of individual checks as one block. Primary source: <https://arxiv.org/html/2605.02211v1>.

* **Hostens, Dehaene, De Moor, 2005, _Stabilizer states and Clifford operations for systems of arbitrary dimensions, and modular arithmetic_.** Standard compact Weyl/stabilizer algebra background. Primary source: <https://arxiv.org/abs/quant-ph/0408190>.

* **Joel Tropp, _An Introduction to Matrix Concentration Inequalities_.** Matrix Chernoff is used for the constant-gap component. Primary source: <https://arxiv.org/abs/1501.01571>.

* **Brakensiek, Guruswami, Putterman, May 2026, _Multiplicative error set system sparsification: A simpler proof via chain length contraction_.** Theorem 1.2 supplies the stronger general set-system baseline $`O(c\log^2(c/\epsilon)(\log\log(c/\epsilon))^2/\epsilon^2)`$, where $`c`$ is chain length; for finite-field whole-block queries $`c\le d`$. This supersedes the older $`\log^6m`$ overhead of Brakensiek--Guruswami's group-code theorem. The new Gaussian companion removes this remaining logarithmic overhead for fixed-field subgroup blocks, and its broader group statement is compared separately there. Primary source: <https://arxiv.org/abs/2605.01508>.

* **Companion manuscript, _Optimal-support sparsification of whole subgroup constraints_.** 30_optimal_whole_subgroup_constraints.md supplies the new whole-subgroup theorem used only for (SB4a). Its proof depends on standard Gaussian comparison, the Reis--Rothvoss partial-coloring theorem, and a stated Gaussian version of their hereditary-section symmetrization argument. The compact polynomial-time bound (SB3) does not depend on this new lemma.

The quantum results are the whole-block constant-gap decomposition with the compact quotient backend, and its sharper support-existence consequence from the Gaussian whole-subgroup theorem. The two construction guarantees use different classical backends and remain separate throughout the proof.
