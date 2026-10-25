# Verification note

**Curated source path:** `sources/checkpoint-p/general_recipient_polymatroid_prefix_four_independent_audit.md`

The source audit follows.

# Independent audit of prefix normalization for arbitrary recipient polymatroids

**25 October 2026. Full mathematical review passed, including binary implementation and quota qualifications.**

This audit reviews Q1--Q11 of
`general_recipient_polymatroid_prefix_four_transfer.md`. It also uses the
independently reviewed natural-matroid and integer-loss arguments in
`general_recipient_polymatroid_independent_audit.md`.

The accepted research conclusion is factor

\[
              d=\lambda^{-1}+3-3/r
\]

against integer optimum, with exact-boundary rank-exponential time and
positive-error rank-quasipolynomial time as stated in that manuscript.
For an exact available-bundle oracle, d=4-3/r. The objects are arbitrary
integral recipient polymatroids supplied through value oracles; no
recipient-rank bound or numerical-capacity expansion is imposed.
This is an internal independent mathematical audit, not external peer
review or formal verification.

## 1. The entire candidate block must be independent

At a resource, the candidate contains a block C of copies belonging to
one player, with a possibly large binary cardinality n. Residual
availability guarantees

\[
                       r(W\cup C)-r(W)=n.
\]

The problematic test compares this entire block to M union X, not just
one copy at a time. If the increase is below n, the completion moves
every currently unmarked matching copy at that resource into the new
designated group. This is exactly the distinction needed for repeated
recipient units; an individual outside-closure test would not suffice.

At a problematic resource, every new reservation remaining before C is
an independent subset of W. At a nonproblematic resource, C is independent
over M union X, which contains every such reservation. Therefore all
new simultaneous reservations are valid without enumerating subsets.

## 2. Prefix additivity survives arbitrary block movements

For every ordered center prefix S, including an internal prefix of a
layer, the invariant is

\[
             r(W(S)\cup U(S))=r(W(S))+|U(S)|.
\]

The quantity |U(S)| is the number of units in unmarked matching records,
not the number of player owners or blocker groups. The proof works with
these potentially large cardinalities as binary integers.

Moving A subset U into W preserves independence of U minus A over
W union A. At a nonproblematic used resource, the entire candidate C
is independent over the original W union U, so it preserves that same
additivity after being adjoined to W. At a problematic resource, all U
is moved, so the new additivity statement has an empty unmarked set.
Earlier ordered prefixes do not change when a new center is appended.

## 3. A current block test proves strong freedom

For a stored center c, let V contain the earlier center/blocker prefix
and its own current designated matching group. When C is independent
over V, prefix additivity for the prefix ending at c gives

\[
 r(V\cup C\cup U)=r(V)+|C|+|U|.
\]

Without C, rank is at most r(V)+|U|, so adding C increases rank by its
whole cardinality. Thus C is independent over V union U, which is the
actual matching plus all earlier selected copies. This is the required
strong free-candidate statement for every retained prefix.

An empty designated group passes automatically, because its candidate
block was independent over its earlier prefix at birth and that prefix
can only lose copies while the center is retained. The same argument
allows a nonempty conservative group to be released when its dependency
has disappeared. A current failed block test supplies an integer rank
deficit of at least one. For a singleton blocker group, that deficit
must occur at a type used by the blocker; otherwise inherited birth
independence would contradict it.

## 4. Earliest exchanges and all old certificates remain valid

The player-side earliest circuit rule sends a nonaugmenting incoming
center from layer i to a layer h<i. Every retained center therefore
precedes it. Strong freedom applies against the matching and all those
selected copies simultaneously.

For a retained ordered prefix, deleting the outgoing matching record
either deletes some copies from W, deletes some from U, or has no effect
at a particular resource. Independence of U over W is preserved in all
three cases. The incoming block is independent over the entire old
W union U, so adding it as an unmarked record preserves additivity after
the deletion. This proof remains valid for large outgoing and incoming
counts, for repeated player names, and for prefixes inside layer h.

Record IDs and copy disjointness prevent numerical aliasing. The incoming
record receives no old designated-group flag. Releasing higher groups
does not change actual matching copies and does not change any retained
prefix; the proof already included those higher-group matching copies
among the unmarked elements of every lower prefix.

Below h, selected and designated records are literally unchanged, hence
the residual rank queries are unchanged. Their player eligibility flats
are unchanged by the earliest exchange lemma. Consequently old maximality
and growth statements below h are preserved as identical statements.
Only the last retained layer needs a new scan and test.

## 5. Eager normalization has a paid finite progress measure

