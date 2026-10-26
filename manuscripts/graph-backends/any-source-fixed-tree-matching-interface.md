# Any-source searches in a fixed matching threshold forest

**Research lemma, 25 October 2026. Root and independent mathematical
audits completed for the operative conservative-price version.**

This note constructs a useful part of the slack-only matching interface.
Within one fixed shortest-path-tree epoch, it finds a threshold-passing
path from any bin to a descendant bin, applies its allocation changes
implicitly, and discovers the necessary price updates. It preserves the
old feasible distance labels. Persistent hysteretic registers give a
price-event bound across epochs.

The number and construction cost of new shortest-path-tree epochs remain
unbounded by this lemma. Consequently it does not improve the current
four-fifths exact general-matching theorem. It does not require the
separate root-only epoch obstruction as a prerequisite.

The allocation equations, guarded common dyadic grid, slack comparison,
and semantic potential screen are those of
slack_only_one_sided_matching_client.md and
slack_potential_semantic_certificate.md. Guard repairs and structural
ledger changes end the current epoch and are explicitly charged events.
No polynomial lower bound on an allocation is inferred merely from
removing its logarithm from the objective.

## 1. A fixed directed forest and the search problem

At the beginning of an epoch, initialize or reuse the persistent
registers from Section 2 and build an exact integer shortest-path tree
from the artificial threshold source in their conservative price graph.
Ordinary receiving arcs have length zero and donor arcs have length

```math
\bar c_e=\left\lceil\frac{H}{4\ell_e}\right\rceil.
 \tag{1}
```

The source arc to bin v has length A-sigma_v, where

```math
\sigma_v=\left\lfloor\frac{3H}{4s_v}\right\rfloor,
 \qquad
 \tau_v=\left\lceil\frac{5H}{4s_v}\right\rceil,
 \qquad A\ge\max_v\sigma_v.
 \tag{2}
```

H is a fixed power-of-two integer of polynomial magnitude satisfying

```math
H\min_v(1/s_v)\ge8(N+2).
 \tag{3}
```

It also satisfies (L times the number of rows plus total slack)/H
at most N, as required by the conservative semantic certificate in
Section 6.1. Guarded polynomial upper bounds permit one fixed choice
of H satisfying both requirements throughout the numerical interval.

The epoch has no structural ledger changes. Its guarded primal values
have O(log S) bits, for a fixed polynomial history scale S. Let D be
the exact old integer labels.

Delete the artificial source and its tree arcs. The remaining object
is a rooted directed forest T, oriented from each source-child bin
toward its descendants. Tree incidences alternate between donor
bin-to-row arcs and receiving row-to-bin arcs. Every receiving tree
arc is tight in D. D and this forest topology stay fixed during the
epoch.

Unlike a root-only rule, permit any bin a as the starting vertex.
For any descendant bin b, use the directed T-path from a to b,
increase s_a and decrease s_b by the same amount. Each internal row
loses that amount on its incoming donor and gains it on its outgoing
receiver; each internal bin has zero net load change. Thus all ledger
conservation equations are respected.

Every allocation incidence occurs at most once in the tree. In
particular, a receiving tree arc and the reverse donor arc of the
same incidence cannot both be tree arcs: that would be a directed
two-cycle. Increasing a receiving allocation therefore changes no
other donor edge of the maintained directed forest.

## 2. Persistent conservative donor registers

For each live allocation coordinate retain a dyadic lower register
ell_e satisfying

```math
\ell_e<x_e<2\ell_e.
 \tag{4}
```

Initially, and at a reset, set ell_e=3x_e/4 exactly. The two extra
denominator bits are fixed; they do not accumulate with resets.
After a numerical update, reset whenever x_e<=ell_e or x_e>=2ell_e.
This keeps (4) in each settled numerical state.

The maintained donor length on a donor tree incidence is

```math
\bar c_e=\left\lceil\frac{H}{4\ell_e}\right\rceil.
 \tag{5}
```

Receiving tree arcs still have length zero. The two useful inequalities
are

```math
\frac{H}{4x_e}\le\bar c_e
       <\frac{H}{2x_e}+1.
 \tag{6}
```

