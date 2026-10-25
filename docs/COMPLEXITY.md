# Complexity guide

This is the canonical display convention for Algorithm Frontier. Every curated result separates its guarantee, objective, parameters, time, space, model, lower-bound type, representation, and review status.

## Display notation

GitHub-facing pages use plain text inside code spans. The notation is intentionally portable:

| Display | Meaning |
|---|---|
| `H` | Complete binary input plus polynomial work charged to named rank, oracle, flow, intersection, or optimization primitives. |
| `H_eps` | `H` plus the complete binary encoding of the supplied rational accuracy. |
| `n, m` | Vertices and edge records in graph problems. |
| `T` | Sum of explicit integer numeric targets. It is numeric, not a bit length and not `1/eps`. |
| `Q` | Number of distinct nonempty support patterns of eligible columns. It is not row count or nonzero count. |
| `d` | Number of overlapping numeric rows in a fixed-dimensional result. |
| `U_j` | Row allowance used by the profile bound: `T_j` for upper/equality rows and `2 T_j - 1` for positive covering rows after zero-cap preprocessing. |
| `eps` | Rational approximation accuracy; objective direction is stated separately. |
| `OPT` | Original integer optimum under the exact model and comparator named by the record. |
| `r, q, c` | Common rank, explicit ground size, and corank-style parameters; each record defines local use. |

Use `2^(...)`, `exp(...)`, `poly(...)`, `Gamma(...)`, `sqrt(...)`, and `binom(...)` rather than TeX commands in curated pages. Keep source notation unchanged in imported manuscripts.

## Required result-card fields

1. **Guarantee** — exact output, approximation, certificate, decision, or tradeoff.
2. **Objective** — MIN, MAX, feasibility, makespan, stretch, recourse, or another measure.
3. **Time and space** — show polynomial factors and writable space independently.
4. **Parameters** — distinguish targets, ranks, graph size, accuracy, support geometry, and encoded input length.
5. **Representation** — opaque rank oracle, readable rank program/circuit, explicit graph, or another representation.
6. **Lower-bound type** — keep unconditional oracle-query results separate from deterministic-ETH or randomized-ETH consequences.
7. **Review status** — distinguish internal review, formal verification, external peer review, and implementation testing.

## Numeric-target frontier

| Regime | Displayed upper bound | Boundary |
|---|---|---|
| Arbitrary overlapping rows | `2^(O((T + 1) log(T + 2)) * poly(H))` | R; matching-order rank-oracle lower bound in the stated model |
| Fixed `d` rows | `exp(O_d((T + 1)^(d / (d + 1))) * poly(H))` | R; matching exponent-order lower bound |
| Exact single-matroid variants | `2^(O(sqrt(T) + 1) * poly(H))`; integer optimization uses `sqrt(OPT)` where stated | R; exact directions and mandatory-base scope are retained |
| Refined accuracy scheme | `(1/eps) * exp(141/(50 eps) + 7) * poly(H_eps)` | R; inverse-accuracy upper/lower gap remains open |
| Support-sensitive rows | `2^(O(T log(2 + Q/T)) * poly(H))` | S; no arity restriction after `T > 0` preprocessing |
| Two-parameter budget envelope | `2^(O(f(T, Q)) * poly(H))`, with `f(t, q) = t log2(2 + min(q/t, t))` | S; worst-case query classification under budget upper bounds |

These are theorem-record displays, not universal practical runtime predictions. A bound remains conditional on the model, representation, backend contract, and source paths recorded by its problem record.

## Result-card template

```markdown
| Item | Result |
|---|---|
| **Guarantee** | Exact or approximate output statement. |
| **Objective** | MIN, MAX, feasibility, makespan, stretch, or certificate target. |
| **Time** | Full displayed bound, including polynomial input factors. |
| **Space** | Writable space and any oracle-work convention. |
| **Parameters** | Numeric, structural, graph, rank, accuracy, and support parameters. |
| **Representation** | Oracle, readable program, explicit graph, or other representation. |
| **Lower bound** | Unconditional or conditional boundary, if available. |
| **Status** | Internal review, formal verification, external review, or implementation state. |
```
