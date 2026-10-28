# CRT SIGN TRIES IN THE HARVEY--HITTMEIR FACTORING SEARCH

<!-- imported-source: checkpoint_10_general_factoring_theory_2026-10-27.zip; crt_trie_hh_log_saving_2026-10-27.txt; sha256=7152397ea3cd85a506d9c8337824274f161524b2e8397e932004ce4dbbc00027 -->

**Scope:** retained separate research branch; not part of the selected conditional theorem review. See the [curated dependency and review map](../../problems/integer-factorization/sources.md).

Research draft, 2026-10-27. Mathematical claim under continuing audit.
No claim of publication priority or external peer review is made.

CLAIM

The construction below, together with the deterministic short-period
recovery lemma proved in the companion file
deterministic_period_recovery_amortized_2026-10-27.txt, gives deterministic
factorisation of a general integer N in

```text
  O( N^(1/5) (log N)^(13/5) / (log log N)^(3/5) )
```


bit operations. This changes a logarithmic factor, not the exponent 1/5.
The argument uses explicit polynomials and charged arithmetic throughout;
it does not assume a compressed-product oracle, generic collisions, or
unproved distributional properties of primes or multiplicative orders.

The principal new construction in this draft is the multiplicative trie
in Section 2. Its use in factoring relies essentially on the ability to
recover from an arbitrary nonzero short period, including one obtained
from a collision modulo the whole composite N.

PRIMARY REFERENCES

[HH] D. Harvey and M. Hittmeir, A log-log speedup for exponent one-fifth
deterministic integer factorisation, arXiv:2105.11105 (2021).
https://arxiv.org/pdf/2105.11105
We use Lemmas 2.1, 2.3, 2.5, 2.6 and the construction in Proposition 3.3.

[H] D. Harvey, An exponent one-fifth algorithm for deterministic integer
factorisation, arXiv:2010.05450 (2020).
https://arxiv.org/pdf/2010.05450
Its small-factor reduction, also described in the introduction of [HH],
reduces general inputs to prime or distinct-prime semiprime inputs at
cost N^(1/6+o(1)).

[BN] P. Pollack, Bounds for the first several prime character nonresidues,
arXiv:1508.05035, Theorem 1.1, for the classical Burgess--Norton bound.
https://arxiv.org/pdf/1508.05035

The geometric factorial blocking operation of Bostan--Yurkevich,
arXiv:2012.08656, was useful in the preceding 14/5 checkpoint. The present
13/5 construction takes block length one and does not require that step.

## 1. ARITHMETIC AND NOTATION

Let L=ceil(log_2 N) and l=ceil(log_2 L). We consider sufficiently large N;
bounded inputs may be handled by a fixed exhaustive algorithm. Ring
elements lie in A=Z/NZ, and every exponent label below has O(L) bits.
All polynomial degrees are O(N). Fast integer multiplication and
Kronecker substitution multiply polynomials of total degree d in
O((d+1)L^2) bit operations. A product of t supplied linear factors costs
O(tL^3) by an ordinary product tree. Multiplicative scaling f(X)->f(uX),
where u is a supplied unit, costs O((deg f+1)L log L), hence at most
O((deg f+1)L^2). Finally, for any unit alpha, geometric multipoint
evaluation of a degree-d polynomial at K consecutive powers of alpha
costs O((d+K)L^2). The latter is [HH, Lemma 2.3] and requires no
distinctness or invertibility of pairwise point differences.

The gcd of two O(L)-bit integers costs O(L(log L)^2). Consequently O(n)
ring operations and gcds cost O(nL^2), for sufficiently large N. All
polynomial algorithms used here are valid over the composite ring A.

## 2. AN EXPLICIT MULTIPLICATIVE SIGN-TRIE LEMMA

There are r records. Record v contains a unit c_v and a type tuple
(t_1(v),...,t_k(v)). At coordinate j the alphabet has at most a_j symbols;
symbol t specifies a unit u_(j,t). Put J=2^k and n=Jr. We want the monic
polynomial, with multiplicities retained,

```text
  P(X)= product_v product_(epsilon in {+1,-1}^k)
          (X-c_v product_j u_(j,t_j(v))^epsilon_j).
```


Assume log a_j=O(j). Then P and the auxiliary node polynomials needed
for nonunit descent can be constructed in

