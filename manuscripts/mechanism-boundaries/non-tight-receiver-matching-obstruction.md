# A matching comparison that needs a non-tight receiving arc

**Research construction, 25 October 2026. Root mathematical review completed.**

See [non-tight-receiver-and-batch-repairs-root-audit.md](../graph-backends/non-tight-receiver-and-batch-repairs-root-audit.md) for the
review, including the corrected 4C preparation trigger and the exact
scope of the fixed-potential obstruction.

The bidirectional compatible-forest interface removes an orientation
obstruction of the older directed-tree search. This example isolates a
different obstruction. Even searching every ordinary path whose receiving
arcs are tight for the old feasible labels can become empty while a strong
path and a large matching comparison survive.

The physical input has actual matching gap one. Preparation uses legal
strong numerical directions of the original general raw-cycle client.
It does not claim that a deterministic policy always choosing the globally
largest source score must reproduce those preparatory choices. The tested
interval starts from fresh exact conservative-price labels; its exhaustion
is independent of the choice among currently passing compatible paths.

This obstructs completeness with permanently fixed labels. It is not a
running-time lower bound for a repaired matching algorithm.

The matching ledger and expansion contracts are those reconstructed in
current_checkpoint/fresh_general_matching_client_interfaces.md and
current_checkpoint/ledger_algebra_and_phase_budget.md. The numerical
threshold, persistent registers, and finite-grid step are those of
any_source_fixed_tree_matching_interface.md.

## 1. A connected subcubic nonbipartite input with gap one

Take two copies of the five-vertex alternating path
```math
c-q-b-r-a
```
with matching edges qb and ra. Vertices c,c' are free. Join the contacts
a,a' through the unmatched edges ap and za' and matching edge pz.
The main twelve-vertex path has matching size five.

Add four paired-remainder vertices u,v,w,t, matching edges uv and wt,
and unmatched edges pu,vw,wu. The triangle u,v,w is attached by pu.
The connected graph has maximum degree three and
```math
N=16.
```
Its initial matching has size seven. Flipping the augmenting main path
from c to c' and keeping uv,wt gives a perfect matching of size eight.
The true gap is exactly one.

The triangle lies entirely in the paired remainder throughout the
construction. It creates no extra contact of an active top bin.
The only eventual top contacts are a-to-p and a'-to-z.

Use K=1, singleton weights one, zero ordinary top debt, and
```math
L=10000CN,\qquad C\ge100.                 \tag{1}
```
Use the standard sufficiently fine dyadic grid and polynomial H.
Negligible positivity-service padding can be absorbed in the strict
margins below.

## 2. Legal preparation with the actual cached threshold

The source rule is cached slack at least 4C. Actual slack at least
3C is only a necessary consequence of eligibility; it is not a
sufficient trigger. During preparation refresh the two endpoint
slack caches exactly after every numerical path step, and refresh
structurally changed slacks exactly after an expansion. This is
O(1) extra slack records per step and is legal under the cache
accuracy contract. It does not reset the allocation registers.

Start from free c and expand qb. The standard top expansion gives
```math
x_{qc}=C+1,\qquad x_{qb}=L-C-1,\qquad s_b=1.
```
Increase b's slack to its first crossing of 4C along b-to-q-to-c.
The donor and terminal are L-O(C), so its true ratio stays above
one half. Use legal steps with every relative motion at most 1/256;
the original raw client's smaller steps are sufficient. The first
eligible exact cache is then in [4C,(257/256)4C].

Expand ra from the eligible b. It places C+1 on rb and L-C-1 on ra,
gives a slack one, and leaves
```math
3C-1\le s_b\le3.015625C-1,\qquad s_a=1 .
```

The missing reduction of b is numerical, not another expansion.
Transfer along a-to-r-to-b until b first falls to at most 2.04C.
This keeps
```math
3C\le s_a+s_b\le3.015625C .
```
Before the last step, s_b>2.04C and s_a<.976C. Its size is at
most s_a/256<.004C. Hence the resulting slacks obey
```math
2.03C\le s_b\le2.04C,\qquad
                    .96C\le s_a<.986C .                     \tag{2}
```

This intermediate path does not need a one-sided ratio above one
half. It passes the one-sided one-quarter threshold, and is a
strong direction for the original full-log raw objective. At
every point in this transfer its positive and negative normalized
full-log masses per unit are
```math
P_{\rm raw}=1/s_a+1/(C+s_a)>1.51/C,\qquad
 Q_{\rm raw}=1/s_b+1/(L-C-s_a)<.493/C .
```
Thus P_raw>3Q_raw and its full-log ratio is greater than one half.
The limiting one-sided ratio is about one third, not one half.
The conservative one-sided score is also positive:
.75/s_a-1.25/s_b exceeds .14/C, while its sole donor price is
O(1/L). There is no reliance on an unavailable strong one-sided
comparison in this stage.

