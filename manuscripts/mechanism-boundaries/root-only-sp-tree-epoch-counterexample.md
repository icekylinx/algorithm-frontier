# A reachable obstruction to linear progress per old-root tree epoch

**25 October 2026. Root mathematical audit completed.** This note gives a family of legal slack-only top
matching states with true matching gap one. Their ordinary allocation
graphs have linear size. An exact source shortest-path tree can lose all
acceptable paths from its original source root after only logarithmic
progress and logarithmic coordinate-price variation.

The conclusion is deliberately specific. It refutes a claim that every
exhausted epoch using only paths from the old artificial-source tree root
must earn linear objective progress or linear logarithmic-price credit.
It does not refute local tree repair, using arbitrary intermediate source
bins, a more general potential-tight path provider, or a history-wide
amortization with additional credits. It is not a running-time lower bound
for matching.

Unlike a generic bad-cycle example, this family has an explicit actual
augmenting path, phase target $`K=1`$, and a feasible comparison with
normalized positive slack mass far above $`12N`$.

## 1. The connected subcubic physical graph

Take two disjoint alternating chains of length $`t`$ matched pairs,
where $`t`$ tends to infinity. On the left use bins
$`v_0=c_A,v_1,\ldots,v_t=a`$ and rows $`r_1,\ldots,r_t`$,
with physical edges
```math
v_{i-1}r_i,\quad r_i v_i.
```
On the right use analogous bins
$`u_0=c_W,u_1,\ldots,u_t=w`$ and rows.

Add a matched pair $`r,b`$, with physical edges $`ra,rw,rb`$.
Add another matched pair $`p,q`$, with physical edges $`ap,pq,qw`$.
The initial matching contains every chain row/child pair, $`rb`$,
and $`pq`$. Its only free vertices are $`c_A,c_W`$.

The graph is connected and has maximum degree three. In particular,
$`a,w,r`$ have degree three. The edges
```math
a-r-w-q-p-a
```
form an odd cycle. The construction is therefore a legitimate general
nonbipartite input, although no nonbipartite hardness is claimed.

There are
```math
N=4t+6
```
physical vertices. The current matching has $`N/2-1`$ edges. The path
from $`c_A`$ along its chain to $`a`$, then through $`p,q,w`$, then
back along the other chain to $`c_W`$, is augmenting. Flipping it gives
a perfect matching. Thus the true gap is exactly one.

Use a phase with $`K=1`$, and the usual sufficiently large row sum
```math
L=10000\,C N,
```
with $`C\ge 4`$ on the standard logarithmic scale. All bins in the
construction are singletons and have weight one.

## 2. A legal preparation of the top state

All ordinary top debts are zero. Tiny positivity-service debt, if used
by an implementation, can be absorbed in the perturbations below and
is too small to pay for a physical peel.

Start with the free bin at the beginning of each chain. Expand the first
matched pair. A top expansion places $`C+1`$ on the old parent incidence
and $`L-C-1`$ on the new child incidence. Its child has slack one.

For this preparation maintain an exact slack cache for structural
eligibility. This is an allowed special case of the client's approximate
cache: each numerical path changes only two bin slacks, so updating these
cache entries explicitly has constant additional work. The actual
eligibility test remains cached slack at least $`4C`$. The guarantee
that an eligible bin has actual slack at least $`3C`$ is only a lower
bound, not an alternative trigger.

For every subsequent chain pair, increase the latest child's slack to
the first crossing of $`4C`$ using a positive numerical path back
toward its free chain root. Then expand the next pair. The old parent
slack is left at $`3C-1`$, up to the small numerical overshoot. All old
internal chain bins cease to contact the paired remainder after their
successor has been expanded.

These numerical paths are valid strong directions. Before the final
bridge expansion, all nonfree slacks in a chain are $`O(C)`$, so each
donor allocation on a path toward its free root is
```math
L-O(tC)\ge .99L.
```
The whole ordinary path cost is at most $`O(t/L)`$, while a newly born
source has slack at most $`O(C)`$, and the free-root slack is
$`L-O(tC)`$. The one-sided ratio is bounded below by an absolute
constant greater than $`1/2`$.

