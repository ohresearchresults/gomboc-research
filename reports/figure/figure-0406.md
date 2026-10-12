# figure-0406

AI research report · 2026-09-18 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# Sharp Raven 82 — global reference centers and the exact closest-center obstruction

Assignment: `figure-0406`.

## 1. Result and source-identity correction

**Global free-reference feasibility is YES for both reconstructible, source-authoritative targets.** The same small rational point

`c_simple = (-1/4, 0, -1/2)`

is strictly interior and has exhaustive reference `(S,U,H)=(1,1,0)`, weak-only `(0,0,0)`, on both targets. I also obtained a stronger global result: the exact infimum of the L-infinity distance from a valid reference center to the actual uniformly filled centroid. It is approximately **0.27721934672215 for C616** and **0.27721934674001 for C620**. The infimum is not attained; an explicit rational sequence of valid centers approaches it. Complete all-root, all-witness exclusion trees certify the lower bounds at the exact critical radii, including their boundaries.

**These are reference-center results, not new own-centroid Gömböcs.** The fixed homogeneous bodies still have own132/weak000.

There is a material conflict in the assignment/navigation text. The actual immutable parent is `figure-0405`, SHA-256 **`f28886751ec1209009224f9c96a7bb23712d246f46417379d11378ca3c28ad08`**, confirmed by a complete worker-library read. Its literal payload and the supplied recovery material identify C620 as **`COORD_C620_ALLWITNESS174_G12_OWN132`, V175/E310/F137**, not the alleged `C620HA39G12`, V174/E310/F138. Its method is `REFERENCE_LRA.py`, not the alternative method described in the brief. The brief/context hash beginning `f288aafaa73e...` is not the attached immutable payload's hash. I followed the literal source rather than manufacture an identification of those different objects. **No result below is claimed for an independently defined V174/E310/F138 HA39 body.** The supplied material explicitly confirms the V175 C620 identity. :contentReference[oaicite:0]{index=0} :contentReference[oaicite:1]{index=1}

The exact inputs reconstructed and used were:

| Target | V/E/F | Exact A=B report bytes | SHA-256 |
|---|---|---:|---|
| `COORD_C616_COLLAPSE132_OWN132` | 174/308/136 | 312051 | `ba4bd93b8fade753cea37dc5a7b36f030fc2d55127fb7c043e01893f4ff94eb9` |
| `COORD_C620_ALLWITNESS174_G12_OWN132` | 175/310/137 | 314808 | `f30fc15a826c78fb05d994a506d97e953e6793472657749f2abc99fce006660a` |

These match the immutable parent report identities. C616 has redundant original support84, explaining the one-index shift in later local facet labels. Neither target is an own121 branch. :contentReference[oaicite:2]{index=2}

## 2. Three preserved rational centers, complete cells and independent feature audits

All coordinates here are in the raw coordinate system of the exact input reports. These three points work on **both** targets:

```text
simple     = (-1/4, 0, -1/2)
near       = (-290787037/1000000000, -270371541/1000000000, -68565859/250000000)
discovered = (-263346267/1000000000, 114192883/1000000000, -469288043/1000000000)
```

For every one of these six body/center pairs, the exact result is strict110/weak000, with **zero primitive equilibrium-form zeros**. The unique U is raw-lex vertex94, exactly `(0,0,1)`. There are no strict or weak saddle edges.

| Center | Stable original input support | C616 local S | C620 local S | Selected strict inequalities, C616/C620 | Certified closed L-infinity box radius |
|---|---:|---:|---:|---:|---:|
| simple | 126 | 125 | 126 | 801/806 | `1/10000` |
| near | 90 | 89 | 90 | 800/805 | `1/10000000` |
| discovered | 116 | 115 | 116 | 802/807 | `1/10000` |

The box around each center is contained in its selected strict witness polyhedron; every point of that box remains interior and reference110/weak000. These are not inferred from sampled corners. For every selected inequality `b+a·c>0`, the verifier checks exactly

`b+a·c_center - radius*(|a_x|+|a_y|+|a_z|) > 0`.

The complete witness polyhedron is reconstructed deterministically: retain all interior inequalities and all positive predicates of the unique S and U; for every other face and vertex, negate its first strictly negative predicate; for every edge, negate its first strictly negative saddle predicate. The output includes **every selected integer row and its feature/side label**. It additionally emits the full signed arrangement chamber using all distinct equilibrium forms: 1368 inequalities including interior for C616, and 1377 for C620. The advertised box radii concern the selected witness polyhedra, which can be larger than a single primitive-sign chamber.

