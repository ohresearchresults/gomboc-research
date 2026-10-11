"""GRID7 full contact-chart own-mass evaluator; fixed per-identity reserves."""
import os
os.environ.setdefault('OPENBLAS_NUM_THREADS','1')
import json,sys,itertools
import numpy as np
from fractions import Fraction
sys.set_int_max_str_digits(0)
class Model:
 def __init__(self,gen,report,deleted=(99,117),forced=None):
  self.gen=gen;self.report=report;self.keep=np.array([i for i in range(gen['n_supports']) if i not in deleted]);self.deleted=list(deleted)
  self.controls=np.array(gen['controls'],float)/gen['grid'];self.free=[(i,k) for i,deps,axes in gen['plan'] for k in range(3) if k not in axes]
  self.z0=np.array([self.controls[i,k] for i,k in self.free]);self.pdim=len(self.z0);self.index={v:j for j,v in enumerate(self.free)}
  self.faces=report['faces'];self.edges=np.array(report['edges']);self.inc=np.zeros((report['V'],len(self.keep)),bool)
  for j,cy in enumerate(self.faces):self.inc[cy,report['active_input_indices'][j]]=True
  self.normid=np.array(report['active_input_indices']);self.adj=[[] for _ in range(report['V'])]
  for i,j in self.edges:self.adj[i].append(j);self.adj[j].append(i)
  self.X0=np.array([[float(Fraction(x)) for x in row] for row in report['raw_vertices']]);self.g0=np.array([float(Fraction(x)) for x in report['raw_centroid']])
  q=self.chart(self.z0,False)[0][self.keep];self.triples=[]
  for inc in self.inc:
   cs=list(itertools.combinations(np.where(inc)[0],3));self.triples.append(max(cs,key=lambda c:abs(np.linalg.det(q[list(c)]))))
  self.triples=np.array(self.triples);self.qscale=np.linalg.norm(q,axis=1)
  self.vi=np.array([i for i,a in enumerate(self.adj) for j in a]);self.vj=np.array([j for i,a in enumerate(self.adj) for j in a]);self.vlens=np.linalg.norm(self.X0[self.vj]-self.X0[self.vi],axis=1)
  self.fid=np.array([f for f,cy in enumerate(self.faces) for i in cy]);self.fi=np.array([i for cy in self.faces for i in cy]);self.fj=np.array([j for cy in self.faces for j in cy[1:]+cy[:1]])
  self.flens=np.linalg.norm(self.X0[self.fj]-self.X0[self.fi],axis=1)*self.qscale[self.normid[self.fid]]
  self.tris=np.array([(cy[0],cy[k],cy[k+1]) for cy in self.faces for k in range(1,len(cy)-1)])
  self.geo_i,self.geo_j=np.where(~self.inc);self.root=next(i for i,p in enumerate(self.X0) if np.array_equal(p,[0,0,1]));self.sface=report['stable_face_ids'][0];self.targetU=sorted(set(report['unstable_vertices'])-{self.root})
  self.vgroups=[np.where(self.vi==i)[0] for i in range(len(self.X0))];self.fgroups=[np.where(self.fid==i)[0] for i in range(len(self.faces))]
  self.forced={82:85,146:147} if forced is None else forced;self.target_idx=np.array([np.where((self.vi==i)&(self.vj==j))[0][0] for i,j in self.forced.items()])
  a=self.eval(self.z0)
  self.locked_v=None
  self.vfloor=np.array([max(1e-8,.2*np.max(a['vert'][g])) if i!=self.root and i not in self.targetU else 0 for i,g in enumerate(self.vgroups)])
  self.ffloor=np.array([max(1e-8,.2*np.max(a['face'][g])) if i!=self.sface else 0 for i,g in enumerate(self.fgroups)])
  self.sfloor=.2*(-a['face'][self.fgroups[self.sface]]);self.geofloor=np.maximum(1e-12,.05*a['geo'])
 def chart(self,z,deriv=True):
  X=self.controls.copy();X[self.gen['n_supports']]=[0,0,1];d=np.zeros((len(X),3,len(z))) if deriv else None
  for i,deps,axes in self.gen['plan']:
   rest=[k for k in range(3) if k not in axes]
   for k in rest:
    j=self.index[(i,k)];X[i,k]=z[j]
    if deriv:d[i,k,j]=1
   if deps:
    A=X[np.ix_(deps,axes)];b=1-X[np.ix_(deps,rest)]@X[i,rest];X[i,axes]=np.linalg.solve(A,b)
    if deriv:
     rhs=-np.einsum('dkp,k->dp',d[deps],X[i])-X[np.ix_(deps,rest)]@d[i,rest];d[i,axes]=np.linalg.solve(A,rhs)
  return X,d
 def eval(self,z,deriv=False):
  full,d=self.chart(z,deriv);q=full[self.keep];Q=q[self.triples];inv=np.linalg.inv(Q);x=(inv@np.ones((len(Q),3,1)))[:,:,0]
  if deriv:dq=d[self.keep];dx=-np.einsum('vik,vkp->vip',inv,np.einsum('vkcp,vc->vkp',dq[self.triples],x))
  ta,tb,tc=(x[self.tris[:,k]] for k in range(3));det=np.einsum('ti,ti->t',ta,np.cross(tb,tc));v6=det.sum();s=ta+tb+tc;g=np.einsum('t,ti->i',det,s)/(4*v6)
  if deriv:
   da,db,dc=(dx[self.tris[:,k]] for k in range(3));dd=np.einsum('ti,tip->tp',np.cross(tb,tc),da)+np.einsum('ti,tip->tp',np.cross(tc,ta),db)+np.einsum('ti,tip->tp',np.cross(ta,tb),dc)
   dg=(np.einsum('tp,ti->ip',dd,s)+np.einsum('t,tip->ip',det,da+db+dc))/(4*v6)-g[:,None]*dd.sum(axis=0)/v6
  r=x-g;vd=x[self.vj]-x[self.vi];vert=np.einsum('ij,ij->i',r[self.vi],vd)/self.vlens
  fi,fj=self.fi,self.fj;n=q[self.normid[self.fid]];ri=r[fi];fd=x[fj]-x[fi];face=-np.einsum('ij,ij->i',n,np.cross(ri,fd))/self.flens
  gi,gj=self.geo_i,self.geo_j;geo=(1-np.einsum('ij,ij->i',x[gi],q[gj]))/self.qscale[gj]
  out=dict(q=q,x=x,g=g,volume=v6/6,vert=vert,face=face,geo=geo,allslack=1-x@q.T,min_det=det.min())
  if deriv:
   dr=dx-dg;dvd=dx[self.vj]-dx[self.vi];dvert=(np.einsum('ik,ikp->ip',vd,dr[self.vi])+np.einsum('ik,ikp->ip',r[self.vi],dvd))/self.vlens[:,None]
   dn=dq[self.normid[self.fid]];dfd=dx[fj]-dx[fi];dface=-(np.einsum('ik,ikp->ip',np.cross(ri,fd),dn)+np.einsum('ik,ikp->ip',np.cross(fd,n),dr[fi])+np.einsum('ik,ikp->ip',np.cross(n,ri),dfd))/self.flens[:,None]
   dgeo=-(np.einsum('ik,ikp->ip',q[gj],dx[gi])+np.einsum('ik,ikp->ip',x[gi],dq[gj]))/self.qscale[gj,None]
   out.update(dvert=dvert,dface=dface,dgeo=dgeo,dg=dg,dx=dx,dq=dq)
  return out
 def select(self,a):
  vv=np.array([g[np.argmax(a['vert'][g])] for i,g in enumerate(self.vgroups) if i!=self.root and i not in self.targetU]);ff=np.array([g[np.argmax(a['face'][g])] for i,g in enumerate(self.fgroups) if i!=self.sface]);return (vv if self.locked_v is None else self.locked_v),ff
 def constr(self,a,vv=None,ff=None,deriv=False,geomask=None):
  if vv is None:vv,ff=self.select(a)
  if geomask is None:geomask=np.ones(len(a['geo']),bool)
  sg=self.fgroups[self.sface];ug=self.vgroups[self.root]
  values=np.r_[a['vert'][vv]-self.vfloor[self.vi[vv]],a['face'][ff]-self.ffloor[self.fid[ff]],-a['face'][sg]-self.sfloor,-a['vert'][ug]-.001,a['geo'][geomask]-self.geofloor[geomask]]
  if not deriv:return values
  jac=np.r_[a['dvert'][vv],a['dface'][ff],-a['dface'][sg],-a['dvert'][ug],a['dgeo'][geomask]];return values,jac
 def census(self,a):
  S=[i for i,g in enumerate(self.fgroups) if np.max(a['face'][g])<0];U=[i for i,g in enumerate(self.vgroups) if np.max(a['vert'][g])<0]
  h=[];weak=[]
  for i,j in self.edges:
   ff=np.where(self.inc[i]&self.inc[j])[0]
   if len(ff)!=2:raise ValueError('edge incidence')
   n,p=a['q'][ff];e=a['x'][j]-a['x'][i];r=a['x'][i]-a['g'];ee=e@e;tt=-r@e/ee;y=r+tt*e
   nn=n@n;pp=p@p;np_=n@p;den=nn*pp-np_**2;lam=(pp*(n@y)-np_*(p@y))/den;mu=(nn*(p@y)-np_*(n@y))/den
   vals=[tt,1-tt,lam,mu]
   if min(vals)>0:h.append([int(i),int(j)])
   elif min(vals)>=-1e-10:weak.append([int(i),int(j)])
  return {'S':S,'U':U,'H':h,'near_weak_edges':weak}
