"""Free-vertex own-filled-mass search with a combinatorial edge ceiling.
Usage OPENBLAS_NUM_THREADS=1 python simplicial105_autodiff_screen.py C602_A OUT
At most105 input vertices imply E<=309 for every 3D convex hull, independently
of facet triangulation or rational rounding. Numerical proposals only.
"""
import hashlib,json,os,sys
from pathlib import Path
from fractions import Fraction as F
import numpy as np,scipy,torch
from scipy.spatial import ConvexHull,QhullError
from scipy.optimize import minimize
assert __debug__;sys.set_int_max_str_digits(0)
torch.set_num_threads(1);torch.set_num_interop_threads(1);torch.set_default_dtype(torch.float64)
EXPECTED='2426da394eda9520bd30b2b8b3e1f00d043697353bb6bc73658f5983653c11ec'
SEED=2026091505;STARTS=8;N=105;MAXITER=1500;MARGIN=3e-6
B=lambda o:json.dumps(o,sort_keys=True,separators=(',',':')).encode()
def farthest(P,mandatory):
 ids=list(dict.fromkeys(mandatory));d=np.min(np.sum((P[:,None,:]-P[ids][None,:,:])**2,axis=2),axis=1);d[ids]=-np.inf
 while len(ids)<N:
  k=int(np.argmax(d));ids.append(k);d=np.minimum(d,((P-P[k])**2).sum(axis=1));d[ids]=-np.inf
 return sorted(ids)
class Model:
 def __init__(self,n):self.n=n;self.evaluations=0;self.best=None
 def compute(self,z,gradient=True):
  P=np.asarray(z).reshape(-1,3);hull=ConvexHull(P)
  T=hull.simplices.copy();p=P[T];fl=np.einsum('ij,ij->i',np.cross(p[:,1]-p[:,0],p[:,2]-p[:,0]),hull.equations[:,:3])<0;T[fl]=T[fl][:,[0,2,1]]
  X=torch.tensor(P,requires_grad=gradient);idx=torch.tensor(T);tri=X[idx];ds=torch.sum(tri[:,0]*torch.linalg.cross(tri[:,1],tri[:,2]),dim=1);D=ds.sum()
  g=(ds[:,None]*tri.sum(dim=1)).sum(dim=0)/(4*D);Y=X-g
  # All outward plane vertices of the SAME-centre polar; no polar mass substitution.
  t=Y[idx];normals=torch.linalg.cross(t[:,1]-t[:,0],t[:,2]-t[:,0]);heights=(normals*t[:,0]).sum(dim=1)
  assert float(D.detach())>0 and float(heights.detach().min())>0
  Q=normals/heights[:,None]
  # Floating coplanar grouping is for proposal mechanics only. E ceiling needs no grouping.
  qn=Q.detach().numpy();_,select=np.unique(np.round(qn,11),axis=0,return_index=True);select=np.sort(select);Q=Q[torch.tensor(select)]
  def escape(V):
   dif=V[None,:,:]-V[:,None,:];den=torch.linalg.vector_norm(V,dim=1)[:,None]*torch.linalg.vector_norm(dif,dim=2)
   vals=torch.sum(V[:,None,:]*dif,dim=2)/torch.clamp(den,min=1e-30)
   vals=vals.masked_fill(torch.eye(len(V),dtype=torch.bool),-1e30)
   return torch.max(vals,dim=1).values
  u=escape(Y);s=escape(Q);active=torch.zeros(self.n,dtype=torch.bool);active[hull.vertices]=True
  u=torch.where(active,u,torch.ones_like(u));iu=int(torch.argmin(u));is_=int(torch.argmin(s))
  ru=torch.relu(MARGIN-u);rs=torch.relu(MARGIN-s);um=torch.ones_like(ru);sm=torch.ones_like(rs);um[iu]=0;sm[is_]=0
  loss=torch.sum((ru*um)**2)+torch.sum((rs*sm)**2)
  un=u.detach().numpy();sn=s.detach().numpy()
  rec=dict(S=int(sum(sn<0)),U=int(sum(un<0)),primal_second=float(np.sort(un)[1]),polar_second=float(np.sort(sn)[1]),cost=float(loss.detach()),V_est=len(hull.vertices),F_est=len(Q),E_est=len(hull.vertices)+len(Q)-2,uniform_filled_centroid=g.detach().tolist(),ordinary_volume=float(D.detach()/6),U_input_indices=np.flatnonzero(un<0).tolist(),S_input_triangles=T[select][sn<0].tolist(),nearU=np.flatnonzero(abs(un)<1e-9).tolist(),nearS=np.flatnonzero(abs(sn)<1e-9).tolist())
  self.evaluations+=1
  if self.best is None or(rec['S']+rec['U'],rec['cost'])<(self.best['S']+self.best['U'],self.best['cost']):self.best=dict(rec,points=P.tolist(),evaluation=self.evaluations)
  if gradient:
   loss.backward();grad=X.grad.detach().numpy().ravel();assert np.all(np.isfinite(grad));return float(loss.detach()),grad
  return rec

