# figure-0489

AI research report · 2026-09-22 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# SC83 — actual-U1 material descendants and an exact full point-cell blocker

## Outcome

No strict110 body is claimed. This continuation produced two substantive advances beyond the closed C180 affine orbit:

1. **Actual uniformly filled U1 descendants:** two exactly reconstructed **V30/E84/F56, C168, strict211/additionalweak000** bodies. One has a 60-bit common centred-coordinate denominator and an explicit full-SPD sign neighbourhood. The other has an improved polar landscape, an 87-bit denominator, and a complete remaining **Q22/18** packet. These are genuine material changes, not metrics on the excluded C180 shape.
2. **A uniform root-transfer obstruction on the original insertion chart:** throughout the **entire strict Q10 point-visibility cell**, not merely the old radius-1/25 box, every symmetric Gram matrix satisfying `max_ij |G_ij-I_ij| <= 31/500` has at least two **strict** physical unstable vertices at the actual filled centroid. This handles transfer from the old root to the inserted point. It does not exclude the rest of SPD or changed retained supports.

I also preserve an exact **C168 strict413** bridge control and a complementary **V48/E72/F26, C144, strict121** support-turnover control. All four have additionalweak000 and primitivezero000. None is asserted to improve the project's global complexity record.

## 1. Input authority and verification status

The authoritative parent is `figure-0483`, advertised immutable SHA-256 `c050f59f0ccac9a3ad07156ff653f2048bce8766491af7c39f98d124a5114421`. The complete journal update and supplied literal parent/source units were read. The mounted update is 223074 bytes, SHA-256 `74aba1796596a72830cefb2a69da4795e975ca35aef5ed1940c63a9aa61fff0a`.

The underlying literal C180 reconstructor is included intact: **17276 bytes**, SHA-256 `033968bb2c49df312a8d92cc89d3a2e015404b329529761fe824f77ec34aabe7`. Its exact rows, cap and affine map remain the authority for the point-cell theorem. No C198 result is transferred. The already completed fixed-C180 SPD exclusion was not rediscovered.

All exact results below were replayed from the final inline source capsule in a fresh directory. The replay matched **17 complete output hashes**. It uses CPython 3.13.5 standard-library arithmetic only. The optional numerical methods use the observed NumPy 2.3.5, SciPy 1.17.0 and Torch 2.10.0+cpu, with one thread and float64.

Verification tier: exhaustive integer supporting-V-triples and the inherited exhaustive H-triple reconstruction provide distinct hull checks; there is **one full mechanical auditor**, not two independent implementations. That auditor checks three exact mass identities, the true maximal complex, all stable/unstable and mixed-edge predicates, additional weak equilibria, primitive zeros, and complete physical and same-physical-centre polar landscapes. The inherited tetra446, weak-prism and unbounded-H controls pass. The point-cell theorem additionally has exact polynomial, matrix and finite-domain checks independent of the numerical nominators.

## 2. Exact theorem on the entire C176 insertion cell

### Geometry and actual mass

Use the parent's raw `AFFINE222` frame and old indices. The inserted point sees exactly

`X=[1,2,3,4,5,15,16,17,18,30]`.

For each old maximal plane `n_i.x <= h_i`, let sigma_i be +1 on X and -1 otherwise. The strict visibility cell is

`Pi={q: sigma_i(n_i.q-h_i)>0 for every old face i}`.

Its exact bounded closure has **6 vertices, 9 edges and 5 maximal faces**. Its active old planes are **1,2,8,14,31**. The complete rational cell vertices and planes are generated in `SC83_FULL_VISIBILITY_BLOCK.json`. Thus the old retained supports8/14 and cap31 really do bound the whole chart; the radius-1/25 box was only a small inner subset.

For every q in Pi the new physical body is `conv(K,q)` with the same C176 insertion incidence. The old outside geometry is fixed. The actual finite mass is

`V(q)=V0+V1.q`,

`M(q)=M0+ML*q+q*(V1.q)/4`,

`c(q)=M(q)/V(q)`.

For an outward triangle `(a,b,c)` of a visible old face, set `w=(b-a)x(c-a)`, `h=det(a,b,c)`, and `s=a+b+c`. Starting from the old exact volume and first moment, add

`V0 -= h/6`, `V1 += w/6`,

`M0_i -= h*s_i/24`,

`ML_ik += (s_i*w_k-h*delta_ik)/24`.

