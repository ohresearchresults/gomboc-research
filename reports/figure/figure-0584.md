# figure-0584

Historical AI scientific report · saved 2026-09-28 UTC. Claims below retain their original status and have not all been independently checked. The current retained construction is C622; the C<500 search remains open.

Public text derivative: internal-record-identifiers-replaced.

---

# Steady Quartz 74 — exact moment control using existing vertex stars

## Result and verification boundary

**No new computed endpoint is accepted in this continuation.** The runtime calls were skipped rather than returning inspectable execution results. I therefore do not count the attempted numerical runs as completed experiments, and do not assert new coordinates, bar depths, equilibrium counts, or output hashes from them.

The retained computational input is **SQ74D_PRUNE_BEST_G6**, author-reported **V53/E153/F102, own211/additionalweak000, P=[], Q=[0.7964296564575203]**. Its current stable triangles are [7,31,18] and [7,20,38], both avoiding U12; its saddle edge is [50,52]. These are the current input identities, not the retired C330 port.

The substantive result here is an exact finite control mechanism: **tangential motions of mutually nonadjacent existing vertex stars can correct three-dimensional first moments by a rational linear solve while preserving volume exactly.** No added vertices, external pyramids, density changes, or coordinate translations are needed for this correction. A supplementary eight-corner certificate can establish convexity and a common positive U-witness forest throughout a moving-vertex parameter box. At the parameter value satisfying the exact moment equation, that reference-center certificate becomes a certificate at the actual homogeneous centroid.

This extends the fixed-height pyramid control in the supplied memory to an arbitrary triangulated vertex star, whose link need not be planar. It is a mathematical construction mechanism, **not a claim that a full-rank, sufficiently capacious controller frame has already been demonstrated on PRUNE_BEST**. The complete implementation below is unexecuted. It reconstructs the authenticated parent point literal, selects controllers, makes finite changes to the current Q component and crossing interface, and audits every resulting nominated body exactly.

## Input and reading continuity

The completed reading from the preceding interrupted attempt was retained: the current notebook through EOF1190 and both required literal parents. The supplied notebook manifest is **255504 bytes**, SHA-256 **2847a2f65d173c3970c2852ecb6cb8eb676b58c5798b641c17ae5db64b631f42**.

The source-authority parents are:

- **figure-0577**, SHA-256 **e50283583f88c4a7d16c5e636796f478143b4909e6f9cec4404e845cb98d79be**.
- **figure-0580**, SHA-256 **7dcb3587aaadc980bc65e9fa8781da3fc19025737460b62ea13962e379611019**.

No additional scientific source or research connector was used. No newly verified source conflict is asserted. The missing evidence is execution of the parent-specific controller selection and candidate audits, not a missing external construction package.

## 1. Exact finite first moments of one existing star

Let the closed boundary be triangulated and consistently outward oriented. For a chosen vertex p, cyclically write every incident triangle as (p,a_f,b_f). Define

A = sum_f a_f cross b_f,

B = sum_f (a_f+b_f)(a_f cross b_f)^T,

J = ((p dot A) I + B)/24.

Move only p to p+d, retaining this oriented face complex. Direct signed-tetrahedron integration gives the **finite identities**

Delta V = (A dot d)/6,

Delta M = Jd + [p(A dot d) + d(A dot d)]/24,

where M is the unnormalized first-moment vector, not the centroid.

Consequently, for any finite displacement satisfying **A dot d=0**,

**Delta V=0 and Delta M=Jd exactly.**

There is no neglected higher-order term under that tangency condition. In particular, this is not a differential centroid approximation followed by an assumption that a finite step has the same mass.

### Derivation

For one incident triangle, put c_f=a_f cross b_f and D_f=p dot c_f. Its signed volume contribution is D_f/6 and its first-moment contribution is D_f(p+a_f+b_f)/24. After replacing p by p+d, the first-moment difference is

[D_f d + (d dot c_f)(p+a_f+b_f) + (d dot c_f)d]/24.

Summing yields the formulas above, since sum D_f=p dot A. The calculation uses neither a planar link nor an apex over one fixed polygon.