```text
  O(nL^2+rL^3)
```


bit operations, apart from the explicitly charged production and sorting
of the records and the table of units. The sum of degrees of all stored
node polynomials is less than 2n.

Proof. Sort the records lexicographically by their type tuples, and make
a trie whose coordinates are considered in the order 1,...,k. At each
leaf, form the product of its supplied factors X-c_v by an ordinary
product tree. The total leaf cost is O(rL^3). For a unit u define

```text
  T_u(f)(X)=f(uX)f(u^(-1)X).
```


The two leading coefficients cancel when f is monic. This operation
replaces each root c by the two roots u c and u^(-1)c, is multiplicative
in f, and costs O((deg f+1)L^2). A coordinate-j node is constructed by
applying T_(u_(j,t)) to its already constructed child polynomial for each
present symbol t, then multiplying the results in a balanced tree.
The children represent the later coordinates j+1,...,k, so the resulting
node represents all signs in coordinates j,...,k. This proves the stated
root identity by induction.

At coordinate j, the total degree of the resulting node polynomials is
exactly n/2^(j-1). There are at most a_j children per node. A balanced
product tree uses O(1+log a_j) multiplication layers, each of total degree
at most this quantity. Hence all internal work is bounded by

```text
  O( nL^2 sum_(j=1)^k (1+log a_j)/2^(j-1) ) = O(nL^2).
```


The same geometric sum, without the logarithmic weights, bounds the
stored node degrees. A zero sign weight means u=1; its operation is
simply squaring. Keeping both identical branches preserves the exact
degree accounting. Repeated roots and zero divisors among coefficients
are harmless.

Nonunit descent. Suppose x is a unit and gcd(P(x),N)>1. At a node, test
its factors f_child(u x) and f_child(u^(-1)x). Some tested value is a
nonunit. A proper gcd immediately factors N; otherwise choose a nonunit
child value and descend, replacing x by the corresponding scaled point.
Horner evaluation of all child factors costs O(deg P_node) ring
operations. Each child has at most half the parent degree. Thus the
total descent cost is O(n) ring operations and gcds. At the selected
leaf, scan its original factors X-c_v to find a nonunit difference.
This costs no more than the leaf degree. The sequence of chosen signs
is known exactly, and therefore identifies an original root label.

The storage and traversal need no unit-cost random-access assumption.
The records may be sorted and nodes processed in lexicographic streams.
At each descent depth, even scanning the entire stored depth costs only
its total coefficient length; those lengths form a geometric series.

## 3. PREPARING THE INPUT AND THE BASE

Use deterministic primality and perfect-power tests and the standard
small-factor search through N^(1/3). If a factor is found, split and
recurse. This costs N^(1/6+o(1)). Otherwise a composite input is a product
N=pq of two distinct odd primes with N^(1/3)<p<q. This is precisely the
general-to-semiprime reduction used in [HH]; no restriction on the
original integer input has been introduced.

Apply [HH, Lemma 2.5] with D0=ceil(N^(2/5)). It either splits the input,
certifies primality, or returns a unit beta with ord_N(beta)>D0. Its cost
is O(N^(1/5)L^2/sqrt(l)).

Set D=ceil(N^(1/3)) and s=ceil(sqrt(D)). Form

```text
  Q(X)=product_(0<=i<s)(X-beta^i)
```


and evaluate Q(beta^(js)) for j=1,...,s. The differences cover exponents
js-i=1,...,s^2. Since s^2<D0 for large N, no individual difference can
vanish modulo N. A nonunit output therefore yields a proper factor by
scanning its s differences. If all outputs are units, then

```text
  ord_p(beta)>D and ord_q(beta)>D.                         (3.1)
```


This additional preparation costs O(N^(1/6)L^3). All preparation costs
are below the final bound.

## 4. HH PARAMETERS AND A SIGN-INVARIANT LATTICE ROUTINE

Let m be the product of primes at most floor(L/30), as in [HH]. Standard
prime estimates give, for all sufficiently large N,

```text
  m<N^(1/20),              phi(m)/m=Theta(1/l).
```


The known factorisation of m is part of the construction. Our prepared
input has no prime factor dividing m. Choose

```text
  T=ceil((N l^2/L^2)^(1/5)),
  m0=ceil(T/m), R=m m0,
  lambda=ceil(4 sqrt(N)/R^(3/2)).
```


