# figure-0578

AI research report · 2026-09-27 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# NF93 — finite completion of J88's whole primal basin; exact own211 successors

Branch `[internal-source-reference]`; executor Nimble Finch 93; transaction `21127780a1c6250a04704786`.

## Outcome

**No own110/weak000 endpoint was obtained.** The strongest completed transition is a new homogeneous **own211/weak000 body with V37/E105/F70**, `NF93_J88_CROSSOVER_211_G8`. Its entire primal persistence list is exactly empty. Original material U40 survives as a true vertex but is no longer unstable. The price is loss of S1: the endpoint has two stable facets and one saddle. It must not be called a C210 own110 construction.

Subsequent exact own211 bodies retain E105 while reducing the remaining Q depth to .5994120407171956, or trade a slightly larger Q depth .6125097164688554 for a substantially larger certified U1 reference-centre neighbourhood. A genuine vertex-addition continuation reaches V45/E129/F86, own211, Q=.5505447402657211. A still smaller main Q in a later body comes with **twenty stable equilibria**, not cancellation. Those bodies and controls are retained separately below.

The starting object is the supplied exact `J88_FULL_C_G8_MASS`: V46/E132/F88, own121/weak000, centroid exactly zero, P=.44727218265729163 and Q empty. Its literal C input and mass correction are in the event capsule. The earlier numerical-method note predates that exact freeze; it is not used to downgrade or replace the later exact input. fileciteturn0file5L4-L10 fileciteturn0file5L23-L26

All eight supplied file byte counts and SHA-256 values matched their manifest. All supplied files were read in full. No required selected input was missing. The historical J85 raw input is not needed: the recovery below embeds the selected C coordinates and the exact target volume. None of these bodies is an alias for RA40, N40, the low-S C276 body, or the journal's C622 own110 reference construction. No replacement of that reference construction is claimed. fileciteturn0file7L351-L359

## Exact endpoints

All nine entries have additional weak census **000** and **P=[]** at their own homogeneous centroids. Their facets are genuinely maximal triangles, certified by exhaustive rational supporting-triple enumeration, not merely Qhull triangles. The radius column is a sufficient **fixed-surface reference-centre U1 cube**, not a permitted amount of arbitrary shape change and not an S2 certificate throughout that cube. Short names in the table have prefix `NF93_J88_`.

| Exact object | V/E/F | Strict S/U/H | Number of positive Q bars | Largest Q | U1 open cube radius |
|---|---:|---:|---:|---:|---:|
| `BRIDGE_U1_G8` | 37/105/70 | (7,1,6) | 6 | .7494027858773948 | .001093254063310987 |
| `ROBUST_U1_G8` | 37/105/70 | (5,1,4) | 4 | .8099452711948801 | .028665381808611796 |
| `DUAL_U1_G10` | 37/105/70 | (6,1,5) | 5 | .7296596469883191 | 1.4099518031790015e-10 |
| `CROSSOVER_211_G8` | 37/105/70 | (2,1,1) | 1 | .8119062472394063 | .02969483860146084 |
| `CLEAN_211_G8` | 37/105/70 | (2,1,1) | 1 | .5994120407171956 | 3.5255597044415264e-5 |
| `BALANCED_211_G8` | 37/105/70 | (2,1,1) | 1 | .6125097164688554 | .0020502424167189886 |
| `DETACHED_211_G10` | 39/111/74 | (2,1,1) | 1 | .5994119092081036 | 3.521289698320385e-5 |
| `EXPANDED_211_G8` | 45/129/86 | (2,1,1) | 1 | .5505447402657211 | 6.469006572040643e-5 |
| `FRAGMENTED_20_1_19_G8` | 49/141/94 | (20,1,19) | 19 | .46581365605571684 | .00010288802099240636 |

The following are **complete positive Q lists**, displayed as decimal approximations. There is no omitted tail. Exact Fraction birth, death and depth values, and their exact carrier labels, are generated in each `_AUDIT.json` by the source below. All nine P lists are empty.

```json
{
  "NF93_J88_BRIDGE_U1_G8": [0.7494027858773948,0.03103481278517677,0.02716869117324379,0.0021973531208447396,0.0014249408331206013,0.00011702602647555509],
  "NF93_J88_ROBUST_U1_G8": [0.8099452711948801,0.004695600862685626,0.0017371314470729473,0.00004870306742319011],
  "NF93_J88_DUAL_U1_G10": [0.7296596469883191,0.03316774094384398,0.031378397139118996,0.004667529690434688,0.0005239675232249472],
  "NF93_J88_CROSSOVER_211_G8": [0.8119062472394063],
  "NF93_J88_CLEAN_211_G8": [0.5994120407171956],
  "NF93_J88_BALANCED_211_G8": [0.6125097164688554],
  "NF93_J88_DETACHED_211_G10": [0.5994119092081036],
  "NF93_J88_EXPANDED_211_G8": [0.5505447402657211],
  "NF93_J88_FRAGMENTED_20_1_19_G8": [0.46581365605571684,0.0032124644922444817,0.002981077960402184,0.0011123532019669505,0.001028945143233844,0.000574556087803351,0.000500228693527833,0.0003799789806497233,0.0001807694849372787,0.00017951963381100634,0.00017222590980393916,0.0001468031974852098,0.0001307950566627316,0.00010696850407592592,0.000056039224402414954,0.00005600715140597058,0.00003975208151893904,0.00000131585527913983,0.0000010726937896462552]
}
```

### Actual homogeneous mass

The descendants are not asserted to retain the parent's volume V0. Search steps rebuild the actual hull and integrate its mass before recentering; rational freezing generally makes the new centroid small but **not zero**. These exact centroids, not the nominal origin, are used by the audits:

```json
{
  "NF93_J88_BRIDGE_U1_G8": {
    "volume":"3262501382184247266543647/1200000000000000000000000",
    "centroid":["14609883097909348566356717/6525002764368494533087294000000000","-224405098118945421912719/3262501382184247266543647000000000","-373309343278997563394453/3262501382184247266543647000000000"]
  },
  "NF93_J88_ROBUST_U1_G8": {
    "volume":"1005762891975975930096369/400000000000000000000000",
    "centroid":["-373021930045583001684359/167627148662662655016061500000000","-1268131044446847484187203/6034577351855855580578214000000000","-188679678724717465131493/754322168981981947572276750000000"]
  },
  "NF93_J88_DUAL_U1_G10": {
    "volume":"16811692727942816783215839813647/6000000000000000000000000000000",
    "centroid":["-10027947066686351078503022206283/672467709117712671328633592545880000000000","-6531096806887875697434209538311/336233854558856335664316796272940000000000","273337103552327036908201718473/21014615909928520979019799767058750000000"]
  },
  "NF93_J88_CROSSOVER_211_G8": {
    "volume":"751231485333861708604061/300000000000000000000000",
    "centroid":["20835326932965281173129547/6009851882670893668832488000000000","9097277182160004644198411/6009851882670893668832488000000000","983703103260015465418399/6009851882670893668832488000000000"]
  },
  "NF93_J88_CLEAN_211_G8": {
    "volume":"625351055041956022634207/200000000000000000000000",
    "centroid":["-761548749317269977937299/500280844033564818107365600000000","-333979409799940058432339/375210633025173613580524200000000","-1911122729824345036664831/1876053165125868067902621000000000"]
  },
  "NF93_J88_BALANCED_211_G8": {
    "volume":"6212567220342164934896081/2000000000000000000000000",
    "centroid":["-3948628623039252106374889/7455080664410597921875297200000000","-3648828085584165843915713/2485026888136865973958432400000000","-9589419338199746324066987/7455080664410597921875297200000000"]
  },
  "NF93_J88_DETACHED_211_G10": {
    "volume":"1876053413444678349076990859/600000000000000000000000000",
    "centroid":["-2977703724684463022484674398047/37521068268893566981539817180000000000","-481239625069386247101906490001/9380267067223391745384954295000000000","864360172007384120960150465697/75042136537787133963079634360000000000"]
  },
  "NF93_J88_EXPANDED_211_G8": {
    "volume":"9639164058179147603764043/3000000000000000000000000",
    "centroid":["-358490810621891180744787/240979101454478690094101075000000","9288353448311913234151907/7711331246543318083011234400000000","-11373180093057189236275127/7711331246543318083011234400000000"]
  },
  "NF93_J88_FRAGMENTED_20_1_19_G8": {
    "volume":"20269830278689141035695399/6000000000000000000000000",
    "centroid":["114417243695450325095481/506745756967228525892384975000000","-905792566135359976834923/810793211147565641427815960000000","85643514855673302723729/101349151393445705178476995000000"]
  }
}
```

## What actually changed

The initial physical bridge has seven links and six new material rows46..51. It uses the short spherical arc from material40 to0, with bend0, power1 and radial-bend0, as specified by the complete numerical `chain` function. The numerical initial hull drops original rows19 and45. An actual-hull maximin global-chord tree flow then takes **18 accepted steps**, with no S quota. Freezing its final true vertices on denominator10^8 gives the exact BRIDGE_U1 body: 37/105/70, strict716, weak000, no P, six positive Q bars.

The material accounting needs both pruning maps. The following 37-entry list maps the compact BRIDGE/CROSSOVER/CLEAN/BALANCED rows to original J88 rows plus bridge rows46..51:

```text
[0,1,4,5,6,7,10,14,15,16,17,20,21,22,26,27,28,30,31,32,33,34,35,36,37,38,39,40,41,42,44,46,47,48,49,50,51]
```

Thus original U40 is **compact27**, not compact28. The retired original/bridge rows are `[2,3,8,9,11,12,13,18,19,23,24,25,29,43,45]`; all six bridge rows survive. In CROSSOVER the exact positive witness path for old U40 is

```text
compact: 27 -> 29 -> 28 -> 31 -> 32 -> 33 -> 34 -> 35 -> 36 -> 0
material:40 -> 42 -> 41 -> 46 -> 47 -> 48 -> 49 -> 50 -> 51 -> 0
```

Every nonroot, not just this path, has a positive exact outgoing chord in the recovered certificate. Positive chords strictly increase squared radius, so their paths cannot cycle and terminate at the sole unstable vertex0. This certifies retirement of the entire original unwanted primal basin, rather than deletion of its birth label or attenuation of one witness.

S1 genuinely failed. The old stable carrier `{0,30,45}` does not survive, since45 is absent from the final hull. BRIDGE has seven actual stable facets. A further **220-iteration** primal-tree clearance phase yields ROBUST_U1, exact514; the requested width .12 is not attained. Two accepted minor-Q repair steps then give CROSSOVER, exact211. Its stable triangles in exact compact ordering are `[7,36,13]` and `[12,22,36]`, corresponding to material `[14,51,22]` and `[21,35,51]`. Its saddle is compact `[8,11]`, material `[15,20]`. Neither stable carrier is the old J88 stable triangle.

