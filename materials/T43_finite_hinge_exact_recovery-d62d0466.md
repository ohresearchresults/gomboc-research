# material-d62d046640d6

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

Public derivative: internal-record-identifiers-replaced.

---

# Recovery capsule — exact whole-body finite hinges of T43

## Objects and evidence
These are useful NONRECORD constructions, not own110. The source below was executed by the coordinator under CPython3.13.5, standard library only, with no floating acceptance tolerance. It contains the full literal T43 all-G3 input from accepted RA43 figure-0554 (SHA75f535724577c7ccca10bff31683fac02ec7a7fc1793b92ba46afb01c671b1b0). Neither that older sandbox nor FULL76 is needed to recover these objects.

T43_SINGLE_HINGE_RAY_C338: true V66/E169/F105, C338, own strict222, additional weak000, primitive zero000, one positive P and one Q, relative depths .4979309460851643 and .6441529768914941.
T43_SINGLE_HINGE_INTERIOR_C340: true V66/E170/F106, C340, own strict222, additional weak000, primitive zero000, one positive P and one Q, depths .4969548098454317 and .6440582839144547.
Both improve both depths from the exact T43 all-G3 baseline (.5341742685943558,.655896727661406), but increase complexity from C246. They are not stronger than all other entrances on every criterion.

Both have canonical U40/46, stable facets23=[7,40,46] and46=[22,46,35], H edges0–4 and46–64. The stable carriers still contain elderU46; there is no stable-root detachment claim. P component15/cut34, root40->46, attaining edge0–4; Q component48/cut27, root46->23, attaining dual edge70–93. Full exact births/deaths/components/true cuts/attaining true-edge paths, maximal facets, coordinates and physical support planes are regenerated without a positive-bar floor. Coordinate denominator maxima are84/115 bits and centroid denominator maxima739/770 bits for ray/interior. Volume is unchanged; the centroid generally moves.

## Finite global convexity theorem
Let a full-dimensional bounded polytope K have maximal supporting planes m_f·x<=b_f. Let z(x)=n·x-h take both signs on K, and choose v with n·v=0. Define F_v(x)=x+v max(0,z(x)). It is a global piecewise-affine homeomorphism, with inverse y-v max(0,n·y-h), and determinant1 on both halves.

For each facet, if min_f z<0, impose z(p)m_f·v<=b_f-m_f·p for EVERY original vertex p with z(p)>0. If max_f z>0, impose -z(p)m_f·v<=b_f-m_f·p for EVERY original vertex p with z(p)<0. These are necessary and sufficient for F_v(K) to be convex. Thus the complete velocity set in n-perpendicular space is a rational convex polygon (possibly lower-dimensional).

Proof: lower facet pieces retain (m_f,b_f); upper pieces have plane (m_f-(m_f·v)n,b_f-(m_f·v)h). The displayed inequalities say that every nonempty boundary piece supports the entire transformed pair of halves; checking original vertices suffices because section vertices have z=0. Necessity follows from convexity. For sufficiency take a point of each transformed half and their segment. Its intersection w with z=0 satisfies every original facet inequality: for each facet at least one nonempty lower/upper piece gives a globally supporting plane, and both transformed plane forms reduce to m_f·w<=b_f on z=0. Hence w belongs to the unchanged section K intersect{z=0}. Convexity of each affine half then puts the entire segment in their union. The polygon is bounded: every facet normal has a finite upper bound m_f·v<=B_f, and the original bounded K has positively spanning normals, so the recession cone is zero.

No convexification mass is silently added. With Kplus=K intersect{z>=0}, Vplus and Mplus its actual filled volume/moment, the exact whole-body law is V(F_vK)=V(K) and M(F_vK)=M(K)+v(n·Mplus-h Vplus). The code integrates the transformed maximal-facet hull and the clipped upper half independently and verifies both identities exactly. Convexity does not imply any equilibrium count.

The specific rational cut is n=(-325273,-698874,-240310),h=-45275161 in the INTEGER T43 coordinate frame; physical coordinates are divided by1000 AFTER applying F. It passes through old input15,29,42 and crosses23 old true edges. Let v0=(6558183650,-10897765265,22816215436)*896003/43031309628659688161280 and v1=(9143958392,-13454834289,26752740547)*896003/57272582292669275259520. RAY uses v=v1/2. INTERIOR uses v=v0/60+59v1/120. These parameters are literal below. The source verifies the exact facet inequalities for each endpoint; it does not claim an interval mechanical certificate or a complete angular family exclusion.

