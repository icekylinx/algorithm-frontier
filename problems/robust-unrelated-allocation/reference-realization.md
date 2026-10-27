# Exact common-basis reference for robust unrelated allocation

The [reference backend](reference/robust.py) executes the original robust
model using the [shared exact LP and rounding core](../unrelated-values-joint-role/reference-realization.md).
It keeps an actual common player basis and independent scenario allocations.
Its finite LP cost is separate from the paid polynomial primitives in the
[canonical theorem](proof.md).

## 1. Model and canonical outputs

`Robust(player_rank, scenarios, setup=None)` accepts a nonempty explicit
scenario list. A scenario is `(resource_ranks, values, costs, budget)` with
complete original recipient-rank tables and type-major exact nonnegative
rational values and costs. Scenario type counts, values, ranks, assignment
costs and budgets may differ. The one setup vector belongs to the common
selected basis and is identical in all scenarios. Every original table and
numeric input is validated through the native joint constructor.

`Allocation(basis, scenarios)` stores one original basis and one integer
type-major original count array per scenario. `verify` checks every original
rank inequality, zero counts outside that basis and the actual combined
setup/assignment budget in each scenario. Strict canonical record types
prevent a duck object from overriding computed utility. No LP, selector,
rounding or target search is used by verification. Original labels are kept,
including loops; the fast theorem may preprocess them when defining its
nonloop parameter. Empty scenario lists are rejected. Rank zero returns the
empty basis with utility `None` as an explicit software convention.

## 2. Actual common setup and changing regions

**Lemma 1.** `zero` decides original common-basis zero-utility feasibility;
`gap` is a sound full-target/weak-success common-basis oracle.

**Proof.** Greedy weighted matroid optimization minimizes the common setup
sum and returns an actual basis. It meets all zero-allocation budgets exactly
when that minimum is no larger than every scenario budget. Nonnegative
original assignment costs prove the converse.

At a recursion node, greedy is repeated inside the current allowed ground.
Failure to obtain original rank rejects the node. The attaining current
basis is also rejected if its setup exceeds any scenario budget. Each
scenario region subtracts the setup sum of that same basis and retains every
original resource and owner. It does not contract physical resources or
remove positive pairs merely because a whole unit would be expensive.

The shared exact support routine queries weak service on the full current
ground. The first failed scenario supplies its valid nonnegative row.
The region always contains zero at these nonnegative residual budgets, so
no empty-region outer support problem arises. A successful query serves the
actual current basis in every scenario after discarding outside counts.

Fix any full-target common basis still in the allowed ground. Current
minimum setup is at most this fixed basis's setup, so its original
fractional allocations remain feasible in every residual scenario region.
The same protected basis therefore supplies the omitted-mass inequality for
each failed row, even if the scenario changes from one node to the next.
The actual canonical first-crossing DFS keeps one protected branch. At zero
deficit its weak query must succeed. Rank and affordability gates also
cannot reject that protected branch. Thus complete failure excludes every
original full-target common basis, proving the lemma.

`forced` seeds use the original ground and the same invariant. A supplied
admissible rational `global_base` is checked by the exact Gamma power
identity, then invokes the canonical streamed logarithmic-block cover. It
does not replace this actual extension with exhaustive basis enumeration.

## 3. Original fractional comparator and rational target search

**Lemma 2.** `fractional(basis)` computes the original common-basis fractional
value and witnesses, and `optimize` attains the requested full fractional
accuracy before integer rounding.

**Proof.** After fixing the actual basis, subtract its actual setup and set
all outside assignment variables to zero. For each scenario, solve the
original resource/cost LP maximizing uniform service on the basis. Independent
scenario allocations imply that the common value is the minimum of these
individual maxima. No fractional mixture or scenario-dependent basis is
used. Different witnesses may give larger service in some scenarios; all
meet the common minimum.

For rational search, the fixed family consists precisely of actual bases
whose common setup fits every budget. The joint LP has one common service
coordinate and at most `rank*sum(number_of_types)` assignment coordinates
after zero-coordinate elimination. Original row data and every possible
subset setup sum have a uniform bit bound. In `denominator_bound`, the
maximum original numerator/denominator bit length is enlarged by a factor
`q+2`, plus slack, to cover a sum of up to `q` rational setup fees and its
subtraction from a budget. Rowwise denominator clearing and the determinant
bound then give the returned `factorial(n)*2**((n+2)*L*n)` denominator bound.
The LP need not add the redundant explicit utility upper-bound row, so this
bound does not require encoding that row's summed value.

The original data give a finite service upper bound from each scenario's
total rank and largest type values, taking the minimum over scenarios.
If this bound is zero, returning the legal initializer is sufficient.
Otherwise the canonical full-accuracy rational search calls Lemma 1, saves
its actual basis on a weak success and lowers the upper endpoint only on
full-target failure. Its fixed-family denominator separation proves that
original reoptimization on the saved basis reaches the full requested
fractional accuracy. No monotonicity of weak successes, positive lower scale
or repeated division of the accuracy is required. This proves the lemma.

## 4. Scenario recovery and model boundaries

**Theorem.** `optimize` returns an original feasible common basis allocation
with the canonical per-player, per-scenario additive guarantee.

**Proof.** Fix the actual basis from Lemma 2 before any scenario rounding.
In each scenario, `recover` restricts real coordinates to this same basis
and calls the original-resource signed-cost prefix routine with that
scenario's nonnegative assignment objective. Its feasible fractional input
is the original reoptimized witness. The reduced integral prefix face
preserves all count floors and loses at most the largest originally eligible
unit at each selected owner, without increasing the scenario assignment
cost. Adding back the fixed original setup sum preserves its exact budget.
Lemmas 1–2 provide the canonical fractional accuracy, and nonnegative
utility gives the maximum with zero. This proves the theorem.

This proof rounds neither a common fractional dummy nor a common role mask.
Assignments adapt independently to the explicitly listed scenarios after
one actual basis is fixed. The common-role and common-dummy counterexamples
in the [boundary manuscript](../../manuscripts/mechanism-boundaries/robust-unrelated-common-role-obstructions.md)
therefore remain valid and do not contradict this additive result.
Arbitrary scenario setup vectors, multiple integer assignment budgets in
one scenario, or one common integer allocation are not supplied interfaces.

## 5. Charged reference cost

For every local LP, the shared core streams at most `binom(N,d)` active
square systems for `N` rows and `d` active variables. A service objective
adds one variable. The outer support LP temporarily stores all distinct
projected service vertices, which may take exponential memory. Rounding
similarly streams active bases of its integral prefix face. Table validation,
all rational arithmetic, stored support vectors, exact Gamma power
comparisons and output bits are charged. No loop runs once per supplied unit
or once per numeric value of a rank or budget.

The reference therefore exercises the actual omission, common setup,
fixed-family rational search and scenario recovery. Its local finite LP
cost and potentially exponential support storage are separate from the
canonical theorem's polynomial LP/intersection implementation and workspace.
The mathematical proof of those fast primitives and the streamed-cover
bound is unchanged.

**Attribution:** Yilin Liu and GPT-6 Astra Pro. **License:** Apache-2.0.
