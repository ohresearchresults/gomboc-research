# figure-0523

AI research report · 2026-09-23 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# SQ87 V3 — exact cone-replacement constructions, a mass-dependent exclusion neighborhood, and an execution boundary

## 1. Status

**No new own110 certificate was observed in this continuation.** The last fully audited entrances remain those of literal parent `figure-0520`, SHA256 `a66205abf64385b024077ab360078b9b0feca1bf7ecb127e841a02cde9bc5fe1`.

This handoff contains two new, completely specified rational construction recipes. They replace the entire degree20 normal polygon of `Q20_QREPAIR211_D100000` by an enclosing acute quadrilateral or triangle. The resulting uniformly filled bodies are proper subsets of that parent, have **true E≤152 and E≤150 respectively**, and retain p0 as a **strict unstable equilibrium at their actual centroids**, independently of the unknown centroid values. All20 old apex facets—including the unwanted stable quadrilateral—cease to be facets. These are finite changes of the retained material and critical cone, not another point in the closed SIMPLE150 insertion cell.

**Their complete equilibrium censuses, masses, maximal face counts and new landscapes have not been observed.** They are reconstructible candidates with proved geometric and partial mechanical properties, not accepted own110 bodies or fully audited nonwinners. The exact patch below performs those outstanding computations and preserves every positive bar.

The execution limitation is specific: the current container/Python calls returned no inspectable output to this executor, including elementary diagnostic calls. I therefore cannot distinguish an executed command from an unexecuted one by its result, and do not claim a new optimizer trajectory, audit completion, generated-file identity or terminal marker. The current513-line journal and its literal parent were read through EOF in the preceding supplied read sequence. No unavailable historical source was substituted.

## 2. Why change the entire apex cone?

The parent offers three different costs of releasing its existing contacts:

| Entrance | Audited V/E/F | Remaining Q feature | Maximal-facet representation | Generic bound after releasing contacts |
|---|---:|---|---:|---:|
| SIMPLE150_G5 |150/225/77|20/34, delta .196281852714…; both stable carriers avoid U|77 planes|E≤225; eight further planes fit F≤85|
| C438_REPAIR_G5 |129/203/76|19/28, delta .188444586555…; stable triangle contains U|76 planes|E≤222; nine further planes fit F≤85|
| Q20_QREPAIR_G5 |117/184/69|30/47, delta .428763360819…; stable quadrilateral contains U|69 planes|E≤201; sixteen further planes fit F≤85|

The last row's original91-row representation has22 inactive inequalities. They can be removed without changing the starting body, but that removal is only a parametrization change. It must not be reported as a geometric improvement. Conversely, retaining all91 rows while moving them freely does not justify a69-facet complexity bound.

For QREPAIR, replacing its entire20-facet apex cone changes substantially more than merely releasing its concurrence. It removes a critical stable carrier, sharpens the apex, and reduces the number of possible maximal facets from69 to at most53 or52. This gives a different mass geometry and a much larger subsequent support budget. It does **not** guarantee that the remaining29 members of the old Q packet disappear, that no new packet is born, or that p0 remains the essential P root.

## 3. Exact finite construction

### Parent and numbering

Use **exactly** `SQ87_Q20_QREPAIR211_D100000`, not its G6 freeze and not SIMPLE150 with the same insertion coordinate. Its input is2814 bytes with SHA256

`0d7f2bfe32bdea0e874238991381a5af2853e315ea12cefe92c594ca2aa9b0d0`.

The literal V2 capsule reconstructs this input. Its actual parent census is117/184/69, strict211/additionalweak000. Its degree20 vertex is

`p0 = (7/10, -1/2, 13/20)`.

Its stable quadrilateral is `[66,73,81,101]`, where vertex101 is p0. The other stable carrier is the disjoint13-gon reported in V2. The new construction does not retain the quadrilateral as a facet.

Reconstruct the69 maximal parent facets. In the original raw coordinate frame, write each as

`q_i · x ≤ 1`.

The raw origin is strictly interior, so this normalization is valid. This raw polar representation is used only for geometry. **Equilibrium landscapes below use the actual physical centroid, not this raw origin.**

Let I be the20 indices satisfying `q_i·p0=1`; all other49 maximal supports satisfy `q_i·p0<1`. Set

