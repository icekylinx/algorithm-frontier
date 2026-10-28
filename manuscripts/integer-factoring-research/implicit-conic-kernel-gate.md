# An explicit power-saving gate for the uncentered conic cover

<!-- imported-source: checkpoint_10_general_factoring_theory_2026-10-27.zip; implicit_conic_kernel_gate_2026-10-27.txt; sha256=7c788e48da0b5a4b062ddd429b0a73fe4ef02fd049d1b188bc016b6d3ccc8fba -->

**Scope:** retained separate research branch; not part of the selected conditional theorem review. See the [curated dependency and review map](../../problems/integer-factorization/sources.md).

Internal research reduction, 27 October 2026. This is a conditional
theorem about a missing product primitive, not a factoring algorithm
with a newly proved exponent.

## 1. The implicit input
Take the squarefree m~R and the uncentered cover from
large_two_power_uncentered_cover_2026-10-27.txt. For N=pq with p<q,
after removing factors at most P0=C*sqrt(N/R), the cover contains
integers a>0, b!=0, 0<|ab|<=8R, with content supported on m, and

```text
  u=aq+bp=tau+m^2*i,   |i|<=K=O(sqrt(N)/R^(3/2)).
```


Here tau is in the stationary image

```text
  T_m(a,b)={aN/sigma+b*sigma mod m^2:
             sigma in (Z/mZ)^*, b*sigma^2=aN mod m}.
```


The expression is independent of the lift of sigma modulo m. Use
canonical tau and an integer signed interval for i large enough to
contain every u. The exact test labels are

```text
  d(a,b,tau,i)=aN+b-tau-m^2*i.
```


All labels are positive for R=N^r with 1/5<r<=1/3, for sufficiently
large N: aN+b>=N-8R, while |tau+m^2*i|=O(sqrt(NR)+m^2)=o(N).
Their bitlength is O(log N). The true label is (p-1)(aq-b), so it
annihilates the multiplicative group modulo p. Any stationary-image
superset with the same signed interval can be used if positivity and
cover are retained.

The input to the proposed primitive is the short description (N,m,R,
beta), NOT the explicit list of all triples (a,b,tau). The existing
enumeration has R^(1+o(1)) records even after the logarithmic sign-trie
compression, and is itself too expensive for a strict power saving.

## 2. Hypothetical product primitive and the consequence
Fix 0<sigma<=1/2. Suppose that, over Z/NZ, the scalar product of

```text
  1-beta^d(a,b,tau,i)
```


over this implicit domain can be computed in

```text
  soft-O(R^(1-sigma)+sqrt(R*K))                       (H)
```


bit operations. Require the same upper bound for the simple binary
restrictions on a,b,tau,i used to isolate one nonunit leaf. This is a
uniform algorithmic assumption, including setup; the coefficient
materialization and the modular square-root/image enumeration must
not be hidden outside its cost.

If the hypothesized primitive is deterministic, then, using the 2026
order-preparation theorem described in Section 4, there is a
deterministic general integer-factorization algorithm with bit complexity

```text
  soft-O(N^((1-sigma)/(5-4*sigma))).                  (C)
```


To verify the exponent, put r=1/(5-4*sigma), R=N^r. The two exponents
in (H) are

```text
  (1-sigma)*r,
  (1/2)*(r+1/2-3*r/2)=1/4-r/4,
```


which coincide at t=(1-sigma)/(5-4*sigma). For sigma in (0,1/2],
one has 1/5<r<=1/3 and 1/6<=t<1/5. In particular, even sigma=1/100
would give t=99/496<1/5. A square-root saving in R would give t=1/6.

Small-factor screening up to P0=C*sqrt(N/R) costs soft-O(sqrt(P0)),
whose exponent is also 1/4-r/4=t. Since P0>N^(1/3) after choosing C,
every remaining non-prime, non-perfect-power cofactor is a product
of two distinct primes. The standard recursive reduction to complete
factorization does not multiply this power bound by a new N-power.

