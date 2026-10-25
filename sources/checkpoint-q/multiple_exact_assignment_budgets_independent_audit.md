# Independent audit of the many-assignment-budget obstruction

**25 October 2026. Full independent read of B1--B7 in
`multiple_exact_assignment_budgets_obstruction.md`, with fresh primary
source checks.**

The reduction, fractional gap, and stated deterministic complexity
consequences pass. The obstruction applies when the number of exact
assignment-budget rows is part of the input. It does not establish
the same claims for two fixed budgets or for budget augmentation.

## 1. The one-player allocation is exactly Independent Set

The player matroid U_(1,1) has q=r=1 and corank zero. Every vertex type
has one unit and value one, so its integer count is exactly a Boolean
choice x_v. A budget row x_u+x_v<=1 for each graph edge forbids choosing
both endpoints. Consequently the chosen vertex types form precisely
an independent set, and the single player's utility is its cardinality.

Conversely every independent set supplies an allocation satisfying all
rank and budget constraints. Unused units are allowed, as required by
the allocation model. The transformation therefore preserves feasible
solutions and objective values in both directions, and preserves every
multiplicative approximation ratio. It has a polynomial explicit
encoding and uses only zero-one numerical data. There is no hidden
oracle or binary-supply issue.

Type costs must remain distinct even though all values coincide; the
model permits arbitrary type-dependent budget coefficients. Merging
equal-valued types while forgetting these coefficients would be an
invalid preprocessing step, not a restriction on this reduction.

## 2. The primary inapproximability statement supports the consequence

I freshly opened David Zuckerman's
[*Linear Degree Extractors and the Inapproximability of Max Clique and
Chromatic Number*](https://theoryofcomputing.org/articles/v003a006/v003a006.pdf).
Theorem 1.1 explicitly states NP-hardness of Maximum Clique
approximation within n^(1-epsilon) for every fixed epsilon>0.
Complementing a graph preserves its number of vertices and changes
cliques into independent sets of the same size. The cited theorem
therefore gives the claimed Independent Set baseline.

Under P!=NP, this excludes the corresponding deterministic polynomial
allocation algorithm. A fixed constant-factor algorithm would also
contradict it: above a constant vertex threshold its factor is smaller
than n^(1-epsilon), and below that threshold exact enumeration is
constant-size work. The manuscript's parameter-only consequences follow
because q=r=1 and c=0 in every constructed instance. A time bound
F(q)*poly(H), F(r)*poly(H), F(c)*poly(H), or A^q*poly(H) for fixed A
is then polynomial in the original graph encoding.

These P!=NP exclusions should be read explicitly for deterministic
algorithms, matching this project's positive theorems. Excluding
bounded-error randomized algorithms requires the appropriate stronger
complexity assumption; P!=NP alone is not that assumption. This is a
wording precision, not a flaw in the reduction.

I also freshly opened Doron-Arad, Kulik and Manurangsi's
[*On the PTAS Complexity of Multidimensional Knapsack*](https://drops.dagstuhl.de/storage/00lipics/lipics-vol362-itcs2026/LIPIcs.ITCS.2026.50/LIPIcs.ITCS.2026.50.pdf).
Its Section 1.2 separately discusses the Independent-Set obstruction
when the dimension count is input-sized and distinguishes fixed-dimension
questions. This supports the manuscript's contextual attribution; the
elementary allocation encoding is proved directly here.

## 3. The complete-graph fractional gap is exactly n/2

For K_n, assigning x_v=1/2 to every type satisfies each coordinate cap
and each edge budget. Its fractional value is n/2. Summing all edge
rows counts each variable n-1 times and yields total value at most n/2.
The fractional optimum is therefore exactly n/2, while the integer
optimum is one.

There is only one actual selected player set. The gap is entirely in
integer resource recovery under simultaneous exact budgets, not in
mixing different player bases. The largest individual value is one.
Thus a lower-rounding guarantee (1-epsilon)*FOPT-1 exceeds the integer
optimum whenever n>4/(1-epsilon), proving its impossibility regardless
of available running time.

The projected fractional region remains downward and polynomially
separable. This example isolates the invalid inference: adding more
budget rows to a fractional LP does not justify preserving them all
under the previous one-objective integer rounding theorem.

## 4. The integer-comparator additive consequence also follows

If a deterministic polynomial algorithm supplied OPT/2-1 for these
integer instances, combine it with enumeration of all independent sets
of size at most four. When OPT<4, that enumeration is exact. When
OPT>=4, OPT/2-1>=OPT/4. Returning the larger solution gives a
four-approximation, contradicting the cited baseline under P!=NP.

More generally, a fixed retention alpha>0 and fixed additive loss L>=0
give retention at least alpha/2 once OPT>=2L/alpha. Exact enumeration
below that constant threshold then converts the guarantee to a constant
multiplicative approximation. The fixed additive term cannot rescue an
unrestricted many-budget theorem with only the player ground or corank
as the exponential parameter.

## 5. Scope conclusion

All B1--B7 mathematical claims pass. This is an explicit complexity
reduction plus an unconditional relaxation gap, not a rank-oracle
indistinguishability bound. It does not assert a subexponential lower
bound in the number of resource types, a fixed-two-budget barrier, or
a restriction on algorithms allowing budget violation.

There is no conflict with continuous multicommodity flow retaining many
routing-only budget rows: those algorithms output the fractional routing
itself and do not perform the obstructed integer allocation recovery.
The single-budget positive allocation theorems retain their exact
stated scope.
