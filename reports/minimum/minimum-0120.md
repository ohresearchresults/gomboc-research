# minimum-0120

AI research report · 2026-09-20 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# FOURCUT_B8_FIVE_SHAPE_FULL_VERTICAL_ALL_SPD_AND_BELOW_COM_V1

## 1. Result and applicability

**Two new continuous shape classes are excluded by U_strict >= 2 for every SPD3 metric at the actual uniform volume centroid.** The first has four independently variable corner cuts and an arbitrary positive apex separation. It consequently includes an entire positive vertical-denominator projective pencil for each base. The second is a four-parameter, horizontally projectively deformed class in which one apex is below the true centroid throughout the entire shape domain. Neither theorem assumes S=1, H=0, absence of weak contacts, an external unstable root, a selected full star, or a condition-number bound.

These are actual balanced two-apex bodies with (V,E,F)=(10,17,9), not arbitrary realizations of that incidence type. They are not the three literal pencils closed by parent minimum-0116, declared SHA-256 2cef2760b08850b346dc9334ba45a1de8c0ba6445d2de2d48526a19c9ac7b1d8. That parent fixes three particular bases and an x-denominator pencil; its explicit remaining complement includes other bases and denominator directions. Projective-orbit separation is proved below. :contentReference[oaicite:0]{index=0} :contentReference[oaicite:1]{index=1}

The accepted global interval remains **34 <= C_min <= 622**. There is no new 110 attainer, whole-E17 exclusion, whole balanced-incidence exclusion, or incidence-registry delta. All certificate counts below are local proof-space counts. :contentReference[oaicite:2]{index=2}

## 2. The five-parameter genuine geometry

Write t=(s,w,n,e), with 0<s,w,n,e<=3/4, and let a>0. Define the ten raw vertices in this order:

```text
0=(-1+s,-1,0)       1=(-1,-1+s,0)
2=(-1,1-w,0)        3=(-1+w,1,0)
4=(1-n,1,0)         5=(1,1-n,0)
6=(1,-1+e,0)        7=(1-e,-1,0)
8=(-a,0,1)          9=(a,0,1).
```

The base is the square [-1,1]^2 with four independent isosceles right corner cuts. The eight base vertices are genuine: consecutive cuts have total depth at most 3/2<2. The complete maximal facets, in the native order used throughout the recovery, are

```text
F0=(0,1,2,3,4,5,6,7)
F1=(0,8,1)   F2=(1,8,2)   F3=(2,8,3)
F4=(3,8,9,4)
F5=(4,9,5)   F6=(5,9,6)   F7=(6,9,7)
F8=(7,9,8,0).
```

The true edges are the basal eight-cycle, (i,8) for i=0,1,2,3, (i,9) for i=4,5,6,7, and (8,9). Both apex degrees are 5; every basal degree is 3. There are six triangular facets, two quadrilateral facets and the octagonal base.

For a direct continuous incidence proof, the eight side halfspaces are the nonnegative regions of

```text
1+y-z,  1-y-z,
1+x+(a-1)z,  1-x+(a-1)z,
2-s+x+y+(a-2+s)z,
2-w+x-y+(a-2+w)z,
2-n-x-y+(a-2+n)z,
2-e-x+y+(a-2+e)z.
```

Together with z>=0 these expose exactly the listed facets. Each cut form exposes its designated apex and base side; its value at the other apex is 2a>0. Off-facet base supports are strict because the cuts are positive and disjoint. Thus actual geometry, not a graph declaration, justifies the true edges and positive apex fans.

**Theorem A.** For every t in (0,3/4]^4 and every a>0, the uniformly filled convex hull P(t,a), and every invertible affine image, has at least two strict unstable vertices at its own volume centroid for every SPD3 metric.

### Actual uniform moments

Set sigma_x=(-1,-1,1,1), sigma_y=(-1,1,1,-1), and

```text
Q  = s^2+w^2+n^2+e^2
Hx = sum_i sigma_x[i]*(t_i^3-3*t_i^2)
Hy = sum_i sigma_y[i]*(t_i^3-3*t_i^2)
Rx = sum_i sigma_x[i]*t_i^2
A  = 4-Q/2
D0 = 32-4Q+16a = 8(A+2a)
N0 = (Hx-a*Rx, Hy, 8-Q+8a).
```

