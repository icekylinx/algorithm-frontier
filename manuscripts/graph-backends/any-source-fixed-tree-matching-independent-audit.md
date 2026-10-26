# Independent audit of the any-source fixed-tree matching interface

**25 October 2026. Independent mathematical and implementation audit.**

This audit concerns [any-source-fixed-tree-matching-interface.md](any-source-fixed-tree-matching-interface.md), with its
operative initialization and feasible labels defined using the persistent
conservative donor prices

$$
\bar c_e=\left\lceil H/(4\ell_e)\right\rceil,
             \qquad \ell_e<x_e<2\ell_e.
$$

The local interface passes the checks below. It does **not** bound the
number or total construction cost of refreshed shortest-path forests and
does not improve the established matching exponent. Polynomial magnitude
guards, the common primal grid, and the actual matching comparison are
explicit imports from the existing matching ledger. A guard or structural
repair terminates the current epoch.

The distinction between conservative initialization and true-price
initialization is material. It is resolved in Sections 1 and 6 below;
certificates for these two graphs must not be combined.

## 1. Initialization must use the same conservative graph as the detector

Write $\alpha_v=1/s_v$, and use source and terminal prices

$$
\sigma_v=\lfloor 3H\alpha_v/4\rfloor,
 \qquad \tau_v=\lceil5H\alpha_v/4\rceil.
$$

The source arc to a bin has cost $A-\sigma_v$, receiving arcs have cost
zero, and donor arcs have cost $\bar c_e$. Choose a nonnegative integer
offset $A\ge\max_v\sigma_v$. The exact initial distances and a directed
shortest-path tree in **this graph** are denoted by $D$ and $T$.

After deleting the artificial source, the tree is a directed forest rooted
at its source-child bins. All receiving tree arcs have equal labels at their
endpoints. Each allocation incidence can contribute at most one orientation
to the tree, because including both orientations would create a directed
two-cycle. Therefore every allocation changed by a tree transfer has a fixed
motion direction throughout this epoch.

The conservative lengths obey

$$
\frac{H}{4x_e}\le\bar c_e<\frac{H}{2x_e}+1.       \tag{A1}
$$

Any directed bin-to-bin path whose true one-sided ratio exceeds one half
satisfies

$$
L_x(a,b)<\alpha_a-3\alpha_b.
$$

Consequently its unrounded conservative threshold margin is greater than
$(\alpha_a+\alpha_b)/4$. A simple path has at most $N$ donor arcs;
donor ceilings and the two endpoint roundings lose at most $N+2$
integer units. The requirement

$$
H\min_v\alpha_v\ge8(N+2)             \tag{A2}
$$

leaves a strict positive margin. An exact conservative shortest path to its
terminal is no more expensive. Thus a newly built conservative SPT contains
a passing source-child-to-bin path whenever the genuine matching comparator
exists.

There is an even stronger fresh-state statement. Suppose no source-child
path in this freshly built SPT passes the integer test. If $a$ is the
source child on the SPT path to $b$, exactness gives

$$
D(b)=A-\sigma_a+\bar L(a,b)\ge A-\tau_b.
$$

For $\pi_v=(A-D(v))/H$, this yields

$$
\pi_b\le\tau_b/H\le5/(4s_b)+1/H,
 \qquad
 \sum_b(s_b\pi_b-5/4)_+\le\frac{\sum_b s_b}{H}.         \tag{A3}
$$

The right side is at most $N$ under the certificate scale below. Fresh
TREE-EMPTY therefore supplies a semantic LOW certificate. This implication
is only asserted at fresh initialization: after numerical steps the fixed
tree need not remain shortest.

An SPT built instead for $\lceil H/(4x_e)\rceil$ is a valid object for the
older local feasibility lemma, but its selected path need not minimize the
conservative path price. The existence of a passing conservative path then
does not by itself show that this different SPT contains one. The operative
interface avoids this unsupported implication by using $\bar c$ for both
initialization and detection.

## 2. Any starting bin preserves the fixed labels

For an ancestor bin $a$ and descendant bin $b$, the detector accepts
when

$$
\sigma_a-\tau_b-\bar L(a,b)>0.       \tag{A4}
$$

The transfer subtracts $\eta$ from every donor allocation, adds it to
every receiver allocation, increases $s_a$, and decreases $s_b$.
Internal row and bin equations are preserved exactly. The path is simple,
so there is no hidden multiplicity in these updates.

Assume that the unchanged labels $D$ are feasible immediately before the
transfer. Tree donors decrease, so their registers can only reset downward
and their conservative prices cannot decrease. Tree receivers increase;
their reverse donor price can decrease when its register resets upward.
That reverse edge is still feasible because the receiving tree arc was
$D$-tight at initialization and its two endpoint labels remain equal.
Unchanged incidences preserve their previous inequalities.

