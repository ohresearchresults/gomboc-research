# figure-0137

Historical AI scientific report · saved 2026-08-28 UTC. Claims below retain their original status and have not all been independently checked. The current retained construction is C622; the C<500 search remains open.

---

# Exact rank-two fan-changing Minkowski atlas

## Verdict

**No winner was found.** The one-dimensional shared wall recorded in the journal has been genuinely enlarged to an exact two-coordinate deformation of the asymmetric seven-face summand `D`. The resulting codimension-two entrance has four simultaneous circuits, eight certified positive fan sectors, an isolated positive centroid root in every sector, and a complete exact own-centroid feature audit.

Every traversed sector is strictly

`(S,U,H)=(2,2,2)`.

Thus the higher-dimensional fan change is real, but it still transfers the Euler-neutral defect block rather than cancelling it. The strongest body improves the predecessor's complexity from `208` to `200`, yet remains a certified nonwinner.

## What changed relative to the supplied journal

The journal ended with the affine one-coordinate `s` direction closed after the shared wall at `s=1`, with post fan `(56,104,50)`, complexity `208`, and class `(2,2,2)`. The new work adds an independent coordinate `b`, reconstructs the exact two-dimensional circuit arrangement around `(a,b)=(0,0)` where `a=s-1`, and traverses all eight positive entrance sectors. After each fan change, the actual common refinement is rebuilt from irredundant H/V data, all mixed-volume and mixed-first-moment coefficients are re-expanded, and `(t1,t2,t3)` are re-solved as full-rank dependent centroid controls.

The fixed Minkowski scale is

`lambda = 10677075263/4294967296`.

The exact family is

`N_i(a,b)=R_i^*+a(R_i^*-R_i^0)+bQ_i`,

`h_i(a,b)=h_i^*+a(h_i^*-h_i^0)+N_i(a,b)·dshift`,

with independent second-direction matrix `Q/2^30` and numerator rows

```text
[  402345185,  749186498,  547594572]
[  366795588,  -70940912,  622966337]
[  521946923,  190802047,    2485404]
[ -175807935, -597856240,  595910948]
[-1055548697, -179880596,   79883822]
[  417876669,  856114940,  482725797]
[ -141670738,  353848327, -613100213]
```

All remaining exact family coefficients are materialized in `D_family_parameterization.csv`.

## Shared codimension-two entrance

At `(a,b)=(0,0)`, `D` is irredundant with `(V,E,F)=(10,15,7)` and the actual common-refinement wall is `(51,90,41)`. Four exact circuit polynomials vanish simultaneously:

| Circuit | P9 ray | D rows |
|---|---:|---:|
| `A13` | `13` | `(3,4)` |
| `A26` | `26` | `(2,3)` |
| `A9` | `9` | `(2,6)` |
| `A100` | `100` | `(3,5)` |

Their complete exact coefficients in the bivariate basis `1,a,b,a²,ab,b²` are in [entrance_circuits.csv](sandbox:/mnt/data/minkowski_2d_atlas_exact_nonwinner/entrance_circuits.csv). The global verifier regenerates those coefficients from the exact family, reconstructs the entrance H/V bodies, enumerates all `317` candidate circuits on each radial chamber, and proves that no additional active circuit occurs on any open sample ray.

## Exact common-fan atlas and isolated moment roots

For every cell, the exact perturbation box is

`B = [t1*−2^-36,t1*+2^-36] × [t2*−2^-36,t2*+2^-36] × [t3*−2^-36,t3*+2^-36]`.

Each box is wholly positive, its exact Krawczyk image lies strictly in its interior, and therefore it contains a unique isolated positive root of `(Mx,My,Mz)=0`. The same box retains the actual common fan and has every face, vertex, inactive H/V inequality, and all four components of every true-edge cone strictly decided.