The lower-Q branch uses actual-U1-constrained affine nomination, then alternating current-Q-bar descent and U1 clearance, and finally reconsolidates the extra small Q basins. The completed producing prefixes are: 12 affine starts; a two-accepted-step clearance phase; seven completed power-two cycles, each with at most50 descent and25 clearance iterations; twelve power-one cycles, each with at most32 descent and20 clearance iterations. The original requests for more cycles were interrupted; the recipe below runs the completed prefixes, not those unexecuted requests. CLEAN is obtained by the minor-Q repair of that final numerical state. BALANCED instead follows the separate clearance with hard Q-sum cap .592, then minor-Q repair with primal angular floor .003.

CLEAN and BALANCED have stable facets `[0,5,22]` and `[0,36,13]`: both contain the unique unstable vertex0. Their remaining saddle is `[8,20]`. Their Q depths should not be compared without the capacity tradeoff: CLEAN's sufficient U1 cube radius is about3.53e-5, versus CROSSOVER's .02969 and BALANCED's .00205. The auxiliary DUAL_U1 control has an especially small U1 cube, about1.41e-10; its slightly lower main Q is not a robust improvement.

DETACHED is a separate exact two-stellar construction from CLEAN. At each of its two steps, take the actual stable-foot point f on a stable triangle containing U0, and add the rationally frozen point `(f+p0)/2 + 10^-6*(f-g)`, using denominator10^10 and exact ties-to-even rounding. Both finite endpoints are audited. Its new stable carriers `[5,22,37]` and `[13,38,36]` exclude U0; true counts are39/111/74 and class211 persists. This frees the carriers without pretending to cancel the remaining Q basin.

EXPANDED starts from exact BALANCED, makes32 accepted small actual-hull face additions of height10^-4, and temporarily uses69 material points, giving the general true-edge upper bound201. Thirteen completed power-one descent/clearance cycles and a minor-Q repair with primal floor10^-4 yield the exact45/129/86 own211 endpoint. Its stable triangles are `[0,41,22]` and `[13,37,38]`; the remaining saddle is `[8,20]`. This is a different body from every other E129 input in the journal.

The subsequent38-addition experiment starts from exact EXPANDED and temporarily uses83 material points, giving the general true-edge upper bound243 before continuation. Eleven completed cycles, followed by fourteen further completed cycles, then180 minor-Q-repair iterations produce the preserved FRAGMENTED body49/141/94, strict(20,1,19), weak000. Its nineteen positive Q bars are listed above. The smaller .46581365605571684 main bar is **not** an improved211, let alone110. Its canonical name contains its actual class; an exploratory filename containing `EXPANDED2_211` is not used as its identity.

## Exact verification and two reusable results

The first audit reuses the supplied J88 Fraction census core: actual supporting planes, homogeneous volume and centroid, global primal/polar root predicates, direct edge saddle/weak predicates and all positive bars. fileciteturn0file0L61-L100 The new second check uses direct projected-foot edge signs for facets and local true-edge guards for vertices. It also integrates over strictly positive tetrahedra based at the mean of all true vertices; its volume and centroid agree exactly with the signed-origin integration. These are distinct census/mass computations sharing the same certified hull and basic rational vector operations, not a claimed completely independent second hull engine. The additional direct-incidence zero diagnostics are000 for the nine primary entries.

The exact supporting-triple routine deliberately rejects nonsimplicial endpoints. Every claimed body passes its triangular-maximal-facet requirement. A future nonsimplicial nominee needs a genuine maximal-facet extension, not acceptance of a triangulation count.

### Intrinsic adjacent-polar angular score

For an outward oriented centered triangle `(u,v,w)` with normal n, the outgoing polar angular score across its oriented edge u->v is

`-n·(u×v) / (|n| |u×v|)`.

Indeed the adjacent polar difference is `-lambda*(u×v)` with lambda>0: both polar points pair to1 with u and v, while the adjacent one pairs to less than1 with w, and det(u,v,w)>0. The scalar cancels from the normalized score. This avoids differentiating a ratio of two nearly coincident polar vertices. The formula is for distinct true adjacent facets; it is not permission to count a coplanar triangulation as separate facets. The minor-Q repair uses this expression, while exact acceptance still uses the full census.

### U1 centre cubes and a whole-Q-basin trap

For a positive primal witness i->j at the actual centroid g, let `W=(p_i-g)·(p_j-p_i)`. It stays positive for infinity-norm centre displacement less than `W/|p_j-p_i|_1`. Select the largest such bound at every nonroot and intersect with the interior-support and strict-root bounds. The exact code verifies all eight corners of the closed half-radius cube. This is only a fixed-surface U1/no-weak-U certificate; it does not certify arbitrary shape motions.

There is also a new exact **fixed-surface** obstruction on CROSSOVER. In its exact face ordering, the dual block is

`[0,2,4,6,9,19,31,32,38,39,40,41,42,43,68]`.

It has17 outgoing dual edges. Every boundary outgoing score remains negative throughout the closed centre cube of radius

`94576726957904025466463219040778446266468500263063910483263 / 996368703820577872438440813762277898652803093574400000000000`

about .09492141472855316. The outside elder, face29, stays strictly stable there. Hence **S>=2 throughout that entire closed cube**, including the smaller certified U1 cube; relabeling the stable birth inside the block cannot remove it.

For fixed normals n_i and own-centred supports a_i, the polar outgoing numerator is `N_ij=(n_i·n_j)*a_i-|n_i|^2*a_j`; its centre-displacement coefficient is `B_ij=|n_i|^2*n_j-(n_i·n_j)*n_i`. The code computes an exact minimax directed-graph cut with threshold `max(0,-N_ij/|B_ij|_1)`. A maximum-radius polar vertex within the block has strictly negative internal scores, and the certified boundary inequalities make it a strict stable equilibrium. The separate elder gives another. CLEAN and BALANCED have analogous exact closed-cube radii .04740926287988333 and .04901247723621328, with16/18 and17/19 block/port counts. All planes, block faces, port vectors and rational bounds are regenerated from the literal coordinates.

These are not exclusions of changed facets, different affine metrics, reference centres outside the cubes, or finite added/removed material. They identify a concrete next boundary to alter, rather than an excuse to repeat centre-only motion or retire a single stable label.

## Continuation and evidence boundary

CROSSOVER offers the largest certified fixed-surface U1 neighbourhood; BALANCED is the intermediate Q/capacity compromise; EXPANDED has the smallest remaining Q among these exact211 endpoints but a much smaller U1 neighbourhood. The E105 inputs leave144 true edges of headroom: adding up to48 vertices would still give V<=85 and the general E<=3V-6<=249 bound. Prefer whole-Q-boundary/fan surgery with live homogeneous mass, allowing carrier changes and temporary pairs but reconsolidating them before acceptance. The exact trap identifies the unchanged-boundary limitation; it supplies no global impossibility result.

The precise numerical paths are not certified rational curves, and a solver success flag is not a body certificate. The canonical exact objects are the literal rational checkpoints below. Source-only replay of the consolidated numerical BRIDGE and CROSSOVER recipes regenerated the BRIDGE, ROBUST and CROSSOVER input byte hashes exactly in the recorded environment. The long consolidated descent recipe was checked only through a prefix, not rerun completely after consolidation. All exact endpoints, including its later literal outputs, were separately reconstructed and their complete output-manifest hash checked repeatedly.

The capsule also reconstructs15 specified exact coarsenings of CROSSOVER/CLEAN/BALANCED on grids10^3 through10^7. Useful simpler exact211 inputs include CROSSOVER_G5, CLEAN_G6 and BALANCED_G6. These are distinct bodies, not denominator-only aliases. For example CLEAN rounded to G5 is actually312, with an additional genuine Q depth4.886335027148757e-11. No minimal-denominator or full-neighbourhood claim is made.

## Durable reconstruction

Save the following complete units as `NF93_EXACT.py` and `NF93_NUMERICAL.py` in the same directory. Exact recovery has no numerical-package or external-file dependency:

```sh
python NF93_EXACT.py
```

Expected terminal marker: `NF93_EXACT_RECOVERY_PASS_WHOLE_P_CANCELLED_NO_110`.
The recovered canonical `NF93_MANIFEST.json` is10734 bytes, SHA-256 `db5511156163637eba2aace71283baa758eb98224c47305db74ad25919129e9d`; its78 entries cover the parent reconstruction, all24 new primary/control bodies, certificates and cut data. The program checks this exact manifest digest after checking geometry, mass, census, weak equilibria, Euler and all positive-bar counts. The manifest itself is an additional output file.

The complete numerical unit uses CPython3.13.5, NumPy2.3.5, SciPy1.17.0 and PyTorch2.10.0+cpu, float64 and one Torch thread. Its historical floating bar cutoff is1e-14 and is nomination-only, never the exact acceptance criterion. fileciteturn0file6L29-L48 Run selected producing prefixes with:

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python NF93_NUMERICAL.py bridge
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python NF93_NUMERICAL.py crossover
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python NF93_NUMERICAL.py descent
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python NF93_NUMERICAL.py expanded
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python NF93_NUMERICAL.py fragmented
# Optional auxiliary control; uses the numerical output of the bridge recipe:
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python NF93_NUMERICAL.py dual
```

Exact starting-parent identity: `J88_FULL_C_G8_INPUT.json`,1430 bytes, SHA-256 `2460fe721517acd3564b2b80709de47d4adac4f53f77c3323c6c023c7889b718`. Its restored volume is `3791834665223904409031391864938220273/2000000000000000000000000000000000000`; the corrector is material16,y, followed by the actual exact centroid translation.

Primary frozen-input identities:

| Input | Bytes | SHA-256 |
|---|---:|---|
| `NF93_J88_BRIDGE_U1_G8_INPUT.json` | 1183 | `4f9fc67cc8d3d8c9d747bc8341e88bafd1e5a0da80f51ad30b10cb5b86f4f521` |
| `NF93_J88_ROBUST_U1_G8_INPUT.json` | 1190 | `b4f9d5fcc712f1ef92b41f9c57b6372a28270b7c11237a0492c8477b939a0987` |
| `NF93_J88_DUAL_U1_G10_INPUT.json` | 1407 | `67abc529dffafe8d6e13879142c1a22e20a3272d5994540e55a7743471c5a289` |
| `NF93_J88_CROSSOVER_211_G8_INPUT.json` | 1194 | `a02eaaf4021f56fe9a96a7800112309d3e07a87ec497ae2bd0435e44eca092eb` |
| `NF93_J88_CLEAN_211_G8_INPUT.json` | 1193 | `6dea75bf7ec864b6ff737f9cc41a404fb34650cadfd05f94be0c49994545a359` |
| `NF93_J88_BALANCED_211_G8_INPUT.json` | 1193 | `3b9873aca31fdc7cab0362465dc3ecc894b7188afd02021f039718ccd0f44871` |
| `NF93_J88_DETACHED_211_G10_INPUT.json` | 1494 | `0ef94c445ea105425b3aeb006d7c4d28aecbf8ae80d4012be097e2ff34e7c8aa` |
| `NF93_J88_EXPANDED_211_G8_INPUT.json` | 1437 | `f66ac4a8987e7cc7567cbe81ee4043465d4f1bd8bdf7b3e17cd46d6dc98cc512` |
| `NF93_J88_FRAGMENTED_20_1_19_G8_INPUT.json` | 1562 | `4a15f1b525d08e085ff5c1ec791f8dda7df0925beb9e8459afc106be4c4af527` |

Source-unit identities:

`NF93_EXACT.py`: 25767 bytes; SHA-256 `70be6a46d2b192621511f72547dcd1f91081d45efebddaca5b54ebf277bebb08`.

`NF93_NUMERICAL.py`: 22224 bytes; SHA-256 `a6679803bf3094e053574866a0689becb0adcf59c4f3e64a59eba2d727cc015a`.

### NF93_EXACT.py — complete self-contained construction and exact checks

```python
"""NF93 exact self-contained recovery; CPython 3.11+ standard library.
Every hull support, homogeneous mass, strict/weak census and positive bar is exact.
The second direct-incidence census and interior-positive tetrahedra check are
independent computations, not an independent hull engine or research replica.
No optimizer, external body or original sandbox is needed.
"""
from fractions import Fraction as R
from itertools import combinations,product
from math import lcm
from pathlib import Path
import json,hashlib,heapq,argparse
ROOT=Path(__file__).resolve().parent/'NF93_EXACT_OUTPUT'
V0=R(3791834665223904409031391864938220273,2000000000000000000000000000000000000)
def add(a,b):return tuple(x+y for x,y in zip(a,b))


