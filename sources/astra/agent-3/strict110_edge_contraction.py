"""Approach a real contact event from inside the strict own110 region.

The existing incidence is retained during each finite step. Edge length is a
continuous objective; no short edge is ever counted as absent. A subsequent
topology reconstruction and exact audit is required to lower complexity.
"""
import argparse,json,time
from pathlib import Path
import numpy as np
from scipy.optimize import linprog
from contact_numpy import Chart
from contact_quota_polish import metric,guards
from contact_polynomial_flow import correct
from exact_contact_audit import audit
from exact_barcode_report import report

def objective(g,pair,kind):
 A,DA=(g['Z'],g['DZ'])if kind=='primal'else(g['H'],g['DH']);i,j=pair;e=A[i]-A[j];de=DA[i]-DA[j];s=np.mean(np.sum(A*A,axis=1));ds=2*np.mean(np.einsum('ic,icp->ip',A,DA),axis=0);e2=e@e;return float(e2/s),2*e@de/s-e2*ds/s**2

def run(source,out,pair,kind,steps):
 c=Chart(source);out=Path(out);out.mkdir(parents=True,exist_ok=False);q=c.q0.copy();g=c.physical(q);rr=[[int(np.argmax(np.sum(g['Z']**2,axis=1)))],[int(np.argmax(np.sum(g['H']**2,axis=1)))]];v,_,cl=guards(c,g,1,1);assert cl==[1,1]and min(v)>0;eps=min(1e-9,float(min(v))*.1);gapfloor=1e-12;trust=.04;trace=[];start=time.time();base,_=objective(g,pair,kind);(out/'method.json').write_text(json.dumps(dict(source=str(Path(source).resolve()),pair=pair,kind=kind,epsilon=eps,gapfloor=gapfloor,initial_relative_length_squared=base),indent=2));rng=np.random.default_rng(93084);d=rng.normal(size=c.d);d/=np.linalg.norm(d);cost,J=objective(g,pair,kind);checks=[]
 for h in [1e-6,1e-7]:checks.append(dict(h=h,analytic=float(J@d),fd=float((objective(c.physical(q+h*d,require_valid=False),pair,kind)[0]-objective(c.physical(q-h*d,require_valid=False),pair,kind)[0])/(2*h))))
 (out/'gradient_check.json').write_text(json.dumps(checks,indent=2))
 for it in range(steps):
  g=c.physical(q);cost,J=objective(g,pair,kind);v,JV,cl=guards(c,g,1,1);assert cl==[1,1];row=dict(it=it,cost=cost,length_ratio=float(np.sqrt(cost/base)),margin=float(min(v)),gap=float(min(g['noncontact'])),trust=trust,seconds=time.time()-start);trace.append(row);np.save(out/'latest_q.npy',q);(out/'trace.json').write_text(json.dumps(trace,indent=2))
  if it%5==0:print('STRICT110_EDGE_CONTRACTION',out,row,flush=True)
  W=metric(c,g);dim=c.d;bound=trust/np.sqrt(dim);gap=g['noncontact'];JG=g['Dgap'][~c.incidence]@W;rhs=gap-gapfloor;keep=rhs<=bound*np.sum(abs(JG),axis=1)+1e-10;A=-np.vstack((JG[keep],JV@W));b=np.r_[rhs[keep],v-eps];r=linprog(J@W,A_ub=A/.001,b_ub=b/.001,bounds=[(-bound,bound)]*dim,method='highs',options=dict(primal_feasibility_tolerance=1e-10,dual_feasibility_tolerance=1e-10,time_limit=20.))
  if not r.success:row['error']=r.message;trust*=.4
  else:
   dq=W@r.x;ok=False
   for k in range(12):
    trial=q+2.**-k*dq
    try:
     qq,good,ncorr=correct(c,trial,W,rr,eps,gapfloor)
     if not good:continue
     gg=c.physical(qq);val,_=objective(gg,pair,kind);vv,_,cc=guards(c,gg,1,1)
    except(ValueError,np.linalg.LinAlgError):continue
    if val<cost-max(1e-14,cost*1e-7)and cc==[1,1]:q=qq;ok=True;row.update(alpha=2.**-k,corrections=ncorr);break
   if ok and k==0:trust=min(.3,trust*1.3)
   if not ok:trust*=.4
  if trust<1e-9 or cost/base<1e-8:break
 np.save(out/'endpoint_q.npy',q);a=audit(source,out/'endpoint_q.npy',out/'exact_endpoint_g15',10**15);report(out/'exact_endpoint_g15');s=json.loads((out/'exact_endpoint_g15/summary.json').read_text());print('EXACT_EDGE_CONTRACTION_ENDPOINT',{key:s[key]for key in ['V','E','F','counts','weak','goal_met']},flush=True)

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('source');p.add_argument('out');p.add_argument('--pair',type=int,nargs=2,required=True);p.add_argument('--kind',choices=['primal','dual'],default='primal');p.add_argument('--steps',type=int,default=100);a=p.parse_args();run(a.source,a.out,a.pair,a.kind,a.steps)
