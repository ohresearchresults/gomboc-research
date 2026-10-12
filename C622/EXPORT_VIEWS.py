"""Export explicitly approximate display copies; exact source stays unchanged."""

from pathlib import Path
from fractions import Fraction as F
from decimal import Decimal, localcontext
from math import lcm, sqrt
from collections import Counter
import json, sys, struct, hashlib

sys.set_int_max_str_digits(0)
ROOT = Path(__file__).resolve().parent
A = json.loads((ROOT / "verified/A.json").read_text())
raw = [tuple(map(F, r)) for r in A["raw_vertices"]]
g = tuple(map(F, A["raw_centroid"]))
X = [tuple(v - c for v, c in zip(r, g)) for r in raw]
faces = A["faces"]
tris = [(f[0], f[j], f[j + 1]) for f in faces for j in range(1, len(f) - 1)]


def sub(a, b):
    return tuple(x - y for x, y in zip(a, b))


def cross(a, b):
    return (
        a[1] * b[2] - a[2] * b[1],
        a[2] * b[0] - a[0] * b[2],
        a[0] * b[1] - a[1] * b[0],
    )


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def dec(x):
    with localcontext() as c:
        c.prec = 80
        return format(Decimal(x.numerator) / Decimal(x.denominator), ".24e")


rows = [[dec(x) for x in r] for r in X]
P = [tuple(map(F, r)) for r in rows]
lines = ["solid C622_APPROXIMATE_VIEW_ONLY_NOT_A_PRINT_CERTIFICATE"]
for ids in tris:
    p, q, r = [P[i] for i in ids]
    n = [float(v) for v in cross(sub(q, p), sub(r, p))]
    length = sqrt(sum(v * v for v in n))
    assert length > 0
    lines.append("  facet normal " + " ".join(format(v / length, ".17e") for v in n))
    lines.append("    outer loop")
    for i in ids:
        lines.append("      vertex " + " ".join(rows[i]))
    lines.extend(["    endloop", "  endfacet"])
lines.append("endsolid C622_APPROXIMATE_VIEW_ONLY_NOT_A_PRINT_CERTIFICATE")
stl = ROOT / "gomboc_C622_V176_view.stl"
stl.write_text("\n".join(lines) + "\n")
# Independently parse what is actually written; use exact rational decimal values.
parsed = [
    tuple(map(F, line.split()[1:]))
    for line in stl.read_text().splitlines()
    if line.strip().startswith("vertex ")
]
assert parsed == [P[i] for tri in tris for i in tri]
counts = Counter(tuple(sorted((i, j))) for t in tris for i, j in zip(t, t[1:] + t[:1]))
assert len(counts) == 522 and set(counts.values()) == {2}
orient = Counter((i, j) for t in tris for i, j in zip(t, t[1:] + t[:1]))
assert all(orient[i, j] == orient[j, i] == 1 for i, j in orient)


def diagnostic(p):
    v6 = F(0)
    mom = [F(0)] * 3
    deg = 0
    neg = 0
    for ids in tris:
        a, b, c = [p[i] for i in ids]
        n = cross(sub(b, a), sub(c, a))
        deg += n == (0, 0, 0)
        d = dot(a, cross(b, c))
        neg += d <= 0
        v6 += d
        for j in range(3):
            mom[j] += d * (a[j] + b[j] + c[j])
    assert v6 > 0
    centre = tuple(m / (4 * v6) for m in mom)
    unstable = []
    weak = []
    for i, a in enumerate(p):
        best = max(dot(sub(a, centre), sub(b, a)) for j, b in enumerate(p) if j != i)
        if best < 0:
            unstable.append(i)
        elif best == 0:
            weak.append(i)
    return {
        "unique_vertices": len(set(p)),
        "degenerate_triangles": deg,
        "nonpositive_origin_tetrahedra": neg,
        "mesh_centroid_approx": [float(x) for x in centre],
        "strict_supporting_vertex_count": len(unstable),
        "strict_supporting_vertex_ids": unstable,
        "weak_supporting_vertex_count": len(weak),
        "scope": "Supporting-plane vertex diagnostic about the oriented triangle-mesh centroid, not a full convex-hull/equilibrium audit of the rounded mesh.",
    }


