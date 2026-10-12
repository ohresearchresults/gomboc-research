# figure-0436

AI research report · 2026-09-20 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# Quiet Comet52 — a coupled retained-chord obstruction at the surviving C616 entrance

## Disposition and evidence boundary

**No new exact polyhedron is promoted in this continuation.** The construction entrance remains **QC52_SURVIVING_ROOT124_G9_F8B57E0F**, V174/E308/F136, own strict121/additionalweak000. No own110 result, new incidence census, or numerical convergence result is claimed.

The substantive result is a **quantified obstruction for coupled motion of the retained stable-face chord and the actual filled centroid**. It is not restricted to cutting the fixed parent. Subject to explicit retained-star and root conditions, it permits arbitrary changes elsewhere in the convex body and excludes an infinite family of coupled deformations. It also gives an exact necessary escape condition separating movement of the face from movement of the material centroid.

The two-link criterion itself is established background in this research. The new work here is its reduction to a particularly simple source-specific chord gate, its application to the actual3/44/72 star, and the resulting finite coupled-motion bound. Passing this gate is not a construction or a sufficient condition for cancellation.

Tool calls attempted a cap-assisted deformation and a release of the stable-plane contact3@140. However, reliable terminal outputs from those calls are not available in this continuation's tool-visible record. I therefore do not classify their proposed endpoints as verified bodies, quote solver outcomes, or treat them as failed mathematical searches. Any files written by those attempts remain unverified and ephemeral for purposes of this handoff. The result below is an analytical deduction from the literal, already certified parent data; its new replay program is complete, but its terminal markers are **expected**, not newly observed.

## 1. Exact parent and the relevant local geometry

Authority is the complete literal parent `figure-0434`, declared SHA256 `037b2078e4f89986594472b0f6e0df78ecf3cb43bbfb82dee2eea017099c529f`. Its22-file recovery is sufficient. The full supplied1655-line journal, common and branch memories, and literal parent were read through EOF in this continuation context. Unchanged source units already read in this chat were reused rather than replaced by an external source.

The surviving generator is10178bytes, SHA256 `f8b57e0f2b61c5c91093b6e989e7bc15486cb69a5e0e1a5458abc9cbe7684241`; RAW is11693bytes, SHA256 `a2a309b2b8ed47fdeeeccc0b30a6eec38ee3e9bb030869fcbb221c0407eb4f2e`. The unrecovered original8adb/6212 identity is not used.

At the parent's actual filled centroid g0:

- sole stable facet: input3, a20-gon;
- strict unstable vertices: apex94 and unwanted vertex124;
- sole saddle:124--134;
- unwanted vertex u=124 has neighbors w=120, z=134, q=109;
- u,w,z lie on facet3;
- w's other neighbors are91 and117;
- all unchanged exits from w are strictly descending, and q has smaller squared radius than w;
- apex94 is a distinct strict unstable vertex.

These are the actual maximal-complex labels. Owners are u:{3,44,72}, w:{3,72,73}, z:{3,44,99}, q:{15,44,72,75}. The parent's cap certificate already verifies the needed descending-exit and radius comparisons, including a centroid neighborhood. 

The parent still has its one complete physical elder bar, delta/V^(2/3) in[418537478,418537479]/10^12, with strict-upper component{124}. No changed physical or polar basin is certified here. The new obstruction is sufficient to exclude the target through an extra vertex equilibrium; it does not assert a constant S/H census over its deformation family.

## 2. Coupled-star theorem

Let L be any full-dimensional convex polyhedron of uniform volume density, and let g be its **actual volume centroid**. Use actual exposed vertices and actual true-edge adjacency after deformation. Suppose L has distinct vertices u,w,z,q,a with these properties:

1. u has exactly the three neighbors w,z,q, and u,w,z lie on one maximal planar facet.
2. Every true edge from w other than w--u is strictly descending: `(w-g)·(v-w)<0` for every such neighbor v.
3. `|q-g|² <= |w-g|²`.
4. a is a strict unstable vertex distinct from w and u.

