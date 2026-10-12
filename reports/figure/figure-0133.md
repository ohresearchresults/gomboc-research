# figure-0133

AI research report · 2026-08-28 UTC

---

# Conway upper mode-two / counter-rotating continuation — exact finite handoff

## Verdict

No homogeneous convex polyhedral Gömböc was obtained. The durable acceptance gate still requires a finite own-centroid strict `(S,U,H)=(1,1,0)` body with exact/isolated coordinates, complete actual incidence and full-cone audit, independent verification, and matching OBJ/STL. The strongest exact post-circuit endpoint is an own-centred rational 13-vertex polyhedron with

```text
(V,E,F,C) = (13,31,20,62)
(S,U,H)   = (3,2,3).
```

It preserves the intended stable bottom pentagon and intended unstable apex. Relative to the prior exact upper-return mode-one endpoint `(6,3,7)`, the new mode-two/counter-rotating cell and its first actual upper-strip circuits remove three extra stable equilibria, one extra unstable equilibrium and four saddles in net. A residual three-pair Morse block remains: two upper stable–saddle pairs and one lower unstable–saddle pair.

## 1. What was searched

The continuation introduced both of the smallest nonrepeating upper-return freedoms:

- counter-rotating planar Laurent terms on upper layers,
  `x+iy = a e^{i phi} + b e^{-i phi}`;
- independent vertical mode two,
  `z = z0 + Re(tau1 e^{i phi} + tau2 e^{2 i phi})`.

Every numerical state was evaluated by rebuilding the convex hull, merging actual maximal polygons, recomputing the uniform-volume centroid, and classifying actual maximal faces, vertices and polygon-boundary true edges. Search archives contained:

```text
mode-two affine archive                  8,052 topology signatures
mode-two upper-centre archive            3,395 topology signatures
free 14-vertex archive                  10,315 topology signatures
free 13-vertex archive                   7,131 topology signatures
free 15-vertex archive                   6,911 topology signatures
```

The best target-valid class in every archive was `(3,2,3)`. No numerical `(1,1,0)`, `(2,1,1)` or target-valid `(2,2,2)` state was found. These archive counts are empirical discovery evidence, not global quantifier elimination.

## 2. Exact upper-return mode-two cell before final compression

The cyclotomic generator in `postcircuit_exact/mode2_generator.json` works in

```text
K = Q(theta), theta=2 cos(pi/10), theta^4-5 theta^2+5=0,
D = 2^48.
```

For layer `i` and `phi_j=2 pi j/5`, it uses

```text
x+iy = (u_i+i v_i)e^{i phi_j} + (p_i+i q_i)e^{-i phi_j},
z     = z_i + Re(t_i e^{i phi_j} + s_i e^{2 i phi_j}),
```

where counter-rotating and mode-two coefficients are supported on the two upper return layers. Thirty-one rows are generated, but only 14 are extreme at the exact endpoint. The rebuilt body has

```text
(V,E,F)=(14,34,22),  class=(3,3,4),
centred first moments=(0,0,0) exactly.
```

The exact `lambda` path that switches on the four mode-two coefficients has four ordered isolated events:

```text
lambda = 0.1625195768428919  upper S-H birth:
         stable [28,30,21] and saddle (21,28) appear;
         (3,3,4) -> (4,3,5)

lambda = 0.6503411881134371  upper S-H transfer:
         stable [28,30,21] and saddle (21,30) disappear,
         saddle (21,28) survives;
         (4,3,5) -> (3,3,4)

lambda = 0.6738210470977616  hull circuit [0,4,23,24]:
         diagonal (0,23) -> (4,24), class unchanged

lambda = 0.9776596490286097  hull circuit [23,24,25,30]:
         diagonal (24,30) -> (23,25), class unchanged.
```

The exact event roots, norm-polynomial Sturm counts and directed full-cell sign certificates are in `mode2_path_event_certificate.json` and `mode2_path_cell_certificate.json`. The new upper modes therefore create and transfer an upper `S-H` packet; they do not cancel it in this cell.

## 3. Exact rational post-circuit endpoint

### 3.1 Normative V generator

Let

```text
D = 2^40 = 1099511627776.
```

The raw vertices are the following integer rows divided by `D`:

| v | X | Y | Z |
|---:|---:|---:|---:|
| 0 | -26639527338 | -1736413487 | -1099511627776 |
| 1 | 22496758260 | -45181645297 | -1099511627776 |
| 2 | 9491516118 | 17035482487 | -1099511627776 |
| 3 | -22913096886 | -115540045480 | -1099511627776 |
| 4 | 28520523846 | -4103913006 | -1099511627776 |
| 5 | 145687670403 | 290096541820 | -590139060908 |
| 6 | 127795654938 | 366130451998 | -491536891075 |
| 7 | -39271473341 | 100957646836 | -807789335139 |
| 8 | -118602190126 | -432672133980 | -493738373162 |
| 9 | -11547424192 | -212457132418 | -968928233156 |
| 10 | -87891242345 | -8309360279 | 898813983060 |
| 11 | -9969372264 | 171108639036 | 388209886033 |
| 12 | 4598502411 | 19268077079 | 1099511627776 |

Subtract the exact solid centroid below. For every oriented face cycle `(a,b,c,...)`, define

```text
n=(v_b-v_a)x(v_c-v_a),  h=n.v_a>0,  q=n/h,
```

and use `q.x <= 1`. This supplies all exact irredundant H rows. Expanded centred V rows and normalized H rows are in `vertices_centered_exact.csv` and `support_rows_exact.csv`.

### 3.2 Volume and centroid

The 22 outward polygon-fan triangles give

```text
V = 209308572296863183479434635570491893 /
    3987683987354747618711421180841033728
  = 0.052488756120243416913861977946...
```

and raw centroid

```text
Cx = -2902302817695688681248370459025600017950268947 /
      460274418067189235932477055152609783330883239936
   = -0.00630559228097708583671288...

Cy =  2503206288533791493249584366931172738190675827 /
      460274418067189235932477055152609783330883239936
   =  0.00543850839906636403936480...

Cz = -81470905486208768625028543119094654801827883199 /
      460274418067189235932477055152609783330883239936
   = -0.177005069776256684921378...
```

The exact oriented tetrahedral identities prove, after translating by this centroid,

```text
V = sum det(a,b,c)/6,
M = sum det(a,b,c)(a+b+c)/24 = (0,0,0).
```

### 3.3 Actual maximal faces

```text
F00 (10,8,12)      F01 (9,12,8)       F02 (9,5,12)
F03 (7,0,8)        F04 (7,8,10)       F05 (6,12,5)
F06 (6,0,7)        F07 (11,7,10)      F08 (11,6,7)
F09 (11,10,12)     F10 (11,12,6)      F11 (3,8,0)
F12 (3,9,8)        F13 (2,0,6)        F14 (2,6,5)
F15 (2,5,4)        F16 (1,9,3)        F17 (1,5,9)
F18 (1,4,5)        F19 (0,2,4,1,3)
```

### 3.4 Every true edge

```text
(0,2) (0,3) (0,6) (0,7) (0,8)
(1,3) (1,4) (1,5) (1,9)
(2,4) (2,5) (2,6)
(3,8) (3,9) (4,5)
(5,6) (5,9) (5,12)
(6,7) (6,11) (6,12)
(7,8) (7,10) (7,11)
(8,9) (8,10) (8,12)
(9,12) (10,11) (10,12) (11,12)
```

Thus `(V,E,F,C)=(13,31,20,62)` and Euler equality holds.

### 3.5 Exhaustive own-centroid class

Stable maximal faces:

```text
F02=(9,5,12), F04=(7,8,10), F19=(0,2,4,1,3).
```

Unstable vertices:

```text
3, 12.
```

Saddle true edges:

```text
(0,2), (6,12), (8,12).
```

Therefore

```text
(S,U,H)=(3,2,3),  S+U-H=2.
```

The intended bottom pentagon `F19` is stable and intended apex `12` is unstable. The residual block is exactly

```text
lower U-H:  vertex 3 paired with edge (0,2)
upper S-H:  face F02 paired with edge (8,12)
upper S-H:  face F04 paired with edge (6,12).
```

Normalized diagnostic margins, after exact sign decisions, are

```text
minimum stable                    +0.001015878508664165
largest nonstable                 -0.007713909673273853
minimum unstable                  +0.05027256448877279
largest nonunstable               -0.001257915207070086
minimum saddle                    +0.001101769278768421
largest nonsaddle                 -0.007892474171091188
target bottom                     +0.001015878508664165
target apex                       +0.5322496727248133
normalized inactive support gap   +0.002025746814931212.
```

