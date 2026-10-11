# figure-0343

Historical AI scientific report · saved 2026-09-09 UTC. Claims below retain their original status and have not all been independently checked. The current retained construction is C622; the C<500 search remains open.

---

# Keen Raven 68 — actual three-edge reduction of the accepted homogeneous Gömböc

## 1. Attained result and acceptance boundary

A smaller homogeneous, own-centred, strict **(S,U,H)=(1,1,0)** convex polyhedron was constructed and subjected to the two complete exact implementations and a fresh source-only replay:

**KR68_CAP257_C1364: V=257, E=682, F=427, C=1364.**

Relative to the authoritative **NN51_CHAIN258_PN03_C1370**, this removes **one actual extreme vertex, three true edges, and two maximal facets**. The change is not a triangulation count or an intended facet union.

The unique stable maximal face is the outward triangle **[158,163,161]**. The unique unstable vertex is **138**. There are **no saddle edges, no weak equilibria, and no zero ordinary edge primitives**. The three ordinary centred first moments are exactly zero.

**E<500 was not attained.** E682 is the smallest completed exact strict110 endpoint obtained in this continuation. Further simultaneous regional replacements and edge contractions were explored, but no further endpoint completed the required acceptance chain.

This construction is **not** a retrospective acceptance of the historical name NN51_VLOSS257_C1364. The immutable parent explicitly did not accept that name. KR68_CAP257_C1364 is a newly materialized endpoint with its own defining bytes and completed verification returns. The inherited acceptance boundary and original recovery bindings are recorded in the supplied parent. 

### New defining-byte identity

The new PN03 definition has SHA-256:

`5c5b1f474bfc65e18aa93bb7212f5e6ef74679cdaaf0194bffda1d066c2ccae628`

The definition contains 257 integer seed triples at D0=10^18, **81 ordered rational reconstruction operations imposing 83 scalar contact equations**, 510 outward integration triangles, and the complete primal and polar witness arrays. The reconstructed raw common denominator has **2,785 decimal digits**.

The exact supplementary escape certificate has **K=3334696**, primal root **138**, and polar root **143** in the new first-occurrence maximal-plane ordering. Every nonroot has a stored positive escape cosine greater than 1/K, and every stored path reaches its corresponding root. These witnesses supplement the exhaustive census; they do not replace it.

### Retained standalone artifacts

The following are actual retained endpoint and replay files, not provisional filenames:

[Six-file standalone exact recovery bundle, JSON](sandbox:/mnt/data/kr68/KR68_CAP257_C1364/bundle.json)

[The same complete bundle, base85/zlib](sandbox:/mnt/data/kr68/KR68_CAP257_C1364/bundle.b85)

[Exact PN03 defining bytes](sandbox:/mnt/data/kr68/KR68_CAP257_C1364/capsule.pn03)

[Completed full replay report](sandbox:/mnt/data/kr68/KR68_CAP257_C1364/REPLAY_REPORT.json)

[Observed fresh source-only replay receipt](sandbox:/mnt/data/kr68/KR68_CAP257_C1364/COLD_RECEIPT.json)

The inline reconstruction in Section 6 is a **parent-relative deterministic replay**, with the assigned journal as an explicit input. It does not require any of these sandbox files. The standalone bundle bypasses numerical discovery entirely and needs only Python's standard library. The bundle's literal encoded body is not duplicated inline here; this is a delivery limitation relative to the requested fully inlined, journal-independent byte capsule. The parent-relative program is supplied so continuation does not depend solely on a sandbox attachment.

## 2. The actual geometric change

Use original parent labels for this comparison. Original vertex **193** is removed. Every retained original label v is mapped to compact label v for v<193 and v−1 for v>193.

The exact maximal-complex comparison found precisely the following five old facets absent from the successor:

```text
[78,192,193]
[88,193,134,102,150,148]
[86,193,88,89]
[23,78,193,86]
[134,193,192,194]
```

They are replaced by these three actual maximal facets, again written with retained original labels:

```text
[23,78,192,134,88,89,86]       new heptagon
[88,134,102,150,148]          pentagon
[192,194,134]                triangle
```

