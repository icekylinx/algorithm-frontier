# FACTORING OR SHORTENING A PERIOD WITH A KNOWN FACTORED COFACTOR

<!-- imported-source: checkpoint_10_general_factoring_theory_2026-10-27.zip; factored_period_cofactor_2026-10-27.txt; sha256=9c368a59d54c0b555247b725285625513b4dd66b17471037b9ce5d006564b5e9 -->

**Scope:** retained separate research branch; not part of the selected conditional theorem review. See the [curated dependency and review map](../../problems/integer-factorization/sources.md).

Research lemma, 2026-10-27. No novelty claim.

GENERAL THEOREM: SHORTENING A KNOWN FACTORED COFACTOR

Let N>=2, L=ceil(log_2 N), and eta a unit modulo N. Suppose a positive
period d of eta is presented as

```text
  d=S D,
```


where the complete prime factorisation S=product_j ell_j^e_j is supplied
and D is a positive K0-bit integer. Let K be the bit length of S. A
deterministic algorithm using soft-O(K+K0+1)*poly(L) bit operations
returns an O(K0+L)-bit positive period of the SAME base eta. It requires
neither a factorisation of N nor a factorisation of D. In particular,
K0=O(L) gives an O(L)-bit period. The result is standard order extraction
from a factored multiple; the point recorded here is its additive cost
in the long factored cofactor.

PROOF

Set beta=eta^D modulo N. Its order r divides S, because eta^(SD)=1.
Also r<=phi(N)<N, so r has at most L bits. We recover r exactly.

Build a product tree on the supplied prime powers E_j=ell_j^e_j. At
a node with product E, store beta^(S/E). The root stores beta. For
children E=E_1 E_2, obtain their values by raising the parent value to
E_2 and E_1, respectively. The resulting leaf value is

```text
  beta_j=beta^(S/E_j).
```


Let ell_j^f_j be the ell_j-primary part of r. Since S/E_j is coprime
to ell_j and contains every other primary part of r, the elementary
order formula gives

```text
  ord_N(beta_j)=r/gcd(r,S/E_j)=ell_j^f_j.
```


Starting with beta_j, repeatedly raise the current value to ell_j
until it is 1. The exact number of such raisings is f_j; if beta_j=1,
then f_j=0. Hence r=product_j ell_j^f_j is recovered explicitly. The
integer D*r is a positive period of eta with O(K0+L) bits, as required.

For completeness, no unknown group order is used in this computation.
The known factorisation of S is the input allowing the primary
projections; the bound r<N is used only to bound their cost and output.
At every level of the exponent-propagation tree, the sum of bit lengths
of all child exponents is O(K). There are O(log(2+K)) levels in a tree
balanced by leaf count. Fast product-tree arithmetic is soft-O(K),
and modular exponentiation therefore costs soft-O(K)*poly(L). The
initial power eta^D costs O(K0)*poly(L). Among the nonidentity primary
components, the total number of exponent bits used while finding the
f_j is

```text
  sum_j f_j*ceil(log_2 ell_j)=O(log r)=O(L).
```


Testing all initially identity components contributes at most O(K L)
bit operations. Multiplying the recovered primary orders has O(L)-bit
output. These bounds prove the stated total cost.

APPLICATION TO PREPARED-BASE RECOVERY

When eta has the high local orders required by the short-period
recovery theorem, a returned period SD of this type can first be
shortened as above. In particular, if D has O(log N) bits, the long
known factored cofactor S does not multiply the Burgess-sized list of
trial bases: its extra cost is additive, up to logarithms. This is a
reduction from a particular form of long period, not a way to produce
a period without a search oracle.

COMPACT FACTORISATIONS AND CAPPED MULTIPLICITIES

If S is supplied only by a compact factorisation, it need not be
expanded. Since r=ord_N(eta^D)<N, discard primes ell>N-1 and replace
every supplied exponent e by min(e,floor(log_ell(N-1))). The resulting
factored integer E still contains r. Apply the same algorithm with E
in place of S. Its bit length is at most L times the number of retained
distinct primes. The cost is therefore soft-O(bitlength(E)+K0+1)*poly(L)
plus the cost of reading the original factorisation, even when S has
enormous supplied multiplicities. The integer logarithm in the cap is
computed by exact comparisons of powers; no real-number oracle is used.

OPTIONAL SEMIPRIME SHORTCUT

For N=pq with distinct odd primes, one can often avoid the full primary
order extraction. Put C=gcd(S,N-1), H=D*C, and beta=eta^H modulo N.
The exponent H already has O(K0+L) bits. If gcd(beta-1,N) is proper,
return that factor; if it equals N, H is a short period. Otherwise the
two local orders of beta are nontrivial, divide S, and are coprime.

