# material-cddbc6421726

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

Public derivative: internal-record-identifiers-replaced.

---

# TREE253_K2_ACTUAL_FAN_CHECKPOINT38 — Recovery capsule part 4/4

## Exact result and scope

This capsule preserves 38 new exact impossibility certificates for specified internal root positions of eight of the native TREE253/K2 incidence systems. It includes, rather than adds to, the earlier six-certificate checkpoint [internal-source-reference]. Thus it adds 32 certificates beyond that checkpoint and 38 beyond the native parent theorem. Each certificate excludes every convex realization of its literal incidence system at its own uniform-volume centroid satisfying the specified nine weak path-arrow inequalities in any common positive-definite metric. This is not a collection of unsuccessful numerical samples.

The native authority and application to mono-monostatic bodies are the complete worker results minimum-0078 (39043 bytes, SHA-256 2a0d3544bfb7f0c3b6366bdda3555bc650eede67a1444d51a2d7207a0079eecd) and its parent minimum-0069 (55605 bytes, SHA-256 d0f91982420a008eef0bc169a4c7b9f999710361057096a930facbf9715942ff). Both were read completely from cursor 0 through eof this turn. Their literal objects remain unchanged. In particular TREE253 means the FULL graph of nonnegative unequal pole-shadow relations with parent tuple (0,0,1,2,3,4,5,0,7), not a freely selected subtree of a larger graph. All eight of its edges are true dual edges. Theorem A of the latest parent forces the complementary actual primal Hamilton path to be a weak escape tree toward the sole unstable vertex. Theorem B excludes its two simple endpoints. No assumption that every off-tree arrow is negative is made here.

The certificate itself has a self-contained proof conditional only on the actual incidence and weak path-arrow hypotheses below. The parent theorem is needed to establish those hypotheses for the TREE253/K2 mono-monostatic application, not to execute the numerical-free matrix check.

Native indices are zero-based. Each ten-token row lists the incident genuine facet labels at native vertices 0 through 9; a token such as 0237 denotes one vertex incident to facets 0,2,3,7. The path is recovered from true edges by removing the eight primal edges dual to TREE253 and is oriented from its endpoint with smaller native vertex label. Root positions below are positions 0 through 9 along this oriented path, NOT new aliases for native vertices.

```
index 2: 012 016 0237 067 1256 235 345 3478 458 5678; roots 3,4,5,6
index 3: 012 016 0237 067 126 2356 345 3478 458 5678; roots 3,4,5,6
index 4: 013 018 0237 078 1245 1278 134 2356 346 456; roots 2,3,4,5,6,7
index 5: 0134 017 0237 1245 128 178 2356 278 346 456; roots 3,4,5,6
index 6: 0134 017 037 1245 1278 2356 238 346 378 456; roots 3,4,5,6
index 7: 0134 017 037 1245 128 178 2356 2378 346 456; roots 3,4,5,6
index 8: 0134 018 023 027 078 1245 1278 2356 346 456; roots 2,3,4,5,6,7
index 9: 0134 018 0237 078 124 1278 2356 245 346 456; roots 2,3,4,5,6,7
```

The reconstructed 38 certificates contain 449 integer 10-by-10 symmetric matrices B. Both exact Bareiss elimination and independent rational LDL decomposition prove all 449 matrices B-I positive definite, agreeing on all 4490 leading principal minors. Coefficient signs and the cross-fan cancellation are also checked exactly.

Together with the native parent endpoint theorem, precisely 148 of the 550 auxiliary K2 incidence/root pairs are now excluded and 402 remain. For W06 the new covered indices are 4,8,9, with six positions each: the subtotal is 58/200 excluded and 142 unresolved. No whole incidence domain is removed: positions 1 and 8 still remain even at indices 4,8,9. These are auxiliary counts, not the global 632/52585 joint register. That global register, TREE410's 17383/24847 closed and 7464 unresolved, and the accepted universal bound C>=34 remain unchanged. This result neither proves C>=36 nor supplies an attainer or an authenticated upper bound.

## Proof: actual tetrahedral fans, one body, one centroid, one metric

Let P be a hypothetical full-dimensional convex three-dimensional realization with its ten actual vertices x_0,...,x_9 in path order. Translate by P's own ordinary uniform-volume centroid so that this centroid is zero. Let X have these vertices as rows. Fix any common SPD matrix M, and put G=X M X^T. Then G is positive semidefinite and nonzero.

For a proposed root r, let p(i)=i+1 when i<r and p(i)=i-1 when i>r. The necessary weak-arrow inequalities are

D_i = x_i^T M (x_{p(i)}-x_i) >= 0, for all i different from r.

Define L_i=2 e_i e_i^T-e_i e_{p(i)}^T-e_{p(i)}e_i^T. Then tr(G L_i)=-2D_i<=0. These inequalities are used weakly: no strict separation at an arrow is required.