def sub(a,b):return tuple(x-y for x,y in zip(a,b))


def mul(a,t):return tuple(x*t for x in a)


def dot(a,b):return sum(x*y for x,y in zip(a,b))


def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])


def det(a,b,c):return dot(a,cross(b,c))


def topology(p,faces):
    edges={};planes=[];verts=set()
    for i,f in enumerate(faces):
        verts.update(f);n=cross(sub(p[f[1]],p[f[0]]),sub(p[f[2]],p[f[0]]));h=dot(n,p[f[0]])
        assert n!=(0,0,0)
        vals=[dot(n,x)-h for x in p]
        assert max(vals)==0,('invalid support',i,max(vals))
        assert {j for j,v in enumerate(vals) if v==0}==set(f),('coplanarity',i)
        planes.append((n,h))
        for a,b in zip(f,f[1:]+f[:1]):edges.setdefault(tuple(sorted((a,b))),[]).append((i,a,b))
    assert verts==set(range(len(p)))
    assert all(len(e)==2 and e[0][1:]==e[1][1:][::-1] for e in edges.values())
    assert len(p)-len(edges)+len(faces)==2
    return edges,planes


def mass(p,faces):
    W=R(0);K=(R(0),)*3
    for f in faces:
        a=p[f[0]]
        for i in range(1,len(f)-1):
            b,c=p[f[i]],p[f[i+1]];z=det(a,b,c)
            W+=z;K=add(K,mul(add(a,add(b,c)),z))
    assert W>0
    return W/6,mul(K,1/(4*W))


def bars(p,edges):
    rad=[dot(v,v) for v in p];parent=list(range(len(p)))
    def find(i):
        while parent[i]!=i:parent[i]=parent[parent[i]];i=parent[i]
        return i
    events=[]
    for a,b in edges:
        d=sub(p[b],p[a]);t=max(R(0),min(R(1),-dot(p[a],d)/dot(d,d)))
        q=add(p[a],mul(d,t));events.append((dot(q,q),a,b))
    out=[]
    for level,a,b in sorted(events,reverse=True):
        i,j=find(a),find(b)
        if i==j:continue
        if (rad[i],-i)<(rad[j],-j):i,j=j,i
        if rad[j]>level:out.append({'root':j,'birth2':str(rad[j]),'death2':str(level),'depth':str(1-level/rad[j]),'edge':[a,b]})
        parent[j]=i
    assert len({find(i) for i in range(len(p))})==1
    return sorted(out,key=lambda b:R(b['depth']),reverse=True)


def audit(p,faces):
    edges,planes=topology(p,faces);V,g=mass(p,faces);xx=[sub(x,g) for x in p];yy=[]
    for n,h in planes:
        z=h-dot(n,g);assert z>0;yy.append(mul(n,1/z))
    def roots(x):
        strict=[];weak=[]
        for i,a in enumerate(x):
            m=max(dot(a,sub(b,a)) for j,b in enumerate(x) if i!=j)
            if m<0:strict.append(i)
            elif m==0:weak.append(i)
        return strict,weak
    U,WU=roots(xx);S,WS=roots(yy);H=[];WH=[]
    for (a,b),ef in edges.items():
        d=sub(xx[b],xx[a]);t=-dot(xx[a],d)/dot(d,d);r=add(xx[a],mul(d,t))
        n,m=planes[ef[0][0]][0],planes[ef[1][0]][0]
        nn,mm,nm=dot(n,n),dot(m,m),dot(n,m);D=nn*mm-nm*nm;assert D>0
        x=(dot(r,n)*mm-dot(r,m)*nm)/D;y=(dot(r,m)*nn-dot(r,n)*nm)/D
        if 0<t<1 and x>0 and y>0:H.append([a,b])
        elif 0<=t<=1 and x>=0 and y>=0:WH.append([a,b])
    dual=[(e[0][0],e[1][0]) for e in edges.values()]
    return dict(V=len(p),E=len(edges),F=len(faces),C=2*len(edges),volume=str(V),centroid=list(map(str,g)),strict=[len(S),len(U),len(H)],weak=[len(WS),len(WU),len(WH)],S=S,U=U,H=H,P=bars(xx,list(edges)),Q=bars(yy,dual))


def exact_hull(p):
    D=lcm(*(x.denominator for v in p for x in v));rows=[tuple(int(x*D) for x in v) for v in p];fs=[]
    for a,b,c in combinations(range(len(rows)),3):
        n=cross(sub(rows[b],rows[a]),sub(rows[c],rows[a]));h=dot(n,rows[a])
        if n==(0,0,0):continue
        vals=[dot(n,v)-h for v in rows]
        if min(vals)<0<max(vals):continue
        assert sum(v==0 for v in vals)==3,'nonsimplicial endpoint'
        fs.append([a,b,c] if max(vals)==0 else [a,c,b])
    assert set(range(len(rows)))=={i for f in fs for i in f},'some row is not a true vertex'
    return fs


def correct(p,fs,V0,pivot=(16,1)):
    """A rational chart wherever the selected volume coefficient is nonzero."""
    a,k=pivot;A=R(0)
    for f in fs:
        if a not in f:continue
        pos=f.index(a);j,l=f[(pos+1)%3],f[(pos+2)%3]
        A+=cross(p[j],p[l])[k]/6
    assert A!=0
    V,g=mass(p,fs);alpha=(V0-V)/A
    q=[list(v) for v in p];q[a][k]+=alpha;q=list(map(tuple,q))
    V1,g1=mass(q,fs);assert V1==V0
    q=[sub(v,g1) for v in q];assert mass(q,fs)==(V0,(0,0,0))
    topology(q,fs)
    return q,dict(pivot=list(pivot),coefficient=str(A),correction=str(alpha),translation=list(map(str,g1)))


def certify(p,f):
 e,planes=topology(p,f);V,g=mass(p,f);c=mul(tuple(map(sum,zip(*p))),R(1,len(p)))
 VV=R(0);MM=(R(0),)*3
 for tri in f:
  a,b,d=(p[i] for i in tri);dv=det(sub(a,c),sub(b,c),sub(d,c))/6
  assert dv>0
  VV+=dv;MM=add(MM,mul(add(c,add(a,add(b,d))),dv/4))
 assert VV==V and mul(MM,1/VV)==g
 x=[sub(a,g) for a in p];adj=[set() for a in p]
 for a,b in e:adj[a].add(b);adj[b].add(a)
 S=[];WS=[];U=[];WU=[];H=[];WH=[];zero=[0,0,0]
 for i,(n,h) in enumerate(planes):
  foot=add(g,mul(n,(h-dot(n,g))/dot(n,n)))
  t=f[i];v=[dot(n,cross(sub(p[b],p[a]),sub(foot,p[a]))) for a,b in zip(t,t[1:]+t[:1])]
  zero[0]+=sum(z==0 for z in v)
  if min(v)>0:S.append(i)
  elif min(v)>=0:WS.append(i)
 for i in range(len(p)):
  v=[dot(x[i],sub(p[j],p[i])) for j in sorted(adj[i])];zero[1]+=sum(z==0 for z in v)
  if max(v)<0:U.append(i)
  elif max(v)==0:WU.append(i)
 for (a,b),ef in e.items():
  u,v=planes[ef[0][0]][0],planes[ef[1][0]][0];d=sub(p[b],p[a]);dd=dot(d,d);T=-dot(x[a],d);rr=add(mul(x[a],dd),mul(d,T));uu,vv,uv=dot(u,u),dot(v,v),dot(u,v);X=dot(rr,u)*vv-dot(rr,v)*uv;Y=dot(rr,v)*uu-dot(rr,u)*uv
  v4=[T,dd-T,X,Y];zero[2]+=sum(z==0 for z in v4)
  if min(v4)>0:H.append([a,b])
  elif min(v4)>=0:WH.append([a,b])
 expected=audit(p,f)
 assert S==expected['S'] and U==expected['U'] and H==expected['H']
 assert [len(WS),len(WU),len(WH)]==expected['weak']
 out=dict(strict=[len(S),len(U),len(H)],weak=[len(WS),len(WU),len(WH)],primitive_zeros=zero,positive_tetrahedra=len(f),volume=str(V),centroid=list(map(str,g)))
 if len(U)!=1:return out
 root=U[0];rho=min((h-dot(n,g))/sum(map(abs,n)) for n,h in planes);inside=rho;witness=[];parents={};lim=None
 for i in range(len(p)):
  if i==root:continue
  opts=[]
  for j in range(len(p)):
   if i==j:continue
   d=sub(p[j],p[i]);w=dot(x[i],d)
   if w>0:opts.append((w/sum(map(abs,d)),j,w))
  r,j,w=max(opts);witness.append([i,j,str(w),str(r)]);parents[i]=j
  if r<rho:rho=r;lim=[i,j]
 # Explicit unique-root strict inequalities, in addition to the no-cycle argument.
 rootbound=min(-dot(x[root],sub(p[j],p[root]))/sum(map(abs,sub(p[j],p[root]))) for j in range(len(p)) if j!=root)
 rho=min(rho,rootbound)
 paths=[]
 for i in range(len(p)):
  a=i;path=[a]
  while a!=root:
   a=parents[a];assert a not in path;path.append(a)
  paths.append(path)
 # Verify closed half-cube directly: all fixed witnesses and root inequalities.
 from itertools import product
 for ss in product([-1,1],repeat=3):
  gg=add(g,mul(ss,rho/2));xx=[sub(a,gg) for a in p]
  assert all(h-dot(n,gg)>0 for n,h in planes)
  assert all(dot(xx[i],sub(p[j],p[i]))>0 for i,j,_,_ in witness)
  assert all(dot(xx[root],sub(p[j],p[root]))<0 for j in range(len(p)) if j!=root)
 out['U1_cube']=dict(root=root,open_rho=str(rho),closed_rho=str(rho/2),open_rho_float=float(rho),inside_bound=str(inside),root_bound=str(rootbound),limiting_witness=lim,witnesses=witness,paths=paths)
 return out


