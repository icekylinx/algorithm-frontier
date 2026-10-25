# Proof note

This file is the curated proof record for the result in `README.md`. The original source note follows.

**Original source:** `sources/checkpoint-o/global_exponential_allocation_flow_transfers.md`

# Global exponential-time allocation, scheduling and selected-flow transfers

**25 October 2026. Complete application manuscript; full root and independent reviews passed.**

The accepted corank gap routines remain valid after an arbitrary set of
candidate positions has been forbidden in advance. Applying the
polynomial-space inclusion-cover conversion therefore gives guarantees
for every corank, and removes the support-parameter promises from the
intrinsic-value allocation theorem. For example, exact factor two for
one-value budgeted allocation and compulsory two-value budgeted
allocation, and exact factor three halves for two-size scheduling, have
whole-ground base `50/27 < 2`.

The transformation `A^c -> (2-1/A)^(q+o(q))` is established monotone
local search. The substantive checks here are the forced-omission
interfaces, the unchanged full-target promises, and their compatibility
with cost recovery and target optimization. Polynomial space uses the
separate explicit block-cover proof in
`polynomial_space_global_gap_conversion.md`, rather than a space claim
inferred from the public derandomization theorem.

## 1. Models, time notation, and main guarantees

All recipient and job rank functions below are normalized, monotone,
integral submodular functions, with paid value-oracle access and the
polynomial deterministic optimization primitives specified in the
underlying manuscripts. Numerical multiplicities and all rational
values and costs are binary encoded. Allocation may leave resource
units unused; scheduling must assign all job units. No numerical unit
expansion is performed.

Let H include the explicit ground, every original numerical bit, and
the paid descriptions and costs of the required polynomial oracles.
For A>1 define

\[
 \mathcal T_A(q,H)=
 (2-1/A)^q\,
 2^{O(q\log\log(q+2)/\log(q+2))}\operatorname{poly}(H).
 \tag{E1}
\]

For each fixed A this is `(2-1/A)^(q+o(q)) poly(H)`. All algorithms
stated here are deterministic and use polynomial workspace. A table
of the principal consequences is:

| Problem and exact constraints | Guarantee | Explicit ground counted by q | Whole-ground time |
| --- | --- | --- | --- |
| One intrinsic value, original player matroid, arbitrary assignment costs, one exact budget | Value at least OPT/2 | Nonloop potential players | T_(27/4)(q,H) |
| Two intrinsic values, every player compulsory, arbitrary assignment costs, one exact budget | Value at least OPT/2 | Players | T_(27/4)(q,H) |
| Arbitrary intrinsic values, original player matroid, arbitrary assignment costs, one exact budget | Value at least (1-1/R)OPT/2 | Nonloop potential players | T_(Gamma(R))(q,H) |
| Two job sizes, arbitrary job polymatroids | Makespan at most 3OPT/2 | Eligible one-large-unit positions; at most all physical machines | T_(27/4)(q,H) |
| Selected splittable concurrent flow, exact permitted set family and routing constraints | Rate at least (1-1/R)OPT | Candidate commodities | T_(Gamma(R))(q,H) |

Here R>1 is a fixed rational accuracy choice and

\[
                \Gamma(R)=\frac{R^R}{(R-1)^{R-1}}.
 \tag{E2}
\]

The flow line also permits the explicit-scenario robust extension and,
under an exact minimum-setup restriction oracle, one shared setup and
routing budget. Their interfaces are checked in Sections 7--8.

## 2. The precise forced-omission wrapper

Fix a q-element candidate ground P and a required selected cardinality
s>=1. Put d=q-s. A full-target witness has a selected set I* of size s,
possibly with additional allocations, job placements or completions.
For every forced omitted set Z with |Z|<=d, require a procedure starting
on Q=P\Z that:

1. returns a valid relaxed-target solution of the original problem, or
   fails;
2. cannot fail if some full-target witness has I* contained in Q;
3. uses at most `A^(d-|Z|) poly(H)` time on every input, including
   unpromised inputs, and polynomial workspace.

