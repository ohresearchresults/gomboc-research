"""Finite predictor/corrector in the actual filled-centroid contact chart.
The corrector solves the nonlinear healthy guards at an intermediate defect target.
It is not a certified continuous trajectory.
"""
from pathlib import Path
import argparse,json,time
import numpy as np
from scipy.linalg import svd
from scipy.optimize import linprog
from minnorm_qp import solve
from model57 import model,enc,freeze
from numeric import mechanics

def run(src,out,steps=40,trust=.003,guard=None,halvings=5,correctors=8,qp_seconds=.5,qp_steps=1500):
 out.mkdir(exist_ok=False);d=json.loads((src/'GENERATOR.json').read_bytes());fs=json.loads((src/'faces.json').read_bytes());meta=json.loads((src/'META.json').read_bytes());m=model(d,fs);m.uparent=np.array(meta['uparent']);m.sparent=np.array(meta['sparent']);u=m.u0.copy();s=m.state(u,False);bad=np.flatnonzero(s['vals']<0);assert len(bad)==1;bad=int(bad[0]);good=np.array([i for i in range(len(s['vals'])) if i!=bad]);ref=s
 if guard is not None:
  gd=json.loads((guard/'GENERATOR.json').read_bytes());gm=model(gd,fs);gm.uparent=m.uparent;gm.sparent=m.sparent;ref=gm.state(gm.u0,False)
 floors=np.minimum(ref['vals']*.1,2e-7);floors[bad]=2e-7;geo=np.minimum(.1*ref['gaps'],1e-6);df=.1*ref['det'];hist=[];start=time.monotonic()
 for name,v in [('faces.json',fs),('META.json',meta),('FLOORS.json',dict(values=floors.tolist(),bad=bad,trust=trust))]: (out/name).write_bytes(enc(v))
 def state(u):
  s=m.state(u);mat=np.r_[s['dq'].reshape(-1,m.np)/2,s['dP'].reshape(-1,m.np)];_,ds,vt=svd(mat,full_matrices=False,check_finite=False);W=vt.T/np.maximum(ds,1e-8);return s,W
 def constraints(s,W,target):
  vi,qi=np.where((~m.inc)&(s['gaps']<.04));A=np.r_[s['J'],m.gap_jac(s,vi,qi),s['ddet']]@W;b=np.r_[target-s['vals'],geo[vi,qi]-s['gaps'][vi,qi],df-s['det']];return A,b
 def error(s,target):return np.linalg.norm(np.r_[np.minimum(s['vals']-target,0),10*np.minimum((s['gaps']-geo)[~m.inc],0),10*np.minimum(s['det']-df,0)])
 for it in range(steps):
  s,W=state(u);oldbad=s['vals'][bad];hist.append(dict(it=it,bad=float(oldbad),minhealthy=float(s['vals'][good].min()),trust=trust,sec=time.monotonic()-start));print(hist[-1],flush=True)
  if oldbad>=floors[bad]:break
  A,b=constraints(s,W,floors);A=np.delete(A,bad,axis=0);b=np.delete(b,bad);sc=np.maximum(np.linalg.norm(A,axis=1),1e-10);A/=sc[:,None];b/=sc;row=s['J'][bad]@W;rn=np.linalg.norm(row)
  lp=linprog(-row/rn,A_ub=-A,b_ub=-b,bounds=[(-trust,trust)]*m.np,method='highs',options={'primal_feasibility_tolerance':1e-9,'dual_feasibility_tolerance':1e-9})
  if not lp.success:print('LPFAIL',lp.message,flush=True);break
  pred=min(row@lp.x,(floors[bad]-oldbad)*1.05)
  if pred<1e-12:print('NO_PROGRESS',pred,flush=True);break
  ok=False
  for halving in range(halvings):
   target=floors.copy();target[bad]=oldbad+.5*pred*2.**-halving;un=u.copy();correction_ok=False
   for jt in range(correctors):
    ss,WW=state(un);er=error(ss,target)
    if er<1e-12 and ss['h'].min()>.2:correction_ok=True;break
    AA,bb=constraints(ss,WW,target);x,why=solve(AA,bb,bound=trust*2,tol=1e-13,seconds=qp_seconds,maxsteps=qp_steps)
    if x is None:break
    for ls in range(12):
     utry=un+2.**-ls*(WW@x)
     try:st=m.state(utry,False)
     except (ValueError,np.linalg.LinAlgError):continue
     if st['h'].min()>.2 and error(st,target)<er*(1-1e-4*2.**-ls):un=utry;break
    else:break
   sn=m.state(un,False)
   if correction_ok and sn['vals'][bad]>oldbad and min(sn['vals'][good]-floors[good])>=-1e-12 and min((sn['gaps']-geo)[~m.inc])>0 and min(sn['det']-df)>0:
    u=un;ok=True;print('ACCEPT',halving,jt,float(sn['vals'][bad]),flush=True);trust=min(.03,trust*(1.3 if halving<2 else .8));break
  if not ok:trust*=.3;print('REDUCE',trust,flush=True)
  (out/'GENERATOR.json').write_bytes(enc(freeze(m,u)));(out/'HISTORY.json').write_bytes(enc(hist))
  if trust<1e-10:break
 s=m.state(u,False);r=mechanics(s['q'],fs,s['P'],tol=1e-13);(out/'GENERATOR.json').write_bytes(enc(freeze(m,u)));(out/'NUMERICAL.json').write_bytes(enc(r));print('FINAL',r['counts'],r['min_gap'],float(s['vals'][bad]),flush=True)
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--src',type=Path,required=True);p.add_argument('--out',type=Path,required=True);p.add_argument('--steps',type=int,required=True);p.add_argument('--trust',type=float,required=True);p.add_argument('--guard',type=Path);p.add_argument('--halvings',type=int,default=5);p.add_argument('--correctors',type=int,default=8);p.add_argument('--qp-seconds',type=float,default=.5);p.add_argument('--qp-steps',type=int,default=1500);a=p.parse_args();run(a.src,a.out,a.steps,a.trust,a.guard,a.halvings,a.correctors,a.qp_seconds,a.qp_steps)
