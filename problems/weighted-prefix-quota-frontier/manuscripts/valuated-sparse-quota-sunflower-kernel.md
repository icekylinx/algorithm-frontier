# Labeled sunflower kernels for sparse numeric quotas and valuated completion

**25 October 2026. Increment U. Complete manuscript-level proof with independent internal review.**

This note gives a deterministic polynomial-time reduction on an explicit
item ground equipped with a minimum-valuated matroid. The constraints have
sparse, bounded, nonnegative integer upper columns. Additional constraints
are preserved by replacement classes. The objective is the full valuation,
which may include the optimal cost of a large, unexpanded completion.

The retained ground has no logarithmic dependence on the number of rows or
items. The proof combines coefficient-consistent sunflowers with disjoint
overlap-first optimization layers. Every deletion preserves a replacement
against contexts in the **original** instance.

The application to the root-cap model of BF gives a uniform polynomial-time
**positive-capacity kernel** even with binary resource counts and arbitrary
signed costs on quota-free coordinates. All such zero coordinates and the
original resource/completion oracle remain available. This is not a
parameter-only bit kernel or a claim that every binary unit is explicitly
listed in the output.

## 1. Explicit fixed-cardinality model

Let $U$ be an explicit item ground of size $N$, and let $0\le k\le N$.
A minimum-valuated matroid of rank $k$ is a function
$$
p:\binom Uk\longrightarrow\mathbb Q\cup\{+\infty\}
$$
with nonempty finite domain and the exchange property
$$
p(S)+p(A)\ \ge\
 p(S-e+f)+p(A-f+e)
\tag{VS1}
$$
for some $f\in A\setminus S$, whenever $S,A$ are finite-domain bases and
$e\in S\setminus A$. In particular both exchanged sets on the right are
finite-domain bases. A separate domain test is allowed to report that the
domain is empty.

Assume an exact oracle which, for an explicit $Y\subseteq U$, returns a
finite-domain basis $A$, together with its value $p(A)$, that first
maximizes $|A\cap Y|$ and then minimizes $p(A)$:
$$
A=\mathcal O_p(Y).
\tag{VS2}
$$
Deterministic tie breaking can be fixed. Oracle calls are charged separately
from polynomial explicit work. In the concrete application below, this
oracle is implemented in polynomial time by two integral polymatroid ranks.

Items are partitioned into $g$ nonempty replacement classes. Let
$\mathcal L(S)$ be any fixed collection of numerical predicates depending
only on the number of selected items in each class. The intended predicates
are the root cap and capped lower quotas. A same-class replacement preserves
$\mathcal L$ exactly.

There are explicit upper rows
$$
\sum_{e\in S}a_{je}\le u_j,\qquad
                    a_{je}\in\mathbb Z_{\ge0},
\tag{VS3}
$$
with finite nonnegative capacities. Every item retained for consideration
is individually eligible:
$$
a_{je}\le u_j\quad\text{for every upper row }j.
\tag{VS4}
$$
Items violating VS4 can be removed, since none belongs to a feasible set.
The valuation and context in the analysis continue to be those of the
original instance.

Set
$$
\delta=\max\{1,\max_e|\{j:a_{je}>0\}|\},\qquad
 A_0=\max\{1,\max_{j,e}a_{je}\}.
\tag{VS5}
$$
The quantities in VS5 are actual bounds from the explicit coefficient table;
their binary encodings do not require enumerating all values up to $A_0$.
The root and class predicates are not counted again in this upper frequency.

Write $\mathcal F$ for the finite-domain $k$-sets satisfying
$\mathcal L$ and VS3. The required output $R\subseteq U$ satisfies
$$
\begin{gathered}
 \forall S\in\mathcal F,\ \forall e\in S,\quad
 \exists f\in R\setminus(S-e):\\
 \tau(f)=\tau(e),\qquad S-e+f\in\mathcal F,\qquad
                         p(S-e+f)\le p(S),
 \end{gathered}
