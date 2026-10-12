from pathlib import Path
from fractions import Fraction as Q
import json,hashlib,sys,collections
sys.set_int_max_str_digits(0);R=Path(__file__).parent
names=['C634_SOC','C636_H213_SOC','C642_GRID6_UNREPAIRED_OWN121','C642_GRID6_REPAIR169','C636_GRID7','C638_H213_GRID7'];rows=[]
def bb(q):q=Q(q);return [abs(q.numerator).bit_length(),q.denominator.bit_length()]
def hh(p):b=p.read_bytes();return dict(bytes=len(b),sha256=hashlib.sha256(b).hexdigest())
for name in names:
 d=R/name;a=json.loads((d/'A.json').read_text());b=json.loads((d/'B.json').read_text());assert a==b;g=json.loads((d/'GENERATOR.json').read_text());raw=json.loads((d/'RAW.json').read_text());ex=json.loads((d/'EXTRA.json').read_text());depth={g['n_supports']:0}
 for i,deps,axes in g['plan']:depth[i]=1+max([depth[j] for j in deps],default=-1)
 row=dict(tag=name,V=a['V'],E=a['E'],F=a['F'],C=2*a['E'],counts=a['counts'],weak=a['weak'],stable_supports=a['stable_face_ids'],unstable_vertices=a['unstable_vertices'],saddles=a['saddle_edges'],S_sizes=[len(a['faces'][i]) for i in a['stable_face_ids']],U_raw=[a['raw_vertices'][i] for i in a['unstable_vertices']],degree_histogram=ex['degree_histogram'],facet_size_histogram=ex['facet_size_histogram'],grid=g['grid'],controls=len(g['controls']),free_parameters=sum(3-len(s[2]) for s in g['plan']),max_depth=max(depth.values()),max_H_integer_bits=max(abs(x).bit_length() for h in raw['H'] for x in h),total_H_integer_bits=sum(abs(x).bit_length() for h in raw['H'] for x in h),max_P_fraction_bits=max(max(bb(x)) for p in a['raw_vertices'] for x in p),total_P_fraction_bits=sum(sum(bb(x)) for p in a['raw_vertices'] for x in p),volume_bits=bb(a['ordinary_volume']),moment_bits=[bb(x) for x in a['raw_first_moments']],centroid_bits=[bb(x) for x in a['raw_centroid']],volume_float=float(Q(a['ordinary_volume'])),moment_floats=[float(Q(x)) for x in a['raw_first_moments']],centroid_floats=[float(Q(x)) for x in a['raw_centroid']],triangles=a['integration_triangle_count'],edge_components=a['edge_primitive_count'],primitive_zeros=[a['face_primitive_zero_count'],a['vertex_max_zero_count'],a['edge_primitive_zero_count']],primal_margin_floor=ex['primal_relative_margin_floor_1e12'],polar_margin_floor=ex['polar_relative_margin_floor_1e12'],hashes={f:hh(d/f) for f in ['GENERATOR.json','RAW.json','A.json','B.json','EXTRA.json','MASS_MOMENTS.json']})
 rows.append(row)
(R/'FINAL_PRIMARY_REPORT.json').write_text(json.dumps(rows,indent=2));print(json.dumps([{k:v for k,v in x.items() if k not in ['hashes','U_raw','degree_histogram','facet_size_histogram']} for x in rows],indent=2))
