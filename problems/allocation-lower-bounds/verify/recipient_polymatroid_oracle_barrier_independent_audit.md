# Verification note

**Curated source path:** `sources/checkpoint-o/recipient_polymatroid_oracle_barrier_independent_audit.md`

The source audit follows.

# Independent audit of the allocation and scheduling oracle barriers

**25 October 2026. Self-contained constructions reviewed successfully.**

The reviewed source is
`recipient_polymatroid_below_two_oracle_barrier.md`, including its
scheduling extension in Section 5. This note verifies the actual rank
functions and transcript arguments. No external parity theorem is needed
for either proof, and no novelty claim or explicit-representation
hardness claim is added by this audit.

## 1. The hidden-set recipient functions are valid

For q>r>=1, the cardinality function

\[
 f_0(S)=\min\{2|S|,2r\}-{\bf1}[|S|=r]
\]

has nonnegative nonincreasing increments: r-1 increments of two, then
one, one, and zeros. It is therefore normalized, monotone, integral and
submodular, including when r=1.

Raise its value by one at a single hidden r-set A. Monotonicity is
preserved because strict subsets have value at most 2r-2 and strict
supersets have value 2r. A submodular inequality can become harder only
when A is a union or intersection on its right side. If neither left
side equals A, the old inequality has exactly one unit of slack: for a
union A both operands are proper subsets, and for an intersection A
both operands are strict supersets. The raise consumes that unit.
Nested cases cancel the same raised term on both sides. Thus every
hidden-set function f_A is a valid recipient polymatroid.

## 2. Value above one identifies the hidden basis

Every rank-r uniform player basis can receive one unit per player.
The hidden basis A can receive two each: on another r-set, its overlap
with A has size at most r-1, and all smaller/larger set inequalities
are also satisfied. Conversely, two units on every member of an output
basis I require f_A(I)>=2r and therefore I=A. Total rank f_A(P)=2r
makes the integer optimum exactly two.

A deterministic approximation factor below two must output integer
minimum value greater than one and hence identify A. Before querying A,
all oracle answers equal those of f_0. If two candidate r-sets remain
unqueried, the same transcript cannot determine a correct output for
both. At least binom(q,r)-1 worst-case queries are required. Fixing
r above any proposed polynomial exponent of q excludes a uniform
f(r)poly(q) oracle bound; all oracle values have only O(log r) bits.

## 3. The scheduling dual is also a valid polymatroid

For q>=r+2, define

\[
                g_A(S)=2|S|+f_A(P\setminus S)-2r.
\]

Complementation preserves the submodular inequality after reversing
unions and intersections, and the modular term cancels. Every singleton
marginal of f_A is at most two, so every marginal of g_A is nonnegative.
Normalization follows from f_A(P)=2r. Its total rank is 2q-2r, and its
singleton ranks are exactly two because q-1>r. Thus g_A is a normalized,
monotone integral polymatroid with each coordinate bounded by two.

For a base x_s of g_A, the complement y=2*1-x_s is a base of f_A,
and conversely. Nonnegativity follows from the singleton upper bounds.
The base sums and complementary-subset inequalities prove this duality
directly. In particular, the complement of 2*1_A is the legal small-job
base 2*1_(P minus A).

## 4. A scheduling approximation below three halves identifies A

The large-job matroid is U_(r,q), with unit size two; the small-job
polymatroid is g_A, with unit size one. Both job vectors are required
to be bases, as specified by the scheduling model. Choosing large
recipients A and the complementary small base gives makespan two.
No schedule can do better because there is a size-two large unit.

An approximation factor below three halves gives makespan below three.
Integral loads are then at most two. Every large recipient receives
zero small units. If I is the large-recipient basis, the dual small
complement y consequently has at least two on every member of I.
The allocation argument forces I=A.

The oracle for g_A differs from the unraised version only at P minus A.
Thus the same hidden-set transcript argument requires binom(q,h)-1
queries, where h=r is the number of large-job units. This proves the
stated parameterized oracle barrier below three halves.

## 5. Limits of the constructions

The allocation example has optimum two and does **not** satisfy the
promise that a four-unit basis exists. It cannot obstruct an algorithm
that uses that stronger promise to produce a two-unit basis. Raising
all capacities or adding free units does not preserve such a hardness
conclusion automatically.

The scheduling example uses a full arbitrary small-job polymatroid
value oracle and mandatory base allocations. It gives no corresponding
hardness theorem for explicit restricted-assignment job lists or models
that permit dropping jobs. The constructions leave the stated gaps
between the current upper bounds and these barriers open.


---

**Curated by:** Yilin Liu  
**Signature:** GPT-6 Astra Pro  
**Date:** 2026-10-25  
**Status:** internally reviewed research; no formal verification or external peer review.