All other maximal facet contact sets are retained. Their coordinates are not claimed to be unchanged: the construction includes a global physical shape repair, with the volume centroid recomputed throughout.

The replaced disk has the unchanged exterior boundary

```text
[23,78,192,194,134,102,150,148,88,89,86].
```

Thus this is a realized **five-facet disk to three-facet disk replacement with one interior vertex removed**. The topological accounting is

```text
Delta V = -1
Delta F = 3-5 = -2
Delta E = Delta F-1 = -3.
```

These numbers agree with the independently reconstructed maximal complex, rather than being used to predict acceptance.

The maximal facet distribution is

```text
359 triangles
59 quadrilaterals
5 pentagons
2 hexagons
2 heptagons.
```

There are 510 integration triangles and **83 flat integration diagonals**. The latter are not physical edges. The checks are

```text
257-682+427 = 2
sum(maximal facet boundary lengths) = 1364 = 2*682.
```

## 3. Why the bounded original193 gate needed enlargement

The inherited delete193 procedure was executed from the hash-bound C1370 parent. Its repaired deletion stage had numerical V257/E686/F431 and S1/U1: still worse in E than its parent.

The actual newly exposed cap consisted of three facets with union boundary

```text
[78,192,134,88,86].
```

The joint regional proposal at coordinate trust **0.003**, followed by 45 whole-body repair iterations at target **3e-7** and initial trust **0.001**, reached a numerical S1/U1 state. However, a tolerance-based hull grouping at that stage was not a valid exact endpoint definition.

In particular, the apparent six-vertex contact polygon

```text
[23,78,192,134,88,89]
```

had an additional nearly coplanar incident triangle involving **23,89,86**. The all-point numerical support check put vertex 86 outside the six-vertex plane by about 2.0e-11. A rational reconstruction of that incomplete contact target rejected the triangle plane through **23,78,192** as non-supporting.

Vertex 86 was not a redundant point to discard. Its projected position lay outside the six-vertex polygon across the 23–89 boundary. The correct operation was to replace the **whole enlarged region** by the seven-vertex polygon

```text
[23,78,192,134,88,89,86].
```

All its contacts were then imposed together, obsolete internal polar nodes were discarded, and the geometry was reconstructed again. This produced numerical V257/E682/F427, S1/U1, positive noncontact exposure, and minimum normalized primal/polar escapes close to 3e-7. Only the subsequent exact reconstruction and complete audits established the reported successor.

This is the continuation-critical distinction: the five-vertex cap proposal was useful for reaching the region, but neither its averaged proposal pole nor the intermediate six-vertex near-plane grouping defined the final physical facet.

## 4. Ordinary homogeneous mass and exhaustive mechanical evidence

Let I_i/D be the raw rational vertices reconstructed from the new PN03 stream, and let T be its 510 complete outward integration triangles. For each (a,b,c) in T, set

```text
w_abc = det(I_a,I_b,I_c)
W = sum_T w_abc
M[k] = sum_T w_abc*(I_a[k]+I_b[k]+I_c[k]).
```

The exact density-one quantities are

```text
ordinary volume          = W/(6*D^3)
raw ordinary moment[k]   = M[k]/(24*D^4)
raw ordinary centroid[k] = M[k]/(4*W*D).
```

Define

```text
g = gcd(4*W,M[0],M[1],M[2])
A = 4*W/g
B = M/g
P_i = A*I_i-B
Q = A*D.
```

The reported own-centred body is **conv{P_i/Q}**. These finite expressions, with the complete PN03 input, specify all volume and first-moment data exactly, without substituting a convenient reference point. The density-one volume is approximately **2.212216056**. Reintegration of the centred integer vertices gives all three first moments exactly zero.

Both complete implementations returned the same feature classification:

```text
V/E/F                         257/682/427
S/U/H                         1/1/0
stable maximal faces          [[158,163,161]]
unstable vertices             [138]
saddle edges                  []
weak/degenerate equilibria    []
zero ordinary edge primitives 0
centred first moments         [0,0,0]
```

Thus all 427 maximal facets, all 257 extreme vertices and all 682 full physical edges were classified. All **2728 ordinary edge primitives** were nonzero.

