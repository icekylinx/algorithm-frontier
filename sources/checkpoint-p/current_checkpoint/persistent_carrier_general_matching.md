# Deterministic general maximum matching through persistent integral carriers

**Research theorem draft, 24 October 2026.** This is a proposed improvement
over the earlier one-third-overhead checkpoint. It addresses arbitrary
undirected general graphs and returns an explicit exact maximum-cardinality
matching. The theorem uses the OAI state framework, reconstructed
state/projection/client proofs, and the constructive deterministic
numerical backend stated below. It is not an implementation, a formal certification,
or a claim of external peer review.

## 1. Proposed fixed-exponent theorem

For every fixed constant `epsilon>0`, the proposed algorithm has running time

\[
 O(n+m)+O_\epsilon\bigl((m_s+1)^{1+\epsilon}\bigr),                 \tag{1}
\]

where `n,m` are the numbers of input vertices and listed edges, and `m_s`
is the number of distinct nonloop edges after cleanup. The output uses
original input edge identifiers. In particular, on a simple graph the bound
is `O_epsilon(n+m^(1+epsilon))`, with the empty graph handled by the input
scan. This is an algorithm family indexed by a fixed accuracy exponent;
the constants and finite-size cutoff may depend on that exponent.

This note supplies the fixed-parameter ingredient. The additional
single-program uniformity argument is in
`uniform_general_maximum_matching.md`; it is not inferred from the
fixed-epsilon quantifier alone. For example,
fixing `epsilon=1/10` gives the concrete candidate bound

\[
                         O(n+m^{11/10}).                          \tag{2}
\]

For `m=Theta(n^rho)`, `1<=rho<=2`, its polynomial exponent is
`11 rho/10`; this includes `11/10` for sparse graphs and `11/5` for
dense graphs. Smaller positive fixed exponents are obtained by choosing
the fixed numerical parameters accordingly. These are asymptotic bounds,
not estimates of useful implementation constants.

The essential change is to maintain each **actual integral ledger** as
an implicit acyclic transportation carrier. It is not enough to keep a
separate forest-supported shadow synchronized with an unrelated allocation
vector. The new representation supplies a small selected forest and an
implicit injection at every settled state, removing the dirty-epoch
rebuild term that produced the earlier one-third exponent.

## 2. Dependencies and what is newly assembled

The public and OAI baseline distinctions remain those in
`public_baselines.md` and `oai_baseline_and_imports.md`. The September 2026 OAI main
algorithm is randomized. This construction uses only the specified
deterministic state, projection, accounting and numerical-client arguments;
it replaces its randomized structural primitive and routing backend.
The OAI manuscript is itself a model-generated, unformalized source,
so the reconstructed arguments must be assessed on their mathematical
content; rewriting them does not supply external verification.

| Ingredient | Required interface | Location/status |
|---|---|---|
| Row/bin matching state | Factor-critical records, exact ledger edits, debt accounting, lazy materialization | `factor_critical_contractions.md`, `ledger_algebra_and_phase_budget.md`, reconstructing the OAI framework |
| Local exact projection | Frozen parent point access; exact sparse allocation/deletion batch of size `O(P+1)`; full residual cut | `local_exact_projection_from_priced_steps.md`, conditional on priced steps and public exact flow |
| Priced numerical client | Exact grid circulation, progress, dirty notifications and finite-word cost | `priced_logarithmic_steps_from_raw_cycles.md`, conditional on a raw backend and mutable dynamic trees |
| Deterministic numerical engine | Raw-length cycle certificates, stable occurrences, adaptive edits, arbitrarily small fixed polynomial overhead | Either complete constructive route in `numerical_backend_choices.md` |
| Persistent transportation carriers | Whole-batch updates followed by one tree pivot per positive off-carrier incidence; retained zero edges; polylogarithmic persistent operations | `persistent_integral_ledger_carrier.md` |
| Canonical injection | Forward and inverse point queries; selected components of weight below `2L`; frozen transaction oracle | Same carrier note |
| Deterministic local pair action | Output-sensitive tight witness, or a successful exchange touching at most two selected trees | `deterministic_local_tight_discovery.md`, `balanced_forest_pair_oracle.md`, `tight_blocks_via_forest_pruning.md` |
| General-gap interpretation and degree reduction | LOW certifies an upper bound on the remaining improvement; exact matching-value offset | `general_graph_gap_reduction.md` |
| Complete phase sum | Structural volume, top objective, reset debt, padding, lifetime sizes and first-failure guards | `deterministic_phase_cost_and_guards.md` |

