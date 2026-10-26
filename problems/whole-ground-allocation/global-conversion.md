# A polynomial-space conversion from corank gaps to global exponential time

The conversion from an A^k extension algorithm to a whole-universe
base 2-1/A is established monotone-local-search background. This
note proves the precise two-target gap interface needed here and
gives a direct logarithmic-block construction with polynomial space.
The resulting applications hold for all coranks, without a small-
corank or heavy-support promise.

The explicit time bound for a supplied rational A>1 is

```math
(2-1/A)^q\,
       2^{O(q\log\log(q+2)/\log(q+2))}\mathrm{poly}(H).
\tag{G1}
```

For a fixed A>1 this is `(2-1/A)^(q+o(q)) poly(H)`. The space is
polynomial if the extension routine uses polynomial space. The
proof does not store an exponentially large global inclusion family.

## 1. The forced-omission gap interface

Fix an explicit q-element ground P and a required selected cardinality
s=q-c>=1. A full-target witness has a selected set I* of size s,
possibly accompanied by allocation, routing or completion witnesses.
The desired output is a valid relaxed-target solution of the original
problem. Full and relaxed targets are fixed throughout this wrapper.

For every forced omitted set Z subseteq P with |Z|<=c, assume an
extension routine on the allowed ground Q=P\Z that:

1. returns a valid relaxed solution with its selected set contained
   in Q, or fails;
2. cannot fail if a full-target witness has I* subseteq Q;
3. costs at most `A^(c-|Z|) poly(H)` on every input, including an
   unpromised one, and uses polynomial workspace.

The polynomial factor and query-description bounds are uniform
in Z. The original cardinality s and all original resource data
remain fixed. Only the allowed selected ground is changed.

The wrapper will return a valid relaxed solution, or soundly report
that no full-target witness exists. It is not an exact full-target
decision algorithm: a relaxed success is allowed above the full
feasibility threshold. No approximation is applied repeatedly across
blocks; every attempted completion uses the original single pair of
targets once.

## 2. An exact local weighted-count identity

For integers 0<=p<=n and 0<=k<=p define

```math
T_{n,p}(k)=
                   {\binom nk\over\binom pk}A^{p-k}.
\tag{G2}
```

The first ratio is the fractional size of a family of k-subsets
that covers every p-subset by containment. The power is the cost
of the remaining omissions after choosing such a k-set.

**Local identity.** For every real A>1,

```math
\min_{0\le k\le p}T_{n,p}(k)
                                    \le(2-1/A)^n.
\tag{G3}
```

To prove it, put

```math
w_k={\binom pk(A-1)^k\over A^p}.
\tag{G4}
```

These weights are nonnegative and sum to one. Their weighted
average of G2 is

```math
\begin{aligned}
  \sum_{k=0}^p w_k T_{n,p}(k)
      &=\sum_{k=0}^p\binom nk\left({A-1\over A}\right)^k\\
      &\le\sum_{k=0}^n\binom nk\left({A-1\over A}\right)^k
        =(2-1/A)^n.
 \end{aligned}
\tag{G5}
```

The minimum is at most this average. This proof includes p=0 and
p=n, needs no Stirling approximation, and has no rounding factor
depending on A. Probabilities are used only as a deterministic
counting device.

For rational A, the minimizing k can be found by checking all
p+1 values exactly. Their numerators and denominators have length
polynomial in n and the binary length of A.

## 3. Explicit local containment covers by greedy set cover

For one n-element block, fix p and its minimizing k. Let the
universe of a set-cover instance consist of all p-subsets of the
block. Each candidate k-subset covers the p-subsets containing it.
Every universe element belongs to exactly binom(p,k) candidates.
There are binom(n,k) candidates, so the uniform fractional cover
has total weight

```math
L={\binom nk\over\binom pk}\ge1.
\tag{G6}
```

Run ordinary greedy cover with deterministic lexicographic tie
breaking. If U uncovered p-subsets remain, summing their candidate
incidences shows that some candidate covers at least U/L of them.
After t steps the remaining count is at most
`binom(n,p)*exp(-t/L)`. Thus a covering family C_(n,p) exists and
is constructed with

