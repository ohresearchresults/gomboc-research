#!/usr/bin/env python3
"""Exact helpers for the isolated post-C17 actual-cell attack.

The source is the immutable rational endpoint produced by
``rank5_circuit_escape_continuation.py``.  The path below is a single affine
19-control displacement.  Five rows move freely in R^3 and rows 231/246 move
in two exact tangent directions of the supporting-shell plane.  Consequently
the two non-triangular maximal faces (the 17-gon base and 16-gon shell) remain
exactly planar; every other support and mechanics statement is rebuilt.
"""
from __future__ import annotations

import csv
import hashlib
import json
import sys
from collections import defaultdict
from fractions import Fraction as Q
from functools import lru_cache
from pathlib import Path
from types import SimpleNamespace

HERE = Path(__file__).resolve().parent
PARENT = HERE.parent
ROOT = PARENT.parents[2]
sys.path.insert(0, str(PARENT))

import rank5_circuit_escape as esc  # noqa: E402
import rank5_circuit_escape_continuation as cont  # noqa: E402
import rank5_exact_jacobian as rj  # noqa: E402
import rank5_exact_reconstruction as ex  # noqa: E402

sys.set_int_max_str_digits(0)

SOURCE = PARENT / "rank5_escape_continuation_cells" / "c17_residual_descent_endpoint.csv"
SOURCE_SHA256 = "6225f1215d303898a46c3139f250a8937d2e831d58fac46b340415ca7f5229f4"

# Exact root brackets.  Both have width 1e-10 and one Sturm-certified root.
MECH_LEFT = Q(8771715268, 10_000_000_000)
MECH_RIGHT = Q(8771715269, 10_000_000_000)
SUPPORT_LEFT = Q(9535026893, 10_000_000_000)
SUPPORT_RIGHT = Q(9535026894, 10_000_000_000)
SUPPORT_PRE_SAMPLE = Q(19, 20)
SUPPORT_FAR_SAMPLE = Q(24, 25)
END = Q(1)

MECH_CIRCUIT_FEATURES = ("U254_via_255", "H254_255_via_t")
SUPPORT_CIRCUIT = (255, 256, 257, 258)


def qs(z: Q) -> str:
    return esc.qs(Q(z))


def qv(text: str) -> Q:
    return esc.qv(text)


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def read_rows(path: Path = SOURCE):
    rows = {}
    for row in csv.DictReader(path.open()):
        rows[int(row["source_id"])] = tuple(
            Q(row[k]) for k in ("x_exact", "y_exact", "z_exact")
        )
    assert len(rows) == 119
    return rows


def write_rows(path: Path, rows) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["source_id", "x_exact", "y_exact", "z_exact", "x", "y", "z"])
        for i, p in sorted(rows.items()):
            w.writerow(
                [i, *(qs(z) for z in p), *(format(float(z), ".17g") for z in p)]
            )


def control_spec():
    out = []
    for row in (228, 229, 254, 255, 256):
        for axis, label in enumerate("xyz"):
            v = [Q(0)] * 3
            v[axis] = Q(1)
            out.append((row, f"r{row}_{label}", tuple(v)))
    # Both directions are exactly tangent to 100*x + 20*y - 6*z = 3700.
    for row in (231, 246):
        out.append((row, f"r{row}_u", (Q(1, 5), Q(-1), Q(0))))
        out.append((row, f"r{row}_v", (Q(3, 50), Q(0), Q(1))))
    assert len(out) == 19
    assert all(ex.dot(ex.N, v) == 0 for row, _, v in out if row in {231, 246})
    return out


