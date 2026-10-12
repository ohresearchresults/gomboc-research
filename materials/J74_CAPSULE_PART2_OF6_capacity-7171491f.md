# material-7171491fba84

AI research material

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

"""Distributed exact finite moment correction, deterministic float LP scout.
The LP is not a proof. Each rational candidate must pass all exact support,
volume/moment, actual hull and complete equilibrium checks in core.py.
"""
import argparse,itertools,json,sys
from pathlib import Path
import numpy as np
from scipy.optimize import linprog
import core as c

def geometry_matrix(X,faces,modes):
 X=np.asarray(X,dtype=float);normals=[];heights=[];pairs=[];values=[]
 for fi,f in enumerate(faces):
  a,b,z=X[f[:3]];n=np.cross(b-a,z-a);h=n@a;length=np.linalg.norm(n)
  normals.append(n);heights.append(h)
  for j in range(len(X)):
   if j not in f:pairs.append((fi,j,length));values.append((h-n@X[j])/length)
 J=np.zeros((len(pairs),len(modes)))
 for k,(i,dd) in enumerate(modes):
  dd=np.array(dd,dtype=float);dn=[];dh=[]
  for fi,f in enumerate(faces):
   a,b,z=X[f[:3]];da=dd if f[0]==i else np.zeros(3);db=dd if f[1]==i else np.zeros(3);dz=dd if f[2]==i else np.zeros(3)
   nn=np.cross(db-da,z-a)+np.cross(b-a,dz-da);dn.append(nn);dh.append(nn@a+normals[fi]@da)
  for r,(fi,j,length) in enumerate(pairs):J[r,k]=(dh[fi]-dn[fi]@X[j]-(normals[fi]@dd if j==i else 0))/length
 return J,np.array(values)

def modes_for(X,faces,verts):
 modes=[];images=[]
 for i in verts:
  basis,im=c.star(X,faces,i)
  for b,a in zip(basis,im):
   scale=max(abs(t) for t in b);modes.append((i,c.mul(b,1/scale)));images.append(c.mul(a,1/scale))
 return modes,images

def exact_endpoint(X,faces,modes,images,approx,target):
 C=np.array(images,dtype=float).T
 pivot=max(itertools.combinations(range(len(modes)),3),key=lambda s:abs(np.linalg.det(C[:,s])))
 coeff=[c.F(round(float(t)*10**15),10**15) for t in approx]
 residual=target
 for k,a in enumerate(coeff):
  if k not in pivot:residual=c.sub(residual,c.mul(images[k],a))
 sol=c.solve_columns([images[k] for k in pivot],residual)
 for k,a in zip(pivot,sol):coeff[k]=a
 Y=list(X)
 for a,(i,d) in zip(coeff,modes):Y[i]=c.add(Y[i],c.mul(d,a))
 return Y,coeff,pivot

def solve_set(X,faces,modes,images,target,geom=True,maximize=False):
 nc=len(modes);C=np.array(images,dtype=float).T;target=np.array(target,dtype=float)
 rows=[];rhs=[]
 if geom:
  J,g=geometry_matrix(X,faces,modes)
  rows.extend(np.column_stack([-J,np.zeros(len(g))]));rhs.extend(0.45*g)
 if maximize:
  eq=np.column_stack([C,-target]);beq=np.zeros(3)
  # Bound each coordinate displacement by 0.02, but allow lambda to grow.
  for i in sorted({i for i,d in modes}):
   for j in range(3):
    r=np.array([float(d[j]) if k==i else 0. for k,d in modes]+[0.])
    rows.extend([r,-r]);rhs.extend([0.02,0.02])
  bounds=[(None,None)]*nc+[(0,None)]
 else:
  eq=np.column_stack([C,np.zeros(3)]);beq=target
  for i in sorted({i for i,d in modes}):
   for j in range(3):
    r=np.array([float(d[j]) if k==i else 0. for k,d in modes]+[-1.])
    rows.extend([r,np.r_[-r[:-1],-1.]]);rhs.extend([0.,0.])
  bounds=[(None,None)]*nc+[(0,None)]
 scale=np.max(np.abs(eq),axis=1);eq=eq/scale[:,None];beq=beq/scale
 cost=np.r_[np.zeros(nc),-1. if maximize else 1.]
 return linprog(cost,A_ub=np.asarray(rows),b_ub=np.asarray(rhs),A_eq=eq,b_eq=beq,bounds=bounds,method='highs',options={'primal_feasibility_tolerance':1e-9,'dual_feasibility_tolerance':1e-9})

