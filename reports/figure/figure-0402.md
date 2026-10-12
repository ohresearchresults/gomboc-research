# figure-0402

AI research report · 2026-09-18 UTC · [Export notes](../../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI report.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../../C622/README.md) passes the supplied exact checks; the search for C<500 remains open. See [verification status and source gaps](../../catalog/coverage.md).
<!-- historical-status:end -->

---

# Calm Raven 70 — joint physical cap, filled-mass closure, and whole polar-basin cancellation

Assignment `figure-0402`; research run `[internal-source-reference]`.

## Result and disposition

**No own110 endpoint or record improvement is claimed.** The principal continuation parent is the new exact **CR70_C544_COARSEN8_G14**, with **154 vertices, 272 true edges, 120 maximal facets, own strict (1,3,2), weak-only (0,0,0)**. It has 38 edges of room below the requested E=310 ceiling. A second frontier, **CR70_C506_COARSEN15_G14**, has E=253 and own143: 57 edges of room, but one additional unwanted U/H pair.

The substantive constructive step is not just recentering the C598 cut. A changed physical cap, removal of a block of original supporting inequalities, and physical movement of the opposite mass-carrying facet first produce C572 own233. An added polar relay, followed by another actual filled-mass correction, then **cancels the entire unwanted stable basin without increasing E**: C572 own233 becomes a different C572 own132. Further physical coarsening retains monostability at E272, and supplies the lower-edge E253 alternative. All five rational bodies below are retained, including the intermediate and less successful mass repair.

| Exact body | V / E / F | C=2E | Own strict S/U/H | Weak-only | Third-integration tetrahedra |
|---|---:|---:|---:|---:|---:|
| CR70_C610_MASS3_G12 | 174 / 305 / 133 | 610 | 2/8/8 | 000 | 344 |
| CR70_C572_BULK7_G14 | 163 / 286 / 125 | 572 | 2/3/3 | 000 | 322 |
| CR70_C572_DUAL_G14 | 163 / 286 / 125 | 572 | 1/3/2 | 000 | 322 |
| CR70_C544_COARSEN8_G14 | 154 / 272 / 120 | 544 | 1/3/2 | 000 | 304 |
| CR70_C506_COARSEN15_G14 | 142 / 253 / 113 | 506 | 1/4/3 | 000 | 280 |

These are uniformly filled physical polyhedra, checked at their own ordinary-volume centroids. C544 and C506 are **not Gömböcs**. Their usefulness is the changed finite architecture, exact arithmetic, and increased repair budget—not an improvement of the accepted own110 record.

## 1. Source authority and an important parent-capsule correction

The literal parent is `figure-0400`, SHA-256 `6632ba5880d0bc5a70a63cc7733259d10de18955a9557f106f084d13f927040d`. I read its complete attached payload and recovered its complete 51-unit source capsule. Re-encoding the attached Markdown with its terminal newline as the version-2 JSON envelope gives exactly 98,789 bytes and that immutable SHA; the read-only research library independently confirmed the same source identity.

**The immutable envelope is intact, but its embedded decoder has a one-character payload inconsistency.** Its whitespace-normalized base64 is 78,017 characters, whereas its own assertion requires 78,016. Deleting the character `n` at zero-based normalized offset **26800** gives the declared base64 SHA `ced4bd9f0c7eb37b688f210b6d5b1ca590aaba2cac36a575f6747eae8f3c8342`. The decoded 58,512-byte XZ and 233,652-byte source dictionary also match their expected hashes. The repaired decoder is 79,983 bytes, SHA `0ee31362550f8348e361123436ffc6ea72c0f385f2c59f251a38e43bc66fdbb9`.

The complete repaired parent replay passed all 50 source-file identities, the independent controls, all seven parent/nonwinner A/B/mass checks, and its scalar-cap, cycle-budget and root-lock certificates. This was a hash-checked repair, not a substitute geometric parent. `PARENT_PAYLOAD_REPAIR.py` in the new capsule is the complete optional patch/auditor. **None of the new constructions requires the old decoder or any ancestor bytes:** the entire A_G1067 generator and all consumed exact verification sources are embedded below.

