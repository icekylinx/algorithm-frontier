"""Exact resource-side backend for ordered recipient-matroid reservations.

Attribution: Yilin Liu and GPT-6 Astra Pro. SPDX-License-Identifier: Apache-2.0
Rank oracles are promised matroid rank functions on range(players). The caller
owns player-matroid eligibility, layers, local bundle feasibility and thresholds.
"""
from dataclasses import dataclass
from typing import Callable, FrozenSet, Iterable, Optional, Tuple

Rank = Callable[[FrozenSet[int]], int]


@dataclass(frozen=True)
class Bundle:
    owner: int
    resources: FrozenSet[int]


@dataclass(frozen=True)
class Center:
    bundle: Bundle
    blockers: FrozenSet[int]


class Reservations:
    """Deterministic ordered centers over immutable, monotonically named records.

    Public snapshots are tuples/frozen values. Failed operations do not mutate
    the state. Successful calls use polynomially many original rank queries.
    """

    def __init__(self, players: int, ranks: Iterable[Rank], matching: Iterable[Bundle] = ()):
        if type(players) is not int or players < 0:
            raise ValueError("players must be a nonnegative integer")
        self.players = players
        self._ranks = tuple(ranks)
        if not all(callable(rank) for rank in self._ranks):
            raise ValueError("rank oracles must be callable")
        bundles = tuple(matching)
        for bundle in bundles:
            self._validate_bundle(bundle)
        if len({bundle.owner for bundle in bundles}) != len(bundles):
            raise ValueError("matching owners must be distinct")
        for j in range(len(self._ranks)):
            owners = frozenset(b.owner for b in bundles if j in b.resources)
            if self._rank(j, owners) != len(owners):
                raise ValueError("infeasible matching recipient column")
        self._matching = dict(enumerate(bundles))
        self._centers = ()
        self._next_id = len(bundles)

    @property
    def matching(self) -> Tuple[Tuple[int, Bundle], ...]:
        return tuple(self._matching.items())

    @property
    def centers(self) -> Tuple[Center, ...]:
        return self._centers

    def _validate_bundle(self, bundle):
        if not isinstance(bundle, Bundle) or type(bundle.owner) is not int:
            raise ValueError("expected a Bundle with an integer owner")
        if not 0 <= bundle.owner < self.players:
            raise ValueError("owner outside player ground")
        if type(bundle.resources) is not frozenset or not bundle.resources:
            raise ValueError("resources must be a nonempty frozenset")
        if any(type(j) is not int or not 0 <= j < len(self._ranks) for j in bundle.resources):
            raise ValueError("resource outside explicit ground")

    def _rank(self, j, owners):
        value = self._ranks[j](frozenset(owners))
        if type(value) is not int or not 0 <= value <= len(owners):
            raise ValueError("invalid rank oracle response")
        return value

    def _outside(self, j, owner, owners):
        owners = frozenset(owners)
        return self._rank(j, owners | {owner}) > self._rank(j, owners)

    def _prefix(self, count):
        if type(count) is not int or not 0 <= count <= len(self._centers):
            raise ValueError("invalid retained prefix length")
        return self._centers[:count]

    def _sets(self, j, prefix):
        marked = frozenset(i for c in prefix for i in c.blockers)
        selected = frozenset(c.bundle.owner for c in prefix if j in c.bundle.resources)
        recipients = frozenset(b.owner for b in self._matching.values() if j in b.resources)
        designated = frozenset(self._matching[i].owner for i in marked
                               if j in self._matching[i].resources)
        return selected, designated, recipients

    def available(self, owner: int) -> FrozenSet[int]:
        """Resources outside the current selected-plus-marked closure (P7)."""
        if type(owner) is not int or not 0 <= owner < self.players:
            raise ValueError("owner outside player ground")
        answer = []
        for j in range(len(self._ranks)):
            selected, designated, _ = self._sets(j, self._centers)
            if self._outside(j, owner, selected | designated):
                answer.append(j)
        return frozenset(answer)

    def complete(self, bundle: Bundle) -> FrozenSet[int]:
        """Append a blocked center using (P9); a free candidate is not stored.

        Returns its designated record IDs, or the empty set for a fresh strongly
        free candidate. The caller supplies a locally feasible minimal bundle.
        """
        self._validate_bundle(bundle)
        if any(b.owner == bundle.owner and b.resources & bundle.resources
               for b in self._matching.values()):
            raise ValueError("candidate repeats an existing matching service")
        if not bundle.resources <= self.available(bundle.owner):
            raise ValueError("candidate uses an unavailable resource")
        marked = frozenset(i for c in self._centers for i in c.blockers)
        blockers = set()
        for j in sorted(bundle.resources):
            selected, _, recipients = self._sets(j, self._centers)
            if not self._outside(j, bundle.owner, selected | recipients):
                blockers.update(i for i, b in self._matching.items()
                                if i not in marked and j in b.resources)
        blockers = frozenset(blockers)
        if blockers:
            self._centers += (Center(bundle, blockers),)
        return blockers

    def releasable(self, index: int) -> bool:
        """Current P12 test, including conservative nonempty blocker groups."""
        if type(index) is not int or not 0 <= index < len(self._centers):
            raise ValueError("invalid center index")
        center = self._centers[index]
        for j in sorted(center.bundle.resources):
            selected, designated, _ = self._sets(j, self._centers[:index])
            own = frozenset(self._matching[i].owner for i in center.blockers
                            if j in self._matching[i].resources)
            if not self._outside(j, center.bundle.owner, selected | designated | own):
                return False
        return True

    def exchange(self, incoming: Bundle, outgoing: Optional[int], keep: int) -> int:
        """Insert a strongly free bundle and retain exactly the requested prefix.

        An outgoing record is deleted from every retained group. New records
        inherit no designation. Augmentation (outgoing=None) discards all
        centers. Caller separately certifies the player-side earliest exchange.
        The stronger resource freedom is checked before any mutation.
        """
        self._validate_bundle(incoming)
        prefix = self._prefix(keep)
        if outgoing is None:
            if keep:
                raise ValueError("augmentation must discard all centers")
        elif type(outgoing) is not int or outgoing not in self._matching:
            raise ValueError("unknown outgoing record")
        if any(i != outgoing and b.owner == incoming.owner for i, b in self._matching.items()):
            raise ValueError("incoming owner already has another matching record")
        for j in sorted(incoming.resources):
            selected, _, recipients = self._sets(j, prefix)
            if not self._outside(j, incoming.owner, selected | recipients):
                raise ValueError("incoming bundle is not strongly free for retained prefix")
        revised = tuple(Center(c.bundle, c.blockers - {outgoing}) for c in prefix)
        new_id = self._next_id
        if outgoing is not None:
            del self._matching[outgoing]
        self._matching[new_id] = incoming
        self._centers = revised
        self._next_id += 1
        return new_id
