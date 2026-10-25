# Verification note

**Curated source path:** `sources/checkpoint-o/general_resource_prefix_additivity_root_audit.md`

The source audit follows.

# Root audit of prefix rank additivity and eager release

**25 October 2026. Independent mathematical review by the root researcher.**

This audit concerns the current version of
`general_resource_prefix_additivity_four_candidate.md`, including its
normalization of **all** redundant center groups and its sharp coefficient

\[
 C(B,u)=\max\{u,2B+\min(u,B)\}.
\]

It is an internal proof audit, not formal verification, external peer
review, or a publication-priority determination. The result concerns
arbitrary recipient **matroids**, one service per player-resource pair.
The resource-polymatroid extension is a separate theorem with a different
comparison guarantee.

## 1. The invariant really is a current-prefix statement

For every ordered center prefix S, including prefixes ending inside a
layer, the proposed invariant is

\[
 r(W(S)\cup U(S))=r(W(S))+|U(S)|,
\]

where W consists of selected and designated matching recipients of that
prefix, while U contains every other actual matching recipient. These
sets are per resource. Selected and matching occurrences are distinct at
that resource; the assertion does not count the same service twice.

The empty prefix is sound because the actual matching recipients are
independent. The inherited availability of a retained center is also
current: preceding selected records remain identical and preceding
designated groups only lose current matching records. Newly inserted
matching records never inherit an old group flag. Thus its preceding W
can only shrink during its lifetime.

This is stronger than the historical birth-saving assertion refuted in
`general_resource_birth_saving_current_cover_obstruction.md`. That
counterexample is not an inconsistency in the new proof. Its redundant
remaining singleton now triggers an actual free augmentation.

## 2. Completion preserves the invariant, not merely reservations

For a new candidate, a problematic used resource is one whose new owner
lies in the span of all current matching and selected recipients. All
unmarked matching records at such a resource are designated. At a
nonproblematic used resource the new owner is outside that entire span.

Write the old prefix as W,U and let A be the recipients moved from U
to W. Since U is independent over W,

\[
 r(W\cup A)=r(W)+|A|,
 \qquad
 r(W\cup U)=r(W\cup A)+|U\setminus A|.
\]

For unused resources this proves preservation immediately. At a
nonproblematic used resource, adjoining the new owner increases both
ranks on the right comparison by one. At a problematic resource all U
is moved, so the new unmarked set is empty. Old prefixes are unchanged.

The universal all-subsets reservation proof is separately valid. At
problematic resources deleting the new group removes every unmarked
matching recipient; availability then extends a subset of W. At other
used resources the new owner extends any old reservation directly. No
enumeration of selected subsets is needed for either argument.

## 3. Strong freedom follows for a whole earlier prefix

Fix a stored center c, let V contain its preceding W and the current
services of its own group, and suppose its owner p is outside cl(V) at
every used resource. Prefix additivity after c gives

\[
 r(V+p+U)=r(V)+1+|U|.
\]

But r(V+U)<=r(V)+|U|. Hence p is outside cl(V+U), and V+U is precisely
the old matching recipients together with all centers preceding c.
This argument works for empty, singleton, and larger groups.

A fresh free center also has this strong property. If one of its used
resources were problematic and had a nonempty U, its group would not be
empty. If that U were empty, problematic status would contradict the
ordinary availability test.

Thus the algorithm never equates conservative group emptiness with a
necessary characterization of freedom. It can safely act on the
stronger, explicitly tested freedom condition.

## 4. Every retained-prefix exchange is covered

The earliest player-circuit rule sends a nonaugmenting center from
layer i to an outgoing record in layer h<i. Therefore every retained
center precedes the incoming one. Strong freedom applies simultaneously
to all retained prefixes, including internal prefixes of layer h.

For a fixed retained prefix, deleting an outgoing marked service shrinks
W. Submodularity implies that the marginal rank of U cannot decrease
when W shrinks; its old marginal was already |U|, the largest possible.
Deleting an unmarked service instead shrinks U, also preserving
additivity. The incoming service lies outside the span of the entire
old W union U and hence outside the span after either deletion. It is
unmarked, so adding it preserves the required rank equation.

This argument explicitly includes matching records whose groups belonged
to higher, discarded layers. Such records were already in U for the
retained prefix. Releasing their flags is not a new algebraic operation
on that prefix. No uncharged rematching or changed resource identity is
hidden in truncation.

