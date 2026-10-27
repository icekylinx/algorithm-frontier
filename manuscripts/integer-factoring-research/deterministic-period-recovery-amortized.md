# DETERMINISTIC RECOVERY FROM ONE PERIOD: AMORTIZED VERSION

<!-- imported-source: checkpoint_10_general_factoring_theory_2026-10-27.zip; deterministic_period_recovery_amortized_2026-10-27.txt; sha256=6b81e204e8341453dede14aea2bdf2cdaa91b782e7aca629c2bccbee432561da -->

**Scope:** retained separate research branch; not part of the selected conditional theorem review. See the [curated dependency and review map](../../problems/integer-factorization/sources.md).

Research checkpoint, 2026-10-27

MAIN CONCLUSION AND SCOPE

After preparing a suitable base alpha, one nonzero O(log N)-bit period of alpha is enough to factor an odd integer N with at least two distinct prime factors deterministically, with an ADDITIONAL

```text
    O_epsilon(N^(kappa+epsilon)),
    kappa=1/(4 sqrt(e))=0.151632664928158...
```


bit-operation budget. The expensive procedure that supplies that period is invoked at most once. The period need not be factored. The number Z of full-N collision leaves does not enter this recovery cost.

This is a reduction for a proposed factoring algorithm. It does not supply the missing fast all-target collision-product procedure, and consequently does not establish a new unconditional factoring exponent. It uses established unconditional large-order and quadratic-nonresidue results. No 2026 zero-free-half-plane claim is required.

This note supersedes the earlier non-amortized recovery exponent 0.174375336 for short periods. Its key addition is that only O(log N) trial bases can require an expensive secondary product search. Every unsuccessful such search strictly enlarges a known common divisor of the prime-minus-one orders.

## 1. ESTABLISHED INPUTS AND NOTATION

Let N be odd, composite, and not a power of a single prime. Write its distinct prime divisors as p_1,...,p_s, with s>=2, and its prime-power factorization as N=product p_i^(e_i). This factorization is used only in the proof, not by the algorithm. Let p be the smallest prime divisor, so p<=sqrt(N).

For a unit x modulo N, ord_l(x) denotes its multiplicative order modulo a prime l. Define

```text
    G=gcd(p_1-1,...,p_s-1).
```


The algorithm will maintain an integer C dividing G without knowing G.

We use these established inputs:

* Harvey--Hittmeir (2026), Theorem 1.1: for 1<=D<N-1, deterministically find a proper factor of N or a unit alpha with ord_N(alpha)>D, in soft-O(sqrt(D)) times polylog N bit operations.

* Burgess--Norton, in Pollack's uniform Theorem 1.1 (2017): for every fixed epsilon>0 and every nonprincipal Dirichlet character of modulus Q, a character nonresidue exists at an integer <=O_epsilon(Q^(kappa+epsilon)). Only primitive real characters are needed below.

* Fast univariate polynomial products and multipoint evaluation over Z/NZ. Monic division suffices, so the composite coefficient ring causes no inversion problem.

All soft-O statements suppress logarithmic factors. Integer and ring costs are converted to bit costs using standard fast arithmetic; powers of log N are displayed generically as polylog N. A supplied period of K bits is explicitly charged below.

## 2. ORDERED SECONDARY SEARCH

LEMMA 1 (first nonunit in an order interval).

Given a unit z modulo N and B>=1, let m=ceil(sqrt(B)). In soft-O(m) ring operations and gcds one can either find a proper factor of N, prove that every z^k-1 with 1<=k<=m^2 is a unit, or return the SMALLEST k in [1,m^2] for which z^k-1 is a nonunit, with z^k=1 modulo N.

Construction. Form the monic polynomial

```text
    F(X)=product_{i=0}^{m-1}(X-z^i)
```


and evaluate it at z^(jm), j=1,...,m. The factors have exponents

```text
    jm-i,  i=0,...,m-1,
```


which, for a fixed j, are exactly the integers (j-1)m+1,...,jm. The unit factors z^i do not change gcds with N.

Inspect j in INCREASING order. If gcd(F(z^(jm)),N) is proper, return the factor. If it equals 1, every exponent in this block has a unit value, so continue. At the FIRST block whose gcd is N, inspect i in DECREASING order, from m-1 to 0. Thus the exponents within this block are inspected in increasing order. Return the first proper gcd, if any. Otherwise the first nonunit leaf is a full-N zero and its exponent k is globally the smallest nonunit exponent. Only one block of at most m leaves is scanned.

All exponents lie in [1,m^2]; none is zero. Padding beyond B is harmless. If a nonunit with exponent <=B is known to exist, then the smallest nonunit exponent returned by this procedure is itself <=B.

