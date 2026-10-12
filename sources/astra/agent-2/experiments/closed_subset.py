"""Select actual baseline vertices using a one-sided reference escape guide.
The graph condition is NOT an own-centroid equilibrium certificate.
"""
from pathlib import Path
import json,sys,numpy as np
from scipy.optimize import milp,Bounds,LinearConstraint
from scipy.sparse import lil_matrix
from fractions import Fraction
from scipy.spatial import ConvexHull
from geometry import angular_scores,mass,escape
ROOT=Path(__file__).resolve().parents[1];sys.set_int_max_str_digits(0)
r=json.loads((ROOT/'artifacts/baseline/B_exact.json').read_text());g=np.array([float(Fraction(v)) for v in r['raw_centroid']]);X=np.array([[float(Fraction(v)) for v in row] for row in r['raw_vertices']])-g
s=r['stable_face_ids'][0];u=r['unstable_vertices'][0];normal=np.array(r['normals'][s],float);axis=-normal/np.linalg.norm(normal);z=X@axis;top=int(np.argmax(z));score=angular_scores(X);allowed=score>1e-11
forced=set(r['faces'][s])|{u,top};n=len(X);A=lil_matrix((n-1,n));row=0
for i in range(n):
 if i==u:continue
 A[row,i]=1;A[row,np.flatnonzero(allowed[i])]=-1;row+=1
lo=np.zeros(n);lo[list(forced)]=1
res=milp(np.ones(n),integrality=np.ones(n),bounds=Bounds(lo,np.ones(n)),constraints=LinearConstraint(A.tocsr(),-np.inf,np.zeros(n-1)),options={'time_limit':30,'mip_rel_gap':0})
assert res.x is not None;keep=np.flatnonzero(res.x>.5);assert all(i==u or any(allowed[i,j] for j in keep) for i in keep)
out=ROOT/'artifacts/closed_subset';out.mkdir(exist_ok=True)
report={'status':res.message,'selected_count':len(keep),'selected':keep.tolist(),'forced':sorted(forced),'root':u,'stable_face':s,'top_vertex':top,'reference_center_raw':r['raw_centroid'],'caution':'Selected-point outward escape is a reference-center guide only; homogeneous mass is separately computed.'}
(out/'minimum_closure.json').write_text(json.dumps(report,indent=2)+'\n');np.save(out/'X_centered.npy',X);print('CLOSURE',len(keep),'middle',len(keep)-len(r['faces'][s])-1,res.message,flush=True)
P=X[keep];h=ConvexHull(P);tri=h.simplices.copy();norm=np.cross(P[tri[:,1]]-P[tri[:,0]],P[tri[:,2]]-P[tri[:,0]]);flip=np.einsum('ij,ij->i',norm,h.equations[:,:3])<0;tri[flip]=tri[flip][:,[0,2,1]]
vol,c=mass(P,tri);Z=P-c;qn=h.equations[:,:3];qh=-h.equations[:,3]-qn@c;Q=qn/qh[:,None]
unique=[]
for q in Q:
 if not unique or np.min(np.linalg.norm(np.array(unique)-q,axis=1))>1e-8:unique.append(q)
Q=np.array(unique);ue,_=escape(Z);se,_=escape(Q)
num={'V':len(h.vertices),'F':len(Q),'E':len(h.vertices)+len(Q)-2,'S':int((se<0).sum()),'U':int((ue<0).sum()),'centroid_displacement':c.tolist(),'volume':vol}
(out/'numerical_own.json').write_text(json.dumps(num,indent=2)+'\n');print('OWN_NUMERICAL',num,flush=True)
