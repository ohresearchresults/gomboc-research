"""Repeated literal vertex additions with true contact topology events.

This finite scientific search recomputes actual mass and admits only physical
own211 intermediate bodies. The requested own110 body is saved immediately if
encountered; a separate exact audit is mandatory before any success claim.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import argparse,json,pathlib,time,contextlib
import numpy as np
from stable_face_augmentation import run as screen
from contact_augmentation_scout import run as contact_scout
from adaptive_contact_events import run as events
from contact_forest import ContactModel
from basin_scout import score

def endpoint(chart,input):
    c=ContactModel(chart,1,2,'local',exempt_junior=True);z=np.load(input)['z'];e=c.evaluate(z,False)
    if e['S']==e['U']==1:return c,e,0.
    if e['S']!=2 or e['U']!=1 or e['mechanical'].min()<8e-8:return None
    if e['minimum_gap']<1e-9 or e['minimum_turn']<1e-11:return None
    if not 17<=c.meta['E']<249:return None
    return c,e,max((b['relative'] for b in e['bars'][1]),default=0.)

def nominate(out,chart,input):
    (out/'POTENTIAL_OWN110.json').write_text(json.dumps(dict(chart=str(pathlib.Path(chart).resolve()),input=str(pathlib.Path(input).resolve()),scope='Numerical physical own110 requires independent exact rational audit'),indent=2))

def run(input,out,cycles=8,samples=650,trials=5,seed=84029):
    out=pathlib.Path(out);out.mkdir(parents=True,exist_ok=False);q=np.load(input)['Q'];value=max(score(q)['Q']);history=[];start=time.time()
    for cycle in range(cycles):
        folder=out/f'cycle{cycle:02d}';folder.mkdir();np.savez(folder/'source.npz',Q=q)
        with (folder/'calculations.log').open('w') as log,contextlib.redirect_stdout(log):
            screen(folder/'source.npz',folder/'screen',samples=samples,repairs=0,seed=seed+cycle)
            if (folder/'screen/POTENTIAL_OWN110.npz').exists():
                np.savez(out/'POTENTIAL_OWN110_SUPPORTS.npz',Q=np.load(folder/'screen/POTENTIAL_OWN110.npz')['Q']);return
            contact_scout(folder/'screen',folder/'contacts',limit=trials)
            if (folder/'contacts/POTENTIAL_OWN110.json').exists():
                (out/'POTENTIAL_OWN110.json').write_bytes((folder/'contacts/POTENTIAL_OWN110.json').read_bytes());return
        records=json.loads((folder/'contacts/history.json').read_text());records=sorted([r for r in records if r.get('strict_corrected') and r.get('S')==2 and r.get('U')==1],key=lambda r:r['Qmax']);possibilities=[]
        for rank,r in enumerate(records[:3]):
            p=folder/'contacts'/f'trial{r["trial"]:02d}-sample{r["sample"]:05d}';candidates=[(p/'chart',p/'corrected.npz'),(p/'chart',p/'descent/latest.npz')]
            with (folder/f'event-rank{rank}.log').open('w') as log,contextlib.redirect_stdout(log):
                try:events(p/'chart',p/'descent/latest.npz',folder/f'events{rank}',side='Q',rounds=8)
                except (ValueError,AssertionError,RuntimeError,np.linalg.LinAlgError) as err:(folder/f'event-rank{rank}-error.txt').write_text(repr(err))
            if (folder/f'events{rank}/POTENTIAL_OWN110.json').exists():
                (out/'POTENTIAL_OWN110.json').write_bytes((folder/f'events{rank}/POTENTIAL_OWN110.json').read_bytes());return
            for body in sorted((folder/f'events{rank}').glob('event*/body')):
                if (body/'realization.npz').exists():candidates.append((body/'chart',body/'realization.npz'))
                flow=body.parent/'flow/latest.npz'
                if flow.exists():candidates.append((body/'chart',flow))
            for chart,pinput in candidates:
                try:data=endpoint(chart,pinput)
                except (ValueError,AssertionError,RuntimeError,np.linalg.LinAlgError,FileNotFoundError):continue
                if data is None:continue
                c,e,v=data
                if e['S']==e['U']==1:nominate(out,chart,pinput);return
                possibilities.append((v,str(chart),str(pinput),c,e))
        if not possibilities:
            row=dict(cycle=cycle,scope='No physical own211 endpoint admitted by this finite candidate set',seconds=time.time()-start);history.append(row);(out/'history.json').write_text(json.dumps(history,indent=2));break
        new,chart,pinput,c,e=min(possibilities,key=lambda a:a[0]);improves=new<value-1e-6
        row=dict(cycle=cycle,previous=value,Qmax=new,accepted=improves,V=len(e['X']),E=c.meta['E'],F=c.F,chart=str(pathlib.Path(chart).resolve()),input=str(pathlib.Path(pinput).resolve()),seconds=time.time()-start);history.append(row);(out/'history.json').write_text(json.dumps(history,indent=2));print('AUGMENTATION_CYCLE',json.dumps(row),flush=True)
        if not improves:break
        q=e['Y'];value=new;np.savez(out/'latest-strict211.npz',Q=q,X=e['X'],z=np.load(pinput)['z']);(out/'latest-source.json').write_text(json.dumps(row,indent=2))

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--input',required=True);ap.add_argument('--out',required=True);ap.add_argument('--cycles',type=int,default=8);ap.add_argument('--samples',type=int,default=650);ap.add_argument('--trials',type=int,default=5);ap.add_argument('--seed',type=int,default=84029);a=ap.parse_args();run(a.input,a.out,a.cycles,a.samples,a.trials,a.seed)
