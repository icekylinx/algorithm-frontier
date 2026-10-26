# Rational quotient ranks from weak value oracles

**Abstract.** We replace a normalized monotone submodular function with a unit positive-marginal gap by an exact rational function having the same closure operator, the same unit gap, and only a constant-factor increase in total rank. The construction uses deterministic approximate values and canonical closure keys. A strictly concave transform creates enough submodularity slack to tolerate rounding. This gives polynomial-bit quotient sparsification for logarithmic finite-subgroup ranks without factoring their orders.

## 1. Statement

Let $E$ be a ground set of $m$ elements. Let
$$
f:2^E\longrightarrow\mathbb R_{\ge0}
$$
be normalized, monotone, and submodular, and assume
$$
f(S+e)-f(S)\in\{0\}\cup[1,\infty)
 \qquad(S\subseteq E,\ e\in E).
 \tag{R1}
$$
Suppose a deterministic weak value oracle returns rational approximations to $f(S)$ to any requested additive precision. Let $R\ge1$ be a known integer with $f(E)\le R$.

**Theorem 1.** There is a deterministic exact rational value oracle for a function $F:2^E\to\mathbb Q_{\ge0}$ such that:

1. $F$ is normalized, monotone, and submodular.
2. $F$ has exactly the same zero marginals, and hence exactly the same closure operator and quotient family, as $f$.
3. Every positive marginal of $F$ is at least one, and $F(E)\le4R$.
4. All values of $F$ have a common denominator $O(R)$.
5. One evaluation uses $O(m)$ weak calls at constant precision and one weak call at additive precision $1/\mathrm{poly}(R)$, followed by polynomial-bit rational arithmetic.

Thus, if the weak oracle is polynomial time in the input length and the requested precision in bits, so is the exact rational oracle for $F$. This is an exact oracle for a different function preserving the quotient structure; it is not an exact oracle for the original real-valued $f$.

When $f(S)=\log_2 \nu(S)$ and $\nu(S)$ is an exactly computable positive integer, one may use the integer $\nu(S)$ directly as the canonical key. This avoids the $O(m)$ closure calls and gives the logarithmic subgroup-order specialization in Section 4.

## 2. Exact closure from approximate values

Define
$$
\mathrm{cl}_f(S)
 =\{e\in E:f(S+e)=f(S)\}.
 \tag{R2}
$$
Approximate $f(S)$ and each $f(S+e)$ to additive error $1/8$. The approximate marginal is in $[-1/4,1/4]$ if the true marginal is zero, and is at least $3/4$ if it is positive. Comparing it to $1/2$ therefore computes (R2) exactly.

We use two standard consequences of monotonicity and submodularity, included here to fix the exact cancellation requirement.

First,
$$
f(\mathrm{cl}_f(S))=f(S).
 \tag{R3}
$$
Indeed, every element added in the closure has marginal zero at $S$, and diminishing returns keeps that marginal zero as the other closure elements are added.

Second, for nested sets $S\subseteq T$,
$$
f(S)=f(T)
 \quad\Longrightarrow\quad
 \mathrm{cl}_f(S)=\mathrm{cl}_f(T).
 \tag{R4}
$$
One inclusion follows from monotonicity of closure. For the other, if $f(T+e)=f(T)=f(S)$, then monotonicity gives $f(S+e)\le f(T+e)=f(S)$, so $e\in\mathrm{cl}_f(S)$.

Represent every closure by its canonical bit vector in the original ground-set order. Repeated evaluations on the same closure will therefore use the identical input to the deterministic weak oracle.

## 3. A strict concave transform makes rounding safe

Set
$$
\phi(t)=t-\frac{t^2}{4R}.
 \tag{R5}
$$
It is increasing on $[0,2R]$, and its derivative lies in $[1/2,1]$ on $[0,R]$.

For each closed set $C$, deterministically choose a rational $A(C)$ satisfying
$$
|A(C)-\phi(f(C))|\le\delta,
 \qquad \delta=\frac1{64R}.
 \tag{R6}
$$
Use the same value on repeated occurrences of the same $C$, and set
$$
A(\mathrm{cl}_f(\varnothing))=0.
 \tag{R7}
$$
Define
$$
F(S)=4A(\mathrm{cl}_f(S)).
 \tag{R8}
$$

### Monotonicity and the marginal gap

For $S\subseteq T$, if $f(S)=f(T)$, equation (R4) makes their rounded values identical. If $f(T)>f(S)$, a chain of single-element additions and (R1) gives $f(T)-f(S)\ge1$. Therefore
$$
\phi(f(T))-\phi(f(S))\ge\frac12.
$$
The two approximation errors yield
$$
F(T)-F(S)
 \ge4\left(\frac12-2\delta\right)>1.
 \tag{R9}