| Cell | Signs `(A13,A26,A9,A100)` | Exact `(a,b)` | Common `(V,E,F)` | Complexity `2E` | Exact Krawczyk-box midpoint `(t1,t2,t3)` | Class |
|---|---|---|---:|---:|---|---:|
| `E0_ppmp` | `++-+` | `(1/8388608,1/67108864)` | `(56,104,50)` | `208` | `(543656559932257/281474976710656, 3248266066963/1152921504606846976, 5544083371118023/70368744177664)` | `(2,2,2)` |
| `E1_mpmp` | `-+-+` | `(1/8388608,1/33554432)` | `(57,106,51)` | `212` | `(8699039295141355/4503599627370496, 6846987313557/288230376151711744, 2772044668564383/35184372088832)` | `(2,2,2)` |
| `E2_mmmp` | `---+` | `(-3/134217728,13/536870912)` | `(59,110,53)` | `220` | `(8699239654190467/4503599627370496, 720484362087/72057594037927936, 346505804157781/4398046511104)` | `(2,2,2)` |
| `E3_mmpp` | `--++` | `(-1/16777216,9/268435456)` | `(57,106,51)` | `212` | `(8699612759749545/4503599627370496, 36093459987005/1152921504606846976, 5544098479537635/70368744177664)` | `(2,2,2)` |
| `E4_mmpm` | `--+-` | `(-5/8388608,-1/16777216)` | `(57,106,51)` | `212` | `(2174350433730003/1125899906842624, 18566730789289/1152921504606846976, 5544081869546053/70368744177664)` | `(2,2,2)` |
| `E5_pmpm` | `+-+-` | `(-7/8388608,-9/8388608)` | `(56,104,50)` | `208` | `(542304091894271/281474976710656, 16126501830931/576460752303423488, 2771843340212167/35184372088832)` | `(2,2,2)` |
| `E6_pppm` | `+++-` | `(13/67108864,-1/4194304)` | `(54,100,48)` | `200` | `(271646439800381/140737488355328, 9537801108145/576460752303423488, 5543983294457625/70368744177664)` | `(2,2,2)` |
| `E7_ppmm` | `++--` | `(1/8388608,1/134217728)` | `(56,104,50)` | `208` | `(2174566987679119/1125899906842624, 606306764419/576460752303423488, 2772040350837079/35184372088832)` | `(2,2,2)` |

The exact lower and upper endpoints, not only the midpoint-radius form, are indexed in [root_boxes.csv](sandbox:/mnt/data/minkowski_2d_atlas_exact_nonwinner/root_boxes.csv).

## Exact mixed-volume and mixed-first-moment coefficients

Every traversed cell has its own exact actual-fan expansion in `(t1,t2,t3)`:

- `20` rational volume coefficients;
- `35` rational coefficients for each of `Mx`, `My`, and `Mz`;
- `125` nonzero exact coefficients per cell.

| Cell | Coefficient-file SHA-256 |
|---|---|
| `E0_ppmp` | `351340f0c374442163006ed84eb859076ec9355a4426d73f363244046a920811` |
| `E1_mpmp` | `0bc09e99ff9ae9bf8e0581225686d423ab4725313c15fd802c74baa4eff04be7` |
| `E2_mmmp` | `4293173f1cca30323b5d4de9302adf37bf01a922585fd2d458f2fb441f58901c` |
| `E3_mmpp` | `2b81d21df5352cab71b7f6317ea610b2985e467a2d0f6aebfcad8c1042b917fb` |
| `E4_mmpm` | `c94f3de694567acf04a2f418a0619372317eff388feb6f7ddc0b2cd2b2bbf565` |
| `E5_pmpm` | `940bc68ffc055f2a0b98f5cb16d3ae71df922b01047cfe3b021703a0caf4846b` |
| `E6_pppm` | `e2cf920e486e34c33d3c54b68864b0d7df1ec3bf2c5bbc4514309dddd0e3aca2` |
| `E7_ppmm` | `2a1ffa93509899cb1967b1340c5c2214932cd5214f6ddec64865cb8ee66800a9` |

The per-cell files and counts are indexed by [mixed_coefficients_manifest.csv](sandbox:/mnt/data/minkowski_2d_atlas_exact_nonwinner/mixed_coefficients_manifest.csv). `verify_independent.py` regenerates the coefficients from the affine H/V body rather than trusting these exports.

## Exact circuit transitions

Each exact straight segment between cyclic neighboring samples crosses one and only one active entrance circuit. Other determinant roots, when present, are isolated exactly and certified outside the relevant positive cone.

