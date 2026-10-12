"""Finite physical material caps over the unwanted S facet of an exact211 body.
No reference-centre substitution: all nominations use new own-volume centroids.
<=84 inputs, with exact numerical110 nominations preserved immediately.
"""
import argparse,json,time
from pathlib import Path
import numpy as np
from gmpy2 import mpq
from vertex_geometry import geometry
from support_geometry import escape
from persistence_birth import evaluate
from capacity_polish import run as repair

def run(source,out):
 out=Path(out);out.mkdir(parents=True,exist_ok=False);d=Path(source);a=json.loads((d/'audit.json').read_text());b=json.loads((d/'exact_bars.json').read_text());f=b['Q'][0]['peak'];X=np.array([[float(mpq(v)) for v in r] for r in a['raw_vertices']]);g=np.array([float(mpq(v)) for v in a['raw_centroid']]);X-=g;n=np.array([float(mpq(v)) for v in a['normals'][f]]);h=float(mpq(a['offsets'][f]))-n@g;foot=n*h/(n@n);unit=n/np.linalg.norm(n);height=np.linalg.norm(foot);face=a['faces'][f];rng=np.random.default_rng(517263);rows=[];selected=[];start=time.time();np.save(out/'parent.npy',X);(out/'source.json').write_text(json.dumps(dict(exact_parent=str(d),dying_stable_face=f,vertices=face,foot=foot.tolist(),normal=unit.tolist()),indent=2))
 locations=[foot]+[(1-t)*foot+t*X[i] for t in [.25,.6,.9] for i in face]
 for index,c in enumerate(locations):
  for ep in [.0001,.001,.005,.02,.05,.1,.2,.4,.8,1.5]:
   Y=np.vstack((X,c+ep*height*unit));assert len(Y)<=84;g=geometry(Y,False);S=int(np.sum(escape(g['H'])[0]<0));U=int(np.sum(escape(g['Z'])[0]<0));info=evaluate(Y)[2];row=dict(location=index,epsilon=ep,S=S,U=U,V=len(g['vertices']),P=info['Pmax'],Q=info['Qmax'],loss=info['loss']);rows.append(row);dest=out/f'l{index}_e{ep:g}';dest.mkdir();np.save(dest/'input.npy',Y);(dest/'nomination.json').write_text(json.dumps(row,indent=2))
   if S==U==1:np.save(dest/'potential.npy',Y);print('CAP_POTENTIAL_OWN110_NEEDS_EXACT',dest,row,flush=True)
   selected.append((info['loss'],dest,S,U))
 (out/'screen.json').write_text(json.dumps(rows,indent=2));selected.sort(key=lambda x:x[0]);print('CAP_SCREEN_DONE',len(rows),'best',rows[np.argmin([r['loss'] for r in rows])],flush=True)
 for _,dest,S,U in selected[:20]:
  repair(dest/'input.npy',dest/'capacity110',1,1,400,1e-6)
 print('FINITE_STABLE_CAPS_DONE',time.time()-start,flush=True)
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('input');p.add_argument('out');a=p.parse_args();run(a.input,a.out)
