# material-96f01bb0253c

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

Public derivative: internal-record-identifiers-replaced.

---

# Complete finite numerical methods for pruned T43 hinges

Exact input dependencies: [internal-source-reference], SHA fde677e1eca6e3e71b0704b641312b81b6a1622e7440061dc1f6b8ca43b86a2d, contains complete hinge_atlas.py2289bytes SHA f8e19b2d6f5f5ae1aaddb4fabbc4e38126332de881c881b68caeadd1328d3e5b and hinge_numeric.py5594bytes SHA2ce18301abf87c61abb48db371ec249159326abf61346deab14a208a6cfb8728. Supply that entire material along with this one. The two files below import those exact units. Meaningful exact nonrecord outputs are independently self-contained in [internal-source-reference]; they do NOT need this numerical method to reconstruct.

These are numerical discovery methods, not exact equilibrium certificates. They take the convex hull of the moved old vertices WITHOUT adding section vertices, and recompute actual uniform filled mass at every evaluation. Full-dimensional hulls with<=43 vertices automatically have E<=123,C<=246. That upper bound says nothing about the equilibrium class. Do not use the determinant-one full-hinge mass law for these pruned bodies.

Save each named code block with final newline. Current verified environment: CPython3.13.5,NumPy2.3.5,SciPy1.17.0,torch2.10.0+cpu. The integer-normal method uses PCG64 seed92643, integer n in[-3,3]^3,w in[-20,20]^3, velocity(n cross w)/(20 n.n), and cut offset rounded to1/1000 from a uniformly sampled .04..96 projection quantile. Run `python pruned_rational_screen.py 30000`. The latest saved checkpoint processed28000 and held199 candidates; it was not a completed30k run. It nominated no S1/U1, S1/U2 or S2/U1. All retained candidates had S2/U2 with both screened bar depths below the baseline. Two exact useful controls, iterations5196 and14875, are recovered and audited in [internal-source-reference]. No total-family exclusion is inferred from this finite screen. The literal controls, not a stochastic rerun, define the preserved bodies.

The ten-variable method uses a free hinge plane/tangent velocity and an SL(3) lower-triangular affine map, true hull/mass automatic differentiation, radius-ordered primal and polar escape deficits with margin1e-5, PCG64 seed260926, SLSQP maxiter400,ftol1e-11. `python pruned_hinge_search.py 0 6` performs six starts. The inspected output had positive losses[3.6743614983509003,3.963168316711009,3.731954323038396,3.6108212366303434,3.2397584872285896,3.8646565382625804] and numerical(S,U)[(6,2),(2,2),(3,6),(2,4),(2,6),(4,2)], so no goal nomination. These are failed finite local searches, not proofs about the ten-parameter family.

Important limitations: Qhull triangulations/rounding of duplicate polar rows at10 decimals are discovery conveniences. The imported all-pair chord screen suppresses positive depths<=1e-12. Exact accepted controls instead reconstruct true facets/edges and retain every positive bar, with all strict and closed S/U/H predicates. The variables named strict_numerical are inferred from this screened barcode and are not a complete weak audit. Small loss or a solver status0 is not success.