To prove the last claim, write r_p=ord_p(eta), r_q=ord_q(eta); both
divide SD. For a prime ell put u=v_ell(S), z=v_ell(D), t=v_ell(N-1).
The valuation of H is z+min(u,t). If u<=t, H removes both local
ell-parts. If u>t, H has valuation z+t>=t, whereas

```text
  min(v_ell(r_p),v_ell(r_q))
    <=min(v_ell(p-1),v_ell(q-1))<=v_ell(N-1)=t,
```


because gcd(p-1,q-1) divides pq-1. Thus at least one residual local
ell-part is removed. This proves the coprimality. An individual
residual order can still share primes with N-1; that is harmless.

A prime-power product tree for S now finds a proper factor by a single
path descent. Maintain a nonidentity unit z whose coprime local orders
divide the current node product E=E_1 E_2, with gcd(E_1,E_2)=1. Check
gcd(z-1,N). If proper, return it. Otherwise it is one. Compute
z_1=z^E_2. If z_1 is nonidentity, descend to E_1 with z_1. If z_1=1,
z_2=z^E_1 must be nonidentity (otherwise ord_N(z) would divide both
coprime E_1 and E_2); descend to E_2 with z_2. Check each new gcd.
At a prime-power leaf, the nonidentity element can be nontrivial at
only one of p and q, so its gcd with N is proper. The cost is again
soft-O(K+K0+1)*poly(L).

This shortcut uses the semiprime hypothesis. The general theorem above
does not: it always returns a short period and does not need a factor.

A COMMON-DENOMINATOR POWER TABLE

Suppose positive known integers v_1,...,v_t are denominator factors,
and let M=product_i v_i. A product tree computes all values

```text
  eta^(M/v_i) mod N
```


in soft-O(t+bitlength M)*poly(L) bit operations. If every v_i>=2, the
t term is absorbed by bitlength M. At a tree node with
denominator product V, store eta^(M/V). For children V_1,V_2, obtain
the two child values by raising the parent value to V_2 and V_1,
respectively. At each tree level the sum of exponent bit lengths is
O(bitlength M), and there are O(log t) levels. Repeated factors and
noncoprime denominators do not invalidate the identity. If the v_i
are smooth numbers with known factorisations, M is supplied factored
as well. A returned period of the form (M/v_i) D_short is then covered
by the theorem.

LCM VERSION WITHOUT PRODUCT INFLATION

Suppose instead that factorizations of all denominators are supplied,
and use the smaller M=lcm(v_1,...,v_t). The same output table can be
constructed in soft-O(bitlength(M)+sum_i bitlength(v_i)+t)*poly(L) bit
operations. In this statement denominators and M are represented as
ordinary integers or by factorizations whose input-reading cost is
also charged; bitlength(M) is not treated as a unit-cost parameter.

Write M=product_j ell_j^e_j. The prime-power exponent-propagation tree
computes eta^(M/ell_j^e_j) for every j. Repeatedly raising each such
value to ell_j gives eta^(M/ell_j^f) for every 1<=f<=e_j. The sum of
the exponent-bit costs of these chains is O(sum e_j log ell_j)=O(log M).
Also compute eta^M once. All these elements are units modulo N.

For one denominator v>1, let P_j=ell_j^f_j be its distinct primary
factors, set w_j=v/P_j, and choose c_j in [0,P_j) with c_j*w_j=1 mod P_j.
The sum of these CRT idempotents is 1 modulo v. Thus

```text
  k=(sum_j c_j*w_j-1)/v
```


is an integer with 0<=k<number_of_primary_factors(v), and the exact
integer identity

```text
  M/v=sum_j c_j*(M/P_j)-k*M
```


gives

```text
  eta^(M/v)=product_j (eta^(M/P_j))^c_j * (eta^M)^(-k) mod N.
```


The exponents c_j have total bit length O(sum log P_j)=O(log v); the
additional exponent k is smaller than the number of factors. All CRT
arithmetic and inversions are on known integers or known units. For
v=1 use eta^M. This proves the stated total cost and does not request
any unknown modular root.

LIMIT OF THIS LEMMA

This controls arithmetic and recovery for known-denominator powers.
It does not make a rational baby progression into an integer progression
of the same size. For instance, replacing an integer phase by P(t)/v
and clearing its denominator generally introduces v fractional index
classes, or a residue correction modulo v depending on t. That separate
product-search cost must still be charged. Nor does the lemma shorten
an arbitrary unfactored long period.

**Attribution:** Yilin Liu and GPT-6 Astra Pro.
