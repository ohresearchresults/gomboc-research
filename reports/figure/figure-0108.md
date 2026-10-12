# figure-0108

AI research report · 2026-08-27 UTC

---

# Sharp Comet 13 — exact distributed moment-compensator handoff

## Verdict

**No polyhedral Gömböc winner was obtained.** I constructed the strongest finite fallback requested: an exact three-parameter distributed support-distance compensator on the journal’s deterministic 4,324-row strict construction-centre cover. Its ordinary first-moment map has certified rank three and has a unique interval-isolated zero of all three moments, but the exactly centred body has certified equilibrium class **(S,U,H)=(291,305,594)**. It is therefore a rigorous nonwinner, not a tolerance-dependent near miss.

The work localizes the first obstruction. Along the direct centering ray, the strict `(1,1,0)` chamber ends at an exact equatorial stable–saddle birth after only about 6.31% of the required x-moment correction. A fourth, topology-changing equatorial relay coordinate is the smallest additional geometric degree of freedom supported by the calculation.

## 1. Deterministic finite family

The baseline generator is

```text
build_ring_Q(nrings=120, m=36, kappa=0.04, twist=0.17,
             gamma0=0.025, gammaT=0.03)
```

It produces 4,324 exact-dyadic polar rows: row 0 is the protected stable cap, rows 1–4320 are 120 rings of 36 rows, and rows 4321–4323 are the corrected terminal unstable fan.

The normative finite data are in `data/source_rows_modes.hex`. Every hexadecimal binary64 entry is interpreted as its exact dyadic rational. Let `q_i^0` be a source row and `F_i=(F_i0,F_i1,F_i2)` its three stored mode values. Define

```text
u_i(t) = 1 + F_i·t
P(t)   = {x : q_i^0·x <= u_i(t)}
q_i(t) = q_i^0 / u_i(t).
```

The three modes are broad smooth fields supported on one connected noncritical ring belt. Row 0, the terminal fan, and six-ring collars at both ends are frozen:

```text
axis_tanh1
cos1_c+0.00_s0.80
sin1_c+0.00_s0.80
```

Within each fixed simplicial polar cell, every primal vertex is exactly affine in the parameters,

```text
p_T(t) = (Q_T^0)^(-1) u_T(t),
```

so volume is an exact rational cubic polynomial and each ordinary first moment is an exact rational quartic polynomial. The verifier evaluates these expressions by outward fixed-dyadic interval arithmetic with 180 fractional bits.

## 2. Certified baseline cover

At `t=(0,0,0)` the complete directed audit gives:

```text
irredundant H rows                     4,324
primal vertices / dual triangles      8,644
true edges                            12,966
primal maximal-face cycles             4,324
oriented surface triangles            17,284
stable rows                            [0]
unstable dual face                     6459 = [4322,4323,4321]
saddles                               none
equilibrium class                     (1,1,0)
```

Directed volume, moment and centroid:

```text
V  = 4.20108007651937279616332264275155543
M  = (0.126043494939438717341485663546899833,
     -3.51047663153281293921555062375078091e-13,
     -3.02648270021214512683463240100785868e-12)
c  = (0.0300026404266654026260473759902062426,
     -8.35612882304607216447381362841581399e-14,
     -7.20405858752306705996243240130019691e-13)
```

Mechanical and incidence margins:

```text
minimum nonincident H/V numerator       1.468921317915317e-9
target stable primitive                 9.4628108434300158446e-4
closest excluded stable primitive      -3.5445701325708441983e-6
target unstable barycentric numerator   0.36500711551672076875
closest excluded unstable numerator    -9.0647896134365256558e-4
closest excluded saddle component      -6.6736322550045730495e-4
```

The entire parameter cube `|t_k|<=2^-30` is interval-certified to preserve all 4,324 irredundant rows, the complete incidence, and strict class `(1,1,0)`.

## 3. Full-rank moment image

The directed Jacobian of `(M_x,M_y,M_z)` at the baseline is

