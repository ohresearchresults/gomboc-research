# figure-0316

AI research report · 2026-09-05 UTC · [Export notes](../../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI report.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../../C622/README.md) passes the supplied exact checks; the search for C<500 remains open. See [verification status and source gaps](../../catalog/coverage.md).
<!-- historical-status:end -->

---

# Vivid Lynx 76 — recovered vertex-loss checkpoint and exact cavity continuation

## 1. Determination and evidence boundary

**The fixed-4355-vertex restriction has been left, but C<1000 has not been reached.** The strongest fully reconstructible checkpoint recovered from the interrupted work is the rational subset body **FUS-SUB4001**:

| Quantity | Literal parent | Recovered checkpoint |
|---|---:|---:|
| Actual vertices V | 4355 | 4001 |
| Actual true edges E | 11634 | 11100 |
| Actual maximal faces F | 7281 | 7101 |
| C=2E | 23268 | 22200 |
| Own-centroid equilibrium class | (1,1,0) | (1,1,0) |

Thus the checkpoint removes **354 vertices and 534 true edges**, decreasing C by **1068**. This is an actual vertex-loss result, not another fixed-cardinality face-fusion result. It is nevertheless a modest intermediate reduction, not the substantially compressed final architecture sought by the assignment.

**Verification provenance must remain explicit.** The recovered work record contains a completed exact global-verifier pass for this 4001-vertex checkpoint: actual filled-volume centroid, global supports, maximal-face merging, vertex extremality, and complete face/vertex/four-component-edge mechanics were checked, with no degenerate equilibrium. In the resumed turn I did not obtain a usable fresh verification readback for the later experimental states. Consequently, I retain FUS-SUB4001 as a **recovered reported-pass checkpoint**, supply its complete modification recipe below, and do not promote any later numerical state or claim a fresh independently replayed final package.

The most useful additional mathematical result is an exact framework for **outward multi-face cavity replacement with genuine vertex disappearance**. It detects disappearance using the full old normal cone, computes rational support-event intervals, and reduces own-centroid mechanics on each resulting x-motion cell to polynomial sign tests of degree at most three. This explicitly distinguishes a geometric rank-loss event from an equilibrium degeneracy.

## 2. Literal parent and object identity

The sole geometric parent is

```text
assignment: figure-0313
immutable payload SHA-256:
7b683411b466e5db8315dd1503bc8e1cc6e3493cdef9241c84efb1ea0ca0d79d

object: P50_FUS4355_C23268_R
(V,E,F)=(4355,11634,7281)
C=23268
own-centroid class=(1,1,0)
```

The source is its **rational fusion table**, not the lattice P50L, affine P50A, or deletion P50D table. No mask, coordinate transform, or frozen-rank certificate from those different bodies is applied here.

The parent archive is identified by

```text
P50_NONSIMPLICIAL_FUSION_HANDOFF.zip
bytes: 1038550
SHA-256:
9297a5a62be6fc15cd8022a2e05c01fe28bd5fbaf0178604dc2c029e4d9c7c9d
```

The defining raw parent coordinates are the first three entries of each row of `body/vertices.csv.gz`, parsed as exact rational numbers. The fourth column is zero. The SHA-256 of that file after gzip decompression is

```text
443fe49ecafb543ea7ca4d66cdf2b958b19d211f9bcc9f7ee6b3c1e23ed7d369
```

The raw table is not assumed centred. Its actual ordinary-volume centroid must be recomputed after every modification. In particular, the very small parent raw centroid is **not** inherited as the centroid of FUS-SUB4001.

No substantive conflict was found between the literal parent definition and the journal's description of it. The parent has a separate stable hexagon and unstable apex; it does not impose one fixed homothetic polygonal section throughout the body. The previous fixed-polygon central-section obstruction therefore remains valid but does not prohibit the present modification.

## 3. Complete exact definition of FUS-SUB4001

Let the parent raw rational points, in their original order, be

\[
q_0,\ldots,q_{4354}.
\]

Define the half-turn mate by exact coordinate equality:

