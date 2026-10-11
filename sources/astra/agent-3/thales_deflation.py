"""Finite whole-basin radial deflation followed by actual-centroid closure.
Starts from an own-S1 body and changes the entire positive-escape forest.
The initial deflation guarantees U1 only at the old reference0, not own mass.
"""
import json,time,argparse
from pathlib import Path
import numpy as np
from vertex_geometry import geometry
from support_geometry import escape
from polish_121 import forest,persistent_root
from thales_chart import Chart,Search
from polish_211 import run as polish
from persistence_birth import evaluate

def deflate(X,root,margin):
 par=forest(X,[root]);Y=np.zeros_like(X);Y[root]=X[root];done={root};order=[root];rho=np.ones(len(X))
 while len(done)<len(X):
  todo=[i for i in range(len(X)) if i not in done and par[i] in done];assert todo,'forest cycle'
  for i in todo:
   u=X[i];p=int(par[i]);dot=u@X[p];assert dot>0,(i,p,dot)
   rho[i]=min((u@u)/dot,1-margin);Y[i]=rho[i]*(u@Y[p])/(u@u)*u;assert Y[i]@u>0;done.add(i);order.append(i)
 assert np.sum(escape(Y)[0]<0)==1
 return Y,dict(root=int(root),parent=par.tolist(),rho=rho.tolist(),order=order,reference_guarantee='U1 at zero only; actual centroid independently constrained in search')

def run(out):
 out=Path(out);out.mkdir(parents=True,exist_ok=False);sources=['artifacts/cap_flow_t0.25/latest.npy','artifacts/projected_pflow1/exact_g9/hull_float.npy','artifacts/j84_seed.npy'];rows=[]
 for si,source in enumerate(sources):
  g=geometry(np.load(source),False);X=g['Z'][g['vertices']];roots=persistent_root(geometry(X,False))
  for ri,root in enumerate(roots):
   for ei,eta in enumerate([.02,.002]):
    d=out/f's{si}_r{ri}_eta{eta:g}';d.mkdir();Y,meta=deflate(X,root,1e-6);Y/=np.max(np.linalg.norm(Y,axis=1));meta['source']=source;meta['initial_actual_centroid']=geometry(Y,False)['g'].tolist();np.save(d/'deflated.npy',Y);(d/'construction.json').write_text(json.dumps(meta,indent=2))
    c=Chart(Y);s=Search(c,d/'search',eta);s.run(4000)
    if (s.out/'best.npy').exists():
     polish(s.out/'best.npy',d/'polish',400,1e-6);p=d/'polish/success.npy'
     if p.exists():row=dict(source=source,root=int(root),eta=eta,result='strict211 numerical',path=str(p),persistence=evaluate(np.load(p))[2])
     else:row=dict(source=source,root=int(root),eta=eta,result='retraction failed')
    else:row=dict(source=source,root=int(root),eta=eta,result='no centroid-feasible endpoint')
    rows.append(row);(out/'trials.json').write_text(json.dumps(rows,indent=2));print('DEFLATION_TRIAL',row,flush=True)
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('out');a=p.parse_args();run(a.out)
