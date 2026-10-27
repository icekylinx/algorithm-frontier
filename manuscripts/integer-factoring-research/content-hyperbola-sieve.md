# CONTENT-SENSITIVE HYPERBOLA COVER FOR GENERAL DETERMINISTIC FACTORING

<!-- imported-source: checkpoint_10_general_factoring_theory_2026-10-27.zip; content_hyperbola_sieve_2026-10-27.txt; sha256=b3311226d28ec6efad61b996d68dfba473cb79831c88e1609b13c68b7b1e26cf -->

**Scope:** retained separate research branch; not part of the selected conditional theorem review. See the [curated dependency and review map](../../problems/integer-factorization/sources.md).

Research manuscript, 2026-10-27.
Continuing internal audit; no publication-priority claim.

PROPOSED CONSEQUENCE

Together with the already audited CRT sign-trie polynomial construction,
geometric baby blocking, and arbitrary-short-period recovery, the route
below gives the candidate general deterministic bit bound

```text
  O(N^(1/5) (log N)^(13/5) / (log log N)^(9/10)).
```


The power of N remains 1/5. The new ingredient here is the 3/2 exponent
in a local-density product, including all possible contents of a shortest
lattice vector. No primality-distribution assumption on the unknown
factors or on short lattice vectors is made.

NOTATION

L=ceil(log_2 N), H=ceil(log_2 L). Fix delta=1/1000. Let m be the maximal
initial prime product with m<=N^delta. It is squarefree, contains 2 for
large N, and gcd(m,N)=1 after checking its prime factors. Write y for
its largest prime, so y=Theta(L), log y=Theta(H), and
```text
  rho=phi(m)/m=Theta(1/H).
```

Choose m0 so that R=m*m0 is within a constant factor of
```text
  (N H^3/L^2)^(1/5).
```

Thus R=N^(1/5) times logarithmic factors and m^2=o(R).

The first k=ceil(log_2 L) odd primes dividing m are selected for the
sign trie. Put J=2^k, so L<=J<2L. The first k odd primes are present for
large N: even Bertrand's bound makes their product exp(O((log L)^2)),
which is N^o(1). Bounded exceptional inputs are handled separately.

## 1. PREPROCESSING AND THE EXISTENCE COVER

Use primality/perfect-power tests and the usual small-factor reduction
through N^(1/3), costing N^(1/6)*poly(L), to reach N=pq with distinct
odd primes. Put
```text
  P0=ceil(4*sqrt(N/R)), s=ceil(sqrt(P0)), D0=s^2.
```

For sufficiently large N, D0>=N^(2/5), so the original HH2021 order
routine applies: at cost O(s L^2/sqrt(H)) it either splits N or returns
a unit beta with ord_N(beta)>D0.

Build Q_s(X)=product_(0<=i<s)(X-beta^i) in O(s L^2) bit operations,
using
```text
  Q_(2h)(X)=beta^(h^2)*Q_h(X)*Q_h(beta^(-h)X)
```

and an extra linear factor for odd lengths. Evaluate Q_s(beta^(js))
for j=1,...,s by geometric multipoint evaluation. These differences
cover positive exponents js-i=1,...,s^2. No individual difference can
vanish modulo N, because ord_N(beta)>s^2. A nonunit product therefore
reveals a proper factor by scanning its s factors. If all products are
units, then
```text
  ord_p(beta),ord_q(beta)>s^2>=P0,
```

and in particular P0<p<q. The entire preparation costs
```text
  O(s L^2)=O(N^(1/4)R^(-1/4)L^2),
```

below the final main bound. It also supplies the high-local-order base
needed for short-period recovery; no second order routine is used.

For existence only, consider the integer lattice
```text
  Lambda_p={(a,b) in Z^2: b*p^2 = a*N (mod m)}.
```

It has determinant m, since p and N are units modulo m. Map it by
```text
  (a,b) -> (a*q, m0*(b*p-a*q)).
```

