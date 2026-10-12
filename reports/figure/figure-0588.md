# figure-0588

AI research report · 2026-09-28 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# Steady Quartz 74 — execution boundary and a coupled finite-capacity experiment

## Result status

**No newly audited body or parent-specific capacity certificate is accepted in this continuation.** The execution calls returned skipped responses rather than inspectable output or exit status. I cannot establish whether the attempted commands ran. In particular, I have not established the contents of `/mnt/data/sq74f/PROBE_BEST_NUM.json`, and I do not promote that possible checkpoint into a construction result.

The last accepted computational input for this branch remains the author's **SQ74D_PRUNE_BEST_G6**, **V53/E153/F102, own strict211/additionalweak000, P=[], Q=[0.7964296564575203]**. Its current stable triangles are **[7,31,18]** and **[7,20,38]**, both avoiding U12; the current saddle is **[50,52]**. These are source-parent indices, not assumptions about the ordering produced by a new auditor.

The mathematical work below makes the proposed capacity experiment more specific than the previous unexecuted three-controller correction. It combines **two primary motions affecting a current stable carrier and the current saddle**, with three compensating scalar star motions, into an **exactly volume- and centroid-preserving two-parameter family**. It gives a rational, explicitly computable inner domain on which the moving bodies—not merely the unchanged parent's reference-center cube—retain U1. It also computes a separate domain where both old stable facets necessarily persist, so a small certified compensation domain is not mistaken for a domain capable of cancelling Q.

**That domain has not been numerically or rationally instantiated on the 53 points here.** The complete continuation unit is preserved below as unexecuted source, not as evidence of successful compensation or cancellation.

## Read scope and exact dependencies

The completed reading from the preceding unfinished attempt was retained: the current notebook through **EOF1588**, including its complete new literal parent, and the earlier unchanged literal Qc parent. The current notebook's supplied manifest is **320688 bytes**, SHA-256 **63097f13da3d54425990c3e4d58cc2ad96f8e0bcfe3795c7dda5b873d03e2339**. This is the supplied identity; a new runtime hash computation did not return an inspectable result.

The two computational source authorities are:

**figure-0580**, SHA-256 **7dcb3587aaadc980bc65e9fa8781da3fc19025737460b62ea13962e379611019**. Its SQ74D dictionary contains the complete PRUNE_BEST53 integer point literal.

**figure-0584**, SHA-256 **6797de00f6052b8cddaed1b1e675597d2d283d7a3bbb58bc6c730f8b927b7a48**. Its complete `SQ74E_STAR_CHART.py` supplies the standard-library input decoder, exact hull, homogeneous mass, strict/additionalweak census, and no-floor primal/polar filtrations used by the new unit below.

The SQ74D uncompressed dictionary identity is **67267 bytes**, SHA-256 **3c53f52e161499be2c96ba442a65bb9b7b5085e5bb88d894bc2c2f66abe18fb3**. The decoder checks this before accepting `SQ74D_PRUNE_BEST_G6_LITERAL.json`.

No new source gap is asserted. The missing evidence is execution and inspection of the parent-specific calculation. The older SQ74C package is not needed by this input-only decoder and the complete tRR auditor; it remains necessary for the old aggregate SQ74D replay and historical modules that import it.

## 1. A finite family that includes compensation from the start

For an outward triangular star at vertex p, cyclically write its incident faces as (p,a,b), and define

A = sum(a cross b),

J = [(p dot A)I + sum((a+b)(a cross b)^T)]/24.

For any finite displacement d satisfying A dot d=0, the exact changes are

**Delta V=0, Delta M=Jd**,

where M is the unnormalized homogeneous first moment. This is the previously supplied finite-star identity, not a new claim of novelty.

Choose two primary scalar directions at vertices touching the current stable and saddle geometry. Choose three compensating scalar directions. Require that **distinct moving vertices are pairwise nonadjacent**; multiple directions at one controller vertex are permitted. Each direction is tangent to its own A-plane. Because no triangle contains two distinct moving vertices, the entire simultaneous five-scalar family has

