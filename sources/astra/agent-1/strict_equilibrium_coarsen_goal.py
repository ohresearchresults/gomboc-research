"""Reduce genuine edge count by strict own110 geometric contractions.

The input's over-budget own110 census is only a starting chamber. Both actual
equilibrium landscapes are hard constraints during edge shortening. Every
topology proposal is re-realized and independently admitted. Only an E<250
own110 body nominates the requested exact certificate.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import pathlib,json,time,contextlib
import numpy as np,networkx as nx
from scipy.optimize import linprog
from scipy.sparse import csr_matrix,eye,hstack,vstack,diags
from contact_forest import ContactModel,correct
from contact_retraction import retract
from contact_persistence_flow import normalized_volume
from merge_contact_vertices import run as merge_vertices
from merge_contact_facets import run as merge_facets

def edge_value(e,side,edge,derivative=False):
    A=e['P'] if side==0 else e['Q'];D=e.get('DP') if side==0 else e.get('DQ');i,j=edge;delta=A[j]-A[i];r=np.sqrt(np.mean(A*A));length=np.linalg.norm(delta);value=length/r
    if not derivative:return value
    dr=np.einsum('ic,icp->p',A,D)/(A.size*r);dl=(delta/length)@(D[j]-D[i]);return value,dl/r-length*dr/r**2

def project_mechanics(c,z,side,edge,floor,length_bound,radius,iterations=8):
    """Explicit minimum-L1 physical correction of nonlinear escape drift.

    The predictor's intended edge decrease is constrained in each correction.
    Failure returns no feasible point; it never relaxes the final own110 test.
    """
    z=z.copy();receipts=[]
    for it in range(iterations):
        e=c.evaluate(z);v=e['mechanical'];length,grad=edge_value(e,side,edge,True);merit=float(np.maximum(floor-v,0).sum())
        if v.min()>=.9*floor and length<=length_bound:return z,e,receipts
        W=c.metric(e);d=c.free;bound=radius/np.sqrt(d);B=e['J']@W;G=e['gapJ']@W;I=eye(d);zeros=csr_matrix((len(v),d));zg=csr_matrix((len(G),d))
        A=vstack([hstack([-csr_matrix(B),zeros]),hstack([I,-I]),hstack([-I,-I]),hstack([-csr_matrix(G),zg]),hstack([csr_matrix((grad@W)[None,:]),csr_matrix((1,d))])],format='csr')
        rhs=np.r_[v-floor,np.zeros(2*d),.8*e['gapv'],length_bound-length]
        scale=np.maximum(bound*np.asarray(abs(A[:,:d]).sum(axis=1)).ravel(),1e-12)
        lp=linprog(np.r_[np.zeros(d),np.ones(d)],A_ub=diags(1/scale)@A,b_ub=rhs/scale,bounds=[(-bound,bound)]*d+[(0,None)]*d,method='highs',options={'primal_feasibility_tolerance':1e-9,'dual_feasibility_tolerance':1e-9})
        if not lp.success:return None
        dz=W@lp.x[:d];accepted=False
        for level in range(12):
            try:zz,ee,_=retract(c,e,dz,2**-level)
            except (ValueError,RuntimeError,np.linalg.LinAlgError):continue
            newmerit=float(np.maximum(floor-ee['mechanical'],0).sum())
            if newmerit<merit-max(1e-15,1e-4*merit*2**-level):
                z=zz;accepted=True;receipts.append(dict(it=it,alpha=2**-level,old_merit=merit,new_merit=newmerit));break
        if not accepted:return None
    e=c.evaluate(z,False)
    if e['mechanical'].min()>=.9*floor and edge_value(e,side,edge)<=length_bound:return z,e,receipts
    return None

def shorten(source,input,out,side,edge,steps=180,tol=2e-7,mechanical_projection=False,preserve_equilibria=True):
    out=pathlib.Path(out);out.mkdir(parents=True,exist_ok=False);c=ContactModel(source,1,1,'local');z=np.load(input)['z'];e=c.evaluate(z);vmin=float(e['mechanical'].min())
    if e['S']!=1 or e['U']!=1 or vmin<=0:raise ValueError('Shortening entrance must be strict actual own110')
    floor=min(vmin*.02,1e-8);volume0=normalized_volume(e)[0];trust=.01;hist=[];start=time.time()
    (out/'definition.json').write_text(json.dumps(dict(source=str(pathlib.Path(source).resolve()),input=str(pathlib.Path(input).resolve()),side=side,edge=list(map(int,edge)),steps=steps,tol=tol,hard_equilibrium_margin=floor if preserve_equilibria else None,normalized_volume_floor=.2*volume0,mechanical_projection=mechanical_projection,preserve_equilibria=preserve_equilibria),indent=2))
    for it in range(steps):
        e=c.evaluate(z);length,grad=edge_value(e,side,edge,True);row=dict(it=it,S=e['S'],U=e['U'],edge_length=length,minimum=float(e['mechanical'].min()),noncontact=e['minimum_gap'],turn=e['minimum_turn'],trust=trust,seconds=time.time()-start);hist.append(row)
        np.savez(out/'latest.npz',z=z,X=e['X'],Q=e['Y']);(out/'history.json').write_text(json.dumps(hist,indent=2))
        if it%10==0:print('STRICT_OWN110_EDGE' if preserve_equilibria else 'GEOMETRIC_EDGE_CONTRACTION',json.dumps(row),flush=True)
        if length<tol:return z,e,True
        W=c.metric(e);d=c.free;bound=trust/np.sqrt(d);B=e['J']@W;G=e['gapJ']@W;nv,DV=normalized_volume(e)
        if preserve_equilibria:A=np.vstack([-B,-G,-(DV@W)[None,:]]);rhs=np.r_[e['mechanical']-floor,.8*e['gapv'],nv-.2*volume0]
        else:A=np.vstack([-G,-(DV@W)[None,:]]);rhs=np.r_[.8*e['gapv'],nv-.2*volume0]
        scale=np.maximum(bound*np.abs(A).sum(1),1e-12)
        objective=grad@W;lp=linprog(objective,A_ub=A/scale[:,None],b_ub=rhs/scale,bounds=[(-bound,bound)]*d,method='highs',options={'primal_feasibility_tolerance':1e-9,'dual_feasibility_tolerance':1e-9})
        accepted=False
        if lp.success:
            dz=W@lp.x;gain=-float(grad@dz)
            if gain>1e-14:
                for level in range(20):
                    try:zz,ee,receipt=retract(c,e,dz,2**-level)
                    except (ValueError,RuntimeError,np.linalg.LinAlgError):continue
                    correction_receipt=None
                    if preserve_equilibria and mechanical_projection and ee['mechanical'].min()<.9*floor:
                        limit=length-.05*gain*2**-level
                        try:projected=project_mechanics(c,zz,side,edge,floor,limit,max(1e-8,trust*2**-level*.7))
                        except (ValueError,RuntimeError,np.linalg.LinAlgError):projected=None
                        if projected is None:continue
                        zz,ee,correction_receipt=projected
                    vv=float(ee['mechanical'].min());newlen=edge_value(ee,side,edge)
                    actual_nv=ee['volume']/np.mean(np.sum(ee['P']**2,axis=1))**1.5
                    mechanics_ok=(ee['S']==ee['U']==1 and vv>=.8*floor) if preserve_equilibria else True
                    if mechanics_ok and actual_nv>=.2*volume0 and newlen<length-max(1e-14,1e-4*gain*2**-level):
                        z=zz;accepted=True;row.update(alpha=2**-level,predicted_reduction=gain*2**-level,actual_reduction=length-newlen,mechanical_correction=correction_receipt);break
        if accepted and level==0:trust=min(.08,trust*1.2)
        elif not accepted:trust*=.4
        if trust<1e-10:break
    e=c.evaluate(z,False);np.savez(out/'latest.npz',z=z,X=e['X'],Q=e['Y']);(out/'history.json').write_text(json.dumps(hist,indent=2));return z,e,edge_value(e,side,edge)<tol

def run(source,input,out,events=100,targets=24,steps=160,mechanical_projection=False,retirement_mode='strict'):
    if retirement_mode not in ('strict','contract-then-correct','contract-then-fixed-route'):raise ValueError('Unknown explicit contraction protocol')
    preserve=retirement_mode=='strict'
    source=pathlib.Path(source);input=pathlib.Path(input);out=pathlib.Path(out);out.mkdir(parents=True,exist_ok=False);(out/'source.py').write_bytes(pathlib.Path(__file__).read_bytes());history=[];start=time.time()
    (out/'definition.json').write_text(json.dumps(dict(source=str(source.resolve()),input=str(input.resolve()),events=events,targets=targets,steps=steps,mechanical_projection=mechanical_projection,retirement_mode=retirement_mode,scope='Only strict own110 bodies with fewer real edges are retained between contractions; over-budget intermediates are not accepted figures'),indent=2))
    for event in range(events):
        c=ContactModel(source,1,1,'local');e=c.evaluate(np.load(input)['z'],False)
        if e['S']!=1 or e['U']!=1 or e['mechanical'].min()<=0:raise ValueError('Retained body lost strict own110')
        if 17<=c.meta['E']<=249:
            np.savez(out/'POTENTIAL_OWN110.npz',z=np.load(input)['z'],X=e['X'],Q=e['Y']);(out/'POTENTIAL_OWN110.json').write_text(json.dumps(dict(chart=str(source.resolve()),input=str((out/'POTENTIAL_OWN110.npz').resolve()),E=c.meta['E'],S=1,U=1,scope='Requires exact same-body mass, hull and weak-contact verification'),indent=2));return
        choices=[]
        for side,edges in enumerate([c.eu,c.es]):
            graph=nx.Graph();graph.add_edges_from(edges)
            for edge in edges:
                length=edge_value(e,side,edge);choices.append((length,side,tuple(map(int,edge))))
        choices.sort();adopted=False;tested=0;parentE=c.meta['E']
        for rank,(length,side,edge) in enumerate(choices):
            graph=nx.Graph();graph.add_edges_from(c.eu if side==0 else c.es);contract=nx.contracted_edge(graph,edge,self_loops=False)
            if nx.node_connectivity(contract)<3:continue
            if tested>=targets:break
            tested+=1;p=out/f'event{event:03d}-try{rank:03d}-side{side}';p.mkdir();rec=dict(event=event,rank=rank,side=side,edge=edge,oldE=parentE,initial_length=length)
            try:
                with (p/'calculation.log').open('w') as log,contextlib.redirect_stdout(log):
                    z,ee,closed=shorten(source,input,p/'shortening',side,edge,steps=steps,mechanical_projection=mechanical_projection,preserve_equilibria=preserve)
                rec.update(shortening_reached=bool(closed),final_length=edge_value(ee,side,edge),minimum=float(ee['mechanical'].min()))
                if closed:
                    # Convert the explicit proposed edge length to the
                    # merger's raw physical-coordinate normalization.
                    A=ee['X'] if side==0 else ee['Y'];scale=np.sqrt(np.mean((ee['P'] if side==0 else A)**2));threshold=1.05*np.linalg.norm(A[edge[0]]-A[edge[1]])/scale+1e-13
                    producer=merge_vertices if side==0 else merge_facets
                    with (p/'merge.log').open('w') as log,contextlib.redirect_stdout(log):
                        summary=producer(source,p/'shortening/latest.npz',p/'body',threshold,1,1,'balanced')
                    child=ContactModel(p/'body/chart',1,1,'local' if preserve else 'shortest',escape_floor=2e-9);zz=np.load(p/'body/realization.npz')['z'];ce=child.evaluate(zz,False)
                    if retirement_mode=='contract-then-fixed-route':
                        from shortest_escape_forest import shortest_forest
                        routes=dict(parents=[],roots=[])
                        for pts in [ce['P'],ce['Q']]:
                            roots=[int(np.argmax(np.sum(pts*pts,axis=1)))];pa,_,_,_=shortest_forest(pts,roots,0.);routes['roots'].append(roots);routes['parents'].append(pa.tolist())
                        (p/'routes.json').write_text(json.dumps(routes,indent=2));child=ContactModel(p/'body/chart',1,1,'fixed-route',route_data=routes);ce=child.evaluate(zz,False)
                    if ce['S']!=1 or ce['U']!=1:
                        with (p/'repair.log').open('w') as log,contextlib.redirect_stdout(log):
                            zz,ce,_=correct(child,zz,p/'repair',steps=180 if preserve else 600,eps=2e-9,trust=.004,physical_retraction=True,acceptance='armijo')
                    rec.update(newE=child.meta['E'],S=ce['S'],U=ce['U'],new_minimum=float(ce['mechanical'].min()))
                    from geometry import arrows
                    guards=[]
                    for points in [ce['P'],ce['Q']]:
                        ww=np.sort(arrows(points).max(1));guards.extend([-ww[0],ww[1]])
                    rec['actual_local_margin']=float(min(guards))
                    if ce['S']==ce['U']==1 and min(guards)>1e-11 and child.meta['E']<parentE:
                        np.savez(p/'retained_own110.npz',z=zz,X=ce['X'],Q=ce['Y']);source=p/'body/chart';input=p/'retained_own110.npz';adopted=True
            except (ValueError,RuntimeError,AssertionError,np.linalg.LinAlgError) as err:rec['error']=str(err)
            rec.update(adopted=adopted,seconds=time.time()-start);history.append(rec);(out/'history.json').write_text(json.dumps(history,indent=2));print('STRICT_OWN110_CONTRACTION',json.dumps(rec),flush=True)
            if adopted:
                (out/'latest.json').write_text(json.dumps(dict(chart=str(source.resolve()),input=str(input.resolve()),E=rec['newE'],S=1,U=1),indent=2));break
        if not adopted:
            (out/'FINITE_END.json').write_text(json.dumps(dict(event=event,targets=tested,seconds=time.time()-start,scope='Specified strict contraction attempts ended without a qualifying figure'),indent=2));return
    (out/'FINITE_END.json').write_text(json.dumps(dict(events=events,seconds=time.time()-start,scope='Finite strict contraction chain exhausted; goal unfulfilled'),indent=2))

if __name__=='__main__':
    import sys
    run(sys.argv[1],sys.argv[2],sys.argv[3])
