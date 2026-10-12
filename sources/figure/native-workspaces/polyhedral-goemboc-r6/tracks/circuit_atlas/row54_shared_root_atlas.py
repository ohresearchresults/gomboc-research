#!/usr/bin/env python3
"""Nonlinear shared-root and first-event atlas for the row54 rank-six packet.

The starting point is the stationary raw-minimum metric on the clean
{2,3,88,242} flip cell.  Its six wrong mechanics signs are continued to a
common zero in six independent rank-revealing charts.  The continuation is
nonlinear: at homotopy time ``t`` it solves

    g_packet(x(t)) = (1-t) g_packet(x(0)).

Every accepted continuation node is checked by a fresh hull, its own volume
centroid, the enlarged base, U8, all 37 forced rail edges, and every fixed-cell
support/polygon guard.  If a branch leaves the actual cell before its shared
root, bisection localizes the first event and records a directional certificate
from the branch tangent.  Full mechanics components and full topology rows are
materialized for the best root or the furthest first-event blocker.
"""
from __future__ import annotations

import argparse
import csv
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Sequence

import numpy as np
from scipy.linalg import qr
from scipy.optimize import least_squares, linprog, root

import materialize_row54_cells as material
import row54_four_residual_search as core
import row54_guarded_escape as guarded


HERE = Path(__file__).resolve().parent
DEFAULT_SOURCE = HERE / "row54_multiwall_flip.csv"
DEFAULT_FACES = HERE / "row54_multiwall_flip_faces.json"
DEFAULT_START = HERE / "row54_multicell_rawmin_local_831593.json"


def jsonable(value: Any):
    if isinstance(value, np.ndarray):
        return value.tolist()
    if isinstance(value, (np.floating, np.integer)):
        return value.item()
    if isinstance(value, tuple):
        return [jsonable(x) for x in value]
    if isinstance(value, list):
        return [jsonable(x) for x in value]
    if isinstance(value, dict):
        return {str(k): jsonable(v) for k, v in value.items()}
    return value


def feature_key(label):
    kind, feature = label
    if kind.startswith("S"):
        return kind, tuple(sorted(feature))
    if kind.startswith("H"):
        return kind, tuple(sorted(feature))
    return kind, int(feature)


def face_set(faces: Sequence[Sequence[int]]):
    return {frozenset(c) for c in faces}


@dataclass
class State:
    t: float
    y: np.ndarray
    x: np.ndarray
    points: np.ndarray
    den: np.ndarray
    guards: np.ndarray
    topology: np.ndarray
    fresh: dict
    fresh_faces: list
    valid: bool
    invalid_reasons: list[str]


