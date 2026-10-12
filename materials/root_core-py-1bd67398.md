# material-1bd673985599

AI research material

---

#!/usr/bin/env python3
"""Exact root eligibility and centroid-core cones on an actual 10/17/9 body.
Python >=3.10, standard library only. No random choices or numeric optimizer.
Run: python root_core.py --output root_core.json
The input is the central (r,s,eta)=(1/4,1/4,1/4) actual cut body, raw frame.
It is not a class110 construction: the generated metrics only select a unique
GLOBAL FARTHEST vertex, a necessary but insufficient condition for unique U.
"""
from fractions import Fraction as F
from itertools import combinations
from math import gcd, lcm
import argparse, json, hashlib

def add(a,b): return tuple(x+y for x,y in zip(a,b))
def sub(a,b): return tuple(x-y for x,y in zip(a,b))
def mul(t,a): return tuple(t*x for x in a)
def dot(a,b): return sum(x*y for x,y in zip(a,b))
def cross(a,b): return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def det(a,b,c): return dot(a,cross(b,c))
def ray(v):
    if not any(v): return None
    g=0
    for x in v: g=gcd(g,abs(x))
    return tuple(x//g for x in v)
def qstr(x): return str(F(x))
def qt(v): return [qstr(x) for x in v]
def raw_input():
    r=s=t=F(1,4); z=(F(0),)*3
    a=(F(0),F(0),F(1)); e1=(F(1),F(0),F(0)); e2=(F(0),F(1),F(0))
    p=(F(45,92),-F(113,345),F(0)); q=(F(135,283),F(1808,1415),F(0))
    v=[a,e1,e2,z,add(mul(1-r,p),mul(r,a)),mul(1-r,p),add(mul(1-r,p),mul(r*(1-t),e1)),add(mul(1-s,q),mul(s,a)),add(mul(1-s,q),mul(s,e1)),add(mul(1-s,q),mul(s,e2))]
    faces=[(0,3,5,4),(0,4,1),(0,1,8,7),(0,7,9,2),(0,2,3),(1,6,5,3,2,9,8),(4,5,6),(7,8,9),(1,4,6)]
    return v,faces

def exact_geometry(v, faces):
    """Orient and certify full true facets, then integrate actual signed tetrahedra."""
    avg=mul(F(1,len(v)),tuple(sum(p[k] for p in v) for k in range(3)))
    oriented=[]; normals=[]; ds=F(0); moment=(F(0),)*3; edges=set()
    for f0 in faces:
        f=tuple(f0); a,b,c=(v[i] for i in f[:3]); n=cross(sub(b,a),sub(c,a))
        assert any(n)
        if dot(n,sub(avg,a))>0:
            f=tuple(reversed(f)); a,b,c=(v[i] for i in f[:3]); n=cross(sub(b,a),sub(c,a))
        assert dot(n,sub(avg,a))<0
        for i,p in enumerate(v):
            d=dot(n,sub(p,a)); assert (d==0 if i in f else d<0)
        for j in range(len(f)):
            i,k,l=f[j],f[(j+1)%len(f)],f[(j+2)%len(f)]
            assert dot(cross(sub(v[k],v[i]),sub(v[l],v[k])),n)>0
            edges.add(tuple(sorted((i,k))))
        for j in range(1,len(f)-1):
            b,c=v[f[j]],v[f[j+1]]; d=det(a,b,c)
            ds+=d; moment=add(moment,mul(d,add(add(a,b),c)))
        oriented.append(f); normals.append(n)
    supports=set()
    for i,j,k in combinations(range(len(v)),3):
        n=cross(sub(v[j],v[i]),sub(v[k],v[i]))
        if not any(n): continue
        sl=[dot(n,sub(p,v[i])) for p in v]
        if min(sl)>=0 or max(sl)<=0:
            supports.add(tuple(t for t,d in enumerate(sl) if d==0))
    assert supports=={tuple(sorted(f)) for f in faces}
    assert all(sum(a in f and b in f and ((f.index(a)-f.index(b))%len(f) in (1,len(f)-1)) for f in faces)==2 for a,b in edges)
    assert ds>0 and len(v)-len(edges)+len(faces)==2
    g=mul(1/(4*ds),moment)
    assert all(dot(n,sub(g,v[f[0]]))<0 for f,n in zip(oriented,normals))
    return oriented,normals,sorted(edges),ds/6,g

def common_fan_rays(v,a,b):
    """Extreme rays of N_max(a) intersect N_min(b), exact integer enumeration.
    Cone is pointed as a subcone of the vertex normal cone of a full-dimensional
    bounded polytope. Every extreme ray has two linearly independent active
    inequalities in R3, including when the cone has dimension 1 or 2.
    """
    inequalities=set()
    for p in v:
        for h in (sub(v[a],p),sub(p,v[b])):
            h=ray(h)
            if h is not None: inequalities.add(h)
    hs=sorted(inequalities); rays=set()
    for h,k in combinations(hs,2):
        r=ray(cross(h,k))
        if r is None: continue
        for rr in (r,mul(-1,r)):
            if all(dot(q,rr)>=0 for q in hs): rays.add(rr)
    return sorted(rays)

def metric_witness(v,g,a,r,n0):
    """Perturb a positive core-fan ray into the strict normal cone, then rank-one + I."""
    rest=[i for i in range(len(v)) if i!=a]
    reflected=[sub(add(v[a],v[i]),mul(2,g)) for i in rest]
    assert all(dot(r,w)>0 for w in reflected)
    eps=F(1)
    for w in reflected:
        d=dot(n0,w)
        if d<0: eps=min(eps,dot(r,w)/(-2*d))
    ell=add(r,mul(eps,n0)); x=[sub(p,g) for p in v]; root=x[a]
    assert all(dot(ell,sub(v[a],v[i]))>0 and dot(ell,reflected[k])>0 for k,i in enumerate(rest))
    assert dot(ell,root)>0
    rank_gaps={i:dot(ell,root)**2-dot(ell,x[i])**2 for i in rest}
    assert min(rank_gaps.values())>0
    eta=min([F(1)]+[d/(2*(1+abs(dot(x[i],x[i])-dot(root,root)))) for i,d in rank_gaps.items()])
    assert eta>0
    M=tuple(tuple(ell[j]*ell[k]+(eta if j==k else 0) for k in range(3)) for j in range(3))
    def norm(p): return dot(p,tuple(dot(row,p) for row in M))
    gaps={i:norm(root)-norm(x[i]) for i in rest}
    assert min(gaps.values())>0
    return ell,eps,eta,M,gaps

def signed_hull_gauge(v,g,a):
    """Exact min l1 representation of the root by the remaining centred points.
    An optimal signed-hull boundary point lies in a face of dimension <=2;
    hence three signed generators suffice. Degenerate supports extend to bases.
    """
    x=[sub(p,g) for p in v]; candidates=[]
    for ids in combinations([i for i in range(len(v)) if i!=a],3):
        p,q,r=(x[i] for i in ids); d=det(p,q,r)
        if not d: continue
        c=(det(x[a],q,r)/d,det(p,x[a],r)/d,det(p,q,x[a])/d)
        assert tuple(sum(c[k]*x[ids[k]][j] for k in range(3)) for j in range(3))==x[a]
        candidates.append((sum(abs(t) for t in c),ids,c))
    assert candidates
    return min(candidates)

def root_controls():
    raw,faces=raw_input(); rawfaces,rawnormals,edges,vol,g=exact_geometry(raw,faces)
    scale=lcm(*(c.denominator for p in raw for c in p)); v=[tuple(int(scale*c) for c in p) for p in raw]; G=mul(scale,g)
    _,normals,_,_,_=exact_geometry(v,faces)
    adj={i:[] for i in range(len(v))}
    for a,b in edges: adj[a].append(b);adj[b].append(a)
    out={'theorem':'ROOT_SYMMETRIC_HULL_CENTROID_CORE_V1','scope':'Necessary root eligibility, not unique U or class110','parameters':{'r':'1/4','s':'1/4','eta':'1/4'},'raw_vertices':[qt(p) for p in raw],'faces':[list(f) for f in rawfaces],'edges':[list(e) for e in edges],'volume':qstr(vol),'actual_centroid':qt(g),'integer_scale':scale,'root_results':[]}
    for a in range(len(v)):
        inequalities={}
        for b in range(len(v)):
            if a==b: continue
            for h in common_fan_rays(v,a,b):
                # Distinct min vertices tied on a fan ray yield the same RHS.
                rhs=dot(h,add(v[a],v[b])); key=(h,rhs)
                inequalities[key]=dot(h,sub(add(v[a],v[b]),mul(2,G)))
        assert inequalities
        good=[(value,h,rhs) for (h,rhs),value in inequalities.items() if value>0]
        entry={'root':a,'core_inequalities':[{'normal':list(h),'rhs':rhs,'value_at_actual_centroid':qstr(value)} for (h,rhs),value in sorted(inequalities.items())],'eligible':bool(good)}
        rho,ids,coeff=signed_hull_gauge(v,G,a)
        assert (rho>1)==bool(good)
        entry['signed_hull_gauge']=qstr(rho)
        entry['l1_basis_certificate']={'vertices':list(ids),'coefficients':qt(coeff)}
        if good:
            _,h,_=max(good)
            n0=(0,0,0)
            for f,n in zip(rawfaces,normals):
                if a in f:
                    n=ray(n); n0=add(n0,n)
            assert all(dot(n0,sub(v[a],v[i]))>0 for i in range(len(v)) if i!=a)
            ell,eps,eta,M,gaps=metric_witness(v,G,a,h,n0)
            x=[sub(p,G) for p in v]
            ds={i:[dot(x[i],tuple(dot(row,sub(x[j],x[i])) for row in M)) for j in adj[i]] for i in adj}
            strict=[i for i,d in ds.items() if max(d)<0]; weak=[i for i,d in ds.items() if max(d)==0]
            assert a in strict and len(strict)==2 and not weak
            entry.update({'separating_linear_form_integer_frame':qt(ell),'normal_cone_perturbation':qstr(eps),'metric_eta':qstr(eta),'metric_integer_frame':[qt(row) for row in M],'minimum_squared_norm_gap':qstr(min(gaps.values())),'strict_unstable_vertices':strict,'weak_unstable_vertices':weak})
        else:
            assert max(inequalities.values())<=0
        out['root_results'].append(entry)
        print('ROOT',a,'ELIGIBLE',bool(good),'CORE_RAYS',len(inequalities),'U',entry.get('strict_unstable_vertices'),flush=True)
    return out

def main():
    p=argparse.ArgumentParser();p.add_argument('--output',default='root_core.json');args=p.parse_args()
    out=root_controls();data=(json.dumps(out,sort_keys=True,indent=2)+'\n').encode()
    with open(args.output,'wb') as f:f.write(data)
    print('OUTPUT',args.output,'BYTES',len(data),'SHA256',hashlib.sha256(data).hexdigest())
    print('END_ROOT_CORE_EXACT_OK')
if __name__=='__main__': main()
