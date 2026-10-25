# A value-oracle barrier below factor two for rank-parameterized allocation

**25 October 2026. Self-contained oracle lower bound; no novelty claim.**

The full recipient-polymatroid algorithm has running time f(r)poly(q,H),
where r is the rank of the player-selection matroid and q is the number
of potential players. This parameter distinction matters. In the same
black-box value-oracle model, a deterministic approximation factor
strictly below two cannot have such a runtime uniformly over all ranks.

The construction is a direct hidden-subset version of the familiar
matroid-parity oracle phenomenon. The proof below does not require
importing a matroid-parity lower-bound theorem. It is a lower bound
for the oracle model, not a complexity-theoretic hardness claim for
explicitly represented special classes.

## 1. The rank functions

Fix integers q>r>=1 and a q-element player set P. The player matroid
is the uniform matroid U_(r,q). There is one resource type with unit
value one. Define

\[
 f_0(S)=\min\{2|S|,2r\}-{\bf1}[|S|=r].
 \tag{O1}
\]

For each hidden r-element set A, define

\[
                 f_A(S)=f_0(S)+{\bf1}[S=A].
 \tag{O2}
\]

Both functions are normalized, monotone, integer-valued and
submodular. For f_0, the cardinality increments are

\[
             2,\ldots,2,1,1,0,\ldots,0,
\]

with the initial run of twos having length r-1. These increments
are nonincreasing and nonnegative, proving the claim.

Raising f_0(A) by one preserves monotonicity: every proper subset
has value at most 2r-2, while every strict superset has value 2r.
To check submodularity, only a raised right-hand side can matter.
If X union Y=A and neither X nor Y equals A, both are smaller than
r and their original submodular slack is exactly one. Raising the
union consumes that slack. If X intersection Y=A and neither X nor
Y equals A, both are strict supersets of A and the same statement
holds: their values and the union value are 2r, while the old
intersection value is 2r-1. Nested cases cancel the identical raised
term from both sides. A raised left-hand side cannot hurt. This
exhausts all cases.

Thus f_A is a valid integral recipient-polymatroid rank oracle,
with numerical values bounded by 2r.

## 2. The hidden basis is the only basis with value two

A feasible recipient-count vector n satisfies n(S)<=f_A(S) for all S.
Every player basis I has a feasible one-unit allocation n=1_I:
for sets smaller than r, the rank bound is 2|S|; for sets of size r,
it is at least 2r-1>=r; and larger sets have rank 2r.

For the hidden basis A, the vector n=2*1_A is feasible. At S=A
the required inequality is equality 2r=f_A(A). At any other
r-element S, at most r-1 players of A lie in S, so
2|A intersection S|<=2r-2<2r-1=f_A(S). Smaller and larger sets
are immediate from their rank bounds.

Conversely, if every member of an r-element output basis I receives
at least two units, then n(I)>=2r. Therefore f_A(I)>=2r, which by
(O1)--(O2) forces I=A. The optimum value is exactly two: no r-player
basis can receive value above two because f_A(P)=2r. In particular,
an approximation factor alpha<2 must identify A, since its integer
output value must exceed one.

## 3. The oracle transcript lower bound

The oracle f_A differs from f_0 at exactly one query set, namely A.
Consider a deterministic algorithm receiving only value-oracle
answers. Until it queries the hidden set, every answer agrees with
f_0. If at least two r-element sets remain unqueried, the same entire
transcript is consistent with either as the hidden set. A single
output basis cannot be correct for both.

Consequently a worst-case deterministic factor-alpha algorithm with
alpha<2 requires at least

\[
                           {q\choose r}-1
 \tag{O3}
\]

resource-oracle queries. This excludes a uniform f(r)q^c bound for
any fixed exponent c: choose a fixed rank r>c and then let q grow.
The values themselves have only O(log r) bits.

## 4. Scope of the obstruction

The construction permits multiple service units from the one resource
to one player. It does not prove the same lower bound for the
one-service-per-player recipient-matroid model without an additional
reduction. It also does not address succinct explicit representations
that reveal the hidden set through their encoding.

Most importantly, this is not an obstruction to the critical promise
problem "a four-unit basis exists; find a two-unit basis." The
constructed resource has optimum two, and the four-unit promise is
absent. Thus it cannot be used to close that remaining algorithmic
question or to explain away the discrete quasipolynomial-time gate.

