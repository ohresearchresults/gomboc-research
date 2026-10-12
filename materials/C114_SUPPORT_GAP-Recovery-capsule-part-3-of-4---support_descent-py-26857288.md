# material-26857288d7de

AI research material

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

"""Own-mass numerical support-gap search; exact checking is separate.
Free mode changes all points. Affine mode changes five determinant-one parameters.
Actual hull, filled centroid and same-centre polar are recomputed on acceptance.
"""
import os
for k in ('OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','OMP_NUM_THREADS'):os.environ[k]='1'
import json,sys,time,platform
from pathlib import Path
import numpy as np
import scipy
from scipy.spatial import ConvexHull,QhullError
from scipy.optimize import minimize
import torch
torch.set_num_threads(1);torch.set_default_dtype(torch.float64)

def topology(v):
    h=ConvexHull(v)
    if len(h.vertices)!=len(v):raise ValueError('inactive input')
    t=h.simplices.copy();a,b,c=np.moveaxis(v[t],1,0)
    flip=np.einsum('ij,ij->i',np.cross(b-a,c-a),h.equations[:,:3])<0
    t[flip]=t[flip][:,[0,2,1]]
    ef={}
    for k,cy in enumerate(t):
        for i,j in zip(cy,np.roll(cy,-1)):ef.setdefault(tuple(sorted((int(i),int(j)))),[]).append(k)
    assert all(len(z)==2 for z in ef.values())
    pe=np.array(sorted(ef),int);qe=np.array([ef[tuple(e)] for e in pe],int)
    return t,pe,qe

def state(v,t):
    a,b,c=v[t[:,0]],v[t[:,1]],v[t[:,2]]
    d=(a*torch.linalg.cross(b,c)).sum(1);V=d.sum()/6
    center=(d[:,None]*(a+b+c)).sum(0)/(4*d.sum());p=v-center
    n=torch.linalg.cross(b-a,c-a);h=(n*(a-center)).sum(1)
    return p,n/h[:,None],V,center

def bars(p,edges):
    r=(p*p).sum(1);a=p[edges[:,0]];d=p[edges[:,1]]-a
    tau=np.clip(-(a*d).sum(1)/(d*d).sum(1),0,1);z=a+tau[:,None]*d;lev=(z*z).sum(1)
    par=list(range(len(p)));out=[]
    def root(i):
        while par[i]!=i:par[i]=par[par[i]];i=par[i]
        return i
    for e in np.argsort(-lev,kind='stable'):
        u,w=(root(int(i)) for i in edges[e])
        if u==w:continue
        if (r[u],-u)<(r[w],-w):u,w=w,u
        if r[w]-lev[e]>1e-13*r.max():out.append((w,u,int(e),float(r[w]),float(lev[e])))
        par[w]=u
    return out

def escape(p,edges):
    n=len(p);mask=np.zeros((n,n),bool)
    for i,j in edges:mask[i,j]=mask[j,i]=True
    d=p[None,:,:]-p[:,None,:]
    denom=torch.linalg.vector_norm(p,dim=1)[:,None]*torch.linalg.vector_norm(d,dim=2)+torch.eye(n)
    val=(p[:,None,:]*d).sum(2)/denom
    return torch.where(torch.tensor(mask),val,torch.full_like(val,-10.)).max(1).values

