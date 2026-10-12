# figure-0301

AI research report · 2026-09-04 UTC · [Export notes](../../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI report.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../../C622/README.md) passes the supplied exact checks; the search for C<500 remains open. See [verification status and source gaps](../../catalog/coverage.md).
<!-- historical-status:end -->

---

# Clear Willow 25 — exact minimal swallowing-cage continuation of J55

## Disposition

**EXACT NONWINNER; no homogeneous polyhedral Gömböc was obtained.**

I left the falsified nine-row convex-combination belt and constructed the smallest standalone full-dimensional support cage that can make row `5003` strictly nonextreme. The construction is exact, rational, evaluated at its own ordinary-volume centroid, and materially changes the J55 topology. It deletes the old residual unstable 17-gon and saddle `(14001,14014)`, but the Euler-neutral packet transfers to a new strict `(2,2,2)` block rather than annihilating.

The strongest new exact endpoint is named

```text
J56_TET4_swallow5003_exact_NONWINNER.
```

Its decisive obstruction is a new true dual edge `(30001,30003)`: every nonmutual row-star arrow at both endpoints is strictly positive. The mutual-arrow identity then forces at least one endpoint to be stable throughout the corresponding strict sign chamber. Since protected row `2475` is independently stable, that chamber has `S>=2`.

The immutable parent `figure-0298`, SHA-256 `091ec5e67ff68955ef13a261fd943972b9c6ed90894e91c5f883be54227ba33a`, established that the purported J56 winner was false and that a valid continuation must make `5003` nonextreme or cross one of its star inequalities no later than the old-pair wall. The underlying exact geometric source is `J55_D17R_anti_carrier18`, strict own-centred `(1,2,1)`.

## Exact deterministic construction

Let the exact own-centred J55 support rows be `q_i`, as serialized in the parent source whose SHA-256 is

```text
ba6f45ae283e444a4ee92ff14e4987041ca4e442a181892675f6b8af00759fa3.
```

Retain all 18 J55 supplied rows and add four rational supports:

```text
q_30000 = q_5003 + ( 3/10,  3/10,  1/10)
q_30001 = q_5003 + ( 3/10, -3/10, -1/10)
q_30002 = q_5003 + (-3/10,  3/10, -1/10)
q_30003 = q_5003 + (-3/10, -3/10,  1/10).
```

They satisfy the exact affine identity

```text
q_5003 = (q_30000+q_30001+q_30002+q_30003)/4.
```

Their raw tetrahedral volume is exactly

```text
3/125 > 0.
```

Thus `5003` lies strictly inside the tetrahedron formed by the four new supports before ordinary-centroid closure. The four new supports are affinely independent, and four is minimal in the scoped class in which new supports alone must strictly contain a point in three dimensions.

Construct the raw polar

```text
P_raw={x:q_i·x<=1}.
```

Enumerate its exact maximal dual faces and corresponding primal vertices. Integrate its exact ordinary volume and first moment by the oriented boundary-triangle formulas

```text
V = sum det(a,b,c)/6,
M = sum det(a,b,c)(a+b+c)/24,
c = M/V.
```

Apply the exact projective support gauge and primal translation

```text
h_i = q_i/(1-q_i·c),
p_v = p_v_raw-c.
```

This gives

```text
P={x:h_i·x<=1}
```

with ordinary centroid exactly zero. Direct rational reintegration gives

```text
Mx=My=Mz=0.
```

The exact source and deterministic construction are available as parent source (`J55_D17R_anti_carrier18_exact_source.json`), endpoint source (`exact_source.json`), and builder (`build_exact_endpoint.py`).

## Complete actual hull

Fresh exact reconstruction from all 22 supplied H rows gives

```text
supplied H rows     22
active H rows       19
inactive H rows      3
primal vertices     34
true edges          51
maximal faces       19
Euler       34-51+19 = 2
complexity          102.
```

The exact inactive rows are

```text
14001,14014,5003.
```

The exact active rows are

```text
14000,14002,14003,14004,14005,14006,14007,
2475,5000,
14008,14009,14010,14011,14012,14013,
30000,30001,30002,30003.
```

All four inserted rows are extreme. Row `5003` is supplied but strictly nonextreme. Its exact barycentric weights in the final own-centred support tetrahedron are positive and sum to one; their decimal diagnostics are

