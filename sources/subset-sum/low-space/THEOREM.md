# A general deterministic low-space construction

Author: Yilin Liu. Assistance: OpenAI Codex, including GPT-6 Astra.

This module records the construction now integrated into the
[complete manuscript](../../../problems/subset-sum-low-space-deterministic/proof.md). Its proof modules retain a
separate development record; the paper itself includes every required
foundation and replacement lemma.

## Theorem

For arbitrary binary-encoded integers $w_1,\ldots,w_n,t$, there is a
uniform deterministic algorithm that returns an indexed binary witness
for $\sum_iw_ix_i=t$, or correctly returns NO, using

$$
T=\operatorname{poly}(n,L)2^{n/2},\qquad
S=\operatorname{poly}(n,L)2^{E_Sn},\qquad
E_S=\frac{18261635770550353}{10^{17}}=.18261635770550353.
$$

Here $L$ is the full binary encoding length, time counts bit operations,
and space counts all simultaneously retained writable bits. Zero,
negative, and repeated weights are included. The two costs describe
one algorithm; the separate faster-time result in Part I is unchanged.

## 1. Foundation and replacement modules

The following manuscript lemmas are the complete foundation used here.

| Foundation | Location in the manuscript |
|---|---|
| Exact distinct-support streams, canonical projections, strict deletion | II.1 |
| Nonlinear potential with powers 52 and 75 | II.1 |
| Fixed-layer trace theorem and three gain rectangles | II.2.1–II.2.2 |
| Constructive balanced-cell families and useful-layer contrast | II.2.5–II.2.6 |
| Sequential common prime paths and weighted interval covers | II.4 |
| Whole-complement atomic arrays, actual product allocation, raw leaves | II.5.4–II.5.7 |
| Exact band joins and independent original-key parent streams | II.6.5–II.6.8 |
| Per-signing cached covers, original ambient bounds, all residue lifts | II.7 |
| Stored-eighth, implicit-quarter high-deficiency fallback | II.9.1 |

The ordinary half-selected projection proof in II.5.1–II.5.2 is used
with its actual analytic hypotheses, as restated in Section 4 below.
Its old scalar range is not a separate assumption on the new high tail.

The changed interfaces are proved in:

- [LINEAR_COVERS.md](LINEAR_COVERS.md): a linear-subspace XOR cover,
  its exact conditional construction, and geometric replay cost;
- [OWNERSHIP.md](OWNERSHIP.md): weighted canonical-distance covers,
  equal variation rates on unequal owner regions, tensorized assignment
  containers, and exact all-profile allocation;
- [BIASED_TOP.md](BIASED_TOP.md): useful integer-layer projection
  with separate physical and code losses, and all-layer separators;
- [RESOURCES.md](RESOURCES.md): the complete mixed-density certificate,
  finite arithmetic, preparation, lifting, and state ledger.

No special-input range theorem or conditional low-noise estimate is
needed for the general theorem.

## 2. Full supports and the exhaustive case split

Enumerate at most two leftover coordinates, leaving $3m$ coordinates.
Partition them into three $m$-blocks. Compute their exact support sizes
$N_j$ in $O^*(2^m)$ time and $O^*(2^{m/2})$ state. Put

$$
d_j=m-\log_2N_j,\qquad
q_\circ=\frac{137}{250},\quad
q=\frac{54784907311651059}{10^{17}},\quad B=\frac34-q,\quad
X=\frac{17}{2000},\quad T=\frac{27}{200}.
$$

Use dictionary capacity $C=\lceil2^{qm}\rceil$. The core-size policies
retain the design anchor $q_\circ$; lowering the actual dictionary
capacity does not change those cores. Here $B<.203$. If some full-block
deficiency is at least $Bm-O(1)$, place that block inside one half
of the whole instance. Its distinct support has cardinality
$U\le2^{3m/2-d_j+O(1)}$. The exact interval fallback costs

$$
O^*(2^{3m/2}+2^{3m/4}U/C)
=O^*(2^{3m/2}),
\qquad S=O^*(2^{3m/8}+C),
$$

because $q+B=3/4$. Test the high threshold using the integer upper
proxy $\widehat d_j=m-\lfloor\log_2N_j\rfloor$: trigger when
$\widehat d_j\ge Bm$. This implies $d_j\ge Bm-1$.
The comparison uses the bit length of $N_j$ and exact rational
arithmetic. Its one-bit tolerance contributes only a constant factor.

Otherwise choose a largest-support block as top. Its normalized
deficiency proxy is $x_0$, and each local proxy $x$ satisfies
$x_0\le x\le B$, within $O(1/m)$. Safe proxies follow from exact
support bit lengths. Exact $N_j$ continue to determine every ambient
histogram and inherited image scale. Use the following exhaustive menu.

