# Verification note

**Curated source path:** `sources/checkpoint-q/arbitrary_accuracy_and_robust_root_audit.md`

The source audit follows.

# Root mathematical audit: the arbitrary-accuracy transfer checkpoint

**25 October 2026. Internal full-proof review.**

This audit records the root's acceptance decisions for the new
checkpoint-Q results. It is mathematical review, not formal verification
or external peer review. The primary guarantees have separately written
proofs and independent full reviews. The historical matching exponent
is outside the active optimization scope.

## 1. Accepted result ledger

| Result | Root decision | Independent full review |
| --- | --- | --- |
| PS arbitrary-time, exact-budget scheduling scheme | Pass | transfer_frontier and polymatroid_transfer |
| PA arbitrary-value, optional-basis shared-budget allocation scheme | Pass | transfer_frontier and polymatroid_transfer |
| AB arbitrary-time bucket curve | Pass after accuracy-encoding clarification | allocation_four and transfer_frontier |
| SP seven-profile exact 3/2 scheduling | Pass; retained as valid predecessor | polymatroid_transfer |
| SX six-profile exact 3/2 scheduling | Pass; current explicit endpoint | polymatroid_transfer |
| US common-two-size costed unrelated scheduling | Pass | polymatroid_transfer |
| HT two positive processing times per machine | Pass | polymatroid_transfer |
| AS activation with one shared setup/assignment budget | Pass | allocation_four |
| BW bounded unit-obstruction branching | Pass | transfer_frontier |
| WF width-two Fibonacci unit gate | Pass | transfer_frontier |
| RA common-setup robust additive theorem | Pass | transfer_frontier |
| CR common-role and common-dummy obstructions | Pass | transfer_frontier |
| RO whole-ground robust oracle boundary | Pass | allocation_four |
| TS two-scenario explicit k-SUM boundary | Pass | polymatroid_transfer |

The two separate PS and PA reviews inspected their complete proofs.
None of these decisions relies on numerical small-instance testing as
a substitute for a theorem. Correctness still depends on the exact
oracle and arithmetic model stated in each manuscript.

## 2. Integral recovery and the one-budget invariant

The upper-prefix machine caps have nondecreasing integer right sides
U_h=ceil(X_h). On any subset of the ordered coordinate ground, the
rank is the largest U_h indexed by a member of that subset. This is a
normalized monotone integral submodular function. Its independence
polytope is exactly the system of prefix caps. Summation by parts
therefore bounds rounded load by fractional load plus the largest
eligible unit in the group. Zero-time coordinates cause no loss.

Machine groups are disjoint and combined by direct sum. The resource
side is the direct sum of the original masked recipient polymatroids.
Two-polymatroid intersection is integral. Requiring the original total
N is a maximum-total face, because no resource can exceed its original
n_j. Thus each resource must individually attain n_j. This is the
reason masked rank deficiency cannot discard jobs silently.

The fractional witness lies on that face. Minimizing actual assignment
cost yields an integral point with cost no greater than the witness.
The argument does not require the face intersected with a cost halfspace
to be integral. Several independent exact budget rows on the same
integer assignment are not supplied by this argument.

For PA, adding a free disposal coordinate completes an independent
resource vector to a base. If f has full rank n, the extension assigns
rank n to every subset containing disposal and rank f(S) otherwise.
It is monotone and submodular. With integer singleton caps d, the
complement rank is g(S)=fhat(E minus S)+d(S)-n. The marginal bound
for fhat proves monotonicity; base complementation is a bijection.

Ceiling prefixes on the complement imply floors on every original
player prefix. Maximizing original cost coefficients on the complement
face minimizes the corresponding original cost, since the d term is
constant. Disposal has zero cost. Removing it leaves legitimate
independent resource allocations. This proves simultaneous value-prefix
and cost guarantees at one integral point.

## 3. PS: full arbitrary processing times

For delta=epsilon/2, big times are in (delta*T,T]. Bins have width
at most delta squared times T and exact lower-open, upper-closed
endpoints. A full-T integer schedule has at most floor(1/delta) big
units at a machine, and its lower-bin load is at most T. Its actual
big counts supply an enumerated profile without changing assignments.

