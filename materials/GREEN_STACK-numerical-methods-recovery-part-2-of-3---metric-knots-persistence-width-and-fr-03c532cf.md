# material-03c532cf1ba8

AI research material · [Export notes](../catalog/coverage.md#text-records)

---

# GREEN_STACK numerical methods recovery, part 2 of 3

Complete continuation/search source units. Part 1 is material [internal-source-reference]. Part 3 supplies exact checkpoints, dependency versions, file hashes, replay commands and scope. All floating outputs remain nominations until an independent exact rational freeze and complete actual-centroid maximal-complex audit. None of these losses certifies exclusion. The known central coplanar face pair is explicitly merged in the Persistence graph; older Model.report S indices can count the two copies separately.

## stack_green_metric.py
```python
"""Finite Green-stack continuation with an extra C2-compatible affine scale.
A numerical nominator only; no failed optimization proves nonexistence.
"""
import sys,json
from pathlib import Path
import numpy as np
import torch
from stack_green import GreenModel

class MetricGreen(GreenModel):
    def __init__(self,n,k):
        super().__init__(n,k)
        self.y0=np.r_[self.y0,0.]
    def unpack(self,y):
        v,q,sl,poly,r,H,cy=super().unpack(y[:-1])
        z=torch.exp(y[-1]);sc=torch.stack((z*0+1,z*0+1,z))
        return v*sc,q/sc,sl,poly,r,H,cy
    def loss(self,y,eps=.002,kind='max'):
        v,q,sl,poly,r,H,cy=self.unpack(y)
        def arrows(a,src,dst):
            d=a[dst]-a[src]
            return (a[src]*d).sum(1)/(torch.linalg.vector_norm(a[src],dim=1)*torch.linalg.vector_norm(d,dim=1)+1e-18)
        pa=arrows(v,self.src,self.dst);qa=arrows(q,self.psrc,self.pdst)
        po=torch.full((len(v),),-1e5).scatter_reduce(0,self.src,pa,reduce='amax',include_self=True)
        qo=torch.full((len(q),),-1e5).scatter_reduce(0,self.psrc,qa,reduce='amax',include_self=True)
        pm=torch.ones(len(po),dtype=torch.bool);pm[self.root]=False
        qm=torch.ones(len(qo),dtype=torch.bool);qm[self.sfaces]=False
        if kind=='forest':
            # Triangle meridians: upper-west escapes via +tip to east, lower-west via -tip.
            # Each east track points toward the central east unstable root.
            assert self.n==3
            m=2*self.k+1;n=self.n
            ps=[];pd=[]
            for i in range(m):
                for j in range(n):
                    p=1+i*n+j
                    if p==self.root:continue
                    if j==0:
                        target=1+(i+(1 if i<self.k else -1))*n
                    elif j==1:
                        target=1+(i+1)*n+j if i<m-1 else n*m+1
                    else:
                        target=1+(i-1)*n+j if i>0 else 0
                    ps.append(p);pd.append(target)
            ps.extend([0,n*m+1]);pd.extend([1,1+(m-1)*n])
            po2=arrows(v,torch.tensor(ps),torch.tensor(pd))
        else:po2=po[pm]
        # Allow a complete-point polar escape witness; convexity makes it sufficient.
        if kind=='allpair':
            dq=q[None,:,:]-q[:,None,:]
            cos=(q[:,None,:]*dq).sum(2)/(torch.linalg.vector_norm(q,dim=1)[:,None]*torch.linalg.vector_norm(dq,dim=2)+1e-18)
            cos=cos-torch.eye(len(q))*1e4
            # Duplicate central S plane is never a meaningful witness.
            for a in self.sfaces:
                for b in self.sfaces:cos[a,b]=-1e4
            qo=cos.max(1).values
        losses=torch.cat((torch.relu(eps-po2),torch.relu(eps-qo[qm]),torch.relu(po[self.root:self.root+1]+eps),torch.relu(qo[self.sfaces]+eps)))
        penalty=torch.relu(.01-H).square().sum()+torch.relu(.01-r[1:-1]).square().sum()
        return losses.square().sum()+10*penalty,(po,qo)

if __name__=='__main__':
    source=sys.argv[1];kind=sys.argv[2] if len(sys.argv)>2 else 'max'
    iters=int(sys.argv[3]) if len(sys.argv)>3 else 6000
    d=json.loads(Path(source).read_text());m=MetricGreen(d['n'],d['k'])
    y0=np.array(d['y']);y0=np.r_[y0,0.] if len(y0)+1==len(m.y0) else y0
    y=torch.tensor(y0,requires_grad=True);op=torch.optim.Adam([y],lr=.002)
    best=float('inf');name=f"metric_{m.n}_{m.k}_{kind}"
    for it in range(iters+1):
        op.zero_grad();val,_=m.loss(y,.002,kind);val.backward();torch.nn.utils.clip_grad_norm_([y],10)
        if float(val.detach())<best:best=float(val.detach());by=y.detach().numpy().copy()
        op.step()
        if it%1000==0 or it==iters:
            rep=m.report(by);print(it,best,rep,flush=True)
            Path(name+'.json').write_text(json.dumps(dict(n=m.n,k=m.k,kind=kind,iteration=it,y=by.tolist(),loss=best,report=rep),sort_keys=True))
```

## stack_green_adaptive.py
```python
"""Adaptive-knot Green stacks. Positive curvature, convexity and mass are exact-form;
float search is only a nomination. Adds complete-point escape and root-radius gates.
"""
import sys,json
from pathlib import Path
import numpy as np
import torch
from stack_green_metric import MetricGreen

class AdaptiveGreen(MetricGreen):
    def __init__(self,n,k):
        super().__init__(n,k)
        ax=self.axis.numpy();pos=ax[k+1:]
        self.y0=np.r_[self.y0,np.log(np.diff(pos))]
    def unpack(self,y):
        n,k=self.n,self.k
        base=y[:-(k+1)];gaps=torch.softmax(y[-(k+1):],0)
        pos=torch.cumsum(gaps,0)
        self.axis=torch.cat((-torch.flip(pos,(0,)),pos[:1]*0,pos))
        x=self.axis[:,None];t=self.axis[None,1:-1]
        self.green=(1-torch.abs(x-t)-x*t)/2
        return super().unpack(base)
    def loss2(self,y,eps=.002,mode='radius'):
        v,q,sl,poly,r,H,cy=self.unpack(y)
        def score(a):
            d=a[None,:,:]-a[:,None,:]
            s=(a[:,None,:]*d).sum(2)/(torch.linalg.vector_norm(a,dim=1)[:,None]*torch.linalg.vector_norm(d,dim=2)+1e-18)
            return s-torch.eye(len(a))*1e4
        ps=score(v);qs=score(q)
        for a in self.sfaces:
            for b in self.sfaces:qs[a,b]=-1e4
        po=ps.max(1).values;qo=qs.max(1).values
        pm=torch.ones(len(po),dtype=torch.bool);pm[self.root]=False
        qm=torch.ones(len(qo),dtype=torch.bool);qm[self.sfaces]=False
        l=torch.cat((torch.relu(eps-po[pm]),torch.relu(eps-qo[qm])))
        R=(v[self.root]*v[self.root]).sum();R2=(q[self.sfaces[0]]*q[self.sfaces[0]]).sum()
        rad=torch.cat((torch.relu((v*v).sum(1)[pm]/R-(1-eps)),torch.relu((q*q).sum(1)[qm]/R2-(1-eps))))
        guards=torch.relu(.01-H).square().sum()+torch.relu(.01-r[1:-1]).square().sum()
        return l.square().sum()+(.5 if mode=='radius' else 0)*rad.square().sum()+10*guards

if __name__=='__main__':
    d=json.loads(Path(sys.argv[1]).read_text());mode=sys.argv[2] if len(sys.argv)>2 else 'radius';steps=int(sys.argv[3]) if len(sys.argv)>3 else 4000
    M=AdaptiveGreen(d['n'],d['k']); yy=np.array(d['y'])
    if len(yy)<len(M.y0):yy=np.r_[yy,M.y0[-M.k-1:]]
    y=torch.tensor(yy,requires_grad=True);opt=torch.optim.Adam([y],lr=.002)
    best=float('inf');name=f'adaptive_{M.n}_{M.k}_{mode}'
    for it in range(steps+1):
        opt.zero_grad();val=M.loss2(y,.002,mode);val.backward();torch.nn.utils.clip_grad_norm_([y],10)
        if float(val.detach())<best:best=float(val.detach());by=y.detach().numpy().copy()
        opt.step()
        if it%1000==0 or it==steps:
            rep=M.report(by);print(it,best,rep,flush=True)
            Path(name+'.json').write_text(json.dumps(dict(n=M.n,k=M.k,iteration=it,mode=mode,y=by.tolist(),loss=best,report=rep),sort_keys=True))
```

## freeze_green.py
```python
"""Freeze a MetricGreen nomination into self-contained positive rational data.
All floating transcendental values are frozen once; exact recovery needs no NumPy.
"""
import sys,json,math
from pathlib import Path
import numpy as np
from fractions import Fraction as F

def pair(x,den):
    z=F(int(round(float(x)*den)),den)
    return [z.numerator,z.denominator]

def freeze(path,den=10**9):
    d=json.loads(Path(path).read_text());k=d['k'];n=d['n'];assert n==3
    y=np.array(d['y']);assert len(y)==4*k+4
    ap=np.exp(y[:k+1]-max(y[:k+1]))
    assert min(ap)*den>2
    logits=y[k+1:k+1+3*k].reshape(k,3);weights=np.exp(logits-logits.max(1)[:,None]);weights/=weights.sum(1)[:,None]
    curv=[pair(a,den) for a in ap]
    bary=[[pair(max(a,1/den),den) for a in row] for row in weights]
    z0=math.sqrt(3)/2
    obj=dict(identity='GREEN_TRI_C472_MAX_G9',k=k,curvatures=curv,positive_barycentric=bary,
        alpha=pair(y[-3]/z0,den),**{'lambda':pair(math.exp(y[-2]),den)},beta=pair(math.exp(y[-1])*z0,den),
        source_checkpoint=Path(path).name,freeze_denominator=den)
    return obj
if __name__=='__main__':
    den=int(sys.argv[2]) if len(sys.argv)>2 else 10**9
    inp=freeze(sys.argv[1],den);out=Path(inp['identity']+'_INPUT.json')
    out.write_text(json.dumps(inp,sort_keys=True,separators=(',',':'))+'\n');print(out)
```

## green_persistence.py
```python
"""Finite whole-feature Green-stack scout; floating results are nominations only.
Uses true maximal graph after the single known central-face merger. Exact
verification must use the separately preserved rational recovery or extension.
"""
import sys,json
from pathlib import Path
import numpy as np
import torch
from stack_green_metric import MetricGreen
from stack_green_adaptive import AdaptiveGreen

class Persistence:
    def __init__(self,model):
        self.M=model
        f,g=model.sfaces
        self.qkeep=np.array([j for j in range(len(model.F)) if j!=g])
        qmap={j:i for i,j in enumerate(self.qkeep)};qmap[g]=qmap[f]
        pe=[];qe=[]
        for e,ef in zip(model.E,model.EF):
            a,b=map(qmap.get,ef)
            if a!=b:pe.append(tuple(e));qe.append(tuple(sorted((a,b))))
        self.pe=np.array(pe,dtype=int);self.qe=np.array(sorted(set(qe)),dtype=int)
        assert len(self.pe)==len(self.qe)==2*model.n*(2*model.k+1)+model.n-1
        self.root=model.root;self.qroot=qmap[f]
    @staticmethod
    def pairs(v,E):
        a,b=E.T;A=(v*v).sum(1);B=(v[a]*v[b]).sum(1)
        D=(v[a]-v[b]).square().sum(1)
        t=torch.clamp((A[a]-B)/(D+1e-30),0,1)
        d=torch.where(t<=0,A[a],torch.where(t>=1,A[b],A[a]+2*t*(B-A[a])+t*t*D))
        an=A.detach().numpy();dn=d.detach().numpy()
        par=list(range(len(v)));peak=list(range(len(v)));birthids=[];deathids=[]
        def root(i):
            while par[i]!=i:par[i]=par[par[i]];i=par[i]
            return i
        for ei in np.argsort(-dn,kind='stable'):
            i,j=map(root,E[ei])
            if i==j:continue
            if (an[peak[i]],-peak[i])<(an[peak[j]],-peak[j]):i,j=j,i
            birthids.append(peak[j]);deathids.append(int(ei));par[j]=i
        assert len(birthids)==len(v)-1
        rel=torch.relu(1-d[deathids]/A[birthids])
        return rel,(birthids,deathids),A,d
    def evaluate(self,y,kind='linear'):
        v,q,sl,poly,r,H,cy=self.M.unpack(y);q=q[self.qkeep]
        p,pp,pa,pd=self.pairs(v,self.pe);s,qp,qa,qd=self.pairs(q,self.qe)
        if kind=='log':loss=(-torch.log(torch.clamp(1-p,min=1e-15))).square().sum()+(-torch.log(torch.clamp(1-s,min=1e-15))).square().sum()
        elif kind=='square':loss=p.square().sum()+s.square().sum()
        else:loss=p.sum()+s.sum()
        local=y.sum()*0
        counts=[]
        for z,E,rt in [(v,self.pe,self.root),(q,self.qe,self.qroot)]:
            src=np.r_[E[:,0],E[:,1]];dst=np.r_[E[:,1],E[:,0]]
            diff=z[dst]-z[src]
            cos=(z[src]*diff).sum(1)/(z[src].norm(dim=1)*diff.norm(dim=1)+1e-18)
            mx=torch.full((len(z),),-1e5).scatter_reduce(0,torch.tensor(src),cos,reduce='amax',include_self=True)
            ids=torch.arange(len(z))!=rt
            local=local+torch.relu(.0002-mx[ids]).square().sum()
            counts.append(int((mx<0).sum()))
        guards=torch.relu(.02-H).square().sum()+torch.relu(.005-r[1:-1]).square().sum()
        loss=loss+.02*local+10*guards
        info=dict(P=float(p.sum().detach()),Q=float(s.sum().detach()),Pmax=float(p.max().detach()),Qmax=float(s.max().detach()),U=counts[0],S=counts[1],local=float(local.detach()),guard=float(guards.detach()))
        return loss,info

if __name__=='__main__':
    source=sys.argv[1];mode=sys.argv[2] if len(sys.argv)>2 else 'fixed';kind=sys.argv[3] if len(sys.argv)>3 else 'linear';steps=int(sys.argv[4]) if len(sys.argv)>4 else 4000
    inp=json.loads(Path(source).read_text());M=(AdaptiveGreen if mode=='adaptive' else MetricGreen)(inp['n'],inp['k'])
    y0=np.array(inp['y'])
    if len(y0)<len(M.y0):y0=np.r_[y0,M.y0[len(y0):]]
    assert len(y0)==len(M.y0)
    P=Persistence(M);y=torch.tensor(y0,requires_grad=True);opt=torch.optim.Adam([y],lr=.003)
    best=float('inf');stem=f'persistence_{M.n}_{M.k}_{mode}_{kind}'
    for it in range(steps+1):
        opt.zero_grad();loss,info=P.evaluate(y,kind);loss.backward();torch.nn.utils.clip_grad_norm_([y],10)
        val=float(loss.detach())
        if val<best:best=val;by=y.detach().numpy().copy();bi=info
        opt.step()
        if it%500==0 or it==steps:
            out=dict(n=M.n,k=M.k,mode=mode,kind=kind,iterations=it,y=by.tolist(),loss=best,info=bi,source=source)
            Path(stem+'.json').write_text(json.dumps(out,sort_keys=True));print(it,best,bi,flush=True)
```

## green_width_scout.py
```python
"""Finite fixed-edge-budget polygon-width scout, numerical nominations only.
No optimizer failure is a family exclusion. Every finite body uses its actual
slab centroid and a convexity-by-construction Green profile.
"""
import sys,json
from pathlib import Path
import numpy as np
import torch
from stack_green_metric import MetricGreen
from green_persistence import Persistence

if __name__=='__main__':
    n,k,seed=map(int,sys.argv[1:4]);steps=int(sys.argv[4]) if len(sys.argv)>4 else 6000
    kind=sys.argv[5] if len(sys.argv)>5 else 'max'
    M=MetricGreen(n,k);P=Persistence(M);rng=np.random.default_rng(seed)
    y0=M.y0.copy()
    if seed:y0+=rng.normal(0,.3,len(y0))
    y=torch.tensor(y0,requires_grad=True);op=torch.optim.Adam([y],lr=.003)
    best=float('inf');stem=f'width_{n}_{k}_{seed}_{kind}'
    for it in range(steps+1):
        op.zero_grad()
        if kind=='log':loss,info=P.evaluate(y,'log')
        else:loss,_=M.loss(y,.001,'max')
        loss.backward();torch.nn.utils.clip_grad_norm_([y],10)
        val=float(loss.detach())
        if val<best:best=val;by=y.detach().numpy().copy()
        op.step()
        if it%1000==0 or it==steps:
            with torch.no_grad(): _,info=P.evaluate(torch.tensor(by),'log')
            out=dict(n=n,k=k,seed=seed,kind=kind,iterations=it,y=by.tolist(),loss=best,info=info)
            Path(stem+'.json').write_text(json.dumps(out,sort_keys=True));print(it,best,info,flush=True)
```
