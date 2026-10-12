# material-996619e62e24

AI research material

---

"""Exact independent-support Green polyhedra and complete centre-line intervals.
Standard library only. Fractions are encoded as [numerator, denominator].
Usage: python igs_exact.py INPUT.json. No floating computation decides a sign.
"""
from fractions import Fraction as R
from collections import defaultdict
from pathlib import Path
import json, math, sys, hashlib

def F(a):return R(*a) if isinstance(a,list) else R(a)
def add(a,b):return tuple(x+y for x,y in zip(a,b))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def mul(a,s):return tuple(x*s for x in a)
def dot(a,b):return sum((x*y for x,y in zip(a,b)),R(0))
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def primitive(row):
    D=math.lcm(*(x.denominator for x in row)); z=[int(x*D) for x in row]; g=math.gcd(*z);assert g
    return tuple(x//g for x in z)
def pack(o):
    if isinstance(o,R):return [o.numerator,o.denominator]
    if isinstance(o,dict):return {str(k):pack(v) for k,v in o.items()}
    if isinstance(o,(list,tuple)):return [pack(v) for v in o]
    return o

def generate(inp):
    n=int(inp['n']);k=int(inp['k']);m=2*k+1;west=(n-1)//2
    N=[tuple(map(F,z)) for z in inp['normals']]; assert len(N)==n and n%2 and k>0
    assert N[west]==(-1,0) and all(N[n-1-j]==(p[0],-p[1]) for j,p in enumerate(N))
    ap=[tuple(map(F,z)) for z in inp['positive_curvatures']];assert len(ap)==k+1
    assert ap[0][west]==0 and ap[0]==ap[0][::-1]
    assert all(a>0 for i,row in enumerate(ap) for j,a in enumerate(row) if (i,j)!=(0,west))
    aa=[row[::-1] for row in ap[:0:-1]]+ap
    ax=[R(-1)]+[2*t/(1+t*t) for t in (R(19,20)*R(i-k,k) for i in range(m))]+[R(1)]
    def G(x,t):return ((x+1)*(1-t) if x<=t else (t+1)*(1-x))/2
    h=[tuple(sum(a[j]*G(x,t) for a,t in zip(aa,ax[1:-1])) for j in range(n)) for x in ax]
    rings=[]
    for hh in h:
        row=[]
        for j in range(n):
            a,b=N[j-1],N[j]; A,B=hh[j-1],hh[j]; det=a[0]*b[1]-a[1]*b[0];assert det>0
            p=((A*b[1]-a[1]*B)/det,(a[0]*B-A*b[0])/det)
            assert all(dot(q,p)<=v for q,v in zip(N,hh))
            row.append(p)
        rings.append(row)
    assert all(rings[i][j]!=rings[i][(j+1)%n] for i in range(1,m+1) for j in range(n))
    lam,beta,alpha=map(F,inp['metric']);assert lam>0 and beta>0
    def world(x,p):return (lam*x,p[0],beta*(p[1]+alpha*x))
    v=[world(ax[0],rings[0][0])]+[world(x,p) for x,row in zip(ax[1:-1],rings[1:-1]) for p in row]+[world(ax[-1],rings[-1][0])]
    planes=set()
    for j,(u,w) in enumerate(N):
        slopes=[(b[j]-a[j])/(lam*(y-x)) for a,b,x,y in zip(h,h[1:],ax,ax[1:])]
        assert all(a>=b for a,b in zip(slopes,slopes[1:]))
        for i,s in enumerate(slopes):planes.add(primitive((-s-w*alpha/lam,u,w/beta,h[i][j]-s*lam*ax[i])))
    return v,[(tuple(map(R,z[:3])),R(z[3])) for z in sorted(planes)],ax,rings,(lam,beta,alpha)

def face_cycle(v,ids,N):
    drop=max(range(3),key=lambda j:abs(N[j]));a,b=[j for j in range(3) if j!=drop]
    ids=sorted(ids,key=lambda i:(v[i][a],v[i][b]))
    def orient(i,j,k):return (v[j][a]-v[i][a])*(v[k][b]-v[i][b])-(v[j][b]-v[i][b])*(v[k][a]-v[i][a])
    lo=[];hi=[]
    for i in ids:
        while len(lo)>1 and orient(lo[-2],lo[-1],i)<=0:lo.pop()
        lo.append(i)
    for i in ids[::-1]:
        while len(hi)>1 and orient(hi[-2],hi[-1],i)<=0:hi.pop()
        hi.append(i)
    cyc=lo[:-1]+hi[:-1];assert len(cyc)>=3
    if dot(cross(sub(v[cyc[1]],v[cyc[0]]),sub(v[cyc[2]],v[cyc[0]])),N)<0:cyc.reverse()
    return cyc

def complex_from_planes(v,planes):
    faces=[];owners=defaultdict(list);directions=defaultdict(list)
    for N,H in planes:
        z=[H-dot(N,p) for p in v];assert min(z)>=0
        cyc=face_cycle(v,[i for i,a in enumerate(z) if not a],N);faces.append(cyc)
    assert set(sum(faces,[]))==set(range(len(v)))
    for f,cyc in enumerate(faces):
        for a,b in zip(cyc,cyc[1:]+cyc[:1]):owners[tuple(sorted((a,b)))].append(f);directions[tuple(sorted((a,b)))].append(a<b)
    E=sorted(owners);assert all(len(z)==2 for z in owners.values()) and all(a!=b for a,b in directions.values())
    assert len(v)-len(E)+len(faces)==2
    return faces,E,[owners[e] for e in E]

def tetra_mass(v,faces,o):
    vol=R(0);moment=(R(0),)*3
    for f in faces:
        a=v[f[0]]
        for j in range(1,len(f)-1):
            b,c=v[f[j]],v[f[j+1]];w=dot(sub(a,o),cross(sub(b,o),sub(c,o)))/6;assert w>=0
            vol+=w;moment=add(moment,mul(add(add(add(o,a),b),c),w/4))
    return vol,moment

def slab_mass(ax,rings,metric):
    # Vertex sections vary linearly, so area is quadratic and each first moment cubic.
    # The rational 3/8 rule integrates all these polynomials exactly, not approximately.
    lam,beta,alpha=metric;V=R(0);M=(R(0),)*3
    for xl,xr,pl,pr in zip(ax,ax[1:],rings,rings[1:]):
        for t,w in ((R(0),R(1,8)),(R(1,3),R(3,8)),(R(2,3),R(3,8)),(R(1),R(1,8))):
            x=(1-t)*xl+t*xr;pp=[add(mul(a,1-t),mul(b,t)) for a,b in zip(pl,pr)]
            pp=[(p[0],beta*(p[1]+alpha*x)) for p in pp]
            zz=[a[0]*b[1]-a[1]*b[0] for a,b in zip(pp,pp[1:]+pp[:1])];area=sum(zz)/2;assert area>=0
            mm=[sum((a[j]+b[j])*z for a,b,z in zip(pp,pp[1:]+pp[:1],zz))/6 for j in range(2)]
            factor=w*lam*(xr-xl);V+=factor*area;M=add(M,mul((lam*x*area,*mm),factor))
    return V,M

def equilibrium(v,planes,faces,E,EF):
    q=[mul(N,1/H) for N,H in planes];out=[[] for p in v];qo=[[] for p in q]
    for (a,b),(f,g) in zip(E,EF):
        out[a].append(dot(v[a],sub(v[b],v[a])));out[b].append(dot(v[b],sub(v[a],v[b])))
        qo[f].append(dot(q[f],sub(q[g],q[f])));qo[g].append(dot(q[g],sub(q[f],q[g])))
    U=[i for i,z in enumerate(out) if max(z)<0];WU=[i for i,z in enumerate(out) if max(z)==0]
    S=[i for i,z in enumerate(qo) if max(z)<0];WS=[i for i,z in enumerate(qo) if max(z)==0]
    S2=[];WS2=[]
    for i,((N,H),f) in enumerate(zip(planes,faces)):
        foot=mul(N,H/dot(N,N));vals=[dot(N,cross(sub(v[b],v[a]),sub(foot,v[a]))) for a,b in zip(f,f[1:]+f[:1])]
        if min(vals)>0:S2.append(i)
        elif min(vals)==0:WS2.append(i)
    assert (S,WS)==(S2,WS2)
    HS=[];WH=[];Z=[]
    for (a,b),(f,g) in zip(E,EF):
        d=sub(v[b],v[a]);t=-dot(v[a],d)/dot(d,d);p=add(v[a],mul(d,t));A=planes[f][0];B=planes[g][0]
        aa,bb,ab=dot(A,A),dot(B,B),dot(A,B);det=aa*bb-ab*ab;assert det>0
        u=(dot(p,A)*bb-dot(p,B)*ab)/det;w=(dot(p,B)*aa-dot(p,A)*ab)/det
        assert p==add(mul(A,u),mul(B,w))
        if 0<t<1 and u>0 and w>0:HS.append((a,b))
        elif 0<=t<=1 and u>=0 and w>=0:WH.append((a,b))
        if t in (0,1) or u==0 or w==0:Z.append((a,b))
    assert len(S)+len(U)-len(HS)==2
    return dict(S=S,U=U,H=HS,weakS=WS,weakU=WU,weakH=WH,zeroPhysical=sum(z==0 for row in out for z in row),zeroPolar=sum(z==0 for row in qo for z in row),zeroMixed=Z),q

def chord_min(a,b):
    A,B,C=dot(a,a),dot(a,b),dot(b,b)
    if B>=A:return A
    if B>=C:return C
    return (A*C-B*B)/(A+C-2*B)

def landscape(v,E):
    levels=[dot(p,p) for p in v];deaths=[chord_min(v[a],v[b]) for a,b in E];events=defaultdict(lambda:[[],[]])
    for i,z in enumerate(levels):events[z][0].append(i)
    for i,z in enumerate(deaths):events[z][1].append(i)
    parent=list(range(len(v)));members={};peak={};bars=[]
    def root(a):
        while parent[a]!=a:parent[a]=parent[parent[a]];a=parent[a]
        return a
    for level,(birth,edgeids) in sorted(events.items(),reverse=True):
        for i in birth:members[i]={i};peak[i]=i
        graph=defaultdict(set)
        for i in edgeids:
            a,b=map(root,E[i])
            if a!=b:graph[a].add(b);graph[b].add(a)
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
                    adj=defaultdict(list)
                    for (a,b),z in zip(E,deaths):
                        if z>=level:adj[a].append(b);adj[b].append(a)
                    prev={p:None};todo=[p]
                    for a in todo:
                        if a==ep:break
                        for b in adj[a]:
                            if b not in prev:prev[b]=a;todo.append(b)
                    assert ep in prev;path=[];cur=ep
                    while cur is not None:path.append(cur);cur=prev[cur]
                    path.reverse();attaining=[tuple(sorted((a,b))) for a,b in zip(path,path[1:]) if chord_min(v[a],v[b])==level];assert attaining
                    bars.append(dict(peak=p,elder=ep,birth=levels[p],death=level,relative=(levels[p]-level)/levels[p],component=sorted(comp),boundary=sorted(boundary),path=path,attaining_edges=attaining))
            total=set().union(*(members[a] for a in group))
            for a in group:
                if a!=elder:parent[a]=elder;del members[a];del peak[a]
            members[elder]=total
    assert len(members)==1
    return dict(roots=sorted([b['peak'] for b in bars]+list(peak.values())),bars=bars)

def interval(coeffs,lo,hi):
    for a,b in coeffs:
        if not b:
            if a<0:return None
        elif b>0:lo=max(lo,-a/b)
        else:hi=min(hi,-a/b)
    return (lo,hi) if lo<=hi else None

def centre_line(v,planes,faces,E,uroot,sroot):
    # Reference point is s*(0,1,0) relative to the actual centroid.
    axis=(max(H/N[1] for N,H in planes if N[1]<0),min(H/N[1] for N,H in planes if N[1]>0));assert axis[0]<0<axis[1]
    records=[];adj=[[] for p in v];eu=(R(0),R(1),R(0))
    for a,b in E:adj[a].append(b);adj[b].append(a)
    for i,nb in enumerate(adj):
        coeff=[(-dot(v[i],sub(v[j],v[i])),v[j][1]-v[i][1]) for j in nb]
        z=interval(coeff,*axis)
        if z is not None:records.append(dict(kind='U',id=i,lo=z[0],hi=z[1],root=i==uroot,coefficients=coeff))
    for i,((N,H),f) in enumerate(zip(planes,faces)):
        foot=mul(N,H/dot(N,N));velocity=sub(eu,mul(N,N[1]/dot(N,N)))
        coeff=[(dot(N,cross(sub(v[b],v[a]),sub(foot,v[a]))),dot(N,cross(sub(v[b],v[a]),velocity))) for a,b in zip(f,f[1:]+f[:1])]
        z=interval(coeff,*axis)
        if z is not None:records.append(dict(kind='S',id=i,lo=z[0],hi=z[1],root=i==sroot,coefficients=coeff))
    # Certificates below use STRICT inequalities, not merely closed weak intervals.
    # Each selected interval's coefficient functions are strictly positive on its
    # interior; endpoint overlaps are strictly nonempty. The two ends of axis are
    # boundary points, not admissible centres.
    viable=[z for z in records if not z['root'] and z['lo']<z['hi'] and all(a+b*(z['lo']+z['hi'])/2>0 for a,b in z['coefficients'])]
    cursor=axis[0];cover=[]
    while cursor<axis[1]:
        eligible=[z for z in viable if (z['lo']<cursor or cursor==axis[0] and z['lo']==cursor) and z['hi']>cursor]
        if not eligible:break
        z=max(eligible,key=lambda z:(z['hi'],-z['id']));cover.append(dict(kind=z['kind'],id=z['id'],lo=z['lo'],hi=z['hi']));cursor=z['hi']
    intended=[z for z in records if z['root']]
    assert len(intended)==2
    # Both intended roots must remain strict throughout the open body-axis segment.
    for z in intended:
        assert (z['lo'],z['hi'])==axis
        assert all(a+b*axis[0]>=0 and a+b*axis[1]>=0 and a+b*(axis[0]+axis[1])/2>0 for a,b in z['coefficients'])
    return dict(axis=axis,records=records,strict_extra_cover=cover,axis_excluded=cursor>=axis[1],intended_strict_throughout=True)

def run(inp):
    raw,rawplanes,ax,rings,metric=generate(inp);faces,E,EF=complex_from_planes(raw,rawplanes)
    Vs,Ms=slab_mass(ax,rings,metric);assert Vs>0;cen=mul(Ms,1/Vs);assert cen[0]==cen[2]==0
    Vt,Mt=tetra_mass(raw,faces,cen);assert (Vt,Mt)==(Vs,Ms)
    v=[sub(p,cen) for p in raw];planes=[(N,H-dot(N,cen)) for N,H in rawplanes];assert all(H>0 for N,H in planes)
    v2,m2=tetra_mass(v,faces,mul(v[0],R(1,17)));assert v2==Vs and m2==(0,0,0)
    eq,q=equilibrium(v,planes,faces,E,EF);P=landscape(v,E);Q=landscape(q,[tuple(z) for z in EF]);assert P['roots']==eq['U'] and Q['roots']==eq['S']
    k,n=inp['k'],inp['n'];uroot=1+k*n
    ss=[i for i,(N,H) in enumerate(planes) if N[0]==N[2]==0 and N[1]<0];assert len(ss)==1;sroot=ss[0]
    assert uroot in eq['U'] and sroot in eq['S']
    line=centre_line(v,planes,faces,E,uroot,sroot)
    out=dict(identity=inp['identity'],V=len(v),E=len(E),F=len(faces),C=2*len(E),strict=[len(eq[z]) for z in ('S','U','H')],weak=[len(eq[z]) for z in ('weakS','weakU','weakH')],volume=Vs,raw_centroid=cen,vertices=v,planes=planes,faces=faces,edges=E,edge_faces=EF,equilibria=eq,P=P,Q=Q,centre_line=line,mass_checks='exact cubic section integration and two tetra origins')
    return out

if __name__=='__main__':
    inp=json.loads(Path(sys.argv[1]).read_text());out=run(inp);path=Path(inp['identity']+'_AUDIT.json')
    data=(json.dumps(pack(out),sort_keys=True,separators=(',',':'))+'\n').encode();path.write_bytes(data)
    print('IGS_EXACT_CENSUS',out['identity'],out['V'],out['E'],out['F'],out['strict'],out['weak'])
    print('IGS_EXACT_PQ',[(len(b['component']),len(b['boundary']),float(b['relative'])) for b in out['P']['bars']],[(len(b['component']),len(b['boundary']),float(b['relative'])) for b in out['Q']['bars']])
    print('IGS_EXACT_LINE_COVER',out['centre_line']['axis_excluded'],[(z['kind'],z['id'],float(z['lo']),float(z['hi'])) for z in out['centre_line']['strict_extra_cover']])
    print('IGS_EXACT_OUTPUT',str(path),len(data),hashlib.sha256(data).hexdigest())
    print('IGS_EXACT_MASS_MECHANICS_AND_LINE_PASS')
