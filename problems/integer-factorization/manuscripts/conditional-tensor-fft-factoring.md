# Conditional general factoring through succinct Fourier networks

<!-- imported-source: checkpoint_10_general_factoring_theory_2026-10-27.zip; conditional_tensor_fft_factoring_2026-10-27.txt; sha256=4aef39ee9c549d6f03cbc0b9c03ac44752fa3050f0c5de73e2385ec0373d21a9 -->

**Scope:** conditional reduction. See the [curated dependency and review map](../sources.md).

Research checkpoint, 2026-10-27. This is a reduction, not a validation of
the newly posted external contraction theorem and not an unconditional
factoring claim.

CONCLUSION AND DEPENDENCY

Assume the Boolean tensor contraction theorem labelled
thm:tensor-contraction in the October 25, 2026 preprint
"The Exponential Time Hypothesis is False" is correct with its stated
uniform bit-complexity and succinct-entry interface. Then every positive
integer N has a deterministic, polynomial-space factorization algorithm
using

```text
             2^{O(n / sqrt(log n))} bit operations,
             n = floor(log_2 N) + 1.
```


Thus the conditional bound is N^{O(1/sqrt(log log N))}. The reduction
works for arbitrary integers and does not assume balanced factors,
special public exponents, leaked bits, or special RSA keys. This bound
improves a fixed positive power of N on the deterministic frontier. It
does not beat the asymptotic heuristic number-field sieve bound or the
usual subexponential randomized factoring bounds.

The external claim was posted two days before this checkpoint. The
precise statement and the applicability of the construction below have
been read and independently checked internally. The whole external proof
has not been certified here; its soundness remains an explicit dependency.
No novelty claim for this corollary is made.

## 1. THE EXACT EXTERNAL INTERFACE NEEDED

Only the following special case of the cited theorem is used. A bipartite
Boolean tensor network has O(s) edges, polynomially many vertices, maximum
degree at most ceil(s^{9/10}), and total description length L=s^{O(1)}.
Each 0/1 tensor entry is computable uniformly from its description and
port bits in polynomial time and space. For P=O(s), its contraction over
Z/(2^P)Z can then be computed deterministically in

```text
              (s+L)^{O(1)} 2^{O(s/sqrt(log s))}
```


bit operations and polynomial space. This specialization takes the
theorem's truncated-polynomial parameter ell=1. The stated theorem even
permits local entry time (s+L)^b 2^{A s^{9/10}}. Its size parameter counts
Boolean edges; it does not require explicit local truth tables.

The distinction between edge count and description length is essential.
Explicit grouped-gate truth tables would violate the polynomial
description and space budgets. Here each entry is verified by a short
uniform exact-arithmetic procedure. For the time bound alone there is
also a fallback: all explicit tables have combined length
2^{O(sqrt(n log n))}. The full cited theorem retains a polynomial factor
in description length even when that length is not polynomial in s.
Thus materializing these tables also fits the claimed final time, at
the cost of losing the polynomial-space guarantee. A reformulation that
used total table length as its exponential parameter would not suffice.

## 2. A POLYNOMIALLY CONSTRUCTIBLE EXACT TRANSFORM FIELD

For sufficiently large n set

```text
 b=floor(log_2 n), B=2^b, t=ceil(n/b),
 M=the least power of 4 at least 2t, K=sqrt(M).
```


Then 2t<=M<8t, K is an integer power of 2, and M=Theta(n/log n).
The finitely many smaller n can be handled directly. Choose a power of 2
Q at least M and strictly larger than 2t B^2. Thus M divides Q and Q is
polynomial in n.

Linnik's theorem supplies a prime pi=1 (mod Q) of size Q^{O(1)}, hence
pi=n^{O(1)}. Enumerate 1+Q, 1+2Q, ... and test primality by trial division
until finding the first prime. The theorem makes this a deterministic
polynomial-time preprocessing step; no unproved prime-distribution
hypothesis and no random prime choice is used. Put h=ceil(log_2 pi), so
h=O(log n).

Search all g in {1,...,pi-1} until g^{(pi-1)/2}=-1 mod pi. This is also
polynomial time. Since M is a power of 2 dividing pi-1, the element

```text
                       omega=g^{(pi-1)/M}
```


has order exactly M. Indeed, a quadratic nonresidue has the full 2-part
of pi-1 in its multiplicative order, which remains exactly M after the
indicated exponentiation. All arithmetic below is exact in F_pi, with
canonical h-bit representatives 0,...,pi-1.

