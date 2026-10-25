# Weighted exact-distance covers and equal-rate variable ownership

Author: Yilin Liu. Assistance: OpenAI Codex, including GPT-6 Astra.

All logarithms are binary, and $O^*$ suppresses polynomial factors in the coordinate count and the binary input length. The layout arity used below is the fixed integer four.

The inherited strict-extraction, local trace/contrast, prime/cover and ordered-stream interfaces are proved in [the manuscript](../../../problems/subset-sum-low-space-deterministic/proof.md), Sections II.1, II.2, II.4–II.7. The new combinatorial constructions and their cost bounds are proved below.

The structural result applies to arbitrary indexed integer weights on a top core of size $a$, with $N$ distinct subset sums and deficiency $d=a-\log N$. For the dense branch, use $a=.9m+O(1)$, $p=1/20$, and $d/a\le17/2000+O(1/m)$. It supplies complete representations, owner lists, exact compatibility checking and actual-profile allocation with these bounds:

$$
\begin{aligned}
T_{\rm owner}&=O^*(2^{3a/2+2d}),&
S_{\rm owner}&=O^*(2^{a/2}+2^d),\\
T_{\rm container}&=O^*(2^{.3825m}),&
S_{\rm construction}&=O^*(2^{.1275m}),\\
S_{\rm assignment/index}&=O^*(2^{.265185m}).
\end{aligned}
\tag{EV-1}
$$

Every parent retains movable top/background logarithmic mass at least $m/2-O(\log m)$. Its upper mass is the central equal-rate budget, up to polynomial factors. Exact incidence is bounded by $2^{3m/2}$ times a polynomial whenever the original local full-block deficiency is at least $d$. The proof does not assume central canonical distance, dense fine profiles, nonnegative weights, or unique representations.

## 1. Direct coefficients and the exact association identity

Let $H$ be the owner-right region of cardinality $b$. For an original top subset $S$ and variation mask $R$, use

$$
(\alpha_i,\beta_i)=
\begin{cases}
(S_i\oplus R_i,\ R_i(2S_i-1)),&i\notin H,\\
(R_i(2S_i-1),\ S_i\oplus R_i),&i\in H.
\end{cases}
\tag{EV-2}
$$

The coordinate sum is $S_i$. The left top weight is
$w(S\setminus H)+w^{S\oplus H}(R)$, where $w_i^G=(-1)^{G_i}w_i$.
Thus the parents use original coefficient weights; no outer top offset is introduced. A compatible pair is exactly one with binary coordinatewise sums.

Choose one canonical full mask $X$ for each distinct original top sum, and denote this family by $\mathcal F$. For a given $S$, let $N_j(S)$ count its canonical witnesses at Hamming distance $j$. Fix integers $b,u,v$ with
$0\le u\le a-b$, $0\le v\le b$, and $j=b+u-v$. Set

$$
Q=\binom{a-b}u\binom bv,\qquad
c(S,H)=\#\{X\in\mathcal F:
 |(X\oplus S)\setminus H|=u,\
 |(X\oplus S)\cap H|=b-v\}.
\tag{EV-3}
$$

For $R=X\oplus S\oplus H$, the required variation quotas are $u,v$.
For fixed $H$, its signed sum equals
$w(X)-w(S\oplus H)$, so canonical contributions remain distinct.
Consequently $c(S,H)$ is a lower bound on the actual signed quota-image size and $c(S,H)\le Q$.

Counting the same pairs $(Y,H)$, with $|Y|=j$, in two orders gives

$$
\binom aj\binom ju\binom{a-j}v=\binom ab Q,\qquad
\frac1{\binom ab}\sum_{|H|=b}c(S,H)
 =\frac{N_j(S)Q}{\binom aj}.
\tag{EV-4}
$$

Choose a distance band $I$ by the integer condition
$\sum_{j\notin I}\binom aj\le N/2$.
For every $S$, some $j\in I$ then has
$N_j(S)\ge N/[2(a+1)]$. All distances in the band are enumerated.

## 2. A weighted owner cover

For a fixed distance and quota configuration, put $C_0=2(a+1)$,