The transformed lattice has determinant N*m*m0=N*R. A shortest nonzero
vector, or the classical rank-two Hermite bound with a fixed constant,
therefore gives
```text
  |a*q| <= 2*sqrt(N*R),
  |b*p-a*q| <= 2*sqrt(N)*m/sqrt(R).                   (1.1)
```

This is precisely the HH lattice construction at the hypothetical anchor
sigma0=p. The algorithm does not know p and does not construct this
lattice; it enumerates a finite superset containing the resulting pair.

The pair may be chosen primitive in Lambda_p. If g=gcd(a,b), then
```text
  g | m.                                             (1.2)
```

Indeed a prime dividing g but not m can be divided from the vector while
preserving the lattice congruence. If ell^2|g with ell|m, division by ell
also preserves the congruence, since m is squarefree. Either contradicts
minimality. This proves (1.2), including squarefreeness of g.

Both coordinates are nonzero. If a=0, the congruence forces m|b and
|bp|>=mp>4m sqrt(N/R), contradicting (1.1). If b=0, the second inequality
has left side at least q>=sqrt(N), whereas its right side is smaller
than sqrt(N) because 2m<sqrt(R). Opposite signs would give
```text
  |bp-aq|>=2 sqrt(N|ab|)>=2 sqrt(N),
```

again impossible. Negate both coordinates if necessary, so a,b>0.
In fact a<=b: if a>b, then
```text
  aq-bp=b(q-p)+(a-b)q>=q>=sqrt(N),
```

contradicting the second bound in (1.1). Therefore the algorithm may
enumerate only A<=B. Emitting both orientations would also be harmless.

Let w=ab. From (1.1),
```text
  Nw=(aq)(bp) <= 2sqrt(NR)*(2sqrt(NR)+2sqrt(N)m/sqrt(R)),
```

so w<=4R+4m<=8R. Moreover,
```text
  u=aq+bp,
  u-2sqrt(Nw)=(aq-bp)^2/(u+2sqrt(Nw))
             <= sqrt(N)*m^2/(R*sqrt(w)).              (1.3)
```

The true weighted label is therefore in a short interval above
2sqrt(Nw), with a bound depending only on w, m and R.

Write a=gA, b=gB. Then A,B are positive, gcd(A,B)=1, g|m, and
```text
  w=g^2 A B<=8R.
```

It is enough algorithmically to require the weaker, periodic condition
```text
  gcd(A,B,m)=1;                                      (1.4)
```

the extra pairs do not harm correctness.

## 2. EXACT LOCAL RESIDUE SETS, INCLUDING CONTENT PRIMES

For each enumerated (g,A,B), put a=gA, b=gB. For every prime ell|m define
S_ell(a,b) to be the set of residues modulo ell^2 of
```text
  a*N/s+b*s,
```

where s runs through units modulo ell satisfying b*s^2=a*N (mod ell).
The expression is independent of the lift of s modulo ell^2, because
its change under s->s+ell*t is
```text
  ell*t*(b-a*N/s^2)=0 (mod ell^2).
```

Thus these sets can be computed entirely with known small moduli.
Every genuine pair from Section 1 satisfies
```text
  u=aq+bp = tau (mod m^2)
```

for some tau in the CRT product of all S_ell(a,b).

For odd ell not dividing g, condition (1.4) and the congruence require
A,B to be units modulo ell. There are exactly two residues if ABN is a
quadratic residue modulo ell, and none otherwise. Equivalently, the two
residues are the roots of
```text
  tau^2=4abN (mod ell^2).
```

Their signs are opposite and neither is zero modulo ell^2.

For odd ell dividing g, write a=ell*a1, b=ell*b1. The congruence modulo
ell is automatic, and
```text
  S_ell = ell * {a1*N/s+b1*s (mod ell): s in F_ell^*}.
```

If A,B are both units, this image has
```text
  (ell+chi(ABN))/2
```

