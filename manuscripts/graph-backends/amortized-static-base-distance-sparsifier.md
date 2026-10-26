# A short-period distance sparsifier with amortized degree feedback

**Alternative construction, 24 October 2026.** This note composes a
static initial distance spanner, touched-set repair, and amortized
degree feedback. It provides an alternative one-level interface for
the distance backend at the same quantitative 14/15 rate. It does not
improve that rate. In particular, its local work retains the quadratic
dependence on the repair depth required by the literal deterministic
static sparsification theorem.

The construction avoids the worst-case pile-splitting argument in
KMPG Claim 3.18. The same high-degree excess potential and publication
after settlement appear in Kyng--Meierhans--Zöcklein,
arXiv:2408.11375, Claim 4.6 and Algorithm 2; the proof below states the
additional initial-credit and inactive-loop details needed here.
It still imports the stable core forests, their
monotone-cut implementation, the deterministic static sparsifier,
and the stated dynamic-tree primitives. The existing 14/15 construction
is unchanged.

## 1. One-level data and source interfaces

Let the parent be a graph of maximum degree three with initial active
size $`m=|V|+|E|`$, and let $`k\geq2`$ be its reduction parameter.
Consider a parent period containing at most $`c m/k`$ external edits,
where $`c>0`$ is a fixed sufficiently small constant. The period starts
on the maintained nonisolated endpoint list. Newly isolated native
slots are retained for this period and reused upon reactivation.
Historical private isolates from earlier periods are not rescanned.

Use the componentwise stable-forest construction of
[the disconnected-component wrapper](disconnected-component-backend-wrapper.md).
Write $`A=\mathrm{poly}(U)`$ for one fixed polynomial large enough
to include its number of forests, length buckets, ancestor-closure
cuts, and ordinary local indexing factors, where $`U`$ is the common
master bit/size parameter. In particular:

1. Each stable forest component contains at most $`O(k)`$ parent
   vertices. A positive core vertex therefore has current degree at
   most $`Ak`$. A native cut partitions incidences and never merges
   core vertices.
2. Initial core roots incident to positive **nonloop** core edges
   number at most $`Am/k`$. The full private core universe may contain
   $`\Theta(mA)`$ additional loop-only or isolated roots.
3. An external parent edit causes at most $`A`$ native core edits.
   Each requested degree-feedback forest cut causes at most $`A`$
   additional native edits, including its ancestor closure.
4. Native core cuts change the endpoints of existing positive edge
   IDs; they do not create those edge IDs. New positive core edge
   lifetimes arise only from external parent edge births or explicit
   repricing replacements. Their number is at most $`Aq`$ through
   $`q`$ external edits. Equal-root alias links are separate gluing
   records and are not positive-metric spanner inputs.

Items 1, 3, and 4 are the constructive stable-core interface of KMPG
Lemma 3.5 and Claim 3.16. Item 2 uses the explicit small-component
initialization in the wrapper; it is false for the total number of
private core roots.

For each positive length bucket use the literal deterministic static
sparsifier of van den Brand et al., arXiv:2309.16629v1, Theorem 8.1.
Choose a common upper envelope

```math
\Gamma=\exp\bigl(O(U^{2/3}\log(U+2))\bigr)
 \tag{1}
```

for its path-length, congestion, sparsity, and fixed polynomial factors.
The important literal guarantee is

```math
C(\Pi\circ\widehat\Pi)
 \leq \Gamma L(\Pi)\bigl(C(\Pi)+\Delta(J)\bigr),
 \qquad
 L(\Pi\circ\widehat\Pi)\leq\Gamma L(\Pi).
 \tag{2}
```

Its running time is bounded by the actual input size times

```math
A\Gamma^2L(\Pi).
 \tag{3}
```

Here path cardinalities and congestion count parallel demand IDs and
repeated edge occurrences. The input-path-length factor in (2) is
retained throughout this proof.

## 2. An initially small selected base in a larger private universe

Initialize one static sparsifier on the nonloop part of each positive
core and length bucket. Do not allocate selected vertices for the
loop-only private roots. Let $`I_0`$ count all selected edge membership
births in these initial calls, before degree feedback. Then

```math
I_0\leq A\Gamma m/k.
 \tag{4}
```

Equal-root alias stars do not allocate a child graph on the private
universe. Identify equal physical roots before publication, or
equivalently suppress every selected component having no positive
nonloop core edge. An inactive core alias sharing a physical root with
an active alias uses that same external root record. Recursive roots
are counted by endpoints of selected nonloop records and already paid
root births, rather than by all native core slots.