```text
0.2839876102727730
0.21674003473400566
0.21034240503076770
0.28892994996245370.
```

The own-centred tetrahedral volume remains strictly positive, approximately

```text
0.019033695044661177.
```

The new-new true dual edges are exactly

```text
(30000,30003)
(30001,30003)
(30001,30002),
```

so the four new extreme supports form one connected physical graph. This is not an inactive interpolation arc or a collection of disconnected caps.

The exact unshifted ordinary volume is a positive rational with decimal value

```text
27.68944307124429...
```

and the exact raw centroid has decimal value

```text
(-0.005196379424305538,
  0.040491436810989524,
 -1.5621929903196745).
```

The exact numerator and denominator of the volume, all three centroid fractions, the zero translated moments, and all inactive gaps are serialized in certificate.json.

Complete finite data:

- All supplied exact H rows (`H_supplied_exact.csv`)
- Raw exact support rows (`Q_raw_exact.csv`)
- All exact primal vertices (`V_exact.csv`)
- Supplied-versus-active ledger (`supplied_active.csv`)
- Every maximal-face cycle (`face_cycles.json`)
- Every true edge (`true_edges.csv`)

The minimum exact all-supplied active-face nonincidence separation is positive; its decimal value is

```text
0.027697067730970297.
```

All three inactive rows have exact positive separating gaps.

## Exhaustive exact equilibrium audit

Every maximal primal face, every complete incident-edge cone at every active primal vertex, and all four components

```text
(t,1-t,beta1,beta2)
```

of every true-edge normal cone were recomputed with exact rational arithmetic.

The endpoint class is

```text
(S,U,H)=(2,2,2).
```

### Stable maximal faces

```text
protected stable row 2475
  minimum normalized component ≈ 0.12337841640362182

replacement stable row 30001
  minimum normalized component ≈ 0.30494456643891266.
```

Every other active H row has an exact nonpositive star witness.

### Unstable primal vertices

The two unstable vertices are the primal vertices dual to

```text
[14006,14007,30002]
  minimum complete-cone component ≈ 0.07740897810204594

[5000,14008,30000]
  minimum complete-cone component ≈ 0.09120586714563625.
```

The protected parent incidence `[2475,5000,5003]` is necessarily replaced because `5003` is nonextreme. The endpoint nevertheless retains two strict unstable vertices, not one.

### Saddle true edges

The two saddle true edges correspond to the dual row pairs

```text
(14002,30001)
  components ≈
  (0.2056842504468928,
   0.7943157495531071,
   0.48006649707601645,
   0.7696367485606675)

(14013,30001)
  components ≈
  (0.22590174239769403,
   0.7740982576023060,
   0.12116651149448995,
   0.9565571432805207).
```

All four components are exactly positive for each listed edge. Every other true edge has an exact nonpositive component.

The full feature-by-feature ledger is mechanics_exact.json.

## Literal death and replacement of the J55 packet

The inherited residual unstable 17-gon is absent because rows `14001` and `14014`, two of its defining support rows, are strictly inactive. The inherited saddle `(14001,14014)` is likewise absent as a true dual edge. Row `5003`, whose premature stability invalidated the orphan J56, is also strictly inactive.

The surgery therefore achieves the requested literal source-carrier destruction. It does not merely alter the mechanical reference point or reverse one local sign.

The replacement packet is

```text
stable row       30001
unstable vertices [14006,14007,30002]
                  [5000,14008,30000]
saddle edges      (14002,30001)
                  (14013,30001).
```

Thus one old U-H pair becomes an S-U-two-H block while the protected stable row remains present; the Poincaré relation is still satisfied:

```text
2+2-2=2.
```

## Exact external-arrow obstruction

All 51 true dual edges and every directed row-star component were audited. The edges for which every nonmutual external arrow is positive at both endpoints include the two protected-row relations

```text
(14007,2475)
(2475,5000)
```

and the new adverse carrier

```text
(30001,30003).
```

For any adjacent support rows `i,j`, define the unnormalized mutual numerators

```text
A(i→j)=||h_i||²-h_j·h_i,
A(j→i)=||h_j||²-h_i·h_j.
```

They satisfy exactly

```text
A(i→j)+A(j→i)=||h_i-h_j||²>0.
```

