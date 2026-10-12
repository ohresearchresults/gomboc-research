"""An exact finite check of the global own-centroid monotonicity bound.
The general statement is proved analytically in the handoff, not by two samples.
"""
import json,sys,math
from fractions import Fraction as F
from pathlib import Path
from exact_orbit import data,dot,sub,matvec,dump
sys.set_int_max_str_digits(0)
source=Path(sys.argv[1]).resolve();records=[]
for name,path in [('MODERATE',sys.argv[2]),('FAR',sys.argv[3])]:
 raw,par,t,A,inv,alpha,lower=data(source,name);r=json.loads((Path(path)/'EXTRA.json').read_text());g=tuple(map(F,r['projective_centroid']));V=F(r['projective_volume']);records.append((t,g,V))
s,g,V=records[0];t,h,W=records[1];delta=sub(t,s);gap=dot(delta,sub(g,h));lower=dot(delta,delta)/(7500*max(V,W));assert gap>lower>0
out=dict(status='EXACT_OWN_CENTROID_STRONG_MONOTONICITY_INSTANCE_PASS',scalar_gap=gap,guaranteed_lower_bound=lower,strict_gap=gap-lower,cube_halfside=F(1,5),projective_cube_halfside=F(1,10))
dump(Path(sys.argv[4]),out);print(out['status'],float(gap),float(lower),flush=True)
