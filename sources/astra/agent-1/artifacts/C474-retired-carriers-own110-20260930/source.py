"""Literal carrier retirement followed by direct actual-root cancellation.

The saved retired physical body is independently rehulled, recharted, and
integrated before any continuation. Its source equations and all finite
trials remain in the same folder. No old equilibrium claim is transferred.
"""
import pathlib,json,time
import numpy as np
from geometry import halfspace_mesh,census
from make_contact_atlas import make
from contact_forest import ContactModel
from targeted_cancellation_goal import run as cancel

def run(source,out,names=('P129','P74','Q29','Q5')):
    source=pathlib.Path(source);out=pathlib.Path(out);out.mkdir(parents=True,exist_ok=False)
    (out/'source.py').write_bytes(pathlib.Path(__file__).read_bytes());(out/'definition.json').write_text(json.dumps(dict(source=str(source.resolve()),names=names,
        scope='Distinct literal hull changes with complete own-mass root-cancellation searches; only110 nominates exact verification'),indent=2))
    history=[];start=time.time()
    for name in names:
        p=out/name;p.mkdir();H=np.load(source/name/'body.npz')['Q'];m=halfspace_mesh(H);Q=H[m['active']];X=m['X']
        proposal=dict(V=len(X),E=len(m['edges']),F=len(Q),faces=m['faces'],edges=m['edges'].tolist(),active=list(range(len(Q))),
            raw_vertices=X.astype(str).tolist(),raw_halfspaces=[list(map(str,q))+['1'] for q in Q])
        (p/'physical_proposal.json').write_text(json.dumps(proposal,indent=2));make(p/'physical_proposal.json',p/'chart',balanced=True)
        c=ContactModel(p/'chart');e=c.evaluate(c.initial,False);delta=max(float(abs(X-e['X']).max()),float(abs(Q-e['Y']).max()))
        if delta>1e-8:raise ValueError('Rechart changed the specified literal retired body')
        np.savez(p/'entrance.npz',z=c.initial,X=e['X'],Q=e['Y']);(p/'entrance.json').write_text(json.dumps(dict(S=e['S'],U=e['U'],E=c.meta['E'],rechart_deviation=delta,raw_hull=census(m,0)),indent=2))
        cancel(p/'chart',p/'entrance.npz',p/'cancellations',rounds=100,steps=220,bar_limit=.3,targets_per_round=16,protect_single=True,acceptance='armijo')
        if (p/'cancellations/POTENTIAL_OWN110.json').exists():
            (out/'POTENTIAL_OWN110.json').write_bytes((p/'cancellations/POTENTIAL_OWN110.json').read_bytes());return
        last=json.loads((p/'cancellations/history.json').read_text())[-1] if (p/'cancellations/history.json').exists() else {}
        row=dict(case=name,seconds=time.time()-start,last=last);history.append(row);(out/'history.json').write_text(json.dumps(history,indent=2));print('LITERAL_RETIREMENT_GOAL_STAGE',json.dumps(row),flush=True)
    (out/'FINITE_END.json').write_text(json.dumps(dict(cases=list(names),seconds=time.time()-start,scope='Finite distinct hull continuations ended without a qualifying body'),indent=2))

if __name__=='__main__':
    import sys
    run(sys.argv[1],sys.argv[2])
