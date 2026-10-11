"""Source-only exact replay of frozen F49_50 reference110 nonwinners.
CPython standard library, assertions enabled. No numerical solver is invoked.
The destination must not exist. Expected hashes are mandatory.
"""
import argparse,hashlib,json,subprocess,sys
from pathlib import Path
import fusion,RECONSTRUCT,CENSUS_AT,centred_mass,STATS
assert __debug__
sys.set_int_max_str_digits(0)
ROOT=Path(__file__).resolve().parent
CASES={'seed':[41,61,100],'pc3':[42,61,101],'slsqp3':[65,76,139]}
def load(p):return json.loads(p.read_text(encoding='utf-8'))
def data(obj):return json.dumps(obj,sort_keys=True,separators=(',',':')).encode('utf-8')
def digest(b):return dict(bytes=len(b),sha256=hashlib.sha256(b).hexdigest())
def file_records(root):return {str(p.relative_to(root)):digest(p.read_bytes()) for p in sorted(root.rglob('*')) if p.is_file() and p.suffix=='.json' and p.name!='RECEIPT.json'}

def initialize(out):
 out.mkdir(parents=True,exist_ok=False)
 gen,fs=fusion.make(load(ROOT/'inputs/S8/GENERATOR.json'),load(ROOT/'inputs/S8/FACES.json'))
 assert data(gen)==(ROOT/'checkpoints/seed/GENERATOR.json').read_bytes()
 assert json.dumps(fs,separators=(',',':')).encode()==(ROOT/'checkpoints/seed/faces.json').read_bytes()
 for p in sorted((ROOT/'checkpoints').glob('*/GENERATOR.json')):
  name=p.parent.name;q=out/name;q.mkdir()
  for n in ['GENERATOR.json','REFERENCE.json','faces.json']:(q/n).write_bytes((p.parent/n).read_bytes())
  (q/'raw.json').write_bytes(data(RECONSTRUCT.recover(load(p))))
 print('ALL_FROZEN_CONTACT_CHECKPOINTS_RECONSTRUCTED',flush=True)

def audits(out):
 jobs=[]
 for name in CASES:
  for label in ['A','B']:
   q=out/name;handle=(q/(label+'.log')).open('wb')
   p=subprocess.Popen([sys.executable,'-B','-S',str(ROOT/('check_'+label+'.py')),str(q/'raw.json'),str(q/(label+'.json'))],stdout=handle,stderr=subprocess.STDOUT)
   jobs.append((name,label,p,handle))
 failed=[]
 for name,label,p,h in jobs:
  code=p.wait();h.close()
  if code:failed.append((name,label,code))
  else:print('INDEPENDENT_FULL_AUDIT_FINISHED',name,label,flush=True)
 assert not failed,failed

def finish(out):
 for name,counts in CASES.items():
  q=out/name;rawa=(q/'A.json').read_bytes();rawb=(q/'B.json').read_bytes();assert rawa==rawb
  a=json.loads(rawa);assert a['counts']==counts and a['weak']==[0,0,0]
  assert [a[k] for k in ['V','E','F']]==[177,311,136]
  assert a['active_input_indices']==list(range(136))
  r=CENSUS_AT.run(a,load(q/'REFERENCE.json'));assert r['counts']==[1,1,0] and r['weak']==[0,0,0]
  assert r['face_primitive_zero_count']==r['edge_primitive_zero_count']==0
  (q/'REFERENCE_AUDIT.json').write_bytes(data(r))
  m=centred_mass.run(a);assert m['tetrahedra']==350
  (q/'CENTRED_MASS.json').write_bytes(data(m))
  print('REFERENCE_AND_THIRD_MASS_FINISHED',name,flush=True)
 STATS.run(out)
 observed=file_records(out);expected=load(ROOT/'EXPECTED.json');assert observed==expected,{'missing':sorted(set(expected)-set(observed)),'extra':sorted(set(observed)-set(expected)),'changed':[k for k in observed if k in expected and observed[k]!=expected[k]]}
 result=dict(status='COORD_F49_50_C622_REFERENCE_CHAMBER_EXACT_NONWINNERS_PASS',own_counts=CASES,reference_counts=[1,1,0],weak=[0,0,0],V=177,E=311,F=136,C=622,record_advanced=False,expected_files=len(expected),source_manifest_sha256=hashlib.sha256((ROOT/'SOURCE_MANIFEST.json').read_bytes()).hexdigest())
 (out/'RECEIPT.json').write_bytes(data(result));print(result['status'],flush=True)

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--out',type=Path,required=True);a=p.parse_args()
 for name,wanted in load(ROOT/'SOURCE_MANIFEST.json').items():assert digest((ROOT/name).read_bytes())==wanted,name
 initialize(a.out);audits(a.out);finish(a.out)