$$
\mathcal E=\{S:C_0N_j(S)\ge N\},\qquad
M=\frac{NQ}{C_0\binom aj},\qquad
L=1+\lfloor\log Q\rfloor.
\tag{EV-5}
$$

Configurations with $M>Q$ have empty eligible universe. Otherwise maintain pairs $(H_i,\ell_i)$, with $0\le\ell_i<L$, and the implicit uncovered set
$\mathcal U=\{S\in\mathcal E:c(S,H_i)<2^{\ell_i}\text{ for all earlier }i\}$.
When $\mathcal U\ne\varnothing$, choose $H$ satisfying
$\sum_{S\in\mathcal U}c(S,H)\ge M|\mathcal U|$.
For $r_\ell=\#\{S\in\mathcal U:c(S,H)\ge2^\ell\}$, the inequality
$c\le\sum_{2^\ell\le c}2^\ell$ gives some threshold with
$2^\ell r_\ell\ge M|\mathcal U|/L$. Choose a maximizing threshold and append that pair.

Charge $2^{-\ell}$ to the pair. If it removes $r$ of the $U$ current elements, its charge is at most $Lr/(MU)$. Summing this through successive removals is bounded by a harmonic sum:

$$
\sum_i2^{-\ell_i}\le\frac{L H_{|\mathcal E|}}M
 \le\frac{L(1+a\ln2)}M,\qquad
K:=\#\{i\}\le\operatorname{poly}(a)2^d.
\tag{EV-6}
$$

The last inequality uses $2^{-\ell_i}\ge1/Q$ and
$\binom aj\le2^a$. Grouping pairs by threshold yields, for each group,

$$
\frac{K_\ell Q}{2^\ell}
 \le\operatorname{poly}(a)\frac{\binom aj}{N}.
\tag{EV-7}
$$

Every eligible pattern succeeds in at least one group. Completeness uses enumeration of all groups; it requires no group that succeeds for every pattern.

Here is a low-state implementation of the owner choice. A prefix fixes owner-one coordinates $F_1$, owner-zero coordinates $F_0$, and leaves $W$ unfixed. It has
$B_P=\binom{|W|}{b-|F_1|}$ completions. For a mask $Y$, put
$z_1=|Y\cap F_1|$, $z_w=|Y\cap W|$. The number of these completions giving the prescribed quotas is zero unless $|Y|=j$, and otherwise equals

$$
k_P(Y)=
 \binom{z_w}{b-v-z_1}
 \binom{|W|-z_w}{b-|F_1|-(b-v-z_1)}.
\tag{EV-8}
$$

Infeasible binomial arguments mean zero. The mean total trace over the prefix's completions is

$$
A_P/B_P,\qquad
A_P=\sum_{S\in\mathcal U}\sum_{X\in\mathcal F}k_P(S\oplus X).
\tag{EV-9}
$$

The current mean is the completion-count-weighted average of the feasible next-bit means. Exact cross multiplication therefore chooses a child with no smaller mean. Starting from (EV-4), $a$ choices produce the required owner. The uncovered set is kept fixed throughout these prefix choices.

Partition coordinates computationally into halves of sizes $\lfloor a/2\rfloor,\lceil a/2\rceil$, independently of ownership. Write $S=(s,z)$, $X=(x,y)$. For fixed $s$, scan $\mathcal F$ and group its low masks $y$ by the three high-part counts of $x\oplus s$ in $F_1,F_0,W$. There are polynomially many arrays of length $2^{\lceil a/2\rceil}$. For each high-count triple, form the low kernel by inserting its counts and the low-mask counts into (EV-8). Summing their XOR convolutions gives every value
$\sum_X k_P((s,z)\oplus X)$ for that $s$.

A Walsh transform computes each convolution exactly: apply the butterflies $(x,y)\mapsto(x+y,x-y)$, multiply the transforms pointwise, apply the transform again, and divide by its length. Character orthogonality proves exactness. The counts and intermediate values have polynomial bitlength. Grouping by high distance similarly computes $N_j((s,z))$; grouping by the two high quota counts computes $c((s,z),H_i)$ for any previous pair. Retain the eligibility/uncovered Boolean array for this $s$, and process previous pairs sequentially.

