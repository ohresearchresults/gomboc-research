"""Direct physical flow on a negative self-polar, uniform-centred contact body.

The unknowns are the physical vertices. Every paired contact x_i.x_j=-1
and the actual uniform centroid are retracted after a predictor. There is
only one radial escape landscape, since the literal polar is -X. Complete
actual primal/dual censuses are independently rebuilt at each admitted body.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import pathlib,json,time
import numpy as np
from scipy.linalg import svd
from scipy.optimize import linprog
from scipy.sparse import csr_matrix,eye,hstack,vstack,diags
from selfdual_pair_goal import check,center
from bottleneck_capacity import capacities
from persistence_search import pairs

class Body:
    def __init__(self,X):
        self.initial=np.asarray(X).copy();m=check(X);self.tri=m['tri'];self.edges=m['ep'];self.faces=m['faces'];self.N=len(X)
        gram=1+X@X.T;self.contacts=np.array([(i,j) for i in range(self.N) for j in range(i+1,self.N) if abs(gram[i,j])<1e-8],int)
        self.noncontacts=np.array([(i,j) for i in range(self.N) for j in range(i+1,self.N) if abs(gram[i,j])>=1e-8],int)
        if len(self.contacts)!=m['row']['E']:raise ValueError('Symmetric contact constraints do not match the self-polar true edge count')
        self.E=m['row']['E']

    def constraints(self,X,jacobian=True):
        a=X[self.tri];six=np.einsum('ij,ij->i',a[:,0],np.cross(a[:,1],a[:,2]));S=six.sum()
        if S<=0 or six.min()<=0:raise ValueError('Physical boundary orientation failed')
        g=(six[:,None]*a.sum(1)).sum(0)/(4*S);i,j=self.contacts.T;con=1+np.einsum('ij,ij->i',X[i],X[j]);values=np.r_[con,g]
        ni,nj=self.noncontacts.T;gaps=1+np.einsum('ij,ij->i',X[ni],X[nj])
        if gaps.min()<=0:raise ValueError('Nonincident self-polar support inequality violated')
        if not jacobian:return values,gaps,g,S/6
        J=np.zeros((len(i)+3,self.N,3));J[np.arange(len(i)),i]=X[j];J[np.arange(len(i)),j]=X[i]
        DG=np.zeros((self.N,3,3));shift=a.sum(1)-4*g
        for k in range(3):
            ds=np.cross(a[:,(k+1)%3],a[:,(k+2)%3])
            terms=np.einsum('ti,tj->tij',shift,ds)+six[:,None,None]*np.eye(3)[None]
            np.add.at(DG,self.tri[:,k],terms)
        J[-3:]=DG.transpose(1,0,2)/(4*S)
        G=np.zeros((len(ni),self.N,3));G[np.arange(len(ni)),ni]=X[nj];G[np.arange(len(ni)),nj]=X[ni]
        return values,J.reshape(len(values),-1),gaps,G.reshape(len(gaps),-1),g,S/6

    def retract(self,X):
        Y=X.copy()
        for it in range(18):
            v,J,gaps,G,g,V=self.constraints(Y);norm=float(np.max(abs(v)))
            if norm<2e-12:return Y
            scale=np.maximum(np.linalg.norm(J,axis=1),1e-12);A=J/scale[:,None];b=v/scale
            U,s,Vt=svd(A,full_matrices=False,check_finite=False)
            if s[-1]<1e-10:raise ValueError('Self-polar mass constraint Jacobian lost full row rank')
            d=-(Vt.T@((U.T@b)/s)).reshape(Y.shape);accepted=False
            for level in range(14):
                Z=Y+d*2**-level
                try:vv,*_=self.constraints(Z,False)
                except ValueError:continue
                if np.max(abs(vv))<norm*(1-1e-4*2**-level):Y=Z;accepted=True;break
            if not accepted:raise ValueError('Full self-polar and physical-mass retraction failed')
        raise ValueError('Self-polar mass retraction iteration limit')

    def mechanical(self,X,nroots,jacobian=True):
        pp,h=pairs(X,self.edges);bars=1-h[pp[:,1]]/np.sum(X[pp[:,0]]**2,axis=1);root=int(np.argmax(np.sum(X*X,axis=1)))
        roots=[root]+[int(pp[i,0]) for i in np.argsort(-bars)[:max(nroots-1,0)]]
        val,ii,jj,sg=capacities(X,roots);keep=np.ones(len(X),bool);keep[roots[1:]]=False;val=val[keep]
        if not jacobian:return val
        ii=ii[keep];jj=jj[keep];sg=sg[keep];src=X[ii];d=X[jj]-src;rr=np.sum(src*src,1);dd=np.sum(d*d,1);den=np.sqrt(rr*dd);w=np.sum(src*d,1)/den
        gi=(d-src)/den[:,None]-w[:,None]*(src/rr[:,None]-d/dd[:,None]);gj=src/den[:,None]-w[:,None]*d/dd[:,None]
        J=np.zeros((len(ii),self.N,3));J[np.arange(len(ii)),ii]=sg[:,None]*gi;J[np.arange(len(ii)),jj]+=sg[:,None]*gj
        return val,J.reshape(len(val),-1)

def run(source,out,steps=1800):
    out=pathlib.Path(out);out.mkdir(parents=True,exist_ok=False);data=pathlib.Path(source).read_bytes();(out/'source_body.npz').write_bytes(data)
    X=np.load(out/'source_body.npz')['X'];X,closure=center(X);body=Body(X);X=body.retract(X);nroots=max(1,check(X)['row']['U']-1)
    (out/'definition.json').write_text(json.dumps(dict(source=str(pathlib.Path(source).resolve()),steps=steps,E=body.E,vertices=len(X),initial_centering=closure,
        scope='Literal negative-self-polar contacts and actual mass are both maintained; only full actual110 is a nomination'),indent=2))
    (out/'source.py').write_bytes(pathlib.Path(__file__).read_bytes());np.savez(out/'entrance.npz',X=X,Q=-X)
    history=[];failures=[];trust=.03;start=time.time();eps=2e-8
    for it in range(steps):
        m=check(X);st=m['row']
        if max(abs(m['g']))>1e-10:raise ValueError('Independent physical centroid readback failed')
        pp,h=pairs(m['P'],m['ep']);bars=1-h[pp[:,1]]/np.sum(m['P'][pp[:,0]]**2,axis=1)
        if st['S']==st['U']==1:
            np.savez(out/'POTENTIAL_OWN110.npz',X=X,Q=-X);(out/'POTENTIAL_OWN110.json').write_text(json.dumps(st,indent=2));return
        if st['U']<=nroots:nroots=max(1,st['U']-1);trust=.03
        v,J,gaps,G,g,V=body.constraints(X);mv,M=body.mechanical(X,nroots);merit=float(np.maximum(eps-mv,0).sum())
        row=dict(it=it,nroots=nroots,merit=merit,minimum=float(mv.min()),Pmax=float(max(bars,default=0)),constraint_residual=float(np.max(abs(v))),
            selfpolar_error=m['selfpolar_error'],trust=trust,seconds=time.time()-start,**st);history.append(row)
        np.savez(out/'latest.npz',X=X,Q=-X);(out/'history.json').write_text(json.dumps(history,indent=2))
        if it%5==0:print('SELF_POLAR_MASS_GOAL',json.dumps(row),flush=True)
        scale=np.maximum(np.linalg.norm(J,axis=1),1e-12);U,s,Vt=svd(J/scale[:,None],full_matrices=True,check_finite=False)
        if s[-1]<1e-10:raise ValueError('Physical mass/contact tangent has deficient row rank')
        T=Vt[len(v):].T;d=T.shape[1];bound=trust/np.sqrt(d);A=M@T;gapA=G@T
        relevant=gaps<bound*np.abs(gapA).sum(1)+1e-5;gapA=gapA[relevant];gapv=gaps[relevant]*.8
        ms=np.maximum(bound*np.abs(A).sum(1),1e-10);gs=np.maximum(bound*np.abs(gapA).sum(1),1e-10);n=len(mv)
        mat=vstack([hstack([-csr_matrix(A/ms[:,None]),-diags(1/ms)]),hstack([-csr_matrix(gapA/gs[:,None]),csr_matrix((len(gapv),n))])],format='csr')
        rhs=np.r_[(mv-eps)/ms,gapv/gs];lp=linprog(np.r_[np.zeros(d),np.ones(n)],A_ub=mat,b_ub=rhs,bounds=[(-bound,bound)]*d+[(0,None)]*n,
            method='highs',options={'primal_feasibility_tolerance':1e-9,'dual_feasibility_tolerance':1e-9})
        accepted=False
        if lp.success:
            D=(T@lp.x[:d]).reshape(X.shape)
            for level in range(16):
                try:
                    Y=body.retract(X+D*2**-level);mm=check(Y);actual=mm['row']
                    if actual['S']==actual['U']==1:
                        np.savez(out/'POTENTIAL_OWN110.npz',X=Y,Q=-Y);(out/'POTENTIAL_OWN110.json').write_text(json.dumps(actual,indent=2));return
                    vv=body.mechanical(Y,nroots,False);new=float(np.maximum(eps-vv,0).sum());pred=merit-float(np.maximum(eps-(mv+M@D.ravel()*2**-level),0).sum())
                    if new<merit-max(1e-13,1e-4*max(pred,0)):
                        X=Y;accepted=True;row.update(alpha=2**-level,predicted=pred,actual_decrease=merit-new);break
                except (ValueError,RuntimeError,AssertionError,np.linalg.LinAlgError) as error:
                    if len(failures)<100:failures.append(dict(it=it,level=level,error=repr(error)))
        if accepted and level==0:trust=min(.15,trust*1.2)
        elif not accepted:trust*=.4
        if trust<1e-10:break
    (out/'failed_proposals.json').write_text(json.dumps(failures,indent=2));(out/'FINITE_END.json').write_text(json.dumps(dict(iterations=len(history),seconds=time.time()-start,
        scope='Finite full physical self-polar mass flow ended without a qualifying Figure'),indent=2))

if __name__=='__main__':
    import sys
    run(sys.argv[1],sys.argv[2],int(sys.argv[3]) if len(sys.argv)>3 else 1800)
