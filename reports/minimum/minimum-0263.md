# minimum-0263

AI research report · 2026-09-27 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# H5_WIDE_XR_CONTINUATION_READBACK_LIMITED_V1

## Status

**This handoff does not certify a new excluded region or a new feasible full tree.** The last verified, reconstructible regional result remains the primary parent `minimum-0256`, SHA-256 `9e71d008aa4b1d85333f293fd38dd05ab80a944563fa4e8fb4c5509dfcebb28e`.

I attempted a substantially wider all-root computation and prepared an exact validation route, but live tool responses in this continuation were replaced by `Skipped ... message` placeholders. This affected even a one-line echo test, filesystem inspection, computation logs, and the attempted image readback. I therefore cannot distinguish an unobserved successful execution from an unobserved failure, attest that the proposed atlas finished, or report new counts, numerical guards, byte counts, or hashes as verified results.

The attempted worktree was `/mnt/data/h5_wide`. That path is a **recovery lead, not confirmation that the files exist**. No sandbox download link is asserted here.

## 1. Input-reading and source-authority limitation

The retained reading record from the preceding unfinished attempt reaches line 1038 of the 2333-line new journal. I requested the remaining consecutive ranges through EOF, including both complete literal parent payloads, but those readbacks also appeared only as skipped-message placeholders. Consequently I cannot honestly attest a completed reading of lines 1039–2333 in this execution.

The expected new-journal manifest supplied by the user is:

```text
research-journal(20260926-235119).md
381278 bytes
d93d7d21bcaadb4de6dbe640276b90587888830dbe30a2bf8a5974dbc3ce7f17
```

These are the supplied manifest values, not a newly observed successful checksum comparison.

The unchanged optimal-floor and finite-height inputs, and the primary parent's source-only recovery, remain available from the earlier conversation. Their previous reading and accepted results were retained. The new companion is identified as `minimum-0255`, SHA-256 `b02e9ea175553f06a5fc27b626e52977c8baf76d50df0e70d68eff5fb913393e`; its summary was available in the retained notebook reading, but its complete new literal payload cannot be claimed as newly read here. No conflict between literal sources is asserted, and no unprovided research connector or archive was used.

## 2. Target chosen for the continuation

The proposed enlarged basal region is

```text
1/5 <= x,r <= 4/5,
1/5 <= p,q <= 1/2,
p+q < 1.
```

The proposed new computation covers the middle taper

```text
1/20 <= lambda <= 3/5.
```

It retains the **entire parent p/q square**, rather than narrowing it to obtain an easier high-x or high-r control. Both x and r interval widths would double relative to the closed central cube. The four-dimensional basal parameter volume would therefore be four times that of the central cube; this is only a parameter-space comparison, not a canonical-class count or an affine-invariant measure.

The already proved central parent covers the lower/lower x/r subbox. The genuinely new part to certify is the closed L-shaped region

```text
max(x,r) >= 1/2
```

inside the displayed enlarged box. Shared boundary faces are allowed to overlap the old region.

The spectral condition remains exactly the optimal floor inherited from the primary parent:

```text
p0 = 7024915/1000000,
q0 = 6832329/1000000,
D0 = p0*q0+q0+1 = 11165771895407/200000000000,
ell = 1/D0,
alpha = 1/(D0-3),
H = Sigma^(1/2) M Sigma^(1/2) / tr(Sigma M) >= ell I.
```

Sigma must be the moving actual homogeneous covariance of the same ten-vertex body. This floor contains the necessary finite-height adjacent-ratio cone, but it is **not the full condition48 cone**. For example, the formal normalized spectrum `(48,48,1)/97` has condition48 but lies below the floor. Conversely, `(D0-2,1,1)/D0` lies in the floor and has condition greater than48. Neither formal spectrum is an assertion of a feasible H5 arrow tree.

A successful middle-taper atlas, combined with the primary central theorem, would give conditional U>=2 on the whole enlarged middle-taper box. An all-taper joint conclusion would additionally use the companion's reported WIDE lower-taper theorem and the accepted all-basal upper-taper exclusion. That combination is **not promoted to a proved new conclusion here**: the new atlas has not been observably validated, and the new companion's complete literal reading remains unfinished.