Every coefficient is regenerated exactly. At `p0=(7/5,1/10,-2/5)` these formulas match the independently rebuilt H-body's actual volume and first moment exactly, with census52/88/38 and strict(11,2,11). Volume positivity is also checked at all six cell vertices. These coefficients are **not reused** after changing retained supports or freely moving the outside vertices.

### Two protected basins, including root transfer

Keep the old labels and give the moving point label60. The protected disjoint sets are

`B0={2}`, `B1={54,56,58,59,60}`.

Their complete outgoing true-edge boundaries are:

```json
[[[2,0],[2,6],[2,57]],[[54,17],[56,10],[58,6],[59,45],[59,57],[60,17],[60,18],[60,19],[60,20],[60,21],[60,29],[60,31],[60,33],[60,35],[60,36],[60,38],[60,45]]]
```

For every point in Pi and every Gram matrix in the stated box, all20 outgoing scores are strictly negative. Consequently vertex2 is strict U. Independently, a vertex of maximal G-radius inside B1 has negative internal outgoing scores, since

`2 x_i^T G(x_j-x_i)=|x_j|_G^2-|x_i|_G^2-|x_j-x_i|_G^2<0`

whenever i is a maximal-radius member and j is another member. Its external arrows are negative by the certificate, so B1 contains another strict U. This is why merely making old root59 escape cannot solve the chart: the second root may transfer within B1, particularly to the inserted point.

### Complete exact coefficient certificate

Write q as a convex combination of the six exact cell vertices. The numerator

`V(q)*(p_i-c(q))^T G(p_j-p_i)`

is quadratic for the eight old-to-old boundary arrows and cubic for the twelve moving-point-to-old arrows. Symmetric homogeneous polarization gives **8*21 + 12*56 = 840** exact symmetric3x3 coefficient matrices A.

For every coefficient the verifier proves

`tr(A)+(31/500)*sum_ij |A_ij| < 0`.

Thus every convex-combination coefficient remains negative for every `|G_ij-I_ij|<=31/500`. Such G is automatically SPD. The complete bank is regenerated, including every rational matrix entry; no numerical eigenvalue is used as proof. The polarization also matches direct evaluation exactly at the nonsymmetric rational convex combination with weights `(1,2,3,4,5,6)/21`.

The limiting coefficient for this sufficient entrywise estimate is the arrow **60→45**, multiset **[0,0,3]**. The radius31/500 is a certified rational choice, not the largest possible geometric metric neighbourhood.

**Scope:** all strict q in this entire visibility cell, all symmetric G in the explicit box, and all positive scalar multiples of those G. This is not all-SPD coverage, not another visibility cell, and not a retained-support deformation theorem.

## 3. Actual new material controls

The numerical point/three-carrier/metric trials did not produce U1. The successful route used broader vertex and support turnover: a finite log-radius bridge, followed by a positive-parent forest objective evaluated at the **rebuilt actual centroid**. Subsequent polar repair and bar descent were guarded by the physical forest. Numerical witnesses and soft convexity penalties nominated shapes only; the exact frozen hulls establish the following results.

| Exact object | V/E/F; C | Strict S/U/H | Centred denominator bits | Final-edge headroom |
|---|---|---|---:|---:|
| `SC83_QCAP_BRIDGE30_C168_413_G4` |30/84/56;168|4/1/3|60|165|
| `SC83_QCAP_REPAIR30_C168_211_G4` |30/84/56;168|2/1/1|60|165|
| `SC83_QCAP_TQ30_C168_211_G6` |30/84/56;168|2/1/1|87|165|
| `SC83_DUALBRIDGE26_C144_121_N4` |48/72/26;144|1/2/1|3292|177|

Every row has **additionalweak000 and primitivezero000**. The first three are simplicial actual bodies; E84 is the true edge count, not an unmerged triangulation count. The last is simple. The denominator bit count is not a maximum coordinate bit count or a complexity bound.

### Main continuation endpoint: C168 strict211, grid10^6

For `SC83_QCAP_TQ30_C168_211_G6`:

`S=[21,55]`, `U=[29]`, `H=[[16,24]]`.

Its exact raw volume is

`6056987155808159273/1500000000000000000`.

Its exact raw filled centroid is

```text
(39811311967989921638069059,
 21064699612607211429139189,
 -20789115494444669605713937)
/96911794492930548368000000.
```

Define the raw body as the convex hull of these complete30 integer triples divided by1000000, and the own-centred body by subtracting that centroid:

