#!/usr/bin/env python3
"""Exact directed first-order audit for branch 4 of the flip atlas.

This script reconstructs the 175 displacement modes used by
``tracks/root_guarded_lp/row54_flip_guarded_lp.py`` from its audited cache,
treating every cached binary64 displacement as its exact dyadic rational.  It then
differentiates the normalized mechanics and support guards analytically.

Although a normalized primitive may contain square roots, its fractional
derivative is rational.  For example

    d log(P / sqrt(R S)) = dP/P - (dR/R + dS/S)/2.

Thus every row used here is an exact Fraction row for an explicitly defined
rational first-jet template.  We solve branch 4 numerically only to locate a
candidate, rationalize that candidate, and finally verify *every* death,
guard, and coefficient-box inequality using Fraction arithmetic.  The final
verdict is therefore exact for this directed first-order template; it is not
a nonlinear path assertion.
"""
from __future__ import annotations

import ast
import csv
import hashlib
import json
import math
from collections import defaultdict
from decimal import Decimal, localcontext
from fractions import Fraction as Q
from pathlib import Path

import numpy as np
from scipy.linalg import qr
from scipy.optimize import linprog

import rank4_flip_exact_ledger as ex


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
ATLAS = ROOT / "tracks" / "circuit_atlas"
ROOT_LP = ROOT / "tracks" / "root_guarded_lp"
CACHE = ROOT_LP / "row54_flip_guarded_jacobian.npz"
SOURCE = ATLAS / "row54_multiwall_flip.csv"
FACES_SOURCE = ATLAS / "row54_multiwall_flip_faces.json"
OUTPUT = HERE / "rank4_flip_exact_directed.json"

BASE_FACE = frozenset(range(17)) | {54}
EXTRA_FACE = frozenset((198, 243, 244))
EXTRA_U = 2
TARGET_U = 8
EXTRA_H = {(4, 5), (12, 13)}
BOUND = Q(20)
DEATH_BUFFER = Q(1, 1_000_000)


def qs(z: Q):
    return str(z.numerator) if z.denominator == 1 else f"{z.numerator}/{z.denominator}"


def qlog10(z: Q):
    if z == 0:
        return -math.inf
    return math.log10(abs(z.numerator)) - math.log10(z.denominator)


def q17(x: float):
    return Q(format(float(x), ".17g"))


def qbinary64(x: float):
    """Interpret the cached binary64 value itself as an exact dyadic."""
    return Q.from_float(float(x))


def read_rows_faces():
    rows = {}
    with SOURCE.open() as f:
        for row in csv.DictReader(f):
            rows[int(row["source_id"])] = tuple(Q(row[k]) for k in ("x", "y", "z"))
    return rows, json.loads(FACES_SOURCE.read_text())


def build_mode_jets(rows, displacement):
    ids = sorted(rows)
    n = displacement.shape[1]
    ex.D = n
    q = {}
    for ii, i in enumerate(ids):
        q[i] = tuple(
            ex.J(rows[i][axis], tuple(qbinary64(displacement[3 * ii + axis, k]) for k in range(n)))
            for axis in range(3)
        )
    return q, ids


def log_gradient(z):
    if z.v == 0:
        raise ZeroDivisionError("zero primitive in log derivative")
    return tuple(t / z.v for t in z.d)


def combine(*terms):
    """Linear combination of gradient tuples: combine((coefficient,row),...)."""
    n = len(terms[0][1])
    return tuple(sum((Q(a) * row[k] for a, row in terms), Q(0)) for k in range(n))