\[
\mu(i)=j\quad\Longleftrightarrow\quad
q_j=(q_{ix},-q_{iy},-q_{iz}).
\]

**Do not use parity or assume adjacent-index pairing.** Construct the mate map from the literal rational coordinates.

Remove each of the following 177 representatives and its mate. The list is complete and contains no abbreviation:

```python
REMOVED_REPRESENTATIVES = [
    16,42,276,312,588,1264,1356,1806,1856,1878,1922,1952,
    2294,2300,2360,2384,2478,2508,2570,2588,2622,2660,2704,
    2768,2842,2874,2906,2958,2998,3076,3086,3116,3212,3356,
    3450,3814,3932,3992,4044,18,22,82,150,226,254,370,422,
    464,472,548,670,710,726,932,962,964,1030,1156,1178,1200,
    1320,1326,1338,1354,1396,1460,1622,1688,1738,1946,2008,
    2052,2104,2246,2266,2346,2372,2434,2532,2542,2558,2566,
    2640,2658,2688,2760,2770,2778,2856,2956,2964,3042,3044,
    3080,3084,3200,3330,3376,3400,3408,3466,3490,3492,3512,
    3564,3570,3656,3674,3684,3708,3742,3764,3810,3836,3902,
    3946,4014,4076,116,264,618,676,770,846,910,966,972,1306,
    2362,2584,2690,2804,2912,2976,3008,3010,3114,3120,3138,
    3152,3176,3264,3286,3358,3368,3370,3394,3534,3554,3576,
    3700,3722,3744,4004,174,208,454,602,1060,3472,3544,3682,
    3788,3916,1750,3556,4196,322,876,1384,470,4226,3184,
    1170,832,1348,2152
]
```

Let I be the remaining original indices in ascending order. There are exactly 4001 of them. Set

\[
K_{\rm raw}=\operatorname{conv}\{q_i:i\in I\}.
\]

No retained coordinate is changed at this checkpoint. The change is a genuine collection of convex-hull cavity replacements after deletion, not a reclassification of old display diagonals.

Let T be a complete outward triangulation of the **new** hull. For its raw coordinates p_i in compact ascending-retention order, define

\[
W=\sum_{(i,j,k)\in T}\det(p_i,p_j,p_k),
\]

\[
M=\sum_{(i,j,k)\in T}
\det(p_i,p_j,p_k)(p_i+p_j+p_k).
\]

The exact body reported by this handoff is

\[
\boxed{K=K_{\rm raw}-g,\qquad
\operatorname{Vol}(K)=W/6,\qquad g=M/(4W).}
\]

The density is identically one throughout the filled convex hull. These finite rational sums, together with the literal parent and complete mask, are an exact definition of both the body and its ordinary-volume centre; no numerical centroid is a defining parameter.

The half-turn symmetry gives g_y=g_z=0 exactly. The recovered numerical diagnostic was

\[
g_x\approx-8.12935735\times10^{-6}.
\]

This approximate value must not be used instead of the exact rational integration.

### Critical features

The retained source indices 0 through 5 remain the compact indices 0 through 5. The stable maximal face has cycle

```text
[0,3,4,5,2,1].
```

Its centred plane is `x=-473/500-g_x`. Source apex 4354 becomes compact index **4000**, with centred coordinate

\[
(527/500-g_x,0,0).
\]

The recovered exact audit records that these are the unique stable face and unstable vertex. There are no saddle edges and no degenerate equilibria. Its centred inradius and maximum radius agree with

\[
r=473/500+g_x,\qquad R=527/500-g_x,
\]

approximately 0.9459918706426501 and 1.05400812935735 respectively. The recovered audit checked all other supporting-plane distances and all other vertex radii, rather than importing the smooth P50 radial bounds.

## 4. Reproduction from either the literal archive or the supplied journal

The following complete modification program accepts the literal parent archive or the journal containing the literal parent source capsule. It does not depend on a surviving worker scratch directory or an unprinted deletion mask.