| Top density | Top representation | Strict top-base fraction |
|---|---|---:|
| $0\le x_0\le X$ | Equal-rate variable ownership, $p=1/20$ | $9/10$ |
| $X\le x_0\le T$ | Support-dependent biased shell, $s=21/50$ | $\min(121/200+3x_0,17/20)$ |
| $T\le x_0\le B$ | Ordinary half-selected top | $18/25$ |

Either certified mode can be used at a shared boundary. On either
local side, $x<T$ uses a strict local core and selected fraction
$\theta=9/20$; $x\ge T$ uses an oriented half. The two sides make
these decisions separately, including mixed strict/half profiles.

## 3. Strict cores and useful signed images

Choose all strict bases before useful layers. For a full-block density
$x\le1/5$ and retained fraction $z$, the potential gives deficiency
$m\beta(x,z)$, where

$$
\beta(x,z)=xt,\qquad
\frac{23}{26}z=xt+\left(\frac{23}{26}-x\right)t^{52/75}.
$$

Clearing powers permits rational bisection by exact integer comparisons.
Nonlinear extraction is used only for the top range $x_0\le T$ and
strict local range $x<T$. Proportional density monotonicity suffices
elsewhere, including densities up to $B>.2$.

For each strict local core, maximize the dyadic support-class mass at
$\theta=.45$. The trace gains are $.079$ through density $.03$,
$.075$ through $.05$, and $1/16$ through $.2$. Thus, with
$\phi=\theta-\mathrm{gain}$, class threshold $\ell$ and actual code
size $K$ satisfy

$$
\ell-\log K\ge(\theta-\tau)c-\phi d-O(\log m),
\qquad \tau=1-h(\theta).
$$

The linear-code construction costs
$O^*(2^{(1+\theta)c+\phi d})$ and is performed once per unsigned
core and scalar configuration. Every later signing-dependent cover,
histogram, cache, and generator start retains its actual $K$ factor.

Store the entire complement of each local core as one distinct-support
array with witnesses. It remains indivisible in child and leaf packing.
The strict local policies give $c>.53m$. Restrict strict local smaller layers to $r/4\le k\le r/2$, as proved
in [SIMPLIFICATIONS.md](SIMPLIFICATIONS.md). Their mask-entropy
contrast is below $(7/16)c+o(c)$; the proved top allocation supplies
the required movable factors. No actual local image is altered by moving
top ancestor factors between children.

For $x\ge T$, choose the represented half with larger support. If
its deficiency is $d_A$ and that of its complement is $d_R$, then
$d_A\le d_R$ and $d_A+d_R\le d_j$. The two corrections
$(d_A-d_R)/2$ and $d_A/2-d_R$ are nonpositive. This handles all
local densities through $B$ without a trace theorem beyond its range.

## 4. The three top representations

For the dense ownership mode, the useful distance band is
$|j/a-1/2|\le3/50+O(1/a)$, where $a=.9m+O(1)$.
At $t=j/a-1/2$, choose

$$
z=\frac{t}{1-2p},\quad b=a(1/2+z),\quad
u=p(a-b),\quad v=pb,
$$

with bounded integer rounding preserving $b+u-v=j$ exactly.
The quota count has logarithm $a h(p)+O(\log a)$.
Weighted trace selection produces owner/threshold groups obeying

$$
K_\ell Q/2^\ell
\le\operatorname{poly}(m)\binom aj/N_{\rm top}.
$$

Every witness succeeds in at least one group. The net top loss is
$d_{\rm core}-a[1-h(1/2+t)]+O(\log a)$.
Equalized container degrees consume less than $3/8$ of this distance
credit. The actual fine-profile cap preserves both incidence and leaf
bounds, including sparse profiles. The parent key carries the complete
original coefficient vector; compatibility means binary coordinatewise
sums. Local signings are restored before original-key deduplication.

For the middle mode, [BIASED_TOP.md](BIASED_TOP.md) proves a useful
shell code with separate deficit $\delta$ and outer code cost $\kappa$:

$$
\delta+\kappa\le[1-h(.42)]\rho m+
\phi_0m\beta(x_0,\rho)+O(\log m).
$$

Projection scales $\delta$ only. Its all-layer separator has common
degree exponent $s-h(s/2)+h(s)/2$ and tuple exponent at most $s$.
The central incidence excess, including the full outer code, is below
$-1/1250$ throughout the active middle range. The exact original
full-local support pays that cost for the entire signing union.

For the high tail, take top-base fraction $\rho=18/25$ and use the
ordinary half-selected representation. The old central-domination
proof requires

$$
p=1-h(1/4)-\xi/2>0,\qquad p\rho<1/5,\qquad
1-\rho\ge(7/10)p\rho^2.
$$