Minimality has a decisive consequence: if the returned leaf is a full-N zero, then

```text
    ord_{p_i}(z)=k for EVERY distinct prime divisor p_i of N.
```


Indeed, the first nonunit exponent is min_i ord_{p_i}(z). A full-N zero forces each ord_{p_i}(z) to divide k, so all equal k. For repeated prime factors, the order modulo p_i^(e_i) also equals k: it divides k because z^k=1 modulo N and is divisible by the prime-level order k.

## 3. PREPARATION OF THE ORIGINAL BASE

LEMMA 2 (large orders at every prime).

Let D>=1 and D_0=ceil(sqrt(D))^2<N-1. In soft-O(sqrt(D)) polylog N bit operations one can find a proper factor of N or produce alpha satisfying

```text
    ord_{p_i}(alpha)>D_0>=D for every prime divisor p_i of N.
```


Proof. Apply Harvey--Hittmeir with target D_0 to get ord_N(alpha)>D_0, or a factor. Then apply Lemma 1 with z=alpha and B=D_0. This interval has no extra padding because D_0 is a square. A full-N zero with exponent <=D_0 would contradict the global-order guarantee. Thus any nonunit detected gives a proper factor. If none exists, all prime-level orders exceed D_0. End proof.

In particular, every prime divisor of N exceeds D. No factorization of an order is used in this preparation.

## 4. INPUT FROM THE MAIN COLLISION PROCEDURE

For the prepared alpha, assume that a separate deterministic procedure returns a proper factor of N or a NONZERO integer d_0 such that

```text
    alpha^(d_0)=1 modulo N.
```


Let K=ceil(log_2(|d_0|+1)). Replace d_0 by |d_0|. The main procedure may be an adaptive descent in a compressed product family; the period need not have been selected in advance and need not be the exact order.

Define the computable bound

```text
    B=ceil(ceil(sqrt(N))/D).
```


For every positive multiple d of d_0 and every unit b modulo N, there is a k<=B with

```text
    b^(dk)=1 modulo p,
```


where p is the smallest prime divisor. To prove this, let r=ord_p(alpha)>D. Since r divides d and p-1,

```text
    gcd(d,p-1)>=r>D.
```


Thus k_0=(p-1)/gcd(d,p-1)<sqrt(N)/D, and p-1 divides d k_0. Fermat's theorem gives the claim. Therefore every secondary search on z=b^d is guaranteed to encounter a nonunit.

## 5. THE AMORTIZATION INVARIANT

Initialize C=1 and d=d_0. Maintain

```text
    C | G,    d=d_0 C.
```


For a trial base b, first compute gcd(b,N). A proper gcd ends the computation; if gcd(b,N)=N, skip this base. Otherwise compute z=b^d modulo N and its gcd after subtracting 1.

Case A: 1<gcd(z-1,N)<N.
```text
    Return this factor.
```


Case B: gcd(z-1,N)=N.
```text
    The current d is a common period of b. Apply the usual 2-adic Miller procedure. If it gives a factor, return it. Otherwise move to the next base, without changing C.
```


Case C: gcd(z-1,N)=1.
```text
    Call the ORDERED secondary search of Lemma 1 with z and B. If a proper factor is returned, stop. Otherwise it supplies the smallest nonunit exponent k, with z^k=1 modulo N. Since the exponent 1 was a unit, k>=2. Update
```


```text
        C <- C k,    d <- d k.
```


```text
    The new d is a common period of this b; apply the Miller procedure to it. Stop on a factor, and otherwise continue to the next base.
```


LEMMA 3 (invariant preservation and number of expensive calls).

Every update preserves C|G. Consequently there are at most floor(log_2 G), hence O(log N), updates and at most O(log N)+1 expensive secondary searches before termination.

Proof. Just before an update, all prime-level orders of z=b^d equal k by minimality. Each such order divides

```text
    (p_i-1)/gcd(p_i-1,d).
```


The elementary prime-valuation identity

```text
    gcd_i [ (p_i-1)/gcd(p_i-1,d) ] = G/gcd(G,d)
```


therefore gives k | G/gcd(G,d). The old C divides G and divides d, so C divides gcd(G,d). It follows that Ck divides G. Since k>=2, each update at least doubles C, whereas C<=G<sqrt(N). A secondary search that does not update C has already returned a proper factor. End proof.

At every stage,

```text
    log_2 d <= K+log_2 G = K+O(log N).
```


Thus the evolving periods never acquire a hidden large bit length.

## 6. DETERMINISTIC TERMINATION

Call a unit b good if the 2-adic valuations of its multiplicative orders modulo the distinct prime divisors of N are not all equal. Every positive common period d of a good b yields a proper factor by the Miller squaring chain. This remains true for prime powers because the kernel of reduction from units modulo p_i^(e_i) to units modulo p_i has odd order.

