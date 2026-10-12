"""Own-centroid coordinates for a whole projective/physical-metric orbit.
Discovery only: every proposal uses actual volume moments; full exact audits are separate.
Dependencies: numpy 2.3.5, scipy 1.17.0; one BLAS thread.
"""
import os
os.environ.setdefault('OPENBLAS_NUM_THREADS','1');os.environ.setdefault('OMP_NUM_THREADS','1')
import sys,json,math,time,argparse
from pathlib import Path
from fractions import Fraction
import numpy as np
from scipy.optimize import least_squares
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import dijkstra
sys.set_int_max_str_digits(0)

def f(x):return float(Fraction(x))
def edge_pairs(faces):
 d={}
 for k,cy in enumerate(faces):
  for a,b in zip(cy,cy[1:]+cy[:1]):d.setdefault(tuple(sorted((a,b))),[]).append(k)
 assert all(len(v)==2 for v in d.values())
 e=np.array(sorted(d),int);return e,np.array([d[tuple(x)] for x in e],int)

class CentroidOrbit:
 def __init__(self,report):
  r=json.loads(Path(report).read_text());self.report=r
  self.X=np.array([[f(v) for v in row] for row in r['raw_vertices']])
  self.q=np.array([[v/h for v in n] for n,h in zip(r['normals'],r['offsets'])])
  self.tri=np.array([(cy[0],cy[j],cy[j+1]) for cy in r['faces'] for j in range(1,len(cy)-1)])
  self.w0=np.einsum('ni,ni->n',self.X[self.tri[:,0]],np.cross(self.X[self.tri[:,1]],self.X[self.tri[:,2]]))
  assert self.w0.min()>0
  self.ep,self.ed=edge_pairs(r['faces']);self.ns=[len(self.X),len(self.q)]
  self.edges=[];self.padded=[]
  for e,n in zip([self.ep,self.ed],self.ns):
   src=np.r_[e[:,0],e[:,1]];dst=np.r_[e[:,1],e[:,0]];self.edges.append((src,dst))
   deg=np.bincount(src,minlength=n);p=np.full((n,deg.max()),len(src),int)
   for i in range(n):p[i,:deg[i]]=np.flatnonzero(src==i)
   self.padded.append(p)
  self.last=None;self.last_t=np.zeros(3);self.calls=0;self.newton_calls=0
  self.b0=self.state(np.zeros(3))[1]
 def state(self,t):
  d=1+self.X@t
  if d.min()<=0:raise ArithmeticError('Projective horizon')
  y=self.X/d[:,None];tr=y[self.tri];w=self.w0/np.prod(d[self.tri],axis=1);W=w.sum()
  s=tr.sum(axis=1);g=np.sum(w[:,None]*s,axis=0)/(4*W)
  second=(np.einsum('n,ni,nj->ij',w,s,s)+np.einsum('n,nai,naj->ij',w,tr,tr))/(20*W)
  cov=second-np.outer(g,g);K=5*cov+np.outer(g,g)
  return y,g,K,d,W/6
 def invert(self,b):
  b=np.asarray(b);t=self.last_t.copy();scale=1+np.linalg.norm(b,np.inf)
  for k in range(100):
   y,g,K,d,V=self.state(t);error=np.linalg.norm(b-g,np.inf)
   self.newton_calls+=1
   if error<1e-12*scale:
    self.last_t=t.copy();return t,y,g,K,d,V,error
   delta=np.linalg.solve(K,g-b);dd=self.X@delta
   alpha=min(1.,.95*np.min(-d[dd<0]/dd[dd<0]) if (dd<0).any() else 1.)
   val=np.log(V)+4*b@t;slope=4*(b-g)@delta
   for back in range(60):
    tt=t+alpha*delta
    yy,gg,KK,ddd,VV=self.state(tt)
    if np.log(VV)+4*b@tt <= val+1e-4*alpha*slope or np.linalg.norm(gg-b,np.inf)<error*(1-1e-4*alpha):
     t=tt;break
    alpha*=.5
   else:
    if error<2e-10*scale:self.last_t=t.copy();return t,y,g,K,d,V,error
    raise ArithmeticError('Centroid Newton backtracking exhausted')
  raise ArithmeticError('Centroid Newton iteration budget exhausted')
 def geometry(self,z):
  t,y,g,K,d,V,err=self.invert(z[:3]);Tb=-np.linalg.inv(K)
  dy=-np.einsum('ni,nj->nij',y,y)@Tb
  p=y-g;dp=dy-np.eye(3)[None,:,:]
  n=self.q+t;hh=1-n@g
  if hh.min()<=0:raise ArithmeticError('Bad own polar interior')
  pole=n/hh[:,None]
  dh=-g@Tb-n
  dpol=Tb[None,:,:]/hh[:,None,None]-n[:,:,None]*dh[:,None,:]/hh[:,None,None]**2
  a,c=z[3:5];ex=np.exp([a,c,-a-c]);U=np.eye(3);U[0,1]=z[5];U[0,2]=z[6];U[1,2]=z[7]
  A=ex[:,None]*U;B=np.linalg.inv(A).T
  DA=np.zeros((5,3,3));DA[0]=np.diag([1,0,-1])@A;DA[1]=np.diag([0,1,-1])@A
  DA[2,0,1]=ex[0];DA[3,0,2]=ex[0];DA[4,1,2]=ex[1]
  DB=np.array([-B@q.T@B for q in DA])
  P=p@A.T;Y=pole@B.T
  JP=np.concatenate((np.einsum('ij,njk->nik',A,dp),np.einsum('kij,nj->nik',DA,p)),axis=2)
  JY=np.concatenate((np.einsum('ij,njk->nik',B,dpol),np.einsum('kij,nj->nik',DB,pole)),axis=2)
  info=dict(t=t.tolist(),A=A.tolist(),volume=V,centroid_projective=g.tolist(),centroid=(A@g).tolist(),centroid_error=float(err),min_den=float(d.min()),condition=float(np.linalg.cond(A)))
  return P,Y,JP,JY,info
 def all_data(self,z):
  z=np.asarray(z,float)
  if self.last is not None and np.array_equal(z,self.last[0]):return self.last[1]
  P,Y,JP,JY,info=self.geometry(z);data=[];phi=[];jac=[];roots=[];rootsets=[]
  for X,J,(src,dst),n,pad in zip((P,Y),(JP,JY),self.edges,self.ns,self.padded):
   a=X[src];e=X[dst]-a;na=np.linalg.norm(a,axis=1);ne=np.linalg.norm(e,axis=1)
   v=np.einsum('ni,ni->n',a,e)/(na*ne)
   va=e/(na*ne)[:,None]-v[:,None]*a/na[:,None]**2
   ve=a/(na*ne)[:,None]-v[:,None]*e/ne[:,None]**2
   dv=np.einsum('ni,nik->nk',va,J[src])+np.einsum('ni,nik->nk',ve,J[dst]-J[src])
   padded=np.r_[v,-np.inf][pad];inds=pad[np.arange(n),np.argmax(padded,axis=1)];best=v[inds].copy()
   root=int(np.argmax(np.einsum('ni,ni->n',X,X)));roots.append(root);rootsets.append(np.where(best<0)[0].tolist())
   best[root]=1.;jj=dv[inds].copy();jj[root]=0
   data.append((v,dv,root));phi.append(best);jac.append(jj)
  info.update(U=rootsets[0],S=rootsets[1],roots=roots,z=z.tolist(),min_nonroot=float(min(x.min() for x in phi)))
  ret=(np.concatenate(phi),np.concatenate(jac),info,data)
  self.last=(z.copy(),ret);self.calls+=1;return ret
 def residual(self,z,target=1e-5):
  v,j,info,data=self.all_data(z);return np.minimum(v-target,0)
 def jacobian(self,z,target=1e-5):
  v,j,info,data=self.all_data(z);return j*(v<target)[:,None]
 def forest(self,z,power=2):
  data=self.all_data(z)[3];choice=[]
  for (v,dv,root),(src,dst),n in zip(data,self.edges,self.ns):
   weights=np.maximum(1e-5-v,0)**power+1e-9
   distances,previous=dijkstra(csr_matrix((weights,(dst,src)),shape=(n,n)),directed=True,indices=root,return_predecessors=True)
   assert np.isfinite(distances).all()
   idx=np.full((n,n),-1,int);idx[src,dst]=np.arange(len(src))
   ids=[idx[i,previous[i]] for i in range(n) if i!=root];assert min(ids)>=0
   choice.append(np.array(ids))
  return choice
 def fixed(self,z,ids):
  data=self.all_data(z)[3];v=np.concatenate([a[0][k] for a,k in zip(data,ids)]);J=np.concatenate([a[1][k] for a,k in zip(data,ids)])
  return np.minimum(v-1e-5,0),J*(v<1e-5)[:,None]

