# Six profiles suffice for exact factor three halves in arbitrary-time scheduling

For arbitrary machine-dependent processing times, six profiles per physical machine suffice for an exact factor-three-halves schedule. Every original job-polymatroid base, binary supply, and one exact assignment-cost budget is preserved, using polynomial space.

## 1. Model and statement

There are q>=1 physical machines. Type j has an integral normalized
monotone submodular recipient rank f_j, with mandatory original count

$$
n_j=f_j(P),\qquad N=\sum_jn_j.
 \tag{SX1}
$$

Eligible pair (p,j) has nonnegative rational processing time ell_pj
and nonnegative rational assignment cost c_pj. An integer schedule
requires x_j in B(f_j) for every j and total assignment cost at most
a supplied C>=0. Additional eligibility masks never reduce n_j.
Let OPT be the minimum makespan of an original budget-feasible schedule.
H includes the binary input and paid polynomial rank, SFM, exact LP
and polymatroid-intersection work.

**Theorem SX.** A deterministic algorithm either detects that no
original budget-feasible schedule exists, even with unbounded load,
or returns a schedule of makespan at most (3/2)OPT in

$$
6^q\mathrm{poly}(H)\text{ time},\qquad \mathrm{poly}(H)\text{ space},
 \tag{SX2}
$$

with all original type totals and the assignment-cost budget exact.
The result is unconditional within this model; q counts all physical
machines, not a structural deficit or a restricted eligible subset.

## 2. The common cost-preserving rounding interface

After any pair mask, the available rank of type j is at most its
original n_j. The requirement

$$
\sum_{p,j}x_j(p)=N.
 \tag{SX3}
$$

therefore forces every type to attain its own original total. Masked
rank loss cannot be hidden by assigning extra units of another type.

For a fractional full-total assignment, construct an integral machine
polymatroid containing it. The intersection with the masked resource
direct sum, and its maximum-total face at N, are integral. Minimizing
actual assignment cost on that face produces an integer full schedule
of no larger cost. One scalar objective preserves the budget; no
integrality claim is made for adding an arbitrary budget row.

The required small-group machine caps use upper-prefix rounding.
Order one group's times v_1>=...>=v_m>=0, set X_h=sum_(i<=h)x_i and
U_h=ceil(X_h), and impose integer prefix caps U_h. Their rank is
max{U_h:e_h in S}, with empty rank zero. This is an integral chain
polymatroid. Summation by parts yields

$$
\sum_iv_ix_i^\prime\le\sum_iv_ix_i+v_1.
 \tag{SX4}
$$

Each disjoint big group below instead has total-count cap one, another
integral polymatroid. All machine groups are combined by direct sum
and rounded jointly with the original resource product. Binary job
counts are not expanded.

## 3. Six exact target-T profiles

Fix T>0 and normalize the following intervals and caps by T. Every
pair outside a machine's permitted groups is forbidden.

Profile 0 allows every time at most 1/2 and caps fractional total
load at 1. It is rounded by one upper-prefix chain, so its integral
load is at most 3/2.

The remaining five profiles have small group [0,1/4]. Each displayed
big group has a separate integer count cap one.

| Profile | Big group 1 | Big group 2 | Fractional small-load cap |
| --- | --- | --- | --- |
| 1 | (1/2, 3/4] | none | 1/2 |
| 2 | (3/4, 1] | none | 1/4 |
| 3 | (1/4, 3/8] | (1/2, 5/8] | 1/4 |
| 4 | (1/4, 3/8] | (5/8, 3/4] | 1/8 |
| 5 | (3/8, 1/2] | (1/2, 5/8] | 1/8 |

All groups in a row are disjoint. Lower endpoints are open and upper
endpoints are closed. In particular a time T/4 is small, a time T/2
is not in a big group starting at T/2, and time T belongs only to a
big interval whose upper endpoint is T.

For each of the 6^q label vectors solve a single exact LP with the
masked original resource constraints, every original mandatory total,
the assignment budget, the big count caps and the displayed fractional
load bounds. A type with insufficient masked rank makes the LP empty;
its original total is never reduced. No separate total-load inequality
is required on profiles 1--5.

## 4. Every feasible profile LP gives a three-halves schedule

On profile 0 use the whole allowed group as one prefix chain. On every
other profile keep the big count-one caps and put a prefix chain on
the small group. The fractional point belongs to this integral machine
polymatroid and to the original resource direct sum at total N.

Use the full-total minimum-cost recovery of Section 2. It returns one
integer assignment preserving all type bases and the exact budget.
The big contribution is at most the sum of big interval upper endpoints.
The small contribution is at most its fractional cap plus 1/4, by
SX4. The five normalized bounds are

$$
\begin{array}{ll}
 \text{Profile 1:}&3/4+1/2+1/4=3/2,\\
 \text{Profile 2:}&1+1/4+1/4=3/2,\\
 \text{Profile 3:}&3/8+5/8+1/4+1/4=3/2,\\
 \text{Profile 4:}&3/8+3/4+1/8+1/4=3/2,\\
 \text{Profile 5:}&1/2+5/8+1/8+1/4=3/2.
 \end{array}
 \tag{SX5}
