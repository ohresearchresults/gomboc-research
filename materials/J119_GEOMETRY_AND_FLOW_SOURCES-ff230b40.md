# material-ff230b40385b

AI research material

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

# J119_GEOMETRY_AND_FLOW_SOURCES.md

Complete runnable source units. Write each fenced block under its named filename, retaining its final newline. Dependencies are explicit imports. Search uses CPython3.13.5, NumPy2.3.5, SciPy1.17.0, Torch2.10.0+cpu, one thread; exact auditing uses g++14.2.0 and GMP6.3.0. Floating search/bar floors are not exact-equilibrium evidence. Exact endpoint recovery is preserved separately.

## orbit119.py

Bytes: 7405; SHA-256: 0081e019c7a52d2d7621bfe553d8f558396617bc0e37cf45f98b9245513a3750.

```python
"""Finite projective/shared-affine orbit: numerical nomination, not exact census.
T_b(x)=x/(1+b.x); A upper triangular det1, normal rows (n+b) A^-1.
The physical homogeneous mass is recomputed from the transformed boundary.
Input: complete H body with origin in its interior. The projective chart fixes
true incidences; unlike raw qhull counting, polygonal facets retain their edges.
"""
import os
os.environ.setdefault('OPENBLAS_NUM_THREADS','1')
os.environ.setdefault('OMP_NUM_THREADS','1')
import sys,json,hashlib
from pathlib import Path
import numpy as np, torch
from scipy.spatial import ConvexHull
from scipy.optimize import minimize

torch.set_num_threads(1);torch.set_default_dtype(torch.float64)

def read_h(path):
 text=Path(path).read_text()
 if str(path).endswith('.json'):return np.array(json.loads(text)['n'],float)
 a=text.splitlines();m,D=map(int,a[0].split());r=np.array([list(map(int,s.split())) for s in a[1:] if s.strip()],float)
 assert len(r)==m
 return r/D if D else r[:,:3]/r[:,3,None]

def geometry(n,apex=None):
 n=np.asarray(n,float);h=ConvexHull(n)
 assert h.equations[:,3].max()<0
 # Construct true physical vertices, grouping exact-plane numerical matches.
 vv=-h.equations[:,:3]/h.equations[:,3,None];verts=[];groups=[];mapping=[]
 from scipy.spatial.distance import pdist
 is_simple=pdist(vv).min()>1e-9
 for i,x in enumerate(vv):
  hits=[] if is_simple else [j for j,y in enumerate(verts) if np.linalg.norm(x-y)<1e-9]
  if hits:j=hits[0];groups[j].append(i)
  else:j=len(verts);verts.append(x);groups.append([i])
  mapping.append(j)
 v=np.array(verts);faces={};tet=[];edgeowners={}
 for f in h.vertices:
  ids=sorted({mapping[i] for i,t in enumerate(h.simplices) if f in t})
  nn=n[f];axis=np.eye(3)[np.argmin(abs(nn))];e=np.cross(nn,axis);e/=np.linalg.norm(e);ff=np.cross(nn,e)
  d=v[ids]-v[ids].mean(0);ids=np.array(ids)[np.argsort(np.arctan2(d@ff,d@e))].tolist()
  faces[int(f)]=ids
  for a,b in zip(ids,ids[1:]+ids[:1]):edgeowners.setdefault(tuple(sorted((a,b))),[]).append(int(f))
  for j in range(1,len(ids)-1):tet.append([ids[0],ids[j],ids[j+1]])
 pe=np.array(sorted(edgeowners),int);qe=np.array([edgeowners[tuple(e)] for e in pe],int)
 assert all(len(x)==2 for x in edgeowners.values()) and len(v)-len(pe)+len(faces)==2
 tet=np.array(tet,int);w=np.linalg.det(v[tet])/6;assert w.min()>0
 volume=w.sum();g=(w[:,None]*v[tet].sum(1)/4).sum(0)/volume
 assert np.max(v@n.T-1)<1e-8
 return dict(n=n,v=v,faces=faces,pe=pe,qe=qe,tet=tet,w=w,volume=volume,g=g,triples=np.array([h.simplices[grp[0]] for grp in groups],int))

def scores(x):
 sq=np.einsum('ij,ij->i',x,x);a=x@x.T/sq[:,None]-1;np.fill_diagonal(a,-np.inf)
 return a.max(1),a.argmax(1)

def bars(x,edges):
 sq=np.einsum('ij,ij->i',x,x);d=x[edges[:,1]]-x[edges[:,0]]
 t=np.clip(-np.einsum('ij,ij->i',x[edges[:,0]],d)/np.einsum('ij,ij->i',d,d),0,1)
 z=x[edges[:,0]]+t[:,None]*d;level=np.einsum('ij,ij->i',z,z)
 par=np.arange(len(x));out=[]
 def find(i):
  while par[i]!=i:par[i]=par[par[i]];i=par[i]
  return i
 for k in sorted(range(len(edges)),key=lambda k:(-level[k],tuple(edges[k]))):
  i,j=map(int,edges[k]);a,b=find(i),find(j)
  if a==b:continue
  if (sq[a],-a)<(sq[b],-b):a,b=b,a
  dep=1-level[k]/sq[b]
  if dep>0:out.append([float(dep),int(b),[i,j],float(sq[b]),float(level[k])])
  par[b]=a
 return sorted(out,reverse=True)

class Orbit:
 def __init__(self,n):
  self.geo=geometry(n);self.n=torch.tensor(n);self.v=torch.tensor(self.geo['v']);self.w=torch.tensor(self.geo['w']);self.tet=self.geo['tet']
 def tensors(self,z):
  b=z[:3];a,c,s,t,u=z[3:]
  zz=z[0]*0;A=torch.stack((torch.stack((torch.exp(a),s,t)),torch.stack((zz,torch.exp(c),u)),torch.stack((zz,zz,torch.exp(-a-c)))))
  den=1+self.v@b;v=self.v/den[:,None]
  w=self.w/den[self.tet].prod(1);V=w.sum();g=(w[:,None]*v[self.tet].sum(1)/4).sum(0)/V
  p=(v-g)@A.T;nn=self.n+b;q=torch.linalg.solve(A.T,(nn/(1-nn@g)[:,None]).T).T
  return p,q,g,V,A,den
 def evaluate(self,z):
  with torch.no_grad():arr=self.tensors(torch.tensor(z))
  p,q,g,V,A,den=[x.numpy() for x in arr];pc,pw=scores(p);qc,qw=scores(q);P=bars(p,self.geo['pe']);Q=bars(q,self.geo['qe'])
  pr=int(np.argmax(np.sum(p*p,1)));qr=int(np.argmax(np.sum(q*q,1)))
  return dict(z=list(map(float,z)),A=A.tolist(),n=((self.geo['n']+z[:3])@np.linalg.inv(A)).tolist(),g=(A@g).tolist(),volume=float(V),VEF=[len(p),len(self.geo['pe']),len(self.geo['faces'])],P=P,Q=Q,S=np.where(qc<-1e-10)[0].tolist(),U=np.where(pc<-1e-10)[0].tolist(),minp=float(np.min(np.delete(pc,pr))),minq=float(np.min(np.delete(qc,qr))),denmin=float(den.min()))
 def constraints(self,z,permitted_q,tau,rootpolicy='dynamic'):
  p,q,g,V,A,den=self.tensors(z)
  psq=(p*p).sum(1);qsq=(q*q).sum(1)
  pa=p@p.T/psq[:,None]-1;qa=q@q.T/qsq[:,None]-1
  pa=pa-torch.eye(len(p))*1e4;qa=qa-torch.eye(len(q))*1e4
  cp=pa.max(1).values;cq=qa.max(1).values
  pr=int(psq.detach().argmax());qr=int(qsq.detach().argmax())
  ip=[i for i in range(len(p)) if i!=pr];allowed=set(permitted_q) if isinstance(permitted_q,(list,tuple,set)) else {qr,permitted_q};iq=[i for i in range(len(q)) if i not in allowed]
  return torch.cat((cp[ip]-tau,cq[iq]-tau,den-.2))
 def qloss(self,z,root,edge):
  p,q,*_=self.tensors(z);a,b=edge;d=q[b]-q[a];t=torch.clamp(-(q[a]@d)/(d@d),0,1);v=q[a]+t*d
  return 1-(v@v)/(q[root]@q[root])

def run(inp,out,kind='sqp',count=20,tau=1e-9):
 orb=Orbit(read_h(inp));z=np.zeros(8);hist=[];best=orb.evaluate(z);Path(out+'.base.json').write_text(json.dumps(best,indent=2)+'\n')
 rng=np.random.default_rng(11928)
 for it in range(count):
  cur=orb.evaluate(z);qb=[b for b in cur['Q'] if b[0]>1e-12]
  if not qb:print('NUMERICAL_TARGET_NOMINATION',cur,flush=True);break
  root,edge=qb[0][1:3];calls=0
  with torch.no_grad():q0=orb.tensors(torch.tensor(z))[1]
  allowed=(root,int((q0*q0).sum(1).argmax()))
  if kind=='sqp':
   def fun(x):
    zz=torch.tensor(x,requires_grad=True);loss=orb.qloss(zz,root,edge);loss.backward();return float(loss.detach()),zz.grad.numpy()
   def con(x):return orb.constraints(torch.tensor(x),allowed,tau).detach().numpy()
   def jac(x):return torch.autograd.functional.jacobian(lambda y:orb.constraints(y,allowed,tau),torch.tensor(x),vectorize=True,strategy='forward-mode').detach().numpy()
   r=.05 if it%3 else .2;bounds=[(z[i]-r,z[i]+r) for i in range(8)]
   res=minimize(fun,z,jac=True,method='SLSQP',bounds=bounds,constraints=[dict(type='ineq',fun=con,jac=jac)],options=dict(maxiter=100,ftol=1e-12,disp=False))
   cand=orb.evaluate(res.x);margin=float(np.min(con(res.x)));ok=margin>=-1e-10 and len(cand['U'])==1 and len(cand['S'])<=2 and cand['Q'][0][0]<qb[0][0]-1e-10
   row=dict(iteration=it,status=int(res.status),message=str(res.message),nit=res.nit,margin=margin,accepted=ok,body=cand);hist.append(row)
   print('ORBIT_SQP',it,res.status,res.nit,margin,len(cand['S']),len(cand['U']),cand['Q'][0][0],ok,flush=True)
   if ok:z=res.x;best=cand;Path(out).write_text(json.dumps(best,indent=2)+'\n')
   elif it>=2:break
  else:raise ValueError(kind)
 Path(out+'.history.json').write_text(json.dumps(hist,indent=2)+'\n')
 print('ORBIT119_COMPLETE',out,len(hist),max((q[0] for q in best['Q']),default=0),flush=True)
 return best

if __name__=='__main__':
 if len(sys.argv)>2:run(sys.argv[1],sys.argv[2],count=int(sys.argv[3]) if len(sys.argv)>3 else 20,tau=float(sys.argv[4]) if len(sys.argv)>4 else 1e-9)
 else:
  orb=Orbit(read_h(sys.argv[1]));print(json.dumps(orb.evaluate(np.zeros(8)),indent=2))
```

