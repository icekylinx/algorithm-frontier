"""Adaptive scenario reference. Attribution: icekylinx and GPT-6 Astra Pro.

Apache-2.0. Exact Bland LP and selected-set enumeration are potentially
exponential; they do not implement the corank approximation scheme.
"""
from dataclasses import dataclass
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path
import importlib.util
import sys

# Keep the shared native flow implementation canonical, without a package install.
_name = '_algorithm_frontier_concurrent'
if _name not in sys.modules:
    _path = Path(__file__).resolve().parents[2] / 'selected-flow/reference/concurrent.py'
    _spec = importlib.util.spec_from_file_location(_name, _path)
    _module = importlib.util.module_from_spec(_spec)
    sys.modules[_name] = _module
    _spec.loader.exec_module(_module)
flow = sys.modules[_name]
Network = flow.Network


@dataclass(frozen=True)
class Scenario:
    network: Network
    budgets: tuple = ()

    def __post_init__(self):
        # Validate and materialize all rows once, including generator inputs.
        net = self.network
        rows = tuple((tuple(tuple(flow.rational(x) for x in row) for row in charges),
                      flow.rational(cap)) for charges, cap in self.budgets)
        if not net.commodities:
            raise ValueError('nonempty common commodity ground required')
        flow.formulation(net, (0,), rows)
        object.__setattr__(self, 'budgets', rows)


def _scenarios(scenarios):
    scenarios = tuple(scenarios)
    if not scenarios or any(not isinstance(s, Scenario) for s in scenarios):
        raise ValueError('nonempty explicit Scenario list required')
    q = len(scenarios[0].network.commodities)
    if any(len(s.network.commodities) != q for s in scenarios):
        raise ValueError('scenario commodity counts differ')
    return scenarios


@dataclass(frozen=True)
class Certificate:
    selected: tuple
    certificates: tuple

    @property
    def rate(self):
        return min(c.rate for c in self.certificates)

    def routings(self):
        """One primal tuple per scenario, with every rate reduced to rate."""
        rate = self.rate
        return tuple(tuple(x * (rate / c.rate) for x in c.primal)
                     if c.rate else tuple(F(0) for _ in c.primal)
                     for c in self.certificates)


def optimize_fixed(scenarios, selected):
    scenarios = _scenarios(scenarios)
    selected = tuple(selected)
    certs = tuple(flow.optimize_fixed(s.network, selected, s.budgets) for s in scenarios)
    return Certificate(selected, certs)


def verify_fixed(scenarios, certificate):
    """Search-free exact fixed-common-set optimality; no global-family claim."""
    try:
        scenarios = _scenarios(scenarios)
        return (type(certificate) is Certificate
                and len(certificate.certificates) == len(scenarios)
                and all(type(c) is flow.Certificate
                        and c.selected == certificate.selected
                        and flow.verify_fixed(s.network, c, s.budgets)
                        for s, c in zip(scenarios, certificate.certificates)))
    except (ValueError, TypeError, AttributeError, IndexError):
        return False


def optimize_selected(scenarios, rank, permitted=lambda selected: True):
    scenarios = _scenarios(scenarios)
    q = len(scenarios[0].network.commodities)
    if type(rank) is not int or not 1 <= rank <= q:
        raise ValueError('rank must be between one and commodity count')
    best = None
    for selected in combinations(range(q), rank):
        if permitted(selected):
            candidate = optimize_fixed(scenarios, selected)
            if best is None or candidate.rate > best.rate:
                best = candidate
    return best


@dataclass(frozen=True)
class ScenarioRow:
    scenario: int
    row: flow.PackingRow


def separate(scenarios, rates):
    """First rejecting scenario's globally valid row; None means membership."""
    scenarios = _scenarios(scenarios)
    rates = tuple(rates)
    for index, scenario in enumerate(scenarios):
        row = flow.separate(scenario.network, rates, scenario.budgets)
        if row is not None:
            return ScenarioRow(index, row)
    return None