Increase a's slack to its first crossing of 23C/8 along
a-to-r-to-b-to-q-to-c. Both donors and the terminal stay L-O(C),
so this has one-sided and full-log ratios above one half. The
normalized step leaves
```math
23C/8\le s_a\le2.9C<3C.                 \tag{3}
```
Bin b is internal and its slack stays fixed.

Write s=s_b and a_0=s_a. The resulting exact top equations are
```math
\begin{aligned}
 x_{rb}&=C+a_0,             &x_{ra}&=L-C-a_0,\\
 x_{qb}&=L-2C-a_0-s,        &x_{qc}&=2C+a_0+s,\\
 s_c&=L-3C-a_0-s .
\end{aligned}                                                     \tag{4}
```
All rows sum to L, and every bin has load plus slack L-C. Every
coordinate is positive and guarded. The only remainder contact a
stays below 3C.

These prescribed preparatory paths are admissible outputs of the
original general direction oracle: all have full-log ratios above
one half and valid positive-progress steps. In the two stages whose
terminal is c, every decreasing donor and the terminal slack have
size L-O(C), so their full-log ratios have still wider margins.
The intervening small-terminal stage uses the explicit calculation
above. Smaller legal raw steps preserve all overshoot bounds.
No fast preparation-time guarantee is claimed.

The paths need not maximize the global source score once b competes
with a. This is the precise preparation-policy qualification. At
every actual expansion, however, the exact cache satisfies the
required 4C trigger; no use is made of its weaker 3C consequence.

Prepare the other copy identically. Leave pz and the decoration
unexpanded.

## 3. Lower ledgers and the no-action condition

For every integral floor c_0<=C, a debt-free allocation is
```math
x^{(c_0)}_{ra}=L-c_0,\quad x^{(c_0)}_{rb}=c_0,\qquad
 x^{(c_0)}_{qb}=L-2c_0,\quad x^{(c_0)}_{qc}=2c_0.             \tag{5}
```
The residuals at a,b are c_0 and at c are L-2c_0>=c_0.
All singleton floor requirements hold. No equality between different
integral-floor ledgers is imposed.

At the tested interval's beginning, a,a' are the only remainder
contacts and have slack below 3C, hence below 4C in the exact caches.
No physical edge joins two top bins.
Ordinary top debt is zero. No expansion, contraction, or debt-funded
peel is being postponed. The actual gap-one augmenting path remains.

## 4. Fresh exact conservative labels are centered at b

Initialize each coordinate's register to ell=3x/4 at its birth,
and retain the usual hysteretic registers throughout preparation.
Do not reset them just because the tested interval begins.
These conservative allocation registers can be maintained as
auxiliary records during the original raw-client preparation;
they are distinct from the exact endpoint slack caches used for
eligibility. All preparatory paths have constant length, so
servicing those auxiliary records requires no implicit long-path
operation.

The receiver rb grows from x_0=C+1 to C+a_0 in
[3.875C,3.9C]. Each preparatory step raises it by at most
2.9C/256<.012C. At the j-th upward reset its value x_j lies
between 1.5x_(j-1) and 1.5x_(j-1)+.012C. Its third crossing
therefore occurs by
```math
x_3\le3.375(C+1)+.012C(1+1.5+2.25)<3.875C
```
for C>=100, and must occur before preparation ends. Its fourth
crossing is beyond 5.0625(C+1)>3.9C, so exactly three occur.
The retained register thus satisfies
```math
\ell_{rb}=(3/4)x_3\ge(81/32)(C+1)>2.53C,\qquad
              \bar c_{rb}/H<.1/C                           \tag{6}
```
after allowing the small integer rounding term.

The large donor qb changes by only O(C) during preparation,
so its birth register .75(L-C-1) is never crossed. Its price
is O(H/L). All other registers are reused as well.
The source offer at b is at least
```math
\sigma_b/H\ge .75/(2.04C)-1/H>.367/C .
```
The price of b-to-r-to-a is below .1/C after division by H.
Its offer at a exceeds .267/C, while a's direct offer is below
```math
.75/((23/8)C)<.261/C .
```
The donor qb is L-O(C), so b's offer at c exceeds .36/C.
The direct offer of c is O(1/L); a's offer anywhere cannot exceed
its own direct offer, because ordinary costs are nonnegative.

Hence b is the unique first bin in the exact conservative SPT.
Its ordinary part is
```math
b\longrightarrow r\longrightarrow a,\qquad
          b\longrightarrow q\longrightarrow c.              \tag{7}
```
Fix these exact labels D. They satisfy
```math
\begin{aligned}
 D(r)&=D(a)=D(b)+\bar c_{rb},\\
 D(q)&=D(c)=D(b)+\bar c_{qb}. 
\end{aligned}                                                     \tag{8}
```
Donor prices are positive integers. Thus r-to-b and q-to-b are
non-tight receiving directions. Only r-to-a and q-to-c are tight.