`q0 = p0/(p0·p0) = (56,-40,52)/93`,

`e1 = (5,7,0)`,

`e2 = (-91,65,148)`.

These vectors satisfy

`p0·e1=p0·e2=e1·e2=0`,

`p0·p0=93/80`, `e1·e1=74`, `e2·e2=34410`.

For each i in I define the exact rational coordinates

`a_i = (q_i-q0)·e1/74`,

`b_i = (q_i-q0)·e2/34410`.

Thus `q_i=q0+a_i e1+b_i e2`. Define

`A = max((101/100) max_i |a_i|, 1/8)`,

`B = max((101/100) max_i |b_i|, 1/128)`.

No floating rounding is used.

### ACUTE_RECT4

Replace all20 rows in I by the four rows

`q0 + s A e1 + t B e2`, for `(s,t)∈{−1,1}²`.

Keep the other49 maximal parent rows. The new body is the intersection of these53 rational halfspaces with right-hand side1.

### ACUTE_TRI3

Instead use the three rows

`q0−2A e1−B e2`,

`q0+2A e1−B e2`,

`q0+3B e2`.

Keep the same49 complementary maximal parent rows. This body is defined by52 rational halfspaces with right-hand side1.

### Exact geometry proved without a census

The original20 points lie strictly inside the coefficient rectangle `[-A,A]×[-B,B]`. That rectangle lies inside the coefficient triangle with vertices `(-2A,-B),(2A,-B),(0,3B)`. Consequently the new raw polar hull contains the old one, and each new physical body is contained in the old body. All defining vectors are finite; hence the raw origin remains strictly interior. Boundedness follows from containment in the bounded parent.

Every new row lies in `p0·q=1`; all49 complementary rows lie strictly below that plane. Therefore the new exposed polar face is exactly the prescribed quadrilateral or triangle. The physical point p0 has degree exactly4 or3, respectively.

Every removed q_i is a strictly positive convex combination of the new face's corners. Equality in its old support inequality now forces equality in every new apex inequality. Their common physical intersection is just p0. Thus **all20 old apex support planes now touch the body only at p0**. None remains a maximal facet. In particular, the old stable quadrilateral really is destroyed, rather than merely renamed.

For a convex three-polyhedron, `E=3F−6−D_V`, where `D_V=Σ_v(deg(v)−3)`. Therefore

`ACUTE_RECT4: F≤53, D_V≥1, E≤152`,

`ACUTE_TRI3: F≤52, D_V≥0, E≤150`.

These are bounds on true edges of the maximal complex, not on triangulation edges. Actual V/E/F remain to be computed. Since both edge bounds are below the parent's184, neither body is affinely equivalent to the parent.

## 4. A strict unstable apex independent of actual-mass displacement

This is a partial mechanical guarantee, not U1.

The thresholds in A and B imply

`A²·74 > 80/93` and `B²·34410 > 80/93`.

Consider a vector `d=p0−x`, where x belongs to the rectangular-cone body. In orthonormal coordinates along p0,e1,e2, write d as `(t,u,v)`. The four apex inequalities give

`t/|p0| ≥ A|e1| |u| + B|e2| |v|`.

It follows that `t≥|u|+|v|`, with a strict inequality for every interior point x. The scalar product of a strict interior vector of this cone with any nonzero vector of its closure is positive.

The actual filled centroid g is interior. For any true neighbor w of p0,

`(p0−g)·(w−p0) < 0`.

Hence p0 is strict U at the actual uniform centroid. The triangular normal face contains the rectangle, so its physical tangent cone is a subset of the same acute cone and the conclusion also holds there.

More generally, this strict-U conclusion survives arbitrary changes elsewhere that keep a full-dimensional convex body inside this acute apex cone and retain p0. It does not require g to remain close to the old centroid. It does not assert that p0 is the only unstable equilibrium or the globally farthest vertex.

This separates one own-mass difficulty from the remaining problem: p0 cannot be lost as a strict U merely because the mass moves. All other physical roots and every polar root still have to be dealt with.

## 5. An explicit actual-mass exclusion neighborhood

The following calculation instantiates the existing bar-continuity principle with a uniform-volume centroid displacement bound. It is not an exclusion of the new cone-replacement family as a whole.

Let K have actual centroid0, inradius r and circumradius R. Suppose a uniformly filled convex body L satisfies raw Hausdorff distance

