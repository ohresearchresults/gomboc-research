# material-8edc6e4e0fc5

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

Public derivative: internal-record-identifiers-replaced.

---

# RAW_HEX6_ALL_ROOT_PHYSICAL5_EXACT_CENSUS_V1

## Accepted scope
An executed exact rational census on ONE NEW rational homogeneous actual-centroid E17 body proves that every weak-U1 component, at every root, must reach a rank-two weak rooted metric. It excludes ALL singular-disconnected components, not rank-two-connected components and not the entire body. No proper110 attainer or global bound improvement results.

The body identity is RAW_TRANSLATED_HEX6_1over5_24over25_49over50_2over9_99over100_V1. It uses the literal changed six-pole raw source model in fully read parent minimum-0218, but is translated by its NEW ACTUAL uniform centroid. It is NOT the fixed-pole star-centred algebraic atlas member for the same fractions. Exact source cuts are (1/5,24/25,49/50,2/9,99/100). The source below includes every coordinate parameter, all true faces/edges, the positive apex integration fan, and exact centroid calculation.

The implication from this finite census to exclusion of singular-disconnected components is the complete analytic theorem FULL_COMPONENT_FIVE_PHYSICAL_WEAK_CONTACTS_V1 in [internal-source-reference], SHA256 3d9a495f54852bbaab9d638b687296cb0d01373bf1c0d62f30e1a6d5d57e89d3. In brief, a vertex of the convex hull of any such component determines an SPD ray by five independent zero arrows at five genuine weak-unstable source vertices. Thus every selected source must have all its outgoing arrows nonpositive. The code enumerates every five-source/one-neighbor choice, rejects directed cycles and rows confined to one facet, computes the exact null ray by fraction-free elimination, tests SPD by exact Sylvester minors, and tests ALL true outgoing arrows. A surviving metric with only one strict U would be necessary. None exists.

## Exact terminal result, counts refer to contact sets, not distinct rays
All roots together: 106596 selections; 35370 directed-cycle rejections; 196 single-facet rejections; 0 deficient-rank remaining row sets; 69598 non-SPD rays; 1432 SPD rays. Of the SPD rays, 1302 fail the five-PHYSICAL-source test. The remaining130 all have at least two strict U:72 selections have two,58 have three. There are0 weak-U1 candidates.
Candidate sign digest: 0a28fccca8065695ff0a839324ba4e636a3f59d76aebb98305132cc1f2fab7b3.
Root0-only supplementary execution:36288 selections;11433 cycles;196 single-facet;0 rank-deficient;23433 non-SPD;1226 SPD;1123 fail physical test;103 pass, with57 having two strict U and46 having three. Again0 weak-U1.

Every decisive test uses Python integers/Fraction, with no floating-point operation. Geometry checks prove true coplanarity, strict supporting inequalities for nonincident vertices, strict convexity of every face cycle, edge incidence twice, three-connectivity, positive fan volumes and exact recomputed volume centroid0. Every computed null vector is checked against all five original integer rows. The census does not assume generic rank or ignore deficient-rank shape strata.

## Recovery and verification
Save the complete fenced source below as physical5_exact.py with LF line endings and a final newline. Python3.13.5 standard library was used; source supports Python>=3.10 and has no external packages.

Recovery command:

    python physical5_exact.py --output physical5_exact_allroots.json

Verification command (after recovery):

    python -c "import hashlib,json,pathlib; p=pathlib.Path('physical5_exact_allroots.json'); b=p.read_bytes(); r=json.loads(b); assert len(b)==14248; assert hashlib.sha256(b).hexdigest()=='8c25c12ddbef7de4d38445e5f9d96cb3c984f820ab0b84d566934928a5a5335a'; assert r['stats_contact_sets_not_distinct_rays']['weak_u1']==0; assert r['stats_contact_sets_not_distinct_rays']['all_contact_sets']==106596; print('PHYSICAL5_RECOVERY_VERIFIED')"

