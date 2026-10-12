# material-257afebf9e10

AI research material · [Export notes](../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

# EXACT_H44_POLAR_W0: exact non-record controls in the own-polar/metric orbit

## Object, provenance and status
These are newly rationalized finite descendants of the literal R3_H44_GROWN_S1_G6 input in immutable worker result figure-0531, SHAcdadf1fd175ad297d3d77738f88d2a85ebefc9f0d8c576774c2bd2f7aeb5d533, read fully before use. The 44 H rows below are the complete literal input, not an alleged FULLQ alias. A coordinator numerical search (LEAD_H44_POLAR24 witness0; all four recovery parts preserved separately) found a finite pole and metric. The present exact objects are defined exclusively by integer H44 and PINS below, not by binary64 optimizer parameters or exponential reevaluation.
For row n_i/1000000, pole z=Z/D and matrix A=M/D, the exact vertex is M*n_i/(D*1000000-n_i·Z). Every denominator is verified positive and det(M)>0. Reduced homogeneous integer rows completely recover the body. All five bodies have V44/E126/F84,C252, so they are within the requested complexity bound but NOT class110.
Grids3,5,6,8 have own(S,U,H)=(2,1,1); grid4 has(3,1,2). All five have additionalweak000 and primitivezero000 under the complete exact primitive audit. This is one exact hull/audit implementation, not two independent exact engines.
Coarsest G3 uses Z=(-674,-400,92), M=[[709,0,0],[88,1208,0],[-75,-130,1168]],D1000. Its reduced homogeneous coordinate numerators fit32bits, denominators31bits; own-centroid denominators have at most2100bits. Stable facets in the exact lexicographic triple order are16=[2,15,26],51=[9,41,36]; U15; saddle7--28. The elder stable facet contains the sole U. The Q junior component has53 facets/cut21, relative depth .913781097300561; this is deeper than old R3 and not an improved residual-bar record.
All own211 grids have the same S/U/H labels above. G4 adds S54=[9,40,41] and saddle9--41; its extra positive singleton Q bar has relative depth1.188149718884967e-8. It is not suppressed or called weak. Higher decimal precision is therefore not assumed to change the class monotonically.

## Exact method and completeness boundary
The standard-library auditor enumerates every44-choose3 candidate supporting plane with integer homogeneous cofactors, tests all44 points, retains every supporting triple, and rejects nontriangular maximal facets. Thus no numerical triangulation or incidence guess controls the final hull. It checks every input point is extreme, two true facets per true edge, Euler, strict interior of the origin, positive oriented tetrahedron volumes, and strict interior of the computed homogeneous volume centroid.
The centroid is the exact oriented-tetrahedral first moment divided by exact volume. Face predicates are the three signed boundary-edge tests for the orthogonal facet foot. Vertex predicates are all outgoing edge radial dot products. Edge predicates are the two segment-parameter signs and two positive-cone Gram numerators from its two outward face normals. Strict and closed-weak alternatives are tested for every physical face/vertex/edge; every raw primitive zero is reported. Exact P/Q graph filtrations retain every positive rational bar, including the small G4 bar. Euler is only a consistency check, not a substitute for primitive census. Non-simplicial inputs are explicitly rejected by this reusable unit and require a different maximal-facet engine.

## Recovery, verification and expected bytes
Save the complete code block as EXACT_H44_POLAR_W0.py, UTF-8 LF with terminal newline:9333bytes SHA25673b4495500e1c0413127c7abdda4e8732daad008e8d136cd0f6f4015295c905e.
No source file or local checkpoint outside this capsule is required. CPython3.13.5 standard library only; no NumPy/SciPy or network dependency. Reconstruction and verification command:
```
python -B -S EXACT_H44_POLAR_W0.py --grids 3,4,5,6,8 --out EXACT_H44_POLAR_W0.json
```
Expected control lines:
```
EXACT_H44_POLAR_W0_CONTROL 3 44 126 84 2 1 1 0 0 0 0 0 0
EXACT_H44_POLAR_W0_CONTROL 4 44 126 84 3 1 2 0 0 0 0 0 0
EXACT_H44_POLAR_W0_CONTROL 5 44 126 84 2 1 1 0 0 0 0 0 0
EXACT_H44_POLAR_W0_CONTROL 6 44 126 84 2 1 1 0 0 0 0 0 0
EXACT_H44_POLAR_W0_CONTROL 8 44 126 84 2 1 1 0 0 0 0 0 0
EXACT_H44_POLAR_W0_RECOVERY_PASS 5 174858 7a6f17cca6ab5286d8066d7ae6e5b5bf6b3ef10ca84d187920cfd0ff85226660
```
EXACT_H44_POLAR_W0.json174858bytes SHA2567a6f17cca6ab5286d8066d7ae6e5b5bf6b3ef10ca84d187920cfd0ff85226660 contains every exact homogeneous vertex, oriented maximal facet, true edge and edge ownership, volume, first moment, own centroid, all primitive equilibrium labels and zero sets, raw minimum absolute predicate values, and complete rational P/Q bars with their components/cuts. This output was generated and checked before permanent storage; the source and all exact inputs below make it reconstructible without the original sandbox.

```python
"""EXACT_H44_POLAR_W0: rational non-record homogeneous own-centroid controls.
Self-contained standard-library generator and complete simplicial hull audit.
Every potential supporting triple is enumerated exactly. This auditor rejects
non-triangular maximal faces rather than silently treating diagonals as edges.
No floating predicates or optimization are used during reconstruction/audit.
Run python -B -S EXACT_H44_POLAR_W0.py --out EXACT_H44_POLAR_W0.json.
"""
import argparse,hashlib,itertools,json,math,sys
from fractions import Fraction as F
from pathlib import Path
sys.set_int_max_str_digits(0)
H44=[[-910728, 789910, -290980, 1000000], [-815027, 1495305, 26495, 1000000], [-862516, 479207, -458064, 1000000], [-893470, 1111850, -141095, 1000000], [-617519, 2021021, 650689, 1000000], [-655450, 1962149, 248395, 1000000], [-142760, -912800, -734235, 1000000], [-333584, 937912, -1102726, 1000000], [-100531, -157666, -955666, 1000000], [449937, 1176903, -1530338, 1000000], [-440133, 1910662, 1460261, 1000000], [-241218, 2053446, -733049, 1000000], [-71846, 1705776, -1150719, 1000000], [414758, -1541987, -70898, 1000000], [142699, -1250380, -512623, 1000000], [838678, -1819380, 829457, 1000000], [-474041, 2104433, -226173, 1000000], [-545740, 2008697, 1050447, 1000000], [-292461, 1740742, 1851404, 1000000], [-97947, 1497603, 2214614, 1000000], [-133899, 1592168, 1834462, 1000000], [129678, 1158344, 2515502, 1000000], [379534, 726572, 2717864, 1000000], [622488, 207097, 2771305, 1000000], [822136, -360098, 2633928, 1000000], [944206, -932947, 2275965, 1000000], [947991, -1421527, 1702571, 1000000], [-616338, 233717, -655870, 1000000], [-366546, -122629, -788911, 1000000], [-48051, -192200, -969504, 1000000], [191867, -689682, -879888, 1000000], [-131202, 514325, -1099556, 1000000], [39829, 1634533, -1166733, 1000000], [35281, 1605926, -168952, 1000000], [310924, -837450, -624566, 1000000], [567816, -1018677, -104222, 1000000], [961592, -748577, 476916, 1000000], [353858, 1009696, 1191052, 1000000], [566062, 692408, 1277821, 1000000], [844972, 298639, 1185414, 1000000], [990151, -6950, 874001, 1000000], [1014262, -472136, 664725, 1000000], [-178306, 1616491, 1964304, 1000000], [-34361, 1418442, 2181920, 1000000]]
PINS={'3': {'D': 1000, 'z': [-674, -400, 92], 'A': [[709, 0, 0], [88, 1208, 0], [-75, -130, 1168]]}, '4': {'D': 10000, 'z': [-6743, -3996, 922], 'A': [[7087, 0, 0], [877, 12082, 0], [-749, -1297, 11678]]}, '5': {'D': 100000, 'z': [-67428, -39963, 9222], 'A': [[70873, 0, 0], [8774, 120824, 0], [-7485, -12974, 116779]]}, '6': {'D': 1000000, 'z': [-674279, -399626, 92219], 'A': [[708731, 0, 0], [87736, 1208245, 0], [-74854, -129737, 1167787]]}, '8': {'D': 100000000, 'z': [-67427895, -39962592, 9221899], 'A': [[70873074, 0, 0], [8773597, 120824486, 0], [-7485429, -12973708, 116778738]]}}
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def det(a,b,c):return dot(a,cross(b,c))
def plane(a,b,c):
    C=[det(tuple(p[k] for k in range(4) if k!=j),tuple(q[k] for k in range(4) if k!=j),tuple(r[k] for k in range(4) if k!=j)) for j in range(4) for p,q,r in [(a,b,c)]]
    return (C[0],-C[1],C[2],C[3])
def primitive(v):
    g=math.gcd(*v)
    return tuple(x//g for x in v)
def construct(pin):
    D=pin['D'];z=pin['z'];A=pin['A']
    assert det(*A)>0
    points=[]
    for row in H44:
        n=row[:3];w=D*row[3]-dot(n,z)
        assert w>0
        p=tuple(dot(r,n) for r in A)+(w,)
        points.append(primitive(p))
    assert len(set(points))==len(points)
    return points

def hull(P):
    planes={}
    for i,j,k in itertools.combinations(range(len(P)),3):
        h=plane(P[i],P[j],P[k]);n=h[:3]
        if not any(n):continue
        pos=neg=False;zeros=[]
        for m,p in enumerate(P):
            s=dot(n,p[:3])-h[3]*p[3]
            pos|=s>0;neg|=s<0
            if s==0:zeros.append(m)
            if pos and neg:break
        if pos and neg:continue
        assert pos or neg,'not three dimensional'
        if pos:h=tuple(-v for v in h)
        h=primitive(h)
        assert len(zeros)==3,('non-simplicial face',zeros)
        planes[tuple(zeros)]=h
    facets=[];normals=[];heights=[];owners={}
    for key,h in sorted(planes.items()):
        t=list(key);assert h[3]>0,'origin must be strictly interior'
        if det(*(P[i][:3] for i in t))<0:t[1],t[2]=t[2],t[1]
        assert det(*(P[i][:3] for i in t))>0
        fi=len(facets);facets.append(t);normals.append(h[:3]);heights.append(h[3])
        for i in range(3):owners.setdefault(tuple(sorted((t[i],t[(i+1)%3]))),[]).append(fi)
    extreme=sorted(set(itertools.chain.from_iterable(facets)))
    assert extreme==list(range(len(P)))
    assert all(len(v)==2 for v in owners.values())
    assert len(P)-len(owners)+len(facets)==2
    return facets,normals,heights,owners

def bars(V,E):
    birth=[dot(v,v) for v in V];events=[]
    for e in E:
        i,j=e;a=V[i];d=sub(V[j],a);dd=dot(d,d);t=max(F(0),min(F(1),-dot(a,d)/dd))
        p=tuple(a[k]+t*d[k] for k in range(3));events.append((dot(p,p),e))
    parent=list(range(len(V)));components=[{i} for i in parent]
    def root(i):
        while parent[i]!=i:parent[i]=parent[parent[i]];i=parent[i]
        return i
    out=[]
    for death,e in sorted(events,key=lambda t:(-t[0],t[1])):
        i,j=map(root,e)
        if i==j:continue
        if (birth[i],-i)<(birth[j],-j):i,j=j,i
        assert birth[j]>=death
        if birth[j]>death:
            comp=sorted(components[j]);cut=[list(a) for a in E if (a[0] in components[j]) != (a[1] in components[j])]
            out.append({'peak':j,'elder':i,'saddle_edge':list(e),'birth':birth[j],'death':death,'relative_depth':(birth[j]-death)/birth[j],'component':comp,'cut':cut})
        parent[j]=i;components[i]|=components[j]
    return sorted(out,key=lambda b:-b['relative_depth'])

def audit(P):
    facets,N,B,owners=hull(P);E=sorted(owners)
    V=[tuple(F(p[k],p[3]) for k in range(3)) for p in P]
    vol6=F(0);mom24=[F(0)]*3
    for t in facets:
        a,b,c=[V[i] for i in t];d=det(a,b,c);assert d>0
        vol6+=d
        for k in range(3):mom24[k]+=d*(a[k]+b[k]+c[k])
    g=tuple(v/(4*vol6) for v in mom24);Y=[sub(v,g) for v in V]
    h=[B[i]-dot(n,g) for i,n in enumerate(N)];assert min(h)>0
    S=[];U=[];H=[];weak=[[],[],[]];zeros=[[],[],[]];factors=[[],[],[]]
    for fi,t in enumerate(facets):
        n=N[fi];nn=dot(n,n)
        vals=[]
        for a,b in zip(t,t[1:]+t[:1]):
            d=sub(V[b],V[a]);p=tuple(nn*(g[k]-V[a][k])+h[fi]*n[k] for k in range(3))
            vals.append(dot(cross(d,p),n))
        factors[0].extend(vals)
        if all(x>0 for x in vals):S.append(fi)
        elif all(x>=0 for x in vals):weak[0].append(fi)
        if any(x==0 for x in vals):zeros[0].append(fi)
    nbr=[[] for _ in V]
    for i,j in E:nbr[i].append(j);nbr[j].append(i)
    for i in range(len(V)):
        vals=[-dot(Y[i],sub(V[j],V[i])) for j in nbr[i]]
        factors[1].extend(vals)
        if all(x>0 for x in vals):U.append(i)
        elif all(x>=0 for x in vals):weak[1].append(i)
        if any(x==0 for x in vals):zeros[1].append(i)
    for i,j in E:
        d=sub(V[j],V[i]);dd=dot(d,d);t=-dot(Y[i],d)
        p=tuple(dd*Y[i][k]+t*d[k] for k in range(3));a,b=[N[f] for f in owners[i,j]]
        aa,ab,bb=dot(a,a),dot(a,b),dot(b,b)
        assert aa*bb-ab*ab>0 and dot(p,d)==0
        la=dot(p,a)*bb-dot(p,b)*ab;lb=dot(p,b)*aa-dot(p,a)*ab
        vals=[t,dd-t,la,lb];factors[2].extend(vals)
        if all(x>0 for x in vals):H.append([i,j])
        elif all(x>=0 for x in vals):weak[2].append([i,j])
        if any(x==0 for x in vals):zeros[2].append([i,j])
    Q=[tuple(F(n[k],1)/hi for k in range(3)) for n,hi in zip(N,h)]
    pb=bars(Y,E);qb=bars(Q,[tuple(v) for v in owners.values()])
    assert len(pb)==len(U)-1 and len(qb)==len(S)-1
    assert len(S)+len(U)-len(H)==2
    return {'V':len(V),'E':len(E),'F':len(facets),'C':2*len(E),'volume':vol6/6,'first_moment':[m/24 for m in mom24],'centroid':g,'S':S,'U':U,'H':H,'additional_weak':weak,'primitive_zero':zeros,'primitive_counts':[len(x) for x in factors],'primitive_min_abs':[min(map(abs,x)) for x in factors],'facet_vertices':facets,'edges':[list(e) for e in E],'edge_owners':[owners[e] for e in E],'homogeneous_vertices':P,'P':pb,'Q':qb}

def encode(x):
    if isinstance(x,F):return str(x.numerator)+'/'+str(x.denominator)
    raise TypeError(type(x).__name__)
def main():
    p=argparse.ArgumentParser();p.add_argument('--grids',default='3,4,5,6,8');p.add_argument('--out',default='EXACT_H44_POLAR_W0.json');a=p.parse_args()
    out={'object_family':'EXACT_H44_POLAR_W0','arithmetic':'rational; no floating predicates','controls':{}}
    for k in a.grids.split(','):
        r=audit(construct(PINS[k]));out['controls'][k]={'pin':PINS[k],'audit':r}
        print('EXACT_H44_POLAR_W0_CONTROL',k,r['V'],r['E'],r['F'],*[len(r[t]) for t in ['S','U','H']],*[len(v) for v in r['additional_weak']],*[len(v) for v in r['primitive_zero']],flush=True)
    b=(json.dumps(out,default=encode,sort_keys=True,separators=(',',':'))+'\n').encode();Path(a.out).write_bytes(b)
    print('EXACT_H44_POLAR_W0_RECOVERY_PASS',len(out['controls']),len(b),hashlib.sha256(b).hexdigest())
if __name__=='__main__':main()
```
