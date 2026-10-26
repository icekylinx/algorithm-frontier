# Binary representation and the integer-comparator lemma

This manuscript supplies the representation and lower-cover arguments used by
the [prefix-normalized allocation theorem](proof.md). All resource
multiplicities remain binary encoded.

## 1. Allocation model

Let $P$ be a finite set of players and let $M$ be a matroid of rank
$r$ on $P$. Each resource type $j$ has a nonnegative rational value
$v_j$ and a normalized, monotone, integral submodular function
$f_j:2^P\to\mathbb Z_{\ge0}$. A legal allocation chooses a basis
$I$ of $M$ and vectors $n_{\cdot j}\in P(f_j)\cap\mathbb Z^P_{\ge0}$
supported on $I$, where

$$
P(f_j)=\{x\ge0:x(S)\le f_j(S)\text{ for all }S\subseteq P\}.
$$

Its utility at $p\in I$ is $\sum_jv_jn_{pj}$. Unused capacity is
allowed. The comparator $\mathrm{OPT}$ is the largest achievable
minimum utility of an integral allocation on an actual basis.

Optionally, player $p$ has a type-symmetric downward-closed family
$\mathcal F_p\subseteq\prod_j\{0,\ldots,f_j(\{p\})\}$. Given an
integer availability vector $A$, its supplied oracle returns a
feasible $n\in\mathcal F_p$, $n\le A$, whose value is at least
$\lambda$ times the best feasible value under $A$. The guarantee
$0<\lambda\le1$ is a certified rational input; write
$\tau=1/\lambda$. Without local restrictions the exact oracle returns
$A$. All oracle work and workspace are charged explicitly.

## 2. A conceptual natural matroid

For one resource $f=f_j$, imagine a block $E_p$ of
$f(\{p\})$ distinct copies at every player. Declare a set independent
when its vector of block counts lies in $P(f)$. Heredity follows from
downward closure; the augmentation axiom follows from integral
polymatroid augmentation. This defines a matroid, without constructing
its possibly enormous ground set.

**Lemma 1 (rank from counts).** A conceptual set with block-count vector
$z$ has rank

$$
R(z)=\min_{S\subseteq P}\{f(S)+z(P\setminus S)\}.
 \tag{R1}
$$

**Proof.** An independent subset has counts $h\in P(f)$ with
$0\le h\le z$. For every $S$, its total is at most
$f(S)+z(P\setminus S)$. Conversely, the box-restricted polymatroid has
rank
$$
f_z(A)=\min_{S\subseteq A}\{f(S)+z(A\setminus S)\},
$$
and $P(f_z)=P(f)\cap[0,z]$. Submodular uncrossing proves that $f_z$
is an integral polymatroid rank; an integral base attains $f_z(P)$.
This gives equality in (R1). In particular, the union of the full
blocks indexed by $S$ has rank $f(S)$. $\square$

Thus every rank query is one submodular minimization on the original
$|P|$ elements with a binary modular term.

## 3. Residual availability and distinct records

At any stage of the local search, selected centers $X$ and marked
matching records $Y$ reserve a count vector

$$
z^j_p=\sum_{\substack{c\in X\\p(c)=p}}n^c_j+
       \sum_{\substack{b\in Y\\p(b)=p}}n^b_j.
 \tag{R2}
$$

Replace coordinate $p$ by $f_j(\{p\})$, obtaining $z^{j,p}$, and
define

$$
A_{pj}=R_j(z^{j,p})-R_j(z^j).
 \tag{R3}
$$

**Lemma 2 (block availability).** For every integer
$0\le a\le A_{pj}$, any $a$ unused copies of player $p$ are
independent after contraction of the reserved set. Moreover,
$A_{pj}\le f_j(\{p\})-z^j_p$.

**Proof.** In (R1), separate the sets $S$ containing $p$ from those
not containing $p$. Increasing $z_p$ by $a$ leaves the first
minimum unchanged and increases the second by $a$. The increase of
the minimum is therefore $\min\{a,A_{pj}\}$ until the entire block
has been added. Symmetry within a block makes the identity independent
of which unused copies are chosen. $\square$

Matching records have distinct owners. A candidate owner already
matched must have its old matching record in the preceding marked
prefix: otherwise it lies in the eligibility flat and cannot be
chosen. Hence all its old copies are included in (R2). All prior
selected records are also included. Lemma 2 supplies disjoint copies
for every new record, even when one owner occurs in several layers.
An exchange moves the incoming record's own copies into the matching
and deletes the outgoing record; it never identifies two record
labels. The numerical execution therefore has a simultaneous
realization in one fixed conceptual matroid.

Only record count vectors, owners, and layer flags are stored.
No copy identities or unary arrays are needed. Minimality above a
positive utility threshold $B$ is achieved in one pass over types:
remove
$$
\min\left\{n_j,\left\lfloor
       \frac{\sum_iv_in_i-B}{v_j}\right\rfloor\right\}