elements, where chi is the quadratic character modulo ell. If exactly
one of A,B is zero modulo ell, it has ell-1 elements. The case both zero
is excluded by (1.4). To verify the image formula, t is attained exactly
when t^2-4ABN is a square, including zero; the standard identity
sum_t chi(t^2-c)=-1 for c!=0 gives the count. The factor (g/ell), a unit
modulo ell, only rescales the image and does not affect its size.

The component at 2 has one allowable residue when admissible and can be
handled explicitly. It contributes only an absolute constant to the
estimates below.

Each odd local set is stable under negation. At selected primes, retain
each nonzero element once and retain zero twice if it occurs. This makes
the local multiset a disjoint union of signed two-element multisets,
including {0,0}. It changes the local cardinality by at most one. At an
unselected prime use the ordinary set with no padding.

Let v_g(A,B) denote the resulting full CRT multiplicity, zero if the pair
is inadmissible. It is periodic modulo m^2 in each variable and factors
as a product of the local multiplicities. Pointwise,
```text
  0<=v_g(A,B)<=m.                                    (2.1)
```

For selected ell|g, the padded cardinality is at most ell, and at every
other odd prime it is at most ell-1; the prime-2 factor is at most one.

## 3. UNIFORM WEIGHTED HYPERBOLA COUNT

For W a power of two with 1<=W<=8R, let n_W count all represented giant
roots, with the selected-zero multiplicities retained, for
```text
  g|m, A,B>0, gcd(A,B,m)=1, W<=g^2 A B<2W,
```

also imposing g^2AB<=8R in the last bucket. We prove

```text
  n_W = O(W*L/H^(3/2) + m^3*sqrt(W)*H),              (3.1)
```


uniformly in W and N. Orientation of A,B costs at most a factor two, so
it suffices for an upper bound to take A<=sqrt(2W)/g and B<=2W/(g^2A).

Average v_g(A,B) over B modulo M=m^2 and call the result f_g(A). Since
the complete B-period has total weight at most M*m=m^3 by (2.1),

```text
  sum_(1<=B<=X) v_g(A,B) <= X*f_g(A)+m^3.             (3.2)
```


For an odd ell, the local factor of f_g(A) depends only on whether ell
divides A. Denote its values by F0 (ell does not divide A) and F1 (ell
divides A). They are:

```text
  ell not dividing g:
    F0=(ell-1)/ell,             F1=0.
```


```text
  ell dividing g, unselected:
    F0=(ell-1)(ell+2)/(2ell),    F1=(ell-1)^2/ell.
```


```text
  ell dividing g, selected:
    F0=(ell-1)(ell+3)/(2ell),    F1=(ell-1)^2/ell.     (3.3)
```


For the first row, summing the two-root multiplicities over unit B
residues gives mean (ell-1)/ell. For the second row, unit B contributes
average image size ell/2 and B=0 contributes ell-1. The third row adds
one for the (ell-1)/2 unit B values for which zero is in the image.
If ell|A, only unit B is permitted, and the image has ell-1 elements.

Let c_g be the average of f_g(A) over A modulo m^2. At odd ell its local
factor is (1-1/ell)F0+F1/ell, namely
```text
  (1-1/ell)^2,                           ell not dividing g;
  (1-1/ell)^2*(ell+4)/2,                  ell|g, unselected;
  (1-1/ell)^2*(ell+5)/2,                  ell|g, selected.      (3.4)
```

At 2 these means are 1/4 when 2 does not divide g and 3/4 when it does.

The harmonic sum of f_g retains this density uniformly. Put s=1/L.
For every X<=N, X^s is bounded by an absolute constant, and

```text
  sum_(A<=X) f_g(A)/A
  <= X^s sum_(A>=1) f_g(A)/A^(1+s)
  = X^s zeta(1+s)
       product_(ell|m)[F0+(F1-F0)*ell^(-1-s)]
  <= C*L*c_g.                                           (3.5)
```


