# Corank omission with a changing residual budget

The earlier weighted omission theorem used one fixed packing region.
For the application below, the region changes with the allowed set,
but a single promised selected set remains feasible in every region
on a surviving branch. Reproving that invariant permits exactly the
same deterministic first-crossing enumeration and Gamma running time.
It removes the price-profile and proportional-cost assumptions from
the intrinsic-value budgeted heavy/light application.

The change of region is proved explicitly here. It must not be
silently substituted into the earlier fixed-region theorem.

## 1. Completion witnesses and a minimum-cost restriction oracle

Let P be an explicit q-element ground and let 1<=s<=q. A completion
pair (I,W) consists of a selected s-element set I subseteq P and a
witness W from a specified admissible relation. The witness has a
nonnegative rational completion cost h(W). Fix a nonnegative total
budget C.

For an allowed set Q subseteq P, assume a polynomial-time exact
oracle finds

$$
h(Q)=\min\{h(W):(I,W)\text{ admissible},\ I\subseteq Q,\ |I|=s\},
\tag{RB1}
$$

and an attaining pair (I_Q,W_Q), or reports that no such pair exists.
All returned costs and witnesses have uniform polynomial bit length.
The minimum is attained whenever the relation is nonempty. Put
c=q-s. In the allocation application W is a feasible one-heavy-unit
completion and this minimum is computed by weighted matroid
intersection, with zero weight on the light copies.

The restriction Q constrains I only. The ambient completion witnesses
and their original ground are retained. In particular, deleting a
light candidate does not delete its heavy assignment copies.

If Q' subseteq Q and both minima exist, then

