# A conditional sequential full router from a shuffler hierarchy

**Separate mathematical construction, 24 October 2026.** This note
reconstructs the query algorithm directly. It does not invoke the
mutually recursive Task 2, expander sorting, and Task 3 algorithms of
[Chang--Huang--Su, arXiv:2405.03908](https://arxiv.org/pdf/2405.03908).
No global best-leaf density parameter is used.

The hierarchy and precomputed embeddings are explicit hypotheses.
The induced-terminal issue in
[chs-hierarchy-and-load-boundaries.md](chs-hierarchy-and-load-boundaries.md)
is not resolved by the query proof. A virtual-root construction may
supply these hypotheses, but must be proved separately. Neither the
existing 6/7 nor the existing 5/6 matching composition needs this note.

## 1. Conditional interface and result

Let $`G`$ be the physical host, with $`n`$ vertices and fixed bounded
maximum degree, as supplied by the incidence-port split. Paths are explicit
physical edge-ID lists, with endpoint annotations even when empty.
Parallel IDs remain distinct. Assume a hierarchy of good vertex sets
of depth at most $`d`$. At a good internal node $`X`$, its vertices
have the disjoint partition
```math
X=Y_1\mathbin{\dot\cup}\cdots\mathbin{\dot\cup}Y_t,\qquad
 Y_i=X_i\mathbin{\dot\cup}B_i.                              \tag{1}
```
Here $`X_i`$ is a good child, and a precomputed injective matching
$`\mu_i:B_i\to X_i`$ has explicit physical paths. Thus
$`|B_i|\leq|X_i|`$. For fixed positive constants and a common $`k`$,
```math
c_-|X|/k\leq |Y_i|\leq n'_X\leq c_+|X|/k,\qquad t\leq k. \tag{2}
```
The CHS normalization $`n'_X=6|X|/k`$ is permitted.

At each $`X`$, there are $`\lambda_X\leq\lambda`$ precomputed
matching families $`M_X^1,\ldots,M_X^{\lambda_X}`$.
A matching joins vertices of different parts. If $`p_{ij}^a`$
counts matching edges between $`Y_i,Y_j`$, put
```math
m_{ij}^a=p_{ij}^a/n'_X,\quad
 Q_a[i,j]=m_{ij}^a/2\ (i\ne j),\quad
 Q_a[i,i]=1-\tfrac12\sum_{j\ne i}m_{ij}^a.                 \tag{3}
```
These matrices are symmetric and stochastic. Require
```math
\left|(Q_{\lambda_X}\cdots Q_1)[i,j]-1/t\right|
                                      \leq 1/(100t).     \tag{4}
```
The stronger CHS potential stopping condition implies (4) eventually;
(4) can also be checked directly by rational arithmetic.

Impose the elementary size guards
```math
\min_i|Y_i|\geq8\lambda t^2,\qquad n'_X\geq\lambda t^2.
                                                               \tag{5}
```
The new sequential construction can enforce these guards without
the source's restriction on its distributed parameter. Given an
integer $`p\geq1`$, use the actual host size to set
```math
v=\lceil\log_2(n+2)\rceil,\qquad
 k=2^{\max\{5,\lceil v/p\rceil\}},\qquad
 \lambda_{\rm cap}=C_0(v+1)^2 .
 \tag{5a}
```
The polynomial energy cut player has
$`\lambda=O(\log(k+2)\log(n+2))`$, with an explicit absolute
constant in its potential-decrease proof. Choose a fixed
sufficiently large $`C_0`$, and stop recursion at a fixed
sufficiently large multiple of $`k^5\lambda_{\rm cap}^2`$
vertices. Each remaining internal terminal set has
$`\Omega(k^5\lambda_{\rm cap}^2)`$ vertices; its smallest
part has $`\Omega(k^4\lambda_{\rm cap}^2)`$ vertices.
This implies (5) for $`t\leq k`$ and
$`\lambda\leq\lambda_{\rm cap}`$, without requiring
$`k\geq c\lambda`$.

The depth is $`O(\log n/\log k)\leq O(p)`$.
All leaves have size $`\mathrm{poly}(k,\lambda_{\rm cap})`$,
including a whole small host declared a leaf. Hence one fixed
polynomial leaf algorithm costs only
$`\exp O(v/p+\log(v+2))`$ per actual host record.
The full hierarchy's preprocessing retains the intended
$`n\exp O(v/p+p\log(v+2))`$ envelope, apart from its explicitly
separated inverse-expansion factor. No old CHS epsilon clipping
or larger master-sized padded graph is used in this adapter.

Each leaf has a full-router circuit: for arbitrary source/destination
tokens of endpoint load at most $`L`$, it returns physical paths of
length at most $`A_{\rm leaf}`$, congestion at most $`LA_{\rm leaf}`$,
and work
```math
|X|L A_{\rm leaf}\mathrm{poly}(\log(nL+2)).
                                                               \tag{6}
```
Preprocessing is independent of $`L`$, with one fixed polynomial
exponent in leaf size, inverse sparsity, and bit size. Section 7
gives a concrete circuit interface.

Assume the union of all precomputed shuffler paths, folding-matching
paths, and elementary leaf-circuit paths has physical edge
congestion at most $`A`$, and each path has length at most $`A`$.
A polynomial factor in levels or circuit layers can be included
in $`A`$. A per-level congestion bound gives the same statement
after multiplying $`A`$ by $`d+1`$.

This is an explicit flattened-family condition. Child virtual
edges need not be genuine edges induced by child terminals.
A virtual-graph hierarchy with consistent embeddings is allowed.

**Conditional result.** There is a deterministic sequential full
router on the hierarchy root. For endpoint load $`L\geq1`$,
```math
\begin{aligned}
 \text{maximum path length}&\leq A(c(\lambda+1))^{d+1},\\
 \text{edge congestion}&\leq LA(c(\lambda+1)^2)^{d+1},\\
 \text{query work}&\leq nLA(c(\lambda+1)^2)^{d+1}
                          \mathrm{poly}(\log(nL+2)).
 \end{aligned}                                                \tag{7}
```
The constant is independent of $`d,k,L`$.
For $`d=O(p)`$, $`\lambda=\mathrm{poly}(\log n)`$, and
```math
A=\phi^{-O(1)}(\log n)^{O(p)},              \tag{8}
```
the non-load factors in (7) are
$`\phi^{-O(1)}(\log n)^{O(p)}`$. No polynomial factor in
$`k=n^{1/p}`$ enters query quality. The original root's inverse
conductance is paid once through $`A`$, rather than once per level.

The work is intentionally $`nL`$-sensitive: the algorithm creates
$`2L`$ dummies at each vertex. It does not claim work proportional
only to a sparse real token list. Section 8 checks the intended
static witness applications.

## 2. Full routing on a part

Assume the full router on good child $`X_i`$ is constructed. Define
```math
h_i(v)=v\ (v\in X_i),\qquad h_i(v)=\mu_i(v)\ (v\in B_i).
                                                               \tag{9}
```
Every fiber has size at most two. For token $`u\to v`$ in $`Y_i`$,
fold $`u`$ to $`h_i(u)`$, route $`h_i(u)\to h_i(v)`$ in the child,
and unfold to $`v`$. Part endpoint load $`P`$ becomes child
endpoint load at most $`2P`$. Each folding-matching edge is used
by at most $`2P`$ source/final pieces. Output destinations are
exactly the requested ones, with destination load at most $`P`$.

Call this the **part router**. It routes on all of $`Y_i`$, without
best-leaf ranks. Physical paths may leave the part through its
valid embedding; only endpoints and counted physical paths matter.

## 3. Deterministic scatter with central portal assignments

Tokens on $`X`$ initially have per-vertex load at most $`L_0`$,
and colors in $`[t]`$. Let $`N_{i\ell}^a`$ be the color-$`\ell`$
count in part $`i`$ after step $`a`$. At that step send
```math
q_{ij\ell}^a=
 \left\lfloor p_{ij}^a N_{i\ell}^{a-1}/(2n'_X)\right\rfloor       \tag{10}
```
tokens of that color from part $`i`$ to part $`j`$.
At most half a color's tokens in a part move, since the fractional
matching row sum is at most one. Choose disjoint token intervals
in fixed token-ID order.

For each directed pair $`i,j`$, concatenate chosen tokens over
colors and assign them cyclically to its $`p_{ij}^a`$ portals.
Invoke the part router on these tokens to their assigned portals.
Each then follows the stored matching path to its paired portal.
Unselected tokens stay at their existing vertices.

### Integer-error and load bounds

For each color, $`N_\ell^a-Q_aN_\ell^{a-1}`$ has infinity norm
at most $`t`$. Stochasticity bounds accumulated error by
$`\lambda t`$. For total color count $`N_\ell`$, (4) gives
```math
.99N_\ell/t-\lambda t
   \leq N_{i\ell}^{\lambda_X}
   \leq1.01N_\ell/t+\lambda t.                                \tag{11}
```
Let $`N_i^a=\sum_\ell N_{i\ell}^a`$ and
$`N_{\max}^0=\max_iN_i^0`$. Summing the color errors gives
```math
N_i^a\leq N_{\max}^0+a t^2,\qquad
 N_{\max}^0\leq L_0n'_X.                                     \tag{12}
```
The total quota on portal group $`i,j`$ is at most
$`p_{ij}^a N_i^{a-1}/(2n'_X)`$. Cyclic assignment therefore puts
at most
```math
\left\lceil N_i^{a-1}/(2n'_X)\right\rceil
        \leq L_0/2+2\leq3L_0                                \tag{13}
```
tokens at any sending portal, using (5) and $`L_0\geq1`$.
The arrival bound is the same. A matching uses each endpoint
at most once per step.

Vertex load increases by at most $`3L_0`$ per step. Thus all
part-router source loads are at most $`4L_0(\lambda+1)`$, and
their destination loads are at most $`3L_0`$. Calling each
part router with parameter $`O(L_0(\lambda+1))`$ is sufficient.
Temporary physical path intersections do not change these
endpoint counts; the result is an explicit path family, not
an assertion of one-step simultaneous communication.

### Linear token bookkeeping rather than a cubic table

For each $`i,a`$, preprocess portal groups in decreasing
$`p_{ij}^a`$ order. Metadata per step is $`O(t^2)`$.
For each nonempty $`(i,\ell)`$, scan this list only until
$`p_{ij}^a N_{i\ell}^{a-1}<2n'_X`$. Later quotas are zero.
Every enumerated positive quota consumes at least one
selected token, and all selected intervals are disjoint.
There is at most one failed stopping test per nonempty
$`(i,\ell)`$. Consequently counts, quota intervals, and
cyclic assignments cost
```math
O((M+t^2)\mathrm{poly}(\log(nL_0+2)))
                                                               \tag{14}
```
per step, with $`M`$ the current token count. There is no
$`t`$-fold scan per token. Ordinary sorting and bucket lists
suffice. Under $`n'_X=6|X|/k`$, each quota is the exact integer
$`\lfloor k p_{ij}^a N_{i\ell}/(12|X|)\rfloor`$.

## 4. Scatter, meet, and reverse dummy traces

Suppose real source load is at most $`L`$, and at most
$`L|Y_j|`$ tokens have mark $`j`$. Scatter the real tokens.
Create exactly $`2L`$ dummy tokens at every vertex of $`Y_j`$,
all with color $`j`$, and scatter those separately. Record
each dummy's full path from its origin.

In each part $`i`$, real color-$`j`$ count is at most
$`1.01L|Y_j|/t+\lambda t`$, whereas dummy color-$`j`$ count is
at least $`1.98L|Y_j|/t-\lambda t`$.
Their difference is at least
```math
.97L|Y_j|/t-2\lambda t>0                  \tag{15}
```
by (5). Centrally assign each real token to a distinct dummy
of its current part and color, using fixed-ID lists.

Within each part, route every real token to its assigned
dummy's final location. Source and destination load are
$`O(L(\lambda+1))`$, since selected dummy destinations form
a subset of the actual dummy configuration. Each real token
then follows the reverse of its assigned dummy trace.
It ends in its desired part. No vertex receives more than
$`2L`$ real tokens: it was the origin of exactly $`2L`$ dummies.

Every dummy is used at most once. Thus reversed trace length
and congestion are bounded by the already computed dummy
trace inventory. No routing subroutine is invoked to reverse
the paths. This proves the part-mark task with final load $`2L`$.

## 5. Full routing by induction

For exact source/destination tokens of endpoint load at most
$`L`$, mark each token by its destination part. That mark count
is at most $`L|Y_j|`$, so Section 4 applies. Afterwards all
tokens lie in their destination part, source load is at most
$`2L`$, and exact destination load remains at most $`L`$.
One final part-router call at parameter $`2L`$ finishes.

The two scatters use at most $`2\lambda`$ families of part-router
calls. Meeting and final routing add two families. Each family
uses only strictly smaller good children, at folded load
$`O(L(\lambda+1))`$. There is no same-level recursive call,
or query preprocessing that depends on the query it answers.

The induction never uses a global best-leaf set, a best-leaf
density ratio, recursive expander sorting, or a renewed
$`L\rho_{\rm best}`$ destination allowance. Central portal
assignment is followed by genuine counted physical paths.

## 6. Work, path length, and congestion

Let $`\mathcal V_j`$ be the sum of $`|X|L_X`$ over all good-node
router invocations at depth $`j`$ in one root query. Child good
sets are disjoint subsets of their parent's vertices. Thus
```math
\mathcal V_0=nL,\qquad
 \mathcal V_{j+1}\leq c(\lambda+1)^2\mathcal V_j.               \tag{16}
```
One factor pays the number of families, the other their load
increase. All dummy records and local bookkeeping are paid
by $`\mathcal V_j\mathrm{poly}(\log(nL+2))`$.
The $`t^2`$ metadata is paid because $`t^2\leq|X|`$.

For a fixed hierarchy node at depth $`j`$, the sum of load
parameters of all its invocations is at most
```math
L(c(\lambda+1)^2)^j.                 \tag{17}
```
Each stored shuffler or folding edge is used a constant times
that load times a fixed polynomial in $`\lambda+1`$. Applying
the globally flattened-family congestion bound yields total
computed-trace congestion
```math
LA(c'(\lambda+1)^2)^{d+1}.           \tag{18}
```
Returned real paths are bounded by this inventory with a fixed
additional factor per recursion level. Within one invocation,
distinct dummy assignments use each returned dummy trace at most
once. That trace can itself contain reversals created by a child
invocation. Inductively, count the child's computed and returned
inventory with multiplicity: consuming a returned trace or its
reverse increases this accounting by at most a fixed factor at
the parent. This factor is included in the constant of
$`c(\lambda+1)^2`$, rather than asserting that an original
primitive occurrence is globally used only once. Immutable
concatenation records avoid repeatedly copying growing prefixes;
materialization is charged to explicit route occurrences.
Extra factors polynomial in depth or circuit layers fit (7).

A single token follows only $`O(\lambda+1)`$ child paths per
parent invocation: its real scatter, a dummy reverse scatter,
meeting, and final routing. Its dilation satisfies
```math
D_j\leq c(\lambda+1)(D_{j+1}+A).             \tag{19}
```
This proves path length in (7), without an $`L`$ factor.
Combining trace materialization, (16), and (14) proves work.

Concatenation initially gives walks. Before exporting a token
route, erase closed subwalks with a vertex stack and a position
table, in time linear in its explicit list length. The resulting
simple path has the same endpoints, uses only retained physical
edge IDs, and has no larger length or edge-occurrence load.
Parallel IDs are kept distinct. This final token-route
normalization is separate from normalizing an input ambient
embedding table in a later static sparsifier call.

It would be incorrect to multiply an already flattened factor
$`A`$ once per level. Here only the number of uses of fixed
precomputed path families multiplies. The hierarchy construction
must independently prove their union's physical quality.

## 7. A leaf circuit independent of token load

[sequential-leaf-routing-and-chs-work.md](sequential-leaf-routing-and-chs-work.md)
constructs short, low-congestion paths for a fixed bounded-load
matching in polynomial work. It uses a symmetric lazy walk with
uniform stationary measure, exact matrix powers, and moment
conditional expectations. A next step is an oriented genuine
edge ID or a holding symbol.

For a literal load-$`L`$ circuit, let $`h_0`$ and $`L_0`$ be the
next powers of two above leaf size $`h`$ and $`L`$. There are
$`h_0`$ blocks of $`L_0`$ scalar positions; at most two blocks
are assigned to one physical vertex. Give each real token a
distinct destination slot and fill the remaining slots by
dummy keys.

Use the scalar bitonic network on $`h_0L_0`$ positions.
Comparator distances below $`L_0`$ stay within one block.
Larger distances pair blocks at equal within-block offsets.
Their block-pair pattern is independent of $`L_0`$, and the
number of cross-block layers is
```math
\sum_{a=1}^{\log_2h_0}a=O(\log^2h_0).            \tag{20}
```
Preprocess the bounded-load matching paths of those layers
once. In a query compute comparisons centrally and move only
tokens requiring a block exchange; at most $`L_0`$ tokens use
each direction. Local work is
$`O(h_0L_0\log^2(h_0L_0))`$. Each real token uses only
$`O(\log^2h_0)`$ stored paths, independent of $`L_0`$, and
congestion scales by $`O(L)`$. This proves (6).

A fixed polynomial leaf-size bound, for example $`O(k^5)`$,
gives one fixed preprocessing exponent independent of $`p`$.
Query quality depends polynomially on leaf inverse sparsity
and logarithmic size, not polynomially on $`k`$.
If the original root is itself a leaf, its inverse expansion
is paid in this single construction only once.

## 8. Aggregate work in the static witness applications

The $`nL`$ term is sufficient for both static witness tasks.

For witness-to-host routing in a degree band $`J_i`$, endpoint
load is $`\mathrm{poly}(\phi^{-1})\deg_{J_i}(v)`$.
The incidence-port split has $`O(|E(J_i)|)`$ vertices with
per-port load $`\mathrm{poly}(\phi^{-1})`$.
Its query volume is therefore
```math
|E(J_i)|\mathrm{poly}(\phi^{-1}).      \tag{21}
```
For host-to-witness routing with witness edge weight $`\rho_i`$,
per-port load is $`L_i=\max(1,\lceil\rho_i\rceil)`$, and
```math
|E(W_i)|L_i
       \leq O(|E(J_i)|+|E(W_i)|).                             \tag{22}
```
The established band sums pay these inventories.

Preprocess each actual host once. Only the query factor,
not the more expensive construction factor, multiplies
load volume. No new preprocessing call is made per unit
of load. Subsequent route normalization is charged to the
full output lists.

## 9. Remaining scope

This note supplies a sequential query induction and actual
token trajectories. A faster static primitive still requires
a uniform polynomial-work hierarchy with the stated virtual
graphs, the flattened-family bound $`A`$, root coverage,
and the actual-size/finite-word preprocessing analysis.
Preprocessing arithmetic is charged at its actual precision.
Spectral elimination, matrix moments, and cut-player conditional
expectations can use a fixed polynomial in $`k`$ and the input
bit size, and are part of the construction-work factor. They are
not required to fit the numerical client's smaller stored-label
word bound. The exported paths still consist of original IDs and
have the length/congestion bounds above; temporary arithmetic
size contributes no extra $`k`$ to those geometric bounds.

The constructive leaf router and energy cut player remove
the two unbounded local computations identified in CHS, but
do not alone prove those hierarchy statements.