The archive route checks its exact hash and uses its literal rational table. The journal route extracts and checks the **complete parent capsule**, reconstructs the parent, and then makes the same 354-point deletion. This route retains an explicit immutable-parent dependency: the named literal parent must accompany the handoff. No replacement object with the same display name is acceptable.

The numerical hull is only a proposed triangulation. The subsequent exact verifier must prove global support, completeness of the boundary, maximal-face merging, extremality, actual volume moments and all-feature mechanics. A failed numerical proposal or exact assertion is a failed replay, not permission to relax a tolerance.

Save this as `construct_FUS_SUB4001.py` and run, for example,

```sh
OPENBLAS_NUM_THREADS=1 python construct_FUS_SUB4001.py \
  P50_NONSIMPLICIAL_FUSION_HANDOFF.zip FUS_SUB4001
```

or pass the journal Markdown as the first argument. The inherited full-source regeneration environment was Python 3.13.5, NumPy 2.3.5 and SciPy 1.17.0. The exact checker itself uses only the standard library. Do not run assertion-based checks with `-O`.

```python
#!/usr/bin/env python3
from __future__ import annotations
import base64
import gzip
import hashlib
import json
import lzma
import os
from pathlib import Path
import re
import subprocess
import sys
import zipfile
from fractions import Fraction as Q

if hasattr(sys, 'set_int_max_str_digits'):
    sys.set_int_max_str_digits(0)

PARENT_ASSIGNMENT = 'figure-0313'
ARCHIVE_SHA = '9297a5a62be6fc15cd8022a2e05c01fe28bd5fbaf0178604dc2c029e4d9c7c9d'
RAW_TABLE_SHA = '443fe49ecafb543ea7ca4d66cdf2b958b19d211f9bcc9f7ee6b3c1e23ed7d369'
CAPSULE_SHA = '5d3c0b41f17ba4d9e18f3efb1432f2fff48aa37ac8f056a840ddde206406783e'

REPS = [
16,42,276,312,588,1264,1356,1806,1856,1878,1922,1952,
2294,2300,2360,2384,2478,2508,2570,2588,2622,2660,2704,
2768,2842,2874,2906,2958,2998,3076,3086,3116,3212,3356,
3450,3814,3932,3992,4044,18,22,82,150,226,254,370,422,
464,472,548,670,710,726,932,962,964,1030,1156,1178,1200,
1320,1326,1338,1354,1396,1460,1622,1688,1738,1946,2008,
2052,2104,2246,2266,2346,2372,2434,2532,2542,2558,2566,
2640,2658,2688,2760,2770,2778,2856,2956,2964,3042,3044,
3080,3084,3200,3330,3376,3400,3408,3466,3490,3492,3512,
3564,3570,3656,3674,3684,3708,3742,3764,3810,3836,3902,
3946,4014,4076,116,264,618,676,770,846,910,966,972,1306,
2362,2584,2690,2804,2912,2976,3008,3010,3114,3120,3138,
3152,3176,3264,3286,3358,3368,3370,3394,3534,3554,3576,
3700,3722,3744,4004,174,208,454,602,1060,3472,3544,3682,
3788,3916,1750,3556,4196,322,876,1384,470,4226,3184,
1170,832,1348,2152
]

def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()

def run_checked(args: list[str], cwd: Path) -> None:
    env = dict(os.environ, OPENBLAS_NUM_THREADS='1')
    subprocess.run(args, cwd=cwd, env=env, check=True)

def recover_parent(source: Path, work: Path) -> tuple[Path, Path]:
    work.mkdir(parents=True, exist_ok=True)
    if zipfile.is_zipfile(source):
        data = source.read_bytes()
        assert digest(data) == ARCHIVE_SHA, 'Wrong literal parent archive'
        with zipfile.ZipFile(source) as archive:
            for item in archive.infolist():
                dest = (work / item.filename).resolve()
                assert dest.is_relative_to(work.resolve()), 'Unsafe archive path'
            archive.extractall(work)
        return work / 'body', work / 'verify_rational.py'

    text = source.read_text(encoding='utf-8')
    heading = '## Parent ' + PARENT_ASSIGNMENT
    assert heading in text, 'Named immutable parent missing from journal'
    section = text.split(heading, 1)[1]
    match = re.search(r'CAPSULE\s*=\s*r"""(.*?)"""', section, re.S)
    assert match is not None, 'Complete parent capsule missing'
    packed = ''.join(match.group(1).split())
    assert len(packed) == 26285, 'Truncated parent capsule'
    raw = lzma.decompress(base64.b85decode(packed))
    assert len(raw) == 46122 and digest(raw) == CAPSULE_SHA
    sources = json.loads(raw)
    expected = {
        'rebuild_final.py', 'rebuild_peel.py', 'rebuild_successor.py',
        'reconstruct_parent.py', 'verify_rational.py'
    }
    assert set(sources) == expected
    for name, content in sources.items():
        assert Path(name).name == name
        (work / name).write_text(content, encoding='utf-8')
    run_checked([sys.executable, 'reconstruct_parent.py'], work)
    run_checked([
        sys.executable, 'rebuild_peel.py',
        'regenerated_exact_polyhedron.npz', 'body'
    ], work)
    return work / 'body', work / 'verify_rational.py'

def main(source: Path, output: Path) -> None:
    source = source.resolve()
    output = output.resolve()
    output.mkdir(parents=True, exist_ok=True)
    body, verifier = recover_parent(source, output / 'literal_parent')

    raw = gzip.decompress((body / 'vertices.csv.gz').read_bytes())
    assert digest(raw) == RAW_TABLE_SHA, 'Parent coordinate substitution'
    points = [
        tuple(Q(v) for v in line.split(',')[:3])
        for line in raw.decode('utf-8').splitlines() if line.strip()
    ]
    assert len(points) == len(set(points)) == 4355
    lookup = {p: i for i, p in enumerate(points)}
    mate = [lookup[(x, -y, -z)] for x, y, z in points]
    assert all(mate[mate[i]] == i for i in range(len(points)))
    assert len(REPS) == len(set(REPS)) == 177
    removed = set(REPS) | {mate[i] for i in REPS}
    assert len(removed) == 354
    assert not removed.intersection(set(range(6)) | {4354})
    indices = [i for i in range(4355) if i not in removed]
    retained = [points[i] for i in indices]
    assert len(retained) == 4001 and indices[-1] == 4354

    # Proposal only: no floating decision is the final certificate.
    import numpy as np
    from scipy.spatial import ConvexHull
    X = np.asarray([[float(v) for v in p] for p in retained], dtype=float)
    hull = ConvexHull(X)
    assert len(hull.vertices) == len(retained), 'Proposal omitted a point'
    triangles = hull.simplices.copy()
    normals = np.cross(
        X[triangles[:, 1]] - X[triangles[:, 0]],
        X[triangles[:, 2]] - X[triangles[:, 0]]
    )
    reverse = np.einsum('ij,ij->i', normals, hull.equations[:, :3]) < 0
    triangles[reverse, 1], triangles[reverse, 2] = (
        triangles[reverse, 2].copy(), triangles[reverse, 1].copy()
    )

    target = output / 'body'
    target.mkdir(exist_ok=True)
    vertices_text = ''.join(
        ','.join(str(v) for v in (*p, Q(0))) + '\n' for p in retained
    )
    triangles_text = ''.join(
        ','.join(str(int(i)) for i in t) + '\n' for t in triangles
    )
    (target / 'vertices.csv.gz').write_bytes(
        gzip.compress(vertices_text.encode(), mtime=0)
    )
    (target / 'triangles.csv.gz').write_bytes(
        gzip.compress(triangles_text.encode(), mtime=0)
    )
    (target / 'source_indices.json').write_text(json.dumps(indices))
    definition = {
        'name': 'FUS_SUB4001', 'D': 1, 'fixed_lambda': '0',
        'expected_VEF': [4001, 11100, 7101],
        'expected_class': [1, 1, 0]
    }
    (target / 'definition_parameters.json').write_text(
        json.dumps(definition, indent=2)
    )

    # The inherited checker is independent of the proposal/construction.
    # Generalize only its old target apex ID. Geometry and predicates
    # are not weakened, skipped, or changed to floating tests.
    source_code = verifier.read_text(encoding='utf-8')
    assert '4354' in source_code
    source_code = source_code.replace('4354', '(nv-1)')
    new_verifier = output / 'verify_rational.py'
    new_verifier.write_text(source_code, encoding='utf-8')
    run_checked([sys.executable, '-S', str(new_verifier), str(target)], output)

    report = json.loads((target / 'rational_verification.json').read_text())
    assert (report['V'], report['E'], report['F'], report['C']) == (
        4001, 11100, 7101, 22200
    )
    assert report['equilibrium_class'] == [1, 1, 0]
    assert report['zero_true_edge_predicates'] == 0
    summary = {
        k: report[k] for k in ('status', 'V', 'E', 'F', 'C', 'equilibrium_class')
    }
    summary['parent_raw_table_sha256'] = RAW_TABLE_SHA
    summary['retained_raw_table_sha256'] = digest(vertices_text.encode())
    summary['removed_vertices'] = len(removed)
    (output / 'replay_summary.json').write_text(json.dumps(summary, indent=2))
    print(json.dumps(summary, indent=2))

if __name__ == '__main__':
    if len(sys.argv) != 3:
        raise SystemExit('usage: construct_FUS_SUB4001.py PARENT_ZIP_OR_JOURNAL OUTPUT')
    main(Path(sys.argv[1]), Path(sys.argv[2]))
```

