"""Terminal assertions for the four exact J90 nonwinners; no floating census."""
import json,sys
from pathlib import Path
from fractions import Fraction as F
sys.set_int_max_str_digits(0)
expected={'J90_DETACHED_B_G10':(132,198,68,169169363170354),'J90_DETACHED_C390_G8':(130,195,67,167176381818987),'J90_BALANCED_C452_G14':(138,226,90,164239827108860),'J90_EXACT_CENTER_C452':(138,226,90,164239827108860)}
bodies={}
for name,(v,e,f,lo) in expected.items():
 d=json.loads(Path(name+'_AUDIT.json').read_text());bodies[name]=d
 assert (d['V'],d['E'],d['F'],d['C'])==(v,e,f,2*e)
 assert d['strict']==[2,1,1] and d['weak']==[0,0,0] and d['primitive_zeros']==[0,0,0]
 assert not d['P'] and len(d['Q'])==1
 q=F(d['Q'][0]['depth']);assert F(lo,10**15)<q<F(lo+1,10**15)
 assert all(u not in d['faces'][s] for s in d['S'] for u in d['U'])
 print(name,'VEF',v,e,f,'own211/weak000/pzero000','Q in',lo,lo+1,'over 10^15')
b=bodies['J90_DETACHED_C390_G8'];a=bodies['J90_BALANCED_C452_G14'];c=bodies['J90_EXACT_CENTER_C452'];r=json.loads(Path('J90_EXACT_CENTER_C452_CORRECTION.json').read_text())
assert b['centroid']==c['centroid']==r['target_centroid']
assert c['volume']==a['volume']==r['expected_volume']
assert all(F(x)==0 for x in r['moment_residual'])
assert a['centroid']!=c['centroid']
print('J90_FOUR_EXACT_OWN211_NONWINNERS_RECOVERED_NO_110')
print('J90_EXACT_SAME_CENTRE_PHYSICAL_ENLARGEMENT_CONFIRMED')
