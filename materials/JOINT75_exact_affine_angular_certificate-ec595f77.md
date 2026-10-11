# material-ec595f77c091

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

Public derivative: internal-record-identifiers-replaced.

---

# JOINT75 exact affine angular exclusion

New exact scoped theorem about the literal parent figure-0549, SHA f996fa67a06c542cbe559aadce39ce5f7b2f06b81a609a4a55dd3f03d9291605. Every uniformly filled affine image A K+t of its exact75-row primary, with kappa(A^T A)<=1095339/904661, retains two strict unstable vertices. If kappa(A^T A)<=66093/58907 it also retains the two cited strict stable faces. Complete integer/rational proof below discovers the entire hull, computes actual mass, and proves every required angle inequality without floating tolerances. Executed successfully by the coordinator. No target construction or full affine exclusion is claimed.

Recovery: save the following literal code block, including final newline, as exact_affine_certificate.py. It is6608 UTF-8 bytes, SHA-256 a5d0cc213b655eb1f1036b726f2587ef0f5eb763e5c99fcd6361476596ed187d. Run `python -B -S exact_affine_certificate.py > exact_affine_certificate.out`. Standard library only, tested CPython3.11.8. Output1753 bytes, SHA-256 a1fd96a1a3ce97672189d6473a7a991c198c5df45dbfc64e3a2d1ea9f0b164ff. Expected terminal marker: `JOINT75_EXACT_AFFINE_ANGULAR_CERTIFICATE_PASS 75 219 146 U2 S2 NO_OWN110_CLAIM`. No other input, seed, tolerance or nondefault parameter is needed.