This concerns the entire ambient ordinary component, which is already
the tree c-q-b-r-a. There is no missing off-forest physical edge.

## 5. Exhausting every old-potential-compatible path

Allow every donor direction and precisely the old-D-tight receiving
directions. The only nontrivial simple bin-to-bin paths are
```math
b\to r\to a,\qquad b\to q\to c.       \tag{9}
```
A or c can use its donor into its incident row, but the only available
receiver returns to that same bin; this backtrack reaches no other bin.

The b-to-a path never passes. Initially
```math
\sigma_b/H\le .75/(2.03C)<.37/C,\qquad
 \tau_a/H\ge1.25/(2.9C)>.431/C.                              \tag{10}
```
Its donor cost is nonnegative. Every accepted path is consequently
b-to-q-to-c. It increases s_b, decreases s_c, and leaves s_a and the
r-incidences fixed, so (10) only strengthens. Fixed-D feasibility
is preserved by the operative accepted-step proof.

Put
```math
T=s_b+s_c=L-3C-a_0.                 \tag{11}
```
Throughout this interval x_qb=s_c+C. The current register bound gives
bar c_qb/H<1/(2(s_c+C))+1/H. While s_b<=T/10,
```math
\sigma_b/H\ge7.5/T-1/H
```
but
```math
\tau_c/H+\bar c_{qb}/H
 \le1.25/(.9T)+1/(2(.9T+C))+2/H<2/T+2/H .
```
The path still passes. At exhaustion, therefore,
```math
s_b>T/10.                     \tag{12}
```

Acceptance before any step also implies s_b<(3/5)s_c.
After its small step,
```math
s_b^{\rm new}/s_c^{\rm new}
 <(257/255)(3/5)<.605 .
```
The initial state satisfies the same bound. Consequently s_c>.62T
throughout, and x_qb remains large. All other allocations are unchanged
or increase from their positive initial values. There is no guard event.

Only s_b has positive log-slack motion. Total objective gain is
O(log(L/C)), so constant progress forces exhaustion in that many
accepted steps. With two copies, any allowed choice just chooses
which copy's b-to-c path to use. Both exhaust in the same asymptotic
total bound.

Then every ambient old-potential-compatible path has nonpositive
threshold score. Contacts a,a' still have slack below 3C, and the
large-slack bins have no remainder contact. No matching action has
become eligible.

## 6. A strong matching comparison and large E remain

At exhaustion consider
```math
a\to r\to b.                  \tag{13}
```
Its donor is L-C-a_0=L-O(C), its terminal slack exceeds T/10,
and its start slack is at most 2.9C. Its true ratio is greater
than one half for (1).

Transfer delta=L/20 on this path. The donor exceeds delta and
s_b>T/10>.09L>delta, so the comparison is feasible. It gives
```math
P=\delta/s_a\ge L/(58C)>12N,\qquad
 Q_s=\delta/s_b<1,\qquad Q_x=\delta/x_{ra}<1.                 \tag{14}
```
The missed direction has the matching comparison's required large
normalized positive mass; it is not merely an isolated small-gain
cycle. The physical graph still independently has matching gap one.

The fixed screen is large as well. Initially
```math
\pi_b=(A-D(b))/H=\sigma_b^{\rm initial}/H>.367/C.
```
It stays fixed while s_b>T/10>.09L. This one term of E exceeds
.033L/C-5/4, already far above 5N.

## 7. Scope: repairing the fixed-potential compatibility contract

Path (13) uses r-to-b, whose old label gap is
```math
D(r)-D(b)=\bar c_{rb}^{\rm initial}>0.    \tag{15}
```
No physical forest choice can make it old-D-tight. The whole ambient
compatible graph was already searched. This reverses an old donor
as a receiving arc, unlike the harmless reverse of an old tight
receiver in the earlier directed-tree obstruction.

An algorithm retaining the compatibility contract must change the
labels to enable this path. An algorithm may instead allow receiving
arcs that are not tight. The bidirectional forest path DP and its
numerical update machinery still work in that larger family; what
is no longer supplied for free is feasibility of the old potential
and the associated semantic screen. Here the whole ordinary graph
is a forest, so allowing every receiver finds (13) immediately.
The obstruction does not rule out that alternative.

Fresh exact labels can enable a strong path. This note does not
lower-bound the work required to obtain or maintain them. It proves
only that indefinitely frozen-potential compatibility is incomplete,
even when all compatible paths are provided and a large feasible
matching comparison is still necessary.

Preparation is deliberately quantified: the state is reachable by
legal strong numerical outputs of the original client, after which
the tested interval begins with fresh exact conservative labels.
The note does not assert that every new deterministic preparation
rule visits this state, or that such a visit forces many expensive
refreshes.