The actual volume and centroid are

```text
Vol(P)=(A+2a)/3,        g=N0/D0.
```

These are genuine filled-volume integrals. Removing the four actual corner triangles gives base first moments (Hx/6,Hy/6). The uniform-transverse-chord midpoint mean is (-Rx/8,0). At height u the actual slice is (1-u)B+[-au,au]e_x, with area A(1-u)^2+4au(1-u). Integrating area and first moments yields the displayed formulas. No vertex masses are chosen.

The recovery independently verifies the formulas symbolically using both true positive fans, from apex 8 and apex 9, in both normalization charts below. With actual six-volume d_tau, it checks all four polynomial identities

```text
sum_tau d_tau = D/4,
sum_tau d_tau * sum_{i in tau} P_i = N.
```

The first is 6 Vol=D/4; the second gives g=N/D. Fan diagonals are integration only, never mechanical edges.

### The entire new positive projective pencil

For K_t=P(t,1), define

```text
T_beta(x,y,z)=(x,y,z)/(1+beta*z),       beta>-1,
a=1/(1+beta).
```

All ten denominators are positive precisely on that interval, and

```text
P(t,a)=diag(1,1,1+beta) T_beta(K_t).
```

Therefore Theorem A covers the entire positive vertical-denominator pencil for every base t, followed by any invertible affine map. The image is uniformly refilled: its actual volume is a(A+2a)/3 and its centroid is (g_x(t,a),g_y(t,a),a*g_z(t,a)). It is not T_beta applied to the old centroid.

## 3. All-metric, all-root continuous certificate

### One metric through the unbounded shape parameter

For 0<a<=1 use chart 0, h=a. For a>=1 use chart 1, r=1/a and L=diag(r,1,1). In chart 1 the base x-coordinates are multiplied by r and the apices are (-1,0,1),(1,0,1). Its true centroid has

```text
D1=(32-4Q)r+16
N1=(r^2*Hx-r*Rx, r*Hy, (8-Q)r+8).
```

For centered coordinates X1=LX, the same physical metric and poles transform by

```text
M1=L^(-T) M L^(-1),
Nmetric1=L Nmetric L^T,       Nmetric=M^(-1),
q1=L^(-T) q.
```

Thus M1*Nmetric1=I and every primal and dual Gram value is unchanged. This is a bijection on SPD3 for every physical r>0. The charts agree at a=r=1. The endpoints h=0 and r=0 are only algebraic certificate endpoints; no full-dimensional E17 body or invertible normalization is asserted there. Likewise t_i=0 only closes certificate boxes; it is not asserted to retain an octagon.

### Exact contradiction for every possible root

For each true directed edge i->j, put Dij=Xi^T M(Xj-Xi). A vertex that is not strict unstable has a true incident edge with Dij>=0. Every such weak arrow strictly increases squared norm, including at equality:

```text
||Xj||_M^2-||Xi||_M^2 = 2Dij+||Xj-Xi||_M^2 > 0.
```

If U=1, choosing one such arrow at every nonroot vertex gives a spanning tree directed toward the unique unstable vertex. All ten root locations, including all eight base vertices, must therefore be considered. A global norm maximum is always strict unstable, so excluding U=1 proves U>=2.

In either chart, write g=N/D and Wi=D*Pi-N. Divide each true edge direction only by a factor ell_ij known to be positive on the physical domain, obtaining e_ij=(Pj-Pi)/ell_ij, and form

```text
Cij=-(Wi e_ij^T+e_ij Wi^T).
```

Then tr(M_chart*Cij)=-(2D/ell_ij)Dij<=0 for a weak escape. The source explicitly constructs these polynomial forms; all canceled factors are positive physical edge factors or positive constants.

A certificate row contains positive integer multipliers on actual directed edges and constructs K=sum lambda_ij*Cij. Every tensor-product Bernstein coefficient matrix of K on its specified closed parameter box is strictly positive definite. Exact integer arithmetic checks all three Sylvester leading minors. Bernstein weights are nonnegative and sum to one, so K is positive definite throughout the box. The same single SPD metric would imply both tr(M_chart*K)>0 and tr(M_chart*K)<=0, a contradiction.