def main():
 pa=argparse.ArgumentParser();pa.add_argument('report');pa.add_argument('out');pa.add_argument('--seed',type=int,default=720618);pa.add_argument('--starts',type=int,default=100);pa.add_argument('--evals',type=int,default=300);pa.add_argument('--forest',type=int,default=0);pa.add_argument('--range',type=float,default=12.);a=pa.parse_args()
 out=Path(a.out);out.mkdir(exist_ok=False);m=CentroidOrbit(a.report);rng=np.random.default_rng(a.seed)
 z0=np.r_[m.b0,np.zeros(5)];print('BASE',m.all_data(z0)[2],flush=True)
 ztest=np.r_[.13,-.24,.09,.2,-.15,.06,-.1,.2];v,J,_,_=m.all_data(ztest)
 num=np.column_stack([(m.all_data(ztest+np.eye(8)[j]*1e-6)[0]-m.all_data(ztest-np.eye(8)[j]*1e-6)[0])/2e-6 for j in range(8)])
 err=float(np.max(abs(J-num)));assert err<2e-5,err;print('CENTROID_COORDINATE_FULL_JACOBIAN_PASS',err,flush=True)
 low=np.r_[np.full(3,-a.range),[-2,-2,-5,-5,-5]];high=-low;best=None;start=time.monotonic();records=[];failures=0
 for k in range(a.starts):
  if k==0:z=z0.copy()
  elif k%4==0 and best is not None:z=best[1]+rng.normal(size=8)*(.04 if k%8==0 else .4)
  else:z=np.r_[rng.normal(size=3)*10**rng.uniform(-2,1),rng.uniform(-1.5,1.5,2),rng.normal(size=3)]
  z=np.clip(z,low+1e-6,high-1e-6)
  try:
   if a.forest:
    for outer in range(a.forest):
     ids=m.forest(z,1+(k%2))
     sol=least_squares(lambda x:m.fixed(x,ids)[0],z,jac=lambda x:m.fixed(x,ids)[1],bounds=(low,high),max_nfev=a.evals,ftol=1e-10,xtol=1e-11,gtol=1e-10)
     diff=np.linalg.norm(sol.x-z);z=sol.x
     if m.all_data(z)[2]['min_nonroot']>1e-8 or diff<1e-8:break
   else:
    sol=least_squares(m.residual,z,jac=m.jacobian,bounds=(low,high),max_nfev=a.evals,ftol=1e-10,xtol=1e-11,gtol=1e-10);z=sol.x
   v,J,info,data=m.all_data(z);info.update(start=k,nfev=int(sol.nfev),loss=float(np.sum(np.minimum(v-1e-5,0)**2)))
   key=(len(info['S'])+len(info['U']),info['loss']);records.append(info)
   with (out/'ALL.jsonl').open('a') as file:file.write(json.dumps(info,sort_keys=True)+'\n')
   if best is None or key<best[0]:
    best=(key,z.copy());(out/'BEST.json').write_text(json.dumps(info,sort_keys=True));print('BEST',k,key,info['min_nonroot'],info['min_den'],info['condition'],flush=True)
   if key[0]==2 and info['min_nonroot']>1e-8:
    (out/'NUMERICAL_WINNER.json').write_text(json.dumps(info,sort_keys=True));print('NUMERICAL_ONLY_110_FOUND',k,flush=True);break
  except (ArithmeticError,np.linalg.LinAlgError,ValueError) as exc:
   failures+=1
   with (out/'FAILURES.txt').open('a') as file:file.write(str(k)+' '+str(exc)+'\n')
   m.last_t=np.zeros(3);m.last=None
  if k%10==0:print('STEP',k,'seconds',time.monotonic()-start,'calls',m.calls,'Newton',m.newton_calls,'failures',failures,flush=True)
 (out/'CONFIG.json').write_text(json.dumps(vars(a),sort_keys=True))
 (out/'SUMMARY.json').write_text(json.dumps(dict(attempts=k+1,completed=len(records),failures=failures,evaluations=m.calls,newton_evaluations=m.newton_calls,seconds=time.monotonic()-start),sort_keys=True))
 print('FINITE_TRUE_CENTROID_METRIC_SEARCH_FINISHED',len(records),failures,flush=True)
if __name__=='__main__':main()
