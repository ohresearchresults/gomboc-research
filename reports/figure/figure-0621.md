# figure-0621

Historical AI scientific report · saved 2026-09-29 UTC. Claims below retain their original status and have not all been independently checked. The current retained construction is C622; the C<500 search remains open.

Public text derivative: internal-record-identifiers-replaced.

---

# Vivid Comet 47 — principal-basin continuation and an unresolved execution boundary

Branch: `[internal-source-reference]`.
Source parent: `figure-0619`, SHA-256 `28bc5fc5fc7ed10735aab14c4012dcdc4ca73119c5030b73b267e19a8b3d1ba0`.

## Status

**No newly verified polyhedron, exact endpoint census, or principal-Q cancellation is established in this continuation.** The last reconstructible clean entrances remain the parent’s VC47B bodies. In particular, PIVOT_G4_STAGE7 remains58/161/105, own211/additionalweak000 with its positive principal Q; PRUNED43_G8 remains43/123/82, own211/additionalweak000 with a deeper positive Q.

The interrupted work submitted direct one-stable-root nominations on the58-point and43-point geometries, followed by polar-relay and finite-forest mass-closure calculations. In this continuation, filesystem inspection, native-file reads, Python execution, short execution probes, and attempted inspection of the resulting logs returned **no inspectable output**. Therefore I do not infer that the submitted calculations completed, that their possible output files contain valid bodies, or that their optimizer status proves anything. I also do not infer that the mounted files were lost.

The retained reading record reaches lines1–1390 of the new2,225-line journal. I requested the remaining lines1391–2225 in consecutive chunks, but those responses were not inspectable. Consequently I cannot certify complete reading or newly authenticate the latest459,528-byte journal against its supplied SHA-256 `1ef7a6238ea011db5f363c5a8f0ec45c9a6c189cf402b75a8ce4713ddd523264`. The complete literal VC47B parent is still present in the preceding conversation and remains the source authority used below. No claim of novelty relative to the unread update is made.

The useful mathematical work preserved here is a **sharp finite centroid-range formulation for a specified lower/upper hull pair**, together with a complete prospective exact driver for principal polar relays on the current clean inputs. The formulation is proved below. Its numerical values and any resulting exclusion on PIVOT or PRUNED43 remain uncomputed; it is not presented as an instantiated obstruction or a new accepted body.

## 1. The actual continuation target

The parent’s detached stable carriers are not the whole principal basin. On PIVOT_G4_STAGE7, the junior is triangle(22,38,26), the saddle is28--42, and three of U10’s four incident facets lie in the37-vertex high polar component. On PRUNED43_G8 the corresponding component has28 polar vertices,22 true crossings, and U8’s incident facets split3/3 across it. A finite operation confined to the junior triangle can therefore encounter the unstable carrier through the rest of the component even though neither stable facet contains U.

Two different resources remain available:

- PIVOT58 has the stronger reported fixed-surface buffer and the detached ten-gon. It permits27 unrestricted added material points. The allowance of29 is conditional on retaining the genuine ten-gon and all ten corners.
- PRUNED43 has42 unrestricted added material-point slots. Its separate82-support parameterization permits only three additional arbitrary halfspaces under the sufficient F<=85 bound; releasing all82 normals does not retain E123.

Neither source’s positive Q is a negligible residual. The previous subsidiary deaths and seven-edge fusion are completed work, not experiments to repeat in this continuation.

## 2. Attempted numerical directions and their evidence boundary

The unfinished workflow requested two direct one-root point deformations using the parent’s complete `consolidate47b.py`, with one permitted stable root rather than two:

```
BUFFER_G4:    allow1, sm=1e-5, um=1e-5, coordinate bound1,   maxiter400
PRUNED43_G8:  allow1, sm=1e-5, um=1e-5, coordinate bound1.5, maxiter400
```

These are actual-mass point nominations, not fixed-reference-center tests. Their possible `S1_DIRECT58.json` and `S1_DIRECT43.json` files are **not new evidence in this handoff**, because their final contents and statuses were not inspectable here.

The other requested direction used a finite polar route between the two current stable normals, followed by a one-root polar forest and a live homogeneous-mass objective. The proposed forest maps a child proposal z into the interior of the diameter ball of its parent p:

```
q = p/2 + min(1, (1/2-epsilon)*|p|/|z-p/2|)*(z-p/2).
```