Enumeration of all C(17,9)=24310 edge subsets gives exactly 4095 spanning trees and 40950 rooted directed trees. An independent Bareiss determinant of the graph Laplacian cofactor also gives 4095. Certificate-support containment removes every rooted tree on every leaf of the continuous parameter cover. Parent-node rows are inherited by both children of a split; the exact verifier checks every closed midpoint split and final empty remainder. No independent metric is chosen for different rows, roots, boxes, apices or sections.

### Executed exact totals for Theorem A

The two five-dimensional root boxes are [0,3/4]^4 x [0,1]. Their binary covers have 58 nodes, 30 leaves and maximum depth 5. The common multidegree is (4,4,4,4,3), hence 2500 Bernstein matrices per row.

```text
positive integer certificate rows:       3441
positive multiplier terms:              19127
strictly PD coefficient matrices:     8602500
positive Sylvester leading minors:   25807500
actual rooted trees covered per chart:  40950.
```

The floating LP only locates integer candidates. The theorem uses exact polynomial reconstruction, exact positive-definiteness, the actual centroid identity and complete true-tree/domain coverage. Failed LPs are never treated as exclusions; unresolved boxes are subdivided and every terminal box is exactly closed.

## 4. A whole four-shape below-COM projective sector

For the same t domain, fix a=2 and form the genuinely refilled projective body

```text
R(t)=T_(3/8 ex)(P(t,2)),
T(x,y,z)=(x,y,z)/(1+3x/8).
```

All denominators are positive. The complete face lattice and true edges are preserved. The apex images are

```text
8=(-8,0,4),        9=(8/7,0,4/7).
```

**Theorem B.** Every uniformly filled R(t), and every affine image, has U_strict>=2 at its actual volume centroid for every SPD3 metric. Moreover,

```text
4/7 < g_z(t) < 4
```

throughout the entire four-parameter domain. Thus vertex 8 alone is above the base-parallel central plane; vertex 9 and all eight basal vertices are below it. No both-apices-above-COM assumption enters either theorem.

### Uniform refilling and exact certificate

Let f_i=1+3P_ix/8. For the actual apex-9 tetrahedral fan, every projective six-volume is

```text
d_tau / product_{i in tau} f_i.
```

The centroid averages image tetrahedron centroids with exactly these actual volume weights. The recovery clears denominators using the squared product of the four variable f_i, at basal vertices 0,3,4,7; the other f_i are positive constants. After exact common-factor cancellation it constructs g=N/D. It does not transport the previous centroid.

The entire cube [0,3/4]^4 is certified in one cell. The multidegree is (5,5,5,5), giving 1296 coefficient matrices per row:

```text
rows:                              796
positive terms:                    3511
strictly PD coefficient matrices: 1031616
positive leading minors:         3094848
actual rooted trees covered:       40950.
```

Four scalar guards D, Nz, 4D-Nz, 7Nz-4D each have multidegree (3,3,3,3) and 256 strictly positive Bernstein coefficients. Their 1024 exact coefficients prove the whole height statement, not selected examples. The centered-edge matrix construction is additionally checked against all 34 directly evaluated true directed-edge forms at t=(1/4,1/3,2/3,3/4); every proportionality factor is positive. The symbolic construction and positive factor formulas provide the continuous bridge.

Together the two theorems use 4237 rows, 22638 positive terms, 9634116 PD matrices and 28902348 positive leading minors. These are not incidence-registry removals.

## 5. Actual controls, sharpness and weak walls

All seven controls use t*=(1/4,1/3,2/3,3/4). The recovery reenumerates all 120 supporting triples, reconstructs maximal facets and true edges, computes both actual positive apex fans, recomputes centered poles, and audits all 68 true-edge primal/dual primitives. Full coordinates, poles, metrics, strict labels, saddle edges, sections and physical weak packets reconstruct from the included source.

With