One can also realize this preparation with exact source-path choices,
rather than asserting an arbitrary strong path is automatically the
global shortest-path answer. Always query the free-root endpoint in the
currently processed allocation component. If the latest contact is
temporarily not the maximizing source, the exact answer raises some
other low-slack bin in that same component. All old noncontact bins can
be raised safely. Until the latest contact reaches $`4C`$, the true
strong path from that contact to the free root prevents termination.
Every chosen source has slack $`O(C)`$, since that path's value dominates
the offer of a much larger-slack source. Constant progress and the
bounded potential range therefore force the desired contact to become
eligible after finitely many steps. No other contact in that allocation
component is eligible first.

The constants in this preparation can be made explicit. Inductively
keep all old nonfree slacks below $`5C`$. Telescoping the chain bin
equations bounds every parent allocation by $`6(t+1)C`$, so every
child-to-row donor has allocation at least $`.99L`$. While the latest
contact has slack at most $`4C`$, its offer at the free-root endpoint
is at least
```math
\frac{3}{16C}-\frac{t}{4(.99)L}>\frac{0.186}{C}.
```
An exact winning source therefore has pre-step slack less than
$`(.75/.186)C<4.033C`$. A normalized step changes its slack by
at most a $`1/256`$ fraction, so its post-step slack is below
$`4.1C`$. This closes the induction with slack. After an expansion,
the old contact lies between $`3C-1`$ and $`3.1C-1`$, before any
later harmless increases. Thus every old noncontact stays at least
$`3C-1`$ and below $`4.1C`$. Finite-word rounding can be made
smaller than the displayed constant margins with the already required
polynomial scale. The exact-source preparation is therefore not
relying on an unspecified hidden constant larger than the later
$`5C`$ bound.

On the left stop its last contact $`a`$ after raising its slack from one
to a value in $`[2,3]`$. This is well below $`3C`$. Process the right
component independently until $`w`$ first becomes eligible. The two
ordinary allocation components are still disjoint, so the small price
at $`a`$ does not force the right component's numerical answer to start
at $`a`$.

Choose the eligible expansion of $`r,b`$ from $`w`$, before expanding
the pair $`p,q`$. This is a legal structural priority. The new row
has three incidences. For a tiny dyadic $`\epsilon>0`$, set
```math
x_{rw}=C+1,\qquad
 x_{ra}=\epsilon,\qquad
 x_{rb}=L-C-1-\epsilon.                                  \tag{1}
```
This is exactly the usual expansion plus a harmless positive padding
on the additional incidence. It decreases the old slack of $`a`$ by
$`\epsilon`$, leaves the old slack of $`w`$ at about $`3C`$, and gives
the new bin $`b`$ slack $`1+\epsilon`$.

After this expansion:

* $`s_b=1+\epsilon`$;
* $`s_a\in[2-\epsilon,3]`$;
* $`s_w<3.1C`$, with the exact eligibility cache still below $`4C`$;
* every old internal chain slack is between a fixed positive multiple
  of $`C`$ and $`5C`$;
* each free-root slack is $`L-O(tC)`$.

The only remainder contacts are $`a`$ and $`w`$, through $`ap`$ and
$`wq`$. Their slacks are below the expansion threshold. There is no
physical bin/bin edge for a contraction or pair operation, and ordinary
top debt is zero. Thus no structural action is being postponed at the
state where the epoch starts.

The actual remainder pair $`p,q`$ still certifies the true gap one.
Changing a canonical row injection does not change the represented
matching cardinality, so this gap does not depend on keeping one
particular carrier orientation.

## 3. The full ledger constraints are feasible

At the top every row sums to $`L`$, and every bin satisfies
```math
\mathrm{load}(d)+s_d=L-C.
```
All coordinates are positive and lie in the guarded polynomial range.
Take $`\epsilon`$ on the existing common dyadic grid.

