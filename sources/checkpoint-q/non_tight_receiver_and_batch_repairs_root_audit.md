# Root audit: non-tight receivers and payable potential repairs

**25 October 2026. Mathematical review completed.**

This audit covers `non_tight_receiver_matching_obstruction.md` and
`normalized_bin_potential_batch_repairs.md`. It accepts the explicit
local results, not a new global matching running-time bound.

## 1. A legal gap-one matching state

The physical graph has sixteen vertices, is connected and subcubic,
and contains an odd triangle in the paired remainder. An explicit
augmenting path raises its matching size from seven to eight. The
ordinary top ledger has two copies of c-q-b-r-a, and only a,a' are
contacts to the remainder.

The revised preparation uses exact structural-eligibility caches and
expands only at the first crossing of 4C. After the second expansion,
a transfer a-to-r-to-b reduces b to [2.03C,2.04C]. The endpoint-slack
sum is in [3C,3.015625C]. The positive full-log mass per unit exceeds
1.51/C, while the negative mass is below .493/C, giving the original
raw ratio greater than one half. Its one-sided ratio need only exceed
one quarter, and is about one third near the endpoint. The main note
now states this distinction explicitly.

A final transfer through the large free terminal raises a to
[23C/8,2.9C] with one-sided ratio above one half, keeping b internal.
These are legitimate raw-client preparatory choices; they are not
asserted to be choices of every global source-maximizing policy.
The row sums, bin capacities, lower integral ledgers and all contact
thresholds are explicitly satisfied. No fast preparation bound is
claimed and no structural action is being postponed.

## 2. Persistent prices, exact labels and exhaustion

The incidence rb increases monotonically from C+1 to [3.875C,3.9C]
in steps smaller than .012C. Its third hysteresis reset occurs
before 3.875C, and its fourth would require more than
5.0625(C+1). Thus exactly three occur, its retained register exceeds
2.53C, and its conservative donor price is below .1H/C. No fresh
epoch reset is used.

Bin b offers more than .367H/C. Its path through rb offers more
than .267H/C at a, beating a's direct offer below .261H/C. The qb
donor is large. The fresh exact source tree is therefore rooted
uniquely at b, with r-to-a and q-to-c tight, but r-to-b and q-to-b
non-tight.

Every nontrivial simple old-compatible path is b-to-a or b-to-c.
The former always fails. The latter remains acceptable while
b<=T/10, where T=s_b+s_c. Acceptance implies b<(3/5)c before a
step, and the relative-step rule keeps c>.62T afterward. Thus no
guard intervenes; O(log(L/C)) accepted steps exhaust all old-compatible
paths while b>T/10. The argument permits arbitrary interleaving of
the two components.

The surviving path a-to-r-to-b has a large donor and terminal.
Transferring L/20 is feasible and has normalized positive slack
mass at least L/(58C)>12N, with both negative masses below one.
The fixed semantic excess is also far above 5N. The unavailable
direction is exactly the non-tight receiver r-to-b.

This proves incompleteness of indefinitely frozen-potential
compatibility. It does not obstruct a forest method allowing all
receivers: that method finds the surviving path immediately here.
It gives no lower bound on potential-repair work.

## 3. The exact batch criterion and its conditional budget

Normalizing each row label to the maximum neighboring bin label
only lowers it. Donor inequalities weaken and receiving inequalities
hold. An old tight receiver forces its row label to remain unchanged.
The source constraints and bin-based screen do not change.

For a supplied set S of bins, raise all their labels by an integer
delta and renormalize neighboring rows. Source feasibility is exactly
delta<=A-sigma_u-D_u for u in S. A shifted donor bin covers a row
rise of at most delta automatically. For an unshifted donor v, each
shifted neighboring bin u requires exactly

\[
                    \delta\le D_v+\bar c_{rv}-D_u.
\]

These are all constraints, proving necessity and sufficiency. Since
row degree is at most three, O(vol(S)) touched records suffice to
verify them and update row maxima, the scalar screen, and affected
forest receiving flags. No primal coordinate or register changes.
Repairs occur only between settled numerical transactions.

If every affected bin loses a fixed fraction zeta of its old A-D,
its positive guarded pi decreases geometrically. Fixed degrees and
the bounded range give total update volume
O((m+nu) zeta^{-1} log S) on a fixed ledger. This pays local label
and direction work, not discovering sets, structural lifetimes, or
restarting a separate reachability provider.

For the example, shifting {b,c} by the old price of rb is feasible,
has constant volume, reduces both old pi values by at least a fifth,
and enables r-to-b. Thus the obstruction has a specifically paid
cheap repair.

## 4. Residual balls are correct static primitives

For nonnegative reduced costs, reverse shortest distances to w obey
d(u)<=r_uv+d(v). The clipped cone Delta_v=(R-d(v))_+ consequently
satisfies Delta_v-Delta_u<=r_uv. If the source distance is at least
R, its shift is zero and this cone preserves all constraints.
The polynomial integer scale may be chosen above every guarded
slack. At s_w pi_w>6, R=floor((A-D_w)/2) is then positive and
leaves a strict margin above the rounded terminal price.

If the source is extracted at a smaller radius R_0, the cone of
radius R_0 makes a shortest source-to-w path tight, with positive
score A-D_w-R_0-tau_w. R_0=0 simply supplies an already tight
passing path. Equality at R may use the half-radius branch. Subsequent
row normalization preserves the witness because every row on it
already has a tight receiver.

Only actual changed labels and flags need updating; a whole shortest-
path-tree restart is not part of this primitive. An explicitly
supplied simple path may be installed in a forest by protecting its
inserted edges and cutting a non-path edge from each newly formed
fundamental cycle. This costs its actual length, which is not claimed
to be polylogarithmic.

Reverse Dijkstra may inspect many boundary vertices that receive only
a tiny shift, or a shift tiny relative to their old pi. Neither the
relative-shift budget nor discovering one passing path pays for that
exploration automatically. Efficient discovery and general-graph path
coverage remain unproved; these local lemmas do not change the
accepted general-matching exponent 4/5.
