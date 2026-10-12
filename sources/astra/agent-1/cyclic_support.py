"""Cyclic-symmetric physical support families, always integrated at own centroid.

Smooth seed equations are (1)--(5) in Domokos/Langi/Varkonyi (2023), DOI
10.1007/s00605-023-01847-w. This is a coarse polyhedral sampling and an independent
deformation experiment; no theorem transfers the smooth census to these bodies.
One axial bottom support plus m cyclic n-orbits gives <=1+mn facets.
All reported successes remain nominations pending full rational physical audit.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import argparse,json,pathlib,time
import numpy as np
import torch
from scipy.linalg import svd
from scipy.optimize import linprog
from scipy.sparse import csr_matrix,eye,hstack,vstack
from geometry import halfspace_mesh,census,arrows
from persistence_search import pairs,polar_edges
from soft_forest_polish import forest
torch.set_num_threads(1);torch.set_default_dtype(torch.float64)

def radius(theta,phi,c,d,n):
    def f(t):
        x=t/torch.pi+.5
        Fc=(c*x*x+(1-c)*(1-x)**2*c*x/(c+x))/(c*x+(1-c)*(1-x)**2)
        return torch.pi*Fc-torch.pi/2
    f1=f(theta);g1=-f(-theta)
    aa=torch.cos(n*phi/2)**2*torch.cos(f1)**2
    bb=torch.sin(n*phi/2)**2*torch.cos(g1)**2
    mix=aa/(aa+bb)
    return 1+d*(mix*torch.sin(f1)+(1-mix)*torch.sin(g1))

def seed(m=27,n=3,c=.2,d=.1,offset=0.):
    zz=-.97+1.94*(np.arange(m)+.5)/m
    theta=torch.tensor(np.arcsin(zz),requires_grad=True)
    phi=torch.tensor((np.arange(m)*np.pi*(3-np.sqrt(5))+offset)%(2*np.pi/n),requires_grad=True)
    r=radius(theta,phi,c,d,n)
    rt,rp=torch.autograd.grad(r.sum(),(theta,phi))
    u=torch.stack([torch.cos(theta)*torch.cos(phi),torch.cos(theta)*torch.sin(phi),torch.sin(theta)],1)
    et=torch.stack([-torch.sin(theta)*torch.cos(phi),-torch.sin(theta)*torch.sin(phi),torch.cos(theta)],1)
    ep=torch.stack([-torch.sin(phi),torch.cos(phi),torch.zeros_like(phi)],1)
    q=(u-(rt/r)[:,None]*et-(rp/(r*torch.cos(theta)))[:,None]*ep)/r[:,None]
    return np.r_[q.detach().numpy().ravel(),1/(1-d)]

class Cyclic:
    def __init__(self,m=27,n=3):
        self.m=m;self.n=n;self.d=3*m+1
        phi=np.arange(n)*2*np.pi/n
        rot=np.zeros((n,3,3));rot[:,0,0]=np.cos(phi);rot[:,0,1]=-np.sin(phi);rot[:,1,0]=np.sin(phi);rot[:,1,1]=np.cos(phi);rot[:,2,2]=1
        self.rot=torch.tensor(rot)
    def expand(self,z):
        q=z[:-1].reshape(self.m,3)
        side=torch.einsum('rij,mj->mri',self.rot,q).reshape(-1,3)
        return torch.cat([torch.stack([z[-1]*0,z[-1]*0,-z[-1]])[None,:],side])
    def eval(self,z,jacobian=False,losskind='log',mechanical='local'):
        Q=self.expand(torch.tensor(z)).detach().numpy()
        if z[-1]<=0:raise ValueError('bottom support must face down')
        m=halfspace_mesh(Q)
        if len(m['edges'])<17:raise ValueError('outside requested complexity search range')
        if abs(m['g'][:2]).max()>1e-8:raise ValueError('cyclic centroid inconsistency')
        st=census(m,0);P=m['X']-m['g'];R=Q[m['active']]/(1-Q[m['active']]@m['g'])[:,None]
        # Unique allowed maximum is the top axial vertex. The bottom axial face
        # is the single permitted polar maximum. A missing axial carrier is not
        # silently replaced by a threefold orbit member.
        radial=np.linalg.norm(P[:,:2],axis=1)
        cand=np.flatnonzero(radial<1e-7)
        if not len(cand):raise ValueError('designated axial unstable carrier is absent')
        rootP=int(cand[np.argmax(P[cand,2])])
        rootQ=int(np.where(m['active']==0)[0][0]) if 0 in m['active'] else -1
        if rootQ<0:raise ValueError('designated bottom face inactive')
        roots=[rootP,rootQ]
        selected=[];vals=[]
        for A,root in zip((P,R),roots):
            W=arrows(A)
            pa=forest(A,[root]) if mechanical=='forest' else W.argmax(1)
            sg=np.ones(len(A));sg[root]=-1
            selected.append((pa,sg));vals.append(sg*W[np.arange(len(A)),pa])
        ep=m['edges'];eqglobal=polar_edges(m);remap={int(j):i for i,j in enumerate(m['active'])};eq=np.array([[remap[int(i)],remap[int(j)]] for i,j in eqglobal])
        bp,hp=pairs(P,ep);bq,hq=pairs(R,eq)
        dp=1-hp[bp[:,1]]/(P[bp[:,0]]**2).sum(1);dq=1-hq[bq[:,1]]/(R[bq[:,0]]**2).sum(1)
        out=dict(Q=Q,m=m,P=P,R=R,mechanical=np.r_[tuple(vals)],Pbars=dp.tolist(),Qbars=dq.tolist(),roots=roots,**st)
        if not jacobian:return out
        tt=torch.tensor(m['triangles']);ti=torch.tensor(m['triples']);act=torch.tensor(m['active']);zz=torch.tensor(z)
        def calc(zz):
            q=self.expand(zz);x=torch.linalg.solve(q[ti],torch.ones((len(ti),3,1)))[:,:,0]
            a=x[tt];vol=(a[:,0]*torch.linalg.cross(a[:,1],a[:,2])).sum(1)/6
            g=(vol[:,None]*a.sum(1)).sum(0)/(4*vol.sum());p=x-g;r=q[act]/(1-q[act]@g)[:,None]
            vs=[];barloss=p.sum()*0
            for A,(pa,sg),eds,pp in zip((p,r),selected,(ep,eq),(bp,bq)):
                pa=torch.tensor(pa);sg=torch.tensor(sg);delta=A[pa]-A
                vs.append(sg*(A*delta).sum(1)/(torch.linalg.vector_norm(A,dim=1)*torch.linalg.vector_norm(delta,dim=1)))
                if len(pp):
                    ed=torch.tensor(eds[pp[:,1]]);born=(A[torch.tensor(pp[:,0])]**2).sum(1);a=A[ed[:,0]];dd=A[ed[:,1]]-a
                    t=(-(a*dd).sum(1)/(dd*dd).sum(1)).clamp(0,1);dead=((a+t[:,None]*dd)**2).sum(1);bar=(1-dead/born).clamp(min=0)
                    if losskind=='log':barloss=barloss+torch.log1p(bar/.001).sum()*.001
                    elif losskind=='square':barloss=barloss+(bar*bar).sum()
                    else:barloss=barloss+bar.sum()
            return torch.cat([*vs,barloss[None],x.flatten(),q.flatten()])
        value=calc(zz).detach().numpy();J=torch.func.jacrev(calc)(zz).detach().numpy();nv=len(out['mechanical'])
        physicalJ=J[nv+1:].copy();physicalJ[:m['X'].size]/=np.sqrt(np.mean(P**2));physicalJ[m['X'].size:]/=np.sqrt(np.mean(Q**2))
        _,dd,Vt=svd(physicalJ,full_matrices=False,check_finite=False)
        if dd.min()<1e-14:raise ValueError('singular physical chart')
        out.update(J=J[:nv],loss=float(value[nv]),gradient=J[nv],W=Vt.T/dd)
        return out

def optimize(model,z,out,steps=300,objective='escape',mechanical='local',eps=2e-7):
    out=pathlib.Path(out);out.mkdir(parents=True,exist_ok=True);history=[];start=time.time();trust=.08;best=float('inf')
    for it in range(steps):
        e=model.eval(z,True,mechanical=mechanical);v=e['mechanical'];merit=float(np.maximum(eps-v,0).sum())
        score=merit if objective=='escape' else e['loss']
        row=dict(it=it,S=e['S'],U=e['U'],E=e['E'],merit=merit,loss=e['loss'],Pmax=max(e['Pbars'],default=0),Qmax=max(e['Qbars'],default=0),trust=trust,seconds=time.time()-start)
        history.append(row);(out/'history.json').write_text(json.dumps(history,indent=2));np.savez(out/'latest.npz',z=z,Q=e['Q'])
        if it%5==0:print('CYCLIC',json.dumps(row),flush=True)
        if score<best:
            best=score;np.savez(out/'best.npz',z=z,Q=e['Q']);(out/'best.json').write_text(json.dumps(row,indent=2))
        if e['S']==e['U']==1 and min(v)>1e-9:
            np.savez(out/'NOMINATION_OWN110.npz',z=z,Q=e['Q']);print('POTENTIAL_CYCLIC_OWN110_REQUIRES_EXACT',flush=True);return z,True
        W=e['W'];d=model.d;bound=trust/np.sqrt(d)
        if objective=='escape':
            nv=len(v);I=eye(d);O=csr_matrix((d,nv));A=vstack([hstack([-csr_matrix(e['J']@W),-eye(nv),csr_matrix((nv,d))]),hstack([I,O,-I]),hstack([-I,O,-I])],format='csr')
            lp=linprog(np.r_[np.zeros(d),np.ones(nv),np.full(d,1e-7)],A_ub=A,b_ub=np.r_[v-eps,np.zeros(2*d)],bounds=[(-bound,bound)]*d+[(0,None)]*(nv+d),method='highs')
            if not lp.success:
                trust*=.5
                if trust<1e-9:break
                continue
            direction=W@lp.x[:d]
        else:
            gradient=e['gradient']@W
            direction=-W@gradient*trust/max(np.linalg.norm(gradient),1e-30)
        accepted=False
        for level in range(18):
            zz=z+direction*2**-level
            try:ee=model.eval(zz,objective!='escape',mechanical=mechanical)
            except (ValueError,RuntimeError,np.linalg.LinAlgError):continue
            newscore=float(np.maximum(eps-ee['mechanical'],0).sum()) if objective=='escape' else ee['loss']
            if newscore<score*(1-1e-6*2**-level):
                z=zz;accepted=True;break
        if accepted and level==0:trust=min(.5,trust*1.3)
        if not accepted:trust*=.4
        if trust<1e-9:break
    return z,False

def scout(out,m=27,n=3):
    out=pathlib.Path(out);out.mkdir(parents=True,exist_ok=True);model=Cyclic(m,n);rows=[]
    for c in [.025,.05,.1,.2,.35,.5,.7]:
        for d in [.025,.06,.12,.22,.4,.65]:
            z=seed(m,n,c,d)
            try:e=model.eval(z)
            except (ValueError,RuntimeError,np.linalg.LinAlgError) as err:
                rows.append(dict(c=c,d=d,error=str(err)));continue
            row=dict(c=c,d=d,S=e['S'],U=e['U'],E=e['E'],Pmax=max(e['Pbars'],default=0),Qmax=max(e['Qbars'],default=0),merit=float(np.maximum(2e-7-e['mechanical'],0).sum()))
            name=f'c{c}_d{d}';np.savez(out/(name+'.npz'),z=z,Q=e['Q']);row['file']=name+'.npz';rows.append(row)
    (out/'scout.json').write_text(json.dumps(rows,indent=2));valid=[r for r in rows if 'error' not in r];print('SCOUT_BEST',sorted(valid,key=lambda r:r['merit'])[:8],flush=True)

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--out',required=True);ap.add_argument('--input');ap.add_argument('--m',type=int,default=27);ap.add_argument('--n',type=int,default=3);ap.add_argument('--steps',type=int,default=300);ap.add_argument('--objective',choices=['escape','persistence'],default='escape');ap.add_argument('--mechanical',choices=['local','forest'],default='local');a=ap.parse_args()
    if not a.input:scout(a.out,a.m,a.n)
    else:optimize(Cyclic(a.m,a.n),np.load(a.input)['z'],a.out,a.steps,a.objective,a.mechanical)