Within an epoch, each tree donor allocation only decreases. Its
register resets downwards and its maintained donor cost cannot
decrease. Each tree receiving allocation only increases; its register
may reset upwards, but the tree length of that receiving arc remains
zero. The decreasing reverse donor price is outside T.

The registers belong to allocation-coordinate lifetimes, not to tree
epochs. Rebuilding T does not reset a register that already satisfies
(4). This distinction is needed for the history-wide event count.

## 3. The finite-word threshold test

For an ancestor bin a and descendant bin b, let

```math
\bar L(a,b)=\sum_{e\text{ donor on }T[a,b]}\bar c_e.
```

The maintained search accepts precisely when

```math
\sigma_a-\tau_b-\bar L(a,b)>0.
 \tag{7}
```

All quantities in (7) are integers. By the directions of rounding,

```math
\frac34\alpha_a-\frac54\alpha_b
       >\frac{\bar L(a,b)}H
       \ge\frac14\sum_{e\text{ donor on }T[a,b]}\frac1{x_e},
 \qquad \alpha_v=1/s_v.
```

Consequently every accepted path has true one-sided ratio greater
than one quarter. This is a sufficient acceptance test, not a
replacement of a lower bound by an optimistic stale price.

It also detects every path in T whose true ratio exceeds one half.
Such a path satisfies

```math
L_x(a,b)<\alpha_a-3\alpha_b.
```

Using (6), its unrounded conservative margin is greater than

```math
\frac34\alpha_a-\frac54\alpha_b-\frac12 L_x(a,b)
          >\frac14(\alpha_a+\alpha_b).
 \tag{8}
```

The source floor, terminal ceiling and donor ceilings lose at most
N+2 integer units. Condition (3) leaves a strict positive margin in
(7). Thus a negative answer means that T contains no direction of
true ratio greater than one half. It does not assert the absence of
such a path elsewhere in the directed allocation graph.

## 4. A concrete max-plus tree dynamic program

The following data structure avoids a separate shortest-path query
from each possible starting bin. Write c(v,u) for the maintained
nonnegative integer length of a directed tree edge v to u. For every
vertex v define

```math
\begin{aligned}
 M_v&=\max_{\substack{b\text{ a bin}\\b\in T_v}}
           \{-\tau_b-\mathrm{dist}_{\bar c}(v,b)\},\\
 F_v&=\max_{\substack{a,b\text{ bins in }T_v\\a\text{ ancestor of }b}}
           \{\sigma_a-\tau_b-\mathrm{dist}_{\bar c}(a,b)\}.
\end{aligned}
\tag{9}
```

Missing candidates have value minus infinity. A bin is its own
descendant, but its self-pair has sigma_v-tau_v<0, so it never passes
(7). The maximum F at the forest roots is exactly the desired search
value. Every maximizing entry also stores its target bin or pair of
bins.

Choose an ordinary static heavy-light decomposition of T. Let h(v)
be the heavy child. Put sigma_v=-infinity for a row, and define

```math
\begin{aligned}
 z_v&=\max\left\{-\tau_v\ \text{if v is a bin},\
       \max_{u\text{ light child}}\{M_u-c(v,u)\}\right\},\\
 q_v&=\max_{u\text{ light child}}F_u.
\end{aligned}
```

For a missing heavy child use input M_h=F_h=-infinity. The recurrences
are

```math
\begin{aligned}
 M_v&=\max\{z_v,M_h-c(v,h)\},\\
 F_v&=\max\{F_h,q_v,\sigma_v+M_v\}.
\end{aligned}
\tag{10}
```

These are a constant-size max-plus transformation on (M_h,F_h,0).
Its matrix is

```math
\begin{pmatrix}
 -c(v,h)&-\infty&z_v\\
 \sigma_v-c(v,h)&0&\max\{q_v,\sigma_v+z_v\}\\
 -\infty&-\infty&0
\end{pmatrix}.
\tag{11}
```

At a terminal heavy-path vertex, terms depending on its absent
child are simply disabled. Store the matrix product along each
heavy path in a balanced segment tree. For the light children of
each vertex, retain deterministic ordered dictionaries for the two
maxima defining z_v and q_v.