\tag{VS6}
$$
where $\tau$ is the class label. The context $S-e$ need not be contained
in $R$, or in any intermediate candidate ground.

**Theorem 1.** For $k\ge1$, a set satisfying VS6 can be constructed
deterministically with
$$
|R|\le
 gk\,\delta!\,[A_0 k(\delta(k-1)+1)]^\delta.
\tag{VS7}
$$
The construction makes $O(N^2+N)$ calls to VS2 and uses polynomial explicit
time and polynomial binary space. These polynomial bounds are uniform in
the explicit frequency and coefficient encodings. They are not
$N^\delta$ bounds. At $k=0$, the retained positive ground is empty.
An empty valuation domain is detected separately.

The output retains the original valuation oracle, restricted only when a
final solution is recovered. It is a ground reduction for this valuation
and these classes, not a simultaneous statement for all objective functions.

## 2. The overlap replacement lemma

For a finite-domain basis $S$ and $e\in S\cap Y$, the oracle output
$A=\mathcal O_p(Y)$ contains an $f\in A\cap Y$, outside $S-e$, such that
$$
p(S-e+f)\le p(S).
\tag{VS8}
$$

If $e\in A$, use $f=e$. Otherwise apply VS1. If its exchange element
$f$ were outside $Y$, the finite-domain basis $A-f+e$ would have more
elements in $Y$ than $A$, contradicting the first oracle criterion.
Thus $f\in Y$. The two bases $A$ and $A-f+e$ have the same overlap
with $Y$, so the second criterion gives
$$
p(A-f+e)\ge p(A).
$$
Substitution into VS1 proves VS8. A proper exchanged $f$ lies outside
$S$, hence outside $S-e$.

No numerical constraint is imposed on the oracle basis $A$. It need not
satisfy VS3 or $\mathcal L$. Feasibility will be established for the
single exchanged basis $S-e+f$.

## 3. External contexts and duplicate full columns

For a current candidate set $T\subseteq U$, a local reduction
$T\mapsto T'\subseteq T$ has the external-context property when the
statement in VS6 holds with $e\in S\cap T$ and $f\in T'$. All quantifiers
over $S$, all rows, and the valuation remain original.

These reductions compose. Fix $I=S-e$. At a stage the current
representative $e_i$ satisfies $I+e_i\in\mathcal F$. The next reduction
provides $e_{i+1}$ in the next ground with
$$
\tau(e_{i+1})=\tau(e_i),\qquad
 p(I+e_{i+1})\le p(I+e_i).
\tag{VS9}
$$
The context $I$ stays fixed. Thus the final output satisfies VS6 even
when $I$ contains elements discarded much earlier.

Within each replacement class, group items by their **entire labeled upper
column**
$$
\alpha_e:\{j:a_{je}>0\}\longrightarrow
                              \{1,\ldots,A_0\},\quad
                         \alpha_e(j)=a_{je}.
\tag{VS10}
$$
For every such full type $Y$, keep only
$$
\mathcal O_p(Y)\cap Y.
\tag{VS11}
$$
At most $k$ items survive in that type. For a protected element, VS8 gives
a replacement of the same full type and class. Every upper total and every
class predicate is unchanged. This simultaneous duplicate reduction
therefore has the external-context property.

If the overlap output has empty intersection with $Y$, no finite-domain
basis can contain an item of $Y$; otherwise that basis would achieve a
positive overlap. Deleting such a type is safe. Subsequent operations only
delete items, so at most $k$ copies of any full type remain forever.

## 4. A constructive labeled sunflower lemma

A labeled column is a partial function from row IDs to
$\{1,\ldots,A_0\}$. A labeled sunflower of size $L$ consists of $L$
distinct partial functions whose **row supports** form a sunflower, and
whose values agree on every row of the common core.

