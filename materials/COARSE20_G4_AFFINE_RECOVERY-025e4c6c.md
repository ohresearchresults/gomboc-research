# material-025e4c6c2c9c

AI research material · [Export notes](../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

# COARSE20_G4: exact rebuild and affine necessary window

## Identity and evidence
Literal H-body COARSE20_G4 from completely read immutable parent figure-0420, SHA-256 0840306c532921996e889d886712fcd1b324432e7bb980bd811a06f2eaf01031. It remains V86/E129/F45,C258,own strict121,weak000; NOT a new class110 body. This fresh rational source rebuilds its maximal complex and uniform filled-volume centroid. Every raw vertex, true edge, cyclic face, centroid and volume agreed exactly with the parent's A audit. The parent's byte-identical H.json is included below.
This does not claim recovery of old ephemeral coordinator scratch programs. Earlier archived affine-cut prose without a complete source is superseded by this exact cut and these numerical intervals; do not substitute different vertex-index sets or old rounded numbers.

## Root-carrier-free affine cut
Let X be own-centred vertices, G=A^T A positive definite, and g(x)=x^T G x. The script computes h as the minimum squared Euclidean radius on saddle edge(82,85). K is the component of vertex25 using only true edges whose whole segment has minimum squared radius greater than h:
[21,22,23,24,25,26,27,29,30,33,34,38,44,45,48,49,57,68,69,83,84,85].
The18 crossing edges are:
[[1,21],[2,22],[4,30],[5,27],[6,33],[8,38],[10,23],[10,26],[11,24],[17,44],[17,45],[19,29],[34,35],[41,44],[68,71],[75,84],[79,85],[82,85]].
Each has a rational gate of norm squared<=h; the generated certificate gives literal coordinates and parameters. Endpoint gates are allowed. The two sides contain anchors0 and25. Put B=min(|X_0|^2,|X_25|^2). If kappa(G)<B/h, each side has a vertex with g>=lambda_min(G)B while all gates have g<=lambda_max(G)h. Choose the maximum-g vertex on each side. An internal edge to y obeys
2 x^T G(y-x)=g(y)-g(x)-(y-x)^T G(y-x)<0.
For an exiting edge its lower-valued gate gives a strictly negative initial derivative by the same identity. Both selected vertices are distinct strict unstable equilibria, regardless of root-carrier migration. Thus U>=2.
B/h lies in [2013394692610,2013394692611)/10^12; kappa(G)<=2 is excluded for U=1. B-2h lies in [9871325096,9871325097)/10^12; (B/2-h)/R^2 in [1866539820,1866539821)/10^12. Equality at the threshold is not settled.

## General bounded spectral window
Suppose r B_3 subset K subset R B_3, centred at0, and A has singular values sigma1>=sigma2>=sigma3>0. If sigma1/sigma2>R/r, split K by the central plane orthogonal to the first right singular vector. Each cap contains +/-r u, with transformed squared radius sigma1^2 r^2. The whole central section has transformed squared radius<=sigma2^2 R^2. A maximum on either cap cannot lie in that section. It occurs at an original vertex. Internal edges and edges reaching the lower central section have strictly negative initial radial derivative. Consequently AK has at least two strict unstable equilibria.
Apply this also to (AK)^polar=A^{-T}K^polar, whose inner/outer radii are1/R and1/r. If sigma2/sigma3>R/r, the polar has at least two strict unstable equilibria, hence AK has at least two strict stable face equilibria. Polarity uses the chosen origin, not the polar's own mass centroid. Uniform filled-volume centroids are affine covariant.
Therefore simultaneous S=U=1 requires
lambda1(G)/lambda2(G)<=(R/r)^2,
lambda2(G)/lambda3(G)<=(R/r)^2,
kappa(G)<=(R/r)^4.
These are necessary, not sufficient; they do not exclude the entire affine orbit.
Here R^2=max_i |X_i|^2 and r^2=min_f (b_f-n_f.c)^2/(n_f.n_f), attained at outer vertex0 and inner facet0. The exact adjacent bound R^2/r^2 lies in [9449228955489,9449228955490)/10^12; its square lies in [89287927853269,89287927853270)/10^12. The necessary condition window is therefore B/h<=kappa(G)<=(R/r)^4, approximately[2.013394692610,89.287927853270], with each adjacent ratio<=approximately9.449228955490. Scalar metric normalization is free. Nonlinear support/normal deformation is not restricted by this fixed-body affine exclusion.

## Deterministic recovery and verification
Save the complete fenced units as H.json and EXACT.py with LF endings and one final newline. Environment: Python3.11.8 standard library only, assertions enabled. No numerical hull/optimizer or third-party dependency.
Reconstruction and verification command:
    python -B -S EXACT.py H.json CERTIFICATE.json
Expected terminal output:
    C258_REBUILT_CONTROLS_PASS tetra446/000 prism446/123
    C258_REBUILT_EXACT_OWN121_WEAK000_PASS 86 129 45 168
    C258_REBUILT_AFFINE_TWO_U_PASS 22 18 [2013394692610, 2013394692611, 1000000000000]
    C258_AFFINE_SPECTRAL_WINDOW_PASS [9449228955489, 9449228955490, 1000000000000] [89287927853269, 89287927853270, 1000000000000]
    OUTPUT 1275380 cddaa6332f2f5ab95cb605c7bce8bb03660852018d89ef7b17f5d45228c7213d
Files:
H.json:1122bytes SHA256 80981f4c9fcf91d6b402e0b85d82d40d5a260eecf23888bdf2d3041d5dfa9011.
EXACT.py:6985bytes SHA256 4e847364725867accff2dc81807a2416a5e505931f94eb2377b6661988395d54.
CERTIFICATE.json:1275380bytes SHA256 cddaa6332f2f5ab95cb605c7bce8bb03660852018d89ef7b17f5d45228c7213d.
The large rational output is completely regenerated by these small sources.168 positive tetrahedra integrate the exact own-centred body; translated first moments vanish. Controls: tetrahedron strict446/weak000 and deliberately weak prism strict446/weak123. Neither is accepted as target.

### H.json
```json
{"H":[[-23190,-6905,7908,10000],[-23088,97,6721,10000],[-21661,5105,5356,10000],[-17597,11697,2180,10000],[-16506,-12372,7875,10000],[-15397,13821,443,10000],[-13071,15339,-1234,10000],[-10613,16339,-2844,10000],[-10253,-15023,6915,10000],[-9872,4347,2001,5000],[-8199,16851,-4303,10000],[-6376,-16759,4976,10000],[-5833,16950,-5611,10000],[-3665,16729,-6919,10000],[-2678,-17455,2777,10000],[-167,1623,-810,1000],[297,15435,-9155,10000],[1155,-15101,3297,10000],[2197,-10814,-6880,10000],[2201,14349,-10087,10000],[2405,622,276,2500],[3006,1081,6706,10000],[3264,4489,-6993,5000],[3833,13183,-10670,10000],[3962,-12705,3497,10000],[4347,2304,6079,10000],[5291,968,-435,5000],[5412,11703,-11335,10000],[5706,613,-3769,5000],[5736,-9516,4393,10000],[5828,11380,-5775,10000],[6814,10496,-10529,10000],[7703,5260,-15433,10000],[7842,-4197,-15197,10000],[8079,9158,-9659,10000],[8156,2782,3261,10000],[8256,790,-15971,10000],[9073,7863,-8907,10000],[9942,6471,-7945,10000],[10587,-1650,-4026,10000],[10595,5108,-7165,10000],[11131,3547,-6374,10000],[11185,-1885,-8502,10000],[11301,1137,-2946,10000],[11329,2340,-4572,10000]]}
```

### EXACT.py
```python
"""Exact own-centroid maximal geometry and affine two-basin certificate.
Python 3.11+ standard library; no numerical hull or optimizer is used.
Run: python -B -S EXACT.py H.json certificate.json
"""
from fractions import Fraction as Q
from itertools import combinations
from pathlib import Path
import hashlib,json,sys
sys.set_int_max_str_digits(0)
def dot(a,b): return sum(x*y for x,y in zip(a,b))
def sub(a,b): return tuple(x-y for x,y in zip(a,b))
def cross(a,b): return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def det(a,b,c): return dot(a,cross(b,c))
def sgn(a): return (a>0)-(a<0)
def geometry(H):
    assert len(H)>=4 and all(len(r)==4 and r[3]>0 for r in H)
    points=set()
    for a,b,c in combinations(H,3):
        d=det(a[:3],b[:3],c[:3])
        if not d: continue
        bc,ca,ab=cross(b,c),cross(c,a),cross(a,b)
        n=tuple(a[3]*bc[k]+b[3]*ca[k]+c[3]*ab[k] for k in range(3))
        if d<0: d=-d; n=tuple(-x for x in n)
        if all(dot(r[:3],n)<=r[3]*d for r in H): points.add(tuple(Q(x,d) for x in n))
    P=sorted(points); assert len(P)>=4
    owners=[{k for k,r in enumerate(H) if dot(r[:3],p)==r[3]} for p in P]
    edges=[(i,j) for i,j in combinations(range(len(P)),2) if len(owners[i]&owners[j])>=2]
    adj=[[] for p in P]; fadj=[set() for r in H]
    for i,j in edges:
        adj[i].append(j);adj[j].append(i)
        fs=sorted(owners[i]&owners[j]);assert len(fs)==2
        a,b=fs;fadj[a].add(b);fadj[b].add(a)
    faces=[];tri=[]
    for k,r in enumerate(H):
        inds={i for i,o in enumerate(owners) if k in o};assert len(inds)>=3
        around={i:sorted(j for j in adj[i] if j in inds) for i in inds}
        assert all(len(v)==2 for v in around.values())
        start=min(inds);cycle=[start];prev=None;now=start
        while True:
            nxt=next(j for j in around[now] if j!=prev)
            if nxt==start:break
            assert nxt not in cycle
            cycle.append(nxt);prev,now=now,nxt
        assert set(cycle)==inds
        if dot(cross(sub(P[cycle[1]],P[start]),sub(P[cycle[2]],P[start])),r[:3])<0:
            cycle=[cycle[0]]+list(reversed(cycle[1:]))
        faces.append(cycle)
        tri.extend((cycle[0],cycle[t],cycle[t+1]) for t in range(1,len(cycle)-1))
    assert len(P)-len(edges)+len(faces)==2
    D=Q(0);N=[Q(0)]*3
    for i,j,k in tri:
        d=det(P[i],P[j],P[k]);assert d>0;D+=d
        for a in range(3):N[a]+=d*(P[i][a]+P[j][a]+P[k][a])
    vol=D/6;c=tuple(v/(4*D) for v in N)
    X=[sub(p,c) for p in P]
    offsets=[r[3]-dot(r[:3],c) for r in H];assert min(offsets)>0
    polar=[tuple(Q(n)/h for n in r[:3]) for r,h in zip(H,offsets)]
    A={(i,j):dot(X[i],sub(X[j],X[i])) for i in range(len(P)) for j in adj[i]}
    B={(f,g):dot(polar[f],sub(polar[g],polar[f])) for f in range(len(H)) for g in fadj[f]}
    U=[i for i in range(len(P)) if all(A[i,j]<0 for j in adj[i])]
    wU=[i for i in range(len(P)) if max(A[i,j] for j in adj[i])==0]
    S=[f for f in range(len(H)) if all(B[f,g]<0 for g in fadj[f])]
    wS=[f for f in range(len(H)) if max(B[f,g] for g in fadj[f])==0]
    saddle=[];wE=[]
    for i,j in edges:
        f,g=sorted(owners[i]&owners[j]);v=[A[i,j],A[j,i],B[f,g],B[g,f]]
        if max(v)<0:saddle.append((i,j))
        if max(v)==0:wE.append((i,j))
    # An independent translated integration identity, on the same exact complex.
    D2=Q(0);N2=[Q(0)]*3
    for i,j,k in tri:
        d=det(X[i],X[j],X[k]);assert d>0;D2+=d
        for a in range(3):N2[a]+=d*(X[i][a]+X[j][a]+X[k][a])
    assert D2==D and N2==[0,0,0]
    return dict(H=H,P=P,X=X,edges=edges,faces=faces,owners=[sorted(o) for o in owners],
                adj=adj,volume=vol,centroid=c,S=S,U=U,saddles=saddle,
                weak=[wS,wU,wE],tetrahedra=len(tri))
def edge_gate(x,y):
    d=sub(y,x); t=max(Q(0),min(Q(1),-dot(x,d)/dot(d,d)))
    p=tuple(a+t*b for a,b in zip(x,d))
    return t,p,dot(p,p)
def interval(x,scale=10**12):
    n=x.numerator*scale//x.denominator
    return [n,n+1,scale]
def affine_cut(g):
    X=g['X'];E=g['edges'];assert g['U']==[0,25] and g['saddles']==[(82,85)]
    gates={e:edge_gate(X[e[0]],X[e[1]]) for e in E}
    h=gates[82,85][2]; K={25}
    while True:
        old=len(K)
        for (i,j),(_,_,v) in gates.items():
            if v>h and (i in K or j in K):K.update([i,j])
        if len(K)==old:break
    assert 0 not in K
    anchors=[0,25];B=min(dot(X[i],X[i]) for i in anchors)
    boundary=[]
    for (i,j),(t,p,v) in gates.items():
        if (i in K)!=(j in K):
            assert v<=h and 0<=t<=1
            boundary.append(dict(edge=[i,j],t=t,point=p,norm2=v))
    assert len(K)==22 and len(boundary)==18 and B>2*h>0
    R2=max(dot(x,x) for x in X)
    return dict(K=sorted(K),anchors=anchors,gates=boundary,B=B,h=h,
                condition_threshold=B/h,threshold_interval=interval(B/h),
                B_minus_2h_interval=interval(B-2*h),
                barrier_over_R2_interval=interval((B/2-h)/R2))
def encode(x):
    if isinstance(x,Q):return str(x.numerator)+'/'+str(x.denominator)
    if isinstance(x,dict):return {k:encode(v) for k,v in x.items()}
    if isinstance(x,(list,tuple)):return [encode(v) for v in x]
    return x
def main():
    assert __debug__ and len(sys.argv)==3
    tet=geometry([[-1,-1,-1,1],[-1,1,1,1],[1,-1,1,1],[1,1,-1,1]])
    prism=geometry([[1,0,0,1],[-2,3,0,1],[1,-3,0,1],[0,0,1,1],[0,0,-1,1]])
    for obj,weak in [(tet,[0,0,0]),(prism,[1,2,3])]:
        assert [len(obj[k]) for k in ['S','U','saddles']]==[4,4,6]
        assert list(map(len,obj['weak']))==weak
    print('C258_REBUILT_CONTROLS_PASS tetra446/000 prism446/123',flush=True)
    raw=Path(sys.argv[1]).read_bytes()
    assert hashlib.sha256(raw).hexdigest()=='80981f4c9fcf91d6b402e0b85d82d40d5a260eecf23888bdf2d3041d5dfa9011'
    g=geometry(json.loads(raw)['H'])
    assert [len(g[k]) for k in ['P','edges','faces']]==[86,129,45]
    assert g['S']==[0] and g['U']==[0,25] and g['saddles']==[(82,85)]
    assert g['weak']==[[],[],[]] and g['tetrahedra']==168
    a=affine_cut(g)
    X=g['X']; c=g['centroid']
    radii=[dot(x,x) for x in X]
    inr=[(r[3]-dot(r[:3],c))**2/dot(r[:3],r[:3]) for r in g['H']]
    R2=max(radii); r2=min(inr); q2=R2/r2
    a['spectral_window']=dict(R2=R2,r2=r2,outer_vertex=radii.index(R2),inner_face=inr.index(r2),adjacent_metric_ratio_bound=q2,total_metric_condition_bound=q2*q2,adjacent_interval=interval(q2),total_interval=interval(q2*q2))
    out=(json.dumps(encode(dict(geometry=g,affine_cut=a)),sort_keys=True,separators=(',',':'))+'\n').encode()
    Path(sys.argv[2]).write_bytes(out)
    print('C258_REBUILT_EXACT_OWN121_WEAK000_PASS 86 129 45 168',flush=True)
    print('C258_REBUILT_AFFINE_TWO_U_PASS',len(a['K']),len(a['gates']),a['threshold_interval'],flush=True)
    print('C258_AFFINE_SPECTRAL_WINDOW_PASS',a['spectral_window']['adjacent_interval'],a['spectral_window']['total_interval'],flush=True)
    print('OUTPUT',len(out),hashlib.sha256(out).hexdigest(),flush=True)
if __name__=='__main__':main()
```