## prune119.py

Bytes: 2731; SHA-256: c1ee5772efc418e603132c88e24b0ddfa2cd25d255a074b56b63a09227484057.

```python
"""Executed feature-retirement beam on the literal KL13 H80 own211 input.
All count filters are numerical and all outputs are nominations only.
"""
import json,sys,time
from pathlib import Path
import numpy as np
from scipy.spatial import ConvexHull,QhullError
from orbit119 import geometry,scores,bars,read_h

def stats(n):
 G=geometry(n);active=sorted(G['faces']);remap={a:i for i,a in enumerate(active)};qe=np.array([[remap[int(a)],remap[int(b)]] for a,b in G['qe']],int);p=G['v']-G['g'];an=n[active];q=an/(1-an@G['g'])[:,None];pc,pw=scores(p);qc,qw=scores(q)
 P=bars(p,G['pe']);Q=bars(q,qe);pr=int(np.argmax(np.sum(p*p,1)));qr=int(np.argmax(np.sum(q*q,1)));qq=int(Q[0][1]) if Q else qr
 minp=float(np.min(np.delete(pc,pr)));iq=[i for i in range(len(q)) if i not in {qr,qq}];minq=float(np.min(qc[iq])) if iq else 1
 return dict(active=active,VEF=[len(p),len(G['pe']),len(q)],S=[active[int(i)] for i in np.where(qc<-1e-10)[0]],U=np.where(pc<-1e-10)[0].tolist(),P=P,Q=Q,minp=minp,minq=minq,volume=G['volume'],g=G['g'].tolist())

def main(inp,out,maxsteps=18,beamwidth=3):
 n=read_h(inp);base=list(range(len(n)));seen={tuple(base)};beam=[dict(keep=base,c=stats(n))];ledger=[dict(step=0,beam=beam)];start=time.time();tested=0
 for step in range(1,maxsteps+1):
  good=[];allrec=[]
  for par in beam:
   for i in par['keep']:
    keep=tuple(j for j in par['keep'] if j!=i)
    if keep in seen:continue
    seen.add(keep);tested+=1
    try:c=stats(n[list(keep)])
    except (ValueError,AssertionError,QhullError,np.linalg.LinAlgError):continue
    row=dict(keep=list(keep),deleted=i,c=c)
    ok=(len(c['U'])==1 and len(c['S'])<=2 and c['minp']>1e-7 and c['minq']>1e-7 and max((b[0] for b in c['P']),default=0)<1e-12 and len([b for b in c['Q'] if b[0]>1e-12])<=1)
    allrec.append(dict(deleted=i,keep=list(keep),Q=max((b[0] for b in c['Q']),default=0),S=len(c['S']),U=len(c['U']),minp=c['minp'],minq=c['minq'],ok=ok))
    if ok:good.append(row)
  good.sort(key=lambda r:max((b[0] for b in r['c']['Q']),default=0));beam=good[:beamwidth]
  ledger.append(dict(step=step,tested=tested,good=len(good),beam=beam,trials=allrec));Path(out).write_text(json.dumps(dict(input=inp,seconds=time.time()-start,ledger=ledger),indent=2)+'\n')
  print('PRUNE119',step,'tested',tested,'good',len(good),'Q',[r['c']['Q'][0][0] if r['c']['Q'] else 0 for r in beam],'seconds',time.time()-start,flush=True)
  if not beam:break
  for k,row in enumerate(beam):Path(out+f'.step{step}.rank{k}.json').write_text(json.dumps(dict(n=n[row['keep']].tolist(),**row),indent=2)+'\n')
 print('PRUNE119_FINISHED',tested,flush=True)
if __name__=='__main__':main(sys.argv[1],sys.argv[2],int(sys.argv[3]) if len(sys.argv)>3 else 18,int(sys.argv[4]) if len(sys.argv)>4 else 3)
```

