# Checkpoint O: global allocation and flow algorithms with exact budgets

**25 October 2026. English research checkpoint.**

The active direction is entirely related optimization problems. The
historical general-graph matching 4/5 result is retained for provenance;
this checkpoint does not attempt to lower that exponent.

The main advance since N is a collection of deterministic guarantees
for **all instances** of the stated allocation, scheduling and selected
flow models. They no longer require a small corank, small heavy support,
bounded price diversity or proportional assignment costs. The algorithms
use exponential time with a base strictly below two and polynomial
workspace. Exact budgets and original feasibility constraints are kept.

The sharper corank bounds remain available. Their global conversion is
based on the public monotone-local-search formula, with a separate
self-contained polynomial-space block construction and fully checked
application interfaces. This is internally reviewed research; no formal
verification, external peer review or exhaustive novelty claim is made.

## 1. The main all-instance results

Let H pay the binary numerical input, the explicit ground and resource
types, all required original and derived oracle evaluations, and the
polynomial deterministic optimization primitives. Rank functions are
normalized, monotone, integral and submodular. Numerical multiplicities
are binary encoded and are not expanded into individual units.

Write

\[
 \Gamma(R)=\frac{R^R}{(R-1)^{R-1}},\qquad
 \mathcal T_A(q,H)=(2-1/A)^q
 2^{O(q\log\log(q+2)/\log(q+2))}\operatorname{poly}(H).
\]

For a fixed A>1, this is (2-1/A)^(q+o(q)) poly(H).
Every row in the following table is deterministic and uses polynomial
space. A maximization factor d means value at least OPT/d.

| Problem | Guarantee | Whole-ground time | Meaning of q |
| --- | --- | --- | --- |
| One-value allocation; original player matroid; arbitrary assignment costs; one exact budget | Exact factor 2 | T_(27/4), base 50/27 approximately 1.851852 | Potential nonloop players |
| Two intrinsic values; all players compulsory; arbitrary assignment costs; one exact budget | Exact factor 2 | T_(27/4), base 50/27 | Players |
| Arbitrary intrinsic values; original player matroid; arbitrary assignment costs; one exact budget | Factor 2R/(R-1) for fixed rational R>1 | T_(Gamma(R)) | Potential nonloop players |
| Two-size scheduling with arbitrary integral job polymatroids | Makespan at most 3OPT/2 | T_(27/4), base 50/27 | Eligible one-large-job positions, at most the physical machines |
| Selected splittable concurrent flow with the stated exact selection oracle | Rate at least (1-1/R)OPT | T_(Gamma(R)) | Candidate commodities |
| The same flow problem with explicit robust scenarios | Same rate in every scenario, with adaptive routing | T_(Gamma(R)) | Candidate commodities; complete scenario input is in H |
| Selected flow with one shared setup and routing budget | Rate at least (1-1/R)OPT, exact combined cost | T_(Gamma(R)) | Candidate commodities |

The final row requires an exact minimum-setup restriction optimizer with
an attaining selected set. An ordinary feasibility selector is not
sufficient. One or two matroid bases have the required implementation.

The general intrinsic-allocation and flow rows yield concrete tradeoffs:

| Fixed R | Gamma(R) | Global base | Intrinsic allocation factor | Flow rate fraction |
| --- | --- | --- | --- | --- |
| 2 | 4 | 7/4 = 1.75 | 4 | 1/2 |
| 3 | 27/4 | 50/27 approximately 1.851852 | 3 | 2/3 |
| 5 | 3125/256 | 5994/3125 = 1.91808 | 5/2 | 4/5 |

For any fixed rational eta>0, taking R=(2+eta)/eta gives factor 2+eta
and global base 2-1/Gamma((2+eta)/eta). The base approaches two as eta
approaches zero. This does not prove exact factor two for arbitrary
intrinsic values in a uniformly smaller-than-two global base.

These are exponential-time theorems, not polynomial-time constant
approximations. Their model is broader than ordinary explicit item or
job eligibility, but their time regime is different from the public
polynomial approximation baselines.

## 2. Arbitrary costs: the adaptive residual-budget argument

Earlier routes could separate heavy and light assignments only under
additional cost structure or price-copy parameters. The new argument
removes those restrictions for intrinsic values.

For a fixed heavy/light split and a number k of selected heavy
recipients, an admissible completion consists of an original player
matroid basis, r-k light labels and k actual one-unit heavy assignments.
At candidate light ground Q, compute the minimum cost h_k(Q) among
all such completions and retain an attaining pair. Weighted matroid
intersection computes this exactly. Only light labels are restricted
to Q: every original heavy assignment remains available, including
heavy recipients outside Q.

The fractional light region at Q has budget C-h_k(Q). The region changes
when Q changes, but a single protected full-target pair supplies the
invariant. Whenever its original light set I* survives inside Q, its
original heavy assignment H* is still a legal completion, so

