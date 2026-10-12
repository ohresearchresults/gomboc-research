# minimum-0297

AI research report · 2026-09-28 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# REGULAR_RIGHT_HORIZON_FULL_WIDTH_PACKET_AND_CENTROID_REDUCTION_V1

## 1. Determination and its limits

**The full positive-width all-root problem is not closed in this handoff. No actual U1 survivor is claimed.** The accepted balanced-width theorem remains unchanged.

There is, however, a new exact full-width mechanical result. At the same cuts `(3/10,3/5,7/10)`, throughout

```
1/3 <= beta <= 1/2,
0 < C/A <= 1/4,
all positive right-width triples c with sum c=C,
all interior stack barycentrics alpha in Delta3,
```

the four genuine weak arrows

```
0 -> 3,  1 -> 4,  2 -> 5,  3 -> 5
```

are jointly impossible under every nonzero PSD metric. The entire positive width simplex is included, not just the balanced cone, and no bound on metric conditioning or fixed centroid is used.

After the affine normalization `A=1`, define

```
w03=1-10*beta/7,
w14=5*beta/2,
w25=7/3,
w35=1.
```

All four weights are positive on the stated beta interval. The quantitative conclusion is

`w03 D03(M)+w14 D14(M)+w25 D25(M)+D35(M) < -tr(M)/10000`.

For an unnormalized A, the right side is `-tr(M diag(A^2,1,1))/10000` in the original coordinates. The metric is transported by the affine normalization, not reset to a Euclidean metric.

This is a seven-dimensional continuous **packet sector**, not an all-root body exclusion. Exactly **256** of the 46,410 labelled rooted trees contain this packet: 64 rooted at 4, 128 rooted at 5, and 64 rooted at 9. The other **46,154** alternatives are not excluded by this new packet. Within the balanced cone they are already excluded by the accepted antecedent; outside that cone this handoff does not determine their feasibility.

Two reusable full-width results accompany the packet:

* The actual volume centroid, with the other parameters fixed, is an explicitly determined strictly convex paraboloid over its two transverse coordinates. This gives an exact width-transfer identity and prevents treating the three centroid coordinates as independent.
* A stress supported away from the right vertices, with weighted displacement opposite the parallel edges, lifts from the three zero-width-corner bodies to the entire width simplex by an exact positive-semidefinite remainder. More generally, positivity of a fixed stress over the whole width triangle has an exact tangential-block/degree-five determinant reduction. It need not be tested through positivity of all width Bernstein matrix coefficients.

These are analytic results with complete literal rational certificates below. **No new numerical full-root cover, source-only execution, certificate hash, or physical survivor census is promoted.** The global bound and incidence registry are unchanged.

## 2. Input and computational-source status

The carried-forward reading record covers the entire current journal through line 1293/EOF, including the literal parent. The supplied journal is 307553 bytes, SHA-256

`2e5ce1a96ddbc2ef12e07556544cbe84c275606f359dafe0c72001727ba6918e`.

The accepted antecedent is

`minimum-0292`,

SHA-256

`060c67f6b1f274596cdca1b6f4f3838b663d34a0d10d2d15744807922b03580d`.

Its all-root balanced-width theorem is a working premise, not a new replay claim here. The original geometric capsule remains authoritative for the operation, true incidence, and actual moments.

The three original computational units are preserved in the previously supplied native archive/source-complete payload. Their expected identities are

```
regular_balanced.py       18878 bytes
87c639ae0793f0f043265ccf31d6ef416af9d0c5cd30e3b774878261b3aa887a

regular_execute.py        1418 bytes
6837fc9d41527cbbd1893cce9923ed764aa95e6e8ebd238cd2e0f9a9e887e458

regular_horizon_audit.py  14645 bytes
9f6e96e03a88ddbe4ef6a00cf32d848a5a7f2a1bafc332d3591b9cd838509567.
```

No usable fresh extraction or execution receipt is available in this resumed record. Consequently I do **not** claim that their byte-identical inline restoration has been completed. Section 9 supplies a complete hash-checked extraction program for the already supplied native inputs; it does not guess or reimplement the antecedent. That program still requires the native source archive or source-complete result file. **This response therefore does not repair the antecedent's standalone-inline source-delivery gap by itself.** Its last accepted computational record remains the antecedent, with its existing qualifications.

The new analytic packet certificate is independent of that gap: all of its geometry, weights, estimates, matrices, and verification source are included here. No old executable or saved certificate is a dependency of the new source.

