"""Change a stable-face/U incidence inside the bicap family's existing budget.
Uses an inactive intermediate input slot, creates a real convex-hull extension,
and recomputes actual homogeneous mass and full numerical persistence.
The foot-to-U cap formula was independently shared in agent3/detach_stable.py.
"""
import json,sys,numpy as np
from bicap_search import ROOT,graph,Search,stats,coords
from bicap_polish import run as polish
source=ROOT/'artifacts/bicap_search/closure_seed1_extra0';meta=json.loads((source/'construction.json').read_text());b,t=meta['bottom'],meta['top'];q0=np.load(source/'polish12/STRICT_NUMERICAL_theta.npy');g=graph(q0,b,t);N=len(g['X']);M=N-b-t
ue=np.linalg.norm(g['Z'],axis=1);ue[g['xm']==0]=0;U=int(np.argmax(ue));scores=__import__('geometry').angular_scores(g['Y']);scores[:,g['ym']==0]=-np.inf;sf=np.flatnonzero((scores.max(1)<0)&(g['ym']>0));f=next(int(f) for f in sf if f<len(g['Y'])-2);carrier=np.flatnonzero(abs(g['Z']@g['Y'][f]-1)<1e-7);W=int(carrier[np.argmax(np.linalg.norm(g['Z'][carrier],axis=1))]);foot=g['c']+g['Y'][f]/(g['Y'][f]@g['Y'][f]);slot=next(i for i in range(b+t,N) if g['xm'][i]==0)
base=ROOT/'artifacts/bicap_detach';base.mkdir(exist_ok=True);rows=[]
for tau in [.25,.5,.75]:
 for eps in [.0001,.001,.01,.03,.1]:
  p=(1-tau)*foot+tau*g['X'][W]+eps*(foot-g['c']);H=np.exp(q0[-3])+p[:2]@q0[-2:]
  if not 0<p[2]<H:continue
  q=q0.copy();q[2*slot:2*slot+2]=p[:2];q[2*N+slot-b-t]=np.log(p[2]/(H-p[2]));gg=graph(q,b,t);name=f't{tau:g}_eps{eps:g}';out=base/name;out.mkdir(exist_ok=True);(out/'construction.json').write_text(json.dumps(dict(meta,source_theta=str(source/'polish12/STRICT_NUMERICAL_theta.npy'),stable_facet=f,U=U,anchor_vertex=W,input_slot=slot,foot=foot.tolist(),mix=tau,epsilon=eps),indent=2)+'\n');np.save(out/'initial_theta.npy',q);row=stats(gg);row.update(name=name);rows.append(row);print('DETACH_INITIAL',row,flush=True)
(base/'screen.json').write_text(json.dumps(rows,indent=2)+'\n')
# Selected finite caps receive all-coordinate deformation and strict retraction.
for name in ['t0.25_eps0.01','t0.5_eps0.03','t0.75_eps0.1']:
 out=base/name
 if not out.exists():continue
 q=np.load(out/'initial_theta.npy')
 for k in range(5):
  ob=Search(q,b,t,out/f'descent{k}',.003);q=ob.run(1500)
  if ob.target:break
  q=polish(q,b,t,out/f'polish{k}',1,2,250)
  np.save(out/f'cycle{k}_theta.npy',q)
