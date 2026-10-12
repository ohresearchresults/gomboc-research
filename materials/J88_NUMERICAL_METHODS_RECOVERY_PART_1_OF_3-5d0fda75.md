# material-5d0fda75fa95

AI research material · [Export notes](../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

# Recovery capsule part 1/3 — J88 numerical methods

Object identity: J88_NUMERICAL_METHODS. Three ordered readable parts preserve the complete new producing algorithms, not a claim of exact floating-output portability. Part1 contains finite88.py, fullchart88.py, clearance88.py; part2 contains rootchart88.py,s1flow88.py,bundle88.py,tree88.py; part3 contains bridge88.py,longbridge88.py and experiment commands. Each fenced source is a complete file including its final newline. Files shared across parts are imports, not omitted helpers.

Dependencies: extract the complete `parallel.py` from immutable [internal-source-reference] (J87_CONTINUATION_RECOVERY.md, SHA17577b959d91488e3e961589f0fd205bbf4d06e596f407df8fc45238ddd40882); parallel.py is7146B/SHA16fd7f6c76dea98e28e8fc59df14a622c16954e01521c7e56b4114862fe78b45 and has no local imports. The default base input is the complete literal J85_DETACHED_CONTINUED_B_G12_INPUT.json from [internal-source-reference]:2029B/SHAecb57f2d9acd94f1bf4fb0af01ba40f6596d13f081823ffb7c23332de4a36232. The exact robust descendant input is generated without optimization by [internal-source-reference] J88_REPLAY.py.txt. Save that as J88_REPLAY.py and run `python J88_REPLAY.py`; the observed marker is J88_EXACT_RECONSTRUCTION_PASS_OWN121_NOT_110 and G8 INPUT1431B/SHA9ce7afd63030c533c48f553a626c7b2ade91bb34bd2d55d8d81d4e12c8f75ffd is produced.

Actual producing environment: CPython3.13.5,GCC14.2.0; NumPy2.3.5; SciPy1.17.0; PyTorch2.10.0+cpu, float64, torch1thread, OPENBLAS_NUM_THREADS=1,OMP_NUM_THREADS=1. This is an environment record, not a claim that those versions will remain downloadable. Every algorithm below is numerical nomination. The imported numerical bars helper drops depths<=1e-14 and is NOT the exact acceptance checker; the independent exact Fraction routine in the replay retains every positive bar. Floating roots have no weak-census authority. There is no seeded stochastic optimization in these new methods. Exact final checkpoint bytes, rather than optimizer replay, define the preserved own121 objects.

Producing sequence for the robust endpoint:
`python finite88.py --cycles 2 --trust .04 --method lp --out J88_FINITE_A.json` was a separate nearly stalled14-direction experiment; it is not the source of the full-chart endpoint.
With J88_WITNESS_FLOOR unset or0, run
`python clearance88.py --out J88_CLEAR_A.json --steps 2 --trust .01 --pbound .451`
`python clearance88.py --input J88_CLEAR_A.json --out J88_CLEAR_B.json --steps 4 --trust .01 --pbound .451`
then `J88_WITNESS_FLOOR=1e-5 python fullchart88.py --input J88_CLEAR_B.json --out J88_FULL_B.json --steps 4 --trust .003`.
The two clearance phases reached minimum angular guard7.6393545254e-5 with P .4488089773629702; four subsequent steps reached P .44770137513387864. G8/G6 rounding and exact fixed-volume repair are preserved literally in J88_REPLAY; they are not aliases of each other. Current fullchart88.py includes a later target-empty-P handling patch: zero loss when P is empty and stop on target. Completed producing steps all had positive P, so this patch does not change their intended control path.

A separate continuation `J88_WITNESS_FLOOR=1e-5 python fullchart88.py --input J88_FULL_B_G8_INPUT.json --out J88_FULL_C.json --steps 3 --trust .005` reached numerical own-nominated121,P .44727218872668384. No exact census or durable literal endpoint was asserted for C at this preservation step. The earlier requested8-step FULL_A experiment ended after only3 completed steps; do not infer eight completed iterations.

## finite88.py — 5414 bytes; SHA610696f53e1f2282cd1f41861eaf9f883d8596355b72bf4fe37a75ff5864857e
```python
"""J88 finite parallel charts on exact detached-B input; numerical nomination only.
Requires the complete preserved parallel.py. All target weak/strict claims must be
resolved by a separate exact endpoint audit. No negative guard is imposed on U40.
"""
import argparse,json,time
from pathlib import Path
import numpy as np
from scipy.optimize import linprog, minimize, LinearConstraint, NonlinearConstraint
from parallel import Chart, hull, mass, edges, bars
ROOT=Path(__file__).resolve().parent

def angular_scores(x):
    """Global normalized outgoing chord score and derivative of an active witness."""
    delta=x[None,:,:]-x[:,None,:]
    a=np.linalg.norm(x,axis=1); b=np.linalg.norm(delta,axis=2)
    np.fill_diagonal(b,1.)
    val=np.einsum('ik,ijk->ij',x,delta)/(a[:,None]*b)
    np.fill_diagonal(val,-np.inf)
    j=val.argmax(axis=1); i=np.arange(len(x)); f=val[i,j]; d=delta[i,j]; length=b[i,j]
    G=np.zeros((len(x),len(x),3)); ratio=(a*length)[:,None]
    G[i,i]=(d-x)/ratio-f[:,None]*x/a[:,None]**2+f[:,None]*d/length[:,None]**2
    G[i,j]=x/ratio-f[:,None]*d/length[:,None]**2
    return f,G,j

def fields(c,z,deriv=True):
    s=c.Z@z; cg=c.linear_c+2*c.H@s; p=c.points(s)
    n=c.n0+np.einsum('ikj,j->ik',c.dn,s)
    h=c.h0+c.hlin@s-c.nd*(c.linear_c@s+s@c.H@s);q=n/h[:,None]
    fp,Gp,jp=angular_scores(p);fq,Gq,jq=angular_scores(q)
    if not deriv:return fp,fq,jp,jq
    gp=Gp@c.d;gp-=gp.sum(axis=1)[:,None]*cg
    dh=c.hlin-c.nd[:,None]*cg
    dq=c.dn/h[:,None,None]-n[:,:,None]*dh[:,None,:]/h[:,None,None]**2
    gq=np.einsum('afk,fkj->aj',Gq,dq)
    return fp,fq,gp@c.Z,gq@c.Z,jp,jq

def report(p):
    f=hull(p);v,g=mass(p,f);p=p-g;e,de=edges(f)
    n=np.cross(p[f[:,1]]-p[f[:,0]],p[f[:,2]]-p[f[:,0]])
    q=n/np.einsum('ij,ij->i',n,p[f[:,0]])[:,None]
    fp,_,_=angular_scores(p);fq,_,_=angular_scores(q)
    P,_=bars(p,e);Q,_=bars(q,de)
    P.sort(reverse=True);Q.sort(reverse=True)
    return dict(V=len(np.unique(f)),E=len(e),F=len(f),volume=float(v),centroid=g.tolist(),
                U=np.where(fp<0)[0].tolist(),S=[f[i].tolist() for i in np.where(fq<0)[0]],
                P=P,Q=Q,minQ=float(np.sort(fq)[1]),minP=float(np.sort(fp)[2]))

def step(p,d,trust=.02,method='lp',maxiter=100):
    c=Chart(p,d);z0=np.zeros(c.Z.shape[1]);fp,fq,gp,gq,*_=fields(c,z0)
    rp=np.where(fp<0)[0];rq=np.where(fq<0)[0]
    if len(rq)!=1 or len(rp)>2:return p,dict(error='initial census',U=rp.tolist(),S=rq.tolist())
    elder=int(np.argmax(np.sum(c.p**2,axis=1))); stable=int(rq[0])
    ip=np.ones(c.N,dtype=bool);ip[rp]=False
    iq=np.arange(len(c.f))!=stable
    gf=np.r_[fp[ip],fq[iq],-fp[elder],-fq[stable]]
    reserves=np.minimum(gf*.05,1e-7)
    def guards(z,jac=False):
        f1,f2,g1,g2,*_=fields(c,z)
        return (np.vstack([g1[ip],g2[iq],-g1[elder],-g2[stable]]) if jac
                else np.r_[f1[ip],f2[iq],-f1[elder],-f2[stable]]-reserves)
    value,grad=c.loss(z0,wq=0.)
    def feasible(z):
        return guards(z).min()>-2e-14 and (c.rhs-c.KZ@z).min()>1e-14 and np.max(abs(c.Z@z))<=trust*(1+1e-7)
    if method=='lp':
        gj=guards(z0,True)
        A=np.vstack([c.KZ,c.Z,-c.Z,-gj])
        b=np.r_[c.rhs*.999,np.full(c.N,trust),np.full(c.N,trust),guards(z0)*.95]
        opt=linprog(grad,A_ub=A,b_ub=b,bounds=[(None,None)]*len(z0),method='highs',options={'primal_feasibility_tolerance':1e-9,'dual_feasibility_tolerance':1e-9})
    else:
        con=[LinearConstraint(c.KZ,-np.inf,c.rhs-np.minimum(1e-13,c.rhs*.001)),LinearConstraint(c.Z,-trust,trust),NonlinearConstraint(guards,0,np.inf,jac=lambda z:guards(z,True))]
        opt=minimize(lambda z:c.loss(z,wq=0),z0,jac=True,method='SLSQP',constraints=con,options={'maxiter':maxiter,'ftol':1e-14})
    result=dict(direction=list(d),initial=value,success=bool(opt.success),message=str(opt.message))
    if opt.x is None:return p,result
    for k in range(36):
        alpha=2.**(-k);z=alpha*opt.x
        if feasible(z) and c.loss(z,wq=0)[0]<value-1e-12:
            pp=c.points(c.Z@z); r=report(pp)
            if len(r['S'])==1 and len(r['U'])<=2 and not r['Q']:
                result.update(alpha=alpha,loss=float(c.loss(z,wq=0)[0]),s=(c.Z@z).tolist(),guard=float(guards(z).min()),slack=float((c.rhs-c.KZ@z).min()),actual=r)
                return pp,result
    result.update(alpha=0,loss=value)
    return p,result

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--input',default='J85_DETACHED_CONTINUED_B_G12_INPUT.json');ap.add_argument('--out',default='J88_FINITE.json');ap.add_argument('--cycles',type=int,default=1);ap.add_argument('--trust',type=float,default=.02);ap.add_argument('--method',default='lp');a=ap.parse_args()
    data=json.loads((ROOT/a.input).read_text());p=np.array(data['points'],float)/data.get('denominator',1)
    dirs=[[1,0,0],[0,1,0],[0,0,1],[1,1,1],[1,2,3],[2,-1,1],[-1,1,2]];hist=[];base=report(p);start=time.monotonic()
    print('BASE',base,flush=True)
    for k in range(a.cycles):
        for d in dirs:
            pp,r=step(p,d,a.trust,a.method);hist.append(r)
            if r.get('alpha',0)>0:p=pp
            (ROOT/a.out).write_text(json.dumps(dict(points=p.tolist(),parameters=vars(a),history=hist,baseline=base,final=report(p)),sort_keys=True,indent=2)+'\n')
            print(k,d,{key:v for key,v in r.items() if key not in ['s','actual']}, 'elapsed',time.monotonic()-start,flush=True)
    print('FINAL',report(p),flush=True)
if __name__=='__main__':main()
```

## fullchart88.py — 7512 bytes; SHA2a80c83aadb9643ac667a51c9ea73f57db78a660174a30c214b7143b7de0be81
```python
"""Unrestricted rational volume-corrector chart; numerical candidate generation.
Dependencies finite88.py, parallel.py; PyTorch differentiation is nomination only.
All vertices move together. U40 is allowed to cancel; extra nonroots stay excluded.
"""
import argparse,json,time,os
from pathlib import Path
import numpy as np,torch
from scipy.optimize import linprog
from parallel import hull,mass,edges,bars
from finite88 import report
ROOT=Path(__file__).resolve().parent
torch.set_default_dtype(torch.float64);torch.set_num_threads(1)

def tmass(p,f):
    t=p[f];D=(t[:,0]*torch.linalg.cross(t[:,1],t[:,2])).sum(1)
    return D.sum()/6,(D[:,None]*t.sum(1)).sum(0)/(4*D.sum())

def score(p):
    delta=p[None,:,:]-p[:,None,:];dd=torch.linalg.vector_norm(delta,dim=2)
    aa=torch.linalg.vector_norm(p,dim=1)
    val=(p[:,None,:]*delta).sum(2)/(aa[:,None]*torch.clamp(dd,min=1e-30))
    return (val-torch.eye(len(p))*4).max(1).values

class Model:
    def __init__(self,p,bar):
        self.f=hull(p);self.N=len(p);v,g=mass(p,self.f);self.p=torch.tensor(p-g);self.v=float(v);self.tf=torch.tensor(self.f)
        # Fix three raw anchor coordinates to remove translations, and solve one volume coordinate.
        A=np.zeros_like(p)
        for f in self.f:
            a,b,c=p[f]
            for i,n in zip(f,[np.cross(b,c),np.cross(c,a),np.cross(a,b)]):A[i]+=n/6
        A[0]=0;self.pivot=tuple(map(int,np.unravel_index(abs(A).argmax(),A.shape)))
        self.free=np.array([i for i in range(3*self.N) if i>=3 and i!=3*self.pivot[0]+self.pivot[1]])
        self.embedding=torch.eye(3*self.N)[:,self.free]
        self.mask=torch.zeros_like(self.p);self.mask[self.pivot]=1
        self.cf=torch.tensor([np.roll(f,-list(f).index(self.pivot[0])) for f in self.f if self.pivot[0] in f])
        self.aden=float(self.coef(self.p))
        ed,de=edges(self.f);tet=[]
        for fs in de:
            f=list(self.f[fs[0]]);other=next(v for v in self.f[fs[1]] if v not in f);tet.append(f+[int(other)])
        self.tet=torch.tensor(tet)
        tri=self.p[self.tf];n=torch.linalg.cross(tri[:,1]-tri[:,0],tri[:,2]-tri[:,0]);h=(n*tri[:,0]).sum(1);q=n/h[:,None]
        gp=score(self.p).numpy();gq=score(q).numpy();self.elder=int(np.argmax(np.sum(np.array(self.p)**2,axis=1)))
        roots=np.where(gp<0)[0];rq=np.where(gq<0)[0]
        assert len(rq)==1 and len(roots)<=2,(roots,rq)
        self.ip=torch.tensor([i for i in range(self.N) if i not in roots]);self.iq=torch.tensor([i for i in range(len(self.f)) if i!=rq[0]])
        self.rq=int(rq[0]);self.root,self.ea,self.eb=map(int,bar[1:])
        t=self.p[self.tet];self.scale=torch.clamp(torch.linalg.vector_norm(torch.linalg.cross(t[:,1]-t[:,0],t[:,2]-t[:,0]),dim=1),min=1e-8)
        self.AREA=torch.linalg.vector_norm(n,dim=1)*.01
        z=torch.zeros(len(self.free));base=self.rawguards(z)
        self.reserve=torch.clamp(base*.05,max=1e-7)
        floor=float(os.environ.get("J88_WITNESS_FLOOR","0"))
        self.reserve[:len(self.ip)+len(self.iq)+2]=torch.clamp(self.reserve[:len(self.ip)+len(self.iq)+2],min=floor)
        assert float(base.min())>0,('base guard',float(base.min()))
    def coef(self,y):
        t=y[self.cf]
        return torch.linalg.cross(t[:,1],t[:,2])[:,self.pivot[1]].sum()/6
    def points(self,z):
        y=self.p+(self.embedding@z).reshape(self.N,3);v,_=tmass(y,self.tf)
        y=y+(self.v-v)/self.coef(y)*self.mask
        _,g=tmass(y,self.tf)
        return y-g
    def rawguards(self,z):
        p=self.points(z);tri=p[self.tf];n=torch.linalg.cross(tri[:,1]-tri[:,0],tri[:,2]-tri[:,0]);h=(n*tri[:,0]).sum(1);q=n/h[:,None]
        gp=score(p);gq=score(q);t=p[self.tet]
        cv=-(torch.linalg.cross(t[:,1]-t[:,0],t[:,2]-t[:,0])*(t[:,3]-t[:,0])).sum(1)/self.scale
        return torch.cat([gp[self.ip],gq[self.iq],-gp[self.elder][None],-gq[self.rq][None],cv,torch.linalg.vector_norm(n,dim=1)-self.AREA])
    def guards(self,z):return self.rawguards(z)-self.reserve
    def objective(self,z):
        p=self.points(z);d=p[self.eb]-p[self.ea]
        t=torch.clamp(-(p[self.ea]*d).sum()/(d*d).sum(),0,1);foot=p[self.ea]+t*d
        return 1-(foot*foot).sum()/(p[self.root]*p[self.root]).sum()
    def vg(self,z,jac=True):
        x=torch.tensor(z);v=self.guards(x).numpy()
        J=torch.func.jacrev(self.guards,chunk_size=16)(x).numpy() if jac else None
        return v,J

def restore(m,z,trust):
    for k in range(8):
        v,J=m.vg(z)
        if v.min()>-2e-14:return z,True,k
        M=len(z);A=np.vstack([np.c_[-J,np.zeros(len(v))],np.c_[np.eye(M),-np.ones(M)],np.c_[-np.eye(M),-np.ones(M)]])
        # Restore actual nonlinear guards with a tiny positive target, not a floor on bar depths.
        b=np.r_[v-1e-12,np.zeros(2*M)]
        rr=linprog(np.r_[np.zeros(M),1.],A_ub=A,b_ub=b,bounds=[(-trust,trust)]*M+[(0,trust)],method='highs')
        if not rr.success:return z,False,k
        z=z+rr.x[:-1]
    return z,bool(m.vg(z,False)[0].min()>-2e-14),8

def step(p,trust=.01):
    f=hull(p);_,g=mass(p,f);e,_=edges(f);bs,_=bars(p-g,e);bs.sort(reverse=True)
    if not bs:return p,{'target':True}
    m=Model(p,[bs[0][0],bs[0][1],*bs[0][2]]);z0=np.zeros(len(m.free));v,J=m.vg(z0)
    z=torch.tensor(z0,requires_grad=True);old=m.objective(z);old.backward();gg=z.grad.numpy()
    r=linprog(gg,A_ub=-J,b_ub=v*.95,bounds=[(-trust,trust)]*len(z0),method='highs',options={'primal_feasibility_tolerance':1e-9,'dual_feasibility_tolerance':1e-9})
    out=dict(initial=float(old),pivot=m.pivot,predicted=None if r.fun is None else float(r.fun),lp_success=bool(r.success))
    if not r.success:return p,out
    for k in range(15):
        alpha=2.**-k;zz,ok,ns=restore(m,alpha*r.x,trust*alpha*.5)
        if not ok:continue
        pp=m.points(torch.tensor(zz)).numpy();rr=report(pp)
        newloss=rr['P'][0][0] if rr['P'] else 0.
        if len(rr['S'])==1 and len(rr['U'])<=2 and not rr['Q'] and newloss<float(old)-1e-11:
            # A fixed-face retraction only certifies physical volume when its facet support complex survives.
            newf={tuple(sorted(t)) for t in hull(pp)};oldf={tuple(sorted(t)) for t in f}
            if newf!=oldf:continue
            out.update(alpha=alpha,restore=ns,loss=newloss,target=(not rr['P'] and len(rr['U'])==1),params=zz.tolist(),actual=rr,min_guard=float(m.vg(zz,False)[0].min()),max_move=float(abs(pp-np.array(m.p)).max()))
            return pp,out
    out.update(alpha=0,loss=float(old));return p,out

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--input',default='J85_DETACHED_CONTINUED_B_G12_INPUT.json');ap.add_argument('--out',default='J88_FULL.json');ap.add_argument('--steps',type=int,default=8);ap.add_argument('--trust',type=float,default=.01);a=ap.parse_args()
    data=json.loads((ROOT/a.input).read_text());p=np.array(data['points'],float)/data.get('denominator',1);hist=[];start=time.monotonic();rad=a.trust
    for k in range(a.steps):
        pp,r=step(p,rad);hist.append(r)
        if r.get('alpha',0)>0:
            p=pp
            if r['alpha']>=.5:rad=min(rad*1.25,.04)
        else:rad*=.5
        if r.get('alpha',1)<.125:rad*=.75
        (ROOT/a.out).write_text(json.dumps(dict(points=p.tolist(),parameters=vars(a),history=hist,final=report(p)),sort_keys=True,indent=2)+'\n')
        print(k,{key:v for key,v in r.items() if key not in ['params','actual']},'time',time.monotonic()-start,'next_trust',rad,flush=True)
        if r.get('target') or rad<1e-7:break
    print('FINAL',report(p),flush=True)
if __name__=='__main__':main()
```

## clearance88.py — 2863 bytes; SHA8936595518df0028d1bcddf30fb60bd0a48a02d9cc6bda26ed8b8f7823f5349d
```python
"""Finite full-coordinate volume-chart clearance phase with an explicit P budget.
Does not assert strictness from numerical thresholds. Final endpoints require exact audit.
"""
from fullchart88 import *

def step_clear(p,trust=.005,pbound=.451):
    f=hull(p);_,g=mass(p,f);e,_=edges(f);bs,_=bars(p-g,e);bs.sort(reverse=True)
    if not bs:return p,dict(target=True)
    m=Model(p,[bs[0][0],bs[0][1],*bs[0][2]]);z0=np.zeros(len(m.free));v,J=m.vg(z0)
    count=len(m.ip)+len(m.iq)+2;old=float(m.rawguards(torch.tensor(z0))[:count].min())
    z=torch.tensor(z0,requires_grad=True);dep=m.objective(z);dep.backward();gg=z.grad.numpy()
    # Common clearance t on all present exclusion/root witnesses, without constraining extra U40 negative.
    A=np.c_[-J,np.r_[np.ones(count),np.zeros(len(v)-count)]]
    b=v.copy();b[:count]+=m.reserve[:count].numpy()
    A=np.vstack([A,np.r_[gg,0.]]);b=np.r_[b,pbound-float(dep)]
    r=linprog(np.r_[np.zeros(len(z0)),-1.],A_ub=A,b_ub=b,bounds=[(-trust,trust)]*len(z0)+[(old,None)],method='highs',options={'primal_feasibility_tolerance':1e-9,'dual_feasibility_tolerance':1e-9})
    out=dict(old_clearance=old,initial_P=float(dep),lp_success=bool(r.success),message=str(r.message),pivot=m.pivot)
    if not r.success:return p,out
    out['predicted_clearance']=float(r.x[-1])
    for k in range(15):
        alpha=2.**-k;zz,ok,ns=restore(m,alpha*r.x[:-1],trust*alpha*.5)
        if not ok:continue
        pp=m.points(torch.tensor(zz)).numpy();rr=report(pp);vv=m.rawguards(torch.tensor(zz)).numpy();new=float(vv[:count].min())
        if len(rr['S'])==1 and len(rr['U'])<=2 and not rr['Q'] and rr['P'][0][0]<pbound and new>old+1e-11:
            if {tuple(sorted(t)) for t in hull(pp)}!={tuple(sorted(t)) for t in f}:continue
            out.update(alpha=alpha,restore=ns,clearance=new,P=rr['P'][0][0],params=zz.tolist(),actual=rr)
            return pp,out
    return p,dict(out,alpha=0)

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--input',default='J85_DETACHED_CONTINUED_B_G12_INPUT.json');ap.add_argument('--out',default='J88_CLEAR.json');ap.add_argument('--steps',type=int,default=2);ap.add_argument('--trust',type=float,default=.002);ap.add_argument('--pbound',type=float,default=.451);a=ap.parse_args()
    data=json.loads((ROOT/a.input).read_text());p=np.array(data['points'],float)/data.get('denominator',1);hist=[];start=time.monotonic()
    for k in range(a.steps):
        pp,r=step_clear(p,a.trust,a.pbound);hist.append(r)
        if r.get('alpha',0)>0:p=pp
        (ROOT/a.out).write_text(json.dumps(dict(points=p.tolist(),parameters=vars(a),history=hist,final=report(p)),sort_keys=True,indent=2)+'\n')
        print(k,{key:v for key,v in r.items() if key not in ['params','actual']},'time',time.monotonic()-start,flush=True)
    print('FINAL',report(p),flush=True)
if __name__=='__main__':main()
```
