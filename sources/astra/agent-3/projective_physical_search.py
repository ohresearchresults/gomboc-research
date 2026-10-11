"""Eight-dimensional physical projective/affine orbit with uniform mass.

For source coordinates x, the single embedding is A*x/(1+p*x).
The physical body is uniformly filled AFTER this transformation.  Its centroid
is integrated each time and its centered support covectors are reconstructed
by the same projective duality.  No reference-point census is substituted.
"""
import argparse,json,hashlib,time
from pathlib import Path
import numpy as np
from scipy.optimize import differential_evolution,minimize
from gmpy2 import mpq
from polar_centroid_orbits import mesh,mass
from persistence_birth import bars_loss
from support_geometry import escape

class Orbit:
    def __init__(self,source):
        self.source=Path(source);a=json.loads(self.source.read_text());self.a=a
        c=[mpq(v)for v in a['raw_centroid']];self.c=np.array(list(map(float,c)))
        X=np.array([[float(mpq(v)-c[j])for j,v in enumerate(row)]for row in a['raw_vertices']]);self.scale=np.max(np.linalg.norm(X,axis=1));self.X=X/self.scale
        H=[]
        for n,h in zip(a['normals'],a['offsets']):
            n=[mpq(v)for v in n];b=mpq(h)-sum(u*v for u,v in zip(n,c));H.append([float(v/b)*self.scale for v in n])
        self.H=np.array(H);self.mesh=mesh(self.X,a['faces']);self.T=self.mesh['T']
        self.R=np.eye(4);self.R[:3,:3]/=self.scale;self.R[:3,3]=-self.c/self.scale

    def physical(self,t):
        aa,bb,cx,dx,ex=t[:5];u=np.array(t[5:]);j=int(np.argmin(self.X@u));m=-self.X[j]@u
        assert m>=-1e-12
        p=.99*u/(1+m);Dp=.99*(np.eye(3)/(1+m)+np.outer(u,self.X[j])/(1+m)**2)
        A=np.array([[np.exp(aa),cx,dx],[0.,np.exp(bb),ex],[0.,0.,np.exp(-aa-bb)]]);DA=np.zeros((3,3,8));DA[0,0,0]=A[0,0];DA[1,1,1]=A[1,1];DA[2,2,:2]=-A[2,2];DA[0,1,2]=1;DA[0,2,3]=1;DA[1,2,4]=1
        den=1+self.X@p;assert min(den)>0
        Y=self.X/den[:,None];DY=np.zeros((len(Y),3,8));DY[:,:,5:]=-Y[:,:,None]*(self.X@Dp)[:,None,:]/den[:,None,None]
        Z0=Y@A.T;DZ0=np.einsum('ic,acp->iap',Y,DA)+np.einsum('icp,ac->iap',DY,A)
        a,b,c=Z0[self.T[:,0]],Z0[self.T[:,1]],Z0[self.T[:,2]];da,db,dc=DZ0[self.T[:,0]],DZ0[self.T[:,1]],DZ0[self.T[:,2]]
        v6=np.einsum('ic,ic->i',a,np.cross(b,c));V=v6.sum()/6;assert V>0
        g=np.sum(v6[:,None]*(a+b+c),axis=0)/(4*v6.sum())
        dv=np.einsum('ic,icp->ip',np.cross(b,c),da)+np.einsum('ic,icp->ip',np.cross(c,a),db)+np.einsum('ic,icp->ip',np.cross(a,b),dc)
        Dg=(np.einsum('ip,ic->cp',dv,a+b+c-4*g)+np.einsum('i,icp->cp',v6,da+db+dc))/(4*v6.sum())
        I=np.linalg.inv(A);Q=(self.H+p)@I;DQ=-np.einsum('ia,abp,bc->icp',Q,DA,I);DQ[:,:,5:]+=np.einsum('ak,ac->ck',Dp,I)[None,:,:]
        hh=1-Q@g;assert min(hh)>0
        Dh=-np.einsum('icp,c->ip',DQ,g)-Q@Dg
        H=Q/hh[:,None];DH=DQ/hh[:,None,None]-Q[:,:,None]*Dh[:,None,:]/hh[:,None,None]**2
        P=np.eye(4);P[:3,:3]=A;P[3,:3]=p;P=P@self.R
        return dict(X=Z0,Z=Z0-g,DZ=DZ0-Dg,H=H,DH=DH,P=P,centroid=g,volume=V,min_denominator=float(min(den)))

    def loss(self,t,eta):
        g=self.physical(t);lp,GP,P=bars_loss(g['Z'],self.mesh['edges'],eta);lq,GQ,Q=bars_loss(g['H'],self.mesh['dual_edges'],eta)
        G=np.einsum('ic,icp->p',GP,g['DZ'])+np.einsum('ic,icp->p',GQ,g['DH'])
        info=dict(loss=lp+lq,Pmax=max(P,default=0.),Qmax=max(Q,default=0.),S=int(np.sum(escape(g['H'])[0]<0)),U=int(np.sum(escape(g['Z'])[0]<0)),volume=g['volume'],centroid=g['centroid'].tolist(),min_denominator=g['min_denominator'])
        return lp+lq,G,info,g

