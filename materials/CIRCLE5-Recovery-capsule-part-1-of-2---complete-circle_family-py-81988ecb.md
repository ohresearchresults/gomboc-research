# material-81988ecb6ea4

AI research material

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

"""Exact rational circular-section family and source-only polyhedron control.
Python >=3.11; numpy 2.3.5, scipy 1.17.0. All certifications use Fraction/int;
Qhull only nominates supporting triples and a closed exact complex is required.
Run: python circle_family.py --out out --m 5 --a 1/26 --mode aligned
"""
from __future__ import annotations
import argparse, hashlib, json, math
from fractions import Fraction as Q
from functools import reduce
from pathlib import Path
from itertools import combinations
import numpy as np
from scipy.spatial import ConvexHull

def add(a,b): return tuple(x+y for x,y in zip(a,b))
def sub(a,b): return tuple(x-y for x,y in zip(a,b))
def mul(t,a): return tuple(t*x for x in a)
def dot(a,b): return sum(x*y for x,y in zip(a,b))
def cross(a,b): return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def frac_json(x):
    if isinstance(x,Q): return str(x)
    if isinstance(x,(list,tuple)): return [frac_json(v) for v in x]
    if isinstance(x,dict): return {str(k):frac_json(v) for k,v in x.items()}
    if isinstance(x,np.integer): return int(x)
    return x

def point(x,r,u,a,aligned=True):
    assert x*x+r*r==1 and r>=0 and dot(u,u)==1 and 0<a<Q(1,25)
    C=r*(1-12*x*x+16*x**4); S=5*x-20*x**3+16*x**5
    assert C*C+S*S==1
    if aligned:
        b=a+r*u[0]; z=r*u[1]
        return (x,C*b-S*z,S*b+C*z)
    return (x,a*C+r*u[0],a*S+r*u[1])

def tangent(p):
    x,y,z,a=p
    r2=1-x*x
    # This routine takes the amplitude as a fourth entry and requires a rational
    # square root. At a tip the unique outward support is x=+/-1.
    if r2==0: return ((Q(1 if x>0 else -1),Q(0),Q(0)),Q(1))
    rn=math.isqrt(r2.numerator); rd=math.isqrt(r2.denominator)
    assert rn*rn==r2.numerator and rd*rd==r2.denominator
    r=Q(rn,rd); C=r*(1-12*x*x+16*x**4); S=5*x-20*x**3+16*x**5
    Cp=5*(-S)/r; Sp=5*C/r
    dy=y-a*C; dz=z-a*S
    n=(x-a*(dy*Cp+dz*Sp),dy,dz)
    return (n,dot(n,(x,y,z)))

def circle8():
    return [(Q(1),Q(0)),(Q(3,5),Q(4,5)),(Q(0),Q(1)),(Q(-3,5),Q(4,5)),(Q(-1),Q(0)),(Q(-3,5),Q(-4,5)),(Q(0),Q(-1)),(Q(3,5),Q(-4,5))]

def samples(m,a,aligned=True):
    if m<2: raise ValueError('m must be >=2')
    rows=[]
    for j in range(-m,m+1):
        t=Q(j,m); x=2*t/(1+t*t); r=(1-t*t)/(1+t*t)
        for u in ([(Q(1),Q(0))] if r==0 else circle8()): rows.append(point(x,r,u,a,aligned))
    return sorted(set(rows))

def integerize(points):
    points=[tuple(Q(c) for c in p) for p in points]
    D=math.lcm(*(c.denominator for p in points for c in p))
    return [tuple(int(c*D) for c in p) for p in points],D

def polygon_cycle(points,ids,n):
    drop=max(range(3),key=lambda k:abs(n[k])); ax=[k for k in range(3) if k!=drop]
    rows=sorted((points[i][ax[0]],points[i][ax[1]],i) for i in ids)
    def turn(a,b,c): return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])
    lo=[]; hi=[]
    for p in rows:
        while len(lo)>=2 and turn(lo[-2],lo[-1],p)<=0: lo.pop()
        lo.append(p)
    for p in reversed(rows):
        while len(hi)>=2 and turn(hi[-2],hi[-1],p)<=0: hi.pop()
        hi.append(p)
    cyc=[p[2] for p in lo[:-1]+hi[:-1]]
    assert len(cyc)>=3
    if dot(cross(sub(points[cyc[1]],points[cyc[0]]),sub(points[cyc[2]],points[cyc[1]])),n)<0: cyc.reverse()
    k=cyc.index(min(cyc)); return cyc[k:]+cyc[:k]