The exact A_G1067 generator is 9,048 bytes, SHA `a29714e1634768b4a834588c5d077228e5618f3e240d0db31e653e0b0d8f1d10`. Its canonical raw-H file is 9,190 bytes, SHA `c0f9de5522b0bc962411f8e8bfba74d1c60deb64add34082a89fc5b3b8dd28ab`; its independently matching A/B report is 176,750 bytes, SHA `e5359803ec5ceab18589e6e48138ac86c3aeb62700cb308ef2c24c863348d915`. Fresh replay verifies V/E/F=174/307/135, own121, weak000.

Additional research-library evidence was independently discovered and read through EOF: `material:[internal-source-reference]`, **COORD_SINGLE_CAP_MASS_EXISTENCE_V1.md**, SHA **`bca38da0cd0c495593041dff24233610ffcc30351b0878e7f6744fdeb1bd333f`**. That source establishes the convex physical-cap mass potential and global mass-closing existence/uniqueness of the corrected body under its stated hypotheses, not preservation of mechanical class, incidence, or edge budget.

## 2. Complete exact geometric recipes

Let `H` be the exact 135-row output of the included `RECONSTRUCT.recover(A_G1067_GENERATOR.json)`. A row `[a,b,c,d]` means `a*x+b*y+c*z <= d`. Every operation in the following recipes uses **original A_G1067 input indices**, before deletion. Replace row 3 first, delete the indicated original indices, then append the listed rows in order. All unmentioned rows are unchanged. This convention also applies to the coarsened bodies; there is no dependence on a previously generated child.

Define the two cap rows

```text
CYCLE = [79460,41240,-185368,100000]
RELAY = [-43051633148875,267903641602096,95336878362968,100000000000000]
```

Keep the displayed integer scaling for byte-identical reports.

**C610_MASS3:** replace row 3 by `[246393667937,2950258038978,977061305992,1000000000000]`; delete nothing; append `[87691904,43103003,-194968361,100000000]`.

**C572_BULK7:** replace row 3 by `[31983249815311,301811508686633,84694966259279,100000000000000]`; delete `[16,17,44,57,71,72,81]`; append `CYCLE`.

**C572_DUAL:** replace row 3 by `[34018990580919,300181065307113,83513010031847,100000000000000]`; delete `[16,17,44,57,71,72,81]`; append `CYCLE, RELAY`.

**C544_COARSEN8:** replace row 3 by `[32858126902000,301891938026247,82838362035487,100000000000000]`; delete `[16,17,18,44,55,56,57,71,72,73,81,117,118,120,134]`; append `CYCLE, RELAY`.

**C506_COARSEN15:** replace row 3 by `[29193410332068,303494959960524,83006385642226,100000000000000]`; delete `[16,17,18,44,55,56,57,71,72,73,81,89,92,110,115,117,118,123,124,125,134]`; append `CYCLE` only. Its deletion history removed the earlier relay inequality as well; it is not silently retained.

For each resulting raw polyhedron P, the reported centered body is exactly `P-g(P)`. The centroid is obtained from the true outward polygon cycles, not imposed as the numerical target. For their oriented face-fan triangles `(a,b,c)`,

```text
V = sum det(a,b,c)/6
M = sum det(a,b,c)*(a+b+c)/24
g(P) = M/V.
```

The included rational routines evaluate these formulas exactly and output every raw vertex, maximal polygon cycle, true edge, volume, first moment, centroid and strict/weak sign array. Inactive input inequalities remain in the recipes; they are not counted as facets. The roughly common displayed centroid is about `(-0.013520375287974, 0.005722766794143, -0.009409512599411)`, but that approximation is not used in any certificate.