$$
units of each positive-value type $j$. Downward closure preserves
feasibility, and each surviving unit is essential when the pass ends.
Zero-value units can be deleted.

## 4. Loss against an integral comparator

Let $J$ be the current eligibility base, let
$w=r-r_M(J)>0$, and suppose a complete scan at an unchanged state
finds no available bundle of value at least $B$. Put

$$
\Phi=\sum_jv_jR_j(z^j).
 \tag{R4}
$$

**Lemma 3 (integer lower cover).** If a target-$T$ integral allocation
exists on a basis and $\tau B\le T$, then

$$
\Phi>(T-\tau B)w.
 \tag{R5}
$$

**Proof.** Let $I^*$ be such a basis and
$E=I^*\setminus\operatorname{cl}_M(J)$. Since a basis has at most
$r_M(J)$ elements in this flat, $|E|\ge w$. Restrict the target
allocation to $E$, and denote its count vector of type $j$ by
$n^*_{\cdot j}$.

Contract the reserved conceptual set $W_j$. The full owner blocks
induce the integral polymatroid
$$
g_j(S)=r_j(W_j\cup E_{S,j})-r_j(W_j).
$$
It has $g_j(\{p\})=A_{pj}$, and
$$
g_j(S)\ge f_j(S)-R_j(z^j).
 \tag{R6}
$$
Box restriction by $n^*_{\cdot j}$ provides an integral
$h_{\cdot j}\le n^*_{\cdot j}$, $h_{\cdot j}\in P(g_j)$, with
$$
\begin{aligned}
 h_{\cdot j}(P)
 &=\min_{S\subseteq P}
      \{g_j(S)+n^*_{\cdot j}(P\setminus S)\}\\
 &\ge n^*_{\cdot j}(P)-R_j(z^j).
 \end{aligned}
 \tag{R7}
$$
The last step uses $n^*_{\cdot j}(S)\le f_j(S)$. Thus at most
$R_j(z^j)$ units of type $j$ are removed.

For each $p\in E$, the surviving bundle $h_p$ belongs to
$\mathcal F_p$ by downward closure and satisfies
$h_{pj}\le A_{pj}$. The completed failed oracle scan implies that its
value is strictly less than $B/\lambda=\tau B$. Its original value
was at least $T$. Summing the lost utility over $E$, and then using
(R7), proves
$$
\Phi>(T-\tau B)|E|\ge(T-\tau B)w.
 \qquad\square
$$

The proof uses an actual integral allocation. Fractional player masses
in an aggregate configuration LP cannot replace it; the
[configuration gap](../allocation-lower-bounds/configuration-gaps.md)
gives an explicit counterexample.

## 5. Large units and recovery of the original basis

At any chosen threshold $B_0>0$, a resource type is large if
$v_j\ge B_0$. Its unit-box restriction is the matroid $N_j$ with
rank
$$
r_{N_j}(S)=
    \min_{A\subseteq S}\{f_j(A)+|S\setminus A|\}.
 \tag{R8}
$$
Restrict this matroid to players for whom one unit is locally feasible.
The local oracle tests that condition exactly on a singleton input:
with positive value, a positive approximation guarantee returns a
nonempty feasible bundle precisely when the singleton is feasible.
Let $N=\bigvee_jN_j$ over the large types and $U=M^*\vee N$.

**Lemma 4 (large-unit reduction).** Every integral target allocation
on an $M$-basis contains a target allocation using only small types
on a $U^*$-basis. Conversely, a small-type allocation on a
$U^*$-basis can be completed to an $M$-basis by giving one large
unit to each additional selected player.

**Proof.** In a target allocation choose one large unit for each
player receiving any. Those players form an $N$-independent set;
the complement of the selected $M$-basis is $M^*$-independent.
Their union extends to a $U$-basis. Its complement is a
$U^*$-basis contained among the original small-only players.

Conversely, decompose a $U$-basis into an $M^*$-independent part
and an $N$-independent part. Extend the first part within that
$U$-basis to an $M^*$-basis. Such an extension exists because the
$U$-basis spans $M^*$: if an outside element increased its
$M^*$-rank, it could also augment its $U$-independent decomposition.
The complement of the extended $M^*$-basis is the required
$M$-basis. Its new players lie in the remaining $N$-part and
receive a unit through the matroid-union decomposition. Small and
large types are disjoint, and deleting recipients preserves all
feasibility constraints. $\square$

## 6. Encoding and dependencies

Every stored count is bounded by its singleton rank. Summing at most
a polynomial number of records adds only logarithmically many bits.
Submodular minimization, matroid duality and union, integral
polymatroid box restriction, and decomposition are the paid standard
primitives. The prefix invariants and progress analysis appear in the
[main proof](proof.md); Lemmas 1–4 supply its compressed representation
and its precise integer comparator.

**Attribution:** Yilin Liu and GPT-6 Astra Pro.