$$
Thus $F$ is monotone, has precisely the same zero marginals, and has positive marginals greater than one. Equations (R3) and (R7) give $F(\varnothing)=0$. Monotonicity then also gives nonnegativity.

Since $\phi(t)\le3R/4$ on $[0,R]$,
$$
F(E)\le3R+4\delta\le4R.
 \tag{R10}
$$

### Submodularity

For arbitrary sets $S,T$, write
$$
I=S\cap T,\quad U=S\cup T,\quad
 c=f(I),\quad
 a=f(S)-c,\quad b=f(T)-c.
$$
If $a=0$, submodularity and monotonicity imply $f(U)=f(T)$. Equation (R4) gives
$$
\mathrm{cl}_f(S)=\mathrm{cl}_f(I),
 \qquad
 \mathrm{cl}_f(U)=\mathrm{cl}_f(T).
$$
The rounded submodularity expression is exactly zero. The case $b=0$ is identical.

Otherwise $a,b\ge1$, by (R1). Submodularity gives
$$
f(U)\le c+a+b,
 \qquad c+a+b=f(S)+f(T)-f(I)\le2R.
$$
Because $\phi$ is increasing on this larger interval,
$$
\begin{aligned}
 &\phi(f(S))+\phi(f(T))-\phi(f(U))-\phi(f(I))\\
 &\qquad\ge
 \phi(c+a)+\phi(c+b)-\phi(c+a+b)-\phi(c)\\
 &\qquad=\frac{ab}{2R}\ge\frac1{2R}.
\end{aligned}
 \tag{R11}
$$
The four rounding errors cost at most $4\delta=1/(16R)$, which is strictly smaller than this gap. Hence
$$
F(S)+F(T)\ge F(U)+F(I).
 \tag{R12}
$$
This proves exact submodularity. Arbitrarily close comparisons between unrelated real function values never need to be resolved.

### A common small dyadic denominator

Take a fixed power of two $\Delta$ with
$$
1024R\le\Delta<2048R.
$$
For a closure $C$, obtain a deterministic rational approximation $u_C$ to $f(C)$ with error at most $1/(1024R)$, and clip it to $[0,R]$. Evaluate $\phi(u_C)$ exactly as a rational number, then round down to a multiple of $1/\Delta$. Force the value in (R7) to zero.

Since $\phi$ is 1-Lipschitz on $[0,R]$, the total error is at most $2/(1024R)<\delta$. Every resulting $F(S)$ is a multiple of $4/\Delta$, has $O(\log R)$ bits apart from its bounded numerator, and is computed without deciding on which side of an exact transcendental rounding threshold the true value lies. The algorithm rounds a specified rational approximation; (R11) makes that choice safe.

If a suitable $R$ is not supplied, take a weak evaluation $\widetilde f(E)$ with additive error at most $1/8$, and set $R=\max\{1,\lceil\widetilde f(E)+1/8\rceil\}$. Then $f(E)\le R\le f(E)+2$. This preserves the rank order whenever $f(E)>0$, because (R1) then implies $f(E)\ge1$.

## 4. Logarithmic subgroup ranks without factoring

Let $A$ be a finite abelian group, and let each original item specify a subgroup $J_e\le A$. Put
$$
H_S=\sum_{e\in S}J_e,\qquad f(S)=\log_2|H_S|.
 \tag{R13}
$$
This is a normalized monotone submodular function. For subgroups $B,C\le A$,
$$
|B+C|\,|B\cap C|=|B|\,|C|,
$$
and $H_{S\cap T}\subseteq H_S\cap H_T$, which proves the submodular inequality for (R13). Every positive marginal is at least one, because a proper subgroup inclusion has integer index at least two.

If $|H_S|$ can be computed exactly in polynomial time, evaluate a deterministic approximation to
$$
\phi(\log_2|H_S|)
$$
using the integer order as the canonical key. Equal orders receive identical approximate values. In the zero-gap cases of the submodularity proof, the needed orders are equal in pairs, so the proof above applies directly. No factorization of the subgroup order is required.

An explicit approximation procedure is elementary. Write $N=2^k u$, with $1\le u<2$ rational. For
$$
z=\frac{u-1}{u+1}\in[0,1/3],
$$
use
$$
\log u=2\sum_{j\ge0}\frac{z^{2j+1}}{2j+1}.
$$
The same series at $z=1/3$ gives $\log2$. $O(\log R)$ terms, with their geometric tail bounds, give a certified approximation to $\log_2N=k+\log u/\log2$ of the precision needed above. The rational arithmetic has polynomial bit complexity in $\log N$ and $\log R$.

