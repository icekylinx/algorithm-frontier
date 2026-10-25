# Second independent audit of the polynomial-space global gap conversion

**25 October 2026. Full independent read and rederivation of G1--G12
in `polynomial_space_global_gap_conversion.md`.**

The theorem passes. A uniform polynomial-space forced-omission gap
routine with time A^(c-|Z|) converts to a deterministic whole-ground
gap routine with time

\[
 (2-1/A)^q\,
 2^{O(q\log\log(q+2)/\log(q+2))}\operatorname{poly}(H)
\]

and polynomial space, under the stated explicit-ground and encoding
conditions. Both targets remain unchanged in every extension call.
The conversion preserves sound full-target rejection and valid
relaxed-target construction; it does not turn a gap oracle into an
exact full-target decision procedure.

This review checks the entire written construction, including work on
seeds that destroy every promised witness. No substantive gap was found.
The small-q convention can be made fully explicit by enumerating all
complete c-element omitted sets and using only deficit-zero extension
calls. This also covers a varying, numerically large rational A.

## 1. The extension interface is sufficient, and its uniformity is necessary

The original selected cardinality s and all resource, routing, cost, and
completion data are fixed. A seed Z only changes the allowed selected
ground to Q=P\Z. Its remaining deficit is exactly c-|Z| because
|Q|-s=q-|Z|-s. The construction never calls the routine with |Z|>c.

Completeness requires only one full-target witness whose selected set
survives the seed. The routine may return a different relaxed witness,
and it may succeed on a seed admitting no full-target witness. Both
behaviors are compatible with the wrapper. Every returned witness must
nevertheless satisfy the original relaxed problem.

The running-time hypothesis applies to every allowed seed, including
those with no compatible selected set or no full-target witness. This
uniform off-promise bound is used in the Cartesian-product sum. A time
bound valid only on promised seeds would not establish the theorem.
Likewise, the polynomial factor and all query encodings must be uniform
in Z. These requirements are explicitly stated.

For adaptive-budget allocation, a forced omission removes only a light
candidate label. All original heavy assignment options and original
recipient constraints remain. Thus a surviving original light set
retains its original compatible heavy witness. The global wrapper does
not introduce a new deletion of heavy resources or owners.

## 2. The exact local weighted identity is correct

Fix 0<=p<=n and define

\[
 T(k)=\frac{\binom nk}{\binom pk}A^{p-k},
 \qquad
 w_k=\frac{\binom pk(A-1)^k}{A^p}
 \quad(0\le k\le p).
\]

Every denominator binomial is positive. By the binomial theorem,
the nonnegative w_k sum to one. Multiplication cancels both the
binomial denominator and the appropriate power of A exactly:

\[
 w_kT(k)=\binom nk\left(\frac{A-1}{A}\right)^k.
\]

Summing only through p gives a truncated binomial expansion with
nonnegative terms. Extending the sum through n yields

\[
 \sum_{k=0}^p w_kT(k)
 \le\left(1+\frac{A-1}{A}\right)^n=(2-1/A)^n.
\]

The minimum T(k) is at most this weighted average. There is no missing
normalizing constant, asymptotic approximation, or loss depending on A.
At p=0, the sole choice is k=0 and T=1. At p=n, k=n gives T=1.
These boundary cases are included without a limiting argument.

For rational A, all local values can be compared exactly. If A has
bit length L_A, a power with exponent at most n has O(nL_A) bits;
binomial coefficients have O(n) bits. Cross multiplication therefore
has polynomial bit complexity. Choosing a deterministic first minimizer
resolves ties without changing any estimate.

## 3. Greedy local containment covers satisfy the stated bound

Let M=binom(n,p) be the number of p-subsets, and let
L=binom(n,k)/binom(p,k). Each p-subset contains exactly binom(p,k)
candidate k-subsets. If U universe members remain uncovered, the total
number of their incidences with all candidates is U*binom(p,k).
Consequently some candidate covers at least U/L currently uncovered
members.

Greedy selection therefore leaves at most M*exp(-t/L) uncovered members
after t steps. For example, t=ceil(L*ln M)+1 makes this quantity strictly
smaller than one, so the cover is complete by that point. Since
ln M<=n*ln 2<=n and L>=1,