The universal reservations survive as well, because the incoming service
extends every retained reservation even before deletion. Removing a
matching record already excluded by a group's deletion does not
reintroduce it. A replacement record has a new identity and no inherited
layer flag.

## 5. Old maximality and termination remain paid

Below h the actual X and Y records are unchanged. Their resource
availability closures are therefore identical. The existing earliest
player-exchange lemma preserves the corresponding eligibility flats.
At h only a fresh scan is used. The proof does not assume that a local
approximation oracle's answers are monotone under changed availability.

Eager release is an atomic ordinary free exchange and its truncation.
It is not a separate deletion of a selected center, which could increase
the old signature. At h the selected count is unchanged and the blocker
count decreases by one, so the lexicographic micro-signature strictly
decreases. An augmentation instead ends the phase. A normalization
episode that makes exchanges strictly decreases the last-layer index.

Scanning every stored center is necessary: an outgoing matching record
can remove the current rank witness of a center whose own group did not
lose that record. Whole-state normalization still makes only polynomially
many original matroid queries per charged state. Between state changes
there is no indefinite repetition of the same scan. The accepted
rank-composition and positive-growth signature counts therefore apply.

## 6. The sharp cover charge has no missing singleton case

Telescope resource rank over the ordered prefixes, then sum with resource
values. Let t be the current group size of a normalized center.

If the center is one resource worth at least B, every blocker is the
same singleton resource by bundle minimality. Failed normalization means
that the new owner adds no rank after the preceding prefix and those t
blockers. The increment is at most t times that resource value, bounded
by tu.

For a nonsingleton center, every resource it uses is below B. Each
designated blocker shares one of those resources, and hence is also a
nonsingleton. Put a=min(u,B). Every bundle in this star has value below
B+a. For t>=2,

\[
 (t+1)(B+a)\le t(2B+a)
\]

because a<=B<=(t-1)B.

For t=1, failed normalization produces a used shared resource j where
the center adds no rank after the preceding prefix and its blocker. The
rank increment saves at least v_j relative to separately counting the
two services. Minimality gives v(blocker)-v_j<B, so the increment is
strictly below 2B+a. This is a **current** witness, not an old charge.

The groups partition the current blockers, proving the claimed C(B,u).
No assumption of representability, physical disjointness of resource
indices, or small recipient rank is used.

## 7. Quality and positive-error arithmetic

The accepted lower cover argument gives

\[
 \Phi>(T-\tau B)w,\qquad \tau=1/\lambda,
\]

at a completed failed scan. Thus the sufficient exact condition is
tau B+rho C(B,u)<=T, with rho=(r-1)/r. The strict lower bound allows
equality in the upper certificate.

For the arbitrary-size wrapper, set d=tau+3rho and fat threshold
B0=T/d. The reduced rank is at most r and small-unit value u<B0.
At B=B0 the cover coefficient is at most 3B0, establishing factor d.

For requested eta>0 use eta0=min(eta,1) and B=T/(d+eta0). Since d>=1,
B>=B0/2. Consequently

\[
 C(B,u)\le\max\{B0,3B\}=3B,
 \qquad
 T-\tau B-\rho C(B,u)\ge\eta_0 B.
\]

Hence gamma=eta0/16 is smaller than the sufficient positive-growth
threshold Delta/(2C), which is at least eta0/6. The requested
d+eta guarantee follows because the actually achieved ratio d+eta0 is
no larger. The rank exponent is independent of lambda; local-oracle
accuracy costs remain part of the input/work bound.

## 8. Assessment and scope

The root audit found no unclosed step in the new recipient-matroid
invariant, normalization, cover, or complexity argument. It supports
the factor 4-3/r and factor 4-3/r+eta conclusions, with the respective
rank-exponential and rank-quasipolynomial times stated in the manuscript.
The coupled configuration-LP comparator is inherited through the
already audited matroid-union wrapper.

This assessment does not automatically cover arbitrary recipient
polymatroids, an aggregate count LP, uniform near-three quasipolynomial
approximation for two values, or a polynomial-time factor four. Each
requires a separate proof. The original general-matching 4/5 exponent
is not altered by this result.


---

**Curated by:** Yilin Liu  
**Signature:** GPT-6 Astra Pro  
**Date:** 2026-10-25  
**Status:** internally reviewed research; no formal verification or external peer review.
