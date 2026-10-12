"""Move clipped bodies into a free <=84-vertex family by literal deletion.
Any infinitesimal-looking displacement is an explicit saved physical change;
no nearly coplanar merger or integration triangulation is counted as a facet.
"""
import argparse,json,time
from pathlib import Path
from fractions import Fraction
import numpy as np
from vertex_geometry import geometry
from persistence_birth import evaluate
from free_vertex_consolidate import run as consolidate

def run(repairs,out,seed):
 repairs=Path(repairs);out=Path(out);out.mkdir(exist_ok=False,parents=True);records=[];start=time.time()
 for k,label in enumerate(['Q1e-07','Q1e-05','Q0.001','Q0.01','Q0.1']):
  d=out/label;d.mkdir();source=repairs/label/'exact_cap_g12/audit.json';a=json.loads(source.read_text());X=np.array([[float(Fraction(v))for v in row]for row in a['raw_vertices']]);g=np.array([float(Fraction(v))for v in a['raw_centroid']]);X-=g;X/=np.max(np.linalg.norm(X,axis=1));rng=np.random.default_rng(seed+k);noise=rng.normal(size=X.shape)*1e-10;X+=noise;np.save(d/'initial.npy',X);np.save(d/'literal_noise.npy',noise);retired=[]
  while len(X)>84:
   best=np.inf;chosen=None
   for i in range(len(X)):
    Y=np.delete(X,i,axis=0);value,_,info=evaluate(Y,.003)
    if value<best:best=value;chosen=(i,Y,info)
   i,X,inf=chosen;retired.append(dict(index_in_current_array=i,loss=best,P=inf['Pmax'],Q=inf['Qmax']));active=geometry(X,False)['vertices'];retired[-1]['additional_interior_retirements']=sorted(set(range(len(X)))-set(map(int,active)));X=X[active]
  np.save(d/'free_input.npy',X);(d/'definition.json').write_text(json.dumps(dict(source=str(source.resolve()),noise_seed=seed+k,noise_std=1e-10,retirements=retired,input_count=len(X),scope='literal new physical convex hull; source contact complex discarded, both complexity bounds guaranteed by84points'),indent=2));consolidate(d/'free_input.npy',d/'consolidate',5000,'121');row=dict(label=label,input_count=len(X),stages=json.loads((d/'consolidate/stages.json').read_text()),seconds=time.time()-start);records.append(row);(out/'trials.json').write_text(json.dumps(records,indent=2));print('CAP_FREE_RETIREMENT',row,flush=True)

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('repairs');p.add_argument('out');p.add_argument('--seed',type=int,default=79600);a=p.parse_args();run(a.repairs,a.out,a.seed)