A source/terminal price edit changes one matrix. An edge-cost edit
either changes its parent's heavy coefficient or one light-child
dictionary key. Recompute that heavy path's product and head values.
The head state includes its numerical values and its maximizing
target/pair metadata, with deterministic tie keys. If either changes,
update the corresponding light-child keys and metadata at its parent
and continue upward; alternatively, propagate unconditionally along
the affected heavy-head chain. Numerical equality alone is not a
reason to retain an obsolete witness. A root-to-leaf route crosses at
most O(log |T|) light edges, so one endpoint-price or tree-edge-price
edit costs O(log^2 |T|) deterministic operations.

Witness metadata has constant size. A coefficient from an external
M input to an F output stores its chosen internal source bin; an
M constant stores its target bin; an F constant stores its pair.
Composing the first two forms creates a pair. A propagated F input
already carries its pair. Thus matrix multiplication carries the
maximizing pair without recursively expanding a long tree path.
The returned witness is the two current bin IDs a,b; its path is
represented by the fixed forest and is not enumerated.

This explicitly handles ancestor restrictions. It is not a maximum
over arbitrary ordered pairs in different branches.

## 5. Implicit allocation updates and the watcher

Use the same static heavy-light decomposition for path data. Index
each edge at its child vertex. A path from ancestor a to descendant
b is a union of O(log |T|) heavy-path intervals, excluding a's edge
to its parent.

On an epoch donor edge retain the watched buffer
w_e=x_e-ell_e. On an epoch receiving edge retain
w_e=2ell_e-x_e. Under a positive path transfer eta, both types of
watched buffer decrease by eta:

* the donor allocation decreases by eta;
* the receiving allocation increases by eta.

Thus a single lazy range-add field suffices for all watched buffers.
Store their minimum, and search for a nonpositive buffer after the
path update. At such a point, recover its exact current allocation
from its type and its old register, reset ell_e=3x_e/4, and set the
new buffer to x_e/4 for a donor or x_e/2 for a receiver. A donor
reset updates (5) in the max-plus structure. A receiver reset changes
no tree price. Repeat until all affected intervals have positive
buffers.

All point records and lazy offsets are on the original common
dyadic grid or its fixed four-times finer extension. No sum of
unrelated rational reciprocals is required by this watcher.
The path data structure also maintains the integer sum of donor
costs (5). Querying that sum and applying the lazy update cost
polynomial logarithmic time, plus the number of reported resets
times polynomial logarithmic time.

Guard discovery is explicit as well. For fixed epoch lower/upper
guards chi_e and U_e, retain a second path-minimum field equal to
x_e-chi_e on a donor edge and U_e-x_e on a receiving edge.
Both fields decrease by eta under the path transfer. Before applying
a proposed eta, compare it with this path minimum; its minimizing
edge is a concrete witness if the step would cross a guard. Equivalent
separate donor-minimum and receiver-maximum fields work when the
guards are uniform. The two endpoint slack guards are checked
directly. Thus stopping for a guard event does not assume a free
scan of the implicit path.

Every current coordinate value remains retrievable. When an epoch
ends, its current tree coordinates may be materialized in linear
time, or queried on demand when initializing the next graph. That
cost belongs to rebuilding the epoch and is not claimed to be free.

## 6. Safe finite-grid steps and old-potential feasibility

For an accepted pair define

```math
V_{\rm up}=\alpha_a+\alpha_b+4\bar L(a,b)/H.
 \tag{12}
```

It upper-bounds the true one-sided charge. The integer acceptance
also gives G=alpha_a-alpha_b>V_up/4. Choose a common dyadic step
on the guarded primal grid such that

```math
\frac1{512}\le\eta V_{\rm up}\le\frac1{256}.
 \tag{13}
```

These are beta/128 and beta/64 for beta=1/4. The existing guard
range and a finer fixed dyadic implementation grid ensure the
interval contains a legal positive step. If a guard repair would
be needed, stop the epoch and execute that explicitly charged
repair; (13) is not used to assert that coordinates can remain
above a polynomial floor forever without intervention.

