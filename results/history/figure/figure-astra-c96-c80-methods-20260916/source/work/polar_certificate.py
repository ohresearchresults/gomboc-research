"""Reconstruct and independently audit the own-centred polar of exact C96."""
import hashlib
import json
import sys
from fractions import Fraction as F
from math import gcd, lcm
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path[:0] = [str(ROOT/'tools'),str(ROOT/'tools/core')]
from exact_points import encoded, make
import check_A
import check_B
import centred_mass


def main():
    b = (ROOT/'work/baseline-check/POINTS.json').read_bytes()
    assert hashlib.sha256(b).hexdigest()=='b49d24fda9620582ca3a011efd07d45a6550aa4e748bdaca32e3f343de822742'
    parent=check_A.run(make(json.loads(b)['points']))
    c=tuple(map(F,parent['raw_centroid']))
    rows=[]
    for p in parent['raw_vertices']:
        row=[F(v)-a for v,a in zip(p,c)]+[F(1)]
        den=lcm(*(x.denominator for x in row))
        r=[int(x*den) for x in row]
        d=gcd(*r)
        rows.append([x//d for x in r])
    raw={'H':sorted(rows)}
    a=check_A.run(raw)
    bb=check_B.run(raw)
    assert a==bb
    m=centred_mass.run(a)
    out=ROOT/'work/polar-exact'
    out.mkdir(exist_ok=False)
    for name,obj in [('raw.json',raw),('A.json',a),('B.json',bb),('MASS.json',m)]:
        data=encoded(obj)
        (out/name).write_bytes(data)
        print(name,len(data),hashlib.sha256(data).hexdigest())
    print('C96_POLAR_OWN_CENSUS_AB_MASS_PASS',a['V'],a['E'],a['F'],a['counts'],a['weak'])


if __name__=='__main__':
    main()