# Rationalized minimum-L-infinity hard-moment endpoint.  The generating LP
# required a 1% first-order decrease of the inherited eight deaths, crossed
# U254/H(254,255), retained one negative witness for every non-equilibrium
# feature, and retained every support slack and every base/U8 component.
DIRECTION = tuple(
    Q(z)
    for z in (
        "106725183/1000000000",
        "-13526271/200000000",
        "194515963/1000000000",
        "194515963/1000000000",
        "36375659/500000000",
        "10563569/1000000000",
        "194515963/1000000000",
        "194515963/1000000000",
        "-2835821/1000000000",
        "194515963/1000000000",
        "4861467/1000000000",
        "1859929/200000000",
        "38785309/200000000",
        "-194515963/1000000000",
        "10337797/250000000",
        "-409597/500000000",
        "-40821943/1000000000",
        "30923089/1000000000",
        "194515963/1000000000",
    )
)


def direction_rows(rows0):
    delta = {i: [Q(0), Q(0), Q(0)] for i in rows0}
    for (row, _, basis), coefficient in zip(control_spec(), DIRECTION):
        for k in range(3):
            delta[row][k] += coefficient * basis[k]
    out = {i: tuple(v) for i, v in delta.items()}
    assert ex.dot(ex.N, out[231]) == 0 and ex.dot(ex.N, out[246]) == 0
    return out


def path_rows(parameter: Q, rows0=None):
    rows0 = read_rows() if rows0 is None else rows0
    delta = direction_rows(rows0)
    return {i: ex.add(p, ex.mul(delta[i], Q(parameter))) for i, p in rows0.items()}


def face_signature(faces):
    return {tuple(sorted(f["cycle"])) for f in faces}


def edge_set(faces):
    return esc.edge_set(faces)


def exact_cell(name: str, parameter: Q, rows0=None):
    rows = path_rows(parameter, rows0)
    faces = ex.exactify_faces(rows, ex.numeric_faces(rows))
    volume, centroid = ex.exact_mass(rows, faces)
    ef, active, fl, vl, el, stable, unstable, saddles = ex.exact_mechanics(
        rows, faces, centroid
    )
    edges = sorted(ef)
    stable_cycles = [faces[i]["cycle"] for i in stable]
    base_stable = any(set(c) == set(range(17)) for c in stable_cycles)
    missing_rails = sorted(esc.forced_rails() - set(edges))
    assert len(active) == 61 and base_stable and 8 in unstable and not missing_rails
    packet = {
        "name": name,
        "parameter_exact": qs(parameter),
        "parameter_decimal": float(parameter),
        "f_vector": [len(active), len(edges), len(faces)],
        "euler": len(active) - len(edges) + len(faces),
        "class": [len(stable), len(unstable), len(saddles)],
        "active_vertices": active,
        "maximal_face_cycles": [f["cycle"] for f in faces],
        "true_edges": [list(e) for e in edges],
        "stable_faces": stable_cycles,
        "unstable_vertices": unstable,
        "saddle_edges": [list(e) for e in saddles],
        "all_61_active": True,
        "base_stable": True,
        "U8_unstable": True,
        "forced_rails_present": 37,
        "all_37_forced_rails_present": True,
        "missing_forced_rails": [],
        "volume_exact": qs(volume),
        "centroid_exact": [qs(z) for z in centroid],
        "face_mechanics_ledger": fl,
        "vertex_mechanics_ledger": vl,
        "edge_mechanics_ledger": el,
    }
    return packet, rows, faces, centroid


def write_cell(directory: Path, name: str, parameter: Q, rows0=None):
    packet, rows, faces, centroid = exact_cell(name, parameter, rows0)
    csv_path = directory / f"{name}.csv"
    json_path = directory / f"{name}.json"
    write_rows(csv_path, rows)
    json_path.write_text(json.dumps(packet, indent=2) + "\n")
    record = {
        "name": name,
        "parameter_exact": qs(parameter),
        "f_vector": packet["f_vector"],
        "class": packet["class"],
        "csv": str(csv_path.relative_to(HERE)),
        "csv_sha256": sha256(csv_path),
        "ledger": str(json_path.relative_to(HERE)),
        "ledger_sha256": sha256(json_path),
    }
    return record, packet, rows, faces, centroid


