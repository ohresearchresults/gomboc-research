"""Move positive escape subtrees from the junior stable basin to the elder.

All vectors come from the same physical H-body at its uniform volume centroid.
Cross-basin targets are selected outside the complete positive-reachability set
of the junior-only region. A new witness is never aimed into a preserved return
cycle. Numerical own110 outputs still require exact physical verification.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import argparse,json,pathlib,time
import numpy as np
import torch
from scipy.linalg import svd
from scipy.optimize import linprog,minimize,LinearConstraint,Bounds
from geometry import halfspace_mesh,arrows,census
from soft_forest_polish import forest,run as polish
from basin_scout import score
from bottleneck_capacity import capacities
torch.set_num_threads(1);torch.set_default_dtype(torch.float64)

def reachability(A,root,eps=0):
    W=arrows(A);reach=np.zeros(len(A),bool);reach[root]=True
    while True:
        new=reach|(W[:,reach]>eps).any(1)
        if np.array_equal(new,reach):return reach
        reach=new

def state(Q,elder=None):
    m=halfspace_mesh(Q);P=m['X']-m['g'];R=Q/(1-Q@m['g'])[:,None];wp=arrows(P);wq=arrows(R)
    U=np.flatnonzero(wp.max(1)<0);S=np.flatnonzero(wq.max(1)<0)
    if elder is None:elder=int(np.argmax((R*R).sum(1)))
    return dict(Q=Q,m=m,P=P,R=R,wp=wp,wq=wq,U=U,S=S,elder=elder,reach=reachability(R,elder),census=census(m,0))

def margins(e,committed):
    p=e['wp'].max(1);q=e['wq'].max(1)
    p[e['U']]*=-1;q[e['S']]*=-1
    cap,_,_,_=capacities(e['R'],[e['elder']])
    return min(float(p.min()),float(q.min()),float(cap[committed].min()))

def derivatives(e,target):
    Q=e['Q'];m=e['m'];P=e['P'];R=e['R'];elder=e['elder'];u,v=target
    if len(e['U'])!=1 or len(e['S'])!=2:raise ValueError('transfer requires a strict own211 body')
    junior=next(int(k) for k in e['S'] if k!=elder)
    pp=forest(P,e['U'].tolist());sp=np.ones(len(P));sp[e['U']]=-1
    pe=forest(R,[elder]);pj=forest(R,[junior]);pq=np.where(e['reach'],pe,pj);sq=np.ones(len(Q));sq[e['S']]=-1
    ip=np.arange(len(P));iq=np.arange(len(Q));keep=iq!=junior if u==junior else np.ones(len(Q),bool)
    # Retain every old positive arrow while opening the extra cross-component
    # arrow. Only the unwanted root's own negative guard is released when it
    # is itself the transfer source.
    tt=torch.tensor(m['triangles']);ti=torch.tensor(m['triples']);pp=torch.tensor(pp);pq=torch.tensor(pq);sp=torch.tensor(sp);sq=torch.tensor(sq);keep=torch.tensor(keep)
    def calc(z):
        q=z.reshape(Q.shape);x=torch.linalg.solve(q[ti],torch.ones((len(ti),3,1)))[:,:,0]
        a=x[tt];vol=(a[:,0]*torch.linalg.cross(a[:,1],a[:,2])).sum(1)/6;g=(vol[:,None]*a.sum(1)).sum(0)/(4*vol.sum());p=x-g;r=q/(1-q@g)[:,None]
        def esc(a,parents):
            dd=a[parents]-a
            return (a*dd).sum(1)/(torch.linalg.vector_norm(a,dim=1)*torch.linalg.vector_norm(dd,dim=1))
        dd=r[v]-r[u];cross=(r[u]*dd).sum()/(torch.linalg.vector_norm(r[u])*torch.linalg.vector_norm(dd))
        return torch.cat([sp*esc(p,pp),(sq*esc(r,pq))[keep],cross[None],x.flatten(),q.flatten()])
    zz=torch.tensor(Q.ravel());vals=calc(zz).detach().numpy();J=torch.func.jacrev(calc)(zz).detach().numpy();ng=len(P)+int(keep.sum());metric=J[ng+1:].copy();metric[:m['X'].size]/=np.sqrt(np.mean(P**2));metric[m['X'].size:]/=np.sqrt(np.mean(Q**2));_,dd,Vt=svd(metric,full_matrices=False,check_finite=False);W=Vt.T/dd
    return vals[:ng],J[:ng],float(vals[ng]),J[ng],W

def transfer(Q,elder,target,committed,out,steps=100):
    out=pathlib.Path(out);out.mkdir(parents=True,exist_ok=True);trust=.03;history=[];start=time.time();u,v=target
    for it in range(steps):
        e=state(Q,elder)
        if len(e['S'])==len(e['U'])==1:
            np.savez(out/'POTENTIAL_OWN110.npz',Q=Q);return Q,True
        guards,J,objective,Dobj,W=derivatives(e,target)
        row=dict(it=it,target=list(map(int,target)),angular_target=objective,elder_reachable=int(e['reach'].sum()),S=len(e['S']),U=len(e['U']),E=len(e['m']['edges']),minimum=float(guards.min()),trust=trust,seconds=time.time()-start)
        history.append(row);(out/'history.json').write_text(json.dumps(history,indent=2));np.savez(out/'latest.npz',Q=Q)
        if it%5==0:print('BASIN_TRANSFER',json.dumps(row),flush=True)
        if e['reach'][u] and objective>1e-8 and e['reach'][committed].all():
            np.savez(out/'NOMINATION_TRANSFER.npz',Q=Q);return Q,True
        d=Q.size;A=J@W;gg=Dobj@W;floor=np.full_like(guards,1e-7);bound=trust/np.sqrt(d)
        lp=linprog(-gg,A_ub=-A,b_ub=guards-floor,bounds=[(-bound,bound)]*d,method='highs',options={'primal_feasibility_tolerance':1e-9,'dual_feasibility_tolerance':1e-9})
        if not lp.success or gg@lp.x<1e-10:
            trust*=.5
            if trust<1e-8:break
            continue
        desired=.75*(gg@lp.x)
        qp=minimize(lambda x:(.5*x@x,x),lp.x*.75,jac=True,method='SLSQP',bounds=Bounds(-bound,bound),constraints=[LinearConstraint(A,floor-guards,np.inf),LinearConstraint(gg,desired,np.inf)],options={'ftol':1e-13,'maxiter':70})
        if min(A@qp.x+guards-floor)<-1e-8 or gg@qp.x<desired-1e-8:
            trust*=.5
            if trust<1e-8:break
            continue
        delta=(W@qp.x).reshape(Q.shape);accepted=False
        for level in range(16):
            candidate=Q+delta*2**-level
            try:
                ee=state(candidate,elder)
                if level<2 and (len(ee['S'])!=2 or len(ee['U'])!=1 or margins(ee,committed)<8e-8):
                    folder=out/f'correct{it:04d}-{level}'
                    candidate=polish(candidate,folder,nP=1,nQ=2,steps=18)
                    ee=state(candidate,elder)
            except (ValueError,RuntimeError,np.linalg.LinAlgError):continue
            if not 17<=len(ee['m']['edges'])<250:continue
            if len(ee['S'])==len(ee['U'])==1:
                np.savez(out/'POTENTIAL_OWN110.npz',Q=candidate);return candidate,True
            if len(ee['S'])==2 and len(ee['U'])==1 and elder in ee['S'] and margins(ee,committed)>8e-8 and ee['wq'][u,v]>objective+1e-9:
                Q=candidate;accepted=True;break
        if accepted and level==0:trust=min(.3,trust*1.25)
        if not accepted:trust*=.4
        if trust<1e-8:break
    return Q,False

def run(input,out,stages=30,steps=90):
    out=pathlib.Path(out);out.mkdir(parents=True,exist_ok=True);Q=np.load(input)['Q'];e=state(Q);elder=e['elder'];history=[];start=time.time()
    np.savez(out/'initial.npz',Q=Q)
    for stage in range(stages):
        e=state(Q,elder)
        if len(e['S'])==len(e['U'])==1:
            np.savez(out/'POTENTIAL_OWN110.npz',Q=Q);return
        committed=np.flatnonzero(e['reach']);junior=next(int(k) for k in e['S'] if k!=elder);I=np.array([i for i in e['m']['active'] if not e['reach'][i]]);J=np.array([j for j in e['m']['active'] if e['reach'][j]])
        ww=e['wq'][np.ix_(I,J)];flat=np.argsort(-ww.ravel());chosen=[];used=set()
        for ij in flat:
            a,b=np.unravel_index(ij,ww.shape);u,v=int(I[a]),int(J[b])
            if u in used:continue
            chosen.append((u,v));used.add(u)
            if len(chosen)==5:break
        chosen.append((junior,int(J[np.argmax(e['wq'][junior,J])])))
        accepted=False
        for attempt,target in enumerate(chosen):
            folder=out/f'stage{stage:03d}-attempt{attempt:02d}'
            try:q,ok=transfer(Q,elder,target,committed,folder,steps)
            except (ValueError,RuntimeError,np.linalg.LinAlgError) as err:
                folder.mkdir(parents=True,exist_ok=True);(folder/'error.txt').write_text(repr(err));continue
            ee=state(q,elder);row=dict(stage=stage,attempt=attempt,target=list(target),accepted=ok,reachable_before=len(committed),reachable_after=int(ee['reach'].sum()),seconds=time.time()-start,**score(q));history.append(row);(out/'history.json').write_text(json.dumps(history,indent=2))
            if ok and len(ee['S'])==len(ee['U'])==1:
                np.savez(out/'POTENTIAL_OWN110.npz',Q=q);print('POTENTIAL_COMPLETE_OWN110_REQUIRES_EXACT',flush=True);return
            if ok and ee['reach'].sum()>len(committed):
                Q=q;accepted=True;np.savez(out/'latest-transfer.npz',Q=Q);print('TRANSFER_ACCEPTED',stage,target,len(committed),int(ee['reach'].sum()),flush=True);break
        if not accepted:
            print('NO_ACCEPTED_BASIN_TRANSFER_IN_FINITE_SCOUT',stage,flush=True);break

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--input',required=True);ap.add_argument('--out',required=True);ap.add_argument('--stages',type=int,default=30);ap.add_argument('--steps',type=int,default=90);a=ap.parse_args();run(a.input,a.out,a.stages,a.steps)
