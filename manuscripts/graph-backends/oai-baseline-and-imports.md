# OpenAI baseline and exact imported interfaces

**Source scope for the present research construction, 24 October 2026.**
This note distinguishes the source's randomized theorem, its deterministic
components used here, and the replacements supplied by this checkpoint.
It is not an independent certification of the complete source manuscript.

## 1. The baseline statement

The source is *Almost-Linear-Time Maximum-Cardinality Matching in General
Graphs*, dated 24 September 2026. Its official directory retains the
historical word `Sparse`:

<https://github.com/openai/math/tree/main/preprints/Almost-Linear-Time-Maximum-Cardinality-Matching-in-Sparse-General-Graphs-September-24-2026>.

Theorem 1.1 covers arbitrary simple undirected graphs, with p=n+m.
It states one uniform randomized word-RAM algorithm, bounded by
p^(1+o(1)) instructions on every random computation path, returning an
explicit maximum matching with probability at least 2/3. A bound on
every path's time is not a deterministic guarantee of successful output.

The collection's official README describes model-produced manuscripts
with varying verification status:

<https://github.com/openai/math>.

The present work therefore treats the deterministic source lemmas below
as explicit mathematical dependencies. Its own final output check does
not certify those lemmas or their running-time consequences.

## 2. Where the source uses randomness

The source's Section 3 structural search uses randomized local cut
exploration and allocation-guided absorbing walks to rearrange bin
assignments. Sections 6--8 use sampled routing objects, sampled cut/load
preservation, random projections and padded partitions to construct the
flat-cycle backend. Checking a sampled object's correctness does not
give an efficient deterministic way to find one.

The deterministic interleaving in Section 9 still runs randomized
branches. Its classical fallback gives termination but does not by
itself give a deterministic near-linear time bound.

The current construction replaces both randomized structural actions
and the randomized routing/backend chain. It uses its own uniform
interleaving of deterministic branches with an independent final
augmenting-path check. It does not enumerate seeds or assume that a
successful sample can be found cheaply.

## 3. Matching state and ledger interfaces

Section 3 represents a matching by disjoint odd factor-critical bins,
single-vertex rows, an injection assigning every row to an incident bin,
a paired remainder and isolated unmatched blockers. Each bin stores a
constructive witness that can expose any specified physical vertex.
A bin of physical size 2w_d-1 has weight w_d. Rows have at most three
physical incidences, with parallel contact IDs retained.

For levels j=0,...,a, put C=a+1 and c_j=C-j. The ledger conditions are

    x_e^j >= 0,
    sum_(e incident to row r) x_e^j = L,
    y_d^j = L - load_d^j,
    p_d^j >= 0,
    y_d^j + p_d^j >= c_j w_d.

The top x and slack variables are positive dyadic values. Levels j>=1
are integral, and the bottom debt is zero at a settled state. The source
does not impose coordinatewise closeness of different integral levels.
The top logarithmic objective uses only the top x and slack variables.

The following deterministic components originate in Section 3:

* valid factor-critical contraction from a minimal tight bin set;
* exact expansion, contraction, gain and preserving-deletion formulas;
* bottom strict Hall surplus and the tight-set weight bound;
* the debt consumed and blockers created by a failed projection peel;
* local small-to-large physical maintenance and lazy materialization of
  saved contraction witnesses.

Their proofs are now reconstructed in this checkpoint:
[factor-critical-contractions.md](factor-critical-contractions.md) proves the minimal-tight Hall argument,
creation-time witnesses and arbitrary-exposure materialization;
[ledger-algebra-and-phase-budget.md](ledger-algebra-and-phase-budget.md) proves the exact ledger formulas,
peel debt payoff, blocker and volume bounds, and small-to-large incidence
charges. These are mathematical proof drafts with the source framework
credited, not external certifications of the manuscript.

The source presents the injection explicitly. The current representation
changes its storage: forward and inverse assignments are point queries
on a retained carrier version, with a finite local overlay during an
event. Every source use of an assignment is supplied through that
interface. Contact lists and expansion eligibility depend on the physical
partition and top slack, so a settled-state canonical assignment change
does not require updating those lists. Contraction witnesses keep the
assignments saved at their creation. These representation claims are
proved in [persistent-integral-ledger-carrier.md](persistent-integral-ledger-carrier.md).

## 4. The integral projection interface

Section 4 takes a current integral parent ledger and seeks an exact
child ledger at the next floor. Its explored exchange network uses
point values of that parent, sparse row neighborhoods and a debt index.
The local algorithm returns the complete exact exchange-flow support,
and when necessary the full residual bin set for a peel. Their record
count is charged to the parent debt and the source's small-instance
padding. The first integral level may use a global exact flow; higher
levels use the local projection and persistent sharing.

