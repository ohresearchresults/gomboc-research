"""Free105 exact-own-mass proposal search with physical triangular face tests.
Replaces near-coincident-polar-vertex escape penalties with signed foot-to-edge
margins in each outward hull triangle. Float triangulated mechanics only;
any promising body still needs exact MAXIMAL-face and full-edge classification.
"""
import hashlib,json,sys
from pathlib import Path
from fractions import Fraction as F
import numpy as np,scipy,torch
from scipy.spatial import ConvexHull
from scipy.optimize import minimize
import simplicial105_autodiff_screen as parent
assert __debug__;sys.set_int_max_str_digits(0)
SEED=2026091506;STARTS=8;ROUNDS=4;MAXITER=1200;MARGIN=2e-6;SWEIGHT=.1
B=parent.B
class Model:
 def __init__(self,n):self.n=n;self.evaluations=0;self.best=None;self.bestcost=None
 def compute(self,z,gradient=True):
  P=np.asarray(z).reshape(-1,3);hull=ConvexHull(P);assert len(hull.vertices)>=9
  T=hull.simplices.copy();p=P[T];fl=np.einsum('ij,ij->i',np.cross(p[:,1]-p[:,0],p[:,2]-p[:,0]),hull.equations[:,:3])<0;T[fl]=T[fl][:,[0,2,1]]
  X=torch.tensor(P,requires_grad=gradient);idx=torch.tensor(T);tri=X[idx];ds=(tri[:,0]*torch.linalg.cross(tri[:,1],tri[:,2])).sum(dim=1);D=ds.sum();g=(ds[:,None]*tri.sum(dim=1)).sum(dim=0)/(4*D);Y=X-g;t=Y[idx]
  normals=torch.linalg.cross(t[:,1]-t[:,0],t[:,2]-t[:,0]);normals=normals/torch.linalg.vector_norm(normals,dim=1)[:,None];heights=(normals*t[:,0]).sum(dim=1)
  assert float(D.detach())>0 and float(heights.detach().min())>0
  edges=torch.roll(t,-1,dims=1)-t;inward=torch.linalg.cross(normals[:,None,:].expand_as(edges),edges);inward=inward/torch.linalg.vector_norm(edges,dim=2)[:,:,None]
  inside=-(inward*t).sum(dim=2)/heights[:,None];s=inside.min(dim=1).values
  dif=Y[None,:,:]-Y[:,None,:];rel=(Y[:,None,:]*dif).sum(dim=2)/(Y*Y).sum(dim=1)[:,None];rel=rel.masked_fill(torch.eye(self.n,dtype=torch.bool),-1e30);u=rel.max(dim=1).values
  active=torch.zeros(self.n,dtype=torch.bool);active[hull.vertices]=True;u=torch.where(active,u,torch.ones_like(u))
  ru=torch.relu(MARGIN-u);rs=torch.relu(MARGIN+s);um=torch.ones_like(ru);sm=torch.ones_like(rs);um[int(torch.argmin(u))]=0;sm[int(torch.argmax(s))]=0
  loss=((ru*um)**2).sum()+SWEIGHT*((rs*sm)**2).sum();un=u.detach().numpy();sn=s.detach().numpy()
  rec=dict(S=int(sum(sn>0)),U=int(sum(un<0)),primal_second=float(np.sort(un)[1]),face_second_largest=float(np.sort(sn)[-2]),cost=float(loss.detach()),V_est=len(hull.vertices),triangulated_F=len(T),ordinary_volume=float(D.detach()/6),uniform_filled_centroid=g.detach().tolist(),U_input_indices=np.flatnonzero(un<0).tolist(),S_input_triangles=T[sn>0].tolist(),nearU=np.flatnonzero(abs(un)<1e-9).tolist(),nearS=np.flatnonzero(abs(sn)<1e-9).tolist())
  self.evaluations+=1
  if self.best is None or(rec['S']+rec['U'],rec['cost'])<(self.best['S']+self.best['U'],self.best['cost']):self.best=dict(rec,points=P.tolist(),evaluation=self.evaluations)
  if self.bestcost is None or rec['cost']<self.bestcost['cost']:self.bestcost=dict(rec,points=P.tolist(),evaluation=self.evaluations)
  if gradient:
   loss.backward();grad=X.grad.detach().numpy().ravel();assert np.all(np.isfinite(grad));return float(loss.detach()),grad
  return rec

def main(src,out):
 b=src.read_bytes();assert hashlib.sha256(b).hexdigest()==parent.EXPECTED;r=json.loads(b);P=np.array([[float(F(x))for x in p]for p in r['raw_vertices']]);P-=np.array([float(F(x))for x in r['raw_centroid']]);apex=r['unstable_vertices'][-1];stable=r['faces'][r['stable_face_ids'][0]];rng=np.random.default_rng(SEED);rows=[]
 for k in range(STARTS):
  ids=parent.farthest(P,[apex] if k%2==0 else stable+[apex]);eps=[1e-5,1e-5,1e-4,1e-4,1e-3,1e-3,.01,.01][k];initial=P[ids]+rng.normal(0,eps,(105,3));model=Model(105);x=initial.ravel().copy();bounds=list(zip(x-.45,x+.45));init=model.compute(x,False);stages=[]
  print('START_PHYS105',k,'S/U',init['S'],init['U'],'cost',init['cost'],flush=True)
  for j in range(ROUNDS):
   ans=minimize(model.compute,x,method='L-BFGS-B',jac=True,bounds=bounds,options=dict(maxiter=MAXITER,maxls=60,ftol=1e-17,gtol=1e-11,maxcor=20))
   rec=model.compute(ans.x,False);stages.append(dict(round=j,nit=int(ans.nit),nfev=int(ans.nfev),status=int(ans.status),message=str(ans.message),record=rec));x=np.array(model.bestcost['points']).ravel()
   print('PHYS105',k,j,rec['S'],rec['U'],rec['cost'],'iter',ans.nit,'best',model.best['S'],model.best['U'],flush=True)
   if rec['S']==rec['U']==1 and min(rec['primal_second'],-rec['face_second_largest'])>1e-8:break
  row=dict(start=k,selected_parent_raw_lex=ids,jitter_sigma=eps,initial_points=initial.tolist(),initial_record=init,stages=stages,best_equilibrium_count_seen=model.best,best_cost_seen=model.bestcost,evaluations=model.evaluations);rows.append(row)
  report=dict(status='NUMERICAL_PHYSICAL_TRIANGLE_105_PROPOSALS_ONLY',input_sha256=parent.EXPECTED,seed=SEED,starts_requested=STARTS,rounds=ROUNDS,maxiter=MAXITER,margin=MARGIN,stable_weight=SWEIGHT,numpy=np.__version__,scipy=scipy.__version__,torch=torch.__version__,threads=1,results=rows);out.write_bytes(B(report))
  if rec['S']==rec['U']==1 and min(rec['primal_second'],-rec['face_second_largest'])>1e-8:print('PHYSICAL105_NUMERICAL110_NEEDS_EXACT_MAXIMAL_GATE',flush=True);break
 print('PHYSICAL105_SCREEN_TERMINAL',len(rows),hashlib.sha256(out.read_bytes()).hexdigest(),flush=True)
if __name__=='__main__':main(*map(Path,sys.argv[1:]))