Every registered loop demand has an empty base route with its CURRENT
endpoint incidence records. It remains in the native splitter and in
the touched-demand index. An old loop exposed by a split is not a new
input edge lifetime.

Within one core, use reference counts for ownership of an original
core edge ID by the base and different repair layers. The actual
selected graph contains that edge once, even if several layers own it.
Insertion counts above may count every layer membership and therefore
upper-bound actual selected insertions. Degrees and the preimage
weights passed to the tree partition routine count the deduplicated
selected graph. Thus each physical parent vertex contributes at most
three selected incidences in a given core, as required by FindSets.

Keep all surviving initially selected base edges. Every subsequently
born nonloop input edge is put directly into the base with its identity
route. Remove a demand and its route-index memberships when that
input lifetime dies. Through $`q`$ external edits, at most $`Aq`$ such
direct base births occur. After native cuts or deletions a base route
may be broken, as allowed by the touched-set construction.

The current base route length is at most $`\Gamma`$. Its vertex
congestion is at most $`A\Gamma k`$: surviving initial demand records
can only be partitioned between descendants, and currently live direct
identity routes contribute at most the CURRENT core degree. This
argument does not use a cumulative master-degree bound.

If a loop becomes a nonloop, both resulting endpoints are touched.
Its projected repair demand uses those endpoints and the surviving
central input edge. One may scan $`O(kA)`$ such records locally, but
one must not replace this native split by that many synthetic edge
insertions. The repair graph is sparsified on its touched vertices.

## 3. A prefix repair bound with no large initialization subsidy

Let $`K\geq1`$ be the repair depth. Choose an integer radix

```math
\rho=\left\lceil M_{\rm cap}^{1/K}\right\rceil\geq2,
 \qquad N_{\rm sched}=\rho^K,
 \tag{5}
```

where $`M_{\rm cap}`$ is any polynomial-master upper bound on the
private native universe and the period's native history. This is only
a counter parameter: no array of size $`N_{\rm sched}`$ is allocated.
For example, when the actual parent size is at most $`2^U`$, take
$`M_{\rm cap}=2^{8U}`$ and impose executable size/history guards.
The proof below gives $`m\mathrm{poly}(U)`$ private records, so
this fixed choice eventually suffices without knowing an asymptotic
constant. Then

```math
\log\rho=O(U/K+1).
 \tag{6}
```

Run the touched-set layers of Chen et al., arXiv:2311.18295v1,
Section 7.2, with periods

```math
p_j=\rho^{K-j},\qquad 0\leq j\leq K.
 \tag{7}
```

The clock $`t`$ counts native deletions and splits. A new edge birth
only changes its base identity route. At a multiple of $`p_j`$,
rebuild the least eligible layer and clear all higher layers.
All repair layers start empty. The base is Section 2, rather than the
source's incremental APSP-based spanner.

The usual validity induction is unchanged: an affected edge had a
valid lower-layer route either at the last lower-layer rebuild or at
its own birth. Prefixes up to the first touched vertices are still
valid. A static repair routes the projected edge between these first
touched vertices. Annotated empty loop paths obey the same argument.

The static output is a sparse SUBGRAPH of the projected graph $`J`$.
For each selected projected edge, insert only its central original
core-edge ID into the repair layer. Its prefix and suffix are paths
in lower-layer graphs that are already retained. Do not expand the
embedding of the selected projected edge into new membership births:
route records and selected memberships are different objects.
This is Algorithm 7's separate central-edge selection and route
assignment. It is why a static output of $`O(\Gamma|S|)`$ projected
edges creates only $`O(\Gamma|S|)`$ memberships, even when the
preexisting base routes have length $`\Gamma^{O(K)}`$.

For the recourse bound, a layer of period $`p`$ can first be rebuilt
only when $`t\geq p`$. At a rebuild, its touched set has size at most

```math
O(\min\{t,\rho p\}).
 \tag{8}
```

The factor $`\rho p`$ is the preceding layer's period; clearing by a
lower layer only shortens the interval. Each such rebuild creates at
most $`A\Gamma\min\{t,\rho p\}`$ selected memberships. Through an
arbitrary prefix of length $`t`$, the total contribution of this
layer is at most

```math
A\Gamma\rho p\lfloor t/p\rfloor
                    \leq A\Gamma\rho t.
```

