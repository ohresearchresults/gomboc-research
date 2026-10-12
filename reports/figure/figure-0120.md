# figure-0120

AI research report · 2026-08-27 UTC

<!-- historical-status:start -->
> **Historical AI report.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../../C622/README.md) passes the supplied exact checks; the search for C<500 remains open. See [verification status and source gaps](../../catalog/coverage.md).
<!-- historical-status:end -->

---

# Conway counterphased two-cell collar — complete research handoff

## Verdict

**No homogeneous convex polyhedral Gömböc was obtained.** The run’s acceptance gate requires a finite uniform-density body evaluated at its own exact volume centroid with strict `(S,U,H)=(1,1,0)`, complete irredundant H/V data, every maximal face and true edge, positive full-normal-cone margins, an independent exact or directed verifier, and matching OBJ/STL; artificial centres, wall points, near-solutions, and unmaterialized existence arguments are excluded.

The predecessor Conway result had already isolated the correct remaining mechanism: its 21-vertex `C5` hull is mechanically `(1,1,0)` in an open axial chamber, but its volume centroid lies `0.38190820146601345` above that chamber; the first face/edge walls arrive after only `1.11%–1.21%` of the linearized centring step, and 12,672 ordinary fifth-ring hulls found no winner. The journal therefore called for a complete fivefold two-cell volumetric collar with counterphased layers.

That architecture has now been materialized and audited exactly. It genuinely adds two counterphased pentagonal layers, transports macroscopic volume downward, preserves a broad strict `(1,1,0)` mechanical chamber, and nearly synchronizes the two target fivefold wall packets. The synchronization has the wrong sign: it creates, rather than cancels, complete equilibrium orbits. At the body’s own exact volume centroid the class is

```text
(S,U,H) = (31,26,55),
```

so the endpoint is a rigorous nonwinner.

## 1. What was tried

The search always rebuilt the actual convex hull and recomputed the solid centroid and complete maximal-face/vertex/true-edge mechanics. Nominal strip connectivity was never accepted as topology.

The tested families included:

- the inherited 12,672 ordinary fifth-ring hulls;
- 15,000 five-ring samples with mode-one vertical corrugation on the two collar layers; the persisted ledger retains the best representatives of at least 300 distinct topology signatures, with best full-active class `(6,6,10)` and hard score `-0.0705338948`;
- 15,000 planar six-ring samples; the persisted ledger retains at least 300 topology signatures, with best full-active class `(21,16,35)` and hard score `-0.113455129`;
- fixed-topology axial optimization with free offsets, which found smaller floating centroid-to-chamber gaps but no algebraically clean winner cell;
- a 6,000-generation search with exact collar offsets `(+π/10,-π/10)` and an explicit nonincident-support floor, from which the endpoint below was selected;
- a broader affine-lobed search whose small nominal defect failed actual hull rebuilding and landed near class `(12,7,17)`, so it was rejected rather than exactified.

The selected state was rounded to dyadic ring parameters, reconstructed in a real cyclotomic field, and re-audited from zero. None of the numerical ledgers is used as the sign oracle for the exact claims.

## 2. Exact finite generator

Work in

\[
K=\mathbb Q(\theta),\qquad
\theta=2\cos(\pi/10),\qquad
\theta^4-5\theta^2+5=0,
\quad \theta\in(19/10,2).
\]

Let `D=2^24`. The six pentagonal ring radii are

```text
(6320544, 9649125, 12173782, 13057424, 13708995, 12339693) / D
```

and their raw heights are

```text
(-16777216, -14388307, -10600577,
 -9784845,  -3721300,   -307450) / D.
```

The offsets, in multiples of `π`, are

```text
(0, 1/10, -1/10, 0, 0, 0).
```

Rings `1` and `2` are the two inserted volumetric collar layers. They are counterphased by `+π/10` and `-π/10`. For `i=0,…,5`, `j=0,…,4`,

\[
\widetilde v_{5i+j}=
\left(r_i\cos(o_i+2\pi j/5),
      r_i\sin(o_i+2\pi j/5),z_i\right),
\]

and `\widetilde v_{30}=(0,0,1)`. Subtract the exact algebraic solid centroid `(0,0,c_z)` given below. These 31 points are all actual extreme vertices.

For each outward maximal face cycle `f=(a,b,c,…)`, its exact normalized H-row is

\[
q_f=\frac{(v_b-v_a)\times(v_c-v_a)}
          {((v_b-v_a)\times(v_c-v_a))\cdot v_a},
\qquad q_f\cdot x\le 1.
\]

