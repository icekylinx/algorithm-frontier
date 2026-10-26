# Exact Boolean convolution with elementary bit arithmetic

**Lemma.** Two Boolean arrays of length at most $`C\ge1`$ have their
integer linear convolution computable deterministically in
$`C\,\mathrm{poly}(\log(C+2))`$ bit operations and writable bits.
Only integer addition, multiplication and division on polynomially many
bits in $`\log(C+2)`$ are required. No prime search, floating-point oracle
or fast multiplication theorem is an assumption.

This supplies the convolution primitive used by the
[short-range Subset Sum theorem](range-branch.md). The inputs to this
primitive are occupancy bits; their original subset witnesses remain
in the corresponding slot arrays.

## 1. Exact transform identity

Choose a power of two $`M`$ with $`2C\le M<4C`$ and pad the two arrays
with zeros. Write $`\omega=\exp(2\pi\mathrm i/M)`$. The geometric sum

```math
\sum_{j=0}^{M-1}\omega^{jr}=
\begin{cases}M,&M\mid r,\\0,&M\nmid r\end{cases}
```

proves that the product of the two transforms, followed by the transform
with conjugate roots and division by $`M`$, is their cyclic convolution.
The zero padding makes its first $`2C-1`$ entries the linear convolution.
The result is an integer in $`[0,C]`$ at each coordinate.

Splitting a transform sum into even and odd indices gives the two
butterflies $`a+\omega^j b`$ and $`a-\omega^j b`$. Recursing for
$`\log_2M`$ levels uses $`O(M\log M)`$ additions and multiplications.
The subsequent construction approximates these operations with a proved
error smaller than the distance from an integer to its rounding boundary.

## 2. Deterministic roots with no transcendental input

Put

```math
P=16+6\log_2M,\qquad \delta=2^{-P},\qquad K=8P.
```

All are explicit integers or dyadic rationals. For rational $`x\in(0,1)`$,
let

```math
A_P(x)=\sum_{j=0}^{P-1}\frac{(-1)^j x^{2j+1}}{2j+1},\qquad
\widetilde\pi=16A_P(1/5)-4A_P(1/239).
```

The alternating series and the tangent addition formula give

```math
\pi=16\arctan(1/5)-4\arctan(1/239),\qquad
|\widetilde\pi-\pi|
\le\frac{20}{5^{2P+1}}\le2^{2-4P}<\delta/16.
```

For clarity, the identity uses
$`\tan(4\arctan(1/5))=120/119`$; subtracting
$`\arctan(1/239)`$ gives tangent one. The angle is positive and less
than $`4/5`$, while $`\pi/2=2\arctan(1)\ge1`$ by integrating
$`1/(1+x^2)\ge1/2`$ on $`[0,1]`$. Thus it lies in the principal
interval and equals $`\pi/4`$.
The same alternating-series bounds give $`0<\widetilde\pi<16/5<4`$.
All terms and the resulting rational are computed exactly.

For each needed twiddle angle $`2\pi j/m`$, with $`m\mid M`$ and
$`0\le j<m/2`$, put $`\theta=2\widetilde\pi j/m`$. Its error is
less than $`\delta/16`$, and $`|\theta|<4`$. Approximate
$`\exp(\mathrm i\theta)`$ by the degree-$`K`$ Taylor polynomial.
Taylor's integral remainder has norm at most

```math
\frac{4^{K+1}}{(K+1)!}
\le4(4/P)^{4P}\le2^{2-8P}<\delta/16.
```

The factorial bound keeps its last $`K/2`$ factors. The displayed
comparison uses $`P\ge16`$.

The polynomial can be evaluated with bounded-size arithmetic. Use a
work grid of spacing $`\delta'=2^{-(P+16)}`$, start at $`z=1`$, and
for $`k=K,K-1,\ldots,1`$ replace $`z`$ by
$`1+(\mathrm i\theta/k)z`$, rounding each real component to this grid.
Without rounding this is exactly the truncated Taylor polynomial.
Each local complex rounding error is at most $`2\delta'`$. Its
amplification toward the output is bounded by a prefix of
$`1,|\theta|,|\theta|^2/2!,\ldots`$, whose sum is at most
$`e^4<64`$. The total evaluation error is therefore less than
$`128\delta'=\delta/512`$.

