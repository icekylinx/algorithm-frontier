# Deterministic phase costs, reset accounting, and finite guards

**Mathematical reconstruction for the current general-matching candidate.**
This note combines the structural budget, local exact projection, and a
deterministic priced-step contract. Large tick jumps, persistent resets,
and first incomplete attempts are included. No perfect-matching or
connectedness promise is used.

The framework and constants originate in OAI Sections 3--5:

<https://github.com/openai/math/tree/main/preprints/Almost-Linear-Time-Maximum-Cardinality-Matching-in-Sparse-General-Graphs-September-24-2026>.

The detailed inputs are `factor_critical_contractions.md`,
`ledger_algebra_and_phase_budget.md`,
`local_exact_projection_from_priced_steps.md`,
`priced_logarithmic_steps_from_raw_cycles.md`, and
`persistent_integral_ledger_carrier.md`. A complete raw-cycle backend
remains a named dependency; see `numerical_backend_choices.md`.

## 1. Parameters and structural budget

Let S=2^s bound the physical subcubic graph order N, with N<=S<2N
outside bounded empty cases. Fix a sufficiently large integer a and set

    C=a+1, B=2^ceil(s/a), q=B^(-100),
    delta=S^(-1000), epsilon=S^(-3000).

For any proposed improvement 1<=K<=N, put

    L=ceil(10000 C N/K), g_*=max(1,floor(K/(100 C))).

The a+1 ledgers have floors c_j=C-j. Top allocations and positive
slacks use the epsilon grid; other ledgers are integral. Settled bottom
debt is zero. The top graph has one coordinate per row-bin incidence
and one slack per bin, hence O(S) live coordinates.

Independently of numerical progress, the structural algebra proves

    Lg_*=O_a(S),
    total peeled weight and materialized volume=O_a(S),
    expansions + sum of contraction arities=O_a(S).

Contractions and expansions add one tick, repaired gains add L, and
peels add none. Total ticks tau are O_a(S). The terminal gain ends the
phase without repairing obsolete ledgers. Tight pair queries charge
their output arity; successful freeing touches at most two selected
components of total physical size O(L) and is immediately consumed
by a gain. All pair work is O_a(S polylog S), including the terminal
gain. No extra L charge is paid for every contraction.

## 2. Local positivity and eligibility

Top variables are x_e>0 and s_d=L-load(d)+p_d-Cw_d>0. For fixed
debts and weights, circulation increments preserve all row and column
equations. Explicit structural batches never interrupt an increment.

For a new incidence or a cached allocation at most 3delta, read its
row's at-most-three entries. Transfer 4delta from an entry of size at
least L/3 and add 4delta debt at the recipient bin. Its load increase
is canceled by the debt; donor-bin slack increases. If both incidences
have the same bin, net load is unchanged and slack increases by the
debt addition. New rows install their two prescribed large entries
before padding others. A cached slack at most 3delta is increased,
together with its debt, by 4delta. Reanchor changed values exactly.
Epsilon divides delta, so every setting is an exact grid operation.

The register guarantee lambda(fhat)|f-fhat|<=q/100 gives relative
error at most q/100 for a single positive logarithm. Unrepaired cached
arguments exceed 3delta; repaired arguments have just increased by
4delta and were reanchored. The step's relative-motion bound leaves
arguments above delta before pricing and delta/10 at refreshes.

There is no no-motion repair chain: each row has at most three entries,
its large donor remains large, transfers never reduce slacks, and a
slack repair changes no other coordinate. Only explicit edit records
and dirty notifications are serviced. Price and forest maintenance
cause no primal motion.

On at most S^20 main actions, a crude O(S)-coordinate count gives
fewer than S^30 repairs eventually, adding less than S^(-800) debt.
This preliminary estimate uses loose caps, not the improved time it
helps prove. Only a large donor logarithm can decrease, by O(delta).

Contact lists to the paired remainder have an accessible first member.
Eligibility uses cached slack>=4C. The relative error guarantee gives
actual slack>=3C for an eligible bin and actual slack<5C on every
contact bin when no expansion is eligible. Updating a flag does not
scan its contact list.

