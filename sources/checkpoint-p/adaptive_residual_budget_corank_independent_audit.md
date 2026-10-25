# Independent audit of omission with a changing residual budget

**25 October 2026. Full independent review of RB1--RB12.**

Reviewed manuscript: `adaptive_residual_budget_corank_gap.md`.
The changing-region lemma passes. Its proof reestablishes the
needed promise at every visited ground rather than assuming the
old fixed-packing-region theorem applies unchanged. The same
first-crossing combinatorics then gives Gamma(R)^c time on all
inputs and polynomial workspace.

This audit concentrated on possible failures caused by replacing
one global budgeted region with a new residual budget after each
omission. No substantive counterexample or missing invariant was
found under the stated exact interfaces.

## 1. The original paired witness is the correct invariant

A full-target witness consists of one fixed admissible pair
(I*,W*) and its service allocation with cost at most C-h(W*).
The set I* has the same required cardinality s at every node.
It is not a witness chosen anew according to the node's cheapest
completion.

If I* remains inside the current allowed ground Q, that same
pair is one of the candidates in the definition of h(Q). Hence
h(Q)<=h(W*). The current residual budget C-h(Q) is at least the
budget used by the original service witness. Budget monotonicity
therefore proves t*1_I* belongs to the current U_(C-h(Q)).

This argument remains true after deleting any subset disjoint
from I*. Even if the newly cheapest completion changes or its
price rises, W* remains admissible because I* still lies inside
the new ground. Its fixed cost again bounds the new minimum
from above. There is no cumulative loss in the residual budget
available to the protected original witness.

For the heavy/light application, this requires restricting only
the light candidate set: all original eligible heavy pairs must
remain available to the completion oracle. Deleting heavy pairs
merely because their player was removed as a light candidate
could destroy W*. The stated admissible relation and its intended
two-matroid implementation retain those pairs.

## 2. Success combines two compatible witnesses within one budget

The completion oracle returns an attaining pair (I_Q,W_Q), with
I_Q subseteq Q and h(W_Q)=h(Q). A successful test serves every
member of Q at level b using cost at most C-h(Q). Restricting
that service allocation to I_Q preserves its required service and
cannot increase cost. Adding W_Q gives total cost at most C.

This is stronger than separately checking that some completion
and some light set are affordable. Membership is tested on the
entire current Q, so it also serves the particular I_Q that
attains the minimum completion cost. Thus the proof does not need
the cheapest completion to use the same selected set as an
independently optimized service allocation.

Attainment and exactness both matter. A numerical lower bound
on completion cost without a corresponding pair would not
justify the output. An approximate minimum that is more expensive
than W* could reduce the residual budget below the protected
witness's needs. The manuscript explicitly requires an attaining
exact minimum and polynomial witness reconstruction.

## 3. A current row still forces a protected deletion certificate

At a node containing I*, the separator's row a*z<=u is valid
for the current region and hence for t*1_I*. It is strictly
violated by b*1_Q. With D*=Q\I*, d=|D*| and W=a(Q),

\[
       t a(I^*)\le u<bW,
       \qquad a(D^*)>\left(1-\frac bt\right)W=\frac WR.
\]

Nonnegativity is used in the ordered-weight layer-cake argument.
It forces a prefix of Q whose D*-density exceeds 1/R. Take the
first such prefix. Its binary indicator word is one of the
algorithm's enumerated first-crossing certificates; all its
one-positions are in D*. Deleting them preserves the fixed I*.

The row need not remain a complete description, or the only
useful row, after this deletion. The child recomputes its
completion minimum and its own separator. The paired-witness
argument in Section 1 supplies the same full target there.
Induction on d therefore closes the changing-region interface
without importing a fixed-region assumption.

If d=0 and I* is still present, Q=I*. The current region contains
t*1_Q, so its downward closure contains b*1_Q. Thus a protected
branch cannot reject at zero deficit. The other initial rejection
cases are also impossible on such a branch: the original pair
shows that a completion exists and h(Q)<=h(W*)<=C.

