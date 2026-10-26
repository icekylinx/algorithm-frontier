# Root audit of the any-source fixed-tree matching interface

**25 October 2026. Local constructive interface accepted after root and
independent mathematical audits.**

Audited construction: [any-source-fixed-tree-matching-interface.md](any-source-fixed-tree-matching-interface.md).
Independent audit: [any-source-fixed-tree-matching-independent-audit.md](any-source-fixed-tree-matching-independent-audit.md).
The operative version builds its tree using the same persistent
conservative donor prices that its search maintains. The earlier
true-price potential certificate remains a separate valid interface;
its potential and LOW threshold must not be mixed with this version.

This lemma closes search, implicit path updates, and price-event
discovery inside a supplied fixed threshold forest. It does not bound
the total cost of creating or repairing those forests, so it supplies
no exact general-matching exponent below four-fifths.

## 1. Operative prices and the initialization correction

For every live allocation x_e retain a register ell_e with
ell_e<x_e<2ell_e. Set ell_e=3x_e/4 on initialization or reset.
Use donor cost

$$
\bar c_e=\left\lceil\frac{H}{4\ell_e}\right\rceil,
$$

zero receiving cost, and source cost A-sigma_v, where

$$
\sigma_v=\left\lfloor\frac{3H}{4s_v}\right\rfloor,
 \qquad
 \tau_v=\left\lceil\frac{5H}{4s_v}\right\rceil.
$$

The supplied exact shortest-path tree is computed in this bar-price
graph. Removing its artificial source leaves a directed forest with
old labels D, and every receiving forest arc is D-tight. Registers
are reused across epochs; they belong to coordinate lifetimes.

An earlier draft instead built the tree with the smaller true donor
ceilings and searched with the larger register ceilings. That was a
valid local search lemma but did not ensure that a fresh tree would
contain a passing path. The operative same-price initialization closes
that mismatch. It is not enough to assert that an arbitrary global
good path belongs to a shortest tree built with different prices.

## 2. Threshold correctness and actual primal motion

For any ancestor bin a and descendant bin b, let bar L be the sum
of donor costs on their directed forest path. Accept if
sigma_a-tau_b-bar L>0. Since

$$
\frac{H}{4x_e}\le\bar c_e<\frac{H}{2x_e}+1,
$$

every accepted path has true one-sided ratio greater than one quarter.
Conversely every forest path whose true ratio exceeds one half passes
the conservative integer test when
H min_v(1/s_v)>=8(N+2). The margin after the factor-two donor
bound exceeds (alpha_a+alpha_b)/4, and the source, terminal, and
simple-path ceilings lose at most N+2 integer units.

The path decreases each donor allocation and increases each receiver
allocation by the same eta. It increases s_a and decreases s_b by
eta. Every internal row and bin has zero net imbalance. Thus the
existing allocation and slack equations are respected exactly.

Define V_up=alpha_a+alpha_b+4 bar L/H. Acceptance gives
alpha_a-alpha_b>V_up/4. A guarded-grid step with
1/512 <= eta V_up <=1/256 keeps every donor and terminal positive
and increases the slack-log objective by an absolute positive constant.
The fixed fine dyadic grid is selected from a known polynomial upper
bound on V_up; no growing denominator or exact-real operation is
assumed.

## 3. The fixed old potential remains feasible

A donor tree incidence only decreases in allocation, so its register
cost cannot decrease during the epoch. A receiving incidence only
increases. Its reverse donor cost can decrease after a reset, but the
receiving arc is tight in the fixed old D, so that reverse arc still
has nonnegative reduced cost. The two orientations of an allocation
incidence cannot both belong to the directed tree, since that would
be a directed cycle. The update therefore cannot silently decrease
another maintained donor tree price.

The starting source cost increases. For the terminal,

$$
D(b)\le D(a)+\bar L\le A-\sigma_a+\bar L<A-\tau_b.
$$

This uses only source feasibility at a, not tightness of its source
arc. It is consequently valid for a newly chosen intermediate source.
The terminal source arc has margin at least H/(2s_b), and the small
step plus its one-unit rounding allowance cannot consume that margin.
All old labels remain feasible for the bar-price graph.

Acceptance also gives alpha_a>5alpha_b/3. The small step leaves the
new terminal reciprocal below the old starting reciprocal. Hence the
global maximum reciprocal cannot increase, and the same nonnegative
source offset A remains valid within the structural epoch.

## 4. A compatible semantic certificate and fresh progress

Put pi=(A-D)/H. Feasibility in the operative graph implies

$$
0\le\pi_d-\pi_r\le\frac1{2x_e}+\frac1H,
 \qquad
 \pi_d\ge\frac3{4s_d}-\frac1H.
$$

For a feasible matching comparison, use the already established
P>12N, Q_s<=N, and Q_x<=3N. Conservation and the preceding inequalities
give

