"""Finite affine-metric search on exact parent audits. Numerical proposals only."""
from pathlib import Path
from fractions import Fraction as F
import sys,json,time
sys.set_int_max_str_digits(0)
import numpy as np
from scipy.optimize import minimize
np.set_printoptions(precision=17)
B=np.array([np.diag([1,0,-1]),np.diag([0,1,-1]),[[0,1,0],[1,0,0],[0,0,0]],[[0,0,1],[0,0,0],[1,0,0]],[[0,0,0],[0,0,1],[0,1,0]]],float)
def metric(x):return np.eye(3)+np.einsum('i,ijk->jk',x[:5],B)
def prepare(a):
 g=np.array([float(F(x)) for x in a['raw_centroid']]);P=np.array([[float(F(x)) for x in p] for p in a['raw_vertices']])-g
 q=np.array([[float(F(n)/F(h)) for n in ns] for ns,h in zip(a['normals'],a['offsets'])]);q=q/(1-q@g)[:,None]
 E=np.array(a['edges']);ef=[]
 for i,j in E:ef.append([k for k,cy in enumerate(a['faces']) if i in cy and j in cy])
 Z=[]
 for pts,edges in [(P,E),(q,np.array(ef))]:
  arcs=np.concatenate([edges,edges[:,::-1]]);u=pts[arcs[:,0]];d=pts[arcs[:,1]]-u;norm=np.linalg.norm(u,axis=1)*np.linalg.norm(d,axis=1)
  C=(u[:,:,None]*d[:,None,:]+d[:,:,None]*u[:,None,:])/2/norm[:,None,None]
  groups=[np.where(arcs[:,0]==i)[0] for i in range(len(pts))]
  root=int(np.argmax(np.sum(pts**2,axis=1)))
  Z.append((C,groups,root,arcs))
 return Z
class Model:
 def __init__(self,a):self.Z=prepare(a);self.ncall=0
 def data(self,x):
  G=metric(x);K=np.linalg.inv(G)
  vals=[];grads=[];roots=[];rootgrads=[];info=[]
  for pol,(C,groups,root,arcs) in enumerate(self.Z):
   T=K if pol else G;v=np.einsum('nij,ij->n',C,T)
   deriv=-np.einsum('ij,bjk,kl->bil',K,B,K) if pol else B
   J=np.einsum('nij,bij->nb',C,deriv)
   ix=[g[np.argmax(v[g])] for i,g in enumerate(groups) if i!=root]
   vals.extend(v[ix]);grads.extend(J[ix]);roots.extend(-v[groups[root]]);rootgrads.extend(-J[groups[root]])
   info.append({'root':root,'nonpositive':[i for i,g in enumerate(groups) if np.max(v[g])<=0],'min_exit':float(min(np.max(v[g]) for i,g in enumerate(groups) if i!=root))})
  return np.array(vals),np.array(grads),np.array(roots),np.array(rootgrads),info
 def cons(self,x):
  v,j,r,rj,_=self.data(x);return np.r_[v-x[5],r-x[5],np.linalg.eigvalsh(metric(x))-.001]
 def jac(self,x):
  v,j,r,rj,_=self.data(x);e,U=np.linalg.eigh(metric(x));ej=np.einsum('ik,bij,jk->kb',U,B,U)
  return np.r_[np.column_stack([j,-np.ones(len(j))]),np.column_stack([rj,-np.ones(len(rj))]),np.column_stack([ej,np.zeros(3)])]
 def solve(self,x0,maxiter=1000):
  self.ncall=0
  obj=lambda x:-x[5];grad=lambda x:np.array([0,0,0,0,0,-1.])
  return minimize(obj,x0,jac=grad,method='SLSQP',constraints=[{'type':'ineq','fun':self.cons,'jac':self.jac}],bounds=[(-2,2)]*5+[(-1,1)],options={'maxiter':maxiter,'ftol':1e-12,'disp':False})
if __name__=='__main__':
 R=Path('/mnt/data/recovered');out=Path(sys.argv[1]);out.mkdir(exist_ok=True)
 rng=np.random.default_rng(2026091501)
 for name in sys.argv[2:]:
  a=json.loads((R/(name+'_A.json')).read_text());m=Model(a);runs=[]
  print('INITIAL',name,m.data(np.zeros(6))[-1],flush=True)
  for k in range(6):
   x=np.r_[np.zeros(5) if k==0 else rng.normal(0,.001 if k<3 else .05,5),0.]
   v,_,r,_,_=m.data(x);x[5]=min(v.min(),r.min())-1e-6
   t=time.time();s=m.solve(x);v,j,r,rj,inf=m.data(s.x)
   o={'case':name,'start':k,'start_x':x.tolist(),'x':s.x.tolist(),'G':metric(s.x).tolist(),'eigenvalues':np.linalg.eigvalsh(metric(s.x)).tolist(),'success':bool(s.success),'message':s.message,'iterations':s.nit,'primal_polar':inf,'minimum_constraint':float(m.cons(s.x).min()),'seconds':time.time()-t}
   runs.append(o);(out/(name+'.json')).write_text(json.dumps(runs,indent=2));print('DONE',name,k,s.nit,s.success,s.x[5],inf,flush=True)
   if min(v.min(),r.min())>1e-9:print('NUMERICAL_AFFINE_110_PROPOSAL',name,flush=True);break
