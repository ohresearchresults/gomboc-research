from pathlib import Path
from fractions import Fraction as Q
from itertools import product
import sys,json,hashlib,math
assert not sys.flags.optimize
sys.set_int_max_str_digits(0)
import audit_A,dual_A,dual_B,exact_extra
R=Path(__file__).resolve().parent
def canon(x):return json.dumps(x,sort_keys=True,separators=(',',':')).encode()
def emit(name,x):
 b=canon(x);(R/name).write_bytes(b);h=hashlib.sha256(b).hexdigest();print(name,len(b),h,flush=True);return h
def controls():
 specs=[({'I':[[1,1,1],[1,-1,-1],[-1,1,-1],[-1,-1,1]],'D':1},[4,4,6],[0,0,0]),({'I':list(map(list,product((-1,1),repeat=3))),'D':1},[8,6,12],[0,0,0]),({'I':[[1,0,0],[-1,0,0],[0,1,0],[0,-1,0],[0,0,1],[0,0,-1]],'D':1},[6,8,12],[0,0,0])]
 w=[[-1,0,1],[1,0,1],[0,1,2],[0,-1,-4]];wa=audit_A.exact_audit(w,1);pp=[tuple(Q(x,h) for x in n) for *n,h in wa['primitive_support_planes']];dd=math.lcm(*(x.denominator for p in pp for x in p));specs.append(({'I':[[int(x*dd) for x in p] for p in pp],'D':dd},[3,2,3],[0,2,2]))
 out=[]
 for raw,count,weak in specs:
  raw['scale']=1;aa=dual_A.run(raw);bb=dual_B.run(raw)
  for k in aa:
   if k!='triangles':assert aa[k]==bb[k],k
  assert aa['counts']==count and aa['weak']==weak
  out.append({'VEF':[aa[k] for k in ['V','E','F']],'counts':count,'weak':weak})
 rejected=0
 for fun in (dual_A.run,dual_B.run):
  for obj in ({'I':specs[0][0]['I'],'D':0},{'I':specs[0][0]['I']+[specs[0][0]['I'][0]],'D':1}):
   try:fun(obj)
   except AssertionError:rejected+=1
   else:raise AssertionError('Invalid input accepted')
 assert rejected==4
 return {'fixtures':out,'invalid_inputs_rejected':rejected}
raw=json.loads((R/'RAW.json').read_text())
assert hashlib.sha256((R/'RAW.json').read_bytes()).hexdigest()=='f5d1d6a9c23cbd89b0d7185971c1d1ac6c384190a50949c4681cbaba2ecf7016'
a=dual_A.run(raw);ha=emit('A.json',a)
b=dual_B.run(raw);hb=emit('B.json',b)
e=exact_extra.extras(raw,a,b);he=emit('EXTRA.json',e)
assert [e[k] for k in ['V','E','F']]==[235, 373, 140]
assert e['counts']==[1,1,0] and e['weak']==[0,0,0]
assert e['edge_primitive_count']==1492 and e['edge_primitive_zero_count']==0
assert e['centred_first_moments']==['0','0','0']
assert not e['whole_boundary_sublevels']['finite_bars']
assert e['primal_forest']['min_relative_dot_floor_1e12'] > 0
assert e['polar_forest']['min_relative_dot_floor_1e12'] > 0
assert e['V']+e['E']+e['F']-2==746
hc=emit('CONTROLS.json',controls())
summary={'tag':'COORD_FLOW_H140_C746_D100000000','VEF':[e[k] for k in ['V','E','F']],'counts':e['counts'],'weak':e['weak'],'definition_sha256':'f5d1d6a9c23cbd89b0d7185971c1d1ac6c384190a50949c4681cbaba2ecf7016','audit_A_sha256':ha,'audit_B_sha256':hb,'extra_sha256':he,'controls_sha256':hc,'stable_face_ids':e['stable_face_ids'],'stable_faces':e['stable_faces'],'unstable_vertices':e['unstable_vertices'],'saddle_edges':e['saddle_edges'],'bar_floor_1e12':[v['bar_floor_1e12'] for v in e['whole_boundary_sublevels']['finite_bars']],'primal_margin_floor_1e12':e['primal_forest']['min_relative_dot_floor_1e12'],'polar_margin_floor_1e12':e['polar_forest']['min_relative_dot_floor_1e12'],'raw_centroid_float':[float(Q(v)) for v in e['raw_centroid']],'volume_float':float(Q(e['ordinary_volume'])),'edge_primitive_count':e['edge_primitive_count'],'zero_primitives':e['edge_primitive_zero_count']}
emit('SUMMARY.json',summary)
print('COORD_FLOW_H140_C746_D100000000_TWO_INDEPENDENT_FULL_AUDITS_SUBLEVELS_FORESTS_CONTROLS_COLD_GOMBOC_PASS',flush=True)
