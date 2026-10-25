# Independent audit of first-violation batching for weighted packing

**25 October 2026. Full independent mathematical review of WP1--WP16.**

Reviewed manuscript: `corank_weighted_prefix_free_batching.md`.

The weighted refinement passes. It obtains the same Gamma(R)^c
parameter dependence as the zero-one batch theorem for arbitrary
nonnegative rational row coefficients, with no coefficient-ratio
parameter. The Bernoulli distribution is a counting argument only;
the algorithm is fully deterministic. The explicit certificate
enumerator and its off-promise runtime are included in this review.

## 1. A violated row forces more than the allowed weighted omission share

At a node, the exact selector first confirms that an allowed
r-element member exists inside Q. Therefore d=|Q|-r is
nonnegative. If b*1_Q satisfies every original packing row,
the selector's member is feasible at b by downward closure.

For a violated row, sort all coefficients on Q in nonincreasing
order, keeping a deterministic order among ties. Its sum W is
positive because capacities are nonnegative and u<bW. Any
t-feasible witness I* has a complement D* of exactly d elements,
and

\[
                  a(D^*)=W-a(I^*)\ge W-u/t>W/R,
       \qquad R=t/(t-b).
\]

The strict inequality is essential and valid for rational t,b,u.
It does not require an integer capacity, a minimum positive
coefficient, or an integral row sum.

Summation by parts writes both W and a(D*) as nonnegative linear
combinations of prefix lengths and omitted-prefix counts. If
every omitted-prefix count k_m were at most m/R, that weighted
sum would be at most W/R. Hence a strict density violation
R*k_m>m occurs somewhere. Equal or zero coefficients do not
affect the implication: their differences in the summation vanish.

If d=0, no positive omitted weight is possible. The manuscript
correctly rejects before forming the zero budget or invoking the
enumerator; it never uses the otherwise undefined negative
expression ceil((R-1)*0)-1 in a counting formula.

## 2. First crossings cover a promised witness and form a code

Take the first prefix of the ordered witness-complement word with
R*k_m>m. Its ones mark a set D contained in D*, so deleting D
preserves the same allowed witness. The number ell of deleted
elements is between one and d, and the new corank is d-ell.
No zero in this word has to be permanently retained: completeness
only requires that the deleted ones avoid the promised member.

A first-crossing word ends in a one. Appending a zero cannot turn
a nonviolating density into a violating density. Thus its length
is determined by its last omitted position, and the word is
unambiguously associated with its deletion set. More importantly,
the words are prefix-free: an extension of a crossing word cannot
be a first crossing. This is exactly the property needed for
the branch charge.

The algorithm is free to explore certificates that do not extend
to any original witness; their selector calls may fail. Completeness
requires only the certificate extracted from a genuine D*. Every
successful descendant is still an original allowed member and is
checked against the original weighted packing system.

## 3. The finite Bernoulli bound gives the correct branch weights

Use the finite probability space of n independent bits with
one-probability p=1/R. A certificate with ell ones and z zeros
has cylinder probability p^ell(1-p)^z. Its final strict crossing
gives z<(R-1)ell, so

\[
       p^\ell(1-p)^z
          \ge p^\ell(1-p)^{(R-1)\ell}
           =\Gamma(R)^{-\ell}.
\]

These cylinders are disjoint because the words are prefix-free.
Their total probability is at most one, proving

\[
                 \sum_D\Gamma(R)^{-|D|}\le1.
\]

The argument works for every real R>1 and therefore for the
rational ratios used by the algorithm. Only the proof refers to
real powers. No Bernoulli random sampling, probability calculation,
or numerical approximation of Gamma occurs during execution.

This weighted sum, rather than a bound merely on the number of
certificates, is what permits deletion batches of different sizes
at one node without paying an extra exponential-base factor.

## 4. The enumerator includes all required first crossings

For d>=1, set Z=ceil((R-1)d)-1. This is a nonnegative integer.
Any valid certificate has ell<=d and

\[
                        z<(R-1)\ell\le(R-1)d,
\]

so z<=Z. Every proper prefix uses no more ones or zeros than the
certificate. A depth-first word generator with these count limits
and length limit n therefore reaches every required certificate.
Stopping immediately at the first strict crossing outputs exactly
the desired minimal prefixes.

