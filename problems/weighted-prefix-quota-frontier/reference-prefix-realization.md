# Native exact one-order prefix quotas and signed recovery

This note proves the original-input contract of the
[reference client](reference/README.md). Its complete mathematical source is
the [one-common-order companion](manuscripts/exact-weighted-prefix-quotas-max-target.md),
including the largest-target profile count and the separately stated oracle
and encoded-program lower bounds. The other orders, weight families, laminar
catalogues and ground reductions retain their separate scopes.

## 1. Original model and exact safe preparation

Input is one complete normalized monotone integral submodular rank table on
an explicit ordered coordinate ground. Counts are integral independent
vectors, or mandatory bases at the original full rank. There is one common
nonnegative integer weight per coordinate, exact mixed prefix quotas with
nonnegative integer targets, one arbitrary signed rational scalar objective,
and optional original eligibility restrictions. The largest listed target is
called `B`, or zero if there are no rows. Resource ranks, weights, targets and
counts keep their binary encodings.

Split each equality into its upper and lower half. At duplicate endpoints
retain the smallest upper target and largest lower target. Positive lower
demand on an empty prefix is immediately impossible. A coordinate whose
original positive weight exceeds any upper target containing it cannot be
used by an integer solution. Mask it, including the zero-upper case. This
uses the original weight, never a capped credited weight. It is safe even
when that upper row will later be removed as redundant. A large weight in
lower rows alone is retained.

Upper suffix-record minima and lower prefix-record maxima are equivalent to
the original quota systems because true weighted prefix values are
nondecreasing. Remove zero lower demands and now automatic zero upper rows.
Each remaining family has positive targets strictly increasing along the
order, so each has at most `B` rows. The implementation stores only original
rows and actual record endpoints, without a target-indexed array.

Mandatory masks retain the original required total. If the resource rank of
all retained original coordinates is smaller, reject; replacing the total by
that smaller rank would change the problem. Optional mode instead adds a
single internal zero-weight, zero-cost disposal coordinate. Its rank equals
the original rank on sets without disposal and the original full total on
sets containing disposal. Thus any original independent vector extends by
its unused mass to a base at the original total. Real zero-weight coordinates
keep their original signed costs and are never replaced by disposal.

## 2. Shared copying, credit and occupied classes

Every retained positive coordinate has one passive and, if there are lower
rows, one active coordinate. A zero-weight coordinate needs only its passive
coordinate. Optional disposal also has just one passive coordinate. Both
copies of a real coordinate retain its full original scalar coefficient.
They share one original resource rank through aggregation, rather than each
receiving an independent resource capacity.

For credit the copied weight is `min(original_weight, B)`. An upper row uses
this weight on both copies. It equals the original weight on every incident
eligible coordinate, by the upper mask. A lower row credits only the active
copy. Its capped value is no larger than the original true value. Therefore
every integer lifted solution satisfying its auxiliary rows projects to an
original feasible count vector with the same scalar, eligibility and required
resource total.

Each nonzero auxiliary column is one positive magnitude times the incidence
vector of its row support. Group together the copies with the same actual
support and magnitude. Keep one additional zero-column group. That group
includes real zero-weight coordinates, disposal and any passive or other
unconstrained copies with empty auxiliary support; all their real scalar
costs remain present. Only occupied classes among the at most twice-original
number of coordinates are stored.

The companion's fixed-order support argument gives at most `3*B` actual
nonempty row-support colors. Distinct magnitudes on one color remain distinct
classes. No hypothetical table with a slot for every target, color or
magnitude is allocated.

## 3. Every original integer witness has a charged profile

Fix any original feasible vector and, in optional mode, its legitimate
disposal completion. Let `C` be the largest retained lower target, or zero
when no lower rows remain. Conceptually scan positive units in the common
coordinate order using capped weights and mark through the first unit
reaching `C`. With no lower rows, mark nothing.

Capping preserves every integer lower target at most `B`: a unit of original
weight at least `B` reaches any such target by itself; otherwise its weight
is unchanged. Thus the marked prefix exists when required and its mass is
between `C` and `C+B-1`. Every lower prefix either contains the cut and gets
all marked credit, or precedes it and retains all its original capped units.
All lower rows are satisfied.

If the marked cut is inside the last upper prefix, all nonzero auxiliary
copies lie there and their mass is at most `B`. If it is after that prefix,
every unit of the latter is marked, so all nonzero auxiliary mass is in the
marked units. Passive copies outside all upper prefixes are zero columns.
This proves the exact profile contract used by the implementation:

```text
L = B + max(C-1, 0)
sum_g magnitude[g]*profile[g] <= L
sum_g profile[g] <= original_total
zero_remainder = original_total - sum_g profile[g].
```

The no-upper and no-lower cases follow by the same argument. When `B=0`,
preparation leaves no nonzero auxiliary column and there is one zero profile.
The marking proof is conceptual; neither the client nor its LP constructs
the resource units or the chronological unit sequence. The checker also
implements marking by binary bulk arithmetic on its supplied original vector.

Every original feasible scalar value is consequently represented by some
charged profile. The profile's later optimizer may choose different marking
bits: credited feasibility already implies original feasibility, so such
freedom is safe.

## 4. Exact original-ground LP for a fixed profile

