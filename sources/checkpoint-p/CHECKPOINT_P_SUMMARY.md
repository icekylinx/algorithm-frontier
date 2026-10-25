# Checkpoint P: unrelated allocation with an exact shared budget

**25 October 2026. English research checkpoint.**

This checkpoint continues the transfer program. It does not attempt to
lower the historical general-graph matching exponent. Its principal
advance over O is a complete joint-role theorem for arbitrary
player-type values, followed by an exact shared-budget extension that
pays both selected-player setup fees and assignment costs. The results
below have complete mathematical manuscripts and recorded internal
reviews. They are not claimed to have formal verification, external
peer review, or established publication priority.

## 1. Principal theorem: unrelated values, optional players, exact cost

Let P be an explicit ground of q nonloop candidate players. An actual
basis B of an original player matroid M must be selected. For each
resource type j, integer recipient counts x_j belong to P(f_j), where
f_j is an arbitrary normalized monotone integer submodular rank supplied
by a value oracle. Units may remain unused. Player p values a type-j
unit at an arbitrary nonnegative rational v_pj. Its assignment cost is
an arbitrary nonnegative rational c_pj, and selecting p costs sigma_p.
The original single budget must hold without violation:

    sum_(p in B) sigma_p + sum_(p in B,j) c_pj x_j(p) <= C.

The objective is max_B,x min_(p in B) sum_j v_pj x_j(p).
Zero-budget feasibility is checked first by a minimum-setup M-basis.
Let OPT be the integer optimum on feasible instances. Let H include
all binary data and all paid polynomial oracle, LP, and intersection
work; resource counts are never expanded into individual units.

For fixed rational R>1, put

    alpha = 1 - 1/R,
    Gamma(R) = R^R/(R-1)^(R-1),
    B(R) = 2 - 1/Gamma(R),
    E(q) = 2^{O(q log log(q+2)/log(q+2))}.

There is a deterministic algorithm returning an actual original basis
and integer allocation of value at least alpha*OPT/2, with exact
original budget, in time

    B(R)^q E(q) poly(H),

and polynomial workspace. This is a factor 2R/(R-1) guarantee. In
particular, every fixed rational eta>0 gives factor 2+eta and a fixed
base strictly below two, with R=(2+eta)/eta.

| Approximation factor | R | Whole-player exponential base |
| --- | ---: | ---: |
| 4 | 2 | 7/4 = 1.75 |
| 3 | 3 | 50/27 = 1.851851... |
| 5/2 | 5 | 5994/3125 = 1.91808 |
| 2+eta | (2+eta)/eta | 2-1/Gamma((2+eta)/eta) |
| exactly 2 | direct role enumeration | 2, without E(q) |

The exact-factor-two endpoint has time 2^q poly(H) and polynomial
space. No uniform base below two is proved for this endpoint on
arbitrary unrelated values.

### Why the broader model is valid

A type can be light for one player and heavy for another. The proof
therefore masks player-type pairs and retains a single shared resource
polytope in a joint LP. One simultaneous rounding preserves the budget,
the floor of each heavy player's total count, and each light player's
utility up to its largest light unit. Two independent copies of the
resource would be invalid and are not used.

The optional-basis shared-budget extension uses a zero-service M*
dummy available at every player. A dummy unit at p has signed
coefficient -sigma_p in an affine budget whose constant is the total
setup fee. The original setup fees and assignment costs remain
nonnegative. The entire canonical dummy complement of a protected
optimum survives every omission. After cost-preserving rounding, the
integral dummy support is independent in M*. Its complement contains
an original M-basis. Selecting that basis converts the affine
inequality into the actual original budget.

The signed dummy is auxiliary proof machinery. It does not assert a
theorem for arbitrary negative original costs, and it must not be
deleted as though it were a dispensable zero-valued original unit.

Main proofs:

- `unrelated_values_joint_role_near_two_allocation.md`.
- `unrelated_allocation_shared_setup_budget.md`.
- `exact_two_global_enumeration_unrelated_allocation.md`.
- `unrelated_joint_role_and_setup_root_audit.md`.

The first two have root review and two separate full independent
reviews. The exact endpoint has root and independent full review.

## 2. Sharper integer-quota tradeoffs

For each fixed integer d>=2 define

    R_d=(d+1)/(d-1),  A_d=Gamma(R_d),  B_d=2-1/A_d.

The following accepted results use the same whole-ground bound
B_d^q E(q) poly(H), with polynomial workspace. Their stated costs
or capacities are respected exactly unless the approximation is
explicitly on makespan.

| Model | Guarantee | Cost scope |
| --- | --- | --- |
| Optional original M-basis, one common unit value | At least ceil(K*/d) units per selected player | One shared setup and assignment budget |
| Compulsory players, unrelated pair values in {0,u,a} | Factor d | One exact assignment budget |
| Two intrinsic job sizes with recipient/job polymatroids | Makespan factor 2-1/d | No arbitrary assignment-budget extension claimed in this checkpoint |

For d=2, B_d=50/27: this gives exact factor two for the first two
allocation models and exact factor 3/2 for the stated scheduling
model. For d=3 the base is 7/4, giving allocation factor three and
scheduling factor 5/3. For d=4 it is
2-(108/3125)^(1/3), approximately 1.674270, giving factors four
and 7/4 respectively.

The optional one-value result also has direct time A_d^(q-r) poly(H),
where r is the original M-rank. Its minimum-setup restriction oracle
must return a basis attaining h(Q), because that same basis is paired
with the fractional count witness at residual budget C-h(Q).
The small-target unit gate uses pair weight sigma_p+c_pj, paying each
selected player's setup once. The high-target branch recovers an exact
integer quota by minimum-cost optimization on an integral face.

