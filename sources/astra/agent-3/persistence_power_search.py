"""Full physical primal/dual persistence with power-norm energy.

Unlike a logarithmic objective, this permits the two deep basins to trade depth
without charging every tiny feature almost equally. All positive finite bars
remain in the formula. Numerical loss is never a strict-equilibrium certificate.
"""
import argparse,json,time,hashlib
from pathlib import Path
import numpy as np
from scipy.spatial import ConvexHull
from scipy.spatial.transform import Rotation
from scipy.optimize import linear_sum_assignment,minimize
from support_geometry import escape
from vertex_geometry import geometry
from goal_nomination import preserve
from capacity_polish import run as repair110

def power_bars(A,edges,power):
 aa=np.einsum('ic,ic->i',A,A);i,j=edges.T;e=A[j]-A[i];ee=np.einsum('ic,ic->i',e,e);t=np.clip(-np.einsum('ic,ic->i',A[i],e)/np.where(ee>0,ee,1),0,1);foot=A[i]+t[:,None]*e;death=np.einsum('ic,ic->i',foot,foot);parent=np.arange(len(A));G=np.zeros_like(A);loss=0.;bars=[]
 def find(k):
  while k!=parent[k]:parent[k]=parent[parent[k]];k=parent[k]
  return k
 for k in np.argsort(death)[::-1]:
  u,v=find(int(i[k])),find(int(j[k]))
  if u==v:continue
  if(aa[u],u)>(aa[v],v):u,v=v,u
  parent[u]=v;dep=aa[u]-death[k];assert dep>=-1e-12*max(aa)
  if dep<=0:continue
  b=dep/aa[u];coeff=power*b**(power-1)/aa[u];loss+=b**power;G[u]+=coeff*(1-b)*2*A[u];G[i[k]]-=coeff*2*(1-t[k])*foot[k];G[j[k]]-=coeff*2*t[k]*foot[k];bars.append(float(b))
 return loss,G,sorted(bars,reverse=True)

def evaluate(X,power=2):
 hull=ConvexHull(X);T=hull.simplices.copy();a,b,c=X[T[:,0]],X[T[:,1]],X[T[:,2]];flip=np.einsum('ic,ic->i',np.cross(b-a,c-a),hull.equations[:,:3])<0;T[flip]=T[flip][:,[0,2,1]];a,b,c=X[T[:,0]],X[T[:,1]],X[T[:,2]];v6=np.einsum('ic,ic->i',a,np.cross(b,c));D=sum(v6);g=np.sum(v6[:,None]*(a+b+c),axis=0)/(4*D);Z=X-g;H=-hull.equations[:,:3]/(hull.equations[:,3]+hull.equations[:,:3]@g)[:,None];ed=np.unique(np.sort(np.concatenate([T[:,[0,1]],T[:,[1,2]],T[:,[2,0]]]),axis=1),axis=0);qe=np.unique(np.sort(np.column_stack((np.repeat(np.arange(len(T)),3),hull.neighbors.ravel())),axis=1),axis=0);active=hull.vertices;mapping=np.full(len(X),-1,int);mapping[active]=np.arange(len(active));lp,GP,P=power_bars(Z[active],mapping[ed],power);lq,GQ,Q=power_bars(H,qe,power);G=np.zeros_like(X);G[active]=GP;w=np.linalg.solve(np.swapaxes(Z[T],1,2),GQ[...,None])[...,0];dz=-w[:,:,None]*H[:,None,:];np.add.at(G,T.ravel(),dz.reshape(-1,3));tg=-G.sum(0);s=(a+b+c-4*g)@tg
 for k,cr in [(0,np.cross(b,c)),(1,np.cross(c,a)),(2,np.cross(a,b))]:np.add.at(G,T[:,k],(v6[:,None]*tg+s[:,None]*cr)/(4*D))
 total=lp+lq
 if total>0:G*=total**(1/power-1)/power
 value=total**(1/power);info=dict(loss=float(value),power=power,V=len(active),P=P,Q=Q,Pmax=max(P,default=0.),Qmax=max(Q,default=0.),S=int(np.sum(escape(H)[0]<0)),U=int(np.sum(escape(Z[active])[0]<0)))
 return value,G,info

def centered(X):
 g=geometry(X,False);X=g['Z'][g['vertices']];return X/max(np.linalg.norm(X,axis=1))

