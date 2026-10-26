# Two short normalized ranges at arbitrary lattice scales

Author: Yilin Liu. Assistance: OpenAI Codex, including GPT-6 Astra.

## Theorem

Partition the coordinates into $`A,B,D`$, each of size at most $`m`$, and
put $`N=2^m`$. After complementing negative coordinates in the first
two blocks and adjusting the target, suppose their sums have forms
$`g_Ax`$, $`g_By`$, where $`g_A,g_B`$ are positive integers and

```math
0\le x\le W_A,\qquad0\le y\le W_B.
```

The third block is unrestricted. For any positive integer $`C`$ with
$`C^2\ge\max\{N,W_A+1,W_B+1\}`$, exact deterministic decision and
witness recovery use

```math
T=O^*(NC+C^3),\qquad S=O^*(C+\sqrt N).
```

In particular two individual ranges $`W_A,W_B\le O^*(2^m)`$ suffice
for time $`O^*(2^{n/2})`$ and space $`O^*(2^{n/6})`$ when
$`n=3m+O(1)`$. There is no restriction on $`g_A/g_B`$ or the third
block's range. This is a detectable input class, separate from the
general $`0.18261635770550353`$ writable-space theorem.

The partition and positive lattice scales are part of the input contract.
They can be checked by exact divisibility and summation. For a block with
weights $`w_i`$, complementing its negative coordinates gives

```math
w(S)=\sum_{w_i<0}w_i+
 g\sum_i\frac{|w_i|}{g}\,1_{i\in S\mathbin\triangle D_-},
\qquad D_-=\{i:w_i<0\}.
```

Thus one may take the gcd of the nonzero absolute weights as the scale
(scale one for an all-zero block) and
$`W=\sum_i|w_i|/g`$. No modulus is factored or expanded into a table of
its own size. Original indices, including repeated and zero weights,
are retained throughout.

## 1. Exact quotient coordinates

Let $`g=\gcd(g_A,g_B)`$, $`\alpha=g_A/g`$, and $`\beta=g_B/g`$.
For a raw third-block mask with weight $`w_D`$, put $`z=t-w_D`$.
If $`g\nmid z`$, discard it. Otherwise $`R=z/g`$ must satisfy

```math
\alpha x+\beta y=R.
```

Since $`\gcd(\alpha,\beta)=1`$, $`R`$ uniquely determines
$`x_0=x\bmod\beta`$ and $`y_0=y\bmod\alpha`$. Writing
$`x=x_0+\beta u`$, $`y=y_0+\alpha v`$ gives the exact condition

```math
u+v=q,\qquad
q=\frac{R-\alpha x_0-\beta y_0}{\alpha\beta}.
```

Least nonnegative residues are used throughout; negative target
quotients are rejected against the actual nonnegative quotient ranges.

## 2. Charged primitives

Two Boolean arrays of length at most $`C`$ can be convolved exactly
in $`O^*(C)`$ bit time and space by the
[elementary convolution lemma](convolution.md). It proves a deterministic
fixed-point transform, including rational construction of its roots,
rounding error below $`1/4`$ and the cost of schoolbook arithmetic on
$`O(\log C)`$-bit words. No fast multiplication theorem is needed.
Store the integer coefficients in an array and one mask per occupied
input slot. A single $`O(C)`$ scan recovers a witness after a positive
coefficient is found.

One may choose the least integer capacity satisfying the required square
bound, by exact integer square root. Its bit length is $`O(n+L)`$.
Choosing this capacity also proves the stated bounds for any larger
$`C`$, by monotonicity; the algorithm need not allocate an unnecessarily
large user-specified capacity. Thus the convolution's logarithmic factors
are included in the fixed polynomial in $`n,L`$.