def trap(p,f):
 edges,planes=topology(p,f);V,g=mass(p,f);ns=[n for n,h in planes];hs=[h-dot(n,g) for n,h in planes];q=[mul(n,1/h) for n,h in zip(ns,hs)];elder=max(range(len(q)),key=lambda i:(dot(q[i],q[i]),-i));adj=[set() for _ in q]
 for ef in edges.values():a,b=ef[0][0],ef[1][0];adj[a].add(b);adj[b].add(a)
 arc={}
 for i in range(len(q)):
  n=ns[i];nn=dot(n,n)
  for j in adj[i]:
   m=ns[j];nm=dot(n,m);W=nm*hs[i]-nn*hs[j];B=sub(mul(m,nn),mul(n,nm));den=sum(map(abs,B));assert den>0;threshold=max(R(0),-W/den);arc[i,j]=(W,B,threshold)
 dist=[None]*len(q);dist[elder]=R(0);heap=[(R(0),elder)]
 while heap:
  dd,j=heapq.heappop(heap)
  if dd!=dist[j]:continue
  for i in adj[j]:
   d=max(dd,arc[i,j][2])
   if dist[i] is None or d<dist[i]:dist[i]=d;heapq.heappush(heap,(d,i))
 eps=max(dist);block={i for i,d in enumerate(dist) if d==eps};assert block and elder not in block
 cut=[(i,j) for i in sorted(block) for j in sorted(adj[i]-block)];assert cut
 bound=min(-arc[i,j][0]/sum(map(abs,arc[i,j][1])) for i,j in cut);assert bound==eps
 er=min(-arc[elder,j][0]/sum(map(abs,arc[elder,j][1])) for j in adj[elder]);assert er>0
 inside=min(h/sum(map(abs,n)) for n,h in zip(ns,hs));r=min(bound,er,inside)*R(99,100)
 assert all(arc[i,j][0]+r*sum(map(abs,arc[i,j][1]))<0 for i,j in cut)
 assert all(arc[elder,j][0]+r*sum(map(abs,arc[elder,j][1]))<0 for j in adj[elder])
 return dict(block=sorted(block),block_faces=[f[i] for i in sorted(block)],elder=elder,elder_face=f[elder],cut=[[i,j,str(arc[i,j][0]),list(map(str,arc[i,j][1])),str(arc[i,j][2])] for i,j in cut],cut_bound=str(bound),elder_bound=str(er),inside_bound=str(inside),closed_cube_rho=str(r),closed_cube_rho_float=float(r),centroid=list(map(str,g)))


BASE=[{"denominator":100000000,"name":"NF93_J88_BRIDGE_U1_G8","points":[[-150370654,-107388266,35970049],[-129711678,-748930,-35256184],[-60184963,86181030,-33448648],[-99446380,36807334,-60626363],[-85565979,62856125,-49300921],[-67954325,50900080,-77929537],[-36013383,59579391,-84287978],[-190412,86601739,37501863],[-4401333,66784659,-78985480],[17718247,98084504,2790265],[38170821,95406857,1019267],[25444225,92082301,-22438119],[12038975,44887554,-82549926],[30578952,86690308,41217796],[52347454,90267580,13817105],[54141902,77656621,44855883],[66833114,80898224,24010763],[91491380,1049386,-52460348],[87317339,67186830,7769961],[78845604,68252655,33986597],[72874252,75616605,-15030701],[99315917,51132268,15868250],[79159482,37392461,-53830556],[93437456,51336115,34698674],[97894601,35969332,-32158282],[106408102,34526740,25372831],[114102618,13233568,22387491],[115037174,-12910639,-15053209],[116371852,-37812165,12807741],[118008725,-10677813,17430498],[105894422,13836528,-32665542],[106928460,-64705070,19681618],[90217393,-90770782,26130168],[64193286,-113683689,37676680],[29090874,-130179630,49957883],[-18289350,-139561679,56697587],[-70704391,-135012314,56369285]]},{"denominator":100000000,"name":"NF93_J88_ROBUST_U1_G8","points":[[-154804778,-113545754,38211727],[-144005338,-13659998,-30523044],[-53458305,92784520,-34433957],[-120201186,28673416,-54767394],[-90644886,68598955,-48120222],[-85178094,51394700,-75518615],[-47961646,67658869,-81485692],[16267896,86392270,31738222],[-12935065,79748260,-72032095],[34974875,93913743,4776281],[59514028,86528829,-296921],[43891197,89901581,-16339010],[13280297,53543021,-77431571],[49486695,80013403,37643163],[74441739,77486805,7765283],[76549760,64533442,39325932],[87130737,65797015,15965442],[91782571,2541067,-41949598],[98642325,46725619,-14840140],[98362233,50676240,23805165],[78808763,56967956,-36880351],[110854274,29766329,3064677],[83391279,18042203,-53312821],[108732968,32510262,24338538],[100971837,13599577,-38003831],[116534231,11511939,22503916],[118658003,-10921890,28513213],[116180580,-33099832,1991142],[110439013,-58075989,33702018],[116659910,-34359542,32338462],[110515996,-9722470,-24779837],[98005016,-81013303,39277751],[80138366,-102191561,44209087],[56825319,-120080434,49030016],[27699299,-133928627,52877630],[-10967453,-142094884,57235808],[-59187989,-140930424,56639212]]},{"denominator":10000000000,"name":"NF93_J88_DUAL_U1_G10","points":[[-14629213066,-10920278733,3516560289],[-13048696410,-33543157,-3121995330],[-6027029000,8620606487,-3158360958],[-10022166624,3680695423,-5916889433],[-8634126498,6306134987,-4990368194],[-6873393833,4910327511,-7861474358],[-3678866909,6060715197,-8428599118],[388811155,8277296420,3928471909],[-290309149,6792893350,-7925154004],[1694296126,9910953861,691903564],[4224934474,9608703430,70095339],[2952274873,9322657536,-2324256448],[1520812149,4105877885,-8335437194],[3300746897,8436812897,4261306275],[5467284183,9051039509,1633416698],[5324737621,7611096065,4794964542],[6821085900,8057175607,2609967342],[9290043502,89076645,-4963404099],[8979862290,6610092351,696551498],[8039931371,6659025252,3742901182],[7401698480,7663245663,-1583514630],[10036826065,5062817417,1753534063],[8304456603,3853673457,-5463500192],[9346214356,5229037018,3527495783],[10011749323,3333573736,-3247133948],[10768855360,3317616385,2602326375],[11504482865,1256371542,2185996278],[11619629329,-1188560368,-1100384506],[11650330114,-3819020600,1424478990],[11861226848,-1186042759,1773714806],[10819148669,1157966853,-2993122689],[10698134980,-6456144278,2161261903],[8977449276,-9114479865,2739571838],[6357293006,-11378588699,3805922199],[2919144440,-12908376227,4978091045],[-1788030997,-13841740492,5752162939],[-7047967756,-13398727879,6053788835]]},{"denominator":100000000,"name":"NF93_J88_CROSSOVER_211_G8","points":[[-154654161,-113252843,38083101],[-143854721,-13367087,-30651670],[-53307689,92476981,-34562583],[-120050569,28966327,-54896020],[-90494269,68891866,-48248847],[-85027478,51687611,-75647241],[-47811029,67951780,-81614317],[16418513,86685181,31609596],[-14451805,80041171,-72160721],[35125491,92647206,4647655],[59664645,86821740,-425547],[44041814,90194492,-16738780],[13248560,53835933,-77560196],[49637312,80306314,37514538],[74592355,77779716,7636658],[76700377,64826353,39197307],[87281353,66089926,15836816],[91933188,2833978,-42078224],[98792942,47018531,-14968765],[98512849,50969151,23676540],[78959380,53260868,-37008977],[111004890,30059240,2936051],[83541895,18335114,-53441446],[108883584,32803173,24209913],[101122453,13892488,-38132457],[116684847,11804850,22375290],[118808619,-10628978,28384588],[116331197,-32806921,1862516],[110589629,-57783078,33573393],[116810527,-34066631,32209836],[110666612,-9429558,-24908462],[98155632,-80720392,39149125],[80288982,-101898650,44080462],[56975935,-119787523,48901390],[27849915,-133635716,52749004],[-10816837,-141801973,57107182],[-59037373,-140637512,56510586]]},{"denominator":100000000,"name":"NF93_J88_CLEAN_211_G8","points":[[-141928587,-91801949,44711612],[-141509451,-25110353,-24851011],[-67991331,88281192,-32871121],[-125184622,10199286,-54571181],[-100219850,55441424,-54443543],[-89938391,27846262,-84680430],[-55512668,50968533,-92587858],[-7322627,70564938,39144499],[-20842059,70881266,-76807915],[33469839,82054415,18820904],[57213401,81824581,1393363],[43988134,80152074,-18752451],[5230810,45199905,-80532584],[31885689,71641501,55640447],[75908001,79885050,8830401],[75375145,67072949,46174643],[91479832,65261848,19785295],[98883104,-18586649,-52381623],[101841082,44456194,-21190225],[100252538,49629412,30934149],[80043490,56961686,-44422493],[114637827,25783153,1114813],[83050958,-5347169,-64921614],[111220961,27342134,31161768],[103474734,5678203,-44485509],[118859685,6097653,22549238],[119170362,-20506161,28110772],[118109823,-33314841,1305987],[104126332,-66891859,37364715],[114532541,-45287646,30318067],[112494352,-21915489,-27160619],[89340989,-87278192,42080685],[70039233,-104050036,48281546],[46632909,-116382659,55664276],[19175758,-123268575,64274684],[-19629751,-126081488,70463064],[-66375337,-120174300,68227055]]},{"denominator":100000000,"name":"NF93_J88_BALANCED_211_G8","points":[[-141293002,-92143143,45198025],[-140717614,-24884540,-24504547],[-67786419,88044199,-33814634],[-124870619,11527743,-53351228],[-100539433,55945110,-52243057],[-88775113,28069113,-84091323],[-54268179,50026142,-92317399],[-8502127,70756024,38407903],[-19596920,72343977,-79296765],[30553923,81883619,19179466],[52641585,82056479,756673],[40833274,80148770,-19941432],[4874949,45728165,-81523247],[32353257,72394974,55349689],[71761614,80119232,8005304],[74776809,65063462,46687053],[89300551,64628163,19157240],[99355680,-18863345,-51651368],[101409312,43538229,-22322888],[97868400,49025068,33000198],[79557765,56613023,-44495029],[114326385,25616106,718796],[83236034,-4871216,-65062478],[110950138,27541948,29247224],[101977071,4866598,-43412792],[118744777,5730262,20727965],[119190529,-19643831,25766906],[117558742,-32902766,1178984],[104008053,-65958334,38044914],[114395507,-44686199,29280495],[113191349,-20130786,-25935495],[89496975,-86213765,42856807],[69932266,-103458767,49269247],[46124451,-116365544,56187803],[18560422,-123575400,64099987],[-21204954,-126454911,70328185],[-67158857,-120309084,67969959]]},{"denominator":100000000,"name":"NF93_J88_EXPANDED_211_G8","points":[[-141265478,-89825373,43593950],[-141892050,-28654295,-19694172],[-67736368,87931548,-34428131],[-127095885,9282551,-50030140],[-102009707,55418594,-50053184],[-92052168,24865853,-83079078],[-53576433,46823975,-93986052],[-17953064,66947895,38437367],[-27087412,69036251,-79342315],[35798080,84267399,24685897],[51274768,85262776,4239691],[41526922,83168287,-17643691],[667240,47497111,-79234855],[26815902,69014423,57873589],[71315934,81888541,5865616],[69958212,66874437,48628692],[89557333,65036211,20135564],[99809571,-23645091,-49757538],[102243990,41902936,-20860516],[99213459,47849128,32713753],[79757824,57139564,-42476054],[114724823,22771399,1813489],[86569152,-6130444,-68043072],[111069517,24345621,31143916],[105817511,5365378,-41173706],[118859109,482509,22027881],[118296318,-24648468,25642703],[117055386,-35993355,2459373],[101199109,-71060586,36032464],[112495286,-50374830,27711740],[114691358,-21014802,-22432858],[85505565,-90186976,42523524],[65580476,-105861800,49515222],[41716272,-116897428,57744904],[13140325,-122677274,67020044],[-26396798,-124250710,72358766],[-68287342,-117858799,68154710],[-58816308,-23792875,54257083],[-35145103,-35402264,62254290],[-17011449,81149398,-43708921],[57722492,36361430,-62756797],[-14696374,18057230,-84466274],[32209289,71122230,-46683333],[-5500458,81848324,19118340],[107793815,-52476156,-6713408]]},{"denominator":100000000,"name":"NF93_J88_FRAGMENTED_20_1_19_G8","points":[[-136769931,-90880430,44843292],[-140278714,-29361276,-18720335],[-69829155,89110638,-34405083],[-127071010,7102538,-48129048],[-103843451,49297791,-54231085],[-92881145,22822566,-81955880],[-49966301,40565186,-96200134],[-22693303,65136763,42662049],[-31834400,70048573,-78580051],[41405864,85104210,30933161],[57219391,85139872,1814113],[46509889,83140011,-15865578],[1603021,49873688,-79940875],[23139350,66978400,64546521],[74360956,79185266,6834602],[64334711,67857985,50143158],[90868447,62505893,22064528],[101415502,-27079848,-50413751],[104596504,40434672,-17051405],[98943320,46109214,35345214],[82023816,58052177,-38389919],[116520768,18172516,3123213],[86740324,-9587374,-70241301],[112181414,20709243,31489185],[109061391,-551042,-39152173],[119652805,-5027347,21861522],[117940707,-31173360,25234278],[116134265,-43695388,2336442],[98918454,-76136306,35151188],[110962060,-56475101,26634608],[115196954,-29040235,-21868763],[82669730,-93776276,42707129],[62261946,-108209914,50571211],[37583694,-117961235,60165474],[8579758,-123022257,68457733],[-27592995,-123545817,72178697],[-67806701,-117080582,68046065],[-60045933,-23132599,56486332],[-16049482,81235956,-44568366],[60260417,37591768,-61946601],[-15009383,14107785,-87146710],[32047250,71924762,-44088677],[-6536883,81653461,23721106],[108366158,-55142850,-12773654],[-23662385,3361854,62502595],[-81984002,69665717,-60369264],[12871782,31387140,-81838976],[12394017,87038980,409607],[39929513,53998028,-60488050]]}]
PARENT={"denominator":100000000,"name":"J88_FULL_C_G8","points":[[-150604932,-96540423,67441653],[-85283974,-10769301,-53633535],[-66896463,10440997,33896392],[-58177345,26507080,24287123],[-56161233,34237446,-2264123],[-54615858,1152174,-75601477],[-55615371,34325903,-12894710],[-37587176,4263643,-83140263],[-38617951,49519084,5494780],[-30613085,52812896,-24077729],[-21712702,4158264,-87101657],[-10994091,4088623,-88436951],[-15255550,51401298,35888395],[-7844566,75133223,-15437521],[-7596860,78213846,-579936],[-908671,4391220,-88524940],[3544482,70873298,-25633083],[3574151,79421415,15789759],[9179437,1889945,-87518445],[6644599,-36103107,-43424585],[12415650,59703852,-35827871],[18562523,474174,-85488765],[18492532,78037080,35645898],[18860647,50361527,-43167755],[24090429,73458692,40942314],[28806222,45310306,53013369],[33694472,71381314,45128426],[44444247,69577455,48342179],[67790145,63407842,52289026],[76572376,57055041,52862818],[77852657,-21843520,-65607076],[83051714,48846928,52364377],[89499225,39950428,50445216],[91076613,49726445,27669611],[95505252,30851878,47049574],[99521171,14019594,-43579804],[100859283,21749414,42155830],[105594137,25655157,-16197540],[105703315,12472222,35354051],[109365328,4040612,27380073],[112501068,-20285983,-25010949],[113847404,-16778412,-8037284],[112213762,-4118157,17207796],[113766335,-11184540,5394655],[114753942,-10181541,-13334280],[83886242,-28735538,-27558190]]}
EXPECTED_COUNTS={'NF93_J88_BRIDGE_U1_G8': [7, 1, 6], 'NF93_J88_ROBUST_U1_G8': [5, 1, 4], 'NF93_J88_DUAL_U1_G10': [6, 1, 5], 'NF93_J88_CROSSOVER_211_G8': [2, 1, 1], 'NF93_J88_CLEAN_211_G8': [2, 1, 1], 'NF93_J88_BALANCED_211_G8': [2, 1, 1], 'NF93_J88_EXPANDED_211_G8': [2, 1, 1], 'NF93_J88_FRAGMENTED_20_1_19_G8': [20, 1, 19]}
# These 37 compact rows belong to the original 46 J88 rows plus bridge rows46..51.
# Compose the initial 52->50 hull pruning with the final 50->37 hull pruning.
MATERIAL_MAP=[0,1,4,5,6,7,10,14,15,16,17,20,21,22,26,27,28,30,31,32,33,34,35,36,37,38,39,40,41,42,44,46,47,48,49,50,51]
COARSE_COUNTS={
'CROSSOVER':{3:[3,1,2],4:[4,1,3],5:[2,1,1],6:[2,1,1],7:[2,1,1]},
'CLEAN':{3:[6,11,15],4:[4,4,6],5:[3,1,2],6:[2,1,1],7:[2,1,1]},
'BALANCED':{3:[5,1,4],4:[6,1,5],5:[3,1,2],6:[2,1,1],7:[2,1,1]}}
EXPECTED_MANIFEST=(10734, 'db5511156163637eba2aace71283baa758eb98224c47305db74ad25919129e9d')

