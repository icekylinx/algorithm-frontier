# Deterministic Static Joint-Freeing by Triangular Forest Exchanges

**Static reduction for one fixed row-bin graph and a supplied witness
forest.** Its current use is the local query in
[balanced-forest-pair-oracle.md](balanced-forest-pair-oracle.md), with balance supplied by the actual
integral-carrier representation. The proof below does not assume that
pruning certificates survive a later structural edit.

## 1. Setting

Let D be bins with positive integer weights w_v, A rows with at most three distinct bin neighbors, and L an integer. Suppose nonnegative allocations x_{rv} satisfy

- sum_v x_{rv}=L for every row r;
- sum_r x_{rv} <= L-w_v for every bin v.

Assume a forest T on D has one edge e_r={u_r,v_r} for every row r, with both endpoints among that row's neighbors. Every tree of T can be rooted at an arbitrary bin. Assign each row to the child endpoint of its edge. This gives an injection covering all rows, leaving exactly the tree roots free.

The witness-forest construction and static tight-block pruning are recorded in [tight-blocks-via-forest-pruning.md](tight-blocks-via-forest-pruning.md). This note supplies the constructive joint-freeing step after pruning.

## 2. Parallel pruning and recorded levels

At round j, remove every surviving row edge e_r whose row has a neighbor outside its current forest component. Record level lambda(r)=j and one such outside neighbor z_r. Edges never removed receive level infinity. The final components are exactly the maximal tight sets, where h(X)=|X|-|A(X)|=1.

Let T_{>=j} be the subforest of the original T containing all edges with level at least j. The recorded witness satisfies:

- both endpoints of e_r lie in the same component of T_{>=lambda(r)};
- z_r lies outside that component.

The level is the parallel round, not an arbitrary sequential deletion index.

### Round bound

Consider a current component C of weight W. Its represented rows number |C|-1. They send total allocation L(|C|-1), while the total capacity of bins in C is at most L|C|-W. Hence those represented rows send at least W-L units outside C. Only rows cut in this round can do so; each contributes at most L. At least W/L-1 edges are cut whenever W>L.

If W>2L, at least W/(2L) edges are cut. Since the children are disjoint nonempty bin sets of positive integer weight, every child component has weight at most W-W/(2L). Thus any continuing component chain falls below weight 2L after O(L log W(D)) rounds. Thereafter it can undergo at most 2L additional splitting rounds. The largest finite level is therefore H=O(L log W(D)).

The number of rounds is not the preprocessing time: the queue/small-side implementation can assign levels while processing each affected incidence only logarithmically many times, as in the companion note.

## 3. Pair-freeing algorithm

Given queried bins i,j in different final tight blocks:

1. If i,j are already in different trees of T, root their trees at i,j and finish.
2. Otherwise add an artificial edge q={i,j}, with level infinity. On its unique cycle, choose a row edge e of minimum finite level and delete it. Its row becomes the sole **hole**: all other rows still have one selected edge, and q is present. Let ell=lambda(e).
3. For the hole row r, let u be either endpoint of its original selected edge, and let z=z_r be its recorded witness.
4. If u,z belong to different current forest components, add the selected edge {u,z} labelled r and finish the exchange chain.
5. Otherwise add {u,z}, creating a cycle. Delete a minimum-level row edge f on that cycle; its row becomes the new hole. Continue with ell=lambda(f).
6. The final forest contains one edge for every row and the artificial edge q. Delete q. Its endpoints i,j are now in distinct trees. Root those two trees at i,j; root every other tree arbitrarily. The induced injection leaves i,j free simultaneously.

All selected row edges remain genuine pairs of that row's neighbors. No artificial q edge is deleted inside the exchange chain: its infinite level excludes it whenever the cycle has a finite edge.

## 4. Strict descent proof

We refer throughout to the original forest T and its fixed threshold components. During the chain, use this invariant for the current hole level ell:

> For every threshold t<=ell, every current forest edge of level at least t has both endpoints in one component of the original T_{>=t}.

This includes q, of infinite level. Initially q's original tree path has minimum level ell. Therefore its endpoints are in one original T_{>=t} component for all t<=ell; all ordinary original edges satisfy the invariant automatically.

Let the hole row have level ell, original endpoint u, and witness z. The pruning certificate says u,z are in different original T_{>=ell} components. If they are connected in the current forest, the path between them must contain an edge of level below ell, by the invariant. Thus the minimum edge f removed in step 5 has level g<ell, and is not q.

