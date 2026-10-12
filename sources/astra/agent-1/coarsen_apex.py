"""Facet retirement with full physical own110 repair, preserving one real apex.
Intermediate bodies may exceed the target budget; only E<250 is nominated.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import numpy as np,json,pathlib,time,argparse
from soft_forest_polish import guards,run as repair
from geometry import census

def run(input,out,stages=80,attempts=10,protect_apex=True,only_apex=False):
    out=pathlib.Path(out);out.mkdir(parents=True,exist_ok=True);Q=np.load(input)['Q'];history=[];start=time.time()
    for stage in range(stages):
        m,v,_,_=guards(Q,1,1);before=census(m)
        if before['S']!=1 or before['U']!=1 or min(v)<1e-8:raise ValueError('coarsening requires genuinely strict floating own110 parent')
        np.savez(out/'latest-strict110.npz',Q=Q)
        if before['E']<250:
            np.savez(out/'NOMINATION_OWN110.npz',Q=Q);print('POTENTIAL_TARGET_BODY_SAVED_REQUIRES_EXACT',before,flush=True);return
        folder=out/f'stage{stage:03d}';folder.mkdir(exist_ok=True);np.savez(folder/'parent.npz',Q=Q);apex=set(np.flatnonzero(np.isclose(Q[:,2],1,atol=1e-12,rtol=0)));protected=set(before['S_ids'])|(apex if protect_apex or len(apex)<=3 else set());screen=[]
        for j in range(len(Q)):
            if j in protected:continue
            if only_apex and j not in apex:continue
            q=np.delete(Q,j,axis=0)
            try:mm,vv,_,_=guards(q,1,1);stats=census(mm);merit=float(np.maximum(5e-7-vv,0).sum());screen.append(dict(row=j,merit=merit,minimum=float(min(vv)),**stats))
            except Exception as e:screen.append(dict(row=j,error=repr(e)))
        screen.sort(key=lambda x:x.get('merit',float('inf')));(folder/'screen.json').write_text(json.dumps(screen,indent=2));print('RETIRE_STAGE',stage,before['E'],before['F'],'best',[(r['row'],r.get('merit')) for r in screen[:5]],flush=True);accepted=False
        for entry in screen[:attempts]:
            if 'error' in entry:continue
            j=entry['row'];trial=np.delete(Q,j,axis=0);p=folder/f'drop{j:03d}';p.mkdir(exist_ok=True);np.savez(p/'input.npz',Q=trial)
            try:repair(trial,p/'repair',nP=1,nQ=1,steps=160,apex=True)
            except Exception as e:(p/'error.txt').write_text(repr(e));continue
            if not (p/'repair/NOMINATION.npz').exists():continue
            q=np.load(p/'repair/NOMINATION.npz')['Q'];mm,vv,_,_=guards(q,1,1);after=census(mm)
            if after['S']==after['U']==1 and after['E']<before['E'] and min(vv)>4e-7:
                Q=q;accepted=True;row=dict(stage=stage,deleted_row=j,source=str(p/'repair/NOMINATION.npz'),minimum_guard=float(min(vv)),seconds=time.time()-start,**after);history.append(row);(out/'history.json').write_text(json.dumps(history,indent=2));np.savez(out/'latest-strict110.npz',Q=Q);print('STRICT_FACET_RETIRED',json.dumps(row),flush=True);break
        if not accepted:print('RETIRE_STAGE_STALLED',stage,flush=True);break

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--input',required=True);ap.add_argument('--out',required=True);ap.add_argument('--stages',type=int,default=80);ap.add_argument('--attempts',type=int,default=10);ap.add_argument('--allow-apex-retirement',action='store_true');ap.add_argument('--only-apex',action='store_true');a=ap.parse_args();run(a.input,a.out,a.stages,a.attempts,not(a.allow_apex_retirement or a.only_apex),a.only_apex)