The physical allocation support is a tree, now with one degree-three
row $`r`$. It admits every lower integral floor with zero debt. For
an integral floor $`c\le C`$, assign row $`r`$ values
```math
c,\ c,\ L-2c
```
to $`a,w,b`$, respectively. On either chain, give row $`i`$
```math
L-(t-i+2)c
```
to its child bin and the complementary amount to its parent. Every
nonroot chain bin then has residual $`c`$, bin $`b`$ has residual
$`2c`$, and each free chain root has residual $`L-(t+1)c`$.
All floor inequalities hold strictly or with equality. The values are
integral, nonnegative, and supported on the actual tree.

This explicitly checks that the state is not obtained by violating an
integral floor. The earlier client has no coordinatewise equality
requirement between different integral levels. Its established ledger
maintenance can process the legal top steps; this example does not
prescribe a fast numerical implementation of the new one-sided client.

## 4. The exact source tree is dominated by the new bin b

Use $`\beta=1/4`$. In the threshold source graph, donor arcs have
length $`\beta/x`$, receiver arcs have length zero, and the source
arc to a bin $`d`$ has length $`A-(1-\beta)/s_d`$.

Every other bin has slack at least $`2-o(1)`$, so its direct source
offer is at most $`3/8+o(1)`$. The offer of $`b`$ is
$`3/4-o(1)`$.

From $`b`$, its donor $`b\to r`$ is large-allocation and cheap.
The two zero receiving arcs reach $`a`$ and $`w`$. The paths from
there to the two free roots use only large-allocation chain donors.
Every such ordinary path has length $`O(t/L)`$. Thus the offer
from $`b`$ exceeds $`0.7`$ everywhere, whereas all other sources
offer at most $`0.4`$.

The exact source shortest-path tree therefore has the unique first bin
$`b`$. It branches at row $`r`$ toward the two chains. All its receiving
arcs are tight in the old distance potential. The tree contains
$`\Theta(N)`$ actual records.

## 5. Exhausting only old-source-root paths

Freeze this exact tree and its old distance labels. Permit the numerical
steps described in [slack-potential-semantic-certificate.md](../graph-backends/slack-potential-semantic-certificate.md): a current
tree path from the artificial source must pass the current threshold.
Its first bin is therefore always $`b`$.

Write $`u`$ for the cumulative slack increase of $`b`$. Every other bin
is only a terminal or an intermediate vertex, so its slack never
increases. All ordinary tree incidences have their fixed donor or
receiver motion direction.

Once $`s_b>4C`$, no old internal bin or contact can remain an acceptable
terminal: all their slacks are at most $`5C`$, whereas positive
$`\beta`$-threshold acceptance requires
```math
s_b<\frac{1-\beta}{1+\beta}s_{\rm terminal}
                       =\frac35s_{\rm terminal}.
```
The two large free-root slacks are the last possible terminals.

A path from $`b`$ to a free root has $`t+1`$ donor incidences.
While $`u=O(L/t)`$, their allocations remain
$`L-O(tC)-O(L/t)`$, and the free-root slack remains
$`L-O(tC)-O(L/t)`$. Its total donor charge is therefore
$`\Theta(t/L)`$.

There are absolute constants $`c_1,c_2>0`$ such that:

* if $`s_b<c_1L/(t+1)`$, a free-root path still passes the threshold;
* if $`s_b>c_2L/(t+1)`$, both free-root paths fail.

For example, a sufficiently small $`c_1`$ works by the preceding upper
bound on path charge. For the second direction, every donor allocation
is at most $`L`$, so donor charge is at least $`(t+1)/L`$.
The source term $`3/(4s_b)`$ alone is below the donor threshold
charge once $`s_b>4L/(t+1)`$.

It follows that exhaustion occurs at
```math
s_b=\Theta(L/t)=\Theta(C),              \tag{2}
```
where the hidden constants can depend on the fixed factor $`10000`$.
This argument allows arbitrary choices of accepted old-root tree
endpoints, not only repeated queries of one selected free root.

For the normalized constant-ratio step rule, $`s_b`$ grows by a
constant factor bounded away from one while a step is accepted.
Indeed, the raw charge $`V`$ lies between $`1/s_b`$ and
$`1/(\beta s_b)`$, and
$`\beta/128\le\eta V\le\beta/64`$. Hence only
```math
O(\log C)
```
such numerical steps are needed in this epoch.

