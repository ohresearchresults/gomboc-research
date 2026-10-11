"""Replace expensive moment controllers without altering the two-apex Q patch.
Linear cap-volume allocation initializes the exact quadratic moment equations.
Candidate convexity, actual mass, U safety, and all root counts are rebuilt.
These are numeric nominations, not exact equilibrium claims.
"""
import json,sys
from pathlib import Path
import numpy as np
from scipy.optimize import linprog,least_squares
from capflow91 import setup
from envelope91 import hullpoly
from j90 import report
from masscaps90 import face_data
ROOT=Path(__file__).resolve().parent

def main():
 m=setup();z=m['z'];old=z['x'];src=json.loads((ROOT/'J91_OUTER2.json').read_text());primary=np.array(src['apexes'])[7:9];prime=hullpoly(np.vstack([old,primary]));M=prime['vol']*prime['g'];print('PRIMARY_ONLY',report(prime),'M',M.tolist(),flush=True)
 U=report(z)['U'][0];stable=report(z)['S'];vis=set(np.where(np.max(z['y']@primary.T,axis=1)>1+1e-10)[0]);choices=[]
 for fi,cy in z['faces'].items():
  if fi in stable or fi in vis or U in cy:continue
  c,n,A=face_data(z,fi);sl=1-z['y']@c;dn=z['y']@n;ix=[j for j in range(len(dn)) if j!=fi and dn[j]>0];cap=.7*np.min(sl[ix]/dn[ix])
  gi=np.argmax(c@(old-c).T);r0=c@(old[gi]-c);b=n@(old[gi]-2*c)
  if r0<=0:continue
  safe=(b+np.sqrt(b*b+4*r0))/2;cap=min(cap,.7*safe)
  if cap<1e-9:continue
  choices.append((int(fi),c,n,A,float(cap),len(cy)))
 C=np.array([c for fi,c,n,A,cap,k in choices]).T;bounds=[(0,A*cap/3) for fi,c,n,A,cap,k in choices];table=[];best=None;rng=np.random.default_rng(910227)
 for case in range(20):
  cost=np.array([k for fi,c,n,A,cap,k in choices],float)
  if case:cost*=np.exp(rng.normal(0,.6,len(cost)))
  bb=bounds.copy()
  if case%3==0:
   for j,item in enumerate(choices):
    if item[0]==14:bb[j]=(0,0)
  op=linprog(cost,A_eq=C,b_eq=-M,bounds=bb,method='highs')
  if not op.success:table.append(dict(case=case,reason='moment-capacity-infeasible'));continue
  sel=np.where(op.x>1e-13)[0];initial=op.x[sel];scale=max(np.max(initial),np.linalg.norm(M))
  def eq(v):
   R=M.copy()
   for j,i in enumerate(sel):
    fi,c,n,A,cap,k=choices[i];R+=v[j]*(c+3*v[j]/A*n/4)
   return R
  upper=np.array([bb[i][1] for i in sel]);sol=least_squares(lambda v:eq(v*scale)/scale,initial/scale,bounds=(np.zeros(len(sel)),upper/scale),xtol=1e-13,gtol=1e-13,ftol=1e-13,max_nfev=500);vv=sol.x*scale
  if max(abs(eq(vv)))>1e-13:table.append(dict(case=case,reason='quadratic-moment-infeasible',residual=eq(vv).tolist()));continue
  caps=[];ids=[]
  for j,i in enumerate(sel):
   fi,c,n,A,cap,k=choices[i];caps.append(c+3*vv[j]/A*n);ids.append(fi)
  w=np.vstack([caps,primary]);guards=np.einsum('ik,ijk->ij',w,old[None]-w[:,None]).max(1)
  try:zz=hullpoly(np.vstack([old,w]));rr=report(zz)
  except Exception as e:table.append(dict(case=case,reason=str(e)));continue
  rec=dict(case=case,controller_faces=ids,report=rr,pyramid_residual=eq(vv).tolist(),min_U_safe=float(guards.min()));table.append(rec)
  if max(abs(zz['g']))>1e-12 or min(guards)<=1e-10 or len(rr['S'])!=2 or len(rr['U'])!=1 or rr['E']>249:continue
  key=(rr['E'],rr['Q'][0]['depth'])
  if best is None or key<best:
   best=key;print('REBALANCE_BEST',key,rec,flush=True);(ROOT/'J91_REBALANCED.json').write_text(json.dumps(dict(base='J90_DETACHED_C390_G8',frame_shift=m['g'].tolist(),apexes=w.tolist(),controller_faces=ids,primary_count=2,info=rec),indent=2)+'\n')
 (ROOT/'J91_REBALANCE_SCAN.json').write_text(json.dumps(dict(seed=910227,choices=[dict(face=i,centre=c.tolist(),normal=n.tolist(),area=A,height_cap=cap,cost=k) for i,c,n,A,cap,k in choices],primary=primary.tolist(),primary_moment=M.tolist(),results=table),indent=2)+'\n');print('J91_REBALANCE_NUMERICAL_FINISHED',best,flush=True)
if __name__=='__main__':main()