Summing the $`K+1`$ layers, and enlarging $`A`$ to absorb $`K+1`$
when $`K\leq U`$, gives

```math
I_{\rm repair}(t)\leq r t,
             \qquad r=A\Gamma\rho.
 \tag{9}
```

This bound holds for EVERY prefix, including a prefix of an unfinished
feedback cascade. It has no additive $`\Gamma N_{\rm sched}`$ term.
The only initial selected credit is the actual $`I_0`$ in (4).
Private empty roots do not enter the selected graph merely because
they are included in the scheduling upper bound.

Native splitting does not create selected edge memberships. Any
local smaller-side relabeling work is separate from (9); the ordinary
selected endpoint transcript will be bounded in Section 5.

## 4. Degree feedback closes using the actual initial credit

Let $`f`$ be the number of requested degree-feedback forest cuts,
including those at initialization. The fixed native translation gives

```math
t\leq A(q+f),\qquad
 I\leq I_0+Aq+Ar(q+f),
 \tag{10}
```

where $`I`$ counts all selected membership insertions. Calls in
different cores and buckets are included in these totals.

Set

```math
z=\lceil 64Ar\rceil.
 \tag{11}
```

Whenever a positive selected star has degree greater than $`6z`$,
apply KMPG Theorem 3.8 (`FindSets`) to its physical preimage tree.
Because the parent has degree three, the resulting pieces each have
at most $`3z`$ selected incidences, and all but one have at least $`z`$.
If there are $`p`$ pieces, then $`p\geq3`$, and $`p-1`$ cuts are
requested. Extra ancestor-closure cuts only refine this partition.

Use the potential

```math
\Phi=\sum_v(\deg_H(v)-z)_+,
 \tag{12}
```

summed over positive uncontracted core stars. Splits and deletions
never increase it. A selected insertion increases it by at most two.
The requested partition decreases it, before the repair response, by
at least

```math
z(p-2)\geq z(p-1)/2.
```

Starting before the initial selected memberships are inserted therefore
gives, on every partial cascade,

```math
zf/2\leq2I.
 \tag{13}
```

Substituting (10) and using (11) absorbs its feedback term. Hence

```math
\boxed{
 f=O(I_0/z+q),\qquad
 I=O(I_0+Arq),\qquad
 t=O(AI_0/z+Aq).
 }
 \tag{14}
```

Because these are bounds on every finite prefix, they also prove
termination of a proposed infinite feedback cascade. At settlement
every positive selected star has degree at most $`6z`$. Identifying
equal physical roots across the $`A`$-bounded family multiplies this
bound by at most $`A`$; alias gluing is handled after the exact gauge
correction used in the existing distance lift.

There is no circular universe assumption. Equations (4), (9), and
(11) imply $`I_0/z\leq O(Am/k)`$ after enlarging the fixed polynomial
$`A`$. Thus all native slots and cuts during a period with
$`q=O(m/k)`$ fit in $`m\mathrm{poly}(U)`$ private records, well
within the polynomial-master allowance in (5). A guard checks this
before a branch can rely on it.

## 5. Ordinary child edits: keep the initial credit

Treat one external parent edit together with all its feedback as an
atomic publication transaction. No child query or accepted flow step
is allowed during that transaction. The old settled selected graph
has degree at most

```math
D_{\rm sel}=O(Az).
 \tag{15}
```

For an old selected edge surviving continuously, compare only its old
and final physical endpoints. At most $`D_{\rm sel}`$ old incidences
belong to any old core vertex whose descendants are split, regardless
of how often internal labels move during the transaction. New
membership records remain unpublished until settlement; a transient
birth followed by death produces no child edge, and an old death and
reselection is an old retirement plus a new record.

Consequently the ordinary endpoint-edit transcript has size

```math
O\bigl(D_{\rm sel}\,t_{\rm split}
          +I_{\rm member}+D_{\rm member}+V_{\rm born}\bigr).
 \tag{16}
```

Combining this with (14), and charging newly activated selected
endpoints to selected memberships, gives a fixed polynomial envelope

```math
R=(A\Gamma\rho)^{O(1)},\qquad
 \log R=O(U/K+U^{2/3}\log(U+2)),
 \tag{17}
```

under which the initial child size is at most $`O(mR/k)`$ and the
ordinary child prefix after $`q`$ external updates has size at most

```math
O(mR/k+Rq).
 \tag{18}
```

