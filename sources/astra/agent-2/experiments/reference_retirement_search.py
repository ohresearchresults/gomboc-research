"""Literal support retirement while retaining a fixed reference110 chamber.
The actual uniform centroid is recomputed for each new physical hull. Only its
distance to the fixed reference point is optimized; no centroid substitution.
All subsets retain original exact plane identities for independent rational audit.
"""
import sys,json,time,numpy as np
from pathlib import Path
from gmpy2 import mpq
from geometry import hull_from_supports,mass,angular_scores
from canonical_atlas import ROOT
sys.set_int_max_str_digits(0)
src=ROOT/'artifacts/projected_contact_retire/delete_4_35_94_99/audit.json';r=json.loads(src.read_text());a=json.loads((ROOT/'artifacts/reference110_exact_C490/audit.json').read_text());center=np.array([float(mpq(x)) for x in a['reference_center']]);Y=np.array([[float(mpq(v,mpq(h))) for v in n] for n,h in zip(r['normals'],r['offsets'])]);Y=Y/(1-Y@center)[:,None];out=ROOT/'artifacts/reference_retirement_C490';out.mkdir(exist_ok=False,parents=True);kept=list(range(len(Y)));start=time.time()
def evaluate(keep):
 X,H,faces,tr,E,active=hull_from_supports(Y[keep],tol=1e-10);v,c=mass(X,tr);s=angular_scores(H).max(1);u=angular_scores(X).max(1);Z=X-c;Q=H/(1-H@c)[:,None];ownS=angular_scores(Q).max(1);ownU=angular_scores(Z).max(1);return dict(kept=keep,V=len(X),E=E,F=len(H),refS=int((s<0).sum()),refU=int((u<0).sum()),ref_margin=float(min(np.sort(s)[1],np.sort(u)[1])),ownS=int((ownS<0).sum()),ownU=int((ownU<0).sum()),centroid_relative_reference=c.tolist(),centroid_distance=float(np.linalg.norm(c)),volume=float(v))
base=evaluate(kept);history=[base];print('START',base,flush=True)
for step in range(80):
 trials=[]
 for removed in kept:
  kk=[i for i in kept if i!=removed]
  try:
   z=evaluate(kk)
   if z['E']>248 or z['E']<17:continue
   z['removed']=removed;trials.append(z)
  except (ValueError,AssertionError,np.linalg.LinAlgError):continue
 (out/f'step{step}_screen.json').write_text(json.dumps(trials,indent=2)+'\n');good=[z for z in trials if z['refS']==z['refU']==1 and z['ref_margin']>1e-7];good.sort(key=lambda z:(z['centroid_distance'],z['E']))
 if not good or good[0]['centroid_distance']>=base['centroid_distance']-1e-12:
  (out/'STOP_REASON.json').write_text(json.dumps(dict(reason='no strictly improving single retirement retaining numericalreference110 within the edge budget',step=step,best_feasible=good[:3]),indent=2)+'\n');print('GREEDY_FINITE_STOP',step,'ref110_candidates',len(good),flush=True);break
 base=good[0];kept=base['kept'];history.append(base);(out/'history.json').write_text(json.dumps(history,indent=2)+'\n');print('REFERENCE_RETIREMENT',step,{k:v for k,v in base.items() if k!='kept'},flush=True)
 if base['ownS']==base['ownU']==1:(out/'NUMERICAL_OWN110_NOMINATION.json').write_text(json.dumps(base,indent=2)+'\n');print('REQUIRES_EXACT_OWN_AUDIT',flush=True);break
(out/'history.json').write_text(json.dumps(history,indent=2)+'\n');print('SECONDS',time.time()-start,flush=True)
