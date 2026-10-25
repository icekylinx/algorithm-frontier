# Matching-specific numerical certificates and contact-reserve stability

**Research continuation, 25 October 2026.** This note returns to exact
maximum matching on arbitrary general graphs. It does not improve the current
`4/5` time exponent. It separates a genuinely weaker numerical obligation
from the unrestricted raw-cycle interface, gives inexpensive additional LOW
certificates for that weaker obligation, and tests a proposal to freeze one
contact-slack comparison for an entire matching phase.

The matching state, ledger equations, and comparison-direction theorem are
those reconstructed in `current_checkpoint/fresh_general_matching_client_interfaces.md`,
`current_checkpoint/ledger_algebra_and_phase_budget.md`, and
`current_checkpoint/deterministic_phase_cost_and_guards.md` from OAI Sections
3--5. The new claims below are the linear upper certificates, their compatible
maintenance, and the explicit contact-retirement example.

## 1. A strong cycle and a matching-semantic witness are different obligations

The top numerical graph has one allocation coordinate `x_e` for each
row-to-bin incidence and one slack coordinate `s_d` for each bin. At a fixed
settled structural state,

\[
 \sum_{e\ni r}x_e=L,
 \qquad \sum_{e\ni d}x_e+s_d=b_d,
 \qquad b_d=L+p_d-Cw_d.
\]

All present coordinates are positive. The top objective is the sum of their
logarithms, so the exact gradient and price are `1/f_e` on every coordinate.
Let `m_log` be the number of these coordinates and let `N` be the phase's
physical-size bound. The maintained state gives `m_log<=4N`.

The current generic numerical engine prevents LOW whenever *any*
circulation has signed-to-absolute gradient ratio greater than one half.
That promise is sufficient for matching, but is stronger than the actual
matching comparison argument needs.

When the phase still has an optimum improvement of at least its target and no
structural action is available, the comparison proof supplies a nonnegative
alternative vector `f'` with the same row and bin equations. For
`d=f'-f`, its positive logarithmic directional mass exceeds `12N`, whereas
its negative mass is at most `m_log<=4N`. In particular,

