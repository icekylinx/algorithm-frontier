# Independent audit of attained-set testing and sparse-separator time bases

**25 October 2026. Fresh full read by the transfer-frontier researcher of
`attained_set_sparse_separator_gap.md`, Sections 1--8 and S1--S8. Internal
mathematical audit, not formal verification or external review.**

The refinement passes. The finite certificate polynomial gives the claimed
smaller width-dependent base, and the backward reachability table removes
the local enumeration cost that would otherwise invalidate that base.
The only requested clarification was to apply the global block wrapper
when beta>1; the author has added it, with beta=1 handled directly by
the polynomial recursion bound.

## 1. Testing an attained candidate requires complete recovery

The first interface condition is substantive. If weak service on the
tested set L_Q already gives a complete legal solution, there is no need
to demand that service on all of Q. This applies to a fixed-family
restriction selector, and to the light set of a pair attaining the
minimum completion cost in the residual-budget theorem.

The protected full set I* need not equal that attained set. For a
nonnegative row violated by b*1_(L_Q), validity of the full t*1_(I*)
implies

\[
 a(L_Q\setminus I^*)
     \ge a(L_Q)-a(I^*)
     \ge a(L_Q)-U/t
     >a(L_Q)/R.
\]

Every coordinate selected for a deletion certificate can therefore be
confined to L_Q while still avoiding I*. The attaining candidate and
the row may change after each deletion; the same inequality is simply
reproved from the unchanged protected witness at its next node.

The manuscript correctly does not substitute an arbitrary subset in the
joint-role compulsory allocation algorithm. That model must still serve
the other current light players, so candidate-only service there lacks
the required complete recovery. This distinction is retained throughout
the statement and examples.

## 2. The finite first-crossing family is counted correctly

A certificate is a binary word whose last bit creates its first strict
crossing `R*ones > length`. Every proper prefix is noncrossing. Sorting
only positive row coefficients on L_Q is valid: zero coefficients
contribute neither useful omitted mass nor any necessity for a prefix.
A failed query cannot have zero positive width because its row capacity
is nonnegative.

Dynamic programming by prefix length and number of ones counts precisely
these words. Noncrossing states propagate zeros or ones; a crossing one
increments its coefficient N_l and is not extended. Integers are at most
2^w, so their bit length is polynomial. Rational threshold comparisons
are exact cross multiplication.

I independently enumerated the displayed examples. For R=3, width four
has words `1`, `01`, `0011`, hence coefficients N_1=2 and N_2=1. Width
five adds `00011` and `00101`, and length six cannot be a first crossing.
For R=2, width three has exactly `1` and `011`. These produce the stated
branching polynomials and constants.

## 3. The root beta and its strict comparison with Gamma

There is always the word `1`, so the positive coefficient sum at beta=1
is at least one. If it equals one, that is the only certificate and the
root is beta=1. Otherwise the sum of N_l*beta^(-l) is continuous and
strictly decreasing from above one to zero, giving a unique root >1.

A first-crossing word with l ones and z zeros has z<(R-1)l. Under
independent bits of one-probability 1/R, its probability is strictly
larger than Gamma(R)^(-l). The finite certificate words form a prefix-
free family, so their probabilities sum to at most one. Consequently
the branching polynomial is strictly below one at Gamma(R), and its
root beta is strictly smaller. This proof is valid for every finite
width; it does not give a uniform gap when the width is unbounded.

## 4. Reachability pruning removes dead-word overhead

The old unrestricted rectangle enumerator could cost Gamma(R)^d even
when the emitted sparse family has a smaller branching polynomial. The
new backward table is needed to avoid that error.

For every noncrossing state (m,k), whether a permitted future crossing
exists depends only on m,k, the width bound and the remaining total
one budget. Earlier history causes no additional condition because the
DFS has already verified that every earlier prefix is noncrossing.
Crossing states are terminal, noncrossing maximum-length states fail,
and other states use the disjunction of their allowed children. This
computes exact reachability in polynomial time and space.

The pruned DFS explores only prefixes with an output descendant.
Every explored nonroot node therefore belongs to at least one
root-to-output path. The total number of such nodes is at most the
sum of output path lengths, at most w_Q times the number of actual
certificates. The per-node preprocessing and the work per emitted
attempted child are polynomial. No hidden unrestricted Gamma^d
enumeration remains.

The omitted element set also identifies its certificate word uniquely:
the last omitted index is the terminating position, and all earlier
indices determine the preceding bits. Counting duplicates would only
overestimate time, but none are needed in this enumeration.

## 5. The complete recurrence includes failed children and beta=1

Each l-one certificate decreases the omission budget by l and has at
most N_l(R,w) possible words under the uniform width hypothesis. Every
attempt is charged, including a child rejected immediately by the
selector, current-region feasibility check, or another paid gate.

The local cost is polynomial preprocessing plus polynomial cost per
attempted child. Starting from the literal recurrence with an extra
entry charge for each child, replacing T by T+P gives the stated
recurrence after a constant enlargement of P. The induction

\[
                  T(d)\le P(H)(d+1)\beta^d
\]

then uses only the truncated branching sum at beta, which is at most
one. The d=0 base has no children. For beta=1 there is only the one
certificate word, so at most one child continues at each node and the
bound is polynomial. It is unnecessary and outside the A>1 conversion
interface to globalize that case.

The width guarantee must hold for all failed rows on every input,
including off-promise branches and forced-omission starts. The
manuscript explicitly requires this uniform condition. Polynomial
space follows from polynomial tables and words at depth at most the
original omission budget; storing one such table per paused level is
still polynomial.

## 6. The concrete global constants and sparse packing application

For R=3,w=4, the root of `2/beta+1/beta^2=1` is 1+sqrt(2). The
global base is exactly 3-sqrt(2). For R=2,w=3, the root of
`1/beta+1/beta^2=1` is the golden ratio, and the global base is
(5-sqrt(5))/2. These are fixed quadratic constants, so exact local
cover comparisons can use their algebraic representations. The
author's new beta>1 sentence correctly restricts this conversion.

For the explicit common-base application, a minimum-cost common basis
inside Q supplies the restriction selector under the original exact
selection-cost threshold. Test that basis against the capacities 2u.
An original feasible basis I* satisfies `2*a(I*)<=2u`, while a violated
weak candidate has `a(L_Q)>2u`, giving full quota two, weak quota one,
and R=2. Each original row has at most three positive entries, so the
tested positive width is at most three on every possible branch.
The golden-ratio recurrence therefore applies directly.

Recovery returns that actual common basis with every capacity at most
twice its original value and the exact selection-cost threshold. No
rounding or additional matroid intersection is hidden. The existing
one-sided cost minimization may optimize the threshold with the same
original-feasibility promise and augmented-capacity output semantics.

## 7. Scope of the improvement

The result is an actual improvement when the returned separators have
a proved width bound. Sparse inequalities in an unprojected LP do not
automatically produce sparse projected utility or routing separators;
the manuscript correctly excludes that inference. Attained-set testing
can bound width by a selected-set cardinality, but an unbounded such
cardinality is not a fixed improved constant.

Thus this refinement does not settle the unrestricted three-unit to
two-unit promise problem or improve the dense-row universal base by
a fixed amount. Its explicit sparse weighted common-base example and
its general tested-set interface match the proof. No substantive gap
was found after the beta=1 clarification.
