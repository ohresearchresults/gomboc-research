# material-2526bca3cae8

AI research material

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

#!/usr/bin/env python3
"""Exact one-triangular-cut centroid steering demonstration (stdlib only).
No claim of a class110 construction. All predicates use fractions.Fraction.
"""
from fractions import Fraction as Q
from itertools import combinations, product
import json

def dot(a,b): return sum((x*y for x,y in zip(a,b)), Q(0))
def add(a,b): return tuple(x+y for x,y in zip(a,b))
def sub(a,b): return tuple(x-y for x,y in zip(a,b))
def scale(k,a): return tuple(k*x for x in a)
def cross(a,b): return (a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2], a[0]*b[1]-a[1]*b[0])
def detcols(a,b,c): return dot(a,cross(b,c))
def product3(v): return v[0]*v[1]*v[2]
def solve3(rows,rhs):
    a,b,c = rows
    d=detcols(a,b,c)
    if not d: raise ValueError('singular matrix')
    return scale(1/d, add(add(scale(rhs[0],cross(b,c)),scale(rhs[1],cross(c,a))),scale(rhs[2],cross(a,b))))
def fstr(x): return str(x)
def vecstr(x): return [fstr(a) for a in x]

def polytope(planes):
    """Enumerate bounded simple 3-polytope from exact n.x <= h inequalities."""
    points=set()
    for ids in combinations(range(len(planes)),3):
        try: x=solve3([planes[i][0] for i in ids],[planes[i][1] for i in ids])
        except ValueError: continue
        if all(dot(n,x)<=h for n,h in planes): points.add(x)
    vs=sorted(points)
    if len(vs)<4: raise ValueError('not a full-dimensional bounded fixture')
    active=[{i for i,(n,h) in enumerate(planes) if dot(n,x)==h} for x in vs]
    if any(len(a)!=3 for a in active): raise ValueError('fixture must be simple and irredundant')
    edges={}
    for i,j in combinations(range(len(vs)),2):
        fs=active[i]&active[j]
        if len(fs)==2: edges[(i,j)]=tuple(sorted(fs))
    adj=[[] for _ in vs]
    for i,j in edges: adj[i].append(j); adj[j].append(i)
    faces=[]
    for f,(n,h) in enumerate(planes):
        ids={i for i,a in enumerate(active) if f in a}
        if len(ids)<3: raise ValueError('empty/redundant face')
        cyc=[min(ids)]; prev=None; cur=cyc[0]
        while True:
            nxts=sorted(j for j in adj[cur] if j in ids and j!=prev)
            if not nxts: raise ValueError('broken face boundary')
            nxt=nxts[0]
            if nxt==cyc[0]: break
            if nxt in cyc: raise ValueError('cycle repeats')
            cyc.append(nxt); prev,cur=cur,nxt
        if set(cyc)!=ids: raise ValueError('face not one cycle')
        orient=dot(n,cross(sub(vs[cyc[1]],vs[cyc[0]]),sub(vs[cyc[2]],vs[cyc[0]])))
        if orient<0: cyc=[cyc[0]]+list(reversed(cyc[1:]))
        elif orient==0: raise ValueError('degenerate face triangle')
        faces.append(cyc)
    vol=Q(0); moment=(Q(0),)*3
    for cyc in faces:
        a=vs[cyc[0]]
        for j in range(1,len(cyc)-1):
            b,c=vs[cyc[j]],vs[cyc[j+1]]
            d=detcols(a,b,c)
            vol+=d/6
            moment=add(moment,scale(d/24,add(add(a,b),c)))
    if vol<=0: raise ValueError('wrong volume')
    com=scale(1/vol,moment)
    assert all(dot(n,com)<h for n,h in planes)
    stable=[]; unstable=[]; saddle=[]; weak=[]
    for i,(n,h) in enumerate(planes):
        y=add(com,scale((h-dot(n,com))/dot(n,n),n))
        sl=[hh-dot(nn,y) for j,(nn,hh) in enumerate(planes) if j!=i]
        if min(sl)>0: stable.append(i)
        elif min(sl)>=0: weak.append(['face',i])
    for i,x in enumerate(vs):
        ds=[dot(sub(x,com),sub(vs[j],x)) for j in adj[i]]
        if max(ds)<0: unstable.append(i)
        elif max(ds)<=0: weak.append(['vertex',i])
    for (i,j),(f,g) in edges.items():
        x=vs[i]; d=sub(vs[j],x)
        t=dot(sub(com,x),d)/dot(d,d)
        if not 0<=t<=1: continue
        y=add(x,scale(t,d)); r=sub(y,com)
        n,m=planes[f][0],planes[g][0]
        nn,nm,mm=dot(n,n),dot(n,m),dot(m,m)
        dd=nn*mm-nm*nm
        aa=(dot(r,n)*mm-dot(r,m)*nm)/dd
        bb=(dot(r,m)*nn-dot(r,n)*nm)/dd
        assert add(scale(aa,n),scale(bb,m))==r
        if aa>=0 and bb>=0:
            if 0<t<1 and aa>0 and bb>0: saddle.append((i,j))
            else: weak.append(['edge',i,j])
    assert len(vs)-len(edges)+len(faces)==2
    assert len(stable)+len(unstable)-len(saddle)==2 if not weak else True
    return dict(vertices=vs,edges=edges,faces=faces,adj=adj,volume=vol,centroid=com,
                stable=stable,unstable=unstable,saddle=saddle,weak=weak)