Expected execution terminal marker: PHYSICAL5_EXACT_CENSUS_OK.
Expected verification marker: PHYSICAL5_RECOVERY_VERIFIED.
Input source physical5_exact.py:9754 bytes,SHA256 c9df71b21def0b88df21bd3e48bb035a12e63a329aeaae52e9ecb36bf3a525c3.
Output physical5_exact_allroots.json:14248 bytes,SHA256 8c25c12ddbef7de4d38445e5f9d96cb3c984f820ab0b84d566934928a5a5335a.
Supplementary command: python physical5_exact.py --root 0 --output physical5_exact_root0.json.
Supplementary output:14244 bytes,SHA256 80b46a629b832c6aba98c4f515f0fa2cc6537307b3445c7c338942f17850389b.
The outputs contain all exact rational vertex and polar coordinates; the deterministic generator is the compact preservation of those complete arrays.

## Complete source: physical5_exact.py
```python
#!/usr/bin/env python3
"""Exact finite physical-contact census on ONE NEW rational actual E17 body.
No floating-point operation enters a decisive comparison.
Output does NOT exclude components reaching rank-two metrics.
Python >=3.10, standard library only.
"""
from fractions import Fraction as F
from functools import reduce
import hashlib, itertools, json, math, sys, time

FACES=((0,4,6,5),(0,5,7,1),(0,1,2),(0,2,8),(0,8,9,3),(0,3,4),(4,3,9,2,1,7,6),(5,6,7),(9,8,2))
EDGES=((0,1),(0,2),(0,3),(0,4),(0,5),(0,8),(1,2),(1,7),(2,8),(2,9),(3,4),(3,9),(4,6),(5,6),(5,7),(6,7),(8,9))
DIRECTED=tuple((i,j) for i,j in EDGES for i,j in ((i,j),(j,i)))
NEIGHBORS=tuple(tuple(j for a,j in DIRECTED if a==i) for i in range(10))
FAN=((4,3,9),(4,9,2),(4,2,1),(4,1,7),(4,7,6),(5,6,7),(9,8,2))
CUTS=(F(1,5),F(24,25),F(49,50),F(2,9),F(99,100))
P=tuple(tuple(F(k,100000) for k in r) for r in ((60401,-32565),(80000,-20000),(0,60000),(-80000,80000),(-483861,-325040),(-447814,-355009)))
BASE=(F(2615613,500000),F(816129,250000),F(-3))
APEX=(F(0),F(0),F(1))


def add(a,b): return tuple(x+y for x,y in zip(a,b))
def sub(a,b): return tuple(x-y for x,y in zip(a,b))
def mul(t,a): return tuple(t*x for x in a)
def dot(a,b): return sum(x*y for x,y in zip(a,b))
def cross(a,b): return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def det3(a): return dot(a[0],cross(a[1],a[2]))
def interpolate(a,b,t): return add(a,mul(t,sub(b,a)))

def solve3(a,b):
    d=det3(a)
    assert d
    return tuple(det3(tuple(tuple(b[i] if j==k else a[i][j] for j in range(3)) for i in range(3)))/d for k in range(3))

def fan_moments(Y):
    ds=[det3(tuple(sub(Y[i],Y[0]) for i in t)) for t in FAN]
    assert all(d>0 for d in ds)
    den=sum(ds)
    g=tuple(sum(d*(Y[0][k]+sum(Y[i][k] for i in t)) for d,t in zip(ds,FAN))/(4*den) for k in range(3))
    return den/6,g

def exact_body():
    qs=tuple(p+(F(1),) for p in P)
    B=tuple(solve3((qs[i],qs[(i+1)%6],BASE),(F(1),)*3) for i in range(6))
    x,y,z,u,v=CUTS
    Y=(APEX,B[1],B[2],B[4],B[5],interpolate(B[0],APEX,x),interpolate(B[0],B[5],y),interpolate(B[0],B[1],z),interpolate(B[3],APEX,u),interpolate(B[3],B[4],v))
    V,g=fan_moments(Y)
    X=tuple(sub(y,g) for y in Y)
    V2,g2=fan_moments(X)
    assert V2==V and g2==(0,0,0)
    # This is a NEW translated rational source body, NOT the fixed-pole
    # star-centred algebraic body for the same five fractions.
    return X,V,g

def geometry_checks(X):
    incid={e:0 for e in EDGES}
    qs=[]
    for face in FACES:
        n=cross(sub(X[face[1]],X[face[0]]),sub(X[face[2]],X[face[0]]))
        h=dot(n,X[face[0]])
        assert h
        if h<0: n=mul(-1,n); h=-h
        assert all(dot(n,X[i])==h for i in face)
        assert all(dot(n,X[i])<h for i in range(10) if i not in face)
        turns=[]
        for k,i in enumerate(face):
            j=face[(k+1)%len(face)]; a=face[(k-1)%len(face)]
            e=tuple(sorted((i,j))); assert e in incid; incid[e]+=1
            turns.append(dot(n,cross(sub(X[i],X[a]),sub(X[j],X[i]))))
        assert all(t>0 for t in turns) or all(t<0 for t in turns)
        qs.append(mul(1/h,n))
    assert all(v==2 for v in incid.values())
    assert len(X)-len(EDGES)+len(FACES)==2
    assert len(set(X))==10
    # Verify three-connectivity of the claimed spherical face graph.
    for removed in itertools.combinations(range(10),2):
        allowed=set(range(10))-set(removed); seen={min(allowed)}
        while True:
            new=seen|{j for i in seen for j in NEIGHBORS[i] if j in allowed}
            if new==seen: break
            seen=new
        assert seen==allowed
    return tuple(qs)

def integral_row(row):
    den=math.lcm(*(x.denominator for x in row))
    v=[int(x*den) for x in row]
    g=math.gcd(*v)
    assert g>0
    return tuple(x//g for x in v)

def arrow_rows(X):
    ans=[]
    for i,j in DIRECTED:
        a=X[i]; e=sub(X[j],a)
        ans.append(integral_row((a[0]*e[0],a[1]*e[1],a[2]*e[2],a[0]*e[1]+a[1]*e[0],a[0]*e[2]+a[2]*e[0],a[1]*e[2]+a[2]*e[1])))
    return tuple(ans)

def exact_null5x6(rows):
    """Fraction-free elimination with row/column pivoting, exact null vector.
    Return None iff rank<5; all divisibility and original row identities checked.
    """
    a=[list(r) for r in rows]; cols=list(range(6)); previous=1
    for k in range(5):
        found=None
        for j in range(k,6):
            for i in range(k,5):
                if a[i][j]: found=(i,j); break
            if found: break
        if found is None: return None
        i,j=found
        if i!=k: a[k],a[i]=a[i],a[k]
        if j!=k:
            for row in a: row[k],row[j]=row[j],row[k]
            cols[k],cols[j]=cols[j],cols[k]
        pivot=a[k][k]
        for i in range(k+1,5):
            aik=a[i][k]
            for j in range(k+1,6):
                num=pivot*a[i][j]-aik*a[k][j]
                q,r=divmod(num,previous); assert r==0
                a[i][j]=q
            a[i][k]=0
        previous=pivot
    v=[0]*6; v[5]=a[4][4]
    for i in range(4,-1,-1):
        num=-sum(a[i][j]*v[j] for j in range(i+1,6))
        v[i],r=divmod(num,a[i][i]); assert r==0
    out=[0]*6
    for i,j in enumerate(cols): out[j]=v[i]
    gcd=math.gcd(*out); assert gcd
    out=tuple(x//gcd for x in out)
    assert all(dot(row,out)==0 for row in rows)
    return out

def positive_ray(v):
    tr=sum(v[:3])
    if tr==0: return None
    if tr<0: v=tuple(-x for x in v)
    a,b,c,d,e,f=v
    if a<=0 or a*b-d*d<=0: return None
    if a*b*c+2*d*e*f-a*f*f-b*e*e-c*d*d<=0: return None
    return v

def forbidden_cycle(srcs,dsts):
    parent=dict(zip(srcs,dsts))
    for i in srcs:
        seen=set()
        while i in parent:
            if i in seen: return True
            seen.add(i); i=parent[i]
    return False

def census(X,root=None):
    R=arrow_rows(X); index={e:i for i,e in enumerate(DIRECTED)}
    outs=tuple(tuple(k for k,(a,b) in enumerate(DIRECTED) if a==i) for i in range(10))
    allowed=tuple(i for i in range(10) if i!=root)
    stats={k:0 for k in ('all_contact_sets','directed_cycle','single_facet','rank_deficient','non_spd_ray','spd_ray','not_five_physical','five_physical','weak_u1')}
    hist={}; survivors=[]; digest=hashlib.sha256()
    for srcs in itertools.combinations(allowed,5):
        for dsts in itertools.product(*(NEIGHBORS[i] for i in srcs)):
            stats['all_contact_sets']+=1
            if forbidden_cycle(srcs,dsts): stats['directed_cycle']+=1; continue
            es=tuple(zip(srcs,dsts))
            if any(all(i in face and j in face for i,j in es) for face in FACES):
                stats['single_facet']+=1; continue
            ids=tuple(index[e] for e in es)
            v=exact_null5x6(tuple(R[k] for k in ids))
            if v is None: stats['rank_deficient']+=1; continue
            v=positive_ray(v)
            if v is None: stats['non_spd_ray']+=1; continue
            stats['spd_ray']+=1
            ds=tuple(dot(r,v) for r in R)
            assert all(ds[k]==0 for k in ids)
            if any(any(ds[k]>0 for k in outs[i]) for i in srcs):
                stats['not_five_physical']+=1; continue
            stats['five_physical']+=1
            strict_roots=tuple(i for i in range(10) if all(ds[k]<0 for k in outs[i]))
            assert strict_roots  # Strict greatest-radius vertex always exists.
            hist[str(len(strict_roots))]=hist.get(str(len(strict_roots)),0)+1
            sig={'edges':es,'strict_unstable':strict_roots,'outgoing_signs':tuple((d>0)-(d<0) for d in ds)}
            digest.update((json.dumps(sig,separators=(',',':'),sort_keys=True)+'\n').encode())
            if len(strict_roots)==1 and (root is None or strict_roots[0]==root):
                stats['weak_u1']+=1
                survivors.append({**sig,'metric_vector':tuple(str(x) for x in v)})
    assert stats['all_contact_sets']==sum(stats[k] for k in ('directed_cycle','single_facet','rank_deficient','non_spd_ray','spd_ray'))
    assert stats['spd_ray']==stats['not_five_physical']+stats['five_physical']
    return stats,hist,survivors,digest.hexdigest()

def main():
    import argparse
    p=argparse.ArgumentParser(); p.add_argument('--root',type=int,default=-1); p.add_argument('--output',default='/mnt/data/physical5_exact_report.json'); a=p.parse_args()
    root=None if a.root<0 else a.root
    assert root is None or 0<=root<10
    X,V,g=exact_body(); poles=geometry_checks(X)
    stats,hist,survivors,pin=census(X,root)
    report={'theorem':'NO SINGULAR-DISCONNECTED WEAK-U1 COMPONENT ON THIS FIXED BODY' if not survivors else 'PHYSICALLY CRITICAL CANDIDATES REQUIRE FURTHER CENSUS','scope':'All roots' if root is None else 'root '+str(root),'body_identity':'RAW_TRANSLATED_HEX6_1over5_24over25_49over50_2over9_99over100_V1','not_the_fixed_pole_star_body':True,'cuts':tuple(str(x) for x in CUTS),'volume':str(V),'raw_centroid':tuple(str(x) for x in g),'vertices':tuple(tuple(str(z) for z in x) for x in X),'true_poles':tuple(tuple(str(z) for z in q) for q in poles),'faces':FACES,'edges':EDGES,'stats_contact_sets_not_distinct_rays':stats,'strict_U_count_histogram_at_five_physical_candidates':hist,'candidate_sign_digest':pin,'survivors':survivors,'limitations':['No rank-two-connected component excluded.','No proper110 construction or whole E17 exclusion.','This is an exact NEW rational uniformly translated source body, not the fixed-pole algebraic atlas member for these cuts.']}
    blob=(json.dumps(report,sort_keys=True,indent=2)+'\n').encode()
    with open(a.output,'wb') as f: f.write(blob)
    print(json.dumps({'stats':stats,'histogram':hist,'candidate_sign_digest':pin,'report_bytes':len(blob),'report_sha256':hashlib.sha256(blob).hexdigest()},sort_keys=True))
    print('PHYSICAL5_EXACT_CENSUS_OK')

if __name__=='__main__': main()
```
