"""Minimum-total-barrier rooted escape trees of the same physical body.

For every nonroot point one outgoing geometric arrow is selected, and every
path must reach the farthest point. Chu-Liu/Edmonds chooses a minimum-weight
arborescence in the COMPLETE directed graph, with cost max(epsilon-arrow,0).
No small cycle can remove the cost of leaving its component. The two trees
use primal and dual vectors computed at the actual integrated centroid.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import json,pathlib,time,hashlib
import numpy as np,networkx as nx
from scipy.optimize import linprog
from scipy.sparse import csr_matrix,eye,hstack,vstack,diags
from contact_multibasin_flow import EssentialMaxima
from contact_escape_choices import arrow_rows
from contact_persistence_flow import normalized_volume
from contact_retraction import retract
from geometry import arrows


def tree(A,eps):
    n=len(A);root=int(np.argmax(np.einsum('ij,ij->i',A,A)));W=arrows(A)
    G=nx.DiGraph();G.add_nodes_from(range(n))
    G.add_weighted_edges_from((j,i,float(max(eps-W[i,j],0)))
                             for i in range(n) if i!=root for j in range(n) if i!=j)
    T=nx.minimum_spanning_arborescence(G,attr='weight',default=1,preserve_attrs=True)
    assert T.in_degree(root)==0 and all(T.in_degree(i)==1 for i in range(n) if i!=root)
    assert len(nx.descendants(T,root))==n-1
    ij=np.array(sorted((i,j) for j,i in T.edges()),int)
    v=W[ij[:,0],ij[:,1]];cost=float(np.maximum(eps-v,0).sum())
    return cost,ij,v


def bar_constraints(c,e,caps):
    values=[];derivatives=[]
    for s,side in enumerate(('P','Q')):
        A=e[side];D=e['D'+side];edges=c.eu if s==0 else c.es
        for record in e['bars'][s]:
            b=record['birth'];u,v=edges[record['edge']];a=A[u];delta=A[v]-a
            t=np.clip(-a@delta/(delta@delta),0,1);foot=a+t*delta
            height=foot@foot;born=A[b]@A[b]
            dh=2*foot@((1-t)*D[u]+t*D[v]);db=2*A[b]@D[b]
            gradient=-dh/born+height*db/born**2
            values.append(caps[s]-record['relative']);derivatives.append(-gradient)
    return np.asarray(values),np.asarray(derivatives).reshape(-1,c.free)


def run(source,input,out,steps=180,eps=1e-7,primal_weight=1.,bar_caps=None):
    source=pathlib.Path(source).resolve();input=pathlib.Path(input).resolve()
    out=pathlib.Path(out);out.mkdir(parents=True,exist_ok=False)
    c=EssentialMaxima(source);z=np.load(input)['z'];e=c.evaluate(z)
    assert 17<=c.meta['E']<249
    if bar_caps is not None and any(max((r['relative'] for r in e['bars'][s]),default=0)>bar_caps[s]+1e-12 for s in (0,1)):
        raise ValueError('Starting body exceeds an explicit radial persistence cap')
    floor=.2*normalized_volume(e)[0];trust=.02;history=[];start=time.time()
    (out/'definition.json').write_text(json.dumps(dict(source=str(source),input=str(input),
        input_sha256=hashlib.sha256(input.read_bytes()).hexdigest(),steps=steps,epsilon=eps,primal_weight=primal_weight,bar_caps=bar_caps,
        normalized_volume_floor=floor,scope='Finite full physical contact search; no exact Figure claim'),indent=2))
    (out/'source.py').write_bytes(pathlib.Path(__file__).read_bytes())
    def trees(e):
        p=tree(e['P'],eps);q=tree(e['Q'],eps);return primal_weight*p[0]+q[0],p,q
    for it in range(steps):
        e=c.evaluate(z);value,tp,tq=trees(e)
        lengths=[float(np.min(np.linalg.norm(A[ed[:,0]]-A[ed[:,1]],axis=1))/np.sqrt(np.mean(A*A)))
                 for A,ed in [(e['X'],c.eu),(e['Y'],c.es)]]
        row=dict(it=it,S=e['S'],U=e['U'],E=c.meta['E'],objective=value,Ptree=tp[0],Qtree=tq[0],
                 Pmax=max((b['relative'] for b in e['bars'][0]),default=0),
                 Qmax=max((b['relative'] for b in e['bars'][1]),default=0),lengths=lengths,trust=trust,seconds=time.time()-start)
        history.append(row);np.savez(out/'latest.npz',z=z,X=e['X'],Q=e['Y'])
        (out/'history.json').write_text(json.dumps(history,indent=2))
        print('MINIMUM_ESCAPE_ARBORESCENCE',json.dumps(row),flush=True)
        if e['S']==e['U']==1:
            np.savez(out/'POTENTIAL_OWN110.npz',z=z,X=e['X'],Q=e['Y'])
            (out/'POTENTIAL_OWN110.json').write_text(json.dumps(dict(chart=str(source),input=str((out/'POTENTIAL_OWN110.npz').resolve())),indent=2));return
        if min(lengths)<1e-7:
            (out/'EDGE_EVENT.json').write_text(json.dumps(row,indent=2));return
        W=c.metric(e);d=c.free;bound=trust/np.sqrt(d)
        vv=[];JJ=[]
        for side,record in [('P',tp),('Q',tq)]:
            ij=record[1];v,J=arrow_rows(e[side],e['D'+side],ij[:,0],ij[:,1]);vv.append(v);JJ.append(J@W)
        v=np.r_[tuple(vv)];J=np.vstack(JJ);n=len(v);scale=np.maximum(bound*np.abs(J).sum(1),1e-12)
        nv,DV=normalized_volume(e);geo=np.vstack([e['J']@W,e['gapJ']@W,DV@W])
        gb=np.r_[e['mechanical']-eps,.8*e['gapv'],nv-floor]
        if bar_caps is not None:
            bv,bJ=bar_constraints(c,e,bar_caps);geo=np.vstack([geo,bJ@W]);gb=np.r_[gb,bv]
        keep=gb<=bound*np.abs(geo).sum(1)+1e-10;geo=geo[keep];gb=gb[keep]
        gs=np.maximum(bound*np.abs(geo).sum(1),1e-12)
        I=eye(d);O=csr_matrix((d,n))
        mat=vstack([hstack([-csr_matrix(J/scale[:,None]),-diags(1/scale),csr_matrix((n,d))]),
                    hstack([-csr_matrix(geo/gs[:,None]),csr_matrix((len(gb),n+d))]),
                    hstack([I,O,-I]),hstack([-I,O,-I])],format='csr')
        rhs=np.r_[(v-eps)/scale,gb/gs,np.zeros(2*d)]
        weights=np.r_[np.full(len(vv[0]),primal_weight),np.ones(len(vv[1]))]
        objective=np.r_[np.zeros(d),weights,np.full(d,1e-7)]
        lp=linprog(objective,A_ub=mat,b_ub=rhs,bounds=[(-bound,bound)]*d+[(0,None)]*(n+d),method='highs',
                   options={'primal_feasibility_tolerance':1e-9,'dual_feasibility_tolerance':1e-9})
        if not lp.success or lp.fun>=value-max(1e-11,1e-8*value):
            trust*=.5
            if trust<1e-9:break
            continue
        row.update(predicted_cost=float(lp.fun),P_arrows=tp[1].tolist(),Q_arrows=tq[1].tolist())
        dz=W@lp.x[:d];accepted=False
        for level in range(10):
            try:
                zz,ee,receipt=retract(c,e,dz,2**-level)
                radius=np.sqrt(np.mean(np.sum(ee['P']**2,axis=1)))
                if ee['volume']/radius**3<=floor or ee['mechanical'].min()<.8*eps:continue
                if bar_caps is not None and any(max((r['relative'] for r in ee['bars'][s]),default=0)>bar_caps[s]+1e-12 for s in (0,1)):continue
                if ee['S']==ee['U']==1:
                    np.savez(out/'POTENTIAL_OWN110.npz',z=zz,X=ee['X'],Q=ee['Y'])
                    (out/'POTENTIAL_OWN110.json').write_text(json.dumps(dict(chart=str(source),input=str((out/'POTENTIAL_OWN110.npz').resolve())),indent=2));return
                newvalue,_,_=trees(ee)
                if newvalue<value-max(1e-11,1e-7*value):
                    z=zz;accepted=True;row.update(alpha=2**-level,retraction=receipt);break
            except (ValueError,RuntimeError,AssertionError,np.linalg.LinAlgError):continue
        if accepted and level==0:trust=min(.2,trust*1.2)
        elif accepted and level>=3:trust*=.7
        elif not accepted:trust*=.4
        if trust<1e-9:break
    (out/'history.json').write_text(json.dumps(history,indent=2))


def continuation(source,input,out,rounds=30,steps=160,primal_weight=1.,bar_caps=None):
    from merge_contact_facets import run as merge_facets
    from merge_contact_vertices import run as merge_vertices
    from repair_contact_domain import run as admit
    source=pathlib.Path(source);input=pathlib.Path(input);out=pathlib.Path(out)
    out.mkdir(parents=True,exist_ok=False);history=[]
    (out/'definition.json').write_text(json.dumps(dict(source=str(source.resolve()),input=str(input.resolve()),
        rounds=rounds,steps=steps,primal_weight=primal_weight,bar_caps=bar_caps,threshold=1e-7,
        policy='Polar retirement first when both primal and polar edges are nominated; explicit compound cleanup',
        scope='Numerical physical construction search; exact hull audit remains necessary'),indent=2))
    for k in range(rounds):
        p=out/f'stage{k:03d}';p.mkdir();run(source,input,p/'flow',steps=steps,primal_weight=primal_weight,bar_caps=bar_caps)
        if (p/'flow/POTENTIAL_OWN110.json').exists():
            (out/'POTENTIAL_OWN110.json').write_bytes((p/'flow/POTENTIAL_OWN110.json').read_bytes());return
        input=p/'flow/latest.npz';c=EssentialMaxima(source);e=c.evaluate(np.load(input)['z'],False)
        row=json.loads((p/'flow/history.json').read_text())[-1]
        for key in ['P_arrows','Q_arrows','retraction']:row.pop(key,None)
        row.update(stage=k,chart=str(source.resolve()),input=str(input.resolve()));history.append(row)
        (out/'history.json').write_text(json.dumps(history,indent=2))
        if not (p/'flow/EDGE_EVENT.json').exists():return
        kind='facets' if row['lengths'][1]<1e-7 else 'vertices';target=p/f'merge-{kind}'
        try:
            if kind=='facets':merge_facets(source,input,target,1e-7,len(e['X']),len(e['Y']),'balanced',cleanup=True)
            else:merge_vertices(source,input,target,1e-7,len(e['X']),len(e['Y']),'balanced')
            nextinput=target/'realization.npz'
        except (ValueError,RuntimeError,AssertionError,np.linalg.LinAlgError) as err:
            (p/'UNADMITTED_PROPOSAL.json').write_text(json.dumps(dict(error=repr(err)),indent=2))
            if not (target/'chart/chart.json').exists():return
            try:admit(target/'chart',target/'domain-admission',nU=len(e['X']),nS=len(e['Y']),eps=1e-9,steps=80)
            except (ValueError,RuntimeError,AssertionError,np.linalg.LinAlgError) as error:
                (p/'ADMISSION_ERROR.json').write_text(json.dumps(dict(error=repr(error)),indent=2));return
            nextinput=target/'domain-admission/ADMITTED.npz'
            if not nextinput.exists():return
        source=target/'chart';input=nextinput;child=EssentialMaxima(source)
        child.evaluate(np.load(input)['z'],False)
        if not 17<=child.meta['E']<249:raise ValueError('New complex violates the explicit complexity range')