## 3. Actual geometry over the full width simplex

Normalize A to 1 and write `q=C/A`. Let

```
f=(3/10,3/5,7/10), p=prod f=63/500,
alpha=(t,alpha1,alpha2,alpha3), sum alpha=1,
nu=(nu0,nu1,nu2), sum nu=1,
c_j=q*nu_j.
```

For genuine members, `0<beta<1`, `q>0`, and both barycentric vectors are interior. The proof below also uses their closed parameter boundaries as indexed limits.

Set

```
B0=(0,-beta,0), B1=(0,1-beta,0), B2=(0,0,1),
G=(-1,0,0),
Lj=(-(1-fj), fj Bj_y, fj Bj_z),
Rj=(q nu_j, Bj_y, Bj_z),
S=tG+alpha1 L0+alpha2 L1+alpha3 L2.
```

The ten actual labels are `(B0,B1,B2,L0,L1,L2,R0,R1,R2,S)`. G is a ghost point, not an actual vertex. The complete outward maximal cycles are

```
(0,3,4,1,7,6), (0,2,5,3), (0,6,8,2),
(1,4,5,2), (1,2,8,7), (3,9,4),
(3,5,9), (4,9,5), (6,7,8).
```

The true edges are

`02,03,06,12,14,17,25,28,34,35,39,45,49,59,67,68,78`.

There is no edge 01. The regular horizon has three nonzero parallel edges 06,17,28 and remains 10/17/9 in the operation interior.

Let D be six-volume and J be 24 times the first volume moment. Put

```
d=1-p+p*t,
D=d+q,
JL=G+sum Bj-p*(G+sum Lj)+p*t*(sum Lj+S),
JRx=q^2*(sum nu_j^2+sum_{i<j}nu_i*nu_j),
JR_yz=q*(sum Bj_yz+sum nu_j Bj_yz),
J=JL+JR,
g=J/(4D).
```

This is the actual homogeneous volume centroid. The left terms are actual full, removed, and added tetrahedral moments. The right terms integrate the positive affine wedge height over the projected triangle. In particular D is independent of nu, while J is not. The new source verifies these moment identities against oriented-boundary integration, rather than assuming a vertex-mass representation.

On the packet sector, `437/500<=d<=1` and `437/500<=D<=5/4`, so every closed proof limit has positive volume.

## 4. Exact full-width centroid and stress-transfer identities

These identities hold for every q>0 and every allowed left shape, not just for q<=1/4.

Write `m=sum nu_j Bj_yz`. Then

```
g_yz=(JL_yz+q sum Bj_yz+q m)/(4D),
gx=JLx/(4D)+q^2*(1+sum nu_j^2)/(8D).
```

The two transverse centroid coordinates determine m, and hence determine the widths uniquely:

```
nu2=m_z,
nu1=m_y+beta*(1-m_z),
nu0=(1-beta)*(1-m_z)-m_y.
```

Thus the actual width-centroid image is a two-dimensional paraboloid, not a three-dimensional freely assignable centre set. With g_y and g_z as coordinates, the Hessian of g_x is exactly

```
4D * ((2,             1-2 beta),
      (1-2 beta, 2(beta^2-beta+1))).
```

Its determinant is `48 D^2>0`. This is an actual-volume identity; no covariance surrogate or separately centred polar appears.

### Exact transfer toward a width boundary

Move an amount eta=nu_j from width j to width k, leaving the other parameters and total width fixed. Then the actual change in centroid is

```
Delta gx = q^2*nu_j*nu_k/(4D),
Delta g_yz = q*nu_j*(Bk-Bj)_yz/(4D),
```

where nu_k on the right is the pre-transfer width. The volume remains exactly unchanged. The target has Rj=Bj and at most nine true vertices; it is not a raw volume-collapse limit.

For a generic single zero width, the true limiting f-vector is 9/16/9. At the width vertices with only c0 or only c1 positive it is 8/14/8; with only c2 positive it is 8/15/9. Further beta or stack boundary degeneracies can reduce these counts. The actual limiting body is always the convex hull of the displayed limiting coordinates, and its actual centroid is still J/(4D).

### A whole-width lifting identity for actual stresses

Take any fixed nonnegative weighted packet whose endpoints avoid R0,R1,R2. Its raw vertices and edge vectors do not move with nu. Let

`E=sum lambda_ij (zj-zi)`

and

`P(nu)=-sum lambda_ij sym((zi-g(nu))(zj-zi)^T)`.

