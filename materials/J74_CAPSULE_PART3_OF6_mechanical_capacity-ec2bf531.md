# material-ec2bf5318f29

AI research material

---

"""A fixed-witness LP for no-new-S/U finite moment capacity.
LP linearization nominates only. Retained endpoints are certified by core.
"""
import json,itertools,sys
from pathlib import Path
import numpy as np
from scipy.optimize import linprog
import core as c
from capacity import modes_for,geometry_matrix,exact_endpoint

def mechanical_matrix(K,modes,images):
 X=np.array(K['points'],dtype=float);V,M=c.mass(K['points'],K['faces']);volume=float(V);x=X-np.array(c.mul(M,1/V),dtype=float);faces=K['faces'];der=[]
 for (i,b),im in zip(modes,images):
  dx=np.tile(-np.array(im,dtype=float)/volume,(len(x),1));dx[i]+=np.array(b,dtype=float);der.append(dx)
 G=[];rows=[];labels=[]
 def choose(vals,jac,label):
  keep=range(len(vals)) if min(vals)>0 else [int(np.argmin(vals))]
  for k in keep:
   sign=1 if vals[k]>0 else -1;G.append(sign*vals[k]);rows.append(sign*jac[k]);labels.append((label,k,sign))
 for fi,f in enumerate(faces):
  a,b,z=x[f[:3]];n=np.cross(b-a,z-a);vals=[];jac=[]
  for i,j in zip(f,f[1:]+f[:1]):
   e=x[j]-x[i];ne=np.cross(n,e);scale=np.linalg.norm(n)*np.linalg.norm(e);vals.append((-ne@x[i])/scale);jj=[]
   for dx in der:
    da,db,dz=dx[f[:3]];dn=np.cross(db-da,z-a)+np.cross(b-a,dz-da);de=dx[j]-dx[i];jj.append((-(np.cross(dn,e)+np.cross(n,de))@x[i]-ne@dx[i])/scale)
   jac.append(jj)
  choose(np.array(vals),np.array(jac),'S:'+str(fi))
 nb=[set() for q in x]
 for i,j in K['edges']:nb[i].add(j);nb[j].add(i)
 for i in range(len(x)):
  vals=[];jac=[]
  for j in sorted(nb[i]):
   e=x[j]-x[i];scale=np.linalg.norm(x[i])*np.linalg.norm(e);vals.append(-x[i]@e/scale)
   jac.append([(-dx[i]@e-x[i]@(dx[j]-dx[i]))/scale for dx in der])
  choose(np.array(vals),np.array(jac),'U:'+str(i))
 return np.array(rows),np.array(G),labels

def solve(K,modes,images,target,J,g,Jm,gm,maximize=False):
 nc=len(modes);C=np.array(images,dtype=float).T;target=np.array(target,dtype=float)
 constraints=[np.column_stack([-J,np.zeros(len(g))]),np.column_stack([-Jm,np.zeros(len(gm))])];rhs=[0.45*g,0.75*gm]
 for i in sorted({i for i,b in modes}):
  for k in range(3):
   a=np.array([float(b[k]) if j==i else 0 for j,b in modes]);r=np.r_[a,0. if maximize else -1.];s=np.r_[-a,0. if maximize else -1.]
   constraints.append(np.array([r,s]));rhs.append(np.array([0.02,0.02]) if maximize else np.zeros(2))
 eq=np.column_stack([C,-target if maximize else np.zeros(3)]);beq=np.zeros(3) if maximize else target;scale=np.max(np.abs(eq),axis=1);eq/=scale[:,None];beq/=scale
 return linprog(np.r_[np.zeros(nc),-1. if maximize else 1.],A_ub=np.vstack(constraints),b_ub=np.concatenate(rhs),A_eq=eq,b_eq=beq,bounds=[(None,None)]*nc+[(0,None)],method='highs',options={'primal_feasibility_tolerance':1e-9,'dual_feasibility_tolerance':1e-9})

def run():
 K=c.convert(json.loads(Path('postcontact_input.json').read_text()));R=c.convert(json.loads(Path('capacity_output/distributed_receipt.json').read_text()));X=K['points'];faces=K['faces'];modes,images=modes_for(X,faces,R['controller_indices']);V,M=c.mass(X,faces);target=c.mul(M,-1);J,g=geometry_matrix(X,faces,modes);Jm,gm,labels=mechanical_matrix(K,modes,images)
 cap=solve(K,modes,images,target,J,g,Jm,gm,True);print('MECHANICAL_LP_CAPACITY',cap.success,cap.x[-1] if cap.success else cap.message,flush=True)
 results=[]
 for factor in ([int(sys.argv[1])] if len(sys.argv)>1 else [4,16,64,256]):
  lp=solve(K,modes,images,c.mul(target,factor),J,g,Jm,gm)
  if not lp.success:
   print('MECHANICAL_LP_INFEASIBLE',factor,flush=True);break
  Y,coeff,pivot=exact_endpoint(X,faces,modes,images,lp.x[:-1],c.mul(target,factor));assert c.mass(Y,faces)==(V,c.mul(M,1-factor))
  c.dump('capacity_output/mechanical_factor'+str(factor)+'_candidate.json',dict(points=Y,coefficients=coeff,pivot=pivot,factor=factor,float_rho=float(lp.fun)))
  valid=c.valid_complex(Y,faces)
  if not valid:
   print('MECHANICAL_GEOMETRY_REJECT',factor,flush=True);break
  H=c.hull(Y);A=c.mechanics(H);print('EXACT_REALLOCATED_CAPACITY',factor,A['strict'],A['weak'],flush=True)
  result=dict(factor=factor,report=A,modes=modes,images=images,coefficients=coeff,pivot=pivot,original_material=K['material'],float_rho=float(lp.fun));results.append(result)
  c.dump('capacity_output/mechanical_factor'+str(factor)+'.json',result)
 c.dump('capacity_output/mechanical_capacity_summary.json',dict(float_nomination_capacity=float(cap.x[-1]) if cap.success else None,observed=[dict(factor=r['factor'],strict=r['report']['strict'],weak=r['report']['weak'],rho=r['float_rho']) for r in results]))
if __name__=='__main__':run()
