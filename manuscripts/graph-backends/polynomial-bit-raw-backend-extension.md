# Polynomial-bit root labels in the deterministic raw-cycle backend

**Transfer lemma, 25 October 2026.** This note extends the numerical input
range of the existing deterministic raw-cycle construction. Its structural
parameters, lifetime rules, and raw (before cancellation) quality guarantee
are unchanged. The purpose is to permit the quasipolynomial metric aspect
that appears in a minimum-cost-flow interior-point method.

This is a proof extension of the current research construction, not an
independently published algorithm. It uses the positive-length, native-ID,
and original-edge tree interfaces in the following existing notes:

* [4/5 composition](quantitative-matching-4-5-composition.md),
  Sections 1--7;
* [uniform source interfaces](uniform-source-interfaces-for-4-5.md);
* [polynomial-bit stable forests](polynomial-bit-stretch-stable-forest-integration.md);
* [degree reset](distance-degree-reset-candidate.md),
  including its exact integral label recurrence;
* [finite-bit low-stretch adapter](an-weighted-finite-bit-adapter.md).

## 1. Statement

Fix constants `a >= 1` and `c_b >= 1`. Let `U >= 2` be the structural
master logarithm. The root graph and the entire guarded structural history
have size at most `2^(c_size U)` for a fixed size exponent. Admit positive
integer root lengths and signed integer root gradients with bit width

$$
b_0\le c_b(U+1)^a.                 \tag{1}
$$

The fully dynamic raw-cycle construction has a computable favorable
constant tuple for which initialization per actual record, amortized
updates and queries, complete exposed forest logs, current occurrence
multiplicity, returned piece count, and inverse raw approximation quality
are all at most

$$
E_a(U)=\exp O_a\!\left(U^{4/5}(\log(U+2))^{1/5}\right).     \tag{2}
$$

Its numerical root sums have `poly_a(U)` bits. In particular, the
extension does not replace the structural logarithm `U` by `b_0` in (2).
All arithmetic is charged using ordinary finite words.

The statement requires one fixed exponent `a` for the client family.
It does not claim the same constant for arbitrary bit widths chosen
after seeing the instance.

## 2. The stored-label induction

Retain the structural choices

$$
h=\lceil\log_2(U+4)\rceil,\quad
 t=\max\{2,\lfloor(U/h)^{1/5}\rfloor\},\quad
 p=r=t,\quad K=t^2,\quad x=\lceil U/t\rceil,\quad k=2^x,
$$

and `d_* = ceil(8U/x)+10`. Under the existing record-size guard, an
original-edge spanning tree gives the exact core-length formula

$$
\ell_{\mathrm{core}}(e)
       =2\sum_{j\le O(\log^2 n)} (\ell_e+P_j),
 \qquad P_j\le 2nL,
$$

where `L` is the largest parent length admitted during this instance.
The port expansion multiplies real lengths and gradients by a dyadic
integer whose logarithm is `O(log U)`. Frozen potential corrections are
sums of at most `n` admitted parent gradients. Consequently, with a fixed
constant `c_*` determined only by the structural size convention,

$$
b_{\ell,i+1}\le b_{\ell,i}+c_*U,
 \qquad b_{g,i+1}\le b_{g,i}+c_*U.                           \tag{3}
$$

Declare before initialization

$$
b_*=b_0+c_*U(d_*+1)+c_*U.                \tag{4}
$$

Equation (3) proves the label guard conditional only on the record-size
guard. It does not use the low-stretch approximation factor or running
time. Thus the polynomial dependence of the AN adapter on its input bit
count cannot recursively amplify that count. Temporary portal coordinates
are discarded and never become exported core labels.

Since `d_* = O(t)`, (4) is a fixed polynomial in `U`. This is the only
change needed in the bit induction.

## 3. Every use of the bit bound

The bit bound appears in the local construction in five places.

1. **Exact distance and ordering arithmetic.** Truncated Dijkstra
   comparisons, symbolic path ties, parent potentials, and explicit path
   aggregates use fixed-polynomial work in `b_*+U`. Their combinatorial
   record and relaxation counts are unchanged.
2. **Stable-forest preprocessing.** The AN adapter and its weighted
   replica wrapper have fixed-polynomial stretch and work in
   `B=b_*+O(U)`. Integer replica counts and dyadic reciprocal proxies use
   the same bit range. Increasing `b_*` therefore changes these factors
   only to another fixed polynomial in `U`.
