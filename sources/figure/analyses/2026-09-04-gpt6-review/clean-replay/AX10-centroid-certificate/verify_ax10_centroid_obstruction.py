"""Exact obstruction for the literal AX10 two-apex band. Standard library only.

The sole geometric lemma is elementary. Cone a convex polyhedron from a point
C it contains and triangulate the boundary. Each positive-volume tetrahedron
has centroid (C+a+b+c)/4. If n.x <= h throughout the body, its volume centroid
g therefore satisfies 4*n.g <= n.C+3*h. This also proves -C/3 belongs to every
convex polyhedron with centroid zero that contains C.

This certifies an obstruction, NOT a Goemboc or a global AX10 impossibility.
"""

from fractions import Fraction as Q
from itertools import combinations
from pathlib import Path
import hashlib
import json
import math
import re

ROOT = Path(__file__).resolve().parent
PARENT = "asg_lSjg7n_lMDvF8a-CVGsUNf_R"
LABELS = ["0", "C", "H", "AS", "AT", "AU", "AV", "AW", "AX", "AY"]
SOURCE_INTS = [
    [-444979431, 132716346, 345410525],
    [-358547791, 1943731258, 345410525],
    [628762393, 132716346, 345410525],
    [732217676, 666787415, 195057784],
    [474380773, -45871008, -42488313],
    [-81367832, 235950210, -437472690],
    [313340949, 439524973, -216915086],
    [-955357250, 405612760, 136467183],
    [-345374236, -103553253, -218759588],
    [-352238969, -200951160, 190060607],
]
POINTS = {k: tuple(Q(v, 2**30) for v in row) for k, row in zip(LABELS, SOURCE_INTS)}


def dot(a, b):
    return sum(x*y for x, y in zip(a, b))


def sub(a, b):
    return tuple(x-y for x, y in zip(a, b))


def cross(a, b):
    return (a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2], a[0]*b[1]-a[1]*b[0])


def hull(points):
    """Enumerate every triple; fail if a maximal face is not triangular."""
    faces = []
    for a, b, c in combinations(points, 3):
        n = cross(sub(points[b], points[a]), sub(points[c], points[a]))
        if not any(n):
            continue
        h = dot(n, points[a])
        slack = [h-dot(n, p) for p in points.values()]
        if all(s >= 0 for s in slack):
            pass
        elif all(s <= 0 for s in slack):
            b, c = c, b
            n, h = tuple(-x for x in n), -h
            slack = [-s for s in slack]
        else:
            continue
        assert sum(s == 0 for s in slack) == 3, "Nontriangular face needs its own audit"
        assert h > 0, "The literal source must contain zero strictly"
        faces.append(((a, b, c), n, h))
    return faces


def mass(points, faces):
    volume = Q(0)
    moment = [Q(0), Q(0), Q(0)]
    for face, n, h in faces:
        a, b, c = [points[k] for k in face]
        v = dot(a, cross(b, c))/6
        assert v > 0
        volume += v
        for j in range(3):
            moment[j] += v*(a[j]+b[j]+c[j])/4
    return volume, tuple(moment)


def encode(x):
    if isinstance(x, Q):
        return str(x)
    raise TypeError(type(x).__name__)


