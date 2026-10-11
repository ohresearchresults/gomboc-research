"""Positive-shadow Figure search with actual mass correction on every step.

All three centroid equations are solved by small direction adjustments. Every
admitted literal body is then checked at its computed OWN centroid. A linear
minimax model includes every positive stable persistence bar, not a selected
thresholded subset. The <=85 inputs and genuine base impose E<=248.
"""
import argparse,json,time
from pathlib import Path
import numpy as np
from scipy.optimize import linprog
from scipy.sparse import csr_matrix,eye,hstack,vstack
from shadow_centroid_goal import Family
from vertex_geometry import geometry
from direct_face_polish import face_scores
from support_geometry import escape
from goal_nomination import preserve

def model(F,q,derivative=True):
    X,DX=F.construct(q);g=geometry(X,derivative)
    if derivative:
        B=DX.reshape(X.size,F.d);g['Jg']=g['Dg']@B;g['JH']=g['DH']@B;g['Jheight']=DX[4:,2]-DX[0,2]
    g['constraints']=g['g']
    if derivative:g['Jconstraints']=g['Jg']
    if hasattr(F,'last_plane'):
        g['constraints']=np.r_[g['constraints'],F.last_plane]
        if derivative:g['Jconstraints']=np.vstack((g['Jconstraints'],F.last_Jplane))
    g['height_gap']=X[4:,2]-X[0,2];g['domain']=g['height_gap']-1e-6
    if derivative:g['Jdomain']=g['Jheight']
    if hasattr(F,'domain'):
        v,J=F.domain(q);g['domain']=np.r_[g['domain'],v]
        if derivative:g['Jdomain']=np.vstack((g['Jdomain'],J))
    return g

def restore(F,q,limit=40):
    q=q.copy();history=[]
    for iteration in range(limit):
        g=model(F,q);res=float(np.linalg.norm(g['constraints']));history.append(res)
        if res<2e-14:return q,g,history
        free=np.array(getattr(F,'restore_free',getattr(F,'mass_controls',np.arange(2*F.n))),int)
        if hasattr(F,'bounds'):
            margin=np.array([min(x-lo,hi-x)for x,(lo,hi)in zip(q,F.bounds)]);free=free[margin[free]>1e-7]
        else:
            theta=q[:2*F.n:2];free=free[np.repeat(abs(theta)<1.549,2)[free]]
        A=g['Jconstraints'][:,free];step=np.linalg.lstsq(A,-g['constraints'],rcond=1e-12)[0];ok=False
        for k in range(15):
            qq=q.copy();qq[free]+=2.**-k*step
            if not hasattr(F,'bounds')and max(abs(qq[:2*F.n:2]))>=1.55:continue
            if hasattr(F,'bounds')and any(v<lo or v>hi for v,(lo,hi)in zip(qq,F.bounds)):continue
            try:gg=model(F,qq,False)
            except(ValueError,np.linalg.LinAlgError):continue
            if min(gg['domain'])<=0:continue
            if np.linalg.norm(gg['constraints'])<res*(1-1e-4):q=qq;ok=True;break
        if not ok:return None,None,history
    return None,None,history

def bars(g,derivative=True):
    T=g['T'];owners={}
    for f,tri in enumerate(T):
        for i,j in zip(tri,np.roll(tri,-1)):owners.setdefault(tuple(sorted((int(i),int(j)))),[]).append(f)
    assert all(len(v)==2 for v in owners.values());ed=np.array(list(owners.values()));A=g['H'];aa=np.einsum('ic,ic->i',A,A);i,j=ed.T;e=A[j]-A[i];ee=np.einsum('ic,ic->i',e,e);t=np.clip(-np.einsum('ic,ic->i',A[i],e)/np.where(ee>0,ee,1),0,1);feet=A[i]+t[:,None]*e;death=np.einsum('ic,ic->i',feet,feet);parent=np.arange(len(A));values=[];Js=[];features=[]
    def find(k):
        while parent[k]!=k:parent[k]=parent[parent[k]];k=parent[k]
        return k
    for k in np.argsort(death)[::-1]:
        u,v=find(int(i[k])),find(int(j[k]))
        if u==v:continue
        if(aa[u],u)>(aa[v],v):u,v=v,u
        parent[u]=v;dep=aa[u]-death[k]
        if dep<=0:continue
        values.append(dep/aa[u]);features.append((int(u),int(i[k]),int(j[k])))
        if derivative:
            DB=2*A[u]@g['JH'][u];DD=2*feet[k]@((1-t[k])*g['JH'][i[k]]+t[k]*g['JH'][j[k]]);Js.append(death[k]/aa[u]**2*DB-DD/aa[u])
    return np.array(values),np.array(Js)if derivative else None,features

def census(g):
    v,_,_=face_scores(g,False);mask=~np.all(g['T']<4,axis=1);vu,_=escape(g['Z'][g['vertices']],angular=True)
    # Four coplanar inputs can have either a genuine quadrilateral or a
    # triangle with one nonvertex input. The latter has at most84 vertices,
    # so both cases obey the same E<=248 and Euler-sum<500 bound.
    basevalid=int(sum(~mask))in(1,2)and min(g['height_gap'])>0
    return dict(S=1+int(sum(v[mask]<0)),U=int(sum(vu<0)),V=len(g['vertices']),base_valid=bool(basevalid),centroid_residual=float(np.linalg.norm(g['g'],np.inf)))

