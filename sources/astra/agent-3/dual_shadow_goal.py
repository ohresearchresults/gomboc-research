"""Homogeneous physical half-space bodies from a positive-shadow normal graph.

The generator's points are SUPPORT VECTORS, not physical mass points. Physical
K={x:Q_i.x<=1} is filled uniformly, integrated, and centred by actual equations.
ReferenceU1 of conv(Q) implies referenceS1 of K. <=84 halfspaces gives E<=246,
sum<=494. Complete exact primal hull, centroid and weak census decide success.
"""
import argparse,json,time
from pathlib import Path
import numpy as np
from scipy.optimize import linprog,lsq_linear
from scipy.sparse import csr_matrix,eye,hstack,vstack
from support_geometry import geometry,escape,census
from exact_audit_supports import audit
from goal_nomination import ExactGoalCandidateFound

class Generator:
    def __init__(self,Q,seed=None,repair_reference=False,cost_floor=1e-8):
        assert len(Q)<=84;self.n=len(Q)-1;self.ad=2*self.n;self.d=3*self.n
        assert cost_floor>0;self.cost_floor=cost_floor
        r=np.linalg.norm(Q,axis=1);root=int(np.argmax(r));ids=[i for i in range(len(Q))if i!=root]+[root];Q=Q[ids];axis=Q[-1]/r[root];e=np.eye(3)[np.argmin(abs(axis))];e-=axis*(e@axis);e/=np.linalg.norm(e);R=np.array([e,np.cross(axis,e),axis]);Q=Q@R.T/r[root];Q[-1]=[0.,0.,1.]
        radii=np.linalg.norm(Q,axis=1);U=Q/radii[:,None];C=U@U.T;caps=C[:-1]*radii[None];np.fill_diagonal(caps[:,:self.n],-np.inf);parent=caps.argmax(1);bestcap=caps[np.arange(self.n),parent]
        if min(bestcap)<=0:raise ValueError('a normal direction has no positive-cosine neighbour')
        cost=-np.log(radii[:-1]/bestcap)
        if repair_reference:
            # This constructs DIFFERENT support vectors. It is not a relaxed
            # census or deletion of small equilibrium bars in the source body.
            cost=np.maximum(cost,cost_floor);edge=np.full_like(C,np.inf);ok=C>1e-12;edge[ok]=-np.log(np.minimum(C[ok],1));edge+=np.r_[cost,0.][:,None];dist=np.full(len(Q),np.inf);dist[-1]=0;used=np.zeros(len(Q),bool);pa=np.full(len(Q),-1,int)
            for _ in range(len(Q)):
                j=int(np.argmin(np.where(used,np.inf,dist)))
                if not np.isfinite(dist[j]):raise ValueError('normal direction graph disconnected from stable root')
                used[j]=True;new=dist[j]+edge[:,j];take=(new<dist)&(~used);dist[take]=new[take];pa[take]=j
            parent=pa[:-1];radii=np.exp(-dist);caps=C[:-1]*radii[None];np.fill_diagonal(caps[:,:self.n],-np.inf)
        else:assert min(cost)>0
        if seed is not None:
            rng=np.random.default_rng(seed)
            for i in range(self.n):
                valid=np.flatnonzero(caps[i]>radii[i]*np.exp(1.0001*cost_floor))
                if len(valid):parent[i]=int(rng.choice(valid))
                cost[i]=np.log(caps[i,parent[i]]/radii[i])
        self.parent=np.r_[parent,-1];self.order=list(map(int,np.argsort(radii)[::-1]));assert self.order[0]==self.n
        self.base_direction=U[:-1].copy();E=[]
        for u in self.base_direction:
            e=np.eye(3)[np.argmin(abs(u))];e-=u*(e@u);e/=np.linalg.norm(e);E.append(e)
        self.tangent1=np.array(E);self.tangent2=np.cross(self.base_direction,self.tangent1)
        self.q=np.r_[np.zeros(self.ad),np.maximum(cost,cost_floor)];self.bounds=[(-3.,3.)]*self.ad+[(cost_floor,3.)]*self.n;self.rotation=R;self.scale=float(r[root]);self.source_ids=ids

    def construct(self,q):
        n=self.n;d=self.d;ab=q[:self.ad].reshape(n,2);raw=self.base_direction+ab[:,0,None]*self.tangent1+ab[:,1,None]*self.tangent2;norm=np.linalg.norm(raw,axis=1);U=np.vstack((raw/norm[:,None],[0.,0.,1.]));DU=np.zeros((n+1,3,d))
        for i in range(n):
            DU[i,:,2*i]=(self.tangent1[i]-U[i]*(U[i]@self.tangent1[i]))/norm[i];DU[i,:,2*i+1]=(self.tangent2[i]-U[i]*(U[i]@self.tangent2[i]))/norm[i]
        R=np.zeros(n+1);R[n]=1;DR=np.zeros((n+1,d))
        for i in self.order[1:]:
            j=self.parent[i];c=U[i]@U[j]
            if c<=0 or q[self.ad+i]<=0:raise ValueError('invalid fixed positive-shadow normal path')
            Dc=DU[i].T@U[j]+DU[j].T@U[i];k=np.exp(-q[self.ad+i]);R[i]=R[j]*c*k;DR[i]=k*(c*DR[j]+R[j]*Dc);DR[i,self.ad+i]-=R[i]
        return R[:,None]*U,DR[:,None,:]*U[:,:,None]+R[:,None,None]*DU

