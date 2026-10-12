# minimum-0059

AI research report · 2026-09-11 UTC · [Export notes](../../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI report.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. [C622](../../C622/README.md) passes the supplied exact checks. See [verification status and source gaps](../../catalog/coverage.md).
<!-- historical-status:end -->

---

A new complete physical domain is excluded: **no uniformly dense convex three-polytope with ten genuine vertices and seventeen true edges admits the weak true-edge escape tree312**, with respect to its own volume centroid and any one common SPD metric. The exact parent tuple is

`312=(0,0,1,2,3,3,0,6,7,8)`.

The finite proof covers every root and all5152 labelled true-face domains, grouped into2576 orbits under the explicit sibling swap. It uses2087 exact certificates,50867 positive-definite10-by-10 blocks and508670 positive leading minors. All selected flat cells, genuine nonsimplicial faces, weak escape walls and arbitrarily ill-conditioned common SPD metrics are included.

This removes312 from the `(V,E,F)=(10,17,9)` escape-tree frontier. It does **not** prove `V>=11` or `C>=36`. The inherited unrestricted point-pair register remains670 exclusions and49 unresolved trees, because the new incidence argument requires true edges. The exact remaining48 true-edge tree shapes at E17 are:

```text
410,523,564,585,608,626,627,645,650,651,664,669,670,671,672,673,
674,675,676,677,678,681,685,690,695,696,697,698,699,700,701,702,
703,704,705,706,707,708,709,710,711,712,713,714,715,716,717,718
```

The checkpoint is `UNIVERSAL10_COMPLETE670_PHYSICAL_FRONTIER_RECOVERY_V1`, whose recovery source is35663 bytes, SHA-256 `f8f5b7c73ad0eab7afb94996ba6e6bd02e2f84ef9d961e8ff96f82bb0b8fd3e9`. Its authoritative universal-nine parent is assignment `minimum-0054`, SHA-256 `4e39e8c2a461dc76a76e49153b9f70ace7e0e287cb3fe5e6b3c3733a8c24d774`. No authority conflict was found. The new E17/tree312 proof is independent of the670 numerical register; that register is used for the global frontier and joint-arrow reduction below.

Tree indices mean: recursively generate sorted rooted-child parenthesis codes, parse in preorder with root parent0, then lexicographically sort the parent tuples. Counts for one through ten vertices are `1,1,2,4,9,20,48,115,286,719`. These are not MP or canonical polytope ordinals.

**Physical implication and analytic premises.** Let `x_i=v_i-c`, where c is the actual uniform-volume centroid, and let `G_ij=x_i^T M x_j`, `n_i=G_ii`, `D_ij=G_ij-n_i` for one common SPD matrix M. Weak escape means `D_i,p(i)>=0`. Distinct genuine vertices give

`n_p(i)-n_i = 2D_i,p(i)+||x_p(i)-x_i||²_M > 0`,

including weak zero walls. Every fan uses actual determinant masses of the same body. For a fourset t, its single mass is `d_t=|det(v_j-v_i,v_k-v_i,v_l-v_i)|`. With indicator `chi_t`, `J_t=chi_t chi_t^T+diag(chi_t)`, `D=6Vol(P)>0`, and actual covariance C, every genuine vertex fan satisfies

```text
sum_t w_at = D,
X^T sum_t w_at chi_t = 0,
sum_t w_at X^T J_t X = 20 D C.
```

Unselected candidates have weight zero even when their determinant is nonzero. Selected flat cells have actual determinant zero. Multiple appearances of one selected fourset always share its same d_t. All determinant cycle identities hold automatically in these same coordinates; for example the oriented determinant is `det(b,c,d)-det(a,c,d)+det(a,b,d)-det(a,b,c)`. The certificate excludes a necessary relaxation by substituting actual quantities; it never infers realizability from fitted masses.

Normalize n0=1. The depth-d weak-path projection bound is `-cos^(d+1)(pi/(d+1))`, obtained from the edge radius inequalities and concavity of log cos. At depths1,2,3,4 its constants are0,1/8,1/4,a, where

`c5=(1+sqrt5)/4`, `a=c5^5=(11+5sqrt5)/64`, `q=3/4-2a=(13-5sqrt5)/32>0`.

Only4,5,9 have depth4. Every root-cell projected vertex sum except `g459=1+G04+G05+G09` is at least q. Actual root-fan centering forces `g459<0` and positive mass on0459. A positive good cell must exist, since otherwise the entire body would equal tetrahedron0459. If459 lay properly inside a larger cofacial face, triangulating from a fourth face vertex would avoid459 and contradict centering. Therefore459 is a genuine triangular maximal facet.

Each leaf4,5,9 has root projection in `[-a,-(1-2a))`. This gives the strict norm bands

`1/10 < n_i/n0 < 2/7`, for i=4,5,9.

The exact endpoint proof uses `r=sqrt(n_i/n0)`, `z=sqrt(r)`, and `f(z)=8z^4-8z^3+z²`. The four-edge angle bound gives projection at least f(z); this polynomial decreases then increases at `(3+sqrt5)/8`. The rational probes `L=281171/500000`, `R=73111/100000` satisfy `L^4>1/10`, `R^4<2/7`, `f(L),f(R)>-15343/50000`, and `1-2a>15343/50000`. The embedded exact quadratic-field verifier checks every comparison.

The sibling estimate uses the exact rank-three PSD identity

```text
y0·y4+c5^5||y0||²+
sum_(j=1..4)c5^(5-2j)(||yj||²-yj·y_(j-1)) >= 0.
```

Its matrix has diagonal `(c5^5,c5^3,c5,c5^-1,c5^-3)`, adjacent entries `-c5^(5-2j)/2`, and corner04 entry1/2. The source checks all31 principal minors, rank3 and two independent exact kernel vectors. Applying it to the averaged sibling chain and the other arm gives

```text
||x4-x5||²_M < ((13-sqrt5)/256)n0 < (27/640)n0,
d0459/D > (4sqrt5-6)/5,
q D n0 <= d0459[(a-1/4)n0-(c5^-3/2)||x4-x5||²_M].
```

Every E17 certificate uses the six safe closed norm rows `n0-10ni<=0`, `7ni-2n0<=0`, and two scalar rows `g459<=0`, `640||x4-x5||²-27n0<=0`. No additional mass-cut block is needed.

**Complete incidence coverage and certificates.** True facet459 supplies45,49,59. True tree edges34,35 form cycle345. Removing3,4,5 leaves the connected true path `2-1-0-6-7-8-9`; thus345 cannot separate nonempty vertex sets and is a genuine triangular facet. The twelve-edge base has two remaining disks with literal cycles

```text
(3,4,9,8,7,6,0,1,2)
(3,5,9,8,7,6,0,1,2)
```

An E17 body adds exactly five true chords. The generator enumerates every split k,5-k, all noncrossing chord sets, excludes duplicate cross-disk edges, and requires minimum degree3 and connectivity after every vertex-pair deletion. Only necessity for physical realizations is used.

| Stage | Count |
|---|---:|
| Five-chord pairs |454014|
| Disjoint noncrossing chord sets |381522|
| Minimum-degree-three candidates |17648|
| Retained labelled true-face domains |5152|
| Free sibling-swap orbits |2576|
| Initial039 actual-mask models |2086|

Every regenerated catalogue row gives all nine literal maximal facet cycles, seventeen true edges and complete maps. The rooted automorphism is `[0,1,2,3,5,4,6,7,8,9]`, fixing root0. Arbitrary physical roots are covered by the rooted-tree isomorphism to these literal roles.

Triangulate each maximal facet from its smallest-labelled vertex. Each domain has sixteen triangles. The plan records12445 selected flat occurrences across2576 representatives. The field `actual_flat_foursets` means foursets forced flat by those maximal facets; accidental coplanarity of unselected foursets is unrestricted. A selected triangular cell is affinely independent, and its cone is flat exactly when its apex belongs to that same supporting facet. Refinement diagonals are not declared true edges.

The final plan retains2070 three-apex records at actual apices `(0,3,9)` and17 five-apex records at actual apices `(0,3,4,5,9)`. Five-apex internal instance labels0 through4 denote integrations at those five geometric vertices. They are not new vertices. The complete16 omitted baseline representatives and17 replacement representatives are literal inputs in `selected_plan.py`.

Changing fans can split an old model. The independent checker therefore rebuilds each target's own refinement and demands equality of the exact `(fourset,active-instance-mask)` pairs. Bitwise mask inclusion is insufficient. Three-apex certificates cover2555 representatives, five-apex certificates cover21, and explicit sibling partners give all5152 labelled domains.

Each grouped integer block contains free centroid terms, common-volume and covariance differences according to its exact mask, and nonnegative multiples of the negative weak arrows and the eight closed scalar/norm necessities. Every `Q_t-I10` is positive definite, verified by integer Bareiss determinants and exact rational LDL/Schur calculations. Weighting each distinct selected fourset once by its actual d_t cancels all free terms and makes the remaining contraction nonpositive. Positive definiteness makes the same sum strictly positive. Distinct grouped masses are not assumed to sum to the number of fans times D.

All2087 records,50867 blocks,508670 leading minors and every target transport passed. A fresh coefficient-free reconstruction reproduced the full aggregate byte for byte; the independent checker also passed on that cold aggregate.

**Exact regions beyond E17.** For each target refinement, restore the selected foursets previously omitted as cofacially flat. Their new matrices use the unchanged free moment, volume and covariance coefficients and zero new local inequality multipliers. Every old mask is preserved exactly; old and restored foursets are disjoint.

Let K be the maximum of1 and the absolute row sums of all restored matrices, so each is at least `-K I10`. Let R sum each distinct restored actual determinant once. The union of selected cells contains a complete fan, so its total distinct mass W satisfies `W>=D`; old mass is at least `D-R`. Exact moment cancellation gives a nonpositive contraction, while the matrix bounds give

`sum_t d_t tr(Q_t G) > (D-(K+1)R) tr(G) >= 0`

under the **closed** condition `R<=D/(K+1)`. Strictness survives equality because K>=1 forces old mass at least D/2>0. All moments belong to the new body at its own centroid.

All2576 target representatives and5152 mapped domains have exact restored lists and constants. Each restores1–9 distinct foursets; K ranges from8027 to193454210. Thus the uniform sufficient exclusion is

`R/D <= 1/193454211`.

Target-specific constants improve it. The source regenerates every restored mask, literal refinement, actual apex-instance map and constant. The specified triangles must genuinely refine the actual boundary. Positive-R realizability for every abstract target is not asserted, and regions above their threshold remain open.

**Additional complete domain and global frontier.** Tree312 is excluded at all84 possible true-edge embeddings, including all ten roots, on the following coherently oriented boundary sphere and every genuine cofacial merger admitting its refinement:

```text
(0,4,1),(0,1,5),(0,6,4),(0,5,6),(1,4,2),(1,2,5),
(2,4,3),(2,3,5),(3,4,5),(4,9,5),(4,6,7),(4,7,8),
(4,8,9),(5,7,6),(5,8,7),(5,9,8)
```

This is the boundary of the join of edge45 with path `3-2-1-0-6-7-8-9`. The complete embedding generator chooses the sibling-edge image, its two incident facets and every intervening Hamilton path. Explicit maps reduce84 embeddings to11 families. Families0,6 use apices `(0,3,4,9)`; the others use `(0,4)`. All use the six leaf norm rows and common covariance, with no redirected-arrow assumptions. Block counts are `[38,19,19,24,24,19,44,20,19,19,19]`, totaling264 blocks and2640 minors. The other48 tree families on this sphere remain unresolved.

Projecting along true edge45 also gives an affine-invariant actual-volume frontier. Every quotient hull cycle is `[45,3,ordered subset of {0,1,2,6,7,8},9]`, giving1957 complete cases. Quotient fan triangles lift to disjoint-interior inscribed tetrahedra45ij, hence `D>=sum d45ij`. The bad-cell mass bound requires

`sum d45ij/d0459 < (10sqrt5+15)/22 < 17/10`.

Thus `10 sum d45ij>=17 d0459` excludes a complete physical region for each realized quotient cycle. These are actual inscribed volumes, not fictitious boundary cells. The generator includes every cycle, including omitted interior/coincident nonmandatory projections.

Relative to the accepted670 whole point-pair exclusions, a hypothetical ten-vertex mono-unstable body has at most **nineteen ordered weak point-pair escapes**, including nonedges. Exhausting644071 parent-choice products over49 trees gives4475 minimal simultaneous-arrow obstructions:3266 pairs,1135 triples,74 quadruples. There are3332 explicit maps to accepted closed trees and1143 directed-cycle witnesses. Independent Cartesian checking and hyperedge splitting produce2487 maximal optional-arrow sets and76 rooted global digraph classes.

A vertex cannot weakly escape to all nine others, since that puts the body on one positive side of a plane through its own centroid. Four maximal graphs contain this outgoing nine-star, including both twenty-arrow graphs. Removing at least one star arrow yields a complete107-member centered overcover and proves the nineteen bound. Optional overcover arrows are permitted, not imposed; absent arrows are strictly negative, including correct treatment of zero walls.

Exactly eighteen final graph IDs have nineteen arrows:

`19,21,22,49,50,51,52,53,54,62,63,64,65,66,82,94,103,104`.

On this boundary, one vertex i escapes to eight destinations with sole omitted destination j. Actual apex-i centering gives `Gij+3ni<=0` and `nj>=9ni`. All literal graphs, omitted pairs and root/vertex maps regenerate. These eighteen cases remain open. The original312 tree has30 maximal branches,15 modulo sibling swap, with at most four optional arrows; an actual complete weak graph containing312 consequently has at most thirteen arrows.

**Thirteen further continuous norm/distance exclusions.** The literal parents are

```text
410=(0,0,1,2,3,4,0,6,7,8)
523=(0,0,1,2,3,4,4,0,7,8)
718=(0,0,1,2,3,4,5,6,7,8)
```

Every physical path718 survivor satisfies strictly:

```text
n1>5n0/16; n2>3n0/16; n3>n0/8;
n4,n5>7n0/64; n6>n0/16; n7>3n0/64;
n8,n9<5n0/32; 2n9<n1.
```

Six lower certificates and one global upper certificate suffice, with no residual norm subdivision. The upper record uses `n9<16n0/49`: the spherical nine-edge path must have angular length L>pi, otherwise its arclength midpoint puts every vertex in a closed hemisphere through the interior centroid. Concavity gives `n9/n0<cos^18(pi/9)<16/49`. For the exact comparison, `x=cos²(pi/9)>3/4` solves `64x³-96x²+36x-1=0`, increasing there and positive at151/171; the source checks `49*151^9<16*171^9`.

For410, `n9>n0/10` and `n5<n0/3`. For523, `n5,n6>n0/10`, `n5,n6,n9<n0/3`, and `||x5-x6||²_M<5n0/64`. Consequently `G56>39n0/640` and the metric-angle cosine exceeds39/64. The explicit rooted automorphism `[0,1,2,3,4,6,5,7,8,9]` transports5 bounds to6. The distance record uses the closed quadratic `5n0-64||x5-x6||²<=0`, with sparse symmetric input `[[0,0,5],[5,5,-64],[6,6,-64],[5,6,64]]`.

All thirteen records use two actual fans and one covariance, totaling2184 blocks and21840 exact positive leading minors. All exact closed rows and successful plans are embedded. Equality walls are excluded, giving strict survivor bounds.

The successful changes were additional actual fan apices, exact target-specific determinant masks, and the analytic312 leaf/sibling constraints. Independent mass-fitting was never used. Hard E17 cases required five fans; the final proof omits unsuccessful searches and needs neither the experimental double-refinement profile nor a mass-cut PSD block. Numerical searches on the remaining nineteen-arrow boundary and further path norm tightening gave no accepted certificate; no physical feasibility or optimality inference is made.

The remaining48 E17 shapes, the other312 incidence domains outside the stated sphere and volume regions, the107 graph overcovers and the path terminal-degeneration region remain open. Genuine cofacial arrangements within E17 are covered; merging away a true edge changes that slice and does not automatically inherit it. Close-sibling contraction still changes the actual centroid and need not preserve weak arrows after recentering.

A useful next consequence is already exact: in E17/tree410, if35 is a true edge then `D53<0`. Otherwise replacing5→4 by5→3 produces exactly literal312 with the identity vertex/root map. This incidence-conditioned redirect can strengthen the remaining410 domains; it must not be inserted into an unrestricted nonedge rewiring oracle.

**Complete durable recovery.** The following single capsule embeds27 complete source units, every retained finite plan and all exact nondefault inputs. It reconstructs all newly claimed objects without an attachment, ancestor source file or coefficient download. The joint-arrow theorem retains the explicitly identified670 register as mathematical authority. Build requires CPython3.12.14, NumPy2.3.5, SciPy1.17.0 and OpenBLAS0.3.30/SkylakeX. Hash seed is0, BLAS/OMP/MKL threads are1, E17 and sphere coefficient workers are3, epsilon is1e-8, maxouter14, with70 Newton and60 line-search steps. E17 rounding powers are8,10,12,14; norm and sphere powers are8,10,12. Exact checking uses only the standard library.

Save as `recover_ten_successor.py`, UTF-8/LF with final LF, and run:

```sh
python recover_ten_successor.py build
python -S recover_ten_successor.py check
```

Optional `python -S recover_ten_successor.py unpack` extracts every source and the36-output manifest into `ten_successor/`. Every numerical component was reconstructed from source in a fresh directory. The assembled capsule then passed its complete standard-library check and every output pin. Expected final marker:

`TEN_SUCCESSOR_ALL5152_E17_TRUE312_19_WEAK_ARROWS_84_SPHERE_EMBEDDINGS_13_NORM_CERTIFICATES_5152_COLLARS_PASS`.

Observed pins:

| Object | Bytes | SHA-256 |
|---|---:|---|
|Recovery capsule|37827|`c3b1f63a068f67a3b388ce67fe45a75bf9fd7cb65bde4f91c7ee7ea886892bfe`|
|Decoded source/input payload|107498|`db7973600ac1c08ae77c9c2b969b41c39b4d17d994b6017254411419480445c5`|
|E17 true-face catalogue|1349468|`100b8dc93f78fc78f94a5023863958fde2d5a6172c07e96f0b4b0c7d48650e76`|
|E17 actual-mask plan|3314002|`07ac9e97bb2af411fb83d3aafaad37d09a5aa2aaa7e28e1aa91c404c9def9e91`|
|2087 coefficient records|12345847|`8c863f059ef041a8c8e60461d697ade5efc04fa64259dd0df2f7fc2f09b74e8a`|
|Independent E17 check report|709|`11ff4e76776ca5ac5d49ee96b5a184b3cb4ec4ef175fb7b3d157055d32e069e6`|
|All restored-mass collars|6800333|`a48d6bad5c8d7d2bdecfe971338a0c2dd183e08940f1e088b6a719f8ce6c4cd0`|

All other coefficient records, graph maps, quotient cycles and reports have observed byte counts and SHA-256 values in the embedded output manifest. No continuation-critical array is abbreviated.

```python
"""Complete ten-vertex physical-frontier recovery, CPython3.12.14.
Build: NumPy2.3.5, SciPy1.17.0, OpenBLAS0.3.30/SkylakeX.
python recover_ten_successor.py build
python -S recover_ten_successor.py check
python -S recover_ten_successor.py unpack
"""
import base64,hashlib,json,lzma,os,subprocess,sys
from pathlib import Path
assert __debug__ and sys.version_info[:3]==(3,12,14)
def enc(x):return(json.dumps(x,sort_keys=True,separators=(',',':'))+'\n').encode()
def pin(b):return[len(b),hashlib.sha256(b).hexdigest()]
DATA="""
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
8Dy13tNf26q310icMeO+FRboxBH9Sb491/TT91J1b5s9r3g58+8a9hF9uz+q6fQyvbmlaV5kN9Rvygzq90v80mkdFH559z4x
jcHKcshhv0EPego9ICXy/0dUq0jkUmUIUmD/0dJ1RtX1WGFwezTlh1/GeuneUvJtcsUe/swZhy/4C8/vcUP3QLWtH5Y87Htk
uU90vzNJQSYDPogKCFBNxnvK12UsuOgWTQATAiTGhO3zDCvxEPsfkuPcwRLeF27dYgq9TLceziyAL63QQqyzx0a++4LVKlSC
ootWuz/Q2SnisSO4nsD5wO6WHud8KU6nm7n3OPMqir8jHuMtIIC9tWo113AlnJaGuqZlc8Jrmz7WOfddRrTqJVB/O5yalFe2
bDwqfYGXej/Kdk6Aqc/GMCgG4QzdeXXTGVKGuS4EY54UocIgcnDLnwGLkp2EPtTntLMmG75HPGkLSMGBKEoeyRUWPhSIwHdT
PriVQW/zLfD7UlRPffUWrBLyqPpWbdM/yuEC7ggMtQiMQ7vf5p+qDQ+GxLAu8B8PV/stdfqejlowg1D5uTEWPehympgOZ2Ov
/5DSlpopfmrWxpLSkE9PdHduHnVbTTp1uMpqGm9ZGuzERi1pfzSQq+Jx4OqrGeTvtuAliJGzqFSRzs0UOdHP1eQ0fpyR/3pc
zCbehraDrXLjcVlE56snv0AueRqkS/QZloeLDkeWxBtVUi1KBo+8pyIVjNMYg+KTx53n/dd1rV5mnknIBp5uOt+eGSx30Ef7
VgBLj8+ZIJaAECMqxcTjm+PmXz71o8E8rOtbyEgT6gakYYkc4BfrreXB60N/yfkRG/5tNSyvkZFugWcmKumprqWcuiYc0TIT
uUGokaqXMSG/7Xq6DjYBAGB4KDpRymT/DhkxjMalBmD+lRpJ6e6lyiBoDj92LCc6qrRf4ga0PU2pg78GEMxruoIjhHAguvpX
08CJ43P0sIGUmo5ea7Fz2BAkHdPZk9VToD7QhCIt634jr0Hfw8On7eGxY1QKinTZFRQjPZQbnOghVPYQiN3Natzlr7E12fWR
u0z5aMhTITvufNeaxuTXn0ZDBJx59O3mRaoeq4TL/auN9Ih/OAHuL36F3Qz+w/kGTt3YV29UffEPO9uZ4jw6Shx6i3rURl1O
gQS0PLn0gE/K8L91eMPuoPLypzBAhJUR60+hqgB/22b3A3Chbj9KXK+IXsILr+kslfjAqkQgTv3/gVcZsKDDCBSywrkXmcxy
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
AAH5ygHqxwbZunwjscRn+wIAAAAABFla
"""
raw=lzma.decompress(base64.b64decode(''.join(DATA.split()),validate=True))
assert pin(raw)==[107498, 'db7973600ac1c08ae77c9c2b969b41c39b4d17d994b6017254411419480445c5']
d=json.loads(raw)
assert d['identity']=='UNIVERSAL10_E17_TREE312_GLOBAL19_NORM_SPHERE_AND_COLLARS_V1'
root=Path(__file__).resolve().with_name('ten_successor');root.mkdir(exist_ok=True)
for name,source in sorted(d['files'].items()):
 q=Path(name);assert not q.is_absolute()and'..'not in q.parts
 p=root/q;p.parent.mkdir(parents=True,exist_ok=True);b=source.encode()
 if p.exists():assert p.read_bytes()==b,('SOURCE_MISMATCH',name)
 p.write_bytes(b)
(root/'source_manifest.json').write_bytes(enc({n:pin(s.encode())for n,s in sorted(d['files'].items())}))
(root/'output_manifest.json').write_bytes(enc(d['outputs']))
mode=sys.argv[1]if len(sys.argv)>1 else'build';assert mode in('build','check','unpack')
if mode=='unpack':print('TEN_SUCCESSOR_COMPLETE_SOURCES_AND_FIXED_INPUTS_UNPACKED',len(d['files']));sys.exit(0)
env=dict(os.environ,PYTHONHASHSEED='0',OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1',MKL_NUM_THREADS='1',OPENBLAS_CORETYPE='SkylakeX')
def run(folder,args,std=True):
 subprocess.run([sys.executable]+(['-S']if std else[])+args,cwd=root/folder,env=env,check=True)
run('work/continue10_cells',['build_selected.py',mode],mode=='check')
run('', ['work/continue10_audit/e17_check.py','work/continue10_cells/coefficients.json','work/continue10_cells/edge17_plan.json','work/continue10_cells/selected_records.json'])
run('', ['work/continue10_merge/collar.py'])
for name in('joint.py','maxgraphs.py','globalgraphs.py','audit_joint.py','orbits312.py','center_graphs.py'):
 run('work/continue10_joint',[name])
for name in('finish_v2.py','finish_nonpath.py','finish_spread.py'):
 run('work/continue10_norm',[name,mode],mode=='check')
for name in('verify.py','shadow.py'):
 run('work/continue312_analytic',[name])
if mode=='build':run('work/continue312_analytic',['families.py','build'],False)
run('work/continue312_analytic',['families.py','check'])
for name,want in sorted(d['outputs'].items()):assert pin((root/name).read_bytes())==want,('OUTPUT_PIN',name)
print('TEN_SUCCESSOR_ALL5152_E17_TRUE312_19_WEAK_ARROWS_84_SPHERE_EMBEDDINGS_13_NORM_CERTIFICATES_5152_COLLARS_PASS')
```

Expanded handoff and convenience source: universal10_continuation_handoff.md, recover_ten_successor.py.