As a hand-checkable example, take the tetrahedron with vertices 0,e1,e2,e3 and move e3 to e3+(1/7,-2/11,0). Its volume remains 1/6. Its first-moment change is (1/168,-1/132,0), and its centroid becomes (2/7,9/44,1/4), agreeing with the direct average of the four vertices. This checks the finite formula; it is not a new PRUNE_BEST endpoint.

## 2. Several stars give an exact physical centroid correction

Choose three scalar tangent directions t_l, each assigned to an existing vertex i_l. Two directions may belong to the same vertex. Require that **distinct controlled vertices are nonadjacent** in the current triangular boundary. Thus no boundary triangle contains two different controlled vertices.

Let T have columns J_i_l t_l. For any simultaneous control parameters s,

V(s)=V_b,

M(s)=M_b+Ts.

These are exact finite identities. The nonadjacency condition eliminates mixed contributions between different controlled stars; two directions at one vertex are also safe because their combined displacement remains in the same plane A_i dot d_i=0.

For a prescribed target center g0, solve

**Ts = V_b g0 - M_b.**

When det T is nonzero, this is a rational 3 by 3 solve. The resulting body has exactly g0 as its homogeneous centroid, provided its final boundary is actually the claimed convex boundary. The volume may have changed during the main geometric deformation; the compensating star motions themselves preserve that new volume exactly.

### Co-design rather than a claimed bridge followed by an unrelated repair

The main geometry and the controller equation should be treated as one parameterized construction. For each proposed whole-boundary baseline, recompute its star coefficients and solve the exact equation before evaluating its equilibria or bars. The baseline can be algebraically evaluated even when it is not itself a valid convex body; only the final corrected point set is eligible for a physical claim, and its geometry must be certified.

The coefficients generally depend on the moved neighboring vertices. They must be recomputed after a baseline change. If a normal-fan event changes a controller star, the old coefficients are no longer authority: reconstruct the new hull and choose or recompute the chart.

The controller selection is not an existence theorem. For example, the two apices of a triangular bipyramid are nonadjacent, but their volume-preserving tangential motions are parallel to the base plane. Those controls cannot correct a first moment perpendicular to that plane. Graph independence alone therefore does not establish rank. Nor does rank establish usable finite displacement capacity.

## 3. A moving-shape box certificate, not the old center cube

For a fixed baseline and controller frame, put each scalar s_l in a closed interval [-b_l,b_l]. There are eight corners for three scalar controls.

**Convexity.** Every oriented face-versus-nonincident-vertex determinant is multiaffine in these scalar parameters: each scalar moves only one vertex, and the determinant is affine in each vertex position. Therefore strict supporting-side inequalities at all eight corners establish those inequalities throughout the box. The same argument applies to keeping a fixed g0 strictly inside every supporting halfspace. With the closed inherited triangular complex, this certifies its faces as the true maximal facets throughout the box.

**A common U forest.** Suppose every material vertex except a designated root has a single witness j for which

(p_i(s)-g0) dot (p_j(s)-p_i(s)) > 0

at every corner. With g0 fixed, this score is separately concave in every scalar control: a scalar moving the source contributes a nonpositive quadratic term; a scalar moving only the destination contributes a linear term. A separately concave function on a box attains a minimum at a corner. Thus every selected witness stays positive throughout the box.

Along each arrow squared radius strictly increases. The fixed witness graph consequently cannot contain a directed cycle. If all paths end at the designated root, each box member has that unique strict U and no additional weak U **with respect to g0**.

Finally, when the exact moment solution s lies inside this certified box, its actual homogeneous centroid is g0. The selected body therefore has physical U1, not merely reference U1.

This argument must not be misapplied to the varying own centroids of all the other box members. Their centroids generally differ from g0. It also does not certify S1 or the complete equilibrium census by corner checking; the final body still receives a direct exact S/U/H and P/Q audit.

## 4. Application to the current small-V frontier

All controller motions use existing points. Keeping at most53 material points gives E<=3V-6<=153, even if a later implementation permits fan changes. In the strict inherited simplicial chart, the actual counts remain 53/153/102. **The 32 extra material-point slots are not spent on moment controllers.** This is different from reserving three new apexes after every attempted surgery.

