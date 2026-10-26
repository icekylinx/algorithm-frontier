# Multiple-resource choices: a monotone charge and a repair obstruction

**Research analysis, 25 October 2026.** A monotone majorant successfully
extends the fractional deletion charge to multiple-resource options.
It does not make arbitrary feasible old assignments cheaply repairable.
Both facts are proved below. Neither is a general matching improvement.

## 1. Model

There are $`M`$ groups. Group $`g`$ has a finite initial option
family $`\mathcal P_g`$, of size at most $`L`$. Each option
contains at most $`D`$ resources. Resource deletions remove every
option containing that resource. A group retires after its final
option disappears. Among its surviving options it has the uniform
fractional distribution.

Write $`s_g`$ for its current option count and

```math
\mu_e=\sum_{g:s_g>0}
       \frac{|\{P\in\mathcal P_g:e\in P\text{ and }P
                        \text{ survives}\}|}{s_g}.
 \tag{1}
```

Unlike the single-resource case, $`\mu_e`$ can decrease while
$`e`$ survives: another resource can kill an option that also used
$`e`$. Define a monotone majorant on each surviving resource by

```math
\widehat\mu_e(0)=\mu_e(0),\qquad
 \widehat\mu_e\leftarrow\widehat\mu_e+
                              \max\{0,\mu_e^{new}-\mu_e^{old}\}.
 \tag{2}
```

The majorant is discarded only when its resource is deleted. It
always dominates the current fractional load.

## 2. The majorant mass is small over the complete history

Consider one group with $`s`$ options before an update, of which
$`r`$ disappear. When $`r<s`$, every surviving option's weight
increases by

```math
\frac1{s-r}-\frac1s
                         =\frac{r}{s(s-r)}.
```

The sum of positive resource-load changes attributable to this group
is at most the total increase contributed by surviving options;
negative contributions from removed options can only reduce it. Since
the surviving options have at most $`D(s-r)`$ resource occurrences,

```math
\sum_e\max\{0,\Delta\mu_{e,g}\}
          \leq D(s-r)\frac{r}{s(s-r)}=D\frac rs.
 \tag{3}
```

If $`r=s`$, the group retires and every contribution decreases to
zero, so the positive change is zero. Summing groups can only reduce
the sum of positive coordinate changes:

```math
\sum_e\max\{0,\sum_g\Delta\mu_{e,g}\}
       \leq\sum_g\sum_e\max\{0,\Delta\mu_{e,g}\}.
```

For each group, batched deletions have

```math
\sum_{\text{its updates}}\frac rs
        \leq \sum_{j=1}^{s_g(0)}\frac1j
        \leq 1+\log L.
 \tag{4}
```

Indeed, a deletion of $`r`$ from a set of size $`s`$ charges no
more than $`\sum_{j=s-r+1}^{s}1/j`$, and these ranges do not
overlap over the group's lifetime.

The initial mass is at most $`DM`$. Equations (3)--(4) prove

```math
\text{total mass ever created in all }\widehat\mu_e
                      =O(DM(1+\log L)).
 \tag{5}
```

In particular, the sum of majorants charged immediately before their
resources are deleted obeys the same bound: each unit of created
majorant mass is charged at most once. Formula (5) is also valid at
every chronological prefix, with the same one-time initial credit.

The proof extends to nonnegative occurrence multiplicities whose sum
on any option is at most $`D`$. Thus an option can be a walk whose
resource accounting counts repeated occurrences, if deletion kills
the whole option whenever it uses the deleted resource.

### Consequence if an integral assignment is maintained

Suppose one could maintain one option per live group while respecting
monotone capacities

```math
c_e=\lceil C\widehat\mu_e+b\rceil,
                  \qquad C\geq1,\ b\geq1.
 \tag{6}
```

At a resource deletion, at most $`c_e`$ selected groups lose their
option. Consequently the total number of directly forced orphan
events after $`Q`$ deletions is

```math
O(CDM\log(L+2)+(b+1)Q).
 \tag{7}
```

Equation (7) counts directly invalidated choices. It does not count
other groups moved to restore feasibility, nor the work of finding
those moves. Those are separate obligations.

### A finite dyadic implementation of the majorant

The exact uniform expressions above are convenient for analysis, but
adding many unrelated fractions $`1/s_g`$ should not be treated as
constant-word arithmetic. There is a simple dyadic replacement.
Give each surviving option of group $`g`$ weight

```math
w_g=2^{-\lfloor\log_2 s_g\rfloor}.
```

Its total group mass lies between one and two. Initialize the resource
majorant with these dyadic option loads. When options disappear, do
not subtract their mass from surviving-resource majorants. When
$`w_g`$ increases, add its increase once for each occurrence of
each still-surviving option of that group. This majorant dominates
both the current dyadic load and the current uniform load.

