# material-9f342a03be76

AI research material

---

# Recovery capsule part 1/3 — J69 paired-bar shape methods

Object family: J69 finite-shape continuation from the literal JOINT56 L18 input. No object in this capsule is strict own110. Canonical C622 is unchanged. Part 1 preserves complete runnable search sources and literal initial data; part 2 contains an exact auditor and two rational own222/weak000 endpoints; part 3 preserves the six floating checkpoints and numerical observations. Parts 1+2 suffice to reconstruct and audit the rational endpoints without any earlier sandbox. Do not treat omitted optimizer progress logs as endpoint data.

The two import-only recovery edits are exact: shapeopt.py imports j69_input instead of l18; constrained.py imports search69 instead of shapeopt. j69_input.py is the complete input generator used by the searches; unused old analysis helpers have no recovery dependency. There is no random seed. Numeric environment observed during preservation: Python 3.13.5, NumPy 2.3.5, SciPy 1.17.0, PyTorch 2.10.0+cpu, Numba 0.65.1. OPENBLAS_NUM_THREADS=1 and OMP_NUM_THREADS=1; Torch float64, one thread. Floating facet grouping rounds normalized Qhull equations to nine decimals; bar cutoff is 1e-14; floating census thresholds are stated in code. None of these is an exact certificate.

## Reconstruction
Save all three material texts unchanged. Extract every file section from each text with this command (replace the three filenames only):

```python
import pathlib,re
for source in ['part1.md','part2.md','part3.md']:
    text=pathlib.Path(source).read_text()
    for name,body in re.findall(r'^## File: ([^\n]+)\n```[^\n]*\n(.*?)^```\n',text,re.M|re.S):
        p=pathlib.Path(name);p.parent.mkdir(parents=True,exist_ok=True);p.write_text(body)
```

Recorded search commands (explicit settings; unspecified settings are the defaults in search69.py):

```sh
OPENBLAS_NUM_THREADS=1 python search69.py --steps 200 --power 2 --radius .12 --folder replay_opt1
OPENBLAS_NUM_THREADS=1 python search69.py --steps 900 --power -2 --radius .3 --folder replay_escape1
OPENBLAS_NUM_THREADS=1 python search69.py --steps 1800 --power .5 --radius .3 --folder replay_half1
OPENBLAS_NUM_THREADS=1 python search69.py --steps 1800 --power 1 --radius .3 --folder replay_linear1
OPENBLAS_NUM_THREADS=1 python search69.py --steps 1800 --power .5 --radius .3 --free --folder replay_freehalf1
OPENBLAS_NUM_THREADS=1 python protect69.py --steps 600 --trust .002 --folder replay_protected1
```

The protected run ended at a bounded tool execution without a CONSTRAINED_END marker. Logs were observed through iteration30, and its later saved checkpoint was separately loaded and audited. Completion of600 iterations or optimizer convergence is NOT asserted. Literal checkpoints in part3, rather than a claim of bit-identical numerical optimization across platforms, define the reported endpoints. `BEST_CENSUS` and `CONSTRAINED_END` are search terminal markers, not proof of110. Exact proof commands and expected markers are in part2.

## Source manifest
j69_input.py: 1691 bytes, SHA-256 74e1955156a9faef4054125d00375700e76b360aef4208806344084dce790413

search69.py: 7132 bytes, SHA-256 89e460cc72e9a96b622c493e76dc6312d1cbd302c1f125f2cf00ab54a418e289

protect69.py: 4246 bytes, SHA-256 d32d107880d5e47fd750c313d991cd6284d44a50036733cc16d01e4d1e01ce3f