To justify the last comparison uniformly in g, if F1>=F0 the bracket is
no larger than its s=0 value. If F1<F0 its ratio to the s=0 value is at
most exp(C*s*log ell/ell), with an absolute adjustment at 2 and 3. Thus
the product of ratios is exp(O(s*(log y)^2))=O(1), even using the sum
over all positive integers up to y instead of only primes. Also
zeta(1+s)=O(1/s)=O(L). This argument does not approximate a generic
periodic harmonic sum and introduces no uncontrolled boundary term.

Summing (3.4) with the factor g^(-2), and bounding +4 by +5, gives

```text
  sum_(g|m) c_g/g^2
  <= C*rho^2 product_(odd ell|m)(1+(ell+5)/(2ell^2))
  = O(H^(-3/2)).                                       (3.6)
```


Indeed the logarithm of the last product is
```text
  (1/2) sum_(ell<=y) 1/ell + O(1)
  = (1/2) log log y + O(1),
```

while rho^2=Theta((log y)^(-2)). These are the classical Mertens
estimates. They are independent of the unknown factors of N.

Finally insert (3.2) and (3.5) into the hyperbola sum. Its main term is
```text
  O(W*L*sum_g c_g/g^2)=O(W L/H^(3/2)).
```

Its B-period truncation term is
```text
  O(m^3 sqrt(W) sum_(g|m)1/g)=O(m^3 sqrt(W) H),
```

because product_(ell|m)(1+1/ell)=O(log y)=O(H).
This proves (3.1). The estimate is deliberately loose in its second
term; the small fixed power used for m makes that term lower order.

## 4. OUTPUT-SENSITIVE ENUMERATION WITHOUT A HIDDEN UNSIEVED PAIR LOOP

The preceding density is algorithmically usable. Precompute, for every
g|m and every pair (A0,B0) modulo m^2, the local admissibility data,
the local residue sets, their signed-orbit representatives at selected
primes, and their ordinary residues at unselected primes. This can be
done by exhaustive known-modulus arithmetic. For example, enumerate all
units sigma modulo m, test B0*sigma^2=A0*N modulo m/g, compute the
corresponding residues, and deduplicate their local images. A generous
bound m^10*poly(L) covers all tables, sorting and inverses. With
m<=N^(1/1000), it is N^(1/100+o(1)), negligible.

For each g and each integer A<=sqrt(16R)/g, traverse the precomputed
table for A modulo m^2. For every admissible B0 modulo m^2 and coarse
CRT orbit record, enumerate the actual integers B=B0+t*m^2 in the
required dyadic hyperbola interval with B>=A. Each successful output is exactly
one coarse record for the sign trie. Boundary visits, including empty
arithmetic progressions, can be bounded very conservatively by
```text
  m^10*sqrt(R)*poly(L)=N^(11/100+o(1)),
```

again below the main exponent. This deliberately avoids a delicate
constant in the precomputation exponent.

There are exactly r_W=n_W/J successful coarse records in bucket W.
For each one compute its actual a,b,w, the center described below, and
one modular beta-power. This takes O(L^3) per record, hence
```text
  O((n_W/J)L^3)=O(n_W L^2).
```

The tuple keys, exact exponent labels and unit values have O(L) bits;
sorting and attaching the precomputed unit tables fit the same bound.
No enumeration of all unsieved A,B pairs of cardinality R log R is
charged at unit cost or silently omitted.

## 5. CRT GIANTS AND A COMMON BABY BASE FOR EVERY CONTENT

Use the unit beta already prepared in Section 1. Its local orders
exceed P0>N^(1/3). Put alpha=beta^(m^2). No high local order of alpha
is required for the new aggregate search or recovery.

For bucket W set
```text
  lambda_W=ceil(sqrt(N)/(R*sqrt(W))),
  K_W=2*lambda_W+2*k+1.
```

For actual a,b,w in that bucket let
```text
  C=2sqrt(Nw), tau0=floor(C/m^2).
```