Then R=Theta(N^(1/5)L^(-2/5)l^(2/5)). All roots and ceilings here can
be implemented with integer root comparisons. Starting at
sigma0=ceil(N^(1/3)), repeatedly replace sigma0 by
ceil((1+1/m0)sigma0), stopping at sqrt(N). Let S be the number of
anchors. Then S=O(m0 L). The resulting half-open intervals contain
every integer p in the required range. Rounding the next anchor up
does not leave an integer uncovered.

For each unit square class z modulo m and anchor sigma0, apply the
explicit lattice construction from [HH, Proposition 3.3], with fixed
deterministic tie-breaking, to

```text
  gamma=N z^(-1) mod m.
```


It returns (a,b)!=(0,0) with O(L)-bit coordinates satisfying

```text
  b = gamma a (mod m),
  |b sigma0-aN/sigma0| <= E1 := 2 sqrt(N) m/sqrt(R),       (4.1)
  |aN/sigma0| <= 2 sqrt(NR).
```


The lattice basis in the cited proof is determined by gamma, sigma0,
N, m0 and m. Thus the SAME pair (a,b) may be used for all residues
sigma with sigma^2=z modulo m. This is an algorithmic fact about the
displayed lattice basis, not an assumption about coincident outputs
of unrelated short-vector calls.

Write C=aN/sigma0+b sigma0 and tau0=floor(C/m^2). If the actual smaller
prime satisfies p=sigma mod m and belongs to this anchor's interval,
the proposition gives

```text
  |aq+bp-C| <= 4 sqrt(N) m^2/R^(3/2),
  aq+bp = aN/sigma+b sigma (mod m^2).                     (4.2)
```


For tau in [0,m^2) representing the latter residue, these facts imply

```text
  aq+bp=m^2(tau0-lambda+i)+tau,  0<=i<=2lambda.          (4.3)
```


This is the covering step of [HH]. We will represent all tau values
without separately constructing all phi(m) giant powers per anchor.

## 5. THE LOCAL SIGN IDENTITY AND COARSE RECORDS

For a prime ell dividing m, fix one of the two local roots z_ell of a
given unit square class modulo ell; the prime 2 has just one root.
The choices and their signs can be generated by listing local residues
and squaring them, so no unknown-modulus square-root oracle is involved.
For any lift of z_ell modulo ell^2 define

```text
  r_ell = aN/z_ell+b z_ell (mod ell^2).
```


The division is by the known unit z_ell modulo ell^2. The congruence
b=aN/z_ell^2 mod ell implies that this residue is independent of the
chosen lift: replacing z_ell by z_ell+ell h changes the expression by
ell h(b-aN/z_ell^2)=0 mod ell^2. Changing its sign negates r_ell.
This remains valid if ell divides a or b.

Let E_ell be the standard CRT idempotent for the component modulo ell^2
inside Z/m^2Z. Set

```text
  w_(ell,r) = E_ell r mod m^2, in [0,m^2).
```


Select the first k=ceil(log_2 L) ODD prime factors ell_1<...<ell_k of m,
and put J=2^k. Such primes are present for all sufficiently large N.
Thus L<=J<2L. Enumerate all square classes modulo m, all S anchors, and
all signs on the UNSELECTED odd primes. One such choice is a coarse
record. Reduce its unselected CRT contribution to a single integer
tau_rest in [0,m^2). The selected local weights give a type tuple

```text
  t=(r_(ell_1),...,r_(ell_k)).
```


For a selected sign vector epsilon, put

```text
  U_epsilon=tau_rest+sum_j epsilon_j w_(ell_j,t_j),
  e_epsilon=aN+b-m^2(tau0-lambda)-U_epsilon+k m^2.         (5.1)
```


There is a canonical tau in [0,m^2) and an integer c with
U_epsilon=tau+c m^2. Because there are k selected weights,

```text
  -k<=c<=k.
```


If the original HH witness had baby index i in (4.3), the new giant
beta^(e_epsilon) collides modulo p with alpha^(i+k-c), where

```text
  alpha=beta^(m^2),   0<=i+k-c<=2lambda+2k.
```


Hence set K=2lambda+2k+1. Enlarging this baby interval preserves the
witness and introduces only O(log log N) extra indices.

The coarse record root and local multipliers are

