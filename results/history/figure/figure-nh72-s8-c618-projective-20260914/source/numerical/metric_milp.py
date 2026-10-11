"""Finite MILP exploration of positive-definite metrics in rotated DD subcones.
Its finite failures do not exclude the full metric or projective orbit.
"""
import os
os.environ.setdefault('OPENBLAS_NUM_THREADS','1');os.environ.setdefault('OMP_NUM_THREADS','1')
import sys,json,argparse,time,warnings
from pathlib import Path
import numpy as np
from scipy.optimize import milp,Bounds,LinearConstraint
from scipy.sparse import lil_matrix
from centroid_metric import CentroidOrbit

def decode(v):return np.array([[v[0],v[3],v[4]],[v[3],v[1],v[5]],[v[4],v[5],v[2]]])
def cone_problem(X,edges,root,seconds=8):
 src,dst=edges;choose=np.where(src!=root)[0];src=src[choose];dst=dst[choose];e=X[dst]-X[src];p=X[src]
 coef=np.c_[p*e,p[:,0]*e[:,1]+p[:,1]*e[:,0],p[:,0]*e[:,2]+p[:,2]*e[:,0],p[:,1]*e[:,2]+p[:,2]*e[:,1]]
 coef/= (np.linalg.norm(p,axis=1)*np.linalg.norm(e,axis=1))[:,None]
 n=len(choose);nv=7+n;nr=1+12+len(X)-1+n;C=lil_matrix((nr,nv));lo=np.full(nr,-np.inf);hi=np.full(nr,np.inf);row=0
 C[row,:3]=1;lo[row]=hi[row]=1;row+=1
 for i,js in [(0,[3,4]),(1,[3,5]),(2,[4,5])]:
  for s in [-1,1]:
   for t in [-1,1]:
    C[row,i]=1;C[row,js[0]]=s;C[row,js[1]]=t;lo[row]=1e-5;row+=1
 for i in range(len(X)):
  if i==root:continue
  C[row,7+np.where(src==i)[0]]=1;lo[row]=1;row+=1
 for k in range(n):
  C[row,:6]=coef[k];C[row,6]=-1;C[row,7+k]=-1.1;lo[row]=-1.1;row+=1
 assert row==nr
 lower=np.r_[[0,0,0,-.5,-.5,-.5,1e-9],np.zeros(n)];upper=np.r_[[1,1,1,.5,.5,.5,.1],np.ones(n)]
 c=np.zeros(nv);c[6]=-1
 with warnings.catch_warnings():
  warnings.simplefilter('ignore')
  result=milp(c,integrality=np.r_[np.zeros(7),np.ones(n)],bounds=Bounds(lower,upper),constraints=LinearConstraint(C.tocsr(),lo,hi),options={'time_limit':seconds,'mip_rel_gap':.05,'threads':1,'mip_feasibility_tolerance':1e-9})
 if result.x is None:return None,dict(status=int(result.status),message=str(result.message))
 G=decode(result.x[:6]);values=coef@result.x[:6];best=np.full(len(X),-np.inf);np.maximum.at(best,src,values);best[root]=np.inf
 return G,dict(status=int(result.status),gamma=float(result.x[6]),actual_minimum=float(best.min()),eigenvalues=np.linalg.eigvalsh(G).tolist(),message=str(result.message))
def counts(m,t,A):
 y,g,K,d,V=m.state(t);P=(y-g)@A.T;Y=(m.q+t)/(1-(m.q+t)@g)[:,None];Y=Y@np.linalg.inv(A)
 out=[]
 for X,(src,dst),n in zip((P,Y),m.edges,m.ns):
  v=np.einsum('ni,ni->n',X[src],X[dst]-X[src]);best=np.full(n,-np.inf);np.maximum.at(best,src,v);out.append(np.where(best<0)[0].tolist())
 return dict(U=out[0],S=out[1],t=t.tolist(),A=A.tolist(),b=g.tolist(),min_den=float(d.min()),condition=float(np.linalg.cond(A)))
def main():
 p=argparse.ArgumentParser();p.add_argument('report');p.add_argument('out');p.add_argument('--cases',type=int,default=30);p.add_argument('--seconds',type=float,default=8);p.add_argument('--seed',type=int,default=721309);a=p.parse_args();m=CentroidOrbit(a.report);out=Path(a.out);out.mkdir(exist_ok=False);rng=np.random.default_rng(a.seed);r=m.report;clock=time.monotonic()
 for k in range(a.cases):
  target=m.b0.copy() if k<4 else (np.zeros(3) if k<8 else rng.normal(size=3)*10**rng.uniform(-1.5,1))
  t,y,g,K,d,V,err=m.invert(target);cov=(K-np.outer(g,g))/5
  B=np.eye(3)
  if k>=2:
   Q,R=np.linalg.qr(rng.normal(size=(3,3)));Q[:,0]*=np.linalg.det(Q)
   B=Q@np.linalg.inv(np.linalg.cholesky(cov));B/=np.linalg.det(B)**(1/3)
  mode=k%2
  X=(y-g)@B.T if mode==0 else ((m.q+t)/(1-(m.q+t)@g)[:,None])@np.linalg.inv(B)
  candidate_roots=r['unstable_vertices'] if mode==0 else r['stable_face_ids']
  root=int(candidate_roots[(k//2)%len(candidate_roots)]) if k<8 else int(np.argmax(np.einsum('ni,ni->n',X,X)))
  G,info=cone_problem(X,m.edges[mode],root,a.seconds);info.update(case=k,mode=mode,root=root,target=target.tolist())
  if G is not None and np.linalg.eigvalsh(G).min()>0:
   A=np.linalg.cholesky(G if mode==0 else np.linalg.inv(G)).T@B;A/=np.linalg.det(A)**(1/3)
   info.update(counts(m,t,A))
   if len(info['S'])==len(info['U'])==1:(out/f'NUMERICAL_WINNER_{k}.json').write_text(json.dumps(info,sort_keys=True))
   (out/f'CASE_{k}.json').write_text(json.dumps(info,sort_keys=True))
  with (out/'ALL.jsonl').open('a') as f:f.write(json.dumps(info,sort_keys=True)+'\n')
  print(k,info['status'],info.get('actual_minimum'),len(info.get('S',[])),len(info.get('U',[])),flush=True)
 (out/'CONFIG.json').write_text(json.dumps(vars(a),sort_keys=True));print('FINITE_DD_METRIC_MILP_FINISHED',a.cases,'seconds',time.monotonic()-clock,flush=True)
if __name__=='__main__':main()
