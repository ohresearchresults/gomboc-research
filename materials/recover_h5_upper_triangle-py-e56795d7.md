# material-e56795d71075

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

---

#!/usr/bin/env python3
"""Recovery capsule part 2/2: exact upgrade of the retained box verifier.
Required part 1: h5_energy_chain_certificate.py (7315 bytes).
Run: python -B -S recover_h5_upper_triangle.py
Then: python -B -S h5_energy_chain_upper_triangle.py OUTPUT_DIRECTORY
"""
from pathlib import Path
import hashlib
SOURCE_SHA='cc89f73f6535e443c4ec7097490e8d32723cc65da86ccb6ed107adebf32b7159'
TARGET_SHA='84191a070c4fcfa26af3fa5627039bb51d92aac198014e2e15c7b075c1e51f18'
NEW_FUNCTION='''def bernstein_matrix(polys):
 indices=list(product(*(range(d+1) for d in DEGREES)));loc={k:i for i,k in enumerate(indices)}
 final=[k for k in indices if k[2]+k[3]<=3]
 den=lcm(*(v.denominator for p in polys for v in p.values()))
 scales={0:3,1:3,4:12};out=[]
 for p in polys:
  vals=[0]*len(indices)
  for k,v in p.items():
   assert all(k[i]<=DEGREES[i] for i in range(NVAR)) and k[2]+k[3]<=3
   vals[loc[k]]=int(v*den)
  for axis in (0,1,4):
   d=DEGREES[axis];old=vals;vals=[0]*len(indices)
   for row,k in enumerate(indices):
    for a in range(k[axis]+1):
     j=list(k);j[axis]=a
     vals[row]+=old[loc[tuple(j)]]*comb(k[axis],a)*scales[axis]//comb(d,a)
  result=[]
  for k in final:
   value=0
   for a in range(k[2]+1):
    for b in range(k[3]+1):
     j=list(k);j[2]=a;j[3]=b
     value+=vals[loc[tuple(j)]]*comb(k[2],a)*comb(k[3],b)*6//(comb(3,a+b)*comb(a+b,a))
   result.append(value)
  out.append(result)
 return final,den*3*3*12*6,out
'''

def replace_once(text,old,new):
 if text.count(old)!=1:raise RuntimeError('Unexpected source span: '+old)
 return text.replace(old,new,1)

def main():
 raw=Path('h5_energy_chain_certificate.py').read_bytes()
 if len(raw)!=7315 or hashlib.sha256(raw).hexdigest()!=SOURCE_SHA:
  raise RuntimeError('Recovery part 1 has the wrong bytes.')
 s=raw.decode('utf-8')
 for old,new in [('F(1,2),F(13,20)','F(2,5),F(4,5)'),('F(1,5),F(3,10)','F(1,5),F(3,5)'),('WEIGHTS=(3204,2267,1707,2822)','WEIGHTS=(218532,289114,307070,185284)'),('H5_FOUR_ARROW_ENERGY_CHAIN_MACRO_BOX_V1','H5_FOUR_ARROW_ENERGY_CHAIN_UPPER_TRIANGLE_V1')]:
  s=replace_once(s,old,new)
 a=s.index('def bernstein_matrix(');b=s.index('\ndef det3(',a)
 s=s[:a]+NEW_FUNCTION+s[b:]
 s=replace_once(s,"'genuine_restrictions':'x<1; lambda>0. Other box coordinates already have genuine strict H5 bounds.'","'genuine_restrictions':'x<1; lambda>0; p+q<1. The p/q affine coordinates satisfy u>=0,v>=0,u+v<=1, not an independent rectangle.'")
 out=s.encode('utf-8')
 if len(out)!=7607 or hashlib.sha256(out).hexdigest()!=TARGET_SHA:
  raise RuntimeError('Recovered target failed its exact identity check.')
 dest=Path('h5_energy_chain_upper_triangle.py')
 if dest.exists() and dest.read_bytes()!=out:raise RuntimeError('Refusing to overwrite a different target.')
 dest.write_bytes(out)
 print('H5_UPPER_TRIANGLE_SOURCE_RECOVERY_PASS',len(out),TARGET_SHA)
if __name__=='__main__':main()
