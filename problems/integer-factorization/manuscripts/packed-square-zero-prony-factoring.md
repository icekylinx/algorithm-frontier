# One literal-ring contraction with subpolynomial precision

<!-- imported-source: checkpoint_13_general_factoring_increment_2026-10-28.zip; packed_square_zero_prony_factoring_2026-10-28.txt; sha256=c05e2e3efd4ed52c784f059242a5d24a8d2ccbc7aa626462649cef2b1e7b7696 -->

**Scope:** conditional reduction. See the [curated dependency and review map](../sources.md).

Research checkpoint, 2026-10-28 (Asia/Singapore).

Conclusion
Assume the Boolean tensor contraction theorem stated in the October 25,
2026 preprint "The Exponential Time Hypothesis is False". There is a
uniform deterministic complete factorization algorithm for every n-bit
positive integer N with the following resources:

```text
 * one contraction of a Boolean network with O(n) edges;
 * exactly the stated ring (Z/2^P Z)[V]/(V^ell), with ell<=n and
   P=n^{o(1)};
 * polynomial-time tensor-entry algorithms and polynomial space;
 * preprocessing time 2^{O(n loglog(n)/log(n))};
 * polynomial-time postprocessing after the contraction;
 * overall time 2^{O(n/sqrt(log n))}.
```


The improvement is in the reduction, required precision, and recovery
interface. The main time exponent remains that supplied by the external
theorem. No extension of that theorem's coefficient-ring interface is
used. An auxiliary finite-field algebra is compiled into ordinary 0/1
matrix-entry tensors and one packed integer output tensor.

All logarithms below are base two. Bounded small inputs are handled
directly. The displayed parameter conditions can also be checked before
using this construction.

## 1. A rough residual with n^{o(1)} nontrivial square roots
Let

```text
 L=ceil(log_2 n),  lambda=ceil(log_2 L),
 h=ceil(n lambda/L),  kappa=ceil(L/lambda),  K=2^kappa.
```


Use direct trial division through 2^h, removing the full multiplicity
of every factor that is encountered. Processing candidates in increasing
order guarantees that every actual divisor encountered is prime; no
separate primality test is needed. This uses polynomial space and

```text
             2^{O(h)}=2^{O(n loglog(n)/log(n))}
```


bit operations. This exponent is o(n/sqrt(log n)).

Let M be the remaining residual. If M=1, the algorithm is finished. Every
prime factor of M exceeds 2^h, so M is odd. If Omega counts prime factors
with multiplicity, then Omega(M)<n/h<=L/lambda. Let k be the number of
distinct prime factors, unknown to the algorithm, and define

```text
 R={x: 0<x<M-1, x even, x^2=1 (mod M)}.
```


Each odd prime power has exactly two square roots of 1. The Chinese
remainder theorem and the fact that negation exchanges even and odd
representatives give

```text
              t=|R|=2^(k-1)-1<=2^{Omega(M)}<=K=n^{o(1)}.
```


The excluded root M-1 is the even representative of the trivial pair
{1,M-1}. In particular t=0 exactly when M has one distinct prime factor.
Let n' be the bit length of M. No balancing, squarefreeness, or special
congruence hypothesis is imposed on the input.

## 2. A unique-extension root verifier
Use Section 5 of the companion note
one_contraction_complete_factoring_2026-10-28.txt. That section supplies
the complete construction in this research round, independent of an
unwritten modification to an earlier checkpoint. It verifies

```text
                           x^2=1+yM
```


with n'-bit x,y, a signed base-beta carry vector, and three grouped
forward finite-field transforms. The frequency equations compare the
squared transform of x, the transform of y times the known transform
of M, and the transform of the signed carries. A sufficiently large
polynomial-size prime field makes the bounded integer carry equations
equivalent to their field congruences. Binary comparators impose
0<x<M-1 and x even.

