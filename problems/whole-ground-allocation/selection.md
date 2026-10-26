# Single-exponential corank time for weighted packing through first-violation prefixes

This manuscript strengthens `corank_nonnegative_weighted_packing_extension.md`.
Arbitrary nonnegative rational packing coefficients admit the same
Gamma(t/(t-b))^c parameter dependence as the zero-one batch theorem.
There is no coefficient-ratio parameter. The algorithm is
deterministic; a Bernoulli measure is used only to count its branches.

The key is to enumerate only prefixes that violate a density bound
for the first time. These certificates are prefix-free. Their
weighted counting inequality pays both for the recursion and for an
explicit, polynomial-space certificate enumerator.

## 1. Model and main theorem

Let B be a family of r-element subsets of a finite q-element ground
P. A paid polynomial restriction selector, on Q subseteq P, finds
an I in B contained in Q or certifies that none exists. Set c=q-r.
If B is empty, report failure immediately. Rank-zero families are
handled separately by testing whether the empty set is allowed.

The packing system consists of nonnegative rational rows

```math
\sum_{p\in P}a_{ip}z_p\le u_i,
                           \qquad a_{ip}\ge0,\quad u_i\ge0.
 \tag{WP1}
```

An exact polynomial separation oracle, applied to the queried
vectors, either certifies feasibility or returns a violated row
with a polynomial-bit coefficient vector and capacity. All selector
costs, separator costs, rational input bits, and arithmetic are
included in H. The rows always remain on the original ground P.

Fix rational t>b>0, and put

```math
R=\frac{t}{t-b}>1,
            \qquad \Gamma(R)=\frac{R^R}{(R-1)^{R-1}}.
 \tag{WP2}
```

**Theorem WP.** A deterministic algorithm either returns I in B
whose vector b*1_I satisfies all packing rows, or soundly reports
that no I* in B has t*1_(I*) satisfying them. It has running time

```math
\Gamma(R)^c\mathrm{poly}(H)
                       \le(eR)^c\mathrm{poly}(H)
 \tag{WP3}
```

and polynomial workspace. These bounds hold on unpromised inputs
as well as promised inputs.

## 2. A violated row forces a prefix-density violation

At a recursive ground Q, first call the restriction selector. If it
reports emptiness, fail. Otherwise retain its witness I subseteq Q.
Separate b*1_Q against the original packing system. If feasible,
return I; nonnegative row coefficients make every coordinatewise
smaller vector feasible.

Suppose the separator returns a violated row. Let n=|Q| and
d=n-r, and order the elements of Q by nonincreasing row weight,
using a fixed deterministic tie order. Denote the ordered weights
by a_1>=...>=a_n>=0, set a_(n+1)=0, and write W=sum_j a_j.
The violated capacity satisfies u<bW, so W>0.

If a t-feasible witness I* is contained in Q, its omitted set
D*=Q\I* has exactly d elements and

```math
a(D^*)\ge W-u/t>W/R.
 \tag{WP4}
```

For every prefix length m, let k_m=|D* intersect [m]|. Summation by
parts gives

```math
a(D^*)=\sum_{m=1}^{n}(a_m-a_{m+1})k_m,
       \qquad W=\sum_{m=1}^{n}(a_m-a_{m+1})m.
 \tag{WP5}
```

If k_m<=m/R held for every prefix, (WP5) would contradict (WP4).
Therefore a promised omission set has a prefix with

```math
Rk_m>m.
 \tag{WP6}
```

Equal weights cause no issue: the corresponding differences in
(WP5) are zero. If d=0, the nonempty required omitted weight is
impossible, and failure is sound before any enumeration.

## 3. First-violation certificates

A certificate is a binary word of length m<=n. Its ones mark a set
D of omitted elements among the first m ordered positions. It has
ell>=1 ones and satisfies

```math
R\ell>m,
 \qquad Rk_j\le j\quad\text{for every proper prefix }j<m,
 \qquad \ell\le d.
 \tag{WP7}
```

Thus it crosses the prefix-density threshold for the first time at
its end. In particular its last bit is one. The certificates form
a prefix-free family: a longer certificate cannot have a shorter
certificate as a proper prefix.

For every promised D*, choose its first violating prefix from
(WP6), and take D=D* intersect [m]. This is a certificate, has
ell<=d, and is contained in D*. Consequently deleting D preserves
the promised basis or selected set. The recursion enumerates every
certificate and calls itself on Q\D, returning the first success.
If every candidate deletion fails, it returns FAILURE.

Induction on d proves correctness. A promised parent has at least
one certificate deletion preserving its witness; that child has
smaller corank d-ell and cannot fail by induction. Successful
outputs satisfy the original packing system, and the selector
ensures they remain original members of B. No matroid exchange
property is needed.

## 4. A prefix-free branch inequality

Consider independent Bernoulli bits with success probability p=1/R.
This is solely a counting device; the algorithm draws no random
bits. A certificate with ell ones and z=m-ell zeros has cylinder
probability

```math
p^\ell(1-p)^z.
```

Since its final prefix violates the threshold, z<(R-1)ell. Hence

```math
p^\ell(1-p)^z
      \ge p^\ell(1-p)^{(R-1)\ell}
      =\Gamma(R)^{-\ell}.
 \tag{WP8}
```

The cylinders associated with different certificates are disjoint,
because their words are prefix-free. One may use the ordinary
finite probability space of n bits; no limiting argument is
needed. Summing their probabilities yields

```math
\sum_{D\text{ certificate}}\Gamma(R)^{-|D|}\le1.
 \tag{WP9}
```

Unlike the simpler all-prefix enumeration, this inequality does
not pay an extra factor two in the exponential base.

## 5. An explicit certificate enumerator and its complete local cost

