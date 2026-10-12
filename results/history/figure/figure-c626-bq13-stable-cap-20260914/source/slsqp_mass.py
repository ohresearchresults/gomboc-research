"""Finite constrained SQP mass closure, fixed reference and positive identity floors.
A numerical proposal, never an exact acceptance gate.
"""
import sys,json,time,argparse
from pathlib import Path
import numpy as np
from scipy.linalg import svd
from scipy.optimize import minimize
R=Path(__file__).resolve().parent
sys.path[:0]=[str(R/'parent/mechanism'),str(R/'parent/mechanism/parent_sources')]
from reference_atlas import ReferenceAtlas
from atlas_opt import Atlas
from numeric import mechanics
from repair626 import refs,rooted

def run(a):
 d=json.loads((a.source/'GENERATOR.json').read_text());fs=json.loads((a.source/'faces.json').read_text());m=ReferenceAtlas(d,fs)
 b=Atlas(json.loads((R/'BASIN/GENERATOR.json').read_text()),fs);m.reference=b.state(b.u0,False)['c'];m.uparent,m.sparent=refs();u=m.u0.copy()
 s=m.state(u);floor=np.maximum(5e-8,np.minimum(1e-5,s['vals']*.4));assert (s['vals']>floor).all();gf=np.maximum(1e-9,np.minimum(1e-6,s['gaps']*.01))
 out=a.out;out.mkdir(parents=True,exist_ok=False);t0=time.monotonic();hist=[];trust=a.trust
 for outer in range(a.outer):
  s=m.state(u);m.uparent=s['cu'].argmax(1);m.sparent=s['cs'].argmax(1);rooted(m.uparent,m.Uroot);rooted(m.sparent,3);s=m.state(u)
  err=np.linalg.norm(s['M']/s['V']-m.reference);hist.append(dict(outer=outer,error=float(err),minref=float(s['vals'].min()),seconds=time.monotonic()-t0));print(hist[-1],flush=True)
  m.save(u,out/'GENERATOR.json');(out/'faces.json').write_text(json.dumps(fs,separators=(',',':')));(out/'history.json').write_text(json.dumps(hist,indent=2))
  if err<1e-13:print('SQP_MASS_CLOSURE_NUMERICAL',flush=True);break
  mat=np.r_[s['dq'].reshape(-1,m.np)/2,s['dP'].reshape(-1,m.np)];_,dd,Vt=svd(mat,full_matrices=False,check_finite=False);W=Vt.T/np.maximum(dd,1e-7)
  vi,qi=np.where((~m.inc)&(s['gaps']<.1));J=np.r_[s['J'],m.gap_jac(s,vi,qi),s['ddet']]@W
  scale=np.maximum(np.linalg.norm(J,axis=1),1e-5);zlast=None;last=None
  def evaluate(z):
   nonlocal zlast,last
   if zlast is None or not np.array_equal(z,zlast):
    st=m.state(u+W@z);ac=st['M']/st['V'];dc=(st['dM']-ac[:,None]*st['dV'][None,:])/st['V'];r=ac-m.reference
    vals=np.r_[st['vals']-floor,st['gaps'][vi,qi]-gf[vi,qi],st['det']-1e-10]/scale
    jac=np.r_[st['J'],m.gap_jac(st,vi,qi),st['ddet']]@W/scale[:,None]
    last=(float(r@r/err**2),2*r@dc@W/err**2,vals,jac,st);zlast=z.copy()
   return last
  result=minimize(lambda z:evaluate(z)[0],np.zeros(m.np),jac=lambda z:evaluate(z)[1],method='SLSQP',constraints=[{'type':'ineq','fun':lambda z:evaluate(z)[2],'jac':lambda z:evaluate(z)[3]}],bounds=[(-trust,trust)]*m.np,options=dict(ftol=1e-12,maxiter=a.inner,disp=False))
  print('SQP',result.message,'nit',result.nit,'fun',result.fun,flush=True)
  good=False
  for ls in range(16):
   un=u+W@(result.x*2.**-ls)
   try:sn=m.state(un,False)
   except Exception:continue
   er=np.linalg.norm(sn['M']/sn['V']-m.reference)
   if (sn['vals']-floor).min()>-1e-10 and sn['gaps'][~m.inc].min()>1e-10 and sn['det'].min()>0 and sn['h'].min()>0 and er<err:
    u=un;good=True;print('ACCEPT',ls,float(er),flush=True);break
  if not good:trust*=.4
  else:trust=min(a.trust,trust*1.3)
  if time.monotonic()-t0>a.seconds or trust<1e-7:break
 s=m.state(u,False);m.save(u,out/'GENERATOR.json');rep=mechanics(s['q'],fs,P=s['P'],tol=1e-13);(out/'NUMERICAL.json').write_text(json.dumps(rep,indent=2));print('FINAL',rep,flush=True)
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--source',type=Path,required=True);p.add_argument('--out',type=Path,required=True);p.add_argument('--trust',type=float,default=.01);p.add_argument('--outer',type=int,default=20);p.add_argument('--inner',type=int,default=80);p.add_argument('--seconds',type=float,default=600);run(p.parse_args())
