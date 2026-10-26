# A total-target ETH lower bound for explicitly encoded rank matroids

**25 October 2026. Complete conditional reduction; root and independent full
mathematical reviews passed.** This is an encoded-input companion to the
unconditional oracle lower bound in
[variable-dimension-total-target-classification.md](variable-dimension-total-target-classification.md).

Assuming deterministic ETH, no deterministic algorithm solves the
stated mixed-target problem on all polynomial-size rank-circuit
matroids in

$$
2^{o(T\log(T+2))}\operatorname{poly}(H),
\tag{ET1}
$$

where `T` is the total numeric target and `H` includes the explicit
rank-circuit description. The lower bound already uses binary row
coefficients and unit targets. It holds for pure covers over
independent sets or bases, pure upper rows over bases, and scalar
cardinality maximization over independent sets with pure upper rows.

The randomized conclusion requires randomized ETH separately. The
result is not a claim about graphic, linearly represented, or other
standard restricted matroid representations.

## 1. Assumption and computational model

Use the consequence of deterministic ETH that 3-SAT with `N`
variables has no deterministic `2^{o(N)} poly(|phi|)` algorithm.
This is the standard variable-count subexponential-time setting;
see the primary reference of Impagliazzo, Paturi and Zane below.

The resource matroid is supplied by a finite circuit computing
its exact rank on a subset indicator, or equivalently by a
uniform polynomial-time rank decoder with its parameter string.
The output instance is promised to be a matroid. The reduction
proves that promise for every input formula; it does not ask an
algorithm to verify arbitrary rank circuits.

The optimization algorithm may inspect the whole circuit and
exploit its description. This is not an opaque-oracle assumption.
Each rank evaluation and the entire circuit size are polynomial
in the produced input. Rank-circuit access is therefore a
concrete encoded representation, although it is much broader
than a matrix representation of a linear matroid.

## 2. Enough perfect matchings to encode all assignments

Given a 3-CNF formula `phi` with `N` variables, choose the
smallest even integer `d>=4` such that

$$
L_d=(d-1)!!\ge2^N.
\tag{ET2}
$$

Let the ground be all unordered pairs of `[d]`, and let
`r=d/2`. The number of perfect matchings on this ground is
exactly `L_d`. The recursion chooses the partner of the
smallest remaining vertex, giving `L_d=(d-1)L_{d-2}`.

Elementary product bounds give
`log L_d=Theta(d log d)`. Minimality in ET2 therefore implies

$$
d\log d=\Theta(N)
\tag{ET3}
$$

for growing `N`. The constant-size initial cases are harmless.
Computing the first such `d` uses polynomially many binary
operations. At the stopping point,
`L_d<(d-1)2^N` unless `d=4`, so the stored matching counts
have `O(N+log d)` bits.

## 3. Polynomial-time matching ranking and assignment decoding

Order perfect matchings recursively as follows. At a residual
ordered vertex set of even size `m`, choose the partner of its
smallest vertex in increasing order. Each partner choice has
exactly `(m-3)!!` residual matchings. If the chosen partner has
zero-based index `j`, the rank is

$$
j(m-3)!!+\text{rank of the residual matching}.
\tag{ET4}
$$

Use the empty matching rank zero and `(-1)!!=1`. This is a
bijection between the perfect matchings and integers
`0,...,L_d-1`. Recognition of a perfect matching and its
recursive rank both take polynomial time on binary data.
There is no enumeration of all matchings.

Decode a matching `A` into the `N` assignment bits of

$$
\operatorname{rank}(A)\bmod 2^N.
\tag{ET5}
$$

This map is surjective: the first `2^N` ranks already supply
all assignments. Evaluating `phi` on a decoded assignment
is polynomial time.

## 4. A valid matroid for every formula

Let `H_phi` consist of the perfect matchings whose decoded
assignment does not satisfy `phi`. Define a rank-`r` matroid
candidate by making every subset of size less than `r`
independent and making an `r`-set a basis exactly when it
does not belong to `H_phi`.

Distinct perfect matchings are not one-exchange neighbors.
Their endpoint-incidence sums are both the all-ones vector,
while their individual edge labels are distinct. The same
nonadjacency property holds for the subfamily `H_phi`.

This proves augmentation directly. Only a size-`(r-1)`
independent set and a size-`r` independent set need attention.
If there is only one candidate augmentation, it is the latter
independent set. If there are at least two, the resulting
rank-size sets are exchange neighbors, so at most one can
be forbidden. An augmentation exists. Heredity is immediate.

There are nonmatching `r`-sets for `d>=4`, so the resource
rank is indeed `r`, regardless of satisfiability. Denote
this matroid by `M_phi`.

