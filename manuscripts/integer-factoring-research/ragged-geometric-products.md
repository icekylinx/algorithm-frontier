# RAGGED GEOMETRIC PREFIX PRODUCTS

<!-- imported-source: checkpoint_10_general_factoring_theory_2026-10-27.zip; ragged_geometric_products_2026-10-27.txt; sha256=c30debe50bd769cfd43220939c999569ee7eecf9ef04286cfe275413a31d4364 -->

**Scope:** retained separate research branch; not part of the selected conditional theorem review. See the [curated dependency and review map](../../problems/integer-factorization/sources.md).

Internal research lemma, 2026-10-27. No novelty claim.

Let A be a commutative ring, let alpha and x_1,...,x_n be explicit units
of A, and let k_j be nonnegative integers. Put V=sum_j k_j. Given monic
polynomial multiplication and multipoint evaluation in soft-linear
arithmetic complexity, the scalar

```text
  P=product_j product_(0<=i<k_j) (1-x_j*alpha^i)
```


can be computed in soft-O(n+sqrt(V)) ring operations. The degenerate
case V=0 has P=1. For A=Z/NZ, all polynomial divisions used below have
monic divisors, so unknown factors of N cause no division obstruction.
The bit cost includes the usual polynomial-arithmetic logarithms and
the bit lengths of the explicit points and exponents.

Proof. Choose h=max(1,ceil(sqrt(V))). Build

```text
  Q_h(X)=product_(0<=i<h) (1-alpha^i X)
```


by scaled doubling. Its leading coefficient is a known unit, so it
may be normalized to monic whenever needed. Write k_j=t_j h+r_j,
0<=r_j<h. Evaluate the one shared Q_h at all points

```text
  x_j*alpha^(h t),  0<=t<t_j.
```


There are at most V/h such points. The cost is soft-O(h+V/h).
For each remaining interval [t_j h,t_j h+r_j), use its binary
prefix decomposition into at most one block of each dyadic length
2^s<h. At scale s, every block product is a value of the same
Q_(2^s) at its corresponding shifted point. There are at most n
points at this scale. The Q_(2^s) are obtained together by doubling,
and their total degree is O(h). Thus all remainder blocks together
cost soft-O(h+n). Multiplying all computed values proves the claim.
Point generation costs O(V/h+n log h) unit multiplications or powers,
which is covered after charging the exponent bit lengths.

If N is composite and gcd(P,N)>1, some computed block value is a
nonunit. Retain or scan the block values and choose any such block.
Scanning its at most h original factors finds a nonunit leaf. This
adds O(h) ring operations and gcd tests, apart from exponent-bit
costs. A proper leaf gcd factors N. A full-N leaf gives a useful
period only in applications where its integer exponent is known to
be nonzero and an appropriate period-recovery theorem applies.
The lemma does not assume that a full-N gcd by itself gives a factor.

SCOPE

This is an explicit-input theorem: reading n arbitrary units costs
Omega(n). It therefore does not replace the n term by the number of
short descriptions of an implicit root family. In particular it does
not solve the modular-conic giant-product bottleneck. Generic MPE also
has logarithmic overhead absent from some special geometric MPE bounds;
no sharp logarithmic factoring claim is based on suppressing that cost.

CONTENT-NORMALIZATION ENVELOPE

In the uncentered factoring cover, write a=gA,b=gB with g|m. If local
conditions at primes dividing g are dropped, use modulus m/g and
multiply the normalized candidate exponent by g^2. All groups then
share baby step beta^(m^2), but group g has a prefix length O(K g),
where K=sqrt(N)/R^(3/2). The true Fermat exponent is multiplied by g,
so its divisibility is preserved without a root extraction assumption.

The noncontent local root mean is (1-1/ell)^2. At ell|g, retaining
only gcd(A,B,ell)=1 gives mean 1-1/ell^2 and no root multiplicity.
Thus, with L=log N and H=loglog N, the main-term model gives

```text
  n=sum_g n_g = O(R L/H^2),
  V=sum_g n_g*(K g) = O(R K L/H).
```


The second identity follows because the local ratio of content to
noncontent means is (ell+1)/(ell-1), and the Euler product for the
weighted sum with 1/g is Theta(H); the sum with 1/g^2 is bounded.
Even granting the optimal arithmetic envelope n+sqrt(V), balancing
its two terms gives only

```text
  N^(1/5) L^(13/5)/H^(4/5)
```


if the sharp L^2 bit factor were available. This is worse than the
retained-image content sieve's H^(-9/10), and the generic-MPE logarithms
can only worsen it. Retaining a fraction t of content refinements
interpolates the formal density exponents a=2-t/2 and b=1+t/2;
the optimized H saving is (a+2b)/5=(4+t/2)/5, largest at t=1.
This is an envelope audit of this normalization template, not a lower
bound for other algorithms.

**Attribution:** Yilin Liu and GPT-6 Astra Pro.
