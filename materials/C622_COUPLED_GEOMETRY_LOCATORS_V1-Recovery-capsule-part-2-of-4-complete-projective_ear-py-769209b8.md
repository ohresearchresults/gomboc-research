# material-769209b8722e

AI research material

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

"""Actual refilled positive projective and reciprocal-metric numerical locator.
Uses only persisted canonical inputs and global_cut.py; no chosen mass center.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import sys,json,platform
from pathlib import Path
import numpy as np
import scipy
from scipy.optimize import linprog
import global_cut as gc
B=np.array([[[1,0,0],[0,0,0],[0,0,-1]],[[0,0,0],[0,1,0],[0,0,-1]],
 [[0,1,0],[1,0,0],[0,0,0]],[[0,0,1],[0,0,0],[1,0,0]],[[0,0,0],[0,0,1],[0,1,0]]],float)
PARS=dict(iterations=160,radius0=.002,radius_min=1e-12,radius_max=.1,
          eigen_floor=1e-6,projective_den_floor=.02,accept=1e-7,
          halvings=25,target=1e-11,lp_scale=1e6,complex_step=1e-24)

def basegeometry(Q):
 z=gc.geometry(Q);ct=gc.census(z);assert ct['euler']==2
 # Keep the origin for the positive tetrahedral projective mass formula.
 X=z['X'];PP=Q[ct['active']];T=z['triangles']
 det=np.einsum('ij,ij->i',X[T[:,0]],np.cross(X[T[:,1]],X[T[:,2]]))
 assert det.min()>0
 norms=[]
 for A in [X-z['J']/z['V'],PP/(1-PP@(z['J']/z['V']))[:,None]]:
  d=A[None,:,:]-A[:,None,:]
  w=np.linalg.norm(A,axis=1)[:,None]*np.linalg.norm(d,axis=2);w[w==0]=1;norms.append(w)
 return dict(X=X,Q=PP,T=T,det=det,norms=norms,census=ct)

def matrices(b,p):
 u=p[:3];M=np.eye(3,dtype=p.dtype)+np.einsum('k,kab->ab',p[3:],B);N=np.linalg.inv(M)
 den=1+b['X']@u;Y=b['X']/den[:,None]
 ds=b['det']/np.prod(den[b['T']],axis=1)
 V=ds.sum()/6;g=(ds[:,None]*Y[b['T']].sum(axis=1)).sum(axis=0)/(24*V)
 X=Y-g
 # Projective support is (q+u).Y<=1; center at actual newly integrated g.
 Q=b['Q']+u;Q=Q/(1-Q@g)[:,None]
 D=[]
 for A,H,w in zip([X,Q],[M,N],b['norms']):
  v=A@H@A.T-np.sum((A@H)*A,axis=1)[:,None];v/=w;D.append(v)
 return D,dict(M=M,N=N,den=den,V=V,g=g,X=X,Q=Q)

def evaluate(b,p,derivative=False):
 try:D,z=matrices(b,p)
 except np.linalg.LinAlgError:return None
 if min(z['den'])<=PARS['projective_den_floor'] or np.linalg.eigvalsh(z['M'])[0]<=PARS['eigen_floor']:return None
 witnesses=[];roots=[];sg=[];guards=[];counts=[]
 for v in D:
  np.fill_diagonal(v,-np.inf);j=v.argmax(axis=1);vals=v[np.arange(len(v)),j]
  r=int(np.argmin(vals));sign=np.ones(len(v));sign[r]=-1
  roots.append(r);witnesses.append(j);sg.append(sign);guards.extend(sign*vals);counts.append(int((vals<0).sum()))
 jac=None
 if derivative:
  jac=np.zeros((sum(map(len,D)),8))
  for k in range(8):
   pp=p.astype(complex);pp[k]+=1j*PARS['complex_step'];dd,_=matrices(b,pp)
   jac[:,k]=np.concatenate([sign*v[np.arange(len(v)),j].imag/PARS['complex_step'] for v,j,sign in zip(dd,witnesses,sg)])
 return dict(margin=float(min(guards)),guards=np.array(guards),jac=jac,roots=roots,counts=counts,
             M=z['M'],N=z['N'],V=float(z['V']),g=z['g'],min_den=float(min(z['den'])))

def optimize(b,p0):
 p=p0.copy();radius=PARS['radius0'];current=evaluate(b,p,True);hist=[]
 for it in range(PARS['iterations']):
  val=current['margin'];hist.append(dict(i=it,margin=val,radius=radius,counts=current['counts'],roots=current['roots']))
  if val>PARS['target']:break
  s=PARS['lp_scale'];G=current['jac']
  lp=linprog([0]*8+[-1],A_ub=np.c_[-G*s,np.ones(len(G))],b_ub=current['guards']*s,
   bounds=[(-radius,radius)]*8+[(None,None)],method='highs',options={'dual_feasibility_tolerance':1e-9,'primal_feasibility_tolerance':1e-9})
  if not lp.success:hist[-1]['lp_failure']=lp.message;break
  step=lp.x[:8];best=None
  for h in range(PARS['halvings']):
   pp=p+2.**(-h)*step;new=evaluate(b,pp,False)
   if new is not None and new['margin']>val+max(1e-16,PARS['accept']*abs(val)):
    best=pp,h;break
  if best is None:
   radius*=.25
   if radius<PARS['radius_min']:break
  else:
   p,h=best;current=evaluate(b,p,True)
   if h==0:radius=min(PARS['radius_max'],radius*1.4)
   elif h>5:radius*=.5
 return dict(parameters=p.tolist(),M=current['M'].tolist(),N=current['N'].tolist(),
  g=current['g'].tolist(),volume=current['V'],min_den=current['min_den'],
  margin=current['margin'],counts_U_S=current['counts'],history=hist)

def main():
 assert len(sys.argv)==7,'A raw checkpoint OUTPUT MODE LIMIT'
 a,Q,ears,facets=gc.load(sys.argv[1],sys.argv[2]);ed={x['vertex']:x for x in ears};mode=sys.argv[5]
 cps=json.loads(Path(sys.argv[3]).read_text());assert gc.sha(sys.argv[3])=='189ad64e23592936d2094b9d8fcdfd661bef49fe62759808ec94bcd9abc832bd'
 if mode=='ear':cps=[{'ear':i} for i in sorted(set(c['ear'] for c in cps))]
 elif mode!='cut':raise ValueError(mode)
 cps=cps[:int(sys.argv[6])]
 out=dict(status='NUMERICAL_PROJECTIVE_AFFINE_OWN_COM_NOT_CERTIFICATE',parameters=PARS,mode=mode,
  versions=[platform.python_version(),np.__version__,scipy.__version__],trials=[])
 for cp in cps:
  if mode=='ear':QQ=np.vstack([Q,ed[cp['ear']]['q']])
  else:QQ=np.vstack([np.delete(Q,cp['released'],0),ed[cp['ear']]['q'],cp['q']])
  b=basegeometry(QQ);res=optimize(b,np.zeros(8));res['checkpoint']=cp;res['float_census']=b['census']
  out['trials'].append(res);Path(sys.argv[4]).write_text(json.dumps(out,sort_keys=True,separators=(',',':'))+'\n')
  print('PROJECTIVE',mode,cp,b['census']['C'],res['counts_U_S'],res['margin'],len(res['history']),flush=True)
 print('PROJECTIVE_AFFINE_TRUE_COM_LOCATOR_FINISHED_NOT_CERTIFICATE',len(out['trials']),flush=True)
if __name__=='__main__':main()
