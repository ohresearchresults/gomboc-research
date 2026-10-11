"""Replay the two finite contractions and the separate reference-only repair.
The frozen exact generators, not floating arithmetic on another platform, define the bodies.
"""
import sys,os,json,subprocess,hashlib,argparse
from pathlib import Path
R=Path(__file__).resolve().parent
H=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def run(out):
 out.mkdir(parents=True,exist_ok=False);env={**os.environ,'OPENBLAS_NUM_THREADS':'1'};results={}
 def call(script,args):subprocess.run([sys.executable,str(R/script),*map(str,args)],env=env,check=True)
 call('contract.py',['--source',R/'C628_WINNER','--an',154,'--bn',159,'--out',out/'winner','--steps',30,'--seconds',1000])
 assert H(out/'winner/GENERATOR.json')==H(R/'BASIN69_96/GENERATOR.json')
 results['winner']=H(out/'winner/GENERATOR.json')
 call('contract.py',['--source',R/'C628_WINNER','--an',152,'--bn',155,'--checkpoint',R/'experiments/BLOWUP_CHECKPOINT.json','--out',out/'basin','--steps',30,'--seconds',1000])
 assert H(out/'basin/GENERATOR.json')==H(R/'BASIN/GENERATOR.json')
 results['basin']=H(out/'basin/GENERATOR.json')
 call('repair_reference.py',['--source',out/'basin','--out',out/'reference','--goal',1e-6,'--trust',.1,'--steps',20,'--seconds',1000])
 assert H(out/'reference/GENERATOR.json')==H(R/'REFERENCE/GENERATOR.json')
 results['reference_nonwinner']=H(out/'reference/GENERATOR.json')
 results['status']='BQ13_C626_COMPLETE_NUMERICAL_REPROPOSAL_BYTE_IDENTICAL'
 (out/'RECEIPT.json').write_text(json.dumps(results,sort_keys=True,separators=(',',':')));print(results['status'],flush=True)
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--out',required=True,type=Path);run(p.parse_args().out)
