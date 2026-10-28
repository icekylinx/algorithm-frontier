# An exact complete-table realization of the heterogeneous scheduling interfaces

The [reference backend](reference/scheduling.py) gives a finite executable
realization of the semantic interfaces in [Theorem HT](proof.md). Its input
contains the complete rank table of every type on the original physical-machine
ground. All counts are nonnegative integers; times, costs, budget and targets
are exact rational numbers. A separate eligibility mask is represented by
`None` processing times. The tradeoff parameter is an integer at least two.
The backend validates rank normalization, monotonicity and submodularity,
nonnegative numerical data and the two-positive-times-per-machine hypothesis.

## 1. Exact LP and mandatory totals

**Lemma 1.** The backend's bounded LP vertex enumeration realizes feasibility
and linear optimization of every joint resource and machine-cap region it builds.
It retains each original mandatory total after every mask.

**Proof.** For each type, eliminate the coordinate at the last physical machine
by its original base equality. Its value is the original full rank minus the sum
of the remaining coordinates of that type. Include all original subset-rank
inequalities, all coordinate nonnegativity inequalities and a zero upper bound
for every masked pair. This represents exactly the original base intersected
with the mask; a mask cannot replace a required full rank by a smaller one.
All coordinates lie between zero and their original singleton ranks. Thus every
resulting feasible region is bounded, even after eliminating the base equalities.

A nonempty bounded polyhedron has a vertex. At any vertex, active inequality
normals span the reduced ambient space: otherwise a small displacement in both
directions orthogonal to those normals contradicts extremality. Enumerating all
full-size active subsets and solving each square system therefore lists every
vertex, including vertices of lower-dimensional feasible faces. Singular systems
are skipped, and every candidate is checked against every row. Exact Gaussian
elimination uses rational arithmetic. In dimension zero the single empty reduced
vector is accepted exactly when all constant inequalities hold. Linear objectives
attain an optimum at a listed vertex. <code class="math">\square</code>

## 2. Service rows and one integral recovery

**Lemma 2.** `separator` returns a valid normalized nonnegative strict separating
row exactly when the weak service query is outside the nonempty joint service
region. `recover` returns original integer bases whose actual cost is no greater
than the cost of the supplied successful fractional witness.

**Proof.** `node` implements the target mask and all five machine classes in
Theorem HT, Sections 2–4. Zero-time coordinates remain in their original resource
bases and cost row and consume no positive-time cap. The finite singleton-rank
bounds already imposed by Lemma 1 supply the separate zero-time modular boxes.
In particular, a zero-time unit is neither deleted nor made cost-free.

Enumerate the vertices of the underlying joint region before adding the weak
service caps. At any nonnegative normal, a linear objective's support equals
its maximum over those vertices. The outer support LP imposes one support row
per listed vertex, normalizes the normal to sum one, and maximizes the weak
query's support excess. Its capacity variable is bounded below by zero and
above by the largest spare-capacity coordinate. This upper bound contains every
normalized true support value, so it cannot remove an optimal separating row.
The outer LP is bounded and Lemma 1's active-set argument applies to it as well.
A positive excess is precisely a strict nonnegative separating row; nonpositive
excess is membership, by compact convex downward service duality. The empty
underlying-region gate is checked first, independently of this separator.

For recovery, retain every partition and laminar count cap, and replace only an
easy machine's weighted load row by upper-prefix ceilings in its own decreasing
processing-time order. Include every positive prefix, including the full prefix.
The witness belongs to these integer chain/partition polymatroids and the same
original resource direct sum. Their maximum-total intersection face is integral,
as proved in Theorem HT, Section 6 and its cited upper-prefix proof. Minimizing
actual assignment cost on that face therefore gives an integer point at no
greater cost. The implementation enumerates all bounded integer reduced vectors,
tests every resource and recovery row, and selects a true minimum. It does not
assume that adding the budget row preserves integrality: that row is removed
before recovery. The recovered point still obeys the budget because its cost
is no greater than the witness's. Every mandatory type total remains exact by
Lemma 1. Theorem HT's per-class load bounds apply. <code class="math">\square</code>

