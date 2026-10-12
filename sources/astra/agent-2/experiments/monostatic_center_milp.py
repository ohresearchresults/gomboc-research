"""Find actual geometric monostatic reference centers of a fixed body via MILP.
This does NOT claim the uniform centroid moved. It nominates a shape-deformation
starting chamber. Vertex and polar edge escape primitives are linear in center.
All numerical solutions are independently recensused; own-centroid audit remains separate.
"""
import sys,json,time,hashlib,numpy as np
from scipy.optimize import milp,Bounds,LinearConstraint
from scipy.sparse import lil_matrix,csr_matrix,vstack
from gmpy2 import mpq
from pathlib import Path
from geometry import angular_scores
ROOT=Path(__file__).resolve().parents[1];sys.set_int_max_str_digits(0)
src=ROOT/sys.argv[1];out=ROOT/sys.argv[2];box=float(sys.argv[3]) if len(sys.argv)>3 else .3;out.mkdir(exist_ok=False,parents=True);r=json.loads(src.read_text());cent=np.array([float(mpq(x)) for x in r['raw_centroid']]);X=np.array([[float(mpq(x)) for x in row] for row in r['raw_vertices']])-cent;Y=np.array([[float(mpq(x,mpq(h))) for x in row] for row,h in zip(r['normals'],r['offsets'])]);Y=Y/(1-Y@cent)[:,None];R=np.linalg.norm(X,axis=1).max();X=X/R;Y=Y*R;V,F=len(X),len(Y);edges=r['edges'];ef={}
for fi,face in enumerate(r['faces']):
 for i,j in zip(face,face[1:]+face[:1]):ef.setdefault(tuple(sorted((i,j))),[]).append(fi)
assert all(len(z)==2 for z in ef.values());arrows=[]
for i,j in edges:
 for a,b in [(i,j),(j,i)]:
  d=X[b]-X[a];arrows.append(dict(kind='U',node=a,other=b,a=-d/np.linalg.norm(d),b=float(X[a]@d/np.linalg.norm(d))))
for i,j in ef.values():
 for f,g in [(i,j),(j,i)]:
  n,m=Y[f],Y[g];a=(n@n)*m-(n@m)*n;b=float(n@m-n@n);norm=np.linalg.norm(a);assert norm>1e-12;arrows.append(dict(kind='S',node=f,other=g,a=a/norm,b=b/norm))
na=len(arrows);N=6+na+V+F;ng=na+V+F+2+6+F;A=lil_matrix((ng,N));lo=np.full(ng,-np.inf);hi=np.full(ng,np.inf);k=0;delta=float(sys.argv[4]) if len(sys.argv)>4 else 1e-6
for i,ar in enumerate(arrows):
 a,b=ar['a'],ar['b'];M=max(0,delta-b+box*abs(a).sum());A[k,:3]=a;A[k,6+i]=-M;lo[k]=delta-b-M;k+=1
for kind,n,rootstart in [('U',V,6+na),('S',F,6+na+V)]:
 for node in range(n):
  for i,ar in enumerate(arrows):
   if ar['kind']==kind and ar['node']==node:A[k,6+i]=1
  A[k,rootstart+node]=1;lo[k]=1;k+=1
 A[k,rootstart:rootstart+n]=1;lo[k]=hi[k]=1;k+=1
for j in range(3):
 A[k,j]=1;A[k,3+j]=-1;hi[k]=0;k+=1;A[k,j]=-1;A[k,3+j]=-1;hi[k]=0;k+=1
for y in Y:A[k,:3]=y;hi[k]=1-1e-4;k+=1
assert k==ng
cost=np.r_[np.zeros(3),np.ones(3),np.zeros(N-6)];lb=np.r_[np.full(3,-box),np.zeros(N-3)];ub=np.r_[np.full(3,box),np.full(3,box),np.ones(N-6)];start=time.time();opt=milp(cost,integrality=np.r_[np.zeros(6),np.ones(N-6)],bounds=Bounds(lb,ub),constraints=LinearConstraint(csr_matrix(A),lo,hi),options={'time_limit':180,'mip_rel_gap':1e-6,'disp':False});result=dict(source=str(src),source_sha256=hashlib.sha256(src.read_bytes()).hexdigest(),box=box,margin=delta,status=int(opt.status),message=str(opt.message),seconds=time.time()-start)
if opt.x is not None:
 c=opt.x[:3];Q=Y/(1-Y@c)[:,None];Z=X-c;U=angular_scores(Z).max(1);S=angular_scores(Q).max(1);result.update(reference_center_normalized=c.tolist(),source_center_shift=(c*R).tolist(),source_reference_center=(cent+c*R).tolist(),own_centroid_unchanged=cent.tolist(),S=int((S<0).sum()),U=int((U<0).sum()),nonroot_angular_floor=float(min(np.sort(U)[1],np.sort(S)[1])),objective=float(opt.fun),mip_gap=float(opt.mip_gap),rootU=np.flatnonzero(opt.x[6+na:6+na+V]>.5).tolist(),rootS=np.flatnonzero(opt.x[6+na+V:]>.5).tolist());selected=[{key:value.tolist() if isinstance(value,np.ndarray) else value for key,value in ar.items()} for i,ar in enumerate(arrows) if opt.x[6+i]>.5];result['selected_arrows']=selected;np.savez(out/'numerical_chamber.npz',reference_center=c,X=X,Y=Y,solution=opt.x);print('REFERENCE_CENTER_ONLY', {k:v for k,v in result.items() if k!='selected_arrows'},flush=True)
else:print('NO_INCUMBENT',result,flush=True)
(out/'result.json').write_text(json.dumps(result,indent=2)+'\n')
