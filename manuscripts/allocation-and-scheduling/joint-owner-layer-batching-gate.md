# Jointly independent layer owners: what it proves and what batching still needs

**25 October 2026. Working proof and obstruction to a proposed progress
lemma. Independent review requested.** This note is separate from the
accepted current-blocker theorem. It proves that a joint-owner variant
retains the same current-blocker growth. It does not obtain a polynomial
running time. The examples below refute specific proposed batch
implications, not the possibility of a different polynomial algorithm.

The base construction is
[matroid-allocation-current-blocker-quasipolynomial.md](matroid-allocation-current-blocker-quasipolynomial.md). Its notation
is retained: the current matching has independent owner set $I$,
$k=|I|<r$, and layer $i$ has selected bundles $X_i$
and unique current blockers $Y_i$. Let

$$
J_i=I\setminus\mathrm{owners}(Y_{<i}),\qquad
 A_i=\mathrm{owners}(X_i).
 \tag{J1}
$$

## 1. A valid stronger per-layer invariant

Require that selected owners in one layer are distinct and that

$$
J_i\mathbin{\dot\cup} A_i
               \text{ is independent.}
 \tag{J2}
$$

Owner names may still repeat between different layers. When extending
the last layer, accept a new owner only outside
$\mathrm{cl}(J_i\cup A_i)$. Physical available-resource
tests, minimal bundles, blockers, and immediate one-at-a-time free
cascades are unchanged. An already stored free center is processed
using its individual eligibility, which follows from (J2); it need
not be tested for independence against its own occurrence in $A_i$.

### 1.1 Earliest-circuit exchange preserves joint independence

Suppose a free center in layer $i$ has owner $p\notin I$,
and its earliest exchangeable blocker lies in layer $j<i$.
The existing proof gives, for every retained layer $h\le j$,