`d_H(K,L) ≤ epsilon r`, with `0≤epsilon<1`.

Then

`(1−epsilon)K ⊆ L ⊆ (1+epsilon)K`.

For any unit direction u, the positive and negative first moments of K in that direction are equal. Moreover

`∫_K (u·x)_+ dx ≤ (1/2)∫_K |x| dx ≤ (3/8) R Vol(K)`.

Using radial integration, expansion by a factor s scales first moment by s⁴. Consequently the actual centroid of L satisfies

`|g_L| ≤ 3R epsilon(1+epsilon²)/(1−epsilon)³`.

Thus, putting

`eta = epsilon + 3(R/r) epsilon(1+epsilon²)/(1−epsilon)³`,

we have

`d_H(K,L−g_L) ≤ eta r`.

For a parent polar positive bar with squared-radius birth b and death d, the bar cannot disappear whenever

`d/b < ((1−eta)/(1+eta))²`.

An elementary component proof avoids assuming continuation of an old vertex label. The two parent components remain represented above the lower new peak level `b/(1+eta)²`. A path joining them above `d/(1−eta)²` would induce a parent path above d, contradicting the old death level. A positive gap therefore leaves at least two radial maxima of the new polar, hence at least two strict stable facets of the new physical polyhedron.

For QREPAIR_G5, the parent certifies `r/R>2/7` and `delta=(b−d)/b≥428763360819/10^12`. At `epsilon=1/100`,

`eta ≤ 1/100 + 210021/1940598 < 1/8`,

and

`428763360819/10^12 > 32/81 = 1−(7/9)²`.

Therefore **every uniformly filled convex polyhedron within raw Hausdorff distance r/100 of QREPAIR_G5 has at least two strict S at its own actual centroid**, regardless of changes in vertices, facets, topology or edge count.

For comparison, the certified SIMPLE150 and REPAIR Q depths imply the analogous exclusion in the closed **own-centered** Hausdorff balls of radii r/20. Both satisfy `delta>80/441=1−(19/21)²`. QREPAIR has an own-centered exclusion radius r/8. The raw r/100 conclusion includes the uniform-mass displacement estimate; it does not hold by treating the center as an independently selected parameter.

These are local exclusions only. The patch computes exact raw Hausdorff distances for the two new inner bodies and records whether this particular exclusion applies. No distance result is claimed before that computation is observed.

## 6. Complete exact recovery and verification patch

The patch depends only on the **unchanged, fully literal35-unit V2 capsule already supplied in this chat**. It does not depend on an old sandbox archive, a new optimizer checkpoint, or the original canonical materials. The V2 decoder and `run_exact.py` recover the exact parent input and its auditors.

Commands:

```
python -B -S RECOVER_SQ87_V2.py V2_SOURCE
python -B -S V2_SOURCE/run_exact.py V2_PROOF
python -B -S SQ87_V3_CONE.py V2_SOURCE V2_PROOF V3_PROOF
```

The first two commands may be omitted when those exact recovered directories already exist. The third command accepts either the V2 proof directory or the exact parent input file as its second argument. It locates the input by its complete SHA256, not by an approximate class or filename alias.

Environment: CPython3.13.5, standard library, assertions enabled. No NumPy, SciPy, Torch or floating optimization is needed. All new nondefault construction parameters are literal in the source: p0, e1, e2, padding101/100, thresholds1/8 and1/128, and the two corner lists.

**Execution status:** the following source has not had an observable cold replay in this executor. Its markers are expected markers, not observed ones. In particular, no new numerical S/U/H, volume, centroid, bar count, byte count or output SHA256 is asserted here. The program writes all of them, including a source receipt, into its manifest. The literal source and exact parent identity—not an unobserved hash—are the recovery authority.

