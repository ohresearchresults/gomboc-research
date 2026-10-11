# material-863a52d33af2

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

Public derivative: internal-record-identifiers-replaced.

---

# Exact recovery capsule: C114 whole-polar-packet cap, all orientations

Object identity: VL12_DUAL_CANCEL21_G4_WHOLE_POLAR_PACKET_CAP_ALL_ORIENTATIONS.
Exact input authority: literal VL12_DUAL_CANCEL21_G4 in immutable result figure-0438, SHA16684588638a09e8929f3ce23437b244db8ef4f46a3cfe29b4deea8a906b0547. The complete 21-row integer input is repeated in the executable below; no old sandbox/source is needed for this proof.

Theorem and scope: Fix those21 physical points, with homogeneous filled mass. Let a new point be strictly beyond exactly the13 parent facets in PACKET and strictly beneath every other parent facet. This is exactly every one-plane removal of the complete old same-centre polar packet while retaining all other old polar vertices. The entire three-dimensional open insertion cell is nonempty and bounded. Its closure has8 vertices. Throughout it, the new actual-centroid body has V22/E60/F40,C120, and four old vertices 2,12,18,20 are simultaneously strict U in the original lexicographically sorted vertex ordering. Thus U>=4, excluding strict110 over ALL separator orientations and offsets in this fixed-incidence one-cap chart, not merely a fixed direction. This does NOT exclude post-cap nonidentity SPD metrics, motion of old physical vertices, a different visible-facet partition, multiple caps, or other C120 bodies.

Proof method: enumerate every nonsingular triple of the38 exact signed halfspaces with integer determinants and exact all-row feasibility. Boundedness is certified by a strictly positive dependence of four spanning normals (rows0,6,24,32). The visible pyramids give V(p) affine and M(p) quadratic in raw added point p. For an old edge i-j, the instability numerator (W_i V-M).(W_j-W_i) has degree<=2; for an edge to the new point it has degree<=3. The polarizations in blossom() are the exact degree2/3 Bernstein coefficients after pullback from the convex hull of the8 insertion-cell vertices to the standard7-simplex. All996 coefficients for all23 directed incident edges of the four claimed vertices are strictly negative. The nonnegative Bernstein basis therefore proves all required outgoing arrows negative over the whole closed cell. In the open cell all old vertices remain exposed, the same horizon cone yields the same40 maximal triangles and60 true edges, and V>0. The insertion point (3/10,-1/2,-1/2) in the parent-centred frame independently reproduces the volume and first moment from full hull integration.

Recovery and verification: save the EXACT following code as C114_ORIENTATION_PROOF.py and run `python -B -S C114_ORIENTATION_PROOF.py > proof.log` in an empty directory. CPython3.13.5 standard library only; no RNG, floating-point predicate, optimizer, NumPy, SciPy or external input. The diagnostic float printed beside each exact sign is not used in any decision.
Source C114_ORIENTATION_PROOF.py:7029bytes,SHA256 c2a36c7d8769217fb255b6c980ead77fc029e5ebf65c2b307e47d8dc2023cb95.
Reproduced all_orientation_coeffs.json:126450bytes,SHA256 9a6cdbcef26d3d93aecfc6d9c48da0085d7f34f4aeb4c25be70ab812d953b53a.
Reproduced proof.log:1638bytes,SHA256 5b572778d771a34d0f548661de4cc24068df9f18890e07b9fd145b90e9f8bcc9.
Expected final marker: C114_ALL_ORIENTATION_CAP_U_GE_4_EXACT_PASS 8 23 996.

