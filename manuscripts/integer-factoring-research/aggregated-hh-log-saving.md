# AGGREGATED GEOMETRIC COLLISIONS IN THE HARVEY--HITTMEIR SEARCH

<!-- imported-source: checkpoint_10_general_factoring_theory_2026-10-27.zip; aggregated_hh_log_saving_2026-10-27.txt; sha256=e77640ee75c3aa915245333b4f99f1dd7c2f11f35005f841547eea2bd9cdf159 -->

**Scope:** retained separate research branch; not part of the selected conditional theorem review. See the [curated dependency and review map](../../problems/integer-factorization/sources.md).

Research checkpoint, 2026-10-27. Draft theorem and proof; novelty unassessed.

CLAIM UNDER AUDIT
The explicit constructions below, together with the deterministic short-period
recovery theorem in deterministic_period_recovery_amortized_2026-10-27.txt,
give general deterministic integer factorisation in

```text
  O( N^(1/5) (log N)^(14/5) / (log log N)^(3/5) )
```


bit operations. This improves a logarithmic factor in the 2021 HH bound;
the power N^(1/5) does not change. No hypothesis concerning compressed
products, random collisions, or a new analytic zero-free theorem is used.
The statement needs further independent/external review before a novelty claim.

PRIMARY INPUTS
[HH] D. Harvey and M. Hittmeir, A log-log speedup for exponent one-fifth
deterministic integer factorisation, arXiv:2105.11105 (2021).
https://arxiv.org/pdf/2105.11105
Needed facts are Lemmas 2.1--2.5, Proposition 3.3, and the giant-label
construction and count in Algorithm 4.3 / Proposition 4.4.
[H] D. Harvey, An exponent one-fifth algorithm for deterministic integer
factorisation, arXiv:2010.05450 (2020).
https://arxiv.org/pdf/2010.05450
[BN] The classical Burgess--Norton least quadratic nonresidue bound, as
stated in P. Pollack, Bounds for the first several prime character
nonresidues, arXiv:1508.05035, Theorem 1.1.
https://arxiv.org/pdf/1508.05035
[BY] A. Bostan and S. Yurkevich, Fast computation of the N-th term of a
q-holonomic sequence and applications, arXiv:2012.08656 (2020), Algorithm3,
Section3.4 and Theorem5. This already supplies the geometric factorial
blocking construction used below. The scalar construction is valid over
Z/NZ with unit q; it uses no inverses of nonunit differences.
https://arxiv.org/pdf/2012.08656

## 1. BIT-ARITHMETIC CONVENTIONS

Put L=ceil(log_2 N) and l=ceil(log_2 L); all asymptotic statements are for
sufficiently large N. Polynomial degrees below are O(N), coefficients are
represented in Z/NZ, and integer labels have O(L) bits. Standard fast
integer multiplication and Kronecker substitution give multiplication of
degree-d polynomials in O((d+1)L^2) bit operations. Constructing a polynomial
from n arbitrary supplied roots costs O(n L^3) by a product tree [HH, Lem2.1].
Evaluating degree-d f at 1,q,...,q^(k-1), for any unit q, costs
O((d+k)L^2) by Bluestein's algorithm [HH, Lem2.3]. No order or distinctness
condition on these geometric points is required for evaluation itself.

## 2. AGGREGATED COLLISION LEMMA

Suppose unit roots v_1,...,v_n are supplied, q is a unit, and the baby
indices are 0<=i<K. Let h be a power of two. Pad the range to
K'=h ceil(K/h), and suppose that a nonunit leaf q^i-v_j is guaranteed
somewhere in the original range. Assume every full-N leaf in the padded
range comes with a nonzero short integer period of a prepared base beta.
Then a proper factor, or such a period, can be found at bit cost

```text
  O( n L^3 + (n h + K/h + 1)L^2 ).                 (A)
```


Proof. Construct f(X)=product_j (X-v_j). Put F_1=f and, successively for
t=1,2,4,...,h/2, compute

```text
  F_(2t)(X)=F_t(X) F_t(q^t X).
```


Then F_h(X)=product_(0<=j<h) f(q^j X), of degree nh. Scaling coefficients
uses O(nt) ring multiplications; multiplication costs O(nt L^2). Summing
the geometrically increasing degrees gives O(nh L^2), with NO extra log h.
Evaluate F_h at 1,q^h,...,q^(h(ceil(K/h)-1)) by geometric evaluation. The
cost is O((nh+K/h+1)L^2).

