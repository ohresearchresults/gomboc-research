"""Retained-primal-vertex contact chart with inherited root-reaching forests.
The old S8 chart is only an auxiliary exact rational parametrization. A convex
hull of selected old intersection points is the actual homogeneous solid.
New triangular facets are solved from their three retained vertices; inherited
maximal facets remain exactly planar. All moments below refer to the new solid.
"""
from pathlib import Path
import json,sys,itertools,os
import numpy as np
SOURCE=Path(os.environ.get('S8_SOURCE','/mnt/data/s8/source'))
sys.path[:0]=[str(SOURCE/'parent/mechanism/parent_sources'),str(SOURCE/'parent/mechanism')]
from atlas_opt import Atlas
from numeric import triangles,topology,best_triples
from deletion import Model
class Coarse:
 def __init__(self,data,raw,deleted):
  self.data=data;self.raw=raw;self.deleted=sorted(deleted);self.base=Atlas(data,raw['faces']);self.np=self.base.np;self.u0=self.base.u0.copy()
  model=Model(raw);keep,faces,H,ef=model.hull(set(deleted));self.keep=np.array(keep);self.faces=faces;self.owners,self.ef=topology(faces);self.tri=triangles(faces);self.H=H
  lut={h:f for f,h in model.originalplanes.items()};self.oldfaces=[lut.get(h,-1)for h in H];self.n=len(H)
  self.baseP=np.linalg.solve(self.base.chart(self.u0,False)[:self.base.n][self.base.triples],np.ones((len(self.base.triples),3,1)))[:,:,0]
  # New polygonal facets would need additional exact rank equations; reject those here.
  assert all(f>=0 or len(cy)==3 for f,cy in zip(self.oldfaces,faces))
  self.newtri={fi:np.array(cy)for fi,(old,cy)in enumerate(zip(self.oldfaces,faces))if old<0}
  self.inc=np.zeros((len(keep),len(H)),bool)
  for i,ow in enumerate(self.owners):self.inc[i,ow]=True
  self.Sroot=self.oldfaces.index(3);self.Uroot=keep.index(95);self.si=np.array([i for i in range(self.n)if i!=self.Sroot]);self.ui=np.array([i for i in range(len(keep))if i!=self.Uroot])
  base=self.base.state(self.u0,False);up=base['cu'].argmax(1);sp=base['cs'].argmax(1);up[self.base.Uroot]=self.base.Uroot;sp[self.base.Sroot]=self.base.Sroot
  where={v:i for i,v in enumerate(keep)};parents=[]
  for i in keep:
   j=int(up[i]);seen={i}
   while j not in where:
    assert j not in seen;seen.add(j);j=int(up[j])
   parents.append(where[j])
  self.uparent=np.array(parents);valid={v:i for i,v in enumerate(self.oldfaces)if v>=0};parents=[];st=self.state(self.u0,False,parents=False)
  for i,old in enumerate(self.oldfaces):
   if old>=0:
    j=int(sp[old]);seen={old}
    while j not in valid:
     assert j not in seen;seen.add(j);j=int(sp[j])
    parents.append(valid[j])
   else:
    js=list(valid.values());parents.append(max(js,key=lambda j:st['cs'][i,j]))
  self.sparent=np.array(parents)
  for par,root in [(self.uparent,self.Uroot),(self.sparent,self.Sroot)]:
   for i in range(len(par)):
    seen=set();j=i
    while j!=root:assert j not in seen;seen.add(j);j=int(par[j])
 def state(self,u,jac=True,parents=True):
  if jac:XX,DXX=self.base.chart(u);qo=XX[:self.base.n];dqo=DXX[:self.base.n]
  else:XX=self.base.chart(u,False);qo=XX[:self.base.n]
  A=qo[self.base.triples];Po=np.linalg.solve(A,np.ones((len(A),3,1)))[:,:,0];P=Po[self.keep]
  if jac:dPo=np.linalg.solve(A,-np.einsum('vrcp,vc->vrp',dqo[self.base.triples],Po));dP=dPo[self.keep]
  q=np.empty((self.n,3));dq=np.empty((self.n,3,self.np))if jac else None
  for f,old in enumerate(self.oldfaces):
   if old>=0:
    q[f]=qo[old]
    if jac:dq[f]=dqo[old]
   else:
    ix=self.newtri[f];q[f]=np.linalg.solve(P[ix],np.ones(3))
    if jac:dq[f]=np.linalg.solve(P[ix],-np.einsum('rcp,c->rp',dP[ix],q[f]))
  a,b,c=[P[self.tri[:,k]]for k in range(3)];det=np.einsum('ij,ij->i',a,np.cross(b,c));V=det.sum()/6;M=np.einsum('t,tc->c',det,a+b+c)/24;cent=M/V
  h=1-q@cent;n=q/h[:,None];x=P-cent;gaps=1-P@q.T
  def cosine(z):
   num=z@z.T-np.einsum('ij,ij->i',z,z)[:,None];diff=z[None,:,:]-z[:,None,:];den=np.linalg.norm(z,axis=1)[:,None]*np.linalg.norm(diff,axis=2)
   out=np.divide(num,den,out=np.full_like(num,-np.inf),where=den>1e-14);np.fill_diagonal(out,-np.inf);return out
  cs=cosine(n);cu=cosine(x);sw=cs[self.si].argmax(1);uw=cu[self.ui].argmax(1)
  if parents:sw=self.sparent[self.si];uw=self.uparent[self.ui]
  vals=np.r_[cs[self.si,sw],cu[self.ui,uw]];out=dict(q=q,P=P,V=V,M=M,c=cent,h=h,n=n,x=x,gaps=gaps,det=det,cs=cs,cu=cu,sw=sw,uw=uw,vals=vals)
  if jac:
   da,db,dc=[dP[self.tri[:,k]]for k in range(3)];ddet=np.einsum('tcp,tc->tp',da,np.cross(b,c))+np.einsum('tcp,tc->tp',db,np.cross(c,a))+np.einsum('tcp,tc->tp',dc,np.cross(a,b));dV=ddet.sum(0)/6
   dM=(np.einsum('tp,tc->cp',ddet,a+b+c)+np.einsum('t,tcp->cp',det,da+db+dc))/24;dcent=(dM-cent[:,None]*dV[None,:])/V
   dh=-np.einsum('icp,c->ip',dq,cent)-q@dcent;dn=dq/h[:,None,None]-q[:,:,None]*dh[:,None,:]/h[:,None,None]**2;dx=dP-dcent[None,:,:]
   def dcoss(z,dz,ii,jj):
    aa=z[ii];bb=z[jj]-aa;daa=dz[ii];dbb=dz[jj]-daa;aa2=np.einsum('ic,ic->i',aa,aa);bb2=np.einsum('ic,ic->i',bb,bb);den=np.sqrt(aa2*bb2);uv=np.einsum('ic,ic->i',aa,bb)
    duv=np.einsum('icp,ic->ip',daa,bb)+np.einsum('icp,ic->ip',dbb,aa)
    return duv/den[:,None]-(uv/den)[:,None]*(np.einsum('icp,ic->ip',daa,aa)/aa2[:,None]+np.einsum('icp,ic->ip',dbb,bb)/bb2[:,None])
   J=np.vstack([dcoss(n,dn,self.si,sw),dcoss(x,dx,self.ui,uw)]);out.update(dq=dq,dP=dP,dc=dcent,J=J,dV=dV,dM=dM,ddet=ddet)
  return out
 def gap_jac(self,s,vi,qi):return -np.einsum('icp,ic->ip',s['dP'][vi],s['q'][qi])-np.einsum('ic,icp->ip',s['P'][vi],s['dq'][qi])
 def save(self,u,path):
  z=json.loads(json.dumps(self.data));X=self.base.chart(u,False);D=z['grid']
  if not np.isfinite(X).all():raise ValueError('nonfinite chart checkpoint')
  z['controls']=[[int(round(float(v)*D)) for v in row]for row in X]
  Path(path).write_text(json.dumps(z,sort_keys=True,separators=(',',':')))
  return z
