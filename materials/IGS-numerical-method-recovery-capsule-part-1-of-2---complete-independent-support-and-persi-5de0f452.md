# material-5de0f452cd7c

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

Public derivative: internal-record-identifiers-replaced.

---

# IGS numerical-method recovery capsule part 1 of 2

These TWO complete Python units produced the numerical checkpoints frozen into IGS5_LOG_C468_G9 and IGS5_PERSIST_C468_G9. They are numerical search methods, not exact certificates. The exact two-part recovery is separately self-contained: [internal-source-reference] and [internal-source-reference]. Part2 of this numerical-method capsule supplies the complete centre-line diagnostic, freeze routine, original checkpoint arrays, dependency versions, commands and hashes.

Save every complete fenced source as its stated filename, UTF-8 with one final LF. No helpers are omitted.

## igs_scout.py
9553 bytes,SHA256 bdb72ae4c828b5d6f74b2bf8bbc7a6bc6a180a045daed3ff343baa0a9e94742c.

```python
"""Independent Green support stacks: finite actual-volume-centred numerical scouts.
All decisive claims require a separate rational audit. Float64, one CPU thread.
"""
from __future__ import annotations
import argparse, json, math, hashlib, time
from pathlib import Path
from collections import defaultdict
import numpy as np
import torch

torch.set_default_dtype(torch.float64)
torch.set_num_threads(1)

class IGS:
    def __init__(self,n:int,k:int):
        assert n>=3 and n%2==1 and k>=1
        self.n,self.k=n,k; self.m=2*k+1; self.west=(n-1)//2
        th=np.arange(n)*2*np.pi/n
        self.base=torch.tensor(np.stack([np.cos(th),np.sin(th)],1))
        th=(np.arange(n)*2+1)*np.pi/n
        self.normals=torch.tensor(np.stack([np.cos(th),np.sin(th)],1))
        # Pin the west axis exactly; the rational verifier uses rational normals.
        self.normals[self.west]=torch.tensor([-1.,0.])
        t=np.linspace(-.95,.95,self.m); x=2*t/(1+t*t)
        self.ax=torch.tensor(np.r_[-1.,x,1.])
        self.G=(1-torch.abs(self.ax[:,None]-self.ax[None,1:-1])-self.ax[:,None]*self.ax[None,1:-1])/2
        ns=torch.stack([torch.roll(self.normals,1,0),self.normals],1)
        self.inv=torch.linalg.inv(ns)
        faces=[]; slab=[]; side=[]
        def ix(i,j):return 1+i*n+j%n
        for j in range(n):
            faces.append([0,ix(0,j+1),ix(0,j)]);slab.append(0);side.append(j)
        for i in range(self.m-1):
            for j in range(n):
                faces.append([ix(i,j),ix(i,j+1),ix(i+1,j+1),ix(i+1,j)]);slab.append(i+1);side.append(j)
        for j in range(n):
            faces.append([ix(self.m-1,j),ix(self.m-1,j+1),n*self.m+1]);slab.append(self.m);side.append(j)
        self.rawfaces=faces
        # The central west face is one maximal face: join the adjacent quads.
        f0=k*n+self.west; f1=(k+1)*n+self.west
        directed=[]
        for f in (faces[f0],faces[f1]):
            directed.extend(zip(f,f[1:]+f[:1]))
        directed=[(a,b) for a,b in directed if (b,a) not in directed]
        succ=dict(directed); cyc=[directed[0][0]]
        while succ[cyc[-1]]!=cyc[0]:cyc.append(succ[cyc[-1]])
        faces=[(cyc if i==f0 else f) for i,f in enumerate(faces) if i!=f1]
        self.faces=faces
        self.slab=torch.tensor([s for i,s in enumerate(slab) if i!=f1])
        self.side=torch.tensor([s for i,s in enumerate(side) if i!=f1])
        ef=defaultdict(list)
        for fi,f in enumerate(faces):
            for a,b in zip(f,f[1:]+f[:1]):ef[tuple(sorted((a,b)))].append(fi)
        assert all(len(ff)==2 for ff in ef.values())
        self.E=torch.tensor(sorted(ef)); self.EF=torch.tensor([ef[tuple(e)] for e in self.E.tolist()])
        self.tris=torch.tensor([[f[0],f[j],f[j+1]] for f in self.rawfaces for j in range(1,len(f)-1)])
        self.uroot=1+k*n; self.sroot=f0
        self.maskp=torch.ones(self.m*n+2,dtype=torch.bool); self.maskp[self.uroot]=False
        self.maskq=torch.ones(len(faces),dtype=torch.bool); self.maskq[self.sroot]=False
        self.cdiag={}

    def init(self, seed=0):
        # Positive curvature of a semicircle with translated analytic circular centres.
        x=self.ax.numpy(); rr=np.sqrt(np.maximum(0,1-x*x))
        phase=5*np.arcsin(x); d=.02*np.stack([np.cos(phase),np.sin(phase)],1)
        # Subtract endpoint chord, which is only a global affine translation/shear.
        d-=((1-x[:,None])/2)*d[0]+((1+x[:,None])/2)*d[-1]
        h=rr[:,None]*math.cos(math.pi/self.n)+d@self.normals.numpy().T
        slopes=np.diff(h,axis=0)/np.diff(x)[:,None]
        a=slopes[:-1]-slopes[1:]
        a=np.maximum(a,1e-5)
        rng=np.random.default_rng(seed)
        z=np.log(a[self.k:]); z+=rng.normal(0,.15,z.shape)
        return np.r_[z.ravel(), math.log(.95), 0., 0.]

    def geometry(self,y):
        n,k=self.n,self.k
        pos=torch.exp(y[:(k+1)*n].reshape(k+1,n))
        cent=(pos[0]+torch.flip(pos[0],[0]))/2
        # Fix zero curvature only at the stable-face support direction.
        mask=torch.ones(n);mask[self.west]=0;cent=cent*mask
        aa=torch.cat([torch.flip(pos[1:],[0,1]),cent[None],pos[1:]],0)
        h=self.G@aa
        h=h/(h[k+1].mean()/math.cos(math.pi/n))
        pair=torch.stack([torch.roll(h,1,1),h],2)
        yz=torch.einsum('nij,mnj->mni',self.inv,pair)
        lam,beta=torch.exp(y[-3]),torch.exp(y[-2]);alpha=y[-1]
        xx=self.ax*lam
        yz2=torch.stack([yz[:,:,0],beta*(yz[:,:,1]+alpha*self.ax[:,None])],2)
        rings=torch.cat([xx[1:-1,None,None].expand(-1,n,1),yz2[1:-1]],2).reshape(-1,3)
        tips=torch.stack([xx[[0,-1]],torch.zeros(2),beta*alpha*self.ax[[0,-1]]],1)
        v=torch.cat([tips[:1],rings,tips[1:]],0)
        a,b,c=(v[self.tris[:,j]] for j in range(3))
        vv=torch.sum(a*torch.linalg.cross(b,c),1)/6
        volume=vv.sum(); centroid=(vv[:,None]*(a+b+c)).sum(0)/(4*volume)
        v=v-centroid
        slope=torch.diff(h,dim=0)/torch.diff(xx)[:,None]
        si,nj=self.slab,self.side
        N=torch.stack([-slope[si,nj]-self.normals[nj,1]*alpha/lam,self.normals[nj,0],self.normals[nj,1]/beta],1)
        H=h[si,nj]-slope[si,nj]*xx[si]-(N*centroid).sum(1)
        q=N/H[:,None]
        # Each claimed section vertex must satisfy every side support.
        slack=h[:,None,:]-torch.einsum('mic,jc->mij',yz,self.normals)
        # Signed positive edge lengths exclude disappeared side directions.
        edges=torch.roll(yz,-1,1)-yz
        tangent=torch.stack([-self.normals[:,1],self.normals[:,0]],1)
        length=(edges*tangent[None]).sum(2)
        return v,q,slack[1:-1],length[1:-1],volume,H,centroid,aa,h

    @staticmethod
    def gaps(v):
        gram=v@v.T; r=(v*v).sum(1)
        eye=torch.eye(len(v),dtype=torch.bool)
        cross=gram.masked_fill(eye,-torch.inf).max(1).values
        # Origin is interior of every valid body, hence cross>0 for these charts.
        return torch.log(r.clamp_min(1e-14))-torch.log(cross.clamp_min(1e-14))

    def loss(self,y,mode='log',eps=1e-4):
        v,q,slack,length,vol,H,cen,aa,h=self.geometry(y)
        gp,gq=self.gaps(v),self.gaps(q)
        if mode=='log':
            core=(torch.relu(gp[self.maskp]+eps)**2).sum()+(torch.relu(gq[self.maskq]+eps)**2).sum()
        elif mode=='max':
            core=torch.relu(gp[self.maskp]+eps).max()+torch.relu(gq[self.maskq]+eps).max()+.1*(torch.relu(gp[self.maskp]+eps)**2).sum()+.1*(torch.relu(gq[self.maskq]+eps)**2).sum()
        elif mode=='linear':
            core=torch.relu(gp[self.maskp]+eps).sum()+torch.relu(gq[self.maskq]+eps).sum()
        else:raise ValueError(mode)
        # All inequality guards are numerical; independent hull/audit remains mandatory.
        guard=100*torch.relu(-slack).square().sum()+10*torch.relu(1e-5-length).square().sum()+100*torch.relu(.01-H).square().sum()+100*torch.relu(.001-vol).square()
        # Keep the two prescribed extremal points strict, not merely global survivors.
        root=10*torch.relu(eps-gp[self.uroot]).square()+10*torch.relu(eps-gq[self.sroot]).square()
        return core+guard+root

    def diagnose(self,y):
        with torch.no_grad():
            v,q,slack,length,vol,H,cen,aa,h=self.geometry(torch.tensor(y))
            gp,gq=self.gaps(v),self.gaps(q)
            return dict(n=self.n,k=self.k,V=len(v),E=len(self.E),F=len(q),C=2*len(self.E),S=int((gq>1e-9).sum()),U=int((gp>1e-9).sum()),maxPgap=float(gp[self.maskp].max()),maxQgap=float(gq[self.maskq].max()),minSlack=float(slack.min()),minEdge=float(length.min()),minH=float(H.min()),volume=float(vol),centroid=cen.tolist(),rootPgap=float(gp[self.uroot]),rootQgap=float(gq[self.sroot]))

    def save(self,path,y,extra=None):
        d={'identity':Path(path).stem,'n':self.n,'k':self.k,'y':np.asarray(y).tolist(),'diagnostic':self.diagnose(y),'extra':extra or {}}
        b=(json.dumps(d,sort_keys=True,separators=(',',':'))+'\n').encode();Path(path).write_bytes(b)
        print('IGS_CHECKPOINT',str(path),len(b),hashlib.sha256(b).hexdigest(),flush=True)

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--n',type=int,default=5);p.add_argument('--k',type=int,default=11);p.add_argument('--seed',type=int,default=0);p.add_argument('--steps',type=int,default=4000);p.add_argument('--lr',type=float,default=.006);p.add_argument('--mode',default='log');p.add_argument('--eps',type=float,default=.0001);p.add_argument('--input');p.add_argument('--output',default='igs_checkpoint.json');p.add_argument('--diag',action='store_true');a=p.parse_args()
    if a.input:
        d=json.loads(Path(a.input).read_text());model=IGS(d['n'],d['k']);y0=np.array(d['y'])
    else:model=IGS(a.n,a.k);y0=model.init(a.seed)
    if a.diag:print(json.dumps(model.diagnose(y0),indent=2));raise SystemExit
    y=torch.tensor(y0,requires_grad=True);opt=torch.optim.Adam([y],lr=a.lr);best=float('inf');besty=y0.copy();start=time.time()
    for it in range(a.steps):
        opt.zero_grad();loss=model.loss(y,a.mode,a.eps)
        if not torch.isfinite(loss):raise ArithmeticError('nonfinite objective')
        # Checkpoint corresponds exactly to the evaluated pre-step iterate.
        val=float(loss.detach())
        if val<best:best=val;besty=y.detach().numpy().copy()
        loss.backward();torch.nn.utils.clip_grad_norm_([y],100.);opt.step()
        if it%500==0:print('IGS_SCOUT',it,round(time.time()-start,2),val,model.diagnose(y.detach().numpy()),flush=True)
    model.save(a.output,besty,dict(loss=best,steps=a.steps,lr=a.lr,mode=a.mode,eps=a.eps,seed=a.seed,input=a.input))
    print('IGS_DIAGNOSTIC',json.dumps(model.diagnose(besty)),flush=True)
```