Define the retained chord and its gate by

`d = z-w`,
`s = (w-g)·d`,
`e = |d|²`,
`Lchord = 4s+e`.

**If Lchord<=0, then L has at least two strict unstable vertices.** This conclusion is independent of the total edge count. In particular, no E<=310 member satisfying these hypotheses can be own110.

There is also a closed weak-inclusive version. Replace condition2 by nonpositive exits, `(w-g)·(v-w)<=0`. Then Lchord<=0 forces either another strict unstable vertex or an additional weak vertex equilibrium, distinct from a. Thus the target strict110/additionalweak000 is still excluded. The stronger conclusion of two **strict** U requires the strict form of condition2.

### Proof

Translate by g. If `w·(u-w)<0`, all incident derivatives at w are negative under condition2, so w is strict unstable. Under its closed variant, w is either strict or additional weak unstable. Either outcome is distinct from a.

Otherwise `w·(u-w)>=0`. Since u and w are distinct,

`|u|²-|w|² = 2w·(u-w)+|u-w|² > 0`.

Consequently `u·(w-u)<0`. Condition3 and Cauchy give `u·(q-u)<0` as well. It remains to show `u·(z-u)<0`.

Let p be the perpendicular projection of the origin onto the common facet plane, and write W=w-p, U=u-p, Z=z-p. Differences within the plane have no normal component, so

`w·(u-w)=W·(U-W)`,
`u·(z-u)=U·(Z-U)`.

Put A=|W|², B=|Z|², C=W·Z. Here A>0 in the application; if W=0, the strict stable-foot assumption needed for that application has already failed.

The condition `U·(Z-U)>=0` is the closed disk

`|U-Z/2|² <= B/4`.

The maximum of W·U on that disk is `(C+sqrt(A*B))/2`. Therefore a nonnegative two-link escape w→u→z requires

`2A-C <= sqrt(A*B)`.

Because `C=A+s` and `B=A+2s+e`, its cleared expression is

`(2A-C)²-A*B = s²-A*(4s+e)`.

When Lchord=4s+e<=0 and d is nonzero, s<=-e/4<0. Thus2A-C=A-s>0, and the last expression is strictly positive. The required two-link escape is impossible, including its zero-derivative boundaries. Hence `u·(z-u)<0`; all three derivatives at u are negative, making u strict unstable. Together with a this proves the theorem.

The planar disk calculation gives the exact feasibility criterion for an unconstrained intermediate point in the facet plane. It does not guarantee a supporting realization in the whole polyhedron.

## 3. Exact specialization to the surviving3/44/72 star

The literal parent's verified bounds include

`A0=|w-g0|² >= 30588221/80000000`,
`B0=|z-g0|² <= 30740959/80000000`,
`C0=(w-g0)·(z-g0) <= 152070761/400000000`.

They were obtained with allowance for the parent's cap-centroid neighborhood, so they also hold at g0 itself. These are the surviving realization's bounds, not a substitution of the unrecovered original. 

The chord gate simplifies without computing a face normal or subtracting a squared plane distance:

`L0 = 4(w-g0)·(z-w)+|z-w|² = B0-3A0+2C0`.

Substituting the bounds gives the exact deduction

`L0 <= -488499/200000000 < 0`.

Define

`gamma = 488499/200000000 = 0.002442495`.

This is a source-derived finite separation, not a selected optimizer guard. It shows that changing u alone cannot complete the two-link escape. More importantly, the following formulas specify what a **coupled** retained-geometry/mass change must accomplish.

### A. Common translation of the retained chord or stable facet

Suppose the changed endpoints are w'=w+t and z'=z+t, while the actual new filled centroid is g'=g0+c. The rest of the body may change arbitrarily. Then

`Lchord' = L0 + 4d·(t-c)`.

As long as the theorem's actual adjacency, descending-exit, radius-order and distinct-root conditions hold, cancellation requires

**`d·(t-c) > gamma/4 = 488499/800000000`.**

The inequality is strict. Equality still leaves Lchord'<=0 and is excluded by the weak-inclusive argument.

