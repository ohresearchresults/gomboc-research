# figure-0069

AI research report · 2026-08-25 UTC

---

# Verdict

**No strict homogeneous polyhedral Gömböc was found.** The strongest completed endpoint is a finite, exact, own-centred, fully audited connected asymmetric Y-patch body with strict class

\[
(S,U,H)=(2,1,1),
\]

not the required `(1,1,0)`. It therefore is a **fallback object, not a winner**.

The branch nevertheless advances the journal in four concrete ways:

1. it independently reconstructs an exact robust Santaló-polar one-pair seed rather than relying on the unavailable worker bundle;
2. it performs a genuine connected bifurcated Y surgery with simultaneous old-row deletion, new-row insertion, and an exact circuit flip;
3. it solves all three first-moment/Santaló equations identically on every accepted branch by three independent mechanically inactive controls with Jacobian `-I_3`;
4. it isolates a specific transfer obstruction: the original stable–saddle pair is replaced, but a new stable equilibrium remains on the upper trunk while the saddle migrates to the lower fork.

The journal’s acceptance gate requires a finite own-centroid strict `(1,1,0)` object with complete incidence and all-feature certification, not an auxiliary-centre or wall state. The durable Santaló frontier specified a robust asymmetric one-pair seed and called specifically for a connected Y replacement with hard moment controls and inactive slacks above `10^-5`.

## 1. Relation to the journal and dual convention

The original worker-local `Q_0/P_0` coordinates were unavailable, so I did not claim to recover them. I rebuilt an equivalent one-pair object from a separate exact-dyadic hull. The naming is dual to the journal’s preferred convention:

- the reconstructed mechanical body `P_seed` has `(2,1,1)`, corresponding in Morse content to the journal’s `Q_0`;
- its polar row polytope `Q_seed=P_seed^\circ` has `(1,2,1)`;
- the connected surgery is carried out in the row geometry of `Q`, while the final own-centroid equilibrium audit is carried out on `P=Q^\circ`.

Consequently the inherited labels `face 30`, `vertex 16`, `face 21`, and edge `(1,18)` do not survive. Their functional counterparts in the reconstructed seed are:

- preserved target stable face: `P_seed` row `0`;
- preserved unique unstable vertex: `P_seed` vertex `8`;
- residual stable face to be cancelled: `P_seed` row `13`;
- residual saddle: `P_seed` edge `(17,20)`.

All labels below refer to the supplied exact artifacts.

## 2. Independently reconstructed exact one-pair seed

The seed starts from 21 hexadecimal binary64 triples, each interpreted as an **exact dyadic rational**. Its V-hull is reconstructed exactly, translated by its exact uniform-volume centroid, and polarized.

| Object | `(V,E,F)` | Complexity `V+E+F-2` | Strict class |
|---|---:|---:|---:|
| `P_seed` | `(21,43,24)` | `86` | `(2,1,1)` at its exact centroid |
| `Q_seed=P_seed^\circ` | `(24,43,21)` | `86` | `(1,2,1)` relative to the origin |

The exact one-pair mechanics on `P_seed` are:

- stable row `0`, normalized margin `0.9649713543587978`;
- residual stable row `13`, margin `0.008229341695809201`;
- unique unstable vertex `8`, incidence `(0,11,12,13)`, full-cone margin `0.6431850700110551`;
- unique saddle edge `(17,20)`, dual/common Q facets `(21,23)`, margin `0.04801665760097508`.

The normalized inactive separations are already robust:

- `P_seed`: `1.2257287622870588e-4`;
- `Q_seed`: `0.0031020293971865164`.

The origin is strictly inside `Q_seed`: rows `(0,2,8,15)` form a containing tetrahedron with positive barycentric weights approximately

```text
(0.2523518487, 0.2484750289, 0.2492515937, 0.2499215288).
```

The complete seed coordinates, maximal cycles, edge list, incidence table, exact volume/centroid, and exact equilibrium witnesses are in the exact reconstructed seed (`seed_one_pair_exact.json`).

## 3. Genuine asymmetric connected Y surgery

The construction begins with a 31-row candidate architecture. It deletes old seed-Q rows

```text
11, 19, 20
```

and permits additional obsolete rows to disappear. Old rows

```text
16, 17, 18
```

indeed become non-extreme and are absent from the final hull.

Ten candidate nodes are inserted as one connected bifurcated graph:

- a five-node trunk from the old `q11` side to a junction near old `q19`;
- a three-node branch from the junction toward old `q20`;
- a two-node branch from the junction toward retained old `q18`.

Seven inserted nodes remain extreme in the strongest final hull. In compressed final-Q labels:

```text
trunk    = (18,19,20)
branch A = (21,22)
branch B = (23,24)
```

Every one of the final 25 Q rows is extreme. Thus this is not an unchanged single rail, a full rotational copy, a single deletion, or determinant-one metric polishing.

The pre-gate shape parameters are:

```text
(hT,hA,hB,twT,twA,twB,epU,epJ,epA)
=(0.042094073563281945,
  0.00224073810555115,
  0.040220944010695,
 -0.01269955080125108,
 -0.0868186686390075,
  0.059374859176738695,
  0.09690295357595402,
  0.0029352495384329844,
  0.027048261948600463).
```

The full deterministic row formula, deleted/retained label map, exact circuit polynomial, branch direction, and sampled topology states are in the branch/circuit record (`branch_family.json`) and branch replay script (`replay_branch.py`).

## 4. Three hard Santaló/first-moment controls

For a point polytope with rows `q_i`, define three projective control parameters `u=(u_x,u_y,u_z)` by

\[
T_u(q_i)=\frac{q_i}{1-q_i\cdot u}.
\]

Whenever all denominators are positive,

\[
(T_u Q)^\circ=Q^\circ-u.
\]

Let the pre-gauge polar have exact uniform centroid `c`. Then

\[
F(u)=\operatorname{centroid}\bigl((T_uQ)^\circ\bigr)=c-u,
\]

so the hard equations `F(u)=0` are solved exactly by `u=c`, with exact Jacobian

\[
D F=-I_3.
\]

These are three independent mechanically inactive controls: they translate the entire polar together with its reference centroid and hence do not alter its own-centroid equilibrium classification. The generator recomputes the exact pre-gauge centroid and applies this gauge after each accepted circuit branch; the moment residual is never treated as a penalty.

For the final gate endpoint:

- pre-gauge centroid:
  `(-0.003293792395125566, 0.003805962970271007, 2.4433471587071115e-05)` approximately;
- projective denominator interval:
  `[0.9911028810343986, 1.006158061293182]`;
- exact post-gauge first moment:
  `(0,0,0)`;
- exact Santaló root:
  `s=(0,0,0)`;
- certified root box:
  `[-2^-80,2^-80]^3`;
- maximum support displacement over that root box:
  `1.8581021596226544e-24 < 1`.

The last inequality keeps the full root box strictly inside the bounded-polar domain. Strict origin interior is separately witnessed by a positive tetrahedron, given below. Since the polar volume has the standard unique Santaló minimizer for a full-dimensional convex body, the exact zero-moment root at the origin is isolated; the supplied box is therefore a valid root enclosure rather than merely a residual tolerance.

## 5. Strongest exact gate-valid Y endpoint

The final exact object is generated from hexadecimal input interpreted as dyadic rationals and then subjected to the exact rational projective gauge above.

| Object | `(V,E,F)` | Complexity | Mechanical reference |
|---|---:|---:|---|
| `Q_gate` | `(25,69,46)` | `138` | exact Santaló root at `0` |
| `P_gate=Q_gate^\circ` | `(46,69,25)` | `138` | exact uniform centroid at `0` |

The exact class of `P_gate` at its own centroid is

\[
(S,U,H)=(2,1,1).
\]

### Complete equilibrium set

**Stable maximal faces**

| P row | Role | Normalized margin | Limiting row |
|---:|---|---:|---:|
| `17` | preserved target stable face | `0.9649056890086949` | `22` |
| `18` | residual stable face on inserted trunk | `0.0100770225428217` | `1` |

The residual stable face is the actual 11-gon with vertex cycle

```text
(1,4,12,44,19,16,21,23,29,8,6).
```

**Unstable vertices**

There is exactly one:

```text
P vertex 7
incident maximal faces = (1,10,17)
normalized margin      = 0.6394137478330385
full normal-cone coefficients
                       = (1.024271975467335,
                          1.0036826238851173,
                          1.3236112045230572)
```

All cone coefficients are strictly positive, so this is a complete normal-cone witness rather than a facetwise surrogate.

**Saddle edges**

There is exactly one:

```text
P true edge            = (40,45)
endpoint labels        = v_16_20_23, v_20_23_24
common Q facets        = (20,23)
normalized margin      = 0.0996491698618887
full condition signs   = (+,+,+,+)
```

The edge test includes both strict interior projection on the segment and positivity in the full two-normal cone.

### Nearest excluded features

The independently rebuilt audit also identifies the closest non-equilibria:

- nearest nonstable face: row `1`, signed margin `-0.010068872140146299`;
- nearest nonunstable vertex: vertex `42`, incidence `(17,22,23)`, signed margin `-0.0032305812035667535`;
- nearest nonsaddle edge: P edge `(24,38)`, common facets `(15,17)`, signed margin `-0.005307892218064514`.