Let each native nonnegative variable correspond to one actual active/passive
coordinate or disposal. For every original subset, impose the original rank
bound on the sum of all copies whose original owner lies in that subset.
Impose the original total as a global upper cap. For optional mode, disposal
has coefficient zero in original subset rows and coefficient one in that
global total row. Finally, impose each nonzero class's profile count as its
upper cap and the zero-column group's remainder as its cap.

These are exactly the independent-region inequalities of the shared copied
resource and the partition polymatroid of the groups. To see sufficiency of
the original-subset rows, a partial set of copies has no more mass than the
full set of copies of the same original owners. Its projected original rank
therefore bounds it. Necessity follows by choosing the full inverse image
of an original subset. In optional mode, any copied set containing disposal
is additionally bounded by the original total, exactly its disposal rank.
This avoids enumerating subsets of the doubled coordinate ground.

The copied resource rank and the partition rank are integral polymatroids.
Their intersection is integral by the same paid polymatroid-intersection
theorem used in Section 7 of the companion. The group caps sum to the original
total, so attaining that total forces every group cap tight. An absent zero
group with positive remainder is infeasible. No numeric row or scalar budget
is added to this integral recovery polytope; numeric rows were evaluated
exactly on the profile before recovery.

The canonical origin-feasible simplex is called with this machine objective:

```text
R = original_total
cmax = maximum absolute copied scalar coefficient, or zero
M = 2*R*cmax + 1
maximize sum_i (M-cost[i])*x[i]       for original scalar minimization
maximize sum_i (M+cost[i])*x[i]       for original scalar maximization.
```

All resource and group caps are nonnegative, so the origin is feasible. The
global total cap makes the LP bounded. Every feasible scalar lies between
`-R*cmax` and `R*cmax`. At integral vertices a unit total difference therefore
dominates the entire possible scalar difference. Every optimal vertex has
maximum total, and, among equal-total points, exactly the best requested
signed scalar. Integrality ensures this vertex comparison establishes the
same lexicographic optimum against all fractional points. The rational
coefficient `M` has polynomial binary length; denominator clearing or a
numerical unit expansion is unnecessary.

The client checks the returned exact primal/dual certificate, checks integral
counts and either rejects an insufficient total or projects a full-total
solution. A final verifier checks every original subset, eligibility, quota,
scalar and mandatory total. Optional disposal is removed only after recovery.

## 5. Completeness, all-input accounting and representation costs

For each passing profile, recovery returns its exact scalar optimum or proves
its face empty. The marked-profile argument represents every original
feasible scalar value; projection gives no new illegal original values.
Taking the best recovered output is therefore exact, and total failure is
original infeasibility. Optional and mandatory versions are separate exact
contracts, not approximation variants.

The actual occupied-profile iterator is reused from the
[arbitrary-processing profile backend](../arbitrary-processing-scheduling/reference/profiles.py).
Normalize each positive class magnitude by `L`; its weighted-cap-one and
binary-count-cap contract is then exactly the required profile family. Empty
classes and zero mass are handled before normalization. The iterator uses an
explicit bounded stack, with one current binary count per occupied class and
no language call-stack dependence.

At each depth every partial profile extends by zeros to a profile satisfying
the count/mass caps. Distinct partial vectors at that depth give distinct
such completions. The number of traversal states, failed original-row
filters, absent zero groups and empty intersection faces is therefore at
most a polynomial occupied-depth factor times the companion's colored
partition bound. This proof charges infeasible inputs as well as successful
ones. Only the current profile, best original output and one LP are retained.

If the original ground has `n` coordinates, the LP has at most `2*n+1`
variables and `2**n + number_of_occupied_classes + 2` explicit rows. Rank
validation is polynomial in the supplied complete-table length. A native
Bland tableau uses polynomial binary workspace and at most
`binom(number_of_variables+number_of_rows, number_of_rows)` feasible bases,
with polynomial exact pivot work. This potentially exponential finite LP
factor is separate from the mathematical theorem's paid polynomial exact
intersection primitive. Rational basic solutions, the dominant scalar,
counts, targets and original IDs retain their actual polynomial encoding
costs. The profile time depends exponentially on the largest numeric target,
not just its bit length, while the workspace is polynomial in that bit length.

## 6. Bounded audit and independent finite evidence

The audit covers the complete one-order companion: safe dominance and masks,
original-total preparation, shared copying and capping, a single charged
marking prefix, support colors, colored-partition counting, exact signed
recovery, all-input traversal and binary workspace. It also checks the
separate sparse-paving oracle and readable-program ETH lower constructions.
Those bounds concern general recipient-rank oracles or encoded rank programs,
not graphic or matrix-represented subclasses; they do not give an optimal
leading exponential constant. This exact numeric-quota theorem is distinct
from a polynomial-time fractional-prefix discrepancy guarantee.

The [independent checker](verify/check_prefix.py) enumerates original vectors
and literal original inequalities on small inputs. It compares mandatory and
optional signed optima, verifies every canonical marked profile, and exercises
zero targets, empty prefixes, no rows, duplicate dominance, eligibility,
large lower-only weights and signed zero-column completion. Binary-large
fixtures run actual recovery with original totals, weights, targets or scalar
denominators beyond 330 bits, without enumerating units or counts. These
checks support the proof without replacing it. The broader two-order,
few-weight-family and ground-reduction audit scopes remain separate; no
proof-assistant verification or external peer review is claimed.

**Attribution:** icekylinx and GPT-6 Astra Pro. Apache-2.0.
