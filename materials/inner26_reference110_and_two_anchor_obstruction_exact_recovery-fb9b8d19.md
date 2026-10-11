# material-fb9b8d199597

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

Public derivative: internal-record-identifiers-replaced.

---

# INNER26: exact reference110 and a two-retained-vertex obstruction

## Source and distinction
The input is literally ROOTFREE_INNER26_G4 from fully read accepted result figure-0555, SHA256 e0dc5597e1a1410335dfc2d509e9f92566c0011685d067534d286cd4cb941a0d. All26 integer rows and all48 oriented maximal triangular facets are included below. Its own class remains121, additional weak000, V/E/F=26/72/48 and C144. This material does NOT claim own110.

## Positive fixed-reference result
At c=(444696,-502924,-485197)/10^6, the same K has exact strict reference class110, additional weak000. The unique U is row3 and unique S is facet[19,21,22]; there are no strict or additional weak edge equilibria. The source calculates both the actual own centroid and this explicitly different reference centre, and performs complete strict/closed face, vertex and true-edge tests using Fraction arithmetic. This is a potential change of critical carriers, not a homogeneous physical realization.

## Two-anchor theorem, arbitrary finite inner geometry
Every full-dimensional homogeneous convex polytope L contained in K and retaining BOTH original vertices3 and12 has at least two strict unstable equilibria, at those same vertices. There is no restriction on the other vertices, complexity, number of cuts, or how far the remaining material is changed.

Proof of the physical centroid constraint: cone a boundary triangulation of L from a retained vertex a. Each positive-volume tetrahedron has centroid (a+x+y+z)/4 with x,y,z in L. Taking volume-weighted averages proves g(L)=(a+3w)/4 for some w in L, hence w in K. No external centroid theorem or unproved numerical optimizer property is needed.

For each ordered pair (a,b)=(v3,v12),(v12,v3), the source checks all26*25=650 integers

    (4 A_b-A_a-3 A_k) dot (A_j-A_b) < 0, k=0,...,25, j != b,

where v_i=A_i/10^7. Bilinearity extends the signs to all w in K and every nonzero direction x-b with x in K. Thus retaining a forces b to be strictly unstable whenever b also belongs to L. Applying both pairs proves the theorem. The two exact upper bounds on the corresponding physical dot products are respectively

    -1278132894693/400000000000000,
    -88980771159/100000000000000.

This is a sufficient two-anchor obstruction, NOT a claim that two is the minimum possible retained set for every related exclusion. Removing or moving either vertex, changing the outer K, or changing to a sufficiently different affine metric is outside the stated Euclidean exclusion.

The same calculation supplies a metric neighbourhood: for every positive definite G with ||G-I||_op <=1/128 all1300 inequalities remain strict, by Cauchy-Schwarz and the exactly checked lower squared negative cosines. Hence the two-anchor obstruction also holds for affine images having such a metric G=A^T A. The floating cosine printouts (.04705169996644564 and .010414045781915703) are explanatory only; the proof uses rational squares. This does not exclude the entire affine orbit.

## Reconstruction and observed verification
Save the complete code below as inner26_exact_capsule.py, UTF-8 with final newline. Execute:

    python -B -S inner26_exact_capsule.py

Only the Python standard library is used; executed with CPython3.13.5. Source6166bytes SHA256 c6ed60bc2a75d3578a5e6817e701fe6a673289441b7c3c4365f89489585110b8.
Reproduced reference26_exact.json:1122bytes SHA256 de7e2e31598fc995099b53fb8cec263ed8ceef5605dfb2365fb4f5405a554c8d.
Reproduced two_anchor26_exact.json:98948bytes SHA256 c5abb7936149227c6dc39467688509e15dc6ff162c608bd35b787969866f4550. This output contains every one of the1300 literal checked integer inequalities, coordinate numerators, maximizing witnesses, and exact squared cosine bounds.
Expected terminal markers:

    REFERENCE26_EXACT_110_NOT_OWN_OK 1122 de7e2e31598fc995099b53fb8cec263ed8ceef5605dfb2365fb4f5405a554c8d
    TWO_ANCHOR26_EXACT_OBSTRUCTION_OK 98948 c5abb7936149227c6dc39467688509e15dc6ff162c608bd35b787969866f4550 rho 1/128

