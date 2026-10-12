"""Independent replay of all 79 capacity bounds.

Directly parses immutable source integers. Cramer's-rule vertices are exact.
Face cycles are reconstructed from common-plane incidence, independently of
the primary projected convex-hull algorithm. Moments are integrated from an
interior point. Uses only the Python standard library.
"""
from pathlib import Path
from fractions import Fraction as F
from itertools import combinations
from functools import lru_cache
from collections import Counter
import hashlib
import json
import re

root = Path(__file__).resolve().parent
raw = (root/'results/asg_lSjg7n_lMDvF8a-CVGsUNf_R.json').read_bytes()
assert hashlib.sha256(raw).hexdigest() == '2c28fe4781353da1c2fdd2b85cb4f28fc41e59870e8fdbfcfd291e002831fd72'
text = json.loads(raw)['result_markdown']
p = {m[0]: tuple(map(int,m[1:])) for m in re.findall(
    r'^(0|C|H|AS|AT|AU|AV|AW|AX|AY)\s*=\s*\(\s*(-?\d+),\s*(-?\d+),\s*(-?\d+)\)/D',text,re.M)}
D = 2**30


def minus(a,b):
    return tuple(x-y for x,y in zip(a,b))


def scalar(a,b):
    return sum(x*y for x,y in zip(a,b))


def det(a,b,c):
    return a[0]*(b[1]*c[2]-b[2]*c[1])-a[1]*(b[0]*c[2]-b[2]*c[0])+a[2]*(b[0]*c[1]-b[1]*c[0])


rows = []
for face in combinations(p,3):
    a,b,c = (p[k] for k in face)
    ab,ac = minus(b,a),minus(c,a)
    signs = [det(ab,ac,minus(v,a)) for v in p.values()]
    if all(x<=0 for x in signs):
        sign=1
    elif all(x>=0 for x in signs):
        sign=-1
    else:
        continue
    assert sum(x==0 for x in signs)==3
    n=tuple(sign*det(ab,ac,tuple(int(j==k) for j in range(3))) for k in range(3))
    rows.append((frozenset(face),n,scalar(n,a)))
assert len(rows)==16
rows.append((frozenset(('CLIP',)),(0,1,0),0))


@lru_cache(None)
def intersection(ids):
    A=[rows[i][1] for i in ids]
    rhs=[rows[i][2] for i in ids]
    denominator=det(*A)
    if denominator==0:
        return None
    xyz=[]
    for j in range(3):
        mat=[list(row) for row in A]
        for i in range(3):
            mat[i][j]=rhs[i]
        xyz.append(F(det(*mat),denominator))
    return tuple(xyz)


def integrate(ids):
    vertices=set()
    for triple in combinations(ids,3):
        v=intersection(triple)
        if v is not None and all(scalar(rows[i][1],v)<=rows[i][2] for i in ids):
            vertices.add(v)
    vertices=sorted(vertices)
    V=len(vertices)
    assert V>=4
    ref=tuple(sum(v[j] for v in vertices)/V for j in range(3))
    cycles=[]
    for plane in ids:
        fv={i for i,v in enumerate(vertices) if scalar(rows[plane][1],v)==rows[plane][2]}
        if len(fv)<3:
            continue
        adjacency={i:set() for i in fv}
        for other in ids:
            if other==plane:
                continue
            shared=[i for i in fv if scalar(rows[other][1],vertices[i])==rows[other][2]]
            assert len(shared)<=2, 'Distinct constraints must not represent a duplicate facet'
            if len(shared)==2:
                a,b=shared
                adjacency[a].add(b)
                adjacency[b].add(a)
        assert all(len(x)==2 for x in adjacency.values())
        start=min(fv)
        cycle=[start,min(adjacency[start])]
        while True:
            nxt=next(x for x in adjacency[cycle[-1]] if x!=cycle[-2])
            if nxt==start:
                break
            assert nxt not in cycle
            cycle.append(nxt)
        assert set(cycle)==fv
        a,b,c=[vertices[q] for q in cycle[:3]]
        if det(minus(a,ref),minus(b,ref),minus(c,ref))<0:
            cycle.reverse()
        cycles.append(cycle)
    edges=Counter()
    volume=F(0)
    moment=[F(0)]*3
    for cycle in cycles:
        for e in zip(cycle,cycle[1:]+cycle[:1]):
            edges[tuple(sorted(e))]+=1
        for j in range(1,len(cycle)-1):
            a,b,c=[vertices[q] for q in (cycle[0],cycle[j],cycle[j+1])]
            delta=det(minus(a,ref),minus(b,ref),minus(c,ref))
            assert delta>0
            assert all(det(minus(b,a),minus(c,a),minus(v,a))<=0 for v in vertices)
            volume+=delta/6
            for q in range(3):
                moment[q]+=delta*(ref[q]+a[q]+b[q]+c[q])/24
    assert set(edges.values())=={2}
    assert V-len(edges)+len(cycles)==2
    return volume/D**3,tuple(x/D**4 for x in moment)


atlas=json.loads((root/'ax10-patch-atlas.json').read_text())
mandatory={frozenset(f) for f in atlas['mandatory_four']}
source_volume,source_moment=integrate(tuple(range(16)))
_,source_negative=integrate(tuple(range(17)))
certificate=json.loads((root/'ax10-centroid-obstruction.json').read_text())
assert source_volume==F(certificate['source_volume'])
assert [str(x/source_volume) for x in source_moment]==certificate['source_centroid']
total=0
excluded=0
for level in atlas['atlas']:
    for case in level['cases']:
        removed=mandatory|{frozenset(f) for f in case['additional_removed_faces']}
        ids=tuple(i for i in range(16) if rows[i][0] not in removed)
        volume,_=integrate(ids)
        _,negative=integrate(ids+(16,))
        lower=source_moment[1]+negative[1]-source_negative[1]
        assert volume==F(case['container_volume'])
        assert negative[1]==F(case['negative_moment'])
        assert lower==F(case['moment_lower'])
        assert (lower>0)==case['closed']
        total+=1
        excluded+=int(lower>0)
    print('INDEPENDENT_EXACT_LEVEL_PASS',level['removed_count'],len(level['cases']),flush=True)
assert total==79 and excluded==78
print('INDEPENDENT_AX10_79_CASE_CAPACITY_ATLAS_PASS closed=78 unresolved=1')