`VERIFY_R82.py` exhaustively compares the inherited affine census with an independent geometric implementation: all-other-vertex normal-cone tests; orthogonal projection onto every maximal facet; and line projection plus exact two-normal Gram-system coefficients on every true edge. All individual face and edge signs agree. Every strict/weak feature list is checked. It also replays the parent's four weak-boundary tetrahedron controls through the new direct implementation. Neither primitive zeros nor weak features are hidden by an Euler-count shortcut.

The six generated audit files preserve all signs, every all-other-vertex sign, both cell descriptions, and exact input identities. They are reproducible outputs, not necessary external inputs. Their complete output hashes are in `EXPECTED.json` inside the capsule below.

## 3. Exact global closest-center result using the actual filled centroid

Let `g(P)` be the exact filled-volume centroid in the matching report, and let

`C(P) = {c in interior(P): strict110 and weak000 at reference c}`.

For **each** target, I proved

`inf { ||c-g(P)||_infinity : c in C(P) } = g(P)[0] - p[0] =: rho(P)`.

The same rational point `p` works for both bodies. Its complete literal coordinates are:

```text
p = (
-3727207307511979534863866163436248024302455822486246926786593375128047835079309301082010067478104086845470369721091127165100865876857298586781162787368983184872644021/12817708495817142077034659053711250290975664177787413480361295535234018470187113917000813293121307422433433969554474122656683307977764908086943173669848124988000000000,
-21659619738421617177110962811480933086099679628267473923239581276417202965518598409099374347719721313423946601358297013629587400313741630983289911173280839588104457203/80110678098857137981466619085695314318597901111171334252258097095212615438669461981255083082008171390208962309715463266604270674861030675543394835436550781175000000000,
-1757710118826367974978871275650043650907584356780867075981583784380989456352628944166286455906882571575798642904357456448154718932411328482876489464971315452244083917041/6408854247908571038517329526855625145487832088893706740180647767617009235093556958500406646560653711216716984777237061328341653988882454043471586834924062494000000000000
)
```

Numerically, `p ≈ (-0.2907857756890239, -0.2703711946077088, -0.27426277004192584)`. The exact radii, defined above rather than rounded, have these rational decimal enclosures:

```text
0.27721934672215 <= rho(C616) < 0.27721934672216
0.27721934674001 <= rho(C620) < 0.27721934674002
```

The exact `str(Fraction)` radius representations are respectively 34440 and 34730 bytes, with SHA-256 `1f35ef70305b1feac8b4e502af5aa82aee4a133aa013c8c6f3a8e7d22901764d` and `bca3511ce6c5453e0adc80743f10bec08a1797259b0164c0802be9bff6aa8e57`. They are regenerated from the complete inherited centroid and the literal/reconstructed `p`; no giant centroid numerator is omitted from a required new input.

**Lower bound and nonattainment.** The complete proof trees exclude every reference110/weak000 center in the **closed** cube `||c-g(P)||_infinity <= rho(P)`. This includes every U root, every stable root and every escape-witness choice. It uses the actual exact centroid, not the rounded anchor from the preliminary search.

**Matching upper bound.** For every rational `0 < eps <= 1`, define

`c_eps = (1-eps)*p + eps*near`.

Every selected inequality of the near witness polyhedron is nonnegative at `p` and strictly positive at `near`; hence every `c_eps` is strictly interior and reference110/weak000. The x-displacement dominates the other two at both endpoints and therefore throughout the segment. Consequently,

`||c_eps-g(P)||_infinity = rho(P) + eps*(p[0]-near[0])`,

which decreases to `rho(P)` as `eps` decreases to zero. The coefficient `p[0]-near[0]` is positive. This proves the exact global infimum, not merely a numerical bracket or a minimum in one frozen cell.

The limit itself is **not** an admissible reference110/weak000 witness. It has strict110 but weak-only **303**: strict stable input90, weak stable inputs `[3,30,91]`, U94, no strict H, and weak H edges `[[30,36],[30,57],[62,100]]` on both bodies. It is strictly interior. Reporting only its strict census would therefore be wrong.

The point `p` is also regenerated without literal long fractions by solving the three zero equations for the near cell's selected rows `[139,166,229]` in C616 or `[140,167,231]` in C620. These are facet-side predicates on original supports3,30,91, first boundary side in the canonical outward cycles. `OPTIMUM_R82.py` checks their intersection, every near-cell closure inequality, the full limit census, the exact distance formula, and the entire global exclusion tree. No uniqueness claim is made about all possible limiting points or all feasible cells. The optimized distance is L-infinity in the supplied raw axes, not Euclidean distance.