This is stronger than taking an ordinary sunflower of pairs
$(\text{row},\text{value})$. Different values of the same row would then
look disjoint, although their real supports overlap. That incorrect
construction is not used here.

**Labeled sunflower lemma.** For $L\ge2$, a family of distinct partial
functions of support size at most $\delta$, of cardinality greater than
$$
H_\delta(A_0,L)
                           :=\delta![A_0(L-1)]^\delta,
\tag{VS12}
$$
contains a labeled sunflower of size $L$. It can be found in uniform
polynomial time on the explicit family.

First pad every distinct full type to support size exactly $\delta$,
using private new row IDs for that type, with coefficient one. A private
row is not an actual quota. Distinctness of the partial functions is
preserved.

For the induction on the current support size $d$, greedily choose a
maximal subfamily with disjoint **row supports**. If it contains at least
$L$ members, those members have empty core and give the required flower.
Otherwise its union $Z_0$ has at most $d(L-1)$ row IDs and meets every
support. Among pairs
$$
(j,a),\quad j\in Z_0,\quad 1\le a\le A_0,
$$
some pair occurs in more than
$$
\frac{d![A_0(L-1)]^d}{d(L-1)A_0}
                   =(d-1)![A_0(L-1)]^{d-1}
\tag{VS13}
$$
members. Restrict to that fixed pair, delete its row, and recurse. The
remaining partial functions are still distinct: their removed row and
value were identical. Reinsert the row with that value into the core.
At support size one the same disjoint-support argument finishes directly;
equivalently, a family of distinct empty functions cannot exceed one.

The recursion follows one popular-pair branch and has depth at most
$\delta$. Popular pairs are counted by scanning pairs actually present;
there is no loop through all $A_0$ possible values. Maximal disjoint
families, restrictions, and pair counts are polynomial explicit operations.

Because $L\ge2$, a private padding row cannot be in the common core.
Removing all padding leaves a real sunflower with identical coefficients
on its core and disjoint real petals. Two distinct real full types cannot
both have empty petals with identical core values. Nothing in the later
argument requires a nonempty petal.

## 5. Valuated layers inside one flower

Set
$$
t=\delta(k-1)+1,\qquad L=kt+1.
\tag{VS14}
$$
Suppose one replacement class contains more than VS12 distinct full types.
Find a labeled sunflower in that class and choose one currently surviving
item per flower type. Let $V$ be the resulting $L$-item set. Other copies
of those types are left outside this particular choice.

Construct disjoint layers
$$
\begin{split}
 Y_1&=V,\\
 A_i&=\mathcal O_p(Y_i),\qquad F_i=A_i\cap Y_i,\\
 Y_{i+1}&=Y_i\setminus F_i\qquad(1\le i\le t).
 \end{split}
\tag{VS15}
$$
Every call uses the **original** valuation and item ground. Its emitted
layer has at most $k$ items. Consequently
$$
R_V:=\bigcup_{i=1}^t F_i,\qquad
                         |R_V|\le kt=L-1.
\tag{VS16}
$$
Delete exactly $V\setminus R_V$. Keep $R_V$ and all current candidates
outside $V$. At least one item is deleted.

## 6. Why one layer replacement satisfies every numeric row

Fix a deleted item $e$, an arbitrary original feasible basis $S$
containing it, and $I=S-e$. The item $e$ remained in every $Y_i$,
because it was emitted in none of the layers. VS8 gives
$$
f_i\in F_i\setminus I,\qquad
                  p(I+f_i)\le p(I+e)\qquad(1\le i\le t).
\tag{VS17}
$$
The $f_i$ are distinct since the layers are disjoint. They belong to
different selected flower types. Each is in the same replacement class as
$e$, so every class predicate remains true.

Let $C$ be the real flower core. If $j\in C$, labeled consistency gives
$$
a_{j,f_i}=a_{j,e}.
$$
Thus the upper load of that row is exactly its original load in $S$.

