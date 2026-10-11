from pathlib import Path
import sys,json,numpy as np
from numeric import recover,mechanics
R=Path(__file__).parent;gen=Path(sys.argv[1]);fac=Path(sys.argv[2]);prefix=sys.argv[3]
g=json.loads(gen.read_text());fs=json.loads(fac.read_text());X=recover(g);out=[]
for k in range(4,13):
 D=10**k;z=json.loads(json.dumps(g));z['grid']=D;z['controls']=[[int(round(t*D)) for t in row] for row in X]
 try:r=mechanics(recover(z)[:z['n_supports']],fs,tol=1e-12)
 except Exception as ex:print(D,repr(ex),flush=True);continue
 row=dict(D=D,**r);out.append(row);print(D,r,flush=True)
 if r['counts']==[1,1,0] and r['min_gap']>1e-10 and min(r['polar_escape_min'],r['primal_escape_min'])>1e-6:
  name=f'{prefix}_D{D}';(R/(name+'_GENERATOR.json')).write_text(json.dumps(z,sort_keys=True,separators=(',',':')));(R/(name+'_faces.json')).write_text(json.dumps(fs,separators=(',',':')))
(R/(prefix+'_QUANTIZATION.json')).write_text(json.dumps(out,indent=2))