## 3. TWO GROUPED LAYERS FOR ONE DFT

For x_0,...,x_{M-1} in F_pi write j=j1+K j2 and k=k1+K k2, with each
subscript in {0,...,K-1}. Let zeta=omega^K. Compute

```text
 Z_{j1,k1} = sum_{j2=0}^{K-1} x_{j1+K j2} zeta^{j2 k1},
```


```text
 Y_{k1+K k2} = sum_{j1=0}^{K-1}
                 Z_{j1,k1} omega^{j1 k1} zeta^{j1 k2}.
```


Expanding the two sums gives Y_k=sum_j x_j omega^{jk}, because the
omitted term K^2 j2 k2 is a multiple of M. The first line consists of K
disjoint K-input/K-output gates. The second line also consists of K such
gates, with the indicated permutation and twiddles incorporated into the
gate descriptions. The inverse DFT uses omega^{-1} and multiplication
of all outputs by M^{-1}; it has the same form.

Each gate is a Boolean 0/1 relation on its input and output encodings:
it accepts precisely when every word is canonical and the displayed
field equations hold. A local entry can be checked by O(K^2) elementary
field operations, with an additional polynomial cost for powers and bit
arithmetic if they were not precomputed. This is polynomial in n.

A grouped gate has at most 2Kh Boolean ports. In particular,

```text
                 2Kh=O(sqrt(n log n))=o(n^{9/10}).
```


Each whole layer exposes M h=O(n) Boolean wires, not M^2 h wires. The
quadratic arithmetic inside an individual gate is performed by its entry
algorithm and is not expanded into Boolean wires. This use of a succinct
local relation is exactly the external theorem's stated interface.

## 4. MULTIPLICATION, CARRIES, AND NONTRIVIAL FACTORS

Let U and V be unknown n-bit nonnegative integers. Pack their bits into
t digits u_i,v_i in base B, pinning any unused bits of their highest
digit to zero. Pad both digit vectors with zeros to length M. Compute
their two DFTs, multiply the transformed words coordinatewise, and apply
one inverse DFT. There are six grouped transform layers in total plus
one layer of M ordinary field-multiplication constraints.

The inverse output is the cyclic convolution modulo pi. Since M>=2t,
there is no cyclic wrap for these padded inputs. Its ordinary integer
coefficients satisfy

```text
 c_i=sum_{j+k=i}u_j v_k,
 0<=c_i<=t(B-1)^2<pi.
```


Consequently the canonical field outputs are exactly these integer c_i,
not merely congruent to them. Coefficients past index 2t-2 are zero.

Write the known N in base B with M digits N_i, padded with zeros. Add a
carry chain with integer variables e_i and the exact constraints

```text
 c_i+e_i=N_i+B e_{i+1}  (0<=i<M),
 e_0=e_M=0,
 0<=e_i<=t(B-1).
```


These are ordinary integer equalities in the local entry predicates.
Each carry has O(log n) bits, and each constraint has O(log n) ports.
The upper bound holds for genuine multiplication: if e_i<=t(B-1), then
(c_i+e_i)/B<=t(B-1). Conversely, summing the equations after multiplying
by B^i shows UV=N. Thus the constraints accept exactly products N.

Require U>=2 and V>=2. For a binary nonnegative integer this is simply
the OR of all bits except its least significant bit. Binary OR trees and
constant-degree equality-copy trees impose these tests using O(n) edges.
The input packing, zero pins, and all field-range checks have O(n) total
edges and polynomially computable entries as well.

All parts of this constraint network therefore have O(n) Boolean edges
and O(n) vertices. Every accepted factor pair extends to its canonical
FFT intermediates and ordinary carries; the construction is exact.

## 5. BIPARTITENESS, PRECISION, AND DESCRIPTIONS

Treat each Boolean constraint as a tensor vertex and each connecting
Boolean wire as an edge. Free input bits terminate at a unary tensor
whose entries are both 1. To copy a bit, use a trivalent tensor accepting
only all-equal port values. Thus no implicit unbounded fan-out is used.

Subdivide every edge once by a binary equality tensor. The old vertices
and the inserted vertices give a bipartition, and the contraction is
unchanged. The resulting number of Boolean edges W is still O(n).
There are at least 2n edges already incident to the free factor-input
bits, so W=Theta(n). Set s=max(2,W). For all sufficiently large n the maximum degree is at
most ceil(s^{9/10}); bounded exceptional inputs can again be handled
directly. The total graph and tensor description length is polynomial
in n: it contains indices, pins, pi, omega, the factorization M=K^2,
and a fixed code implementing each type of local relation. No truth
table with exponentially many entries is written down.