Exact raw minima are

```text
support slack       1143623835671956037554256389575 /
                    10384593717069655257060992658440192
                  = 1.1012696951178038e-4

face/vertex abs     668240934955406236191058209112071839731411943770450792563463394001052462875 /
                    9559525659976850312447001466101789133560445364879950552821254023174673090083815424
                  = 6.990314778411552e-8

edge-cone abs       2444765416345608190799189950221708073694505403068994376762944957076825403979797899174568836635377929965661791459331535831334155242722633929222444375 /
                    36271470945450506616774610314615004187942749428076130752467151691690519002854484712288490353369041356990105841200631990095428525265814893426935950153423361568407552
                  = 6.740188232295146e-17.
```

The exact ledger has 198 positive nonincident support slacks, 62 face primitives, 62 vertex primitives, 124 four-component edge-cone primitives and 13 nonzero normal-span witnesses.

## 4. Exact finalization path and circuit sequence

An exact 14-row path moves only obsolete upper label `10`:

```text
p10(q)=p10(0)+q n,  0<=q<=3/50.
```

Following the continuation from `q=3/50` down to `q=0` gives:

```text
q3 in [0.0433606823373647,0.0433606823373648]
  shared U-H wall: unstable vertex 2 cancels with saddle edge (2,4)
  (3,3,4) -> (3,2,3)

q2 = 2353234748360773946362458653990285058221539328 /
     76503132368797378150514669370842953722197929919
   = 0.030759979042643305...
  2-2 circuit [8,9,10,13], diagonal relay
  [10,13,8] -> [10,13,9]; saddle (8,13) remains

q1 = 17692894824243759884205427753133262361933643776 /
     1008421128916720182564228178866753689066313992017
   = 0.017545144897201888...
  1-3/3-1 circuit [5,9,10,13]
  obsolete vertex 10 deactivates; [10,13,9] -> [9,5,13].
```

The class is exactly `(3,2,3)` in all three low-q actual cells. At high q it is `(3,3,4)`. Exact event ordering, the quadratic minimal polynomial for `q3`, every actual face lattice and directed full-cone cell boxes are independently certified by `path_event_certificate.json`, `verify_path_atlas.py`, and `path_verification_output.json`.

The topology event is genuine: one extreme upper-strip vertex disappears and two upper circuits relay a stable branch, yet the two upper saddles and the lower `(vertex 3, edge (0,2))` pair survive.

## 5. Open perturbation certificate

The 13-vertex endpoint remains in the same lattice and class when all 34 free raw-coordinate parameters vary independently by `+/-2^-90`; the common bottom `z=-1` plane is preserved. Directed exact interval arithmetic gives

```text
class and topology             (3,2,3), (13,31,20)
minimum support slack lower    1.1012696951178038e-4
minimum positive primitive     6.740188232295146e-17
minimum exclusion clearance    3.986340937856186e-6
minimum normal-span abs         1.2114461578482433e-7.
```

The certificate is `postcircuit13_parameter_box_output.json`, generated by `verify_parameter_box_fraction.py`.

## 6. Independent verification and mesh

A clean-room exact verifier reads only the compact generator. SciPy/Qhull proposes face sets; all support, incidence, tetrahedral moment and full-cone decisions are then recomputed with exact rational arithmetic. It independently obtains

```text
(V,E,F)=(13,31,20), M=(0,0,0), class=(3,2,3),
198 positive nonincident slacks and 13 normal-span witnesses.
```

A separate OBJ/STL-only audit reconstructs the same 20 maximal polygons and 31 true edges, obtains volume `0.05248875612024342`, centroid residual below `3e-17`, and verifies the 22-triangle STL is watertight with edge multiplicity two.

## 7. Connected-patch test

A separately exactified 15-vertex dyadic endpoint adds one connected cross-link patch to the counter-rotating upper-return geometry. It has

```text
(V,E,F,C)=(15,37,24,76),
V=0.0749106515647515875...,
M=(0,0,0) exactly,
(S,U,H)=(3,2,3).
```