For modular row blocks in $\mathbb Z_q^d$, the subgroup orders in (R13) are lattice indices computable by Hermite or Smith normal form. For commuting Weyl blocks, the order oracle additionally includes the scalar phase subgroup; the exact construction is given in [../../quantum-stabilizer/manuscripts/arbitrary-dimension-whole-stabilizer-blocks.md](../../quantum-stabilizer/manuscripts/arbitrary-dimension-whole-stabilizer-blocks.md).

There is another useful application that permits nonabelian groups: for arbitrary subgroups $K_e\le G$,
$$
f(S)=\log_2\!\left[G:\bigcap_{e\in S}K_e\right]
 \tag{R14}
$$
is the joint entropy of the coset variables $gK_e$ for uniform $g$. It is submodular, and its positive marginals are at least one. Whenever the relevant indices have a compact polynomial-time exact oracle, the same rationalization applies. This does not claim that arbitrary nonabelian subgroup intersections are efficiently computable from arbitrary succinct presentations.

The qualification is necessary: $\log|\langle J_e:e\in S\rangle|$ need not be submodular for arbitrary noncommuting subgroups. The generated-subgroup form (R13) uses an abelian ambient group; the entropy form (R14) has a different proof and remains valid for nonabelian groups.

## 5. Consequence for polynomial-bit quotient sparsification

Quanrud's SODA 2024 Theorem 1.1 explicitly accepts normalized real-valued monotone submodular functions with every positive marginal at least one. It does not require integral ranks. Applying it to the exact rational $F$ above preserves exactly the quotient family of $f$ and gives
$$
O\!\left(\frac{R\log(2mR)}{\epsilon^2}\right)
$$
retained original items. The adaptive resparsification argument in [../../label-block-cut/manuscripts/adaptive-quotient-resparsification.md](../../label-block-cut/manuscripts/adaptive-quotient-resparsification.md) improves this to
$$
O\!\left(\min\left\{m,
       \frac{R\log(2R/\epsilon)}{\epsilon^2}\right\}\right).
 \tag{R15}
$$
Both constructions now have an exact rational value oracle, with polynomial-bit submodular minimization and strength arithmetic, rather than a symbolic logarithmic oracle.

The fixed denominator must **not** be multiplied into the rank parameter of the support bound. The theorem already permits rational values with the stated marginal gap. Internally, rational submodular minimization can of course clear denominators as an arithmetic operation; this does not change the rank used in the sparsification analysis.

Use the same original function $F$, the same upper bound $R$, and the same denominator $\Delta$ throughout all restrictions and repeated calls. In the closure-key implementation, the canonical closure is always computed in the original ground set; this defines one fixed function whose restrictions are passed to the backend.

For completeness, the repeated weight-update ledger remains polynomial. A positive rank difference is a rational number with the fixed denominator $\Delta$ and numerator $O(R\Delta)$. Thresholds in Quanrud's strength decomposition have the form
$$
\tau=\theta\,
 \frac{w(U)-w(V)}{F(U)-F(V)},
$$
with $\theta$ chosen dyadic within a fixed constant factor of the analytic threshold multiplier. Writing the rank difference as $a/\Delta$, the threshold is $\theta\Delta(w(U)-w(V))/a$: the common rank denominator enters only the numerator. If current weights have a common denominator, one pass enlarges it by a product of at most $m_i$ integers of size $O(R\Delta)$, and the dyadic parameter denominator. The increase in bit length is polynomial. The adaptive sequence uses only polynomially many such operations and calls. Exact rational sampling, or finite-bit sampling with an allocated constant failure budget, therefore preserves the stated compact polynomial-time contract.

## 6. References and scope

The public input is Kent Quanrud, *Quotient Sparsification for Submodular Functions*, SODA 2024, Theorem 1.1 and Section 3. Its real-valued hypothesis and the entropy application are already explicit in the paper. [Primary source](https://kentq.s3.amazonaws.com/submodular-sparsification.pdf).

Closure theory, concave composition of monotone submodular functions, and polynomial-time integer normal forms are standard. The contribution is the quantitative concave transform, canonical-key rounding, and resulting exact rational quotient surrogate, which closes the finite-precision gap for logarithmic subgroup ranks. The support improvement obtained by adaptive repeated calls is recorded separately and is a standard resparsification consequence, not a new public theorem attributed to Quanrud.

The construction preserves zero marginals and quotient queries. It need not preserve the exact numerical rank values, optimal bases of an unrelated optimization problem, or every property of the original real-valued submodular function.