A replay must finish and its resulting report must be read before upgrading the checkpoint's **fresh-replay status**. An unfinished process, a constructor completing without the checker, or a numerical `(1,1,0)` count does not close that gate.

## 5. What the complete exact checker must establish

For clarity, the certificate is not just a count assertion. The inherited global checker reconstructs supporting planes from exact rational vertices, identifies identical planes exactly, and removes triangulation diagonals inside maximal faces. It verifies the polygon boundary cycles and their strict in-plane convexity, complete plane-equality contact sets, oriented two-face edge incidence, connectedness, and vertex links. Every listed vertex must have three independent supporting normals. The global plane–point inequalities and complete contact sets establish the actual convex boundary rather than relying on Qhull.

For the calculated own centroid g, write v_i=p_i-g. With an outward face normal N, the oriented face-side predicate on edge i→j is

\[
N\cdot(v_i\times v_j).
\]

A maximal face is stable exactly when all its true boundary-side predicates are positive. A vertex is unstable exactly when

\[
v_i\cdot(v_j-v_i)<0
\]

for every true neighbour j. This test includes the complete tangent cone at nonsimple vertices.

For each true edge, let its two incident faces supply the two correctly oriented face-side predicates. A saddle requires **all four** conditions: both endpoint radial dots negative and both face-side predicates positive. Weak versions must also be checked to detect boundary equilibria. An interior line foot alone is not a saddle certificate, and Euler's equilibrium identity is not used to infer the absence of saddles.