Outside $C$, consider rows meeting the fixed context $I$. Their number
is at most
$$
\left|\bigcup_{u\in I}\operatorname{supp}\alpha_u\right|
                         \le\delta(k-1)=t-1.
\tag{VS18}
$$
Every such row lies in at most one real petal of the chosen flower and
therefore can obstruct at most one of the distinct $f_i$. Some of these
rows may already be safe; counting all of them only overestimates the
number of bad candidates.

Finally, a row outside the core that does not meet $I$ has zero context
load. If a candidate enters it, VS4 gives
$a_{j,f_i}\le u_j$, so that row is safe.

The $t$ candidates and at most $t-1$ possibly obstructing touched rows
leave at least one feasible $f_i$. Its valuation is no larger by VS17.
This proves the external-context property of the deletion. A retained item
can represent itself.

This argument handles unequal coefficients in petals. It requires their
equality only on the core and individual eligibility on untouched rows.
It also counts context items that have disappeared from the current
candidate set. No packing feasibility is assumed for any whole $A_i$.

## 7. Termination, ground size, and uniform polynomial construction

Perform the duplicate reduction first. Then repeatedly choose a class with
more than $H_\delta(A_0,L)$ distinct full types and perform Sections 4–6.
Every iteration deletes at least one item; at most $N$ iterations occur.
A type can survive through an unchosen duplicate, but this does not affect
item-count termination.

At termination every class has at most $H_\delta(A_0,L)$ types, each with
at most $k$ items. VS7 follows from $L-1=k(\delta(k-1)+1)$. The
external-context invariant composes by Section 3 and proves VS6.

There are at most $N$ initial type queries. Whenever a flower iteration
is invoked, its threshold is smaller than the number of current types.
For $A_0,\delta\ge1$,
$$
H_\delta(A_0,L)\ge L-1,
$$
so $L\le N$ and $t\le N$ at that iteration. It makes at most $N$
overlap queries. At most $N$ iterations give $O(N^2+N)$ calls in total.
The count includes empty overlaps and unsuccessful numerical feasibility
of the eventual optimization problem.

Private padding uses at most $N\delta$ labels. A flower search follows
at most $\delta$ recursive restrictions and performs polynomial work at
each level. The threshold has
$$
O\bigl(\delta\log(\delta+1)+
       \delta\log(A_0+1)+\delta\log(k+1)\bigr)
$$
bits and can instead be saturated at $N+1$ during comparison. No candidate
tuple over row IDs or coefficient values is enumerated. All data structures,
oracle inputs, and threshold arithmetic fit polynomial binary space.

When there are no upper rows, one overlap query per class already suffices;
the normalized bound VS7 remains valid. For an empty finite domain, return
infeasibility before the construction. For a nonempty domain but no
numerically feasible basis, the replacement guarantee is vacuous and all
the same work bounds still hold.

## 8. Exact optimization and the meaning of the retained oracle

Starting with any $S\in\mathcal F$, replace an element outside $R$ using
VS6. The replacement lies in $R$ and outside the unchanged context, so it
strictly increases $|S\cap R|$. After at most $k$ steps the entire basis
lies in $R$, its class counts are unchanged, and its valuation has not
increased. Hence restriction to $R$ preserves the minimum objective.

If only the overlap oracle is supplied, a proposed $k$-set $S$ can be
tested and valued using $\mathcal O_p(S)$. Maximum overlap $k$ occurs
exactly when $S$ is a finite-domain basis, and then the returned basis
equals $S$. This gives an exact postprocessing oracle for enumeration.

The original oracle is not progressively replaced by an oracle whose
contexts are confined to the shrinking ground. It must continue to answer
VS2 for the original valuation. Final recovered solutions are restricted
to $R$; this is compatible with every deletion proof above.

Theorem 1 applies to one specified valuation. It preserves arbitrary signed
costs that generated that valuation, but does not state that one retained
set works for every later change of costs. The function $\mathcal L$ and
its class system are also fixed throughout.

