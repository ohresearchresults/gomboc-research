"""Finite RL leaf contact on the exact BQ13 stable-cap C626 chart.
Numerical proposal only; the frozen rational generator requires full exact audits.
Usage: combine.py BQ13_SOURCE fresh_output [axis]
"""
import json,sys
from pathlib import Path
import numpy as np
base=Path(sys.argv[1]).resolve();out=Path(sys.argv[2]);axis=int(sys.argv[3]) if len(sys.argv)>3 else 2
sys.path[:0]=[str(base/'parent/mechanism'),str(base/'parent/mechanism/parent_sources')]
from numeric import recover,merge_faces,mechanics,topology
src=base/'BASIN69_96';d=json.loads((src/'GENERATOR.json').read_text());fs=json.loads((src/'faces.json').read_text());X=recover(d);own,ef=topology(fs)
a=own.index([16,18,94]);b=own.index([18,71,94]);assert tuple(sorted((a,b))) in ef
assert [i for i,deps,axes in d['plan'] if 18 in deps]==[]
assert [18,[],[]] in d['plan'];d['plan'].remove([18,[],[]])
p=np.linalg.solve(X[[16,71,94]],np.ones(3));q=X[18];q=q+(1-q@p)/(p@p)*p
idx=len(d['controls']);assert idx==d['n_supports']+len(d['groups'])
d['controls'][18]=np.rint(q*d['grid']).astype(np.int64).tolist();d['controls'].append(np.rint(p*d['grid']).astype(np.int64).tolist());d['groups'].append([16,18,71,94]);d['plan'] += [[idx,[16,71,94],[0,1,2]],[18,[idx],[axis]]]
nf=merge_faces(fs,a,b);out.mkdir(parents=True,exist_ok=False)
for name,obj in [('GENERATOR.json',d),('faces.json',nf)]: (out/name).write_text(json.dumps(obj,sort_keys=True,separators=(',',':')))
r=mechanics(recover(d)[:137],nf,tol=1e-12);(out/'NUMERICAL.json').write_text(json.dumps(r,indent=2));print('SEED',a,b,'axis',axis,'delta18',np.linalg.norm(recover(d)[18]-X[18]),r,flush=True)