Its intended bottom face and apex remain equilibria. A `+/-2^-24` box in 39 independent raw coordinates preserves its topology and class. The residual block is again two upper `S-H` pairs plus one lower `U-H` pair. Thus one added communicating patch transfers the block but does not reduce it.

## 8. Attempt to break the conclusion

The exact endpoint’s complete local separator family has two extra stable faces, one extra unstable vertex and three saddles. Selecting one strict exclusion witness for every unwanted feature gives `2^2 * 4^1 * 4^3 = 2304` complete first-order branches. A deterministic finite-difference Jacobian plus HiGHS screen found no branch with a positive common linear margin; the best was `-1.6078861949108496e-4`. This is useful local evidence, not an exact nonlinear impossibility theorem.

Additional free-coordinate searches with one, two and three communicating patch vertices retained target-valid `(3,2,3)` as the best class. Numerical target-invalid `(2,2,2)` cells exist, but in each the intended bottom face has already ceased to be stable; they are not near-winners under the assignment’s target preservation.

## 9. Smallest genuinely new continuation

Upper mode two on a single return layer, counter-rotation, one connected patch, and the first upper-strip vertex deletion are now exhausted as separate mechanisms. The smallest nonduplicative cell is a **bifurcated three-patch replacement of the entire exact residual block**:

1. one lower patch spanning unstable vertex `3`, bottom saddle `(0,2)`, and the adjacent bottom boundary branches;
2. one upper patch spanning stable face `(9,5,12)` and apex saddle `(8,12)`;
3. one upper patch spanning stable face `(7,8,10)` and apex saddle `(6,12)`.

The three patches must have genuine cross-links, not three disjoint serial rails. Keep three remote coordinates as dependent variables enforcing the exact ordinary moments, permit apex-adjacent return vertices to deactivate, and enumerate every rebuilt common cell. A useful event must delete or reroute both apex saddle edges while crossing the lower `U-H` wall in the same connected circuit; another fixed 13-vertex polish or one-patch insertion is redundant.

## 10. Reproduction files

The package contains:

- exact 13-vertex generator, certificate, V/H/edge tables, OBJ/STL;
- primary and independent exact verifiers;
- exact 14-to-13 path generator, event certificate and full-cell verifier;
- exact mode-two/counter-rotating 14-vertex generator, event atlas and box verifier;
- exact 15-vertex connected-patch endpoint and box verifier;
- numerical search-scope report.

No file in the package claims a Gömböc.

## 11. Downloadable artifact index

- Complete checksummed archive (`conway_mode2_joint_handoff.zip`) — SHA-256 `f2ec999e686d86466af3bdc13cb3dc98982fc0590ac8b8be133cdd062ef7ae2c`.
- Archive checksum (`conway_mode2_joint_handoff.zip.sha256`)
- Exact 13-vertex generator (`postcircuit13_generator.json`)
- Exact 13-vertex certificate (`postcircuit13_certificate.json`)
- Exact V rows (`vertices_centered_exact.csv`)
- Exact H rows (`support_rows_exact.csv`)
- True-edge incidence (`true_edges.csv`)
- Deterministic exact generator/verifier (`generate_exact_postcircuit13.py`)
- Independent clean-room exact verifier (`independent_exact_verify_postcircuit13.py`) and output (`independent_exact_verify_postcircuit13_output.json`)
- Directed perturbation verifier (`verify_parameter_box_fraction.py`) and box certificate (`postcircuit13_parameter_box_output.json`)
- 14-to-13 exact event certificate (`path_event_certificate.json`) and verification output (`path_verification_output.json`)
- Mode-two/counter-rotating generator (`mode2_generator.json`), event certificate (`mode2_path_event_certificate.json`), and full-cell certificate (`mode2_path_cell_certificate.json`)
- Watertight OBJ (`postcircuit13.obj`) and STL (`postcircuit13.stl`)
- Independent mesh audit (`independent_mesh_audit_output.json`)
- Exact connected-patch generator (`patch_generator.json`), certificate (`patch_certificate.json`), OBJ (`patch_endpoint.obj`), and STL (`patch_endpoint.stl`)
- Combined verifier transcript (`RUN_ALL_FINAL_VERIFIERS.txt`)
- SHA-256 manifest (`MANIFEST.sha256`) and manifest verification (`SHA256_VERIFY.txt`)
