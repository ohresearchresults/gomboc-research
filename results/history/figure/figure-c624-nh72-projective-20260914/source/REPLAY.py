"""Source-only replay of both finite rational endpoints, including weak fixtures."""
import json,sys,hashlib,subprocess,argparse
from pathlib import Path
assert __debug__
sys.set_int_max_str_digits(0)
source=Path(__file__).resolve().parent
sys.path.insert(0,str(source))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def dump(p,x):p.write_text(json.dumps(x,sort_keys=True,separators=(',',':')),encoding='utf-8')
def call(script,*args):subprocess.run([sys.executable,'-B','-S',str(source/script),*map(str,args)],check=True)
def fixtures():
 import check_A,check_B
 results=[]
 samples=[('tetra',[[-1,-1,-1,1],[-1,1,1,1],[1,-1,1,1],[1,1,-1,1]],[4,4,6],[0,0,0]),('weak_prism',[[1,0,0,1],[-2,3,0,1],[1,-3,0,1],[0,0,1,1],[0,0,-1,1]],[4,4,6],[1,2,3])]
 for name,H,c,w in samples:
  a=check_A.run({'H':H});b=check_B.run({'H':H});assert a==b and a['counts']==c and a['weak']==w
  assert (c,w)!=([1,1,0],[0,0,0]);results.append(dict(name=name,counts=c,weak=w,winner_gate_rejected=True))
 for check in (check_A.run,check_B.run):
  for H in (samples[0][1]+[samples[0][1][0]],[[1,0,0,0]]*4):
   try:check({'H':H})
   except AssertionError:pass
   else:raise AssertionError('Invalid fixture was accepted')
 return results
p=argparse.ArgumentParser();p.add_argument('--out',type=Path,required=True);args=p.parse_args();out=args.out.resolve();out.mkdir(parents=True,exist_ok=False)
manifest=json.loads((source/'MANIFEST.json').read_text())
for name,r in manifest.items():assert (source/name).stat().st_size==r['bytes'] and sha(source/name)==r['sha256'],name
fixture=fixtures();expected=json.loads((source/'EXPECTED.json').read_text());receipt={}
for name in ['MODERATE','FAR']:
 target=out/name
 for stage in ['BUILD','A','B','MASS','EXTRA']:call('exact_orbit.py',source,name,target,stage)
 call('basin_detail.py',source,name,target)
 call('exact_orbit.py',source,name,target,'FINISH')
 a=json.loads((target/'A.json').read_text());receipt[name]=dict(VEF=[a['V'],a['E'],a['F']],counts=a['counts'],weak=a['weak'],files=expected[name])
call('moment_certificate.py',source,out/'MODERATE',out/'FAR',out/'MOMENT_CERTIFICATE.json')
r=expected['_MOMENT'];assert (out/'MOMENT_CERTIFICATE.json').stat().st_size==r['bytes'] and sha(out/'MOMENT_CERTIFICATE.json')==r['sha256']
for name,r in manifest.items():assert (source/name).stat().st_size==r['bytes'] and sha(source/name)==r['sha256'],name
receipt=dict(status='NH72_C624_TWO_PROJECTIVE_NONWINNERS_SOURCE_ONLY_COLD_PASS',objects=receipt,fixtures=fixture,source_manifest_sha256=sha(source/'MANIFEST.json'))
dump(out/'RECEIPT.json',receipt);print(receipt['status'],flush=True)
