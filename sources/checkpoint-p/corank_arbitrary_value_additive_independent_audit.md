# Independent audit: arbitrary-value corank allocation with one-unit additive loss

**25 October 2026. Full independent review of V1--V19 passed.**

Reviewed manuscript:
`corank_arbitrary_value_additive_allocation.md`.
Dependencies independently checked here are the batch quota
interface, the two explicit integral-polymatroid intersections,
complement duality and prefix rounding, target-search orientation,
and all parameter/bit/scope claims. This audit is mathematical
review, not a claim of formal verification or of implemented code.

## 1. Accepted theorem and its exact scope

The manuscript proves an allocation value at least

\[
                    \max\{0,(1-\epsilon)\mathrm{OPT}-u\}
\]

in time Gamma(1/epsilon)^c poly(H), using polynomial workspace.
Here c is the player-matroid corank after deleting loops, values
are common intrinsic values per type, every recipient type is an
integral polymatroid, and unused resource units are permitted.

Fixed per-player/per-type upper caps are absorbed into the recipient
polymatroids before the algorithm. General constraints coupling
types at one player are not supported. The current statement
correctly excludes those constraints and player-dependent values.
Its small-unit multiplicative corollary retains the explicit
condition on u/OPT, so it does not contradict the strict-below-two
oracle lower bound for arbitrary integer unit allocation.

## 2. Loop deletion and exact quota engineering

Deleting player loops preserves all bases and preserves the
allocation optimum: restrict any original feasible allocation to
the remaining ground, and conversely extend any restricted
allocation by zero. Monotonicity of each original recipient rank
validates that extension for every original subset inequality.
Discarding zero-value and zero-rank types is harmless. The empty
resource and rank-zero player cases are explicitly separated.

Writing 1-epsilon=B/A with A>B>=1 and Delta=g/A is sufficient to
make every multiplier m_j=A(v_j/g), every promise quota t=Ak, and
every output quota b=Bk integral. The strict gap is present even at
the first positive target k=1. In particular, no hidden invocation
at t=b is needed. The exact ratio is

\[
                            t/(t-b)=1/\epsilon.
\]

Summing the original recipient inequalities proves that an integer
allocation's workload lies in P(F). If every selected player has
value at least T, downward closure yields t*1_I in P(F). Thus every
batch failure is a sound certificate against the original target.

## 3. Base extension and explicit scaled decomposition

The workload vector b*1_I is first restored to the fixed ground and
extended coordinatewise to an integer base w of F. At most q
coordinate saturations suffice. Once a coordinate is blocked by a
tight set, further nonnegative feasible increments cannot unblock
it. At the end all coordinates are saturated; the usual tight-set
union argument, or maximality in a polymatroid, proves total rank.
The maximum increment is obtained by one submodular minimization
with that coordinate forced into the queried subset. Its numerical
size does not determine the number of updates.

The decomposition on E=P times J is correct. Its first rank is the
direct sum of m_j f_j. Its second rank is the partition-capacity
polymatroid with row capacity w_p. For an arbitrary S subseteq E,
the players whose entire type row lies in S are exactly
R=intersection_j S_j. Therefore

\[
 \mathcal B(E\setminus S)=w(P)-w(R),\qquad
 \mathcal A(S)\ge F(R)\ge w(R).
\]

This proves every required intersection min-max inequality. A
maximum common integer vector has total w(P). Equality in the
sum of all type upper totals forces each z_j to be a base of
m_j f_j; equality in the sum of player capacities forces each row
sum to equal w_p. Dividing z_j by m_j gives fractional original
bases, and the workload identity is exact. No divisibility of z_j
by m_j is assumed.

The construction uses q times the number of types as its ground
size. This is an actual compressed implementation of the
decomposition interface, not an implicit expansion into m_j copies.

## 4. Complement duality and the lower-rounding lemma

For a_j(p)=f_j({p}), the complement rank

\[
               f_j^\#(S)=a_j(S)+f_j(P\setminus S)-f_j(P)
\]