```text
  c_v=beta^(aN+b-m^2(tau0-lambda)-tau_rest+k m^2),
  u_(j,t)=beta^(-w_(ell_j,t)).
```


Then (5.1) says exactly that all represented giant roots are
c_v product_j u_(j,t_j)^epsilon_j. There are

```text
  n=S phi(m)=O(RL/l)                                    (5.2)
```


full roots counted with multiplicity and r=n/J coarse records.
Every zero selected weight retains both identical sign choices. The
full count n and every trie degree are therefore exact, even when
distinct residues produce the same giant ring element.

At coordinate j the type alphabet has at most ell_j^2 elements.
Bertrand's bound gives log ell_j=O(j), which is the hypothesis of the
sign-trie lemma. Apply that lemma to obtain the complete giant
polynomial P in O(nL^2+(n/J)L^3)=O(nL^2), once records are prepared.

## 6. ALL SETUP COSTS

Let t be the number of odd prime factors of m. The number of full unit
square classes modulo m is phi(m)/2^t. We run the O(L^3)-bit lattice
routine once per square class and anchor, and produce 2^(t-k) coarse
records from that output. Thus the number of lattice calls is at most
r=n/J, and their total cost is O(rL^3).

Each coarse record may, conservatively, compute its CRT contributions,
O(L)-bit exponent and unit power in O(L^3) bit operations. In particular,
there are at most O(L/log L) prime components; processing all of them
with O(L)-bit modular arithmetic fits this budget. Enumerating the
local square classes, known CRT data and the primes costs only
N^(1/20+o(1)), which is lower order. The records have O(L+k log L)
bits including their keys and labels, and can be sorted within
O(rL^3). Sharper setup estimates are unnecessary.

For each selected prime precompute beta^(+/-w_(ell_j,r)) for all
0<=r<ell_j^2. There are sum_j ell_j^2 such values. Bertrand alone
bounds this number by O(4^k)=O(L^2); consequently the entire table
costs a fixed polynomial in L, negligible compared with nL^2. The
stronger usual prime estimates would give a polynomial in log L.
The table can be streamed or merged into the trie processing, so an
unbounded random-access model is not being used. These global tables
are used by the record-generation bound; separately exponentiating
all k unit powers for every record is not included in that bound.

Combining these charges with Section 2 proves that all giant setup
and polynomial construction cost O(nL^2). In particular, the n roots
are not separately exponentiated, and no hidden nL^3 term remains.

## 7. EVERY PADDED EXPONENT IS A NONZERO INTEGER

This removes the exact-zero issue uniformly, rather than deleting roots
in a way that could break the sign structure. Fix ANY generated coarse
record, sign vector, and 0<=i<K. Put d=e_epsilon-m^2 i. Let
delta=b sigma0-aN/sigma0, so |delta|<=E1. Direct algebra gives

```text
  aN+b-C = aN(1-1/sigma0)^2-delta(1-1/sigma0).            (7.1)
```


If a is nonzero, sigma0>=2 and therefore

```text
  |aN+b-C| >= N/4-E1.
```


If a=0, the lattice congruence forces m to divide b. Since the vector
is nonzero,

```text
  |aN+b-C|=|b|(sigma0-1)>=m(N^(1/3)-1).                  (7.2)
```


On the other hand, set

```text
  V=m^2(tau0-lambda-k+i)+U_epsilon,
```


so that d=aN+b-V. From |m^2 tau0-C|<m^2, the range of i, and
|U_epsilon|<(k+1)m^2, one obtains

```text
  |V-C| <= m^2(lambda+2k+2).                            (7.3)
```


For the chosen R and m<N^(1/20), E1=o(N) and the right side of (7.3)
is o(N). It is also o(m N^(1/3)): the possibly largest ratio is

```text
  m sqrt(N)/(R^(3/2) N^(1/3))
    = O(N^(-1/12) L^(3/5) l^(-3/5)) = o(1).
```


The ceiling and k terms are smaller. Equations (7.1)--(7.3) therefore
imply d!=0 for every represented leaf, including all extra carry
padding and every duplicate root. The bit length of d is O(L), by
the bounds on a,b and all construction parameters.

## 8. FINDING A FACTOR OR A SHORT PERIOD

