# figure-0425

Historical AI scientific report · saved 2026-09-19 UTC. Claims below retain their original status and have not all been independently checked. The current retained construction is C622; the C<500 search remains open.

Public text derivative: internal-record-identifiers-replaced.

---

# Quiet Raven 11 — a 49-dimensional positive-width chart with exact finite mass normalization

Branch: `[internal-source-reference]`.

**No new own110/weak000 body is established by this handoff.** The durable result is a larger physical construction space outside the fixed-width theorem: an explicit **49-dimensional rational height chart**, with convexity given by linear inequalities, exact constant filled volume, and exact own-centroid normalization. Its open complex is **V53/E153/F102**. Every closed-chart member, and every nonsingular affine image of one, has **E≤153**. Adding the five affine-metric parameters gives a 54-parameter local construction space modulo rotations.

An important design correction is to **release the horizontal first moments rather than freeze them unnecessarily**. They can be allowed to change and then accounted for by translating to the actual filled centroid. Fixing volume and both horizontal first moments, followed by three affine-height gauge conditions, leaves the narrower 47-dimensional slice. The new chart fixes only volume and three gauge values, retaining two additional genuine width-redistribution directions.

The final section supplies a complete exact extension to the literal parent. It constructs the chart and defines a terminating, rational, nonuniform-width own121 calibration. That calibration is not presented as basin cancellation or as a freshly observed computational receipt.

## 1. Authority and the limit of the computational closeout

The required literal parent is `figure-0421`, SHA-256 `0249d8929405ba8d63199d59a43e6f4dbcc762401666816530147fd8239cf19e`. Its complete source capsule is the authority for the original coordinates and the exact auditors used below. The current journal and that parent were read in the preceding work in this chat; the unchanged sources are retained.

The geometric input is exactly `farthest_merged_G10000.json`, **2051 bytes**, SHA-256 `89599e0825f7075c151639b70d9db5959fcdc058c0be555d1a96d8598ccdea3e`. It contains all53 integer point rows on grid10000 and all102 oriented triangles. The original body is V53/E153/F102, own strict121, additional weak000, with volume

`1690203202641/1000000000000`.

Its actual centroid is

`(409355912737/135216256211280000, 855529297349/67608128105640000, 5154137003/270432512422560)`.

The interrupted width work attempted free-coordinate, actual-hull continuations and generated provisional output names including W48, OWN121, OWN312, OWN222 and HEIGHT47. **At closeout, readable successful execution receipts and complete visible literal coordinate tables for those new endpoints were not available.** I therefore do not promote their provisional counts, persistence numbers, or claimed rounding companions. In particular, this response does not establish a new C276, C282, C168 or other optimizer-produced body merely from an earlier scratch summary.

The missing continuation-critical material for those provisional numerical endpoints is their complete frozen point table or checkpoint, its matching producing source and parameters, and its matching exact hull/census receipt. A local filename or an attempted read is not a substitute. This limitation does not affect the mathematical chart below, whose exact input and complete source dependency closure are already present in the selected parent.

Canonical own110 remains C622. No failure of a finite numerical campaign, and no global exclusion of the new width chart, is claimed.

## 2. Physical heights, not auxiliary triangulation lifts

Write the literal input as

`p_i=(x_i,y_i,z_i), i=0,...,52`.

Keep the projected coordinates `(x_i,y_i)` and the original upper and lower triangulations. Replace the physical third coordinates by53 variable heights `h_i`.

These are actual boundary coordinates. They are not secondary-polytope lifts on an unchanged physical body. Changing an interior lower height changes the length of the vertical fibres above its piecewise-linear hat function. Changing upper heights does the analogous operation on the other skin.

The original projection has34 upper nodes and36 lower nodes, sharing17 silhouette nodes. Thus there are53 heights, not70 independently movable cap values. Shared silhouette heights make the two skins agree along the boundary of the projection.

For a triangle `t=(a,b,c)` and a projected input point j, let `lambda_a,lambda_b,lambda_c` be the exact planar barycentric coordinates of `(x_j,y_j)` relative to t. If the projected orientation of t is positive, the supporting inequality is

