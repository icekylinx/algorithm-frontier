# A repeated-owner interface in the public matroid allocation algorithm

**25 October 2026. Source-interface audit, not a disproof of a published theorem.**

This note isolates a condition needed before treating a parameter
reoptimization of Davies--Rothvoss--Zhang as an independently verified
algorithmic baseline. It does not alter their stated Theorem 2 or claim
that every choice in their algorithm fails. It exhibits a literal
execution permitted by the displayed pseudocode and explains what a
stronger exchange rule would have to exclude.

Primary source: Davies, Rothvoss and Zhang, *A Tale of Santa Claus,
Hypergraphs and Matroids*, arXiv:1807.07189v4, 4 January 2026,
Algorithms 1--2 and Lemmas 8--12:

<https://arxiv.org/html/1807.07189v4>.

## 1. The parameter calculation and its scope

Write $\delta=u/T$, and choose

$$
\alpha=(1-\delta)/2,\qquad
 \beta=\alpha^2-\eta>0,\qquad d=\alpha-\beta,
$$

where $0<\eta<(1-\delta)^2/4$. The choices

$$
\kappa=\frac{\eta}{2d(1-\alpha)},\qquad
 \mu=\frac{\eta}{2d(1+\delta)},\qquad
 \phi=\frac{d}{\alpha+\delta}
 \tag{P1}
$$

make the exact expression for $\mu$ in the source's Expansion Lemma
positive. Indeed $\alpha+\delta=1-\alpha$ and

$$
1-\alpha-\delta-\frac{\beta(\alpha+\delta)}d
     =\frac{\alpha^2-\beta}{d}=\frac\eta d,
$$

of which the $\kappa(\alpha+\delta)$ term uses exactly one half.
The source's geometric blocker coefficient becomes

$$
c_g=\frac{d\mu}{\beta+\delta+\kappa d}
     =\frac{2\eta}{(1+\delta)^3-4\delta\eta}.
 \tag{P2}
$$

Here $\kappa=2\mu$, $\mu\ge\eta$,
$\phi\ge\alpha>\sqrt\eta$, and
$\eta/4\le c_g<1/2$. Thus all these constants are quantitatively
positive for fixed $\eta$. Lemmas 9 and 10 use these symbolic
parameters; their resource inequalities do not require the numerical
choices printed earlier in the source.

There is a separate, harmless constant-choice issue in applying
Lemma 11. Its premise includes both geometric blocker growth and a
lower bound on the size of the proposed exchange set relative to the
earlier blocker prefix. A fresh expansion supplies the latter only with
coefficient $\phi\mu$; an internal collapse supplies it with
coefficient $\kappa c_g$. A conservative legal common constant is

$$
c_* = \min\{c_g,\phi\mu,\kappa c_g,1/2\}>0.
 \tag{P3}
$$

Use $\gamma(c_*)$ from Lemma 11, rather than silently substituting
$\gamma(c_g)$ in every call. This still gives polynomial running
time for fixed $\eta$, if the swap-interface invariant discussed
next is supplied. In fact $c_*\ge\eta^2/2$ for the parameter range
above. The leading candidate value is
$((1-\delta)^2/4-\eta)T$.

## 2. A condition required by the swap subroutine

At a call to source Algorithm 2, let $S$ be the independent player
set, $i_0\in S$ the exposed player, and $D'$ the players covered
by the resource-free candidate edges. The displayed subroutine asks
for an earlier player set $C'$ such that

$$
|C'|=|D'|,\qquad (S\setminus C')\cup D'\in\mathcal I.
 \tag{P4}
$$

To retain the intended cardinality, this also needs

$$
D'\cap(S\setminus C')=\varnothing.
 \tag{P5}
$$

When $D'$ is a fresh output of Lemma 8, its membership in
$(P\setminus S)\cup C$ makes a suitable cardinality-preserving
exchange available. For a previously stored adding layer, this player
membership must still be true after intervening changes of $S$.

Algorithm 1 requires a new expansion's resources to avoid the resources
of old adding and blocking layers. It does not impose disjointness of
their player names. Consequently a newly matched player can already
own an adding edge in a retained layer. The matching may then have two
different resource bundles associated with that player in the two
roles, even though their resources do not intersect.

## 3. A concrete allowed execution

Take $T=1$, $\delta=1/10$,
$\alpha=9/20$, $\beta=1/5$, and $\eta=1/400$.
Then $\kappa=1/110$, $\mu=1/220$,
$\phi=5/11$, and $c_g=1/266$.

Use the rank-two uniform matroid on players $s_0,y,p$.
Start an augmentation phase with

$$
S=\{s_0,y\},\qquad M=\{e_y\},
$$

where $s_0$ is exposed. The bundle $e_y$ consists of three
resources of value $19/200$, for a total of $57/200$. It is a
minimal $\beta$-bundle, because deleting any resource leaves
$38/200<1/5$.

Player $p$ likes all three of these resources, two additional
resources of value $9/100$, and five further distinct resources of
value $19/200$. Let

