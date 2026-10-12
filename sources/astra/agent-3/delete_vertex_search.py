"""Finite exact-input vertex deletions with actual homogeneous mass re-evaluation.
Exhaustive singles/pairs plus seeded larger subsets; no tolerance acceptance.
"""
import argparse,json,time
from pathlib import Path
from itertools import combinations
import numpy as np
from vertex_geometry import geometry
from support_geometry import escape
from persistence_birth import evaluate
from polish_211 import run as polish

def run(source,out,random_trials):
 out=Path(out);out.mkdir(parents=True,exist_ok=False);g=geometry(np.load(source),False);X=g['Z'][g['vertices']];assert len(X)<=84;np.save(out/'parent.npy',X);root=int(np.argmax(np.sum(X*X,axis=1)));indices=[i for i in range(len(X)) if i!=root];rng=np.random.default_rng(849501);hist=[];ranked=[];start=time.time();subsets=list(combinations(indices,1))+list(combinations(indices,2))
 for _ in range(random_trials):subsets.append(tuple(sorted(rng.choice(indices,int(rng.integers(3,10)),replace=False))))
 for it,remove in enumerate(subsets):
  Y=np.delete(X,remove,axis=0);gg=geometry(Y,False);S=int(np.sum(escape(gg['H'])[0]<0));U=int(np.sum(escape(gg['Z'])[0]<0));row=dict(it=it,removed=list(map(int,remove)),S=S,U=U,V=len(gg['vertices']))
  if S+U<=10:
   info=evaluate(Y)[2];row.update(P=info['Pmax'],Q=info['Qmax'],loss=info['loss']);ranked.append((info['Pmax']*8+info['Qmax'],row))
  if S==U==1:
   d=out/f'potential{it}';d.mkdir();np.save(d/'vertices.npy',Y);(d/'definition.json').write_text(json.dumps(row,indent=2));print('DELETE_POTENTIAL_OWN110_REQUIRES_EXACT',d,row,flush=True)
  hist.append(row)
  if it%1000==0:print('DELETE_SCREEN',it,'best count',min(h['S']+h['U'] for h in hist),flush=True)
 (out/'screen.json').write_text(json.dumps(hist,indent=2));ranked.sort(key=lambda x:x[0]);print('DELETE_SCREEN_DONE',len(hist),'low_count_candidates',len(ranked),flush=True)
 for _,row in ranked[:30]:
  d=out/f'candidate{row["it"]}';d.mkdir();Y=np.delete(X,row['removed'],axis=0);np.save(d/'input.npy',Y);(d/'definition.json').write_text(json.dumps(row,indent=2));polish(d/'input.npy',d/'repair211',300,1e-6)
 print('DELETE_SEARCH_DONE',time.time()-start,flush=True)
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('input');p.add_argument('out');p.add_argument('--random-trials',type=int,default=2000);a=p.parse_args();run(a.input,a.out,a.random_trials)
