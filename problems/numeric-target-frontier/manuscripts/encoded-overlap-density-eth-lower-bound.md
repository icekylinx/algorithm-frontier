# An encoded ETH tradeoff across row-overlap densities

**25 October 2026. Complete new conditional reduction; root and independent full mathematical reviews passed.**

The overlap-density upper bound has an encoded-input counterpart. Under deterministic ETH, its exponent order cannot be uniformly reduced on the rank-program or rank-circuit representation described here, even when every target is one and every coefficient column has exactly two ones.

The reduction calibrates a family of disjoint cliques from constant clique order to one dense clique. It uses a polynomial-time ranking and decoding of products of perfect matchings. The resource is a proved valid matroid for every formula. Algorithms may inspect its entire rank circuit; the conclusion is conditional computational hardness, not an opaque-oracle lower bound.

Companion upper bound: [row-overlap-density-numeric-target-refinement.md](row-overlap-density-numeric-target-refinement.md).
The dense endpoint is also proved in [conditional-lower-bound-encoded-target-matroids.md](conditional-lower-bound-encoded-target-matroids.md); the present note supplies the uniform density tradeoff.

## 1. Assumption and precise representation

Use the deterministic ETH consequence that 3-SAT on `nu` variables has no deterministic `2^{o(nu)} poly(|phi|)` algorithm. The randomized conclusion would require randomized ETH separately.

The resource matroid is supplied either by a uniform polynomial-time rank decoder with its finite parameter string, or by an explicitly constructed Boolean circuit computing its exact rank on a subset indicator. The instance is promised to be a matroid; the reduction proves that promise and does not require the algorithm to recognize arbitrary rank circuits.

The input length `H` includes the complete rank-program or circuit description. All rank computations, all circuit sizes, and the complete non-oracle data produced below are polynomial in the input formula length. Nothing prevents an algorithm from reading the formula embedded in the circuit. A faster solver would still solve 3-SAT through the reduction.

This representation is broader than an explicit matrix, graph, or laminar family defining the resource matroid. No corresponding hardness for those restricted representations is claimed.

## 2. Clique parameters and integer calibration

Let `phi` have `nu>=1` variables. Choose an even integer `b>=4`, and put

$$
A_b=(b-1)!!,
\qquad
p_b=\lfloor\log_2 A_b\rfloor,
\qquad
L=\left\lceil\frac{\nu}{p_b}\right\rceil.
\tag{ED1}
$$

The positive integer `p_b` is obtained from the binary length of `A_b`; no real logarithm is needed by the construction. We use choices satisfying

$$
1\le p_b\le2\nu.
\tag{ED2}
$$

Build `L` disjoint labeled complete graphs of order `b`. Their vertex count, edge count, and intended matroid rank are

$$
T=bL,
\qquad
m=L\binom b2=\frac{T(b-1)}2,
\qquad
r=T/2.
\tag{ED3}
$$

The vertex count will be the total numeric target, and `m` will be precisely the row-interaction edge count.

Elementary product estimates imply, uniformly for even `b>=4`,

$$
p_b=\Theta(b\log(b+2)).
\tag{ED4}
$$

For example, at least `floor(b/4)` factors in `(b-1)(b-3)...1` are at least `b/2`, while every factor is at most `b`. Taking a floor loses only a constant factor because `log_2 A_b>=1`.

The ceiling in ED1 gives

$$
\nu\le Lp_b<\nu+p_b\le3\nu.
\tag{ED5}
$$

Consequently,

$$
T\log\left(2+\frac mT\right)
=bL\log\left(\frac{b+3}{2}\right)
=\Theta(Lp_b)
=\Theta(\nu),
\tag{ED6}
$$

with constants independent of the admissible choice of `b`. In particular, `T=O(nu)` and `m=O(nu^2)`.

All quantities in ED1 can be computed by ordinary integer multiplication and binary-length inspection. Stored matching counts have polynomial bit length. More specifically,

$$
\log_2(A_b^L)<L(p_b+1)\le2Lp_b\le6\nu.
\tag{ED7}
$$

Thus even the complete product of matching counts needs only `O(nu)` bits.

## 3. Polynomial ranking of a clique matching

At an ordered set of `t` remaining vertices, with `t` even, take its smallest vertex. Order its `t-1` possible partners increasingly. Every fixed partner leaves exactly

$$
A_{t-2}=(t-3)!!
\tag{ED8}
$$

matchings of the remaining vertices. If a given matching chooses the partner at zero-based index `j`, define its rank recursively by

