# Independent audit of the polynomial-space global gap conversion

**25 October 2026. Full independent mathematical read of G1--G12: passes.**

This audit covers `polynomial_space_global_gap_conversion.md`, including its
forced-omission interface, exact local identity, explicit cover construction,
all failed completion calls, rational arithmetic, polynomial space, and public
scope. It does not certify an implementation or claim publication priority.

## 1. The exact local bound has no hidden entropy loss

Fix a block of size n, a promised omitted count p, and A>1. For

\[
 T_k=\frac{\binom nk}{\binom pk}A^{p-k},\qquad
 w_k=\frac{\binom pk(A-1)^k}{A^p},\qquad 0\le k\le p,
\]

the binomial theorem gives sum_k w_k=1. Cancellation gives exactly

\[
 \sum_{k=0}^p w_kT_k
 =\sum_{k=0}^p\binom nk(1-1/A)^k
 \le (2-1/A)^n.
\]

Thus a minimizing k has the desired bound. This includes p=0, p=n,
and k=0 without limiting arguments. All terms are nonnegative, and no
probabilistic algorithm is invoked. There is no A-dependent polynomial
loss that could become exponential across the blocks.

## 2. The local set cover is explicit and small enough

The universe consists of the N=binom(n,p) possible p-subsets. A candidate
k-subset covers exactly those universe members containing it. Every universe
member belongs to binom(p,k) candidates, so the uniform fractional cover has
weight L=binom(n,k)/binom(p,k), with L>=1.

If U members remain uncovered, at least one candidate covers U/L of them:
this follows by summing the candidate incidences of the uncovered members.
Greedy therefore covers all members within ceil(L log N)+1 choices when
N>1. Since log N<=n log 2 and L>=1, the manuscript's bound

\[
 |\mathcal C_{n,p}|\le(n+2)L
\]

is valid, including ceilings. If N=1, one candidate suffices. If k=0, the
single empty candidate covers the universe.

For n<=floor(log_2 q), both the universe and candidate list have at most q
members. Direct containment tests, uncovered-bit storage, and deterministic
greedy tie breaking are consequently polynomial in q. Even a deliberately
simple implementation that rescans all candidate/universe pairs at each
greedy iteration suffices. The proof does not rely on an implicit optimal
cover or a global combinatorial-design oracle.

## 3. Completeness protects the same full witness

Let D*=P\I* have size c. Its intersections with the fixed blocks determine
one enumerated profile. In that profile, each local cover has a member
Z_i contained in D* intersect B_i. Their union Z is therefore contained in
D*, so the original full-target selected set I* remains permitted.

The extension guarantee applies directly to that call. Every returned
success is already a valid relaxed-target witness, and complete failure
excludes every full-target witness. The approximation is not composed across
blocks: every call uses the same original full and relaxed targets exactly
once.

The interface is stronger than merely having a fast algorithm on the
unrestricted input. It needs a uniform bound for every forced omission,
including calls on unpromised instances. The accepted prefix-free routines
have this off-promise bound, and that is the property used here.

## 4. All Cartesian-product choices and all profiles are charged

Within a profile, every product choice forces the same number sum_i k_i of
omissions. Therefore the entire cost of the profile, including failed calls,
is at most a uniform polynomial factor times

\[
 \prod_i |\mathcal C_{n_i,p_i}|A^{p_i-k_i}
 \le (\ell+2)^m(2-1/A)^q.
\]

There are at most (ell+1)^m count profiles. Since
m=ceil(q/ell) and ell=floor(log_2 q), the total is

\[
 (2-1/A)^q\,
 2^{O(q\log\log(q+2)/\log(q+2))}\operatorname{poly}(H).
\]

Constructing each forced set and advancing the product iterator costs only
polynomial work per call; its extension multiplier A^(c-|Z|) is at least
one, so this work is absorbed. Local-table preprocessing is polynomial and
is absorbed as well. The short tail block has its actual size n_i, and
sum_i n_i=q, so it introduces no missing exponent.