## 9. Application: binary polymatroid counts, mixed rows, and root cap

Consider the model of *bounded_frequency_root_cap_valuated_fpt.md* (BF).
One normalized monotone integral rank $F$ describes either optional
integer counts in $P(F)$, or mandatory counts in $B(F)$ of original total
$R$. There is a nonnegative integer root charge
$$
\sum_e w_ex_e\le B_0
\tag{VS19}
$$
and arbitrary interval rows
$$
l_j\le\sum_e a_{je}x_e\le u_j.
$$
Finite targets and coefficients are nonnegative integers, upper bounds may
be absent, and an equality is one interval row. The essential assumption is
$$
w_e=0\ \Longrightarrow\ a_{je}=0
                                         \quad\text{for all }j.
\tag{VS20}
$$
The scalar $c\cdot x$ is arbitrary signed rational and is minimized exactly;
maximization is handled by negation. This permits a decision threshold on
that same scalar, but does not add an unrelated second scalar constraint.

Let $\Delta$ be the maximum of one and the nondistinguished column
frequency, and let
$$
B=\max\{B_0,\text{finite row targets}\}.
\tag{VS21}
$$
BF's preparation removes individually impossible coordinates, retains
original mandatory total $R$, and introduces a free zero-scalar disposal
coordinate for an optional instance. The disposal rank is $F^+(D)=F(D)$
if disposal is absent and $F^+(D)=R$ if it is present. Every optional
original vector extends to total $R$, and projection preserves the
original scalar and rows.

Write $P=\{e:w_e>0\}$, $Z=\{e:w_e=0\}$ after preparation, and
$n=|P|$. All numeric rows vanish on $Z$; their scalar coefficients do
not have to vanish or agree. An upper-zero row masks all its positive
coordinates. Every surviving upper coefficient is individually eligible
and at most $B$.

For a positive lower target, use
$$
\lambda_{je}=\min(a_{je},l_j).
\tag{VS22}
$$
For integer nonnegative counts, replacing coefficients by VS22 preserves
the predicate that the row reaches $l_j$. If a used coefficient is at
least $l_j$, its first occurrence already reaches the target; otherwise
capping changes no used coefficient. It is not a fractional equivalence
or preservation of the original row total.

At most $B_0$ positive units can be selected. A positive lower row must
meet such a unit, so more than $\Delta B_0$ positive lower rows proves
infeasibility. Otherwise classify a positive coordinate by its root weight
and full capped lower vector. With $G$ actual classes,
$$
G\le B_0(1+\Delta B_0B)^\Delta
                         \qquad(B_0\ge1).
\tag{VS23}
$$
Same-class replacement preserves the root and all capped lower totals.
Upper sides are left to Theorem 1. Equalities follow from their lower and
upper sides together. Only classes occurring in the input are built.

## 10. The complete-cost valuation and its compressed overlap oracle

Give a positive owner $e$ the valid cap
$$
b_e=\min\{F(\{e\}),\lfloor B_0/w_e\rfloor\}.
\tag{VS24}
$$
For the moment suppose its $b_e$ positive copies $U_e$ are explicit,
and let $U=\bigcup_eU_e$. Section 11 removes this supposition when binary
capacities would be too large.

Fix $0\le k\le\min\{B_0,R,|U|\}$. For a $k$-set $S\subseteq U$, define
$p_k(S)$ to be the least **full original scalar** of a resource base of
total $R$ with positive copies exactly $S$, and arbitrary compatible
integer zero counts. Set $p_k(S)=+\infty$ when no completion exists.

