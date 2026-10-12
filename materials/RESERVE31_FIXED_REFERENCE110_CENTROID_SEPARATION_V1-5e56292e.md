# material-5e56292efbbb

AI research material · [Export notes](../catalog/coverage.md#text-records)

---

# RESERVE31_FIXED_REFERENCE110_CENTROID_SEPARATION_V1

## Exact result and scope
K is the literal H23_CAP_RESERVE31_G5 source below, identical to the input in material [internal-source-reference], not coordinates from a prose summary. It has V31/E87/F58,C174. The present exact integer cover proves: for every interior reference centre c of this FIXED K with c_x >= -56057/200000, either S(K,c)>=2 or U(K,c)>=2. Thus the entire strict reference110 region of K lies in c_x < -56057/200000. All possible stable and unstable roots are covered; no old witness tree/root is assumed. No saddle/Euler inference is needed for this necessary-condition exclusion.

For any full-dimensional convex L subset K retaining K's lexicographic vertex30=(174422,57073,13918)/100000, its homogeneous volume centroid c_L satisfies c_L in (3K+p30)/4 and hence c_L,x >= -56057/200000. Therefore NO reference110 centre of the original K is an attainable centroid of that inner-retained-root family. IMPORTANT: this does NOT exclude an own110 changed inner body L: its facet/vertex equilibrium regions need not equal those of K. It also does not exclude moved roots or outward deformations. The construction target remains unresolved.

The classical centroid input is -(L-c_L) subset 3(L-c_L), giving (4c_L-p30)/3 in L. Consulted primary source: D.V. Feldman, Arranging convex bodies for maximum intersection volume: the sharp efficiency of centroid alignment, arXiv:2608.04516v1 (5 Aug 2026), Lemma6 and body-form restatement in Section2. The integer cover itself is independent of this external lemma.

## Method
Enumerate all exact supporting triples of all 56 input points, reject nontriangular maximal faces, obtain the exact hull. For each true vertex, all adjacent escape rows are linear in c; all strictly negative implies strict U. For each oriented triangle face, its three extruded side inequalities are linear in c; all strictly inside implies strict S. Subdivide the enclosing box of K intersected with c_x>=threshold, bisecting a longest axis. Each leaf is outside K by a strict supporting-plane bound, or has two forced U or two forced S over the entire closed box. An independent coverage traversal checks every leaf's integer inequalities and the complete binary cover. No floating arithmetic, tolerance, MILP oracle, or interval library participates in this proof.

Observed: 607 leaves (206 outside,379 U,22 S), maximum depth26. All certificate arithmetic is exact integer arithmetic. Exploratory floating MILP suggested sup c_x about -0.4579449256, but that sharper bound is NOT asserted by this capsule.

## Recovery
Save the two following fenced files with one trailing newline. Python3.13.5 standard library only. Run `python exact_center_cover.py`. Expected marker `RESERVE31_EXACT_CENTER_COVER_PASS`. Run `sha256sum RESERVE31_INPUT.json exact_center_cover.py RESERVE31_EXACT_CENTER_COVER.json`.
Expected UTF-8 byte counts and SHA256:
- RESERVE31_INPUT.json:1339,4b1bed14b6174e65850f72f54a597e0dc284c3cf65fa3962d75a27c796017d5f
- exact_center_cover.py:6537,0ae775a8f3c7946345fe47000d1430a0290e4bb6f46e325000cd463a63110f4f
- RESERVE31_EXACT_CENTER_COVER.json:18348,6b93a83d39517933acf0923a8de070174cffc89133a8cb76f0bb2a0756445cf0
The output leaf list is regenerated completely; no sandbox file is required.

## RESERVE31_INPUT.json
```json
{"denominator":100000,"grid":5,"name":"H23_CAP_RESERVE31_G5","points":[[-95512,1490,25213],[-92617,4591,3048],[-90183,-23425,34547],[-85936,-33837,16739],[-85037,249,-17306],[-74926,5521,-33963],[-77222,-42862,-1043],[-61439,-786,-47925],[-65034,-36022,5303],[-38556,897,-61657],[-42340,-38436,9258],[-64356,-50158,-16879],[-32278,-63506,-21925],[-48064,-55390,-29772],[-36669,-42439,6021],[9251,-59221,-17697],[-35867,-46732,-2637],[-34821,-46844,-2896],[-33545,-49162,-5868],[-21087,-13232,-56495],[-27949,-15979,21685],[-15824,-25602,6806],[-5504,-13406,-36512],[-29705,-57450,-39772],[12113,-19371,-55111],[-8131,-62437,-39885],[-13440,-56712,-43998],[10910,-24179,-53048],[-1833,-213,33447],[654,85,33808],[13962,-48903,-49048],[14709,6666,-43730],[27111,12571,44253],[58833,34102,51451],[37350,29486,-11086],[66559,39299,53495],[53229,31424,-27879],[68995,44973,39725],[74206,45726,36267],[75708,49026,34308],[86377,47555,32579],[174422,57073,13918],[-93489,-4976,45789],[-91581,10889,57855],[-85118,19369,72156],[-73491,17040,92064],[-58357,27635,106661],[-38845,38199,118343],[-16345,44940,126466],[11341,51558,130173],[28827,55973,127854],[64679,62553,118152],[104620,67256,93276],[-79271,-19947,6471],[-78555,-20797,6749],[-77981,-21651,7044]],"rounding":"binary64, independent nearest ties-to-even","source":"CAP_RESERVE.json"}
```

## exact_center_cover.py
```python
"""RESERVE31 reference110 region / retained-root centroid separation.
Standard-library, exact integers throughout the covering proof.
The theorem concerns equilibrium of the FIXED hull K about a variable centre.
It does NOT exclude changed inner hulls L, whose facet geometry changes.
"""
from itertools import combinations
from functools import reduce
from math import gcd
from pathlib import Path
import hashlib,json,sys

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

def rows(p,facets,edges):
    # Variable X = 2 D c; c is the physical reference-centre coordinate.
    # Every row a.X+b is positive for the corresponding escape witness.
    nb=[[] for _ in p]
    for a,b in sorted(edges):nb[a].append(b);nb[b].append(a)
    us=[];ss=[]
    for i,ns in enumerate(nb):
        g=[]
        for j in sorted(ns):
            a=sub(p[i],p[j]);g.append(primitive(a,-2*dot(a,p[i])))
        us.append(g)
    for f,n,h in facets:
        g=[]
        for i,j in zip(f,f[1:]+f[:1]):
            a=neg(cross(n,sub(p[j],p[i])))
            g.append(primitive(a,-2*dot(a,p[i])))
        ss.append(g)
    outs=[primitive(n,-2*h) for f,n,h in facets]
    return us,ss,outs

def upper(row,l,u,den):
    a,b=row
    return b*den+sum(v*(u[k] if v>=0 else l[k]) for k,v in enumerate(a))
def lower(row,l,u,den):
    a,b=row
    return b*den+sum(v*(l[k] if v>=0 else u[k]) for k,v in enumerate(a))
def split(l,u):
    k=max(range(3),key=lambda k:u[k]-l[k]);m=l[k]+u[k]
    ll=[2*v for v in l];uu=[2*v for v in u];leftu=uu[:];rightl=ll[:]
    leftu[k]=m;rightl[k]=m
    return k,(ll,leftu),(rightl,uu)

def create_cover(p,facets,edges,lo_x):
    us,ss,outs=rows(p,facets,edges)
    l=[2*min(v[k] for v in p) for k in range(3)];u=[2*max(v[k] for v in p) for k in range(3)];l[0]=lo_x
    stack=[(l,u,1,'')];leaves=[];maxdepth=0
    while stack:
        l,u,den,path=stack.pop();maxdepth=max(maxdepth,len(path))
        out=next((i for i,row in enumerate(outs) if lower(row,l,u,den)>0),None)
        if out is not None:leaves.append([path,'outside',out]);continue
        covered=False
        for name,groups in [('U',us),('S',ss)]:
            forced=[]
            for i,g in enumerate(groups):
                if all(upper(row,l,u,den)<0 for row in g):forced.append(i)
                if len(forced)==2:leaves.append([path,name,forced]);covered=True;break
            if covered:break
        if covered:continue
        if len(path)>=60:raise RuntimeError('cover search unresolved at depth60')
        k,left,right=split(l,u)
        stack.append((*right,2*den,path+'1'));stack.append((*left,2*den,path+'0'))
    return {'scale':2*100000,'lower':[lo_x]+[2*min(v[k] for v in p) for k in [1,2]],'upper':[2*max(v[k] for v in p) for k in range(3)],'leaf_count':len(leaves),'maxdepth':maxdepth,'leaves':leaves}

def verify_cover(obj,p,facets,edges):
    us,ss,outs=rows(p,facets,edges);leaves={r[0]:r[1:] for r in obj['leaves']}
    assert len(leaves)==obj['leaf_count'];visited=set();stack=[(obj['lower'],obj['upper'],1,'')]
    counts={'outside':0,'U':0,'S':0};margins=[]
    while stack:
        l,u,den,path=stack.pop()
        if path not in leaves:
            assert any(q.startswith(path) for q in leaves)
            k,left,right=split(l,u);stack.append((*right,2*den,path+'1'));stack.append((*left,2*den,path+'0'));continue
        name,ids=leaves[path];visited.add(path);counts[name]+=1
        if name=='outside':assert lower(outs[ids],l,u,den)>0
        else:
            assert len(ids)==2 and ids[0]!=ids[1]
            groups=us if name=='U' else ss
            assert all(upper(row,l,u,den)<0 for i in ids for row in groups[i])
    assert visited==set(leaves)
    return counts

def main():
    root=Path(__file__).parent;data=(root/'RESERVE31_INPUT.json').read_bytes()
    assert hashlib.sha256(data).hexdigest()=='4b1bed14b6174e65850f72f54a597e0dc284c3cf65fa3962d75a27c796017d5f'
    raw=json.loads(data);assert raw['denominator']==100000
    p,facets,edges=exact_hull(raw)
    assert (len(p),len(edges),len(facets))==(31,87,58)
    assert p[30]==(174422,57073,13918)
    assert min(v[0] for v in p)==-95512
    # 2 D ((3 min(K_x)+p30_x)/4) = -56057.
    assert (3*min(v[0] for v in p)+p[30][0])//2==-56057
    obj=create_cover(p,facets,edges,-56057);counts=verify_cover(obj,p,facets,edges)
    out={'object':'RESERVE31_FIXED_REFERENCE110_CENTROID_SEPARATION_V1','V':31,'E':87,'F':58,'C':174,'x_threshold':'-56057/200000','meaning':'Every c in K with cx >= threshold has S(K,c)>=2 or U(K,c)>=2. This is a fixed-K reference-centre exclusion, not an exclusion of all changed inner polyhedra L.','leaf_types':counts,**obj}
    text=json.dumps(out,sort_keys=True,separators=(',',':'))+'\n';target=root/'RESERVE31_EXACT_CENTER_COVER.json';target.write_text(text)
    print('RESERVE31_EXACT_CENTER_COVER_PASS',counts,'leaves',obj['leaf_count'],'maxdepth',obj['maxdepth'])
    print(target.name,len(text.encode()),hashlib.sha256(text.encode()).hexdigest())
if __name__=='__main__':main()
```
