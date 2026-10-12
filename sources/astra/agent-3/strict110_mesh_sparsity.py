"""Collective geometric contraction inside the physical own110 region.

For each genuine edge, primal endpoint distance times its centered-polar dual
endpoint distance is invariant under uniform scaling. A concave logarithmic
penalty favors concentrating these products into fewer edges. An edge is
never removed merely because this score is small.
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

def objective(c,g,delta):
 a,b=c.pe.T;f,h=c.qe.T;e=g['Z'][a]-g['Z'][b];de=g['DZ'][a]-g['DZ'][b];q=g['H'][f]-g['H'][h];dq=g['DH'][f]-g['DH'][h];L=np.sum(e*e,axis=1);D=np.sum(q*q,axis=1);P=L*D;DP=2*D[:,None]*np.einsum('ic,icp->ip',e,de)+2*L[:,None]*np.einsum('ic,icp->ip',q,dq);val=float(np.log1p(P/delta**2).sum());grad=np.sum(DP/(P+delta**2)[:,None],axis=0);return val,grad,np.sqrt(P)

def normalized_volume(g):
 return float(g['V']/np.mean(np.sum(g['Z']**2,axis=1))**1.5)

def run(source,out,steps,delta):
 c=Chart(source);out=Path(out);out.mkdir(parents=True,exist_ok=False);q=c.q0.copy();g=c.physical(q);v,_,cl=guards(c,g,1,1);assert cl==[1,1]and min(v)>0;rr=[[int(np.argmax(np.sum(g['Z']**2,axis=1)))],[int(np.argmax(np.sum(g['H']**2,axis=1)))]];eps=min(1e-9,float(min(v))*.1);volume_floor=.1*normalized_volume(g);gapfloor=1e-12;trust=.02;trace=[];start=time.time();(out/'source_construction.json').write_bytes(Path(source).read_bytes());(out/'method.json').write_text(json.dumps(dict(delta=delta,epsilon=eps,gapfloor=gapfloor,normalized_volume_floor=volume_floor,energy='sum log(1+(primal_edge_length * own_centroid_polar_dual_edge_length)^2/delta^2)',scope='continuous proposal energy; complete exact hull required to change complexity'),indent=2));rng=np.random.default_rng(952162);d=rng.normal(size=c.d);d/=np.linalg.norm(d);v0,J,_=objective(c,g,delta);checks=[]
 for h in [1e-6,1e-7]:checks.append(dict(h=h,fd=(objective(c,c.physical(q+h*d,require_valid=False),delta)[0]-objective(c,c.physical(q-h*d,require_valid=False),delta)[0])/(2*h),analytic=float(J@d)))
 (out/'gradient_check.json').write_text(json.dumps(checks,indent=2))
 for it in range(steps):
  g=c.physical(q);cost,J,products=objective(c,g,delta);v,JV,cl=guards(c,g,1,1);assert cl==[1,1];row=dict(it=it,energy=cost,minimum_product=float(min(products)),smallest_edges=[dict(index=int(k),primal=c.pe[k].tolist(),dual=c.qe[k].tolist(),product=float(products[k]))for k in np.argsort(products)[:4]],margin=float(min(v)),gap=float(min(g['noncontact'])),normalized_volume=normalized_volume(g),trust=trust,seconds=time.time()-start);trace.append(row);np.save(out/'latest_q.npy',q);(out/'trace.json').write_text(json.dumps(trace,indent=2))
  if it%5==0:print('STRICT110_MESH_SPARSITY',row,flush=True)
  W=metric(c,g);dim=c.d;bound=trust/np.sqrt(dim);JG=g['Dgap'][~c.incidence]@W;rhs=g['noncontact']-gapfloor;keep=rhs<=bound*np.sum(abs(JG),axis=1)+1e-10;A=-np.vstack((JG[keep],JV@W));b=np.r_[rhs[keep],v-eps];sol=linprog(J@W,A_ub=A/.001,b_ub=b/.001,bounds=[(-bound,bound)]*dim,method='highs',options=dict(primal_feasibility_tolerance=1e-10,dual_feasibility_tolerance=1e-10,time_limit=20.))
  if not sol.success:row['error']=sol.message;trust*=.4
  else:
   dq=W@sol.x;ok=False
   for k in range(12):
    trial=q+2.**-k*dq
    try:
     qq,good,ncorr=correct(c,trial,W,rr,eps,gapfloor)
     if not good:continue
     gg=c.physical(qq);val,_,_=objective(c,gg,delta);vv,_,cc=guards(c,gg,1,1)
    except(ValueError,np.linalg.LinAlgError):continue
    if val<cost-max(1e-10,abs(cost)*1e-9)and cc==[1,1]and normalized_volume(gg)>volume_floor:q=qq;ok=True;row.update(alpha=2.**-k,corrections=ncorr);break
   if ok and k==0:trust=min(.3,trust*1.3)
   if not ok:trust*=.4
  if trust<1e-9:break
 np.save(out/'endpoint_q.npy',q);audit(source,out/'endpoint_q.npy',out/'exact_endpoint_g15',10**15);report(out/'exact_endpoint_g15');s=json.loads((out/'exact_endpoint_g15/summary.json').read_text());print('MESH_SPARSITY_EXACT',{k:s[k]for k in ['V','E','F','counts','weak','goal_met']},flush=True)

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('source');p.add_argument('out');p.add_argument('--steps',type=int,default=300);p.add_argument('--delta',type=float,default=1e-5);a=p.parse_args();run(a.source,a.out,a.steps,a.delta)
