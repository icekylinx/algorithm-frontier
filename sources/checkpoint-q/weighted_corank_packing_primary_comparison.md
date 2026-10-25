# Bounded primary-source comparison for weighted corank packing

**25 October 2026. Public comparison for WP1--WP16; not an exhaustive novelty review.**

The reviewed project theorem is
`corank_weighted_prefix_free_batching.md`: an exact restriction
selector for a family of r-element subsets, together with a
nonnegative weighted packing separator, yields a deterministic
t-versus-b gap algorithm in Gamma(t/(t-b))^(q-r) poly(H) time.
Its augmentation specialization preserves membership in that
family exactly and permits capacity factor 1+epsilon. A cost
threshold in the selector preserves cost against the original
integer optimum.

The checked public results below already provide broad resource
augmentation and exponential approximation methods. The proper
comparison concerns the parameter and oracle interface. In
particular, coefficient-independent running time under resource
augmentation is not, by itself, a new claim of this project.

## 1. Integer programming with resource augmentation

**Primary source.** Hauke Brinkop, Hua Chen, Lin Chen, Klaus
Jansen and Guochuan Zhang, *Approximation Algorithms for Integer
Programming with Resource Augmentation*, STACS 2026, Theorem 1.
[Published paper](https://drops.dagstuhl.de/storage/00lipics/lipics-vol364-stacs2026/LIPIcs.STACS.2026.20/LIPIcs.STACS.2026.20.pdf)
and [publisher record](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.STACS.2026.20).

For an integer program with m constraint rows, their theorem has
time f(m,epsilon) poly(input length), preserves the objective
against the exact optimum, and permits infinity-norm equality
error epsilon*Delta, where Delta is the largest absolute matrix
entry. The displayed bound is 2^((m/epsilon)^{O(m)}) times a
polynomial. Their applications include multidimensional knapsack
with resource augmentation.

**Comparison.** This is a genuinely relevant coefficient-independent
approximation result. Its parameter is the number of explicit
rows, with additional block-structure results in the paper. WP
uses the number q-r of omitted elements and a possibly implicit
row separator. It also preserves an abstract selection family
exactly. General-IP equality error and packing capacity inflation
are not identical interfaces, although normalization relates
them in suitable packing instances. Neither theorem uniformly
dominates the other as stated.

## 2. Adding many budgets to a packing dynamic program

**Primary source.** Alexander Armbruster, Fabrizio Grandoni,
Antoine Tinguely and Andreas Wiese, *Augmenting Packing Dynamic
Programs to Handle (Many) Additional Budget Constraints*, SODA
2026, Theorems 1.1, 1.2 and 1.5.
[Author-hosted paper](https://people.idsia.ch/~grandoni/Pubblicazioni/AGTW26soda.pdf).

Given an exact packing dynamic program, their randomized framework
adds M cardinality or budget constraints. Theorem 1.5 handles
budget rows under small-coefficient assumptions or resource
augmentation, with an additional 1+epsilon objective approximation.
The general displayed runtime is
(log(Mn)/epsilon)^{O(M)}(n T(input length))^{O(1)}, with stronger
variants for unary dynamic programs. This is fixed-parameter
approximation in M and epsilon when the supplied DP is polynomial.

**Comparison.** Their structural interface is a packing DP; WP
requires a restriction selector and a separating row. Their
nonlinear parameter counts added constraints; WP counts omitted
elements. Exact fixed-cardinality selection and cost at most
integer OPT in the common-basis application are different from
the DP framework's profit approximation. This difference supports
a separate statement, not a claim that WP supersedes their
results for unrestricted DP-solvable packing problems.

## 3. Weighted approximate monotone local search

**Primary source.** Baris Can Esmer, Ariel Kulik, Daniel Marx,
Daniel Neuen and Roohani Sharma, *Approximate Monotone Local Search
for Weighted Problems*, Algorithmica 88, article 59 (2026),
Theorem 2.8. The publisher records publication on 18 August 2026.
[Publisher full text](https://link.springer.com/article/10.1007/s00453-026-01402-7).

The theorem converts an assumed parameterized approximate extension
oracle into a deterministic approximation algorithm with time
amls(alpha,c,beta)^{n+o(n)} on an n-element weighted universe.
It studies monotone subset minimization and approximation of
objective weight. The parameterized extension routine is an
input to the framework.

**Comparison.** This is a relevant general framework for turning
parameterized algorithms into whole-universe exponential algorithms.
Its theorem does not directly supply WP's required extension/gap
routine for arbitrary weighted packing and an exact selector.
The word "weighted" also refers to objective weights there,
whereas the WP refinement concerns coefficients in packing rows.
The exact-selector corank statement and its first-crossing branch
bound require their own argument. No reduction establishing
subsumption in either direction was verified in this bounded pass.

## 4. Why deletion, covering, and packing slack are not interchangeable

**Primary nearby result.** Andres Cristi, Mathieu Mari and Andreas
Wiese, *Fixed-Parameter Algorithms for Unsplittable Flow Cover*,
STACS 2020.
[Publisher paper record](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.STACS.2020.42).
The paper treats minimum-cardinality path tasks covering edge
demands. Its primary abstract reports fixed-parameter tractability
with slight demand violation, and a parameterized approximation
scheme allowing a small factor more tasks. This is a genuine
solution-cardinality resource-augmentation precedent with a
special path structure.

The following comparison is a direct algebraic observation. For
a packing row with total weight W and capacity u, deleting a set
D is equivalent to covering weight at least W-u. Inflating the
packing capacity to (1+epsilon)u changes this demand to

\[
                         W-u-\epsilon u.
\]

It does not change it to (1-epsilon)(W-u). These losses can differ
greatly when u and W-u have different scales. Thus passing to
the omitted set does not automatically identify WP with a
relative-demand covering theorem. An arbitrary exact selection
family also adds constraints absent from unrestricted deletion.

## 5. Knapsack parameterization and strict-budget hardness

Two additional primary references were checked as context, without
treating them as direct matches:

* Albrecht, Gurski, Rethmann and Yilmaz, [Knapsack Problems: A
  Parameterized Point of View](https://arxiv.org/abs/1611.07724).
  Its stated parameter study includes item count, profit threshold,
  sizes, profits, dimensions and number of knapsacks. The inspected
  statement does not establish the precise omitted-element
  augmentation theorem considered here.
* Doron-Arad, Kulik and Manurangsi, [On the PTAS Complexity of
  Multidimensional Knapsack, ITCS 2026](https://drops.dagstuhl.de/storage/00lipics/lipics-vol362-itcs2026/html/LIPIcs.ITCS.2026.50/LIPIcs.ITCS.2026.50.html).
  This is an ETH-based near-tight time lower bound for profit
  approximation as a function of dimension and accuracy while
  respecting budgets. It does not contradict changing both the
  parameter to q-r and the feasibility requirement to capacity
  augmentation.

Searches included corank/co-rank, number of rejected or excluded
items, dual-parameter multidimensional knapsack, approximate
monotone local search, and parameterized covering/resource
augmentation. These searches returned the adjacent sources above,
but did not produce a checked primary theorem identical to WP.
This is a report of a limited search, not evidence that no such
result exists elsewhere.

## 6. Safe comparison wording for the research checkpoint

The supported statement is:

> The internally proved weighted packing theorem has deterministic
> Gamma(t/(t-b))^c dependence on the number c of omitted elements,
> with an exact restriction selector and polynomial-bit violated
> nonnegative rows. The checked public augmentation frameworks use
> different structural interfaces or parameters. A first-publication
> claim is not made.

The quoted paragraph is original checkpoint wording, not an
excerpt from any source. It keeps the result concrete while
avoiding claims that coefficient-independent approximation,
resource augmentation, or parameterized approximation are new
concepts introduced by this work.

This comparison complements, rather than replaces, the separate
mathematical audit `corank_weighted_prefix_free_independent_audit.md`.
