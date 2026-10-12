"""Whole primal/dual rooted-forest repair on the actual uniform-volume incidence manifold.
Positive identity reserves are fixed for the entire phase; negative selected arrows
are the explicitly declared cancellation basin. No change of reference centre.
"""
from implicit import Manifold
from model import dot,norm,divide,HERE
import radial,sys,json,time,argparse,heapq
from fractions import Fraction as F
import numpy as np
from scipy.linalg import qr,cho_solve,cho_factor,lstsq
sys.set_int_max_str_digits(0)

def forest(edges,values,root,N):
 incoming=[[] for i in range(N)]
 for k,(i,j) in enumerate(edges):incoming[j].append((i,k))
 dist={root:0.};nxt={};todo=[(0.,root)]
 while todo:
  d,j=heapq.heappop(todo)
  if d!=dist[j]:continue
  for i,k in incoming[j]:
   cc=d+max(-values[k],0)+1e-10
   if i not in dist or cc<dist[i]:dist[i]=cc;nxt[i]=k;heapq.heappush(todo,(cc,i))
 assert len(nxt)==N-1
 for i in nxt:
  seen=set();j=i
  while j!=root:assert j not in seen;seen.add(j);j=int(edges[nxt[j],1])
 return np.array([nxt[i] for i in range(N) if i!=root])
class Forest(Manifold):
 def __init__(self,P,q,faces):
  super().__init__(P,q,faces);efs={tuple(e):[] for e in self.E.tolist()}
  for k,cy in enumerate(self.F):
   for a,b in zip(cy,cy[1:]+cy[:1]):efs[tuple(sorted((a,b)))].append(k)
  self.fe=np.array([(a,b) for fs in efs.values() for a,b in [fs,fs[::-1]]]);self.ffi=[np.flatnonzero(self.fe[:,0]==i) for i in range(self.n)]
 def evalf(self,z,T):
  R=self.evaluate(z,T);K=T.shape[1];P=R['P'];q=R['q'];DP=T[:self.V*3].reshape(self.V,3,K);DQ=T[self.V*3:].reshape(self.n,3,K)
  # Reuse filled centroid derivative by a direct face-triangle formula.
  from model import cross
  X=P[self.tris];DX=DP[self.tris];v,dv=cross(X[:,1],X[:,2],DX[:,1],DX[:,2]);dt,dd=dot(X[:,0],v,DX[:,0],dv);S=dt.sum();DS=dd.sum(axis=0);B=np.einsum('n,ni->i',dt,X.sum(axis=1));DB=np.einsum('nk,ni->ik',dd,X.sum(axis=1))+np.einsum('n,nik->ik',dt,DX.sum(axis=1));g=R['g'];dg=(DB-4*g[:,None]*DS)/(4*S)
  h=1-q@g;dh=-np.einsum('nik,i->nk',DQ,g)-q@dg;Q=q/h[:,None];dQ=(DQ-Q[:,:,None]*dh[:,None,:])/h[:,None,None];i,j=self.fe.T;e=Q[j]-Q[i];de=dQ[j]-dQ[i];v,dv=dot(Q[i],e,dQ[i],de);a,da=norm(Q[i],dQ[i]);b,db=norm(e,de);v,dv=divide(v,a*b,dv,da*b[:,None]+db*a[:,None]);R['dual']=v;R['ddual']=dv;return R