| Transition | Active circuit | Exact segment-parameter root box | Total roots / inactive roots | `Δ(V,E,F)` | `Δ(S,U,H)` |
|---|---|---|---:|---:|---:|
| `E0→E1` | `A13` | `[224246852330217427936601609/1237940039285380274899124224, 112123426165108713968300805/618970019642690137449562112]` | `1 / 0` | `(1,2,1)` | `(0,0,0)` |
| `E1→E2` | `A26` | `[56965181935399891142854063/77371252455336267181195264, 911442910966398258285665009/1237940039285380274899124224]` | `4 / 3` | `(2,4,2)` | `(0,0,0)` |
| `E2→E3` | `A9` | `[383146380244776698024815703/1237940039285380274899124224, 47893297530597087253101963/154742504910672534362390528]` | `2 / 1` | `(-2,-4,-2)` | `(0,0,0)` |
| `E3→E4` | `A100` | `[212250246202331681940656273/309485009821345068724781056, 849000984809326727762625093/1237940039285380274899124224]` | `1 / 0` | `(0,0,0)` | `(0,0,0)` |
| `E4→E5` | `A13` | `[8985590424714736083998549/309485009821345068724781056, 35942361698858944335994197/1237940039285380274899124224]` | `1 / 0` | `(-1,-2,-1)` | `(0,0,0)` |
| `E5→E6` | `A26` | `[14908333804643203674882157/38685626227668133590597632, 477066681748582517596229025/1237940039285380274899124224]` | `4 / 3` | `(-2,-4,-2)` | `(0,0,0)` |
| `E6→E7` | `A9` | `[277431394206164911650598919/618970019642690137449562112, 554862788412329823301197839/1237940039285380274899124224]` | `2 / 1` | `(2,4,2)` | `(0,0,0)` |
| `E7→E0` | `A100` | `[167952533025682801241071109/1237940039285380274899124224, 83976266512841400620535555/618970019642690137449562112]` | `1 / 0` | `(0,0,0)` | `(0,0,0)` |

The exact removed and added lineages, cone intervals, and inactive-root witnesses are in [transition_summary.csv](sandbox:/mnt/data/minkowski_2d_atlas_exact_nonwinner/transition_summary.csv) and `transition_path_certificate.json` inside the full bundle.

## Complete defect-transfer audit

Across all eight sectors:

- protected stable face `P9:27` remains critical;
- protected intended source `(15,26,27)` remains, always with `D` active triple `[0,4,5]`;
- unwanted source `(9,32,103)` remains, always with `D` active triple `[1,2,6]`;
- the extra stable feature alternates between `P9:13` and the mixed lineage `P9edge(13,15)|Dedge(n17,n10)`;
- the inherited saddle alternates among `P9:13/P9:26` and mixed `P9edge(13,26)` lineages;
- the return saddle alternates among `P9:100` and mixed `P9edge(27,100)` lineages.

Therefore every traversed circuit changes the actual fan but has `Δ(S,U,H)=(0,0,0)`. The cell-local feature IDs, edge endpoints, active rows, and exact lineages are in [critical_transfer_ledger.csv](sandbox:/mnt/data/minkowski_2d_atlas_exact_nonwinner/critical_transfer_ledger.csv).

## Strongest materialized body

The strongest cell is `E6_pppm`:

- exact shape sample: `(a,b)=(13/67108864,-1/4194304)`;
- actual common fan: `(V,E,F)=(54,100,48)`;
- mechanical complexity: `200`;
- unique positive moment root in the exact `2^-36` box centered at
  `(271646439800381/140737488355328, 9537801108145/576460752303423488, 5543983294457625/70368744177664)`;
- exact midpoint Jacobian determinant is nonzero, approximately `0.15937930561821317`;
- exact rational midpoint body translated by its exact rational own centroid;
- exact first moment after that translation: `(0,0,0)`;
- exact volume approximately `788.288240468534`;
- direct audit covers `48` faces, `54` vertices, `100` true edges, and all `400` edge-cone components;
- class: `(2,2,2)`.

Descriptive normalized midpoint margins are:

| Quantity | Margin |
|---|---:|
| Minimum inactive H/V gap | `1.2206412769444341e-08` |
| Minimum stable component | `16.19694566439219` |
| Closest excluded face witness | `-1.3455964714983475` |
| Minimum unstable component | `1.3824118391164555` |
| Closest excluded vertex witness | `-0.35572267506732963` |
| Minimum saddle component | `15.449140583108866` |
| Closest excluded edge witness | `-0.0006473053595072997` |

The proof uses exact rational interval files, not these decimal summaries.

The materialized H/V body is the exact rational box midpoint translated to its own centroid; the algebraic moment root itself is represented by its strict rational Krawczyk box rather than asserted to equal the midpoint. Because the complete mechanics audit is strict throughout that box, both the isolated root and the materialized representative belong to the same `(2,2,2)` chamber.

Mesh verification passes with `54` vertices, `104` triangles, `156` mesh edges, Euler characteristic `2`, exact agreement with the exported face triangulation, and zero parsed coordinate discrepancy against the exact CSV representation. Hashes:

- OBJ: `6aaeb45c0e2a85238a29295359328d092024e94ca4c7e186078f507ce7d924ab`
- STL: `76c3ad5a12b718ba6c41aa6189c185cde357b2e3db653744eb5d6aa441513ae3`

