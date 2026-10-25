# Checkpoint T — maximum-target prefix quotas and exact laminar optimization

**25 October 2026. Increment only, relative to frozen checkpoint S.**

This package contains new proofs developed after S. It does not reproduce the earlier total-target/support-pattern classification or reopen the retired general-matching exponent. Its two main additions are sharp maximum-target classifications for ordered quotas and an exact root-cap algorithm for branching laminar quotas with unrestricted scalar costs.

All upper bounds below are deterministic, preserve optional integer vectors or the original required base total, and use uniform polynomial binary workspace. The resource is one global normalized monotone integral polymatroid supplied by an exact rank-value interface. An arbitrary signed rational scalar is optimized exactly. Standard exact submodular minimization and integral polymatroid intersection are charged polynomially. H denotes the complete binary input and oracle bit bounds.

The new lower bounds distinguish unconditional rank-query statements from conditional readable-rank-program/circuit statements. They do not imply hardness for graphic or explicitly matrix-represented resources.

## 1. New theorem map

Here B is the largest quota target in the prefix results, and the explicit root-weight cap in the laminar result. C is the number of distinct original positive row-incidence supports after the stated preparation. The parameter p counts distinct supplied weight families.

| New model | Deterministic exact time, apart from polynomial(H) | Lower statement proved in this increment |
|---|---|---|
| One coordinate order, one common nonnegative integer weight vector | \(2^{O(B)}\) | \(2^{\Omega(B)}\) randomized worst-case rank queries |
| Two arbitrary coordinate orders, one common weight vector | \(2^{O(B\log(B+2))}\) | \(B!/3=2^{\Omega(B\log B)}\) queries |
| One order and its reversal, one common weight vector | \(2^{O(B)}\) | The one-order lower family applies |
| One order, support count C | \(2^{O(\sqrt{B\min\{C,B\}})}\) | Matching worst-case parameter-budget exponent |
| Two arbitrary orders, support count C | \(2^{O(\min\{\sqrt{BC},\,B\log_2(2+\min\{C/B,B\})\})}\) | Matching worst-case parameter-budget exponent |
| One common order, p weight families | \(2^{O(pB\log(p+2))}\) | Joint matching oracle exponent on every even \(p\ge4\), \(B\ge1\), and for upper-budget classes |
| Arbitrary branching laminar quota family, one common weight vector, root cap B | \(2^{O(B^2\log(B+1))}\) | A \(2^{\Omega(B)}\) oracle lower example; the gap is open |

The laminar theorem includes arbitrary signed scalar coefficients on zero-weight coordinates. Their number, total possible resource mass, and diversity of scalar costs do not enter the exponential factor.

These are exact numeric algorithms. Their parameter B is an integer magnitude, not its binary encoding length, and the time bounds are not polynomial in log B.

## 2. One versus two ordered quota systems

For one common weight vector, prefix dominance leaves at most B positive upper targets and B positive covering targets in each order. Covering feasibility can be witnessed by a first-reaching segment of units. After capping cover coefficients at B, that segment has mass at most \(2B-1\). The full resource and true scalar remain on shared active/passive copies; uncredited units stay in the model.

One order therefore has at most \(O(B)\) colored coefficient directions and \(O(B)\) useful mass. Colored integer-partition counting gives the single-exponential bound. Two arbitrary orders need at most four shared copies, have \(O(B)\) useful mass, and can have \(O(B^2)\) incidence colors. The second colored-profile count gives the \(B\log B\) exponent.

Opposite orders are a stricter geometry. Prefix and suffix endpoints have only \(O(B)\) combined interval patterns, restoring the single-exponential bound.

The two-order lower construction uses the edge ground of \(K_{B,B}\). The first order groups edges by left endpoint and the second by right endpoint; cumulative equality targets \(1,\ldots,B\) force a perfect matching. A single globally hidden paving-type resource distinguishes B! candidate matchings. This is a maximum-target calibration of established paving/partition constructions, not a new general 3-matroid-intersection hardness framework.

The one-order lower uses consecutive blocks with weights 1,2,3,4 and cumulative equality targets 5,10,... . Each block has two balanced choices, giving an exponential family. Readable rank-program ETH reductions are proved separately in the manuscripts.