## File: j69_input.py
```python
"""Literal JOINT56 L18 recovery input; 75 vertices, exact plane projection."""
import numpy as np
ROWS='''-114525 0 2815
-114408 0 -21012
-110220 0 -38817
-102074 0 -55623
-95244 0 65065
-93745 0 -67376
-84871 0 89483
-83812 0 -77505
-76508 0 -83525
-64581 0 -90582
-61476 25894 -14839
-62395 23368 463
-56261 23741 8340
-52412 0 -95480
-51315 23453 14016
-52494 34497 -19706
-42771 21590 23057
-42863 2890 42398
-41427 18386 27657
-41360 12530 33866
-41047 44227 -22695
-39278 42001 -8155
-34778 0 -100114
-33227 5517 41437
-34030 41543 3065
-32655 47126 -31146
-27505 0 -101349
-26092 6359 40643
-29349 -3094 46727
-23601 48813 -36091
-20202 0 -101916
-22835 44187 7116
-19759 39126 14237
-15413 37019 17653
-12669 0 -101808
-11758 47157 -43142
-9937 36825 18784
-5171 0 -100970
-4354 45931 -43781
-656 39016 17643
-285 7861 35467
2454 -27623 -99473
1609 5616 35659
7524 7250 33248
9975 -29293 -97278
8760 16281 29866
12615 42039 15586
23787 44736 -31885
17334 -30836 -94391
30460 -17220 -87918
24468 -32254 -90824
38470 40587 -9618
31322 -33549 -86591
29555 47228 10455
33038 0 -80951
37731 -34969 -81714
36888 40349 12838
41804 34722 13816
43728 -36211 -76251
41605 0 -68494
44676 31334 13390
47360 27874 12796
49134 -37619 -70267
49897 24291 12029
52973 -47543 -55156
53765 -8364 -59155
55076 17110 8707
59503 9479 4527
58901 -42244 -45006
63005 1560 -490
63029 -35973 -35698
65329 -6139 -5970
66608 -13854 -12187
65610 -28928 -27007
66746 -21494 -19185'''
Q=np.array([[int(k) for k in row.split()] for row in ROWS.splitlines()],dtype=np.int64)
PATCH=np.array([0,1,2,3,4,5,6,7,8,9,13,22,26,30,34,37,54,59])
I=Q*1000
I[PATCH,1]=-272*Q[PATCH,0]-409*Q[PATCH,2]-68526367
D=100000000
X=I/D

```