Scan gcds of the output values with N until the first nonunit value. A
proper gcd already splits N. If its gcd is N, evaluate f by Horner at the
h babies in that block, until a nonunit f-value is found. This costs at
most O(nh) ring multiplications; no recursion or product reconstruction is
necessary. A proper gcd again splits. Otherwise scan the n individual
differences v_j-q^i at that baby until a nonunit leaf is found. This gives
a proper factor or a full-N leaf. Gcd and scan costs are dominated by (A).
The guarantee of some nonunit leaf ensures that this procedure terminates.

This is the scalar geometric factorial / q-shift construction of [BY].
The building block itself is established prior art. Its useful consequence
is that the price of all K baby outputs is replaced by nh+K/h, because
the recovery theorem allows stopping at ANY nonunit leaf, including a
full-N collision.

## 3. PREPARATION USING ONLY PRE-2026 INPUTS

First remove powers of 2 and handle primality and pure perfect powers by
deterministic polynomial-time routines. It suffices to split an odd
composite N that is not a prime power.

Apply [HH, Lem2.5] with D0=ceil(N^(2/5)). This either factors N, certifies
primality, or supplies a unit beta with ord_N(beta)>D0. Its bit cost is
O(N^(1/5)L^2/sqrt(l)), below the claimed final bound.

Set D=ceil(N^(1/3)), s=ceil(sqrt(D)). For sufficiently large N, s^2<D0.
Form Q(X)=product_(0<=i<s)(X-beta^i), evaluate Q(beta^(js)) for 1<=j<=s,
and test gcds. Its factors correspond, up to units, to beta^k-1 with

```text
  k=js-i, 1<=j<=s, 0<=i<s,
```


which cover every integer 1<=k<=s^2 exactly once. No individual leaf has
gcd N, because ord_N(beta)>D0>s^2. Thus any nonunit evaluation reveals a
proper factor by one scan of its s leaves. If all evaluations are units,

```text
  ord_p(beta)>s^2>=D                             (B)
```


for every prime p dividing N. The whole screening step costs
O(N^(1/6)L^3), negligible here. Condition (B) implies p>N^(1/3) for every
prime factor, so N has at most two prime factors counted with multiplicity.
Our input therefore is now a product of two distinct primes. This avoids
any need to extend HH's semiprime statements to more general moduli.

## 4. PARAMETERS AND HH GIANT LABELS

Let m be the product of primes at most floor(L/30), as in HH. If gcd(m,N)
is proper, return it; otherwise m is a unit modulo N. For all large N,

```text
  N^(1/21)<m<N^(1/20),  phi(m)/m=Theta(1/l).
```


Choose

```text
  T=ceil( (N l^2/L^6)^(1/5) ),
  m0=ceil(T/m),  R=m m0,
  lambda=ceil(4 sqrt(N)/R^(3/2)), K=2lambda+1,
  h=2^ceil(log_2 L), K'=h ceil(K/h).
```


These are constructive integer choices; roots of rational numbers can be
rounded by integer root/comparison operations. As m=o(T),

```text
  R=Theta(N^(1/5)L^(-6/5)l^(2/5)),
  K=Theta(N^(1/5)L^(9/5)l^(-3/5)), h=Theta(L).
```


Run ONLY the giant-label generation loop of [HH, Algorithm4.3], Steps4--11.
For each sigma coprime to m and each HH interval anchor sigma0, the routine
produces integers a,b, not both zero, and a label j=j_(sigma,sigma0), with
O(L) bits. Store the unit

```text
  v_g=beta^(e_g), e_g=aN+b-j.
```


The number n of labels is

```text
  n=O(phi(m)m0 L)=O(R L/l),                      (C)
```


and their total generation cost is O(nL^3), using the original (unimproved)
HH two-dimensional lattice routine. Negative e_g use inversion of beta.

The HH covering proof supplies, for some giant and some 0<=i<K,

```text
  aq+bp=j+m^2 i,  and  v_g = beta^(m^2 i) mod p,
```


where N=pq, p<q. Let alpha=beta^(m^2). From (B),

```text
  ord_p(alpha) = ord_p(beta)/gcd(ord_p(beta),m^2)
               > D/m^2 > N^(7/30),              (D)
```


and likewise modulo q. Since K'=N^(1/5+o(1)), these local orders exceed
K'. Thus all babies alpha^i in the padded range are distinct modulo each
prime. This local-order condition is used only for the next filtering step.

