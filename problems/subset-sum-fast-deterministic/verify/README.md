# Verification of the deterministic Subset Sum refinement

The continuous-domain checker establishes the numerical contact inequalities
used by the refined signed circuit construction. The scalar checker derives
the reflected profile and outer running-time exponent from those contacts.
The energy-tensor check compares finite algebraic identities with independent
enumeration.

| Program | Mathematical scope | Complete command |
|---|---|---|
| [Continuous contacts](../../../tools/verify_subset_sum_contacts.py) | Every legal color, both nonnegative-maximum branches, and every routing branch of all refined contacts | `python tools/verify_subset_sum_contacts.py --all --jobs 4` |
| [Scalar composition](../../../tools/verify_subset_sum_scalars.py) | Exact entropy enclosures, contact-chord envelope, reflected quadratic compensation, and every outer cost inequality | `python tools/verify_subset_sum_scalars.py` |
| [Energy tensor](check_energy.py) | Exact rank-three identities and pruned contractions compared with independent binary endpoint enumeration on dimensions one through four | `python problems/subset-sum-fast-deterministic/verify/check_energy.py` |

All commands are run from the repository root with Python assertions enabled.
They use only the Python standard library. Parallelism changes execution time, not the accepted
inequalities. These programs do not implement the full asymptotic input
algorithm or mechanically verify its combinatorial compiler and reduction;
those arguments are given in the [proof](../proof.md).

## 1. Exact logarithm bounds

Let `Q=2^128` and `D=10^14`. For a positive rational `x`, the checker finds
integers `k` and a rational `v` with `x=2^k v` and `1<=v<2`. With

$$
q=\frac{v-1}{v+1}\in[0,1/3],
\qquad
\ln v=2\sum_{j=0}^{31}\frac{q^{2j+1}}{2j+1}+R,
$$

the tail satisfies

$$
0\le R\le\frac{2q^{65}}{65(1-q^2)}.
$$

Every power, product and division in this calculation uses integer floors
and ceilings on the `1/Q` grid. The same calculation encloses `ln 2`.
Since `ln v>=0` and `ln 2>0`, division by the opposite positive endpoint
gives a valid enclosure for `log_2 v`. Adding `k` exactly and rounding
outward yields integers `l,u` such that

$$
l/D\le\log_2x\le u/D.
$$

For `0<=y<=c`, entropy lower bounds use

$$
H(c,y)=-y\log_2(y/c)-(c-y)\log_2((c-y)/c),
$$

with continuous endpoint value zero. Taking the upper logarithm endpoints
therefore gives a rational lower entropy bound. No floating-point logarithm
can accept a comparison.

## 2. Coverage of the entire color domain

The fixed types are `a=.065`, `b=.075`, `s=.14`, `t=.45`. Write
`beta=a+rho(m-a)` and `c=gamma beta`. The direct branch begins with

$$
m\in[a,s],\qquad z\in[a,\beta(s)],
$$

and enforces the necessary inequalities `z>=m`, `z<=beta`.

For the push branch, eliminating the first color from

$$
\max\{\beta-z,c-m,0\}\le w_1
\le\min\{\beta-m,c/2\}
$$

adds the necessary inequalities `m>=c/2` and `z>=beta-c/2`.
The eliminated color is bounded in the acceptance calculation, rather than
sampled.

For the recursive branch, let `v=w_1-c/2`. The initial interval
`v in [0,c(s)/2]` contains the full feasible range. The checker enforces

$$
v\ge0,\qquad
v\ge\beta-z-c/2,\qquad
v\ge c/2-m,\qquad
v\le c/2,\qquad
v\le\beta-m-c/2.
$$

All these restrictions are affine in `(m,z,v)`. For a constraint
`a_0+sum_i a_i x_i>=0`, compute its maximum on the current rational box
by taking the appropriate endpoint of each coordinate. A negative maximum
proves emptiness. For `a_i>0`, the maximum contribution of the other
coordinates supplies a necessary lower bound on `x_i`; for `a_i<0`, it
supplies a necessary upper bound. Every tightened box therefore contains
every feasible point of its parent. This argument uses the actual coefficient
signs, including families with `gamma rho>2`.

A rejected nonempty box is bisected at the exact rational midpoint of the
coordinate maximizing `3 width(m)`, `width(z)`, `2 width(v)`, in that tie
order. Both children are processed. Empty boxes are discarded only by the
necessary affine constraints. Acceptance of every remaining leaf therefore
covers the original continuous domain, including all boundary points.

## 3. The acceptance inequality

For every rational `p in (0,1)`, the Gibbs inequality gives

$$
H(c,y)\le-y\log_2p-(c-y)\log_2(1-p).
$$

The checker proposes `p` as a multiple of `10^-12`, clamped to
`[10^-9,1-10^-9]`, and uses the exact outward logarithm bounds above.
Any such proposal gives a valid affine majorant. Approximate stationary
points make the majorants tighter; correctness does not require the
proposals to be exact optimizers.

