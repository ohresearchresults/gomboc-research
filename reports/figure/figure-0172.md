# figure-0172

AI research report · 2026-09-01 UTC · [Export notes](../../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI report.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../../C622/README.md) passes the supplied exact checks; the search for C<500 remains open. See [verification status and source gaps](../../catalog/coverage.md).
<!-- historical-status:end -->

---

# Vivid Quartz 58 — exact handoff

## Literal disposition

**Exact compact NONWINNER.** No homogeneous convex polyhedron with strict own-centroid `(S,U,H)=(1,1,0)` was found. The useful immutable result is a complete exact advance from `E8A` through the first requested nine-vertex topology, together with a new rigorous obstruction: throughout the certified three-control family there are two persistent strict unstable vertices, so `U>=2` and the winner-cell count is exactly zero.

The shared journal’s prior frontier was the exact dyadic `E8A`, strict `(2,2,2)`, with a `2^-14` coordinate box and a two-control rectangle forced by `S>=2`; the prior one-dimensional `E9A` continuation also retained two unstable witnesses but did not exclude the full nine-vertex realization space. This handoff leaves that excluded eight-vertex family: it replaces the whole residual disk by three interacting internal vertices, crosses five actual hull flips, and certifies all resulting incidence cells.

## Reproducible artifact

- Portable exact archive (`vivid_quartz_58_E9_prism_nonwinner.zip`)
- Archive SHA-256 (`vivid_quartz_58_E9_prism_nonwinner.zip.sha256`): `4b785641ce61fe2899a52880fbab8ecfc89d931d85410093786bfd4215a0d58b`
- Complete 501-line determination (`RESULT.md`), containing every exact V/H row, every nonincident support slack, every face/vertex/true-edge margin, every wall, and every open incidence region
- README (`README.md`), one-command verifier (`[internal-source-reference].sh`), 67-file manifest (`SHA256SUMS`)

## 1. Full exact `E8A` reconstruction

With `D=2^32`, the uncentred integer numerators for labels `[1,2,8,10,12,11,9,13]` are

```text
(530040125,643855394,-1512448411)
(-101975672,-353004289,-2568491886)
(401952773,-99192463,-2265838312)
(-919221045,-2550270254,-3079245229)
(-512240919,1524361669,10433736513)
(937145320,115523428,-743279424)
(-830715985,-399706071,-606055616)
(495015403,1118432586,341622365)
```

The exact ordinary volume, moments, and centroid are

```text
V = 10905171760828200534604875467/79228162514264337593543950336
M = (-21539638888105603626551320746659391019,
     -9535649324942179956197940290482256039,
      150194951900586327996316620510038458121)
    /4083388403051261561560495289181218537472
C = (-3077091269729371946650188678094198717/80292610405748323149698839565001818112,
     -9535649324942179956197940290482256039/562048272840238262047891876955012726784,
      150194951900586327996316620510038458121/562048272840238262047891876955012726784).
```

The verifier checks `M_j=VC_j` exactly and centred first moments `(0,0,0)`. Actual maximal faces are

```text
[12,13,9] [10,12,9] [1,9,13] [11,13,12]
[11,1,13] [11,8,1] [11,10,8] [11,12,10]
[2,10,9] [2,9,1] [2,8,10] [2,1,8]
```

and all 18 true edges are recorded in the report. The class is strict `(2,2,2)`: stable `[12,13,9]`, `[11,12,10]`; unstable `10`, `12`; saddles `(10,12)`, `(12,13)`. Minimum absolute signed normalized feature margin is `0.0025504040643727723`; minimum normalized nonincidence distance is `0.008118650934125917`. Exact interval arithmetic preserves the entire lattice and class under independent `±2^-14` perturbations of all 24 coordinate entries.

Evidence: exact report (`E8A_exact_report.json`), complete H rows (`E8A_H_representation.json`), all normalized margins (`E8A_audit.md`), perturbation certificate (`E8A_perturbation_certificate.json`), independent verifier (`verify_E8_independent.py`), OBJ (`E8A_centered.obj`), STL (`E8A_centered.stl`).

The recovered predecessor rectangle is also bundled. It keeps the six boundary vertices fixed and moves only `9,13`; all 60 support polynomials remain strict, and stable faces `[9,12,13]`, `[10,11,12]` force `S>=2`. Its exact mass identity and generator are documented in the prior result. See exact two-control atlas (`E8_two_parameter_exact_atlas.json`).