The integer tau0 is computable by exact integer-square-root comparisons.

Let tau_rest in [0,m^2) be the CRT sum of the unselected local residues.
Let w_j in [0,m^2) be the CRT lift of the selected signed-orbit
representative. Set
```text
  T_epsilon=tau_rest+sum_(j=1)^k epsilon_j*w_j,
  e_epsilon=aN+b-m^2*(tau0-lambda_W-k)-T_epsilon.       (5.1)
```


As in the sign-trie proof, floor(T_epsilon/m^2) lies in [-k,k]. The
genuine residue tau=u modm^2 is represented by one such sign vector.
Equation (1.3), w>=W and the floor inequality imply that u equals
m^2*(tau0-lambda_W+i0)+tau for some 0<=i0<=2lambda_W.
Thus beta^(e_epsilon) collides modulo p with
```text
  alpha^(i0+k-floor(T_epsilon/m^2)),
```

whose index is in [0,K_W-1].

Crucially, these are the original a=gA,b=gB labels and residues modulo
m^2. They are NOT divided by g in the exponent. Hence every content
class uses the SAME baby base alpha=beta^(m^2). The normalized modulus
m^2/g is used only to understand and count the local images.

The local alphabet at the j-th selected prime has at most ell_j^2
symbols, even for content primes. Every coarse record contributes a
full J-term sign cube, with zero weights repeated. The already proved
sign-trie construction therefore forms the giant polynomial in
O(n_W L^2) bit operations.

## 6. BABY BLOCKING, NONZERO PERIODS, AND FACTOR RECOVERY

Let f_W be this giant polynomial. If n_W=0, skip the bucket. Otherwise
choose a power of two h within a constant factor of
```text
  max(1,sqrt(K_W/n_W)).
```

Form
```text
  G_h(X)=product_(0<=j<h) f_W(alpha^j X)
```

by doubling, G_(2h)(X)=G_h(X)G_h(alpha^h X), and evaluate at
```text
  X=alpha^(h*t), 0<=t<ceil(K_W/h).
```

The complete cost, including f_W construction, is
```text
  O((n_W+sqrt(n_W K_W)) L^2).                         (6.1)
```

This is the q-holonomic blocking operation already used in the 14/5
checkpoint. Padding to a full final block is allowed.

Every represented integer period is strictly positive for sufficiently
large N. Indeed aN+b>=N, while every padded candidate U subtracted from
it satisfies
```text
  U<=2sqrt(8NR)+O(m^2*(lambda_W+k+h+1)).
```

Over all W>=1,
```text
  lambda_W=O(sqrt(N)/R+1), h=O(sqrt(K_W)+1),
```

so the right side is
```text
  O(sqrt(NR)+m^2*sqrt(N)/R+m^2*sqrt(sqrt(N)/R)+m^2*k)
  =o(N)
```

for m<=N^(1/1000), R=N^(1/5) times logarithmic factors. Thus the
integer d=e_epsilon-m^2*i at every padded leaf is positive, and has
O(L) bits. This handles all overincluded pairs and all padded zero
weights uniformly.

A proper output gcd factors N. If an aggregated value has gcd N,
evaluate at most h original f_W baby values by Horner's rule to find a
nonunit one, then use the stored-trie nonunit descent. The cost is
O(n_W*h L^2+n_W L^2), within (6.1). A proper leaf gcd factors N; a
full-N leaf gives a nonzero O(L)-bit period of the same prepared beta.
The previously audited deterministic arbitrary-period recovery finishes
in N^(1/(4sqrt(e))+epsilon)*poly(L)+N^(1/12)*poly(L), lower order.
Only one full-N recovery is invoked, because it terminates with a factor.

## 7. SUMMING THE BUCKETS AND OPTIMIZING

Write
```text
  A=L/H^(3/2), B=m^3 H.
```

