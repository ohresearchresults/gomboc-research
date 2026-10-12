"""Freeze and audit specified finite caps; no optimizer required for replay."""
import json,hashlib
from fractions import Fraction as R
from exact84 import load,clip,audit,ROOT
P,F=load()
# Literal D=1e8 nominations. Both the normal and height share that denominator.
CASES={
 'J84_SMALL_WITNESS_CAP_G8':([49641352,-84919108,18013364],67547761),
 'J84_BAR_CAP_G8':([94301537,-19495777,-26965437],95968983),
}
for name,(n,h) in CASES.items():
    Q,ff=clip(P,F,tuple(map(R,n)),R(h));s=audit(Q,ff);s['name']=name;s['cut_normal_integers']=n;s['cut_height_integer']=h
    raw=(json.dumps(s,sort_keys=True,separators=(',',':'))+'\n').encode();(ROOT/(name+'.json')).write_bytes(raw)
    print(name,s['V'],s['E'],s['F'],s['strict'],s['weak'],len(raw),hashlib.sha256(raw).hexdigest(),flush=True)
    print('P',[float(R(x['depth'])) for x in s['P']],'Q',[float(R(x['depth'])) for x in s['Q']],flush=True)
print('J84_EXACT_FINITE_CAP_CONTROLS_PASS_NO_110',flush=True)
