"""Put the exact two-plane C182 body in a full radial-incidence continuation chart.
The pose change is only a similarity; rational chart freezing creates the stated new body."""
import json,numpy as np,radial,sys
from fractions import Fraction as F
from pathlib import Path
sys.set_int_max_str_digits(0)
if __name__=='__main__':
 A=json.load(open('audit_plane6/A.json'));P=np.array([[float(F(x)) for x in p] for p in A['raw_vertices']]);g=np.array([float(F(x)) for x in A['raw_centroid']]);q=np.array([[float(F(v,h)) for v in n] for n,h in zip(A['normals'],A['offsets'])]);r=P-g;root=int(np.argmax(np.linalg.norm(r,axis=1)));z=r[root]/np.linalg.norm(r[root]);x=np.eye(3)[np.argmin(abs(z))];x-=z*(x@z);x/=np.linalg.norm(x);y=np.cross(z,x);B=np.stack((x,y,z))/np.linalg.norm(r[root]);N=(q/(1-q@g)[:,None])@np.linalg.inv(B);PP=r@B.T;stable=int(np.argmax(np.linalg.norm(N,axis=1)));perm=[root]+[i for i in range(len(P)) if i!=root];priority=list(range(len(q)))+[1000+i for i in perm];G=radial.make(PP,N,A['faces'],root,10**12,priority);G['priority']=priority;G['parent_labels']=perm;G['stable_root']=stable;G['parent_name']='TWO_PLANE_CHECKPOINT6_C182';Path('SMALL182.json').write_text(json.dumps(G,sort_keys=True,separators=(',',':')));H,Q=radial.reconstruct(G);print('SMALL182',root,stable,'free',sum(3-len(r[1]) for r in G['plan']),'bits',max(abs(x).bit_length() for h in H['H'] for x in h),flush=True)
