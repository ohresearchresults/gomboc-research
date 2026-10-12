# figure-0340

AI research report · 2026-09-08 UTC

<!-- historical-status:start -->
> **Historical AI report.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../../C622/README.md) passes the supplied exact checks; the search for C<500 remains open. See [verification status and source gaps](../../catalog/coverage.md).
<!-- historical-status:end -->

---

# Nimble Nova 51 — nonterminal handoff: vertex-loss and cap-replacement gate

## 1. Acceptance boundary

**No smaller exact homogeneous own-centred strict (1,1,0) body is promoted by this continuation. The E < 500 objective remains unestablished.**

The source-authoritative starting construction remains **NN51_CHAIN258_PN03_C1370**, with actual maximal counts **V = 258, E = 685, F = 429**, stable outward triangle **[158,163,161]**, unstable vertex **138**, no saddle edges, no equilibrium degeneracies, and no zero ordinary edge primitives. These are the claims of the preserved, fully literal parent handoff, not a newly observed verification in this continuation. Its defining stream and recovery bundle are present in the supplied journal. 

The visible continuation record does not supply inspectable defining bytes together with completed verification returns for a new successor. In particular, **NN51_VLOSS257_C1364 is not an accepted result identifier in this handoff**. Names used in issued reconstruction or verification commands must not substitute for the returned data and completed receipts. This limitation does not establish that a proposed body is geometrically impossible or that a local computation could not have produced useful data.

The strongest useful continuation is a specific **delete-one-vertex, then replace its entire new cap** procedure, rather than another isolated coplanar-face proposal. A complete bounded reproduction and exact-acceptance program is supplied below. It starts from the correct literal C1370 parent and emits a self-contained successor capsule only after both exact implementations and a separate cold reconstruction complete successfully.

## 2. Exact parent identity and carried-forward evidence

Use precisely these two source bindings:

| Source | Decompressed bytes | SHA-256 |
|---|---:|---|
| Complete six-file recovery bundle | 31524 | `910825acaaf3769cbaa6e8e8c000facbcd6cb9239403db4121d27393bcb01071` |
| PN03 body definition | 10534 | `7b04ac8b258f880034877a398528e6d777de81368f6c314d266376773373337d` |

The six bundled files are `codec.py`, `exact_audit.py`, `independent_audit.py`, `REPLAY.py`, `capsule.b85`, and `SUMMARY.json`. The journal gives their complete literal payload, not merely download locations. 

The parent uses D0 = 10^18, 258 seed triples, 79 ordered coordinate operations, and 83 scalar contact equations. Its 512 integration triangles represent 429 maximal facets and contain 83 flat diagonals that are **not** true edges. Its reported facet distribution is 359 triangles, 62 quadrilaterals, four pentagons, three hexagons, and one heptagon. 

The preserved parent handoff reports two completed independently implemented full exact audits and fresh standard-library replays, including translation-covariance and malformed-boundary controls. That historical evidence must remain distinguished from any command issued during this continuation. 

### Ordinary mass convention

For integer raw vertices I_i with common positive denominator D and complete outward integration triangles T, define

    w_abc = det(I_a,I_b,I_c)
    W = sum_T w_abc
    M_k = sum_T w_abc (I_a,k + I_b,k + I_c,k).

Then the exact ordinary density-one quantities are

    volume = W / (6 D^3)
    raw first moment_k = M_k / (24 D^4)
    raw centroid_k = M_k / (4 W D).

Set

    g0 = gcd(4W, M_x, M_y, M_z)
    A = 4W / g0
    B = M / g0
    P_i = A I_i - B
    Q = A D.

The accepted own-centred body is conv{P_i/Q}. Its three ordinary first moments must be checked to be exactly zero by reintegration, not inferred from a small decimal centroid. The parent's reported ordinary volume is approximately 2.2135471789877386. Its full exact inputs and these finite sums determine all ordinary mass and first-moment data. 

## 3. Preserved numerical gate, not an exact successor

The carried-forward working context records a numerical deletion of **original vertex 193**, followed by whole-body repair with the actual volume centroid recomputed. The reported endpoint was

    V/E/F = 257/686/431
    S/U = 1/1
    minimum normalized primal escape ≈ 2.9992530057293034e-7
    minimum normalized polar escape ≈ 2.982633525374751e-7
    ordinary volume ≈ 2.213533643115921.

That was a numerical observation, not a retained exact defining table or a pair of exact audit receipts. Moreover, **E686 is worse than the current parent's E685**, despite the real loss of one vertex. It is therefore a useful intermediate gate, not a smaller accepted Gömböc.