If a positive-entropy majorant is affine in an auxiliary color `w`, then
its coefficient determines which side of the feasible interval can be
substituted. A nonnegative coefficient uses a globally valid affine upper
endpoint, and a negative coefficient uses a globally valid affine lower
endpoint. One endpoint expression is fixed throughout the box. This removes
`w_1` in the push branch, `w_2` in both recursive maximum branches, and
the trace variables `g,u` without adding subdivision dimensions.

Negative entropies use lower vertex interpolants. Joint concavity implies
that the multiaffine interpolation of their exact vertex values is a lower
bound throughout a rectangle; replacing the vertex values by certified
lower bounds preserves that conclusion. If a relaxed rectangular corner is
outside an entropy's domain, the entire negative term uses the safe lower
bound zero on that box.

After these replacements, each relevant branch is multiaffine in
`(m,z,v)`. Maxima and nonnegative sums preserve separate convexity.
Its maximum on the box is consequently attained at a vertex. The checker
evaluates every vertex with exact rational arithmetic and accepts only if
all values are at most the specified contact.

The recursive right degree has two alternative upper bounds: the old
occurrence bound, optionally strengthened by the closed trace correction,
and the continuous pooled-trace bound. The checker first maximizes each
alternative over **the whole box** and then takes the minimum of these
two maxima. A pointwise minimum of different separately convex bounds at
the vertices would not justify this acceptance rule and is never used.

**Certificate proposition.** If a run completes with `status: PASS`, every
selected contact holds throughout its specified feasible color domain,
assuming the analytic circuit and pooled-trace inequalities in the proof.
If it also reports `complete_X02_contact_menu: true`, it has covered all
42 push/recursive calculations and both direct calculations of the refined
menu. Node or depth limits raise an error and do not produce a complete
receipt. The limits cannot cause an unresolved box to be accepted.

## 4. Scalar composition and remaining proof dependencies

For one fixed circuit family, the supremum of
`tau L+(1-tau)R` over its colors is convex in `tau`. Consecutive certified
contacts therefore bound that same family's profile by their chord.
The scalar checker reconstructs the eligible lower envelope, adjoins its
reflected breakpoints, retains both one-sided values, and checks 104 exact
endpoint comparisons for the quadratic compensation inequality. It also
checks the refined type constraints, the initial difference-table size,
the fixed compiler grid, and all outer operation costs at

$$
E=\frac{158153814247997}{318928754919134}.
$$

The reflected contact budget is `S=.4111243`, and the compiler allowance
is `10^-8` on a fixed core-fraction grid of size `10000`. These smaller
allowances use the strict margin of the existing contact certificate;
they do not change its menu, acceptance kernel or saved receipt. The
scalar checker recomputes every affected outer rate.

The proof still supplies the exact signed identities, finite circuit
existence, fixed-data compiler, integer-key reduction, bit-cost accounting,
and indexed witness recovery. The startup constant is finite and independent
of the input; the verifiers do not supply a practical bound on it.

The imported baseline profile wrapper required modules absent from the
provided source and did not supply a self-contained replay of the older
contacts. Historical leaf counts are not used by either reconstructed
verifier. The refined menu is checked directly, without an assumed receipt
for the older parameter setting.

## 5. Completed full run and receipt binding

The committed [full-run receipt](receipt.json) records successful coverage
of all 44 branches: 188,227 accepted nonempty leaves, 376,414 subdivision
nodes, two empty recursive domains, and maximum subdivision depth 29.
The smallest exact acceptance margin is

$$
\frac{136285389119}{128000000000000000000}>10^{-9}.
$$

The proof's contact table gives the individual leaf counts. They are the
counts from this reconstructed run; no historical receipt or reported count
is used to accept a box. Floating-point proposals can affect the subdivision
chosen on a different platform, while every successful run still has to
pass the same exact rational inequalities over the full domain.

To reconstruct the complete certificate and check the new result's binding:

```sh
python tools/verify_subset_sum_contacts.py --all --jobs 4 --output /tmp/subset-sum-contacts.json
python tools/verify_subset_sum_contacts.py --check-receipt /tmp/subset-sum-contacts.json
```

The checker captures the SHA256 digest of its source bytes at startup and
refuses to write a receipt if those bytes change during the run. The receipt
also records a digest of the exact contact menu and all 44 expected
`(rho,gamma,tau,target,branch)` choices.

The inexpensive check of the committed reference result is:

```sh
python tools/verify_subset_sum_contacts.py --check-receipt problems/subset-sum-fast-deterministic/verify/receipt.json
```

This checks the current code and menu fingerprints, complete unique branch
coverage, subdivision-count consistency, and exact recorded acceptance
margins. It is a provenance check; it does not re-evaluate every leaf.
Changing the checker or menu requires a new full run to obtain a matching
receipt. The scalar checker and the energy-tensor check retain their own
separate scopes described above.
