# material-f6a002abedea

AI research material · [Export notes](../catalog/coverage.md#text-records)

---

# Recovery capsule part 2/2: G6_DEPTH5_ESCAPE_MASS_OBSTRUCTION

Required part1: [internal-source-reference], SHA256 1768033b4a72517d687b46bda0f861425a7cbf504fc72ac28a6f1cd2aef2455e,10263bytes. Both parts together supply all literal inputs, complete runnable producer/checker, proof, parameters and identities. No originating sandbox is required. This is a restricted-family mass obstruction, not a new own110 construction.

## Exact source-identity correction to part1 and reconstruction
The BUILD_DEPTH5.py block in part1 has an algebraically identical two-line floating diagnostic in place of the one-line original diagnostic. Its actual extracted identity is2814bytes,SHA256 adb2f96bd14ef2a60dcca0881a4d0659d4097405b17476f990e11abfad18c75a, not the canonical source hash quoted in part1. This does not change any generated geometry, but byte identity must be corrected explicitly. After extracting G6.json without final newline and BUILD_DEPTH5.py with one final LF, execute this COMPLETE exact patch. It replaces only the diagnostic; afterward the canonical2814byte source has precisely the hash in the part1 manifest. This correction supersedes part1's omission of the patch step.

```python
from pathlib import Path
from hashlib import sha256
p=Path('BUILD_DEPTH5.py')
b=p.read_bytes()
assert len(b)==2814
assert sha256(b).hexdigest()=='adb2f96bd14ef2a60dcca0881a4d0659d4097405b17476f990e11abfad18c75a'
old=b"w=np.einsum('i,ij->j',np.einsum('ij,ij->i',t[:,0],np.cross(t[:,1],t[:,2])),t.sum(axis=1))/24\nmom=w\n"
new=b"w=np.einsum('ij,ij->i',t[:,0],np.cross(t[:,1],t[:,2]));mom=np.einsum('i,ij->j',w,t.sum(axis=1))/24\n"
assert b.count(old)==1
b=b.replace(old,new)
assert len(b)==2814
assert sha256(b).hexdigest()=='01fde8323e7efc2440dd862f2db43392699866ddf3be209998dafd719d094bfb'
p.write_bytes(b)
```

Write VERIFY_DEPTH5.py from its complete block below with one final LF,11793bytes,SHA256 5f99e7a6b74049111e12a091eeb056d42d9e627caf01498095d43dbdbe28e734. All three canonical recovery inputs are then exactly those cold-replayed. Run OPENBLAS_NUM_THREADS=1 python BUILD_DEPTH5.py 14, followed by python -B -S VERIFY_DEPTH5.py. No source or parameter is omitted.

Observed output identities: DEPTH5_K14_CANONICAL.json131094bytes,SHA256 f939e6df7fa195e13ff102a386c437cef0fe9fceef8d192a559f2113253aa31d; DEPTH5_PROOF.json7469bytes,SHA256 6c20b7c64119bea8951be862d7b588d5db5fec702d6410036653b0059de6005f.
Observed terminal: G6_DEPTH5_NEW_FACET_ESCAPE_MASS_OBSTRUCTION_PASS 2353 84 197652.
The result is the exact inequality integral_L(200*x+52*y-61*z)dV<-1/100 for all P5 subset L subset G6, and the consequent requirement of at least six new active facets in a polar escape path when an origin-centered subbody retains an inherited unique strict stable facet. It does not exclude replacing that root or a deeper<=21-cut construction.

## File: VERIFY_DEPTH5.py
```python
"""Exact five-generation polar-escape/filled-mass obstruction for literal G6.
Standard library only.  Nominated faces are verified, maximally merged and
closed before integration.  Integer-grid mass is independently recomputed
using a strictly interior anchor.  No floating operation occurs in this file.
"""
from fractions import Fraction as F
from collections import defaultdict,Counter
from pathlib import Path
from itertools import combinations,product
import json,hashlib,math,sys
sys.set_int_max_str_digits(0)
Z=F(0)
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def add(a,b):return tuple(x+y for x,y in zip(a,b))
def mul(t,a):return tuple(t*x for x in a)
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def det(a,b,c):return dot(a,cross(b,c))
def enc(o):return json.dumps(o,sort_keys=True,separators=(',',':'),default=str).encode()
def identity(b):return dict(bytes=len(b),sha256=hashlib.sha256(b).hexdigest())

def cycle(points,n):
    points=sorted(set(points));drop=max(range(3),key=lambda i:abs(n[i]));axes=[i for i in range(3) if i!=drop]
    def xy(p):return (p[axes[0]],p[axes[1]])
    def turn(a,b,c):
        a,b,c=xy(a),xy(b),xy(c)
        return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])
    ordered=sorted(points,key=xy);lo=[];hi=[]
    for p in ordered:
        while len(lo)>1 and turn(lo[-2],lo[-1],p)<=0:lo.pop()
        lo.append(p)
    for p in reversed(ordered):
        while len(hi)>1 and turn(hi[-2],hi[-1],p)<=0:hi.pop()
        hi.append(p)
    out=lo[:-1]+hi[:-1]
    if len(out)<3:return ()
    if dot(cross(sub(out[1],out[0]),sub(out[2],out[0])),n)<0:out.reverse()
    j=out.index(min(out));return tuple(out[j:]+out[:j])

def closed_complex(faces):
    """Faces have already been proved maximal supporting polygons."""
    points=sorted({p for n,h,pp in faces for p in pp});where={p:i for i,p in enumerate(points)}
    rows=[];edges=defaultdict(list);nbr=defaultdict(set);links=defaultdict(lambda:defaultdict(set))
    for k,(n,h,pp) in enumerate(faces):
        row=[where[p] for p in pp];rows.append(row)
        for t,v in enumerate(row):
            a=row[t-1];b=row[(t+1)%len(row)]
            edges[tuple(sorted((v,b)))].append((k,v,b));nbr[v].add(b);nbr[b].add(v)
            links[v][a].add(b);links[v][b].add(a)
    for e,inc in edges.items():assert len(inc)==2 and inc[0][1:]==tuple(reversed(inc[1][1:]))
    assert len(points)-len(edges)+len(rows)==2
    def connected(graph):
        start=next(iter(graph));seen={start};todo=[start]
        while todo:
            for j in graph[todo.pop()]-seen:seen.add(j);todo.append(j)
        return seen==set(graph)
    assert connected(nbr)
    for link in links.values():assert all(len(s)==2 for s in link.values()) and connected(link)
    return points,dict(V=len(points),E=len(edges),F=len(faces),face_histogram=dict(sorted(Counter(map(len,rows)).items())))

def integer_hull(raw,nominations):
    ip=[tuple(x) for x in raw['points']];N=len(ip);S=tuple(sum(x[k] for x in ip) for k in range(3));keys=set()
    for tri in nominations:
        a,b,c=[ip[i] for i in tri];n=cross(sub(b,a),sub(c,a));h=dot(n,a)
        assert n!=(0,0,0)
        sign=dot(n,S)-N*h;assert sign!=0
        if sign>0:n=mul(-1,n);h=-h
        g=math.gcd(*n,h);keys.add(tuple(x//g for x in (*n,h)))
    faces=[]
    for key in sorted(keys):
        n,h=key[:3],key[3];on=[]
        for p in ip:
            d=dot(n,p)-h;assert d<=0
            if d==0:on.append(p)
        pp=cycle(on,n);assert len(pp)>=3
        faces.append((n,h,pp))
    points,info=closed_complex(faces)
    # A closed connected supporting shell with exact convex maximal polygons
    # covers the entire boundary of the full-dimensional input convex hull.
    return faces,points,info,sorted(keys)

def integer_mass(faces,points,grid,origin_inside=False):
    D=0;M=[0,0,0];positive=negative=zero=0
    N=len(points);S=tuple(sum(x[k] for x in points) for k in range(3));DA=0;MA=[0,0,0];apos=0
    for n,h,pp in faces:
        for i in range(1,len(pp)-1):
            a,b,c=pp[0],pp[i],pp[i+1];d=det(a,b,c)
            if d>0:positive+=1
            elif d<0:negative+=1
            else:zero+=1
            if origin_inside:assert d>=0
            D+=d
            for k in range(3):M[k]+=d*(a[k]+b[k]+c[k])
            aa=sub(mul(N,a),S);bb=sub(mul(N,b),S);cc=sub(mul(N,c),S);da=det(aa,bb,cc)
            assert da>0;DA+=da;apos+=1
            for k in range(3):MA[k]+=da*(S[k]+N*(a[k]+b[k]+c[k]))
    v=F(D,6*grid**3);m=tuple(F(x,24*grid**4) for x in M)
    v2=F(DA,6*N**3*grid**3);m2=tuple(F(x,24*N**4*grid**4) for x in MA)
    assert v>0 and (v,m)==(v2,m2)
    return dict(volume=v,first_moment=m,origin_positive=positive,origin_negative=negative,
                origin_zero=zero,interior_positive_tetrahedra=apos,second_anchor_mass_equal=True)

def rational_faces(ifaces,grid):
    return [(n,F(h,grid),tuple(tuple(F(x,grid) for x in p) for p in pp)) for n,h,pp in ifaces]

def clip_positive(faces,U):
    out=[];cap=set()
    for n,h,pp in faces:
        vv=[]
        for a,b in zip(pp,pp[1:]+pp[:1]):
            sa,sb=dot(U,a),dot(U,b)
            if sa>=0:vv.append(a)
            if sa==0:cap.add(a)
            if (sa<0<sb) or (sb<0<sa):
                p=add(a,mul(sa/(sa-sb),sub(b,a)));assert dot(U,p)==0
                vv.append(p);cap.add(p)
        poly=cycle(vv,n)
        if len(poly)>=3:out.append((n,h,poly))
    n=mul(-1,U);poly=cycle(cap,n);assert len(poly)>=3
    out.append((n,Z,poly));return out

def fraction_mass(faces):
    points=sorted({p for n,h,pp in faces for p in pp})
    for n,h,pp in faces:
        assert all(dot(n,p)<=h for p in points)
        assert cycle([p for p in points if dot(n,p)==h],n)==pp
    points,info=closed_complex(faces)
    anchor=tuple(sum(p[k] for p in points)/len(points) for k in range(3))
    def calc(o):
        v=Z;m=[Z,Z,Z];pos=zero=0
        for n,h,pp in faces:
            for i in range(1,len(pp)-1):
                a,b,c=pp[0],pp[i],pp[i+1];w=F(det(sub(a,o),sub(b,o),sub(c,o)),6)
                assert w>=0
                if w:pos+=1
                else:zero+=1
                v+=w
                for k in range(3):m[k]+=w*(o[k]+a[k]+b[k]+c[k])/4
        return v,tuple(m),pos,zero
    v,m,p,z=calc((Z,Z,Z));vv,mm,pp,zz=calc(anchor)
    assert v>0 and (v,m)==(vv,mm) and zz==0
    return info|dict(volume=v,first_moment=m,origin_positive=p,origin_zero=z,
                     interior_positive_tetrahedra=pp,second_anchor_mass_equal=True)

def sixth_root_ceiling(bn,bd,A,limit):
    target=bn*A**6;assert limit**6*bd>=target
    lo,hi=0,limit
    while hi-lo>1:
        mid=(lo+hi)//2
        if mid**6*bd>=target:hi=mid
        else:lo=mid
    assert (hi-1)**6*bd<target<=hi**6*bd
    return hi

def safe_depth5(point,planes,A,limit):
    p2=dot(point,point);roots=0;maxroot=0;minslack=None
    for n,h in planes:
        bn=dot(n,n)*p2;bd=h*h;c=dot(n,point)
        if bn<=bd:continue
        u=sixth_root_ceiling(bn,bd,A,limit);roots+=1;maxroot=max(maxroot,u)
        rhs=h*(32*A**3-48*u*A*A+18*u*u*A-u**3);lhs=c*A**3
        assert lhs<=rhs
        slack=F(rhs-lhs,h*A**3);minslack=slack if minslack is None else min(minslack,slack)
    return roots,maxroot,minslack

def controls():
    raw=dict(grid=1,points=[list(v) for v in product([-1,1],repeat=3)]);tr=[];p=raw['points']
    for t in combinations(range(8),3):
        a,b,c=[p[i] for i in t];n=cross(sub(b,a),sub(c,a));h=dot(n,a)
        if n==(0,0,0):continue
        vv=[dot(n,x)-h for x in p]
        if max(vv)<=0 or min(vv)>=0:tr.append(t)
    ff,pp,info,kk=integer_hull(raw,tr);mm=integer_mass(ff,pp,1,True)
    assert (info['V'],info['E'],info['F'])==(8,12,6)
    assert mm['volume']==8 and mm['first_moment']==(0,0,0)
    mm=fraction_mass(clip_positive(rational_faces(ff,1),(1,0,0)))
    assert mm['volume']==4 and mm['first_moment']==(2,0,0)
    # The clockwise nomination of any valid triangle must still recover the
    # same outward maximal polygon rather than negate the physical mass.
    f2,p2,i2,k2=integer_hull(raw,[tuple(reversed(t)) for t in tr])
    assert k2==kk and integer_mass(f2,p2,1,True)==integer_mass(ff,pp,1,True)
    return 'cube, clipped half-cube and reversed nominations passed'

def main():
    gb=Path('G6.json').read_bytes();ib=Path('DEPTH5_K14_CANONICAL.json').read_bytes()
    assert identity(gb)==dict(bytes=1144,sha256='63ead46daff5c7c9cd4344699cbe551a7e92b2a2851703aacfa55eb1621b6aa5')
    assert identity(ib)==dict(bytes=131094,sha256='f939e6df7fa195e13ff102a386c437cef0fe9fceef8d192a559f2113253aa31d')
    raw=json.loads(gb);inner=json.loads(ib);grid=raw['grid'];U=tuple(inner['covector'])
    assert grid==inner['grid']==10**6 and inner['depth']==5 and U==(200,52,-61)
    A,limit=inner['root_scale'],inner['root_limit'];assert A==10**6 and 0<limit and 3*limit<=4*A
    old,op,oi,keys=integer_hull(raw,inner['old_triangles'])
    assert (oi['V'],oi['E'],oi['F'])==(44,126,84) and all(len(pp)==3 for n,h,pp in old)
    assert all(k[3]>0 for k in keys);planes=[(k[:3],k[3]) for k in keys]
    om=integer_mass(old,op,grid,True);assert om['first_moment']!=(0,0,0)
    stable=[];weak=[]
    for i,(n,h) in enumerate(planes):
        vals=[dot(n,n)*k-dot(n,m)*h for j,(m,k) in enumerate(planes) if i!=j]
        if min(vals)>0:stable.append(i)
        elif min(vals)>=0:weak.append(i)
    assert len(stable)==1 and not weak
    ss=stable[0];sn,sh=planes[ss]
    stable_input=[i for i,p in enumerate(raw['points']) if dot(sn,p)==sh]
    assert stable_input==[5,38,44]
    nroot=maxroot=0;slack=None
    for point in inner['points']:
        assert dot(U,point)<=0
        nr,mr,s=safe_depth5(point,planes,A,limit);nroot+=nr;maxroot=max(maxroot,mr)
        if s is not None:slack=s if slack is None else min(slack,s)
        assert all(dot(n,point)<=h for n,h in planes)
    nf,np,ni,nk=integer_hull(inner,inner['nominations']);nm=integer_mass(nf,np,grid)
    pm=fraction_mass(clip_positive(rational_faces(old,grid),U))
    neg=dot(U,nm['first_moment']);pos=dot(U,pm['first_moment']);upper=neg+pos
    assert upper<F(-1,100)
    report=dict(source_G6=identity(gb),compulsory_inner_input=identity(ib),
        covector=U,depth=5,point_count=len(inner['points']),normal_count=len(planes),
        exact_point_normal_checks=len(inner['points'])*len(planes),sixth_root_checks=nroot,
        largest_root_upper_numerator=maxroot,root_scale=A,least_Chebyshev_slack=slack,
        original=oi|om,original_strict_stable_input=stable_input,original_weak_stable_count=len(weak),compulsory_negative=ni|nm,maximal_positive=pm,
        positive_directional_moment=pos,compulsory_directional_moment=neg,
        total_directional_moment_upper=upper,strict_upper_bound='-1/100',
        controls=controls(),
        theorem_scope='Every new active normal has a closed dot-escape chain of at most five links to ANY ORIGINAL normal. Arbitrary number of cuts.',
        conclusion='Any measurable L between this inner body and G6 has integral_L (200*x+52*y-61*z) < -1/100, hence is not centered at the reference origin.',
        S1_consequence='An origin-centered subbody of G6 whose only strict stable facet is inherited must have at least six NEW active facets along a closed dot-escape path before reaching an original normal. This does not exclude replacing the stable root, and does not require absence of weak stable facets.')
    b=enc(report);Path('DEPTH5_PROOF.json').write_bytes(b)
    print(json.dumps(dict(report=identity(b),inner_complex=ni,checks=report['exact_point_normal_checks'],sixth_root_checks=nroot),sort_keys=True))
    print('G6_DEPTH5_NEW_FACET_ESCAPE_MASS_OBSTRUCTION_PASS',len(inner['points']),len(planes),report['exact_point_normal_checks'])
if __name__=='__main__':main()
```