def main(src,out):
 b=src.read_bytes();assert hashlib.sha256(b).hexdigest()==EXPECTED;r=json.loads(b)
 P=np.array([[float(F(x))for x in p]for p in r['raw_vertices']]);P-=np.array([float(F(x))for x in r['raw_centroid']])
 apex=r['unstable_vertices'][-1];stable=r['faces'][r['stable_face_ids'][0]];rng=np.random.default_rng(SEED);rows=[]
 for k in range(STARTS):
  forced=[apex] if k%2==0 else stable+[apex];ids=farthest(P,forced)
  eps=[1e-5,1e-5,1e-4,1e-4,1e-3,1e-3,.01,.01][k];initial=P[ids]+rng.normal(0,eps,(N,3));model=Model(N)
  initrec=model.compute(initial,False);print('START105',k,'S/U',initrec['S'],initrec['U'],'cost',initrec['cost'],flush=True)
  bounds=list(zip(initial.ravel()-.45,initial.ravel()+.45))
  ans=minimize(model.compute,initial.ravel(),method='L-BFGS-B',jac=True,bounds=bounds,options=dict(maxiter=MAXITER,maxls=40,ftol=1e-16,gtol=1e-10,maxcor=20))
  rec=model.compute(ans.x,False);rec.update(start=k,selected_parent_raw_lex=ids,jitter_sigma=eps,initial_points=initial.tolist(),initial_record=initrec,points=ans.x.reshape(-1,3).tolist(),nit=int(ans.nit),nfev=int(ans.nfev),status=int(ans.status),message=str(ans.message),best_equilibrium_count_seen=model.best,evaluations=model.evaluations)
  rows.append(rec);report=dict(status='NUMERICAL_SIMPLICIAL_105_PROPOSALS_ONLY',input_sha256=EXPECTED,seed=SEED,starts_requested=STARTS,maxiter=MAXITER,margin=MARGIN,numpy=np.__version__,scipy=scipy.__version__,torch=torch.__version__,threads=1,results=rows)
  out.write_bytes(B(report));print('END105',k,'S/U',rec['S'],rec['U'],'cost',rec['cost'],'iter',rec['nit'],'best',model.best['S'],model.best['U'],flush=True)
  if min(rec['primal_second'],rec['polar_second'])>1e-9 and rec['S']==rec['U']==1:print('SIMPLICIAL105_NUMERICAL110_NEEDS_FULL_EXACT_GATE',flush=True);break
 print('SIMPLICIAL105_AUTODIFF_SCREEN_TERMINAL',len(rows),hashlib.sha256(out.read_bytes()).hexdigest(),flush=True)
if __name__=='__main__':main(*map(Path,sys.argv[1:]))
