# material-1768033b4a72

AI research material · [Export notes](../catalog/coverage.md#text-records)

---

# Recovery capsule part 1/2: G6_DEPTH5_ESCAPE_MASS_OBSTRUCTION

This is an exact restricted-family obstruction, NOT a new own110 body or an exclusion of the whole <=21-cut family. Part2 supplies the complete verifier; BOTH parts are necessary. Literal G6 below comes from fully read immutable figure-0413, SHA256 c90bbfd9147dd255be0c9f0f057598c405246432a28a6036463a1d8d5cb507c4. G6 and the compulsory inner witness P5 are distinct objects.

## Theorem and scope
Let K be the literal G6 hull, and normalize its84 original facet normals p by p.x<=1. K has V44/E126/F84, contains0 strictly, is not mass-centered, and its only strict stable facet relative to0 is the triangle on input rows[5,38,44]; there are no extra weak stable facets.
A closed dot-escape arrow a->b means a!=b and a.(b-a)>=0. Any added halfspace n.x<=1 is called shallow if n has at most FIVE such arrows to ANY original p, allowing arbitrary hypothetical intermediate vectors. There may be arbitrarily many shallow cuts. The generated P5 is contained in K and ALL possible shallow halfspaces, and entirely in U.x<=0 for U=(200,52,-61).
For ANY measurable P5 subset L subset K,
integral_L (200*x+52*y-61*z)dV < -1/100.
Hence no such L has ordinary volume centroid0. In particular every origin-centered polyhedral subbody of G6 whose unique strict stable facet is inherited requires a directed escape path containing at least SIX consecutive new active facets before its first original facet. This excludes <=5 new active facets with an inherited unique strict S, and more generally arbitrarily many shallow cuts. Stable-root replacement and six-or-more cooperating facets remain OPEN. No G8 statement is inferred.

## Proof linking the finite certificate to arbitrary cut families
Closed arrows strictly increase squared norm: |b|^2=|a|^2+2*a.(b-a)+|b-a|^2>|a|^2. Every actual polar vertex corresponding to a non-strict-stable facet has a closed outgoing arrow because its perpendicular foot fails at least one strict inequality p.n<|n|^2. Finite paths therefore end at a strict polar unstable vertex, equivalently a strict primal stable facet. With a unique inherited strict S, every new normal reaches an original one. Additional weak S does not evade the closed-arrow argument, although the construction target forbids weak equilibria.

Suppose n reaches p in at most m arrows. When n.x<=0 there is nothing to check. Otherwise multiply the radial cosine bounds along the arrows and the angle between x and n, padding zero angles to m+1 factors. The angle triangle inequality and concavity of log(cos) yield
n.x <= |p|*|x|*cos(angle(p,x)/(m+1))^(m+1).
The angles in the product lie in[0,pi/2); their sum is at least angle(p,x). No actual intermediate facet or fixed chain plane is required. It suffices to bound this expression by1 at every P5 vertex for all original p; membership in every reachable halfspace extends by convexity.

For m5 put b=|p|^2*|x|^2,c=p.x. If b<=1 Cauchy suffices. Otherwise t=b^(1/6). On1<=t<=4/3 the bound is equivalent to c<=T(t), where T(t)=32-48t+18t^2-t^3, by expansion of cos(6acos(1/sqrt(t))). The endpoint4/3=sec(pi/6)^2 keeps the relevant angle<=pi. T is decreasing on this interval; therefore any rational u>=t,u<=4/3 with c<=T(u) suffices.
In integer coordinates p=G*n/h,x=I/G,G=10^6, b=(n.n)*(I.I)/h^2 and c=(n.I)/h. With A=10^6 the verifier finds the smallest integer v satisfying
(v-1)^6*h^2 < (n.n)*(I.I)*A^6 <= v^6*h^2,
checks3*v<=4*A, and checks
(n.I)*A^3 <= h*(32*A^3-48*v*A^2+18*v^2*A-v^3).
All predicates are integer/rational. The generator's floating initial root is corrected by exact powers; the verifier uses independent integer binary search.

The final mass bound follows from inclusion: integral_(L positive)U.x <= integral_(K positive)U.x and integral_(L negative)U.x <= integral_P5 U.x. Their exact sum is below-1/100. Informative approximations ONLY: positive17.246575837690326, compulsory negative-17.262479827793143, total-0.015903990102815995.

## Complete recovery commands, identities and observed execution
In an empty directory write G6.json from its block with NO terminal newline; write BUILD_DEPTH5.py below and VERIFY_DEPTH5.py from part2 with exactly one final LF. These THREE files are all recovery inputs, requiring no original sandbox.
Observed environment: CPython3.13.5, NumPy2.3.5, SciPy1.17.0.
Run:
OPENBLAS_NUM_THREADS=1 python BUILD_DEPTH5.py 14
python -B -S VERIFY_DEPTH5.py
NumPy/SciPy only nominate triangles. The standard-library-only verifier certifies all global supporting inequalities, merged maximal polygons, real edges, closed topology, exact containment and two complete volume/first-moment integrations. No floating predicate occurs in that verifier. All maximal P5 faces are triangular.
The full nondefault settings are literal: cube grid14, root grid10^6, root limit1333333, radial integer bracket[0,2000000), U=(200,52,-61), lexicographic rays, canonically oriented/rotated/sorted nominations.

Expected AND actually observed after cold replay from only those three inputs:
G6_DEPTH5_NEW_FACET_ESCAPE_MASS_OBSTRUCTION_PASS 2353 84 197652
Both regenerated output hashes below matched. Exact point-normal checks197652, sixth-root checks64372, largest upper-root numerator1156726. P5V2353/E7053/F4702; all4702faces triangles. P5 signed-origin fan has4699positive,2negative,1zero tetrahedra; all4702interior-anchor tetrahedra are positive, and volume and all3moments agree. K and K positive also have two matching exact integrations. Cube, half-cube and reversed-nomination controls pass.

Canonical identities:
G6.json:1144bytes;SHA256 63ead46daff5c7c9cd4344699cbe551a7e92b2a2851703aacfa55eb1621b6aa5.
BUILD_DEPTH5.py:2814bytes;SHA256 01fde8323e7efc2440dd862f2db43392699866ddf3be209998dafd719d094bfb.
VERIFY_DEPTH5.py:11793bytes;SHA256 5f99e7a6b74049111e12a091eeb056d42d9e627caf01498095d43dbdbe28e734.
DEPTH5_K14_CANONICAL.json:131094bytes;SHA256 f939e6df7fa195e13ff102a386c437cef0fe9fceef8d192a559f2113253aa31d.
DEPTH5_PROOF.json:7469bytes;SHA256 6c20b7c64119bea8951be862d7b588d5db5fec702d6410036653b0059de6005f.
All2353points, incidence and exact result fractions are regenerated by these complete sources. Hashes identify bytes rather than replace them.

## File: G6.json
```json
{"grid":1000000,"points":[[-662782,-214465,-845973],[-414228,-151742,533649],[-161896,254607,812156],[365352,256078,682778],[-4963,148822,-521027],[472559,520988,212704],[79060,562904,-173068],[201613,126680,-443592],[329321,453145,628173],[223093,597478,579771],[-19072,614025,655946],[-249702,561436,698505],[-441568,542642,645050],[81579,740260,404654],[-621409,499632,558154],[-759574,464284,346398],[-876227,418544,281729],[-762901,475717,422075],[-969023,321126,89302],[-933907,249672,-106357],[-931297,367490,186346],[-990566,281683,-2502],[-1004114,233262,-93695],[-1009407,175066,-181963],[-1003594,111429,-275498],[-985825,56733,-362387],[-963561,3357,-431336],[-926489,-29260,-514430],[-874803,-74796,-604952],[-797712,-129095,-709746],[212288,-80824,-582533],[-530449,-300001,-896862],[-453991,-363552,-909506],[-263404,-613951,20338],[-477834,-372599,114345],[-600760,-232410,-880486],[-364153,-430343,-913823],[217011,-462047,-780335],[486981,106570,612006],[157779,-569803,63306],[-149044,-601434,-828255],[-98079,-133974,751134],[19869,-745421,-660667],[119026,-858571,-341744],[285028,-657317,-632695],[168908,-413062,260503]]}
```

## File: BUILD_DEPTH5.py
```python
from fractions import Fraction as F
from itertools import product,combinations
import json,math,hashlib,sys,time
import numpy as np
from scipy.spatial import ConvexHull
raw=json.load(open('G6.json'));P=raw['points']
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def sub(a,b):return [x-y for x,y in zip(a,b)]
def cross(a,b):return [a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]]
old_triangles=[];planes=[]
for triple in combinations(range(len(P)),3):
 tri=list(triple);a,b,c=[P[i] for i in tri];n=cross(sub(b,a),sub(c,a));h=dot(n,a)
 if n==[0,0,0] or h==0:continue
 if h<0:n=[-x for x in n];h=-h;tri[1],tri[2]=tri[2],tri[1]
 if any(dot(n,x)>h for x in P):continue
 assert sum(dot(n,x)==h for x in P)==3
 j=tri.index(min(tri));old_triangles.append(tri[j:]+tri[:j])
 g=math.gcd(*n,h);planes.append(([x//g for x in n],h//g))
old_triangles=sorted(old_triangles);assert len(old_triangles)==84
planes=sorted(planes);A=10**6;LIMIT=4*A//3;U=(200,52,-61)
def rootup(bn,bd):
 u=int((bn/bd)**(1/6)*A)+1;t=bn*A**6
 while (u-1)**6*bd>=t:u-=1
 while u**6*bd<t:u+=1
 return u

def valid(j,checks):
 for dn,n2d2,h in checks:
  bn=j*j*n2d2;bd=h*h
  if bn<=bd:continue
  u=rootup(bn,bd)
  if u>LIMIT:return False
  if j*dn*A**3>h*(32*A**3-48*u*A*A+18*u*u*A-u**3):return False
 return True

k=int(sys.argv[1]) if len(sys.argv)>1 else 14;dirs=set()
for ax in range(3):
 for u,v in product(range(-k,k+1),repeat=2):
  for sg in[-k,k]:
   d=[u,v];d.insert(ax,sg)
   if dot(d,U)<=0:dirs.add(tuple(d))
points=[];start=time.time()
for d in sorted(dirs):
 checks=[(dot(n,d),dot(n,n)*dot(d,d),h) for n,h in planes]
 lo,hi=0,2*10**6
 while hi-lo>1:
  mid=(hi+lo)//2
  if valid(mid,checks):lo=mid
  else:hi=mid
 points.append([lo*x for x in d])
h=ConvexHull(np.array(points,float));t=np.array(points,float)[h.simplices]/1e6
flip=np.einsum('ij,ij->i',np.cross(t[:,1]-t[:,0],t[:,2]-t[:,0]),h.equations[:,:3])<0
q=t[flip,1].copy();t[flip,1]=t[flip,2];t[flip,2]=q
w=np.einsum('i,ij->j',np.einsum('ij,ij->i',t[:,0],np.cross(t[:,1],t[:,2])),t.sum(axis=1))/24
mom=w
nominations=[]
S=tuple(sum(p[j] for p in points) for j in range(3));N=len(points)
for tri0 in h.simplices.tolist():
 tri=list(tri0);a,b,c=[points[i] for i in tri];n=cross(sub(b,a),sub(c,a));d=dot(n,a)
 if dot(n,S)>N*d:tri[1],tri[2]=tri[2],tri[1]
 j=tri.index(min(tri));nominations.append(tri[j:]+tri[:j])
nominations=sorted(nominations)
obj=dict(grid=1000000,points=points,nominations=nominations,old_triangles=old_triangles,root_scale=A,root_limit=LIMIT,depth=5,cube_grid=k,covector=U)
b=json.dumps(obj,sort_keys=True,separators=(',',':')).encode();path=f'DEPTH5_K{k}_CANONICAL.json';open(path,'wb').write(b)
print(path,len(points),'V',len(h.vertices),'Mx alongcov',dot(mom,U),'bytes',len(b),'sha',hashlib.sha256(b).hexdigest(),'seconds',time.time()-start,flush=True)
```
