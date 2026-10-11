"""Polar Thales chart plus actual uniform-mass projection.

The reference-S1 chart is the polar counterpart of peer3's published primal
chart. Its derivative and bar functional are adapted from the complete pinned
sources in sources/dual-thales-peer-provenance.json. Physical halfspace mass,
SVD-conditioned constrained descent and nonlinear mass projection are agent1.
No reference-root or small residual is accepted as an own-centroid Figure.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import numpy as np,json,pathlib,time,argparse
from scipy.special import expit,logit
from scipy.linalg import svd
from scipy.optimize import linprog
from geometry import halfspace_mesh,census,arrows

def bars(A,edges,eta=.01):
    aa=(A*A).sum(1);i,j=edges.T;e=A[j]-A[i];ee=(e*e).sum(1);t=np.clip(-(A[i]*e).sum(1)/np.maximum(ee,1e-300),0,1);feet=A[i]+t[:,None]*e;death=(feet*feet).sum(1);parent=np.arange(len(A));G=np.zeros_like(A);loss=0.;vals=[]
    def root(k):
        while k!=parent[k]:parent[k]=parent[parent[k]];k=parent[k]
        return k
    for k in np.argsort(-death):
        u,v=root(int(i[k])),root(int(j[k]))
        if u==v:continue
        if (aa[u],u)>(aa[v],v):u,v=v,u
        parent[u]=v;dep=aa[u]-death[k]
        if dep<-1e-12*aa.max():raise ValueError('persistence edge above endpoint')
        if dep<=0:continue
        birth=aa[u];coef=1/(eta*birth+dep);loss+=np.log1p(dep/(eta*birth));G[u]+=coef*(1-dep/birth)*2*A[u];G[i[k]]-=coef*2*(1-t[k])*feet[k];G[j[k]]-=coef*2*t[k]*feet[k];vals.append(float(dep/birth))
    return loss,G,sorted(vals,reverse=True)

class Chart:
    def __init__(self,Q):
        self.base=Q.copy();self.n=len(Q);aa=(Q*Q).sum(1);self.root=int(aa.argmax());raw=Q@Q.T-aa[:,None];np.fill_diagonal(raw,-np.inf);self.parent=raw.argmax(1);self.order=[int(i) for i in np.argsort(-aa) if i!=self.root];self.d=3*len(self.order);self.index={i:3*k for k,i in enumerate(self.order)};self.u0=Q/np.sqrt(aa)[:,None];self.B=np.zeros((self.n,3,2));self.z0=np.zeros(self.d)
        assert all(raw[i,self.parent[i]]>0 for i in self.order)
        for i in self.order:
            u=self.u0[i];v=np.eye(3)[np.argmin(abs(u))];v-=u*(u@v);v/=np.linalg.norm(v);self.B[i]=np.c_[v,np.cross(u,v)];rho=aa[i]/(Q[i]@Q[self.parent[i]])
            if not 0<rho<1:raise ValueError('positive Thales margin unresolved')
            self.z0[self.index[i]+2]=np.log(rho)
        rng=np.random.default_rng(48574);best=None;score=-np.inf
        for _ in range(6000):
            ids=rng.choice(self.n,4,replace=False)
            try:w=np.linalg.solve(np.vstack([Q[ids].T,np.ones(4)]),[0.,0.,0.,1.])
            except np.linalg.LinAlgError:continue
            if w.min()>score:best=ids;score=w.min()
        if not score>.005:raise ValueError('interior carrier unresolved')
        self.tetra=best;self.det0=np.linalg.det(Q[best[1:]]-Q[best[0]])
    def physical(self,z):
        if np.max(z[2::3])>=-1e-13 or np.min(z[2::3])<-30:raise ValueError('outside explicit strict radial chart bounds')
        Q=np.zeros_like(self.base);D=np.zeros((self.n,3,self.d));Q[self.root]=self.base[self.root]
        for i in self.order:
            k=self.index[i];p=self.parent[i];u=self.u0[i]+self.B[i]@z[k:k+2];uu=u@u;rho=np.exp(z[k+2]);s=u@Q[p]/uu;Q[i]=rho*s*u;D[i]=(rho*np.outer(u,u)/uu)@D[p];Ju=rho*(s*np.eye(3)+np.outer(u,Q[p])/uu-2*s*np.outer(u,u)/uu);D[i,:,k:k+2]+=Ju@self.B[i];D[i,:,k+2]+=Q[i]
        return Q,D
    def interior(self,Q,D):
        A=np.vstack([Q[self.tetra].T,np.ones(4)]);w=np.linalg.solve(A,[0.,0.,0.,1.]);Dw=np.linalg.solve(A,np.vstack([-np.einsum('i,icp->cp',w,D[self.tetra]),np.zeros((1,self.d))]));P=Q[self.tetra[1:]]-Q[self.tetra[0]];DP=D[self.tetra[1:]]-D[self.tetra[0]];det=np.linalg.det(P);Ddet=sum(np.cross(P[(k+1)%3],P[(k+2)%3])@DP[k] for k in range(3));return np.r_[w-.001,det/self.det0-.02],np.vstack([Dw,Ddet/self.det0])

def evaluate(chart,z,eta=.01):
    Q,DQ=chart.physical(z);ine,DI=chart.interior(Q,DQ)
    if min(ine)<0:raise ValueError('outside certified interior carrier chart')
    m=halfspace_mesh(Q);X=m['X'];tri=m['triples'];T=m['triangles'];DX=np.linalg.solve(Q[tri],-np.einsum('nc,nacp->nap',X,DQ[tri]));a,b,c=X[T[:,0]],X[T[:,1]],X[T[:,2]];det=np.einsum('ij,ij->i',a,np.cross(b,c));Ddet=np.einsum('ti,tip->tp',np.cross(b,c),DX[T[:,0]])+np.einsum('ti,tip->tp',np.cross(c,a),DX[T[:,1]])+np.einsum('ti,tip->tp',np.cross(a,b),DX[T[:,2]]);g=m['g'];Dg=(np.einsum('tp,ti->ip',Ddet,a+b+c-4*g)+np.einsum('t,tip->ip',det,DX[T].sum(1)))/(4*det.sum());Z=X-g;DZ=DX-Dg;loss,G,depth=bars(Z,m['edges'],eta);grad=np.einsum('ic,icp->p',G,DZ)
    return dict(Q=Q,DQ=DQ,X=X,DX=DX,g=g,Dg=Dg,loss=float(loss),gradient=grad,P=depth,ine=ine,DI=DI,mesh=m)

def conditioner(ev):
    sx=np.sqrt(np.mean((ev['X']-ev['g'])**2));sq=np.sqrt(np.mean(ev['Q']**2));metric=np.vstack([ev['DX'].reshape(-1,ev['DX'].shape[-1])/sx,ev['DQ'].reshape(-1,ev['DQ'].shape[-1])/sq]);_,dd,Vt=svd(metric,full_matrices=False,check_finite=False)
    if min(dd)<1e-14:raise ValueError('singular physical chart metric')
    return Vt.T/dd,sx

def project_mass(chart,z,eta=.01):
    for it in range(12):
        ev=evaluate(chart,z,eta)
        if np.linalg.norm(ev['g'])<1e-14:return z,ev
        W,sx=conditioner(ev);A=ev['Dg']@W/sx;dz=-W@A.T@np.linalg.solve(A@A.T,ev['g']/sx);accepted=False
        for j in range(14):
            trial=z+dz*2**-j
            try:e=evaluate(chart,trial,eta)
            except (ValueError,np.linalg.LinAlgError):continue
            if np.linalg.norm(e['g'])<np.linalg.norm(ev['g'])*(1-1e-4):z=trial;accepted=True;break
        if not accepted:raise ValueError('nonlinear own-volume centroid projection stalled')
    raise ValueError('centroid projection did not converge')

def run(input,out,steps=600,eta=.01):
    Q=np.load(input)['Q'];m=halfspace_mesh(Q);Q=Q/(1-Q@m['g'])[:,None];Q/=np.max(np.linalg.norm(Q,axis=1));out=pathlib.Path(out);out.mkdir(parents=True,exist_ok=True);history=[];trust=.03;t0=time.time();chart=Chart(Q);z=chart.z0.copy();best=np.inf
    for it in range(steps):
        ev=evaluate(chart,z,eta);st=census(ev['mesh']);row=dict(it=it,loss=ev['loss'],Pmax=max(ev['P'],default=0),bars=len(ev['P']),mass_norm=float(np.linalg.norm(ev['g'])),trust=trust,seconds=time.time()-t0,**st);history.append(row);(out/'history.json').write_text(json.dumps(history,indent=2));np.savez(out/'latest.npz',Q=ev['Q']);print('DUAL_THALES',json.dumps({k:row[k] for k in ['it','loss','Pmax','bars','mass_norm','S','U','E','trust','seconds']}),flush=True)
        if st['S']==st['U']==1 and st['min_primal_nonroot']>1e-12 and st['min_polar_nonroot']>1e-12 and st['E']<250:
            np.savez(out/'NOMINATION_OWN110.npz',Q=ev['Q']);print('POTENTIAL_OWN110_REQUIRES_EXACT',flush=True);return
        if ev['loss']<best and np.linalg.norm(ev['g'])<1e-10:
            best=ev['loss'];np.savez(out/'best.npz',Q=ev['Q']);(out/'best.json').write_text(json.dumps(row,indent=2))
        W,sx=conditioner(ev);d=len(z);gradient=ev['gradient']@W;mass=ev['Dg']@W/sx;A=ev['DI']@W;bound=trust/np.sqrt(d);radial=np.arange(2,d,3);ineq=np.vstack([-A,W[radial],-W[radial]]);rhs=np.r_[ev['ine']*.8,-1e-10-z[radial],z[radial]+25];lp=linprog(gradient,A_ub=ineq,b_ub=rhs,A_eq=mass,b_eq=-ev['g']/sx,bounds=[(-bound,bound)]*d,method='highs',options={'primal_feasibility_tolerance':1e-9,'dual_feasibility_tolerance':1e-9})
        if not lp.success:print('DUAL_LP_UNRESOLVED',lp.message,flush=True);trust*=.5;continue
        dz=W@lp.x;accepted=False
        for j in range(14):
            try:trial,ee=project_mass(chart,z+dz*2**-j,eta)
            except (ValueError,np.linalg.LinAlgError):continue
            if ee['loss']<ev['loss']-max(1e-12,abs(ev['loss'])*1e-9) and census(ee['mesh'])['S']==1:z=trial;accepted=True;break
        if accepted and j==0:trust=min(.25,trust*1.25)
        if not accepted:trust*=.4
        if trust<1e-8:print('DUAL_CHART_LOCAL_STALL',flush=True);break
        if accepted and it%20==19:
            Q=ee['Q'];chart=Chart(Q);z=chart.z0.copy();(out/f'rechart{it}.json').write_text(json.dumps(dict(root=chart.root,parent=chart.parent.tolist(),tetra=chart.tetra.tolist())))

def check(input,out):
    Q=np.load(input)['Q'];m=halfspace_mesh(Q);Q=Q/(1-Q@m['g'])[:,None];Q/=np.max(np.linalg.norm(Q,axis=1));c=Chart(Q);z=c.z0.copy();e=evaluate(c,z);direction=np.random.default_rng(473).normal(size=len(z));direction/=np.linalg.norm(direction);rows=[]
    for h in [1e-4,1e-5,1e-6,1e-7]:
        a=evaluate(c,z+h*direction);b=evaluate(c,z-h*direction);r=dict(h=h,objective_fd=(a['loss']-b['loss'])/(2*h),objective_ad=float(e['gradient']@direction),mass_error=float(np.max(abs((a['g']-b['g'])/(2*h)-e['Dg']@direction))),support_reconstruction=float(np.max(abs(e['Q']-Q))));rows.append(r);print(r,flush=True)
    pathlib.Path(out).write_text(json.dumps(rows,indent=2))

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--input',required=True);ap.add_argument('--out',required=True);ap.add_argument('--steps',type=int,default=600);ap.add_argument('--eta',type=float,default=.01);ap.add_argument('--check',action='store_true');a=ap.parse_args();check(a.input,a.out) if a.check else run(a.input,a.out,a.steps,a.eta)
