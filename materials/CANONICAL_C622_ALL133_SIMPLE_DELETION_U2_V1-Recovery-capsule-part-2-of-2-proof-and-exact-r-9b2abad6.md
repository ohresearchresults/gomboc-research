# material-9b2abad624e3

AI research material · [Export notes](../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

# CANONICAL_C622_ALL133_SIMPLE_DELETION_U2_AND_LOCAL_METRIC_BOX_V1
## Recovery capsule part 2 of 2: finite geometric theorem, exact execution, and complete dependency closure

This object is a finite negative construction/method, not a new attaining example or a global complexity lower bound. The parent is exactly VQ20_C622_ROUTE88_118_G12, the canonical uniformly filled own-centroid strict110/weak000 polytope with (V,E,F)=(176,311,137). It is not C622_HOMOTOPY_POSITIVE. All vertex indices below are the parent's raw lexicographic indices in A.json.

### Theorem
For every one of the 133 degree-three vertices v of the canonical parent, let P_v be the convex hull of all other parent vertices, uniformly filled at its NEW volume centroid g_v. At the Euclidean metric it has between 20 and 87 strict unstable equilibrium vertices. Moreover each P_v has at least two strict unstable vertices at every symmetric metric M satisfying max_{a<=b}|M_ab-I_ab|<=2^-22. These matrices are positive definite, since ||M-I||_op<=3*2^-22<1. Consequently no such child, or linear image with A^T A in this closed box, is proper strict110 without weak equilibria.

The exact true-facet counts classify the children as follows: 94 have (175,311,138), 16 have (175,310,137), and 23 have (175,309,136). Thus the attempted one-simple-vertex operation gives complexities 622,620,618, respectively, but every child fails U=1. The true counts of incident triangular facets are {0:94,1:16,2:23}. This replaces the old floating classification {0:94,1:38,2:1}. No random or floating computation is used in this theorem.

### Geometric certificate
Let a,b,c be the three actual neighbors of v, in the orientation for which N=(b-a)x(c-a) satisfies N.(v-a)>0. The complete exact program verifies N.(x-a)<0 at EVERY other parent vertex x except v,a,b,c. Thus the plane abc strictly separates a genuine tetrahedral ear: P_v=P intersect {N.x<=N.a}, and the removed region is exactly conv(v,a,b,c). The remaining true old maximal faces are obtained by removing v, dropping an incident triangle, and retaining all other nondegenerate faces; abc is a new genuine triangular maximal face. Strict separation also prevents accidental mergers with its supporting plane.

If t is the number of true triangular parent faces incident to v, then V'=175,E'=311-t,F'=138-t. The program forms every new face cycle and every actual edge from these cycles, checks this edge formula and Euler, and checks that v has no remaining incident edges.

Write parent volume V, raw first moment J, ear volume dV=|det(a-v,b-v,c-v)|/6 and ear centroid c_T=(v+a+b+c)/4. The new volume and moment are EXACTLY V_v=V-dV, J_v=J-dV*c_T, and g_v=J_v/V_v. In particular the reference is not the parent's centroid and not the mean of the vertex coordinates. All computations use fractions or denominator-cleared integers.

For each actual remaining vertex i and each actual neighbor j, set z=x_i-g_v and e=x_j-x_i. Strict negativity of z^T M e along all incident edges is equivalent to the radial normal being in the interior of the vertex normal cone, hence makes i a strict unstable equilibrium vertex. Convexity supplies the edge tangent-cone generators. At M=I the program identifies all such vertices and selects two with the most robust exact metric bounds. Vertex 94 is among the selected pair in every child.

For one selected pair i,j clear positive denominators jointly. Let d be the resulting integer multiple of z.e, and let the six symmetric-entry coefficients c_s be the same positive multiple of z_k e_k for diagonals and z_k e_l+z_l e_k for k<l. For a symmetric perturbation with max|M_ab-I_ab|<=2^-k, its primitive is bounded above by (2^k*d+sum_s|c_s|)/2^k times the inverse positive scale. The program verifies the strict INTEGER inequality 2^k*d+sum_s|c_s|<0, with k<=22 for the two chosen vertices of every child. This proves strictness even on the CLOSED common box of radius 2^-22. The program separately tests z.(x_j-x_i)<0 for every other remaining vertex j at M=I for each selected i, independently of the adjacency-sufficiency argument. There are 6365 strict adjacency metric-box primitive checks across the selected pairs.

The worst selected power is 22 only for deletion 131, with pair [94,57]. The minimum Euclidean strict-U count is 20 for deletion 171; the maximum is 87 for deletion 78. The maximum bit size of a new centroid's common denominator is 56600. The parent degree counts are {3:133,4:34,5:5,6:3,44:1}; its maximal-facet size counts are {3:51,4:33,5:24,6:14,7:7,8:3,9:2,10:1,12:1,20:1}.

### Exact recovery inputs — ALL needed sources are immutable
1. The CORRECT part1 of this capsule is material [internal-source-reference], named CANONICAL_C622_ALL133_SIMPLE_DELETION_U2_V1 Recovery capsule part 1 of 2 CORRECT literal exact_ears.py.txt. Save its complete literal text as exact_ears.py: 6699 UTF-8 bytes, SHA256 ef03f8f4792e36b8d8df8b2262ad9b88b8a732b833e1799bdacd714c4afe2170. It contains ALL vector, fraction, serialization, ear, mass, incidence, metric-box, chunk and merge helpers and has no nonstandard dependency. Do NOT substitute the older 6451-byte [internal-source-reference]; that is a different, superseded source unit, retained historically.
2. Canonical source recovery part1 is [internal-source-reference], 15305 UTF-8 bytes, SHA256 d5846089dd79e70e4aa35f67d5d66b8480c3dd72bca1de45359a281931f632aa.
3. Canonical source recovery part2 is [internal-source-reference], 20685 UTF-8 bytes, SHA256 c4a0ef05c36066f7b2851dc18ea1c3cda599f724130ec0ce7a89785613cde5b1. It includes the COMPLETE decoder RECOVER_C622_SCOPED16.py, 2053 bytes, SHA256 cf90d8a2240f4b7154a902bc6ff558dbd2f3157683adadda1485a882cfd17d28, plus reconstruction and verification commands. The two parts decode the exact canonical generator and all 16 complete standalone source files; no FULL76 source dependency or lost sandbox checkpoint remains. They contain literal input data, not just hashes.

Both canonical materials and the correct part1 were completely read, copied, and byte-checked in this coordinator execution. Full canonical normalized base64 has 27864 characters, SHA256 6a7d42eeabc1365c9dc122a9e62e6127e779db025765c6cbb37107cb31788638; XZ bytes 20896, SHA256 74dfffa9c2c4972bf1d4b99c269e3c3df99eaa01549548b858c542b431fa3597; complete 16-file source-map JSON 68603 bytes, SHA256 63b9a7de970fa8fb01f43ce10bec573441e5afeebe4ef2d3b7031ea6fb64c9ca. Every decoded file's byte count/hash matched MANIFEST.json, itself 1673 bytes, SHA256 0ba857a7d98fa85ad04ac1800886a9c450a5dc4c25e02177832adf9e0275d6af.

### Reconstruction and verification commands
Use fresh SOURCE and PROOF destinations. Save canonical materials as CANONICAL_PART1.md and CANONICAL_PART2.md; extract their exact decoder and the correct complete exact_ears.py part1.

```sh
python -B -S RECOVER_C622_SCOPED16.py SOURCE CANONICAL_PART1.md CANONICAL_PART2.md
python -B -S SOURCE/REPLAY_SCOPED.py PROOF
python -B -S exact_ears.py PROOF/A.json ears_000_030.json 0 30
python -B -S exact_ears.py PROOF/A.json ears_030_060.json 30 60
python -B -S exact_ears.py PROOF/A.json ears_060_090.json 60 90
python -B -S exact_ears.py PROOF/A.json ears_090_120.json 90 120
python -B -S exact_ears.py PROOF/A.json ears_120_133.json 120 133
python -B -S exact_ears.py merge ALL133.json ears_000_030.json ears_030_060.json ears_060_090.json ears_090_120.json ears_120_133.json
```

Exact execution environment here: CPython 3.11.8 standard library only, assertions enabled, -S; sys.set_int_max_str_digits(0) is in the source. Neither NumPy nor a floating hull routine is used. Smaller chunk boundaries are operationally convenient; the final sorted merged object is deterministic and independent of chunking. Exact geometric derivations and full literals, not this receipt alone, provide the certificate.

Canonical replay was executed anew, returning SCOPED_EXACT_A_PASS, SCOPED_EXACT_B_PASS and COORD_C622_SCOPED_CANONICAL_AB_MASS_CONTROLS_PASS. Both full exact auditors classify the parent as true176/311/137, strict110/weak000, with 137 active maximal supports, 1244 nonzero edge primitives, no degeneracy counters; true stable facet input3, unstable raw vertex94. Third mass calculation confirms 348 positive centered tetrahedra and zero exact first moments. Correct controls include regular tetrahedron strict446/weak000 and deliberately weak prism strict446/weak123; each independent auditor rejects three invalid fixtures. This execution did not rerun the separate optional numerical smoke test or the historical ten-case aggregate.

Canonical outputs: GENERATOR.json11841 bytes SHA2563cbd90d799189108f26b941800c8fa79a6f1c5abb17b2db614f0e54f57fffee7; raw.json15437 bytes SHA256ac01d1625274b64f336a715e1f5462f40686f647f0b7d1a4d90a5ee21765adb5; A.json and B.json311825 bytes each SHA256142ddb5d88fdc8b1721dbb62f52d9b71b78ac4c36e8600131235c6c4289698a0; RECEIPT.json681 bytes SHA2566ca0671aace64125886235d1060235f93290915c512bd7e9ac1e0789d7ec3f8a; this replay's MASS.json223 bytes SHA2562e8dbc53a73e9af00364dc91d13bccfb614fc88228bfcea3d9c791ae058352c1. Other older mass serialization pins must not be substituted for this file.

Each of the five exact ear chunks returned CANONICAL_C622_EXACT_SIMPLE_DELETION_RANGE_PASS. Their exact output pins are:
- ears_000_030.json21392 bytes SHA256515269a660f7474acb9c21a72b059058ae99dae8716932198994428c5f7e4712;
- ears_030_060.json20688 bytes SHA256f4efe3c389c6b610555ceed5c2563d65dd39a14c8d9f112e29e865625d3f1eac;
- ears_060_090.json19241 bytes SHA25667c3ce8ca1b31f9af74230c8c3a29e0285941654be309180f8da14d387f4c981;
- ears_090_120.json17827 bytes SHA2561fb0789764c05c7f485f948c312a5042fef41ab2650595dbb9d6044956f24ca5;
- ears_120_133.json7442 bytes SHA25636d280b07da36c4831eca0bd430b830295ccd9380135ef9c839f1fbe30ad0d09.

Merge verified contiguous complete coverage, 133 distinct deletion labels, the corrected 94/16/23 incidence distribution, strict-U min20/max87, universal selected94, and the maximum power22. Its observed final terminal line is:

```
CANONICAL_C622_ALL133_SIMPLE_DELETIONS_STRICT_U2_METRIC_BOX_PASS 84656 cf3dec4e67d481662e5fdd6cca8b5b7eb735f44686128e3e343c8c148f954cfb
```

ALL133.json therefore has84656 bytes and SHA256cf3dec4e67d481662e5fdd6cca8b5b7eb735f44686128e3e343c8c148f954cfb. All exact child centroids, witnesses and this report are reproducible from the complete immutable source closure without the originating sandbox; the report hashes do not replace that closure. Per-row strict_witness_sha256 hashes identify each exact witness stream; the chunk-level similarly named field reflects only its final row and is removed during merge, not promoted as a hash of all witnesses.

### Scope and next mathematical boundary
This theorem covers ONLY all single degree-three vertex deletions from the fixed canonical parent and the explicit closed near-Euclidean metric box for each resulting fixed shape. It covers neither the other43 nonsimple parent vertices, nor simultaneous deletions, face/vertex reshaping, general projective deformation or unrestricted SPD metrics. It is NOT a proof that C622 is locally minimal in realization space, and NOT a new universal lower bound for C_min. It explains why a promising elementary compression step fails and supplies exact own-mass and metric-robust controls for more coupled compression. The accepted global bracket remains34<=C_min<=622, first layer10/17/9 open.