The current construction freezes one parent version for ALL threshold
tests, locks, capacity reads, final exact-flow extraction and cut/peel
recovery belonging to a projection. Carrier pivots occur before that
snapshot or after its complete final batch. They never change the
parent while its projection engine is running.

The new child is based on the designated pre-peel parent version.
Its exact flow and ALL deletions, including exterior load released by
removed rows, are applied before normalization. Preserved coarser
ledgers receive their separate preserving-deletion batches. These
requirements prevent both stale-coordinate updates and a silent scan
of the entire old bottom vector.

The deterministic exact-flow primitive is public: van den Brand et al.,
*A Deterministic Almost-Linear Time Algorithm for Minimum-Cost Flow*,
arXiv:2309.16629v1:

<https://arxiv.org/abs/2309.16629v1>.

Capacity digit scaling handles large capacities relative to a small
local graph. [local-exact-projection-from-priced-steps.md](local-exact-projection-from-priced-steps.md) reconstructs
the local exploration, locked threshold tests, exact two-region recovery
and full residual cut, conditional on its explicitly stated priced-step
interface. It proves the O(P) support and physical-volume bound. The
public static flow theorem alone would not establish this locality.

The newer alternative is
[near-feasible-rounding-and-exact-projection.md](near-feasible-rounding-and-exact-projection.md). It gives an explicit
cost-nonincreasing rounding algorithm for exactly conserved rational
flows with less than one unit of total integral-bound violation.
Success at a threshold gives a true feasible flow; the adjacent final
failure gives an optimistic maximum flow and a cut. Their checked
primal/dual pair certifies the full local optimum, and their represented
union gives the complete full residual peel without a fresh flow solve.
An all-expanded version also replaces the first-level reset. Thus the
new `14/15` composition does not import the public static flow time
bound for recovery. It still requires the priced client's complete
raw-cycle interface and its strong-direction guarantee.

## 5. The numerical client and phase accounting

Section 5 converts a flat-cycle backend into priced logarithmic steps.
The backend must return a circulation with a literal traversal-length
certificate, stable occurrence images and explicit retirement records.
The client keeps exact values implicitly, maintains coordinate anchors,
and separately accounts for signed increments and absolute motion.
[priced-logarithmic-steps-from-raw-cycles.md](priced-logarithmic-steps-from-raw-cycles.md) supplies the full client
derivation, including integer rounding under derivative cancellation,
raw-motion positivity, exact grid steps, dormant counters, query-answer
transactions, and the D-squared refresh-sweep charge. Its remaining
imports are the named raw flat-cycle backend and standard mutable
dynamic trees.
The two replacements supplying its backend are catalogued in
[numerical-backend-choices.md](numerical-backend-choices.md).

Section 4 also supplies the debt/tick accounting and the bounded
objective argument. The present general-gap proof replaces the source
perfect matching by any comparison matching with K additional edges.
The symmetric difference supplies the same number of disjoint
augmenting paths. The exact derivation and driver are in
[general-graph-gap-reduction.md](general-graph-gap-reduction.md).

[deterministic-phase-cost-and-guards.md](deterministic-phase-cost-and-guards.md) gives the complete phase sum:
local positivity, objective losses, large tick jumps, all local and
global integral resets, nominal lifetime sizes, and first-failure
guard adequacy. That generic composition states the numerical interfaces
it uses. For the four-fifths matching theorem, those interfaces are
instantiated by the explicit local constructions in
[Theorem 11.6](../../problems/general-matching/proof.md#116-deterministic-cycle-search-realization):
raw cycle quality, chronological repair, occurrence retirement, finite
bit bounds, and parameter-uniform routing all have named suppliers.

## 6. Components supplied by this checkpoint

The main additions are the actual persistent integral allocation
carrier, retained zero edges, implicit canonical assignments, frozen
event overlays, deterministic local tight discovery and pair exchange,
the two constructive raw numerical routes, the direct optimum-gap
reduction, and the independent-check uniformization.

These constructions establish the deterministic mathematical branch using
the named public results and the reconstructed local proofs. The full
dependency closure and its parameter substitution are stated in
[the matching theorem, Sections 11.6–12](../../problems/general-matching/proof.md#116-deterministic-cycle-search-realization).
The finite first-failure interleaving obtains its improved time bound
from that favorable proved parameter choice. Its final matching verifier
separately guarantees that only an exact output is returned.

These are research proofs available for review; external peer review and
formal verification are separate forms of evidence. Executable coverage
is likewise a separate question: the repository's
[ordinary polynomial reference solver](../../problems/general-matching/reference/README.md)
implements exact matching and independently checked certificates, while
the fast construction is specified by the mathematical proof. Absence of
that fast executable is not an additional hypothesis of the theorem.
