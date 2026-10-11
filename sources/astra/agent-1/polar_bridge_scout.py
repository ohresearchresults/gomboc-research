"""Polar positive-chord chains on the new strict211 body; actual mass is audited."""
import os
os.environ['OPENBLAS_NUM_THREADS']='1'
import numpy as np,json,pathlib,time,argparse,itertools
from geometry import halfspace_mesh,census,arrows
from basin_scout import balance,score

def run(input,out):
 out=pathlib.Path(out);out.mkdir(parents=True,exist_ok=True);Q=np.load(input)['Q'];m=halfspace_mesh(Q);Q=Q[m['active']]/(1-Q[m['active']]@m['g'])[:,None];ss=np.flatnonzero(arrows(Q).max(1)<0);ss=ss[np.argsort(np.linalg.norm(Q[ss],axis=1))];v0,v1=Q[ss];r0,r1=np.linalg.norm(v0),np.linalg.norm(v1);u0,u1=v0/r0,v1/r1;theta=np.arccos(u0@u1);normal=np.cross(u0,u1);normal/=np.linalg.norm(normal);records=[];best=999;t0=time.time();np.savez(out/'initial.npz',Q=Q)
 for n,bend,allocation in itertools.product([12,14,16,20,24],np.linspace(-1,1,11),[0,.25,.5,.75,1.]):
  t=np.linspace(0,1,n+1);U=(np.sin((1-t)*theta)[:,None]*u0+np.sin(t*theta)[:,None]*u1)/np.sin(theta)+bend*np.sin(np.pi*t)[:,None]*normal;U/=np.linalg.norm(U,axis=1)[:,None];cs=np.sum(U[:-1]*U[1:],axis=1)
  if cs.min()<=0:continue
  need=-np.log(cs);spare=np.log(r1/r0)-need.sum()
  if spare<=1e-4:continue
  rr=r0*np.exp(np.cumsum(need+spare*(.002+.998*allocation)/n));added=rr[:-1,None]*U[1:-1];H=np.vstack([Q,added]);assert np.sum(arrows(H).max(1)<0)==1
  try:
   mm=halfspace_mesh(H);s=census(mm);records.append(dict(n=n,bend=float(bend),allocation=allocation,closed=False,**s))
   if s['E']>=250:continue
   for closed in [False,True]:
    HQ,b=(balance(H) if closed else (H,np.zeros(3)));g=score(HQ);row=dict(n=n,bend=float(bend),allocation=allocation,closed=closed,shift=b.tolist(),**g);records.append(row)
    if g['E']<250 and g['score']<best:
     best=g['score'];np.savez(out/'best.npz',Q=HQ);(out/'best.json').write_text(json.dumps(row,indent=2));print('BEST',n,bend,allocation,closed,g['S'],g['U'],g['E'],best,'seconds',time.time()-t0,flush=True)
    if g['E']<250 and g['S']==g['U']==1 and min(g['min_primal_nonroot'],g['min_polar_nonroot'])>1e-9:
     np.savez(out/'NOMINATION110.npz',Q=HQ);(out/'NOMINATION110.json').write_text(json.dumps(row,indent=2));print('NUMERIC110_REQUIRES_EXACT',flush=True);return
  except Exception as e:records.append(dict(n=n,bend=float(bend),allocation=allocation,error=str(e)))
  if len(records)%20<3:(out/'history.json').write_text(json.dumps(records,separators=(',',':')))
 (out/'history.json').write_text(json.dumps(records,separators=(',',':')));print('DONE',len(records),'best',best,flush=True)
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--input',required=True);ap.add_argument('--out',required=True);a=ap.parse_args();run(a.input,a.out)