```json
[[-1004740,-306697,-347110],[-979874,-152512,-589868],[-979263,-439305,-98403],[-960840,234386,-506700],[-920207,-521410,147851],[-907160,241291,-749980],[-830721,-574115,370098],[-799174,437796,-339405],[-765184,-136902,-941866],[-706572,-623230,567813],[-704469,565678,-911221],[-552007,-661200,748176],[-522879,-564521,-777270],[-377786,-663698,920458],[-375767,827541,-523979],[-364906,-288261,-1096362],[-312869,681326,-1154587],[-185373,-633653,1077737],[-126611,831672,-478048],[32630,-577591,1215475],[124351,265377,-1199439],[288515,-501526,1325659],[565761,-413416,1389001],[856548,-282241,1412709],[902444,1109574,-957554],[1297246,-74366,1356130],[1352450,476628,-1191706],[1876848,237043,1087364],[2481132,628094,401983],[2598489,878261,-156934]]
```

The physical bar list is empty. The remaining Q bar has22 vertices and18 boundary edges. Exact quality brackets are

`r/R in [174314039994,174314039995)/10^12`,

`TQ in [9420445292610,9420445292611)/10^12`,

`relative Q depth in [814444608638,814444608639)/10^12`.

This improves the polar bar of the compact grid10^4 strict211 control, whose relative depth is in `[899975048372,899975048373)/10^12` and TQ in `[16441835334868,16441835334869)/10^12`. The residual bar is still deep; no near110 assertion is intended.

### Complementary S1 support control

`SC83_DUALBRIDGE26_C144_121_N4` has `S=[19]`, `U=[1,47]`, `H=[[19,24]]`. Its volume is approximately0.8574312389814415 and raw actual centroid approximately `(0.28333756476025906,0.17255952687330514,-0.18310583239248188)`. The complete exact volume, first moment and centroid are regenerated, not replaced by these decimals.

Its complete26 minimal raw H rows `(n_x,n_y,n_z,h)` are:

```json
[[-18972,22423,5249,10000],[-15795,6476,-17742,10000],[-9127,25175,18766,10000],[-7820,22499,4081,10000],[-7710,94,-4953,10000],[-6135,19585,-1794,10000],[-5825,928,-10157,5000],[-5381,-6085,-22395,10000],[-5300,5948,-15599,10000],[-5028,-3355,-3530,10000],[-4739,-3547,-3020,10000],[-4121,12013,5047,5000],[-3581,21819,8878,10000],[-1356,21675,25796,10000],[1742,-10441,-10645,5000],[3836,17363,29481,10000],[5547,15634,32500,10000],[6306,2637,18901,5000],[7427,12399,36238,10000],[10848,-21709,-2402,5000],[15369,489,37585,10000],[17417,-3931,37244,10000],[19461,-8947,35974,10000],[19825,-36200,-1118,10000],[22249,-16868,31813,10000],[24599,-28355,21826,10000]]
```

It comes from normal/support-space bridge enrichment and actual H-mass repair, not from treating a separately centred polar as a uniformly filled physical solution. Its Q bar list is empty; the one P packet is21/17. TP is in `[7008800394369,7008800394370)/10^12`.

## 4. Complete surviving P/Q interfaces

Indices below are the exact reconstructed indices of each named body. Exact birth/death levels, depths, all vertices/planes and all other audit fields are regenerated in its `_A.json` output. No component or boundary is abbreviated here.

