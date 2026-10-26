# Row-dependent weights defeat the largest-prefix-target parameter

**25 October 2026. Complete scope-boundary reduction; full internal mathematical reviews completed for checkpoint T.**

The common weight vector in the one-order and two-order prefix theorems is essential. If each row may use its own weights, exact integer feasibility is W[2]-hard parameterized by the largest target B, even under all of the following restrictions:

- every row is a covering requirement on the very same full-ground prefix of one order;
- every coefficient is either one or two;
- every column has the same full positive support, so the original support-pattern count is Q=1;
- the only resource is an explicitly represented uniform matroid;
- the separately optimized scalar is identically zero.

The claim holds for integer independent sets and for bases. It needs no additional scalar budget. It is parameterized computational hardness, not a rank-oracle hiding result or a quantitative ETH lower bound.

## 1. Source problem and harmless cases

Start from parameterized k-SetCover: a finite nonempty universe U, an explicitly given family of n sets S_1,...,S_n, and the question whether at most k of them cover U. The parameter is k.

The nontrivial reduction may assume

```math
1\le k\le n.
 \tag{RW1}
```

The excluded cases are polynomially decidable. An empty universe is a YES instance. With k=0, a nonempty universe is a NO instance. If n<k, the answer is determined by whether the union of all n sets covers U. If a many-one reduction must output a quota instance in these cases, use a constant YES or NO instance: one ground element and a rank-one uniform matroid, one full-prefix row of target two, and coefficient two for YES or one for NO. These constant outputs preserve a parameter bound depending only on k.

One may also preprocess an uncovered universe element as an immediate NO, but this is unnecessary for correctness. Duplicate sets are allowed as distinct selectable coordinates; no duplication or parameter-sized padding is required by the construction.

## 2. An explicit uniform resource and full-prefix rows

Create one resource coordinate for each input set. Use the rank-k uniform matroid M on this n-element ground, with explicit rank

```math
r_M(A)=\min\{k,|A|\}.
 \tag{RW2}
```

Give the ground any one linear order. For each universe element u, introduce a row on its full prefix E, with coefficients

```math
a_{u,S}=1+\mathbf1[u\in S]\in\{1,2\},
       \qquad
             \sum_{S\in E}a_{u,S}x_S\ge k+1.
 \tag{RW3}
```

Set the scalar objective to zero. No other numeric constraint is imposed. In particular the bound on the number of chosen sets comes from the uniform resource, not from an extra scalar side condition.

Every column is positive in every row. Because U is nonempty, all columns have the same nonempty support U. The parameter values are therefore

```math
Q=1,\qquad B=k+1.
 \tag{RW4}
```

The resource is fully explicit and easily evaluated. The matrix has n times |U| entries from a two-element alphabet, and all targets have O(log(k+1)) bits. Its size and construction time are polynomial in the explicit SetCover input.

## 3. Exact equivalence for integer independent sets

An integer vector in P(M) is the indicator of a subset I of sets, with |I|<=k. In row u its value is

```math
\sum_{S\in I}a_{u,S}
           =|I|+|\{S\in I:u\in S\}|.
 \tag{RW5}
```

If I satisfies RW3, then for every u,

```math
|\{S\in I:u\in S\}|
                       \ge k+1-|I|\ge1.
 \tag{RW6}
```

Thus the selected family I is a cover using at most k sets.

Conversely, suppose I_0 is a cover with |I_0|<=k. Since n>=k, extend it by arbitrary additional distinct set coordinates to a set I of exactly k coordinates. Its cover property remains true. Every row value in RW5 is then at least k+1, so I is feasible for the quota instance.

Consequently

```math
\text{SetCover has a cover of size at most k}
 \quad\Longleftrightarrow\quad
 \text{RW3 is feasible over the integer points of P(M)}.
 \tag{RW7}
```

The integrality qualifier matters: this is not a claim that fractional feasibility solves SetCover.

## 4. Bases and the parameter consequence

The forward construction in Section 3 already produces exactly k selected coordinates, hence a base of M. Conversely every feasible base is an independent set, and RW6 extracts a cover. Therefore the equivalence also holds over B(M).

The reduction maps k to B=k+1 on every nontrivial instance. Exact k-SetCover is W[2]-hard, so exact feasibility in either quota formulation is W[2]-hard parameterized by B. In particular, unless FPT=W[2], there is no algorithm with running time

```math
f(B)\mathrm{poly}(H)
 \tag{RW8}
```

for any computable f on this row-dependent-weight class. Since rank(M)=k and Q=1, adding the uniform rank and support-pattern count to the parameter does not remove this conclusion.

This is not hardness for a fixed constant B: for each fixed k the usual subset enumeration is polynomial with an exponent depending on k. Nor is a time lower bound such as 2^{Omega(B)} or n^{Omega(B)} being inferred from W[2]-hardness alone.

## 5. Why this does not contradict the positive prefix or support results

Every row in RW3 has the same endpoint, but its weight vector depends on u. A coordinate may carry coefficient one in one row and two in another. There need not be a single v_S for which its auxiliary column is v_S times its support indicator. The common-weight factorization used in [exact-weighted-prefix-quotas-max-target.md](exact-weighted-prefix-quotas-max-target.md) and [two-order-weighted-prefix-target-classification.md](two-order-weighted-prefix-target-classification.md) is therefore absent.

Likewise the dominance rule for repeated prefix endpoints requires a common cumulative weight functional. It cannot discard the universe rows here merely because their endpoints and targets agree.

The original-support theorem is parameterized by the sum of numeric targets, not just their maximum. In this construction that sum is (k+1)|U|, which is not bounded by a function of k. Its Q=1 singly exponential total-target upper bound is fully consistent with RW8.

No approximation-hardness statement for relaxed quota satisfaction is proved here. The zero scalar is used only to show that infeasibility detection already contains the obstruction. No black-box rank-query or quantitative ETH conclusion is asserted.

## 6. Checked primary source and attribution

Bingkai Lin, Xuandi Ren, Yican Sun and Xiuhan Wang, *Constant Approximating Parameterized k-SetCover is W[2]-hard*, arXiv:2202.04377v2, 23 October 2022. The Introduction explicitly records the standard W[2]-completeness of exact k-SetCover; Theorem 1 proves the stronger obstruction to constant-ratio FPT approximation under FPT!=W[2]. Only the exact decision hardness is used above.

<https://arxiv.org/html/2202.04377v2>

<https://arxiv.org/abs/2202.04377v2>

The primary abstract, Introduction and Theorem 1 were directly checked for this note. The reduction is a scope clarification for the shared-weight prefix theorems; it makes no priority claim for SetCover hardness or for general covering formulations.