The canonical scan itself sorts the two half-subset occurrence lists and heap-merges their pair-sum rows. Process each equal-weight run completely, retaining only its smallest full mask. It costs $O^*(2^a)$ time and $O^*(2^{a/2})$ state per reset, including repeated and negative sums. For each $s$, its scan dominates the polynomially many low transforms. Enumerating all $s$, a prefix score, termination test or threshold count costs
$O^*(2^{3a/2}(1+K_{\rm old}))$ time and
$O^*(2^{a/2}+K_{\rm old})$ state.
Summing over the $K$ choices proves the first line of (EV-1).

Finally, for $t=j/a-1/2$, binomial upper bounds turn (EV-7) into

$$
\log Q-\ell+\log K_\ell
 \le d-aD(t)+O(\log a),\qquad
D(t)=1-h(1/2+t).
\tag{EV-10}
$$

Owner construction precedes common-prime selection. Its sufficient canonical predicate is replaced downstream by the actual signed quota image.

## 3. Equal variation rates on unequal owner regions

Fix $p=1/20$. For an exact distance $j$, set

$$
t=j/a-1/2,\qquad z=\frac{t}{1-2p},\qquad
b=a(1/2+z),\qquad
u=p(a-b),\quad v=pb.
\tag{EV-11}
$$

Then $b+u-v=j$, the total variation radius is $pa$, and the ideal natural quota entropy is $a h(p)$, independent of $t$.
Round $b$, round $u=p(a-b)$, and define $v=b+u-j$. This preserves the distance exactly and changes all counts by $O(1)$. On the active band $|t|\le.06$, both owner regions and both quota fractions have fixed positive interior margins, so rounding changes logarithmic estimates by $O(\log a)$. Thus

$$
\log Q=a h(p)+O(\log a),\qquad u+v=pa+O(1).
\tag{EV-12}
$$

The band exists for every original pattern: strict extraction does not increase density, so $d/a\le.0085+O(1/m)$, whereas the positive entropy series and $\ln2<52/75$ give

$$
D(.06)\ge\frac{2(.06)^2}{52/75}
 =\frac{27}{2600}>\frac{17}{2000}.
\tag{EV-13}
$$

The binomial tail outside the band is at most
$2(a+1)2^{a h(.56)+O(1)}$, hence is below $N/2$ after a fixed coordinate cutoff. The algorithm uses the exact integer tail comparison rather than an entropy oracle.

## 4. Variable containers and equal sided degrees

The following primitive is deterministic. A zero support uses one empty container. On $n$ coordinates, with ternary support size $k$ and container length $l\ge2k$, let
$N_k=\binom nk$, $A_k=\binom lk$, $p_k=A_k/N_k$. Choose

$$
\nu=\left\lceil16(n+1)/p_k\right\rceil,\qquad
L_k=\lceil4\nu p_k+8(n+1)\rceil.
\tag{EV-14}
$$

A multiset of $\nu$ containers can cover every support while giving each support fewer than $L_k=O(n)$ containing indices. For independent random containers, the potential
$\#\{\text{uncovered supports}\}+\sum_B2^{\deg(B)-L_k}$
has expectation
$N_k(1-p_k)^\nu+N_k2^{-L_k}(1+p_k)^\nu<1$.
Fix one container at a time by minimizing its exact conditional expectation. After $i$ choices that expectation is

$$
(1-p_k)^{\nu-i}U_i+
2^{-L_k}(1+p_k)^{\nu-i}\sum_B2^{d_i(B)}.
\tag{EV-15}
$$

For a proposed next container and $s=\nu-i-1$, comparisons use the common-denominator integer score
$2^{L_k}(N_k-A_k)^sU_Y+(N_k+A_k)^s\sum_B2^{d_Y(B)}$.
Its bitlength is $O(n\nu)$. Since
$N_k/A_k\le(n+1)(5/4)^n$, schoolbook arithmetic, a scan of all supports for each candidate, and all rounds cost at most
$O^*(2^{2n}\nu^3)=O^*((125/16)^n)<O^*(2^{3n})$.
Support flags/degrees, selected containers and the large operands occupy $O^*(2^n)$ state.