For specificity, if all primal values lie between S^{-c} and S^c
for a fixed c and N<=S, then (6) gives a fixed polynomial upper
bound V_max on (12), for example 8(N+1)S^c after increasing the
constant for the finite initial cases. Choose the common primal
dyadic grid spacing delta at most 1/(4096 V_max) once. The interval
in (13) has width at least 1/(512 V_max), so it contains a grid
multiple, computable by exact integer division. Its description
still has O(log S) bits. Registers use the fixed grid delta/4.
Equation (12) contains only two slack reciprocals and one integer
path sum divided by H; combining these few denominators also uses
O(log S)-bit arithmetic. The guard path minimum just described
is checked before that proposed grid step is committed.

Every donor and terminal slack changes by less than one part in
256 of its old value, because each corresponding reciprocal is a
term of V_up. All values remain positive. The row and bin equations
hold exactly. The slack objective increases by an absolute constant:

```math
\begin{aligned}
 \Delta\Phi
 &=\log(1+\eta\alpha_a)+\log(1-\eta\alpha_b)\\
 &\ge\eta G-2(\eta V_{\rm up})^2
 \ge\frac18\,\eta V_{\rm up}>0.
\end{aligned}
\tag{14}
```

The old D remains feasible for the current conservative integer
threshold graph (1). On an ordinary donor, its register cost can
only increase. On an ordinary receiver, an upward register reset
can decrease the reverse donor cost, but that decrease is safe
because its receiving arc is D-tight. Other ordinary incidences
do not change. This statement concerns the conservative graph in
which D was computed; its semantic screen is derived in Section 6.1.

The start's source cost increases. For the terminal, feasibility of
D before the step and the conservative costs give

```math
D(b)\le D(a)+\bar L(a,b)
       \le A-\sigma_a+\bar L(a,b)<A-\tau_b.
 \tag{15}
```

Thus the old source slack at b is more than tau_b-sigma_b, at least
H/(2s_b). The small terminal slack change in (13), including the
one-unit rounding allowance, decreases that source cost by less
than this amount. The argument is identical for a starting bin
whose old source arc was not tight.

Acceptance implies alpha_a>(5/3)alpha_b. The small step keeps the
new alpha_b below the old alpha_a, while alpha_a itself decreases.
The global maximum reciprocal therefore never increases and the
same A remains a valid nonnegative offset.

The fixed semantic certificate below continues to use feasible
old labels. A path step changes just its two endpoint slack terms,
so its exact dyadic maintenance remains cheap. After an epoch has
evolved, TREE-EMPTY and semantic LOW are separate outcomes.

### 6.1 A semantic certificate for the conservative price graph

Put pi_v=(A-D(v))/H. Feasibility, (4)--(6), and source rounding give

```math
0\le\pi_d-\pi_r\le\frac1{2x_e}+\frac1H,\qquad
 \pi_d\ge\frac3{4s_d}-\frac1H.
 \tag{16}
```

Define the exactly maintainable dyadic quantity

```math
E=\sum_d(s_d\pi_d-5/4)_+.
 \tag{17}
```

For any feasible comparison h, let P be its positive normalized
slack mass, Q_s its negative normalized slack mass, and Q_x its
one-sided negative allocation charge. Conservation and (16) yield

```math
\sum_d\pi_d h_{s_d}
       =-\sum_e(\pi_d-\pi_r)h_e
       \le\frac12 Q_x+\frac{L|R_{\rm rows}|}{H}.
```

On positive slack changes the source inequality in (16) applies.
On a negative slack change, its absolute amount is at most the
current s_d; hence its excess above 5/(4s_d) is paid by (17).
The total positive absolute slack change is at most the fixed
total slack T_slack. Consequently

```math
\frac34P-\frac54Q_s-\frac12Q_x
       \le E+\frac{L|R_{\rm rows}|+T_{\rm slack}}H.
 \tag{18}
```

The genuine matching comparison has P>12N, Q_s<=N and Q_x<=3N.
The left side of (18) is therefore greater than 25N/4.
Choose H so that the displayed rounding error is at most N.
Then that matching comparison would force E>21N/4. In particular,

```math
E\le5N
 \tag{19}
```

is a safe semantic LOW screen for this conservative graph.
The six-N screen proved elsewhere for a potential with donor bound
1/(4x)+1/H is not substituted here: (16) has the different
coefficient one half.

The nonnegative part in (17) uses only a dyadic slack times the
integer-based fixed pi value. It has the common denominator from
H and the fixed primal grid. Updating the two endpoint terms is
finite-word work. Row potentials can again be normalized upward
to the minimum neighbouring bin potential without changing E or
violating (16); this optional normalization is unnecessary for the
fixed-tree implementation.