The carrier dynamic-tree primitive uses Alstrup--Holm--de Lichtenberg--Thorup,
*Maintaining Information in Fully-Dynamic Trees with Top Trees*,
<https://arxiv.org/pdf/cs/0310065>, with the **worst-case** implementation.
Its ordinary memory is simulated by a path-copy persistent balanced map,
so arbitrary branching of old versions adds only a logarithmic factor.
An amortized splay bound is not substituted for that guarantee.

The exact frozen-parent, assignment, transaction and materialization
interfaces are stated in the carrier note and in
`oai_baseline_and_imports.md`. The named external graph and numerical
primitives remain dependencies; current numerical route status is
recorded in `numerical_backend_choices.md`.

## 3. Why sparse ledger work remains sparse

For every integral level `j>=1`, the actual nonnegative incidence vector
is represented by a carrier forest. Every positive coordinate is a carrier
edge; zero coordinates may remain on carrier edges. Residuals, debts and
their indices are kept separately in persistent point maps. The top
numerical ledger, level zero, is not changed by this normalization.

A transportation cycle circulation preserves every row sum and column
load. Consequently it preserves every ledger floor inequality, residual,
debt and debt total. The source projection and reset arguments do not
require the normalized allocation to remain coordinatewise close to an
older integral vector or to another integral level.

For a sparse batch, first read all needed old values from its prescribed
input version and apply the entire final-coordinate and topology batch.
Only then normalize. After removing changed carrier incidences, all
positive incidences outside the surviving forest belong to that batch.
For each such incidence, either link two components or cancel its unique
fundamental transportation cycle. Cut **one** newly zero edge and keep
all other zero edges. Each processed incidence causes only a constant
number of path operations and topology edits, regardless of how many
coordinates its implicit path circulation changes.

This order is essential. Applying a later old-coordinate delta after
an earlier normalization can make an allocation negative or overwrite
a valid path change. The algorithm never uses that invalid interface.

For contractions, the source already retains a largest old bin and
retargets only incidences of moved smaller-bin members. Carrier cuts
and reinsertion attempts are charged to those same physical incidence
touches. At a local projection, the source's final exact-flow region
contains `O(P+1)` records, so the normalization adds only that many
polylogarithmic operations. A fresh child clones its normalized parent
version; deeper fresh levels share that child's roots. It never scans
the difference from the former bottom version. A level-one reset already
pays for a global flow, so a near-linear carrier build fits its budget.

## 4. Small selected trees without global assignment writes

At a settled bottom state, each row has total allocation `L` and each
bin has load at most `L-w_d<L`. Every row therefore has at least two
positive incidences. Physical subcubicity makes its carrier degree two
or three, even when zero carrier edges are retained.

Root each carrier component at a deterministic bin. Keep both incidences
of a degree-two row. For a degree-three row, omit the parent incidence
and keep the two child incidences. Suppressing row vertices gives one
selected forest edge per row. A selected component has at most one
internal row exporting allocation, and that export is less than `L`.
Writing its bin set as `C` gives

\[
 \operatorname{load}(C)=L(|C|-1)-\operatorname{out}
                        +\operatorname{in},
 \qquad
 w(C)\le L+\operatorname{out}-\operatorname{in}<2L.                 \tag{3}
\]

