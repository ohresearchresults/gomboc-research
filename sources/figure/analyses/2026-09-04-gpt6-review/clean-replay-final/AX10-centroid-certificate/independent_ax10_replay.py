"""Second exact implementation: integer determinants, direct result parsing.

Does not import the main verifier or its source/face table.
"""
from pathlib import Path
from fractions import Fraction
from itertools import combinations
import hashlib
import json
import re

root = Path(__file__).resolve().parent
aid = 'asg_lSjg7n_lMDvF8a-CVGsUNf_R'
raw = (root/'results'/(aid+'.json')).read_bytes()
assert hashlib.sha256(raw).hexdigest() == '2c28fe4781353da1c2fdd2b85cb4f28fc41e59870e8fdbfcfd291e002831fd72'
text = json.loads(raw)['result_markdown']
points = {m[0]: tuple(map(int, m[1:])) for m in re.findall(
    r'^(0|C|H|AS|AT|AU|AV|AW|AX|AY)\s*=\s*\(\s*(-?\d+),\s*(-?\d+),\s*(-?\d+)\)/D', text, re.M)}
assert len(points) == 10
D = 2**30


def difference(a, b):
    return tuple(x-y for x, y in zip(a, b))


def det(a, b, c):
    return (a[0]*(b[1]*c[2]-b[2]*c[1])
            - a[1]*(b[0]*c[2]-b[2]*c[0])
            + a[2]*(b[0]*c[1]-b[1]*c[0]))


faces = []
bad_faces = []
det_sum = 0
moment_numerator = [0, 0, 0]
C = points['C']
for labels in combinations(points, 3):
    a, b, c = [points[x] for x in labels]
    ab, ac = difference(b, a), difference(c, a)
    signs = [det(ab, ac, difference(x, a)) for x in points.values()]
    if all(x <= 0 for x in signs):
        orientation = 1
    elif all(x >= 0 for x in signs):
        orientation = -1
    else:
        continue
    assert sum(x == 0 for x in signs) == 3
    faces.append(labels)
    # 3*h+n.C with unnormalised, outward integer normal.
    gap = orientation*det(ab, ac, tuple(3*x+y for x, y in zip(a, C)))
    h = orientation*det(ab, ac, a)
    assert h > 0
    if gap < 0:
        bad_faces.append((labels, Fraction(gap, D**3)))
    d = orientation*det(difference(a, C), difference(b, C), difference(c, C))
    assert d >= 0
    det_sum += d
    for j in range(3):
        moment_numerator[j] += d*(C[j]+a[j]+b[j]+c[j])

assert len(faces) == 16
volume = Fraction(det_sum, 6*D**3)
centroid = tuple(Fraction(x, 4*D*det_sum) for x in moment_numerator)
primary = json.loads((root/'ax10-centroid-obstruction.json').read_text())
assert str(volume) == primary['source_volume']
assert list(map(str, centroid)) == primary['source_centroid']
assert {frozenset(f) for f, _ in bad_faces} == {frozenset(x['face']) for x in primary['obstructing_faces']}
for face, gap in bad_faces:
    published = next(x for x in primary['obstructing_faces'] if frozenset(x['face']) == frozenset(face))
    assert gap == Fraction(published['exact_centroid_inequality_rhs'])
    print('EXACT_INDEPENDENT_NEGATIVE_GAP', list(face), str(gap))
print('SOURCE_VOLUME_AND_CENTROID_RECONSTRUCTED_FROM_C_APEX_TETRAHEDRA')
print('INDEPENDENT_INTEGER_AX10_CENTROID_OBSTRUCTION_PASS')
