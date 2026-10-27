# One contraction for complete deterministic integer factorization

<!-- imported-source: checkpoint_13_general_factoring_increment_2026-10-28.zip; one_contraction_complete_factoring_2026-10-28.txt; sha256=0b199f4f2eb02e6b7848f61ef7691db2aad0f0c4fcc38d48f9a9fe2fd1060ee5 -->

**Scope:** conditional reduction. See the [curated dependency and review map](../sources.md).

Research increment, 2026-10-28 (Asia/Singapore)

Status. The tensor-contraction theorem in the October 25, 2026 preprint
"The Exponential Time Hypothesis is False" is an assumed theorem in this
note, as requested. The extraction arguments below are proved here. They
do not assert that the resulting exponent is optimal, or that this
corollary is new in the literature.

MAIN RESULT

Assume the preprint's uniform Boolean tensor-contraction theorem, including
its truncated-polynomial coefficient ring and succinct-entry interface.
For every positive n-bit integer N, complete prime factorization reduces
to ONE contraction of a polynomially described bipartite Boolean tensor
network with

```text
  O(n) Boolean edges,
  maximum degree O(sqrt(n log n)),
  coefficients in (Z/2^P Z)[V]/(V^ell),
  P = n + O(n/log n),       ell = O(log n).
```


Every local entry is computable in polynomial time and space. Deterministic
postprocessing costs 2^{O(n/log n)} bit operations and polynomial space.
Consequently the assumed theorem gives complete factorization in

```text
               2^{O(n/sqrt(log n))} bit operations
```


and polynomial space. This improves the reduction from repeated adaptive
factor-bit queries to one contraction that encodes a separating family for
ALL prime-power factors. It does not improve the main exponential scale
over the previously established FFT reduction. Since the contraction's
polynomial overhead may depend on ell, this is a query-complexity result,
not a claim that a particular implementation is faster by a stated factor.

There is a tradeoff: for 1 <= m <= n, one can instead use ell = 2m+1,
P = n + ceil(n/m) + O(n/log n), and postprocessing
2^{O(n/m+n/log n)}. Taking m = ceil(log_2 n) gives the bounds above.

## 1. ROOTS, SIGNS, AND A COMPUTABLE ROOT-COUNT BOUND

Remove powers of 2 from the input by ordinary division. Write the remaining
odd integer again as N, and let n be its bit length. N=1 is immediate;
bounded small inputs can be handled directly.

For purposes of proof only, write

```text
                    N = product_{i=1}^k q_i,
                    q_i = p_i^{e_i},
```


where the p_i are distinct odd primes. The algorithm does not know them.
Every solution x^2=1 modulo q_i is +1 or -1, because the odd prime p_i
cannot divide both x-1 and x+1. The Chinese remainder theorem gives
exactly 2^k roots in [0,N).

Define R to consist of the even representatives r satisfying

```text
                0 < r < N-1,       r^2 = 1 (mod N).
```


The involution r -> N-r reverses parity. Thus the even roots choose one
representative from each global sign pair. Removing the even root N-1
removes the trivial pair {1,N-1}. Therefore

```text
                         T = |R| = 2^{k-1}-1.              (1)
```


For k=1 the set is empty. For k>=2 its size is odd. A parity contraction
and parity-preserving prefix restrictions already suffice to find a root;
Sections 2--5 give a stronger, nonadaptive extraction of all factors.

Let K be the largest integer such that (K+1)! <= N. This is computable
with polynomially many n-bit operations. Since the i-th smallest distinct
prime is at least i+1, k<=K. Elementary factorial estimates give

```text
                         K = O(n/log n),
                         T < 2^K.                         (2)
```


Only this upper bound, not a factorization of N or an estimate using the
prime number theorem, is needed to set the contraction precision.

## 2. A SMALL FAMILY OF WEIGHTED ROOT MOMENTS

Choose an integer m in [1,n], put b=ceil(n/m), and B=2^b. Write

```text
                   r = sum_{j=0}^{m-1} B^j d_j(r),
                   0 <= d_j(r) < B,
```


with zero padding in the final block when needed. The quantities to be
computed are the ordinary nonnegative integers

```text
                   S_j = sum_{r in R} d_j(r) r.            (3)
```


For each unknown prime power q_i define its sign on r by

```text
                   r = epsilon_i(r) (mod q_i),
                   epsilon_i(r) in {+1,-1},
```


and define the ordinary signed counts

```text
                   A_{i,j} = sum_{r in R} d_j(r) epsilon_i(r).
```


These signed counts are not computed by the algorithm. They satisfy

```text
            |A_{i,j}| <= D := (B-1)T,
            S_j = A_{i,j} (mod q_i).                       (4)
```


PAIR-SEPARATION LEMMA.
For any two different prime factors p_i,p_h, there is an index j such that