Assign every degree-two row to its sole carrier child and every
degree-three row to one deterministically chosen carrier child. Only
the parent row of a bin can choose that bin, so this is an injection.
Its inverse is obtained from the bin's parent row and that row's choice.
The chosen component root and each parent are dynamic-tree queries;
they do not require an explicit reroot traversal or assignment array
rewrite. Each selected component has exactly one free bin.

The physical volume of a selected component, including its internal
row vertices, is `2w(C)-1<4L`. Therefore a successful pair action can
enumerate and reorient its at most two original selected trees in
`O(L polylog N)` time. A failed pair action first uses the separate
output-sensitive tight-set detector, so it is charged to contraction
arity rather than to `L` for every contraction.

Changing the canonical injection need not materialize the represented
matching globally. Factor-critical records permit a requested exposure
to remain lazy; contraction records save their own captive assignments.
Only erased physical volume and the final phase scan are materialized.

## 5. Event transactions and phase cost

Freeze the pre-event bottom-carrier version as the assignment oracle.
An event uses that oracle plus a sparse forward/inverse overlay. An
expansion adds one assigned row; a contraction saves captive assignments
and records the entering assignment; a successful pair action writes
the assignments of its two small trees before immediately executing
the gain. A projection peel uses the same oracle and overlay when it
identifies and removes assigned rows.

Apply structural edits and preserving deletions to the appropriate
ledger versions. A projected child is based on the prescribed parent
snapshot, including the exact flow and peel deletions, and is then
normalized. Only after all repairs have restored a settled bottom
ledger is its canonical injection published. No new canonical
assignment is consulted halfway through a deletion transaction.

For a general-gap phase on a subcubic graph of order `N`, use the
same fixed parameters `a`, `C=a+1`, target `K`, and

\[
 L=\left\lceil10000CN/K\right\rceil,
 \qquad g_* =\max\{1,\lfloor K/(100C)\rfloor\}.                   \tag{4}
\]

The algebraic accounting in `ledger_algebra_and_phase_budget.md` gives

\[
 \#\text{expansions}+\sum\text{contraction arities}=O_a(N),
 \quad \sum\text{peeled weights}=O_a(N),
 \quad Lg_*=O_a(N).                                               \tag{5}
\]

Consequently all successful pair actions cost
`O_a(g_* L polylog N)=O_a(N polylog N)`, including a possible
terminal gain. Output-sensitive tight searches and small-to-large
physical updates have the same near-linear bound. Sparse carrier
maintenance multiplies the already charged integral projection work
only by a polylogarithmic factor. It introduces no additional factor
of `K`, `L`, or the number of assignment changes.

The complete reset and guard sum in `deterministic_phase_cost_and_guards.md`,
with the numerical replacement and local projection proof, gives the phase bound

\[
                    N^{1+O(1/a)+o_a(1)}.                          \tag{6}
\]

Use the source's rounded physical size `S`, for example the next power
of two above `N`, so `N<=S<2N` apart from bounded small cases. Historical
persistent-memory allocation is not substituted for the numerical graph
size. Each logical carrier version still has `O(N)` current vertices
and incidences; its version dictionary contributes only the separately
charged polylogarithmic access overhead.

All source nominal-size and finite-precision guards remain explicit.
Carrier normalization preserves the quantities used to prove eventual
guard adequacy and adds polynomially bounded bookkeeping. A suspended
guard is not a LOW certificate. At each sufficiently large fixed `a`,
the exceptional-size range is finite. The executable uniform program
does not need its unknown endpoint: suspended branches are unavailable,
all proposals are checked, and the classical branch guarantees finite
termination. The cutoff enters only the asymptotic analysis.

## 6. Direct maximum matching on arbitrary general graphs

