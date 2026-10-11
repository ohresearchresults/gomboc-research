"""Exact rational bit-length diagnostics; no floating computations."""
import sys,json,math
from fractions import Fraction as F
from pathlib import Path
sys.set_int_max_str_digits(0)
def run(root):
 out={}
 for name,p in [('C598',root/'C598_A.json'),('COORD_C598_F114_LAMBDA005_G14_C612',root/'FACET_CHECKPOINT_1/A.json'),('COORD_C598_F114_TARGET_G14_C664',root/'FACET_CHECKPOINT_20/A.json')]:
  a=json.loads(p.read_text());X=[F(v) for row in a['raw_vertices'] for v in row];g=list(map(F,a['raw_centroid']));first=list(map(F,a['raw_first_moments']));volume=F(a['ordinary_volume']);bits=lambda vv:max(max(abs(v.numerator).bit_length(),v.denominator.bit_length()) for v in vv)
  d=math.lcm(*(v.denominator for v in X+g))
  out[name]={'V_E_F':[a[k] for k in ['V','E','F']],'counts':a['counts'],'weak':a['weak'],'max_primitive_plane_bits':max(abs(v).bit_length() for row,h in zip(a['normals'],a['offsets']) for v in [*row,h]),'max_raw_vertex_fraction_bits':bits(X),'raw_centroid_fraction_bits':bits(g),'volume_fraction_bits':bits([volume]),'raw_first_moment_fraction_bits':bits(first),'common_centred_denominator_bits':d.bit_length()}
 return out
if __name__=='__main__':
 root=Path(sys.argv[1]);b=json.dumps(run(root),sort_keys=True,separators=(',',':'));(root/'ARITHMETIC_REPORT.json').write_text(b);print('ONE_FACET_EXACT_ARITHMETIC_STATS_PASS')
