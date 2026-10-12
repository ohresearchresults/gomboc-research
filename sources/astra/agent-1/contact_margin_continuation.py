"""Increase strict own110 escape margins through actual nonlinear correction.
The over-budget C622 control is not a qualifying figure; this experiment seeks
an open physical chamber from which incidence retirement may be possible.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import argparse,pathlib,json,time
import numpy as np
from contact_forest import ContactModel,correct

def run(source,out,input=None,stages=100):
    c=ContactModel(source,1,1,'local');z=np.load(input)['z'] if input else c.initial.copy();out=pathlib.Path(out);out.mkdir(parents=True,exist_ok=False);history=[];start=time.time();factor=1.6
    e=c.evaluate(z,False)
    if e['S']!=1 or e['U']!=1:raise ValueError('source is not own110')
    for k in range(stages):
        old=float(e['mechanical'].min());target=old*factor/.8;folder=out/f'stage{k:03d}'
        zz,ee,ok=correct(c,z,folder,steps=65,eps=target,trust=.001,verbose=False,polish_margin=True,physical_retraction=True)
        improved=bool(ok and ee['S']==ee['U']==1 and ee['mechanical'].min()>old*1.03)
        row=dict(stage=k,requested_margin=target,old_margin=old,candidate_margin=float(ee['mechanical'].min()),S=ee['S'],U=ee['U'],accepted=improved,gap=ee['minimum_gap'],seconds=time.time()-start);history.append(row);(out/'history.json').write_text(json.dumps(history,indent=2));print('MARGIN_CONTINUATION',row,flush=True)
        if improved:
            z=zz;e=ee;np.savez(out/'latest-strict.npz',z=z,X=e['X'],Q=e['Y']);factor=min(2.,factor*1.1)
            if c.meta['E']<250:
                np.savez(out/'POTENTIAL_OWN110.npz',z=z,X=e['X'],Q=e['Y']);return
        else:factor=1+(factor-1)*.5
        if factor<1.04:break

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--source',required=True);ap.add_argument('--out',required=True);ap.add_argument('--input');ap.add_argument('--stages',type=int,default=100);a=ap.parse_args();run(a.source,a.out,a.input,a.stages)