\[
 h_k(Q)\le \operatorname{cost}(H^*).
\]

Its original full light allocation remains feasible under the current
residual budget. A separating row therefore has the same weighted
omission certificate as in the fixed-region gap theorem. At success,
use the actual attaining completion, not a different set with an
unrelated cost. Cost-preserving lower rounding of the light allocation
then keeps the combined actual budget at most C.

The resulting parameterized arbitrary-cost theorem gives factor 2+eta
in Gamma((2+eta)/eta)^(c+K) poly(H), when a suitable optimum has at most
K heavy recipients at the stated threshold and c is the original player
corank. The global version processes every k<=r and every value split,
so it needs no such promise.

This argument uses one scalar minimum cost. Independent minima for
several budget coordinates need not be attained by the same completion.
Intrinsic values make the resource type classes disjoint; the accepted
proof here does not silently split a shared type differently for
different players. A separate unrelated-value route is under investigation.

## 3. Exact unit quotas give exact factor two

For one common unit value, a fractional integer quota b on a chosen
set can be recovered without losing one unit. Trim to exactly b units
per selected player, intersect the direct-sum resource polymatroid with
the per-player quota partition rank, and optimize the single assignment
cost over its full-total integral face. An integral optimum exists
with no greater cost than the original fractional point.

For a full quota K>=2, choose b=ceil(K/2). Its gap ratio obeys

\[
 \frac{K}{K-\lceil K/2\rceil}\le3,
 \qquad \Gamma(3)=27/4.
\]

Quota K=1 uses a separate exact minimum-cost matroid-intersection gate.
The original one-sided integer target search is valid even when a
relaxed success occurs at a nominal target above OPT.

For compulsory two-value allocation, the same exact small-unit recovery
is combined with the attaining arbitrary-cost heavy completion. At
T<2a, where a is the large value, a retained heavy unit suffices for
T/2; small players receive ceil(ceil(T/u)/2) small units. At T>=2a,
the fixed-player fractional LP and cost-preserving additive-a rounding
already give T-a>=T/2. Together these branches give exact factor two
with no remaining cost or heavy-support restriction in global time.

## 4. The whole-ground conversion and its space bound

Suppose a gap extension algorithm has cost A^(c-|Z|) poly(H) after a
forced omission seed Z, on every input. It must never fail if an original
full-target selected set survives. Success need only produce the
required relaxed-target solution. This stronger distinction matters:
the algorithm is not being treated as an exact decision procedure.

Partition the explicit ground into logarithmic blocks. For a block of
size n with p omitted elements, choose k minimizing

\[
 \frac{\binom nk}{\binom pk}A^{p-k}.
\]

An exact weighted average bounds this minimum by (2-1/A)^n. A local
greedy containment cover adds only a polynomial-in-block-size factor.
Enumerate every omitted-count profile and stream the products of local
covers. At least one seed is contained in the true omitted set. The
sum of costs of all seeds, including failed extensions, is T_A(q,H).
Only polynomial-sized local tables and one extension workspace are
stored. The full proof also covers zero deficits, small grounds and
binary accuracy encoding.

The same construction has a sharper corank-sensitive bound. With
E(q)=2^{O(q log log(q+2)/log(q+2))},

\[
 \Psi_A(q,c)=
 \begin{cases}
 A^c,&Ac\le q,\\[2pt]
 \displaystyle\frac{q^q}{c^c(q-c)^{q-c}}
            (1-1/A)^{q-c},&Ac>q,\quad c<q.
 \end{cases}
\]

One may use the smallest of A^c, E(q)Psi_A(q,c), and binom(q,c),
times polynomial input cost. The last option enumerates complete
omission sets and invokes deficit-zero gap routines. It does not
assume an exact fixed-set solver. The maximum of the refined curve
occurs at c/q=A/(2A-1) and equals (2-1/A)^q.

The numerical global formula is due to public monotone local search.
Polynomial space and the application-specific forced-omission
interfaces are separately proved in this checkpoint. No priority claim
for the block construction is asserted.

## 5. Selected flow and exact fractional optimization

The continuous service region comes from a rational flow LP on the
original network. A bounded Farkas-potential LP constructs nonnegative
service separating rows, including for directed networks and several
nonnegative routing budget rows. Successful service membership is
followed by actual route reconstruction.

For fixed selected sets, exact rational LP optima have a uniform
polynomial-bit denominator bound D. A one-sided fine-grid search with
spacing below 1/(2BD^2), followed by exact reoptimization of the saved
set, recovers a desired rational factor alpha=A/B without an extra
accuracy loss. Thus the corank time is Gamma(1/epsilon)^c poly(H)
for rate (1-epsilon)OPT. This improves the earlier safe
Gamma(2/epsilon)^c search bound and also applies to the accepted
fractional allocation comparator.

