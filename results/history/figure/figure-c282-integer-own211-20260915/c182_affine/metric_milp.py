"""Finite PSD outer-approximation search for a single-root escape metric.
No numerical infeasibility status is an exact mathematical exclusion.
The input audit and raw object are hash-bound by affine_search.load.
"""
import argparse,itertools,json,time
from pathlib import Path
import numpy as np
from scipy.optimize import Bounds,LinearConstraint,milp
from scipy.sparse import coo_matrix
from affine_search import load

def form(u,v):
 return np.array([u[0]*v[0],u[1]*v[1],u[2]*v[2],u[0]*v[1]+u[1]*v[0],u[0]*v[2]+u[2]*v[0],u[1]*v[2]+u[2]*v[1]])
def matrix(g):return np.array([[g[0],g[3],g[4]],[g[3],g[1],g[5]],[g[4],g[5],g[2]]])
def main():
 p=argparse.ArgumentParser();p.add_argument('--audit',required=True);p.add_argument('--raw',required=True);p.add_argument('--out',required=True);p.add_argument('--side',choices=['primal','polar'],default='primal');p.add_argument('--steps',type=int,default=20);p.add_argument('--seconds',type=float,default=15);p.add_argument('--floor',type=float,default=1e-5);p.add_argument('--margin',type=float,default=1e-7);a=p.parse_args()
 P,Q,ep,eq,W=load(a.audit,a.raw);X=P@W.T if a.side=='primal' else Q@np.linalg.inv(W);adj=ep if a.side=='primal' else eq
 arcs=[(i,j) for i,nb in enumerate(adj) for j in sorted(nb)];C=np.array([form(X[i]/np.linalg.norm(X[i]),(X[j]-X[i])/np.linalg.norm(X[j]-X[i])) for i,j in arcs]);n=len(X);ne=len(arcs);nv=7+ne+n;tindex=nv-1
 lb=np.r_[np.zeros(3),np.full(3,-.5),np.zeros(ne+n),a.margin];ub=np.r_[np.ones(3),np.full(3,.5),np.ones(ne+n),1.]
 obj=np.zeros(nv);obj[tindex]=-1;integ=np.r_[np.zeros(6),np.ones(ne+n),0]
 rows=[];lower=[];upper=[]
 def add(dic,l,u):rows.append(dic);lower.append(l);upper.append(u)
 add({0:1,1:1,2:1},1,1)
 add({6+ne+i:1 for i in range(n)},1,1)
 for i in range(n):add({**{6+k:1 for k,(s,j) in enumerate(arcs) if s==i},6+ne+i:1},1,np.inf)
 for k,c in enumerate(C):add({**{j:v for j,v in enumerate(c)},6+k:-2,tindex:-1},-2,np.inf)
 dirs=[]
 for vv in itertools.product([-1,0,1],repeat=3):
  if not any(vv) or next(x for x in vv if x)!=1:continue
  v=np.array(vv,float);v/=np.linalg.norm(v);dirs.append(v.tolist());add(dict(enumerate(form(v,v))),a.floor,np.inf)
 out=Path(a.out);out.mkdir(parents=True,exist_ok=False);records=[]
 for step in range(a.steps):
  ii=[];jj=[];dd=[]
  for i,dic in enumerate(rows):
   for j,v in dic.items():ii.append(i);jj.append(j);dd.append(v)
  M=coo_matrix((dd,(ii,jj)),shape=(len(rows),nv)).tocsc();tic=time.monotonic()
  r=milp(obj,integrality=integ,bounds=Bounds(lb,ub),constraints=LinearConstraint(M,lower,upper),options={'time_limit':a.seconds,'mip_rel_gap':0.,'presolve':True})
  rec={'step':step,'status':int(r.status),'message':r.message,'constraint_count':len(rows),'elapsed_seconds':time.monotonic()-tic}
  if r.x is not None:
   G=matrix(r.x[:6]);vals,vec=np.linalg.eigh(G);w=C@r.x[:6];scores=np.array([max(w[k] for k,(s,j) in enumerate(arcs) if s==i) for i in range(n)]);rec.update(G=G.tolist(),eigenvalues=vals.tolist(),margin=float(r.x[tindex]),scores=scores.tolist(),negative_vertices=np.where(scores<0)[0].tolist(),selected_arcs=[list(arcs[k]) for k in range(ne) if r.x[6+k]>.5],root_variables=np.where(r.x[6+ne:6+ne+n]>.5)[0].tolist(),solver_dual_bound=None if r.mip_gap is None else float(r.mip_dual_bound),gap=None if r.mip_gap is None else float(r.mip_gap))
   for j,e in enumerate(vals):
    if e<a.floor-1e-9:
     v=vec[:,j];dirs.append(v.tolist());add(dict(enumerate(form(v,v))),a.floor,np.inf)
   if min(vals)>=a.floor-1e-9 and sum(scores<0)==1:
    L=np.linalg.cholesky(G).T;T=L@W if a.side=='primal' else np.linalg.inv(L).T@W;rec['physical_transform']=T.tolist();rec['physical_condition']=float(np.linalg.cond(T));(out/'CANDIDATE.json').write_text(json.dumps(rec,sort_keys=True,separators=(',',':')));records.append(rec);print('NUMERICAL_SINGLE_ROOT_METRIC_FOUND',step,rec['margin'],rec['negative_vertices'],rec['physical_condition'],flush=True);break
  records.append(rec);print('STEP',step,'status',r.status,'eig',rec.get('eigenvalues'),'margin',rec.get('margin'),flush=True)
  (out/'SEARCH.json').write_text(json.dumps({'parameters':vars(a),'whitener':W.tolist(),'directions':dirs,'records':records},sort_keys=True,separators=(',',':')))
  if r.x is None:break
 (out/'SEARCH.json').write_text(json.dumps({'parameters':vars(a),'whitener':W.tolist(),'directions':dirs,'records':records},sort_keys=True,separators=(',',':')))
 print('C182_METRIC_MILP_FINISHED',a.side,len(records),flush=True)
if __name__=='__main__':main()
