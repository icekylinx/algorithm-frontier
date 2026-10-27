# One literal-ring contraction at square-root precision

<!-- imported-source: checkpoint_13_general_factoring_increment_2026-10-28.zip; sidon_second_moment_factoring_2026-10-28.txt; sha256=5706b952ffef7f0850127e4512810081ec98a419c1d24b8085efeda037d92c01 -->

**Scope:** conditional reduction. See the [curated dependency and review map](../sources.md).

Research checkpoint, 2026-10-28 (Asia/Singapore).

Assumption and status
Assume the Boolean tensor contraction theorem in the October 25, 2026
preprint "The Exponential Time Hypothesis is False". This construction
uses its stated coefficient ring (Z/2^P Z)[V]/(V^ell), with no coefficient-
field extension. It retains the general deterministic time bound

```text
                       2^{O(n/sqrt(log n))}
```


and polynomial space, but uses only one contraction, precision P=O(sqrt n),
and auxiliary work 2^{O(sqrt n)}. It does not improve the main exponent.
Here n is the bit length of the original positive integer input N.

## 1. Rough residual and its even square roots
Remove small factors by direct trial division through 2^h, where
h=ceil(sqrt n), dividing out every discovered prime to full multiplicity.
This takes 2^{O(sqrt n)} bit operations and polynomial space. Call the
remaining integer M. If M=1, the factorization is already complete.

Otherwise M is odd. Write n' for its bit length and K=ceil(n'/h).
Every prime factor of M exceeds 2^h, so the number of prime factors
counted with multiplicity is at most K. Since h>=sqrt(n'), K<=ceil(sqrt n').

Let q_i=p_i^{e_i}, i=1,...,k, be the pairwise coprime prime-power factors
of M. These are unknown to the algorithm. Define

```text
 R={r: 0<r<M, r even, r^2=1 (mod M), r != M-1}.
```


For every odd prime power there are exactly two square roots of 1.
The Chinese remainder theorem gives 2^k roots modulo M. Negation pairs
them, and exactly one representative in each pair is even because M is
odd. Removing M-1 therefore leaves

```text
                   T=|R|=2^(k-1)-1 <= 2^(K-1)-1.
```


If k=1, R is empty. The construction below still works; the final residual
is then a prime power and is handled by exact integer root extraction.

