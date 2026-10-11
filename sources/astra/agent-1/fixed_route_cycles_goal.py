"""Rechoose complete acyclic physical escape witnesses between finite solves.

Each route is an explicit reverse-Dijkstra tree using max(-W,0)^power. Its
subsequent nonlinear correction freezes those witnesses. Complete actual own
censuses, not route costs, decide whether a figure has been found.
"""
import pathlib,json,time,contextlib
import numpy as np
from geometry import arrows
from contact_forest import ContactModel,correct
from strict_equilibrium_coarsen_goal import run as contract

def routes_for(A,power):
    W=arrows(A);root=int(np.argmax(np.sum(A*A,axis=1)));cost=np.maximum(-W,0)**power;n=len(A);dist=np.full(n,np.inf);dist[root]=0;parent=np.full(n,-1,int);used=np.zeros(n,bool)
    for _ in range(n):
        j=int(np.argmin(np.where(used,np.inf,dist)));used[j]=True;trial=dist[j]+cost[:,j];take=(trial<dist)&(~used);dist[take]=trial[take];parent[take]=j
    parent[root]=int(np.argmax(W[root]))
    if np.any(parent<0):raise ValueError('Incomplete explicit physical routes')
    return parent.tolist(),[root]

def actual_margin(e):
    vals=[]
    for A in [e['P'],e['Q']]:
        w=np.sort(arrows(A).max(1));vals.extend([-w[0],w[1]])
    return float(min(vals))

def run(source,input,out,rounds=24,steps=260):
    source=pathlib.Path(source);input=pathlib.Path(input);out=pathlib.Path(out);out.mkdir(parents=True,exist_ok=False);(out/'source_body.npz').write_bytes(input.read_bytes());(out/'source.py').write_bytes(pathlib.Path(__file__).read_bytes());z=np.load(out/'source_body.npz')['z'];base=ContactModel(source);hist=[];start=time.time()
    (out/'definition.json').write_text(json.dumps(dict(source=str(source.resolve()),input=str(input.resolve()),rounds=rounds,steps=steps,powers=[1.,2.,.5,3.],scope='Explicit complete physical witness alternatives; over-budget1/1 requires further real-edge contraction'),indent=2))
    def finish(e,zz,label):
        if e['S']!=1 or e['U']!=1:return False
        filename='POTENTIAL_OWN110' if base.meta['E']<250 else 'OVERBUDGET_OWN110';np.savez(out/(filename+'.npz'),z=zz,X=e['X'],Q=e['Y']);(out/(filename+'.json')).write_text(json.dumps(dict(chart=str(source.resolve()),input=str((out/(filename+'.npz')).resolve()),E=base.meta['E'],actual_margin=actual_margin(e),**label),indent=2))
        if base.meta['E']>=250 and actual_margin(e)>1e-11:contract(source,out/(filename+'.npz'),out/'further_contractions',events=100,targets=14,steps=120,retirement_mode='contract-then-fixed-route')
        return True
    for k in range(rounds):
        e=base.evaluate(z,False)
        if finish(e,z,dict(round=k,stage='entrance')):return
        oldcount=e['S']+e['U'];best=None;bestkey=(oldcount,float('inf'))
        for ti,power in enumerate([1.,2.,.5,3.]):
            p=out/f'round{k:02d}-power{power}';p.mkdir();route=dict(parents=[],roots=[])
            for A in [e['P'],e['Q']]:pa,rs=routes_for(A,power);route['parents'].append(pa);route['roots'].append(rs)
            (p/'routes.json').write_text(json.dumps(route,indent=2));model=ContactModel(source,1,1,'fixed-route',route_data=route)
            with (p/'calculation.log').open('w') as log,contextlib.redirect_stdout(log):zz,ee,ok=correct(model,z,p/'flow',steps=steps,eps=2e-8,trust=.006,physical_retraction=True,acceptance='armijo',geometry_event_tolerance=2e-7)
            row=dict(round=k,power=power,oldS=e['S'],oldU=e['U'],S=ee['S'],U=ee['U'],E=base.meta['E'],corrected=bool(ok),Pmax=max([b['relative'] for b in ee['bars'][0]],default=0),Qmax=max([b['relative'] for b in ee['bars'][1]],default=0),seconds=time.time()-start)
            if finish(ee,zz,row):return
            key=(ee['S']+ee['U'],row['Pmax']+row['Qmax'])
            if key<bestkey:bestkey=key;best=(zz,ee,row)
            hist.append(row);(out/'history.json').write_text(json.dumps(hist,indent=2));print('FIXED_ROUTE_CYCLE_TRIAL',json.dumps(row),flush=True)
            if key[0]<oldcount:break
        if best is None or bestkey[0]>oldcount:
            (out/'FINITE_END.json').write_text(json.dumps(dict(round=k,seconds=time.time()-start,scope='These explicit route alternatives didnotreduce the actual census; no goal body'),indent=2));return
        z,ee,row=best;np.savez(out/'latest.npz',z=z,X=ee['X'],Q=ee['Y']);(out/'latest.json').write_text(json.dumps(row,indent=2))
    (out/'FINITE_END.json').write_text(json.dumps(dict(rounds=rounds,seconds=time.time()-start,scope='Finite route cycles ended without a qualifying figure'),indent=2))

if __name__=='__main__':
    import sys
    run(sys.argv[1],sys.argv[2],sys.argv[3])