Evaluate P at 1,alpha,...,alpha^(K-1) in O((n+K)L^2) bit operations.
Some value is a nonunit by the covering argument (4.3)--(5.1).
Scan gcds with N. A proper gcd finishes. If a value has gcd N, use
the stored-trie descent from Section 2. It takes O(nL^2) bit operations
and finds a nonunit leaf. At a descent step x is multiplied by a known
beta-power; track the corresponding exponent as an exact integer.
At the leaf scan, a proper gcd finishes, while a full-N equality gives

```text
  beta^d=1 mod N,        0<|d|,       bitlength(d)=O(L).
```


Nonzeroness is Section 7. The exponent is a period of the SAME prepared
base beta satisfying (3.1), regardless of which nonunit leaf was selected.
No local uniqueness, randomness, or exact-order computation is needed.

Apply the deterministic short-period recovery lemma from the companion
proof with D=N^(1/3). For every fixed epsilon>0 its cost is

```text
  soft-O(N^(1/12)) + O_epsilon(N^(1/(4 sqrt(e))+epsilon) polylog N).
```


Take epsilon so that 1/(4 sqrt(e))+epsilon<1/6. Recovery is lower order
than the already charged preparation. It is invoked at most once.

For completeness, the mechanism of this lemma is recalled here. Given a
period d0, maintain d_cur=|d0| C where C divides G=gcd(p-1,q-1), initially
C=1. For each small integer base b, first test b^(d_cur)-1 modulo N and
apply the standard powers-of-two splitting chain whenever d_cur is a
period. If that gcd is one, set z=b^(d_cur). At the smaller prime,
ord_p(z) <= (p-1)/ord_p(beta) < sqrt(N)/D. A baby-step giant-step
product search of length B=ceil(sqrt(N)/D), at cost soft-O(sqrt(B)),
finds the MINIMUM positive k for which z^k-1 is a nonunit: select the
first nonunit giant block and scan its exponents in increasing order.
A proper gcd splits. A full-N minimum implies ord_p(z)=ord_q(z)=k>1.
Then k divides G/gcd(G,d_cur), so replacing C by Ck preserves C|G
and at least doubles C. At most O(log N) expensive searches occur.
All other base trials require only O(L)-bit exponentiation and gcds.
The Burgess--Norton bound guarantees a base b<=N^(1/(4 sqrt(e))+epsilon)
whose local order has different powers of two at p and q: if
v2(p-1)=v2(q-1), use a nonresidue of the character (./p)(./q); if these
valuations differ, use a nonresidue at the prime with larger valuation.
Any period of such a base yields a proper factor by the powers-of-two
chain. This proves the stated recovery bound without factoring d0.
The companion proof includes the invariant and character details.

## 9. FINAL COMPLEXITY AND SCOPE

By (5.2) and the definition of K, the main search costs

```text
  O( (RL/l + sqrt(N)/R^(3/2) + k)L^2 ).
```


For R=Theta(N^(1/5)L^(-2/5)l^(2/5)), both principal counts are

```text
  O(N^(1/5)L^(3/5)l^(-3/5)).
```


The resulting bit bound is

```text
  O(N^(1/5)L^(13/5)l^(-3/5)).
```


The initial O(N^(1/5)L^2/sqrt(l)) order construction, N^(1/6+o(1))
small-factor reduction and local-order screening, all coarse-record
generation, trie tables, output gcds, one nonunit descent, and one
period-recovery invocation lie within this bound. All degrees and point
counts are O(N), as required by the cited polynomial arithmetic lemmas.

Recursively splitting composite factors does not add another log N.
For any fixed positive theta, the sum A^theta+B^theta for A B=N and
A,B>=2 is at most c N^theta for a constant c<1 once N is sufficiently
large. The logarithmic multiplier here is eventually increasing, so
the costs over the factorisation tree form a convergent geometric
bound relative to the root cost; bounded-size leaves contribute only
polylogarithmic overhead. Pure powers were already handled by exact
root tests. The asserted bound therefore concerns complete factorisation
of general integer inputs.

This derivation is a candidate theorem assembled during an active
research session. The proof has internal independent audits, but no
external review or exhaustive novelty check. Its intended scope is an
unconditional improvement in logarithmic factors if the argument stands;
it does not establish a smaller power of N, an RSA polynomial-time
algorithm, or a general number-field-sieve fruitfulness theorem.

**Attribution:** icekylinx and GPT-6 Astra Pro.
