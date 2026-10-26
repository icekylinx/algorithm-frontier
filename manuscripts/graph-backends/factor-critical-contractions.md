# Minimal tight contractions and explicit factor-critical witnesses

**A self-contained combinatorial component of the current construction.**
This note proves the factor-critical contraction and materialization
facts used by the row/bin state. The organization follows the role of
these witnesses in OAI Section 3, but the Hall arguments and the complete
local reconstruction are given here. No new publication-priority claim
is made.

Primary source for the row/bin framework:

<https://github.com/openai/math/blob/main/preprints/Almost-Linear-Time-Maximum-Cardinality-Matching-in-Sparse-General-Graphs-September-24-2026/build/sections/03-matching-state.tex>.

## 1. Setting

Bins are disjoint odd physical vertex sets. Bin d has weight
w_d=(|d|+1)/2 and a constructive factor-critical witness: after any
one physical vertex of d is designated as exposed, all other vertices
of d can be matched internally. Initially bins are singletons.

Rows are distinct physical singleton vertices outside the bins. Their
incidences list all physical edges to bins, keeping edge IDs and
physical contact endpoints. Each row has at most three incidences.
Let N(r) be the corresponding set of bin neighbors. There is an
injection mu assigning each row to an incident bin.

For a bin set Y write

    R(Y) = {r : N(r) is contained in Y},
    h(Y) = |Y|-|R(Y)|.

Assume strict Hall surplus h(Y)>=1 for every nonempty Y. A set is
tight when h(Y)=1. Let i,j be distinct bins with a physical edge e
between them. Suppose X is the inclusion-minimal tight set containing
i and j. Put R_X=R(X), so |R_X|=|X|-1.

The proposed contracted bin contains all bins in X and all singleton
rows in R_X. Its weight is w(X), because its physical size is

    sum_(d in X)(2w_d-1) + (|X|-1) = 2w(X)-1.

## 2. Exposing a physical vertex inside a child bin

Fix d in X. There is an injection of every row in R_X into X without d.
To prove this using ordinary bipartite Hall, take any nonempty row
subset S of R_X and put Y=N(S). All rows of S are captive in Y, so

    |Y| >= |R(Y)|+1 >= |S|+1.

Removing d from the available bins leaves at least |S| neighbors.
Hall's condition therefore holds. The empty row subset is harmless.

Given a desired physical exposure v in d, choose such an injection.
Expose v inside d. In every other child bin, expose the endpoint of
its assigned row edge, use that edge to match the row, and use the
child's factor-critical witness on the remaining vertices. Every
physical vertex of the union except v is matched.

## 3. Exposing a swallowed row

Fix r in R_X. We claim that the remaining rows R_X without r can be
injected into X without i and j.

If Hall failed, some nonempty S contained in R_X without r would have

    |N(S) without {i,j}| < |S|.

Strict Hall as above gives |N(S)|>=|S|+1. Removing only two bins can
cause this failure only if BOTH i,j belong to N(S) and
|N(S)|=|S|+1. Moreover S is contained in R(N(S)); strict Hall forces
equality |R(N(S))|=|S|. Thus N(S) is tight and contains i,j.

But |S|<=|X|-2, so |N(S)|<=|X|-1. This is a proper tight subset of X
containing i,j, contradicting the minimality of X. The desired injection
therefore exists.

Use e to match the specified physical endpoints in bins i and j.
Assign and match each remaining row into its designated child bin.
Each child bin exposes exactly its incident row or joining-edge contact
and uses its factor-critical witness internally. Only r remains
unmatched. Together with Section 2, this proves that the entire
contracted bin is factor-critical.

Minimality of X is essential in this second argument. Contracting an
arbitrary tight superset containing i,j would not be justified by the
same proof. The deterministic tight-set routine returns the required
minimal set, rather than only a maximal tight block.

## 4. Preserving the surrounding assignment

The old injection assigns the |X|-1 captive rows to that many distinct
bins in X. At most one remaining row can therefore be assigned into X.
Delete the captive rows from the outer assignment. If an exterior row
was assigned into X, retain its physical incidence and assign it to
the new bin. All other exterior assignments are unchanged.

This is still an injection. The new bin's factor-critical witness can
expose the retained physical contact, so the represented physical
matching has the same cardinality as before contraction. If no exterior
row was assigned into X, the new bin has one unmatched exposure, again
preserving cardinality.

New physical row-bin incidences can appear when previously external
rows have edges to swallowed rows. Those incidences must be recorded
by the state and ledger update, but they do not invalidate this
factor-critical proof or the preserved assignment: the proof already
uses a subgraph of the actual contracted physical block.

## 5. A compact creation-time record

At contraction create one immutable record containing:

* pointers to its |X| child-bin records;
* its |X|-1 captive physical row vertices and all their at-most-three
  physical contact incidences into those children;
* the joining edge e, with its two physical endpoints and child IDs;
* the captive assignment restricted from the CURRENT precontraction
  injection.

The last assignment covers all but one child. It remains a creation-time
witness even if later settled states use a different implicit global
assignment. Capture it by point queries while the pre-event version
and overlay are available. Its size and construction cost are
O(|X| polylog N), independent of the children's physical sizes.

The representation does not precompute a separate matching for every
possible exposure. It stores enough information to reconstruct one
when the bin is actually dissolved.

## 6. Materialization with any prescribed exposure

Work at one contraction record and copy its small stored captive
assignment into temporary local dictionaries.

If the prescribed exposure lies in child d, forbid d and remove the
assignment into d if one exists. At most one captive row becomes
unmatched. Section 2 guarantees that all captives can be matched into
the remaining children. Hence one ordinary bipartite augmenting-path
search repairs the local assignment; no search is needed if d was
already the unused child. Give d its prescribed exposure and give each
other child its assigned row's physical contact as its exposure.

If the prescribed exposure is a captive row r, remove r and its
assignment. Reserve i,j for the joining edge and remove any remaining
assignments into those children. At most two remaining rows become
unmatched. Section 3 guarantees a complete injection into the other
children, so at most two ordinary bipartite augmentations suffice.
Give i,j the contacts of e, and every other child the contact of its
assigned row. Leave r unmatched.

Each local search scans an abstract bipartite graph with O(|X|) records,
because rows have degree at most three. Each child receives exactly one
exposure and is recursively materialized once. These are ordinary
bipartite matching searches on the record, not a general-graph solve.

## 7. Total work of dissolving a bin

The record structure of one active bin is a tree. At a contraction of
arity k>=2 it has k child-bin records and k-1 swallowed singleton row
leaves. Child bins are physically disjoint. The singleton base bins and
swallowed rows supply the physical leaves. Thus total record arity is
linear in the bin's physical size; unary contraction chains are absent.

One initial traversal assigns contiguous physical-leaf intervals to
records. The interval of a prescribed physical endpoint identifies its
direct child with logarithmic dictionary/search overhead. Internal
node searches, exposure lookups and recursive visits therefore take
O(|bin| polylog N) total work.

Distinct active roots have disjoint physical leaves and can be dissolved
within the sum of their sizes. A saved record is not repeatedly expanded
merely because the outer injection changes: internal exposure is lazy.
On a true erasure or a phase boundary each active record is dissolved
once. If vertices later return to new bins, their new lifetimes and
record creation are charged to the new structural actions.

This proves the factor-critical and output-materialization component
needed by [Deterministic Exact General Matching through Persistent Integral Carriers and Normalized Routing](../../problems/general-matching/proof.md). The separate ledger,
projection, numerical progress and total erased-volume arguments remain
necessary for the complete fast-time theorem.
