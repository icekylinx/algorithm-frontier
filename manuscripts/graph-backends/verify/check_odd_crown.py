#!/usr/bin/env python3
"""Independent finite check of the restored contact-rank and odd-crown identities.

This enumerates injections, all candidate bin sets, and brute-force physical
matchings. It does not certify the asymptotic flow/data-structure bounds.
"""
from __future__ import annotations
from functools import lru_cache
from itertools import permutations,product
import hashlib,json,random
from pathlib import Path

if not __debug__:
    raise SystemExit("Run mathematical verification without python -O.")

def require(value,message):
    if not value:
        raise AssertionError(message)

def outside_optimum(neighbors,outside):
    states={0}
    for row in neighbors:
        nxt=set(states)
        for used in states:
            available=row & outside & ~used
            while available:
                bit=available & -available
                nxt.add(used|bit);available-=bit
        states=nxt
    return max(map(int.bit_count,states),default=0)

def reachable(neighbors,assignment,contact,n):
    result=contact
    while True:
        previous=result
        for row,assigned in zip(neighbors,assignment):
            if result >> assigned & 1:
                result |= row
        if result==previous:return result

def matching_number(n,edges,retained=None):
    adjacency=[0]*n
    for u,v in edges:
        require(u!=v,"loop in physical test")
        adjacency[u]|=1<<v;adjacency[v]|=1<<u
    @lru_cache(None)
    def solve(mask):
        if not mask:return 0
        bit=mask & -mask;u=bit.bit_length()-1
        rest=mask^bit;best=solve(rest)
        candidates=adjacency[u]&rest
        while candidates:
            b=candidates & -candidates
            best=max(best,1+solve(rest^b));candidates-=b
        return best
    return solve((1<<n)-1 if retained is None else retained)

def physical_check(rng,n,neighbors,assignment,contact):
    vertices=[];weights=[];edges=[];count=0
    for _ in range(n):
        w=rng.choice((1,1,2));weights.append(w)
        group=list(range(count,count+2*w-1));count+=len(group);vertices.append(group)
        if w==2:edges.extend([(group[0],group[1]),(group[1],group[2]),(group[2],group[0])])
    row_vertices=list(range(count,count+len(neighbors)));count+=len(neighbors)
    for rv,nb in zip(row_vertices,neighbors):
        for d in range(n):
            if nb>>d&1:edges.append((rv,rng.choice(vertices[d])))
    u,v,b=count,count+1,count+2;count+=3;edges.append((u,v))
    for d in range(n):
        if contact>>d&1:edges.append((rng.choice(vertices[d]),rng.choice((u,v,b))))
    # These extra edges can meet H and therefore exercise the upper bound.
    extras=row_vertices+[u,v,b]
    for i,x in enumerate(extras):
        for y in extras[i+1:]:
            if rng.randrange(7)==0:edges.append((x,y))
    S=reachable(neighbors,assignment,contact,n);T=((1<<n)-1)^S
    H=[i for i,row in enumerate(neighbors) if row&T]
    removed={x for d in range(n) if T>>d&1 for x in vertices[d]}
    removed.update(row_vertices[i] for i in H)
    retained=sum(1<<x for x in range(count) if x not in removed)
    offset=sum(weights[d]-1 for d in range(n) if T>>d&1)+len(H)
    require(matching_number(count,edges)==offset+matching_number(count,edges,retained),
            ("physical optimum offset",n,neighbors,assignment,contact,edges))
    return count

def main():
    graphs=contacts=injections_checked=physical=0;max_physical=0
    rng=random.Random(41024)
    for n in range(5):
        full=(1<<n)-1
        for rows in range(min(3,n)+1):
            for neighbors in product(range(1,1<<n),repeat=rows):
                injections=[p for p in permutations(range(n),rows)
                            if all(nb>>d&1 for nb,d in zip(neighbors,p))]
                if not injections:continue
                graphs+=1
                h=[mask.bit_count()-sum(nb&~mask==0 for nb in neighbors)
                   for mask in range(1<<n)]
                for contact in range(1<<n):
                    contacts+=1
                    unused=[full^sum(1<<d for d in p) for p in injections]
                    r=max((mask&contact).bit_count() for mask in unused)
                    q=outside_optimum(neighbors,full^contact)
                    require(r==contact.bit_count()-rows+q,"outside matching formula")
                    values=[(h[mask],mask) for mask in range(1<<n) if mask&contact==contact]
                    optimum=min(value for value,_ in values)
                    minimizers=[mask for value,mask in values if value==optimum]
                    canonical=full
                    for mask in minimizers:canonical&=mask
                    require(optimum==r and h[canonical]==r,"minimum captive deficit")
                    optimizers=[p for p,u in zip(injections,unused)
                                if (u&contact).bit_count()==r]
                    for p in optimizers:
                        injections_checked+=1
                        S=reachable(neighbors,p,contact,n)
                        require(S==canonical,"canonical reachable envelope")
                        free=full^sum(1<<d for d in p)
                        require(free&S&~contact==0,"reachable noncontact free bin")
                        T=full^S
                        H={i for i,nb in enumerate(neighbors) if nb&T}
                        assigned={i for i,d in enumerate(p) if T>>d&1}
                        require(H==assigned,"crown row neighborhood")
                    if rng.randrange(97)==0:
                        max_physical=max(max_physical,physical_check(
                            rng,n,neighbors,optimizers[0],contact))
                        physical+=1
    result=dict(status="PASS",scope="Exhaustive abstract contact-rank/canonical-envelope identities for <=4 bins and <=3 rows; seeded physical odd-bin offset cases checked by independent subset matching DP.",
                abstract_graphs=graphs,contact_instances=contacts,
                optimal_injections_checked=injections_checked,
                physical_offset_instances=physical,max_physical_vertices=max_physical,
                source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
    print(json.dumps(result,sort_keys=True))

if __name__=="__main__":main()