def make_jets(rows, faces, spec=None):
    spec = control_spec() if spec is None else spec
    rj.M = len(spec)
    by_row = defaultdict(list)
    for k, (row, _, basis) in enumerate(spec):
        by_row[row].append((k, basis))
    q = {}
    for i, p in rows.items():
        xyz = []
        for axis in range(3):
            derivative = [Q(0)] * len(spec)
            for k, basis in by_row.get(i, []):
                derivative[k] = basis[axis]
            xyz.append(rj.J(Q(p[axis]), tuple(derivative)))
        q[i] = tuple(xyz)
    centroid, _ = rj.exact_centroid(q, faces)
    return q, centroid


def named_jet_features(rows, faces):
    q, centroid = make_jets(rows, faces)
    inc = esc.incidence(faces)

    def fc(vertices, edge):
        values = dict(rj.face_components(esc.face_by_vertices(faces, vertices), q, centroid))
        return values[edge] if edge in values else values[edge[::-1]]

    def ec(edge, component):
        e = tuple(sorted(edge))
        return rj.edge_components(e, inc[e], faces, q, centroid)[component]

    return [
        ("S228_264_246_via_246_228", fc([228, 264, 246], (246, 228))),
        ("U228_via_251", rj.vertex_support(228, 251, q, centroid)),
        ("U231_via_232", rj.vertex_support(231, 232, q, centroid)),
        ("U246_via_245", rj.vertex_support(246, 245, q, centroid)),
        ("H8_246_via_t", ec((8, 246), "t")),
        ("H228_254_via_beta2", ec((228, 254), "beta2")),
        ("H231_247_via_beta1", ec((231, 247), "beta1")),
        ("H236_237_via_beta1", ec((236, 237), "beta1")),
        ("U254_via_255", rj.vertex_support(254, 255, q, centroid)),
        ("H254_255_via_t", ec((254, 255), "t")),
    ]


def exact_named_values(rows, faces):
    return {name: jet.v for name, jet in named_jet_features(rows, faces)}


def symbolic_path(rows0, faces):
    delta = direction_rows(rows0)
    q = {
        i: tuple(esc.RP.make([p[k], delta[i][k]], [Q(1)]) for k in range(3))
        for i, p in rows0.items()
    }
    centroid, volume = esc.symbolic_centroid(q, faces)
    return q, centroid, volume


def named_symbolic_features(q, faces, centroid):
    inc = esc.incidence(faces)

    def fc(vertices, edge):
        face = esc.face_by_vertices(faces, vertices)
        values = cont.symbolic_face_components_general(face, q, centroid, read_rows(), Q(0))
        return values[edge] if edge in values else values[edge[::-1]]

    def ec(edge, component):
        e = tuple(sorted(edge))
        return esc.symbolic_edge_components(e, inc[e], faces, q, centroid)[component]

    return {
        "S228_264_246_via_246_228": fc([228, 264, 246], (246, 228)),
        "U228_via_251": esc.symbolic_vertex_support(228, 251, q, centroid),
        "U231_via_232": esc.symbolic_vertex_support(231, 232, q, centroid),
        "U246_via_245": esc.symbolic_vertex_support(246, 245, q, centroid),
        "H8_246_via_t": ec((8, 246), "t"),
        "H228_254_via_beta2": ec((228, 254), "beta2"),
        "H231_247_via_beta1": ec((231, 247), "beta1"),
        "H236_237_via_beta1": ec((236, 237), "beta1"),
        "U254_via_255": esc.symbolic_vertex_support(254, 255, q, centroid),
        "H254_255_via_t": ec((254, 255), "t"),
    }


def polynomial_record(power):
    power = esc.ptrim(list(power))
    primitive = esc.primitive_integer_polynomial(power)
    return {
        "degree": len(power) - 1,
        "primitive_integer_coefficients_ascending": [str(z) for z in primitive],
    }


def derivative_numerator(z):
    return esc.psub(
        esc.pmul(esc.pderivative(list(z.n)), list(z.d)),
        esc.pmul(list(z.n), esc.pderivative(list(z.d))),
    )