A raw block congruence-and-interval query costs $`O^*(\sqrt N+J)`$
time and $`O^*(\sqrt N)`$ space. Store its two half lists, sort the
second by residue and actual weight, and binary-search the matching
residue slice and translated interval for each first-list record.
$`J`$ counts all reported mask occurrences, including equal sums.
The modulus length is never an allocation size.

For nested positive moduli $`Q_1\mid Q_2`$, all raw masks can also be
streamed in $`(w\bmod Q_1,w\bmod Q_2,w)`$ order in $`O^*(N)`$ time and
$`O^*(\sqrt N)`$ space. Here is an explicit construction of this
primitive. Sort the second half list by those three keys and an occurrence
identifier. Record the nonempty primary groups, and within each primary
group record its nonempty secondary groups. The entire directory is
linear in that half list.

For a first-half sum $`x`$ and fixed affine offset $`d`$, set $`s=x+d`$.
Adding $`s`$ rotates the primary residues, with cut at $`(-s)\bmod Q_1`$.
Within the current primary group it rotates the secondary residues,
with cut at $`(-s)\bmod Q_2`$. Binary search locates each cut in the
shared directory. The divisibility $`Q_1\mid Q_2`$ ensures that a
secondary group stays inside one shifted primary group. Actual weights
within a secondary group retain their order. A row therefore needs only
its current primary group, secondary group, occurrence position and wrap
counters. It visits only nonempty groups and emits every right-list
occurrence once. A heap holding one head per first-half record merges
these sorted rows. Group transitions and heap work cost a polynomial
factor per emitted occurrence; no right list or directory is copied per
row. Signed weights and arbitrarily large moduli change only the bit
length of the keys.

The large-scale case below applies the same primitive to the scaled
normalized A weights, obtaining $`(\alpha x\bmod\beta,x)`$ order because
$`\alpha>0`$, and to the affine D weights $`z=t-w_D`$. Their actual order
and original mask identifiers are retained.

## 3. Both reduced scales at most C

Suppose $`\alpha,\beta\le C`$. In each $`x_0`$ residue, split its
nonnegative $`u`$ range into width-$`C`$ blocks, and do the same for $`v`$.
The total numbers of quotient blocks satisfy

```math
K_A\le\beta+(W_A+1)/C\le2C,\qquad
K_B\le\alpha+(W_B+1)/C\le2C.
```

Stream the A blocks once. For each A block regenerate the B stream,
fill the two occupancy arrays, and convolve them. If their starts are
$`s_A,s_B`$, query third-block masks at the residue
$`z\equiv g(\alpha x_0+\beta y_0)\pmod{g\alpha\beta}`$ and within
the interval corresponding to
$`q\in[s_A+s_B,s_A+s_B+2C-2]`$. Compute $`q`$ and inspect the coefficient.

Each third-block occurrence has one compatible residue pair. For
each fixed A block, its quotient belongs to at most two B sum bands;
over all blocks it is therefore reported $`O(C)`$ times. Raw output
cost is $`O^*(NC)`$. There are $`O(C)`$ whole B passes and $`O(C^2)`$
convolutions and query starts. The latter cost $`O^*(C^3)`$ because
$`\sqrt N\le C`$. Only the current blocks and constant many stream
states coexist.

## 4. A large reduced scale

Otherwise swap A and B if needed so $`\beta\ge C`$.
The full A quotient class at residue $`x_0`$ has ambient length

```math
L_A(x_0)=\lfloor(W_A-x_0)/\beta\rfloor+1\le C.
```

Process $`O(C)`$ B batches described below. For each batch, stream A
in $`(\alpha x\bmod\beta,x)`$ order and D on $`z=t-w_D`$ in
$`(z\bmod g\beta,z\bmod g\alpha\beta,z)`$ order. Merge their
primary groups, ignoring residues not divisible by $`g`$. A matched
secondary D residue $`r_2`$ identifies

```math
y_0=\left((r_2/g-\alpha x_0)/\beta\right)\bmod\alpha.
```