All five raw bodies retain the exact apex `(0,0,1)` of degree 44. In C572_DUAL its raw-lex ID is95, its strict U list is `[88,95,151]`, and its strict saddle edges are `[[102,138],[151,154]]`. In C544_COARSEN8 these are apex87, U=`[82,87,139]`, H=`[[83,129],[141,145]]`. In C506_COARSEN15 they are apex74, U=`[30,69,74,133]`, H=`[[35,40],[70,115],[133,135]]`. In all three monostable bodies the sole stable input inequality is original row 3.

## 3. The constructive mechanism and its limitations

The numerical discovery frame was the exact A_G1067 own centroid, converted to binary64 only for scouting. A physical corrective plane is represented there by `q*x<=1`. For a fixed remaining body,

```text
Phi(q) = integral_H max(1-q*x,0) dx
D Phi(q) = -M(q)
D M(q)[v] = -K(q)v
K(q) = integral_Fq x*x^T dA / norm(q).
```

`hmodel.py` supplies the complete maximal-face reconstruction, ordinary filled integration, face second moments, and damped Newton/Armijo mass closure. Each evaluation recomputes the current physical complex; this is not a fixed reference-center census. The derivative for simultaneous movement of other planes is `Dq3 = -K3^(-1) sum_(f!=3) Kf Dqf`, when the active controller and differential chart are valid. Its usefulness is to move physical mass and supporting geometry together, not to declare a root condition solved.

For the original C598 cap, correcting physical facet 3 gives the exact C610 own288. Thus mass restoration repairs much of the disastrous own27/29/54 census, but raises E from299 to305 and leaves many unwanted equilibria. That is an explicit nonwinning mass-control result.

The replacement cap `CYCLE`, the seven-row deletion block, and a newly solved physical row 3 give C572_BULK7 own233. Its two stable carriers are original supports 3 and 130. Write `u` for carrier 130's polar point and `z` for carrier 3's polar point in the discovery frame. I inserted the relay

```text
q = z/2 + t*norm(z)*u/(2*norm(u)),   t=0.91.
```

Before the next mass correction, this has `q*(z-q)>0` whenever `0<t<1`, and `u*(q-u)>0` whenever

```text
t > (2*norm(u)^2-u*z)/(norm(u)*norm(z)).
```

The threshold in this scout was approximately 0.8646208201. I then **re-solved the physical filled mass**, rounded both changed raw rows to denominator 10^14, and performed the complete independent exact audit. The relay inequalities before mass closure are not offered as a proof about the rounded endpoint. The exact endpoint checks and the complete actual-centered polar trees below supply that proof. They show that the extra stable basin really disappears while V/E/F stays163/286/125.

The subsequent beam removes physical input rows and re-solves row 3 at every state. Its eight-row child gives the exact C544 own132. The fifteen-row alternative supplies C506 own143 and a cheaper mass arithmetic. For reproducing the historical deletion paths, the child-index deletion sets relative to C572_DUAL were, respectively, `[16,52,53,67,110,111,113,127]` and `[16,52,53,67,82,85,103,108,110,111,116,117,118,127,129]`. These child indices must not be confused with the direct original-parent recipes in Section 2.

The included finite exploratory programs also test outward radial relay hulls, joint cycle-cap/mass/polar-relay changes, and the complete eight-parameter actual-mass projective/affine chart with local and rooted objectives. `EXPERIMENTS.json` fixes every reported campaign's command, seed and nondefault settings. The bulk beam used depth 8/beam 5 and visited 3,888 states including its start; the later beam used depth 15/beam 4 and visited 6,718. The joint-cap campaign attempted 750 states, 748 completed; the two outward-relay grids had 54 and 96 attempts; the two orbit campaigns had 24 starts each. None produced an own110 endpoint. These are finite observations, **not exclusions of their continuous families or orbits**. The recovered sources retain those methods, rather than turning their unsuccessful runs into an impossibility assertion.

## 4. Exact global routing certificates and a fixed-geometry center obstruction