## 3. Exact parameter decomposition prepared

Set `m=1/2` and `c=7/20`. Seven direct root boxes suffice for the new region.

First take

```text
x in [1/2,4/5], r in [1/5,1/2],
```

and all four products of the p and q intervals `[1/5,7/20]` and `[7/20,1/2]`. These are four direct boxes, called HL below. Reflecting the whole bodies gives the corresponding low-x/high-r boxes.

Next take

```text
x,r in [1/2,4/5]
```

and the three p/q products low/low, low/high, and high/high. These are three direct boxes, called HH below. Whole-body reflection supplies the missing high/low p/q product.

Every direct box has the full taper `[1/20,3/5]`. The exact reflection is

```text
(x,r,p,q,lambda) -> (r,x,q,p,lambda),
(X,Y,Z) -> (Y,X,Z),
vertex permutation pi=(5,4,3,2,1,0,6,7,9,8).
```

The literal vertex formulas give `Z_i(reflected theta)=R Z_pi(i)(theta)`. Therefore the actual centroid and covariance transform as `g'=Rg` and `Sigma'=R Sigma R^T`; with the pulled-back physical metric, every original arrow derivative is preserved. The reflection also preserves the nine true maximal facets and the seventeen true edges. This is reflection of the entire actual body and metric, not reflection of a packet at a frozen geometry.

Together with the inherited lower/lower x/r box, these seven boxes and their specified reflections form a complete closed parameter cover of the proposed enlarged box. This decomposition is a valid bookkeeping reduction. It is **not**, by itself, an exclusion proof.

## 4. Computation attempted, without an observed verdict

The attempted generator reused the primary parent's cancellation-preserving moment compiler and optimal scalar map. It selected the first 1024 literal integer certificates from the primary atlas, then added their whole-body reflected packets. This was a finite initial proposal library, not an assumption that those weights remain valid on the new region.

The exact parent atlas from which that seed was to be extracted is:

```text
h5_floor_atlas.json
5600262 bytes
aba157dc06fde52307bf82866600fa6b969282b820dfe79087d3f4a3dbb78927
```

Seven independent jobs were prepared so that each job's traversal and weight proposals would be independent of process scheduling. The intended configuration was CPython3.13.5, NumPy2.3.5, SciPy1.17.0, with one OpenBLAS thread per job. The attempted numerical screening used floating Sylvester expressions to discard obviously unsuitable stored packets, followed by exact integer checks for every accepted packet. A screen could only skip a proposal; it could not certify a packet.

The attempted subdivision and acceptance parameters followed the parent: 80-bit outward dyadic arithmetic; rational midpoint covariance preconditioning; 32 corners of an affine **lower Taylor model**, not 32 nonlinear samples; 70 LP cutting iterations; at most2000 proposal calls per cell; midpoint subdivision by largest weighted width, with taper weight2; and maximum subdivision depth32. Locator or enclosure failure was to cause subdivision. Exhausting a limit was to raise an error with **no feasibility conclusion**.

The intended worktree units were:

```text
h5_floor_core.py
poly_moments.py
wide_seed.json
wide_search.py
wide_verify.py
wide_controls.py
```

The intended generator outputs were `wide_job_0.json` through `wide_job_6.json`, followed by `wide_atlas.json`. The intended exact output was `wide_report.json`. These filenames are not claims that completed files were observed. In particular, no progress percentage, completed-cell count, certificate count, or success marker from that attempted run is treated as evidence in this handoff.

The source-only archive creation was also attempted, but its readback was likewise unavailable. It is not presented as a verified recovery artifact.

## 5. Exact acceptance criterion to retain

For original centered true-edge tensors

```text
A_e = sym((Z_i-g)(Z_j-Z_i)^T),
Q = -sum_e w_e A_e,
t = tr(Sigma^-1 Q),
P = Q+alpha*t*Sigma,
```

