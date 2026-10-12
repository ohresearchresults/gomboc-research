"""Source-only exact reconstruction and two full independent audits.
No numerical-library dependency. Do not disable assertions.
"""
import sys,json,hashlib,time,argparse
from pathlib import Path
if not __debug__:raise RuntimeError('Run without -O')
sys.set_int_max_str_digits(0)
R=Path(__file__).resolve().parent;sys.path.insert(0,str(R/'parent'))
import RECONSTRUCT,check_A,check_B,centred_mass
import measure626,compare626

def canon(x):return json.dumps(x,sort_keys=True,separators=(',',':')).encode()
def sha(b):return hashlib.sha256(b).hexdigest()
def sources():
 m=json.loads((R/'SOURCE_MANIFEST.json').read_text())
 for p,h in m.items():assert sha((R/p).read_bytes())==h,p
 return len(m)
def fixtures():
 out=[]
 cases=[('tetra',[[-1,-1,-1,1],[-1,1,1,1],[1,-1,1,1],[1,1,-1,1]],[4,4,6],[0,0,0]),('weak_prism',[[1,0,0,1],[-2,3,0,1],[1,-3,0,1],[0,0,1,1],[0,0,-1,1]],[4,4,6],[1,2,3])]
 for name,H,c,w in cases:
  a=check_A.run({'H':H});b=check_B.run({'H':H});assert a==b and a['counts']==c and a['weak']==w
  assert c!=[1,1,0] or w!=[0,0,0];out.append(dict(name=name,counts=c,weak=w,winner_gate_rejected=True))
 return out

def run(name,out):
 nf=sources();spec=json.loads((R/'EXPECTED626.json').read_text())[name];data=(R/name/'GENERATOR.json').read_bytes();assert sha(data)==spec['generator_sha256']
 out.mkdir(parents=True,exist_ok=False);(out/'GENERATOR.json').write_bytes(data)
 raw=RECONSTRUCT.recover(json.loads(data));rb=canon(raw);assert sha(rb)==spec['raw_sha256'];(out/'raw.json').write_bytes(rb)
 records=[];receipts=[]
 for label,engine in [('A',check_A),('B',check_B)]:
  t=time.perf_counter();a=engine.run(raw);elapsed=time.perf_counter()-t;ab=canon(a)
  assert sha(ab)==spec['record_sha256'];assert a['counts']==spec['counts'] and a['weak']==[0,0,0]
  assert [a[k] for k in ['V','E','F']]==spec['VEF'];assert a['active_input_indices']==list(range(137))
  assert all(a[k]==0 for k in ['face_primitive_zero_count','vertex_max_zero_count','edge_primitive_zero_count'])
  assert a['centred_first_moments']==a['centred_centroid']==[0,0,0]
  (out/(label+'.json')).write_bytes(ab);receipts.append(dict(engine=label,seconds=elapsed,bytes=len(ab),sha256=sha(ab)));records.append(a)
  print('EXACT',label,name,a['counts'],a['weak'],flush=True)
 assert records[0]==records[1];a=records[0];st=measure626.run(a,raw);co=compare626.run(a,raw,tuple(spec['pair']));cm=centred_mass.run(a);ff=fixtures()
 for p,obj in [('STATS.json',st),('COMPARISON.json',co),('CENTRED_MASS.json',cm)]: (out/p).write_bytes(canon(obj))
 assert sources()==nf
 rec=dict(status='BQ13_C626_TWO_FULL_EXACT_SOURCE_ONLY_PASS',object=name,VEF=spec['VEF'],counts=a['counts'],weak=a['weak'],S=a['stable_face_ids'],U=a['unstable_vertices'],H=a['saddle_edges'],generator_sha256=sha(data),record_sha256=sha(canon(a)),independent_records_identical=True,source_payload_files=nf,engines=receipts,centred_mass=cm,fixtures=ff,python=sys.version)
 (out/'RECEIPT.json').write_bytes(canon(rec));print(rec['status'],name,flush=True)
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--object',choices=['BASIN69_96','BASIN','REFERENCE'],default='BASIN69_96');p.add_argument('--out',required=True,type=Path);a=p.parse_args();run(a.object,a.out)