```text
                   A_{i,j} != A_{h,j} (mod p_i).            (5)
```


Proof. Suppose every difference were zero modulo p_i. The base-B digit
expansion would then imply

```text
  0 = sum_j B^j(A_{i,j}-A_{h,j})
    = sum_{r in R} r(epsilon_i(r)-epsilon_h(r))
    = sum_{r in R}(1-epsilon_i(r)epsilon_h(r))  (mod p_i).
```


In the full Boolean sign cube, exactly half the sign vectors have unequal
coordinates i,h. The condition of unequal coordinates is invariant under
global sign reversal. Hence the chosen one-root-per-sign-pair section has
exactly 2^{k-2} roots with unequal coordinates. Removing the trivial pair
does not change this count. The final sum is consequently 2^{k-1}, which
is nonzero modulo the odd prime p_i. Contradiction. QED.

In particular, let j satisfy (5) and let c=A_{h,j}. Then

```text
               q_h divides S_j-c,     p_i does not divide S_j-c.
```


Thus one of the explicitly enumerable gcds

```text
                 gcd(N,S_j-c),
                 0<=j<m,  -D<=c<=D,                       (6)
```


contains all of q_h and none of p_i. This holds without any lower bound
on the prime factors relative to T or B. There is no hidden small-prime
assumption and no need to trial-divide up to D.

## 3. COMPLETE FACTORIZATION FROM THE MOMENTS

For each gcd d in (6), replace it by its saturated divisor

```text
                    u = gcd(N, d^n mod N).                 (7)
```


Every prime-power exponent e_i is at most n. Therefore u contains either
all of q_i or none of it: u is a unitary divisor of N. Saturation preserves
every separation proved above.

Start with a list consisting of N. For each u, replace every list entry F
by gcd(F,u) and F/gcd(F,u), omitting 1 and leaving F unchanged for trivial
splits. Since u is unitary, every list entry remains a product of complete
prime-power components. Once all u have been processed, no list entry can
contain two distinct primes: the separation lemma supplies a processed u
which would have separated them. Thus the final entries are exactly the
pairwise coprime prime powers q_1,...,q_k.

An integer known to be a prime power can be reduced to its prime base by
testing exact integer roots for exponents up to its bit length and taking
the largest valid exponent. This is polynomial-time integer arithmetic.
The input's previously removed power of 2 is appended to the output.

If T=0, (1) already proves that the odd N is a prime power. The same exact
integer-root procedure handles this case, with exponent 1 when N is prime.
Thus no separate primality or perfect-power oracle is required for the
correctness of the one-contraction reduction.

The list has at most n entries. Each modular exponentiation and gcd takes
polynomial time and space. There are m(2D+1) candidates, with

```text
                 log_2(D+1) <= b+K+O(1).
```


The postprocessing is therefore 2^{O(b+K)} bit operations and polynomial
space. It can stream c and the gcds; it never materializes exponentially
many candidate divisors at once. With m=ceil(log_2 n), b=O(n/log n), so
this cost is 2^{O(n/log n)}.

## 4. ONE CONTRACTION THAT RETURNS T AND ALL S_j

Suppose first that there is a Boolean 0/1 tensor network whose accepting
assignments are in bijection with R, with explicit input bits r_i. Section
5 constructs such a network with O(n) edges.

Work in the coefficient ring

```text
                 (Z/2^P Z)[V]/(V^{2m+1}).
```


For bit i in block j=floor(i/b), attach the weight

```text
            1 + 2^{i-jb} r_i V^{m+1+j}.                    (8)
```


All marker exponents are at least m+1, so every product of two marker
terms vanishes. The product of all bit weights is exactly

```text
                     1 + sum_j d_j(r) V^{m+1+j}.           (9)
```


Notice that (8) attaches to INDIVIDUAL bits. There is no high-degree gate
which has to read a b-bit digit. This matters when b=n/log n exceeds the
maximum-degree allowance in the assumed contraction theorem.

To supply the numerical weight r, add a two-state chain. At the step for
bit i, the allowed state transitions and weights are

```text
         0->0 : 1,       1->1 : 1,
         0->1 : 2^i r_i, 1->0 : 0.
```


Pin the initial state to 0. Give final state 1 weight 1 and final state 0
weight V^m. Summing over chain states yields r+V^m: a transition into state
1 can occur exactly once, and summing its position gives sum_i 2^i r_i=r.

Multiplying this chain weight by (9), and using the truncation, gives

```text
             r + V^m + sum_j r d_j(r) V^{m+1+j}.
```


The single contraction thus returns

```text
     F(V) = sum_{r in R}r
            + T V^m
            + sum_{j=0}^{m-1} S_j V^{m+1+j}.                (10)
```