## 6. The earned credit is sublinear

Only $`b`$'s slack increases during the epoch. The objective increase
therefore satisfies
```math
\Delta\Phi\le
                    \log\frac{s_b^{\rm final}}{s_b^{\rm initial}}
                          =O(\log C).                    \tag{3}
```

The total logarithmic variation of allocation prices is also only
$`O(\log N)`$. Each large donor changes by at most $`O(L/t)`$;
summed over the $`O(t)`$ donors, its negative logarithmic variation
is $`O(1)`$.

On a chain, the initial receiving allocation at distance $`j`$
from the far endpoint is at least a constant times $`Cj`$.
Every such receiving coordinate increases by at most $`O(L/t)=O(C)`$.
Consequently its total positive logarithmic variation is bounded by
```math
\sum_{j=1}^{t}\log(1+O(1)/j)
                         =O(\log(t+1)).
```
The receiving incidence $`ra`$ starts at $`\epsilon`$; its possible
increase contributes only $`O(\log(C/\epsilon))=O(\log S)`$.
Here $`S`$ is polynomially related to $`N`$, and the padding exponent
is fixed. The other new-row incidence contributes $`O(1)`$.
Slack variation adds $`O(\log C)`$.

Thus neither objective gain nor total logarithmic coordinate movement
provides $`\Omega(N)`$ credit for an entire-tree refresh.

## 7. The semantic certificate does not terminate the epoch as LOW

For the old exact labels, put $`\pi=A-D_{\rm old}`$. Every bin
has $`\pi_d\ge 1/2`$, by the strict source dominance in Section 4.
Total slack is fixed:
```math
T=2L-C(2t+3).
```
At every point in the epoch,
```math
\begin{aligned}
 E(\pi,s)
   &=\sum_d(s_d\pi_d-5/4)_+\\
   &\ge \tfrac12T-\tfrac54(2t+3)
     =\Omega(L)\gg7N.
\end{aligned}
\tag{4}
```
The stronger maintained LOW screen therefore cannot close this case.

There remains an explicit large comparison. Increase the slack of
contact $`a`$ by $`L/10`$ and decrease the free-root slack on its own
chain by $`L/10`$, transferring allocation along that chain. All
donors and the terminal slack are still at least $`0.8L`$, so this
is feasible. Since $`s_a\le3`$,
```math
P\ge L/30>12N.
```
Its negative normalized coordinates are bounded by their coordinate
counts, as in the matching comparison theorem. The true matching gap
is still one, and neither contact became eligible during the old-root
epoch because their slacks only decreased.

The same example survives conservative integer source/donor pricing.
Choose the fixed polynomial scale $`H`$ as in the finite-word oracle.
The total rounding error on a simple path is $`O(N/H)`$; all source
dominance margins and the asymptotic bounds in (2)--(4) have constant
slack. No exact-real-only cancellation is used.

## 8. Exact scope and a constructive lesson

This is a reachable obstruction to the literal old-root-path epoch
rule, with a connected subcubic physical graph, a linear-size active
ledger, and a genuine matching comparison. It is not a proof that a
full recomputation is necessary, nor that many such refreshes force a
quadratic total running time.

The root reachability and quantitative audit is
[root-only-sp-tree-epoch-root-audit.md](../graph-backends/root-only-sp-tree-epoch-root-audit.md). The fixed-tree interface in
[any-source-fixed-tree-matching-interface.md](../graph-backends/any-source-fixed-tree-matching-interface.md) deliberately allows
intermediate source bins, which this example does not rule out.

In fact the strong path from $`a`$ to its own free root is a segment
of the old ordinary tree starting at an intermediate bin. Its receiving
arcs are still tight in the old potential. Allowing a fresh source arc
to such an intermediate bin would continue progress while preserving
old-potential feasibility.

Thus one concrete next interface is stronger than a fixed-root tree
search but weaker than arbitrary directed SSSP: find a threshold-passing
ancestor-to-descendant bin path in a fixed directed forest, with a
source price at every bin, under implicit allocation updates. Its
completion and any bound on when that larger search space must be
refreshed remain open. The counterexample does not rule them out.