```text
M0=[[36,34,58],[34,77,121],[58,121,261]],
A0=[[4,8,16],[-4,-2,2],[2,-3,1]],       M0=A0^T A0,
```

the primary controls at a=1/5,1,5 have strict (S,U,H)=(6,4,8),(5,3,6),(3,3,4), respectively, with all 68 primitives nonzero. Their raw volumes are 2743/2160,779/432,1931/432. Their normalized-chart inverse metrics are transported by the same L.

### Compact literal rational Euclidean 222 body

For P(t*,1), subtract its actual centroid and apply

```text
A=[[3,1,3/5],[0,1/2,-1/5],[0,0,1/10]].
```

The resulting physical vertices are these integer triples divided by 186960:

```text
(-611907,-80901,-6402)
(-705387,-57531,-6402)
(-440527,74899,-6402)
(-191247,106059,-6402)
(369633,106059,-6402)
(618913,43739,-6402)
(509853,-10791,-6402)
(-51027,-80901,-6402)
(-452991,-24813,12294)
(668769,-24813,12294).
```

Its actual centroid is zero, volume is 779/2880 and metric is Euclidean I. It has the native facets above; strict stable facets are F0,F4; strict unstable vertices are 1 and 9; saddle edges are (3,4),(7,9). All 68 primitives are nonzero and there is no weak physical point. Thus Theorem A's U>=2 bound is sharp as a family. The basal unstable vertex is retained; this is not an external-root-only result or a 110 attainer.

### Below-COM sharp control and coherent sections

For R(t*) the actual raw volume and centroid are

```text
V=6947631616/828429525
g=(-7189896653824/3244286142405,
   -12220913737/1081428714135,
    98040056/94987151).
```

The centered apex heights are 281908548/94987151>0 and -43761684/94987151<0. After actual centering, A=diag(100,10,1) gives another rational Euclidean 222 control: stable facets F2,F8, unstable vertices 8,9 and saddle edges (0,8),(3,8), all 68 primitives nonzero. The lower apex remains below the COM and is nonetheless strict unstable. This proves Theorem B's sharpness without a 110 claim.

A different metric on this same actual R(t*) displays coherent central sections. Put

```text
v=-X8_xy/X8_z
 =(4691098121354/2407146614235,
   -12220913737/3209528818980),
G=[[1,1/7],[1/7,49]],        y=1/10000,
M=[[G,Gv],[v^T G,v^T Gv+y]],        N=M^(-1).
```

This control has strict (S,U,H)=(4,4,6), with no zero primitive. For the three actual central planes z=0, x+v0*z=0, y+v1*z=0, the exact sets of vertices in each open half whose squared norm is at least the maximum squared norm of the true section are, in negative/positive order,

```text
z=0:           ({0,1,2,3}, {})
x+v0*z=0:      ({0,1,2,3}, {})
y+v1*z=0:      ({0,1,7}, {2,3,4,9}).
```

The last plane has both high halves; the first two do not. Section points come from true-edge intersections and actual on-plane vertices, not independent formal data. For each plane the recovery constructs X=C X_section and checks

```text
M_section=C^T M C,
N_section=C^(-1) N C^(-T),
q_section=C^T q,
M_section*N_section=I.
```

All 100 primal and 81 dual Gram equalities are checked in each chart. These coherent sections are controls, not the universal all-metric proof, which is the common-M certificate above.

### A genuine weak wall is retained

On P(t*,1), take

```text
G=[[9,3],[3,5/4]],        v=(1/3,-2/5),
M_y=[[9,3,9/5],[3,5/4,1/2],[9/5,1/2,2/5+y]],
y=8271/136600,       N_y=M_y^(-1).
```

Strict counts remain 222, but there is one genuine EF weak resting point on true edge (8,9), at parameter 150997/373920. Its centered position is

```text
r=(-4073/31160,-15/6232,2049/3116).
```

The normal-cone coefficients for adjacent facets F4,F8 are (0,34018623/776756480), and M_y*r=(34018623/776756480)*q8 is checked exactly. There is exactly one zero among the 68 primitives and 67 nonzero primitives. This is a physical EF packet, not a harmless zero. It is included in U>=2. All seven controls, including this non-weak-free one, are preserved.

