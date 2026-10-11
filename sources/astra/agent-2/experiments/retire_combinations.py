import sys,json,itertools,numpy as np
from gmpy2 import mpq
from retire_current_vertices import screen,ROOT
sys.set_int_max_str_digits(0)
out=ROOT/'artifacts/retire_current/exact_concave_checkpoint1';data=json.loads((out/'single_screen.json').read_text());r=json.loads(open(data['source']).read());X=np.array([[float(mpq(v)) for v in p] for p in r['raw_vertices']]);X-=np.array([float(mpq(v)) for v in r['raw_centroid']]);base=data['baseline'];poss=[row['removed'][0] for row in data['rows'] if row['U']==1 and row['E']<=r['E']];rows=[]
for k in [3,4,5]:
 for gone in itertools.combinations(poss,k):
  ids=[i for i in range(len(X)) if i not in gone];z=screen(X,ids)
  if z['E']>246:continue
  z.update(removed=list(gone),selected=ids,edges_saved=r['E']-z['E'],volume_removed=base['volume']-z['volume'],centroid_norm=float(np.linalg.norm(z['centroid'])));rows.append(z)
rows.sort(key=lambda z:(z['U']!=1,z['E']>245,z['U'],z['S'],z['centroid_norm']));(out/'multiple_screen.json').write_text(json.dumps(dict(source=data['source'],single_U1_candidates=poss,rows=rows),indent=2)+'\n');print('MULTIPLE_BEST',[(z['removed'],z['E'],z['S'],z['U'],z['volume_removed'],z['centroid_norm']) for z in rows[:15]],flush=True)
