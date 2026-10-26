# Intrinsic-value allocation near factor two

**Guarantee**

For a supplied budget $k$, if $\gamma(\theta_\star)\le k$ at $\theta_\star=(1-\varepsilon)\mathrm{OPT}/2$, returns minimum value at least $(1-\varepsilon)\mathrm{OPT}/2$. Choosing $\varepsilon=\eta/(2+\eta)$ gives factor $2+\eta$.

**Objective and output**

Allocate integral counts to every compulsory player. Enumerate heavy-value splits and retain the best legal allocation.

**Randomness**

Deterministic split enumeration, omission branching and integral recovery, including optional-player, exact-two and constructive local-search fallback variants.

**Time**

$\Gamma(1/\varepsilon)^k\mathrm{poly}(H)$, where $\Gamma(R)=R^R/(R-1)^{R-1}$. The simpler sufficient promise is $\nu(\theta_\star)\le k$.

**Space**

Polynomial in the complete binary input and paid oracle workspace; numerical resource multiplicities are not expanded into individual units.

**Parameters**

$N_\theta$ is the Boolean-cap matroid of the sum of resource ranks with unit value at least $\theta$; $\nu(\theta)=\mathrm{rank}(N_\theta)$; $\gamma(\theta)=\nu(\theta)-\#\{\text{coloops of }N_\theta\}$. $0<\varepsilon<1$ is rational. $H$ includes the explicit ground, all rational and integer encodings, and paid rank, submodular-minimization, LP, intersection, and decomposition work.

**Model and representation**

Compulsory players, common intrinsic resource values, arbitrary integral recipient polymatroids, and unused resources allowed. This manuscript has no setup or assignment budget.

**Lower-bound scope**

No upper bound strictly below factor two is inferred. The refined-parameter-zero oracle barrier is proved in the [lower-bound record](../allocation-lower-bounds/refined-parameter-barrier.md).

**Review status**

The [verification note](verify/README.md) records the proof scope, executable evidence and remaining conditions. No proof-assistant verification or external peer review is claimed.

**Source**

[Manuscript and proof](proof.md), with [dependencies and verification sources](sources.md).

The algorithm does not interpret a skipped split as infeasibility. A separate polynomial $8+\zeta$ fallback, for fixed $\zeta>0$, remains valid when the heavy-parameter promise fails. Optional player selection and exact costs have their own [joint-role proof](../unrelated-values-joint-role/README.md).

## Optional player selection through a derived light matroid

The [player-selection theorem](player-selection.md) extends the intrinsic,
unbudgeted model to a basis of any original player matroid $M$.
At threshold $\theta$ define

$N_\theta=\mathrm{Boolean}\left(\sum_{j:v_j\ge\theta}f_j\right)$,
$K_\theta=(M^*\vee N_\theta)^*$,

and delete the loops of $K_\theta$. If its remaining ground is $Q_\theta$,
put $c(\theta)=\lvert Q_\theta\rvert-\mathrm{rank}(K_\theta)$.

**Factor $2+\eta$ on an actual original basis**

If $c(\mathrm{OPT}/(2+\eta))\le k$, time is $\Gamma((2+\eta)/\eta)^k\mathrm{poly}(H)$ for rational $\eta>0$

**Polynomial fallback**

Factor $8+\zeta$ for any fixed $\zeta>0$, whether or not the derived-corank condition holds

**Rank and corank identities**

$\mathrm{rank}(K_\theta)=\mathrm{rank}(M)-\nu(M,N_\theta)$ and $c(\theta)\le q-\mathrm{rank}(M)+\nu(M,N_\theta)$, where $\nu$ is maximum common-independent-set size

Every output uses an actual original basis and integral recipient counts.
The derived parameter need not be monotone in the threshold; all value
splits are enumerated. This extension has no assignment or setup budget,
and its exponent is not asserted to depend on original player corank
alone. The compulsory-player statement above is its free-matroid
specialization.

## Exact-factor-two endpoints

The [half-optimum corank manuscript](exact-two-boundaries.md) uses the
same original player matroid and resource model as player-selection.md,
but evaluates $c(\theta)$ at the exact threshold $\theta=\mathrm{OPT}/2$.

**Exact factor two, XP time**

If $c(\mathrm{OPT}/2)\le k$, time is $(q+1)^k\mathrm{poly}(H)$, with polynomial workspace

**Exact factor two, polynomial endpoint**

$c(\mathrm{OPT}/2)=0$; the loopless derived light matroid has a unique basis

**Exact factor two, quantified light-value separation**

If $c(\mathrm{OPT}/2)\le k$ and $u_L\le(1/2-\sigma)\mathrm{OPT}$ for supplied rational $0<\sigma\le1/2$, time is $\Gamma(1/\sigma)^k\mathrm{poly}(H)$

The separated-value endpoint needs the stated separation: strict inequality $u_L<\mathrm{OPT}/2$
alone can have exponentially small relative slack in the binary input.
An exact-factor-two $F(k)\mathrm{poly}(H)$ theorem for unrestricted intrinsic
values is not established. The companion also proves a two-unit
coverage counterexample to matroid augmentation, explaining why a
second heavy-cover layer cannot be imported automatically.

**Attribution.** Yilin Liu · GPT-6 Astra Pro