[Strongest exact H data](sandbox:/mnt/data/minkowski_2d_atlas_exact_nonwinner/strongest/body_midpoint_centered_H.csv) · [Strongest exact V data](sandbox:/mnt/data/minkowski_2d_atlas_exact_nonwinner/strongest/body_midpoint_centered_V.csv) · [OBJ mesh](sandbox:/mnt/data/minkowski_2d_atlas_exact_nonwinner/strongest/strongest_E6_pppm.obj) · [STL mesh](sandbox:/mnt/data/minkowski_2d_atlas_exact_nonwinner/strongest/strongest_E6_pppm.stl)

## Independent verification

The bundle contains independent scripts that read the exported exact files rather than construction checkpoints:

- `verify_independent.py`: reconstructs each `D`, the actual common H/V body, irredundancy, exact mixed coefficients, Krawczyk inclusion, inactive inequalities, and the complete face/vertex/four-component-edge audit;
- `audit_direct_centered.py`: independently integrates each exact rational midpoint body, translates it to its exact centroid, and repeats the complete feature audit;
- `verify_global.py`: regenerates all four entrance polynomials, the exact entrance wall, and `317` candidate circuits per radial chamber;
- `verify_transition_paths.py`: isolates all roots on every inter-cell segment and proves exactly one active crossing;
- `verify_minkowski_expansion.py`: proves every affine body vertex is literally `B+t1C1+t2C2+t3C3+lambda D` and every common-face support function agrees;
- `verify_strongest_mesh.py`: checks the materialized mesh against exact H/V data.

All eight cell verifiers, the global common-fan verifier, the transition verifier, the exact Minkowski-expansion verifier, the direct own-centroid audits, and the strongest mesh verifier report `PASS`. See [verification_summary.json](sandbox:/mnt/data/minkowski_2d_atlas_exact_nonwinner/verification_summary.json).

## Scope and unresolved uncertainty

This is a rigorous negative result for **this exact rank-two family and its eight certified entrance sectors**. It is not a proof that every possible two-coordinate deformation of `D` fails. The certified rectangular perturbation boxes are three-dimensional boxes in the dependent controls `(t1,t2,t3)` at fixed exact shape samples; the two-dimensional shape chambers themselves are certified by exact circuit signs, ray certificates, and exact one-wall transition paths rather than by one combined rectangular five-dimensional box.

No finite own-centroid strict `(1,1,0)` body is claimed.

## Nonrepeating higher-dimensional continuation

The rank-two entrance mechanism is now exhausted. The next search should start from `E6_pppm`, not repeat the four entrance circuits.

1. Add a source-targeting coordinate supported on `D` rows `1,2,6`, selected from the exact nullspace of the protected `[0,4,5]` cone constraints, so that one of P9 rays `9,32,103` is forced out of the unwanted source cone.
2. Add an independent coordinate targeting the exact `13/26` mixed saddle packet listed in the transfer ledger.
3. Add an independent coordinate targeting the `27/100` return packet, especially the `(n14,n24)` and `(n17,n24)` lineages, while keeping every row-27 protection inequality positive.
4. If those three circuit gradients become rank-deficient under the protection constraints, add a fourth support/normal coordinate to separate the packets while retaining all seven irredundant faces of `D`.

Retain `(t1,t2,t3)` as dependent full-rank moment controls and re-expand the actual-cell mixed polynomials after every new circuit. Rank three is the first genuinely untested possibility; rank four is the safer design because it gives one independent target direction for the unwanted source and for each of the two saddle packets after protection constraints are imposed.

## Artifacts

The `tar.zst` archive is the smaller full bundle; the store-mode ZIP is provided for compatibility.

- [Full exact bundle — TAR.ZST](sandbox:/mnt/data/minkowski_2d_atlas_exact_nonwinner.tar.zst) — `201,441,299` bytes; SHA-256 `4b9d9fa9338d9c39c922f2f907d1446346161bf90c5af5e3b8aacdca02552794`
- [TAR.ZST checksum](sandbox:/mnt/data/minkowski_2d_atlas_exact_nonwinner.tar.zst.sha256)
- [Full exact bundle — ZIP](sandbox:/mnt/data/minkowski_2d_atlas_exact_nonwinner.zip) — `470,017,599` bytes; SHA-256 `e07617607206d53f0e6ba3151715694a295c1b9b46b6ded282992170a201d650`
- [ZIP checksum](sandbox:/mnt/data/minkowski_2d_atlas_exact_nonwinner.zip.sha256)
- [Detailed README](sandbox:/mnt/data/minkowski_2d_atlas_exact_nonwinner/README.md)
- [Complete exact atlas](sandbox:/mnt/data/minkowski_2d_atlas_exact_nonwinner/atlas.json)
- [Integrity manifest](sandbox:/mnt/data/minkowski_2d_atlas_exact_nonwinner/manifest.sha256)
