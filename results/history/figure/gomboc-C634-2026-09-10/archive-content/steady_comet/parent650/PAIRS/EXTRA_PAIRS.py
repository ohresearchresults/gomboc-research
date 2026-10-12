"""Exact identities and rational barrier brackets for two NONWINNERS."""
from fractions import Fraction as Q
from pathlib import Path
from collections import Counter
import hashlib,json,sys
sys.set_int_max_str_digits(0)
def summarize(drop,folder='.'):
 base=Path(folder);aa=(base/f'A_{drop}.json').read_bytes();bb=(base/f'B_{drop}.json').read_bytes();assert aa==bb
 a=json.loads(aa);assert (a['V'],a['E'],a['F'],a['counts'],a['weak'])==(189,323,136,[1,2,1],[0,0,0])
 x=[list(map(Q,p)) for p in a['raw_vertices']];g=list(map(Q,a['raw_centroid']));root=next(i for i,p in enumerate(x) if p==[Q(0),Q(0),Q(1)]);u=next(i for i in a['unstable_vertices'] if i!=root);h=a['saddle_edges'][0];assert u in h;j=next(k for k in h if k!=u)
 dot=lambda a,b:sum(s*t for s,t in zip(a,b))
 y=[s-c for s,c in zip(x[u],g)];e=[s-t for s,t in zip(x[j],x[u])];t=-dot(y,e)/dot(e,e);assert 0<t<1
 barrier=dot(y,e)**2/(dot(e,e)*dot(y,y));lo=int(barrier*10**12);assert Q(lo,10**12)<barrier<Q(lo+1,10**12)
 assert lo=={102:1265676705,120:1591788057}[drop]
 owners=[a['active_input_indices'][i] for i,cy in enumerate(a['faces']) if u in cy];orig=[i+(i>=drop) for i in owners]
 assert orig=={102:[47,84,103],120:[58,97,121]}[drop]
 assert a['active_input_indices']==list(range(136));assert a['edge_primitive_count']==1292 and a['edge_primitive_zero_count']==0
 degrees=Counter(i for edge in a['edges'] for i in edge);assert sorted(Counter(degrees.values()).items())==[(3,155),(4,28),(5,5),(44,1)]
 assert degrees[root]==44 and len(a['faces'][a['stable_face_ids'][0]])==21
 assert a['active_input_indices'][a['stable_face_ids'][0]]==3
 out={'drop':drop,'V':a['V'],'E':a['E'],'F':a['F'],'counts':a['counts'],'weak':a['weak'],'root':root,'extra_U':u,'H':h,'U_owners_original':orig,'barrier_floor_1e12':lo,'barrier_ceiling_1e12':lo+1,'volume_float':float(Q(a['ordinary_volume'])),'centroid_float':[float(v) for v in g],'stable_face_vertices':21,'edge_zeros':0,'raw_sha256':hashlib.sha256((base/f'RAW_{drop}.json').read_bytes()).hexdigest(),'canonical_sha256':hashlib.sha256(aa).hexdigest()}
 (base/f'SUMMARY_{drop}.json').write_text(json.dumps(out,sort_keys=True,separators=(',',':')))
 return out
if __name__=='__main__':
 for drop in (102,120):print(summarize(drop))