```math
|\mathcal C_{n,p}|\le(n+2)L.
\tag{G7}
```

The loose n+2 factor covers the ceiling and the one-element-universe
cases. If k=0, the singleton family containing the empty set is
enough; the same bound holds. Repeated candidates need not be used.

There are at most 2^n universe elements and at most 2^n candidates.
When n is logarithmic in q, exhaustive greedy evaluation therefore
takes polynomial time and space in q. This local computation is
finite and explicit; no unimplemented combinatorial-design oracle
is assumed.

## 4. Fixed logarithmic blocks and count profiles

For q<4, enumerate all c-element forced omitted sets and invoke
the extension routine at residual deficit zero; there are at most
eight calls, with no factor A^c. Otherwise set ell=floor(log_2 q) and partition
P, in its given order, into m=ceil(q/ell) consecutive blocks
B_1,...,B_m of sizes n_i<=ell. Precompute the local minimizing k
and greedy family C_(n,p) for the block sizes needed and every
0<=p<=n.

Enumerate all profiles

```math
(p_1,\ldots,p_m),\qquad
              0\le p_i\le n_i,\quad\sum_i p_i=c.
\tag{G8}
```

They represent the possible counts of a full witness's omitted
set in the fixed blocks. There are at most `(ell+1)^m` such
profiles. Binary counters or a bounded-composition iterator
enumerate them in polynomial space. No random or balanced partition
is required; every possible distribution is explicitly covered.

For one profile, let k_i minimize T_(n_i,p_i). Iterate through the
Cartesian product of its local cover families. For each choice
Z_i in C_(n_i,p_i), form Z=union_i Z_i and run the extension
routine with those forced omissions. Each |Z_i|=k_i<=p_i, so
|Z|<=c and the extension call has nonnegative remaining deficit.
Return immediately on any successful relaxed solution; continue
until all profiles and product choices have failed otherwise.

## 5. Completeness with one unchanged promised witness

Suppose a full-target witness has selected set I* and omitted set
D*=P\I*, |D*|=c. Its block counts p_i=|D* intersect B_i| form one
of the profiles G8. By the local containment-cover property, for
every block there is a listed Z_i contained in D* intersect B_i.
Their union Z is contained in D*. Therefore I* subseteq P\Z,
and that extension call cannot fail.

Every successful extension supplies a valid relaxed solution of
the original problem. Total failure thus excludes every full
witness. The argument only needs a protected selected set and
the original completion promise. It applies to the residual-budget
recursion because a forced omission restricts light candidacy
only: all original heavy assignment options are retained, and the
same promised heavy/light pair is still available.

## 6. Complete time bound, including failed product choices

At a fixed profile, all product choices have the same seed size
sum_i k_i. Its total extension cost is bounded, up to a uniform
polynomial factor, by

```math
\begin{aligned}
 \left(\prod_i|\mathcal C_{n_i,p_i}|\right)
                 A^{c-\sum_i k_i}
   &\le\prod_i\left[(n_i+2)
       {\binom{n_i}{k_i}\over\binom{p_i}{k_i}}A^{p_i-k_i}\right]\\
   &\le(\ell+2)^m(2-1/A)^q.
 \end{aligned}
\tag{G9}
```

The last inequality is G3 in each block, and sum_i n_i=q. This
bound pays for every failed extension as well as every successful
one. The work of forming and traversing each product choice is
polynomial and can be absorbed because its extension cost factor
is at least one.

Multiplying G9 by the at most `(ell+1)^m` profiles gives

```math
[(\ell+1)(\ell+2)]^m(2-1/A)^q\mathrm{poly}(H)
   =(2-1/A)^q
     2^{O(q\log\log(q+2)/\log(q+2))}\mathrm{poly}(H).
\tag{G10}
```