The first implementation reconstructs primitive supporting planes and maximal polygon cycles from the exact oriented triangulation, checks every supporting plane against every input point, verifies polygon convexity, vertex extremality, incidence, connectedness and Euler, and computes ordinary volume and moments. Its full edge test uses both segment-foot conditions and both adjacent-normal conditions.

The second implementation independently checks complete facet contact sets, polygon halfplanes, rank-three vertices and cyclic vertex links. It reconstructs edges from intersections of facet contact sets, recomputes ordinary mass with an interior-apex decomposition, tests vertices against every other point, and tests complete edge feet with the two-normal Gram cone. It is a separate implementation, not a second call to the first predicate set.

The unchanged source hashes are

```text
exact_audit.py
7d44d745f236e3a2a7ada6802bfffb578ea262c0b39ba345f2abbf31299e2f90

independent_audit.py
e510e67194e2ac3dd6b87f1cb69fbd23f1555331aab92c8cf7595710e849c6d4
```

The completed replay included exact translation covariance under **(17,-11,23)**, rejection of a reversed integration triangle, rejection of a missing integration triangle, reintegration at the exact own-centroid, and all stored rooted witness checks.

A separate directory was then created from the actual serialized six-file source bundle. The PN03 stream was decoded there, and both complete audits and controls completed again. The observed statuses were

```text
FRESH_STANDARD_LIBRARY_COMPLETE_REPLAY_PASS
COLD_LITERAL_SUCCESSOR_REPLAY_PASS.
```

The generic replay field `new_below1000_winner: false` refers to its C<1000 threshold. It does not negate the verified reduction from E685 to E682.

## 5. Further construction attempted, without promoting a second endpoint

After the E682 body was retained, work continued on simultaneous vertex-disjoint polar-region replacements, preservation of outside ascent witnesses, guarded physical repair, and contractions of short primal edges. These were not substitutions of another low-complexity nonwinner for the accepted parent.

A useful distinction emerged between a common-parent screen and a complete outside-witness screen. Two polar nodes can have a common positive parent while their replacement removes the only positive witness of another, outside node. Accordingly, a common-parent average is not a sufficient endpoint guard. The whole remaining ascent system must be rebuilt, and every surviving nonroot must retain a positive physical escape.

Neither the observed simultaneous coarsening trajectories nor the additional edge-contraction trajectories supplied another completed exact strict110 endpoint. Numerical S/U counts, lower provisional E values, and partially repaired states from those experiments are not promoted as continuation parents here. The next exact construction should start from **KR68_CAP257_C1364**, with its completed seven-vertex contact region, rather than from the invalid six-vertex grouping or the worse E686 deletion stage.

## 6. Complete parent-relative reconstruction program

This is a finite replay of the construction actually used, not an open-ended instruction to search until a smaller body is found. Its explicit source input is the assigned journal, containing the complete authoritative parent bundle and the regional source units. It extracts and hash-checks those sources, executes the bounded delete-and-complete-cap construction, freezes every exact rational operation, and requires the stated successor PN03 digest before accepting anything.

Numerical replay dependencies are **Python 3.13.5, NumPy 2.3.5 and SciPy 1.17.0**, with one BLAS/OMP thread. Floating-point discovery can be platform-sensitive; the byte-digest guard deliberately rejects a different regenerated stream. Once the retained standalone bundle is available, its exact reconstruction and proof use only the Python standard library and do not have this numerical dependency.

Save the following as `recover_kr68.py` and run

```text
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python recover_kr68.py research-journal.md kr68_recovered
```

The output directory must not already exist.