class Atlas:
    def __init__(self, source: Path, faces_path: Path, start_path: Path,
                 fd_step: float):
        ids, source_points, faces = guarded.load_problem(source, faces_path)
        self.ids = ids
        self.source_points = source_points
        self.expected_faces = faces
        self.problem = guarded.Problem(ids, source_points, faces)
        self.start_record = json.load(start_path.open())
        self.x0 = np.zeros(44)
        self.x0[:8] = np.asarray(self.start_record["theta"], dtype=float)
        p0, den0, g0, top0, _ = self.problem.evaluate(self.x0)
        self.g0 = g0
        self.top0 = top0
        self.active = g0 < 0.0
        if int(np.sum(self.active)) != 6:
            packet = [
                (float(g0[k]), self.problem.mech_labels[k])
                for k in np.flatnonzero(self.active)
            ]
            raise ValueError(("expected rank-six packet", packet))
        self.noncritical = ~self.active
        self.active_g0 = g0[self.active]
        # Equalities are scaled comparably without hiding their exact zeros.
        self.active_scales = np.maximum(np.abs(self.active_g0), 2.5e-4)
        self.fd_step = fd_step
        self.jm0, self.jt0 = self.finite_full(self.x0)
        self.start_state = self.make_state(0.0, np.zeros(6), self.x0, p0, den0,
                                           g0, top0)

    def finite_full(self, x):
        _, _, jm, jt = guarded.finite_jacobian(self.problem, x, self.fd_step)
        return jm, jt

    def finite_basis(self, x, basis, step=None):
        step = self.fd_step if step is None else step
        _, _, g0, t0, _ = self.problem.evaluate(x)
        jm = np.zeros((len(g0), basis.shape[1]))
        jt = np.zeros((len(t0), basis.shape[1]))
        for k in range(basis.shape[1]):
            h = step
            got = {}
            for _ in range(7):
                for sign in (1.0, -1.0):
                    trial = x + sign * h * basis[:, k]
                    try:
                        _, _, g, t, _ = self.problem.evaluate(trial)
                        got[sign] = (g, t)
                    except (ValueError, FloatingPointError):
                        pass
                if got:
                    break
                h *= 0.2
            if 1.0 in got and -1.0 in got:
                jm[:, k] = (got[1.0][0] - got[-1.0][0]) / (2.0 * h)
                jt[:, k] = (got[1.0][1] - got[-1.0][1]) / (2.0 * h)
            elif 1.0 in got:
                jm[:, k] = (got[1.0][0] - g0) / h
                jt[:, k] = (got[1.0][1] - t0) / h
            elif -1.0 in got:
                jm[:, k] = (g0 - got[-1.0][0]) / h
                jt[:, k] = (t0 - got[-1.0][1]) / h
            else:
                raise RuntimeError(("basis finite difference failed", k))
        return jm, jt

    def fresh_summary(self, points):
        try:
            audit, faces, mechanics = self.problem.fresh(points)
            edges, _ = core.edge_lattice(faces)
            fsets = face_set(faces)
            base_present = core.BASE in fsets
            # These are actual-cell facts, recomputed with the fresh centroid.
            base_stable = False
            if base_present:
                bi = next(k for k, c in enumerate(faces) if frozenset(c) == core.BASE)
                base_stable = bool(mechanics["fdec"][bi] > 0.0)
            u8 = float(mechanics["udec"].get(8, -np.inf))
            audit.update({
                "all_61_rows_active": mechanics["active"] == self.ids,
                "enlarged_base_present": base_present,
                "enlarged_base_stable": base_stable,
                "U8_decision": u8,
                "U8_unstable": u8 > 0.0,
                "forced_rail_edge_count": len(self.problem.forced),
                "all_forced_rail_edges_present": self.problem.forced <= set(edges),
                "missing_forced_rail_edges": [
                    list(e) for e in sorted(self.problem.forced - set(edges))
                ],
                "edge_0_1_present": (0, 1) in edges,
            })
            return audit, faces
        except Exception as exc:
            return {"fresh_hull_error": repr(exc)}, []

    def make_state(self, t, y, x, points=None, den=None, guards=None,
                   topology=None):
        if points is None:
            points, den, guards, topology, _ = self.problem.evaluate(x)
        fresh, faces = self.fresh_summary(points)
        reasons = []
        if float(np.min(den)) <= 0.06:
            reasons.append("projective_denominator")
        noncritical = guards[self.noncritical]
        if float(np.min(noncritical)) <= 0.0:
            reasons.append("nonpacket_mechanics_guard")
        if float(np.min(topology)) <= 0.0:
            reasons.append("fixed_topology_guard")
        expected = {
            "f_vector": [61, 162, 103],
            "faces_match_fixed_cell": True,
            "all_61_rows_active": True,
            "enlarged_base_present": True,
            "enlarged_base_stable": True,
            "U8_unstable": True,
            "all_forced_rail_edges_present": True,
            "edge_0_1_present": False,
        }
        for key, wanted in expected.items():
            if fresh.get(key) != wanted:
                reasons.append("fresh:" + key)
        return State(float(t), np.asarray(y).copy(), np.asarray(x).copy(),
                     np.asarray(points).copy(), np.asarray(den).copy(),
                     np.asarray(guards).copy(), np.asarray(topology).copy(),
                     fresh, faces, not reasons, reasons)

    def chart_bases(self):
        j = self.jm0[self.active] / self.active_scales[:, None]
        charts = []
        for family, cols0 in (
            ("metric", np.arange(8)),
            ("base", np.arange(8, 44)),
            ("joint", np.arange(44)),
        ):
            cols0 = np.asarray(cols0, dtype=int)
            block = j[:, cols0]
            _, singular, vt = np.linalg.svd(block, full_matrices=False)
            svd_basis = np.zeros((44, 6))
            svd_basis[cols0, :] = vt[:6].T
            charts.append((family + "_svd", svd_basis, {
                "family": family,
                "construction": "six right singular directions at rawmin",
                "singular_values": singular.tolist(),
            }))
            _, r, piv = qr(block, mode="economic", pivoting=True)
            selected = cols0[piv[:6]]
            qr_basis = np.zeros((44, 6))
            qr_basis[selected, np.arange(6)] = 1.0
            charts.append((family + "_qr", qr_basis, {
                "family": family,
                "construction": "six column-pivoted controls at rawmin",
                "selected_control_indices": selected.tolist(),
                "selected_control_names": [self.problem.chart.names[k] for k in selected],
                "selected_condition_number": float(np.linalg.cond(j[:, selected])),
                "R_diagonal": np.diag(r)[:6].tolist(),
            }))
        return charts

    def solve_at(self, basis, t, y_guess, max_nfev=180):
        target = (1.0 - t) * self.active_g0

        def residual(y):
            x = self.x0 + basis @ y
            try:
                _, den, guards, _, _ = self.problem.evaluate(x,
                                                               include_topology=False)
                if float(np.min(den)) <= 0.0600001:
                    return np.full(6, 1e4 + 1e3 * (0.0600001 - float(np.min(den))))
                return (guards[self.active] - target) / self.active_scales
            except Exception:
                return np.full(6, 1e5 + min(1e3, float(np.linalg.norm(y))))

        # This is a square six-equation chart.  MINPACK's hybrid corrector is
        # dramatically cheaper than a generic least-squares finite-difference
        # trust region (which re-evaluates the full 320+ mechanics packet for
        # every Jacobian column).  The predictor is already on the local
        # branch, so the hybrid solve normally needs one or two Jacobians.
        result = root(
            residual, np.asarray(y_guess), method="hybr",
            options={"xtol": 2e-10, "maxfev": max_nfev},
        )
        final_residual = residual(result.x)
        if float(np.max(np.abs(final_residual))) > 2e-7:
            # A short trust-region fallback handles an occasional component
            # switch in a min-defined face/vertex/edge decision.
            fallback = least_squares(
                residual, np.asarray(result.x), method="trf", jac="2-point",
                xtol=2e-11, ftol=2e-11, gtol=2e-11,
                max_nfev=min(max_nfev, 55), x_scale="jac",
            )
            if float(np.max(np.abs(residual(fallback.x)))) < float(
                    np.max(np.abs(final_residual))):
                result = fallback
        x = self.x0 + basis @ result.x
        try:
            points, den, guards, topology, _ = self.problem.evaluate(x)
        except Exception:
            return None, result
        error = float(np.max(np.abs((guards[self.active] - target) /
                                    self.active_scales)))
        if not np.isfinite(error) or error > 2e-7:
            return None, result
        return self.make_state(t, result.x, x, points, den, guards, topology), result

    def state_record(self, state: State):
        wrong = [
            {"value": float(state.guards[k]),
             "feature": self.problem.mech_labels[k]}
            for k in np.flatnonzero(state.guards <= 0.0)
        ]
        ordinary = [
            (float(state.guards[k]), self.problem.mech_labels[k], int(k))
            for k in np.flatnonzero(self.noncritical)
        ]
        ordinary.sort(key=lambda row: row[0])
        top_order = np.argsort(state.topology)[:8]
        return {
            "t": state.t,
            "parameters": state.x.tolist(),
            "chart_coordinates": state.y.tolist(),
            "minimum_projective_denominator": float(np.min(state.den)),
            "maximum_packet_target_residual": float(np.max(np.abs(
                state.guards[self.active] - (1.0 - state.t) * self.active_g0))),
            "packet_guards": [
                {"value": float(state.guards[k]),
                 "feature": self.problem.mech_labels[k]}
                for k in np.flatnonzero(self.active)
            ],
            "negative_packet": wrong,
            "minimum_nonpacket_mechanics_guard": ordinary[0][0],
            "closest_nonpacket_mechanics": [
                {"value": v, "feature": lab, "guard_index": k}
                for v, lab, k in ordinary[:12]
            ],
            "minimum_fixed_topology_guard": float(np.min(state.topology)),
            "closest_fixed_topology": [
                {"value": float(state.topology[k]),
                 "label": self.problem.top_labels[int(k)], "guard_index": int(k)}
                for k in top_order
            ],
            "valid_actual_cell": state.valid,
            "invalid_reasons": state.invalid_reasons,
            "fresh_hull_audit": state.fresh,
        }

    def continue_chart(self, name, basis, meta, nodes, minimum_step):
        t = 0.0
        y = np.zeros(6)
        dt = 1.0 / nodes
        state = self.start_state
        path = [self.state_record(state)]
        first_bad_pair = None
        solver_fail = None
        while t < 1.0 - 1e-13:
            target_t = min(1.0, t + dt)
            # Tangent predictor for the exact six-equation branch.
            jm, _ = self.finite_basis(state.x, basis)
            a = jm[self.active] / self.active_scales[:, None]
            rhs = (-self.active_g0 / self.active_scales) * (target_t - t)
            try:
                dy = np.linalg.solve(a, rhs)
            except np.linalg.LinAlgError:
                dy = np.linalg.lstsq(a, rhs, rcond=1e-12)[0]
            candidate, result = self.solve_at(basis, target_t, y + dy)
            if candidate is None:
                dt *= 0.5
                if dt < minimum_step:
                    solver_fail = {
                        "after_t": t,
                        "attempted_t": target_t,
                        "step": dt * 2.0,
                        "message": str(result.message),
                        "cost": None if not hasattr(result, "cost") else float(result.cost),
                        "optimality": None if not hasattr(result, "optimality") else
                            float(result.optimality),
                        "nfev": int(getattr(result, "nfev", -1)),
                    }
                    break
                continue
            if first_bad_pair is None and state.valid and not candidate.valid:
                first_bad_pair = (state, candidate)
            t, y, state = target_t, candidate.y, candidate
            path.append(self.state_record(state))
            # The actual-cell question is decided at the *first* event.  Do
            # not spend dozens of expensive fresh audits following an already
            # invalid branch.  A separate direct nonlinear corrector below
            # still computes the chart's shared root for the atlas.
            if first_bad_pair is not None:
                break
            # Once a corrector succeeds, cautiously restore the nominal grid.
            dt = min(1.0 / nodes, dt * 1.4)

        event = None
        event_state = None
        before_state = None
        if first_bad_pair is not None:
            before_state, event_state = self.refine_first_event(
                basis, first_bad_pair[0], first_bad_pair[1]
            )
            event = self.event_certificate(basis, before_state, event_state)
        # Independently solve the common six-wall root.  Extrapolating the
        # localized branch is usually better than a raw linear predictor, but
        # the latter is retained as a fallback for very early topology events.
        a0 = self.jm0[self.active] @ basis
        try:
            linear_root = np.linalg.solve(a0, -self.active_g0)
        except np.linalg.LinAlgError:
            linear_root = np.linalg.lstsq(a0, -self.active_g0, rcond=1e-12)[0]
        guesses = []
        if event_state is not None and event_state.t > 1e-8:
            guesses.append(event_state.y / event_state.t)
        guesses.append(linear_root)
        root = None
        root_solver = None
        for guess in guesses:
            candidate_root, result_root = self.solve_at(
                basis, 1.0, guess, max_nfev=110
            )
            root_solver = {
                "message": str(result_root.message),
                "nfev": int(getattr(result_root, "nfev", -1)),
                "success_flag": bool(getattr(result_root, "success", False)),
            }
            if candidate_root is not None:
                root = candidate_root
                break
        root_record = None if root is None else self.state_record(root)
        cone = None
        if root is not None and root.valid:
            cone = self.full_cone_audit(root)
        return {
            "name": name,
            "basis": basis.tolist(),
            "metadata": meta,
            "completed_shared_root": root is not None,
            "shared_root_valid_actual_cell": bool(root is not None and root.valid),
            "solver_failure": solver_fail,
            "shared_root_solver": root_solver,
            "first_event": event,
            "shared_root": root_record,
            "full_cone_audit": cone,
            "path": path,
        }, root, event_state

    def refine_first_event(self, basis, good: State, bad: State):
        lo, hi = good, bad
        for _ in range(20):
            if hi.t - lo.t < 2e-9:
                break
            tm = 0.5 * (lo.t + hi.t)
            f = (tm - lo.t) / (hi.t - lo.t)
            guess = (1.0 - f) * lo.y + f * hi.y
            mid, _ = self.solve_at(basis, tm, guess, max_nfev=260)
            if mid is None:
                hi = State(tm, guess, self.x0 + basis @ guess, hi.points,
                           hi.den, hi.guards, hi.topology, hi.fresh,
                           hi.fresh_faces, False, ["corrector_failure"])
            elif mid.valid:
                lo = mid
            else:
                hi = mid
        return lo, hi

    def event_certificate(self, basis, before: State, event: State):
        # Tangent imposed by d g_packet / dt = -g_packet(0).
        jm, jt = self.finite_basis(before.x, basis, step=self.fd_step * 0.5)
        a = jm[self.active]
        rhs = -self.active_g0
        try:
            dy_dt = np.linalg.solve(a, rhs)
        except np.linalg.LinAlgError:
            dy_dt = np.linalg.lstsq(a, rhs, rcond=1e-12)[0]
        dx_dt = basis @ dy_dt
        mech_rate = jm @ dy_dt
        top_rate = jt @ dy_dt
        candidates = []
        for k in np.flatnonzero(self.noncritical):
            candidates.append({
                "kind": "mechanics",
                "guard_index": int(k),
                "feature": self.problem.mech_labels[k],
                "value_before": float(before.guards[k]),
                "value_event_side": float(event.guards[k]),
                "directional_derivative": float(mech_rate[k]),
                "predicted_time_from_before": (
                    None if mech_rate[k] >= 0 else
                    float(-before.guards[k] / mech_rate[k])
                ),
            })
        for k in range(len(before.topology)):
            candidates.append({
                "kind": "topology",
                "guard_index": int(k),
                "feature": self.problem.top_labels[k],
                "value_before": float(before.topology[k]),
                "value_event_side": float(event.topology[k]),
                "directional_derivative": float(top_rate[k]),
                "predicted_time_from_before": (
                    None if top_rate[k] >= 0 else
                    float(-before.topology[k] / top_rate[k])
                ),
            })
        decreasing = [c for c in candidates if c["predicted_time_from_before"] is not None]
        decreasing.sort(key=lambda c: c["predicted_time_from_before"])
        actual_near = sorted(candidates, key=lambda c: abs(c["value_event_side"]))[:20]
        return {
            "bracket": [before.t, event.t],
            "t_width": event.t - before.t,
            "state_before": self.state_record(before),
            "state_event_side": self.state_record(event),
            "branch_tangent_chart": dy_dt.tolist(),
            "branch_tangent_controls": dx_dt.tolist(),
            "required_packet_derivatives": (-self.active_g0).tolist(),
            "realized_packet_derivatives": mech_rate[self.active].tolist(),
            "nearest_predicted_events": decreasing[:24],
            "nearest_actual_event_guards": actual_near,
        }

    def full_cone_audit(self, root: State):
        """Crossing cone at a valid six-wall root, using all 44 controls.

        The first LP finds a minimum-L-infinity direction which crosses all
        six walls.  The second maximizes the weakest normalized derivative of
        *every* other mechanics and topology inequality while retaining unit
        inward speed on the six walls.  Its dual marginals expose any exact
        first-order cone blocker rather than relying on a selected packet.
        """
        jm, jt = self.finite_full(root.x)
        jc = jm[self.active] / self.active_scales[:, None]
        n = 44
        # Variables [v(44), r].
        aub = []
        bub = []
        for row in jc:
            aub.append(np.r_[-row, 0.0])
            bub.append(-1.0)
        for k in range(n):
            row = np.zeros(n + 1); row[k] = 1.0; row[-1] = -1.0
            aub.append(row); bub.append(0.0)
            row = np.zeros(n + 1); row[k] = -1.0; row[-1] = -1.0
            aub.append(row); bub.append(0.0)
        c = np.zeros(n + 1); c[-1] = 1.0
        lp_min = linprog(c, A_ub=np.asarray(aub), b_ub=np.asarray(bub),
                         bounds=[(None, None)] * n + [(0.0, None)], method="highs")
        out = {
            "finite_difference_step": self.fd_step,
            "full_44_crossing_direction_exists": bool(lp_min.success),
            "minimum_Linf_lp_message": str(lp_min.message),
        }
        if not lp_min.success:
            return out
        v = lp_min.x[:n]
        out["minimum_Linf_control_norm"] = float(lp_min.x[-1])
        out["minimum_Linf_direction"] = v.tolist()
        out["packet_normalized_derivatives"] = (jc @ v).tolist()

        non_idx = np.flatnonzero(self.noncritical)
        mech_scales = np.maximum(np.abs(root.guards[non_idx]), 1e-5)
        top_scales = np.maximum(root.topology, 1e-9)
        jother = np.vstack((jm[non_idx] / mech_scales[:, None],
                            jt / top_scales[:, None]))
        other_labels = ([
            ("mechanics", int(k), self.problem.mech_labels[k]) for k in non_idx
        ] + [
            ("topology", int(k), self.problem.top_labels[k])
            for k in range(len(root.topology))
        ])
        # Variables [v(44), eta], |v| <= max(1, 1.2*minimum norm).
        radius = max(1.0, 1.2 * float(lp_min.x[-1]))
        aub = []
        bub = []
        for row in jc:
            aub.append(np.r_[-row, 0.0]); bub.append(-1.0)
        for row in jother:
            aub.append(np.r_[-row, 1.0]); bub.append(0.0)
        c = np.zeros(n + 1); c[-1] = -1.0
        lp_cone = linprog(c, A_ub=np.asarray(aub), b_ub=np.asarray(bub),
                          bounds=[(-radius, radius)] * n + [(None, None)],
                          method="highs")
        out.update({
            "complete_other_guard_count": len(other_labels),
            "cone_Linf_radius": radius,
            "all_guard_inward_lp_success": bool(lp_cone.success),
            "all_guard_inward_lp_message": str(lp_cone.message),
        })
        if lp_cone.success:
            vc = lp_cone.x[:n]
            eta = float(lp_cone.x[-1])
            rates = jother @ vc
            order = np.argsort(rates)[:30]
            out.update({
                "maximum_weakest_normalized_other_derivative": eta,
                "all_guard_direction": vc.tolist(),
                "packet_normalized_derivatives": (jc @ vc).tolist(),
                "weakest_other_derivatives": [
                    {"normalized_derivative": float(rates[k]),
                     "constraint": other_labels[int(k)]}
                    for k in order
                ],
            })
            marginals = np.asarray(lp_cone.ineqlin.marginals)
            # First six rows are packet constraints; remaining rows correspond
            # one-for-one to the complete other-guard list.
            dual = marginals[6:]
            dual_order = np.argsort(np.abs(dual))[::-1]
            out["largest_other_guard_dual_marginals"] = [
                {"dual_marginal": float(dual[k]),
                 "constraint": other_labels[int(k)]}
                for k in dual_order[:30] if abs(dual[k]) > 1e-10
            ]
        return out

    def complete_audit(self, state: State, name: str, certificate=None):
        hull, faces, normals = core.group_maximal_faces(self.ids, state.points)
        mechanics, stable, unstable, saddles = core.classify(self.ids, state.points,
                                                              faces)
        edges, _ = core.edge_lattice(faces)
        requested = material.requested_margins(
            mechanics, faces, {core.BASE}, {8}, set()
        )
        topology = material.topology_audit(self.ids, state.points, faces, normals)
        fixed_top_values, fixed_top_labels = guarded.topology_guards(
            self.ids, state.points, self.expected_faces
        )
        return {
            "version": 1,
            "name": name,
            "homotopy_time": state.t,
            "parameters": state.x.tolist(),
            "chart_coordinates": state.y.tolist(),
            "minimum_projective_denominator": float(np.min(state.den)),
            "transform_convention": (
                "move 18 enlarged-base rows in their fixed common base plane; "
                "then fixed-source-normalized projective + trace-free SPD map"
            ),
            "fresh_hull_audit": {
                "f_vector": [len(hull.vertices), len(edges), len(faces)],
                "active": mechanics["active"],
                "centroid": mechanics["centroid"].tolist(),
                "class": [len(stable), len(unstable), len(saddles)],
                "stable_faces": stable,
                "unstable_vertices": unstable,
                "saddle_edges": saddles,
                "faces_match_flip_cell": face_set(faces) == face_set(self.expected_faces),
                "enlarged_base_present": core.BASE in face_set(faces),
                "all_61_rows_active": mechanics["active"] == self.ids,
                "edge_0_1_present": (0, 1) in edges,
                "forced_rail_edge_count": len(self.problem.forced),
                "all_forced_rail_edges_present": self.problem.forced <= set(edges),
                "missing_forced_rail_edges": [
                    list(e) for e in sorted(self.problem.forced - set(edges))
                ],
            },
            "all_target_mechanics_margins_and_components": requested,
            "fresh_topology_audit": topology,
            "fixed_flip_cell_full_topology_guards": {
                "minimum": float(np.min(fixed_top_values)),
                "records": [
                    {"value": float(v), "label": lab}
                    for v, lab in zip(fixed_top_values, fixed_top_labels)
                ],
            },
            "directional_certificate": certificate,
        }, faces


