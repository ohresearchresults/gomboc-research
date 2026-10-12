# figure-0140

AI research report · 2026-08-28 UTC

<!-- historical-status:start -->
> **Historical AI report.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../../C622/README.md) passes the supplied exact checks; the search for C<500 remains open. See [verification status and source gaps](../../catalog/coverage.md).
<!-- historical-status:end -->

---

# Keen Quartz 40 — exact multidimensional whole-pair continuation

## Verdict

**Exact finite multidimensional nonwinner.** No own-centroid strict `(1,1,0)` chamber was found in the certified atlas.

The requested two azimuthally separated whole-star controls do eliminate the four persistent target stable rows `2384,2385,2402,2403`, and all four are inactive at the terminal certified endpoint. They do **not** annihilate the stable block: twelve exact mechanical-zero certificates show that two neighboring stable rows are born before each target dies. The fully post-deactivation endpoint `C44` has actual lattice

`(H,V,E)=(2650,5296,7944)`

and strict own-centroid class

`(S,U,H)=(9,39,46)`.

This sharply delimits the tested architecture. It is not a CAD exclusion of every real `(alpha,beta)` component or of other multidimensional field designs.

## Exact two-control family

The predecessor is exact cell `C26` from the 28-cell scalar atlas. Its fixed dyadic parameters, in order `(c1,c2,t0,t1,t2,u,a2,aH,aL,b)`, are

```text
0x1.dd5d71082df60p-30
0x1.8858df5d891f7p-29
0x1.1db0d4b1b0ad2p-15
0x1.27502eacb39f1p-15
-0x1.f7d0c523ebd19p-12
0x1.c5ff15359460ap-3
0x1.5c28f5c28f5c3p-3
0x1.47ae147ae147bp-7
0x1.47ae147ae147bp-6
0x1.7bebd28e8ae95p-19
```

With `(u,t1,t2)` dependent and `(alpha,beta)` independent, every polar row is

```text
q_i = Qint_i/2^48 * (1 + 2^-24 Wint_i·p(u,t1,t2))
      + alpha*Aint_i/2^172 + beta*Bint_i/2^172.
```

Control A is supported on the complete actual one-ring

`[2348,2349,2350,2351,2383,2384,2385,2386,2419,2420]`

of target pair `{2384,2385}`. Control B is supported on the disjoint complete one-ring

`[2366,2367,2368,2369,2401,2402,2403,2404,2437,2438]`

of target pair `{2402,2403}`. Rows `0,4321,4322,4323` are protected.

For each target `r`, the exact field is

```text
2*(sum_j n_j/2^20 q_j(C26) - q_r(C26)),
```

with positive weights

```text
2384: 2349:583179, 2383:812, 2419:464585
2385: 2350:586764, 2386:812, 2420:461000
2402: 2367:583189, 2401:812, 2437:464575
2403: 2368:586776, 2404:812, 2438:460988.
```

Every other supported star row receives `-2^-16 q_r(C26)`. Canonical hashes are:

```text
generic generator  35c6259d86e8daf02d2bde0498ea775184aec8dddc812be7b86c812247a57bbd
predecessor         85011b6a70ee321b1e931900c9135f447f8ba4ab3e31a82ffc0d291bcdc81ef1
A field             76c4747ad026a1c4d26d5b4c1d49c9af7bc3d14d0fefad9db636e4de0331f127
B field             730b5c1c440af0efe33776901acf204536d75f1abeca4aa8d520609fb1bf2e80
```

## Hard moment solve and projected rank

Every actual cell is rebuilt before forming its moment equations. For an active row triple `T`, the corresponding primal vertex is recomputed as `v_T=Q_T^{-1}(1,1,1)^T`; with the actual outward surface triangulation,

```text
V = Σ det(v_a,v_b,v_c)/6,
M = Σ det(v_a,v_b,v_c)(v_a+v_b+v_c)/24.
```

`Mx=My=Mz=0` is then solved for `(u,t1,t2)` by a separate interval/Krawczyk proof in that rebuilt cell. No nominal inherited H/V/E data are used after a circuit flip or row deactivation.

On the exact C26 root box, the dependent moment-Jacobian determinant is directed into

`[-0.0014461625043935683,-0.000882621838260005]`.

After projection through that Jacobian, the target stability responses are

```text
2384: d/dalpha [-0.06843397628550751,-0.05855655195211527]
      d/dbeta  [ 0.012863036957895714,0.022740100468511625]
2385: d/dalpha [-0.06753019880870574,-0.058521418589084]
      d/dbeta  [ 0.012127659596840196,0.021136110377378538]
2402: d/dalpha [-0.020577030081314236,-0.007872325798635187]
      d/dbeta  [-0.037817748311591105,-0.025113500748666563]
2403: d/dalpha [-0.01874566634603407,-0.006539393057867745]
      d/dbeta  [-0.03985080919577008,-0.02764497380081433].
```