Thus the reported `(2,1,1)` class is open and not a numerical wall.

### Incidence separation and boundedness

Minimum normalized inactive separation:

- P: `1.0212329223510219e-5`, attained at vertex `19` versus row `19`;
- Q: `0.0005024975554808691`, attained at Q face `25` versus vertex `22`.

Both strict comparisons against `10^-5` are carried out exactly by squared rational inequalities. The P value is close to the requested gate but is genuinely above it.

The origin is strictly inside `Q_gate`: rows `(3,8,9,17)` contain it with positive barycentric weights

```text
(0.25202387648325714,
 0.25282618599814355,
 0.24750489952182894,
 0.2476450379967704).
```

The minimum origin-to-face distance recorded for Q is approximately `0.5462307243698028`. The corresponding polar is therefore globally bounded, and the root-box test above preserves boundedness throughout the certified Santaló enclosure.

The exact polar volume is stored as a rational number; its floating value is approximately

```text
0.021361762463550777.
```

Every maximal face cycle, true edge, vertex incidence, nonincidence slack, face projection witness, vertex tangent/full-normal-cone witness, and edge segment/full-normal-cone witness is stored in the exact Y-patch certificate (`y_patch_gate_exact.json`). The complete coordinate tables are P coordinates (`y_patch_gate_P.csv`) and Q coordinates (`y_patch_gate_Q.csv`).

## 6. Topology transitions and active circuit branches

The stored affine pre-gauge family is

\[
Q_{\rm pre}(\alpha)=Q_{\rm pre}(0)+\alpha D,
\]

followed on every accepted branch by the exact three-coordinate centering gauge.

### Exact incidence circuit

The active four-row circuit is

```text
{0,3,4,17}.
```

Its augmented determinant is an exact cubic. All rational coefficients and an exact isolating interval are stored in `branch_family.json`; the unique small root is approximately

```text
alpha = -9.215042961288109e-15.
```

Across this circuit:

| Side | Exact/sample alpha | P vertex incidences in the circuit | Dual Q edge |
|---|---:|---|---|
| negative | `-10^-12` | `(0,4,17)`, `(3,4,17)` | `(4,17)` |
| positive | `0` | `(0,3,4)`, `(0,3,17)` | `(0,3)` |

Both sides have exact f-vector `(46,69,25)` for P. A floating tolerance had initially made `alpha=0` look like a wall; exact dyadic evaluation places it on the positive side, with the true circuit root slightly negative.

### Mechanical transfer inside the post-circuit topology

| Branch location | Class | Actual residual block |
|---:|:---:|---|
| below about `0.3138` | `(2,1,1)` | stable row `18` and saddle with common facets `(22,23)` |
| sample `alpha=0.315` | `(3,1,2)` | temporary stable row `23` and saddle `(20,23)` are born while the old pair remains |
| sample `alpha=0.335` | `(2,1,1)` | stable row `23` and old saddle `(22,23)` disappear; the saddle has transferred to `(20,23)`, while row `18` remains stable |
| stored binary64 `alpha=0.65`, interpreted exactly | `(2,1,1)` | final gate endpoint; all 25 Q rows active and both P/Q inactive separations exceed `10^-5` |

The incidence circuit and final endpoint are exact. The intermediate mechanical transition locations are reproducible binary64 samples, not interval-isolated bifurcation parameters; they are included to expose the branch topology honestly, not as exact transition times.

## 7. Structural obstruction

The surgery succeeds at replacing the old residual neighborhood, but it performs a **Morse-pair transfer rather than cancellation**.

The lower fork has strong control over the saddle. It moves the saddle from the old dual edge `(22,23)` to the new downstream Q edge `(20,23)`. During this movement a temporary second stable–saddle pair appears, producing `(3,1,2)`, after which the old pair disappears. However, the residual stable equilibrium has already migrated to inserted trunk row `18` and remains strictly stable.

Its complete final Q one-ring is

```text
{0,1,2,4,5,6,7,9,10,19,20}.
```

The corresponding P stable face is the 11-gon

```text
(1,4,12,44,19,16,21,23,29,8,6).
```

The surviving saddle lies downstream on Q edge `(20,23)`, dual to P edge `(40,45)`. The two cancellation duties are therefore geometrically separated: the lower fork controls the saddle basin, while the upper trunk carries the stable normal cone.

This obstruction is not caused by centering, rank, unbounded polarity, or an incidence wall:

- all three first moments are identically zero after every accepted branch;
- the control Jacobian is exactly `-I_3`;
- the origin is strictly interior and the whole root box remains in the bounded-polar domain;
- target face `17` and unstable vertex `7` have large margins;
- final P and Q inactive separations pass the strict `10^-5` gate.

A winner would require a second, upper bifurcation coupled to the existing lower fork. It must replace the **entire star of row 18 and edge `(20,23)` simultaneously**, allowing obsolete members of the eleven-row ring to become non-extreme. Extending only the lower fork should continue to transfer the saddle; moving only row `18` should reproduce the temporary `(3,1,2)` block.

No Euclidean coordinate perturbation radius is claimed for this nonwinner. Exact strict signs and inactive margins prove an open `(2,1,1)` chamber, but I did not convert their joint Lipschitz bounds into a certified coordinate-ball radius.

## 8. Independent verification and finite meshes

The independent verifier (`verify_independent.py`) uses only the Python standard library and does not import the generator. Starting from the hexadecimal input, it independently rebuilds:

- exact V- and H-hulls and polarity;
- exact volume and first moments;
- the projective centering gauge;
- every maximal cycle, true edge, incidence, and nonincidence;
- all stable-face tests;
- all vertex tangent/full-normal-cone witnesses, including nonsimple incidences;
- all true-edge segment and two-normal-cone saddle witnesses;
- exact `>10^-5` inactive comparisons;
- strict positive interior tetrahedra;
- the certified root-box boundedness test.

The stored independent report is `PASS` and records these hashes:

```text
seed_one_pair_exact.json
13e799f4d10c5bffe8c2ceb535eb48cb74a31208a0f8dcc67851dd5e03ffd7a4

y_patch_gate_exact.json
4b94055beb83ff9935d20702f4bd7cfa7874827daa4c3929553a424bbc84da30
```

See the verification report (`independent_verification.json`). A fresh full verifier invocation in the present response exceeded the 900-second execution limit, so the attached stored PASS transcript was inspected and hash-checked but not newly regenerated end-to-end during this turn.

Mesh reconstruction was separately checked:

| Mesh | OBJ vertices | OBJ maximal faces | STL triangles |
|---|---:|---:|---:|
| seed P | `21` | `24` | `38` |
| seed Q | `24` | `21` | `44` |
| gate P | `46` | `25` | `88` |
| gate Q | `25` | `46` | `46` |

The STL files are fan triangulations of the exact OBJ maximal-face cycles:

- gate P OBJ (`y_patch_gate_P.obj`)
- gate P STL (`y_patch_gate_P.stl`)
- gate Q OBJ (`y_patch_gate_Q.obj`)
- gate Q STL (`y_patch_gate_Q.stl`)

## 9. Reproducible artifact bundle

The complete archive is santalo_y_patch_fallback.zip.

```text
SHA-256
65c5c682ac04b3194b35af5cb214a84c64b5f59294555f71402f5c03696dc298
```

Principal files:

- README (`README.md`)
- deterministic exact generator (`generate_exact.py`)
- independent verifier (`verify_independent.py`)
- exact reconstructed seed (`seed_one_pair_exact.json`)
- exact Y-patch certificate (`y_patch_gate_exact.json`)
- branch/circuit record (`branch_family.json`)
- branch replay (`replay_branch.py`)
- certificate summary (`certificate_summary.json`)
- verification report (`independent_verification.json`)
- manifest (`MANIFEST.json`)
- SHA256SUMS

Reproduction commands:

```bash
cd santalo_y_patch_fallback
python generate_exact.py
python verify_independent.py
```

## 10. Most useful continuation

The next search should start from `y_patch_gate_exact.json`, not from the original seed.

1. Freeze the target stable row `17` and unique unstable vertex `7` by explicit lower bounds on their current large margins.
2. Replace residual row `18`, its full eleven-row one-ring, and the downstream edge `(20,23)` in one connected **double-Y** or upper/lower bifurcated patch.
3. Permit simultaneous deletion of obsolete rows; do not constrain the old star to remain extreme.
4. Retain the exact projective controls `u=c`, so every circuit branch is solved on the three-equation Santaló manifold rather than projected back by optimization.
5. Enumerate each four- and five-row circuit before metric polishing, and reject every branch whose exact P or Q inactive separation is at most `10^-5`.
6. Audit the actual rebuilt maximal faces, true edges, vertices, and complete normal cones after every topology change.
7. Rationalize or interval-isolate a prospective winner only after a common desired-class margin above `10^-6` is open.

The present branch rules out neither a larger double-Y patch nor a different equivalent Santaló one-pair seed. It does delimit the architecture: one lower bifurcation can move and replace the residual saddle basin, but cannot by itself remove the upper stable star while the three centering equations and strict incidence gate are maintained.