The selected portion protected by the wrapper must be contained in Q.
Other parts of the returned solution may use original positions outside
Q when the model requires that, as with heavy recipients or machines
carrying only small jobs. The uniform polynomial factor includes all
failed selector and completion calls.

The block-cover theorem yields a relaxed solution, or soundly excludes
all full-target witnesses, in E1 time. Its proof enumerates deletion
counts in fixed logarithmic blocks, streams products of local greedy
containment covers, and invokes the original gap only once per seed.
Thus its approximation losses are not multiplied across blocks.

For clarity, the numerical base follows from the exact identity

\[
 \begin{aligned}
 &w_z=\binom dz\frac{(A-1)^z}{A^d},
       \qquad \sum_{z=0}^d w_z=1,\\
 &\sum_{z=0}^d w_z\,
       \frac{\binom qz}{\binom dz}A^{d-z}
   =\sum_{z=0}^d\binom qz\left(\frac{A-1}{A}\right)^z
   \le(2-1/A)^q.
 \end{aligned}
 \tag{E3}
\]

The local-cover overhead and count-profile enumeration contribute the
subexponential factor in E1. Their stored local universes have only
polynomial size. The referenced conversion manuscript proves the
complete construction, off-promise running time, and polynomial-space
accounting.

## 3. One-value arbitrary-cost allocation: exact factor two

Use the model and proof of
`one_value_exact_budget_corank_two_allocation.md`. The original player
matroid M has rank r on its q nonloops. Each resource has the same
positive intrinsic value, but its assignment cost may depend arbitrarily
on its type and recipient. Total assignment cost is at most C>=0.

For an integer full quota K>=2 put b=ceil(K/2). The budgeted fractional
count region is kept on the original player ground, with every resource
rank and cost unchanged. A query on Q is b*1_Q with zero counts outside
Q. The restriction selector asks for an original M-basis contained in
Q. For a forced set Z, the remaining omission budget is

\[
                      |Q|-r=(q-r)-|Z|.
 \tag{E4}
\]

If a full-K basis I* avoids Z, its original allocation remains feasible
in this fixed count region. The weighted omission routine is therefore
a valid extension algorithm. Since

\[
                  \frac{K}{K-\lceil K/2\rceil}\le3
                       \quad(K\ge2),
 \tag{E5}
\]

one may uniformly take A=Gamma(3)=27/4. Gamma is increasing on (1,infty),
as follows by differentiating its logarithm to obtain
`log(R/(R-1))>0`.

A successful fractional b-quota is trimmed to exactly b units at each
selected player. Minimum-cost integral polymatroid intersection on the
full-total partition-cap face recovers an integer b-quota at no larger
cost. This recovery takes polynomial time and has no additive unit
loss. The K=1 case uses the separate exact minimum-cost matroid
intersection gate; if invoked on Q, it simply forbids pairs belonging
to players outside Q. Zero quota is the initialized legal allocation.

Apply the global wrapper to every positive-gap target and retain the
original one-sided integer search. Total target failure excludes an
integer full-K solution; relaxed success is allowed at a nominal K
above the integer optimum. The original external upper bound and
adjacent-grid argument still return quota at least ceil(K*/2).
Consequently the complete algorithm has exact approximation factor two
in

\[
                          \mathcal T_{27/4}(q,H),
                  \qquad 2-\frac4{27}=\frac{50}{27}.
 \tag{E6}
\]

This is an unconditional theorem for all original matroid ranks and
all budgets, not just a result for bounded corank. When all players are
compulsory, the one-value instance was already exactly polynomially
solvable by its fixed-player quota intersection.

## 4. Compulsory two-value arbitrary-cost allocation: exact factor two

Use `two_value_arbitrary_cost_exact_two_allocation.md`. All q players
are compulsory, the two values are 0<u<a, and all type-player costs
are arbitrary nonnegative rationals. There is one exact assignment
budget C. Types with the same value may be aggregated only in a way
that retains their individual assignment costs; the costed pair and
count formulations of the underlying theorem do so.

At a target T<2a, let K=ceil(T/u). Fix a possible number k of large-unit
recipients. The protected light set has size s=q-k. For k<q and K>=2,
use full quota K and output quota b=ceil(K/2). At each Q compute the
minimum cost h_k(Q) of assigning one original large unit to each of k
distinct recipients whose complementary light set lies in Q. Light
labels are allowed only on Q; **all original heavy recipient pairs
remain available**, including those on P\Q.