The additive term in (18) is intentional. Even after initialization,
a future feedback cascade may spend potential present in the initial
selected graph. We do not assert a prefix bound $`Rq`$ with no initial
credit. The total initial credit is charged once to this parent's
initialization allowance, even if some of its work occurs late in
the period.

An executable prefix guard for this alternative must accordingly
check $`A_0+Rq`$, with one $`A_0=O(mR/k)`$ budget for the whole parent
period. A guard checking only $`Rq`$ would assert a stronger interface
than this proof. The allowance is an accounting bound, not a padded
child allocation: empty or small actual children are initialized
lazily on their actual records.

Old root labels are not silently renamed to implement smaller-side
splits. Each record retains its physical-root, stable-forest, and
parent-edge provenance. Retire old changed records using their old
metadata before publishing final new records. Pure loop-only native
slots remain private. Every actually published isolated child root
and every retained port-fiber ghost is counted in (18).

## 6. Local work, route reports, and exact flat-lift compatibility

The static base has $`L_{-1}\leq\Gamma`$ and
$`C_{-1}\leq Ak\Gamma`$. The literal recurrence (2) gives

```math
L_j\leq c\Gamma L_{j-1},\qquad
 C_j\leq c\Gamma L_{j-1}C_{j-1},
 \tag{19}
```

and therefore

```math
L_K\leq\Gamma^{O(K)},\qquad
 C_K\leq Ak\Gamma^{O(K^2)}.
 \tag{20}
```

At a rebuild, affected demand records are enumerated from touched
vertices. Their count is bounded by the touched-set size times the
appropriate $`C_j`$. Computing and indexing all new explicit routes
costs their actual total length. Thus the static work and route-change
notifications can be charged by the same geometric-period summation
as in Section 3, with the additional local factor in (20).
Native incidence scans, positive loop awakenings, and physical
`FindSets` scans cost at most $`k\mathrm{poly}(U)`$ per relevant
native event. They remain local work; they are not child edits.
For a local static call, its ambient graph is the union of the
explicit affected routes and central edges, with isolated unrelated
private vertices omitted. It is not obtained by rescanning the entire
selected base or allocating the scheduling universe.

A sufficiently generous common local envelope is

```math
W=k^{O(1)}\rho^{O(1)}
                    \Gamma^{O(K^2)}\mathrm{poly}(U).
 \tag{21}
```

The one-level total local time through $`q`$ external edits is
$`O(mW+qW)`$, including actual-size initialization, complete route
records, and initial-credit feedback. This bound also covers explicit
candidate-circulation changes in the distance cycle reduction.
It does not claim that demand-route congestion is $`k`$-free.

Selected nonloop edges have the same core lengths, gradients, and
physical provenance as in the original distance construction.
Positive core loops remain local fundamental-cycle candidates.
Hence its ASZ comparison, correction-cycle decomposition, and exact
raw lift apply unchanged. The retained-edge gauge correction still
makes equal-root gluing gradients zero before contraction.

The [existing pool and lifetime implementation](distance-degree-reset-candidate.md)
applies to the settled ordinary transcript (18). A parent transaction
retains all old metadata and old pool images until their exact signed
and absolute retirement callbacks have been consumed. It flushes
retiring physical lifetimes before forgetting their records. No
intermediate transaction state is exposed to a raw-cycle query.
Dormant pool counters persist. An internal demand embedding is not a
published flat-forest occurrence, and reindexing that embedding never
creates an uncharged physical pool.

The stable core-forest cut logs obey their own $`A(q+f)`$ bound.
They are processed with the same complete old/new transaction and
with the existing descendant-occurrence factor. Neither the pool
maintenance nor (16) expands each child forest log by a $`k`$-edge
parent path. Thus no extra $`k`$ factor multiplies recursive updates.

### Optional fresh-base normalization after initialization

The additive credit is sufficient for Section 7, but it can also be
removed from the subsequent child transcript by one actual
initialization operation. First perform the initial feedback just
proved, reaching maximum positive selected degree $`6z`$. Before
publishing any child graph, freeze the ENTIRE settled, deduplicated
selected graph as a new base $`H_{\rm base}'`$. For every currently
live demand, copy its current valid highest-owner route into this
base. Clear all repair layers and touched sets and reset the native
clock to zero. No forest, physical root, gradient gauge, input edge
ID, or physical lifetime is reset by this operation.