### 6.2 Fresh initialization is a complete static step

At fresh initialization, T is an exact SPT of the same conservative
prices used by the search. Suppose its search is TREE-EMPTY.
For any bin b, let a be the first bin on its exact source-tree
path. That root-to-b path is among the tested ancestor paths, so

```math
D(b)=A-\sigma_a+\bar L(a,b)\ge A-\tau_b.
```

Thus pi_b<=tau_b/H<=5/(4s_b)+1/H, which gives

```math
E\le T_{\rm slack}/H\le N.
 \tag{20}
```

Fresh TREE-EMPTY therefore immediately implies semantic LOW.
Otherwise a current passing path is available. Equivalently, a
global true-ratio-above-one-half comparator passes the conservative
test by Section 3, and an exact conservative SPT finds a path at
least as good for that threshold.

This closes the initialization-to-search interface. It would not
follow merely from building a different, lower-priced SPT and then
testing its paths using the conservative costs. The construction
in this note uses the same register graph throughout.

## 7. Register events admit a history-wide charge

At a reset, ell=3x/4. Until its next reset, x must either fall to at
most three quarters of that reset value, or rise to at least three
halves of it. Hence every later reset consumes at least a fixed
positive amount of absolute logarithmic variation of this coordinate.
There is no chatter from crossing an unbuffered dyadic boundary.

For one fixed coordinate lifetime, the reset count is bounded by
one plus a constant times its total absolute log variation. Summing
over coordinate births and explicitly changed structural records
gives the same statement for the whole run, not just one epoch.
Existing registers are reused when a coordinate changes its tree
role after a refresh.

For one accepted numerical step, total negative log variation of
allocations is at most

```math
2\eta\sum_{\rm donors}1/x_e
      \le2\eta V_{\rm up}=O(1).
 \tag{21}
```

Summing log x only as an accounting potential gives total positive
variation at most total negative variation plus
O((N+A_ext) log S), where A_ext counts explicitly born, deleted
or set allocation records. This is the prior one-sided variation
lemma, now coupled to an actual threshold-discovery structure.
Accordingly the total numerical register reset count is

```math
O(J+(N+A_{\rm ext})\log S)
 \tag{22}
```

over J accepted steps, independently of the number of epochs.
An externally set value can reset its register directly; that is an
explicit structural record event. Reversing an incidence's tree role
does not, by itself, reset its register.

The factor O(N) needed to build a new SPT or initialize its heavy-light
and max-plus representation is not a price event and is not bounded
by (22).

## 8. Exact achieved interface and the remaining bottleneck

For one fixed old exact conservative threshold forest on nu row/bin vertices,
initialization takes nu polylog(S) work after the SPT is supplied.
A numerical step costs polynomial logarithmic work plus that of its
reported register resets. The search either returns a current
ancestor-to-descendant bin path of true ratio above one quarter or
certifies that this forest contains no path of true ratio above one
half. Each accepted path is applied implicitly and preserves the old
feasible labels. Finite-word arithmetic uses O(log S)-bit values
under the explicit guarded-range import.

At fresh initialization it either returns such a path or satisfies
the stronger bound (20), which safely terminates the numerical
search as LOW. The stronger search can continue from intermediate bins that the
literal root-only rule omits. It still does not search ordinary arcs
outside the fixed forest. The genuine matching comparator may need
those arcs after this forest is exhausted. An E-based semantic LOW
certificate can sometimes terminate without a refresh, but no bound
has been proved on the remaining refreshes.

The next sufficient result would therefore bound the total cost of
creating or repairing potential-compatible forests when this search
is empty and the semantic certificate remains above its LOW threshold.
It must pay the actual SPT/DP construction work, not just the now
globally bounded register notifications. That question remains open.

The operative conservative-price version is checked in
[any-source-fixed-tree-matching-independent-audit.md](any-source-fixed-tree-matching-independent-audit.md) and
[any-source-fixed-tree-matching-root-audit.md](any-source-fixed-tree-matching-root-audit.md). These are internal
mathematical and data-structure audits, not formal verification,
external review, or implementation benchmarks.