$$
h(Q')\ge h(Q).
\tag{RB2}
$$

More importantly, for any fixed admissible witness (I*,W*) with
I* subseteq Q,

$$
h(Q)\le h(W^*).
\tag{RB3}
$$

The latter is the witness inequality needed by the branching proof.

## 2. The light service regions and their exact interfaces

For every rational B>=0, let U_B be a fixed-ground set of nonnegative
service vectors on P. Assume:

* U_B contains zero and is downward closed.
* If B<=B', then U_B subseteq U_B'.
* Exact membership at a polynomial-bit query z is implemented by
  either a real service witness of cost at most B, or a violated
  row `a*z<=u` valid for all of U_B, with a>=0 and u>=0.
* Membership, row encoding and witness reconstruction take polynomial
  time in the original data and the query encodings. For the budgets
  and targets used here those encodings have a uniform polynomial
  bound.
* Restricting a service witness from Q to a subset I preserves that
  subset's service, all its resource constraints, and does not
  increase its nonnegative cost.

For the allocation application, U_B is the utility projection of
the light recipient-polymatroid independent allocations with their
actual arbitrary nonnegative assignment costs and total cost at
most B. It has exactly these properties by the explicit budgeted
support LP in B. No heavy resource occurs among its light types.

An optional final rounding step can lose at most a stated additive
quantity while preserving the service witness's cost. That rounding
is outside the gap lemma itself. Integer unit quotas can instead be
recovered without service loss by the separate minimum-cost integral
intersection construction.

## 3. Full-target promise and desired relaxed output

Let t>b>0 be rational and put

$$
R=\frac{t}{t-b}>1,
          \qquad \Gamma(R)=\frac{R^R}{(R-1)^{R-1}}.
\tag{RB4}
$$

The full-target promise is the existence of an admissible pair
(I*,W*) satisfying

$$
h(W^*)\le C,
                   \qquad t\mathbf1_{I^*}\in U_{C-h(W^*)}.
\tag{RB5}
$$

The algorithm must return some admissible pair (I,W) with

$$
b\mathbf1_I\in U_{C-h(W)},
\tag{RB6}
$$

including its service and completion witnesses, or correctly report
that no pair satisfying RB5 exists. A successful relaxed output need
not certify the full target t.

**Theorem RB.** Under the stated exact oracle interfaces, this is
possible deterministically in `Gamma(R)^c poly(H)` time and polynomial
workspace, including unsuccessful branches and unpromised inputs.
The total cost of the returned two witnesses is at most C.

## 4. The recursive algorithm

At a node Q, let d=|Q|-s. If d<0, reject. Compute RB1. Reject if no
pair exists or h(Q)>C. Otherwise set

$$
B_Q=C-h(Q)\ge0.
\tag{RB7}
$$

Test `b*1_Q` for membership in U_(B_Q), with zeros outside Q.

If it belongs, keep the oracle's attaining pair (I_Q,W_Q), restrict
the service witness to I_Q, and return. Restriction preserves service
b and costs at most B_Q, while the completion costs h(Q). This is
an actual pair of witnesses with total cost at most C. There is no
independent second budget allocation or substitution of an unpriced
completion.

Otherwise obtain a valid violated nonnegative row
`a*z<=u` for U_(B_Q). Its weight on Q is W=a(Q), and `bW>u`.
If d=0 reject. For d>0, sort Q in nonincreasing a-weight and enumerate
the same first-crossing certificates as in
[Single-exponential corank time for weighted packing through first-violation prefixes](selection.md): a binary word on a prefix
with ell ones, 1<=ell<=d, whose last bit makes its one-density
strictly greater than 1/R, while every proper prefix has density
at most 1/R. Recurse after deleting its ell one-positions.

Try the certificates deterministically until one child returns a
solution. If none succeeds, reject. No old row is assumed to be a
complete description of a later residual region; each visited node
recomputes its own minimum completion and separation problem.

## 5. The fixed-witness invariant closes the changing-region issue

Fix one promised pair (I*,W*) from RB5. Suppose a recursive node Q
still contains I*. Its completion oracle cannot fail, and RB3 gives

$$
C-h(Q)\ge C-h(W^*)\ge0.
\tag{RB8}
$$

Budget monotonicity implies

$$
t\mathbf1_{I^*}\in U_{C-h(Q)}.
\tag{RB9}
$$

Thus every row returned at this particular node is valid for the
same promised service vector, even though the region is allowed
to change at the next node. With D*=Q\I*, |D*|=d, validity and
violation yield

$$
\begin{aligned}
       t a(I^*)&\le u<b a(Q),\\
       a(D^*)&=a(Q)-a(I^*)
                     >\left(1-\frac bt\right)a(Q)
                       =\frac{a(Q)}R.
 \end{aligned}
\tag{RB10}
$$

The layer-cake argument for ordered nonnegative coefficients then
gives a first-crossing prefix whose one-positions lie entirely in
D*. Its certificate is enumerated, and deleting those positions
preserves I*. At that child RB8--RB9 apply again, using the same
original W* and the newly recomputed h(Q'). This completes the
inductive promise preservation.

If d=0 then Q=I*, and downward closure of the current region gives
`b*1_Q` feasible from RB9. Hence a surviving promised branch cannot
reject at d=0. Every recursive descent decreases d, so it must find
a successful output. This proves the soundness of total failure.

Nestedness of the regions also follows from RB2, but the stronger
point is the explicit RB9 invariant. Merely observing that regions
are nested would not by itself prove that an optimal witness survives.
Nor would a generic arbitrary changing separator suffice.

## 6. Complete time and space accounting

At a node of deficit d, first-crossing words are prefix-free and
satisfy

$$
\sum_C\Gamma(R)^{-|C|}\le1.
\tag{RB11}
$$

The deterministic generator visits at most
`(q+1)Gamma(R)^d` states, including unfinished words, by the same
bounded-ones/zeros counting argument proved in WP. These are purely
combinatorial properties of R,d and the explicit sorted ground;
they do not depend on whether the row came from a fixed or a
residual-budget region.

Every attempted child either rejects after paid polynomial oracle
work or invokes the same algorithm at deficit d-|C|. With a uniform
polynomial bound P(H) covering completion optimization, separation,
reconstruction and generator overhead, the augmented recursion obeys

$$
T(d)\le P(H)\Gamma(R)^d+\sum_C T(d-|C|)
                \le P'(H)(d+1)\Gamma(R)^d.
\tag{RB12}
$$

The second inequality follows from RB11 and induction, using |C|>=1.
It charges failed selectors and unpromised branches. Because
c<=q, all recursion and local certificate stacks have polynomial
depth and entry size. The minimum completion cost has a fresh uniform
bit bound rather than an accumulated numerical description, so
changing h(Q) causes no recursive coefficient growth.

## 7. Boundaries of the lemma

One scalar completion cost can be minimized to obtain a single
residual budget that both lower-bounds every promised completion
and is attained by an actual output completion. Minimizing several
cost coordinates separately would not normally give one witness
attaining all those minima. This proof therefore does not preserve
multiple unrelated assignment budgets automatically.

Heavy and light resource feasibility must also separate except
through this budget and the completion relation. In arbitrary
player-dependent-value heavy/light partitions, the same original
resource type can contribute on both sides. A cheaper heavy
completion can consume different recipient capacity, invalidating
RB9 for the original light witness. The intrinsic-type partition
avoids that problem; the lemma does not resolve it by itself.

The minimum-cost completion oracle must be exact and polynomial.
An approximate minimum may exceed h(W*) and destroy RB8. A coordinatewise
lower bound on completion cost without an attaining pair would not
justify the successful-node construction either. Both properties
are required, and the two-matroid implementation provides them in
the stated applications.

This proof supersedes the earlier cost-coupling obstruction only
for the scalar-budget, independently partitioned-resource setting
where RB1--RB9 are established. Earlier price-profile algorithms
remain valid but are no longer needed to assume cost compatibility
in that setting. The original matching exponent is unrelated to
this refinement.

---

**Attribution:** Yilin Liu and GPT-6 Astra Pro.
