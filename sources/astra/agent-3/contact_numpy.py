"""Independent NumPy forward differentiation of a complete rational contact chart.
The supplied exact plan solves each dependent coordinate from n.x=1. True
facets/edges are retained only when every noncontact and face turn is positive.
"""
import json,argparse
from pathlib import Path
import numpy as np
from gmpy2 import mpq
from persistence_birth import bars_loss
from support_geometry import escape

class Chart:
 def __init__(self,path):
  self.path=Path(path);self.meta=json.loads(self.path.read_text());m=self.meta;self.F=m['F'];self.V=m['V'];self.N=m['nodes'];self.d=len(m['free_controls']);self.q0=np.array(m['free_controls'],float)/m['grid'];self.plan=m['plan'];self.faces=m['faces'];self.T=np.array([(f[0],f[k],f[k+1]) for f in self.faces for k in range(1,len(f)-1)]);owners={};self.incidence=np.zeros((self.F,self.V),bool)
  for f,cy in enumerate(self.faces):
   self.incidence[f,cy]=True
   for i,j in zip(cy,cy[1:]+cy[:1]):owners.setdefault(tuple(sorted((i,j))),[]).append(f)
  self.pe=np.array(list(owners));self.qe=np.array(list(owners.values()));assert len(self.pe)==m['E'] and all(len(v)==2 for v in owners.values())
 def reconstruct(self,q,derivative=True):
  A=np.zeros((self.N,3));DA=np.zeros((self.N,3,self.d)) if derivative else None
  for p in self.plan:
   i=p['node'];deps=p['deps'];axes=p['axes'];rest=p['free_axes'];indices=p['free_indices'];x=np.zeros(3)
   for axis,v in p['fixed'].items():x[int(axis)]=v
   if rest:x[rest]=q[indices]
   if deps:
    M=A[np.ix_(deps,axes)];rhs=1-A[deps]@x;x[axes]=np.linalg.solve(M,rhs)
   A[i]=x
   if derivative:
    if rest:DA[i,rest,indices]=1
    if deps:DA[i,axes]=np.linalg.solve(M,-np.einsum('jcp,c->jp',DA[deps],x)-A[deps]@DA[i])
  return A,DA
 def physical(self,q,derivative=True,require_valid=True):
  A,DA=self.reconstruct(q,derivative);Y=A[:self.F];X=A[self.F:];gap=1-Y@X.T;T=self.T;a,b,c=X[T[:,0]],X[T[:,1]],X[T[:,2]];v6=np.einsum('ic,ic->i',a,np.cross(b,c));V=v6.sum()/6;cent=np.sum(v6[:,None]*(a+b+c),axis=0)/(4*v6.sum());Z=X-cent;den=1-Y@cent;Q=Y/den[:,None];non=gap[~self.incidence];contact=float(np.max(abs(gap[self.incidence])));turns=[]
  for i,fc in enumerate(self.faces):
   for k in range(1,len(fc)-1):turns.append(np.cross(X[fc[k]]-X[fc[0]],X[fc[k+1]]-X[fc[0]])@Y[i])
  valid=min(non)>0 and contact<1e-8 and V>0 and min(den)>0 and min(turns)>0
  if require_valid and not valid:raise ValueError('invalid physical contact realization')
  g=dict(X=X,Y=Y,Z=Z,H=Q,centroid=cent,V=V,gap=gap,noncontact=non,contact_error=contact,valid=valid,min_turn=float(min(turns)),den=den)
  if not derivative:return g
  DY=DA[:self.F];DX=DA[self.F:];da,db,dc=DX[T[:,0]],DX[T[:,1]],DX[T[:,2]];dv=np.einsum('ic,icp->ip',np.cross(b,c),da)+np.einsum('ic,icp->ip',np.cross(c,a),db)+np.einsum('ic,icp->ip',np.cross(a,b),dc);Dc=(np.einsum('ip,ic->cp',dv,a+b+c-4*cent)+np.einsum('i,icp->cp',v6,da+db+dc))/(4*v6.sum());DZ=DX-Dc;Dden=-np.einsum('fcp,c->fp',DY,cent)-Y@Dc;DQ=DY/den[:,None,None]-Y[:,:,None]*Dden[:,None,:]/den[:,None,None]**2;Dgap=-(np.einsum('fcp,vc->fvp',DY,X)+np.einsum('fc,vcp->fvp',Y,DX));g.update(DX=DX,DY=DY,DZ=DZ,DH=DQ,Dcentroid=Dc,Dgap=Dgap)
  return g
 def loss(self,g,eta):
  lp,GP,P=bars_loss(g['Z'],self.pe,eta);lq,GQ,Q=bars_loss(g['H'],self.qe,eta);grad=np.einsum('ic,icp->p',GP,g['DZ'])+np.einsum('ic,icp->p',GQ,g['DH']);return lp+lq,grad,dict(P=P,Q=Q,Pmax=max(P,default=0.),Qmax=max(Q,default=0.),S=int(np.sum(escape(g['H'])[0]<0)),U=int(np.sum(escape(g['Z'])[0]<0)))

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('construction');p.add_argument('out');a=p.parse_args();c=Chart(a.construction);g=c.physical(c.q0);v,J,inf=c.loss(g,.01);rng=np.random.default_rng(3385);d=rng.normal(size=c.d);d/=np.linalg.norm(d);r=[]
 for h in [1e-6,1e-7,1e-8]:
  p1=c.physical(c.q0+h*d,require_valid=False);p2=c.physical(c.q0-h*d,require_valid=False);vv1=c.loss(p1,.01)[0];vv2=c.loss(p2,.01)[0];row=dict(h=h,objective_fd=(vv1-vv2)/(2*h),objective_analytic=float(J@d),centroid_error=float(np.max(abs((p1['centroid']-p2['centroid'])/(2*h)-g['Dcentroid']@d))),contact_error=g['contact_error']);r.append(row);print('CONTACT_GRAD',row,flush=True)
 Path(a.out).write_text(json.dumps(dict(source=a.construction,seed=inf,checks=r,notes='finite differences use the explicit algebraic chart even when a perturbed proposal violates noncontacts; only the initial seed is asserted a physical convex body'),indent=2));print('CONTACT_SEED',inf,flush=True)