This distinguishes movement of material from movement of the reference frame. Translating the face and moving the actual centroid by the same amount gives no progress on this gate. A translation normal to the facet also gives no direct chord contribution because d is tangent to that facet. Such a normal move can help only through its induced tangential centroid response, a change of the retained chord, or departure from the theorem's other hypotheses.

This is not a claim that a general support-height change translates its whole polygon rigidly. Intersections with adjacent supports usually move its vertices nonuniformly; those changes belong to the next formula.

### B. General coupled endpoint and centroid motion

Let

`w'=w+a`, `z'=z+b`, `g'=g0+c`,
`t=a-c`, `eta=b-a`, `x=w-g0`.

Thus t is the entry vertex's motion **relative to the actual centroid**, and eta is the change of the retained chord. An exact expansion gives

`Lchord'-L0 = 4t·d + (4x+2d)·eta + 4t·eta + |eta|²`.

Accordingly every successful cancellation retaining the theorem's local structure and distinct root must satisfy

**`4t·d + (4x+2d)·eta + 4t·eta + |eta|² > gamma`.**

This is a finite quadratic escape condition, not merely a first-order Jacobian test. It permits coupled support rotations, nonuniform motion of the stable polygon, and arbitrary redistribution of the remaining material, with c always equal to the new homogeneous centroid displacement.

The contrapositive is a scoped exclusion of the entire closed region where the left side is at most gamma, subject to the stated graph and sign conditions. It does not exclude root replacement, an incidence change at u or w, opening another exit from w, or reversing q's radius ordering.

### C. A simple finite coupled-motion corollary

The parent's certificate gives |x|<5/8 and |z-g0|<5/8, hence |d|<5/4. Therefore

`Lchord'-L0 <= 5|t|+5|eta|+4|t||eta|+|eta|²`.

If both `|t|<=1/5000` and `|eta|<=1/5000`, the right side is at most

`10001/5000000 = 0.0020002`.

Consequently

`Lchord' <= -88459/200000000 < 0`.

Thus this finite coupled neighborhood cannot cancel the pair while retaining the theorem's conditions. Unlike the old cap result, this statement allows movement of the retained endpoints and arbitrary changes elsewhere; unlike an unrestricted Hausdorff theorem, it explicitly conditions on the actual local graph and exits. It must not be broadened to every small deformation of the polyhedron.

## 4. The sharp planar gate after the quarter-chord condition is crossed

Lchord>0 is necessary but not sufficient. For the actual new facet plane, let p be the perpendicular foot of its actual centroid, A=|w-p|², s=(w-g)·(z-w), and e=|z-w|². Set

`Psi = s²-A*(4s+e)`.

When A-s>0, a nonnegative two-link route requires Psi<=0; two strictly positive links require Psi<0. The disk argument above is sharp for the unconstrained intermediate point in that plane.

A rational countercontrol prevents mistaking the simpler gate for success: W=(1,0), Z=(0,9/5) gives Lchord=6/25>0 but Psi=19/25>0, so no nonnegative two-link route exists. A boundary control W=(1,0), U=(1,1), Z=(0,2) has both directed derivatives exactly zero and Psi=0. The boundary must not be rejected as though it had a strict negative escape. These are endpoint-link controls, not full polyhedral equilibrium censuses.

For a moving plane n·r=b, with h=b-n·g,

`A=|w-g|²-h²/(n·n)`.

This makes the stable-plane/global-centroid coupling explicit. The derivative of the discarded normal-square term is

`d(h²/(n·n)) = 2h*dh/(n·n) - 2h²(n·dn)/(n·n)²`,

where `dh=db-dn·g-n·dg`. Omitting dg would optimize a free-reference problem rather than the requested homogeneous body.

For an actual differentiable exposed chart, the finite gate has derivative

`dLchord = 4(dw-dg)·d + (4(w-g)+2d)·(dz-dw)`.

A scale-invariant optimization quantity is Lchord/V^(2/3), whose derivative also contains `-(2Lchord/(3V))*dV`. This is a design gate for changing the retained interface, not a replacement for the whole physical/polar basin objectives or the final strict/weak census.

