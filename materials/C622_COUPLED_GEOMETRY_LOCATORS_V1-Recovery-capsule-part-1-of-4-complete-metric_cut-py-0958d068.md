# material-0958d068b39b

AI research material

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

"""Common reciprocal SPD metric locator on persisted centered-cut checkpoints.
NUMERICAL ONLY. Every trial uses M and exactly its floating inverse N.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import sys,json,hashlib,platform
from pathlib import Path
import numpy as np
import scipy
from scipy.optimize import linprog
import global_cut as gc
B=np.array([[[1,0,0],[0,0,0],[0,0,-1]],[[0,0,0],[0,1,0],[0,0,-1]],
 [[0,1,0],[1,0,0],[0,0,0]],[[0,0,1],[0,0,0],[1,0,0]],[[0,0,0],[0,0,1],[0,1,0]]],float)
PARS=dict(iterations=120,radius0=.01,radius_min=1e-12,radius_max=.1,
          eigen_floor=1e-6,accept=1e-7,halvings=24,target=1e-11,lp_scale=1e6)
def rawforms(X):
 d=X[None,:,:]-X[:,None,:]
 norm=np.linalg.norm(X,axis=1)[:,None]*np.linalg.norm(d,axis=2)
 norm[norm==0]=1
 A=(np.einsum('ia,ijb->ijab',X,d)+np.einsum('ijb,ia->ijba',d,X))/2
 A/=norm[:,:,None,None]
 return A

def primitive(A,M):
 D=np.einsum('ijab,ab->ij',A,M);np.fill_diagonal(D,-np.inf);return D

def evaluate(A,C,p,derivative=False):
 M=np.eye(3)+np.einsum('k,kab->ab',p,B)
 if np.linalg.eigvalsh(M)[0]<=PARS['eigen_floor']:return None
 N=np.linalg.inv(M);DS=[primitive(A,M),primitive(C,N)]
 roots=[];guards=[];jac=[]
 for typ,(D,T) in enumerate(zip(DS,[A,C])):
  j=D.argmax(axis=1);v=D[np.arange(len(D)),j]
  # A unique source can only be the global radius maximum; choose the most
  # negative current vertex escape. This keeps an existing strict sink when possible.
  root=int(np.argmin(v));roots.append(root);sgn=np.ones(len(v));sgn[root]=-1
  guards.extend(sgn*v)
  if derivative:
   act=T[np.arange(len(D)),j]
   if typ==1:act=-np.einsum('ab,ibc,cd->iad',N,act,N)
   jac.extend(sgn[:,None]*np.einsum('iab,kab->ik',act,B))
 g=np.array(guards)
 return dict(M=M,N=N,roots=roots,guards=g,jac=np.array(jac) if derivative else None,
       margin=float(g.min()),counts=[int((D.max(axis=1)<0).sum()) for D in DS])

def optimize(A,C):
 p=np.zeros(5);radius=PARS['radius0'];hist=[];current=evaluate(A,C,p,True)
 for it in range(PARS['iterations']):
  val=current['margin'];hist.append(dict(i=it,margin=val,radius=radius,counts=current['counts'],roots=current['roots']))
  if val>PARS['target']:break
  G=current['jac'];s=PARS['lp_scale']
  aa=np.c_[-G*s,np.ones(len(G))];bb=current['guards']*s
  # t is the predicted common guard margin scaled by s.
  lp=linprog([0]*5+[-1],A_ub=aa,b_ub=bb,bounds=[(-radius,radius)]*5+[(None,None)],method='highs',
      options={'dual_feasibility_tolerance':1e-9,'primal_feasibility_tolerance':1e-9})
  if not lp.success:
   hist[-1]['lp_failure']=lp.message;break
  step=lp.x[:5];best=None
  for h in range(PARS['halvings']):
   alpha=2.**(-h);pp=p+alpha*step;new=evaluate(A,C,pp,True)
   if new is None:continue
   if new['margin']>val+max(1e-16,PARS['accept']*abs(val)):
    best=(pp,new,h);break
  if best is None:
   radius*=.25
   if radius<PARS['radius_min']:break
  else:
   p,current,h=best
   if h==0:radius=min(PARS['radius_max'],radius*1.4)
   elif h>5:radius*=.5
 return dict(parameters=p.tolist(),M=current['M'].tolist(),N=current['N'].tolist(),
             margin=current['margin'],counts_U_S=current['counts'],history=hist)

def main():
 assert len(sys.argv)==6,'A raw checkpoint OUTPUT LIMIT'
 assert gc.sha(sys.argv[3])=='189ad64e23592936d2094b9d8fcdfd661bef49fe62759808ec94bcd9abc832bd'
 a,Q,ears,facets=gc.load(sys.argv[1],sys.argv[2]);earmap={x['vertex']:x for x in ears}
 cps=json.loads(Path(sys.argv[3]).read_text())[:int(sys.argv[5])]
 out=dict(status='NUMERICAL_COMMON_METRIC_LOCATOR_NOT_CERTIFICATE',parameters=PARS,
   versions=[platform.python_version(),np.__version__,scipy.__version__],checkpoint_sha=gc.sha(sys.argv[3]),trials=[])
 for cp in cps:
  K=np.vstack([np.delete(Q,cp['released'],axis=0),earmap[cp['ear']]['q']]);z=gc.geometry(K,np.array(cp['q']))
  ct=gc.census(z);assert ct['euler']==2
  g=z['J']/z['V'];X=z['X']-g;PP=z['Q'][ct['active']];PP/=1-(PP@g)[:,None]
  res=optimize(rawforms(X),rawforms(PP));res['checkpoint']=cp;res['float_census']=ct
  out['trials'].append(res);Path(sys.argv[4]).write_text(json.dumps(out,sort_keys=True,separators=(',',':'))+'\n')
  print('METRIC',cp['ear'],cp['released'],ct['C'],res['counts_U_S'],res['margin'],len(res['history']),flush=True)
 print('COMMON_METRIC_CENTERED_CUT_LOCATOR_FINISHED_NOT_CERTIFICATE',len(out['trials']),flush=True)
if __name__=='__main__':main()