For a promised full-target allocation, keep one original large unit
at each heavy recipient and remove all other counts there. Its actual
support F* has size k; the complement I*=P\F* is small-only and receives
at least K original small units. If a forced set Z is contained in F*,
then I* remains a valid light set in Q=P\Z and

\[
                  h_k(Q)\le c(H^*),\qquad
             c(x_s^*)\le C-c(H^*)\le C-h_k(Q).
 \tag{E7}
\]

This is the adaptive residual-budget promise at the starting node and
at every surviving child. The extension recursion has omission budget
k-|Z| and A=27/4. At success it uses the attaining minimum-cost heavy
completion and recovers integer b small units by the exact quota
intersection. Heavy value a>T/2 and small value bu>=T/2 give the target
factor two.

Enumerate every k=0,...,q-1, or skip cardinalities whose global minimum
heavy cost already exceeds C. The k=q pure-heavy case is a direct
minimum-cost unit assignment. The K=1 gate is exact one-unit coverage
on the full original instance. For T>=2a, the original fixed-player
budgeted fractional allocation LP followed by cost-preserving largest-
unit rounding gives at least T-a>=T/2 in polynomial time. No global
exponential procedure is needed for these boundary cases.

The original rational value grid and one-sided maximization search
therefore apply without change. Every integer full-target witness has
one of the enumerated support cardinalities. The number of cardinalities
and targets is polynomial, so the complete exact-factor-two algorithm
has time T_(27/4)(q,H), with no condition on affordable-heavy rank or
support size.

## 5. General intrinsic values and arbitrary costs: no support promise

Use `arbitrary_cost_residual_budget_near_two_allocation.md`, with an
original player matroid M of rank r on q nonloops. Values are intrinsic
to resource types, costs are arbitrary nonnegative type-player numbers,
and the one total assignment budget is exact.

Fix R>1, put alpha=1-1/R, and enumerate every distinct light/heavy split
of the intrinsic values, including the empty classes. For one split
and 0<=k<r the protected light set has size

\[
                    s=r-k,\qquad d=q-r+k.
 \tag{E8}
\]

For a target T the full light promise is T and the output fractional
light promise is alpha*T. Their gap ratio is exactly R. The original
completion oracle finds the minimum heavy cost h_k(Q) of an M-basis
completion with r-k light labels in Q and k actual original heavy
assignments. Its weighted matroid-intersection construction retains the
full original M and every heavy pair; only the available light labels
are restricted to Q.

A protected original pair I*,H* has |I*|=r-k. Its complement in P contains
both its k selected heavy recipients and the q-r players outside its
selected original basis. A forced deletion Z contained in that
complement must not be interpreted as forbidding every use of Z:
some of its players may still carry H*. Because the completion oracle
retains all heavy pairs, h_k(P\Z)<=c(H*) and the original full-T light
allocation stays feasible under the residual budget C-h_k(P\Z).
Exactly the invariant E7 holds at every later surviving node.

Thus the adaptive routine is an extension algorithm with time

\[
                     \Gamma(R)^{d-|Z|}\operatorname{poly}(H).
 \tag{E9}
\]

The global conversion bounds every split/k target by
T_(Gamma(R))(q,H), uniformly over d. A saved fractional light allocation
is rounded on the light types alone, preserving its actual assignment
cost and losing at most the largest light unit u_L at each player.
The attaining heavy completion is kept unchanged. Intrinsic values
make the two type classes disjoint, so these allocations share no
resource capacity.

For each fixed split and k retain the original joint benchmark: the
largest original-value-grid T admitting a genuine selected basis,
integral one-heavy-per-recipient assignment, fractional T-service on its
light set, and total cost at most C. This benchmark is downward in T.
The global routine has the same sound failure and relaxed success
interface as the local gap, so the original one-sided grid search still
finds a saved target at least this benchmark. No monotonicity of the
algorithm's successful targets is asserted. Empty light classes and
k=r use the original zero-service and pure-heavy exits.

