"""Finite exact-control rounding and explicitly numerical own-mass screening."""
import sys,json,copy,hashlib
from pathlib import Path
from fractions import Fraction as F
import numpy as np
sys.set_int_max_str_digits(0)
source=Path(sys.argv[1]);proof=Path(sys.argv[2]);out=Path(sys.argv[3]);out.mkdir(parents=True,exist_ok=False)
sys.path.insert(0,str(source/'methods/parent'));import RECONSTRUCT
B=lambda v:json.dumps(v,sort_keys=True,separators=(',',':')).encode()
GB=(proof/'C622_ROUTED/GENERATOR.json').read_bytes();assert hashlib.sha256(GB).hexdigest()=='3cbd90d799189108f26b941800c8fa79a6f1c5abb17b2db614f0e54f57fffee7'
G=json.loads(GB);R=json.loads((proof/'C622_ROUTED/A.json').read_text());faces=R['faces'];edges=R['edges'];owners=[[f for f,cy in enumerate(faces) if i in cy] for i in range(R['V'])]
trip=[]
raw=RECONSTRUCT.recover(G);q=np.array([[float(F(v,row[-1])) for v in row[:3]] for row in raw['H']])
from itertools import combinations
for own in owners:trip.append(max(combinations(own,3),key=lambda t:abs(np.linalg.det(q[list(t)]))))
tris=np.array([(cy[0],cy[j],cy[j+1]) for cy in faces for j in range(1,len(cy)-1)])
mask=np.ones((137,R['V']),bool)
for i,own in enumerate(owners):mask[own,i]=False
for D in [10**k for k in range(11,4,-1)]+[2**k for k in [34,31,28,25,22,19]]:
 H=copy.deepcopy(G);H['grid']=D;H['controls']=[[round(F(v*D,G['grid'])) for v in row] for row in G['controls']]
 p=out/str(D);p.mkdir();(p/'GENERATOR.json').write_bytes(B(H));r=RECONSTRUCT.recover(H);(p/'raw.json').write_bytes(B(r))
 q=np.array([[float(F(v,row[-1])) for v in row[:3]] for row in r['H']]);X=np.array([np.linalg.solve(q[list(t)],np.ones(3)) for t in trip]);slack=1-q@X.T
 det=np.einsum('ij,ij->i',X[tris[:,0]],np.cross(X[tris[:,1]],X[tris[:,2]]));vol=det.sum()/6;g=(det[:,None]*(X[tris].sum(axis=1))).sum(axis=0)/(24*vol);Y=X-g
 vs=Y@Y.T-(Y*Y).sum(axis=1)[:,None];np.fill_diagonal(vs,-np.inf);U=np.where(vs.max(axis=1)<0)[0].tolist()
 S=[];Hh=[];edgeguards=[]
 for f,cy in enumerate(faces):
  vals=[np.dot(q[f],np.cross(Y[i],X[j]-X[i])) for i,j in zip(cy,cy[1:]+cy[:1])]
  if min(vals)>0:S.append(f)
 for i,j in edges:
  e=X[j]-X[i];ee=e@e;ze=Y[i]@e;z=Y[i]*ee-ze*e;fs=sorted(set(owners[i])&set(owners[j]));assert len(fs)==2
  n,m=q[fs];nn=n@n;mm=m@m;nm=n@m;v=[-ze,ee+ze,z@(mm*n-nm*m),z@(nn*m-nm*n)]
  if min(v)>0:Hh.append([i,j])
  edgeguards.append(min(abs(t) for t in v))
 row=dict(grid=D,numerical_only=True,counts=[len(S),len(U),len(Hh)],stable=S,unstable=U,saddles=Hh,nonowner_slack_min=float(slack[mask].min()),owner_error_max=float(abs(slack[~mask]).max()),triangle_det_min=float(det.min()),volume=float(vol),centroid=g.tolist(),H_max_bits=max(abs(v).bit_length() for a in r['H'] for v in a))
 (p/'NUMERICAL_SCREEN.json').write_bytes(B(row));print(json.dumps(row),flush=True)
print('C622_FINITE_GRID_NUMERICAL_SCREEN_DONE',flush=True)