Suppose `E=-sigma e_x`, with sigma>=0. For the three width vertices e0,e1,e2,

```
P(nu)=sum_j nu_j P(ej)
       +sigma*q^2*(1-sum_j nu_j^2)/(8D) * e_x e_x^T.
```

The second term is PSD on the entire width simplex. Therefore the **same nonnegative weights**, if they yield `P(ej)>delta I` at all three actual corner bodies, yield `P(nu)>delta I` for every width. The extra conditions on E and the use of the same weights are essential; separate corner exclusions do not suffice.

This is a finite convex three-block search at fixed outer geometry: impose `E_y=E_z=0`, `E_x<=0`, and the three corner LMIs. It uses the actual centroid curvature rather than ignoring it. It is a sufficient full-width packet method, not a proof that every rooted tree admits such a packet.

## 5. Proof of the new four-arrow theorem

Let `Dij(M)=(zi-g)^T M(zj-zi)`. Choose the weights from Section 1. Direct expansion gives `E=-e_x` and

```
P=-w03*T03-w14*T14-w25*T25-T35

 = ((7/25-gx,       63 beta/200-gy/2, 119/200-gz/2),
    (63 beta/200-gy/2, beta-121 beta^2/100, 21 beta/200),
    (119/200-gz/2,       21 beta/200,       7/10)),
```

where `Tij=sym((zi-g)(zj-zi)^T)`. In particular the tangential block is independent of the widths and the stack position. The common actual g remains in the first row and column.

Write

```
a=7/25-gx,
y=63 beta/200-gy/2,
z=119/200-gz/2,
C=((beta-121 beta^2/100,21 beta/200),
   (21 beta/200,7/10)).
```

We prove P>I/10000 by an explicit Schur-complement bound.

### Actual x-centroid bound

Let `u=t+sum alpha_(j+1)*(1-fj)`. Then

```
-JLx=436/625+p*t*(7/5+u),
u-(3/10+7t/10)=2 alpha1/5+alpha2/10 >=0.
```

Consequently

`-JLx >= 436/625+1071t/5000+441t^2/5000`.

Because `sum nu_j^2+sum_{i<j}nu_i nu_j<=1`, comparison after multiplication by the positive denominators gives

```
gx <= -(436/625-q^2)/(4(437/500+q))
   <= -6351/44960,                 0<=q<=1/4.
```

For the first comparison the difference has nonnegative t coefficients; its linear coefficient contains the positive constant

`p*((17/10)*(437/500)-436/625)`.

The second comparison follows by differentiation: `(436/625-q^2)/(437/500+q)` decreases strictly for q>=0. Thus

`a >= 94699/224800`.

### Actual transverse-centroid bounds

The exact left z moments satisfy

```
JLz-d=p*(1-f2)*(1-t)+p*t*f2*alpha3 >=0,
1-JLz=p*f2*((1-t)^2+t*(alpha1+alpha2)) >=0.
```

Hence

`1/4 <= gz <= 375/1124`,

and therefore

`17/40 < z <= 47/100`.

At beta=1/2, the actual left y moment obeys

`-189/10000 <= JLy <= 189/5000`.

The right contribution is between -q/2 and q/2. Using D=d+q gives

```
-1439/44960 <= gy|_(beta=1/2) <= 407/11240,
11/80 < y|_(beta=1/2) < 7/40.
```

For general beta, let

```
a1=1-p*f1+p*t*f1*(1+alpha2),
n=(a1+q*(1+nu1))/(8D).
```

Then `0<n<=375/2248`, and the exact affine-in-beta identity is

`y(beta)=2 beta*y(1/2)+(2 beta-1)n`.

For `1/3<=beta<=1/2` it follows that

`(152/1405) beta < y < (7/20) beta`.

All these bounds use the same actual moment formula and hold simultaneously for the full stack tetrahedron and full width simplex.

### Uniform positive Schur complement

The tangential determinant is

`det C = beta*(7/10-34321 beta/40000)>0`.

The numerator of `(y,z) C^-1 (y,z)^T` is

`N=(7/10)y^2-(21 beta/100)yz+(beta-121 beta^2/100)z^2`.

On the just-proved rectangle for `(y/beta,z)`, N is increasing in both variables. This follows from the two exact positive derivative bounds

```
(7/5)*(152/1405) > (21/100)*(47/100),
(79/200)*(17/40) > (21/200)*(7/40).
```