$$
\operatorname{rank}_t(M)=j A_{t-2}
 +\operatorname{rank}_{t-2}(M\text{ on the remaining vertices}).
\tag{ED9}
$$

Use the empty matching rank zero and `A_0=1`. This is a bijection from the `A_b` clique matchings to the integers `0,...,A_b-1`. Its inverse divides a proposed rank by `A_{t-2}`, uses the quotient to choose the partner, and recurses with the remainder. Both ranking and unranking use only polynomially many operations on polynomial-length integers. No enumeration of matchings is performed.

Given a perfect matching of the disjoint union, let its clique ranks be `j_1,...,j_L`. Give it the product rank

$$
J=\sum_{i=1}^L j_i A_b^{i-1}.
\tag{ED10}
$$

This is a bijection between all perfect matchings of the union and the integers `0,...,A_b^L-1`. The mixed-radix inverse is polynomial-time for the same reason. Recognition of a perfect matching is also polynomial: each vertex must have degree exactly one in the queried edge subset.

By ED5, `A_b^L>=2^nu`. Therefore the first `2^nu` ranks encode every Boolean assignment of the formula bijectively. Call a perfect matching **accepted** precisely when `J<2^nu` and the `nu` binary digits of `J` satisfy `phi`. Ranks beyond this range are rejected. This acceptance predicate is computable by evaluating `phi` on one specified assignment, without solving a satisfiability problem inside the rank decoder.

## 4. A promised matroid with an explicit rank circuit

Let `H_phi` be the perfect matchings not accepted by the preceding predicate. Define the independent sets by allowing every edge subset smaller than `r` and allowing a rank-sized subset as a base exactly when it is not in `H_phi`.

Any two distinct perfect matchings are not one-exchange neighbors. They have the same all-ones endpoint-incidence sum, while distinct edges have different endpoint-incidence vectors. The forbidden subfamily inherits this property.

This proves the matroid augmentation axiom. The only nontrivial case compares an independent set of size `r-1` with an independent set of size `r`. If there is one available added element, the result is that known larger independent set. If there are at least two, their resulting rank-sized sets are one-exchange neighbors; at most one can be forbidden. An allowed augmentation exists. All smaller augmentation cases follow because every set below rank is independent.

There are nonmatching rank-sized subsets when `b>=4`, so the rank is exactly `r` for every formula, satisfiable or not. The resulting matroid is denoted `M_phi`.

Its exact rank on a query edge set `S` is computed as follows:

- If `|S|<r`, return `|S|`.
- If `|S|>r`, return `r`.
- If `|S|=r` but `S` is not a perfect matching, return `r`.
- If `S` is a perfect matching, compute ED10 and its acceptance predicate. Return `r` when it is accepted, and `r-1` otherwise.

The second branch is valid because a set larger than rank contains two adjacent rank-sized subsets, at least one of which is not forbidden. All operations in the decoder take polynomial time and polynomial binary space. Its loops have polynomial bounds in the explicit ground size, its arithmetic has `O(nu)`-bit operands by ED7, and formula evaluation is polynomial in `|phi|`. Standard bounded computation unrolling therefore constructs a Boolean rank circuit of polynomial size uniformly from the formula and `b`.

No uniqueness of a satisfying assignment is required: any subfamily of accepted matchings gives a valid matroid by the same argument. In contrast to an oracle hiding proof, the entire decoder and its formula are part of the explicit input.

## 5. Unit target rows and the reduction

For every vertex, create the row counting selected incident edges and give it target one. Each coefficient column has exactly two ones. The row-interaction graph is exactly the disjoint union of cliques, so its total target and edge count are precisely ED3.

With equality rows, a feasible base is a perfect matching. It is a base of `M_phi` exactly when its rank decodes to a satisfying assignment. All assignments appear among the first `2^nu` product ranks. Thus

$$
\text{the target instance is feasible}
\quad\Longleftrightarrow\quad
\phi\text{ is satisfiable}.
\tag{ED11}
$$

The same reduction works for the following variants.

- **Pure covers over independent sets or bases.** At most `r` edges have total incidence at most `2r=T`. The `T` unit covering rows force total incidence at least `T`, so every vertex is covered exactly once and the set is a full perfect matching.
- **Pure upper rows over bases.** A base has total incidence `T`; all `T` unit caps must be tight, forcing a perfect matching.
- **Pure upper rows with scalar cardinality maximization over independent sets.** The optimum is `r` if the formula is satisfiable and `r-1` otherwise. In the unsatisfiable case, a partial matching of size `r-1` is independent, while no complete matching is a base. Hence exact optimization decides ED11 without infeasible reference instances.

