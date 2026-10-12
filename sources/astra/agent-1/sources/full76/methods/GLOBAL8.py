"""Eight physical global variables with true recomputation of uniform filled mass.
X'=B X/(1+u.X), Q'=B^{-T}(Q+u), B=(1+u_z)A,
A=[[exp(a),0,0],[b,exp(c),0],[d,e,1]]. Apex001 is retained.
Numerical discovery only. Exact inputs are the audited raw H body and rational
matrix/translation serialized after quantization; no reference centre is used.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import json,sys,math,time,argparse,hashlib
from pathlib import Path
from fractions import Fraction as F
import numpy as np
from scipy.optimize import least_squares
sys.set_int_max_str_digits(0)
BLOB=lambda x:json.dumps(x,sort_keys=True,separators=(',',':')).encode()
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--audit',type=Path,required=True);ap.add_argument('--out',type=Path,required=True);ap.add_argument('--starts',type=int,default=12);ap.add_argument('--steps',type=int,default=1000);ap.add_argument('--seed',type=int,default=420624);a=ap.parse_args();a.out.mkdir(parents=True,exist_ok=False);raw=json.load(open(a.audit/'raw.json'));rep=json.load(open(a.audit/'A.json'));Q=np.array([[float(F(x,r[-1])) for x in r[:3]] for r in raw['H']]);X=np.array([[float(F(t)) for t in row] for row in rep['raw_vertices']]);tri=np.array([(cy[0],cy[j],cy[j+1]) for cy in rep['faces'] for j in range(1,len(cy)-1)]);U=next(i for i,x in enumerate(X) if list(x)==[0,0,1]);S=rep['active_input_indices'][rep['stable_face_ids'][0]];active=rep['active_input_indices'];Q=Q[active];S=active.index(S)
 def edges_domain(edges,n):
  ed=np.array([e for p in edges for e in [p,p[::-1]]]);return ed[:,0],ed[:,1],[[k for k,(i,j) in enumerate(ed) if i==v] for v in range(n)]
 ep=edges_domain(rep['edges'],len(X));dual=set()
 for i,j in rep['edges']:
  ff=[f for f,cy in enumerate(rep['faces']) if i in cy and j in cy];assert len(ff)==2;dual.add(tuple(ff))
 eq=edges_domain(sorted(dual),len(Q));keep1=[i for i in range(len(X)) if i!=U];keep2=[i for i in range(len(Q)) if i!=S];last={}
 def escape(Z,ed):
  i,j,adj=ed;e=Z[j]-Z[i];val=np.einsum('ij,ij->i',Z[i],e)/np.sqrt(np.maximum(np.sum(Z[i]**2,axis=1)*np.sum(e**2,axis=1),1e-40));return np.array([max(val[g]) for g in adj])
 def evaluate(p):
  A=np.array([[np.exp(p[0]),0,0],[p[2],np.exp(p[1]),0],[p[3],p[4],1.]]);u=p[5:];B=(1+u[2])*A;den=1+X@u;xx=(X@B.T)/den[:,None];qq=(Q+u)@np.linalg.inv(B);tr=xx[tri];v6=np.einsum('ij,ij->i',tr[:,0],np.cross(tr[:,1],tr[:,2]));V=v6.sum()/6;g=(v6[:,None]*tr.sum(1)).sum(0)/(24*V);h=1-qq@g;H=qq/h[:,None];vp=escape(xx-g,ep);vq=escape(H,eq);values=np.r_[vp[keep1],vq[keep2],-vp[U],-vq[S]];return values,den,V,g,A,u,h
 goal=1e-7;floor=np.r_[np.full(len(X)+len(Q)-2,goal),1e-7,1e-7]
 def residual(p):
  v,de,V,g,A,u,h=evaluate(p);return np.r_[np.maximum(floor-v,0),np.maximum(.05-de,0)*10,np.maximum(.05-h,0)*10,max(.01-V,0)*10]
 rng=np.random.default_rng(a.seed);records=[];best=(float('inf'),None)
 for k in range(a.starts):
  p=np.zeros(8) if k==0 else rng.normal(size=8)*[.003,.01,.03,.1][(k-1)%4];ans=least_squares(residual,p,bounds=([-1,-1,-1,-1,-1,-.4,-.4,-.4],[1,1,1,1,1,.4,.4,.4]),max_nfev=a.steps,ftol=1e-13,xtol=1e-13,gtol=1e-13,diff_step=1e-5);v,de,V,g,A,u,h=evaluate(ans.x);score=float(residual(ans.x)@residual(ans.x));row=dict(start=k,score=score,minimum=float(v.min()),counts_SU=[int(sum(v[len(keep1):len(keep1)+len(keep2)]<0)+(v[-1]>0)),int(sum(v[:len(keep1)]<0)+(v[-2]>0))],nfev=ans.nfev,parameters=[float(x).hex() for x in ans.x]);records.append(row);print('GLOBAL8',json.dumps(row),flush=True)
  if score<best[0]:
   best=(score,ans.x.copy());data=dict(scale=10**12,A=np.rint(A*10**12).astype(np.int64).tolist(),u=np.rint(u*10**12).astype(np.int64).tolist(),parameters=row['parameters'],input_raw_sha256=hashlib.sha256(BLOB(raw)).hexdigest(),formula='B=(1+u_z)*A; Qnew=B^-T*(Q+u)');(a.out/'GLOBAL.json').write_bytes(BLOB(data));(a.out/'SOURCE_RAW.json').write_bytes(BLOB(raw))
  (a.out/'RECORDS.json').write_bytes(BLOB(records))
  if v.min()>goal*.9 and de.min()>.05 and h.min()>.05:break
 (a.out/'INPUT.json').write_bytes(BLOB(dict(seed=a.seed,starts=a.starts,steps=a.steps,goal=goal,numpy=np.__version__)));print('GLOBAL8_END_NUMERICAL_ONLY',best[0],flush=True)
if __name__=='__main__':main()