Every edge on the current u-z path has level at least g. Applying the invariant at threshold g shows that u,z are in one original T_{>=g} component. Hence the new selected edge for r has both endpoints in one original T_{>=g} component, and therefore also in one original T_{>=t} component for every t<=g. All unchanged edges retain the invariant. The next hole has level g, so induction applies.

Finite levels strictly decrease at every nonterminal pivot. A level-one hole must link into a different original tree component; therefore termination occurs after at most H+1 pivots. Each cycle deletion preserves acyclicity and the current forest components. Only the final link merges two original tree components. Deleting q restores the original number of components and separates i from j.

## 5. Cost and representation

A dynamic-tree structure stores the current selected forest with each edge's fixed pruning level and row label. Connectivity, path-minimum, link and cut operations take logarithmic time. The chain therefore costs O(H log |D|)=O(L polylog N), beyond the static preprocessing.

The new injection can differ on long alternating paths. It should be represented implicitly: root each tree and assign every row to its child endpoint. A bin's assigned row is its parent-edge label; a row's assigned bin is its edge's child endpoint. Standard rooted-forest operations support these point queries and rerooting with logarithmic overhead. Full materialization is linear in the represented graph and can be postponed to a phase boundary or other already-charged materialization.

This distinction is necessary. The theorem does not promise an explicit list of all changed assignments in O(L polylog N) time if the list itself is longer. It supplies an implicit valid injection with efficient point access. A caller demanding explicit change notifications for every assignment would require a separate cost bound.

For a single query, only two original tree components can become involved. Their old designated roots can be replaced by i,j; all other roots remain unchanged.

## 6. What this does and does not settle

Together with the companion static forest construction and tight-block/minimal-tight-set routines, this gives a deterministic static structural pair oracle after near-linear preprocessing: return a minimal tight contraction witness, or an implicit joint-freeing injection, with the requested local work bounds.

It does not justify retaining the original pruning certificates after arbitrary edits. A pivot of a level-ell row can connect different original components at higher thresholds, so the invariant is intentionally maintained only below the currently decreasing hole level. Once topology changes by gain, peel, expansion or contraction, the original certificates can become stale. Rebuilding the entire structure after every gain costs O(N) per gain, which does not yield the desired near-linear phase bound. A valid faster overall algorithm needs a charged update/rebuild scheme or a replacement invariant spanning all phase edits.

The static statement concerns arbitrary row-bin states satisfying the supplied invariants. Its dynamic composition is supplied separately by [Deterministic Exact General Matching through Persistent Integral Carriers and Normalized Routing](../../problems/general-matching/proof.md), which obtains a fresh balanced selected forest from the actual ledger at each settled state.

## 7. Repeated queries on one fixed incidence graph

The static oracle can answer an arbitrary sequence of read-only pair queries without rebuilding the pruning certificate. Retain the original labelled forest, its parallel levels and witnesses, and a canonical root per original tree. For each query, start from that reference forest, perform the at most `H+1` exchanges above, and designate the two requested roots. A rollback dynamic-tree implementation can undo the preceding query's edits before beginning the next one. Each link, cut, path-minimum operation and root change is charged once when performed and once when undone. The resulting amortized query bound remains `O(L polylog N)`; preprocessing is paid once. Persistence gives the analogous bound if several returned injection descriptions must coexist.

The previously returned injection need not be extended or respected. Every rooted selected forest defines a valid injection of the same rows into the same bins; replacing one such injection by another preserves the represented matching cardinality. The allocations, debts and barrier coordinates are attached to physical row-bin incidences, rather than to the current injection, and therefore do not change on such a replacement. A future structural operation asks only for the currently assigned row or assigned bin where it needs that information.

For the physical matching representation, each selected endpoint stores a genuine physical incidence of its row with the indicated bin. The parent edge at a bin determines the external row contact, if any. The bin's factor-critical witness then determines its internal matching with that contact exposed. A free root has an independently designated exposed vertex. These choices describe one exact matching without explicitly rewriting every physical edge whenever a tree is rerooted. Point queries and eventual materialization use this description; full materialization costs linear work in the materialized physical vertices. This is an implementation interface, not a claim that a caller maintaining a fully explicit matching array can perform the same bulk change for free.

The fixed-graph hypothesis is essential. In the OAI driver each successful structural pair query is immediately followed by a gain or contraction, so an unmodified application does not provide a long sequence of read-only pair queries. The rollback statement removes repeated-query staleness for an unchanged graph; it does not remove the update problem after topology changes.