To see this explicitly, write d=2^v t with t odd. If the prime-component order 2-parts differ, the squaring sequence beginning with b^t passes through a value that is 1 modulo at least one prime and not 1 modulo at least another. The corresponding gcd with N is proper. Neither the factorization of d nor exact order computation is required.

LEMMA 4 (a short deterministic list contains a good base).

Among the integers b<=O_epsilon(N^(kappa+epsilon)), there is a nonunit yielding a proper factor or a good unit.

Proof. Select any two distinct prime divisors p_i,p_j, for the proof only. If v_2(p_i-1)=v_2(p_j-1), use the primitive quadratic character

```text
    chi(b)=(b/p_i)(b/p_j)
```


of conductor p_i p_j<=N. A value chi(b)=-1 gives opposite Legendre signs, hence different order 2-parts at this pair. If the prime-minus-one 2-adic valuations differ, use the Legendre character at the prime with the larger valuation: a nonresidue has the full larger 2-part and is good. The Burgess--Norton bound supplies the required b in the stated range. If b shares any factor with N, its preliminary gcd already succeeds. End proof.

The algorithm simply tries b=2,3,... . It does not know the selected pair of primes and does not evaluate their Legendre symbols. For the first good base, Case B or Case C supplies a common period and Miller succeeds; Case A already succeeds. Thus the deterministic process terminates within the claimed list length.

## 7. COMPLETE RECOVERY THEOREM

THEOREM 5 (general integers, parameterized cost).

Let N be odd and have at least two distinct prime divisors. Choose D with ceil(sqrt(D))^2<N-1. First prepare alpha by Lemma 2. Suppose a separate procedure, of bit cost P(N,D), produces a proper factor or a nonzero K-bit period d_0 of this prepared alpha.

Then N can be split deterministically at total bit cost

```text
    P(N,D)
      + soft-O( sqrt(D)
                 + N^(kappa+epsilon) (K+1)
                 + N^(1/4)/sqrt(D) + 1 ) polylog N.
```


Proof. Preparation costs soft-O(sqrt(D)) polylog N. There are O_epsilon(N^(kappa+epsilon)) trial bases. For each, modular exponentiation, gcds, and the Miller chain cost O(K+log N) modular operations. Lemma 3 bounds the number of expensive secondary searches by O(log N); each costs soft-O(sqrt(B)) polylog N. Since sqrt(B)=O(1+N^(1/4)/sqrt(D)), all displayed terms follow. The main procedure P is invoked only once. End proof.

COROLLARY 6 (short supplied periods).

For K=O(log N), choose D=ceil(N^(1/4)), with harmless adjustments of integer rounding. The preparation and all expensive secondary searches together have exponent 1/8. The deterministic base list has exponent kappa>1/8. Therefore the total cost is

```text
    P(N,D) + O_epsilon(N^(kappa+epsilon)).
```


This conclusion is unconditional in analytic number theory. It depends on the explicitly stated period-producing procedure P, which is not supplied by this note.

Primes, even inputs, and prime powers can be handled by standard deterministic polynomial-logarithmic preprocessing. Recursing on proper factors uses O(log N) calls. Thus, under a uniform monotone cost bound for P on smaller inputs, complete factorization has only logarithmic overhead when the period procedure is available for every prepared composite input.

## 8. SEMIPRIME REFINEMENT FOR LONGER PERIODS

For a known squarefree semiprime N=pq, one may reduce the number of bases requiring long exponentiation when K is large.

First find a Jacobi nonresidue b_0 using cheap Jacobi-symbol evaluations and gcds. Its search costs N^(kappa+epsilon) polylog N, independent of K. Process only this selected base using the algorithm of Section 5. If it fails, v_2(p-1)!=v_2(q-1): under equal valuations, a Jacobi nonresidue is good and any returned common period would have split N.

Now enumerate all b up to O_epsilon((N/D)^(kappa+epsilon)). Since both primes exceed D, either prime is below N/D. Burgess supplies a nonresidue at the higher-valuation prime in this shorter list, and it is good. The same C-growth amortization applies throughout.

The resulting semiprime cost is

```text
    P(N,D)
      + soft-O( sqrt(D)
                 + N^(kappa+epsilon)
                 + (N/D)^(kappa+epsilon) (K+1)
                 + N^(1/4)/sqrt(D) + 1 ) polylog N.
```


For K=N^(lambda+o(1)) and D=N^delta, this gives the exponent envelope

```text
    max{delta/2, kappa,
        kappa(1-delta)+lambda,
        1/4-delta/2}.
```


For 0<=lambda<=1/4-kappa/2, optimizing delta yields

