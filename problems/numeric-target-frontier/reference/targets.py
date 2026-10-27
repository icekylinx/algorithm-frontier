"""Exact mixed numeric targets via occupied profiles and covering chains.

Attribution: Yilin Liu and GPT-6 Astra Pro. Apache-2.0.
Complete original rank tables are charged. Local LPs stream active systems,
with an explicit cost separate from paid polynomial weighted intersection.
No resource-unit list or copied-ground subset rank table is constructed.
"""
from dataclasses import dataclass
from fractions import Fraction as F
from itertools import permutations
from pathlib import Path
import importlib.util
import sys


def load(name,path):
    if name not in sys.modules:
        spec=importlib.util.spec_from_file_location(name,Path(__file__).resolve().parents[2]/path)
        module=importlib.util.module_from_spec(spec)
        sys.modules[name]=module
        spec.loader.exec_module(module)
    return sys.modules[name]


shared=load('_numeric_target_profile_lp','arbitrary-value-allocation-scheme/reference/scheme.py')
exact=shared.exact


@dataclass(frozen=True)
class Answer:
    counts: tuple  # original coordinate IDs, including masked coordinates
    value: F


@dataclass(frozen=True)
class Prepared:
    eligible: tuple
    rows: tuple  # original surviving row IDs
    covers: tuple
    supports: tuple  # original nonempty supports after zero-target preparation
    rank_loss: bool


@dataclass(frozen=True)
class Chain:
    order: tuple  # original covering row IDs in stopping order
    keys: tuple  # (original coordinate ID or None for legitimate disposal, layer)
    columns: tuple
    lower: tuple
    upper: tuple
    classes: tuple  # sorted (nonzero coefficient vector, copied coordinate indices)
    zero: tuple