$$

Big groups are only upper-capped: omitting a big unit only improves
these estimates. No per-type capacity, cost or assignment is split
between independent rounding procedures. All mandatory jobs remain
assigned.

## 5. Complete coverage of every full target schedule

Fix one machine in an original schedule of makespan at most T.
If every assigned job has time at most T/2, profile 0 applies.
Otherwise the machine has a unique job b>T/2.

There can be at most one additional job above T/4. Indeed b together
with two such additional units would have total load strictly above
T. This gives the exhaustive two-large-unit classification used below.

### 5.1 No additional job above T/4

If b is in (T/2,3T/4], select profile 1. Every other unit is small
and its total load is at most T-b<T/2, fitting the small cap.
If b is in (3T/4,T], select profile 2. The remaining total load is
less than T/4, fitting its small group and cap.

### 5.2 Exactly one additional job above T/4

Write its time as a. Since b>T/2 and a+b<=T,

$$
T/4<a<T/2,\qquad T/2<b<3T/4.
 \tag{SX6}
$$

Partition a into (T/4,3T/8] or (3T/8,T/2], and b into
(T/2,5T/8] or (5T/8,3T/4]. Choosing both upper intervals would give
a>3T/8 and b>5T/8, hence a+b>T. That pair is impossible.

The only possibilities are therefore

$$
\begin{array}{ll}
 a\le3T/8,\ b\le5T/8:&\text{profile 3},\\
 a\le3T/8,\ b>5T/8:&\text{profile 4},\\
 a>3T/8,\ b\le5T/8:&\text{profile 5}.
 \end{array}
 \tag{SX7}
$$

All remaining units have time at most T/4. Their total load is at
most T-a-b. The corresponding sums of interval lower endpoints
are 3T/4, 7T/8 and 7T/8, respectively, so the remaining loads fit
the caps T/4, T/8 and T/8 in the table. Boundary times belong to
the preceding interval and remain covered.

This classification is exhaustive and leaves the original schedule
unchanged on every machine. Its resources, mandatory counts and
cost therefore satisfy one enumerated profile LP. It follows that

$$
\begin{aligned}
 \text{target }T\text{ feasible}&\Longrightarrow
       \text{a legal schedule of load at most }3T/2,\\
 \text{every profile fails}&\Longrightarrow \mathrm{OPT}>T.
 \end{aligned}
 \tag{SX8}
$$

The algorithm does not treat weak success as full target-T feasibility.

## 6. Exact initialization and target optimization

Minimum cost over the original resource bases on eligible pairs,
retaining every n_j, decides feasibility with unbounded load. If the
original totals are unavailable or their minimum cost exceeds C,
return infeasibility. Otherwise save an integral feasible schedule
and its finite makespan. When N=0, return the empty schedule.

Test target zero by retaining only zero-time pairs and solving the
same original full-total minimum-cost problem. On success return a
zero-load schedule. On failure, OPT>0, and the profile construction
is used only at positive T.

A positive rational g dividing all positive finite processing times
has polynomial bit length. Every integer schedule load, including
OPT, lies on this grid. Initialize a failed lower endpoint L=0 and
an upper endpoint U equal to the saved feasible load. The initial
saved output has load U<=3U/2.

At grid midpoints, use the full six-profile search. Failure raises L
and maintains L<OPT by SX8. Weak success lowers U and saves the actual
schedule of load at most 3U/2. At adjacent endpoints U=L+g, grid
integrality gives U<=OPT, proving the exact factor 3/2.

No monotonicity of weak successes or additional approximation loss is
used. The initial upper load is at most N times the largest eligible
finite time, so the number of calls is polynomial in the binary
encoding. All-zero processing, empty groups, zero capacities and
masked rank loss are already covered by the full-total tests.

## 7. Complete complexity and scope

The six labels use only constant-denominator thresholds. Each fixed
label vector costs polynomial exact LP, prefix-rank and integral
minimum-cost work. Streaming a radix-six counter and retaining only
the current workspace and best schedule gives 6^q poly(H) total time
and polynomial space after the polynomial number of target calls.

The [bucket curve](../processing-bucket-tradeoff/proof.md) remains useful
at weaker ratios, while the full profile approximation scheme gives
every factor 1+epsilon in 2^{O(q/epsilon)} polynomial time. The special
two-time scheduling theorems retain their smaller, below-two bases
on their restricted processing-time inputs.

The base six is not claimed optimal. The lower bound for factors
strictly below three halves in the full recipient-oracle model does
not establish optimality at the endpoint. Classical cost-preserving
rounding and ordinary fixed-machine approximation schemes are public
background. This manuscript supplies an explicit finite-profile theorem in
the stated full oracle and exact-budget model and makes no publication-
priority or formal-verification claim.

---

**Attribution:** Yilin Liu and GPT-6 Astra Pro.