## File: search69.py
```python
"""Own-centroid persistent-bar shape descent from the exact JOINT56 L18 input.
Exploratory floating optimizer; NOT a strict-equilibrium certificate.
"""
import os, time, json, argparse
os.environ.setdefault('OMP_NUM_THREADS','1')
import numpy as np
from scipy.spatial import ConvexHull, QhullError
from scipy.optimize import minimize
import torch
from numba import njit
from j69_input import X as X0, PATCH

torch.set_num_threads(1)
torch.set_default_dtype(torch.float64)

@njit(cache=True)
def barcodes(Y, eps=1e-14):
 n=len(Y); r2=(Y*Y).sum(1); ne=n*(n-1)//2
 aa=np.empty(ne,np.int64);bb=np.empty(ne,np.int64);ww=np.empty(ne);k=0
 for i in range(n):
  for j in range(i+1,n):
   d=Y[j]-Y[i];dd=np.dot(d,d)
   t=max(0.,min(1.,-np.dot(Y[i],d)/dd)) if dd>1e-30 else 0.
   z=Y[i]+t*d;aa[k]=i;bb[k]=j;ww[k]=np.dot(z,z);k+=1
 order=np.argsort(-ww);pa=np.arange(n);own=np.arange(n);out=np.zeros((n-1,6));m=0
 for k in order:
  a=aa[k];b=bb[k]
  while pa[a]!=a:
   pa[a]=pa[pa[a]];a=pa[a]
  while pa[b]!=b:
   pa[b]=pa[pa[b]];b=pa[b]
  if a==b:continue
  if r2[own[a]]<r2[own[b]] or (r2[own[a]]==r2[own[b]] and own[a]>own[b]):a,b=b,a
  dep=1-ww[k]/r2[own[b]]
  if dep>eps:
   out[m,0]=dep;out[m,1]=own[b];out[m,2]=aa[k];out[m,3]=bb[k];out[m,4]=r2[own[b]];out[m,5]=own[a];m+=1
  pa[b]=a
 return out[:m]

def mesh(X):
 h=ConvexHull(X);tri=h.simplices.copy()
 a,b,c=X[tri[:,0]],X[tri[:,1]],X[tri[:,2]]
 swap=np.sum(np.cross(b-a,c-a)*h.equations[:,:3],axis=1)<0
 tri[swap]=tri[swap][:,[0,2,1]]
 # Coplanar facets stay exact under the fixed-cap parameterization.
 _,group=np.unique(np.round(h.equations,9),axis=0,return_inverse=True)
 return h,tri,group

def geometry(Z,tri,group):
 t=torch.as_tensor(tri,dtype=torch.long);g=torch.as_tensor(group,dtype=torch.long)
 a,b,d=Z[t[:,0]],Z[t[:,1]],Z[t[:,2]]
 w=(a*torch.linalg.cross(b,d)).sum(1);W=w.sum()
 c=(w[:,None]*(a+b+d)).sum(0)/(4*W)
 ns=torch.linalg.cross(b-a,d-a);hs=(ns*a).sum(1)
 nf=int(group.max())+1
 N=torch.zeros((nf,3)).index_add(0,g,ns);H=torch.zeros(nf).index_add(0,g,hs)
 Y=N/(H-(N*c).sum(1))[:,None]
 return c,Y,W/6

def escape_loss(Y, margin=1e-5, power=2., root=None):
 r2=(Y*Y).sum(1)
 slopes=(Y@Y.T-r2[:,None])/r2[:,None]
 slopes=slopes-torch.eye(len(Y))*1e6
 vals,indices=slopes.max(dim=1)
 if root is None:root=int(r2.detach().argmax())
 keep=torch.arange(len(Y))!=root
 return torch.relu(margin-vals[keep]).pow(power).sum()

def torch_depth(Y,bars):
 if not len(bars):return torch.zeros(0)
 idx=torch.as_tensor(bars[:,1:4].astype(np.int64))
 r=Y[idx[:,0]];a=Y[idx[:,1]];d=Y[idx[:,2]]-a
 tt=torch.clamp(-(a*d).sum(1)/(d*d).sum(1),0.,1.)
 death=((a+tt[:,None]*d)**2).sum(1)
 return 1-death/(r*r).sum(1)

def unpack(x,keepcap):
 z=x.reshape(-1,3)
 if not keepcap:return z
 z=z.clone();z[PATCH,1]=-.272*z[PATCH,0]-.409*z[PATCH,2]-.68526367
 return z

class Objective:
 def __init__(self,start,keepcap=True,power=2,weight=1.,regularization=0.,folder='opt', maxcalls=5000):
  self.start=np.array(start);self.keepcap=keepcap;self.power=power;self.weight=weight;self.reg=regularization
  self.k=0;self.best=np.inf;self.path=folder;self.maxcalls=maxcalls;self.started=time.time();os.makedirs(folder,exist_ok=True)
  self.trace=[]
 def __call__(self,x):
  self.k+=1
  T=torch.tensor(x,requires_grad=True);Z=unpack(T,self.keepcap);X=Z.detach().numpy()
  h,tri,g=mesh(X);c,Y,vol=geometry(Z,tri,g)
  Pc=Z[torch.tensor(h.vertices,dtype=torch.long)]-c
  bp=barcodes(Pc.detach().numpy());bq=barcodes(Y.detach().numpy())
  dp=torch_depth(Pc,bp);dq=torch_depth(Y,bq)
  # All finite bars, not just frozen target pairs. Max values remain separately logged.
  if self.power<0:
   loss=escape_loss(Pc,margin=1e-5,power=-self.power)+self.weight*escape_loss(Y,margin=1e-5,power=-self.power)
  else:
   loss=(dp**self.power).sum()+self.weight*(dq**self.power).sum()
  if self.reg:loss=loss+self.reg*((Z-torch.tensor(self.start))**2).sum()
  loss.backward();v=float(loss);grad=T.grad.detach().numpy()
  p=float(bp[:,0].max()) if len(bp) else 0.;q=float(bq[:,0].max()) if len(bq) else 0.
  rec={'call':self.k,'loss':v,'P':p,'Q':q,'nP':len(bp),'nQ':len(bq),'V':len(h.vertices),'F':len(Y),'vol':float(vol.detach()),'grad':float(np.linalg.norm(grad)),'seconds':time.time()-self.started}
  self.trace.append(rec)
  if v<self.best:
   self.best=v;np.save(os.path.join(self.path,'best.npy'),X)
   json.dump(rec,open(os.path.join(self.path,'best.json'),'w'),indent=2)
  if self.k%25==0 or self.k==1:
   print(json.dumps(rec),flush=True)
   json.dump(self.trace,open(os.path.join(self.path,'trace.json'),'w'))
  if self.k>self.maxcalls:raise RuntimeError('MAXCALLS reached; best endpoint saved')
  return v,grad

def describe(X):
 h,tri,g=mesh(X);c,Y,vol=geometry(torch.tensor(X),tri,g);c=c.numpy();Y=Y.numpy()
 pb=barcodes(X[h.vertices]-c);qb=barcodes(Y)
 faces=[set(tri[g==f].ravel().tolist()) for f in range(len(Y))]
 edge={}
 for f in range(len(faces)):
  for j in range(f):
   common=faces[f]&faces[j]
   if len(common)==2:edge[tuple(sorted(common))]=(j,f)
 # Per-stratum strict floating signs, with numerical tolerance stated in the output.
 Z=X-c;S=[];U=[];H=[]
 for i,y in enumerate(Y):
  foot=y/(y@y);sl=1-Y@foot;sl[i]=np.inf
  if min(sl)>1e-10:S.append((i,sorted(faces[i]),float(min(sl))))
 for v in h.vertices:
  vals=[Z[v]@(Z[b if v==a else a]-Z[v]) for a,b in edge if v in (a,b)]
  if vals and max(vals)<-1e-12:U.append((int(v),float(max(vals))))
 for (a,b),(f,j) in edge.items():
  d=Z[b]-Z[a];t=-Z[a]@d/(d@d);p=Z[a]+t*d
  coef=np.linalg.lstsq(Y[[f,j]].T,p,rcond=None)[0]
  if 1e-12<t<1-1e-12 and min(coef)>1e-10:H.append((a,b,float(t),coef.tolist()))
 return dict(V=len(h.vertices),E=len(edge),F=len(Y),C=2*len(edge),centroid=c.tolist(),volume=float(vol),P=sorted(pb.tolist(),reverse=True),Q=sorted(qb.tolist(),reverse=True),S=S,U=U,H=H,counts=[len(S),len(U),len(H)],facets=[sorted(f) for f in faces],hullvertices=h.vertices.tolist())

if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--start');ap.add_argument('--free',action='store_true');ap.add_argument('--power',type=float,default=2);ap.add_argument('--weight',type=float,default=1);ap.add_argument('--radius',type=float,default=.12);ap.add_argument('--steps',type=int,default=350);ap.add_argument('--folder',default='/mnt/data/j56/opt');ap.add_argument('--reg',type=float,default=0)
 args=ap.parse_args();start=np.load(args.start) if args.start else X0.copy()
 obj=Objective(start,not args.free,args.power,args.weight,args.reg,args.folder)
 f,j=obj(start.ravel());print('BASELINE',json.dumps(describe(start)),flush=True)
 bounds=list(zip(start.ravel()-args.radius,start.ravel()+args.radius))
 try:
  r=minimize(obj,start.ravel(),jac=True,method='L-BFGS-B',bounds=bounds,options={'maxiter':args.steps,'maxls':30,'ftol':1e-15,'gtol':1e-11,'maxcor':20})
  print('OPT_END',r.message,r.fun,'nit',r.nit,'nfev',r.nfev,flush=True)
 except RuntimeError as ex:print('OPT_STOP',ex,flush=True)
 best=np.load(args.folder+'/best.npy');report=describe(best)
 json.dump(report,open(args.folder+'/census.json','w'),indent=2)
 np.savetxt(args.folder+'/best.txt',best,fmt='%.17g');print('BEST_CENSUS',json.dumps(report),flush=True)
```