For every selected container $Y$ and binary assignment $s$ on $Y$, use the rectangle consisting of binary $x$ with $x|_Y=s$, and ternary $y$ supported on a $k$-subset of $Y$ with $y_i=(-1)^{s_i}$ on that support. All pairs have binary sums, and every compatible pair is covered. Binary degree, ternary degree and tuple count are respectively

$$
O^*(N_k/A_k),\qquad O^*(2^{l-k}),\qquad O^*(N_k2^l/A_k).
\tag{EV-16}
$$

Build a support-to-container index by enumerating each container's $k$-subsets. Its length is $\nu A_k=O^*(N_k)$, with polynomially many indices per support. A ternary query enumerates just these indices and the permitted assignment extensions. This realizes the degree bound as an actual query-time bound.

For the two owner regions, take $t\ge0$ by reflection and write
$n_\pm=a(1/2\pm z)$, $k_\pm=pn_\pm$.
Set $h=h(p)$, $g=h-3p>0$. Initially use container length $2k_\pm$. The full right degree exceeds the left by $C=2zag$. Enlarge the plus-region container by $w$, keeping the minus-region length unchanged. Define

$$
E(l,k)=l[1-h(k/l)],\qquad
2w-E(2k_++w,k_+)=C.
\tag{EV-17}
$$

The binary degree on the enlarged region decreases by $w-E$, while its ternary degree increases by $w$. Thus (EV-17) equalizes the full parent degrees.

On the active range $p=1/20$, $|t|\le.06$, we have
$z\le1/15$. The entropy bound $h(.05)<.2864$ gives $g<7/50$, so

$$
\frac C{k_+}
 =\frac{2z}{1/2+z}\frac gp
 \le\frac4{17}\frac{14}5=\frac{56}{85}.
$$

For $l\ge2k$, differentiation gives
$E(2k,k)=E_l(2k,k)=0$, $0\le E_l<1$, and
$E_{ll}=k/[(\ln2)l(l-k)]$.
Hence $E(2k+w,k)\le w^2/(4k\ln2)$.
The left side of (EV-17) is strictly increasing with derivative greater than one. At $w=3C/4$,
$E\le63C/(680\ln2)<C/2$, using $\ln2>1/2$;
thus its value exceeds $C$. The unique root satisfies
$0\le w\le3C/4$, and its container fits with fixed slack:

$$
2k_++w\le(2+42/85)k_+=\frac{53}{425}n_+<n_+.
$$

Both complete checker degrees and the global assignment table therefore have logarithmic bounds

$$
D_{\rm side}=\frac a2[h(p)-p]+\frac E2+O(\log a),
\qquad
\log N_{\rm tup}=a h(p)+E+O(\log a).
\tag{EV-18}
$$

The positive binary-entropy series gives $D(t)\ge2t^2/\ln2$. Combining this with the curvature bound proves, for $t\ne0$,

$$
\frac{E}{2aD(t)}
 \le\frac{9g^2}{32p(1-2p)^2}
 \le\frac{49}{360}<\frac38.
\tag{EV-19}
$$

At $t=0$, use the original containers and $E=0$.
Integer container lengths bracket the monotone degree crossing. Expanding entropy at rational arguments converts each sign test to a comparison of integer powers with polynomial bitlength. Rounding an interior length changes exponents by $O(\log a)$; actual polynomial load caps are retained.

## 5. Elementary support-balanced tensorization

To avoid a full-region container construction, fix $q=4$. For a support $R$ on an $n$-coordinate owner region, remove a residual set $T$ containing $|R|\bmod4$ supported and $(n-|R|)\bmod4$ unsupported coordinates. It has at most six coordinates. Enumerate every such $T$ and its support pattern. The remaining total and support cardinalities are divisible by four.

For any ordered even-size coordinate set with an even support, consider every cyclic interval containing half the coordinates. Its support count changes by at most one when the interval advances by one position. The opposite interval has the complementary support count. Discrete intermediate value therefore gives an interval with exactly half the support. Apply this twice: first divide the remaining region into two equal coordinate/support halves, then divide each half likewise. The four regions have equal coordinate counts and equal support counts.

Enumerating all cyclic choices at these three nodes gives a polynomial family. Every support is balanced by some branch, with no external layout theorem. The residual coordinates remain explicit in all coefficient vectors and actual sums. Their checker enumerates binary assignments, with ternary signs forced on the fixed residual support; its cost is constant.