The prototype constructs its target region from the actual parent audit. It finds the positive Q bar, its entire dying polar component immediately above its exact death level, and the physical edge corresponding to that death. It does not hard-code retired labels. Its finite baseline fields combine an outward motion distributed over that whole component, a contraction of the current death edge and its two-ring vertex neighborhood, and a spatially weighted rotational field. The moment correction is included in each candidate before its physical census is evaluated.

The concrete unresolved issue is whether such a finite stable-basin/interface change can be accompanied by a correction that remains in a convex, U1-safe moving-star domain while eliminating the whole Q component. **Neither controller rank nor sufficient capacity on PRUNE_BEST has been computed in this continuation.** A singular chosen matrix, a failed box, or a failed fixed-fan trial would be evidence about that chart or candidate, not a proof that the 53-point shape family is empty.

## 5. Complete unexecuted implementation

Save the following unit as **SQ74E_STAR_CHART.py**. It uses only the Python standard library and is intended for Python3.13, the supplied parent environment. It does not invoke an optimizer or require NumPy, SciPy, Torch, a connector, or a historical workspace.

Run:

    python SQ74E_STAR_CHART.py SQ74D_RECOVER.py --out sq74e_star_results --max-evals 24

The input-only loader reads the literal SQ74D PAYLOAD and checks the authoritative uncompressed dictionary identity: **67267 bytes / 3c53f52e161499be2c96ba442a65bb9b7b5085e5bb88d894bc2c2f66abe18fb3**. It accepts quoted strings and their explicitly written .lstrip() suffixes, without executing the parent wrapper. A mismatch is a hard error.

The full old SQ74D replay still has its supplied SQ74C dependency. This new unit instead needs only SQ74D's authenticated complete PRUNE_BEST point literal and supplies its own complete hull, mass, census, and bar routines. It does not silently substitute another endpoint.

The default search has a **24-evaluation bound**, drawn from five rational amplitudes and18 finite whole-patch fields. It permits vertex degrees greater than three. It explicitly rejects unhandled nonsimplicial facet charts rather than counting a triangulation as maximal facets. Every output includes exact coordinates, actual volume and first moments, actual centroid, true facets and edges, all strict/additionalweak equilibria, and every positive P/Q bar without a floor. The run manifest computes actual file byte counts and SHA-256 values when executed.

Prospective terminal markers are **SQ74E_STAR_CHART_SEARCH_FINISHED_NO_WINNER** or **SQ74E_EXACT_OWN110_FOUND**. Neither was observed here. There is no new selected input hash or claimed replay match in this handoff.

