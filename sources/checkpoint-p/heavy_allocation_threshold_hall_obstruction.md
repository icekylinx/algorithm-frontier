# Constant heavy-allocation thresholds do not preserve a row matching

**25 October 2026. Explicit boundary example.**

The following proposed shortcut is false:

> If every row has at most three incidences, every row allocates L,
> and every bin has load at most L-C, then the incidences of value
> at least gamma L contain a matching saturating all rows, for some
> universal constant gamma>0.

The failure already occurs when the entire ordinary row/bin support
is a tree. The example also has a subcubic nonbipartite physical
realization, valid integral lower ledgers, zero debt, and an actual
matching gap of one. It is not a running-time lower bound or a claim
that a prescribed raw-gradient trajectory must visit these exact
top coordinates.

## 1. A path of rows with private bins

Fix any constant 0<gamma<1. Choose a power of two S>=8/gamma.
There are rows r_1,...,r_S, internal bins b_1,...,b_(S-1), and
private bins f_1,...,f_S.

The ordinary incidences are

r_i--f_i for 1<=i<=S,

r_i--b_i and r_(i+1)--b_i for 1<=i<S.

Thus the internal incidences form an alternating path, and every row
has one private leaf bin. Each internal row has degree three; the
two endpoint rows have degree two. The ordinary graph is a tree.

Every bin has weight one, top capacity L-C, and zero debt. Put

a=(L-2C)/S,

x_(r_i,b_(i-1))=(i-1)a when i>1,

x_(r_i,b_i)=(S-i)a when i<S,

x_(r_i,f_i)=tau=L-(S-1)a
                 =L/S+2C(S-1)/S.                         (1)

All displayed incidence values are positive. The two internal
contributions of a row sum to (S-1)a, including the natural
one-contribution endpoint cases. Hence every row sum is exactly L.

The two contributions to b_i are (S-i)a and i a. Thus

load(b_i)=S a=L-2C,       slack(b_i)=C.                   (2)

A private bin has

load(f_i)=tau,            slack(f_i)=L-C-tau>0.           (3)

The positivity condition holds, for example, at the matching phase
scale below.

## 2. Every constant heavy threshold loses Hall's condition

At L=10000 C N with N>=S,

tau/L = 1/S + (2C/L)(1-1/S)
      < gamma/8 + 1/(5000 S)
      < gamma.                                          (4)

Consequently none of the private incidences r_i--f_i survives a
threshold at gamma L. Every retained incidence of any row leads
to one of only S-1 internal bins.

The S rows therefore have a neighborhood of size at most S-1
in the thresholded graph. Hall's condition fails, regardless of
which internal incidences also fall below the threshold.

The full ordinary graph trivially has a row-saturating matching:
assign r_i to f_i. The conclusion concerns loss under the threshold,
not absence of a matching before it.

In particular, the fact that every row individually has an incidence
of value at least L/3 does not imply that these large incidences can
be chosen injectively. The obstruction is a collective neighborhood
deficit.

## 3. A genuine subcubic general-matching realization

Treat every bin as a singleton physical vertex, and initially match
r_i to f_i. Add two remainder vertices u,v with matched edge uv.
Add the unmatched physical edges f_2u and vf_3.

The physical graph is connected and has maximum degree three.
The cycle

f_2, r_2, b_2, r_3, f_3, v, u, f_2

has length seven, so this realization is nonbipartite.

The current matching has S+1 edges. The path

b_1, r_2, f_2, u, v, f_3, r_3, b_2

is augmenting, so a matching of size S+2 exists. On the other hand,
the physical vertex set consisting of all S rows together with u,v
is a vertex cover of size S+2. Hence the maximum matching size is
exactly S+2: the current matching has exact gap one.

There are N=3S+1 physical vertices. Taking the phase estimate K=1
gives precisely L=10000 C N, the scale used in (4).
The two remainder contacts are at f_2 and f_3. Their top slacks are
large and the next structural action may expand them; this example
does not assert that the numerical solver is stuck or should return
LOW. The failed claim is the unconditional heavy-support carrier
implication at a valid row/bin state.

## 4. Finite top coordinates and integral lower ledgers

Since S is a power of two, (1) uses a finite dyadic grid with
polynomial bit length. No limiting zero coordinate or infinitesimal
allocation is used.

For every integral floor c_0<=C, put

a_0=floor((L-2C)/S),

x^0_(r_i,b_(i-1))=(i-1)a_0,
x^0_(r_i,b_i)=(S-i)a_0,

x^0_(r_i,f_i)=L-(S-1)a_0.                                (5)

The same endpoint conventions apply. These allocations are integral,
nonnegative, and have row sum L. The internal-bin residual is

L-S a_0>=2C>=c_0.

The private-bin residual is (S-1)a_0, which is much larger than C
at the stated phase scale. Every lower ledger therefore satisfies
its weight-one floor with zero debt. The lower ledger need not
coincide coordinatewise with the top ledger; only their separate
row sums and residual requirements are used.

The prescribed injection r_i to f_i is valid on the physical
incidences. The ordinary support is already a forest, so no
forestification, cycle cancellation, or small-support rounding is
needed to expose the failure.

## 5. Scope of the boundary

This example rules out deriving a row-saturating carrier merely by
discarding all allocations below a universal constant fraction of L.
It also rules out justifying that deletion from the row-degree bound
or from positive column slack.

It does not rule out thresholds depending on a relevant set size:
the private leakage here is Theta(L/S+C). It does not rule out an
adaptive weighted carrier, a paid pivot rule, or a general path
oracle that retains receiving incidences independently of their
current allocation size.

In particular, off-basis or small-allocation receiving directions
remain part of the discovery problem. A carrier simplification must
prove its full matching or path interface, rather than only certify
that each row retains some individually large edge.

