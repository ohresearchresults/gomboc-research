# material-5cd934dc55f8

AI research material

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

# C114_FINITE_ADDITIONS — Recovery capsule part 2/3

Same ordered recovery capsule and exact object identities as part1. This part contains the complete newly executed exact source units, with no omitted helpers. Read all three parts for campaign context, literal inputs, checkpoint freezing, replay and output assertions. Evidence is one full mechanical implementation with separately coded coordinate-boundary mass, not two full independent mechanical auditors. Controls tetrahedron446/weak000 and prism446/weak123 are observed. This implementation deliberately rejects a nomination containing a non-extreme point inside a coplanar maximal facet rather than pretending that it is a vertex; all retained inputs here pass. It is not a universal point-cloud preprocessing service. All output vertex indices retain original input labels, and face indices sort primitive integer support planes. These are not the original parent's raw-lex labels.

The exact elder code checks every positive true-edge bar, an attaining path and complete strict-upper cut, using Q at P's actual physical volume centroid. Cube enclosures are integer/rational. The cosine-hinge is the original root-exempt all-point squared negative-escape surrogate, evaluated exactly without square roots by selecting the smallest squared cosine when every escape is negative. It is not the full objective with discrete count/edge penalties and is not a basin metric.

@@FILE exact_addition.py 6947 130800bb8fd045a0399a04663cb193d728fbc7ed4379a6d5328ea5d4972cc079
"""Standalone exact maximal-hull / own-volume / S,U,H audit for rational point inputs.
Uses Python 3.13 standard library. Every decisive geometry comparison is exact.
One complete mechanical implementation plus distinct coordinate-boundary mass.
All indexed outputs use retained input labels, and lexicographically sorted planes.
"""
from fractions import Fraction as F
from functools import cmp_to_key
from itertools import combinations,product
from math import gcd,lcm
import json,sys,hashlib
from pathlib import Path