the inherited identity at `tr(Sigma M)=1` is

```text
tr(MQ) = tr((H-ell I) Sigma^-1/2 P Sigma^-1/2).
```

Thus a positive-definite P rejects the selected weak arrows throughout the floor cone. If a cell proves

```text
P/(sum w) >= delta I,
Sigma <= R I,
```

then the normalized negative-arrow mean is at least

```text
delta*(D0-3)/(R*D0).
```

Every rooted tree must contain a packet with this exact positive certificate. A failed finite library is not a feasible tree. Nor is a feasible sparse packet a substitute for one common SPD metric satisfying a complete rooted tree.

The following independent, optimizer-free validation unit is preserved as a **durable exact patch** against the primary parent's two named source dependencies. It can validate a compatible completed `wide_atlas.json` should the attempted worktree be recoverable. It does not generate an absent atlas, and no execution of its final pass marker is claimed here.

Its actual dependencies are the unchanged primary sources:

```text
h5_floor_core.py
8083 bytes
5cc97f945b963a87d651d41e529c3206a65664b702922564b1862de509a0be6d

poly_moments.py
3098 bytes
70256230321e1cc00fa1d4bcf43db89bcd52c1755dce44a84938471eb467f3a2
```

They are reconstructed by the primary parent's complete `recover_h5_floor.py` already supplied in this conversation. They are real source dependencies, not inferred library contents. The validator checks their hashes before import. Its additional input is an **untrusted** completed atlas: every packet, every lower-model matrix, every direct tree cover, the reflection map, and the complete new partition are checked anew.

### validate_h5_wide_attempt.py