```text
    max{kappa, (kappa+lambda)/(1+2kappa)}.
```


In particular, lambda<=2kappa^2 still permits exponent kappa. For lambda=1/6, this construction gives approximately 0.244232179, so the low-overhead short-period conclusion MUST NOT be applied to exponentially large divisor-cover differences without charging their bit length. The separate randomized or conditional small-nonresidue reduction is better for that setting.

## 9. APPLICATION TO WEIGHTED-SUM COLLISION PRODUCTS

For labels d_s=aN+b-u, a correct weighted-sum cover includes u=aq+bp when N=pq; hence

```text
    d_s=(p-1)(aq-b),
```


which guarantees a nonunit alpha^(d_s)-1 for every unit base alpha. If all candidate exponents are nonzero and have O(log N) bits, a restriction-closed product routine can descend to ANY nonunit leaf. A proper gcd factors N. A full-N leaf supplies precisely the short period required by Corollary 6.

For this semiprime application, a product routine whose restricted queries cost C(N), with a logarithmic-depth restriction tree, yields

```text
    soft-O(C(N)) + O_epsilon(N^(kappa+epsilon))
```


deterministic factoring cost after the base preparation, provided it works for that prepared alpha and all label extraction costs are included. Full-N leaves are useful outputs rather than objects that must all be deleted.

The main cover may have additional small-prime preprocessing requirements. For example, if its guarantee requires p>sqrt(N/r), choose D>=sqrt(N/r) in Theorem 5 (or charge a separate small-factor search), rather than automatically taking D=N^(1/4). At the Newton-cover target, D=sqrt(N/r) has preparation cost N^(0.184699031+o(1)), already within the proposed total budget. The parameterized theorem accounts for this choice. A weighted-sum procedure proved only for semiprimes needs its usual separate reduction from general integers; the general-integer statement of Theorem 5 presumes that P itself is available on each prepared input.

The intended Newton-cover target 1/(4+sqrt(2))=0.184699031... exceeds kappa. At that target, this recovery overhead fits within the budget. The missing all-target product primitive remains the central unresolved step; no new general factoring complexity bound follows until that primitive or another period-producing algorithm is proved.

PRIMARY SOURCES

David Harvey and Markus Hittmeir, Deterministic methods for finding elements of large multiplicative order, arXiv:2601.11131v2, 5 June 2026, Theorem 1.1.
https://arxiv.org/pdf/2601.11131

Paul Pollack, Bounds for the first several prime character nonresidues, Proceedings of the American Mathematical Society 145 (2017), 2815--2826, Theorem 1.1.
https://arxiv.org/pdf/1508.05035
https://www.ams.org/journals/proc/2017-145-07/S0002-9939-2016-13432-1/S0002-9939-2016-13432-1.pdf

François Morain, Guénaël Renault, and Benjamin Smith, Deterministic factoring with oracles, Applicable Algebra in Engineering, Communication and Computing 34 (2023), 663--690. Sections 2.3 and 6.2 provide context for the classical order-to-factor ingredients.
https://arxiv.org/pdf/1802.08444

PRIOR-ART SCOPE (LIMITED CHECK)

Sutherland's 2007 thesis, Section 2.3, Algorithm 2.1 and Proposition 2.5, already proves the randomized reduction from an arbitrary order multiple, with success probability at least one half and no need to factor the multiple. Corollary 2.6 explicitly charges the exponent bit length. Thus the random-base/Miller component is classical.

Sutherland's Section 8.3, Algorithm 8.2 and Proposition 8.7, accumulates an exponent by replacing E with E*ord(b^E); its analysis amortizes nontrivial order computations over growth of E. Harvey--Hittmeir 2026, Algorithm 3.1 and Section 3.2, likewise skips bases already killed by an accumulated common order and bounds expensive steps by multiplicative growth. These amortization ideas are established.

The precise reduction formulated here starts from a possibly nonminimal, unfactored period d_0 of a prepared base. Its ordered nonunit search uses the short index bound B, and a full-N minimum certifies a common prime-level quotient order; this permits the invariant C|gcd_i(p_i-1) without factoring d_0. The resulting N^(kappa+epsilon) overhead is the statement proved in this note. This limited literature check has not established its novelty or found an identical theorem. It should be described as a rigorous combination and adaptation of established methods, not a newly discovered factoring paradigm.

Andrew V. Sutherland, Order Computations in Generic Groups, MIT doctoral thesis, 2007. Sections 2.3 and 8.3--8.4.
https://math.mit.edu/~drew/sutherland-phd.pdf

The reduction has also been checked independently within this research session. No claim of novelty relative to the full literature is made.

**Attribution:** Yilin Liu and GPT-6 Astra Pro.
