"""Exact scalar enclosures and arithmetic-size accounting for three nonwinners.
The bounds are integer-grid intervals proved by integer/rational comparisons.
No float is used in this verifier.
"""
import json,sys
from pathlib import Path
from fractions import Fraction as Q
from math import isqrt,lcm
sys.set_int_max_str_digits(0)
assert __debug__
SCALE=10**16

def qbits(q):
 q=Q(q);return max(abs(q.numerator).bit_length(),q.denominator.bit_length())

def sqrt_interval(q):
 assert q>0
 k=isqrt(q.numerator*SCALE*SCALE//q.denominator)
 assert Q(k*k,SCALE*SCALE)<=q<Q((k+1)**2,SCALE*SCALE)
 return dict(lower_numerator=k,upper_numerator=k+1,denominator=SCALE,upper_strict=True)

def rational_interval(q):
 k=q.numerator*SCALE//q.denominator
 assert Q(k,SCALE)<=q<Q(k+1,SCALE)
 return dict(lower_numerator=k,upper_numerator=k+1,denominator=SCALE,upper_strict=True)

def load(path):return json.loads(Path(path).read_text(encoding='utf-8'))
def save(path,obj):Path(path).write_text(json.dumps(obj,sort_keys=True,separators=(',',':')),encoding='utf-8')

def inspect(case):
 case=Path(case);a=load(case/'A.json');b=load(case/'B.json');ref=load(case/'REFERENCE.json');ra=load(case/'REFERENCE_AUDIT.json')
 assert (case/'A.json').read_bytes()==(case/'B.json').read_bytes() and a==b
 assert [a[k] for k in ['V','E','F']]==[177,311,136]
 assert a['weak']==ra['weak']==[0,0,0] and ra['counts']==[1,1,0]
 assert a['counts']!=[1,1,0]
 X=[[Q(t) for t in row] for row in a['raw_vertices']];c=list(map(Q,a['raw_centroid']));g=[Q(t,ref['denominator']) for t in ref['numerators']]
 d2=sum((p-q)**2 for p,q in zip(c,g));assert d2>0
 vol=Q(a['ordinary_volume']);assert vol>0
 den=lcm(*(v.denominator for row in X for v in row),*(v.denominator for v in c))
 report=dict(V=177,E=311,F=136,C=622,own_counts=a['counts'],own_weak=a['weak'],reference_counts=ra['counts'],reference_weak=ra['weak'],reference=ref,reference_distance=sqrt_interval(d2),ordinary_volume=rational_interval(vol),centroid_intervals=[rational_interval(t) for t in c],raw_vertex_bits=max(qbits(t) for row in X for t in row),integer_support_bits=max(abs(int(t)).bit_length() for row,d in zip(a['normals'],a['offsets']) for t in row+[d]),centroid_bits=max(qbits(t) for t in c),common_centred_denominator_bits=den.bit_length(),reference_stable_faces=ra['stable_faces'],reference_unstable_vertices=ra['unstable_vertices'],reference_face_primitive_zeros=ra['face_primitive_zero_count'],reference_edge_primitive_zeros=ra['edge_primitive_zero_count'],reference_edge_primitive_count=ra['edge_primitive_count'],independent_own_audits_byte_equal=True)
 return report,d2,vol

def run(root):
 root=Path(root);rows={};values={}
 for name in ['seed','pc3','slsqp3']:
  report,d2,vol=inspect(root/name);rows[name]=report;values[name]=(d2,vol);save(root/name/'STATS.json',report)
 d0,v0=values['seed'];d1,v1=values['pc3'];d2,v2=values['slsqp3']
 assert 0<d2<d1<d0 and v1>v0 and v2<v0
 assert 64*d2<9*d0 # distance_final/distance_seed < 3/8
 normalized_sixth_ratio=(d2/d0)**3*(v0/v2)**2
 assert normalized_sixth_ratio<Q(3,8)**6
 assert Q(998,1000)<v2/v0<Q(999,1000)
 out=dict(status='EXACT_NONWINNER_REFERENCE_DISTANCE_COMPARISON_PASS',records=rows,distance_final_over_seed=sqrt_interval(d2/d0),distance_reduction_strictly_greater_than='5/8',final_over_seed_volume=rational_interval(v2/v0),middle_volume_greater_than_seed=True,final_volume_less_than_seed=True,scale_normalized_distance_reduction_strictly_greater_than='5/8',scale_normalized_ratio_sixth_power=rational_interval(normalized_sixth_ratio),no_centroid_closure=True,all_C=622,not_a_gomboc_record=True)
 save(root/'COMPARISON.json',out);return out
if __name__=='__main__':
 out=run(sys.argv[1]);print(out['status'])