```python
"""Optimizer-free validator for the attempted wide H5 atlas.
Dependency: the exact primary h5_floor_core.py and poly_moments.py below.
CPython 3.13.5 standard library; assertions must be enabled.
This source has not received an observable execution receipt in this handoff.
"""
from pathlib import Path
from fractions import Fraction as F
from itertools import product
from functools import reduce
import hashlib
import json
import sys

PINS = {
    'h5_floor_core.py':
        '5cc97f945b963a87d651d41e529c3206a65664b702922564b1862de509a0be6d',
    'poly_moments.py':
        '70256230321e1cc00fa1d4bcf43db89bcd52c1755dce44a84938471eb467f3a2',
}
for name, pin in PINS.items():
    assert hashlib.sha256(Path(name).read_bytes()).hexdigest() == pin

from h5_floor_core import (
    ARROWS, EDGES, FACETS, BITS, UNIT, DEN, ALPHA,
    compile_box, trees, mat, minors,
)

LOW = tuple(map(F, ('1/5','1/5','1/5','1/5','1/20')))
HIGH = tuple(map(F, ('4/5','4/5','1/2','1/2','3/5')))
MID = F(1,2)
CUT = F(7,20)
PI = (5,4,3,2,1,0,6,7,9,8)
PARENT = 'minimum-0256'
PARENT_SHA = '9e71d008aa4b1d85333f293fd38dd05ab80a944563fa4e8fb4c5509dfcebb28e'
PARENT_GAP = F(1,1 << 28)


def encoded(x):
    if isinstance(x, F):
        return str(x)
    if isinstance(x, dict):
        return {str(k): encoded(v) for k,v in x.items()}
    if isinstance(x, (list,tuple)):
        return [encoded(v) for v in x]
    return x


def root_boxes():
    out = []
    for sector in ('HL','HH'):
        for p,q in product(range(2), repeat=2):
            if sector == 'HH' and p > q:
                continue
            lo = (
                MID, LOW[1] if sector == 'HL' else MID,
                LOW[2] + p*(CUT-LOW[2]),
                LOW[3] + q*(CUT-LOW[3]), LOW[4],
            )
            hi = (
                HIGH[0], MID if sector == 'HL' else HIGH[1],
                CUT + p*(HIGH[2]-CUT),
                CUT + q*(HIGH[3]-CUT), HIGH[4],
            )
            out.append((sector,lo,hi))
    assert len(out) == 7
    return out


def reflected(a):
    return (a[1],a[0],a[3],a[2],a[4])


def mirror_required(lo, hi):
    return hi[1] <= MID or (
        lo[1] >= MID and hi[2] <= CUT and lo[3] >= CUT
    )


def box_volume(lo, hi):
    return reduce(lambda a,b: a*b,
                  (b-a for a,b in zip(lo,hi)), F(1))


def partition_check(new_boxes):
    assert len(new_boxes) == len(set(new_boxes))
    anchor = (LOW, (MID,MID,HIGH[2],HIGH[3],HIGH[4]))
    assert anchor not in new_boxes
    assert all(lo[0] >= MID or lo[1] >= MID
               for lo,hi in new_boxes)
    leaves = list(new_boxes) + [anchor]
    assert all(all(LOW[k] <= lo[k] < hi[k] <= HIGH[k]
                   for k in range(5)) for lo,hi in leaves)

    def visit(lo, hi, boxes):
        if len(boxes) == 1:
            assert boxes[0] == (lo,hi)
            return
        for j in range(5):
            middle = (lo[j]+hi[j])/2
            if all(b[j] <= middle or a[j] >= middle
                   for a,b in boxes):
                left = [v for v in boxes if v[1][j] <= middle]
                right = [v for v in boxes if v[0][j] >= middle]
                assert left and right
                assert len(left)+len(right) == len(boxes)
                lh = hi[:j]+(middle,)+hi[j+1:]
                rl = lo[:j]+(middle,)+lo[j+1:]
                visit(lo,lh,left)
                visit(rl,hi,right)
                return
        raise AssertionError('Incomplete or overlapping closed partition')

    visit(LOW,HIGH,leaves)
    assert sum(box_volume(a,b) for a,b in leaves) == box_volume(LOW,HIGH)
    return {
        'new_parameter_volume': sum(box_volume(a,b) for a,b in new_boxes),
        'inherited_parameter_volume': box_volume(*anchor),
        'inherited_box': anchor,
        'inherited_parent': PARENT,
        'inherited_parent_sha256': PARENT_SHA,
    }


def determinant(a):
    a = [list(map(F,row)) for row in a]
    result = F(1)
    for k in range(len(a)):
        j = next(j for j in range(k,len(a)) if a[j][k])
        if j != k:
            a[k],a[j] = a[j],a[k]
            result = -result
        pivot = a[k][k]
        result *= pivot
        for i in range(k+1,len(a)):
            factor = a[i][k]/pivot
            for j in range(k+1,len(a)):
                a[i][j] -= factor*a[k][j]
    return result


def validate(path):
    raw = Path(path).read_bytes()
    data = json.loads(raw)
    assert data['identity'] == 'H5_OPTIMAL_FLOOR_WIDE_XR_ATLAS_V1'
    assert data['status'] == 'COMPLETE_UNVERIFIED'
    assert data['bits'] == BITS == 80
    assert data['alpha'] == str(ALPHA)
    assert data['den'] == str(DEN)
    assert tuple(map(F,data['domain_lo'])) == LOW
    assert tuple(map(F,data['domain_hi'])) == HIGH
    assert DEN > 3 and ALPHA/(1+3*ALPHA) == 1/DEN
    roots = root_boxes()
    assert [(s,tuple(map(F,a)),tuple(map(F,b)))
            for s,a,b in data['roots']] == roots

    assert len(EDGES) == 17 and len(FACETS) == 9 and len(ARROWS) == 34
    assert {frozenset(PI[i] for i in f) for f in FACETS} == {
        frozenset(f) for f in FACETS
    }
    am = tuple(ARROWS.index((PI[i],PI[j])) for i,j in ARROWS)
    assert all(am[am[i]] == i for i in range(34))
    tr = trees()
    assert len(tr) == len(set(tr)) == 48790
    ts = set(tr)
    assert all((PI[r],tuple(sorted(am[i] for i in t))) in ts for r,t in tr)
    lap = [[F(0)]*10 for _ in range(10)]
    for i,j in EDGES:
        lap[i][i] += 1
        lap[j][j] += 1
        lap[i][j] -= 1
        lap[j][i] -= 1
    assert determinant([r[:-1] for r in lap[:-1]]) == 4879

    certs = data['certificates']
    assert len({tuple(map(tuple,c)) for c in certs}) == len(certs)
    allbits = (1 << len(tr))-1
    arrowbits = [0]*34
    for j,(r,t) in enumerate(tr):
        for i in t:
            arrowbits[i] |= 1 << j
    hits = []
    reflected_hits = []
    for cert in certs:
        assert cert and len({i for i,w in cert}) == len(cert)
        assert all(type(i) is int and 0 <= i < 34
                   and type(w) is int and w > 0 for i,w in cert)
        hit = rhit = allbits
        for i,w in cert:
            hit &= arrowbits[i]
            rhit &= arrowbits[am[i]]
        assert hit and rhit
        hits.append(hit)
        reflected_hits.append(rhit)

    new_boxes = []
    records = []
    used = set()
    reflected_cells = 0
    direct_uses = reflected_uses = 0
    minimum_gap = None
    table_stream = hashlib.sha256()
    for cell in data['cells']:
        root = cell['root']
        assert type(root) is int and 0 <= root < len(roots)
        lo,hi = tuple(map(F,cell['lo'])),tuple(map(F,cell['hi']))
        sector,a,b = roots[root]
        assert all(a[k] <= lo[k] < hi[k] <= b[k] for k in range(5))
        chosen = cell['certificates']
        assert chosen and len(chosen) == len(set(chosen))
        rows,info = compile_box(lo,hi)
        assert len(rows) == 34 and all(len(r) == 32 for r in rows)
        table_raw = (json.dumps(rows,separators=(',',':'))+'\n').encode()
        table_stream.update(hashlib.sha256(table_raw).digest())
        covered = rcovered = 0
        delta = None
        for j in chosen:
            assert type(j) is int and 0 <= j < len(certs)
            used.add(j)
            covered |= hits[j]
            rcovered |= reflected_hits[j]
            cert = certs[j]
            weight = sum(w for i,w in cert)
            for k in range(32):
                row = [sum(w*rows[i][k][h] for i,w in cert)
                       for h in range(6)]
                mm = minors(mat(row))
                assert min(mm) > 0
                trace = row[0]+row[3]+row[5]
                bound = F(4*mm[2],UNIT*trace*trace*weight)
                delta = bound if delta is None else min(delta,bound)
        assert covered == allbits
        radius = F(info['covariance_norm_upper'])
        gap = delta*(DEN-3)/(radius*DEN)
        assert gap > 0
        minimum_gap = gap if minimum_gap is None else min(minimum_gap,gap)
        new_boxes.append((lo,hi))
        direct_uses += len(chosen)
        is_mirror = mirror_required(lo,hi)
        if is_mirror:
            assert rcovered == allbits
            new_boxes.append((reflected(lo),reflected(hi)))
            reflected_cells += 1
            reflected_uses += len(chosen)
        records.append({
            'lo':lo, 'hi':hi, 'root':root,
            'certificate_uses':len(chosen),
            'covered_rooted_trees':48790,
            'reflected_copy':is_mirror,
            'normalized_negative_arrow_gap':gap,
        })
    assert used == set(range(len(certs)))
    partition = partition_check(new_boxes)
    combined_gap = min(minimum_gap,PARENT_GAP)
    power = 0
    while F(1,1 << power) > combined_gap:
        power += 1
    result = {
        'identity':'H5_WIDE_ATTEMPT_OPTIMIZER_FREE_VALIDATION_V1',
        'status':'PASS',
        'input_atlas_bytes':len(raw),
        'input_atlas_sha256':hashlib.sha256(raw).hexdigest(),
        'direct_cells':len(records),
        'reflected_cells':reflected_cells,
        'new_cells':len(new_boxes),
        'direct_certificate_uses':direct_uses,
        'reflected_certificate_uses':reflected_uses,
        'direct_PD_corner_matrices':32*direct_uses,
        'direct_positive_leading_minors':96*direct_uses,
        'new_raw_tree_cell_combinations':48790*len(new_boxes),
        'new_exact_uniform_gap':minimum_gap,
        'combined_middle_taper_dyadic_gap':F(1,1 << power),
        'spectral_floor':1/DEN,
        'partition':partition,
        'cells':records,
        'table_digest_stream_sha256':table_stream.hexdigest(),
        'scope':'Conditional U>=2 in the stated actual covariance floor. '
                'The lower/lower x/r anchor uses the named accepted parent. '
                'No full-condition48, unrestricted-U2, or global-minimum claim.',
    }
    output = (json.dumps(encoded(result),sort_keys=True,indent=2)+'\n').encode()
    Path('wide_validation.json').write_bytes(output)
    print(len(output),hashlib.sha256(output).hexdigest())
    print('H5_WIDE_ATTEMPT_VALIDATED_PASS')


if __name__ == '__main__':
    validate(sys.argv[1] if len(sys.argv) > 1 else 'wide_atlas.json')
```