V(lambda)=V0,

M(lambda)=M0+C lambda,

exactly, not merely to first order. The columns of C are the five Jt vectors computed at the parent. They stay valid throughout this fixed-star family because no moving vertex is a neighbor of another distinct moving vertex.

Partition C into two primary columns C_P and the three-controller matrix T. When det(T) is nonzero, define

**K = -T^{-1} C_P.**

For primary parameters z=(a,b), use controller parameters s=Kz. Every resulting member then has

**V=V0, M=M0, and actual homogeneous centroid g=g0**, exactly.

This differs from evaluating a bridge at g0 and hoping that post-hoc mass repair preserves it. The mass-corrected geometry is the family being searched. It also differs from applying a common translation after a deformation: only the selected existing stars move, and their finite first moments cancel.

There is no assertion that a suitable, well-conditioned T has been found on PRUNE_BEST. The implementation searches a bounded collection of compatible frames and records the actual selected directions and matrix if execution succeeds.

## 2. An explicit rational capacity bound

For this independent-star family, every face-versus-nonincident-vertex supporting determinant is a polynomial of total degree at most two in the five scalar parameters. A face contains at most one moving vertex; its probe contains at most one further moving vertex. The fixed-target interiority tests have degree at most one. Every fixed-target outgoing chord score has degree at most two.

Write any one required positive inequality as

f(lambda)=c0+sum(l_i lambda_i)+sum(d_i lambda_i^2)+sum(c_ij lambda_i lambda_j),

with c0>0 at the parent. Let

L=sum|l_i|+sum|d_i|+sum|c_ij|.

Then, for |lambda_i|<=h<=1,

|f(lambda)-c0|<=hL.

Therefore the rational choice

**h=min(1, min over L>0 of c0/(2L))**

certifies every selected inequality with margin at least c0/2 throughout the closed five-dimensional box. The coefficients are recovered exactly from evaluations at 0, plus/minus each coordinate vector, and each pairwise sum; no finite differences or floating tolerances are used.

The inequalities included are all strict nonincident supporting determinants, all fixed-target interiority tests, one selected positive outgoing chord for every nonroot, and all strict negative outgoing chords of the retained root. This gives a fixed-target U1 certificate for the whole box. Restricting to the exact closure plane s=Kz makes it an **own-centroid U1 certificate throughout a moving physical family**.

A guaranteed primary square is

**|a|,|b|<=alpha**, where

**alpha=h/max(1, max_i(|K_i0|+|K_i1|)).**

The three-controller moment image at zero primary parameters is exactly the parallelepiped T[-h,h]^3. It contains a closed coordinate cube of first-moment residuals with radius

**rho=min_i h/||row_i(T^{-1})||_1.**

Thus the requested output is not merely det(T) or a Jacobian rank: it is the exact T, h, rho, alpha, the limiting positive polynomial, and the corrected finite bodies.

These are **sufficient inner capacities**, not maximal feasible capacities. A small h does not prove that a larger nonlinear domain, another controller frame, or a changed fan is impossible.

## 3. Explicitly test whether the certified domain still traps both stable carriers

For each of the two current stable facets, its three oriented foot guards are positive at the parent. After substituting the exact closure s=Kz, those guards are quadratic polynomials in the two primary parameters. Applying the same coefficient bound gives a rational radius beta on which **both original stable facets remain strictly stable**.

If alpha<=beta, the entire certified primary square retains at least two stable equilibria. In that case the result would be:

**A genuine finite physical compensation domain has been proved, but that particular certified domain cannot contain own110.**

This is a useful, precisely scoped distinction. It is not an exclusion of the whole star chart, the full 53-point family, a larger feasible region, a different witness policy, or an incidence-changing deformation. It also prevents a successful moment solve and a positive U forest from being presented as progress on S1 without examining the current stable geometry.