def profiles(vectors,caps,total):
    """Exactly occupied-vector multiplicities under component and rank caps."""
    vectors,caps=tuple(tuple(v) for v in vectors),tuple(caps)
    if (type(total) is not int or total<0 or any(type(x) is not int or x<0 for x in caps)
            or any(len(v)!=len(caps) or not any(v) or any(type(x) is not int or x<0 for x in v) for v in vectors)):
        raise ValueError('nonnegative integral caps/total and nonzero integer vectors required')
    if not vectors:
        yield ()
        return
    current=[0]*len(vectors)
    def frame(i,used,loads):
        maximum=min((caps[j]-loads[j])//a for j,a in enumerate(vectors[i]) if a)
        return [i,used,loads,0,min(total-used,maximum)]
    stack=[frame(0,0,(0,)*len(caps))]
    while stack:
        i,used,loads,value,maximum=stack[-1]
        if value>maximum:
            stack.pop()
            continue
        stack[-1][3]+=1
        current[i]=value
        if i+1==len(vectors): yield tuple(current)
        else:
            next_loads=tuple(b+a*value for a,b in zip(vectors[i],loads))
            stack.append(frame(i+1,used+value,next_loads))


class Targets:
    def __init__(self,rank,coefficients,relations,targets,scalar,mandatory=False,eligible=None):
        self.rank=tuple(rank)
        length=len(self.rank)
        if not length or length&(length-1): raise ValueError('complete original rank table required')
        self.n=length.bit_length()-1
        # Canonical table validation checks all integral polymatroid axioms.
        shared.intrinsic.weighted.table_scenario((self.rank,),((0,),)*self.n,0)
        self.coefficients=tuple(tuple(row) for row in coefficients)
        self.relations,self.targets=tuple(relations),tuple(targets)
        self.scalar=tuple(exact(x) for x in scalar)
        self.mandatory=mandatory
        self.eligible=(True,)*self.n if eligible is None else tuple(eligible)
        if (type(mandatory) is not bool or len(self.scalar)!=self.n or len(self.eligible)!=self.n
                or any(type(x) is not bool for x in self.eligible)
                or not len(self.coefficients)==len(self.relations)==len(self.targets)
                or any(len(row)!=self.n or any(type(x) is not int or x<0 for x in row) for row in self.coefficients)
                or any(r not in ('<=','=','>=') for r in self.relations)
                or any(type(t) is not int or t<0 for t in self.targets)):
            raise ValueError('matching original dimensions, nonnegative integer rows/targets and exact scalar required')
        self.total=self.rank[-1]
        self.last_stats={}

    def verify(self,answer):
        try:
            if (type(answer) is not Answer or type(answer.counts) is not tuple or len(answer.counts)!=self.n
                    or any(type(x) is not int or x<0 or (x and not self.eligible[e]) for e,x in enumerate(answer.counts))): return False
            x=answer.counts
            if self.mandatory and sum(x)!=self.total: return False
            if any(sum(x[e] for e in range(self.n) if s>>e&1)>bound for s,bound in enumerate(self.rank)): return False
            for row,relation,target in zip(self.coefficients,self.relations,self.targets):
                value=sum(a*b for a,b in zip(row,x))
                if not {'<=':value<=target,'=':value==target,'>=':value>=target}[relation]: return False
            return type(answer.value) in (int,F) and answer.value==sum((a*b for a,b in zip(self.scalar,x)),F(0))
        except (ValueError,TypeError,AttributeError,IndexError): return False

    def prepare(self):
        eligible=tuple(e for e in range(self.n) if self.eligible[e] and
                       all(relation=='>=' or row[e]<=target for row,relation,target in zip(self.coefficients,self.relations,self.targets)))
        rows=tuple(j for j,t in enumerate(self.targets) if t>0)
        covers=tuple(j for j in rows if self.relations[j]=='>=')
        supports=tuple(sorted({tuple(j for j in rows if self.coefficients[j][e]>0) for e in eligible}-{()}))
        loss=self.mandatory and self.rank[sum(1<<e for e in eligible)]<self.total
        return Prepared(eligible,rows,covers,supports,loss)

    def chains(self):
        prepared=self.prepare()
        if prepared.rank_loss: return
        owners=prepared.eligible+(() if self.mandatory else (None,))
        for order in permutations(prepared.covers):
            # Every layer is one suffix in a single stopping-order chain.
            removed={j:i for i,j in enumerate(order)}
            keys=tuple((e,layer) for e in owners for layer in range(len(order)+1))
            columns=[]
            for e,layer in keys:
                column=[]
                for j in prepared.rows:
                    a=0 if e is None else self.coefficients[j][e]
                    if j in removed: a=min(a,self.targets[j]) if removed[j]>=layer else 0
                    column.append(a)
                columns.append(tuple(column))
            # Layers with the same original owner and coefficient column are
            # interchangeable; aggregate them without changing any scalar/rank.
            unique={}
            for key,column in zip(keys,columns): unique.setdefault((key[0],column),key)
            keys=tuple(unique.values())
            columns=tuple(column for (_,column) in unique)
            classes={}
            zero=[]
            for i,column in enumerate(columns):
                if any(column): classes.setdefault(column,[]).append(i)
                else: zero.append(i)
            lower=tuple(self.targets[j] if self.relations[j] in ('=','>=') else 0 for j in prepared.rows)
            upper=tuple(2*self.targets[j]-1 if self.relations[j]=='>=' else self.targets[j] for j in prepared.rows)
            yield Chain(order,keys,tuple(columns),lower,upper,tuple((v,tuple(classes[v])) for v in sorted(classes)),tuple(zero))

    def profile_vectors(self,chain):
        for h in profiles(tuple(v for v,_ in chain.classes),chain.upper,self.total):
            loads=tuple(sum(v[j]*count for (v,_),count in zip(chain.classes,h)) for j in range(len(chain.upper)))
            if all(value>=bound for value,bound in zip(loads,chain.lower)):
                yield h

    def recover(self,chain,multiplicities,maximize=False):
        """One actual shared-resource / prescribed-partition full-total face.

        Chain records are internal prepared objects, not input certificates.
        The returned original answer is independently verified.
        """
        if type(maximize) is not bool: raise ValueError('boolean optimization direction required')
        if (len(multiplicities)!=len(chain.classes) or any(type(h) is not int or h<0 for h in multiplicities)
                or sum(multiplicities)>self.total): raise ValueError('invalid class multiplicities')
        loads=tuple(sum(v[j]*h for (v,_),h in zip(chain.classes,multiplicities)) for j in range(len(chain.upper)))
        if any(not lo<=value<=hi for lo,value,hi in zip(chain.lower,loads,chain.upper)):
            raise ValueError('profile does not meet bounded target intervals')
        remainder=self.total-sum(multiplicities)
        if remainder and not chain.zero: return None
        size=len(chain.keys)
        if not size:
            answer=Answer((0,)*self.n,F(0))
            return answer if self.total==0 and self.verify(answer) else None
        # Prescribed partition totals eliminate one variable per nonempty
        # class, retaining exactly the same original-total face.
        groups=tuple((indices,h) for (_,indices),h in zip(chain.classes,multiplicities))+((chain.zero,remainder),)
        if any(h and not indices for indices,h in groups): return None
        groups=tuple((indices,h) for indices,h in groups if indices)
        free=tuple(i for indices,_ in groups for i in indices[:-1])
        dimension=len(free)
        positions={i:k for k,i in enumerate(free)}
        def reduce(row,bound):
            reduced=[F(0)]*dimension
            constant=F(0)
            for indices,h in groups:
                last=indices[-1]
                constant+=row[last]*h
                for i in indices[:-1]: reduced[positions[i]]=F(row[i]-row[last])
            return tuple(reduced),F(bound)-constant
        rows=[]
        for i in range(size): rows.append(reduce(tuple(-int(i==j) for j in range(size)),0))
        # Aggregate-copy rank rows are equivalent to every copied-set rank row.
        # Optional disposal is excluded: only real original units consume F.
        for subset,bound in enumerate(self.rank):
            rows.append(reduce(tuple(int(e is not None and bool(subset>>e&1)) for e,_ in chain.keys),bound))
        weights=tuple(F(0) if e is None else self.scalar[e] for e,_ in chain.keys)
        objective,_=reduce(tuple(-a if maximize else a for a in weights),0)
        point=shared.active_vertex(rows,dimension,objective,self.last_stats)
        if point is None: return None
        copied=[F(0)]*size
        for i,value in zip(free,point): copied[i]=value
        for indices,h in groups: copied[indices[-1]]=h-sum((copied[i] for i in indices[:-1]),F(0))
        if any(x.denominator!=1 for x in copied): raise RuntimeError('resource/partition full-total face was fractional')
        original=[0]*self.n
        for (e,_),x in zip(chain.keys,copied):
            if e is not None: original[e]+=int(x)
        answer=Answer(tuple(original),sum((a*b for a,b in zip(self.scalar,original)),F(0)))
        if not self.verify(answer): raise RuntimeError('chain recovery violated original target/resource model')
        return answer

    def greedy(self,prepared,maximize):
        """Exact signed scalar optimum after all numeric rows are automatic."""
        order=sorted(prepared.eligible,key=lambda e:((-1 if maximize else 1)*self.scalar[e],e))
        if not self.mandatory:
            order=tuple(e for e in order if (self.scalar[e]>0 if maximize else self.scalar[e]<0))
        counts=[0]*self.n
        previous=selected=0
        for e in order:
            selected|=1<<e
            counts[e]=self.rank[selected]-previous
            previous=self.rank[selected]
        answer=Answer(tuple(counts),sum((a*b for a,b in zip(self.scalar,counts)),F(0)))
        return answer if self.verify(answer) else None

    def solve(self,maximize=False):
        if type(maximize) is not bool: raise ValueError('boolean optimization direction required')
        self.last_stats={'chains':0,'profiles':0}
        prepared=self.prepare()
        if prepared.rank_loss: return None
        if not prepared.rows or not prepared.supports:
            return self.greedy(prepared,maximize)
        best=None
        for chain in self.chains():
            self.last_stats['chains']+=1
            for h in self.profile_vectors(chain):
                self.last_stats['profiles']+=1
                answer=self.recover(chain,h,maximize)
                if answer is not None and (best is None or (answer.value>best.value if maximize else answer.value<best.value)):
                    best=answer
        return best
