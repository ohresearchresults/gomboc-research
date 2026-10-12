"""Correct actual unstable roots of a finite deep cap, then merge stable basins.
Every trial is a new full physical contact body with independently integrated
mass. The old reference centre is not constrained or accepted as its centroid.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import argparse,json,pathlib,contextlib,time
import numpy as np
from contact_forest import correct
from contact_multibasin_flow import UniqueUnstable,run as multibasin
from contact_topology_continuation import run as strict_continue

def run(source,out,limit=6,etas=(.015,.004,.001,.0001,.00001),bar_cap=None):
    source=pathlib.Path(source);out=pathlib.Path(out);out.mkdir(parents=True,exist_ok=False);history=[];start=time.time()
    for trial,chart in enumerate(sorted(source.glob('trial*/chart'))[:limit]):
        p=out/f'trial{trial:02d}';p.mkdir();row=dict(trial=trial,source=str(chart.resolve()))
        try:
            with (p/'calculation.log').open('w') as log,contextlib.redirect_stdout(log):
                c=UniqueUnstable(chart);z,e,ok=correct(c,c.initial,p/'actual-U-correction',steps=120,eps=1e-7,trust=.005,verbose=True,polish_margin=True,physical_retraction=True);np.savez(p/'corrected.npz',z=z,X=e['X'],Q=e['Y']);row.update(corrected=bool(ok),S=e['S'],U=e['U'],Q=[b['relative'] for b in e['bars'][1]],E=c.meta['E'])
                if e['S']==e['U']==1:
                    (out/'POTENTIAL_OWN110.json').write_text(json.dumps(dict(chart=str(chart.resolve()),input=str((p/'corrected.npz').resolve())),indent=2));return
                if ok:
                    multibasin(chart,p/'corrected.npz',p/'recombine',etas=etas,steps=90,bar_cap=bar_cap)
                    if (p/'recombine/POTENTIAL_OWN110.json').exists():
                        (out/'POTENTIAL_OWN110.json').write_bytes((p/'recombine/POTENTIAL_OWN110.json').read_bytes());return
                    q=p/'recombine/latest-source.json'
                    if q.exists():
                        result=json.loads(q.read_text());row['recombine_final']=result
                        # Recover all strict stable escape witnesses on this
                        # endpoint. Small numerical bars are never discarded.
                        strict_continue(result['chart'],p/'recombine/latest.npz',p/'strict-repair',side='Q',rounds=12,strategy='balanced',flow_steps=100)
                        if (p/'strict-repair/POTENTIAL_OWN110.json').exists():
                            (out/'POTENTIAL_OWN110.json').write_bytes((p/'strict-repair/POTENTIAL_OWN110.json').read_bytes());return
                        h=p/'strict-repair/history.json'
                        if h.exists():row['strict_final']=json.loads(h.read_text())[-1]
        except (ValueError,RuntimeError,AssertionError,np.linalg.LinAlgError) as error:row['error']=repr(error)
        row['seconds']=time.time()-start;history.append(row);(out/'history.json').write_text(json.dumps(history,indent=2));print('DEEP_CAP_RECOMBINATION',json.dumps(row),flush=True)

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--source',required=True);p.add_argument('--out',required=True);p.add_argument('--limit',type=int,default=6);p.add_argument('--etas',default='.015,.004,.001,.0001,.00001');p.add_argument('--bar-cap',type=float);a=p.parse_args();run(a.source,a.out,a.limit,tuple(map(float,a.etas.split(','))),a.bar_cap)