## 3. Complete target search and scope of its time

**Proposition 3.** For every accepted finite input, `optimize` either detects
original-total or budget infeasibility, or returns the approximation guaranteed
by Theorem HT with the budget and all original bases exact. Its implementation
uses the following explicit-table enumeration costs, rather than Theorem HT's
fast running time.

**Proof.** Enumerating original integer bases and minimizing cost first detects
unbounded-load infeasibility or supplies a legal finite upper schedule. The
zero-target mask tests zero makespan exactly with the original mandatory totals.
For a positive target, enumerate all subsets of the current role ground, testing
the weak joint LP and recovering an integer schedule at its first success.
If a full target schedule exists, choose the subset consisting exactly of its
large recipients in the role class. The unchanged schedule survives every mask;
its full spare quotas dominate the weak quotas on that subset. Every non-role
machine satisfies its prescribed full-target caps. This supplies a feasible
weak query, so total failure soundly excludes the full target. Every success
satisfies the per-class approximation bounds by Lemma 2.

The common denominator and integer gcd of positive processing times give an
exact load grid. Initialization saves the actual upper schedule. At each grid
midpoint, failure raises a strictly infeasible lower endpoint, while weak success
lowers the upper endpoint and saves its actual output. At adjacent endpoints,
the upper nominal target is at most the integer-grid optimum. The saved output
therefore satisfies the claimed approximation. No monotonicity of weak successes
is required. This is exactly Theorem HT's one-sided optimization argument.

For explicit costs, let <code class="math">q</code> be the machine count,
<code class="math">m</code> the type count, and
<code class="math">D=m(q-1)</code> the reduced LP dimension. Write
<code class="math">L</code> for a given LP's actual number of rows. An LP vertex
enumeration inspects at most <code class="math">\binom{L}{D}</code> square systems,
with polynomial rational work per system and feasibility check. Original
rank-table validation takes <code class="math">O(m4^q)</code> table comparisons.
An integer recovery or initialization inspects at most
<code class="math">\prod_j(n_j+1)^{q-1}</code> reduced integer vectors. A target
uses at most <code class="math">2^q</code> weak LP/recovery attempts, and target
search uses polynomially many calls in the binary length of the upper load/grid
index. These counts include target-dependent masks, not just successful queries.

The optional support routine lists the underlying LP vertices and then enumerates
an outer LP of dimension <code class="math">&#124;Q&#124;</code>, with one support row per
listed vertex and <code class="math">O(&#124;Q&#124;)</code> other rows. All stored rational
coordinates have bounded bit length by rational determinant bounds, but storing
all vertices may require exponential space. Numeric count-vector enumeration
is not polynomial in binary multiplicities. There is no unit-copy construction;
these explicit enumeration costs are nevertheless real and are charged here.
Neither the fast weighted omission recursion nor the streamed global cover is
implemented by this backend. Their asymptotic proof remains Theorem HT's
separate mathematical dependency. <code class="math">\square</code>

## 4. Independent finite evidence

[check_scheduling.py](verify/check_scheduling.py) independently enumerates all
original pair counts using singleton-rank bounds, checks every original subset
rank, and computes actual costs and loads. It does not call the backend's row
builder, coordinate elimination, integer enumerator or cost/load helpers for
this oracle. It compares target failures, successful outputs and optimized
approximations against those original schedules. It also checks every enumerated
weak LP vertex's joint recovery, normalized support rows and the scaled
protected-omission inequality on finite instances. The test includes all machine
classes, unequal role quotas, rational fractional vertices, nonmodular ranks,
zero-time costs, infeasible masks, zero-dimensional reduced LPs, and three-machine inputs.

These are finite executable checks of this explicit-table realization. They
neither prove Theorem HT by enumeration nor certify its polynomial value-oracle
implementation, fast running time, or external/formal verification.

**Attribution:** icekylinx and GPT-6 Astra Pro. Apache-2.0.