This also checks the strict integer boundary in Z: when (R-1)d
is an integer, the zero budget is one less, as required by z<
(R-1)d. When R is close to one, Z can be zero. Then the
enumerator is still meaningful, and the first possible one
already crosses. No argument assumes R is an integer or at least
two.

The enumerator also explores nonterminal words that yield no
certificate. Their cost is explicitly included rather than being
charged only to successfully emitted branches.

## 5. The complete local-state bound is valid even for huge numerical R

Fix a word length m. A visited word has at most d ones and Z
zeros. Append the missing ones and then the missing zeros to
obtain a word with exactly d ones and Z zeros. This map is
injective among words of length m: the original length-m prefix
is recoverable from the completed word. Different original
lengths need not inject jointly, and the factor n+1 accounts
for precisely that issue.

Thus all local states are bounded by

\[
                       (n+1){d+Z\choose d}.
\]

Since d+Z<Rd, the finite binomial estimate gives
binom(d+Z,d)<=Gamma(R)^d. One can avoid any endpoint convention
by using success probability 1/R directly in the binomial
expansion:

\[
 {d+Z\choose d}
   \le R^d\left(\frac{R}{R-1}\right)^Z
   \le\Gamma(R)^d.
\]

This remains valid at Z=0. The completed words are only a
counting device. Actual words have length at most n<=q, even
when Z has a very large binary numerical value. The implementation
does not generate all completed words or allocate a table of
size Z.

Every local step uses exact polynomial-bit comparisons and counters.
Sorting and preparing the returned violated row are polynomial in
the explicitly guaranteed row encoding. Therefore a uniform
polynomial P(H) bounds local work by P(H)Gamma(R)^d throughout
the entire recursion.

## 6. The global recurrence counts rejected selector calls

For every emitted certificate D, the recursive call on Q minus D
is charged, even when its very first selector call fails. It has
the nonnegative remaining budget d-|D| because certificates have
at most d ones. Thus

\[
 T(d)\le P(H)\Gamma(R)^d+\sum_D T(d-|D|).
\]

With T(0)<=P(H), induction and |D|>=1 give

\[
 \begin{split}
 T(d)&\le P(H)\Gamma(R)^d
       \left(1+\sum_D(d-|D|+1)\Gamma(R)^{-|D|}\right)\\
     &\le P(H)\Gamma(R)^d(1+d) .
 \end{split}
\]

The last step is the prefix-free branch inequality. The proof
does not assume a promised solution exists. A node with no
possible witness and many rejected candidate deletions still
obeys the same bound.

Deletion recursion has depth at most c<=q. Each paused local
enumerator has depth at most q and stores polynomially encoded
words, row data and counters. Polynomial workspace follows,
including when the rational coefficient ratios or R are
numerically large. The factor c+1 in time is polynomial in
the explicit ground size.

## 7. The augmentation and cost consequences have the stated scope

Inflating capacities by 1+epsilon and setting t=1+epsilon,b=1
supplies the stronger promise from every original feasible
incidence vector. The output therefore remains an exact member
of the selected family and violates each nonnegative weighted
row by at most the multiplicative factor 1+epsilon. Failure is
sound original infeasibility.

A cost threshold can be included in a two-matroid common-basis
selector by weighted matroid intersection. The independently
audited negative-cost shift and failed-lower/successful-upper
cost search then apply without change. Costs are enforced by
the selector and are not augmented packing rows. The comparator
is the original integer optimum; no LP-optimum cost statement
is inferred.

The exact bounded-capacity endpoint for zero-one rows should
not be silently generalized to arbitrary rational coefficients:
there, an integer selected incidence vector can have a fractional
weighted row sum. The weighted manuscript claims only the
augmentation consequence and correctly avoids that unsupported
inference.

Nonnegative coefficients are essential to downward closure and
to the ordered layer-cake proof. A projected or implicit resource
system must provide a polynomial-bit nonnegative violated row;
mere abstract convex feasibility does not supply this interface
without a separate proof. The manuscript states that requirement
explicitly.

No gap was found in WP1--WP16. The coefficient-independent
entropy base, exact certificate generation, degenerate cases,
off-promise runtime and polynomial space are all supported by
the written argument. This is internal mathematical review;
the generic weighted result's publication-priority comparison
remains separate.