@lru_cache(maxsize=None)
def _root_count_cached(power: tuple[Q, ...], left: Q, right: Q):
    count, _ = esc.sturm_root_count(list(power), left, right)
    return count


def root_count(power, left: Q, right: Q):
    return _root_count_cached(tuple(power), Q(left), Q(right))


def rp_root_counts(z, left: Q, right: Q):
    return root_count(z.n, left, right), root_count(z.d, left, right)


def support_polynomial(poly_rows, ids):
    a, b, c, d = (poly_rows[i] for i in ids)
    return esc.ptrim(
        list(
            cont.pv_dot(
                cont.pv_sub(b, a),
                cont.pv_cross(cont.pv_sub(c, a), cont.pv_sub(d, a)),
            )
        )
    )


def polynomial_rows(rows0):
    delta = direction_rows(rows0)
    return {i: tuple((p[k], delta[i][k]) for k in range(3)) for i, p in rows0.items()}


def support_root_atlas(rows0, faces, left=Q(0), event_left=SUPPORT_LEFT, event_right=SUPPORT_RIGHT):
    poly_rows = polynomial_rows(rows0)
    ids = sorted(rows0)
    event_poly = support_polynomial(poly_rows, SUPPORT_CIRCUIT)
    event_primitive = [Q(z) for z in esc.primitive_integer_polynomial(event_poly)]
    assert root_count(event_primitive, event_left, event_right) == 1
    assert esc.peval(event_primitive, event_left) * esc.peval(event_primitive, event_right) < 0

    planar = 0
    in_face = 0
    strict = 0
    event_rows = []
    for fi, face in enumerate(faces):
        cycle = face["cycle"]
        a = cycle[0]
        tri = None
        for j in range(1, len(cycle) - 1):
            for k in range(j + 1, len(cycle)):
                if ex.cross(
                    ex.sub(rows0[cycle[j]], rows0[a]),
                    ex.sub(rows0[cycle[k]], rows0[a]),
                ) != ex.ZERO:
                    tri = (a, cycle[j], cycle[k])
                    break
            if tri is not None:
                break
        assert tri is not None
        aa, bb, cc = tri

        # A polygon can change its true boundary while its supporting plane
        # remains valid.  Consecutive-turn polynomials close that missing
        # event family.  The only polygons here are the fixed base and the
        # shell; the shell controls are exactly tangent to its fixed plane.
        if len(cycle) > 3:
            normal = face["n"]
            normal_poly = tuple((z,) for z in normal)
            for j in range(len(cycle)):
                prev = poly_rows[cycle[j - 1]]
                cur = poly_rows[cycle[j]]
                nxt = poly_rows[cycle[(j + 1) % len(cycle)]]
                turn = esc.ptrim(
                    list(
                        cont.pv_dot(
                            cont.pv_cross(cont.pv_sub(cur, prev), cont.pv_sub(nxt, cur)),
                            normal_poly,
                        )
                    )
                )
                assert esc.peval(turn, left) != 0
                assert root_count(turn, left, event_right) == 0
                in_face += 1
        for i in cycle:
            p = support_polynomial(poly_rows, (aa, bb, cc, i))
            assert p == [Q(0)]
            planar += 1
        for i in ids:
            if i in cycle:
                continue
            p = support_polynomial(poly_rows, (aa, bb, cc, i))
            assert esc.peval(p, left) != 0
            assert root_count(p, left, event_left) == 0
            count = root_count(p, event_left, event_right)
            if count:
                assert count == 1
                gcd = esc.pgcd(p, event_primitive)
                assert len(gcd) - 1 == len(event_primitive) - 1
                event_rows.append(
                    {
                        "face_index": fi,
                        "face_cycle": cycle,
                        "outside_row": i,
                        "polynomial_degree": len(p) - 1,
                    }
                )
            strict += 1
    assert len(event_rows) == 2
    return {
        "pre_cell_face_count": len(faces),
        "identically_planar_face_vertex_polynomials": planar,
        "strict_in_face_consecutive_turn_polynomials": in_face,
        "zero_in_face_boundary_roots_through_event_bracket": True,
        "strict_support_polynomials_checked": strict,
        "zero_support_roots_before_event_bracket": True,
        "event_polynomial": polynomial_record(event_primitive),
        "event_bracket_exact": [qs(event_left), qs(event_right)],
        "event_bracket_width_exact": qs(event_right - event_left),
        "event_root_count_exact": 1,
        "event_endpoint_signs": [
            1 if esc.peval(event_primitive, event_left) > 0 else -1,
            1 if esc.peval(event_primitive, event_right) > 0 else -1,
        ],
        "event_support_rows": event_rows,
        "only_two_support_rows_share_the_event": True,
    }