The division is exact. Every record in that secondary group has the
same compatible B class and increasing target quotient $`q`$.
If the current batch contains that class or segment, test whether
$`q`$ lies in the two ambient quotient intervals' sum band. Activate
the convolution only at the first relevant raw D occurrence, reuse
it for the rest of the secondary group, then release it. An empty
relevant group pays no convolution. All rejected D records are still
charged to the full raw scan.

If $`\alpha\le C`$, one width-$`C`$ segment of a B residue class is
a batch. There are at most $`\alpha+(W_B+1)/C\le2C`$ batches.
Fill each batch by a complete B mask scan. A D occurrence is relevant
to at most two segments, because their starts are separated by $`C`$
and $`L_A\le C`$. Charging each activated convolution to its first
relevant D occurrence gives at most $`2N`$ activations in total.

If $`\alpha\ge C`$, each full B class has length at most $`C`$.
Enumerate only $`0\le y_0\le\min(\alpha-1,W_B)`$ and pack whole
class arrays greedily into batches of capacity $`2C`$. Their total
ambient length is $`W_B+1\le C^2`$; every nonfinal batch has more
than $`C`$ slots. Thus there are at most $`C+1`$ batches. A complete B
scan fills one batch's arrays. Every D occurrence has one B class
in one batch, giving at most $`N`$ convolution activations. This also
handles arbitrarily large lattice scales without enumerating an
absent modulus range.

Whole A, B, and D scans cost $`O^*(NC)`$. Activated convolutions cost
$`O^*(NC)`$. Conservatively, clearing the actual A class arrays costs
at most $`\sum_{x_0}L_A(x_0)=W_A+1\le C^2`$ per batch, hence
$`O(C^3)`$ overall. B batches use $`O(C)`$ slots each. These charges
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
convolution are live. Their state is $`O^*(C+\sqrt N)`$, including
witness masks, heap directories, and polynomial-bit moduli and keys.
The convolution's root and transform arrays use $`C\,\mathrm{poly}(\log(C+2))`$
bits, already charged.

Dropping $`C^2\ge N`$ retains the more precise time bound

```math
O^*\!\left(NC+(C+\sqrt N)C^2\right),
\qquad S=O^*(C+\sqrt N).
```

Only the small-scale query startup changes to $`\sqrt N`$ per block
pair. If both ranges are at most $`W\le N`$, choose
$`C=\lceil\sqrt{W+1}\rceil`$: the time is $`O^*(N\sqrt{W+1})`$
and state $`O^*(\sqrt N)`$. Explicitly enumerated signature or
cardinality configurations multiply this time by their actual count.
Signed affine coordinates are permitted after translating their
accepted ranges and the target; membership filtering charges all raw
masks and retains the chosen configuration in every witness.

The theorem is conditional on the supplied three-block partition and its two normalized range bounds. It does not assert that arbitrary instances admit such a partition.

## 6. Executable evidence

The [range-identity check](verify/check_range_identities.py) verifies the
quotient formulas, ambient batches and packed coefficient identities.
The separate [reference solver check](verify/check_range_solver.py)
implements the two scale regimes, the shared-directory nested stream,
closed-interval queries, lazy convolution activation and restoration of
indexed witnesses. It compares every tested decision with independent
exhaustive mask enumeration, including negative and repeated weights,
zero and empty blocks, nontrivial gcds, unequal block sizes and lattice
scales of more than 80 bits.

This is finite evidence for the full control flow. Its packed-product
convolution is exact, while the asymptotic algorithm can use the
elementary transform above. The separate
[fixed-point transform check](verify/check_exact_convolution.py) constructs
all roots by rational arithmetic and compares its coefficients with direct
summation. These checks do not replace the arbitrary-length error and
resource proofs. The [source map](sources.md#short-range-theorem-arithmetic-proof)
records the discharged arithmetic dependency.

**Curated by:** Yilin Liu and GPT-6 Astra Pro.