## 5. REMOVE EXACT INTEGER-ZERO LABELS, NOT ALL MODULAR COLLISIONS

For each giant, test by exact integer arithmetic whether

```text
  e_g=m^2 i0 for an integer 0<=i0<K'.
```


If so, test whether a is nonzero, a divides b, and t=b/a is an integer
with 1<t<N dividing N. If all these conditions hold, return t. Otherwise
delete this giant. This exact division test also handles signed a,b and
does not presume that both coefficients are nonzero. The test and decoding
cost O(n L log L), below nL^3.

Why deletion is safe: at i0 the equality v_g=alpha^i0 is an integer-label
identity. By (D), every difference v_g-alpha^i with i!=i0 in the padded
range is a unit modulo N. If this giant were the HH witness, its witness
index i would therefore have to equal i0. Then aq+bp=j+m^2 i0=aN+b, so
(p-1)(aq-b)=0 and b=aq. If a=0 this would force b=0, contrary to the
lattice output condition. Thus a is nonzero and t=b/a=q is a proper
factor that the preceding test finds. Consequently, unless factoring has
already succeeded, at least one true witness giant remains after deletion.

The surviving list has no integer-zero leaf. Nevertheless it may contain
arbitrarily many MODULAR full-N collisions and repeated root values. These
are deliberately retained; no separation or multiplicity hypothesis is used.

## 6. RUN AGGREGATION, THEN SHORT-PERIOD RECOVERY ONCE

Use Lemma2 with q=alpha and the surviving giants. If it returns a proper
gcd, finish. Otherwise the returned leaf supplies

```text
  d=|e_g-m^2 i|>0,  beta^d=1 mod N.
```


The strict inequality follows from Step5. The bit length of d is O(L),
because all HH labels have O(L) bits and i<K'=N^(1/5+o(1)). The period is
for the SAME prepared beta satisfying (B).

The separate deterministic period-recovery theorem applies with D=N^(1/3).
It costs, for every fixed epsilon>0,

```text
  soft-O(N^(1/12)) + O_epsilon(N^(kappa+epsilon) polylog N),
  kappa=1/(4 sqrt(e))<1/6.
```


Choose a fixed epsilon with kappa+epsilon<1/6. This is below the preparation
cost and therefore negligible in the final bound. The original main
collision search is not repeated for each base tried by recovery. The
recovery proof and its Burgess--Norton input are in the companion TXT file.

## 7. COMPLETE COST CALCULATION

After (C), Lemma2 yields

```text
  O( (R L/l)L^3 + ((R L/l)h+K/h+1)L^2 )
  = O( R L^4/l + sqrt(N) L/R^(3/2) ).
```


The chosen R balances these two terms and gives

```text
  O( N^(1/5)L^(14/5)/l^(3/5) ).
```


Giant generation has the same R L^4/l bound. The old high-order setup
N^(1/5)L^2/sqrt(l), local screening N^(1/6)L^3, all exact-zero tests,
all output gcds, the one block scan, and one period-recovery call are below
this bound. Polynomial degrees nh and counts K/h are O(N), so every cited
arithmetic subroutine is in its stated parameter regime. The construction
of F_h doubles degrees, hence charges a geometric sum and not nh log h.

Repeatedly splitting composite outputs gives complete factorisation without
an additional log N factor. For any fixed theta>0, for sufficiently large
M and any split M=AB with A,B>=2, A^theta+B^theta <= c M^theta for a fixed
c<1 (the maximum occurs at an endpoint A=2 or B=2). This bounds the total
cost over the factorisation tree by a constant times the root cost; the
bounded-size terminal nodes contribute only polylog N additional work.

## 8. SCOPE AND OPEN QUESTIONS

This is an unconditional logarithmic improvement IF the assembled proof
survives further review. It is not an improvement of the exponent 1/5,
and it is not an RSA break in polynomial or subexponential deterministic
time. The aggregate lemma is established [BY], and the recovery amortisation
draws on established ideas; no priority claim is made. Targeted searches
for the exponent 14/5
and this combination did not locate an identical published bound, which is
not an exhaustive literature review.

The remaining power-exponent target is unchanged: to go below N^(1/5),
one needs a reduction of the number/description cost of giant labels or
a stronger all-target aggregate primitive. Blocking only the geometric
baby sequence yields the actual logarithmic gain above but preserves the
same power balance n versus sqrt(nK).

**Attribution:** icekylinx and GPT-6 Astra Pro.
