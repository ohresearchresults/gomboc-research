"""Finite saddle-boundary absorption. Numeric search only, with frozen exact checkpoints.
A nonwinner label is never upgraded without separately rebuilding and auditing it.
"""
import sys,json,argparse,subprocess,os,time
from pathlib import Path
import numpy as np
R=Path(__file__).resolve().parent;sys.path[:0]=[str(R),str(R/'parent/parent/mechanism/parent_sources')]
from numeric import recover,mechanics,topology
from leaf_general import Leaf

def dump(p,o):p.write_text(json.dumps(o,sort_keys=True,separators=(',',':')))
def run(a):
 out=a.out;out.mkdir(parents=True,exist_ok=False);src=a.source;history=[]
 ids=json.loads(a.support_ids.read_text()) if a.support_ids else list(range(json.loads((src/'GENERATOR.json').read_text())['n_supports']))
 protected_original={3,17,49,57,73,88,134,135,136,71,94,109,116,119,126}
 for step in range(a.count):
  d=json.loads((src/'GENERATOR.json').read_text());fs=json.loads((src/'faces.json').read_text());q=recover(d)[:d['n_supports']];s=mechanics(q,fs,details=True,tol=1e-13);root=int(np.argmin(np.linalg.norm(s['P']-[0,0,1],axis=1)));bad=[i for i in s['U']if i!=root]
  rec=dict(step=step,source=str(src),VEF=[s[k]for k in ['V','E','F']],counts=s['counts'],U=s['U'],H=s['H'],original_support_ids=ids);history.append(rec);dump(out/'history.json',history);print(rec,flush=True)
  if s['counts']==[1,1,0]:print('NUMERICAL_WINNER_NEEDS_AUDIT',flush=True);break
  if len(bad)!=1 or s['S']!=[3]:break
  keep=bad[0];options=[]
  for ed in s['H']:
   if keep not in ed:continue
   drop=ed[0]if ed[1]==keep else ed[1];uni=set(s['owners'][keep])|set(s['owners'][drop]);diff=set(s['owners'][drop])-set(s['owners'][keep])
   if drop==root or len(diff)!=1:continue
   moved=next(iter(diff));lost=[j for j,c in enumerate(fs)if len(c)==3 and keep in c and drop in c]
   if any(ids[j]in protected_original for j in lost):continue
   if {16,18,71,94}.issubset({ids[j]for j in uni}):continue
   if any(moved in deps for i,deps,ax in d['plan']):continue
   if len(next(z for z in d['plan']if z[0]==moved)[1])>=3:continue
   if any(set(g)==set(s['owners'][drop])for g in d['groups']):continue
   options.append((drop,moved,lost))
  if not options:print('NO_SUPPORTED_LEAF_STRATUM',flush=True);break
  drop,moved,lost=options[0];child=out/f'STEP{step+1}';cmd=[sys.executable,str(R/'leaf_general.py'),'--source',str(src),'--out',str(child),'--keep',str(keep),'--drop',str(drop),'--moved',str(moved),'--release','--steps',str(a.steps)]
  rec['chosen']=dict(keep=keep,drop=drop,moved=moved,lost=lost,original_moved=ids[moved]);dump(out/'history.json',history)
  with (out/f'STEP{step+1}.log').open('w')as log:
   try:res=subprocess.run(cmd,stdout=log,stderr=subprocess.STDOUT,timeout=a.seconds,check=False)
   except subprocess.TimeoutExpired:print('FINITE_EXECUTION_LIMIT_NO_CONTACT',flush=True);break
  if res.returncode or not (child/'GENERATOR.json').exists():print('NO_FINITE_CONTACT',res.returncode,flush=True);break
  ids=[k for j,k in enumerate(ids)if j not in lost];dump(child/'ORIGINAL_SUPPORT_IDS.json',ids);src=child
 dump(out/'history.json',history);print('LAST_FINITE',str(src),flush=True)
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--source',type=Path,required=True);p.add_argument('--out',type=Path,required=True);p.add_argument('--support-ids',type=Path);p.add_argument('--count',type=int,default=6);p.add_argument('--steps',type=int,default=60);p.add_argument('--seconds',type=float,default=180);run(p.parse_args())
