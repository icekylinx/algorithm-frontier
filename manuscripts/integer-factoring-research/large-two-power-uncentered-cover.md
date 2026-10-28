# Large two-power modulus: a globally uncentered coefficient cover

<!-- imported-source: checkpoint_10_general_factoring_theory_2026-10-27.zip; large_two_power_uncentered_cover_2026-10-27.txt; sha256=43aa16a8120c8b5e6d9740d515718cbb358b1f22d1e1a0f6b7de5bfa3db13d2f -->

**Scope:** retained separate research branch; not part of the selected conditional theorem review. See the [curated dependency and review map](../../problems/integer-factorization/sources.md).

Internal research note, 27 October 2026. This is a structural reduction,
not a new improvement of the current N^(1/5) bound by itself.

## 1. Cover and exact labels
Let N=pq, p<q, with p>P0. Let s be a small odd squarefree primorial,
let m=2^e s, and choose an integer m0=O(1). Put R=m*m0, so m~R.
The usual coefficient lattice at the existence-only anchor p is

```text
    Lambda_p={(a,b): bp^2=aN mod m}.
```


Under (a,b)->(aq,m0(bp-aq)), its determinant is NR. A shortest
nonzero vector therefore satisfies, with harmless absolute constants,

```text
    |aq| <= 2 sqrt(NR),    |bp-aq| <= 2 sqrt(NR)/m0.
```


Take P0>4 sqrt(NR)/m. Then a=0 is impossible, because m|b would
give |bp|>=mp>4sqrt(NR). Also b=0 is impossible once m>2sqrt(R),
because m|a and |aq|>=m sqrt(N). Change the sign to ensure a>0;
b is allowed to be positive or negative. Consequently

```text
    0<|ab|<=8R,       |u=aq+bp|<=6sqrt(NR).
```


No approximation of sqrt(ab), and no real-valued centering, is needed.
For any sigma=p mod m, the stationary congruence bp^2=aN mod m
implies that

```text
    u = aN/sigma + b sigma mod m^2.
```


The right side is independent of the lift of sigma, because its first
derivative vanishes mod m. Enumerate its possible phase residues tau
mod m^2. All true u lie in

```text
    u=tau+m^2 i,     |i|<=ceil(6sqrt(NR)/m^2)+1
                         =O(sqrt(N)/R^(3/2)).
```


Thus giants beta^(aN+b-tau) and one universal signed geometric baby
interval have the usual width but no floor-square-root phase. Labels
aN+b-u are positive: aN+b>=N-8R, whereas every padded candidate u
has size O(sqrt(NR)+m^2 loglog N)=o(N) for R=N^(1/5+o(1)).

The content g=gcd(a,b) divides m. Indeed, if a prime occurs to a
larger exponent in g than in m, division by that prime preserves
Lambda_p and shortens the vector. Write g=2^t h, 0<=t<=e, h|s.
The normalized pair (A,B)=(a/g,b/g) is primitive; its exact gcd may
be weakened to gcd(A,B,2s)=1 in an enumerated superset.

## 2. The large 2-power contributes only a constant to root counts
The stationary congruence always gives

```text
    tau^2=4abN mod 2^(2e).
```


If t<e, a/g and b/g must both be odd whenever a stationary residue
exists. All square roots of 4abN mod 2^(2e) may safely be retained,
instead of just the stationary-image roots. Their number is at most
8*2^t. If t=e, their number is at most 2^e. For t<e-1 this follows
by writing tau=2^(t+1)z and applying the at-most-four-root theorem
for odd squares mod powers of two; the missing high bits give
2^(t+1) lifts. For t=e-1 or e the congruence is tau^2=0 mod 2^(2e).
Existence for the odd normalized square condition is decided mod 8
(with the familiar mod 2 or mod 4 exceptions at the top levels).
Roots can be constructed by binary/Hensel lifting in polynomial
bit time plus their output size. No unknown-prime square root is used.

