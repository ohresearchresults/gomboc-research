"""Physical <=84-halfspace Figure search with canonical projective mass.

A physical projective transformation y=x/(1+p.x) changes every support vector
Q_i to Q_i+p. We solve the actual uniform centroid equation using integrated
second moments, then differentiate p implicitly. Reference normal-shadow S1
is never confused with the actual post-normalization physical census.
"""
import argparse,json,time
from pathlib import Path
import numpy as np
from scipy.optimize import linprog
from scipy.sparse import csr_matrix,eye,hstack,vstack
from support_geometry import geometry,census,escape
from dual_shadow_goal import Generator,bars as pbars
from canonical_projective_mass import moment_jacobian
from shadow_mass_retracted_goal import bars as qbars
from bounded_goal_search import exact_support

def center(Q,DQ=None):
    p=np.zeros(3)
    for iteration in range(60):
        g=geometry(Q+p,False);a=dict(X=g['X'],T=g['tris'],V=g['V'],g=g['g']);res=np.linalg.norm(g['g']);J=moment_jacobian(a)
        if res<1e-14:break
        step=np.linalg.solve(J,-g['g']);ok=False
        for k in range(22):
            pp=p+2.**-k*step
            try:gg=geometry(Q+pp,False)
            except(ValueError,np.linalg.LinAlgError):continue
            if np.linalg.norm(gg['g'])<res*(1-1e-5):p=pp;ok=True;break
        if not ok:raise ValueError('actual support-body projective centroid iteration did not descend')
    else:raise ValueError('actual support-body projective centroid iteration limit')
    if DQ is not None:
        g=geometry(Q+p,True);J=moment_jacobian(dict(X=g['X'],T=g['tris'],V=g['V'],g=g['g']));d=DQ.shape[-1];Dp=np.linalg.solve(J,-g['Dg']@DQ.reshape(Q.size,d));B=(DQ+Dp).reshape(Q.size,d);g['JZ']=g['DZ']@B;g['JH']=g['DH']@B;g['Dp']=Dp
    owners={}
    for f,cy in enumerate(g['faces']):
        for i,j in zip(cy,cy[1:]+cy[:1]):owners.setdefault(tuple(sorted((i,j))),[]).append(f)
    assert all(len(v)==2 for v in owners.values());g['edges']=np.array(list(owners));g['dual_edges']=np.array(list(owners.values()));g['normalization_p']=p;return g

def stable_bars(g,derivative=True):
    # Reuse the primal persistence computation on this body's polar points.
    dual=dict(Z=g['H'],edges=g['dual_edges'])
    if derivative:dual['JZ']=g['JH']
    return pbars(dual,derivative)

def model(F,q,derivative=True):
    Q,DQ=F.construct(q);return center(Q,DQ if derivative else None)