## 3. A preparation issue and a Las Vegas resolution
HH2021 Lemma 2.5 requires its requested global order bound to be at
least N^(2/5). Reusing that preparation literally would cost at least
N^(1/5) and would destroy (C). It must not be silently retained.

For the Las Vegas assertion, first perform the ordinary deterministic
small-factor screen just described. Set D=floor(P0/2). Sample a
uniform residue beta; gcd(beta,N) either factors N or certifies a unit.
Run the ordered baby-step/giant-step local-order screen up to D. A
proper gcd finishes. A full-N short-period leaf is simply grounds for
discarding this beta; no period-recovery theorem is needed at this
stage. If every tested difference is a unit, every local order exceeds
D. The product and geometric-evaluation implementation has cost
soft-O(sqrt(D)) per sample.

Conditioned on being a unit, beta is uniform in F_p^* x F_q^*.
The probability of being a primitive root in both components is

```text
  [phi(p-1)/(p-1)]*[phi(q-1)/(q-1)]
    =Omega((loglog N)^(-2)).
```


Such a beta certainly passes because p-1,q-1>D. Thus the expected
number of attempts is polylogarithmic. This establishes the required
high-local-order preparation for every input, without an unproved
distribution assumption about the prime factors.

After a product leaf is isolated, its nonzero O(log N)-bit label is
a period modulo at least one prime. A proper gcd already factors.
A full-N leaf can be handled by the proven prepared-base recovery
in deterministic_period_recovery_amortized_2026-10-27.txt. Its cost
is soft-O(N^(kappa+epsilon)+N^(1/4)/sqrt(D)), where
kappa=1/(4*sqrt(e))<1/6. The second exponent equals r/4<=1/12.
Choose a fixed epsilon<1/6-kappa. Both terms are below (C).

All random choices in the alternative preparation above have exact
certificates, so that alternative is Las Vegas. The unresolved hypothesis
is solely the complete implicit
product primitive (H), including restricted-domain descent. Existing
sign tries and scalar blocking give R+sqrt(R*K), corresponding to
sigma=0, and do not establish (H) for any positive sigma.

Primary inputs for the preparation: Harvey, arXiv:2010.05450, for the
deterministic bounded-small-factor screen; Harvey--Hittmeir,
arXiv:2105.11105, for geometric product/evaluation tools and the precise
restriction in Lemma 2.5. The period-recovery proof is in the companion
internal note cited above.

## 4. Deterministic preparation from the verified 2026 theorem
Harvey--Hittmeir, arXiv:2601.11131v2, Theorem 1.1, applies to every
1<=D0<N-1, without the old N^(2/5) restriction. It returns a proper
factor or beta with ord_N(beta)>D0 in

```text
  O(sqrt(D0)*log(D0)*log(N)/sqrt(loglog D0))
```


bit operations. This precise statement was checked against the primary
paper, version 2 dated 5 June 2026.

Choose s=ceil(sqrt(P0)) and D0=s^2. On receiving beta of global order
greater than s^2, use the geometric polynomial

```text
  Q_s(X)=product_(0<=i<s)(X-beta^i)
```


and evaluate at beta^(j*s), 1<=j<=s. The differences test every positive
exponent j*s-i from 1 through s^2. A nonunit leaf cannot have gcd N,
since that would contradict ord_N(beta)>s^2. Hence the screen either
produces a proper factor or certifies ord_p(beta)>s^2 for every p|N.
It costs O(s*log^2 N) by geometric construction and evaluation.

In the latter case all prime factors exceed P0. After primality and
perfect-power handling, the remaining input is a semiprime because
P0>N^(1/3). Both stages cost soft-O(sqrt(P0))=soft-O(N^t), exactly
the preparation required for (C). They also provide the local-order
hypothesis used in the period-recovery companion. This closes the
deterministic preparation issue for the conditional gate; the new
implicit product primitive remains unproved.

**Attribution:** icekylinx and GPT-6 Astra Pro.
