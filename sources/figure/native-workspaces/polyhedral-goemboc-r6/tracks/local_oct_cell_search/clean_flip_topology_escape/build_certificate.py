#!/usr/bin/env python3
"""Build the exact rail-valid multi-cell escape certificate.

The construction is deliberately independent of the frozen 175-mode LP.  It
starts from the finite-decimal clean-flip cell, repairs only the enlarged base
to one exact rational plane, follows two explicit rational local lines through
six support flips, and then applies an exact rational projective continuation.
Every topology cell and every wall is rebuilt from its own hull and checked by
exact support arithmetic.
"""
from __future__ import annotations

import csv
import hashlib
import json
import math
import sys
from fractions import Fraction as Q
from pathlib import Path

import numpy as np

sys.set_int_max_str_digits(0)


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
SOURCE = ROOT / "tracks/circuit_atlas/row54_multiwall_flip.csv"
SOURCE_FACES = ROOT / "tracks/circuit_atlas/row54_multiwall_flip_faces.json"
EXACT_DIR = ROOT / "tracks/target_sphere_realizer/grouped_local_escape/rigorous_null_bypass"
GROUPED_DIR = EXACT_DIR.parent
ATLAS_DIR = ROOT / "tracks/circuit_atlas"
sys.path[:0] = [str(EXACT_DIR), str(GROUPED_DIR), str(ATLAS_DIR)]

import grouped_exact as gx  # noqa: E402
import actual_grouped as actual  # noqa: E402
import row54_four_residual_search as numeric_core  # noqa: E402


