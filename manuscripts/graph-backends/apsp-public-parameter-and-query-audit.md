# Public APSP parameters, queries, and admissible comparisons

**Primary-source audit, 25 October 2026.** This supplements
[apsp frontier proof](../../problems/apsp-frontier/proof.md). The comparison is for undirected,
fully dynamic, deterministic numerical distance oracles, with
polynomial logarithmic query time. Amortized and worst-case update
bounds remain different interfaces. The current checkpoint supplies
amortized bounds only.

**Checkpoint E update.** Section 2 remains a valid, deliberately
restricted reconstruction using the unchanged packaged local theorem.
It is superseded as the strongest comparison in this research by the
joint source reconstruction in [public-apsp-joint-retuning-audit.md](public-apsp-joint-retuning-audit.md):
amortized overhead `exp O(U^(6/7) h^(1/7))`, stretch
`exp O(U^(5/7) h^(2/7))`, and polynomial logarithmic numerical queries.
The new comparison retains the public ambient-length congestion loss,
charges small-instance fallback work, and separates construction work
from selected recourse. See its independent audit and
[same-stretch-apsp-comparison-and-root-audit.md](same-stretch-apsp-comparison-and-root-audit.md); do not continue to
advertise `59/63` as the best public consequence checked here.

Write `U=log(N+4)` and `h=log(U+4)`, where `N` is a graph-size and
finite-history bound. For the usual polynomial-length histories and
polynomial-size graphs, the logarithms of the input vertex bound,
edge bound, and master bound differ by constant factors. Comparisons
with arbitrarily long histories can instead use the block restart in
Section 5.

## 1. Audited theorem interfaces

| Primary source and version | Update guarantee | Numerical query | Parameter restriction / qualification |
|---|---|---|---|
| KMG, *A Dynamic Shortest Paths Toolbox*, arXiv:2311.06402v1, Theorems 1.2 and 4.1 | Worst-case factor `exp O(U^(20/21) h)`; stretch `exp O(U^(6/7) h)` | `O(log m log L)` in Theorem 1.2 | The local Theorem 3.1 permits `K=o((log m)^(1/6)/log log m)`; its isolated Claim 4.6 heading is inconsistent with its theorem and proof and is not used. |
| KMZ, *Bootstrapping Dynamic APSP via Sparsification*, arXiv:2408.11375v1; ESA 2025 | Deterministic amortized `N^(o(1))`; printed logarithmic update envelope `O(U/h^(1/4))` | `O(D)`, where the printed depth is `D=O(h^(1/4))` | Local spanner parameter `1<=K<=O((log n)^(1/3))`. The paper suggests a worst-case extension but does not prove that extension in its headline theorem. |
| Haeupler--Long--Saranurak, arXiv:2402.18541v2, Theorem 12.1 | Worst-case `O(n^epsilon)`; stretch `2^(poly(1/epsilon))` | `O(log log n / epsilon^4)` | `epsilon>=log^(-c)n` for an unspecified sufficiently small absolute `c>0`; Section 3.3 explicitly uses this to absorb parameter-dependent factors. |
| Chuzhoy--Zhang, arXiv:2304.09321v1, Corollary 1.5 | Amortized `n^(O(epsilon)) log L` | `2^(O(1/epsilon)) log n log log L` | `log^(-1/200)n < epsilon < 1/400`; the approximation depends doubly exponentially on an inverse power of `epsilon`. |

All four constructions are deterministic, so their guarantees are not
restricted to an oblivious adversary. The numerical query bounds are
part of the comparison: the factor `2^(O(1/epsilon))` in CZ cannot
be erased when `epsilon` depends on the graph size.

Primary links:

* [KMG full paper](https://arxiv.org/pdf/2311.06402).
* [KMZ full paper](https://arxiv.org/html/2408.11375v1) and
  [ESA 2025 publication](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ESA.2025.113).
* [HLS full paper](https://arxiv.org/pdf/2402.18541).
* [CZ full paper](https://arxiv.org/pdf/2304.09321).

The current arXiv histories were checked: KMG, KMZ, and CZ list only
v1; HLS lists v2, dated 10 April 2024. No later arXiv version was found
for these four titles on the audit date.

## 2. KMG plus public degree reduction: the 59/63 baseline

This is a derived public composition, not a printed theorem. It uses
the KMG local Theorem 3.1 and the already public binary-tree degree
reduction. It does not use this checkpoint's new static provider or
normalized local repair.

For every nonbase owner restore maximum degree three at its child.
With the global upper bounds

$$
g_0=C U^{2/3}h,\qquad
 q=C(U/K+g_0+h),\qquad P=e^q,
$$

Theorem 3.1 provides at most `P` child edits per owner edit,
`O(PM/k)` initial child inventory for owner size `M`, local work
`exp O(x+q+K^2 g_0)`, and local terminal stretch `exp O(K g_0)`.
Here `k=exp(x)`. A phase of `Theta(M/k)` owner edits keeps the child
inventory `O(PM/k)`; rebuilding costs are spread over this phase.
Every boundary's public degree adapter adds only polynomial
logarithmic edits and a constant metric factor.

As `x>>q`, the nominal logarithmic size decreases by
`x-O(q)` per level. Thus the full hierarchy has
`d=O(U/x)` levels. Its total initialization/update ledger gives

$$
B_{\rm public}=O(x+K^2g_0+dq),\qquad
 a_{\rm public}=O(dKg_0+dh).
$$

Take

$$
x=C_xU^{59/63},\qquad
 K=\lfloor U^{8/63}\rfloor,\qquad
 d=O(U^{4/63}).
$$

Then `q=O(U^(55/63))`, while `g_0` and its logarithmic factors
are smaller. The individual close terms are

$$
dq=O(U^{59/63}),\quad
 K^2g_0=O(U^{58/63}h)=o(U^{59/63}),\quad
 dKg_0=O(U^{54/63}h)=O(U^{6/7}h).
$$

The hidden metric constants only change the absolute constant in the
last `O` bound. A constant factor at every degree reduction adds
`O(d)` to log-stretch and does not change its displayed scale. This
means the same asymptotic stretch scale as the KMG headline, not an
assertion that the numerical hidden stretch constant is identical.

### 2.1 Local admissibility is not inferred from the global size

Terminate at `log M<=x`. At every nonbase owner,

$$
\frac{K\log\log M}{(\log M)^{1/6}}
 \le O\left(
 U^{8/63-59/378}h\right)
 =O(U^{-11/378}h)=o(1).
$$

Therefore the actual-size local range in KMG Theorem 3.1 holds all
the way to the base. Its exact base costs `exp O(x)` per edit and
can be included in the same budget.

### 2.2 Length and query composition

Use fixed query handles and the positive binary-tree adapter from
Section 5 of [apsp frontier proof](../../problems/apsp-frontier/proof.md). Each adapter rescales
real edges by a power of two `H=polylog N` and gives connectors
length one. For distinct handles it preserves the old metric within
a factor two after division by `H`. Equal handles return zero, and
disconnected pairs stay disconnected. Isolated vertices can be kept
outside the active nontrivial hierarchy and activated when incident
edges are inserted.

KMG's child lengths increase by at most the local vertex count, so
after `d` levels the magnitude has logarithm `O(Ud)`. The arithmetic
and length bucketing therefore have polynomial logarithmic overhead;
the relevant length range is never silently treated as a constant.
An external numerical query follows a single pivot pair through the
levels and performs the indicated positive scalings and additions.
It takes polynomial logarithmic time. These checks do not establish
a worst-case version of the derived hierarchy or a stronger final
simple-path reporting interface.

## 3. A legal improvement of the printed KMZ parameter choice

The printed KMZ update envelope is not its best immediate retuning.
The following stronger public consequence still has a logarithmic
update exponent larger than every `U^b` for fixed `b<1`.

Theorem 4.7 and its Section 4.4 recursion give, for global shrink
`k=e^x`, depth allowance `D`, and repair parameter `K`,

$$
\log\gamma_{RC}=O(U/K+h),
$$

$$
B_{\rm KMZ}=O\left(x+D^2(U/K+h)+K^2a+h\right),
 \tag{K1}
$$

where `a` is a common upper bound on the logarithm of all recursive
distance approximation factors. Its approximation recurrence is

$$
a\le C h(CK)^{D}.
 \tag{K2}
$$

The quadratic depth charge in (K1) retains the original growing-degree
analysis; no checkpoint degree-reset improvement is needed. Constant
branch multiplicities and restarting the subproblems add only the
already covered logarithmic terms.

Choose a sufficiently small fixed `eta>0` and a sufficiently large
fixed `C_x`, and put

$$
D=\left\lfloor\eta h/\log(h+4)\right\rfloor,
 \qquad K=D^3,\qquad x=C_x U/D.
$$

The source shrink condition
`D log gamma_RC=o(x)` holds. With these choices, the actual depth is
at most `D` for all sufficiently large `N`. Also,

$$
\log\bigl(h(CK)^D\bigr)
 =3\eta h+o(h).
$$

For any fixed desired `0<a_0<1`, choose `eta<a_0/4`. Then the
approximation log bound can be made at most `U^(a_0)` for all
sufficiently large `N`. Moreover,

$$
D^2 U/K=U/D,
 \qquad K^2U^{a_0}=o(U/D),
 \qquad D^2h=o(U/D).
$$

Consequently this original public recursion certifies

$$
\boxed{\quad B_{\rm KMZ}=O(U\log(h+4)/h),\qquad
                 \log\gamma\le U^{a_0},\quad}
$$

with `O(D)` numerical query steps and amortized updates. Its local
restriction `K=O((log n_local)^(1/3))` holds above the exact base:
`K=poly(h)` and `log n_local>=x=Theta(U log h/h)`.

This retuning should be included in a fair public comparison. It is
still asymptotically slower in its update envelope than the
checkpoint's fixed-power `11/14` and `3/4` choices, while offering a
different and potentially finer approximation. No assertion is made
that this exhausts modifications to the KMZ construction.

The same recurrence explains why simply taking polynomial-in-`U`
depth does not certify the checkpoint points. Its bound raises `CK`
to that depth in (K2). Replacing this compounded approximation charge
would be a new analysis or construction, not the substitution of a
smaller `k` into the published headline.

## 4. Why the HLS and CZ headlines require care

HLS Theorem 12.1 has an excellent query guarantee: even a legally
chosen inverse-polylogarithmic `epsilon` leaves its numerical query
polynomial logarithmic. The issue is numerical admissibility of the
parameter and its hidden work factors. Section 3.3 uses the small
constant in `epsilon>=log^(-c)n` to absorb
`(log n)^(poly(1/epsilon))` into powers of `n^epsilon`.

There are concrete unabsorbed terms, not merely a missing convention:
Theorem 5.1 has router update factor
`(1/epsilon)^(O(1/epsilon^4)) 2^(O(i))`; its preceding paragraph
allows `t_local=O(1/epsilon^5)`. Table 2 propagates these factors
through the dynamic vertex sparsifier and expander hierarchy. Thus a
choice such as `epsilon=U^(-3/14)` cannot be justified by writing
only `n^epsilon` and discarding those terms. The audit has not
optimized all local HLS parameters, so it does not rule out a better
derived public point from that independent framework.

For CZ, the printed lower bound `epsilon>log^(-1/200)n` already
does not permit that substitution. In addition, the displayed
query formula is only certified polynomial logarithmic when
`1/epsilon=O(log log n)`. At smaller `epsilon` its declared
query guarantee must be retained explicitly. The abstract and
Corollary 1.5 differ in the inverse power occurring in their
approximation expression; neither version is silently strengthened
in this comparison.

## 5. Long update histories and adaptivity

Suppose a fixed `N` bounds the current graph inventory and lengths
have polynomial magnitude in `N`, while the update history can be
arbitrarily long. Divide the external update sequence into blocks of
`N` operations. At a block boundary initialize a fresh structure on
the current graph and use master size `Theta(N)` for the next block.
Its initial graph plus update inventory is `O(N)`.

The first block costs initial work plus its updates. Each later
initialization costs at most `N exp O(B(log N))` and is charged to
the preceding completed block of `N` operations. Hence the whole
history has total cost

$$
(\text{initial inventory}+Q)\exp O(B(\log N)),
$$

up to changing absolute constants. Restarting is a deterministic
reversible maintenance operation; it does not restrict how the
adversary chooses the next update or query. It preserves an amortized
bound and does not make it worst-case. This avoids comparing a
history-dependent master logarithm with HLS's current-size parameter
when a fixed capacity bound is available.

## 6. Freshness checks beyond the older headlines

The January 2026 full version of Chuzhoy--Parter,
[*Fully Dynamic Algorithms for Graph Spanners via Low-Diameter Router
Decompositions*](https://arxiv.org/html/2601.20718v1), explicitly allows
`512<=k<=log^(1/49)n` and `1/k<=delta<=1/400`, with worst-case
`n^(O(delta))` updates. Its stated parameter range does not directly
supply the update points here.

The September 2026 Algorithmica article
[*New Tradeoffs for Decremental Approximate All-Pairs Shortest
Paths*](https://link.springer.com/article/10.1007/s00453-026-01407-2)
has randomized, oblivious-adversary decremental guarantees. Forster,
Goranci, Nazari, and Skarlatos's
[*Bootstrapping Dynamic Distance Oracles*](https://arxiv.org/abs/2303.06102)
is likewise randomized and oblivious, despite the similar title.
These do not provide deterministic fully dynamic substitutes.

The October 2026 manuscript
[*Dynamic Distances Without Matrix Inverse*](https://arxiv.org/abs/2610.28573)
concerns a different, polynomial-update algebraic distance regime.
The current [FOCS 2026 accepted-paper
list](https://focs.computer.org/2026/accepted-papers/) and primary
author publication pages were also checked for a newer fully dynamic
deterministic distance-oracle headline. The search did not identify
one that directly settles the tradeoff under discussion. This is a
search finding, not a completeness theorem about the literature.

## 7. Wording justified by this audit

The checkpoint gives explicit new points for its proved separated
hierarchy. They improve the update envelope at the stated stretch
scale over the quantified KMG headline and the stronger public
`59/63` composite audited above. The legally retuned KMZ point is
included as another public comparison. A claim to the globally best
possible deterministic APSP tradeoff across all public constructions
would require a more complete numerical analysis of the independent
HLS framework and any further combinations, and is not made here.