## File: protect69.py
```python
"""Finite-bar descent with explicit no-new-extrema linearized protection.
Floating discovery tool only; neither grouping tolerances nor output are an exact proof.
"""
import os,json,time,argparse
os.environ.setdefault('OPENBLAS_NUM_THREADS','1')
import numpy as np
import torch
from scipy.optimize import linprog
from search69 import X0,PATCH,mesh,geometry,unpack,barcodes,torch_depth,describe

def fields(x,need_jac=True,weight=1):
    T=torch.tensor(x,requires_grad=True)
    Z=unpack(T,True);h,tri,g=mesh(Z.detach().numpy())
    c,Y,vol=geometry(Z,tri,g);A=Z[torch.tensor(h.vertices,dtype=torch.long)]-c
    bp=barcodes(A.detach().numpy());bq=barcodes(Y.detach().numpy())
    loss=torch_depth(A,bp).sum()+weight*torch_depth(Y,bq).sum()
    protected=[];rootcounts=[]
    for B in [A,Y]:
        r=(B*B).sum(1);sl=(B@B.T-r[:,None])/r[:,None]
        sl=sl-torch.eye(len(B))*1e6
        s,j=sl.max(dim=1)
        roots=s.detach().numpy()<=1e-13
        rootcounts.append(int(roots.sum()))
        protected.append(s[~torch.as_tensor(roots)])
    cons=torch.cat(protected)
    data={'P':float(bp[:,0].max()) if len(bp) else 0.,'Q':float(bq[:,0].max()) if len(bq) else 0.,'nP':len(bp),'nQ':len(bq),'roots':rootcounts,'loss':float(loss.detach()),'V':len(h.vertices),'F':len(Y),'min_escape':float(cons.detach().min())}
    if not need_jac:return data,Z.detach().numpy()
    grad=torch.autograd.grad(loss,T,retain_graph=True)[0].detach().numpy()
    J=torch.autograd.grad(cons,T,grad_outputs=torch.eye(len(cons)),is_grads_batched=True)[0].detach().numpy()
    return data,Z.detach().numpy(),grad,J,cons.detach().numpy()

def run(folder,steps=1000,trust=.002,start=None,weight=1):
    os.makedirs(folder,exist_ok=True)
    x=(X0.copy() if start is None else np.load(start)).ravel();trace=[]
    prev=None;began=time.time()
    for k in range(steps):
        data,X,grad,J,s=fields(x,weight=weight)
        if max(data['roots'])>2:raise RuntimeError('input has additional extrema')
        trace.append(dict(k=k,seconds=time.time()-began,trust=trust,**data))
        if k%10==0:print(json.dumps(trace[-1]),flush=True)
        if not data['nP'] and not data['nQ']:
            print('FLOATING_BAR_FREE_NEEDS_EXACT_AUDIT',flush=True);break
        grad=grad/max(np.linalg.norm(grad),1e-20)
        # Maintain half the current escape margin in the linear model.
        scale=np.maximum(np.linalg.norm(J,axis=1),1e-20)
        lp=linprog(grad,A_ub=-J/scale[:,None],b_ub=.5*s/scale,bounds=[(-trust,trust)]*len(x),method='highs')
        if not lp.success:print('LP_FAILURE',lp.message,flush=True);break
        direction=lp.x;accepted=False
        for bt in range(24):
            trial=x+direction*(.5**bt)
            try:q,W=fields(trial,False,weight=weight)
            except Exception:continue
            # Strict positivity of old nonroots is supported by the linear step;
            # actual global root census, rebuilt on the current hull, is authoritative.
            if max(q['roots'])<=2 and q['nP']<=1 and q['nQ']<=1 and q['loss']<data['loss']-1e-12:
                x=trial;accepted=True
                np.save(folder+'/best.npy',W);json.dump(q,open(folder+'/best.json','w'),indent=2)
                if bt==0:trust=min(.01,trust*1.05)
                elif bt>8:trust=max(1e-7,trust*.75)
                break
        if not accepted:
            trust*=.3
            if trust<1e-9:print('TRUST_STALL',flush=True);break
        if k%20==0:json.dump(trace,open(folder+'/trace.json','w'),indent=2)
    X=unpack(torch.tensor(x),True).numpy();np.save(folder+'/best.npy',X)
    np.savetxt(folder+'/best.txt',X,fmt='%.17g')
    report=describe(X);json.dump(report,open(folder+'/census.json','w'),indent=2)
    json.dump(trace,open(folder+'/trace.json','w'),indent=2)
    print('CONSTRAINED_END',json.dumps({k:report[k] for k in ['V','E','F','C','counts','centroid','volume']}),flush=True)

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--folder',default='protected1');ap.add_argument('--steps',type=int,default=1000);ap.add_argument('--trust',type=float,default=.002);ap.add_argument('--start');ap.add_argument('--weight',type=float,default=1)
    a=ap.parse_args();run(a.folder,a.steps,a.trust,a.start,a.weight)
```
