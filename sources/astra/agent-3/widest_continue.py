import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import numpy as np,json,time,argparse
from pathlib import Path
from scipy.optimize import linprog
from scipy.sparse import csr_matrix,hstack,vstack,eye
from vertex_geometry import geometry,widest,summary
from support_geometry import escape

def run(path,out,steps,eps,trust0):
 out=Path(out);out.mkdir(exist_ok=False,parents=True);X=np.load(path);np.save(out/'initial.npy',X);trust=trust0;hist=[];t0=time.time()
 for it in range(steps):
  g=geometry(X);ci=summary(g);ci.update(it=it,trust=trust,elapsed=time.time()-t0);hist.append(ci);print('WIDEST',ci,flush=True)
  (out/'history.json').write_text(json.dumps(hist,indent=2));np.save(out/'latest.npy',X)
  rp,pp,bp=widest(g['Z']);rq,pq,bq=widest(g['H']);vp,jp,Jp=escape(g['Z'],g['DZ'],chosen=pp);vq,jq,Jq=escape(g['H'],g['DH'])
  kp=np.arange(len(vp))!=rp;kq=np.arange(len(vq))!=rq;vp=vp[kp];Jp=Jp[kp];vq=vq[kq];Jq=Jq[kq];current=bp.min()
  if current>1e-10 and ci['S']==ci['U']==1:
   np.save(out/'potential.npy',X);(out/'potential.json').write_text(json.dumps(ci,indent=2));print('POTENTIAL_WIDEST110',out,flush=True);break
  d=X.size;I=eye(d);O=csr_matrix((d,1));mp=len(vp);mq=len(vq)
  A=vstack([hstack([-csr_matrix(Jp),np.ones((mp,1)),csr_matrix((mp,d))]),hstack([-csr_matrix(Jq),csr_matrix((mq,1)),csr_matrix((mq,d))]),hstack([I,O,-I]),hstack([-I,O,-I])],format='csr')
  qtarget=np.minimum(vq,eps);b=np.r_[vp,vq-qtarget,np.zeros(2*d)];obj=np.r_[np.zeros(d),-1,np.full(d,1e-7)]
  sol=linprog(obj,A_ub=A,b_ub=b,bounds=[(-trust,trust)]*d+[(None,eps)]+[(0,None)]*d,method='highs')
  if not sol.success:
   ci['lp_failure']=sol.message;trust*=.5
   if trust<1e-10:break
   continue
  dx=sol.x[:d].reshape(X.shape);ci['predicted']=float(sol.x[d]);accepted=False
  for alpha in [1.,.5,.25,.125,.0625,.03125,.015625,.0078125,.00390625,.001953125,.0009765625]:
   xx=X+alpha*dx;gg=geometry(xx,False);cc=summary(gg)
   if cc['S']==1 and cc['dual_bottleneck']>0 and cc['primal_bottleneck']>current+max(1e-13,abs(current)*1e-7):
    X=xx;accepted=True;ci['alpha']=alpha
    if alpha>.99:trust=min(trust*1.25,.05)
    break
  if not accepted:trust*=.4
  if trust<1e-10:break
 print('WIDEST_FINISHED',out,hist[-1],flush=True)
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('input');p.add_argument('output');p.add_argument('--steps',type=int,default=400);p.add_argument('--epsilon',type=float,default=1e-7);p.add_argument('--trust',type=float,default=.005);a=p.parse_args();run(a.input,a.output,a.steps,a.epsilon,a.trust)