Choose any of the actual vertex apices specified in the coefficient record. For each apex a, take every genuine polygonal facet not containing that apex and triangulate that facet by its listed cycle fan. Join these triangles to the apex. Convexity and genuine maximal-facet incidence imply that these are nondegenerate tetrahedra with disjoint interiors covering P, up to shared lower-dimensional boundaries. In particular their actual fractions theta_(a,T)=Vol(T)/Vol(P) are positive and sum to one. If u_T is the ten-vector with ones at T's four vertices, the actual uniform-volume centroid identity gives

sum_T theta_(a,T) X^T u_T = 0.

The factor 1/4 in each tetrahedron's centroid cancels. Triangulation diagonals here are only integration devices: no extra mechanical edge or facet is introduced. Different apex fans are tetrahedralizations of the SAME P, not independent bodies. Consequently the SAME X, G, and zero centroid appear in every identity. No independent moment variables or engineered masses are substituted for these actual volume fractions.

The stored integer coefficient record supplies, for each selected fan a, a vector g_a and symmetric matrix C_a, and for each of its tetrahedra T, nonnegative integers mu_(a,T,i). The last C_a is encoded as the exact negative sum of all previous C_a, so sum_a C_a=0 literally. Define

B_(a,T) = g_a u_T^T + u_T g_a^T + C_a + sum_(i != r) mu_(a,T,i) L_i.

The verifier proves B_(a,T)-I positive definite for every listed tetrahedron. On the one hand each tr(G B_(a,T)) is strictly positive, because G is nonzero PSD and B_(a,T)>I. Its average with the positive actual tetrahedral volumes, followed by the sum over fans, is therefore positive. On the other hand,

sum_a sum_T theta_(a,T) tr(G B_(a,T)) <= 0.

Indeed the two g_a terms vanish by the centroid identity, the C_a terms cancel because every fan's weights sum to one and sum C_a=0, and the remaining terms are nonpositive by mu>=0 and tr(G L_i)<=0. This contradiction excludes the hypothetical realization.

This argument has no cutoff on the metric condition number, no coordinates restricted to a neighborhood, no floating tolerance, no assumption of simplicial facets, and no replacement of the volume centroid by a reference point. The full fan and actual-volume hypotheses are essential; arbitrary independently assigned occurrence Gram matrices would not justify the cancellation.

## Exact verifier boundary

verify_exact.py imports only the Python standard library. It reconstructs true edges from the literal incident-facet sets, checks 17 edges and the two endpoints of every dual-facet pair, reconstructs each genuine facet cycle, and rebuilds the complementary nine-edge Hamilton path. It independently reconstructs each specified actual apex fan and requires exact equality with the tetrahedra recorded in the coefficient file. It checks that every coefficient is an integer, all mu are nonnegative, sum C_a is zero in every matrix entry, and that each B-I is positive definite by two exact arithmetic algorithms. For every leading minor the Bareiss integer result equals the cumulative Fraction-LDL pivot product. No numerical locator is imported or trusted during verification.

A reused numeric coefficient proposal was accepted for a second incidence only after the reconstructed fan tetrahedron sets agreed literally and that incidence's exact verification passed. Such reuse never identifies two incidence systems as one exact object.

## Recovery capsule ordering and immutable source IDs

Parts 1,2,3 are consecutive literal UTF-8/LF source spans, including terminal LF, of ONE complete recovery program. Do not insert Markdown fences, headings, blank lines, or separators between them. Part 4 is this proof/manifest and is NOT concatenated into the Python source.

1. [internal-source-reference], Recovery capsule part 1/4, source lines 1-120: 14076 bytes; SHA-256 4dea6d5a3e065bd498240e678e5a05a2a1577950761614e306a15fb29195bb2a.
2. [internal-source-reference], Recovery capsule part 2/4, source lines 121-240: 13680 bytes; SHA-256 75786af84e6f16e508b2f0282853c424b6dfaaafa492e96c4990f77fb8ce2f92.
3. [internal-source-reference], Recovery capsule part 3/4, source lines 241-340: 10345 bytes; SHA-256 a908bb23a54b82249fecc504f493b59e78dfed6bf75d399e460242519ab1dd73.
4. This proof, scope, reconstruction instructions and complete input/output manifest.

Save the first three literal texts as part1.txt, part2.txt, part3.txt. Reconstruct and execute, with assertions ENABLED:

```
python -S -c "from pathlib import Path; Path('recover_checkpoint38.py').write_bytes(b''.join(Path('part%d.txt'%i).read_bytes() for i in (1,2,3)))"
python -S recover_checkpoint38.py
```

The concatenated recover_checkpoint38.py is 38101 bytes, SHA-256 ea3892417235991b9b97013fbb3ddfd8cdfd727cadd07e31b619a760f012992e. Its base85/zlib payload expands to 67157 bytes of exact UTF-8 JSON, SHA-256 369aac262389f0d4486598612091d4a5ed203959ef8b28325c8a8a5d68f3778f. All data needed for the exact new theorem are in this payload, not in an originating sandbox or a hash-only pointer. The program checks payload and extracted-file hashes, writes the following eight complete files in tree253_checkpoint38/, runs the standard-library checker, and compares the literal expected report and exact coverage list.