## 4. Nestedness is valid but is not used as a substitute for the promise

For Q' subseteq Q, minimizing over fewer admissible pairs gives
h(Q')>=h(Q), when both minima exist. Thus the residual service
regions shrink under deletion. This observation alone would not
prove that the original optimum remains feasible inside them.
RB8--RB9 provide the missing comparison to the fixed h(W*), and
are the actual reason the promise survives.

This also explains the algorithm's choice to recompute all node
data. Its correctness is not based on keeping a stale residual
budget, reusing a nonattaining lower bound, or assuming membership
in an arbitrary changing family of regions.

## 5. The complete first-crossing runtime is unaffected

For fixed R and deficit d, first-crossing words form a prefix-free
family. The Bernoulli counting proof gives
sum_C Gamma(R)^(-|C|)<=1 independently of where the nonnegative
coefficient ordering came from. The explicit bounded-ones/zeros
enumerator likewise visits at most (q+1)Gamma(R)^d local states,
including unfinished paths.

Neither statement needs a full-target witness or a common region
across nodes. It only needs the current finite ordering, the
fixed ratio R, and the cap |C|<=d. They therefore apply at every
unpromised node as well.

Every attempted child has smaller nonnegative deficit d-|C|.
A failed completion call or a negative residual-budget rejection
still incurs paid polynomial work and is counted as a terminal
child in the recurrence. Consequently

\[
 T(d)\le P(H)\Gamma(R)^d+\sum_C T(d-|C|)
       \le P'(H)(d+1)\Gamma(R)^d.
\]

The induction uses |C|>=1 and the prefix-free branch sum. It
does not assume that the input has a protected witness. This
proves the asserted all-input running time, rather than only
termination on YES instances.

## 6. Changing the budget does not create growing coefficient descriptions

The minimum-cost oracle is required to return polynomial-bit
costs and witnesses uniformly over allowed grounds. In the
allocation implementation, each h(Q) is a sum of costs of at
most k original heavy player-type assignments. Thus its rational
encoding, and that of C-h(Q), is bounded from the original
input independently of the depth or number of visited nodes.

The budgeted service support LP uses this fresh residual budget
as one right side. Its other coefficients are the original
recipient ranks, values and costs. The previously proved
uniform vertex and separator bit bounds therefore remain
polynomial. No previously generated row or rational error is
recursively substituted into the next completion optimization.

The omission depth is at most c<=q. Each paused certificate
enumerator stores a polynomial-length word and polynomial-bit
data, and each exact oracle uses polynomial workspace. The
changing residual budget does not alter the polynomial-space
conclusion.

## 7. The scalar and resource-separation boundaries are necessary

One scalar minimum is simultaneously no greater than the cost
of any protected completion and attained by the completion used
at success. Several coordinatewise minima need not be attained
by one completion, so the argument does not automatically preserve
several unrelated shared budgets. The explicit scalar-budget
restriction is correct.

The completion and service resource constraints must also be
compatible in the way assumed by the interface. In the intrinsic-
value heavy/light application, they involve disjoint collections
of resource types, and the remaining coupling is the original
player-basis relation plus the scalar cost. A cheaper heavy
completion does not consume any light resource capacity.

If a single original resource could be heavy for one recipient
and light for another, changing the completion could alter the
capacity available to the protected service allocation. The
budget comparison alone would then be insufficient. The
manuscript expressly excludes that unsupported extension.

Likewise, an exact restriction selector that merely decides
admissibility is not automatically an exact minimum-completion-
cost optimizer. Concrete applications must establish the stronger
oracle, which weighted matroid intersection supplies in the
stated heavy/light construction.

The RB lemma therefore removes the price-profile and proportional-
cost assumptions for the stated scalar-budget, disjoint-resource
application. Its proof remains conditional on the explicit
minimum-cost completion and nonnegative service-separation
interfaces; it is not a general claim about arbitrary adaptive
packing systems.
