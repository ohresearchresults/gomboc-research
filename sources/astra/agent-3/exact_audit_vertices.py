"""Exhaustive rational supporting planes plus complete exact native line-pair audit.
Defines the rounded physical body explicitly; never promotes a floating label.
"""
from pathlib import Path
from itertools import combinations
from math import gcd
import sys,json,time,hashlib,numpy as np
sys.set_int_max_str_digits(0)
sys.path.insert(0,str(Path('sources/FULL76/methods/parent').resolve()))
import check_B
from gmpy2 import mpq
check_B.Q=mpq

def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def audit(path,out,D):
 out=Path(out);out.mkdir(exist_ok=False,parents=True);start=time.time();X=np.load(path);original=[tuple(int(round(float(v)*D)) for v in row) for row in X];N=len(original);s=tuple(sum(row[j] for row in original) for j in range(3));P=[tuple(N*row[j]-s[j] for j in range(3)) for row in original];den=N*D
 data=dict(source=str(path),rounding='ties-to-even nearest integer after binary64 multiplication by D',original_grid=D,translated_denominator=den,translated_integer_points=P,translation_numerator=s,original_integer_points=original)
 B=lambda x:json.dumps(x,sort_keys=True,separators=(',',':')).encode();(out/'coordinates.json').write_bytes(B(data));planes=set()
 for ia,ib,ic in combinations(range(N),3):
  a,b,c=P[ia],P[ib],P[ic];n=cross(sub(b,a),sub(c,a))
  if n==(0,0,0):continue
  h=dot(n,a);pos=False;neg=False
  for p in P:
   v=dot(n,p)-h;pos|=v>0;neg|=v<0
   if pos and neg:break
  if pos and neg:continue
  if pos:n=tuple(-x for x in n);h=-h
  assert h>0
  row=tuple(den*x for x in n)+(h,);d=gcd(*row);planes.add(tuple(x//d for x in row))
 raw={'H':sorted(planes)};(out/'raw.json').write_bytes(B(raw));print('EXACT_PLANES',len(planes),time.time()-start,flush=True)
 rep=check_B.run(raw)
 rational_input={tuple(mpq(v,den) for v in p) for p in P};rational_output={tuple(mpq(v) for v in p) for p in rep['raw_vertices']}
 assert rational_output<=rational_input,'intersection contains a vertex outside literal input hull'
 assert all(dot(row[:3],p)<=row[3]*den for row in raw['H'] for p in P)
 (out/'audit.json').write_bytes(B(rep));summary={k:rep[k] for k in ['V','E','F','counts','weak','stable_face_ids','unstable_vertices','saddle_edges','face_primitive_zero_count','vertex_max_zero_count','edge_primitive_zero_count']};summary.update(C=2*rep['E'],seconds=time.time()-start,goal_met=rep['counts']==[1,1,0] and rep['weak']==[0,0,0] and 34<=2*rep['E']<500)
 summary['C_2E']=2*rep['E'];summary['VplusEplusF']=rep['V']+rep['E']+rep['F'];summary['goal_met']=summary['goal_met'] and summary['VplusEplusF']<500
 summary['files']={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in out.iterdir() if p.is_file()};(out/'summary.json').write_text(json.dumps(summary,indent=2)+'\n');print('EXACT_CENSUS',json.dumps(summary),flush=True)
 if summary['goal_met']:
  (out/'GOAL_CANDIDATE_COMPLETE.json').write_text(json.dumps(summary,indent=2));print('POTENTIAL_GOAL_COMPLETE_NEEDS_FINAL_SOURCE_REVIEW',out,flush=True)
 return rep
if __name__=='__main__':
 import argparse
 p=argparse.ArgumentParser();p.add_argument('input');p.add_argument('output');p.add_argument('--grid',type=int,default=10**9);a=p.parse_args();audit(a.input,a.output,a.grid)
