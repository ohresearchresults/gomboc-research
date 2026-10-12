# material-8fec7e437c3f

AI research material · [Export notes](../catalog/coverage.md#text-records)

---

"""Complete E17 FULL253 incidence intersection for the genuine root-CD pair cap.
python -S pair_cap_incidence.py build|check
The cap and FULL253 concentration are mathematical premises, not graph feasibility.
"""
from pathlib import Path
from collections import Counter
import hashlib,json,sys
assert __debug__
HERE=Path(__file__).resolve().parent
PINS={'k3_census.py':[13141,'9d87d21a211545b6174a755b75feda6620e3df8ac4074f0e4703cc51bb9be68a']}
def pin(b):return[len(b),hashlib.sha256(b).hexdigest()]
for n,p in PINS.items():assert pin((HERE/n).read_bytes())==p
import k3_census as C

def match(inc):
 f=[{v for v,row in enumerate(inc) if i in row} for i in range(9)]
 if len(f[5])!=3 or len(f[6])!=3:return None
 ab=f[5]&f[6];assert len(ab)==2
 c,d=next(iter(f[5]-ab)),next(iter(f[6]-ab));assert c!=d
 if {c,d}<=f[0] and not ab&f[0]:return {'shared_edge_vertices':sorted(ab),'opposite_vertices':[c,d],'root_vertices':sorted(f[0])}
 return None

def build():
 domains=set();path_count=0
 for rot in C.maps9e17():
  faces=C.face_cycles(rot);assert len(faces)==10
  for h in C.paths(rot):
   path_count+=1;p=dict(zip(h,C.Z))
   domains.add(tuple(sorted(tuple(sorted(p[v] for v in f)) for f in faces)))
 assert path_count==356940 and len(domains)==326693
 full=Counter();prior=Counter();removed=Counter();records=[]
 for ordinal,inc in enumerate(sorted(domains)):
  W=C.window(inc);K=len(W);full[K]+=1
  if C.contact056(inc):continue
  prior[K]+=1;witness=match(inc)
  if witness is not None:
   removed[K]+=1;records.append({'full_ordinal':ordinal,'incidence':inc,'window':W,'witness':witness})
 assert dict(full)=={2:142,3:5209,4:45231,5:127613,6:119375,7:29123}
 assert dict(prior)=={2:55,3:2307,4:22577,5:74731,6:81021,7:21886}
 out={'identity':'FULL253_ACTUAL_TRIANGLE_ROOT_CD_PAIR_CAP_INCIDENCE_V1','input_pins':PINS,
 'concentration_authority':['minimum-0069','d0f91982420a008eef0bc169a4c7b9f999710361057096a930facbf9715942ff'],
 'cap_identity':'ACTUAL_ADJACENT_TRIANGLE_ROOT_CD_PAIR_CAP_51_25_V1',
 'all':dict(sorted(full.items())),'prior_no056':dict(sorted(prior.items())),
 'newly_excluded':dict(sorted(removed.items())),'remaining':dict(sorted((k,prior[k]-removed[k]) for k in prior)),
 'records':records,'scope':'Complete marked incidence domains under FULL253 concentration only; no conclusion of realization or exact complexity minimum.',
 'source_pin':pin(Path(__file__).read_bytes())}
 print('PAIR_CAP_FULL_INCIDENCE_COUNTS',out['newly_excluded'],'total',len(records),flush=True)
 return C.enc(out)
def main():
 assert sys.argv[1:] in (['build'],['check'])
 b=build();p=HERE/'pair_cap_incidence.json'
 if sys.argv[1]=='check' or p.exists():assert p.read_bytes()==b
 else:p.write_bytes(b)
 print('FULL253_ROOT_CD_TRIANGLE_PAIR_CAP_INCIDENCE_PASS',*pin(b),flush=True)
if __name__=='__main__':main()
