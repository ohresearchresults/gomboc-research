from pathlib import Path
import sys,json,numpy as np
from fractions import Fraction
from support_persistence import ROOT,complex_for,points
from geometry import angular_scores
sys.path.insert(0,str(ROOT/'sources/full76/decoded/methods/parent'));import check_B
base=json.loads((ROOT/'artifacts/kf27d/H_exact.json').read_text())['H'];Y=np.array([r[:3] for r in base])/10000
DS,xm,tr,tm,ym=complex_for(Y);Z,Q=points(Y,DS,tr,tm);scores=angular_scores(Z);r=np.linalg.norm(Z,axis=1);uroots=np.flatnonzero(scores.max(axis=1)<0)
valid=np.ones(len(Z),bool);valid[uroots]=False
# Exact angular/root classification below is independently checked after generation.
directions=Z/r[:,None];selected=[];distance=np.full(len(Z),np.inf)
current=int(np.argmax(np.where(valid,r,-np.inf)))
for k in range(36):
 selected.append(current);distance=np.minimum(distance,1-directions@directions[current]);distance[~valid]=-np.inf;distance[selected]=-np.inf;current=int(np.argmax(distance))
out=ROOT/'artifacts/kf27d_expanded';out.mkdir(exist_ok=True)
for power in [3,4,5,6]:
 d=10**power;H=[list(row) for row in base]
 for i in selected:
  ids=DS[i];n=[sum(base[j][k] for j in ids)*(d+1) for k in range(3)];H.append(n+[30000*d])
 name=f'F85_caps_g{power}';rep=check_B.run({'H':H});(out/(name+'_H.json')).write_text(json.dumps({'H':H},sort_keys=True,separators=(',',':')));(out/(name+'_audit.json')).write_text(json.dumps(rep,sort_keys=True,separators=(',',':')))
 print(name,*[rep[k] for k in ('V','E','F','counts','weak')],flush=True)
 np.save(out/(name+'.npy'),np.array([[float(Fraction(x,row[3])) for x in row[:3]] for row in H]))
(out/'construction.json').write_text(json.dumps({'base':'../kf27d/H_exact.json','selected_base_dual_triangles':[DS[i].tolist() for i in selected],'new_support_formula':'sum(base triple normals) * (10^power+1) / (3*10^power), original offsets normalized to1'},indent=2)+'\n')
