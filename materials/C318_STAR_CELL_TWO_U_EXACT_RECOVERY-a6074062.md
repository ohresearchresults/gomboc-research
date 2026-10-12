# material-a60740621aca

AI research material · [Export notes](../catalog/coverage.md#text-records)

---

# C318 input17 full constant-star-volume replacement-cell obstruction

This is a self-contained recovery capsule for a new exact NEGATIVE RESULT, not a new own110 construction. Exact object: C318_VERTEX55_G3_PRUNE7_OWN121, the 55 literal P1000 rows of material [internal-source-reference] (SHA256 85f9594dab01535e13f4de15c40616a0233549e0157756c10990fd194bb18bdd), NOT C318_PROTECTED15. The original body has V55/E159/F106, C318, own121/weak000. This checker independently reconstructs the proposed full triangular supporting hull and volume centroid; it proves a new continuous-cell exclusion rather than repeating the original complete S/H census.

## Exact conclusion and its scope

Keep every original vertex other than input17 fixed. Move input17 within its complete CLOSED convex replacement cell, subject to keeping the volume of its original incident star constant. This entire two-dimensional cell is a bounded quadrilateral. At every point, BOTH input17 and input0 remain strictly unstable at the ACTUAL filled-volume centroid. Every input17 dot escape against each of the other54 inputs is < -1/50; every input0 escape is < -1/100. Thus none of these bodies is own110. These uniform inequalities include the boundary even when some original triangular facets merge.

This is not an infinitesimal LP claim or a finite sample. It is not a global exclusion for this body, for all isolated moves of unrestricted volume, or for its projective/affine family. Escapes from the theorem include changing star volume, moving local neighbors or guards10/11, changing incidence outside the replacement cell, or coupled changes with a different actual-centroid response.

The reference-center part also proves input17 remains U under any coupled remote changes that preserve the four displayed local inequalities, its fixed star-volume plane, all eight original incident-neighbor coordinates and the reference center. This does NOT automatically extend the physical centroid formula to such coupled moves. Inputs10 and11 occur in the defining guards even though they are not incident neighbors of17.

## Mathematical certificate

Globally check all106 oriented supporting triangles, all159 true edges each with two incident faces, all55 exposed vertices and Euler2. Compute exact uniform volume and centroid, and verify positive centered tetrahedra and zero centered first moments.

For centered old coordinates X, moving vertex v, and oriented incident triangles (v,p,q), define a=sum(p cross q)/6, tau=a dot v_old and B=sum (p+q)(p cross q)^T/24. Constant star volume means a dot v=tau. Four original hull constraints define the complete cell: face/index pairs (19,17),(26,17),(35,17),(36,32). They are respectively original face [4,11,14] tested against17, [7,20,10] against17, [9,14,11] against17 and moving face [9,17,14] against32. Enumerate the four exact intersections and prove boundedness of the two-dimensional recession cone. Every other original hull constraint is affine in v and holds at all four corners, proving equality with the FULL convex replacement cell, not merely a selected outer test.

At the original center, each escape v dot (X_j-v) is a strictly concave quadratic. Its exact maximum over the polygon is found from its constrained plane maximizer, when feasible, and all pairwise corner segments (the boundary edges are included; diagonals remain inside). Every maximum is < -1/50.

For actual filled mass, along this constant-volume plane the star first moment is M_star(v)=(tau I/4+B)v. Therefore c(v)=C(v-v_old), C=(tau I/4+B)/Vol. The full tetrahedral volume/moments are separately recomputed at all four corners and agree with this affine response. For L=I-C and H=(L+L^T)/2, exact Sylvester tests prove H positive definite. Each own-centroid escape (v-c(v)) dot (X_j-v) is a strictly concave quadratic with Hessian -2H. Its exact constrained maximum is found by the H-metric projection onto the star-volume plane and exact maximizers on all corner segments; all54 are < -1/50. Input0's escapes against fixed vertices are affine in v and bounded at the corners. Its one escape against moving17 is bounded with a rational interval product box; all54 are < -1/100.

## Reconstruction, environment and expected output

No originating sandbox, numeric hull library, external file or missing helper is needed. Python3.11.8 standard library was executed. The two literal file blocks below are complete UTF-8 files; save each with exactly one final LF. Reconstruction command is to extract the named blocks to input.json and exact_star.py in one directory. Verification command: `python exact_star.py` (do not run with Python -O, since assertions are the certificate checks).

Input manifest:
- input.json: 1958 bytes, SHA256 5cd9cf50c8574da530c02d1b13d24840c0a9d15562fc8c3fe92e32b2eaebf90b.
- exact_star.py: 9815 bytes, SHA256 28a378195484f0377f0c378108a5c93f7e1097d764ab2d0c02311333cdb9873b.

Reproduced output:
- star_certificate.json: 56111 bytes, SHA256 ba71c4912f7c2279d80459c298b14b85b025a70ff564934e50c8be617305447f.
- Terminal marker: C318_FIXED_STAR_VOLUME_TWO_U_EXCLUSION_PASS 4 54 54 54.
- Volume: 676078799/400000000.
- Exact original centroid: (-3507317369/13521575980000, 296801875987/10141181985000, -834626177527/40564727940000).
- reference_global_max: -0.024698918948030096.
- actual_centroid_global_max: -0.024702262157301254.
- root0_actual_global_upper: -0.017797575558276376.

These rational centroid values, output byte count/hash and decimal diagnostics are the values actually obtained by the stored executable in a fresh recovery directory. Any earlier unpersisted scratch/compaction summary with different centroid fractions, a 58676-byte output or hash b6f253cab6be2cbd70e1c989587292f40032f50d5d849ccdf34bc546a6e2131b9 is NOT this executed certificate and must not replace it. No scientific exact input is to be reconstructed from a summary when this literal source is available.

### File: input.json
```json
{"P1000":[[-681,-206,-1391],[-679,-107,-1396],[-629,-369,-1329],[-617,53,-1375],[-609,92,-1348],[-555,142,-1297],[-428,-626,-982],[-342,333,-1068],[-321,338,1121],[-315,217,1142],[-304,375,-893],[-294,463,1098],[-271,-686,-813],[-239,349,-994],[-218,601,1066],[-188,-34,1135],[-186,-86,1099],[-114,734,1026],[-91,-280,847],[-79,418,-737],[-61,755,986],[-36,517,-404],[-24,657,238],[35,620,-19],[84,-732,-513],[106,708,953],[149,586,-141],[152,-212,955],[146,-111,1077],[234,-715,-454],[267,564,-130],[273,276,-551],[305,-15,1032],[320,-521,5],[438,248,-394],[459,590,333],[459,-379,178],[487,-524,-407],[476,172,-398],[479,338,-279],[499,377,-222],[515,541,29],[519,75,-403],[527,412,-155],[540,-23,-412],[560,-140,-388],[561,463,-57],[609,306,-71],[612,271,-81],[614,92,-155],[618,154,-121],[636,123,260],[642,-336,-135],[660,-55,333],[671,-212,37]],"T":[[0,1,3],[0,8,1],[0,3,2],[0,2,9],[0,9,8],[1,4,3],[1,11,4],[1,8,11],[2,3,37],[2,6,16],[2,29,6],[2,16,9],[2,37,29],[3,4,5],[3,5,13],[3,13,44],[3,45,37],[3,44,45],[4,17,5],[4,11,14],[4,14,17],[5,7,13],[5,17,7],[6,12,18],[6,29,12],[6,18,16],[7,20,10],[7,10,22],[7,19,13],[7,17,20],[7,26,19],[7,23,21],[7,21,26],[7,22,23],[8,9,11],[9,14,11],[9,17,14],[9,16,15],[9,15,28],[9,32,17],[9,28,32],[10,20,22],[12,24,18],[12,29,24],[13,19,46],[13,40,31],[13,31,42],[13,43,40],[13,42,44],[13,46,43],[15,16,28],[16,18,27],[16,27,28],[17,25,20],[17,32,25],[18,24,29],[18,29,27],[19,26,30],[19,30,41],[19,41,46],[20,23,22],[20,35,23],[20,25,35],[21,23,26],[23,35,26],[25,32,35],[26,41,30],[26,35,41],[27,32,28],[27,29,33],[27,36,32],[27,33,36],[29,36,33],[29,37,36],[31,34,38],[31,39,34],[31,38,42],[31,40,39],[32,53,35],[32,36,53],[34,39,38],[35,46,41],[35,51,46],[35,53,51],[36,37,52],[36,52,54],[36,54,53],[37,45,52],[38,39,42],[39,40,42],[40,43,42],[42,43,46],[42,47,44],[42,46,47],[44,49,45],[44,47,48],[44,48,50],[44,50,49],[45,49,52],[46,51,47],[47,54,48],[47,51,53],[47,53,54],[48,54,50],[49,50,52],[50,54,52]]}
```

### File: exact_star.py
```python
"""Exact isolated-star obstruction for C318_VERTEX55_G3_PRUNE7_OWN121.
Standard-library rational checker. input.json contains all 55 literal rows
and all 106 proposed oriented faces. Every face is globally rechecked.
This is NOT an exclusion for changing the star volume, neighboring geometry,
or arbitrary coupled centroid changes. No newly constructed own110 is claimed.
"""
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path
import json,hashlib
ROOT=Path(__file__).resolve().parent

def add(a,b):return tuple(x+y for x,y in zip(a,b))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def scale(a,t):return tuple(t*x for x in a)
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def det(a,b,c):return dot(a,cross(b,c))
def solve3(A,b):
 d=det(*A)
 if d==0:return None
 return scale(add(add(scale(cross(A[1],A[2]),b[0]),scale(cross(A[2],A[0]),b[1])),scale(cross(A[0],A[1]),b[2])),1/d)
def sj(o):
 if isinstance(o,F):return str(o)
 if isinstance(o,(list,tuple)):return [sj(x) for x in o]
 if isinstance(o,dict):return {str(k):sj(v) for k,v in o.items()}
 return o

def run():
 data=json.loads((ROOT/'input.json').read_text());P=[tuple(F(x,1000) for x in p) for p in data['P1000']];T=[tuple(t) for t in data['T']]
 assert len(P)==55 and len(T)==106 and len(set(T))==106
 # Check proposed triangular hull globally and its complete edge closure.
 edge={};D=[]
 for fi,t in enumerate(T):
  a,b,c=(P[i] for i in t);N=cross(sub(b,a),sub(c,a));assert dot(N,N)>0
  values=[dot(N,sub(p,a)) for p in P];assert max(values)==0
  assert set(i for i,v in enumerate(values) if v==0)==set(t)
  for i in range(3):edge.setdefault(tuple(sorted((t[i],t[(i+1)%3]))),[]).append(fi)
  D.append(det(a,b,c))
 assert len(edge)==159 and all(len(v)==2 for v in edge.values())
 assert set(i for t in T for i in t)==set(range(55)) and 55-159+106==2
 d6=sum(D);assert d6>0
 centroid=tuple(sum(D[k]*sum(P[i][j] for i in t) for k,t in enumerate(T))/(4*d6) for j in range(3))
 X=[sub(p,centroid) for p in P];dcenter=[det(*(X[i] for i in t)) for t in T];assert min(dcenter)>0 and sum(dcenter)==d6
 assert all(sum(dcenter[k]*sum(X[i][j] for i in t) for k,t in enumerate(T))==0 for j in range(3))
 m=17;v0=X[m];inc=[t for t in T if m in t];a=(F(0),)*3
 for t in inc:
  k=t.index(m);a=add(a,scale(cross(X[t[(k+1)%3]],X[t[(k+2)%3]]),F(1,6)))
 tau=dot(a,v0);assert tau>0
 def face_value(fi,j,v):
  t=T[fi];q=[v if i==m else X[i] for i in t];p=v if j==m else X[j]
  return dot(cross(sub(q[1],q[0]),sub(q[2],q[0])),sub(p,q[0]))
 def affine(fi,j):
  f0=face_value(fi,j,v0);C=[]
  for k in range(3):
   e=tuple(F(int(i==k)) for i in range(3));C.append(face_value(fi,j,add(v0,e))-f0)
  return tuple(C),f0-dot(C,v0)
 chosen=[(19,17),(26,17),(35,17),(36,32)];lin=[affine(*ij) for ij in chosen]
 assert all(dot(C,v0)+d<0 for C,d in lin)
 def feasible(v):return all(dot(C,v)+d<=0 for C,d in lin)
 vertices=[];pairs=[]
 for i,j in combinations(range(4),2):
  v=solve3([a,lin[i][0],lin[j][0]],[tau,-lin[i][1],-lin[j][1]])
  if v is not None and feasible(v):vertices.append(v);pairs.append([i,j])
 assert len(vertices)==4 and len(set(vertices))==4
 # No nonzero boundary direction of the two-dimensional recession cone
 # satisfies all inequalities. The projected normals span the plane.
 assert any(det(a,lin[i][0],lin[j][0])!=0 for i,j in combinations(range(4),2))
 for C,_ in lin:
  h=cross(a,C);assert dot(h,h)>0
  for s in [F(-1),F(1)]:assert any(dot(D,scale(h,s))>0 for D,_ in lin)
 # Every original hull inequality is valid at all four vertices, hence
 # throughout this polygon (affine under this isolated vertex replacement).
 all_linear=[]
 for fi,t in enumerate(T):
  for j in (range(len(X)) if m in t else [m]):
   if j in t:continue
   C,d=affine(fi,j);all_linear.append((C,d))
   assert all(dot(C,v)+d<=0 for v in vertices)
 # The four-plane relaxation is therefore exactly the full closed cell.
 neighbors=sorted(set(i for t in inc for i in t if i!=m));assert neighbors==[4,5,7,9,14,20,25,32]
 extrema=[]
 for j in [k for k in range(55) if k!=m]:
  w=scale(X[j],F(1,2));candidate=[]
  plane_projection=add(w,scale(a,(tau-dot(a,w))/dot(a,a)))
  if feasible(plane_projection):candidate.append(plane_projection)
  for p,q in combinations(vertices,2):
   d=sub(q,p);t=dot(sub(w,p),d)/dot(d,d);t=max(F(0),min(F(1),t));candidate.append(add(p,scale(d,t)))
  scores=[dot(v,sub(X[j],v)) for v in candidate];k=max(range(len(scores)),key=scores.__getitem__)
  assert scores[k]<-F(1,50)
  extrema.append({'neighbor':j,'maximum_dot_escape':scores[k],'maximizer':candidate[k]})
 # Actual filled-centroid response along this constant-volume star cell.
 # M_star(v)=(tau I/4+B)v, with B=sum (p+q)(p cross q)^T/24.
 B=[[F(0) for _ in range(3)] for _ in range(3)]
 for t in inc:
  k=t.index(m);p,q=X[t[(k+1)%3]],X[t[(k+2)%3]];s=add(p,q);n=cross(p,q)
  for i in range(3):
   for j in range(3):B[i][j]+=s[i]*n[j]/24
 volume=d6/6
 C=[[((tau/4 if i==j else 0)+B[i][j])/volume for j in range(3)] for i in range(3)]
 L=[[F(i==j)-C[i][j] for j in range(3)] for i in range(3)]
 H=[[(L[i][j]+L[j][i])/2 for j in range(3)] for i in range(3)]
 d=tuple(dot(row,v0) for row in C)
 assert H[0][0]>0 and H[0][0]*H[1][1]-H[0][1]**2>0 and det(*H)>0
 ha=solve3(H,a);assert dot(a,ha)>0
 # Independently recompute the full tetrahedral moments at all corners
 # and confirm the affine centroid formula, not a vertex-average proxy.
 for v in vertices:
  Y=list(X);Y[m]=v;dd=[det(*(Y[i] for i in t)) for t in T];assert sum(dd)==d6
  cc=tuple(sum(dd[k]*sum(Y[i][j] for i in t) for k,t in enumerate(T))/(4*d6) for j in range(3))
  assert cc==tuple(dot(row,sub(v,v0)) for row in C)
 own_extrema=[]
 for j in [k for k in range(55) if k!=m]:
  pj=X[j]
  h=tuple(sum(L[i][k]*pj[i] for i in range(3))-d[k] for k in range(3))
  w=solve3(H,scale(h,F(1,2)))
  plane_projection=add(w,scale(ha,(tau-dot(a,w))/dot(a,ha)))
  candidates=[]
  if feasible(plane_projection):candidates.append(plane_projection)
  for p,q in combinations(vertices,2):
   delta=sub(q,p)
   quadratic=-sum(delta[i]*H[i][k]*delta[k] for i in range(3) for k in range(3));assert quadratic<0
   slope=dot(h,delta)-2*sum(p[i]*H[i][k]*delta[k] for i in range(3) for k in range(3))
   t=max(F(0),min(F(1),-slope/(2*quadratic)))
   candidates.append(add(p,scale(delta,t)))
  def own_escape(v):
   cv=tuple(dot(row,sub(v,v0)) for row in C)
   return dot(sub(v,cv),sub(pj,v))
  scores=[own_escape(v) for v in candidates];k=max(range(len(scores)),key=scores.__getitem__)
  assert scores[k]<-F(1,50)
  own_extrema.append({'other_input':j,'maximum_own_dot_escape':scores[k],'maximizer':candidates[k]})
 # The original dominant root input0 also stays strictly unstable.
 # For fixed other vertices each own escape is affine in the moving v;
 # the one moving target is bounded by a rational interval box.
 r=X[0];corner_centers=[tuple(dot(row,sub(v,v0)) for row in C) for v in vertices]
 root0_bounds=[]
 for j in range(1,55):
  if j==m:continue
  ub=max(dot(sub(r,cc),sub(X[j],r)) for cc in corner_centers)
  assert ub<-F(1,100)
  root0_bounds.append({'other_input':j,'upper_bound':ub})
 moving_bound=F(0)
 for k in range(3):
  aa=[min(r[k]-cc[k] for cc in corner_centers),max(r[k]-cc[k] for cc in corner_centers)]
  bb=[min(v[k]-r[k] for v in vertices),max(v[k]-r[k] for v in vertices)]
  moving_bound+=max(x*y for x in aa for y in bb)
 assert moving_bound<-F(1,100)
 root0_bounds.append({'other_input':m,'upper_bound':moving_bound})
 assert all(dot(r,sub(p,r))<-F(1,100) for j,p in enumerate(X) if j not in [0,m])
 assert all(dot(r,sub(v,r))<-F(1,100) for v in vertices)
 report={'object':'C318_VERTEX55_G3_PRUNE7_OWN121','moving_input':17,'VEF':[55,159,106],'volume':d6/6,'centroid':centroid,'fixed_star_volume_normal':a,'fixed_star_volume':tau,'four_inequalities':[{'face':list(T[fi]),'tested_vertex':j,'C':lin[k][0],'d':lin[k][1]} for k,(fi,j) in enumerate(chosen)],'cell_vertices':vertices,'cell_active_pairs':pairs,'extrema':extrema,'uniform_strict_bound':'-1/50','persistent_other_U_input':0,'root0_own_upper_bounds':root0_bounds,'root0_uniform_strict_bound':'-1/100','conclusion':'Every point of this full closed convex constant-star-volume replacement cell has at least two strict U at its actual filled-volume centroid; therefore none is own110.','actual_centroid_response_matrix':C,'own_escape_positive_hessian':H,'own_extrema':own_extrema,'scope':'Holding all other original vertices fixed, and retaining the convex replacement-cell inequalities and the original volume of the input17 star, input17 stays strictly U throughout the closed cell at BOTH the original reference center and its actual filled centroid. The four-inequality outer bound suffices for the reference-center statement whenever those local inequalities and the eight neighbor coordinates persist. This is not an exclusion for changing star volume, moving local neighbors/guards (including inputs10 and11), changing the incident graph beyond this cell, or coupling other changes that move the actual centroid outside the stated affine response.'}
 output=json.dumps(sj(report),indent=2)+'\n';(ROOT/'star_certificate.json').write_text(output)
 print('C318_FIXED_STAR_VOLUME_TWO_U_EXCLUSION_PASS',len(vertices),len(extrema),len(own_extrema),len(root0_bounds))
 print('volume',d6/6,'centroid',*[str(x) for x in centroid])
 print('reference_global_max',max(float(r['maximum_dot_escape']) for r in extrema))
 print('actual_centroid_global_max',max(float(r['maximum_own_dot_escape']) for r in own_extrema))
 print('root0_actual_global_upper',max(float(r['upper_bound']) for r in root0_bounds))
 print('certificate_bytes_sha256',len(output.encode()),hashlib.sha256(output.encode()).hexdigest())
 return report
if __name__=='__main__':run()
```
