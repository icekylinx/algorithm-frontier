# A maintained potential certificate for the slack-only matching client

**Independent mathematical audit, 25 October 2026.** The certificate below
is valid for the top matching ledger, including conservative finite-word
prices. It is stronger than requiring every individual directed threshold
test to fail. A fixed old shortest-path tree also supports a monotone
numerical epoch. Neither result supplies a bound on the number of tree
refreshes, and no matching exponent below `4/5` is claimed.

The primal model and comparison theorem are those in
`slack_only_one_sided_matching_client.md`. This note records a proposal from
the root agent and an independent proof, including its exact scope.

## 1. Model and the matching comparison margin

At a fixed structural state let `R` be the rows, `D` the bins, and let

\[
 \sum_{e\ni r}x_e=L,\qquad
 \sum_{e\ni d}x_e+s_d=b_d,
 \qquad b_d=L+p_d-Cw_d.
\]

All current allocation and slack values are positive. A feasible comparison
`(x',s')` is nonnegative and obeys the same equations. Write
`h=x'-x`, `h_s=s'-s`, and

\[
 P=\sum_d\frac{(h_{s_d})_+}{s_d},\qquad
 Q_s=\sum_d\frac{(-h_{s_d})_+}{s_d},\qquad
 Q_x=\sum_e\frac{(-h_e)_+}{x_e}.
\]

The slack gradient and one-sided motion charge are

\[
                       G=P-Q_s,\qquad
                       \mathcal C=P+Q_s+Q_x.
\]

The actual matching comparison in a settled state with the promised gap
has `P>12N`, `Q_s<=N`, and `Q_x<=3N`. Consequently, at `beta=1/4`,

\[
 G-\beta\mathcal C
   =\tfrac34P-\tfrac54Q_s-\tfrac14Q_x
   >9N-\tfrac54N-\tfrac34N=7N.                 \tag{1}
\]

This stronger, absolute comparison margin is essential. The certificate is
allowed to disregard isolated positive-ratio directions that cannot carry
the matching comparison's normalized mass.

## 2. Any feasible distance potential gives a scalar upper certificate

Use the source graph of the slack-only threshold test. An allocation has a
zero-cost receiving arc `r -> d` and donor arc `d -> r` of cost `beta/x_e`.
The source arc to bin `d` has cost

\[
                         A-(1-\beta)/s_d.
\]

Let `D(v)` be **any** lower-feasible distance labels, with source label zero:
each arc `u -> v` of length `c` obeys `D(v)<=D(u)+c`. The labels need not
equal current shortest distances. Define

\[
                              \pi_v=A-D(v)
\]

for ordinary rows and bins. Arc feasibility is precisely

\[
 0\le\pi_d-\pi_r\le\beta/x_e,
 \qquad
 \pi_d\ge(1-\beta)/s_d.                       \tag{2}
\]

Rows have zero net allocation change and bins obey
`sum_(e incident d) h_e + h_(s_d)=0`. Therefore

\[
 \begin{aligned}
 \sum_d\pi_d h_{s_d}
  &=-\sum_e\pi_d h_e\\
  &=-\sum_{e=(r,d)}(\pi_d-\pi_r)h_e\\
  &\le\beta Q_x.                              \tag{3}
 \end{aligned}
\]

Subtracting this upper bound for the allocation charge yields

\[
 \begin{aligned}
 G-\beta\mathcal C
 &\le
  \sum_d\big((1-\beta)/s_d-\pi_d\big)(h_{s_d})_+\\
 &\quad+
  \sum_d\big(\pi_d-(1+\beta)/s_d\big)(-h_{s_d})_+\\
 &\le
  \sum_d\big(\pi_d-(1+\beta)/s_d\big)_+(-h_{s_d})_+\\
 &\le
  \sum_d\big(s_d\pi_d-1-\beta\big)_+.
                                                        \tag{4}
 \end{aligned}
\]

The first sum is nonpositive by (2). The final inequality uses only
`s'_d>=0`, which gives `(-h_(s_d))_+<=s_d`.

Define

\[
                  E(\pi,s)=
                    \sum_d(s_d\pi_d-1-\beta)_+.          \tag{5}
\]

Equations (1) and (4) prove the semantic decision:

> At a settled top matching state, a valid potential with `E<=7N` certifies
> that the phase's promised matching improvement is absent.

This does not assert that every individual threshold margin is nonpositive.
Some bin can violate `D(d)>=A-(1+beta)/s_d` while the sum of its normalized
excesses remains too small to support the required matching comparison.

## 3. Conservative integer prices and an exact finite-word certificate

Fix `beta=1/4` and a polynomial integer scale `H`. Use

\[
 c_e=\lceil H/(4x_e)\rceil,
 \qquad
 \sigma_d=\lfloor3H/(4s_d)\rfloor,
\]

with receiving cost zero and source cost `A-sigma_d`. Let the integer
labels `D_int` be feasible for this integer graph and put

\[
                         \pi_v=(A-D_{\rm int}(v))/H.
\]

Then

\[
 0\le\pi_d-\pi_r\le\frac1{4x_e}+\frac1H,
 \qquad
 \pi_d\ge\frac3{4s_d}-\frac1H.                \tag{6}
\]

Let `T=sum_d s_d`. Feasibility of the comparison implies
`sum_d s'_d=T`, because every row retains sum `L` and every bin right-hand
side remains fixed. Thus

\[
 \sum_e(-h_e)_+\le\sum_e x_e=L|R|,
 \qquad
 \sum_d(h_{s_d})_+\le T.                       \tag{7}
\]

Repeating the preceding calculation with (6) proves

