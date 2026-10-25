# Checkpoint N: weighted corank selection, general values, and compressed scheduling

**25 October 2026. English research checkpoint.**

This checkpoint continues exclusively with related optimization
problems. The historical general-graph matching exponent 4/5 is
not being lowered in this work. Checkpoint M remains available
unchanged. This snapshot adds complete mathematical manuscripts,
independent audits and root reviews; it contains no Lean, PDF,
implementation or test bundle.

The principal advance is a deterministic weighted omission theorem
whose running time is single exponential in the number of omitted
elements, even with arbitrary nonnegative rational row coefficients.
It supports new general-value allocation, unrelated-value allocation,
exact-budget additive allocation, common-basis packing and binary
large-job-slot scheduling statements. These are different models
and have different parameters. The table and definitions below
keep those differences explicit.

These are internally reviewed research results. Primary-source
checks identify available comparison theorems and important scope
differences; they do not establish first-publication priority.

## 1. Main accepted statements

Write

\[
                  \Gamma(R)=\frac{R^R}{(R-1)^{R-1}}
                  \le eR,\qquad R>1.
\]

H denotes the full binary input and oracle-description length,
including the uniform rank-value and rational coefficient bit
bounds stipulated by the manuscripts. The polynomial factors
include polynomial-time exact matroid, submodular-minimization
and well-described rational-LP primitives where used. An oracle
description is not a claim of a strongly polynomial arithmetic
bound independent of all numeric encoding.

| Problem and exact scope | Accepted guarantee | Nonlinear time dependence | Parameter |
|---|---|---|---|
| Any polynomial restriction-selectable family of r-subsets; nonnegative weighted packing rows with polynomial-bit exact separation | If some permitted set supports quota t, find a permitted set supporting quota b, for t>b>0; otherwise a sound full-target failure | Gamma(t/(t-b))^c | c=q-r |
| Two exact matroid bases, arbitrary rational selection costs, arbitrary nonnegative weighted side capacities | Cost at most original integer OPT; every side capacity at most 1+epsilon times its original bound | Gamma((1+epsilon)/epsilon)^c | c=q-r on the explicit common ground |
| Intrinsic-value allocation with arbitrary recipient polymatroids and an arbitrary selected player-matroid basis | Approximation factor 2+eta under the stated derived-corank condition | Gamma((2+eta)/eta)^k | k bounds c(OPT/(2+eta)), defined in Section 3 |
| Same intrinsic-value model, exact factor two boundary cases | Polynomial at c(OPT/2)=0; XP for general k; single-exponential with quantified light-value separation | (q+1)^k, or Gamma(1/sigma)^k with the stated separation | Half-optimum derived corank, not the near-two threshold |
| Arbitrary player-dependent values with recipient polymatroids and a selected player basis | Every selected p receives at least max(0,(1-epsilon)OPT-u_p) | Gamma(1/epsilon)^c | Original player-matroid corank c |
| Same unrelated-value model, stronger selected-basis fractional comparator | Every selected p receives at least max(0,(1-epsilon)FOPT-u_p) | Gamma(2/epsilon)^c | Same c; FOPT still selects one actual basis |
| Either unrelated-value additive statement with one nonnegative assignment-cost budget | Same utility guarantee against its budgeted comparator; budget satisfied exactly | Same respective Gamma bases | Same c; one assignment budget |
| Arbitrary-size job-polymatroid scheduling, with binary-encoded multiplicities of the largest size a | Always a public additive fallback; at bounded optimum slot surplus, makespan at most (1+epsilon)OPT+u | Gamma(1/epsilon)^k, for 0<epsilon<=1/2 | k bounds the compressed largest-slot surplus at OPT |

Each row has an additional factor polynomial in H and uses polynomial
workspace. Some corank parameters are ordinary ground-set cardinalities;
the slot-surplus parameter can be large in binary. Section 6 explains
why the latter space claim does not silently expand that many copies.

The earlier exact factor-two unit-allocation and exact three-halves
two-size scheduling results in `(27/4)^c poly(H)` remain accepted.
So does the compulsory-player two-value factor-two result in
`(27/4)^nu poly(H)` from M. Their exact integer boundary guarantees
are not replaced by the new additive or near-two statements.

## 2. Weighted first-crossing certificates preserve the exponential base

The selector is a deterministic polynomial procedure that, for an
allowed set Q, returns some permitted r-set contained in Q or certifies
that none exists. A permitted family need not itself be a matroid.
Examples include common bases of two matroids, with one exact linear
cost threshold enforced by weighted matroid intersection.