Substitute `y=(7/20)beta`, `z=47/100`. The resulting ratio N/det C increases with beta; the numerator of its derivative is

`15311569/400000000>0`.

Therefore

```
(y,z) C^-1 (y,z)^T <= 225716/541975,
a-(y,z) C^-1 (y,z)^T
 >=94699/224800-225716/541975
 >1/250.
```

Moreover `C >= (29/200)I` throughout the beta interval, by exact diagonal-dominance bounds at the two endpoints and concavity of its quadratic diagonal expression. Also

`y^2+z^2 < (51/100)^2`.

Thus `||C^-1(y,z)^T||<102/29`. Completing the square and using

`1+2*(102/29)^2=21649/841<26`

gives

`P > I/6500 > I/10000`.

This proves the stated quantitative contradiction to the four weak arrows, including nonzero PSD metrics. No SDP result is a premise.

## 6. Complete count of the covered rooted alternatives

The four prescribed parents are `0->3`, `1->4`, `2->5`, `3->5`. Their forced components have roots 5 and 4:

```
A={0,2,3,5}, root 5;
B={1,4}, root 4;
F={9};
right singleton groups {6},{7},{8}.
```

On A,B,F the possible outgoing multiplicities are

```
A->B:1, A->F:1;
B->A:2, B->F:1;
F->A:2, F->B:1.
```

The rooted counts are 8 toward A, 4 toward B, and 4 toward F. None of these components can point to a right singleton, so the final root cannot be 6,7,8.

Each right singleton has its two right-triangle neighbors and one left exit. There are `3^3-3*3-2=16` acyclic choices leading into the left components. Hence the complete counts are

```
root 4: 64
root 5: 128
root 9: 64
TOTAL: 256.
```

The source also enumerates all 46,410 original labelled rooted trees and checks this count directly. These are overlapping selected-packet counts, not canonical registry changes. The theorem is not promoted to all-root U2 on its seven-dimensional sector.

## 7. Full-width acceptance without the width Bernstein matrix hull

Fix beta, q and the stack barycentrics. For any fixed nonnegative stress on arbitrary true arrows, partition its symmetric matrix as

`P(nu)=((a(nu),b(nu)^T),(b(nu),C(nu)))`,

with the first coordinate parallel to the three right edges.

The exact actual-centroid formulas imply

```
C(nu) is affine in the two width variables,
b(nu) has degree at most 2,
a(nu) has degree at most 3,
det P(nu) has degree at most 5.
```

The same assertions hold after subtracting a constant positive margin times I. Therefore strict positivity over the full closed width triangle is equivalent to:

1. the three corner values of C are PD;
2. the scalar polynomial det P is positive over the whole width triangle.

The first statement propagates by convexity. The second is exactly the scalar Schur-complement condition. A rational triangular Bernstein subdivision of the degree-five determinant is a complete positive-gap acceptance procedure for a fixed uniformly PD stress. A failed finite subdivision is still unresolved; a negative determinant at an exact point rejects that stress only, not the body or the packet's physical feasibility.

The distinction is material even algebraically. The matrix

```
((1/100+u^2,u,0),
 (u,1,0),
 (0,0,1))
```

is PD on the entire width triangle: its tangential block is I and determinant is 1/100. Its degree-two Bernstein matrix coefficient with first width count 1 has leading 2x2 determinant `1/100-1/4<0`. Thus matrix-coefficient positivity can fail while the exact whole-width matrix inequality holds. This is an algebraic acceptance control, not an actual-polyhedron survivor.

For outer parameter cells, the same rule can be applied to the outer Bernstein coefficient matrices as width-polynomial matrices. This supplies a different exact acceptance route from demanding PD at every width Bernstein matrix coefficient. It does not prove that the remaining rooted trees possess a common separating row.

## 8. Boundary reduction and genuine residuals

There is a useful uniform boundary reduction, conditional on the journal's accepted **nine-vertex nonzero-PSD refinement theorem**, not merely on an SPD equilibrium count for nine vertices.

Use the parent's compact coordinates `A=1-rho`, `C=3rho`, `rho in [0,1]`. Transfer the smallest width eta from one coordinate to another. The exact centroid-transfer formula and `D>=C` give

```
||Delta g|| <= sqrt(11)*eta/4,
max_i ||Delta zi|| <=3eta,
diameter(P)<=sqrt(11).
```

Consequently every actual arrow tensor changes in operator norm by less than

`(9 sqrt(11)+11/4)eta <33eta`.