`lambda_a h_a + lambda_b h_b + lambda_c h_c - h_j ≥ 0`.

For negative projected orientation, reverse the sign. These are rational **linear inequalities in the physical heights**. Taking all102 triangles and all50 off-triangle points gives5100 such inequalities. The equivalent local formulation uses the136 original interior cap creases, but the global formulation is particularly convenient for an exact implementation.

Let `C` denote this closed height cone. Its strict version contains the original height vector. For every strict member, all102 original triangles remain maximal supporting facets and all53 vertices remain exposed. Therefore its actual maximal complex is exactly

**V53/E153/F102.**

On the closed boundary, faces can merge and vertices can cease to be extreme. The integration triangles must then not be counted as maximal faces. Nevertheless, the convex hull still has at most53 vertices, so its true edge count satisfies

`E≤3V−6≤153`.

This bound is independent of contact turnover and is preserved by nonsingular affine transformations.

### Positive width follows from the actual convexity conditions

Let `u_h` and `l_h` be the upper and lower piecewise-affine graph functions. The inequalities make `u_h` concave and `l_h` convex. Their difference

`w_h=u_h-l_h`

is concave, agrees with0 on the projection boundary, and is nonnegative on the whole projection. When its integral is positive, it is strictly positive in the interior. Hence

`K(h)={(x,y,z):(x,y)∈D, l_h(x,y)≤z≤u_h(x,y)}`

is an actual full-dimensional convex solid with a uniformly filled interior.

This is where the assumptions differ from SIGNED13. In SIGNED13 the function w was fixed. Here w is a physical variable. No old curvature-transfer fraction condition `0≤Rt≤1` is imposed or silently reused.

## 3. Exact finite volume and moment formulas

For each oriented triangle t, its determinant is linear in h. Write

`d_t(h)=k_t·h`.

Set

`D(h)=Σ_t d_t(h)=d·h`.

Then

`6V(h)=D(h)`.

If `s_t·h` denotes the sum of the three triangle heights, define

`N_x(h)=Σ_t (x_a+x_b+x_c)d_t(h)`,

`N_y(h)=Σ_t (y_a+y_b+y_c)d_t(h)`,

`N_z(h)=Σ_t d_t(h)(s_t·h)`.

The first two expressions are linear. The last is quadratic. With

`H=(1/2)Σ_t(k_t s_t^T+s_t k_t^T)`,

we have `N_z(h)=h^T H h`. The **actual uniformly filled centroid** is exactly

`c(h)=(N_x(h),N_y(h),h^T H h)/(4D(h))`.

There is no vertex-average substitution and no fixed reference center in this formula.

In graph notation the same facts are

`V=∫_D w`,

`M_x=∫_D xw`, `M_y=∫_D yw`,

`M_z=∫_D wm`, where `m=(u+l)/2`.

Thus width controls horizontal mass redistribution, while the vertical moment couples width and midpoint height. Keeping both horizontal moments fixed removes real width freedom; it is not required for an own-centroid construction.

## 4. A global rational gauge gives49 height parameters

Choose the three original projected anchor indices

`A={0,14,52}`.

They are noncollinear in the literal projection. Let `ell(x,y)` be the affine plane interpolating their original physical heights, and let `h0` be the original height vector. Put `D0=D(h0)>0`.

For any height vector h with positive volume, define

`a=D0/D(h)>0`.

Choose the unique affine function `b(x,y)` such that

`a h_i+b(x_i,y_i)=h0_i` for i in A.

Then

`h'_i=a h_i+b(x_i,y_i)`

has the original volume and the original three anchor heights. This transformation is a positive longitudinal affine transformation of the physical solid. It preserves convexity and incidence, and it does not change the solid's full affine orbit.

Consequently the normalized height space is

`C ∩ {d·h=D0, h_0=h0_0, h_14=h0_14, h_52=h0_52}`.

