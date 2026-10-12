"""Finish the exact nonwinner certificate for the rational opposite-point hull.
Requires augment_exact.py and the already preserved FOUR_FRONTIERS core.
Usage: python -B -S verify_opposite.py CORE_DIRECTORY C592_PROOF OPPOSITE_PROOF
"""
import hashlib,json,sys
from fractions import Fraction as Q
from pathlib import Path
import augment_exact as ag
assert __debug__
sys.set_int_max_str_digits(0)
B=ag.B;SHA=ag.SHA
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def bits(x):return max(abs(x.numerator).bit_length(),x.denominator.bit_length())
def run(core,parent,out):
 sys.path.insert(0,str(core));import centred_mass
 aa=(out/'A.json').read_bytes();bb=(out/'B.json').read_bytes();assert aa==bb
 A=json.loads(aa);pa=(parent/'A.json').read_bytes();assert SHA(pa)==ag.CHILD
 P=json.loads(pa);pb=(parent/'PARENT_A.json').read_bytes()
 assert SHA(pb)=='2426da394eda9520bd30b2b8b3e1f00d043697353bb6bc73658f5983653c11ec'
 c0=tuple(map(Q,json.loads(pb)['raw_centroid']));c=tuple(map(Q,A['raw_centroid']))
 points=[tuple(map(Q,p)) for p in P['raw_vertices']]
 a=tuple(Q(x,ag.D) for x in ag.TRIAL);points.append(a)
 assert Q(17,20)<=a[0]<=Q(9,10) and Q(43,100)<=a[1]<=Q(47,100) and Q(-57,100)<=a[2]<=Q(-27,50)
 vertices=[tuple(map(Q,p)) for p in A['raw_vertices']]
 assert set(vertices)<=set(points)
 assert (A['V'],A['E'],A['F'])==(118,243,127)
 assert A['active_input_indices']==list(range(127))
 assert A['counts']==[7,2,7] and A['weak']==[0,0,0]
 rows=json.loads((out/'raw.json').read_text())['H']
 assert all(ag.dot(row[:3],p)<=row[3] for p in points for row in rows)
 mapping=[points.index(x) for x in vertices]
 r=(Q(0),Q(0),Q(1));assert points[81]==r
 assert A['unstable_vertices']==[vertices.index(r),vertices.index(a)]
 assert max(map(abs,c0))<=Q(1,50)
 r2=ag.dot(sub(r,c0),sub(r,c0));rho=Q(1,1000)
 for x in points[:-1]:
  if x==r:continue
  e=sub(x,r);delta=-ag.dot(sub(r,c0),e)
  assert delta>0 and ag.dot(sub(x,c0),sub(x,c0))<r2
  rho=min(rho,delta/(2*sum(map(abs,e))))
 error=max(map(abs,sub(c,c0)));assert error<rho and error<Q(1,10**12)
 mass=centred_mass.run(A);(out/'MASS.json').write_bytes(B(mass))
 assert mass['filled_first_moments']==[0,0,0]
 small=dict(identity='COORD_C592_OPPOSITE_POINT_R12',C=486,V_E_F=[118,243,127],counts=A['counts'],weak=A['weak'],input_domain='C592 raw-lex vertices0..162 followed by opposite point163',raw_lex_to_input=mapping,hidden_C592_raw_lex=sorted(set(range(163))-set(mapping)),strict_U_raw_lex=A['unstable_vertices'],strict_U_inputs=[mapping[i] for i in A['unstable_vertices']],stable_facet_ids=A['stable_face_ids'],saddle_edges=A['saddle_edges'],target_centroid_is_C602_own_centroid=True,actual_centroid_equals_target=(error==0),actual_centroid_inf_error_lt_1_over_10pow12=True,actual_centroid_within_two_U_radius=True,raw_halfspace_max_bits=max(abs(v).bit_length() for row in rows for v in row),raw_vertex_max_bits=max(bits(x) for p in vertices for x in p),raw_centroid_max_bits=max(map(bits,c)),common_centred_denominator_bits=mass['common_centred_denominator_bits'],centred_vertex_max_bits=max(bits(x-g) for p in vertices for x,g in zip(p,c)),volume_bits=bits(Q(A['ordinary_volume'])),first_moments_max_bits=max(bits(Q(x)) for x in A['raw_first_moments']),new_winner=False)
 small['outputs']={name:dict(bytes=(out/name).stat().st_size,sha256=SHA((out/name).read_bytes())) for name in ['raw.json','SELECTORS.json','A.json','B.json','MASS.json']}
 (out/'RECEIPT.json').write_bytes(B(small))
 print('EXACT_RATIONAL_OPPOSITE_C486_OWN727_TWO_AUDITS_PASS',SHA(B(small)),flush=True)
 print(json.dumps({k:v for k,v in small.items() if k not in ['raw_lex_to_input','hidden_C592_raw_lex','outputs']},sort_keys=True))
if __name__=='__main__':run(*map(Path,sys.argv[1:]))
