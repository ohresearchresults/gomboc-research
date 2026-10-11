"""Direct physical C2-symmetric <=85-input homogeneous Figure search.

The common-height basal quadrilateral and unique axial top vertex supply the
stable and unstable roots. All other contacts use the actual uniform centroid.
No approximate coplanar grouping or small-positive-equilibrium cutoff is used.
"""
import argparse,json,time
from pathlib import Path
import numpy as np
from scipy.optimize import linprog
from scipy.sparse import csr_matrix,eye,hstack,vstack
from vertex_geometry import geometry
from direct_face_polish import face_scores
from support_geometry import escape
from goal_nomination import preserve

class Family:
    def __init__(self,X):
        n=(len(X)-5)//2
        assert len(X)==2*n+5 and len(X)<=85
        assert np.array_equal(X[4:4+n]*[-1,-1,1],X[4+n:-1])
        assert np.array_equal(X[1],X[0]*[-1,-1,1])
        assert np.array_equal(X[3],X[2]*[-1,-1,1])
        assert np.all(X[:4,2]==X[0,2]) and np.all(X[-1,:2]==0)
        self.n=n;self.d=6+3*n
        self.B=np.zeros((len(X),3,self.d))
        for i in range(4):
            self.B[i,2,0]=1
            pair=i//2;sign=1 if i%2==0 else -1
            self.B[i,0,1+pair*2]=sign;self.B[i,1,2+pair*2]=sign
        for i in range(n):
            for k in range(3):
                self.B[4+i,k,5+3*i+k]=1
                self.B[4+n+i,k,5+3*i+k]=1 if k==2 else -1
        self.B[-1,2,-1]=1
        self.q=np.r_[X[0,2],X[0,:2],X[2,:2],X[4:4+n].ravel(),X[-1,2]]
        assert np.array_equal(self.points(self.q),X)
        self.orient=np.sign(np.linalg.det(X[[0,2],:2]))

    def points(self,q):return np.einsum('ncd,d->nc',self.B,q)

    def evaluate(self,q,derivative=True):
        X=self.points(q)
        if min(X[4:-1,2])<=X[0,2]+1e-8 or max(X[:-1,2])>=X[-1,2]-1e-8:
            raise ValueError('basal or apical invariant')
        if self.orient*np.linalg.det(X[[0,2],:2])<1e-6:raise ValueError('base degeneracy')
        g=geometry(X,derivative)
        if derivative:
            B=self.B.reshape(X.size,self.d)
            for k in ('DX','DZ','DH','Dg'):g[k]=g[k]@B
        vf,JF,_=face_scores(g,derivative);mask=~np.all(g['T']<4,axis=1)
        ids=g['vertices'];A=g['Z'][ids]
        if derivative:vu,_,JU=escape(A,g['DZ'][ids],angular=True)
        else:vu,_=escape(A,angular=True);JU=None
        um=ids!=len(X)-1
        if len(np.flatnonzero(~mask))!=2:raise ValueError('base not a genuine quadrilateral in numeric hull')
        cl=dict(S=1+int(sum(vf[mask]<0)),U=int(sum(vu<0)),V=len(ids),min_face=float(min(vf[mask])),min_escape=float(min(vu[um])),centroid_z=float(g['g'][2]))
        return g,vf[mask],vu[um],JF[mask]if derivative else None,JU[um]if derivative else None,cl

def run(source,out,steps,epsilon,hard_u):
    out=Path(out);out.mkdir(parents=True,exist_ok=False);X=np.load(source);F=Family(X);q=F.q.copy();np.save(out/'initial.npy',X)
    rng=np.random.default_rng(11905);qq=q+rng.normal(0,1e-7,len(q));g,f,u,Jf,Ju,_=F.evaluate(qq);d=rng.normal(size=len(q));d/=np.linalg.norm(d);h=1e-8
    plus=F.evaluate(qq+h*d,False);minus=F.evaluate(qq-h*d,False)
    # Select guards at a generic physical cell; every later topology is rebuilt.
    check=dict(face_fd=float((plus[1].sum()-minus[1].sum())/(2*h)),face_analytic=float(Jf.sum(0)@d),u_fd=float((plus[2].sum()-minus[2].sum())/(2*h)),u_analytic=float(Ju.sum(0)@d))
    (out/'gradient_check.json').write_text(json.dumps(check,indent=2))
    assert abs(check['face_fd']-check['face_analytic'])<2e-5
    assert abs(check['u_fd']-check['u_analytic'])<2e-5
    trace=[];trust=.002;start=time.time();eps=epsilon
    for it in range(steps):
        g,f,u,Jf,Ju,cl=F.evaluate(q);v=np.r_[f,u];merit=float(np.maximum(eps-v,0).sum());row=dict(it=it,merit=merit,trust=trust,seconds=time.time()-start,**cl);trace.append(row)
        np.save(out/'latest.npy',g['X']);np.save(out/'parameters.npy',q);(out/'trace.json').write_text(json.dumps(trace,indent=2))
        if it%10==0:print('C2_PHYSICAL_GOAL',out,row,flush=True)
        if cl['S']==cl['U']==1:
            preserve(g['X'],out/f'exact_goal_{it:05d}','C2 symmetric physical body; actual filled-centroid numerical census110; all exact weak contacts still required')
        d=len(q);sc=.005;m=len(f)if hard_u else len(v);J=Jf if hard_u else np.vstack((Jf,Ju));vv=f if hard_u else v
        A=[hstack([-csr_matrix(J/sc),-eye(m)])];b=[(vv-eps)/sc]
        if hard_u:
            A.append(hstack([-csr_matrix(Ju/sc),csr_matrix((len(u),m))]));b.append((u-eps)/sc)
        lp=linprog(np.r_[np.zeros(d),np.ones(m)],A_ub=vstack(A,format='csr'),b_ub=np.concatenate(b),bounds=[(-trust,trust)]*d+[(0,None)]*m,method='highs',options=dict(primal_feasibility_tolerance=1e-9,dual_feasibility_tolerance=1e-9,time_limit=10.))
        ok=False
        if lp.success:
            for k in range(16):
                qt=q+2.**-k*lp.x[:d]
                try:gg,ff,uu,_,_,cc=F.evaluate(qt,False)
                except(ValueError,np.linalg.LinAlgError):continue
                mm=float(np.maximum(eps-np.r_[ff,uu],0).sum())
                if cc['S']==cc['U']==1:
                    preserve(gg['X'],out/f'exact_goal_{it:05d}_line{k}','C2 physical line trial; actual filled-centroid numerical110')
                if hard_u and min(uu)<=eps*.95:continue
                if mm<merit-max(1e-13,merit*1e-8):q=qt;ok=True;row['alpha']=2.**-k;break
        else:row['lp_error']=lp.message
        if ok:
            if k==0:trust=min(.03,trust*1.25)
        else:trust*=.4
        if trust<1e-10:break
    np.save(out/'endpoint.npy',F.points(q));print('C2_PHYSICAL_FINITE_STOP',out,trace[-1],flush=True)

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('source');p.add_argument('out');p.add_argument('--steps',type=int,default=600);p.add_argument('--epsilon',type=float,default=1e-7);p.add_argument('--soft-u',action='store_true');a=p.parse_args();run(a.source,a.out,a.steps,a.epsilon,not a.soft_u)