## apex_flow119.py

Bytes: 7367; SHA-256: 9c54217b5e02ae71f5c41fe50a05d62f940e40bfe972c348e00ab6a4b82355ad.

```python
"""Actual-mass free-normal chart with a persistent high-degree physical apex.
M input planes, K constrained through apex a. Other planes obey n.a<1 via
an exponential height coordinate. For every admissible hull, true
E <= 3M-K-3: redundant ordinary/apex supports only lower the upper bound.
This is a floating search. Neither its bar floor nor a small loss certifies110.
"""
import os
os.environ.setdefault('OPENBLAS_NUM_THREADS','1');os.environ.setdefault('OMP_NUM_THREADS','1')
import sys,json,time
from pathlib import Path
import numpy as np,torch
from scipy.optimize import minimize
from scipy.spatial import QhullError
from orbit119 import geometry,scores,bars
from prune119 import stats

torch.set_num_threads(1);torch.set_default_dtype(torch.float64)

class ApexChart:
 def __init__(self,n,a):
  G=geometry(n);active=sorted(G['faces']);self.n=np.asarray(n)[active];self.a=np.asarray(a);self.ss=self.a@self.a;self.c=self.a/self.ss
  axis=np.eye(3)[np.argmin(abs(self.a))];self.e=np.cross(self.a,axis);self.e/=np.linalg.norm(self.e);self.f=np.cross(self.a,self.e);self.f/=np.linalg.norm(self.f)
  self.ap=np.where(abs(self.n@self.a-1)<1e-7)[0];self.op=np.array([i for i in range(len(self.n)) if i not in self.ap],int);assert len(self.ap)>=3
  self.M=len(self.n);self.K=len(self.ap);assert (1-self.n[self.op]@self.a).min()>0
  self.initial=np.concatenate([(self.n[self.ap]@np.stack([self.e,self.f],axis=1)).ravel(),np.column_stack([self.n[self.op]@self.e,self.n[self.op]@self.f,np.log(1-self.n[self.op]@self.a)]).ravel()])
  self.tc=torch.tensor(self.c);self.te=torch.tensor(self.e);self.tf=torch.tensor(self.f);self.ta=torch.tensor(self.a)
 def normals(self,z):
  ap=z[:2*self.K].reshape(-1,2);op=z[2*self.K:].reshape(-1,3)
  n=torch.empty((self.M,3),dtype=z.dtype)
  n[self.ap]=self.tc+ap[:,0,None]*self.te+ap[:,1,None]*self.tf
  n[self.op]=(1-torch.exp(op[:,2,None]))*self.tc+op[:,0,None]*self.te+op[:,1,None]*self.tf
  return n
 def tensors(self,z,G):
  n=self.normals(z);v=torch.linalg.solve(n[G['triples']],torch.ones((len(G['v']),3,1))).squeeze(-1)
  ai=int(np.argmin(np.linalg.norm(G['v']-self.a,axis=1)));assert np.linalg.norm(G['v'][ai]-self.a)<1e-7
  v=v.clone();v[ai]=self.ta
  tet=v[G['tet']];w=torch.linalg.det(tet)/6;volume=w.sum();g=(w[:,None]*tet.sum(1)/4).sum(0)/volume
  p=v-g;active=sorted(G['faces']);nn=n[active];q=nn/(1-nn@g)[:,None]
  remap={i:j for j,i in enumerate(active)};qe=np.array([[remap[int(a)],remap[int(b)]] for a,b in G['qe']],int)
  return n,p,q,g,volume,ai,qe

def main(inp,out,maxiter=900,mode='bars',weight=.02,tau=1e-5):
 r=json.load(open(inp));n=np.array(r['n']);a=np.array(r['apex']);ch=ApexChart(n,a);x=ch.initial.copy();start=time.time();hist=[];best=np.inf;calls=0;success=0
 prefix=Path(out);prefix.parent.mkdir(parents=True,exist_ok=True)
 def save(z,G,p,q,g,V,loss,label):
  nr=ch.normals(torch.tensor(z)).detach().numpy();s=stats(nr);s.update(n=nr.tolist(),apex=a.tolist(),parameters=list(map(float,z)),M=ch.M,K=ch.K,E_upper=3*ch.M-ch.K-3,mode=mode,weight=weight,tau=tau,loss=loss,calls=calls)
  Path(str(prefix)+label+'.json').write_text(json.dumps(s,indent=2)+'\n')
 def fg(flat):
  nonlocal calls,best,success
  calls+=1;z=torch.tensor(flat,requires_grad=True)
  try:
   n=ch.normals(z);nf=n.detach().numpy();G=geometry(nf);assert len(G['pe'])<=3*ch.M-ch.K-3
   n,p,q,g,V,ai,qe=ch.tensors(z,G)
   p0=p.detach().numpy();q0=q.detach().numpy();P=[b for b in bars(p0,G['pe']) if b[0]>1e-10];Q=[b for b in bars(q0,qe) if b[0]>1e-10]
   ps=(p*p).sum(1);qs=(q*q).sum(1);qr=int(qs.detach().argmax());pa=p@p.T/ps[:,None]-1;qa=q@q.T/qs[:,None]-1
   pa=pa-torch.eye(len(p))*1e4;qa=qa-torch.eye(len(q))*1e4;cp=pa.max(1).values;cq=qa.max(1).values
   ip=np.array([i for i in range(len(p)) if i!=ai]);iq=np.array([i for i in range(len(q)) if i!=qr]);guards=torch.cat([cp[ip],cq[iq]])
   penalty=torch.clamp(tau-guards,min=0).square().sum()
   energy=z.sum()*0
   for xx,bb in [(p,P),(q,Q)]:
    for dep,root,ed,birth,death in bb:
     u,v=ed;d=xx[v]-xx[u];t=torch.clamp(-(xx[u]@d)/(d@d),0,1);foot=xx[u]+t*d;D=1-(foot@foot)/(xx[root]@xx[root]);energy=energy+torch.clamp(D,min=0)
   if mode=='bars':loss=energy+weight*penalty
   elif mode=='guards':loss=penalty+weight*energy
   elif mode.startswith('barrier'):
    ep=1e-7;allowedp={int(ps.detach().argmax())};allowedq={qr}
    if P:allowedp.add(int(P[0][1]))
    if Q:allowedq.add(int(Q[0][1]))
    gi=torch.cat([cp[[i for i in range(len(p)) if i not in allowedp]],cq[[i for i in range(len(q)) if i not in allowedq]]]);safe=torch.clamp(gi,min=ep);below=(gi-ep)/ep
    barrier=torch.where(gi>=ep,-torch.log(safe),-np.log(ep)-below+.5*below*below).sum();loss=weight*barrier
    for name,xx,bb in [('P',p,P),('Q',q,Q)]:
     if bb and (mode=='barrierBoth' or mode=='barrier'+name):
      dep,root,ed,birth,death=bb[0];u,v=ed;d=xx[v]-xx[u];t=torch.clamp(-(xx[u]@d)/(d@d),0,1);foot=xx[u]+t*d;loss+=1-(foot@foot)/(xx[root]@xx[root])
   elif mode=='sqrt':
    loss=penalty*weight
    for xx,bb in [(p,P),(q,Q)]:
     for dep,root,ed,birth,death in bb:
      u,v=ed;d=xx[v]-xx[u];t=torch.clamp(-(xx[u]@d)/(d@d),0,1);foot=xx[u]+t*d;D=torch.clamp(1-(foot@foot)/(xx[root]@xx[root]),min=0);loss+=torch.sqrt(D+1e-12)-1e-6
   else:raise ValueError(mode)
   loss.backward();val=float(loss.detach());grad=z.grad.detach().numpy()
   if not np.isfinite(val) or not np.isfinite(grad).all():raise ValueError('nonfinite objective')
   SU=[int((cq.detach().numpy()<-1e-10).sum()),int((cp.detach().numpy()<-1e-10).sum())]
   rec=dict(call=calls,loss=val,energy=float(energy.detach()),penalty=float(penalty.detach()),S=SU[0],U=SU[1],P=len(P),Q=len(Q),maxP=max((b[0] for b in P),default=0),maxQ=max((b[0] for b in Q),default=0),VEF=[len(p),len(G['pe']),len(q)],minguard=float(guards.detach().min()),seconds=time.time()-start);hist.append(rec)
   if val<best:
    best=val
    if calls%10==0 or best<1e-5:save(flat,G,p0,q0,g,V,val,'.best')
   if SU==[1,1] and float(guards.detach().min())>1e-8:
    success+=1;save(flat,G,p0,q0,g,V,val,f'.nomination{success}')
   if calls%25==0:print('APEX_FLOW119',rec,flush=True);Path(str(prefix)+'.history.json').write_text(json.dumps(hist,indent=2)+'\n')
   return val,grad
  except (ValueError,AssertionError,QhullError,np.linalg.LinAlgError,RuntimeError) as e:
   if calls%25==0:print('APEX_FLOW_REJECT',calls,type(e).__name__,str(e),flush=True)
   return 1e6,np.zeros_like(flat)
 bounds=[]
 for i,z in enumerate(x):bounds.append((z-2,z+2))
 res=minimize(fg,x,jac=True,method='L-BFGS-B',bounds=bounds,options=dict(maxiter=maxiter,maxls=35,maxcor=25,ftol=1e-14,gtol=1e-9))
 nr=ch.normals(torch.tensor(res.x)).detach().numpy();s=stats(nr);s.update(n=nr.tolist(),apex=a.tolist(),parameters=res.x.tolist(),M=ch.M,K=ch.K,E_upper=3*ch.M-ch.K-3,mode=mode,weight=weight,tau=tau,status=int(res.status),message=str(res.message),iterations=int(res.nit),calls=calls)
 Path(str(prefix)+'.last.json').write_text(json.dumps(s,indent=2)+'\n');Path(str(prefix)+'.history.json').write_text(json.dumps(hist,indent=2)+'\n');print('APEX_FLOW119_COMPLETE',res.status,res.nit,calls,best,'SU',[len(s['S']),len(s['U'])],'VEF',s['VEF'],flush=True)
if __name__=='__main__':main(sys.argv[1],sys.argv[2],int(sys.argv[3]) if len(sys.argv)>3 else 900,sys.argv[4] if len(sys.argv)>4 else 'bars',float(sys.argv[5]) if len(sys.argv)>5 else .02,float(sys.argv[6]) if len(sys.argv)>6 else 1e-5)
```