The stable hexagon and apex must additionally be checked against the global supporting-plane-distance and vertex-radius extrema. This prevents the previous error mode in which tiny local face margins disguise a macroscopic inradius inconsistency.

## 6. An exact mechanism for leaving the planar fixed-cardinality chart

### 6.1 Interiorization of an old vertex uses its entire normal cone

Let P₀ be a full-dimensional rational convex polyhedron. At an old vertex w, let all incident maximal supporting planes be

\[
n_j\cdot x\leq h_j,\qquad h_j=n_j\cdot w.
\]

Insert a point q. Then

\[
\boxed{w\in\operatorname{int}\operatorname{conv}(P_0,q)
\iff n_j\cdot(q-w)>0\text{ for every incident maximal facet }j.}
\]

Proof: every supporting normal of P₀ at w is a nonnegative combination of the incident facet normals. If every displayed dot is positive, no nonzero such normal can support the enlarged body at w. Conversely, a facet normal with nonpositive dot still supports the enlarged body at w. This uses every generator of the normal cone; selecting an arbitrary three incident faces is not valid at a nonsimple vertex.

This provides genuine vertex disappearance. It is not necessary to force w onto a prescribed true edge. With frozen y,z, generic disappearance can be into the relative interior of one new maximal facet, with normal-cone dimension one at the event, followed by strict interiority.

