"""Positive-shadow primal shapes with canonical physical projective centering.

Every evaluation solves only a strictly definite 3x3 centroid equation. The
implicit derivative includes actual solid second moments. Physical U1 after
this nonlinear map is checked separately, never inherited from the preimage.
The <=84 literal physical points give an unconditional E<=246 bound.
"""
import argparse,json,time
from pathlib import Path
import numpy as np
from scipy.optimize import linprog
from scipy.sparse import csr_matrix,eye,hstack,vstack
from canonical_projective_mass import normalize
from dual_shadow_goal import Generator,bars as pbars
from shadow_mass_retracted_goal import bars as qbars
from unrestricted_shadow_goal import census
from support_geometry import escape
from goal_nomination import preserve

def model(F,q,derivative=True):
    X,DX=F.construct(q);g,p,h=normalize(X,DX if derivative else None);g['normalization_p']=p;g['preimage']=X
    if derivative:
        B=g['parameter_DX'].reshape(X.size,F.d);g['JH']=g['DH']@B;g['JZ']=g['DZ']@B
    owners=set()
    for tri in g['T']:
        for i,j in zip(tri,np.roll(tri,-1)):owners.add(tuple(sorted((int(i),int(j)))))
    g['edges']=np.array(list(owners));return g

def run(source,out,steps=1000,seed=None,power=1.,floor=1e-12,mode='hard'):
    out=Path(out);out.mkdir(parents=True,exist_ok=False);X=np.load(source);r=np.linalg.norm(X,axis=1);X=X*(r/max(r))[:,None]**(power-1);F=Generator(X,seed,False,floor);q=F.q.copy();g=model(F,q);cl=census(g)
    if mode=='hard'and cl['U']!=1:raise ValueError('hard physicalU1 mode requires actual normalized physicalU1 initial census')
    definition=dict(source=str(Path(source).resolve()),seed=seed,radial_power=power,cost_floor=floor,mode=mode,parent=F.parent.tolist(),order=F.order,base_direction=F.base_direction.tolist(),tangent1=F.tangent1.tolist(),tangent2=F.tangent2.tolist(),source_ids=F.source_ids,rotation=F.rotation.tolist(),source_scale=F.scale,physical_definition='primal positive-shadow point coordinates then y=x/(1+p.x), with p solving the actual solid centroid; actual census re-evaluated after the map',maximum_E=246)
    (out/'definition.json').write_text(json.dumps(definition,indent=2));trace=[];trust=.003;start=time.time()
    for it in range(steps):
        g=model(F,q);cl=census(g);Q,JQ,_=qbars(g);P,JP=pbars(g);Qmax=float(max(Q,default=0.));Pmax=float(max(P,default=0.));merit=Qmax+(Pmax if mode=='joint'else 0.);row=dict(it=it,Qmax=Qmax,Pmax=Pmax,positive_Q=len(Q),positive_P=len(P),merit=merit,trust=trust,seconds=time.time()-start,**cl);trace.append(row);np.save(out/'latest.npy',g['X']);np.save(out/'latest_parameters.npy',q);np.save(out/'latest_projective_p.npy',g['normalization_p']);(out/'latest.json').write_text(json.dumps(row,indent=2));(out/'trace.json').write_text(json.dumps(trace,indent=2))
        if it%10==0:print('PROJECTIVE_MASS_SHADOW',out,row,flush=True)
        if cl['U']==1 and(cl['S']==1 or Qmax<1e-10):preserve(g['X'],out/f'exact_goal_{it:05d}','canonical projectively centered positive-shadow nomination; small Q is only an audit trigger, never a discarded positive bar; exact maximal-facet/weak census required')
        if mode=='hard':assert cl['U']==1
        d=F.d;ns=2 if mode=='joint'else 1;I=eye(d);O=csr_matrix((d,ns));blocks=[];rhs=[]
        for k,(v,J)in enumerate([(Q,JQ)]+([(P,JP)]if mode=='joint'else [])):
            if not len(v):continue
            sl=np.zeros((len(v),ns));sl[:,k]=-1;blocks.append(hstack((csr_matrix(J),sl,csr_matrix((len(v),d)))));rhs.append(-v)
        if mode=='hard':
            ids=g['vertices'];A=g['Z'][ids];uv,_,JU=escape(A,g['JZ'][ids],angular=False);root=np.argmax(np.sum(A*A,axis=1));mask=np.arange(len(A))!=root;eps=min(1e-10,float(min(uv[mask]))*.05);blocks.append(hstack((-csr_matrix(JU[mask]),csr_matrix((sum(mask),ns+d)))));rhs.append(uv[mask]-eps)
        blocks.extend((hstack((I,O,-I)),hstack((-I,O,-I))));rhs.append(np.zeros(2*d));bounds=[(max(a-x,-trust),min(b-x,trust))for x,(a,b)in zip(q,F.bounds)]+[(0,None)]*(ns+d);lp=linprog(np.r_[np.zeros(d),np.ones(ns),np.full(d,1e-8)],A_ub=vstack(blocks,format='csr'),b_ub=np.concatenate(rhs),bounds=bounds,method='highs',options=dict(primal_feasibility_tolerance=1e-10,dual_feasibility_tolerance=1e-10,time_limit=15.));ok=False
        if lp.success:
            for k in range(18):
                qq=q+2.**-k*lp.x[:d];qq=np.array([min(b,max(a,x))for x,(a,b)in zip(qq,F.bounds)])
                try:gg=model(F,qq,False);cc=census(gg)
                except(ValueError,np.linalg.LinAlgError):continue
                if mode=='hard'and cc['U']!=1:continue
                qv=qbars(gg,False)[0];pv=pbars(gg,False)[0];mm=float(max(qv,default=0.))+(float(max(pv,default=0.))if mode=='joint'else 0.)
                if cc['U']==1 and(cc['S']==1 or max(qv,default=0.)<1e-10):preserve(gg['X'],out/f'exact_goal_{it:05d}_line{k}','actual normalized homogeneous trial equilibrium nomination; complete exact hull census decides strict110 and weak000')
                if mm<merit-max(1e-13,merit*1e-8):q=qq;ok=True;row['alpha']=2.**-k;break
        else:row['lp_error']=lp.message
        if ok:
            if k==0:trust=min(.04,trust*1.35)
            elif k>6:trust*=.7
        else:trust*=.4
        if trust<1e-10:break
    gg=model(F,q,False);np.save(out/'endpoint.npy',gg['X']);np.save(out/'endpoint_parameters.npy',q);np.save(out/'endpoint_projective_p.npy',gg['normalization_p']);print('PROJECTIVE_MASS_SHADOW_FINITE_STOP',out,trace[-1],flush=True);return out/'endpoint.npy'

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('source');p.add_argument('out');p.add_argument('--steps',type=int,default=1000);p.add_argument('--seed',type=int);p.add_argument('--power',type=float,default=1.);p.add_argument('--cost-floor',type=float,default=1e-12);p.add_argument('--mode',choices=['hard','joint'],default='hard');a=p.parse_args();run(a.source,a.out,a.steps,a.seed,a.power,a.cost_floor,a.mode)