The equality and cover reductions also work for optional independent sets because every feasible set has full rank. All scalar costs can be zero in the feasibility versions.

The coefficient matrix has at most `T*m=O(nu^3)` entries. The ground, targets, and rank circuit have polynomial encoding length in `|phi|+nu`. Duplicate clauses can be removed if desired; there are only polynomially many distinct clauses of length at most three on `nu` variables. No sparse-formula assumption beyond the stated ETH consequence is needed.

## 6. Uniform density regimes and the dense endpoint

For any polynomial-time computable admissible choice `b=b(nu)` satisfying ED2, the reduction obeys ED6 with universal constant factors. A deterministic target solver with uniform time

$$
2^{o\left(T\log\left(2+m/T\right)\right)}\operatorname{poly}(H)
\tag{ED12}
$$

on these encoded instances would consequently solve 3-SAT in `2^{o(nu)} poly(|phi|)` time, contradicting deterministic ETH.

The range includes the following regimes.

**Constant density.** Fix `b=4`. Then `p_b=1`, `L=nu`, `T=4nu`, and `m=3T/2`. Thus even this fixed clique size rules out `2^{o(T)} poly(H)` under ETH.

**Intermediate densities.** Any admissible growing `b` gives `m/T=(b-1)/2` while preserving `T log(2+m/T)=Theta(nu)`. The constants in the calibration do not depend on `b`. This covers the whole polynomially constructible range between constant clique sizes and clique sizes of order `nu/log(nu+2)`.

**One dense clique.** Choose the smallest even `b>=4` with `A_b>=2^nu`. Then `p_b>=nu`, so `L=1` and `T=b`. Minimality gives

$$
A_b<(b-1)2^\nu
\tag{ED13}
$$

apart from harmless constant initial cases. Thus `p_b<=nu+log_2(b-1)`, which satisfies ED2 for all sufficiently large `nu`. Also `b log b=Theta(nu)`. This yields `m=T(T-1)/2` and rules out `2^{o(T log T)} poly(H)` on the dense encoded family.

These are uniform reductions across parameterized subfamilies. They do not assert hardness for every exact prescribed pair `(T,m)`, nor do they specify a tight leading constant in the exponent.

## 7. A zero-overlap encoded endpoint

For completeness, the zero-overlap equality family can also carry an encoded ETH lower bound directly. Given `nu` variables, make one row per variable with four elements of coefficients `1,2,3,4` in that row and zero elsewhere. Give each row target five and set rank `2nu`.

The equality sets choose either `{1,4}` or `{2,3}` in every row. Their `2^nu` choices encode assignments without any arithmetic ranking. Admit a complete equality set as a base exactly when its assignment satisfies `phi`, and admit all other rank-sized sets. The forbidden equality family is pairwise nonadjacent, so the same augmentation and rank-decoder proof applies.

Here `T=5nu` and `m=0`. The coefficient data and rank circuit are polynomial-size. Thus deterministic ETH rules out `2^{o(T)} poly(H)` on zero-overlap equality instances as well. This endpoint uses coefficients up to four; the support-two positive-density families above use only unit coefficients and unit targets.

## 8. Comparison and representation boundaries

Together with the overlap-density upper theorem, ED12 supplies matching exponent order in the promised rank-program/rank-circuit model across the described density families. It is logically separate from the unconditional rank-query lower bound: explicit inspection is allowed here, and the lower bound uses ETH.

The deterministic and randomized assumptions are kept separate. Ordinary deterministic ETH does not by itself justify the same claim against bounded-error randomized algorithms.

The construction does not produce a matrix representation, graphic resource matroid, or another standard restricted representation. The complete graph is used to label target constraints and to rank a family of subsets; the resource matroid is the formula-dependent paving construction. No lower bound for ordinary graph matching follows.

Primary ETH reference: Impagliazzo, Paturi and Zane, *Which Problems Have Strongly Exponential Complexity?*, Journal of Computer and System Sciences 63 (2001), 512–530, DOI 10.1006/jcss.2001.1774:

<https://www.sciencedirect.com/science/article/pii/S002200000191774X>.

The general use of paving matroids to hide constrained bases has public antecedents, including Doron-Arad, Kulik and Shachnai:

<https://arxiv.org/html/2412.02217v2>.

This note gives the explicit product decoder and uniform density calibration for the stated numeric-target model. It makes no publication-priority claim.
