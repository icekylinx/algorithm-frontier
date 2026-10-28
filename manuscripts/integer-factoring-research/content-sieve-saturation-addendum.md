# Saturation of the current small-modulus content-cover count

<!-- imported-source: checkpoint_10_general_factoring_theory_2026-10-27.zip; content_sieve_saturation_addendum_2026-10-27.txt; sha256=0d03e402555be51724b4c3e01cf5a27f3b4955bdce4a8d5f6af7f2259c286cdd -->

**Scope:** retained separate research branch; not part of the selected conditional theorem review. See the [curated dependency and review map](../../problems/integer-factorization/sources.md).

Internal derivation and independent preprocessing audit, 27 October 2026.
This is an exact count of the presently represented family, not a lower
bound for factoring algorithms or for all possible coefficient covers.

Use the notation of content_hyperbola_sieve_2026-10-27.txt. In particular,
m<=N^(delta), delta=1/1000, M=m^2, L~log N, H~loglog N, R=N^(1/5+o(1)),
and f_g(A) is the B-period mean of the padded root multiplicity v_g(A,B).
Its A-period is M and its mean is c_g. All these weights are nonnegative.

Claim. In any full dyadic bucket W~R for which [W,2W) lies within the
enumerated range [1,8R],

```text
    n_W = Theta(W L/H^(3/2)),
```


uniformly for N coprime to m. Such a bucket always exists; for example
choose a power of two W in [R,2R]. The final clipped bucket itself need
not have this lower bound if its remaining width is exceptionally short.

Proof. Restrict to g|m, 1<=A<=X_g=floor(sqrt(W)/g), and the integers
B in [W/(g^2 A),2W/(g^2 A)). This already has B>=A and is a subset of
the actual bucket, including its orientation condition. A difference of
two B-prefix sums gives

```text
    sum_B v_g(A,B) >= (W/(g^2 A))*f_g(A) - O(m^3).
```


The O(m^3) error is uniform in g,A,N: a whole B-period has total weight
at most m^3, and the two endpoints lose at most two such periods.

Partition 1<=A<=X into complete blocks of length M. Each complete block
has f_g-weight exactly M c_g. On the j-th block, A<=(j+1)M, so its
contribution to sum f_g(A)/A is at least c_g/(j+1). Consequently,

```text
    sum_(A<=X) f_g(A)/A >= c_g(log(X/M)-O(1)).
```


For W~R and every g|m, g<=m and therefore

```text
    log(X_g/M) >= (1/2)log W-3log m-O(1)
                 >= (1/10-3delta+o(1))log N.
```


The coefficient 1/10-3delta is positive. Thus the last harmonic sum is
at least c*L*c_g with one absolute c>0, simultaneously for every g.
Summing the row lower bounds gives

```text
    n_W >= c W L sum_(g|m)c_g/g^2
             -O(m^3 sqrt(W) sum_(g|m)1/g).
```


The exact local means give

```text
    sum_(g|m)c_g/g^2 = Theta(H^(-3/2)).
```


Indeed, at each odd prime the additional Euler factor is
1+(ell+c_ell)/(2ell^2), where c_ell is 4 or 5 according to whether it
is unselected or selected; their difference affects only a convergent
sum of O(ell^(-2)). Together with (phi(m)/m)^2, Mertens gives the
claimed two-sided estimate. The prime 2 contributes a fixed positive
factor. Also sum_(g|m)1/g=O(H).

The error is negligible compared with the main term, since

```text
    [m^3 sqrt(W) H]/[W L/H^(3/2)]
       =O(m^3 H^(5/2)/(sqrt(W)L))
       =N^(3delta-1/10+o(1))=o(1).
```


This proves the lower bound. The already established uniform upper
bound in the main note supplies the matching upper bound. QED.

Consequence and scope. The current explicit root family truly has the
L/H^(3/2) density in a dominant bucket. A sharper estimate for exactly
this family cannot remove a power of L or H. A further asymptotic
improvement must change the represented family, exploit dependencies
without constructing all its roots, or use a different search primitive.
The result does not assert that every candidate is necessary, that the
shortest-vector subset has the same count, or that factoring itself has
an N^(1/5) lower bound.

**Attribution:** icekylinx and GPT-6 Astra Pro.