For edge `(30001,30003)`, every other incident component at both endpoints is exactly positive. Therefore at least one of its two mutual numerators is positive, and the corresponding endpoint has every row-star component positive. At least one of `30001,30003` must consequently be a stable face throughout the same strict external-sign chamber.

Since row `2475` is independently stable, the chamber satisfies

```text
S>=2.
```

At the promoted endpoint the selected sink is `30001`. The exact complete audit and the forcing identity are in external_arrow_audit.json.

This is the precise residual obstruction. It is stronger than merely observing the endpoint class: every realization retaining this incidence and all of these strict external signs remains a nonwinner.

## Exact activation chronology

I tested the natural homothetic cage ingress

```text
q_3000k(t)=q_5003+t(q_3000k(1)-q_5003),
```

followed at each rational `t` by exact reconstruction and exact ordinary-centroid closure.

Three exact rational samples establish the ordering failure:

```text
t=1/1000
  class (1,2,1)
  old residual unstable 17-gon still strict
  old saddle (14001,14014) still strict
  no additional stable face yet

t=1/100
  class (7,2,7)
  old residual unstable 17-gon still strict
  old saddle (14001,14014) still strict
  six additional stable faces and six additional saddles already strict

t=1
  class (2,2,2)
  rows 14001,14014,5003 inactive
  old residual pair absent
  replacement block strict.
```

At `t=1/100`, the additional stable faces include rows `14002,14003,14004,14008,14009,14010`, in addition to protected row `2475`; their exact positive components coexist with the old U-H pair. This proves that the canonical activation fails death-before-birth before the old packet disappears.

The certificate deliberately makes no unsupported claim that these three samples isolate every algebraic root. It proves the required negative ordering statement for this explicit ingress. Full data are in exact_activation_chronology.json.

## Nonzero exact perturbation chamber

A determinant-one shear provides a genuine nontrivial shape chamber:

```text
L(s) = [[1,s,0],
        [0,1,0],
        [0,0,1]],

|s| <= 2^-24.
```

Transform the exact endpoint by

```text
p_v(s)=L(s)p_v,
h_i(s)=L(s)^(-T)h_i.
```

Because the original centroid is zero and `det L(s)=1`, every member remains exactly ordinary-centred with the same positive volume. Every guarded incidence, inactive separation, stable/unstable decision, and four-component saddle decision becomes an exact univariate rational polynomial in `s`. Coefficient-sum variation bounds prove that no guarded polynomial can reach zero on the interval.

The entire box therefore retains

```text
(V,E,F)=(34,51,19)
(S,U,H)=(2,2,2)
```

and the same active/inactive labels and critical features. The smallest reported guarded lower bound is approximately `0.01907363602645078` after normalization.

Files:

- Exact shear-box certificate (`one_parameter_shear_box.json`)
- Exact polynomial verifier (`verify_1d_shear_box_poly.py`)

The verifier terminates with

```text
EXACT_TET4_ONE_PARAMETER_SHEAR_BOX_PASS.
```

This is a nonzero open interval of geometrically distinct exact-centred nonwinners, not a cancellation wall.

## Connected positive-volume transition certificate

The tetrahedral cage certificate records:

```text
rank                         4
new supports                 30000,30001,30002,30003
all new supports active      yes
raw enclosed row             5003
raw tetrahedral volume       3/125
own-centred tetra volume     positive
new-row graph connected      yes.
```

The exact certificate is tetrahedral_cage_certificate.json.

The construction is genuinely three-dimensional and endpoint-changing. Its failure cannot be attributed to a sheet, isolated stellar insertion, inactive arc, or failure to deactivate `5003`.

## Meshes

Finite display meshes were generated from the exact primal vertices and maximal-face cycles:

- OBJ (`J56_TET4_swallow5003.obj`), SHA-256 `fddeaa4d5cef0600fddb0eb7f72a99a744c3e25f65ac169190a10d69587e1063`
- STL (`J56_TET4_swallow5003.stl`), SHA-256 `449b8455d9c7243d858b97f3ae67b1f193c1bf7f999896bbb1c1fda1720e49a6`

The OBJ contains 34 exact-source vertices and 64 display triangles. Display triangulation diagonals are not included in the 51-edge mechanics ledger.

## Finite empirical screens

The following searches rebuilt the actual hull and ordinary centroid for every accepted numerical sample:

```text
960 first-order separator branches around the exact cage
unrestricted four-support tetrahedral cages
tetrahedral cage plus one active outlet
tetrahedral cage plus two active outlets
five-support bipyramidal cages
six-support triangular prisms
six-support octahedral cages
eight-support cubical cages.
```

No sampled body was `(1,1,0)`. The strongest one-port/two-port numerical states remained `(2,2,2)` with maximum unwanted margins on the order of `9.3e-5` to `3.5e-4`. The best near-branch linearized common margin remained negative, approximately `-2.36e-5`.

These are finite empirical screens only. They do not exclude the full continuous realization spaces of those abstract topologies. Reproducible records are under empirical.

## What changed relative to the supplied journal

The supplied frontier knew only that active row `5003` had to be destroyed or have its star crossed before the old U-H death. This continuation resolves the smallest standalone destruction topology exactly:

1. Four supports suffice to make `5003` strictly nonextreme in a positive-volume connected cage.
2. The old residual 17-gon and saddle can disappear together with `5003` from the actual irredundant hull.
3. This does not produce cancellation. A replacement `(2,2,2)` block forms.
4. The endpoint failure is controlled by an exact all-positive-external edge `(30001,30003)`, not by centroid error, inactivity of the new supports, or a hidden triangulation edge.
5. The natural homothetic activation violates death-before-birth while the old pair is still strict.
6. The obstruction persists in a certified nonzero determinant-one shear chamber.

Thus merely swallowing `5003` is necessary but not sufficient. The new supports must also be given independent escape geometry before their mutual carrier edge closes.

## Smallest genuinely unrepresented successor

The next operation must be larger than a standalone tetrahedron and materially different from the tested scalar-port attachments. A robust minimal model is a **bifurcated two-cell cage with a shared triangular or quadrilateral volume interface**.

It must act simultaneously on

```text
forcing edge       (30001,30003)
left saddle sector (14002,30001)
right saddle sector(14013,30001)
unstable sectors   [14006,14007,30002]
                   [5000,14008,30000].
```

A successful far chamber must satisfy all of the following in its rebuilt exact hull:

```text
1. row 5003 remains nonextreme;
2. at least one of 30001,30003 becomes nonextreme, or each receives an
   independent strictly nonpositive external-arrow witness;
3. both current saddle edges disappear before an adjacent edge becomes
   saddle;
4. exactly one of the two current unstable sectors survives, or a new
   single unstable feature is deliberately selected;
5. row 2475 remains the sole stable sink;
6. all three ordinary first moments are solved exactly;
7. at least two independent physical controls remain after moment closure
   for carrier suppression and saddle-death timing.
```

The most economical plausible realization uses two overlapping tetrahedral or hexahedral cells, approximately six to eight new extreme supports in total, and permits coordinated deactivation or motion of old rows `14000,14002,14012,14013`. The cells should share an actual two-dimensional interface and have at least three non-collinear outgoing ports. A single additional tip, two isolated tips, another convex-combination belt, or one-dimensional motion of `30001` repeats a mechanism already screened or exactly obstructed here.

## Verification boundary

The endpoint construction, complete rational H/V/E reconstruction, exact mass closure, exact mechanics ledgers, external-arrow theorem, activation samples, and one-parameter shear certificate were completed. The standalone clean-extraction archive, independent C++ all-triples replay, and an independent OBJ/STL parity transcript were **not completed before the computation boundary**. Accordingly, I do not represent the current directory as a contract-complete immutable package or as independently clean-room verified.

This missing replay layer does not change the exact endpoint class or the algebraic forcing-edge proof, but it is required before the endpoint should be promoted as a fully archived parent. The next copy should first add the independent all-triples and mesh-parity replays, then attack the bifurcated two-cell successor rather than repeat the tetrahedral cage or falsified belt.

## Final conclusion

**NO GÖMBÖC.** The strongest new exact object is the 22-supplied-row tetrahedral swallowing cage with actual primal `(V,E,F)=(34,51,19)`, exact ordinary-centroid closure, strict class `(2,2,2)`, positive-volume connected four-support replacement, and a certified nonzero shear chamber. It performs the previously missing literal deactivation of row `5003` and removes the old J55 residual pair, but births a replacement block before that death.

The decisive surviving component is the all-positive-external edge `(30001,30003)`, together with saddles `(14002,30001)` and `(14013,30001)`. The first genuinely nonrepeating continuation is the shared-volume bifurcated two-cell cage specified above.