class Problem:
    def __init__(self,seed,mode):self.seed=torch.tensor(seed);self.mode=mode
    def points(self,z):
        if self.mode=='free':return z.reshape(-1,3)
        zero=z[0]*0
        A=torch.stack([torch.stack([torch.exp(z[0]),zero,zero]),torch.stack([z[2],torch.exp(z[1]),zero]),torch.stack([z[3],z[4],torch.exp(-z[0]-z[1])])])
        return self.seed@A.T
    def model(self,x,s,grad=True):
        with torch.no_grad():v=self.points(torch.tensor(x)).numpy()
        t,pe,qe=topology(v)
        with torch.no_grad():p,q,V,c=state(torch.tensor(v),t);pn=p.numpy();qn=q.numpy();vf=float(V)
        if vf<=0:raise ValueError('nonpositive volume')
        pb=bars(pn,pe);qb=bars(qn,qe);root=int(np.argmax((pn*pn).sum(1)))
        def fun(z):
            p,q,vol,c=state(self.points(z),t);loss=torch.zeros(())
            for peak,elder,ei,br,dd in qb:
                i,j=qe[ei];a=q[i];d=q[j]-a;w=a+torch.clamp(-(a*d).sum()/(d*d).sum(),0,1)*d
                loss=loss+1/torch.linalg.vector_norm(w)-1/torch.linalg.vector_norm(q[peak])
            loss=loss/vol**(1/3)
            pc=escape(p,pe);keep=[i for i in range(len(p)) if i!=root]
            R=torch.linalg.vector_norm(p,dim=1).max();ri=1/torch.linalg.vector_norm(q,dim=1).max()
            em=torch.linalg.vector_norm(p[pe[:,0]]-p[pe[:,1]],dim=1).min()/R
            cc=torch.cat((pc[keep]-s['p_floor'],torch.stack([em-s['edge_floor'],ri/R-s['inradius_floor'],vol/R**3-s['volume_floor']])))
            return torch.cat((loss.reshape(1),cc))
        xx=torch.tensor(x,requires_grad=grad);y=fun(xx).detach().numpy()
        J=torch.autograd.functional.jacobian(fun,xx,vectorize=True).detach().numpy() if grad else None
        with torch.no_grad():pc=escape(p,pe).numpy();qc=escape(q,qe).numpy()
        R=np.linalg.norm(pn,axis=1).max()
        dg=dict(V=len(v),E=len(pe),F=len(t),S=int((qc<0).sum()),U=int((pc<0).sum()),Pbars=len(pb),Qbars=len(qb),support_sum=float(y[0]),support_max=max([(d**-.5-b**-.5)/vf**(1/3) for _,_,_,b,d in qb],default=0.),TQ=sum(b-d for _,_,_,b,d in qb)*vf**(2/3),p_root=root,p_margin=float(np.delete(pc,root).min()),min_constraint=float(y[1:].min()),volume=vf,centroid=c.numpy().tolist(),edge_R=float(np.linalg.norm(pn[pe[:,0]]-pn[pe[:,1]],axis=1).min()/R),r_R=float(1/(np.linalg.norm(qn,axis=1).max()*R)),V_R3=float(vf/R**3))
        return y,J,dg

def qp(g,A,c,s,restore=False):
    eta=1. if restore else s['eta']
    return minimize(lambda d:(g@d+.5*eta*(d@d),g+eta*d),np.zeros(len(g)),jac=True,method='SLSQP',bounds=[(-s['trust'],s['trust'])]*len(g),constraints={'type':'ineq','fun':lambda d:c+A@d-s['buffer'],'jac':lambda d:A},options={'maxiter':s['qp_maxiter'],'ftol':s['qp_ftol']})

def restore(pr,x,s):
    w=x.copy();trials=0
    for k in range(s['restore_steps']+1):
        try:y,J,d=pr.model(w,s,True)
        except (ValueError,AssertionError,RuntimeError,QhullError,FloatingPointError):return None,trials
        if y[1:].min()>=-s['feasibility_tol'] and d['U']==1:return (w,y,J,d),trials
        if k==s['restore_steps']:break
        vio=np.minimum(y[1:]-s['buffer'],0);score=vio@vio
        ans=qp(np.zeros_like(w),J[1:],y[1:],s,True)
        if not ans.success and np.linalg.norm(ans.x)<1e-12:return None,trials
        found=False
        for j in range(s['restore_backtracks']):
            candidate=w+2.**-j*ans.x;trials+=1
            try:z,_,dd=pr.model(candidate,s,False)
            except (ValueError,AssertionError,RuntimeError,QhullError,FloatingPointError):continue
            vv=np.minimum(z[1:]-s['buffer'],0)
            if vv@vv<score*(1-s['armijo']*2.**-j):w=candidate;found=True;break
        if not found:break
    return None,trials