All four cross-pair `2x2` minors are strictly positive; their union of certified intervals is approximately `[0.00156515,0.00315343]`. Thus the hard-centred response has rigorously certified rank two and is not a scalar continuation in disguise.

## Exact cell and wall coverage

The atlas contains:

- `30` exact ingress cells on `alpha=beta=s`, `0<=s<=1/2`;
- `29` exact ingress joint moment/circuit walls;
- a genuine two-dimensional `5x5` rectangle with A levels `1/2,4103/8192,4107/8192,32870/65536,257/512` and B levels `1/2,4103/8192,4107/8192,32871/65536,257/512`;
- `25` exact rectangle cells and `40` exact rectangle circuit walls;
- `12` exact hard-centred mechanical-zero walls.

Hence there are `55` separately isolated ordinary-centroid cells, `69` separately isolated four-equation circuit walls, and `12` separately isolated four-equation mechanical walls. Every stored cell contains its actual exact H rows and active flags, exact Cramer vertices, actual true edges, maximal-face cycles, surface triangulation, point ledgers, complete root-box face/vertex/full-edge-cone ledgers, and directed nonincidence ledger.

The ingress class sequence is

```text
I00-I06  (5,39,42)
I07      (7,39,44)
I08-I19  (9,39,46)
I20      (11,39,48)
I21-I29  (9,39,46).
```

All 25 exact two-control rectangle roots have class `(9,39,46)`.

Across all 55 root boxes, the global worst directed bounds remain strict:

```text
minimum actual nonincident gap       2.9916591426371037e-10
minimum included stable margin       8.706772206623635e-05
closest excluded face upper         -2.1000091586342858e-05
minimum included unstable margin     0.019676759982694744
closest excluded vertex upper       -0.007180716141442999
minimum included saddle margin       0.004535248321858142
closest excluded edge-cone upper    -0.0014211253265894697.
```

The linked full report tabulates the exact root box for every cell and the exact center, dyadic radii, circuit quad, directed signs, and actual facet exchange for every wall.

## Exact mechanical lineage: cancellation becomes transfer

Along the certified diagonal ingress, the mechanical events occur in this strict order:

```text
s≈0.07205242923646544  birth row 2383 against target 2384
s≈0.07213941652823979  birth row 2401 against target 2402
s≈0.08279471347245417  birth row 2404 against target 2403
s≈0.08287338638662005  birth row 2386 against target 2385
s≈0.20929513055435905  birth row 2368 against target 2403
s≈0.20936983885085077  birth row 2350 against target 2385
s≈0.21395809032407136  birth row 2367 against target 2402
s≈0.21402416766795746  birth row 2349 against target 2384
s≈0.23464376563320018  death row 2403 against witness 2368
s≈0.23471647934027125  death row 2385 against witness 2350
s≈0.24028265235612785  death row 2402 against witness 2367
s≈0.24034688533289423  death row 2384 against witness 2349.
```

Each event has its own strict four-dimensional Krawczyk box, nonzero reduced hard-centred derivative, positive margins for every other true neighbor, and positive clearance to the enclosing incidence walls. Therefore two replacement stable rows are present before each target dies. The exact lineage is

```text
stable deaths: 2384,2385,2402,2403
stable births: 2349,2350,2367,2368,2383,2386,2401,2404.
```

This is a rigorous obstruction for the tested target-directed whole-star architecture: it cannot remove the target block without first creating a larger eight-row replacement block along the certified ingress.

## Remote relay generated by moment closure

The local controls also change remote actual incidences outside their supports. Remote unstable deaths are

```text
(1408,1444,2319) (1415,1451,2328) (1426,1462,2337)
(1433,1469,2310) (1519,1658,2326) (1537,1676,2308)
(1657,1692,2287) (1674,1675,2269),
```

while remote unstable births are

```text
(1408,1409,2319) (1415,1416,2328) (1426,1427,2337)
(1433,1434,2310) (1518,1519,2326) (1536,1537,2308)
(1657,1692,2322) (1674,1675,2340).
```

Local saddle births include `(2349,2350)`, `(2349,2383)`, `(2350,2386)`, `(2367,2368)`, `(2367,2401)`, `(2368,2404)`; target saddle edges `(2384,2385)` and `(2402,2403)` die. The field therefore changes the remote relay coherently after the hard moment solve; it does not merely translate the original four equilibria.

## Strongest fully post-deactivation endpoint `C44`

At fixed `alpha=beta=257/512`, the exact moment root is isolated in

```text
u  in [0x1.c8f48895cf17fp-3, 0x1.c8f48896cf181p-3]
t1 in [0x1.233a2b5b44aabp-15,0x1.233a2c5b44aadp-15]
t2 in [-0x1.f1b0891be2f54p-12,-0x1.f1b088fbe2f52p-12].
```

The Krawczyk image is

