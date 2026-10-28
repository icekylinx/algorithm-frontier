# Realization of the arbitrary-processing bucket client

The [reference client](reference/buckets.py) instantiates the
[general-processing joint plan solver](../arbitrary-processing-scheduling/reference/profiles.py)
with the exact bucket masks and bounds from [Theorem AB](proof.md).
Its inputs are arbitrary complete integral recipient-rank tables, original
mandatory type totals, nonnegative rational processing times and costs,
eligibility masks, one exact assignment budget and an integer bucket depth.

**Realization proposition.** The reference either detects infeasibility of the
original bases/budget or returns Theorem AB's depth-dependent approximation.
It implements the actual bucket enumeration and joint original-total recovery,
with the shared reference LP/count costs charged separately from the theorem.

**Proof.** The client computes the rational endpoints and factor in AB3 and
AB10 exactly. At depth zero, label zero permits every time at most the target
and keeps its load bound. At positive depth, label zero retains the initial
prefix of processing times and one full load bound. A positive label retains
only its open-left/closed-right big interval and its disjoint small interval.
It gives the big group integer count cap one and the small group the residual
fractional load bound. The big interval's upper endpoint is always at most
the target; no oversized pair is accidentally retained. All original time-zero
coordinates remain in the appropriate small group.

`plan` records these groups as a partition of the allowed original coordinates.
The common [joint realization lemma](../arbitrary-processing-scheduling/reference-realization.md#1-a-general-data-adapter-and-one-joint-finite-solver)
therefore applies: its LP keeps every original type equality and the budget,
and its single minimum-cost integer recovery keeps the big cap and imposes
every descending-time small-prefix ceiling, including the full prefix.
The actual scalar assignment cost is minimized on the integral full-total face;
the budget is preserved by comparison with the witness. Jobs and resource
capacity are not copied across the groups or rounded independently.

Theorem AB, Section 6, proves that each original full-target schedule supplies
one of the enumerated label vectors. Its unique job above the initial threshold,
if present, determines a positive label, and the remainder fits the corresponding
small load. Thus total failure soundly excludes the original full target.
Sections 3 and 5 give the per-machine load bound after the joint recovery.
The exact zero gate and one-sided rational-grid optimization are inherited
from the same canonical code as the profile client, so the fixed target factor
implies the optimization factor without a monotone-success assumption.

The client streams label vectors with a counter over the depth-plus-one alphabet.
Its threshold bit lengths and alphabet storage are polynomial in the numeric
depth, exactly as charged by AB4; no polynomial-in-log-depth claim is made.
Each fixed-label LP and integer minimum-cost call has the explicit active-set,
numeric count-enumeration and vertex-storage costs in the joint realization
proof. Those costs are multiplied by the depth-dependent label count and the
polynomial number of grid calls. The source theorem uses separately paid
polynomial oracle primitives; their absence from this reference is an
implementation boundary, not an unresolved mathematical premise.
<code class="math">\square</code>

The [finite checker](verify/check_buckets.py) uses the independent original-pair
count oracle shared by the profile checker. It checks optimized outputs, sound
full-target rejections, all fixed-label fractional witnesses' joint recovery
and actual budget/load against original schedules. It explicitly constructs
the protected label vector from each full schedule and tests its joint LP.
Separate endpoint cases test open-left/closed-right big groups. Empty job
classes, rank-loss masks, zero-time costs, rational values, more than two
positive processing times on a machine and three-machine inputs are included.
Finite executable comparisons are distinct from the complete oracle proof;
no formal verification or external review is claimed.

**Attribution:** icekylinx and GPT-6 Astra Pro. Apache-2.0.
