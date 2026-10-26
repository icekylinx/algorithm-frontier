# Singly exponential target lower bounds with one full support pattern

**25 October 2026. Complete new oracle and encoded-input constructions; root and independent full mathematical reviews passed.**

One original nonempty support pattern does not make exact mixed-target optimization polynomial. Even when every coefficient column is positive in every target row, with entries only one or two, the problem can require `2^{Omega(T)}` rank queries. A separate polynomial-size rank-program/circuit reduction gives the corresponding `2^{o(T)}` exclusion under deterministic ETH.

The construction has polynomially many ground elements in the numeric target. Its encoded version ranks subsets of complementary-pair identifiers, avoiding the need to rank all balanced subsets of a hypercube. This supplies a sharp endpoint for a singly exponential upper bound at original support-pattern count `Q=1`.

## 1. Positive hypercube labels and target sizes

Choose a positive integer `h` and put

```math
r=2^h,
\qquad d=2h,
\qquad E=\{1,2\}^{d},
\qquad n=|E|=r^2.
\tag{OS1}
```

The resource will be an ordinary rank-`r` matroid on this explicit ground. For each coordinate `j=1,...,d`, give element `u` the row coefficient `u_j` and target `3r/2`. Add a cardinality row whose coefficient is one on every element and whose target is `r`. All rows are equalities.

Every coefficient is one or two, and every column has exactly the same full nonempty support. Thus the number of original support patterns is

```math
Q=1.
\tag{OS2}
```

The total numeric target is

```math
T=r+d\frac{3r}{2}=r(3h+1)=\Theta(r\log(r+2)).
\tag{OS3}
```

The cardinality row is redundant for bases but makes the optional independent-set version equivalent as well. It retains `Q=1` and changes the target sum only by `r`.

Let `H` be all rank-sized subsets whose vector sum in the first `d` rows is the constant vector `(3r/2,...,3r/2)`. These are exactly the sets satisfying all equalities. Two different members of `H` are not one-exchange neighbors: replacing one distinct hypercube label by another changes at least one row sum.

## 2. An explicitly countable large balanced subfamily

Pair each label `u` with its coordinatewise complement `bar u=3-u`. There are

```math
M=n/2=r^2/2
\tag{OS4}
```

disjoint complementary pairs. Let `G` consist of the unions of exactly `k=r/2` such pairs. Every member has size `r`, and each pair contributes three in every label coordinate. Hence

```math
G\subseteq H,
\qquad
N=|G|=\binom{r^2/2}{r/2}.
\tag{OS5}
```

Elementary binomial bounds give

```math
r^{r/2}\le N\le(r^2/2)^{r/2}\le r^r.
\tag{OS6}
```

For the lower estimate, write the binomial coefficient as a product of `k` ratios `(M-i)/(k-i)`, each at least `M/k=r`. Therefore

```math
\frac{rh}{2}\le\log_2N\le rh,
\qquad
N=2^{\Theta(T)}.
\tag{OS7}
```

In fact the lower estimate and OS3 imply `N>=2^{T/8}`, since `h>=1`.

The explicit ground and row matrix have size polynomial in `T`: there are `r^2` elements and `2h+1` rows. This avoids a lower bound whose apparent exponential factor could be absorbed by a large explicit input.

## 3. Valid reference and hidden matroids

Define the reference independent sets by permitting every subset smaller than `r` and making a rank-sized set a basis precisely when it is not in `H`. For each hidden `A in G`, additionally permit `A` as a basis.

More generally, forbidding any subfamily of `H` defines a matroid in this manner. Heredity is immediate. The only nontrivial augmentation case compares an independent `(r-1)`-set with an independent `r`-set. If there is only one possible added element, the result is the known larger independent set. If there are two or more, the resulting rank-sized sets are one-exchange neighbors, so at most one is forbidden. At least one augmentation is allowed.

The rank is really `r`: there are `r` distinct labels with first coordinate one, because `r^2/2>=r`. Their first-coordinate sum is `r`, so they are outside `H` and form a reference base.

The reference and hidden rank oracles differ only on the hidden set `A`. Smaller sets have their cardinality as rank. A larger set contains two adjacent rank-sized subsets and therefore a base in every instance. At rank, only the permitted status of `A` changes.

The reference target instance is infeasible. The hidden instance has exactly `A` as a feasible set. This holds over both bases and independent sets because the cardinality equality forces full rank. All scalar weights may be zero.

On a reference transcript, `Q_alg` queries can hit at most that many candidates in `G`. Under the balanced distribution consisting of the reference instance and a uniformly chosen hidden instance, decision success is at most `1/2+Q_alg/(2N)`. Success at least `2/3` on every input requires

```math
Q_{\rm alg}\ge N/3=2^{\Omega(T)}.
\tag{OS8}
```

This is an unconditional rank-oracle lower bound. It already holds at original support-pattern count one and with nonnegative coefficient magnitudes bounded by two.

## 4. Choosing a polynomial-size encoding for a SAT instance

Let `phi` be a 3-CNF formula with `nu>=1` variables. Choose the smallest power of two `r>=2` such that

```math
N(r)=\binom{r^2/2}{r/2}\ge2^{\nu}.
\tag{OS9}
```

Compute it by successive doubling and exact binomial arithmetic. Let `h=log_2r` and use OS1–OS3.

The power-of-two jumps preserve constant-factor calibration. From OS7 and OS9,

```math
\nu\le\log_2N(r)\le rh.
\tag{OS10}
```

If `r>2`, minimality gives `N(r/2)<2^nu`. Its lower bound from OS7 gives

```math
\frac r4(h-1)<\nu.
\tag{OS11}
```

For `h>=2`, `3h+1<=7(h-1)`. Consequently