```python
"""SQ87 V3: exact finite replacement of QREPAIR's entire apex cone.
Usage: python -B -S SQ87_V3_CONE.py V2_SOURCE PARENT_INPUT_OR_PROOF_DIR NEW_OUT
Dependency: the complete literal SQ87 V2 35-unit capsule in the supplied parent.
Exact arithmetic only. This source was not cold-replayed observably in V3.
"""
import hashlib
import importlib
import json
import math
import sys
from collections import deque
from fractions import Fraction as F
from itertools import combinations, product
from pathlib import Path

assert __debug__ and len(sys.argv) == 4
sys.set_int_max_str_digits(0)
SRC = Path(sys.argv[1]).resolve()
PIN = Path(sys.argv[2]).resolve()
OUT = Path(sys.argv[3]).resolve()
assert not OUT.exists(), 'NEW_OUT must not exist'
PARENT_SHA = '0d7f2bfe32bdea0e874238991381a5af2853e315ea12cefe92c594ca2aa9b0d0'
sha = lambda b: hashlib.sha256(b).hexdigest()
enc = lambda x: json.dumps(x, sort_keys=True, separators=(',', ':')).encode()

manifest = json.loads((SRC / 'MANIFEST.json').read_text())
assert len(manifest) == 34
for name, rec in manifest.items():
    data = (SRC / name).read_bytes()
    assert len(data) == rec['bytes'] and sha(data) == rec['sha256'], name

for directory in sorted({str(p.parent) for p in SRC.rglob('*.py')}):
    sys.path.insert(0, directory)
mods = []
for name in ['check_A', 'check_B']:
    matches = list(SRC.rglob(name + '.py'))
    assert len(matches) == 1, ('Missing or ambiguous parent source', name)
    mod = importlib.import_module(name)
    assert Path(mod.__file__).resolve() == matches[0].resolve()
    mods.append(mod)
check_A, check_B = mods

paths = [PIN] if PIN.is_file() else sorted(PIN.rglob('*.json'))
hits = [p for p in paths if sha(p.read_bytes()) == PARENT_SHA]
assert hits, 'Exact Q20_QREPAIR211_D100000 input was not found'
parent_bytes = hits[0].read_bytes()
assert len(parent_bytes) == 2814
parent_raw = json.loads(parent_bytes)


def dot(a, b):
    return sum(x*y for x, y in zip(a, b))


def add(a, b):
    return tuple(x+y for x, y in zip(a, b))


def sub(a, b):
    return tuple(x-y for x, y in zip(a, b))


def mul(t, a):
    return tuple(t*x for x in a)


def cross(a, b):
    return (a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2],
            a[0]*b[1]-a[1]*b[0])


def primitive(values):
    values = list(map(F, values))
    D = math.lcm(*(x.denominator for x in values))
    row = [int(D*x) for x in values]
    g = math.gcd(*row)
    assert g > 0
    return [x//g for x in row]


def geometry(report):
    V = [tuple(map(F, v)) for v in report['raw_vertices']]
    g = tuple(map(F, report['raw_centroid']))
    faces = report['faces']
    Q = []
    owners = {}
    for f, cycle in enumerate(faces):
        a = V[cycle[0]]
        n = None
        for j in range(1, len(cycle)-1):
            candidate = cross(sub(V[cycle[j]], a), sub(V[cycle[j+1]], a))
            if candidate != (0, 0, 0):
                n = candidate
                break
        assert n is not None
        h = dot(n, a)
        if dot(n, g) > h:
            n, h = mul(-1, n), -h
        assert h > 0 and dot(n, g) < h
        q = mul(1/h, n)
        assert all(dot(q, v) <= 1 for v in V)
        assert all(dot(q, V[i]) == 1 for i in cycle)
        Q.append(q)
        for i, j in zip(cycle, cycle[1:]+cycle[:1]):
            owners.setdefault(tuple(sorted((i, j))), []).append(f)
    assert all(len(fs) == 2 for fs in owners.values())
    E = sorted(owners)
    assert len(V)-len(E)+len(faces) == 2
    assert [len(V), len(E), len(faces)] == [report[k] for k in ['V','E','F']]
    return V, g, Q, E, owners


def both(raw):
    a = check_A.run(raw)
    b = check_B.run(raw)
    assert enc(a) == enc(b)
    return a, b


def independent_mass(report):
    V, g, Q, E, owners = geometry(report)
    o = tuple(sum(v[k] for v in V)/len(V) for k in range(3))
    volume = F(0)
    moment = [F(0), F(0), F(0)]
    for cycle in report['faces']:
        a = V[cycle[0]]
        for j in range(1, len(cycle)-1):
            b, c = V[cycle[j]], V[cycle[j+1]]
            six = abs(dot(sub(a,o), cross(sub(b,o), sub(c,o))))
            assert six > 0
            vol = six/6
            volume += vol
            for k in range(3):
                moment[k] += vol*(o[k]+a[k]+b[k]+c[k])/4
    assert volume == F(report['ordinary_volume'])
    assert tuple(x/volume for x in moment) == g
    centered = [sub(v,g) for v in V]
    D = math.lcm(*(x.denominator for v in centered for x in v))
    r2 = min((1-dot(q,g))**2/dot(q,q) for q in Q)
    R2 = max(dot(v,v) for v in centered)
    return {'volume':str(volume), 'moment':list(map(str,moment)),
            'centroid':list(map(str,g)), 'reference':list(map(str,o)),
            'centered_denominator':str(D), 'denominator_bits':D.bit_length(),
            'r2':str(r2), 'R2':str(R2)}


def chord(a, b):
    A, B, C = dot(a,a), dot(a,b), dot(b,b)
    if B >= A:
        return A
    if B >= C:
        return C
    D = A+C-2*B
    assert D > 0
    return (A*C-B*B)/D


def landscape(V, E):
    """Exact simultaneous upper filtration; all positive bars, no cutoff."""
    n = len(V)
    E = sorted(set(tuple(sorted(e)) for e in E))
    birth = [dot(v,v) for v in V]
    W = {e:chord(V[e[0]],V[e[1]]) for e in E}
    adj = [[] for _ in V]
    events = {}
    for i, level in enumerate(birth):
        events.setdefault(level, [[],[]])[0].append(i)
    for e, level in W.items():
        assert level <= min(birth[e[0]],birth[e[1]])
        events.setdefault(level, [[],[]])[1].append(e)
        adj[e[0]].append(e[1]); adj[e[1]].append(e[0])
    for a in adj:
        a.sort()

    def find(parent, x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    # A maximum spanning tree verifies domination of EVERY complete chord.
    ds = list(range(n)); tree = [[] for _ in V]; tree_rows = []
    for e in sorted(E, key=lambda e:(-W[e],e)):
        a,b = (find(ds,x) for x in e)
        if a != b:
            ds[b] = a
            i,j = e
            tree[i].append((j,W[e])); tree[j].append((i,W[e]))
            tree_rows.append([i,j,str(W[e])])
    assert len(tree_rows) == n-1
    checks = 0
    for i in range(n):
        cap = {i:max(birth)+1}; queue = deque([i])
        while queue:
            u = queue.popleft()
            for v,w in tree[u]:
                if v not in cap:
                    cap[v] = min(cap[u],w); queue.append(v)
        assert len(cap) == n
        for j in range(i+1,n):
            assert chord(V[i],V[j]) <= cap[j]
            checks += 1

    parent = list(range(n)); members = {i:{i} for i in range(n)}
    active = set(); bars = []
    for level in sorted(events, reverse=True):
        born, edges = events[level]
        active.update(born)
        nodes = {find(parent,i) for i in born}
        pairs = []
        for i,j in edges:
            assert i in active and j in active
            a,b = find(parent,i),find(parent,j)
            nodes.update((a,b)); pairs.append((a,b))
        temporary = {x:x for x in nodes}
        for a,b in pairs:
            a,b = find(temporary,a),find(temporary,b)
            temporary[b] = a
        groups = {}
        for x in nodes:
            groups.setdefault(find(temporary,x),[]).append(x)
        for roots in sorted(groups.values(), key=lambda x:min(x)):
            roots.sort()
            elder = min(roots, key=lambda x:(-birth[x],x))
            for peak in roots:
                if peak == elder or birth[peak] <= level:
                    continue
                component = set(members[peak])
                cut = []
                for i,j in E:
                    if (i in component) != (j in component):
                        if j in component:
                            i,j = j,i
                        cut.append([i,j])
                cut.sort()
                assert cut and max(W[tuple(sorted(e))] for e in cut) == level
                pred = {peak:None}; queue = deque([peak])
                while queue and elder not in pred:
                    u = queue.popleft()
                    for v in adj[u]:
                        if v not in pred and W[tuple(sorted((u,v)))] >= level:
                            pred[v] = u; queue.append(v)
                assert elder in pred
                path = []; u = elder
                while u is not None:
                    path.append(u); u = pred[u]
                path.reverse()
                assert min(W[tuple(sorted(e))] for e in zip(path,path[1:])) == level
                bars.append({'peak':peak,'elder':elder,'birth':str(birth[peak]),
                             'death':str(level),'delta':str(1-level/birth[peak]),
                             'component':sorted(component),'cut':cut,'path':path})
            for root in roots:
                if root != elder:
                    parent[root] = elder
                    members[elder].update(members.pop(root))
    essential = find(parent,0)
    assert all(find(parent,i) == essential for i in range(n))
    forest, strict_roots, closed_weak_roots = [],[],[]
    for i in range(n):
        candidates = [(dot(V[i],sub(V[j],V[i])),j) for j in adj[i]]
        value,j = max(candidates, key=lambda x:(x[0],-x[1]))
        if value > 0:
            forest.append([i,j,str(value)])
        elif value < 0:
            strict_roots.append(i)
        else:
            closed_weak_roots.append(i)
    return {'vertices':[list(map(str,v)) for v in V],
            'births':list(map(str,birth)),
            'edges':[[i,j,str(W[i,j])] for i,j in E],
            'bars':bars,'essential_root':essential,
            'positive_forest':forest,'strict_roots':strict_roots,
            'closed_weak_roots':closed_weak_roots,
            'maximum_spanning_tree':tree_rows,'allpair_checks':checks,
            'levels':'actual unscaled squared Euclidean radii'}


def full_pq(report):
    V,g,Q,E,owners = geometry(report)
    P = [sub(v,g) for v in V]
    polar = [mul(1/(1-dot(q,g)),q) for q in Q]
    dual_edges = sorted({tuple(sorted(fs)) for fs in owners.values()})
    p,q = landscape(P,E),landscape(polar,dual_edges)
    if report['weak'] == [0,0,0]:
        assert len(p['bars']) == report['counts'][1]-1
        assert len(q['bars']) == report['counts'][0]-1
    return {'P':p,'Q':q,
            'edge_facet_owners':[[i,j,owners[i,j]] for i,j in E],
            'physical_face_cycles':report['faces'],
            'physical_centroid':list(map(str,g))}


def distance2(point, V, Q, E):
    if all(dot(q,point) <= 1 for q in Q):
        return F(0)
    best = min(dot(sub(point,v),sub(point,v)) for v in V)
    for i,j in E:
        d = sub(V[j],V[i]); dd = dot(d,d)
        t = min(F(1),max(F(0),dot(sub(point,V[i]),d)/dd))
        w = add(V[i],mul(t,d))
        best = min(best,dot(sub(point,w),sub(point,w)))
    for q in Q:
        w = add(point,mul((1-dot(q,point))/dot(q,q),q))
        if all(dot(a,w) <= 1 for a in Q):
            best = min(best,dot(sub(point,w),sub(point,w)))
    return best


OUT.mkdir(parents=True)
receipts = {}
def save(name,obj):
    b = enc(obj); (OUT/name).write_bytes(b)
    receipts[name] = {'bytes':len(b),'sha256':sha(b)}

# Independent exact controls inherited from the documented parent interfaces.
controls = [
    ([[-1,-1,-1,1],[-1,1,1,1],[1,-1,1,1],[1,1,-1,1]],[4,4,6],[0,0,0]),
    ([[1,0,0,1],[-2,3,0,1],[1,-3,0,1],[0,0,1,1],[0,0,-1,1]],
     [4,4,6],[1,2,3])
]
for H,c,w in controls:
    aa,bb = both({'H':H})
    assert aa['counts'] == c and aa['weak'] == w

old,old_b = both(parent_raw)
assert [old[k] for k in ['V','E','F']] == [117,184,69]
assert old['counts'] == [2,1,1] and old['weak'] == [0,0,0]
V,g,Q,E,owners = geometry(old)
p0 = (F(7,10),F(-1,2),F(13,20))
u0 = V.index(p0)
assert u0 in old['unstable_vertices']
I = [i for i,q in enumerate(Q) if dot(q,p0) == 1]
J = [i for i,q in enumerate(Q) if dot(q,p0) < 1]
assert len(I) == 20 and len(J) == 49
old_mass = independent_mass(old)
r2,R2 = F(old_mass['r2']),F(old_mass['R2'])
assert 49*r2 > 4*R2
old_pq = full_pq(old)
assert len(old_pq['P']['bars']) == 0 and len(old_pq['Q']['bars']) == 1
old_delta = F(old_pq['Q']['bars'][0]['delta'])
assert F(428763360819,10**12) <= old_delta < F(428763360820,10**12)

q0 = mul(1/dot(p0,p0),p0)
e1,e2 = (F(5),F(7),F(0)),(F(-91),F(65),F(148))
assert dot(p0,e1) == dot(p0,e2) == dot(e1,e2) == 0
ab = []
for i in I:
    a = dot(sub(Q[i],q0),e1)/dot(e1,e1)
    b = dot(sub(Q[i],q0),e2)/dot(e2,e2)
    assert add(q0,add(mul(a,e1),mul(b,e2))) == Q[i]
    ab.append((i,a,b))
A = max(F(101,100)*max(abs(a) for i,a,b in ab),F(1,8))
B = max(F(101,100)*max(abs(b) for i,a,b in ab),F(1,128))
assert A*A*dot(e1,e1) > 1/dot(p0,p0)
assert B*B*dot(e2,e2) > 1/dot(p0,p0)
assert all(abs(a) < A and abs(b) < B for i,a,b in ab)

summary = {}
for name,corners in [
    ('SQ87_V3_ACUTE_RECT4',[(s*A,t*B) for s,t in product([-1,1],repeat=2)]),
    ('SQ87_V3_ACUTE_TRI3',[(-2*A,-B),(2*A,-B),(F(0),3*B)])
]:
    newq = [add(q0,add(mul(a,e1),mul(b,e2))) for a,b in corners]
    assert all(dot(q,p0) == 1 for q in newq)
    identities = []
    for i,a,b in ab:
        if len(corners) == 4:
            weights = [(1+s*a/A)*(1+t*b/B)/4
                       for s,t in product([-1,1],repeat=2)]
        else:
            top = (1+b/B)/4
            weights = [(1-top-a/(2*A))/2,(1-top+a/(2*A))/2,top]
        assert all(w > 0 for w in weights) and sum(weights) == 1
        assert tuple(sum(w*q[k] for w,q in zip(weights,newq)) for k in range(3)) == Q[i]
        identities.append({'old_facet':i,'weights':list(map(str,weights))})
    qrows = [Q[i] for i in J]+newq
    raw = {'H':[primitive(list(q)+[F(1)]) for q in qrows]}
    a,b = both(raw)
    vv,gg,qq,ee,oo = geometry(a)
    uu = vv.index(p0)
    degree = sum(uu in edge for edge in ee)
    m = len(newq)
    assert degree == m and a['F'] <= 49+m and a['E'] <= 144+2*m
    assert uu in a['unstable_vertices']
    assert F(a['ordinary_volume']) < F(old['ordinary_volume'])
    assert all(all(dot(q,v) <= 1 for q in Q) for v in vv)
    for i in I:
        assert [j for j,v in enumerate(vv) if dot(Q[i],v) == 1] == [uu]
    mass = independent_mass(a)
    pq = full_pq(a)
    material = []
    for i,v in enumerate(V):
        feasible = all(dot(q,v) <= 1 for q in qq)
        assert feasible == (v in vv)
        material.append({'old_vertex':i,'retained':feasible,
                         'new_vertex':vv.index(v) if feasible else None})
    distances = [distance2(v,vv,qq,ee) for v in V]
    hausdorff2 = max(distances)
    in_exclusion_ball = 10000*hausdorff2 <= r2
    if in_exclusion_ball:
        assert a['counts'][0] >= 2
    structure = {
        'parent_input_sha256':PARENT_SHA,'p0':list(map(str,p0)),
        'old_apex_facets':I,'kept_parent_facets':J,
        'A':str(A),'B':str(B),'e1':list(map(str,e1)),
        'e2':list(map(str,e2)),'q0':list(map(str,q0)),
        'new_apex_normals':[list(map(str,q)) for q in newq],
        'strict_convex_identities':identities,'apex_vertex':uu,
        'apex_degree':degree,'material_map':material,
        'directed_old_vertex_distance2':list(map(str,distances)),
        'raw_hausdorff2':str(hausdorff2),
        'within_raw_r_over_100_exclusion':in_exclusion_ball,
        'strict_counts':a['counts'],'additionalweak':a['weak'],
        'closed_counts':[x+y for x,y in zip(a['counts'],a['weak'])]
    }
    for suffix,obj in [('INPUT',raw),('A',a),('B',b),('MASS',mass),
                       ('PQ',pq),('STRUCTURE',structure)]:
        save(name+'_'+suffix+'.json',obj)
    summary[name] = {'V':a['V'],'E':a['E'],'F':a['F'],
                     'strict':a['counts'],'additionalweak':a['weak'],
                     'Pbars':len(pq['P']['bars']),'Qbars':len(pq['Q']['bars']),
                     'raw_hausdorff2':str(hausdorff2)}
    if a['counts'] == [1,1,0] and a['weak'] == [0,0,0] and a['E'] <= 249:
        print('SQ87_V3_EXACT_TARGET_FOUND',name)
    print('SQ87_V3_ONE_FINITE_CONE_AUDIT_PASS',name,summary[name],flush=True)

# Exact scalar checks for the derived mass-continuity certificates.
epsilon = F(1,100)
eta = epsilon+3*F(7,2)*epsilon*(1+epsilon*epsilon)/(1-epsilon)**3
assert eta < F(1,8)
assert F(428763360819,10**12) > F(32,81)
assert F(196281852714,10**12) > F(80,441)
assert F(188444586555,10**12) > F(80,441)
save('MASS_CONTINUITY.json',{'epsilon':str(epsilon),'eta_upper':str(eta),
                            'eta_comparison':str(F(1,8)),
                            'parent_r2':str(r2),'parent_R2':str(R2),
                            'parent_Q_delta':str(old_delta)})
save('SUMMARY.json',summary)
source = Path(__file__).read_bytes()
(OUT/'SQ87_V3_CONE.py').write_bytes(source)
receipts['SQ87_V3_CONE.py'] = {'bytes':len(source),'sha256':sha(source)}
(OUT/'MANIFEST.json').write_bytes(enc(receipts))
print('SQ87_V3_EXACT_FINITE_CONE_REPLACEMENT_PASS',2)
print('SQ87_V3_RAW_MASS_CONTINUITY_SCALAR_CHECKS_PASS')
print(json.dumps(receipts,sort_keys=True))
```

