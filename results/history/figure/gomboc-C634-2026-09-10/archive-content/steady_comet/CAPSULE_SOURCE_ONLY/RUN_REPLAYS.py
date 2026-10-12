"""Source-only recovery and independent exhaustive exact replay.
All input definitions and code are contained in this packet. No optimizer is
required to reconstruct any promoted endpoint. Optional discovery uses SciPy.
"""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import argparse,hashlib,json,shutil,subprocess,sys,os
R=Path(__file__).resolve().parent
assert not sys.flags.optimize
sys.set_int_max_str_digits(0)
def digest(p):
 b=p.read_bytes();return [len(b),hashlib.sha256(b).hexdigest()]
def invoke(cmd,cwd,log):
 with open(log,'w') as f:subprocess.run(cmd,cwd=cwd,stdout=f,stderr=subprocess.STDOUT,check=True,env={**os.environ,'OPENBLAS_NUM_THREADS':'1'})
def body(name,expected):
 d=R/name
 for f in ['RECONSTRUCT.py','check_A.py','check_B.py','EXTRA.py']:
  shutil.copyfile(R/'audit'/f,d/f)
 if not (d/'REPLAY.py').exists():shutil.copyfile(R/'audit/REPLAY.py',d/'REPLAY.py')
 inputs={p.name:digest(p) for p in sorted(d.iterdir()) if p.suffix=='.py' or p.name in ['GENERATOR.json','META.json','FROZEN_OUTPUTS.json']}
 invoke([sys.executable,'-u','-S','REPLAY.py'],d,d/'SOURCE_REPLAY.log')
 got={f:digest(d/f) for f in expected};assert got==expected,(name,got,expected)
 markers=[line for line in (d/'SOURCE_REPLAY.log').read_text().splitlines() if 'PASS' in line]
 out=dict(tag=name,source_inputs=inputs,outputs=got,all_outputs_match=True,markers=markers)
 (d/'SOURCE_RECEIPT.json').write_text(json.dumps(out,sort_keys=True,separators=(',',':')))
 print(name,'SOURCE_ONLY_ALL_EXPECTED_OUTPUTS_MATCH_PASS',flush=True);return out

def main():
 p=argparse.ArgumentParser();p.add_argument('--jobs',type=int,default=3);p.add_argument('--symbolic',action='store_true');p.add_argument('--moments',action='store_true');p.add_argument('--parents',action='store_true');p.add_argument('--body',action='append');a=p.parse_args()
 exp=json.loads((R/'EXPECTATIONS.json').read_text());names=a.body or sorted(exp['bodies']);assert set(names)<=set(exp['bodies'])
 with ThreadPoolExecutor(max_workers=a.jobs) as pool:receipts=list(pool.map(lambda n:body(n,exp['bodies'][n]),names))
 out=dict(bodies=receipts,all_requested_body_replays_pass=True)
 if a.parents:
  d=R/'parent650/C650';invoke([sys.executable,'-u','-S','REPLAY.py'],d,d/'SOURCE_REPLAY.log');got={f:digest(d/f) for f in exp['C650']};assert got==exp['C650'];out['C650']=got
  for f,site in [('VERIFY_MIN213.py',False),('BUILD_TUTTE_XY.py',True),('REALIZE_AUDIT_H213.py',False)]:invoke([sys.executable,'-u']+([] if site else ['-S'])+[f],R,R/(f+'.SOURCE_REPLAY.log'))
  out['H213_parent_markers']=[line for line in (R/'REALIZE_AUDIT_H213.py.SOURCE_REPLAY.log').read_text().splitlines() if line.startswith(('class','weak','EXACT','polar n'))]
  print('C650_AND_EXACT_H213_PARENTS_REPLAY_PASS',flush=True)
 if a.symbolic:
  for f,site in [('symbolic_pair.py',True),('pair_wall_certificate.py',False),('pair_interval_certificate.py',True)]:invoke([sys.executable,'-u']+([] if site else ['-S'])+[f],R,R/(f+'.SOURCE_REPLAY.log'))
  got={f:digest(R/f) for f in exp['symbolic']};assert got==exp['symbolic'];out['symbolic']=got;print('SOURCE_ONLY_FULL_PAIR_INTERVAL_CERTIFICATE_MATCH_PASS',flush=True)
 if a.moments:
  for name,expected in exp['moments'].items():
   invoke([sys.executable,'-u','-S','mass_moments.py',name],R,R/(name+'.MASS_SOURCE_REPLAY.log'));assert digest(R/name/'MASS_MOMENTS.json')==expected
  out['moments']=exp['moments'];print('SOURCE_ONLY_ALL_FILLED_MOMENT_CERTIFICATES_MATCH_PASS',flush=True)
 blob=json.dumps(out,sort_keys=True,separators=(',',':')).encode();(R/'SOURCE_ONLY_RECEIPT.json').write_bytes(blob);print('SOURCE_ONLY_RECEIPT.json',len(blob),hashlib.sha256(blob).hexdigest(),flush=True)
 print('ALL_REQUESTED_SOURCE_ONLY_REPLAYS_PASS',flush=True)
if __name__=='__main__':main()