## Recovery, verification and pinned receipts
Save the sole Python block EXACTLY as finite_hinge_exact.py, UTF-8 with its terminal newline. It is12917 bytes, SHA256 5efb192313d80dbfa4dcea4f14187464bae76c07c5f058dfb853ee8e9e0e4154.
Run:
    python -B -S finite_hinge_exact.py ray
    python -B -S finite_hinge_exact.py interior
Both commands reconstruct and verify their complete object. Expected markers are HINGE_EXACT_BODY_PASS ray [66, 169, 105] [2, 2, 2] [0, 0, 0] 1 1 and HINGE_EXACT_BODY_PASS interior [66, 170, 106] [2, 2, 2] [0, 0, 0] 1 1.
Regenerated physical-coordinate ledgers:
- hinge_ray_exact.json,33778 bytes,SHA256 43dd2a187ca06d57dde282cf0aebf4b1f8e745bcf8739e6a9f8dc72624e21c8a.
- hinge_interior_exact.json,38170 bytes,SHA256 f2ff293ba7743c4a607db754891761abe90123636b2f8e7bd4a2571eaa0e2198.
These are the executed final ledgers; earlier local ledgers with raw-coordinate barcode levels were superseded. Complete code and exact inputs here, not output hashes alone, are the durable construction. Numerical search sources are separate and not needed for reconstruction. This is exact rational computation and an analytic theorem, not proof-assistant verification or an independently commissioned audit.