def run(tag,start,steps,mu=1e-11,lam=.0001):
 G=json.load(open(start));raw,P=radial.reconstruct(G);PP=np.array([[float(x) for x in p] for p in P]);q=np.array([[float(F(v,h[-1])) for v in h[:3]] for h in raw['H']]);M=Forest(PP,q,G['faces']);z=np.r_[PP.ravel(),q.ravel()];R=M.evalf(z,np.zeros((M.K,1)));ut=forest(M.ue,R['u'],0,M.V);ft=forest(M.fe,R['dual'],114,M.n);vals=np.r_[R['u'][ut],R['dual'][ft]];neg=vals<=1e-9;floors=np.maximum(1e-10,.1*vals[~neg]);sf=.01*R['s'];tf=.01*R['det'];root=M.ui[0];st=M.ffi[114];rm=.1*(-R['u'][root]);sm=.1*(-R['dual'][st]);trace=[]
 spec={'u_tree':M.ue[ut].tolist(),'f_tree':M.fe[ft].tolist(),'negative_indices':np.flatnonzero(neg).tolist(),'floors':floors.tolist(),'mu':mu,'lambda':lam,'start':start};(HERE/(tag+'_FOREST.json')).write_text(json.dumps(spec,sort_keys=True,separators=(',',':')))
 print('BASIN',[(M.ue[k].tolist(),float(R['u'][k])) for k in ut if R['u'][k]<=1e-9],[(M.fe[k].tolist(),float(R['dual'][k])) for k in ft if R['dual'][k]<=1e-9],flush=True)
 def dat(R):
  vals=np.r_[R['u'][ut],R['dual'][ft]];J=np.vstack((R['du'][ut],R['ddual'][ft]));v=vals[neg]-1e-6;dv=J[neg];g=np.r_[vals[~neg]-floors,-R['u'][root]-rm,-R['dual'][st]-sm,R['s']-sf,R['det']-tf];dg=np.vstack((J[~neg],-R['du'][root],-R['ddual'][st],R['ds'],R['ddet']));active=v<0;return v[active],dv[active],g,dg,vals
 def cost(R):
  v,J,g,dg,vals=dat(R)
  if min(g)<=0:return np.inf
  return .5*v@v-mu*np.log(g).sum()
 for it in range(steps):
  t=time.time();c,A=M.con(z);Q,_=qr(A.T,mode='full');T=Q[:,len(c):];R=M.evalf(z,T);v,J,g,dg,vals=dat(R);BB=dg/g[:,None];H=J.T@J+mu*BB.T@BB+lam*np.eye(T.shape[1]);b=-J.T@v+mu*BB.sum(axis=0)
  try:u=cho_solve(cho_factor(H),b)
  except np.linalg.LinAlgError:u=lstsq(np.vstack((J,np.sqrt(mu)*BB,np.sqrt(lam)*np.eye(T.shape[1]))),np.r_[-v,np.full(len(BB),np.sqrt(mu)),np.zeros(T.shape[1])],lapack_driver='gelsy')[0]
  dz=T@u;a=min(1.,.2/max(np.linalg.norm(dz),1e-12));old=cost(R);ok=False
  for ls in range(24):
   zz,proj=M.project(z+a*dz)
   if proj:
    R2=M.evalf(zz,np.zeros((M.K,1)));new=cost(R2)
    if np.isfinite(new) and new<old-1e-16:ok=True;break
   a*=.5
  row={'it':it,'accepted':ok,'alpha':a,'lambda':lam,'cost':float(old),'targets':vals[neg].tolist(),'guard_min':float(g.min()),'class':M.res(R)[2],'seconds':time.time()-t}
  if ok:z=zz;lam=max(1e-10,lam*(.8 if a>.25 else 1.2))
  else:lam*=10
  trace.append(row);np.save(HERE/(tag+'.npy'),z);(HERE/(tag+'.trace.json')).write_text(json.dumps(trace,sort_keys=True,separators=(',',':')));print(json.dumps(row),flush=True)
  if (vals>0).all() or lam>1e6:break
 PP=z[:M.V*3].reshape(-1,3);qq=z[M.V*3:].reshape(-1,3);out=radial.make(PP,qq,M.F,0,10**12,G['priority']);out['priority']=G['priority'];out['parent_labels']=G['parent_labels'];(HERE/(tag+'_GENERATOR.json')).write_text(json.dumps(out,sort_keys=True,separators=(',',':')));print('END',M.res(M.evalf(z,np.zeros((M.K,1))))[2],flush=True)
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--tag',default='FOREST1');p.add_argument('--start',required=True);p.add_argument('--steps',type=int,default=50);p.add_argument('--mu',type=float,default=1e-11);p.add_argument('--lam',type=float,default=.0001);a=p.parse_args();run(a.tag,a.start,a.steps,a.mu,a.lam)