def dump(name,obj):
 raw=(json.dumps(obj,sort_keys=True,separators=(',',':'))+'\n').encode()
 (ROOT/name).write_bytes(raw)
 return dict(name=name,bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest())

def points(data):
 return [tuple(R(x,data['denominator']) for x in row) for row in data['points']]

def detached(data):
 p=points(data);f=exact_hull(p);r=audit(p,f);root=r['U'][0];D=10**10
 for k in range(2):
  _,g=mass(p,f);si=next(i for i in r['S'] if root in f[i]);a,b,c=[p[j] for j in f[si]]
  n=cross(sub(b,a),sub(c,a));h=dot(n,sub(a,g));foot=add(g,mul(n,h/dot(n,n)))
  w=add(mul(add(foot,p[root]),R(1,2)),mul(sub(foot,g),R(1,1000000)))
  p.append(tuple(R(round(x*D),D) for x in w));f=exact_hull(p);r=audit(p,f)
  assert r['strict']==[2,1,1] and r['weak']==[0,0,0]
 assert all(root not in f[i] for i in r['S'])
 return dict(name='NF93_J88_DETACHED_211_G10',denominator=D,points=[[int(x*D) for x in row] for row in p])

def main():
 global ROOT
 ap=argparse.ArgumentParser();ap.add_argument('--out',default=str(ROOT));a=ap.parse_args();ROOT=Path(a.out);ROOT.mkdir(parents=True,exist_ok=True);manifest=[]
 # The exact selected J88 starting object, not the absent old J85 raw input.
 manifest.append(dump('J88_FULL_C_G8_INPUT.json',PARENT));pp=points(PARENT);ff=exact_hull(pp);pc,co=correct(pp,ff,V0)
 pr=audit(pc,ff);assert len(pr['P'])==1 and not pr['Q'];assert pr['strict']==[1,2,1] and pr['weak']==[0,0,0] and pr['centroid']==['0','0','0']
 manifest.append(dump('NF93_PARENT_C_MASS.json',dict(points=[[str(x) for x in row] for row in pc],faces=ff,report=pr,correction=co)))
 inputs=list(BASE);counts=dict(EXPECTED_COUNTS)
 clean=next(d for d in inputs if d['name']=='NF93_J88_CLEAN_211_G8');inputs.append(detached(clean));counts['NF93_J88_DETACHED_211_G10']=[2,1,1]
 for tag,ks in COARSE_COUNTS.items():
  d=next(d for d in BASE if d['name']=='NF93_J88_'+tag+'_211_G8')
  for k,ct in ks.items():
   name='NF93_J88_'+tag+('_211_G'+str(k) if ct==[2,1,1] else '_ROUND_G'+str(k)+'_CONTROL')
   inputs.append(dict(name=name,denominator=10**k,points=[[round(R(x,d['denominator'])*10**k) for x in row] for row in d['points']]))
   counts[name]=ct
 for d in inputs:
  name=d['name'];manifest.append(dump(name+'_INPUT.json',d));p=points(d);f=exact_hull(p);r=audit(p,f);assert r['strict']==counts[name] and r['weak']==[0,0,0]
  assert len(r['P'])==r['strict'][1]-1 and len(r['Q'])==r['strict'][0]-1 and r['strict'][0]+r['strict'][1]-r['strict'][2]==2
  r.update(name=name,faces=f);manifest.append(dump(name+'_AUDIT.json',r));cc=certify(p,f);manifest.append(dump(name+'_CERT.json',cc))
  if name in ['NF93_J88_CROSSOVER_211_G8','NF93_J88_CLEAN_211_G8','NF93_J88_BALANCED_211_G8']:
   manifest.append(dump(name+'_QTRAP.json',trap(p,f)))
  print(name,r['V'],r['E'],r['F'],r['strict'],r['weak'],'g',r['centroid'],'P',[z['depth'] for z in r['P']],'Q',[z['depth'] for z in r['Q']],flush=True)
 manifest.append(dump('NF93_MATERIAL_MAP.json',dict(compact37_to_original52=MATERIAL_MAP,original40_compact_index=27,initial_pruned_original_rows=[19,45],retired_original_rows=[2,3,8,9,11,12,13,18,19,23,24,25,29,43,45])))
 blob=(json.dumps(manifest,sort_keys=True,separators=(',',':'))+'\n').encode()
 assert (len(blob),hashlib.sha256(blob).hexdigest())==EXPECTED_MANIFEST
 dump('NF93_MANIFEST.json',manifest)
 print('NF93_EXACT_RECOVERY_PASS_WHOLE_P_CANCELLED_NO_110')