For physical points centered at their **actual** filled centroid, and for the polar of that centered physical body, use

```text
W(x,y) = x*(y-x)/(norm(x)*norm(y-x)).
```

The polar is not recentered using a separate polar mass. Complete literal parent arrays in `GATE_INPUTS.json` give rooted polar arborescences for **C572_DUAL, C544_COARSEN8 and C506_COARSEN15**, all rooted at stable face 3. Every nonroot arrow is certified exactly to satisfy **W > 1/469238**; every parent chain ends at that root. Together with the direct stable-face checks, this verifies whole polar-basin closure, not merely positive local escape at selected faces.

The remaining primal difficulty is substantial. The same input contains the complete literal closed pools and exact checks of **every** pool-to-complement pair:

| Body | Pool / complement sizes | Number of checked crossing arrows | Certified bound |
|---|---:|---:|---:|
| C572_BULK7 | 119 / 44 | 5236 | W < -1/5 |
| C572_DUAL | 120 / 43 | 5160 | W < -1/5 |
| C544_COARSEN8 | 111 / 43 | 4773 | W < -1/5 |
| C506_COARSEN15 | 98 / 44 | 4312 | W < -1/5 |

Before its cancellation, C572_BULK7 also has a polar pool 117/complement 8 with all 936 crossings below `-1/200`. These are exact certificates at the stated bodies. They do not exclude moved supporting geometries, different metrics, or projective transformations.

The arithmetic uses a separate homogeneous denominator for each point, avoiding the enormous common denominator of all polar points. For `x=N/s`, `y=M/t`, let `alpha=N*N`, `beta=M*M`, `gamma=N*M`, `D=s*gamma-t*alpha`, and `R=s*s*beta-2*s*t*gamma+t*t*alpha`. Then `W=D/sqrt(alpha*R)`. A negative bound `W<-p/q` is checked by the two integer inequalities `D<0` and `q*q*D*D>p*p*alpha*R`; the positive-tree test reverses the sign requirement. No floating square roots enter verification.

**A sharply scoped additional result:** for the fixed physical geometry of either C572_DUAL or C544_COARSEN8, every center c satisfying `norm(c-g(P)) <= 2/25` has at least two **strict** unstable vertices. This is a complete center-ball assertion, not a numerical search.

Proof: exact norm checks show that every pool point has radius strictly greater than 2/5, every pool-to-outside arrow has W<-1/5, and the old apex outside the pool has radius greater than 1. A center displacement of at most2/25 therefore leaves every crossing dot product strictly negative. The pool's maximum radius is below 5/8 for C572_DUAL and below 2/3 for C544. Even after that displacement, an outside point is farther from the new center than every pool point. A farthest pool vertex is strictly unstable against every other pool vertex by the strict Cauchy inequality, and against every outside vertex by the crossing certificate. A farthest vertex of the entire body lies outside the pool and is also strictly unstable. Exact supporting-plane distance checks give inradius>3/10, so the whole stated center ball lies inside the body. `CENTRE_BALL_INPUT.json` and `verify_gates.py` contain and check all rational inequalities used in this argument.

Consequently a tiny centroid adjustment cannot repair these fixed bodies. This does not prohibit a genuine joint physical redesign; it explains why the next step must change the primal escape architecture rather than only chase a near-zero local escape number.

## 5. Independent verification and arithmetic cost

Auditor A enumerates all support triples, certifies boundedness, reconstructs exact maximal polygon cycles and true edges, checks their oriented incidence and connectivity, integrates ordinary filled volume/moments, and tests every face, every vertex against all other vertices, and every true edge for strict and weak equilibrium conditions. Auditor B independently clips every support-pair line, constructs the face cycles by different predicates, uses a different interior-base triangulation for filled mass, and uses independent feature tests. Their complete canonical JSON reports agree byte for byte. The third checker triangulates from the exact centroid using shifted face fans and checks positive integer tetrahedra, the same volume, and exactly zero filled first moments.

