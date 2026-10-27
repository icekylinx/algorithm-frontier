# CRT SIGN-CUBE PREPROCESSING AND ZERO-FREE AUDIT

<!-- imported-source: checkpoint_10_general_factoring_theory_2026-10-27.zip; crt_preprocessing_audit_2026-10-27.txt; sha256=ac23bc946d5e8a8f9d4aeb3dc64c3d4fb79c3404713a2c09e6368bd1c68eb3df -->

**Scope:** retained separate research branch; not part of the selected conditional theorem review. See the [curated dependency and review map](../../problems/integer-factorization/sources.md).

Independent preprocessing audit, 2026-10-27.

This note supports the proposed compressed HH giant-product construction.
It is an internal proof audit, not a novelty claim or a substitute for the
complete factoring theorem.

Notation.
```text
  L = ceil(log_2 N), m is a squarefree primorial containing 2,
  w = omega(m), Q = 2^(w-1), R = m*m0,
  lambda = ceil(4*sqrt(N)/R^(3/2)).
```

The HH scale list starts at ceil(N^(1/3)) and ends below sqrt(N). Let S
be its size; S=O(m0*L). The expanded giant multiset has
```text
  n = phi(m)*S
```

entries. Choose the first k odd primes dividing m, with
```text
  k = ceil(log_2 L), J = 2^k.
```

All asymptotic statements concern sufficiently large N; any finite
exceptional range can use a fixed deterministic factoring algorithm.

## 1. Coefficients really are invariant under independent local signs.

In HH Proposition 3.3 the integer lattice is
```text
  b = (N/sigma^2)*a (mod m),
```

and its real linear change of variables uses only N,m,m0,sigma0.
Consequently one deterministic short-vector computation per global
square class sigma^2 (mod m), per scale sigma0, gives a single pair
(a,b) valid for all Q roots in that class. The centering value
```text
  C = a*N/sigma0 + b*sigma0,
  tau0 = floor(C/m^2)
```

has the same invariance.

For an odd prime ell dividing m, choose any unit lift s of the local
residue sigma modulo ell and put
```text
  t_ell = a*N/s + b*s (mod ell^2).
```

This is independent of the lift s (mod ell): replacing s by s+ell*z
changes it by
```text
  ell*z*(b-a*N/s^2) = 0 (mod ell^2),
```

because the lattice relation holds modulo ell. Replacing the residue
s by -s negates t_ell modulo ell^2. No invertibility of a or b is used.
The prime 2 is left among the unselected coordinates.

Let E_ell be the standard CRT projector modulo m^2, equal to 1 modulo
ell^2 and 0 modulo the other prime squares. Choose
```text
  w_ell = E_ell*t_ell mod m^2,  0 <= w_ell < m^2.
```

For fixed selected local weights there are at most ell^2 choices at the
ell-coordinate, independently of the factor scale and of (a,b).

## 2. Exact carry and the enlarged baby interval.

Enumerate the signs at all unselected odd primes. For each such coarse
choice reduce their CRT sum, including the fixed prime-2 contribution,
to a single integer tau_rest in [0,m^2). Leave only the k selected signs
unreduced. Thus
```text
  T(epsilon) = tau_rest + sum_{selected ell} epsilon_ell*w_ell,
  -k*m^2 <= T(epsilon) < (k+1)*m^2,
  floor(T(epsilon)/m^2) in [-k,k].
```

The canonical HH residue is tau=T(epsilon) mod m^2.

Replace the HH center m^2*(tau0-lambda)+tau by
```text
  j(epsilon) = m^2*(tau0-lambda-k) + T(epsilon).
```

If the original genuine baby index is i0 in [0,2*lambda], the new one is
```text
  i = i0 - floor(T(epsilon)/m^2) + k,
```

and lies in [0,2*lambda+2*k]. Therefore
```text
  kappa = 2*lambda+2*k+1
```

is sufficient. If a subsequent baby aggregation pads to a multiple of
h, all tested indices lie in [0,2*lambda+2*k+h-1].

## 3. All tested integer periods are nonzero.

Put
```text
  D = b*sigma0 - a*N/sigma0,
  E1 = 2*sqrt(N)*m/sqrt(R),
  W  = 4*sqrt(N)*m^2/R^(3/2).
```

HH gives |D|<=E1. For any padded candidate
```text
  U = j(epsilon) + m^2*i
```

the carry calculation gives
```text
  |U-C| <= W + (2*k+h+2)*m^2.
```


If a is nonzero, the exact identity
```text
  a*N+b-C
    = a*N*(1-1/sigma0)^2 - D*(1-1/sigma0)
```

implies
```text
  |a*N+b-C| >= N/4-E1
```

for sigma0>=2. If a=0, the lattice congruence forces m|b, and b is
nonzero. Hence
```text
  |a*N+b-C| >= m*(N^(1/3)-1).
```