Then (3.1) is n_W=O(AW+B sqrt(W)), and throughout W<=8R,
```text
  K_W=O(sqrt(N)/(R sqrt(W)))
```

because the logarithmic carry padding is smaller than this expression.
The buckets are dyadic, so (6.1) sums to

```text
  O(L^2 * [ A R
           +N^(1/4)R^(-1/4)sqrt(A)
           +B sqrt(R)
           +L*N^(1/4)R^(-1/2)sqrt(B) ]).             (7.1)
```


The first two terms balance at
```text
  R=Theta((N H^3/L^2)^(1/5)),
```

and give
```text
  O(N^(1/5)L^(13/5)H^(-9/10)).
```


The remaining two terms have N-exponents at most
```text
  1/10+3/1000 and 3/20+3/2000,
```

respectively, before logarithmic factors. They are strictly lower order.
The deliberately coarse table/enumeration cost N^(11/100+o(1)) is also
lower order. The order-based preparation and local screen cost
```text
  O(N^(1/4)R^(-1/4)L^2)
  =O(N^(1/5)L^(21/10)H^(-3/20)),
```

below the claimed main bound. The initial N^(1/3) small-factor reduction
and the eventual short-period recovery are lower order as well.

The usual multiplicative recursion argument for factoring proper
divisors avoids an extra log N factor: for fixed theta=1/5 and large N,
A0^theta+B0^theta<=c N^theta for A0B0=N, A0,B0>=2, with c<1. The
logarithmic multiplier is eventually increasing. Thus the bound is for
complete factorisation of general integer inputs, not only balanced or
otherwise specially structured semiprimes.

AUDIT STATUS

Root and frontier have now completed independent end-to-end internal
reads and found no remaining mathematical or complexity gap in the
present argument. This includes the local density, uniform Rankin bound,
global lattice cover, output-sensitive enumeration, padded nonzero
periods, dyadic blocking, and all preprocessing costs. External novelty
and peer review checks remain outstanding. The result should not be
described as a smaller power of N or as a polynomial-time RSA attack.

COMPANION INTERNAL PROOFS

```text
  crt_trie_hh_log_saving_2026-10-27.txt
    Section 2 proves the multiplicative sign-trie and nonunit descent.
```


```text
  deterministic_period_recovery_amortized_2026-10-27.txt
    Gives the complete arbitrary-short-period recovery invariant and
    Burgess--Norton argument used after a full-N leaf collision.
```


```text
  crt_preprocessing_audit_2026-10-27.txt
    Audits local lift invariance, signed CRT carries, small-prime tables
    and the earlier HH setup; the content-specific table enumeration
    and stronger initial order screen are proved in the present note.
```


```text
  The q-holonomic/Bostan--Yurkevich doubling needed here is written
  explicitly in Section 6, including its cost and block recovery. No
  unstated compressed-product subroutine is assumed.
```


PRIMARY SOURCES FOR IMPORTED RESULTS

Harvey--Hittmeir, arXiv:2105.11105, Lemma 3.1 / Proposition 3.3 (the
rank-two lattice) and Lemmas 2.3, 2.5 (geometric evaluation and order).
```text
  https://arxiv.org/pdf/2105.11105
```

Harvey, arXiv:2010.05450, Proposition 2.5, suffices for the initial
N^(1/3) small-factor reduction; its log^3 factor is harmless at that
smaller exponent. The stronger P0 screen is constructed explicitly
in Section 1 using the old HH order routine and a geometric product.
```text
  https://arxiv.org/pdf/2010.05450
```

Bostan--Yurkevich, arXiv:2012.08656 (geometric/q-holonomic blocking).
```text
  https://arxiv.org/pdf/2012.08656
```

Pollack, arXiv:1508.05035, Theorem 1.1 (Burgess--Norton nonresidues),
used in the separately proved arbitrary-period recovery lemma.
```text
  https://arxiv.org/pdf/1508.05035
```

**Attribution:** Yilin Liu and GPT-6 Astra Pro.