```json
{
"SC83_QCAP_TQ30_C168_211_G6":{"P":{"roots":[29],"bars":[]},"Q":{"roots":[21,55],"bars":[{"peak":21,"elder":55,"death_edge":[5,42],"component":[0,1,2,3,5,8,9,10,11,12,13,14,16,18,20,21,24,27,29,31,32,36],"boundary":[[1,53],[2,55],[5,42],[8,43],[10,37],[11,33],[12,45],[14,28],[20,44],[21,50],[24,23],[24,38],[27,48],[27,54],[31,45],[31,51],[32,15],[32,46]],"path":[21,18,36,5,42,39,41,52,47,55]}]}},
"SC83_QCAP_REPAIR30_C168_211_G4":{"P":{"roots":[29],"bars":[]},"Q":{"roots":[0,52],"bars":[{"peak":0,"elder":52,"death_edge":[37,46],"component":[0,1,2,4,5,9,10,12,16,18,19,20,21,22,24,30,33,34,35,36,37,38,39],"boundary":[[0,53],[1,52],[2,47],[10,14],[16,50],[19,13],[19,17],[20,42],[22,44],[30,3],[30,15],[33,6],[34,47],[35,41],[36,43],[37,46],[38,49],[39,45],[39,54]],"path":[0,4,9,37,46,26,40,48,51,52]}]}},
"SC83_QCAP_BRIDGE30_C168_413_G4":{"P":{"roots":[29],"bars":[]},"Q":{"roots":[9,19,25,55],"bars":[{"peak":25,"elder":9,"death_edge":[9,25],"component":[25],"boundary":[[25,9],[25,36],[25,37]],"path":[25,9]},{"peak":19,"elder":55,"death_edge":[19,43],"component":[11,19],"boundary":[[11,6],[11,53],[19,32],[19,43]],"path":[19,43,49,51,55]},{"peak":9,"elder":55,"death_edge":[6,11],"component":[0,1,3,4,6,7,8,9,10,14,17,21,23,25,26,27,28,29,30,34,35,36,37],"boundary":[[0,41],[4,5],[4,16],[6,11],[7,44],[8,47],[9,54],[17,42],[21,52],[21,53],[23,46],[26,48],[27,39],[28,33],[29,18],[29,38],[30,50],[34,45],[36,55]],"path":[9,25,37,6,11,19,43,49,51,55]}]}},
"SC83_DUALBRIDGE26_C144_121_N4":{"P":{"roots":[1,47],"bars":[{"peak":1,"elder":47,"death_edge":[19,24],"component":[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,23],"boundary":[[1,42],[8,43],[9,36],[10,40],[11,36],[13,32],[14,20],[15,25],[16,26],[16,34],[17,29],[18,35],[18,39],[19,21],[19,24],[23,30],[23,32]],"path":[1,0,2,3,4,19,24,45,46,47]}]},"Q":{"roots":[19],"bars":[]}}
}
```

## 5. Exact feasible SPD cells on the new U1 geometries

These are positive feasible-cell certificates, not exclusions. They use the actual centroid and complete true-edge/face data of the new rational bodies.

For a physical arrow, use its exact symmetric matrix A with score `tr(GA)`. For a polar arrow use `tr(adj(G)A)`. If `|G_ij-I_ij|<=e`, then

`|adj(G)_ij-I_ij| <= 2e+2e^2`.

Exact trace/L1 bounds preserve signs. The full-cell check includes every directed physical true edge and every ordered polar vertex pair. Mixed-edge H is checked against the full auditor: both physical directed scores and both corresponding polar directed scores must be negative. Preserving these signs preserves the full strict/weak/mixed census and primitivezero000.

| Body | U1-only radius | S/U-count radius | Full primitive-sign radius |
|---|---:|---:|---:|
| G4 strict211 |1/4096|1/8192|1/8192|
| G6 strict211 |1/2048|1/524288|1/1048576|

All radii are entrywise boxes about I. They are sufficient, not optimal. Complete positive physical and polar parent selections and exact limiting ratios are generated in the `_METRIC_CELL.json` files. This supplies explicit full-dimensional SPD starting cells for continuation instead of only a floating metric sample.

## 6. What worked, what did not, and the next concrete geometry

Finite point/metric/three-carrier nominations did not reach the target; those failures are not exclusions. Broad material turnover succeeded in creating U1. The reusable method is a finite great-circle/log-radius bridge, actual-hull mass rebuilding, and a positive-parent forest directed toward one root. A complete-point positive forest is sufficient to eliminate all other U even when a selected parent is not a true edge. Exact final certification nevertheless uses the actual true complex.

The dual repair used the analogous forest on the same-physical-centre polar, with actual material centroid feedback. Fixed old triangle/vertex witnesses and soft convexity penalties were only optimization devices; their feasibility was never substituted for the actual final hull. The exact frozen controls and their positive SPD cells are the durable results, not an assertion that every intermediate numerical trial remained in the same equilibrium class.

The most useful continuation is the **G6 C168 strict211 body**, its empty P landscape, sole Q22/18 packet and165-edge headroom. Its sole saddle is physical edge16–24, dual to the Q death edge5–42. Preserve or rebuild a strictly positive physical forest while changing the complete Q cut, rather than protecting only vertex29 or deleting only Q peak21. The G4 control gives a simpler-coordinate and larger full-sign-cell starting point. The C144 mirror provides an alternative S1-first route with a complete P21/17 packet and177-edge headroom.