## pruned_rational_screen.py
2505bytes SHA256 de29ccac286895b8efc16f0c899e06e52b07af5237cb59b27b2d640c8aebb041.
```python
"""Finite rational-normal pruned-hinge discovery; own hull and mass each trial."""
import os
os.environ['OPENBLAS_NUM_THREADS']='1'
import numpy as np,json,time,sys
from scipy.spatial import ConvexHull,QhullError
from hinge_atlas import P
from hinge_numeric import bar
X=np.array(P,float)/1000

def audit_float(Y):
 h=ConvexHull(Y);f=h.simplices.copy();sg=np.einsum('ij,ij->i',np.cross(Y[f[:,1]]-Y[f[:,0]],Y[f[:,2]]-Y[f[:,0]]),h.equations[:,:3]);f[sg<0]=f[sg<0][:,[0,2,1]]
 q=Y[h.vertices].mean(0);R=Y-q;t=R[f];d=np.einsum('ij,ij->i',t[:,0],np.cross(t[:,1],t[:,2]));c=q+np.einsum('i,ij->j',d,t.sum(1))/(4*d.sum())
 Z=Y[h.vertices]-c;N=h.equations[:,:3];s=-h.equations[:,3]-N@c;Q=N/s[:,None]
 _,idx=np.unique(np.round(Q,10),axis=0,return_index=True);Q=Q[sorted(idx)]
 def cnt(B):
  rr=(B*B).sum(1);D=(B@B.T-rr[:,None])/rr[:,None];np.fill_diagonal(D,-np.inf);a=D.max(1)
  return int((a < -1e-9).sum()),float(np.min(abs(a))),a
 U,um,ua=cnt(Z);S,sm,sa=cnt(Q)
 return S,U,um,sm,Z,Q,c,d.sum()/6,len(h.vertices)

if __name__=='__main__':
 count=int(sys.argv[1]) if len(sys.argv)>1 else 30000;rng=np.random.default_rng(92643);hist={};rows=[];best=100;now=time.time()
 for it in range(count):
  n=rng.integers(-3,4,3);w=rng.integers(-20,21,3)
  if not any(n):continue
  nv=n@n;v=np.cross(n,w)/(20*nv)
  pp=X@n;hh=int(round(np.quantile(pp,rng.uniform(.04,.96))*1000));z=pp-hh/1000
  Y=X+np.maximum(0,z)[:,None]*v
  try:S,U,um,sm,Z,Q,c,V,nvert=audit_float(Y)
  except QhullError:continue
  hist[(S,U)]=hist.get((S,U),0)+1
  if S+U<best:best=S+U;print('BEST',it,S,U,um,sm,flush=True)
  if S+U<=4 and um>1e-7 and sm>1e-7:
   pb=bar(Z);qb=bar(Q)
   if len(pb)!=U-1 or len(qb)!=S-1:continue
   if S+U==4 and not (max(pb,default=0)<.5341742685943558 and max(qb,default=0)<.655896727661406):continue
   r={'iteration':it,'n':n.tolist(),'w':w.tolist(),'h_integer':hh,'v_denominator':int(20*nv),'S':S,'U':U,'Pbar':pb,'Qbar':qb,'centroid':c.tolist(),'volume':V,'V':nvert,'min_abs_primal_margin':um,'min_abs_dual_margin':sm}
   rows.append(r);print('CANDIDATE',json.dumps(r),flush=True)
  if it%1000==0:open('/mnt/data/pruned_rational_candidates.json','w').write(json.dumps({'rows':rows,'hist':{str(k):v for k,v in hist.items()},'processed':it},sort_keys=True,indent=2)+'\n')
 open('/mnt/data/pruned_rational_candidates.json','w').write(json.dumps({'rows':rows,'hist':{str(k):v for k,v in hist.items()},'processed':count},sort_keys=True,indent=2)+'\n')
 print('DONE',count,len(rows),hist,'seconds',time.time()-now,flush=True)
```