EDGE_COMPONENT_NAMES = ("t", "one_minus_t", "beta1", "beta2")


def _guard_record(kind, feature, component, z, left, right, expected_roots=0):
    nr, dr = rp_root_counts(z, left, right)
    assert nr == expected_roots and dr == 0
    return {
        "kind": kind,
        "feature": list(feature) if isinstance(feature, tuple) else feature,
        "component": str(component),
        "value_at_left_sign": 1 if z.at(left) > 0 else -1,
        "numerator_root_count": nr,
        "denominator_root_count": dr,
        "numerator_degree": len(z.n) - 1,
        "denominator_degree": len(z.d) - 1,
    }


def mechanics_guard_audit(
    rows0,
    faces,
    left: Q,
    right: Q,
    special_pair=False,
    reference_parameter: Q | None = None,
):
    """Complete four-component cone cover over a fixed combinatorial formula.

    Every present equilibrium keeps every defining component, except the two
    explicitly linked U254/H(254,255) components on the pre-wall formula.
    Every absent equilibrium gets one exact negative witness with no root.
    """
    reference_parameter = left if reference_parameter is None else reference_parameter
    reference_rows = path_rows(reference_parameter, rows0)
    # Rebuild the supplied fixed combinatorial formula exactly at the chosen
    # reference parameter; support validity is checked by exactify_faces.
    reference_faces = ex.exactify_faces(
        reference_rows, SimpleNamespace(faces=faces)
    )
    assert face_signature(reference_faces) == face_signature(faces)
    faces = reference_faces
    volume, centroid = ex.exact_mass(reference_rows, faces)
    ef, active, fl, vl, el, stable, unstable, saddles = ex.exact_mechanics(
        reference_rows, faces, centroid
    )
    q, symbolic_centroid, symbolic_volume = symbolic_path(rows0, faces)
    assert rp_root_counts(symbolic_volume, left, right) == (0, 0)
    inc = esc.incidence(faces)
    face_symbolic = [
        cont.symbolic_face_components_general(
            f, q, symbolic_centroid, reference_rows, reference_parameter
        )
        for f in faces
    ]
    neighbors = defaultdict(set)
    for a, b in inc:
        neighbors[a].add(b)
        neighbors[b].add(a)

    records = []
    special_seen = []
    for fi, f in enumerate(faces):
        values = face_symbolic[fi]
        if fi in stable:
            for edge, z in values.items():
                records.append(_guard_record("present_stable", f["cycle"], edge, z, left, right))
        else:
            candidates = [(edge, z) for edge, z in values.items() if z.at(left) < 0]
            candidates.sort(key=lambda item: item[1].at(left))
            chosen = None
            for edge, z in candidates:
                if rp_root_counts(z, left, right) == (0, 0):
                    chosen = (edge, z)
                    break
            assert chosen is not None, ("face witness", fi)
            records.append(_guard_record("absent_stable_witness", f["cycle"], chosen[0], chosen[1], left, right))

    for i in active:
        symbolic = {j: esc.symbolic_vertex_support(i, j, q, symbolic_centroid) for j in sorted(neighbors[i])}
        if i in unstable:
            for j, z in symbolic.items():
                expected = 1 if special_pair and i == 254 and j == 255 else 0
                records.append(_guard_record("present_unstable", i, j, z, left, right, expected))
                if expected:
                    special_seen.append("U254_via_255")
        else:
            candidates = [(j, z) for j, z in symbolic.items() if z.at(left) < 0]
            candidates.sort(key=lambda item: item[1].at(left))
            chosen = None
            for j, z in candidates:
                if rp_root_counts(z, left, right) == (0, 0):
                    chosen = (j, z)
                    break
            assert chosen is not None, ("vertex witness", i)
            records.append(_guard_record("absent_unstable_witness", i, chosen[0], chosen[1], left, right))

    for edge in sorted(inc):
        symbolic = esc.symbolic_edge_components(edge, inc[edge], faces, q, symbolic_centroid)
        if edge in saddles:
            for component, z in symbolic.items():
                expected = 1 if special_pair and edge == (254, 255) and component == "t" else 0
                records.append(_guard_record("present_saddle", edge, component, z, left, right, expected))
                if expected:
                    special_seen.append("H254_255_via_t")
        else:
            candidates = [(component, z) for component, z in symbolic.items() if z.at(left) < 0]
            candidates.sort(key=lambda item: item[1].at(left))
            chosen = None
            for component, z in candidates:
                if rp_root_counts(z, left, right) == (0, 0):
                    chosen = (component, z)
                    break
            assert chosen is not None, ("edge witness", edge)
            records.append(_guard_record("absent_saddle_witness", edge, chosen[0], chosen[1], left, right))

    if special_pair:
        assert sorted(special_seen) == sorted(MECH_CIRCUIT_FEATURES)
    else:
        assert not special_seen
    return {
        "interval_exact": [qs(left), qs(right)],
        "formula_f_vector": [len(active), len(ef), len(faces)],
        "reference_parameter_exact": qs(reference_parameter),
        "class_at_reference": [len(stable), len(unstable), len(saddles)],
        "guard_records": records,
        "guard_record_count": len(records),
        "complete_four_component_cone_cover": True,
        "special_linked_root_features": special_seen,
        "all_other_guard_numerators_and_all_denominators_have_zero_roots": True,
    }


