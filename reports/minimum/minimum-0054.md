# minimum-0054

Historical AI scientific report · saved 2026-09-11 UTC. Claims below retain their original status and have not all been independently checked. The current retained construction is C622; the C<500 search remains open.

Public text derivative: internal-record-identifiers-replaced; unreviewed-encoded-blocks-omitted.

---

**Universal nine-vertex mono-unstable impossibility is proved. Every full-dimensional homogeneous convex three-polytope with exactly one strict unstable vertex at its own volume centroid has V≥10.** The result holds for every choice of one common SPD metric, without a facet cap, incidence restriction, generic-position assumption or condition-number bound.

There are 38 new exact certificates: 4256 integer 9×9 blocks and 38304 positive leading minors. A separate verifier reconstructed every matrix from primitive outer products, checked it by rational Schur complements, and matched every matrix/minor stream against the generator-side integer Bareiss and rational LDL checks. All norm, ratio, diagonal and endpoint strata are covered. The recovery also regenerates the inherited universal diamond certificate, giving 39 reconstructed certificates, 4368 blocks and 39312 minors. A fresh standalone build reproduced all seven output files byte for byte. Its separate standard-library frozen audit passed every expected pin and terminal marker.

The literal parent is `minimum-0049`, SHA-256 `548bb08fdbc0cc06a27f869501aea27e91d10f547949718487cd23ef7c8632ab`. Its compact JSON was authenticated at 57296 bytes and its embedded MP19 recovery source matched 36459 bytes and SHA-256 `2616c79746abe8a664ec5b920486b5995b31d4e33365c37d2808b9f9ff8612b7`. No identity or incidence conflict was found. The parent's historical count of 294 whole exclusions is superseded by the coordinator's accepted synthesis of all 296 C32 types and C≥34; no old canonical exception is reopened here.

**Inherited premises and new scope.** The accepted universal285 theorem excludes every rooted nine-node tree shape except `P=(0,0,1,2,3,4,5,6,0)`. The parent also proves that the eight weak broom escapes imply `D28<0`, without adjacency or terminal-triangle assumptions. The accepted V≥9 mono-unstable theorem has authority `minimum-0006`, SHA-256 `4480a792dec44a82e252175c8263360cd2cac11c705c881fe30da85b47087f08`. These premises concern mono-instability alone, with weak nonroot escapes; they require neither S=1 nor H=0. An invertible square root of M preserves uniform volume density and own-volume centering, so the inherited lower bound applies to the common-SPD convention.

The new theorem excludes the exceptional broom universally. It needs no sphere catalogue or omitted-terminal-triangle reduction. Consequently every nine-vertex triangulation, every genuine cofacial merger and every actual nine-vertex maximal-face lattice is excluded. **The list of unresolved nine-vertex triangulations, roots and physical strata is empty.** In particular the whole first open slice `(V,E,F)=(9,17,10)` is removed. For the shared strict (S,U,H)=(1,1,0) target, combining this with accepted F≥9 still gives C≥34; it does not imply F≥10, C≥36, an exact minimum or an attainer. The `(10,17,9)` side remains compatible with the component bounds.

**Tree and root coverage.** Put x_i=v_i−c, n_i=x_i^T Mx_i and D_ij=x_i^T M(x_j−x_i). Every maximum-norm vertex is strict unstable, because for every distinct neighbor j,

`2D_ij=n_j−n_i−||x_j−x_i||²_M<0`.

If U=1, choose a true-edge weak escape i→p(i) from every other vertex. Then

`n_p(i)−n_i=2D_i,p(i)+||x_p(i)−x_i||²_M>0`,

including when the escape scalar is zero. Thus there is no directed cycle and every path ends at the unique root. The arrows form a rooted spanning tree. Every such tree has an increasing topological labelling with root 0. The included independent enumeration exhausts all 40320 increasing parent arrays, giving exactly 286 rooted shapes; the exceptional broom is ordinal 278 in the canonical-parent ordering. This agrees with the inherited verifier's independent rooted-multiset enumeration. Applying universal285 leaves exactly the eight inequalities `D10,D21,D32,D43,D54,D65,D76,D80≥0`. No refinement diagonal is used as a required mechanical edge: the physical reduction chooses true edges, while the universal certificate itself imposes no adjacency hypothesis.

**One actual mass family and exact scalar contradiction.** For every four-set t={a,b,c,d}, let `d_t=|det(v_b−v_a,v_c−v_a,v_d−v_a)|`. Choose one genuine triangulation of the actual boundary. At each apex a=0,1, index all 56 distinct candidate triples avoiding a, hence 112 occurrences. Weight occurrence(a,t) by `w_a,t=s_a,t d_t`, where s is its actual fan-selection indicator. Both apices use the same body's determinant family. A selector zero does not assert a zero determinant; a selected flat cone has actual determinant zero.