class ExactFractionalLedger:
    def __init__(self, q, faces):
        self.q = q
        self.faces = faces
        self.centroid, self.volume = ex.exact_centroid(q, faces)
        self.incidence, self.neighbors = ex.edge_data(faces)
        self.face_by_key = {tuple(sorted(cyc)): k for k, cyc in enumerate(faces)}
        self.normals = [ex.cycle_normal(cyc, q) for cyc in faces]
        self.memo = {}

    def face(self, key):
        _, face_key, edge_key = key
        fi = self.face_by_key[tuple(face_key)]
        cyc = self.faces[fi]
        n = self.normals[fi]
        h = ex.dot(n, ex.sub(self.q[cyc[0]], self.centroid))
        foot = ex.mul(n, h / ex.dot(n, n))
        x = {i: ex.sub(self.q[i], self.centroid) for i in cyc}
        ref = tuple(sum((x[i][k] for i in cyc), ex.J.c(0)) / len(cyc) for k in range(3))
        directed = next((a, b) for a, b in zip(cyc, cyc[1:] + cyc[:1])
                        if tuple(sorted((a, b))) == tuple(edge_key))
        a, b = directed
        e = ex.sub(x[b], x[a])
        p = ex.dot(ex.cross(e, ex.sub(foot, x[a])), n)
        reference = ex.dot(
            ex.cross(ex.sub(ex.values(x[b]), ex.values(x[a])),
                     ex.sub(ex.values(ref), ex.values(x[a]))),
            ex.values(n),
        )
        if reference < 0:
            p = -p
        e2, n2 = ex.dot(e, e), ex.dot(n, n)
        row = combine((1, log_gradient(p)), (-Q(1, 2), log_gradient(e2)),
                      (-Q(1, 2), log_gradient(n2)))
        return p.v, row

    def vertex(self, key):
        _, i, j = key
        xi = ex.sub(self.q[i], self.centroid)
        direction = ex.sub(self.q[j], self.q[i])
        p = -ex.dot(xi, direction)
        xi2, d2 = ex.dot(xi, xi), ex.dot(direction, direction)
        row = combine((1, log_gradient(p)), (-Q(1, 2), log_gradient(xi2)),
                      (-Q(1, 2), log_gradient(d2)))
        return p.v, row

    def edge(self, key):
        _, edge, component = key
        i, j = edge
        xi, xj = ex.sub(self.q[i], self.centroid), ex.sub(self.q[j], self.centroid)
        direction = ex.sub(xj, xi)
        t = -ex.dot(xi, direction) / ex.dot(direction, direction)
        if component == "t":
            return t.v, log_gradient(t)
        if component == "one_minus_t":
            omt = 1 - t
            return omt.v, log_gradient(omt)
        foot = ex.add(xi, ex.mul(direction, t))
        inc = self.incidence[tuple(edge)]
        n1, n2 = self.normals[inc[0]], self.normals[inc[1]]
        aa, bb, cc = ex.dot(n1, n1), ex.dot(n1, n2), ex.dot(n2, n2)
        r1, r2 = ex.dot(foot, n1), ex.dot(foot, n2)
        den = aa * cc - bb * bb
        beta1 = (r1 * cc - r2 * bb) / den
        beta2 = (r2 * aa - r1 * bb) / den
        qn = ex.dot(foot, foot)
        if component == "beta1":
            row = combine((1, log_gradient(beta1)), (Q(1, 2), log_gradient(aa)),
                          (-Q(1, 2), log_gradient(qn)))
            return beta1.v, row
        if component == "beta2":
            row = combine((1, log_gradient(beta2)), (Q(1, 2), log_gradient(cc)),
                          (-Q(1, 2), log_gradient(qn)))
            return beta2.v, row
        raise ValueError(key)

    def topology(self, key):
        _, face_key, witness = key
        fi = self.face_by_key[tuple(face_key)]
        cyc, n = self.faces[fi], self.normals[fi]
        p = ex.dot(n, ex.sub(self.q[cyc[0]], self.q[witness]))
        n2 = ex.dot(n, n)
        row = combine((1, log_gradient(p)), (-Q(1, 2), log_gradient(n2)))
        return p.v, row

    def row(self, key):
        if key not in self.memo:
            self.memo[key] = getattr(self, key[0])(key)
        return self.memo[key]


def selected_guards(keys, values):
    groups = {"face": defaultdict(list), "vertex": defaultdict(list), "edge": defaultdict(list)}
    topology = []
    for key in keys:
        if key[0] == "face":
            groups["face"][frozenset(key[1])].append(key)
        elif key[0] == "vertex":
            groups["vertex"][key[1]].append(key)
        elif key[0] == "edge":
            groups["edge"][key[1]].append(key)
        elif key[0] == "topology":
            topology.append(key)
    out = []
    for feature, candidates in groups["face"].items():
        if feature == EXTRA_FACE:
            continue
        if feature == BASE_FACE:
            out.extend((key, +1, "protected_base_component") for key in candidates)
        else:
            key = min(candidates, key=values.__getitem__)
            out.append((key, -1, "nonstable_face_witness"))
    for feature, candidates in groups["vertex"].items():
        if feature == EXTRA_U:
            continue
        if feature == TARGET_U:
            out.extend((key, +1, "protected_U8_support") for key in candidates)
        else:
            key = min(candidates, key=values.__getitem__)
            out.append((key, -1, "nonunstable_vertex_witness"))
    for feature, candidates in groups["edge"].items():
        if feature in EXTRA_H:
            continue
        key = min(candidates, key=values.__getitem__)
        out.append((key, -1, "nonsaddle_edge_witness"))
    out.extend((key, +1, "support_slack") for key in topology)
    return out


