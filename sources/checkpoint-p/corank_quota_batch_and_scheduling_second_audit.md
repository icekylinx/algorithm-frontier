# Second independent audit of corank quotas, batch branching, and scheduling

**25 October 2026. Independent mathematical review of the complete composition.**

Reviewed manuscripts:

* `unit_quota_corank_gap_branching.md`;
* `unit_quota_corank_batch_branching_improvement.md`;
* `two_size_makespan_corank_three_halves_transfer.md`.

The proofs pass. The batch algorithm gives Gamma(t/(t-b))^c
times polynomial input work, where Gamma(R)=R^R/(R-1)^(R-1).
In particular the critical four-to-two promise takes 4^c time,
and both exact factor-two unit allocation and exact factor-three-
halves two-size scheduling take (27/4)^c time, up to polynomial
factors. The parameter is the explicitly defined loop-deleted
corank, and the numerical supply magnitudes remain binary.

## 1. The deficient-set promise has the correct direction

At a ground restriction Q retaining player rank r, let d=|Q|-r.
A deficient set satisfies f(S)<b|S|. If a t-unit basis I* exists
inside Q, feasibility gives

`t |S intersection I*| <= f(S)`.

For the single-deletion proof this implies
`(t-b)|S|<td`, since I* omits only d elements of Q. The strict
inequality justifies the ceiling-minus-one branch bound and the
guard that rejects larger sets on unpromised instances.

For the batch proof put m=|S| and
ell=m-floor(f(S)/t). Because f is nonnegative and deficient,
1<=ell<=m. Every promised basis omits at least ell elements of S.
If ell>d the target promise is impossible. Otherwise at least one
enumerated ell-subset consists entirely of omitted elements; deleting
it leaves the promised basis and preserves player rank. This is
the witness branch needed for the inductive correctness argument.

No claim that every branch preserves the promise is needed. Every
successful leaf verifies resource feasibility of b*1_Q and then
takes a player basis inside Q. Downward closure and monotonicity
justify zero extension to the original resource ground. Every
failure is proved against the stronger t-unit target.

Deleting player loops initially is harmless. Subsequent ground
deletions always restrict the same f; they do not contract it or
recompute any dual on a smaller universe. Rank zero exits before
the recursion, and corank zero either immediately succeeds or
rejects a genuine deficiency.

## 2. The entropy bound gives single-exponential time

With R=t/(t-b)>1, deficiency gives ell>m/R. For m>ell,
the binomial expansion at probability ell/m gives

`binom(m,ell) <= Gamma(m/ell)^ell <= Gamma(R)^ell`.

The derivative of log Gamma(x) is log(x/(x-1))>0, which proves
the required monotonicity. At m=ell there is one candidate subset;
the Gamma(1)=1 limiting convention is consistent. Thus the estimate
does not silently exclude a full-set deletion.

Every attempted deletion is counted as a child, including those
rejected by their player-rank test. This is essential because
enumerating those subsets still costs time. Each child has budget
d-ell. Induction gives at most (d+1)Gamma(R)^d computation nodes:

`1+binom(m,ell)(d-ell+1)Gamma(R)^(d-ell)
 <=1+(d-ell+1)Gamma(R)^d
 <=(d+1)Gamma(R)^d`.

The estimate is valid even when no promised basis exists. The guard
ell<=d prevents uncontrolled enumeration in that case. Rank tests,
submodular minimization and the arithmetic in floor(f(S)/t) all
have polynomial bit cost. A lexicographic subset iterator and
depth-first traversal require polynomial workspace.

Gamma(2)=4. For b=ceil(t/2) and t>=2, the ratio t/(t-b) is at
most three, with Gamma(3)=27/4. The exact one-unit algorithm covers
t=b=1 separately. These constants therefore follow from the actual
branching procedure, rather than from a numerical optimization of
the older single-deletion estimate.

## 3. Integer unit optimization uses a sound one-sided search