All coefficients are nonnegative integers before reduction. They are
bounded by T(B-1)N, except the smaller count and constant coefficients.
Taking

```text
                       P = n+b+K+2                        (11)
```


makes every required coefficient strictly less than 2^P. Reading the
coefficients of (10) therefore recovers the exact integers T and S_j,
with no modular-count cancellation.

The chain, markers, and constant-degree copies of r_i add O(n) edges.
Their entries use integers of at most O(n) bits and are computable in
polynomial time. The total description length remains polynomial.

## 5. A LINEAR-EDGE NETWORK FOR THE ROOT RELATION

The previous checkpoint proved an O(n)-edge exact multiplication network
using grouped two-layer finite-field DFTs. The root relation can be encoded
at the same three-transform scale by transforming a signed carry vector.
Details are supplied here to avoid an implicit large arithmetic circuit.

Set u=floor(log_2 n), beta=2^u, t=ceil(n/u), and let M be the least power
of 4 at least 2t. Write M=H_0^2. Then M=Theta(n/log n) and H_0 is a power
of 2. Use a field F_pi with

```text
          pi > 8t beta^2,       M divides pi-1,
          log_2 pi = O(log n),
```


and a primitive M-th root omega. Such a field is deterministically
constructible in polynomial time: choose a power of 2 Q divisible by M
and larger than 8t beta^2; Linnik's least-prime theorem gives a prime
pi=1 mod Q of polynomial size in n. Exhaustive search with trial-division
primality checks is therefore polynomial. Searching for a quadratic
nonresidue g and setting omega=g^{(pi-1)/M} gives exact order M.

The unknown integer r and an auxiliary integer q have n-bit encodings,
packed into t base-beta digits and zero-padded to M. Their intended
equation is

```text
                          r^2 = 1+qN.                     (12)
```


The known digit vector of N is transformed once in preprocessing.
Let c_i(r*r) and c_i(q*N) denote the ordinary integer convolution
coefficients. They have no cyclic wrap because M>=2t, and each lies
between 0 and t(beta-1)^2.

Introduce signed carries e_i, with e_0=0, e_M=e_0=0, and

```text
                         |e_i| <= H := t(beta-1)+1.
```


The local integer equations are

```text
      c_i(r*r)-c_i(q*N)-delta_{i0}+e_i-beta e_{i+1}=0.      (13)
```


For a genuine equality (12), the recurrence from e_0=0 gives unique
integer carries. Integrality follows successively from equality modulo
beta^{i+1}; the last carry is zero. The bound follows by induction from

```text
  |c_i(r*r)-c_i(q*N)-delta_{i0}| <= t(beta-1)^2+1,
```


since division by beta preserves the asserted bound H. Conversely,
summing (13) after multiplying by beta^i telescopes the carries and gives
(12).

Encode e_i as its canonical field residue, checked to belong either to
[0,H] or to [pi-H,pi-1]. These intervals are disjoint, so the signed value
is unique. All words have O(log n) bits.

Compute THREE forward DFTs: the digit vectors of r, q, and e. Their
frequency values R_k,Q_k,E_k must satisfy

```text
      R_k^2-Q_k Nhat_k = 1+(beta omega^{-k}-1)E_k.           (14)
```


This identity is exactly the DFT of (13), since a cyclic shift of e has
transform omega^{-k}E_k. The inverse DFT is invertible over F_pi. Thus
(14) forces (13) modulo pi. The chosen pi exceeds the absolute value of
every expression in (13), so each congruence is the exact integer equality.
The constant 8 in pi>8t beta^2 is more than sufficient for the displayed
coefficient and carry bounds.

Each DFT is represented by two grouped layers. For j=j1+H_0 j2 and
k=k1+H_0 k2, with zeta=omega^{H_0}, use

```text
  Z_{j1,k1} = sum_{j2} x_{j1+H_0 j2} zeta^{j2 k1},
  Y_{k1+H_0 k2} = sum_{j1} Z_{j1,k1}
                       omega^{j1 k1} zeta^{j1 k2}.
```


Every grouped gate has O(H_0 log n)=O(sqrt(n log n)) Boolean ports, and its
0/1 entry is checked by polynomial-time exact field arithmetic. Every
whole layer has O(M log n)=O(n) Boolean wires. Pointwise (14) has only
O(log n) ports per frequency. Therefore the three transforms and all
their sinks use O(n) edges in total.

Binary comparators impose 0<r<N-1 and r even. They need O(n) edges with
constant-degree local constraints. For every r in R, q=(r^2-1)/N is a
unique nonnegative integer less than N, the signed carries are unique,
and every canonical transform word is unique. Hence the network's
accepting assignments are in bijection with R as required in Section 4.