```python
"""Exact C114 parent and fixed-visible-cap chart. CPython 3.13.5.
Geometry authority: literal VL12_DUAL_CANCEL21_G4, figure-0438.
Fractions are exact; NumPy/SciPy routines nominate candidates only.
"""
from fractions import Fraction as F
from itertools import combinations
import json, math, hashlib
RAW={'grid':10000,'points':[[-13513,10001,-9032],[7585,971,-5336],[9215,2535,-2766],[9859,3065,-261],[10414,1455,1511],[10533,-561,2627],[10245,-2747,3309],[9489,-4870,3884],[8292,-6612,4622],[6777,-7643,5870],[4984,-8225,7187],[2841,-8790,8032],[556,-8903,8725],[-1868,-8784,9006],[-4342,-8346,8933],[-6808,-7570,8472],[-9197,-6461,7561],[-11427,-4979,6139],[-13362,-2964,4209],[-14798,-281,1613],[-15515,3415,-2186]]}
PACKET=[0,2,4,9,11,13,14,17,19,20,26,30,32]
def dot(a,b): return sum(x*y for x,y in zip(a,b))
def sub(a,b): return tuple(x-y for x,y in zip(a,b))
def add(a,b): return tuple(x+y for x,y in zip(a,b))
def mul(a,t): return tuple(t*x for x in a)
def cross(a,b): return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def hull(v):
    """All supporting triples, exact maximal faces; rational coplanar grouping."""
    faces={}
    for i,j,k in combinations(range(len(v)),3):
        n=cross(sub(v[j],v[i]),sub(v[k],v[i]))
        if not any(n): continue
        h=dot(n,v[i]); ds=[dot(n,x)-h for x in v]
        if max(ds)>0 and min(ds)<0: continue
        if max(ds)>0: n=mul(n,-1); h=-h; ds=[-x for x in ds]
        ids=tuple(t for t,d in enumerate(ds) if not d)
        if ids in faces: continue
        # Sort around an interior face anchor using rational half-plane ordering.
        from functools import cmp_to_key
        c=tuple(F(sum(v[t][l] for t in ids))/len(ids) for l in range(3))
        e=sub(v[ids[0]],c); f=cross(n,e)
        z={t:(dot(sub(v[t],c),e),dot(sub(v[t],c),f)) for t in ids}
        def cmp(a,b):
            xa,ya=z[a]; xb,yb=z[b]
            ha=int(ya<0 or (ya==0 and xa<0)); hb=int(yb<0 or (yb==0 and xb<0))
            if ha!=hb: return -1 if ha<hb else 1
            d=xa*yb-ya*xb
            return -1 if d>0 else (1 if d<0 else 0)
        cyc=tuple(sorted(ids,key=cmp_to_key(cmp)))
        faces[ids]=(cyc,n,h)
    return [faces[k] for k in sorted(faces)]
def geometry_edges(faces):
    ed={}
    for f,(cyc,n,h) in enumerate(faces):
        for a,b in zip(cyc,cyc[1:]+cyc[:1]): ed.setdefault(tuple(sorted((a,b))),[]).append(f)
    assert all(len(fs)==2 for fs in ed.values())
    return ed
def mass(v,faces):
    V=F(0); M=[F(0)]*3
    for cyc,n,h in faces:
        for j in range(1,len(cyc)-1):
            a,b,c=[v[t] for t in (cyc[0],cyc[j],cyc[j+1])]
            w=F(dot(a,cross(b,c)))/6
            V+=w
            for l in range(3): M[l]+=w*(a[l]+b[l]+c[l])/4
    assert V>0
    return V,tuple(M),tuple(x/V for x in M)
def parent():
    v=sorted(tuple(F(x,RAW['grid']) for x in p) for p in RAW['points'])
    fs=hull(v); V,M,c=mass(v,fs)
    x=[sub(p,c) for p in v]
    qs=[mul(n,1/(h-dot(n,c))) for cyc,n,h in fs]
    return v,x,fs,qs,V,c


def det(a,b,c): return dot(a,cross(b,c))
def get_cell():
    W=sorted(tuple(p) for p in RAW['points']); fs=hull(W)
    rows=[]
    for i,(cyc,n,h) in enumerate(fs):
        # n,h are integral for integer coordinates.
        n=tuple(int(t) for t in n); h=int(h)
        g=math.gcd(*n,h); n=tuple(t//g for t in n); h//=g
        if i in PACKET: n=mul(n,-1); h=-h
        rows.append((n,h))
    vertices={}
    for ii in combinations(range(len(rows)),3):
        A=[rows[i][0] for i in ii]; b=[rows[i][1] for i in ii]
        d=det(*A)
        if not d: continue
        num=tuple(b[0]*cross(A[1],A[2])[j]+b[1]*cross(A[2],A[0])[j]+b[2]*cross(A[0],A[1])[j] for j in range(3))
        if d<0: d=-d; num=mul(num,-1)
        if any(dot(n,num)>h*d for n,h in rows): continue
        v=tuple(F(z,d) for z in num)
        vertices[v]=[i for i,(n,h) in enumerate(rows) if dot(n,num)==h*d]
    # Four normals enclosing0 give an exact recession-cone boundedness certificate.
    bounds=None
    for ii in combinations(range(len(rows)),4):
        ns=[rows[i][0] for i in ii]
        lam=[((-1)**j)*det(*[ns[k] for k in range(4) if k!=j]) for j in range(4)]
        if all(t<0 for t in lam): lam=[-t for t in lam]
        if all(t>0 for t in lam):
            g=math.gcd(*lam);lam=[t//g for t in lam]
            assert all(sum(lam[k]*ns[k][j] for k in range(4))==0 for j in range(3))
            bounds={'rows':ii,'positive_weights':lam}; break
    assert bounds is not None
    return W,fs,rows,vertices,bounds

from itertools import combinations_with_replacement as cwr
from functools import lru_cache

W,fs,rows,vs,bounds=get_cell(); vv=list(sorted(vs))
V0,M0,c0=mass(W,fs)
@lru_cache(None)
def vm(p):
    V=V0; M=list(M0)
    for fi in PACKET:
        cyc,n,h=fs[fi]; assert len(cyc)==3
        w=(dot(n,p)-h)/6
        assert w>=0
        V+=w
        for k in range(3): M[k]+=w*(p[k]+sum(W[i][k] for i in cyc))/4
    assert V>0
    return V,tuple(M)
interior=tuple(F(10000)*a+c0[k] for k,a in enumerate((F(3,10),F(-1,2),F(-1,2))))
assert all(dot(n,interior)<h for n,h in rows)
cf=hull(W+[interior]); ed=geometry_edges(cf)
assert (len(W)+1,len(ed),len(cf))==(22,60,40)
for p in [interior]:
    V,M=vm(p); VE,ME,CE=mass(W+[p],cf); assert V==VE and M==ME

def f(p,i,j):
    V,M=vm(p)
    return dot(sub(mul(W[i],V),M),sub(p if j==21 else W[j],W[i]))
def blossom(i,j,ix):
    if len(ix)==2:
        x,y=[vv[k] for k in ix]
        return 2*f(mul(add(x,y),F(1,2)),i,j)-(f(x,i,j)+f(y,i,j))/2
    x,y,z=[vv[k] for k in ix]
    return (27*f(mul(add(add(x,y),z),F(1,3)),i,j)
            -8*(f(mul(add(x,y),F(1,2)),i,j)+f(mul(add(x,z),F(1,2)),i,j)+f(mul(add(y,z),F(1,2)),i,j))
            +f(x,i,j)+f(y,i,j)+f(z,i,j))/6

out={'object':'VL12_DUAL_CANCEL21_G4_WHOLE_POLAR_PACKET_CAP_ALL_ORIENTATIONS','bounds':bounds,'cell_vertices':[{'Y':[str(t) for t in p],'active':vs[p]} for p in vv],'VEF':[22,60,40],'certificate':[]}
for i in [2,18,12,20]:
    adj=sorted(j if k==i else k for k,j in ed if i in (k,j))
    good=True
    for j in adj:
        degree=3 if j==21 else 2
        coefs=[(ix,blossom(i,j,ix)) for ix in cwr(range(len(vv)),degree)]
        mx=max(t for ix,t in coefs); good=good and mx<0
        print('EXACT_COEF',i,j,degree,len(coefs),'maxsign',(mx>0)-(mx<0),'max',float(mx))
        out['certificate'].append({'i':i,'j':j,'degree':degree,'coefficients':[[list(ix),str(t)] for ix,t in coefs]})
    assert good, ('unproved root',i)
    print('ALL_CELL_STRICT_U',i,good)
jsontext=json.dumps(out,sort_keys=True,separators=(',',':'))+'\n'
open('all_orientation_coeffs.json','w').write(jsontext)
print('EXACT_ORIENTATION_COEFFICIENTS',len(jsontext.encode()),hashlib.sha256(jsontext.encode()).hexdigest())

assert len(vv)==8 and len(out['certificate'])==23
assert sum(len(e['coefficients']) for e in out['certificate'])==996
assert hashlib.sha256(jsontext.encode()).hexdigest()=='9a6cdbcef26d3d93aecfc6d9c48da0085d7f34f4aeb4c25be70ab812d953b53a'
print('C114_ALL_ORIENTATION_CAP_U_GE_4_EXACT_PASS 8 23 996')
```
