# material-2b70ce7cf783

AI research material · [Export notes](../catalog/coverage.md#text-records)

---

# J131 — polyhedral reference-centre cells, mass-gap projection, and an exact four-guard circuit

This is coordinator-derived mathematics and an executed exact DETACHED47 policy obstruction. It is NOT a new physical body, an all-policy reference110 exclusion, or a proof that homogeneous own110 is impossible. Canonical own110 remains C622, and E<=249 is still unmet. The method separates the auxiliary choice of reference centre from actual geometric mass closure.

## Exact dependencies and recovery

Mandatory source dependency: J131 recovery part1, material [internal-source-reference],13967B/SHA5ef7761abe1e21f2c93a1c41c838f85e52e12d110f70fd059d649455de972859. Only its complete DETACHED_G6.txt and engine131.py are needed here; parallel131.py and its explicitly stated transcription patch are NOT used by these two new programs. No other old workspace, parent archive or recovery parts2/3 are needed for this computation.

Dependency file identities:
- DETACHED_G6.txt1034B/SHAa5b7cb7cd10de4a8ba08a997945ee3a932385cf03a5e259946be867954772a50.
- engine131.py5318B/SHA57c193dfbdc155935de187e4c6b01f0115bd1dba1c65d89b383076abd0c7f63a.

Save the two complete named Python blocks below beside those two dependency files, preserving terminal newlines. Observed environment: CPython3.13.5,NumPy2.3.5,SciPy1.17.0, one OpenBLAS/OMP thread. Fractions.Fraction performs exact arithmetic. Qhull nominates the parent triangular facets, then the inherited exact engine proves every supporting/incidence sign. There is one exact implementation, not independent dual verification.

The first command reconstructs the exact four-row certificate without running a floating optimizer. The second optionally reproduces the policy nomination and tests the general exact-certificate routines:

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python centre131_exact.py
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python centre131.py
```

Complete new source identities:
- centre131.py6617B/SHAec7cd8b426367f46054f7d59b6cb63af3ddd888d438adef6013bac5788e1f0da.
- centre131_exact.py1841B/SHA0666b974aa3edc42325ec1e8a89f77d7c4e3cdf9f7b0778751aff618cacbcf72.

Observed exact output:
- J131_CENTRE_FOUR_ROW_EXACT.json4103B/SHA13695741c5499f1f9cdf8ae616d6d09c964ef45a04fbdacf57256c70eaf8b3be.
- Terminal J131_FOUR_REFERENCE_GUARDS_INFEASIBLE_ANY_CENTRE_PASS.

Supplementary full nominated-policy output:
- J131_CENTRE_CELL_REPORT.json147973B/SHA87ebebff2ee07fecce4bcd4db6cbfef3178dfa82bd98985bbb2f761ba803d98e.
- Terminal J131_REFERENCE_CENTRE_CELL_CERTIFICATE, status exact_dual, margin upper approximately -.1126516344481102.
- Terminal J131_EXACT_PROJECTION_SYNTHETIC_PASS.

The full numerical nomination may depend on floating solver details; exact four-row reconstruction does not. The source below includes all nondefault settings. A returned no_certificate is a failure to obtain a certificate, not a proof of feasibility or infeasibility. These identities were read from the actual files and the exact four-row driver was reexecuted before this material was stored.

## 1. A fixed witness policy gives linear reference-centre constraints

Fix a rational full-dimensional convex polyhedron with labelled vertices p_i and maximal supporting planes n_f.x<=h_f. Let c be a strictly interior reference centre and set H_f(c)=h_f-n_f.c>0. The corresponding polar vertices are q_f(c)=n_f/H_f(c).

A physical positive chord i->j is equivalent to

(p_i-c).(p_j-p_i)>0,

an affine inequality in c with coefficient a=-(p_j-p_i) and constant b=p_i.(p_j-p_i).

A polar positive chord f->k satisfies

q_f.(q_k-q_f)>0
iff (n_f.n_k)H_f(c)-|n_f|^2 H_k(c)>0,

because its omitted denominator H_f(c)^2 H_k(c) is strictly positive. Thus its affine coefficient and constant are

a=|n_f|^2 n_k-(n_f.n_k)n_f,
b=(n_f.n_k)h_f-|n_f|^2 h_k.

Negating either form gives a strict negative chord guard for a selected root. Add all interiority inequalities. A fixed choice of one outgoing positive chord per nonroot in the physical and polar graphs, together with strict negative global chords from each selected root to every other vertex, therefore gives a rational OPEN POLYHEDRON of reference centres. Positive chords strictly increase squared radius, so a finite graph with these outgoing guards and only one exempt root cannot contain a cycle and every vertex reaches that root. A global positive chord rules out even weak instability, since it implies a positive edge direction in the tangent cone. The negative root inequalities make the selected roots strictly unstable. The polar root is the physical stable facet. Consequently these predicates certify reference S1/U1; no weak edge equilibrium can occur without weak S or U, so the full reference class is110/additionalweak000.

This is a sufficient cell for the SPECIFIED root/witness choice. It is not the union over all possible roots, forests or geometry. Empty one-policy cells do not exclude reference110 with other witnesses. The geometry, density and actual centroid have not changed merely because c changes.

## 2. An exact nearest-centre certificate removes the auxiliary reference choice

Write the strict rows as ell_r(c)=a_r.c+b_r>0. Choose positive rational weights w_r and eta>0 and form the closed robust subcell

C_eta={c:ell_r(c)>=eta*w_r for every r}.

This is a subset of the original strict cell. For the fixed body's rational actual centroid g, minimize |g-c|^2 over a nonempty C_eta. Put A_r=-a_r and B_r=b_r-eta*w_r. A proposed projection x is certified globally by rational data satisfying

A_r.x<=B_r for all r,
A_i.x=B_i for selected active rows i,
g-x=sum_i lambda_i A_i, lambda_i>=0.

For every y in C_eta, (g-x).(y-x)<=0, proving x is the unique nearest point. The normal g-x and offset (g-x).x give a separating direction when g is outside the cell. A minimal conic representation of the projection normal in three dimensions uses at most three linearly independent active normals; solving their rational Gram system makes x and the multipliers rational. This remains an exact certificate even when a floating solver nominated the active rows. The complete code checks feasibility, sign, active equality and stationarity with Fractions.

If V is the exact physical volume, the normalized gap m=|g-x|/V^(1/3) has rational sixth power m^6=(|g-x|^2)^3/V^2. This supplies a fixed-policy distance diagnostic independent of arbitrary movement of c. It does NOT make positive residual a global mass-capacity obstruction: a different policy, root or changed physical body may have a smaller gap or a different feasible cell. No such nearest-cell calculation on the QW49G common-apex body has been executed here; it is a concrete continuation opportunity, not a claimed result.

The executed projection test is only the synthetic cube. With rows +/-c_j+11/10 and eta=1/10,w=1, C_eta=[-1,1]^3. Target(2,2,1/2) projects exactly to(1,1,1/2),distance squared2,active x<=1/y<=1,multipliers1/1,separator normal(1,1,0),offset2. The general code obtains the same exact KKT certificate; the four-row replay checks its explicit algebra without an optimizer.

## 3. Exact four-row circuit: reference-centre motion cannot rescue this policy

For any affine guards ell_r=a_r.c+b_r and positive scales w_r, the system ell_r(c)>=rho*w_r is equivalent to [-a_r,w_r].(c,rho)<=b_r. Nonnegative rational multipliers lambda with

sum lambda_r a_r=0,
sum lambda_r w_r=1

give rho<=sum lambda_r b_r. A negative right side excludes even simultaneous NONNEGATIVE guards for every c, without requiring c to be interior.

On the exact DETACHED47 parent, use this auditor's oriented lexicographically sorted triangular-face indices, NOT an older canonical polar ordering. The following FOUR desired positive guards have such a strictly positive circuit:

physical38->31;
polar79->75;
polar16->17;
polar80->18.

The exact constant and maximum common scaled margin are

-1551583586577962439702192238186433879845565847372257734021513700662011242933
/
13773289612523603298056571328191547477644519056434920165690023596689700000000,

approximately -.1126516344481102. The four-row driver reconstructs all four raw affine forms, their scales, the positive multipliers and the unique four-row optimizing(c,rho), and verifies every equality exactly. Hence geometry or at least one of these four witnesses must change; shifting an auxiliary reference centre alone cannot make this selected policy work.

The full nominated global polar route in the preserved general report is
[16,17,9,11,14,68,79,75,74,72,89,87,83,82,80,18].
It is distinct from the earlier parallel-chart forest131.py route and must not be replaced by a shortened three-link sketch. The chosen physical root is6 and polar elder root18. The four-row optimum is also exactly feasible for all rows of that full nominated policy, so its exact dual bound is attained there. The smaller four-row certificate already suffices for the scoped impossibility and needs no floating route reproduction.

This is NOT an exclusion of other DETACHED47 reference110 centres, other physical/polar witnesses, other root identities or future geometric edits. It supplies a local policy conflict useful for deciding what to release, not a universal nonexistence result. No newly changed homogeneous body or E improvement is produced by this computation.

## File: centre131.py
```python
#!/usr/bin/env python3
"""Rational reference-centre cells, exact LP duals and projection certificates.
Floating solvers nominate supports only; returned certificates are rational.
A selected forest cell is NOT the union of all reference equilibrium cells.
"""
from fractions import Fraction as F
from itertools import combinations
import numpy as np
from scipy.optimize import linprog,minimize,LinearConstraint
from scipy.sparse.csgraph import dijkstra
import engine131 as e
O=F(0)

def solve(A,b):
 n=len(A[0]);rr,piv=e.rref([list(row)+[y]for row,y in zip(A,b)])
 if n in piv or len(piv)!=n:return None
 x=[O]*n
 for k,j in enumerate(piv):x[j]=rr[k][-1]
 if any(e.dot(row,x)!=y for row,y in zip(A,b)):return None
 return x

def row(a,b,label):
 w=max(abs(b),*(abs(x)for x in a))
 assert w>0
 return dict(a=a,b=b,w=w,label=label)

def reference_rows(X,planes,P,Q,uroot,sroot):
 # Each row is a.c+b>0, where c is the raw reference centre.
 rows=[row(e.mul(-1,n),h,('interior',i))for i,(n,h)in enumerate(planes)]
 def primal(i,j,sign):
  d=e.sub(X[j],X[i]);return row(e.mul(-sign,d),sign*e.dot(X[i],d),('physical',i,j,sign))
 def polar(i,j,sign):
  n,h=planes[i];m,k=planes[j];s=e.dot(n,m);nn=e.dot(n,n)
  return row(e.mul(sign,e.sub(e.mul(nn,m),e.mul(s,n))),sign*(s*h-nn*k),('polar',i,j,sign))
 for i,j in enumerate(P):
  if i!=uroot:rows.append(primal(i,j,F(1)))
 rows.extend(primal(uroot,j,F(-1))for j in range(len(X))if j!=uroot)
 for i,j in enumerate(Q):
  if i!=sroot:rows.append(polar(i,j,F(1)))
 rows.extend(polar(sroot,j,F(-1))for j in range(len(planes))if j!=sroot)
 return rows

def margin_dual(rows):
 # -a.c+w*rho <= b. Nonnegative dual with A^T lambda=(0,0,0,1)
 # proves rho <= b.lambda for EVERY c, whether or not an optimum was found.
 A=[list(e.mul(-1,r['a']))+[r['w']]for r in rows];b=[r['b']for r in rows]
 Af=np.array([[float(z/r['w'])for z in a]for a,r in zip(A,rows)]);bf=np.array([float(x/r['w'])for x,r in zip(b,rows)])
 res=linprog([0,0,0,-1],A_ub=Af,b_ub=bf,bounds=[(None,None)]*4,method='highs')
 if not res.success:return dict(status='no_certificate',message=res.message)
 ids=list(np.argsort(res.ineqlin.marginals)[:8]);target=[O,O,O,F(1)]
 for k in range(1,5):
  for I in combinations(ids,k):
   I=list(map(int,I));lam=solve([[A[i][j]for i in I]for j in range(4)],target)
   if lam is None or min(lam)<0:continue
   upper=sum((b[i]*z for i,z in zip(I,lam)),O)
   # Explicit rational identity is the complete upper-bound certificate.
   assert [sum((A[i][j]*z for i,z in zip(I,lam)),O)for j in range(4)]==target
   out=dict(status='exact_dual',active=I,multipliers=lam,margin_upper=upper,linear_identity=target,float_margin=float(res.x[3]),float_centre=res.x[:3].tolist())
   y=solve([A[i]for i in I],[b[i]for i in I]) if k==4 else None
   if y is not None and all(e.dot(a,y)<=z for a,z in zip(A,b)):
    assert y[3]==upper;out['exact_optimum']=y
   return out
 return dict(status='no_certificate',message='No exact nonnegative dual found among nominated supports')

def project(rows,g,eta,feasible):
 # Closed positive-margin cell C: a.c+b >= eta*w. eta>0 makes C a
 # subset of the original STRICT reference-centre cell.
 assert eta>0
 A=[e.mul(-1,r['a'])for r in rows];b=[r['b']-eta*r['w']for r in rows]
 assert all(e.dot(a,feasible)<=z for a,z in zip(A,b))
 if all(e.dot(a,g)<=z for a,z in zip(A,b)):
  return dict(status='exact_projection',point=g,active=[],multipliers=[],distance2=O)
 Af=np.array([[float(z/r['w'])for z in a]for a,r in zip(A,rows)]);bf=np.array([float(x/r['w'])for x,r in zip(b,rows)])
 gf=np.array(g,float);seed=np.array(feasible,float)
 res=minimize(lambda x:(.5*np.dot(x-gf,x-gf),x-gf),seed,jac=True,method='SLSQP',constraints=[LinearConstraint(Af,-np.inf,bf)],options=dict(ftol=1e-13,maxiter=300))
 ids=list(np.argsort(abs(Af@res.x-bf))[:16])
 for k in range(1,4):
  for I in combinations(ids,k):
   I=list(map(int,I));gram=[[e.dot(A[i],A[j])for j in I]for i in I]
   lam=solve(gram,[e.dot(A[i],g)-b[i]for i in I])
   if lam is None or min(lam)<0:continue
   x=list(g)
   for i,z in zip(I,lam):x=list(e.sub(x,e.mul(z,A[i])))
   if any(e.dot(a,x)>z for a,z in zip(A,b)):continue
   assert all(e.dot(A[i],x)==b[i]for i in I)
   d=e.sub(g,x);assert d==tuple(sum((z*A[i][j]for i,z in zip(I,lam)),O)for j in range(3))
   return dict(status='exact_projection',point=x,active=I,multipliers=lam,distance2=e.dot(d,d),separator_normal=d,separator_offset=e.dot(d,x),float_success=bool(res.success))
 return dict(status='no_certificate',message='No exact projection support found among nominated rows',float_success=bool(res.success))

def self_test():
 # C at eta=1/10 is exactly [-1,1]^3. Positive-margin rows start at 11/10.
 rows=[]
 for j in range(3):
  for s in [-1,1]:
   a=[O]*3;a[j]=F(s);r=row(tuple(a),F(11,10),('cube',j,s));r['w']=F(1);rows.append(r)
 cert=project(rows,[F(2),F(2),F(1,2)],F(1,10),[O]*3)
 assert cert['status']=='exact_projection'and cert['point']==[F(1),F(1),F(1,2)]and cert['distance2']==2
 return cert

def main():
 X=e.load();base,fs=e.audit(X);_,planes,edges,vs=e.hull(X);g=base['centroid'];Y=np.array([e.sub(p,g)for p in X],float)
 Z=np.array([e.mul(1/(h-e.dot(n,g)),n)for n,h in planes],float)
 def scores(P):
  W=P@P.T-np.einsum('ij,ij->i',P,P)[:,None];W/=np.einsum('ij,ij->i',P,P)[:,None];np.fill_diagonal(W,-np.inf);return W
 WP,WQ=scores(Y),scores(Z);P=list(map(int,WP.argmax(axis=1)));Q=list(map(int,WQ.argmax(axis=1)))
 ur=base['U'][0];junior=base['Q'][0]['root'];elder=next(i for i in base['S_indices']if i!=junior)
 costs=np.maximum(0,-WQ)+1e-7;np.fill_diagonal(costs,0)
 dist,pred=dijkstra(costs,directed=True,indices=junior,return_predecessors=True);path=[elder]
 while path[-1]!=junior:path.append(int(pred[path[-1]]))
 path=path[::-1]
 for i,j in zip(path,path[1:]):Q[i]=j
 rows=reference_rows(X,planes,P,Q,ur,elder);dual=margin_dual(rows)
 out=dict(parent_centroid=g,selected_physical_root=ur,selected_polar_root=elder,reoriented_global_path=path,physical_policy=P,polar_policy=Q,rows=rows,margin_certificate=dual,projection_synthetic_test=self_test(),scope='One fixed DETACHED47 physical/polar policy. No all-policy centre exclusion; no new physical body or own110.')
 if dual.get('exact_optimum')and dual['exact_optimum'][3]>0:
  c=dual['exact_optimum'][:3];eta=dual['exact_optimum'][3]/2;out['positive_margin']=eta;out['mass_projection']=project(rows,g,eta,c)
 rec=e.write('J131_CENTRE_CELL_REPORT.json',out)
 print('J131_REFERENCE_CENTRE_CELL_CERTIFICATE',rec,dual['status'],float(dual.get('margin_upper',0)),'PATH',path,flush=True)
 print('J131_EXACT_PROJECTION_SYNTHETIC_PASS',flush=True)
if __name__=='__main__':main()
```

## File: centre131_exact.py
```python
#!/usr/bin/env python3
"""Exact four-reference-guard circuit; no floating optimizer is run.
The fixed DETACHED47 geometry is nominated then rationally hull-checked.
"""
from fractions import Fraction as F
import engine131 as e
from centre131 import row,solve
O=F(0)

def main():
 X=e.load();fs,H,E,V=e.hull(X)
 labels=[('physical',38,31),('polar',79,75),('polar',16,17),('polar',80,18)]
 rows=[]
 for kind,i,j in labels:
  if kind=='physical':
   d=e.sub(X[j],X[i]);a=e.mul(-1,d);b=e.dot(X[i],d)
  else:
   n,h=H[i];m,k=H[j];s=e.dot(n,m);nn=e.dot(n,n)
   a=e.sub(e.mul(nn,m),e.mul(s,n));b=s*h-nn*k
  rows.append(row(a,b,(kind,i,j)))
 A=[list(e.mul(-1,r['a']))+[r['w']]for r in rows];b=[r['b']for r in rows]
 target=[O,O,O,F(1)];lam=solve([list(x)for x in zip(*A)],target);assert lam is not None and min(lam)>0
 upper=e.dot(lam,b);assert upper<0
 assert tuple(sum((z*r['a'][j]for z,r in zip(lam,rows)),O)for j in range(3))==(O,O,O)
 assert sum((z*r['w']for z,r in zip(lam,rows)),O)==1
 y=solve(A,b);assert y is not None and y[3]==upper
 # Synthetic Euclidean projection certificate on [-1,1]^3:
 g=(F(2),F(2),F(1,2));p=(F(1),F(1),F(1,2));normal=e.sub(g,p)
 assert normal==(F(1),F(1),O)and e.dot(normal,normal)==2
 out=dict(rows=rows,positive_multipliers=lam,constant_weighted_sum=upper,max_common_scaled_margin=upper,four_row_optimizer=y,statement='The four specified reference-centre guards cannot all be nonnegative at ANY c. This does not exclude other witnesses, routes, geometry or all reference110 centres.',synthetic_projection=dict(target=g,point=p,distance2=F(2),active_inequalities=['x<=1','y<=1'],multipliers=[F(1),F(1)],separator_normal=normal,separator_offset=F(2)))
 rec=e.write('J131_CENTRE_FOUR_ROW_EXACT.json',out)
 print('J131_FOUR_REFERENCE_GUARDS_INFEASIBLE_ANY_CENTRE_PASS',rec,flush=True)
if __name__=='__main__':main()
```
