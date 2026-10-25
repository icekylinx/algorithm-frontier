# Exact factor two for general values: proved boundary cases and the remaining corank gate

**25 October 2026. Research status note with complete positive partial results;
no general hardness conclusion.**

The general-player theorem in
`general_value_matroid_selection_near_two.md` gives factor 2+eta
in single-exponential time in its derived corank. This note examines
whether eta can be removed while retaining fixed-parameter bit
complexity for arbitrary intrinsic values and arbitrary recipient
polymatroids. That full extension has not been established here.

Three positive statements are immediate but useful: exact factor
two is polynomial at derived corank zero; it is available in XP
time for any derived corank; and it is fixed-parameter tractable
when light values have a quantified separation below OPT/2. The
note then records two tempting routes that do not close the
unrestricted gate.

## 1. Definitions and the relevant half-optimum split

Keep the full model of the near-two manuscript: an arbitrary
original player matroid M, independent integral recipient
polymatroids f_j, common nonnegative intrinsic values, and optional
waste. For a threshold theta, define

\[
          N_\theta=\operatorname{Boolean}\!\left(\sum_{v_j\ge\theta}f_j\right),
        \qquad K_\theta=(M^*\vee N_\theta)^*.
 \tag{X1}
\]

Delete the loops of K_theta, obtaining ground Q_theta and rank
delta(theta). The derived corank is
c(theta)=|Q_theta|-delta(theta). At positive OPT, the exact-factor-two
threshold of interest is theta*=OPT/2, with equality counted heavy.
Every light value is strictly below theta*.

The audited dual-union adapter gives two facts. First, an original
optimal allocation contains a K_theta*-basis whose players obtain
OPT using only light types. Second, any K_theta*-basis can be
completed to an original M-basis by giving one heavy unit to each
new player. The completion preserves the chosen light players.

OPT=0 is trivial and needs no threshold parameter. Derived rank
zero is a pure-heavy polynomial case.

## 2. Exact factor two in XP time, including a polynomial zero-corank case

Enumerate all value-class splits, as in the near-two theorem. For
each split of positive derived rank whose derived corank c is at
most a supplied budget k, enumerate every c-element subset D of
its loopless ground Q. Set I=Q\D and test whether I is a basis of
the derived K. There are at most binom(|Q|,c) candidates, and the
iterator uses polynomial workspace.

For a surviving fixed basis I, compute an exact workload bound
without a quota gap. Choose a common positive value quantum g
and form the integral workload rank

\[
                       F(S)=\sum_{j\text{ light}}(v_j/g)f_j(S).
 \tag{X2}
\]

For an integer target ell, membership of ell*1_I in P(F) is
decided exactly by minimizing F(S)-ell|I intersect S|. Binary
search over the polynomial-bit range up to F(Q) finds the largest
feasible integer ell. Complete the workload vector, use the
compressed sum decomposition, and apply the per-player lower
rounding lemma. The result is an original light allocation of
value at least

\[
                                 g\ell-u_L,
 \tag{X3}
\]

where u_L is the largest light value. All these computations are
polynomial in the input bit length. A fixed-I integer allocation
of value T on the original g-grid guarantees ell>=T/g, so the
procedure dominates that integer target before paying u_L.

At the split theta*=OPT/2, the enumeration contains a promised
light basis I*. Its workload target is at least OPT, and therefore
its rounded light value is at least

\[
                             \mathrm{OPT}-u_L>\mathrm{OPT}/2.
 \tag{X4}
\]

Heavy completion contributes at least OPT/2 to every other
selected player. Hence, if c(OPT/2)<=k, this algorithm returns an
exact factor-two allocation in

\[
                            (q+1)^k\operatorname{poly}(H)
 \tag{X5}
\]

time and polynomial workspace, retaining the same public fallback
when the condition is absent. Skipping an over-budget split is
not an infeasibility assertion.

When k=0, the loopless derived matroid is free: Q is its unique
basis. Thus (X5) is polynomial. In particular, exact factor two
already holds at c(OPT/2)=0, even though a separate oracle lower
bound excludes every factor strictly below two at refined
parameter zero. There is no contradiction between these statements.

The XP bound is a baseline, not the desired fixed-parameter result:
the polynomial degree in q grows with k.

## 3. Exact factor two with a quantitative light-value gap

Fix rational 0<sigma<=1/2. Suppose that at theta*=OPT/2 the largest
light value obeys

