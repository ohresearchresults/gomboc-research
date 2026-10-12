from pathlib import Path
from fractions import Fraction as Q
import json,hashlib,sys,collections
import RECONSTRUCT,check_A,check_B,EXTRA
sys.set_int_max_str_digits(0);assert not sys.flags.optimize
R=Path(__file__).resolve().parent

def emit(name,obj):
 blob=json.dumps(obj,sort_keys=True,separators=(',',':')).encode();(R/name).write_bytes(blob);h=hashlib.sha256(blob).hexdigest();print(name,len(blob),h,flush=True);return [len(blob),h]
meta=json.loads((R/'META.json').read_text());g=json.loads((R/'GENERATOR.json').read_text());outs={};raw=RECONSTRUCT.recover(g);outs['RAW.json']=emit('RAW.json',raw);a=check_A.run(raw);b=check_B.run(raw);assert a==b;outs['A.json']=emit('A.json',a);outs['B.json']=emit('B.json',b)
assert [a[k] for k in ['V','E','F']]==meta['VEF'];assert a['counts']==meta['counts'] and a['weak']==[0,0,0];assert a['edge_primitive_zero_count']==a['face_primitive_zero_count']==a['vertex_max_zero_count']==0
ex=EXTRA.finish(a,b);outs['EXTRA.json']=emit('EXTRA.json',ex);P=[list(map(Q,p)) for p in a['raw_vertices']];c=list(map(Q,a['raw_centroid']));root=next(i for i,p in enumerate(P) if p==[0,0,1]);extra=next(i for i in a['unstable_vertices'] if i!=root);pair=next(e for e in a['saddle_edges'] if extra in e);other=pair[0] if pair[1]==extra else pair[1];u=[v-w for v,w in zip(P[extra],c)];d=[v-w for v,w in zip(P[other],P[extra])]
def dot(a,b):return sum(x*y for x,y in zip(a,b))
t=-dot(u,d)/dot(d,d);beta=dot(u,d)**2/(dot(u,u)*dot(d,d));den=10**18;floor=beta.numerator*den//beta.denominator;assert Q(floor,den)<beta<Q(floor+1,den)
summary={k:a[k] for k in ['V','E','F','counts','weak','stable_face_ids','unstable_vertices','saddle_edges','edge_primitive_count','edge_primitive_zero_count','face_primitive_zero_count','vertex_max_zero_count']}
summary.update(volume_float=float(Q(a['ordinary_volume'])),centroid_float=[float(x) for x in c],extra_owners=[i for i,cy in enumerate(a['faces']) if extra in cy],other_owners=[i for i,cy in enumerate(a['faces']) if other in cy],extra_raw=P[extra],other_raw=P[other],saddle_t=t,beta=beta,beta_floor_1e18=floor)
summary=check_A.encode(summary);outs['PAIR.json']=emit('PAIR.json',summary);print(meta['tag']+'_TWO_COMPLETE_EXACT_NONWINNER_AUDITS_PASS',flush=True)
frozen=R/'FROZEN_OUTPUTS.json'
if frozen.exists():assert json.loads(frozen.read_text())==outs;print(meta['tag']+'_SOURCE_ONLY_REPLAY_PASS',flush=True)
else:emit('FROZEN_OUTPUTS.json',outs)
