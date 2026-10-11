"""Uniform Minkowski sums with two segments and one consistent affine map.

True facets are constructed from the common normal fan: old facets, supported
old-edge/segment parallelograms, and segment/segment parallelograms. No angular
facet merging is performed. Exact success freezes the entire rational body.
"""
import argparse,json,hashlib,time
from pathlib import Path
from math import gcd,lcm
from itertools import product
import numpy as np
from gmpy2 import mpq
from scipy.optimize import differential_evolution,minimize
from contact_physical_110 import PhysicalGuards
from exact_audit_vertices import check_B,cross,sub,dot
from persistence_birth import bars_loss
from goal_nomination import ExactGoalCandidateFound


class Family:
 def __init__(self,source,projective=False,segments_count=2):
  assert segments_count in [1,2];self.k=segments_count;self.base_d=5+3*self.k;self.projective=projective;self.d=self.base_d+(3 if projective else 0);self.source=Path(source);a=json.loads(self.source.read_text());self.a=a
  self.origin=tuple(mpq(float(mpq(z)))for z in a['raw_centroid'])
  self.exactX=[tuple(mpq(v)-self.origin[k]for k,v in enumerate(row))for row in a['raw_vertices']]
  scale=max(np.linalg.norm(np.array(self.exactX,float),axis=1));self.scale=mpq(float(scale));self.exactX=[tuple(v/self.scale for v in x)for x in self.exactX]
  self.X=np.array(self.exactX,float);self.oldfaces=a['faces'];self.oldedges=np.array(a['edges'])
  N=[]
  for row in a['normals']:
   n=tuple(map(mpq,row));sc=max(map(abs,n));nn=np.array([float(v/sc)for v in n]);N.append(nn/np.linalg.norm(nn))
  self.N=np.array(N);self.n=len(self.X)

 def parameters(self,t):
  aa,bb,c,d,e=t[:5];A=np.array([[np.exp(aa),c,d],[0,np.exp(bb),e],[0,0,np.exp(-aa-bb)]],float);DA=np.zeros((3,3,self.d));DA[0,0,0]=A[0,0];DA[1,1,1]=A[1,1];DA[2,2,:2]=-A[2,2];DA[0,1,2]=1;DA[0,2,3]=1;DA[1,2,4]=1
  seg=[];ds=[]
  for start in range(5,self.base_d,3):
   lr,theta,phi=t[start:start+3];r=np.exp(lr);v=r*np.array([np.sin(theta)*np.cos(phi),np.sin(theta)*np.sin(phi),np.cos(theta)]);D=np.zeros((3,self.d));D[:,start]=v;D[:,start+1]=r*np.array([np.cos(theta)*np.cos(phi),np.cos(theta)*np.sin(phi),-np.sin(theta)]);D[:,start+2]=r*np.array([-np.sin(theta)*np.sin(phi),np.sin(theta)*np.cos(phi),0]);seg.append(v);ds.append(D)
  return A,DA,np.array(seg),np.array(ds)

 def base_derivatives(self,t,ids):
  return None

 def geometry(self,t,derivative=True):
  A,DA,seg,Dseg=self.parameters(t)
  if self.k==2 and np.linalg.norm(np.cross(seg[0],seg[1]))<1e-7*np.linalg.norm(seg[0])*np.linalg.norm(seg[1]):raise ValueError('parallel segment directions')
  facekeys=[]
  for n,cy in zip(self.N,self.oldfaces):
   z=seg@n
   if min(abs(z))<1e-12:raise ValueError('segment lies at a normal-fan contact')
   signs=tuple(map(int,np.where(z>0,1,-1)));facekeys.append([(int(i),*signs)for i in cy])
  for s in range(self.k):
   other=1-s
   for i,j in self.oldedges:
    ee=self.X[j]-self.X[i];nn=np.cross(ee,seg[s]);ll=np.linalg.norm(nn)
    if ll<1e-14:raise ValueError('segment parallel to source edge')
    nn/=ll
    for sign in [-1,1]:
     n=sign*nn;gap=self.X[i]@n-self.X@n;mask=np.ones(self.n,bool);mask[[i,j]]=False
     if min(gap[mask])<=0:continue
     z=float(n@seg[other])if self.k==2 else 1.
     if abs(z)<1e-12:raise ValueError('segment at edge-fan contact')
     ss=1 if z>0 else-1;cy=[]
     for vertex,sgn in [(i,-1),(j,-1),(j,1),(i,1)]:
      si=[ss]*self.k;si[s]=sgn;cy.append((int(vertex),*si))
     if sign<0:cy.reverse()
     facekeys.append(cy)
  nn=np.cross(seg[0],seg[1])if self.k==2 else np.ones(3);nn/=np.linalg.norm(nn)
  for sign in ([-1,1]if self.k==2 else []):
   n=sign*nn;values=self.X@n;i=int(np.argmax(values));rest=np.delete(values,i)
   if values[i]-max(rest)<1e-12:raise ValueError('nonunique base vertex in segment-sum facet')
   cy=[(i,-1,-1),(i,1,-1),(i,1,1),(i,-1,1)]
   if sign<0:cy.reverse()
   facekeys.append(cy)
  labels=sorted({k for cy in facekeys for k in cy});lookup={k:i for i,k in enumerate(labels)};faces=[[lookup[k]for k in cy]for cy in facekeys]
  owners={}
  for f,cy in enumerate(faces):
   for i,j in zip(cy,cy[1:]+cy[:1]):owners.setdefault(tuple(sorted((i,j))),[]).append(f)
  if not all(len(x)==2 for x in owners.values())or len(labels)-len(owners)+len(faces)!=2:raise ValueError('incomplete common normal fan')
  if not(17<=len(owners)<=248 and len(labels)+len(owners)+len(faces)<500):raise ValueError('true graph exceeds target complexity')
  ids=np.array([k[0]for k in labels]);signs=np.array([k[1:]for k in labels]);B=self.X[ids]+signs@seg;DB=np.einsum('is,scp->icp',signs,Dseg);baseD=self.base_derivatives(t,ids)
  if baseD is not None:DB+=baseD
  p=np.zeros(3);Dp=np.zeros((3,self.d))
  if self.projective:
   u=np.array(t[self.base_d:self.d]);j=int(np.argmin(B@u));m=-B[j]@u;Du=np.zeros((3,self.d));Du[:,self.base_d:self.d]=np.eye(3);Dm=-u@DB[j]-B[j]@Du;p=.99*u/(1+m);Dp=.99*Du/(1+m)-.99*u[:,None]*Dm/(1+m)**2
  bd=1+B@p
  if min(bd)<=0:raise ValueError('nonpositive projective denominator')
  W=B/bd[:,None];X=W@A.T
  T=np.array([(cy[0],cy[k],cy[k+1])for cy in faces for k in range(1,len(cy)-1)]);a,b,c=X[T[:,0]],X[T[:,1]],X[T[:,2]];v6=np.einsum('ic,ic->i',a,np.cross(b,c));volume=v6.sum()/6
  if volume<=0:raise ValueError('wrong common-fan orientation')
  centre=np.sum(v6[:,None]*(a+b+c),axis=0)/(4*v6.sum());Z=X-centre;tri=np.array([cy[:3]for cy in faces]);Y=np.linalg.solve(X[tri],np.ones((len(tri),3,1)))[:,:,0];den=1-Y@centre
  if min(den)<=0:raise ValueError('physical centroid outside a support')
  H=Y/den[:,None];inc=np.zeros((len(faces),len(X)),bool)
  for f,cy in enumerate(faces):inc[f,cy]=True
  gap=1-Y@X.T
  if min(gap[~inc])<=0 or max(abs(gap[inc]))>1e-8:raise ValueError('common-fan body failed strict floating contact validation')
  g=dict(X=X,Z=Z,Y=Y,H=H,centroid=centre,volume=volume,faces=faces,labels=labels,pe=np.array(list(owners)),qe=np.array(list(owners.values())),A=A,segments=seg,projective_p=p,E=len(owners),V=len(X),F=len(faces),T=T)
  if not derivative:return g
  Dbd=np.einsum('icp,c->ip',DB,p)+B@Dp;DW=DB/bd[:,None,None]-W[:,:,None]*Dbd[:,None,:]/bd[:,None,None];DX=np.einsum('ic,acp->iap',W,DA)+np.einsum('icp,ac->iap',DW,A)
  da,db,dc=DX[T[:,0]],DX[T[:,1]],DX[T[:,2]];dv=np.einsum('ic,icp->ip',np.cross(b,c),da)+np.einsum('ic,icp->ip',np.cross(c,a),db)+np.einsum('ic,icp->ip',np.cross(a,b),dc)
  Dg=(np.einsum('ip,ic->cp',dv,a+b+c-4*centre)+np.einsum('i,icp->cp',v6,da+db+dc))/(4*v6.sum());DY=np.linalg.solve(X[tri],-np.einsum('fc,facp->fap',Y,DX[tri]));Dden=-np.einsum('fcp,c->fp',DY,centre)-Y@Dg;DH=DY/den[:,None,None]-Y[:,:,None]*Dden[:,None,:]/den[:,None,None]**2
  g.update(DX=DX,DZ=DX-Dg,DY=DY,DH=DH);return g

 def score(self,t,derivative=False):
  g=self.geometry(t,derivative);lp,GP,P=bars_loss(g['Z'],g['pe'],.03);lq,GQ,Q=bars_loss(g['H'],g['qe'],.03)
  from support_geometry import escape
  cl=dict(S=int(sum(escape(g['H'])[0]<0)),U=int(sum(escape(g['Z'])[0]<0)),Pmax=max(P,default=0.),Qmax=max(Q,default=0.),V=g['V'],E=g['E'],F=g['F'])
  G=np.einsum('ic,icp->p',GP,g['DZ'])+np.einsum('ic,icp->p',GQ,g['DH'])if derivative else None
  return lp+lq,G,cl,g

 def freeze(self,t,out):
  out=Path(out);out.mkdir(parents=True,exist_ok=False);g=self.geometry(t,False);np.save(out/'parameters.npy',t)
  A=[tuple(mpq(float(v))for v in row)for row in g['A']];seg=[tuple(mpq(float(v))for v in row)for row in g['segments']];p=tuple(mpq(float(v))for v in g['projective_p'])
  points=[];lookup={}
  for i,x in enumerate(self.exactX):
   for signs in product([-1,1],repeat=self.k):
    y=tuple(x[k]+sum(signs[j]*seg[j][k]for j in range(self.k))for k in range(3));den=1+dot(p,y);assert den>0;z=tuple(dot(row,y)/den for row in A);lookup[(i,*signs)]=z;points.append(z)
  X=[lookup[k]for k in g['labels']];rows=set()
  for cy in g['faces']:
   a,b,c=[X[i]for i in cy[:3]];n=cross(sub(b,a),sub(c,a));h=dot(n,a)
   assert h>0 and all(dot(n,x)<=h for x in points),'literal rational sum violates nominated support'
   rr=(*n,h);D=lcm(*(int(v.denominator)for v in rr));ii=tuple(int(v*D)for v in rr);gg=gcd(*ii);rows.add(tuple(v//gg for v in ii))
  for axis in range(3):
   for s in [-1,1]:
    n=tuple(mpq(s if k==axis else 0)for k in range(3));h=max(dot(n,x)for x in points)+1;rr=(*n,h);D=lcm(*(int(v.denominator)for v in rr));ii=tuple(int(v*D)for v in rr);gg=gcd(*ii);rows.add(tuple(v//gg for v in ii))
  raw=dict(H=sorted(rows));B=lambda v:json.dumps(v,default=str,sort_keys=True,separators=(',',':')).encode();(out/'raw.json').write_bytes(B(raw));(out/'coordinates.json').write_bytes(B(dict(points=points,density=1)));(out/'construction.json').write_bytes(B(dict(source=str(self.source.resolve()),source_sha256=hashlib.sha256(self.source.read_bytes()).hexdigest(),origin=self.origin,scale=self.scale,base_points=self.exactX,affine=A,segments=seg,projective_p=p,definition='physical image x -> A*x/(1+p.x) of convex hull of the listed exact base_points plus the listed symmetric line segments, uniformly filled AFTER transformation; six exact redundant box planes establish boundedness')))
  a=check_B.run(raw);found={tuple(map(mpq,x))for x in a['raw_vertices']};assert found<=set(points);assert all(dot(row[:3],p)<=row[3]for row in raw['H']for p in points)
  (out/'audit.json').write_bytes(B(a));s={k:a[k]for k in ['V','E','F','counts','weak','face_primitive_zero_count','vertex_max_zero_count','edge_primitive_zero_count']};s.update(C_2E=2*a['E'],VplusEplusF=a['V']+a['E']+a['F'],audit_sha256=hashlib.sha256((out/'audit.json').read_bytes()).hexdigest());s['goal_met']=a['counts']==[1,1,0]and a['weak']==[0,0,0]and 34<=2*a['E']<500 and s['VplusEplusF']<500;(out/'summary.json').write_text(json.dumps(s,indent=2));print('MINKOWSKI_EXACT',s,flush=True)
  if s['goal_met']:raise ExactGoalCandidateFound('Exact homogeneous Minkowski Figure '+str(out))


def run(source,out,iterations,seed,projective=False,segments_count=2):
 out=Path(out);out.mkdir(parents=True,exist_ok=False);c=Family(source,projective,segments_count);rng=np.random.default_rng(seed);calls=0;best=np.inf;t0=time.time()
 (out/'source.json').write_text(json.dumps(dict(source=str(Path(source).resolve()),sha256=hashlib.sha256(Path(source).read_bytes()).hexdigest(),segments_count=segments_count,projective=projective,scope='new uniformly filled Minkowski/affine bodies, exact audit only for numerical strict110 nominations'),indent=2))
 def fun(t,jac=False):
  nonlocal calls,best
  calls+=1
  try:value,G,cl,g=c.score(t,jac)
  except(ValueError,AssertionError,np.linalg.LinAlgError):return (1e5,np.zeros(c.d))if jac else 1e5
  if value<best:
   best=value;np.save(out/'best_parameters.npy',t);np.save(out/'best_vertices.npy',g['X']);(out/'best.json').write_text(json.dumps(dict(loss=value,calls=calls,seconds=time.time()-t0,**cl),indent=2))
  if cl['S']==cl['U']==1:c.freeze(t,out/f'exact_nomination{calls}')
  if calls%2000==0:print('MINKOWSKI_GOAL_SEARCH',calls,best,cl,flush=True)
  return(value,G)if jac else value
 bounds=[(-1.2,1.2)]*2+[(-1.5,1.5)]*3+[(-9.,1.),(.02,np.pi-.02),(-np.pi,np.pi)]*c.k
 if projective:bounds+=[(-5.,5.)]*3
 pop=np.empty((110,c.d));pop[:,:5]=rng.normal(0,.08,(110,5))
 for j in range(5,c.base_d,3):pop[:,j]=rng.uniform(-7.,0.,110);pop[:,j+1]=rng.uniform(.1,np.pi-.1,110);pop[:,j+2]=rng.uniform(-np.pi,np.pi,110)
 if projective:pop[:,c.base_d:c.d]=rng.normal(0,.15,(110,3))
 r=differential_evolution(fun,bounds,init=pop,maxiter=iterations,popsize=10,seed=seed,polish=False,tol=1e-9,mutation=(.4,1.1),recombination=.85)
 if (out/'best_parameters.npy').exists():
  rr=minimize(lambda t:fun(t,True),np.load(out/'best_parameters.npy'),jac=True,method='L-BFGS-B',bounds=bounds,options=dict(maxiter=1200,maxls=40,ftol=1e-14,gtol=1e-9));(out/'termination.json').write_text(json.dumps(dict(global_message=str(r.message),local_message=str(rr.message),calls=calls),indent=2))
 print('MINKOWSKI_GOAL_FINITE_STOP',calls,best,flush=True)


if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('source');p.add_argument('out');p.add_argument('--iterations',type=int,default=600);p.add_argument('--seed',type=int,default=96601);p.add_argument('--projective',action='store_true');p.add_argument('--segments',type=int,choices=[1,2],default=2);a=p.parse_args();run(a.source,a.out,a.iterations,a.seed,a.projective,a.segments)
