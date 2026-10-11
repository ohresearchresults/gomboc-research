"""Polar positive-escape chart and homogeneous mass closure, with <=2U guards.
The younger primal root is deliberately allowed to disappear. All other current
primal vertices receive strictly positive rooted escape witnesses. Fresh hull
and full own census gate each finite accepted step.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import numpy as np,pathlib,json,time,argparse
from scipy.optimize import linprog,minimize,LinearConstraint,Bounds
from dual_thales import Chart,evaluate,conditioner,project_mass
from soft_forest_polish import forest
from geometry import halfspace_mesh,census,arrows
from persistence_search import pairs

def primal_guards(ev):
    A=ev['X']-ev['g'];DA=ev['DX']-ev['Dg'];aa=(A*A).sum(1);pp,hh=pairs(A,ev['mesh']['edges']);roots=[int(aa.argmax())]
    if len(pp):roots.append(int(pp[np.argmax(1-hh[pp[:,1]]/aa[pp[:,0]]),0]))
    pa=forest(A,roots);i=np.array([i for i in range(len(A)) if i not in roots],int);j=pa[i];a=A[i];d=A[j]-a;rr=(a*a).sum(1);dd=(d*d).sum(1);den=np.sqrt(rr*dd);val=(a*d).sum(1)/den;gi=(d-a)/den[:,None]-val[:,None]*(a/rr[:,None]-d/dd[:,None]);gj=a/den[:,None]-val[:,None]*d/dd[:,None];J=np.einsum('ic,icp->ip',gi,DA[i])+np.einsum('ic,icp->ip',gj,DA[j]);return val,J,roots

def run(input,out,steps=700,eta=.01,epsilon=1e-8):
    Q=np.load(input)['Q'];m=halfspace_mesh(Q);Q=Q/(1-Q@m['g'])[:,None];Q/=np.max(np.linalg.norm(Q,axis=1));out=pathlib.Path(out);out.mkdir(parents=True,exist_ok=True);chart=Chart(Q);z=chart.z0.copy();trust=.015;history=[];start=time.time()
    for it in range(steps):
        ev=evaluate(chart,z,eta);st=census(ev['mesh']);v,J,roots=primal_guards(ev);row=dict(it=it,loss=ev['loss'],Pmax=max(ev['P'],default=0),minimum_primal_guard=float(min(v)),mass_norm=float(np.linalg.norm(ev['g'])),seconds=time.time()-start,trust=trust,**st);history.append(row);(out/'history.json').write_text(json.dumps(history,indent=2));np.savez(out/'latest.npz',Q=ev['Q']);print('GUARDED_DUAL',json.dumps({k:row[k] for k in ['it','Pmax','S','U','E','minimum_primal_guard','mass_norm','trust','seconds']}),flush=True)
        if st['S']==st['U']==1 and st['min_primal_nonroot']>1e-12 and st['min_polar_nonroot']>1e-12 and 17<=st['E']<250:
            np.savez(out/'NOMINATION_OWN110.npz',Q=ev['Q']);print('POTENTIAL_OWN110_REQUIRES_EXACT',flush=True);return
        if st['S']!=1 or st['U']>2:raise ValueError('guarded method needs actual ownS1 and atmost2U')
        W,sx=conditioner(ev);d=len(z);grad=ev['gradient']@W;mass=ev['Dg']@W/sx;rad=np.arange(2,d,3);A=np.vstack([-ev['DI']@W,-J@W,1e3*W[rad],-W[rad]]);b=np.r_[ev['ine']*.8,v-epsilon,1e3*(-1e-10-z[rad]),z[rad]+25];bound=trust/np.sqrt(d)
        lp=linprog(grad,A_ub=A,b_ub=b,A_eq=mass,b_eq=-ev['g']/sx,bounds=[(-bound,bound)]*d,method='highs',options={'primal_feasibility_tolerance':1e-9,'dual_feasibility_tolerance':1e-9})
        if not lp.success:trust*=.5;print('GUARDED_LP_UNRESOLVED',lp.message,flush=True);continue
        theta=trust/max(np.linalg.norm(grad),1e-20);qp=minimize(lambda x:(.5*x@x+theta*(grad@x),x+theta*grad),lp.x,jac=True,method='SLSQP',bounds=Bounds(-bound,bound),constraints=[LinearConstraint(A,-np.inf,b),LinearConstraint(mass,-ev['g']/sx,-ev['g']/sx)],options={'maxiter':120,'ftol':1e-13})
        if np.max(A@qp.x-b)>1e-8 or np.max(abs(mass@qp.x+ev['g']/sx))>1e-9:print('QP_FINITE_RESIDUAL_REJECTED',flush=True);trust*=.4;continue
        dz=W@qp.x;accepted=False
        for level in range(15):
            try:trial,ee=project_mass(chart,z+dz*2**-level,eta);ss=census(ee['mesh']);vv,_,_=primal_guards(ee)
            except (ValueError,np.linalg.LinAlgError):continue
            if ss['S']==1 and ss['U']<=2 and min(vv)>epsilon*.5 and ee['loss']<ev['loss']-1e-11:
                z=trial;accepted=True;break
        if accepted and level==0:trust=min(.08,trust*1.25)
        if not accepted:trust*=.4
        if trust<1e-8:print('GUARDED_DUAL_LOCAL_STALL',flush=True);break
        if accepted and it%20==19:chart=Chart(ee['Q']);z=chart.z0.copy()

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--input',required=True);ap.add_argument('--out',required=True);ap.add_argument('--steps',type=int,default=700);ap.add_argument('--eta',type=float,default=.01);ap.add_argument('--epsilon',type=float,default=1e-8);a=ap.parse_args();run(a.input,a.out,a.steps,a.eta,a.epsilon)