if __name__=='__main__':main()
```

### NF93_NUMERICAL.py — complete producing and continuation algorithms

```python
"""NF93 complete compact numerical producing/continuation unit.
CPython3.13.5, numpy2.3.5, scipy1.17.0, torch2.10.0+cpu;
float64, one Torch thread; set OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1.
The floating bars routine retains the historical 1e-14 NOMINATION cutoff.
NF93_EXACT.py separately verifies every positive exact bar without a cutoff.
Exact literal checkpoints, not floating optimizer portability, define the bodies.
"""
import argparse,json,heapq
from pathlib import Path
from fractions import Fraction
import numpy as np,torch
from scipy.spatial import ConvexHull,QhullError
from scipy.optimize import minimize,linprog
ROOT=Path(__file__).resolve().parent/'NF93_NUMERICAL_OUTPUT'
ROOT.mkdir(parents=True,exist_ok=True)
torch.set_default_dtype(torch.float64);torch.set_num_threads(1)
def hull(p):
    h=ConvexHull(p)
    f=h.simplices.copy()
    wrong=np.einsum('ij,ij->i',np.cross(p[f[:,1]]-p[f[:,0]],p[f[:,2]]-p[f[:,0]]),h.equations[:,:3])<0
    f[wrong]=f[wrong][:,[0,2,1]]
    # Canonical indexing, independent of Qhull ordering for ordinary comparisons.
    f=np.array([np.roll(t,-np.argmin(t)) for t in f]);f=f[np.lexsort(f[:,::-1].T)]
    return f


def mass(p,f):
    tr=p[f];D=np.einsum('ij,ij->i',tr[:,0],np.cross(tr[:,1],tr[:,2]));return D.sum()/6,(D[:,None]*tr.sum(axis=1)).sum(axis=0)/(4*D.sum())


def edges(f):
    ed={}
    for i,tri in enumerate(f):
        for a,b in zip(tri,np.roll(tri,-1)):ed.setdefault(tuple(sorted([int(a),int(b)])),[]).append(i)
    assert all(len(v)==2 for v in ed.values())
    return np.array(list(ed),dtype=int),np.array(list(ed.values()),dtype=int)


def bars(p,e,grad=False):
    rad=np.einsum('ij,ij->i',p,p);dv=p[e[:,1]]-p[e[:,0]];dd=np.einsum('ij,ij->i',dv,dv)
    t=np.clip(-np.einsum('ij,ij->i',p[e[:,0]],dv)/dd,0,1)
    foot=p[e[:,0]]+t[:,None]*dv;levels=np.einsum('ij,ij->i',foot,foot)
    par=np.arange(len(p));out=[];gg=[]
    def root(i):
        while i!=par[i]:par[i]=par[par[i]];i=par[i]
        return i
    for k in np.argsort(-levels,kind='stable'):
        a,b=e[k];i,j=root(a),root(b)
        if i==j:continue
        if (rad[i],-i)<(rad[j],-j):i,j=j,i
        depth=1-levels[k]/rad[j]
        if depth>1e-14:
            out.append((float(depth),int(j),[int(a),int(b)]))
            if grad:
                g=np.zeros_like(p);g[j]+=2*levels[k]/rad[j]**2*p[j]
                g[a]-=2*(1-t[k])*foot[k]/rad[j];g[b]-=2*t[k]*foot[k]/rad[j]
                gg.append(g)
        par[j]=i
    return out,gg

def angular_scores(x):
    """Global normalized outgoing chord score and derivative of an active witness."""
    delta=x[None,:,:]-x[:,None,:]
    a=np.linalg.norm(x,axis=1); b=np.linalg.norm(delta,axis=2)
    np.fill_diagonal(b,1.)
    val=np.einsum('ik,ijk->ij',x,delta)/(a[:,None]*b)
    np.fill_diagonal(val,-np.inf)
    j=val.argmax(axis=1); i=np.arange(len(x)); f=val[i,j]; d=delta[i,j]; length=b[i,j]
    G=np.zeros((len(x),len(x),3)); ratio=(a*length)[:,None]
    G[i,i]=(d-x)/ratio-f[:,None]*x/a[:,None]**2+f[:,None]*d/length[:,None]**2
    G[i,j]=x/ratio-f[:,None]*d/length[:,None]**2
    return f,G,j


def report(p):
    f=hull(p);v,g=mass(p,f);p=p-g;e,de=edges(f)
    n=np.cross(p[f[:,1]]-p[f[:,0]],p[f[:,2]]-p[f[:,0]])
    q=n/np.einsum('ij,ij->i',n,p[f[:,0]])[:,None]
    fp,_,_=angular_scores(p);fq,_,_=angular_scores(q)
    P,_=bars(p,e);Q,_=bars(q,de)
    P.sort(reverse=True);Q.sort(reverse=True)
    return dict(V=len(np.unique(f)),E=len(e),F=len(f),volume=float(v),centroid=g.tolist(),
                U=np.where(fp<0)[0].tolist(),S=[f[i].tolist() for i in np.where(fq<0)[0]],
                P=P,Q=Q,minQ=float(np.sort(fq)[1]),minP=float(np.sort(fp)[2]))

def tscore(p):
 d=p[None,:,:]-p[:,None,:];ln=torch.linalg.vector_norm(d,dim=2)
 val=(p[:,None,:]*d).sum(2)/(torch.linalg.vector_norm(p,dim=1)[:,None]*torch.clamp(ln,min=1e-20))
 return (val-torch.eye(len(p))*4).max(1).values

def rooted_tree(p):
    delta=p[None,:,:]-p[:,None,:];ll=np.linalg.norm(delta,axis=2);np.fill_diagonal(ll,1.)
    ss=np.einsum('ik,ijk->ij',p,delta)/(np.linalg.norm(p,axis=1)[:,None]*ll);np.fill_diagonal(ss,-np.inf)
    root=int(np.argmax(np.sum(p*p,axis=1)));width=np.full(len(p),-np.inf);width[root]=np.inf
    heap=[(-np.inf,root)];par={};done=set()
    while heap:
        neg,j=heapq.heappop(heap)
        if j in done:continue
        done.add(j)
        for i in range(len(p)):
            if i in done:continue
            z=min(width[j],ss[i,j])
            if z>width[i]:width[i]=z;par[i]=j;heapq.heappush(heap,(-z,i))
    assert len(par)==len(p)-1
    return np.array(sorted(par.items())),float(width.min())

def tpoints(y,f):
 t=y[f];D=(t[:,0]*torch.linalg.cross(t[:,1],t[:,2])).sum(1);return y-(D[:,None]*t.sum(1)).sum(0)/(4*D.sum())


def tscores(raw,f,e):
 x=tpoints(raw,f);a=x[e[:,0]];d=x[e[:,1]]-a
 return (a*d).sum(1)/(torch.linalg.vector_norm(a,dim=1)*torch.clamp(torch.linalg.vector_norm(d,dim=1),min=1e-20))


def qfields(raw,f):
 x=tpoints(raw,f);t=x[f];n=torch.linalg.cross(t[:,1]-t[:,0],t[:,2]-t[:,0]);h=(n*t[:,0]).sum(1);q=n/h[:,None];ee=torch.linalg.cross(t,torch.roll(t,-1,dims=1));sc=(-(n[:,None,:]*ee).sum(2)/(torch.linalg.vector_norm(n,dim=1)[:,None]*torch.clamp(torch.linalg.vector_norm(ee,dim=2),min=1e-20))).max(1).values
 return sc,q

def polar(raw,f):
 x=tpoints(raw,f);t=x[f];n=torch.linalg.cross(t[:,1]-t[:,0],t[:,2]-t[:,0]);return n/(n*t[:,0]).sum(1)[:,None]

def chain(p,c,n,bend,power,radbend=0):
    a=p[40]-c;b=p[0]-c;ra=np.linalg.norm(a);rb=np.linalg.norm(b);u=a/ra;v=b/rb
    theta=np.arccos(np.clip(u@v,-1,1));normal=np.cross(u,v);normal/=np.linalg.norm(normal)
    t=np.arange(1,n)/n
    tt=t**power
    z=np.sin((1-tt)*theta)[:,None]*u+np.sin(tt*theta)[:,None]*v
    z/=np.sin(theta);z+=bend*np.sin(np.pi*tt)[:,None]*normal;z/=np.linalg.norm(z,axis=1)[:,None]
    radii=ra*np.exp(np.log(rb/ra)*t+radbend*np.sin(np.pi*t))
    added=c+radii[:,None]*z;seq=np.vstack([p[40],added,p[0]])-c
    margin=np.einsum('ij,ij->i',seq[:-1],np.diff(seq,axis=0))
    return np.vstack([p,added]),float(margin.min()),float(theta),float(rb/ra)

def tree_flow(p,steps=150,trust=.03,protectS=False,keep=None,target_margin=1e-5):
 hist=[];p=p-mass(p,hull(p))[1]
 for k in range(steps):
  f=hull(p);p=p-mass(p,f)[1];e,old=rooted_tree(p);tf=torch.tensor(f);te=torch.tensor(e);x=torch.tensor(p);fun=lambda y:tscores(y,tf,te);v=fun(x).numpy();J=torch.func.jacrev(fun,chunk_size=32)(x).numpy().reshape(len(e),-1);M=p.size
  if old>target_margin:hist.append(dict(k=k,targetU1=True,width=old));break
  A=np.c_[-J,np.ones(len(v))];b=v.copy()
  if protectS:
   qfun=lambda y:qfields(y,tf)[0];qsc,q=qfields(x,tf);iq=np.arange(len(f))!=int((q*q).sum(1).argmax());qv=qsc.numpy()[iq];QJ=torch.func.jacrev(qfun,chunk_size=32)(x).numpy().reshape(len(f),-1)[iq];A=np.vstack([A,np.c_[-QJ,np.zeros(len(qv))]]);b=np.r_[b,qv-1e-6]
  opt=linprog(np.r_[np.zeros(M),-1],A_ub=A,b_ub=b,bounds=[(-trust,trust)]*M+[(old,None)],method='highs');accepted=False;out=dict(k=k,width=old,predicted=None if not opt.success else float(opt.x[-1]),lp=bool(opt.success))
  if opt.success:
   for j in range(16):
    alpha=2.**-j;y=p+alpha*opt.x[:-1].reshape(-1,3)
    try:
     ff=hull(y);y-=mass(y,ff)[1];new_e,new=rooted_tree(y)
     if new<=old+1e-9:continue
     rr=report(y)
     if protectS and len(rr['S'])!=1:continue
     p=y;accepted=True;out.update(alpha=alpha,new=new,report=rr,flips=len({tuple(sorted(t)) for t in ff}^{tuple(sorted(t)) for t in f}));break
    except (QhullError,ValueError):continue
  hist.append(out);rr=report(p)
  if keep is not None:(ROOT/keep).write_text(json.dumps(dict(points=p.tolist(),history=hist,report=rr,parameters=dict(steps=steps,trust=trust,protectS=protectS)),sort_keys=True,indent=2)+'\n')
  print('T',k,old,out.get('new'),out.get('alpha'),len(rr['S']),len(rr['U']),rr['P'][:2],rr['Q'][:2],flush=True)
  if accepted:
   if out['alpha']>=.5:trust=min(trust*1.15,.08)
  else:trust*=.5
  if trust<1e-7:break
 return p,hist

