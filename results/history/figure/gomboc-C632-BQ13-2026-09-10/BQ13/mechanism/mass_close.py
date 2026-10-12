"""Close the actual filled first moment inside a fully guarded reference-110 cap cell.
No density change and no replacement of the physical centroid by a chosen point.
"""
import sys,json,time,argparse,numpy as np
from pathlib import Path
from scipy.linalg import svd
R=Path(__file__).resolve().parent;sys.path[:0]=[str(R),str(R/'parent_sources')]
from atlas_opt import Atlas
from contact_chart import make_chart
from numeric import mechanics,recover,topology
from live_hull import census
from minnorm_qp import solve
class MassModel:
 def __init__(self,g,fs,ref):
  self.m=Atlas(g,fs,stable=3);self.ref=np.asarray(ref);self.g0=self.m.state(self.m.u0,False)['gaps']
 def state(self,u,jac=True):
  m=self.m;s=m.state(u,jac);q=s['q'];h=1-q@self.ref;n=q/h[:,None];x=s['P']-self.ref
  def cos(z):
   d=z[None,:,:]-z[:,None,:];num=np.einsum('ic,ijc->ij',z,d);den=np.linalg.norm(z,axis=1)[:,None]*np.linalg.norm(d,axis=2);v=np.divide(num,den,out=np.full_like(num,-np.inf),where=den>1e-14);np.fill_diagonal(v,-np.inf);return v
  sc=cos(n);uc=cos(x);sw=sc[m.si].argmax(1);uw=uc[m.ui].argmax(1);s['rvals']=np.r_[sc[m.si,sw],uc[m.ui,uw]]
  if jac:
   dq=s['dq'];dh=-np.einsum('icp,c->ip',dq,self.ref);dn=dq/h[:,None,None]-q[:,:,None]*dh[:,None,:]/h[:,None,None]**2;dx=s['dP']
   def dcoss(z,dz,ii,jj):
    a=z[ii];b=z[jj]-a;da=dz[ii];db=dz[jj]-da;aa=np.einsum('ic,ic->i',a,a);bb=np.einsum('ic,ic->i',b,b);den=np.sqrt(aa*bb);uv=np.einsum('ic,ic->i',a,b);du=np.einsum('icp,ic->ip',da,b)+np.einsum('icp,ic->ip',db,a)
    return du/den[:,None]-(uv/den)[:,None]*(np.einsum('icp,ic->ip',da,a)/aa[:,None]+np.einsum('icp,ic->ip',db,b)/bb[:,None])
   s['rJ']=np.r_[dcoss(n,dn,m.si,sw),dcoss(x,dx,m.ui,uw)];mat=np.r_[dq.reshape(-1,m.np)/2,s['dP'].reshape(-1,m.np)];U,d,Vt=svd(mat,full_matrices=False,check_finite=False);s['W']=Vt.T/np.maximum(d,1e-12)
  return s
 def rows(self,s,fl):
  m=self.m;vi,qi=np.where((~m.inc)&(s['gaps']<.05));G=m.gap_jac(s,vi,qi);gf=np.maximum(1e-9,np.minimum(1e-7,self.g0[vi,qi]*.01));A=np.r_[s['rJ'],G];b=np.r_[fl-s['rvals'],gf-s['gaps'][vi,qi]];return A@s['W'],b
 def valid(self,s,fl):return s['rvals'].min()>0 and np.min(s['rvals']-fl)>-1e-11 and s['gaps'][~self.m.inc].min()>1e-10 and s['det'].min()>0 and s['h'].min()>0

def seed():
 # Interface-only recovery patch: these are the original seed()'s saved outputs.
 out=R/'cap632_seed'
 g=json.loads((out/'GENERATOR.json').read_text())
 fs=json.loads((out/'faces.json').read_text())
 ref=np.array(json.loads((out/'reference.json').read_text()),float)
 return g,fs,ref

def run(out,initial=None,seconds=24,fraction=1.,reserve=.2):
 g,fs,ref=seed();mod=MassModel(g,fs,ref);m=mod.m;u=m.u0.copy();st=mod.state(u);floors=np.minimum(1e-5,st['rvals']*reserve);assert floors.min()>0
 if initial:
  gg=json.loads(Path(initial).read_text());xx=np.array(gg['controls'],float)/gg['grid'];u=xx[m.free[:,0],m.free[:,1]]/m.scale
 out=R/out;out.mkdir(exist_ok=True);start=time.time();history=[];rad=.04
 for it in range(100):
  if time.time()-start>seconds:break
  s=mod.state(u);err=ref-s['c'];norm=np.linalg.norm(err);rec={'it':it,'err':err.tolist(),'norm':norm,'min_reference_cos':float(s['rvals'].min()),'fraction':fraction,'sec':time.time()-start};history.append(rec);print('MASS',rec,flush=True)
  m.save(u,out/'LATEST.json');(out/'faces.json').write_text(json.dumps(fs,separators=(',',':')));(out/'history.json').write_text(json.dumps(history,indent=2))
  if norm<2e-13 and mod.valid(s,floors):print('MASS_NUMERICAL_SUCCESS',mechanics(s['q'],fs,P=s['P'],tol=1e-12),flush=True);break
  A,b=mod.rows(s,floors*1.04);E=s['dc']@s['W'];d,why=solve(A,b,E,err*fraction,bound=rad,seconds=1.5,maxsteps=1800,tol=1e-10)
  if d is None:print('MASS_QPFAIL',why,flush=True);fraction*=.5;continue
  print('MASS_STEP_NORM',np.linalg.norm(d),flush=True);acc=False
  for ls in range(7):
   lam=2.**-ls;un=u+lam*(s['W']@d);target=s['c']+lam*fraction*err
   for rp in range(8):
    try:sn=mod.state(un)
    except Exception:break
    if mod.valid(sn,floors) and np.linalg.norm(sn['c']-target)<max(1e-13,.01*norm*lam*fraction):
     u=un;acc=True;fraction=min(1.,fraction*(1.3 if ls==0 else .8));break
    AA,bb=mod.rows(sn,floors*1.03);ee=sn['dc']@sn['W'];rr=target-sn['c'];cc,why=solve(AA,bb,ee,rr,bound=.04,seconds=.8,maxsteps=1300,tol=3e-11)
    if cc is None:break
    un+=sn['W']@cc
   if acc:break
   if time.time()-start>seconds:break
  if not acc:fraction*=.3
  if fraction<1e-8:break
 s=mod.state(u,False);m.save(u,out/'END.json');np.savez(out/'END.npz',u=u,q=s['q'],P=s['P'],c=s['c'],reference=ref);(out/'faces.json').write_text(json.dumps(fs,separators=(',',':')));(out/'history.json').write_text(json.dumps(history,indent=2));print('END',mod.valid(s,floors),census(s['q'],s['P'],fs,ref)['counts'],mechanics(s['q'],fs,P=s['P'],tol=1e-12),flush=True)
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--out',required=True);p.add_argument('--initial');p.add_argument('--seconds',type=float,default=24);p.add_argument('--fraction',type=float,default=1);p.add_argument('--reserve',type=float,default=.2);a=p.parse_args();run(a.out,a.initial,a.seconds,a.fraction,a.reserve)