Hashes identify bytes, not substitute for the complete runnable source provided here. The fixed-reference certificate and the general inner-family theorem are distinct claims.

```python
"""Exact rational reference110 and two-anchor obstruction for literal INNER26.
Own class remains121: the positive110 certificate uses an explicitly different
reference centre. Every inequality is checked with integers or Fractions.
Run: python -B -S inner26_exact_capsule.py
"""
from fractions import Fraction as F
import json,hashlib,math
I=[[4555,1456,-2626],[4532,871,-3396],[2460,1627,-1122],[2071,3232,1738],[2883,1687,-1885],[2020,2624,1975],[4134,253,-4370],[2103,2117,2423],[4013,1436,1842],[3346,559,1440],[2685,-3687,-6337],[5173,-144,-625],[3007,-4469,-6249],[5025,-204,-335],[5458,-174,-3261],[5125,-1002,-1089],[5357,-583,-1139],[4695,962,375],[5135,-3216,-2798],[4249,-5178,-4847],[5891,-1088,-3270],[4680,-4958,-5035],[5094,-4790,-4344],[5197,781,-1894],[5664,-462,-2348],[5718,-2436,-3536]]
faces=[[0,1,6],[14,1,0],[0,4,3],[8,0,3],[0,6,4],[23,0,8],[14,0,23],[14,6,1],[3,4,2],[3,2,10],[2,4,10],[3,5,7],[5,3,10],[3,7,8],[4,6,10],[7,5,10],[6,12,10],[6,20,12],[14,20,6],[7,9,8],[7,19,9],[7,10,12],[7,12,19],[9,18,8],[13,11,8],[11,17,8],[8,18,13],[17,23,8],[9,22,18],[9,19,22],[16,11,13],[16,24,11],[24,17,11],[12,21,19],[20,21,12],[15,16,13],[18,15,13],[20,14,23],[18,16,15],[18,25,16],[20,24,16],[25,20,16],[24,23,17],[22,25,18],[19,21,22],[21,20,25],[20,23,24],[21,25,22]]
def add(a,b):return [x+y for x,y in zip(a,b)]
def sub(a,b):return [x-y for x,y in zip(a,b)]
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def cross(a,b):return [a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]]
def det(a,b,c):return dot(a,cross(b,c))
def outer(a,b):return [[x*y for y in b] for x in a]
def zeros():return [[F(0) for _ in range(3)] for _ in range(3)]

def audit(P,c,faces):
 X=[sub(v,c) for v in P];norms=[];fc=[];fv=[];owners={}
 for j,f in enumerate(faces):
  a,b,d=[X[i] for i in f];n=cross(sub(b,a),sub(d,a));h=dot(n,a);assert h>0;norms.append(n)
  assert all(dot(n,sub(x,a))<0 for i,x in enumerate(X) if i not in f)
  foot=[h*z/dot(n,n) for z in n];vals=[]
  for i,k in zip(f,f[1:]+f[:1]):
   owners.setdefault(tuple(sorted((i,k))),[]).append(j);vals.append(dot(cross(sub(X[k],X[i]),sub(foot,X[i])),n))
  if min(vals)>0:fv.append(j)
  if min(vals)>=0:fc.append(j)
 vc=[];vv=[];vvals={}
 for i,x in enumerate(X):
  ns=sorted({b if a==i else a for a,b in owners if i in (a,b)});vals=[-dot(x,sub(X[k],x)) for k in ns];vvals[i]=min(vals)
  if min(vals)>0:vv.append(i)
  if min(vals)>=0:vc.append(i)
 hc=[];hv=[]
 for (i,j),ff in owners.items():
  assert len(ff)==2;a,b=X[i],X[j];d=sub(b,a);t=-dot(a,d)/dot(d,d);w=add(a,[t*v for v in d]);n,m=[norms[k] for k in ff];nn,mm,nm=dot(n,n),dot(m,m),dot(n,m);D=nn*mm-nm*nm;assert D>0
  alpha=(dot(w,n)*mm-dot(w,m)*nm)/D;beta=(dot(w,m)*nn-dot(w,n)*nm)/D
  if 0<t<1 and alpha>0 and beta>0:hv.append([i,j])
  if 0<=t<=1 and alpha>=0 and beta>=0:hc.append([i,j])
 return dict(S=len(fv),U=len(vv),H=len(hv),strict_faces=[faces[j] for j in fv],strict_vertices=vv,strict_edges=hv,additional_weak=[len(fc)-len(fv),len(vc)-len(vv),len(hc)-len(hv)],edges=len(owners),facets=len(faces))
def reference_main():
 P=[[F(999*r[k]+[4800,300,-2700][k],10**7) for k in range(3)] for r in I];c=[F(444696,10**6),F(-502924,10**6),F(-485197,10**6)];V=F(0);M=[F(0)]*3
 for f in faces:
  a,b,d=[P[i] for i in f];w=det(a,b,d)/6;V+=w
  for k in range(3):M[k]+=w*(a[k]+b[k]+d[k])/4
 g=[m/V for m in M];own=audit(P,g,faces);ref=audit(P,c,faces);assert (ref['S'],ref['U'],ref['H'],ref['additional_weak'])==(1,1,0,[0,0,0]);assert(own['S'],own['U'],own['H'],own['additional_weak'])==(1,2,1,[0,0,0])
 rep=dict(parent='figure-0555',point_rule='(999 I+(4800,300,-2700))/10^7',own_centroid=[str(x) for x in g],volume=str(V),reference=[str(x) for x in c],reference_census=ref,own_census=own,claim='fixed-reference110 only; NOT an own110 construction')
 raw=(json.dumps(rep,sort_keys=True,indent=2)+'\n').encode();open('reference26_exact.json','wb').write(raw);print('REFERENCE26_EXACT_110_NOT_OWN_OK',len(raw),hashlib.sha256(raw).hexdigest())

def two_anchor_main():
 A=[[999*r[k]+[4800,300,-2700][k] for k in range(3)] for r in I];D=10**7;rows=[];summ=[]
 for anchor,target in [(3,12),(12,3)]:
  local=[];angles=[]
  for k,p in enumerate(A):
   r=[4*A[target][i]-A[anchor][i]-3*p[i] for i in range(3)]
   for j,w in enumerate(A):
    if j==target:continue
    d=[w[i]-A[target][i] for i in range(3)];value=sum(r[i]*d[i] for i in range(3));assert value<0
    local.append([anchor,target,k,j,value]);den=sum(x*x for x in r)*sum(x*x for x in d);angles.append((F(value*value,den),k,j))
  rows.extend(local);worst=max(local,key=lambda t:t[-1]);amin=min(angles);summ.append(dict(retained_anchor=anchor,forced_unstable=target,maximum_numerator=worst[-1],maximizing_k_j=worst[2:4],strict_dot_upper=str(F(worst[-1],4*D*D)),minimum_squared_negative_cosine=str(amin[0]),cosine_witness_k_j=list(amin[1:]),number_of_inequalities=len(local)))
  print('PAIR',anchor,target,'upper',F(worst[-1],4*D*D),'mincos',math.sqrt(float(amin[0])))
 assert len(rows)==1300
 # Also give an exact metric-neighbourhood certificate. If ||G-I||op <=1/100,
 # Cauchy-Schwarz bounds the perturbation by ||r||||d||/100.
 # Establish whichever rational rho below is actually supported; no rounded proof.
 mincos2=min(F(s['minimum_squared_negative_cosine']) for s in summ);rho=F(1,1)
 while rho*rho>=mincos2:rho/=2
 for s in summ:assert rho*rho<F(s['minimum_squared_negative_cosine'])
 rep=dict(object='ROOTFREE_INNER26_G4',parent='figure-0555',coordinate_denominator=D,coordinate_numerators=A,pairs=summ,all_inequalities=rows,metric_open_neighbourhood=dict(spectral_norm_bound=str(rho),condition='G positive definite and ||G-I||op <= rho',claim='the same two-anchor obstruction holds after the affine map with G=A^T A'),claim='No own110 inner homogeneous convex polytope retaining BOTH original rows3 and12. Removing/moving either anchor or leaving K is outside this exclusion.')
 raw=(json.dumps(rep,sort_keys=True,indent=2)+'\n').encode();open('two_anchor26_exact.json','wb').write(raw);print('TWO_ANCHOR26_EXACT_OBSTRUCTION_OK',len(raw),hashlib.sha256(raw).hexdigest(),'rho',rho)

if __name__=='__main__':
 reference_main()
 two_anchor_main()
```