## 5. Consequential continuation

The next construction should deliberately change the entry-to-outlet chord120--134 relative to the actual centroid, or abandon one of the retained-star hypotheses. Merely flattening the old124 peak, translating the face together with its centroid, or lifting a rigid face normally while its tangential centroid coordinate stays fixed cannot cross the proved gate.

A stable-plane contact release is meaningful only when its resulting retained-vertex and mass motion is measured by the finite expression above. Even after that expression exceeds gamma and the planar two-link region becomes nonempty, one must realize the intermediate geometry as globally supporting, rebuild the true maximal complex, and demonstrate that the complete unwanted physical component disappears without a replacement physical or polar component. Spending either spare edge on changing the local graph is another genuine escape, but leaves this theorem's domain and requires a new graph analysis.

There is no new accepted body to prefer over the surviving parent. Its one physical bar, strict121 census, and two-edge headroom remain the constructive state. Canonical C622 remains the own110 incumbent.

## 6. Complete exact replay unit

The program below is self-contained for the new arithmetic certificate and rational link controls. With no arguments it checks all displayed constants and controls. With `--proof-dir`, it additionally locates the exact hash-pinned surviving A/B report in a freshly reconstructed parent proof directory and verifies the source-specific chord, local graph, planar obstruction, and baseline strict-root conditions directly with Fraction arithmetic.

Its optional geometric input is not a new missing dependency: it is produced by the already literal22-file parent capsule. No originating sandbox, numerical producer, NumPy, SciPy, or Library lookup is needed. Use the complete recovery program in parent `figure-0434`:

```sh
python -B -S QC52_SURVIVING_RECOVER.py PARENT
python -B -S PARENT/RECONCILE_REPLAY.py --case ROOT124_G9 --out PARENT_PROOF
python -B -S QC52_COUPLED_GATE.py
python -B -S QC52_COUPLED_GATE.py --proof-dir PARENT_PROOF --out COUPLED_GATE.json
```

The script intentionally searches the specified fresh proof directory for the pinned report content rather than assuming an output subdirectory layout. It accepts only230639bytes with SHA256 `bf713a4201231250cfb98d45cc35f47f27afee73a7938f700ce51359ef3b19f5`. That report identity belongs to the surviving realization, not the unavailable original.

Dependencies: Python3.11 or newer standard library; the parent reports were previously executed on CPython3.13.5. This new program has no newly observed execution receipt in this continuation. Expected markers are `QC52_COUPLED_GATE_CONSTANTS_PASS` and, with the reconstructed report, `QC52_SURVIVING_PARENT_QUARTER_GATE_PASS`. It prints the byte count and SHA256 of its generated certificate when run; no unobserved output hash is invented here.

