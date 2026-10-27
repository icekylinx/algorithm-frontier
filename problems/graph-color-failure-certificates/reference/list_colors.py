"""Exact mixed/list color certificates using actual evaluation-feature spans.

Attribution: Yilin Liu and GPT-6 Astra Pro. Apache-2.0.
No failure family or formal monomial universe is enumerated. The optional
single-failure wrapper uses an explicitly charged exact reference MSF update,
not the published polylogarithmic dynamic-MSF implementation.
"""
from dataclasses import dataclass
from fractions import Fraction as F
from bisect import bisect_left
from math import comb
from pathlib import Path
import importlib.util
import sys


def load(name,path):
    if name not in sys.modules:
        spec = importlib.util.spec_from_file_location(name,path)
        module = importlib.util.module_from_spec(spec)
        sys.modules[name] = module
        spec.loader.exec_module(module)
    return sys.modules[name]


features = load('_graph_list_features',Path(__file__).resolve().parents[2]/'persistence-failure-certificates/reference/feature_summary.py')
vertex = load('_graph_list_vertex',Path(__file__).with_name('vertex_colors.py'))


def rational(value):
    if type(value) not in (int,F): raise ValueError('exact integer or Fraction weight required')
    return F(value)


def labels(values):
    values = tuple(values)
    if any(type(v) is not int or v < 0 for v in values) or len(set(values)) != len(values):
        raise ValueError('distinct nonnegative original color IDs required')
    return frozenset(values)


def field(modulus):
    # Same declared-prime interface as the canonical exact feature module.
    # Do not trial-divide a potentially enormous encoded modulus.
    if modulus is not None and (type(modulus) is not int or modulus < 2):
        raise ValueError('caller-supplied prime modulus required')
    return features.Field(modulus)


@dataclass(frozen=True)
class Edge:
    u: int
    v: int
    weight: F
    colors: tuple = ()


@dataclass(frozen=True)
class Component:
    vertices: tuple
    mode: str
    feature_rank: int
    formal_dimension: int
    support_bound: int
    expanded: int


@dataclass(frozen=True)
class Certificate:
    vertex_colors: tuple
    records: tuple  # retained (original ID, original exact Edge), in fixed order
    failures: int
    support_bound: int
    components: tuple

    def forest(self,failed_colors=(),threshold=None):
        raw = tuple(failed_colors)
        failed = labels(raw)
        if len(raw) > self.failures: raise ValueError('failure budget exceeded')
        if threshold is not None:
            if type(threshold) is not tuple or len(threshold) != 2 or type(threshold[1]) is not int or threshold[1] < 0:
                raise ValueError('threshold must be an exact weight/original-ID pair')
            threshold = rational(threshold[0]),threshold[1]
        dsu = vertex._DSU(len(self.vertex_colors))
        answer = []
        for i,edge in self.records:
            if threshold is not None and (edge.weight,i) > threshold: break
            destroyed = self.vertex_colors[edge.u] | self.vertex_colors[edge.v] | frozenset(edge.colors)
            if not destroyed & failed and dsu.join(edge.u,edge.v): answer.append(i)
        return tuple(answer)


def validate(vertex_colors,edges):
    vertex_colors = tuple(labels(row) for row in vertex_colors)
    n = len(vertex_colors)
    records = []
    for i,edge in enumerate(edges):
        if (type(edge) is not Edge or type(edge.u) is not int or type(edge.v) is not int
                or not 0 <= edge.u < n or not 0 <= edge.v < n):
            raise ValueError('canonical edge and original endpoint IDs required')
        color = tuple(sorted(labels(edge.colors)))
        weight = rational(edge.weight)
        if edge.u != edge.v: records.append((i,Edge(edge.u,edge.v,weight,color)))
    return vertex_colors,tuple(sorted(records,key=lambda pair:(pair[1].weight,pair[0])))


def polynomial(color,pad,points,f):
    result = [f.one]
    for c in sorted(color):
        result = features._multiply_linear(result,f.sub(f.zero,points[c]),f.one,f)
    for _ in range(pad-len(color)):
        result = features._multiply_linear(result,f.zero,f.one,f)
    return tuple(result)


def multiply(first,second,f):
    result = [f.zero]*(len(first)+len(second)-1)
    for i,a in enumerate(first):
        for j,b in enumerate(second): result[i+j] = f.add(result[i+j],f.mul(a,b))
    return tuple(result)


