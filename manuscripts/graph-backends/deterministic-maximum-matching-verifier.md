# A deterministic near-linear final maximum-matching verifier

24 October 2026. This note records a classical primary interface useful
for checking outputs of finite-parameter branches. It is not a new
matching algorithm and does not itself prove any uniform portfolio bound.

## Primary source and exact interface

Kurt Mehlhorn and Romina Nobahari, *Gabow's O(sqrt(n)m) Maximum
Cardinality Matching Algorithm, Revisited*, arXiv:2603.22909v2,
21 April 2026:

<https://arxiv.org/html/2603.22909v2>.

Section 2 describes Part I, initialized with an arbitrary current
matching. Section 2.3 explains that if an augmenting path exists, the
search discovers its bridge by Delta=floor(n/2); after `2Delta>n`
without discovery, no augmenting path exists. This concerns internal
distance phases of a single search, not repeated matching
augmentations. Section 4 gives `O(m alpha(n))` time per full iteration
with ordinary union-find, or O(m) with the specialized structure of
Gabow--Tarjan. Part I alone fits the same bound. Include O(n) setup
when isolated vertices are retained.

Therefore, given a valid matching M of an arbitrary general graph, one
deterministic search either finds an augmenting path or certifies that
none exists, in `O(n+m alpha(n))` time. The conservative inverse-Ackermann
factor suffices for every near-linear exponent comparison here.

## Verifier

Given an arbitrary proposed edge list:

1. Check original edge identifiers, endpoint validity, and vertex
   disjointness. Reject malformed lists.
2. Initialize the classical search with the resulting matching M.
3. If the search discovers an augmenting path, reject M as nonmaximum.
4. If it exhausts with no augmenting path, accept M.

Correctness is Berge's augmenting-path characterization: a matching is
maximum if and only if no augmenting path exists. Thus the verifier is
sound on every input and does not rely on a branch's claimed gap,
claimed LOW answer, numerical parameter adequacy, or internal state.

The verifier can work on the cleaned simple graph, with a final
original-ID check. In a subcubic reduction it can instead check the
materialized gadget matching before decoding. Both choices preserve
near-linear verification cost in their respective input sizes.

## Consequence for parameter branches

Suppose a proposed branch is known to produce a correct maximum matching
for sufficiently large inputs at its fixed parameter, but its behavior
on smaller inputs is only guarded termination or a possibly unreliable
candidate. The verifier converts the branch's output into either a
certified maximum matching or a rejected branch. A false finite-size
LOW conclusion then cannot cause an incorrect accepted output.

This observation alone does not give an efficient uniform algorithm.
One must separately bound the simulation overhead, initialization,
parameter encoding, word lengths, rejected-candidate verification, and
allocation of work among branches. A classical exact branch can provide
unconditional termination. If a complete uniform construction is used,
verification time must be charged as part of that branch's work.

## Avoiding an unnecessary formula dependency

Section 2.3 also discusses an explicit optimality labeling. The intended
standard bound is `n_1 + sum_(i>=2) floor(n_i/2)` when each edge either
touches label one or has equal endpoint labels at least two. The rendered
display appears to include other indices. The no-augmenting-path
verifier above does not rely on that displayed formula or on constructing
the labeling.