def exact_complex(points):
    P,D=integerize(points)
    if len(set(P))!=len(P): raise ValueError('duplicate input points')
    B=np.array([[float(Q(c,D)) for c in p] for p in P])
    trial=ConvexHull(B)
    planes={}
    for tri in trial.simplices:
        a,b,c=(P[int(i)] for i in tri); n=cross(sub(b,a),sub(c,a)); h=dot(n,a)
        if n==(0,0,0): continue
        signs=[dot(n,p)-h for p in P]
        if max(signs)>0 and min(signs)<0:
            raise ArithmeticError('Qhull nominated a non-supporting exact plane')
        if min(signs)==max(signs)==0: raise ArithmeticError('rank deficient input')
        if max(signs)>0: n=mul(-1,n); h=-h; signs=[-s for s in signs]
        g=math.gcd(*n,h); n=tuple(c//g for c in n); h//=g
        planes[n+(h,)]=[i for i,s in enumerate(signs) if s==0]
    faces=[]; normals=[]; supports=[]
    for row,ids in sorted(planes.items()):
        normals.append(row[:3]); supports.append(row[3]); faces.append(polygon_cycle(P,ids,row[:3]))
    used=sorted(set(i for f in faces for i in f)); index={j:i for i,j in enumerate(used)}
    faces=[[index[i] for i in f] for f in faces]; P=[P[i] for i in used]
    owners={}; oriented={}
    for fi,f in enumerate(faces):
        n=normals[fi]; h=supports[fi]
        assert all(dot(n,p)<=h for p in P)
        assert all(dot(n,P[i])==h for i in f)
        for i,j in zip(f,f[1:]+f[:1]):
            e=tuple(sorted((i,j))); owners.setdefault(e,[]).append(fi); oriented.setdefault(e,[]).append((i,j))
    assert all(len(v)==2 for v in owners.values()), 'exact complex is not closed'
    assert all(v[0]==v[1][::-1] for v in oriented.values()), 'orientation mismatch'
    assert len(P)-len(owners)+len(faces)==2
    # Connectedness together with convex support, maximal facet polygons, closure
    # and full-dimensional input certifies the complete convex boundary.
    seen={0}; stack=[0]; adj=[set() for p in P]
    for i,j in owners: adj[i].add(j); adj[j].add(i)
    while stack:
        for j in adj[stack.pop()]-seen: seen.add(j); stack.append(j)
    assert len(seen)==len(P)
    return P,D,faces,normals,supports,owners,adj

def mass(P,faces,origin=(0,0,0)):
    v6=0; m24=(0,0,0)
    for f in faces:
        a=sub(P[f[0]],origin)
        for i in range(1,len(f)-1):
            b=sub(P[f[i]],origin); c=sub(P[f[i+1]],origin)
            d=dot(a,cross(b,c)); v6+=d; m24=add(m24,mul(d,add(add(a,b),c)))
    assert v6>0
    return Q(v6,6),add(origin,tuple(Q(c,4*v6) for c in m24))

def census(points,landscape=False):
    P,D,faces,N,h,own,adj=exact_complex(points); V,c=mass(P,faces)
    mean=tuple(Q(sum(p[k] for p in P),len(P)) for k in range(3))
    V2,c2=mass(P,faces,mean); assert V2==V and c2==c
    # Independent coordinatewise divergence identities for volume and moment.
    fluxV=[Q(0)]*3; fluxM=[Q(0)]*3
    for f in faces:
        a=P[f[0]]
        for k in range(1,len(f)-1):
            b,d=P[f[k]],P[f[k+1]]; nn=cross(sub(b,a),sub(d,a))
            for j in range(3):
                fluxV[j]+=Q(nn[j]*(a[j]+b[j]+d[j]),6)
                ss=a[j]**2+b[j]**2+d[j]**2+a[j]*b[j]+a[j]*d[j]+b[j]*d[j]
                fluxM[j]+=Q(nn[j]*ss,24)
    assert all(v==V for v in fluxV) and tuple(m/V for m in fluxM)==c
    X=[sub(p,c) for p in P]; q=[]
    for n,b in zip(N,h):
        s=b-dot(n,c); assert s>0
        q.append(tuple(Q(v,s) for v in n))
    U=[]; Uw=[]; uz=0; S=[]; Sw=[]; sz=0; H=[]; Hw=[]; hz=0
    for i,x in enumerate(X):
        vals=[dot(x,sub(X[j],x)) for j in sorted(adj[i])]; uz+=sum(v==0 for v in vals)
        if max(vals)<0: U.append(i)
        elif max(vals)==0: Uw.append(i)
    face_adj=[set() for f in faces]
    for e,(i,j) in own.items(): face_adj[i].add(j); face_adj[j].add(i)
    for i,x in enumerate(q):
        vals=[dot(x,sub(q[j],x)) for j in sorted(face_adj[i])]; sz+=sum(v==0 for v in vals)
        if max(vals)<0: S.append(i)
        elif max(vals)==0: Sw.append(i)
        foot=mul(Q(h[i]-dot(N[i],c),dot(N[i],N[i])),N[i])
        fv=[dot(N[i],cross(sub(X[b],X[a]),sub(foot,X[a]))) for a,b in zip(faces[i],faces[i][1:]+faces[i][:1])]
        assert (min(fv)>0)==(i in S) and (min(fv)==0)==(i in Sw)
    for (i,j),(f,g) in sorted(own.items()):
        d=sub(X[j],X[i]); den=dot(d,d); t=-dot(X[i],d)/den; r=add(X[i],mul(t,d))
        a,b=N[f],N[g]; aa=dot(a,a); bb=dot(b,b); ab=dot(a,b)
        det=aa*bb-ab*ab; assert det>0
        A=dot(r,a)*bb-dot(r,b)*ab; B=dot(r,b)*aa-dot(r,a)*ab
        assert mul(det,r)==add(mul(A,a),mul(B,b))
        vals=[t,1-t,A,B]; hz+=sum(v==0 for v in vals)
        if min(vals)>0: H.append([i,j])
        elif min(vals)==0: Hw.append([i,j])
    out={'input_count':len(points),'V':len(P),'E':len(own),'F':len(faces),'C':2*len(own),
         'strict':[len(S),len(U),len(H)],'additional_weak':[len(Sw),len(Uw),len(Hw)],
         'primitive_zeros':[sz,uz,hz],'S':S,'U':U,'H':H,'weakS':Sw,'weakU':Uw,'weakH':Hw,
         'volume':V/Q(D**3),'centroid':tuple(v/D for v in c),
         'faces':faces,'edges':sorted(own),'hull_vertices':[tuple(Q(v,D) for v in p) for p in P]}
    if not any(out['additional_weak']): assert len(S)+len(U)-len(H)==2
    if landscape:
        out['P_landscape']=radial_landscape(X,sorted(own))
        out['Q_landscape']=radial_landscape(q,sorted(set(tuple(sorted(x)) for x in own.values())))
    return out

def radial_landscape(P,edges):
    vv=[dot(p,p) for p in P]; weights=[]
    for i,j in edges:
        a,b,c=vv[i],dot(P[i],P[j]),vv[j]
        z=a if b>=a else c if b>=c else (a*c-b*b)/(a+c-2*b)
        weights.append((z,i,j))
    parent=list(range(len(P))); members={i:{i} for i in range(len(P))}; peak=list(range(len(P)))
    def root(i):
        while parent[i]!=i: parent[i]=parent[parent[i]]; i=parent[i]
        return i
    bylevel={}
    for w,i,j in weights: bylevel.setdefault(w,[]).append((i,j))
    def path(start,stop,level):
        adj=[[] for p in P]
        for w,i,j in weights:
            if w>=level: adj[i].append(j); adj[j].append(i)
        queue=[start]; prev={start:None}
        for i in queue:
            if stop in prev: break
            for j in sorted(adj[i]):
                if j not in prev: prev[j]=i; queue.append(j)
        assert stop in prev
        out=[stop]
        while out[-1]!=start: out.append(prev[out[-1]])
        return out[::-1]
    bars=[]
    # Equal death levels are processed simultaneously. The reported component is
    # the whole STRICT-superlevel component, not a tie-order-dependent partial union.
    for level,ee in sorted(bylevel.items(),reverse=True):
        rr={}
        for i,j in ee:
            a,b=root(i),root(j)
            if a!=b: rr.setdefault(a,set()).add(b); rr.setdefault(b,set()).add(a)
        seen=set()
        for first in sorted(rr):
            if first in seen: continue
            group={first}; queue=[first]; seen.add(first)
            for a in queue:
                for b in rr[a]-seen: seen.add(b); group.add(b); queue.append(b)
            elder=max(group,key=lambda a:(vv[peak[a]],-peak[a])); epeak=peak[elder]
            for dyingroot in sorted(group-{elder}):
                dp=peak[dyingroot]; dying=members[dyingroot]
                if vv[dp]>level:
                    cut=[list(e) for e in edges if (e[0] in dying)!=(e[1] in dying)]
                    pp=path(dp,epeak,level)
                    wmap={tuple(sorted((i,j))):w for w,i,j in weights}
                    assert min(wmap[tuple(sorted((i,j)))] for i,j in zip(pp,pp[1:]))==level
                    bars.append({'peak':dp,'elder':epeak,'birth':vv[dp],'death':level,'relative_depth':(vv[dp]-level)/vv[dp],
                                 'component':sorted(dying),'cut':cut,'attaining_path':pp})
            for dyingroot in group-{elder}:
                parent[dyingroot]=elder; members[elder]|=members.pop(dyingroot)
    return {'vertex_radius2':vv,'edge_chord_min2':weights,'bars':bars}

def identities():
    # Exact finite polynomial identities; no numerical quadrature.
    import sympy as s
    x=s.symbols('x'); R=1-x*x; A=1-12*x*x+16*x**4; B=5*x-20*x**3+16*x**5
    assert s.expand(R*A*A+B*B-1)==0
    # Integral cos^3(t)*cos(5t)dt vanishes by orthogonality to cos(t),cos(3t).
    # Alternatively beta half-integer moments: int x^(2k)*(1-x^2)^(3/2) dx.
    I=sum(s.Poly(A,x).coeff_monomial(x**(2*k))*s.beta(s.Rational(2*k+1,2),s.Rational(5,2)) for k in range(3))
    assert s.simplify(s.expand_func(I.rewrite(s.gamma)))==0
    assert s.integrate((1-x*x)*B,(x,-1,1))==0
    # rho^6 * |d''/a|^2 =25*(25-24*x^2).
    f=s.sqrt(R)*A
    assert s.simplify(R**3*(s.diff(f,x,2)**2+s.diff(B,x,2)**2)-25*(25-24*x*x))==0
    print('CIRCLE5_EXACT_IDENTITIES_PASS')

def main():
    pa=argparse.ArgumentParser(); pa.add_argument('--out',default='circle_out'); pa.add_argument('--m',type=int,default=5); pa.add_argument('--a',default='1/26'); pa.add_argument('--mode',choices=['aligned','fixed'],default='aligned'); pa.add_argument('--no-landscape',action='store_true'); args=pa.parse_args()
    out=Path(args.out); out.mkdir(parents=True,exist_ok=True)
    identities(); a=Q(args.a); pts=samples(args.m,a,args.mode=='aligned')
    for p in pts:
        n,h=tangent((*p,a)); assert dot(n,p)==h
        assert all(dot(n,q)<=h for q in pts)
    data={'family':'CIRCLE5','amplitude':str(a),'m':args.m,'mode':args.mode,'points':frac_json(pts)}
    (out/'input.json').write_text(json.dumps(data,sort_keys=True,separators=(',',':'))+'\n')
    report=census(pts,not args.no_landscape)
    (out/'audit.json').write_text(json.dumps(frac_json(report),sort_keys=True,separators=(',',':'))+'\n')
    for key in ('V','E','F','C','strict','additional_weak','primitive_zeros','centroid'): print(key,report[key])
    for f in sorted(out.glob('*.json')): print(f.name,len(f.read_bytes()),hashlib.sha256(f.read_bytes()).hexdigest())
    print('CIRCLE5_EXACT_POLYHEDRON_PASS')
if __name__=='__main__': main()