Cleanup removes loops, coalesces parallel edges while retaining an
original identifier, and discards isolated vertices. Deterministic
integer/radix sorting implements cleanup in `O(n+m)` in the standard
word-RAM input model. Let the remaining order be `r`.

Replace a vertex of degree `d` by an odd path with `2d-1` vertices,
using its odd positions as the original-edge ports. The resulting
subcubic graph `J` has

\[
               N=4m_s-r,\qquad A=2m_s-r,
               \nu(J)=A+\nu(G).                                 \tag{7}
\]

Any actual matching `M` in `G` lifts in linear time to one of size
`A+|M|` in `J`. Conversely, every matching `Q` in `J` decodes in
linear time to an original matching of size at least `|Q|-A`.
The complete proof and decoder are in Sections 1--3 of
`general_graph_gap_reduction.md`. The graph may have odd order
and need not have a perfect matching.

Start with any deterministic supplied matching, for example a greedy
matching or the empty matching, and its exact lift. Maintain a valid
integer upper bound `U` on the remaining optimum improvement. Initially
one can take `U=floor(r/2)-|M|`. While `U>0`, set `K=ceil(U/2)` and
run the general-gap phase.

* On `g_*` successful gains, subtract `g_*` from `U`.
* On LOW after `i<g_*` gains, set `U=K-1-i`.

The gap-phase proof uses a comparison matching with at least `K`
additional edges, rather than a perfect-matching promise. A valid
LOW answer therefore gives `nu(J)<q_0+K`, exactly justifying the
second update. The invariant `U>=nu(J)-|Q|` is preserved throughout.
For `U` above a fixed `O(a)` threshold, success shrinks it by a fixed
fraction depending on `a`, and LOW approximately halves it. Below
that threshold, each successful phase gains one edge and each LOW
reduces the remaining bound. There are `O_a(1+log(r+1))` phases.

When `U=0`, the current matching is maximum. Materialize it and use
the linear decoder. No randomized branch, approximation final answer,
perfect-matching decision search, regularity hypothesis, or restricted
graph family is used.

Choose `a` so the fixed part of the exponent in (6) is less than
`epsilon/3`, and choose in the analysis a size threshold beyond which the remaining
subpolynomial and logarithmic factors fit the other `2epsilon/3`.
Since `N=Theta(m_s)` for a nonempty cleaned graph, summing (6)
over the phase driver proves (1). The earlier blocking warm start
and classical tail are unnecessary for this composition.

## 7. Optional matching-size-sensitive corollary

Let `nu` be the maximum matching cardinality. A greedy maximal
matching gives a vertex cover `C` of size `c` with
`nu<=c<=2nu`. Keep all `C-C` edges and at most `c+1` distinct outside
neighbors per vertex in `C`. The elementary replacement argument in
`matching_size_kernel_corollary.md` proves exact optimum preservation
and a kernel with

\[
                         O(\min\{m_s,\nu^2\})
\]

edges. Apply the present direct carrier algorithm to that kernel,
retaining original edge identifiers. This yields

\[
 O(n+m)+O_\epsilon\!\left(
          (\min\{m_s,\nu^2\}+1)^{1+\epsilon}\right).               \tag{8}
\]

The empty graph is again settled by the input scan. This corollary
uses no estimate of `nu` supplied by the user and adds no new
numerical dependency.

## 8. Current proof boundary

The improvement rests on a representational freedom actually allowed
by the OAI integral-ledger contract. It would fail if a client required
every normalized allocation to remain coordinatewise equal to a
separately maintained prescribed vector, required an explicit list of
all assignment changes after each update, or charged an entire large
tree for every implicit path circulation. None of these requirements
is used in the stated construction.

The reconstructed OAI-framework proofs and the full constructive
raw-length numerical backend remain explicit mathematical dependencies.
Independent interface review does not constitute external verification
of those whole manuscripts or of the new constructions.
The checkpoint should be read as a detailed candidate proof for
further mathematical scrutiny, with those dependencies visible.