The optimum integer quota K* is at most floor(f(P)/r) for positive
rank r. This is a direct hard-target upper certificate, independent
of the gap algorithm's behavior. At K>=2, the batch routine returns
ceil(K/2) units or certifies K>K*. At K=1, Boolean-cap matroid
intersection is exact.

The stored upper index always exceeds K*, while the lower index
has a recorded successful output. At adjacent integer endpoints,
the lower index is at least K*. Its output is therefore at least
ceil(K*/2). Success need not be monotone and does not assert that
the full target K is feasible. The K*=0 case retains the zero-quota
basis; the empty-rank case is handled without assigning a finite
minimum to an empty selected set.

This is an integer-OPT theorem. No unproved stronger configuration-
LP comparator is used in the branching argument.

## 4. Scheduling forms its dual before restricting players

Let h be the large-unit total rank and N its Boolean recipient
matroid. If rank N<h, every large base has a repeated recipient,
so OPT>=2a. The public additive schedule OPT+a then supplies
factor three halves in polynomial time. This includes h>q.

If rank N=h>0, only the player ground is reduced to the nonloops
P+ of N, giving corank c=|P+|-h. For a target a<=T<2a, small-job
counts are capped at C=floor(T/u). A feasible target must retain
their full rank s. The complement dual

`f_T(S)=C|S|+g(P\S)-s`

is correctly formed on all original machines P. Only then is f_T
restricted to P+ for the unit problem. Machines without large-job
eligibility remain available in the small-resource dual and its
final base completion.

The exact promised quota is

`K=C-floor((T-a)/u)=ceil((a+Cu-T)/u)`.

Because 0<u<a<=T, one has 1<=K<=C and
0<a+Cu-T<=a<=T. An original target-T schedule therefore supplies
a K-unit N-basis in this dual. The K=1 case is again handled by
exact matroid intersection, so the gap theorem is never used at
t=b without justification.

## 5. Reconstruction has no additive small-unit loss

The returned b=ceil(K/2) count vector is extended by zero to P,
completed to an integer dual base, and complemented in C*1.
The resulting small count vector is a base of the capped resource
and, because total rank was preserved, a base of the original
small resource. The large indicator is a Boolean independent set
of size h and hence a base of the original large polymatroid.

For a selected large recipient, put delta=a+Cu-T. Its load is at
most

`a+Cu-bu=T+delta-bu <= T+delta/2 <= 3T/2`.

Here b>=K/2 and Ku>=delta. Other machines have load at most Cu<=T.
Every count is integral; this is why no extra +u is incurred.
The easy target T>=2a uses ordinary additive rounding and satisfies
the same 3T/2 bound. Targets below a fail soundly.

All original loads lie on a common rational size grid. A failed
lower target is strictly below OPT, and an arbitrary feasible
schedule supplies a successful upper target. At adjacent endpoints,
the successful upper target is at most OPT. This is the correct
minimization orientation; it does not require monotone success.

## 6. The corank oracle lower bounds match the factors

The hidden-subset construction in Section 6 of
`recipient_polymatroid_below_two_oracle_barrier.md` has uniform
player matroids with no loops. For allocation, its binomial query
bound is binom(q,c)-1 for every factor below two. For scheduling,
take h=q-c, large size two, small size one and total small rank
2c. For c>=2 the construction has OPT two, and any factor below
three halves must identify the hidden c-element complement.
It again requires binom(q,c)-1 queries.

Fixing c above a proposed uniform polynomial exponent rules out
fixed-parameter oracle time below the stated approximation factors.
The positive thresholds two and three halves are therefore matched
in this value-oracle sense. This does not establish optimality of
the exponential bases, an ETH lower bound, or the same hardness
for explicitly listed ordinary restricted-assignment instances.

The full composition is internally consistent. These are independent
mathematical checks, not implementation, formal verification,
external peer review, or exhaustive publication-priority claims.