```text
u  in [0x1.c8f488964cc71p-3,0x1.c8f488965168fp-3]
t1 in [0x1.233a2bd7e5fa5p-15,0x1.233a2bdea35b3p-15]
t2 in [-0x1.f1b0890fdb9c9p-12,-0x1.f1b08907ea4ddp-12],
```

strictly inside the initial box. The minimum exact image-to-box clearance is

`12613003/18446744073709551616 = 6.837522627083092e-13`.

At the unique root the ordinary first moment is exactly `(0,0,0)`. The actual endpoint has:

```text
candidate H rows        4324
irredundant active H     2650
inactive H               1674
primal vertices          5296
true edges               7944
maximal faces            2650
surface triangles       10588
Euler number                 2
class                 (9,39,46)
stable rows [0,2349,2350,2367,2368,2383,2386,2401,2404].
```

All four targets are inactive. All `22,884,016` actual row/vertex nonincidences are strict, with minimum lower gap `1.4677438153753995e-9`. Directed equilibrium margins are

```text
stable included lower       0.000946281084334366
face excluded upper        -2.4703829044403488e-05
unstable included lower     0.01968344850652678
vertex excluded upper      -0.0071867147910182885
saddle included lower       0.027802616149925245
edge-cone excluded upper   -0.0015433986429340934.
```

The endpoint is separated from the incoming A and B target-deactivation walls by exact positive control gaps approximately `0.0003731870060273765` and `0.00037358396872103734`. This is a positive fixed-control moment parameter box and strict incidence/mechanical chamber, not a claimed free two-control implicit tube.

## First unresolved boundary

Beyond `C44`, increasing `alpha` with `beta=257/512` brackets the first unresolved actual circuit at

`alpha in [1049/2048,4197/8192]`

on quad `(4170,4171,4205,4206)`. The local exchange removes

`(4170,4171,4206),(4170,4205,4206)`

and adds

`(4170,4171,4205),(4171,4205,4206)`.

Both rebuilt bracket endpoints remain `(9,39,46)` with `(H,V,E)=(2650,5296,7944)`. Its approximate wall coordinate is `0.5122478897272673`. This boundary is deliberately marked numeric-only; no exact certificate is claimed for it.

## Independent verification and mesh

The clean-room verifier imports only the Python standard library and NumPy. It independently reparses the exact family, proves the two supports are the complete actual predecessor stars, reconstructs every exact H/V/E lattice, checks every exact Cramer incidence equation, rebuilds true edges and maximal cycles, exhausts every stored root-box face, vertex, full four-component edge-cone, and nonincidence ledger, verifies all 69 circuit-wall local exchanges and all 12 mechanical-wall orderings, and checks the endpoint meshes.

Its result is `PASS=true`, with `55` cells, `69` circuit walls and `12` mechanical walls verified.

The endpoint OBJ/STL has `5296` vertices and `10588` triangles, is connected and watertight, has Euler number `2`, and has positive oriented volume `3.2804648507390275`.

## Artifacts

- Complete exact package (`slot4_multidimensional_wholepair_exact_nonwinner.zip`), SHA-256 `b14ccea6c9693b98f5faefb2053e8e58723491e8f851380ef299070bdb89c833`; `unzip -t` reports no errors.
- Full 55-cell/81-wall handoff with all exact tables (`RESULT_FINAL.md`), SHA-256 `90504391ceae3aa51ff9a490556604333b199fdc3452c5e0a54ce40e4237089d`.
- Canonical machine-readable atlas (`complete_atlas.json`), SHA-256 `fcb1f7b452b193fda68beb976a68d8986b11e52f912607e60d28860ed9cfd8e0`.
- Projected rank-two certificate (`projected_response_interval_certificate.json`), SHA-256 `5e98d02d8494a6b91d4cd066038c923e52cd03e2b7dc57b8a621c11d16a04bdf`.
- Strongest endpoint perturbation certificate (`strongest_endpoint_perturbation.json`), SHA-256 `b9306538b0ba7acfd7e63fa67992a745acdd916923ebc8ae656cd7e155acb2cd`.
- Independent verifier (`verify_multidim_independent.py`), passing report (`verification_report.json`), and transcript (`verification_transcript.txt`).
- C44 OBJ (`strongest_postdeactivation_C44.obj`) and C44 STL (`strongest_postdeactivation_C44.stl`).
- SHA-256 manifest (`MANIFEST.sha256`), SHA-256 `c82e0d5e182c202507bb5135268ba89c7983ca108cc7347dcb858213683ac0c8`.

## Continuation

The next nonduplicative architecture must act on the replacement-star layer rather than repeat target-directed whole-star controls. A useful minimum is four independent controls spanning complete stars around `{2349,2383}`, `{2350,2386}`, `{2367,2401}`, and `{2368,2404}`, together with a nonlocal counterfield selected after projection through the `(u,t1,t2)` Jacobian. The target event must cross all eight replacement stable primitives in one connected actual cell without a remote birth.
