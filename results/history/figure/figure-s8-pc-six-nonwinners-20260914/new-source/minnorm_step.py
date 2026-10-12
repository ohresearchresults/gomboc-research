"""One exact-input numerical SQP proposal; it is not an exact body certificate."""
import json,sys,time
from pathlib import Path
import numpy as np
from scipy.linalg import svd
from forest_repair import Atlas,paths,mechanics
from minnorm_qp import solve
R=Path(__file__).resolve().parent; inp=R/sys.argv[1]; gain=float(sys.argv[2]); out=R/sys.argv[3]
out.mkdir(exist_ok=False)
d=json.loads((inp/'GENERATOR.json').read_text());a=json.loads((inp/'A.json').read_text());fs=a['faces'];m=Atlas(d,fs);u=m.u0.copy()
ums=np.zeros((len(m.owners),len(m.owners)),bool);sms=np.zeros((m.nphys,m.nphys),bool)
for (i,j),ff in m.ef.items():ums[i,j]=ums[j,i]=True;sms[tuple(ff)]=sms[tuple(ff[::-1])]=True
s=m.state(u,False);m.uparent,_=paths(s['cu'],m.Uroot,ums,np.full(len(m.owners),1e-7));m.sparent,_=paths(s['cs'],m.Sroot,sms,np.full(m.nphys,1e-7));s=m.state(u)
goals=np.maximum(1e-7,np.minimum(.1*s['vals'],1e-4));good=s['vals']>0;bad=np.where(~good)[0];goals[bad]=np.minimum(s['vals'][bad]+gain,1e-7)
geom=np.r_[s['dq'].reshape(-1,m.np)/2,s['dP'].reshape(-1,m.np)]
_,ss,Vt=svd(geom,full_matrices=False,check_finite=False);select=ss>1e-8;W=Vt[select].T/ss[select]
vi,qi=np.where((~m.inc)&(s['gaps']<.03));G=np.r_[m.gap_jac(s,vi,qi),s['ddet']]
b=np.r_[goals-s['vals'],1e-7-s['gaps'][vi,qi],1e-10-s['det']]
A=np.r_[s['J'],G]@W
t=time.monotonic();z,rr=solve(A,b,bound=None,tol=1e-10,seconds=8,maxsteps=2500);print('QP',gain,rr,'sec',time.monotonic()-t,flush=True)
if z is not None:
 print('norms',np.linalg.norm(z),np.linalg.norm(W@z), 'linbad',s['vals'][bad]+s['J'][bad]@W@z,flush=True)
 for ls in range(16):
  step=2.**(-ls);un=u+step*(W@z);sn=m.state(un,False)
  valid=sn['gaps'][~m.inc].min()>0 and sn['det'].min()>0 and sn['h'].min()>0 and sn['vals'][good].min()>0 and sn['vals'][bad].min()>s['vals'][bad].min()
  print('STEP',step,valid,'bad',sn['vals'][bad],'good',sn['vals'][good].min(),flush=True)
  if valid:
   m.save(un,out/'GENERATOR.json');(out/'TOPOLOGY.json').write_text(json.dumps(fs,separators=(',',':')))
   rep=mechanics(sn['q'],fs,P=sn['P'],tol=1e-12);(out/'NUMERICAL.json').write_text(json.dumps(rep,sort_keys=True,separators=(',',':')))
   print('COUNTS',[len(rep[k]) for k in ('S','U','H')]);break
