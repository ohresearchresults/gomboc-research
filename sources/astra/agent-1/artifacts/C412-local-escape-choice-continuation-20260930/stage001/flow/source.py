"""Finite mixed-integer physical escape-direction search.

An outgoing positive arrow certifies that a point is not a radial maximum.
The linearized search may select among several actual geometric arrows for
each nonessential point. Every admitted step is reconstructed as one convex
contact body and its uniform centroid and complete arrow census recomputed.
MILP feasibility is only a search proposal, never a Figure certificate.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1'
os.environ['OMP_NUM_THREADS']='1'
import argparse, hashlib, json, pathlib, time, warnings
import numpy as np
from scipy.optimize import milp, Bounds, LinearConstraint
from scipy.sparse import coo_matrix
from contact_forest import ContactModel
from contact_retraction import retract
from contact_persistence_flow import normalized_volume
from geometry import arrows


def arrow_rows(A,D,ii,jj):
    src=A[ii];delta=A[jj]-src
    rr=np.einsum('ij,ij->i',src,src);dd=np.einsum('ij,ij->i',delta,delta)
    den=np.sqrt(rr*dd);v=np.einsum('ij,ij->i',src,delta)/den
    gi=(delta-src)/den[:,None]-v[:,None]*(src/rr[:,None]-delta/dd[:,None])
    gj=src/den[:,None]-v[:,None]*delta/dd[:,None]
    return v,np.einsum('ic,icp->ip',gi,D[ii])+np.einsum('ic,icp->ip',gj,D[jj])


def escape_choices(c,e,W,bound,choices,branch_limit,phase,ordering='local'):
    records=[];offset=0
    for side in ('P','Q'):
        A=e[side];D=e['D'+side];n=len(A);w=arrows(A)
        radii=np.einsum('ij,ij->i',A,A);root=int(np.argmax(radii))
        rank=np.empty(n,int);rank[np.argsort(radii,kind='stable')]=np.arange(n)
        for i in range(n):
            order=np.argsort(-w[i])
            if ordering=='radius' and i!=root:order=order[rank[order]>rank[i]]
            if i==root:
                jj=order[:1];sign=-1.
            else:
                jj=order[:choices];sign=1.
            v,J=arrow_rows(A,D,np.full(len(jj),i),jj)
            v*=sign;J=sign*J@W
            # A single safe outgoing arrow suffices throughout the predictor
            # trust box. Actual nonlinear feasibility is still re-evaluated.
            if i!=root and v[0]-bound*np.abs(J[0]).sum()>1e-6:
                jj=jj[:1];v=v[:1];J=J[:1]
            records.append(dict(index=offset+i,side=side,point=i,root=i==root,
                                parents=jj,values=v,J=J))
        offset+=n
    eligible=[k for k,r in enumerate(records) if len(r['parents'])>1]
    # Each bounded MILP explicitly changes only one finite group of parent
    # choices. The group rotates; all other points use their current best arrow.
    if len(eligible)>branch_limit:
        eligible=sorted(eligible,key=lambda k:(records[k]['values'][0]-records[k]['values'][1])/
                        max(bound*np.abs(records[k]['J'][0]-records[k]['J'][1]).sum(),1e-12))
        start=(phase*branch_limit)%len(eligible)
        selected=set((eligible+eligible)[start:start+branch_limit])
        for k in eligible:
            if k not in selected:
                for key in ('parents','values','J'):records[k][key]=records[k][key][:1]
    return records


def proposal(c,e,trust,eps,choices,seconds,primal_weight,volume_floor,branch_limit=16,phase=0,ordering='local'):
    W=c.metric(e);d=c.free;bound=trust/np.sqrt(d)
    records=escape_choices(c,e,W,bound,choices,branch_limit,phase,ordering);n=len(records)
    nb=sum(len(r['parents']) for r in records if len(r['parents'])>1)
    N=d+n+nb+d;rows=[];cols=[];vals=[];lower=[];upper=[]
    def add(ids,values,lo=-np.inf,hi=np.inf):
        row=len(upper);ids=np.asarray(ids);values=np.asarray(values)
        keep=values!=0;rows.extend([row]*int(keep.sum()))
        cols.extend(ids[keep].tolist());vals.extend(values[keep].tolist())
        lower.append(lo);upper.append(hi)
    next_binary=d+n
    for r in records:
        si=d+r['index'];binary=[]
        for value,J in zip(r['values'],r['J']):
            ids=list(range(d))+[si];coeff=list(-J)+[-1.]
            rhs=float(value-eps)
            if len(r['parents'])>1:
                M=max(0.,eps-value+bound*np.abs(J).sum())+1e-15
                ids.append(next_binary);coeff.append(M);binary.append(next_binary)
                next_binary+=1;rhs+=M
            scale=max(bound*np.abs(J).sum(),abs(rhs),1e-10)
            add(ids,np.asarray(coeff)/scale,hi=rhs/scale)
        if binary:add(binary,np.ones(len(binary)),lo=1.,hi=1.)
    nv,DV=normalized_volume(e)
    G=np.vstack([e['gapJ']@W,DV@W]);b=np.r_[.8*e['gapv'],nv-volume_floor]
    for J,rhs in zip(G,b):
        if rhs>bound*np.abs(J).sum()+1e-10:continue
        scale=max(bound*np.abs(J).sum(),1e-12)
        add(range(d),-J/scale,hi=rhs/scale)
    for j in range(d):
        add([j,d+n+nb+j],[1.,-1.],hi=0.)
        add([j,d+n+nb+j],[-1.,-1.],hi=0.)
    matrix=coo_matrix((vals,(rows,cols)),shape=(len(upper),N)).tocsc()
    integrality=np.zeros(N,int);integrality[d+n:d+n+nb]=1
    lb=np.r_[np.full(d,-bound),np.zeros(n+nb+d)]
    ub=np.r_[np.full(d,bound),np.full(n,np.inf),np.ones(nb),np.full(d,bound)]
    weights=np.r_[np.full(len(e['P']),primal_weight),np.ones(len(e['Q']))]
    cost=np.r_[np.zeros(d),weights,np.zeros(nb),np.full(d,1e-7)]
    with warnings.catch_warnings():
        warnings.filterwarnings('ignore',message='Unrecognized options detected.*')
        res=milp(cost,integrality=integrality,bounds=Bounds(lb,ub),
                 constraints=LinearConstraint(matrix,lower,upper),
                 options={'time_limit':seconds,'mip_rel_gap':.01,'node_limit':1000,'threads':1})
    report=dict(status=int(res.status),message=res.message,binaries=nb,
                nodes=getattr(res,'mip_node_count',None),gap=getattr(res,'mip_gap',None))
    if res.x is None:return None,report
    values=matrix@res.x
    violation=max(float(np.max(values-np.asarray(upper))),float(np.max(np.asarray(lower)-values)),
                  float(np.max(lb-res.x)),float(np.max(res.x-ub)))
    int_error=float(np.max(abs(res.x[d+n:d+n+nb]-np.rint(res.x[d+n:d+n+nb])))) if nb else 0.
    report.update(proposal_residual=violation,integrality_residual=int_error,
                  predicted_merit=float(cost@res.x))
    if violation>1e-7 or int_error>1e-6:return None,report
    selected=[];cursor=d+n
    for r in records:
        count=len(r['parents']);k=0
        if count>1:
            k=int(np.argmax(res.x[cursor:cursor+count]));cursor+=count
        selected.append(dict(side=r['side'],point=r['point'],parent=int(r['parents'][k])))
    report['selected_arrows']=selected
    return W@res.x[:d],report


def ordered_values(e):
    values=[]
    for side in ('P','Q'):
        A=e[side];radii=np.einsum('ij,ij->i',A,A);root=int(np.argmax(radii));w=arrows(A)
        rank=np.empty(len(A),int);rank[np.argsort(radii,kind='stable')]=np.arange(len(A))
        root_value=-w[root].max();w[rank[None,:]<=rank[:,None]]=-np.inf
        v=w.max(1);v[root]=root_value;values.append(v)
    return np.r_[tuple(values)]


def run(source,input,out,steps=120,choices=3,seconds=5.,primal_weight=1.,eps=1e-7,branch_limit=16,ordering='local'):
    source=pathlib.Path(source).resolve();input=pathlib.Path(input).resolve()
    out=pathlib.Path(out);out.mkdir(parents=True,exist_ok=False)
    c=ContactModel(source,1,1,'local');z=np.load(input)['z'];e=c.evaluate(z)
    assert 17<=c.meta['E']<249
    volume_floor=.3*normalized_volume(e)[0];trust=.04;history=[];start=time.time()
    definition=dict(source=str(source),input=str(input),input_sha256=hashlib.sha256(input.read_bytes()).hexdigest(),
                    steps=steps,choices=choices,branch_limit=branch_limit,milp_seconds=seconds,primal_weight=primal_weight,epsilon=eps,ordering=ordering,
                    volume_floor=volume_floor,scope='Finite numerical physical escape-choice experiment, not exact evidence')
    (out/'definition.json').write_text(json.dumps(definition,indent=2))
    (out/'source.py').write_bytes(pathlib.Path(__file__).read_bytes())
    weights=np.r_[np.full(len(e['P']),primal_weight),np.ones(len(e['Q']))]
    if ordering not in ('local','radius'):raise ValueError('Unknown explicit parent-order policy')
    def merit(e):return float(weights@np.maximum(eps-(ordered_values(e) if ordering=='radius' else e['mechanical']),0))
    for it in range(steps):
        e=c.evaluate(z);value=merit(e)
        lengths=[float(np.min(np.linalg.norm(A[ed[:,0]]-A[ed[:,1]],axis=1))/np.sqrt(np.mean(A*A)))
                 for A,ed in [(e['X'],c.eu),(e['Y'],c.es)]]
        row=dict(it=it,S=e['S'],U=e['U'],E=c.meta['E'],merit=value,minimum=float(e['mechanical'].min()),
                 Pmax=max((b['relative'] for b in e['bars'][0]),default=0),
                 Qmax=max((b['relative'] for b in e['bars'][1]),default=0),trust=trust,lengths=lengths,seconds=time.time()-start)
        history.append(row);np.savez(out/'latest.npz',z=z,X=e['X'],Q=e['Y'])
        (out/'history.json').write_text(json.dumps(history,indent=2));print('ESCAPE_CHOICES',json.dumps(row),flush=True)
        if e['S']==e['U']==1:
            np.savez(out/'POTENTIAL_OWN110.npz',z=z,X=e['X'],Q=e['Y'])
            (out/'POTENTIAL_OWN110.json').write_text(json.dumps(dict(chart=str(source),input=str((out/'POTENTIAL_OWN110.npz').resolve())),indent=2));return
        if min(lengths)<1e-8:
            (out/'EDGE_EVENT.json').write_text(json.dumps(row,indent=2));return
        dz,report=proposal(c,e,trust,eps,choices,seconds,primal_weight,volume_floor,branch_limit,it,ordering)
        row['milp']=report
        if dz is None or report['predicted_merit']>=value-1e-10:
            trust*=.5
            if trust<1e-8:break
            continue
        accepted=False
        for level in range(12):
            try:
                zz,ee,receipt=retract(c,e,dz,2**-level)
                nv=ee['volume']/np.sqrt(np.mean(np.sum(ee['P']**2,axis=1)))**3
                if nv<=volume_floor:continue
                if ee['S']==ee['U']==1:
                    np.savez(out/'POTENTIAL_OWN110.npz',z=zz,X=ee['X'],Q=ee['Y'])
                    (out/'POTENTIAL_OWN110.json').write_text(json.dumps(dict(chart=str(source),input=str((out/'POTENTIAL_OWN110.npz').resolve())),indent=2));return
                if merit(ee)<value-max(1e-12,value*1e-6):
                    z=zz;accepted=True;row.update(accepted_alpha=2**-level,retraction=receipt);break
            except (ValueError,RuntimeError,AssertionError,np.linalg.LinAlgError):continue
        if accepted and level==0:trust=min(.2,trust*1.25)
        elif accepted and level>3:trust*=.7
        elif not accepted:trust*=.4
        if trust<1e-8:break
    (out/'history.json').write_text(json.dumps(history,indent=2))


def continuation(source,input,out,rounds=30,steps=100,choices=2,seconds=5.,branch_limit=14,ordering='local'):
    from merge_contact_vertices import run as merge_vertices
    from merge_contact_facets import run as merge_facets
    from repair_contact_domain import run as admit
    source=pathlib.Path(source);input=pathlib.Path(input);out=pathlib.Path(out)
    out.mkdir(parents=True,exist_ok=False);history=[]
    (out/'definition.json').write_text(json.dumps(dict(source=str(source.resolve()),input=str(input.resolve()),
        rounds=rounds,steps=steps,choices=choices,branch_limit=branch_limit,ordering=ordering,
        scope='Finite explicit-complex continuation of physical escape-choice search; no exact incidence claim'),indent=2))
    for k in range(rounds):
        p=out/f'stage{k:03d}';p.mkdir()
        run(source,input,p/'flow',steps=steps,choices=choices,seconds=seconds,branch_limit=branch_limit,ordering=ordering)
        if (p/'flow/POTENTIAL_OWN110.json').exists():
            (out/'POTENTIAL_OWN110.json').write_bytes((p/'flow/POTENTIAL_OWN110.json').read_bytes());return
        input=p/'flow/latest.npz';c=ContactModel(source,1,1,'local');e=c.evaluate(np.load(input)['z'],False)
        row=json.loads((p/'flow/history.json').read_text())[-1];row.pop('milp',None)
        row.update(stage=k,chart=str(source.resolve()),input=str(input.resolve()))
        history.append(row);(out/'history.json').write_text(json.dumps(history,indent=2))
        if not (p/'flow/EDGE_EVENT.json').exists():return
        kind='vertices' if row['lengths'][0]<row['lengths'][1] else 'facets'
        target=p/f'merge-{kind}';tol=1e-8
        try:
            if kind=='vertices':merge_vertices(source,input,target,tol,len(e['X']),len(e['Y']),'balanced')
            else:merge_facets(source,input,target,tol,len(e['X']),len(e['Y']),'balanced',cleanup=True)
            nextinput=target/'realization.npz'
        except (ValueError,RuntimeError,AssertionError,np.linalg.LinAlgError) as err:
            (p/'INITIAL_PROPOSAL_ERROR.json').write_text(json.dumps(dict(error=repr(err)),indent=2))
            if not (target/'chart/chart.json').exists():return
            try:admit(target/'chart',target/'domain-admission',nU=len(e['X']),nS=len(e['Y']),eps=1e-9,steps=80)
            except (ValueError,RuntimeError,AssertionError,np.linalg.LinAlgError) as error:
                (p/'ADMISSION_ERROR.json').write_text(json.dumps(dict(error=repr(error)),indent=2));return
            nextinput=target/'domain-admission/ADMITTED.npz'
            if not nextinput.exists():return
        source=target/'chart';input=nextinput;child=ContactModel(source,1,1,'local')
        child.evaluate(np.load(input)['z'],False)
        if not 17<=child.meta['E']<249:raise ValueError('Proposed contact complex is outside the explicit search budget')


if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--source',required=True);p.add_argument('--input',required=True)
    p.add_argument('--out',required=True);p.add_argument('--steps',type=int,default=120)
    p.add_argument('--choices',type=int,default=3);p.add_argument('--seconds',type=float,default=5.)
    p.add_argument('--primal-weight',type=float,default=1.);a=p.parse_args()
    run(a.source,a.input,a.out,a.steps,a.choices,a.seconds,a.primal_weight)
