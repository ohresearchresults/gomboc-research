"""Prescribed physical edge contraction with explicit nonlinear admission.

A normalized physical endpoint-distance equation is imposed together with the
true uniform-centroid equilibrium inequalities. Short edges remain counted.
"""
import argparse,json,time
from pathlib import Path
import numpy as np
from scipy.optimize import linprog
from scipy.sparse import csr_matrix,eye,hstack,vstack
from contact_numpy import Chart
from contact_quota_polish import metric,guards
from exact_contact_audit import audit
from exact_barcode_report import report

def edge(g,pair,kind):
 A,DA=(g['Z'],g['DZ'])if kind=='primal'else(g['H'],g['DH']);i,j=pair;r=np.sqrt(np.mean(np.sum(A*A,axis=1)));Dr=np.mean(np.einsum('ic,icp->ip',A,DA),axis=0)/r;e=A[i]-A[j];return e/r,(DA[i]-DA[j])/r-e[:,None]*Dr/r**2

def retract(c,q,pair,kind,target,eps,out):
 out=Path(out);out.mkdir(parents=True,exist_ok=False);trace=[];trust=.04
 def values(q):
  g=c.physical(q,require_valid=False);v,J,cl=guards(c,g,1,1);e,Je=edge(g,pair,kind);gap=g['noncontact'];vv=np.r_[gap,v];tt=np.r_[np.full(len(gap),1e-11),np.full(len(v),eps)];JJ=np.vstack((g['Dgap'][~c.incidence],J));length=np.linalg.norm(e);res=np.array([length-target]);Je=(e@Je/length)[None,:];merit=float(np.maximum(tt-vv,0).sum()+np.linalg.norm(res,1));return g,vv,tt,JJ,res,Je,merit,cl
 for it in range(36):
  g,v,t,J,res,Je,merit,cl=values(q);row=dict(it=it,S=cl[1],U=cl[0],valid=bool(g['valid']),edge_error=float(np.linalg.norm(res)),merit=merit,minimum_slack=float(min(v-t)),trust=trust);trace.append(row);np.save(out/'latest_q.npy',q);(out/'trace.json').write_text(json.dumps(trace,indent=2))
  if g['valid']and cl==[1,1]and min(v-t)>-eps*.08 and np.linalg.norm(res)<1e-11:return q,True,trace
  W=metric(c,g);d=c.d;bound=trust/np.sqrt(d);JW=J@W;keep=v-t<=bound*np.sum(abs(JW),axis=1)+1e-10;m=int(sum(keep));I=eye(d);zero=csr_matrix((d,m));sc=.001;A=vstack([hstack([-csr_matrix(JW[keep]/sc),-eye(m),csr_matrix((m,d))]),hstack([I,zero,-I]),hstack([-I,zero,-I])],format='csr');b=np.r_[(v[keep]-t[keep])/sc,np.zeros(2*d)];AE=hstack([csr_matrix((Je@W)*1e5),csr_matrix((1,m+d))],format='csr');r=linprog(np.r_[np.zeros(d),np.ones(m),np.full(d,1e-5)],A_ub=A,b_ub=b,A_eq=AE,b_eq=-res*1e5,bounds=[(-bound,bound)]*d+[(0,None)]*(m+d),method='highs',options=dict(primal_feasibility_tolerance=1e-10,dual_feasibility_tolerance=1e-10,time_limit=12.))
  if not r.success:row['error']=r.message;return q,False,trace
  dq=W@r.x[:d];ok=False
  for k in range(12):
   qq=q+2.**-k*dq
   try:*_,mm,cc=values(qq)
   except(ValueError,np.linalg.LinAlgError):continue
   if np.isfinite(mm)and mm<merit-max(1e-14,merit*1e-7):q=qq;ok=True;row['alpha']=2.**-k;break
  if not ok:return q,False,trace
 return q,False,trace

def run(source,out,pair,kind,steps):
 c=Chart(source);out=Path(out);out.mkdir(parents=True,exist_ok=False);q=c.q0.copy();g=c.physical(q);v,_,cl=guards(c,g,1,1);assert cl==[1,1]and min(v)>0;eps=min(float(min(v))*.1,1e-9);initial=np.linalg.norm(edge(g,pair,kind)[0]);fraction=.1;trace=[];start=time.time();(out/'method.json').write_text(json.dumps(dict(source=str(Path(source).resolve()),pair=pair,kind=kind,epsilon=eps,initial_length=float(initial)),indent=2))
 for it in range(steps):
  g=c.physical(q);e,_=edge(g,pair,kind);target=float(np.linalg.norm(e)*(1-fraction));qq,good,detail=retract(c,q.copy(),pair,kind,target,eps,out/f'attempt{it:03d}');gg=c.physical(qq,require_valid=False);ee,_=edge(gg,pair,kind);row=dict(it=it,fraction=fraction,accepted=False,proposed_length_ratio=float(np.linalg.norm(ee)/initial),correction_steps=len(detail),seconds=time.time()-start)
  if good:
   q=qq;row['accepted']=True;fraction=min(.2,fraction*1.3)
  else:fraction*=.5
  current=c.physical(q);vv,_,cc=guards(c,current,1,1);assert cc==[1,1];row.update(length_ratio=float(np.linalg.norm(edge(current,pair,kind)[0])/initial),minimum=float(min(vv)),gap=float(min(current['noncontact'])));trace.append(row);np.save(out/'latest_q.npy',q);(out/'trace.json').write_text(json.dumps(trace,indent=2));print('STRICT110_EDGE_HOMOTOPY',row,flush=True)
  if row['length_ratio']<.01 or fraction<1e-5:break
 np.save(out/'endpoint_q.npy',q);audit(source,out/'endpoint_q.npy',out/'exact_endpoint_g15',10**15);report(out/'exact_endpoint_g15');s=json.loads((out/'exact_endpoint_g15/summary.json').read_text());print('EDGE_HOMOTOPY_EXACT',{k:s[k]for k in ['V','E','F','counts','weak','goal_met']},flush=True)

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('source');p.add_argument('out');p.add_argument('--pair',nargs=2,type=int,required=True);p.add_argument('--kind',choices=['primal','dual'],default='primal');p.add_argument('--steps',type=int,default=60);a=p.parse_args();run(a.source,a.out,a.pair,a.kind,a.steps)
