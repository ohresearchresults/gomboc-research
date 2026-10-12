"""Finite primal escape chains plus physical projective mass closure.
The complete raw augmented points and rebuilt body are retained for each best case.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1'
import numpy as np,json,pathlib,time,argparse
from scipy.spatial import ConvexHull
from geometry import halfspace_mesh,census,arrows
from audit_exact import R
from basin_scout import balance,score

def supports(X):
 h=ConvexHull(X);rows=[]
 for e in h.equations:
  if e[3]>=0:raise ValueError('origin outside physical hull')
  q=e[:3]/(-e[3])
  if not any(np.max(abs(q-v))<1e-8 for v in rows):rows.append(q)
 return np.array(rows)

def run(out):
 out=pathlib.Path(out);out.mkdir(parents=True,exist_ok=True);hh=json.load(open('sources/peer-agent2-KF27D-H_exact.json'))['H'];Q=np.array([[float(R(v,row[3])) for v in row[:3]] for row in hh]);m=halfspace_mesh(Q);X=m['X']-m['g'];uu=np.flatnonzero(arrows(X).max(1)<0);uu=uu[np.argsort(np.linalg.norm(X[uu],axis=1))];v0,v1=X[uu];r0,r1=np.linalg.norm(v0),np.linalg.norm(v1);u0,u1=v0/r0,v1/r1;theta=np.arccos(u0@u1);normal=np.cross(u0,u1);normal/=np.linalg.norm(normal);records=[];best=999.;t0=time.time()
 for n in [9,10,12,15,18,22,28]:
  for bend in np.linspace(-1.2,1.2,13):
   t=np.linspace(0,1,n+1);U=(np.sin((1-t)*theta)[:,None]*u0+np.sin(t*theta)[:,None]*u1)/np.sin(theta)+bend*np.sin(np.pi*t)[:,None]*normal;U/=np.linalg.norm(U,axis=1)[:,None];cos=np.sum(U[:-1]*U[1:],axis=1)
   if cos.min()<=0:continue
   required=-np.log(cos);spare=np.log(r1/r0)-required.sum()
   if spare<=1e-4:continue
   for allocation in [0.,.25,.5,1.]:
    increments=required+spare*.002/n+allocation*spare*.998/n;rr=r0*np.exp(np.cumsum(increments));Y=rr[:-1,None]*U[1:-1];W=np.vstack([X,Y]);ref=arrows(W).max(1);assert np.sum(ref<0)==1
    try:
     H=supports(W);mm=halfspace_mesh(H);st=census(mm);row=dict(n=n,bend=float(bend),allocation=allocation,mass_closed=False,**st);records.append(row)
     if st['E']<250:
      for close in [False,True]:
       HQ,shift=(balance(H) if close else (H,np.zeros(3)));s=score(HQ);rrr=dict(n=n,bend=float(bend),allocation=allocation,mass_closed=close,shift=shift.tolist(),**s);records.append(rrr)
       if s['E']<250 and s['score']<best:
        best=s['score'];np.savez(out/'best.npz',Q=HQ,raw_points=W);(out/'best.json').write_text(json.dumps(rrr,indent=2));print('BEST',n,bend,allocation,close,s['S'],s['U'],s['E'],best,'seconds',time.time()-t0,flush=True)
       if s['E']<250 and s['S']==s['U']==1 and min(s['min_primal_nonroot'],s['min_polar_nonroot'])>1e-9:
        np.savez(out/'NOMINATION110.npz',Q=HQ,raw_points=W);(out/'NOMINATION110.json').write_text(json.dumps(rrr,indent=2));print('NUMERIC110_REQUIRES_EXACT',flush=True);return
    except Exception as e:records.append(dict(n=n,bend=float(bend),allocation=allocation,error=str(e)))
  (out/'history.json').write_text(json.dumps(records,separators=(',',':')));print('N_DONE',n,'best',best,flush=True)
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--out',required=True);a=ap.parse_args();run(a.out)
