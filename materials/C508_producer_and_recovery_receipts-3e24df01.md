# material-3e24df011ae8

AI research material · [Export notes](../catalog/coverage.md#text-records)

---

# C508 exact nonwinners: recovery receipts and complete numerical producer

## Evidence boundary and reconstruction

G6_CHAIN_M60_I1_G12 and the DISTINCT rational ties-to-even rounded G6_CHAIN_M60_I1_G5 are homogeneous own176/weak000 nonwinners: V164/E254/F92,C508. They do not replace the accepted own110 C622 endpoint. This turn cold-replayed the complete deterministic recovery source from an empty originating sandbox and matched both recorded geometry hashes, all own-centroid predicates, and projected mass/depth assertions.

The self-contained exact source is material [internal-source-reference], C508_RECOVER_C508.py.txt, 14236 bytes, SHA-256 12c3e1fa064498a760c0c7eb5ef0d79d00276584b0053dab531b7c6cc5cb3838. Save its entire literal text as RECOVER_C508.py. Reconstruction and verification are the same command: `python RECOVER_C508.py`. Tested Python 3.13.5, numpy 2.3.5, scipy 1.17.0. No external input files, random search or originating sandbox are needed. Expected markers: G6_CHAIN_EXACT_AUDIT_PASS twice; PROJECTED_MASS_AND_POLAR_DEPTH_PASS twice; C508_RECOVERY_COMPLETE_NONWINNER_176_WEAK000. The source includes all 46 original G6 control points, all 60 rational G12 cut normals, precise grid/rounding rules, and every exact helper.

Both bodies have 60 new active planes and 32 of the 84 old planes active. The maximum shortest path through the FULL positive polar graph from any new active facet to ANY active old facet is 59, uniquely input143. Depths1..59 occur once, except depth51 occurs twice. Exact projected divergence mass and first moments agree with origin-tetrahedral integration on all three coordinate axes. This is a separate mass identity, not a claim of two independent whole-feature auditors. G12 centroid-denominator bits29807, G5 15126; homogeneous vertex bits138 and92. G4 was classified strict(22,7,27), not176.

The exact capsule alone is sufficient for descendants. The numerical producer below is preserved because it materially generated the original checkpoint; replay does NOT require the full floating iteration trace or bitwise optimizer reproducibility. The original command was `python cut_flow.py --index 1 --count 1 --m 60 --branches 1 --maxiter 1000 --eps 1e-5`, after running RECOVER_C508.py to write G6.json. Index1 sets angle2.8, twist0, scale0.999; RNG seed190928. Original run reported969 iterations. Its full trace CUT_CHAIN_B1_M60_I1.json was259508 bytes, SHA1858f3633b2e27286cd83c91c2662d25d2244d5c691592fe706c6524da146e7f, supplementary in the Library ZIP but not required exact input. The embedded G12 checkpoint is the authoritative finite recovery input.

## Reproduced identities

|File|Bytes|SHA-256|
|---|---:|---|
|G6.json|1144|63ead46daff5c7c9cd4344699cbe551a7e92b2a2851703aacfa55eb1621b6aa5|
|G6_CHAIN_M60_I1_G12.json|2970|ba0d5d46957d91b0ef99e0ddb475c0f18ded3b513125e67ecde46c026ca6fb63|
|G6_CHAIN_M60_I1_G5.json|1702|0e46277b37be19e5a35a391f73f7a16957edf93a9e4b4128144ce8eb17b637fd|
|G6_CHAIN_M60_I1_G12_EXACT_GEOMETRY.json|79549|504c86dedd6b9293ce1bf0c34f3db8349f0fe95db534f6b88e28c6e57cfe6f35|
|G6_CHAIN_M60_I1_G5_EXACT_GEOMETRY.json|46853|986270e0b0f5d396fe78b5ecc93ed28b6154999dc3d9c2e79fa016c8a3c67510|
|G6_CHAIN_M60_I1_G12_EXACT_GEOMETRY_MASS_DEPTH.json|967|3c8b7360928ce106fe324f624b47988565ce0cfbd22250df1386ba80bb0bde24|
|G6_CHAIN_M60_I1_G5_EXACT_GEOMETRY_MASS_DEPTH.json|967|3c8b7360928ce106fe324f624b47988565ce0cfbd22250df1386ba80bb0bde24|
|G6_CHAIN_M60_I1_G12_EXACT_REPORT_STABLE.json|741|7405a3a5fa385423707eba870af0ebe5355e08b1519575bbb31cc4a136cacad7|
|G6_CHAIN_M60_I1_G5_EXACT_REPORT_STABLE.json|736|09cdf20df5584deffe3f925a2b71d491806bf98bbb70435efade9f21d53ffdef|

## Complete cut_flow.py

Extract this fence literally, including the final newline. Expected5831 bytes, SHAd05b7cfab872affcd15ea1d9e914e1b2be28fb65de47e79308bbbbac7f0b229c.

```python
"""Finite G6 clipping searches with explicit positive polar chains.
All masses use the actual rebuilt uniform-volume hull. Numerical scout only.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1'
import argparse,json,hashlib,time
from pathlib import Path
import numpy as np
from scipy.spatial import ConvexHull,HalfspaceIntersection
from scipy.optimize import minimize
from depth_scout import geometry

class Cuts:
 def __init__(self):
  self.P,self.N=geometry('G6.json');D=self.N@self.N.T-np.sum(self.N*self.N,axis=1)[:,None];np.fill_diagonal(D,-np.inf)
  self.root=int(np.argmin(D.max(1)));self.r=self.N[self.root].copy();self.cache=None;self.evaluations=0
 def geom(self,new,derivative=True):
  key=new.tobytes()
  if self.cache is not None and key==self.cache[0]:return self.cache[1]
  N=np.vstack([self.N,new]);Q=HalfspaceIntersection(np.c_[N,-np.ones(len(N))],np.zeros(3))
  p=np.unique(np.round(Q.intersections,12),axis=0);h=ConvexHull(p)
  t=p[h.simplices].copy();co=np.cross(t[:,1]-t[:,0],t[:,2]-t[:,0]);flip=np.einsum('ij,ij->i',co,h.equations[:,:3])<0
  tmp=t[flip,1].copy();t[flip,1]=t[flip,2];t[flip,2]=tmp;co[flip]*=-1
  det=np.einsum('ij,ij->i',t[:,0],np.cross(t[:,1],t[:,2]));V=det.sum()/6;M=(det[:,None]*t.sum(1)).sum(0)/24;c=M/V
  if V<=0:raise ValueError('Nonpositive rebuilt volume')
  mids=t.mean(1);owners=np.argmax(mids@N.T,axis=1)
  gaps=np.max(np.abs(np.einsum('ij,ij->i',mids,N[owners])-1))
  if gaps>1e-7:raise ValueError(f'Facet input assignment gap {gaps}')
  H=np.zeros((len(new),3,3))
  for a,own,cr in zip(t,owners,co):
   i=own-len(self.N)
   if i<0:continue
   n=N[own];s=a.sum(0);H[i]+=np.dot(cr,n)/(24*np.dot(n,n))*(np.outer(s,s)+a.T@a)
  J=np.einsum('ijk,ik->ij',H,new)
  val=np.dot(c,c)/V**(2/3)
  grad=(-2*np.einsum('ijk,k->ij',H,c)+(8/3)*np.dot(c,c)*J)/V**(5/3)
  ans=dict(value=val,grad=grad,H=H,J=J,V=V,M=M,c=c,points=p,triangles=h.simplices,owners=owners,new=new.copy(),N=N,eval=self.evaluations)
  self.evaluations+=1;self.cache=(key,ans);return ans
 def flows(self,new,parent,eps):
  nxt=np.array([self.r if j<0 else new[j] for j in parent]);
  val=np.einsum('ij,ij->i',new,nxt)-(1+eps)*np.einsum('ij,ij->i',new,new)
  jac=np.zeros((len(new),len(new),3))
  for i,j in enumerate(parent):
   jac[i,i]=nxt[i]-2*(1+eps)*new[i]
   if j>=0:jac[i,j]+=new[i]
  return val,jac.reshape(len(new),-1)
 def census(self,g):
  p=g['points']-g['c'];N=g['N'][np.unique(g['owners'])];N=N/(1-N@g['c'])[:,None]
  def count(a):
   e=a@a.T-np.sum(a*a,axis=1)[:,None];np.fill_diagonal(e,-np.inf);loss=e.max(1);return int(np.sum(loss< -1e-9)),float(loss.min())
  return {'S':count(N)[0],'U':count(p)[0],'num_points':len(p),'num_faces':len(N),'worst_polar_escape':count(N)[1],'worst_physical_escape':count(p)[1]}

def initial(r,m,angle,twist,startscale,branches=1):
 R=np.linalg.norm(r);u=r/R
 v=np.array([-1.,0,0]);v-=u*np.dot(v,u)
 if np.linalg.norm(v)<.05:v=np.array([0,1.,0]);v-=u*np.dot(v,u)
 v/=np.linalg.norm(v);w=np.cross(u,v)
 new=[];parents=[]
 for b,n in enumerate([m//branches+(j<m%branches) for j in range(branches)]):
  inds=[]
  for j in range(1,n+1):
   t=j/n;alpha=angle*t;rot=twist*np.sin(np.pi*t)+2*np.pi*b/branches
   direction=u*np.cos(alpha)+(v*np.cos(rot)+w*np.sin(rot))*np.sin(alpha)
   nxt=r if j==1 else new[-1]
   length=np.dot(nxt,direction)*startscale
   if length<=0:raise ValueError('bad initial angular increment')
   new.append(direction*length);parents.append(-1 if j==1 else len(new)-2);inds.append(len(new)-1)
 return np.array(new),np.array(parents)

def run(index,m,maxiter,branches,eps):
 model=Cuts();rng=np.random.default_rng(190927+index)
 angle=[2.5,2.8,3.05][index%3];twist=[0.,.4,-.4,.8,-.8][(index//3)%5];scale=[.999,.99,.97][(index//15)%3]
 new,par=initial(model.r,m,angle,twist,scale,branches)
 # Rotate about old stable-root axis while retaining all initial constraints.
 if index>=45:
  theta=rng.uniform(-np.pi,np.pi);u=model.r/np.linalg.norm(model.r)
  new=new*np.cos(theta)+np.cross(u,new)*np.sin(theta)+np.outer(new@u,u)*(1-np.cos(theta))
 start=new.copy();trace=[];last=[0.]
 def fun(x):
  g=model.geom(x.reshape(m,3));return g['value'],g['grad'].ravel()
 def con(x):return model.flows(x.reshape(m,3),par,eps)[0]
 def jac(x):return model.flows(x.reshape(m,3),par,eps)[1]
 def callback(x):
  g=model.geom(x.reshape(m,3));row={'iter':len(trace)+1,'value':float(g['value']),'V':float(g['V']),'c':g['c'].tolist(),'minflow':float(con(x).min())}
  trace.append(row)
  if time.time()-last[0]>10:print('TRACE',index,row,flush=True);last[0]=time.time()
 res=minimize(fun,new.ravel(),jac=True,method='SLSQP',constraints=[{'type':'ineq','fun':con,'jac':jac}],
  callback=callback,options={'maxiter':maxiter,'ftol':1e-16,'disp':False})
 g=model.geom(res.x.reshape(m,3));report={'index':index,'m':m,'branches':branches,'eps':eps,'maxiter':maxiter,'angle':angle,'twist':twist,'scale':scale,
  'initial':start.tolist(),'parent':par.tolist(),'final':res.x.reshape(m,3).tolist(),'message':res.message,'success':bool(res.success),'iterations':int(res.nit),
  'value':float(g['value']),'V':float(g['V']),'c':g['c'].tolist(),'minflow':float(con(res.x).min()),'census':model.census(g),'trace':trace}
 Path(f'CUT_CHAIN_B{branches}_M{m}_I{index}.json').write_text(json.dumps(report,sort_keys=True,indent=2));print('FINAL',json.dumps({k:v for k,v in report.items() if k not in ['initial','parent','final','trace']}),flush=True)
 return report

if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--index',type=int,default=0);ap.add_argument('--count',type=int,default=1);ap.add_argument('--m',type=int,default=21);ap.add_argument('--branches',type=int,default=1);ap.add_argument('--maxiter',type=int,default=200);ap.add_argument('--eps',type=float,default=1e-5);a=ap.parse_args()
 for i in range(a.index,a.index+a.count):run(i,a.m,a.maxiter,a.branches,a.eps)
```

## Complete depth_scout.py

Expected2357 bytes, SHA07e73846c7e73b064e10d65ddf375d85be8041348cd331f010cffc59a49399ba.

```python
"""Finite floating scout for the exact relaxed-depth compulsory core; no proof."""
import os
os.environ['OPENBLAS_NUM_THREADS']='1'
import argparse,hashlib,json,time
from pathlib import Path
import numpy as np
from scipy.spatial import ConvexHull
from scipy.special import roots_legendre
from scipy.optimize import minimize


def geometry(path):
 raw=json.loads(Path(path).read_text());p=np.array(raw['points'],float)/raw['grid']
 hull=ConvexHull(p);N=hull.equations[:,:3]/(-hull.equations[:,3,None])
 return p,N

def directions(n):
 z,w=roots_legendre(n);phi=np.arange(2*n)*np.pi/n
 ns=np.stack(np.broadcast_arrays(np.sqrt(1-z[:,None]**2)*np.cos(phi),np.sqrt(1-z[:,None]**2)*np.sin(phi),z[:,None]),axis=-1).reshape(-1,3)
 weights=np.broadcast_to(w[:,None]*np.pi/n,(n,2*n)).ravel()/4
 return ns,weights

def run(n=100,depths=(4,5,6,7,8,10,15,21)):
 p,N=geometry('G6.json');ns,w=directions(n)
 products=ns@N.T;rhoK=1/products.max(axis=1)
 norms=np.linalg.norm(N,axis=1)
 angles=np.arccos(np.clip(products/norms,-1,1))
 oldw=w*rhoK**4
 out=[]
 for d in depths:
  r=1/np.max(norms*np.cos(angles/(d+1))**(d+1),axis=1)
  corew=w*r**4
  def fun(z):
   h=np.r_[1.,z];a=ns@h;pos=a>0
   value=np.dot(np.where(pos,oldw,corew),a)
   grad=np.where(pos,oldw,corew)@ns
   return value,grad[1:]
  res=minimize(fun,np.array([.26,-.305]),jac=True,method='BFGS',options={'gtol':1e-11,'maxiter':200})
  h=np.r_[1.,res.x];a=ns@h
  o={'depth':d,'h':h.tolist(),'upper':float(fun(res.x)[0]),'normalized_upper':float(fun(res.x)[0]/np.linalg.norm(h)),
  'positive':float(oldw@np.maximum(a,0)),'negative':float(corew@np.minimum(a,0)),
  'old_h_upper':float(fun([.26,-.305])[0]),'success':bool(res.success),'iterations':int(res.nit),
  'core_moment':(corew@ns).tolist(),'minimum_core_radius':float(r.min()),'maximum_core_radius':float(r.max())}
  print(o,flush=True);out.append(o)
 report={'kind':'finite floating quadrature; no exact exclusion','quadrature_n':n,'sphere_points':len(ns),'rows':len(N),'G6_sha256':hashlib.sha256(Path('G6.json').read_bytes()).hexdigest(),'results':out}
 Path(f'DEPTH_SCOUT_N{n}.json').write_text(json.dumps(report,sort_keys=True,indent=2))

if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--n',type=int,default=100);ap.add_argument('--depths',type=int,nargs='+',default=[4,5,6,7,8,10,15,21]);a=ap.parse_args();run(a.n,a.depths)
```

## Continuation significance

The depth59 body bypasses the restricted shallow-depth5 mass obstruction through much deeper active polar structure. It does not contradict that theorem, and does not imply depth6 suffices. Nor is21 an unconditional cap on added planes:52 old active facets disappear in this example. Its reduced92-support representation leaves E<=270,C<=540 for any bounded full-dimensional continuation of that92-plane family, but strict S=1 must be re-established after deformation; obsolete inactive normals are not automatically valid future witnesses. The scientific remaining task is actual mass-closed removal of six unwanted physical maxima/saddles, or using this architecture as an alternative to the much thinner LOW121 body. Neither lower complexity alone nor easier arithmetic is accepted own110 progress.