### 6.2 Rational support-event intervals for x motion

Take

\[
q(s)=q_0+s\,d\,e_x
\]

with rational q₀,d. The strict visibility inequalities are

\[
a_j+b_js>0,
\quad a_j=n_j\cdot(q_0-w),\quad b_j=d\,n_{jx}.
\]

Their intersection is an exactly computable open rational interval. When every b_j is positive, disappearance occurs after

\[
\tau_w=\max_j\frac{h_j-n_j\cdot q_0}{d\,n_{jx}}.
\]

For mixed signs, positive b_j give lower bounds, negative b_j give upper bounds, and b_j=0 requires a_j>0. This is a finite exact computation, not a parameter grid.

At a boundary parameter, zero contact does not by itself prove that w has ceased to be a vertex. Reconstruct the complete contact set. If w belongs to the relative interior of one maximal facet, its normal cone has rank one; if it is on an actual edge, use the full two-dimensional cone. Remove redundant points and collinear face-boundary segments before reporting V/E/F.

### 6.3 Multiple inserted controls: a necessary correction

It is **not sufficient** that every old incident facet be visible from at least one of several inserted points. Different facets may be visible from different points while a positive combination of their normals still supports w.

A correct finite certificate for points q₁,…,q_r is to find rational coefficients

\[
\lambda_k\geq0,\quad\sum_k\lambda_k=1,
\]

such that

\[
n_j\cdot\left(\sum_k\lambda_kq_k-w\right)>0
\quad\text{for every incident facet }j.
\]

The convex combination belongs to the enlarged body, so the preceding complete-normal-cone argument proves strict interiority. Conversely, separation of the convex hull of the column vectors `((n_j dot(q_k-w))_j)` from the positive orthant gives a nonzero nonnegative combination of old normals supporting w. Thus the finite linear feasibility test is also a complete criterion for this interiorization question.

This is useful for a communicating two-control or multi-face cavity: it handles nonsimple old vertices without the false union-of-visible-faces shortcut.

## 7. Geometry and actual mass can be certified together on each x-motion cell

Suppose any finite set of vertices moves affinely only in x, in exact half-turn pairs:

\[
p_i(s)=(a_i+b_i s,y_i,z_i).
\]

This includes motion in a rational affine coplanarity chart, not merely a single moved point. On a fixed oriented boundary triangulation:

\[
6V(s)=\sum_f\det(p_i(s),p_j(s),p_k(s))
\]

is affine in s, because only one coordinate column changes. The axial first moment

\[
24M_x(s)=\sum_f\det(p_i(s),p_j(s),p_k(s))
\bigl(x_i(s)+x_j(s)+x_k(s)\bigr)
\]

is quadratic. Half-turn symmetry makes M_y=M_z=0 exactly. The actual mechanical centre is therefore

\[
g_x(s)=\frac{M_x(s)}{V(s)},
\]

not a fixed external point.

Every four-point support determinant is affine in s. Consequently geometric support walls are rational, unless the determinant vanishes identically. Coplanarity can be enforced by exact linear equations in the x controls.

For mechanics, write `W(s)=6V(s)` and `M(s)=24M_x(s)`, so `g_x=M/(4W)`. A raw directed vertex predicate is quadratic in s minus g_x times an affine polynomial. A face-side predicate has the same degree structure: the unnormalized normal and coordinate cross product are affine in their variable components, yielding a quadratic raw term and an affine coefficient of g_x. Multiplication by positive `4W(s)` gives a polynomial of degree at most **three**.