This network has O(n') edges, maximum degree O(sqrt(n' log n')), and
polynomial-size descriptions. Each root x in R has exactly one extension:
y=(x^2-1)/M is a unique nonnegative integer less than M, all signed
carries are unique, and all canonical transform values are unique.
Thus there are exactly t distinct x witnesses. Only the free unary
tensors at the x input bits are changed below. Every arithmetic
verification tensor retains its 0/1 value.

## 3. A small characteristic-two algebra encoding all required moments
Construct an explicit field F=GF(2^r), with r the least power of two at
least n'. Thus n'<=r<2n', except for a harmless bounded-size convention.
Choose a fixed F_2-basis alpha_0,...,alpha_(r-1), with alpha_0=1.

For clarity, this field has a direct deterministic polynomial-time
construction. Begin with F_2 and a_0=1. At stage j adjoin z_j satisfying
z_j^2+z_j+a_j=0 and set a_(j+1)=a_j z_j. The absolute trace of a_j is 1
inductively: the new generator has relative trace 1, so a_j z_j has
relative trace a_j. The Artin--Schreier polynomial is therefore
irreducible at every step. After log_2 r stages, the tower monomials
provide the desired field and basis. Arithmetic and traces in this
explicit tower take polynomial time in r.

Put q=kappa+1, so 2^q=2K. Form the internal F_2-algebra

```text
        A=F[z_0,...,z_(q-1)]/(z_0^2,...,z_(q-1)^2).
```


This notation is separate from the field-tower generators above. Its
F_2-dimension is

```text
                          D=r 2^q=2rK.
```


Index a basis by (S,u), where S is a subset of {0,...,q-1} and
0<=u<r; the basis element is alpha_u product_(j in S) z_j.

For a in F define

```text
                   E_a=product_(j=0)^(q-1)(1+a^(2^j) z_j).
```


Because the characteristic is two and z_j^2=0,

```text
                            E_a E_b=E_(a+b).
```


The coefficient of the monomial indexed by the binary mask v of S is
a^v. Thus E_a stores precisely the powers a^0,...,a^(2K-1), one in each
squarefree monomial coordinate. This identity uses neither division nor
two-adic exponentials.

Encode an integer x by

```text
              a(x)=sum_(i=0)^(n'-1) alpha_i bit_i(x) in F.
```


This map is injective on n'-bit integers. Summing E_(a(x)) over x in R
therefore stores the first 2K power sums of t distinct field elements.
The next sections compute these coordinates using the literal external
tensor ring.

## 4. Grouped regular-representation tensors
Take the external theorem's size parameter s=n. Partition the n' x bits
into G consecutive groups of size at most

```text
                       g=floor(n^(9/10)/4).
```


For sufficiently large n, G=O(n^(1/10)). For a group assignment, compute
the field element a_group equal to the sum of its assigned alpha_i bits.
Let B_group be the D-by-D matrix over F_2 for multiplication by E_a_group
on A. Every entry is a bit.

An entry is particularly simple to evaluate. For source basis (S,u)
and target basis (T,v), it is zero unless S is a subset of T. If S=T,
the entry is 1 exactly when u=v. If S is a proper subset of T, it is
the alpha_v coordinate of

```text
              alpha_u a_group^(mask(T\S)) in F.
```


This is polynomial-time finite-field arithmetic. No exponential truth
table for the group is materialized.

Replace the free x-bit unary tensors in a group by a tensor whose ports
are those input bits together with a source and a target state index,
each encoded in d=ceil(log_2 D) Boolean bits. Invalid indices >=D have
entry zero. Link the group tensors as a matrix-product chain and pin
the initial state to the basis element 1. The final state remains free.

Modulo two, for every satisfying x assignment this chain computes the
coordinate vector of

```text
                       product_groups E_a_group=E_(a(x)).
```


The added chain uses O(G log D)=o(n) Boolean edges. A group tensor has
at most g+2d<=n^(9/10) ports for all sufficiently large n. The old
arithmetic verifier also satisfies this degree bound. Equality
subdivision makes the full graph bipartite while preserving O(n) edges
and all tensor values. Descriptions and entry computation are uniform
and polynomial in n.

## 5. A short monotone path bound prevents output-lane carries
For the moment, view all the 0/1 matrices as ordinary integer matrices.
For each final coordinate i, let H_i be the nonnegative integer obtained
by summing its matrix-chain paths over all t satisfying root witnesses.
Its parity is the desired coordinate of sum_(x in R) E_(a(x)).

The raw counts H_i are much smaller than a general D-state G-step path
bound suggests. At every nonzero transition, the monomial mask S can
only increase under set inclusion. When it stays unchanged, the field
index must also stay unchanged because the same-mask block is exactly
the identity. Thus every path has at most q state-changing transitions.

Choose their positions among the G groups and overbound each new state
by D possibilities. It follows that

```text
 H_i <= K sum_(j=0)^q binom(G,j) D^j
     <= K(q+1)(GD+1)^q.
```


Choose the integer guard width

```text
 W = kappa + ceil(log_2(q+1))
     + q(ceil(log_2(G+1))+ceil(log_2 D)) + 3.
```


Then every H_i<2^W, and W=O(log K log n). This bound is independent of
G in the exponent outside its logarithm; the square-zero algebra is
what makes this possible.

Set

```text
          Q=ceil(D/n),   ell=ceil(D/Q)<=n,   P=QW.
```


Attach to the final state i<D the output tensor weight

```text
                       2^((i mod Q)W) V^(floor(i/Q))
```


in the literal ring R=(Z/2^P Z)[V]/(V^ell); invalid states receive zero.
All other tensors have entries 0 or 1 in this same ring. The coefficient
of V^j in the contraction is the ordinary integer

```text
                  sum_(floor(i/Q)=j) H_i 2^((i mod Q)W).
```


Because H_i<2^W, its base-2^W lanes do not overlap. It is strictly below
2^(QW)=2^P, so the ring residue determines this integer exactly. Extract
the lanes and reduce each H_i modulo two. This obtains every coordinate
of sum_(x in R) E_(a(x)) in the internal algebra.

Since D=O(nK), Q=O(K), and W=O(log K log n),

```text
                        P=O(K log K log n)=n^{o(1)}.
```


In particular P<=n for all sufficiently large n. Thus both P and ell
meet the original theorem's O(s) requirements with s=n. The algebra A
was only a way to define efficiently computable binary matrix entries;
the theorem is never invoked on A or on a coefficient-field extension.

## 6. Polynomial-time recovery of all roots and all prime factors
Decode the field power sums

```text
                     mu_v=sum_(x in R) a(x)^v in F,
                     0<=v<2K,
```


from the recovered coordinate parities. The number t of roots need
not be known or recovered as an exact integer count in the contraction.
Form the K-by-K Hankel matrix H=(mu_(i+j))_(0<=i,j<K).

Writing the distinct encodings as x_1,...,x_t, let V be the K-by-t
Vandermonde matrix V_(i,j)=x_j^i. Then H=VV^T. Since t<=K, V has full
column rank t and V^T has full row rank t. Their product has rank t:
V^T maps onto F^t and V injects F^t into F^K. Hence Gaussian elimination
determines the exact t in characteristic two. If the rank is zero,
R is empty, so M is a prime power; recover its prime base by exact integer
root extraction and finish. For example, test exponents up to n' and
choose the largest exponent representing M as a perfect power; if none
exists, M itself is prime under this established prime-power guarantee.

The leading t-by-t Hankel matrix is invertible, because its Vandermonde
factor is square and invertible. Solve

```text
 (mu_(i+j))_(0<=i,j<t) (c_0,...,c_(t-1))^T
                         = (mu_t,...,mu_(2t-1))^T.
```


The resulting monic polynomial

```text
                   P_root(X)=X^t+sum_(j=0)^(t-1)c_j X^j
```


is product_(j=1)^t (X-x_j). This follows by multiplying the equations
out and using invertibility of the square Vandermonde matrix.

Split P_root deterministically using field traces. For each F_2-basis
element beta_i of F, compute Tr_(F/F2)(beta_i X) modulo P_root by repeated squaring,
then split every current factor with gcd against this trace polynomial
and against its sum with 1. The trace pairing is nondegenerate, so these
r binary trace maps distinguish every pair of distinct roots. All
factors are linear after the r basis elements have been processed.
The work is polynomial in r and t, and hence polynomial in n.

Decode each field root in the alpha basis to recover every integer x in
the set R. For each, form d_x=gcd(M,x-1). Every d_x is a unitary divisor:
for each prime-power component p_i^(e_i), the root x is either +1 or -1
modulo that entire component, and oddness prevents the component from
dividing both x-1 and x+1. Thus d_x contains each prime-power component
either in full or not at all.

These divisors separate all distinct prime-power components. Given two
components i and j, choose a CRT sign vector with opposite signs at
i,j. Exactly one of its two negated roots is even; it is nontrivial and
was not excluded from R. Its gcd d_x includes exactly one of those two
components. Repeated gcd refinement of M by all the d_x therefore
produces precisely the individual prime-power blocks. There are at most
K roots and at most n' blocks, so this step is polynomial-time. Exact
integer root extraction on each block gives its prime and multiplicity.
Together with the preliminary small factors, this is the complete prime
factorization of the original N.

## 7. Resources, alternatives, and limits
There is one contraction whenever M>1 remains after trial division.
The graph has O(n) Boolean edges, maximum degree at most n^(9/10), and
polynomial-size descriptions. Tensor entries are uniformly polynomial-
time computable. The literal ring has ell<=n and P=n^{o(1)}. All
decoding, field construction, linear algebra, trace splitting, and final
factor extraction are polynomial-time and polynomial-space.

Under the assumed tensor theorem, the contraction costs
2^{O(n/sqrt(log n))}; the preceding trial division has strictly smaller
exponent O(n loglog(n)/log(n)). The complete result is deterministic for
all inputs, including unbalanced semiprimes, prime powers, and integers
with many prime factors. No randomized isolation, prime selection, or
finite-field splitting is used.

A different roughness tradeoff is possible. Taking a trial exponent
h=Theta(n/sqrt(log n)) gives K=2^{O(sqrt(log n))} and hence
P=2^{O(sqrt(log n))}, while the preprocessing then shares the same
asymptotic time scale as the contraction. The chosen parameters above
keep preprocessing strictly lower order. Neither choice improves the
leading contraction exponent itself.

The packing lemma also illustrates why a coefficient-algebra extension
need not always be assumed: its regular representation can sometimes be
compiled into bounded-degree Boolean tensors, and a monotone state-path
bound can make all coordinates accessible through guarded integer lanes.
Here the square-zero algebra provides the required short path bound.

Primary dependency
https://github.com/openai/math/blob/main/preprints/The-Exponential-Time-Hypothesis-is-False-October-25-2026/build/quantitative-reduction.tex
https://github.com/openai/math/blob/main/preprints/The-Exponential-Time-Hypothesis-is-False-October-25-2026/build/quantitative-contraction.tex

**Attribution:** Yilin Liu and GPT-6 Astra Pro.
