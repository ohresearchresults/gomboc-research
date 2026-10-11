"""Free C2 physical vertices, a uniform-centred moving apex, and dynamic hulls.

The old horizontal stable facet remains a literal quadrilateral. At most85
input vertices then give E<=248. The apex's actual mass derivative is eliminated
implicitly. Primal positive escape guards are hard constraints; the polar
escape capacities to the actual bottom facet are the objective. No fixed hull
triangulation or reference-centre claim substitutes for the complete census.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import pathlib,json,time
import numpy as np
import torch
from scipy.optimize import brentq,linprog
from scipy.linalg import svd
from scipy.spatial import QhullError
from scipy.sparse import csr_matrix,diags,hstack,vstack
from geometry import arrows
from free_primal_goal import mesh_points
from primal_chain_mass_goal import quick_mass
from bottleneck_capacity import capacities
from persistence_search import pairs

torch.set_num_threads(1);torch.set_default_dtype(torch.float64)

def canonical(X):
    if len(X)>85 or np.linalg.norm(X[0,:2])>1e-10:raise ValueError('Explicit C2 point budget or axial root invalid')
    pairs=[];seen={0}
    for i in range(1,len(X)):
        if i in seen:continue
        mate=int(np.argmin(np.linalg.norm(X-X[i]*np.array([-1,-1,1]),axis=1)))
        if mate==i or np.linalg.norm(X[mate]-X[i]*np.array([-1,-1,1]))>1e-10:raise ValueError('Literal half-turn pair absent')
        pairs.append((i,mate));seen.update([i,mate])
    bottom=float(X[:,2].min());base=[p for p in pairs if abs(X[p[0],2]-bottom)<1e-10]
    if len(base)!=2:raise ValueError('Expected one genuine four-vertex horizontal stable facet')
    ordered=[p for p in pairs if p not in base]+base;reps=X[[p[0] for p in ordered]].copy();reps[-1,2]=reps[-2,2]
    return reps.ravel()[:-1],ordered

def other_points(z):
    q=np.r_[z,z[-3]].reshape(-1,3);Y=np.empty((2*len(q),3));Y[::2]=q;Y[1::2]=q*np.array([-1,-1,1]);return Y

def mass_body(z):
    other=other_points(z);bottom=other[-1,2]
    if np.any(other[:-4,2]<=bottom+1e-9):raise ValueError('An extra point cuts the protected horizontal bottom facet')
    W=arrows(other);sinks=np.flatnonzero(W.max(1)<=1e-13);p=other[sinks]
    if not len(p) or np.any(p[:,2]<=0):raise ValueError('No strict axial-root sink bound')
    rmin=float(np.max(np.sum(p*p,axis=1)/p[:,2]))*(1+1e-12);X=np.r_[[[0.,0.,rmin]],other]
    def f(r):
        Y=X.copy();Y[0,2]=r;return float(quick_mass(Y)[1][2])
    if f(rmin)>=0:raise ValueError('Uniform centre lies beyond the allowed unique-U apex interval')
    hi=rmin*1.2
    for _ in range(18):
        if f(hi)>0:break
        hi*=1.5
    X[0,2]=brentq(f,rmin,hi,xtol=1e-13);return X

def evaluate(z,jacobian=False):
    X=mass_body(z);m=mesh_points(X);st=m['row']
    if not 17<=st['E']<=248 or st['U']!=1 or np.max(abs(m['g']))>2e-9:raise ValueError('Fresh same-body mass, unstable census, or true edge budget failed')
    P=X-m['g'];Q=m['R'];axis=np.flatnonzero((np.linalg.norm(Q[:,:2],axis=1)<1e-8)&(Q[:,2]<0))
    if len(axis)!=1:raise ValueError('Unique actual horizontal bottom facet absent')
    cap,ii,jj,sg=capacities(Q,[int(axis[0])]);wp=arrows(P);pi=np.arange(len(P));pj=wp.argmax(1);ps=np.ones(len(P));ps[0]=-1;pv=ps*wp[pi,pj]
    if pv.min()<=0:raise ValueError('Strict actual unique-U point witnesses failed')
    pp,h=pairs(Q,m['eq']);bars=1-h[pp[:,1]]/np.sum(Q[pp[:,0]]**2,axis=1);eps=2e-8
    row=dict(**st,score=float(np.maximum(eps-cap,0).sum()),Qmax=float(max(bars,default=0)),minimum_U_guard=float(pv.min()),minimum_S_capacity=float(cap.min()))
    result=dict(X=X,m=m,cap=cap,pv=pv,row=row)
    if not jacobian:return result
    ti=torch.tensor(m['triples']);tt=torch.tensor(m['tri']);ii=torch.tensor(ii);jj=torch.tensor(jj);sg=torch.tensor(sg);pj=torch.tensor(pj);ps=torch.tensor(ps)
    def mechanics(w):
        q=torch.cat([w[1:],w[-3:-2]]).reshape(-1,3);other=torch.stack([q,q*torch.tensor([-1.,-1.,1.])],dim=1).reshape(-1,3)
        x=torch.cat([torch.stack([w[0]*0,w[0]*0,w[0]])[None],other]);a=x[tt];six=(a[:,0]*torch.linalg.cross(a[:,1],a[:,2])).sum(1)
        g=(six[:,None]*a.sum(1)).sum(0)/(4*six.sum());p=x-g;q=torch.linalg.solve(x[ti],torch.ones((len(ti),3,1)))[:,:,0];r=q/(1-q@g)[:,None]
        src=r[ii];d=r[jj]-src;cv=sg*(src*d).sum(1)/(src.norm(dim=1)*d.norm(dim=1));dd=p[pj]-p;uv=ps*(p*dd).sum(1)/(p.norm(dim=1)*dd.norm(dim=1))
        return torch.cat([g[2:3],cv,uv,p.flatten(),r.flatten()])
    w=torch.tensor(np.r_[X[0,2],z]);val=mechanics(w).detach().numpy();J=torch.func.jacrev(mechanics)(w).detach().numpy();n=len(cap);k=len(pv)
    if abs(J[0,0])<1e-10:raise ValueError('Moving-apex actual mass derivative singular')
    D=J[1:,1:]-J[1:,0,None]*J[0,1:][None,:]/J[0,0]
    if np.max(abs(val[1:1+n]-cap))>1e-8 or np.max(abs(val[1+n:1+n+k]-pv))>1e-8:raise ValueError('Differentiated own mechanics disagree with the fresh physical hull')
    metric=D[n+k:]/np.r_[np.full(P.size,np.sqrt(np.mean(P*P))),np.full(Q.size,np.sqrt(np.mean(Q*Q)))][:,None]
    _,s,Vt=svd(metric,full_matrices=False,check_finite=False);keep=s>max(s[0]*1e-11,1e-11)
    result.update(Jcap=D[:n],Jpv=D[n:n+k],W=Vt[keep].T/s[keep]);return result

def run(source,out,steps=1400):
    out=pathlib.Path(out);out.mkdir(parents=True,exist_ok=False);data=pathlib.Path(source).read_bytes();(out/'source_body.npz').write_bytes(data)
    X=np.load(out/'source_body.npz')['X'];z,order=canonical(X);e=evaluate(z,True);np.savez(out/'entrance.npz',X=e['X'],z=z)
    (out/'definition.json').write_text(json.dumps(dict(source=str(pathlib.Path(source).resolve()),steps=steps,pair_reordering=order,
        scope='All paired point coordinates free, actual mass implicit apex, hard unique-U and dynamic full hull; only actual110 nominated'),indent=2))
    (out/'source.py').write_bytes(pathlib.Path(__file__).read_bytes());rng=np.random.default_rng(939083);d=rng.normal(size=len(z));d/=np.linalg.norm(d);eta=1e-7
    active=e['cap']<2e-8;prediction=float(-e['Jcap'][active].sum(0)@d)
    measured=(evaluate(z+eta*d)['row']['score']-evaluate(z-eta*d)['row']['score'])/(2*eta)
    check=dict(predicted=prediction,measured=measured,error=abs(prediction-measured));(out/'directional_check.json').write_text(json.dumps(check,indent=2));print('POINT_MASS_DERIVATIVE',json.dumps(check),flush=True)
    if abs(prediction-measured)>2e-4:raise ValueError('Independent implicit same-body derivative check failed')
    trust=.02;history=[];failed=[];start=time.time();eps=2e-8
    for it in range(steps):
        e=evaluate(z,True);row=dict(it=it,trust=trust,seconds=time.time()-start,**e['row']);history.append(row)
        np.savez(out/'latest.npz',X=e['X'],Q=e['m']['Q'],z=z);(out/'history.json').write_text(json.dumps(history,indent=2))
        if it%5==0:print('FREE_CYCLIC_POINT_GOAL',json.dumps(row),flush=True)
        if row['S']==row['U']==1:
            np.savez(out/'POTENTIAL_OWN110.npz',X=e['X'],Q=e['m']['Q'],z=z);(out/'POTENTIAL_OWN110.json').write_text(json.dumps(row,indent=2));return
        W=e['W'];A=e['Jcap']@W;B=e['Jpv']@W;n=W.shape[1];k=len(e['cap']);bound=trust/np.sqrt(n)
        ms=np.maximum(bound*np.abs(A).sum(1),1e-10);bs=np.maximum(bound*np.abs(B).sum(1),1e-10)
        mat=vstack([hstack([-csr_matrix(A/ms[:,None]),-diags(1/ms)]),hstack([-csr_matrix(B/bs[:,None]),csr_matrix((len(B),k))])],format='csr');rhs=np.r_[(e['cap']-eps)/ms,(e['pv']-eps)/bs]
        lp=linprog(np.r_[np.zeros(n),np.ones(k)],A_ub=mat,b_ub=rhs,bounds=[(-bound,bound)]*n+[(0,None)]*k,method='highs',options={'primal_feasibility_tolerance':1e-9,'dual_feasibility_tolerance':1e-9})
        accepted=False
        if lp.success:
            dz=W@lp.x[:n]
            for level in range(16):
                zz=z+dz*2**-level
                try:
                    ee=evaluate(zz)
                    if ee['row']['S']==ee['row']['U']==1:
                        np.savez(out/'POTENTIAL_OWN110.npz',X=ee['X'],Q=ee['m']['Q'],z=zz);(out/'POTENTIAL_OWN110.json').write_text(json.dumps(ee['row'],indent=2));return
                    if ee['pv'].min()<eps*.8:continue
                    predicted=row['score']-float(np.maximum(eps-(e['cap']+e['Jcap']@dz*2**-level),0).sum())
                    if ee['row']['score']<row['score']-max(1e-13,1e-4*max(predicted,0)):
                        z=zz;accepted=True;row.update(alpha=2**-level,predicted=predicted,actual_decrease=row['score']-ee['row']['score']);break
                except (ValueError,RuntimeError,AssertionError,QhullError,np.linalg.LinAlgError) as error:
                    if len(failed)<100:failed.append(dict(it=it,level=level,error=repr(error)))
        if accepted and level==0:trust=min(.15,trust*1.2)
        elif not accepted:trust*=.4
        if trust<1e-10:break
    (out/'failed_proposals.json').write_text(json.dumps(failed,indent=2));(out/'FINITE_END.json').write_text(json.dumps(dict(iterations=len(history),seconds=time.time()-start,
        scope='Finite actual-centroid dynamic point search ended without a qualifying body'),indent=2))

if __name__=='__main__':
    import sys
    run(sys.argv[1],sys.argv[2],int(sys.argv[3]) if len(sys.argv)>3 else 1400)