Every retained body has zero additional weak faces/vertices/edges; all three reported primitive zero-count fields are also zero. The audit fixtures reproduce strict446/weak000 for the tetrahedron and strict446/weak123 for the prism, and reject the three invalid inputs. The five bodies, the literal parent, routing certificates, center-ball data and costs all passed a fresh replay from the embedded source capsule alone.

All five have maximum stored H-integer length 217 bits and maximum reduced raw-vertex numerator/denominator lengths 292/293 bits. The following entries are **maximum numerator / denominator bit lengths**, except the last column:

| Body | Raw centroid | Centered coordinates | Volume | Common centered denominator bits |
|---|---:|---:|---:|---:|
| C610_MASS3 | 29931 / 29938 | 29941 / 29942 | 15011 / 15012 | 29949 |
| C572_BULK7 | 28364 / 28371 | 28372 / 28373 | 14223 / 14224 | 28388 |
| C572_DUAL | 28964 / 28972 | 28977 / 28978 | 14527 / 14528 | 28992 |
| C544_COARSEN8 | 27313 / 27320 | 27321 / 27323 | 13701 / 13702 | 27330 |
| C506_COARSEN15 | 25316 / 25323 | 25324 / 25326 | 12696 / 12697 | 25331 |

`COSTS.json` additionally gives the first-moment costs, common integer-coordinate costs, complete face-size/degree histograms, roots and saddle edges. Canonical raw-H and matching A/B identities are:

```text
C610 raw 9202 12322a3ef9582f1d05d809cbdbe3a42658cc181193a87ebad2589415ea716a8d
     A=B 173506 e1494b82466e01562a6ecb0d89cac8fe9b74e10ab96e67b091dd0cde6501f382
C572 BULK raw 8715 82567ad9f4d6f700e4cfdb8435e71c517e739a7939f7236f5266122dd2b861c3
     A=B 164337 04c372c1341f1bcde2b6586d34134be2172b1ac5b9f414bf73e23e0271f09dc3
C572 DUAL raw 8780 5c08590d6a557795e49caaeb29b5286e20612a341a33618681681b3546de6511
     A=B 167179 9ed697b4ae42847636656581aaeed6564d34e91bfd627dc90f86a3c37320373b
C544 raw 8332 fed21b5061863798e66320e90cbc46646abce16acbf4199913a444ce43e92c5d
     A=B 158016 633aabc31aee433af35aba88b62cdb5be30bafef2a929ea5ae09243ee94189e1
C506 raw 7982 872d1f1e8ff2aa318b5a89f3f10ceff04c1047812df97b1c436fd2283ca49f08
     A=B 146532 6c0d22ef2b4860ac4c1114e5b180d883921c7d295699e7182e09d3ad6250fcdb
```

## 6. Consequential continuation

Use **C544_COARSEN8** for a 38-edge repair budget with only two unwanted U/H pairs; retain **C572_DUAL** as the less coarsened comparison and **C506_COARSEN15** as the 57-edge-budget alternative. In C544 the unwanted unstable vertices are 82 and 139; root 87 is the retained degree 44 apex. The 111-vertex closed primal pool, not the best-looking single escape edge, is the principal interface to replace.

The open constructive gate is a finite primal relay/interface that connects that pool to the apex-side component while the opposite physical material moves to close the ordinary mass and the complete polar arborescence remains valid. The supplied outward-relay experiments show why one should not blindly use facet 3 as the only compensator: the mass-closing plane can substantially cut or reorganize the intended relay/apex region and introduce new basins. The global existence theorem for one corrective cap does not prevent that. A promising next parameterization keeps the desired apex incidences explicitly, releases more than one opposite material carrier, and enforces global rooted constraints on both sides at the recomputed actual centroid. It must then undergo the same all-feature exact audit; there is no currently certified endpoint of that repair in this result.

## 7. Self-contained recovery capsule

