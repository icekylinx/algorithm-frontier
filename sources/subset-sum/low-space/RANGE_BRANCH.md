# Two short normalized ranges at arbitrary lattice scales

Author: Yilin Liu. Assistance: OpenAI Codex, including GPT-6 Astra.

## Theorem

Partition the coordinates into $A,B,D$, each of size at most $m$, and
put $N=2^m$. After complementing negative coordinates in the first
two blocks and adjusting the target, suppose their sums have forms
$g_Ax$, $g_By$, where $g_A,g_B$ are positive integers and

$$
0\le x\le W_A,\qquad0\le y\le W_B.
$$

The third block is unrestricted. For any positive integer $C$ with
$C^2\ge\max\{N,W_A+1,W_B+1\}$, exact deterministic decision and
witness recovery use

$$
T=O^*(NC+C^3),\qquad S=O^*(C+\sqrt N).
$$

In particular two individual ranges $W_A,W_B\le O^*(2^m)$ suffice
for time $O^*(2^{n/2})$ and space $O^*(2^{n/6})$ when
$n=3m+O(1)$. There is no restriction on $g_A/g_B$ or the third
block's range. This is a detectable input class, separate from the
general $137/750$ theorem.

## 1. Exact quotient coordinates

Let $g=\gcd(g_A,g_B)$, $\alpha=g_A/g$, and $\beta=g_B/g$.
For a raw third-block mask with weight $w_D$, put $z=t-w_D$.
If $g\nmid z$, discard it. Otherwise $R=z/g$ must satisfy

$$
\alpha x+\beta y=R.
$$

Since $\gcd(\alpha,\beta)=1$, $R$ uniquely determines
$x_0=x\bmod\beta$ and $y_0=y\bmod\alpha$. Writing
$x=x_0+\beta u$, $y=y_0+\alpha v$ gives the exact condition

$$
u+v=q,\qquad
q=\frac{R-\alpha x_0-\beta y_0}{\alpha\beta}.
$$

Least nonnegative residues are used throughout; negative target
quotients are rejected against the actual nonnegative quotient ranges.

## 2. Charged primitives

