# Independent audit of binary scaled recipient-matroid configuration transfer

**25 October 2026. Independent mathematical audit of the complete draft;
substantive proof chain passes. No formal or external peer review is claimed.**

Reviewed document:
`scaled_recipient_matroids_binary_configuration_transfer.md`.
The new statement combines the compressed general-polymatroid algorithm
with a stronger comparator for a deliberately narrower resource class:
each supplied type has rank f_j=c_j r_Rj, and different types retain
separate configuration marginals.

## 1. Integer model and no hidden supply expansion

For one type, the condition n(S)<=c r_R(S) is equivalent to partitioning
the occurrences into c independent recipient sets. The note's matroid
union argument on a conceptual parallel extension is valid: for any
occurrence subset A, its size is at most the total count on its support,
which is at most c times that support's original matroid rank. The
union theorem then gives the desired partition.

This proves existence of a realization of the output count vector. It
does not supply an algorithm whose running time is linear in c, and
the note does not claim to print every copy. The actual implementation
uses only the natural-matroid count ranks and the O(r) record vectors
of the previously reviewed polymatroid algorithm. Local feasibility
must be invariant under permutations of copies of the same type, as
the stated count-family interface requires.

## 2. Fractional loss lemma

Fix a resource type and let L be the rank of its reserved natural-matroid
set W. Write a_p for its residual player-block rank and c for its scale.
For an independent set I of the underlying recipient matroid, the
whole copy set E_I is independent and has exactly c|I| elements.

The contracted block rank g(S)=r(W union E_S)-r(W) is normalized and
submodular even if W is dependent. Thus sum_(p in I) a_p>=g(I), while
g(I)>=c|I|-L. It follows that

\[
                        \sum_{p\in I}(c-a_p)\le L.
\]

Since a_p<=c, these weights are nonnegative. Every point y/c in the
recipient independence polytope is a convex combination of indicators
of independent sets, including the empty set if needed. Multiplying
the last inequality by those convex weights gives exactly

\[
                       \sum_p(1-a_p/c)y_p\le L.
\]

No factor depending on recipient rank is lost. Loop coordinates cause
no issue: their y coordinate is zero, their conceptual block is empty,
and their residual capacity is zero. Types with c=0 must be removed
before division, as the model explicitly does.

## 3. Player-local restriction and strictness

The private-slot argument is a convex-combination construction for one
player's local count vector. For each type, choosing n_j of c_j slots
uniformly and retaining its intersection with a fixed a_pj-slot set
preserves downward-closed local feasibility and the availability box.
The expected retained count is a_pj n_j/c_j. It is unnecessary for
different players' private slots to share any physical labeling.

The global compatibility of the fractional retained/lost accounting
comes from the loss lemma in Section 2, rather than from a claimed
joint random feasible allocation. This distinction is stated correctly
in the draft and is essential.

At a fresh completed scan, a feasible lambda-approximate oracle result
below B implies true available optimum below B/lambda. Hence every
positive player coordinate has retained expected value strictly below
(B/lambda)x_p. The eligible set has fractional mass at least w>0, so
strictness survives summation. Summing the nonnegative loss terms over
eligible players costs no more than the full loss budget. This proves
the strict lower cover Phi>(T-B/lambda)w when T>=B/lambda.

The new lemma therefore supplies exactly the lower-cover interface
needed by the prefix-normalized algorithm; it does not require changing
the already reviewed rank upper cover or its progress signature.

## 4. Fat configurations and the dual union

Choosing one fat unit per fat-containing configuration yields f_.j<=y_.j
and total f<=x<=1. Downward closure gives f_.j in c_j P_I(R_j), and the
unit coordinate bound puts it in the independence polytope of the
c_j-fold union matroid. The displayed minimum rank formula proves this
identification directly.

For a one-service assignment the multiplicity may be clipped to q;
there are at most q selected distinct recipient names to distribute.
Thus ordinary matroid union and decomposition remain polynomial oracle
operations even for binary c_j. Singleton local feasibility restrictions
are legitimate matroid restrictions and can be decided by any positive
factor feasible oracle on a singleton availability vector.

The sum of separate fat marginals belongs to the union matroid's
independence polytope because its coordinates are at most one. Adding
the dual base vector 1-x, extending the resulting independent vector
coordinatewise to a union base, and complementing gives x'<=h=x-f.
Scaling the original all-small configurations by x'_p/h_p preserves
their value threshold, local perspective constraints and each separate
recipient column. Zero h coordinates give zero x' and need no division.

Reverse decomposition and deletion of excess players produce an original
player basis with legal count vectors. No fractional point is needed
by the algorithm itself.

## 5. Complexity and boundary of the conclusion

All residual-rank computations are submodular minimizations on the q
explicit players with polynomial-bit modular terms. The number of
stored records is O(r), and pruning and record moves use binary counts.
The only exponential or quasipolynomial rank dependence is the proved
search signature. In particular, an exponential table of copy patterns
and a recipient-rank parameter are unnecessary.

For complete finite-bit wording, lambda should be a supplied rational
certified guarantee, or a supplied rational lower bound on one; eta is
a positive rational accuracy parameter. Their encoding lengths and any
oracle accuracy cost belong to H. This is a precision clarification,
not a change to the mathematical loss argument.

The component-level comparator is essential. The independent gap
construction f(S)=|S|+D min(1,|S|) consists of two different scaled
matroid components whose merged aggregate configuration relaxation has
gap approaching r. It does not contradict this theorem, which retains
the two columns. Conversely, integer-optimum guarantees from the full
polymatroid theorem survive merging; only the stronger comparator is
lost. The draft makes this separation correctly.

The audited conclusion is therefore a factor lambda^(-1)+3-3/r
rank-exponential algorithm, or that factor plus eta in the stated
rank-quasipolynomial time, against the supplied-component configuration
optimum, with polynomial binary-count storage and fully paid oracle
work. This is an internal proof review, not a publication-priority
determination or external validation.