## 2. Literal residual-disk replacement

Boundary: `[1,2,8,10,12,11]`. Preserved exterior faces: `[11,10,8]`, `[11,12,10]`, `[1,11,8]`, `[2,1,8]`.

Removed disk:

```text
[12,13,9] [10,12,9] [1,9,13] [11,13,12]
[11,1,13] [2,10,9] [2,9,1] [2,8,10]
```

Replacement disk with internal vertices `A,B,C` and all three shared central edges:

```text
[A,1,2] [A,2,8] [A,8,B] [B,8,10] [B,10,12]
[B,12,C] [C,12,11] [C,11,1] [C,1,A] [A,B,C]
```

Both disks have Euler characteristic one and the same boundary. Disk f-vector changes `(8,15,8)->(9,18,10)`; global f-vector changes `(8,18,12)->(9,21,14)`. Exact patch certificate (`E8A_to_E9B_patch_complex.json`).

## 3. Exact post-replacement endpoint `E9B`

At exact parameters `s=1/8`, `a=1`, `b=7/8`, use denominator `2^36` and numerators

```text
1 (39428681832,-36122094848,-252234331904)
2 (79118164792,-149867202954,-221447174192)
8 (125866983176,-409326222704,-42540822464)
10 (68719476736,0,0)
12 (21700706104,198677699374,0)
11 (0,0,0)
A (102366804672,231475733552,-283137248696)
B (108052165760,297462448073,-103277563112)
C (24731283248,425720160880,-127045607424)
```

Exact mass data:

```text
V = 831536337117433975748327212084633/30423614405477505635920876929024
C = (4010611221118848592847054764556265466244297/4081624426691439814032368574411833964756992,
     26162350077216951834267532738414393335095879/32652995413531518512258948595294671718055936,
    -450220525980617438631913585727201234528473/255101526668214988377023035900739622797312).
```

All exact moments are in the report and satisfy `M=VC`. The actual endpoint has 14 triangular maximal faces, 21 true edges, and strict `(2,2,2)`: stable `[1,11,C]`, `[8,A,B]`; unstable `8`, `C`; saddles `(1,A)`, `(11,12)`. Thus the old intended stable `[10,11,12]` and old intended unstable `12` are both inactive; the surgery genuinely relays the packet rather than preserving it.

Minimum absolute signed normalized feature margin is `0.018827209131856603`; minimum normalized nonincidence distance is `0.019220928596724713`. All 27 coordinate entries may vary independently by `±2^-11` while preserving `(9,21,14)` and `(2,2,2)`. A clean-room Qhull/tetrahedral/Trimesh reconstruction agrees to `3.55e-15` in volume and `2.22e-16` in centroid coordinates; both meshes are watertight and winding-consistent.

Evidence: exact report with every exact mechanics component (`E9B_exact_report.json`), H representation with all nonincident slacks (`E9B_H_representation.json`), exhaustive face/vertex/edge audit (`E9B_audit.md`), perturbation certificate (`E9B_perturbation_certificate.json`), independent report (`E9B_independent_verification.json`), OBJ (`E9B_centered.obj`), STL (`E9B_centered.stl`).

## 4. Exact three-control theorem across actual incidence cells

Generator:

```text
Q_i(s)=Q0_i+s(Q1_i-Q0_i)
p_i(s,a,b)=diag(a,b,1)Q_i(s)/2^30
0<=s<=4/5, 4/13<=a,b<=13/4.
```

The complete integer matrices `Q0,Q1` are literal in the family specification (`E9_prism_family_spec.json`). These are three independent coordinate parameters; `a,b` are positive diagonal affine shape modes, not claimed as arbitrary local vertex controls.

Exact enumeration expands all `C(9,4)=126` nonzero circuit polynomials, isolates all 21 simple roots by Sturm arithmetic, reconstructs all 22 circuit-open hulls by exhaustive support tests, and merges them into six actual simplicial incidence regions. Exactly five roots are hull flips:

```text
[1,2,8,11]: diagonal [1,8] -> [2,11]
[1,11,A,C]:  [1,C] -> [11,A]
[12,11,A,C]: [11,C] -> [12,A]
[8,10,12,11]: [10,11] -> [8,12]
[8,A,B,C]: [A,B] -> [8,C]
```