```python
import argparse, ast, base64, hashlib, itertools, json, lzma, math, sys
from fractions import Fraction as R
from pathlib import Path

if hasattr(sys, 'set_int_max_str_digits'):
    sys.set_int_max_str_digits(0)
Z = (R(0), R(0), R(0))
AXES = ((R(1), R(0), R(0)), (R(0), R(1), R(0)), (R(0), R(0), R(1)))
PARENT_BYTES = 67267
PARENT_SHA = '3c53f52e161499be2c96ba442a65bb9b7b5085e5bb88d894bc2c2f66abe18fb3'

def add(a, b): return tuple(x+y for x, y in zip(a, b))
def sub(a, b): return tuple(x-y for x, y in zip(a, b))
def mul(t, a): return tuple(t*x for x in a)
def dot(a, b): return sum(x*y for x, y in zip(a, b))
def cross(a, b):
    return (a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2], a[0]*b[1]-a[1]*b[0])
def det(a, b, c): return dot(a, cross(b, c))
def vsum(rows):
    s = Z
    for row in rows: s = add(s, row)
    return s

def encoded(x):
    if isinstance(x, R): return str(x)
    if isinstance(x, dict): return {str(k): encoded(v) for k, v in x.items()}
    if isinstance(x, (list, tuple)): return [encoded(v) for v in x]
    return x

def write_json(path, obj):
    b = (json.dumps(encoded(obj), sort_keys=True, indent=2)+chr(10)).encode()
    path.write_bytes(b)
    return dict(bytes=len(b), sha256=hashlib.sha256(b).hexdigest())

def parent_points(path):
    text = path.read_text()
    lines = text.splitlines()
    start = next(i for i, s in enumerate(lines) if s.replace(' ', '').strip() == 'PAYLOAD=(')
    strings = []
    for line in lines[start+1:]:
        s = line.strip()
        if s == ')': break
        if not s: continue
        if s.endswith('+'): s = s[:-1].rstrip()
        strip = s.endswith('.lstrip()')
        if strip: s = s[:-9]
        value = ast.literal_eval(s)
        if not isinstance(value, str): raise ValueError('Non-string PAYLOAD entry')
        strings.append(value.lstrip() if strip else value)
    raw = lzma.decompress(base64.b85decode(''.join(strings)))
    if len(raw) != PARENT_BYTES or hashlib.sha256(raw).hexdigest() != PARENT_SHA:
        raise ValueError('SQ74D source dictionary identity mismatch')
    files = json.loads(raw)
    keys = [k for k in files if Path(k).name == 'SQ74D_PRUNE_BEST_G6_LITERAL.json']
    if len(keys) != 1: raise ValueError('Exact PRUNE_BEST literal not uniquely present')
    literal = files[keys[0]].encode()
    data = json.loads(literal)
    if data['name'] != 'SQ74D_PRUNE_BEST_G6': raise ValueError('Wrong endpoint name')
    D = int(data['denominator'])
    rows = data['vertices']
    if D != 10**6 or len(rows) != 53: raise ValueError('Wrong parent grid or material count')
    homogeneous = []
    for row in rows:
        if len(row) != 3: raise ValueError('Bad point row')
        g = math.gcd(*map(int, row), D)
        homogeneous.append(tuple(int(v)//g for v in row)+(D//g,))
    homogeneous = sorted(set(homogeneous))
    if len(homogeneous) != 53: raise ValueError('Unexpected duplicate parent points')
    p = [tuple(R(v, h[3]) for v in h[:3]) for h in homogeneous]
    return p, dict(parent_dictionary_sha256=PARENT_SHA,
                   literal_bytes=len(literal), literal_sha256=hashlib.sha256(literal).hexdigest(),
                   capsule_file_sha256=hashlib.sha256(path.read_bytes()).hexdigest())

def edges_of(faces):
    e = {}
    for j, f in enumerate(faces):
        for a, b in zip(f, f[1:]+f[:1]):
            e.setdefault(tuple(sorted((a, b))), []).append(j)
    if not all(len(v) == 2 for v in e.values()):
        raise ValueError('Boundary is not a closed two-manifold')
    return e

def strict_fan(p, faces):
    smallest = None
    for f in faces:
        a, b, c = (p[i] for i in f)
        n = cross(sub(b, a), sub(c, a))
        if n == Z: return None
        for i, v in enumerate(p):
            if i in f: continue
            s = -dot(n, sub(v, a))
            if s <= 0: return None
            smallest = s if smallest is None else min(smallest, s)
    return smallest

def hull(p):
    D = math.lcm(*(a.denominator for v in p for a in v))
    x = [tuple(int(a*D) for a in v) for v in p]
    found = {}
    for i, j, k in itertools.combinations(range(len(x)), 3):
        n = cross(sub(x[j], x[i]), sub(x[k], x[i]))
        if n == (0, 0, 0): continue
        h = dot(n, x[i])
        s = [dot(n, a)-h for a in x]
        if min(s) < 0 < max(s): continue
        if min(s) == max(s) == 0: raise ValueError('Not full dimensional')
        eq = tuple(a for a, v in enumerate(s) if v == 0)
        if len(eq) != 3:
            raise ValueError('Unhandled nonsimplicial maximal facet; no triangulation substitute')
        found[eq] = (i, j, k) if max(s) <= 0 else (i, k, j)
    faces = [found[k] for k in sorted(found)]
    if set(itertools.chain.from_iterable(faces)) != set(range(len(p))):
        raise ValueError('This fixed-fan chart requires all supplied points extreme')
    e = edges_of(faces)
    if len(p)-len(e)+len(faces) != 2 or strict_fan(p, faces) is None:
        raise ValueError('Invalid convex triangular boundary')
    return faces

def mass(p, faces):
    V = R(0); M = Z
    for f in faces:
        a, b, c = (p[i] for i in f)
        d = det(a, b, c)
        V += d/6
        M = add(M, mul(d/24, add(add(a, b), c)))
    return V, M

def segment_level(a, b):
    d = sub(b, a); dd = dot(d, d)
    if dd == 0: raise ValueError('Zero-length true edge')
    t = max(R(0), min(R(1), -dot(a, d)/dd))
    z = add(a, mul(t, d))
    return dot(z, z)

def bars(points, edges):
    radius = [dot(p, p) for p in points]
    parent = list(range(len(points)))
    def find(i):
        while parent[i] != i:
            parent[i] = parent[parent[i]]; i = parent[i]
        return i
    events = sorted([(segment_level(points[a], points[b]), (a, b)) for a, b in edges],
                    key=lambda t: (-t[0], t[1]))
    result = []
    for level, edge in events:
        i, j = find(edge[0]), find(edge[1])
        if i == j: continue
        if radius[i] < radius[j] or (radius[i] == radius[j] and i > j): i, j = j, i
        if radius[j] > level:
            result.append(dict(root=j, edge=edge, birth2=radius[j], death2=level,
                               depth=(radius[j]-level)/radius[j]))
        parent[j] = i
    return sorted(result, key=lambda b: (-b['depth'], b['root'], b['edge']))

def audit(p, faces):
    if strict_fan(p, faces) is None: raise ValueError('Outside the strict inherited hull chart')
    ef = edges_of(faces); V, M = mass(p, faces)
    if V <= 0: raise ValueError('Nonpositive physical volume')
    g = mul(1/V, M); z = [sub(v, g) for v in p]
    normals = []; poles = []; S = []; wS = []
    for j, f in enumerate(faces):
        a, b, c = (p[i] for i in f)
        n = cross(sub(b, a), sub(c, a)); h = dot(n, sub(a, g))
        if h <= 0: raise ValueError('Own centroid not strictly interior')
        normals.append(n); poles.append(mul(1/h, n))
        guard = [dot(n, cross(z[u], z[v])) for u, v in zip(f, f[1:]+f[:1])]
        if min(guard) > 0: S.append(j)
        elif min(guard) == 0: wS.append(j)
    U = []; wU = []
    for i, a in enumerate(z):
        mx = max(dot(a, sub(b, a)) for j, b in enumerate(z) if j != i)
        if mx < 0: U.append(i)
        elif mx == 0: wU.append(i)
    H = []; wH = []
    for edge, inc in sorted(ef.items()):
        a, b = (z[i] for i in edge); d = sub(b, a)
        t = -dot(a, d)/dot(d, d)
        if not 0 <= t <= 1: continue
        r = add(a, mul(t, d)); n, m = (normals[i] for i in inc)
        A, B, C = dot(n, n), dot(n, m), dot(m, m)
        den = A*C-B*B
        if den <= 0: raise ValueError('Nonmaximal or degenerate adjacent facets')
        alpha = (C*dot(n, r)-B*dot(m, r))/den
        beta = (A*dot(m, r)-B*dot(n, r))/den
        if alpha < 0 or beta < 0: continue
        if 0 < t < 1 and alpha > 0 and beta > 0: H.append(edge)
        else: wH.append(edge)
    de = sorted(set(tuple(sorted(v)) for v in ef.values()))
    P, Q = bars(z, sorted(ef)), bars(poles, de)
    strict = [len(S), len(U), len(H)]; weak = [len(wS), len(wU), len(wH)]
    if weak == [0, 0, 0]:
        if strict[0]+strict[1]-strict[2] != 2: raise ValueError('Equilibrium Euler check failed')
        if len(P) != len(U)-1 or len(Q) != len(S)-1: raise ValueError('Root/bar count check failed')
    return dict(V=len(p), E=len(ef), F=len(faces), volume=V, first_moments=M, centroid=g,
                facets=faces, edges=sorted(ef), dual_edges=de, poles=poles,
                strict=strict, weak=weak, S=S, U=U, H=H,
                weak_S=wS, weak_U=wU, weak_H=wH, P=P, Q=Q)

def star_direction(p, faces, i, axis):
    pieces = []
    for f in faces:
        if i not in f: continue
        k = f.index(i); a, b = p[f[(k+1)%3]], p[f[(k+2)%3]]
        pieces.append((a, b, cross(a, b)))
    A = vsum(c for a, b, c in pieces)
    t = cross(A, AXES[axis]); scale = max(map(abs, t))
    if scale == 0: return None
    t = mul(1/scale, t)
    if dot(A, t) != 0: raise AssertionError('Not a volume-tangent direction')
    column = add(mul(dot(p[i], A), t),
                 vsum(mul(dot(c, t), add(a, b)) for a, b, c in pieces))
    return t, mul(R(1, 24), column)

def compatible(description, edges):
    vertices = sorted(set(i for i, axis in description))
    return all(tuple(sorted((i, j))) not in edges for i, j in itertools.combinations(vertices, 2))

def choose_frame(p, faces, g, junior_pole, root):
    edges = edges_of(faces)
    order = sorted(range(len(p)), key=lambda i: (i == root, dot(sub(p[i], g), junior_pole), i))
    pool = []
    for i in order:
        for axis in range(3):
            item = star_direction(p, faces, i, axis)
            if item is not None: pool.append(((i, axis), item[1]))
    for entries in itertools.combinations(pool, 3):
        description = tuple(v[0] for v in entries)
        if not compatible(description, edges): continue
        cols = [v[1] for v in entries]
        if det(*cols) != 0: return description
    raise ValueError('No full-rank independent-star frame found; not a family exclusion')

def solve_columns(cols, b):
    d = det(*cols)
    if d == 0: raise ValueError('Chosen moment frame became singular')
    return (det(b, cols[1], cols[2])/d,
            det(cols[0], b, cols[2])/d,
            det(cols[0], cols[1], b)/d)

def apply_controls(p, description, directions, s):
    q = list(p)
    for (i, axis), t, value in zip(description, directions, s): q[i] = add(q[i], mul(value, t))
    return q

def compensate(baseline, faces, description, target):
    if not compatible(description, edges_of(faces)): raise ValueError('Overlapping controller stars')
    items = [star_direction(baseline, faces, i, axis) for i, axis in description]
    if any(v is None for v in items): raise ValueError('Degenerate tangent direction')
    directions, cols = [v[0] for v in items], [v[1] for v in items]
    V, M = mass(baseline, faces)
    s = solve_columns(cols, sub(mul(V, target), M))
    q = apply_controls(baseline, description, directions, s)
    Vq, Mq = mass(q, faces)
    if Vq != V or Mq != mul(V, target): raise AssertionError('Finite moment identity failed')
    return q, directions, cols, s

def box_certificate(baseline, faces, description, directions, columns, s, target, root):
    bounds = tuple(2*abs(v)+R(1, 2**20) for v in s)
    corner_points = []; gaps = []; inside = []
    V, M = mass(baseline, faces)
    for signs in itertools.product((-1, 1), repeat=3):
        u = tuple(v*b for v, b in zip(signs, bounds))
        p = apply_controls(baseline, description, directions, u)
        gap = strict_fan(p, faces)
        if gap is None: return dict(certified=False, reason='A control-box corner leaves the hull chart')
        inner = min(-dot(cross(sub(p[f[1]], p[f[0]]), sub(p[f[2]], p[f[0]])),
                         sub(target, p[f[0]])) for f in faces)
        if inner <= 0: return dict(certified=False, reason='Target center outside a corner body')
        Vc, Mc = mass(p, faces)
        expected = add(M, vsum(mul(a, c) for a, c in zip(u, columns)))
        if Vc != V or Mc != expected: raise AssertionError('Corner moment identity failed')
        corner_points.append(p); gaps.append(gap); inside.append(inner)
    forest = [-1]*len(baseline); lower = [None]*len(baseline)
    for i in range(len(baseline)):
        if i == root: continue
        candidates = []
        for j in range(len(baseline)):
            if i == j: continue
            low = min(dot(sub(p[i], target), sub(p[j], p[i])) for p in corner_points)
            if low > 0: candidates.append((low, j))
        if not candidates: return dict(certified=False, reason='No common positive corner witness', vertex=i)
        lower[i], forest[i] = max(candidates)
    for i in range(len(baseline)):
        seen = set()
        while i != root:
            if i in seen or i < 0: raise AssertionError('Witness graph is not rooted')
            seen.add(i); i = forest[i]
    return dict(certified=True, target_center=target, root=root, halfwidths=bounds,
                chosen_parameters=s, forest=forest, corner_chord_lower_bounds=lower,
                corner_convexity_slacks=gaps, corner_interiority_slacks=inside)

def normalized_field(v):
    s = max(abs(a) for p in v for a in p)
    return v if s == 0 else [mul(1/s, p) for p in v]

def basin_fields(p, faces, report):
    bar = report['Q'][0]; poles = report['poles']; comp = {bar['root']}; todo = list(comp)
    while todo:
        a = todo.pop()
        for u, v in report['dual_edges']:
            if a not in (u, v) or segment_level(poles[u], poles[v]) <= bar['death2']: continue
            b = v if a == u else u
            if b not in comp: comp.add(b); todo.append(b)
    ef = edges_of(faces)
    death_edge = next(e for e, inc in ef.items() if set(inc) == set(bar['edge']))
    distance = {i: 0 for i in death_edge}
    for depth in (1, 2):
        for a, b in sorted(ef):
            if distance.get(a) == depth-1 and b not in distance: distance[b] = depth
            if distance.get(b) == depth-1 and a not in distance: distance[a] = depth
    incident = [[f for f, cycle in enumerate(faces) if i in cycle] for i in range(len(p))]
    selected = [[f for f in row if f in comp] for row in incident]
    out = [mul(R(1, len(row)), vsum(poles[f] for f in row)) if row else Z for row in selected]
    g = report['centroid']
    neck = [mul(-R(1, 2**distance[i]), sub(v, g)) if i in distance else Z for i, v in enumerate(p)]
    elder = max(range(len(poles)), key=lambda i: (dot(poles[i], poles[i]), -i))
    axis = cross(poles[bar['root']], poles[elder])
    if axis == Z: axis = next(cross(poles[bar['root']], a) for a in AXES if cross(poles[bar['root']], a) != Z)
    axis = mul(1/max(map(abs, axis)), axis)
    rotation = [mul(R(len(selected[i]), len(incident[i])), cross(axis, sub(v, g))) for i, v in enumerate(p)]
    return normalized_field(out), normalized_field(neck), normalized_field(rotation), sorted(comp), death_edge

def literal_points(name, points):
    D = math.lcm(*(a.denominator for p in points for a in p))
    return dict(name=name, denominator=D, vertices=[[int(a*D) for a in p] for p in points])

def self_test():
    p = [Z, AXES[0], AXES[1], AXES[2]]
    faces = [(1, 2, 3), (0, 3, 2), (0, 1, 3), (0, 2, 1)]
    d = (R(1, 7), -R(2, 11), R(0)); q = list(p); q[3] = add(q[3], d)
    V, M = mass(p, faces); W, N = mass(q, faces)
    assert V == W == R(1, 6) and sub(N, M) == mul(R(1, 24), d)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('parent_capsule', type=Path)
    parser.add_argument('--out', type=Path, default=Path('sq74e_star_results'))
    parser.add_argument('--max-evals', type=int, default=24)
    args = parser.parse_args()
    if args.max_evals < 1: raise ValueError('max-evals must be positive')
    self_test(); args.out.mkdir(parents=True, exist_ok=True)
    p, authority = parent_points(args.parent_capsule)
    faces = hull(p); initial = audit(p, faces)
    if [initial[k] for k in ('V', 'E', 'F')] != [53, 153, 102]: raise ValueError('Parent geometry mismatch')
    if initial['strict'] != [2, 1, 1] or initial['weak'] != [0, 0, 0]: raise ValueError('Parent census mismatch')
    if initial['P'] or len(initial['Q']) != 1: raise ValueError('Parent bar mismatch')
    target = initial['centroid']; out, neck, rotation, component, death_edge = basin_fields(p, faces, initial)
    description = choose_frame(p, faces, target, initial['poles'][initial['Q'][0]['root']], initial['U'][0])
    manifest = {}; log = []; winner = None
    manifest['PARENT_AUDIT.json'] = write_json(args.out/'PARENT_AUDIT.json', initial)
    specifications = list(itertools.product((1, -1), (R(0), R(1), R(-1)), (R(0), R(1, 2), R(-1, 2))))
    amplitudes = (R(1, 64), R(1, 32), R(1, 16), R(1, 8), R(1, 4))
    trials = itertools.islice(itertools.product(amplitudes, specifications), args.max_evals)
    for number, (amplitude, (sign, lam, mu)) in enumerate(trials):
        entry = dict(trial=number, amplitude=amplitude, outward_sign=sign, neck_weight=lam, rotation_weight=mu)
        try:
            field = [add(mul(sign, a), add(mul(lam, b), mul(mu, c))) for a, b, c in zip(out, neck, rotation)]
            baseline = [add(a, mul(amplitude, d)) for a, d in zip(p, field)]
            q, directions, columns, s = compensate(baseline, faces, description, target)
            if q == p: raise ValueError('Correction returned the unchanged parent')
            report = audit(q, faces)
            if report['centroid'] != target: raise AssertionError('Not the actual target centroid')
            if report['E'] > 249: raise AssertionError('Edge budget exceeded')
            report['controller'] = dict(vertices_axes=description, directions=directions, moment_columns=columns,
                                        parameters=s, signed_baseline_mass=mass(baseline, faces))
            report['current_parent_Q_component'] = component
            report['current_parent_death_edge'] = death_edge
            report['trial_parameters'] = entry.copy()
            if report['strict'][1] == 1 and report['weak'][1] == 0:
                report['moving_star_box'] = box_certificate(baseline, faces, description, directions, columns,
                                                           s, target, report['U'][0])
            name = 'SQ74E_STAR_%03d' % number
            inp = literal_points(name, q)
            for suffix, data in (('_INPUT.json', inp), ('_AUDIT.json', report)):
                filename = name+suffix; manifest[filename] = write_json(args.out/filename, data)
            is_winner = (report['strict'] == [1, 1, 0] and report['weak'] == [0, 0, 0]
                         and not report['P'] and not report['Q'])
            entry.update(name=name, strict=report['strict'], weak=report['weak'],
                         P=[b['depth'] for b in report['P']], Q=[b['depth'] for b in report['Q']], winner=is_winner)
            if is_winner: winner = name
        except (ValueError, ZeroDivisionError) as exc:
            entry['chart_rejection'] = str(exc)
        log.append(entry)
        if winner is not None: break
    run = dict(authority=authority, method_source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
               controller_vertices_axes=description, target_centroid=target,
               parent_Q_component=component, parent_death_edge=death_edge,
               max_evals=args.max_evals, trials=log, winner=winner,
               scope='Finite exact probes in one inherited simplicial hull chart; not a family exclusion')
    manifest['RUN.json'] = write_json(args.out/'RUN.json', run)
    write_json(args.out/'MANIFEST.json', manifest)
    print('SQ74E_EXACT_OWN110_FOUND' if winner else 'SQ74E_STAR_CHART_SEARCH_FINISHED_NO_WINNER')
    print(json.dumps(dict(completed_trials=len(log), winner=winner, output_directory=str(args.out))))

if __name__ == '__main__': main()
```

## Most useful continuation

First execute the parent-specific frame selection and exact moving-star capacity test, without counting rank alone as success. A useful result is a nontrivial finite corrected PRUNE_BEST descendant with its actual center exactly retained and a certified U1-safe controller box. Then put this exact correction inside a whole-boundary stable-basin search, rebuilding the chart after genuine hull events. The important new resource is physical first-moment control using the already installed material while leaving all32 extra point slots available—not another reference-only bridge, and not an assumption that the old fixed-surface center cube protects a moving shape.
