# minimum-0301

AI research report · 2026-09-28 UTC · [Export notes](../../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI report.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. [C622](../../C622/README.md) passes the supplied exact checks. See [verification status and source gaps](../../catalog/coverage.md).
<!-- historical-status:end -->

---

# FULL_WIDTH_SMALL_RATIO_ALLROOT_CHECKPOINT_AND_EXACT_INTEGER_ACCEPTANCE_V1

## 1. Strongest retained result and acceptance boundary

The retained computation reached **complete discovery of an all-root cover on a full-positive-width sector**:

```
f=(3/10,3/5,7/10),
0<beta<1,
0<C/A<=1/4,
alpha in the entire interior stack tetrahedron Delta3,
nu=(c0,c1,c2)/C in the entire interior width triangle Delta2.
```

Unlike the immediate parent's four-arrow theorem, this computation treats **all 46,410 true rooted alternatives**, not only its 256 covered trees. Unlike the balanced-width antecedent, it permits arbitrarily small positive width coordinates and arbitrarily large width ratios.

The retained discovery record is:

| Quantity | Recorded value |
|---|---:|
| Binary proof nodes | 33 |
| Closed leaves | 17 |
| Integer stress rows | 3167 |
| Row/cell applications | 13506 |
| Bernstein coefficient matrices per application | 2400 |
| Rooted systems passed to the cover | 46410 |
| Final discovery state | `DISCOVERY_COMPLETE` |

Each newly used row was subjected to exact integer acceptance during discovery, including rows reused from the developing library. The recorded complete cover would entail 32,414,400 positive-definite coefficient-matrix checks, or 97,243,200 positive leading-minor checks, in a complete standalone readback.

**I do not promote this checkpoint to a completed, source-complete theorem in this handoff.** The retained record stops before an inspectable completion result for the subsequent standalone checker and independent audit. The slow readback was stopped after discovery, and a new exact integer-lower-bound checker was started. Its terminal result, final report bytes, and audit outcome are not inspectable in the current record. I therefore give no final acceptance-stream hash, cold-replay claim, or assertion that those later stages passed.

A separate search for the entire positive `C/A` interval was also started. The last inspectable record was partial: 14 nodes and 2072 rows, with open work remaining. That is neither a full-domain exclusion nor a physical survivor.

The computational advance is consequently a **complete-discovery checkpoint for a substantial all-root sector**, with final delivery and standalone acceptance still outstanding. The accepted balanced-width theorem and immediate parent's analytic packet remain the last promoted results. No U1 or 110 body, whole-incidence subtraction, or change to `34<=C_min<=622` is claimed.

## 2. Input authority and actual source availability

The entire current journal was read consecutively through line 1644/EOF, including the complete literal immediate parent. Its identity is

```
research-journal(20260928-043409).md
323069 bytes
SHA-256 3ff78253a83d5e0258b1f4c37b971ac8f0a9e8a3ca6375e58d09ebd655d57f91.
```

The immediate parent is

```
minimum-0297
SHA-256 4fe742bd59047aa442716293285486d437e7ec34413c0513eb713bb285c8db6f.
```

Its actual-centroid curvature, directional-load corner lifting, and four-arrow theorem are retained without alteration. The new discovery does not reinterpret its 256-tree count as a full cover.

There is a useful correction to the previous source-availability status: the native antecedent archive was actually opened in this attempt, its source units extracted, their byte identities verified, and all three units read completely. The archive is

```
regular_horizon_sector_v2.zip
708510 bytes
SHA-256 e10ecfdf31d4cb1608c5777a9b58df39018a00ce9a4bd1a36ae39b4006dcbb2.
```

The recovered unchanged units are

```
regular_balanced.py, 18878 bytes
87c639ae0793f0f043265ccf31d6ef416af9d0c5cd30e3b774878261b3aa887a

regular_execute.py, 1418 bytes
6837fc9d41527cbbd1893cce9923ed764aa95e6e8ebd238cd2e0f9a9e887e458

regular_horizon_audit.py, 14645 bytes
9f6e96e03a88ddbe4ef6a00cf32d848a5a7f2a1bafc332d3591b9cd838509567.
```

Thus those bytes were genuinely available for the present computation; they were not reconstructed by guessing from hashes. This repairs availability in this execution, **not the requirement to embed all executable bytes in the immutable final payload**. No fresh rerun of the old complete balanced certificate is claimed.

## 3. Exact geometry of the new candidate sector

Use the compact normalization

```
rho=C/(3A+C),
Acompact=1-rho,
cjcompact=3rho nu_j.
```

Then `C/A<=1/4` is exactly `rho<=1/13`. The candidate domain is the closed proof product

```
beta in [0,1], rho in [0,1/13],
alpha in closed Delta3, nu in closed Delta2.
```

The genuine bodies use the appropriate operation interiors; the closed faces are included in polynomial acceptance and carry their actual limiting moments, not fictitious ten-vertex censuses.

The raw vertices are

```
Bj=(0,-beta,0),(0,1-beta,0),(0,0,1),
G=(-(1-rho),0,0),
Lj=(-(1-rho)(1-fj), fj Bj_y, fj Bj_z),
Rj=(3rho nu_j,Bj_y,Bj_z),
S=alpha0 G+alpha1 L0+alpha2 L1+alpha3 L2.
```

Labels remain `(B0,B1,B2,L0,L1,L2,R0,R1,R2,S)`. G is not an actual vertex. The true outward maximal cycles are

```
(0,3,4,1,7,6), (0,2,5,3), (0,6,8,2),
(1,4,5,2), (1,2,8,7), (3,9,4),
(3,5,9), (4,9,5), (6,7,8).
```

The true edges are

`02,03,06,12,14,17,25,28,34,35,39,45,49,59,67,68,78`.

There is no edge 01. The three parallel edges 06,17,28 remain nonzero in the regular operation interior.

With `p=63/500`, the actual six-volume and first moment are

```
dL=1-p+p alpha0,
D=(1-rho)dL+3rho,
JL=(1-rho)(G+sum Bj)
   -(1-rho)p(G+sum Lj)
   +(1-rho)p alpha0(sum Lj+S),
JRx=9rho^2(sum nu_j^2+sum_{i<j}nu_i nu_j),
JR_yz=3rho(sum Bj_yz+sum nu_j Bj_yz),
g=(JL+JR)/(4D).
```

These are the actual uniform-volume moments, checked symbolically in the compiler against the oriented boundary fan. In particular, changing nu changes the actual centroid; it is not frozen at a balanced reference. The bound `D>=437/500` holds on the entire closed proof product.

At a zero width a right label can coincide with its B label; at rho=0 all three do. These are full-dimensional convex-hull limits because D stays positive. No lower-vertex theorem or unevaluated Gamma collar is needed by the proposed explicit coefficient cover.

## 4. What the retained discovery actually tests

Let `H=diag(1,2,2)`, and define

```
Xi=H(zi-g),
Ri=4D Hzi-HJ=4D Xi,
Qij=-sym(Ri,H(zj-zi)).
```

For one physical metric M in this affine gauge,

`tr(M Qij)=-4D Dij(M)`.

The exact target of each accepted row is

`sum lambda_ij Qij > (sum lambda_ij)/2^30 * I`,

with nonnegative integer weights on true arrows. This is not an eigenvalue restriction on M. If established by a complete certificate, it excludes the selected weak arrows for every nonzero PSD M. For SPD M, true nonnegative arrows strictly increase squared norm, so a unique strict U supplies a rooted tree and is contradicted. Every stable facet and every actual same-inverse foot is then covered indirectly, without an S1 premise or an independently chosen polar metric.

The polynomial degrees remain beta 2, rho 3, total stack degree 3, and total width degree 3. Thus one row/cell application has `3*4*20*10=2400` exact Bernstein coefficient matrices. The new compiler uses **nu itself over the full triangle**, not the old balanced substitution `nu_j=1/6+theta_j/2`.

The accelerated numerical locator starts with at most 64 deterministic coefficient blocks and adds eigenvector cuts from the worst blocks. It still examines all coefficient blocks and requires exact integer row acceptance before a row is used. A failed numerical call causes subdivision; it never removes a physical parameter region. All remaining rooted alternatives pass to both closed children, and only an empty remainder can close a leaf.

The final standalone readback and independent polynomial/pullback audit are still required for the intended promoted computational handoff. Their absence here is not evidence that the candidate cover fails.

## 5. A proved exact integer-lower-bound acceptance lemma

The new readback acceleration has a small complete mathematical basis that is independent of numerical SDP outcomes.

Suppose `A_i,b` are symmetric integer coefficient matrices for arrow i and Bernstein block b, after the required rational margin shift has already been rounded conservatively. Choose a single power of two `s=2^k` for the entire cell. If k>0, define

`L_i,b=floor(A_i,b/s)-3I`,

where the floor is entrywise and symmetric. If k=0, take L=A without a correction. Then

`A_i,b >= s L_i,b`

in Loewner order. Indeed, the entrywise remainder of A/s has absolute row sums at most three, so its symmetric matrix is bounded below by -3I.

For nonnegative integer weights lambda,

`sum lambda A_i,b >= s sum lambda L_i,b`.

Therefore exact positive definiteness of all the weighted lower matrices is sufficient for the original coefficient test. A failed lower test is not rejection: evaluating the original arbitrary-size integer matrices as a fallback makes the Boolean acceptance predicate **identical** to the original exact test.

The implementation selects k so that coefficient magnitudes have at most 35 bits, checks an explicit signed-integer accumulation bound, and converts to Python integers before products forming principal minors. It never computes a determinant in overflowing fixed-width integer arithmetic. The reported lower-matrix minor stream can differ from an original-coefficient minor stream; those streams must not be falsely identified byte-for-byte.

This is an exact certificate-evaluation method, not a new geometric relaxation. It can accelerate a large readback without weakening the theorem that a successful readback proves.

### Complete standalone reference implementation of the lemma

The following source is complete and needs only Python's standard library. It reconstructs the acceptance predicate for a supplied integer coefficient array and row, including exact fallback. Its self-test is algebraic, not a polyhedral census. This reference unit is not claimed to have been executed in the resumed record.

```python
#!/usr/bin/env python3
"""Exact lower-coefficient acceptance, standard-library reference version.
Input convention: arrows[arrow_index][block_index] is a symmetric matrix
packed as (A00,A01,A02,A11,A12,A22), all entries exact Python integers.
A row is a sequence of (arrow_index, positive_integer_weight).
The required geometric margin must already be included in the input array.
"""
import json
import sys
from pathlib import Path


def leading_minors(v):
    a,b,c,d,e,f = map(int,v)
    second = a*d-b*b
    third = second*f+2*b*c*e-a*e*e-d*c*c
    return a,second,third


def weighted_blocks(arrows,row):
    blocks = len(arrows[0])
    for k in range(blocks):
        yield tuple(sum(w*arrows[i][k][j] for i,w in row)
                    for j in range(6))


def positive_minima(arrows,row):
    minimum = None
    for block in weighted_blocks(arrows,row):
        m = leading_minors(block)
        if min(m) <= 0:
            return None
        minimum = m if minimum is None else tuple(min(x,y)
                    for x,y in zip(minimum,m))
    return minimum


def exact_accept(arrows,row,bits=35):
    if type(bits) is not int or bits < 2:
        raise ValueError('bits must be an integer >=2')
    if not arrows or not arrows[0]:
        raise ValueError('nonempty coefficient array required')
    block_count = len(arrows[0])
    for arrow in arrows:
        if len(arrow) != block_count:
            raise ValueError('inconsistent block counts')
        for block in arrow:
            if len(block) != 6 or any(type(x) is not int for x in block):
                raise ValueError('coefficient entries must be exact integers')
    row = tuple(tuple(a) for a in row)
    if (not row or len({a[0] for a in row}) != len(row)
        or any(len(a) != 2 or type(a[0]) is not int or type(a[1]) is not int
               or not 0 <= a[0] < len(arrows) or a[1] <= 0 for a in row)):
        raise ValueError('invalid nonnegative arrow row')
    magnitude_bits = max(abs(x).bit_length()
                         for arrow in arrows for block in arrow for x in block)
    shift = max(0,magnitude_bits-bits)
    if not shift:
        m = positive_minima(arrows,row)
        return dict(accepted=m is not None,route='original',shift=0,minima=m)
    scale = 1 << shift
    lower = []
    for arrow in arrows:
        blocks = []
        for block in arrow:
            a = [x//scale for x in block]
            for j in (0,3,5):
                a[j] -= 3
            blocks.append(tuple(a))
        lower.append(tuple(blocks))
    m = positive_minima(lower,row)
    if m is not None:
        return dict(accepted=True,route='integer_lower',shift=shift,minima=m)
    m = positive_minima(arrows,row)
    return dict(accepted=m is not None,route='original_fallback',shift=shift,minima=m)


def self_test():
    large = 1 << 120
    a = [[(large,0,0,large,0,large)]]
    assert exact_accept(a,[(0,1)])['accepted']
    b = [[(large,large-1,0,large,0,large)]]
    result = exact_accept(b,[(0,1)])
    assert result['accepted'] and result['route']=='original_fallback'
    c = [[(large,large+1,0,large,0,large)]]
    assert not exact_accept(c,[(0,1)])['accepted']
    d = [[(large,0,0,-large,0,large)],
         [(0,0,0,2*large,0,0)]]
    assert exact_accept(d,[(0,1),(1,1)])['accepted']
    print('EXACT_INTEGER_LOWER_ACCEPTANCE_REFERENCE_PASS')


if __name__=='__main__':
    if not __debug__:
        raise RuntimeError('Assertions must remain enabled')
    if len(sys.argv)==1:
        self_test()
    elif len(sys.argv)==2:
        data=json.loads(Path(sys.argv[1]).read_text())
        print(json.dumps(exact_accept(data['arrows'],data['row']),sort_keys=True))
    else:
        raise SystemExit('Use no arguments for self-test, or one exact input JSON')
```

## 6. Recovery state of the substantive checkpoint

The retained files are available at the following previously established paths:

Completed-discovery small-sector certificate (`certificate.json`)

Full-width compiler, locator and recursive checker (`fullwidth_fast.py`)

Exact integer-lower checker driver (`quant_execute.py`)

Independent geometry, polynomial and physical audit (`fullwidth_audit.py`)

Original balanced-width native source archive (`regular_horizon_sector_v2.zip`)

The recorded environment was CPython3.13.5, NumPy2.3.5, SciPy1.17.0 and SymPy1.14.0 with `OPENBLAS_NUM_THREADS=1`. There was no random seed. The current source defines all geometry, degrees, margin, tree order, cut tolerances, integer-weight rounding and subdivision rules.

The intended definitive commands are

```sh
OPENBLAS_NUM_THREADS=1 python -B quant_execute.py check fast_small/certificate.json
OPENBLAS_NUM_THREADS=1 python -B fullwidth_audit.py fast_small/certificate.json
```

A fresh source-only reconstruction uses

```sh
OPENBLAS_NUM_THREADS=1 python -B quant_execute.py build small fresh_small
OPENBLAS_NUM_THREADS=1 python -B quant_execute.py check fresh_small/certificate.json
OPENBLAS_NUM_THREADS=1 python -B fullwidth_audit.py fresh_small/certificate.json
```

The source-only directory must contain the complete compiler, driver and audit units. The final result must compare the regenerated certificate and definitive reports, not just the `DISCOVERY_COMPLETE` flag.

**Delivery limitation:** those substantive source bytes and all candidate rows are not embedded in this `result_markdown`. The links are continuation conveniences, not a replacement for the requested inline recovery capsule. The new all-root object therefore remains an **unpromoted computational checkpoint rather than a durable source-complete successor**. No byte count or SHA-256 for its final source/report set is assigned without an inspectable final readback.

This limitation does not erase the actual complete discovery, nor does it turn the checkpoint into a physical counterexample. It specifies exactly which evidence is missing for promotion.

## 7. Controls, negative outcomes and the remaining problem

No new physical U1 or joint110 survivor was constructed. The old actual extreme-width 323 control remains valid in its original scope: it refutes the transported stress `5D03+10D35+4D54`, not all possible stresses. It lies at rho=1/2 and is outside the small-ratio candidate sector, so the proposed small-sector cover would not settle its entire affine metric orbit.

The initial dense-constraint discovery attempts were stopped without complete certificates. Their remaining trees were library or solver residues, not physical feasible systems. The later 64-block cutting-plane locator reached complete discovery for the small sector while retaining exact acceptance of every used row. This is a numerical-discovery improvement, not a modification of the actual-body relaxation.

The entire positive `C/A` search has no inspectable terminal outcome here. Nothing beyond `C/A<=1/4` may be inferred from the small-sector checkpoint. Free left cuts, finite-ghost motion, and full-incidence shape freedom remain outside its geometry.

The next decisive step is the definitive exact readback and independent audit of the already completed small-sector discovery, followed by source-complete immutable preservation. If those stages pass, the resulting theorem will cover **all beta, all stack positions and the entire positive width simplex** on `0<C/A<=1/4`, thereby replacing the immediate parent's selected-packet conclusion on that range with an all-root result. Until that evidence is preserved, the accepted analytical and balanced-width parents remain authoritative.