def dotq(row, vector):
    return sum((a * b for a, b in zip(row, vector)), Q(0))


def digest_rows(items):
    h = hashlib.sha256()
    for key, row in items:
        h.update(repr(key).encode())
        h.update(b"|")
        h.update("|".join(qs(z) for z in row).encode())
        h.update(b"\n")
    return h.hexdigest()


def solve_square_high_precision(a, b, dps=180):
    """Solve a rational active basis at high precision, then rationalize.

    A 150-plus dimensional Gauss-Jordan elimination over raw Fractions causes
    needless intermediate numerator growth.  LU at 180 decimal digits locates
    the same rational open feasible region; its displayed 150-digit decimals
    are then checked from scratch as exact Fractions against every inequality.
    The final theorem depends only on that exact postcheck, not on LU accuracy.
    """
    n = len(a)
    if any(len(row) != n for row in a):
        raise ValueError("not square")
    with localcontext() as ctx:
        ctx.prec = dps
        def dq(z):
            return Decimal(z.numerator) / Decimal(z.denominator)
        aa = [[dq(z) for z in row] + [dq(rhs)] for row, rhs in zip(a, b)]
        # Partial-pivoted Gaussian elimination.  Decimal arithmetic is only a
        # locator; the returned finite decimals undergo a full Fraction check.
        for col in range(n):
            pivot = max(range(col, n), key=lambda r: abs(aa[r][col]))
            if aa[pivot][col] == 0:
                raise ArithmeticError(("singular high-precision active basis", col))
            aa[col], aa[pivot] = aa[pivot], aa[col]
            p = aa[col][col]
            for r in range(col + 1, n):
                if aa[r][col] == 0:
                    continue
                factor = aa[r][col] / p
                aa[r][col] = Decimal(0)
                for k in range(col + 1, n + 1):
                    aa[r][k] -= factor * aa[col][k]
            if col and col % 25 == 0:
                print("high-precision elimination column", col, "/", n, flush=True)
        xx = [Decimal(0)] * n
        for r in range(n - 1, -1, -1):
            rhs = aa[r][n] - sum((aa[r][k] * xx[k] for k in range(r + 1, n)), Decimal(0))
            xx[r] = rhs / aa[r][r]
        # Exact finite decimals with a large safety reserve over the thin gap.
        return [Q(format(z, f".{dps - 30}g")) for z in xx]


def recover_exact_basic_solution(solve, guard_rows_exact, death_rows_exact, guard_info):
    """Recover the HiGHS vertex by an exact active-basis solve.

    Directly decimalizing a binary64 coefficient vector is unsafe here: the
    ultrathin support row has coefficients around 1e11, so harmless-looking
    1e-15 coefficient roundoff can consume the 3e-5 normalized survival gap.
    A dual-simplex solution is a vertex.  Fix its active box variables exactly
    at +/-20, select a rank-revealing square subset of its active general rows,
    and solve the remaining system over Fractions.
    """
    c0 = np.asarray(solve.x[:-1], dtype=float)
    delta0 = float(solve.x[-1])
    bound_indices = [k for k, z in enumerate(c0) if abs(abs(z) - float(BOUND)) < 1e-7]
    free_indices = [k for k in range(len(c0)) if k not in set(bound_indices)]
    fixed = {k: (BOUND if c0[k] > 0 else -BOUND) for k in bound_indices}
    target = Q(1) + DEATH_BUFFER

    equations = []
    # kind, source index, exact full coefficient row in (c,delta), exact rhs,
    # and the floating residual at the locator vertex.
    for k, logrow in enumerate(guard_rows_exact):
        loss = tuple(-z for z in logrow)
        residual = abs(sum(float(loss[j]) * c0[j] for j in range(len(c0))) - delta0)
        equations.append(("guard", k, loss + (-Q(1),), Q(0), residual))
    for k, logrow in enumerate(death_rows_exact):
        residual = abs(sum(float(logrow[j]) * c0[j] for j in range(len(c0))) + float(target))
        equations.append(("death", k, tuple(logrow) + (Q(0),), -target, residual))

    unknown_columns = free_indices + [len(c0)]
    needed = len(unknown_columns)
    # Include a generous set of nearly active rows, then QR-pivot their
    # transpose to obtain a well-conditioned independent row basis.
    ordered = sorted(equations, key=lambda z: z[4])
    pool = ordered[:max(needed * 6, needed + 40)]
    matrix = np.asarray([
        [float(eq[2][j]) for j in unknown_columns]
        for eq in pool
    ])
    _, r, piv = qr(matrix.T, mode="economic", pivoting=True)
    diag = np.abs(np.diag(r))
    rank = int(np.sum(diag > (diag[0] * 1e-11 if len(diag) else 0.0)))
    if rank < needed:
        raise ArithmeticError(("active row pool has insufficient rank", rank, needed,
                               len(bound_indices), len(free_indices)))
    chosen = [pool[int(k)] for k in piv[:needed]]

    exact_a, exact_b = [], []
    for eq in chosen:
        full, rhs = eq[2], eq[3]
        fixed_part = sum((full[k] * value for k, value in fixed.items()), Q(0))
        exact_a.append([full[k] for k in unknown_columns])
        exact_b.append(rhs - fixed_part)
    print("active recovery: fixed/free/basis", len(bound_indices), len(free_indices), needed,
          "best locator residual", chosen[0][4], "worst chosen", max(z[4] for z in chosen),
          flush=True)
    solution = solve_square_high_precision(exact_a, exact_b)
    candidate = [Q(0)] * len(c0)
    for k, value in fixed.items():
        candidate[k] = value
    for k, value in zip(free_indices, solution[:-1]):
        candidate[k] = value
    delta = solution[-1]
    basis = []
    for eq in chosen:
        if eq[0] == "guard":
            key, kind = guard_info[eq[1]]
            label = {"type": "guard", "key": repr(key), "kind": kind}
        else:
            label = {"type": "death", "death_index": eq[1]}
        label["locator_residual"] = eq[4]
        basis.append(label)
    return candidate, delta, {
        "fixed_box_variable_count": len(bound_indices),
        "free_coefficient_count": len(free_indices),
        "square_active_basis_size": needed,
        "active_basis": basis,
    }