The VZ manuscript, *laminar_valuated_zero_completion_fpt.md*, proves that a
nonempty finite domain of $p_k$ is a minimum-valuated matroid. That fact
uses no laminarity of the numerical rows. Its weighted Rado representation
has private edges for allowed positive copies and $R-k$ zero-only dummy
vertices; the right natural matroid keeps rank $R$. Edge weights are minus
the true scalar. The resulting maximum valuation is $-p_k$. This is a
finite conceptual proof construction, not a unit expansion in the algorithm.

The exact algorithm works on $U\dot\cup Z$. Its first rank is
$$
G_F(D)=\min_{C\subseteq P}
       \left[F((D\cap Z)\cup C)+
                      \sum_{e\in P\setminus C}|D\cap U_e|\right].
\tag{VS25}
$$
This is the original resource lifted to positive copies and capped at one
per positive copy, while retaining binary zero coordinates. Rank queries
are submodular minimizations on original coordinates.

Intersect VS25 with **one** partition rank: positive total at most $k$,
zero total at most $R-k$. Require total $R$. This integral full-total
face forces both counts exactly. It detects an empty $p_k$ domain and
permits exact signed linear optimization.

After clearing scalar denominators, let $C_{\max}$ be the largest
absolute integer scalar coefficient and put $M_0=2RC_{\max}+1$. Minimizing
$$
\widetilde c\cdot z-M_0\sum_{u\in Y}z_u
\tag{VS26}
$$
first maximizes overlap with $Y$, then minimizes $p_k$. Indeed any two
full-total true costs differ by at most $2RC_{\max}$. The overlap reward
is on individual positive copies, not merely their owner totals.
Deterministic tie breaking has polynomial bit complexity.

No numeric row is added to this overlap problem, and no extra rank is
introduced for $Y$. Its basis may fail all the root or lower constraints;
same-class replacement and the labeled-flower argument are what preserve
them in the protected solution.

Consequently Theorem 1 applies with $g=G$, $\delta=\Delta$, and
$A_0\le B$. For every nonempty cardinality domain it returns $R_k$ with
$$
|R_k|\le
 Gk\,\Delta!\,[B k(\Delta(k-1)+1)]^\Delta.
\tag{VS27}
$$
The zero coordinates, their signed costs, and the original total remain
part of $p_k$ at every oracle call.

## 11. Uniform polynomial preprocessing without binary expansion

Here a **positive-capacity kernel** means a reduction of the allowed
positive coordinate capacities, with a parameter-bounded sum of those
capacities, while retaining original coordinate identities, numeric rows,
scalar coefficients, all zero coordinates, and the original resource
oracle. The bound does not include the number of zero coordinates or their
binary resource mass.

**Theorem 2.** The BF instance admits a deterministic, uniform
polynomial-time positive-capacity kernel preserving feasibility and the
exact scalar optimum at every positive cardinality. For $B_0\ge1$, its
total positive capacity is at most
$$
\begin{split}
 K_+ := \max\bigg\{ B_0^2,\quad&
 G\,\frac{B_0(B_0+1)}2\,\Delta!\,
       [B B_0(\Delta(B_0-1)+1)]^\Delta\bigg\}\\
 &\le(\Delta B_0B+2)^{O(\Delta)}.
 \end{split}
\tag{VS28}
$$
For fixed frequency this is a polynomial in the numerical parameters.
Construction uses polynomial binary workspace. It does not require
enumerating $B_0$ values when $B_0$ is binary-large.

The following two branches prove this stronger original-input statement.

**Large root cap: $B_0\ge n\ge1$.** Keep every positive coordinate with
the valid binary cap VS24. Their total capacity obeys
$$
\sum_{e\in P}b_e\le nB_0\le B_0^2.
\tag{VS29}
$$
Nothing is expanded. These caps are already implied by the root and
singleton resource bounds on every feasible integer solution, so this
branch preserves the entire feasible set. It performs only polynomial
binary arithmetic and oracle work. The theorem in this branch is a bound
on a compressed capacity sum, not an explicit listing of that many items.