def paired(X,Y,twist):
 root=int(np.argmax(np.linalg.norm(X,axis=1)));axis=X[root]/np.linalg.norm(X[root]);YY=Y@Rotation.from_rotvec(twist*axis).as_matrix().T;cost=np.sum((X[:,None]-YY[None])**2,axis=2);ii,jj=linear_sum_assignment(cost);Q=np.zeros_like(X);Q[ii]=YY[jj];missing=sorted(set(range(len(X)))-set(ii));g=geometry(YY,False);HH=g['H'];cc=g['g']
 for i in missing:
  ray=X[i]-cc;den=max(HH@ray);factor=min(1.,.999/den)if den>0 else 1.;Q[i]=cc+factor*ray
 assert len(X)<=84 and len(YY)<=len(X);return Q,dict(assigned_X=ii.tolist(),assigned_Y=jj.tolist(),interior_indices=missing,twist=twist)

def optimize(X,out,iterations):
 out=Path(out);out.mkdir(parents=True,exist_ok=False);np.save(out/'initial.npy',X);rows=[];start=time.time()
 for phase,power in enumerate([2,4,2]):
  d=out/f'phase{phase}_p{power}';d.mkdir();best=np.inf;calls=0
  def fun(flat):
   nonlocal best,calls
   calls+=1;Y=flat.reshape(X.shape);value,G,info=evaluate(Y,power)
   if value<best:
    best=value;np.save(d/'best.npy',Y);info.update(calls=calls,seconds=time.time()-start);(d/'best.json').write_text(json.dumps(info,indent=2))
   if info['S']==info['U']==1:preserve(Y,d/f'goal_nomination_{calls}','power-norm whole physical persistence numerical own110')
   if calls%1000==0:print('POWER_PERSISTENCE',str(d),calls,value,info['Pmax'],info['Qmax'],info['S'],info['U'],flush=True)
   return value,G.ravel()
  r=minimize(fun,X.ravel(),jac=True,method='L-BFGS-B',options=dict(maxiter=iterations,maxls=50,maxcor=35,gtol=1e-12,ftol=1e-15));X=np.load(d/'best.npy');row=dict(phase=phase,power=power,message=r.message,nit=r.nit,info=evaluate(X,power)[2]);rows.append(row);(out/'phases.json').write_text(json.dumps(rows,indent=2));print('POWER_PERSISTENCE_PHASE',row,flush=True)
  repair110(d/'best.npy',d/'repair110',1,1,180,1e-7)
  if(d/'repair110/success.npy').exists():preserve(np.load(d/'repair110/success.npy'),d/'exact_goal_nomination','complete actual-mass capacity repair after power-norm physical search')

def run(xsource,ysource,out,iterations):
 out=Path(out);out.mkdir(parents=True,exist_ok=False);X=centered(np.load(xsource));Y=centered(np.load(ysource));assert len(X)>=len(Y);(out/'sources.json').write_text(json.dumps([dict(path=str(Path(p).resolve()),sha256=hashlib.sha256(Path(p).read_bytes()).hexdigest())for p in [xsource,ysource]],indent=2));np.save(out/'X.npy',X);np.save(out/'Y.npy',Y);bestpaths=[]
 for j,twist in enumerate([-.2,-.1,0.,.1,.2]):
  YY,meta=paired(X,Y,twist);d=out/f'path{j}';d.mkdir();np.savez(d/'endpoints.npz',X=X,Y=YY);(d/'matching.json').write_text(json.dumps(meta,indent=2));best=np.inf;rows=[]
  for t in np.linspace(0,1,501):
   Z=(1-t)*X+t*YY;v,_,inf=evaluate(Z,2);rows.append(dict(t=float(t),loss=v,P=inf['Pmax'],Q=inf['Qmax'],S=inf['S'],U=inf['U']))
   if inf['S']==inf['U']==1:preserve(Z,d/f'goal_t{t:.6f}','literal interpolated physical point hull at its own centroid')
   if .01<t<.99 and v<best:best=v;np.save(d/'best.npy',Z);(d/'best.json').write_text(json.dumps(rows[-1],indent=2))
  (d/'screen.json').write_text(json.dumps(rows,indent=2));bestpaths.append((best,d));print('POWER_COMPLEMENTARY_PATH',d,best,flush=True)
 for rank,(best,d)in enumerate(sorted(bestpaths)[:3]):optimize(np.load(d/'best.npy'),out/f'optimize{rank}',iterations)

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('xsource');p.add_argument('ysource');p.add_argument('out');p.add_argument('--iterations',type=int,default=4000);a=p.parse_args();run(a.xsource,a.ysource,a.out,a.iterations)
