from pathlib import Path
import sys,json,hashlib
from fractions import Fraction
import numpy as np
from geometry import hull_from_supports,mass,escape
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'sources/full76/decoded/methods/parent'))
import check_B
name=sys.argv[1];Y=np.load(name);digits=int(sys.argv[2]) if len(sys.argv)>2 else 10
D=10**digits;H=np.c_[np.rint(Y*D).astype(np.int64),np.full(len(Y),D,dtype=np.int64)].tolist()
folder=Path(name).parent/f'{Path(name).stem}_exact_g{digits}';folder.mkdir(exist_ok=True)
(folder/'H.json').write_text(json.dumps({'H':H},sort_keys=True,separators=(',',':')))
rep=check_B.run({'H':H});data=json.dumps(rep,sort_keys=True,separators=(',',':')).encode();(folder/'audit.json').write_bytes(data)
X=np.array([[float(Fraction(x)) for x in row] for row in rep['raw_vertices']]);c=np.array([float(Fraction(x)) for x in rep['raw_centroid']]);Z=X-c
u,policy=escape(Z);r=np.linalg.norm(Z,axis=1)
print('EXACT',*[rep[k] for k in ('V','E','F','counts','weak')],'sha',hashlib.sha256(data).hexdigest(),flush=True)
print('U',[(i,float(r[i]),int(policy[i]),float(u[i]),float(np.linalg.norm(Z[i]-Z[policy[i]]))) for i in rep['unstable_vertices']])
print('S',rep['stable_face_ids'],'H',rep['saddle_edges'])
print('H radii',[(e,float(np.linalg.norm(Z[e[0]]-np.clip(np.dot(Z[e[0]],Z[e[1]]-Z[e[0]])/np.dot(Z[e[1]]-Z[e[0]],Z[e[1]]-Z[e[0]]),-1,0)*(Z[e[1]]-Z[e[0]])))) for e in []])
for i,j in rep['saddle_edges']:
 d=Z[j]-Z[i];t=-np.dot(Z[i],d)/np.dot(d,d);h=Z[i]+t*d;print('saddle',i,j,'radius',float(np.linalg.norm(h)),'t',float(t))