The proposed next operation is to identify the entire cap newly exposed by the deletion, replace all its constituent facets together by their union boundary, and repair the resulting geometry and both escape systems simultaneously. The cap is recovered from the actual hull; its incidence must not be guessed from a filename or an old face ordering.

The program below deliberately does not hard-code an alleged successful cap boundary. It derives the cap as those actual post-deletion facets whose retained original labels are not contained in any surviving old facet contact set. It then verifies that their oriented union has one boundary cycle and no retained interior vertex before using the existing joint regional proposal mechanism.

## 4. Geometry that explains the gate

### Vertex deletion need not reduce the true edge count

Suppose a vertex has degree d and belongs to t triangular maximal facets. Assume that deleting it retains the other vertices, shortens the incident nontriangular facets without further mergers, and exposes a triangulated d-gon cap. Under those hypotheses,

    ΔV = -1
    ΔF = d - 2 - t
    ΔE = d - 3 - t.

Thus a vertex deletion can increase E. Counting one fewer vertex is not sufficient evidence of a smaller body.

Under the additional hypotheses that the whole replacement cap becomes one genuine supporting maximal facet and no other incidence changes occur,

    ΔF = 1 - t
    ΔE = -t.

This is why deleting a vertex and subsequently coalescing its **entire** replacement cap is a materially different operation from isolated facet fusion.