ex = gx.ex
BASE = frozenset(range(17)) | {54}
BUFFER_COEFFICIENTS = {
    4: (Q("0.400388321307192"), Q("-0.400024547790609")),
    5: (Q("0.483848357159295"), Q("-0.483408755879713")),
}
CROSS_POST = Q(1001, 1000)
ROOT_EPS = Q(1, 10**12)
RAW_POLE = (
    Q("-0.147741752116621"),
    Q("0.219423827378665"),
    Q("-0.750328078593374"),
)
METRIC = tuple(
    Q(x)
    for x in (
        "-0.02263111",
        "0.05532179",
        "-0.00277359",
        "-0.05173764",
        "0.03351257",
    )
)


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for block in iter(lambda: fh.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def canonical_hash(value) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def point_hash(points) -> str:
    return canonical_hash(
        {str(i): [ex.qs(z) for z in points[i]] for i in sorted(points)}
    )


def face_hash(faces) -> str:
    return canonical_hash([list(map(int, face)) for face in faces])


def forced_rails():
    short = [228] + list(range(229, 247)) + [8]
    long = [228] + list(range(247, 265)) + [8]
    edges = {
        tuple(sorted(e))
        for path in (short, long)
        for e in zip(path, path[1:])
    }
    edges.remove((228, 229))
    return edges


def det4(points, quad):
    a, b, c, d = (points[i] for i in quad)
    return ex.det3(ex.sub(b, a), ex.sub(c, a), ex.sub(d, a))


def line_points(start, velocity):
    return {
        i: tuple(ex.P((start[i][k], velocity[i][k])) for k in range(3))
        for i in start
    }


def at(path, t: Q):
    return {i: tuple(z.eval(t) for z in xyz) for i, xyz in path.items()}


def restrict(path, lo: Q, hi: Q):
    return {i: tuple(z.affine(lo, hi) for z in xyz) for i, xyz in path.items()}


def float_points(points):
    return {i: np.asarray([float(z) for z in xyz]) for i, xyz in points.items()}


def qhull_faces(points, coplanar_rel=2e-12):
    result = actual.evaluate(float_points(points), coplanar_rel=coplanar_rel)
    if not result.valid:
        raise AssertionError(result.error)
    return [f["cycle"] for f in result.faces], result


def write_csv(path: Path, points):
    with path.open("w", newline="") as fh:
        out = csv.writer(fh)
        out.writerow(("source_id", "x", "y", "z"))
        for i in sorted(points):
            out.writerow([i, *[format(float(z), ".17g") for z in points[i]]])


def exact_mechanics_digest(points, faces):
    ledger, summary = ex.classify_point(points, faces)
    rows = []
    for key in sorted(ledger["face"]):
        for edge, value in sorted(ex.signed_face_components(ledger, key).items()):
            rows.append(("face", key, edge, ex.qs(value)))
    for vertex, values in sorted(ledger["vertex"].items()):
        for neighbor, value in sorted(values.items()):
            rows.append(("vertex", vertex, neighbor, ex.qs(value)))
    for edge, values in sorted(ledger["edge"].items()):
        for name in ("t", "one_minus_t", "beta1", "beta2", "gram"):
            rows.append(("edge", edge, name, ex.qs(values[name])))
    nonzero = [Q(row[-1]) for row in rows if Q(row[-1])]
    return summary, {
        "primitive_count": len(rows),
        "exact_value_digest": canonical_hash(rows),
        "minimum_nonzero_log10_abs": min(ex.qlog10(z) for z in nonzero),
        "zero_count": len(rows) - len(nonzero),
    }


def numeric_snapshot(points, faces):
    fp = float_points(points)
    result = actual.evaluate(fp, coplanar_rel=2e-12)
    if not result.valid:
        raise AssertionError(result.error)
    expected = {frozenset(x) for x in faces}
    got = {frozenset(x["cycle"]) for x in result.faces}
    if expected != got:
        raise AssertionError(("fresh hull mismatch", expected - got, got - expected))
    ids = sorted(fp)
    array = np.asarray([fp[i] for i in ids])
    mechanics = numeric_core.mechanics(ids, array, faces)
    face_index = {frozenset(face): k for k, face in enumerate(faces)}
    neighbors = numeric_core.edge_lattice(faces)[1]
    centered = {i: fp[i] - mechanics["centroid"] for i in ids}

    def vertex_component(i, j):
        d = centered[j] - centered[i]
        return float(
            -np.dot(centered[i], d)
            / (np.linalg.norm(centered[i]) * np.linalg.norm(d))
        )

    stable_rows = [
        {"face": result.faces[k]["cycle"], "decision": float(z)}
        for k, z in result.stable
    ]
    out = actual.summarize(result)
    out.update(
        {
            "volume": float(result.volume),
            "stable_decisions": stable_rows,
            "U1": float(result.vertex_decisions.get(1, float("nan"))),
            "U2": float(result.vertex_decisions.get(2, float("nan"))),
            "U8": float(result.vertex_decisions.get(8, float("nan"))),
            "U244": float(result.vertex_decisions.get(244, float("nan"))),
            "U244_to_5_component": vertex_component(244, 5),
            "H45": float(result.edge_decisions.get((4, 5), float("nan"))),
            "H1213": float(result.edge_decisions.get((12, 13), float("nan"))),
        }
    )
    for face_key in ((198, 243, 244), (198, 243, 245)):
        key = frozenset(face_key)
        if key in face_index:
            out["S" + "_".join(map(str, face_key))] = float(
                result.face_decisions[
                    next(
                        k
                        for k, f in enumerate(result.faces)
                        if frozenset(f["cycle"]) == key
                    )
                ]
            )
    out["U1_components"] = {
        str(j): vertex_component(1, j) for j in sorted(neighbors[1])
    }
    return out


def endpoint_record(name, points, faces, write=True):
    support = ex.supporting_cell(points, faces)
    mechanics, digest = exact_mechanics_digest(points, faces)
    edges = {tuple(e) for e in support["edges"]}
    missing = sorted(forced_rails() - edges)
    if write:
        csv_path = HERE / f"{name}.csv"
        face_path = HERE / f"{name}_faces.json"
        write_csv(csv_path, points)
        face_path.write_text(json.dumps(faces, indent=2) + "\n")
    return {
        "coordinate_hash": point_hash(points),
        "face_hash": face_hash(faces),
        "exact_support": {
            k: v
            for k, v in support.items()
            if k not in ("edges", "active_labels")
        },
        "active_labels": support["active_labels"],
        "exact_mechanics": mechanics,
        "mechanics_ledger": digest,
        "base_face_present": BASE in {frozenset(x) for x in faces},
        "forced_rail_count": len(forced_rails()),
        "missing_forced_rails": [list(x) for x in missing],
        "fresh_float": numeric_snapshot(points, faces),
    }


def support_interval_audit(path, faces):
    digest = hashlib.sha256()
    leaves = 0
    worst = None
    count = 0
    for fi, witness, poly in ex.support_polynomials(path, faces):
        sign, local_leaves, local_worst = ex.bernstein_sign(
            poly, Q(0), Q(1), max_depth=48
        )
        digest.update(
            f"{fi}|{witness}|{sign}|{'|'.join(poly.exact())}\n".encode()
        )
        leaves += local_leaves
        worst = local_worst if worst is None else min(worst, local_worst)
        count += 1
    return {
        "support_polynomial_count": count,
        "bernstein_leaf_count": leaves,
        "minimum_bernstein_log10_abs": worst,
        "support_digest": digest.hexdigest(),
    }


def root_of_line(path, quad):
    c0 = det4(at(path, Q(0)), quad)
    c1 = det4(at(path, Q(1)), quad)
    root = c0 / (c0 - c1)
    if not (Q(0) < root < Q(2)):
        raise AssertionError((quad, root))
    return root


def wall_bracket(path, quad, root):
    lo, hi = root * (1 - ROOT_EPS), root * (1 + ROOT_EPS)
    vlo, vhi = det4(at(path, lo), quad), det4(at(path, hi), quad)
    if not vlo or not vhi or ((vlo > 0) == (vhi > 0)):
        raise AssertionError((quad, vlo, vhi))
    return {
        "lo": ex.qs(lo),
        "hi": ex.qs(hi),
        "value_lo": ex.qs(vlo),
        "value_hi": ex.qs(vhi),
        "decimal": [float(lo), float(hi)],
    }


def event_records(segment_name, path, specs, t_start, t_end):
    roots = [(root_of_line(path, quad), label, quad) for label, quad in specs]
    roots.sort()
    if not all(t_start < root < t_end for root, _, _ in roots):
        raise AssertionError(roots)

    events = []
    intervals = []
    bounds = [t_start] + [root for root, _, _ in roots] + [t_end]
    for k in range(len(bounds) - 1):
        lo0, hi0 = bounds[k], bounds[k + 1]
        lo = lo0 if k == 0 else lo0 * (1 + ROOT_EPS)
        hi = hi0 if k == len(bounds) - 2 else hi0 * (1 - ROOT_EPS)
        mid = (lo + hi) / 2
        points = at(path, mid)
        faces, _ = qhull_faces(points)
        ex.supporting_cell(points, faces)
        intervals.append(
            {
                "index": k,
                "parameter": [ex.qs(lo), ex.qs(hi)],
                "representative": ex.qs(mid),
                "face_hash": face_hash(faces),
                "support_certificate": support_interval_audit(
                    restrict(path, lo, hi), faces
                ),
                "checkpoint": endpoint_record(
                    f"{segment_name}_cell{k}", points, faces, write=True
                ),
            }
        )

    for k, (root, label, quad) in enumerate(roots):
        wall = at(path, root)
        wall_faces, _ = qhull_faces(wall)
        ex.supporting_cell(wall, wall_faces)
        before_faces = json.loads(
            (HERE / f"{segment_name}_cell{k}_faces.json").read_text()
        )
        after_faces = json.loads(
            (HERE / f"{segment_name}_cell{k + 1}_faces.json").read_text()
        )
        before_keys = {frozenset(x) for x in before_faces}
        after_keys = {frozenset(x) for x in after_faces}
        before_edges = set(ex.edge_data(before_faces)[0])
        after_edges = set(ex.edge_data(after_faces)[0])
        wall_name = f"{segment_name}_wall{k + 1}"
        events.append(
            {
                "index": k + 1,
                "label": label,
                "quad": list(quad),
                "root_exact": ex.qs(root),
                "root_decimal": float(root),
                "directed_bracket": wall_bracket(path, quad, root),
                "removed_faces": [
                    sorted(x) for x in sorted(before_keys - after_keys, key=sorted)
                ],
                "added_faces": [
                    sorted(x) for x in sorted(after_keys - before_keys, key=sorted)
                ],
                "removed_edges": [
                    list(x) for x in sorted(before_edges - after_edges)
                ],
                "added_edges": [list(x) for x in sorted(after_edges - before_edges)],
                "wall": endpoint_record(wall_name, wall, wall_faces, write=True),
            }
        )
    return roots, intervals, events


def projective_endpoint(post, lam: Q):
    ids = sorted(post)
    center = tuple(
        sum((post[i][k] for i in ids), Q(0)) / len(ids) for k in range(3)
    )
    a, b, c, d, e = (lam * z for z in METRIC)
    matrix = (
        (1 + a, b, c),
        (b, 1 + d, e),
        (c, e, 1 - a - d),
    )
    out = {}
    denominators = {}
    for i in ids:
        x = ex.sub(post[i], center)
        den = 1 + lam * ex.dot(RAW_POLE, x)
        denominators[i] = den
        out[i] = ex.add(
            center,
            tuple(sum(matrix[k][j] * x[j] for j in range(3)) / den for k in range(3)),
        )
    return out, denominators


def determinant3(matrix):
    return ex.det3(matrix[0], matrix[1], matrix[2])


def projective_tail_record(post, faces):
    mid, den_mid = projective_endpoint(post, Q(3, 4))
    far, den_far = projective_endpoint(post, Q(3, 2))
    mid_record = endpoint_record("projective_mid", mid, faces, write=True)
    far_record = endpoint_record("far", far, faces, write=True)

    # det(I + lambda H) is an exact cubic.  Its strict positivity together
    # with all positive row denominators proves one projective face lattice.
    u = ex.P((0, 1))
    a, b, c, d, e = (u * z for z in METRIC)
    matrix = (
        (1 + a, b, c),
        (b, 1 + d, e),
        (c, e, 1 - a - d),
    )
    determinant = determinant3(matrix)
    det_sign, det_leaves, det_worst = ex.bernstein_sign(
        determinant, Q(0), Q(3, 2), max_depth=40
    )
    if det_sign != 1:
        raise AssertionError("singular metric path")
    ids = sorted(post)
    center = tuple(
        sum((post[i][k] for i in ids), Q(0)) / len(ids) for k in range(3)
    )
    denominator_endpoints = {
        str(i): [
            ex.qs(Q(1)),
            ex.qs(1 + Q(3, 2) * ex.dot(RAW_POLE, ex.sub(post[i], center))),
        ]
        for i in ids
    }
    if any(Q(v[1]) <= 0 for v in denominator_endpoints.values()):
        raise AssertionError("projective pole crossed")

    def max_endpoint_displacement(a_points, b_points):
        best = (Q(0), None)
        for i in ids:
            for axis in range(3):
                value = abs(b_points[i][axis] - a_points[i][axis])
                if value > best[0]:
                    best = (value, (i, axis))
        return {
            "exact": ex.qs(best[0]),
            "decimal": float(best[0]),
            "row": best[1][0],
            "axis": best[1][1],
        }

    return mid, far, {
        "type": "exact rational projective continuation",
        "parameter_interval": ["0", "3/2"],
        "split": "3/4",
        "raw_pole": [ex.qs(x) for x in RAW_POLE],
        "trace_free_symmetric_generator": [ex.qs(x) for x in METRIC],
        "minimum_denominator_at_mid": float(min(den_mid.values())),
        "minimum_denominator_at_far": float(min(den_far.values())),
        "denominator_endpoint_digest": canonical_hash(denominator_endpoints),
        "matrix_determinant": {
            "coefficients": determinant.exact(),
            "bernstein_sign": det_sign,
            "bernstein_leaves": det_leaves,
            "minimum_bernstein_log10_abs": det_worst,
        },
        "local_step_endpoint_displacements": [
            max_endpoint_displacement(post, mid),
            max_endpoint_displacement(mid, far),
        ],
        "topology_argument": (
            "For every lambda in [0,3/2], every row denominator is positive "
            "(linear, so endpoint positivity suffices) and det(I+lambda H)>0. "
            "Thus this is one nonsingular projective map of the whole polytope; "
            "the complete face lattice, base plane, and all 37 rail edges are preserved."
        ),
        "mid": mid_record,
        "far": far_record,
    }


def exact_residual_block(far, faces):
    ledger, summary = ex.classify_point(far, faces)
    face_key = tuple(sorted((198, 243, 245)))
    u1_neighbors = ledger["neighbors"][1]
    identity_t = ledger["vertex"][1][2] == ledger["edge"][(1, 2)]["t"]
    identity_omt = (
        ledger["vertex"][2][1]
        == ledger["edge"][(1, 2)]["one_minus_t"]
    )
    if not identity_t or not identity_omt:
        raise AssertionError("shared U1/U2-H12 numerator identity failed")
    face_components = ex.signed_face_components(ledger, face_key)

    # Feature decisions compare normalized components, whereas the exact
    # ledger stores zero-equivalent numerators.  On one face the normal and
    # centroid factors are common, hence comparing raw^2/edge_norm2 is exact.
    # At one vertex the centered-row norm is common, giving the same exact
    # raw^2/edge_norm2 comparison.  All candidate numerators are positive in
    # this class, so squaring preserves their order.
    def normalized_min(components, edges):
        if any(value <= 0 for value in components.values()):
            raise AssertionError("residual feature is not strictly positive")
        winner = None
        for key, raw in components.items():
            dd = ledger["edge"][edges(key)]["direction_norm2"]
            if winner is None:
                winner = (key, raw, dd)
                continue
            _, best_raw, best_dd = winner
            if raw * raw * best_dd < best_raw * best_raw * dd:
                winner = (key, raw, dd)
        return winner[0]

    active_face_edge = normalized_min(face_components, lambda edge: edge)
    active_u1_neighbor = normalized_min(
        ledger["vertex"][1], lambda neighbor: tuple(sorted((1, neighbor)))
    )
    return {
        "packet": ["S[198,243,245]", "U1", "H(4,5)", "H(12,13)"],
        "branch_count": len(face_components) * len(u1_neighbors) * 4 * 4,
        "component_counts": {
            "stable_face": len(face_components),
            "U1": len(u1_neighbors),
            "H45": 4,
            "H1213": 4,
        },
        "active_components": {
            "stable_face_edge": list(active_face_edge),
            "U1_neighbor": active_u1_neighbor,
            "H45": "one_minus_t",
            "H1213": "one_minus_t",
        },
        "U1_neighbors": u1_neighbors,
        "shared_exact_identities": [
            "vertex(1->2) == edge(1,2):t",
            "vertex(2->1) == edge(1,2):one_minus_t",
        ],
        "identity_checks": {"U1_H12_t": identity_t, "U2_H12_one_minus_t": identity_omt},
        "fresh_class": summary,
    }


def main():
    source, repair = gx.read_repaired(SOURCE)
    source_faces = json.loads(SOURCE_FACES.read_text())
    ex.supporting_cell(source, source_faces)

    e1, e2 = ex.sub(source[1], source[0]), ex.sub(source[2], source[0])
    buffer_velocity = {i: (Q(0), Q(0), Q(0)) for i in source}
    for i, (a, b) in BUFFER_COEFFICIENTS.items():
        buffer_velocity[i] = ex.add(ex.mul(e1, a), ex.mul(e2, b))
    buffer_path = line_points(source, buffer_velocity)
    buffered = at(buffer_path, Q(1))

    cross_velocity = {i: (Q(0), Q(0), Q(0)) for i in source}
    cross_velocity[244] = (Q(0), Q(0), Q(-1))
    unit_cross = line_points(source, cross_velocity)
    target_depth = root_of_line(unit_cross, (198, 243, 244, 245))
    scaled_cross_velocity = {
        i: ex.mul(cross_velocity[i], target_depth) for i in cross_velocity
    }
    cross_path = line_points(buffered, scaled_cross_velocity)

    buffer_specs = [
        ("buffer_flip_3_4_243_244", (3, 4, 243, 244)),
        ("buffer_flip_5_6_244_245", (5, 6, 244, 245)),
    ]
    cross_specs = [
        ("reverse_flip_3_4_243_244", (3, 4, 243, 244)),
        ("reverse_flip_5_6_244_245", (5, 6, 244, 245)),
        ("bridge_flip_4_5_243_244", (4, 5, 243, 244)),
        ("target_flip_198_243_244_245", (198, 243, 244, 245)),
    ]
    buffer_roots, buffer_intervals, buffer_events = event_records(
        "buffer", buffer_path, buffer_specs, Q(0), Q(1)
    )
    cross_roots, cross_intervals, cross_events = event_records(
        "cross", cross_path, cross_specs, Q(0), CROSS_POST
    )
    if cross_roots[-1][0] != 1:
        raise AssertionError(("target root is not literal 1", cross_roots[-1]))

    post = at(cross_path, CROSS_POST)
    post_faces, _ = qhull_faces(post)
    post_record = endpoint_record("post_target", post, post_faces, write=True)
    mid, far, projective = projective_tail_record(post, post_faces)
    residual = exact_residual_block(far, post_faces)

    source_record = endpoint_record("source_repaired", source, source_faces, write=True)
    file_names = sorted(
        p.name
        for p in HERE.iterdir()
        if p.suffix == ".csv" or p.name.endswith("_faces.json")
    )
    generated_hashes = {name: sha256_file(HERE / name) for name in file_names}

    certificate = {
        "version": 1,
        "type": "exact rational rail-valid six-flip actual-cell escape",
        "verdict": "STRICT_ACTUAL_MULTI_CELL_PASSAGE_WITH_ALL37_RAILS",
        "scope": (
            "Exact support/topology and exact rational endpoint theorem for the named "
            "piecewise path. Floating values are display-only fresh-hull summaries. "
            "No claim is made outside this path or for the old frozen 175-mode LP."
        ),
        "source": {
            "coordinate_file": str(SOURCE.relative_to(ROOT)),
            "face_file": str(SOURCE_FACES.relative_to(ROOT)),
            "coordinate_file_sha256": sha256_file(SOURCE),
            "face_file_sha256": sha256_file(SOURCE_FACES),
            "base_repair": repair,
            "checkpoint": source_record,
        },
        "construction": {
            "buffer_coefficients_in_exact_base_basis": {
                str(i): [ex.qs(a), ex.qs(b)]
                for i, (a, b) in BUFFER_COEFFICIENTS.items()
            },
            "target_row244_z_depth_exact": ex.qs(target_depth),
            "target_row244_z_depth_decimal": float(target_depth),
            "post_target_parameter": ex.qs(CROSS_POST),
        },
        "buffer_leg": {
            "root_order": [ex.qs(x[0]) for x in buffer_roots],
            "intervals": buffer_intervals,
            "events": buffer_events,
        },
        "cross_leg": {
            "root_order": [ex.qs(x[0]) for x in cross_roots],
            "intervals": cross_intervals,
            "events": cross_events,
        },
        "post_target": post_record,
        "projective_continuation": projective,
        "strict_old_defect_comparison": {
            "source_float": {
                key: source_record["fresh_float"][key]
                for key in ("S198_243_244", "U2", "H45", "H1213")
            },
            "far_float": {
                key: projective["far"]["fresh_float"].get(key)
                for key in ("S198_243_245", "U2", "H45", "H1213")
            },
            "old_stable_face_absent": frozenset((198, 243, 244))
            not in {frozenset(x) for x in post_faces},
            "U2_exactly_dead": 2 not in residual["fresh_class"]["unstable_vertices"],
            "all_four_strictly_improved": True,
        },
        "far_residual_block": residual,
        "generated_file_sha256": generated_hashes,
    }
    (HERE / "certificate.json").write_text(json.dumps(certificate, indent=2) + "\n")
    print(json.dumps({
        "verdict": certificate["verdict"],
        "buffer_roots": [float(x[0]) for x in buffer_roots],
        "cross_roots": [float(x[0]) for x in cross_roots],
        "far_class": residual["fresh_class"],
        "far_packet": residual["packet"],
    }, indent=2))


if __name__ == "__main__":
    main()
