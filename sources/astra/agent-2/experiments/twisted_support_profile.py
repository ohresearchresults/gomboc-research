"""Numerical smooth-support guides for a new symmetric polyhedral seed family.

s(n)=1+f(g(n)), g=x cos(kz)-y sin(kz), with odd polynomial f and f'>0.
The curvature matrix Hess_S(s)+s I is affine in the profile coefficients.
Boundary point x=s n+grad_S(s), volume=(1/3) integral s detR, and first
moment=(1/4) integral x s detR are integrated by sphere quadrature. These
guides are not goal bodies or exact continuous certificates.
"""
import sys,json,time
from pathlib import Path
import numpy as np
from scipy.special import roots_legendre
from scipy.optimize import minimize,LinearConstraint
import jax
import jax.numpy as jnp
from support_persistence import ROOT
jax.config.update('jax_enable_x64',True)
DEGREES=np.array([1,3,5,7,9])

def tensors(k,nz=72,nt=64):
    zz,ww=roots_legendre(nz);tt=np.arange(nt)*2*np.pi/nt;z,theta=np.meshgrid(zz,tt,indexing='ij');z=z.ravel();theta=theta.ravel();weight=np.repeat(ww,nt)*(2*np.pi/nt);r=np.sqrt(1-z*z);x=r*np.cos(theta);y=r*np.sin(theta);u=np.c_[x,y,z];ct=np.cos(k*z);st=np.sin(k*z);g=x*ct-y*st;grad=np.c_[ct,-st,-k*(x*st+y*ct)];H=np.zeros((len(z),3,3));H[:,0,2]=H[:,2,0]=-k*st;H[:,1,2]=H[:,2,1]=-k*ct;H[:,2,2]=-k*k*g
    T=np.stack([np.c_[-np.sin(theta),np.cos(theta),np.zeros(len(z))],np.c_[-z*np.cos(theta),-z*np.sin(theta),r]],axis=2);dg=np.einsum('nci,nc->ni',T,grad);Hg=np.einsum('nci,ncd,ndj->nij',T,H,T)-np.sum(grad*u,axis=1)[:,None,None]*np.eye(2)
    S=np.stack([g**j for j in DEGREES],axis=1);D=np.stack([j*g**(j-1) for j in DEGREES],axis=1);D2=np.stack([j*(j-1)*g**(j-2) if j>1 else np.zeros(len(g)) for j in DEGREES],axis=1)
    R=D[:,:,None,None]*Hg[:,None]+D2[:,:,None,None]*np.einsum('ni,nj->nij',dg,dg)[:,None]+S[:,:,None,None]*np.eye(2);X=S[:,:,None]*u[:,None]+D[:,:,None]*np.einsum('nci,ni->nc',T,dg)[:,None]
    return dict(k=k,u=u,w=weight,S=S,R=R,X=X)

@jax.jit
def moment(a,u,w,S,R,X):
    h=1+S@a;rr=jnp.eye(2)+jnp.einsum('nqij,q->nij',R,a);det=rr[:,0,0]*rr[:,1,1]-rr[:,0,1]*rr[:,1,0];points=u+jnp.einsum('nqc,q->nc',X,a);volume=jnp.sum(w*h*det)/3;M=jnp.sum((w*h*det)[:,None]*points,axis=0)/4
    return M[0]/jnp.sum(w)
momentgrad=jax.jit(jax.value_and_grad(moment))

def values(a,data):
    h=1+data['S']@a;R=np.eye(2)+np.einsum('nqij,q->nij',data['R'],a);det=np.linalg.det(R);X=data['u']+np.einsum('nqc,q->nc',data['X'],a);volume=np.sum(data['w']*h*det)/3;M=np.sum((data['w']*h*det)[:,None]*X,axis=0)/4;ev=np.linalg.eigvalsh(R);t=np.linspace(-1,1,2001);slope=np.stack([j*t**(j-1) for j in DEGREES],1)@a
    return dict(amplitude=float(np.sum(a)),extreme_radius_ratio=float((1+np.sum(a))/(1-np.sum(a))),minimum_support=float(h.min()),minimum_curvature_eigenvalue=float(ev.min()),minimum_profile_derivative=float(slope.min()),volume=float(volume),centroid=(M/volume).tolist())

def run(out,parameter_values=None,tensor_factory=tensors):
    out=Path(out);out.mkdir(parents=True,exist_ok=False);rows=[];start=time.time();floor=.015;tt=np.linspace(-1,1,301);slopes=np.stack([j*tt**(j-1) for j in DEGREES],1)
    if parameter_values is None:parameter_values=[3.9,4.,4.1,4.2,4.3,4.4,4.493409,4.6]
    for k in parameter_values:
        data=tensor_factory(k);angles=np.arange(10)*np.pi/10;v=np.c_[np.cos(angles),np.sin(angles)];curves=np.einsum('ai,nqij,aj->naq',v,data['R'],v).reshape(-1,len(DEGREES));C=np.r_[curves,slopes,-np.ones((1,len(DEGREES)))];lower=np.r_[np.full(len(curves),floor-1),np.full(len(slopes),1e-5),-.8];a=np.array([.005,0,0,0,0]);args=[data[t] for t in ['u','w','S','R','X']]
        def eq(a):return float(moment(a,*args))
        def eqjac(a):return np.asarray(momentgrad(a,*args)[1])
        for outer in range(3):
            result=minimize(lambda a:(-a.sum(),-np.ones(len(a))),a,jac=True,method='SLSQP',bounds=[(-2,2)]*len(a),constraints=[LinearConstraint(C,lower,np.inf),dict(type='eq',fun=eq,jac=eqjac)],options=dict(maxiter=180,ftol=1e-12));a=result.x
            fine=tensor_factory(k,120,96);mats=np.eye(2)+np.einsum('nqij,q->nij',fine['R'],a);ev,vec=np.linalg.eigh(mats);bad=np.flatnonzero(ev[:,0]<floor*.95)
            if not len(bad):break
            direction=vec[bad,:,0];extra=np.einsum('ni,nqij,nj->nq',direction,fine['R'][bad],direction);C=np.r_[C,extra];lower=np.r_[lower,np.full(len(extra),floor-1)]
        check=values(a,fine);row=dict(k=k,degrees=DEGREES.tolist(),coefficients=a.tolist(),success=bool(result.success),message=str(result.message),iterations=int(result.nit),mass_equation=eq(a),linear_violation=float(np.min(C@a-lower)),curvature_floor=floor,**check,seconds=time.time()-start,scope='numerical support guide, all claims limited to quadrature and sampled curvature checks')
        rows.append(row);(out/f'profile_{k:.6f}.json').write_text(json.dumps(row,indent=2)+'\n');(out/'profiles.json').write_text(json.dumps(rows,indent=2)+'\n');print('TWISTED_PROFILE',row,flush=True)
    (out/'FINITE_PROFILE_SEARCH_END.json').write_text(json.dumps(dict(profiles=len(rows),goal_complete=False),indent=2)+'\n')

if __name__=='__main__':run(ROOT/sys.argv[1])