def run(source,out,steps=1400,seed=None,repair=False,mode='joint',floor=1e-8):
    out=Path(out);out.mkdir(parents=True,exist_ok=False);F=Generator(np.load(source),seed,repair,floor);q=F.q.copy();g=model(F,q);cl=census(g)
    (out/'definition.json').write_text(json.dumps(dict(source=str(Path(source).resolve()),seed=seed,repair_reference=repair,mode=mode,cost_floor=floor,parent=F.parent.tolist(),order=F.order,base_direction=F.base_direction.tolist(),tangent1=F.tangent1.tolist(),tangent2=F.tangent2.tolist(),physical_definition='uniform intersection (Q_i+p).x<=1, p determined from its actual uniform centroid using integrated second moments; <=84 halfspaces'),indent=2))
    if mode=='hard'and cl['S']!=1:raise ValueError('hardS1 requested for a post-map body with multiple stable equilibria')
    trace=[];trust=.003;start=time.time()
    for it in range(steps):
        g=model(F,q);cl=census(g);P,JP=pbars(g);Q,JQ=stable_bars(g);pm=float(max(P,default=0.));qm=float(max(Q,default=0.));merit=pm+(qm if mode=='joint'else 0.);row=dict(it=it,Pmax=pm,Qmax=qm,positive_P=len(P),positive_Q=len(Q),merit=merit,trust=trust,seconds=time.time()-start,**cl);trace.append(row);np.save(out/'latest_supports.npy',g['Q']);np.save(out/'latest_parameters.npy',q);np.save(out/'latest_projective_p.npy',g['normalization_p']);(out/'latest.json').write_text(json.dumps(row,indent=2));(out/'trace.json').write_text(json.dumps(trace,indent=2))
        if it%10==0:print('PROJECTIVE_MASS_NORMAL',out,row,flush=True)
        if cl['S']==cl['U']==1:exact_support(g['Q'],out/f'exact_goal_{it:05d}')
        d=F.d;ns=2 if mode=='joint'else 1;blocks=[];rhs=[]
        for k,(v,J)in enumerate([(P,JP)]+([(Q,JQ)]if mode=='joint'else [])):
            if not len(v):continue
            S=np.zeros((len(v),ns));S[:,k]=-1;blocks.append(hstack((csr_matrix(J),S,csr_matrix((len(v),d)))));rhs.append(-v)
        if mode=='hard':
            assert cl['S']==1;v,_,J=escape(g['H'],g['JH']);root=np.argmax(np.sum(g['H']**2,axis=1));mask=np.arange(len(v))!=root;eps=min(1e-10,float(min(v[mask]))*.05);blocks.append(hstack((-csr_matrix(J[mask]),csr_matrix((sum(mask),ns+d)))));rhs.append(v[mask]-eps)
        I=eye(d);O=csr_matrix((d,ns));blocks.extend((hstack((I,O,-I)),hstack((-I,O,-I))));rhs.append(np.zeros(2*d));bd=[(max(a-x,-trust),min(b-x,trust))for x,(a,b)in zip(q,F.bounds)]+[(0,None)]*(d+ns);lp=linprog(np.r_[np.zeros(d),np.ones(ns),np.full(d,1e-8)],A_ub=vstack(blocks,format='csr'),b_ub=np.concatenate(rhs),bounds=bd,method='highs',options=dict(primal_feasibility_tolerance=1e-10,dual_feasibility_tolerance=1e-10,time_limit=15.));ok=False
        if lp.success:
            for k in range(18):
                qq=q+2.**-k*lp.x[:d];qq=np.array([min(b,max(a,x))for x,(a,b)in zip(qq,F.bounds)])
                try:gg=model(F,qq,False);cc=census(gg)
                except(ValueError,np.linalg.LinAlgError):continue
                if mode=='hard'and cc['S']!=1:continue
                if cc['S']==cc['U']==1:exact_support(gg['Q'],out/f'exact_goal_{it:05d}_line{k}')
                pp=pbars(gg,False)[0];qqq=stable_bars(gg,False)[0];mm=float(max(pp,default=0.))+(float(max(qqq,default=0.))if mode=='joint'else 0.)
                if mm<merit-max(1e-13,merit*1e-8):q=qq;ok=True;row['alpha']=2.**-k;break
        else:row['lp_error']=lp.message
        if ok:
            if k==0:trust=min(.04,trust*1.35)
            elif k>6:trust*=.7
        else:trust*=.4
        if trust<1e-10:break
    g=model(F,q,False);np.save(out/'endpoint_supports.npy',g['Q']);np.save(out/'endpoint_parameters.npy',q);print('PROJECTIVE_MASS_NORMAL_FINITE_STOP',out,trace[-1],flush=True)

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('source');p.add_argument('out');p.add_argument('--steps',type=int,default=1400);p.add_argument('--seed',type=int);p.add_argument('--repair',action='store_true');p.add_argument('--mode',choices=['hard','joint'],default='joint');p.add_argument('--cost-floor',type=float,default=1e-8);a=p.parse_args();run(a.source,a.out,a.steps,a.seed,a.repair,a.mode,a.cost_floor)
