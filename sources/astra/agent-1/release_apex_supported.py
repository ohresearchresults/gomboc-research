"""Free all support planes except one retained actual unstable vertex star.

An orthogonal similarity puts the retained vertex at(0,0,1). Its k incident
planes retain literal q_z=1, so every admitted full-dimensional body has
degree excess at least k-3 and E<=3F-k-3. Every normal is otherwise free;
actual uniform centroids and all equilibria are independently recomputed.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import argparse,pathlib,json,time,contextlib
import numpy as np
from scipy.spatial import QhullError
from contact_multibasin_flow import UniqueUnstable
from contact_forest import correct
from contact_topology_continuation import run as continue_contacts
from geometry import halfspace_mesh,census,arrows
from bottleneck_capacity import capacities
from make_contact_atlas import make
from persistence_search import pairs,polar_edges

def run(source,input,out,samples=120,trials=2,seed=309143,sigmas=None,stratified=False,log_gaps=False):
    out=pathlib.Path(out);out.mkdir(parents=True,exist_ok=False);c=UniqueUnstable(source);e=c.evaluate(np.load(input)['z'],False);assert e['U']==1;u=e['roots'][0][0];fixed=c.inc[:,u];k=int(fixed.sum());bound=3*c.F-k-3
    if not 17<=bound<249:raise ValueError('Apex-preserving free-support family exceeds the explicit edge budget')
    pole=e['P'][u];radius=np.linalg.norm(pole);zaxis=pole/radius;basis=np.eye(3)[np.argmin(abs(zaxis))];xaxis=np.cross(basis,zaxis);xaxis/=np.linalg.norm(xaxis);yaxis=np.cross(zaxis,xaxis);rotation=np.stack([xaxis,yaxis,zaxis]);Q=(e['Q']@rotation.T)*radius;Q[fixed,2]=1.;assert np.max(Q[~fixed,2])<1.;rng=np.random.default_rng(seed);rows=[];candidates=[];start=time.time();np.savez(out/'similarity-parent.npz',Q=Q,rotation=rotation,radius=radius,fixed=fixed);scale=np.sqrt(np.mean(Q*Q));sigmas=[1e-7,3e-7,1e-6,3e-6,1e-5,3e-5] if sigmas is None else list(sigmas);(out/'definition.json').write_text(json.dumps(dict(source=str(pathlib.Path(source).resolve()),input=str(pathlib.Path(input).resolve()),seed=seed,retained_old_vertex=u,incident_facets=np.flatnonzero(fixed).tolist(),F=c.F,k=k,edge_upper_bound=bound,sigmas=sigmas,stratified=stratified,log_gaps=log_gaps,scope='New physical support perturbations; old equilibrium claims are not transferred through changed mass'),indent=2))
    for it in range(samples):
        sigma=sigmas[it%len(sigmas)];d=rng.normal(size=Q.shape)*sigma*scale;d[fixed,2]=0;H=Q+d
        if log_gaps:H[~fixed,2]=1-(1-Q[~fixed,2])*np.exp(rng.normal(size=np.sum(~fixed))*3*sigma)
        try:
            if np.max(H[~fixed,2])>=1-1e-12:raise ValueError('A nonincident plane cuts or contacts the explicitly retained vertex')
            m=halfspace_mesh(H);own=census(m,0)
            if len(m['active'])!=c.F or own['E']!=bound:raise ValueError('Perturbation did not realize the intended generic apex family')
            p=m['X']-m['g'];q=H/(1-H@m['g'])[:,None];root=int(np.argmax((q*q).sum(1)));cap,_,_,_=capacities(q,[root]);value=-float(cap.min());pp,h=pairs(q,polar_edges(m));bars=(1-h[pp[:,1]]/(q[pp[:,0]]**2).sum(1)).tolist();row=dict(sample=it,sigma=sigma,capacity_objective=value,Qmax=max(bars,default=0),**own);rows.append(row);rank=value+10*max(0,-own['min_primal_nonroot']);candidates.append((rank,it,H,row))
            if own['S']==own['U']==1 and min(own['min_primal_nonroot'],own['min_polar_nonroot'])>1e-9:np.savez(out/'POTENTIAL_OWN110_SUPPORTS.npz',Q=H);(out/'screen.json').write_text(json.dumps(rows,indent=2));return
        except (ValueError,QhullError,np.linalg.LinAlgError) as error:rows.append(dict(sample=it,sigma=sigma,error=repr(error)))
    (out/'screen.json').write_text(json.dumps(rows,indent=2));history=[];print('APEX_RELEASE_SCREEN',len(rows),'generic',len(candidates),'bound',bound,flush=True)
    if stratified:
        chosen=[]
        for sigma in sigmas:
            group=[x for x in candidates if x[3]['sigma']==sigma]
            if group:chosen.append(min(group,key=lambda x:x[0]))
    else:chosen=sorted(candidates,key=lambda x:x[0])
    for rank,(_,it,H,initial) in enumerate(chosen[:trials]):
        p=out/f'trial{rank:02d}-sample{it:04d}';p.mkdir();m=halfspace_mesh(H);proposal=dict(scope='Numerical apex-preserving fully released support body; independent physical correction required',V=len(m['X']),E=len(m['edges']),F=c.F,faces=m['faces'],edges=m['edges'].tolist(),active=list(range(c.F)),raw_vertices=[[str(x) for x in row] for row in m['X']],raw_halfspaces=[[str(x) for x in row]+['1'] for row in H]);(p/'proposal.json').write_text(json.dumps(proposal,indent=2));(p/'initial.json').write_text(json.dumps(initial,indent=2));make(p/'proposal.json',p/'chart',balanced=True);row=dict(trial=rank,sample=it)
        try:
            with (p/'calculation.log').open('w') as log,contextlib.redirect_stdout(log):
                child=UniqueUnstable(p/'chart');zz,ee,ok=correct(child,child.initial,p/'unique-U-correction',steps=150,eps=1e-7,trust=.003,verbose=True,polish_margin=True,physical_retraction=True);np.savez(p/'corrected.npz',z=zz,X=ee['X'],Q=ee['Y']);row.update(U_corrected=bool(ok),S=ee['S'],U=ee['U'],E=child.meta['E'])
                if ee['S']==ee['U']==1:
                    (out/'POTENTIAL_OWN110.json').write_text(json.dumps(dict(chart=str((p/'chart').resolve()),input=str((p/'corrected.npz').resolve())),indent=2));return
                if ok:
                    continue_contacts(p/'chart',p/'corrected.npz',p/'continuation',side='Q',rounds=40,tol=1e-7,flow_steps=260,epsilon=1e-7,objective_mode='capacity-tree',hold_unique_only=True)
                    if (p/'continuation/POTENTIAL_OWN110.json').exists():(out/'POTENTIAL_OWN110.json').write_bytes((p/'continuation/POTENTIAL_OWN110.json').read_bytes());return
                    if (p/'continuation/history.json').exists():row['last']=json.loads((p/'continuation/history.json').read_text())[-1]
        except (ValueError,RuntimeError,AssertionError,np.linalg.LinAlgError) as error:row['error']=repr(error)
        row['seconds']=time.time()-start;history.append(row);(out/'history.json').write_text(json.dumps(history,indent=2));print('APEX_RELEASE_TRIAL',json.dumps(row),flush=True)

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--source',required=True);p.add_argument('--input',required=True);p.add_argument('--out',required=True);p.add_argument('--samples',type=int,default=120);p.add_argument('--trials',type=int,default=2);p.add_argument('--sigmas');p.add_argument('--stratified',action='store_true');p.add_argument('--log-gaps',action='store_true');a=p.parse_args();run(a.source,a.input,a.out,a.samples,a.trials,sigmas=None if a.sigmas is None else tuple(map(float,a.sigmas.split(','))),stratified=a.stratified,log_gaps=a.log_gaps)