Now fix any integer optimum and choose the split at

\[
                             \theta^*=\frac{\alpha\,\mathrm{OPT}}2.
 \tag{E10}
\]

Equality belongs to the heavy side. Keep one original heavy unit per
selected heavy recipient and preserve the full original small-only
allocations at the remaining selected players. This gives the required
joint full-OPT witness without increasing cost. Its support k is now
always processed because **every k<=r is enumerated**. At that split,
u_L<theta* and each retained heavy unit has value at least theta*.
The saved fractional light service is at least alpha*OPT, so its
integer recovery gives more than alpha*OPT-theta*=theta* on light
players. The resulting minimum utility is at least theta*.

The number of splits, support cardinalities and target calls is
polynomial. We obtain the unconditional guarantee

\[
 \boxed{\quad
       \text{value}\ge\frac{1-1/R}{2}\,\mathrm{OPT},
       \qquad
       \text{time }\mathcal T_{\Gamma(R)}(q,H),
       \qquad\text{actual cost}\le C.
       \quad}
 \tag{E11}
\]

Zero optimum needs no threshold convention: an arbitrary M-basis with
zero counts is a valid initialized output. The additive fallback in
the parameterized theorem may be omitted here because all support
cardinalities are processed. Alternatively it can be globalized through
its own fixed-region extension interface; running its original raw
Gamma(R)^(q-r) implementation would unnecessarily spoil E11's bound.

There is no corank, heavy-support, price-diversity or proportional-cost
hypothesis in E11. It still requires intrinsic values and one scalar
assignment budget. The theorem does not extend the heavy/light split to
unrelated player-dependent values sharing an original resource type.

## 6. Two-size scheduling: exact three halves on every instance

Use `two_size_makespan_corank_three_halves_transfer.md`. There are q_0
physical machines, small size u and large size a>u. Their total integral
job-polymatroid ranks are f_s,f_b; write h=f_b(P). Let M_b be the
Boolean-cap large-job matroid and P^+ its nonloop set.

If h=0, solve the one-size problem exactly. If rank(M_b)<h, every
schedule puts at least two large units on some machine, so OPT>=2a.
The original fractional scheduling LP and additive-a rounding give a
polynomial-time factor-three-halves schedule. Thus no structural
hypothesis is excluded from the global theorem.

Assume rank(M_b)=h>0 and put q=|P^+|. At a hard target a<=T<2a define

\[
 \begin{aligned}
 C_T&=\lfloor T/u\rfloor,\qquad
      P(g_T)=P(f_s)\cap[0,C_T]^P,\\
 F_T(S)&=C_T|S|+g_T(P\setminus S)-f_s(P),\\
 K_T&=C_T-\left\lfloor\frac{T-a}{u}\right\rfloor,
       \qquad b_T=\lceil K_T/2\rceil.
 \end{aligned}
 \tag{E12}
\]

The retained-rank test g_T(P)=f_s(P) is performed first. Failure proves
target infeasibility. The dual F_T is constructed on the **full physical
machine set P**, and only then restricted to the candidate player ground
P^+. A target-T schedule promises K_T*1_(I*) in P(F_T) on its h-element
large-position basis I*.

For a forced set Z subseteq P^+, start the quota gap with large positions
Q=P^+\Z and fixed player rank h. Do not remove Z from the physical
machine ground, re-dualize the small resource, or contract its capacity.
If I* avoids Z, its full-K_T promise remains valid in the same F_T.
The remaining omission count is q-h-|Z|. For K_T>=2, the quota ratio
is at most three, so A=27/4; K_T=1 has its exact matroid-intersection
gate. This verifies the forced-omission interface.

At success, zero-extend b_T*1_I to every physical machine and complete
it to an integral base y of F_T. The count bases
`x_b=1_I` and `x_s=C_T*1-y` schedule all original units. No small-job
rounding is used. Their load is at most T on machines outside I and
at most 3T/2 on I, by the original integer deficit calculation. This
completion may use small-job capacity on omitted large positions and
on machines never eligible for a large job, as required.