## free_flow119.py

Bytes: 2182; SHA-256: 84783d3f51b22d2c6320222c253b6948f381975f851b22000c6ef0f25a2b4e3b.

```python
"""Release the high-degree apex: all currently active H rows become free.
This is a different physical family, not the common-apex chart. Its sufficient
bound is E<=3M-6, M<=85. The input apex is only an inherited coordinate marker.
Complete dependency: apex_flow119.py, orbit119.py and prune119.py.
Use python free_flow119.py INPUT.json PREFIX ITERATIONS barrierBoth 0.00001 SEED.
"""
import json,sys
from pathlib import Path
import numpy as np,torch
import apex_flow119 as F
from orbit119 import geometry

class FreeHChart:
 def __init__(self,n,a):
  G=geometry(n);self.n=np.asarray(n)[sorted(G['faces'])];self.M=len(self.n);assert self.M<=85
  self.K=0;self.initial=self.n.ravel().copy();self.a=np.asarray(a)
 def normals(self,z):return z.reshape(self.M,3)
 def tensors(self,z,G):
  n=self.normals(z);v=torch.linalg.solve(n[G['triples']],torch.ones((len(G['v']),3,1))).squeeze(-1)
  tet=v[G['tet']];w=torch.linalg.det(tet)/6;volume=w.sum();g=(w[:,None]*tet.sum(1)/4).sum(0)/volume
  p=v-g;active=sorted(G['faces']);nn=n[active];q=nn/(1-nn@g)[:,None]
  remap={i:j for j,i in enumerate(active)};qe=np.array([[remap[int(a)],remap[int(b)]] for a,b in G['qe']],int)
  assert len(G['pe'])<=3*self.M-6
  return n,p,q,g,volume,int((p.detach()*p.detach()).sum(1).argmax()),qe

def main(inp,out,iterations,mode,weight,seed):
 r=json.loads(Path(inp).read_text());n=np.array(r['n']);G=geometry(n);n=n[sorted(G['faces'])]
 rng=np.random.default_rng(seed);n=n+1e-5*rng.normal(size=n.shape)
 start=dict(n=n.tolist(),apex=r['apex'],seed=seed,jitter=1e-5,chart='free_H',parent_input=inp)
 ip=out+'.release_input.json';Path(ip).write_text(json.dumps(start,indent=2)+'\n')
 F.ApexChart=FreeHChart;F.main(ip,out,iterations,mode,weight,1e-5)
 for suffix in ['.last.json','.best.json']:
  path=Path(out+suffix)
  if path.exists():
   a=json.loads(path.read_text());a['inherited_anchor']=a.pop('apex',None);a['chart']='free_H';a['E_upper']=3*a['M']-6;a['seed']=seed;a['jitter']=1e-5
   path.write_text(json.dumps(a,indent=2)+'\n')
 print('FREE_H_RELEASE119_COMPLETE',out,flush=True)
if __name__=='__main__':main(sys.argv[1],sys.argv[2],int(sys.argv[3]),sys.argv[4],float(sys.argv[5]),int(sys.argv[6]))
```