```python
"""Exact whole-body hinge recovery and complete rational equilibrium/bar audits.
The literal rational T43 input and every necessary helper are included below.
All code here uses the Python standard library. No floating tolerance accepts a claim.
"""
from fractions import Fraction as F
from itertools import combinations
from collections import defaultdict
from pathlib import Path
import json, math, hashlib, sys
P0=[[-1131,-380,23],[-1127,-283,-218],[-1086,-225,-391],[-1013,-181,-547],[-945,-683,646],[-931,-156,-666],[-871,-801,885],[-869,-137,-738],[-780,-129,-818],[-668,-131,-892],[-635,202,-115],[-589,230,-7],[-559,224,54],[-528,217,107],[-496,331,-186],[-445,199,212],[-382,425,-214],[-366,407,-88],[-316,410,9],[-307,448,-285],[-230,462,-332],[-215,439,46],[-128,476,-366],[-30,481,-367],[-2,-201,-1240],[126,415,143],[140,485,-321],[295,502,-44],[325,457,97],[385,-951,2433],[389,393,124],[432,342,135],[462,305,132],[491,268,127],[517,230,121],[553,-80,-600],[564,161,93],[602,94,61],[633,24,23],[657,-49,-23],[674,-125,-78],[675,-281,-220],[681,-203,-143]]
P=list(map(tuple,P0))
def dot(a,b): return sum(x*y for x,y in zip(a,b))
def sub(a,b): return tuple(x-y for x,y in zip(a,b))
def cross(a,b): return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def primitive(v):
    g=math.gcd(*v)
    return tuple(x//g for x in v) if g else tuple(v)
def hull(P):
    faces=[]; edges=defaultdict(list)
    for ids in combinations(range(len(P)),3):
        a,b,c=[P[i] for i in ids]; m=cross(sub(b,a),sub(c,a))
        if not any(m):continue
        h=dot(m,a); ss=[dot(m,p)-h for p in P]
        if min(ss)<0<max(ss): continue
        if max(ss)==min(ss): continue
        if max(ss)>0: m=tuple(-x for x in m); ids=(ids[0],ids[2],ids[1]); h=-h
        assert sum(s==0 for s in ss)==3, 'Non-simplicial input'
        m=primitive(m); h=dot(m,a); i=len(faces);faces.append((ids,m,h))
        for e in combinations(ids,2):edges[tuple(sorted(e))].append(i)
    assert all(len(v)==2 for v in edges.values())
    return faces,dict(edges)
def moments(P,faces):
    D=0; T=[0,0,0]
    for ids,m,h in faces:
        a,b,c=[P[i] for i in ids];d=dot(a,cross(b,c));D+=d
        for k in range(3):T[k]+=d*(a[k]+b[k]+c[k])
    assert D>0
    return F(D,6),tuple(F(t,4*D) for t in T)
def controls(P,faces,n,h):
    z=[dot(n,p)-h for p in P]; active=[]; bounds=[]
    for fi,(ids,m,b) in enumerate(faces):
        lo=min(z[i] for i in ids);hi=max(z[i] for i in ids)
        if lo<0<hi:active.append(fi)
        B=[]
        if lo<0:
            B.extend(F(b-dot(m,p),zj) for p,zj in zip(P,z) if zj>0)
        if hi>0:
            B.extend(F(b-dot(m,p),-zj) for p,zj in zip(P,z) if zj<0)
        assert B
        bounds.append(min(B))
    return z,active,bounds



def add(a,b):return tuple(x+y for x,y in zip(a,b))
def scale(a,t):return tuple(t*x for x in a)
def det(a,b,c):return dot(a,cross(b,c))
def primitive_plane(m,h):
    q=tuple(map(F,(*m,h)));D=math.lcm(*(x.denominator for x in q))
    w=tuple(int(x*D) for x in q);g=math.gcd(*w)
    return tuple(x//g for x in w)
def rational(x):
    if isinstance(x,F):return str(x)
    if isinstance(x,dict):return {str(k):rational(v) for k,v in x.items()}
    if isinstance(x,(tuple,list)):return [rational(v) for v in x]
    return x

def complex_from_supports(points,planes):
    """Exact extreme points and maximal facets from certified supporting planes."""
    points=sorted(set(points));planes=sorted(set(planes))
    for pl in planes:
        assert all(dot(pl[:3],x)<=pl[3] for x in points)
    active=[[j for j,pl in enumerate(planes) if dot(pl[:3],x)==pl[3]] for x in points]
    keep=[]
    for i,act in enumerate(active):
        if any(det(planes[a][:3],planes[b][:3],planes[c][:3]) for a,b,c in combinations(act,3)):keep.append(i)
    X=[points[i] for i in keep]
    facets=[];usedplanes=[]
    for pl in planes:
        ids=[i for i,p in enumerate(X) if dot(pl[:3],p)==pl[3]]
        if len(ids)>=3:
            assert any(cross(sub(X[b],X[a]),sub(X[c],X[a]))!=(0,0,0) for a,b,c in combinations(ids,3))
            facets.append(set(ids));usedplanes.append(pl)
    order=sorted(range(len(facets)),key=lambda j:sorted(facets[j]))
    facets=[facets[j] for j in order];usedplanes=[usedplanes[j] for j in order]
    E=defaultdict(list)
    for a,b in combinations(range(len(facets)),2):
        common=facets[a]&facets[b]
        if len(common)>=2:
            assert len(common)==2
            E[tuple(sorted(common))].extend((a,b))
    assert all(len(f)==2 for f in E.values())
    oriented=[]
    for fi,vs in enumerate(facets):
        adj=defaultdict(list)
        for (a,b),owners in E.items():
            if fi in owners:adj[a].append(b);adj[b].append(a)
        assert set(adj)==vs and all(len(z)==2 for z in adj.values())
        start=min(vs);path=[start,min(adj[start])]
        while True:
            q=next(x for x in adj[path[-1]] if x!=path[-2])
            if q==start:break
            assert q not in path;path.append(q)
        assert set(path)==vs
        if dot(cross(sub(X[path[1]],X[path[0]]),sub(X[path[2]],X[path[0]])),usedplanes[fi][:3])<0:
            path=[path[0]]+list(reversed(path[1:]))
        oriented.append(path)
    assert len(X)-len(E)+len(facets)==2
    return X,oriented,usedplanes,dict(E)

def integrate(X,faces,q=None):
    if q is None:q=tuple(sum(p[k] for p in X)/len(X) for k in range(3))
    V=F(0);M=(F(0),)*3
    for f in faces:
        for a,b,c in ((f[0],f[i],f[i+1]) for i in range(1,len(f)-1)):
            A,B,C=X[a],X[b],X[c];v=det(sub(A,q),sub(B,q),sub(C,q))/6
            assert v>0
            V+=v;M=add(M,scale(add(add(A,B),add(C,q)),v/4))
    assert V>0
    return V,M,scale(M,1/V)

def census(X,faces,planes,E,c):
    Y=[sub(x,c) for x in X];strict=[[],[],[]];weak=[[],[],[]]
    counters={k:[0,0,0] for k in ('vertex','side','edge')}
    def record(kind,values):
        for x in values:counters[kind][(x>0)-(x<0)+1]+=1
    for i,x in enumerate(Y):
        vals=[dot(x,sub(y,x)) for j,y in enumerate(Y) if j!=i];record('vertex',vals)
        if max(vals)<=0:(strict if max(vals)<0 else weak)[1].append(i)
    for fi,(ids,pl) in enumerate(zip(faces,planes)):
        m=pl[:3];s=pl[3]-dot(m,c);assert s>0
        foot=add(c,scale(m,s/dot(m,m)))
        vals=[dot(cross(sub(X[b],X[a]),sub(foot,X[a])),m) for a,b in zip(ids,ids[1:]+ids[:1])]
        record('side',vals)
        if min(vals)>=0:(strict if min(vals)>0 else weak)[0].append(fi)
    for (i,j),(f,g) in sorted(E.items()):
        a=Y[i];d=sub(Y[j],a);t=-dot(a,d)/dot(d,d);q=add(a,scale(d,t))
        n,m=planes[f][:3],planes[g][:3]
        aa=dot(n,n);bb=dot(n,m);cc=dot(m,m);disc=aa*cc-bb*bb;assert disc>0
        lam=(cc*dot(q,n)-bb*dot(q,m))/disc
        mu=(aa*dot(q,m)-bb*dot(q,n))/disc
        assert q==add(scale(n,lam),scale(m,mu))
        record('edge',[t,1-t,lam,mu])
        if min(t,1-t,lam,mu)>=0:(strict if min(t,1-t,lam,mu)>0 else weak)[2].append([i,j])
    assert len(strict[0])+len(strict[1])-len(strict[2])==2 if not any(weak) else True
    return dict(strict_counts=list(map(len,strict)),additional_weak_counts=list(map(len,weak)),strict=strict,additional_weak=weak,primitive_signs=counters)

def chord(a,b):
    A=dot(a,a);B=dot(a,b);C=dot(b,b)
    if B>=A:return A
    if B>=C:return C
    return (A*C-B*B)/(A+C-2*B)

def barcode(X,skeleton):
    X=list(X);rr=[dot(x,x) for x in X];edges=[]
    for i,j in combinations(range(len(X)),2):edges.append((chord(X[i],X[j]),i,j))
    edges.sort(key=lambda x:(-x[0],x[1],x[2]))
    par=list(range(len(X)));peak=par.copy();members=[{i} for i in par];bars=[];tree=defaultdict(list)
    def root(i):
        while i!=par[i]:par[i]=par[par[i]];i=par[i]
        return i
    # Equal levels produce zero bars for ephemeral components; positive pairs are unchanged.
    for death,u,v in edges:
        i,j=root(u),root(v)
        if i==j:continue
        if (rr[peak[i]],-peak[i])<(rr[peak[j]],-peak[j]):i,j=j,i
        birth=rr[peak[j]]
        if birth>death:
            bars.append(dict(root=peak[j],elder=peak[i],birth=birth,death=death,depth=(birth-death)/birth,
                             component=sorted(members[j]),attaining=[u,v]))
        tree[u].append(v);tree[v].append(u);par[j]=i;members[i]|=members[j]
    for bar in bars:
        # Canonical strict-superlevel component, independent of equal-level processing order.
        above=defaultdict(list)
        for w,i,j in edges:
            if w>bar['death']:above[i].append(j);above[j].append(i)
        comp={bar['root']};todo=[bar['root']]
        for u in todo:
            for v in above[u]:
                if v not in comp:comp.add(v);todo.append(v)
        bar['component']=sorted(comp)
        cut=[(w,i,j) for w,i,j in edges if (i in comp)!=(j in comp)]
        assert max(w for w,i,j in cut)==bar['death']
        bar['complete_chord_cut_count']=len(cut)
        bar['max_cut_witnesses']=[[i,j] for w,i,j in cut if w==bar['death']]
        truecut=[(chord(X[i],X[j]),i,j) for i,j in skeleton if (i in comp)!=(j in comp)]
        assert max(w for w,i,j in truecut)==bar['death']
        bar['true_edge_cut']=[[i,j] for w,i,j in truecut]
        bar['true_cut_max_witnesses']=[[i,j] for w,i,j in truecut if w==bar['death']]
        eligible=defaultdict(list)
        for i,j in skeleton:
            if chord(X[i],X[j])>=bar['death']:eligible[i].append(j);eligible[j].append(i)
        target=bar['elder'];start=bar['root'];todo=[start];prev={start:None}
        for u in todo:
            if u==target:break
            for v in sorted(eligible[u]):
                if v not in prev:prev[v]=u;todo.append(v)
        assert target in prev
        path=[target]
        while path[-1]!=start:path.append(prev[path[-1]])
        path.reverse();assert min(chord(X[a],X[b]) for a,b in zip(path,path[1:]))==bar['death']
        bar['attaining_true_edge_path']=path
    return sorted(bars,key=lambda b:(-b['depth'],b['root']))

def hinge_body(n,h,v):
    faces,edges=hull(P);z,active,bounds=controls(P,faces,n,h)
    assert min(z)<0<max(z) and dot(n,v)==0
    slacks=[B-dot(m,v) for (_,m,_),B in zip(faces,bounds)];assert min(slacks)>=0
    cp=[tuple(F(z[i]*P[j][k]-z[j]*P[i][k],z[i]-z[j]) for k in range(3))
        for i,j in edges if z[i]*z[j]<0]
    pts=[add(tuple(map(F,p)),scale(v,max(0,zz))) for p,zz in zip(P,z)]+cp
    planes=[]
    for ids,m,b in faces:
        if min(z[i] for i in ids)<0:planes.append(primitive_plane(m,b))
        if max(z[i] for i in ids)>0:
            mv=dot(m,v);planes.append(primitive_plane(sub(m,scale(n,mv)),b-mv*h))
    X,ff,pl,ee=complex_from_supports(pts,planes)
    V,M,c=integrate(X,ff)
    V0,c0=moments(P,faces);assert V==V0
    # Independent clipped-upper mass determines the affine first-moment law.
    upper=[tuple(map(F,p)) for p,zz in zip(P,z) if zz>=0]+cp
    upp=[primitive_plane(m,b) for ids,m,b in faces]+[primitive_plane(scale(n,-1),-h)]
    up,uf,un,ue=complex_from_supports(upper,upp);vp,mp,cu=integrate(up,uf)
    J=dot(n,mp)-h*vp
    expected=add(scale(c0,V0),scale(v,J));assert M==expected
    report=census(X,ff,pl,ee,c)
    PX=[scale(sub(x,c),F(1,1000)) for x in X];QX=[scale(p[:3],1000/(p[3]-dot(p[:3],c))) for p in pl]
    report.update(VEF=[len(X),len(ee),len(ff)],C=2*len(ee),volume=V/10**9,
                  centroid=scale(c,F(1,1000)),moment=scale(M,F(1,10**12)),
                  exact_volume_and_affine_moment_law=True,
                  vertices=[scale(x,F(1,1000)) for x in X],facets=ff,edges=sorted(ee),
                  support_planes=[primitive_plane(scale(p[:3],1000),p[3]) for p in pl],original_integral_coordinate_units=1000,
                  P=barcode(PX,sorted(ee)),Q=barcode(QX,sorted(tuple(sorted(v)) for v in ee.values())),velocity=v,n=n,h=h,
                  convexity_slacks=slacks,upper_volume=vp/10**9,upper_moment=scale(mp,F(1,10**12)))
    assert len(report['P'])==report['strict_counts'][1]-1
    assert len(report['Q'])==report['strict_counts'][0]-1
    return report

def main():
    # Exact rational interior point in the velocity triangle for edge15--29/vertex42 cut.
    n=(-325273,-698874,-240310);h=-45275161
    v0=scale((6558183650,-10897765265,22816215436),F(896003,43031309628659688161280))
    v1=scale((9143958392,-13454834289,26752740547),F(896003,57272582292669275259520))
    mode=sys.argv[1] if len(sys.argv)>1 else 'interior'
    v=scale(v1,F(1,2)) if mode=='ray' else add(scale(v0,F(1,60)),scale(v1,F(59,120)))
    out=hinge_body(n,h,v);raw=(json.dumps(rational(out),sort_keys=True,separators=(',',':'))+'\n').encode()
    path=Path(__file__).with_name('hinge_'+mode+'_exact.json');path.write_bytes(raw)
    print('HINGE_EXACT_BODY_PASS',mode,out['VEF'],out['strict_counts'],out['additional_weak_counts'],len(out['P']),len(out['Q']),
          [float(x['depth']) for x in out['P']],[float(x['depth']) for x in out['Q']],len(raw),hashlib.sha256(raw).hexdigest())
if __name__=='__main__':main()
```
