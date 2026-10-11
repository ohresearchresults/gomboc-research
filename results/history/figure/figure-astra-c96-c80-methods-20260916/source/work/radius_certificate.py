"""Exact centred inradius/circumradius comparisons for already audited bodies."""
import hashlib,json
from fractions import Fraction as F
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]


def dot(a,b):
    return sum(x*y for x,y in zip(a,b))


def metric(name,sha):
    data=(ROOT/'work'/name/'A.json').read_bytes()
    assert hashlib.sha256(data).hexdigest()==sha
    a=json.loads(data);g=tuple(map(F,a['raw_centroid']))
    x=[tuple(F(v)-c for v,c in zip(p,g))for p in a['raw_vertices']]
    radius2=[dot(v,v) for v in x]
    supports=[F(h)-dot(n,g) for n,h in zip(a['normals'],a['offsets'])]
    assert min(supports)>0
    inr2=[h*h/dot(n,n) for n,h in zip(a['normals'],supports)]
    ratio2=min(inr2)/max(radius2)
    return dict(identity=name,audit_sha256=sha,ratio_squared=str(ratio2),
                inradius_facet=inr2.index(min(inr2)),circumradius_vertex=radius2.index(max(radius2)),
                ratio_greater_than_one_tenth=100*ratio2>1,
                ratio_less_than_one_fortieth=1600*ratio2<1,
                own=a['counts'],weak=a['weak'])


def main():
    report=[metric('baseline-check','a6c33c9f089de95cbbe52ebe51ecb4351306575df32f2aced706f62774793093'),
            metric('pyramid-101-exact','f17bb48815e8ff86697936d33af34e8e28170808674e9149dbae23c5228a19f7'),
            metric('rounder25-exact','c41d79fbc3a4711cef1201a17fcec0ba85ecded87f9072cf67e65ebb19229283')]
    assert report[0]['ratio_less_than_one_fortieth']
    assert report[2]['ratio_greater_than_one_tenth']
    out=ROOT/'work/radius-certificate.json'
    out.write_text(json.dumps(report,sort_keys=True,indent=2)+'\n')
    print('EXACT_CENTRED_RADIUS_COMPARISON_PASS')
    print(json.dumps(report,indent=2))
    print('SHA256',hashlib.sha256(out.read_bytes()).hexdigest())


if __name__=='__main__':
    main()