Targets T<a fail, while T>=2a use the polynomial additive-a branch.
The original common-size grid and one-sided minimization maintain a
failed lower bound and an actual saved successful schedule. Sound full-
target failures imply the final successful target is at most OPT; hence
the recorded makespan is at most 3OPT/2.

The complete time is T_(27/4)(|P^+|,H), and in particular at most the
same whole-machine bound with q_0 replacing |P^+|. This is a statement
about the explicit machine ground. It does not replace a binary number
of expanded job slots by q_0 in a slot-based global conversion.

## 7. Selected concurrent flow and explicit robust scenarios

Use `selected_multicommodity_flow_corank_scheme.md`. The network and all
capacities are fixed. There are q candidate commodities with distinct
terminals and positive demand scales. A polynomial restriction selector
chooses an actual permitted r-set, with r>=1. Routing is splittable;
explicit nonnegative routing budget rows, including several such rows,
are enforced exactly. The permitted family can be a matroid basis or
two common bases, with one selection-cost constraint when the stated
restriction selector is supplied by weighted matroid intersection.

At full target T and output target alpha*T, alpha=1-1/R, the gap queries
the original normalized service region at alpha*T*1_Q. Every forbidden
commodity has zero service; the physical network, its capacities and
its routing budgets are unchanged. A full-T permitted set I* avoiding
forced Z remains feasible. The restriction selector on Q=P\Z has
required cardinality r and remaining omission budget q-r-|Z|. Thus the
weighted gap is an extension routine with A=Gamma(R).

Replace each fixed-target gap by the global wrapper. For each genuine
selected set I, its optimum common rate is an attained rational LP
optimum with a uniform polynomial-bit denominator bound. The existing
rational-comparator search, followed by exact reoptimization of the
saved actual selected set, consequently gives the full factor alpha,
with no extra accuracy loss. The fixed-set reoptimization uses the
original LP, not the artificial fine-grid target witness. We obtain

\[
              \text{rate}\ge(1-1/R)\,\mathrm{OPT}
                 \quad\text{in }\mathcal T_{\Gamma(R)}(q,H)
                 \text{ time}.
 \tag{E13}
\]

All capacities, routing budgets and selection conditions remain exact.
Zero optimum and an empty permitted family are handled by the original
initial selector check; a zero-rate witness needs no positive starting
guess. Rank-zero selection is returned separately.

For a nonempty explicit finite scenario list, use
`robust_scenario_selected_flow_corank.md`. The same selected set and
rate must work in every scenario; its routing may depend on the
scenario. Membership is tested in the intersection of the scenario
regions. A row violated in any scenario is valid for the intersection,
and all original full-target scenario flows survive a forced omission
avoided by I*. The same time E13 applies with H counting the complete
scenario list. It does not assert a separation oracle for exponentially
many implicitly specified scenarios or enforce unstated coupling
between their route choices.

## 8. One shared setup and routing budget

The extension in `shared_setup_routing_budget_corank_flow.md` has a
nonnegative setup fee sigma_i for every selected commodity and a single
combined budget

\[
              \sum_{i\in I}\sigma_i+
                         \text{actual routing cost}\le C.
 \tag{E14}
\]

Its family must admit an exact minimum-setup restriction optimizer,
which returns h(Q)=min_{I subseteq Q} sum_(i in I) sigma_i and an
attaining I_Q. A restriction feasibility selector alone is insufficient.
One or two matroid bases supply the required optimizer; an additional
unrelated exact selection-cost constraint is not automatically allowed.

At Q the gap queries light service using routing budget C-h(Q). If a
full witness I* avoids forced Z, then h(Q)<=sum_(i in I*)sigma_i, so
its full original routing is feasible in the current residual region.
Every surviving child repeats the same inequality. At success the
algorithm takes the attaining I_Q and restricts the reconstructed flows
to it, making the actual combined cost at most C. The same adaptive
extension bound Gamma(R)^(q-r-|Z|) therefore holds.

Globalization and exact fixed-set rational reoptimization prove E13
with this combined budget also exact. Additional fixed nonnegative
routing-only budgets remain safe. First test h(P)<=C; otherwise no
selected set is legal even at zero routing. This initial feasibility
test must not be replaced by a free zero-rate output. Several unrelated
setup objectives or selection-dependent network capacities need another
argument and are not included.

