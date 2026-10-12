# material-029a73a077b0

AI research material · [Export notes](../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

# Linear reference-mechanics height cone and actual filled-mass closure

This is a complete mathematical derivation plus runnable numerical source/patch capsule. It establishes a useful linear constraint chart, NOT an own110 existence theorem. Its executed continuation produced the separately exactified C366_HEIGHT100_G10 own121 nonwinner. The accepted own110 remains C622.

## Exact derivation

Fix nonzero physical normal directions n_i whose positive hull is R^3, and positive heights h_i. Let P(h)={x:n_i dot x<=h_i}; it is bounded, full-dimensional, and contains0 in its interior. Its polar is conv{q_i=n_i/h_i}.

For a directed arrow i->j,
q_i dot(q_j-q_i)>0 iff (n_i dot n_j)h_i-||n_i||^2 h_j>0.
All denominators are positive, so this is a LINEAR strict height inequality. Choose arrows giving every input index except r a route to r. Along each arrow squared norm strictly increases, because ||q_j||^2=||q_i||^2+2 q_i dot(q_j-q_i)+||q_j-q_i||^2. Consequently q_r is the unique largest-norm input point and a strict unstable vertex of the polar. Every other actual polar vertex has a positive escape to an included point and cannot be unstable or weakly unstable. Thus the physical body has exactly one strict stable facet at the reference0 and no extra stable-weak facets. Input points may disappear into the polar hull or new contacts may form: this argument does not require retaining their original incidences or counting artificial diagonals. It does NOT imply physical U=1.

A moving physical unstable root can also be protected linearly. Choose3 independent owner normals as rows of A, basis heights h_B, and put p(h)=A^{-1}h_B. Extra owner contacts n_i dot p=h_i are linear equalities, all other inequalities h_i-n_i dot p>0 are linear, and lambda=(AA^T)^{-1}h_B>0 is linear. Then p=A^T lambda. For any other x in P,
p dot(x-p)=lambda dot(Ax-h_B)<0,
since equality in all3 independent basis inequalities would force x=p. Hence p is a strict physical unstable vertex. This does not rule out another unstable vertex elsewhere. The conjunction of these constraints with positive heights is a polyhedral open region; fixing one height removes uniform scaling, not shape freedom.

The remaining homogeneous condition is genuinely nonlinear: the ordinary FILLED-volume centroid of P(h) must equal0. It is not the mean of vertices, not a loading choice, and not automatically enforced by the linear cone. A tiny numerical residual is not an exact mass lock. Complete own-centroid rational auditing decides acceptance after freezing.

## Complete source dependencies and environment

Use H_NO_SADDLE.py from [internal-source-reference] for actual hull and differentiable ordinary mass. REFINE_POLAR_PATHS.py below also uses SUPPORT_BEAM.py from [internal-source-reference]. All required helper units are literal in those materials, not merely named local paths. CPython3.13.5, NumPy2.3.5, SciPy1.17.0, Torch2.10.0+cpu; one OpenBLAS/OMP/Torch thread, float64. The exact input checkpoints are the complete rational C288, C318 and C378_GLOBAL65 capsules and their stated dependencies. No archive or random seed is hidden in this method.

HEIGHT_FLOW_MASS.py5630bytes SHA2564551fdd309c6ab629f41541f0fafb7c05bbb7708d2fcfaec961f928792ad7919;
REFINE_POLAR_PATHS.py2901bytes SHA2568771be751cda8e3baa50a2351b9f5f23a1173b09bfcaec134b4ca3a75c3b4ab5;
HEIGHT_FLOW_EQUALITY.py5986bytes SHA2568678dc2ea25a14b9a9a3a443b976bb90364bc3b1e4db2957cd10ce28447703de;
HEIGHT_FLOW_COSINE.py5722bytes SHA2564090919fc4b524f54efc78ae969a670334acd0c9dd1e31e7fe9ee216ecb0973f.

## Exact input recipes and executed finite cases

The consequential producing path starts from the exact65-vector C378_GLOBAL65_G9 POLAR_POINTS.json,2221bytes SHA2b5ecca639ec77327fb6caa3c6d3cd14f9b03fa041b92f5eb9aff5d41e11cbe3 in [internal-source-reference]. Convert each integer vector to binary64 by dividing by its grid, preserving row order, and write {"polar_points": rows} as NUMERICAL.json. Execute `python REFINE_POLAR_PATHS.py NUMERICAL.json refine378_protected.json --protected --maxlinks 100 --logmargin .000001 --protection .00001`. This finite census adds49 protected intermediate points to the65 inputs, total114. The realized numerical polar hull has100 active inputs. Select these with SciPy ConvexHull(polar_points).vertices, preserving that returned order, and write HEIGHT378_INPUT.json with just keys polar_points and physical_root (the latter copied unchanged from refine378_protected.json), canonical sorted JSON/separators(',',':'), no terminal newline. Observed input6161bytes SHAb71f459f3bda4f6abff23c3075f5b6e27af5464dcf847a591e78700b3dbb82b5. The full code and exact upstream integer checkpoint define this deterministic geometric input recipe; no earlier optimizer checkpoint is needed.

Execute `python HEIGHT_FLOW_MASS.py HEIGHT378_INPUT.json height_flow378.json --steps 300 --massweight 1000 --uweight 100 --ballweight 1 --margin .000001 --flow-fraction .001 --root-fraction .001 --lower .1 --upper 10`. This completed63 objective calls, numerical reference S/U1/2 and own S/U1/2, centroid approximately(1.17e-13,9.22e-11,1.70e-10), volume2.08078835584. Full output22020bytes SHA4c601e740bc7caf06d2ab608c189f48e24141a786e7d75dca15b58e556c6338f. Pruning its63 active support vectors and freezing ties-to-even at grid10^10 produced the separately preserved exact C366_HEIGHT100_G10 own121, not own110. All deformations of this100-row chart have E<=294; after pruning to63 rows, the corresponding bound is E<=183.

Other finite cases were also executed, not exclusions. C288 long32 input comes from the complete PROTECTED_ENVELOPE_SCOUT.py and exact C288/RAW.json already preserved. Default HEIGHT_FLOW_MASS with steps300 gave reference1/4, own24/4 and centroid(-.03498,.03329,-.04170), then a line-search stop. Setting uweight=0 and ballweight=0, same300 steps and all other defaults, gave reference1/3, own24/3, centroid(-.0006658,.0014157,-.0010685),1225 objective calls, iteration limit. The explicit mass-equality patch below, applied to that last numerical output with steps200,uweight100,ballweight10,flow-fraction1e-6,root-fraction1e-6,lower.01,upper100 and other defaults, did not improve the centroid and stopped after192 calls. These failures do not prove a height-cone mass obstruction.

For an exact reproducible alternate input, use C318/RAW.json and REFERENCE.json from [internal-source-reference] and C288/A.json. Put g=the exact rational reference, N_i=n_i/(h_i-n_i dot g), root=C288 raw vertex16-g, then convert each rational scalar to binary64. Write canonical JSON {grid:1,polar_points:N,root:root}. Observed4925bytes SHA47590a45300a6d1de914f8de7f51e273ce44cf0e04a30c09cc3d914fcbc50198. Default height search with steps300 completed95 calls without closure: reference1/3, own22/4, centroid(.06727,-.02252,-.01607). Again, no family exclusion follows.

## Essential correction: near-coincident vertices can hide a large global U obstruction

The first height objective normalizes an all-pair escape only by ||p_i||^2. For the nearly mass-closed C366 precursor, two vertices are only3.19e-8 apart; one has local normalized deficit about-7.07e-10. This DOES NOT mean the unwanted unstable basin is close to cancellation. Its numerical physical true-edge global beta is about-.826, while the centered-polar beta is positive about7.6e-7. Independent exact auditing confirms TWO strict unstable vertices, no weak equilibrium. The stable root is not lost, but there is a large physical obstruction elsewhere. This is a failure of that local objective as a distance-to-solution surrogate, not of the exact sign test.

The cosine-normalized patch below replaces that deficit by p_i dot(p_j-p_i)/(|p_i||p_j-p_i|), avoiding the vanishing-length deception. It was executed on height_flow378.json with steps300 and margin1e-5, all other defaults. After1884 calls it ended reference1/4, own29/3 with centroid(.00609,.00130,-.00159), not a solution. A useful next change is explicit growth of the protected root's radial advantage, or joint normal-direction/height deformation, rather than further shrinking the tiny local edge. At the C366 precursor, protected-root radius/other-root radius is only about1.009, explaining why a long opposite physical route can remain expensive.

<!-- FILE HEIGHT_FLOW_MASS.py -->
```python
"""Mass closure inside a LINEAR reference-monostability height cone.
Fixed physical normals n_i, variable positive heights h_i. A polar escape i->j
is equivalent to (n_i.n_j)/(n_i.n_i)*h_i-h_j>0, hence linear in h.
A moving prescribed physical root with a preserved owner star is also protected
by linear height/contact/normal-cone inequalities. Own mechanics is recomputed.
Numerical optimization only; rational whole-hull auditing is still mandatory.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import argparse,json,sys,hashlib,itertools,time
from pathlib import Path
import numpy as np
import torch
from scipy.optimize import minimize,LinearConstraint,Bounds
from H_NO_SADDLE import evaluate

def run(a):
 cfg=json.loads(Path(a.input).read_text());N=np.array(cfg['polar_points']);n=len(N)
 with torch.no_grad():ff,uu,g,V,X,Z,active,edges=evaluate(torch.tensor(N));P=(X+g).numpy()
 pr0=np.array(cfg.get('root',cfg.get('physical_root',P[(P*P).sum(1).argmax()].tolist())))
 owners=np.flatnonzero(abs(N@pr0-1)<1e-7).tolist();cand=[]
 for ids in itertools.combinations(owners,3):
  A=N[list(ids)]
  if abs(np.linalg.det(A))<1e-7:continue
  B=np.linalg.inv(A);pp=B@np.ones(3);C=np.linalg.inv(A@A.T);lam=C@np.ones(3)
  if lam.min()>1e-9:cand.append((float(lam.min()/lam.sum()),ids,B,C))
 assert cand,'No strict root cone basis found.'
 _,basis,B,C=max(cand,key=lambda x:x[0]);basis=list(basis);T=np.zeros((3,n));T[:,basis]=B;root0=T@np.ones(n);R20=root0@root0;norm2=(N*N).sum(1);dr=int(norm2.argmax());DD=N@N.T-norm2[:,None];np.fill_diagonal(DD,-np.inf);parents=DD.argmax(1)
 rows=[];low=[];upp=[]
 for i in range(n):
  if i==dr:continue
  j=int(parents[i]);gap=DD[i,j]/norm2[i];assert gap>0
  row=np.zeros(n);row[i]=(N[i]@N[j])/norm2[i];row[j]-=1;rows.append(row);low.append(a.flow_fraction*gap);upp.append(np.inf)
 for i in owners:
  if i in basis:continue
  row=N[i]@T;row[i]-=1;rows.append(row);low.append(0.);upp.append(0.)
 for i in range(n):
  if i in owners:continue
  row=-N[i]@T;row[i]+=1;gap=float(row.sum());assert gap>0;rows.append(row);low.append(a.root_fraction*gap);upp.append(np.inf)
 for k in range(3):
  row=np.zeros(n);row[basis]=C[k];gap=row.sum();assert gap>0;rows.append(row);low.append(a.root_fraction*gap);upp.append(np.inf)
 # Fix one height to rule out collapse by uniform scaling.
 row=np.zeros(n);row[dr]=1;rows.append(row);low.append(1.);upp.append(1.)
 L=np.array(rows);lower=np.array(low);upper=np.array(upp);eq=np.isfinite(upper);cons=[LinearConstraint(L[eq],lower[eq],upper[eq]),LinearConstraint(L[~eq],lower[~eq],np.inf)];Nt=torch.tensor(N);Tt=torch.tensor(T);calls=0;best=None;hist=[];start=time.time()
 def calc(h):
  Y=Nt/h[:,None];ff,u,g,V,X,Z,active,e=evaluate(Y);P=X+g;root=Tt@h;ir=int(((P.detach()-root.detach())**2).sum(1).argmin());r2=P.square().sum(1);D=(P@P.T-r2[:,None])/r2[:,None];D-=torch.eye(len(P))*1e6;pe=D.max(1).values[torch.arange(len(P))!=ir];ball=torch.relu(r2/root.square().sum()-1)
  return Y,P,Z,g,V,root,pe,ball
 def summary(h):
  with torch.no_grad():
   Y,P,Z,g,V,r,pe,ball=calc(torch.tensor(h));X=P-g
   def counts(Q):
    D=Q@Q.T-Q.square().sum(1)[:,None];D-=torch.eye(len(Q))*1e6;return int((D.max(1).values<0).sum())
   refs=[counts(Y),counts(P)];own=[counts(Z),counts(X)];violation=max(float(np.max(lower-L@h)),float(np.max((L@h-upper)[eq])))
  return dict(polar_points=Y.tolist(),normal_directions=N.tolist(),heights=list(map(float,h)),root=r.tolist(),owners=owners,basis=basis,grid=1,numerical_only=True,summary=dict(reference_SU=refs,own_SU=own,centroid=g.tolist(),volume=V.item(),min_reference_escape=pe.min().item(),max_ball_violation=ball.max().item(),linear_violation=violation,input_supports=n),points=P.tolist())
 def fun(x):
  nonlocal calls,best
  h=torch.tensor(x,requires_grad=True);Y,P,Z,g,V,r,pe,ball=calc(h);loss=a.massweight*g.square().sum()/R20+a.uweight*torch.relu(a.margin-pe).square().sum()+a.ballweight*ball.square().sum();loss.backward();calls+=1;val=loss.item();feas=max(float(np.max(lower-L@x)),float(np.max((L@x-upper)[eq])))<1e-8
  if feas and (best is None or val<best[0]):
   best=(val,x.copy())
   if calls%25==0:
    rr=summary(x);hist.append(dict(call=calls,loss=val,**rr['summary']));Path(a.output).write_text(json.dumps(rr,sort_keys=True,separators=(',',':')));print(calls,val,rr['summary'],flush=True)
  return val,h.grad.numpy()
 x=np.ones(n);res=minimize(fun,x,jac=True,method='SLSQP',bounds=Bounds(np.full(n,a.lower),np.full(n,a.upper)),constraints=cons,options=dict(maxiter=a.steps,ftol=1e-16,disp=False))
 rr=summary(best[1]);Path(a.output).write_text(json.dumps(rr,sort_keys=True,separators=(',',':')));Path(a.output+'.report.json').write_text(json.dumps(dict(arguments=vars(a),calls=calls,history=hist,best_loss=best[0],status=int(res.status),message=str(res.message),input_sha256=hashlib.sha256(Path(a.input).read_bytes()).hexdigest(),elapsed=time.time()-start),sort_keys=True,separators=(',',':')));print('HEIGHT_FLOW_MASS_FINITE_END',calls,best[0],rr['summary'],res.message,flush=True)
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('input');p.add_argument('output');p.add_argument('--steps',type=int,default=1000);p.add_argument('--massweight',type=float,default=1000);p.add_argument('--uweight',type=float,default=100);p.add_argument('--ballweight',type=float,default=1);p.add_argument('--margin',type=float,default=1e-6);p.add_argument('--flow-fraction',type=float,default=.001);p.add_argument('--root-fraction',type=float,default=.001);p.add_argument('--lower',type=float,default=.1);p.add_argument('--upper',type=float,default=10);run(p.parse_args())
```

<!-- FILE REFINE_POLAR_PATHS.py -->
```python
"""Finite shortest equal-angle/geometric-radius polar routes at the recomputed centroid.
Numerical nominations only, no global protected minimum or own-class claim.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import argparse,json,sys,math
from pathlib import Path
import numpy as np
import torch
from H_NO_SADDLE import evaluate
from SUPPORT_BEAM import hullstate

def path(u,z,n):
 ru=np.linalg.norm(u);rz=np.linalg.norm(z);e=u/ru;f=z/rz;co=np.clip(e@f,-1,1);phi=np.arccos(co);v=f-co*e;v/=np.linalg.norm(v)
 return np.array([ru*(rz/ru)**(k/n)*(np.cos(phi*k/n)*e+np.sin(phi*k/n)*v) for k in range(1,n)])
def run(a):
 cfg=json.loads(Path(a.input).read_text());YY=np.array(cfg['polar_points'])
 with torch.no_grad():ff,uv,g,V,X,Y,act,ed=evaluate(torch.tensor(YY));Y=Y.numpy();X=X.numpy();g=g.numpy()
 r=np.linalg.norm(Y,axis=1);dr=int(r.argmax());pr=X[(X*X).sum(1).argmax()];D=Y@Y.T-r[:,None]**2;np.fill_diagonal(D,-np.inf);stable=np.flatnonzero(D.max(1)<-1e-12);chosen=[];allpoints=[];cases=[]
 for i in stable:
  if i==dr:continue
  options=[]
  for j in range(len(Y)):
   if r[j]<=r[i]:continue
   phi=np.arccos(np.clip(Y[i]@Y[j]/(r[i]*r[j]),-1,1));lr=np.log(r[j]/r[i]);n=1
   while n<=a.maxlinks and (phi/n>=np.pi/2 or lr+n*np.log(np.cos(phi/n))<=a.logmargin):n+=1
   if n>a.maxlinks:continue
   Q=path(Y[i],Y[j],n);protect=float((Q@pr).max()) if len(Q) else -1.;options.append((n,protect,j,Q))
  options.sort(key=lambda t:(t[0],t[1]));safe=[o for o in options if o[1]<1-a.protection]
  pick=(safe if a.protected and safe else options)[0] if options else None
  if pick is None:cases.append(dict(start=int(i),impossible_in_finite_cap=True));continue
  n,pro,j,Q=pick;allpoints.extend(Q.tolist());item=dict(start=int(i),end=int(j),links=n,protect=pro,all_min_links=options[0][0],protected_min_links=safe[0][0] if safe else None);cases.append(item);print(item,flush=True)
 new=np.vstack((Y,np.array(allpoints))) if allpoints else Y;out=dict(polar_points=new.tolist(),parent_polar_points=Y.tolist(),reference_origin=g.tolist(),physical_root=pr.tolist(),cases=cases,added=len(allpoints),input_supports=len(new),grid=1,numerical_only=True)
 try:
  from scipy.spatial import ConvexHull
  active=ConvexHull(new).vertices;st,P=hullstate(new[active]);out.update(summary=st,points=P.tolist());print('AFTER_INSERT',st,flush=True)
 except Exception as ex:out['hull_error']=str(ex)
 Path(a.output).write_text(json.dumps(out,sort_keys=True,separators=(',',':')));print('FINITE_PATH_CENSUS',len(stable),len(allpoints),len(new),flush=True)
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('input');p.add_argument('output');p.add_argument('--maxlinks',type=int,default=100);p.add_argument('--logmargin',type=float,default=1e-6);p.add_argument('--protection',type=float,default=1e-5);p.add_argument('--protected',action='store_true');run(p.parse_args())
```

### Exact equality variant patch
```python
from pathlib import Path
import hashlib
b=Path('HEIGHT_FLOW_MASS.py').read_bytes()
assert hashlib.sha256(b).hexdigest()=='4551fdd309c6ab629f41541f0fafb7c05bbb7708d2fcfaec961f928792ad7919'
s=b.decode()
changes=[('from scipy.optimize import minimize,LinearConstraint,Bounds','from scipy.optimize import minimize,LinearConstraint,NonlinearConstraint,Bounds'),('x=np.ones(n);res=minimize(fun,x,jac=True',"def massfun(x):\n  with torch.no_grad():return calc(torch.tensor(x))[3].numpy()\n def massjac(x):\n  return torch.autograd.functional.jacobian(lambda h:calc(h)[3],torch.tensor(x),vectorize=True).numpy()\n cons.append(NonlinearConstraint(massfun,np.zeros(3),np.zeros(3),jac=massjac))\n x=np.ones(n);res=minimize(fun,x,jac=True"),("'HEIGHT_FLOW_MASS_FINITE_END'","'HEIGHT_FLOW_MASS_EQUALITY_FINITE_END'"),('if feas and (best is None or val<best[0]):','key=val+1e8*float(g.detach().square().sum())\n  if feas and (best is None or key<best[0]):'),('best=(val,x.copy())','best=(key,x.copy())')]
for old,new in changes:
 assert s.count(old)==1
 s=s.replace(old,new)
b=s.encode();assert len(b)==5986 and hashlib.sha256(b).hexdigest()=='8678dc2ea25a14b9a9a3a443b976bb90364bc3b1e4db2957cd10ce28447703de'
Path('HEIGHT_FLOW_EQUALITY.py').write_bytes(b)
print('HEIGHT_FLOW_EQUALITY_EXACT_PATCH_PASS')
```
The patch itself was executed and its complete output source hash matched before preservation.

### Exact cosine variant patch
```python
from pathlib import Path
import hashlib
b=Path('HEIGHT_FLOW_MASS.py').read_bytes();assert hashlib.sha256(b).hexdigest()=='4551fdd309c6ab629f41541f0fafb7c05bbb7708d2fcfaec961f928792ad7919';s=b.decode()
a="r2=P.square().sum(1);D=(P@P.T-r2[:,None])/r2[:,None];D-=torch.eye(len(P))*1e6;pe=D.max(1).values[torch.arange(len(P))!=ir];ball=torch.relu(r2/root.square().sum()-1)"
z="r2=P.square().sum(1);eye=torch.eye(len(P));dist=torch.sqrt((P[:,None,:]-P[None,:,:]).square().sum(2)+eye);D=(P@P.T-r2[:,None])/(torch.sqrt(r2)[:,None]*dist);D-=eye*1e6;pe=D.max(1).values[torch.arange(len(P))!=ir];ball=torch.relu(r2/root.square().sum()-1)"
assert s.count(a)==1;s=s.replace(a,z).replace('HEIGHT_FLOW_MASS_FINITE_END','HEIGHT_FLOW_COSINE_FINITE_END');b=s.encode();assert len(b)==5722 and hashlib.sha256(b).hexdigest()=='4090919fc4b524f54efc78ae969a670334acd0c9dd1e31e7fe9ee216ecb0973f';Path('HEIGHT_FLOW_COSINE.py').write_bytes(b)
```