Suppose the original container ratio is $\gamma=l/k$. In each regular subregion, set $l_i=\lceil\gamma k_i\rceil$. On the active range $k/n$ is bounded away from zero and $1/2$, $l/n$ is bounded below one, and $l/k$ is bounded. Thus all four lengths are feasible after a fixed cutoff. Removing finitely many coordinates and rounding four lengths gives

$$
\begin{aligned}
\sum_i l_i&=l+O(1),&
\sum_i k_i&=k+O(1),\\
\sum_i n_i h(k_i/n_i)&=n h(k/n)+O(\log n),&
\sum_i l_i h(k_i/l_i)&=l h(k/l)+O(\log n).
\end{aligned}
\tag{EV-20}
$$

The tensor rectangles preserve (EV-16) and (EV-18) up to polynomial factors. Their support indices realize the same sided degrees. Construction runs on regions of size $n/4+O(1)$, so it takes
$O^*(2^{3n/4})$ time and $O^*(2^{n/4})$ construction state. The full assignment table, its initialization and clearing structure remain separately charged.

In the active band, $|z|\le1/15$, so the larger owner region has at most $.51m+O(1)$ coordinates. Construction therefore has exponents $.3825m$ and $.1275m$. Exact entropy enclosures
$h(.05)<.28639696<.2864$ and $D(.06)<.011$, together with (EV-19), give

$$
a h(p)+E
 < .9m[.2864+(3/4)(.011)]+O(\log m)
 =.265185m+O(\log m).
\tag{EV-21}
$$

This includes the tuple table and support incidence indices.

Choose each local useful cardinality layer, balanced layout and child role from its physical integer image before common-prime selection. Full selected-support size at least its Good threshold gives a useful physical layer/layout after a polynomial loss in the coordinate count alone; this supplies the local contrast bound independently of the bitlength of the input weights. Include all such enumerated local images in the common-prime universe, together with the global exact-quota top images. Keep the selected local images and child roles fixed throughout the following top refinement. Once the common prime path makes the global top image good, retain one variation witness per occupied top residue; each witness belongs to some residual/cyclic-layout branch. A polynomial pigeonhole leaves one branch with a reciprocal-polynomial fraction of these residues. Repeat for finer top count profiles if needed. The algorithm enumerates every branch, and the eligibility allowance includes these polynomial losses. Local images remain fixed.

The local prime scan still has a paid bound. Enumerate each Good selected set outside the signing loop, so its membership test is performed once. The translate-cover bound gives $K|{\rm Good}|\le\operatorname{poly}(n)2^c$. For each signing and Good set, enumerate the polynomial family of physical layers/layouts and their images in $O^*(2^r)$ time each. Thus all local candidate scoring costs $O^*(2^{c+r})$, with sequential image workspace; this scan is shared across the outer top labels. For the active $r=.45c+O(1)$, $c\le m$, maximum modulus exponent $.45m$ and prime depth 16, the preparation exponent is at most $1.45+.45/16=1.478125<1.5$. Only polynomial factors in the actual input bitlength are suppressed. The selected physical images retain their coordinate-only cardinality guarantees even when the modulus density allowance depends on that bitlength.

## 6. Clamping actual profiles with all background coordinates

For an actual top profile, let $P_-,P_+$ be its support-position products, with logarithms $h_-,h_+$. Let $r=u+v$. The exact raw top-domain logarithms are

$$
L_L=n_-+h_++v,\qquad
L_R=n_++h_-+u,
\qquad
M_{\rm total}=m+h_-+h_++r.
\tag{EV-22}
$$

These use actual products, including sparse profiles. Since
$P_-P_+\le Q$, take the exact upper cap

$$
M_{\rm cap}=\frac{m+\log Q+r}{2}.
\tag{EV-23}
$$

Choose $M_j\in[\max(m/2,L_j),M_{\rm cap}]$ with sum $M_{\rm total}$. Then $z_j=M_j-L_j\ge0$ are background counts summing to $m-a$. The interval conditions follow as follows. The upper-sum condition is $M_{\rm total}\le2M_{\rm cap}$, from $P_-P_+\le Q$. The sum of the two lower bounds is handled by four cases. The both-$m/2$ case uses $M_{\rm total}\ge m$; the both-$L_j$ case uses $m\ge a$. The two mixed cases follow from
$m/2\ge(1-p)n_+$ up to bounded rounding. Each individual upper bound exceeds its raw lower bound when the following two inequalities hold with fixed slack:

$$
m-a\ge2|z|[1-h(p)-p]a,\qquad
m-a\ge[2|z|(1-p)-p]a.
\tag{EV-24}
$$

The first proves $L_j\le M_{\rm cap}+O(\log a)$, using
$h_\pm\le n_\pm h(p)+O(\log a)$; the second proves the mixed lower-sum cases. Also $M_{\rm cap}\ge m/2$.
With $p=.05$, $|z|\le1/15$, $a=.9m+O(1)$, their right sides are respectively less than $.08m$ and at most $.069m$, whereas $m-a=.1m+O(1)$. Thus every profile has a feasible interval pair after a fixed cutoff.

The allocation is exact and does not evaluate real entropy. Binary-search the first integer $z_L\in[0,m-a]$ satisfying the appropriate lower interval bounds; square products to compare $2^{z_L}2^{L_L}$ with $2^{m/2}$ or the cap. The cap comparison uses the integer $2^{m+r}Q$. Choosing a nearest feasible integer pair changes each logarithmic bound by at most a constant. Accordingly,

$$
M_j\ge m/2-O(1),\qquad
M_j\le\frac{m+a[h(p)+p]}2+O(\log a).
\tag{EV-25}
$$

The fixed slack in (EV-24) absorbs the binomial and quota-rounding corrections. Every one of the $m-a$ background coordinates is assigned.

Combining (EV-23) with the actual-quota form of (EV-18) gives
$M_j+D_{\rm side}\le m/2+\log Q+E/2+O(\log a)$.
For original local full-support deficiency $d_j$, the ambient count after the natural top modulus and summing the threshold group's owners therefore has exponent at most

$$
\frac32m-d_j+d-aD(t)+E/2+O(\log n)
 \le\frac32m-d_j+d-\frac58aD(t)+O(\log n).
\tag{EV-26}
$$

Choosing a least-deficient original full block as top, and extracting without increasing absolute deficiency, gives $d\le d_j$. Independent sorted parent streams charge these two sided incidence counts separately. At a complementary actual weight, one representative per tensor rectangle is sufficient: every pair in that rectangle has binary coefficient sum. There is no cross-side replay factor.

If a local core has size at least $m/2$, its whole complementary support is one atomic factor of logarithmic size at most $m/2$. The independently proved local-layer contrast is below $.49c+O(\log m)$. Put the atom on the smaller prescribed local child; the fixed-load difference is at most $m/2+O(\log m)$. Equation (EV-25) supplies enough actual movable top mass to balance these children, up to the fixed fine-factor error. Only top/background factors move; local mask roles remain fixed. Splitting each child's small factors into leaves preserves the atomic support and gives the usual leaf bound $\max(R_T,\beta/2)+O(m/Q_{\rm grid}+Q_{\rm grid}\log m)$.

Finally, (EV-12) and (EV-25) give the same central top coefficients at every distance:

$$
D_p=\frac{h(p)-p}{2},\qquad
A_p=\frac{h(p)-3p}{4},\qquad
f_p=\frac{h(p)+p}{8}.
\tag{EV-27}
$$

Relative to those central raw and restart expressions, (EV-10) adds the favorable correction $-aD(t)$; the leaf coefficient is unchanged. The checker enlargement affects incidence and tuple state only. The fine-grid constant is fixed before the input. Partition the top regions into that many chunks, enumerate each chunk count, and use their actual binomial products; a chunk factor has logarithmic size at most twice its coordinate count. All layout, count-profile and residue-pigeonhole families therefore have fixed polynomial size. Their logarithmic losses are polynomial factors. The only fixed linear allocation error is the displayed factor granularity, made smaller than any prescribed positive scalar margin by one fixed grid choice.

These are the precise interfaces for the separate mixed scalar, prime, residue-cover, initialization and global-branch certificates. They establish the ownership mechanism, without asserting those independent premises.