Define Gamma to be the minimum, over the compact zero-width boundary, all 46,410 limiting labelled trees, and PSD metrics of trace one, of the maximum negative selected-arrow derivative. The accepted refinement theorem implies Gamma>0. The positivity of volume, continuity of the actual moments, compactness and finite tree list then give

`min nu_j <= Gamma/66  =>  no weak rooted tree`.

This is an **unevaluated analytical collar**, not a newly computed numerical width threshold or certificate table. Its dependency on the stronger refinement theorem is explicit. It shows that an actual full-width U1 survivor cannot be justified by approaching a zero-width collision while retaining these compact shape coordinates. It does not remove a possible interior component.

The principal remainder is therefore the complete rooted alternatives outside the balanced cone and outside any established boundary collar. The new four-arrow theorem removes only the stated 256 alternatives where its beta and C/A hypotheses hold. The old extreme-width 323 countercontrol remains a failure of one transported stress, not a U1 witness. I have not reclassified it or inferred a new census from a finite library failure.

## 9. Exact source restoration from the already supplied native capsule

The following program restores the **unchanged** three antecedent units by their complete byte identities. It accepts the previously supplied native zip, Markdown, or JSON source-complete payload. It never executes an unverified recovery program. If only the original recovery wrapper is found, it executes it only after checking its exact accepted hash and then verifies every restored unit.

This is a reconstruction recipe using an explicitly required native input. It is **not** a claim that the original source bytes have been embedded in this Markdown. No fresh successful execution is reported.

Save as `restore_antecedent.py` and run, for example:

```
python -B -S restore_antecedent.py restored regular_horizon_sector_v2.zip
```

The archive is the already supplied native antecedent source archive (`regular_horizon_sector_v2.zip`). The restoration target marker is `REGULAR_HORIZON_ANTECEDENT_IDENTITIES_RESTORED`.

```python
#!/usr/bin/env python3
from pathlib import Path
import hashlib, io, json, re, subprocess, sys, tempfile, zipfile

EXPECTED = {
    'regular_balanced.py': (18878, '87c639ae0793f0f043265ccf31d6ef416af9d0c5cd30e3b774878261b3aa887a'),
    'regular_execute.py': (1418, '6837fc9d41527cbbd1893cce9923ed764aa95e6e8ebd238cd2e0f9a9e887e458'),
    'regular_horizon_audit.py': (14645, '9f6e96e03a88ddbe4ef6a00cf32d848a5a7f2a1bafc332d3591b9cd838509567')
}
WRAPPER = (17562, 'ab76673c575475469d8d26a3c4ca6666a6677b9c1584d163c4e7cc089b383d24')
found = {}
wrappers = []
seen = set()

def inspect(data):
    digest = hashlib.sha256(data).hexdigest()
    if digest in seen:
        return
    seen.add(digest)
    for name, (size, pin) in EXPECTED.items():
        if len(data) == size and digest == pin:
            found[name] = data
    if (len(data), digest) == WRAPPER:
        wrappers.append(data)
    if zipfile.is_zipfile(io.BytesIO(data)):
        with zipfile.ZipFile(io.BytesIO(data)) as archive:
            for item in archive.infolist():
                if not item.is_dir():
                    inspect(archive.read(item))
        return
    try:
        text = data.decode('utf-8')
    except UnicodeDecodeError:
        return
    for match in re.finditer(r'```[^\n]*\n(.*?)\n```', text, re.S):
        block = match.group(1).encode()
        inspect(block)
        inspect(block + b'\n')
    try:
        obj = json.loads(text)
    except (ValueError, RecursionError):
        return
    def strings(value):
        if isinstance(value, str):
            inspect(value.encode())
        elif isinstance(value, dict):
            for child in value.values():
                strings(child)
        elif isinstance(value, list):
            for child in value:
                strings(child)
    strings(obj)

def main():
    if len(sys.argv) < 3:
        raise SystemExit('restore_antecedent.py OUTPUT_DIRECTORY INPUT [INPUT ...]')
    out = Path(sys.argv[1])
    if out.exists():
        raise SystemExit('Output directory must not exist')
    for name in sys.argv[2:]:
        inspect(Path(name).read_bytes())
    if len(found) != len(EXPECTED) and wrappers:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            wrapper = root / 'recover_regular_horizon.py'
            wrapper.write_bytes(wrappers[0])
            dest = root / 'recovered'
            subprocess.run([sys.executable, '-B', '-S', str(wrapper), str(dest)],
                           check=True, cwd=root)
            for path in dest.rglob('*'):
                if path.is_file():
                    inspect(path.read_bytes())
    missing = sorted(set(EXPECTED) - set(found))
    if missing:
        raise SystemExit('Exact source bytes not found: ' + ', '.join(missing))
    out.mkdir()
    for name, data in sorted(found.items()):
        (out / name).write_bytes(data)
        print(name, len(data), hashlib.sha256(data).hexdigest())
    print('REGULAR_HORIZON_ANTECEDENT_IDENTITIES_RESTORED')

if __name__ == '__main__':
    main()
```

