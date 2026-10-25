# The logarithmic claw factor in the current transversal analysis

**Research boundary note, 25 October 2026. Root mathematical review completed.**

The current-blocker lemma reduces the independent-transversal layer
depth to O(epsilon^{-1} log(q+1)). The retained public signature
analysis still gives the exponent

\[
          O(\epsilon^{-1}\log(2+r/\epsilon)).
\]

This note explains two precise limitations of that proof architecture.
It does not prove an algorithmic lower bound, and it does not rule out
a different adoption rule with a new progress argument.

The relevant constructions are
independent_transversal_current_blocker_growth.md and
independent_transversal_input_linear_iteration_implementation.md.
The public operations and signature are those of Graf--Haxell,
arXiv:1811.02687v2, Sections 4 and 6.

## 1. Increasing mu alone loses the candidate certificate

The current test retains an actual rejected candidate with fewer
than mu times the current selected count in extra selected vertices.
A selected extra can have r-1 independent matching neighbours in
distinct classes. The certificate therefore pays as many as r
additional vertices per selected extra.

For example, a layer may have k selected vertices and about k
current blockers, while its rejected extension adds one new selected
vertex with r-1 fresh matching blockers. If mu k>1, the public
selected-count adoption test can reject this extension. Its candidate
has only one extra selected vertex, but its additional domination
support has size r. This is a legal local star configuration in an
r-claw-free graph. Nothing in the current layer invariants bounds
that r by a constant times epsilon k.

Consequently the existing estimate

\[
 |D\setminus K|
       \le O(\mu r)\sum |X_i|
\]

cannot be made O(epsilon) times the blocker prefix merely by taking
mu=Theta(epsilon) independently of r. The chosen mu=Theta(epsilon/r)
is doing actual work in this proof.

One possible new rule is to adopt whenever the extra candidate
vertex volume

\[
          |Xhat_i\setminus X_i|+|Yhat_i\setminus Y_i|
\]

is a significant fraction of the current blocker count. Rejection
would then give a rank-independent certificate loss directly.
But an adopted candidate could add just one selected vertex and
many blockers. The first negative log-selected coordinate of the
public signature need not decrease by one, while its following
positive log-blocker coordinate can increase. The old lexicographic
proof does not cover this rule.

Using an unrounded integer selected-count coordinate would certify
that one new selected vertex is progress, but would enlarge its
range to the input size. The resulting naive depth-based count is
quasipolynomial in q and does not remove the present obstacle.
No replacement progress argument is proved here.

## 2. A realizable signature family forces the logarithm in this count

There is a stronger counting limitation. Even with the new current-Y
growth and all current graph invariants, the set of possible public
signature vectors can have

\[
                 q^{\Omega(\epsilon^{-1}\log r)}
 \tag{1}
\]

distinct elements. This is a statement about the container counted
by the analysis, across valid inputs and reachable states of that
size. It is not a statement that one input executes all these states.

For clarity take r>=3, mu=rho=epsilon/(100r), and
Q=ceil(1/mu). Start with

\[
       X_1=Q,\qquad Y_1=(r-1)Q,\qquad W_2=1+Y_1.
\]

For each later layer, fix its blocker count by

\[
       W_i=1+\sum_{j<i}Y_j,\qquad
       Y_i=\left\lceil\frac{\epsilon}{5}W_i\right\rceil.
 \tag{2}
\]

Stop after L layers, and let q=1+sum_{j<=L}Y_j. Once q is
sufficiently larger than (r^2/epsilon)^2, this gives

\[
                     L=\Theta(\epsilon^{-1}\log q).
\]

The small integer rounding in (2) changes only constants: W_2 is
already much larger than 1/epsilon.

Independently at every layer i>=2, choose one of r-1 selected counts

\[
       X_i(j)=\left\lceil\frac{jY_i}{r-1}\right\rceil,
                      \qquad j=1,\ldots,r-1.
 \tag{3}
\]

These choices satisfy all the count conditions used by the current
signature proof:

* every selected vertex can have at least one and at most r-1
  blockers, because ceil(Y_i/(r-1))<=X_i<=Y_i;
* noncollapsibility holds with no free selected vertices at all;
* Y_i>(epsilon/10)W_i, the new current-blocker growth;
* X_i>rho sum_{j<i}Y_j, the public birth-selected growth;
* X_i<=QY_(i-1), the active-class cap, since successive Y_i
  increase by less than a factor two after the initial warm layer.