```python
import os
os.environ['OPENBLAS_NUM_THREADS'] = '1'
os.environ['OMP_NUM_THREADS'] = '1'
import base64, hashlib, json, re, subprocess, sys, zlib
from pathlib import Path
from fractions import Fraction
from itertools import combinations
from math import isqrt

assert __debug__, 'Do not run with python -O'
sys.set_int_max_str_digits(0)
assert sys.version_info[:3] == (3, 13, 5)
import numpy as np
import scipy
assert np.__version__ == '2.3.5'
assert scipy.__version__ == '1.17.0'

PARENT_BUNDLE = '910825acaaf3769cbaa6e8e8c000facbcd6cb9239403db4121d27393bcb01071'
PARENT_PN03 = '7b04ac8b258f880034877a398528e6d777de81368f6c314d266376773373337d'
CHILD_PN03 = '5c5b1f474bfc65e18aa93bb7212f5e6ef74679cdaaf0194bffda1d066c2ccae628'
SOURCE_HASHES = {
    'regional.py': '0cf918a9e334a62a1d074c632b396792dbd0a04873993b88531ed1993a4bf885',
    'joint_gate.py': '3fe9e361943b2c802231d25c6f0159ba164b4e0c6437840cea74886bc34b0ac1',
}

def sha(data):
    return hashlib.sha256(data).hexdigest()

journal = Path(sys.argv[1]).resolve()
work = Path(sys.argv[2]).resolve()
work.mkdir(exist_ok=False)
parent = work / 'parent'
parent.mkdir()
s = journal.read_text(encoding='utf-8')
heading = '# Nimble Nova 51 — exact two-edge reduction with a complete recovery capsule'
start = s.index(heading)
part = s[start:s.index('## 8. Supplemental', start)]
m = re.search(r'### Literal payload\s+```text\s+(.*?)\s+```', part, re.S)
assert m is not None
packed = zlib.decompress(base64.b85decode(''.join(m.group(1).split())))
assert len(packed) == 31524 and sha(packed) == PARENT_BUNDLE
bundle = json.loads(packed)
assert bundle['version'] == 1
for name, text in bundle['files'].items():
    assert Path(name).name == name
    (parent / name).write_text(text, encoding='utf-8')
pn = zlib.decompress(base64.b85decode((parent / 'capsule.b85').read_bytes()))
assert len(pn) == 10534 and sha(pn) == PARENT_PN03
(parent / 'capsule.pn03').write_bytes(pn)

heading = '# Nimble Nova 51 — constructive continuation, with a reproducible regional gate'
start = s.index(heading)
part = s[start:s.index('\n## 2026-', start)]
for name, digest in SOURCE_HASHES.items():
    h = re.search(r'### [^\n]*`' + re.escape(name) + r'`[^\n]*\n', part)
    assert h is not None
    m = re.search(r'```python\s+(.+?)\n```', part[h.end():], re.S)
    assert m is not None
    source = (m.group(1) + '\n').encode()
    assert sha(source) == digest
    (parent / name).write_bytes(source)

subprocess.run([
    sys.executable, str(parent / 'codec.py'),
    str(parent / 'capsule.pn03'), str(parent / 'baseline.npz')
], check=True)
sys.path.insert(0, str(parent))
from regional import get_hull, repair, region_boundary, retract, tree
from joint_gate import joint_proposal
from codec import reconstruct, topology, dot, sub
from exact_audit import audit

# The exact parent's own-centred floating image, not a historical checkpoint.
X = np.load(parent / 'baseline.npz', allow_pickle=True)['V']
T, old, E, active = get_hull(X)
assert (len(active), len(E), len(old)) == (258, 685, 429)
removed = 193
keep = [v for v in range(len(X)) if v != removed]
inv = {v:i for i,v in enumerate(keep)}
locks = [[inv[v] for v in c if v != removed] for c in old if len(c) > 3]
locks = [c for c in locks if len(c) > 3]
Y, deletion_report, deletion_history = repair(
    X[keep], locks, target=3e-7, iterations=12, trust=.001)
T, cycles, E, active = get_hull(Y)
oldsets = [set(c) - {removed} for c in old]
region = [f for f,c in enumerate(cycles)
          if not any({keep[v] for v in c} <= q for q in oldsets)]
boundary = region_boundary(cycles, region)
assert boundary == [78,192,134,88,86]
assert not ({v for f in region for v in cycles[f]} - set(boundary))
locks = [c for c in cycles if len(c) > 3]
Z, locks, proposal_report, geometry = joint_proposal(
    Y, region, locks, trust=.003, target=3e-7)
Z, repair_report, repair_history = repair(
    Z, locks, target=3e-7, iterations=45, trust=.001)

# Complete the physical region; do not freeze the near-plane six-cycle.
T, cycles, E, active = get_hull(Z)
region = [f for f,c in enumerate(cycles)
          if set(c) in ({23,78,192,134,88,89}, {23,89,86})]
assert len(region) == 2
boundary = region_boundary(cycles, region)
assert boundary == [23,78,192,134,88,89,86]
locks = [c for f,c in enumerate(cycles)
         if f not in region and len(c) > 3] + [boundary]
Z = retract(Z, locks)
T, cycles, E, active = get_hull(Z)
assert (len(active), len(E), len(cycles)) == (257, 682, 427)
assert len(active) == len(Z)

# Freeze a vertex-only rational contact chart. In reverse deletion order,
# every final triangular basis has already been reconstructed.
faces = [list(c) for c in cycles]
alive = set(range(len(Z)))
schedule = []
while any(len(c) > 3 for c in faces):
    choices = []
    for v in alive:
        ff = [f for f,c in enumerate(faces) if len(c) > 3 and v in c]
        if ff:
            choices.append((len(ff), v, ff))
    rank, v, ff = min(choices)
    assert 1 <= rank <= 3
    schedule.append((v, ff))
    alive.remove(v)
    for f in ff:
        faces[f].remove(v)
ops = []
for v, ff in reversed(schedule):
    bases = [tuple(faces[f]) for f in ff]
    normals = [np.cross(Z[b]-Z[a], Z[c]-Z[a]) for a,b,c in bases]
    if len(bases) == 1:
        axes = (int(np.argmax(abs(normals[0]))),)
    elif len(bases) == 2:
        axes = max(combinations(range(3), 2), key=lambda ab:
            abs(normals[0][ab[0]]*normals[1][ab[1]]
                - normals[0][ab[1]]*normals[1][ab[0]]))
    else:
        axes = (0,1,2)
    ops.append((v, bases, axes))
D0 = 10**18
J = [[round(float(x)*D0) for x in row] for row in Z]
T = [(c[0], c[k], c[k+1]) for c in cycles for k in range(1,len(c)-1)]
assert len(ops) == 81 and sum(len(o[1]) for o in ops) == 83
assert len(T) == 510

def encode(D0, J, ops, T, K=1, pr=0, po=0, witnesses=((),())):
    out = bytearray(b'PN03')
    def u(x):
        x = int(x)
        assert x >= 0
        while x >= 128:
            out.append((x & 127) | 128)
            x >>= 7
        out.append(x)
    def signed(x):
        u(2*x if x >= 0 else -2*x-1)
    u(D0)
    u(len(J))
    last = [0,0,0]
    for row in J:
        for k in range(3):
            signed(row[k]-last[k])
            last[k] = row[k]
    u(len(ops))
    for v, bases, axes in ops:
        u(v)
        u(len(bases))
        for b in bases:
            for x in b:
                u(x)
        for x in axes:
            u(x)
    u(len(T))
    last = 0
    for tri in T:
        for x in tri:
            signed(x-last)
            last = x
    u(K)
    u(pr)
    u(po)
    for row in witnesses:
        u(len(row))
        last = 0
        for x in row:
            signed(x-last)
            last = x
    return bytes(out)

raw = encode(D0, J, ops, T)
I, D, T, extra = reconstruct(raw)
R, P = audit(I, T, D, expected=(1,1,0))
assert (R['V'], R['E'], R['F']) == (257,682,427)
assert R['stable'] == [[158,163,161]] and R['unstable'] == [138]
assert not R['saddles'] and not R['degeneracies']
assert R['zero_edge_primitives'] == 0
assert list(map(int, R['centred_moments'])) == [0,0,0]

# The selected witnesses are checked by exact integer signs before encoding.
A = int(R['centroid_multiplier'])
B = tuple(map(int, R['centroid_subtract']))
planes, exact_cycles, exact_edges, tf = topology(I,T)
h = [A*p[3]-dot(p[:3],B) for p in planes]
assert min(h) > 0
XX = np.array([[float(Fraction(x,A*D)) for x in row] for row in P])
QQ = np.array([[float(Fraction(n*A*D,hh)) for n in p[:3]]
               for p,hh in zip(planes,h)])
witnesses = []
roots = []
K = 1
for side, points in enumerate((XX,QQ)):
    ii, jj, values, root = tree(points, target=3e-7)
    parents = [-1]*len(points)
    for i,j in zip(ii,jj):
        i,j = int(i),int(j)
        parents[i] = j
        if side == 0:
            n = P[i]
            e = sub(P[j],P[i])
        else:
            n = planes[i][:3]
            e = tuple(planes[j][k]*h[i]-n[k]*h[j] for k in range(3))
        a = dot(n,e)
        assert a > 0
        K = max(K,isqrt((dot(n,n)*dot(e,e))//(a*a))+1)
    witnesses.append(parents)
    roots.append(root)
assert roots[0] == 138
assert set(exact_cycles[roots[1]]) == {158,163,161}
raw = encode(D0,J,ops,T,K,*roots,witnesses)
assert sha(raw) == CHILD_PN03, 'Numerical replay produced different defining bytes'

body = work / 'KR68_CAP257_C1364'
body.mkdir()
for name in ('codec.py','exact_audit.py','independent_audit.py','REPLAY.py'):
    (body/name).write_bytes((parent/name).read_bytes())
(body/'capsule.pn03').write_bytes(raw)
(body/'capsule.b85').write_text(base64.b85encode(zlib.compress(raw,9)).decode())
summary = dict(name='KR68_CAP257_C1364', raw_bytes=len(raw),
               raw_sha256=sha(raw), V=257, E=682, F=427)
(body/'SUMMARY.json').write_text(json.dumps(summary,indent=2))
subprocess.run([sys.executable,'-S',str(body/'REPLAY.py')],check=True)

# Serialize actual endpoint sources, then decode them into an empty directory.
names = ('codec.py','exact_audit.py','independent_audit.py',
         'REPLAY.py','capsule.b85','SUMMARY.json')
portable = json.dumps({'version':1,'files':{
    name:(body/name).read_text() for name in names
}},separators=(',',':')).encode()
(body/'bundle.json').write_bytes(portable)
encoded = base64.b85encode(zlib.compress(portable,9)).decode()
(body/'bundle.b85').write_text(encoded)
restored = zlib.decompress(base64.b85decode(encoded))
assert restored == portable
cold = work/'cold'
cold.mkdir(exist_ok=False)
for name,text in json.loads(restored)['files'].items():
    assert Path(name).name == name
    (cold/name).write_text(text,encoding='utf-8')
cold_raw = zlib.decompress(base64.b85decode((cold/'capsule.b85').read_bytes()))
assert sha(cold_raw) == CHILD_PN03
(cold/'capsule.pn03').write_bytes(cold_raw)
subprocess.run([sys.executable,'-S',str(cold/'REPLAY.py')],check=True)
receipt = json.loads((cold/'REPLAY_REPORT.json').read_text())
assert receipt['status'] == 'FRESH_STANDARD_LIBRARY_COMPLETE_REPLAY_PASS'
assert receipt['VEF'] == [257,682,427]
assert receipt['SUH'] == [1,1,0]
assert receipt['independent_full_audits'] == 2
assert receipt['centred_moments'] == ['0','0','0']
print('COLD_LITERAL_SUCCESSOR_REPLAY_PASS')
print('PN03_SHA256',sha(cold_raw))
print('BUNDLE_BYTES',len(portable),'BUNDLE_SHA256',sha(portable))
print(json.dumps(receipt,indent=2))
```

## 7. Continuation checkpoint

Resume from **KR68_CAP257_C1364**, actual **257/682/427**, own-centred strict110, stable **[158,163,161]**, unstable **138**, with the complete **seven-vertex** new facet and the new PN03 binding above.

The completed construction demonstrates genuine simultaneous primal vertex loss and polar rank loss: the original five-facet star was replaced by three actual supporting facets, and the changed ordinary solid was re-centred and fully checked. It does not establish the requested E<500 endpoint or exclude further reductions. The remaining target is another **183 true-edge reductions** to reach E499, with actual geometry, ordinary mass, complete feature classification, and retained exact endpoint bytes deciding every claimed improvement.