Save the entire following Python block as `RECOVER_CR70.py`. The exact replay needs only the Python standard library; the tested runtime was CPython 3.13.5. Numerical discovery methods additionally used NumPy 2.3.5 and SciPy 1.17.0 with `OPENBLAS_NUM_THREADS=1` and `OMP_NUM_THREADS=1`. Their version pins and complete campaign settings are included. No numerical search, ancestor download, or access credential is required to reconstruct and verify the exact bodies.

```sh
python -B -S RECOVER_CR70.py CR70_source
python -B -S CR70_source/REPLAY.py --workers 4
```

The first command requires a fresh output directory. Expected recovery marker: `CR70_COMPLETE_STANDALONE_SOURCE_RECOVERED 28`. Replay checks 27 source identities, the control fixtures, the literal A_G1067 parent, all five new independent A/B/mass results, every supplied routing/center-ball certificate, and the complete fraction-cost report. Its terminal marker is:

```text
CR70_COLD_SOURCE_ONLY_ALL_EXACT_NONWINNERS_AB_MASS_GATES_PASS 3215 0aaf86cf4c3d06347c9ed801c257fb39b663b7cf0d6fa9f490326ff7810e584d
```

Capsule identities: source dictionary 87,516 bytes, SHA `74eb7012f9cb4585d4169af0a6780c4852712bfb6699c8d3e166475f06b1a243`; XZ 25,304 bytes, SHA `edc9c41fe0140b888c6a0ac1981aaf7e5db0db18bff4000bb8c10a1a4e4cc502`; normalized base64 length 33,740, SHA `2813c3610b3b478d98c773aefcba07e2b7e76afa45481b1b41df6f4beb650fd5`. The decoder itself is 35,452 bytes, SHA `19b4013fbc241cb3bca90f4e1d2c3bc62f79942bd438488dab93d2e5a4e800c4`.

```python
"""CR70 complete standalone exact source, certificates and discovery methods.
No ancestor files or numerical solver are required for the exact replay.
"""
import sys,json,hashlib,base64,lzma
from pathlib import Path
PAYLOAD = """
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
2amcu0oAAbHFAdyrBTpJgDKxxGf7AgAAAAAEWVo=
"""
def main():
 assert __debug__ and len(sys.argv)==2
 sha=lambda x:hashlib.sha256(x).hexdigest()
 text=''.join(PAYLOAD.split())
 assert len(text)==33740 and sha(text.encode())=='2813c3610b3b478d98c773aefcba07e2b7e76afa45481b1b41df6f4beb650fd5'
 xz=base64.b64decode(text,validate=True)
 assert len(xz)==25304 and sha(xz)=='edc9c41fe0140b888c6a0ac1981aaf7e5db0db18bff4000bb8c10a1a4e4cc502'
 raw=lzma.decompress(xz)
 assert len(raw)==87516 and sha(raw)=='74eb7012f9cb4585d4169af0a6780c4852712bfb6699c8d3e166475f06b1a243'
 files=json.loads(raw);assert len(files)==28
 out=Path(sys.argv[1]);out.mkdir(parents=True,exist_ok=False)
 for name,value in files.items():
  rel=Path(name);assert not rel.is_absolute() and '..' not in rel.parts
  dst=out/rel;dst.parent.mkdir(parents=True,exist_ok=True);dst.write_bytes(value.encode())
 manifest=json.loads((out/'MANIFEST.json').read_text());assert set(files)==set(manifest)|{'MANIFEST.json'}
 for name,e in manifest.items():
  bb=(out/name).read_bytes();assert len(bb)==e['bytes'] and sha(bb)==e['sha256'],name
 print('CR70_COMPLETE_STANDALONE_SOURCE_RECOVERED',len(files))
if __name__=='__main__':main()
```

Source, all exact reports and the completed cold-replay log (`CR70_JOINT_CAP_BULK.zip`) are supplementary conveniences. The complete recovery data and verification code are already contained in this immutable handoff.