```python
"""Exact rational angular certificate for the primary JOINT75 affine orbit.
Python standard library only. Coordinates and mass are from immutable parent
figure-0549, SHA f996fa67a06c542cbe559aadce39ce5f7b2f06b81a609a4a55dd3f03d9291605.
For G=A^T A, kappa(G)<=1095339/904661 preserves strict U at vertices6,62.
For kappa(G)<=66093/58907 it also preserves strict S on the two cited faces.
Proof: normalize G by (lambda_max+lambda_min)/2; its operator distance from
I is delta=(kappa-1)/(kappa+1). Each tested cos(-x,d) strictly exceeds c,
so x^T G d<0 whenever delta<=c. Polar images use A^{-T}; kappa(G^{-1})
is the same. Uniformly filled affine images have centroid A*g+t exactly.
This excludes own110 only in the specified moderate-distortion affine set.
No own110 construction or full-affine exclusion is claimed.
Reconstruct: save this complete UTF-8 text as exact_affine_certificate.py.
Verify: python -B -S exact_affine_certificate.py > exact_affine_certificate.out
Terminal marker: JOINT75_EXACT_AFFINE_ANGULAR_CERTIFICATE_PASS 75 219 146 U2 S2 NO_OWN110_CLAIM
Dependency: Python standard library (tested CPython3.11.8), exact integers
and fractions only; no tolerance, random seed, or non-default input.
"""
from fractions import Fraction as Q
from itertools import combinations
import json
I=[[-11310213, -3802031, 232661], [-11269293, -2834032, -2182730], [-10855182, -2246500, -3911998], [-10128821, -1814868, -5467871], [-9452382, -6834502, 6456555], [-9308206, -1555414, -6662777], [-8712882, -8006246, 8846843], [-8693078, -1373304, -7380329], [-7797905, -1286403, -8181129], [-6681453, -1307873, -8916622], [-6352338, 2020313, -1146993], [-5892536, 2295258, -71116], [-5592263, 2241235, 541206], [-5425338, -1474781, -9487378], [-5280741, 2171200, 1073969], [-4959361, 3312877, -1863739], [-4453446, 1994305, 2115702], [-4311479, 345947, 4048866], [-4305575, 1694912, 2608464], [-4237167, 1203950, 3206121], [-3820955, 4252385, -2139686], [-3661038, 4074852, -884602], [-3623465, -1644023, -10021566], [-3190033, 811977, 3827673], [-3155609, 4102561, 85230], [-3074935, 4483432, -2851622], [-2953571, -1851896, -10161171], [-2718323, 668005, 3934224], [-2651732, 122199, 4295157], [-2302445, 4621821, -3324860], [-2248430, -2037367, -10247983], [-2145336, 4388373, 461753], [-1938256, 3964861, 1093487], [-1561887, 3760992, 1454978], [-1502148, -2223378, -10275715], [-1278721, 4758931, -3663608], [-1049751, 3727821, 1606020], [-740759, -2457388, -10231458], [-298044, 4806779, -3669461], [-159770, 3872224, 1576892], [-121991, 838112, 3483867], [39249, -2666243, -10115526], [91753, 589879, 3521150], [725989, 729286, 3291554], [822613, -2865673, -9923443], [847151, 1601384, 2948252], [1257541, 4150503, 1429262], [1400720, 4852019, -3212547], [1599055, -3043575, -9655675], [2331916, -2317243, -9420429], [2351892, -3267823, -9302290], [2947803, 5018418, -438633], [3091632, -3449326, -8871363], [3252567, 4572542, 973174], [3518927, -4445832, -8207140], [3801752, -3598386, -8365506], [3886092, 3932529, 1241770], [4317265, 3420766, 1352627], [4466143, -3720508, -7791824], [4524082, -5334292, -6695320], [4622668, 3053371, 1323427], [4905967, 2678528, 1274548], [5061533, -3853293, -7158199], [5166891, 2298083, 1206990], [5506198, -4926808, -5369878], [5525767, -801605, -6004784], [5644371, 1606910, 926729], [6018142, 937609, 612094], [6137534, -4326615, -4182924], [6330239, 239389, 230320], [6547165, -3582767, -3087182], [6574260, -489010, -228500], [6738672, -1246564, -776981], [6751376, -2814918, -2197016], [6805726, -2026966, -1429050]]
D=10000000
GD=301728380651199510841280000000
GN=(-53286920506055854442174018051,-42633799180986064597953397917,-43819041531080084398689329023)
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
# Enumerate all strictly supporting triples using integers only.  This input
# has triangular maximal facets; no approximate hull or external facet list.
FACES=[]
for a,b,c in combinations(range(len(I)),3):
 n=cross(sub(I[b],I[a]),sub(I[c],I[a]));h=dot(n,I[a])
 if n==(0,0,0):continue
 sign=0
 for j,v in enumerate(I):
  if j in (a,b,c):continue
  z=dot(n,v)-h
  if z==0 or (sign and (z>0)!=(sign>0)):break
  sign=z
 else:FACES.append((a,b,c))
Z=[tuple(GD*x-D*y for x,y in zip(v,GN)) for v in I]
facets=[];edges={};tot=0;moment=[0,0,0]
for raw in FACES:
 a,b,c=raw;n=cross(sub(I[b],I[a]),sub(I[c],I[a]));h=dot(n,I[a]);
 vals=[dot(n,v)-h for j,v in enumerate(I) if j not in raw]
 assert all(x<0 for x in vals) or all(x>0 for x in vals)
 if vals[0]>0:b,c=c,b;n=tuple(-x for x in n)
 assert dot(n,Z[a])>0
 det=dot(I[a],cross(I[b],I[c]));tot+=det
 for k in range(3):moment[k]+=det*(I[a][k]+I[b][k]+I[c][k])
 for e in combinations(raw,2):edges.setdefault(tuple(sorted(e)),[]).append(len(facets))
 facets.append((a,b,c,n,dot(n,Z[a])))
assert len(I)==75 and len(facets)==146 and len(edges)==219
assert all(len(v)==2 for v in edges.values())
seen={0};todo=[0]
while todo:
 f=todo.pop()
 for e in combinations(FACES[f],2):
  for j in edges[tuple(sorted(e))]:
   if j not in seen:seen.add(j);todo.append(j)
assert len(seen)==146
vol=Q(tot,6*D**3);g=tuple(Q(v,4*D*tot) for v in moment)
assert vol==Q(942901189534998471379,750000000000000000000)
assert g==tuple(Q(n,GD) for n in GN)
# Supporting genuine triangles make a connected closed convex triangulation;
# hence they are the complete hull boundary, not a set of sampled faces.
def prove_angle(v,ds,num,den):
 ratios=[]
 for j,d in ds:
  s=dot(v,d); vv=dot(v,v);dd=dot(d,d)
  assert s<0 and dd>0
  assert den*den*s*s>num*num*vv*dd
  ratios.append((Q(s*s,vv*dd),j))
 return min(ratios)
p=[]
for i in (6,62):
 d=[(j,sub(Z[j],Z[i])) for j in range(75) if j!=i]
 rat,j=prove_angle(Z[i],d,95339,1000000)
 p.append(dict(vertex=i,attaining_vertex=j,cos_squared=str(rat)))
q=[]
for face in ((0,4,59),(14,16,24)):
 i=FACES.index(face);ni=facets[i][3];hi=facets[i][4]
 ds=[]
 for j,(_,_,_,nj,hj) in enumerate(facets):
  if j!=i:ds.append((j,tuple(hi*a-hj*b for a,b in zip(nj,ni))))
 rat,j=prove_angle(ni,ds,57488,1000000)
 q.append(dict(face=list(face),attaining_face=list(FACES[j]),cos_squared=str(rat)))
res=dict(V=75,E=219,F=146,volume=str(vol),centroid=list(map(str,g)),P=p,Q=q,
 primal_cos_lower='95339/1000000',polar_cos_lower='57488/1000000',
 U2_condition_G=str(Q(1095339,904661)),S2_condition_G=str(Q(1057488,942512)))
print(json.dumps(res,sort_keys=True,indent=2))
print('JOINT75_EXACT_AFFINE_ANGULAR_CERTIFICATE_PASS 75 219 146 U2 S2 NO_OWN110_CLAIM')
```