The unrelated two-valued theorem is compulsory-player. The usual
large dummy value would create a third value in an optional-player
instance, so that adapter is not a proof of the same exact-d bound.

Main proofs:

- `integer_quota_approximation_time_tradeoffs.md`.
- `unrelated_two_value_integer_tradeoffs.md`.
- `one_value_shared_setup_assignment_budget_tradeoff.md`.

## 3. A separate faster result from sparse actual separators

When every separator returned on the tested attaining set has support
at most w, a finite first-crossing recurrence can replace Gamma(R) by
a smaller beta(R,w). The proof includes an output-sensitive certificate
generator; it does not hide the old exponential enumeration cost.
The width promise is required on all relevant calls, including forced
seeds and inputs without a full feasible witness.

At R=2,w=3, beta is the golden ratio phi=(1+sqrt(5))/2. This gives an
explicit application with two common matroids, one exact selected-set
cost threshold, and nonnegative packing rows of support at most three:
capacity factor two is achievable in either

    phi^(q-r) poly(H)

or

    ((5-sqrt(5))/2)^q E(q) poly(H).

The global base is approximately 1.381966. This is a capacity-augmented
packing theorem. It is not the allocation theorem at that time base.
Sparse input rows do not by themselves prove sparse separators for a
projected allocation or flow region.

See `attained_set_sparse_separator_gap.md` and its full independent
audit.

## 4. Robust integer allocation: positive guarantee and exact obstruction

A common selected M-basis may be allocated resources separately in
each of an explicitly listed collection of scenarios. With common unit
value, scenario-specific recipient polymatroids, and one exact
assignment budget per scenario, intersection of fractional count
regions permits exact integer quota recovery separately in every
scenario on that same basis.

The accepted unconditional guarantee is floor(K*/2), and it strengthens
to ceil(K*/2) whenever K*>=2. Time is (27/4)^(q-r) poly(H) or
(50/27)^q E(q) poly(H), with polynomial space. A supplied actual
one-unit robust basis and its allocations fill the K*=1 case and give
a complete factor-two guarantee.

Without such a promise or certificate, a general finite-factor corank
algorithm cannot be inferred. An explicit Hitting Set reduction uses
zero costs, a uniform original player matroid, and one Boolean resource
per scenario with rank

    f_S(A)=|A minus S|+min(|A intersect S|,|S|-1).

The robust optimum is one exactly when the omitted players hit every
source set, and is zero otherwise. Therefore any finite multiplicative
algorithm in F(q-r) poly(H) time would imply FPT=W[2]. This is not a
lower bound on a whole-q exponential base. Separate scenario budgets
also do not contradict the following same-allocation obstruction.

Main proofs:

- `robust_unit_allocation_additive_and_promised_two.md`.
- `robust_unit_allocation_corank_obstruction.md`.

## 5. Many exact assignment budgets are a real boundary

With an input-sized number of independent exact assignment budgets on
one integer allocation, even one unit-valued player can encode Maximum
Independent Set: each graph vertex is a unit resource and each edge
imposes x_u+x_v<=1. The parameter q is one and its corank is zero.
Under the cited deterministic approximation hardness, a constant-factor
F(q) poly(H) extension would imply P=NP. Complete graphs also exhibit
an unconditional unbounded fractional gap.

This does not exclude a fixed two-budget theorem, relaxed budgets, or
multiple budgets imposed on different adaptive scenario allocations.
See `multiple_exact_assignment_budgets_obstruction.md` and its audit.

## 6. Public baselines and OpenAI scope

The source audit `unrelated_allocation_primary_baselines.md` records
direct primary-source checks, including:

- Jansen--Maack already gives a parameterized approximation scheme for
  ordinary unbudgeted unrelated allocation by the number of player
  types, and hence by the number of players. Its fixed-accuracy upper
  bound is of order 2^(O(q log q)) plus a polynomial. The present work
  is not the first constant-factor player-FPT approximation.
- Rohwedder--Rouhani--Wennmann, ICALP 2025, supplies public
  cost-preserving rounding background and a randomized polynomial
  O(log n) ordinary intrinsic-value budgeted allocation guarantee.
- Bamas--Li--Rohwedder, STOC 2026, gives a newer ordinary unrelated
  budgeted allocation result whose stated application is bicriteria:
  it allows budget augmentation. The current theorem keeps the budget
  exact and uses exponential time in the player count.
- The generic base 2-1/A comes from public monotone local search. The
  current complete polynomial-space streaming implementation and
  application-specific extension interfaces have separate proofs.
- The public OpenAI mathematics index was checked at index level.
  Its visible polymatroid-counting and unit-job scheduling entries are
  different stated tasks. No private baseline or indexed manuscript
  is presumed validated.

These comparisons distinguish approximation quality, input model,
representation, determinism and time. They do not establish uniform
dominance or exhaustive publication novelty.

## 7. What remains unresolved

The main open endpoint is exact factor two for arbitrary unrelated
values with a fixed global base below two independent of numerical
value gaps. The exact 2^q endpoint above bounds the current gap.
For the dense integer K=3 to weak quota two, the present generic
corank base remains 27/4 unless actual separator structure is proved.
General robust positive integer service has the stated low-quota
obstruction; structured scenarios require their own additional proof.
Several exact budgets on the same allocation and submodular utility
functions are not covered by the additive-utility theorem.

Checkpoint O's selected-flow, continuous robust-flow, global conversion
and earlier allocation results remain in the cumulative archive. Their
separate model qualifications remain in force. This snapshot contains
English research text and a hash manifest, without Lean, PDF, executable
code or experimental bundles.