def run(source,parameters,out,steps,free_base=False,full_shadow=False,fixed_tree=False,tree_seed=None,cost_floor=1e-8):
    out=Path(out);out.mkdir(parents=True,exist_ok=False)
    if full_shadow:
        from full_shadow_family import Family as FullShadowFamily
        F=FullShadowFamily(np.load(source),cost_floor=cost_floor)
    elif free_base:
        from shadow_free_base_family import Family as FreeBaseFamily
        F=FreeBaseFamily(np.load(source))
    else:F=Family(np.load(source))
    q=np.load(parameters)if parameters else F.q
    if fixed_tree:
        assert full_shadow,'fixed tree requires the complete shadow graph family'
        q=F.freeze_tree(q,tree_seed);(out/'fixed_tree.json').write_text(json.dumps(dict(parent=F.fixed_parent.tolist(),order=F.fixed_order,seed=tree_seed,cost_floor=cost_floor,scope='explicit fixed positive-shadow forest; no alternate-parent substitution within this run'),indent=2))
    q,g,rest=restore(F,q);(out/'initial_mass_restoration.json').write_text(json.dumps(rest))
    if q is None:raise ValueError('initial actual centroid correction failed; no body admitted')
    np.save(out/'initial.npy',g['X']);np.save(out/'initial_parameters.npy',q);trace=[];trust=.005;start=time.time()
    bounds=F.bounds if hasattr(F,'bounds')else[(-1.55,1.55),(-20,20)]*F.n+[(-1.55,-.05),(-20,20)]*2+[(1e-8,2.)]*F.n+[(1e-7,.6)]
    for it in range(steps):
        g=model(F,q);values,J,features=bars(g);value=max(values,default=0.);cl=census(g)
        if not cl['base_valid']or cl['U']!=1:raise ValueError('mass-corrected body lost required physical reference invariant')
        row=dict(it=it,Qmax=float(value),positive_Q=len(values),trust=trust,seconds=time.time()-start,**cl);trace.append(row);np.save(out/'latest.npy',g['X']);np.save(out/'latest_parameters.npy',q);(out/'latest.json').write_text(json.dumps(row,indent=2));(out/'trace.json').write_text(json.dumps(trace,indent=2))
        if it%10==0:print('SHADOW_RETRACTED_GOAL',out,row,flush=True)
        if cl['S']==cl['U']==1:preserve(g['X'],out/f'exact_goal_{it:05d}','independent shadow body, actual uniform centroid restored, numerical own110')
        d=F.d;I=eye(d);O=csr_matrix((d,1));m=len(values)
        Ab=vstack([hstack([csr_matrix(J),-np.ones((m,1)),csr_matrix((m,d))]),hstack([I,O,-I]),hstack([-I,O,-I]),hstack([-csr_matrix(g['Jdomain']),csr_matrix((len(g['domain']),1+d))])],format='csr');bb=np.r_[-values,np.zeros(2*d),g['domain']]
        Aeq=hstack([csr_matrix(g['Jconstraints']),csr_matrix((len(g['constraints']),1+d))]);bd=[(max(lo-qk,-trust),min(hi-qk,trust))for qk,(lo,hi)in zip(q,bounds)]+[(0,None)]+[(0,None)]*d
        lp=linprog(np.r_[np.zeros(d),1.,np.full(d,1e-8)],A_ub=Ab,b_ub=bb,A_eq=Aeq,b_eq=-g['constraints'],bounds=bd,method='highs',options=dict(primal_feasibility_tolerance=1e-10,dual_feasibility_tolerance=1e-10,time_limit=10.))
        ok=False
        if lp.success:
            for k in range(15):
                qq=q+2.**-k*lp.x[:d]
                # HiGHS may miss an active box bound by a few binary ulps.
                # Define the proposed parameters by exact box projection,
                # then reconstruct, integrate and restore this NEW body.
                qq=np.array([min(hi,max(lo,x))for x,(lo,hi)in zip(qq,bounds)])
                try:qq,gg,correction=restore(F,qq)
                except(ValueError,np.linalg.LinAlgError):continue
                if qq is None:continue
                cc=census(gg)
                if not cc['base_valid']or cc['U']!=1:continue
                vals,_,_=bars(gg,False);vv=max(vals,default=0.)
                if cc['S']==cc['U']==1:preserve(gg['X'],out/f'exact_goal_{it:05d}_line{k}','actual mass-corrected positive-shadow line trial own110')
                if vv<value-max(1e-13,value*1e-8):q=qq;ok=True;row['alpha']=2.**-k;break
        else:row['lp_error']=lp.message
        if ok:
            if k==0:trust=min(.03,trust*1.3)
            elif k>4:trust*=.7
        else:trust*=.4
        if trust<1e-10:break
    np.save(out/'endpoint_parameters.npy',q);np.save(out/'endpoint.npy',model(F,q,False)['X']);print('SHADOW_RETRACTED_FINITE_STOP',out,trace[-1],flush=True)

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('source');p.add_argument('out');p.add_argument('--parameters');p.add_argument('--steps',type=int,default=1000);p.add_argument('--free-base',action='store_true');p.add_argument('--full-shadow',action='store_true');p.add_argument('--fixed-tree',action='store_true');p.add_argument('--tree-seed',type=int);p.add_argument('--cost-floor',type=float,default=1e-8);a=p.parse_args();run(a.source,a.parameters,a.out,a.steps,a.free_base,a.full_shadow,a.fixed_tree,a.tree_seed,a.cost_floor)
