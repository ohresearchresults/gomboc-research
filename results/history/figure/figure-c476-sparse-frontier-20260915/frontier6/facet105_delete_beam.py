"""Finite support-plane deletion beam from literal homogeneous C602 own121.
Delete vertices of its RAW polar, but reintegrate the PHYSICAL polar hull at
its own filled centroid every time. At <=105 actual facets E<=309 without
any simpliciality assumption. Float proposals require exact maximal audits.
Usage OPENBLAS_NUM_THREADS=1 python facet105_delete_beam.py C602_A OUT
"""
import json,sys,hashlib,os
from pathlib import Path
from fractions import Fraction as F
import numpy as np,scipy
from scipy.spatial import ConvexHull,QhullError
assert __debug__;sys.set_int_max_str_digits(0)
EXPECTED='2426da394eda9520bd30b2b8b3e1f00d043697353bb6bc73658f5983653c11ec'
STEPS=34;WIDTH=4;ROOT=3;GROUP=10;MARGIN=1e-8
B=lambda o:json.dumps(o,sort_keys=True,separators=(',',':')).encode()
def exits(X):
 d=X[None,:,:]-X[:,None,:];v=np.einsum('ij,ikj->ik',X,d);den=np.linalg.norm(X,axis=1)[:,None]*np.linalg.norm(d,axis=2);np.fill_diagonal(den,1);v/=den;np.fill_diagonal(v,-np.inf);return v.max(axis=1)
class Model:
 def __init__(self,src):
  b=src.read_bytes();assert hashlib.sha256(b).hexdigest()==EXPECTED;r=json.loads(b)
  self.Q=np.array([[float(F(t,d))for t in n]for n,d in zip(r['normals'],r['offsets'])]);assert len(self.Q)==136
 def evaluate(self,keep):
  Q=self.Q[keep];dual=ConvexHull(Q);assert min(-dual.equations[:,3])>1e-7
  xp=dual.equations[:,:3]/(-dual.equations[:,3])[:,None];_,ix=np.unique(np.round(xp,GROUP),axis=0,return_index=True);X=xp[np.sort(ix)]
  hull=ConvexHull(X);T=hull.simplices.copy();t=X[T];fl=np.einsum('ij,ij->i',np.cross(t[:,1]-t[:,0],t[:,2]-t[:,0]),hull.equations[:,:3])<0;T[fl]=T[fl][:,[0,2,1]];t=X[T];ds=np.einsum('ij,ij->i',t[:,0],np.cross(t[:,1],t[:,2]));D=ds.sum();assert D>0 and min(ds)>-1e-10
  g=np.einsum('i,ij->j',ds,t.sum(axis=1))/(4*D);qids=dual.vertices;Q=Q[qids];heights=1-Q@g;assert min(heights)>0
  u=exits(X[hull.vertices]-g);s=exits(Q/heights[:,None]);ru=np.minimum(u-MARGIN,0);rs=np.minimum(s-MARGIN,0);ru[np.argmin(u)]=0;rs[np.argmin(s)]=0
  return dict(S=int(sum(s<0)),U=int(sum(u<0)),V_est=len(hull.vertices),F_est=len(qids),E_est=len(hull.vertices)+len(qids)-2,hinge_cost=float(ru@ru+rs@rs),keep_C602_maximal_support_labels=np.array(keep)[qids].tolist(),S_C602_support_labels=np.array(keep)[qids][s<0].tolist(),own_raw_centroid=g.tolist(),ordinary_volume=float(D/6),primal_second=float(np.sort(u)[1]),polar_second=float(np.sort(s)[1]),nearU=int(sum(abs(u)<1e-10)),nearS=int(sum(abs(s)<1e-10)),proposal_only=True)
def total(r):return(r['S']+r['U'],r['U'],r['hinge_cost'],r['E_est'])
def firstU(r):return(r['U'],r['S'],r['hinge_cost'],r['E_est'])
def main(src,out):
 m=Model(src);initial=m.evaluate(list(range(136)));print('FACET105_BASE',initial,flush=True);assert(initial['S'],initial['U'],initial['E_est'])==(1,2,301)
 beam=[initial];levels=[];trials=[];best=None
 for step in range(STEPS):
  seen=set();cand=[]
  for parent,p in enumerate(beam):
   for k in p['keep_C602_maximal_support_labels']:
    if k==ROOT:continue
    keep=tuple(i for i in p['keep_C602_maximal_support_labels'] if i!=k)
    if keep in seen:continue
    seen.add(keep)
    try:
     r=m.evaluate(list(keep));r.update(step=step,parent=parent,deleted=k);trials.append(r)
     if not r['nearU'] and not r['nearS']:cand.append(r)
    except(QhullError,ValueError,AssertionError,np.linalg.LinAlgError)as e:trials.append(dict(step=step,parent=parent,deleted=k,error=type(e).__name__))
  if not cand:break
  choices=sorted(cand,key=total)[:2]+sorted(cand,key=firstU)[:2];chosen={tuple(r['keep_C602_maximal_support_labels']):r for r in choices}
  if len(chosen)<WIDTH:
   for r in sorted(cand,key=total):
    chosen.setdefault(tuple(r['keep_C602_maximal_support_labels']),r)
    if len(chosen)==WIDTH:break
  beam=list(chosen.values());levels.append(beam);qual=[r for r in beam if r['F_est']<=105]
  if qual:
   v=min(qual,key=total)
   if best is None or total(v)<total(best):best=v
  report=dict(status='NUMERICAL_PHYSICAL_HULL_SUPPORT_DELETION_BEAM',source_sha256=EXPECTED,steps_requested=STEPS,beam_width=WIDTH,protected_stable_support=ROOT,group_digits=GROUP,margin=MARGIN,numpy=np.__version__,scipy=scipy.__version__,openblas_threads=os.environ.get('OPENBLAS_NUM_THREADS'),initial=initial,levels=levels,trials=trials,best_facet_budget_candidate=best);out.write_bytes(B(report))
  r=min(beam,key=total);print('FACET105',step,'S/U',r['S'],r['U'],'F',r['F_est'],'E',r['E_est'],'cost',r['hinge_cost'],flush=True)
  if any(r['S']==r['U']==1 and r['E_est']<=310 for r in beam):print('FACET105_NUMERICAL110_NEEDS_EXACT_GATE',flush=True);break
 print('FACET105_DELETE_BEAM_TERMINAL',len(levels),len(trials),hashlib.sha256(out.read_bytes()).hexdigest(),flush=True)
if __name__=='__main__':main(*map(Path,sys.argv[1:]))