\[
 \lceil L\ln M\rceil+1\le L\ln M+2\le(n+2)L.
\]

This proves G7, including M=1 and L=1. A previously chosen candidate
covers no remaining member, so it need not be chosen again. The k=0
case uses just the empty subset and covers the entire local universe.

Every local block has n<=floor(log_2 q), hence at most q possible subsets.
A direct implementation may store all universe masks and candidate
masks, scan their incidences to evaluate a greedy step, and repeat at
most M<=q steps. This is polynomial time and space in q. Its intentionally
loose polynomial bound suffices; no efficiently constructed global
design or unimplemented set-cover oracle is required.

## 4. Every omitted-set distribution is explicitly represented

The fixed partition does not need to balance an unknown witness. For
any omitted set D* of size c, the numbers p_i=|D* intersect B_i| satisfy
the listed profile bounds and sum to c. That exact profile is enumerated.

For each block, its local family contains a k_i-subset Z_i of
D* intersect B_i. The Cartesian product includes this collection of
local choices. Their union is contained in D*, so the full selected set
I*=P\D* is contained in P\Z. The corresponding extension call cannot
fail. This proves completeness for one unchanged protected witness.

It does not matter that most other product choices need not be contained
in any valid omitted set. The algorithm checks them under the same
uniform extension bound. It also does not matter if one seed appears
in products belonging to different profiles; duplicate work is included
in the profile count, and no exponential duplicate-elimination table
is required.

There are at most product_i(n_i+1)<=(ell+1)^m profiles before imposing
the sum condition. Enumerating all such bounded tuples and filtering
their sum is already within this bound, or a bounded-composition
iterator can enumerate only those of sum c. Both need only polynomial
space. Thus profile generation does not depend on a favorable or balanced
distribution of D*.

## 5. The Cartesian runtime pays all failed seeds

Within one fixed profile, each local choice has cardinality k_i.
Therefore every global seed has exactly the same total size sum_i k_i,
and every extension call has the same remaining-deficit upper bound
A^(c-sum_i k_i). The complete cost for that profile is bounded by

\[
 \begin{aligned}
 \left(\prod_i |\mathcal C_{n_i,p_i}|\right)
       A^{c-\sum_i k_i}
 &\le
 \prod_i\left[(n_i+2)
        \frac{\binom{n_i}{k_i}}{\binom{p_i}{k_i}}
        A^{p_i-k_i}\right]\\
 &\le (\ell+2)^m(2-1/A)^{\sum_i n_i}
   =(\ell+2)^m(2-1/A)^q.
 \end{aligned}
\]

The first equality of exponents uses sum_i p_i=c. The last inequality
uses the independently verified local minimum bound in every block.
No choice is excluded because it is a bad seed; the cost is a count of
the full Cartesian product. Returning early on a successful seed can
only reduce it.

Constructing a seed, advancing indices, and checking a profile all take
polynomial work. Each product is nonempty and its extension factor is
at least one, so such work can be absorbed into the same uniform
polynomial factor. Multiplication by the complete profile bound yields
exactly G10.

For ell=floor(log_2 q) and m=ceil(q/ell), the logarithm of the extra
factor is at most

\[
 m\bigl(\log_2(\ell+1)+\log_2(\ell+2)\bigr)
 =O\!\left(\frac{q\log\log(q+2)}{\log(q+2)}\right).
\]

The polynomial local precomputation is absorbed as well. This establishes
the stated explicit bound even when A varies with its input encoding.
For q<4, enumerating full c-omission sets leaves remaining deficit zero
and takes at most eight extension calls, avoiding a spurious numeric
A^c cost in this direct base case.

## 6. Polynomial space follows from the actual stored representation

Local tables contain only subsets of logarithmic-size blocks. Each
local universe and candidate family has at most q members, each mask
has O(log q) bits, and there are polynomially many required local
instances. Storing the selected local covers, or even all local
incidence tables, is therefore polynomial.