is monotone because a singleton marginal of a normalized
submodular function is an upper bound on every later marginal.
Its singleton values are at most a_j(p). These observations verify
nonnegativity of both complement maps. The base equality and
complement-set inequalities prove the forward and inverse maps
between B(f_j) and B(f_j^#). In particular, the proof does not
assume that the entire singleton-cap vector is resource feasible.

The prefix-capacity polymatroid used in upper rounding is valid.
For each player, its rank on a set of type indices is the maximum
prefix cap C_(p,k) represented in that set. Nondecreasing prefix
caps make its inequalities equivalent to all prefix upper bounds:
an arbitrary subset is dominated by the prefix ending at its
largest index, and a full prefix has exactly its designated cap.
A nonnegative maximum-weight rank is submodular.

The original fractional dual bases satisfy the prefix ceilings and
have the full direct-sum total. Integral polymatroid intersection
therefore provides a common integer vector with that same total.
Every dual component is a base. With values sorted in descending
order, summation by parts bounds each player's rounded dual value
by the original value plus
sum_k(v_k-v_(k+1))=u. Complementing back proves the desired lower
bound separately at every player. The argument remains correct
with repeated values, zero dual ranks, or zero player capacities.

This rounding is independently established by the manuscript's
proof. The primary public comparison is also accurate: Bamas et
al., arXiv:2307.08453v1, Theorem 21 states the largest-unit additive
allocation guarantee for a fractional assignment. I opened and
checked that theorem and its surrounding proof directly:
<https://arxiv.org/html/2307.08453v1>.
No reliance on the corrected DRZ local-search analysis is used.

## 5. Reconstruction and target search

Every selected player has fractional original value at least
(1-epsilon)T, hence integer value at least (1-epsilon)T-u after
rounding. Deleting counts outside the selected basis preserves
recipient independence and leaves selected values unchanged.
The note correctly distinguishes this independent-vector output
from a stronger, unsupported requirement that all original resource
bases be assigned only within the selected basis.

All integer utilities and the attained optimum lie on the g-grid.
The total value V is a valid upper bound because the selected rank
is positive. Therefore V+g is an external strict upper certificate;
the algorithm need not force the weaker gap procedure to reject it.
The maintained lower endpoint is a successful target and the upper
endpoint is certified above OPT. At adjacency, integrality gives
L>=OPT. This is the correct direction for a max-min objective, and
the saved allocation then proves the theorem. Algorithmic success
need not be monotone.

## 6. Binary cost and small-unit consequence

All multiplier and quota bit lengths are polynomial in the original
input and accuracy encoding. Both intersection grounds are
polynomial in q and the number of types. Prefix sums of the
rational x_j and y_j may use products of input denominators, but
the bit length of such a product is only the sum of polynomially
many polynomial bit lengths. No primitive runs once per resource
copy or workload unit.

The batch count includes attempted deletions rejected by a rank
test on unpromised targets. Polynomial-time deterministic oracle
primitives, depth-first traversal, and a polynomial number of
target calls preserve the stated time and workspace. The analytic
Gamma expression is not evaluated in the implementation.

Under u<=eta OPT and epsilon=eta, the bound becomes
(1-2eta)OPT. Substituting eta=delta/(2(1+delta)) gives exactly
OPT/(1+delta) and time (O(1+delta^-1))^c poly(H). The condition is
stated as an instance hypothesis, not as something the algorithm
must know or certify. Every claim in V1--V19 survives this audit.

## 7. Optional refinement, separate from acceptance

The largest-value additive term can be sharpened in the rounding
lemma without changing the algorithm. If f_j^#(P)=0, its entire
dual base is zero, both before and after rounding, so type j causes
no rounding loss. Thus the global u may be replaced by the largest
v_j among types with positive complement total rank, with value
zero if there are none. Positive complement total rank is
equivalent to nonmodularity of f_j on the fixed ground: total
singleton rank equals total rank precisely in the modular case.

More locally, player p incurs loss at most the largest v_j for
which f_j^#({p})>0. Types with zero such singleton are forced to
zero in that player's dual assignment. Before the first type with
positive dual singleton, all corresponding prefix sums and their
ceilings are zero; the same telescoping calculation begins at that
type and yields its value as the additive bound.

These are optional refinements of the proved rounding statement.
They are not needed for the main theorem's validity and have not
been substituted into its headline in this audit.
