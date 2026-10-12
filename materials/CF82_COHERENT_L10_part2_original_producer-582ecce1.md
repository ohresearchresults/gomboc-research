# material-582ecce1bef3

AI research material

---

"""Graph-coherent actual-mass whole-support-gap flow, numerical discovery only.
Requires MAIN83.json (5053 bytes/SHA ff07c078...fd4b2) and geom.py.
Python3.13.5/NumPy2.3.5/SciPy1.17.0/Torch2.10.0+cpu; float64; one thread; no RNG.
Run: OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 python COUPLED_FLOW.py 10 100
"""
import hashlib,json,sys,time
from pathlib import Path
import numpy as np
import torch
from scipy.optimize import minimize
from geom import geometry,report,bars
torch.set_num_threads(1);torch.set_default_dtype(torch.float64)
ROOT=Path(__file__).resolve().parent
raw=(ROOT/'MAIN83.json').read_bytes()
assert len(raw)==5053 and hashlib.sha256(raw).hexdigest()=='ff07c078fdfbcb672dadb156dc59cc8cfe6078130645c34758f70c4f98afd4b2'
Y0=np.array(json.loads(raw)['points']);N=len(Y0)
SMOOTH=float(sys.argv[1]) if len(sys.argv)>1 else 10.
STEPS=int(sys.argv[2]) if len(sys.argv)>2 else 100
GUARD=1e-5;TRUST=.25;MAX_BACK=22;MAX_COR=10;MAX_COR_NORM=.15;EDGE_FLOOR=.003
OUT=ROOT/f'FLOW_L{SMOOTH:g}';OUT.mkdir(exist_ok=True)
counts=dict(geometries=0,charts=0,main_qp=0,restore_qp=0,line_trials=0,exceptions=0)
def geom(y):
    counts['geometries']+=1
    return geometry(y)
def tensor(z,ch):
    t=ch['T'];a,b,c=z[t[:,0]],z[t[:,1]],z[t[:,2]]
    vol=(a*torch.linalg.cross(b,c)).sum(1)/6;V=vol.sum()
    g=(vol[:,None]*(a+b+c)).sum(0)/(4*V)
    X=z[ch['ids']]-g
    normal=torch.linalg.cross(b-a,c-a)
    Q=normal/((a-g)*normal).sum(1)[:,None]
    diff=X[None,:,:]-X[:,None,:]
    length=torch.linalg.vector_norm(diff,dim=2)+torch.eye(len(X))
    w=(X[:,None,:]*diff).sum(2)/(torch.linalg.vector_norm(X,dim=1)[:,None]*length)-10*torch.eye(len(X))
    return X,Q,V,g,w
def setup(y,ch):
    assert len(ch['Q'])==len(ch['T'])
    z=torch.tensor(y,requires_grad=True);x,q,V,g,w=tensor(z,ch)
    root=int((x*x).sum(1).argmax())
    src=np.array([i for i in range(len(x)) if i!=root]);dst=w.detach().numpy().argmax(1)[src]
    def cons(v):return tensor(v,ch)[4][src,dst]
    val=cons(z).detach().numpy()
    J=torch.autograd.functional.jacobian(cons,z,vectorize=True).detach().numpy().reshape(len(val),-1)
    counts['charts']+=1
    return z,val,J
def objective(z,ch):
    x,q,V,g,w=tensor(z,ch);qb=bars(ch['Q'],ch['QE']);terms=[]
    for b in qb:
        i,j=b['edge'];d=q[j]-q[i]
        t=torch.clamp(-(q[i]*d).sum()/(d*d).sum(),0,1)
        h=((q[i]+t*d)**2).sum();r=(q[b['peak']]**2).sum()
        terms.append((h.rsqrt()-r.rsqrt())/2/V.pow(1/3))
    return torch.stack(terms).sum() if terms else z.sum()*0
def feasible(ch):
    x=ch['X'];r=np.linalg.norm(x,axis=1)
    d=x[None,:,:]-x[:,None,:];ll=np.linalg.norm(d,axis=2);np.fill_diagonal(ll,1.)
    w=np.einsum('ij,ikj->ik',x,d)/(r[:,None]*ll);np.fill_diagonal(w,-np.inf)
    score=w.max(1);pr=int((r*r).argmax())
    return (len(ch['E'])<=310 and np.min(np.delete(score,pr))>=GUARD
       and np.min(np.linalg.norm(x[ch['E'][:,1]]-x[ch['E'][:,0]],axis=1))/max(r)>=EDGE_FLOOR)
