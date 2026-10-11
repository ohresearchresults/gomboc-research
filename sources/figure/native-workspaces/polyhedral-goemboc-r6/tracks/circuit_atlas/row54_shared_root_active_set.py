#!/usr/bin/env python3
"""Active-set continuation of the row54 six-wall shared root in all 44 controls.

This is the chart-transition companion to ``row54_shared_root_atlas.py``.
Whenever the deterministic joint-QR branch meets a nonpacket mechanics or
fixed-topology wall, the wall's underlying scalar/circuit is held at its
strict rawmin value and the six-wall homotopy is restarted in a larger
rank-revealing chart.  Thus a removable first event changes charts, while a
repeated event is a directional active-cone obstruction.
"""
from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from pathlib import Path

import numpy as np
from scipy.linalg import qr
from scipy.optimize import linprog, root

import row54_shared_root_atlas as atlas_mod


HERE = Path(__file__).resolve().parent


@dataclass(frozen=True)
class Equation:
    kind: str
    index: int
    target: float
    scale: float
    key: tuple


class ActiveSet:
    def __init__(self, atlas: atlas_mod.Atlas, nodes: int, fd_step: float):
        self.a = atlas
        self.nodes = nodes
        self.fd_step = fd_step
        self.critical_indices = list(np.flatnonzero(atlas.active))
        self.preserved: list[Equation] = []

    def values(self, x, topology=True):
        points, den, guards, top, _ = self.a.problem.evaluate(
            x, include_topology=topology
        )
        return points, den, guards, top

    def equations(self):
        out = []
        for position, k in enumerate(self.critical_indices):
            out.append(Equation("mechanics", int(k), 0.0,
                                float(self.a.active_scales[position]),
                                ("packet", int(k))))
        out.extend(self.preserved)
        return out

    def equation_value(self, guards, top, eq: Equation):
        return guards[eq.index] if eq.kind == "mechanics" else top[eq.index]

    def target_at(self, eq: Equation, t):
        if eq.key[0] == "packet":
            pos = self.critical_indices.index(eq.index)
            return (1.0 - t) * self.a.active_g0[pos]
        return eq.target

    def normalized_jacobian_at_start(self, equations):
        rows = []
        for eq in equations:
            row = (self.a.jm0[eq.index] if eq.kind == "mechanics"
                   else self.a.jt0[eq.index])
            rows.append(row / eq.scale)
        return np.asarray(rows)

    def select_basis(self, equations, method="qr"):
        j = self.normalized_jacobian_at_start(equations)
        if method == "svd":
            _, singular, vt = np.linalg.svd(j, full_matrices=False)
            basis = vt.T
            selected = np.full(len(equations), -1, dtype=int)
            return basis, selected, singular, singular.copy()
        _, r, piv = qr(j, mode="economic", pivoting=True)
        selected = np.asarray(piv[:len(equations)], dtype=int)
        basis = np.zeros((44, len(equations)))
        basis[selected, np.arange(len(equations))] = 1.0
        singular = np.linalg.svd(j[:, selected], compute_uv=False)
        return basis, selected, singular, np.diag(r)[:len(equations)]

    def finite_basis(self, x, basis):
        return self.a.finite_basis(x, basis, step=self.fd_step)

    def solve_at(self, equations, basis, t, guess, maxfev=120):
        targets = np.asarray([self.target_at(eq, t) for eq in equations])
        scales = np.asarray([eq.scale for eq in equations])

        def residual(y):
            x = self.a.x0 + basis @ y
            try:
                _, den, guards, top = self.values(x)
                if float(np.min(den)) <= 0.0600001:
                    return np.full(len(equations), 1e5)
                vals = np.asarray([
                    self.equation_value(guards, top, eq) for eq in equations
                ])
                return (vals - targets) / scales
            except Exception:
                return np.full(len(equations), 1e6)

        result = root(residual, np.asarray(guess), method="hybr",
                      options={"xtol": 2e-10, "maxfev": maxfev})
        rr = residual(result.x)
        if not np.all(np.isfinite(rr)) or float(np.max(np.abs(rr))) > 3e-7:
            return None, result
        x = self.a.x0 + basis @ result.x
        points, den, guards, top = self.values(x)
        return self.a.make_state(t, result.x, x, points, den, guards, top), result

    def tangent(self, state, equations, basis):
        jm, jt = self.finite_basis(state.x, basis)
        rows = []
        rhs = []
        for eq in equations:
            rows.append(jm[eq.index] if eq.kind == "mechanics" else jt[eq.index])
            if eq.key[0] == "packet":
                pos = self.critical_indices.index(eq.index)
                rhs.append(-self.a.active_g0[pos])
            else:
                rhs.append(0.0)
        mat = np.asarray(rows)
        try:
            dy = np.linalg.solve(mat, np.asarray(rhs))
        except np.linalg.LinAlgError:
            dy = np.linalg.lstsq(mat, np.asarray(rhs), rcond=1e-12)[0]
        return dy, jm @ dy, jt @ dy

    def continuation(self, equations, basis):
        p0, d0, g0, t0, _ = self.a.problem.evaluate(self.a.x0)
        state = self.a.make_state(0.0, np.zeros(basis.shape[1]), self.a.x0,
                                  p0, d0, g0, t0)
        t = 0.0
        y = np.zeros(basis.shape[1])
        dt = 1.0 / self.nodes
        path = [self.a.state_record(state)]
        failure = None
        bad_pair = None
        while t < 1.0 - 1e-13:
            tn = min(1.0, t + dt)
            dy_dt, _, _ = self.tangent(state, equations, basis)
            candidate, result = self.solve_at(
                equations, basis, tn, y + (tn - t) * dy_dt
            )
            if candidate is None:
                dt *= 0.5
                if dt < 1e-5:
                    failure = {
                        "after_t": t,
                        "attempted_t": tn,
                        "message": str(result.message),
                        "nfev": int(getattr(result, "nfev", -1)),
                    }
                    break
                continue
            path.append(self.a.state_record(candidate))
            if state.valid and not candidate.valid:
                bad_pair = (state, candidate)
                break
            state, t, y = candidate, tn, candidate.y
            dt = min(1.0 / self.nodes, dt * 1.3)
        if bad_pair is None:
            return state if state.t >= 1.0 - 1e-10 else None, None, path, failure
        good, bad = self.refine(equations, basis, *bad_pair)
        event = self.event(equations, basis, good, bad)
        return None, event, path, failure

    def refine(self, equations, basis, good, bad):
        lo, hi = good, bad
        for _ in range(23):
            if hi.t - lo.t < 3e-10:
                break
            tm = 0.5 * (lo.t + hi.t)
            frac = (tm - lo.t) / (hi.t - lo.t)
            guess = (1.0 - frac) * lo.y + frac * hi.y
            mid, _ = self.solve_at(equations, basis, tm, guess, maxfev=180)
            if mid is not None and mid.valid:
                lo = mid
            else:
                hi = mid if mid is not None else hi
        return lo, hi

    def event(self, equations, basis, good, bad):
        dy, mech_rate, top_rate = self.tangent(good, equations, basis)
        candidates = []
        for k in np.flatnonzero(self.a.noncritical):
            if mech_rate[k] < 0.0:
                candidates.append({
                    "kind": "mechanics", "index": int(k),
                    "label": self.a.problem.mech_labels[k],
                    "value": float(good.guards[k]),
                    "event_side_value": float(bad.guards[k]),
                    "derivative": float(mech_rate[k]),
                    "time_from_good": float(-good.guards[k] / mech_rate[k]),
                })
        for k in range(len(good.topology)):
            if top_rate[k] < 0.0:
                candidates.append({
                    "kind": "topology", "index": int(k),
                    "label": self.a.problem.top_labels[k],
                    "value": float(good.topology[k]),
                    "event_side_value": float(bad.topology[k]),
                    "derivative": float(top_rate[k]),
                    "time_from_good": float(-good.topology[k] / top_rate[k]),
                })
        candidates.sort(key=lambda row: row["time_from_good"])
        return {
            "bracket": [good.t, bad.t],
            "good_state": self.a.state_record(good),
            "bad_state": self.a.state_record(bad),
            "tangent_chart": dy.tolist(),
            "packet_derivatives": mech_rate[self.a.active].tolist(),
            "predicted_events": candidates[:40],
        }

    def event_key(self, event):
        first = event["predicted_events"][0]
        if first["kind"] == "mechanics":
            label = first["label"]
            # U0 and H(0,54) are the same numerator.  Preserve U0 as the
            # canonical representative of this exact paired event.
            if label == ("U-", 0) or label == ("H-", [0, 54]):
                u0 = next(k for k, lab in enumerate(self.a.problem.mech_labels)
                          if lab == ("U-", 0))
                return ("mechanics", int(u0), ("radial_edge_numerator", 0, 54))
            return ("mechanics", int(first["index"]),
                    ("mechanics", atlas_mod.feature_key(label)))
        label = first["label"]
        circuit = tuple(sorted(set(label[2]) | {label[3]}))
        # Any support row of the same four-point circuit has the same oriented
        # determinant up to a positive scale in the current cell.
        representative = next(
            k for k, lab in enumerate(self.a.problem.top_labels)
            if lab[0] == "support" and tuple(sorted(set(lab[2]) | {lab[3]})) == circuit
        )
        return ("topology", int(representative), ("support_circuit", circuit))

    def add_event(self, key):
        kind, index, canonical = key
        if any(eq.key == canonical for eq in self.preserved):
            return False
        if kind == "mechanics":
            value = float(self.a.g0[index])
            scale = max(abs(value), 1e-4)
        else:
            value = float(self.a.top0[index])
            scale = max(abs(value), 1e-8)
        self.preserved.append(Equation(kind, index, value, scale, canonical))
        return True

    def active_cone(self, state, equations):
        """Full-44 feasibility and dual record at a repeated first event."""
        jm, jt = self.a.finite_full(state.x)
        aeq, beq = [], []
        preserved_rows = []
        preserved_keys = set()
        for eq in equations:
            row = jm[eq.index] if eq.kind == "mechanics" else jt[eq.index]
            if eq.key[0] == "packet":
                aeq.append(row / eq.scale)
                pos = self.critical_indices.index(eq.index)
                beq.append(-self.a.active_g0[pos] / eq.scale)
            else:
                # A bypass wall need only be kept on its admissible side.  It
                # is a cone inequality, not a spurious equality that forbids
                # moving deeper into the actual cell.
                preserved_rows.append((eq.kind, eq.index, row, eq.scale, eq.key))
                preserved_keys.add((eq.kind, eq.index))
        boundary_mech = [k for k in np.flatnonzero(self.a.noncritical)
                         if state.guards[k] < 1e-7]
        boundary_top = [k for k, v in enumerate(state.topology) if v < 1e-8]
        cone_rows = []
        cone_labels = []
        cone_scales = []
        for k in boundary_mech:
            cone_rows.append(jm[k]); cone_labels.append(("mechanics", k,
                self.a.problem.mech_labels[k])); cone_scales.append(max(abs(state.guards[k]), 1e-4))
        for k in boundary_top:
            cone_rows.append(jt[k]); cone_labels.append(("topology", k,
                self.a.problem.top_labels[k])); cone_scales.append(max(abs(state.topology[k]), 1e-7))
        for kind, index, row, scale, key in preserved_rows:
            if (kind, index) not in {
                    (lab[0], lab[1]) for lab in cone_labels}:
                cone_rows.append(row); cone_labels.append((kind, index, key)); cone_scales.append(scale)
        cone_rows = np.asarray(cone_rows)
        cone_scales = np.asarray(cone_scales)
        guard_aub = -cone_rows
        # Minimum-L-infinity tangent, rather than an arbitrary feasible basic
        # solution at control bounds.  This is the transverse direction that
        # can actually be integrated with a finite fresh-hull step.
        aub = np.c_[guard_aub, np.zeros(len(guard_aub))]
        box_rows = []
        for k in range(44):
            row = np.zeros(45); row[k] = 1.0; row[-1] = -1.0
            box_rows.append(row)
            row = np.zeros(45); row[k] = -1.0; row[-1] = -1.0
            box_rows.append(row)
        aub = np.vstack((aub, np.asarray(box_rows)))
        aeq45 = np.c_[np.asarray(aeq), np.zeros(len(aeq))]
        objective = np.zeros(45); objective[-1] = 1.0
        lp = linprog(objective, A_ub=aub,
                     b_ub=np.r_[np.zeros(len(guard_aub)), np.zeros(88)],
                     A_eq=aeq45, b_eq=np.asarray(beq),
                     bounds=[(-1e4, 1e4)] * 44 + [(0.0, 1e4)], method="highs")
        out = {
            "success": bool(lp.success), "status": int(lp.status),
            "message": str(lp.message),
            "boundary_mechanics": [
                {"index": k, "value": float(state.guards[k]),
                 "label": self.a.problem.mech_labels[k]} for k in boundary_mech
            ],
            "boundary_topology_count": len(boundary_top),
            "boundary_topology": [
                {"index": k, "value": float(state.topology[k]),
                 "label": self.a.problem.top_labels[k]} for k in boundary_top
            ],
            "minimum_Linf_norm": None if not lp.success else float(lp.x[-1]),
            "direction": None if not lp.success else lp.x[:44].tolist(),
        }
        if not lp.success:
            return out

        # Within a modest multiple of the minimum norm, maximize the weakest
        # normalized inward derivative of every active/preserved cone wall.
        # This avoids a numerically fragile tangent that has zero derivative
        # on hundreds of 1e-11 support slacks.
        radius = max(1.0, 2.0 * float(lp.x[-1]))
        inward_aub = np.c_[-cone_rows / cone_scales[:, None],
                           np.ones(len(cone_rows))]
        inward_aeq = np.c_[np.asarray(aeq), np.zeros(len(aeq))]
        inward_c = np.zeros(45); inward_c[-1] = -1.0
        inward = linprog(
            inward_c, A_ub=inward_aub, b_ub=np.zeros(len(inward_aub)),
            A_eq=inward_aeq, b_eq=np.asarray(beq),
            bounds=[(-radius, radius)] * 44 + [(None, None)], method="highs",
        )
        out.update({
            "inward_lp_success": bool(inward.success),
            "inward_lp_message": str(inward.message),
            "inward_Linf_radius": radius,
        })
        if inward.success:
            rates = cone_rows @ inward.x[:44] / cone_scales
            order = np.argsort(rates)[:30]
            out.update({
                "maximum_weakest_normalized_inward_derivative": float(inward.x[-1]),
                "inward_direction": inward.x[:44].tolist(),
                "weakest_inward_constraints": [
                    {"normalized_derivative": float(rates[k]),
                     "constraint": cone_labels[int(k)]} for k in order
                ],
            })
            if float(inward.x[-1]) > 1e-10:
                out["direction"] = inward.x[:44].tolist()
                out["selected_direction"] = "max_weakest_inward"
            else:
                out["selected_direction"] = "minimum_Linf"
        else:
            out["selected_direction"] = "minimum_Linf"
        return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--nodes", type=int, default=32)
    ap.add_argument("--stages", type=int, default=8)
    ap.add_argument("--fd-step", type=float, default=8e-6)
    ap.add_argument("--resume", help="resume stages/preserved equations from an earlier JSON")
    ap.add_argument("--basis", choices=("qr", "svd"), default="qr")
    ap.add_argument("--retry-last", action="store_true",
                    help="drop the final failed stage from --resume and retry it")
    ap.add_argument("--output", default="row54_shared_root_active_set.json")
    args = ap.parse_args()
    atlas = atlas_mod.Atlas(atlas_mod.DEFAULT_SOURCE, atlas_mod.DEFAULT_FACES,
                            atlas_mod.DEFAULT_START, args.fd_step)
    solver = ActiveSet(atlas, args.nodes, args.fd_step)
    stages = []
    if args.resume:
        old = json.load((HERE / args.resume).open())
        stages = old.get("stages", [])
        if args.retry_last and stages and stages[-1].get("failure"):
            stages = stages[:-1]

        def tuplify(value):
            return tuple(tuplify(x) for x in value) if isinstance(value, list) else value

        solver.preserved = [
            Equation(row["kind"], int(row["index"]), float(row["target"]),
                     float(row["scale"]), tuplify(row["key"]))
            for row in old.get("preserved_events", [])
        ]
    verdict = "ACTIVE_SET_LIMIT"
    root_state = None
    blocker_state = None
    cone = None
    for stage_index in range(len(stages), args.stages):
        equations = solver.equations()
        basis, selected, singular, rdiag = solver.select_basis(equations, args.basis)
        selected_names = [
            atlas.problem.chart.names[k] if k >= 0 else f"svd_direction_{j}"
            for j, k in enumerate(selected)
        ]
        print(json.dumps({
            "stage": stage_index, "equations": len(equations),
            "basis_method": args.basis, "selected": selected_names,
        }), flush=True)
        root_state, event, path, failure = solver.continuation(equations, basis)
        record = {
            "stage": stage_index,
            "equations": [eq.__dict__ for eq in equations],
            "selected_control_indices": selected.tolist(),
            "basis_method": args.basis,
            "selected_control_names": selected_names,
            "selected_singular_values": singular.tolist(),
            "selected_condition_number": float(singular[0] / singular[-1]),
            "R_diagonal": rdiag.tolist(),
            "root_found": root_state is not None,
            "root": None if root_state is None else atlas.state_record(root_state),
            "first_event": event,
            "failure": failure,
            "path": path,
        }
        stages.append(record)
        if root_state is not None and root_state.valid:
            verdict = "VALID_SHARED_ROOT"
            cone = atlas.full_cone_audit(root_state)
            break
        if event is None or not event["predicted_events"]:
            verdict = "CORRECTOR_OR_EVENT_LOCALIZATION_FAILURE"
            break
        key = solver.event_key(event)
        record["canonical_first_event"] = key
        if not solver.add_event(key):
            verdict = "REPEATED_FIRST_EVENT_ACTIVE_CONE_BLOCKER"
            # The good state is serialized in the event; reconstruct the last
            # actual numerical state by resolving the lower bracket.
            tgood = event["bracket"][0]
            guess = np.asarray(event["good_state"]["chart_coordinates"])
            blocker_state, _ = solver.solve_at(equations, basis, tgood, guess, 220)
            if blocker_state is not None:
                cone = solver.active_cone(blocker_state, equations)
            break
        print(json.dumps({"stage": stage_index, "added_event": key}), flush=True)

    # A square-chart corrector failure is not itself a geometric obstruction.
    # Audit the last valid node in the complete 44-control active cone before
    # assigning the verdict.  This also makes resumed post-processing cheap.
    if cone is None and stages and stages[-1].get("failure"):
        last = stages[-1]

        def tuple_key(value):
            return tuple(tuple_key(x) for x in value) if isinstance(value, list) else value

        last_equations = [
            Equation(row["kind"], int(row["index"]), float(row["target"]),
                     float(row["scale"]), tuple_key(row["key"]))
            for row in last["equations"]
        ]
        last_path = last.get("path", [])
        if last_path:
            row = last_path[-1]
            x = np.asarray(row["parameters"], dtype=float)
            y = np.asarray(row["chart_coordinates"], dtype=float)
            points, den, guards, top, _ = atlas.problem.evaluate(x)
            last_state = atlas.make_state(row["t"], y, x, points, den, guards, top)
            cone = solver.active_cone(last_state, last_equations)
            verdict = (
                "SQUARE_CHART_FAILURE_FULL44_CONE_FEASIBLE"
                if cone["success"] else
                "FULL44_ACTIVE_CONE_BLOCKER"
            )

    result = {
        "version": 1,
        "verdict": verdict,
        "source": atlas_mod.DEFAULT_SOURCE.name,
        "start": atlas_mod.DEFAULT_START.name,
        "packet_labels": [atlas.problem.mech_labels[k]
                          for k in solver.critical_indices],
        "packet_start_values": atlas.active_g0.tolist(),
        "stages": stages,
        "preserved_events": [eq.__dict__ for eq in solver.preserved],
        "full_cone_audit": cone,
    }
    json.dump(atlas_mod.jsonable(result), (HERE / args.output).open("w"), indent=2)
    print(json.dumps({
        "output": args.output, "verdict": verdict,
        "stage_count": len(stages),
        "preserved_events": [eq.key for eq in solver.preserved],
        "cone_success": None if cone is None else cone.get(
            "success", cone.get("full_44_crossing_direction_exists")),
    }, indent=2), flush=True)


if __name__ == "__main__":
    main()
