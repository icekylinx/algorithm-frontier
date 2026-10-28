"""Elementary certifying transversal fallback with positive blocker signatures.

Derived public Graf--Haxell single-vertex procedure; no fast layer algorithm.
Copyright 2026 icekylinx. Authored by GPT-6 Astra Pro.
SPDX-License-Identifier: Apache-2.0
"""
from transversal_certificates import Constellation, Transversal, instance


def solve(classes, edges, observe=None):
    """Return an independent transversal or an exact domination constellation.

    Optional observe receives immutable stable-state snapshots (root, current
    matching, stars). Callback work/storage is additional and not retained by
    the algorithm. Vertex and class ties use their original integer IDs.
    """
    classes, owner, adjacent = instance(classes, edges)
    q = len(classes)
    matched = {}
    for root in range(q):
        if root in matched:
            continue
        stars = []
        while True:
            if observe is not None:
                observe(root, tuple(sorted(matched.values())),
                        tuple((center, tuple(sorted(leaves))) for center, leaves in stars))
            active = {root} | {owner[v] for _, leaves in stars for v in leaves}
            forest = {v for center, leaves in stars for v in (center, *leaves)}
            x = next((v for v in range(len(owner))
                      if owner[v] in active and not (adjacent[v] & forest)), None)
            if x is None:
                return Constellation(tuple(sorted(active)),
                                     tuple((c, tuple(sorted(l))) for c, l in stars))
            blockers = adjacent[x] & set(matched.values())
            if blockers:
                stars.append((x, blockers))
                continue
            # Free vertices swap within their own class. A zero-blocker last
            # center is processed immediately, before recording a stable state.
            while True:
                group = owner[x]
                old = matched.get(group)
                matched[group] = x
                if old is None:
                    break
                index = next(i for i, (_, leaves) in enumerate(stars) if old in leaves)
                stars = stars[:index+1]
                center, leaves = stars[-1]
                leaves.remove(old)
                if leaves:
                    break
                stars.pop()
                x = center
            if old is None:
                break
    return Transversal(tuple(matched[i] for i in range(q)))