def main():
    saved = np.load(CACHE, allow_pickle=True)
    displacement = np.asarray(saved["displacement"], dtype=float)
    keys = [ast.literal_eval(str(z)) for z in saved["primitive_keys"]]
    values = {key: float(v) for key, v in zip(keys, saved["primitive_values"])}
    mode_meta = [json.loads(str(z)) for z in saved["mode_meta"]]
    rows, faces = read_rows_faces()
    q, ids = build_mode_jets(rows, displacement)
    if displacement.shape != (3 * len(ids), len(mode_meta)):
        raise AssertionError(displacement.shape)
    ledger = ExactFractionalLedger(q, faces)
    guards = selected_guards(keys, values)

    # Candidate branch 0 from the complete 144-branch numerical atlas.  Solver
    # rankings disagree at O(1e-5), so this is merely a proposal; the exact
    # all-row postcheck below decides its sign independently.
    deaths = [
        ("face", (198, 243, 244), (198, 243)),
        ("vertex", 2, 1),
        ("edge", (4, 5), "t"),
        ("edge", (12, 13), "t"),
    ]
    death_rows_exact = [ledger.row(key)[1] for key in deaths]

    guard_rows_exact = []
    guard_rows_float = []
    guard_info = []
    for count, (key, sign, kind) in enumerate(guards, 1):
        primitive, logrow = ledger.row(key)
        # Sign is already absorbed by f'/f: requested signed guard sign*f has
        # the same logarithmic derivative as f.
        if (primitive > 0) != (sign > 0):
            raise AssertionError(("exact primitive sign mismatch", key, primitive, sign))
        guard_rows_exact.append(logrow)
        guard_rows_float.append([-float(z) for z in logrow])  # fractional loss
        guard_info.append((key, kind))
        if count % 1000 == 0:
            print("built exact guard rows", count, "/", len(guards), flush=True)

    guard_matrix = np.asarray(guard_rows_float, dtype=float)
    death_matrix = np.asarray([[float(z) for z in row] for row in death_rows_exact])
    n = displacement.shape[1]
    a_ub = np.vstack((
        np.hstack((guard_matrix, -np.ones((len(guards), 1)))),
        np.hstack((death_matrix, np.zeros((4, 1)))),
    ))
    b_ub = np.r_[np.zeros(len(guards)), np.full(4, -float(1 + DEATH_BUFFER))]
    objective = np.r_[np.zeros(n), 1.0]
    solve = linprog(
        objective,
        A_ub=a_ub,
        b_ub=b_ub,
        bounds=[(-float(BOUND), float(BOUND))] * n + [(-1000.0, 1000.0)],
        method="highs-ds",
    )
    if not solve.success:
        raise RuntimeError(solve.message)
    print("analytic locator solved: delta", solve.x[-1], flush=True)

    candidate, delta_exact, active_basis = recover_exact_basic_solution(
        solve, guard_rows_exact, death_rows_exact, guard_info
    )

    death_survival = [-(Q(1) + dotq(row, candidate)) for row in death_rows_exact]
    guard_survival = [Q(1) + dotq(row, candidate) for row in guard_rows_exact]
    bound_survival = [BOUND - abs(z) for z in candidate]
    death_ok = all(z >= 0 for z in death_survival)
    guard_ok = all(z > 0 for z in guard_survival)
    bound_ok = all(z >= 0 for z in bound_survival)
    if not (death_ok and guard_ok and bound_ok and delta_exact < 1):
        worst_death = min(death_survival)
        worst_guard = min(guard_survival)
        worst_bound = min(bound_survival)
        raise AssertionError(("exact active-basis candidate failed", float(worst_death),
                              float(worst_guard), float(worst_bound), float(delta_exact)))

    worst_order = sorted(range(len(guards)), key=lambda k: guard_survival[k])[:24]
    exact_rows_for_digest = [
        *((key, row) for key, row in zip(deaths, death_rows_exact)),
        *((guards[k][0], guard_rows_exact[k]) for k in range(len(guards))),
    ]
    result = {
        "version": 1,
        "type": "exact rational strict-positive directed first-order branch",
        "verdict": "EXACT_BRANCH0_ALL_FOUR_DEATHS_WITH_EVERY_SELECTED_FIXED_CELL_GUARD_STRICTLY_POSITIVE",
        "scope": (
            "Exact Fraction theorem for the explicitly defined analytic first jet obtained by "
            "interpreting the 175 cached binary64 displacement modes as exact dyadics. This is not a "
            "nonlinear path or fresh-hull theorem."
        ),
        "source_csv": SOURCE.name,
        "faces_json": FACES_SOURCE.name,
        "mode_source": str(CACHE.relative_to(ROOT)),
        "mode_count": n,
        "primitive_key_count": len(keys),
        "selected_guard_count": len(guards),
        "branch_index_in_numerical_atlas": 0,
        "death_components": [repr(key) for key in deaths],
        "coefficient_box": "[-20,20]^175",
        "locator_lp": {
            "death_buffer": qs(DEATH_BUFFER),
            "floating_delta": float(solve.x[-1]),
            "floating_max_guard_loss": float(np.max(guard_matrix @ solve.x[:n])),
            "message": solve.message,
        },
        "exact_active_basis_recovery": {
            **active_basis,
            "delta_exact": qs(delta_exact),
            "delta_decimal": float(delta_exact),
            "strict_delta_below_one": delta_exact < 1,
        },
        "exact_rational_witness": {
            "coefficients_exact": [qs(z) for z in candidate],
            "nonzero_coefficients": [
                {"column": k, "coefficient_exact": qs(z), "coefficient_decimal": float(z),
                 "mode": mode_meta[k]}
                for k, z in enumerate(candidate) if z
            ],
            "death_slacks_exact": [qs(z) for z in death_survival],
            "death_slacks_decimal": [float(z) for z in death_survival],
            "minimum_death_slack_exact": qs(min(death_survival)),
            "minimum_death_slack_decimal": float(min(death_survival)),
            "minimum_guard_survival_exact": qs(min(guard_survival)),
            "minimum_guard_survival_decimal": float(min(guard_survival)),
            "minimum_guard_survival_log10": qlog10(min(guard_survival)),
            "minimum_coefficient_box_slack_exact": qs(min(bound_survival)),
            "all_four_death_inequalities": death_ok,
            "all_selected_guard_inequalities_strict": guard_ok,
            "all_coefficient_bounds": bound_ok,
        },
        "worst_exact_guards": [
            {
                "key": repr(guards[k][0]),
                "kind": guards[k][2],
                "survival_exact": qs(guard_survival[k]),
                "survival_decimal": float(guard_survival[k]),
                "fractional_loss_decimal": float(1 - guard_survival[k]),
            }
            for k in worst_order
        ],
        "exact_matrix_sha256": digest_rows(exact_rows_for_digest),
        "proof_obligations": {
            "death": "1 + (d log f_i) dot c <= 0 for all four named death components",
            "guard": "1 + (d log g_k) dot c > 0 for every selected protected/witness/support guard",
            "box": "abs(c_j) <= 20 for every rationalized mode coefficient",
        },
    }
    OUTPUT.write_text(json.dumps(result, indent=2) + "\n")
    print(result["verdict"])
    print("analytic locator delta", solve.x[-1])
    print("exact active-basis delta", float(delta_exact))
    print("exact minimum death slack", float(min(death_survival)))
    print("exact minimum guard survival", float(min(guard_survival)), repr(guards[worst_order[0]][0]))
    print("exact minimum box slack", float(min(bound_survival)))
    print("output", OUTPUT)


if __name__ == "__main__":
    main()