## 3. The count vectors are actual algorithm states

For every choice in (3), make one graph star for each selected
vertex. Partition its layer's Y_i leaves among its X_i centres
in nonempty groups of size at most r-1. There are no graph edges
other than these star edges. The graph has maximum degree at most
r-1 and is therefore r-claw-free for every partition.

Give every leaf its own class. Put each centre of layer i>=2
in a class of a leaf from layer i-1, distributing centres with
at most two per class; the checked X_i<=2Y_(i-1) makes this
possible, and two is below Q. Put the Q first-layer centres in one root
class. These are all classes and vertices. The graph has q
classes and O(q) explicit vertices and edges.

The partial independent transversal consisting of all leaves is
valid and misses only the root class. It can itself be reached by
the outer source algorithm: process the non-root classes first,
with their leaf vertices earlier than their centres in the fixed
vertex order. Each such leaf is immediately available. A non-root
class has at most three vertices, so its first build, even if it
also selects centres, has an immediately addable fraction at least
one third. It collapses immediately, and the fixed order chooses
its leaf. Thus the asserted initial partial transversal is reached.

On the root augmenting call, BuildLayer selects exactly the first
layer's centres and their disjoint blockers. At each later build it
selects exactly the centres in the active previous-leaf classes.
All their blockers are distinct and lie outside the previous
prefix. No centre is free, so no collapse occurs. Every birth and
current-Y check passes through layer L. Reachability here refers to
the stated algorithm, which attempts the new current-Y certificate
only when its growth threshold fails. It does not refer to a modified
algorithm that tries every possible domination inequality at every
state. Thus the resulting vectors
are reachable states of the actual continuing operation sequence,
not merely solutions to isolated numerical inequalities.

The eventual next empty build can return a certificate. That does
not invalidate the preceding reachable state or the counting point.
Different choices in (3) may give different input graphs; this
construction is not an execution-length lower bound.

## 4. The old signature distinguishes all the choices

The negative selected coordinate at layer i is

\[
 -\left\lfloor\log_b
    \frac{\rho^{-i}}{(1-\mu)^{i-1}}X_i\right\rfloor,
 \qquad b=\frac{Q}{Q-\mu\rho}.
\]

Here log b=Theta(mu^3). Consecutive values in (3) differ
multiplicatively by at least 1+c/r for an absolute c, after the
warm layer; its Y_i is already sufficiently large. This change is
much larger than one factor b. Hence these r-1 choices give
different negative signature coordinates. The positive blocker
coordinates are fixed by (2).

The choices at the L-1 later layers are independent, so the
container has at least (r-1)^(L-1) different signatures. This
proves (1). The signatures also obey the source's monotone
absolute-coordinate ordering; that follows from the checked birth
and noncollapsibility inequalities.

Therefore a uniform bound obtained only by counting possible old
signature vectors cannot delete the logarithmic r factor from its
exponent. Using the actual transition sequence, a stronger progress
measure, or a new adoption/collapse rule could still do better.

## 5. Remaining constructive target

The useful possible change is to charge a rejected candidate by
its actual extra selected-plus-blocker volume rather than the
worst-case r times its selected extras. A successful version would
need a new progress theorem covering both types of adoption:
substantial selected growth, and substantial blocker growth caused
by very few selected vertices. It must also handle the public
operation's truncation of all higher layers after adoption.

No such theorem has been obtained in this investigation. The
present current-Y result and its source-signature implementation
remain at the displayed logarithmic claw dependence. The
elementary P exp(O(q)) fallback applies to the same certificate
contract and should be retained independently of this boundary.

## 6. Root review and precise quantifiers

The root checked the geometric blocker inventory, the selected-count
range, cap feasibility, star realization, outer augmentation order,
and separation of the rounded signature coordinates. The construction
is valid for the stated family in which q is sufficiently larger than
the warm-layer parameter size; it is not asserted for every possible
triple q,r,epsilon. Across those valid instances it supplies the
claimed number of distinct reachable signatures while keeping explicit
graph size O(q).

The root also confirms the essential limitation on its conclusion:
different signatures may require different input star graphs. Neither
their existence nor the failure of the present selected-growth
adoption proof shows that one execution takes that many steps. The
note only prevents removing the logarithmic factor by counting the
same whole signature container without additional transition information.