Its rank on a query set `S` has the following explicit
polynomial-time computation:

- If `|S|<r`, return `|S|`.
- If `|S|>r`, return `r`.
- If `|S|=r` and `S` is not a perfect matching, return `r`.
- Otherwise return `r` if `phi` accepts its decoded assignment,
  and return `r-1` if it does not.

The second branch is correct because a larger set contains
two neighboring rank-size sets, at least one of which is
not forbidden. All operations, including ET4 and formula
evaluation, use polynomial time and polynomial bit lengths.
They can be compiled uniformly into a Boolean rank circuit
of polynomial size. The only formula-dependent operation
is evaluating `phi` on one specified assignment.

## 5. Unit target rows encode satisfiability

For every vertex `j` create its incidence row on the edge
ground, with target one. There are `d` rows, all with binary
coefficients, and

$$
T=d.
\tag{ET6}
$$

A base satisfying equality in every row is a perfect matching.
Such a matching is a basis of `M_phi` precisely when its
decoded assignment satisfies `phi`. Surjectivity of ET5
therefore gives

$$
\phi\text{ is satisfiable}
 \quad\Longleftrightarrow\quad
 \text{the target instance is feasible}.
\tag{ET7}
$$

The same equivalence holds for pure covering rows over either
independent sets or bases: total endpoint incidence is at most
`2r=d`, whereas all covers require at least `d`, so every
row and the cardinality must be exact. It also holds for
pure upper rows over bases, where total incidence is already
`d` and the upper bounds force equality.

For pure upper rows on independent sets, maximize cardinality.
If `phi` is satisfiable the optimum is `r`. Otherwise it is
`r-1`: every full matching is forbidden, while every
`(r-1)`-edge partial matching is independent and respects
all upper rows. Thus exact scalar optimization distinguishes
the same SAT instances, with a feasible optimization family
in both cases.

## 6. Size and the ETH implication

The ground has `binom(d,2)` elements, and its explicit
incidence matrix has `O(d^3)` entries. All targets are one.
The rank decoder contains the formula, the recursive
matching-count constants and polynomial arithmetic logic.
Its size is polynomial in `N+|phi|`. The entire reduction
is polynomial time and produces a valid matroid for every
formula.

By ET3 and ET6, an algorithm with time ET1 would decide
3-SAT in `2^{o(N)} poly(|phi|)`, contradicting the stated
deterministic ETH assumption. If desired, duplicate and
tautological clauses can first be removed, leaving only
polynomially many distinct 3-clauses in `N`; no sparsification
claim is required by this particular reduction.

For a bounded-error randomized target algorithm, the same
reduction gives a bounded-error randomized subexponential
3-SAT algorithm. Excluding that consequence requires the
randomized version of ETH. Deterministic ETH alone is not
used to rule out randomized algorithms.

## 7. Relation to the unconditional oracle statement

The oracle lower bound uses a single hidden acceptable
matching, whereas this construction accepts every matching
whose decoded assignment satisfies a supplied formula.
The latter acceptance predicate is available in a polynomial-
size description; no unknown hidden set is assumed.

Consequently the two lower statements have different meanings:
the oracle statement is unconditional and counts information
queries, while this encoded-input statement is conditional
and bounds total computation even when the algorithm reads
the representation. Both match the total-target exponent
order of the exact upper theorem in their stated models.

## 8. Primary antecedents and attribution

Impagliazzo, Paturi and Zane, *Which Problems Have Strongly
Exponential Complexity?*, JCSS 63 (2001), 512–530, develops
the variable-count subexponential framework used here.
Primary article copy:
<https://courses.cs.washington.edu/courses/cse599i/24sp/papers/ImpagliazzoPaturiZane_2001_jcss.pdf>.

Doron-Arad, Kulik and Shachnai, *Lower Bounds for Matroid
Optimization Problems with a Linear Constraint*, arXiv
2307.07773v2, Section 4 and Definitions 4.4–4.5, explicitly
develops SAT-encoded matroid decoders. That is a direct
antecedent for encoding a predicate in a paving-type matroid:
<https://arxiv.org/html/2307.07773v2>.

The same authors' *You (Almost) Can't Beat Brute Force for
3-Matroid Intersection*, arXiv 2412.02217v2, Section 3,
defines G-matroids that accept arbitrary chosen balanced
grid subsets; Theorem 1.3 gives a rank-times-log-rank
parameterized oracle obstruction. Its two-dimensional
unit-target specialization already has permutation
candidates. These are substantive public antecedents:
<https://arxiv.org/html/2412.02217v2>.

The explicit matching-ranking reduction above proves the
stated total-target ETH consequence in full. It is not
presented as the first encoded-matroid hardness result or
as an exhaustive comparison of all prior representations.