The LP keeps every original base, the assignment budget, big-bin upper
count caps, and the remaining fractional small-load capacity. The
rounded big load exceeds its lower-bin profile by at most delta*T.
The rounded small load exceeds its fractional cap by at most delta*T.
The resulting total is at most (1+epsilon)T.

Every target has a complete all-input bound. Only occupied bins are
stored. The pruned recursive count enumeration never descends through
a partial state that violates its count or lower-load cap. Each partial
state completes by zeros. Mapping the count in bin i to parts of size
K+i, K=floor(1/delta), bounds the partition weight by floor(delta^-2).
The elementary generating-function estimate gives exp(3(K+1)) states
per machine. It is used only in the proof; no analytic product or
large partition table is evaluated by the algorithm.

## 4. PA: full arbitrary values and actual selected bases

Fixing the actual original M-basis before the LP correctly makes its
setup cost constant. Enumerating r-subsets includes rejected nonbases
and unaffordable bases in the all-input bound. No fractional selection
is substituted for a genuine selected basis.

Target capping preserves an integer target witness because an assigned
unit of value at least T becomes a single unit worth T. This is not
valid for arbitrary fractional comparators, and PA does not claim
otherwise. Trimming a first-reaching sequence of big units retains
at most ceil(1/delta) units and total capped big value strictly below
2T. If the big total is below T, retaining every big unit also respects
that count bound. Deleting other counts is legitimate only because
allocation resources are independent vectors and costs are nonnegative.

The fractional LP fixes every big-bin count to an integer. Surrogate
values are constant within a bin. The only nonzero large-value drops
occur at bin boundaries, whose fractional cumulative counts are
integers. Every large-boundary term in the lower-prefix error sum is
therefore zero. The small-value terms telescope to at most delta*T.
No unsupported exact big-count promise is made for the rounded output.

The gap between upper and lower surrogate sums is at most K*delta^2.
With delta=epsilon/3 and K=ceil(1/delta), the total loss is at most
delta+K*delta^2 <= 2delta+delta^2 <= epsilon. The original values are
at least the surrogate values and actual assignment cost does not
increase. The same basis pays the same setup fee.

For enumeration, J=floor(1/delta) and lower-bin load at most two give
partition weight less than 2(J+1)^2. The same generating-function
estimate bounds the states by exp(4(J+1)) per selected player. Thus
the displayed binom(q,r)*exp(O(r/epsilon)) bound is proved without
a hidden unweighted-composition enumeration.

## 5. Encoding, feasibility and one-sided optimization

The rational accuracy is part of the input in full. Bounds stated
only in terms of log(1/epsilon) would undercount the encoding of a
long rational near one. AB's corollary has been clarified to use
H_epsilon=H+size(epsilon); this changes no algorithmic exponent.

All stored counters are binary, and the number of stored occupied-bin
positions is bounded by original coordinates. Subset enumeration,
profile enumeration, exact LP work, integral recovery and saved actual
solutions can all be streamed with polynomial workspace. A running-time
factor exponential in 1/epsilon is not a license to allocate unary
epsilon arrays.

Allocation uses an affordable minimum-setup basis with zero allocation
as an initializer. Scheduling first minimizes cost over all original
bases on eligible pairs, and separately tests the zero-time mask. AS
correctly enumerates activation bases at both gates: a minimum-setup
basis could lack enough recipient rank to receive mandatory jobs.

Every original integer utility or load lies on the rational grid
generated by the original values or times. For maximization, complete
failure implies the target is strictly above OPT; for minimization,
complete failure implies the target is strictly below OPT. Weak
success saves an actual solution, not a claim of exact target
feasibility. At adjacent grid endpoints these one-sided invariants
give the desired factor without assuming monotonicity of successes.
Initial magnitudes and all target encodings have polynomial bit length.

## 6. Explicit finite scheduling curves

For AB, the interval endpoints satisfy

    l_i+2(1-l_(i-1))=gamma_k,  1+l_0=gamma_k,  l_k=1.

A full-T machine either contains no unit above l_0*T, or has exactly
one such unit and all remaining units below its compatible small
threshold. Recovery is one common full-total intersection. The
recurrence proves optimality only for this stated interval template.

