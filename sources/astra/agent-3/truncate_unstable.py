"""Oblique physical removal of the unique U corner to detach stable carriers.
At most85 literal input points after named cap-point deletion; thus C<=498.
The explicitly recorded tiny physical perturbation makes a new nomination;
it is not interpreted as a coplanar exact body. Exact audits remain decisive.
"""
import argparse,json,time
from pathlib import Path
import numpy as np
from vertex_geometry import geometry
from support_geometry import escape
from persistence_birth import evaluate
from polish_211 import run as polish

def run(source,out,trials):
 out=Path(out);out.mkdir(exist_ok=False,parents=True);X=np.load(source);g=geometry(X,False);X=g['Z'][g['vertices']];g=geometry(X,False);root=int(np.argmax(np.sum(X*X,axis=1)));inc=np.flatnonzero(np.any(g['T']==root,axis=1));neighbors=sorted(set(g['T'][inc].ravel())-{root});H=g['H'][inc];H/=np.linalg.norm(H,axis=1)[:,None];S=np.flatnonzero(escape(g['H'])[0]<0);stable_members=set(i for f in S if root in g['T'][f] for i in g['T'][f]);rng=np.random.default_rng(502811);rows=[];best=np.inf
 np.save(out/'parent.npy',X)
 for it in range(trials):
  w=rng.dirichlet(np.full(len(inc),.2));normal=w@H;gaps=(X[root]-X[neighbors])@normal;assert min(gaps)>0;beta=[.0001,.001,.01,.03,.1][it%5];delta=beta*min(gaps);t=delta/gaps;cap=X[root]+t[:,None]*(X[neighbors]-X[root]);u=int(np.argmax(np.sum(cap*cap,axis=1)));detached=neighbors[u] not in stable_members
  if not detached:rows.append(dict(it=it,status='new root remains on old stable carrier',beta=beta));continue
  keep=list(range(len(cap)));drop=[]
  while len(X)-1+len(keep)>85:
   eligible=[i for i in keep if i!=u];j=min(eligible,key=lambda i:np.dot(cap[i],cap[i]));keep.remove(j);drop.append(j)
  Y=np.vstack((np.delete(X,root,axis=0),cap[keep]));noise=rng.normal(size=Y.shape)*1e-9;Y+=noise;info=evaluate(Y)[2];cl=(int(np.sum(escape(geometry(Y,False)['H'])[0]<0)),int(np.sum(escape(geometry(Y,False)['Z'])[0]<0)))
  row=dict(it=it,beta=beta,N=len(Y),S=cl[0],U=cl[1],P=info['Pmax'],Q=info['Qmax'],detached_before_perturbation=detached)
  if info['Pmax']<1e-5 and info['Qmax']<best:
   best=info['Qmax'];d=out/f'candidate{it}';d.mkdir();np.save(d/'input.npy',Y);np.savez(d/'construction.npz',parent=X,normal=normal,weights=w,incident_facets=inc,neighbors=neighbors,root=root,beta=beta,cap_fraction=t,dropped_cap_indices=drop,noise=noise);(d/'nomination.json').write_text(json.dumps(row,indent=2));polish(d/'input.npy',d/'polish',300,1e-6)
   if (d/'polish/success.npy').exists():row['polished']=evaluate(np.load(d/'polish/success.npy'))[2];row['path']=str(d/'polish/success.npy')
  rows.append(row);(out/'trials.json').write_text(json.dumps(rows,indent=2))
  if it%20==0:print('TRUNCATION',row,flush=True)
 print('TRUNCATION_DONE',len(rows),flush=True)
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('input');p.add_argument('out');p.add_argument('--trials',type=int,default=200);a=p.parse_args();run(a.input,a.out,a.trials)