## 4. Decision algorithm and global coverage

The useful change from the parent's large Boolean formula was to search first with the **no-saddle necessary condition**, leaving S and U completely unfixed. For an edge, the four shared rational affine predicates are its two directed vertex forms and its two adjacent facet-side forms. A strict saddle has all four positive; a weak-only saddle has all four nonnegative with a zero. Therefore absence of both requires at least one strictly negative predicate. The inherited implementation independently derives and checks the line-foot/normal-cone identity on every true edge. :contentReference[oaicite:3]{index=3}

The searched relaxation is exactly:

`all interior forms > 0; and, for every true edge e, OR over its four forms of (form < 0)`.

This is used as a necessary condition, not assumed equivalent to110. Every positive point is subsequently passed through the complete S/U/H and weak audit. An exclusion of this relaxation excludes the requested full union automatically.

At a node, the numerical LP maximizes a common strict margin over the currently selected halfspaces. It only proposes a point, a violated edge clause or a small candidate certificate support. A violated edge clause branches into **all four** escape alternatives. The alternatives may overlap; they still cover every possible valid center. No vertex, facet root, Voronoi cell or witness tree is prescribed. The first unrestricted search on each target returned the preserved `discovered` point in three LP nodes, depth2, with no excluded leaves. It passed the independent exact census. Rounding then produced the quarter-coordinate witness.

Every negative leaf is justified independently with rational arithmetic. For its rows `r_i(c)=b_i+a_i·c`, the checker reconstructs nonnegative weights, normalized to sum1, such that `sum lambda_i*a_i=0`. It accepts a leaf only if `sum lambda_i*b_i<0`, or if this sum is zero and some positively weighted row is required to be strict. Interior and selected escape rows are strict; the critical cube sides are allowed to be non-strict. This distinction makes the exclusion valid on the cube boundary as well as its interior. Every leaf uses at most four rows, and every row must belong to that leaf's actual assumption path.

| Target | Complete tree nodes | Four-way branch nodes | Certified leaves | Maximum depth |
|---|---:|---:|---:|---:|
| C616 | 1221 | 305 | 916 | 15 |
| C620 | 1353 | 338 | 1015 | 15 |

The replay rejects open nodes, missing children, unproved leaves, invalid row IDs and certificates using assumptions from another branch. No timeout, negative floating margin, HiGHS infeasibility status or approximate dual vector is accepted as proof.

The two frozen trees were initially generated for radius `36335/131072` around centroids rounded to grid `10^12`. `VERIFY_R82.py` reproduces that preliminary exclusion. **The exact-optimum result is a separate, stronger verification:** `OPTIMUM_R82.py` re-instantiates the same tree's row system with the actual filled centroid and the exact critical radius `g_x-p_x`, and recomputes every certificate. The six cube normals are kept as signed unit vectors to avoid unnecessarily inflating their coefficient matrices with the very large centroid denominator. Their constants remain exact rationals. Thus the original radius field in the frozen discovery records must not be mistaken for the final optimum claim.

The capsule retains the complete numerical producer, twelve-step bisection script, exact nearest-cell LP reconstruction, critical-radius producer, independent certificate verifier and both full trees. Discovery used CPython3.13.5, NumPy2.3.5, SciPy1.17.0; `geom_search.py` sets `OPENBLAS_NUM_THREADS=1`, uses no RNG, and calls `linprog(method='highs')` with primal and dual feasibility tolerances `1e-9`. Its complete normalization, margin thresholds, rational rounding denominators, node caps and branch policy are in the source. Other HiGHS settings are defaults. The immutable tree and exact checks, not platform-dependent LP traversal order, define the reproducible certificate.

## 5. Fresh geometry/mass receipts and construction implications

The cold replay reconstructed both targets from the four inherited material texts. It reran the support-pair B hull audit, independently reran the exhaustive-triple A audit, matched A and B byte-for-byte, and completed the third centered integer-tetrahedron mass integration. C616 has344 positive centered tetrahedra and common centered denominator56869bits; C620 has346 and57351bits. Both have exactly zero filled first moments about their actual centroid and own132/weak000. This is fresh verification, not only an inherited wrapper claim.

The global distance result rules out repairing these **unchanged** geometries by a reference-center shift arbitrarily near their own centroid, regardless of root or witness turnover. A valid center must move farther than the exact0.277219... threshold. This does **not** by itself prove a Hausdorff-distance lower bound for a different successful body.

