"""Full-contact-chart semismooth correction; numerical discovery, not an exact certificate."""
from general_atlas import *
from scipy.optimize import linprog
import qp

def lp_l1(A,lo,hi,lb,ub,cost):
 n=len(lb);eq=np.isfinite(hi)&(lo==hi);il=np.isfinite(lo)&~eq;ih=np.isfinite(hi)&~eq
 AA=np.vstack((-A[il],A[ih]));bb=np.r_[-lo[il],hi[ih]]
 AA=np.column_stack((AA,np.zeros_like(AA)))
 AA=np.vstack((AA,np.column_stack((np.eye(n),-np.eye(n))),np.column_stack((-np.eye(n),-np.eye(n)))))
 bb=np.r_[bb,np.zeros(2*n)];Ae=np.column_stack((A[eq],np.zeros_like(A[eq])))
 ans=linprog(np.r_[np.zeros(n),cost],A_ub=AA,b_ub=bb,A_eq=Ae,b_eq=lo[eq],bounds=list(zip(lb,ub))+[(0,None)]*n,method='highs-ipm',options={'time_limit':10,'primal_feasibility_tolerance':1e-10,'dual_feasibility_tolerance':1e-10,'ipm_optimality_tolerance':1e-10})
 return (ans.x[:n],None) if ans.success else (None,ans.message)

def warm(s,steps=2000):
 best=[np.inf,None]
 def fun(z):
  r=s.residual(z);obj=float(r@r)
  if obj<best[0]:best[:]=[obj,z.copy()]
  return r
 least_squares(fun,np.zeros(s.n),jac=s.derivative,max_nfev=steps,ftol=1e-13,xtol=1e-13,gtol=1e-13,x_scale='jac',verbose=0)
 return best[1]

def correct(s,z,steps=100):
 z=np.array(z).copy();trust=.03;qbound=.004;records=[]
 for it in range(steps):
  v,J,g=s.evaluate(z);merit=float(np.linalg.norm(s.residual(z)))
  row=dict(iteration=it,merit=merit,minimum_mechanical=float(v[:s.mechlen].min()),minimum_nonowner_slack=float(g['slack'].min()),trust=trust)
  records.append(row);print('CORRECT',json.dumps(row),flush=True)
  if v[:s.mechlen].min()>1.5e-7 and g['slack'].min()>1e-8 and g['v6'].min()>0:return z,records
  Y,DY=contact(s.G,s.base+s.scale*z,s.free);JQ=(DY[:137]*s.scale[None,None,:]).reshape(-1,s.n)
  A=np.vstack((J/s.rescale[:,None],JQ));lo=np.r_[(s.floor-v)/s.rescale,np.full(411,-qbound)];hi=np.r_[np.full(len(v),np.inf),np.full(411,qbound)];lb=np.full(s.n,-trust);ub=np.full(s.n,trust)
  dz,status=qp.solve(A,lo,hi,lb,ub,np.ones(s.n))
  if dz is None:
   dz,status=lp_l1(A,lo,hi,lb,ub,np.ones(s.n))
   if dz is None:
    records[-1]['failure']=status;trust=min(.5,trust*1.5);qbound=min(.05,qbound*1.5);continue
  accepted=False
  for alpha in [1.,.5,.25,.125,.0625,.03125,.015625,.0078125]:
   zz=z+alpha*dz;new=float(np.linalg.norm(s.residual(zz)))
   if np.isfinite(new) and (new<merit*(1-1e-5) or new<1e-8):z=zz;accepted=True;break
  records[-1]['alpha']=alpha;records[-1]['accepted']=accepted
  if not accepted:trust*=.5;qbound*=.5
  if trust<1e-7:break
 return z,records
