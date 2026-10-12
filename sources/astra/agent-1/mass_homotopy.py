"""Physical-vertex continuation from a 0-skeleton to uniform-volume mass.

Only lambda=1 represents the requested density. Earlier lambda values are
explicit search scaffolding: c(lambda)=(1-lambda)*sum(w_i X_i)+lambda*g_volume.
Conway n,k seed source: Domokos/Kovacs arXiv:2103.13727 Table1.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import numpy as np,torch,json,pathlib,time,argparse
from scipy.spatial import ConvexHull
from scipy.optimize import linprog
from scipy.sparse import csr_matrix,eye,hstack,vstack
from soft_forest_polish import forest
from geometry import arrows
torch.set_num_threads(1);torch.set_default_dtype(torch.float64)

def mesh(X):
    h=ConvexHull(X);T=h.simplices.copy();a=X[T];cross=np.cross(a[:,1]-a[:,0],a[:,2]-a[:,0]);flip=(cross*h.equations[:,:3]).sum(1)<0;T[flip]=T[flip][:,[0,2,1]]
    keep=[];eq=[]
    for k,e in enumerate(h.equations):
        if any(np.max(abs(e-v))<1e-9 for v in eq):continue
        keep.append(k);eq.append(e)
    a=X[T];vv=np.einsum('ij,ij->i',a[:,0],np.cross(a[:,1],a[:,2]))/6;volume=vv.sum();g=(vv[:,None]*a.sum(1)).sum(0)/(4*volume)
    if not volume>0:raise ValueError('nonpositive volume')
    return dict(T=T,polar_triangles=T[keep],active=h.vertices,g=g,volume=volume,V=len(h.vertices),F=len(keep),E=len(h.vertices)+len(keep)-2)

def geometry(X,w,lam):
    m=mesh(X);c=lam*m['g']+(1-lam)*(w@X);P=X[m['active']]-c;Q=np.linalg.solve(X[m['polar_triangles']]-c,np.ones((m['F'],3,1)))[:,:,0]
    if np.max(Q@(X-c).T)>1+1e-6:raise ValueError('support inclusion')
    return m,c,P,Q

def guards(X,w,lam):
    m,c,P,Q=geometry(X,w,lam);parents=[];signs=[];v=[];roots=[]
    for A in [P,Q]:
        root=int(np.argmax((A*A).sum(1)));pa=forest(A,[root]);sg=np.ones(len(A));sg[root]=-1;parents.append(pa);signs.append(sg);roots.append(root);v.append(sg*arrows(A)[np.arange(len(A)),pa])
    return m,c,np.concatenate(v),parents,signs,dict(S=int(np.sum(arrows(Q).max(1)<-1e-10)),U=int(np.sum(arrows(P).max(1)<-1e-10)),rootP=int(m['active'][roots[0]]),rootQ=int(roots[1]),centroid=m['g'].tolist(),reference=c.tolist(),V=m['V'],E=m['E'],F=m['F'],lambda_mass=lam)

def check_own(X,w,out):
    m,c,v,pa,sg,st=guards(X,w,1.)
    if st['S']==st['U']==1 and min(v)>1e-9 and 17<=m['E']<250:
        np.savez(pathlib.Path(out)/'NOMINATION_OWN110.npz',X=X,w=w,lam=1.)
        (pathlib.Path(out)/'NOMINATION_OWN110.json').write_text(json.dumps(dict(minimum=float(min(v)),**st),indent=2))
        print('POTENTIAL_OWN110_REQUIRES_EXACT',flush=True);return True
    return False

def repair(X,w,lam,out,steps=150,eps=2e-6):
    out=pathlib.Path(out);out.mkdir(parents=True,exist_ok=True);trust=.01;hist=[];start=time.time()
    for it in range(steps):
        m,c,v,pa,sg,st=guards(X,w,lam);merit=float(np.maximum(eps-v,0).sum());hist.append(dict(it=it,merit=merit,minimum=float(v.min()),trust=trust,seconds=time.time()-start,**st));np.savez(out/'latest.npz',X=X,w=w,lam=lam);(out/'history.json').write_text(json.dumps(hist,indent=2))
        if it%10==0:print('REPAIR',lam,it,merit,float(v.min()),st['S'],st['U'],st['E'],trust,flush=True)
        if v.min()>eps*.8 and st['S']==st['U']==1:
            np.savez(out/'strict_reference110.npz',X=X,w=w,lam=lam);return X,True,st
        tt=torch.tensor(m['T']);tp=torch.tensor(m['polar_triangles']);ti=torch.tensor(m['active']);tw=torch.tensor(w);parents=list(map(torch.tensor,pa));signs=list(map(torch.tensor,sg))
        def calc(z):
            x=z.reshape(X.shape);a=x[tt];vol=(a[:,0]*torch.linalg.cross(a[:,1],a[:,2])).sum(1)/6;g=(vol[:,None]*a.sum(1)).sum(0)/(4*vol.sum());c=lam*g+(1-lam)*(tw@x);P=x[ti]-c;Q=torch.linalg.solve(x[tp]-c,torch.ones((len(tp),3,1)))[:,:,0];vs=[]
            for A,pp,ss in zip([P,Q],parents,signs):
                d=A[pp]-A;vs.append(ss*(A*d).sum(1)/(torch.linalg.vector_norm(A,dim=1)*torch.linalg.vector_norm(d,dim=1)).clamp(min=1e-18))
            return torch.cat(vs)
        J=torch.func.jacrev(calc)(torch.tensor(X.ravel())).detach().numpy();d=X.size;n=len(v);I=eye(d);O=csr_matrix((d,n));A=vstack([hstack([-csr_matrix(J),-eye(n),csr_matrix((n,d))]),hstack([I,O,-I]),hstack([-I,O,-I])],format='csr');b=np.r_[v-eps,np.zeros(2*d)];obj=np.r_[np.zeros(d),np.ones(n),np.full(d,1e-7)];scale=np.sqrt(np.mean((X-c)**2));bound=trust*scale
        sol=linprog(obj,A_ub=A,b_ub=b,bounds=[(-bound,bound)]*d+[(0,None)]*(n+d),method='highs',options={'primal_feasibility_tolerance':1e-9,'dual_feasibility_tolerance':1e-9})
        if not sol.success:trust*=.4;continue
        dx=sol.x[:d].reshape(X.shape);accepted=False
        for k in range(13):
            xx=X+dx*2**-k
            try:mm,cc,vv,_,_,ss=guards(xx,w,lam);newmerit=float(np.maximum(eps-vv,0).sum())
            except Exception:continue
            if newmerit<merit*(1-1e-5):X=xx;accepted=True;break
        if accepted and k==0:trust=min(.08,trust*1.2)
        if not accepted:trust*=.4
        if trust<1e-9:break
    return X,False,st

def seed(n=4,k=5,randomseed=0,extra=0):
    angles={4:[66.173,44.519,29.875,19.716],5:[59.680,43.215,29.781,20.336,13.494],7:[43.0788,43.0793,30.9129,22.1409,15.6392,10.7864,7.1815]}[n]
    X=[[0,0,1]];theta=0.;r=1.
    for a in np.deg2rad(angles):
        theta+=a;r*=np.cos(a)
        for phi in np.arange(k)*2*np.pi/k:X.append([r*np.sin(theta)*np.cos(phi),r*np.sin(theta)*np.sin(phi),r*np.cos(theta)])
    X=np.array(X);w=np.ones(len(X))/len(X);rng=np.random.default_rng(randomseed)
    X+=rng.normal(size=X.shape)*1e-7
    if extra:
        h=ConvexHull(X);ids=rng.choice(len(h.simplices),size=min(extra,len(h.simplices)),replace=False);more=[]
        for j in ids:more.append(X[h.simplices[j]].mean(0)+1e-7*h.equations[j,:3])
        X=np.vstack([X,more]);w=np.r_[w,np.zeros(len(more))]
    return X,w

def run(out,n=4,k=5,randomseed=0,extra=0,input=None,maxstages=120):
    out=pathlib.Path(out);out.mkdir(parents=True,exist_ok=True)
    if input:
        dat=np.load(input);X=dat['X'];w=dat['w'];lam=float(dat['lam'])
    else:X,w=seed(n,k,randomseed,extra);lam=0.
    np.savez(out/'initial.npz',X=X,w=w,lam=lam);hist=[];step=.05;start=time.time()
    for stage in range(maxstages):
        target=lam if stage==0 else min(1,lam+step);folder=out/f'stage{stage:03d}-lambda{target:.8f}';Y,ok,st=repair(X.copy(),w,target,folder,steps=250);row=dict(stage=stage,target=target,accepted=ok,step=step,seconds=time.time()-start,**st);hist.append(row);(out/'history.json').write_text(json.dumps(hist,indent=2));print('HOMOTOPY_STAGE',json.dumps(row),flush=True)
        if ok:
            X=Y;lam=target;np.savez(out/'latest-strict.npz',X=X,w=w,lam=lam)
            if check_own(X,w,out):return
            if lam==1:
                np.savez(out/'NOMINATION_OWN110.npz',X=X,w=w,lam=lam);print('POTENTIAL_OWN110_REQUIRES_EXACT',flush=True);return
            step=min(.1,step*1.3)
        else:step*=.5
        if step<1e-6:print('HOMOTOPY_LOCAL_STALL',lam,flush=True);break

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--out',required=True);ap.add_argument('--n',type=int,default=4);ap.add_argument('--k',type=int,default=5);ap.add_argument('--seed',type=int,default=0);ap.add_argument('--extra',type=int,default=0);ap.add_argument('--input');ap.add_argument('--stages',type=int,default=120);a=ap.parse_args();run(a.out,a.n,a.k,a.seed,a.extra,a.input,a.stages)