Precomputing every local cover is polynomial: 2^ell<=q, only
polynomially many local instances are needed, and a direct greedy
implementation scans polynomially many candidate/universe pairs
per iteration. Its input rational comparisons have polynomial
encoding. Profile enumeration overhead is already below G10.
The asymptotic overhead in G10 is independent of the numerical
value of a supplied rational A; its encoding is included in H.

## 7. Polynomial space rather than storage of a global family

Store the local cover tables, whose total size is polynomial in q,
and the current block-count profile, product indices and q-bit
forced set. Invoke one extension at a time and reuse its workspace.
The original q-element input order translates local masks into
global elements without any extra family construction.

Every local universe has at most q elements and every local
candidate list has at most q subsets of at most log_2 q bits.
There are only polynomially many local tables. The count-profile
and Cartesian-product iterators have polynomially many counters
of polynomial bit length. Hence the wrapper's working storage is
polynomial in H, even though its streamed global family is large.

This differs from asserting that a published subexponential-size
derandomization object fits in polynomial space. The proof pays
for the present representation directly. Its time overhead is
subexponential, while the stored data remain polynomial.

## 8. The Gamma constants and explicit approximation choices

For the accepted half-quota and adaptive budgeted count gaps one
may uniformly take the rational constant A=Gamma(3)=27/4. G1 then
has whole-ground base

```math
2-1/A=50/27.
\tag{G11}
```

For a four-unit promise and two-unit output, A=Gamma(2)=4 yields
base 7/4. For intrinsic-value factor `2R/(R-1)` with a fixed
integer R>=2, the gap has

```math
A=\Gamma(R)={R^R\over(R-1)^{R-1}},
\tag{G12}
```

a fixed rational number. All comparisons above are then exact
rational comparisons. In particular R=2 gives factor four at
base 7/4; R=3 gives factor three at base 50/27; and R=5 gives
factor 5/2 at base 5994/3125.

More generally, for any fixed rational R=a/b>1, Gamma(R)^b is
the rational constant `a^a/(b^b*(a-b)^(a-b))`. Comparing the finitely
many G2 values can be done exactly by raising positive comparisons
to the fixed power b. Thus the sharp Gamma base is also available
for fixed rational approximation choices. This does not require
calling an exact transcendental real-number oracle.

If R is treated as a varying binary input and one does not supply
a certified polynomial-bit upper approximation to Gamma(R), the
simple rational choice A=3R is always valid since Gamma(R)<=eR<3R.
It yields a uniform bound with base `2-1/(3R)`. The sharper fixed-
accuracy statements must not silently impose the cost of expanding
huge powers a^a when a is binary encoded and unbounded.

## 9. Public attribution and the exact contribution of this manuscript

Fomin, Gaspers, Lokshtanov and Saurabh, *Exact Algorithms via
Monotone Local Search*, preliminary version STOC 2016, already
prove the deterministic whole-universe base 2-1/A from an A^k
extension routine. Their author-hosted journal manuscript has
the deterministic theorem as Theorem 1.2 and discusses permissive
subroutines in Section 2.3:
[author manuscript](https://sites.cs.ucsb.edu/~daniello/papers/monotoneLocalSearch19.pdf),
[arXiv record](https://arxiv.org/abs/1512.01621).

The discussion in that manuscript's Section 4 states an additional
subexponential-space cost for its presented derandomization. It
does not by itself certify the polynomial-space claim made here.
G2--G10 provide a self-contained streamed block proof for the
required extension-cost interface, including the same off-promise
time bound and the full-target/relaxed-target distinction.

The base formula is therefore not claimed as a new discovery.
The project applications must still prove their corank extension
oracle, preserve the original protected witness under forced
omissions, and perform their valid target searches and cost recovery.
Those are established separately in the named allocation, scheduling
and flow manuscripts. No exhaustive priority claim is made for the
block representation either.

This is a whole-ground exponential-time bound, not a polynomial-time
approximation result. It can be run alongside the original corank
algorithm and direct subset enumeration, retaining whichever valid
time bound is smaller for the instance. Binary-expanded slot grounds
are not replaced by the explicit machine count in this theorem.

---

**Attribution:** Yilin Liu and GPT-6 Astra Pro.