The positive factor-four general-value algorithm and factor-three
unit-quota algorithm lie above this lower bound. The bound does not
show either approximation factor is best possible. It explains why
enumerating all q-player choices is not an innocuous replacement for
their rank-parameterized running times.

## 5. A corresponding scheduling barrier below factor three halves

The same construction gives a direct oracle lower bound for the
large-job parameter in `two_size_makespan_few_large_jobs_transfer.md`.
Take q>=r+2 machines, large-unit size a=2, and small-unit size u=1.
The large-job polymatroid is the ordinary uniform matroid U_(r,q),
so exactly h=r machines receive one large unit.

Define the small-job rank function by dualizing f_A with respect to
the all-twos vector:

\[
             g_A(S)=2|S|+f_A(P\setminus S)-2r.
 \tag{O4}
\]

This is normalized, monotone, integral and submodular. Submodularity
follows from complementing a submodular function and adding a modular
term. Monotonicity follows because every singleton marginal of f_A
is at most two. The total rank is 2q-2r, and q>=r+2 makes every
singleton rank exactly two. Thus every small-job base x_s has
0<=x_s(p)<=2.

The hidden set A supplies a schedule of makespan two:

\[
                 x_b={\bf1}_A,\qquad
                 x_s=2{\bf1}_{P\setminus A}.
 \tag{O5}
\]

Indeed, 2*1_A is a base of P(f_A), so its complement in the
all-twos vector is a base of P(g_A). Every machine has load exactly
two. Positive large jobs also imply that no schedule has smaller
makespan, so OPT=2.

Any approximation factor alpha<3/2 must return a schedule of
makespan strictly below three. Its loads are integral, hence all
loads are at most two. Every large-unit recipient consequently gets
zero small units. Let I be its r-element large-recipient basis and
put y=2*1-x_s. Base duality makes y a base of P(f_A); it has at
least two units on every member of I. Section 2 then forces I=A.

The value oracle g_A differs from g_0 at exactly the complement
P\A. Therefore the transcript argument of Section 3 again requires
at least binom(q,h)-1 value queries in the worst case. In particular,
there is no deterministic factor strictly below 3/2 algorithm with
f(h)poly(q,H) oracle runtime for this full two-size job-polymatroid
model.

This barrier and the constructive 5/3 upper bound concern the same
large-unit rank parameter h. They leave a gap between 3/2 and 5/3;
the upper bound is not claimed optimal. The lower bound relies on an
arbitrary small-job polymatroid supplied by a value oracle. It is not
a hardness theorem for ordinary restricted-assignment jobs given by
explicit allowed-machine lists, nor a barrier to the four-unit/two-unit
promise problem discussed above.

## 6. The same bounds hold when parameterized by corank

The transcript bounds are symmetric in rank and corank because
`binom(q,r)=binom(q,q-r)`. This gives a separate obstruction for
the new corank-parameterized algorithms.

For allocation, put c=q-r. The instance of Sections 1--3 has
player-matroid corank c, and every factor below two still requires
at least binom(q,c)-1 value queries. Consequently no uniform
deterministic running time f(c) times a polynomial in the explicit
ground size and input bit lengths can attain a factor below two
in this full value-oracle model. For any proposed fixed polynomial
degree, choose a fixed larger integer c and let q grow, with r=q-c.
The oracle values have only O(log q) bits, so their encoding length
does not absorb the binomial growth.

For scheduling, fix c>=2, take h=q-c, and use precisely (O4)--(O5).
The large-job matroid is U_(q-c,q), with corank c, while the small
polymatroid has total rank

\[
                         g_A(P)=2q-2h=2c.
 \tag{O6}
\]

The condition q>=h+2 is exactly c>=2. The optimum is still two.
Every factor below three halves must identify the hidden h-set A,
or equivalently its hidden c-element complement. The sole exceptional
query is that complement, and there are binom(q,c) possibilities.
The worst-case bound is therefore

\[
                   \binom qc-1
 \tag{O7}
\]

small-job rank-value queries. Fixing c above a proposed uniform
polynomial exponent again rules out f(c) polynomial-ground-size
time for every approximation factor strictly below three halves.

This is consistent with an exact three-halves guarantee in
fixed-parameter corank time: an output with makespan three need
not identify A. It supplies an oracle-model approximation threshold
for such a theorem, if that theorem's independent proof is closed.
It remains a black-box lower bound for arbitrary job polymatroids,
not a complexity-theoretic hardness theorem for explicit ordinary
restricted assignment or a lower bound for the critical four-unit
to two-unit promise itself.