3. **Number of stable forests.** The path inventory halves total
   surviving length. If it has `T_occ` occurrences, the number of calls
   is at most `1+ceil(log_2(T_occ L+1)) = O(b_*+log(T_occ+2))`.
   This is polynomial in `U`; it is neither proportional to `L` nor a
   power of `b_*` applied anew at each level.
4. **Length buckets.** The positive-length reduction needs `O(b_*)`
   buckets, counted explicitly. Each bucket invokes the same unweighted
   native graph routines. The sequential expander router and static
   ambient sparsifier do not depend on the numeric length magnitude
   inside one bucket.
5. **Base cases and exported counters.** A base graph has at most
   `O(k)` actual records. Its direct ratio computation has
   `k^O(1) poly(b_*+U)` work. Root numerator and raw denominator sums have
   at most `b_0+O(U+log E_a)` bits because the number of physical
   traversals is at most `M E_a^2`.

No step performs one iteration per integer length unit. No common
denominator over unrelated rational input coordinates is formed.
Root integer labels may be obtained from a common fixed-point grid;
constructing that grid belongs to the numerical client.

The old check `b_* <= (log m_local)^2` was a sufficient way of exhibiting
a quasipolynomial aspect ratio, not a combinatorial condition used by the
replacement static-base repair construction. At a nonbase instance,
`log m_local >= x-O(1)`. Choose once and for all an integer

$$
q_a>\tfrac54\max\{a,6/5\}.                    \tag{5}
$$

The replacement check

$$
b_*\le(\log m_{\rm local})^{q_a}   \tag{6}
$$

then holds eventually. For the flow case `a=2`, the concrete choice
`q_a=3` suffices. This change is justified by the five explicit cost
dependencies above, rather than by applying an old fixed-aspect theorem
outside its advertised range. Tiny instances use the exact base routine.

## 4. Recurrences and quality

Write `poly_a(U)` for fixed polynomial factors whose degree may depend
on the fixed input-width exponent `a`. The same local envelopes hold:

$$
\begin{split}
 \log\Gamma&=O((p+r)h),\\
 \log F&=O(U/p+U/r+r^2h+(p+r)h),\\
 \log P&=O_a(U/K+\log\Gamma+\log U),\\
 W&=k^{O(1)}\rho_{\rm sched}^{O(1)}F^{O(1)}
                              \Gamma^{O(K)}\mathrm{poly}_a(U).
\end{split}                                                 \tag{7}
$$

The larger bit count does not add an extra factor `k` to a propagated
child log. Complete lifetime retirement, actual central-edge provenance,
degree feedback, and the initial child credit remain as before. Thus

$$
\begin{split}
 G_d&\le P(G_{d-1}+1),\\
 J_d&\le W+P(G_{d-1}+1)+(P/k)(J_{d-1}+T_{d-1}),\\
 T_d&\le O(kW+kP(G_{d-1}+1))+O(P)(J_{d-1}+T_{d-1})
\end{split}                                                 \tag{8}
$$

close using `J_d+T_d/k`. The added low-stretch and bucket factors
contribute at most `O_a(d log U)` to the quality exponent. Even if a
presentation absorbs them into `Gamma` before all repair layers, the
extra term is only `O_a(dK log U)`.

For the parameters above,

$$
dK\log U=O(t^3h),\qquad
 dK(p+r)h=O(t^4h)\le O(U/t)=O(x).                            \tag{9}
$$

All remaining exponent terms are the previous `O(x)` terms. Equation
(2) follows. One first proves (3)--(4) under the size guard, then uses
the now-fixed polynomial bit overhead in (7)--(8) to prove that a
favorable fixed tuple satisfies that size guard. This preserves the
acyclic first-failure proof.

## 5. Consequence for flow interfaces

The deterministic flow framework of van den Brand et al.,
[arXiv:2309.16629v1, Section 2 and Theorem 4.6](https://arxiv.org/html/2309.16629v1),
uses fixed-point numbers of polynomial logarithmic bit width and
quasipolynomially bounded lengths. That numerical range is covered by
(1) for a sufficiently large fixed `a`.

For the usual polynomially bounded min-cost-flow instances, the standard
power-barrier estimate gives an explicit `O(log^2 m)` magnitude bound
before the stopping threshold. Nevertheless, (1) is stated for a fixed
general polynomial width so that the client need not conceal a precision
loss in this magnitude shorthand.

This lemma alone does not solve min-cost flow. A numerical adapter must
still maintain the exact circulation and cost, apply a safe dyadic step,
report stale coordinates with a charged raw-motion bound, and supply the
correct IPM progress and stopping proof. Those obligations are separate
from the structural extension proved here.