def data_fields(p):
 f=hull(p);p=p-mass(p,f)[1];tf=torch.tensor(f);xx=torch.tensor(p);sq,q=qfields(xx,tf);gp=tscore(xx).numpy();q=q.numpy();e,de=edges(f);bs,_=bars(q,de);bs.sort(reverse=True);iq=np.ones(len(f),bool);iq[int(np.sum(q*q,axis=1).argmax())]=False
 if bs:iq[int(bs[0][1])]=False
 ip=np.arange(len(p))!=int(np.sum(p*p,axis=1).argmax());return p,f,iq,ip,sq.numpy(),gp,bs

def minor(p,steps=250,trust=.02,tau=1e-5,keep='MINOR_Q.json',clear=False,p_floor=None):
 p=p[ConvexHull(p).vertices];hist=[]
 for k in range(steps):
  p,f,iq,ip,sq,gp,bs=data_fields(p);tf=torch.tensor(f);x=torch.tensor(p);nv=int(iq.sum());v=np.r_[sq[iq],gp[ip]];nt=len(p)-1;old=float(np.square(np.maximum(tau-sq[iq],0)).sum());M=p.size
  if min(gp[ip])<=0:print('LOST U1',gp[ip].min(),flush=True);break
  if min(sq[iq])>tau*.99:print('S2_TARGET',k,flush=True);break
  fun=lambda y:torch.cat([qfields(y,tf)[0][iq],tscore(tpoints(y,tf))[ip]])
  J=torch.func.jacrev(fun,chunk_size=32)(x).numpy().reshape(len(v),-1)
  # Hinge violations remain explicit; the old point is feasible for this LP.
  A=np.vstack([np.c_[-J[:nv],-np.eye(nv)],np.c_[-J[nv:],np.zeros((nt,nv))]])
  b=np.r_[v[:nv]-tau,(v[nv:]*.95 if p_floor is None else v[nv:]-p_floor)];weights=np.maximum(tau-v[:nv],tau)
  opt=linprog(np.r_[np.zeros(M),weights],A_ub=A,b_ub=b,bounds=[(-trust,trust)]*M+[(0,None)]*nv,method='highs');out=dict(k=k,old=old,trust=trust,lp=bool(opt.success));accepted=False
  if opt.success:
   for j in range(20):
    alpha=2.**-j;y=p+alpha*opt.x[:M].reshape(-1,3)
    try:
     y,ff,jq,jp,qs,ps,bb=data_fields(y);loss=float(np.square(np.maximum(tau-qs[jq],0)).sum())
     if ps[jp].min()<=(1e-10 if p_floor is None else p_floor*.999) or loss>=old-1e-12:continue
     p=y;accepted=True;out.update(alpha=alpha,new=loss,minP=float(ps[jp].min()),minQ=float(qs[jq].min()));break
    except (QhullError,ValueError):continue
  hist.append(out);rr=report(p);(ROOT/keep).write_text(json.dumps(dict(points=p.tolist(),history=hist,report=rr,parameters=dict(steps=steps,initial_trust=.02,tau=tau)),sort_keys=True,indent=2)+'\n')
  print('M',k,old,out.get('new'),out.get('alpha'),'SU',len(rr['S']),len(rr['U']),'Q',rr['Q'][:4],flush=True)
  if accepted:
   if out['alpha']>=.5:trust=min(trust*1.2,.08)
  else:trust*=.5
  if trust<1e-8:break
 return p

def q_cycle(p,steps=60,trust=.012,clear=False,cap=None,target=.02,keep='U1_QFLOW.json',power=2,recharge=False):
 hist=[];p=p[ConvexHull(p).vertices]
 for k in range(steps):
  f=hull(p);p-=mass(p,f)[1];tf=torch.tensor(f);x=torch.tensor(p);q=polar(x,tf).numpy();ed,de=edges(f);bs,_=bars(q,de);bs.sort(reverse=True);old=sum(b[0]**power for b in bs);gp=tscore(x).numpy();ip=np.arange(len(p))!=int(np.sum(p*p,axis=1).argmax());pv=gp[ip];M=p.size
  if not bs:print('S1NUMERIC',flush=True);break
  if not clear and recharge and k>=12 and pv.min()<1e-7:print('RECHARGE_NEEDED',flush=True);break
  if pv.min()<=0:print('LOST_U1',pv.min(),flush=True);break
  if clear and pv.min()>=target:print('CLEAR_TARGET',pv.min(),flush=True);break
  def objective(y):
   q=polar(y,tf);loss=torch.tensor(0.)
   for dep,r,(a,b) in bs:
    d=q[b]-q[a];t=torch.clamp(-(q[a]*d).sum()/(d*d).sum(),0,1);foot=q[a]+t*d;dd=torch.clamp(1-(foot*foot).sum()/(q[r]*q[r]).sum(),min=0);loss+=(dd*dd if power==2 else dd)
   return loss
  pf=lambda y:tscore(tpoints(y,tf))[ip];PJ=torch.func.jacrev(pf,chunk_size=32)(x).numpy().reshape(len(pv),-1);grad=torch.func.jacrev(objective)(x).numpy().ravel()
  if clear:
   if cap is None:cap=old*1.01+.0001
   A=np.vstack([np.c_[-PJ,np.ones(len(pv))],np.r_[grad,0.][None,:]]);b=np.r_[pv,cap-old];c=np.r_[np.zeros(M),-1.];bounds=[(-trust,trust)]*M+[(float(pv.min()),None)]
  else:A=-PJ;b=pv-np.minimum(pv*.05,1e-5);c=grad;bounds=[(-trust,trust)]*M
  opt=linprog(c,A_ub=A,b_ub=b,bounds=bounds,method='highs');out=dict(k=k,clear=clear,old=old,minP=float(pv.min()),trust=trust,lp=bool(opt.success),cap=cap);accepted=False
  if opt.success:
   for j in range(18):
    alpha=2.**-j;y=p+alpha*opt.x[:M].reshape(-1,3)
    try:
     ff=hull(y);y-=mass(y,ff)[1];rr=report(y);newgp=tscore(torch.tensor(y)).numpy();nr=int(np.sum(y*y,axis=1).argmax());mar=float(newgp[np.arange(len(y))!=nr].min());loss=sum(b[0]**power for b in rr['Q'])
     if len(rr['U'])!=1 or rr['P'] or mar<=1e-9:continue
     if clear:
      if loss>cap or mar<=pv.min()+1e-9:continue
     elif loss>=old-1e-10:continue
     p=y;accepted=True;out.update(alpha=alpha,new=loss,newmargin=mar,report=rr);break
    except (QhullError,ValueError):continue
  hist.append(out);rr=report(p);(ROOT/keep).write_text(json.dumps(dict(points=p.tolist(),history=hist,report=rr,parameters=dict(steps=steps,clear=clear,cap=cap,target=target)),sort_keys=True,indent=2)+'\n');print('CQ',k,clear,old,out.get('new'),pv.min(),out.get('newmargin'),out.get('alpha'),'SU',len(rr['S']),len(rr['U']),'Q',rr['Q'][:3],flush=True)
  if accepted:
   if out['alpha']>=.5:trust=min(trust*1.1,.04)
  else:trust*=.5
  if trust<1e-8:break
 return p

def mat(z):return torch.stack([torch.stack([z[0],z[2],z[3]]),torch.stack([z[2],z[1],z[4]]),torch.stack([z[3],z[4],3-z[0]-z[1]])])


def metric_scores(p,G):
 d=p[None,:,:]-p[:,None,:];a=torch.einsum('ni,ij,nj->n',p,G,p);b=torch.einsum('nmi,ij,nmj->nm',d,G,d);v=torch.einsum('ni,ij,nmj->nm',p,G,d)/(torch.sqrt(torch.clamp(a,min=1e-30))[:,None]*torch.sqrt(torch.clamp(b,min=1e-30)));return (v-torch.eye(len(p))*4).max(1).values

def metric_search(src='NF93_J88_CROSSOVER_211_G8_INPUT.json',starts=12,out='METRIC_BAR.json'):
 d=json.load(open(ROOT/src));p=np.array(d['points'],float)/d.get('denominator',1);p-=mass(p,hull(p))[1];q=polar(torch.tensor(p),torch.tensor(hull(p)));p=torch.tensor(p);ip=np.arange(len(p))!=int((p*p).sum(1).argmax());tau=1e-5
 def guards(z):
  G=mat(z);return torch.cat([metric_scores(p,G)[ip]-tau,torch.linalg.eigvalsh(G)-1e-5])
 ed,de=edges(hull(p.numpy()))
 def objective(z):
  G=mat(z);H=torch.linalg.inv(G);L=torch.linalg.cholesky(H);qq=q@L;bs,_=bars(qq.detach().numpy(),de);loss=torch.tensor(0.)
  for olddep,r,(a,b) in bs:
   d=q[b]-q[a];t=torch.clamp(-(q[a]@H@d)/(d@H@d),0,1);ft=q[a]+t*d;dep=torch.clamp(1-(ft@H@ft)/(q[r]@H@q[r]),min=0);loss+=dep*dep
  return loss
 def ev(z):
  x=torch.tensor(z,requires_grad=True);v=objective(x);v.backward();return float(v.detach()),x.grad.numpy()
 def gv(z):return guards(torch.tensor(z)).numpy()
 def gj(z):return torch.func.jacrev(guards)(torch.tensor(z)).numpy()
 rng=np.random.default_rng(93302);hist=[];initial=np.array([1.,1.,0,0,0]);seeds=[initial]
 for _ in range(5000):
  z=initial+rng.normal(0,[.12,.12,.12,.12,.12])
  if gv(z).min()>0:seeds.append(z)
  if len(seeds)>=starts:break
 for k,z0 in enumerate(seeds):
  opt=minimize(ev,z0,jac=True,method='SLSQP',constraints=[{'type':'ineq','fun':gv,'jac':gj}],bounds=[(.0001,2.9999)]*2+[(-1.4999,1.4999)]*3,options=dict(maxiter=600,ftol=1e-14));G=mat(torch.tensor(opt.x)).numpy()
  try:A=np.linalg.cholesky(G).T;P=p.numpy()@A.T;rr=report(P)
  except Exception:continue
  item=dict(k=k,z=opt.x.tolist(),fun=float(opt.fun),min_guard=float(gv(opt.x).min()),SU=[len(rr['S']),len(rr['U'])],report=rr,success=bool(opt.success));hist.append(item);print('MBAR',k,item['fun'],item['min_guard'],item['SU'],G.tolist(),flush=True)
  (ROOT/out).write_text(json.dumps(dict(points=P.tolist(),G=G.tolist(),history=hist,source=src,seed=93302,tau=tau),sort_keys=True,indent=2)+'\n')
  if item['SU']==[1,1]:print('NOMINATED110',flush=True);break