SX's exact factor 3/2 proof is exhaustive. A unit above T/2 is unique.
There can be at most one additional unit above T/4. With none, two
large intervals suffice; with one, the upper/upper interval pair has
lower endpoints summing to T and is impossible. The remaining three
pairs and the all-small profile give six labels. Every positive-label
load bound sums to 3T/2. Empty groups and boundary equalities are
handled by the prescribed half-open intervals.

US and HT use one same-resource LP to forbid only the relevant large
placements. A protected full-target schedule retains every original
job on every omission path. In HT, a machine's individual capacity
K_p and separator coefficient lambda_p are combined as
w_p=lambda_p*K_p. The bound on ceil(K_p/d)/K_p gives the uniform
weighted omission ratio. Easy machines, small-K machines and branched
machines are recovered together in one integral face. An ordinary
allocation reduction that adds job players would not by itself prove
the physical-machine exponent stated here.

## 7. Robust positive results and obstruction scope

BW applies its width promise to the hereditary aggregate one-unit
feasibility family of a scenario, including its assignment budget.
Shrinking a failed set yields a minimal obstruction. If it exceeds
the promised width, the procedure returns a distinct width-violation
certificate. It does not report that no robust solution exists.

WF converts all singleton and pair obstructions into a graph and
forced dual-basis members. Degree branching permits overlap between
branches and never uses an unjustified independent-set dominance rule.
When the residual graph is a matching, matroid intersection selects
one independent endpoint per edge, and then extension to a full dual
basis is performed after dropping the endpoint partition restriction.
The final returned original basis is tested in every actual scenario.

RA's full comparator selects one genuine common basis. At a current
allowed set Q, the same minimum common setup charge h(Q) is subtracted
from every scenario budget. Every protected basis pays at least that
charge, and the current attained basis really pays exactly h(Q).
Scenario failures can therefore share one protected omission argument.
The comparator LP is fixed independently of target queries, which
supports the rational-separation reoptimization step. Rounding each
scenario after fixing the common basis incurs only its additive unit
loss and preserves its own scalar budget.

CR correctly excludes replacing unrelated scenario roles by one
common heavy/light partition, and excludes fractional common-dummy
selection as a general integer positivity certificate. Its separate
scenario-specific setup obstruction concerns cheap selection methods;
it is not an impossibility of exhaustive whole-ground enumeration.

RO's residue classes have pairwise intersections at most r-2, so its
sparse-paving ranks are valid. Relaxing one hidden forbidden r-set
changes a rank oracle at exactly that set. Two remaining unqueried
candidates force indistinguishable positive instances with different
required outputs, proving the stated minus-one lower bound. This
argument requires a genuine oracle representation, not inspectable
hidden-set source data. The public two-scenario consequence is separately
attributed to the three-matroid-intersection theorem; simulating a rank
query uses at most q independence queries.

TS uses two nonnegative cost vectors a_p and L-a_p with L=A+1.
The two budgets force the omitted k-subset sum both above and below
the source target. The second budget is nonnegative, zero allocations
are legal, and the selected rank is positive. Unit singleton caps make
OPT exactly zero or one. The primary source supports the bounded,
nonnegative k-SUM W[1]-hardness actually used; no claim about membership
of unrestricted k-SUM is needed.

## 8. Claims deliberately left open

No claim is made that the present schemes are the first ordinary
fixed-parameter approximation schemes. No uniform superiority over
all known accuracy tradeoffs is asserted. A query lower bound of
2^{q-o(q)} does not rule out F(q)*poly(H) approximation schemes.
The robust oracle bounds are not transferred to explicit graphic or
linear matroids without a separate reduction.

Several exact budgets on the same integer assignment, mandatory jobs
discarded after a mask, changing the selected common basis by scenario,
and arbitrary overlapping load groups are not accepted consequences.
Any subsequent extension must prove its own integral recovery,
initialization and all-input time bound before entering a checkpoint.


---

**Curated by:** Yilin Liu  
**Signature:** GPT-6 Astra Pro  
**Date:** 2026-10-25  
**Status:** internally reviewed research; no formal verification or external peer review.
