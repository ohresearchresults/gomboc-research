# material-b197829bdae6

AI research material · [Export notes](../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

# J75 exact recovery source: reference110 is NOT own110

Parent: immutable figure-0566, SHA256 1dd2a815454fdcdf5442f539f13181506b8ecd85c884a433f8061ea92c9f08be, read completely. The reconstructed R22-B7 body is V75/E204/F131, C408, own strict222, weak000. Its geometry admits the two exact interior reference centres below with reference110, weak000 and no primitive zeros. This does not change its own homogeneous class. Stable face53 is its 18-gon and unstable vertex6 is the elder root in the deterministic ordering of this source.

A necessary cut-only mass-removal bound is exact. Let c0 be the original uniform centroid and c the desired centroid of a measurable remaining subset of relative volume 1-v. Its removed material has centroid r=c+(c0-c)/v in K. For every support n.x<=h with n.(c0-c)>0 this requires v>=n.(c0-c)/(h-n.c). At the robust reference centre the maximum is 59025415830779399196860455609672891442360768001109/98513453130444726592326870922584689695803548320159 = approximately0.5991609669049162, attained by facet4 in the exact ordering. This is a necessary bound for this particular target, not a global exclusion of all reference110 centres or all geometry changes.

An exact rational-plane cut nominated by a centroid-constrained numerical cap minimization gives V14/E25/F13, C50, own strict233, weak000, primitivezero000. Retained relative volume approximately0.00022965676568068185. Its own centroid is close to, but is not asserted exactly equal to, the robust nominated target. This is a reproducible nonwinning body, not an advance of canonical C622.

## Environment and recovery
Python3.13.5, NumPy2.3.5, SciPy1.17.0 were used. Save the complete code below as J75_REFERENCE110_CAP233.py with LF endings and a final newline. Run `OPENBLAS_NUM_THREADS=1 python J75_REFERENCE110_CAP233.py`. The same command reconstructs and verifies; no original sandbox, optimizer result file, or decoder is needed. Qhull nominates facets only; integer support checks and the connected oriented closed maximal-facet sphere check establish the hull used for exact rational integration and complete S/U/H guard census. The code checks a second, positive-tetrahedron integration at the cap's own centroid.

Expected terminal marker: J75_REFERENCE110_CAP233_EXACT_PASS.
Source J75_REFERENCE110_CAP233.py:11412 bytes, SHA256 e16788d0d477fef56c4a8ac979d2b201c9691d0f6ee302939f7699209a740b82.
Output J75_PARENT.json:4392 bytes, SHA256 bd11ca3c0700bccd1a99a4cc2171a725c8a5d8acae5f22992b265f1c2797fb59.
Output J75_CAP233.json:2213 bytes, SHA256 0fff649b93f148c88f6120a7ae0bb8d2873cd52bdd2c05196ccb785462a59d1d.
Output J75_EXACT_REPORT.json:4748 bytes, SHA256 63aee978096a8723d10d43a4d884f94b02a5d27e5d7671e2549ddc1dbd3740f5.
The manifest identifies byte content; all required reconstruction bytes appear literally below.

```python
"""J75 self-contained exact construction/census and mass-steering boundary.
Source parent figure-0566 SHA
1dd2a815454fdcdf5442f539f13181506b8ecd85c884a433f8061ea92c9f08be.
Python 3.13.5 / NumPy 2.3.5 / SciPy 1.17.0 used for this receipt.
Run: python J75_REFERENCE110_CAP233.py
No optimizer success is assumed in this exact replay.
"""
"""Complete exact hull/mass/equilibrium helpers, with floating facet nomination only.
All actual geometric support and equilibrium signs use fractions/integers.
The closed connected maximal-facet check rejects incomplete nominations.
"""
from fractions import Fraction as F
from functools import reduce
from math import gcd,lcm
from collections import defaultdict
import json,hashlib
from pathlib import Path
import numpy as np
from scipy.spatial import ConvexHull
Z=(F(0),)*3
def add(a,b):return tuple(x+y for x,y in zip(a,b))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def mul(a,t):return tuple(x*t for x in a)
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def det(a,b,c):return dot(a,cross(b,c))
def polygon(ids,p,n):
    drop=max(range(3),key=lambda k:abs(n[k]));u,v=[k for k in range(3) if k!=drop]
    ids=sorted(ids,key=lambda i:(p[i][u],p[i][v]))
    def turn(i,j,k):return (p[j][u]-p[i][u])*(p[k][v]-p[i][v])-(p[j][v]-p[i][v])*(p[k][u]-p[i][u])
    def half(seq):
        out=[]
        for i in seq:
            while len(out)>1 and turn(out[-2],out[-1],i)<=0:out.pop()
            out.append(i)
        return out
    f=half(ids)[:-1]+half(reversed(ids))[:-1];assert len(f)>=3
    if dot(cross(sub(p[f[1]],p[f[0]]),sub(p[f[2]],p[f[0]])),n)<0:f.reverse()
    k=f.index(min(f));return f[k:]+f[:k]
def hull(points):
    p=list(dict.fromkeys(tuple(F(x) for x in q) for q in points));assert len(p)>=4
    D=lcm(*(x.denominator for q in p for x in q));zz=[tuple(int(x*D) for x in q) for q in p]
    planes=set()
    for i,j,k in ConvexHull(np.array(p,dtype=float)).simplices:
        i,j,k=int(i),int(j),int(k);n=cross(sub(zz[j],zz[i]),sub(zz[k],zz[i]))
        if not any(n):continue
        h=dot(n,zz[i]);ss=[dot(n,q)-h for q in zz]
        if min(ss)<0<max(ss) or min(ss)==max(ss):continue
        a=tuple(n)+(h,)
        if max(ss)>0:a=tuple(-x for x in a)
        gg=reduce(gcd,(abs(x) for x in a),0);planes.add(tuple(x//gg for x in a))
    assert len(planes)>=4
    ff=[]
    for a in sorted(planes):
        assert all(dot(a[:3],q)<=a[3] for q in zz)
        ff.append(polygon([i for i,q in enumerate(zz) if dot(a[:3],q)==a[3]],zz,a[:3]))
    keep=sorted({i for f in ff for i in f});remap={i:j for j,i in enumerate(keep)}
    ff=[[remap[i] for i in f] for f in ff];owners=defaultdict(list);ori=defaultdict(list)
    for fi,f in enumerate(ff):
        for i,j in zip(f,f[1:]+f[:1]):
            e=tuple(sorted((i,j)));owners[e].append(fi);ori[e].append(i<j)
    edges=sorted(owners)
    assert all(len(owners[e])==2 and ori[e][0]!=ori[e][1] for e in edges)
    adj=[[] for _ in ff]
    for e in edges:
        a,b=owners[e];adj[a].append(b);adj[b].append(a)
    reach={0};todo=[0]
    while todo:
        for v in adj[todo.pop()]:
            if v not in reach:reach.add(v);todo.append(v)
    assert len(reach)==len(ff) and len(keep)-len(edges)+len(ff)==2
    return {'points':[p[i] for i in keep],'material':keep,'faces':ff,'edges':edges,'edge_faces':[owners[e] for e in edges]}
def mass(K,o=Z,positive=False):
    p=K['points'];V=F(0);M=Z
    for f in K['faces']:
        for j in range(1,len(f)-1):
            a,b,c=[p[i] for i in (f[0],f[j],f[j+1])];w=det(sub(a,o),sub(b,o),sub(c,o))/6
            if positive:assert w>0
            V+=w;M=add(M,mul(add(add(o,a),add(b,c)),w/4))
    return V,M

def affine_guards(K):
    """Each returned (A,b) has strict-equilibrium sign b-A.dot(c)>0.
    Order S facets, U vertices, H true edges; all guards are linear in centre.
    """
    p=K['points'];ff=K['faces'];edges=K['edges']
    ns=[cross(sub(p[f[1]],p[f[0]]),sub(p[f[2]],p[f[0]])) for f in ff]
    stable=[]
    for f,n in zip(ff,ns):
        stable.append([(mul(cross(n,sub(p[j],p[i])),-1),-dot(cross(n,sub(p[j],p[i])),p[i])) for i,j in zip(f,f[1:]+f[:1])])
    nb=[set() for _ in p]
    for i,j in edges:nb[i].add(j);nb[j].add(i)
    unstable=[[(sub(p[i],p[j]),dot(p[i],sub(p[i],p[j]))) for j in sorted(nb[i])] for i in range(len(p))]
    saddle=[]
    for (i,j),(f,g) in zip(edges,K['edge_faces']):
        d=sub(p[j],p[i]);dd=dot(d,d);a,b=ns[f],ns[g];aa,ab,bb=dot(a,a),dot(a,b),dot(b,b)
        assert aa*bb-ab*ab>0
        # t=(c-p_i).d; R=dd*(p_i-c)+d*t. R dot v = p_i dot w-c dot w.
        v1=sub(mul(a,bb),mul(b,ab));v2=sub(mul(b,aa),mul(a,ab))
        w1=sub(mul(v1,dd),mul(d,dot(d,v1)));w2=sub(mul(v2,dd),mul(d,dot(d,v2)))
        saddle.append([(mul(d,-1),-dot(p[i],d)),(d,dd+dot(p[i],d)),(w1,dot(p[i],w1)),(w2,dot(p[i],w2))])
    return [stable,unstable,saddle]

def census(K,c):
    groups=affine_guards(K);out={'strict':[],'weak':[],'primitive_zero':[],'ids':[],'weak_ids':[]}
    for group in groups:
        strict=[];weak=[];nz=0
        for k,guards in enumerate(group):
            vals=[b-dot(a,c) for a,b in guards];nz+=sum(v==0 for v in vals)
            if min(vals)>0:strict.append(k)
            elif min(vals)>=0:weak.append(k)
        out['strict'].append(len(strict));out['weak'].append(len(weak));out['primitive_zero'].append(nz)
        out['ids'].append(strict);out['weak_ids'].append(weak)
    if out['weak']==[0,0,0]:assert out['strict'][0]+out['strict'][1]-out['strict'][2]==2
    return out

def dump(path,value):
    bb=(json.dumps(value,sort_keys=True,separators=(',',':'),default=str)+'\n').encode()
    Path(path).write_bytes(bb);return {'bytes':len(bb),'sha256':hashlib.sha256(bb).hexdigest()}

"""Literal R22-B7 checkpoint from immutable figure-0566.
Input transport hash: 1dd2a815454fdcdf5442f539f13181506b8ecd85c884a433f8061ea92c9f08be.
No current working memory or historical summary is used for coordinates.
"""
from fractions import Fraction as F
RAW7 = r"""
-11439418,-3850063,266376;-11436586,-2891673,-2078758;-11012478,-2268283,-3884988;-10198402,-1802514,-5565178;-9510348,-6927925,6508810
-9366848,-1548293,-6739759;-8478663,-8202318,8938576;-8378931,-1404158,-7749168;-7644821,-1356105,-8354867;-6450171,-1391943,-9061728
-6145891,2597816,-1494981;-6241984,2345593,36135;-5623246,2386234,828841;-5235324,-1521597,-9552644;-5121264,2359319,1410928
-5260944,3446660,-1971281;-4273979,2164859,2318946;-4290349,293681,4244065;-4147867,1843405,2773686;-4141030,1258405,3392028
-4113528,4422686,-2267736;-3937485,4202473,-812284;-3481009,-1810034,-10014104;-3329731,549552,4149437;-3408971,4159659,315756
-3278652,4707395,-3115791;-2748873,-1958542,-10137900;-2607660,636130,4067037;-2939567,-310459,4675082;-2370803,4875226,-3611610
-2016463,-2134865,-10193873;-2280378,4424803,718191;-1977909,3912817,1432905;-1542658,3702017,1773344;-1264265,-2344367,-10181882
-1187049,4712991,-4311133;-993382,3683080,1885113;-516110,-2582496,-10097209;-443297,4592143,-4372164;-65807,3904189,1768343
-29868,788154,3545525;245829,-2761621,-9946813;160797,561054,3564566;752453,723937,3323126;997862,-2929127,-9726299
876498,1627910,2986509;1262262,4204445,1562564;2405332,4462279,-3190451;1733591,-3083920,-9436565;3076914,-1717501,-8776968
2446935,-3226134,-9078737;3863116,4048136,-959866;3132038,-3356539,-8654079;2958214,4725441,1046972;3302520,-4439629,-8096073
3771261,-3499268,-8165843;3688981,4039304,1282536;4185393,3471690,1378209;4366444,-3628525,-7620150;4155985,-5179565,-6854522
4469579,3135309,1334821;4735947,2790900,1274870;4910575,-3748103,-7021958;4981252,2443667,1199756;5287381,-4753653,-5513321
5388246,-833841,-5916406;5506849,1716087,863424;5948514,952468,446780;5881216,-4223874,-4499633;6297887,159744,-53863
6294597,-3598061,-3572441;6529699,-611856,-601691;6656697,-1384755,-1223312;6554121,-2893685,-2704614;6669225,-2149699,-1922826
"""
PATCH = [0,1,2,3,4,5,6,7,8,9,13,22,26,30,34,37,54,59]
def points():
    rows=[list(map(int,row.split(','))) for row in RAW7.replace('\n',';').split(';') if row.strip()]
    assert len(rows)==75
    p=[tuple(F(x,10**7) for x in row) for row in rows]
    for i in PATCH:
        x,_,z=p[i]
        p[i]=(x,(-F(68526367,100000)-272*x-409*z)/1000,z)
    return p

# Exact nominated centres; all are reference points, not changes to density.
REF_NEAR=(F(27584923,80000000),F(-4647585587,10**10),F(-3406441751,5000000000))
REF_ROBUST=(F(463597809,1250000000),F(-4993524079,10**10),F(-6706652071,10**10))
CAP_LAMBDA=(F(138611483,50000000),F(-5938384297,50000000),F(-561985037,12500000))
def clip_exact(K,lam,c):
    values=[1+dot(sub(p,c),lam) for p in K['points']]
    p=[q for q,s in zip(K['points'],values) if s>=0]
    for i,j in K['edges']:
        if values[i]*values[j]<0:
            p.append(add(K['points'][i],mul(sub(K['points'][j],K['points'][i]),-values[i]/(values[j]-values[i]))))
    return hull(p)
def inside(K,c):
    return all(dot(cross(sub(K['points'][f[1]],K['points'][f[0]]),sub(K['points'][f[2]],K['points'][f[0]])),sub(K['points'][f[0]],c))>0 for f in K['faces'])
def removed_fraction_lower_bound(K,c,c0):
    bounds=[]
    for j,f in enumerate(K['faces']):
        p,q,r=[K['points'][i] for i in f[:3]]
        n=cross(sub(q,p),sub(r,p));den=dot(n,sub(p,c));num=dot(n,sub(c0,c))
        assert den>0
        if num>0:bounds.append((num/den,j))
    return max(bounds)
def main():
    K=hull(points());V,M=mass(K);c0=mul(M,1/V)
    assert (len(K['points']),len(K['edges']),len(K['faces']))==(75,204,131)
    parent_receipt=dump('J75_PARENT.json',{'density':1,'points':K['points']})
    assert parent_receipt['sha256']=='bd11ca3c0700bccd1a99a4cc2171a725c8a5d8acae5f22992b265f1c2797fb59'
    cp=census(K,c0);assert cp['strict']==[2,2,2] and cp['weak']==[0,0,0]
    ref=[]
    for c in (REF_NEAR,REF_ROBUST):
        cr=census(K,c)
        assert inside(K,c) and cr['strict']==[1,1,0] and cr['weak']==cr['primitive_zero']==[0,0,0]
        assert cr['ids']==[[53],[6],[]]
        ref.append({'centre':c,'census':cr})
    lower,j=removed_fraction_lower_bound(K,REF_ROBUST,c0)
    assert lower==F(59025415830779399196860455609672891442360768001109,98513453130444726592326870922584689695803548320159)
    L=clip_exact(K,CAP_LAMBDA,REF_ROBUST);v,m=mass(L);c=mul(m,1/v)
    assert (len(L['points']),len(L['edges']),len(L['faces']))==(14,25,13)
    cap=census(L,c);assert cap['strict']==[2,3,3] and cap['weak']==cap['primitive_zero']==[0,0,0]
    assert inside(L,c)
    # A second mass sum at the interior centroid must have all positive tetrahedra.
    vv,mm=mass(L,c,positive=True);assert vv==v and mm==m
    cap_receipt=dump('J75_CAP233.json',L['points'])
    out={'parent_size':[75,204,131],'parent_census':cp,'parent_centroid':c0,'reference_centres':ref,
         'removed_fraction_lower_bound':lower,'bound_face':j,'bound_face_vertices':K['faces'][j],
         'cap_lambda':CAP_LAMBDA,'cap_size':[14,25,13],'cap_census':cap,'cap_centroid':c,
         'cap_volume_fraction':v/V,'parent_receipt':parent_receipt,'cap_receipt':cap_receipt}
    receipt=dump('J75_EXACT_REPORT.json',out)
    print('J75_REFERENCE110_CAP233_EXACT_PASS')
    print(json.dumps({'report':receipt,'parent':parent_receipt,'cap':cap_receipt,'removed_fraction':float(lower),'cap_fraction':float(v/V)},sort_keys=True))
if __name__=='__main__':main()
```
