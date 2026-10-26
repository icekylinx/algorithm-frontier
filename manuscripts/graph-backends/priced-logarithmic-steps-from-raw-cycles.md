# Priced logarithmic steps from raw flat-cycle certificates

**Conditional numerical-client theorem.** This note reconstructs the
priced-step client in OAI Section 5 from an exact raw flat-cycle and
lifetime interface. It proves integer pricing, stale-price accuracy,
circulation steps, positivity and objective progress, exact-value
preservation, refresh charging, and finite-word client costs. It does
not construct the raw cycle backend or reimplement the external
dynamic-tree primitive.

Primary sources and the explicit lifetime specification are:

- [OAI preprint source, Section 5](https://github.com/openai/math/tree/main/preprints/Almost-Linear-Time-Maximum-Cardinality-Matching-in-Sparse-General-Graphs-September-24-2026),
  *Priced logarithmic steps*.
- [Chen, Kyng, Liu, Meierhans and Probst Gutenberg, arXiv:2311.18295v1](https://arxiv.org/abs/2311.18295v1),
  Lemma 2.7 for dynamic-tree path operations and Theorem 3.6 for the
  flow-maintenance viewpoint.
- [Numerical backend lifetime and loops](numerical-backend-lifetime-and-loops.md),
  for the required complete copy lists, ordered callbacks, dormant
  counters, and real-loop classification.

Either proposed backend route may be used only if it actually supplies
the whole interface below. A certificate for a ratio value alone, a
net-length bound without a raw bound, or a vertex map without stable
edge provenance does not meet the hypotheses.

## 1. Parameters, client state, and the theorem

Fix a sufficiently large integer a and a master bound S=2^s. Set

    B=2^ceil(s/a),   q=B^(-100),
    delta=S^(-1000), epsilon=S^(-3000), H=S^100.

The client's changing oriented multigraph has variables f_e on the
epsilon grid. Its separable objective has, on each coordinate, one of
the terms

    log f,
    log(f-D1)+log(D2-f),
    -W log(T-f),                 1<=W<=S^20, W integral.       (1)

Descriptors and values are on the same grid. At pricing and refresh
states, data have the stated polynomial envelope and positive arguments
lie between delta/10 and S^20, with enough client margin for the small
relative changes proved below. Constant-factor post-step margins may
be included in the numerical guards. The matching and local projection
clients provide much more headroom than these loose powers require.
The engine proves positivity; a separate client remains responsible
for its own feasibility equations and global magnitude envelope.

Let g_e=phi'_e(f_e). Define lambda_e as the sum of the absolute
derivatives of the individual logarithmic terms, with their weights.
For the two-sided term this means

    g_e = 1/(f_e-D1)-1/(D2-f_e),
    lambda_e = 1/(f_e-D1)+1/(D2-f_e).                         (2)

The client may insert, delete or retarget graph records; change a value
or descriptor; or request an exact coordinate value. Such explicit edits
need not be circulations. Between them every numerical increment must
be an exact circulation, so the current divergence is preserved.

A nominal lifetime size R counts logical vertex and edge births and
endpoint insertions, including retargetings. Value changes and internal
repricing on retained logical topology do not consume fresh ports.
Assume R+B<=S^(1+2/a). Let Q count external pricing, point and edit
operations, with a loose guard Q<=S^100.

**Theorem.** Conditional on Sections 2 and 7's backend and dynamic-tree
interfaces, there is one finite implementation with the following
properties, at all sufficiently large S for each sufficiently large
fixed a:

1. LOW cannot be returned when a nonzero logical circulation d satisfies
   g^T d >= (1/2) sum_e lambda_e |d_e|.
2. An accepted step is an exact epsilon-grid circulation h with
   sum_e lambda_e |h_e|<=q/100 and g^T h>=q^2/1000. All logarithmic
   arguments stay positive throughout its application, and the complete
   step increases the objective by Omega(q^2).
3. After settlement, registers fhat_e satisfy
   lambda_e(fhat_e)|f_e-fhat_e|<=q/100. Refreshes are reported as a
   dirty-entry list, with at most the number of accepted steps times
   S^(O(1/a)+o_a(1)) reports, apart from explicit client settings.
4. Total time, including initialization, arithmetic and all representation
   changes, is (R+B+Q)S^(O(1/a)+o_a(1)). No full coordinate scan is
   performed after a numerical step.

An imported explicit failure or suspension is propagated. A failed
structural, lifetime or defensive conservation check causes suspension,
not LOW. This client is deterministic when its backend is deterministic. Any imported
conditional failure allowance is unchanged, since the remaining
operations use no randomness.

## 2. Exact raw backend and lifetime hypotheses

Choose M=2^u by rounding 16(R+B) upward so that u is divisible by 2a^2.
For fixed a this adds only a fixed multiplicative factor. Check

    S^(1/a)<=M<=S^2,        D=M^(10/a),        D<=S^2,
    M^(-10/a)/4>2q.                                        (3)

These conditions eventually hold under the nominal-size premise. The
chosen divisibility makes D an integer power of two.

The backend accepts a degree-three undirected multigraph with reference
orientations and fixed vertex slots, of total current size at most M.
Lengths are positive integers and signed gradients are integers, with
magnitudes at most M^(1200a). Repricing may be a deletion and insertion
on the same fixed endpoint slots.

It maintains an exposed forest with these properties:

- Each occurrence vertex has an input-slot image. Each forest edge
  maps to one actual input-edge lifetime with specified endpoint
  correspondence, or is a true null edge joining equal images.
- At most D/4 occurrence vertices have any one input-slot image. This
  counts isolated and dormant exposed occurrences and reserved pools.
- A query returns P_c=M^(O(1/a)+o_a(1)) oriented input edges and forest
  paths, each with unit coefficient; repetitions are listed separately.
  Their signed physical projection c is a circulation.
- Let V be the sum of the input lengths of **all mapped traversals**,
  counting multiplicities before cancellation. Null edges contribute
  zero. If the optimum integer-priced circulation ratio is positive,

      V>0,    |gamma^T c|/V >= M^(-10/a) OPT.                (4)

- Initialization, edits, queries and exposed forest logs have the
  M^(1+O(1/a)+o_a(1)) initialization and
  M^(O(1/a)+o_a(1)) amortized per-operation bounds, throughout the
  polynomial lifespans used here, including adaptive clients.

The lifetime contract is equally necessary. Retained images and endpoint
correspondences are immutable during a record's lifetime. Changed images
or endpoints are replacements. Before a record retires, its old mapping,
coordinate lifetime and price metadata remain available for callbacks.
An old-to-final transaction permits deletion-first forest edits and no
intervening path query or numerical motion. Every exposed dormant copy
remains in the numerical copy lists and their multiplicity bound.

A released pool slot retains its counters if its edge lifetime and image
remain live. If it is removed from the exposed forest, it undergoes an
actual retirement and the transfers in Section 8. It cannot disappear
and later reappear with silently restarted counters. A real edge is
not null merely because its endpoints have equal images or its current
gradient is zero. Real loop/nonloop changes also require the appropriate
retirement and replacement.

This is the complete imported numerical-backend boundary. In particular,
the theorem does not infer its recourse or quality from a final matching
verification procedure.

## 3. Port paths reduce degree without changing logical conservation

For each logical vertex lifetime, maintain a private path of port
vertices, optionally beginning with an isolated representative. Every
logical edge insertion receives a fresh port at each endpoint; a logical
loop receives two different ports. Append new ports to their endpoint
paths. Retargeting uses new ports. Each real edge joins its two ports.
Path connectors have length one and gradient zero.

The degree is at most three. Retired ports and wholly inactive old
vertex paths can stay until instance retirement; different logical
vertex lifetimes have different paths. Their total size is O(R), since
only logical endpoint insertions extend paths. A price replacement
retains its endpoint ports. The factor 16 in the choice of M leaves
ample room for ports, representatives, connectors, real edges and fixed
slots. Counts are checked incrementally.

Summing conservation over a port path cancels its internal connectors
and gives conservation at its logical vertex. Conversely, a logical
circulation d lifts by routing its incidence imbalances along each port
path. The imbalance sum on each such path is zero. A real incidence
contributes at most |d_e| to each of at most M connector positions.
Therefore its lift has connector length at most

    2M sum_(real e) |d_e|.                                  (5)

No connector primal value is stored. Connectors express conservation
of increments. Existing logical values may have nonzero divergence.

## 4. Integer prices remain accurate under stale registers

At an anchor, fhat_e is an exact current point value. Compute

    ell_e = ceil(H lambda_e(fhat_e)),
    gamma_e = round(H g_e(fhat_e)),                          (6)

with deterministic nearest-integer tie breaking. These operations use
exact rational arithmetic, not logarithm evaluations. Every individual
argument is a dyadic rational, and each coordinate has at most two
reciprocal terms and one bounded integer weight.

The argument and weight bounds give, with room in the exponents,

    S^(-20)<=lambda_e(fhat_e)<=S^1022,
    ell_e>=S^80,

and the prices fit M^(1200a), because S<=M^a. The constant-factor
rounding overhead fits the same loose price cap.

For now assume the register invariant

    lambda_e(fhat_e)|f_e-fhat_e|<=tau,       tau=q/100.         (7)

Consider one logarithmic term of weight W>=1 with anchored argument
rhat and current argument r. Its derivative magnitude W/rhat is at
most lambda_e(fhat_e), so

    |r-rhat|/rhat <= tau/W <= tau.

Its derivative changes by at most tau/(1-tau) times its anchored
magnitude. Summing these absolute errors term by term remains valid
when two signed derivatives almost cancel. Rounding contributes at
most 1/(2H), which is negligible relative to q ell_e/H because
ell_e>=S^80 and the checked guard q>=S^(-1) holds. Thus

    |g_e(f_e)-gamma_e/H| <= (q/10) ell_e/H,
    .9 ell_e/H <= lambda_e(f_e) <= 1.1 ell_e/H.              (8)

The lower and upper estimates also follow directly by comparing each
positive derivative magnitude with its anchored value. Equation (8)
uses lambda, not |g|; near cancellation in g therefore causes no loss
of relative error control. Section 9 will prove (7) without scanning
all coordinates.

## 5. Strong directions pass the raw acceptance test

Suppose a logical circulation d satisfies the theorem's strong-direction
inequality. Write A=sum_(real e) ell_e|d_e|. By (8), its integer-priced
numerator is at least (.45-q/10)A. Its port lift has additional length
at most 2M sum|d_e|, which is at most 2S^(-78)A by (5).
For sufficiently large checked S, the lifted ratio therefore exceeds
1/4. The raw backend's optimum is at least this value.

For the returned list, compute its exact **integer-priced** numerator
Gamma and raw length V with forest path aggregates. This does not
compute the current real gradient at every traversed coordinate.
Accept precisely when

    V>0,                 |Gamma|>=2qV.                     (9)

The backend guarantee (4) and margin (3) force acceptance whenever a
strong direction exists. Otherwise a failed test can return LOW.

If a query itself exposes no-motion forest changes, process its complete
old-to-final logs before reading the returned paths. Treat those logs
and the use or discard of that answer as one transaction: defer refresh
flags raised by the logs until the answer is consumed. Query churn
changes neither f, its anchors nor its input prices, so the register
accuracy certified before the query remains true, even if retirement
has concentrated old absolute mass into a bucket above its threshold.
The returned list must refer to the final forest of that query, and no
backend replacement may invalidate it before use. After applying or
discarding it, drain all flags. One may instead discard a list and
re-query after refreshing, but must not use a list invalidated by that
refresh. The first ordering needs no extra query.

A defensive conservation check can additionally sum the mapped endpoint
imbalances of the P_c pieces in O(P_c log P_c) dictionary work. Each
forest path telescopes to its two mapped endpoints, and a true null edge
contributes zero, so no path expansion is needed. An invalid list can
cause suspension before motion. This check verifies conservation of
the reported list; it does not certify raw approximation quality or
the completeness of the backend's copy/counter records.

## 6. A common dyadic step gives progress and protects every partial update

Reverse every piece if necessary so that Gamma>0. Let N_e count every
real-variable traversal in the list, including repetitions. Its net
coefficient obeys |c_e|<=N_e. From (8)--(9),

    g^T c >= 2qV/H-(q/10)sum_e ell_e N_e/H
            >= 1.9qV/H >= qV/H,
    sum_e lambda_e N_e <= 1.1 V/H.                         (10)

Choose a positive power of two mu in the interval

    q/400 <= mu V/H <= q/200.                              (11)

The interval has ratio two, so such a power exists. Section 11 proves
that it is an exact multiple of epsilon. Apply the same mu to every
piece, then project away the port connectors. The resulting logical
increment h=mu c is an exact grid circulation, and

    g^T h >= q^2/400,
    ||lambda h||_1 <= 1.1q/200 < q/100.                     (12)

Equation (10) controls the **sum of absolute partial motions**, not
only their final net value. During the entire application, each argument
stays within relative distance 1.1q/200 of its starting value, divided
by the weight for a weighted term. Hence every argument remains positive,
even if the list repeatedly traverses one physical coordinate in
opposite directions.

Apply the complete list before any reprice, refresh or client change.
Individual pieces need not be circulations, and a partially updated
vector need not satisfy the client's conservation equations. The final
vector does. Threshold detection may flag and disable copies during
the list, but it cannot change their prices or service a coordinate
until the complete list has been applied.

For a positive logarithm, log(1+z)>=z-z^2 when |z|<=q/100. The sum of
these quadratic losses is at most (q/100)^2. A negative weighted
logarithm in (1) is convex and lies above its tangent. Consequently

    Phi(f+h)-Phi(f) >= g^T h-q^2/10000 = Omega(q^2).          (13)

Both the progress and partial-positivity arguments require the raw V
in (9)--(11). Replacing it by the norm after cancellation would remove
the bound on the actually performed partial motion.

## 7. Mutable dynamic forests and the required augmentation

Import a deterministic mutable dynamic-forest implementation supporting
link, cut, evert, path exposure, point access and constant-size lazy path
aggregates in logarithmic amortized time per primitive. Reporting and
disabling a witnessed threshold violation has the same per-report
amortized cost. These are the standard dynamic-tree operations cited
in Lemma 2.7 of the primary incremental-graphs source. We do not prove
or reimplement that underlying data structure here.

The extra fields needed by this client have a constant-size tag algebra,
which we now specify. Subdivide each exposed forest edge by an edge
node. On a real-variable copy c, let s_c=+1 when traversal from its
represented-parent side agrees with the fixed physical orientation,
and s_c=-1 otherwise. Store:

    h_c : signed physical increment since this copy's birth,
    A_c : absolute motion since its last coordinate anchor or birth.

After everting v and exposing the path to w, a path increment uses

    h_c <- h_c + mu s_c,       A_c <- A_c + |mu|.            (14)

Connector and true-null copies do not carry primal counters. Preferred
path aggregates maintain the signed sum sum s_c gamma_c, the raw sum
sum ell_c, and a witnessed minimum of theta_c-A_c over enabled real
copies. Disabled real copies are omitted from this minimum but still
receive (14).

An evert flips traversal signs and path order, but does not negate h_c.
The lazy transformations have the form

    (s,h,A) -> (r s, h+alpha s, A+beta),       r in {+1,-1}.

Applying transformation 1 and then transformation 2 gives signed offset
alpha_1+r_1 alpha_2 and absolute offset beta_1+beta_2. Thus a later
reroot cannot retroactively reverse an earlier physical increment.
The gradient aggregate changes sign on reversal, raw length does not,
and an absolute addition uniformly shifts the enabled minimum. Tags
are pushed before point fields, children, or physical interpretations
are changed. This augmentation costs constant field work per imported
tree primitive and needs no virtual-subtree aggregate.

After each path update, repeatedly expose that path, find a nonpositive
minimum, and disable its witnessed copy at a point. This costs
O((1+number of actual disables)log N_f) amortized tree operations.
Do not refresh the coordinate during this process.

The numerical engine has **one mutable history**. Its amortized forest
state is never forked through persistent snapshots. The persistent
integral-ledger carrier used elsewhere is a separate data structure
with its own worst-case persistent-operation proof. Initial forest
construction and reuse of a fixed isolated-node pool are charged in
this one mutable sequence.

## 8. Exact values survive churn, dormant reuse and repricing

There are at most D current copies of any one actual edge. For a nonloop
edge, all such copies lie in the forest induced by its two endpoint
occurrence sets, which together have at most D/2 vertices. A forest on
those vertices has fewer than D/2 edges. For a loop, use its one endpoint
occurrence set. The looser D bound also leaves transaction slack. All
dormant exposed copies are counted. Parallel physical edge identifiers
remain distinct.

Maintain the complete current-copy list of every real coordinate e,
including dormant internal pool edges. With an explicit signed base,
maintain

    f_e = base_e + sum_(c maps to e) h_c.                    (15)

An explicit single-edge traversal changes the base. A new copy starts
with h_c=0. Before retiring a copy, read its h_c and transfer it into
the base, then remove the record from the list. Old mappings and
orientation metadata remain available until this transfer finishes.
A client setting to f_new sets base_e=f_new-sum h_c. These operations
prove (15) by induction. Exact point access or a coordinate sweep costs
O(D) tree point operations, not unit time.

A retained dormant copy keeps h_c even when its slot is assigned to a
different child occurrence. Its already executed physical increment
need not be a circulation in the *current* forest representation.
Equation (15) records that old increment in the physical coordinate;
every newly executed step is a circulation in the current representation.
Representation maintenance alone changes no f_e.

Absolute motion is a different invariant. Maintain a nonnegative bucket
b_e containing absolute explicit-edge motion and absolute counters
transferred from retired copies since the most recent anchor. Then

    |f_e-fhat_e| <= b_e + sum_(c maps to e) A_c.              (16)

On copy retirement, transfer **both** h_c to the signed base and A_c to
the absolute bucket before invalidating its old identity. The two
transfers serve different purposes. A new copy starts with A_c=0;
a surviving dormant copy retains A_c. Repeated retirement of copies
with individually small drift therefore cannot hide accumulated motion.

A real edge with zero gradient, a real loop, or a traversal that cancels
another traversal still carries these counters. Suppression of an
actually null fiber is safe only after all real incident records have
retired and transferred their counters, as specified in the lifetime
interface.

## 9. Drift detection, transaction order, and register accuracy

At an anchor, choose a power of two theta_e with

    qH/(800D ell_e) <= theta_e <= qH/(400D ell_e).            (17)

All current real copies of e and its bucket use this threshold. New
copies receive the current price and threshold before they can be
traversed. A copy reaching threshold is disabled and sets a coalesced
pending flag on the **coordinate lifetime**. Explicit bucket changes
and retirement transfers test the bucket directly. A flag survives
retirement of the particular copy that triggered it.

At a safe boundary after a complete accepted step or a completed
representation transaction, service a pending coordinate by this
no-motion transaction. The query-log/answer transaction of Section 5
must first consume or discard its answer; a refresh cannot invalidate
an answer still waiting to be applied.

1. Read its exact value using the full current copy list.
2. Reset every current A_c and its bucket to zero, reenable all its
   current copies, and clear the old pending flag.
3. Install the new anchor and compute its new integer prices and
   threshold. Process the backend price replacement, retaining all old
   metadata until removals finish. Every new copy receives the current
   fields. Sweep retained copies as needed so all current copies have
   the new price and threshold before the transaction ends.
4. Queue flags raised on other coordinates by those removals. Complete
   the representation transaction before servicing the queued entries.

Resetting before the replacement logs means the coordinate's own
retiring copies transfer zero absolute mass. Signed h_c is not reset;
its value transfer remains necessary. Pending flags on other coordinates
are not lost. Descriptor changes and explicit client settings reanchor
with the same order, subsuming any old flag. Retired coordinate lifetimes
have their stale queue entries removed or recognized as stale.

No unfinished old-to-final representation transaction may coexist with
an anchor sweep: otherwise a late old copy could transfer unreset mass
after the sweep. Likewise, an old record cannot silently disappear merely
because a later final topology looks the same. The lifetime contract
requires either genuine retention or a completed retirement.

Drain the queue before the next pricing call. At settlement, every
current copy and the bucket are below theta_e. Equations (16)--(17) give

    lambda_e(fhat_e)|f_e-fhat_e|
      <= (ell_e/H)(D+1)theta_e
      <= q(D+1)/(400D) <= q/200.                            (18)

This proves a stronger form of (7), closing the stale-price argument.
Only touched copies, bucket events and pending coordinates are read.

## 10. Refreshes and no-motion cascades are paid by actual motion

Partition each coordinate's history into intervals between successive
anchors. Its integer price is fixed in one such interval. A genuine
refresh report requires at least theta_e of raw absolute motion in that
interval, whether witnessed in one copy or accumulated in the bucket.
In units of anchored length it consumes at least

    theta_e ell_e/H >= q/(800D).                            (19)

Intervals for one coordinate are disjoint, and different coordinates
use different real-edge traversals. Transfers between copies and bucket
do not duplicate mass. A client reanchor can discard old credit, but
cannot create credit and is separately charged as an external operation.

A copy-disable event also consumes at least (19) in that copy's
accumulation since birth or reset. It can be disabled at most once in
that accumulation; reenabling at an anchor resets its A_c. These
disable charges are disjoint within their own charge category. Counting
the refresh and disable categories together costs only a constant
factor, even if a disabled copy later retires into the bucket.

During a successful step the prices remain fixed, and (11) gives total
raw priced real-edge motion at most

    sum_e (ell_e/H)|mu|N_e <= mu V/H <= q/200.               (20)

Therefore, over any prefix, refresh reports and copy disables number
O(D) times the number of successful steps, apart from explicit client
settings. This charge includes flags revealed by arbitrary later
representation churn.

A no-motion refresh cascade is finite. After a coordinate's reset all
its absolute locations are zero; subsequent no-motion representation
changes preserve this fact. Its own replacement cannot recreate mass.
Other coordinates may expose pre-existing mass, but each report has
the disjoint charge above. A coordinate cannot repeatedly refresh
without new motion or a separately charged explicit client change.

The O(D) reports per step each perform O(D) point accesses in their
copy sweeps. The resulting **O(D^2)** sweep cost is included in the
time bound. It is not replaced by an assumed constant-time coordinate
refresh.

## 11. Exact dyadic choices and finite-word bounds

Every argument at an anchor is k epsilon for an integer k>0. The
polynomial upper bound gives k=O(S^3020), so k has O(log S) bits.
Its reciprocal is epsilon^(-1)/k. The products, sums and quotients
needed for at most two such fractions and W<=S^20 have O(log S) bits,
with fixed constants in the bit bound. Rounding (6), comparing ratios,
and selecting powers in (11) and (17) use exact integer arithmetic.
No logarithmic objective value is evaluated.

The exposed forest has O(MD) occurrence and subdivided edge nodes.
A simple forest path has at most that many edge traversals. Thus the
piece count and forest-size bound give a computable upper bound on total
traversals without expanding any path. Check the loose cap S^20. It
eventually holds at each sufficiently large fixed a, since M<=S^2 and
the occurrence and piece overheads have exponent O(1/a)+o_a(1).

All physical input lengths are integral, so V is an integer. The
derivative and price bounds give the conservative estimate

    V/H <= S^1044.

Together with q>=S^(-1), the chosen power of two satisfies

    mu >= S^(-1045)/400.

For sufficiently large checked S this exceeds epsilon. Since both
mu and epsilon are powers of two, mu is an integer multiple of epsilon.
There is **no coordinatewise rounding** of c or h. Every partial update
and the final circulation stay exactly on the common grid.

Similarly, (17), D<=S^2 and the rounded price range put theta_e above
S^(-1030) for sufficiently large S, far above epsilon. It too is an
exact grid-compatible power of two. These conservative inequalities
can instead be checked directly from the selected powers at finite
sizes, with suspension when inadequate.

Because V>=1 on an accepted answer, mu<=S^100. There are at most Q<=S^100
successful steps and at most S^20 raw traversals per step. Total
unweighted absolute numerical motion is consequently at most S^220.
Signed copy counters, absolute counters, buckets and lazy offsets have
polynomial magnitudes on the epsilon grid. Bases have the same property:
a client setting replaces the base by a value of magnitude at most
S^20 minus a sum of already charged signed motion. Transfers do not
duplicate motion, and anchors only reset absolute counters.

Path length and gradient aggregates and record-generation identifiers
also have polynomial magnitudes. Thus every field has O_a(log S) bits
at fixed parameters, and its arithmetic adds only logarithmic-power
overhead. Varying-parameter portfolio branches must represent longer
integers and addresses as charged digit arrays or touched-cell
dictionaries; this fixed-branch proof does not grant unit-cost
unbounded-word operations.

## 12. Total work and the exact scope of the result

Let U=M^(O(1/a)+o_a(1)) bound backend edit/query cost and exposed
recourse, and P_c=M^(O(1/a)+o_a(1)) its piece count. Let N be the number
of successful steps, so N<=Q. The work consists of:

- Backend initialization and the initial exposed forest, within
  M^(1+O(1/a)+o_a(1)).
- External queries and logical edits, and O(DN) internal coordinate
  repricings. Their backend work and forest logs cost at most
  O(M+Q+DN)U, with logarithmic tree/identifier overhead per log.
- Exact coordinate reads, settings and anchor sweeps, costing
  O((Q+DN)D) tree point operations, including the D^2 N term.
- The returned path pieces, raw sums, complete signed/absolute updates,
  optional sparse conservation checks, and O(DN) disables. These use
  O(QP_c+DN) logarithmic-amortized tree and dictionary operations.
  The QP_c term includes computing the raw sums of answers that fail
  the acceptance test and return LOW; only successful answers incur
  the complete signed/absolute updates.

Retirement transfers are one point operation per actual retiring copy;
their log cost is already included. Cascaded refreshes are covered by
Section 10. Mere maintenance causes no new primal motion, so it cannot
generate an additional uncharged category of refresh work.

Since D=M^(10/a), these costs sum to

    (M+Q) M^(O(1/a)+o_a(1)).

For fixed a, M is at most a fixed multiple of R+B and is at most S^2.
The claimed (R+B+Q)S^(O(1/a)+o_a(1)) follows. Backend calls caused by
refreshes have a polynomial total horizon in M at each fixed a; that
horizon is part of the imported interface in Section 2.

All client guards are checked locally or with incrementally maintained
counts: descriptor validity, anchor argument ranges, slot and record
counts, the quality margin, dyadic-grid compatibility, and the loose
traversal/operation bounds. The established inequalities apply through
a first attempted guard-reaching operation. In the sufficiently large
fixed-parameter range, the client's guards therefore do not interrupt
a proceeding computation whose backend satisfies its own eventual
prerequisites. The backend's prerequisite theorem remains an explicit
dependency.

The proof yields the exact priced-step interface needed by the top
barrier and by
[local exact projection](local-exact-projection-from-priced-steps.md).
Its substantive numerical dependencies are now separated: a valid raw
flat-cycle/lifetime backend, and the standard mutable dynamic-tree
primitive. The current matching phase and projection arguments supply
the client magnitude margins and their own operation counts.