## 6. Separation from the parent orbits

At s=w=n=e=1/2 all eight new base vertices lie on x^2+y^2=5/4. For the first six literal vertices of the parent's balanced m=3 base, using its actual convention (x/100,y/10), the determinant of the six rows (x^2,xy,y^2,x,y,1) is

```text
-48503/781250000 != 0.
```

Thus even those six old points lie on no conic. Conic containment is preserved by an invertible projective plane map, and the unique octagonal maximal facet must map to the unique octagonal maximal facet. Hence this new symmetric specimen, its vertical projective pencil and its secondary horizontal projective image are outside the full projective orbit of the old balanced base, not just outside its closed pencil. The other parent types have degree pairs (3,7),(4,6), not (5,5). Both the determinant and the new conic identity are exactly checked. Literal parent coordinates, rather than incidence aliases, are used. :contentReference[oaicite:3]{index=3}

The remaining complement includes unequal/non-45-degree corner cuts, other boundary shapes, cuts beyond the certified box, general horizontal projective parameters, multi-direction denominators, and other incidence types outside their known literal orbits. No arbitrary balanced-octagon realization theorem is claimed.

## 7. What was tried and the useful continuation

The initial direction examined root-consistent central planes. A pointwise limitation emerged: for a fixed actual body and fixed M with a unique global norm maximum r, every plane not containing r automatically has a strictly high r-side, because every section point has smaller squared norm than r. A plane containing r has section maximum ||r||^2, so no other vertex can be high. Consequently, when no individual plane has both high halves, the full vertex sets of all certified high halves necessarily contain the same actual r. An empty intersection of those full half-vertex sets at fixed M already entails a one-plane two-high-half obstruction; tied global maxima themselves give U>=2. This does not rule out uniform multiple-plane covers over varying shapes and metrics, but prevents treating independently optimized halves or metrics as extra pointwise information.

A sufficient all-plane-blindness construction was explored numerically: place each nonglobal U vertex in the positive cone of points connected to the global maximum by true-edge paths strictly outside the ball at its radius. A separating central plane would then meet one such path above that radius. No certified all-plane counterconstruction resulted. The complete optional locator and literal floating checkpoint are included as exploratory_visibility.py and numerical_visibility_checkpoint.json. The locator input is seed 94821 and 20000 iterations. Its retained checkpoint, iteration 3403, has four numerical U vertices and global root 5; only vertices 4 and 9 of the three other numerical U vertices pass the locator's masking test. It is NONPROOF floating data, not a rationally verified body, all-plane obstruction or 110 construction. Neither theorem uses it.

The successful change of direction was independent actual base parameters and a full unbounded apex-separation parameter, with the real filled centroid and an affine endpoint normalization. The secondary four-shape projective sector retains a below-COM apex over a whole domain; it does not revive the parent's withdrawn alpha=1/2 claim. The parent retains its distinct corrected below-COM sector and full-lens sparsity theorem. :contentReference[oaicite:4]{index=4} :contentReference[oaicite:5]{index=5}

The most useful continuation is a whole independent-slope corner-cut class, or a continuous horizontal denominator parameter coupled to the four actual cuts, retaining the actual fan centroid and one reciprocal metric. More metric searches on the two classes proved here are exhausted. The pointwise maximum observation may also help formulate a uniform plane-selection theorem over genuinely varying shapes; it is not itself a global exclusion.

## 8. Input authority and delivered-source limitation

I read the entire supplied research-journal, including branch memory and literal parent payload, through line 1888/EOF. The mounted file is 312046 bytes, SHA-256 f2e437fffaf95fa8e5d0fec3edd8a7e68977507d96bb302ec1426ad0584575cd. No other source files were supplied and no research connector or inaccessible archive was used.

