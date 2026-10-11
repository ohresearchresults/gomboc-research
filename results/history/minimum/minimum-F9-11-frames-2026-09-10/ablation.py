"""Exact counterterm-omission audit. Does not assert physical feasibility.
Run after check.py; imports its exact arithmetic, never the numerical code.
"""
import json,hashlib
from pathlib import Path
from inputs import TREES,PLAN
from check import weights,expand,bareiss,ldl,serial
assert __debug__
raw=Path('shadow_exact.json').read_bytes();obj=json.loads(raw)
v=json.loads(Path('shadow_verified.json').read_text())
assert v['coefficient_sha256']==hashlib.sha256(raw).hexdigest()
direct=0;monotone=0;unchanged=0
for r,(o,ex,rows) in zip(obj['records'],PLAN):
 if len(rows)==1:unchanged+=168;continue
 g=r['g'];edges=[(i,TREES[o][i]) for i in range(1,9)]+[ex]
 for ri,a in enumerate(rows):
  for wi,w in enumerate(weights(a)):
   if 20*w[rows[1-ri]]-181<=0:monotone+=1;continue
   A=expand(g[9*ri:9*ri+9],w,r['mu'][168*ri+wi],edges,g[18:63],[0]*45,0,1 if ri==0 else -1)
   ldl(A,bareiss(A));direct+=1
assert (direct,monotone,unchanged)==(504,1512,1008)
report=dict(tag='NOVA24_SHADOW_COUPLING_OMISSION_V1',direct=direct,PSD_monotonicity=monotone,unchanged=unchanged,all_matrices_without_counterterm_PD=True)
b=serial(report);Path('omission.json').write_bytes(b)
print('EXACT_COUPLING_OMISSION_PASS',3024,'DIRECT',direct,'PSD_MONOTONICITY',monotone,'UNCHANGED',unchanged)
print('NO_COUPLING_ESSENTIALITY_OR_PHYSICAL_WITNESS_CLAIM')
print('REPORT',len(b),hashlib.sha256(b).hexdigest())