At the starting bin, the source cost increases. At the terminal bin,
feasibility along the current conservative tree path gives

$$
D(b)\le D(a)+\bar L(a,b)
            \le A-\sigma_a+\bar L(a,b)<A-\tau_b.         \tag{A5}
$$

Thus its current source inequality has margin greater than
$\tau_b-\sigma_b\ge H\alpha_b/2$. If
$\eta\alpha_b\le1/256$, the source-cost decrease is at most

$$
\frac{3H\alpha_b}{4}\,
 \frac{\eta\alpha_b}{1-\eta\alpha_b}+1,
$$

which is less than the available margin by (A2). No source-tightness at
$a$ was used. This is the precise reason an intermediate bin may start
the transfer.

Acceptance also implies $\alpha_a>(5/3)\alpha_b$. The new reciprocal
at $a$ decreases, and that at $b$ is at most
$(256/255)\alpha_b<\alpha_a$. Hence the largest bin reciprocal never
increases, and the fixed offset $A$ remains valid.

This proof preserves one fixed feasible potential. It does not assert that
current exact shortest distances are monotone between arbitrary subsequent
non-shortest tree steps.

## 3. The heavy-light max-plus search is complete for its stated domain

For each tree vertex $v$, let

$$
M_v=\max_{b\in T_v\text{ bin}}
       [-\tau_b-\operatorname{dist}_{\bar c}(v,b)]
$$

and let $F_v$ be the maximum of (A4)'s left side over ancestor-descendant
bin pairs inside $T_v$. If the first bin is $v$, its best value is
$\sigma_v+M_v$. Otherwise both bins lie in a single child subtree.
These two cases prove the main note's recurrence, including the exclusion
of pairs in different branches.

Separating the heavy child gives the stated constant-size triangular
max-plus transformation. The $M$ state carries a terminal bin; a
coefficient from $M$ to $F$ carries the chosen starting bin; an
$F$ constant carries the complete pair. These metadata types are closed
under the required matrix compositions. No expanded tree path is needed
to report the two endpoint IDs.

A point price change affects one heavy-path product and then at most one
light-child dictionary at each ancestor heavy head. There are
$O(\log |T|)$ heads, each costing $O(\log |T|)$. Thus the claimed
$O(\log^2 |T|)$ deterministic update bound is valid.

The implementation must propagate witness and tie metadata as well as
numbers. Equal maximum values can conceal a changed maximizing pair.
Propagating the full head state, or simply continuing unconditionally along
the affected head chain, avoids stale witnesses. This clarification is
present in the audited main note.

## 4. Implicit updates discover both register and guard events

An ancestor-descendant path consists of $O(\log |T|)$ heavy-path
intervals, with each edge indexed by its child. On a donor edge store
$x-\ell$; on a receiver edge store $2\ell-x$. Both buffers decrease
by exactly $\eta$ under the transfer. One lazy range-add/minimum
structure therefore identifies every expired register without inspecting
the complete path.

At an expired register, the exact current $x$ is recoverable from its
orientation, buffer and old register. Resetting $\ell=3x/4$ restores
the buffer to $x/4$ for a donor and $x/2$ for a receiver. A donor
reset changes one maintained tree price. A receiver reset changes only its
non-tree reverse donor price, already covered by Section 2's feasibility
argument.

Register expiration alone does not identify an allocation guard crossing:
different registers have different offsets. The additional guard buffer in
the corrected main note is therefore necessary. With fixed epoch guards
$\chi_e,U_e$, store $x_e-\chi_e$ on a donor and
$U_e-x_e$ on a receiver. Both again decrease by $\eta$. A path
minimum and its witness detect any proposed violation before committing the
step. The two endpoint slack guards are checked directly.

The donor-cost sum is an integer aggregate. Current allocation values can
be read on demand or materialized at epoch end. Full materialization is
charged to epoch rebuilding, not hidden in a cheap path update.

## 5. Grid, positivity, progress and finite arithmetic

Set

$$
V_{\rm up}=\alpha_a+\alpha_b+4\bar L(a,b)/H.
$$

By (A1) it dominates the true one-sided path charge, and (A4) gives
$G=\alpha_a-\alpha_b>V_{\rm up}/4$. Choose a common-grid step with

$$
1/512\le\eta V_{\rm up}\le1/256.      \tag{A6}
$$

A polynomial guard range gives a fixed polynomial $V_{\max}$.
A dyadic primal grid of spacing at most $1/(4096V_{\max})$ has a
multiple in every interval prescribed by (A6). Registers need only the
fixed grid four times finer than this primal grid. Their denominator length
does not grow with the number of resets.

The sum defining $V_{\rm up}$ contains only two endpoint reciprocals
and one integer sum divided by $H$. Its exact numerator and denominator
have $O(\log S)$ bits under the stated guards. This does not require
forming a sum of unrelated reciprocals along the entire path.