The profile iterator uses at most m counters. The Cartesian iterator
uses one index into each local cover, and the current global seed uses
q bits. All these counters have polynomial bit length. One extension
routine runs at a time and its workspace can be reused. Streaming
the global product consequently avoids materializing a subexponential
or exponential global family.

The proof relies on q being an explicit ground size paid for by H.
A conceptual ground of binary many unit slots cannot be substituted
by its physical owner count in this construction. The manuscript
correctly keeps that limitation explicit.

## 7. Fixed Gamma choices and varying accuracy are separated correctly

The local counting inequality is analytic and valid for every real
A>1. Implementing the minimization nevertheless requires a valid
finite representation of the comparisons. For supplied rational A,
the earlier exact-arithmetic argument applies directly.

For fixed rational R=a/b>1, in lowest terms,

\[
 \Gamma(R)^b
 =\frac{a^a}{b^b(a-b)^{a-b}}.
\]

Thus raising a positive comparison between two local T values to the
fixed power b makes it a rational comparison. As a and b are fixed
accuracy constants, this has polynomial complexity in the instance
encoding. No transcendental-number comparison oracle is needed.

If a and b are arbitrary binary input integers, expanding a^a can
have nonpolynomial output length. The manuscript does not charge that
operation as polynomial. Its fallback A=3R is a polynomial-bit rational
upper bound because

\[
 \Gamma(R)=R\left(1+\frac1{R-1}\right)^{R-1}<eR<3R.
\]

The resulting uniform base is 2-1/(3R), as stated. A supplied certified
upper approximation could be used instead, but its construction and
encoding cannot be silently assumed.

The notation (2-1/A)^(q+o(q)) is justified when A>1 is fixed, because
the explicit subexponential factor can then be absorbed through a fixed
positive logarithm of the base. For a varying A approaching one, that
absorption need not be uniform. The manuscript properly leads with
the explicit G1 bound and limits this shorthand to fixed A.

## 8. The numerical constants and target interpretation check

Using the uniform half-quota bound A=Gamma(3)=27/4 gives
2-1/A=50/27. A four-to-two quota gap has A=Gamma(2)=4 and hence
base 7/4. For integer R, the intrinsic-value factor 2R/(R-1)
uses the stated fixed rational A=R^R/(R-1)^(R-1). In particular,

\[
 R=3:\quad \text{factor }3,\ \text{base }50/27;
 \qquad
 R=5:\quad \text{factor }5/2,\ \text{base }5994/3125.
\]

The latter follows from Gamma(5)=3125/256, so
2-1/Gamma(5)=(6250-256)/3125=5994/3125=1.91808.
These are global time bases; they do not multiply a relaxed ratio
once per block. Each extension is invoked only once on the original
full/relaxed target pair.

Applications must still handle an empty selected light set separately,
because the wrapper assumes s>=1. The existing pure-heavy branches do
so. Iterating polynomially many support sizes or value splits preserves
the global base, provided every call has the verified fixed-cardinality
extension interface. The wrapper alone does not establish these
application-specific promises or their outer target searches.

## 9. Primary-source attribution was checked directly

I freshly opened Fomin, Gaspers, Lokshtanov and Saurabh's
[*Exact Algorithms via Monotone Local Search*](https://sites.cs.ucsb.edu/~daniello/papers/monotoneLocalSearch19.pdf).
Theorem 1.2 states the deterministic base conversion with a subexponential
time factor; Section 2.3 covers permissive extension subroutines.
Section 4 explicitly describes an additional subexponential space
requirement for the presented derandomization. These passages support
the manuscript's attribution and its decision to prove the present
space bound directly. The base formula is established background.
This review makes no priority claim for the streamed block representation.

## 10. Audit conclusion

The exact local identity, explicit greedy covers, exhaustive profiles,
Cartesian cost including all failed seeds, and streamed polynomial-space
representation form a complete proof. The independent protected witness
argument matches the two-target gap semantics and the adaptive residual
budget interface. Exact arithmetic and fixed-versus-varying accuracy
are handled within the stated scope.

The theorem is accepted as an internally audited whole-ground
exponential-time conversion. It supplies no polynomial-time guarantee,
does not remove the underlying approximation gap, and does not replace
an expanded numerical slot count by a physical machine count.
