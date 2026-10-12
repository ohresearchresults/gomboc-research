"""Individual actual equilibrium cancellations after a common projective map.

The embedding is recharted with the same complete contact incidence. Each
trial asks for one fewer genuine root and re-evaluates the complete own census.
Small persistence values alone never qualify. Only an actual110 is nominated.
"""
import pathlib,json,time,contextlib
import numpy as np
from contact_forest import ContactModel,correct
from make_contact_atlas import make

def run(parent_chart,projective,out,rounds=100,steps=110,bar_limit=.03):
    out=pathlib.Path(out);out.mkdir(parents=True,exist_ok=False);parent=ContactModel(parent_chart)
    data=np.load(projective);X=data['X'];Q=data['Q'];F=len(Q)
    proposal=dict(V=len(X),F=F,E=parent.meta['E'],raw_vertices=X.astype(str).tolist(),
        raw_halfspaces=[list(map(str,r))+['1'] for r in Q],faces=parent.meta['faces'],edges=parent.eu.tolist(),active=list(range(F)),
        scope='Numerical single-projective physical embedding; not an exact certificate')
    (out/'embedding.json').write_text(json.dumps(proposal,indent=2));make(out/'embedding.json',out/'chart',balanced=True)
    chart=out/'chart';c=ContactModel(chart,1,1,'capacity',exempt_junior=True);z=c.initial;e=c.evaluate(z,False)
    deviation=max(float(abs(e['X']-X).max()),float(abs(e['Y']-Q).max()))
    if deviation>1e-8:raise ValueError('Contact rechart materially changed the specified physical embedding')
    np.savez(out/'entrance.npz',z=z,X=e['X'],Q=e['Y'])
    (out/'source.py').write_bytes(pathlib.Path(__file__).read_bytes())
    (out/'definition.json').write_text(json.dumps(dict(parent_chart=str(pathlib.Path(parent_chart).resolve()),projective=str(pathlib.Path(projective).resolve()),
        rounds=rounds,steps=steps,bar_limit=bar_limit,rechart_max_deviation=deviation,
        scope='Direct individual equilibrium cancellations at the same uniform volume centroid; exact only after own110'),indent=2))
    history=[];start=time.time()
    def potential(z,e,path):
        np.savez(out/'POTENTIAL_OWN110.npz',z=z,X=e['X'],Q=e['Y'])
        (out/'POTENTIAL_OWN110.json').write_text(json.dumps(dict(chart=str(chart.resolve()),input=str((out/'POTENTIAL_OWN110.npz').resolve()),
            source=path,E=c.meta['E'],S=e['S'],U=e['U']),indent=2))
    for k in range(rounds):
        e=c.evaluate(z,False)
        if e['S']==e['U']==1:potential(z,e,'round entrance');return
        options=[]
        for side,number,bars in [('P',e['U'],e['bars'][0]),('Q',e['S'],e['bars'][1])]:
            if number>1:options.append((min([b['relative'] for b in bars],default=0),side))
        options.sort();accepted=False;base=e['S']+e['U']
        for rank,(_,side) in enumerate(options):
            targetU=e['U']-(side=='P');targetS=e['S']-(side=='Q');trial=out/f'round{k:03d}-{rank}-{side}';trial.mkdir()
            model=ContactModel(chart,targetU,targetS,'capacity',exempt_junior=True)
            try:
                with (trial/'calculation.log').open('w') as log,contextlib.redirect_stdout(log):
                    zz,ee,ok=correct(model,z,trial/'flow',steps=steps,eps=2e-9,trust=.006,verbose=True,physical_retraction=True)
                row=dict(round=k,side=side,oldS=e['S'],oldU=e['U'],targetS=targetS,targetU=targetU,S=ee['S'],U=ee['U'],
                    corrected=bool(ok),Pmax=max([b['relative'] for b in ee['bars'][0]],default=0),Qmax=max([b['relative'] for b in ee['bars'][1]],default=0),
                    seconds=time.time()-start)
                if ee['S']==ee['U']==1:potential(zz,ee,str(trial));return
                if ee['S']+ee['U']<base and max(row['Pmax'],row['Qmax'])<=bar_limit:
                    z=zz;accepted=True;row['adopted']=True
                    np.savez(out/'latest.npz',z=z,X=ee['X'],Q=ee['Y'])
                else:row['adopted']=False
            except (ValueError,RuntimeError,AssertionError,np.linalg.LinAlgError) as error:row=dict(round=k,side=side,error=repr(error),adopted=False)
            history.append(row);(out/'history.json').write_text(json.dumps(history,indent=2));print('INDIVIDUAL_OWN_CANCELLATION',json.dumps(row),flush=True)
            if accepted:break
        if not accepted:
            (out/'FINITE_END.json').write_text(json.dumps(dict(round=k,seconds=time.time()-start,scope='Neither individual cancellation trial reduced the complete census within the specified finite search chamber'),indent=2));return
    (out/'FINITE_END.json').write_text(json.dumps(dict(rounds=rounds,seconds=time.time()-start,scope='Finite sequence completed without a qualifying own110'),indent=2))

if __name__=='__main__':
    import sys
    run(sys.argv[1],sys.argv[2],sys.argv[3])