## 9. Explicit constant tradeoffs and accuracy encoding

For integer R>=2 the needed constant A=Gamma(R) is rational. The same
whole-ground base yields two different application guarantees:

| R | A=Gamma(R) | Base 2-1/A | Intrinsic allocation factor | Selected-flow rate fraction |
| --- | --- | --- | --- | --- |
| 2 | 4 | 7/4=1.75 | 4 | 1/2 |
| 3 | 27/4 | 50/27 approximately 1.851852 | 3 | 2/3 |
| 5 | 3125/256 | 5994/3125=1.91808 | 5/2 | 4/5 |

The exact half-quota allocation and two-size scheduling guarantees use
A=27/4 but have their separately proved factors two and three halves;
they are stronger than substituting R=3 into the generic intrinsic
rounding formula.

For any fixed rational eta>0, choose R=(2+eta)/eta. Then E11 has factor
2+eta and base `2-1/Gamma((2+eta)/eta)`. Alternatively an integer
R>=max{2,ceil(1+2/eta)} gives factor at most 2+eta and the rational
constant table formula. These are strictly sub-two bases for every
fixed positive accuracy loss, and converge to two as eta tends to zero.

For a fixed rational R=a/b>1, the block comparisons are exact because

\[
                  \Gamma(R)^b=
                     \frac{a^a}{b^b(a-b)^{a-b}}.
 \tag{E15}
\]

Raising a positive comparison to its fixed denominator b therefore
reduces it to rational arithmetic. This is not an implicit
transcendental-number oracle.

If R is a varying binary input, the claimed polynomial factors must
not hide expansion of integers of length proportional to its numerical
value. The safe supplied rational A=3R>Gamma(R) gives the uniform
version of E1 with base `2-1/(3R)`, with the encoding of R included in
H. The sharper Gamma-base displays above are fixed-accuracy statements,
or require a separately supplied and paid certified numerical bound.

## 10. Balanced hidden-subset oracle barriers

The accepted lower-bound constructions now give a global time boundary,
in addition to their parameterized corank interpretation. Let q=2r>=4
and hide one r-element set A in the resource rank

\[
      f_A(S)=\min\{2|S|,2r\}-{\bf1}[|S|=r]+{\bf1}[S=A].
 \tag{E16}
\]

Its normalized, monotone, integral submodularity is proved in
`recipient_polymatroid_below_two_oracle_barrier.md`. Values need only
O(log q) bits. Relative to the common baseline with the final indicator
removed, only the query A has a different answer.

**One-value optional allocation.** Choose the original player matroid
U_(r,q), one resource of value one, all assignment costs zero and C=0.
The optimum is two on hidden basis A. Any integer allocation with value
strictly greater than one on an r-element selected basis I forces
f_A(I)>=2r, hence I=A. Every approximation factor strictly below two
must therefore identify A.

**Compulsory two-value allocation.** Keep the small value-one resource
f_A and add a value-two heavy resource with recipient matroid U_(r,q).
Every player is compulsory, and costs remain zero. Give two small units
to A and one heavy unit to its complement to obtain optimum two. An
output with minimum value above one must serve every small-only player
with at least two small units. Since the small total rank is 2r and
at most r players receive a heavy unit, exactly r players must be
small-only and their set must have f_A-value 2r. This set is A.

**Two-size scheduling.** Take r size-two jobs governed by U_(r,q) and
small size-one jobs governed by

\[
                         g_A(S)=2|S|+f_A(P\setminus S)-2r.
 \tag{E17}
\]

The optimum makespan is two: put the large units on A and two small
units on each other machine. Every approximation factor strictly below
three halves has integer makespan at most two, so each large recipient
gets no small units. Complement-base duality forces its large-recipient
set to be A. The exceptional small-rank query is P\A. All q machines
are eligible large positions, and q>=r+2 holds.

Until the exceptional query, one deterministic transcript is consistent
with every still-hidden set. If two possible hidden r-sets remain,
one output cannot identify both. Therefore each respective problem
requires at least

