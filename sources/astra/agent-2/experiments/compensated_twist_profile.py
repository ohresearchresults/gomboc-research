"""Height after Tz(a*z), Ty(b*y), Tz(a*z), b=2a/(1+a*a).

Each T is a smooth sphere diffeomorphism. The composition fixes +/-x, and
its derivative on either tangent plane is orthogonal: S(a)L(-b)S(a) is a
rotation. Thus the pulled-back height has exactly two critical points and
isotropic Hessians there. This does NOT by itself supply a homogeneous convex
body. The separate support-profile optimization checks numerical mass and
sampled curvature; final target still requires a rational polyhedral audit.
"""
import sys,json
import numpy as np
from scipy.special import roots_legendre
import jax
import jax.numpy as jnp
from twisted_support_profile import ROOT,DEGREES,run
jax.config.update('jax_enable_x64',True)

def height(u,a):
    b=2*a/(1+a*a)
    def tz(p):
        t=a*p[2];co=jnp.cos(t);si=jnp.sin(t);return jnp.array([p[0]*co-p[1]*si,p[0]*si+p[1]*co,p[2]])
    def ty(p):
        t=b*p[1];co=jnp.cos(t);si=jnp.sin(t);return jnp.array([p[0]*co+p[2]*si,p[1],-p[0]*si+p[2]*co])
    return tz(ty(tz(u)))[0]
gradient=jax.grad(height,argnums=0);hessian=jax.jacfwd(gradient,argnums=0)
all_derivatives=jax.jit(jax.vmap(lambda u,a:(height(u,a),gradient(u,a),hessian(u,a)),in_axes=(0,None)))

def tensors(a,nz=72,nt=64):
    zz,ww=roots_legendre(nz);tt=np.arange(nt)*2*np.pi/nt;z,theta=np.meshgrid(zz,tt,indexing='ij');z=z.ravel();theta=theta.ravel();weight=np.repeat(ww,nt)*(2*np.pi/nt);r=np.sqrt(1-z*z);x=r*np.cos(theta);y=r*np.sin(theta);u=np.c_[x,y,z];g,grad,H=map(np.asarray,all_derivatives(u,a))
    T=np.stack([np.c_[-np.sin(theta),np.cos(theta),np.zeros(len(z))],np.c_[-z*np.cos(theta),-z*np.sin(theta),r]],axis=2);dg=np.einsum('nci,nc->ni',T,grad);Hg=np.einsum('nci,ncd,ndj->nij',T,H,T)-np.sum(grad*u,axis=1)[:,None,None]*np.eye(2)
    S=np.stack([g**j for j in DEGREES],axis=1);D=np.stack([j*g**(j-1) for j in DEGREES],axis=1);D2=np.stack([j*(j-1)*g**(j-2) if j>1 else np.zeros(len(g)) for j in DEGREES],axis=1);R=D[:,:,None,None]*Hg[:,None]+D2[:,:,None,None]*np.einsum('ni,nj->nij',dg,dg)[:,None]+S[:,:,None,None]*np.eye(2);X=S[:,:,None]*u[:,None]+D[:,:,None]*np.einsum('nci,ni->nc',T,dg)[:,None]
    return dict(k=a,u=u,w=weight,S=S,R=R,X=X,g=g)

if __name__=='__main__':
    out=ROOT/sys.argv[1];out.mkdir(parents=True,exist_ok=False);checks=[]
    for a in [1.,1.5,2.,2.5,3.,3.5,4.]:
        poles=np.array([[1.,0,0],[-1.,0,0]]);g,G,H=map(np.asarray,all_derivatives(poles,a));spherical=H[:,1:,1:]-np.sum(G*poles,1)[:,None,None]*np.eye(2);error=float(np.max(abs(spherical-np.array([-np.eye(2),np.eye(2)]))));assert error<1e-10;d=tensors(a,40,64);moment=float(np.sum(d['w']*d['g']*d['u'][:,0]));checks.append(dict(a=a,b=2*a/(1+a*a),pole_spherical_hessian_error=error,linear_first_harmonic_x=moment))
    (out/'pole_and_moment_checks.json').write_text(json.dumps(checks,indent=2)+'\n');print('COMPENSATED_TWIST_CHECKS',checks,flush=True)
    run(out/'profiles',[1.5,1.75,2.,2.25,2.5,2.75,3.,3.25,3.5],tensors)