At a dyadic weight change, the total newly added mass for one group
is at most $`2D`$. There are at most $`1+\log_2 L`$ such changes.
Thus (5)--(7) remain valid up to absolute constants. Every value has
a common power-of-two denominator at most $`2L`$, and its numerator
has $`O(\log(DML+2))`$ bits. Scanning surviving option occurrences
at these changes costs at most the initial occurrence inventory times
$`O(\log L)`$. No fast integral-repair procedure is hidden in this
bookkeeping claim.

## 3. The capacity condition gives a static strong-Haxell instance

For completeness, the majorant has a useful static interpretation.
Replace resource $`e`$ by $`c_e`$ disjoint slots. For every option,
allow all choices of one slot for each resource it uses. These are
rank-at-most-$`D`$ hyperedges, with one group vertex on the left.

If a set $`X`$ of slots hits every clone realization of a particular
option, it must contain *all* slots of at least one resource in that
option. Otherwise one could choose an unhit slot independently for
every resource of that option. Let

```math
F=\{e:\text{every slot of }e\text{ lies in }X\}.
```

If $`X`$ hits all options of a group set $`S`$, every option of
every group in $`S`$ contains a resource of $`F`$. Averaging over
their fractional distributions yields

```math
|S|\leq \sum_{e\in F}\mu_e
      \leq \sum_{e\in F}\widehat\mu_e,
 \qquad
 |X|\geq\sum_{e\in F}c_e\geq C|S|.
 \tag{8}
```