def write_csv(path: Path, ids, points):
    with path.open("w", newline="") as f:
        w = csv.writer(f)
        w.writerow(("source_id", "x", "y", "z"))
        for i, p in zip(ids, points):
            w.writerow([i, *[format(float(z), ".17g") for z in p]])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--source", default=str(DEFAULT_SOURCE))
    ap.add_argument("--faces", default=str(DEFAULT_FACES))
    ap.add_argument("--start", default=str(DEFAULT_START))
    ap.add_argument("--fd-step", type=float, default=8e-6)
    ap.add_argument("--nodes", type=int, default=32)
    ap.add_argument("--minimum-step", type=float, default=2e-4)
    ap.add_argument("--charts", nargs="*", help="optional chart-name subset")
    ap.add_argument("--output", default="row54_shared_root_atlas.json")
    ap.add_argument("--artifact-prefix", default="row54_first_event_blocker")
    args = ap.parse_args()
    source = Path(args.source); faces = Path(args.faces); start = Path(args.start)
    atlas = Atlas(source, faces, start, args.fd_step)
    start_rank = guarded.rank_record(atlas.problem, atlas.jm0, atlas.active)
    branches = []
    material_candidates = []
    for name, basis, meta in atlas.chart_bases():
        if args.charts and name not in args.charts:
            continue
        print(json.dumps({"chart": name, "status": "starting"}), flush=True)
        record, root, event_state = atlas.continue_chart(
            name, basis, meta, args.nodes, args.minimum_step
        )
        branches.append(record)
        if root is not None and root.valid:
            material_candidates.append((2.0, name, root, record.get("full_cone_audit")))
        elif event_state is not None:
            # Prefer the branch that stays actual-cell-valid furthest toward
            # the common root.  Valid roots outrank all blockers.
            material_candidates.append((event_state.t, name, event_state,
                                        record["first_event"]))
        print(json.dumps({
            "chart": name,
            "completed_root": record["completed_shared_root"],
            "valid_root": record["shared_root_valid_actual_cell"],
            "first_event_t": None if record["first_event"] is None else
                record["first_event"]["bracket"],
            "solver_failure": record["solver_failure"],
        }), flush=True)

    selected = None
    if material_candidates:
        _, chart_name, selected_state, certificate = max(
            material_candidates, key=lambda row: row[0]
        )
        prefix = args.artifact_prefix
        if selected_state.t >= 1.0 - 1e-10 and selected_state.valid:
            prefix = "row54_shared_root_valid"
        audit, fresh_faces = atlas.complete_audit(
            selected_state, prefix, certificate=certificate
        )
        csv_name = prefix + ".csv"
        faces_name = prefix + "_faces.json"
        audit_name = prefix + "_audit.json"
        write_csv(HERE / csv_name, atlas.ids, selected_state.points)
        json.dump(fresh_faces, (HERE / faces_name).open("w"), indent=2)
        audit.update({
            "coordinates": csv_name,
            "fixed_expected_faces": faces_name,
            "selected_chart": chart_name,
        })
        json.dump(jsonable(audit), (HERE / audit_name).open("w"), indent=2)
        selected = {
            "chart": chart_name,
            "homotopy_time": selected_state.t,
            "valid_actual_cell": selected_state.valid,
            "coordinates": csv_name,
            "faces": faces_name,
            "audit": audit_name,
        }

    result = {
        "version": 1,
        "source": source.name,
        "faces": faces.name,
        "start": start.name,
        "homotopy": "g_six(x(t))=(1-t)g_six(x0)",
        "finite_difference_step": args.fd_step,
        "packet_labels": [
            atlas.problem.mech_labels[k] for k in np.flatnonzero(atlas.active)
        ],
        "packet_start_values": atlas.active_g0.tolist(),
        "start_state": atlas.state_record(atlas.start_state),
        "rank_at_start": start_rank,
        "branch_count": len(branches),
        "branches": branches,
        "selected_materialization": selected,
    }
    json.dump(jsonable(result), (HERE / args.output).open("w"), indent=2)
    print(json.dumps({
        "output": args.output,
        "branch_count": len(branches),
        "valid_shared_roots": [b["name"] for b in branches
                               if b["shared_root_valid_actual_cell"]],
        "selected_materialization": selected,
    }, indent=2), flush=True)


if __name__ == "__main__":
    main()
