from pathlib import Path
import json,numpy as np,time
from numeric import *
R=Path(__file__).parent;data=json.loads((R/'parent650/C650/GENERATOR.json').read_text());A=json.loads((R/'parent650/C650/A.json').read_text());faces=A['faces'];X=recover(data);q=X[:137]
base=mechanics(q,faces,details=True,tol=1e-12);print('base', {k:v for k,v in base.items() if not isinstance(v,np.ndarray) and k!='owners'},flush=True)
P=base['P'];owners,ef=topology(faces);H=set(tuple(map(int,l.split())) for l in (R/'H213_edges.txt').read_text().splitlines())
candidates=sorted((np.linalg.norm(P[a]-P[b]),a,b) for a,b in ef if tuple(sorted(ef[a,b])) not in H)
out=[]
for dist,a,b in candidates:
 for m in sorted(set(owners[a])^set(owners[b])):
  try:
   z,fs=snapped(data,faces,a,b,m);XX=recover(z);r=mechanics(XX[:137],fs,tol=1e-10)
   row={'edge':[a,b],'polar_edge':ef[a,b],'moved':m,'length':float(dist),**r};out.append(row)
   if r['min_gap']>1e-9 and r['max_incidence_error']<1e-8:
    print('valid',len(out),a,b,m,r['counts'],r['min_gap'],r['polar_escape_min'],r['primal_escape_min'],flush=True)
    if r['counts']==[1,1,0]:
     name=f'SNAP_E{r["E"]}_{a}_{b}_Q{m}'
     (R/(name+'_GENERATOR.json')).write_text(json.dumps(z,sort_keys=True,separators=(',',':')))
     (R/(name+'_faces.json')).write_text(json.dumps(fs))
     print('NUMERICAL_WINNER',name,flush=True)
  except (AssertionError,ValueError,np.linalg.LinAlgError,StopIteration):pass
(R/'snap_screen.json').write_text(json.dumps(out,indent=2));print('DONE',len(out),flush=True)