At the nominated reference origin this supplies a positive outgoing polar chord. It does **not** establish ownS1 unless the actual mass is compatible with the resulting surface. The attempted physical objective therefore used the global filled-hull centroid, normalized by volume^(1/3), rather than treating a small raw displacement or a one-step moment sum as closure.

No claimed R18/R20 normal count, own census, converged mass residual, or forest endpoint is imported from the possible files of that calculation. Likewise, failure of one direct optimizer would not exclude the current principal-basin geometry.

## 3. Sharp finite centroid bounds for a specified geometric corridor

This is an analytical result, independent of an optimizer or an unobserved execution.

Let A and C be bounded measurable sets with positive volume, with A subset C. In the intended application they are exact convex polyhedra, and one studies homogeneous convex bodies B satisfying

```
A subset B subset C.
```

Fix a nonzero direction w. Write V_A for volume(A), M_A for its unnormalized first moment, and define

```
F_w(t) = w.M_A - t*V_A
       + integral_(C minus A) max(w.x-t,0) dx.
```

Then the greatest possible value of `w.centroid(B)` over **all measurable fillings** between A and C is the unique zero of F_w. The smallest value is the negative of the corresponding greatest value for direction -w. Since convex fillings are a subset of measurable fillings, these extrema are rigorous outer bounds for every homogeneous convex B in the corridor.

### Proof

For any permitted B,

```
volume(B)*(w.centroid(B)-t)
  = integral_A (w.x-t) dx + integral_(B minus A) (w.x-t) dx
 <= F_w(t).
```

For a fixed t, equality is attained among measurable fillings by taking

```
B_t = A union {x in C: w.x>t}.
```

The overlap with A is counted only once. Thus F_w(t)>0 exactly when some permitted measurable filling has centroid projection greater than t. The function is continuous and strictly decreasing: increasing t by h>0 decreases the mandatory A contribution by h*V_A, while the positive-part shell contribution cannot increase. It changes sign between the minimum and maximum projection of C, so it has one zero. At that zero the indicated filling attains the extremal centroid projection.

The maximizing filling need not be convex. Accordingly, a bound excluding a desired centroid is a valid convex-body obstruction, but a bound permitting it is **not** a convex realizability certificate.

### Why this is useful here

The earlier six-U corridor theorem bounded an integral and then divided by an upper volume. F_w instead couples the **actual variable volume and moment in the extremization itself**. It gives the sharp measurable-filling bound in each direction, without a controller count, a chosen witness tree, a small-centroid assumption, or a local Jacobian.

For rational polyhedra and rational t, F_w(t) is exactly computable by clipping complete hulls:

```
F_w(t) = w.M_A - t*V_A
       + [w.M(C intersect {w.x>=t}) - t*V(C intersect {w.x>=t})]
       - [w.M(A intersect {w.x>=t}) - t*V(A intersect {w.x>=t})].
```

Exact rational bisection therefore gives certified intervals for the extremal projection. The computation uses full global hull integrals, not a sum of potentially overlapping caps.

For a physical polar-relay cut, a natural corridor is

```
A = the fully cut relay body,
C = the original current clean body.
```

A separator showing that zero is outside the centroid range would exclude every attempt to restore the old center by adding back material while staying inside C and retaining A. A separator failing to exclude zero would merely leave that family unresolved. Neither conclusion may be assumed before the exact calculation.

### Conversion to retained equilibrium guards

The same bounds apply directly to affine functions of the actual centroid.

For a common vertex u and an upper-hull incident ray d, its radial guard is

```
(u-c).d = u.d - c.d.
```

A strictly negative upper bound on this guard for every extreme ray certifies that u remains strict U throughout the corridor, provided u is retained and is an extreme vertex of the upper hull.

For an oriented mandatory facet polygon with outward n and directed boundary edge a--b, the stable-foot guard is

```
f_ab(c) = n.((a-c) cross (b-c))
        = n.(a cross b) + ((a-b) cross n).c.
```

If the polygon is retained in the lower hull and its plane supports the upper hull, strictly positive lower bounds on every such guard put the actual foot inside that mandatory polygon. The same supporting facet is then strict stable for every intermediate body, even when its surrounding polygon grows and the centroid moves substantially.

These are sharply specified retained-carrier tests. They do not exclude arbitrary carrier retirement, extension beyond the chosen upper hull, or deletion of material required by the lower hull. They also do not supply a full S/U/H census by themselves.

