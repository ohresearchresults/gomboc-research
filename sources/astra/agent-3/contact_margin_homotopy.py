"""Raise uniform own110 margins by explicit minimum-motion target homotopy."""
import argparse,json,time
from pathlib import Path
import numpy as np
from contact_numpy import Chart
from contact_quota_polish import metric,guards
from contact_polynomial_flow import correct
from exact_contact_audit import audit
from exact_barcode_report import report

def run(source,out,steps):
 c=Chart(source);out=Path(out);out.mkdir(parents=True,exist_ok=False);q=c.q0.copy();trace=[];factor=2.;start=time.time();g=c.physical(q);rr=[[int(np.argmax(np.sum(g['Z']**2,axis=1)))],[int(np.argmax(np.sum(g['H']**2,axis=1)))]];v,_,cl=guards(c,g,1,1);assert cl==[1,1]and min(v)>0;(out/'source_construction.json').write_bytes(Path(source).read_bytes())
 for it in range(steps):
  g=c.physical(q);v,_,cl=guards(c,g,1,1);before=float(min(v));target=min(.001,before*factor);d=out/f'attempt{it:03d}';d.mkdir();np.save(d/'initial_q.npy',q);W=metric(c,g);qq,good,n=correct(c,q.copy(),W,rr,target,1e-8);np.save(d/'proposed_q.npy',qq);gg=c.physical(qq,require_valid=False);vv,_,cc=guards(c,gg,1,1);row=dict(it=it,before=before,target=target,factor=factor,reported_success=bool(good),valid=bool(gg['valid']),S=cc[1],U=cc[0],after=float(min(vv)),gap=float(min(gg['noncontact'])),corrections=n,seconds=time.time()-start)
  if good and gg['valid']and cc==[1,1]and min(vv)>before:
   q=qq;factor=min(2.,1+(factor-1)*1.5);row['accepted']=True
  else:factor=1+(factor-1)*.4;row['accepted']=False
  trace.append(row);np.save(out/'latest_q.npy',q);(out/'trace.json').write_text(json.dumps(trace,indent=2));print('CONTACT_MARGIN_HOMOTOPY',row,flush=True)
  if factor<1.001 or min(vv)>.00095:break
 np.save(out/'endpoint_q.npy',q);audit(source,out/'endpoint_q.npy',out/'exact_endpoint_g15',10**15);report(out/'exact_endpoint_g15');s=json.loads((out/'exact_endpoint_g15/summary.json').read_text());print('MARGIN_HOMOTOPY_EXACT',{k:s[k]for k in ['V','E','F','counts','weak','goal_met']},flush=True)

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('source');p.add_argument('out');p.add_argument('--steps',type=int,default=45);a=p.parse_args();run(a.source,a.out,a.steps)