These four affine conditions are independent. Indeed, D annihilates all affine height functions1,x,y because adding an affine function to both skins does not change width. Evaluation at the three noncollinear anchors is invertible on that three-dimensional affine-function space. Finally D is nonzero because `D(h0)>0`.

Therefore the normalized chart has **exact dimension53−4=49**. Its strict convexity region has nonempty relative interior because it contains the strict original body.

For every member of this49-dimensional chart, translate by its exact centroid `c(h)`. This produces a homogeneous solid with exact own centroid0 and exact volume

`1690203202641/10^12`.

No additional equation fixing `M_x` or `M_y` is necessary. On this fixed-volume chart,

`c_x=N_x/(4D0)`, `c_y=N_y/(4D0)`, `c_z=h^T H h/(4D0)`.

In particular, for a finite height increment v,

`c_z(h+v)-c_z(h)=[2h^T Hv+v^T Hv]/(4D0)`.

Dropping the quadratic term would give only a tangent controller, not the finite mass closure supplied here.

A determinant-one lower-triangular metric map may subsequently be applied:

`L=[[a,0,0],[b,c,0],[d,e,1/(ac)]]`, with a,c>0.

Its five free parameters preserve centroid0 and the fixed volume. The three anchor conditions have already removed the longitudinal affine-height freedoms, so this supplies a54-parameter local shape/metric chart modulo rotations, not another copy of the old18-parameter fixed-width search.

**This is a construction space, not an own110 existence theorem.** It permits finite changes of the complete physical and polar landscapes, but neither landscape is automatically preserved.

## 5. A deterministic nonuniform-width calibration, with an explicit verification boundary

The source below defines a particular rational calibration without an optimizer trajectory.

Start with

`h_trial=h0+epsilon*e_3`.

Node3 is a lower interior cap node. Set

`a=D0/D(h_trial)`

and

`h=a*h_trial+(1-a)*ell`.

Because node3 is not an anchor, this fixes all three anchor heights and the actual volume exactly.

The width change is genuinely nonuniform. At projected node5, which is not changed by the node3 hat function,

`w_new(5)=a*w_old(5)`.

At projected node3,

`w_new(3)=a*(w_old(3)-epsilon)`.

For nonzero epsilon these ratios differ. An affine height shear cancels from width and cannot undo this difference. The construction therefore does not merely rename a fixed-width translation.

The deterministic parameter rule is to test

`epsilon=2^(16-k)`, for k=0,1,2,...,

in original grid units, and select the first value for which the original support inequalities are strict and the full own-centroid audit gives strict121 and additional weak000. This procedure terminates: the original strict hull and its strict/weak equilibrium classification have an open neighborhood, and epsilon tends to0. The limiting argument is used only to prove termination, not to assert that the selected change removes a basin.

The resulting rational body is uniquely defined by the literal input, anchor set, moved node and parameter rule. It is a **calibration of the new physical chart**, deliberately not a110 construction. Its physical and polar elder-rule bars are emitted by the supplied auditor.

**Execution status:** I do not have a readable successful execution receipt for the extension below in this closeout. Its terminal marker is therefore stated as expected, not observed. No new output byte count, hash, selected exponent, denominator statistic or persistence improvement is invented. The calibration should not be entered as an accepted computed successor until its replay receipt is obtained.

## 6. Complete exact source extension

This source is an exact extension to the supplied literal16-file parent capsule. Decode that capsule unchanged, then place the following file beside its recovered sources as `WIDTH49_EXACT.py`.

Exact dependencies, all present literally in the selected parent:

- `farthest_merged_G10000.json`, identified above;
- `fractional_y_exact.py` and `integer_census.py`;
- `LOWER_FACE_EXACT.py`, for the separate Fraction feature census;
- `freeze_controls.py`, for the independent projected mass identity and full physical/polar elder-rule certificates.

No research Library item, originating sandbox or numerical endpoint is a dependency. The parent payload must accompany this extension when handing it to a fresh executor; a parent hash alone is not a replacement for its literal capsule.

