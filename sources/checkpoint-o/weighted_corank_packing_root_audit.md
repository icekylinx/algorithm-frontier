# Root audit: arbitrary weighted packing and exact-cost common bases

**25 October 2026. Completed internal mathematical review.**

This audit accepts `corank_packing_selection_oracle_extension.md`
(E1--E9), `corank_degree_bounded_common_bases.md` (G1--G10), and
`corank_weighted_prefix_free_batching.md` (WP1--WP16). The original
weighted singleton argument remains a valid predecessor, but its
factorial parameter dependence is superseded by the prefix-free
algorithm. The reviewed current bound is Gamma(t/(t-b))^c poly(H)
for arbitrary nonnegative rational packing coefficients, where
Gamma(R)=R^R/(R-1)^(R-1) and c=q-r.

## 1. What the selection oracle must actually supply

The allowed family consists of sets of one fixed cardinality r.
On every restricted candidate ground Q, the selector must produce
an allowed set contained in Q or certify that none exists. Exchange
axioms and hereditary closure are not required. Each call, including
one on a child immediately rejected, is paid polynomial work.

The packing separator acts on the original full system, with a
candidate vector b*1_Q extended by zero outside Q. It must return
a valid violated row with nonnegative rational coefficients and a
nonnegative capacity, all of polynomial binary length. Restricting
the row family to rows contained in Q would be invalid. The proofs
correctly retain the original rows and use current-ground weights
only to identify omissions.

At a successful leaf b*1_Q satisfies all rows. Nonnegative
coefficients make the selected subset b*1_I feasible as well.
The selector certifies exact original membership of I. These
facts justify output validity even without the stronger promise.

## 2. The weighted prefix certificate is complete

For a violated row, order current weights a_1>=...>=a_n>=0,
put a_(n+1)=0, W=sum a_i and d=n-r. The violation is u<bW,
so W>0. A stronger t-feasible witness omits a set D* of exactly
d elements whose weight satisfies

    a(D*)>=W-u/t>W/R,       R=t/(t-b)>1.

For prefix omission counts k_m, summation by parts gives

    a(D*)=sum_m(a_m-a_(m+1))k_m,
    W=sum_m(a_m-a_(m+1))m.

Hence some prefix has R k_m>m. The first such prefix, with ell
ones marking its omitted elements, is one of the enumerated
certificates and is contained in D*. Deleting it preserves the
same promised selected set. Its last bit must be one, and ell>=1,
so the corank decreases. If d=0, a violated row soundly rejects
the target before any enumeration.

Equal row weights are harmless; their consecutive differences vanish.
All strict threshold comparisons are made by exact rational arithmetic.
The proof never requires a coefficient-ratio bound or an integral row.

## 3. Prefix-free counting removes the extra exponential factor

Each enumerated certificate is a binary word that crosses R*k>m
for the first time at its endpoint. No certificate is a proper
prefix of another. In a finite Bernoulli word of length n, with
success probability 1/R, a certificate with ell ones and z zeros
has probability

    (1/R)^ell ((R-1)/R)^z >= Gamma(R)^(-ell),

because z<(R-1)ell. Disjoint certificate cylinders therefore give

    sum_certificates Gamma(R)^(-ell)<=1.

This is a counting argument for a deterministic algorithm. No random
bits or probabilistic success guarantee are part of the procedure.
Different branches may later delete elements represented by zero
bits in an earlier certificate; that does not invalidate the local
counting inequality, which is used solely to bound branching cost.

## 4. Enumeration work is included, not assumed away

For remaining corank d>=1, the enumerator uses at most d ones,
at most Z_d=ceil((R-1)d)-1 zeros, and actual word length at most
n. It stops at the first density violation. Every needed certificate
has these bounds, since its zeros are fewer than (R-1)ell.

At one fixed word length, complete any explored word to a word
with exactly d ones and Z_d zeros. The completion preserves the
original prefix and therefore gives an injection at that length.
There are at most

    (n+1) binom(d+Z_d,d) <= (n+1) Gamma(R)^d

local states. The completion is used only in the proof and is
never constructed. Even if Z_d is numerically huge, the actual
word length is bounded by the explicit current ground size.
Z_d=0 and a full-ones certificate are included without exception.