```
filename             bytes SHA-256
incidences.txt        2630 58126aee072933749b18eca00ac4d32842e56e6ac8d662d06713bacef28bf96e
verify_exact.py       5357 bdb639ca2f41592c876f54209f0144f7f87e22f2367705439852130713539dcb
quantize.py            770 87e41ed970cca20fba888f28fc278afd8fe1a2d657f2e9de9b3bf2afc2e5eb0b
locate_fans.py        4392 cd56f3b245834be5bbbc1c9968c7d424a9cadc9e8cbe7eb0a8bb42e9d7b0475c
locate_smooth.py      1698 3b0d12fedf96b1829e9ec2e05236ba114379a21f29a2984ceba8dff5d85cf955
run_batch.py          2057 1fd7a9a3492016c427ae9951c1281c48487fa748c889732e40e43e85d42f8399
certificates.json   48703 979292aba141144e9827ae86409a75cd2262f28835dd802bde598a35b403e13b
expected_report.json  569 6a2bb9de3fafcf453c325360785cf7dfb3e4b7bf9b77a299bebba17e3c7e0146
```

Independent verification after extraction:

```
cd tree253_checkpoint38
python -S verify_exact.py certificates.json
```

Expected terminal markers from the complete recovery run:

```
TREE253_K2_EXACT_FAN_CERTIFICATES_PASS 38 449
TREE253_K2_CHECKPOINT38_COLD_REPLAY_PASS
```

The complete stdout is 656 bytes, SHA-256 3d40e4e199e22de886af200d1ff5188eb69abfa1707ccc6be5e06d790699c5da. The integer B-matrix stream hash is bf7ac3921d867d653398272de951c17ee4c867321810d67a9cf95c9b852aaf94. The minimum exact LDL pivot of B-I over the complete collection is

3202349039104142878998516635787100969604561218470874069925786 / 59621234411728383794608487616971030049929771802572339055.

A fresh empty-directory cold recovery and independent exact verification completed successfully before storage. A second cold recovery after assembling all three local source spans reproduced the identical source and stdout hashes. The storage acknowledgements for all three spans match their stated byte counts and hashes exactly.

## Numerical source provenance and unsuccessful searches

The complete numerical locator, quantizer, and batch driver are preserved because they materially produced this finding, but none is needed to check the accepted integer certificates. Observed environment: CPython 3.13.5, NumPy 2.3.5, SciPy 1.17.0, one BLAS thread enforced through threadpoolctl. Initial index4/root4 used the eigen-cut HiGHS linear-program locator. The other accepted proposals used the convex smoothed minimum-eigenvalue locator with temperatures (0.1,0.03,0.01,0.003,0.001,0.0003,0.0001), at most 1500 L-BFGS-B iterations per temperature, maxcor30, ftol1e-15, gtol1e-10, maxls40; g and independent C entries in [-1,1], mu in [0,1]; zero initial point, no randomness. Proposals were rounded to integers at scale 2^24, then accepted only when the exact checker passed. A different floating environment need not reproduce identical proposed coefficients; the exact accepted coefficient checkpoint is included losslessly and reconstructs identically without those libraries.

The complete run_batch.py gives the selected fan plans: root2 apices(0,2,3), root3(3), root4(4), root5(5), root6(6), root7(6,7,9). It skips already accepted exact records, optionally reuses only a literally identical reconstructed fan, and otherwise calls the locator and exact acceptance. CLI form is python run_batch.py START STOP ROOT_POSITION..., with zero-based inclusive start and exclusive stop as in the full code. The materialized results in this capsule are only the 38 listed records; this is not an assertion of complete numeric scanning of all 55 incidences.

The chosen single fans for native indices0 and1 at roots3-6 did not yield accepted certificates. A root4 union-fan proposal over all55 and an index0/root4 multiple-fan proposal also did not yield a certificate. Their status is UNKNOWN: no feasibility witness, no exclusion theorem. Some locator calls were terminated by execution limits; only files completed and subsequently exactly verified enter this capsule. Root positions1 and8 were not closed, and most of the 55 systems were not tested with this new method. These failures cannot prove that no different fan, stronger moment relation, or exact certificate works.

## Research disposition

The two native worker parents are USED for the literal 55-system index, full-OJ implication and endpoint theorem; this new coordinator capsule is USED as an exact internal-root exclusion and reusable actual-fan method. The earlier checkpoint6 remains a valid independently recoverable subset. Universal C>=34 is inherited from the separately preserved V>=10 and F>=9 proofs; their full computational coverage was not replayed in this particular turn. No current minimum, C>=36, Figure C650 certificate, or historical/prize claim is asserted. All five worker copies were healthy and idle; no new assignment was dispatched, and the latest explicit operator drain was preserved.