```text
[3.87604739106983604085042359598227515   2.9979610597e-18  1.1171368075e-17]
[4.2339768127e-17                        3.28457666093397055392
                                             0.020483146783821244916]
[1.2597295900e-17                        0.021451329444189676067
                                             3.28471859000272685148]
```

with directed determinant

```text
41.8166234302432559033250639185429823.
```

Thus the three ordinary volume moments have exact rank three. The failure is not a lack of mass-control rank.

## 4. Unique interval-isolated exact moment root

A Krawczyk calculation starts from a radius-`2^-44` box and maps it strictly into itself. The unique root is isolated in

```text
t0 in [-0.0325691204264063875168183628302320128,
       -0.0325691204264063875168183628287934171]

t1 in [ 1.01631042686047008076530805950272929e-13,
        1.01631042686047022424387134701824234e-13]

t2 in [ 9.25217194395705862302816581796640482e-13,
        9.25217194395705879480701000298852293e-13].
```

The second Krawczyk image has widths approximately

```text
(2.90e-41, 3.58e-41, 3.53e-41).
```

The Jacobian determinant interval excludes zero throughout the starting box. At the root,

```text
V in [4.17955576236278627859191227716709694,
      4.17955576236278627859191235830236972]
M_x = M_y = M_z = 0 exactly,
```

so the body’s ordinary centroid is exactly the original construction centre.

## 5. Exhaustive audit of the centred root

The complete fixed-topology interval audit over the entire contracted root box gives:

```text
irredundant H rows                     4,324
maximal triangular dual faces          8,644
true edges                            12,966
equilibrium class                    (291,305,594)

minimum positive stable primitive       1.2073183492270106881e-6
closest negative stable primitive      -1.0499512624237583597e-6
minimum positive unstable numerator     1.0060093213928824737e-3
closest negative unstable numerator    -1.2020331264651516722e-4
minimum positive saddle component       9.6220487302243386532e-4
closest negative saddle component      -1.1740813299242659915e-4
```

Every face, vertex, true edge and normal-cone component is included. The centred root is therefore decisively not a Gömböc.

## 6. First exact blocking inequality

On the axis ray `t=(-a,0,0)`, the stable-exclusion primitive for row `i` and true-neighbour witness `j` is

```text
E_ij(a) = u_j - r_ij u_i
        = (1-r_ij) + a(r_ij F_i0-F_j0),

r_ij = (q_j^0·q_i^0)/||q_i^0||^2.
```

The first exact zero is row 2184 with witness 2149:

```text
a1 =
8164249234989496014501371756908122616312627200
/
3978696236342448017364815083047135797794086977207

= 0.00205199109206053893212444239862013967807118958...
```

Its half-turn mate, row 2166 with witness 2131, crosses at

```text
a2 = 0.00205199109206058570070237674195563555820755190...
```

with `a2-a1 ≈ 4.6768577934343e-17`. Directed audits at exact dyadic sample points prove

```text
before a1       (1,1,0), stable [0],           saddles []
between a1,a2   (2,1,1), stable [0,2184],      saddles [(2149,2184)]
after a2        (3,1,2), stable [0,2166,2184], saddles [(2131,2166),(2149,2184)]
```

while the terminal fan remains the unique unstable feature. At the first wall,

```text
V  ≈ 4.200540005571845
Mx ≈ 0.11808846279384565
cx ≈ 0.028112686139688255
remaining fraction of original Mx = 0.9368866108527486.
```

Thus the strict chamber permits only about 6.31% of the needed direct correction.

## 7. Global fixed-chamber evidence and the missing degree of freedom

With the cap/fan collars frozen, all stable exclusions imposed, the target stable and unstable signs retained, bounds `0.02<=u_i<=3`, and all 8,403 non-target faces’ unique mandatory negative barycentric components preserved, a HiGHS linear program minimizes the linearized x-moment only to

```text
Mx_linear_min = 0.06613504464683362 > 0
u_min = 0.9583662789114361
u_max = 1.0016603172590766.
```