At a node Q, a violated row has nonnegative coefficients a and
capacity u, with `b*a(Q)>u`. A promised t-feasible set I must omit
weight greater than `a(Q)/R`, where `R=t/(t-b)`. Order Q by decreasing
row coefficient. A layer-cake identity implies that the omitted set
has more than a 1/R fraction in at least one prefix of that order.

Branch only on the first prefix at which this strict density is
crossed. A certificate is a zero-one word; ones specify elements to
delete, and every proper prefix stays at density at most 1/R.
These first-crossing words are prefix-free. Their Bernoulli measure,
used only for deterministic counting, gives

\[
             \sum_{\text{certificates }C}
                    \Gamma(R)^{-|C|}\le1.
\]

The proof pays for certificate generation as well as recursive
children. At deletion budget d, the generator has at most
`(q+1)Gamma(R)^d` states, including unsuccessful partial words.
The augmented recursion, including children rejected by the selector,
therefore costs `poly(H)(d+1)Gamma(R)^d`. There is no uncharged
factor from arbitrary weights, a failed branch, or certificate
enumeration. All words use the explicit ground, so a large binary
R does not cause an expanded word representation.

This replaces an earlier weighted singleton-deletion bound containing
a factorial in c. The weighted theorem now has the same Gamma base
as the unweighted batch argument. It uses no random choices.

**Read:** `corank_weighted_prefix_free_batching.md`, its independent
audit, and `weighted_corank_packing_root_audit.md`. The unweighted
selector and exact-cost common-basis applications are developed in
`corank_packing_selection_oracle_extension.md` and
`corank_degree_bounded_common_bases.md`.

For explicit zero-one rows with integer capacities at most U, a
separate exact branching argument improves the augmentation-based
specialization: choose any u+1 elements of a violated row and delete
one of them. Every truly feasible solution omits one, giving exact
feasibility and cost optimization in `(U+1)^c poly(H)`. This exact
integer-capacity statement does not extend unchanged to arbitrary
rational weighted rows.

## 3. Arbitrary intrinsic values: factor 2+eta with original-basis recovery

Let M be the original player matroid of rank r. Each resource type j
has a common intrinsic value v_j and an arbitrary integral recipient
polymatroid f_j. Allocation counts are independent vectors and unused
resources are allowed. Types have no additional cross-type local
constraint. This is not limited to two values or to ordinary items.

For a threshold theta, let N_theta be the Boolean matroid of the
sum of the resource ranks of types whose value is at least theta.
Define

\[
       K_\theta=(M^*\vee N_\theta)^*,\qquad
       c(\theta)=|\operatorname{nonloops}(K_\theta)|
                       -\operatorname{rank}(K_\theta).
\]

The near-two theorem processes all distinct value splits whose
derived corank is at most the supplied budget k. If
`c(OPT/(2+eta))<=k`, it achieves factor `2+eta` in the time in
the main table. The algorithm need not know OPT to enumerate those
splits. A skipped split is never treated as an infeasibility proof.
The accepted public polynomial fallback is retained when the
parameter condition does not hold.

The original optimum yields a derived K-basis consisting only of
players receiving no heavy unit. Their light allocation still has
value OPT. An additive corank algorithm produces light value at
least `(1-epsilon)OPT-u_L`, where u_L is the largest light value.
With `epsilon=eta/(2+eta)` and the critical threshold
`theta=OPT/(2+eta)`, this exceeds theta. Every other player in the
recovered original M-basis receives one heavy unit worth at least
theta.

Recovering that original basis is a proved step, not a postprocessing
assumption. Every basis of `M* union N_theta` spans M*. Extend the
M* component of its union decomposition to an M*-basis inside that
union basis. Its complement is an original M-basis containing the
light basis; the newly added players form an N_theta-independent
set and can receive the promised heavy units.

For compulsory players M is free, so the derived parameter is the
heavy-cover rank minus its number of coloops. The more conservative
heavy-cover rank is a sufficient parameter bound. For arbitrary M,
the stated derived corank must not be replaced by the original
player-matroid corank without proof.

**Read:** `corank_arbitrary_value_additive_allocation.md`,
`general_value_allocation_heavy_cover_near_two.md`,
`general_value_matroid_selection_near_two.md`, their independent
audits and `general_value_near_two_root_audit.md`.

### The exact-two boundary is now precise

At threshold OPT/2, exact factor two is polynomial when the derived
corank is zero, since the loopless derived matroid has just one basis.
Enumerating omitted sets gives an exact-two XP baseline
`(q+1)^k poly(H)` for `c(OPT/2)<=k`. If additionally
`u_L <= (1/2-sigma)OPT`, the additive method yields exact factor two
in `Gamma(1/sigma)^k poly(H)`.