p32 = [
    tuple(F(struct.unpack("f", struct.pack("f", float(x)))[0]) for x in p) for p in P
]
h = lcm(*(x.denominator for r in raw for x in r), *(x.denominator for x in g))
diag = {
    "exact_C": 622,
    "exact_V_E_F": [176, 311, 137],
    "exact_strict_S_U_H": A["counts"],
    "exact_weak": A["weak"],
    "common_centred_denominator_bits": h.bit_length(),
    "common_centred_denominator_decimal_digits": len(str(h)),
    "STL_triangle_count": len(tris),
    "triangulation_edges": len(counts),
    "true_edges": 311,
    "added_face_diagonals": len(counts) - 311,
    "closed_consistently_oriented_indexed_mesh": True,
    "ascii_25_significant_digits": diagnostic(P),
    "float32_import_simulation": diagnostic(p32),
    "physical_printability_certified": False,
}
(ROOT / "PRECISION_AND_MESH_CHECK.json").write_text(json.dumps(diag, indent=2) + "\n")
# Exact interchange data avoids a very large repeated centroid in every coordinate.
(ROOT / "EXACT_MODEL.json").write_text(
    json.dumps(
        {
            "coordinate_system": "raw rational vertices; subtract raw_centroid to centre at (0,0,0). Strings are exact fractions, not floating point.",
            "raw_vertices": A["raw_vertices"],
            "raw_centroid": A["raw_centroid"],
            "faces_outward": faces,
            "edges": A["edges"],
            "stable_face_ids": A["stable_face_ids"],
            "unstable_vertex_ids": A["unstable_vertices"],
        },
        separators=(",", ":"),
    )
    + "\n"
)
print(json.dumps(diag, indent=2), flush=True)
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

xf = np.array([[float(v) for v in r] for r in X])
polys = [xf[f] for f in faces]
fig = plt.figure(figsize=(15, 5.3), facecolor="white")
col = ["#3789c7" if i in A["stable_face_ids"] else "#d3dbe2" for i in range(len(faces))]
lo = xf.min(axis=0)
hi = xf.max(axis=0)
mid = (lo + hi) / 2
rad = max(hi - lo) * 0.55
for j, (el, az, label) in enumerate(
    [(0, 0, "along x"), (0, 90, "along y"), (90, -90, "along z")], 1
):
    ax = fig.add_subplot(1, 3, j, projection="3d")
    ax.set_proj_type("ortho")
    ax.add_collection3d(
        Poly3DCollection(
            polys, facecolors=col, edgecolors="#465765", linewidths=0.4, alpha=1
        )
    )
    for u in A["unstable_vertices"]:
        ax.scatter(*xf[u], color="#bf2435", s=28, depthshade=False)
        ax.text(*xf[u], " U", color="#bf2435", fontsize=12)
    for f in A["stable_face_ids"]:
        p = xf[faces[f]].mean(axis=0)
        ax.text(*p, " S", color="#1163a2", fontsize=12)
    for dim, fn in enumerate([ax.set_xlim, ax.set_ylim, ax.set_zlim]):
        fn(mid[dim] - rad, mid[dim] + rad)
    ax.set_box_aspect((1, 1, 1))
    ax.view_init(el, az)
    ax.set_axis_off()
    ax.set_title(label, fontsize=12)
fig.suptitle(
    "C = 622  |  176 vertices · 311 edges · 137 maximal facets", fontsize=16, y=0.95
)
fig.text(
    0.5,
    0.08,
    "S: unique stable face (blue)   ·   U: unique unstable vertex (red)   ·   exact uniform-volume centroid: (0, 0, 0)",
    ha="center",
    fontsize=10,
)
fig.text(
    0.5,
    0.035,
    "Approximate orthographic views, original proportions. Exact equilibrium claims apply to the rational data, not a printed model.",
    ha="center",
    fontsize=10,
    color="#555555",
)
fig.subplots_adjust(left=0.01, right=0.99, bottom=0.12, top=0.88, wspace=0)
fig.savefig(ROOT / "gomboc_C622_views.png", dpi=170)
plt.close(fig)