Explicit robust scenarios are handled by intersecting their service
regions. Routes may differ between scenarios. A shared setup and
routing budget instead uses the attaining minimum-setup optimizer
and the protected-pair residual-budget argument. All scenario
capacities and routing budgets remain exact.

Several routing-only budgets are allowed because the routing variables
remain continuous. This does not transfer to several unrelated exact
assignment budgets in an integer allocation theorem.

## 6. Limits proved in the same models

Balanced hidden-subset rank functions give deterministic query lower
bounds of

\[
 \binom q{q/2}-1=2^{q-O(\log q)}
\]

for approximation factors strictly below two in the accepted one-value
optional and two-value compulsory allocation models, and strictly
below three halves in two-size scheduling. The threshold factors
themselves are attained at base 50/27. This is an approximation
threshold separation; it does not establish that 50/27 is the optimal
base at the threshold.

The lower bounds concern full rank-value-oracle access. They do not
automatically imply hardness for ordinary explicit eligibility input.
No analogous selected-flow oracle lower bound is asserted.

Separate Hitting Set reductions give W[2]-hardness for exact full-rate
admission with corank k in two settings: many explicit scenarios, and
one scenario with many routing budget rows. They do not rule out the
fixed-relative-error algorithms above or prove hardness for a single
unbudgeted scenario.

An optional-active-machine basis scheduling obstruction is also retained:
with mandatory jobs and arbitrary recipient rank oracles, even finding
any feasible schedule can reveal a hidden basis. Merely moving the
allocation player-selector to the machine side is therefore not a
valid transfer.

## 7. Baseline audit and attribution

The relevant checked primary comparisons are:

- Fomin, Gaspers, Lokshtanov and Saurabh,
  [Exact Algorithms via Monotone Local Search](https://arxiv.org/abs/1512.01621),
  STOC 2016, and the
  [author journal manuscript](https://sites.cs.ucsb.edu/~daniello/papers/monotoneLocalSearch19.pdf):
  the public base 2-1/A and permissive-extension context. Its presented
  derandomization discusses an extra subexponential space requirement;
  our polynomial-space claim has its own proof.
- Rohwedder, Rouhani and Wennmann,
  [Cost Preserving Dependent Rounding for Allocation Problems](https://doi.org/10.4230/LIPIcs.ICALP.2025.127),
  ICALP 2025: randomized polynomial O(log n) approximation for ordinary
  Budgeted Santa Claus, with exact cost, and public cost-preserving
  additive-rounding background.
- Bamas et al.,
  [arXiv:2307.08453](https://arxiv.org/abs/2307.08453):
  the recipient- and job-polymatroid baselines and the public fractional
  scheduling/additive-largest-job ingredients.
- The public selected-flow comparisons and standard fixed-set LP
  baseline are recorded in the selected-flow manuscript. The global
  relative-loss results improve on direct 2^q enumeration in their
  stated explicit selected ground and continuous-routing model.
- The public
  [OpenAI math index](https://raw.githubusercontent.com/openai/math/main/CONTENTS.md)
  was audited only for the relevant visible entries and their scope.
  The flow-cut/embedding entry does not supply this selected-flow
  theorem; the prior counting and scheduling entries concern different
  stated models. No unpublished internal OpenAI baseline is assumed.

The ordinary unbudgeted Santa Claus comparison retains N's distinction
between a 2026 university announcement and an independently checked
complete algorithm proof. No outdated polynomial ratio is advertised
as the current universal best.

## 8. Reading order and review status

Start with global_exponential_allocation_flow_transfers.md for the
complete all-instance theorem chain. Then read:

1. adaptive_residual_budget_corank_gap.md and
   arbitrary_cost_residual_budget_near_two_allocation.md;
2. one_value_exact_budget_corank_two_allocation.md and
   two_value_arbitrary_cost_exact_two_allocation.md;
3. polynomial_space_global_gap_conversion.md and
   global_gap_corank_profile_bound.md;
4. selected_multicommodity_flow_corank_scheme.md,
   robust_scenario_selected_flow_corank.md, and
   shared_setup_routing_budget_corank_flow.md;
5. rational_comparator_gap_optimization.md;
6. unrestricted_budget_allocation_root_audit.md and
   selected_flow_and_global_conversion_root_audit.md, together with
   their named independent audits.

All these principal statements passed full root and independent
mathematical review. The archive includes the relevant proof and audit
notes and retains earlier checkpoints as historical dependencies.
Historical best-result language is superseded only within the precise
models stated here.

Current open directions include multiplicative unrelated-value
allocation with shared resource types, exact factor two for arbitrary
intrinsic values with a strictly sub-two global base, and additional
integer assignment budgets. Work on a stronger unrelated-value route
continues separately; it is not used to justify this checkpoint.

The deliverable contains English Markdown research notes and a checksum
manifest. It contains no Lean, PDF, implementation or test bundle.
