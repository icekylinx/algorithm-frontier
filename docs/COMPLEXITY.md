# Complexity and computational models

Every result card states its output, objective, time, space, parameters,
representation and lower-bound scope. The linked theorem fixes all quantifiers
and exceptional cases. Similar notation in two families does not identify
their computational models.

## Input size and charged operations

| Symbol or convention | Meaning |
|---|---|
| $H$ | The complete binary input and the polynomial work charged to explicitly named oracle or optimization primitives. The local theorem specifies those primitives. |
| $H_\varepsilon$ | $H$ plus the complete binary encoding of the supplied rational accuracy. |
| $n,m$ | Vertices and edge records in graph problems, unless the local statement says otherwise. |
| $N$ | A declared finite graph or numerical cap; initialization, lifetime and restart conventions belong to the theorem. |
| $T$ | A numeric target or sum of targets, not its bit length. |
| $Q$ | In the numeric-target family, the number of distinct nonempty eligible-column support patterns. |
| $q,r,c$ | Typically explicit ground size, selected rank and corank. Local definitions take precedence. |
| $\operatorname{poly}(H)$ | A polynomial in encoded input size and paid primitive work, not a polynomial in a binary-encoded numeric capacity. |
| $O^*(f)$ | Suppresses the polynomial factors explicitly identified in that manuscript. It does not suppress a second exponential parameter. |

A conceptual unit expansion can prove integrality without providing a valid
implementation on binary capacities. An executable algorithm must account for
compressed records, rank evaluations, optimization calls, rational arithmetic,
workspace and witness recovery. Mandatory resource bases keep their original
total after restrictions or lifts.

An original rank oracle, a readable rank circuit, a represented matroid and
an explicit graph are different inputs. A theorem using a completion or
weighted-optimization oracle must name it; a rank-only theorem does not
silently provide that operation.

## Guarantees and comparators

An approximation ratio is measured against the precise comparator in its
statement. Integer optimum, configuration-LP optimum and a fractional
assignment optimum on an actual selected basis are distinct. A fractional
comparator does not mix selected bases unless its definition permits this.

An additive term such as the largest unit value or processing time remains
visible. Exact budgets, compulsory totals, eligibility restrictions and
shared resource roles survive the rounding step. A theorem for compulsory
players does not automatically extend to selecting a player basis.

Support size, construction time, writable space, update work, query cost,
output length and recourse are separate quantities. A compact witness is not
an algorithm that lists a potentially much larger witness in the same time.

## Parameter ranges

State whether accuracy and tradeoff parameters are fixed constants, binary
inputs or functions of instance size. Uniform statements require uniform
constants and an implementation valid throughout the declared range.

Graph compositions name their backend contracts, degree and length
assumptions, update horizon and restart costs. A finite startup constant in
a fixed-data compiler is independent of the input; that fact does not make
its construction a practical polynomial-time preprocessing routine.

## Numeric-target examples

The [numeric-target family](../problems/numeric-target-frontier/) illustrates
why several bounds must remain separate.

| Regime | Bound | Scope |
|---|---|---|
| Arbitrary overlapping rows | $2^{O((T+1)\log(T+2))}\operatorname{poly}(H)$ | The stated numeric-target oracle model |
| Fixed row dimension $d$ | $\exp(O_d((T+1)^{d/(d+1)}))\operatorname{poly}(H)$ | Constants may depend on fixed $d$ |
| Exact single-matroid variants | $2^{O(\sqrt T+1)}\operatorname{poly}(H)$ | Directions, original-base requirements and optimization variants are specified individually |
| Refined accuracy schemes | $\varepsilon^{-1}\exp(141/(50\varepsilon)+7)\operatorname{poly}(H_\varepsilon)$ | The seven specified minimum/maximum schemes |
| Two-parameter budget envelope | $2^{O(f(T,Q))}\operatorname{poly}(H)$, $f(T,Q)=T\log_2(2+\min\{Q/T,T\})$ | $T,Q>0$ after preprocessing; zero cases are polynomial |

The matching-order lower bound for the last row is a worst-case statement
under parameter upper budgets. It does not say that every instance with the
same exact parameter pair is hard.

## Lower bounds and kernels

Unconditional oracle-query lower bounds concern access to an opaque oracle.
Deterministic-ETH consequences for readable programs use a separate complexity
assumption. They do not exclude randomized algorithms without an appropriate
randomized assumption, or automatically apply to every graphic or linear
representation.

A ground reduction can retain few selectable items while still querying the
original oracle and carrying original weights. It is not a parameter-only bit
kernel unless the entire encoded output is bounded. Bounds on retained ground
size must not be substituted for construction-time bounds.

## Evidence

Each problem's `verify/README.md</BT> distinguishes its manuscript proof from
available executable evidence. Exact finite checks establish the reported
identities on their stated domains. A continuous-domain certificate additionally
needs a coverage argument and sound interval bounds. Neither form alone is a
proof-assistant derivation of an asymptotic algorithmic theorem.

The [evidence index](../reviews/README.md) lists all current programs and the
single repository validation command. Internal review and external peer review
are separate statuses; the repository does not claim external review or
proof-assistant verification.