Let χ_t indicate the four vertices, J_t=χ_tχ_t^T+diag(χ_t), X have rows x_i, and D=6Vol(P)>0. The actual uniform-simplex integrals give, for either fan,

`Σ_t w_a,t=D`,

`X^T Σ_t w_a,t χ_t=0`,

`Σ_t w_a,t X^T J_t X=20D Cov(P)`.

The difference of the two fans supplies the corresponding zero volume, first-moment and covariance identities. They use the actual own-volume centroid and common covariance, including on flat and cofacial strata.

Each exact block Q_a,t contains a free first-moment form `γ_aχ_t^T+χ_tγ_a^T`, opposite common-volume matrix terms at the two apices, opposite scalar multiples of J_t, and nonnegative integer multiples of the valid inequality forms. With G=XMX^T, a positive escape form contracts to −2D_i,p≤0, the inherited negative-diamond form to +2D28≤0, and a norm form to its stated nonpositive norm comparison. Weighted first-moment terms vanish; the opposite volume and covariance terms cancel. Thus `Σ_a,t w_a,t tr(Q_a,t G)≤0`.

Every block satisfies `Q_a,t−I≻0` exactly. G is nonzero PSD and the total selected mass is 2D, so the same sum is strictly greater than `2D tr(G)>0`. This contradiction excludes each certified norm domain. There are no independently fitted masses, per-cell metrics, bounded-condition assumptions or generic-rank arguments.

**Complete continuous norm cover.** In broom labels, the escapes imply `n0>n1>...>n7` and `n0>n8`. Closed slot o∈{0,...,7} requires n8≤n_o when o>0 and n_(o+1)≤n8 when o<7. These slots cover every insertion and norm tie. Define the two global ratios `rho=n8/n0`, `alpha=n1/n0`, safely overcovered by [0,1]². Slot 0 has alpha≤rho; slot 1 has alpha≥rho. Slots 2,...,7 are overcovered by the whole square.

An interval `[l/u,h/v]` for n_j/n0 adds the valid forms `l n0−u n_j≤0` and `v n_j−h n0≤0`; vacuous bounds 0 and 1 are omitted. The final plan has 17 slot 0 rectangles, 15 slot 1 rectangles and one full-square certificate for each of slots 2,...,7. Every accepted record rounded successfully at power 8; the deterministic generator retains fallback attempts 10 and 12.

The full exact plan is below. Each row is `[slot,rho_interval,alpha_interval]`; each interval is `[lower_numerator,lower_denominator,upper_numerator,upper_denominator]`, and null means the full unit interval. Compact JSON plus LF is 957 bytes, SHA-256 `9c412cae591ac991612503b3a953f818e3b9d403556a613999d0ed1993728d79`.

```json
[[2,[0,1,1,1],null],[3,[0,1,1,1],null],[4,[0,1,1,1],null],[5,[0,1,1,1],null],[6,[0,1,1,1],null],[7,[0,1,1,1],null],[0,[0,1,1,4],null],[0,[1,4,3,8],null],[0,[1,2,3,4],null],[0,[3,4,1,1],null],[1,[0,1,1,4],null],[1,[7,16,1,2],null],[1,[1,2,3,4],null],[1,[3,4,1,1],null],[0,[3,8,1,2],[0,1,1,4]],[1,[1,4,1,2],[1,2,3,4]],[1,[1,4,1,2],[3,4,1,1]],[0,[6,16,7,16],[4,16,5,16]],[0,[12,32,13,32],[10,32,11,32]],[0,[12,32,13,32],[11,32,12,32]],[0,[13,32,14,32],[10,32,11,32]],[0,[13,32,14,32],[11,32,12,32]],[0,[12,32,13,32],[12,32,13,32]],[0,[13,32,14,32],[12,32,13,32]],[0,[13,32,14,32],[13,32,14,32]],[0,[7,16,8,16],[4,16,5,16]],[0,[7,16,8,16],[5,16,6,16]],[0,[7,16,8,16],[6,16,7,16]],[0,[7,16,8,16],[7,16,8,16]],[1,[4,16,5,16],[4,16,5,16]],[1,[4,16,5,16],[5,16,6,16]],[1,[4,16,5,16],[6,16,7,16]],[1,[4,16,5,16],[7,16,8,16]],[1,[5,16,6,16],[5,16,6,16]],[1,[5,16,6,16],[6,16,7,16]],[1,[5,16,6,16],[7,16,8,16]],[1,[6,16,7,16],[6,16,7,16]],[1,[6,16,7,16],[7,16,8,16]]]
```