The nearest feasible basin uses stable support90, not the old own-stable support3. Its limiting obstruction involves facet-side walls from supports3,30,91. The simple center supplies a separate robust basin with stable support126. These are concrete alternatives for coupled shape-and-mass continuation; forcing the original stable face or the original frozen witness tree would miss them.

For an actual homogeneous modification P' at a selected target c, mass closure still requires

`V(P)*(g-c) + integral_(P' minus P)(x-c) dx - integral_(P minus P')(x-c) dx = 0`.

Pure addition with volume v and centroid a requires `v*(a-c)=V(P)*(c-g)`; pure removal requires `v*(a-c)=V(P)*(g-c)`. These are necessary mass identities, not a convex modification construction. :contentReference[oaicite:4]{index=4}

A useful next construction attempt should jointly move exposed geometry near the identified facet-side walls and the material contributing the required moment, recomputing exact mass and the complete feature census after contact turnover. It must not substitute nonuniform density or a point mass for uniform filling. For the C<622 goal, C616's308 edges leave only two extra true edges; C620's310 leave no edge increase without compensating coarsening. No particular mass correction was completed here, and the canonical own-centroid record is unchanged.

## 6. Durable recovery inputs

Use these four immutable materials unchanged, in the indicated order:

| Local name | Material ID | UTF-8 bytes | SHA-256 |
|---|---|---:|---|
| `part1.md` | `[internal-source-reference]` |16573|`20469536cc4461b597cd92b9c7420b89ad4f1efd82ef72aa4f934b9bb772067a`|
| `part2.md` | `[internal-source-reference]` |13041|`a527d91c2ba70ee5220ca4b6ba30964e804fd4fa52a8619d3ae6567608cc8087`|
| `part3.md` | `[internal-source-reference]` |12100|`ecb59180686fbea53343e4b78e64b70478df5ede3679acd200c163185c1e29d4`|
| `own132.md` | `[internal-source-reference]` |14491|`ea73bb56a864135d250099bb0ecedfd09f53884c559efe5913c2906d00a3b2df`|

The three CONDITION25 parts concatenate to normalized base64 length36568, SHA `6311ad9802f5a98c2600fa2d856a64af0f7a19d055c2d9849e0080c141f00c50`, decoding to the complete24-file source dictionary93169bytes, SHA `631fae9cb3d532ace34aa06230c4a5a1c03aec1d99055805e536d2442cb697b3`. The own132 material has normalized base64 length10536, SHA `7e00bccdeb2da1228fa060f2c5f8997f5cca71c2954f733beea58b703df0f85a`, decoding to19545bytes, SHA `8c876916dba1c272adcf8ec3ee4e16df120ad479b4386060e09e2b7b18a65c15`. These complete parent units are sufficient; no ancestor sandbox or numerical rediscovery is needed. :contentReference[oaicite:5]{index=5}

The capsule includes the entire authoritative `REFERENCE_LRA.py`,11491bytes, SHA `88cbab1d3e300fd463076a2cea3398d0667b4fa9b69cb316509525705028940a`. Its recovery routine reconstructs C620 generator SHA `38ebffa8f00ba3b67e105463bf162f8ac766ce2d738bf3e7a8271539d8d05cd6`; it then performs the complete C616 support105/group31/point168/axis0 collapse and DAG reordering, verifying generator SHA `4eb48034bf6d6d429c593977bee2b934759ba2c3a22865788880d4e18741720a`.

## 7. Recovery commands, observed markers and output identities

Save the following complete decoder as `RECOVER_R82.py`, and save the final base64 block as `R82_CAPSULE.b64`. The new capsule contains13 complete text files, including both full proof trees and all new continuation-critical source. It also contains source and output manifests. The parent coordinate inputs are exactly the four complete immutable materials above, not an unnamed external dependency.