For a fixed polynomial P(H), the complete work obeys

    T(d)<=P(H)Gamma(R)^d+sum_D T(d-|D|).

Using the prefix-free bound and |D|>=1 gives

    T(d)<=P(H)(d+1)Gamma(R)^d.

This includes local dead-end generator states, sorting, separation,
all candidate child construction, and selectors rejecting a child.
The same estimate holds on unpromised inputs. Paused generators
have length at most q and recursive depth at most c<=q, establishing
polynomial workspace. The algorithm does not evaluate Gamma.

The older all-prefix proof with (2 Gamma(R))^c is also valid;
the first-crossing family is the precise additional ingredient
that improves its base. This strengthening has been checked
independently in full.

## 5. Exact selected structure and augmented capacities

For an original system a_i*1_I<=u_i, inflate capacities to
(1+epsilon)u_i and use t=1+epsilon, b=1. An original feasible set
satisfies the stronger promise. The output retains exact membership
in the allowed family and obeys every capacity within 1+epsilon.
Failure is a sound original-feasibility rejection. The runtime is

    Gamma((1+epsilon)/epsilon)^c poly(H).

This applies to any number of explicit nonnegative weighted rows,
or to a proved polynomial separation interface. It does not apply
to negative row coefficients, arbitrary unimplemented projection
oracles, or a relaxed selection oracle.

For two exact player matroids and a cost threshold W, weighted
matroid intersection supplies the required restriction selector
for common bases of cost at most W. Thus both original matroids
remain exact while weighted side capacities are augmented.

## 6. The cost comparator and search are correct

All selected sets have cardinality r, so adding a common constant
to element costs changes every selected-set cost by the same
amount. This safely makes costs nonnegative, including when the
original costs had either sign. The sum of shifted costs is an
upper bound on every common-basis cost.

At a cost target W, success returns an augmented-feasible common
basis of cost at most W; failure excludes all original-feasible
common bases of cost at most W. The cost-grid minimization search
starts below zero and at the explicit upper bound. Adjacent
failed-lower/successful-upper endpoints give upper target at most
the original integer constrained optimum. Undoing the fixed shift
preserves the cost-at-most-OPT guarantee. Success need not be
monotone or originally feasible. If the original instance is
infeasible, a reported failure remains sound, but success is still
allowed under the augmented capacities.

Additional matroid or polymatroid rank systems are separated in
full by submodular minimization. Their number and overlaps enter
polynomial input work. No exact intersection algorithm for three
arbitrary matroids is assumed.

## 7. The sharper exact bounded-capacity endpoint

For zero-one rows with integer capacities bounded by U_max, a
direct exact routine gives (U_max+1)^c poly(H). A violated row
contains u_i+1 candidate elements; every feasible selected set
omits one of them. Branching on those single deletions gives the
claimed bound, while a zero-capacity row forces deletion. A zero
remaining budget with any violation is rejected. The exact target
routine and the same cost search return an exact minimum-cost
solution or an exact infeasibility conclusion.

This improves the weaker bound obtained by choosing epsilon
small enough that augmented integer counts cannot cross the next
integer. It is explicitly a joint dependence on U_max and c.
The exact zero-one endpoint must not be silently extended to
arbitrary rational weighted rows, whose count increments can be
arbitrarily small relative to their capacities.

## 8. Public comparison boundary

The primary Kiraly--Lau--Singh theorem provides an additive
Delta-1 upper-degree error for one exact matroid in polynomial
time. The primary Linhares--Olver--Swamy--Zenklusen theorem
preserves one distinguished basis and its LP objective with
overlap-based multipliers on other matroid systems; its separate
knapsack extension has explicitly stated item-size errors.
Their statements were opened and checked directly. The new
corank theorem has two exact matroids, tunable multiplicative
capacity error and an integer-OPT cost comparator in a different
time regime. No uniform dominance follows.

A separate current-primary comparison records recent integer-
programming resource augmentation and monotone-local-search
frameworks. Coefficient independence alone is not claimed new.
The complete first-crossing argument establishes the stated
algorithm, but a bounded source search does not prove priority.
