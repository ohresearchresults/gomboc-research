# material-f86dc15bccb1

AI research material · [Export notes](../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

# C306_G4_OWN121: useful rational non-winner, not a solution of the target

This is a new V53/E153/F102, C306 uniformly filled rational simplicial polyhedron. Its actual-centroid complete census is strict121, weak000. It is NOT own110 and does NOT replace the canonical C622 winner. It comes from the coordinator's coupled free-coordinate numerical flow on the exact C318 V55 input, followed by deleting original indices17 and21 from the near-collision checkpoint, rounding all remaining coordinates to the 1/10000 grid with numpy ties-to-even, lexicographically sorting and rebuilding the hull. Literal integer points and oriented true facets below are the recovery authority; reconstructing the exploratory floating flow is unnecessary to reconstruct or check this exact body.

All coordinates are integers divided by10000. The exact audit checks every triangle against every other vertex with strict support inequalities, so there are no artificial coplanar triangle edges. It checks every oriented edge occurs twice, all vertices appear, Euler, positive volume, and actual centroid interior. Filled-volume mass and first moments are integrated twice, about the coordinate origin and an interior rational average. It directly enumerates ALL stable face feet, unstable vertex cones, saddle edge cones and equality cases. It does not infer H or weak counts from Morse arithmetic.

Expected exact census: V53,E153,F102,C306; strict [1,2,1], weak [0,0,0]; stable input facet0, unstable input vertices[0,14], saddle input edge[44,46]. These input indices belong to this literal lex-sorted C306 source, NOT C318's indices. Volume=1690203202641/1000000000000. Centroid=[409355912737/135216256211280000,855529297349/67608128105640000,5154137003/270432512422560].

Reconstruction: write the two file blocks below exactly, data without final newline, Python source with one final newline. Python3.11.8 standard library only. Run `python exact_tri_audit.py farthest_merged_G10000.json C306_G4_EXACT.json`. Expected marker `EXACT_SIMPLICIAL_FILLED_CENSUS_PASS 306 1 2 1 0 0 0`. Run `sha256sum farthest_merged_G10000.json exact_tri_audit.py C306_G4_EXACT.json`.
Input farthest_merged_G10000.json:2051 bytes,SHA256 89599e0825f7075c151639b70d9db5959fcdc058c0be555d1a96d8598ccdea3e.
Source exact_tri_audit.py:3006 bytes,SHA256 8847ba4656c7930bbf149cf98dc0f1f17b24902524f94220539441572d14facc.
Output C306_G4_EXACT.json:346 bytes,SHA256 50939b89e946cb8c47c43bc07268489a44af1a48bc528f7b580d4e52e53adf61.

The same source passed a regular tetrahedron control: P=[(1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1)], oriented T=[[0,1,2],[0,3,1],[0,2,3],[1,3,2]], all coordinates Fraction integers. `audit(P,T)` returns strict[4,4,6],weak[0,0,0]. Reversing those facets is correctly rejected by the support test.

## File farthest_merged_G10000.json
```json
{"points":[[-7119,-2846,-12077],[-7102,-909,-11968],[-6439,441,-10952],[-5349,-4467,-12086],[-5306,1891,-11437],[-5230,335,-12543],[-4444,-6826,-8110],[-3525,3597,-8449],[-3014,4040,-6427],[-2286,2708,12727],[-2227,2539,12720],[-2057,3816,12738],[-1808,-7620,-6954],[-1509,3919,-8754],[-1436,6502,12651],[-1283,-100,12426],[-1163,-418,12195],[-890,6773,12054],[-406,6327,4821],[-161,-2259,9752],[-91,4644,-5528],[153,6179,2265],[554,-7288,-2690],[638,6245,10653],[1035,-840,11842],[1095,-1583,10629],[1411,5933,1052],[2617,-309,11395],[2785,-7516,-3384],[2832,5731,1161],[3015,-4896,1990],[3199,3144,-4133],[4148,-3498,3419],[4148,5374,4913],[5115,5438,2525],[5262,2761,-1815],[5273,-5387,-2759],[5640,1860,-2182],[5640,3983,67],[5646,3546,-433],[5715,4413,873],[5808,4866,1838],[5964,426,4608],[6055,645,-2661],[6147,-654,4872],[6229,-630,-2949],[6271,-2552,1707],[6289,-3808,-183],[6330,-2190,-2728],[6504,2553,1748],[6634,126,825],[6643,1898,1637],[6681,844,1225]],"grid":10000,"T":[[6,15,0],[1,0,9],[7,13,4],[23,34,17],[21,13,7],[45,52,48],[14,17,7],[14,7,4],[16,15,6],[29,17,34],[29,21,17],[18,17,21],[50,48,52],[50,52,47],[50,47,48],[5,45,48],[5,4,13],[5,13,45],[5,0,1],[5,1,4],[11,1,9],[11,14,1],[2,4,1],[2,14,4],[2,1,14],[20,13,21],[20,29,34],[8,21,7],[8,18,21],[8,7,17],[8,17,18],[36,48,47],[36,47,28],[22,12,28],[22,6,12],[43,45,13],[10,15,11],[10,11,9],[10,0,15],[10,9,0],[46,47,52],[46,52,44],[46,44,47],[51,44,52],[51,49,44],[51,52,45],[51,45,43],[51,43,49],[41,20,34],[41,49,43],[41,13,20],[26,21,29],[26,20,21],[26,29,20],[3,5,48],[3,48,36],[3,0,5],[3,28,12],[3,36,28],[3,6,0],[3,12,6],[30,28,47],[30,25,28],[19,22,28],[19,28,25],[19,16,6],[19,6,22],[24,11,15],[24,14,11],[24,15,16],[24,16,19],[24,19,25],[31,13,38],[31,43,13],[42,44,49],[42,49,41],[40,38,13],[40,13,41],[40,43,38],[40,41,43],[27,25,30],[27,47,44],[27,24,25],[27,44,42],[27,23,17],[27,17,14],[27,14,24],[33,42,41],[33,34,23],[33,41,34],[33,23,27],[33,27,42],[32,30,47],[32,47,27],[32,27,30],[39,38,43],[39,31,38],[39,35,31],[37,43,31],[37,31,35],[37,39,43],[37,35,39]]}
```

## File exact_tri_audit.py
```python
"""Complete exact strict/weak census for a proposed strictly simplicial convex hull.
Rejects coplanar triangle subdivisions: the accepted triangle complex is maximal.
Boundary mass is integrated about zero and an interior rational reference point.
"""
import json,sys,pathlib
from fractions import Fraction as Q

def dot(a,b):return sum(x*y for x,y in zip(a,b))
def add(a,b):return tuple(x+y for x,y in zip(a,b))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def mul(q,a):return tuple(q*x for x in a)
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def det(a,b,c):return dot(a,cross(b,c))
def integration(P,T,o):
 D=Q(0);N=(Q(0),)*3
 for tri in T:
  a,b,c=[sub(P[i],o) for i in tri];d=det(a,b,c);D+=d;N=add(N,mul(d,add(add(a,b),c)))
 return D/6,add(o,mul(1/(4*D),N))
def audit(P,T):
 assert len(set(P))==len(P) and len(set(tuple(sorted(t)) for t in T))==len(T)
 edges={};H=[]
 for f,tri in enumerate(T):
  assert len(tri)==3 and len(set(tri))==3
  a,b,c=[P[i] for i in tri];n=cross(sub(b,a),sub(c,a));assert any(n)
  h=dot(n,a);assert all(dot(n,p)<h for j,p in enumerate(P) if j not in tri)
  H.append((n,h))
  for i,j in zip(tri,tri[1:]+tri[:1]):edges.setdefault(tuple(sorted((i,j))),[]).append((f,i,j))
 assert set(i for t in T for i in t)==set(range(len(P)))
 assert all(len(e)==2 and e[0][1:]==e[1][1:][::-1] for e in edges.values())
 assert len(P)-len(edges)+len(T)==2
 interior=tuple(sum(p[k] for p in P)/len(P) for k in range(3))
 V,c=integration(P,T,(Q(0),)*3);V2,c2=integration(P,T,interior)
 assert V==V2 and c==c2 and V>0
 assert all(h-dot(n,c)>0 for n,h in H)
 strict=[[],[],[]];weak=[[],[],[]]
 def classify(z,vals,key):
  if all(x>=0 for x in vals):(strict if all(x>0 for x in vals) else weak)[z].append(key)
 for f,(n,h) in enumerate(H):
  nn=dot(n,n);p=add(mul(nn,c),mul(h-dot(n,c),n))
  vals=[hh*nn-dot(m,p) for g,(m,hh) in enumerate(H) if g!=f]
  classify(0,vals,f)
 for i,p in enumerate(P):classify(1,[-dot(sub(p,c),sub(q,p)) for j,q in enumerate(P) if i!=j],i)
 for (i,j),pair in sorted(edges.items()):
  d=sub(P[j],P[i]);dd=dot(d,d);te=dot(sub(c,P[i]),d);r=add(mul(dd,sub(P[i],c)),mul(te,d))
  n=H[pair[0][0]][0];m=H[pair[1][0]][0];aa=dot(n,n);bb=dot(n,m);cc=dot(m,m);G=aa*cc-bb*bb
  assert dd>0 and G>0
  A=cc*dot(n,r)-bb*dot(m,r);B=aa*dot(m,r)-bb*dot(n,r)
  classify(2,[te,dd-te,A,B],[i,j])
 return dict(V=len(P),E=len(edges),F=len(T),C=2*len(edges),strict=[len(x) for x in strict],weak=[len(x) for x in weak],strict_labels=strict,weak_labels=weak,volume=str(V),centroid=[str(x) for x in c],second_centroid_integration_equal=True,maximal_complex_exact=True)
def main():
 z=json.load(open(sys.argv[1]));P=[tuple(Q(x,z['grid']) for x in p) for p in z['points']];out=audit(P,z['T'])
 if len(sys.argv)>2:pathlib.Path(sys.argv[2]).write_text(json.dumps(out,sort_keys=True,separators=(',',':')))
 print(json.dumps(out,sort_keys=True));print('EXACT_SIMPLICIAL_FILLED_CENSUS_PASS',out['C'],*out['strict'],*out['weak'])
if __name__=='__main__':main()
```

For the companion no-go source [internal-source-reference], the full_star_exact.py source byte count omitted from its prose manifest is6230; its published SHA256 and output hashes are unchanged.