def report(p):
    return dict(V=len(p['vertices']),E=len(p['edges']),F=len(p['faces']),C=2*len(p['edges']),
                volume=fstr(p['volume']),centroid=vecstr(p['centroid']),
                S=len(p['stable']),U=len(p['unstable']),H=len(p['saddle']),weak=p['weak'])

def cut_plane(w,us,ts):
    q=solve3(us,[1/t for t in ts])
    return scale(-1,q), -1-dot(q,w)

def main():
    Z=Q(0); O=Q(1)
    cube=[]
    for i in range(3):
        e=tuple(O if j==i else Z for j in range(3))
        cube.extend([(scale(-1,e),Z),(e,O)])
    aa,bb,cc=Q(1,100),Q(1,5),Q(3,10)
    planes=cube+[((-1/aa,-1/bb,-1/cc),Q(-1))]
    base=polytope(planes)
    assert (len(base['stable']),len(base['unstable']),len(base['saddle']),len(base['weak']))==(6,8,12,0)
    w=(Z,bb,Z)
    wi=base['vertices'].index(w)
    assert wi not in base['unstable']
    neigh=((Z,O,Z),(aa,Z,Z),(Z,Z,cc))
    assert set(neigh)=={base['vertices'][i] for i in base['adj'][wi]}
    us=tuple(sub(x,w) for x in neigh)
    ts=(Q(1,10),Q(1,8),Q(1,6))
    n,h=cut_plane(w,us,ts)
    assert dot(n,w)>h
    assert all(dot(n,x)<h for x in base['vertices'] if x!=w)
    after=polytope(planes+[(n,h)])
    v=abs(detcols(*us))*ts[0]*ts[1]*ts[2]/6
    m=add(w,scale(Q(1,4),tuple(sum(ts[i]*us[i][j] for i in range(3)) for j in range(3))))
    pred=scale(1/(base['volume']-v),sub(scale(base['volume'],base['centroid']),scale(v,m)))
    assert base['volume']-after['volume']==v
    assert pred==after['centroid']
    c=after['centroid']; V=after['volume']
    cols=tuple(scale(-v/V,add(sub(m,c),scale(ts[i]/4,us[i]))) for i in range(3))
    detj=detcols(*cols)
    q=scale(-1,n); qc=dot(q,sub(c,w))
    expected=4*(v/V)**3*(detcols(*us)*ts[0]*ts[1]*ts[2]/64)*(qc-1)
    assert detj==expected and detj!=0 and qc>1
    assert (len(after['stable']),len(after['unstable']),len(after['saddle']),len(after['weak']))==(6,8,12,0)
    witness=us[1]
    patch=[x for x in after['vertices'] if dot(n,x)==h]
    patch_min=min(dot(sub(x,c),witness) for x in patch)
    assert patch_min>0
    # The same local control in normalized inward-plane coordinates.
    pnormal=scale(1/(qc-1),q)
    ys=[sub(x,c) for x in patch]
    ysum=tuple(sum(y[j] for y in ys) for j in range(3))
    area_over_norm=abs(dot(cross(sub(ys[1],ys[0]),sub(ys[2],ys[0])),pnormal))/(2*dot(pnormal,pnormal))
    Jp=tuple(tuple(area_over_norm/(12*V)*(ysum[i]*ysum[j]+sum(y[i]*y[j] for y in ys)) for j in range(3)) for i in range(3))
    minors=(Jp[0][0],Jp[0][0]*Jp[1][1]-Jp[0][1]**2,detcols(*Jp))
    assert all(x>0 for x in minors)
    # Chain rule converts normalized-plane controls to the intercept controls.
    for i in range(3):
        dq=solve3(us,[(-1/ts[i] if j==i else Q(0)) for j in range(3)])
        dk=dot(dq,sub(c,w))
        dp=scale(1/(qc-1)**2,sub(scale(qc-1,dq),scale(dk,q)))
        assert tuple(dot(row,dp) for row in Jp)==cols[i]
    # Exact inverse quartic for this rational target centroid.
    # Coordinates in the edge basis are obtained from the transposed row matrix.
    rows=tuple(tuple(us[j][i] for j in range(3)) for i in range(3))
    avec=solve3(rows,sub(c,w))
    bvec=scale(base['volume'],solve3(rows,sub(base['centroid'],c)))
    kappa=abs(detcols(*us))/6
    assert v**4==64*kappa*product3(tuple(avec[i]*v+bvec[i] for i in range(3)))
    assert tuple(4*(avec[i]+bvec[i]/v) for i in range(3))==ts
    corners=[]
    for s in product((Q(99,100),Q(101,100)),repeat=3):
        tt=tuple(x*y for x,y in zip(ts,s))
        pn,ph=cut_plane(w,us,tt)
        assert all(dot(pn,x)<ph for x in base['vertices'] if x!=w)
        pp=polytope(planes+[(pn,ph)])
        assert (len(pp['stable']),len(pp['unstable']),len(pp['saddle']),len(pp['weak']))==(6,8,12,0)
        corners.append(dict(multipliers=vecstr(s),centroid=vecstr(pp['centroid'])))
    # Exact derivative cross-check via rational polynomial identity after differentiating
    # the cap formulas directly at each intercept (no finite differences).
    for i in range(3):
        dv=v/ts[i]; dm=scale(Q(1,4),us[i])
        direct=scale(1/V,sub(scale(dv,sub(c,m)),scale(v,dm)))
        assert direct==scale(1/ts[i],cols[i])
    out=dict(base=report(base),steered=report(after),apex=vecstr(w),
             edge_vectors=[vecstr(u) for u in us],intercepts=vecstr(ts),
             removed_volume=fstr(v),cut_plane=dict(n=vecstr(n),h=fstr(h)),
             jacobian_log_columns=[vecstr(col) for col in cols],
             jacobian_log_determinant=fstr(detj),q_of_centroid=fstr(qc),
             patch_exclusion_witness=vecstr(witness),patch_witness_min=fstr(patch_min),
             normalized_inward_normal=vecstr(pnormal),
             plane_jacobian_rows=[vecstr(row) for row in Jp],
             plane_jacobian_leading_minors=vecstr(minors),
             inverse_quartic_a=vecstr(avec),inverse_quartic_b=vecstr(bvec),kappa=fstr(kappa),
             tested_corner_fixtures=corners,
             note='Eight exact corner fixtures are not a certificate of the whole parameter box; the theorem gives a local open neighborhood.')
    with open('result.json','w',encoding='utf-8',newline='\n') as f:
        json.dump(out,f,indent=2,sort_keys=True); f.write('\n')
    print('EXACT_STEERING_OK')
    print('BASE',report(base))
    print('AFTER',report(after))
    print('DET_LOG_J',fstr(detj))
    print('PATCH_WITNESS_MIN',fstr(patch_min))
    print('NO_CLASS110_CLAIM')
if __name__=='__main__': main()