Full proofs:

- exact_weighted_prefix_quotas_max_target.md (PX1–PX15).
- two_order_weighted_prefix_target_classification.md (TP1–TP22).

## 3. Actual-support refinements and exact lower quantifiers

The same profile catalogue has both a square-root colored-partition estimate and a binomial estimate. Applying both to the actual original incidence count C yields the two support-sensitive exponents in the table.

For every integer upper budgets \(b\ge2^{14}\) and \(c\ge1\), the lower construction has actual \(B\le b\), \(C\le c\), polynomial(b)-size explicit coefficient data, and randomized worst-case query lower bound at least

\[
  2^{g_i(b,c)/64},
\]

where

\[
 g_1(b,c)=\sqrt{b\min\{c,b\}},\qquad
 g_2(b,c)=\min\{\sqrt{bc},\,b\log_2(2+\min\{c/b,b\})\}.
\]

The low-pattern family uses complementary pairs in weighted blocks. The forbidden reference family is the whole feasible rank-sized family, not merely a convenient countable subfamily. This prevents overlooked feasible bases from invalidating the reduction.

For mandatory bases the low-pattern lower is an equality-feasibility lower. For optional vectors it uses exact cardinality maximization, because the equalities need not force the full rank. The high-pattern two-order family already gives pure feasibility hardness in both conventions. These distinctions are explicit rather than hidden behind one undifferentiated statement.

The theorem is a worst-case upper-budget classification. It does not assert matching lower bounds for every exact parameter pair, every order geometry, or every explicit resource representation.

Full proof: weighted_prefix_support_budget_tradeoffs.md (PS1–PS23).

## 4. Several weight families: a jointly sharp exponent

When every prefix row chooses one of p nonnegative integer weight vectors but all rows use the same coordinate order, there is still one common chronological unit list. Each covering family has one first-reaching cut. Sorting those cuts gives at most p+1 shared copy layers after enumerating their order.

The collapsed coefficient vector of a copy has p entries, including genuine zero entries. Its total useful mass across families is \(O(pB)\). Within one endpoint/layer color, a multiset of such vectors of total mass w injects into a length-w word over p symbols with marked cuts. Its count is at most \((2p)^w\). Endpoint colors, the shared resource recovery, and the streamed cut orders then give

\[
  2^{O(pB\log(p+2))}\operatorname{poly}(H).
\]

The exponent does not separately enumerate all zero patterns, and binary-large original rank does not create a unit list.

The new joint lower reuses p vertex-incidence weight families over B consecutive copies of \(K_p\), for every even \(p\ge4\). At the end of block j, every family has cumulative equality target j. Feasible sets select one perfect matching in each block, so

\[
 N=((p-1)!!)^{B}
   =2^{\Theta(pB\log(p+2))}.
\]

There is one global hidden resource matroid across the blocks. It is not a direct sum of independently hidden oracles. Randomized exact feasibility needs at least N/3 queries.

The encoded ETH reduction chooses \(a_p=\lfloor\log_2((p-1)!!)\rfloor\) and \(B=\lceil\nu/a_p\rceil\), with an explicit admissible range for p. Product-matching ranks then encode all assignments in polynomial space and input size, and \(pB\log(p+2)=\Theta(\nu)\). This supplies calibrated joint families, without claiming pointwise encoded ETH hardness at every arbitrary numerical pair.

Full proofs:

- few_weight_families_prefix_target_scheme.md (FW1–FW20).
- few_weight_prefix_joint_lower_bounds.md (FJ1–FJ19).

## 5. The boundary when every row has its own weight vector

A largest target alone cannot support the preceding FPT claim for arbitrary row-dependent weights. The new reduction uses a uniform rank-k resource, identical full-prefix supports, coefficients only 1 and 2, and common target \(k+1\).

For a SetCover instance, give the row for element u and the coordinate for set S coefficient \(1+\mathbf1[u\in S]\). Any feasible independent vector selects at most k sets and covers every element. Conversely, a cover of size at most k can be padded to k sets, making every row feasible. This yields W[2]-hardness in \(B=k+1\), for both optional and mandatory feasibility, with scalar zero.

