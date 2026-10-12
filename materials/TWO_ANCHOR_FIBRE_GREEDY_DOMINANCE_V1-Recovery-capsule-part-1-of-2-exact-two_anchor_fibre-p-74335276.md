# material-743352761b9b

AI research material

---

#!/usr/bin/env python3
"""Exact actual-body control for TWO_ANCHOR_FIBRE_GREEDY_DOMINANCE_V1.
Pure standard library, rational geometry throughout. Run: python3 two_anchor_fibre.py
"""
from fractions import Fraction as F
from itertools import combinations
from functools import reduce
import json, hashlib
from pathlib import Path

def dot(a,b): return sum(x*y for x,y in zip(a,b))
def add(a,b): return tuple(x+y for x,y in zip(a,b))
def sub(a,b): return tuple(x-y for x,y in zip(a,b))
def scale(a,t): return tuple(t*x for x in a)
def cross(a,b): return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def det(a,b,c): return dot(a,cross(b,c))
def solve3(rows,rhs):
    d=det(*rows)
    if not d: return None
    return scale(add(add(scale(cross(rows[1],rows[2]),rhs[0]),scale(cross(rows[2],rows[0]),rhs[1])),scale(cross(rows[0],rows[1]),rhs[2])),1/d)
def hull2(points):
    points=sorted(set(points))
    if len(points)<3: return points
    def turn(a,b,c): return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])
    low=[]
    for p in points:
        while len(low)>1 and turn(low[-2],low[-1],p)<=0: low.pop()
        low.append(p)
    high=[]
    for p in reversed(points):
        while len(high)>1 and turn(high[-2],high[-1],p)<=0: high.pop()
        high.append(p)
    return low[:-1]+high[:-1]
def polygon_area(poly):
    return abs(sum(poly[i][0]*poly[(i+1)%len(poly)][1]-poly[i][1]*poly[(i+1)%len(poly)][0] for i in range(len(poly))))/2

def upper_value(forms,t): return max(p*t+q*(1-t) for p,q in forms)
def breaks(forms):
    out={F(0),F(1)}
    for (p,q),(r,s) in combinations(forms,2):
        den=p-q-r+s
        if den:
            t=(s-q)/den
            if 0<t<1: out.add(t)
    return sorted(out)

ALPHA=F(1,2); H=F(2); L0=(F(9,5),F(9,5))
AOLD=[(-F(1),F(0)),(F(0),-F(1)),(-F(1,250),-F(4,5))]
BOLD=[(F(1),F(0)),(F(0),F(1)),(F(99,100),F(1,5))]
ANEW=[(-F(1),F(0)),(-F(1,250),-F(4,5)),(F(0),-F(22,25))]
BNEW=[(F(0),F(1)),(F(99,100),F(1,5)),(F(249,250),F(2,25)),(F(1),-F(3,25))]

def body(lower,upper):
    hs=[((F(-1),F(0),F(0)),F(0),'x0'),((F(0),F(-1),F(0)),F(0),'y0')]
    hs += [((p,q,F(-1)),F(0),f'A{i}') for i,(p,q) in enumerate(lower)]
    hs += [((p,q,F(1)),F(1),f'B{i}') for i,(p,q) in enumerate(upper)]
    hs += [((L0[0],L0[1],F(1)),H,'root')]
    vertices=set()
    for ids in combinations(range(len(hs)),3):
        rows=[hs[i][0] for i in ids]; rhs=[hs[i][1] for i in ids]
        p=solve3(rows,rhs)
        if p is not None and all(dot(n,p)<=b for n,b,_ in hs): vertices.add(p)
    vertices=sorted(vertices); index={p:i for i,p in enumerate(vertices)}
    assert len(vertices)>=4
    center=scale(reduce(add,vertices),F(1,len(vertices)))
    facets=[]; edges=set(); V=F(0); first=(F(0),)*3; root=None
    for n,b,name in hs:
        incident=[p for p in vertices if dot(n,p)==b]
        if len(incident)<3: continue
        axis=next(i for i in range(3) if n[i]); dims=[i for i in range(3) if i!=axis]
        lookup={tuple(p[i] for i in dims):p for p in incident}
        face=[lookup[p] for p in hull2(list(lookup))]
        if len(face)<3: continue
        if dot(n,cross(sub(face[1],face[0]),sub(face[2],face[0])))<0: face.reverse()
        ids=[index[p] for p in face]; facets.append({'name':name,'vertices':ids,'normal':n,'offset':b})
        for i in range(len(ids)): edges.add(tuple(sorted((ids[i],ids[(i+1)%len(ids)]))))
        for i in range(1,len(face)-1):
            tri=(face[0],face[i],face[i+1])
            v=det(sub(tri[0],center),sub(tri[1],center),sub(tri[2],center))/6
            assert v>0
            centroid=scale(reduce(add,(center,)+tri),F(1,4))
            V+=v; first=add(first,scale(centroid,v))
        if name=='root': root=hull2([(p[0],p[1]) for p in face])
    assert len(vertices)-len(edges)+len(facets)==2
    assert root is not None and polygon_area(root)>0
    K=hull2([(p[0],p[1]) for p in vertices])
    E=V-F(9,10)*(first[0]+first[1])-F(1,2)*first[2]
    N=F(8,5)*(first[0]+first[1])
    assert V>0 and E>0
    # The two genuine coordinate supports still contain ABC and ABD.
    marks=[(F(0),F(0),F(0)),(F(0),F(0),F(1)),(F(0),F(1),F(0)),(F(1),F(0),F(0))]
    assert all(all(dot(n,p)<=b for n,b,_ in hs) for p in marks)
    for p in marks: assert p in index
    # These are genuine maximal triangles, not enlarged supporting patches.
    expected={'x0':{index[marks[i]] for i in (0,1,2)},
              'y0':{index[marks[i]] for i in (0,1,3)}}
    for name, ids in expected.items():
        f=next(f for f in facets if f['name']==name)
        assert set(f['vertices'])==ids and len(f['vertices'])==3
    return {'vertices':vertices,'facets':facets,'edges':sorted(edges),'f_vector':[len(vertices),len(edges),len(facets)],'volume':V,'first':first,'centroid':scale(first,1/V),'ell_integral':E,'n_integral':N,'trace':N/(6*V*E),'K':K,'R':root}

