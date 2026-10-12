"""Two complementary finite positive-chord chains replacing a secondary U basin."""
import os
os.environ['OPENBLAS_NUM_THREADS']='1'
import numpy as np,json,pathlib,time,itertools
from geometry import halfspace_mesh,census,arrows
from audit_exact import R
from bridge_scout import supports
from basin_scout import balance,score

def main():
 out=pathlib.Path('artifacts/kf27d-two-arcs');out.mkdir(parents=True,exist_ok=True);hh=json.load(open('sources/peer-agent2-KF27D-H_exact.json'))['H'];Q=np.array([[float(R(v,r[3])) for v in r[:3]] for r in hh]);m=halfspace_mesh(Q);X=m['X']-m['g'];uu=np.flatnonzero(arrows(X).max(1)<0);uu=uu[np.argsort(np.linalg.norm(X[uu],axis=1))];v0,v1=X[uu];r0,r1=np.linalg.norm(v0),np.linalg.norm(v1);u0,u1=v0/r0,v1/r1;theta=np.arccos(u0@u1);e=(u1-np.cos(theta)*u0)/np.sin(theta);normal=np.cross(u0,e)
 def chain(n,angle,bend,allocation):
  t=np.linspace(0,1,n+1);U=np.cos(t*angle)[:,None]*u0+np.sin(t*angle)[:,None]*e+bend*np.sin(np.pi*t)[:,None]*normal;U/=np.linalg.norm(U,axis=1)[:,None];cs=np.sum(U[:-1]*U[1:],axis=1)
  if cs.min()<=0:return None
  need=-np.log(cs);spare=np.log(r1/r0)-need.sum()
  if spare<=1e-4:return None
  inc=need+spare*(.002+.998*allocation)/n;rr=r0*np.exp(np.cumsum(inc));return rr[:-1,None]*U[1:-1]
 records=[];best=999;bestcount=999;t0=time.time()
 for n0,n1,b0,b1,a0,a1 in itertools.product([10,14],[28,36],[-.6,0,.6],[-.6,0,.6],[0,.6,1],[0,.6,1]):
  A=chain(n0,theta,b0,a0);B=chain(n1,theta-2*np.pi,b1,a1)
  if A is None or B is None:continue
  W=np.vstack([X,A,B]);assert np.sum(arrows(W).max(1)<0)==1
  try:
   H=supports(W);mm=halfspace_mesh(H);st=census(mm);refS=int(np.sum(arrows(H).max(1)<-1e-10));row=dict(parameters=[n0,n1,b0,b1,a0,a1],referenceS=refS,closed=False,**st);records.append(row)
   if st['E']>=250:continue
   for closed in [False,True]:
    HQ,b=(balance(H) if closed else (H,np.zeros(3)));s=score(HQ);rr=dict(parameters=[n0,n1,b0,b1,a0,a1],referenceS=refS,closed=closed,shift=b.tolist(),**s);records.append(rr)
    if s['E']<250 and s['score']<best:
     best=s['score'];np.savez(out/'best.npz',Q=HQ,raw_points=W);(out/'best.json').write_text(json.dumps(rr,indent=2));print('BEST',rr['parameters'],closed,'SU',s['S'],s['U'],'E',s['E'],'refS',refS,'score',best,'seconds',time.time()-t0,flush=True)
    if s['E']<250 and s['S']+s['U']<bestcount:
     bestcount=s['S']+s['U'];np.savez(out/'best-count.npz',Q=HQ,raw_points=W);(out/'best-count.json').write_text(json.dumps(rr,indent=2))
    if s['E']<250 and s['S']==s['U']==1 and min(s['min_primal_nonroot'],s['min_polar_nonroot'])>1e-9:
     np.savez(out/'NOMINATION110.npz',Q=HQ,raw_points=W);(out/'NOMINATION110.json').write_text(json.dumps(rr,indent=2));print('NUMERIC110_REQUIRES_EXACT',flush=True);return
  except Exception as err:records.append(dict(parameters=[n0,n1,b0,b1,a0,a1],error=str(err)))
  if len(records)%20<3:(out/'history.json').write_text(json.dumps(records,separators=(',',':')))
 (out/'history.json').write_text(json.dumps(records,separators=(',',':')));print('DONE',len(records),'best',best,'bestcount',bestcount,flush=True)
if __name__=='__main__':main()
