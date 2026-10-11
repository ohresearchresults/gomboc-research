"""Exact ties-to-even grid coarsening, then full floating census (not certification)."""
import sys,json,os
from fractions import Fraction as F
from pathlib import Path
BASE=Path(os.environ['BQ13_SOURCE']).resolve();sys.path.insert(0,str(BASE/'parent/mechanism/parent_sources'))
from numeric import recover,mechanics
src=Path(sys.argv[1]);out=Path(sys.argv[2]);d=json.loads((src/'GENERATOR.json').read_text());fs=json.loads((src/'faces.json').read_text());old=d['grid'];rows=[]
for k in range(6,13):
 z=json.loads(json.dumps(d));D=10**k;z['grid']=D;z['controls']=[[round(F(v*D,old)) for v in row] for row in d['controls']]
 r=mechanics(recover(z)[:137],fs,tol=1e-12)
 p=out/f'G{k}';p.mkdir(parents=True,exist_ok=False)
 for f,o in [('GENERATOR.json',z),('faces.json',fs),('NUMERICAL.json',r)]: (p/f).write_text(json.dumps(o,sort_keys=True,separators=(',',':')))
 print('G',k,r['counts'],r['min_gap'],r['max_incidence_error'],r['polar_escape_min'],r['primal_escape_min'],flush=True)
 rows.append({'grid_exponent':k,**r})
(out/'GRID_SCREEN.json').write_text(json.dumps(rows,indent=2))
