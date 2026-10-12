from pathlib import Path
import json,hashlib,sys
import RECONSTRUCT,check_A,check_B,EXTRA
assert not sys.flags.optimize
sys.set_int_max_str_digits(0)
R=Path(__file__).parent

def emit(name,obj):
 b=json.dumps(obj,sort_keys=True,separators=(',',':')).encode();(R/name).write_bytes(b);print(name,len(b),hashlib.sha256(b).hexdigest(),flush=True);return hashlib.sha256(b).hexdigest()
gen=json.loads((R/'GENERATOR.json').read_text());raw=RECONSTRUCT.recover(gen);emit('RAW.json',raw)
a=check_A.run(raw);emit('A.json',a);b=check_B.run(raw);emit('B.json',b);assert a==b
ex=EXTRA.finish(a,b);emit('EXTRA.json',ex)
assert [a[k] for k in ('V','E','F')]==[189,324,137]
assert a['counts']==[1,1,0] and a['weak']==[0,0,0]
assert a['face_primitive_zero_count']==a['edge_primitive_zero_count']==a['vertex_max_zero_count']==0
print('STEADY_COMET_C648_REPAIR44_TWO_EXACT_AUDITS_PASS',flush=True)
print({k:a[k] for k in ('V','E','F','counts','weak','stable_face_ids','unstable_vertices','edge_primitive_count','integration_triangle_count')},flush=True)