The parent's readable mathematical statement and geometry remain authoritative accepted evidence. There is an exact limitation in this delivered copy of its embedded recovery source: extracting the final Python block with one terminal LF gives 28702 bytes, SHA-256 851ce3385ce5f41baf94c1a7aeaee36d07d55dc8188d89a37a3c10e57837332c, rather than the declared 28681-byte wrapper SHA-256 4b5830dfa742153d4ec4e84e1cee169b2a4cc4e2b758488c9b02c2949fa260b6. Its literal DATA fails with `ValueError: base85 overflow in hunk starting at byte 275`. No repair or contents of the five unavailable decoded units were guessed. This is a source-delivery/recovery limitation, not a refutation or reopening of the accepted parent theorem. The new independent capsule has no dependency on that decoder or any of its five units.

## 9. Recovery and actual verification status

The complete capsule below contains ten runnable source units and the full optional numerical checkpoint. Build deterministically regenerates all coefficient rows, both exact reports and all seven exact controls from literal geometry. No parent, old coefficient file, journal, network source or sandbox input is needed. Coefficient records reconstruct through the fully included pinned locator and are then accepted exactly.

Executed environment: CPython 3.13.5, NumPy 2.3.5, SciPy 1.17.0, SymPy 1.14.0, OpenBLAS 0.3.30, Linux x86_64, assertions enabled. The wrapper fixes OPENBLAS_CORETYPE=SkylakeX, OPENBLAS_NUM_THREADS=OMP_NUM_THREADS=MKL_NUM_THREADS=1 and PYTHONHASHSEED=0. Accepted discovery has no random input. The optional nonproof locator has its separately stated seed.

Discovery parameters are maxouter=40, 30 unresolved proposals before splitting, maximum depth 15, primary split-axis cycle (4,0,1,2,3), secondary cycle (0,1,2,3), and rounding scales (1,2,5,10,20,50,100,1000,10000,100000). Secondary per-arrow conditioning factors are positive powers of two computed by the exact source; common normalization is 2^47. Pinned versions matter for byte-identical numerical discovery. Exact acceptance does not accept floating eigenvalues or solver status as proof.

Two source-only build reproductions succeeded. Finally, a fresh directory containing only the frozen wrapper completed `build`, reproduced all five output pins, and completed `check` with the same pins. Both reached the final self-contained-recovery marker. All recorded multipliers were additionally checked to be positive integers on distinct valid true directed-edge IDs. This is an executed exact certificate plus the geometric argument, not a proof-assistant formalization or independently peer-reviewed priority claim.

Save the complete block as recover_fourcuts.py, UTF-8/LF with one terminal LF, and run:

```sh
python recover_fourcuts.py sources
python recover_fourcuts.py build
python recover_fourcuts.py check
```

Sources extracts and authenticates the units. Build and check use the sibling directory fourcuts_recovered. Check regenerates projective polynomial caches from source. Existing mismatched source files cause assertions rather than silent replacement.

Principal markers:

```text
INDEPENDENT_KIRCHHOFF_4095_AND_ALL_40950_TRUE_ROOTED_TREES_PASS
FOUR_TRUE_APEX_FAN_ALL_PARAMETER_VOLUME_AND_CENTROID_IDENTITIES_PASS
EXACT_PRIMARY_PASS 58 3441 19127 8602500 25807500
PROJECTIVE_ALL_34_POLYNOMIAL_ROWS_MATCH_ACTUAL_CENTERED_EDGE_FORMS_PASS
EXACT_PROJECTIVE_PASS 796 3511 1031616 3094848
AUDIT_PASS 7 47835 5f5bdcfb5c2fca47332759765949aee64697f00809357dc56463609533c80976
FOUR_CUT_FIVE_SHAPE_FULL_VERTICAL_PENCIL_AND_BELOW_COM_PROJECTIVE_SECTOR_ALL_SPD_EXACT_PASS
FOUR_CUT_ROOFS_SELF_CONTAINED_SOURCE_ONLY_RECOVERY_PASS
```

Exact pins:

| Object | Bytes | SHA-256 |
|---|---:|---|
| recover_fourcuts.py | 20099 | 0dfcb0c3b855b1d1e1a6256e958c6af3503d780353add523b559639411c8c44f |
| decoded source/checkpoint bundle | 34603 | 8990a44dace422695e1095256049a6d3e07888b2378b7fa791416a632a8b38a5 |
| primary_certificate.json | 146146 | 5f2b42dec7e52a8cc1afe0ee8e59132a6c9ccef90fcc4ad9f7f1a6092ed9c6f1 |
| projective_certificate.json | 25822 | 91717590586babdcf2c11bd38d2f836a58c3f739a3426c57f64c4f81a9c8d281 |
| primary_exact_report.json | 2008 | f2ca63b885227308351f07f0853596670cc98443b79842a792b44e8bf450ff88 |
| projective_exact_report.json | 453 | 8eac2451c9259024df084f70d196b08a23444cb02b94402d30e40a785c27d873 |
| actual_controls.json | 47835 | 5f5bdcfb5c2fca47332759765949aee64697f00809357dc56463609533c80976 |

Individual source pins are embedded and checked before execution. Supplementary copies: [recovery wrapper](sandbox:/mnt/data/recover_fourcuts.py), [complete exact controls](sandbox:/mnt/data/fourcuts_sources/actual_controls.json). Neither link is required by the literal recovery.

### Complete self-contained source