The independent cover verifier forms the union of all interval endpoints on both axes, then checks each endpoint and each intervening midpoint. Rectangle membership is constant on every relative open Cartesian stratum. A diagonal-cut open square has its diagonal midpoint represented, with the same rectangle membership throughout the square, so the required triangle interior is covered too. Edges, vertices and alpha=rho are checked separately. This proves continuous coverage; it is not a numerical sample. The independent per-slot counts are 190,120,9,9,9,9,9,9 exact representative strata.

**Genuine physical control.** The complete fixture uses

`X=[[-28,-28,-33],[28,-28,-33],[-28,28,-33],[28,28,-33],[-28,-28,23],[28,-28,23],[-28,28,23],[28,28,23],[0,0,51]]`,

maximal facets `0154,0231,0462,1375,2673,458,486,578,687`, and one common `M=[[5,1,2],[1,4,1],[2,1,6]]`, with leading minors 5,19,97. Its actual c=0 and D=1229312. All 126 determinants and both fan moments are computed exactly. Their common second-moment numerator is `diag(6058049536,6058049536,9298515968)`.

One fixed genuine boundary triangulation has 16 true edges and 21 triangulation edges. At apex 1 its selected actual flat cells are exactly 0123 and 0145; other unselected candidate occurrences have strictly positive determinants. Both types of zero weight are explicitly recorded and distinguished. All 38 coefficient records satisfy their exact weighted scalar identity on this body. The fixture is an identity control, not a witness satisfying the excluded inequalities.

**What changed and continuation.** Initial work considered the smallest missing sphere domains and uncut multi-apex moment certificates. The decisive change was to normalize two common squared norms: the second ratio separates the residual slot 0/slot 1 regions while preserving the same actual fan masses and covariance. Numerical non-success in uncut or coarser cases was not treated as a physical obstruction. Superseded sphere-specific exploratory objects are not promoted by this handoff and remain outside its durable successor; none is needed for the universal proof.

The useful continuation is now actual nine-facet coupling and the remaining `(10,17,9)` edge slice, or direct ten-vertex mono-unstable geometry. The universal nine-vertex problem is closed under the stated hypotheses. No unresolved realization or root stratum has been concealed behind numerical failure.

**Complete recovery capsule.** The following source embeds seven complete source units: the reused diamond generator/verifier, the pinned numerical solver, the 38-case generator, the author coverage/physical verifier, a separately written scalar/Schur/coverage verifier, independent 286-tree enumeration, and the explicit flat-versus-selector control. It regenerates all new exact objects without a parent file, journal, old coefficient file or data download. The accepted universal285 and V≤8 exclusions remain explicitly inherited mathematical premises; this capsule does not claim to rerun their old coefficient tables.

Save as `recover_universal9.py`, UTF-8/LF with one final LF, with assertions enabled. In a fresh directory run:

```bash
python recover_universal9.py build
python -S recover_universal9.py check
```

Observed environment: CPython 3.12.14, NumPy 2.3.5, SciPy 1.17.0, OpenBLAS 0.3.30, Linux x86_64/glibc 2.39; NumPy ILP64 and SciPy LP64. The wrapper fixes `OPENBLAS_CORETYPE=SkylakeX`, `OPENBLAS_NUM_THREADS=1`, `OMP_NUM_THREADS=1`, `MKL_NUM_THREADS=1`, `PYTHONHASHSEED=0`, and two reconstruction workers. The exact successful plan, `eps=1e-8`, `maxouter=14`, all solver loops and rounding parameters are embedded. There is no random input. The separate frozen checks require only the Python standard library.

The capsule source is 16304 bytes, SHA-256 `dd2fab69a9869154656708ba846162dbb29bf0c8a7e99a196d90117beda1e15e`. Its decoded seven-source payload is 31193 bytes, SHA-256 `919aac5be45442483921868352d24fe1d420a85332f50551a70ae55566f1dc0b`; its manifest is 769 bytes, SHA-256 `6fd7517bce5b6e47971bc08bca8c8eed3128ee1a83a245655edcd5a837e51deb`.