There are $`O(I_0)`$ frozen selected edges by (14) with $`q=0`$.
Fully flattening all old route owners and rebuilding the inverse
route lists is actual
initialization work. Equations (20) bound their length by
$`\Gamma^{O(K)}`$ and their congestion by $`Ak\Gamma^{O(K^2)}`$;
the total copying cost is absorbed by $`mW`$. Annotated empty loops
are copied as such. Subsequent input births still get direct identity
base routes, and input deaths remove their demand records.

For subsequent feedback use
```math
\Phi'(H)=\sum_v(\deg_H(v)-6z)_+,
```
which starts at zero, and trigger a partition only at degree
$`d>12z`$. The same partition with parameter $`z`$ creates pieces of
degree at most $`3z`$, so its immediate potential drop is
```math
d-6z>d/2\geq z(p-1)/2.
```
The final inequality follows because all but one of its $`p`$ pieces
carry at least $`z`$ incidences. The touched-set repair layers start
empty, so their new memberships have the pure prefix bound (9).
The potential argument now gives $`f=O(q)`$, with no initial term,
and the settled ordinary child transcript after publication has
$`O(Rq)`$ updates. Initialization still has actual size $`O(mR/k)`$.
The maximum settled degree is now $`12z`$, only a constant change.

The new base routes are longer than those of Section 2, but not
enough to change (21). Starting (19) with
$`\log L_{\rm base}'=O(K\log\Gamma)`$ and
$`\log(C_{\rm base}'/(Ak))=O(K^2\log\Gamma)`$ still yields
$`\log L_K=O(K\log\Gamma)`$ and
$`\log(C_K/(Ak))=O(K^2\log\Gamma)`$. In particular no cubic power of
$`K`$ is introduced. Future splits and deletions can only decrease
the ancestor congestion of the frozen route records.

This normalization is performed once, before child publication, in
each parent period. Repeating a global route copy after every update
would not have the claimed cost. The unnormalized construction and
the safe initial-credit recurrence below remain valid independently
of this optional step.

## 7. The same 14/15 recurrence

Apply the existing fixed port-fiber degree reset after the settled
selected graph. Take a port cap $`C=R^{O(1)}`$, and enlarge
$`P=R^{O(1)}`$ to cover the fiber size, child edit encoding, root-pool
factor, and additive initial credit. The root fiber identities,
inactive-fiber suppression, and exact scaling remain those of the
degree-reset construction.

For $`r`$ remaining levels write $`G_r`$ for flat occurrence/answer
size, $`J_r`$ for an initial ALLOWANCE per parent record, and $`T_r`$
for amortized update work. The allowance includes work caused later
by initial recourse credit; it is not a claim that all of that work
is done at initialization. With fixed constants safe coupled bounds
are:

```math
\begin{aligned}
 G_r&\leq P(G_{r-1}+1),\\
 J_r&\leq W+P(G_{r-1}+1)
                   +(P/k)(J_{r-1}+T_{r-1}),\\
 T_r&\leq O\bigl(kW+kP(G_{r-1}+1)\bigr)
                   +O(P)(J_{r-1}+T_{r-1}).
 \end{aligned}
 \tag{22}
```

In the second line, $`(P/k)J_{r-1}`$ charges the actual small child.
The separate $`(P/k)T_{r-1}`$ term charges the $`mP/k`$ child UPDATES
that may occur later when initial recourse credit is spent. Calling
that credit an initialization allowance does not make those updates
cost $`J_{r-1}`$ each. On a completed parent period, dividing the
entire allowance by $`\Theta(m/k)`$ parent edits contributes
$`O(P)(J_{r-1}+T_{r-1})`$. The ordinary $`P`$ child updates per parent
edit fit in the same term. Initial or incomplete periods retain the
displayed $`mJ_r`$ allowance. The full initial credit is not recharged
after every edit.

To solve these coupled bounds, set $`H_r=J_r+T_r/k`$. Since
$`(J_{r-1}+T_{r-1})/k\leq H_{r-1}`$, equations (22) imply

```math
H_r\leq c\bigl(W+P(G_{r-1}+1)\bigr)+cP H_{r-1}
```

for a fixed $`c`$, while $`G_r\leq P(G_{r-1}+1)`$.
Consequently $`H_r\leq (c'P)^{r+1}W`$ after enlarging the common
local/base envelope, and
$`J_r\leq H_r,\ T_r\leq kH_r`$. Thus there is one overall polynomial
factor in $`k`$, not a factor $`k`$ at every recursive level.

