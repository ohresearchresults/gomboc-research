"""Physical support-coordinate continuation, with true homogeneous mass.

This independently derived chart follows the journal's free-normal/root-plane
idea. It never treats the centroid of the support hull as physical mass.
"""
import argparse,json,time
from fractions import Fraction
from pathlib import Path
import numpy as np
from scipy.optimize import linprog
from scipy.spatial import ConvexHull,QhullError
from geometry import baseline,census,escape_table,mass,write_json
from differential import mass_gradient,persistence_gradient


def physical(q):
    hull=ConvexHull(q);assert max(hull.equations[:,3])<0
    vertices=hull.equations[:,:3]/(-hull.equations[:,3,None])
    keep=[];triangles=[]
    for i,p in enumerate(vertices):
        if not any(np.linalg.norm(p-v)<1e-9 for v in keep):
            keep.append(p);triangles.append(hull.simplices[i])
    return np.array(keep),np.array(triangles)


def evaluate(q,derivative=False,roundness_min=0.,max_stable=0,target='stable'):
    p,triples=physical(q);r=census(p,True);g=np.array(r['centroid'])
    x=p-g;rs=np.einsum('ij,ij->i',x,x);root=int(np.argmax(rs));radius2=rs[root]
    s=1-q@g;assert min(s)>0;ownq=q/s[:,None]
    b,gb=persistence_gradient(ownq);score=b/radius2
    table=escape_table(x);w=table.argmax(axis=1)
    protect=[i for i in range(len(p)) if i!=root]
    cos=table[protect,w[protect]];values=list(cos)
    st=escape_table(ownq);sw=st.argmax(axis=1)
    qs=np.einsum('ij,ij->i',ownq,ownq);qroot=int(np.argmax(qs));qscale=qs[qroot]
    qprotect=[i for i in range(len(q)) if i!=qroot]
    qcos=st[qprotect,sw[qprotect]]
    if target=='unstable':
        b,gx=persistence_gradient(x);score=b/qscale;values=list(qcos)
    ratio=1/np.sqrt(radius2*max(np.einsum('ij,ij->i',ownq,ownq)))
    info=dict(score=float(score),ratio=float(ratio),points=p.tolist(),supports=q.tolist(),
              census={k:v for k,v in r.items() if k not in ['x','q','hull','ut','st','groups']},
              minimum_primal_exit=float(min(cos)),root=root)
    info['minimum_protected_exit']=float(min(cos) if target=='stable' else min(qcos))
    if not derivative:
        return info
    dq=len(q)*3
    jp=np.zeros((len(p),3,dq))
    for v,ids in enumerate(triples):
        if np.linalg.norm(p[v]-[0,0,1])<1e-8:
            continue
        inverse=np.linalg.inv(q[ids])
        for k,f in enumerate(ids):
            jp[v,:,3*f:3*f+3]=-np.outer(inverse[:,k],p[v])
    cg,dv=mass_gradient(p,r)
    jg=np.einsum('avc,vcd->ad',cg,jp)
    jx=jp-jg[None,:,:]
    jq=np.einsum('fa,fb,bd->fad',q,q,jg)/(s*s)[:,None,None]
    for f in range(len(q)):
        jq[f,:,3*f:3*f+3]+=np.eye(3)/s[f]+np.outer(q[f],g)/s[f]**2
    drs=2*x[root]@jx[root]
    grad=np.einsum('fa,fad->d',gb,jq)/radius2-b*drs/radius2**2
    if target=='unstable':
        grad=np.einsum('va,vad->d',gx,jx)/qscale-b*(2*ownq[qroot]@jq[qroot])/qscale**2
    jac=[]
    for i in protect:
        j=w[i];z=x[i];e=p[j]-p[i];rz=np.linalg.norm(z);re=np.linalg.norm(e)
        c=table[i,j];gz=e/(rz*re)-c*z/rz**2;ge=z/(rz*re)-c*e/re**2
        jac.append(gz@jx[i]+ge@(jp[j]-jp[i]))
    if target=='unstable':
        primal_jac=jac;jac=[]
        for i in qprotect:
            j=sw[i];c=st[i,j];z=ownq[i];e=ownq[j]-z;rz=np.linalg.norm(z);re=np.linalg.norm(e)
            gz=e/(rz*re)-c*z/rz**2;ge=z/(rz*re)-c*e/re**2
            jac.append(gz@jq[i]+ge@(jq[j]-jq[i]))
        if max_stable:
            for value,row in zip(cos,primal_jac):
                if value>1e-9:
                    values.append(value);jac.append(row)
    if max_stable and target=='stable':
        for i,j in enumerate(sw):
            c=st[i,j]
            if c<=1e-9:
                continue
            z=ownq[i];e=ownq[j]-z;rz=np.linalg.norm(z);re=np.linalg.norm(e)
            gz=e/(rz*re)-c*z/rz**2;ge=z/(rz*re)-c*e/re**2
            values.append(c);jac.append(gz@jq[i]+ge@(jq[j]-jq[i]))
    if roundness_min:
        f=int(np.argmax(np.einsum('ij,ij->i',ownq,ownq)));qs=ownq[f]@ownq[f]
        dratio=-.5*ratio*(drs/radius2+(2*ownq[f]@jq[f])/qs)
        values.append(ratio-roundness_min);jac.append(dratio)
    return info,grad,np.array(values),np.array(jac)


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--out',required=True)
    ap.add_argument('--input');ap.add_argument('--root',type=int,default=14)
    ap.add_argument('--steps',type=int,default=400);ap.add_argument('--seed',type=int,default=961)
    ap.add_argument('--margin',type=float,default=1e-7)
    ap.add_argument('--roundness-min',type=float,default=0.)
    ap.add_argument('--max-stable',type=int,default=2)
    ap.add_argument('--target',choices=['stable','unstable'],default='stable')
    ap.add_argument('--condition-budget',type=float,default=0.)
    ap.add_argument('--condition-target',type=float,default=.001)
    ap.add_argument('--check-gradient',action='store_true')
    args=ap.parse_args();out=Path(args.out);out.mkdir(exist_ok=False)
    data=None if args.input is None else json.loads(Path(args.input).read_text())
    if data is not None and 'supports' in data:
        q=np.array(data['supports'],float);rootfaces=np.flatnonzero(abs(q[:,2]-1)<1e-9)
    else:
        p=baseline() if data is None else np.array([[float(Fraction(x)) for x in row] for row in data.get('points',data.get('raw_vertices'))])
        p-=mass(p)[1]
        if args.root<0:
            args.root=int(np.argmax(np.linalg.norm(p,axis=1)))
        u=p[args.root].copy();p/=np.linalg.norm(u);u/=np.linalg.norm(u)
        ex=np.cross(u,[1.,0,0])
        if np.linalg.norm(ex)<.1:
            ex=np.cross(u,[0.,1,0])
        ex/=np.linalg.norm(ex);ey=np.cross(u,ex);p=p@np.array([ex,ey,u]).T
        r=census(p,True);q=r['q'];rootfaces=np.flatnonzero(abs(q[:,2]-1)<1e-8)
        q[rootfaces,2]=1.
        perturb=np.random.default_rng(args.seed).normal(size=q.shape);perturb[rootfaces,2]=0.
        attempts=[];accepted=False
        for amplitude in [1e-3,1e-4,1e-5,1e-6,1e-7,1e-8,1e-9]:
            trial=q+amplitude*perturb
            info=evaluate(trial,target=args.target);c=info['census'];attempts.append(dict(amplitude=amplitude,census=c))
            good=(c['U']==1 and (not args.max_stable or c['S']<=args.max_stable)) if args.target=='stable' else(c['S']==1 and c['U']<=2)
            if good and c['U_uncertain']==c['S_uncertain']==0:
                q=trial;accepted=True;break
        write_json(out/'OPENING.json',dict(attempts=attempts,accepted=accepted,root_faces=rootfaces.tolist()))
        if not accepted:
            return
    initial=evaluate(q,target=args.target);write_json(out/'INITIAL.json',initial)
    history=[];start=time.time();trust=.02
    primal_floor=min(args.margin,.5*initial['minimum_protected_exit'])
    barrier_ceiling=initial['score']+args.condition_budget
    if args.check_gradient:
        info,grad,values,jac=evaluate(q,True,args.roundness_min,args.max_stable,args.target)
        rng=np.random.default_rng(20260916);rows=[]
        for k in range(8):
            direction=rng.normal(size=q.shape);direction[rootfaces,2]=0;direction/=np.linalg.norm(direction)
            eps=1e-8
            a=evaluate(q+eps*direction,target=args.target)['score'];b=evaluate(q-eps*direction,target=args.target)['score']
            rows.append(dict(predicted=float(grad@direction.ravel()),observed=float((a-b)/(2*eps))))
        write_json(out/'DERIVATIVE.json',rows);print('SUPPORT_DERIVATIVE',rows,flush=True)
    scales=np.repeat(np.maximum(np.linalg.norm(q,axis=1),1.),3)
    for step in range(args.steps):
        info,grad,values,jac=evaluate(q,True,args.roundness_min,args.max_stable,args.target)
        reserve=np.minimum(args.margin,.1*np.maximum(values,0.))
        primal_count=(len(info['points']) if args.target=='stable' else len(q))-1
        reserve[:primal_count]=primal_floor
        if args.max_stable:
            reserve[primal_count:]=np.maximum(reserve[primal_count:],1.1e-9)
        if args.roundness_min:
            reserve[-1]=0.
        bounds=[(-trust,trust)]*q.size
        for f in rootfaces:
            bounds[3*f+2]=(0.,0.)
        for f in set(range(len(q)))-set(rootfaces):
            bounds[3*f+2]=(-trust,min(trust,(1-q[f,2])/scales[3*f+2]))
        if args.condition_budget:
            count=primal_count
            arb=np.c_[-jac*scales[None,:],np.r_[np.ones(count),np.zeros(len(values)-count)]]
            arb=np.r_[arb,np.r_[grad*scales,0.][None,:]]
            rhs=np.r_[values-np.r_[np.zeros(count),reserve[count:]],barrier_ceiling-info['score']]
            cost=np.r_[np.zeros(q.size),-1.]
            lp=linprog(cost,A_ub=arb,b_ub=rhs,bounds=bounds+[(0.,args.condition_target)],
                       method='highs',options={'threads':1,'primal_feasibility_tolerance':1e-9})
            descent=lp.success and lp.x[-1]>info['minimum_protected_exit']+1e-12
        else:
            lp=linprog(grad*scales,A_ub=-jac*scales[None,:],b_ub=values-reserve,
                       bounds=bounds,method='highs',options={'threads':1,'primal_feasibility_tolerance':1e-9})
            descent=lp.success and lp.fun < -1e-12
        if not descent:
            history.append(dict(step=step,stopped=lp.message));break
        delta=(lp.x[:q.size]*scales).reshape(q.shape);accepted=False;trials=[]
        for alpha in [1.,.5,.25,.125,.0625,.03125,.015625,.0078125]:
            try:
                trial=q+alpha*delta;rr=evaluate(trial,target=args.target);cc=rr['census']
                trials.append(dict(alpha=alpha,score=rr['score'],S=cc['S'],U=cc['U'],ratio=rr['ratio'],
                                   minimum_primal_exit=rr['minimum_primal_exit'],S_uncertain=cc['S_uncertain'],
                                   minimum_protected_exit=rr['minimum_protected_exit'],
                                   U_uncertain=cc['U_uncertain'],maximum_root_contact=float(max(trial[:,2]))))
                stable=(not args.max_stable)or(cc['S']<=args.max_stable and cc['S_uncertain']==0)
                census_ok=cc['U']==1 and cc['U_uncertain']==0 and stable
                if args.target=='unstable':
                    census_ok=cc['S']==1 and cc['U']<=2 and cc['U_uncertain']==cc['S_uncertain']==0
                improvement=(rr['score']<info['score']-1e-10)
                if args.condition_budget:
                    improvement=rr['score']<=barrier_ceiling and rr['minimum_protected_exit']>info['minimum_protected_exit']+1e-12
                if improvement and rr['minimum_protected_exit']>=primal_floor and census_ok and rr['ratio']>=args.roundness_min and max(trial[:,2])<=1+1e-10:
                    q=trial;accepted=True;break
            except (QhullError,AssertionError,np.linalg.LinAlgError):
                continue
        if accepted:
            trust=min(.05,trust*(1.15 if alpha>=.5 else .8));rr.update(step=step,trust=trust)
            write_json(out/'BEST.json',rr);history.append({k:v for k,v in rr.items() if k not in ['points','supports']})
            if step%10==0:
                print('SUPPORT_ACCEPT',step,rr['score'],cc['S'],cc['U'],cc['E_proposal'],rr['ratio'],flush=True)
            if cc['S']==cc['U']==1 and cc['S_uncertain']==cc['U_uncertain']==0:
                write_json(out/'PROPOSAL110.json',rr);break
            if args.condition_budget and rr['minimum_protected_exit']>=.99*args.condition_target:
                break
        else:
            trust*=.35;history.append(dict(step=step,accepted=False,trust=trust,trials=trials))
            if trust<1e-9:
                break
        write_json(out/'SEARCH.json',dict(config=vars(args),history=history,elapsed=time.time()-start))
    write_json(out/'SEARCH.json',dict(config=vars(args),history=history,elapsed=time.time()-start))
    print('SUPPORT_FLOW_FINISHED',len(history),time.time()-start,flush=True)


if __name__=='__main__':
    main()