def run(mode,steps,output,input_file,pfloor=1e-5):
    data=json.loads(Path(input_file).read_text())
    if 'grid' in data:seed=np.array(data['points'],float)/data['grid']
    else:seed=np.array([float.fromhex(h) for h in data['final_points_hex']]).reshape(-1,3)
    pr=Problem(seed,mode);x=seed.ravel() if mode=='free' else np.zeros(5)
    s=dict(p_floor=pfloor,edge_floor=.03,inradius_floor=.06,volume_floor=.1,trust=.06 if mode=='free' else .1,eta=2.,buffer=1e-9,feasibility_tol=1e-11,restore_steps=15,restore_backtracks=10,outer_backtracks=20,armijo=1e-4,min_decrease=1e-12,qp_maxiter=250,qp_ftol=1e-14)
    y,J,d=pr.model(x,s);initial=d;hist=[];reason='requested steps completed';t0=time.time()
    print('START',mode,json.dumps(d),flush=True)
    for k in range(steps):
        ans=qp(J[0]/max(1.,np.linalg.norm(J[0])),J[1:],y[1:],s)
        if not ans.success:reason='QP failed: '+ans.message;break
        ok=False;nrall=0
        for j in range(s['outer_backtracks']):
            rr,nr=restore(pr,x+2.**-j*ans.x,s);nrall+=nr
            if rr is None:continue
            z,yy,JJ,dd=rr
            if yy[0]<y[0]-max(s['min_decrease'],s['armijo']*max(0.,-J[0]@(z-x))):
                hist.append(dict(iteration=k,backtrack=j,restore_trials=nrall,diagnosis=dd,parameters_hex=[float(a).hex() for a in z]));x,y,J,d=z,yy,JJ,dd;ok=True;break
        if not ok:reason='no accepted finite restored step';break
        with torch.no_grad():points=pr.points(torch.tensor(x)).numpy()
        out=dict(mode=mode,settings=s,initial_seed_hex=[float(a).hex() for a in seed.ravel()],initial=initial,final_parameters_hex=[float(a).hex() for a in x],final_points_hex=[float(a).hex() for a in points.ravel()],diagnosis=d,history=hist,reason='checkpoint',versions={'python':platform.python_version(),'numpy':np.__version__,'scipy':scipy.__version__,'torch':torch.__version__})
        Path(output).write_text(json.dumps(out,sort_keys=True,separators=(',',':'))+'\n')
        print('STEP',k,json.dumps(d),'bt',j,'restore',nrall,flush=True)
        if d['S']==1 and d['U']==1:reason='numerical S1U1; exact verification required';break
    with torch.no_grad():points=pr.points(torch.tensor(x)).numpy()
    out=dict(mode=mode,settings=s,initial_seed_hex=[float(a).hex() for a in seed.ravel()],initial=initial,final_parameters_hex=[float(a).hex() for a in x],final_points_hex=[float(a).hex() for a in points.ravel()],diagnosis=d,history=hist,reason=reason,versions={'python':platform.python_version(),'numpy':np.__version__,'scipy':scipy.__version__,'torch':torch.__version__})
    Path(output).write_text(json.dumps(out,sort_keys=True,separators=(',',':'))+'\n')
    print('SUPPORT_GAP_SEARCH_END',len(hist),reason,'elapsed',time.time()-t0,flush=True)
if __name__=='__main__':run(sys.argv[1],int(sys.argv[2]),sys.argv[3],sys.argv[4],float(sys.argv[5]) if len(sys.argv)>5 else 1e-5)
