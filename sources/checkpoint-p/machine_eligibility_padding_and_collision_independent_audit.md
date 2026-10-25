# Independent audit of eligibility padding and collision-aware makespan

**25 October 2026. Full independent mathematical review of I1--I20 and the optional I16a--I16c refinement.**

Reviewed manuscript:
`machine_eligibility_padding_and_collision_makespan_draft.md`.
The padding, withdrawal, collision threshold, reconstruction and target
search pass this review. The result remains an internally derived
theorem for arbitrary integral job polymatroids, with its stated
rank-dependent runtime, commitment term and smaller-job rounding loss.

## 1. The collision threshold is exact in the stated model

For any machine p and large type j, at most f_j({p}) units of that
type can be assigned to p. Thus any two large units coexisting at p
must appear among the multiset that retains up to two copies of every
eligible type size. Their summed load is at least the sum of that
multiset's two smallest entries. Minimizing over p proves the lower
bound C2 for every large collision.

The converse used to describe C2 as an exact threshold is also valid.
One unit at p from a type with singleton rank at least one is an
independent integer vector of that type polymatroid. Two units from
one type are independent when its singleton rank is at least two.
The chosen vector can be extended to an integer base of that type.
For two different types, perform the extensions independently. Since
job-type constraints are separate, these bases coexist as an assignment
of the large types. Other assigned units may add load, but the selected
pair itself realizes the claimed two-unit collision load.

This argument would need revision for a model coupling different job
types by additional constraints. No such coupling is present here.

If C2 is infinite, every aggregate singleton f_b({p}) is at most one.
An integral normalized monotone submodular function with these singleton
bounds is a matroid rank function, so its Boolean cap preserves rank h.
Thus Boolean rank loss and C2=infinity cannot occur simultaneously.
In fact this case also forces a_p=ell_p on every large-eligible machine:
only one large type can have positive singleton rank there, and that
rank is one. Therefore H=0 automatically on every residual Q. Its
rank-one special case consequently gives max{OPT+u,B(F0)} without
an additional zero-width assumption.
If Boolean rank is below h, every complete large assignment has some
collision, giving OPT>=C2 and the stated public additive bound.

The easy/hard partition is also valid when C2<a_+: then the hard
interval [a_+,C2) is empty. The guarantee may be weak in that case,
but its separate public additive or factor-two fallback remains valid.

## 2. Commitment, contraction and loop removal preserve the full promise

Let F0 be an arbitrary independent commitment of size h-k in the
Boolean large-recipient matroid M. A target-feasible schedule below
C2 has a Boolean M-basis I*. Its image spans M/F0, so I* minus F0
contains a basis J* of that contraction. Every such basis lies among
the nonloops Q used in the draft.

Restricting the optimal dual small-workload vector to J* preserves
its recipient-polymatroid feasibility. It supplies at least
ell_p/Delta at every selected p, because the actual large job at p
has size at least ell_p. No type is preassigned to F0 or J*, and
the promise does not require F0 to belong to the optimum basis.

The resource operation is restriction to Q, not contraction by an
unspecified resource vector at F0. This is essential. Later zero
extension to all other machines is feasible by monotonicity of f_T.
Discarding contraction loops only removes players that cannot belong
to a contracted basis; it does not remove the promised J*.

The original singleton definitions of ell_p and a_p remain valid on
Q. Every nonloop of M/F0 is a nonloop of M, hence can receive some
large type. The required extrema therefore exist for k>=1.

## 3. The simple padding scale and its binary arithmetic

For all p in Q, a_p-ell_p<=A-a_-. Taking the maximum width gives
H<=A-a_-, and therefore

\[
                    a_-\le L=A-H\le A\le a_+.
\]

In particular L is positive. It is a difference of attained sizes
and attained size differences, so it lies on the common original
size grid g. If D=A_D/B_D and Delta=g/A_D, then

\[
                   K=(L/g)A_D,\qquad b=(L/g)B_D
\]