This LP is floating-point global chamber evidence, not part of the directed exact proof. Its dominant constraints are two interleaved equatorial chains around ring 60, including `(2189,2154)`, `(2171,2136)`, `(2154,2119)` and `(2136,2101)`.

The smallest additional geometric freedom supported by both the exact local wall and the chamber LP is one **tangential/topology-changing equatorial relay parameter**, in addition to the three moment coordinates. Locally a relay perturbation `h` must satisfy

```text
h_2149 - r_(2184,2149) h_2184 < 0
h_2131 - r_(2166,2131) h_2166 < 0.
```

A concrete minimal continuation is a half-turn-paired four-star or `2x2` equatorial zipper replacing the complete stars around rows `{2149,2184,2131,2166}`, fixing its two boundary chains and adding one tangential diagonal/relay coordinate. The three distributed modes then remain available to solve the three moment equations as dependent constraints. This gives four scalar coordinates in total; another support-height-only mode is not enough because it stays in the blocked mandatory-sign chamber.

## 8. Reproducible artifact

The complete bundle contains the exact generator, parameter modes, interval certificates, full irredundant H/V data, maximal-face cycles, every true edge, full normal-cone ledgers, volume/moment data, verifier, and OBJ/STL exports:

Download the complete exact finite compensator bundle (`slot9_distributed_compensator.zip`)

Read the full research handoff (`research_handoff.md`)

Download the bundle SHA-256 record (`slot9_distributed_compensator.zip.sha256`)

Bundle SHA-256:

```text
b4c343a9c1840859dfe0b68183942b9c480e2cfa4b4139ea9bb32673069c8684
```

Canonical source-table SHA-256:

```text
4f68118d14eb1843d24d3163db53f5b53a02754f053290f5404593ccd00bb58a
```

Key contents:

```text
data/source_rows_modes.hex
data/*_topology.npz
certificates/baseline_mass_interval.json
certificates/baseline_full_interval_audit.json
certificates/baseline_box_30_audit.json
certificates/root3_interval_certificate.json
certificates/root3_full_interval_audit.json
certificates/first_wall_exact.json
certificates/wall_pre_interval_audit.json
certificates/wall_between_interval_audit.json
certificates/wall_post_interval_audit.json
geometry/baseline_hv.npz
geometry/root_midpoint_hv.npz
geometry/baseline.obj
geometry/baseline.stl
geometry/root_midpoint.obj
geometry/root_midpoint.stl
src/generator.py
src/certify_root.py
src/audit_interval.py
src/verify_all.py
src/gomboc_search.py
```

Each H/V archive contains `H`, `Q0`, `F`, `u`, `P`, every dual facet, all oriented surface triangles, all maximal primal face cycles in flattened-offset form, and every true edge as `(P_endpoint_0,P_endpoint_1,H_row_0,H_row_1)`.

The exact root is the interval-isolated nonlinear solution. The root OBJ/STL uses its interval midpoint only for visualization and must not be mistaken for the exact defining data.

## 9. Independent verification

`unzip -t` reports no archive errors. Running

```text
python src/verify_all.py
```

reproduces the exact source hash and reports `overall_ok: true`, including:

```text
baseline class                         (1,1,0)
root class                             (291,305,594)
source bitwise match                   true
baseline/root full audits              complete
Krawczyk strict inclusion              true
unique moment root                     true
wall class sequence                    (1,1,0)->(2,1,1)->(3,1,2)
```

An independent `trimesh` read gives watertight Euler-2 meshes with 8,644 merged vertices and 17,284 triangles. Its floating volumes agree with the direct tetrahedral calculation:

```text
baseline      4.201080076609948
root midpoint 4.179555759066108
```

## 10. Continuation

Do not search another global radial/support-height mode: the three-moment image is already full rank, and the first exact wall plus fixed-chamber LP identify incidence transport as the missing mechanism. Continue from the supplied four-star equatorial relay. Solve the three moments as dependent equations while varying the relay parameter; then interval-audit the first new circuit cell. If the next blocking primitive is independent of the paired equatorial stars, add exactly one further relay cell rather than enlarging the support wave globally.