At each odd ell|s, retain exactly the same stationary image as in
content_hyperbola_sieve_2026-10-27.txt, including its signed padding
at the selected odd primes. Multiplication by 2^t changes only a unit
scaling and does not affect the row-average formulas. The count for
the 2^t class has coefficient area reduced by 2^(2t) and root weight
at most O(2^t); summing over t gives the convergent series sum 2^-t.

With L=log N, H=loglog N and s=N^delta, the same row-mean/Rankin
argument therefore gives the dyadic total

```text
    n_W = O(W L/H^(3/2) + s^3 sqrt(W) H L).
```


The additional L in the crude boundary is from at most e+1 values
of t; the main term has no extra factor. Every root phase has O(L)
bits despite m~R. Odd-period lookup tables use modulus s^2, not m^2.
The root-generation cost may be charged to successful coarse records:
each pair has at least J~L signed leaves at the selected odd primes.
Hence O(L^3) per pair/coarse phase still fits O(n_W L^2).

## 3. Remaining kernel question
The existing sign trie and geometric scalar-blocking theorem apply
unchanged, with a canonical CRT residue for the large 2-part included
in the unselected phase. Carry padding is O(loglog N). They recover
the same general asymptotic bound after optimizing R. This note does
not improve it.

The cleaner unresolved product now has labels

```text
    aN+b-tau-m^2 i,
    0<|ab|<=O(R),    tau^2=4abN mod 2^(2e),
    |i|<=O(sqrt(N)/R^(3/2)),
```


with the small odd stationary-image conditions. The real floor and
the narrow real Taylor patch have disappeared. A useful new kernel
would exploit this 2-adic conic structure directly without expanding
all (a,b,tau) roots or inflating the signed baby interval.

## 4. Alternative: a large squarefree modulus, using Burgess
The same uncentered reduction can use a squarefree m~R, rather than
a large power of two. This gives a clean complete root-count proof
with a power-saving error, at the cost of invoking Burgess in addition
to its existing use in period recovery. The parent independently
checked the main count and supplied the sparse setup below; a further
complete independent audit and external review remain appropriate.

Choose an initial primorial s maximal below R/(4 log R). Its last prime
is Theta(log R). Choose a fresh prime ell0 in [R/(2s),R/s], using
Bertrand; ell0>2 log R lies above all prime factors of s, and ell0 is
O((log R)^2). Put m=s*ell0, so R/2<=m<=R, and use actual R'=m (or a
fixed constant times
m) in the lattice cover. All asymptotic optimization parameters are
therefore preserved up to absolute constants. The extra prime changes
the relevant Mertens products only by constant factors. If it divides
N, a factor is obtained immediately.

Let v_g(A,B) be precisely the signed/padded stationary-image weight
from the main content-sieve note, for g|m and gcd(A,B,m)=1. At an odd
prime ell not dividing g its local factor is

```text
    1_(ell∤A) 1_(ell∤B) + chi_ell(ABN).
```


At ell|g, write I_A=1_(ell∤A), I_B=1_(ell∤B). Its local factor is

```text
    c_ell I_A I_B + b_ell chi_ell(ABN)
       +(ell-1)[(1-I_A)I_B+I_A(1-I_B)],
```


where (c_ell,b_ell)=(ell/2,1/2) if unselected, and

```text
    (c_ell,b_ell)=((ell+1)/2,(1+chi_ell(-1))/2)
```


if selected. The selected formula uses that zero belongs to the image
exactly when chi_ell(-ABN)=1, and the signed representation pads zero
by one duplicate. The prime 2 is a bounded periodic factor.

Fix A. Expanding these factors and the zero-residue indicators gives
at most C^omega(m)=m^o(1) terms, each with coefficient O(g), consisting
of a quadratic character in B times divisibility conditions. The
principal-character contribution to the prefix sum through B<=Y is
exactly Y*f_g(A), up to O(g*m^o(1)); f_g is the same row mean as in the
main note. A nonprincipal character has squarefree conductor d|m.
After inclusion-exclusion, a divisibility condition B=kz is either
zero or reduces to a character sum of length floor(Y/k), with (k,d)=1.
Burgess with r=2 gives, for every fixed epsilon>0,

