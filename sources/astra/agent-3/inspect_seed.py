import json,sys,numpy as np
from fractions import Fraction as F
sys.set_int_max_str_digits(0)
a=json.load(open('artifacts/c622/audit.json'));r=json.load(open('artifacts/c622/raw.json'))
X=np.array([[float(F(x)) for x in row] for row in a['raw_vertices']]);c=np.array([float(F(x)) for x in a['raw_centroid']]);Q=np.array([[float(F(x,row[3])) for x in row[:3]] for row in r['H']]);H=Q/(1-Q@c)[:,None];Z=X-c
np.savez('artifacts/c622/seed.npz',X=Z,Q=H,centroid=c)
for label,A in [('primal',Z),('dual',H)]:
 E=A[None]-A[:,None]; D=np.linalg.norm(A,axis=1)[:,None]*np.linalg.norm(E,axis=2)
 esc=np.einsum('ik,ijk->ij',A,E)/np.maximum(D,1e-100);np.fill_diagonal(esc,-np.inf)
 e=esc.max(axis=1);js=esc.argmax(axis=1)
 print(label,'ranges',A.min(axis=0),A.max(axis=0),'radii',np.linalg.norm(A,axis=1).min(),np.linalg.norm(A,axis=1).max())
 print('roots',np.where(e<0)[0],'escape quantiles',np.quantile(e,[0,.01,.05,.25,.5,.75,.95,1]),'lowest',[(int(i),int(js[i]),float(e[i])) for i in np.argsort(e)[:12]])
 print('rms',np.mean(A*A,axis=0))
print('volume',float(F(a['ordinary_volume'])),'centroid',c,'facet degrees',np.unique([len(x) for x in a['faces']],return_counts=True))