## 10. Complete new analytic-certificate verification source

This unit is self-contained. It reads no parent program, saved certificate, source archive, or hidden input. It verifies the symbolic moment and stress identities, every rational bound used in Section 5, the actual width-centroid lifting identity, the Schur degree bounds for all 34 true arrows, and the exact 256-tree count.

Save as `right_width_packet.py` and run with assertions enabled:

```
python -B right_width_packet.py
```

Expected dependencies are CPython3.13.5 and SymPy1.14.0. The expected marker is `REGULAR_HORIZON_FULL_WIDTH_FOUR_ARROW_PACKET_PASS`. **This consolidated source has not been observed executing in the resumed record.** Its output byte counts and hashes are therefore unassigned, not fabricated; the program prints them when executed. The analytic theorem above rests on the complete displayed identities and rational inequalities, not on an asserted unobserved marker.

```python
#!/usr/bin/env python3
from itertools import combinations
from pathlib import Path
from collections import Counter
import hashlib, json
import sympy as S

R = S.Rational
PARENT = ('minimum-0292',
          '060c67f6b1f274596cdca1b6f4f3838b663d34a0d10d2d15744807922b03580d')
FACES = ((0,3,4,1,7,6),(0,2,5,3),(0,6,8,2),
         (1,4,5,2),(1,2,8,7),(3,9,4),(3,5,9),
         (4,9,5),(6,7,8))
EDGES = tuple(sorted({tuple(sorted(e)) for f in FACES
                      for e in zip(f, f[1:]+f[:1])}))
ARROWS = tuple(e for ij in EDGES for e in (ij, ij[::-1]))
PACKET = ((0,3),(1,4),(2,5),(3,5))
f = (R(3,10), R(3,5), R(7,10))
p = R(63,500)
beta, q, t, a1, a2, u, v = S.symbols('beta q t a1 a2 u v')
a3 = 1-t-a1-a2
alpha = (t,a1,a2,a3)
nu = (u,v,1-u-v)
B = (S.Matrix((0,-beta,0)), S.Matrix((0,1-beta,0)),
     S.Matrix((0,0,1)))
G = S.Matrix((-1,0,0))
L = tuple(S.Matrix((-(1-f[j]), f[j]*B[j][1], f[j]*B[j][2]))
          for j in range(3))
Zright = tuple(S.Matrix((q*nu[j],B[j][1],B[j][2])) for j in range(3))
stack = t*G + a1*L[0] + a2*L[1] + a3*L[2]
z = B + L + Zright + (stack,)

def vsum(vectors):
    return sum(vectors, S.zeros(3,1))

def zero(expression):
    return S.cancel(expression) == 0

def sym(a,b):
    return (a*b.T+b*a.T)/2

def degree(expression):
    poly = S.Poly(S.expand(expression),u,v)
    return 0 if poly.is_zero else poly.total_degree()

def encode(obj):
    if isinstance(obj,S.MatrixBase):
        return [[str(x) for x in row] for row in obj.tolist()]
    if isinstance(obj,S.Basic):
        return str(obj)
    if isinstance(obj,dict):
        return {str(k):encode(vv) for k,vv in obj.items()}
    if isinstance(obj,(tuple,list)):
        return [encode(x) for x in obj]
    return obj

def count_trees():
    ai = {e:i for i,e in enumerate(ARROWS)}
    packet = sum(1 << ai[e] for e in PACKET)
    all_roots = 0
    unrooted = 0
    hit = Counter()
    for es in combinations(EDGES,9):
        adj = [[] for _ in range(10)]
        for i,j in es:
            adj[i].append(j)
            adj[j].append(i)
        todo = [0]
        seen = {0}
        for i in todo:
            for j in adj[i]:
                if j not in seen:
                    seen.add(j)
                    todo.append(j)
        if len(seen) != 10:
            continue
        unrooted += 1
        for root in range(10):
            parent = {root:root}
            todo = [root]
            for i in todo:
                for j in adj[i]:
                    if j not in parent:
                        parent[j] = i
                        todo.append(j)
            mask = sum(1 << ai[(i,parent[i])]
                       for i in range(10) if i != root)
            assert mask.bit_count() == 9
            all_roots += 1
            if mask & packet == packet:
                hit[root] += 1
    assert unrooted == 4641 and all_roots == 46410
    assert dict(hit) == {4:64,5:128,9:64}
    return dict(unrooted=unrooted,rooted=all_roots,
                packet_roots=dict(hit),packet_total=sum(hit.values()),
                not_covered_by_packet=all_roots-sum(hit.values()))

def main():
    assert __debug__ and S.__version__ == '1.14.0'
    assert len(EDGES) == 17 and len(ARROWS) == 34 and (0,1) not in EDGES
    d0 = 1-p
    d = d0+p*t
    D = d+q
    JL = G+vsum(B)-p*(G+vsum(L))+p*t*(vsum(L)+stack)
    JR = S.Matrix((q*q*(1+sum(x*x for x in nu))/2,
                   q*(sum(b[1] for b in B)+sum(nu[j]*B[j][1] for j in range(3))),
                   q*(1+nu[2])))
    J = (JL+JR).applyfunc(S.expand)
    g = J/(4*D)
    bd = S.S(0)
    bj = S.zeros(3,1)
    for face in FACES:
        a = z[face[0]]
        for j in range(1,len(face)-1):
            b,c = z[face[j]],z[face[j+1]]
            w = S.Matrix.hstack(a,b,c).det()
            bd += w
            bj += w*(a+b+c)
    assert zero(bd-D)
    assert all(zero(x) for x in bj-J)
    weights = (1-R(10,7)*beta,R(5,2)*beta,R(7,3),S.S(1))
    E = vsum(w*(z[j]-z[i]) for w,(i,j) in zip(weights,PACKET))
    assert E == S.Matrix((-1,0,0))
    P = S.zeros(3)
    for w,(i,j) in zip(weights,PACKET):
        P -= w*sym(z[i]-g,z[j]-z[i])
    P = P.applyfunc(S.cancel)
    target = S.Matrix(((R(7,25)-g[0],R(63,200)*beta-g[1]/2,R(119,200)-g[2]/2),
                       (R(63,200)*beta-g[1]/2,beta-R(121,100)*beta**2,R(21,200)*beta),
                       (R(119,200)-g[2]/2,R(21,200)*beta,R(7,10))))
    assert all(zero(x) for x in P-target)
    corners = ({u:1,v:0},{u:0,v:1},{u:0,v:0})
    interpolation = sum((nu[j]*P.subs(corners[j]) for j in range(3)),S.zeros(3))
    curvature = S.zeros(3)
    curvature[0,0] = q*q*(1-sum(x*x for x in nu))/(8*D)
    assert all(zero(x) for x in P-interpolation-curvature)
    depth = t+sum(alpha[j+1]*(1-f[j]) for j in range(3))
    assert zero(depth-R(3,10)-R(7,10)*t-R(2,5)*a1-R(1,10)*a2)
    assert zero(-JL[0]-R(436,625)-p*t*(R(7,5)+depth))
    assert zero(JL[2]-d-p*(1-f[2])*(1-t)-p*t*f[2]*a3)
    assert zero(1-JL[2]-p*f[2]*((1-t)**2+t*(a1+a2)))
    half_y = JL[1].subs(beta,R(1,2))
    assert zero(half_y+R(3,20)*p-p*t*(R(3,20)-R(3,20)*a1+R(3,10)*a2))
    j1 = 1-p*f[1]+p*t*f[1]*(1+a2)
    n = (j1+q*(1+nu[1]))/(8*D)
    by = target[0,1]
    assert zero(by-2*beta*by.subs(beta,R(1,2))-(2*beta-1)*n)
    qmax = R(1,4)
    zeta0 = R(436,625)
    assert p*(R(17,10)*d0-zeta0) > 0
    amin = R(7,25)+(zeta0-qmax*qmax)/(4*(d0+qmax))
    assert amin == R(94699,224800)
    gzmax = (1+2*qmax)/(4*(d0+qmax))
    assert gzmax == R(375,1124) and 2*d0-1 > 0
    bzmin,bzmax = R(17,40),R(47,100)
    assert R(119,200)-gzmax/2 > bzmin
    assert R(119,200)-R(1,8) == bzmax
    gymin = -(R(3,20)*p+qmax/2)/(4*(d0+qmax))
    gymax = (R(3,10)*p+qmax/2)/(4*(d0+qmax))
    assert gymin == -R(1439,44960) and gymax == R(407,11240)
    assert R(63,400)-gymax/2 > R(11,80)
    assert R(63,400)-gymin/2 < R(7,40)
    nmax = gzmax/2
    slow,shigh = R(11,40)-nmax,R(7,20)
    assert slow == R(152,1405)
    assert R(7,5)*slow > R(21,100)*bzmax
    assert R(79,200)*bzmin > R(21,200)*R(7,40)
    cdet = beta*(R(7,10)-R(34321,40000)*beta)
    C = target[1:3,1:3]
    assert zero(C.det()-cdet)
    aa = bzmax*bzmax
    bb = R(7,10)*shigh**2-R(21,100)*shigh*bzmax-R(121,100)*bzmax**2
    derivative_numerator = R(7,10)*bb+R(34321,40000)*aa
    assert derivative_numerator == R(15311569,400000000) > 0
    rmax = (aa+bb/2)/(R(7,10)-R(34321,80000))
    assert rmax == R(225716,541975)
    assert amin-rmax > R(1,250)
    for endpoint in (R(1,3),R(1,2)):
        assert (C[0,0]-C[0,1]).subs(beta,endpoint) >= R(29,200)
    assert (C[1,1]-C[0,1]).subs(beta,R(1,2)) > R(29,200)
    assert R(7,40)**2+bzmax**2 < R(51,100)**2
    assert 1+2*(R(102,29))**2 < 26
    assert R(1,6500) > R(1,10000)
    degrees = []
    for i,j in ARROWS:
        Q = (-sym(4*D*z[i]-J,z[j]-z[i])).applyfunc(S.expand)
        assert degree(Q[0,0]) <= 3
        assert max(degree(Q[0,1]),degree(Q[0,2])) <= 2
        assert max(degree(Q[1,1]),degree(Q[1,2]),degree(Q[2,2])) <= 1
        determinant = S.expand(Q.det())
        assert degree(determinant) <= 5
        degrees.append(((i,j),degree(determinant)))
    calibration = S.Matrix(((R(1,100)+u*u,u,0),(u,1,0),(0,0,1)))
    assert S.expand(calibration.det()) == R(1,100)
    assert R(1,100)-R(1,4) < 0
    assert (33-R(11,4))**2 > 81*11
    report = dict(
        object='REGULAR_RIGHT_HORIZON_FULL_WIDTH_PACKET_AND_CENTROID_REDUCTION_V1',
        parent=PARENT,faces=FACES,edges=EDGES,cuts=f,packet=PACKET,weights=weights,
        domain=dict(beta=('1/3','1/2'),C_over_A=('0','1/4'),
                    stack='entire interior Delta3',width='entire interior Delta2'),
        D=D,J=J,centroid=g,negative_stress=P,
        normal_lower=amin,schur_upper=rmax,schur_gap_lower=R(1,250),
        matrix_margin=R(1,10000),degrees=degrees,tree_counts=count_trees(),
        all_root_exclusion=False,physical_U1_survivor=False,
        status='ANALYTIC_PACKET_CERTIFICATE_CHECKED')
    raw=(json.dumps(encode(report),sort_keys=True,indent=2)+'\n').encode()
    output=Path('right_width_packet_report.json')
    output.write_bytes(raw)
    for path in (Path(__file__),output):
        data=path.read_bytes()
        print(path.name,len(data),hashlib.sha256(data).hexdigest())
    print('REGULAR_HORIZON_FULL_WIDTH_FOUR_ARROW_PACKET_PASS')

if __name__ == '__main__':
    main()
```

## 11. Continuation boundary

The new packet proves a genuine whole-positive-width statement with actual centroid control, but only for its four-arrow obligation and stated beta/C/A sector. It is not a substitute for the other 46,154 rooted alternatives. The full-width all-root theorem, or a complete physical U1 survivor, remains to be established.

The most useful computational continuation is to restore the exact antecedent units, retain independent arrow weights, and add the actual normal-resultant corner lift and degree-five Schur acceptance before interpreting any full-width Bernstein-library failure. The original extreme-width countercontrol rules out one stress, not this route or the full body. No further numerical completion or source-only pass is asserted in this handoff.