def main():
    raw = (ROOT/"results"/(PARENT+".json")).read_bytes()
    expected = next(x["sha256"] for x in json.loads((ROOT/"results-index.json").read_text()) if x["id"] == PARENT)
    assert hashlib.sha256(raw).hexdigest() == expected
    text = json.loads(raw)["result_markdown"]
    literal = dict((m[0], [int(m[j]) for j in range(1, 4)]) for m in re.findall(
        r"^(0|C|H|AS|AT|AU|AV|AW|AX|AY)\s*=\s*\(\s*(-?\d+),\s*(-?\d+),\s*(-?\d+)\)/D", text, re.M))
    assert literal == dict(zip(LABELS, SOURCE_INTS))
    assert "D=2^30" in text

    faces = hull(POINTS)
    assert len(faces) == 16
    edges = {tuple(sorted(e)) for f, _, _ in faces for e in combinations(f, 2)}
    assert len(edges) == 24
    assert all(sum(set(e) <= set(f) for f, _, _ in faces) == 2 for e in edges)
    volume, moment = mass(POINTS, faces)
    assert volume == Q(4314676606919473104543174179, 7427640235712281649394745344)
    centroid = tuple(m/volume for m in moment)
    assert centroid == (
        Q(-1473813210086390509534743809321315697, 18531394919535384289564522118836649984),
        Q(9136681163149509051862738422235609781, 18531394919535384289564522118836649984),
        Q(825639602344978981352215841493392229, 9265697459767692144782261059418324992),
    )

    removed_by_proposed_band = {frozenset(("AW", "AX", "AY")), frozenset(("AT", "AY", "AX"))}
    failures = []
    for face, n, h in faces:
        witness = min(POINTS, key=lambda k: dot(n, POINTS[k]))
        gap = dot(n, POINTS[witness])+3*h
        if gap >= 0:
            continue
        failures.append({
            "face": list(face), "witness_point": witness, "normal": n, "support": h,
            "opposite_to_support_ratio": -dot(n, POINTS[witness])/h,
            "exact_centroid_inequality_rhs": gap,
            "retained_by_literal_two_apex_band": frozenset(face) not in removed_by_proposed_band,
            "centroid_distance_lower_bound_squared": gap**2/(16*dot(n, n)),
            "centroid_distance_lower_bound_decimal": -float(gap)/(4*math.sqrt(float(dot(n, n)))),
        })
    expected_failures = {
        frozenset(("H", "AT", "AY")), frozenset(("AT", "AU", "AX")),
        frozenset(("AT", "AX", "AY")), frozenset(("AW", "AX", "AY")),
    }
    assert {frozenset(x["face"]) for x in failures} == expected_failures
    assert all(x["witness_point"] == "C" for x in failures)
    kept = [x for x in failures if x["retained_by_literal_two_apex_band"]]
    assert len(kept) == 2
    assert max(x["centroid_distance_lower_bound_squared"] for x in kept) > Q(303, 1000)**2

    mandatory = tuple(-x/3 for x in POINTS["C"])
    assert {frozenset(f) for f, n, h in faces if dot(n, mandatory) > h} == expected_failures
    expanded = dict(POINTS, REQUIRED=mandatory)
    expanded_faces = hull(expanded)
    assert len(expanded_faces) == 18
    # The entire reflected source is already contained after this one addition.
    for p in POINTS.values():
        reflected = tuple(-x/3 for x in p)
        assert all(dot(n, reflected) <= h for _, n, h in expanded_faces)
    boundary_edges = [e for e in edges if sum(set(e) <= set(f) for f in expected_failures) == 1]
    assert len(boundary_edges) == 6
    result = {
        "verdict": "LITERAL_FIXED_SOURCE_TWO_APEX_BAND_CANNOT_HAVE_CENTROID_ZERO",
        "parent_assignment": PARENT, "parent_sha256": expected,
        "source_volume": volume, "source_centroid": centroid,
        "source_f_vector": [10, 24, 16], "obstructing_faces": failures,
        "required_point": mandatory, "minimum_required_patch_boundary_edges": boundary_edges,
        "mandatory_hull_f_vector": [11, 27, 18],
        "scope": "Original source coordinates fixed; C retained as a point, even if no longer extreme. Each retained halfspace suffices for exclusion. This does not exclude moving old vertices, crossing all obstructing planes, changing the target centre, or other AX10 topologies.",
    }
    (ROOT/"ax10-centroid-obstruction.json").write_text(json.dumps(result, default=encode, indent=2)+"\n")
    print(json.dumps(result, default=encode, indent=2))
    print("EXACT_AX10_CENTROID_OBSTRUCTION_PASS")


if __name__ == "__main__":
    main()