$$
\mathrm{cl}(J'_h)=\mathrm{cl}(J_h),
              \qquad |J'_h|=|J_h|.
 \tag{J3}
$$

Independence of $J_h\cup A_h$ means that adjoining $A_h$
increases rank by exactly $|A_h|$. Rank increments depend only
on the flat $\mathrm{cl}(J_h)$. Hence (J3) implies the
same rank increment for $J'_h\cup A_h$, proving (J2) after
the exchange. In particular no retained candidate owner has secretly
become an element of $J'_h$.

If $p\in I$, its existing allocation is in the earlier blocker
prefix. Replacing that allocation does not change $I$, and all
retained $J_h$ are literally unchanged. The conclusion follows
again. Each free-center cascade discards its own layer before doing
another such exchange, so the argument also applies throughout a
cascade.

### 1.2 Earlier maximality still survives

For $h<j$, the selected owner set $A_h$ and physical forbidden
set are unchanged. Equation (J3) also preserves
$\mathrm{cl}(J_h\cup A_h)$. Therefore the earlier
statement that no jointly addable owner has an available bundle is
literally the same statement after the exchange. Layer $j$ is
refreshed before a growth test, as in the accepted construction.

No new player-side exchange rule is needed for these one-at-a-time
operations. In particular the repeated-owner difficulty of a more
general batch swap is not hidden inside this lemma.

## 2. Joint maximality still gives the original growth scale

Fix a completed, fully blocked layer $i$, and write

$$
s=|Y_{<i}|,\qquad y=|Y_i|,\qquad a=|A_i|,
 \qquad w=r-k+s.
 \tag{J4}
$$

We have $a=|X_i|\le y$, and $w\ge s+1$. For any
fractional base vector $x$, the mass outside the flat
$\mathrm{cl}(J_i\cup A_i)$ is at least

$$
r-(k-s+a)=w-a.
 \tag{J5}
$$

Whenever $w-a>0$, maximality and the same fractional cover
argument as in the accepted theorem therefore imply

$$
v\bigl(R(X_{\le i}\cup Y_{\le i})\bigr)
                   >(T-B)(w-a).
 \tag{J6}
$$

For ordinary liking sets this follows from their available total
value. For the player-local downward-closed extension, use the exact
available-weight oracle and its perspective-polytope inequality.

Let

$$
B=(T-u)/3-\varepsilon T>0,
 \qquad A=2B+u.
 \tag{J7}
$$

The physical star charge remains

$$
v\bigl(R(X_{\le i}\cup Y_{\le i})\bigr)
                    \le A(s+y).
 \tag{J8}
$$

Suppose, for contradiction, that $y\le\varepsilon w$. Since
$0<\varepsilon<(1-u/T)/3<1$, (J5) is positive and (J6)
applies. Using $a\le y$, $s\le w-1$, and
$T-B=A+3\varepsilon T$, its lower bound exceeds the upper
bound in (J8) by at least

$$
\begin{split}
 &(A+3\varepsilon T)(1-\varepsilon)w
                      -A((1+\varepsilon)w-1)\\
 &\qquad=
       \varepsilon\bigl(3T-(2A+3\varepsilon T)\bigr)w+A.
 \end{split}
 \tag{J9}
$$

But $2A+3\varepsilon T=T+B+u<2T$, so (J9) is strictly
positive. Thus

$$
|Y_i|>\varepsilon(r-k+|Y_{<i}|).
 \tag{J10}
$$

This is the same order of growth as in the individual-owner
construction. The joint requirement does not force an extra inverse
power of $\varepsilon$ in the depth bound. At an attempted failed
growth test the flat $J_i\cup A_i$, together with the physical
cover and the availability tests, also gives a valid infeasibility
certificate through (J6).

The same integer signature $(-|X_i|,|Y_i|)$, resource identities,
and one-at-a-time earliest exchanges therefore still give a rank
quasipolynomial bound. This observation alone does not improve that
bound: the progress coordinate may still decrease by one.

## 3. A jointly independent free family need not give a useful early batch

It is tempting to collect a large family of resource-free candidates,
use its joint independence to replace equally many blockers, and then
apply a fixed-fraction layer-collapse analysis. The following linear
matroid example isolates why that implication needs another premise.

Let the current independent set contain the vectors

$$
I=\{e_1,\ldots,e_L,\ f_1,\ldots,f_L\}
 \tag{J11}
$$

of a vector-space basis. The ambient matroid may have one additional
independent direction, so $|I|<r$ as in a real augmentation phase.
Place $e_1,\ldots,e_L$ in an earlier blocker layer $Y_1$
and $f_1,\ldots,f_L$ in a later layer $Y_2$. Consider the
candidate player elements

$$
g_t=e_1+f_t\quad(1\le t\le L),
             \qquad F=\{g_1,\ldots,g_L\}.
 \tag{J12}
$$

The family $F$ is independent over $J_3=\varnothing$.
Each $g_t$ has fundamental circuit
$\{g_t,e_1,f_t\}$ in $I\cup\{g_t\}$, so every
candidate's earliest circuit layer is $Y_1$, and every such
circuit has the **same** earlier blocker $e_1$.

A complete batch exchange is possible: replace all $f_t$ by
all $g_t$, keeping all $e_j$. This replaces $L$ matching
owners. But the flat required by the retained second layer changes
from

$$
\mathrm{span}\{f_t:1\le t\le L\}
          \quad\text{to}\quad
          \mathrm{span}\{e_1+f_t:1\le t\le L\}.
 \tag{J13}
$$

Thus this batch does not inherit the earlier-flat preservation lemma.
It can invalidate a retained candidate whose owner is, for example,
one of the $g_t$.

Conversely, if the batch is required to remove blockers only from
the earliest layer $Y_1$, keeping the later basis vectors, its
incoming elements have rank **one** modulo the span of the later
vectors. It can therefore replace at most one member of $Y_1$.
That is only a $1/L$ fraction of the earliest layer even though
$|F|=L$. The analogous batch wholly in $Y_2$ cannot preserve
the old $J_2$ flat, because no $g_t$ lies in that flat.

This example concerns the proposed matroid implication. It does not
assert that every such set configuration is reached by a particular
fixed-order allocation execution. It is enough to show that joint
independence and a large free-family cardinality, by themselves, do
not prove a geometric collapse while retaining the old flat
certificates.

## 4. Projected rank cannot be converted freely into actual candidates

Another proposed repair would count the rank of the portion of a free
family's span lying in a protected earlier flat, then select that many
free players from the flat. This is not a valid matroid implication.

Over a field of characteristic different from two, take

$$
F=\{e_1+e_2,e_1-e_2\},\qquad L=\mathrm{span}\{e_2\}.
 \tag{J14}
$$

Here $\mathrm{span}(F)\cap L=L$ has dimension one,
but neither actual candidate element belongs to $L$. The vector
$e_2$ is a linear combination of candidate elements; it is not
automatically a player with a resource-free bundle. In an independence-
oracle matroid there is not even a supplied vector representation from
which such a new player could be constructed.

Hence an argument based only on rank increments or intersections of
spans must still prove that the required **subset of actual candidate
players** exists. Virtual linear combinations do not implement an
allocation exchange.

## 5. The remaining substantive algorithmic gate

A polynomial analysis needs more than the growth in (J10). A useful
new lemma would have to supply one of the following explicit progress
contracts, or another contract with a comparably bounded potential.

1. Find a large simultaneous exchange that preserves eligibility and
   sufficient maximality information for **every retained layer**,
   while deleting a constant fraction of a suitable earlier blocker
   prefix.
2. Permit some retained flats to change, but charge the invalidated
   selected bundles and their certificates to a progress measure that
   decreases polynomially often. Simply discarding them does not
   preserve the current signature: a loss of an earlier $X_i$
   can increase its first affected coordinate.
3. Keep a different representation of retained matroid information
   that survives a full rank batch, and prove that its fractional
   availability inequality still refers to the actual matched players
   and actual free resource bundles.

The less restrictive requirement that all stored $A_h$ remain
jointly independent, without preserving their whole underlying flats,
could allow more batches than (J3). However, it does not by itself
preserve earlier maximality: a changed eligibility flat can expose
new players. Refreshing all such layers would need a paid adoption
or certificate-repair argument. This is a concrete next direction,
not a completed polynomial-time bound.

The current verified gain is therefore the joint-layer variant and
its unchanged growth scale. The quasi-to-polynomial transfer remains
open at the batch-retention and progress interface.
