# material-f38a5a364722

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

Public derivative: internal-record-identifiers-replaced.

---

# Projective physical mass, polar translation, and exact recovery

This is a reusable analytic/computational method, not a new equilibrium construction. The literal input is ROOTFREE_INNER26_G4 from fully read accepted parent figure-0555, SHA256 e0dc5597e1a1410335dfc2d509e9f92566c0011685d067534d286cd4cb941a0d. Its accepted own121/weak000 mechanics remain unchanged as source authority. The source below contains the actual26 integer rows beginning [4555,1456,-2626], all48 oriented facets, and the exact coordinate rule; no originating sandbox is needed.

## Analytic statement and derivation
Let K be a full-dimensional convex body containing0 in its interior and let d_b(x)=1+b·x be strictly positive on K. Put T_b(x)=x/d_b(x), L_b=T_b(K). The Jacobian determinant is d_b(x)^(-4) in dimension3. Thus V(b)=volume(L_b)=integral_K d_b^(-4), and its first moment is M(b)=integral_K x d_b^(-5). With m=M/V the actual uniform-volume centroid, differentiation under this bounded positive-denominator integral gives

    grad_b log V = -4m,
    Hess_b log V = 20 Cov(L_b) + 4 m m^T,
    D_b m = -5 Cov(L_b) - m m^T.

Cov denotes covariance under uniform volume on L_b, not its vertex cloud. It is positive definite for a full-dimensional body. Consequently log V is strictly convex on the convex positive-denominator domain, and the map b -> m is strictly anti-monotone and injective there. A free chosen reference centre cannot be combined independently with a projective deformation.

For a supporting inequality q·x<=1, substitution x=y/(1-b·y) yields (q+b)·y<=1. Therefore (T_b K)^polar=K^polar+b exactly. Minimizing V(b) is the Santaló translation problem of the polar body (the conventional Santaló point has the opposite sign to b). Its stationary point has actual centroid0. This last relationship is a reformulation of established Santaló geometry, not a novelty claim. Related primary source: Dmitrii Pavlov and Simon Telen, Santaló Geometry of Convex Polytopes, arXiv:2402.18955v2 (24 Nov2024), Introduction equations(1)-(2), on the strictly convex rational dual-volume minimizer. The projective identities above have the displayed direct derivation and the exact check below; they do not depend on numerical optimization or an appeal to that citation.

For an oriented tetrahedron(0,a,b,c) of volume w, its image volume is w/(d_a d_b d_c), its first moment is that volume times(a/d_a+b/d_b+c/d_c)/4, and its raw second moment is that volume times[ss^T+aa^T/d_a^2+bb^T/d_b^2+cc^T/d_c^2]/20, where s=a/d_a+b/d_b+c/d_c. These finite formulas give rational exact identities for rational vertices and rational b.

## Recovery and observed receipts
Save the single code block verbatim as projective_moment_identity.py, UTF-8 with a final newline. Run:

    python -B -S projective_moment_identity.py

Only the Python standard library is used (executed with CPython3.13.5). Expected terminal marker:

    PROJECTIVE_MOMENT_IDENTITY_EXACT_OK 29952 2744b41ff7de0f6fbaabe70352ac3e20ffb642e91cd798b1c0979c2b03257c75

The source file is4283bytes, SHA256 63cff560b71743dc78bf289c491acf985f9dbbbc3607c33c22ab5ab2cbb3fb35. The reproduced projective_moment_identity.json is29952bytes with the SHA256 in the terminal marker. Source and output hashes identify bytes; the complete source is below. The command checks every facet against every other point, the accepted exact input volume, the exact gradient/Hessian identities, positive leading principal minors, and the polar translation inequalities. It does not perform or claim a new equilibrium audit.