```python
"""Four-cut octagonal roofs: complete self-contained research recovery.
CPython 3.13.5; NumPy 2.3.5; SciPy 1.17.0; SymPy 1.14.0; assertions enabled.
python recover_fourcuts.py sources|build|check
No parent, archived coefficient table, network data, or journal is required.
"""
import base64,hashlib,json,os,subprocess,sys,zlib
from pathlib import Path
assert __debug__
ROOT=Path(__file__).resolve().parent/'fourcuts_recovered'
ROOT.mkdir(exist_ok=True)
DATA="""
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
jhYLsGdu4XthMQoWV3dzjxyL0BAwlyw2lE5LcUDUsLo8w4qgG0vYyXRBK1hwu6OlhqD/K9qlNgk8TNvY/lu3cyy7pQv63aeMdYgl
3DrmHjKNiKsrmV7FeYL7aqEaSHopXUHD0HfWOPaeOWUwU6wOqtAnD3LL0TUbcjMwr4I3p4gAjsy3RDNaQDD5IC1znoX0fFbqZbAW
t5JxCSNlzUacFyb0fypPkxdgP3k5lsfJy6W8TF5INEjDFHImSDrLqysdBKIMOpU5hJCfBJPYl/dCbLc+QxPbYO8+Xp4c5gW6nr/M
i0vaF12uYdcJXW0eyM5jyHmBP5u7nWZhmukNfsJddgOc7PD3Hw4Peyd5sd2L7J43ywBzQm39H8TudNJP1wTTcX0XcU9pfkUec2i6
iMfdez09GhuDEwhN37fsSCr2XcHprj60DKuTtTR1r0Rscw6TUxM8HzBAf//yQ0wrX35o5ypVpyJyX3645Rd6SiiHkvpuqVyvOY16
rdZq1BvlSqsmck6p1azXWm6jVS7XW5VyvSly5VK1Xq5Vam6zXHFbrTqlNGrVctVt1Nyq06pWyyIHaVWtuuWGW6/UmpUqlauXXLfe
cN1a3a2Va7UKQ9WdWqPilBv1aqsFuDI12axX6jVIXLdWaTXwn8gVnVLVrTiVRh0JDnpWr3Nixa2W641Gs9oolyt1VydWGtVGEz1E
h5vo14DGespD3DlGCAaHmoV1kuujvIM2auVKuVqvVxt1t/pC87qAU6q7lXK57FaaGFa9VnZ3DyEG30Zouv2dqEyymyUHOTWnXm+0
qsBa4wU0aPBGqYWGMAOYqSpq24mfVNubE5tFze7ZcriHBPBqPs/CFc9CueSim8CwU2sSXatpQ7FmpeU00a2W49RaVLbiOs1aq1Wu
191G2eUqjtVEYkYcp1JtNluVilN13YrChFupYnjNulOpNRzXaTW5FsxltYJFHG21nHq1oid6J7BbrTgtQny9WW44zZbCGUAqjLRW
vQm6AAGpydyq+gVoqrlaA9m5ICrHrbiNRkWh5JLHg1YAgw60OJGkIqXX6EWJHQOmAEgwcwq4/J4eqpxqtCPOIsSDNwUxOyoClhup
JpTKpJCJLjdrIAX0re4QWWn2agHpdacFHnYIJ64mto056RfLpXIZXAOedqqgrXpDE1qz5oLa3QoqbYHrXioOWeE6wIpDmALvVZmD
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
"""
BUNDLE_PIN=[34603, '8990a44dace422695e1095256049a6d3e07888b2378b7fa791416a632a8b38a5']
SOURCE_PINS={'actual_audit.py': [8975, 'f008fa7a9b97140131c1c62f04a4cf265dd0ce8b458bc29177dc624606ae9986'], 'adapt_box.py': [3408, '21706ab1092040ec386ddb8edd9dd3de76939299e8ea70d99a172fd7c977dbea'], 'bern_box.py': [538, '7d02a4b4d68e7ed3046a29d4b19bcdc5d68fb73273a5edfc2cf1eb00e41b72e2'], 'exact_box_check.py': [4384, '606b725c492d000d6488763c26ce3408354618defddebb2fcee50c68733a4d2d'], 'exact_projective_check.py': [2821, '4f4ba6d4e9b5bb3f17a0d7d258788b66ae8f6be566e54857d5ef10182dcc9fc7'], 'exploratory_visibility.py': [3601, '43ea848b7cbe0cb197e0085871cf879bb86ff6a9c8aae537f91c7a1f9f68334c'], 'numerical_visibility_checkpoint.json': [2973, '23627ed530aabbec2d687b179a1b31d821c7043a3450b3e83f690923c2f3c385'], 'projective_cuts.py': [2440, '304d3e6d73a2e9b41daede9652ba9f183fd89aeab93d5ac9fd5c9efdeace826d'], 'projective_resume.py': [1168, '971d8cdcccd5836b725f1726a28527492baaadec1a0dcdaacfa93bcf372a94e3'], 'roof_box.py': [2203, '4636c6dbf4fe058a0cb93108573d392bf7c65d4b10ad76967b3e0da899392c47'], 'run_all.py': [1179, '5a4b9beb30fb67044b662dd9571c37f4b6c3cdd5d6243a945c4ede88de30ca7c']}
OUTPUT_PINS={'primary_certificate.json': [146146, '5f2b42dec7e52a8cc1afe0ee8e59132a6c9ccef90fcc4ad9f7f1a6092ed9c6f1'], 'projective_certificate.json': [25822, '91717590586babdcf2c11bd38d2f836a58c3f739a3426c57f64c4f81a9c8d281'], 'primary_exact_report.json': [2008, 'f2ca63b885227308351f07f0853596670cc98443b79842a792b44e8bf450ff88'], 'projective_exact_report.json': [453, '8eac2451c9259024df084f70d196b08a23444cb02b94402d30e40a785c27d873'], 'actual_controls.json': [47835, '5f5bdcfb5c2fca47332759765949aee64697f00809357dc56463609533c80976']}
def verify(data,p):
 assert [len(data),hashlib.sha256(data).hexdigest()]==p
blob=zlib.decompress(base64.b64decode(''.join(DATA.split()),validate=True))
verify(blob,BUNDLE_PIN)
sources=json.loads(blob);assert set(sources)==set(SOURCE_PINS)
for name,text in sources.items():
 data=text.encode();verify(data,SOURCE_PINS[name]);path=ROOT/name
 if path.exists():assert path.read_bytes()==data
 else:path.write_bytes(data)
assert sys.argv[1:] in (['sources'],['build'],['check'])
if sys.argv[1]!='sources':
 env=os.environ.copy()
 for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):env[k]='1'
 env['OPENBLAS_CORETYPE']='SkylakeX';env['PYTHONHASHSEED']='0'
 subprocess.run([sys.executable,'run_all.py',sys.argv[1]],cwd=ROOT,env=env,check=True)
 for name,p in OUTPUT_PINS.items():verify((ROOT/name).read_bytes(),p)
for name,p in SOURCE_PINS.items():print('SOURCE',name,*p)
print('FOUR_CUT_ROOFS_SELF_CONTAINED_SOURCE_ONLY_RECOVERY_PASS')
```
