"""Greedy actual convex-hull vertex removal proposals from C486 affine334.
Usage: OPENBLAS_NUM_THREADS=1 python primal334_delete_screen.py R12_A OUT
Floating support grouping is proposal-only; every promising finite set needs exact hull audits.
"""
import json,sys,hashlib,itertools,os
from pathlib import Path
from fractions import Fraction
import numpy as np
from scipy.spatial import ConvexHull,QhullError
import scipy
import REPLAY_AFFINE334 as aff
assert __debug__;sys.set_int_max_str_digits(0)
ROUNDS=12;ROUND=10;TOL=1e-10
B=lambda x:json.dumps(x,sort_keys=True,separators=(',',':')).encode()
class Model:
 def __init__(self,path):
  b=path.read_bytes();assert hashlib.sha256(b).hexdigest()==aff.SOURCES['A.json'];r=json.loads(b)
  self.P=np.array([[float(Fraction(s)) for s in v] for v in r['raw_vertices']]);self.w=np.array(aff.W)/aff.D;self.A=np.array(aff.AA)/aff.D
 def evaluate(self,keep):
  P=self.P[keep];h=ConvexHull(P)
  if min(-h.equations[:,3])<=1e-8:raise ValueError('origin too close to hull boundary')
  T=h.simplices.copy();p=P[T];sg=np.einsum('ij,ij->i',np.cross(p[:,1]-p[:,0],p[:,2]-p[:,0]),h.equations[:,:3]);fl=sg<0;T[fl]=T[fl][:,[0,2,1]]
  Y=P/(1+P@self.w)[:,None];t=Y[T];ds=np.einsum('ij,ij->i',t[:,0],np.cross(t[:,1],t[:,2]));V=ds.sum()/6;g=np.einsum('i,ij->j',ds,t.sum(axis=1))/(24*V)
  assert min(ds)>-1e-12 and V>0
  Q=h.equations[:,:3]/(-h.equations[:,3])[:,None];_,idx=np.unique(np.round(Q,ROUND),axis=0,return_index=True);idx=np.sort(idx);Q=Q[idx]+self.w
  pol=(Q/(1-Q@g)[:,None])@np.linalg.inv(self.A);X=(Y[h.vertices]-g)@self.A.T
  def exits(V):
   d=V[None,:,:]-V[:,None,:];v=np.einsum('ij,ikj->ik',V,d);den=np.linalg.norm(V,axis=1)[:,None]*np.linalg.norm(d,axis=2);np.fill_diagonal(den,1);v/=den;np.fill_diagonal(v,-np.inf);return v.max(axis=1)
  u=exits(X);s=exits(pol);ru=np.minimum(u-2e-7,0);rs=np.minimum(s-2e-7,0);ru[np.argmin(u)]=0;rs[np.argmin(s)]=0
  S=int(sum(s<0));U=int(sum(u<0));E=len(h.vertices)+len(Q)-2
  return dict(S=S,U=U,V_est=len(h.vertices),F_est=len(Q),E_est=E,cost=float(ru@ru+rs@rs),U_original_R12_labels=np.array(keep)[h.vertices][u<0].tolist(),S_triangles_original_R12_labels=np.array(keep)[h.simplices[idx]][s<0].tolist(),nearU=np.flatnonzero(abs(u)<TOL).tolist(),nearS=np.flatnonzero(abs(s)<TOL).tolist(),keep_original_R12_labels=keep,exposed_original_R12_labels=np.array(keep)[h.vertices].tolist(),projected_actual_centroid=g.tolist(),physical_actual_centroid=(self.A@g).tolist(),projected_volume=float(V),proposal_only=True)
def main(src,out):
 m=Model(src);rows=[];keeps=list(range(118));baseline=m.evaluate(keeps);assert (baseline['S'],baseline['U'])==(3,3)
 branches=[('total',lambda r:(r['S']+r['U'],r['cost'],r['E_est'])),('Ufirst',lambda r:(r['U'],r['S'],r['cost'],r['E_est']))]
 alltrials=[]
 for name,score in branches:
  keep=keeps[:];best=m.evaluate(keep);path=[]
  for step in range(ROUNDS):
   cand=[]
   for k in keep:
    if k==79:continue
    kk=[i for i in keep if i!=k]
    try:r=m.evaluate(kk)
    except (QhullError,ValueError,AssertionError,np.linalg.LinAlgError) as e:
     alltrials.append(dict(branch=name,step=step,delete=k,error=type(e).__name__));continue
    r.update(delete=k,step=step,branch=name);alltrials.append(r)
    if r['E_est']<=310 and not r['nearU'] and not r['nearS']:cand.append(r)
   if not cand:break
   new=min(cand,key=score)
   if score(new)>=score(best):print('NO_IMPROVEMENT',name,step,score(best),score(new),flush=True);break
   best=new;keep=best['exposed_original_R12_labels'];path.append(best)
   print('PRIMAL_DELETE',name,step,'removed',sorted(set(keeps)-set(keep)),'S/U',best['S'],best['U'],'E',best['E_est'],'cost',best['cost'],flush=True)
   if best['S']==best['U']==1:break
  rows.append(dict(branch=name,path=path,final=best))
  report=dict(status='NUMERICAL_PRIMAL_DELETION_PROPOSALS_ONLY',source_sha256=aff.SOURCES['A.json'],transform_script_sha256=hashlib.sha256(Path(aff.__file__).read_bytes()).hexdigest(),rounds=ROUNDS,support_group_decimals=ROUND,tolerance=TOL,retained_root=79,numpy=np.__version__,scipy=scipy.__version__,openblas_threads=os.environ.get('OPENBLAS_NUM_THREADS'),baseline=baseline,branches=rows,trials=alltrials)
  out.write_bytes(B(report))
 print('PRIMAL334_DELETE_SCREEN_TERMINAL',len(alltrials),hashlib.sha256(out.read_bytes()).hexdigest(),flush=True)
if __name__=='__main__':main(*map(Path,sys.argv[1:]))