More generally, a certified disk replacement changing k old facets into k' new facets and deleting r interior vertices, with the external boundary unchanged, satisfies

    E_new - E_old = (k' - k) - r.

For example, the abstract pattern r = 1, k = 5, k' = 3 would change the parent counts to 257/682/427. **That arithmetic specifies a target incidence pattern; it is not evidence that a realization or a strict110 endpoint has been attained.** All counts must come from the final exact maximal complex.

### Disappearing polar witnesses are not endpoint constraints

A temporary averaged regional pole may be used to formulate a proposal. Once several physical polar nodes coalesce, their old internal arrows are no longer features of the endpoint. Acceptance must instead reconstruct the actual maximal supporting planes, translate them using the newly computed ordinary centroid, and rebuild the endpoint's two escape systems.

For a raw primal arrow i → j and actual centroid c, the required inequality is

    (v_i-c) · (v_j-v_i) > 0.

For raw polar points q_i and q_j, with all denominators 1-q_i·c positive, the centred polar arrow condition is

    (q_i·q_j)(1-q_i·c) - (q_i·q_i)(1-q_j·c) > 0.

These are conditions on the actual reconstructed geometry and its actual mass. They do not license using the averaged proposal pole as the physical endpoint.

### Larger parent-closed pruning remains only a proposal

A useful exact graph fact is the following. If every nonroot point has a parent satisfying

    p_i · (p_parent(i)-p_i) > 0,

then squared radius increases strictly along each arrow. Any parent-closed retained subset preserves these arrows about the same reference point. Removing leaves is therefore a principled way to reduce the primal escape architecture rather than deleting arbitrary points.

This does **not** preserve the ordinary centroid, guarantee that the old reference remains interior, preserve the polar escape system, or prove monostability. Large pruning targets require the full physical reconstruction and mass tests again. No E < 500 result is inferred from a target retained-vertex count.

## 5. Complete continuation program

This is a **bounded reproduction and acceptance program**, not a claim that its successful output was observed here. Its explicit source input is the supplied complete journal. It recovers the hash-bound C1370 parent and the complete regional source units already printed in that journal. It does not depend on an old numerical checkpoint, a missing archive, or an unverified smaller-body filename.

The numerical stage is specified for Python 3.13.5, NumPy 2.3.5, and SciPy 1.17.0, with one BLAS/OMP thread. The eventual emitted exact recovery capsule requires only the Python standard library. The numerical trajectory is not itself the mathematical definition: the emitted integer chart and complete exact reconstruction sources become that definition only after successful verification.

Save this as `resume_cap_gate.py` and run

    OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python resume_cap_gate.py 'research-journal(20260908-052356).md' continuation_work

The program's success condition is stricter than the historical rational-chart driver's E < 687 guard: it explicitly requires **V < 258 and E < 685**, strict110, no degeneracies, and zero ordinary edge primitives. A failure is only a failure of this bounded gate.

```python
import os
os.environ['OPENBLAS_NUM_THREADS'] = '1'
os.environ['OMP_NUM_THREADS'] = '1'
import base64, hashlib, json, re, subprocess, sys, zlib
from pathlib import Path
sys.set_int_max_str_digits(0)
assert __debug__, 'Assertions must remain enabled'

VERIFY = '''from pathlib import Path
import hashlib, json, math, sys
sys.set_int_max_str_digits(0)
assert __debug__
from rational_chart import reconstruct, write_rows
from exact_audit import audit
from independent_audit import run
from REPLAY import complete
from codec import topology, dot, sub, det
base = Path(__file__).resolve().parent
raw = (base/'chart.json').read_bytes()
data = json.loads(raw)
I,D,T,nodes,order = reconstruct(data)
R,P = audit(I,T,D,expected=(1,1,0))
complete(I,R)
assert R['V'] < 258 and R['E'] < 685
assert not R['degeneracies'] and R['zero_edge_primitives'] == 0
assert list(map(int,R['centred_moments'])) == [0,0,0]
folder = base/'verified'
folder.mkdir(exist_ok=False)
write_rows(folder/'raw_vertices.csv.gz',I)
write_rows(folder/'vertices.csv.gz',P)
write_rows(folder/'triangles.csv.gz',T)
(folder/'definition.json').write_text(json.dumps({'raw_denominator':str(D)}))
(folder/'exact_report.json').write_text(json.dumps(R,indent=2))
(folder/'chart_order.json').write_text(json.dumps(order))
run(folder)

def moments(points):
    W = 0
    M = [0,0,0]
    for a,b,c in T:
        w = det(points[a],points[b],points[c])
        W += w
        for k in range(3):
            M[k] += w*(points[a][k]+points[b][k]+points[c][k])
    return W,M

W,M = moments(I)
shift = (17*D,-11*D,23*D)
J = [tuple(p[k]+shift[k] for k in range(3)) for p in I]
W1,M1 = moments(J)
assert W1 == W
assert M1 == [M[k]+4*W*shift[k] for k in range(3)]
assert moments(P)[1] == [0,0,0]
for bad in ([tuple(reversed(T[0]))]+list(T[1:]), list(T[:-1])):
    try:
        audit(I,bad,D)
    except AssertionError:
        pass
    else:
        raise AssertionError('Malformed boundary was not rejected')

planes,cycles,edges,tf = topology(I,T)
A = int(R['centroid_multiplier'])
B = tuple(map(int,R['centroid_subtract']))
h = [A*p[3]-dot(p[:3],B) for p in planes]
assert min(h) > 0
pr = R['unstable'][0]
po = next(f for f,c in enumerate(cycles) if set(c)==set(R['stable'][0]))
parents = []
K = 1
for side,root,count in ((0,pr,len(P)),(1,po,len(planes))):
    parent = [-1]*count
    for i in range(count):
        if i == root:
            continue
        n = P[i] if side == 0 else planes[i][:3]
        for j in range(count):
            if side == 0:
                e = sub(P[j],P[i])
            else:
                e = tuple(planes[j][k]*h[i]-n[k]*h[j] for k in range(3))
            a = dot(n,e)
            if a > 0:
                parent[i] = j
                K = max(K,math.isqrt((dot(n,n)*dot(e,e))//(a*a))+1)
                break
        assert parent[i] >= 0
    for i in range(count):
        v = i
        seen = set()
        while v != root:
            assert v >= 0 and v not in seen
            seen.add(v)
            v = parent[v]
    parents.append(parent)
(folder/'witnesses.json').write_text(json.dumps({'K':K,'roots':[pr,po],'parents':parents}))
receipt = {k:R[k] for k in ('V','E','F','class_SUH','stable','unstable','saddles','degeneracies','zero_edge_primitives')}
receipt.update(chart_bytes=len(raw),chart_sha256=hashlib.sha256(raw).hexdigest(),K=K)
(folder/'receipt.json').write_text(json.dumps(receipt,indent=2))
print('TWO_EXACT_AUDITS_CONTROLS_AND_ROOTED_WITNESSES_PASS',json.dumps(receipt),flush=True)
'''

journal = Path(sys.argv[1]).resolve()
work = Path(sys.argv[2]).resolve()
work.mkdir(exist_ok=False)
s = journal.read_text(encoding='utf-8')
heading = '# Nimble Nova 51 — exact two-edge reduction with a complete recovery capsule'
start = s.index(heading)
part = s[start:s.index('## 8. Supplemental',start)]
m = re.search(r'### Literal payload\s+```text\s+(.*?)\s+```',part,re.S)
assert m is not None
packed = zlib.decompress(base64.b85decode(''.join(m.group(1).split())))
assert len(packed) == 31524
assert hashlib.sha256(packed).hexdigest() == '910825acaaf3769cbaa6e8e8c000facbcd6cb9239403db4121d27393bcb01071'
bundle = json.loads(packed)
assert bundle['version'] == 1
for name,text in bundle['files'].items():
    assert Path(name).name == name
    (work/name).write_text(text,encoding='utf-8')
pn = zlib.decompress(base64.b85decode(bundle['files']['capsule.b85']))
assert len(pn) == 10534
assert hashlib.sha256(pn).hexdigest() == '7b04ac8b258f880034877a398528e6d777de81368f6c314d266376773373337d'
(work/'capsule.pn03').write_bytes(pn)

heading = '# Nimble Nova 51 — constructive continuation, with a reproducible regional gate'
start = s.index(heading)
end = s.index('\n## 2026-',start)
part = s[start:end]
for name in ('regional.py','rational_chart.py','joint_gate.py'):
    h = re.search(r'### [^\n]*`'+re.escape(name)+r'`[^\n]*\n',part)
    assert h is not None, name
    m = re.search(r'```python\s+(.+?)\n```',part[h.end():],re.S)
    assert m is not None, name
    source = m.group(1)+'\n'
    (work/name).write_text(source,encoding='utf-8')
    print('SOURCE',name,hashlib.sha256(source.encode()).hexdigest(),flush=True)

subprocess.run([sys.executable,'-S',str(work/'REPLAY.py')],check=True)
subprocess.run([sys.executable,str(work/'codec.py'),str(work/'capsule.pn03'),str(work/'baseline.npz')],check=True)
sys.path.insert(0,str(work))
import numpy as np
import scipy
assert np.__version__ == '2.3.5'
assert scipy.__version__ == '1.17.0'
from regional import get_hull, repair, region_boundary, evaluate
from joint_gate import joint_proposal
z = np.load(work/'baseline.npz',allow_pickle=True)
X = z['V']
T,old,E,active = get_hull(X)
assert (len(active),len(E),len(old)) == (258,685,429)
removed = 193
keep = [i for i in range(len(X)) if i != removed]
inv = {v:i for i,v in enumerate(keep)}
locks = [[inv[v] for v in c if v != removed] for c in old if len(c)>3]
locks = [c for c in locks if len(c)>3]
Y,R,history = repair(X[keep],locks,target=3e-7,iterations=10,trust=.001)
(work/'deletion_report.json').write_text(json.dumps({'report':R,'history':history},indent=2))
T,cycles,E,active = get_hull(Y)
oldsets = [set(c)-{removed} for c in old]
region = [f for f,c in enumerate(cycles) if not any({keep[v] for v in c} <= q for q in oldsets)]
boundary = region_boundary(cycles,region)
assert boundary is not None, 'New cap is not one boundary disk'
assert not ({v for f in region for v in cycles[f]}-set(boundary)), 'Retained cap interior vertices require a broader replacement'
locks = [c for c in cycles if len(c)>3]
(work/'cap_selection.json').write_text(json.dumps({'removed_original_vertex':removed,'region':region,'boundary':boundary,'original_boundary':[keep[v] for v in boundary]},indent=2))
options = []
for trust in (.001,.003,.01):
    try:
        Z,L,rr,geometry = joint_proposal(Y,region,locks,trust=trust,target=3e-7)
        options.append((rr['deficit'],trust,Z,L))
    except (ValueError,ArithmeticError,AssertionError,np.linalg.LinAlgError) as exc:
        print('INITIAL_GATE_REJECTED',trust,repr(exc),flush=True)
assert options, 'No bounded initial regional proposal'

sources = ('codec.py','exact_audit.py','independent_audit.py','REPLAY.py','rational_chart.py')
accepted = False
for number,(_,trust,Z,L) in enumerate(sorted(options,key=lambda q:(q[0],q[1]))):
    Z,rr,history = repair(Z,L,target=3e-7,iterations=45,trust=.001)
    T,cycles,E,active = get_hull(Z)
    candidate = work/('candidate_'+str(number))
    candidate.mkdir()
    (candidate/'numerical_report.json').write_text(json.dumps({'trust':trust,'report':rr,'history':history},indent=2))
    # Remove any genuinely inactive retained generators before freezing indices.
    active = list(map(int,active))
    renumber = {v:i for i,v in enumerate(active)}
    frozen_cycles = [[renumber[v] for v in c] for c in cycles]
    data = {'D0':str(10**18),'J':[[round(float(x)*10**18) for x in Z[v]] for v in active],'cycles':frozen_cycles}
    chart = json.dumps(data,separators=(',',':')).encode()
    (candidate/'chart.json').write_bytes(chart)
    (candidate/'original_labels.json').write_text(json.dumps([keep[v] for v in active]))
    if not (len(active)<258 and len(E)<685 and rr['S']==rr['U']==1 and min(rr['min_primal'],rr['min_polar'])>0):
        print('NUMERICAL_NONWINNER',number,json.dumps(rr),flush=True)
        continue
    for name in sources:
        (candidate/name).write_bytes((work/name).read_bytes())
    (candidate/'VERIFY.py').write_text(VERIFY,encoding='utf-8')
    try:
        subprocess.run([sys.executable,'-S',str(candidate/'VERIFY.py')],check=True)
    except subprocess.CalledProcessError:
        print('EXACT_CANDIDATE_REJECTED',number,flush=True)
        continue
    names = (*sources,'VERIFY.py','chart.json','original_labels.json')
    portable = json.dumps({'version':1,'files':{name:(candidate/name).read_text() for name in names}},separators=(',',':')).encode()
    digest = hashlib.sha256(portable).hexdigest()
    encoded = base64.b85encode(zlib.compress(portable,9)).decode()
    (candidate/'bundle.b85').write_text(encoded)
    # Decode the actual portable bytes into a separate empty directory.
    restored = zlib.decompress(base64.b85decode(encoded))
    assert restored == portable and hashlib.sha256(restored).hexdigest() == digest
    cold = work/('cold_'+str(number))
    cold.mkdir()
    for name,text in json.loads(restored)['files'].items():
        (cold/name).write_text(text,encoding='utf-8')
    subprocess.run([sys.executable,'-S',str(cold/'VERIFY.py')],check=True)
    print('COLD_LITERAL_SUCCESSOR_REPLAY_PASS',flush=True)
    print('BUNDLE_BYTES',len(portable),'BUNDLE_SHA256',digest,flush=True)
    print('CHART_BYTES',len(chart),'CHART_SHA256',hashlib.sha256(chart).hexdigest(),flush=True)
    print('LITERAL_SUCCESSOR_BUNDLE_BEGIN',flush=True)
    for i in range(0,len(encoded),100):
        print(encoded[i:i+100],flush=True)
    print('LITERAL_SUCCESSOR_BUNDLE_END',flush=True)
    accepted = True
    break
if not accepted:
    raise RuntimeError('No smaller exact strict110 endpoint accepted by this bounded gate')
```

### Evidentiary use of this program

A successful execution must preserve the **actual emitted literal bundle**, its byte count and hash, the defining chart hash, both exhaustive reports, the complete maximal cycles and true edges, ordinary mass integers, rational reconstruction order, witness lists, and cold-replay receipt. The numerical source trajectory alone is not an exact defining capsule.

The cold verifier does not rely on SciPy's facet grouping as proof. It reconstructs the rational contact chart, checks complete support and incidence, performs the two different exact mechanical implementations, recomputes ordinary mass, checks all weak cases, rebuilds positive primal and polar root paths, and runs malformed-boundary and translation controls. The final guard is E < 685, not a historical E686/E682 filename.

## 6. Sharply scoped unsuccessful directions

The carried-forward working context reports that aggressive conditioning toward 1e-4 could sacrifice existing positive escapes under the elastic total-deficit objective. It also reports bounded single-deletion repairs for original vertices 214 and 202 that retained extra equilibria. These observations concern those objectives, parameter choices, and bounded trajectories. They are not infeasibility certificates for the associated incidence types, and they do not exclude simultaneous regional replacement.

The larger parent-closed leaf-pruning direction is mathematically well-defined, but no inspectable completed exact endpoint from those larger proposals is supplied here. A planned retained-vertex target of 165 or 150 is not a true-edge count, an ordinary-centroid certificate, or an equilibrium census. No such proposal is promoted as C < 1000.

## 7. Continuation checkpoint

**Accepted source to resume from:** NN51_CHAIN258_PN03_C1370, actual 258/685/429, literal PN03 SHA-256 `7b04ac8b258f880034877a398528e6d777de81368f6c314d266376773373337d`.

**Concrete bounded next gate:** delete original vertex 193, repair using actual mass, recover its actual new cap, replace the complete cap while discarding obsolete internal polar requirements, then reconstruct and audit the final rational body.

**Unresolved requirement:** a returned, literal smaller defining object with two completed independent exact audits and an observed cold replay. Until those data are captured, neither a lower numerical deficit nor a lower provisional V/E/F label changes the accepted record.
