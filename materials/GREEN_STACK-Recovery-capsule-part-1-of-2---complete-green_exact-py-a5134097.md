# material-a5134097f1d3

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

---

"""Exact homogeneous C2 Green-stack recovery and full equilibrium/landscape audit.
Python standard library only. Input fractions are [numerator, denominator].
The support-plane completeness proof is in GREEN_STACK_THEOREM.md.
"""
from fractions import Fraction as F
from collections import defaultdict
from functools import reduce
import sys,json,hashlib,math
from pathlib import Path

def ff(x): return F(*x) if isinstance(x,list) else F(x)
def add(a,b): return tuple(x+y for x,y in zip(a,b))
def sub(a,b): return tuple(x-y for x,y in zip(a,b))
def mul(a,s): return tuple(x*s for x in a)
def dot(a,b): return sum((x*y for x,y in zip(a,b)),F(0))
def cross(a,b): return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def primitive(a):
    D=math.lcm(*(x.denominator for x in a)); z=[int(x*D) for x in a]
    g=math.gcd(*z); assert g
    return tuple(x//g for x in z)
def pack(x):
    if isinstance(x,F): return [x.numerator,x.denominator]
    if isinstance(x,dict): return {str(k):pack(v) for k,v in x.items()}
    if isinstance(x,(list,tuple)): return [pack(v) for v in x]
    return x

def polygon_area_centroid(poly):
    zz=[poly[i][0]*poly[(i+1)%len(poly)][1]-poly[i][1]*poly[(i+1)%len(poly)][0] for i in range(len(poly))]
    twice=sum(zz); assert twice>0
    cc=tuple(sum((poly[i][j]+poly[(i+1)%len(poly)][j])*zz[i] for i in range(len(poly)))/(3*twice) for j in range(2))
    return twice/2,cc

def generate(inp):
    k=int(inp['k']); n=3; m=2*k+1
    K=[(F(1),F(0)),(F(-1,2),F(1)),(F(-1,2),F(-1))]
    ax=[F(-1)]+[2*t/(1+t*t) for t in (F(19,20)*F(i-k,k) for i in range(m))]+[F(1)]
    ap=list(map(ff,inp['curvatures'])); assert len(ap)==k+1 and min(ap)>0
    aa=ap[:0:-1]+ap
    ws=[[ff(v) for v in row] for row in inp['positive_barycentric']]
    assert len(ws)==k and all(len(w)==n and min(w)>0 for w in ws)
    ws=[[v/sum(w) for v in w] for w in ws]
    kp=[tuple(sum(w[j]*K[j][c] for j in range(n)) for c in range(2)) for w in ws]
    kk=[(p[0],-p[1]) for p in kp[::-1]]+[(F(-1,2),F(0))]+kp
    def green(x,t): return (x+1)*(1-t)/2 if x<=t else (t+1)*(1-x)/2
    RR=[];DD=[]
    for x in ax:
        h=[a*green(x,t) for a,t in zip(aa,ax[1:-1])]
        RR.append(sum(h)); DD.append(tuple(-sum(v*p[j] for v,p in zip(h,kk)) for j in range(2)))
    r0=RR[k+1];assert r0>0
    r=[z/r0 for z in RR]
    alpha=ff(inp['alpha']); lam=ff(inp['lambda']); beta=ff(inp['beta']);assert lam>0 and beta>0
    xx=[lam*x for x in ax]
    dd=[(d[0]/r0,d[1]/r0+alpha*x) for x,d in zip(ax,DD)]
    # Cross-sectional finite mass, independent of any triangulation.
    weights=[F(0) for x in xx]
    for i,(a,b) in enumerate(zip(r,r[1:])):
        dx=xx[i+1]-xx[i]
        weights[i]+=dx*(3*a*a+2*a*b+b*b)/12
        weights[i+1]+=dx*(a*a+2*a*b+3*b*b)/12
    area,pc=polygon_area_centroid(K);assert pc==(0,0)
    vol=area*beta*sum(weights)
    cen=tuple(sum(w*c[j] for w,c in zip(weights,[(x,d[0],beta*d[1]) for x,d in zip(xx,dd)]))/sum(weights) for j in range(3))
    assert cen[0]==cen[2]==0
    v=[(xx[0],dd[0][0],beta*dd[0][1])]
    for x,d,s in zip(xx[1:-1],dd[1:-1],r[1:-1]):
        v.extend((x,d[0]+s*p[0],beta*(d[1]+s*p[1])) for p in K)
    v.append((xx[-1],dd[-1][0],beta*dd[-1][1]))
    # Three support directions, each piecewise-affine support profile.
    planes=set(); slope_bank=[]
    for j,p in enumerate(K):
        p1=K[(j+1)%n];normal=(p1[1]-p[1],p[0]-p1[0]);h=dot(normal,p)
        B=[dot(normal,d)+h*s for d,s in zip(dd,r)]
        slopes=[(b-a)/(y-x) for a,b,x,y in zip(B,B[1:],xx,xx[1:])]
        assert all(b<=a for a,b in zip(slopes,slopes[1:])), 'nonconvex support profile'
        slope_bank.append(slopes)
        for i,s in enumerate(slopes):
            N=(-s,normal[0],normal[1]/beta);H=B[i]-s*xx[i]
            planes.add(primitive((*N,H)))
    # The centre of an actual full-dimensional bounded convex volume is interior.
    centred=[sub(p,cen) for p in v]
    cplanes=[]
    for row in sorted(planes):
        N=tuple(F(x) for x in row[:3]);H=F(row[3])-dot(N,cen); assert H>0
        cplanes.append((N,H))
    return centred,cplanes,vol,cen,weights,slope_bank

def face_cycle(v,ids,N):
    # Rational planar monotone-chain hull, deleting collinear nonvertices.
    drop=max(range(3),key=lambda j:abs(N[j])); dims=[j for j in range(3) if j!=drop]
    ids=sorted(ids,key=lambda i:(v[i][dims[0]],v[i][dims[1]]))
    def orient(i,j,k):
        a,b,c=(v[t] for t in (i,j,k));u,w=dims
        return (b[u]-a[u])*(c[w]-a[w])-(b[w]-a[w])*(c[u]-a[u])
    lo=[];hi=[]
    for i in ids:
        while len(lo)>1 and orient(lo[-2],lo[-1],i)<=0:lo.pop()
        lo.append(i)
    for i in ids[::-1]:
        while len(hi)>1 and orient(hi[-2],hi[-1],i)<=0:hi.pop()
        hi.append(i)
    cyc=lo[:-1]+hi[:-1]; assert len(cyc)>=3
    if dot(cross(sub(v[cyc[1]],v[cyc[0]]),sub(v[cyc[2]],v[cyc[0]])),N)<0:cyc.reverse()
    return cyc

def complex_from_planes(v,planes):
    faces=[];cp=[]
    for N,h in planes:
        vals=[h-dot(N,p) for p in v];assert min(vals)>=0
        ids=[i for i,z in enumerate(vals) if not z];assert len(ids)>=3
        faces.append(face_cycle(v,ids,N));cp.append((N,h))
    used=sorted(set(sum(faces,[])));assert used==list(range(len(v))), 'input contains a nonextreme point'
    owners=defaultdict(list);orients=defaultdict(list)
    for f,cyc in enumerate(faces):
        for a,b in zip(cyc,cyc[1:]+cyc[:1]):
            e=tuple(sorted((a,b)));owners[e].append(f);orients[e].append(a<b)
    assert all(len(x)==2 for x in owners.values())
    assert all(x[0]!=x[1] for x in orients.values())
    E=sorted(owners);assert len(v)-len(E)+len(faces)==2
    return faces,E,[owners[e] for e in E],cp

def tetra_mass(v,faces,origin=(F(0),)*3):
    vol=F(0);moment=(F(0),)*3
    for face in faces:
        a=v[face[0]]
        for ib,ic in zip(face[1:-1],face[2:]):
            b,c=v[ib],v[ic];w=dot(sub(a,origin),cross(sub(b,origin),sub(c,origin)))/6
            assert w>=0
            vol+=w;moment=add(moment,mul(add(add(add(origin,a),b),c),w/4))
    return vol,moment

def equilibrium(v,planes,E,EF,faces):
    q=[mul(N,1/h) for N,h in planes]
    out=[[] for p in v];qout=[[] for p in q]
    for (a,b),(f,g) in zip(E,EF):
        out[a].append(dot(v[a],sub(v[b],v[a])));out[b].append(dot(v[b],sub(v[a],v[b])))
        qout[f].append(dot(q[f],sub(q[g],q[f])));qout[g].append(dot(q[g],sub(q[f],q[g])))
    U=[i for i,l in enumerate(out) if max(l)<0];WU=[i for i,l in enumerate(out) if max(l)==0]
    S=[i for i,l in enumerate(qout) if max(l)<0];WS=[i for i,l in enumerate(qout) if max(l)==0]
    # Independent face-foot membership check against all true face boundaries.
    S2=[];WS2=[]
    for f,(N,h) in enumerate(planes):
        foot=mul(N,h/dot(N,N));cyc=faces[f]
        z=[dot(N,cross(sub(v[b],v[a]),sub(foot,v[a]))) for a,b in zip(cyc,cyc[1:]+cyc[:1])]
        if min(z)>0:S2.append(f)
        elif min(z)==0:WS2.append(f)
    assert S==S2 and WS==WS2
    saddles=[];weakH=[];zeroH=[]
    for e,fg in zip(E,EF):
        a,b=e;f,g=fg;d=sub(v[b],v[a]);t=-dot(v[a],d)/dot(d,d);foot=add(v[a],mul(d,t))
        A,h=planes[f];B,hb=planes[g];aa=dot(A,A);bb=dot(B,B);ab=dot(A,B);det=aa*bb-ab*ab;assert det>0
        al=(dot(foot,A)*bb-dot(foot,B)*ab)/det;be=(dot(foot,B)*aa-dot(foot,A)*ab)/det
        assert foot==add(mul(A,al),mul(B,be))
        if 0<t<1 and al>0 and be>0:saddles.append(e)
        elif 0<=t<=1 and al>=0 and be>=0:weakH.append(e)
        if t in (0,1) or al==0 or be==0:zeroH.append(e)
    assert len(S)+len(U)-len(saddles)==2, 'Morse count failed'
    return dict(S=S,U=U,H=saddles,weakS=WS,weakU=WU,weakH=weakH,
        physical_zero_arrows=sum(z==0 for row in out for z in row),polar_zero_arrows=sum(z==0 for row in qout for z in row),mixed_zero_edges=zeroH),q

def chord_min(a,b):
    A=dot(a,a);B=dot(a,b);C=dot(b,b)
    if B>=A:return A
    if B>=C:return C
    return (A*C-B*B)/(A+C-2*B)

def landscape(v,E):
    levels=[dot(p,p) for p in v];death=[chord_min(v[a],v[b]) for a,b in E]
    events=defaultdict(lambda: [[],[]])
    for i,z in enumerate(levels):events[z][0].append(i)
    for i,z in enumerate(death):events[z][1].append(i)
    parent=list(range(len(v)));members={};peak={};bars=[]
    def root(i):
        while parent[i]!=i:parent[i]=parent[parent[i]];i=parent[i]
        return i
    for level,(birth,edgeids) in sorted(events.items(),reverse=True):
        for i in birth:members[i]={i};peak[i]=i
        # Batch all connections at this exact level BEFORE choosing the elder.
        graph=defaultdict(set)
        for ei in edgeids:
            a,b=E[ei];ra,rb=root(a),root(b)
            if ra!=rb:graph[ra].add(rb);graph[rb].add(ra)
        seen=set()
        for start in sorted(graph):
            if start in seen:continue
            group=[];todo=[start];seen.add(start)
            while todo:
                a=todo.pop();group.append(a)
                for b in graph[a]:
                    if b not in seen:seen.add(b);todo.append(b)
            elder=min(group,key=lambda a:(-levels[peak[a]],peak[a]));ep=peak[elder]
            for rr in group:
                if rr==elder:continue
                p=peak[rr];comp=members[rr].copy()
                if levels[p]>level:
                    boundary=[(a,b) if a in comp else (b,a) for a,b in E if (a in comp)!=(b in comp)]
                    # An attaining path in the level-supergraph to the elder peak.
                    adj=defaultdict(list)
                    for (a,b),w in zip(E,death):
                        if w>=level:adj[a].append(b);adj[b].append(a)
                    pathparent={p:None};todo=[p]
                    for a in todo:
                        if a==ep:break
                        for b in adj[a]:
                            if b not in pathparent:pathparent[b]=a;todo.append(b)
                    assert ep in pathparent
                    path=[];cur=ep
                    while cur is not None:path.append(cur);cur=pathparent[cur]
                    path.reverse()
                    attaining=[tuple(sorted((a,b))) for a,b in zip(path,path[1:]) if chord_min(v[a],v[b])==level]
                    assert attaining
                    bars.append(dict(peak=p,elder=ep,birth=levels[p],death=level,depth=levels[p]-level,
                        component=sorted(comp),boundary=sorted(boundary),path=path,attaining_edges=attaining))
            allmem=set().union(*(members[rr] for rr in group))
            for rr in group:
                if rr!=elder:parent[rr]=elder;del members[rr];del peak[rr]
            members[elder]=allmem
    assert len(members)==1
    return dict(roots=sorted([b['peak'] for b in bars]+list(peak.values())),bars=bars)

def run(inp):
    v,planes,volume,centroid,weights,slopes=generate(inp)
    faces,E,EF,planes=complex_from_planes(v,planes)
    v1,m1=tetra_mass(v,faces);assert v1==volume and m1==(0,0,0)
    # A second strictly interior rational origin; actual COM is exactly zero.
    o=mul(v[0],F(1,17));v2,m2=tetra_mass(v,faces,o);assert v2==volume and m2==(0,0,0)
    # Independent directional divergence volumes and first moments.
    flux=[];momflux=[]
    for axis in range(3):
        av=F(0);am=[F(0)]*3
        for face in faces:
            a=v[face[0]]
            for ib,ic in zip(face[1:-1],face[2:]):
                b,c=v[ib],v[ic];w=cross(sub(b,a),sub(c,a))[axis]
                av+=w*(a[axis]+b[axis]+c[axis])/6
                for j in range(3):
                    s=(a[axis]+b[axis]+c[axis])*(a[j]+b[j]+c[j])+a[axis]*a[j]+b[axis]*b[j]+c[axis]*c[j]
                    am[j]+=w*s/F(48 if axis==j else 24)
        assert av==volume and tuple(am)==(0,0,0);flux.append(av);momflux.append(am)
    eq,q=equilibrium(v,planes,E,EF,faces)
    P=landscape(v,E);Q=landscape(q,[tuple(x) for x in EF])
    assert P['roots']==eq['U'] and Q['roots']==eq['S']
    out=dict(identity=inp['identity'],V=len(v),E=len(E),F=len(faces),C=2*len(E),strict=[len(eq[x]) for x in ('S','U','H')],
       weak=[len(eq[x]) for x in ('weakS','weakU','weakH')],volume=volume,raw_centroid=centroid,
       vertices=v,planes=planes,faces=faces,edges=E,edge_faces=EF,equilibria=eq,P=P,Q=Q,
       mass_checks='exact slab + two tetra origins + three directional divergence moments')
    return out

if __name__=='__main__':
    p=Path(sys.argv[1]);inp=json.loads(p.read_text());out=run(inp)
    dest=Path(inp['identity']+'_AUDIT.json');data=(json.dumps(pack(out),sort_keys=True,separators=(',',':'))+'\n').encode();dest.write_bytes(data)
    print('GREEN_EXACT_CENSUS',out['identity'],out['V'],out['E'],out['F'],out['strict'],out['weak'])
    print('GREEN_EXACT_PQ_PACKETS',[(len(b['component']),len(b['boundary'])) for b in out['P']['bars']],[(len(b['component']),len(b['boundary'])) for b in out['Q']['bars']])
    print('GREEN_EXACT_OUTPUT',str(dest),len(data),hashlib.sha256(data).hexdigest())
    print('GREEN_EXACT_HOMOTHETIC_MASS_MECHANICS_PASS')