The code evaluates eight nonzero rational members of the primary square and recomputes their complete exact census and all P/Q bars. It does not assume that Q decreases, that weak S/H are absent, or that the largest Q alone determines acceptance.

## 4. Complete unexecuted continuation source

Save the full tRR source already supplied in this chat as `SQ74E_STAR_CHART.py`, the Qc capsule as `SQ74D_RECOVER.py`, and the following new unit as **SQ74F_CAPACITY.py**. These are its complete transitive source dependencies; no historical numerical workspace is imported.

Run:

```text
python SQ74F_CAPACITY.py SQ74D_RECOVER.py --engine SQ74E_STAR_CHART.py --out SQ74F_CAPACITY_RUN --max-frame-tests 20000
```

The implementation uses the Python standard library. It preserves the exact input's original coordinates, recomputes its actual current facets and equilibrium identities, and does not assume simple vertices. It uses the supplied auditor's explicit rejection of unhandled nonsimplicial maximal facets rather than treating their triangulation as a new facet count.

The prospective terminal marker is **SQ74F_CAPACITY_AND_EIGHT_ENDPOINTS_AUDITED**, or **SQ74F_EXACT_OWN110_FOUND** if a complete target is actually obtained. Neither marker was observed in this continuation. Output byte counts and hashes are computed by the program when run; none is invented here.