```text
    |sum_{B<=Y} v_g(A,B) - Y*f_g(A)|
       <= C_epsilon*g*m^(3/16+epsilon)*sqrt(Y) + g*m^o(1).
```


Here all C^omega(m) factors may be absorbed by slightly enlarging
epsilon. The usual character bound for intervals longer than d follows
by removing complete periods before applying Burgess. Thus no relation
between Y and d is silently required.

For X=O(R/g^2), use hyperbola symmetry and sum rows A<=sqrt(X),
with Y=X/A. Since sum_{A<=sqrt(X)} A^(-1/2)=O(X^(1/4)), their total
nonprincipal error is

```text
    O_epsilon(g*m^(3/16+epsilon)*X^(3/4))
       =O_epsilon(R^(15/16+epsilon)/sqrt(g)).
```


Summing over g|m contributes only m^o(1), since
sum_{g|m}g^(-1/2)=prod_{ell|m}(1+ell^(-1/2))=m^o(1).
The principal term is bounded by exactly the old Rankin argument,

```text
    O(R L * sum_{g|m} c_g/g^2)=O(R L/H^(3/2)).
```


Consequently the whole signed, uncentered giant family satisfies

```text
    n=O(R L/H^(3/2) + R^(15/16+epsilon)),                 (4.1)
```


for each fixed sufficiently small epsilon>0. This argument is uniform
in N coprime to m. Negative b changes a local character sign but not
the principal means or the absolute Burgess bound.

No complete modulus-m or modulus-m^2 table is needed. Let s0|m be a
tiny initial primorial of size N^(delta+o(1)), delta=1/1000. Precompute
the allowed residue rows (a,b mod s0^2): at every odd ell|s0 allow
both units with chi_ell(Nab)=1, or both divisible by ell but not both
by ell^2. Reject the exactly-one-zero cases. The prime 2 is harmless.
Every true primitive lattice vector passes this necessary filter.
For each fixed a, the permitted b residues occupy at most half of the
residues at each odd ell: for a unit the fraction is (ell-1)/(2ell),
and for a nonunit it is at most 1/ell. Thus the row density is at most
2^(-omega(s0)+O(1)), uniformly in a. Enumerating b progressions in these
rows, and using the shorter coordinate to traverse the hyperbola,
produces at most

```text
    O(R L*2^(-omega(s0)) + s0^2 sqrt(R))
```


prefix survivors, with O(s0^2 sqrt(R)) table-visit overhead. Even
O(L^3) full local/content arithmetic per survivor is lower order:
2^(-omega(s0)) decreases faster than every inverse power of L, and
s0^2 sqrt(R)=N^(1/10+2delta+o(1)). The precomputed small table itself
has polynomial-in-s0 size and remains below N^(1/5).

Individual local image/root tables for the full modulus have only
polynomial-in-L size, since every prime factor of m is polynomial in L.
All expensive CRT-root exponentiations are charged to successful coarse
records, each supporting J~L signed leaves, as before. Therefore this
sparse setup does not rely on doing O(L^3) work for every pair in the
unsieved O(R log R) hyperbola.

Use a single universal baby length K=O(sqrt(N)/R^(3/2)); no W buckets
are necessary in the uncentered version. The sign trie plus scalar
blocking costs O((n+sqrt(nK))*L^2). The error term from (4.1) contributes

```text
    O_epsilon(N^(1/4) R^(-9/32+epsilon/2) L^2).
```


At R=N^(1/5+o(1)), this is N^(31/160+epsilon/10+o(1)), strictly below
N^(1/5) when epsilon is fixed small. The main term therefore recovers
the same bound as the content-sieve checkpoint:

```text
    O(N^(1/5) L^(13/5)/H^(9/10)).
```


This is a structurally simpler alternative, not an additional speedup:
the uncentered labels are exactly aN+b-tau-m^2 i, with tau satisfying
known local stationary-image conditions, and contain no real-floor
function. It is intended as a cleaner starting point for a new product
kernel.

**Attribution:** icekylinx and GPT-6 Astra Pro.