Round the resulting real and imaginary components to the coarser
$`\delta`$ grid. The final rounding has complex error at most $`\delta`$.
The angle perturbation, Taylor remainder, work-grid errors and final
rounding together are less than $`2\delta`$. We use the conservative
bound

```math
|\widetilde\omega-\omega|\le4\delta.
\tag{1}
```

Conjugation supplies inverse roots with the same error. Rational
arctangent partial sums have $`\mathrm{poly}(P)`$-bit numerator and
denominator. The Horner recurrence uses them with $`O(P)`$-bit fixed-grid
values; each rounded division is exact integer arithmetic. The intermediate
Horner polynomials have magnitude at most $`e^4`$, since each denominator
product is at least the corresponding factorial; their accumulated
rounding errors obey the same bound as above. Thus one
root costs $`\mathrm{poly}(P)`$ bit operations and temporary bits.
Compute the $`M/2`$ roots for the full transform one at a time. Every
smaller-stage root is one of these roots, so their stored array has
$`O(MP)`$ bits.

## 3. Forward, product and inverse error

All transform values are stored on the $`\delta`$ grid. Additions and
subtractions are exact. A complex product is rounded componentwise to
that grid; its rounding error has norm at most $`2\delta`$.

Consider one transform whose exact input values are already on the grid
and have magnitude at most $`A`$. An exact partial transform has magnitude
at most $`MA`$. If $`E_\ell`$ bounds the current butterfly errors, (1)
gives

```math
E_{\ell+1}\le(2+4\delta)E_\ell+4\delta MA+2\delta,
\qquad E_0=0.
```

Since $`2+4\delta\le3`$ and
$`3^{\log_2M}\le M^2`$, summing the recurrence gives the safe bound

```math
E_{\rm FFT}\le6\delta M^3(A+1).
\tag{2}
```

For a Boolean input, $`A=1`$, so each forward error is at most
$`E_f=12\delta M^3<1`$. Each exact transform value has magnitude at
most $`M`$, and its approximation has magnitude at most $`M+1`$.
After a rounded pointwise product, the error from the exact product
is at most

```math
(2M+1)E_f+2\delta\le40\delta M^4.
\tag{3}
```

The approximate products have magnitude at most $`4M^2`$. Applying (2)
to their inverse transform costs at most $`30\delta M^5`$ error.
Applying the *exact* inverse transform to the input errors (3) costs
at most another $`40\delta M^5`$, by the triangle inequality for its
$`M`$ unit-modulus coefficients. Division by $`M`$ therefore leaves error
at most

```math
70\delta M^4=
\frac{70}{2^{16}M^2}<\frac14.
\tag{4}
```

The division is by a power of two and can be retained exactly for the
final integer comparison. Rounding the real part to the nearest integer
recovers every convolution coefficient uniquely. The imaginary part is
irrelevant to the output and obeys the same error bound.

## 4. Bit cost and writable space

Forward intermediates have magnitude $`O(M)`$, pointwise products have
magnitude $`O(M^2)`$, and inverse intermediates have magnitude $`O(M^3)`$.
Equations (1)–(4) preserve these bounds with fixed constants. Their
scaled integer coordinates have $`O(P+\log M)=O(\log M)`$ bits.
Schoolbook multiplication and long division therefore cost
$`\mathrm{poly}(\log M)`$ per butterfly. There are $`O(M\log M)`$
butterflies, and the root construction costs
$`M\,\mathrm{poly}(\log M)`$ as well.

The roots and a constant number of transform arrays occupy
$`O(M\log M)`$ bits. One root's rational work is reused before computing
the next; it uses only $`\mathrm{poly}(\log M)`$ temporary bits. Thus
both time and writable space are $`M\,\mathrm{poly}(\log M)`$,
proving the lemma. Every tolerance and rounding operation is specified
by integers; the procedure is uniform and has no random choices.

The [exact reference check](verify/check_exact_convolution.py) implements
these integer rounding rules and compares finite outputs with direct
coefficient summation. Its finite comparisons support the implementation;
the error and resource bounds for every $`C`$ are proved above.