```python
"""QC52 coupled retained-chord certificate.

No new physical body is defined by this program.
The optional input is the exact surviving ROOT124_G9 full audit,
reconstructible from the complete literal 22-file parent capsule.
All calculations below use only exact standard-library arithmetic.
"""
from fractions import Fraction as F
from pathlib import Path
import argparse
import hashlib
import json
import sys

if hasattr(sys, 'set_int_max_str_digits'):
    sys.set_int_max_str_digits(0)

AUDIT_BYTES = 230639
AUDIT_SHA = 'bf713a4201231250cfb98d45cc35f47f27afee73a7938f700ce51359ef3b19f5'
AL = F(30588221, 80000000)
BH = F(30740959, 80000000)
CH = F(152070761, 400000000)
GAMMA = F(488499, 200000000)
R = F(5, 8)
EPS = F(1, 5000)


def dot(a, b):
    assert len(a) == len(b)
    return sum((x*y for x, y in zip(a, b)), F(0))


def add(a, b):
    return [x+y for x, y in zip(a, b)]


def sub(a, b):
    return [x-y for x, y in zip(a, b)]


def mul(t, a):
    return [t*x for x in a]


def cross(a, b):
    assert len(a) == len(b) == 3
    return [a[1]*b[2]-a[2]*b[1],
            a[2]*b[0]-a[0]*b[2],
            a[0]*b[1]-a[1]*b[0]]


def interval(x, scale=10**12):
    x = F(x)
    lo = (x.numerator*scale)//x.denominator
    return {'lo': lo, 'hi': lo+1, 'denominator': scale}


def planar_gate(w, z):
    """Origin is the foot in the common plane, not a polar mass center."""
    d = sub(z, w)
    A = dot(w, w)
    s = dot(w, d)
    e = dot(d, d)
    L = 4*s+e
    psi = s*s-A*L
    return L, psi


def constants_and_controls():
    assert AL > 0
    assert BH-3*AL+2*CH == -GAMMA
    assert GAMMA/4 == F(488499, 800000000)
    # |x|<R and |d|<2R bound the exact finite perturbation.
    upper = 4*(2*R)*EPS + (4*R+4*R)*EPS + 5*EPS*EPS
    assert upper == F(10001, 5000000)
    assert GAMMA-upper == F(88459, 200000000) > 0

    w = [F(1), F(0)]
    z = [F(0), F(9, 5)]
    L, psi = planar_gate(w, z)
    assert L == F(6, 25) > 0
    assert psi == F(19, 25) > 0

    u = [F(1), F(1)]
    z = [F(0), F(2)]
    assert dot(w, sub(u, w)) == 0
    assert dot(u, sub(z, u)) == 0
    assert planar_gate(w, z)[1] == 0

    u = [F(3, 2), F(0)]
    z = [F(2), F(0)]
    assert dot(w, sub(u, w)) > 0
    assert dot(u, sub(z, u)) > 0
    assert planar_gate(w, z)[1] < 0

    # Exact algebraic regression of the finite coupled-motion identity.
    x = [F(2, 7), F(-3, 11), F(5, 13)]
    d = [F(-1, 17), F(2, 19), F(3, 23)]
    t = [F(1, 29), F(-2, 31), F(1, 37)]
    eta = [F(3, 41), F(1, 43), F(-2, 47)]
    old = 4*dot(x, d)+dot(d, d)
    new = 4*dot(add(x, t), add(d, eta))+dot(add(d, eta), add(d, eta))
    change = (4*dot(t, d)+dot(add(mul(4, x), mul(2, d)), eta)
              +4*dot(t, eta)+dot(eta, eta))
    assert new-old == change

    return {
        'gamma': str(GAMMA),
        'parent_gate_upper_bound': str(-GAMMA),
        'necessary_common_translation_projection': str(GAMMA/4),
        'coupled_relative_motion_radius': str(EPS),
        'coupled_chord_change_radius': str(EPS),
        'finite_change_upper_bound': str(upper),
        'remaining_gate_separation': str(GAMMA-upper),
        'positive_quarter_gate_is_not_sufficient_control': True,
        'closed_zero_derivative_link_control': True,
        'finite_perturbation_identity_control': True,
    }


def find_audit(root):
    root = Path(root)
    if not root.is_dir():
        raise ValueError('The specified parent proof directory does not exist')
    matches = []
    for p in sorted(root.rglob('*.json')):
        if p.is_file() and p.stat().st_size == AUDIT_BYTES:
            b = p.read_bytes()
            if hashlib.sha256(b).hexdigest() == AUDIT_SHA:
                matches.append((p, b))
    if not matches:
        raise ValueError('No exact surviving ROOT124_G9 audit matched the pinned identity')
    # Both independently generated A and B can match. Their content is identical.
    return matches[0]


def verify_parent(root):
    path, raw = find_audit(root)
    a = json.loads(raw)
    assert [a['V'], a['E'], a['F']] == [174, 308, 136]
    assert a['counts'] == [1, 2, 1]
    assert a['unstable_vertices'] == [94, 124]
    assert a['saddle_edges'] == [[124, 134]]
    X = [[F(v) for v in row] for row in a['raw_vertices']]
    g = [F(v) for v in a['raw_centroid']]
    assert len(X) == 174 and len(g) == 3
    edges = {tuple(sorted(e)) for e in a['edges']}
    assert len(edges) == 308
    adj = [set() for _ in X]
    for i, j in edges:
        adj[i].add(j)
        adj[j].add(i)
    u, w, z, q, apex = 124, 120, 134, 109, 94
    assert adj[u] == {w, z, q}
    assert adj[w]-{u} == {91, 117}
    assert {u, w, z}.issubset(set(a['faces'][3]))

    x = sub(X[w], g)
    y = sub(X[z], g)
    d = sub(X[z], X[w])
    A0, B0, C0 = dot(x, x), dot(y, y), dot(x, y)
    assert AL <= A0 and B0 <= BH and C0 <= CH
    assert A0 < R*R and B0 < R*R
    s, e = dot(x, d), dot(d, d)
    assert e > 0
    L0 = 4*s+e
    assert L0 == B0-3*A0+2*C0
    assert L0 <= -GAMMA

    for j in adj[w]-{u}:
        assert dot(x, sub(X[j], X[w])) < 0
    # Difference of squared radii avoids unnecessary centroid-square expansion.
    radius_gap = dot(sub(X[w], X[q]), sub(add(X[w], X[q]), mul(2, g)))
    assert radius_gap > 0
    ap = sub(X[apex], g)
    for j in range(len(X)):
        if j != apex:
            assert dot(ap, sub(X[j], X[apex])) < 0

    normal = cross(sub(X[u], X[w]), d)
    nn = dot(normal, normal)
    assert nn > 0
    h = dot(normal, x)
    normal_square = h*h/nn
    A = A0-normal_square
    B = B0-normal_square
    C = C0-normal_square
    assert A > 0 and B > 0
    assert s == C-A
    assert e == A+B-2*C
    psi = s*s-A*L0
    assert psi == (2*A-C)**2-A*B
    assert 2*A-C > 0 and psi > 0

    return {
        'audit_sha256': AUDIT_SHA,
        'audit_bytes': len(raw),
        'identity': 'QC52_SURVIVING_ROOT124_G9_F8B57E0F',
        'V_E_F': [174, 308, 136],
        'strict_census_from_pinned_audit': [1, 2, 1],
        'u_w_z_q_apex': [u, w, z, q, apex],
        'entry_other_neighbors': sorted(adj[w]-{u}),
        'parent_chord_gate_interval': interval(L0),
        'certified_parent_gate_upper_bound': str(-GAMMA),
        'planar_sharp_obstruction_positive': True,
        'entry_other_exits_strictly_negative': True,
        'other_tip_neighbor_radius_smaller': True,
        'distinct_apex_all_point_strictness': True,
        'new_body_constructed': False,
    }


def main():
    if not __debug__:
        raise RuntimeError('Assertions must remain enabled')
    p = argparse.ArgumentParser()
    p.add_argument('--proof-dir')
    p.add_argument('--out')
    args = p.parse_args()
    report = {'constants_and_controls': constants_and_controls()}
    print('QC52_COUPLED_GATE_CONSTANTS_PASS')
    if args.proof_dir:
        report['parent_application'] = verify_parent(args.proof_dir)
        print('QC52_SURVIVING_PARENT_QUARTER_GATE_PASS')
    b = json.dumps(report, sort_keys=True, separators=(',', ':')).encode('utf-8')
    if args.out:
        Path(args.out).write_bytes(b)
    print(b.decode('utf-8'))
    print('CERTIFICATE_BYTES_SHA256', len(b), hashlib.sha256(b).hexdigest())


if __name__ == '__main__':
    main()
```

## Final status

The completed mathematical result is a source-specific, weak-aware **coupled retained-chord/actual-centroid exclusion**, with an explicit finite quadratic escape condition and a sharp planar follow-on test. It does not solve the full branch and does not establish any new exact nonwinner. Numerical attempts without accessible terminal evidence are not promoted. The surviving C616 parent remains reconstructible and available for a construction that crosses this gate or changes its actual local incidence/root assumptions.
