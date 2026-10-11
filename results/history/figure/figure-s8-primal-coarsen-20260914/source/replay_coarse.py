"""Exact reconstruction and two audits of a moved retained-primal solid.
Usage: python -B -S replay_coarse.py S8_SOURCE GENERATOR INCIDENCE NEW_OUT
Numerical discovery is not needed to reconstruct the prescribed rational body.
"""
from pathlib import Path
from fractions import Fraction as F
from math import gcd,lcm
import json,sys,hashlib
if not __debug__:raise RuntimeError('Assertions must be enabled')
sys.set_int_max_str_digits(0)
root=Path(sys.argv[1]).resolve();sys.path.insert(0,str(root));import REPLAY,RECONSTRUCT,check_A,check_B,centred_mass
REPLAY.sources();data=json.loads(Path(sys.argv[2]).read_text());inc=json.loads(Path(sys.argv[3]).read_text());out=Path(sys.argv[4]);out.mkdir(parents=True,exist_ok=False)
Haux=RECONSTRUCT.recover(data)['H'];qo=[tuple(F(v,h[3])for v in h[:3])for h in Haux];allP=[tuple(RECONSTRUCT.solve([qo[j]for j in tri],[F(1)]*3))for tri in inc['triples']];P=[allP[j]for j in inc['keep']];H=[]
for old,cy in zip(inc['oldfaces'],inc['faces']):
 if old>=0:r=Haux[old]
 else:
  assert len(cy)==3;q=RECONSTRUCT.solve([P[i]for i in cy],[F(1)]*3);D=lcm(*(v.denominator for v in q));r=[int(v*D)for v in q]+[D];g=gcd(*r);r=[a//g for a in r]
 assert r[3]>0
 for i,p in enumerate(P):
  v=check_A.dot(r[:3],p)-r[3];assert (v==0)if i in cy else(v<0),('support error',old,cy,i)
 H.append(r)
raw={'H':sorted(H)};canon=lambda x:json.dumps(x,sort_keys=True,separators=(',',':')).encode();files={}
def save(n,x):
 b=canon(x);(out/n).write_bytes(b);files[n]=dict(bytes=len(b),sha256=hashlib.sha256(b).hexdigest())
save('raw.json',raw);a=check_A.run(raw);save('A.json',a);print('COARSE_A_PASS',a['V'],a['E'],a['F'],a['counts'],a['weak'],flush=True);b=check_B.run(raw);assert a==b;assert [tuple(map(F,p))for p in a['raw_vertices']]==sorted(P);save('B.json',b);save('CENTRED_MASS.json',centred_mass.run(a))
stats=dict(V=a['V'],E=a['E'],F=a['F'],C=2*a['E'],counts=a['counts'],weak=a['weak'],support_bits=max(abs(v).bit_length()for r in H for v in r),raw_coordinate_bits=max(max(abs(v.numerator).bit_length(),v.denominator.bit_length())for p in P for v in p),deleted_parent_vertices=[i for i in range(len(allP))if i not in inc['keep']]);save('STATS.json',stats);receipt=dict(status='MOVED_COARSE_RATIONAL_A_B_PASS',stats=stats,files=files.copy());save('RECEIPT.json',receipt);print(receipt,flush=True)