def addfaces(p,count=32,height=1e-4):
 history=[]
 for k in range(count):
  f=hull(p);p-=mass(p,f)[1];t=p[f];n=np.cross(t[:,1]-t[:,0],t[:,2]-t[:,0]);area=np.linalg.norm(n,axis=1);order=np.argsort(-area)
  for i in order:
   c=t[i].mean(0);w=c+height*n[i]/area[i];q=np.vstack([p,w]);ff=hull(q)
   if len(np.unique(ff))!=len(q):continue
   rr=report(q)
   if len(rr['U'])==1 and not rr['P']:
    history.append(dict(face=f[i].tolist(),point=w.tolist(),report=rr));p=q;break
  else:break
 return p,history


def pscores(raw,f,e):
 q=polar(raw,f);a=q[e[:,0]];d=q[e[:,1]]-a
 return (a*d).sum(1)/(torch.linalg.vector_norm(a,dim=1)*torch.clamp(torch.linalg.vector_norm(d,dim=1),min=1e-20))


def dual_flow(p,steps=200,trust=.02,keep='DUAL_TREE.json',mode='min',target=None):
 p=p-mass(p,hull(p))[1];hist=[]
 for k in range(steps):
  f=hull(p);p=p-mass(p,f)[1];tf=torch.tensor(f);x=torch.tensor(p);q=polar(x,tf).numpy();e,old=rooted_tree(q);te=torch.tensor(e);fun=lambda y:pscores(y,tf,te);v=fun(x).numpy();J=torch.func.jacrev(fun,chunk_size=32)(x).numpy().reshape(len(e),-1);M=p.size
  gp=tscore(x).numpy();rp=int(np.sum(p*p,axis=1).argmax());ip=np.arange(len(p))!=rp;pv=gp[ip];pfun=lambda y:tscore(tpoints(y,tf));PJ=torch.func.jacrev(pfun,chunk_size=32)(x).numpy().reshape(len(p),-1)[ip]
  if old>1e-5:hist.append(dict(k=k,targetS1=True,width=old));break
  if pv.min()<=0:print('LOST U1',pv.min(),flush=True);break
  A=np.c_[-J,np.ones(len(v))];b=v.copy();A=np.vstack([A,np.c_[-PJ,np.zeros(len(pv))]]);b=np.r_[b,pv*.95]
  opt=linprog(np.r_[np.zeros(M),-1.],A_ub=A,b_ub=b,bounds=[(-trust,trust)]*M+[(old,None)],method='highs');accepted=False;out=dict(k=k,width=old,predicted=None if not opt.success else float(opt.x[-1]),lp=bool(opt.success),trust=trust)
  if opt.success:
   for j in range(18):
    alpha=2.**-j;y=p+alpha*opt.x[:-1].reshape(-1,3)
    try:
     ff=hull(y);y-=mass(y,ff)[1];newq=polar(torch.tensor(y),torch.tensor(ff)).numpy();new_e,new=rooted_tree(newq)
     if new<=old+1e-10:continue
     newgp=tscore(torch.tensor(y)).numpy();nr=int(np.sum(y*y,axis=1).argmax())
     if np.min(newgp[np.arange(len(y))!=nr])<=1e-10:continue
     rr=report(y);p=y;accepted=True;out.update(alpha=alpha,new=new,report=rr,flips=len({tuple(sorted(t)) for t in ff}^{tuple(sorted(t)) for t in f}));break
    except (QhullError,ValueError):continue
  hist.append(out);rr=report(p)
  (ROOT/keep).write_text(json.dumps(dict(points=p.tolist(),history=hist,report=rr,parameters=dict(steps=steps,trust=trust)),sort_keys=True,indent=2)+'\n')
  print('D',k,old,out.get('new'),out.get('alpha'),'SU',len(rr['S']),len(rr['U']),'Q',rr['Q'][:3],flush=True)
  if accepted:
   if out['alpha']>=.5:trust=min(trust*1.1,.06)
  else:trust*=.5
  if trust<1e-8:break
 return p,hist


def load(src):
 path=Path(src)
 if not path.exists():path=ROOT/path
 d=json.loads(path.read_text())
 return np.array([[float(Fraction(x)) for x in row] for row in d['points']])/d.get('denominator',1)

def save(name,p,**kw):
 (ROOT/name).write_text(json.dumps(dict(points=p.tolist(),**kw),sort_keys=True,indent=2)+'\n')

def freeze(name,p,power=8):
 import NF93_EXACT as E
 ac=ConvexHull(p).vertices;rows=np.rint(p[ac]*10**power).astype(np.int64).tolist()
 d=dict(name=name,denominator=10**power,points=rows)
 raw=(json.dumps(d,sort_keys=True,separators=(',',':'))+'\n').encode();(ROOT/(name+'_INPUT.json')).write_bytes(raw)
 pp=E.points(d);ff=E.exact_hull(pp);rr=E.audit(pp,ff)
 import hashlib
 print('FROZEN_EXACT',name,len(raw),hashlib.sha256(raw).hexdigest(),rr['V'],rr['E'],rr['F'],rr['strict'],rr['weak'],flush=True)
 return d

def alternating(p,rounds,prefix,power=1,desc_steps=32,clear_steps=20,recharge=True):
 hist=[]
 for j in range(rounds):
  old=sum(b[0]**power for b in report(p)['Q'])
  p=q_cycle(p.copy(),desc_steps,.012,False,None,.02,f'{prefix}_{j:02}_DESC.json',power,recharge)
  loss=sum(b[0]**power for b in report(p)['Q'])
  p=q_cycle(p.copy(),clear_steps,.008,True,loss*1.003+.00001,.02,f'{prefix}_{j:02}_CLEAR.json',power,recharge)
  rr=report(p);hist.append(dict(j=j,old=old,desc_loss=loss,clear_loss=sum(b[0]**power for b in rr['Q']),report=rr))
  save(prefix+'_FINAL.json',p,history=hist)
  if len(rr['S'])==1:break
 return p

def recipe(stage,exact_dir):
 # Every selected prefix corresponds to actually completed saved iterations.
 # Running later stages uses exact checkpoints rather than unstored earlier floats
 # wherever the original producing route did so.
 E=Path(exact_dir).resolve()
 if stage=='bridge':
  p=load(E/'NF93_PARENT_C_MASS.json');p,mar,phi,ratio=chain(p,mass(p,hull(p))[1],7,0,1,0)
  active=ConvexHull(p).vertices;p=p[active]
  save('BRIDGE_START.json',p,initial_active=active.tolist(),reference_margin=mar,angle=phi,ratio=ratio)
  p,h=tree_flow(p,180,.03,False,'BASIN_SHORT7.json');freeze('NF93_J88_BRIDGE_U1_G8',p)
 elif stage=='dual':
  p=load('BASIN_SHORT7.json');p=p[ConvexHull(p).vertices];p,h=dual_flow(p,160,.02,'DUAL_SHORT7.json');freeze('NF93_J88_DUAL_U1_G10',p,10)
 elif stage=='crossover':
  p=load(E/'NF93_J88_BRIDGE_U1_G8_INPUT.json');p,h=tree_flow(p,220,.03,False,'ROBUST_U1_A.json',.12)
  freeze('NF93_J88_ROBUST_U1_G8',p)
  # This phase used the numerical robust result, not its separately rounded copy.
  p=minor(p,160,.02,1e-5,'MINOR_ROBUST7.json');freeze('NF93_J88_CROSSOVER_211_G8',p)
 elif stage=='descent':
  metric_search(str(E/'NF93_J88_CROSSOVER_211_G8_INPUT.json'),12,'METRIC_BAR.json')
  p=load('METRIC_BAR.json');p=q_cycle(p,100,.012,True,.56,.02,'CLEAR_METRIC_A.json',2,False)
  p=alternating(p,7,'POWER2',2,50,25,False)
  p=alternating(p,12,'L1_MORE',1,32,20,True);save('L1_MORE_SAVED.json',p)
  clean=minor(p.copy(),140,.02,1e-5,'MINOR_L1_MORE.json');freeze('NF93_J88_CLEAN_211_G8',clean)
  strong=q_cycle(p.copy(),100,.012,True,.592,.025,'CLEAR_L1_STRONG.json',1,True)
  balanced=minor(strong,100,.02,1e-5,'MINOR_STRONG_FLOOR.json',p_floor=.003);freeze('NF93_J88_BALANCED_211_G8',balanced)
 elif stage=='expanded':
  p=load(E/'NF93_J88_BALANCED_211_G8_INPUT.json');p,h=addfaces(p,32,1e-4);save('ADDFACES32.json',p,history=h)
  p=alternating(p,13,'BIG_L1',1,32,20,True)
  p=minor(p,180,.02,1e-5,'BIG_MINOR_A.json',p_floor=.0001);freeze('NF93_J88_EXPANDED_211_G8',p)
 elif stage=='fragmented':
  p=load(E/'NF93_J88_EXPANDED_211_G8_INPUT.json');p,h=addfaces(p,38,1e-4);save('ADDFACES38_B.json',p,history=h)
  p=alternating(p,11,'BIG2_L1',1,32,20,True);p=alternating(p,14,'BIG2_CONT',1,32,20,True)
  p=minor(p,180,.02,1e-5,'BIG2_MINOR_A.json',p_floor=.0001);freeze('NF93_J88_FRAGMENTED_20_1_19_G8',p)
 else:raise ValueError(stage)

if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('stage',choices=['bridge','dual','crossover','descent','expanded','fragmented']);ap.add_argument('--exact-dir',default=str(Path(__file__).resolve().parent/'NF93_EXACT_OUTPUT'));a=ap.parse_args();recipe(a.stage,a.exact_dir)
```

Readable copies and generated audit data are also available in [the recovery bundle](sandbox:/mnt/data/NF93_J88_RECOVERY.zip) and [the Markdown handoff](sandbox:/mnt/data/NF93_RESULT.md). These supplement the complete literal recovery units above.
