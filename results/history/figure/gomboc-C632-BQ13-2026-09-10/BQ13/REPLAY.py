"""Full exact reconstruction and independent maximal-complex/mechanical replay.
Run with Python 3.11+ standard library, never with -O.
"""
import sys,json,hashlib,time,argparse
from pathlib import Path
from fractions import Fraction as F
from math import gcd
sys.set_int_max_str_digits(0)
if not __debug__:raise RuntimeError('Assertions are essential; do not use -O.')
ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT))
import RECONSTRUCT,check_A,check_B,endpoint_stats,centred_mass

def canon(x):return json.dumps(x,sort_keys=True,separators=(',',':')).encode()
def digest(x):return hashlib.sha256(x).hexdigest()
def manifest():
 p=ROOT/'SOURCE_MANIFEST.json'
 if p.exists():
  entries=json.loads(p.read_text())
  for name,h in entries.items():assert digest((ROOT/name).read_bytes())==h,('source changed',name)
  return len(entries)
 return 0

def fixtures():
 cases=[('regular_tetrahedron',{'H':[[-1,-1,-1,1],[-1,1,1,1],[1,-1,1,1],[1,1,-1,1]]},[4,4,6],[0,0,0]),('weak_triangular_prism',{'H':[[1,0,0,1],[-2,3,0,1],[1,-3,0,1],[0,0,1,1],[0,0,-1,1]]},[4,4,6],[1,2,3])]
 receipts=[]
 for name,raw,counts,weak in cases:
  a=check_A.run(raw);b=check_B.run(raw);assert a==b and a['counts']==counts and a['weak']==weak
  assert not (counts==[1,1,0] and weak==[0,0,0])
  receipts.append({'name':name,'VEF':[a[k] for k in ('V','E','F')],'counts':counts,'weak':weak,'winner_gate_rejects':True})
 for raw in ({'H':[[1,0,0,-1]]*4},{'H':[[1,0,0,1]]*4}):
  for engine in (check_A,check_B):
   try:engine.run(raw)
   except (AssertionError,ValueError):pass
   else:raise AssertionError('Malformed fixture was accepted')
 return receipts

def run(name,out,translation=False,phase='all',baseline=None):
 if phase in ('all','A'):
  assert not out.exists(),('output must be absent',out)
  out.mkdir(parents=True)
 else:assert out.is_dir()
 before=manifest();spec=json.loads((ROOT/'OBJECTS.json').read_text())[name]
 data=(ROOT/'objects'/name/'GENERATOR.json').read_bytes();assert digest(data)==spec['generator_sha256']
 raw=RECONSTRUCT.recover(json.loads(data));deletes=set(spec['delete_supports']);raw={'H':[r for i,r in enumerate(raw['H']) if i not in deletes]}
 (out/'GENERATOR.json').write_bytes(data);(out/'raw.json').write_bytes(canon(raw));(out/'DELETE.json').write_bytes(canon(sorted(deletes)))
 original=None
 if translation:
  if phase in ('all','A'):
   original=json.loads(baseline.read_text()) if baseline else check_A.run(raw)
   assert digest(canon(original))==spec['normalized_output_sha256']
   (out/'ORIGINAL_A.json').write_bytes(canon(original))
  else:original=json.loads((out/'ORIGINAL_A.json').read_text());assert digest(canon(original))==spec['normalized_output_sha256']
  d=2**30;t=(F(1,d),F(-2,d),F(3,d));HH=[]
  for x,y,z,h in raw['H']:
   r=[d*x,d*y,d*z,d*h+x-2*y+3*z];g=gcd(*r);r=[v//g for v in r];assert r[-1]>0;HH.append(r)
  raw={'H':HH};(out/'translated_raw.json').write_bytes(canon(raw))
 for label,engine in [('A',check_A),('B',check_B)]:
  if phase not in ('all',label):continue
  start=time.perf_counter();a=engine.run(raw);elapsed=time.perf_counter()-start
  body=canon(a);(out/(label+'.json')).write_bytes(body)
  assert [a[k] for k in ('V','E','F')]==spec['VEF'] and a['counts']==spec['counts'] and a['weak']==spec['weak']
  assert a['active_input_indices']==list(range(a['F']))
  assert a['face_primitive_zero_count']==a['vertex_max_zero_count']==a['edge_primitive_zero_count']==0
  assert a['centred_first_moments']==a['centred_centroid']==[0,0,0]
  if not translation:assert digest(body)==spec['normalized_output_sha256']
  receipt={'engine':label,'seconds':elapsed,'record_sha256':digest(body),'generator_sha256':digest(data),'VEF':spec['VEF'],'counts':a['counts'],'weak':a['weak']}
  (out/(label+'_RECEIPT.json')).write_bytes(canon(receipt))
  print(label,name,a['V'],a['E'],a['F'],a['counts'],a['weak'],digest(body),flush=True)
 if phase in ('A','B'):
  assert manifest()==before
  return
 records=[json.loads((out/(k+'.json')).read_text()) for k in ('A','B')]
 rr=[json.loads((out/(k+'_RECEIPT.json')).read_text()) for k in ('A','B')]
 for k,a,r in zip(('A','B'),records,rr):
  assert r['engine']==k and r['record_sha256']==digest(canon(a)) and r['generator_sha256']==digest(data)
  if not translation:assert digest(canon(a))==spec['normalized_output_sha256']
 assert records[0]==records[1];a=records[0]
 if translation:
  assert original['ordinary_volume']==a['ordinary_volume']
  c=list(map(F,a['raw_centroid']));g=list(map(F,original['raw_centroid']))
  assert all(c[k]-g[k]==t[k] for k in range(3))
  for p,q in zip(a['raw_vertices'],original['raw_vertices']):assert all(F(p[k])-c[k]==F(q[k])-g[k] for k in range(3))
 elif name=='C632_WINNER':
  s=endpoint_stats.run(a,raw);(out/'STATS.json').write_bytes(canon(s))
  im=centred_mass.run(a);(out/'CENTRED_MASS.json').write_bytes(canon(im))
 fs=fixtures();after=manifest();assert before==after
 receipt={'status':'BQ13_EXACT_TRANSLATION_REPLAY_PASS' if translation else 'BQ13_EXACT_TWO_IMPLEMENTATION_REPLAY_PASS','object':name,'VEF':spec['VEF'],'counts':a['counts'],'weak':a['weak'],'source_manifest_files':before,'normalized_records_identical':True,'normalized_record_sha256':digest(canon(a)),'seconds':{r['engine']:r['seconds'] for r in rr},'fixtures':fs,'python':sys.version}
 (out/'RECEIPT.json').write_bytes(canon(receipt));print(receipt['status'],flush=True)
 return receipt
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--object',default='C632_WINNER',choices=['C630_START','C622_DISK','C622_READY','C632_WINNER']);p.add_argument('--out',required=True,type=Path);p.add_argument('--translation-fixture',action='store_true');p.add_argument('--phase',default='all',choices=['all','A','B','finish']);p.add_argument('--baseline',type=Path);a=p.parse_args();run(a.object,a.out,a.translation_fixture,a.phase,a.baseline)
