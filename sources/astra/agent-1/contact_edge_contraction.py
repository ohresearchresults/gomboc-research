"""Contract true edges within an own110 physical contact realization.

The objective is edge length divided by RMS own-centred vertex radius. It cannot
be improved by mere scaling. Complete incidence, actual uniform mass and strict
mechanics are recomputed at every accepted step. Contracted complexes are only
proposals until reconstructed, checked, and eventually audited rationally.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import argparse,json,pathlib,time,itertools
import numpy as np
from scipy.optimize import linprog,minimize,LinearConstraint,Bounds
from contact_forest import ContactModel,correct
from make_contact_atlas import make
from contact_retraction import retract

def normalized(e,edge):
    u,v=edge;P=e['P'];r=np.sqrt(np.mean(np.sum(P*P,axis=1)))
    dr=np.einsum('ic,icp->p',P,e['DP'])/(len(P)*r)
    delta=e['X'][v]-e['X'][u]
    dd=e['DX'][v]-e['DX'][u]
    x=delta/r;J=dd/r-delta[:,None]*dr/r**2
    nv=e['volume']/r**3;DV=e['DV']/r**3-3*e['volume']*dr/r**4
    return x,J,nv,DV

def propose(model,e,edge,out):
    out=pathlib.Path(out);out.mkdir(parents=True,exist_ok=True)
    u,v=map(int,edge);keep=[i for i in range(len(e['X'])) if i!=v];idx={i:k for k,i in enumerate(keep)};idx[v]=idx[u]
    X=e['X'][keep].copy();X[idx[u]]=(e['X'][u]+e['X'][v])/2
    faces=[];oldfaces=[]
    for f,cy in enumerate(model.meta['faces']):
        mapped=[idx[i] for i in cy];new=[x for k,x in enumerate(mapped) if x!=mapped[k-1]]
        if len(new)<3:continue
        if len(set(new))!=len(new):raise ValueError('edge contraction creates pinched polygon')
        faces.append(new);oldfaces.append(f)
    edges=sorted({tuple(sorted((i,j))) for cy in faces for i,j in zip(cy,cy[1:]+cy[:1])})
    if len(X)-len(edges)+len(faces)!=2:raise ValueError('contracted proposal fails Euler sphere identity')
    if len(edges)>=model.meta['E']:raise ValueError('edge contraction did not lower genuine count')
    for edge2 in edges:
        if sum(edge2[0] in cy and edge2[1] in cy for cy in faces)!=2:
            raise ValueError('contracted proposal has nonmanifold adjacency')
    Y=e['Y'][oldfaces]
    proposal=dict(scope='UNVERIFIED contracted physical contact-complex proposal',V=len(X),E=len(edges),F=len(faces),faces=faces,edges=edges,
                  raw_vertices=[[str(a) for a in p] for p in X],raw_halfspaces=[[str(a) for a in q]+['1'] for q in Y],active=list(range(len(Y))),
                  contracted_edge=[u,v],parent_complex=dict(V=len(e['X']),E=model.meta['E'],F=model.F))
    (out/'proposal.json').write_text(json.dumps(proposal,indent=2));make(out/'proposal.json',out/'chart')
    child=ContactModel(out/'chart');ee=child.evaluate(child.initial,False)
    summary=dict(V=len(ee['X']),E=child.meta['E'],F=child.F,S=ee['S'],U=ee['U'],minimum=float(ee['mechanical'].min()),noncontact=ee['minimum_gap'],turn=ee['minimum_turn'])
    (out/'summary.json').write_text(json.dumps(summary,indent=2));np.savez(out/'realization.npz',z=child.initial,X=ee['X'],Q=ee['Y'])
    if ee['S']==ee['U']==1 and ee['mechanical'].min()>1e-10:
        np.savez(out/'NOMINATION_OWN110.npz',z=child.initial,X=ee['X'],Q=ee['Y'])
        print('CONTRACTED_NUMERICAL_OWN110_REQUIRES_EXACT',summary,flush=True)
        return True
    z,ee,ok=correct(child,child.initial,out/'repair',steps=35,eps=1e-9,trust=.003,verbose=False)
    if ok and ee['S']==ee['U']==1 and ee['mechanical'].min()>1e-10:
        np.savez(out/'NOMINATION_OWN110.npz',z=z,X=ee['X'],Q=ee['Y']);return True
    return False

def contract(source,out,edge_index,steps=150,eps=1e-10,use_corrector=False,input=None,merit='direct',physical_retraction=False,keep_shortening=False):
    model=ContactModel(source,merit=merit);z=np.load(input)['z'] if input else model.initial.copy();out=pathlib.Path(out);out.mkdir(parents=True,exist_ok=True)
    edge=model.eu[edge_index];history=[];trust=.03;start=time.time();e=model.evaluate(z)
    if e['S']!=1 or e['U']!=1 or e['mechanical'].min()<=0:raise ValueError('source is not strict own110')
    _,_,vol0,_=normalized(e,edge);floor=.2*vol0
    (out/'source.json').write_text(json.dumps(dict(source=str(pathlib.Path(source).resolve()),edge_index=int(edge_index),edge=edge.tolist(),normalized_volume_floor=float(floor)),indent=2))
    for it in range(steps):
        e=model.evaluate(z);delta,J,nv,DV=normalized(e,edge);length=np.linalg.norm(delta);v=e['mechanical']
        row=dict(it=it,normalized_length=float(length),S=e['S'],U=e['U'],minimum=float(v.min()),minimum_gap=e['minimum_gap'],minimum_turn=e['minimum_turn'],normalized_volume=float(nv),trust=trust,seconds=time.time()-start)
        history.append(row);(out/'history.json').write_text(json.dumps(history,indent=2));np.savez(out/'latest.npz',z=z,X=e['X'],Q=e['Y'])
        if it%5==0:print('EDGE_CONTRACTION',edge_index,json.dumps(row),flush=True)
        if length<2e-5 and (it%5==0 or length<2e-7):
            try:
                if propose(model,e,edge,out/f'contracted{it:04d}'):
                    (out/'accepted_contraction.json').write_text(json.dumps(dict(folder=f'contracted{it:04d}',edge=edge.tolist(),normalized_parent_length=float(length)),indent=2));return True
            except (ValueError,AssertionError,RuntimeError,np.linalg.LinAlgError) as err:
                (out/f'proposal{it:04d}_error.txt').write_text(repr(err))
        W=model.metric(e);d=model.free;A=np.vstack([-e['J']@W,-e['gapJ']@W,-DV@W]);b=np.r_[v-eps,e['gapv']*.8,nv-floor];C=(delta/length)@J@W;C=C[None,:];bound=trust/np.sqrt(d)
        keep=b<=bound*np.abs(A).sum(1)+1e-10
        row['linear_rows_full']=len(b);row['linear_rows_kept']=int(keep.sum());A=A[keep];b=b[keep]
        scale=np.maximum(bound*np.abs(A).sum(1),1e-12);A=A/scale[:,None];b=b/scale
        lp=linprog(np.r_[np.zeros(d),-1],A_ub=np.c_[A,np.zeros(len(A))],b_ub=b,A_eq=np.c_[C,[length]],b_eq=np.zeros(1),bounds=[(-bound,bound)]*d+[(0,.85)],method='highs',options={'primal_feasibility_tolerance':1e-9,'dual_feasibility_tolerance':1e-9})
        if not lp.success or lp.x[-1]<1e-8:
            trust*=.5
            if trust<1e-9:break
            continue
        fraction=.8*lp.x[-1]
        qp=minimize(lambda x:(.5*x@x,x),lp.x[:-1]*.8,jac=True,method='SLSQP',bounds=Bounds(-bound,bound),constraints=[LinearConstraint(A,-np.inf,b),LinearConstraint(C,-fraction*length,-fraction*length)],options={'maxiter':80,'ftol':1e-13})
        if np.max(A@qp.x-b)>1e-8 or np.max(abs(C@qp.x+fraction*length))>1e-8:
            trust*=.5
            if trust<1e-9:break
            continue
        dz=W@qp.x;accepted=False
        for level in range(18):
            zz=z+dz*2**-level
            try:
                if physical_retraction:
                    zz,ee,receipt=retract(model,e,dz,2**-level)
                    (out/f'step{it:04d}-retraction{level}.json').write_text(json.dumps(receipt,indent=2))
                else:ee=model.evaluate(zz,False)
                if use_corrector and level<4 and (ee['S']!=1 or ee['U']!=1 or ee['mechanical'].min()<eps*.5):
                    limit=(int(edge[0]),int(edge[1]),float(length*(1-.15*fraction*2**-level))) if keep_shortening else None
                    zz,ee,ok=correct(model,zz,out/f'step{it:04d}-correction{level}',steps=30,eps=3e-9,trust=.003,verbose=False,polish_margin=True,physical_retraction=physical_retraction,edge_limit=limit)
                    if not ok:continue
                rr=np.sqrt(np.mean(np.sum(ee['P']**2,axis=1)));ll=np.linalg.norm(ee['X'][edge[1]]-ee['X'][edge[0]])/rr
            except (ValueError,RuntimeError,np.linalg.LinAlgError):continue
            if ee['S']==ee['U']==1 and ee['mechanical'].min()>eps*.5 and ee['volume']/rr**3>floor and ll<length*(1-1e-6):
                z=zz;accepted=True;break
        if accepted and level==0:trust=min(.2,trust*1.25)
        if not accepted:trust*=.4
        if trust<1e-9:break
    return False

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--source',required=True);ap.add_argument('--out',required=True);ap.add_argument('--edge',type=int,required=True);ap.add_argument('--steps',type=int,default=150);ap.add_argument('--corrector',action='store_true');ap.add_argument('--input');ap.add_argument('--merit',choices=['direct','local'],default='direct');ap.add_argument('--physical-retraction',action='store_true');ap.add_argument('--keep-shortening',action='store_true');a=ap.parse_args();contract(a.source,a.out,a.edge,a.steps,use_corrector=a.corrector,input=a.input,merit=a.merit,physical_retraction=a.physical_retraction,keep_shortening=a.keep_shortening)
