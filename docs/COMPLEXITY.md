# Complexity guide

This is the canonical display convention for Algorithm Frontier. Every curated result should separate its guarantee, parameters, time, space, model, lower bound, and review status.

## Notation

| Symbol | Meaning |
|---|---|
| $$H$$ | Complete binary input plus the polynomial work charged to the named rank, oracle, flow, intersection, or optimization primitives. |
| $$H_\varepsilon$$ | $$H$$ plus the complete binary encoding of the supplied rational accuracy. |
| $$n,m$$ | Vertices and edge records in graph problems. |
| $$T$$ | Sum of the explicit integer numeric targets in a target-row instance. It is a numeric parameter, not a bit length and not $$1/\varepsilon$$. Support-sensitive bounds with $$T>0$$ state their separate zero-target preprocessing. |
| $$Q$$ | Number of distinct nonempty support patterns of eligible columns. It is not the number of rows, the maximum arity, or the number of nonzero coefficients. |
| $$d$$ | Number of overlapping numeric rows in a fixed-dimensional result. |
| $$U_j$$ | Row allowance used by the profile bound: $$T_j$$ for upper/equality rows and $$2T_j-1$$ for positive covering rows after zero-cap preprocessing. |
| $$\varepsilon$$ | Rational approximation accuracy, with the objective direction stated separately. |
| $$\mathrm{OPT}$$ | Original integer optimum under the exact model and comparator named by the record. |
| $$r,q,c$$ | Common rank, explicit ground size, and corank-style parameter, respectively; each record defines its local use. |

## How to read a result

1. **Guarantee.** Exact, approximation, certificate, decision, or tradeoff.
2. **Objective direction.** State MIN/MAX, feasibility, makespan, stretch, recourse, or another output measure.
3. **Time and space.** Keep polynomial factors visible and report writable space independently from oracle work.
4. **Parameters.** Distinguish numeric targets, ranks, graph size, accuracy, support geometry, and encoded input length.
5. **Representation.** Say whether the resource is an opaque rank oracle, a readable rank program/circuit, an explicit graph, or another representation.
6. **Lower-bound status.** Mark unconditional oracle-query results separately from deterministic-ETH or randomized-ETH consequences.
7. **Review status.** Internal review, formal verification, external peer review, and implementation testing are different claims.

## Current numeric-target frontier

| Regime | Displayed upper bound | Boundary |
|---|---|---|
| Arbitrary overlapping rows | $$2^{O((T+1)\log(T+2))}\,\mathrm{poly}(H)$$ | R; matching-order rank-oracle lower bound in the stated model |
| Fixed $$d$$ rows | $$\exp(O_d((T+1)^{d/(d+1)}))\,\mathrm{poly}(H)$$ | R; matching exponent-order lower bound |
| Exact single-matroid variants | $$2^{O(\sqrt{T+1})}\,\mathrm{poly}(H)$$, and $$2^{O(\sqrt{\mathrm{OPT}+1})}\,\mathrm{poly}(H)$$ for integer optimization | R; exact side directions and mandatory-base scope are retained |
| Refined accuracy scheme | $$\frac1\varepsilon\exp(141/(50\varepsilon)+7)\,\mathrm{poly}(H_\varepsilon)$$ | R; the inverse-accuracy upper/lower gap remains open |
| Support-sensitive rows | $$2^{O(T\log(2+Q/T))}\,\mathrm{poly}(H)$$ | S; no arity restriction, with $$T>0$$ after preprocessing |
| Two-parameter budget envelope | $$2^{O(f(T,Q))}\,\mathrm{poly}(H)$$, $$f(t,q)=t\log_2(2+\min\{q/t,t\})$$ | S; matching worst-case query classification under budget upper bounds |

These are theorem-record displays, not universal practical runtime predictions. A formula remains conditional on the model, representation, backend contract, and source paths recorded by its problem record.

## Result-card template

```markdown
| Item | Result |
|---|---|
| **Guarantee** | Exact or approximate output statement. |
| **Objective** | MIN, MAX, feasibility, makespan, stretch, or certificate target. |
| **Time** | The full displayed bound, including polynomial input factors. |
| **Space** | Writable space and any oracle-work convention. |
| **Parameters** | Numeric, structural, graph, rank, accuracy, and support parameters. |
| **Model** | Resource and representation assumptions. |
| **Lower bound** | Unconditional or conditional boundary, if available. |
| **Status** | Internal review, formal verification, external review, or implementation state. |
```