Subdivide every edge by an equality tensor to obtain a bipartite network.
This changes edge count by only a constant factor. With s=Theta(n), the
maximum degree O(sqrt(n log n)) is below s^{9/10} for sufficiently large
n. All bounded exceptions can be handled directly.

## 6. APPLYING THE ASSUMED THEOREM

The augmented network still has O(n) Boolean edges and polynomial
description length. Its entries are elements of the precise ring allowed
by the assumed theorem, not arbitrary non-Boolean-index tensors.
The bounds P=O(n) and ell=O(log n) satisfy the theorem with fixed constants.
One contraction consequently costs

```text
                     n^{O(1)} 2^{O(n/sqrt(log n))}
```


and polynomial space. The postprocessing 2^{O(n/log n)} is of strictly
smaller exponential order. No adaptive sequence of factor-bit queries
or recursive contraction calls is needed for complete factorization.

## 7. WHY ORDINARY BITWISE XOR DOES NOT SUFFICE

The weighted moments in (3) are essential to the separation proof. Merely
computing the bitwise XOR of all selected roots is not a correct general
extraction method. For example,

```text
        N=385=5*7*11,      R={34,76,274}.
```


Their XOR is 380. Its square is 25 modulo 385, and both gcd(379,385) and
gcd(381,385) are 1. Thus neither the square-root test nor the usual two
adjacent gcds succeeds. The integer weighted-moment identity avoids this
failure and proves pairwise separation for every odd input.

For the same example, n=9, m=4, b=3, B=8 give the four moments

```text
                 (S_0,S_1,S_2,S_3) = (920,760,1172,0).
```


Here T=3 and D=21. The allowed shifts include

```text
       gcd(920,385)=5,   gcd(760+3,385)=7,
       gcd(760-1,385)=11.
```


These are exact small-number illustrations of the separation proof, not
evidence about asymptotic running time.

## 8. OPTIONAL BALANCING OF THE NON-CONTRACTION WORK

There is a second useful parameter choice when a somewhat larger
truncated-polynomial dimension is acceptable. Let n_0 be the original
input bit length and h=ceil(sqrt(n_0)). First remove every prime factor at
most 2^h by deterministic trial division. This costs 2^{O(h)} bit
operations and polynomial space. Trial division through consecutive
integers suffices: after smaller primes have been fully removed, any
dividing trial integer is itself prime.

If the remaining integer is 1, the factorization is already complete.
Otherwise write its bit length as n. All its prime factors exceed 2^h,
so k<n/h and in particular T<2^{ceil(n/h)}. Choose m=h (or the harmless
integer adjustment min(h,n)), giving b=ceil(n/m). A nontrivial remaining
integer necessarily has n>h, so the main case has m=h<=n.

Use K=ceil(n/h) in the precision bound instead of the factorial bound.
Then the moment scan costs 2^{O(n/h)}, the ring has ell=O(h), and
P=n+O(n/h). The initial trial division and final extraction together cost

```text
                       2^{O(h+n/h)}.
```


Taking h=ceil(sqrt(n_0)) makes all non-contraction work
2^{O(sqrt(n_0))}, while ell=O(sqrt(n_0)) and the graph still has O(n)
edges for the remaining integer. The overall bound remains
2^{O(n_0/sqrt(log n_0))}; the exponential term from the assumed theorem
still dominates. This is an auxiliary-complexity tradeoff, not an
improvement in the main exponent.

Thus two explicit versions are available:

```text
  (a) ell=O(log n), no small-prime preprocessing, and auxiliary work
      2^{O(n/log n)};
```


```text
  (b) ell=O(sqrt(n_0)), small-prime preprocessing, and auxiliary work
      2^{O(sqrt(n_0))}.
```


Both use at most one contraction for complete factorization and retain
polynomial space.

REFERENCES AND DEPENDENCIES

[T] "The Exponential Time Hypothesis is False", October 25, 2026.
The assumed statement is thm:tensor-contraction, with the coefficient ring
(Z/2^P Z)[V]/(V^ell), uniform succinct local entries, and the stated bit-time
and space bounds.
https://github.com/openai/math/blob/main/preprints/The-Exponential-Time-Hypothesis-is-False-October-25-2026/build/quantitative-reduction.tex

[L] T. Xylouris, "On Linnik's constant", Acta Arithmetica 150 (2011),
65--91; arXiv:0906.2749. Only an unspecified fixed polynomial bound for the
least prime in a coprime arithmetic progression is used.
https://arxiv.org/abs/0906.2749

[P] Previous internal reduction, 2026-10-27:
conditional_tensor_fft_factoring_2026-10-27.txt.
The present note supplies an alternative root network and the new
nonadaptive complete-factorization extraction, rather than relying on an
unwritten modification of the previous multiplication network.

End of research increment.

**Attribution:** Yilin Liu and GPT-6 Astra Pro.
