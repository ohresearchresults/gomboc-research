"""Exact dimensionless full-point escape margin certificate at the true filled COM.
Floating calculations select witnesses only; every claimed bound is verified by
integer dot products and squared rational inequalities, without square roots.
"""

import argparse, json, sys, math, hashlib
from pathlib import Path
from fractions import Fraction as F

sys.set_int_max_str_digits(0)
B = lambda x: json.dumps(x, sort_keys=True, separators=(",", ":")).encode()


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def sub(a, b):
    return tuple(x - y for x, y in zip(a, b))


def run(raw, rep, floor, upper=None):
    g = list(map(F, rep["raw_centroid"]))
    X = [list(map(F, row)) for row in rep["raw_vertices"]]
    D = math.lcm(
        *(x.denominator for row in X for x in row), *(x.denominator for x in g)
    )
    G = [int(x * D) for x in g]
    Z = [tuple(int(x * D) - v for x, v in zip(row, G)) for row in X]
    N = [tuple(r[:3]) for r in raw["H"]]
    ss = [r[3] * D - dot(r[:3], G) for r in raw["H"]]
    assert min(ss) > 0
    p = [[float(x - y) for x, y in zip(row, g)] for row in X]
    q = [[float(F(a * D, s)) for a in n] for n, s in zip(N, ss)]
    root = rep["unstable_vertices"][0]
    S = rep["stable_face_ids"][0]
    assert rep["active_input_indices"] == list(range(rep["F"]))

    def pair(kind, i, j):
        if kind == "physical":
            return Z[i], sub(Z[j], Z[i])
        return N[i], tuple(b * ss[i] - a * ss[j] for a, b in zip(N[i], N[j]))

    def score(a, b):
        e = sub(b, a)
        return dot(a, e) / math.sqrt(dot(a, a) * dot(e, e))

    results = {}
    minimums = []
    for kind, pts, rt in [("physical", p, root), ("polar", q, S)]:
        witnesses = []
        approx = []
        for i, a in enumerate(pts):
            if i == rt:
                continue
            js = [j for j in range(len(pts)) if j != i]
            j = max(js, key=lambda j: score(a, pts[j]))
            n, e = pair(kind, i, j)
            d = dot(n, e)
            aa = dot(n, n)
            ee = dot(e, e)
            assert d > 0 and d * d * floor.denominator**2 > floor.numerator**2 * aa * ee
            witnesses.append([i, j])
            approx.append([score(a, pts[j]), i])
        results[kind] = dict(witnesses=witnesses, minimum_approx=min(approx)[0])
        minimums.append((min(approx)[0], kind, min(approx)[1]))
    out = dict(
        status="EXACT_ALL_NONROOT_ESCAPE_FLOOR_PASS",
        floor=str(floor),
        common_physical_denominator_bits=D.bit_length(),
        physical=results["physical"],
        polar=results["polar"],
    )
    if upper is not None:
        _, kind, i = min(minimums)
        pts = p if kind == "physical" else q
        for j in range(len(pts)):
            if j == i:
                continue
            n, e = pair(kind, i, j)
            d = dot(n, e)
            assert d <= 0 or d * d * upper.denominator**2 < upper.numerator**2 * dot(
                n, n
            ) * dot(
                e, e
            )
        out["exact_minimum_upper_bound"] = str(upper)
        out["upper_feature"] = [kind, i]
    return out


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--audit", type=Path, required=True)
    ap.add_argument("--floor", type=F, required=True)
    ap.add_argument("--upper", type=F)
    ap.add_argument("--out", type=Path, required=True)
    a = ap.parse_args()
    r = run(
        json.load(open(a.audit / "raw.json")),
        json.load(open(a.audit / "A.json")),
        a.floor,
        a.upper,
    )
    a.out.write_bytes(B(r))
    print(
        r["status"],
        r["floor"],
        r.get("exact_minimum_upper_bound"),
        hashlib.sha256(B(r)).hexdigest(),
        flush=True,
    )
