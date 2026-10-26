# Arbitrary-dimensional Weyl eigenvalue checks

**Abstract.** Positive eigenvalue checks on arbitrary-dimensional registers are the single-generator case of whole stabilizer-block sparsification. We give the resulting strongest support and compact construction bounds, including the dependence on binary-encoded composite dimension. The proof preserves whole original checks and requires no prime factorization.

## 1. Compact model

Let $q\ge2$, $Q=2q$, and $\tau=e^{2\pi i/Q}$. On $n$ registers of local dimension $q$, an input check is specified by

$$
U_e=\tau^{c_e}X^{a_e}Z^{b_e},\qquad
 a_e,b_e\in\mathbb Z_q^n,\quad c_e\in\mathbb Z_Q.
 \tag{C1}
$$

Here $X|z\rangle=|z+1\rangle$, $Z|z\rangle=e^{2\pi iz/q}|z\rangle$, and the vectors specify tensor products. A requested $Q$-th-root eigenvalue is absorbed into the phase. Every such operator has $U_e^Q=I$, including for even $q$. Define

$$
P_e=\Pi_{U_e,1}=Q^{-1}\sum_{j=0}^{Q-1}U_e^j,
 \qquad B_e=I-P_e,
 \qquad H=\sum_{e=1}^m w_eB_e,
 \tag{C2}
$$

with nonnegative rational weights. The accepted eigenspace may be empty, giving $B_e=I$, or the entire space, giving a zero clause. The phases, displacement vectors, dimensions, and weights form the compact input. The total Hilbert dimension is $D=q^n$, and put $\rho=\log_2(2D)$.

## 2. Support and construction theorem

**Theorem C.** For $0<\epsilon<1$, there is a nonnegative reweighting of original checks satisfying

$$
(1-\epsilon)H\preceq\sum_e\widehat w_eB_e
 \preceq(1+\epsilon)H.
 \tag{C3}
$$

A randomized algorithm polynomial in the compact binary input length and $\epsilon^{-1}$, with success probability at least $2/3$, obtains support

$$
O\!\left(\min\left\{m,
 \frac{\rho\log(2\rho/\epsilon)}{\epsilon^2}\right\}\right).
 \tag{C4}
$$

An output also exists with support

$$
O\!\left(\min\{m,\rho/\epsilon^2\}\right).
 \tag{C4'}
$$

The construction supplied for (C4') is randomized polynomial in $D$ and the remaining input and accuracy parameters. It may therefore be exponential in the compact input. The compact algorithm for (C4) uses integer normal forms and does not factor $q$ or materialize a $D$-dimensional matrix.

**Proof.** Treat each check as a block containing its single Weyl generator in [the arbitrary-dimensional whole-block theorem](arbitrary-dimension-whole-stabilizer-blocks.md), and set every local dimension equal to $q$. Its phase modulus becomes $2\operatorname{lcm}(q,\ldots,q)=2q=Q$; its block penalty is exactly (C2). Theorems 1 and 2 of that manuscript give (C4') and (C4), respectively, with the same original item identities and weights. This proves every claimed support, representation, probability, and running-time assertion. $\square$

For clarity, the composite-dimensional algebra does not use a field basis. If $UV=\zeta VU$ and the nontrivial scalar commutator has order $t$, then

$$
\Pi_{U,1}\Pi_{V,1}\Pi_{U,1}
 =t^{-1}\Pi_{U,1}\Pi_{V^t,1}\Pi_{U,1}
 \preceq t^{-1}\Pi_{U,1}.
 \tag{C5}
$$

To verify this, average the $Q$ powers of $V$. Every term whose exponent is not divisible by $t$ changes the $U$-eigenvalue and vanishes after sandwiching. Thus a conflicting pair of check penalties has an absolute lower spectral gap. Balanced subtraction separates a uniformly positive part from a commuting remainder. The commuting subgroup's scalar relations and displacement lattice are retained by the exact subgroup-order oracle; closure-preserving rationalization then supplies the compact quotient backend. These are the full proof's steps that require care at composite $q$.

## 3. Dependence on the local dimension

Theorem C gives support $O(n\log(2q)/\epsilon^2)$ existentially and

$$
O\!\left(
 \frac{n\log(2q)}{\epsilon^2}
 \log\frac{2n\log(2q)}{\epsilon}
 \right)
$$

for the compact construction, always capped by $m$. The bound has no locality, clause-order, or weight-ratio factor.

For $q=2^k$, $0<\epsilon\le1/4$, and $n\ge2\lceil(2\epsilon)^{-2}\rceil$, the layered modular cut construction in [Section 7 of the whole-block theorem](arbitrary-dimension-whole-stabilizer-blocks.md) already uses individual commuting checks and forces $\Omega(n\log q/\epsilon^2)$ retained items. Hence the existential order is jointly necessary in that regime.

When the dimension is known to be prime, the compact whole-block construction in [the prime-dimensional theorem](arbitrary-locality-stabilizer-block-sparsification.md) can be smaller:

$$
O\!\left(\min\left\{m,
 \frac{(n+1)[\log q+\log((n+2)/\epsilon)]}{\epsilon^2}
 \right\}\right).
$$

The prime and general-dimensional construction bounds are therefore kept distinct. Neither asserts that the $\log q$ dependence is necessary for every prime dimension. The guarantee concerns the eigenvalue-check penalty $I-\Pi_{U,1}$; the different energy $I-(U+U^*)/2$ has a different spectral analysis.

## 4. References

The complete proof, including character multiplicities, normal-form order queries, bit complexity, and the lower-bound construction, is in [Whole stabilizer-block sparsification in arbitrary local dimensions](arbitrary-dimension-whole-stabilizer-blocks.md). Its quotient-rank surrogate is proved in [Rational quotient ranks from weak value oracles](../../group-metric-constraints/manuscripts/rational-quotient-ranks-from-weak-oracles.md).

- Hostens, Dehaene, and De Moor, *Stabilizer States and Clifford Operations for Systems of Arbitrary Dimensions, and Modular Arithmetic*, Physical Review A 71 (2005): <https://arxiv.org/abs/quant-ph/0408190>.
- Kannan and Bachem, *Polynomial Algorithms for Computing the Smith and Hermite Normal Forms of an Integer Matrix*, SIAM Journal on Computing 8 (1979): <https://doi.org/10.1137/0208040>.
- Quanrud, *Quotient Sparsification for Submodular Functions*, SODA 2024, Theorem 1.1: <https://kentq.s3.amazonaws.com/submodular-sparsification.pdf>.