For unrestricted binary values, setting epsilon arbitrarily small
does not close the FPT gate: the separation of u_L below OPT/2 can
be exponentially tiny in its bit encoding. Replacing a one-heavy-unit
cover by a two-medium-unit cover also does not automatically work;
the latter feasible player sets need not be a matroid. The exact-two
gate note proves these positive cases and gives an explicit failed
augmentation example. It does not infer hardness from those failed
proof routes.

A separate hidden-set value-oracle construction excludes every
factor strictly below two even when the refined corank is zero.
It is consistent with exact factor two at that endpoint. This is
an oracle-query lower bound, not explicit-input hardness and not
an optimal exponential-base claim.

**Read:** `general_value_exact_two_corank_gate.md`, its independent
audit, and `near_two_refined_parameter_zero_oracle_barrier.md`.

## 4. Arbitrary player-dependent values: additive corank selection

Now the same resource j can have an arbitrary nonnegative rational
value v_pj at player p. There need not be a single global ordering
of resource types. The utility region is the downward convex sum
of diagonal images of the resource independence polytopes.

The manuscripts give an exact polynomial-bit nonnegative support
separator for this region. An outer rational LP chooses a normalized
nonnegative normal. Its support constraints are separated by greedy
resource optimization. Downward closure proves that nonnegative
normals suffice, even when the region is lower dimensional. Thus
the weighted corank theorem applies directly to utility quotas.

After selecting a genuine player basis, an exact LP reconstructs
fractional counts. Lower rounding uses a different decreasing
value order at each player. The corresponding prefix-cap rank is
still the direct sum of integral polymatroids on the player rows.
Intersecting it with the resource duals gives integer counts and
loses at most the largest eligible unit value u_p at each player.

The integer-OPT comparison uses the common rational utility grid.
The stronger FOPT comparison needs a separate relative-precision
search: FOPT relaxes only resource counts while choosing one actual
basis. Averaging one feasible positive unit per player gives a
polynomial-bit positive scale `v_min/r`, when such a basis exists.
This closes the search without assuming a grid for fractional OPT.

The results remain additive. If all selected unit values are small
relative to OPT, they imply the corresponding near-one relative
guarantee; that hypothesis must be stated. They do not by themselves
give a constant factor for arbitrary unrelated-value Santa Claus.

**Read:** `unrelated_values_corank_additive_allocation.md`, its
independent audit and `unrelated_values_and_exact_budget_root_audit.md`.

## 5. One exact assignment budget without losing the additive theorem

The budgeted extension allows nonnegative assignment costs c_pj and
requires `sum c_pj n_jp <= C`. The support LP now optimizes the
whole budgeted resource polytope, since the budget couples types.
The manuscript proves a uniform polynomial vertex-bit bound before
using those vertices in the outer separation LP. This avoids an
unjustified assumption about the encoding of projected normals.

The rounding proof cannot complete allocations to their original
resource bases: that could add cost. Instead, every resource gains
a zero-cost, zero-value disposal coordinate holding unused supply.
Complementation then produces the same prefix-constrained integral
intersection. On its maximum-total face, maximize the dual cost
objective. The integral optimizer has dual cost at least that of
the fractional witness, so the complemented original assignment
has cost no greater than the witness. Prefix utility guarantees
are unchanged. Disposal does not add candidate players or copies
of binary supply units.

The final budget is exact. The fractional comparator still chooses
one genuine player basis. When C>0, an individually expensive unit
can be fractionally affordable and must not be removed just because
its whole-unit cost exceeds C. At C=0, removing positive-cost
coordinates is exact. Both cases are handled in the proof and the
positive fractional search scale.

This mechanism preserves one linear assignment budget. It does
not automatically preserve several such budgets. It also does not
justify a budgeted near-two heavy/light theorem: independently chosen
parts can spend the same budget twice. Such a stronger transfer
requires a separate selection argument and is not included as a
proved result in this snapshot.

**Read:** `unrelated_values_exact_budget_additive_allocation.md`,
its independent audit and the combined root audit above.

## 6. Binary largest-job slots and an additive near-one scheduling bound

Let a be the largest processing size, with aggregated job-polymatroid
rank f_b and total h=f_b(P). Let u<a be the largest remaining size.
All jobs must be assigned, unlike the optional waste in allocation.
At a target makespan T define the number of possible largest-job
slots at machine p as

\[
 s_p(T)=\min\{f_b(\{p\}),\lfloor T/a\rfloor\},\qquad
 c_{\rm slot}(T)=\sum_p s_p(T)-h.
\]