## 3. Objective and top-client cost

Use Phi=sum_e log x_e+sum_d log s_d. Row sums give x_e<=L. Top debt
is at most 2L(g_*-1)+S^(-800): expansions create no ordinary top debt,
contractions conserve it, repaired gains add at most 2L, and peels
decrease it. Therefore s_d<=L+sum p_d=O_a(S). With the lower margins,
every argument has O_a(log S) logarithmic width. The objective range
is O_a(S log S).

Largest-child maintenance touches O_a(S log S) physical incidences
and bin records, as proved in `ledger_algebra_and_phase_budget.md`.
Read a top column residual as y_d=s_d-p_d+Cw_d. This uses an exact
slack point query; it never sums all implicitly moving allocations of
a high-degree bin. Contraction aggregates these residuals and debts
through one point read per child bin, while preserving unchanged
exterior incidence values.
Compute all old and final top settings before submitting a batch.
Each changed logarithmic term costs at most O_a(log S) in objective,
so cumulative structural losses are O_a(S log^2 S). Positivity losses
are negligible. Integral carrier normalization changes no top value.

Each successful priced step gains Omega(q^2). Thus

    J_top=O_a(S q^(-2) log^2 S)=S^(1+200/a+o_a(1)).

One final LOW or interrupted attempt adds one query. This prefix
bound holds whether or not the proposed improvement K exists.

The priced-step theorem charges initialization, external operations,
and its maintenance by S^(O(1/a)+o_a(1)). Its notification count is
at most this factor times J_top, plus events paid by explicit client
actions. Its proof includes dormant real copies, signed and absolute
retirement transfers, and full coordinate sweeps; the exact lifetime
contract is `numerical_backend_lifetime_and_loops.md`.

The client responds with constantly many local repairs or flag changes
per notification. Reanchoring causes no motion, pending flags can be
coalesced, and stale flags are skipped. Combining engine and response
costs multiplies a fixed number of small-exponent factors. Total top
work is S^(1+O(1/a)+o_a(1)), without a global per-step scan.

Use topological lifetime size R_top=SB. Actual births and endpoint
retargetings total O_a(S log S), fitting SB eventually. Repricing,
motion and positivity settings of retained coordinates create no new
topological slots. B<=2S^(1/a) implies R_top+B<=S^(1+2/a) eventually.
Persistent integral history is not numerical graph size.

## 4. Reset rule and debt at a trigger

Define exact integer periods b_j=B^(a-j), 0<=j<=a. Compare each
event's pre- and post-event ticks. Choose the smallest j in {1,...,a}
whose quotient by b_j increases. Such a j exists since b_a=1.
Project a fresh zero-debt j-ledger and share it with deeper levels;
preserve coarser levels through any peel.

If j>1 is selected, the event crosses no b_(j-1) boundary, or a
coarser reset would have been selected. Parent j-1 last reset to zero
debt in this same interval: crossing such a boundary resets it or a
coarser level and every descendant. Expansions add at most C integral
debt and one tick; repaired gains add at most 2L debt and L ticks.
Contractions never increase debt and peels decrease it. Even an L-tick
triggering jump has equal pre- and post-event quotients at the coarser
scale. Consequently

    P<=(C+2)b_(j-1).                                      (1)

This counts actual boundaries. It does not assume unit tick advances
or one reset per boundary skipped inside a long event. Since
b_0=B^a<2^a S, it proves P=O_a(S) at every local trigger.

## 5. Exact projection and persistent-reset totals

For j>1 the local projection costs (P+B)S^(O(1/a)+o_a(1)) and returns
O(P) allocation/deletion records. Its parent stays frozen through all
tests and final exact-flow/cut recovery. Apply the full batch to a
child, then normalize. Persistence makes the clone constant time,
with polylogarithmic work per changed record. Deeper fresh levels
share the child's roots. No difference from the old bottom is scanned.

At most floor(tau/b_j) events select j, each crossing a distinct
b_j boundary. Since b_(j-1)/b_j=B and B>=2,

    sum_(j=2)^a (tau/b_j)[(C+2)b_(j-1)+B]
      <=tau[(a-1)(C+2)B+2B]
      =O_a(SB).                                          (2)

