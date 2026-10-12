# material-fdb1e5022481

AI research material · [Export notes](../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

# J123 exact V bodies and finite flip-wall mass kernel — complete standalone recovery

These are useful NONWINNERS, not own110 or a new canonical record. The original exact seed is the literal KF27G_QDESC_G4 body in immutable result figure-0599, SHA a585962132f976fee04dc73b2eaa97cbfb33bb898819dcff1850bb879954b753, read completely. The three new G8 inputs below are finite actual-mass descendants from coordinator J123 numerical experiments, rounded coordinatewise by numpy.rint(X*10^8), ties to even. They are preserved as exact bodies independently of floating optimizer reproducibility. The fourth new body is an exact orthogonal projection derived from the first G8 input.

## Exact results and evidence scope
One newly implemented exhaustive rational V auditor was executed on every listed new body. It enumerates ALL supporting triples, derives true vertices/maximal facets/true edges, checks a closed convex complex, computes exact uniform volume and centroid by two internal tetrahedral formulas, classifies all strict/weak/primitive predicates and all positive radial bars without a numerical floor, and cross-checks local versus global equilibrium signs. These are internal checks of ONE program, not independent implementations.

- J123_SAFECAPA_G8: V38/E108/F72,C216,own211,weak000,primitive000,P[],Q~.7642883867237126.
- J123_BUFFEREDD_G8:38/108/72,C216,own312,weak000,primitive000,P[],Q~.6433948558611409,.10066361913744264.
- J123_FULLF_G8:38/108/72,C216,own(10,1,9),weak000,primitive000,P[],nine Q with largest~.44232925312946464. It is NOT own211 merely because its primary Q is smaller.
- J123_FLIPWALL_EXACT:38/107/71,C214,own211,weak000,primitive000,P[],Q~.7642884032212514. It has exactly one quadrilateral with oriented submitted-vertex cycle[0,32,8,9], not two triangular maximal facets. All other coordinates of SAFECAPA are unchanged. This exact coplanarity is not an additional weak equilibrium. Its larger common denominator is not an arithmetic simplification claim.

## Finite mass identity and derivative jump
For an oriented four-point cycle(a,b,c,d), replace triangles A={(a,b,c),(a,c,d)} by B={(a,b,d),(b,c,d)}, leaving all other oriented boundary triangles fixed. For the corresponding signed boundary mass polynomials,
Delta V=V_B-V_A=det(b-a,c-a,d-a)/6,
Delta M=M_B-M_A=((a+b+c+d)/4)*Delta V.
These are exact polynomial identities at finite coordinates. On a flat wall Delta V=0, with common positive volume V and centroid g, the centroid Jacobian jump is
Dg_B-Dg_A=((c_T-g)/V) outer D(Delta V), c_T=(a+b+c+d)/4.
It has rank at most one; the code below verifies exact rank ONE at this particular rational wall in all114 input-coordinate directions, and verifies24 finite rational perturbations.
For a physical angular chord A_ij=p_i.dot(d_ij)/(|p_i||d_ij|), p_i=x_i-g, d_ij=x_j-x_i, the mass-induced derivative jump similarly factors through this rank-one centroid jump; grad_g A_ij=-d_ij/(|p_i||d_ij|)+A_ij*p_i/|p_i|^2. No such rank-one claim is made for every polar-facet derivative across arbitrary topology changes.
If these are the only two local convex boundary charts and no other incidence changes, the convex choice uses V_A+max(Delta V,0), M_A+c_T*max(Delta V,0). The program certifies the finite polynomial kernel and wall derivative, NOT global validity of that two-chart membership hypothesis or an exclusion of other geometries. A sign-conditioned correction is a proposed constructive use, not yet an executed own110 method here.

## Reconstruction and verification
Use Python3.13.5 standard library; no third-party dependency is needed for this exact package. Save each fenced source/input block under its heading, preserving its terminal newline. From the same directory run:
```sh
python exactv123.py KF27G_QDESC_G4.txt > exact_seed.json
python exactv123.py J123_SAFECAPA_G8.txt > J123_SAFECAPA_G8_AUDIT.json
python exactv123.py J123_BUFFEREDD_G8.txt > J123_BUFFEREDD_G8_AUDIT.json
python exactv123.py J123_FULLF_G8.txt > J123_FULLF_G8_AUDIT.json
python flatten123.py J123_SAFECAPA_G8.txt J123_FLIPWALL_EXACT.txt 0 8 9 32
python exactv123.py J123_FLIPWALL_EXACT.txt > J123_FLIPWALL_EXACT_AUDIT.json
python flipkernel123.py J123_FLIPWALL_EXACT.txt J123_FLIPWALL_EXACT_AUDIT.json J123_FLIP_KERNEL.json
```
Each audit writes J123_EXACT_V_PASS plus its true V/E/F,strict/weak/primitive counts to stderr. The last command prints J123_FINITE_TETRA_MASS_AND_RANK_ONE_CENTROID_JUMP_PASS quad [0,32,8,9] rank 1. Run the commands with these RELATIVE input filenames: the kernel JSON records its input name.

Source/input identities (bytes,SHA256):
exactv123.py 7742 25e3b9c7536a39b4c10d5ba83ea859381a6a2596189df97bff6b61ee61257c1d
flatten123.py 1359 de56742c5e8755e9a3549e213ce868e0f520642a6a72616592389ebc46424414
flipkernel123.py 3156 bd9c7bd5bbd929a774bcbbd731268fe3d92c44daa34c9d0e76c40d1d8da0679c
KF27G_QDESC_G4.txt 608 5a0a14dfd8804ba2a6422ae31bd5f9611c5f994a21ee00584f30fffd500db754
J123_SAFECAPA_G8.txt 1068 2552e3bf57c053cded7bdfa41d2c8166ad6a1aeffc37d072f49d10c2d72df8f9
J123_BUFFEREDD_G8.txt 1070 250078e0661c1a4d11697b4cd94f16be095c65b45b7fd7f4c6e30e58dc1d41ba
J123_FULLF_G8.txt 1059 e28c35d7cc22dabe8965b8db8a8b6da41b35319d82bd53d419b8c55371f1aaa0

Expected reproduced outputs (bytes,SHA256):
J123_SAFECAPA_G8_AUDIT.json 11650 4d3f44b2204ba3b7c1f8c7ca81e1f45fd1aa4221656f90497a7eb5d5359c3c8e
J123_BUFFEREDD_G8_AUDIT.json 12414 be9377ad69add6e5ef155c0e555d89a1316f424604363615628f9c1b744bf5cd
J123_FULLF_G8_AUDIT.json 16921 948eccfaa5be5c9dec0e8a1ac84b13406ad792916824fd4c0bf3c2da2a1925f7
J123_FLIPWALL_EXACT.txt 4556 9d71a6564344421846acdc73b1c4bd28e28ffa4598f3769db73a8fea8dc1f543
J123_FLIPWALL_EXACT_AUDIT.json 13392 5f8a588690547e5e278ad9334c666f874474b68ce2326df4d768378894f73b5e
J123_FLIP_KERNEL.json 15380 8b4c1c2ce432520edfd96f8f2d7e9ba22d6cf832d21685e2dff2e680387cee5a
The exact wall common denominator is212636057149186232650537913141000000000. No originating sandbox or older optimizer archive is required for these reconstructions.

## exactv123.py
```python
"""Exhaustive rational V-polyhedron mass/equilibrium/persistence audit.
Pure Python 3 standard library. Input: N D followed by N integer triples, D>0.
Enumerates every supporting triple; no floating hull decides geometry/signs.
Floating atan2 only proposes a face order that is subsequently proved convex.
Two tetrahedral mass formulas and direct/global equilibrium checks are internal
cross-checks of this ONE auditor, not claims of independent implementations.
"""
from __future__ import annotations
from fractions import Fraction as Q
from itertools import combinations
from functools import reduce
from math import gcd,atan2
import json,sys

def dot(a,b):return sum(x*y for x,y in zip(a,b))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def add(a,b):return tuple(x+y for x,y in zip(a,b))
def mul(a,s):return tuple(x*s for x in a)
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def det(a,b,c):return dot(a,cross(b,c))
def fq(x):return str(x)
def vector(x):return [str(t) for t in x]

def persistence(points,edges):
    r=[dot(x,x) for x in points];events=[]
    for u,v in edges:
        d=sub(points[v],points[u]);dd=dot(d,d);assert dd>0
        t=max(Q(0),min(Q(1),-dot(points[u],d)/dd));z=add(points[u],mul(d,t))
        level=dot(z,z);assert level<=r[u] and level<=r[v]
        events.append((level,u,v))
    events.sort(key=lambda e:(-e[0],e[1],e[2]));par=list(range(len(points)));comp=[{i} for i in range(len(points))];out=[]
    def find(i):
        while par[i]!=i:par[i]=par[par[i]];i=par[i]
        return i
    for level,u,v in events:
        a,b=find(u),find(v)
        if a==b:continue
        if r[a]<r[b] or (r[a]==r[b] and a>b):a,b=b,a
        assert r[b]>=level
        if r[b]>level:out.append({'root':b,'edge':[u,v],'birth':r[b],'death':level,'depth':1-level/r[b],'component':sorted(comp[b])})
        par[b]=a;comp[a]|=comp[b]
    assert len({find(i) for i in range(len(points))})==1
    return sorted(out,key=lambda z:(-z['depth'],z['root'],z['edge']))

def audit(path):
    tokens=open(path).read().split();N,D=map(int,tokens[:2]);assert N>=4 and D>0 and len(tokens)==2+3*N
    raw=[tuple(map(int,tokens[2+3*i:5+3*i])) for i in range(N)];assert len(set(raw))==N
    planes={}
    for i,j,k in combinations(range(N),3):
        n=cross(sub(raw[j],raw[i]),sub(raw[k],raw[i]));h=dot(n,raw[i])
        if n==(0,0,0):continue
        sides=[dot(n,p)-h for p in raw]
        if max(sides)>0 and min(sides)<0:continue
        if max(sides)==0 and min(sides)==0:raise AssertionError('Not three-dimensional')
        if min(sides)>=0:n=mul(n,-1);h=-h;sides=[-s for s in sides]
        div=reduce(gcd,(*n,h));n=tuple(z//div for z in n);h//=div
        planes[(*n,h)]=tuple(t for t,s in enumerate(sides) if s==0)
    keys=sorted(planes);assert len(keys)>=4
    used=[]
    for i in range(N):
        normals=[k[:3] for k in keys if i in planes[k]]
        if any(det(a,b,c)!=0 for a,b,c in combinations(normals,3)):used.append(i)
    assert len(used)>=4
    index={r:i for i,r in enumerate(used)};x=[tuple(Q(t,D) for t in raw[i]) for i in used]
    fs=[];normals=[];heights=[]
    for key in keys:
        members=[index[i] for i in planes[key] if i in index];assert len(members)>=3
        n=key[:3];h=Q(key[3],D);assert all(dot(n,p)<=h for p in x)
        centre=mul(tuple(sum(x[i][t] for i in members) for t in range(3)),Q(1,len(members)))
        axis=max(range(3),key=lambda t:abs(n[t]));uv=[t for t in range(3) if t!=axis]
        members.sort(key=lambda i:atan2(float(x[i][uv[1]]-centre[uv[1]]),float(x[i][uv[0]]-centre[uv[0]])))
        if dot(n,cross(sub(x[members[1]],x[members[0]]),sub(x[members[2]],x[members[0]])))<0:members.reverse()
        at=members.index(min(members));members=members[at:]+members[:at]
        for a,b in zip(members,members[1:]+members[:1]):
            for t in members:
                if t not in (a,b):assert dot(n,cross(sub(x[b],x[a]),sub(x[t],x[a])))>0
        fs.append(members);normals.append(n);heights.append(h)
    edge_faces={}
    for f,cy in enumerate(fs):
        for a,b in zip(cy,cy[1:]+cy[:1]):edge_faces.setdefault(tuple(sorted((a,b))),[]).append(f)
    edges=sorted(edge_faces);assert all(len(edge_faces[e])==2 for e in edges)
    V,F,E=len(x),len(fs),len(edges);assert V-E+F==2
    for f,g in combinations(range(F),2):
        it=set(fs[f])&set(fs[g]);assert len(it)<=2
        if len(it)==2:assert tuple(sorted(it)) in edge_faces
    W=Q(0);M=(Q(0),)*3;anchor=mul(tuple(sum(p[t] for p in x) for t in range(3)),Q(1,V))
    volume2=Q(0);moment2=(Q(0),)*3
    for cy in fs:
        for j in range(1,len(cy)-1):
            a,b,c=x[cy[0]],x[cy[j]],x[cy[j+1]];w=det(a,b,c)
            W+=w;M=add(M,mul(add(add(a,b),c),w))
            v2=det(sub(a,anchor),sub(b,anchor),sub(c,anchor))/6;assert v2>0
            volume2+=v2;moment2=add(moment2,mul(add(add(a,b),add(c,anchor)),v2/4))
    assert W>0;volume=W/6;g=mul(M,1/(4*W));assert volume2==volume and mul(moment2,1/volume2)==g
    p=[sub(a,g) for a in x];q=[]
    for n,h in zip(normals,heights):
        hh=h-dot(n,g);assert hh>0;q.append(mul(n,1/hh))
    adjacent=[[] for _ in x]
    for u,v in edges:adjacent[u].append(v);adjacent[v].append(u)
    stable=[];unstable=[];saddle=[];ws=[];wu=[];wh=[];zero=[0,0,0]
    for i in range(V):
        signs=[dot(p[i],sub(p[j],p[i])) for j in adjacent[i]];zero[1]+=signs.count(0)
        if max(signs)<0:unstable.append(i)
        elif max(signs)==0:wu.append(i)
    for f,(n,h,cy) in enumerate(zip(normals,heights,fs)):
        foot=add(g,mul(n,(h-dot(n,g))/dot(n,n)))
        signs=[dot(n,cross(sub(x[b],x[a]),sub(foot,x[a]))) for a,b in zip(cy,cy[1:]+cy[:1])];zero[0]+=signs.count(0)
        if min(signs)>0:stable.append(f)
        elif min(signs)==0:ws.append(f)
    dual=[]
    for u,v in edges:
        f1,f2=edge_faces[u,v];dual.append((f1,f2));d=sub(p[v],p[u]);dd=dot(d,d);t=-dot(p[u],d);rr=add(mul(p[u],dd),mul(d,t))
        n1,n2=normals[f1],normals[f2];aa,bb,ab=dot(n1,n1),dot(n2,n2),dot(n1,n2);assert aa*bb-ab*ab>0
        guards=[t,dd-t,dot(rr,n1)*bb-dot(rr,n2)*ab,dot(rr,n2)*aa-dot(rr,n1)*ab];zero[2]+=guards.count(0)
        if min(guards)>0:saddle.append([u,v])
        elif min(guards)==0:wh.append([u,v])
    P,B=persistence(p,edges),persistence(q,dual)
    if not(ws or wu or wh):
        assert len(stable)+len(unstable)==len(saddle)+2
        assert len(P)+1==len(unstable) and len(B)+1==len(stable)
    def global_roots(points):
        strict=[];weak=[]
        for i,a in enumerate(points):
            vals=[dot(a,sub(b,a)) for j,b in enumerate(points) if j!=i]
            if max(vals)<0:strict.append(i)
            elif max(vals)==0:weak.append(i)
        return strict,weak
    assert global_roots(p)==(unstable,wu) and global_roots(q)==(stable,ws)
    def format_bars(bars):
        return [{k:vector(v) if False else str(v) if isinstance(v,Q) else v for k,v in bar.items()} for bar in bars]
    result={'input_rows':N,'input_denominator':D,'V':V,'E':E,'F':F,'C':2*E,'strict':[len(stable),len(unstable),len(saddle)],'weak':[len(ws),len(wu),len(wh)],'primitive_zeros':zero,'volume':str(volume),'centroid':vector(g),'input_vertex_indices':used,'vertices':[vector(v) for v in x],'planes':[[*map(str,n),str(h)] for n,h in zip(normals,heights)],'faces':fs,'edges':edges,'S':stable,'U':unstable,'H':saddle,'P':format_bars(P),'Q':format_bars(B),'checks':'EXHAUSTIVE_SUPPORT_TRIPLES_TRUE_COMPLEX_TWO_MASSES_DIRECT_GLOBAL_ALL_BARS_PASS'}
    print('J123_EXACT_V_PASS',V,E,F,'SUH',result['strict'],'weak',result['weak'],'zeros',zero,'P',len(P),'Q',len(B),file=sys.stderr,flush=True)
    return result
if __name__=='__main__':
    result=audit(sys.argv[1]);print(json.dumps(result,sort_keys=True,separators=(',',':')))
```

## flatten123.py
```python
"""Exact finite co-planarization at an observed four-vertex flip wall.
Preserves all other literal rational points, projects the fourth orthogonally
onto the plane of the first three, and emits one common-denominator V input.
No equilibrium preservation is assumed: run exactv123.py on the result.
"""
from fractions import Fraction as F
from math import lcm
from functools import reduce
import sys,json
from exactv123 import dot,sub,cross,mul

def flatten(inp,out,indices):
 t=open(inp).read().split();n,d=map(int,t[:2]);x=[tuple(F(int(z),d) for z in t[2+3*i:5+3*i]) for i in range(n)]
 a,b,c,k=indices;normal=cross(sub(x[b],x[a]),sub(x[c],x[a]));nn=dot(normal,normal);assert nn>0
 delta=dot(normal,sub(x[k],x[a]))/nn;y=x.copy();y[k]=sub(x[k],mul(normal,delta));assert dot(normal,sub(y[k],x[a]))==0
 D=reduce(lcm,(v.denominator for p in y for v in p),1)
 data=f'{n} {D}\n'+'\n'.join(' '.join(str(int(v*D)) for v in p) for p in y)+'\n';open(out,'w').write(data)
 record={'input':inp,'indices':indices,'projected_vertex':k,'displacement':[str(a-b) for a,b in zip(y[k],x[k])],'plane_normal':list(map(str,normal)),'projection_coefficient':str(delta),'common_denominator':str(D)}
 open(out+'.flatten.json','w').write(json.dumps(record,indent=2)+'\n');print(json.dumps(record))
if __name__=='__main__':flatten(sys.argv[1],sys.argv[2],list(map(int,sys.argv[3:7])))
```

## flipkernel123.py
```python
"""Exact two-chart mass kernel at J123_FLIPWALL_EXACT.
Verifies a signed tetrahedral difference at finite rational perturbations and
the rank-one centroid-Jacobian jump at the wall. No claim of whole-class110.
"""
from fractions import Fraction as F
from itertools import product
import json,sys
from exactv123 import dot,cross,sub,add,mul,det

def masses(x,triangles):
 v=F(0);m=(F(0),)*3
 for i,j,k in triangles:
  a,b,c=x[i],x[j],x[k];w=det(a,b,c)/6
  v+=w;m=add(m,mul(add(add(a,b),c),w/4))
 return v,m

def generator(inp,auditfile,out):
 t=open(inp).read().split();n,d=map(int,t[:2]);x=[tuple(F(int(z),d) for z in t[2+3*i:5+3*i]) for i in range(n)];audit=json.load(open(auditfile));assert audit['input_vertex_indices']==list(range(n))
 quads=[cy for cy in audit['faces'] if len(cy)==4];assert len(quads)==1;cy=quads[0];a,b,c,e=cy
 common=[]
 for face in audit['faces']:
  if face==cy:continue
  common.extend((face[0],face[i],face[i+1]) for i in range(1,len(face)-1))
 A=common+[(a,b,c),(a,c,e)];B=common+[(a,b,e),(b,c,e)]
 v,m=masses(x,A);vb,mb=masses(x,B);assert v==vb and m==mb
 g=mul(m,1/v);ct=mul(add(add(x[a],x[b]),add(x[c],x[e])),F(1,4))
 delta_grad=[];jac_jump=[];finite=[]
 for k,axis in product(range(n),range(3)):
  y=x.copy();q=list(y[k]);q[axis]+=1;y[k]=tuple(q)
  da=det(sub(y[b],y[a]),sub(y[c],y[a]),sub(y[e],y[a]))/6
  # The volume gradient jump is exact since only one coordinate varies.
  va1,ma1=masses(y,A);vb1,mb1=masses(y,B)
  assert vb1-va1==da
  # Moment is quadratic in this one coordinate; symmetric differences are its exact derivative at 0.
  z=x.copy();q=list(z[k]);q[axis]-=1;z[k]=tuple(q)
  va_1,ma_1=masses(z,A);vb_1,mb_1=masses(z,B)
  dma=mul(sub(ma1,ma_1),F(1,2));dmb=mul(sub(mb1,mb_1),F(1,2))
  dga=mul(sub(dma,mul(g,va1-v)),1/v);dgb=mul(sub(dmb,mul(g,vb1-v)),1/v)
  predicted=mul(sub(ct,g),da/v);actual=sub(dgb,dga);assert actual==predicted
  delta_grad.append(da);jac_jump.append(actual)
 for k in cy:
  for axis in range(3):
   for h in [F(1,1000000),F(-1,1000000)]:
    y=x.copy();p=list(y[k]);p[axis]+=h;y[k]=tuple(p)
    va,ma=masses(y,A);vb,mb=masses(y,B);delta=det(sub(y[b],y[a]),sub(y[c],y[a]),sub(y[e],y[a]))/6
    cc=mul(add(add(y[a],y[b]),add(y[c],y[e])),F(1,4))
    assert vb-va==delta and sub(mb,ma)==mul(cc,delta)
    finite.append({'vertex':k,'axis':axis,'step':str(h),'delta_volume':str(delta)})
 nonzero=[i for i,q in enumerate(jac_jump) if q!=(0,0,0)];assert nonzero
 # All 2x2 minors of the 3x3N jump vanish; at least one entry is nonzero.
 for i in range(3):
  for j in range(i+1,3):
   for k in range(len(jac_jump)):
    for l in nonzero:
     assert jac_jump[k][i]*jac_jump[l][j]==jac_jump[k][j]*jac_jump[l][i]
 result={'input':inp,'quad':cy,'volume':str(v),'centroid':list(map(str,g)),'tetra_centroid':list(map(str,ct)),'delta_gradient':list(map(str,delta_grad)),'jacobian_jump':[[str(t) for t in q] for q in jac_jump],'rank':1,'finite_checks':finite,'marker':'J123_FINITE_TETRA_MASS_AND_RANK_ONE_CENTROID_JUMP_PASS'}
 open(out,'w').write(json.dumps(result,sort_keys=True,separators=(',',':'))+'\n');print(result['marker'],'quad',cy,'rank',1)
if __name__=='__main__':generator(*sys.argv[1:4])
```

## KF27G_QDESC_G4.txt
```text
38 10000
-8421 -4792 3346
-6088 -3489 6255
-6874 -3723 -950
-3372 -2059 7759
-4753 -568 -2676
559 4416 -3716
-723 4236 -3806
3490 2646 -4259
1588 -465 7570
-577 -1192 8013
5763 1304 -2265
3322 74 6673
-619 1134 -5527
-1433 -371 -5075
4069 1845 -4223
1541 4763 -2529
3624 -527 -4451
5576 2829 353
3719 2283 -4296
4687 1419 -3803
2779 3467 -4125
4268 3590 -1558
6413 1230 -23
2268 3644 -4254
5243 1497 -3074
935 2995 -5033
3203 3083 -4158
5524 1004 4196
194 2136 -5408
564 4148 -4125
4620 561 5511
1642 -2119 -4447
2459 -1911 -3850
1626 3569 -4553
6127 1187 2768
6413 1242 1344
6165 1249 -1252
5288 -591 -2768
```

## J123_SAFECAPA_G8.txt
```text
38 100000000
-84210000 -47920000 33460000
-60885106 -34889346 62557565
-68996294 -37132316 -9592348
-33846795 -20108330 77783548
-47847556 -5348900 -26744561
5324086 44958089 -37051450
-6629042 41221424 -38020264
34900601 26468603 -42593190
15905549 -4731119 75609753
-5832112 -12025329 79992636
57654298 13060255 -22653322
33278203 484376 66682960
-6204099 11344683 -55322680
-14355105 -3741645 -50820052
40706481 18445876 -42218330
15109836 47480641 -25091196
36255679 -5275556 -44563019
55785964 28220048 3461861
37199445 22825454 -42960012
46877984 14212007 -38024523
27790907 34667046 -41266224
42662148 35870312 -15551412
64172372 12311603 -233499
22675090 36432665 -42558205
52448032 14960512 -30748162
9350316 29947788 -50329362
32028106 30832907 -41588540
55088330 10616246 42150125
1949466 21359652 -54099437
5702261 41515607 -41280012
46295132 5353644 55102005
16429609 -21258668 -44530193
24590124 -19111296 -38503255
16241121 35733778 -45513035
61305944 11883519 27689885
64174704 12427213 13442244
61688998 12502350 -12524655
52907336 -5933477 -27694455
```

## J123_BUFFEREDD_G8.txt
```text
38 100000000
-84210000 -47920000 33460000
-44671632 -29541709 64357454
-85730768 -47923373 -2227647
-23051647 -17691391 72407646
-45918025 4771222 -18050803
-3316927 49208783 -30591105
-11124020 43503234 -27946525
40496226 18850406 -48102306
10520603 -1845316 70989215
-4122876 -8931694 73516888
62436048 11555802 -13253536
23674234 3998717 65635883
-10343038 28832127 -53738568
-5094645 10639791 -62882338
50853214 10434637 -39776302
-886237 50059309 -28426109
37309876 -14155411 -48796017
58405936 21404522 -168723
45528006 13921120 -45126171
55820712 6712584 -33040457
30252145 29685675 -49801532
50716028 28524338 -22055370
62697071 13299860 10414139
24287148 29919537 -53137879
59773133 9257786 -23800747
12437146 23392701 -60350552
35613459 24527960 -49227816
45141744 13063780 47785804
10595080 11118961 -63252479
6316093 40292557 -48372356
33992756 10104341 58644172
15893739 -26979085 -50417620
28921251 -20002931 -42591518
17962114 29371292 -56143709
53883178 13320590 35579077
59574492 13790340 22774600
63569293 12547960 -1736280
51489739 -6872304 -37726973
```

## J123_FULLF_G8.txt
```text
38 100000000
-84210000 -47920000 33460000
-46546809 -28354867 64140052
-79655317 -49457102 2470613
-24319785 -17616580 72237222
-49459952 6503125 -24088034
-3772466 50119664 -37022552
-18369915 50916263 -20634748
45335966 16403780 -45357222
10800242 -4563705 70451862
-6737145 -10882472 73631777
63289387 9644629 -6589480
25297772 258166 64212639
-15467432 22809986 -58846785
-1594523 4151972 -64762120
55137053 11038522 -33125493
5471732 51150069 -34856762
35070665 -13986274 -48658849
57056212 18685065 -1143292
50606929 13922461 -39555515
58809518 8104288 -26042292
32867933 23620968 -53405757
49845394 30440105 -20223867
61905678 9135888 15212129
25552287 26280312 -56551067
61603653 9652531 -16762179
7549422 24101884 -62764296
39334110 19417482 -50172481
46442441 6141334 46542135
10925299 9656408 -63797903
11032495 41100006 -50276221
36954502 3760230 56135895
13688723 -23355132 -52203522
26268810 -20022038 -48652763
17508663 28996446 -58610089
53488614 7575606 36541628
58622132 8618543 25947777
63447479 9510448 4214705
50148534 -7260734 -36968734
```