def model(F,q,derivative=True):
    Q,DQ=F.construct(q);g=geometry(Q,derivative)
    owners={}
    for cy in g['faces']:
        for i,j in zip(cy,cy[1:]+cy[:1]):owners.setdefault(tuple(sorted((i,j))),0)
    g['edges']=np.array(list(owners))
    if derivative:
        B=DQ.reshape(Q.size,F.d);g['Jg']=g['Dg']@B;g['JZ']=g['DZ']@B
    return g

def bars(g,derivative=True):
    A=g['Z'];ed=g['edges'];aa=np.einsum('ic,ic->i',A,A);i,j=ed.T;e=A[j]-A[i];ee=np.einsum('ic,ic->i',e,e);t=np.clip(-np.einsum('ic,ic->i',A[i],e)/np.where(ee>0,ee,1),0,1);feet=A[i]+t[:,None]*e;death=np.einsum('ic,ic->i',feet,feet);pa=np.arange(len(A));v=[];J=[]
    def find(k):
        while pa[k]!=k:pa[k]=pa[pa[k]];k=pa[k]
        return k
    for k in np.argsort(death)[::-1]:
        a,b=find(int(i[k])),find(int(j[k]))
        if a==b:continue
        if(aa[a],a)>(aa[b],b):a,b=b,a
        pa[a]=b;dep=aa[a]-death[k]
        if dep<=0:continue
        v.append(dep/aa[a])
        if derivative:
            Db=2*A[a]@g['JZ'][a];Dd=2*feet[k]@((1-t[k])*g['JZ'][i[k]]+t[k]*g['JZ'][j[k]]);J.append(death[k]/aa[a]**2*Db-Dd/aa[a])
    return np.array(v),np.array(J)if derivative else None

def restore(F,q,limit=35):
    q=q.copy();history=[]
    for _ in range(limit):
        g=model(F,q);res=float(np.linalg.norm(g['g']));history.append(res)
        if res<2e-14:return q,g,history
        free=np.arange(F.d);lower=np.array([lo-x for x,(lo,hi)in zip(q,F.bounds)]);upper=np.array([hi-x for x,(lo,hi)in zip(q,F.bounds)])
        # Correct actual mass using both direction and radial-cost controls.
        # Positive cost bounds keep every fixed reference escape path strict.
        sol=lsq_linear(g['Jg'][:,free],-g['g'],bounds=(lower,upper),tol=1e-13,max_iter=100,lsmr_tol='auto');step=sol.x;ok=False
        for k in range(17):
            qq=q.copy();qq[free]+=2.**-k*step;qq=np.array([min(hi,max(lo,x))for x,(lo,hi)in zip(qq,F.bounds)])
            try:gg=model(F,qq,False)
            except(ValueError,np.linalg.LinAlgError):continue
            if np.linalg.norm(gg['g'])<res*(1-1e-5):q=qq;ok=True;break
        if not ok:return None,None,history
    return None,None,history

def freeze(g,out):
    out=Path(out);out.mkdir(parents=True,exist_ok=False);Q=g['Q'];np.save(out/'literal_supports.npy',Q);D=max(float(x).as_integer_ratio()[1]for x in Q.ravel());a=audit(out/'literal_supports.npy',out/'exact',D)
    if a['counts']==[1,1,0]and a['weak']==[0,0,0]and 34<=2*a['E']<500 and a['V']+a['E']+a['F']<500:raise ExactGoalCandidateFound('Exact physical dual-shadow Figure '+str(out))

