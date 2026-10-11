"""Optional numerical reproduction; exact replay has no numerical dependency."""
import json,sys,subprocess
from pathlib import Path
root=Path(__file__).resolve().parent
job,base,out=sys.argv[1:];base=Path(base);out=Path(out)
if job=='mass_roots':cmd=['ROOT_DISCOVERY.py',base,out]
elif job=='null99':cmd=['cap_null_search.py',base/'DEL99/B.json','99','129,145','15',out]
elif job=='forest99':cmd=['cluster_search.py',base/'DEL99/B.json','99','129,145','20',out]
elif job=='three_compensated_slides':
 import numpy as np
 from compensate import Compensated
 out.mkdir(exist_ok=False)
 for j,u,w in [(99,145,146),(117,81,84),(84,175,174)]:
  m=Compensated(base/f'DEL{j}/B.json',j,u,w);z=np.zeros(3);rows=[]
  for s in [1e-6,1e-5,.0001,.001,.01,.05,.1,.2,.4,.6,.8,.99]:
   r=m.close(s,z);rows.append(r)
   if r['com_error']<1e-10:z=np.array(r['eta'])
  (out/f'{j}.json').write_text(json.dumps(rows,sort_keys=True))
 print('FINITE_36_OWN_MASS_CLOSED_SAMPLES_FINISHED');raise SystemExit(0)
else:raise SystemExit('jobs: mass_roots, null99, forest99, three_compensated_slides')
subprocess.run([sys.executable,str(root/cmd[0]),*map(str,cmd[1:])],check=True)