## 4. Complete prospective exact relay and centroid-range driver

The following is a new **unexecuted diagnostic source unit**, not a claim that any of its terminal markers was observed. It replaces dependence on the uninspectable numerical prototype files with an exact, source-complete finite test.

It uses only these already supplied dependencies:

1. `exact47.py` from the complete Fxvz parent;
2. `corridor47.py` from that parent, for exact clipping and the independent divergence-form first-moment identity;
3. `NOMINATION_MIN47B.json`, recovered by the complete VC47B parent capsule.

The VC47B capsule authenticates its complete107,749-byte dictionary with SHA-256 `3c7c015455f163d4a99d08201a5f1ead98ba77df1d0451983af9b835b480608d`. No earlier C622 workspace or on-demand source is needed. The current unit does not rerun the29-death proof or the detached fusion proof.

### What it does

It reconstructs PIVOT_G4_STAGE7 and PRUNED43_G8 from the exact parent freezing conventions, rebuilds their maximal hulls and actual mass, and creates a finite polar route from the current junior to either the current elder or a new root at101/100 of the elder vector. The route uses the supplied rational spherical-bisection generator,60-decimal rational square-root midpoints, and a new-point grid10^-10. All source normals are retained exactly. Exact positive chord checks establish referenceS1 only; the full actual homogeneous census is computed separately.

The physical halfspace body is reconstructed by exact polarity. Its true facets and edges are not inferred from the number of submitted normals. Every own and reference positive P/Q bar is retained. E<=249 is checked on the actual body; no facet-budget guarantee is assumed for these relay proposals.

With `--bounds`, the driver computes certified directional centroid intervals for every measurable filling between the relay body and the original body. These are necessary physical mass bounds, not certificates that a convex correction exists.

Save as `VC47C_RELAY_DIAGNOSTICS.py` alongside the dependencies. Prospective commands are:

```sh
python -B -S VC47C_RELAY_DIAGNOSTICS.py --out VC47C_OUT
python -B -S VC47C_RELAY_DIAGNOSTICS.py --out VC47C_BOUNDS --bounds --bisections 48
```

The default is a32-link route on each of the two clean seeds, with root factors1 and101/100. To nominate other finite lengths, use `--depths 3 4 5 6`, corresponding to8,16,32,64 links. A failed exact positive-chain test is recorded as a rejected route, not as a family exclusion. Any hull, topology, mass or census assertion failure stops the calculation rather than reporting a zero-root body.

No byte count or SHA-256 for this newly written source was measured in an inspectable execution. The complete literal source below is its recovery authority; it records its own bytes and hashes when run. There is no claimed new computed exact object whose identity is being replaced by an unmeasured hash.

