# Verification and proof scope

Theorem 2.1 derives the full time--stretch curve from the generic local
interface; Corollary 2.2 instantiates it with the constructed normalized
provider and hierarchy. For <code class="math">U=\log_2(N+4)</code> and <code class="math">h=\log_2(U+4)</code>, the range
<code class="math">t\to\infty</code> with <code class="math">t^2h=o(U)</code> is part of the statement. The work is
an amortized factor multiplying the charged lifetime size.

All five displayed parameter choices are substitutions into that theorem.
The proof also accounts for current-incidence port allocation, degree
reduction, positive internal path lengths, stable roots and numerical
queries. The [source map](../sources.md) links the static sparsifier,
normalized repair, chronological recurrence and deterministic source
algorithms that establish the interface. The complete theorem is ready
for review; there is no executable dynamic APSP implementation in this
repository.

The local nonnegative-integer adapter in Corollary 6.1 is ready for
review. Its floor recovery requires the explicit uniform condition
<code class="math">G(N)n\delta&lt;1</code> for the full stretch, including degree conversion,
throughout the announced lifetime. The fixed perturbation is evaluated
on a predeclared enlarged polynomial length range; exact computation
handles the finite sizes at which its explicit stretch cap is too large.
Every displayed frontier row has subpolynomial stretch, so the adapter
applies. The general family needs the additional <code class="math">t^4h=o(U)</code> condition.
This extension uses that constructed oracle and makes no additional
path-reporting claim.

Read the [main proof](../proof.md) with its [source map](../sources.md). Repository checks validate links, mathematical syntax and catalogue coverage; they do not certify the asymptotic theorem. No proof-assistant verification or external peer review is claimed.
