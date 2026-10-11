"""Finite series of literal cap additions and full physical deformations.

Each adopted stage is independently frozen from a rational contact chart and
audited at its own uniform centroid. All failed stages remain saved. Neither
the numerical Q objective nor a numerical root census is an acceptance gate.
"""
import sys,json,hashlib,time
from pathlib import Path
import numpy as np
from support_persistence import ROOT
from targeted_stable_caps import run as scout
from apex_exact_freeze import run as freeze_cap
from canonical_atlas_threshold_multiroot import make
from canonical_own_corrector import run as prepare
from canonical_projected_boxflow import run as flow
from audit_canonical_atlas import audit as freeze_chart
from exact_bars_gmp import audit as exact_bars

def run(src,out,rounds=3,iterations=450):
    src=Path(src);out=Path(out);out.mkdir(parents=True,exist_ok=False)
    history=[];start=time.time()
    for stage in range(rounds):
        old=json.loads(src.read_text())
        if old['counts']!=[2,1,1] or old['weak']!=[0,0,0]:raise ValueError('source is not exact own211weak000')
        if old['E']+3>248:break
        d=out/f'round{stage:02d}';d.mkdir()
        (d/'source.json').write_text(json.dumps(dict(source=str(src),sha256=hashlib.sha256(src.read_bytes()).hexdigest()),indent=2)+'\n')
        scout(src,d/'screen',samples=6500,seed=95073+stage)
        rows=json.loads((d/'screen/screen.json').read_text())['rows']
        rows=[r for r in rows if r['S']<=2 and r['U']==1 and r['E']<=248]
        if not rows:
            (d/'NO_STRICT_NOMINATION.json').write_text('{}\n');break
        row=min(rows,key=lambda r:(r['S'],r['Qmax']))
        r=freeze_cap(src,d/'screen/screen.json',row['sample'],d/'exact_added_cap')
        if r['counts']==[1,1,0] and r['weak']==[0,0,0]:
            (out/'EXACT_B_GOAL_REQUIRES_INDEPENDENT_A.json').write_text(json.dumps(dict(source=str(d/'exact_added_cap/audit.json')),indent=2)+'\n');return
        if r['counts']!=[2,1,1] or r['weak']!=[0,0,0]:raise ValueError('rounded cap has a different class; do not continue silently')
        chart=d/'chart';meta,q,*_=make(d/'exact_added_cap/audit.json',chart,quality_floor=.01);np.save(chart/'initial_q.npy',q)
        prepare(chart,chart/'strict_preparation',chart/'initial_q.npy',iters=150,eps=2e-7)
        strict=chart/'strict_preparation/STRICT_NUMERICAL_q.npy'
        if not strict.exists():
            (d/'STRICT_PREPARATION_FAILED.json').write_text('{}\n');break
        flow(chart,chart/'projected_flow',strict,iters=iterations,eps=1e-7)
        r=freeze_chart(chart,chart/'projected_flow/latest_q.npy',chart/'exact_endpoint_g14',10**14)
        exact_bars(chart/'exact_endpoint_g14/audit.json')
        summary=json.loads((chart/'exact_endpoint_g14/summary.json').read_text());bars=json.loads((chart/'exact_endpoint_g14/audit_exact_bars.json').read_text())
        rec=dict(stage=stage,source=str(src),body=str(chart/'exact_endpoint_g14/audit.json'),summary=summary,P=[x['relative_depth_float'] for x in bars['P']],Q=[x['relative_depth_float'] for x in bars['Q']],seconds=time.time()-start)
        history.append(rec);(out/'history.json').write_text(json.dumps(history,indent=2)+'\n');print('EXACT_CAP_CYCLE_ENDPOINT',rec,flush=True)
        if r['counts']==[1,1,0] and r['weak']==[0,0,0] and r['E']<=248:
            (out/'EXACT_B_GOAL_REQUIRES_INDEPENDENT_A.json').write_text(json.dumps(rec,indent=2)+'\n');return
        if r['counts']!=[2,1,1] or r['weak']!=[0,0,0]:raise ValueError('endpoint audit changed strict class')
        src=chart/'exact_endpoint_g14/audit.json'
    (out/'FINITE_SERIES_END.json').write_text(json.dumps(dict(stages=len(history),latest_source=str(src),goal_complete=False),indent=2)+'\n')

if __name__=='__main__':run(ROOT/sys.argv[1],ROOT/sys.argv[2],int(sys.argv[3]) if len(sys.argv)>3 else 3,int(sys.argv[4]) if len(sys.argv)>4 else 450)