```math
T=r(3h+1)<28\nu.
\tag{OS12}
```

Together with OS10 and the constant `r=2` case, this proves

```math
T=\Theta(\nu),\qquad
r=O(\nu),\qquad
n=r^2=O(\nu^2).
\tag{OS13}
```

Stored binomial counts have `O(rh)=O(nu)` bits. The number of doubling stages, the final ground, and all row descriptions are polynomial in `nu`. Exact binomial values can be computed by the usual multiplicative recurrence, with no enumeration of subsets.

## 5. Complementary-pair identifiers and subset ranking

Every complementary pair has a unique representative whose first coordinate is one. Interpret its remaining `d-1` entries, after subtracting one, as a binary identifier in `0,...,M-1`, where `M=r^2/2`.

A query subset belongs to `G` exactly when it consists of `k=r/2` complete complementary pairs. Pair closure and the selected identifier set can be checked in polynomial time on the explicit subset indicator. Such a set is automatically balanced and belongs to `H`.

Order the `k`-subsets of `[0,M-1]` lexicographically. For identifiers
`a_1<...<a_k`, their zero-based rank is computed by, at position `i`, summing

```math
\binom{M-x-1}{k-i}
\tag{OS14}
```

over each skipped candidate `x` between the previous chosen identifier and `a_i`. This counts exactly the suffix choices for that alternative first differing identifier. The rank lies in `0,...,N(r)-1`.

The inverse chooses the next identifier by these suffix bucket sizes, subtracting skipped buckets and then recursing on the remainder. This proves a ranking/unranking bijection and uses polynomially many arithmetic operations on polynomial-bit integers. Even a direct loop over all possible identifiers is polynomial because `M=O(nu^2)`.

Decode a member of `G` into the `nu` assignment bits of its lexicographic rank modulo `2^nu`. This map is surjective: the first `2^nu` ranks already encode every assignment. Formula evaluation on these bits is polynomial time.

## 6. A rank program or circuit valid for every formula

Let `H_phi` contain all balanced sets in `H\G`, together with those sets in `G` whose decoded assignment does not satisfy `phi`. Define `M_phi` to permit all subsets smaller than `r` and every rank-sized set outside `H_phi`.

The forbidden family is a subfamily of the stable family `H`. Section 3 therefore proves that `M_phi` is a matroid for every formula, irrespective of satisfiability. Nonbalanced rank-sized sets give the same fixed rank `r` in every instance.

Its rank on an explicit query subset `S` is computed as follows:

- If `|S|<r`, return `|S|`.
- If `|S|>r`, return `r`.
- If `|S|=r` and its label sums are not the balanced target vector, return `r`.
- If it is balanced but not a union of complete complementary pairs, return `r-1`.
- Otherwise compute its identifier-subset rank, decode the assignment modulo `2^nu`, and return `r` if the formula accepts and `r-1` otherwise.

The larger-set branch is correct because two adjacent rank-sized subsets cannot both be forbidden. Every remaining branch uses explicit row sums, pair membership, binomial suffix counts, and evaluation of one specified assignment. It takes polynomial time and polynomial workspace in the formula and constructed input size.

The loops are polynomially bounded and all arithmetic values have polynomial bit length. The decoder can therefore be compiled uniformly into a Boolean circuit of polynomial size computing the rank in binary. This is a promised rank-circuit representation; the matroid promise has just been proved, and recognizing arbitrary rank circuits is not an added task.

No uniqueness assumption on satisfying assignments is needed. The program is allowed to admit any subset of `G` selected by the formula, while always rejecting `H\G`.

## 7. Exact feasibility and the ETH consequence

A set meeting the target equalities belongs to `H`. Among those sets, the resource matroid accepts exactly the members of `G` whose decoded assignments satisfy `phi`. Surjectivity of the rank decoder therefore proves

```math
\text{target feasibility in }M_\phi
\quad\Longleftrightarrow\quad
\phi\text{ is satisfiable}.
\tag{OS15}
```

The full input, including the rank circuit and coefficient matrix, has size polynomial in `|phi|+nu`. By OS13, a deterministic algorithm for these encoded instances with running time

```math
2^{o(T)}\mathrm{poly}(H)
\tag{OS16}
```

would solve 3-SAT in `2^{o(nu)} poly(|phi|)` time. Deterministic ETH excludes such an algorithm. The corresponding randomized statement requires randomized ETH separately.

An algorithm may read and exploit the entire rank-program or circuit description, including the embedded formula. This lower bound still follows from the polynomial reduction. It is not an assertion that the formula remains hidden from the algorithm.

The result is for the stated rank-program/circuit representation. It does not provide a matrix, a graphic representation, or another standard restricted representation of the resource matroid, and does not establish hardness in those models.

## 8. Interpretation and attribution

The original support-pattern count is one, while the number of rows grows logarithmically with the matroid rank. This is distinct from the disjoint-row endpoint, which has one support pattern for each row. All coefficients here are positive, so sparse row incidence is not the source of the lower bound.

The oracle lower bound and the encoded ETH lower bound are separate statements. The first is unconditional information complexity; the second permits full input inspection and uses a computational hypothesis. Both prove the singly exponential target order at this endpoint, not a leading constant or a more general accuracy lower bound.

Public antecedents for hiding constrained bases in paving matroids include Doron-Arad, Kulik and Shachnai:

<https://arxiv.org/html/2412.02217v2>.

The ETH reference is Impagliazzo, Paturi and Zane, *Which Problems Have Strongly Exponential Complexity?*, Journal of Computer and System Sciences 63 (2001), 512–530:

<https://www.sciencedirect.com/science/article/pii/S002200000191774X>.

The complementary-pair family, its target calibration, and its explicit decoder are proved here. No publication-priority claim is made.