The algorithm must scan all retained centers for a newly passing strong
release test. Removing an earlier marked record can erase dependency
witnesses for centers whose own groups did not change. Restricting the
scan to the outgoing record's assigned center would miss this case.

The draft performs a release as one atomic earliest player exchange,
not as an uncharged deletion of X or a standalone group release. At h,
X_h remains fixed and Y_h loses the outgoing record. All later layers,
including the incoming stored center's old layer, are discarded. Thus
the existing integer micro-signature strictly decreases. A nonaugmenting
normalization step strictly lowers the last layer index, so each episode
contains at most r such steps. Augmentation ends the phase.

All scans between signature changes cost polynomially many rank queries.
The total selected and blocker group counts remain O(r), irrespective
of the number of units in their records. The accepted exponential and
positive-growth quasipolynomial signature bounds therefore remain valid.

## 6. Current rank deficits give the sharp upper cover

The rank cover telescopes over ordered center prefixes. This current
telescoping charge, rather than a birth-time rank saving, is essential.

A center consisting of one unit of value at least B has only one-unit
blockers of that same type. A current failed release test makes its
unit dependent on the earlier prefix and those t blockers. The rank
increment is at most t, so its value charge is at most t u.

For a center containing at least two units, every unit has value below
B. Every sharing blocker also has no unit worth at least B, by inclusion
minimality. Put a=min(u,B); each such bundle has value below B+a. If
t>=2, their combined charge is below

\[
                 (t+1)(B+a)\le t(2B+a),
\]

because (t-1)B>=a. If t=1, the current failed test gives a shared type
j and saves at least one rank unit at that type. Removing just one
j unit from the minimal blocker leaves value below B, even if it
contains several units of j. The resulting charge is below 2B+a.

Summing the group charges proves

\[
               \Phi\le\max\{u,2B+\min(u,B)\}\,|Y|.
\]

Every dependency used here is tested in the present prefix, so the
birth-saving counterexample does not apply.

## 7. Integer optimum, fat reduction and the positive gap

The independent contraction-and-box loss lemma provides the unchanged
strict lower cover Phi>(T-B/lambda)w against any integral target-T basis
allocation. Combining it with the sharp upper cover gives the stated
condition tau B+rho C(B,u)<=T.

The fat-unit Boolean recipient matroids and dual-union construction
preserve an integral target promise on a derived player basis of rank
at most r. At B0=T/(tau+3rho), all remaining units have value below B0,
and C(B0,u)<=3B0. This proves the exact-boundary factor.

For eta0=min(eta,1), take B=T/(d+eta0), retaining fat threshold B0.
Since d>=1, B>=B0/2; therefore

\[
 C(B,u)\le\max\{B0,3B\}=3B,
 \qquad T-\tau B-3\rho B=\eta0 B.
\]

The proposed gamma=eta0/16 is safely below the gap divided by twice
the coefficient, namely eta0/6. This provides a uniform positive growth
margin. It does not deteriorate with a numerical recipient capacity.

The comparator remains integer optimum. The aggregate polymatroid
configuration relaxation has a rank-sized gap and is not imported into
this proof. A component-specific strengthened comparator needs a
separate fractional-loss argument.

## 8. Binary complexity and equal-unit arithmetic

Every rank query uses the natural-matroid minimum f(S)+z(P minus S),
with polynomial-bit modular terms. Every record stores only its count
vector. The current-prefix invariants are mathematical facts maintained
by the operations, not enumerated tests over exponentially many copies
or center subsets. The stated wrapper space and paid oracle cost are
therefore consistent. For finite-bit claims, lambda can be taken as a
supplied rational certified guarantee, or replaced by a supplied rational
certified lower bound.

For equal unit values and integer quota b, the improved cover
(2b-1)|Y| is correct: b=1 uses the singleton dependence case; b>=2
uses one saved rank for t=1 and (t+1)b<=t(2b-1) for t>=2.
Against integer target t, a failed scan leaves at most b-1 units per
eligible optimal player, hence the sufficient strict inequality is

\[
             (3-2/r)b<t+1+(r-1)/r.
\]

For b=ceil(t/3), the three residue-class gaps stated in the draft are
correct and positive. This gives the uniform factor-three
rank-exponential equal-unit conclusion. At t=4 and b=2, however, the
gap is only 3/r. The draft correctly withholds a uniform near-three
quasipolynomial theorem without another progress argument or a
separate small-quota algorithm.


---

**Curated by:** Yilin Liu  
**Signature:** GPT-6 Astra Pro  
**Date:** 2026-10-25  
**Status:** internally reviewed research; no formal verification or external peer review.