For fixed A>1 the expression can be written
(2-1/A)^(q+o(q)) poly(H). The manuscript correctly retains the explicit
uniform expression when A is not fixed: one should not reinterpret the
additive o(q) exponent as uniform when the base approaches one.

For q<4, the direct constant-size treatment can enumerate all c-element
forced sets and call the extension at remaining deficit zero. This gives
polynomial work even if a supplied rational A has large numerical value.
The c=0 case needs only the unforced zero-deficit call. Empty selected sets
are outside the stated s>=1 interface and are handled separately by the
applications that admit them.

## 5. Polynomial space is proved for the actual representation

Only the local tables, one count profile, one list of product indices,
one q-bit forced set, and one extension workspace are live at a time.
There are polynomially many local tables, each with at most polynomially
many masks of logarithmic length. Product counters have polynomial total
length even though the product has exponentially many entries.

No global cover is stored, and no table is indexed by all global omitted
sets. A sequential depth-first or mixed-radix traversal therefore preserves
polynomial space whenever the extension routine does. This proof does not
equate a subexponential quantity with a polynomial quantity.

## 6. The numerical constants and encoding restrictions check

For a rational A, all local comparisons involve powers of exponent at most
ell and have polynomial binary length. Thus exact minimization is allowed.

The explicit specializations are correct:

| Gap time base A | Whole-ground base 2-1/A |
| --- | --- |
| 4 | 7/4 |
| 27/4 | 50/27 |
| 3125/256 | 5994/3125 |

For fixed rational R=a/b>1,

\[
 \Gamma(R)^b=\frac{a^a}{b^b(a-b)^{a-b}}.
\]

Raising positive comparisons to the fixed power b therefore implements the
sharp Gamma-based local minimization using exact rational arithmetic. This
argument is stated for fixed R, so it does not falsely expand a binary-sized
input exponent a or b in polynomial time. The alternative A=3R for varying
binary R is a valid polynomial-bit rational bound because Gamma(R)<=eR<3R.

## 7. Application interfaces that must remain explicit

For ordinary optional-player allocation, forced omissions restrict the
allowed selected players while all original recipient resource data remain
fixed. For selected flow, omitted commodities are not selected, and the
network and capacity representation remain fixed.

For adaptive heavy/light allocation, the selected set in this wrapper is
the LIGHT set of size r-k. Forced omissions prohibit those players only
from light candidacy. They must retain every original heavy-assignment
option and remain in the original player matroid. The surviving original
heavy/light pair still witnesses the minimum-completion residual budget.
Deleting those players globally would not satisfy the advertised interface.

The light-selection deficit is c+k, so the whole-ground wrapper still uses
the explicit original q-player ground. Trying all k up to r is polynomially
many applications and removes a small-heavy-support promise. The pure-heavy
k=r case is handled directly, not by pretending that positive light service
is required on an empty set.

No application may replace a binary-expanded ground with its compressed
machine count without a separate proof. The current theorem is stated only
for the explicit ground on which its forced-omission routine operates.

## 8. Public baseline and scope

The primary author manuscript of Fomin, Gaspers, Lokshtanov and Saurabh,
[*Exact Algorithms via Monotone Local Search*](https://sites.cs.ucsb.edu/~daniello/papers/monotoneLocalSearch19.pdf),
already gives the deterministic 2-1/A conversion in Theorem 1.2 and discusses
permissive subroutines in Section 2.3. Its Section 4 describes additional
subexponential storage for the presented derandomization. The current note
therefore correctly attributes the time base and proves its polynomial-space
block representation directly. This check is not an exhaustive search for
every subsequent space refinement.

The new allocation and flow consequences still depend on their separately
proved extension interfaces, adaptive residual-budget invariant, target
optimization, and exact-cost recovery. A generic time conversion alone
cannot substitute for any of those proofs. The manuscript maintains these
distinctions and does not make an unsupported first-result claim.

## 9. Audit disposition

The full G1--G12 chain passes. No substantive correction is required.
The result is a deterministic whole-ground exponential-time guarantee with
polynomial workspace and an unchanged approximation guarantee. It should be
reported together with the existing corank and direct-enumeration bounds,
allowing the strongest applicable bound for each instance.
