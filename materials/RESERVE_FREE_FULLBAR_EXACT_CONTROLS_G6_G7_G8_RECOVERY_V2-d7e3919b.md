# material-d7e3919b42b5

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

Public derivative: internal-record-identifiers-replaced.

---

# RESERVE_FREE_FULLBAR_EXACT_CONTROLS_G6_G7_G8_RECOVERY_V2

Three distinct exact nonrecord homogeneous convex bodies. NOT own110. All V30/E84/F56,C168, additionalweak000 and primitivezero000. Actual filled-volume-centroid strict counts at grids6/7/8 respectively (8,13,19),(8,10,16),(8,1,7), with P/Q positive-bar counts12/7,9/7,0/7. Relative Q-depth sums .630614358160475,.630614512260678,.6306144899443885. G8 only slightly improves old FREE_FIRST_G8 Qsum.6311139273972071, without cancelling seven stable defects. Coarse grids lose U1 and are retained as arithmetic-fragility controls. No denominator-minimality claim.

## Recovery and verification
Save all four fenced files with exactly one trailing LF. Python3.13.5 standard library only. Run `python exact_poly.py FREE_LIVE_FULLBAR_G6.json` and correspondingly G7/G8. Expected and previously observed terminal marker EXACT_POLY_AUDIT_PASS with the counts above. Complete audit JSON files are regenerated, including exact actual centroid, volume, three first moments, maximal faces, true edges, mixed-edge census, closed-weak tests, and all positive P/Q depths/components/cuts/attaining paths. Nonsimplicial inputs are explicitly rejected rather than silently triangulated into false edges. Euler is a post-check only. P coordinates Y=4WI-M scale physical centred coordinates by4WD; Q=n/(n.Y) has reciprocal scaling. Relative persistence depths and incidence are unchanged by these positive scalings. Equal-height elder choices use the deterministic convention in the source, not a uniqueness theorem.

Producing numerical method is already owned material [internal-source-reference]; its original inputs are [internal-source-reference] and [internal-source-reference]. These numerical inputs are NOT required to recover the three literal rational bodies here. The output/auditor ID [internal-source-reference] used in the earlier brief/method capsule was an erroneous unowned reference. Likewise [internal-source-reference] is not owned. This actual capsule, with the ID returned by its successful store receipt, supersedes those references. No object was canonically advanced to own110.

## UTF-8 manifest
Verify with sha256sum. Source/input files have one trailing newline.
- exact_poly.py6134B SHA898f77989193886996d6f2dc121ccdfdf611b8a9ac52fd3207557eac6a69c0c4
- FREE_LIVE_FULLBAR_G6.json798B SHAa6e8716985d52e681eb7f212877695d9e8e07b8f477753ddebab2d5050660f83
- FREE_LIVE_FULLBAR_G7.json889B SHAf4b80f4b9c67f7ff36d5ee84f48a7cf64cadabeee9d8b320a8c9b9780a674ff1
- FREE_LIVE_FULLBAR_G8.json980B SHA01ae955a622475409f6fb70c90143651eeff5d433279461b3d0c92632c4c53b0
- FREE_LIVE_FULLBAR_G6_AUDIT.json12542B SHA027253464ae1042718ec158ab01e03a849d9909a104e9fd0679a2e5ce06761c4
- FREE_LIVE_FULLBAR_G7_AUDIT.json11880B SHA2bc86d2b578665b6fb191f5dff60ee18a6c69831cecc60b9d0350eb99b9b2614
- FREE_LIVE_FULLBAR_G8_AUDIT.json7715B SHA569dc46550db31095218e37c2694e4b08f3197d1cc63eeca7a77a9e4278504de

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

## FREE_LIVE_FULLBAR_G6.json
```json
{"denominator":1000000,"name":"FREE_LIVE_FULLBAR_G6","points":[[-952817,-11945,231078],[-940433,-37265,448837],[-920744,15974,19909],[-900886,60970,613198],[-933388,-178977,300739],[-891645,-299764,144732],[-826532,159289,769716],[-844858,41864,-180018],[-816305,-398150,-12470],[-723019,51678,-365076],[-715559,242005,920497],[-707170,-476456,-162089],[-582162,-20909,-503825],[-569122,303214,1060657],[-559471,-547440,-287728],[-386161,363289,1178147],[-354854,24044,-630910],[-329743,-744500,-118185],[-376563,-533206,-441512],[-166570,426655,1261488],[-148354,-500657,-543123],[137137,-597701,-427270],[97283,-772328,37442],[92335,492190,1299179],[105785,-289262,-619373],[381050,555026,1273584],[651085,376045,-319837],[688768,609999,1167090],[1028623,653902,938504],[1638212,679253,175997]]}
```

## FREE_LIVE_FULLBAR_G7.json
```json
{"denominator":10000000,"name":"FREE_LIVE_FULLBAR_G7","points":[[-9528168,-119445,2310785],[-9404330,-372647,4488373],[-9207439,159745,199090],[-9008856,609705,6131979],[-9333881,-1789768,3007385],[-8916452,-2997642,1447319],[-8265316,1592888,7697162],[-8448583,418638,-1800181],[-8163052,-3981497,-124701],[-7230185,516775,-3650761],[-7155590,2420048,9204973],[-7071696,-4764558,-1620888],[-5821620,-209090,-5038254],[-5691219,3032144,10606566],[-5594715,-5474398,-2877278],[-3861609,3632892,11781470],[-3548544,240442,-6309102],[-3297429,-7444998,-1181849],[-3765630,-5332064,-4415124],[-1665697,4266552,12614884],[-1483537,-5006565,-5431228],[1371373,-5977014,-4272697],[972831,-7723282,374418],[923349,4921900,12991790],[1057845,-2892616,-6193735],[3810499,5550263,12735835],[6510848,3760455,-3198373],[6887683,6099989,11670904],[10286228,6539022,9385045],[16382119,6792525,1759966]]}
```

## FREE_LIVE_FULLBAR_G8.json
```json
{"denominator":100000000,"name":"FREE_LIVE_FULLBAR_G8","points":[[-95281685,-1194451,23107849],[-94043301,-3726468,44883730],[-92074390,1597447,1990897],[-90088559,6097046,61319792],[-93338810,-17897683,30073851],[-89164517,-29976424,14473190],[-82653160,15928883,76971621],[-84485826,4186380,-18001810],[-81630517,-39814966,-1247005],[-72301850,5167754,-36507605],[-71555903,24200485,92049733],[-70716960,-47645582,-16208883],[-58216198,-2090901,-50382535],[-56912189,30321437,106065656],[-55947147,-54743984,-28772785],[-38616090,36328922,117814700],[-35485445,2404420,-63091020],[-32974295,-74449975,-11818487],[-37656301,-53320635,-44151235],[-16656975,42665520,126148844],[-14835366,-50065650,-54312275],[13713726,-59770136,-42726973],[9728312,-77232818,3744183],[9233485,49218999,129917902],[10578453,-28926162,-61937345],[38104992,55502626,127358352],[65108477,37604547,-31983730],[68876832,60999894,116709036],[102862284,65390222,93850445],[163821187,67925255,17599660]]}
```