```python
import argparse
import hashlib
import importlib.util
import itertools
import json
from fractions import Fraction as R
from pathlib import Path

E = None


def load_engine(path):
    spec = importlib.util.spec_from_file_location('sq74e_exact_parent', path)
    if spec is None or spec.loader is None:
        raise ValueError('Cannot load the complete supplied tRR source')
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def moved(points, description, directions, parameters):
    return E.apply_controls(points, description, directions, parameters)


def select_frame(points, faces, report, limit):
    edges = E.edges_of(faces)
    stable_vertices = sorted(set(v for f in report['S'] for v in faces[f]))
    saddle_vertices = sorted(set(v for edge in report['H'] for v in edge))
    root = report['U'][0]
    tested = 0
    for first, second in itertools.product(stable_vertices, saddle_vertices):
        if first == second or tuple(sorted((first, second))) in edges:
            continue
        for axis_a, axis_b in itertools.product(range(3), repeat=2):
            primary = ((first, axis_a), (second, axis_b))
            primary_items = [E.star_direction(points, faces, i, a) for i, a in primary]
            if any(item is None for item in primary_items):
                continue
            pool = []
            for vertex in range(len(points)):
                if vertex in (first, second, root):
                    continue
                if any(tuple(sorted((vertex, v))) in edges for v in (first, second)):
                    continue
                for axis in range(3):
                    item = E.star_direction(points, faces, vertex, axis)
                    if item is not None:
                        pool.append(((vertex, axis), item))
            for triple in itertools.combinations(pool, 3):
                description = primary + tuple(item[0] for item in triple)
                if not E.compatible(description, edges):
                    continue
                tested += 1
                if tested > limit:
                    raise ValueError('Bounded controller-frame search exhausted; no family exclusion')
                items = primary_items + [item[1] for item in triple]
                columns = [item[1] for item in items]
                if E.det(*columns[2:]) != 0:
                    return description, [item[0] for item in items], columns, tested
    raise ValueError('No frame found in the specified independent-star construction')


def parent_forest(points, target, root):
    forest = [-1] * len(points)
    for i, source in enumerate(points):
        if i == root:
            continue
        scored = [(E.dot(E.sub(source, target), E.sub(dest, source)), -j, j)
                  for j, dest in enumerate(points) if j != i]
        value, _, witness = max(scored)
        if value <= 0:
            raise ValueError('Parent does not have the required strict outgoing witness')
        forest[i] = witness
    for start in range(len(points)):
        seen = set()
        i = start
        while i != root:
            if i in seen or i < 0:
                raise AssertionError('Parent witness graph is not rooted')
            seen.add(i)
            i = forest[i]
    return forest


def geometric_values(points, faces, target, forest, root):
    values = []
    labels = []
    for fno, face in enumerate(faces):
        a, b, c = [points[i] for i in face]
        normal = E.cross(E.sub(b, a), E.sub(c, a))
        for vertex, point in enumerate(points):
            if vertex in face:
                continue
            values.append(-E.dot(normal, E.sub(point, a)))
            labels.append(['support', fno, vertex])
        values.append(E.dot(normal, E.sub(a, target)))
        labels.append(['target_interior', fno])
    for i, j in enumerate(forest):
        if i == root:
            continue
        values.append(E.dot(E.sub(points[i], target), E.sub(points[j], points[i])))
        labels.append(['positive_U_witness', i, j])
    for j in range(len(points)):
        if j == root:
            continue
        values.append(-E.dot(E.sub(points[root], target), E.sub(points[j], points[root])))
        labels.append(['strict_root_support', root, j])
    return values, labels


def stable_values(points, faces, stable, target):
    values = []
    labels = []
    centered = [E.sub(p, target) for p in points]
    for fno in stable:
        face = faces[fno]
        a, b, c = [points[i] for i in face]
        normal = E.cross(E.sub(b, a), E.sub(c, a))
        for i, j in zip(face, face[1:] + face[:1]):
            values.append(E.dot(normal, E.cross(centered[i], centered[j])))
            labels.append(['retained_stable_foot', fno, i, j])
    return values, labels


def exact_quadratics(evaluator, dimension):
    zero = [R(0)] * dimension
    constant = evaluator(zero)
    linear = []
    square = []
    for i in range(dimension):
        plus = list(zero)
        minus = list(zero)
        plus[i], minus[i] = R(1), R(-1)
        fp, fm = evaluator(plus), evaluator(minus)
        if len(fp) != len(constant) or len(fm) != len(constant):
            raise AssertionError('Constraint indexing changed')
        linear.append([(a-b)/2 for a, b in zip(fp, fm)])
        square.append([(a+b)/2-c for a, b, c in zip(fp, fm, constant)])
    mixed = {}
    for i, j in itertools.combinations(range(dimension), 2):
        point = list(zero)
        point[i] = point[j] = R(1)
        value = evaluator(point)
        mixed[(i, j)] = [v-c-linear[i][k]-linear[j][k]-square[i][k]-square[j][k]
                         for k, (v, c) in enumerate(zip(value, constant))]
    polynomials = []
    for k, c in enumerate(constant):
        polynomials.append(dict(constant=c,
                                linear=[row[k] for row in linear],
                                square=[row[k] for row in square],
                                mixed=[[i, j, row[k]] for (i, j), row in mixed.items() if row[k]]))
    return polynomials


def safe_radius(polynomials):
    radius = R(1)
    limiting = None
    for i, polynomial in enumerate(polynomials):
        c = polynomial['constant']
        if c <= 0:
            raise ValueError('The base constraint is not strictly positive')
        total = (sum(map(abs, polynomial['linear']))
                 + sum(map(abs, polynomial['square']))
                 + sum(abs(row[2]) for row in polynomial['mixed']))
        if total:
            candidate = c/(2*total)
            if candidate < radius:
                radius, limiting = candidate, i
    return radius, limiting


def column_product(columns, parameters):
    return E.vsum(E.mul(s, column) for s, column in zip(parameters, columns))


def main():
    global E
    parser = argparse.ArgumentParser()
    parser.add_argument('parent_capsule', type=Path)
    parser.add_argument('--engine', type=Path, default=Path('SQ74E_STAR_CHART.py'))
    parser.add_argument('--out', type=Path, default=Path('SQ74F_CAPACITY_RUN'))
    parser.add_argument('--max-frame-tests', type=int, default=20000)
    args = parser.parse_args()
    if args.max_frame_tests < 1:
        raise ValueError('max-frame-tests must be positive')
    E = load_engine(args.engine)
    E.self_test()
    points, authority = E.parent_points(args.parent_capsule)
    faces = E.hull(points)
    parent = E.audit(points, faces)
    if [parent[k] for k in ('V', 'E', 'F')] != [53, 153, 102]:
        raise ValueError('Wrong exact parent geometry')
    if parent['strict'] != [2, 1, 1] or parent['weak'] != [0, 0, 0]:
        raise ValueError('Wrong exact parent equilibrium class')
    if parent['P'] or len(parent['Q']) != 1:
        raise ValueError('Wrong exact parent positive-bar census')
    target = parent['centroid']
    root = parent['U'][0]
    description, directions, columns, tested = select_frame(points, faces, parent, args.max_frame_tests)
    forest = parent_forest(points, target, root)
    _, labels = geometric_values(points, faces, target, forest, root)

    def five_values(parameters):
        current = moved(points, description, directions, parameters)
        return geometric_values(current, faces, target, forest, root)[0]

    polynomials = exact_quadratics(five_values, 5)
    halfwidth, limiting = safe_radius(polynomials)
    T = columns[2:]
    response_a = tuple(-x for x in E.solve_columns(T, columns[0]))
    response_b = tuple(-x for x in E.solve_columns(T, columns[1]))
    closure = [[response_a[i], response_b[i]] for i in range(3)]
    multiplier = max([R(1)] + [abs(a)+abs(b) for a, b in closure])
    amplitude = halfwidth/multiplier
    inverse_columns = [E.solve_columns(T, axis) for axis in E.AXES]
    inverse_row_norms = [sum(abs(column[i]) for column in inverse_columns) for i in range(3)]
    moment_cube = min(halfwidth/norm for norm in inverse_row_norms)

    def parameters_for(primary):
        a, b = primary
        return [a, b] + [row[0]*a+row[1]*b for row in closure]

    def closed_points(primary):
        return moved(points, description, directions, parameters_for(primary))

    def old_stable_values(primary):
        return stable_values(closed_points(primary), faces, parent['S'], target)[0]

    stable_polynomials = exact_quadratics(old_stable_values, 2)
    stable_radius, stable_limiter = safe_radius(stable_polynomials)
    _, stable_labels = stable_values(points, faces, parent['S'], target)

    # Direct corner checks supplement, rather than replace, the coefficient proof.
    minimum_corner_guard = None
    for signs in itertools.product((-1, 1), repeat=5):
        lam = [sign*halfwidth for sign in signs]
        current = moved(points, description, directions, lam)
        values, _ = geometric_values(current, faces, target, forest, root)
        guard = min(values)
        if guard <= 0:
            raise AssertionError('Certified five-dimensional box failed a corner check')
        minimum_corner_guard = guard if minimum_corner_guard is None else min(minimum_corner_guard, guard)
        volume, moment = E.mass(current, faces)
        expected = E.add(parent['first_moments'], column_product(columns, lam))
        if volume != parent['volume'] or moment != expected:
            raise AssertionError('Finite independent-star mass identity failed')

    args.out.mkdir(parents=True, exist_ok=True)
    manifest = {}
    certificate = dict(authority=authority,
                       parent_geometry=[53, 153, 102],
                       parent_S=parent['S'], parent_U=parent['U'], parent_H=parent['H'],
                       parent_stable_triangles=[faces[i] for i in parent['S']],
                       controller_frame_tests=tested,
                       max_frame_tests=args.max_frame_tests,
                       vertices_axes=description, directions=directions,
                       moment_columns=columns, controller_determinant=E.det(*T),
                       five_scalar_box_halfwidth=halfwidth,
                       moment_cube_radius=moment_cube,
                       exact_closure_matrix=closure,
                       primary_square_halfwidth=amplitude,
                       target_centroid=target, fixed_volume=parent['volume'],
                       fixed_first_moments=parent['first_moments'],
                       U_forest=forest,
                       limiting_box_constraint=None if limiting is None else labels[limiting],
                       all_constraint_labels=labels,
                       all_constraint_polynomials=polynomials,
                       corner_minimum_guard=minimum_corner_guard,
                       retained_two_S_square_halfwidth=stable_radius,
                       retained_two_S_limiter=None if stable_limiter is None else stable_labels[stable_limiter],
                       retained_two_S_polynomials=stable_polynomials,
                       both_old_S_persist_on_entire_certified_primary_square=(amplitude <= stable_radius),
                       scope='Certified inner domain in one independent-star fixed-fan chart; not maximal capacity')
    manifest['CAPACITY_CERTIFICATE.json'] = E.write_json(args.out/'CAPACITY_CERTIFICATE.json', certificate)
    manifest['PARENT_AUDIT.json'] = E.write_json(args.out/'PARENT_AUDIT.json', parent)
    endpoints = []
    winner = None
    for serial, pair in enumerate(pair for pair in itertools.product((-1, 0, 1), repeat=2) if pair != (0, 0)):
        primary = [R(v)*amplitude for v in pair]
        parameters = parameters_for(primary)
        if max(map(abs, parameters)) > halfwidth:
            raise AssertionError('Closure left the certified scalar box')
        current = closed_points(primary)
        if current == points:
            raise AssertionError('The nominated finite deformation is unchanged')
        report = E.audit(current, faces)
        if report['volume'] != parent['volume'] or report['first_moments'] != parent['first_moments']:
            raise AssertionError('Endpoint is not exactly mass-preserving')
        if report['centroid'] != target or report['U'] != [root] or report['weak_U'] or report['P']:
            raise AssertionError('Endpoint violates the own-U1 certificate')
        if [report[k] for k in ('V', 'E', 'F')] != [53, 153, 102]:
            raise AssertionError('Inherited maximal-facet counts changed inside the strict box')
        name = 'SQ74F_CLOSED_STAR_%02d' % serial
        report['primary_parameters'] = primary
        report['all_scalar_parameters'] = parameters
        report['name'] = name
        for suffix, value in (('_INPUT.json', E.literal_points(name, current)), ('_AUDIT.json', report)):
            filename = name+suffix
            manifest[filename] = E.write_json(args.out/filename, value)
        is_winner = (report['strict'] == [1, 1, 0] and report['weak'] == [0, 0, 0]
                     and not report['P'] and not report['Q'] and report['E'] <= 249)
        endpoints.append(dict(name=name, strict=report['strict'], weak=report['weak'],
                              P=[bar['depth'] for bar in report['P']],
                              Q=[bar['depth'] for bar in report['Q']], winner=is_winner))
        if is_winner:
            winner = name
    summary = dict(authority=authority,
                   engine_source_sha256=hashlib.sha256(args.engine.read_bytes()).hexdigest(),
                   new_source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                   halfwidth=halfwidth, primary_amplitude=amplitude, moment_cube_radius=moment_cube,
                   retained_two_S_radius=stable_radius,
                   both_old_S_persist_on_certified_square=(amplitude <= stable_radius),
                   endpoints=endpoints, winner=winner)
    manifest['SUMMARY.json'] = E.write_json(args.out/'SUMMARY.json', summary)
    E.write_json(args.out/'MANIFEST.json', manifest)
    print('SQ74F_EXACT_OWN110_FOUND' if winner else 'SQ74F_CAPACITY_AND_EIGHT_ENDPOINTS_AUDITED')
    print(json.dumps(E.encoded(summary), sort_keys=True))


if __name__ == '__main__':
    main()
```

## Continuation boundary

The new source changes the experiment in three concrete ways: it includes current stable and saddle motion in the same exact mass-preserving family; it computes a rational finite moment image rather than stopping at matrix rank; and it distinguishes a certified U1-safe compensation domain from a domain in which both stable carriers are still provably trapped.

**None of the parent-specific numerical quantities in that proposed certificate has been observed.** There is no new accepted input, no new census, and no claimed reduction of Q. The retained PRUNE_BEST53 body and the supplied exact source parents remain the continuation authority. Any local SQ74F checkpoint from a skipped call must be read and audited before it is used as evidence.