**Small root cap: $1\le B_0<n$.** Expand the at most
$nB_0<n^2$ allowed positive copies. The zero ground remains compressed.
For each $k\le\min\{B_0,R,|U|\}$, detect whether $p_k$ has a finite
domain; skip empty domains and construct $R_k$ for the others. Every one
of these kernels uses the same original $U$, original completion oracle,
and original rows. One cardinality's reduction is not substituted into the
next cardinality's oracle.

Keep $R_+=\bigcup_kR_k$. By monotonicity of
$k(\Delta(k-1)+1)$ and summing the leading $k$ in VS27,
$$
|R_+|\le
 G\,\frac{B_0(B_0+1)}2\,\Delta!\,
       [B B_0(\Delta(B_0-1)+1)]^\Delta.
\tag{VS30}
$$
There are fewer than $n$ cardinalities, each on fewer than $n^2$
positive items. Theorem 1 and the compressed oracle of Section 10 therefore
give a uniform polynomial original-input construction. No factor
$n^\Delta$, no coefficient-value enumeration, and no binary-$B_0$
cardinality loop is hidden in this statement.

Copies of a fixed original owner have identical resource behavior, rows,
and true scalar. They can be merged back into that owner's binary capacity
$$
\widehat b_e=|R_+\cap U_e|.
$$
An original count vector fitting these caps can be realized using retained
copies, since the shared resource depends on owner counts and is symmetric
within every copy class. Conversely any retained-copy vector projects to
the same original resource and rows. Thus merging is exact.

At each fixed positive cardinality, Theorem 1 retains a feasible basis
with no greater $p_k$ than any original feasible one. Restriction cannot
create a solution outside the original instance. Hence the optimum is
preserved exactly. Arbitrary true zero costs are already included in
$p_k$, so no subsequent independent insertion of zeros is being assumed.

For example, with $X=\Delta B_0B+2$, the class bound and elementary
$\Delta!\le\Delta^\Delta$ show that VS28 is at most $X^{7\Delta}$.
This rough explicit exponent is only a size bound; no claim of optimal
polynomial degree is made.

When $B_0=0$ or $n=0$, all positive counts vanish. Positive lower
requirements fail, and otherwise the signed scalar is optimized on the
zero resource with the original required total. This is polynomial. Zero
original resource rank is covered by the same gate.

## 12. Exact FPT consequence, bits, and workspace

The capacity kernel supplies the same all-input FPT order as BF:
$$
2^{O(\Delta B_0\log(\Delta B_0B+2))}
                                      \operatorname{poly}(H).
\tag{VS31}
$$
The additional conclusion is the uniform polynomial-time positive-capacity
preprocessing with original-context replacement, not a smaller FPT
exponential order than the already proved hash and direct-profile methods.

For the small-cap branch, enumerate at most $B_0$ distinct retained
positive copies, test the original numeric rows, and compute the attaining
completion $p_k$. A final fixed $S$ query masks $U\setminus S$, uses
positive total $k$, and keeps zero total $R-k$; unit caps force exactly
the requested positive set. Enumeration of a ground bounded by VS28 gives
VS31. Since the ground actually stored is a subset of fewer than $n^2$
input copies, this branch uses polynomial space.

For the large-cap branch, do not materialize the capacity bound. Stream
positive vectors $0\le x_e\le b_e$. There are at most
$(B_0+1)^n\le(B_0+1)^{B_0}$, within VS31. For each numerically feasible,
resource-independent positive vector, use the residual zero rank
$$
h_x(D)=\min_{C\subseteq P}
                              [F(D\cup C)-x(C)]\qquad(D\subseteq Z).
\tag{VS32}
$$
It is normalized, monotone and submodular. Compatible zero counts are
exactly $P(h_x)$, by the original inequalities for $D\cup C$. Its total
rank is at most $R-x(P)$; full completion exists exactly when equality
holds. Then signed minimum-weight base optimization on $h_x$ returns the
best completion. This is the same explicit compressed primitive proved in
BF. It keeps only $n$ binary counters and polynomial oracle workspace.