Every wall is materialized as 12 common triangles plus one quadrilateral, f-vector `(9,20,13)`, with 20 true edges; no second circuit root coincides. Every wall and every open-region face/edge list is in the exact certificate (`E9_prism_exact_certificate.json`) and `RESULT.md`.

For each region the certificate stores exact integer polynomials `V6_r(s),N_r,j(s)`. With `D=2^30`,

```text
V0=V6/(6D^3), M0_j=N_j/(24D^4), C0_j=N_j/(4DV6)
V=abV0
M=(a^2bM0_x,ab^2M0_y,abM0_z)
C=(aC0_x,bC0_y,C0_z),
```

so `M=VC` identically. All regional volume polynomials are strictly positive by exact Bernstein coefficients.

For target vertex `i` and actual neighbour `j`, the denominator-cleared instability component is

```text
U_(i->j)=-[a^2(4V6Q_ix-N_x)DeltaQ_x
           +b^2(4V6Q_iy-N_y)DeltaQ_y
           +(4V6Q_iz-N_z)DeltaQ_z].
```

It is affine in `a^2,b^2`, so minima occur at the four metric corners. For vertices `8` and `C`, all actual neighbours in all six regions produce **232** corner polynomials. Every Bernstein coefficient is strictly positive. The global minimum is

```text
1720807049973636026193637957582238924211488119636178/105625
```

at region 5, component `C->A`, `a=b=4/13`. Adjacent-region certificates cover every true wall neighbour. Therefore both vertices are strict unstable everywhere in the closed box, including all five nonsimplicial walls: **`U>=2`, winner-cell count `0`**.

The route is not overstated: on the larger symmetric box `[2/7,7/2]^2`, at `s=4/5`, `a=b=2/7`, the actual `C->A` numerator is exactly

```text
-22212365956551825332914622150872065478787670917621294/153125,
```

so this persistent-`C` proof genuinely breaks there. It does not imply a winner.

The independent checker sampled 9,139 bodies over the full certified box, reconstructed exactly six simplicial hulls and 63 equilibrium classes, and found no `(1,1,0)`; its minimum persistent-unstable normalized component was `0.004633127627040464`. Independent family report (`E9_prism_independent_verification.json`).

## 5. Attempts, uncertainty, and next open topology

Transverse searches varied all nine internal coordinates, upper-triangular affine maps, and targeted `(2,1,1)` precursor packets. None produced a valid winner. The best affine runs approached zero only with condition numbers around `2.8e3–3.1e3` and support margins down to about `10^-7`, consistent with collapse toward degeneracy. These are diagnostics only; search ledger (`search_ledger.json`).

**Proved:** exact `E8A`; literal three-cell disk surgery; exact dyadic `E9B`; all endpoint V/H/incidence/mechanics; positive perturbation boxes; all actual incidence regions and walls of the stated three-control family; exact `U>=2` there.

**Unresolved:** arbitrary independent coordinates in the full nine-vertex central-triangle realization space. Therefore the smallest topology still open is the same `(9,21,14)` central-triangle type outside the affine-prism generator.

The first larger explicit fallback has four internal vertices and a central nonsimplicial quadrilateral, global f-vector `(10,23,15)`, with disk faces

```text
[A,1,2] [A,2,8] [A,8,B] [B,8,10] [B,10,C]
[C,10,12] [C,12,D] [D,12,11] [D,11,1] [D,1,A]
[A,B,C,D]
```

It is materialized but not claimed globally minimal. The prior handoff identified the same explicit fallback after the E9 line. See next topology certificate (`next_open_topology.json`).

## Reusable conclusion

`E8A` is completely reconstructed. Its entire residual disk has been replaced by a three-internal-vertex central triangle. The exact dyadic endpoint `E9B` is strict `(2,2,2)`. The complete compact family `0<=s<=4/5`, `4/13<=a,b<=13/4` crosses six actual simplicial hulls and five actual quadrilateral walls, remains exactly centred by the displayed moment identity, and has two persistent strict unstable vertices by 232 exact positive Bernstein certificates. Its explicit disposition is **NONWINNER with `U>=2`**. The full nine-vertex realization space remains the smallest open frontier.