\[
 G-\tfrac14\mathcal C
       \le E(\pi,s)+\frac{L|R|+T}{H},
 \qquad
 E(\pi,s)=\sum_d(s_d\pi_d-\tfrac54)_+.
                                                        \tag{8}
\]

No sum of independently encoded rational reciprocals appears in `E`.
On the existing common dyadic primal grid, every `s_d pi_d` has the same
fixed denominator `H` times the common dyadic denominator. The sum,
positive-part operations, and comparisons therefore use fixed-length
integer arithmetic. The polynomial magnitude guards make the required
word size `O(log S)` with fixed precision constants.

Choose `H` large enough both for the static detection margin in the main
slack-only note and for

\[
                         (L|R|+T)/H\le N.
\]

Then the conservative finite-word decision is

> A valid integer potential with `E<=6N` safely certifies matching LOW.

For a fixed potential, a numerical path step changes only its two endpoint
slacks. Hence `E` can be updated by two exact term replacements. Rebuilding
or explicitly changing the potential requires charging all changed terms.
Structural edits also require reestablishing potential feasibility; their
effect is not covered by the fixed-topology statement.

## 4. Row-potential normalization

For any potential satisfying (2), replace each row value by

\[
                       \pi_r^{\rm new}
                          =\min_{d\sim r}\pi_d.          \tag{9}
\]

Every old row value is at most this minimum. Raising it to the minimum
preserves nonnegativity of every difference `pi_d-pi_r` and only decreases
those differences, preserving every donor upper bound. It leaves source
constraints and `E` unchanged. The same proof works for the integer
constraints with upper bound `c_e/H`.

Each row now has at least one zero receiving arc that is tight in the
potential. A physical row has degree at most three, so its normalized
value and a tight exit can be recomputed in constant local work after its
neighboring bin potentials change.

This local statement does not guarantee that an excess bin has a
source-rooted path of tight or sufficiently cheap arcs. It does not
construct the global directed path oracle.

## 5. A fixed old shortest-path tree defines a monotone epoch

At the beginning of an epoch compute an exact shortest-path tree in the
integer source graph (or the real graph) and keep both its topology and its
original labels fixed. Every later numerical step must use a path in this
same rooted tree, and its **current actual path cost** must still pass the
strict threshold at the selected endpoint. No structural edit is included
in this epoch statement.

All of the following are proved properties of such an epoch.

### 5.1 The fixed labels remain feasible

The donor arcs on the tree path increase in cost when their allocations
decrease. Reverse donor arcs of receiving incidences may decrease, but the
receiving zero arcs are tight in the fixed original labels. Their reverse
arcs therefore retain nonnegative reduced cost at any positive new donor
price.

The starting bin's source cost increases. For the terminal bin, feasibility
gives `D_old(b)<=current_tree_path_cost(b)`. Current path acceptance gives
the latter a strict upper bound `A-tau_b` in the integer model. Thus the
source arc to the terminal bin has margin greater than
`tau_b-sigma_b>=H/(2s_b)` over `D_old(b)`. The small step from the main
slack-only note decreases that source cost by less than this margin.
Induction proves feasibility of the unchanged labels after every accepted
step. The identical real proof uses margin `2 beta/s_b`.

This argument does **not** require the old tree to remain a current
shortest-path tree. It uses current path cost for acceptance and old-label
tightness only on its receiving arcs.

### 5.2 Every tree incidence has one motion direction

A tree incidence has a fixed orientation away from the artificial source.
It is either always a donor on selected root paths, so its allocation only
decreases, or always a receiver, so its allocation only increases. Both
directions of one incidence cannot simultaneously lie in a rooted tree.

Each child bin of the artificial source can only be the initial bin of a
tree path. It cannot be an accepted terminal bin, since its direct path
cost `A-sigma_b` is never smaller than `A-tau_b`. Its slack therefore only
increases, and its source cost only increases.

Every other bin can only lose slack as a terminal bin; intermediate visits
leave its slack unchanged. Its reciprocal and terminal threshold price
`tau_b` therefore only increase.

### 5.3 All current tree threshold margins decrease

Every positive tree-arc cost is a donor cost and is nondecreasing. Each
used source-child cost is nondecreasing. For a non-source-child endpoint,
`tau_b` is nondecreasing. Consequently

\[
       A-\tau_b-\operatorname{cost}_{\rm current}(T[z_*,b])
\]

is nonincreasing throughout the epoch. A bin whose old-tree path has failed
the threshold cannot become acceptable later in that same epoch.

This is a genuine monotone search space. It can guide a future fixed-tree
implementation, but exact sums of reciprocal costs under implicit path
updates and all repricing events still need an explicit implementation or
conservative pricing variant.

## 6. What the epoch lemma does not establish

Exhausting all acceptable paths of the fixed tree is weaker than exhausting
all acceptable directed paths. The tree can become poor because of donor
cost increases, while alternative non-tree routes remain useful. The fixed
potential remains a valid certificate candidate, but `E` need not be below
the matching LOW threshold merely because the tree has no accepted path.

There is presently no proof that every such tree refresh must consume
`Omega(N)` objective progress, `Omega(N)` logarithmic price variation, or an
equivalent global credit. A shared tree bottleneck is the central risk:
one increased donor can simultaneously spoil many root-to-bin paths, while
the fixed potential can retain excess at many terminal bins. The monotone
epoch properties alone do not charge those stale paths to distinct
coordinate changes. This paragraph records a missing proof obligation,
not a proved lower bound for every possible refresh strategy.

The established interface is therefore:

* feasible old labels give a cheap, stronger semantic LOW screen;
* current threshold-passing paths in their old exact tree preserve those
  labels and form a monotone epoch;
* row normalization supplies a local tight receiving exit;
* a total refresh bound or a dynamic directed path provider is still
  required before improving the general matching running time.

