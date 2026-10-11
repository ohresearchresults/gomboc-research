"""Find reference110 cuts as a first step toward actual uniform-mass closure."""
import argparse
import hashlib
import json
import time
from pathlib import Path

import numpy as np

from unstable_cap_clip import Clip
from support_geometry import escape
from exact_clip_audit import audit
from goal_nomination import ExactGoalCandidateFound


def run(source,out,trials):
    out=Path(out);out.mkdir(parents=True,exist_ok=False);c=Clip(source);rng=np.random.default_rng(95528)
    (out/'definition.json').write_text(json.dumps(dict(source=str(Path(source).resolve()),source_audit_sha256=hashlib.sha256((Path(source)/'audit.json').read_bytes()).hexdigest(),scale=c.scale,center=c.center.tolist(),scope='reference110 is a nomination for physical mass closure, never a homogeneous success'),indent=2))
    rows=[];best=[];t0=time.time()
    for it in range(trials):
        slope=rng.normal(size=2)*rng.choice([.08,.25,.7,1.7,4.]);ratio=float(rng.uniform(.03,.99));control=np.r_[slope,ratio]
        try:
            g=c.body(control)
            if not(34<=2*g['E']<500 and g['V']+g['E']+g['F']<500):continue
            H0=g['H']/(1+g['H']@g['centroid'])[:,None]
            sr=int(sum(escape(H0)[0]<0));ur=int(sum(escape(g['X'])[0]<0))
            so=int(sum(escape(g['H'])[0]<0));uo=int(sum(escape(g['Z'])[0]<0))
            row=dict(it=it,controls=control.tolist(),normal=g['n'].tolist(),offset=g['h'],reference=[sr,ur],own=[so,uo],V=g['V'],E=g['E'],F=g['F'],centroid=g['centroid'].tolist(),centroid_norm=float(np.linalg.norm(g['centroid'])))
            if so==uo==1:
                p=out/f'goal_nomination{it}';p.mkdir();(p/'nomination.json').write_text(json.dumps(row,indent=2));a=audit(source,p/'nomination.json',out/'definition.json',p/'exact',10**15)
                if a['counts']==[1,1,0]and a['weak']==[0,0,0]and 34<=2*a['E']<500 and a['V']+a['E']+a['F']<500:raise ExactGoalCandidateFound('Exact bounded homogeneous clipped Figure '+str(p))
            if sr==ur==1:
                best.append(row);best.sort(key=lambda r:r['centroid_norm']);best=best[:20]
            rows.append(row)
        except(ValueError,AssertionError,np.linalg.LinAlgError)as err:rows.append(dict(it=it,controls=control.tolist(),error=repr(err)))
        if it%1000==0:
            print('REFERENCE_CLIP_GOAL_SCOUT',it,'bounded',len(rows),'reference110',len(best),'min_mass_displacement',None if not best else best[0]['centroid_norm'],flush=True)
            (out/'reference110_candidates.json').write_text(json.dumps(best,indent=2))
    (out/'trials.json').write_text(json.dumps(rows,indent=2));(out/'reference110_candidates.json').write_text(json.dumps(best,indent=2));print('REFERENCE_CLIP_SCOUT_COMPLETE',len(rows),len(best),time.time()-t0,flush=True)


if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('source');p.add_argument('out');p.add_argument('--trials',type=int,default=10000);a=p.parse_args();run(a.source,a.out,a.trials)
