"""Portable complete numerical production graph from the literal C626 source.
Frozen integer generators, not successful floating reproposal, define the bodies.
The TRI9 free-point approach starts at its literal stored binary64 checkpoint.
"""
import argparse,hashlib,json,os,subprocess,sys
from pathlib import Path
R=Path(__file__).resolve().parent
sys.path[:0]=[str(R),str(R/'parent'),str(R/'parent/parent/mechanism/parent_sources')]
import numpy as np
import normal_form
from numeric import recover
from delete_screen import drop_chart,hull
from snap_free_pair import construct

def canon(o):return json.dumps(o,sort_keys=True,separators=(',',':')).encode()
# node: source node, module, keeper, disappeared vertex, moving support, max iterations.
NODES={
'GUARD50':('PARENT','leaf_contract',26,19,113,80),
'GUARD50_SECOND93':('GUARD50','leaf_nonsimple',25,23,93,80),
'GUARD50_CHAIN':('GUARD50_SECOND93','leaf_general',24,26,87,80),
'DELETE99_SECOND80':('DELETE99','leaf_general',96,134,80,80),
'DELETE99_CHAIN':('DELETE99_SECOND80','leaf_general',96,124,69,60),
'TRI9_SECOND88':('TRI9_BASE','leaf_nonsimple',13,15,88,80),
'TRI9_THIRD110':('TRI9_SECOND88','leaf_general',13,14,110,80),
'STABLE120':('PARENT','leaf_general',167,165,120,55),
'STABLE73':('PARENT','leaf_general',125,121,73,55),
'STABLE13':('PARENT','leaf_general',161,164,13,55)}
for i,(drop,moved)in enumerate([(15,109),(16,111),(18,123),(19,112),(22,124),(24,114),(24,92),(25,113)],1):
 NODES[f'TRI9_TRIANGLE9_STEP{i}']=(f'TRI9_TRIANGLE9_STEP{i-1}'if i>1 else'TRI9_THIRD110','leaf_general',13,drop,moved,60)

def main(a):
 a.out.mkdir(parents=True,exist_ok=False);expected=json.loads((R/'EXPECTED.json').read_text());seen={};receipts=[]
 def node(name):
  if name=='PARENT':return R/'parent/BASIN69_96'
  if name in seen:return seen[name]
  p=a.out/name
  if name=='TRI9_BASE':
   base=node('PARENT');d=json.loads((base/'GENERATOR.json').read_text());fs=json.loads((base/'faces.json').read_text());cp=json.loads((R/'trans9_finite/CHECKPOINT.json').read_text());u=np.array([float.fromhex(x)for x in cp['u_hex']]);dd,ff,info=construct(d,fs,cp['an'],cp['bn'],u);p.mkdir();(p/'GENERATOR.json').write_bytes(canon(dd));(p/'faces.json').write_bytes(canon(ff));(p/'CHANGE.json').write_bytes(canon(info))
  elif name=='DELETE99':
   base=node('PARENT');d=json.loads((base/'GENERATOR.json').read_text());dd=drop_chart(d,[99]);q=recover(dd)[:dd['n_supports']];_,ff=hull(q);p.mkdir();(p/'GENERATOR.json').write_bytes(canon(dd));(p/'faces.json').write_bytes(canon(ff))
  elif name=='GUARD50_DOUBLE':
   with (a.out/(name+'.log')).open('w')as log:subprocess.run([sys.executable,str(R/'from_double.py'),str(p)],check=True,stdout=log,stderr=subprocess.STDOUT)
  else:
   src,mod,k,drop,moved,steps=NODES[name];src=node(src)
   cmd=[sys.executable,str(R/(mod+'.py')),'--source',str(src),'--out',str(p),'--keep',str(k),'--drop',str(drop),'--moved',str(moved),'--release','--steps',str(steps)]
   with (a.out/(name+'.log')).open('w')as log:subprocess.run(cmd,check=True,stdout=log,stderr=subprocess.STDOUT)
  if not(p/'GENERATOR.json').exists():raise RuntimeError('No finite contact: '+name)
  db=canon(normal_form.normalize(json.loads((p/'GENERATOR.json').read_text())))
  if name in expected:
   assert len(db)==expected[name]['normal_generator_bytes']and hashlib.sha256(db).hexdigest()==expected[name]['normal_generator_sha256'],'different numerical proposal: '+name
   assert json.loads((p/'faces.json').read_text())==json.loads((R/expected[name]['path']/'faces.json').read_text())
   receipts.append(dict(alias=name,normal_generator_sha256=hashlib.sha256(db).hexdigest()));print('NUMERICAL_DEFINITION_BYTE_IDENTICAL',name,flush=True)
  seen[name]=p;return p
 targets=sorted(expected)if a.object=='ALL'else[a.object]
 for n in targets:node(n)
 receipt=dict(status='BQ13_REQUESTED_NUMERICAL_PRODUCTION_BYTE_IDENTICAL',targets=targets,receipts=receipts,python=sys.version,numpy=np.__version__)
 (a.out/'NUMERICAL_REPROPOSAL_RECEIPT.json').write_bytes(canon(receipt));print(receipt['status'],flush=True)
if __name__=='__main__':
 if os.environ.get('OPENBLAS_NUM_THREADS')!='1':raise RuntimeError('Set OPENBLAS_NUM_THREADS=1')
 p=argparse.ArgumentParser();p.add_argument('--object',default='TRI9_TRIANGLE9_STEP8');p.add_argument('--out',type=Path,required=True);main(p.parse_args())