def curvature(forms):
    """Distributional second derivative of a max-affine envelope on (0,1)."""
    out={}
    for t in breaks(forms):
        if not 0<t<1: continue
        value=upper_value(forms,t)
        slopes=[p-q for p,q in forms if p*t+q*(1-t)==value]
        jump=max(slopes)-min(slopes)
        if jump: out[t]=jump
    return out

def greedy_tail(capacity,budget):
    """Fill earliest curvature first, subject to its exact endpoint cost."""
    chosen={}
    for t,cap in sorted(capacity.items()):
        take=min(cap,budget/(1-t))
        if take: chosen[t]=take
        budget-=take*(1-t)
    assert budget>=0
    return chosen,budget

def sf(x):
    if isinstance(x,F): return str(x)
    if isinstance(x,(tuple,list)): return [sf(y) for y in x]
    if isinstance(x,dict): return {k:sf(v) for k,v in x.items()}
    return x

def main():
    # Exhaustive interval endpoint audit: all functions below are piecewise affine.
    knots=sorted(set(breaks(AOLD)+breaks(BOLD)+breaks(ANEW)+breaks(BNEW)))
    for t in knots:
        ao,bo=upper_value(AOLD,t),upper_value(BOLD,t)
        an,bn=upper_value(ANEW,t),upper_value(BNEW,t)
        assert ao+bo==an+bn and an>=ao
        assert F(9,5)+ao>0  # Positive radial root slope proves boundedness.
        if t>=F(20,21):
            assert H*(an+bn)-(F(9,5)+an)>0
        if an>ao:
            # The entire changed angular tail is strictly nonroot for BOTH bodies.
            assert H*(ao+bo)-(F(9,5)+ao)>0
            assert H*(an+bn)-(F(9,5)+an)>0
    s1,s2=F(20,21),F(50,51)
    assert upper_value(ANEW,s1)==upper_value(AOLD,s1)
    assert F(1,250)==F(21,250)*(1-s1)==F(51,250)*(1-s2)
    old,new=body(AOLD,BOLD),body(ANEW,BNEW)
    assert old['K']==new['K'] and old['R']==new['R']
    v=max(x/(x+y) for x,y in old['R'])
    assert v==F(25,27)
    ca,cb=curvature(AOLD),curvature(BOLD)
    cap={t:ca.get(t,F(0))+cb.get(t,F(0)) for t in set(ca)|set(cb) if v<=t<1}
    assert cap=={s1:F(21,100),s2:F(51,250)}
    value=upper_value(AOLD,v)
    slope=min(p-q for p,q in AOLD if p*v+q*(1-v)==value)
    budget=-value-slope*(1-v)
    chosen,unspent=greedy_tail(cap,budget)
    assert budget==F(1,250) and unspent==0
    assert chosen=={s1:F(21,250)}
    assert {t:m for t,m in curvature(ANEW).items() if t>=v}==chosen
    assert old['volume']==new['volume'] and old['first'][:2]==new['first'][:2]
    assert old['n_integral']==new['n_integral']
    dz=new['first'][2]-old['first'][2]
    assert dz>0 and old['ell_integral']-new['ell_integral']==ALPHA*dz
    assert new['trace']>old['trace']
    output={'object':'TWO_ANCHOR_FIBRE_GREEDY_DOMINANCE_V1','old':old,'new':new,'delta_z_moment':dz,'delta_ell_integral':old['ell_integral']-new['ell_integral'],'source_forms':{'a_old':AOLD,'b_old':BOLD,'a_new':ANEW,'b_new':BNEW},'curvature_transfer':{'early':s1,'late':s2,'new_mass':F(21,250),'old_mass':F(51,250),'weighted_mass':F(1,250),'right_root_endpoint':v,'available_curvature':[[t,m] for t,m in sorted(cap.items())],'greedy_curvature':[[t,m] for t,m in sorted(chosen.items())]}}
    data=(json.dumps(sf(output),sort_keys=True,indent=2)+'\n').encode()
    Path('two_anchor_fibre_report.json').write_bytes(data)
    print('TWO_ANCHOR_FIBRE_GREEDY_DOMINANCE_V1 PASS')
    for label,o in [('OLD',old),('NEW',new)]:
        print(label,'f=',o['f_vector'],'V=',o['volume'],'first=',sf(o['first']),'E=',o['ell_integral'],'N=',o['n_integral'],'T=',o['trace'])
    print('DELTA_Z',dz,'DELTA_E',old['ell_integral']-new['ell_integral'])
    print('REPORT',len(data),hashlib.sha256(data).hexdigest())
if __name__=='__main__': main()