All columns have the same nonempty row support. Thus a support-count hypothesis cannot replace the common-weight or bounded-family hypothesis. No stronger quantitative ETH or approximation statement is asserted by this reduction.

Full proof: row_dependent_full_prefix_target_boundary.md (RW1–RW8).

## 6. Branching laminar quotas, including all zero-weight costs

The laminar model has one common nonnegative integer weight vector, arbitrary mixed quotas on an explicit laminar family, and a root cap B. Dominance bounds the depth of retained upper rows by B. Retained positive lower rows have at most B disjoint minimal requirements and depth at most B, yielding at most \(B^2+1\) lower-membership patterns. The number of upper nodes can still be unbounded.

The elementary proof uses bounded-rank tests for inclusion-maximal upper blockers. These blockers are disjoint and each contains a selected witness, so their total test rank is small even when the upper family is large. A total-rank refinement of the Huang–Ward representative recursion gives a catalogue of size \(2^{O(B\log(B+1))}\); enumerating at most B choices gives the displayed \(B^2\log B\) time bound.

Arbitrary zero-weight scalar costs require a stronger comparison. At a fixed positive cardinality k, define \(p_k(S)\) as the best full scalar obtainable by completing the positive set S through all zero-weight coordinates. Public weighted Rado induction proves that \(p_k\), when finite, is a minimum-cost valuated matroid. The enormous conceptual matching construction is used only for this proof.

For any candidate pool Y, optimize a full completion first to maximize the overlap \(|A\cap Y|\), then to minimize \(p_k(A)\). Valuated exchange shows that the at most k elements of \(A\cap Y\) contain a no-worse replacement for any protected \(e\in S\cap Y\). The laminar blocker recursion uses this statement in place of a fixed positive-element score.

Every actual overlap query is binary-compressed. Positive copies have cap one in one box-truncated shared polymatroid. One two-group partition imposes positive total k and zero total \(R-k\); total R forces both equalities. A dominant integral reward gives the lexicographic objective without introducing a third resource. Zero capacities and their true signed costs remain compressed.

If B is at least the explicit positive-coordinate count, a direct streamed count-vector fallback avoids expanding B copies per coordinate. In the other branch B is smaller than that count, so the positive copy ground and every replayed recursion state have polynomial binary size. Failed profiles, infeasible cardinalities, invalid candidate paths, and empty completion faces are included in the all-input time analysis.

Full proofs:

- laminar_common_weight_root_cap_fpt.md (LM1–LM25), including the residual-polymatroid and elementary representative lemmas.
- uniform_zero_scalar_laminar_extension.md (UZ1–UZ8), an independent simpler uniform-cost specialization.
- laminar_valuated_zero_completion_fpt.md (VZ1–VZ20), the full arbitrary-cost theorem.

The \(2^{\Omega(B)}\) lower example does not match the \(2^{O(B^2\log B)}\) upper bound. This gap is left explicit.

## 7. Baselines, status, and what is not claimed

The primary-source increment records the exact relationships to profile/partition intersection, Huang–Ward joint representatives, the 2026 reachable kernels, weighted Rado induction, SetCover hardness, and paving/SAT-decoder lower frameworks. These are substantial antecedents. No publication-priority claim is made.

A targeted additional check of the public OpenAI mathematics index looked for laminar, valuated, matchoid, quota, and prefix terminology. Its scope is the index and the displayed descriptions, not an exhaustive examination of every linked manuscript.

All nine mathematical manuscripts in this package received complete internal mathematical review, including a separate review of their major proof gates. That is evidence of careful scrutiny, not formal verification or external peer review. No Lean files, PDFs, executables, test bundles, or internal review logs are included.

The package does not claim an algorithm for arbitrary row-dependent prefix weights parameterized by B alone; a closed optimal laminar exponent; a deterministic consequence of a randomized public kernel; or a lower bound for graph/matrix resource representations.

Work on arbitrary overlapping, column-sparse row systems began after these T proofs. That work is not asserted or included here.
