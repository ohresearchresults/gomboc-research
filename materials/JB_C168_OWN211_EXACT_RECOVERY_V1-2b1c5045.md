# material-2b1c5045a6ba

AI research material · [Export notes](../catalog/coverage.md#text-records)

---

# JB_C168_OWN211 exact recovery capsule, complete 1/1

This is a new non-target control, not own110 and not a replacement of the accepted own110/C622. Two rational grids of a root-free joint P/Q descent checkpoint have true V30/E84/F56, own strict211, additionalweak000, primitivezero000. The smaller-grid G6 gives an independently reconstructible simpler-arithmetic control. A lower numerical objective checkpoint is exact222 and is preserved as a meaningful nearweak negative control, not mislabelled211.

The literal inputs below and complete exact auditor suffice to reconstruct every reported object and its complete audit, without any originating sandbox. The producing floating method and exact float checkpoints are preserved separately in JB_ROOT_FREE_JOINT_FULLBAR_METHOD_V1; it is not required to reconstruct these literal rational objects. Old HARD_U1_B G8 input identity is f5ee0fa9fd5f39860ff0e85add8c695c4476c8601ea0a623a13de9ada9f41d97 (978 bytes), fully preserved in [internal-source-reference]. Do not identify these new bodies with that old input.

## Reconstruction and verification
Write each labelled code block verbatim to its labelled UTF-8 filename with LF line endings and the displayed final newline. Run:

```sh
python exact_poly.py JB_CONT211_G8.json
python exact_poly.py JB_CONT211_G6.json
python exact_poly.py JB_CONT_BEST_G8.json
```

Only Python standard library is needed for exact auditing; observed Python 3.13.5. The auditor enumerates all point triples and all supporting planes with integer arithmetic, requires each maximal facet to be triangular, computes the filled homogeneous volume and first moment with signed tetrahedra, then exact strict/weak facet/vertex/edge tests and complete P/Q radial merge-tree bars. It is NOT a general non-simplicial auditor: nontriangular supporting faces trigger an assertion, rather than treating triangulation diagonals as edges. The saved new bodies pass the simplicial requirement.

Observed terminal receipts:

```
RATIONAL_GRID_WRITTEN JB_CONT211_G8.json 974 7735223d4eaceea6a2fc71b76e464e10ddffc860c5040bcdb71114aa462bf9e6
EXACT_POLY_AUDIT_PASS JB_CONT211_G8 (30, 84, 56) [2, 1, 1] additionalweak [0, 0, 0] primitivezero [0, 0, 0] P/Qbars 0 1 Qsum 0.6961615601433753
JB_CONT211_G8_AUDIT.json 3778 a0743a98a83b2ac09d7b25d7ccda43402423fa29f33a7b9ef88874055fd59788
RATIONAL_GRID_WRITTEN JB_CONT211_G6.json 792 27c6bcafff1d74ae7d9a3c0a67854aa8dcadfeccf583f6d398d6a5096efee12f
EXACT_POLY_AUDIT_PASS JB_CONT211_G6 (30, 84, 56) [2, 1, 1] additionalweak [0, 0, 0] primitivezero [0, 0, 0] P/Qbars 0 1 Qsum 0.6961620787334448
JB_CONT211_G6_AUDIT.json 3376 84c1e6d01d53ef0fb081cd5437149f5c1cefd279307dfbaeeed21fe90f0ee616
RATIONAL_GRID_WRITTEN JB_CONT_BEST_G8.json 976 62212062036562c396ff9402c4bbe39e5264703ef7a2179eca22d6e77d4cf395
EXACT_POLY_AUDIT_PASS JB_CONT_BEST_G8 (30, 84, 56) [2, 2, 2] additionalweak [0, 0, 0] primitivezero [0, 0, 0] P/Qbars 1 1 Qsum 0.69326221606963
JB_CONT_BEST_G8_AUDIT.json 4387 6f3bd83dfd7d456c5b18e4bcc793aa432604d11a9209eae4b4aeb6f6c58fca18
```

Observed source exact_poly.py: 6134 bytes, SHA256 898f77989193886996d6f2dc121ccdfdf611b8a9ac52fd3207557eac6a69c0c4. Do not substitute other historical summary hashes of same-named files.

For the two211 bodies, exact sorted-hull facet IDs S=[38,49], U=[29], H=[[22,29]], no P bars. Their sole Q bar has peak49, elder38, component [7,8,14,15,16,17,21,24,31,34,43,47,48,49,50,51,52,53], cut [[6,7],[2,8],[5,7],[9,15],[10,14],[18,21],[16,22],[23,24],[30,31],[24,33],[30,34],[43,44],[46,48],[42,52],[46,53],[52,54],[44,47],[45,49],[50,55],[51,55]], attainingedge [52,54], path [49,50,51,48,53,52,54,39,40,41,38]. Thus Q18/cut20 remains genuinely deep: this is not elimination of the stable basin.
G6 volume=598837605749458451/500000000000000000; centroid=[98161798173374904343729/14372102537987002824000000,58625756662250763283/191628033839826704320000,-43165262138901783949541/14372102537987002824000000].
G8 volume=2395349498881686954587581/2000000000000000000000000; centroid=[3272015538545086599813797359579/479069899776337390917516200000000,879411175331002890567549039359/2874419398658024345505097200000000,-2877817284671092970378349013291/958139799552674781835032400000000].
G8 depth exact=12416444543411792820309665349317989820987085159872588238553971114573196973684742016200449567154515057453751523553/17835579058479776053057868187482665383282092346119398303109791451629895265947143451233916395232865919788734069898.
The222 control has S=[33,48],U=[12,29],H=[[7,12],[22,29]], extra P1/cut11 depth1.2092062988384298e-10. Its sole Q18/cut20 depth .69326221606963 does not justify dropping that positive primal bar.

## exact_poly.py
```python
"""Exact rational audit of a simplicial rational convex 3-polyhedron.
All maximal faces are enumerated; nontriangular faces are explicitly rejected.
Centroid is the actual filled homogeneous volume centroid, never a nominated point.
"""
from itertools import combinations
from functools import reduce
from math import gcd
from fractions import Fraction as F
from pathlib import Path
import json,sys,hashlib
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def neg(a):return tuple(-x for x in a)
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def primitive(a,b):
    g=reduce(gcd,(abs(x) for x in (*a,b)),0)
    assert g
    return tuple(x//g for x in a),b//g

def exact_hull(raw):
    allp=sorted(set(map(tuple,raw['points'])));supports={}
    for i,j,k in combinations(range(len(allp)),3):
        n=cross(sub(allp[j],allp[i]),sub(allp[k],allp[i]))
        if not any(n):continue
        h=dot(n,allp[i]);ds=[dot(n,p)-h for p in allp]
        if min(ds)<0<max(ds):continue
        if max(ds)>0:n=neg(n);h=-h;ds=[-v for v in ds]
        if min(ds)==0:continue
        ids=tuple(i for i,d in enumerate(ds) if d==0)
        # Exact source is simplicial; reject all nontriangular facet cases.
        assert len(ids)==3
        supports[ids]=primitive(n,h)
    ids=sorted(set(i for f in supports for i in f));mp={i:j for j,i in enumerate(ids)}
    p=[allp[i] for i in ids];facets=[]
    for f,(n,h) in supports.items():
        f=sorted(mp[i] for i in f)
        if dot(cross(sub(p[f[1]],p[f[0]]),sub(p[f[2]],p[f[0]])),n)<0:f[1],f[2]=f[2],f[1]
        facets.append((f,n,h))
    facets.sort(key=lambda f:sorted(f[0]));edges={}
    for k,(f,n,h) in enumerate(facets):
        assert all(dot(n,v)<=h for v in allp)
        for a,b in zip(f,f[1:]+f[:1]):edges.setdefault(tuple(sorted((a,b))),[]).append(k)
    assert all(len(v)==2 for v in edges.values())
    assert len(p)-len(edges)+len(facets)==2
    return p,facets,edges

def radial(X,edges):
    R=[dot(x,x) for x in X];events=[]
    for a,b in edges:
        d=sub(X[b],X[a]);den=dot(d,d)
        if den==0:t=F(0)
        else:t=max(F(0),min(F(1),F(-dot(X[a],d),den)))
        p=tuple(X[a][i]+t*d[i] for i in range(3));events.append((dot(p,p),a,b))
    pa=list(range(len(X)));peak=pa[:];members=[{i} for i in pa];bars=[];tree=[[] for _ in X]
    def find(i):
        while pa[i]!=i:pa[i]=pa[pa[i]];i=pa[i]
        return i
    for h,a,b in sorted(events,key=lambda e:(-e[0],e[1],e[2])):
        u,v=find(a),find(b)
        if u==v:continue
        if (R[peak[u]],peak[u])<(R[peak[v]],peak[v]):u,v=v,u
        tree[a].append(b);tree[b].append(a)
        birth=R[peak[v]]
        if birth>h:
            group=members[v].copy();r=peak[v];elder=peak[u];seen={r:None};todo=[r]
            for j in todo:
                if j==elder:break
                for k in tree[j]:
                    if k not in seen:seen[k]=j;todo.append(k)
            path=[elder]
            while path[-1]!=r:path.append(seen[path[-1]])
            path.reverse();depth=(birth-h)/birth
            bars.append(dict(peak=r,elder=elder,birth=str(birth),death=str(h),depth=str(depth),depth_float=float(depth),component=sorted(group),cut=[list(e) for e in edges if (e[0] in group)!=(e[1] in group)],attaining_edge=[a,b],attaining_path=path))
        pa[v]=u;members[u]|=members[v]
    return bars

def audit(raw):
    I,facets,E=exact_hull(raw);D=raw['denominator'];W=0;M=[0,0,0]
    for f,n,h in facets:
        a,b,c=[I[i] for i in f];d=dot(a,cross(b,c));W+=d
        for k in range(3):M[k]+=d*(a[k]+b[k]+c[k])
    assert W>0;Y=[tuple(4*W*v[k]-M[k] for k in range(3)) for v in I]
    nb=[set() for _ in I]
    for a,b in E:nb[a].add(b);nb[b].add(a)
    S=[];SW=[];U=[];UW=[];H=[];HW=[];zero=[0,0,0];Q=[]
    for k,(f,n,h) in enumerate(facets):
        height=dot(n,Y[f[0]]);assert height>0;Q.append(tuple(F(x,height) for x in n))
        g=[dot(cross(n,sub(I[j],I[i])),neg(Y[i])) for i,j in zip(f,f[1:]+f[:1])]
        zero[0]+=sum(v==0 for v in g)
        if min(g)>0:S.append(k)
        if min(g)>=0:SW.append(k)
    for i in range(len(I)):
        g=[dot(Y[i],sub(I[j],I[i])) for j in sorted(nb[i])];zero[1]+=sum(v==0 for v in g)
        if max(g)<0:U.append(i)
        if max(g)<=0:UW.append(i)
    for (i,j),(a,b) in sorted(E.items()):
        d=sub(Y[j],Y[i]);L=dot(d,d);T=-dot(Y[i],d);qn=tuple(Y[i][k]*L+T*d[k] for k in range(3));n=facets[a][1];m=facets[b][1]
        A=dot(n,n);B=dot(n,m);C=dot(m,m);det=A*C-B*B;assert det>0
        aa=C*dot(qn,n)-B*dot(qn,m);bb=A*dot(qn,m)-B*dot(qn,n)
        assert tuple(q*det for q in qn)==tuple(aa*n[k]+bb*m[k] for k in range(3))
        g=[T,L-T,aa,bb];zero[2]+=sum(v==0 for v in g)
        if min(g)>0:H.append([i,j])
        if min(g)>=0:HW.append([i,j])
    strict=list(map(len,[S,U,H]));weak=list(map(len,[SW,UW,HW]));additional=[a-b for a,b in zip(weak,strict)]
    if additional==[0,0,0]:assert strict[0]+strict[1]-strict[2]==2
    pb=radial([tuple(F(y) for y in v) for v in Y],sorted(E));qb=radial(Q,[tuple(v) for k,v in sorted(E.items())])
    return dict(name=raw.get('name','UNNAMED'),V=len(I),E=len(E),F=len(facets),C=2*len(E),denominator=D,points=I,volume=str(F(W,6*D**3)),centroid=[str(F(m,4*W*D)) for m in M],first_moment=[str(F(m,24*D**4)) for m in M],strict=strict,weak=weak,additional_weak=additional,primitive_zero=zero,S=S,U=U,H=H,faces=[f for f,n,h in facets],edges=[list(k) for k in sorted(E)],P_bars=pb,Q_bars=qb)

def main():
    p=Path(sys.argv[1]);raw=p.read_bytes();x=json.loads(raw);out=audit(x);out['input_sha256']=hashlib.sha256(raw).hexdigest();s=json.dumps(out,sort_keys=True,separators=(',',':'))+'\n';target=p.with_name(p.stem+'_AUDIT.json');target.write_text(s)
    print('EXACT_POLY_AUDIT_PASS',out['name'],(out['V'],out['E'],out['F']),out['strict'],'additionalweak',out['additional_weak'],'primitivezero',out['primitive_zero'],'P/Qbars',len(out['P_bars']),len(out['Q_bars']),'Qsum',sum(v['depth_float'] for v in out['Q_bars']))
    print(target.name,len(s.encode()),hashlib.sha256(s.encode()).hexdigest())
if __name__=='__main__':main()
```

## JB_CONT211_G8.json
```json
{"denominator":100000000,"name":"JB_CONT211_G8","points":[[-96784188,-5465233,3473178],[-95888680,-8644825,25969368],[-92317079,-2238270,-18997666],[-92271552,761055,42877205],[-93642497,-24194977,12199322],[-88326021,-36606313,-1405446],[-85016851,10875539,58341032],[-80629413,-3708123,-41463023],[-80389851,-45473912,-16065236],[-60238309,6016184,-60942495],[-74137481,19789793,72634027],[-69002492,-52568678,-30057533],[-61164595,-13140693,-59581154],[-59604126,26887621,85685591],[-53135394,-59118624,-41150796],[-41413645,32533046,96731754],[-33011520,10458323,-72816535],[-6964651,-70037365,-19009461],[-38574783,-56015313,-54722971],[-19721609,38463781,104181003],[-22415662,-47066819,-66600592],[1041320,-53037771,-61153375],[10922041,-60854326,-40058856],[6187381,44584240,107013969],[1543434,-29254518,-73346667],[37020008,50890914,102829555],[61520767,18076131,-45079257],[67950336,55901002,89563603],[92905254,58521833,69327266],[146700365,60253902,-3041979]]}
```

## JB_CONT211_G6.json
```json
{"denominator":1000000,"name":"JB_CONT211_G6","points":[[-967842,-54652,34732],[-958887,-86448,259694],[-923171,-22383,-189977],[-922716,7611,428772],[-936425,-241950,121993],[-883260,-366063,-14054],[-850169,108755,583410],[-806294,-37081,-414630],[-803899,-454739,-160652],[-602383,60162,-609425],[-741375,197898,726340],[-690025,-525687,-300575],[-611646,-131407,-595812],[-596041,268876,856856],[-531354,-591186,-411508],[-414136,325330,967318],[-330115,104583,-728165],[-69647,-700374,-190095],[-385748,-560153,-547230],[-197216,384638,1041810],[-224157,-470668,-666006],[10413,-530378,-611534],[109220,-608543,-400589],[61874,445842,1070140],[15434,-292545,-733467],[370200,508909,1028296],[615208,180761,-450793],[679503,559010,895636],[929053,585218,693273],[1467004,602539,-30420]]}
```

## JB_CONT_BEST_G8.json
```json
{"denominator":100000000,"name":"JB_CONT_BEST_G8","points":[[-96833671,-5623789,3519012],[-95844645,-8777708,26045260],[-92367303,-2147049,-18909518],[-92228279,732534,42883220],[-93619894,-24316505,12146650],[-88331880,-36622219,-1442607],[-85012828,10926816,58368636],[-80738091,-3867110,-41528206],[-80425456,-45436060,-16144217],[-60171813,6204769,-61048241],[-74135518,19820566,72632801],[-69055162,-52489216,-30154255],[-60916594,-13104440,-59659222],[-59588953,26917307,85678516],[-53171819,-59142766,-41164999],[-41426458,32578804,96742308],[-32954913,10228192,-72749163],[-6844908,-69976609,-18492733],[-38678829,-56015453,-54794296],[-19755040,38445601,104181626],[-22306088,-47259613,-66603971],[1024994,-52876241,-60826808],[10920821,-60540735,-40016922],[6121933,44588725,107005682],[1507192,-29136833,-73192496],[37337268,50883292,102822972],[61785688,18152339,-44869146],[68242227,55879908,89445852],[92790354,58528032,69447378],[146601123,60232816,-3122819]]}
```