Let $`x=\log k`$. The recursion has depth $`O(U/x)`$. Equations
(17), (21), and (22) give a total logarithmic overhead bounded by a
constant multiple of

```math
x+K^2U^{2/3}\log(U+2)
       +\frac{U^2}{Kx}
       +\frac{U^{5/3}(K+1)\log(U+2)}{x},
 \tag{23}
```

plus smaller logarithmic terms. The $`K`$ part of the last term
explicitly includes multiplication of the one-level
$`\Gamma^{O(K)}`$ quality loss through $`O(U/x)`$ levels.
With

```math
K=\Theta\bigl(U^{2/15}(\log(U+2))^{-2/5}\bigr),\qquad
 x=\Theta\bigl(U^{14/15}(\log(U+2))^{1/5}\bigr),
 \tag{24}
```

this is $`O(U^{14/15}(\log(U+2))^{1/5})`$. Literal integer choices,
master length/gradient caps, raw-certificate computation, and finite
guards can be those of the current 14/15 degree-reset note, with their
fixed constants enlarged. This alternative batching proof does not
invoke the old restriction $`K=o(\log^{1/6}m/\log\log m)`$ from the
different KMPG worst-case spanner theorem. Its elementary clock
construction only requires $`K\leq O(U)`$, and its static calls use
the stated actual-input static primitive.

For the finite program, replace the analytical factors $`A,\Gamma,r,z`$
by the existing declared dyadic caps of the form
$`2^{c_C(\lceil U/K\rceil+\lceil U^{2/3}\rceil \lceil\log_2(U+4)\rceil+\lceil\log_2(U+4)\rceil)}`$, raised to fixed
powers where needed. Use one such cap for the feedback threshold and
check the selected-membership prefix on every intermediate cascade.
Some fixed enumerated $`c_C`$ eventually dominates all the fixed
polynomial and static-source constants. Thus no unknown asymptotic
constant is supplied as executable advice. The child prefix guard is
the initial-credit guard just specified, rather than a pure $`Rq`$
guard.

The maximum stretch of a one-level spanner is
$`\Gamma^{O(K)}`$. Its multiplication through the hierarchy and the
single terminal local extraction factor fit within (23). The
arbitrary-graph matching driver, exact projection recovery, and
finite-program verification wrapper are not changed by this note.

## 8. What this alternative does and does not establish

Subject to the named stable-core, static-sparsifier, and dynamic-tree
interfaces, the construction supplies actual-size initialization,
bounded selected degree, a complete settled ordinary transcript,
explicit short demand routes and route-change reports, and the
existing exact raw flat lift. Its prefix child bound includes the
necessary initial credit. Arbitrarily many initially loop-only cores
are not charged as child vertices or selected initial edges.

This replaces the source's worst-case degree-control dependency by
the explicit amortized potential and publication argument above.
It retains the current 14/15 asymptotic envelope. Removing the
$`L(\Pi)`$ congestion factor in (2), or proving a different route
repair theorem, could improve the local-work recurrence. That alone
does not imply an 8/9 raw-backend bound: the accumulated
$`O((U/x)K\log\Gamma)`$ inverse-quality exponent must also fit the
new target. Under the naive balance $`x\asymp K\log\Gamma`$ this
quantity is $`\Theta(U)`$. Neither a better static theorem nor a
better full quality balance follows from cheap base initialization
or from degree feedback alone.

## Primary references

* [Kyng, Meierhans and Probst Gutenberg, arXiv:2311.06402v1](https://arxiv.org/pdf/2311.06402v1),
  Lemma 3.5, Theorem 3.8, and Claims 3.16--3.18.
* [Chen, Kyng, Liu, Meierhans and Probst Gutenberg, arXiv:2311.18295v1](https://arxiv.org/pdf/2311.18295v1),
  Section 7.2, Algorithm 7, Lemma 7.14, and the geometric rebuild
  argument in Lemma 7.16. Its length-free restatement of static
  congestion is not used here.
* [van den Brand et al., arXiv:2309.16629v1](https://arxiv.org/pdf/2309.16629v1),
  Theorem 8.1 and its proof, including the input-path-length factor.
* [Kyng, Meierhans and Zöcklein, arXiv:2408.11375](https://arxiv.org/pdf/2408.11375),
  Claim 4.6 and Algorithm 2, for an independent primary precedent for
  amortized degree feedback and child publication after settlement.