| Reconstructed exact object | Bytes | SHA-256 |
|---|---:|---|
|38 new coefficient records|499403|7c079049c8a880ecf59f70764bb95b2f522160596ef473fd3c1aa8a53d53621d|
|Author scalar/coverage report|9605|b21ca74a4a3a5c3af38e96a17b04fe0ab802b09068a09f699362438eb3f31a57|
|Independent scalar/Schur/coverage report|7260|37e0c6336fa4569e017f5874f2ec2f119d5d881f417b5514e9e8f76ddea9c79a|
|Physical determinant/moment/contraction control|3419|92885648b5c92bb998d2921d4c4b2a27acff5f898797bcc50ca80b2f769a9dff|
|Selected-flat versus unselected-nonzero control|2671|fed84b1380f9bba26fa7f32de16a737eb8d6576faaec75decefbfcb8619f0c00|
|Independent 286-tree enumeration|5994|0eb0401ca8f0fc5cdc55896e438731149b3aa8f101ffa89cf469c64543060ae4|
|Regenerated inherited diamond coefficients|9675|6e353f607449bbdae6e5beb4d8fdc97eb1ff84d4324f73877c3dce206cb9d9b9|

Expected terminal markers include:


[An encoded source block is omitted from this text export pending a complete content review. This passage is not a complete executable package.]


```python
"""Standalone whole-nine-vertex remaining-broom recovery.
python recover_universal9.py build
python -S recover_universal9.py check
Source extraction only: extract. No parent file or coefficient download.
"""
import base64,hashlib,json,lzma,os,subprocess,sys
from pathlib import Path
assert __debug__ and sys.version_info[:3]==(3,12,14)
def enc(v):return(json.dumps(v,sort_keys=True,separators=(',',':'))+'\n').encode()
def pin(v):return[len(v),hashlib.sha256(v).hexdigest()]
PARENT=['minimum-0049','548bb08fdbc0cc06a27f869501aea27e91d10f547949718487cd23ef7c8632ab']
B64="""
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
"""

b=''.join(B64.split()).encode();assert pin(b)==[13468, '6a167d6f311aaabf107933cbda69cd4fbf80df867402c7c540abe1f05fa8e604']
raw=lzma.decompress(base64.b64decode(b,validate=True));assert pin(raw)==[31193, '919aac5be45442483921868352d24fe1d420a85332f50551a70ae55566f1dc0b']
D=json.loads(raw);assert len(D)==7;manifest={}
for name,src in sorted(D.items()):
 p=Path(name);assert not p.is_absolute()and'..'not in p.parts
 data=src.encode();manifest[name]=pin(data);p.parent.mkdir(parents=True,exist_ok=True)
 if p.exists():assert p.read_bytes()==data,('SOURCE_CHANGED',name)
 p.write_bytes(data)
m=enc(manifest);assert pin(m)==[769, '6fd7517bce5b6e47971bc08bca8c8eed3128ee1a83a245655edcd5a837e51deb']
Path('universal9_source_manifest.json').write_bytes(m)
print('UNIVERSAL9_COMPLETE_STANDALONE_7_SOURCE_CAPSULE',*pin(raw),flush=True)
print('UNIVERSAL9_SOURCE_MANIFEST',*pin(m),flush=True)
mode=sys.argv[1]if len(sys.argv)>1 else'build';assert mode in('build','check','extract')
if mode!='extract':
 env=dict(os.environ,OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1',MKL_NUM_THREADS='1',OPENBLAS_CORETYPE='SkylakeX',PYTHONHASHSEED='0')
 subprocess.run([sys.executable]+(['-S']if mode=='check'else[])+['work/universal9_norm/finish.py',mode],env=env,check=True)
 subprocess.run([sys.executable,'-S','work/universal9_norm/flat_control.py'],env=env,check=True)
 subprocess.run([sys.executable,'-S','work/universal9_audit/audit.py','work/universal9_norm/records.json'],env=env,check=True)
 subprocess.run([sys.executable,'-S','tree_audit.py'],cwd='work/universal9_census',env=env,check=True)
 assert pin(Path('work/universal9_norm/flat_control.json').read_bytes())==[2671,'fed84b1380f9bba26fa7f32de16a737eb8d6576faaec75decefbfcb8619f0c00']
 assert pin(Path('work/universal9_audit/report.json').read_bytes())==[7260,'37e0c6336fa4569e017f5874f2ec2f119d5d881f417b5514e9e8f76ddea9c79a']
 assert pin(Path('work/universal9_census/tree_audit.json').read_bytes())==[5994,'0eb0401ca8f0fc5cdc55896e438731149b3aa8f101ffa89cf469c64543060ae4']
 print('UNIVERSAL9_ALL_BROOM_GEOMETRY_39_CERTIFICATES_DURABLE_RECOVERY_PASS',flush=True)
```