## primal_relay119.py

Bytes: 3724; SHA-256: 3cec747417e76711627ac3ae38ebf9888de1ff318127d38f801a79bbe0d8ddec.

```python
"""Finite physical convex-hull relays on current own-centred input geometry.
Every endpoint is re-hulled at its new actual uniform centre. Counts and bars
are numerical only. Only E<=249 proposals are retained. This is not an exclusion.
"""
import json,sys,time
from pathlib import Path
import numpy as np
from scipy.spatial import ConvexHull,QhullError
from orbit119 import geometry,bars,scores
from prune119 import stats

def normals(v):
 h=ConvexHull(v);assert h.equations[:,3].max()<0
 rows=-h.equations[:,:3]/h.equations[:,3,None];out=[]
 for n in rows:
  if not any(np.linalg.norm(n-x)<1e-8 for x in out):out.append(n)
 return np.array(out)

def arc(u,z,links,power,bow,long):
 ru=np.linalg.norm(u);rz=np.linalg.norm(z);e=u/ru;v=z/rz;co=np.clip(e@v,-1,1);theta=np.arccos(co);f=v-co*e;f/=np.linalg.norm(f);h=np.cross(e,f)
 if long:theta=2*np.pi-theta;f=-f
 t=np.linspace(0,1,links+1);dirs=np.cos(theta*t)[:,None]*e+np.sin(theta*t)[:,None]*f+bow*np.sin(np.pi*t)[:,None]*h
 dirs/=np.linalg.norm(dirs,axis=1)[:,None];cos=np.einsum('ij,ij->i',dirs[:-1],dirs[1:]);assert cos.min()>0
 costs=np.r_[0,np.cumsum(-np.log(cos))];slack=np.log(rz/ru)-costs[-1];assert slack>0
 r=ru*np.exp(costs+slack*t**power);w=r[:,None]*dirs;assert np.min(np.einsum('ij,ij->i',w[:-1],w[1:]-w[:-1]))>0
 return w[1:-1]

def main(inp,out):
 base=json.loads(Path(inp).read_text());n=np.array(base['n']);G=geometry(n);g=G['g'];v=G['v'];p=v-g;P=bars(p,G['pe']);root=P[0][1];elder=int(np.argmax(np.sum(p*p,1)))
 out=Path(out);out.mkdir(exist_ok=True);ledger=[];best=1e6;count=0;start=time.time();saved=0
 # Elder component in the complete nonlocal positive-chord graph.
 sc=p@p.T-np.sum(p*p,1)[:,None];reach={elder}
 while True:
  add={i for i in range(len(p)) if any(sc[i,j]>1e-10 for j in reach)}-reach
  if not add:break
  reach|=add
 candidates=[]
 for j in reach:
  R=np.linalg.norm(p[j])/np.linalg.norm(p[root]);phi=np.arccos(np.clip((p[j]@p[root])/(np.linalg.norm(p[j])*np.linalg.norm(p[root])),-1,1))
  if R<=1:continue
  needed=next((k for k in range(1,65) if phi/k<np.pi/2 and R*np.cos(phi/k)**k>1+1e-5),None)
  if needed is not None:candidates.append((needed,phi,j))
 endpoints=[j for _,_,j in sorted(candidates)[:4]]
 if elder not in endpoints:endpoints.append(elder)
 for target in endpoints:
  for links in [6,10,14,18]:
   for power in [.5,1.,2.]:
    for bow in [0.,-.35,.35]:
     for long in [False,True]:
      try:
       w=arc(p[root],p[target],links,power,bow,long)+g;nn=normals(np.vstack([v,w]));s=stats(nn);count+=1
       Pp=[x for x in s['P'] if x[0]>1e-10];Qq=[x for x in s['Q'] if x[0]>1e-10];energy=sum(x[0] for x in Pp+Qq)
       rec=dict(target=target,links=links,power=power,bow=bow,long=long,VEF=s['VEF'],S=len(s['S']),U=len(s['U']),P=len(Pp),Q=len(Qq),sum=energy,maxP=max([b[0] for b in Pp],default=0),maxQ=max([b[0] for b in Qq],default=0));ledger.append(rec)
       if s['VEF'][1]<=249 and (energy<best or len(s['U'])==1 or len(s['S'])==1):
        if energy<best:best=energy;label='best'
        else:saved+=1;label='one_sided'+str(saved)
        s.update(n=nn.tolist(),old_normals=n.tolist(),added_material_points=w.tolist(),parent_input=inp,recipe=rec,old_g=g.tolist());(out/(label+'.json')).write_text(json.dumps(s,indent=2)+'\n');print('PRIMAL_RELAY119_KEEP',label,rec,flush=True)
      except (AssertionError,ValueError,QhullError,np.linalg.LinAlgError):continue
 (out/'ledger.json').write_text(json.dumps(dict(parent=inp,parent_root=root,parent_elder=elder,endpoint_candidates=candidates,selected_endpoints=endpoints,seconds=time.time()-start,ledger=ledger),indent=2)+'\n')
 print('PRIMAL_RELAY119_COMPLETE',count,'best',best,'one_sided',saved,flush=True)
if __name__=='__main__':main(sys.argv[1],sys.argv[2])
```

