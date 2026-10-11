from pathlib import Path
from fractions import Fraction as Q
from math import gcd
import json,hashlib,sys,collections
import RECONSTRUCT,check_A,check_B,EXTRA
assert not sys.flags.optimize
sys.set_int_max_str_digits(0)
R=Path(__file__).resolve().parent

def emit(name,obj):
    blob=json.dumps(obj,sort_keys=True,separators=(',',':')).encode();(R/name).write_bytes(blob)
    h=hashlib.sha256(blob).hexdigest();print(name,len(blob),h,flush=True);return [len(blob),h]
meta=json.loads((R/'META.json').read_text());g=json.loads((R/'GENERATOR.json').read_text())
outputs={};raw=RECONSTRUCT.recover(g);outputs['RAW.json']=emit('RAW.json',raw)
a=check_A.run(raw);outputs['A.json']=emit('A.json',a)
b=check_B.run(raw);outputs['B.json']=emit('B.json',b);assert a==b
assert [a[k] for k in ['V','E','F']]==meta['VEF']
assert a['counts']==[1,1,0] and a['weak']==[0,0,0]
assert a['face_primitive_zero_count']==a['vertex_max_zero_count']==a['edge_primitive_zero_count']==0
assert a['active_input_indices']==list(range(137))
assert a['stable_face_ids']==[3]
assert len(a['unstable_vertices'])==1 and list(map(Q,a['raw_vertices'][a['unstable_vertices'][0]]))==[0,0,1]
ex=EXTRA.finish(a,b);outputs['EXTRA.json']=emit('EXTRA.json',ex)
ef=collections.defaultdict(list)
for i,cy in enumerate(a['faces']):
    for v,w in zip(cy,cy[1:]+cy[:1]):ef[tuple(sorted((v,w)))].append(i)
pol={tuple(sorted(v)) for v in ef.values()};H=set(tuple(e) for e in meta['H213_edges']);G=set(tuple(e) for e in meta['G650_edges'])
assert pol<=G and len(pol)==a['E']
if meta.get('require_H213',True):assert H<=pol
depth={137:0}
for i,deps,axes in g['plan']:depth[i]=1+max([depth[j] for j in deps],default=-1)
def bits(t):
    q=Q(t);return [abs(q.numerator).bit_length(),q.denominator.bit_length()]
cx=dict(controls=len(g['controls']),grid=g['grid'],free_parameters=sum(3-len(t[2]) for t in g['plan']),max_reconstruction_depth=max(depth.values()),H_integer_max_bits=max(abs(t).bit_length() for r in raw['H'] for t in r),P_coordinate_max_bits=max(max(bits(x)) for p in a['raw_vertices'] for x in p),volume_bits=bits(a['ordinary_volume']),moment_bits=[bits(v) for v in a['raw_first_moments']],centroid_bits=[bits(v) for v in a['raw_centroid']],definition_bytes=(R/'GENERATOR.json').stat().st_size,raw_integer_bytes=(R/'RAW.json').stat().st_size,removed_polar_edges=sorted(G-pol),missing_H213_edges=sorted(H-pol),added_to_H213_edges=sorted(pol-H))
outputs['DESCRIPTION.json']=emit('DESCRIPTION.json',cx)
summary={k:a[k] for k in ['V','E','F','counts','weak','stable_face_ids','unstable_vertices','edge_primitive_count','edge_primitive_zero_count','face_primitive_zero_count','vertex_max_zero_count','integration_triangle_count']}
summary.update(C=2*a['E'],volume_float=float(Q(a['ordinary_volume'])),centroid_float=[float(Q(v)) for v in a['raw_centroid']],moments_float=[float(Q(v)) for v in a['raw_first_moments']],degree_histogram=ex['degree_histogram'],facet_size_histogram=ex['facet_size_histogram'],primal_relative_margin_floor_1e12=ex['primal_relative_margin_floor_1e12'],polar_relative_margin_floor_1e12=ex['polar_relative_margin_floor_1e12'])
outputs['SUMMARY.json']=emit('SUMMARY.json',summary)
print(meta['tag']+'_TWO_EXHAUSTIVE_INDEPENDENT_EXACT_AUDITS_PASS',flush=True)
print(summary,flush=True)
frozen=R/'FROZEN_OUTPUTS.json'
if frozen.exists():
    assert json.loads(frozen.read_text())==outputs
    print(meta['tag']+'_SOURCE_ONLY_REPLAY_SIX_OUTPUTS_MATCH_PASS',flush=True)
else:emit('FROZEN_OUTPUTS.json',outputs)