Use the parent's standard-library exact environment, CPython3.13.5 with assertions enabled:

    python -B -S WIDTH49_EXACT.py

Expected terminal marker after a successful replay:

    QR11_WIDTH49_DEFINED_OWN121_REPLAY_PASS 53 153 102

The script writes the exact49-dimensional basis, all linear support rows, all moment coefficients, the selected rational parameter, complete coordinates and maximal faces, both full feature censuses, projected mass checks, both elder-rule basin certificates, and a byte-count/SHA-256 manifest.

```python
from fractions import Fraction as Q
from pathlib import Path
import hashlib
import itertools
import json
import math
import sys

import fractional_y_exact as f
from integer_census import audit
from LOWER_FACE_EXACT import second_census
from freeze_controls import projected_mass, both_elder

ROOT = Path(__file__).resolve().parent
INPUT = 'farthest_merged_G10000.json'
INPUT_SHA = '89599e0825f7075c151639b70d9db5959fcdc058c0be555d1a96d8598ccdea3e'
ANCHORS = (0, 14, 52)
MOVED = 3
FIRST_EXPONENT = 16
GRID = 10000

if hasattr(sys, 'set_int_max_str_digits'):
    sys.set_int_max_str_digits(0)


def write(name, obj):
    f.save(str(ROOT / name), obj)


def primitive_plane(a, b, c):
    n = f.cross(f.sub(b, a), f.sub(c, a))
    assert any(n)
    row = tuple(n) + (f.dot(n, a),)
    den = math.lcm(*(x.denominator for x in row))
    integers = [int(x * den) for x in row]
    g = math.gcd(*integers)
    return tuple(x // g for x in integers)


def maximal_complex(points, triangles):
    # The supplied mesh is a valid oriented triangulation of the convex
    # boundary. Merge coplanar triangles before counting real features.
    groups = {}
    for t in triangles:
        key = primitive_plane(*(points[i] for i in t))
        groups.setdefault(key, []).append(t)
    faces = []
    for key, group in sorted(groups.items()):
        boundary = set()
        for t in group:
            for i, j in zip(t, t[1:] + t[:1]):
                if (j, i) in boundary:
                    boundary.remove((j, i))
                else:
                    assert (i, j) not in boundary
                    boundary.add((i, j))
        successor = {}
        for i, j in boundary:
            assert i not in successor
            successor[i] = j
        start = min(successor)
        face = [start]
        while successor[face[-1]] != start:
            face.append(successor[face[-1]])
            assert len(face) <= len(boundary)
        assert len(face) == len(boundary)
        changed = True
        while changed:
            changed = False
            for k in range(len(face)):
                a = points[face[k - 1]]
                b = points[face[k]]
                c = points[face[(k + 1) % len(face)]]
                if not any(f.cross(f.sub(b, a), f.sub(c, b))):
                    face.pop(k)
                    changed = True
                    break
        assert len(face) >= 3
        faces.append(face)
    used = sorted({i for face in faces for i in face})
    back = {i: j for j, i in enumerate(used)}
    return ([points[i] for i in used],
            [[back[i] for i in face] for face in faces], used)


def make_coefficients(points, triangles):
    n = len(points)
    K = []
    S = []
    for t in triangles:
        row = [Q(0)] * n
        summation = [Q(0)] * n
        for i, j, k in (t, t[1:] + t[:1], t[2:] + t[:2]):
            row[i] = points[j][0] * points[k][1] - points[j][1] * points[k][0]
            summation[i] = Q(1)
        assert sum(row[i] * points[i][2] for i in range(n)) == f.det(*(points[i] for i in t))
        K.append(row)
        S.append(summation)
    D = [sum(row[i] for row in K) for i in range(n)]
    Nx = [sum(K[k][i] * sum(points[j][0] for j in t)
              for k, t in enumerate(triangles)) for i in range(n)]
    Ny = [sum(K[k][i] * sum(points[j][1] for j in t)
              for k, t in enumerate(triangles)) for i in range(n)]
    H = [[sum((K[k][i] * S[k][j] + S[k][i] * K[k][j]) / 2
              for k in range(len(triangles)))
          for j in range(n)] for i in range(n)]
    return K, S, D, Nx, Ny, H


def support_rows(points, triangles):
    n = len(points)
    rows = []
    for t in triangles:
        a, b, c = [points[i] for i in t]
        den = f.side(a, b, c)
        assert den
        sign = 1 if den > 0 else -1
        for j, p in enumerate(points):
            if j in t:
                continue
            bary = [f.side(p, b, c) / den,
                    f.side(a, p, c) / den,
                    f.side(a, b, p) / den]
            assert sum(bary) == 1
            row = [Q(0)] * n
            for i, coefficient in zip(t, bary):
                row[i] += sign * coefficient
            row[j] -= sign
            rows.append(row)
    return rows


def value(row, h):
    return sum(a * b for a, b in zip(row, h))


def vertical_width(points, triangles, xy):
    values = set()
    for t in triangles:
        tri = [points[i] for i in t]
        sign = f.side(*tri)
        if all(f.side(tri[k], tri[(k + 1) % 3], xy) * sign >= 0
               for k in range(3)):
            values.add(f.val(f.plane(*tri), xy))
    assert len(values) == 2
    return max(values) - min(values)


def main():
    raw = (ROOT / INPUT).read_bytes()
    assert len(raw) == 2051
    assert hashlib.sha256(raw).hexdigest() == INPUT_SHA
    data = json.loads(raw)
    P = [tuple(map(Q, p)) for p in data['points']]
    T = [list(t) for t in data['T']]
    assert len(P) == 53 and len(T) == 102
    h0 = [p[2] for p in P]
    K, S, D, Nx, Ny, H = make_coefficients(P, T)
    D0 = value(D, h0)
    assert D0 == 6 * Q(1690203202641)

    affine_rows = [[Q(1)] * len(P),
                   [p[0] for p in P], [p[1] for p in P]]
    assert all(value(D, row) == 0 for row in affine_rows)
    assert f.side(*(P[i] for i in ANCHORS)) != 0
    constraints = [D]
    for i in ANCHORS:
        row = [Q(0)] * len(P)
        row[i] = Q(1)
        constraints.append(row)
    basis = f.kernel(constraints, len(P))
    assert len(basis) == 49
    assert all(value(row, b) == 0 for row in constraints for b in basis)

    rows = support_rows(P, T)
    assert len(rows) == 5100
    assert all(value(row, h0) > 0 for row in rows)
    V0, c0 = f.integrate(P, T)
    baseline_points = [f.sub(p, c0) for p in P]
    baseline = audit(baseline_points, T, grid=GRID)
    assert baseline['strict'] == [1, 2, 1]
    assert baseline['weak'] == [0, 0, 0]

    ell_plane = f.plane(*(P[i] for i in ANCHORS))
    ell = [f.val(ell_plane, p) for p in P]
    assert value(D, ell) == 0
    old_widths = [vertical_width(P, T, P[i][:2]) for i in (3, 5)]
    assert min(old_widths) > 0

    k = 0
    while True:
        epsilon = Q(2) ** (FIRST_EXPONENT - k)
        trial = h0.copy()
        trial[MOVED] += epsilon
        Dt = value(D, trial)
        k += 1
        if Dt <= 0:
            continue
        scale = D0 / Dt
        h = [scale * trial[i] + (1 - scale) * ell[i]
             for i in range(len(P))]
        assert value(D, h) == D0
        assert all(h[i] == h0[i] for i in ANCHORS)
        if not all(value(row, h) > 0 for row in rows):
            continue
        X = [(P[i][0], P[i][1], h[i]) for i in range(len(P))]
        volume, center = f.integrate(X, T)
        assert volume == V0
        Nz = sum(h[i] * H[i][j] * h[j]
                 for i in range(len(P)) for j in range(len(P)))
        predicted = [value(Nx, h) / (4 * D0),
                     value(Ny, h) / (4 * D0), Nz / (4 * D0)]
        assert list(center) == predicted
        centered = [f.sub(p, center) for p in X]
        points, faces, used = maximal_complex(centered, T)
        result = audit(points, faces, grid=GRID)
        if result['strict'] != [1, 2, 1] or result['weak'] != [0, 0, 0]:
            continue
        assert [result['V'], result['E'], result['F']] == [53, 153, 102]
        second = second_census(points, faces)
        assert second['strict'] == result['strict']
        assert second['weak'] == result['weak']
        assert second['volume_grid'] == V0
        assert list(result['centroid_grid']) == [0, 0, 0]
        new_widths = [vertical_width(X, T, P[i][:2]) for i in (3, 5)]
        assert new_widths[0] * old_widths[1] != new_widths[1] * old_widths[0]
        mass = projected_mass(points, faces)
        basins = both_elder(points, faces)
        break

    family = dict(
        input_sha256=INPUT_SHA, grid=GRID, anchors=ANCHORS,
        dimension=49, fixed_D=D0, basis=basis,
        support_rows=rows, D=D, Nx=Nx, Ny=Ny, H=H,
        definition='h=h0+sum(t_j*basis_j), support_rows @ h >= 0',
        centroid_formula='(Nx.h,Ny.h,h^T H h)/(4*D0)',
        open_complex=[53, 153, 102], closed_edge_upper_bound=153)
    selected = dict(
        grid=GRID, points=points, faces=faces, original_used=used,
        heights=h, epsilon=epsilon, selected_k=k-1,
        first_exponent=FIRST_EXPONENT, moved_node=MOVED,
        anchors=ANCHORS, raw_centroid=center,
        old_widths=old_widths, new_widths=new_widths,
        volume=V0 / GRID**3)
    objects = {
        'WIDTH49_FAMILY.json': family,
        'WIDTH49_SELECTED.json': selected,
        'WIDTH49_AUDIT.json': result,
        'WIDTH49_SECOND_CENSUS.json': second,
        'WIDTH49_PROJECTED_MASS.json': mass,
        'WIDTH49_BASINS.json': basins,
        'WIDTH49_BASELINE_AUDIT.json': baseline}
    for name, obj in objects.items():
        write(name, obj)
    manifest = {}
    for name in sorted(objects):
        b = (ROOT / name).read_bytes()
        manifest[name] = dict(bytes=len(b), sha256=hashlib.sha256(b).hexdigest())
    write('WIDTH49_MANIFEST.json', manifest)
    print('QR11_WIDTH49_DEFINED_OWN121_REPLAY_PASS',
          result['V'], result['E'], result['F'])
    print('SELECTED_EXACT_EPSILON', epsilon)
    print('STRICT', result['strict'], 'ADDITIONAL_WEAK', result['weak'])


if __name__ == '__main__':
    main()
```

## 7. Consequential continuation

The substantive next search space is the **full49-dimensional fixed-volume positive-width chart**, not its narrower horizontal-moment-locked slice and not another metric weighting inside SIGNED13. Its support inequalities are linear before centering; its true centroid is known exactly as a finite quadratic function on the chart. This makes it possible to optimize actual physical and same-center polar elder-rule persistence while retaining a large, explicit complexity reserve.

A finite step must use the complete updated centroid. At a contact boundary, coplanar triangles must be merged and redundant vertices removed before reporting V/E/F or equilibria. The largest physical bar, all other physical bars, all polar bars, strict counts, additional weak counts and conditioning should remain separate diagnostics. Allowing a temporary extra stable basin may open a different physical route, but its later removal must be demonstrated rather than inferred from a lower weighted objective.

The two original SIGNED13 pole inequalities do not constitute a theorem for this variable-width chart. Conversely, leaving that theorem's hypotheses does not itself prove that either complete unwanted basin can be removed.

**Final status:** the49-dimensional mass-normalized positive-width family and its complexity bound are proved; a complete exact recovery extension and a terminating rational calibration are supplied. New numerical endpoint receipts remain unconfirmed, no optimizer-produced body is promoted, and no own110 successor or global obstruction is claimed.