\[
                         u_L\le(1/2-\sigma)\mathrm{OPT},
                   \qquad c(\mathrm{OPT}/2)\le k.
 \tag{X6}
\]

Run the same split-enumeration and heavy-completion algorithm, but
use the additive corank routine with epsilon=sigma on every
processed split. At the optimum split, its light output is at
least

\[
            (1-\sigma)\mathrm{OPT}-u_L\ge\mathrm{OPT}/2.
 \tag{X7}
\]

Together with heavy completion this yields exact factor two in
Gamma(1/sigma)^k poly(H) time and polynomial space. The algorithm
does not need OPT to enumerate the split or run the inner routine;
(X6) is the condition under which its guarantee applies.

This is a quantified value-separation regime. It does not solve the
general case in which a light value can approach OPT/2 with
arbitrarily high binary precision.

## 4. The numerical gate in the current additive route

At the exact half-optimum split, the additive theorem alone needs

\[
                   \epsilon\le\frac{\mathrm{OPT}/2-u_L}{\mathrm{OPT}}
 \tag{X8}
\]

to guarantee light value at least OPT/2. The right-hand side is
positive, but its reciprocal need not be polynomial in its binary
encoding.

For example, the numerical pattern OPT=2B, u_L=B-1 forces
epsilon<=1/(2B). If B is represented with L bits, plugging this
into the corank bound gives a dependence of order B^c rather than
a function of c times a fixed polynomial in L. Even at c=1 that
particular substitution can take exponential time in L, while the
XP enumeration above is polynomial for c=1. Thus this is a precise
limitation of the current additive-gap proof, not evidence of
hardness of the underlying exact-factor-two problem.

## 5. Why a second heavy-cover layer cannot simply use two medium units

A plausible idea is to classify light units in [OPT/4,OPT/2) as
medium. Two such units suffice for the desired half-optimum value.
An optimum player with at most one medium unit must receive more
than OPT/2 from the smaller units. This suggests another heavy-cover
adapter, but its proposed cover family would consist of players
that can each receive **two** medium units.

That family need not be a matroid. Consider players a,b,c,d and
the coverage polymatroid whose underlying resource neighborhoods
are

\[
 \begin{array}{c|c}
 a,b&\{1,2,3,4\}\\
 c&\{1,2,3,5\}\\
 d&\{1,2,3,6\}.
 \end{array}
 \tag{X9}
\]

Its rank on a player set is the cardinality of the union of these
neighborhoods. The set {a,b} can receive two units per player.
The larger set {a,c,d} can also receive two units each: its union
has size six and all pair unions have size at least four. But
neither c nor d can augment {a,b}, because either resulting triple
has union size five and would need six units. Matroid augmentation
therefore fails.

This example can coexist with a genuine strong allocation promise.
Add three players e,f,g with pairwise disjoint private neighborhoods
of size three, and use the player matroid U_(3,7). Give every unit
value 3/4. The basis {e,f,g} has value 9/4. Every basis containing
a private player has value at most 9/4 at that player, while a
basis of three original players has total resource count at most
six and hence smaller minimum value. Thus OPT=9/4, and all these
units lie in [OPT/4,OPT/2). The same failed augmentation persists.

This only invalidates the automatic use of a matroid dual-union
adapter for two-unit coverage. It is not a lower bound: the example
itself is a one-value instance already handled by the corank unit
algorithm. A successful repair would need to preserve the stronger
promise while dealing with the nonmatroid cover structure.

## 6. A simple attempted oracle obstruction also fails

The known hidden-basis resource f_A has optimum two on a uniform
rank-r player matroid, while every player basis admits one unit.
Adding a modular private bonus delta>0 to every selected player
does not turn its strict-below-two obstruction into an exact-two
obstruction. If its unit value is v, the new optimum is 2v+delta,
but any basis with one ordinary unit plus that same private bonus
has value

\[
                            v+\delta\ge(2v+\delta)/2.
 \tag{X10}
\]

The bonus helps the output as well as the hidden optimum. This
rules out that particular modification; it does not rule out a
more elaborate oracle construction. No exact-factor-two oracle
lower bound has been established in this investigation.

The present remaining task is therefore specific: attain exact
factor two for arbitrary intrinsic values in F(k)poly(H) time under
c(OPT/2)<=k, or derive a valid obstruction aligned with that same
parameter and exact ratio. The proved 2+eta theorem, the weighted
packing theorem, and the unit four-to-two gap result do not by
themselves close this integer boundary.
