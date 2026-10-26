# Prefix, laminar and sparse quotas

Exact algorithms for structured quota systems and deterministic reductions that retain original items.

**Objective and output**

Decide mixed numeric quotas and recover an exact signed-scalar optimum; kernel rows instead return a smaller original ground with a replacement guarantee.

**Randomness**

Deterministic exact algorithms and deterministic original-ground reductions in the stated exact oracle model; universal colorings are explicitly enumerated rather than sampled.

**Time**

One order <code class="math">2^{O(B)}</code>; two orders <code class="math">2^{O(B\log(B+2))}</code>; <code class="math">p</code> shared weight families <code class="math">2^{O(pB\log(p+2))}</code>; common-weight laminar quotas <code class="math">2^{O(B^2)}</code>, all times <code class="math">\mathrm{poly}(H)</code>. Sparse and support-sensitive refinements appear below.

**Space**

Uniform polynomial binary workspace. Enumerated profiles and universal colorings are streamed.

**Parameters**

<code class="math">B</code> bounds finite targets; <code class="math">B_0\le B</code> is the distinguished root cap; <code class="math">\Delta</code> bounds positive nonroot incidences; <code class="math">C</code> counts distinct support patterns; <code class="math">H</code> is the full encoded input with paid oracle work. Kernel parameters are solution size <code class="math">k</code> and the specified frequency or additional matroid count.

**Model and representation**

One global normalized monotone integral polymatroid with exact rank access. Prefix rows share the stated coordinate orders and weight vectors. Sparse rows require every zero-root coordinate to be zero in every numeric row. Mandatory bases retain their original total; zero-weight coordinates retain their actual scalar costs.

**Lower-bound scope**

Oracle-query and readable-program ETH bounds are stated separately. Frequency-one disjoint weighted equalities already require <code class="math">2^{\Omega(B\log(B+2))}</code> queries. Row-dependent weights have a separate W[2] boundary. The laminar upper and lower exponents are not claimed to coincide.

**Review status**

**Ready for review in the stated scope.** The sharp sparse-packing FPT restriction with improved basis-tree preprocessing, arbitrary signed-profit ordered extension, capacity-sensitive failure budget, exact original-context lower construction, and aggregate laminar reduction to at most B lower rows.

**Conditions and remaining work.** The smaller sparse ground uses explicit FPT preprocessing; it is distinct from the uniform polynomial sunflower tradeoff. These checks do not verify the family’s general valuated completion, universal-coloring construction or lower-bound literature. Original oracles and weights remain available after restriction.

The [verification note](verify/README.md) identifies executable coverage. This status does not claim external peer review or proof-assistant verification.

**Source**

[Formal theorems and quadratic laminar proof](proof.md), [complete companion and reference index](sources.md).

## Exact algorithm bounds

All time bounds include <code class="math">\mathrm{poly}(H)</code>.

**One common order**

<code class="math">2^{O(B)}</code>

**Two common orders**

<code class="math">2^{O(B\log(B+2))}</code>

**One order, <code class="math">C</code> actual supports**

<code class="math">2^{O(\sqrt{B\min\{C,B\}})}</code>

**Two orders, <code class="math">C</code> actual supports**

<code class="math">2^{O(\min\{\sqrt{BC},B\log(2+\min\{C/B,B\})\})}</code>

**<code class="math">p</code> shared weight families**

<code class="math">2^{O(pB\log(p+2))}</code>

**Common-weight laminar family with root cap <code class="math">B</code>**

<code class="math">2^{4B^2+O(B\log(B+1))}</code>

**Root cap <code class="math">B_0</code>, maximum target <code class="math">B</code>, frequency <code class="math">\Delta</code>**

<code class="math">2^{O((\Delta+1)B_0\log((\Delta+1)B_0(B+2)+2))}</code>; in particular <code class="math">2^{O(\Delta B\log(\Delta B+2))}</code> for <code class="math">\Delta\ge1</code>

## Deterministic ground reductions

These constructions are polynomial in the explicit input. The retained original resource oracle and weights remain part of the output model.

**One item matroid and frequency-<code class="math">\delta</code> sparse packing**

<code class="math">k\delta![k(\delta(k-1)+1)]^\delta=O_\delta(k^{2\delta+1})</code>

**The same packing with distinct item supports**

The leading multiplicity factor <code class="math">k</code> is unnecessary: <code class="math">O_\delta(k^{2\delta})</code>

**One arbitrary and <code class="math">d</code> additional coverable matroids**

<code class="math">k\,d![k(1+\sum_i g_i)]^d</code>, for the stated closure-class bounds <code class="math">g_i</code>

**One arbitrary and <code class="math">d</code> explicitly represented transversal matroids**

<code class="math">O_d(k^{2d+1})</code>

**Graph matching with one matroid on edges**

<code class="math">O(k^4)</code> for simple graphs; <code class="math">O(k^5)</code> with parallel edges

**Sparse numeric quotas and valuated completion**

Parameter-bounded positive capacity with all original zero-coordinate completion and signed costs retained

Each reduction preserves replacements against feasible contexts in the original instance. A small retained ground is not a parameter-only bit encoding of an arbitrary oracle.

## Sharper retained size with FPT preprocessing

The [sharp packing theorem](manuscripts/sharp-sparse-packing-fpt-restrictions.md)
gives a different time/size tradeoff for one arbitrary item matroid.

**Unweighted sparse packing**

At most <code class="math">k\binom{\delta k}{\delta}=O_\delta(k^{\delta+1})</code> original
items, with deterministic
<code class="math">2^{O(\delta k\log(\delta k+2))}\mathrm{poly}(H)</code> preprocessing.
This size is worst-case exact for single replacement against every
original feasible context. With <code class="math">q</code> fixed profit values, multiply the
support by at most <code class="math">q</code> to preserve profits exactly.

**Arbitrary signed profits**

At most <code class="math">e^\delta k^{\delta+1}</code> original items with no-worse-profit
replacements, independent of the number of profit values. The deterministic
preprocessing has the same FPT parameter dependence. The exponent is
optimal for original-context replacement at each fixed <code class="math">\delta</code>; the
displayed constant is not claimed optimal.

**Matching with an arbitrary edge matroid**

Retain at most <code class="math">k\binom{2k}{2}</code> edges for unweighted replacement, or
<code class="math">e^2k^3</code> for arbitrary signed profits, including parallel records.
Both use <code class="math">2^{O(k\log(k+2))}\mathrm{poly}(H)</code> oracle time. This
preprocessing is exponential in <code class="math">k</code>; the polynomial-time reduction above
has a larger retained ground.

**Larger packing capacities**

If every feasible context saturates at most <code class="math">h</code> rows, the unweighted
support becomes <code class="math">k\binom{h+\delta}{\delta}</code>; arbitrary profits use
<code class="math">k\Gamma(h,\delta)</code> with the explicit Bernoulli factor in the theorem.
The theorem gives a polynomially computable inverse-capacity load bound
on <code class="math">h</code>. When <code class="math">h\le1</code>, arbitrary signed
profits admit at most <code class="math">(\delta+1)k</code> retained items with uniform
polynomial preprocessing.

For common-weight laminar quotas, aggregate lower demands also reduce
the lower-row system to at most <code class="math">B</code> rows and <code class="math">B+1</code> membership patterns.
This improves preprocessing and catalogue factors while leaving the
stated quadratic exponential upper bound unchanged.

**Attribution:** Yilin Liu and GPT-6 Astra Pro.
