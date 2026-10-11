"""All directions free, no basal-plane restriction, physical U1 family.

The positive-shadow coordinate generator is interpreted here as PRIMAL
physical points. Uniform mass is that of their convex hull. <=84 inputs is a
hard E<=246/sum<=494 bound, with no selected facet or symmetry restrictions.
Radial powers create new seeds: for p>=1 every positive reference witness
x_i.(x_j-x_i)>0 remains positive, since r_j>r_i and cos(angle)>0.
No own-centroid claim is made until the new uniform mass equations close.
"""
import argparse,json,time
from pathlib import Path
import numpy as np
from scipy.optimize import linprog,lsq_linear
from scipy.sparse import csr_matrix,eye,hstack,vstack
from dual_shadow_goal import Generator
from vertex_geometry import geometry
from shadow_mass_retracted_goal import bars
from support_geometry import escape
from direct_face_polish import face_scores
from goal_nomination import preserve

def model(F,q,derivative=True):
    X,DX=F.construct(q);g=geometry(X,derivative)
    if derivative:
        B=DX.reshape(X.size,F.d);g['Jg']=g['Dg']@B;g['JH']=g['DH']@B
    return g

def census(g):
    v,_,_=face_scores(g,False);u,_=escape(g['Z'][g['vertices']],angular=True)
    return dict(S=int(sum(v<0)),U=int(sum(u<0)),V=len(g['vertices']),minU=float(np.partition(u,1)[1]),centroid_residual=float(np.linalg.norm(g['g'])))

def restore(F,q,limit=80):
    q=q.copy();history=[]
    for it in range(limit):
        g=model(F,q);res=float(np.linalg.norm(g['g']));history.append(res)
        if res<1e-14:
            if census(g)['U']==1:return q,g,history
            return None,None,history
        lo=np.array([a-x for x,(a,b)in zip(q,F.bounds)]);hi=np.array([b-x for x,(a,b)in zip(q,F.bounds)]);step=lsq_linear(g['Jg'],-g['g'],bounds=(lo,hi),tol=1e-13,max_iter=60,lsmr_tol='auto').x;ok=False
        for k in range(19):
            qq=q+2.**-k*step;qq=np.array([min(b,max(a,x))for x,(a,b)in zip(qq,F.bounds)])
            try:gg=model(F,qq,False)
            except(ValueError,np.linalg.LinAlgError):continue
            if np.linalg.norm(gg['g'])<res*(1-1e-5):q=qq;ok=True;break
        if not ok:return None,None,history
    return None,None,history

def run(source,out,steps=1200,seed=None,power=1.,floor=1e-12):
    out=Path(out);out.mkdir(parents=True,exist_ok=False);X=np.load(source);assert len(X)<=84 and power>=1
    r=np.linalg.norm(X,axis=1);X=X*r[:,None]**(power-1);F=Generator(X,seed,False,floor);q=F.q.copy();(out/'definition.json').write_text(json.dumps(dict(source=str(Path(source).resolve()),seed=seed,radial_power=power,cost_floor=floor,parent=F.parent.tolist(),order=F.order,base_direction=F.base_direction.tolist(),tangent1=F.tangent1.tolist(),tangent2=F.tangent2.tolist(),source_ids=F.source_ids,rotation=F.rotation.tolist(),source_scale=F.scale,physical_definition='uniform filled convex hull of generated primal points; no base plane constraint; full physical own centroid solved',maximum_E=246),indent=2));np.save(out/'initial_parameters.npy',q)
    q,g,hist=restore(F,q,250);(out/'initial_mass_restoration.json').write_text(json.dumps(hist))
    if q is None:print('UNRESTRICTED_SHADOW_INITIAL_FAILURE',out,hist[-1],len(hist),flush=True);return None
    trace=[];trust=.004;start=time.time()
    for it in range(steps):
        g=model(F,q);cl=census(g);assert cl['U']==1;v,J,features=bars(g);value=float(max(v,default=0.));row=dict(it=it,Qmax=value,positive_Q=len(v),trust=trust,seconds=time.time()-start,**cl);trace.append(row);np.save(out/'latest.npy',g['X']);np.save(out/'latest_parameters.npy',q);(out/'latest.json').write_text(json.dumps(row,indent=2));(out/'trace.json').write_text(json.dumps(trace,indent=2))
        if it%10==0:print('UNRESTRICTED_SHADOW_GOAL',out,row,flush=True)
        if cl['S']==1:preserve(g['X'],out/f'exact_goal_{it:05d}','fully free primal shadow body at own uniform centroid; <=84 literal inputs')
        d=F.d;m=len(v);I=eye(d);O=csr_matrix((d,1));A=vstack((hstack((csr_matrix(J),-np.ones((m,1)),csr_matrix((m,d)))),hstack((I,O,-I)),hstack((-I,O,-I))),format='csr');b=np.r_[-v,np.zeros(2*d)];eq=hstack((csr_matrix(g['Jg']),csr_matrix((3,d+1))));bd=[(max(a-x,-trust),min(b-x,trust))for x,(a,b)in zip(q,F.bounds)]+[(0,None)]*(d+1);lp=linprog(np.r_[np.zeros(d),1.,np.full(d,1e-8)],A_ub=A,b_ub=b,A_eq=eq,b_eq=-g['g'],bounds=bd,method='highs',options=dict(primal_feasibility_tolerance=1e-10,dual_feasibility_tolerance=1e-10,time_limit=15.));ok=False
        if lp.success:
            for k in range(17):
                qq=q+2.**-k*lp.x[:d];qq=np.array([min(b,max(a,x))for x,(a,b)in zip(qq,F.bounds)])
                try:qq,gg,hh=restore(F,qq)
                except(ValueError,np.linalg.LinAlgError):continue
                if qq is None:continue
                cc=census(gg)
                if cc['U']!=1:continue
                if cc['S']==1:preserve(gg['X'],out/f'exact_goal_{it:05d}_line{k}','fully free actual-centroid positive-shadow trial numerical110')
                vv=bars(gg,False)[0];val=float(max(vv,default=0.))
                if val<value-max(1e-13,value*1e-8):q=qq;ok=True;row['alpha']=2.**-k;break
        else:row['lp_error']=lp.message
        if ok:
            if k==0:trust=min(.04,trust*1.4)
            elif k>5:trust*=.7
        else:trust*=.4
        if trust<1e-10:break
    np.save(out/'endpoint.npy',model(F,q,False)['X']);np.save(out/'endpoint_parameters.npy',q);print('UNRESTRICTED_SHADOW_FINITE_STOP',out,trace[-1],flush=True);return out/'endpoint.npy'

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('source');p.add_argument('out');p.add_argument('--steps',type=int,default=1200);p.add_argument('--seed',type=int);p.add_argument('--power',type=float,default=1.);p.add_argument('--cost-floor',type=float,default=1e-12);a=p.parse_args();run(a.source,a.out,a.steps,a.seed,a.power,a.cost_floor)