\[
                             g^T(f'-f)>8N.
\]

The negative-mass bound is elementary and exact: whenever `d_e<0`,
`-d_e/f_e<=1` because `f'_e>=0`.

Define the linearized feasible-gain quantity

\[
 \mathcal G(f)=
 \max\left\{
    \sum_e\frac{f'_e-f_e}{f_e}:
    f'\ge0\text{ obeys the same row and bin equations}
          \right\}.
\]

Thus a valid upper bound `Gbar<=8N` on `G(f)` is enough to certify the
matching phase's LOW conclusion, even if the numerical graph still contains
some ratio-greater-than-one-half cycle. It is essential to apply this only at
the settled no-action point at which the matching comparison theorem applies.
It is not a replacement for the projection client's separate threshold test.

This distinction leaves a real opening beyond the previous route-quality
counterexamples. A short strongly improving cycle may have only constant
total feasible linearized gain. Such a cycle can occur when the represented
matching is already maximum. Hiding that cycle behind a poor route family
does not, by itself, show that every matching-semantic oracle must find it.

## 2. Two elementary dual upper certificates

Let

\[
 T=\sum_d s_d
   =L(|D|-|R|)+\sum_d p_d-C\sum_d w_d.
\]

This sum is the slack-source divergence and remains fixed during a numerical
circulation. It is updated exactly from the explicit structural ledger data.

Set

\[
 a_r=\max_{e\ni r}\frac1{x_e},
 \qquad b=\max_d\frac1{s_d}.
\]

Every feasible alternative obeys

\[
 \sum_{e\ni r}\frac{x'_e}{x_e}\le L a_r,
 \qquad \sum_d\frac{s'_d}{s_d}\le Tb.
\]

Consequently

\[
 \boxed{\quad
       \mathcal G(f)\le
            L\sum_r a_r+Tb-m_{\log}.
       \quad}
\]

There is a separate bin-side certificate. Put

\[
 c_d=\max\left\{\frac1{s_d},
                   \max_{e\ni d}\frac1{x_e}\right\}.
\]

The bin equation gives

\[
 \boxed{\quad
             \mathcal G(f)\le\sum_d b_d c_d-m_{\log}.
       \quad}
\]

Both estimates are upper bounds, not heuristics. Taking their minimum is
valid. They are simple feasible dual solutions for the linear transportation
optimization problem defining `G(f)`; computing them does not solve that
optimization problem.

The row-side bound can also be applied separately to each connected component
of the original physical input graph. Structural operations never create an
allocation incidence between different original components. Each such
component has its own fixed slack sum `T_H`, so replace the global term `Tb`
by `sum_H T_H b_H`, where `b_H` is its maximum slack reciprocal. This
strengthening uses a partition computed once at input cleanup, and needs no
dynamic-connectivity oracle. It avoids coupling a tiny slack in one physical
component with irrelevant large slack mass in another component.

## 3. Maintaining safe versions without a full flow scan

The preceding formulas need not read current implicit values after every
numerical step. Use the existing anchored integer prices

\[
                       \ell_e=\lceil H/\widehat f_e\rceil.
\]

For a single logarithm the settled register condition gives
`|f_e-fhat_e|/fhat_e<=tau`, with the existing small `tau=q/100`. Hence

\[
                         \frac1{f_e}
                            \le\frac{\ell_e}{H(1-\tau)}.
\]

Define integer aggregates

\[
 A=\sum_r\max_{e\ni r}\ell_e,
 \qquad B=\max_{d}\ell_{s_d},
 \qquad Q=\sum_d b_d
                \max\{\ell_{s_d},\max_{e\ni d}\ell_e\}.
\]

Then safe computable upper bounds are

\[
 \widehat G_{\rm row}
       =\frac{LA+TB}{H(1-\tau)}-m_{\log},
 \qquad
 \widehat G_{\rm bin}
       =\frac{Q}{H(1-\tau)}-m_{\log}.
\]

These aggregates use integer prices and the common dyadic ledger grid.
They do not sum unrelated exact rational reciprocals into a denominator of
growing bit length. All aggregate numerators have `O(log S)` bits up to the
existing absolute precision constants.

Each row has at most three physical incidences. A dirty allocation price
therefore updates its row maximum in constant local work and its bin maximum
in a balanced dictionary or heap. A dirty slack price changes the global
slack heap and one bin heap. Maintain the sum of bin-capacity times bin
maximum when that bin's maximum, debt, or weight changes. Retargeting and
topology edits use the already charged incidence transcripts.

Thus every reported dirty logical coordinate or explicit structural edit
adds only `O(log S)` work. A numerical path update need not be expanded, and
there is no scan over a high-degree bin when its slack price changes. The
certificate is queried only after the existing refresh transaction has
settled all flags, so all prices obey their current accuracy promise.

For the component-wise strengthening, keep a separate slack-price heap and
the exact ledger sum `T_H` for each fixed original physical component. A
coordinate update affects only its one component, so the same bounds apply.

If the minimum of these two upper bounds is at most `8N`, the top client may
return semantic LOW immediately. This is a positive, complete interface
improvement. It does not bound the number of states where both estimates are
large, and therefore does not yet improve the worst-case time exponent.

## 4. The proposed frozen contact comparison

Let `Z` be the current bins that have a physical contact to the paired
remainder. A natural proposed replacement for repeated general raw-cycle
queries is:

1. compute once a feasible allocation maximizing `sum_(d in Z) s_d`;
2. keep it as an additional comparison ledger;
3. extend it through contractions, preserving deletions, and expansions;
4. charge losses of its contact-slack reserve to physical work and the phase
   debt budget until the required number of gains has occurred.

The difficulty is that `Z` changes. The following example disproves a
specific simple stability claim: an arbitrary old contact-LP maximizer,
continued using the literal top expansion formulas, need not lose only
`O(C)` reserve per touched physical vertex. It also shows that computing the
certificate at the phase's initial state does not cure this problem if its
later extension remains literal. It does not rule out choosing a stronger
certificate or actively redistributing reserve.

## 5. A reachable two-sided contact-retirement example

For `j=1,2`, make physical vertices `a_j,r_j,b_j,u_j,v_j`. Also make `p,q`.
Use the following initial matching:

\[
     r_1b_1,\quad r_2b_2,\quad u_1v_1,\quad u_2v_2,\quad pq.
\]

The unmatched vertices are `a_1,a_2`. Add the nonmatching edges

\[
 a_jr_j,\quad a_ju_j\quad(j=1,2),\qquad b_1p,\quad qb_2.
\]

Every vertex has degree at most two. There is an augmenting path

\[
             a_1,r_1,b_1,p,q,b_2,r_2,a_2.
\]

It matches all twelve gadget vertices after augmentation, so the true gap is
exactly one. The two `u_jv_j` branches are dead ends. One may add arbitrarily
many disconnected matched edges. They introduce neither new unmatched
vertices nor remainder contacts to any current bin. The entire graph remains
simple, subcubic, and without isolated vertices.

For this enlarged graph the direct driver's initial upper bound is still
one, its phase target is `K=1`, and

\[
                         L=10000CN.
\]

Initially each `a_j` is a singleton bin of weight one, there are no rows, and
the remaining vertices belong to their listed matched pairs. The unique
allocation is empty and the contact slack is `s_(a_j)=L-C`. Thus a one-time
contact-LP solution at the initial phase state has no tie to choose.

### First legal expansions

Expand the matched pairs `r_jb_j` from their contacts to `a_j`. This is a
legal priority order: the parent slacks are far above `3C`, and the example
has no distinct-bin edge forcing a competing gain or contraction. The new
row and child bin are `r_j` and `b_j`, respectively. The literal top settings
are

\[
 x_{r_j,a_j}=C+1,\qquad x_{r_j,b_j}=L-C-1,
\]

and therefore

\[
              s_{a_j}=L-2C-1,
              \qquad s_{b_j}=1.
\]

All these values are positive integers, so no small-coordinate padding is
required. The child `b_j` has a contact to `p` or `q`, but its slack one is
ineligible for an expansion. The old parent `a_j` still has its eligible
dead-end contact to `u_j`.

At this point `Z={a_1,b_1,a_2,b_2}`. Each side has one row of sum `L` and two
bin capacities `L-C`, so its total slack is exactly `L-2C` under *every*
feasible allocation. The displayed vector is consequently an exact old
contact-LP maximizer, with reserve `2L-4C`.

For any integral ledger floor `c<=C`, one can take

\[
          x^{\rm int}_{r_j,a_j}=c,
          \qquad x^{\rm int}_{r_j,b_j}=L-c.
\]

Both bin residuals are at least `c`, debts are zero, and the positive support
is a tree. This verifies simultaneous settled feasibility of every required
integral floor. During the literal expansion transaction itself, the usual
child debt `c` makes the standard initialization valid; exact projection can
then produce this zero-debt state.

Give `a_j` the smallest bin identifier in its carrier component. The
canonical orientation of this two-incidence-row tree then assigns `r_j` to
`b_j`; after the next expansions it likewise assigns `u_j` to `v_j`. Thus
the displayed augmenting path remains literal under the canonical carrier
choice. Even without this identifier convention, the unchanged matching
cardinality and fixed graph optimum still imply a true remaining gap of one.

### The contact-retiring expansions

Now expand each dead matched pair `u_jv_j`. Its parent `a_j` remains eligible.
The new row `u_j` has allocations

\[
                 x_{u_j,a_j}=C+1,
                 \qquad x_{u_j,v_j}=L-C-1.
\]

The old row settings are unchanged. Thus

\[
 s_{a_j}=L-3C-2,\qquad s_{b_j}=s_{v_j}=1.
\]

All top debts remain zero and all slacks stay positive. The paired edge
`pq` remains. The bins `a_j` have no further contacts to the paired
remainder, and `v_j` has no other physical neighbor. Consequently the new
contact set is exactly `Z'={b_1,b_2}`.

The continued reserve is only

\[
                         s_{b_1}+s_{b_2}=2.
\]

No matching gain has occurred. Only four physical vertices, the two matched
dead-end pairs, were expanded. The original augmenting path still exists, so
the true remaining gap is still one.

For an integral floor `c<=C`, the two rows on one side can be given `c` on
their incidences to `a_j` and `L-c` on their child incidences. The three bin
residuals are `L-2c,c,c`, respectively. They satisfy floor `c` when `L>=3c`,
and all debts are zero. This allocation is already a forest carrier. The
example therefore does not rely on an impossible lower-ledger repair.

The total reserve loss in these two contact-retiring expansions is
`2L-4C-2`. By adding the disconnected matched edges, `L/C=10000N` is
arbitrarily large while the touched gadget volume is constant. Thus the
claimed `O(C * touched physical volume)` bound cannot hold for this literal
continuation.

## 6. Exact quantifier boundary and a positive repair of this example

The old objective is constant across all feasible allocations of each
two-bin side. One could instead have placed most old slack on `b_j`, which
would avoid the stated reserve loss. The example therefore does not defeat
every rule for choosing an old optimum. Starting at the initial phase state
removes that initial tie, but a nonliteral extension or a later redistribution
can still improve the evolving certificate.

Indeed the example has a constant-size repair. After the dead expansions,
modify only row `r_j`:

\[
 x_{r_j,a_j}: C+1\longmapsto L-2C-1,
 \qquad x_{r_j,b_j}: L-C-1\longmapsto2C+1.
\]

This moves `L-3C-2` units from the `b_j` incidence to the `a_j` incidence.
Decrease `s_(a_j)` by the same amount and increase `s_(b_j)` by that amount.
Every row and bin equation is preserved. The resulting slacks are zero at
`a_j` and `L-3C-1` at `b_j`, with `s_(v_j)=1`; the additional comparison
ledger permits zero coordinates. If strict positivity is wanted, reduce the
transfer by one, leaving slack one at `a_j` and `L-3C-2` at `b_j`.

Thus a conserved batch flow transfers the old reserve to the surviving
contact. This repair uses a constant number of coordinates in this example.
In a general state, the surviving contact may be separated from the retiring
one by a long alternating network, and simultaneous transfers can compete
for the same allocation capacities.

## 7. A concrete sufficient reserve-stability interface

A meaningful version of the proposed frozen-comparator route would maintain
more than one immutable allocation vector. One sufficient contract would be:

* A feasible extra allocation on the current row/bin graph, with the same
  row sums and the actual bin capacities, together with a separately stated
  nonnegative contact-reserve invariant.
* For each structural batch, a conserved redistribution that restores
  feasibility and transfers reserve away from contacts that retire, while
  handling any newly created contacts. Its representation may use forest
  paths; expanding all touched path coordinates is not automatically cheap.
* A history-wide loss bound proportional to already paid phase quantities,
  sufficient to retain a reserve of order `LK` until the required gains, or
  a separately justified gain/LOW certificate when that reserve cannot be
  retained.
* Actual-size initialization, sparse topological and value updates, complete
  current path/edge identities, and a total work bound that does not hide a
  fresh general flow computation after each retirement.

An alternative is to keep a compressed *set* of feasible allocations that
allows the reserve to be moved on demand. Either version needs a new
algorithmic theorem. The elementary preserving-deletion and expansion
identities by themselves establish none of these redistribution guarantees.

The counterexample does not rule out this interface. It identifies the
operation that must be added: moving capacity already stored at an obsolete
contact through the old row network to contacts that remain relevant. That
operation is exactly the point at which a static comparison can become a
dynamic flow-maintenance problem.

## 8. What remains open for the original `4/5` bottleneck

The new dual screens are compatible with the existing finite numerical
implementation and strictly weaken the situations in which a raw-cycle call
is necessary. They do not yet show that the remaining calls admit smaller
serial correction or recursive lift quality.

The fixed-contact-reserve proposal also survives in a strengthened form that
permits charged redistribution. Its literal immutable-vector interpretation
does not survive the reachable example above. Any future claim below `4/5`
must prove either the needed redistribution interface or a capacity-aware
cycle-comparison theorem specifically for the large feasible-gain witnesses
required by matching. Algebraic rebalancing of the existing generic
`d K log Gamma` bound is not such a proof.