The promised parameter is `c_slot(OPT)<=k`; feasibility of the
large-job box is checked separately. It can hold when many large
jobs share a machine, so this theorem is not restricted to T<2a.

The slot matroid is conceptual. The algorithm stores only machine
counts and computes the large-job box rank by submodular minimization.
Each deficiency branches on a deletion-count vector rather than
individual slot labels. The number of vectors is bounded by the
same binomial certificate bound.

Polynomial space requires extra care because k itself can be large
numerically. When k is below the square of the number of machines,
ordinary bounded-depth recursion has polynomial depth. Otherwise,
a direct count-vector enumeration uses binary counters; its number
of vectors is at most `(k+1)^q <= e^k <= Gamma(1/epsilon)^k` for
the stated epsilon range. This hybrid pays for both running time
and space without expanding binary multiplicities.

With b=(1-epsilon)t, the returned largest counts leave a smaller-job
fractional workload whose upper rounding loses at most u. The restored
largest-job load is at most epsilon*T above its discounted load,
giving `(1+epsilon)T+u`. A parameter-capped one-sided search ensures
the final successful target is at most original OPT whenever the
optimum meets the slot-surplus bound. An over-budget target is not
reported as infeasible. The public additive fallback remains valid
in every case.

For example, if `u<=epsilon*OPT`, the conditional bound is
`(1+2epsilon)OPT`. This is a useful explicit regime; the +u term is
not omitted from the unrestricted theorem.

**Read:** `compressed_large_slots_corank_makespan.md`, two independent
audits and `compressed_large_slots_corank_root_audit.md`.

## 7. Public and OpenAI comparison boundaries

The public recipient-polymatroid paper by Bamas and coauthors gives
the directly relevant general intrinsic-value and two-value constant
approximation baselines and the largest-unit additive rounding
ingredients. The new time guarantees above depend on corank or slot
surplus; they are not unconditional polynomial improvements for every
instance of those models. Classical cost-preserving unrelated-item
rounding is also acknowledged explicitly in the budgeted extension.

The new weighted-packing comparison checks STACS 2026 integer
programming with resource augmentation, SODA 2026 augmentation of
packing dynamic programs, and 2026 weighted approximate monotone
local search. Coefficient-independent approximation already appears
in this literature. The distinguishing statement here is the exact
restriction-selector interface with nonlinear dependence on the
number of omitted elements, including implicit packing rows. The
checked sources use different parameters or structural assumptions.
No claim of uniform domination or exhaustive novelty is made.

A current-source clarification also prevents an outdated ordinary
Santa Claus headline. Cheng and Mao provide a checked constructive
4+delta algorithm. An official January 2026 IIT Madras thesis-defense
abstract announces 3.534+epsilon, but this bounded audit did not locate
and check its complete algorithm proof. Haxell--Szabo's published
53/15 integrality-gap statement must likewise be distinguished from
a controlled construction time. None of these ordinary-item sources
states the arbitrary recipient-polymatroid extension used here.

The public OpenAI mathematics index was rechecked in M. Its identified
polymatroid-counting and scheduling entries are not substitutes for
the exact selection theorems above: common integer points in scaled
polymatroid bases need not be scaled zero-one bases, and the listed
scheduling model is different. This is a bounded public-index audit,
not a claim to have accessed private OpenAI baselines or exhaustively
verified every indexed proof.

**Read:** `weighted_corank_packing_primary_comparison.md`,
`ordinary_santa_2026_announced_baseline_clarification.md`,
`corank_public_and_oai_baseline_recheck.md`, and the cited primary
sources linked directly in those notes.

## 8. Review status and what remains open

The weighted prefix-free core, arbitrary-value additive transfer,
heavy-cover and arbitrary-player near-two adapter, unrelated-value
projection, exact-budget rounding and compressed slot scheduling
have full written proofs and independent mathematical audits. Root
reviews check the major interfaces, target-search directions,
rank/base recovery, failed-branch charges and binary space bounds.
The exact-two gate has its own independent audit. These reviews do
not amount to external certification.

The unresolved goals are specific: remove eta from the unrestricted
general-value FPT theorem at the half-optimum derived parameter;
obtain a multiplicative guarantee for unrelated values without a
small-unit condition; and combine arbitrary heavy/light assignment
costs under one exact budget. None is claimed solved in N.

New applications to selected multicommodity flow and structured
budgeted heavy/light allocation are being investigated separately.
They are not included as accepted theorems merely because their
initial interfaces look promising.

The archive retains earlier checkpoints as research chronology.
Current claims are the precisely scoped statements in this summary
and the named accepted manuscripts. Older draft or best-known
language is not a replacement for the later audits and source
version clarifications.
