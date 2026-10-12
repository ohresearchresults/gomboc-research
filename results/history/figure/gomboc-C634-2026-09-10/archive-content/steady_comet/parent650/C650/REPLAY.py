from pathlib import Path
from itertools import product
from fractions import Fraction as Q
import sys,json,hashlib
assert not sys.flags.optimize
sys.set_int_max_str_digits(0)
import RECONSTRUCT,check_A,check_B,EXTRA
R=Path(__file__).resolve().parent
def canon(x):return json.dumps(x,sort_keys=True,separators=(',',':')).encode()
def emit(name,x):
 b=canon(x);(R/name).write_bytes(b);h=hashlib.sha256(b).hexdigest();print(name,len(b),h,flush=True);return h

def controls():
 tests=[([[1,1,1,1],[1,-1,-1,1],[-1,1,-1,1],[-1,-1,1,1]],[4,4,6],[0,0,0]),([[s if j==i else 0 for j in range(3)]+[1] for i in range(3) for s in [-1,1]],[6,8,12],[0,0,0]),([list(p)+[1] for p in product([-1,1],repeat=3)],[8,6,12],[0,0,0]),([[0,-1,1,1],[0,-5,1,1],[-2,3,-1,1],[2,3,-1,1]],[3,2,3],[0,2,2]),([[-1,0,0,1],[1,0,0,2],[0,-1,0,2],[0,1,0,1],[0,0,-1,1],[0,0,1,1]],[6,8,12],[0,0,0])]
 out=[]
 for H,count,weak in tests:
  a=check_A.run({'H':H});b=check_B.run({'H':H});assert a==b;assert a['counts']==count and a['weak']==weak;out.append({k:a[k] for k in ['V','E','F','counts','weak','ordinary_volume','raw_first_moments','raw_centroid','edge_primitive_zero_count']})
 assert out[-1]['ordinary_volume']=='18' and out[-1]['raw_first_moments']==['9','-9','0'] and out[-1]['raw_centroid']==['1/2','-1/2','0']
 invalid=[[[1,0,0,0],[0,1,0,1],[0,0,1,1],[-1,-1,-1,1]],tests[0][0]+[tests[0][0][0]],[[1,0,0,1],[0,1,0,1],[0,0,1,1],[1,1,1,1]]]
 rejected=0
 for f in [check_A.run,check_B.run]:
  for H in invalid:
   try:f({'H':H})
   except AssertionError:rejected+=1
   else:raise AssertionError('invalid body accepted')
 assert rejected==6
 return {'fixtures':out,'invalid_inputs_rejected':rejected}

meta=json.loads((R/'EXPECTED.json').read_text());data=json.loads((R/'GENERATOR.json').read_text());raw=RECONSTRUCT.recover(data);hd=emit('RAW.json',raw);assert hd==meta['raw_sha256'];a=check_A.run(raw);ha=emit('A.json',a);b=check_B.run(raw);hb=emit('B.json',b);e=EXTRA.finish(a,b);he=emit('EXTRA.json',e);hc=emit('CONTROLS.json',controls());assert [e[k] for k in ['V','E','F']]==meta['VEF'];assert e['counts']==[1,1,0] and e['weak']==[0,0,0];assert e['edge_primitive_zero_count']==e['face_primitive_zero_count']==e['vertex_max_zero_count']==0;assert e['centred_first_moments']==[0,0,0] or e['centred_first_moments']==['0','0','0'];assert e['primal_relative_margin_floor_1e12']>0 and e['polar_relative_margin_floor_1e12']>0
summary={k:e[k] for k in ['V','E','F','C','counts','weak','degree_histogram','facet_size_histogram','stable_input_rows','unstable_vertices','unstable_raw_coordinates','edge_primitive_count','edge_primitive_zero_count','face_primitive_zero_count','vertex_max_zero_count','primal_relative_margin_floor_1e12','polar_relative_margin_floor_1e12']};summary.update(tag=meta['tag'],definition_sha256=hd,audit_A_sha256=ha,audit_B_sha256=hb,extra_sha256=he,controls_sha256=hc,ordinary_volume_float=float(Q(e['ordinary_volume'])),raw_centroid_float=[float(Q(v)) for v in e['raw_centroid']],raw_first_moments_float=[float(Q(v)) for v in e['raw_first_moments']]);emit('SUMMARY.json',summary);print(meta['tag']+'_TWO_INDEPENDENT_COMPLETE_EXACT_AUDITS_PASS',flush=True)

import ARCHITECTURE
emit("ARCHITECTURE.json",ARCHITECTURE.run(data,a))
print(meta["tag"]+"_FULL_EXPOSED_CONTACT_ARCHITECTURE_PASS",flush=True)
