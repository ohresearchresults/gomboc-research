#!/usr/bin/env python3
from pathlib import Path
import sys,json,csv
from fractions import Fraction as Q
import numpy as np
SRC=Path('/mnt/data/m42_fourth_work')
sys.path[:0]=[str(SRC),str(SRC/'parent')]
import search_lobe_prism as S
from numeric_hull_proposer import evaluate,score_target
x=np.array(json.load(open(SRC/'lobe911_robust_x.json'))['x'],float)
p=S.build(x,0); assert p is not None
D=10**12
rows={i:tuple(int(round(float(z)*D)) for z in q) for i,q in p.items()}
q={i:np.array([z/D for z in a]) for i,a in rows.items()}
r=evaluate(q,plane_tol=5e-8,strict_tol=1e-10)
assert r.valid,r.error
print('ROUNDED',len(rows),'active',len(r.active),'E/F',len(r.edges),len(r.faces),'class',len(r.stable),len(r.unstable),len(r.saddles),'centroid',r.centroid,'volume',r.volume)
print('stable',[(r.faces[i]['cycle'],z) for i,z in r.stable]);print('unstable',r.unstable);print('saddles',r.saddles);print('score',score_target(r))
with open(Path(__file__).parent/'input_rows_lattice.csv','w',newline='') as f:
 w=csv.writer(f);w.writerow(['source_id','x_int','y_int','z_int','denominator','lineage'])
 for i in sorted(rows):
  lin='parent_transformed'
  if i in S.ABSORB:lin='absorbed_parent_packet'
  elif 223<=i<=225:lin='prism_near_section'
  elif 226<=i<=228:lin='prism_far_section'
  w.writerow([i,*rows[i],D,lin])
json.dump({'version':1,'source':'exact rounding of robust lobe candidate','search_parameters':x.tolist(),'denominator':D,'absorbed_rows':sorted(S.ABSORB),'new_rows':list(range(223,229))},open(Path(__file__).parent/'construction.json','w'),indent=2)