The expanded exact field coefficients of **all 31 centred V rows and all 51 normalized H rows** are in the machine certificate:

- Expanded exact certificate (`two_cell_certificate.json`)
- Compact normative generator (`two_cell_generator.json`)

## 3. Actual rebuilt lattice

The exact hull has

```text
(V,E,F,C) = (31,80,51,160)
V-E+F     = 2.
```

All 51 outward maximal faces are:

```text
F00 (23,22,13)       F01 (11,21,20)       F02 (10,20,24)
F03 (25,30,29)       F04 (28,29,30)       F05 (28,30,27)
F06 (16,21,11)       F07 (3,8,13)         F08 (18,23,13)
F09 (18,13,8)        F10 (5,10,0)         F11 (10,9,0)
F12 (26,27,30)       F13 (26,30,25)       F14 (1,11,5)
F15 (1,5,0)          F16 (15,20,10)       F17 (15,10,5)
F18 (20,15,11)       F19 (11,15,5)        F20 (14,18,8)
F21 (14,24,23)       F22 (14,23,18)       F23 (24,19,10)
F24 (10,19,9)        F25 (19,24,14)       F26 (19,14,9)
F27 (9,4,0)          F28 (4,8,3)          F29 (4,14,8)
F30 (4,9,14)         F31 (12,22,21)       F32 (12,21,16)
F33 (3,7,2)          F34 (13,7,3)         F35 (7,12,2)
F36 (2,6,1)          F37 (12,6,2)         F38 (6,12,16)
F39 (6,16,11)        F40 (6,11,1)         F41 (22,17,13)
F42 (13,17,7)        F43 (17,22,12)       F44 (17,12,7)
F45 (25,29,24,20)    F46 (24,29,28,23)    F47 (22,23,28,27)
F48 (22,27,26,21)    F49 (21,26,25,20)    F50 (4,3,2,1,0)
```

All 80 true edges are:

```text
(0,1) (0,4) (0,5) (0,9) (0,10)
(1,2) (1,5) (1,6) (1,11)
(2,3) (2,6) (2,7) (2,12)
(3,4) (3,7) (3,8) (3,13)
(4,8) (4,9) (4,14)
(5,10) (5,11) (5,15)
(6,11) (6,12) (6,16)
(7,12) (7,13) (7,17)
(8,13) (8,14) (8,18)
(9,10) (9,14) (9,19)
(10,15) (10,19) (10,20) (10,24)
(11,15) (11,16) (11,20) (11,21)
(12,16) (12,17) (12,21) (12,22)
(13,17) (13,18) (13,22) (13,23)
(14,18) (14,19) (14,23) (14,24)
(15,20)
(16,21)
(17,22)
(18,23)
(19,24)
(20,21) (20,24) (20,25)
(21,22) (21,26)
(22,23) (22,27)
(23,24) (23,28)
(24,29)
(25,26) (25,29) (25,30)
(26,27) (26,30)
(27,28) (27,30)
(28,29) (28,30)
(29,30)
```

The exact edge-to-two-face incidence table is included in the certificate. The OBJ contains the 51 actual maximal polygons. The STL uses 58 outward triangles; its triangulation diagonals are not treated as true mechanical edges.

## 4. Exact tetrahedral volume and centroid

The exported 58-triangle boundary mesh and a separate 60-triangle `C5`-equivariant moment triangulation were both evaluated by

\[
V=\sum_T\frac{\det(a,b,c)}6,
\qquad
M=\sum_T\frac{\det(a,b,c)(a+b+c)}{24}.
\]

In the descending power basis of `θ`, the exact volume has coefficients

```text
684473549120864431875/4722366482869645213696
2570212213257814765855/4722366482869645213696
1334086794198004644555/18889465931478580854784
-12851061066289073829275/9444732965739290427392
```

and

```text
V = 1.740327800108463030886727746907218193006...
```

The raw transverse moments vanish exactly:

```text
Mx = My = 0.
```

The raw axial moment is

```text
Mz = -0.4891554518505916274776509962862389749624...
```

and the exact algebraic solid centroid is

```text
c = (0,0,-0.2810708717174464654516247502230938186464...).
```

After translating by this exact algebraic centroid,

```text
M = (0,0,0) exactly
```

on both triangulations. The equivariant triangulation partitions into 12 complete five-triangle orbits, and every orbit separately has transverse moment `(0,0)`. Thus horizontal centring is structural in the actual tetrahedral formula, not a post hoc local actuator correction.

## 5. Exact mechanics and the decisive wall packet

### Mechanical chamber retained by the collar

At the exact axial reference point