def main(count,out):
 out=Path(out);out.mkdir(exist_ok=True)
 K=c.convert(json.loads(Path('postcontact_input.json').read_text()));X=K['points'];faces=K['faces'];base=c.mechanics(K);V,M=c.mass(X,faces);target=c.mul(M,-1)
 # Original primary and U roots protected; other fixed-rim triangle stars may act.
 protected={6,13,14,16,22,24,62};eligible=[i for i,m in enumerate(K['material']) if m not in protected and all(len(f)==3 for f in faces if i in f)]
 neighbors={i:{j for f in faces if i in f for j in f}-{i} for i in eligible};rng=np.random.default_rng(74057)
 candidates=[];sets=set()
 for trial in range(count):
  order=list(eligible);rng.shuffle(order)
  if trial==0:
   score={i:sum(np.linalg.norm(np.array(a,dtype=float))/np.linalg.norm(np.array(b,dtype=float)) for b,a in zip(*c.star(X,faces,i))) for i in eligible};order.sort(key=lambda i:-score[i])
  verts=[]
  for i in order:
   if not any(j in neighbors[i] for j in verts):verts.append(i)
  verts=sorted(verts)
  if tuple(verts) in sets:continue
  sets.add(tuple(verts));assert all(sum(i in f for i in verts)<=1 for f in faces)
  modes,images=modes_for(X,faces,verts);lp=solve_set(X,faces,modes,images,target,geom=False)
  if lp.success:candidates.append((float(lp.fun),verts,lp.x[:-1]))
 candidates.sort(key=lambda r:r[0]);print('SCOUT_SETS',len(sets),'feasible',len(candidates),'best_unconstrained',candidates[0][0],flush=True)
 accepted=[]
 for rho,verts,unused in candidates[:12]:
  modes,images=modes_for(X,faces,verts);lp=solve_set(X,faces,modes,images,target,geom=True)
  if not lp.success:continue
  Y,coeff,pivot=exact_endpoint(X,faces,modes,images,lp.x[:-1],target)
  assert c.mass(Y,faces)==(V,c.ZERO)
  valid=c.valid_complex(Y,faces)
  if not valid:
   print('RATIONAL_GEOMETRY_REJECT',verts,float(lp.fun),flush=True);continue
  H=c.hull(Y);R=c.mechanics(H);assert H['material']==list(range(len(X))) and R['volume']==V and R['centroid']==c.ZERO
  disp=max(abs(float(y-x)) for p,q in zip(X,Y) for x,y in zip(p,q));print('EXACT_DISTRIBUTED',float(lp.fun),disp,R['strict'],[K['material'][i] for i in verts],flush=True)
  if R['weak']==R['zeros']==[0,0,0]:accepted.append((disp,verts,Y,coeff,pivot,R,modes,images))
  if len(accepted)>=1:break
 assert accepted,'No exact verified distributed correction found'
 disp,verts,Y,coeff,pivot,R,modes,images=min(accepted,key=lambda r:r[0])
 receipt=dict(controller_material=[K['material'][i] for i in verts],controller_indices=verts,modes=modes,images=images,coefficients=coeff,pivot=pivot,input_mass=base,output_report=R,max_coordinate_displacement=disp,LP_status='floating nomination; full rational endpoint certified',original_material=K['material'])
 c.dump(out/'distributed_body.json',dict(points=Y,density=1));c.dump(out/'distributed_receipt.json',receipt)
 # Explore finite directional reservoir size with all guards then certify selected factors.
 cap=None
 if '--capacity' in sys.argv:cap=solve_set(X,faces,modes,images,target,geom=True,maximize=True)
 if cap is not None and cap.success:
  print('FLOAT_CAPACITY_FACTOR',float(cap.x[-1]),flush=True)
  cert=[]
  for lam in [c.F(1),c.F(2),c.F(4),c.F(8),c.F(16),c.F(32),c.F(64),c.F(128),c.F(256)]:
   if float(lam)>cap.x[-1]:break
   lp=solve_set(X,faces,modes,images,c.mul(target,lam),geom=True)
   if not lp.success:break
   Z,cc,pp=exact_endpoint(X,faces,modes,images,lp.x[:-1],c.mul(target,lam))
   assert c.mass(Z,faces)==(V,c.mul(M,1-lam))
   if not c.valid_complex(Z,faces):print('CAP_GEOMETRY_FAIL',lam,flush=True);break
   Q=c.hull(Z);rr=c.mechanics(Q);print('EXACT_CAPACITY',lam,rr['strict'],flush=True)
   cert.append(dict(factor=lam,coefficients=cc,pivot=pp,report=rr))
  c.dump(out/'directional_capacity.json',dict(modes=modes,images=images,certified_endpoints=cert,float_nomination_factor=float(cap.x[-1])))
 print('J74_DISTRIBUTED_EXACT_MASS_CORRECTION_PASS_NOT_110',flush=True)

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--sets',type=int,default=80);p.add_argument('--out',default='capacity_output');p.add_argument('--capacity',action='store_true');a=p.parse_args();main(a.sets,a.out)