def run(source,out,iterations,seed):
    out=Path(out);out.mkdir(parents=True,exist_ok=False);c=Orbit(source);calls=0;best=np.inf;start=time.time()
    (out/'source.json').write_text(json.dumps(dict(audit_path=str(Path(source).resolve()),audit_sha256=hashlib.sha256(Path(source).read_bytes()).hexdigest()),indent=2))
    t=np.array([.07,-.12,.05,.01,-.03,.1,-.04,.03]);d=np.random.default_rng(seed).normal(size=8);d/=np.linalg.norm(d);v,G,_,_=c.loss(t,.03);checks=[]
    for step in [1e-5,1e-6,1e-7]:
        p=c.physical(t+step*d);q=c.physical(t-step*d);z=c.physical(t)
        checks.append(dict(step=step,objective_fd=(c.loss(t+step*d,.03)[0]-c.loss(t-step*d,.03)[0])/(2*step),objective_analytic=float(G@d),mass_jacobian_error=float(np.max(abs((p['Z']-q['Z'])/(2*step)-np.einsum('icp,p->ic',z['DZ'],d)))),polar_jacobian_error=float(np.max(abs((p['H']-q['H'])/(2*step)-np.einsum('icp,p->ic',z['DH'],d))))))
    (out/'gradient_check.json').write_text(json.dumps(checks,indent=2));assert abs(checks[1]['objective_fd']-checks[1]['objective_analytic'])<1e-4 and checks[1]['polar_jacobian_error']<1e-5
    def fun(t,jac=False):
        nonlocal best,calls
        calls+=1;v,G,info,g=c.loss(t,.03);info.update(calls=calls,seconds=time.time()-start)
        if v<best:
            best=v;np.save(out/'best_parameters.npy',t);np.savez(out/'embedding.npz',P=g['P'],dual=0);np.save(out/'best_vertices.npy',g['Z']);(out/'best.json').write_text(json.dumps(info,indent=2))
        if info['S']==info['U']==1:
            dest=out/f'potential{calls}';dest.mkdir();np.savez(dest/'embedding.npz',P=g['P'],dual=0);(dest/'source.json').write_text((out/'source.json').read_text());(dest/'nomination.json').write_text(json.dumps(info,indent=2));print('PROJECTIVE_PHYSICAL_POTENTIAL_REQUIRES_EXACT',dest,info,flush=True)
        if calls%10000==0:print('PROJECTIVE_PHYSICAL_SEARCH',out,info,'best',best,flush=True)
        return (v,G)if jac else v
    fun(np.zeros(8));rng=np.random.default_rng(seed);pop=rng.normal(0,.05,(120,8));pop[0]=0;bounds=[(-1.5,1.5)]*2+[(-2.,2.)]*3+[(-12.,12.)]*3
    r=differential_evolution(fun,bounds,maxiter=iterations,init=pop,seed=seed,polish=False,tol=1e-10)
    rr=minimize(lambda t:fun(t,True),np.load(out/'best_parameters.npy'),method='L-BFGS-B',jac=True,bounds=bounds,options=dict(maxiter=5000,maxls=50,gtol=1e-10,ftol=1e-15))
    (out/'termination.json').write_text(json.dumps(dict(global_message=r.message,local_message=rr.message),indent=2));print('PROJECTIVE_PHYSICAL_DONE',out,json.loads((out/'best.json').read_text()),flush=True)

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('source');p.add_argument('out');p.add_argument('--iterations',type=int,default=900);p.add_argument('--seed',type=int,default=81501);a=p.parse_args();run(a.source,a.out,a.iterations,a.seed)