```text
m=(0,0,-3/4)
```

the actual body is strict `(1,1,0)`:

- unique stable maximal face: bottom pentagon `F50=(4,3,2,1,0)`;
- unique unstable vertex: apex `30`;
- no saddle true edge.

The complete strict axial target chamber is

\[
-1<c_z<c_V,
\qquad
c_V=-\frac{95380952353}{173560299520}
=-0.549555126470664435967896628806\ldots .
\]

Reference diagnostic clearances are

```text
stable positive min       +0.3047840303000574
largest excluded face     -0.0878950600564455
unstable positive min     +1.4186583973596394
largest excluded vertex   -0.1003793572107553
largest nonsaddle score   -0.1293564083383787
```

### First orbit wall

At the exact rational value `c_V`, five unstable vertices and five saddles are born:

```text
U: 20 21 22 23 24
H: (20,25) (21,26) (22,27) (23,28) (24,29)
```

and the class becomes `(1,6,5)`.

### Second orbit wall

The next wall is the exact algebraic value

```text
c_F = -0.5495551196741486334879672945051995681168...
```

whose four exact field coefficients are in the certificate. It creates

```text
S: F11=(10,9,0), F14=(1,11,5), F29=(4,14,8),
   F34=(13,7,3), F37=(12,6,2)
H: (0,9) (1,5) (2,6) (3,7) (4,8)
```

and the class becomes `(6,6,10)`.

The two complete wall packets are rigorously ordered by

```text
c_F-c_V = 0.000000006796515802479929334300986995440484190242... > 0.
```

This is the sharp obstruction. The inserted two-cell collar almost synchronizes the intended face/edge and vertex/edge orbit walls, but their common orientation is a **fivefold birth/transfer cascade**, not a cancellation. These are mechanical equilibrium walls on the exact rebuilt collar hull; the insertion of the collar itself is the topology-changing replacement relative to Conway.

### Mechanics at the own centroid

The own centroid lies

```text
0.2684842547532179705162718785830927449108...
```

above the first target wall. At that exact centroid the exhaustive class is

```text
(S,U,H)=(31,26,55),    S+U-H=2.
```

Every positive and excluded feature is listed in the certificate. Diagnostic endpoint clearances are

```text
stable positive min       +0.0124208510417431
largest excluded face     -0.0450751469965802
unstable positive min     +0.0263529934259425
largest excluded vertex   -0.0299471089361463
saddle positive min       +0.0516039251878215
largest nonsaddle score   -0.1365954317554114
```

## 6. Raw incidence and full-cone margins

Exact field sign isolation certifies:

```text
minimum normalized nonincident support gap  9.999329731159986e-5
minimum raw nonincident support slack        2.776611031073274e-5
minimum raw face/vertex primitive |.|        1.192173043068654e-3
minimum raw full-edge-cone primitive |.|     8.727862633069807e-9
incident-normal span witnesses               31
all endpoint primitives exactly nonzero      true
```

The original Conway centroid-to-chamber gap was `0.38190820146601345`; the exact collar reduces it to `0.26848425475321797`, an absolute reduction `0.11342394671279549`, or `29.6992696876894%`. The collar therefore solves the *scale* problem partially and materially, but not the coupled topology problem.

## 7. Open perturbation certificate

A separate directed verifier varies all six radii and all six raw ring heights independently by `±2^-45`, while offsets and apex remain fixed. Over the entire 12-parameter box it certifies:

```text
actual topology                    (31,80,51)
volume interval                    [1.7403278001078586,1.7403278001090672]
centroid-z interval                [-0.2810708717177132,-0.28107087171717965]
minimum support slack lower        2.7766109722037254e-5
reference class                    (1,1,0)
reference positive lower           0.02517956744642708
reference exclusion lower          2.7356786146110135e-8
own-centroid class                 (31,26,55)
own positive lower                 4.6733139805640565e-7
own exclusion lower                8.727862579368696e-9
wall-order gap lower               6.789333983903134e-9
centroid-minus-wall-1 lower        0.26848425475210486
```

Physical `C5` symmetry remains exact throughout this box, so `Mx=My=0` identically and each representative wall is replicated fivefold. The result is an open chamber, not tolerance dust.

## 8. Independent verification

All verification paths were rerun after packaging:

1. The deterministic algebraic generator reconstructs the exact field body, both tetrahedral moment triangulations, the actual maximal-face lattice and true edges, every equilibrium primitive, the exact wall ordering, and the meshes.
2. A clean-room exact verifier reads only `two_cell_generator.json`, reconstructs the body without importing stored ledgers, checks all 1,421 positive nonincident support slacks, recomputes the exact moments, classes, and wall groups, and reports `PASS`.
3. A directed 12-parameter box verifier reports `PASS`.
4. A separate decimal OBJ/STL/Qhull audit merges the same 51 maximal faces, reconstructs 80 true edges, verifies 58 STL triangles and edge multiplicity two, obtains volume `1.7403278001084628`, centroid residual below `5×10^-17`, and recovers both `(31,26,55)` and the reference `(1,1,0)` class.
5. `sha256sum -c MANIFEST.sha256` passes for every normative file.

## 9. Smallest genuinely new continuation

Another planar pentagonal ring or another fixed axial profile is now redundant. The smallest unclosed architecture keeps the same 31 vertices but makes the two collar layers vertically mode-one corrugated:

\[
\begin{aligned}
x_{1,j}+iy_{1,j}&=r_1e^{i(\pi/10+2\pi j/5)},
&z_{1,j}&=z_1+\Re(\tau\omega^j),\\
x_{2,j}+iy_{2,j}&=r_2e^{i(-\pi/10+2\pi j/5)},
&z_{2,j}&=z_2+\Re(\sigma\omega^j),
\end{aligned}
\qquad \omega=e^{2\pi i/5}.
\]

With a fixed helical strip indexing, every coordinate is a Laurent polynomial of degree at most one. Consequently the actual tetrahedral volume polynomial has degree at most three and each first-moment polynomial degree at most four. Five-point root summation removes every nonzero alias exactly; only the degree-zero coefficients remain.

The next exact/interval solver should:

1. use the two real equations `Mx=My=0` to make the complex counterphase `σ` dependent on `τ` and the strip geometry, rather than append local actuators;
2. solve `Mz=0` by isolating one radius or mean collar height inside the actual rebuilt cell;
3. retain one independent complex corrugation direction to split the nearly coincident fivefold birth packet;
4. permit the five current quadrilateral faces to triangulate asymmetrically and enumerate the first actual hull circuits;
5. cross the current unstable/saddle and stable/saddle wall stars in one coupled asymmetric cell while preserving the bottom pentagon and apex;
6. abandon physical `C5` equilibrium symmetry but retain exact five-point Fourier closure of the tetrahedral moments.

Only if that two-layer mode-one cell still transfers the Euler-neutral block should a third transverse closure band be added. This is the smallest architecture not excluded by the exact planar-collar result.

## 10. Artifacts

- Complete checksummed handoff ZIP (`conway_two_cell_collar_handoff.zip`) — SHA-256 `b2ed82e0099f81c57bfd9267da53a0b02d256f63c15732d7d7eca30a420b5bfb`.
- ZIP SHA-256 file (`conway_two_cell_collar_handoff.zip.sha256`)
- Full Markdown handoff with all faces and edges (`README.md`)
- Compact exact generator data (`two_cell_generator.json`)
- Expanded exact H/V, topology, moment and mechanics certificate (`two_cell_certificate.json`)
- Deterministic algebraic generator and primary verifier (`generate_exact_two_cell.py`)
- Clean-room exact verifier (`independent_exact_verify.py`)
- Clean-room verifier output (`independent_exact_verify_output.json`)
- Directed perturbation-box verifier (`verify_parameter_box.py`)
- Perturbation-box certificate (`parameter_box_output.json`)
- Independent mesh/Qhull audit (`independent_mesh_audit.py`)
- Independent mesh audit output (`independent_mesh_audit_output.json`)
- Watertight maximal-face OBJ (`two_cell_collar.obj`)
- Watertight 58-triangle STL (`two_cell_collar.stl`)
- Search scope and rejected routes (`search_report.json`)
- Fresh combined verifier transcript (`RUN_ALL_VERIFIERS.txt`)
- SHA-256 manifest (`MANIFEST.sha256`)

## Bottom line

The requested finite winner was not found. The exact two-cell collar is the strongest materialized result of this direction: it is a fully expanded 31-vertex/80-edge/51-face algebraic body, has exact zero first moments after algebraic centring, has a wide strict `(1,1,0)` chamber about an axial mechanical centre, reduces the Conway mass gap by 29.7%, and has complete exact and independent audits. Its failure is sharply localized: two complete fivefold mechanical wall packets are separated by only `6.7965×10^-9`, but they are births, not cancellations, and the own centroid remains `0.26848425475` beyond them. The next nonredundant move is a vertically corrugated counterphased two-layer cell that preserves finite Fourier moment closure while breaking the physical fivefold equilibrium orbits.