Set P=s+1. Every tensor has entries 0 or 1, so the ordinary integer
contraction Z lies between 0 and 2^W. Therefore its residue modulo 2^P
uniquely identifies Z, and is zero if and only if no satisfying
assignment exists. This precision argument does not even require
uniqueness of internal extensions. It avoids a possible modular-count
cancellation mistake. The theorem's precision bound holds with a fixed
constant C>=2 and ell=1.

The result is a uniform, exact Boolean network description constructed
in polynomial bit time and space. Neither real-number computation nor
nonuniform advice is present. The external theorem is being invoked on
0/1 tensors, not on tensors whose entries are arbitrary elements of
F_pi; the latter field is used solely inside efficiently testable local
predicates.

## 6. COUNTING TO FINDING, AND COMPLETE FACTORIZATION

The contraction is positive precisely when N has a nontrivial ordered
factor pair. In fact, all field encodings are canonical, each transform
and copy/OR gate is functional, and the ordinary carry chain is unique.
Every ordered factor pair therefore contributes exactly one assignment.
For N>=2 a single contraction equals tau(N)-2, where tau(N) is the number
of positive divisors. Prefix restrictions count the corresponding
factor pairs exactly. Binary interval comparators could likewise be
added with O(n) edges if a factor-interval count were wanted.

To find a factor, successively pin each bit of U. Query whether
the existing prefix followed by 0 still has positive contraction; keep
0 if it does and otherwise keep 1. The positive initial count ensures
that one option always survives. After n calls U is known and satisfies
2<=U<=N/2. Compute V=N/U by ordinary exact division and verify UV=N.
The pin tensors do not change the asymptotic network size.

Each call has s=O(n) and L=n^{O(1)}, so the assumed theorem gives time

```text
                    n^{O(1)} 2^{O(n/sqrt(log n))}.
```


The n prefix calls and the polynomial preprocessing are absorbed in
the same bound. Recursive splitting produces the complete prime
factorization; its recursion tree has O(n) nodes and hence only
polynomially many contraction calls in total. A depth-first implementation
uses polynomial space. The complete result remains valid on every
integer N, including unbalanced products, prime powers, and inputs
with many prime factors.

For an ordinary RSA modulus, the resulting factorization gives lambda(N),
then the inverse of the public exponent modulo lambda(N), and finally
the plaintext by modular exponentiation. Thus the same conditional bound
also applies to general RSA inversion, plus a polynomial cost in the
public input length. This implication uses factoring as a sufficient
method; it does not assert that RSA inversion and factoring are equivalent.

## 7. AUDIT STATUS AND PRIMARY REFERENCES

The reduction and its wire count have been independently checked by
the root researcher and the frontier researcher in this session. The
external tensor theorem is a separate, newly posted mathematical claim.
The dependency must remain explicit until its proof is validated; the
conditional result must not be merged into an unconditional factoring
bound or a claim that RSA has been broken.

[T] "The Exponential Time Hypothesis is False", October 25, 2026,
preprint hosted in the openai/math repository.
Statement, thm:tensor-contraction:
https://github.com/openai/math/blob/main/preprints/The-Exponential-Time-Hypothesis-is-False-October-25-2026/build/quantitative-reduction.tex
Core contraction proof, app:tensor:
https://github.com/openai/math/blob/main/preprints/The-Exponential-Time-Hypothesis-is-False-October-25-2026/build/quantitative-contraction.tex

[L] T. Xylouris, "On Linnik's constant", Acta Arithmetica 150 (2011),
65-91; arXiv:0906.2749. Only existence of some fixed polynomial bound
for the least prime in a coprime progression is needed here, not the
value 5.2.
https://arxiv.org/abs/0906.2749

[F] J. W. Cooley and J. W. Tukey, "An algorithm for the machine
calculation of complex Fourier series", Mathematics of Computation
19 (1965), 297-301. The two-layer identity needed here is proved
explicitly in Section 3, so no analytic or approximate FFT hypothesis
is imported.
https://doi.org/10.1090/S0025-5718-1965-0178586-1

End of conditional reduction.

**Attribution:** Yilin Liu and GPT-6 Astra Pro.