def one_sided_support_bracket_mechanics_audit(
    rows0,
    faces,
    left: Q,
    right: Q,
    reference_parameter: Q,
):
    """Certify the far mechanics class immediately right of a support flip.

    The new diagonal is undefined at the algebraic wall.  Some barycentric
    rational functions therefore have a pole whose denominator contains the
    support-circuit polynomial.  Every selected cone component below has no
    numerator root in the isolating bracket; every denominator root in that
    bracket is proved to be the unique support root.  Its sign at the rational
    right endpoint thus persists throughout the open algebraic-right side.
    """
    assert left < reference_parameter == right
    reference_rows = path_rows(reference_parameter, rows0)
    # This endpoint is only 1e-10 beyond the wall, inside the numeric hull
    # merger tolerance.  Rebuild the already-proved far cycles exactly;
    # asking the floating hull to rediscover them would spuriously merge the
    # circuit into a nonplanar quadrilateral.
    reference_faces = ex.exactify_faces(
        reference_rows, SimpleNamespace(faces=faces)
    )
    assert face_signature(reference_faces) == face_signature(faces)
    faces = reference_faces
    _, reference_centroid = ex.exact_mass(reference_rows, faces)
    ef, active, fl, vl, el, stable, unstable, saddles = ex.exact_mechanics(
        reference_rows, faces, reference_centroid
    )
    q, symbolic_centroid, symbolic_volume = symbolic_path(rows0, faces)
    assert rp_root_counts(symbolic_volume, left, right) == (0, 0)
    incidence = esc.incidence(faces)
    neighbors = defaultdict(set)
    for a, b in incidence:
        neighbors[a].add(b)
        neighbors[b].add(a)

    event_power = support_polynomial(polynomial_rows(rows0), SUPPORT_CIRCUIT)
    event_power = tuple(Q(z) for z in esc.primitive_integer_polynomial(event_power))
    assert root_count(event_power, left, right) == 1

    def record(kind, feature, component, z):
        numerator_roots = root_count(z.n, left, right)
        denominator_roots = root_count(z.d, left, right)
        assert numerator_roots == 0
        shared_roots = 0
        shared_degree = 0
        if denominator_roots:
            common = esc.pgcd(list(z.d), list(event_power))
            shared_degree = len(common) - 1
            shared_roots = root_count(common, left, right)
            assert shared_roots == denominator_roots == 1
        value = z.at(reference_parameter)
        assert value != 0
        return {
            "kind": kind,
            "feature": list(feature) if isinstance(feature, tuple) else feature,
            "component": str(component),
            "right_endpoint_sign": 1 if value > 0 else -1,
            "numerator_root_count": numerator_roots,
            "denominator_root_count": denominator_roots,
            "denominator_roots_shared_with_support_event": shared_roots,
            "support_event_gcd_degree": shared_degree,
            "numerator_degree": len(z.n) - 1,
            "denominator_degree": len(z.d) - 1,
        }

    face_symbolic = [
        cont.symbolic_face_components_general(
            f, q, symbolic_centroid, reference_rows, reference_parameter
        )
        for f in faces
    ]
    records = []
    for fi, face in enumerate(faces):
        values = face_symbolic[fi]
        if fi in stable:
            for edge, z in values.items():
                assert z.at(reference_parameter) > 0
                records.append(record("present_stable", face["cycle"], edge, z))
        else:
            candidates = sorted(
                ((edge, z) for edge, z in values.items() if z.at(reference_parameter) < 0),
                key=lambda item: item[1].at(reference_parameter),
            )
            chosen = next(
                ((edge, z) for edge, z in candidates if root_count(z.n, left, right) == 0),
                None,
            )
            assert chosen is not None, ("face one-sided witness", fi)
            records.append(record("absent_stable_witness", face["cycle"], chosen[0], chosen[1]))

    for vertex in active:
        symbolic = {
            neighbor: esc.symbolic_vertex_support(vertex, neighbor, q, symbolic_centroid)
            for neighbor in sorted(neighbors[vertex])
        }
        if vertex in unstable:
            for neighbor, z in symbolic.items():
                assert z.at(reference_parameter) > 0
                records.append(record("present_unstable", vertex, neighbor, z))
        else:
            candidates = sorted(
                (
                    (neighbor, z)
                    for neighbor, z in symbolic.items()
                    if z.at(reference_parameter) < 0
                ),
                key=lambda item: item[1].at(reference_parameter),
            )
            chosen = next(
                (
                    (neighbor, z)
                    for neighbor, z in candidates
                    if root_count(z.n, left, right) == 0
                ),
                None,
            )
            assert chosen is not None, ("vertex one-sided witness", vertex)
            records.append(record("absent_unstable_witness", vertex, chosen[0], chosen[1]))

    for edge in sorted(incidence):
        symbolic = esc.symbolic_edge_components(
            edge, incidence[edge], faces, q, symbolic_centroid
        )
        if edge in saddles:
            for component, z in symbolic.items():
                assert z.at(reference_parameter) > 0
                records.append(record("present_saddle", edge, component, z))
        else:
            candidates = sorted(
                (
                    (component, z)
                    for component, z in symbolic.items()
                    if z.at(reference_parameter) < 0
                ),
                key=lambda item: item[1].at(reference_parameter),
            )
            chosen = next(
                (
                    (component, z)
                    for component, z in candidates
                    if root_count(z.n, left, right) == 0
                ),
                None,
            )
            assert chosen is not None, ("edge one-sided witness", edge)
            records.append(record("absent_saddle_witness", edge, chosen[0], chosen[1]))

    singular = [entry for entry in records if entry["denominator_root_count"]]
    assert singular
    assert any(entry["feature"] == [256, 258] for entry in singular)
    return {
        "isolating_bracket_exact": [qs(left), qs(right)],
        "reference_parameter_exact": qs(reference_parameter),
        "support_event_polynomial": polynomial_record(event_power),
        "support_event_root_count_exact": 1,
        "formula_f_vector": [len(active), len(ef), len(faces)],
        "class_at_right_endpoint": [len(stable), len(unstable), len(saddles)],
        "guard_records": records,
        "guard_record_count": len(records),
        "singular_guard_records": singular,
        "singular_guard_record_count": len(singular),
        "all_selected_numerators_root_free_in_bracket": True,
        "all_selected_denominator_roots_are_the_unique_support_event": True,
        "complete_four_component_cone_cover_on_open_algebraic_right_side": True,
    }