The validation command is:

```sh
python -B -S validate_h5_wide_attempt.py wide_atlas.json
```

`H5_WIDE_ATTEMPT_VALIDATED_PASS` is the marker that this source is designed to emit after all assertions pass. It is **not an observed terminal marker from this continuation**. No new validator-source or output checksum is advertised, because its execution and checksum readback could not be observed. The complete source above, rather than an invented pin, is the preserved patch.

## 6. Additional candidate-control method prepared

A rational covariance-orthogonal construction was prepared to obtain genuine weak-wall tests without relying on floating eigenvalues. It is useful independently of the numerical atlas but does not supply a verified new census here.

At any fixed rational actual covariance Sigma, choose a rational Sigma-orthogonal basis by Gram–Schmidt starting with `u0=e_z`, then `e_x`, then `e_y`. Define

```text
B_k = u_k*u_k^T/(u_k^T Sigma u_k).
```

Then `sum B_k=Sigma^-1`, and

```text
M_raw(c,b)=c*B0+B1+b*B2
```

has covariance-weighted eigenvalues exactly `(c,1,b)`. For a target true arrow e=(i,j), put

```text
a_k = (Z_i-g)^T B_k (Z_j-Z_i).
```

When `a0!=0`, the rational choice

```text
c=-(a1+b*a2)/a0
```

