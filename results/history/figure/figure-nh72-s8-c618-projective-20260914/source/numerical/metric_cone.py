"""Finite positive-metric cutting-plane searches for complete rooted ascent forests.
LP relaxations approximate the PSD cone; only actual positive-metric outcomes count.
"""
import os
os.environ.setdefault('OPENBLAS_NUM_THREADS','1');os.environ.setdefault('OMP_NUM_THREADS','1')
import json,sys,argparse,time,heapq
from pathlib import Path
import numpy as np
from scipy.optimize import linprog
from centroid_metric import CentroidOrbit

def sym(v):return np.array([[v[0],v[3],v[4]],[v[3],v[1],v[5]],[v[4],v[5],v[2]]])
def quadratic(u):return np.r_[u*u,2*u[0]*u[1],2*u[0]*u[2],2*u[1]*u[2]]
def arrow_coefs(X,edges):
 src,dst=edges;p=X[src];e=X[dst]-p
 return np.c_[p*e,p[:,0]*e[:,1]+p[:,1]*e[:,0],p[:,0]*e[:,2]+p[:,2]*e[:,0],p[:,1]*e[:,2]+p[:,2]*e[:,1]]/(np.linalg.norm(p,axis=1)*np.linalg.norm(e,axis=1))[:,None]
def tree(coef,G,edges,n,root):
 v=coef@np.r_[np.diag(G),G[0,1],G[0,2],G[1,2]];src,dst=edges;incoming=[[] for _ in range(n)]
 for k,j in enumerate(dst):incoming[j].append(k)
 quality=np.full(n,-np.inf);quality[root]=np.inf;prev=np.full(n,-1,int);queue=[(-np.inf,root)];seen=set()
 while queue:
  neg,j=heapq.heappop(queue)
  if j in seen:continue
  seen.add(j)
  for k in incoming[j]:
   i=src[k];candidate=min(v[k],quality[j])
   if i not in seen and candidate>quality[i]:quality[i]=candidate;prev[i]=k;heapq.heappush(queue,(-candidate,int(i)))
 assert len(seen)==n
 return np.array([prev[i] for i in range(n) if i!=root])
def psd_metric(C,lam=1e-4):
 cuts=[quadratic(v) for v in np.eye(3)];info={}
 for it in range(100):
  A=np.r_[np.c_[-C,np.ones(len(C))],np.c_[-np.array(cuts),np.zeros(len(cuts))]];b=np.r_[np.zeros(len(C)),-lam*np.ones(len(cuts))]
  sol=linprog([0]*6+[-1],A_ub=A,b_ub=b,A_eq=[[1,1,1,0,0,0,0]],b_eq=[1],bounds=[(lam,1)]*3+[(-.5,.5)]*3+[(-1,1)],method='highs')
  if not sol.success:return None,dict(status='LP_no_solution',message=sol.message)
  G=sym(sol.x[:6]);eig,U=np.linalg.eigh(G);margin=float(np.min(C@sol.x[:6]));info=dict(iterations=it+1,lambda_min=float(eig[0]),margin=margin,lp_gamma=float(sol.x[6]))
  if eig[0]>=lam*(1-1e-5):return G,info
  # The LP is an outer relaxation, but its numerical negative optimum is not a claimed proof.
  if sol.x[6]<-1e-3:return None,dict(info,status='negative_relaxation')
  for j in range(3):
   if eig[j]<lam:cuts.append(quadratic(U[:,j]))
 return None,dict(info,status='spectral_cut_budget')