```python
"""Exact rational projective-volume/centroid identities; standard library only.
Input: literal ROOTFREE_INNER26_G4 (26 rows, parent figure-0555).
Run: python -B -S projective_moment_identity.py
Output: projective_moment_identity.json and PROJECTIVE_MOMENT_IDENTITY_EXACT_OK.
This verifies moment identities, not a new equilibrium construction.
"""
from fractions import Fraction as F
from itertools import combinations
import json,hashlib
I=[[4555,1456,-2626],[4532,871,-3396],[2460,1627,-1122],[2071,3232,1738],[2883,1687,-1885],[2020,2624,1975],[4134,253,-4370],[2103,2117,2423],[4013,1436,1842],[3346,559,1440],[2685,-3687,-6337],[5173,-144,-625],[3007,-4469,-6249],[5025,-204,-335],[5458,-174,-3261],[5125,-1002,-1089],[5357,-583,-1139],[4695,962,375],[5135,-3216,-2798],[4249,-5178,-4847],[5891,-1088,-3270],[4680,-4958,-5035],[5094,-4790,-4344],[5197,781,-1894],[5664,-462,-2348],[5718,-2436,-3536]]
faces=[[0,1,6],[14,1,0],[0,4,3],[8,0,3],[0,6,4],[23,0,8],[14,0,23],[14,6,1],[3,4,2],[3,2,10],[2,4,10],[3,5,7],[5,3,10],[3,7,8],[4,6,10],[7,5,10],[6,12,10],[6,20,12],[14,20,6],[7,9,8],[7,19,9],[7,10,12],[7,12,19],[9,18,8],[13,11,8],[11,17,8],[8,18,13],[17,23,8],[9,22,18],[9,19,22],[16,11,13],[16,24,11],[24,17,11],[12,21,19],[20,21,12],[15,16,13],[18,15,13],[20,14,23],[18,16,15],[18,25,16],[20,24,16],[25,20,16],[24,23,17],[22,25,18],[19,21,22],[21,20,25],[20,23,24],[21,25,22]]
def add(a,b):return [x+y for x,y in zip(a,b)]
def sub(a,b):return [x-y for x,y in zip(a,b)]
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def cross(a,b):return [a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]]
def det(a,b,c):return dot(a,cross(b,c))
def outer(a,b):return [[x*y for y in b] for x in a]
def zeros():return [[F(0) for _ in range(3)] for _ in range(3)]
def main():
 P=[[F(999*r[k]+[4800,300,-2700][k],10**7) for k in range(3)] for r in I]
 origin=[sum(p[k] for p in P)/len(P) for k in range(3)];X=[sub(p,origin) for p in P]
 for ids in faces:
  a,b,c=[X[i] for i in ids];n=cross(sub(b,a),sub(c,a));assert dot(n,a)>0
  assert all(dot(n,sub(x,a))<0 for i,x in enumerate(X) if i not in ids)
 edges={tuple(sorted(e)) for f in faces for e in ((f[0],f[1]),(f[1],f[2]),(f[2],f[0]))};assert len(edges)==72
 V0=sum(det(*[X[i] for i in f])/6 for f in faces);assert V0==F(112995444835506046059,2*10**21)
 beta=[F(1,3),-F(1,5),F(1,7)];den=[1+dot(beta,x) for x in X];assert min(den)>0
 V=F(0);M=[F(0)]*3;raw2=zeros();dV=[F(0)]*3;d2V=zeros()
 for ids in faces:
  x=[X[i] for i in ids];d=[den[i] for i in ids];w=det(*x)/(6*d[0]*d[1]*d[2]);y=[[xx/di for xx in xi] for xi,di in zip(x,d)];s=[sum(yi[k] for yi in y) for k in range(3)]
  V+=w
  for k in range(3):M[k]+=w*s[k]/4;dV[k]-=w*s[k]
  for k in range(3):
   for l in range(3):
    term=s[k]*s[l]+sum(yi[k]*yi[l] for yi in y);raw2[k][l]+=w*term/20;d2V[k][l]+=w*term
 m=[v/V for v in M];cov=[[raw2[k][l]/V-m[k]*m[l] for l in range(3)] for k in range(3)]
 grad=[v/V for v in dV];hess=[[d2V[k][l]/V-grad[k]*grad[l] for l in range(3)] for k in range(3)]
 assert grad==[-4*x for x in m]
 assert hess==[[20*cov[k][l]+4*m[k]*m[l] for l in range(3)] for k in range(3)]
 minors=[hess[0][0],hess[0][0]*hess[1][1]-hess[0][1]**2,det(*hess)];assert all(t>0 for t in minors)
 # Polar translation identity: q_f -> q_f+beta, with q_f=n/(n dot a).
 Y=[[xx/di for xx in x] for x,di in zip(X,den)]
 for f in faces:
  a,b,c=[X[i] for i in f];n=cross(sub(b,a),sub(c,a));q=[z/dot(n,a) for z in n];qp=add(q,beta)
  assert all(dot(qp,Y[i])==1 for i in f)
  assert all(dot(qp,Y[i])<1 for i in range(len(Y)) if i not in f)
 def conv(v):
  if isinstance(v,list):return [conv(t) for t in v]
  return str(v)
 report=dict(parent='figure-0555',V0=str(V0),origin=conv(origin),beta=conv(beta),minimum_denominator=str(min(den)),volume=str(V),centroid=conv(m),gradient_log_volume=conv(grad),hessian_log_volume=conv(hess),positive_principal_minors=conv(minors),identities='exact Fraction equality',polar_translation='all48 facets and all26 points checked',equilibrium_claim='none')
 data=(json.dumps(report,sort_keys=True,indent=2)+'\n').encode();name='projective_moment_identity.json';open(name,'wb').write(data)
 print('PROJECTIVE_MOMENT_IDENTITY_EXACT_OK',len(data),hashlib.sha256(data).hexdigest())
if __name__=='__main__':main()
```