def dot(a,b):return sum(x*y for x,y in zip(a,b))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def add(a,b):return tuple(x+y for x,y in zip(a,b))
def mul(a,t):return tuple(x*t for x in a)
def cross(a,b):return(a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def det(a,b,c):return dot(a,cross(b,c))
def encode(x):
    if isinstance(x,F):return str(x)
    if isinstance(x,dict):return {str(k):encode(v) for k,v in x.items()}
    if isinstance(x,(list,tuple)):return [encode(v) for v in x]
    return x

def audit(points,grid=1):
    P=list(map(tuple,points));assert len(set(P))==len(P)
    planes={}
    for i,j,k in combinations(range(len(P)),3):
        n=cross(sub(P[j],P[i]),sub(P[k],P[i]));h=dot(n,P[i])
        if n==(0,0,0):continue
        ss=[dot(n,p)-h for p in P]
        if min(ss)>=0:n=mul(n,-1);h=-h;ss=[-x for x in ss]
        if max(ss)>0:continue
        div=gcd(gcd(gcd(abs(n[0]),abs(n[1])),abs(n[2])),abs(h))
        key=tuple(x//div for x in n)+(h//div,)
        planes[key]=[v for v,s in enumerate(ss) if s==0]
    faces=[]
    for key,ids in sorted(planes.items()):
        n=key[:3];base=P[ids[0]];v=sub(P[ids[1]],base);w=cross(n,v)
        # Sort in exact oriented plane coordinates around point average.
        N=len(ids);s=tuple(sum(P[i][j] for i in ids) for j in range(3))
        uv={i:(dot(sub(mul(P[i],N),s),v),dot(sub(mul(P[i],N),s),w)) for i in ids}
        def cmp(i,j):
            a,b=uv[i],uv[j];ha=(a[1]<0 or (a[1]==0 and a[0]<0));hb=(b[1]<0 or(b[1]==0 and b[0]<0))
            if ha!=hb:return 1 if ha else -1
            c=a[0]*b[1]-a[1]*b[0]
            return -1 if c>0 else 1 if c<0 else 0
        cyc=sorted(ids,key=cmp_to_key(cmp))
        for i,j in zip(cyc,cyc[1:]+cyc[:1]):
            vals=[dot(cross(sub(P[j],P[i]),sub(P[k],P[i])),n) for k in ids if k not in(i,j)]
            assert min(vals)>0,('non-extreme coplanar nomination',key)
        faces.append(dict(n=n,h=key[3],cycle=cyc))
    owners={};tri=[]
    for f,face in enumerate(faces):
        cyc=face['cycle']
        for i,j in zip(cyc,cyc[1:]+cyc[:1]):owners.setdefault(tuple(sorted((i,j))),[]).append(f)
        tri += [(cyc[0],cyc[k],cyc[k+1]) for k in range(1,len(cyc)-1)]
    verts=sorted(set(sum([x['cycle'] for x in faces],[])))
    assert len(verts)-len(owners)+len(faces)==2
    assert all(len(x)==2 for x in owners.values())
    # Connected vertex links and graph, true maximal complex, not just Euler.
    adj={i:set() for i in verts}
    for a,b in owners:adj[a].add(b);adj[b].add(a)
    seen={verts[0]};todo=list(seen)
    while todo:
        for j in adj[todo.pop()]-seen:seen.add(j);todo.append(j)
    assert len(seen)==len(verts)
    for i in verts:
        link={j:set() for j in adj[i]}
        for face in faces:
            c=face['cycle']
            if i in c:
                k=c.index(i);a,b=c[k-1],c[(k+1)%len(c)];link[a].add(b);link[b].add(a)
        assert all(len(x)==2 for x in link.values())
        reached={next(iter(link))};todo=list(reached)
        while todo:
            for j in link[todo.pop()]-reached:reached.add(j);todo.append(j)
        assert len(reached)==len(link)
    D=sum(det(P[a],P[b],P[c]) for a,b,c in tri);assert D>0
    N=tuple(sum(det(P[a],P[b],P[c])*(P[a][k]+P[b][k]+P[c][k]) for a,b,c in tri) for k in range(3))
    volume=F(D,6*grid**3);centroid=tuple(F(x,4*D*grid) for x in N)
    # Separate divergence integration: V=int_boundary x_k n_k, M_j=int_boundary x_j^2 n_j/2.
    vm=[];mm=[]
    for k in range(3):
        vtot=F(0);mtot=F(0)
        for a,b,c in tri:
            A=cross(sub(P[b],P[a]),sub(P[c],P[a]))[k]
            vals=[P[a][k],P[b][k],P[c][k]]
            vtot+=F(A*sum(vals),6)
            mtot+=F(A*(sum(vals)**2+sum(x*x for x in vals)),48)
        vm.append(vtot/grid**3);mm.append(mtot/grid**4)
    assert vm==[volume]*3 and all(mm[k]==volume*centroid[k] for k in range(3))
    X=[sub(mul(p,4*D),N) for p in P];nf=[f['n'] for f in faces];hf=[dot(f['n'],X[f['cycle'][0]]) for f in faces]
    assert min(hf)>0
    stable=[];weak_s=[];unst=[];weak_u=[];sad=[];weak_h=[];zeros=[0,0,0]
    for i,(n,h) in enumerate(zip(nf,hf)):
        vals=[hh*dot(n,n)-h*dot(nn,n) for j,(nn,hh) in enumerate(zip(nf,hf)) if j!=i]
        zeros[0]+=sum(v==0 for v in vals)
        if min(vals)>0:stable.append(i)
        elif min(vals)>=0:weak_s.append(i)
    for i in verts:
        vals=[dot(X[i],sub(X[j],X[i])) for j in adj[i]];zeros[1]+=sum(v==0 for v in vals)
        assert (max(vals)<0)==all(dot(X[i],sub(X[j],X[i]))<0 for j in verts if j!=i)
        if max(vals)<0:unst.append(i)
        elif max(vals)<=0:weak_u.append(i)
    for (a,b),(f,g) in sorted(owners.items()):
        e=sub(X[b],X[a]);dd=dot(e,e);t=-dot(X[a],e);w=add(mul(X[a],dd),mul(e,t));n,m=nf[f],nf[g]
        aa,bb,ab=dot(n,n),dot(m,m),dot(n,m);assert aa*bb-ab*ab>0
        ca=dot(w,n)*bb-dot(w,m)*ab;cb=dot(w,m)*aa-dot(w,n)*ab
        vals=[t,dd-t,ca,cb];zeros[2]+=sum(v==0 for v in vals)
        if min(vals)>0:sad.append([a,b])
        elif min(vals)>=0:weak_h.append([a,b])
    assert len(stable)+len(unst)-len(sad)==2 if not(weak_s or weak_u or weak_h) else True
    return dict(V=len(verts),E=len(owners),F=len(faces),C=2*len(owners),strict=[len(stable),len(unst),len(sad)],weak=[len(weak_s),len(weak_u),len(weak_h)],primitive_zeros=zeros,
      volume=volume,centroid=centroid,S=stable,U=unst,H=sad,weak_S=weak_s,weak_U=weak_u,weak_H=weak_h,faces=faces,edges=sorted(owners),active_inputs=verts,
      mass_method='oriented origin tetrahedra vs coordinate boundary divergence',common_centered_denominator_bits=lcm(*(F(x,4*D*grid).denominator for p in X for x in p)).bit_length())

def controls():
    tetra=[(1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1)]
    a=audit(tetra);assert a['strict']==[4,4,6] and a['weak']==[0,0,0]
    prism=[(x,y,z) for x,y in [(1,0),(1,1),(-2,-1)] for z in (-1,1)]
    a=audit(prism);assert a['strict']==[4,4,6] and a['weak']==[1,2,3],encode(a)
    print('ADDITION_TETRA446_PRISM446_WEAK123_CONTROLS_PASS')
if __name__=='__main__':
    controls()
    if len(sys.argv)>1:
        d=json.loads(Path(sys.argv[1]).read_text());a=audit(d['points'],d['grid']);raw=(json.dumps(encode(a),sort_keys=True,indent=2)+'\n').encode()
        out=Path(sys.argv[2] if len(sys.argv)>2 else 'AUDIT.json');out.write_bytes(raw)
        print('C114_EXACT_ADDITION_AUDIT_PASS',a['V'],a['E'],a['F'],a['strict'],a['weak'],len(raw),hashlib.sha256(raw).hexdigest())

@@END

@@FILE exact_landscape.py 4720 e65997173e5eb13d05d15f5a6989b4337be15aec6cc733c1a04468545ae1a964
"""Exact full primal/polar elder bars, attaining paths and complete cuts.
Q is the polar at P's physical volume centroid, never independently recentered.
Dependency: exact_addition.py. Python standard library only.
"""
from fractions import Fraction as F
from collections import deque
from pathlib import Path
import json,sys,hashlib
from exact_addition import audit,encode,dot,sub,add,mul
SCALE=10**12

def floor_cube_root(n):
    assert n>=0
    lo,hi=0,1<<((n.bit_length()+2)//3)
    while lo+1<hi:
        m=(lo+hi)//2
        if m**3<=n:lo=m
        else:hi=m
    return lo

def cube_bracket(r):
    """Enclose the positive cube root of an exact rational, no float."""
    assert r>=0
    z=floor_cube_root((r.numerator*SCALE**3)//r.denominator)
    assert F(z**3,SCALE**3)<=r<F((z+1)**3,SCALE**3)
    return [z,z+1]

def landscape(points,edges):
    radius={i:dot(p,p) for i,p in points.items()};adj={i:[] for i in points};events=[]
    for i,j in sorted(edges):
        d=sub(points[j],points[i]);dd=dot(d,d);assert dd>0
        t=min(F(1),max(F(0),-dot(points[i],d)/dd))
        p=add(points[i],mul(d,t));h=dot(p,p)
        assert h<=min(radius[i],radius[j])
        events.append((h,i,j));adj[i].append((j,h));adj[j].append((i,h))
    parent={i:i for i in points}
    def find(i):
        while parent[i]!=i:parent[i]=parent[parent[i]];i=parent[i]
        return i
    bars=[]
    for death,i,j in sorted(events,reverse=True):
        a,b=find(i),find(j)
        if a==b:continue
        if (radius[a],-a)<(radius[b],-b):a,b=b,a
        delta=radius[b]-death;assert delta>=0
        if delta>0:
            cut={b};todo=[b]
            while todo:
                k=todo.pop()
                for v,h in adj[k]:
                    if h>death and v not in cut:cut.add(v);todo.append(v)
            assert a not in cut
            boundary=sorted((u,v) for u in cut for v,h in adj[u] if v not in cut)
            assert boundary and all(h<=death for u in cut for v,h in adj[u] if v not in cut)
            pred={b:None};todo=deque([b])
            while todo and a not in pred:
                k=todo.popleft()
                for v,h in sorted(adj[k]):
                    if h>=death and v not in pred:pred[v]=k;todo.append(v)
            assert a in pred
            path=[a]
            while path[-1]!=b:path.append(pred[path[-1]])
            path.reverse()
            assert min(next(h for v,h in adj[u] if v==w) for u,w in zip(path,path[1:]))==death
            bars.append(dict(peak=b,elder=a,death_edge=[i,j],birth=radius[b],death=death,depth=delta,path=path,component=sorted(cut),boundary=boundary))
        parent[b]=a
    roots=sorted(i for i,p in points.items() if all(dot(p,sub(points[j],p))<0 for j,h in adj[i]))
    assert len(bars)==len(roots)-1
    global_root=max(points,key=lambda i:(radius[i],-i));hinge=F(0)
    for i,p in points.items():
        if i==global_root:continue
        terms=[(dot(p,sub(q,p)),dot(sub(q,p),sub(q,p))) for j,q in points.items() if j!=i]
        if all(v<0 for v,dd in terms):hinge+=min(v*v/(radius[i]*dd) for v,dd in terms)
    return dict(roots=roots,bars=bars,radius2=max(radius.values()),sum_depth=sum((b['depth'] for b in bars),F(0)),root_exempt_allpoint_cosine_hinge_sum=hinge)

def run(d):
    A=audit(d['points'],d['grid']);assert A['weak']==[0,0,0]
    P={i:sub(tuple(F(x,d['grid']) for x in d['points'][i]),A['centroid']) for i in A['active_inputs']}
    Q={i:mul(f['n'],1/(F(f['h'],d['grid'])-dot(f['n'],A['centroid']))) for i,f in enumerate(A['faces'])}
    owners={}
    for i,f in enumerate(A['faces']):
        c=f['cycle']
        for u,v in zip(c,c[1:]+c[:1]):owners.setdefault(tuple(sorted((u,v))),[]).append(i)
    assert all(len(v)==2 for v in owners.values())
    Lp=landscape(P,A['edges']);Lq=landscape(Q,list(map(tuple,owners.values())))
    assert Lp['roots']==A['U'] and Lq['roots']==A['S']
    V=A['volume'];pc=Lp['sum_depth']**3/V**2;qc=Lq['sum_depth']**3*V**2
    return dict(V=A['V'],E=A['E'],F=A['F'],strict=A['strict'],weak=A['weak'],volume=V,P=Lp,Q=Lq,
       TP_cube=pc,TQ_cube=qc,TP_bracket_1e12=cube_bracket(pc),TQ_bracket_1e12=cube_bracket(qc),
       relative_P_bracket_1e12=[int(Lp['sum_depth']/Lp['radius2']*SCALE),int(Lp['sum_depth']/Lp['radius2']*SCALE)+1],
       relative_Q_bracket_1e12=[int(Lq['sum_depth']/Lq['radius2']*SCALE),int(Lq['sum_depth']/Lq['radius2']*SCALE)+1])

if __name__=='__main__':
    d=json.loads(Path(sys.argv[1]).read_text());r=run(d)
    raw=(json.dumps(encode(r),sort_keys=True,indent=2)+'\n').encode()
    out=Path(sys.argv[2]);out.write_bytes(raw)
    print('C114_EXACT_FULL_ELDER_PATH_CUT_PASS',r['strict'],r['TP_bracket_1e12'],r['TQ_bracket_1e12'],len(raw),hashlib.sha256(raw).hexdigest())

@@END
