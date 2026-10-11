"""Try explicitly chosen actual root cancellations in a complete contact hull.

The target is an identified persistence birth, excluded from the admissible
remaining root set. This permits trying another geometric cancellation when
the smallest bar is trapped. Every finite trial and actual count is retained.
"""
import pathlib,json,time,contextlib
import numpy as np
from contact_forest import ContactModel,correct

def run(source,input,out,rounds=100,steps=160,bar_limit=.15,targets_per_round=14):
    out=pathlib.Path(out);out.mkdir(parents=True,exist_ok=False);source=pathlib.Path(source);c=ContactModel(source,1,1,'capacity',exempt_junior=True)
    z=np.load(input)['z'];e=c.evaluate(z,False);np.savez(out/'entrance.npz',z=z,X=e['X'],Q=e['Y'])
    (out/'definition.json').write_text(json.dumps(dict(source=str(source.resolve()),input=str(pathlib.Path(input).resolve()),rounds=rounds,
        steps=steps,bar_limit=bar_limit,targets_per_round=targets_per_round,scope='Explicit alternative actual-root cancellations; only complete own110 is a candidate'),indent=2))
    (out/'source.py').write_bytes(pathlib.Path(__file__).read_bytes());history=[];start=time.time()
    def nominate(zz,ee,row):
        np.savez(out/'POTENTIAL_OWN110.npz',z=zz,X=ee['X'],Q=ee['Y'])
        (out/'POTENTIAL_OWN110.json').write_text(json.dumps(dict(chart=str(source.resolve()),input=str((out/'POTENTIAL_OWN110.npz').resolve()),**row),indent=2))
    for k in range(rounds):
        e=c.evaluate(z,False)
        if e['S']==e['U']==1:nominate(z,e,dict(round=k,S=1,U=1,E=c.meta['E']));return
        options=[]
        for side,number,bars in [(0,e['U'],e['bars'][0]),(1,e['S'],e['bars'][1])]:
            if number>1:
                options.extend((float(b['relative']),side,int(b['birth'])) for b in bars)
        options.sort();base=e['S']+e['U'];accepted=False
        for rank,(depth,side,target) in enumerate(options[:targets_per_round]):
            trial=out/f'round{k:03d}-try{rank:02d}-side{side}-root{target}';trial.mkdir()
            ex=[[],[]];ex[side]=[target];tu=e['U']-(side==0);ts=e['S']-(side==1)
            model=ContactModel(source,tu,ts,'capacity',exempt_junior=True,excluded_roots=ex)
            try:
                with (trial/'calculation.log').open('w') as log,contextlib.redirect_stdout(log):
                    zz,ee,ok=correct(model,z,trial/'flow',steps=steps,eps=2e-9,trust=.008,verbose=True,physical_retraction=True)
                row=dict(round=k,rank=rank,side=side,target=target,depth=depth,oldS=e['S'],oldU=e['U'],targetS=ts,targetU=tu,
                    S=ee['S'],U=ee['U'],corrected=bool(ok),Pmax=max([b['relative'] for b in ee['bars'][0]],default=0),
                    Qmax=max([b['relative'] for b in ee['bars'][1]],default=0),seconds=time.time()-start)
                if ee['S']==ee['U']==1:nominate(zz,ee,row);return
                if ee['S']+ee['U']<base and max(row['Pmax'],row['Qmax'])<=bar_limit:
                    z=zz;accepted=True;row['adopted']=True;np.savez(out/'latest.npz',z=z,X=ee['X'],Q=ee['Y'])
                else:row['adopted']=False
            except (ValueError,RuntimeError,AssertionError,np.linalg.LinAlgError) as error:
                row=dict(round=k,rank=rank,side=side,target=target,depth=depth,error=repr(error),adopted=False,seconds=time.time()-start)
            history.append(row);(out/'history.json').write_text(json.dumps(history,indent=2));print('TARGETED_ACTUAL_CANCELLATION',json.dumps(row),flush=True)
            if accepted:break
        if not accepted:
            (out/'FINITE_END.json').write_text(json.dumps(dict(round=k,seconds=time.time()-start,scope='All specified finite target cancellations failed to reduce the actual census in this search chamber'),indent=2));return
    (out/'FINITE_END.json').write_text(json.dumps(dict(rounds=rounds,seconds=time.time()-start,scope='Finite direct sequence exhausted without a qualifying body'),indent=2))

if __name__=='__main__':
    import sys
    run(sys.argv[1],sys.argv[2],sys.argv[3])