## igs_persistence.py
3811 bytes,SHA256 362ec075caf8c295270fe1d8cee90600f5b81f4d3ee4be4bf5055ac6aa51fa16.

```python
"""Full true-edge/same-centre-polar persistence for IGS numerical scouts.
Selected birth/death levels remain differentiable; combinatorial selection is detached.
Equal floating levels are tie-broken, not claimed exact-batched certificates.
"""
import argparse,json,time
from pathlib import Path
import numpy as np
import torch
from igs_scout import IGS

def persistence(v, edges):
    rr=(v*v).sum(1)
    a,b=v[edges[:,0]],v[edges[:,1]];d=b-a
    t=torch.clamp(-(a*d).sum(1)/(d*d).sum(1),0.,1.)
    death=((a+t[:,None]*d)**2).sum(1)
    R=rr.detach().numpy();D=death.detach().numpy();E=edges.numpy()
    parent=list(range(len(v)));peak=list(range(len(v)));members={i:{i} for i in range(len(v))};bars=[]
    def root(a):
        while parent[a]!=a:parent[a]=parent[parent[a]];a=parent[a]
        return a
    for ei in np.argsort(-D,kind='stable'):
        x,y=E[ei];x,y=root(int(x)),root(int(y))
        if x==y:continue
        if (R[peak[x]],-peak[x])<(R[peak[y]],-peak[y]):x,y=y,x
        p=peak[y]
        if R[p]-D[ei]>1e-12:
            bars.append((p,int(ei),len(members[y])))
        parent[y]=x;members[x]|=members[y];del members[y]
    vals=torch.stack([torch.log(rr[p]/death[e]) for p,e,c in bars]) if bars else rr[:0]
    return vals,bars,rr,death

class PersistIGS(IGS):
    def ploss(self,y,mode='squared',weight=.02):
        v,q,slack,length,vol,H,cen,aa,h=self.geometry(y)
        p,bp,rp,dp=persistence(v,self.E);qv,bq,rq,dq=persistence(q,self.EF)
        if mode=='squared':core=(p*p).sum()+(qv*qv).sum()
        elif mode=='linear':core=p.sum()+qv.sum()
        elif mode=='max':core=(p.max() if len(p) else 0)+(qv.max() if len(qv) else 0)+.1*((p*p).sum()+(qv*qv).sum())
        else:raise ValueError(mode)
        # Prescribed global survivors prevent root-transfer rewards.
        root=.5*(torch.relu(torch.log(rp/rp[self.uroot])).square().sum()+torch.relu(torch.log(rq/rq[self.sroot])).square().sum())
        return core+root+weight*self.loss(y,'log')
    def pdiagnose(self,y):
        d=self.diagnose(y)
        with torch.no_grad():
            v,q,*_=self.geometry(torch.tensor(y))
            for label,x,e in [('P',v,self.E),('Q',q,self.EF)]:
                bars,ix,rr,death=persistence(x,e)
                d[label+'bars']=[dict(peak=p,edge=k,size=c,log=float(z),relative=float(1-torch.exp(-z))) for z,(p,k,c) in sorted(zip(bars,ix),key=lambda z:float(z[0]),reverse=True)]
        return d

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--input',required=True);p.add_argument('--output',default='igs_persistence.json');p.add_argument('--steps',type=int,default=4000);p.add_argument('--lr',type=float,default=.002);p.add_argument('--mode',default='squared');p.add_argument('--weight',type=float,default=.02);p.add_argument('--diag',action='store_true');a=p.parse_args()
    data=json.loads(Path(a.input).read_text());m=PersistIGS(data['n'],data['k']);y0=np.array(data['y'])
    if a.diag:print(json.dumps(m.pdiagnose(y0),indent=2));raise SystemExit
    y=torch.tensor(y0,requires_grad=True);opt=torch.optim.Adam([y],lr=a.lr);best=float('inf');besty=y0.copy();start=time.time()
    for it in range(a.steps):
        opt.zero_grad();loss=m.ploss(y,a.mode,a.weight);val=float(loss.detach())
        if val<best:best=val;besty=y.detach().numpy().copy()
        loss.backward();torch.nn.utils.clip_grad_norm_([y],100.);opt.step()
        if it%500==0:
            print('IGS_PERSISTENCE',it,round(time.time()-start,1),val,m.diagnose(y.detach().numpy()),flush=True)
            m.save(a.output,besty,dict(loss=best,steps=it+1,lr=a.lr,mode=a.mode,weight=a.weight,input=a.input))
    m.save(a.output,besty,dict(loss=best,steps=a.steps,lr=a.lr,mode=a.mode,weight=a.weight,input=a.input))
    print('IGS_COMPLETE_BARS',json.dumps(m.pdiagnose(besty)),flush=True)
```
