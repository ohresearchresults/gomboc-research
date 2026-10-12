"""Transport true uniform mass with continuous reference-root capacities.

The reference centre is fixed at0; one reference-U vertex is fixed at(0,0,1),
which prevents shrinking the body to fake a small centroid residual. A fixed
positive volume floor prevents lower-dimensional degeneration in this search.
All accepted steps rebuild the physical hull and retain both reference trees.
Only an independent own-centroid strict census can trigger an exact nomination.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import numpy as np,torch,pathlib,json,time,argparse
from scipy.spatial import ConvexHull
from scipy.optimize import linprog,minimize,LinearConstraint,Bounds
from scipy.sparse import csr_matrix,eye,hstack,vstack
from mass_homotopy import mesh
from bottleneck_capacity import capacities
from geometry import arrows
torch.set_num_threads(1);torch.set_default_dtype(torch.float64)

def state(X,root=0):
    m=mesh(X);h=ConvexHull(X)
    if np.max(h.equations[:,3])>=-1e-9:raise ValueError('reference origin is not strictly interior')
    if root not in m['active']:raise ValueError('fixed reference apex ceased to be a vertex')
    P=X[m['active']];Q=np.linalg.solve(X[m['polar_triangles']],np.ones((m['F'],3,1)))[:,:,0];parents=[];signs=[];vals=[];rr=[int(np.flatnonzero(m['active']==root)[0]),int(np.argmax((Q*Q).sum(1)))];classes=[]
    for A,r in zip([P,Q],rr):
        cap,ii,jj,sg=capacities(A,[r]);parents.append((ii,jj));signs.append(sg);W=arrows(A);vals.append(cap);classes.append(int(np.sum(W.max(1)<0)))
    return m,np.concatenate(vals),parents,signs,dict(referenceS=classes[1],referenceU=classes[0],V=m['V'],E=m['E'],F=m['F'],volume=float(m['volume']),centroid=m['g'].tolist(),mass_norm=float(np.linalg.norm(m['g'])))

def jacobian(X,m,parents,signs,flat):
    tt=torch.tensor(m['T']);tp=torch.tensor(m['polar_triangles']);ti=torch.tensor(m['active']);pp=[(torch.tensor(i),torch.tensor(j)) for i,j in parents];ss=list(map(torch.tensor,signs))
    def calc(z):
        x=z.reshape(X.shape);a=x[tt];vol=(a[:,0]*torch.linalg.cross(a[:,1],a[:,2])).sum(1)/6;volume=vol.sum();g=(vol[:,None]*a.sum(1)).sum(0)/(4*volume);P=x[ti];Q=torch.linalg.solve(x[tp],torch.ones((len(tp),3,1)))[:,:,0];v=[]
        for A,(ii,jj),s in zip([P,Q],pp,ss):
            anchor=A[ii];delta=A[jj]-anchor;v.append(s*(anchor*delta).sum(1)/(torch.linalg.vector_norm(anchor,dim=1)*torch.linalg.vector_norm(delta,dim=1)).clamp(min=1e-18))
        return torch.cat([*v,g,volume.reshape(1)])
    return torch.func.jacrev(calc)(torch.tensor(X.ravel())).detach().numpy()[:,flat]

def own(X):
    m=mesh(X);P=X[m['active']]-m['g'];Q=np.linalg.solve(X[m['polar_triangles']]-m['g'],np.ones((m['F'],3,1)))[:,:,0];vp=arrows(P).max(1);vq=arrows(Q).max(1);return dict(S=int(np.sum(vq<0)),U=int(np.sum(vp<0)),minP=float(np.sort(vp)[1]),minQ=float(np.sort(vq)[1]),V=m['V'],E=m['E'],F=m['F'])

def reference_repair(X,root,flat,volume_floor,eps=2e-7,steps=45):
    trust=.008;d=len(flat)
    for it in range(steps):
        m,v,pa,sg,st=state(X,root);merit=float(np.maximum(eps-v,0).sum())
        if min(v)>eps*.8 and st['referenceS']==st['referenceU']==1:return X,True
        J=jacobian(X,m,pa,sg,flat)[:len(v)];n=len(v);I=eye(d);O=csr_matrix((d,n));A=vstack([hstack([-csr_matrix(J),-eye(n),csr_matrix((n,d))]),hstack([I,O,-I]),hstack([-I,O,-I])],format='csr');b=np.r_[v-eps,np.zeros(2*d)];lp=linprog(np.r_[np.zeros(d),np.ones(n),np.full(d,1e-7)],A_ub=A,b_ub=b,bounds=[(-trust,trust)]*d+[(0,None)]*(n+d),method='highs',options={'primal_feasibility_tolerance':1e-9,'dual_feasibility_tolerance':1e-9})
        if not lp.success:trust*=.5;continue
        dz=np.zeros(X.size);dz[flat]=lp.x[:d];dz=dz.reshape(X.shape);accepted=False
        for level in range(12):
            Y=X+dz*2**-level
            try:mm,vv,_,_,ss=state(Y,root)
            except Exception:continue
            if mm['volume']>volume_floor and np.maximum(eps-vv,0).sum()<merit*(1-1e-5):X=Y;accepted=True;break
        if accepted and level==0:trust=min(.025,trust*1.2)
        if not accepted:trust*=.4
        if trust<1e-9:break
    return X,False

def run(input,out,steps=400,eps=2e-7):
    dat=np.load(input);X=dat['X'];m=mesh(X)
    if 'reference' in dat:c=dat['reference']
    elif 'lam' in dat:c=float(dat['lam'])*m['g']+(1-float(dat['lam']))*(dat['w']@X)
    else:c=np.zeros(3)
    X=X-c;root=int(np.argmax((X*X).sum(1)));r=np.linalg.norm(X[root]);axis=X[root]/r;a=np.eye(3)[np.argmin(abs(axis))];a-=axis*(a@axis);a/=np.linalg.norm(a);R=np.array([a,np.cross(axis,a),axis]);X=X@R.T/r;X[root]=[0,0,1];m=mesh(X);floor=m['volume']*.02;out=pathlib.Path(out);out.mkdir(parents=True,exist_ok=True);np.savez(out/'initial.npz',X=X,reference=np.zeros(3));(out/'frame.json').write_text(json.dumps(dict(source=str(pathlib.Path(input).resolve()),old_reference=c.tolist(),rotation=R.tolist(),scale=r,fixed_root=root,volume_floor=float(floor)),indent=2));mask=np.ones(X.size,bool);mask[3*root:3*root+3]=False;flat=np.flatnonzero(mask);d=len(flat);trust=.012;history=[];t0=time.time()
    X,ok=reference_repair(X,root,flat,floor,eps=eps,steps=80)
    if not ok:raise ValueError('initial reference chamber correction failed')
    for it in range(steps):
        m,v,pa,sg,st=state(X,root);oo=own(X);row=dict(it=it,minimum_reference_guard=float(min(v)),trust=trust,seconds=time.time()-t0,own=oo,**st);history.append(row);(out/'history.json').write_text(json.dumps(history,indent=2));np.savez(out/'latest.npz',X=X,reference=np.zeros(3));print('MASS_TRANSPORT',json.dumps(row),flush=True)
        if oo['S']==oo['U']==1 and oo['minP']>1e-10 and oo['minQ']>1e-10 and 17<=oo['E']<250:
            np.savez(out/'NOMINATION_OWN110.npz',X=X,reference=np.zeros(3));print('POTENTIAL_OWN110_REQUIRES_EXACT',flush=True);return
        JJ=jacobian(X,m,pa,sg,flat);J=JJ[:len(v)];M=JJ[-4:-1];VJ=JJ[-1];g=m['g'];A=np.vstack([np.c_[-J,np.zeros(len(v))],np.r_[-VJ,0][None]]);b=np.r_[v-eps,m['volume']-floor];eq=np.c_[M,g];lp=linprog(np.r_[np.zeros(d),-1],A_ub=A,b_ub=b,A_eq=eq,b_eq=np.zeros(3),bounds=[(-trust,trust)]*d+[(0,1)],method='highs',options={'primal_feasibility_tolerance':1e-9,'dual_feasibility_tolerance':1e-9})
        if not lp.success or lp.x[-1]<1e-8:trust*=.5;print('MASS_TRANSPORT_NO_LINEAR_PROGRESS',lp.message,flush=True);continue
        target=.8*lp.x[-1];qp=minimize(lambda x:(.5*x@x,x),lp.x[:-1]*.8,jac=True,method='SLSQP',bounds=Bounds(-trust,trust),constraints=[LinearConstraint(A[:,:-1],-np.inf,b),LinearConstraint(M,-target*g,-target*g)],options={'maxiter':120,'ftol':1e-13})
        if np.max(A[:,:-1]@qp.x-b)>1e-8 or np.max(abs(M@qp.x+target*g))>1e-8:trust*=.5;print('MASS_TRANSPORT_QP_REJECTED',flush=True);continue
        delta=np.zeros(X.size);delta[flat]=qp.x;delta=delta.reshape(X.shape);accepted=False
        for level in range(8):
            Y=X+delta*2**-level
            try:Y,ok=reference_repair(Y,root,flat,floor,eps=eps,steps=45);mm,vv,_,_,ss=state(Y,root)
            except Exception:continue
            if ok and np.linalg.norm(mm['g'])<np.linalg.norm(g)*(1-1e-7) and mm['volume']>floor:X=Y;accepted=True;row['fraction']=target*2**-level;break
        if accepted and level==0:trust=min(.045,trust*1.2)
        if not accepted:trust*=.4
        if trust<1e-8:print('MASS_TRANSPORT_LOCAL_STALL',flush=True);break

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--input',required=True);ap.add_argument('--out',required=True);ap.add_argument('--steps',type=int,default=400);ap.add_argument('--epsilon',type=float,default=2e-7);a=ap.parse_args();run(a.input,a.out,a.steps,a.epsilon)