def run(source,out,steps,seed,repair_reference=False):
    out=Path(out);out.mkdir(parents=True,exist_ok=False);F=Generator(np.load(source),seed,repair_reference);q=F.q.copy();(out/'definition.json').write_text(json.dumps(dict(source=str(Path(source).resolve()),parent=F.parent.tolist(),order=F.order,source_ids=F.source_ids,rotation=F.rotation.tolist(),normal_scale=F.scale,seed=seed,direction_chart='normalize(base_direction+a*tangent1+b*tangent2)',base_direction=F.base_direction.tolist(),tangent1=F.tangent1.tolist(),tangent2=F.tangent2.tolist(),reference_repair_constructs_new_normals=repair_reference,physical_definition='uniform density on K={x:Q_i dot x<=1}; Q is a normal generator, not a physical mass discretization',max_halfspaces=84,max_edges=246),indent=2))
    rng=np.random.default_rng(601381);t=q+rng.normal(0,1e-5,len(q));t[F.ad:]=np.maximum(t[F.ad:],1e-4);d=rng.normal(size=F.d);d/=np.linalg.norm(d);h=1e-7;g=model(F,t);gp=model(F,t+h*d,False);gm=model(F,t-h*d,False);check=dict(physical_centroid_derivative_error=float(max(abs((gp['g']-gm['g'])/(2*h)-g['Jg']@d))));(out/'gradient_check.json').write_text(json.dumps(check,indent=2));assert check['physical_centroid_derivative_error']<1e-5
    q,g,hist=restore(F,q,limit=150);(out/'initial_mass_restoration.json').write_text(json.dumps(hist))
    if q is None:raise ValueError('physical half-space body centroid closure failed; no candidate admitted')
    trust=.005;trace=[];start=time.time()
    for it in range(steps):
        g=model(F,q);cl=census(g);values,J=bars(g);val=float(max(values,default=0.));row=dict(it=it,Pmax=val,positive_P=len(values),trust=trust,seconds=time.time()-start,**cl);trace.append(row);np.save(out/'latest_supports.npy',g['Q']);np.save(out/'latest_parameters.npy',q);(out/'latest.json').write_text(json.dumps(row,indent=2));(out/'trace.json').write_text(json.dumps(trace,indent=2))
        if it%10==0:print('DUAL_SHADOW_GOAL',out,row,flush=True)
        if cl['S']!=1:raise ValueError('actual physical body lost unique stable equilibrium after mass closure')
        if cl['S']==cl['U']==1:freeze(g,out/f'exact_goal_{it:05d}')
        d=F.d;m=len(values);I=eye(d);O=csr_matrix((d,1));A=vstack([hstack([csr_matrix(J),-np.ones((m,1)),csr_matrix((m,d))]),hstack([I,O,-I]),hstack([-I,O,-I])],format='csr');bb=np.r_[-values,np.zeros(2*d)];Aeq=hstack([csr_matrix(g['Jg']),csr_matrix((3,1+d))]);bd=[(max(lo-x,-trust),min(hi-x,trust))for x,(lo,hi)in zip(q,F.bounds)]+[(0,None)]+[(0,None)]*d
        lp=linprog(np.r_[np.zeros(d),1.,np.full(d,1e-8)],A_ub=A,b_ub=bb,A_eq=Aeq,b_eq=-g['g'],bounds=bd,method='highs',options=dict(primal_feasibility_tolerance=1e-10,dual_feasibility_tolerance=1e-10,time_limit=10.));ok=False
        if lp.success:
            for k in range(16):
                qq=q+2.**-k*lp.x[:d]
                # Exact box projection defines the trial parameters explicitly;
                # actual geometry, mass and census are recomputed afterwards.
                qq=np.array([min(hi,max(lo,x))for x,(lo,hi)in zip(qq,F.bounds)])
                try:qq,gg,hist=restore(F,qq)
                except(ValueError,np.linalg.LinAlgError):continue
                if qq is None:continue
                cc=census(gg)
                if cc['S']!=1:continue
                if cc['U']==1:freeze(gg,out/f'exact_goal_{it:05d}_line{k}')
                vv=bars(gg,False)[0];value=float(max(vv,default=0.))
                if value<val-max(1e-13,val*1e-8):q=qq;ok=True;row['alpha']=2.**-k;break
        else:row['lp_error']=lp.message
        if ok:
            if k==0:trust=min(.03,trust*1.3)
            elif k>4:trust*=.7
        else:trust*=.4
        if trust<1e-10:break
    np.save(out/'endpoint_supports.npy',model(F,q,False)['Q']);print('DUAL_SHADOW_FINITE_STOP',out,trace[-1],flush=True)

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('source');p.add_argument('out');p.add_argument('--steps',type=int,default=1200);p.add_argument('--seed',type=int);p.add_argument('--repair-reference',action='store_true');a=p.parse_args();run(a.source,a.out,a.steps,a.seed,a.repair_reference)