def restore(y):
    sizes=[]
    for it in range(MAX_COR+1):
        ch=geom(y)
        if feasible(ch):return y,ch,sizes
        if it==MAX_COR:break
        z,val,J=setup(y,ch);counts['restore_qp']+=1
        sol=minimize(lambda d:(.5*d@d,d),np.zeros(y.size),method='SLSQP',jac=True,
          constraints={'type':'ineq','fun':lambda d:val+J@d-(GUARD+1e-9),'jac':lambda d:J},
          options={'maxiter':180,'ftol':1e-18})
        step=sol.x.reshape(y.shape)
        if not sol.success or np.linalg.norm(step)>MAX_COR_NORM:return None,None,sizes
        y=y+step;sizes.append(float(np.linalg.norm(step)))
    return None,None,sizes
def metric(ch):
    lap=np.zeros((N,N))
    for i,j in ch['raw_edges']:
        lap[i,i]+=1;lap[j,j]+=1;lap[i,j]-=1;lap[j,i]-=1
    deg=np.sqrt(np.maximum(np.diag(lap),1));lap=lap/deg[:,None]/deg[None,:]
    return np.kron(np.eye(N)+SMOOTH*lap,np.eye(3))
Y=Y0.copy();records=[];start=time.monotonic();initial=report(Y)
for k in range(STEPS):
    ch=geom(Y);z,val,J=setup(Y,ch);loss=objective(z,ch);loss.backward();grad=z.grad.numpy().ravel();M=metric(ch)
    norm=float(np.sqrt(grad@np.linalg.solve(M,grad)))
    if norm<1e-14:break
    b=grad/norm;counts['main_qp']+=1
    sol=minimize(lambda d:(.5*d@M@d+b@d,M@d+b),np.zeros(Y.size),method='SLSQP',jac=True,
       constraints={'type':'ineq','fun':lambda d:val+J@d-(GUARD+1e-9),'jac':lambda d:J},
       options={'maxiter':350,'ftol':1e-12})
    if not sol.success:
        print('MAIN_QP_FAILURE',k,sol.message,flush=True);break
    d=sol.x.reshape(Y.shape);dn=np.linalg.norm(d)
    if dn>TRUST:d*=TRUST/dn
    old=report(Y);accepted=None;errors=[]
    for j in range(MAX_BACK):
        counts['line_trials']+=1;alpha=2.**(-j)
        try:
            Z,cz,cor=restore(Y+alpha*d)
            if Z is None:continue
            rr=report(Z)
            if rr['sum_eta']<old['sum_eta']-1e-13:
                accepted=(Z,rr,alpha,cor);break
        except (ValueError,AssertionError,RuntimeError) as exc:
            counts['exceptions']+=1;errors.append(type(exc).__name__+':'+str(exc))
    if accepted is None:
        print('FINITE_LINE_FAILURE',k,old['sum_eta'],flush=True);break
    Y,rr,alpha,cor=accepted
    rec=dict(iteration=k+1,alpha=alpha,main_direction_norm=float(dn),corrections=cor,report=rr,counts=counts.copy(),errors=errors)
    records.append(rec)
    (OUT/'ENDPOINT.json').write_text(json.dumps(dict(points=Y.tolist()),separators=(',',':')))
    (OUT/'LEDGER.json').write_text(json.dumps(dict(settings=dict(smooth=SMOOTH,steps=STEPS,guard=GUARD,trust=TRUST,max_back=MAX_BACK,maxcor=MAX_COR,maxcornorm=MAX_COR_NORM,edgefloor=EDGE_FLOOR),initial=initial,records=records),separators=(',',':')))
    if k%5==0 or rr['S']==1:print('FLOW',SMOOTH,k+1,rr['V'],rr['E'],rr['S'],rr['U'],rr['eta'],rr['sum_eta'],alpha,flush=True)
    if rr['S']==1 and rr['U']==1:print('NUMERICAL_ONE_ONE_REQUIRES_EXACT_AUDIT',flush=True);break
print('COUPLED_FLOW_STOP',SMOOTH,len(records),json.dumps(counts),time.monotonic()-start,flush=True)
