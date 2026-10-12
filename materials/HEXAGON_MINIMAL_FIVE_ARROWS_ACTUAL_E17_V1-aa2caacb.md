# material-aa2caacb28bf

AI research material · [Export notes](../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

# HEXAGON_MINIMAL_FIVE_ARROWS_ACTUAL_E17_V1

Coordinator-derived exact result. The general local five-arrow bound is SHARP even for consecutive true edges of a convex hexagonal polar face, and this phenomenon occurs at the actual uniform-volume centroid of a true(V,E,F)=(10,17,9) body. No proper110 construction, whole-incidence exclusion or global bound change follows:34<=Cmin<=622 remains.

## 1. Exact local five-arrow obstruction
Take the counterclockwise strictly convex hexagon

p=((3,-2),(4,-1),(0,3),(-4,4),(-3,-1),(-1,-4)), q_i=(p_i,1).

Select its five consecutive boundary arrows0->1->2->3->4->5. All24 nonincident left-of-edge determinants are strictly positive. Write the common inverse metric in blocks N=[[H,k],[k^T,c]], H=[[a,b],[b,d]] positive definite. The arrows are

D0=3a+b-2d+kx+ky,
D1=-16a+20b-4d-4kx+4ky,
D2=-12b+3d-4kx+ky,
D3=-4a+24b-20d+kx-5ky,
D4=-6a+7b+3d+2kx-3ky.

Positive weights w=(236,5,109,10,105) satisfy sum w_i(p_(i+1)-p_i)=0 and

sum w_i D_i=-42a+3b-50d=-tr(HQ), Q=((42,-3/2),(-3/2,50)).

Q is positive definite: its leading minors are42 and8391/4. Thus ALL FIVE WEAK arrows are impossible for every physical SPD N. This includes every finite weak-arrow wall. In any affine embedding of the pole plane the stress is a nonzero rank-two negative-semidefinite3x3 matrix, not a zero certificate.

Every proper subset is strictly feasible on the SAME hexagon. For omitted arrow i use the following H,k, and set c=1+k^T H^-1 k; its Schur complement is exactly1, so N is strictly positive definite:

omit0: H=((1,-1),(-1,3)), k=(-167/4,-59/2), arrows=(-301/4,1,317/2,71/4,1).
omit1: H=((7,-1),(-1,1)), k=(-1/2,-16), arrows=(3/2,-198,1,15/2,1).
omit2: H=((9,7),(7,7)), k=(-201/16,-69/16), arrows=(25/8,1,-273/16,1,61/16).
omit3: H=((1,2),(2,7)), k=(2/5,48/5), arrows=(1,164/5,5,-718/5,1).
omit4: H=((6,3),(3,2)), k=(-197/16,-17/16), arrows=(29/8,1,291/16,1,-487/16).

The source checks every exact matrix, inverse, principal minor and arrow. Hence not only consecutive four-arrow windows but EVERY four-arrow subset passes strictly, while their five-arrow union fails even weakly. Strict convexity, all proper-subsystem inequalities and the negative-definite tangent stress persist on an open neighborhood; the stress weights may be varied continuously by keeping w1,w3,w4 fixed and solving the two displacement equations for w0,w2. Their coefficient determinant is nonzero at this example.

## 2. Why five is the exact universal local support bound
The fully read materials [internal-source-reference] and [internal-source-reference] establish the exact tangent alternative, weak/strict boundary distinction and general bound. The essential argument is included here.

For any coplanar selected arrows, write e_i=p_j-p_i. All local physical constraints are D_i=p_i^T H e_i+k.e_i with H positive definite and k free; an unused normal coefficient c>k^T H^-1 k always completes a genuine SPD N. Eliminating k gives the cone of nonnegative zero-displacement weights. Weak infeasibility is equivalent to a weight vector lambda>=0 with sum lambda e=0 and S=sum lambda sym(p_i e_i^T) nonzero negative semidefinite. Encode every arrow by (e_i,sym(p_i e_i^T)) in R2 direct-sum Sym2, dimension5. Conic elimination reduces any representation of(0,S) to at most five arrow vectors without changing S or nonnegativity. Therefore a weakly infeasible selected system has an infeasible subset of size<=5.

For strict infeasibility while weak feasibility holds, the obstruction is instead a nontrivial nonnegative zero relation among those five-dimensional vectors. An inclusion-minimal positive dependence uses at most6 vectors. If it used6, their rank would be5 and their positive cone would be the whole space, because the strictly positive zero relation lets one shift every real representation to a nonnegative one. That cone would contain(0,-I), contradicting weak feasibility. Thus <=5 also suffices for strict infeasibility. Zero stress is an obstruction only for strict arrows, never for weak arrows.

The explicit hexagon above needs all5 even for weak infeasibility and has strict feasibility of every proper subset. It therefore proves sharpness in BOTH formulations, already among consecutive convex boundary paths. No six-arrow local circuit is needed to witness infeasibility. This is not a theorem that independent local tests decide a global common metric across different primal vertices.

## 3. Every prescribed convex hexagon has an exact own-centred E17 completion
This is an analytical real/existential theorem, not a claim that all prescribed real polygons have rational completions. It extends the actual-centroid construction of the fully read Bright Willow18 parent minimum-0197, SHA a7b006ad09534e46e35a14bb5255b09a5f091f2f1672ad26878cb0d4d6dbfc94, with a DIFFERENT incidence surgery. No parent polygon or body is silently renamed.

Normalize any prescribed strictly convex pole hexagon to q_i=(p_i,1) and its primal apex to A=e3. Let C=conv p_i. The function f(s)=Area((C-s)^*) on int C is strictly convex and proper. Radial integration gives grad f=3 int_(C-s)^* y dy and Hess f=3 int_(S1) uu^T(h_C(u)-s.u)^-4 dtheta>0. Boundary divergence follows because the polar contains a disk of radius1/diam(C) and a point u/delta as delta=h_C(u)-s.u tends to0. Its unique minimizer s* therefore gives a polar polygon B with true area centroid0.

With base support b=(-3s*_x,-3s*_y,-3), the six fixed side supports q_i.x<=1 bound a pyramid. Its base is parameterized by x_xy=(4/3)y, z=-1/3-s*.x_xy, y in B. The area Jacobian is constant, so the base centroid is -A/3 and the true volume centroid is0. The pyramid has(7,12,7). Label B_i as the base vertex incident to side supports q_i,q_(i+1).

First make a small GENERIC truncation of simple base vertex B0, retaining three points on B0A,B0B5,B0B1. This changes the f-vector by(2,3,1), giving(9,15,8), without moving any of the six side planes or the apex.

Next make a PARTIAL truncation at B3, through the EXISTING neighbor B2 and through small interior points R_A on B3A and R_4 on B3B4. The plane removes B3 but preserves B2, replacing the removed vertex by two new vertices. It changes the f-vector by(1,2,1), giving EXACTLY(10,17,9). This is not a second generic truncation, which would instead give(11,18,9).

Here is a direct validity proof, including the nongeneric incidence. Use the global simple-vertex cone coordinates at B3 with axes B2-B3,A-B3,B4-B3. Every point of the current convex body has nonnegative coordinates(alpha,beta,gamma). For R_A=B3+u(A-B3) and R_4=B3+v(B4-B3), the retained side is alpha+beta/u+gamma/v>=1. B2 lies exactly on the plane. Every other old vertex except B3 has beta+gamma>0: only the edge B3B2 has both coordinates zero. Therefore all such vertices are strictly retained for sufficiently small positive u,v. The apex survives and still has all six true incident facets. The generic cut at B0 is disjoint from B3 and does not alter this cone argument.

Repair the ACTUAL centroid by varying the three base-plane coefficients b while keeping the six side supports fixed. At the centred pyramid,

D_b g=-Area(base)/(Vol(pyramid)||b||) E_base[xx^T],

which is invertible since an open base plane not through0 cannot annihilate a nonzero linear functional. Vertices and the actual oriented tetrahedral volume/moment sums are analytic functions of b and the cut fractions, including the zero-cut limits where some cells collapse. First choose a sufficiently small generic truncation and use the implicit-function theorem to restore all3 centroid coordinates. Then introduce the small partial cut and apply it again. The strict finite incidence inequalities above persist uniformly under the coherent base adjustment. This yields an ACTUAL uniformly filled own-centred E17 body with EXACTLY the original six pole vectors, not merely a projectively equivalent hexagon.

There are three generic-cut fractions and two partial-cut fractions. Locally these five completion parameters remain free after the three base coefficients repair the three centroid equations. The original base plane and removed base vertices are recoverable from the final incidence/supports, so the fractions are genuine completion parameters. Allowing the prescribed coplanar hexagon itself to vary gives15 face parameters plus5 completion parameters, a20-dimensional local own-centred chart. The theorem is real/analytic; no uniform cut radius over every possible hexagon and no universal rational fixed-hexagon solution is asserted.

## 4. Complete literal rational actual control
The autonomous source below chooses the pole p from Section1, the rational base parameter

s=(-414693/1000000,-37403/1000000), b=(-3s_x,-3s_y,-3),

and all three generic-cut fractions and both partial-cut fractions equal to1/1000. This s is NOT asserted to be the exact minimizer s*. Instead the source reconstructs every vertex rationally, proves the complete true lattice, calculates the actual volume centroid and accounts for the true pole changes.

Label raw vertices as
0=A,1=B1,2=B2,3=B4,4=B5,5=T_A,6=T_prev,7=T_next,8=R_A,9=R_4,
where the T points lie1/1000 of the way from B0 towards A,B5,B1, and the R points lie1/1000 from B3 towards A,B4. All B_i are given exactly by the three support-plane equations q_i.B_i=q_(i+1).B_i=b.B_i=1. This is a complete finite rational generator; no coordinate row or shape parameter is omitted.

The nine outward maximal facet cycles are
F0=(0,4,6,5),F1=(0,5,7,1),F2=(0,1,2),F3=(0,2,8),F4=(0,8,9,3),F5=(0,3,4),F6=(4,3,9,2,1,7,6),F7=(5,6,7),F8=(9,8,2).

The17 true edges are01,02,03,04,05,08,12,17,28,29,34,39,46,56,57,67,89. Vertex0 has degree6 and vertex2 has degree4; all other vertices have degree3. The source exhausts all supporting vertex triples, merges coplanar triangles, checks strict convexity of every full facet cycle, and exhausts all support-plane triple intersections. Thus no triangulation diagonal is counted as an edge.

Two different real tetrahedral fans, one based at the interior origin and one at apex0 with different facet triangulations, agree exactly in volume, first moments and second moments. The source then subtracts the actual centroid g and verifies a zero new first moment. Actual poles are q_f=n_f/(1-n_f.g) from this ONE centroid. Their entire polar lattice is checked, and the six side poles form the ENTIRE true polar face at vertex0.

Set h0=1-gz,t=gxy/h0, phat_i=p_i/(1-p_i.t), Lg=(1/h0)[[1,0,0],[0,1,0],[tx,ty,1]]. Then actual q_i=Lg(phat_i,1). Keep weights1,3,4 equal to5,10,105 and solve exactly for weights0,2 from zero displacement among the actual phat edges. Allfive weights remain strictly positive and the actual tangent stress remains positive definite. The original five H,k witnesses retain every required strict arrow after transport Nactual=Lg^-T Nchart Lg^-1, Mactual=Nactual^-1. Hence the actual own-centred E17 body is minimally infeasible with FIVE true local arrows, not merely its raw uncentred pyramid.

Full physical strict censuses for the five proper-subsystem witnesses are222,323,323,323,222, allweak000 and all340 true edge primitives nonzero. These are not U1 or110.

Three additional rational proper-subsystem metrics also make the true degree6apex itself STRICT U. In actual phat coordinates choose
omit0: H=((86,85),(85,100)), f=(23/6,-13/12);
omit2: H=((43,45),(45,50)), f=(4/5,-1/10);
omit3: H=((1,2),(2,7)), f=(8/3,-2).

Put k=-Hf and normal Schur complement1. Each f lies strictly inside the actual hexagon; Nchart^-1 e3=(f,1), so apex instability follows with the same physical reciprocal metric. The actual complete censuses are respectively222,233,345, allweak000. All544 primitives across all8 records are nonzero. No analogous apical witness or impossibility theorem is claimed for omitted1 or4, and no complete-U1 witness is claimed for any omission. Thus five-support sharpness after imposing FULL U1 remains a separate global question.

A verified topological dual tree with root5 has parents(1,2,3,4,5,5,0,0,3), containing all five arrows. Its primal complement is04,12,17,29,34,39,57,67,89; apex0 is a leaf via04. This shows an actual true-tree domain to which the gate applies, but the domain's physical signs are INFEASIBLE, not an asserted110 continuation.

## 5. Consequences and scope
For(V,E,F)=(10,17,9), the true vertex degree excess is sum(deg(v)-3)=4, so every degree is<=7. At a high-degree vertex, selected local pole-arrow infeasibility always has support<=5, and this cannot be reduced to4 even under actual homogeneous-centroid E17 incidence. The six-gon example settles the formerly open local five-versus-four sharpness question. It does not establish that some such gate is necessarily violated by every global proper110 orientation, nor that independently feasible local gates share one global metric.

The general prescribed-hexagon realization is analytical. The finite rational source proves its literal control, actual moments, true incidences, stress, reciprocal witnesses and physical censuses; it does not formalize the implicit-function theorem or enumerate all convex hexagons. The construction has C34 but NOT the target equilibrium class. No new attaining110 object or global lower-bound increase is claimed.

## 6. Complete source-only recovery and executed evidence
Save the entire fence below as hexagon_five.py, UTF-8/LF including its final LF. CPython3.13.5 standard library, assertions enabled. No parent file, package, solver, random seed, network or exploratory search is needed.

python -B -S hexagon_five.py build > build.stdout
python -B -S hexagon_five.py check > check.stdout
cmp build.stdout check.stdout

Coordinator executed both commands and repeated build/check from a fresh directory containing ONLY the source. The reports and stdout matched byte-for-byte. This is exact source-only regeneration, not an independently written verifier or proof-assistant formalization.

hexagon_five.py:11755bytes SHA2564c113fb5c4f9307f2219df999b02ac6ec5320040db51365de8f649323a931380
hexagon_five.json:376033bytes SHA256bfc26aa4c7de6622e7c1d4dcf75cfa2c957576bb724884a1184e6d3db61bca44
build.stdout=check.stdout:707bytes SHA256eb473b676eb7a84f402c4831efe0eaa94cb72bf38c2c44e8c6a705f663e5cb4b

Expected final markers include CONVEX_HEXAGON_FIVE_WEAK_ARROWS_IMPOSSIBLE_POSITIVE_ND_STRESS_PASS, EVERY_PROPER_FOUR_ARROW_SUBSET_STRICT_RATIONAL_SPD_PASS, ACTUAL_E17_TRUE_DEGREE6_FULL_POLAR_FACE_OWN_VOLUME_CENTROID_PASS, ALL_544_TRUE_PRIMITIVES_NONZERO_WEAK000_PASS and NO_110_CONSTRUCTION_NO_GLOBAL_BOUND_CHANGE.

```python
#!/usr/bin/env python3
"""Sharp five-arrow convex-hexagon obstruction and an actual E17 realization.
CPython 3.13.5 standard library. python -B -S hexagon_five.py build|check
All proof inputs are literal rational data. No optimizer or probe is a dependency.
"""
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path
import hashlib,json,sys

P=((3,-2),(4,-1),(0,3),(-4,4),(-3,-1),(-1,-4))
W=(236,5,109,10,105)
DATA=(
 (((1,-1),(-1,3)),('-167/4','-59/2')),
 (((7,-1),(-1,1)),('-1/2',-16)),
 (((9,7),(7,7)),('-201/16','-69/16')),
 (((1,2),(2,7)),('2/5','48/5')),
 (((6,3),(3,2)),('-197/16','-17/16')),
)
APEX_DATA=(
 (0,((86,85),(85,100)),('23/6','-13/12')),
 (2,((43,45),(45,50)),('4/5','-1/10')),
 (3,((1,2),(2,7)),('8/3',-2)),
)
SBASE=(F(-414693,1000000),F(-37403,1000000))
CUT=F(1,1000)

def v(a):return tuple(F(x) for x in a)
def add(a,b):return tuple(x+y for x,y in zip(a,b))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def mul(t,a):return tuple(t*x for x in a)
def dot(a,b):return sum((x*y for x,y in zip(a,b)),F(0))
def cross2(a,b):return a[0]*b[1]-a[1]*b[0]
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def det(A):
 if len(A)==1:return A[0][0]
 return sum(((-1)**j*A[0][j]*det(tuple(tuple(r[k] for k in range(len(A)) if k!=j) for r in A[1:])) for j in range(len(A))),F(0))
def transpose(A):return tuple(zip(*A))
def mv(A,b):return tuple(dot(r,b) for r in A)
def mm(A,B):return tuple(tuple(dot(r,c) for c in transpose(B)) for r in A)
def inv(A):
 n=len(A);B=[list(v(r))+[F(i==j) for j in range(n)] for i,r in enumerate(A)]
 for j in range(n):
  k=next(k for k in range(j,n) if B[k][j]);B[j],B[k]=B[k],B[j]
  B[j]=[x/B[j][j] for x in B[j]]
  for k in range(n):
   if k!=j:
    c=B[k][j];B[k]=[x-c*y for x,y in zip(B[k],B[j])]
 return tuple(tuple(r[n:]) for r in B)
def identity(n):return tuple(tuple(F(i==j) for j in range(n)) for i in range(n))
def minors(A):return [det(tuple(tuple(r[:k]) for r in A[:k])) for k in range(1,len(A)+1)]
def form(A,x,y):return dot(x,mv(A,y))
def serial(a):
 if isinstance(a,F):return str(a)
 if isinstance(a,dict):return {str(k):serial(x) for k,x in a.items()}
 if isinstance(a,(tuple,list)):return [serial(x) for x in a]
 return a

def metric(H,k):
 H=tuple(v(r) for r in H);k=v(k)
 c=1+form(inv(H),k,k)
 N=(H[0]+(k[0],),H[1]+(k[1],),(k[0],k[1],c))
 assert min(minors(N))>0
 M=inv(N);assert mm(N,M)==identity(3)
 return N,M

def stress(p,w):
 E=[sub(p[i+1],p[i]) for i in range(5)]
 assert all(sum((w[i]*E[i][j] for i in range(5)),F(0))==0 for j in range(2))
 return tuple(tuple(-sum((w[i]*(p[i][j]*E[i][k]+p[i][k]*E[i][j])/2 for i in range(5)),F(0)) for k in range(2)) for j in range(2))

def convex(p):
 sl=[cross2(sub(p[(i+1)%6],p[i]),sub(p[j],p[i])) for i in range(6) for j in range(6) if j not in (i,(i+1)%6)]
 assert len(sl)==24 and min(sl)>0
 return sl

def local():
 p=[v(x) for x in P];E=[sub(p[i+1],p[i]) for i in range(5)]
 Q=stress(p,W);assert Q==((F(42),F(-3,2)),(F(-3,2),F(50)))
 assert min(minors(Q))>0
 witnesses=[]
 for om,(H,k) in enumerate(DATA):
  N,M=metric(H,k)
  arrows=[form(N,p[i]+(F(1),),E[i]+(F(0),)) for i in range(5)]
  assert all(d>0 for i,d in enumerate(arrows) if i!=om) and arrows[om]<0
  assert dot(W,arrows)==-sum(N[i][j]*Q[j][i] for i in range(2) for j in range(2))
  witnesses.append(dict(omitted=om,N=N,M=M,leading_minors=minors(N),arrows=arrows))
 return dict(points=p,convexity=convex(p),weights=W,Q=Q,Qminors=minors(Q),witnesses=witnesses)

def rawbody():
 q=[v(p+(1,)) for p in P];A=v((0,0,1));b=(-3*SBASE[0],-3*SBASE[1],F(-3))
 B=[mv(inv((q[i],q[(i+1)%6],b)),v((1,1,1))) for i in range(6)]
 along=lambda x,y:add(x,mul(CUT,sub(y,x)))
 # Generic cut at B0, then partial cut at B3 through existing B2.
 tA,tprev,tnext=(along(B[0],x) for x in (A,B[5],B[1]))
 rA,rnext=(along(B[3],x) for x in (A,B[4]))
 Y=[A,B[1],B[2],B[4],B[5],tA,tprev,tnext,rA,rnext]
 faces=[(0,4,6,5),(0,5,7,1),(0,1,2),(0,2,8),(0,8,9,3),(0,3,4),(6,7,1,2,9,3,4),(5,6,7),(2,8,9)]
 mean=mul(F(1,10),tuple(sum(y[j] for y in Y) for j in range(3)))
 normals=[];orient=[];edgefaces={}
 for fi,f in enumerate(faces):
  n=cross(sub(Y[f[1]],Y[f[0]]),sub(Y[f[2]],Y[f[0]]))
  if dot(n,sub(mean,Y[f[0]]))>0:n=mul(-1,n);f=tuple(reversed(f))
  h=dot(n,Y[f[0]]);assert h>0;n=mul(1/h,n)
  assert all((dot(n,y)==1)==(i in f) for i,y in enumerate(Y))
  assert all(dot(n,y)<1 for i,y in enumerate(Y) if i not in f)
  # Each supplied facet cycle is strictly convex in its own plane.
  for i in range(len(f)):
   for j in range(len(f)):
    if j in (i,(i+1)%len(f)):continue
    assert dot(n,cross(sub(Y[f[(i+1)%len(f)]],Y[f[i]]),sub(Y[f[j]],Y[f[i]])))>0
  for i,j in zip(f,f[1:]+f[:1]):edgefaces.setdefault(tuple(sorted((i,j))),[]).append(fi)
  normals.append(n);orient.append(f)
 assert normals[:6]==q and normals[6]==b
 assert len(edgefaces)==17 and all(len(fs)==2 for fs in edgefaces.values())
 # Exhaust all vertex triples and merge coplanar supporting triangles.
 hull=set()
 for a,b0,c in combinations(range(10),3):
  n=cross(sub(Y[b0],Y[a]),sub(Y[c],Y[a]))
  if n==(0,0,0):continue
  ds=[dot(n,sub(y,Y[a])) for y in Y]
  if max(ds)<=0 or min(ds)>=0:hull.add(frozenset(i for i,d in enumerate(ds) if d==0))
 assert hull==set(map(frozenset,faces))
 # All support-plane triple intersections give precisely the ten vertices.
 found=set()
 for fs in combinations(range(9),3):
  N=tuple(normals[i] for i in fs)
  if det(N)==0:continue
  x=mv(inv(N),v((1,1,1)))
  if all(dot(n,x)<=1 for n in normals):found.add(x)
 assert found==set(Y)
 return Y,normals,orient,edgefaces,B

def mass(Y,faces,o,reverse=False):
 vol=F(0);J=v((0,0,0));T=[[F(0)]*3 for _ in range(3)]
 for face in faces:
  face=face[-1:]+face[:-1] if reverse else face
  for j in range(1,len(face)-1):
   verts=(o,Y[face[0]],Y[face[j]],Y[face[j+1]])
   dv=det(tuple(sub(x,o) for x in verts[1:]))/6;assert dv>=0
   vol+=dv;s=tuple(sum(x[i] for x in verts) for i in range(3));J=add(J,mul(dv/4,s))
   for i in range(3):
    for k in range(3):T[i][k]+=dv*(s[i]*s[k]+sum(x[i]*x[k] for x in verts))/20
 return vol,J,tuple(map(tuple,T))

def census(X,Q,M,N,edges):
 ps={};qs={}
 for (i,j),(k,l) in edges.items():
  for a,b in ((i,j),(j,i)):ps[a,b]=form(M,X[a],sub(X[b],X[a]))
  for a,b in ((k,l),(l,k)):qs[a,b]=form(N,Q[a],sub(Q[b],Q[a]))
 assert len(ps)==len(qs)==34
 assert all(ps.values()) and all(qs.values())
 U=[i for i in range(10) if all(d<0 for (a,b),d in ps.items() if a==i)]
 S=[i for i in range(9) if all(d<0 for (a,b),d in qs.items() if a==i)]
 H=[(i,j) for (i,j),(k,l) in edges.items() if ps[i,j]<0 and ps[j,i]<0 and qs[k,l]<0 and qs[l,k]<0]
 assert len(S)+len(U)-len(H)==2
 return dict(S=S,U=U,H=H,weak=(0,0,0),primal=ps,dual=qs)

def actual():
 Y,normals,faces,edges,B=rawbody()
 V,J,T=mass(Y,faces,v((0,0,0)))
 assert (V,J,T)==mass(Y,faces,Y[0],True)
 g=mul(1/V,J);X=[sub(y,g) for y in Y]
 VC,JC,TC=mass(X,faces,v((0,0,0)))
 assert VC==V and JC==(0,0,0)
 Q=[mul(1/(1-dot(n,g)),n) for n in normals]
 h=1-g[2];t=mul(1/h,g[:2]);Lg=((1/h,F(0),F(0)),(F(0),1/h,F(0)),(t[0]/h,t[1]/h,1/h))
 Li=inv(Lg);Xh=[mv(transpose(Lg),x) for x in X];Qh=[mv(Li,q) for q in Q]
 assert Xh[0]==v((0,0,1)) and all(q[2]==1 for q in Qh[:6])
 ph=[q[:2] for q in Qh[:6]];convexity=convex(ph)
 assert ph==[mul(1/(1-dot(p,t)),v(p)) for p in P]
 # Keep three weights fixed and solve exactly for weights 0 and 2.
 E=[sub(ph[i+1],ph[i]) for i in range(5)];w=list(map(F,W))
 target=mul(-1,add(add(mul(w[1],E[1]),mul(w[3],E[3])),mul(w[4],E[4])))
 w[0],w[2]=mv(inv(transpose((E[0],E[2]))),target)
 assert min(w)>0;QQ=stress(ph,w);assert min(minors(QQ))>0
 # The six pole vertices form the entire actual true polar face at primal apex0.
 assert [i for i,q in enumerate(Q) if dot(X[0],q)==1]==list(range(6))
 # Enumerate the complete polar maximal-face lattice, not only the selected face.
 dualhull=set()
 for a,b,c in combinations(range(9),3):
  n=cross(sub(Q[b],Q[a]),sub(Q[c],Q[a]))
  if n==(0,0,0):continue
  ds=[dot(n,sub(q,Q[a])) for q in Q]
  if max(ds)<=0 or min(ds)>=0:dualhull.add(frozenset(i for i,d in enumerate(ds) if d==0))
 assert dualhull=={frozenset(i for i,f in enumerate(faces) if vtx in f) for vtx in range(10)}
 # A full topological dual tree contains the five-arrow path; its complement is primal.
 dualtree={(0,1),(1,2),(2,3),(3,4),(4,5),(0,6),(0,7),(3,8)}
 assert dualtree <= {tuple(sorted(fs)) for fs in edges.values()}
 primalcomplement=[ij for ij,fs in edges.items() if tuple(sorted(fs)) not in dualtree]
 def tree(n,es):
  assert len(es)==n-1
  seen={0}
  while True:
   more={v for a,b in es for v in (a,b) if a in seen or b in seen}
   new=seen|more
   if new==seen:break
   seen=new
  assert len(seen)==n
 tree(9,dualtree);tree(10,primalcomplement)
 assert [ij for ij in primalcomplement if 0 in ij]==[(0,4)]
 witnesses=[]
 for om,(HH,k) in enumerate(DATA):
  Nh,Mh=metric(HH,k)
  Na=mm(transpose(Li),mm(Nh,Li));Ma=mm(Lg,mm(Mh,transpose(Lg)))
  assert mm(Na,Ma)==identity(3) and min(minors(Na))>0 and min(minors(Ma))>0
  arrows=[form(Na,Q[i],sub(Q[i+1],Q[i])) for i in range(5)]
  assert all(d>0 for i,d in enumerate(arrows) if i!=om) and arrows[om]<0
  assert dot(w,arrows)==-sum(Nh[i][j]*QQ[j][i] for i in range(2) for j in range(2))
  cc=census(X,Q,Ma,Na,edges)
  assert cc==census(Xh,Qh,Mh,Nh,edges)
  witnesses.append(dict(omitted=om,N=Na,M=Ma,arrows=arrows,census=cc))
 apical=[]
 for om,HH,ff in APEX_DATA:
  HH=tuple(v(r) for r in HH);ff=v(ff)
  inside=[cross2(sub(ph[(i+1)%6],ph[i]),sub(ff,ph[i])) for i in range(6)]
  assert min(inside)>0
  kk=mul(-1,mv(HH,ff));Nh,Mh=metric(HH,kk)
  Na=mm(transpose(Li),mm(Nh,Li));Ma=mm(Lg,mm(Mh,transpose(Lg)))
  arrows=[form(Na,Q[i],sub(Q[i+1],Q[i])) for i in range(5)]
  assert all(d>0 for i,d in enumerate(arrows) if i!=om) and arrows[om]<0
  cc=census(X,Q,Ma,Na,edges);assert 0 in cc['U']
  apical.append(dict(omitted=om,H=HH,f=ff,interior_slacks=inside,N=Na,M=Ma,arrows=arrows,census=cc))
 return dict(base_parameter=SBASE,cut=CUT,base_vertices=B,raw_vertices=Y,raw_normals=normals,
             faces=faces,edges=edges,volume=V,centroid=g,raw_second_moment=T,centred_second_moment=TC,
             vertices=X,poles=Q,Lg=Lg,chart_vertices=Xh,chart_poles=Qh,convexity=convexity,
             actual_weights=w,actual_Q=QQ,actual_Qminors=minors(QQ),witnesses=witnesses,apical_witnesses=apical,
             topological_dual_tree=sorted(dualtree),primal_complement=primalcomplement)

def main():
 assert __debug__
 r=dict(identity='HEXAGON_MINIMAL_FIVE_ARROWS_ACTUAL_E17_V1',local=local(),actual=actual())
 b=(json.dumps(serial(r),sort_keys=True,indent=2)+'\n').encode();p=Path('hexagon_five.json')
 if sys.argv[1]=='build':p.write_bytes(b)
 else:assert p.read_bytes()==b
 print('CONVEX_HEXAGON_FIVE_WEAK_ARROWS_IMPOSSIBLE_POSITIVE_ND_STRESS_PASS')
 print('EVERY_PROPER_FOUR_ARROW_SUBSET_STRICT_RATIONAL_SPD_PASS')
 print('ACTUAL_E17_TRUE_DEGREE6_FULL_POLAR_FACE_OWN_VOLUME_CENTROID_PASS')
 print('TWO_TRUE_MASS_FANS_FULL_PRIMAL_AND_POLAR_LATTICES_PASS')
 print('ACTUAL_MINIMAL_FIVE_ARROW_OBSTRUCTION_AND_FIVE_RECIPROCAL_METRICS_PASS')
 print('ACTUAL_CENSUSES',[(len(w['census']['S']),len(w['census']['U']),len(w['census']['H'])) for w in r['actual']['witnesses']])
 print('APICAL_PROPER_SUBSYSTEMS',[(w['omitted'],len(w['census']['S']),len(w['census']['U']),len(w['census']['H'])) for w in r['actual']['apical_witnesses']])
 print('ALL_544_TRUE_PRIMITIVES_NONZERO_WEAK000_PASS')
 print('TOPOLOGICAL_DUAL_TREE_WITH_PRIMAL_APEX_LEAF_NOT_A_FEASIBLE_110_DOMAIN_PASS')
 print('NO_110_CONSTRUCTION_NO_GLOBAL_BOUND_CHANGE')
 print(p.name,len(b),hashlib.sha256(b).hexdigest())
if __name__=='__main__':
 if len(sys.argv)!=2 or sys.argv[1] not in ('build','check'):raise SystemExit('Usage: python -B -S hexagon_five.py build|check')
 main()
```