The landscape routine constructs the true edge graph from maximal face cycles, batches simultaneous levels, preserves every positive bar, and records each complete component, full boundary cut and attaining path. It also verifies every complete chord against a maximum-spanning-tree bottleneck of the true graph. Its values are **unscaled actual squared radii**, explicitly distinguished from the parent's scaled representation. Both new physical and polar geometries use the new actual filled centroid.

The independently calculated mass uses a tetrahedral fan from the average of the exact extreme vertices only as an interior integration point. That average is not used as the center of gravity. The integral is checked against the filled volume and centroid returned by both parent auditors.

## 7. What is established, and what remains open

Established analytically: the two rational recipes define bounded full-dimensional proper subsets of exact QREPAIR_G5; they destroy all20 old apex facets; p0 has degree4 or3; true E is at most152 or150; and p0 is strict U at the actual centroid. Also established is the stated raw r/100 actual-mass exclusion neighborhood and the two shallower entrances' own-centered r/20 exclusions.

Not established in this execution: actual maximal V/E/F for the two children, complete strict/additionalweak counts, their exact evaluated mass fractions, the number or depths of their new positive bars, their measured Hausdorff motion, any improvement in the final basin, or an optimizer result. The patch supplies those calculations but its expected completion markers are not evidence that they occurred.

The useful next finite chart is not restricted to the original one-point cell. The triangular child has at most52 listed supports and can accommodate **33 further supports** under the sufficient F≤85/E≤249 bound; the quadrilateral child can accommodate32. Keeping the new acute apex inequalities and requiring other supports to contain p0 preserves the proved strict-U apex property while the remaining material and actual mass change. This leaves substantial freedom to rebuild the complete physical and polar escape landscapes. It does not ensure U1, S1 or preservation of the old elder.

The last-bar question is still unresolved. A destroyed old stable quadrilateral is not a canceled Q landscape. The next accepted endpoint must be decided by the full outputs of the patch—or an equally complete exact audit—not by the cone geometry, edge bound or retained-apex proof alone.