def state_counts(m,t,A):
 y,g,K,d,V=m.state(t);P=(y-g)@A.T;Y=((m.q+t)/(1-(m.q+t)@g)[:,None])@np.linalg.inv(A);sets=[];mins=[]
 for X,(src,dst),n in zip((P,Y),m.edges,m.ns):
  p=X[src];e=X[dst]-p;v=np.einsum('ni,ni->n',p,e)/(np.linalg.norm(p,axis=1)*np.linalg.norm(e,axis=1));maximum=np.full(n,-np.inf);np.maximum.at(maximum,src,v);sets.append(np.where(maximum<0)[0].tolist());maximum[np.argmax(np.einsum('ni,ni->n',X,X))]=1.;mins.append(float(maximum.min()))
 return dict(U=sets[0],S=sets[1],t=t.tolist(),A=A.tolist(),b=g.tolist(),min_den=float(d.min()),condition=float(np.linalg.cond(A)),min_nonroot=min(mins),side_minima=mins)
def main():
 p=argparse.ArgumentParser();p.add_argument('report');p.add_argument('out');p.add_argument('--cases',type=int,default=400);p.add_argument('--seed',type=int,default=720622);p.add_argument('--lam',type=float,default=.0001);p.add_argument('--side',type=int,default=0);p.add_argument('--outer',type=int,default=5);a=p.parse_args();m=CentroidOrbit(a.report);out=Path(a.out);out.mkdir(exist_ok=False);rng=np.random.default_rng(a.seed);clock=time.monotonic();best={};observations=0
 for k in range(a.cases):
  b=m.b0 if k<4 else rng.normal(size=3)*10**rng.uniform(-2,1.3)
  try:t,y,g,K,d,V,error=m.invert(b)
  except ArithmeticError:continue
  B=np.eye(3) if k<2 else np.linalg.inv(np.linalg.cholesky((K-np.outer(g,g))/5));B/=np.linalg.det(B)**(1/3)
  X=(y-g)@B.T if a.side==0 else ((m.q+t)/(1-(m.q+t)@g)[:,None])@np.linalg.inv(B)
  C=arrow_coefs(X,m.edges[a.side]);src,dst=m.edges[a.side];vals=C@np.r_[np.ones(3),np.zeros(3)];mx=np.full(len(X),-np.inf);np.maximum.at(mx,src,vals);roots=np.where(mx<0)[0]
  root=int(roots[k%len(roots)]) if len(roots) else int(np.argmax(np.sum(X*X,axis=1)));G=np.eye(3)/3
  for outer in range(a.outer):
   ids=tree(C,G,m.edges[a.side],len(X),root);GG,info=psd_metric(C[ids],a.lam)
   if GG is None:break
   G=GG;A=np.linalg.cholesky(G if a.side==0 else np.linalg.inv(G)).T@B;A/=np.linalg.det(A)**(1/3)
   info.update(state_counts(m,t,A));info.update(case=k,outer=outer,selected_root=root,side=a.side,target_centroid=np.asarray(b).tolist())
   observations+=1
   with (out/'ALL.jsonl').open('a') as f:f.write(json.dumps(info,sort_keys=True)+'\n')
   count=(len(info['S']),len(info['U']));key=f'S{count[0]}U{count[1]}'
   if sum(count)<=6 and (key not in best or info['min_nonroot']>best[key]):
    best[key]=info['min_nonroot'];(out/(key+'.json')).write_text(json.dumps(info,sort_keys=True));print('BEST',k,outer,count,info['margin'],info['min_nonroot'],info['condition'],flush=True)
   if count==(1,1) and info['min_nonroot']>1e-8:
    (out/'NUMERICAL_WINNER.json').write_text(json.dumps(info,sort_keys=True));break
   if info['margin']>1e-8:break
  if (out/'NUMERICAL_WINNER.json').exists():break
  if k%25==0:print('STEP',k,'observations',observations,'seconds',time.monotonic()-clock,flush=True)
 (out/'CONFIG.json').write_text(json.dumps(vars(a),sort_keys=True));(out/'SUMMARY.json').write_text(json.dumps(dict(cases=k+1,observations=observations,seconds=time.monotonic()-clock),sort_keys=True));print('FINITE_PSD_ROOTED_METRIC_CONE_FINISHED',k+1,observations,flush=True)
if __name__=='__main__':main()