```python
from pathlib import Path
import base64,hashlib,json,lzma,sys
assert __debug__ and len(sys.argv)==3,'Give R82_CAPSULE.b64 NEW_DIRECTORY'
H=lambda b:hashlib.sha256(b).hexdigest()
s=''.join(Path(sys.argv[1]).read_text(encoding='utf-8').split())
assert len(s)==27772 and H(s.encode())=='c7c0161c7514a83843e4d5d62045284696271734e6a945f3da0661f8f76e5c95'
xz=base64.b64decode(s,validate=True)
assert len(xz)==20828 and H(xz)=='476dd64a0616b6fa57f38b3efc9c9f74efeb05d412869d8ccc4f646713b1c64c'
b=lzma.decompress(xz)
assert len(b)==118035 and H(b)=='29133f0fbcbe5908a3ee7c64f4648917b6b4f26c6c20b00d4d7d2381e24123e1'
d=json.loads(b);assert len(d)==13
out=Path(sys.argv[2]);out.mkdir(parents=True,exist_ok=False)
for name,text in d.items():
 q=Path(name);assert not q.is_absolute() and '..' not in q.parts
 p=out/q;p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(text.encode('utf-8'))
for name,v in json.loads((out/'SOURCE_MANIFEST.json').read_text()).items():
 bb=(out/name).read_bytes();assert len(bb)==v['bytes'] and H(bb)==v['sha256']
print('R82_SOURCE_CAPSULE_RECOVERED13')
```

Run, with assertions enabled:

```sh
python -B -S RECOVER_R82.py R82_CAPSULE.b64 R82_RECOVERED
python -B -S R82_RECOVERED/REPLAY_R82.py part1.md part2.md part3.md own132.md
```

`R82_RECOVERED` must be new. The replay creates new `WORK`, `AUDIT`, `OPTIMUM` and `AB_MASS` subdirectories. It uses only the Python standard library; the new exact replay neither imports SciPy nor requires Z3. The tested interpreter was `3.13.5 (main, Jul 15 2026, 20:25:40) [GCC 14.2.0]`.

Observed terminal markers and frozen receipts:

```text
R82_SOURCE_CAPSULE_RECOVERED13
EXACT_REFERENCE_LRA_THREE_INPUTS_RECOVERED
R82_TWO_GLOBAL_SAT_THREE_CENTERS_AND_ALLROOT_BOX_EXCLUSIONS_EXACT_PASS
  AUDIT/RECEIPT.json: 4792 bytes
  SHA256 36d59fd850667baaaed2c904af37bf8d277ba1c0352341c1bbdde9978226f361
R82_EXACT_GLOBAL_OWN_COM_LINF_INFIMA_BOTH_CERTIFIED
  OPTIMUM/RECEIPT.json: 3874 bytes
  SHA256 4df1f2450b98221e42d06b9e9a1b5660c40e84c89eb93a8b5fccb8b87b3d8694
R82_INHERITED_AB_AND_THIRD_MASS_PASS
  AB_MASS/RECEIPT.json: 462 bytes
  SHA256 262c5ff506b54e9e84ff9830650d50fd7361640aef2ebe93ab47ffcf57f3b86c
R82_COLD_REPLAY_GLOBAL_SAT_AND_EXACT_OWN_DISTANCE_PASS 16
  EXPECTED.json SHA256 0804263f0f8c5f9eca91049fd996fedd785109b35f8a5b559a489421cbfc79bc
```

The last marker means all16 frozen output byte counts and hashes matched. The exact same replay was also run from a freshly decoded copy of the inline capsule, not merely from the original working files.

For optional numerical rediscovery after the exact replay:

```sh
python -B R82_RECOVERED/geom_search.py 616 --out REDISCOVER616.json
python -B R82_RECOVERED/geom_search.py 620 --out REDISCOVER620.json
python -B R82_RECOVERED/nearest_cell.py
python -B R82_RECOVERED/global_critical.py
```

These optional runs use the numerical dependency versions specified above; their discovery timing or traversal order need not be byte-identical. They are not required to check any reported exact conclusion.

## 8. Complete new source/certificate capsule

Normalized base64:27772characters, SHA-256 `c7c0161c7514a83843e4d5d62045284696271734e6a945f3da0661f8f76e5c95`. XZ:20828bytes, SHA-256 `476dd64a0616b6fa57f38b3efc9c9f74efeb05d412869d8ccc4f646713b1c64c`. Decoded UTF-8 JSON dictionary:118035bytes, SHA-256 `29133f0fbcbe5908a3ee7c64f4648917b6b4f26c6c20b00d4d7d2381e24123e1`.

[Supplementary executable bundle, including the four parent materials and complete cold outputs](sandbox:/mnt/data/R82_GLOBAL_CENTERS_AND_EXACT_DISTANCE.zip). 2717768 bytes; SHA-256 `3896bf441dfde762ff68007be9dae6a0e0b4a9528bdc7cd6e65009270178b782`. The inline capsule and exact parent recovery above are the durable handoff; the ZIP is only a convenience.

```base64
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
```
