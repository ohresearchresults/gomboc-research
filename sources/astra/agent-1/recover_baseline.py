import sys,json,pathlib,time,hashlib
from fractions import Fraction
root=pathlib.Path('sources/full76').resolve()
sys.path[:0]=[str(root/'methods'),str(root/'methods/parent')]
sys.set_int_max_str_digits(0)
import G_FREE_CODEC,RECONSTRUCT
p=pathlib.Path('artifacts/baseline');p.mkdir(parents=True,exist_ok=True)
G=G_FREE_CODEC.decode(json.loads((root/'inputs/C622_ROUTED.json').read_text()))
(p/'generator.json').write_text(json.dumps(G,sort_keys=True,separators=(',',':')))
raw=RECONSTRUCT.recover(G)
(p/'raw.json').write_text(json.dumps(raw,sort_keys=True,separators=(',',':')))
print('RAW',hashlib.sha256((p/'raw.json').read_bytes()).hexdigest(),flush=True)
import numpy as np
from scipy.spatial import ConvexHull
H=np.array([[float(Fraction(x,r[3])) for x in r[:3]] for r in raw['H']]);
pol=ConvexHull(H)
V=[]; groups=[]
for s in pol.simplices:
 A=H[s];v=np.linalg.solve(A,np.ones(3))
 if len(V) and min(np.linalg.norm(v-vv) for vv in V)<1e-7:continue
 V.append(v);groups.append(np.flatnonzero(abs(H@v-1)<1e-8).tolist())
V=np.array(V)
np.savez(p/'float.npz',X=V,H=H)
(p/'groups-float.json').write_text(json.dumps(groups))
print('numeric support/vertex sizes',len(H),len(V),flush=True)
print('extents',np.min(V,axis=0),np.max(V,axis=0),flush=True)