The original C176 chart remains open outside the certified Gram cone, and support changes8/14/31 leave the new theorem's scope. The full affine orbits and material neighbourhoods of the new C168/C144 controls are also unresolved. No C180 obstruction is transferred to them.

## 7. Complete recovery capsule

The inline capsule contains **22 complete source/input files**: the literal parent, exact new point/support definitions, both exact hull/freezing methods, mass and full mechanics/landscape auditor, the840-matrix generator/checker, feasible SPD-cell checker, complete report generator,17 expected output receipts, and complete reusable numerical-method dependency closure. Numerical continuation commands start from the exact bodies written by the replay. Historical optimizer trajectories are not required to reconstruct or verify any claimed body.

Save the decoder as `RECOVER_SC83_FINITE_INLINE.py` and run:

```sh
python -B -S RECOVER_SC83_FINITE_INLINE.py SC83_FINITE_REPLAY
cd SC83_FINITE_REPLAY
python -B -S REPLAY_SC83_FINITE.py
```

Expected decisive markers include:

```text
SC83_FULL_POINT_VISIBILITY_CELL_PASS 6 9 5
SC83_POINT_CHART_ACTUAL_MASS_CHECK_PASS 52 88 38
SC83_TWO_PROTECTED_BASINS_840_COEFFICIENTS_PASS
SC83_FULL_VISIBILITY_GRAM_BOX_EXCLUSION_PASS 31/500
SC83_EXACT_MATERIAL_SPD_CELLS_PASS
SC83_NEW_FOUR_MATERIAL_MASS_AND_COMPLETE_INTERFACES_PASS 4
SC83_FINITE_SEVENTEEN_OUTPUT_HASHES_PASS 17
SC83_ACTUAL_MASS_C168_211_C144_121_AND_FULL_POINT_CELL_HANDOFF_PASS
```

The source dictionary is **89447 bytes**, SHA-256 `19cfd3720ac7dd6bf1c34bd840ca3aaf017ea0d6a0d570b9b51a70596dfd0d4b`. Its XZ representation is **24448 bytes**, SHA-256 `6035ead1c0ff9013a35aed1fe029c8a3d9caa137b606ec6098bc02f996e4cc99`, encoded in32600 nonwhitespace base64 characters.

The full point-cell report is26755 bytes, SHA-256 `3ebc619d29770e5601cf0b8c9163a2ca262ee636f741eb6b7a19e64480147416`; the complete840-matrix bank is18864051 bytes, SHA-256 `b28e372c18b32372c1e08b3f44c9a3b3539a5661a18012ce12dbb54a2d8b7936`. The generator reconstructs that large bank compactly; it is not an ephemeral object behind a hash.

Convenience copies, not dependencies of the inline recovery: [complete source/audit bundle](sandbox:/mnt/data/SC83_FINITE_GEOMETRY_HANDOFF.zip), [source-only bundle](sandbox:/mnt/data/SC83_FINITE_SOURCE_ONLY.zip), and [decoder](sandbox:/mnt/data/RECOVER_SC83_FINITE_INLINE.py).

```python
# Complete exact definitions/auditors and reusable finite nomination sources.
import base64,hashlib,json,lzma,pathlib,sys
B64='''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'''
z=base64.b64decode(B64)
assert len(z)==24448 and hashlib.sha256(z).hexdigest()=='6035ead1c0ff9013a35aed1fe029c8a3d9caa137b606ec6098bc02f996e4cc99'
b=lzma.decompress(z)
assert len(b)==89447 and hashlib.sha256(b).hexdigest()=='19cfd3720ac7dd6bf1c34bd840ca3aaf017ea0d6a0d570b9b51a70596dfd0d4b'
files=json.loads(b);assert len(files)==22
out=pathlib.Path(sys.argv[1] if len(sys.argv)>1 else 'SC83_FINITE_REPLAY');out.mkdir(parents=True,exist_ok=True)
for name,text in sorted(files.items()):
 assert pathlib.Path(name).name==name
 x=text.encode();(out/name).write_bytes(x)
 print('SC83_SOURCE_FILE',name,len(x),hashlib.sha256(x).hexdigest())
print('SC83_FINITE_SOURCE_RECOVERY_PASS',len(files),len(b),hashlib.sha256(b).hexdigest())
```
