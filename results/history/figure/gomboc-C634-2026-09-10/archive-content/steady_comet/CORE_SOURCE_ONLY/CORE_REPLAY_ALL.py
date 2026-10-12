"""Replay the four literal primary definitions, then the exact interval theorem.
Run: python3 CORE_REPLAY_ALL.py. Numerical search is not part of the definition.
"""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import hashlib,json,shutil,subprocess,sys,os
assert not sys.flags.optimize
sys.set_int_max_str_digits(0)
R=Path(__file__).resolve().parent
E=json.loads((R/'EXPECTATIONS.json').read_text())
def digest(p):
 b=p.read_bytes();return [len(b),hashlib.sha256(b).hexdigest()]
def execute(cmd,cwd,log):
 with open(log,'w') as f:subprocess.run(cmd,cwd=cwd,stdout=f,stderr=subprocess.STDOUT,check=True,env={**os.environ,'OPENBLAS_NUM_THREADS':'1'})
def one(name):
 d=R/name
 for f in ['RECONSTRUCT.py','check_A.py','check_B.py','EXTRA.py']:shutil.copyfile(R/'audit'/f,d/f)
 if not (d/'REPLAY.py').exists():shutil.copyfile(R/'audit/REPLAY.py',d/'REPLAY.py')
 inputs={p.name:digest(p) for p in sorted(d.iterdir()) if p.suffix=='.py' or p.name in ['GENERATOR.json','META.json','FROZEN_OUTPUTS.json']}
 execute([sys.executable,'-u','-S','REPLAY.py'],d,d/'SOURCE_REPLAY.log')
 actual={f:digest(d/f) for f in E['bodies'][name]};assert actual==E['bodies'][name]
 print(name,'SOURCE_ONLY_EXACT_A_B_AND_ALL_FROZEN_OUTPUTS_MATCH_PASS',flush=True)
 return dict(tag=name,source_inputs=inputs,outputs=actual)
if __name__=='__main__':
 with ThreadPoolExecutor(max_workers=3) as pool:out=dict(bodies=list(pool.map(one,sorted(E['bodies']))))
 for file,site in [('symbolic_pair.py',True),('pair_wall_certificate.py',False),('pair_interval_certificate.py',True)]:execute([sys.executable,'-u']+([] if site else ['-S'])+[file],R,R/(file+'.SOURCE_REPLAY.log'))
 got={f:digest(R/f) for f in E['symbolic']};assert got==E['symbolic'];out['symbolic']=got
 for name,want in E['moments'].items():
  execute([sys.executable,'-u','-S','mass_moments.py',name],R,R/(name+'.MASS_SOURCE_REPLAY.log'));assert digest(R/name/'MASS_MOMENTS.json')==want
 out['moments']=E['moments'];out['all_requested_source_only_replays_pass']=True
 blob=json.dumps(out,sort_keys=True,separators=(',',':')).encode();(R/'SOURCE_ONLY_RECEIPT.json').write_bytes(blob)
 print('FOUR_EXACT_ENDPOINTS_FULL_INTERVAL_AND_FILLED_MOMENTS_SOURCE_ONLY_PASS',flush=True)
 print('SOURCE_ONLY_RECEIPT.json',len(blob),hashlib.sha256(blob).hexdigest(),flush=True)