The local small-exponent factor turns (2) into
S^(1+O(1/a)+o_a(1)). B padding is paid at every small reset.

At level one, start with L on every currently assigned incidence and
zero elsewhere, run a global exact integral exchange flow, and build
the carrier. This initial allocation need not satisfy the next floor.
The flow/cut proof still yields a child or peel, while preserved
coarser ledgers have the larger floor needed for the debt payoff.
The work is S^(1+o(1)). Since b_0>=S and b_1=b_0/B, at most tau B/S
level-one resets occur, for total S^(1+1/a+o_a(1)).

The exact-flow import is van den Brand et al., arXiv:2309.16629v1:

<https://arxiv.org/abs/2309.16629v1>.

For a small network with capacities polynomial in S, use the capacity
digit reduction proved in the local-projection note. A polynomial in
S is not automatically a fixed polynomial in the local network size.

## 6. Eventual guard adequacy

Use initial checks such as

    S>=2^100, 100000C<=S^(1/20),
    B<=S^(1/20), q>=S^(-1).

Cap phase main actions and each threshold test's pricing iterations
at S^20, and each numerical instance's external operations at S^100.
Check nominal sizes, integer magnitudes, precision and primitive
parameter conditions as records change. A failed deterministic check
suspends the branch and never supplies LOW.

Consider a prefix through a putative first failure. The loose caps
already bound top positivity debt. In a local test, a constant multiple
of S^100 pad settings of size O(delta) gives total unpadded-bound
violation below S^(-800), before using its O(P) locality bound.
Reanchoring and no motion during service exclude an infinite repair
chain.

Completed structural actions preserve the algebraic state independently
of numerical progress. Even L<=10000CS+1, g_*<=S and erased volume
O(Lg_*+1) bound expansions and integral debts by a fixed polynomial
in S. Column loads are at most L times the row count. Under the check
on C, exchange capacities, scaled capacities, return weights and
argument upper bounds fit the loose S^20 envelope. Include one
attempted physical-size batch at a first incomplete action.

The sharper structural count verifies the SB lifetime bound before
a first overflow. For a local test, (1) and nominal size 8192(P+1),
or a fixed larger constant, imply R+B<=S^(1+2/a) eventually. The
projection proof pays for a region expansion from already accumulated
sink flow before expanding. Its size bound therefore holds at a
putative first overflow.

Objective estimates bound completed top and local steps by
S^(1+O(1/a)+o_a(1)); add one final attempted operation. Notification
charges apply to prefixes and client responses have no no-motion
cascade. A putative first S^100 external-operation overflow would
therefore occur after fewer than S^100 charged operations, for
sufficiently large fixed a and sufficiently large S. The S^20 action
guards are adequate by the same argument.

Finally use a COMPLETE deterministic backend with its stated input
range, horizon, topology and lifetime contract. Its own size and
precision checks must be eventually adequate on these inputs. This
remains a named dependency, not a consequence of outer accounting.
The numerical notes use computable caps rather than giving hidden
asymptotic constants to the program as advice.

This first-failure proof does not assume completion of the fast
algorithm to justify a preliminary debt, pad or bit bound. Exceptional
finite suspensions are handled by the separate verified wrapper.

## 7. Phase conclusion and exact proof boundary

Initialization, materialization, structural work, pair actions, top
pricing and all resets together cost S^(1+O(1/a)+o_a(1)) for every
sufficiently large fixed a. The coefficient of O(1/a) is absolute,
provided the priced-step and numerical contracts use this same
quantitative convention. Parameter-dependent constants and convergence
thresholds occur outside the fixed exponent.

The bound holds on arbitrary inputs and prefixes ending in LOW or a
final attempted operation. LOW's logical meaning is proved separately
in `general_graph_gap_reduction.md`, using any comparison matching
with K additional edges.

The independent verifier protects accepted-answer correctness. It
does not prove this time bound, validate a missing numerical interface,
or externally certify this research assembly.
