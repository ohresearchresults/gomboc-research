"""Increase the weakest actual-centroid escape margin in a full contact chart.

All accepted states are convex physical bodies within the selected equilibrium
quota. The all-contact exact body is frozen separately; margin size is not a
certificate of the requested complexity.
"""
import argparse,json,time
from pathlib import Path
import numpy as np
from scipy.optimize import linprog
from scipy.sparse import csr_matrix,hstack,vstack,eye
from contact_numpy import Chart
from contact_quota_polish import guards,metric
from exact_contact_audit import audit
from exact_barcode_report import report

def run(source,out,steps,S,U):
 c=Chart(source);out=Path(out);out.mkdir(parents=True,exist_ok=False);q=c.q0.copy();trace=[];trust=.025;start=time.time();(out/'source_construction.json').write_bytes(Path(source).read_bytes());gapfloor=1e-7
 for it in range(steps):
  g=c.physical(q);v,J,cl=guards(c,g,S,U);margin=float(min(v));assert margin>0 and cl[0]<=U and cl[1]<=S;row=dict(it=it,margin=margin,S=cl[1],U=cl[0],gap=float(min(g['noncontact'])),trust=trust,seconds=time.time()-start);trace.append(row);np.save(out/'latest_q.npy',q);(out/'trace.json').write_text(json.dumps(trace,indent=2))
  if it%10==0:print('CONTACT_MARGIN_GROWTH',out,row,flush=True)
  W=metric(c,g);d=c.d;bound=trust/np.sqrt(d);JG=g['Dgap'][~c.incidence]@W;rhs=g['noncontact']-gapfloor;keep=rhs<=bound*np.sum(abs(JG),axis=1)+1e-10;n=int(sum(keep));I=eye(d);sc=.001;A=vstack([hstack([-csr_matrix(J@W/sc),csr_matrix(np.ones((len(v),1))),csr_matrix((len(v),d))]),hstack([-csr_matrix(JG[keep]/sc),csr_matrix((n,1+d))]),hstack([I,csr_matrix((d,1)),-I]),hstack([-I,csr_matrix((d,1)),-I])],format='csr');b=np.r_[v/sc,rhs[keep]/sc,np.zeros(2*d)];r=linprog(np.r_[np.zeros(d),-1.,np.full(d,1e-5)],A_ub=A,b_ub=b,bounds=[(-bound,bound)]*d+[(margin/sc,100.)]+[(0,None)]*d,method='highs',options=dict(primal_feasibility_tolerance=1e-10,dual_feasibility_tolerance=1e-10,time_limit=20.))
  if not r.success:row['error']=r.message;trust*=.4
  else:
   row['linear_margin']=float(r.x[d]*sc);dq=W@r.x[:d];ok=False
   for k in range(16):
    qq=q+2.**-k*dq
    try:gg=c.physical(qq);vv,_,cc=guards(c,gg,S,U)
    except(ValueError,np.linalg.LinAlgError):continue
    if min(vv)>margin+max(1e-13,margin*1e-6)and min(gg['noncontact'])>gapfloor*.9 and cc[0]<=U and cc[1]<=S:q=qq;ok=True;row['alpha']=2.**-k;break
   if ok and k==0:trust=min(.4,trust*1.3)
   if not ok:trust*=.4
  if trust<1e-10:break
 np.save(out/'endpoint_q.npy',q);a=audit(source,out/'endpoint_q.npy',out/'exact_endpoint_g15',10**15);report(out/'exact_endpoint_g15');s=json.loads((out/'exact_endpoint_g15/summary.json').read_text());print('CONTACT_MARGIN_EXACT_ENDPOINT',{k:s[k]for k in ['V','E','F','counts','weak','C_2E','VplusEplusF','goal_met']},flush=True)

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('source');p.add_argument('out');p.add_argument('--steps',type=int,default=1500);p.add_argument('--S',type=int,default=1);p.add_argument('--U',type=int,default=1);a=p.parse_args();run(a.source,a.out,a.steps,a.S,a.U)