These hold for every $0\le\xi\le.203$: the first follows from
$h(1/4)<.812$ and $\xi/2\le.1015$; the others follow from
$p<.19$, $\rho=.72$. The derivative and projection proof therefore
extends over this exact range. Half-core compression on both local
sides gives the high-tail resource row in the certificate.

## 5. Filters, covers, and independent streams

Use constant prime depth sixteen. The complete pattern universe includes
every already constructed top owner or code label, and both local
signing/Good-set/physical-layer/layout universes. Good-set membership
is tested outside the local signing loop; $K|\mathrm{Good}|\le\operatorname{poly}(m)2^c$
pays the joint image scans. Its conditional potential yields a
common-good nested prime path for each eligible triple.

In ownership mode make the global quota image dense before top fine
profiles are selected by residue-witness pigeonholing. Fix the physical integer local
layers, layouts, images, and child roles before prime selection, hence
before this top refinement. This preserves their entropy guarantees
for arbitrary input bit length. In the biased ordinary
mode first enumerate the projected integer layers, then choose common
primes for those actual images. Both orders preserve the appropriate
eligibility theorem. Owner-dependent solves pay the owner count;
top-dependent solves pay the outer top-code count. The expensive local
prime universes themselves are scanned once in the shared construction.

The weighted top residue cover controls the two integer raw counts and
two original ambient sums. Each signing's local cover controls its
scan, diagonal restart, and raw-pair costs, shared over every parent
lift. Cache only the selected residue lists, reusing a single histogram
workspace. Normalize a fixed polynomial number of integer means,
rather than adding exponentially many unrelated rational denominators.

At a lift, one dictionary on each side unions every restored local
signing and cached seed. A raw occurrence retains its labels for cost
accounting; a valid output key is deduplicated across them. Its original
full-block ambient histogram bounds the entire union once. The exact
independent-stream lemma gives side cost

$$
O^*\!\left[
\left(C+\sum_D(F_D+G_D)\right)(1+U/C)+\sum_DJ_D
\right].
$$

The two sides add. Complementary equal-weight groups meet through one
fixed checker table, with one incidence charge per distinct key.
Interval and top-label prefix restrictions are imposed before raw
generation; a raw occurrence belongs to one cell at each polynomial
depth. Paused streams retain completed bounded dictionaries and scalar
frames, not unfinished raw generators. These facts give the same
finite witness and NO-decision guarantees as the manuscript's stream proof.

## 6. Complete costs and correctness

[RESOURCES.md](RESOURCES.md) proves all three mixed domains, both
local gain switches, the local upper cap, the top plateau, every half
handoff, and the high tail. Its raw, restart, and leaf margins pay
fixed-grid and integer-rounding losses. The ownership incidence uses
exact quota products, with polynomial losses only. Biased incidence
has its separate positive linear margin.

The actual capacity is the tight certified restart envelope plus a
declared finite-loss reserve. In particular, the middle tiny cap
retains its sharper physical top gain and exact root enclosure;
replacing it by a uniform weaker coefficient would increase the final
space bound. All core-size policies retain their original anchor.
The full-block fallback threshold changes with the actual capacity
through $q+B=3/4$.

Every construction is paid, including weighted owner selection,
linear codes, prime candidates, cover scores, histograms, actual lifts,
empty stream starts, assignment indices, and conditional-expectation
integer arithmetic. The largest pure-lift bound is below $1.49355m$;
the largest stored-leaf and dictionary exponent is at most $qm$.
Multiple live objects add their sizes. No complete filtered child or
parent stream is materialized.

Fix $Q_{\rm grid}=10^{12}$. Its common linear loss is at most
$100m/Q_{\rm grid}$; choose a fixed coordinate cutoff so logarithmic
and bounded rounding losses total at most another $100m/Q_{\rm grid}$.
The total normalized allowance is $2\cdot10^{-10}$, below the
$10^{-9}$ reserve above the critical restart envelope. The certified
strict margins exceed this reserve. Polynomial factors in arbitrary
$L$ remain polynomial; the finite small-coordinate cases only change
fixed constants. The high fallback uses its exact $O(1)$ threshold
tolerance rather than a positive linear loss.

A genuine solution has a useful top representation and two useful
local images. One common prime path makes them eligible; the weighted
covers preserve their actual offset and lift. The restored streams
emit the parent keys, and the compatibility table finds a pair at the
original target. Conversely a returned pair has exact integer target
weight and binary original coefficients. Restoring each local signing
once and the entire ordinary top signing once gives a genuine indexed
witness. All configuration families are finite. Exhaustion therefore
returns NO exactly when no witness exists.

Since $n=3m+O(1)$ and $E_S=q/3$, the theorem follows. In particular
it implies the received checkpoint bound with space exponent $137/750$.