$$
\frac34P-\frac54Q_s-\frac12Q_x
  \le E(\pi,s)+\frac{L|R|+T_{\rm slack}}H,
 \qquad
 E(\pi,s)=\sum_d(s_d\pi_d-5/4)_+.
$$

The left side is strictly larger than 25N/4. Choose H also so that
the rounding term is at most N. Then E<=5N safely certifies matching
LOW. This is the half-price certificate appropriate to the bar-price
tree. The earlier true-price potential uses a different donor bound
and the separate E<=6N threshold.

For a freshly initialized bar-price tree, suppose no original
source-child-to-bin path passes. Exact tree equality then gives
D(b)>=A-tau_b for every bin. Thus pi_b<=tau_b/H and
E<=T_slack/H<=N. A fresh TREE-EMPTY answer therefore implies LOW.
Equivalently, a fresh tree with E>5N contains a passing path. This
does not assert progress after an arbitrary later exhaustion without
paying for a repair or refresh.

The scalar E has a common fixed rational denominator from the
primal grid and H. A path step changes only its two endpoint slack
terms. It can be maintained exactly without summing unrelated rational
reciprocals. Rebuilding pi requires charging its changed terms.

## 5. The max-plus data structure finds all eligible tree paths

For each node v, M_v stores the best negative terminal price minus
distance to a descendant bin. F_v stores the best complete threshold
margin over ancestor/descendant bin pairs in its subtree. The
recurrences in the main note distinguish a pair entirely within a
child subtree from a pair whose source is v. They do not admit
incomparable vertices in separate branches.

A static heavy-light decomposition represents each node's recurrence
as a 3-by-3 max-plus matrix. Balanced products along heavy paths and
ordered dictionaries for light-child summaries permit a source price,
terminal price, or tree donor-price change in O(log^2 nu) operations,
where nu is the supplied forest size. A propagated change travels
through at most logarithmically many light edges.

Witness metadata stores the chosen bin pair. A head's witness may
change when its numerical maximum ties, so the implementation
propagates changed value-and-witness summaries, not only changed
numeric values. This clarification closes a stale-witness possibility.
Retrieving a pair does not enumerate its path; the fixed forest gives
its implicit representation.

## 6. Lazy path changes, guards, and notifications

On a donor tree edge store buffer x-ell; on a receiver tree edge store
buffer 2ell-x. Both decrease by eta under a path transfer. The path
is a logarithmic number of heavy intervals, so lazy range addition
and a range minimum discover every nonpositive buffer. Its exact
current x is recovered from the old register and role. Resetting
ell=3x/4 leaves a positive buffer and changes the max-plus price only
for a donor role.

Guard detection is explicit and separate. Additional path minima store
x-chi for donors and U_guard-x for receivers; these also decrease by
eta. Endpoint slack guards are checked directly. A proposed step
crossing a guard reports a minimizing coordinate and ends the epoch
for the already declared repair. Register thresholds alone would not
detect an arbitrary guard boundary.

Each coordinate reset consumes at least a constant absolute logarithmic
variation: since its last reset, x fell to at most three quarters of
its previous reset value or rose to at least three halves. This
hysteresis prevents boundary chatter. Every accepted numerical step
has O(1) aggregate negative allocation-log variation. Summing log x
as an accounting potential, with the guarded range and explicit
structural record edits, bounds total positive variation too. Therefore
the total notification count across all epochs is

$$
O(J+(N+A_{\rm ext})\log S).
$$

Here J is the number of accepted steps and A_ext counts all explicitly
born, deleted, or externally set allocation records. Existing registers
are not reset merely because a tree is rebuilt or an incidence changes
its tree role. Values can be materialized when an epoch ends, but that
linear work is part of rebuilding, not a free notification operation.

## 7. Exact achieved interface and the remaining research task

After a fixed threshold tree is supplied, initialization is
nu polylog(S). Each numerical step, empty-search decision, and
certificate update has polynomial logarithmic cost plus its actual
notifications. The searches include every ancestor-to-descendant bin
path; accepted paths have true ratio greater than one quarter, and
an empty search excludes true ratio greater than one half within that
forest. All updates preserve the operative old potential. Fresh
initialization cannot produce TREE-EMPTY while its semantic certificate
is still above LOW.

What is not bounded is the total work of supplying and initializing
new forests when an old one becomes empty with E>5N. The global
notification bound does not pay that work. The root-only obstruction
in [root-only-sp-tree-epoch-counterexample.md](../mechanism-boundaries/root-only-sp-tree-epoch-counterexample.md) shows why one simpler
epoch rule fails, and the present any-source interface escapes that
example; it does not prove a general refresh amortization.

No accepted matching exponent changes until the remaining repair cost
and all guarded structural edits are charged in a complete algorithm.