Each donor and the terminal slack decreases by less than a $1/256$
fraction. The row equations control receiving magnitudes; the explicit
guards handle the imported finite-range restriction. With
$z=\eta V_{\rm up}$,

$$
\Delta\Phi\ge\eta G-2z^2>z/4-2z^2\ge z/8
                      \ge1/4096.                       \tag{A7}
$$

The endpoint, donor, and receiver updates therefore provide the claimed
positive step whenever a proposed step passes its explicit guards.

## 6. The conservative graph has a valid five-N semantic certificate

For the operative conservative graph, feasible labels imply

$$
0\le\pi_d-\pi_r<\frac1{2x_e}+\frac1H,
 \qquad \pi_d\ge\frac3{4s_d}-\frac1H.                  \tag{A8}
$$

Let $(x',s')$ be the genuine comparison with the same row and bin
equations. Write $h=x'-x$, $h_s=s'-s$, and use the existing
normalized masses $P,Q_s,Q_x$. Conservation gives

$$
\sum_d\pi_dh_{s_d}
 =-\sum_{e=(r,d)}(\pi_d-\pi_r)h_e
 \le\tfrac12Q_x+L|R|/H.                               \tag{A9}
$$

Let $T_s=\sum_d s_d=\sum_d s'_d$, and define

$$
E=\sum_d(s_d\pi_d-5/4)_+.
$$

Separating positive and negative slack changes, using
$(-h_{s_d})_+\le s_d$, and applying (A8)--(A9) proves

$$
\tfrac34P-\tfrac54Q_s-\tfrac12Q_x
                 \le E+(L|R|+T_s)/H.                  \tag{A10}
$$

The actual matching comparison has $P>12N$, $Q_s\le N$, and
$Q_x\le3N$. Hence the left side is strictly greater than

$$
9N-5N/4-3N/2=25N/4.
$$

Choose $H$ also to satisfy $(L|R|+T_s)/H\le N$. Then a promised
improvement requires $E>21N/4$, and **$E\le5N$ is a safe semantic
LOW certificate**. This is consistent with the stronger fresh-state upper
bound (A3).

All terms of $E$ share the fixed primal-grid denominator times $H$.
The fixed potential changes no term except the two endpoint slack terms
during a tree step. Exact maintenance therefore takes constant many
finite-word term replacements. Rebuilding the potential pays for every
changed term.

The earlier true-price certificate in
[slack-potential-semantic-certificate.md](slack-potential-semantic-certificate.md) uses donor coefficient $1/4$
and threshold $E\le6N$. It remains valid for labels feasible for that
different graph. The operative conservative graph only supplies the
coefficient $1/2$ in (A8); it must use (A10), not the six-N screen.

## 7. Register accounting survives changes of epoch and direction

After a reset at value $x_0$, the next reset requires either
$x\le3x_0/4$ or $x\ge3x_0/2$. Thus each reset after the initial
one consumes a fixed positive amount of absolute logarithmic variation.
This remains true if later epochs reverse the incidence's tree role,
because a role change does not itself reset the register.

During a numerical step, only donor allocations contribute negative log
variation, which is at most

$$
2\eta\sum_{\rm donors}1/x_e\le2\eta V_{\rm up}=O(1).
$$

Over a coordinate lifetime, positive log variation is bounded by negative
variation plus its endpoint log difference. Polynomial magnitude guards
bound that difference by $O(\log S)$. Explicit births, deletions and
sets contribute the same endpoint allowance. Therefore the total number of
register resets over $J$ numerical steps is

$$
O\bigl(J+(N+A_{\rm ext})\log S\bigr). \tag{A11}
$$

This is a history-wide count, rather than a per-epoch count. The two slack
endpoint price updates per accepted step add only $O(J)$ point events.

## 8. Exact status and remaining gap

The audited operative interface now has mutually consistent initialization,
threshold detection, fixed-label feasibility, and semantic certification.
It searches every ancestor-descendant bin pair in a supplied fixed forest;
finds and applies a qualifying path implicitly; discovers register and guard
events; and globally charges the register resets. A freshly initialized
forest either contains a passing path or already gives semantic LOW.

None of these results pays for the number of full shortest-path/DP rebuilds
after an old forest is exhausted. Later TREE-EMPTY is only a statement about
that old forest. Its fixed feasible potential may still have $E>5N$,
and useful paths may use non-tree arcs. Constant progress from at least one
step per fresh epoch is not an adequate near-linear rebuilding bound.

The remaining positive theorem must bound actual forest repair or creation
work, not merely re-use (A11) as if a price notification paid for a whole
SPT. No such theorem, and no resulting improved general-matching exponent,
is asserted here.
