# Independent review of the robust common-role obstructions

**25 October 2026. Reviewer: transfer_frontier. Full review of
`robust_unrelated_common_role_obstructions.md`, CR1--CR7 and all
six sections: PASS.**

This review separates the explicit failed-proof counterexamples from
the conditional parameterized hardness consequence. Neither is
interpreted as a new whole-ground exponential-base lower bound.

## 1. One player already invalidates a common role promise

With one compulsory player, scenario A has one value-two unit and
scenario B has three value-three-quarters units. The robust optimum
is exactly two. At threshold one, A can serve the player only through
a heavy pair and B only through light pairs. Putting the player into
one shared light set forbids the useful A pair; putting it outside
forbids the required heavy unit in B. Both possible common roles
therefore fail to represent the original witness.

For a fixed near-two scaling alpha, replacing B's unit value by
alpha/2 and its capacity by ceil(4/alpha) keeps its maximum at least
two while its units remain strictly below the threshold alpha. The
capacity change is needed and is correctly explicit. This example
is a representation failure, not a computational lower bound.

## 2. Zero role disagreement does not make a common dummy integral

For M=U_(2,4), each scenario S is a pair and its resource is free
off S with a rank-one cap on S. The common fractional dummy y=1/2
on all four players has total two and lies in P(M*). Each scenario
vector x^S=1/2 is feasible: its two coordinates in S sum to one and
its other singleton coordinates are at most one. Thus x^S+y=1
holds everywhere with zero costs and budgets.

For every actual original basis B, scenario S=B permits at most
one total unit on the two selected players. At least one receives
zero integer utility, so the robust optimum is zero. All real
values are one and can be declared heavy in every scenario, hence
there is no role-disagreement issue to blame for this failure.

If a common integer dummy existed after a count-preserving rounding,
its support would have size at most two. Choose two dummy-free
players u,v. Scenario {u,v} would have to provide a real unit to
both, contradicting its rank-one cap. This proves that even the
proposed simultaneous count-floor property cannot be achieved.
Each scenario separately admits an integral dummy completion, but
the support may depend on the scenario; that does not establish
a common actual selected basis.

## 3. Parameterized consequence and its precise assumption

The existing Hitting Set reduction preserves player corank c=k and
has integer robust optimum either zero or one. Every possible
positive real unit has the same heavy role, so adding a parameter
that is zero on these identical all-heavy role patterns does not
remove the reduction. Any deterministic finite multiplicative
guarantee would have to output positive, hence at least unit,
utility on a yes instance. Legal outputs on no instances have
value zero. Such an algorithm in F(c,d) times polynomial input
time would decide the parameterized Hitting Set problem.

Fresh primary checks confirm the required public hardness premise:
[Jansen's paper](https://arxiv.org/abs/1507.05890) explicitly states
W[2]-completeness for Hitting Set parameterized by solution size;
[Inamdar et al., MFCS 2023, Section 1.1](https://drops.dagstuhl.de/storage/00lipics/lipics-vol272-mfcs2023/LIPIcs.MFCS.2023.55/LIPIcs.MFCS.2023.55.pdf)
records the same lower-bound background. Under FPT!=W[2], the
manuscript's deterministic exclusion follows. It is not a claim
about an arbitrary disagreement definition that measures unrelated
resource data, a scenario-count parameter, or an exponential base
in q.

## 4. Scenario-specific setup charges add a separate feasibility gate

For a source set S, assigning setup fee one exactly on S and
budget |S|-1 makes a basis B affordable exactly when it omits at
least one element of S. With M=U_(q-k,q), its complement is a
size-k hitting set. Empty source sets and rank-zero edge cases
are handled by the stated companion preprocessing. All real
assignments can have zero value and cost, so the obstruction is
already present in legal zero-utility selection.

Independent per-scenario setup minimizers need not coincide and
therefore do not supply one affordable common basis. This validates
the common-scalar restriction in the positive additive theorem.

## 5. The retained positive regimes and public-model distinction

When the actual selected basis is fixed, scenario allocations are
separate one-budget problems. Running their algorithms independently
preserves the same basis and costs a sum of scenario runtimes, not
a Cartesian product of their role choices. This is consistent with
both explicit counterexamples. The additive common-setup theorem
also fixes one actual basis before rounding scenarios, avoiding the
failed shared-dummy requirement. The robust unit floor guarantee
likewise does not promise positive output at optimum one without
its additional unit-feasibility hypothesis.

The cited recoverable-basis paper was freshly opened from the
[working Kyushu repository PDF](https://catalog.lib.kyushu-u.ac.jp/opac_download_md/7161146/7161146.pdf).
Its input is one matroid and full-rank scenario subsets E_i; its
decision condition is a basis B with |B intersection E_i|>=r-k.
It proves fixed-parameter tractability by scenario count for that
recovery model. This is not the present common-selection model
with adaptive integer service resources, so the manuscript's
literal model distinction is justified. The original `api.lib`
URL failed during this check; the `catalog.lib` URL above works.

## 6. Verdict

All explicit constructions and conditional implications pass. The
note correctly identifies failures of two proposed lifts, preserves
the distinction between additive and multiplicative guarantees,
and avoids an unsupported universal robust impossibility claim.
Only the repository URL replacement is suggested; no substantive
mathematical correction is requested.