* $A_1$ contain the single adding edge owned by $p$ using the
  first three resources and the two resources of value $9/100$;
* $H_2$ contain the single adding edge owned by $p$ using the
  last five resources.

The first adding edge has value $93/200$, is inclusion-minimal
above $\alpha=90/200$, and has only $36/200<\beta$ value
free of $M$. Thus it is blocked, rather than already having a
free $\beta$-subbundle. The next layer has $B_1=\{e_y\}$.
The first expansion is legal: with discovered set $\{s_0\}$,
replacing $s_0$ by $p$ preserves independence; a singleton
expansion exceeds its required size $\mu$.

The second adding edge has value $95/200$, is minimal above
$\alpha$, and is entirely resource-disjoint from the previous
adding edge and from $M$. The discovered set is now
$\{s_0,y\}$; this second singleton expansion exceeds
$2\mu$, and is again jointly eligible for the current call.
It has a free minimal $\beta$-subbundle, obtained by taking any
three of its five resources.

In this second call, the displayed swap rules allow choosing
$C'=\{y\}$, and consequently swapping out $e_y$ for the new
bundle of $p$. The selected collapse layer is 1. The resulting
state is

$$
S=\{s_0,p\},\qquad M=\{e_p^{\rm new}\},\qquad
  A_1\text{ retained},\qquad B_1=\varnothing.
 \tag{P6}
$$

The retained edge in $A_1$ is now entirely resource-free. The
inner collapse loop therefore calls Algorithm 2 on that edge with
layer index 1. Its candidate player set is $D'=\{p\}$.
The only earlier exchange player is $s_0$. Taking
$C'=\{s_0\}$ satisfies the literal tests (P4), because

$$
(S\setminus\{s_0\})\cup\{p\}=\{p\}
$$

is independent. But its size is one, not two. The exposed-player branch
then attempts to return the existing matching together with a second
edge also owned by $p$. This is not a matching on the player side
and does not cover a rank-two independent set. Condition (P5) fails.

The numerical instance may be made fractionally feasible at target 1:
give each of $s_0$ and $y$ ten private resources of value
$1/10$. They provide an integral feasible basis allocation, while
leaving all the displayed choices legal. The initial bundle $e_y$
can itself be produced in an earlier phase: an adding edge consisting
of its three resources and two private resources has sufficient value,
and its minimal $\beta$-subbundle may be chosen as $e_y$.
Fixed scan orders can prioritize the displayed adding edges.

This execution is not forced. For example, in the second expansion
one could instead choose $C'=\{s_0\}$ and augment immediately.
The point is that the displayed independence tests and resource-side
disjointness alone do not prove the invariant for all allowed choices.
A proof using a particular stronger choice rule must state and verify
that rule, including its batch exchanges and quantitative progress.

### 3.1 The same interface test with the source's printed parameters

This issue is not caused by the alternative constants. Take the source's
own choices with $T=1$, $\delta=1/10$, and source approximation
slack $\varepsilon=1/100$. Then
$\alpha=71/200=0.355$, $\beta=17/100$, and
$\kappa=1/200$. Its expansion coefficient is approximately
$0.1133$, so one adding edge satisfies the expansion requirement
for a discovered set of size either one or two.

Use a matching bundle $e_y$ with two resources of value $0.1$.
Let the retained adding edge of $p$ consist of these two resources
and two additional resources of values $0.09$ and $0.07$.
Its total is $0.36$, it is minimal above $0.355$, and only
$0.16<0.17$ is initially free. Give $p$ four further private
resources of value $0.09$; together they form the second adding
edge, of total $0.36$. The same two swaps produce (P6) and the
same failure of (P5). Private target-value allocations for $s_0,y$
again make $Q(1)$ feasible. This is the same literal-choice test,
not an additional impossibility claim.

## 4. What remains to be proved for the candidate public retuning

A complete independently checked retuning would need one of the
following, or an equivalent invariant:

1. a swap selection rule that preserves joint eligibility and distinct
   player ownership for every retained adding layer;
2. a repair that removes or replaces newly invalid stored adding edges,
   together with a new proof that current layer growth and the polynomial
   iteration bound survive the repair;
3. a source theorem explicitly providing this retained-layer interface
   with the symbolic parameters used in (P1).

Checking only the positivity of $\mu,\phi,c_g,\gamma$ is
insufficient. Pending this interface, the square curve is recorded as
an algebraic candidate from the public analysis, rather than as a
fully audited derived theorem. The published Theorem 2 is still reported
as the published baseline, without treating this note as a retraction.

The new one-at-a-time current-blocker construction is independent of
this issue. Its earliest-circuit exchange explicitly preserves every
retained eligibility flat, handles an already matched candidate owner
separately, and discards the layer from which that candidate came. Its
audits are in [Current blocker growth for matroid max-min allocation](../allocation-and-scheduling/matroid-allocation-current-blocker-quasipolynomial.md)
and [Current blocker growth for matroid max-min allocation](../allocation-and-scheduling/matroid-allocation-current-blocker-quasipolynomial.md).