def component_features(vertices,records,vertex_colors,failures,f):
    """Actual row span of all formal monic-coefficient evaluation features."""
    universe = set().union(*(vertex_colors[v] for v in vertices),*(set(e.colors) for _,e in records))
    if f.modulus is not None and f.modulus <= len(universe):
        raise ValueError('prime field needs distinct nonzero label points plus dummy zero')
    points = {c:f.value(i+1) for i,c in enumerate(sorted(universe))}
    h = min(failures,len(universe))
    dv = max((len(vertex_colors[v]) for v in vertices),default=0)
    vp = {v:polynomial(vertex_colors[v],dv,points,f) for v in vertices}
    if all(not e.colors for _,e in records):
        mode,keys,polynomials,degree = 'VERTEX',tuple(vertices),tuple(vp[v] for v in vertices),dv
    else:
        de = max(len(e.colors) for _,e in records)
        ep = {i:polynomial(e.colors,de,points,f) for i,e in records}
        keys = tuple((i,v) for i,e in records for v in (e.u,e.v))
        polynomials = tuple(multiply(vp[v],ep[i],f) for i,v in keys)
        degree = dv+de
        mode = ('CUBIC' if all(len(vertex_colors[v]) == 1 for v in vertices)
                and all(len(e.colors) == 1 for _,e in records) else 'MIXED')
    coords = tuple(tuple(poly[j] for poly in polynomials) for j in range(degree))
    module = features.evaluation_module(((f.one,)*len(keys),),coords,h,f)
    vectors = {key:tuple(row[j] for row in module.vectors) for j,key in enumerate(keys)}
    formal = comb(h+degree,degree)
    if mode == 'VERTEX':
        t = module.rank
        bound = len(vertices)*t-comb(t+1,2)
    elif mode == 'CUBIC':
        k = h+1
        t = min(k,len({next(iter(vertex_colors[v])) for v in vertices}))
        bound = len(vertices)*comb(k+1,2)-comb(k+2,3)+comb(k-t+2,3)
    else:
        bound = len(vertices)*formal
    return vectors,Component(tuple(vertices),mode,module.rank,formal,min(len(records),bound),module.expanded)


def build(vertex_colors,edges,failures,modulus=None):
    if type(failures) is not int or failures < 0: raise ValueError('nonnegative integral failure budget required')
    vertex_colors,records = validate(vertex_colors,edges)
    f = field(modulus)
    n = len(vertex_colors)
    dsu = vertex._DSU(n)
    for _,edge in records: dsu.join(edge.u,edge.v)
    groups = {}
    for v in range(n): groups.setdefault(dsu.root(v),[]).append(v)
    retained,info = [],[]
    for root,vertices in groups.items():
        local = tuple((i,e) for i,e in records if dsu.root(e.u) == root)
        if not local:
            info.append(Component(tuple(vertices),'EMPTY',0,0,0,0))
            continue
        vectors,component = component_features(vertices,local,vertex_colors,failures,f)
        info.append(component)
        width = component.feature_rank
        positions = {v:j for j,v in enumerate(vertices)}
        basis = features.Echelon(len(vertices)*width,f)
        count = 0
        for i,edge in local:
            column = [f.zero]*(len(vertices)*width)
            left = vectors[edge.v] if component.mode == 'VERTEX' else vectors[i,edge.v]
            right = vectors[edge.u] if component.mode == 'VERTEX' else vectors[i,edge.u]
            for j,x in enumerate(left): column[positions[edge.u]*width+j] = x
            for j,x in enumerate(right): column[positions[edge.v]*width+j] = f.sub(f.zero,x)
            if basis.insert(column):
                retained.append((i,edge))
                count += 1
        if count > component.support_bound: raise RuntimeError('activation rank exceeded proved bound')
    retained.sort(key=lambda pair:(pair[1].weight,pair[0]))
    return Certificate(vertex_colors,tuple(retained),failures,sum(c.support_bound for c in info),tuple(info))