Use a Boolean tensor network for r^2=1+zM, with 0<r<M, r even and r!=M-1.
The exact three-transform construction in Section 5 of the companion
one_contraction_complete_factoring_2026-10-28.txt gives O(n') Boolean edges,
maximum degree O(sqrt(n' log n')), polynomial-size descriptions, and
polynomial-time entries. The quotient z, transform values, comparisons,
and carries are uniquely determined by each root r. Thus every root
contributes exactly one satisfying assignment. No factorization of M
is used to construct this network.

## 2. An integer Sidon set for the digit-pair coordinates
Choose m=ceil(sqrt n') and b=ceil(n'/m). Set D=2^b and write each root
as r=sum_(j=0)^(m-1) D^j d_j(r), with 0<=d_j<D and zero-padded top bits.
Both b and m are O(sqrt n').

Choose an odd prime p with m<=p<2m, handling bounded small m separately.
Trial division and Bertrand's elementary prime bound make this a
deterministic polynomial-time choice. For 0<=j<m define

```text
              v_j=j+2p (j^2 mod p),   Q=2p^2.
```


Then 0<=v_j<Q. Unordered pair sums v_j+v_l are all distinct, including
the repeated-index pairs. Indeed, equality of two sums modulo 2p gives
equality of the ordinary index sums, since each lies in [0,2p-2]. The
quotients then give equality of the sums of squares modulo p. Because
p is odd, the two elementary symmetric functions of the index pairs
agree modulo p, so the unordered pairs agree modulo p and hence exactly.

Set A=2Q+1, a_j=A+v_j, and

```text
                         ell=2A+2Q+1.
```


All single exponents a_j lie below every pair exponent. All unordered
pair exponents a_j+a_l are distinct. Finally 3A>ell-1, so every product
of three nonconstant terms is killed by truncation modulo V^ell.
Since ell=6Q+3<48m^2+3, ell=O(n'). A fixed constant in the tensor theorem
accommodates this truncation length without increasing s beyond Theta(n').

## 3. Quadratic weights give every digit second moment exactly
Set

```text
                           P=2b+K+3
```


and work in the literal theorem ring (Z/2^P Z)[V]/(V^ell).
For input bit i in digit block j, let w=2^(i-jb) and let x be the Boolean
value of that bit. Replace its free unary tensor by

```text
              1 + 2w x V^(a_j) + 2w^2 x V^(2a_j).
```


These entries are computable in polynomial time. The existing bit edge
is used, so this weighting does not require a global numeric-weight
automaton or extra copies of the root bits.

For any satisfying root define F_r(V)=sum_j d_j(r) V^(a_j). Direct
multiplication of the unary factors, using the absence of cubic terms,
gives

```text
                 product_i weight_i = 1+2F_r(V)+2F_r(V)^2
                                             modulo V^ell.
```


For completeness: a single bit supplies its own square term 2w^2 x;
two different bit factors supply 4w_i w_l x_i x_l. These are precisely
the diagonal and off-diagonal terms in 2(sum_i w_i x_i V^(a_(j(i))))^2.
Thus no division by a nonunit, formal differentiation, or unproved
exponential identity is needed.

The contraction C(V) has constant coefficient T, and if

```text
                     C_(j,l)=sum_(r in R) d_j(r)d_l(r),
```


then its coefficient at 2a_j is 2 C_(j,j), and its coefficient at
a_j+a_l for j<l is 4 C_(j,l). The Sidon property prevents any pair alias,
and the shift prevents contamination by single or cubic terms.

Every second moment is nonnegative and below T 2^(2b), so even the largest
coefficient 4 C_(j,l) is smaller than 2^P. Hence its residue gives the
ordinary integer coefficient exactly. Divide by 2 or 4 as appropriate
after recovering that integer. The constant coefficient gives T exactly
as well. In particular, T=0 certifies that the residual has one distinct
prime factor, and T>0 also reveals k=1+log_2(T+1).

## 4. Reconstruct the signed separating moments
Compute, by ordinary integer arithmetic after the contraction,

```text
                   S_j=sum_l D^l C_(j,l)
                      =sum_(r in R) d_j(r) r.
```


For analysis define the unknown signs epsilon_i(r) in {+1,-1} by
r=epsilon_i(r) (mod q_i), and put

```text
                   A_(i,j)=sum_(r in R) d_j(r) epsilon_i(r).
```


Then |A_(i,j)|<=T(D-1) and q_i divides S_j-A_(i,j).
The algorithm computes gcd(M,S_j-c) for every j and every integer
|c|<=T(D-1), and refines the resulting divisors into common factors.

To prove complete separation, fix different prime components i and t.
The product epsilon_i(r)epsilon_t(r) is unchanged under r -> M-r.
Among all 2^k CRT sign vectors, 2^(k-1) have different i,t signs;
therefore 2^(k-2) of the selected even roots have different signs.
The excluded root M-1 has agreeing signs, so it does not alter this count.
Consequently

```text
 sum_j D^j (A_(i,j)-A_(t,j))
 =sum_(r in R) r(epsilon_i(r)-epsilon_t(r))
 =-2^(k-1) (mod p_t).
```


This is nonzero because p_t is odd. Thus for some j,
A_(i,j) differs from A_(t,j) modulo p_t. The scanned choice c=A_(i,j)
then gives a gcd containing the full q_i and excluding p_t. Every pair
of different prime components is separated by at least one scanned gcd.

For each scanned gcd d, first form its saturated divisor

```text
                         u=gcd(M,d^(n') mod M).
```


Every exponent in M is at most n', so u contains either the complete
prime power q_i or none of it. This preserves the pairwise separations.
Starting with the block M, split each current block F into gcd(F,u) and
F/gcd(F,u), omitting 1, for every such u. The blocks stay products of
complete prime-power components. The pair-separation property therefore
forces the final blocks to be precisely the individual q_i. Exact integer
root extraction yields their primes and multiplicities.
The same conclusion includes the case T=0: the single residual block
is already a prime power.

## 5. Complexity and resource improvement
The contraction graph has s=Theta(n') edges. Its precision is

```text
               P=2b+K+3=O(sqrt n'),
```


and its polynomial truncation length is ell=O(n'). It meets the literal
theorem's precision and truncation hypotheses. All tensor entries remain
polynomial-time and polynomial-space computable. There is exactly one
contraction if a residual M>1 remains.

The gcd scan contains at most

```text
             m (2T(D-1)+1) <= poly(n') 2^(K+b)
```


candidates. Since K<=ceil(sqrt n') and b<=ceil(sqrt n'), its cost is
2^{O(sqrt n')}, including polynomial-time gcd refinement and root
extraction. The preliminary trial division costs 2^{O(sqrt n)}. All
second-moment decoding and reconstruction use polynomial additional space.

Thus the entire method is deterministic on every input, uses polynomial
space, and has time

```text
              2^{O(n/sqrt(log n))} + 2^{O(sqrt n)}.
```


The improvement established here is one-call complete factor recovery
with square-root precision and a square-root-exponential auxiliary cost,
inside the original theorem interface. It does not change the leading
n/sqrt(log n) exponent supplied by the contraction theorem.

Primary dependency
https://github.com/openai/math/blob/main/preprints/The-Exponential-Time-Hypothesis-is-False-October-25-2026/build/quantitative-reduction.tex
https://github.com/openai/math/blob/main/preprints/The-Exponential-Time-Hypothesis-is-False-October-25-2026/build/quantitative-contraction.tex

**Attribution:** Yilin Liu and GPT-6 Astra Pro.