def linked_mechanics_event(rows0, faces):
    q, centroid, _ = symbolic_path(rows0, faces)
    features = named_symbolic_features(q, faces, centroid)
    u = features["U254_via_255"]
    h = features["H254_255_via_t"]
    common = esc.pgcd(list(u.n), list(h.n))
    primitive = [Q(z) for z in esc.primitive_integer_polynomial(common)]
    assert len(primitive) - 1 == 5
    assert esc.pdivmod(list(u.n), common)[1] == [Q(0)]
    assert esc.pdivmod(list(h.n), common)[1] == [Q(0)]
    assert root_count(primitive, MECH_LEFT, MECH_RIGHT) == 1
    assert u.at(MECH_LEFT) > 0 and u.at(MECH_RIGHT) < 0
    assert h.at(MECH_LEFT) > 0 and h.at(MECH_RIGHT) < 0

    monotone = []
    for name, z in features.items():
        derivative = derivative_numerator(z)
        assert root_count(derivative, Q(0), END) == 0
        assert esc.peval(derivative, Q(0)) < 0
        assert root_count(z.d, Q(0), END) == 0 and esc.peval(z.d, Q(0)) != 0
        monotone.append(
            {
                "name": name,
                "derivative_numerator_degree": len(derivative) - 1,
                "derivative_numerator_root_count_on_0_1": 0,
                "strictly_decreasing": True,
            }
        )
    return {
        "features": list(MECH_CIRCUIT_FEATURES),
        "common_polynomial": polynomial_record(primitive),
        "isolating_bracket_exact": [qs(MECH_LEFT), qs(MECH_RIGHT)],
        "bracket_width_exact": qs(MECH_RIGHT - MECH_LEFT),
        "sturm_root_count": 1,
        "both_numerators_divisible_by_common_polynomial": True,
        "both_positive_on_left_and_negative_on_right": True,
        "class_transition": [[2, 5, 5], [2, 4, 4]],
        "selected_feature_monotonicity": monotone,
        "all_ten_selected_components_strictly_decrease_on_0_1": True,
    }


def direction_gradient_certificate(rows0, faces):
    records = []
    for name, jet in named_jet_features(rows0, faces):
        derivative = sum((jet.d[k] * DIRECTION[k] for k in range(len(DIRECTION))), Q(0))
        assert jet.v > 0 and derivative < 0
        records.append(
            {
                "name": name,
                "value_exact": qs(jet.v),
                "value_decimal": float(jet.v),
                "gradient_exact": [qs(z) for z in jet.d],
                "directed_derivative_exact": qs(derivative),
                "directed_derivative_decimal": float(derivative),
                "relative_directed_derivative_decimal": float(derivative / jet.v),
            }
        )
    return {
        "control_names": [name for _, name, _ in control_spec()],
        "direction_exact": [qs(z) for z in DIRECTION],
        "feature_records": records,
        "all_ten_exact_directed_derivatives_strictly_negative": True,
        "exact_gradient_rank": rj.matrix_rank([jet.d for _, jet in named_jet_features(rows0, faces)]),
    }
