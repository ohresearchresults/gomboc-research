"""Exact audit of a saved numerical point or halfspace proposal on an integer grid."""
import argparse
import hashlib
import json
import sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
sys.path[:0]=[str(ROOT/'tools'),str(ROOT/'tools/core')]
from exact_points import encoded,make
import check_A,check_B,centred_mass


def main():
    ap=argparse.ArgumentParser();ap.add_argument('input');ap.add_argument('out')
    ap.add_argument('--grid',type=int,default=10**8)
    ap.add_argument('--supports',action='store_true')
    args=ap.parse_args();out=Path(args.out);out.mkdir(exist_ok=False)
    source=Path(args.input).read_bytes();data=json.loads(source)
    if args.supports:
        rows=[list(map(lambda x:round(float(x)*args.grid),q))+[args.grid] for q in data['supports']]
        from math import gcd
        rows=sorted({tuple(x//gcd(*row) for x in row) for row in rows})
        raw={'H':[list(row) for row in rows]}
    else:
        points=[[round(float(x)*args.grid) for x in p] for p in data['points']]
        shift=[sum(p[j] for p in points)//len(points) for j in range(3)]
        points=[[p[j]-shift[j] for j in range(3)]for p in points]
        (out/'POINTS.json').write_bytes(encoded({'points':points}))
        raw=make(points)
    a=check_A.run(raw);b=check_B.run(raw);assert a==b
    m=centred_mass.run(a)
    for name,obj in [('raw.json',raw),('A.json',a),('B.json',b),('MASS.json',m)]:
        binary=encoded(obj);(out/name).write_bytes(binary)
        print(name,len(binary),hashlib.sha256(binary).hexdigest())
    receipt=dict(input=args.input,input_sha256=hashlib.sha256(source).hexdigest(),
                 grid=args.grid,supports=args.supports,V=a['V'],E=a['E'],F=a['F'],C=2*a['E'],
                 own=a['counts'],weak=a['weak'],mass=m,
                 status='EXACT_AB_AND_THIRD_MASS_PASS')
    (out/'RECEIPT.json').write_bytes(encoded(receipt))
    print('EXACT_PROPOSAL_AB_MASS_PASS',a['V'],a['E'],a['F'],a['counts'],a['weak'])


if __name__=='__main__':
    main()
