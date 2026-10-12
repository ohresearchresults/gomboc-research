# material-88858a7bbf6e

AI research material · [Export notes](../catalog/coverage.md#text-records)

---

# New finite D2 H methods: complete source and deterministic numerical replay

These are NEW methods, not reconstruction of the missing historical quotient part2. No110 found; no family exclusion. Exact endpoints and literal frozen checkpoints are independently preserved in [internal-source-reference] with its full-auditor dependency. This material preserves how those endpoints were obtained and the complete finite numerical experiments, not just fragments. No external input files are required: exact D2_AXIS_S0_T10_G4 seed is literal in the source. Its canonical input1033B SHA368e8294eb64507b6ade790b64f973b03f0a007b300d6338d1840731a36b4d80; independently exact-audited elsewhere.

Environment: CPython3.13.5,NumPy2.3.5,SciPy1.17.0,Torch2.10.0+cpu,one thread. Save each complete unit below UTF8/LF with one terminal newline. d2_section_search.py8880B SHAf871a631ea318b147557f1ba31aa795629a4d09ceaea7dabee796af0e0eb73c9; d2_chord_lbfgs.py3716B SHAe74fae1d7137e2d60c2a907b32deea4f7ec8c60953f36309db5a91ab02cb7934; d2_metric_scout.py1420B SHAf7b4c1c9e00eb829a536f3bb2e9a72689be4bf2e1afee0f85d8a7c000da0f1f3; replay_d2_h.py1062B SHAc850fb8bb888dd7d13aab00cf11dcf6bdc99189f31005f8d553a8166880d59a0.

Run `python replay_d2_h.py`. Actual cold replay completed all three experiments. The wrapper drops ONLY elapsed wall-clock seconds; full numerical checkpoints, parameters, complex counts, objective values and complete call ledgers remain. Expected canonical outputs: d2_run_0_adaptive_canonical.json207066B SHAf1e0b9670d43d9ced48359858d21e0e46cbcd7777901d011d34f7a9f1059e308; d2_chord_1_canonical.json139623B SHA3ce621ceaac16b2bcc0b5068060702c2f74adbfd66101a19415883af8a9afe61; d2_metric_160801_canonical.json6647B SHA6aea2589a917105a0113b96a84bbe4996f36b50f9573a48638c64ce917e49756. Terminal D2_NEW_H_METHODS_REPLAY_COMPLETE. Exact endpoint reconstruction does not require numerically identical optimization on other software versions.

Finite scope/results: Adam400 iterations/401 evaluations, lr.015,seed0,noise0, actual-centroid orbit-exterior true-edge angular exits plus root-norm penalties. The score-best is iteration0 (initial z-affine chart of the old seed), V79/E130/F53, numericalS3U3, not a new equilibrium improvement. Final changed body rounds atG3/G4/G6 to exact V57/E88/F33,7/7/12weak000. Do not repeat the withdrawn unsupported V55/E94 progress claim. The actual initial chart centroid is approximately-.1622725933, loss1.0403000307; temporary notes claiming-.00438 or other traces were not the saved object.

L-BFGS-B all-chord relative support loss: maxiter250 but ACTUAL34 iterations/235 calls; normal relative-reduction convergence, not abnormal termination. Best call235 objective.003452430285749414, V87/E142/F57, numericalS3U3, true-edge angular deficit.7006936163 and centroid≈-.1447809057. G3/G6 round to334weak000, butG4 to7/3/8weak000. Positive chords can eliminate an equilibrium but need not remain true edges; a tiny relative-chord loss is not weak-free feasibility and can coexist with large angular deficits. Neither this finite pass nor failure to improve proves a family exclusion.

Diagonal metric grid on ORIGINAL seed only:401x401=160801 samples, G=diag(a,b,1), a∈geomspace(.03,100,401),b∈geomspace(.003,10,401). Same-centre physical/polar inverse metrics, true edges, tolerance1e-10 numerical strict classification. MinimumS+U6; noS1/U1 in this finite grid. This is not a certificate excluding all diagonal metrics.

## d2_section_search.py
```python
"""New D2 true-edge orbit-exterior search, 2026-09-23.
Independent finite H chart; NOT a replay of missing historical quotient code.
Exact seed: D2_AXIS_S0_T10_G4 from material [internal-source-reference].
Python 3.13.5 / numpy 2.3.5 / scipy 1.17.0 / torch 2.10.0+cpu.
"""
import os
for key in ['OMP_NUM_THREADS','MKL_NUM_THREADS','OPENBLAS_NUM_THREADS']:os.environ[key]='1'
import json,sys,hashlib,itertools,time
from pathlib import Path
import numpy as np
from scipy.spatial import HalfspaceIntersection,ConvexHull
from scipy.optimize import minimize
import torch
torch.set_num_threads(1)
torch.set_default_dtype(torch.float64)
SEED=dict(name='D2_AXIS_S0_T10_G4',denominator=10000,bottom=17570,representatives=[[6587,-411,-16958],[1376,0,-17547],[15671,-1387,-14233],[4230,1462,-15223],[21734,-952,-9489],[7248,3181,-10081],[22968,0,-5668],[9140,3908,-5060],[21786,955,-3414],[10059,3902,-1223],[19911,1552,-1211],[9934,3600,1329],[16972,1637,1494],[8584,3228,3137],[12519,1313,4191],[6112,2618,4848],[6055,659,6347],[2663,1426,6453],[8467,2438,6989]])
def raw(x):return (json.dumps(x,sort_keys=True,indent=2)+'\n').encode()
def seednormals():
 r=np.asarray(SEED['representatives'],float)/SEED['denominator'];r[:,:2]=abs(r[:,:2]);return r,SEED['bottom']/SEED['denominator']
def expand(r,b):
 ns=[];owners=[]
 for i,row in enumerate(r):
  for sx,sy in [(1,1),(-1,1),(-1,-1),(1,-1)]:
   q=row*np.array([sx,sy,1.])
   if not any(np.array_equal(q,old) for old in ns):ns.append(q);owners.append((i,sx,sy))
 ns.append([0.,0.,-b]);owners.append((-1,0,0))
 return np.asarray(ns),owners

def geometry(r,b,need_arrays=False):
 q,own=expand(r,b); hs=HalfspaceIntersection(np.column_stack((q,-np.ones(len(q)))),np.zeros(3))
 p=hs.intersections
 # Use maximal supporting H faces; all incidences refer to actual intersection coordinates.
 inc=abs(q@p.T-1)<1e-8
 fs=[];active=[];tris=[];edge={}
 for i,n in enumerate(q):
  ids=np.flatnonzero(inc[i])
  if len(ids)<3:continue
  centre=p[ids].mean(0);unit=n/np.linalg.norm(n);u=p[ids[0]]-centre;u/=np.linalg.norm(u);v=np.cross(unit,u)
  angle=np.arctan2((p[ids]-centre)@v,(p[ids]-centre)@u);f=ids[np.argsort(angle)].tolist()
  if np.dot(n,np.cross(p[f[1]]-p[f[0]],p[f[2]]-p[f[0]]))<0:f.reverse()
  fi=len(fs);fs.append(f);active.append(i)
  for a,bb in zip(f,f[1:]+f[:1]):edge.setdefault(tuple(sorted((a,bb))),[]).append(fi)
  for j in range(1,len(f)-1):tris.append([f[0],f[j],f[j+1]])
 if any(len(x)!=2 for x in edge.values()) or len(p)-len(edge)+len(fs)!=2:raise ValueError('nonmanifold tolerance complex')
 tris=np.asarray(tris,int);vols=np.einsum('ij,ij->i',p[tris[:,0]],np.cross(p[tris[:,1]],p[tris[:,2]]));vol=vols.sum()/6
 c=(vols[:,None]*p[tris].sum(1)).sum(0)/(4*vols.sum())
 x=p-c;n=q[active];h=1-n@c;z=n/h[:,None]
 eu=np.asarray(sorted(edge),int);eq=np.asarray([edge[tuple(e)] for e in eu],int)
 def escape(v,e,quotient=True):
  scor=np.full(len(v),-np.inf);arg=np.full(len(v),-1,int)
  for a,bb in e:
   if quotient and np.linalg.norm(np.r_[abs(v[a,:2])-abs(v[bb,:2]),v[a,2]-v[bb,2]])<1e-7:continue
   d=v[bb]-v[a];dn=np.linalg.norm(d)
   for i,j,sign in [(a,bb,1),(bb,a,-1)]:
    s=sign*np.dot(v[i],d)/(np.linalg.norm(v[i])*dn)
    if s>scor[i]:scor[i]=s;arg[i]=j
  return scor,arg
 us,ua=escape(x,eu);ss,sa=escape(z,eq)
 strict=[int((ss<-1e-9).sum()),int((us<-1e-9).sum())]
 def root(v,kind):
  axis=np.linalg.norm(v[:,:2],axis=1)<1e-7
  ids=np.flatnonzero(axis)
  if not len(ids):return -1
  return int(ids[np.argmax(v[ids,2]) if kind=='top' else np.argmin(v[ids,2])])
 ur=root(x,'top');sr=root(z,'bottom')
 def deficits(scores,root):
  ids=np.arange(len(scores))!=root;return float(np.maximum(0,.0001-scores[ids]).sum())
 stat=dict(V=len(p),E=len(eu),F=len(fs),strict_SU=strict,centroid=c.tolist(),volume=float(vol),root_U=ur,root_S=sr,minimum_exit_U=float(np.min(np.delete(us,ur))) if ur>=0 else None,minimum_exit_S=float(np.min(np.delete(ss,sr))) if sr>=0 else None,loss=deficits(us,ur)+deficits(ss,sr),r_over_R=float(np.min(1/np.linalg.norm(z,axis=1))/np.max(np.linalg.norm(x,axis=1))))
 if need_arrays:
  triples=[]
  for j in range(len(p)):
   inds=np.flatnonzero(inc[:,j]);choices=list(itertools.combinations(inds,3));tr=max(choices,key=lambda ijk:abs(np.linalg.det(q[list(ijk)])))
   triples.append(tr)
  return stat,dict(p=p,q=q,n=n,x=x,z=z,c=c,fs=fs,active=active,own=own,tris=tris,eu=eu,eq=eq,us=us,ss=ss,ua=ua,sa=sa,triples=np.array(triples))
 return stat

def chart(r,b):
 # Affine z normalization moves bottom=-1/b,top=1/max(rz) to -1,+1.
 lo=-1/b;hi=1/max(r[:,2]);mid=(lo+hi)/2;scale=(hi-lo)/2
 nr=r.copy();nr[:,:2]/=(1-r[:,2]*mid)[:,None];nr[:,2]=r[:,2]*scale/(1-r[:,2]*mid)
 assert abs(nr[-1,2]-1)<1e-12
 return nr,1.

def optimize(r,b,steps=250,lr=.01,seed=0,mode='adaptive',weightS=1.,noise=0.):
 rng=np.random.default_rng(seed);r,b=chart(r,b);mask=r[:,:2]>0
 param=np.r_[np.log(r[:,:2][mask]),np.arctanh(np.clip(r[:-1,2],-.999999,.999999))]
 if noise:param+=rng.normal(0,noise,len(param))
 param=torch.tensor(param,requires_grad=True);opt=torch.optim.Adam([param],lr=lr)
 init=param.detach().numpy().copy();ledger=[];best=None;bestscore=np.inf;failed=0;start=time.time()
 def decode(pt):
  nr=torch.zeros((len(r),3));nr[:,:2][torch.tensor(mask)]=torch.exp(pt[:mask.sum()]);nr[:-1,2]=torch.tanh(pt[mask.sum():]);nr[-1,2]=1.;return nr
 for it in range(steps+1):
  nr=decode(param);nrnp=nr.detach().numpy()
  try:stat,g=geometry(nrnp,b,True)
  except Exception as exc:
   failed+=1
   if best is None:raise
   with torch.no_grad():param.copy_(torch.tensor(best['parameters'])+torch.tensor(rng.normal(0,.002,len(param))))
   opt=torch.optim.Adam([param],lr=lr/2);continue
  score=sum(stat['strict_SU'])*10+stat['loss']
  if score<bestscore:
   bestscore=score;best=dict(iteration=it,parameters=param.detach().numpy().tolist(),representatives=nrnp.tolist(),bottom=b,stat=stat)
  ledger.append(dict(iteration=it,**stat))
  if it%50==0:print('ITER',seed,mode,it,stat['strict_SU'],stat['loss'],stat['E'],flush=True)
  if it==steps:break
  own=g['own'];ql=[]
  for row,sx,sy in own:
   if row<0:ql.append(torch.tensor([0.,0.,-b]))
   else:ql.append(nr[row]*torch.tensor([sx,sy,1.]))
  q=torch.stack(ql);p=torch.linalg.solve(q[torch.tensor(g['triples'])],torch.ones((len(g['p']),3)))
  tris=torch.tensor(g['tris']);a,bb,cc=p[tris[:,0]],p[tris[:,1]],p[tris[:,2]];vols=(a*torch.linalg.cross(bb,cc)).sum(1)
  c=(vols[:,None]*(a+bb+cc)).sum(0)/(4*vols.sum());x=p-c;n=q[g['active']];z=n/(1-n@c)[:,None]
  terms=[]
  for vv,ee,old,root,weight in [(x,g['eu'],g['x'],stat['root_U'],1.),(z,g['eq'],g['z'],stat['root_S'],weightS)]:
   adj=[[] for _ in old]
   for a,bb in ee:
    if np.linalg.norm(np.r_[abs(old[a,:2])-abs(old[bb,:2]),old[a,2]-old[bb,2]])<1e-7:continue
    adj[a].append(bb);adj[bb].append(a)
   for a,nei in enumerate(adj):
    if a==root:continue
    if not nei:terms.append(weight*torch.tensor(10.)+0*vv.sum());continue
    ds=vv[nei]-vv[a];scores=(ds*vv[a]).sum(1)/(torch.linalg.norm(vv[a])*torch.linalg.norm(ds,dim=1))
    if mode=='norm_ascent':
     norms=(old[nei]**2).sum(1);j=int(np.argmax(norms));score=scores[j]
    else:score=torch.max(scores)
    terms.append(weight*torch.relu(.0001-score))
   if root<0:terms.append(100.+0*vv.sum())
   else:
    # Both root norms dominate; eliminates spurious local improvement toward wrong elder.
    rad=(vv*vv).sum(1);rootrad=rad[root];gap=(rad-rootrad)/rootrad
    terms.append(.3*weight*torch.relu(gap+.0001).sum())
  # Keep modest parameter movements rather than singular collapsing charts.
  loss=sum(terms)+1e-6*((param-torch.tensor(init))**2).sum()
  opt.zero_grad();loss.backward();torch.nn.utils.clip_grad_norm_([param],10.);opt.step()
 return dict(seed=seed,mode=mode,steps=steps,lr=lr,weightS=weightS,noise=noise,failed=failed,seconds=time.time()-start,initial=init.tolist(),mask=mask.tolist(),best=best,final=dict(parameters=param.detach().numpy().tolist(),representatives=decode(param).detach().numpy().tolist(),bottom=b),ledger=ledger)

if __name__=='__main__':
 out=Path(sys.argv[1] if len(sys.argv)>1 else '.');out.mkdir(parents=True,exist_ok=True)
 r,b=seednormals();bs=raw(SEED);assert len(bs)==1033 and hashlib.sha256(bs).hexdigest()=='368e8294eb64507b6ade790b64f973b03f0a007b300d6338d1840731a36b4d80'
 (out/(SEED['name']+'.json')).write_bytes(bs)
 s,g=geometry(r,b,True);print(json.dumps(s,indent=2));
 print('S indices',np.flatnonzero(g['ss']<0),'U indices',np.flatnonzero(g['us']<0));
 print('S active H',[(i,g['active'][i],g['own'][g['active'][i]],g['ss'][i],g['z'][i].tolist()) for i in np.flatnonzero(g['ss']<0)])
 print('U positions',[(int(i),g['x'][i].tolist(),float(g['us'][i])) for i in np.flatnonzero(g['us']<0)])
 if len(sys.argv)>2:
  cfg=json.loads(sys.argv[2]);res=optimize(r,b,**cfg);name=f"d2_run_{cfg.get('seed',0)}_{cfg.get('mode','adaptive')}.json";(out/name).write_bytes(raw(res));print('SAVED',name,res['best']['stat'])
```

## d2_chord_lbfgs.py
```python
"""New orbit-exterior all-chord D2 H continuation with L-BFGS-B.
Continuous unnormalised support residuals, at the actual mass centre. A positive
chord eliminates a critical carrier but is NOT claimed to be a true edge.
Needs d2_section_search.py. Outputs exact binary64 checkpoints and complete call ledger.
"""
from pathlib import Path
import json,sys,itertools,time
import numpy as np,torch
from scipy.optimize import minimize
from d2_section_search import seednormals,geometry,chart,raw

def run(steps=400,seed=0,noise=0.,weightS=1.,squared=False,initfile=None):
 r,b=seednormals();r,b=chart(r,b)
 if initfile:
  old=json.load(open(initfile));r=np.array(old['final']['representatives']);b=old['final']['bottom']
 mask=r[:,:2]>0;nm=mask.sum();p0=np.r_[np.log(r[:,:2][mask]),np.arctanh(np.clip(r[:-1,2],-.999999,.999999))]
 p0+=np.random.default_rng(seed).normal(0,noise,len(p0));ledger=[];best=None;bestloss=None;calls=0;t0=time.time()
 def decode(par):
  nr=torch.zeros((len(r),3));nr[:,:2][torch.tensor(mask)]=torch.exp(par[:nm]);nr[:-1,2]=torch.tanh(par[nm:]);nr[-1,2]=1.;return nr
 def fun(par):
  nonlocal calls,best,bestloss
  calls+=1;pt=torch.tensor(par,requires_grad=True);nr=decode(pt)
  try:stat,g=geometry(nr.detach().numpy(),b,True)
  except Exception as ex:
   ledger.append(dict(call=calls,error=str(ex)));return 1e3,np.zeros(len(par))
  q=torch.stack([torch.tensor([0.,0.,-b]) if row<0 else nr[row]*torch.tensor([sx,sy,1.]) for row,sx,sy in g['own']])
  p=torch.linalg.solve(q[torch.tensor(g['triples'])],torch.ones((len(g['p']),3)))
  ti=torch.tensor(g['tris']);a,bb,c=p[ti[:,0]],p[ti[:,1]],p[ti[:,2]];vols=(a*torch.linalg.cross(bb,c)).sum(1);cent=(vols[:,None]*(a+bb+c)).sum(0)/(4*vols.sum());x=p-cent;n=q[g['active']];z=n/(1-n@cent)[:,None]
  terms=[]
  for vv,old,root,wt in [(x,g['x'],stat['root_U'],1.),(z,g['z'],stat['root_S'],weightS)]:
   rad=(vv*vv).sum(1);scores=(vv@vv.T)/rad[:,None]-1.
   orb=np.column_stack((abs(old[:,:2]),old[:,2]));same=(abs(orb[:,None,:]-orb[None,:,:]).max(2)<1e-7)
   scores=scores.masked_fill(torch.tensor(same),-1e6);ex=torch.max(scores,dim=1).values
   ex=ex[torch.arange(len(old))!=root];pen=torch.relu(1e-5-ex)
   terms.append(wt*((pen*pen).sum() if squared else pen.sum()))
  loss=sum(terms)+1e-7*((pt-torch.tensor(p0))**2).sum();val=float(loss.detach());loss.backward();grad=pt.grad.numpy()
  ledger.append(dict(call=calls,objective=val,**stat));score=(sum(stat['strict_SU']),val)
  cp=dict(call=calls,parameters=par.tolist(),representatives=nr.detach().numpy().tolist(),bottom=b,objective=val,stat=stat)
  if best is None or score<(sum(best['stat']['strict_SU']),best['objective']):best=cp
  if bestloss is None or val<bestloss['objective']:bestloss=cp
  if calls%100==1:print('CALL',seed,calls,stat['strict_SU'],val,stat['E'],flush=True)
  return val,grad
 bounds=[(-3.5,3.5)]*nm+[(-5.,5.)]*(len(r)-1)
 opt=minimize(fun,p0,jac=True,method='L-BFGS-B',bounds=bounds,options=dict(maxiter=steps,maxfun=steps*4,ftol=1e-13,gtol=1e-8,maxls=25,maxcor=20))
 return dict(method='D2_CHORD_LBFGS_NEW',seed=seed,noise=noise,weightS=weightS,squared=squared,steps=steps,initfile=initfile,initial=p0.tolist(),bounds=bounds,mask=mask.tolist(),status=int(opt.status),message=str(opt.message),nit=int(opt.nit),nfev=int(opt.nfev),seconds=time.time()-t0,best=best,bestloss=bestloss,final=dict(parameters=opt.x.tolist(),representatives=decode(torch.tensor(opt.x)).numpy().tolist(),bottom=b),ledger=ledger)
if __name__=='__main__':
 cfg=json.loads(sys.argv[1]) if len(sys.argv)>1 else {};out=run(**cfg);name=f"d2_chord_{cfg.get('seed',0)}.json";Path(name).write_bytes(raw(out));print('SAVED',name,'BEST',out['best']['stat'],'LOSSBEST',out['bestloss']['stat'],out['message'])
```

## d2_metric_scout.py
```python
"""New finite diagonal-metric scout on exact D2_AXIS_S0_T10_G4.
Uses true edges of the seed, own volume centroid, and inverse diagonal polar metric.
Numerical only: finite scout is not a family exclusion or weak-equilibrium audit.
"""
from pathlib import Path
import numpy as np,json
from d2_section_search import geometry,seednormals,raw

def forms(v,e):
 out=[[] for _ in v]
 for a,b in e:
  d=v[b]-v[a];out[a].append(v[a]*d);out[b].append(-v[b]*d)
 return out

def count(fs,weights):
 return np.asarray([np.max(np.array(row)@weights.T,axis=0)<-1e-10 for row in fs]).sum(0)

def run():
 r,b=seednormals();stat,g=geometry(r,b,True);uf=forms(g['x'],g['eu']);sf=forms(g['z'],g['eq'])
 ax=np.geomspace(.03,100,401);by=np.geomspace(.003,10,401);best=[];minimum=1000;distribution={}
 for a in ax:
  w=np.column_stack((np.full(len(by),a),by,np.ones(len(by))));u=count(uf,w);s=count(sf,1/w)
  for j,(ss,uu) in enumerate(zip(s,u)):
   k=f'{ss},{uu}';distribution[k]=distribution.get(k,0)+1
   if ss+uu<minimum:minimum=int(ss+uu);best=[]
   if ss+uu==minimum and len(best)<30:best.append([float(a),float(by[j]),int(ss),int(uu)])
 result=dict(seed='D2_AXIS_S0_T10_G4',a_geomspace=[.03,100,401],b_geomspace=[.003,10,401],samples=len(ax)*len(by),minimum_SU=minimum,best_first30=best,distribution=distribution)
 Path('d2_metric_160801.json').write_bytes(raw(result));print(json.dumps(result,indent=2))
if __name__=='__main__':run()
```

## replay_d2_h.py
```python
"""Replay three numerical finite experiments and hash all scientifically relevant output.
Elapsed wall-clock seconds alone are omitted from canonical outputs.
"""
from pathlib import Path
import subprocess,sys,json,hashlib,os
FILES=['d2_run_0_adaptive.json','d2_chord_1.json','d2_metric_160801.json']
def main():
 cmds=[[sys.executable,'d2_section_search.py','.','{"steps":400,"lr":0.015,"seed":0,"mode":"adaptive","weightS":1.0,"noise":0.0}'],[sys.executable,'d2_chord_lbfgs.py','{"steps":250,"seed":1,"noise":0.0,"weightS":1.0,"squared":false,"initfile":null}'],[sys.executable,'d2_metric_scout.py']]
 for i,cmd in enumerate(cmds):
  with open(f'D2_H_REPLAY_{i}.log','w') as out:subprocess.run(cmd,check=True,stdout=out,stderr=subprocess.STDOUT)
 for name in FILES:
  d=json.load(open(name));d.pop('seconds',None);b=(json.dumps(d,sort_keys=True,indent=2)+'\n').encode();p=Path(name.replace('.json','_canonical.json'));p.write_bytes(b);print(p.name,len(b),hashlib.sha256(b).hexdigest())
 print('D2_NEW_H_METHODS_REPLAY_COMPLETE')
if __name__=='__main__':main()
```