makes that original arrow exactly zero. Positive c,b give SPD; sorting `(c,1,b)` gives exact rational adjacent-ratio tests. A full actual-inverse audit is still required: an isolated zero primitive is not automatically a physical weak equilibrium.

The attempted control geometry was

```text
theta=(13/20,7/10,2/5,1/3,2/5),
```

with target arrows `(1,8)` and `(7,6)`. The attempted exact finite search used `b=k/20`, `k=1,...,160`, and required both strict finite-height adjacent caps and negative remaining outgoing derivatives at the source vertex. No selected b value, covariance spectrum, equilibrium count, or weak-point count from that attempted run is promoted to a verified construction. These candidates remain unverified recovery leads, not proper110 or complete-tree witnesses.

## 7. Strongest supported conclusion and continuation

The supported new contribution in this limited execution is the explicit seven-box/reflection decomposition and a complete optimizer-free validator for the proposed wider computation. **The actual wider exclusion remains pending observable exact acceptance.** The old central theorem and the accepted bounds remain unchanged.

The next executor should first restore readable tool output and finish the literal companion/journal reading. It should then inspect, rather than assume, the attempted `wide_job_*.json`, `wide_atlas.json`, source files, and logs. A completed compatible atlas can be checked with the source above; partial checkpoints must not be described as full-region coverage. If no attempted worktree is recoverable, the primary parent's complete source-only recovery remains the last durable computational starting point.

No negative numerical result has been interpreted as an exclusion, no sparse packet has been substituted for a complete tree, and no canonical count or minimum bound has been changed. The attempted new atlas and candidate controls are explicitly **not a durable verified successor** to the primary parent.