In either branch the required total $R$ is retained after all masks and
boxes. Rank loss is not repaired by silently lowering that total.
Denominator clearing and the reward VS26 have polynomial bit length.
The conceptual natural matroid, Rado dummies, and binary-large zero counts
are never expanded.

The preprocessing retains all zero coordinates. Consequently it does not
bound the whole explicit ground, the full original rank, the lengths of
arbitrary scalar coefficients, or the size of an oracle program by the
parameters alone. The exact optimum, rather than all possible zero
completions, is what the valued positive reduction preserves.

## 13. Relation to the simpler packing kernel and primary antecedents

The companion manuscript *deterministic_sparse_packing_oracle_kernel.md*
(SK) covers an ordinary oracle matroid with additive profits and zero-one
upper packing. Its greedy layers and original-context composition motivate
the present construction. Here two extra ingredients are necessary:
coefficients must agree on the sunflower core, and full completion cost is
represented by a valuation rather than an additive item cost.

The underlying tools have established antecedents:

- Erdős and Rado, *Intersection Theorems for Systems of Sets* (1960),
  provides the sunflower framework. Section 4 proves the precise
  coefficient-labeled induction required here, including its constructive
  and binary-input accounting.
  <https://www.renyi.hu/~p_erdos/1960-04.pdf>

- Fomin, Golovach, Korhonen and Saurabh, *Stability in Graphs with Matroid
  Constraints*, SWAT 2024, Theorem 4, uses disjoint independent layers and
  a bounded-conflict replacement argument. The present flower supplies
  a local touched-row bound, and VS8 replaces the ordinary rank exchange.
  <https://drops.dagstuhl.de/storage/00lipics/lipics-vol294-swat2024/LIPIcs.SWAT.2024.22/LIPIcs.SWAT.2024.22.pdf>

- Huang, Kakimura, Kobayashi and Terao,
  *Polynomial Kernels with Reachability for Weighted d-Matroid
  Intersection*, arXiv:2603.17345v1, Lemma 2 and Section 7, explicitly
  develop the external-context greedy exchange and deterministic
  single-exchangeability interfaces. Its randomized reachable kernels
  have smaller degrees in several ordinary matroid/partition
  specializations. This note does not claim to improve those degrees.
  <https://arxiv.org/html/2603.17345v1>

- Husić, Loho, Smith and Végh, *On complete classes of valuated matroids*,
  TheoretiCS 3 (2024), Definition 1.1 and Theorem 2.9, supplies the
  weighted Rado induction behind $p_k$. VZ gives the precise sign
  convention and the compressed two-rank implementation used here.
  <https://theoretics.episciences.org/14792/pdf>

These comparisons delimit the proof contribution: deterministic
coefficient-consistent ground reduction, followed by a compressed
positive-capacity application with full signed completion costs. They
do not establish a first-ever kernel or a new sunflower construction
framework.

## 14. Scope limits

The finite upper coefficients are nonnegative and bounded numerically by
$A_0$. The bound necessarily records that diversity. Treating only
unlabeled supports as types would fail for unequal upper coefficients.

The extra numerical predicates must be invariant within each replacement
class. In the BF application, the number of classes is controlled by the
root cap, lower capping, and frequency. Arbitrary extra constraints that
do not meet this condition are not automatically preserved.

The assumption VS20 makes the zero coordinates quota-free. Without it,
the optimal-completion valuation does not by itself encode their numerical
feasibility, and BF already records an oracle obstruction to the proposed
root parameterization. No removal of VS20 is claimed.

There is one global integral resource and one exact scalar objective.
A second unrelated resource, several independent scalar budgets, signed
quota coefficients, or a classical parameter-only bit kernel requires
additional arguments. The present integral recoveries use one resource
rank and one partition rank, or the residual rank VS32.
