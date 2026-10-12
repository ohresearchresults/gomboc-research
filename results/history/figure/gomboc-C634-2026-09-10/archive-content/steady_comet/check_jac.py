from pathlib import Path
import json,numpy as np,time
from numeric import *
from atlas_opt import *
R=Path(__file__).parent;d=json.loads((R/'parent650/C650/GENERATOR.json').read_text());faces=json.loads((R/'parent650/C650/A.json').read_text())['faces']
m=Atlas(d,faces);t=time.time();s=m.state(m.u0);print('eval',time.time()-t,'n',m.np, 'min',s['vals'].min(),flush=True)
rng=np.random.default_rng(123);v=rng.normal(size=m.np);v/=np.linalg.norm(v);eps=1e-7
sp=m.state(m.u0+eps*v,False);sm=m.state(m.u0-eps*v,False)
for label,truth,approx in [('chart',np.einsum('icp,p->ic',m.chart(m.u0)[1],v),(sp['X']-sm['X'])/(2*eps)),('centroid',s['dc']@v,(sp['c']-sm['c'])/(2*eps)),('escape',s['J']@v,(sp['vals']-sm['vals'])/(2*eps))]:
 print(label,np.max(abs(truth-approx)),np.max(abs(truth)),flush=True)
for a,b,move in [(148,151,45),(146,148,44),(137,142,70),(164,188,86)]:
 z,fs=snapped(d,faces,a,b,move);name=f'SNAP_{a}_{b}_{move}';(R/(name+'_GENERATOR.json')).write_text(json.dumps(z,sort_keys=True,separators=(',',':')));(R/(name+'_faces.json')).write_text(json.dumps(fs))
 mm=Atlas(z,fs);ss=mm.state(mm.u0);ix=np.argmin(ss['vals']);print(name,ss['vals'].min(),('S',mm.si[ix]) if ix<len(mm.si) else ('U',mm.ui[ix-len(mm.si)]),flush=True)
