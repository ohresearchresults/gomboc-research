"""Finite one-way polar-chain search with exact-own-mass numerical closure.
A chain has positive radial exits only when its full logarithmic budget is >0.
Closure or proposal equilibrium counts are not an exact-polyhedron certificate.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import argparse,hashlib,itertools,json,sys
from fractions import Fraction as F
from pathlib import Path
import numpy as np
from scipy.spatial import ConvexHull,QhullError
from scipy.optimize import least_squares

def encoded(o):return json.dumps(o,sort_keys=True,separators=(',',':')).encode()
def exits(X):
 D=X[None,:,:]-X[:,None,:];den=np.linalg.norm(X,axis=1)[:,None]*np.linalg.norm(D,axis=2)
 eta=np.sum(X[:,None,:]*D,axis=2)/np.maximum(den,1e-100);np.fill_diagonal(eta,-1e10)
 return eta.max(axis=1)
def invert(Q):
 hull=ConvexHull(Q);assert np.max(hull.equations[:,-1])<0
 X=np.linalg.solve(Q[hull.simplices],np.ones((len(hull.simplices),3,1)))[:,:,0]
 # Remove numerical representations of the same vertex, not distinct support rows.
 X=np.unique(np.round(X,decimals=11),axis=0)
 hp=ConvexHull(X);X=X[hp.vertices];hp=ConvexHull(X)
 abc=X[hp.simplices];D=np.einsum('ij,ij->i',abc[:,0],np.cross(abc[:,1],abc[:,2]));D=abs(D)
 assert D.min()>0
 g=np.sum(D[:,None]*abc.sum(axis=1),axis=0)/(4*D.sum())
 return X,g,float(D.sum()/6)
class Model:
 def __init__(self,path):
  b=Path(path).read_bytes();assert hashlib.sha256(b).hexdigest()=='f17bb48815e8ff86697936d33af34e8e28170808674e9149dbae23c5228a19f7'
  a=json.loads(b);self.P=np.array([[float(F(x)) for x in p] for p in a['raw_vertices']])/1e8
  self.g=np.array([float(F(x)) for x in a['raw_centroid']])/1e8
  self.q=np.array(a['normals'],float);self.q/=np.array(a['offsets'],float)[:,None]/1e8
  self.u,self.v=0,13;self.evals=0
 def shape(self,c,n,bow,gain,force=False):
  h=1-self.q@c
  if h.min()<=0:raise ValueError('chart outside original solid')
  Q=self.q/h[:,None];u=Q[self.u];v=gain*Q[self.v];r0=np.linalg.norm(u);r1=np.linalg.norm(v);a=u/r0;b=v/r1;co=np.clip(a@b,-1,1);phi=np.arccos(co)
  t=(b-co*a)/np.linalg.norm(b-co*a);axis=np.cross(a,t);s=np.linspace(0,1,n+1)
  dirs=np.cos(phi*s)[:,None]*a+np.sin(phi*s)[:,None]*t+bow*np.sin(np.pi*s)[:,None]*axis;dirs/=np.linalg.norm(dirs,axis=1)[:,None]
  cosines=np.einsum('ij,ij->i',dirs[:-1],dirs[1:]);assert cosines.min()>0
  need=-np.log(cosines);budget=np.log(r1/r0)-need.sum()
  radii=r0*np.exp(np.r_[0,np.cumsum(need+budget/n)]);chain=dirs*radii[:,None]
  Z=np.vstack((Q,chain[1:]));X,g,V=invert(Z)
  return X,g,V,Z,float(budget),float(h.min())
 def closure(self,c,n,bow,gain):
  self.evals+=1
  try:return self.shape(c,n,bow,gain)[1]
  except (ValueError,AssertionError,np.linalg.LinAlgError,QhullError):return (c-self.g)*10+np.ones(3)
 def report(self,c,n,bow,gain):
  X,g,V,Q,budget,hmin=self.shape(c,n,bow,gain);own=X-g
  active=ConvexHull(Q).vertices;OQ=Q[active]/(1-Q[active]@g)[:,None]
  se=exits(OQ);ue=exits(own)
  return {'chart':c.tolist(),'closure':float(np.linalg.norm(g)),'budget':budget,'chart_min_height':hmin,'S':int(sum(se<-1e-8)),'U':int(sum(ue<-1e-8)),'S_uncertain':int(sum(abs(se)<=1e-8)),'U_uncertain':int(sum(abs(ue)<=1e-8)),'V_proposal':len(X),'F_proposal':len(active),'E_proposal':len(X)+len(active)-2,'volume':V,'s':se.tolist(),'u':ue.tolist(),'points':(X+c).tolist(),'polar_about_chart':Q.tolist()}
def main():
 p=argparse.ArgumentParser();p.add_argument('--audit',required=True);p.add_argument('--out',required=True);p.add_argument('--n',nargs='+',type=int,default=[16,24,40]);p.add_argument('--bow',nargs='+',type=float,default=[-1,0,1]);p.add_argument('--gain',nargs='+',type=float,default=[1,2,4]);p.add_argument('--maxfev',type=int,default=250);a=p.parse_args();out=Path(a.out);out.mkdir(parents=True,exist_ok=False);obj=Model(a.audit);rows=[];best=None
 for n,bow,gain in itertools.product(a.n,a.bow,a.gain):
  # Height is tiny, so nondimensionalize the unknown using original coordinate widths.
  widths=np.ptp(obj.P,axis=0);fun=lambda z:obj.closure(obj.g+widths*z,n,bow,gain)
  r=least_squares(fun,np.zeros(3),diff_step=1e-5,xtol=1e-11,ftol=1e-11,gtol=1e-11,max_nfev=a.maxfev);c=obj.g+widths*r.x
  row=dict(n=n,bow=bow,gain=gain,nfev=int(r.nfev),status=int(r.status))
  try:
   detail=obj.report(c,n,bow,gain);row.update({k:v for k,v in detail.items() if k not in ['s','u','points','polar_about_chart']})
   rank=(detail['S']+detail['U']+detail['S_uncertain']+detail['U_uncertain'],detail['E_proposal'],detail['closure'])
   if best is None or rank<best:best=rank;(out/'BEST.json').write_bytes(encoded({'parameters':row,**detail}))
   if detail['S']==detail['U']==1 and detail['S_uncertain']==detail['U_uncertain']==0 and detail['E_proposal']<=310:(out/('PROPOSAL_'+str(len(rows))+'.json')).write_bytes(encoded({'parameters':row,**detail}))
  except (ValueError,AssertionError,np.linalg.LinAlgError,QhullError) as e:row['error']=str(e)
  rows.append(row);(out/'SEARCH.json').write_bytes(encoded({'parameters':vars(a),'records':rows,'evals':obj.evals}));print('CASE',len(rows),row,flush=True)
 print('C80_SINGLE_POLAR_CHAIN_SEARCH_FINISHED',len(rows),obj.evals,best,flush=True)
if __name__=='__main__':main()