## vertex_flow119.py

Bytes: 2509; SHA-256: 606c171357dc3dfb7de12de49dbb66e9944177fc8e39eed0ca541170806fdb69.

```python
"""Physical material-point release after a current whole-P relay proposal.
Greedy actual-mass retirement first enforces N<=85, hence true E<=249 for EVERY
subsequent hull. Normals are differentiated through their active material triples.
Dependencies: free_flow119.py, apex_flow119.py, orbit119.py, prune119.py,
primal_relay119.py. All search/bar floors are numerical; exact census is separate.
"""
import json,sys
from pathlib import Path
import numpy as np,torch
from scipy.spatial import ConvexHull
import apex_flow119 as F
from free_flow119 import FreeHChart
from orbit119 import geometry
from prune119 import stats
from primal_relay119 import normals

class VChart(FreeHChart):
 def __init__(self,n,a):
  G=geometry(n);self.v=G['v'];self.M=len(self.v);assert self.M<=85
  self.K=0;self.initial=self.v.ravel().copy();self.a=np.asarray(a)
 def normals(self,z):
  v=z.reshape(self.M,3);h=ConvexHull(v.detach().numpy());assert h.equations[:,3].max()<0
  vv=v[h.simplices];cross=torch.linalg.cross(vv[:,1]-vv[:,0],vv[:,2]-vv[:,0]);n=cross/(cross*vv[:,0]).sum(1)[:,None]
  nf=n.detach().numpy();keep=[]
  for i,x in enumerate(nf):
   if not any(np.linalg.norm(x-nf[j])<1e-9 for j in keep):keep.append(i)
  return n[keep]

def main(inp,out,iterations,mode,weight):
 r=json.loads(Path(inp).read_text());v=geometry(np.array(r['n']))['v'];deletions=[]
 while len(v)>85:
  cand=[]
  for i in range(len(v)):
   w=np.delete(v,i,axis=0)
   try:
    nn=normals(w);s=stats(nn);energy=sum(x[0] for x in s['P']+s['Q'] if x[0]>1e-10)
   except (ValueError,AssertionError,np.linalg.LinAlgError):continue
   cand.append((energy,i,nn,s))
  energy,i,nn,s=min(cand,key=lambda x:x[0]);deletions.append(dict(index=i,point=v[i].tolist(),energy=energy,VEF=s['VEF']));v=geometry(nn)['v']
 nn=normals(v);g=geometry(nn)['g'];a=v[np.argmax(np.sum((v-g)**2,1))]
 ip=out+'.release_input.json';Path(ip).write_text(json.dumps(dict(n=nn.tolist(),apex=a.tolist(),parent_input=inp,retirement=deletions),indent=2)+'\n')
 F.ApexChart=VChart;F.main(ip,out,iterations,mode,weight,1e-5)
 for suffix in ['.last.json','.best.json']:
  p=Path(out+suffix)
  if p.exists():
   s=json.loads(p.read_text());s['inherited_anchor']=s.pop('apex',None);s['chart']='free_V';s['E_upper']=3*s['M']-6;s['material_points']=np.array(s['parameters']).reshape(-1,3).tolist();p.write_text(json.dumps(s,indent=2)+'\n')
 print('VERTEX_FLOW119_COMPLETE',out,flush=True)
if __name__=='__main__':main(sys.argv[1],sys.argv[2],int(sys.argv[3]),sys.argv[4],float(sys.argv[5]))
```
