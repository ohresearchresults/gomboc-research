"""Exact C96 disk/slab certificate; stdlib and unchanged exact source only."""
import hashlib
import json
import sys
from fractions import Fraction as F
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path[:0] = [str(ROOT/'tools'), str(ROOT/'tools/core')]
from exact_points import make, encoded
import check_A
import check_B
import centred_mass


def dot(a, b):
    return sum(x*y for x, y in zip(a, b))


def main():
    pfile = ROOT/'work/baseline-check/POINTS.json'
    b = pfile.read_bytes()
    assert hashlib.sha256(b).hexdigest() == 'b49d24fda9620582ca3a011efd07d45a6550aa4e748bdaca32e3f343de822742'
    raw = make(json.loads(b)['points'])
    a = check_A.run(raw)
    assert a == check_B.run(raw)
    centred_mass.run(a)
    g = tuple(map(F, a['raw_centroid']))
    x = [tuple(F(v)-c for v,c in zip(row,g)) for row in a['raw_vertices']]
    n = (89, 229, -10)
    nn = dot(n, n)
    radius = F(45400)
    halfwidth = F(4100)
    disk = []
    for row in raw['H']:
        u, h = row[:3], F(row[3])-dot(row[:3], g)
        projected = dot(u,u) - F(dot(u,n)**2, nn)
        assert h > 0 and projected >= 0
        slack = h*h-radius*radius*projected
        assert slack > 0
        disk.append(slack/(h*h))
    slab = [1-F(dot(n,v)**2, nn*halfwidth*halfwidth) for v in x]
    assert min(slab) > 0
    report = dict(identity='C96_TILTED_DISK_SLAB_CERTIFICATE',
                  parent_points_sha256=hashlib.sha256(b).hexdigest(),
                  V=a['V'], E=a['E'], F=a['F'], own=a['counts'], weak=a['weak'],
                  own_centroid=a['raw_centroid'], normal=n,
                  disk_radius=str(radius), slab_halfwidth=str(halfwidth),
                  radius_to_halfwidth=str(radius/halfwidth),
                  disk_min_relative_squared_slack=str(min(disk)),
                  slab_min_relative_squared_slack=str(min(slab)),
                  all_facets_checked=len(disk), all_vertices_checked=len(slab),
                  conclusion='S >= 2 for every nonsingular affine image with Euclidean singular-value condition number strictly below 454/41. No claim outside this range or for arbitrary non-affine descendants.')
    out = ROOT/'work/shape-certificate.json'
    out.write_bytes(encoded(report))
    print('C96_EXACT_TILTED_DISK_SLAB_PASS')
    print(json.dumps(report, indent=2))
    print('SHA256', hashlib.sha256(out.read_bytes()).hexdigest())


if __name__ == '__main__':
    main()
