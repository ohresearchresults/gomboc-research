# material-2a921685e99d

AI research material · [Export notes](../catalog/coverage.md#text-records)

---

# GREEN_STACK numerical methods recovery, part 1 of 3

This capsule preserves the actual finite search methods, including unsuccessful approaches, rather than only the final exact input. These floating programs nominate geometries; no failed optimization is an exclusion theorem. The accepted exact C472356 and C40558 nonwinners can independently be recovered from [internal-source-reference] and [internal-source-reference] without running these numerical methods. Parts 1-3 of this numerical capsule are separately required to replay the indicated searches. Every source unit below is complete. Save the contents of each code fence under its heading filename, UTF-8/LF with one trailing newline. Part 3 contains dependencies, literal checkpoints, commands, hashes and the finite negative-result boundary. These files use NumPy/SciPy/Torch; they are not the standard-library exact certificate.

## stack_scout.py
```python
"""Finite homothetic-section scouts; floating search is not an exclusion proof."""
import json, math, sys
from pathlib import Path
import numpy as np
from scipy.optimize import minimize

# Planar vertices are CCW in (u,v). Layer data are (x,d_u,d_v,r).
def planar_centroid(k):
    z=k[:,0]*np.roll(k[:,1],-1)-k[:,1]*np.roll(k[:,0],-1)
    return np.sum((k+np.roll(k,-1,axis=0))*z[:,None],axis=0)/(3*z.sum())

def moments(layers):
    """Volume divided by area(K) and exact-form weighted layer first moments."""
    x,p,q,r=layers.T
    dt=np.diff(x); a=r[:-1]; b=r[1:]
    w0=dt*(3*a*a+2*a*b+b*b)/12
    w1=dt*(a*a+2*a*b+3*b*b)/12
    w=np.r_[w0,0]+np.r_[0,w1]
    vol=w.sum()
    return vol,(w[:,None]*layers[:,:3]).sum(axis=0)/vol,w

def complex_stack(layers,k):
    assert layers[0,3]==layers[-1,3]==0
    m=len(layers)-2; n=len(k)
    v=np.concatenate([layers[:1,:3],np.c_[np.repeat(layers[1:-1,0],n),
                 (layers[1:-1,None,1:3]+layers[1:-1,None,3:4]*k[None,:,:]).reshape(-1,2)],layers[-1:,:3]])
    f=[]
    for j in range(n):f.append([0,1+(j+1)%n,1+j])
    for i in range(m-1):
        for j in range(n):
            a=1+i*n+j;b=1+i*n+(j+1)%n
            f.append([a,b,b+n,a+n])
    for j in range(n):f.append([len(v)-1,1+(m-1)*n+j,1+(m-1)*n+(j+1)%n])
    return v,f

def state(layers,k,margin=0.0):
    # Centre K first, as required by the moment formula.
    k=k-planar_centroid(k)
    vol,c,w=moments(layers)
    v,f=complex_stack(layers,k);v-=c
    nr=np.array([np.cross(v[F[1]]-v[F[0]],v[F[2]]-v[F[0]]) for F in f])
    lens=np.linalg.norm(nr,axis=1)
    nr/=lens[:,None]
    h=np.array([np.dot(nr[i],v[F[0]]) for i,F in enumerate(f)])
    # Orientations above should already be outward; negative h indicates invalidity.
    polar=nr/np.maximum(h[:,None],1e-15)
    edge={}
    for i,F in enumerate(f):
        for a,b in zip(F,F[1:]+F[:1]):edge.setdefault(tuple(sorted([a,b])),[]).append(i)
    E=np.array(sorted(edge)); EF=np.array([edge[e] for e in sorted(edge)])
    uv=np.linalg.norm(v,axis=1)
    dots=np.einsum('ij,ij->i',v[E[:,0]],v[E[:,1]])
    out=np.full(len(v),-np.inf)
    np.maximum.at(out,E[:,0],(dots-uv[E[:,0]]**2)/(uv[E[:,0]]*np.linalg.norm(v[E[:,1]]-v[E[:,0]],axis=1)))
    np.maximum.at(out,E[:,1],(dots-uv[E[:,1]]**2)/(uv[E[:,1]]*np.linalg.norm(v[E[:,1]]-v[E[:,0]],axis=1)))
    # Stable test directly via edge halfspaces within each oriented facet.
    so=[]
    for i,F in enumerate(f):
        foot=h[i]*nr[i]
        a=v[F];b=np.roll(a,-1,axis=0)
        s=np.einsum('ij,j->i',np.cross(b-a,foot-a),nr[i])
        so.append(-np.min(s/np.linalg.norm(b-a,axis=1)))
    so=np.array(so)
    support=np.max(v@nr.T-h[None,:],axis=0)
    # K polygon convexity, layer support-profile concavity encoded by full support.
    U=np.flatnonzero(out<0);S=np.flatnonzero(so<0)
    return {'V':v,'F':f,'N':nr,'h':h,'U':U,'S':S,'out':out,'sout':so,
            'support':support,'E':E,'EF':EF,'centroid':c,'volume_factor':vol,'k':k}

def initial(n=7,m=9,model='axial'):
    assert m%2==1
    t=np.linspace(-.95,.95,m)
    x=2*t/(1+t*t);y=x*x
    P=1/14-279*y/560+79*y*y/240
    Q=11/40-37*y/70+5*y*y/49
    layers=np.c_[497*x/500,P,x*Q,np.sqrt(1-y)]
    tipP=1/14-279/560+79/240;tipQ=11/40-37/70+5/49
    layers=np.vstack([[-497/500,tipP,-tipQ,0],layers,[497/500,tipP,tipQ,0]])
    theta=2*np.pi*np.arange(n)/n
    k=np.c_[np.cos(theta),np.sin(theta)]
    return layers,k

def describe(s):
    return len(s['V']),len(s['E']),len(s['F']),len(s['S']),len(s['U']),float(s['support'].max()),s['centroid'].tolist()

if __name__=='__main__':
    for n,m in [(5,11),(7,9),(9,11),(11,9),(13,7),(17,5)]:
        layers,k=initial(n,m)
        s=state(layers,k)
        print(n,m,describe(s))
```

## stack_opt.py
```python
"""C2 homothetic stacks with one exactly merged equatorial stable patch.
Floating optimisation only. No numerical failure is an exclusion.
"""
import os
os.environ['OMP_NUM_THREADS']='1'
import sys,json,time
from pathlib import Path
import numpy as np
import torch
from scipy.optimize import minimize
from stack_scout import initial, planar_centroid

torch.set_num_threads(1)
torch.set_default_dtype(torch.float64)

class Model:
    def __init__(self,n=7,k=5,free_polygon=False):
        self.n=n;self.k=k;self.free_polygon=free_polygon
        layers,poly=initial(n,2*k+1)
        self.x=torch.tensor(layers[:,0])
        self.poly0=torch.tensor(poly)
        positive=layers[k+2:]
        self.y0=np.r_[positive[:-1,1:4].ravel(),positive[-1,1:3]]
        if free_polygon:self.y0=np.r_[self.y0,poly[:(n+1)//2].ravel()]
        m=2*k+1
        def vi(i,j):return 0 if i==0 else n*m+1 if i==m+1 else 1+(i-1)*n+j%n
        F=[]
        for i in range(m+1):
            for j in range(n):
                F.append(list(dict.fromkeys([vi(i,j),vi(i,j+1),vi(i+1,j+1),vi(i+1,j)])))
        ed={}
        for f,Fc in enumerate(F):
            for a,b in zip(Fc,Fc[1:]+Fc[:1]):ed.setdefault(tuple(sorted((a,b))),[]).append(f)
        E=np.array(sorted(ed)); EF=np.array([ed[e] for e in sorted(ed)])
        self.src=torch.tensor(np.r_[E[:,0],E[:,1]])
        self.dst=torch.tensor(np.r_[E[:,1],E[:,0]])
        self.psrc=torch.tensor(np.r_[EF[:,0],EF[:,1]])
        self.pdst=torch.tensor(np.r_[EF[:,1],EF[:,0]])
        self.root=vi(k+1,0)
        self.sfaces=[k*n+(n-1)//2,(k+1)*n+(n-1)//2]
        mask=np.ones(len(self.psrc),dtype=bool)
        for i,(a,b) in enumerate(zip(self.psrc.tolist(),self.pdst.tolist())):
            if a in self.sfaces and b in self.sfaces:mask[i]=False
        self.psrc=self.psrc[mask];self.pdst=self.pdst[mask]
        self.F=F;self.E=E;self.EF=EF
    def unpack(self,y):
        n,k=self.n,self.k
        pos=y[:3*k].reshape(k,3)
        tip=y[3*k:3*k+2]
        if self.free_polygon:
            half=y[3*k+2:].reshape((n+1)//2,2)
            # The east vertex stays on the C2 axis.
            first=torch.stack((half[0,0],half[0,1]*0)).reshape(1,2)
            half=torch.cat((first,half[1:]))
            poly=torch.cat((half,torch.flip(half[1:],(0,))*torch.tensor([1.,-1.])))
        else:poly=self.poly0
        z=poly[:,0]*torch.roll(poly[:,1],-1)-poly[:,1]*torch.roll(poly[:,0],-1)
        pc=((poly+torch.roll(poly,-1,0))*z[:,None]).sum(0)/(3*z.sum())
        poly=poly-pc
        # west edge has constant u; support b=-P + hs*r.
        hs=-poly[(n-1)//2,0]
        centre=torch.stack((pos[0,0]+hs*(1-pos[0,2]),pos[0,1]*0,pos[0,2]*0+1)).reshape(1,3)
        posfull=torch.cat((pos,torch.cat((tip,tip[:1]*0)).reshape(1,3)))
        cross=torch.cat((torch.flip(posfull,(0,))*torch.tensor([1.,-1.,1.]),centre,posfull))
        r=cross[:,2]
        dt=torch.diff(self.x);a=r[:-1];b=r[1:]
        w0=dt*(3*a*a+2*a*b+b*b)/12
        w1=dt*(a*a+2*a*b+3*b*b)/12
        w=torch.cat((w0,w0[:1]*0))+torch.cat((w1[:1]*0,w1))
        cy=(w*cross[:,0]).sum()/w.sum()
        cross=cross-torch.stack((cy,cy*0,cy*0))
        vertices=torch.cat((torch.cat((self.x[:1],cross[0,:2])).reshape(1,3),
           torch.cat((self.x[1:-1,None,None].expand(-1,n,1),
                      cross[1:-1,None,:2]+r[1:-1,None,None]*poly[None,:,:]),2).reshape(-1,3),
           torch.cat((self.x[-1:],cross[-1,:2])).reshape(1,3)))
        de=torch.roll(poly,-1,0)-poly
        normals=torch.stack((de[:,1],-de[:,0]),1)
        normals=normals/torch.linalg.vector_norm(normals,dim=1)[:,None]
        support=(normals*poly).sum(1)
        B=cross[:,:2]@normals.T+r[:,None]*support[None,:]
        slope=torch.diff(B,dim=0)/dt[:,None]
        H=B[:-1]-slope*self.x[:-1,None]
        N=torch.cat((-slope[:,:,None],normals[None,:,:].expand(len(dt),-1,-1)),2)
        polar=(N/H[:,:,None]).reshape(-1,3)
        return vertices,polar,slope,poly,r,H,cy
    def evaluate(self,y,mu=20.,eps=0.0005):
        v,q,sl,poly,r,H,cy=self.unpack(y)
        def scores(a,src,dst):
            d=a[dst]-a[src]
            s=(a[src]*d).sum(1)/(torch.linalg.vector_norm(a[src],dim=1)*torch.linalg.vector_norm(d,dim=1)+1e-18)
            out=torch.full((len(a),),-1e5)
            return out.scatter_reduce(0,src,s,reduce='amax',include_self=True)
        po=scores(v,self.src,self.dst);qo=scores(q,self.psrc,self.pdst)
        pm=torch.ones(len(po),dtype=torch.bool);pm[self.root]=False
        qm=torch.ones(len(qo),dtype=torch.bool);qm[self.sfaces]=False
        losses=torch.cat((torch.relu(eps-po[pm]),torch.relu(eps-qo[qm]),torch.relu(po[self.root:self.root+1]+eps),torch.relu(qo[self.sfaces]+eps)))
        # Concavity is a finite exact condition, regularity penalties are scouting only.
        conc=torch.relu(torch.diff(sl,dim=0)).ravel()
        pd=torch.roll(poly,-1,0)-poly
        convex=pd[:,0]*torch.roll(pd[:,1],-1)-pd[:,1]*torch.roll(pd[:,0],-1)
        constraints=torch.cat((conc,torch.relu(.002-r[1:-1]),torch.relu(.002-H).ravel(),torch.relu(.002-convex)))
        obj=(losses*losses).sum()+mu*(constraints*constraints).sum()
        return obj,(po,qo,conc,cy,v,q)
    def report(self,y):
        with torch.no_grad():
            val,(po,qo,cc,cy,v,q)=self.evaluate(torch.tensor(y))
            return dict(loss=float(val),U=torch.nonzero(po<0).flatten().tolist(),S=torch.nonzero(qo<0).flatten().tolist(),
                        max_concavity_violation=float(cc.max()),cy=float(cy),max_pos_target_U=float(po[self.root]),
                        polygon=self.unpack(torch.tensor(y))[3].tolist())
    def solve(self,y0,steps=400,mu=30,eps=0.0005):
        def fun(y):
            yt=torch.tensor(y,requires_grad=True)
            val,_=self.evaluate(yt,mu=mu,eps=eps);val.backward()
            return float(val.detach()),yt.grad.numpy().copy()
        return minimize(fun,y0,jac=True,method='L-BFGS-B',options={'maxiter':steps,'ftol':1e-15,'gtol':1e-9,'maxls':30,'maxcor':15})

if __name__=='__main__':
    n=int(sys.argv[1]) if len(sys.argv)>1 else 7
    k=int(sys.argv[2]) if len(sys.argv)>2 else 5
    free=int(sys.argv[3]) if len(sys.argv)>3 else 0
    seed=int(sys.argv[4]) if len(sys.argv)>4 else 0
    M=Model(n,k,bool(free));y=M.y0.copy();rng=np.random.default_rng(seed)
    if seed:y+=rng.normal(0,.025,len(y))
    stem=f'stack_{n}_{k}_{free}_{seed}'
    print('INITIAL',M.report(y),flush=True)
    for stage,mu in enumerate([30,100,300,1000,10000]):
        r=M.solve(y,500,mu);y=r.x
        rep=M.report(y);print('STAGE',stage,rep,flush=True)
        Path(stem+'.json').write_text(json.dumps({'n':n,'k':k,'free':free,'seed':seed,'y':y.tolist(),'stage':stage,'mu':mu,'report':rep},sort_keys=True))
```

## stack_green.py
```python
"""Convexity-by-construction C2 homothetic polygon stacks.
Finite numerical search. Hard geometry via Green kernels; no exclusion claim.
"""
import os
os.environ['OMP_NUM_THREADS']='1'
import sys,json
from pathlib import Path
import numpy as np
import torch
from stack_opt import Model
from stack_scout import initial

def mean_value(poly,p):
    v=poly-p;r=np.linalg.norm(v,axis=1)
    if r.min()<1e-10:
        w=np.zeros(len(poly));w[r.argmin()]=1;return w
    cs=np.sum(v*np.roll(v,-1,axis=0),axis=1)/(r*np.roll(r,-1))
    sn=(v[:,0]*np.roll(v[:,1],-1)-v[:,1]*np.roll(v[:,0],-1))/(r*np.roll(r,-1))
    tan=sn/(1+cs)
    w=(tan+np.roll(tan,1))/r
    if np.any(w<=0):return np.ones(len(poly))/len(poly)
    return w/w.sum()

class GreenModel(Model):
    def __init__(self,n=7,k=5):
        super().__init__(n,k,False)
        base=Model(n,k,False)
        with torch.no_grad():
            vv,_,_,poly,r,_,_=base.unpack(torch.tensor(base.y0))
        layers,_=initial(n,2*k+1)
        # Recover the actual section centres from the old vertices.
        centres=np.vstack((vv[0,1:].numpy(),vv[1:-1,1:].numpy().reshape(2*k+1,n,2).mean(1),vv[-1,1:].numpy()))
        axis=base.x.numpy()/float(base.x[-1]);self.axis=torch.tensor(axis)
        t=axis[1:-1]
        gg=np.where(axis[:,None]<=t[None,:],(axis[:,None]+1)*(1-t[None,:])/2,(t[None,:]+1)*(1-axis[:,None])/2)
        self.green=torch.tensor(gg)
        dr=np.diff(r.numpy())/np.diff(axis)
        aa=-np.diff(dr)
        d2=np.diff(np.diff(centres,axis=0)/np.diff(axis)[:,None],axis=0)
        kk=d2/aa[:,None]
        logits=[]
        for point in kk[k+1:]:
            w=mean_value(poly.numpy(),point)
            logits.extend(np.log(np.maximum(w,1e-10)))
        self.y0=np.r_[np.log(np.maximum(aa[k:],1e-6)),np.array(logits),centres[-1,1],np.log(float(base.x[-1]))]
        self.poly0=poly
    def unpack(self,y):
        n,k=self.n,self.k
        ap=torch.exp(y[:k+1])
        aa=torch.cat((torch.flip(ap[1:],(0,)),ap))
        weights=torch.softmax(y[k+1:k+1+k*n].reshape(k,n),dim=1)
        kp=weights@self.poly0
        middle=torch.tensor([float(self.poly0[(n-1)//2,0]),0.]).reshape(1,2)
        kk=torch.cat((torch.flip(kp,(0,))*torch.tensor([1.,-1.]),middle,kp))
        r=self.green@aa
        d=-(self.green@(aa[:,None]*kk))
        r0=r[k+1]
        r=r/r0;d=d/r0
        alpha=y[-2]
        d=d+torch.stack((self.axis*0,alpha*self.axis),1)
        x=self.axis*torch.exp(y[-1])
        dt=torch.diff(x);a=r[:-1];b=r[1:]
        w0=dt*(3*a*a+2*a*b+b*b)/12
        w1=dt*(a*a+2*a*b+3*b*b)/12
        w=torch.cat((w0,w0[:1]*0))+torch.cat((w1[:1]*0,w1))
        cy=(w*d[:,0]).sum()/w.sum()
        d=d-torch.stack((cy,cy*0))
        poly=self.poly0
        v=torch.cat((torch.cat((x[:1],d[0])).reshape(1,3),
          torch.cat((x[1:-1,None,None].expand(-1,n,1),d[1:-1,None,:]+r[1:-1,None,None]*poly[None,:,:]),2).reshape(-1,3),
          torch.cat((x[-1:],d[-1]).reshape(1,3)))
        de=torch.roll(poly,-1,0)-poly
        normals=torch.stack((de[:,1],-de[:,0]),1)
        normals=normals/torch.linalg.vector_norm(normals,dim=1)[:,None]
        support=(normals*poly).sum(1)
        B=d@normals.T+r[:,None]*support[None,:]
        sl=torch.diff(B,dim=0)/dt[:,None]
        H=B[:-1]-sl*x[:-1,None]
        N=torch.cat((-sl[:,:,None],normals[None,:,:].expand(len(dt),-1,-1)),2)
        q=(N/H[:,:,None]).reshape(-1,3)
        return v,q,sl,poly,r,H,cy
    def run(self,seed=0,iterations=6000,lr=.004,start=None):
        rng=np.random.default_rng(seed);y0=self.y0.copy() if start is None else np.array(start)
        if seed:y0+=rng.normal(0,.25,len(y0))
        y=torch.tensor(y0,requires_grad=True);opt=torch.optim.Adam([y],lr=lr)
        stem=f'green_{self.n}_{self.k}_{seed}'
        best=1e100
        for it in range(iterations+1):
            opt.zero_grad();val,_=self.evaluate(y,mu=10.,eps=.0001);val.backward()
            torch.nn.utils.clip_grad_norm_([y],10);opt.step()
            if float(val.detach())<best:
                best=float(val.detach());by=y.detach().numpy().copy()
            if it%1000==0 or it==iterations:
                rep=self.report(y.detach().numpy());print(it,rep,flush=True)
                Path(stem+'.json').write_text(json.dumps(dict(n=self.n,k=self.k,seed=seed,iteration=it,y=by.tolist(),report=self.report(by)),sort_keys=True))
        return by

if __name__=='__main__':
    n,k,seed=map(int,sys.argv[1:4]);m=GreenModel(n,k)
    print('INITIAL',m.report(m.y0),flush=True)
    m.run(seed)
```