Thus the clone hypergraph satisfies strong Haxell expansion at least
$`C`$. Taking $`C\geq dD^2`$ fits the static regime of
Bucić--He--Huang--Saranurak,
[arXiv:2511.02214v1, Theorem 1.5]
(https://arxiv.org/html/2511.02214v1).

That theorem is not yet a router update theorem. An option with
$`D`$ resources has a Cartesian product of slot realizations, so
the explicit hypergraph can be huge. Their implicit half-layer
interface would need an implementation. More importantly, neither
(8) nor the static theorem promises low reassignment recourse after
each new deletion.

## 4. A layered counterexample to arbitrary-state short repair

Here is an explicit obstruction to the statement:

> Any old assignment feasible for (6) can be repaired after one
> resource deletion using only $`O(D\mathrm{polylog}M)`$
> other group changes.

The obstruction works for every integer $`C\geq1`$, including
$`C\geq dD^2`$. Set

```math
A=4C-1,\qquad D\geq2,\qquad b=3t,
 \tag{9}
```

where $`t\geq1`$ is an integer. We may choose $`b`$ to be a
sufficiently large multiple of the logarithm of the resource universe;
the construction does not depend on a small additive reserve.

### 4.1 Resources and groups

There is a top group $`g_*`$, a private resource $`x`$, and
$`A`$ disjoint blocks of $`D`$ level-zero resources. The options
of $`g_*`$ are its singleton $`\{x\}`$ and those $`A`$ blocks.

Each internal resource $`v`$ at level $`j`$ has $`c_j`$
resident groups. Every resident group of $`v`$ has the same
$`A+1`$ options:

* the singleton $`\{v\}`$;
* $`A`$ disjoint blocks, each containing $`D`$ fresh child
  resources at level $`j+1`$.

The child blocks of distinct parent resources are disjoint. All
groups use the uniform distribution on their surviving options.
There are $`h`$ levels of internal resources, numbered
$`0,\ldots,h-1`$. Their level-$`h`$ child resources have no
resident groups and will provide the final free capacity.

Define the resident counts by

```math
c_0=4t+1,\qquad
 c_j=\left\lceil\frac{c_{j-1}+4b}{3}\right\rceil
                       \quad(1\leq j<h).
 \tag{10}
```

All these counts are $`\Theta(b)`$; they remain between positive
constant multiples of $`b`$.

### 4.2 The old assignment exactly fills the internal capacities

Initially choose $`\{x\}`$ for $`g_*`$, and choose the
singleton $`\{v\}`$ for every resident group of every internal
resource. Thus resource $`v`$ at level $`j`$ has selected load
exactly $`c_j`$.

For a non-root internal resource, its fractional load is

```math
\mu_v=\frac{c_j+c_{j-1}}{A+1}
                         =\frac{c_j+c_{j-1}}{4C}.
```

Consequently its capacity in (6) is exactly

```math
\left\lceil C\mu_v+b\right\rceil
 =\left\lceil\frac{c_j+c_{j-1}}4+b\right\rceil=c_j.
 \tag{11}
```

The last equality follows directly from (10):
$`0\leq3c_j-(c_{j-1}+4b)\leq2`$.

Before deleting $`x`$, each level-zero resource has

```math
\mu_v^{old}=\frac{c_0+1}{4C}.
```

Its capacity is

```math
\left\lceil\frac{c_0+1}{4}+3t\right\rceil
        =\lceil4t+1/2\rceil=4t+1=c_0.
 \tag{12}
```

The private resource has ample capacity for its single selected group.
Leaf resources have no selected groups. The entire old assignment is
therefore feasible, and every internal resource is full.

### 4.3 One deletion leaves the relevant capacities unchanged

Delete $`x`$. Only $`g_*`$'s singleton option disappears. The
top group is the only directly forced orphan. Its remaining options
are the $`A`$ level-zero blocks.

At a level-zero resource, its new fractional load, and hence its
majorant after this first update, is

```math
\widehat\mu_v
                     =\frac{c_0}{4C}+\frac1{4C-1}.
```

Its capacity is still $`c_0`$, because

```math
\left\lceil C\widehat\mu_v+b\right\rceil
  =\left\lceil4t+\frac14+\frac{C}{4C-1}\right\rceil
  =4t+1.
 \tag{13}
```

Here $`1/4<C/(4C-1)\leq1/3`$. No lower-level fractional load
or majorant changes. Thus there is no newly available capacity at an
internal resource that could absorb the new choice for free.

The example also works with the finite dyadic majorant above. Choose
$`C`$ to be a power of two. Every initial group has exactly
$`4C`$ options, so its dyadic weight initially equals its uniform
weight. After deleting $`x`$, only the top group's weight doubles,
to $`1/(2C)`$. A level-zero resource's capacity then becomes

```math
\left\lceil c_0/4+1/2+b\right\rceil
                    =\lceil4t+3/4\rceil=c_0.
```

All other calculations are unchanged. The obstruction therefore does
not depend on using large rational denominators.

### 4.4 Every repair changes a branching number of groups

Any new option for $`g_*`$ occupies $`D`$ full level-zero
resources. At least $`D`$ resident groups must therefore leave
their old singletons. Each such changed resident must use a block of
$`D`$ child resources. Those resources were also full.

Let $`R_j`$ be the number of level-$`j`$ resident groups whose
final selected option is no longer their singleton. Counting final
resource loads, rather than following a particular repair algorithm,
gives

```math
R_0\geq D,\qquad
                    R_{j+1}\geq D R_j.
 \tag{14}
```

There is no cancellation in this count: only resident groups of a
resource can free its original capacity, and each moved group uses
exactly $`D`$ resources one level below. Any additional rearrangement
can only increase the required departures. Hence

```math
R_{h-1}\geq D^h,
 \qquad
              \text{total changed groups}\geq
                              D+D^2+\cdots+D^h.
 \tag{15}
```

Feasible repairs exist, since the final child resources are initially
empty. They can be obtained by moving the necessary groups down the
tree. The lower bound is a recourse obstruction, not an infeasibility
example.

There are $`\Theta((AD)^h)`$ internal resources up to constant
factors, and

```math
M=\Theta(b(AD)^h)
```

resident groups. For fixed $`C,D`$, (15) is polynomial in
$`M/b`$, with exponent $`\log D/\log(AD)>0`$. In particular,
$`D=2`$ and fixed $`C`$ contradict a logarithmic per-orphan
repair bound even when $`b=\Theta(\log R)`$.

## 5. What the counterexample does and does not exclude

The example rules out deriving short individual repairs from just
capacity feasibility and a strong-Haxell surplus. A dynamic algorithm
would need an additional invariant, or an amortized potential that
pays for large cascades from its initial credit and replenishes that
credit under actual updates.

It does **not** refute a total bound such as
$`(M+Q)\mathrm{polylog}(MR)`$. One cascade in (15) can be
paid from an $`O(M)`$ initialization allowance. Nor does it force
every algorithm to start in this saturated old assignment. A carefully
chosen maintained assignment could avoid this particular state.

The static hypergraph algorithm's alternating forest is rooted at
the currently unmatched groups, but its half-layer calls may inspect
the full option graph and move many matched groups. Its static
signature argument does not directly pay for restarting that forest
after every deletion. A useful dynamic import would have to prove a
single history-wide potential, together with the costs of its implicit
half-layer oracle and the complete reassignment transcript.

The monotone majorant (5) supplies a real part of that potential
accounting: direct failures and capacity growth have a finite grouped
charge. It does not supply the missing bound on the branching repair
process. This distinction remains essential before using the result
to remove the repeated-quality factor in the general matching router.