Two Boolean arrays of length at most $C$ can be convolved exactly
in $O^*(C)$ bit time and space. Pack entries into fields of width
$\lceil\log_2(C+1)\rceil$; coefficients are at most $C$, so fields
do not carry into one another. Quasi-linear deterministic integer
multiplication supplies the stated cost. Packing and unpacking are
linear bit-field passes. Store one mask per occupied slot; a single
$O(C)$ scan recovers a witness after a positive coefficient is found.
The required multiplication theorem is David Harvey and Joris van der
Hoeven, *Integer multiplication in time O(n log n)*, Annals of
Mathematics 193 (2021), 563–617,
[doi:10.4007/annals.2021.193.2.4](https://doi.org/10.4007/annals.2021.193.2.4).

A raw block congruence-and-interval query costs $O^*(\sqrt N+J)$
time and $O^*(\sqrt N)$ space. Store its two half lists, sort the
second by residue and actual weight, and binary-search the matching
residue slice and translated interval for each first-list record.
$J$ counts all reported mask occurrences, including equal sums.
The modulus length is never an allocation size.

For nested moduli $Q_1\mid Q_2$, all raw masks can also be streamed
in $(w\bmod Q_1,w\bmod Q_2,w)$ order in $O^*(N)$ time and
$O^*(\sqrt N)$ space. Sort the second half list in this order.
Adding a fixed first-half value rotates its primary groups and then
its secondary groups, preserving actual order within a full residue
group. Binary-search the two cut positions. Each first-half record
defines a sorted row with constant wrap state; a heap merges the
rows. Only nonempty groups are visited, and no right list is copied
per row. Signed weights and an affine offset preserve this proof.

## 3. Both reduced scales at most C

Suppose $\alpha,\beta\le C$. In each $x_0$ residue, split its
nonnegative $u$ range into width-$C$ blocks, and do the same for $v$.
The total numbers of quotient blocks satisfy

$$
K_A\le\beta+(W_A+1)/C\le2C,\qquad
K_B\le\alpha+(W_B+1)/C\le2C.
$$

Stream the A blocks once. For each A block regenerate the B stream,
fill the two occupancy arrays, and convolve them. If their starts are
$s_A,s_B$, query third-block masks at the residue
$z\equiv g(\alpha x_0+\beta y_0)\pmod{g\alpha\beta}$ and within
the interval corresponding to
$q\in[s_A+s_B,s_A+s_B+2C-2]$. Compute $q$ and inspect the coefficient.

Each third-block occurrence has one compatible residue pair. For
each fixed A block, its quotient belongs to at most two B sum bands;
over all blocks it is therefore reported $O(C)$ times. Raw output
cost is $O^*(NC)$. There are $O(C)$ whole B passes and $O(C^2)$
convolutions and query starts. The latter cost $O^*(C^3)$ because
$\sqrt N\le C$. Only the current blocks and constant many stream
states coexist.

## 4. A large reduced scale

Otherwise swap A and B if needed so $\beta\ge C$.
The full A quotient class at residue $x_0$ has ambient length

$$
L_A(x_0)=\lfloor(W_A-x_0)/\beta\rfloor+1\le C.
$$

Process $O(C)$ B batches described below. For each batch, stream A
in $(\alpha x\bmod\beta,x)$ order and D on $z=t-w_D$ in
$(z\bmod g\beta,z\bmod g\alpha\beta,z)$ order. Merge their
primary groups, ignoring residues not divisible by $g$. A matched
secondary D residue $r_2$ identifies

$$
y_0=\left((r_2/g-\alpha x_0)/\beta\right)\bmod\alpha.
$$

The division is exact. Every record in that secondary group has the
same compatible B class and increasing target quotient $q$.
If the current batch contains that class or segment, test whether
$q$ lies in the two ambient quotient intervals' sum band. Activate
the convolution only at the first relevant raw D occurrence, reuse
it for the rest of the secondary group, then release it. An empty
relevant group pays no convolution. All rejected D records are still
charged to the full raw scan.

If $\alpha\le C$, one width-$C$ segment of a B residue class is
a batch. There are at most $\alpha+(W_B+1)/C\le2C$ batches.
Fill each batch by a complete B mask scan. A D occurrence is relevant
to at most two segments, because their starts are separated by $C$
and $L_A\le C$. Charging each activated convolution to its first
relevant D occurrence gives at most $2N$ activations in total.

If $\alpha\ge C$, each full B class has length at most $C$.
Enumerate only $0\le y_0\le\min(\alpha-1,W_B)$ and pack whole
class arrays greedily into batches of capacity $2C$. Their total
ambient length is $W_B+1\le C^2$; every nonfinal batch has more
than $C$ slots. Thus there are at most $C+1$ batches. A complete B
scan fills one batch's arrays. Every D occurrence has one B class
in one batch, giving at most $N$ convolution activations. This also
handles arbitrarily large lattice scales without enumerating an
absent modulus range.

Whole A, B, and D scans cost $O^*(NC)$. Activated convolutions cost
$O^*(NC)$. Conservatively, clearing the actual A class arrays costs
at most $\sum_{x_0}L_A(x_0)=W_A+1\le C^2$ per batch, hence
$O(C^3)$ overall. B batches use $O(C)$ slots each. These charges
prove the announced bound without requiring free array initialization.

## 5. Correctness, witnesses, and smaller ranges

A genuine solution has one residue pair and one quotient decomposition.
Its quotient blocks are processed together in the small-scale case.
In the large-scale case its B segment is in a processed batch, its A
and D primary groups match, and its target activates or queries the
correct convolution. A positive coefficient supplies actual occupied
slots and retained masks. The quotient identity proves their original
sum equals the target. Reversing the initial complements returns an
indexed witness. Finite exhaustion gives the exact NO decision.

At most two raw stream states, one A class, one B batch, and one
convolution are live. Their state is $O^*(C+\sqrt N)$, including
witness masks, heap directories, and polynomial-bit moduli and keys.
Convolution integers have $O(C\log C)$ bits, already charged.

Dropping $C^2\ge N$ retains the more precise time bound

$$
O^*\!\left(NC+(C+\sqrt N)C^2\right),
\qquad S=O^*(C+\sqrt N).
$$

Only the small-scale query startup changes to $\sqrt N$ per block
pair. If both ranges are at most $W\le N$, choose
$C=\lceil\sqrt{W+1}\rceil$: the time is $O^*(N\sqrt{W+1})$
and state $O^*(\sqrt N)$. Explicitly enumerated signature or
cardinality configurations multiply this time by their actual count.
Signed affine coordinates are permitted after translating their
accepted ranges and the target; membership filtering charges all raw
masks and retains the chosen configuration in every witness.

Support-four relation certificates and bounded annihilator signatures
are sufficient triggers recorded in [FRONTIER.md](frontier.md).
The general theorem does not assume that two such blocks always exist.