are positive integers and Db=K exactly. The private count
(L-ell_p)_+/Delta is integral for the same reason. Binary lengths
of all products and scaled rank values remain polynomial in the
input encoding and in the supplied rational D; no numerical count
is expanded.

Adding the private modular vector d to f_T gives a valid integral
polymatroid. On the promised J*, ell_p/Delta+d_p is at least K.
Thus the uniform K-quota core is promised feasible. The core may
legally be asked for b units, since D>=3-2/k makes its strict
finite-rank condition hold. For D=3-2/k+eta, its relative margin
exceeds eta/2 as claimed. This is a paid workload construction,
not an assertion about splitting original indivisible jobs for free.

## 4. Private withdrawal is a global rank proof, not a coordinate guess

The withdrawal identity is correct for every nonnegative modular d:

\[
                        y\in P(f+d)
                      \Longrightarrow (y-d)_+\in P(f).
\]

For S, put E={p in S:y_p>d_p}. Then

\[
        (y-d)_+(S)=y(E)-d(E)\le f(E)\le f(S).
\]

This proves all rank inequalities simultaneously. It does not rely
on choosing compatible private/original decompositions one coordinate
at a time.

Prune the returned allocation to b on each member of J and zero
elsewhere, then withdraw d. The retained original dual counts are
exactly (b-d_p)_+ at the selected machines and zero elsewhere.
They are feasible in the restricted original dual, extend by zero
to the full original dual, and can be extended to an integer base.
The subsequent complement produces a capped small-workload base.
All count and nonnegativity requirements follow from feasibility in
that dual polymatroid; no negative slack is inserted into a schedule.

## 5. The load bound survives restoration of every original type

The guaranteed original dual workload at a residual selected p is

\[
      \max\{0,L/D-(L-\ell_p)_+\}.
\]

If ell_p>=L, the overhead from its large job is at most a_p-L/D,
which is bounded by A-L/D. If ell_p<L, the same overhead is at most
(a_p-ell_p)+(1-1/D)L, even when the untruncated lower bound on
retained dual workload is negative. This is bounded by
H+(1-1/D)L. The two bounds coincide at L=A-H, yielding

\[
                       E_D=((D-1)A+H)/D.
\]

A fully piecewise check gives the same conclusion: when the retained
dual workload is zero, ell_p<(1-1/D)L, so
a_p<=ell_p+H<E_D. Thus the truncation at zero does not hide a bad
machine in the upper bound.

The basis F0 union J has exactly h distinct large recipients.
Decomposition into the original large-type bases assigns at most
a_p large load at p, whatever type the decomposition chooses.
The small workload decomposes into fractional bases of every original
small type; the previously audited per-machine rounding adds at most u.
This proves T+E_D+u on residual selected machines and T+u on machines
without a large job.

Committed machines use an absolute bound after rounding. Every
original small-type integer base satisfies x_j(p)<=f_j({p}), so their
small load is at most W_p. Their large load is at most a_p. Therefore
their final bound is C_p=W_p+a_p, with no extra u. This verifies the
combined hard-target bound in I17.

## 6. Easy branches, exceptional cases and the target search

At every feasible target T<C2, there is at most one large unit per
machine, so the promised-basis argument applies. At T>=C2, the
ordinary additive algorithm gives T+a_+ and hence coefficient
1+a_+/C2. In the hard branch T>=a_+, so T+E_D is at most
(1+E_D/a_+)T. Their maximum gives I18. When C2 is infinite, no
collision branch is needed and its coefficient is correctly set to
one. An automatic three-halves floor is not inserted in that case.

Every failure in these branches is original integer infeasibility:
a target below the attained largest job size, a necessary capped
small-workload rank loss, an impossible retained padded quota, or
infeasibility of the easy assignment relaxation. There is no failure
caused solely by an inconvenient rank budget.