It remains to bound enumeration itself, including branches that do
not produce certificates. For d>=1 define the integer zero budget

```math
Z_d=\lceil(R-1)d\rceil-1\ge0.
 \tag{WP10}
```

Perform a depth-first search of binary words, with at most d ones,
at most Z_d zeros, and length at most n. At every state, first test
the density inequality. If it is violated, output the word as a
certificate and do not extend it. Otherwise append either bit
whose count budget and the length bound permit it. If no extension
is permitted, terminate that local branch. Empty words do not
violate the threshold.

Every required first-violation certificate is enumerated. Indeed,
its ell<=d and its zero count satisfies
z<(R-1)ell<=(R-1)d, hence z<=Z_d. Every earlier prefix has no more
ones or zeros, so the enumerator reaches it. Because the density
test stops at the first violation, it outputs no extraneous
nonminimal prefix.

For a rigorous local time bound, fix a word length m. Any explored
word at that length has k<=d ones and z<=Z_d zeros. Complete it by
appending d-k ones followed by Z_d-z zeros. This injects the
length-m words into the words with exactly d ones and Z_d zeros:
different original prefixes of the same length remain different
after completion. Consequently the number of local search states
over all possible lengths is at most

```math
(n+1){d+Z_d\choose d}.
 \tag{WP11}
```

Since d+Z_d<Rd, the binomial entropy estimate gives

```math
{d+Z_d\choose d}\le\Gamma(R)^d.
 \tag{WP12}
```

The degenerate case Z_d=0 is included by the convention
Gamma(1)=1 in the intermediate entropy expression. Each local
state has polynomial arithmetic cost. Handling an output set,
including constructing the smaller ground and a selector call,
also has polynomial cost per output.

The completion words in the counting argument are not constructed.
In particular, Z_d may have a large binary numerical value, but the
actual enumerator always stops at length n<=q. It stores only its
current word, counts and chosen indices. It does not allocate a
table indexed by Z_d, R, a capacity, or a coefficient magnitude.

## 6. Global runtime, including failed selectors

Let T(d) be the worst total time at remaining corank d, with a fixed
polynomial P(H) large enough to pay all node setup, separation,
sorting, local-state processing and output handling. By
(WP11)--(WP12), the local work is at most P(H)Gamma(R)^d. The
remaining recursive work obeys

```math
T(d)\le P(H)\Gamma(R)^d
              +\sum_{D\text{ certificate}}T(d-|D|).
 \tag{WP13}
```

Every attempted deletion is charged in this expression, including
children whose selector immediately reports emptiness. Such a
child is merely a terminal computation with the nonnegative
budget d-|D|. Thus the bound does not omit rejected candidate work.

The base case satisfies T(0)<=P(H). Inductively use |D|>=1 and
(WP9):

```math
\begin{aligned}
 T(d)
  &\le P(H)\Gamma(R)^d
       +P(H)\sum_D(d-|D|+1)\Gamma(R)^{d-|D|}\\
  &\le P(H)\Gamma(R)^d
                \left(1+d\sum_D\Gamma(R)^{-|D|}\right)\\
  &\le P(H)(d+1)\Gamma(R)^d.
 \end{aligned}
 \tag{WP14}
```

The factor d+1 is polynomial in the original input. This proves
(WP3) on every instance, without assuming that a promised witness
exists. The witness is used only for completeness, not for the
running-time estimates.

The recursive deletion depth is at most c. Each paused local
enumerator has word length at most q and uses polynomial storage;
all levels together still use polynomial workspace. Rational
comparisons Rk>m and the ceiling in (WP10) are made by exact
cross multiplication. Gamma and the Bernoulli probabilities are
never evaluated numerically.

## 7. Resource augmentation and the common-basis cost consequence

For requested capacity inflation 1+epsilon, scale every original
row capacity by 1+epsilon and set t=1+epsilon, b=1. Any original
feasible incidence vector supplies the stronger promise. The
algorithm returns an exact selected set obeying

```math
\sum_{p\in I}a_{ip}\le(1+\epsilon)u_i
                                          \quad\text{for every row }i,
 \tag{WP15}
```

or soundly rejects original feasibility, in time

```math
\Gamma\!\left(\frac{1+\epsilon}{\epsilon}\right)^c\mathrm{poly}(H)
       \le\left(\frac{e(1+\epsilon)}{\epsilon}\right)^c\mathrm{poly}(H).
 \tag{WP16}
```

The restriction selector may include a cost threshold for common
bases of two arbitrary matroids, implemented by weighted matroid
intersection. The one-sided cost-grid optimization in
[Minimum-cost common bases with degree capacities: a corank augmentation scheme](../../manuscripts/allocation-and-scheduling/corank-degree-bounded-common-bases.md) then gives the same
cost-at-most-original-integer-OPT guarantee for arbitrary
nonnegative weighted side rows. Both matroids remain exact and
all weighted side capacities are inflated by only 1+epsilon.
No coefficient-frequency or coefficient-ratio assumption is needed.

## 8. Scope and provenance

The simpler weighted singleton theorem remains correct, but its
factorial dependence is superseded by this first-violation prefix
method. A still simpler alternative that branches over all
ell-subsets of the first ceil(Rell)-1 positions gives
(2Gamma(R))^c time; the prefix-free charge is what removes that
extra factor in the base.

This theorem concerns a fixed-cardinality selection oracle and
nonnegative packing inequalities. Negative row coefficients would
break downward closure and the layer-cake argument, and are not
included. The ability to obtain a polynomial-bit violated row is
part of the input interface. A projection-based or implicit
application must prove that interface independently.

The statement is a complete mathematical algorithm and cost proof,
not a publication-priority claim. A primary-source comparison for
the generic weighted packing parameterization is still required.

---

**Attribution:** Yilin Liu and GPT-6 Astra Pro.