## pruned_hinge_search.py
4226bytes SHA256 3f4e9793d9154f50adc30a5467e1efe9a49aff7c0f5aa6d0dd98d9c14034758a.
```python
"""Actual-mass low-dimensional, complexity-safe pruned hinge search.
All results here are numerical nominations until an exact rational audit.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import numpy as np,torch,json,sys,time
from scipy.spatial import ConvexHull,QhullError
from scipy.optimize import minimize
from hinge_atlas import P,faces
from hinge_numeric import bar
T=torch.float64;torch.set_num_threads(1)
raw=np.array(P,float)/1000;fi=np.array([f[0] for f in faces]);d=np.einsum('ij,ij->i',raw[fi[:,0]],np.cross(raw[fi[:,1]],raw[fi[:,2]]))
c=np.einsum('i,ij->j',d,raw[fi].sum(1))/(4*d.sum());r=np.sqrt(np.mean(np.sum((raw-c)**2,axis=1)));BASE=torch.tensor((raw-c)/r,dtype=T)

def geometry(t):
 th,ph,h,al,be,aa,bb,s10,s20,s21=t
 z=th*0
 n=torch.stack([ph.cos()*th.cos(),ph.cos()*th.sin(),ph.sin()])
 e1=torch.stack([-th.sin(),th.cos(),z]);e2=torch.stack([-ph.sin()*th.cos(),-ph.sin()*th.sin(),ph.cos()])
 v=al*e1+be*e2
 rawy=BASE+torch.relu(BASE@n-h)[:,None]*v
 A=torch.stack([torch.stack([aa.exp(),z,z]),torch.stack([s10,bb.exp(),z]),torch.stack([s20,s21,(-aa-bb).exp()])])
 Y=rawy@A.T
 hull=ConvexHull(Y.detach().numpy());f=hull.simplices.copy();rawpts=Y.detach().numpy()
 sg=np.einsum('ij,ij->i',np.cross(rawpts[f[:,1]]-rawpts[f[:,0]],rawpts[f[:,2]]-rawpts[f[:,0]]),hull.equations[:,:3]);f[sg<0]=f[sg<0][:,[0,2,1]]
 q=Y[hull.vertices].mean(0);R=Y-q;tt=R[f]
 weights=(tt[:,0]*torch.linalg.cross(tt[:,1],tt[:,2])).sum(1);vol=weights.sum()/6
 com=q+(weights[:,None]*tt.sum(1)).sum(0)/(4*weights.sum());Z=Y-com
 face=Z[f];norm=torch.linalg.cross(face[:,1]-face[:,0],face[:,2]-face[:,0]);height=(norm*face[:,0]).sum(1)
 Q=norm/height[:,None]
 # Qhull facet triangulations are discovery only; explicit duplicate polar rows merged.
 _,idx=np.unique(np.round(Q.detach().numpy(),10),axis=0,return_index=True);Q=Q[sorted(idx)]
 return Z[hull.vertices],Q,Y,com,vol,len(hull.vertices)

def ordered(Z):
 rr=(Z*Z).sum(1);D=Z@Z.T-rr[:,None];order=torch.argsort(rr.detach());mask=torch.zeros_like(D,dtype=torch.bool)
 for k in range(len(order)-1):mask[order[k],order[k+1:]]=True
 vals=(D/rr[:,None]).masked_fill(~mask,-1e8).max(1).values
 return vals[order[:-1]]

def report(t):
 with torch.no_grad():
  P,Q,Y,c,V,n=geometry(torch.tensor(t,dtype=T))
  out={'t':list(map(float,t)),'vertices':Y.numpy().tolist(),'centroid':c.numpy().tolist(),'volume':float(V),'V':n,'Pbar':bar(P.numpy()),'Qbar':bar(Q.numpy())}
  out['strict_numerical']=[len(out['Qbar'])+1,len(out['Pbar'])+1]
  return out

class Fun:
 def __init__(self,power=1,margin=1e-5):self.power=power;self.margin=margin;self.calls=0;self.best=(1e100,None)
 def __call__(self,x):
  t=torch.tensor(x,dtype=T,requires_grad=True)
  try:P,Q,*_=geometry(t)
  except (QhullError,RuntimeError):return 1e5,np.zeros_like(x)
  pd=torch.relu(self.margin-ordered(P));qd=torch.relu(self.margin-ordered(Q))
  # First-order ordered deficits; no unconstrained-neighbour near-duplicate shortcut.
  loss=(pd**self.power).sum()+(qd**self.power).sum()
  val=float(loss.detach());loss.backward();g=t.grad.detach().numpy();self.calls+=1
  if np.isfinite(val) and val<self.best[0]:self.best=(val,x.copy())
  return val,g

if __name__=='__main__':
 start=int(sys.argv[1]) if len(sys.argv)>1 else 0;count=int(sys.argv[2]) if len(sys.argv)>2 else 10
 rng=np.random.default_rng(260926);starts=[]
 for i in range(start+count):
  x=np.zeros(10);x[0]=rng.uniform(-np.pi,np.pi);x[1]=rng.uniform(-1.5,1.5);x[2]=rng.uniform(-.75,.75);x[3:5]=rng.normal(0,.3,2);x[5:]=rng.normal(0,.1,5);starts.append(x)
 bounds=[(-4*np.pi,4*np.pi),(-1.55,1.55),(-2,2),(-4,4),(-4,4),(-1.2,1.2),(-1.2,1.2),(-2,2),(-2,2),(-2,2)]
 rows=[];beg=time.time()
 for i in range(start,start+count):
  fun=Fun(power=1,margin=1e-5)
  sol=minimize(fun,starts[i],jac=True,method='SLSQP',bounds=bounds,options={'maxiter':400,'ftol':1e-11})
  v,x=fun.best;o=report(x);o.update(start=i,loss=v,nfev=fun.calls,status=int(sol.status),nit=int(sol.nit));rows.append(o)
  print(i,'loss',v,'class',o['strict_numerical'],'P',o['Pbar'],'Q',o['Qbar'],'calls',fun.calls,'seconds',time.time()-beg,flush=True)
  open(f'/mnt/data/pruned_{start}_{count}.json','w').write(json.dumps(rows,sort_keys=True,indent=2)+'\n')
```
