# material-32d9113122c3

AI research material · [Export notes](../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

# TREE253_K2_CHECKPOINT40 — Shared actual tetrahedral moments: theorem, proof and complete recovery manifest

## 1. Exact statement and literal domain

For the nine native TREE253/K2 incidence rows specified below, no full-dimensional convex realization at its own uniform-volume centroid can satisfy the nine weak arrows along the genuine complementary primal Hamilton path directed toward any of the indicated root positions, in any one common positive-definite metric. These are universal impossibility certificates, not tests of particular coordinates or unsuccessful searches.

Native indices are precisely parent55_index in the immutable result minimum-0078, 39043 bytes, SHA-256 2a0d3544bfb7f0c3b6366bdda3555bc650eede67a1444d51a2d7207a0079eecd, read completely from cursor 0 through EOF. Its literal parent is minimum-0069, 55605 bytes, SHA-256 d0f91982420a008eef0bc169a4c7b9f999710361057096a930facbf9715942ff, fully read in an earlier turn. Neither native index is a global polyhedral-type number. The original pole-labelled domains are not merged or renamed here.

The full unequal nonnegative pole-arrow tree in this application has parent tuple (0,0,1,2,3,4,5,0,7). It is the full graph, not an arbitrarily selected spanning subtree. Its eight true dual edges are 01,12,23,34,45,56,07,78. Their eight primal duals are removed from the genuine 17-edge graph. The remaining nine edges form the Hamilton path. The endpoint having the smaller native vertex number starts the path. Root positions below refer to positions 0,...,9 in that oriented path, not to native vertex labels. Each token in the following literal row is the incident maximal-facet set of one native vertex; tokens occur in native order 0,...,9.

```
0: 012 016 0237 067 1245 156 234 3478 458 5678; roots 1,2,3,4,5,6,7,8
1: 012 016 0237 067 1256 234 245 3478 458 5678; roots 1,2,3,4,5,6,7,8
2: 012 016 0237 067 1256 235 345 3478 458 5678; roots 1,2,7,8
3: 012 016 0237 067 126 2356 345 3478 458 5678; roots 1,2,7,8
5: 0134 017 0237 1245 128 178 2356 278 346 456; roots 1,2,7,8
6: 0134 017 037 1245 1278 2356 238 346 378 456; roots 1,2,7,8
7: 0134 017 037 1245 128 178 2356 2378 346 456; roots 1,2,7,8
8: 0134 018 023 027 078 1245 1278 2356 346 456; roots 1,8
9: 0134 018 0237 078 124 1278 2356 245 346 456; roots 1,8
```

Theorem A of the latest native parent supplies the weak-path hypothesis for a hypothetical mono-monostatic member of each literal TREE253/K2 domain. The certificate theorem below only needs this actual incidence and path hypothesis. It assumes neither negativity of every off-path arrow nor that the polar volume centroid is at the origin. The one metric and own-volume-centroid conditions are essential.

## 2. Actual tetrahedralizations of one convex body

Let x_0,...,x_9 be the genuine vertices in path order of a hypothetical body P. Translate by its ordinary uniform-volume centroid, so its centroid is zero. Write X for the matrix with these vertex rows. Fix one symmetric positive-definite 3-by-3 matrix M and let G=X M X^T. Then G is positive semidefinite and nonzero.

Every chosen fan has a genuine vertex as apex. Triangulate each genuine polygonal facet not containing that apex by its specified cycle fan, then join each triangle to the apex. A facet is a maximal supporting face, so the apex is strictly off its plane. The facet polygon has genuine extreme vertices, making all its fan triangles nondegenerate. Convexity implies that these tetrahedra have disjoint interiors and cover P up to lower-dimensional boundaries. Thus every tetrahedron in a selected fan has strictly positive actual volume. Integration diagonals here never become mechanical edges.

Let T be the union of unordered four-vertex sets occurring in the selected fans F_a. A particular four-vertex set t represents the SAME tetrahedron whenever it occurs in different fans. Put d_t=6 Vol(conv{x_i:i in t})>0 and D=6 Vol(P)>0. No independent occurrence volume is substituted for this actual d_t. Let chi_t be the ten-vector whose four entries at t equal one, and let J_t=chi_t chi_t^T+diag(chi_t).

For every chosen fan a, actual integration gives the following identities:

(2.1)  sum_(t in F_a) d_t = D.

(2.2)  X^T sum_(t in F_a) d_t chi_t = 0.

(2.3)  sum_(t in F_a) d_t X^T J_t X = 20 D Sigma_P,

where Sigma_P=(1/Vol(P)) integral_P x x^T dx is the actual central second moment of the same body P. Identity (2.2) follows from the tetrahedral centroid (1/4)sum x_i. For (2.3), write a point of a tetrahedron as sum lambda_i x_i. The normalized tetrahedral integrals are E(lambda_i^2)=1/10 and E(lambda_i lambda_j)=1/20 for i different from j. These follow by integrating the monomials over the standard 3-simplex: integral lambda^alpha = product(alpha_i!)/(3+sum alpha_i)!, with the affine Jacobian 6Vol(t). Therefore 20 E_t(x x^T)=X^T J_t X. Summing over an actual tetrahedralization proves (2.3).

In particular, all fans share X, G, D, and Sigma_P. The identities are not valid for independently assigned reference centres, metrics or bodies. A non-simplicial facet causes no exception: each selected polygon triangulation is a valid integration subdivision.

## 3. Weak arrows and the exact separating certificate

For the proposed root position r define p(i)=i+1 for i<r and p(i)=i-1 for i>r. The required nine weak arrows are

(3.1)  D_i=x_i^T M(x_(p(i))-x_i) >= 0, i different from r.

Let e_i be the standard coordinate vectors of R^10 and define

L_i=2 e_i e_i^T-e_i e_(p(i))^T-e_(p(i)) e_i^T.

Then tr(G L_i)=-2D_i<=0. Equality is allowed; no strict-arrow perturbation is used.

The frozen integer record gives, for each selected fan a, an integer vector g_a, a symmetric integer matrix C_a and an integer scalar k_a, and for each distinct tetrahedron t and i different from r a nonnegative integer mu_(t,i). The last C_a and last k_a are represented as the exact negative sums of all preceding ones, so sum_a C_a=0 entrywise and sum_a k_a=0. Define

(3.2)  B_t = sum_(a:t in F_a) [g_a chi_t^T+chi_t g_a^T+C_a+k_a J_t]
              + sum_(i different from r) mu_(t,i) L_i.

For every tetrahedron t, the exact checker proves B_t-I positive definite. Consequently tr(G B_t)>0, since G is nonzero positive semidefinite. Weighting by the positive actual d_t gives

(3.3)  sum_t d_t tr(G B_t)>0.

On the other hand this same sum is nonpositive. Indeed the g_a terms vanish separately for each fan by (2.2), because G=X M X^T. The C_a terms sum to D tr(G sum_a C_a)=0 by (2.1). The k_a terms sum to 20D tr(M Sigma_P) sum_a k_a=0 by (2.3). Every remaining arrow term is nonpositive by mu_(t,i)>=0 and tr(G L_i)<=0. This contradicts (3.3), proving the theorem.

The actual shared tetrahedral volumes and shared second moment strengthen a weaker method which treats separate fan occurrences with only per-fan centroid identities. No optimization duality theorem, finite-precision sign, rank truncation, coordinate neighbourhood, metric-condition-number cutoff, engineered mass distribution, or equilibrium count of a sample enters this contradiction. The argument applies to every convex realization of the specified incidence satisfying (3.1).

## 4. Precisely what the finite computation checks

The two frozen checkers reconstruct the genuine edges, facet cycles and complementary path from each literal incidence row; verify 17 edges, the closed polygon boundary cycles, the edge/facet incidences and Euler's relation; and reconstruct every selected fan from that geometry. They rebuild the sorted union of actual tetrahedral foursets and its fan-membership masks. Names, integer counts, optional recorded cells, nonnegative multipliers, symmetry, and the exact C and k cancellations are checked.

For every 10-by-10 block A=B_t-I, all ten leading principal minors are proved strictly positive by fraction-free Bareiss elimination. Independently, rational Fraction-LDL elimination proves ten strictly positive pivots, and their cumulative products are required to equal the Bareiss minors. Thus Sylvester's criterion proves the claimed positive definiteness with integer/rational arithmetic only. No numerical search library is imported by verification. The pinned reports retain native root labels, paths, true edges, maximal facets, fan identities, and hashes of the reconstructed blocks, memberships, determinants and rational pivots.

The standard checker uses the ten actual vertex-apex fans determined by the default facet-cycle start. The alternative checker generates such fans for all ten apices at cycle shifts 0 and 1, discards only literal duplicate fans, and checks the exact surviving fan labels. These alternative triangulations are different subdivisions of the same genuine facets, not new facets or bodies.

Standard certificates: 30 records, 2376 blocks, 23760 positive leading minors.
Alternative certificates: 10 records, 1276 blocks, 12760 positive leading minors.
Combined: exactly 40 distinct native-index/root pairs, 3652 blocks and 36520 positive leading minors. The standard rows contain respectively 82,79,79,80,78,77,79,79,79 tetrahedral cells for native indices 0,1,2,3,5,6,7,8,9. Alternative native0 uses132 cells, native1 uses126, native2 uses125 and native3 uses126.

The split of the forty records is exact:

```
standard: 0:(1,2,4,7,8); 1:(1,2,7,8); 2:(7,8); 3:(2,7,8);
          5:(1,2,7,8); 6:(1,2,7,8); 7:(1,2,7,8); 8:(1,8); 9:(1,8).
alternative: 0:(3,5,6); 1:(3,4,5,6); 2:(1,2); 3:(1).
```

## 5. Exact recovery, dependencies and integrity

The complete shared recovery program is [internal-source-reference], 15320 bytes, SHA-256 bb7e5afb92c0708251528299eb10f72cb05e4d7450a34d42d73a245adcfdf254. Save its literal text as recover_shared_code.py. It reconstructs thirteen complete files in shared_code/, including the numerical search programs, the two exact checkers, recover_case.py, the nine explicit incidence rows and discovery_plan_and_environment.json. The legacy native4 incidence used by grouped_search.py is hard-coded in that complete source. Every extracted file is checked against its stored size and SHA-256. The purported old source ID [internal-source-reference] does not exist and is NOT a dependency.

The correct complete native capsules follow. For native00 and01, save the two parts separately and concatenate their bytes in the listed order, without inserting a heading, fence, separator or extra newline. Each stored source span already includes its own terminal LF. For the other seven rows the single listed material is the complete case file. All new source-span acknowledgement hashes match the recovered bytes below.

### Native 0: case_00.txt

Complete file: 29354 bytes; SHA-256 960b9d9f570c954ea8c57334f7e42be187a53a9ed08076b67d5b439208b6ca65.

Source part 1/2: [internal-source-reference]; 15694 bytes; SHA-256 512807a27bd9e555ce95b6e1e5ff35bd878d1a17e03f8e46550542ad5362844c.

Source part 2/2: [internal-source-reference]; 13660 bytes; SHA-256 b8e7a63afb218e089b32d32dd06d71f66665367f6125e5598f511ef3117e3951.

Lossless decoded raw input: 26227 bytes; SHA-256 afce4d36a53c6b8d9468cb1fe9e27a6be25b5736ae1d9b7325359896ba7aafc3.

````
filename | bytes | SHA-256
native_00/alternative_certificates.json | 28096 | 489a7f61b017cf379ff868ad32a0c0f85019330586ce5acc2cdff41cca643c68
native_00/standard_certificates.json | 30433 | 6175066ad2a882f5994070aa228ebc3a02e652c82c55433cc4adef4209fe1ae2
native_00/alternative_exact.log | 292 | 22572f244316d925c2c143d7ed343e8303a68384be761c715ddb525e22acb162
native_00/alternative_report.json | 3395 | 5e57d7556e78bc791c0e25dd90395883965b4e6b4d4f2e220ad179830d47cf5c
native_00/standard_exact.log | 417 | 2c0c6a8001c7932d72e330a8b018fb30607cdbe6cf5d593e4a63e7b66ee55020
native_00/standard_report.json | 4737 | cbb799aaef0051c1cbde9b778a719fa37cb7b2ddc7a1f098d78c83afb1c9de3d
````

### Native 1: case_01.txt

Complete file: 29156 bytes; SHA-256 010ac21d4e32eb0c342ef2cb988398a70e312bfca0254dfe214ea006f7c3510f.

Source part 1/2: [internal-source-reference]; 15694 bytes; SHA-256 193de7083b1f21795195ff0c7fbf50d916b20f33b0ec89cec1d5de5e129c17fe.

Source part 2/2: [internal-source-reference]; 13462 bytes; SHA-256 f1c3d0a58e1c8fc0e9619a09c9a8c513887ab315af254f6144256ba275a11939.

Lossless decoded raw input: 26508 bytes; SHA-256 c6789cda175384b15d4811c00d2ab249ebb54aebb60dbe3c2117c9aa2c5d084e.

````
filename | bytes | SHA-256
native_01/alternative_certificates.json | 37453 | 8d5437169a61fdd68a33e7ec9e82f7f3c932f7c921a34e437e12e71f7459222b
native_01/standard_certificates.json | 22177 | 27932680a336d3f6d57b35f224259f83c815356c6e111cbbb6dfb570756b4b83
native_01/alternative_exact.log | 344 | 33e402f5904f8d80c42e5dcbb06ff1aa5d65258db2814aa9c60660e5202bfa93
native_01/alternative_report.json | 4434 | c73e57cd23def52d56e3a16f6744bf1422890ddcc4f7186947ffbe2c343ea2d0
native_01/standard_exact.log | 361 | 9b4598efe573d69e19617d3b0f0a7559873d35f14156379b50147616816870a4
native_01/standard_report.json | 3775 | 96e9fd690c6a0dadcda2b2ded878c2a87341f9cc25e183b0e06268b2fcee4a95
````

### Native 2: case_02.txt

Complete file: 15880 bytes; SHA-256 60758b9d5b0200bd7e2aaccedbf286a5692c98e119c87a5c3a9312deee8a04c9.

Source complete: [internal-source-reference]; 15880 bytes; SHA-256 60758b9d5b0200bd7e2aaccedbf286a5692c98e119c87a5c3a9312deee8a04c9.

Lossless decoded raw input: 13732 bytes; SHA-256 4ecf594d7d9cc7258af2504ba7830d83938fd79ea1956d6fb3fa8b8ba7d2ca56.

````
filename | bytes | SHA-256
native_02/alternative_certificates.json | 20311 | aa5a1c1f825c454f0ffb0ee1b84665b12cfe254f35a25ecbab87dea148c2944e
native_02/standard_certificates.json | 10753 | 97b801212f7d172f21787245c6bad29a44f033e706720c50f35241f82f3fef00
native_02/alternative_exact.log | 240 | fd4c5b2191436a094acd5016569ffb61e3c81f0ac8bceaf4d982cf86b35b8434
native_02/alternative_report.json | 2258 | 5ecefaa9df2d0bb6d5e3ba55dce120a444e8e23802eeace0e6bf58bb2de48d4d
native_02/standard_exact.log | 249 | 28161fff73b7612fdcecc5b06c70d3475411c9930ce5270daf62daa2bea1b35d
native_02/standard_report.json | 1970 | 6095a9e57c5a38ce97ee9c62ab5ce9c79cb6ebce431cb503b26a3449eee9c96c
````

### Native 3: case_03.txt

Complete file: 14309 bytes; SHA-256 1c0b77e02863c5c0862ce67864dd8e379c343360a5fc97d33fa7005d277e378b.

Source complete: [internal-source-reference]; 14309 bytes; SHA-256 1c0b77e02863c5c0862ce67864dd8e379c343360a5fc97d33fa7005d277e378b.

Lossless decoded raw input: 11851 bytes; SHA-256 0584a1140fd73c01ca906dbb5838a7573fc389cfb847f3c8c18de805560a8348.

````
filename | bytes | SHA-256
native_03/alternative_certificates.json | 10532 | 0a4944b6889fef496b6dab4b5da1410cb851c7ed22b6f118bbb5cbe698d1f7c7
native_03/standard_certificates.json | 16564 | 51feeff6555ad53e105437cd5bcbe2408cb9348dd9396a65055e5e7c8ee2b712
native_03/alternative_exact.log | 188 | aa5d53c938fa28752449b23aa1bee552e083858e64f0bf7b7a36504aecf08f3a
native_03/alternative_report.json | 1189 | 3ee78d6f0c5623595b4836e7ce997e3fcc87093b86612ef3dbeffa9ab810993a
native_03/standard_exact.log | 305 | deeabf857fc026ec811fac17b4a80ae76bdc3aa5ff2b5b5f1b4bef0033ab84bb
native_03/standard_report.json | 2902 | 090c262c3c859b1e5e872020de355107675a009a84d7c8061d531bd7488f58df
````

### Native 5: case_05.txt

Complete file: 11121 bytes; SHA-256 38d40db498f315da9fdbc74a80d5e8e3193e9e4f605ba89c93ebd62ce73ca73d.

Source complete: [internal-source-reference]; 11121 bytes; SHA-256 38d40db498f315da9fdbc74a80d5e8e3193e9e4f605ba89c93ebd62ce73ca73d.

Lossless decoded raw input: 9617 bytes; SHA-256 98522a1543b9998ccee6f6b46e44efc57f1d14fc0b030bef265b7dd1f0c7e268.

````
filename | bytes | SHA-256
native_05/standard_certificates.json | 22065 | 8882fa20a7bae74727124a8563dc2410a253329c2d8963e0d52588e198fe9923
native_05/standard_exact.log | 361 | d2e7d8d6a32c8583246194e84f0f65e44f3180cbe42b3ca26368d9ee95a48f94
native_05/standard_report.json | 3758 | 7af67e11701bcc94d64689806db22e13cf479b907cd3a8ce0493b2e6e7b73545
````

### Native 6: case_06.txt

Complete file: 11688 bytes; SHA-256 d459310e83380f7d9085af514fdf097c312e7c87249684b4313704ba867c749d.

Source complete: [internal-source-reference]; 11688 bytes; SHA-256 d459310e83380f7d9085af514fdf097c312e7c87249684b4313704ba867c749d.

Lossless decoded raw input: 10019 bytes; SHA-256 8a6069fb2604d3f57280ab0bac1f7e8584b75d8c6114651fc06ac1d947bb8a0a.

````
filename | bytes | SHA-256
native_06/standard_certificates.json | 22634 | 4fd2ffcb5a284d5b0fb348d36ed2867dda6bcd6da11a7457a322329393a8e503
native_06/standard_exact.log | 361 | e19bebb544ea81b0622f486759c01d5445587092fefb26f5d052d0b3eb6b09bc
native_06/standard_report.json | 3805 | 6d239740a88d2b100e8c4d1088562b3d59f464a185354abdd239fe4083457c84
````

### Native 7: case_07.txt

Complete file: 11335 bytes; SHA-256 e4117f52a47f28968c87b3125999e94046cff17afb025b2635f78cb0c271d808.

Source complete: [internal-source-reference]; 11335 bytes; SHA-256 e4117f52a47f28968c87b3125999e94046cff17afb025b2635f78cb0c271d808.

Lossless decoded raw input: 9777 bytes; SHA-256 9116204a6f3156b4c2db8bd9aa25e247714b5dee66fac3fbb0f79e2c737ccfab.

````
filename | bytes | SHA-256
native_07/standard_certificates.json | 22397 | 047ba188adcd6b8221db15f873e703b84792b8d7d6f1ef670eabbbfa4a02ae95
native_07/standard_exact.log | 361 | 27da97b9e9dbd41bbe46b9d53fc8f3f806a793ade994ec909989663ca7b4d1b4
native_07/standard_report.json | 3750 | 92c3a14f1703195e66de5f471649ed1848771320a6645fad255b518978f77dda
````

### Native 8: case_08.txt

Complete file: 6253 bytes; SHA-256 1a80d70438d18b72d06a860ffe1e2f814c8cf7d858f4af32b4754a457927d6b1.

Source complete: [internal-source-reference]; 6253 bytes; SHA-256 1a80d70438d18b72d06a860ffe1e2f814c8cf7d858f4af32b4754a457927d6b1.

Lossless decoded raw input: 4882 bytes; SHA-256 e0ddf531ecaca994b82726ff3a924aa0475d5c9fe58872be7055c4912cc12dff.

````
filename | bytes | SHA-256
native_08/standard_certificates.json | 11072 | f600c848d71f044e0a93b0d3a0e634001d41f4deba069af201a75663cb98c5f7
native_08/standard_exact.log | 249 | 66c96f27adf1872f3e5031e442ebcf0cd533cc9cf716259deb53fff2a7342067
native_08/standard_report.json | 1939 | d729410a8f7d5fe2d8ae164357dd4bcb42405d48e86037875e77a9e0ee9566ee
````

### Native 9: case_09.txt

Complete file: 6261 bytes; SHA-256 28c9f2eed87f08cb09b1ab9dbe6b5667a61163d73f3739d22e5fcdf8bfae1d84.

Source complete: [internal-source-reference]; 6261 bytes; SHA-256 28c9f2eed87f08cb09b1ab9dbe6b5667a61163d73f3739d22e5fcdf8bfae1d84.

Lossless decoded raw input: 4911 bytes; SHA-256 438258c2452214e9b1858a8e4a7b5b909f41087bf071aae5a09c848e4706a27f.

````
filename | bytes | SHA-256
native_09/standard_certificates.json | 11128 | abe9751d9095b15907db617ba80ba4ffd25dc9db9d96b129733ce7dfd6e1878f
native_09/standard_exact.log | 249 | 1fb423722df5a14ad10311ae5e6d6f5751c1afcd70f676b3eaae9ddabd38cb31
native_09/standard_report.json | 1941 | 55ce080fa48b304ca15bd9af80d5a3c432aabc2808d81186b97ebbfb0fd11ae2
````

### Commands and expected markers

Run with assertions ENABLED in a fresh directory containing the source and case files:

```
python -S recover_shared_code.py
python -S shared_code/recover_case.py case_00.txt
python -S shared_code/recover_case.py case_01.txt
python -S shared_code/recover_case.py case_02.txt
python -S shared_code/recover_case.py case_03.txt
python -S shared_code/recover_case.py case_05.txt
python -S shared_code/recover_case.py case_06.txt
python -S shared_code/recover_case.py case_07.txt
python -S shared_code/recover_case.py case_08.txt
python -S shared_code/recover_case.py case_09.txt
```

The shared-source marker is TREE253_K2_CHECKPOINT40_SHARED_SOURCE_RECOVERY_PASS 13. Each native command ends with TREE253_K2_CHECKPOINT40_NATIVE_COLD_REPLAY_PASS INDEX ROOT_COUNT, where (INDEX,ROOT_COUNT) is (0,8),(1,8),(2,4),(3,4),(5,4),(6,4),(7,4),(8,2),(9,2). It also emits NATIVE_SHARED_ACTUAL_MOMENTS_EXACT_CASE_PASS or NATIVE_ALTERNATIVE_FAN_EXACT_CASE_PASS for each root and the applicable aggregate checker marker. Every input JSON, exact report and captured checker stdout is compared to the pins above by recover_case.py, not just printed.

For independent repeated verification of an extracted input, use, from its native_XX/ directory:

```
python -S ../shared_code/verify_catalogue.py standard_certificates.json standard_report.json
python -S ../shared_code/verify_variants.py alternative_certificates.json alternative_report.json
```

Only native00,01,02,03 have alternative inputs. verify_catalogue.py is 8229 bytes, SHA-256 459eb1de9cf3d876f9937832ca13c12b9ee0b1faa0c0a13ab9966d3ad2c55cac; verify_variants.py is 9034 bytes, SHA-256 dbdfbb3cee97fffcd0a19e6d2dc3d372d58f6822247850f18d45c2f0bf8241a0. Their pins are also enforced in each case header.

The native capsule layout is: sorted compact JSON header with LF, one blank line, then the base64 encoding of an LZMA preset9 compressed raw input, wrapped at100 columns and terminated by LF. Raw input is a little-endian four-byte metadata length, complete compact JSON metadata with LF, then all coefficient arrays encoded as signed zigzag unsigned varints, in sorted filename order and literal record order. The decoder reconstructs the complete frozen coefficients and rejects missing or surplus bytes. A SHA-256 identifies this exact object; the literal stored source/data, not its hash alone, provides recoverability.

A fresh empty-directory cold replay of all nine complete native capsules and the shared source succeeded before this proof was stored. Native00 and01 whole-file hashes reproduce the original intended full objects, not different mathematical replacement certificates. An intermediate journal entry which said their bytes differ was based on stale asserted input pins and is corrected here. The old incomplete/wrong native00 part1 [internal-source-reference] and erroneous728-byte part2 [internal-source-reference] are EXCLUDED; neither is a prefix or suffix dependency of the repaired capsule. Native02,03,05,06,07 complete recovered files match their existing immutable receipt hashes; native08/09 were recovered directly from their complete immutable texts.

## 6. Discovery provenance and scope of negative observations

The complete original numerical locators, batch programs, quantizers, exact incidence inputs, library versions and parameters are in the shared-source material. Observed environment: CPython3.13.5, NumPy2.3.5, SciPy1.17.0, OpenBLAS0.3.30, x86_64 Linux; OPENBLAS_NUM_THREADS=1 and OMP_NUM_THREADS=1. No random input. The smoothed minimum-eigenvalue locator uses zero starts, temperatures (0.1,0.03,0.01,0.003,0.001,0.0003,0.0001,0.00003), L-BFGS-B maximum2500 iterations per temperature, maxcor30, ftol1e-15, gtol1e-10 and maxls40, coefficient bounds [-1,1] for g,C,k and [0,1] for mu, and stops early only after a numerical minimum eigenvalue greater than1e-5. The exact accepted records preserve their rounding powers. In this recovery, powers12,14,16,18,20,24 were tried in order with NumPy rint; a proposal was accepted only after the integer/rational checker passed. Reproducing identical floating proposals in another environment is not required: all accepted integer checkpoints are stored losslessly.

The standard-only attempts at native0 roots3,5,6, native1 roots3,4,5,6, native2 roots1,2 and native3 root1 did not produce accepted certificates; these are not proved feasible cases and do not prove infeasibility of a different separator. Alternative triangulations then supplied the ten accepted records covering these same positions. A container interruption of one numerical run was not interpreted as a mathematical result. Nothing here asserts numerical scanning or geometric exclusion of all other45 native rows.

## 7. Research integration boundary

The native endpoint theorem excludes positions0,9 of all55 rows. The old38-certificate checkpoint is preserved by [internal-source-reference], [internal-source-reference], [internal-source-reference] and proof [internal-source-reference]; all four were read completely in this turn. Native4 near-end positions1,8 are separately preserved by the corrected source parts [internal-source-reference] and [internal-source-reference] with proof [internal-source-reference]. Thus the present forty records add to, and do not duplicate, the earlier150 excluded native-index/root pairs, giving190/550 and fully excluding native rows0 through9 under the parent TREE253/K2 mono-monostatic hypotheses.

The separate exact maximal-facet/path transport theorem [internal-source-reference] can additionally carry all eight internal-root exclusions from native5 to12,6 to18 and7 to16 with explicit vertex/facet permutations and root reflection r->9-r. That yields24 further pairs, hence214/550 and13 whole native rows, when integrated with a coverage ledger. This is a path-hypothesis transport, not an identification of pole-labelled objects. The present proof itself is the source theorem for exactly forty new direct certificates.

The universal accepted lower bound remains C>=34. These are auxiliary K2 incidence/root counts, not the global632-type/52585-joint-root register. TREE410's17383/24847 closed7464 unresolved register is unchanged. This theorem does not prove C>=36, produce an attainer at C34, determine the exact minimum, authenticate Figure C650, or establish historical novelty or prize eligibility.
