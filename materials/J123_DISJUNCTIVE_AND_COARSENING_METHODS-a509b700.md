# material-a509b700b201

AI research material · [Export notes](../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

# J123 — finite disjunctive fan choice and stable-patch coarsening

This is a complete follow-up method unit, not a fourth required part of the already complete J123 numerical capsule. Its dependencies are the literal geometry/bar methods in [internal-source-reference] and [internal-source-reference], plus the complete raw floating FULLF/STARH points in [internal-source-reference]. Exact related rational bodies are independently reconstructible from [internal-source-reference]. No new own110 or exact class for the new floating checkpoint is claimed.

## Scientific change and finite evidence
Requiring physical and polar derivative guards from every neighboring boundary triangulation simultaneously can overrestrict the local model. fanchoice123.py instead solves each sampled chart separately, including THAT chart's own mass/guard constants at the CURRENT coordinates. It chooses a finite candidate only after rebuilding its ACTUAL convex hull, integrating its own homogeneous mass, finding a complete positive physical tree and computing all polar merge events. This is a disjunctive nomination method, not a proof that a selected local polynomial is the actual chart throughout the step. No finite chart membership theorem is assumed. The exact rank-one mass-jump identity from the separate exact material motivates this change but is not substituted for the finite acceptance test.

On FULLF, ten completed requested steps with trust.01, actual tauP1e-6, model buffer1e-5 and sum weight1 lower Phi=maxQ+sumQ from1.017169007449835 to.9860784330637884. The endpoint is numerical V38/E108/F72, S11/U1, P[], TEN positive Q with max~.43837953254031437 and sum~.547698900523474. Thus this escaped the previous all-fan intersection stop and reduced total depth, but increased the Q count from9 to10; it is not a basin cancellation, exact own211 or own110. An earlier25-step call was externally interrupted after its iteration20 print and did not save a terminal body. It is not counted as25 completed steps or used as the exact input; the saved ten-step run was then executed completely. The source now saves every accepted intermediate prefix to avoid that specific loss.

coarsen123.py tests orthogonal projections of adjacent or connected stable-patch vertices onto an existing supporting plane. Every candidate recomputes actual mass and physical positive-tree feasibility. It examines patch angles2,5,10,20,35,60 degrees, deduplicates face/vertex sets and admits only minP>=1e-8, maxQ<=parent+.025 and sumQ<=parent+.02. Exactly73 proposals from FULLF and110 from STARH were executed, zero admitted in either finite family. This is NOT a theorem that coplanar coarsening is impossible. Many small parent physical guards are consumed by actual-centroid movement. The next meaningful variant is coupled shape/mass repair while preserving the new flat facet, not accepting a reference-centre projection or treating this finite failure as global infeasibility.

## Reproduction
Python3.13.5, NumPy2.3.5,SciPy1.17.0,PyTorch2.10.0+cpu,float64,single torch thread. Set OMP_NUM_THREADS=OPENBLAS_NUM_THREADS=MKL_NUM_THREADS=1. Save the complete sources and literal checkpoint below with their terminal newline, restore the earlier capsule, and run:
```sh
python restore123.py
python fanchoice123.py fullF_points.json choiceI10 10 .01 1e-6 1e-5 1
python coarsen123.py fullF_points.json coarseJ
python coarsen123.py starH_points.json coarseK
```
The producing run originally used identical point arrays in fullF.json/starH.json; the suffixed files are exact complete restored equivalents. Full output JSON contains elapsed seconds and input filename, so it is not a deterministic byte-hash target. The literal selected output coordinates below provide a complete direct continuation input without rerunning an optimizer. Source and literal input byte identities are exact; floating classifications remain nominations subject to rational audit.

Source/checkpoint identities:
fanchoice123.py4699 SHA22e74b7246767ebc37fa07ff3cb9ab9206800b47389d1f867abce403a0875c08
coarsen123.py3003 SHA277ee0407d349947a814cf5fc6c5620717b29ed8a078b9d84e50ac5f43b0f316
choiceI10_points.json2314 SHAdf7f8c225edcce551f52a5a8a2998ec277ea07337e7744a48bae33c237eb9644

## fanchoice123.py
```python
"""Disjunctive neighboring-fan continuation, not intersection of all fan guards.
Each chart uses its own mass, P guards and polar bar constants at the current
coordinates. It is only a local polynomial nomination. Every finite candidate
is admitted by a rebuilt actual hull/mass, a complete positive P tree and the
whole Q objective. No optimizer status certifies a shape or global exclusion.
"""
from __future__ import annotations
import json,sys,time
from pathlib import Path
import numpy as np,torch
from scipy.optimize import minimize
from geometry123 import load_points,triangulate,live_values,reference_tree_guards,stats
from barflow123 import values,bar_structure,dual_edges,depths

def chart(x,current,sample):
 tr,fa,_,hull=triangulate(sample)
 _,_,_,qs=live_values(torch.tensor(sample),tr,fa)
 st=bar_structure(qs.detach().numpy(),dual_edges(hull))
 base=torch.tensor(x);ids=current['ids'];z=base[ids].reshape(-1).detach().requires_grad_()
 def f(t):
  xx=base.index_copy(0,torch.tensor(ids),t.reshape(-1,3));v,g,p,q=live_values(xx,tr,fa)
  return torch.cat((reference_tree_guards(p,current['rootP'],current['parentsP']),depths(q,st),v.reshape(1)))
 val=f(z).detach().numpy();jac=torch.autograd.functional.jacobian(f,z,vectorize=True).detach().numpy()
 return val,jac,tuple(sorted(tuple(sorted(map(int,t))) for t in tr))

def run(inp,prefix,steps,trust,taup,buffer,weight):
 x=load_points(inp);v0=values(x)['volume'];frames=[];trace=[];start=time.monotonic()
 for it in range(steps):
  a=values(x);m=len(a['p']);phi=float(max(a['bars'])+weight*sum(a['bars']))
  samples=[x.copy()];seen=set();choices=[];best=None;ci=0
  while ci<len(samples) and ci<10:
   sample=samples[ci];ci+=1
   try:val,J,sig=chart(x,a,sample)
   except Exception:continue
   if sig in seen:continue
   seen.add(sig);k=len(val)-m-1;n=J.shape[1]
   for radius in [trust,trust/10]:
    bm=float(max(val[m:-1]));A=np.zeros((m+k+1,n+1));A[:,:n]=J;A[m:m+k,:n]*=-1;A[m:m+k,n]=-1
    b=np.r_[val[:m]-(taup+buffer),bm-val[m:-1],val[-1]-.05*v0];lin=weight*J[m:m+k].sum(0)
    sub=minimize(lambda y:(.5*(y[:-1]@y[:-1])+lin@y[:-1]-y[-1],np.r_[y[:-1]+lin,-1.]),np.zeros(n+1),jac=True,method='SLSQP',constraints=[{'type':'ineq','fun':lambda y:A@y+b,'jac':lambda y:A}],bounds=[(-radius,radius)]*n+[(-.1,.1)],options={'ftol':1e-12,'maxiter':120})
    d=sub.x[:-1].reshape(-1,3);ok=False;evals=[]
    for alpha in [1.,.1,.01,.001]:
     q=x.copy();q[a['ids']]+=alpha*d
     try:qsig=tuple(sorted(tuple(sorted(map(int,t))) for t in triangulate(q)[0]))
     except Exception:continue
     if qsig not in seen and len(samples)<12:samples.append(q)
    for ls in range(20):
     alpha=2.**(-ls);xx=x.copy();xx[a['ids']]+=alpha*d
     try:aa=values(xx)
     except Exception:continue
     newphi=float(max(aa['bars'])+weight*sum(aa['bars']))
     if min(aa['p'])>=taup-1e-11 and aa['volume']>=.05*v0 and newphi<phi-1e-11:
      ok=True
      if best is None or newphi<best[0]:best=(newphi,xx.copy(),aa,ci-1,radius,alpha)
      break
    choices.append({'chart':ci-1,'radius':radius,'status':int(sub.status),'accepted':ok,'gain':float(sub.x[-1]),'qp_min':float(min(A@sub.x+b))})
  row={'iteration':it,'phi':phi,'maxQ':float(max(a['bars'])),'sumQ':float(sum(a['bars'])),'charts':len(seen),'choices':choices,'accepted':best is not None}
  if best is not None:
   newphi,x,aa,chosen,radius,alpha=best;row.update(new_phi=newphi,new_maxQ=float(max(aa['bars'])),new_sumQ=float(sum(aa['bars'])),chosen_chart=chosen,radius=radius,alpha=alpha,minP=float(min(aa['p'])));frames.append(x.tolist())
  trace.append(row)
  Path(prefix+'.partial.json').write_text(json.dumps({'points':x.tolist(),'input':inp,'completed_rows':trace,'frames':frames},indent=2)+'\n')
  if it%10==0 or best is None:print(json.dumps({k:v for k,v in row.items() if k!='choices'}),flush=True)
  if best is None or max(aa['bars'])<1e-14:break
 out={'input':inp,'points':x.tolist(),'parameters':{'steps':steps,'trust':trust,'tauP':taup,'buffer':buffer,'sum_weight':weight,'chart_limit':10,'sample_limit':12,'sample_scales':[1,.1,.01,.001],'radius_factors':[1,.1],'line_search_steps':20,'ridge':1,'qp_maxiter':120,'qp_ftol':1e-12,'minimum_phi_improvement':1e-11},'trace':trace,'frames':frames,'seconds':time.monotonic()-start,'stats':stats(x)}
 Path(prefix+'.json').write_text(json.dumps(out,indent=2)+'\n');s=out['stats'];print(json.dumps({'accepted':len(frames),'SU':[len(s['S']),len(s['U'])],'P':[b['depth'] for b in s['P']],'Q':[b['depth'] for b in s['Q']],'VEF':[s[k] for k in ['V','E','F']],'seconds':out['seconds']}),flush=True)
if __name__=='__main__':run(sys.argv[1],sys.argv[2],int(sys.argv[3]),float(sys.argv[4]),float(sys.argv[5]),float(sys.argv[6]),float(sys.argv[7]))
```

## coarsen123.py
```python
"""Finite support-plane projections for actual-mass stable-facet coarsening.
Nominate by rebuilding the hull/mass and a complete positive physical forest.
Exact geometry/class is certified separately; floating coplanarity is not proof.
"""
from __future__ import annotations
import sys,json
from pathlib import Path
import numpy as np,torch
from geometry123 import load_points,triangulate,live_values,angular,stats
from barflow123 import values,dual_edges

def run(inp,prefix):
 x=load_points(inp);a=values(x);tr,fa,_,hull=triangulate(x);v,g,p,q=live_values(torch.tensor(x),tr,fa)
 normals=q.detach().numpy().copy();normals/=np.linalg.norm(normals,axis=1)[:,None]
 stable=set(map(int,np.flatnonzero(angular(q).max(1).values.detach().numpy()<0)))
 dual=dual_edges(hull);adj=[[] for _ in fa]
 for i,j in dual:adj[i].append(int(j));adj[j].append(int(i))
 proposals=[];accepted=[];seen=set()
 def test(f,vertices,kind):
  vertices=sorted(set(map(int,vertices))-set(map(int,fa[f])))
  if not vertices:return
  key=(f,tuple(vertices))
  if key in seen:return
  seen.add(key);n=normals[f];origin=x[fa[f,0]];xx=x.copy();delta=(xx[vertices]-origin)@n
  xx[vertices]-=delta[:,None]*n
  desc={'face':fa[f].tolist(),'projected':vertices,'kind':kind,'max_move':float(max(abs(delta)))}
  try:
   aa=values(xx);bars=aa['bars'];mp=float(min(aa['p']));count=int(sum(bars>1e-12));bm=float(max(bars));bs=float(sum(bars))
   row={**desc,'minP':mp,'maxQ':bm,'sumQ':bs,'Q_count':count,'numeric_F':len(aa['faces'])}
   if mp>=1e-8 and bm<=max(a['bars'])+.025 and bs<=sum(a['bars'])+.02:accepted.append((count,bm+bs,xx.copy(),row))
  except Exception as e:row={**desc,'failed':type(e).__name__}
  proposals.append(row)
 for f in range(len(fa)):
  for j in adj[f]:
   if f in stable or j in stable:test(f,set(fa[f])|set(fa[j]),'adjacent')
  if f not in stable:continue
  for angle in [2,5,10,20,35,60]:
   patch={f};queue=[f]
   for i in queue:
    for j in adj[i]:
     if j not in patch and normals[f]@normals[j]>np.cos(np.radians(angle)):
      patch.add(j);queue.append(j)
   test(f,set(int(t) for j in patch for t in fa[j]),f'connected-{angle}-degrees')
 accepted.sort(key=lambda z:(z[0],z[1]));summary={'input':inp,'base_maxQ':float(max(a['bars'])),'base_sumQ':float(sum(a['bars'])),'base_Q_count':int(sum(a['bars']>1e-12)),'proposal_count':len(proposals),'admitted':len(accepted),'rules':{'tauP':1e-8,'maxQ_allowance':.025,'sumQ_allowance':.02,'patch_angles_degrees':[2,5,10,20,35,60]},'ranked':[s[-1] for s in accepted],'proposals':proposals}
 Path(prefix+'.search.json').write_text(json.dumps(summary,indent=2)+'\n')
 for k,(_,_,xx,row) in enumerate(accepted[:6]):Path(f'{prefix}.{k}.json').write_text(json.dumps({'points':xx.tolist(),'operation':row,'stats':stats(xx)},indent=2)+'\n')
 print(json.dumps({k:summary[k] for k in ['input','base_Q_count','base_maxQ','base_sumQ','proposal_count','admitted']},indent=2));print(json.dumps(summary['ranked'][:6],indent=2))
if __name__=='__main__':run(sys.argv[1],sys.argv[2])
```

## choiceI10_points.json
```json
{"points":[[-0.8421,-0.4792,0.3346],[-0.46821809316394647,-0.28079866542124005,0.6409626730023936],[-0.7993031710241406,-0.4943188775479331,0.02195612790997186],[-0.24176035153740336,-0.177603298178465,0.7214736192502388],[-0.49184952485213196,0.06228124992579044,-0.2381303435525372],[-0.04047466473645725,0.5014286687952709,-0.3729755194141544],[-0.18565724951656778,0.511912630011182,-0.20359748290631588],[0.4553266346129904,0.16432826158048763,-0.4532018477514801],[0.1057524151673178,-0.0433870517807664,0.7045339456096705],[-0.06887144750419888,-0.10732471677557841,0.7358769461623091],[0.6335027350783599,0.09485166537710252,-0.06314479848695717],[0.2517277168188097,0.0038316613891877477,0.6417875578448684],[-0.15468715004836367,0.22534985591562212,-0.5912178482116407],[-0.018695228550732655,0.03876972364949534,-0.6501852401340935],[0.5532462726724489,0.11236282197996578,-0.3291004855096301],[0.054347487245003975,0.5099840905848955,-0.3512551228478572],[0.3534566533745613,-0.13711273903197496,-0.4866244380963668],[0.5678255163920121,0.18413583128677083,-0.013890214504789684],[0.5083344985110346,0.1392454453432068,-0.39433090572520657],[0.5896584420737281,0.08379288235131876,-0.2576729215564284],[0.3295088298909952,0.235567779115248,-0.5356937533291555],[0.5000250243306863,0.3018141976737849,-0.20498867278783764],[0.6185044714525195,0.09067692476775965,0.15336081771700635],[0.25526889922349266,0.2639652054848482,-0.5669140368671568],[0.6173002492091398,0.09494710934514983,-0.16487178746888842],[0.07720569642113896,0.23966822196494703,-0.6297820462966913],[0.39460375661187824,0.1940330716023354,-0.5025477300220788],[0.4655339346997888,0.05866333781973897,0.4627417713018576],[0.10870977815023633,0.09711478665312279,-0.6406540998825566],[0.10843432034835586,0.41192937881016284,-0.5047309080349639],[0.3700713859782687,0.03635229655853231,0.559597844377924],[0.13413722750246862,-0.2308013234345557,-0.5240984665322866],[0.2647772060393838,-0.20290742519391197,-0.4861861759794428],[0.1758421076237783,0.29107738402809236,-0.5872464890834691],[0.5356031124784636,0.07306855534156016,0.36281391359604226],[0.5856377004876611,0.08346948816643282,0.2602504429579678],[0.6344297785011245,0.0935920950883908,0.04454328679829971],[0.5023803473963616,-0.07368567097335713,-0.3680869457975179]]}
```