\[
              \binom q{q/2}-1
                    =2^{q-O(\log q)}
 \tag{E18}
\]

oracle queries for the strictly better approximation factor. In
particular, for any fixed delta>0 there is no deterministic
`(2-delta)^q poly(H)` algorithm achieving factor strictly below two
for these allocation models, or strictly below three halves for this
scheduling model, uniformly in the full rank-value-oracle model.

This supplies a qualitative all-instance approximation threshold:
the threshold factors are attained at base 50/27<2, whereas every
strictly better factor has the nearly-2^q oracle barrier. It does not
prove optimality of the base 50/27 at the threshold factor. The
obstruction is black-box and does not apply automatically to ordinary
explicit item or job eligibility lists, nor to a succinct representation
that exposes the hidden set. No flow analogue is inferred here.

## 11. Public baseline attribution and interpretation

Fomin, Gaspers, Lokshtanov and Saurabh's
[*Exact Algorithms via Monotone Local Search*](https://arxiv.org/abs/1512.01621)
(STOC 2016; [author journal manuscript](https://sites.cs.ucsb.edu/~daniello/papers/monotoneLocalSearch19.pdf))
already gives the deterministic base `2-1/A` from an `A^k` extension
routine. Its inclusion-family theorem and permissive-extension
discussion explain the public context. Our full-target/relaxed-target
formulation is proved directly by preserving one witness, so it does
not silently identify two different target families. The author's
Section 4 discusses a subexponential-space cost for its presented
derandomization. Polynomial space here is independently proved by the
streamed logarithmic-block representation.

The allocation comparisons remain model- and time-specific.
[*Cost Preserving Dependent Rounding for Allocation Problems*,
ICALP 2025](https://doi.org/10.4230/LIPIcs.ICALP.2025.127), Theorem 3,
provides a randomized polynomial logarithmic approximation for ordinary
Budgeted Santa Claus with intrinsic values and arbitrary costs.
Its cost-preserving additive rounding is public background. E6 and
E11 give stronger multiplicative guarantees in exponential time, while
also allowing the recipient-polymatroid and player-selection model
specified above. They are not unconditional polynomial-time constant
approximations.

The two-size scheduling comparison uses the public fractional
job-polymatroid relaxation and additive-largest-job rounding of
[Bamas et al., arXiv:2307.08453v1](https://arxiv.org/html/2307.08453v1),
Theorem 23, in its easy branch. The exact three-halves hard branch and
its extension interface are proved in the internal scheduling
manuscript. No priority claim against all specialized ordinary
restricted-assignment algorithms is made.

For a specified commodity set, the continuous routing problem remains
a standard rational LP. The source discussion and bounded primary
comparison for selected flow are in the original flow manuscript;
the whole-ground transfer here applies its reviewed packing separator
and exact rational reoptimization. For these continuous selected-flow
problems, direct enumeration of all permitted sets followed by exact
fixed-set LP optimization is a `2^q poly(H)` baseline, whereas the
displayed relative-loss algorithms have a strictly smaller base for
fixed accuracy. This comparison concerns the explicit selected ground and
does not turn splittable flow into an integral routing theorem.

No exhaustive publication-priority claim, formal verification or
external peer review is asserted. The source of the time formula,
the separately proved extension interfaces, and the scope of every
oracle lower bound are kept distinct.

## 12. Review checklist for this application manuscript

The substantive gates for a full independent read are: keeping all
original heavy copies after forced light omissions; keeping the full
physical machine ground when dualizing and completing small jobs;
paying every support cardinality and off-promise extension within E1;
retaining the original one-sided and exact-rational target searches;
preserving the actual cost of the attaining completion; omitting or
globalizing any optional raw-corank fallback that could spoil the new
time; and restricting E18 to its deterministic full-oracle models.

The individual allocation, scheduling, adaptive-gap, rounding and flow
primitives have separate internal proofs and audits. This manuscript
submits their global composition for a fresh root and independent read.


---

**Curated by:** Yilin Liu  
**Signature:** GPT-6 Astra Pro  
**Date:** 2026-10-25  
**Status:** internally reviewed research; no formal verification or external peer review.