For m<=N^(1/20), R=N^(1/5) times powers of logarithms, and h bounded by
a power of L, both lower bounds dominate W+O((k+h)*m^2). Thus every
integer label
```text
  d = a*N+b-U
```

tested by the compressed product is nonzero. Duplicate roots caused by
t_ell=0 are harmless and can be retained as squarings. No deletion
polynomial is needed under these parameter choices.

## 4. Construction of m and the selected primes costs only polylog N.

Take the maximal initial prime product satisfying m^40<=N. Generate the
primes and check gcd(ell,N), returning a factor if necessary. Standard
Chebyshev bounds imply that only primes O(L) are examined. Consequently
all this work, including trial division, prime generation, exact product
comparisons, and the CRT projectors, costs a fixed polynomial in L.
The previous product and the next prime show
```text
  N^(1/40)/(O(L)) <= m <= N^(1/40).
```

Mertens' product theorem gives phi(m)/m=O(1/log L), as in HH.

There are enough selected odd primes. Indeed the product of the first
k=O(log L) odd primes is exp(O(k^2)) even using only Bertrand's bound;
this is N^o(1), hence less than the chosen primorial for large N.
In particular Q>=J>=L.

## 5. Enumerating coarse data and evaluating their base phases.

There are exactly phi(m)/Q global square classes, and Q/J coarse sign
choices per class. Across all scales:
```text
  short-vector computations: n/Q;
  coarse base records:        n/J.
```


Each short-vector calculation costs O(L^3) using HH's existing bound.
At the same cost one can compute the center and all local residues by
ordinary integer arithmetic: w=O(L), and each operation on O(L)-bit
integers is bounded by O(L^2). Thus all class/scale work costs
```text
  O((n/Q)*L^3) <= O(n*L^2).
```


For each coarse record, computing tau_rest, the exact exponent
```text
  e0 = a*N+b - m^2*(tau0-lambda-k) - tau_rest,
```

and beta^e0 modulo N costs O(L^3). The exponent has O(L) bits, by the
HH coefficient bounds. Negative exponents use the already-known inverse
of beta. Therefore all coarse base generation costs
```text
  O((n/J)*L^3) <= O(n*L^2).
```


One can precompute all unit residues and their square/sign class data
modulo m by direct enumeration, sorting, and CRT arithmetic. Even a
coarse bound m*poly(L) is negligible because m=N^(1/40+o(1)), whereas
n=N^(1/5) times logarithmic factors in the target parameter regime.
This eliminates any need for an unstated fast modular-square-root
algorithm or expensive on-line class identification.

The selected weight tuple has bitlength
```text
  sum_{selected ell} log_2(ell^2) = O((log L)^2),
```

using Bertrand alone; the prime number theorem improves this to
O(log L*log log L). Sorting the n/J coarse records by these tuples and
building a sparse trie costs O((n/J)*poly(L)) within the same O(n L^2)
budget with standard O(L)-bit record representations. For example,
comparison sorting requires O((n/J)*L*log(n/J))=O(n L).

## 6. Interface to the polynomial trie.

For a monic polynomial F whose roots are the coarse phases, expanding
one common signed weight w means replacing F by
```text
  F(beta^w X)*F(beta^(-w) X).
```

Its roots are the two corresponding multiplicative translates, and it
remains monic. Zero weights may use F^2, preserving the uniform count.
At depth j the total degree, over all nonempty trie nodes, is at most
```text
  n / 2^(j-1).
```

Each node merges at most ell_j^2 child polynomials. With polynomial
multiplication of degree D in O(D L^2) bit operations, the total merge
cost is bounded by
```text
  O(n L^2 * sum_{j>=1} 2^(-j) log ell_j) = O(n L^2).
```

Bertrand's ell_j<=2^(j+O(1)) already proves convergence of this sum.
All signed expansions cost O(n L^2) as well. The leaf product trees
cost O((n/J)L^3)=O(n L^2).

## 7. Recovery does not require redoing n lattice calculations or powers.

If one evaluated f(alpha^i) has gcd N, regenerate the roots using their
stored coarse base phases and Gray-code selected sign changes. One
selected sign change multiplies by the known unit beta^(+/-2*w_ell).
These units can be precomputed per selected local weight. The exact
integer exponent can be updated simultaneously in O(L) bit additions.
Thus scanning all n roots, computing gcds, and selecting the first
nonunit costs O(n L^2), without restoring an n L^3 term. A proper gcd
factors N; a full-N leaf gives a nonzero O(L)-bit period by Section 3,
to which the separately audited amortized period-recovery theorem applies.

Sources for the imported pieces:
```text
  Harvey--Hittmeir, arXiv:2105.11105, Proposition 3.3 and Algorithm 4.3.
  The short-vector, fast integer/polynomial arithmetic, CRT, Mertens,
  and Chebyshev facts are standard ingredients already used in that paper.
```

**Attribution:** Yilin Liu and GPT-6 Astra Pro.