Thus all four true-edge conditions, all face-side predicates and all vertex radial predicates reduce to exact univariate polynomials of degree at most three on a fixed actual face-lattice cell. A complete continuation can:

1. isolate its rational support walls and rebuild the maximal face lattice at each wall;
2. prove positive volume and calculate the exact centroid function on each cell;
3. isolate the relevant cubic mechanical roots, or certify strict witnesses by exact Bernstein subdivision;
4. classify the wall and both adjacent cells, explicitly including weak boundary equilibria.

This gives an effective exact route to a geometric vertex-loss event followed, when necessary, by a genuine stable–saddle cancellation. It does **not** imply that every proposed cavity has a winning cell. A finite failed sweep is not an infeasibility theorem, and a winning endpoint does not certify its entire incoming path.

### A rank-loss point need not be an equilibrium

Let r be a retained point of the body and let g be the actual centroid. If

\[
(p-g)\cdot(r-p)>0,
\]

then p cannot be an equilibrium of any feature type: the purported radial supporting plane would have r strictly outside it.

For a patch whose vertices p_i all satisfy that strict inequality with the same retained r, concavity gives

\[
\phi\!\left(\sum_i\alpha_i p_i\right)
=\sum_i\alpha_i\phi(p_i)
+\sum_{i<j}\alpha_i\alpha_j\|p_i-p_j\|^2>0,
\]

where `phi(p)=(p-g) dot(r-p)` and the alpha_i form a convex combination. This certifies the whole patch, including a newly flat face and all mixed normal cones at its seams. A finite subdivision with different retained witnesses on different leaves is also valid. With moving g(s), the corresponding vertex checks are among the cubic predicates above and must be certified over the actual parameter interval.

## 8. What was tried and what is not promoted

The reconstructible successful stage used C2-paired deletion on the literal fusion coordinates, recomputing the actual hull and filled-volume centroid after each numerical proposal. Its recovered complete mask is printed in Section 3. Only the final endpoint's recorded exact check is used; no continuous safe path through all 177 deletion proposals is claimed.

Further exploration targeted whole-star planarization with fixed y,z, outward x controls intended to swallow neighbouring stars, and event-aligned cavity replacement. These are genuinely different from continuing to fuse facets while insisting that all 4355 vertices remain extreme. However, the later experimental states are **not admitted as additional exact successors here**: a readable fresh verification transcript and a complete confirmed endpoint definition were not recovered for promotion in this resumed turn. No numerical near-winner is silently upgraded.

The distinction matters. An exact coordinate formula, an observed loss of normal rank, or a small numerical count is not enough. The actual post-event convex hull may split old nonsimplicial faces, make other points redundant, or create a stable–saddle packet after its centroid changes. Those possibilities are precisely why the full endpoint and wall checks above remain mandatory.

## 9. Most useful continuation

Start by executing the supplied FUS-SUB4001 reconstruction and reading its complete fresh exact report. Keep the original parent raw table and the source-index map intact. This closes the resumed-session evidence gap without inventing a later object.

Then use the full-normal-cone visibility interval to choose an outward control whose **actual vertex disappearance occurs before its first adverse own-centroid mechanical root**. For a promising multi-face cavity, allow a small communicating set of controls and use the convex-combination visibility certificate rather than freezing every old planar patch or relying on a union of visible facets. At each geometric event, remove nonextreme points and rebuild exact maximal faces and true edges before integrating mass and mechanics again.

The fixed-yz outline remains a limitation: a vertex whose yz projection is an exposed vertex of the projected convex hull cannot become interior while those projections remain fixed and distinct. That is a scoped geometric constraint, not a global prohibition on vertex elimination. It indicates where selected y,z controls must eventually be released.

Finally, preserving 4001 extreme vertices still forces `3V<=2E`, hence `C>=12004`. FUS-SUB4001 is therefore a useful vertex-loss checkpoint and verifier input, not a plausible end of the C<1000 search. The next substantial gain must again remove genuine vertices or redesign the finite architecture; another fixed-cardinality fusion-only result cannot close the requested gate.