```python
'''Prospective VC47C finite principal-relay diagnostics.
Standard-library exact arithmetic. No claimed execution receipt accompanies it.
Required supplied files: exact47.py, corridor47.py, NOMINATION_MIN47B.json.
'''
import argparse
import hashlib
import json
from pathlib import Path

import exact47 as E
import corridor47 as C

Q = E.Q
ZERO = E.ZERO
PARENT_ID = 'figure-0619'
PARENT_SHA = '28bc5fc5fc7ed10735aab14c4012dcdc4ca73119c5030b73b267e19a8b3d1ba0'
AUTH = {
    'exact47.py': {
        '14431f428ffce4d3c19bfae1671529790bd41a4d4bf06cdb2117a2e4edffa473'
    },
    'corridor47.py': {
        '5d5187a462c9b8bab978772b284ba6180ea4a187d619c7b6db4e288071e2130e',
        '3cadf6a06219fb30f53cf08fad459b4ef57b9bfb289d61347e99f7c1d9b7c3a7'
    }
}


def authenticate():
    for name, module in [('exact47.py', E), ('corridor47.py', C)]:
        raw = Path(module.__file__).read_bytes()
        digest = hashlib.sha256(raw).hexdigest()
        assert digest in AUTH[name], (name, digest)


def checked(points, faces=None):
    if faces is None:
        faces = E.hull(points)
    volume, moment = C.check_surface(points, faces)
    report = E.audit(points, faces)
    assert report['volume'] == volume
    assert report['first_moment'] == moment
    assert C.flux_moment(points, faces) == moment
    centered = [E.sub(p, report['centroid']) for p in points]
    assert E.mass(centered, faces) == (volume, ZERO)
    return report


def grid_points(rows, denominator):
    # JSON numbers are converted to their exact Python binary64 values before
    # the same rational nearest-ties-to-even freeze used by the parent.
    return [tuple(Q(round(Q(v) * denominator), denominator) for v in row)
            for row in rows]


def seed_points(name, nominations):
    if name == 'PIVOT_G4_STAGE7':
        points = grid_points(nominations['BUFFER_C.json']['x'], 10**4)
        base = checked(points)
        assert [base[k] for k in ('V', 'E', 'F')] == [58, 168, 112]
        assert base['strict'] == [2, 1, 1] and base['weak'] == [0, 0, 0]
        assert base['volume'] == Q(2775843712561, 300000000000)
        assert base['centroid'] == tuple(Q(v, 2220674970048800000) for v in (
            173348991486622797, -138652517065707771, -806066199977119242))
        for i in [0, 1, 2, 3, 4, 9, 32, 37, 56, 57]:
            x, y, z = points[i]
            y = (Q(895914) + 523027*x + 412587*z) / Q(-745798)
            points[i] = (x, y, z)
        expected = [58, 161, 105]
        qlo, qhi = Q('0.288594132748664'), Q('0.288594132748667')
    elif name == 'PRUNED43_G8':
        points = grid_points(nominations['PRUNEREPAIR/CURRENT.json']['x'], 10**8)
        expected = [43, 123, 82]
        qlo, qhi = Q('0.571818845634936'), Q('0.571818845634939')
    else:
        raise ValueError(name)
    report = checked(points)
    assert [report[k] for k in ('V', 'E', 'F')] == expected
    assert len(points) == report['V']
    assert report['strict'] == [2, 1, 1] and report['weak'] == [0, 0, 0]
    assert not report['P'] and len(report['Q']) == 1
    assert qlo < report['Q'][0]['depth'] < qhi
    return points, report


def physical_from_normals(normals):
    '''Exact body {x: y.x <= 1 for every supplied normal y}.'''
    dual_faces = E.hull(normals)
    points = []
    for face in dual_faces:
        n = E.normal(normals, face)
        h = E.dot(n, normals[face[0]])
        # A closed full-dimensional dual hull with strictly positive support
        # in every outward facet contains zero in its strict interior.
        assert h > 0
        points.append(E.mul(1/h, n))
    assert len(set(points)) == len(points)
    active = sorted({i for face in dual_faces for i in face})
    paired_faces = []
    for i in active:
        incident = [j for j, face in enumerate(dual_faces) if i in face]
        assert len(incident) >= 3
        cycle = E.cycle(incident, points, normals[i])
        paired_faces.append((cycle, i))
    paired_faces.sort(key=lambda pair: tuple(sorted(pair[0])))
    faces = [pair[0] for pair in paired_faces]
    face_to_normal = [pair[1] for pair in paired_faces]
    assert all(E.dot(y, p) <= 1 for y in normals for p in points)
    for face, i in paired_faces:
        assert all(E.dot(normals[i], points[j]) == 1 for j in face)
    report = checked(points, faces)
    report['active_submitted_normals'] = active
    report['face_to_submitted_normal'] = face_to_normal
    report['polar_maximal_faces'] = dual_faces
    return points, faces, report


def positive_reference_forest(normals, root):
    for i, a in enumerate(normals):
        scores = [E.dot(a, E.sub(b, a))
                  for j, b in enumerate(normals) if i != j]
        if i == root:
            assert max(scores) < 0
        else:
            assert max(scores) > 0


def make_relay(parent_report, depth, root_factor):
    normals = list(parent_report['poles'])
    stable = parent_report['S']
    assert len(stable) == 2
    elder = max(stable, key=lambda i: (E.dot(normals[i], normals[i]), -i))
    junior = next(i for i in stable if i != elder)
    root = elder
    target = E.mul(root_factor, normals[elder])
    if root_factor != 1:
        assert root_factor > 1
        root = len(normals)
        normals.append(target)
        assert E.dot(normals[elder], E.sub(target, normals[elder])) > 0
    old_grid, old_digits = E.GRID, E.SQRT_DIGITS
    try:
        E.GRID, E.SQRT_DIGITS = 10**10, 60
        chain = E.route(normals[junior], target, depth)
    finally:
        E.GRID, E.SQRT_DIGITS = old_grid, old_digits
    # route() contains its start but excludes its terminal point.
    assert chain[0] == normals[junior]
    first = len(normals)
    normals.extend(chain[1:])
    path = [junior] + list(range(first, len(normals))) + [root]
    scores = [E.dot(normals[a], E.sub(normals[b], normals[a]))
              for a, b in zip(path, path[1:])]
    assert len(scores) == 2**depth and min(scores) > 0
    positive_reference_forest(normals, root)
    return normals, dict(junior=junior, elder=elder, root=root,
                         root_factor=root_factor, path=path, scores=scores,
                         links=2**depth, grid=10**10, sqrt_digits=60)


def assert_nested(lower_points, upper_points, upper_faces):
    for face in upper_faces:
        n = E.normal(upper_points, face)
        a = upper_points[face[0]]
        assert all(E.dot(n, E.sub(p, a)) <= 0 for p in lower_points)


def affine_cap_integral(points, faces, w, t):
    '''Integral of max(w.x-t,0) over a complete convex hull.'''
    p, f, volume, moment = C.clip(points, faces, E.mul(-1, w), -t)
    value = E.dot(w, moment) - t*volume
    assert value >= 0
    return value


def maximum_centroid_interval(lower_points, lower_faces,
                              upper_points, upper_faces, w, iterations):
    '''Sharp measurable-filling maximum; convex fillings obey the same bound.'''
    assert E.dot(w, w) > 0 and iterations >= 1
    assert_nested(lower_points, upper_points, upper_faces)
    vl, ml = E.mass(lower_points, lower_faces)
    vu, mu = E.mass(upper_points, upper_faces)
    assert 0 < vl <= vu
    def function(t):
        low_positive = affine_cap_integral(lower_points, lower_faces, w, t)
        high_positive = affine_cap_integral(upper_points, upper_faces, w, t)
        assert high_positive >= low_positive
        return E.dot(w, ml) - t*vl + high_positive - low_positive
    used = sorted({i for f in upper_faces for i in f})
    lo = min(E.dot(w, upper_points[i]) for i in used)
    hi = max(E.dot(w, upper_points[i]) for i in used)
    assert lo < hi and function(lo) > 0 and function(hi) < 0
    for _ in range(iterations):
        mid = (lo + hi)/2
        value = function(mid)
        if value == 0:
            lo = hi = mid
            break
        if value > 0:
            lo = mid
        else:
            hi = mid
    return dict(lower=lo, upper=hi, lower_value=function(lo),
                upper_value=function(hi), direction=w,
                scope='Sharp over measurable fillings; outer bound for convex bodies')


def centroid_range(lower_points, lower_faces, upper_points, upper_faces,
                   w, iterations):
    maximum = maximum_centroid_interval(lower_points, lower_faces,
        upper_points, upper_faces, w, iterations)
    opposite = maximum_centroid_interval(lower_points, lower_faces,
        upper_points, upper_faces, E.mul(-1, w), iterations)
    minimum = dict(lower=-opposite['upper'], upper=-opposite['lower'])
    return dict(minimum=minimum, maximum=maximum,
                zero_excluded=(minimum['lower'] > 0 or maximum['upper'] < 0))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--out', default='VC47C_OUT')
    ap.add_argument('--data', default='NOMINATION_MIN47B.json')
    ap.add_argument('--depths', type=int, nargs='+', default=[5])
    ap.add_argument('--bounds', action='store_true')
    ap.add_argument('--bisections', type=int, default=48)
    args = ap.parse_args()
    assert all(1 <= d <= 6 for d in args.depths)
    authenticate()
    source_data = Path(args.data).read_bytes()
    nominations = json.loads(source_data)
    output = Path(args.out)
    output.mkdir(parents=True, exist_ok=True)
    manifest, run = {}, []
    def save(name, value):
        raw = (json.dumps(E.encode(value), sort_keys=True, indent=2) + '\n').encode()
        (output/name).write_bytes(raw)
        manifest[name] = dict(bytes=len(raw), sha256=hashlib.sha256(raw).hexdigest())
    for seed in ['PIVOT_G4_STAGE7', 'PRUNED43_G8']:
        raw_parent, parent = seed_points(seed, nominations)
        center = parent['centroid']
        parent_points = [E.sub(p, center) for p in raw_parent]
        parent_faces = parent['facets']
        assert E.mass(parent_points, parent_faces) == (parent['volume'], ZERO)
        save(seed + '_PARENT_EXACT.json', parent)
        for depth in args.depths:
            for factor in [Q(1), Q(101,100)]:
                name = seed + '_L' + str(2**depth) + '_R' + str(factor).replace('/','d')
                try:
                    normals, construction = make_relay(parent, depth, factor)
                except (AssertionError, ArithmeticError) as exc:
                    run.append(dict(name=name, route_rejected=True,
                        reason=type(exc).__name__, scope='This route only; no family exclusion'))
                    continue
                save(name + '_NORMALS.json', dict(normals=normals,
                    construction=construction, raw_frame_center=center,
                    source_parent=PARENT_ID, source_parent_sha256=PARENT_SHA))
                points, faces, report = physical_from_normals(normals)
                assert_nested(points, parent_points, parent_faces)
                reference = E.census(points, faces, ZERO)
                assert len(reference['S']) == 1 and not reference['weakS']
                assert report['face_to_submitted_normal'][reference['S'][0]] == construction['root']
                raw_points = [E.add(p, center) for p in points]
                expected_raw_moment = E.add(report['first_moment'], E.mul(report['volume'], center))
                assert E.mass(raw_points, faces) == (report['volume'], expected_raw_moment)
                report.update(reference_census=reference,
                    raw_frame_center=center,
                    raw_centroid=E.add(center, report['centroid']),
                    removed_volume=parent['volume']-report['volume'],
                    true_edge_budget_met=(report['E'] <= 249),
                    target=(report['E'] <= 249 and report['strict'] == [1,1,0]
                            and report['weak'] == [0,0,0]
                            and not report['P'] and not report['Q']))
                assert report['removed_volume'] >= 0
                if args.bounds:
                    directions = [(Q(1),Q(0),Q(0)), (Q(0),Q(1),Q(0)),
                                  (Q(0),Q(0),Q(1)), parent['poles'][construction['junior']]]
                    report['corridor_centroid_ranges'] = [
                        centroid_range(points, faces, parent_points, parent_faces,
                                       w, args.bisections) for w in directions]
                save(name + '_EXACT.json', report)
                run.append(dict(name=name, V=report['V'], E=report['E'], F=report['F'],
                    strict=report['strict'], weak=report['weak'],
                    P_count=len(report['P']), Q_count=len(report['Q']), target=report['target']))
                print(name, report['V'], report['E'], report['F'],
                      report['strict'], report['weak'], flush=True)
    own_source = Path(__file__).read_bytes()
    save('RUN.json', dict(source_parent=PARENT_ID, source_parent_sha256=PARENT_SHA,
        source_bytes=len(own_source), source_sha256=hashlib.sha256(own_source).hexdigest(),
        nomination_data_bytes=len(source_data),
        nomination_data_sha256=hashlib.sha256(source_data).hexdigest(),
        settings=vars(args), outcomes=run))
    (output/'MANIFEST.json').write_text(json.dumps(manifest, sort_keys=True, indent=2)+'\n')
    print('VC47C_RELAY_EXACT_DIAGNOSTICS_DONE', flush=True)
    if any(r.get('target', False) for r in run):
        print('VC47C_EXACT_OWN110_ENDPOINT_FOUND', flush=True)
    else:
        print('VC47C_NO_OWN110_IN_THE_COMPLETED_RELAY_TESTS', flush=True)


if __name__ == '__main__':
    main()
```

## 5. Continuation-critical interpretation

A positive polar route provides only the reference one-stable-root side of the construction. The acceptance endpoint still requires the actual homogeneous centroid, actual U count, additional weak census, and true E. The driver deliberately preserves those distinctions rather than assigning a successful class from its route or mass objective.

The sharp centroid-range test is useful only for its stated corridor. For a relay body A inside the original body C, a proved exclusion of zero would rule out restoring the old center by intermediate filling. It would not exclude a different actual center, changing the relay geometry, moving the original supports, or leaving C. Conversely, a centroid interval containing zero would not prove that a convex filling with that centroid exists, nor that it has own110.

No proposed source marker, possible optimizer checkpoint, or unread log is an execution receipt. The present handoff therefore does **not** supersede the exact VC47B parent with a new body. It preserves the unfinished principal-basin attempts, an exact finite mass-range method, and a complete next computation without relying on inaccessible prototype files or inventing a successful result.