class ReferenceMSF:
    """Exact exchange-reporting reference; each update scans the fixed order."""
    def __init__(self,n,records):
        self.n,self.records = n,tuple(records)
        self.by_id = dict(self.records)
        self.active = set()
        self.forest = ()
        self.updates = 0

    def update(self,original_id,present):
        if type(original_id) is not int or original_id not in self.by_id or type(present) is not bool:
            raise ValueError('valid original update ID and boolean presence required')
        if (original_id in self.active) == present: raise ValueError('update must change edge presence')
        if present: self.active.add(original_id)
        else: self.active.remove(original_id)
        dsu = vertex._DSU(self.n)
        current = tuple(i for i,e in self.records if i in self.active and dsu.join(e.u,e.v))
        before,after = set(self.forest),set(current)
        removed,added = tuple(before-after),tuple(after-before)
        if len(removed) > 1 or len(added) > 1: raise RuntimeError('single update changed more than one MSF exchange')
        self.forest = current
        self.updates += 1
        return removed,added


class _Extras:
    """Dense original-ID linked list: constant event work, output-size scan."""
    def __init__(self,size):
        self.next,self.previous,self.present = [None]*size,[None]*size,[False]*size
        self.head = None

    def add(self,i):
        if self.present[i]: raise RuntimeError('duplicate forest insertion event')
        self.present[i] = True
        self.next[i],self.previous[i] = self.head,None
        if self.head is not None: self.previous[self.head] = i
        self.head = i

    def remove(self,i):
        if not self.present[i]: raise RuntimeError('missing forest deletion event')
        before,after = self.previous[i],self.next[i]
        if before is None: self.head = after
        else: self.next[before] = after
        if after is not None: self.previous[after] = before
        self.present[i] = False

    def ids(self):
        current = self.head
        while current is not None:
            yield current
            current = self.next[current]


@dataclass(frozen=True)
class Difference:
    removed: tuple
    added: tuple
    value: F


@dataclass(frozen=True)
class SingleFailure:
    palette: tuple
    baseline: tuple
    baseline_value: F
    differences: tuple
    records: tuple
    replacement_total: int
    incidence_total: int
    updates: int

    def indexed(self,index):
        if type(index) is not int or not 0 <= index < len(self.palette): raise ValueError('valid compact color index required')
        return self.differences[index]

    def color(self,color):
        if type(color) is not int or color < 0: raise ValueError('nonnegative original color ID required')
        index = bisect_left(self.palette,color)
        return (self.differences[index] if index < len(self.palette) and self.palette[index] == color
                else Difference((),(),self.baseline_value))

    def forest(self,color):
        difference = self.color(color)
        chosen = (set(self.baseline)-set(difference.removed)) | set(difference.added)
        return tuple(i for i,_ in self.records if i in chosen)


def single_failure(vertex_colors,edges,backend=ReferenceMSF):
    """Actual completed-batch exchange wrapper, with a paid dynamic backend."""
    edges = tuple(edges)
    vertex_colors,records = validate(vertex_colors,edges)
    n = len(vertex_colors)
    dynamic = backend(n,records)
    for i,_ in records: dynamic.update(i,True)
    baseline = tuple(dynamic.forest)
    base = frozenset(baseline)
    by_id = dict(records)
    baseline_value = sum((by_id[i].weight for i in baseline),F(0))
    destroyed = {}
    palette = set().union(*vertex_colors)
    for i,e in records:
        color = vertex_colors[e.u] | vertex_colors[e.v] | frozenset(e.colors)
        palette.update(color)
        for c in color: destroyed.setdefault(c,[]).append(i)
    extra = _Extras(len(edges))
    def update(i,present):
        removed,added = dynamic.update(i,present)
        for e in removed:
            if e not in base: extra.remove(e)
        for e in added:
            if e not in base: extra.add(e)
    results = []
    used = set(baseline)
    order = {i:j for j,(i,_) in enumerate(records)}
    for c in sorted(palette):
        block = tuple(destroyed.get(c,()))
        removed = tuple(i for i in block if i in base)
        if removed:
            for i in block: update(i,False)
            added = tuple(sorted(extra.ids(),key=order.__getitem__))
            if len(added) > len(removed): raise RuntimeError('replacement bound exceeded')
            used.update(added)
            value = baseline_value-sum((by_id[i].weight for i in removed),F(0))+sum((by_id[i].weight for i in added),F(0))
            for i in reversed(block): update(i,True)
            if tuple(extra.ids()): raise RuntimeError('restoration left nonbaseline forest edges')
        else:
            added,value = (),baseline_value
        results.append(Difference(removed,added,value))
    return SingleFailure(tuple(sorted(palette)),baseline,baseline_value,tuple(results),
                         tuple((i,e) for i,e in records if i in used),sum(len(r.added) for r in results),
                         sum(len(block) for block in destroyed.values()),dynamic.updates)