All original schedule loads and the finite collision threshold lie
on the chosen Delta-grid. The minimization search keeps a failed
lower target, strictly below OPT, and a successful upper target.
A success need not imply a schedule of that trial's own makespan.
Nevertheless grid adjacency forces the final successful trial to
be at most OPT. Substituting it into the fixed monotone output
bound proves I19. This orientation is the correct minimization
counterpart of the separate fractional max-min search.

If OPT<C2, that final successful trial is also below C2, so the
conditional additive comparison OPT+E_D+u is justified. It must
not be claimed if the successful search may use the easy branch.
Rank loss in M is handled separately, and the no-small-job case
has u=0 with a zero small-workload rank. The commitment-free case
uses B(F0)=0. All these cases are consistent with the formulas.

## 7. Optional exact scalar padding optimization

The added Section 8.1 is also correct. For D>1, a target common
overhead C<A requires positive residual workload only from players
with a_p>C. For each active p, both linear terms in I16a must be
at least a_p-C. The common lower endpoint is D(A-C), because a
machine attaining A is active. The common upper endpoint is
D(C-H_active)/(D-1). Their intersection is nonempty precisely when

\[
                  DC\ge(D-1)A+H_{\rm active}(C).
\]

The strict comparison a_p>C is necessary: a player with a_p=C
requires zero residual workload and imposes no upper endpoint.
Sorting the a_p values therefore gives the stated half-open intervals
with constant active width, and each right endpoint is correctly
reconsidered with its new active set. A sufficiently small positive
L0 supplies positive residual workload to every player, proving
the existence of a candidate with C<A.

If C* lies on g/A_D, then L0=D(A-C*) lies on g/B_D. The refined
quantum g/(A_D B_D) makes K, b and all private counts integral,
with Db=K. The argument changes only the guaranteed overhead and
the finite grid; it does not change the resource or player proof.
For D=1, the optimum is H and the simple scale already attains it.

The stated limitation for D<=3 also checks. A strict improvement
C*<E_D forces every machine attaining width H to have a_p<=C*;
otherwise that width remains active and forces C*>=E_D. In this
case H>0, and such a machine is eligible for two distinct large
sizes whose sum is 2a_p-H. Hence

\[
                       C_2\le2E_D-H.
\]

For a short check of the algebra, put h0=H/A and e=E_D/A. For
1<=D<=3, one has h0<=e<=(2+h0)/3. The function e(2e-h0) is
nondecreasing on that range, so

\[
 \frac{E_D(2E_D-H)}{A^2}
       \le\frac{(2+h_0)(4-h_0)}9
       =1-\frac{(1-h_0)^2}{9}\le1.
\]

Since A<=a_+, it follows that a_+/C2>=E_D/a_+. The easy collision
coefficient already dominates the unrefined hard coefficient.
Therefore this scalar optimization does not by itself improve the
unconditional coefficient for those D values, although its hard-
branch additive certificate can improve. The manuscript preserves
that qualification correctly.

## 8. Scope and review conclusion

No substantive gap was found in the full composition. The useful
new structural information is machine-specific eligibility width and
the actual minimum two-large-unit collision, with arbitrary integral
job polymatroids and binary multiplicities retained. The output still
pays the explicit +u at machines whose guarantee comes from rounded
small workload, and still pays B(F0) on commitments.

The approximation quality is conditional on these computable quantities
being favorable; it is not a uniform near-five-thirds theorem for
arbitrary sizes. The local width may be small despite a large global
size spread, and C2 may be infinite, but those facts are instance
properties, not omitted assumptions.

Public aggregation, decomposition and additive-rounding primitives are
those already checked against [Bamas et al., arXiv:2307.08453v1](https://arxiv.org/html/2307.08453v1)
in the preceding workload audits. The unit search depends on the
internally reviewed prefix core, including its mandatory all-center
normalization. This note adds independent mathematical review; it
does not claim an implementation, formal verification, external peer
review, or exhaustive publication-priority determination.
