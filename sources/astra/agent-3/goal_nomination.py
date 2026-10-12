"""Preserve and exactly audit a110nomination before any class-specific repair.
Binary64 coordinates are interpreted as their literal exact dyadic rationals;
an exact translation by their arithmetic mean merely places the origin inside.
"""
from pathlib import Path
import json,numpy as np
from gmpy2 import mpq
from detach_stable import audit_points

class ExactGoalCandidateFound(RuntimeError):pass

def preserve(X,out,reason):
 out=Path(out);out.mkdir(exist_ok=False,parents=True);np.save(out/'literal_binary64.npy',X);P=[tuple(mpq(float(v))for v in row)for row in X];mean=[sum(p[k]for p in P)/len(P)for k in range(3)];P=[tuple(p[k]-mean[k]for k in range(3))for p in P];a=audit_points(P,out/'exact_dyadic',dict(definition='literal binary64 physical vertices, exact arithmetic-mean translation',source='literal_binary64.npy',reason=reason));good=a['counts']==[1,1,0] and a['weak']==[0,0,0] and 34<=2*a['E']<500 and a['V']+a['E']+a['F']<500;row=dict(goal_candidate=good,counts=a['counts'],weak=a['weak'],V=a['V'],E=a['E'],F=a['F'],C_2E=2*a['E'],VplusEplusF=a['V']+a['E']+a['F'],scope='requires final source review; no native goal status changed');(out/'nomination.json').write_text(json.dumps(row,indent=2))
 if good:raise ExactGoalCandidateFound('Full exact Figure candidate preserved at '+str(out))
