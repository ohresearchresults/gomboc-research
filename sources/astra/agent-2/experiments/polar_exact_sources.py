"""Actual uniformly filled polar bodies, separately integrated and recensused.
Polarity is taken about the source's exact own centroid. No dual-centroid equality
is assumed; target body receives an independent exact mass/equilibrium audit.
"""
import sys,json,hashlib
from math import lcm,gcd
from pathlib import Path
from gmpy2 import mpq
ROOT=Path(__file__).resolve().parents[1];sys.set_int_max_str_digits(0)
sys.path.insert(0,str(ROOT/'sources/full76/decoded/methods/parent'));import check_B
check_B.Q=mpq
blob=lambda x:json.dumps(x,sort_keys=True,separators=(',',':')).encode()
for arg in sys.argv[1:]:
 src=ROOT/arg;r=json.loads(src.read_text());center=tuple(map(mpq,r['raw_centroid']));H=[]
 for p in r['raw_vertices']:
  z=[mpq(v)-c for v,c in zip(p,center)];d=lcm(*(int(v.denominator) for v in z));row=[int(v*d) for v in z]+[d];gg=gcd(*row);H.append([v//gg for v in row])
 out=src.parent/'polar_own';out.mkdir(exist_ok=False);body={'H':H};(out/'H.json').write_bytes(blob(body));(out/'source.json').write_text(json.dumps(dict(source=str(src),source_sha256=hashlib.sha256(src.read_bytes()).hexdigest(),polar_origin=r['raw_centroid']),indent=2));a=check_B.run(body);(out/'audit.json').write_bytes(blob(a));summ={k:a[k] for k in ['V','E','F','counts','weak','face_primitive_zero_count','vertex_max_zero_count','edge_primitive_zero_count']};summ['audit_sha256']=hashlib.sha256(blob(a)).hexdigest();(out/'summary.json').write_text(json.dumps(summ,indent=2)+'\n');print('EXACT_ACTUAL_POLAR',arg,summ,flush=True)
