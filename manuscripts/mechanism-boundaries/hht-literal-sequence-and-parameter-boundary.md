# A literal sequence lemma and the remaining quantitative spiral boundary

This is a separate source-reconstruction note. It does not alter the
current 4/5 matching construction, which does not use the primitive
examined here. All references below are to the latest arXiv version
checked on 24 October 2026:
[Haeupler--Hershkowitz--Tan, arXiv:2404.13446v2](https://arxiv.org/html/2404.13446v2).
The v2 submission is dated 15 May 2024. The statements discussed here
are present in v2, not merely in the first version.

## 1. The exact quantities

Definitions 5.5, 5.7 and 5.13 use an **hs-length moving cut** for an
(h,s)-sparsity test. A value C(e) increases the current edge length by
hs C(e). Its cost is the capacity-weighted sum of C(e), without the hs
factor.

Definition 5.12 bounds the maximum of outgoing and incoming demand at
each vertex by its node weight. In particular, every A-respecting
demand has total mass at most |A|. Definition 13.1 calls the maximum
mass of an A-respecting, currently h-short demand that the cut makes
farther than hs the cut's demand-size. Definition 13.2 maximizes that
quantity over individual sparse cuts.

Definition 14.2 instead sums the demand-sizes in a **sequence** of
cuts. Every summand is evaluated after earlier length increases, but
the same node weighting A is used throughout. It is neither a sum of
cut costs nor a sequence with depleted node weights.

These distinctions are exactly those needed below.

## 2. An eight-vertex counterexample to the displayed Lemma 14.3

Take K_8 with all capacities and original lengths equal to one, and
set A(v)=7 for every vertex. Set h=1, s=8 and phi=1. Label the vertices
by the binary strings of length three.

For j=1,2,3, partition every block of vertices with a common prefix of
length j-1 into its two next-bit halves. Let C_j(e)=1 exactly on the
edges between those two halves of the same old block, and zero on all
other edges. The three cut supports are disjoint. Their costs are
respectively 16, 8 and 4.

Each C_j is an hs=8-length moving cut. Its affected edges change from
length 1 to length 9. Before round j, every old prefix block is still
a unit-length clique, while every edge joining distinct old blocks
already has length 9.

Inside every old block, choose a perfect pairing between its two
next-bit halves. Orient every pair arbitrarily, and place six units
of demand on it. There are four pairs over the whole graph in every
round, so the demand mass is 24. At each vertex the larger of its
incoming and outgoing demands is six, strictly less than A(v)=7.
Thus even a strict reading of the source's pointwise comparison
symbol causes no issue.

Every chosen pair has current distance one before C_j. After C_j,
any path joining that pair has to cross between two new prefix
blocks. Every such crossing edge has length 9, either because of the
current cut or an earlier cut. The pair is therefore at distance
greater than hs=8. Consequently,

    A_(1,8)(C_j) >= 24,
    spars_(1,8)(C_j,A) <= |C_j|/24 <= 1.

This is a legal sequence under Definition 14.2 with the SAME fixed
A in all three rounds. It proves

    LDSCS(1,1,8) >= 72.

On the other hand |A|=56, and **every single A-respecting demand has
mass at most 56**. Hence, for every value of phi',

    LDSC(phi',2,3) <= 56.

The displayed Lemma 14.3 would assert the reverse comparison 72<=56,
since its transformed parameters are h'=2h=2 and s'=(s-2)/2=3.
No choice of the hidden constant in phi' repairs this example.

This refutes the literal factor-one inequality in that lemma. It is
not a counterexample to the paper's overall decomposition theorem:
a repaired proof could retain an additional demand-loss factor or
use a different epoch invariant.

## 3. The missing factor is visible in the same source

The matching-dispersed demand in Definition 10.6 is scaled by an
arboricity parameter. Lemma 10.7 retains at least 1/(4 alpha) of the
sum of the input demand masses. Lemma 10.8 consequently gives a
factor

    F(s,N) = s^3 log^3(N) N^{O(1/s)}

in the separated-demand guarantee. Applying its constructive
structural conclusion to maximum witnessing demands yields the safe
comparison

    LDSCS(phi,h,s)
        <= F(s,N) LDSC(F(s,N) phi, 2h, (s-2)/2),

with the source's usual harmless adjustments for integral copies and
the moving-cut convention. The factor F cannot simply be deleted:
the displayed proof of Lemma 14.3 cancels it when replacing
|C|/phi' by the sum of the witnessing demands.

The later structural union theorem in
[Bodwin--Haeupler--Hershkowitz--Tan, arXiv:2510.10227v1](https://arxiv.org/html/2510.10227v1)
improves the corresponding loss, but still divides the dispersed
demand by arboricity. It does not supply the factor-one inequality.

## 4. A second literal issue: demand-size need not decrease after a sparse cut

The proof of Lemma 14.4 also uses monotonicity of LDSC during its
epoch. The following example shows that this is not an automatic
consequence of its stated definitions, even when the preceding cut
has maximum demand-size.

Let the graph be K_4 on vertices 0,1,2,3, with unit initial lengths,
node weights A(v)=4, and capacities

| Edge | 01 | 02 | 03 | 12 | 13 | 23 |
|---|---:|---:|---:|---:|---:|---:|
| Capacity | 6 | 5 | 8 | 2 | 6 | 1 |

Take h=1, s=2 and phi=55/78. An hs=2 moving cut has entries
0,1/2,1. Define the first cut by

    C_0(01)=1/2, C_0(12)=1, C_0(23)=1/2,

and zero elsewhere. Its cost is 11/2. It makes 1 and 2 farther than
two: their direct edge has length three and both alternative
two-edge routes have length at least three. Put 39/10 units in each
orientation between 1 and 2. This is strictly A-respecting, has
mass 39/5, and witnesses sparsity (11/2)/(39/5)=55/78.

Initially LDSC(phi,1,2)<=8. Here is a finite proof covering ALL
moving cuts, not just pure cuts. For a fixed cut, form the undirected
graph of original distance-one pairs that it makes farther than
two. Maximizing the demand is a bipartite matching problem with
capacity four on every source and sink copy. Its value is four times
an integer in {0,1,2,3,4}. A value greater than eight requires either
a separated triangle or two disjoint separated pairs.

For a separated triangle every one of its three original edges must
have cut value one. The cheapest triangle has capacity sum nine;
a demand value of twelve would allow cost only 12 phi<9.

For two disjoint separated pairs the pair edges must have cut value
one. Every two-edge alternate route must contain an edge with cut
value at least one half. The minimum possible costs for the three
pairings, including those necessary half-edge cuts, are

    (01,23): 6+1 + (1/2) min(5+6,8+2) = 12;
    (02,13): 5+6 + (1/2) min(6+1,8+2) = 29/2;
    (03,12): 8+2 + (1/2) min(6+1,5+6) = 27/2.

All exceed 16 phi<12. Thus no sparse cut initially has demand-size
greater than eight. The first cut attains demand-size eight under
the source's non-strict load convention, so it is itself a
demand-size-largest sparse cut.

After applying C_0, let C_1(02)=C_1(13)=1 and let its other entries
be zero. Its cost is eleven. Before C_1, both its pair edges still
have length one. Afterwards, both pair distances exceed two. Four
oriented demands of 39/10 each, one in each direction of 02 and 13,
have total mass 78/5 and strictly respect A. Their sparsity is
11/(78/5)=55/78. Therefore

    LDSC_after_C0(phi,1,2) >= 78/5 > 8
                            >= LDSC_before_C0(phi,1,2).

The exact-monotonicity step in the proof of Lemma 14.4 consequently
needs its own repair; retaining only the demand-loss factor from
Section 3 is not a complete reconstruction of that epoch proof.
This remains a statement about the literal intermediate argument,
not a refutation of the top-level theorem.

### The monotonicity issue is not restricted to slack two

The same four active vertices give an even simpler example for any
integer s>=3 within the source's polynomial length range. Retain the
capacities above, but set

    ell(02)=ell(12)=ell(13)=1,
    ell(01)=ell(23)=s-1, ell(03)=2s,
    h=1, phi=11/16, A(v)=4+1/(10s).

The graph of distance-one pairs is the path 0--2--1--3. A cut with
demand-size greater than 2A(v) must separate both 02 and 13. Each of
those direct edges needs cut value one, costing eleven. Moreover,
the original 0--1--2 route has length exactly s and avoids these two
edges. It requires at least 1/s additional cut on an edge of capacity
at least two. Such a cut therefore costs at least 11+2/s, whereas
even a demand of the maximum possible size 4A(v) permits cost only

    phi * 4A(v) = 11+11/(40s) < 11+2/s.

Thus initially LDSC(phi,1,s)<=2A(v). Now apply

    C_0(12)=1, C_0(01)=C_0(23)=1/s.

Its cost is 2+7/s. It separates 12 beyond s: the direct edge has
length s+1 and both alternative relevant paths have length s+1.
Four units in each direction witness sparsity at most phi and
strictly respect A. Its actual demand-size is 2A(v), so it is a
demand-size-largest sparse cut.

After this cut, C_1(02)=C_1(13)=1 has cost eleven and separates both
pairs beyond s. Four units in each of their four orientations give
demand mass sixteen and sparsity exactly phi, again strictly
respecting A. Hence LDSC increases from at most 8+1/(5s) to at least
sixteen. Larger admissible s can be accommodated by a larger declared
polynomial size bound (or unused zero-weight vertices); no
small-slack escape is available for the literal monotonicity claim.

## 5. A separate parameter inconsistency

The proof of Theorem 15.1 prints the recurrence

    s_i = alpha_(s,i)^{O(1/epsilon')}
        = epsilon^{-2} s_(i-1)^{1+O(1/epsilon)},

followed by s_i <= (1/epsilon)^{O(1/epsilon')} after recursion depth
at most 1/epsilon'. The latter does not follow from the displayed
recurrence. For example, a literal upper recurrence

    log s_i <= 2 log(1/epsilon)
                 + (1+c/epsilon) log s_(i-1)

allows log s_i to grow geometrically in i with ratio
1+c/epsilon. A safe envelope derived ONLY from that recurrence is

    log s_i <= (log s_0 + O(log(1/epsilon)))
                   (1+c/epsilon)^{i+1},

not O(log(1/epsilon)/epsilon'). This observation diagnoses an
unresolved index/parameter identification; it does not prove that
the algorithm intrinsically needs the larger envelope.

There is also an interface issue to reconstruct. Lemma 14.1 assumes
one fixed length-approximation alpha_s for all slack inputs up to its
output slack. Lemma 13.4 supplies a length approximation depending
on the slack supplied to that particular call. Their direct
substitution needs an explicit distinction between the child
decomposition slack, the current sparse-cut input slack, and the
epoch comparison slack. These three quantities cannot be identified
merely by renaming each of them s.

## 6. Consequence for the current investigation

The published top-level theorem remains a named theorem. However,
these literal intermediate formulas do not currently support our
independently reconstructed, quantitative inverse-epsilon tradeoff.
Neither a better matching exponent nor a growing-parameter backend
is inferred from the paper's unexpanded exp(poly(1/epsilon)) term.

The next reconstruction must specify a valid epoch invariant with
the demand-loss factor retained, a replacement for the failed
monotonicity step, and all three slack parameters separated. Shared
path-representation questions are independent of this issue and can
still be studied using the explicit splitting, concatenation and
stacking operations of the flow-emulator paper.
