# figure-0530

Historical AI scientific report · saved 2026-09-24 UTC. Claims below retain their original status and have not all been independently checked. The current retained construction is C622; the C<500 search remains open.

Public text derivative: internal-record-identifiers-replaced.

---

# RN45 — executed RN44 mass envelopes, complete exact controls, and the required material release

## Result

**No own-centroid strict110 body is established.** The main advance is that the previously pending RN44 tests were executed successfully: five changed uniformly filled bodies received complete exact audits, and both proposed nested-mass obstructions passed.

The resulting obstruction is substantially stronger than fixed-complement cap-cover=2. For every uniformly filled convex polyhedron K satisfying

```
RN44_INNER ⊆ K ⊆ RN44_OUTER,
```

and every symmetric Gram matrix G with entrywise `|G-I|≤1/1024`, K has **at least two strict stable and two strict unstable equilibria at its own centroid**. At the Euclidean metric, the stable lower bound strengthens to three. Arbitrary additional cuts, intermediate material, topology changes and other root changes inside this envelope do not repair the body. The theorem does not impose an edge bound, so increasing resolution inside this particular envelope cannot solve the problem either.

A second, broader statement proves S≥2 throughout

```
CORE33 ⊆ K ⊆ BROAD,
|G-I|entrywise ≤ 1/1024.
```

This identifies actual retained triangles, not source names, that must be released. I also derive an unbounded-cone metric obstruction from the two opposite coordinate corners of RN36. It explains why restoring the discarded old apex while retaining the opposite corner is not an adequate mass repair.

The exact five-body replay is complete. Later numerical release attempts did not produce an accepted exact successor. Their available rational construction data and the most useful next material-release recipe are preserved below, with their incomplete mechanical verification clearly separated from the five audited controls.

## 1. Source identity and observed execution

The complete latest journal was read consecutively through its1045 lines, including common memory, branch memory and the literal RN44 parent. The unchanged RN30/RN36 literal parent was retained from the preceding continuation. The latest journal is169910 bytes, SHA256 `37abdff7813ad1d2b70c7c05938ce319e1d8e0610d3ee593c43c856dde27e590`.

The two source authorities are:

- `figure-0519`, advertised SHA256 `0949d6226b6c7e5bc6b8faade6bc3152fa888d44d07ed1cf4620b79ccab87bdc`;
- `figure-0526`, advertised SHA256 `ebc5d7126be28e7147420bef998a71c2b19848885d35f34ee946f498a3995018`.

The first supplies the complete46-unit RN30 recovery, including `exact.py`, `verify_new.py` and the exact RN36 input. The second supplies the complete `RN44_PATCH.py`. No H49, canonical-C622, research connector or historical scratch file was used as an exact dependency.

The decoded RN30 dictionary matched207257 bytes and SHA256 `223ee37c0175e1ea17f27f8a9505be12986827cf2a85571751c3a3577099d8b6`. The reconstructed RN36 input matched2664 bytes and SHA256 `7025e2ba2706047c05ec27dc2ef6ccedf57f67244c5f668ff6feaa01878b9ecd`. Its fresh full audit matched65880 bytes and SHA256 `46b4dda3151d5e6c2be950d4d129a6e6df9c1d731142af1c2b7cfc747f588aa5`.

An initial combined run was interrupted by a shell timeout. A subsequent complete RN44 run finished, and its output was inspected. The interrupted prefix is not counted as an independent verification. Observed terminal lines were:

```
RN44_PARENT_HASH_PASS
RN44_COVER_EXACTLY_TWO_PASS
RN44_FULL_AUDIT RN44_CORE33 33 93 62 [18,8,24] [0,0,0] 7 17
RN44_FULL_AUDIT RN44_INNER 67 139 74 [13,14,25] [0,0,0] 13 12
RN44_FULL_AUDIT RN44_OUTER 62 135 75 [12,12,22] [0,0,0] 11 11
RN44_FULL_AUDIT RN44_MID 70 143 75 [12,13,23] [0,0,0] 12 11
RN44_FULL_AUDIT RN44_BROAD 62 137 77 [13,10,21] [0,0,0] 9 12
RN44_U_ENVELOPE_PASS 0
RN44_U_ENVELOPE_PASS 1/4096
RN44_U_ENVELOPE_PASS 1/1024
RN44_U_ENVELOPE_PASS 1/256
RN44_S_ENVELOPE_PASS RN44_OUTER 0 [3,9,43]
RN44_S_ENVELOPE_PASS RN44_BROAD 0 [3,9]
RN44_S_ENVELOPE_PASS RN44_BROAD 1/1024 [3,9]
RN44_PATCH_REPLAY_COMPLETE 5 19
```

These are newly observed consequences of the previously supplied pending source, not inherited claims that the parent had already executed them.

## 2. Exact constructions and complete mechanical census

Let P be the literal RN36 body. Its canonical exposed vertices are the following integer triples divided by1000:

```json
[[-1517,623,-1146],[-554,-83,94],[-426,-330,-55],[-370,26,323],[-351,-294,253],[-317,469,30],[-309,-387,-20],[-251,-284,-416],[-189,-355,492],[-169,-405,-266],[-143,-2,-604],[-130,-441,93],[-75,253,530],[-42,373,-282],[-8,-429,-5],[48,-412,-28],[59,436,123],[67,185,-363],[83,405,266],[89,426,21],[130,347,445],[132,414,74],[144,415,27],[176,-361,-60],[178,390,-23],[195,350,-83],[196,316,339],[216,368,-16],[223,363,47],[253,312,141],[272,194,-219],[275,-199,-286],[275,304,-80],[280,260,-135],[311,235,-139],[315,238,-129],[366,104,-186],[462,-75,-153],[590,-69,160],[667,-634,1676]]
```

Set

```
X = [8,20,31,36,37,38,39]
Y = {0,...,39} minus X
n1 = (1000,-273,-348)
n2 = (1000,-611,986)
L1 = 295433/1000       R1 = 402336/1000
L2 = 337411/1000       R2 = 356753/1000
K(h1,h2) = P ∩ {n1·x≤h1} ∩ {n2·x≤h2}.
```

The five exact bodies are

```
CORE33 = conv({v_i : i in Y})
INNER  = K(L1,L2)
OUTER  = K(R1,R2)
MID    = K(697769/2000,173541/500)
BROAD  = P ∩ {n2·x≤500}.
```

The first cut used to construct BROAD in the executable is explicitly redundant: its offset is `max_P(n1·x)+1`.

| Body | V/E/F | Strict S/U/H | Additional weak | Positive P/Q bars |
|---|---:|---:|---:|---:|
| CORE33 |33/93/62|18/8/24|0/0/0|7/17|
| INNER |67/139/74|13/14/25|0/0/0|13/12|
| OUTER |62/135/75|12/12/22|0/0/0|11/11|
| MID |70/143/75|12/13/23|0/0/0|12/11|
| BROAD |62/137/77|13/10/21|0/0/0|9/12|

Every body has zero primitive equalities on both sides and no boundary face foot. Thus the controls do not hide weak residues. Every body is within the required edge budget, but none has the desired mechanics.

The five complete physical/polar landscapes contain **52 positive P bars and63 positive Q bars:115 total**. All are retained, with exact rational births/deaths, full components, all cut edges and attaining paths. The corresponding full-chord checks cover8936 physical and13068 polar unordered pairs. No numerical positivity cutoff is used in these exact reports.

For orientation only, the largest birth-relative squared-radius depths are:

| Body | Largest P depth | Largest Q depth |
|---|---:|---:|
| CORE33 |0.6992758763301256|0.2287994186638903|
| INNER |0.6710472096388512|0.21704298858179655|
| OUTER |0.6770404642920566|0.24848180213382848|
| MID |0.6739445817151182|0.2362095117430148|
| BROAD |0.6834036108057880|0.2245429704938788|

These selected depths do not replace the115 complete bar records reconstructed by the capsule.

### Actual mass

All masses were integrated for the new filled bodies. CORE33 has exact volume

```
135346477/240000000.
```

Representative numerical displays of the exact audit values are:

```
CORE33 centroid ≈ (-0.3495306030, 0.1225589460,-0.2105023926)
INNER  volume   ≈ 0.603567314699
INNER  centroid ≈ (-0.3285293067, 0.1088450671,-0.1897395930)
OUTER  volume   ≈ 0.623887324713
OUTER  centroid ≈ (-0.3112691558, 0.1034104214,-0.1842340751)
MID    volume   ≈ 0.615112197690
MID    centroid ≈ (-0.3186970007, 0.1057999880,-0.1868891301)
BROAD  centroid ≈ (-0.2754081419, 0.0880602397,-0.1494204253).
```

The recovery writes the unreduced-output rational `volume`, all three `moment` entries and `centroid` entries for each body. It also writes every rational vertex, maximal supporting plane, oriented maximal facet cycle and true edge with both owners. The small defining cuts and literal P above are complete recovery data for these large rational outputs; no lost floating checkpoint is needed.

The audits use the inherited exact maximal-hull implementation, actual mass-origin/divergence crosschecks, and a separate support-foot mechanics calculation with an additional mass decomposition. These are two mechanics calculations on shared certified incidences, **not two independent hull engines**.

## 3. Executed unstable-equilibrium envelope

Write W=INNER and O=OUTER. The retained physical points are

```
v0  = (-1517,623,-1146)/1000
v10 = (-143,-2,-604)/1000.
```

For either retained v and every other vertex w of O, put d=w-v and

```
ell(x) = (v-x)·d.
```

For every uniformly filled W⊆K⊆O,

```
V(K) ell(c_K)
≤ V(W) ell(c_W)
  + (V(O)-V(W)) max(0,max_O ell).
```

Strict negativity for all these directions proves that v is a strict U vertex of every such K. This tests all outer directions, so it is not conditional on retaining a particular neighbor graph.

For a Gram box, replace the fixed-inner contribution by

```
tr(A)+epsilon Σ|A_ij|,
A = V(W) sym((v-c_W)dᵀ),
```

and bound the variable material by the maximum over outer vertices of the analogous expression, also compared with zero. The trace-plus-absolute-value expression is convex in x, so its maximum over O is bounded by its vertex maximum. The condition `3epsilon<1` guarantees positive definiteness throughout the entrywise box.

All122 inequalities passed at each of epsilon=0,1/4096,1/1024 and1/256. At epsilon=1/256, the largest exact rational upper bounds have numerical displays approximately

```
v0 : -1.476450701934273
v10: -0.0005022583845498213.
```

Therefore:

**For every uniformly filled convex polyhedron INNER⊆K⊆OUTER and every symmetric G with entrywise |G-I|≤1/256, both old v0 and old v10 are strict unstable equilibria at the actual affine centroid.**

No restriction on other equilibria, additional weak states, edge count or intermediate topology is required. This does not exclude material outside OUTER, removal of material from INNER, different outer cuts, or unrestricted metrics.

## 4. Executed stable-material envelopes

The certified retained triangles, in the RN36 canonical vertex numbering, are

```
parent face3  = [0,3,12]
parent face9  = [0,9,2]
parent face43 = [0,10,7].
```

They are maximal triangles of P. Containment of their vertices in a convex K⊆P retains the entire triangles as the same maximal facets; merely changing labels does not remove them.

For one outward triangle normal n, an oriented edge beginning at a with direction e, and t=n×e, the Euclidean foot condition is

```
t·(c-a)>0.
```

For a Gram matrix G, put J=adj(G). Clearing the positive denominator gives

```
(nᵀJn)t·(c-a) + (h-n·c)tᵀJn > 0.
```

This is affine in the centre. The source integrates its coefficient matrix over the fixed inner body and bounds the remaining material by the minimum over outer vertices. The bound `|adj(G)-I|entrywise≤2epsilon+2epsilon²` handles the whole metric box. Three positive oriented-edge bounds prove a strict interior face foot.

Executed consequences are:

```
CORE33⊆K⊆OUTER, G=I:
    faces3,9,43 are strict S; hence S≥3.

CORE33⊆K⊆BROAD, G=I:
    faces3,9 are strict S; hence S≥2.

CORE33⊆K⊆BROAD, |G-I|entrywise≤1/1024:
    faces3,9 are strict S; hence S≥2.
```

Since CORE33⊆INNER and OUTER⊆BROAD, these combine with the unstable-envelope theorem. In particular the entire closed two-offset rectangle, and every arbitrary uniformly filled intermediate body between its INNER and OUTER extremes, is excluded from110 in the stated metric neighborhood.

This is not an exclusion of general multi-cap surgery. It says that changing cap directions while still retaining CORE33 and remaining inside BROAD cannot restore S1 near the identity metric. The actual retained material or the outer envelope must change.

## 5. A further exact geometric obstruction: opposite coordinate corners

The literal RN36 body lies in the box

```
B = [-1517/1000,667/1000]
  × [-634/1000,623/1000]
  × [-1146/1000,1676/1000].
```

Its two U vertices v0 and v39 are opposite corners of this box. Relative to v0, every other original vertex has component signs(+,-,+); relative to v39 the signs are(-,+,-). The minimum positive component gaps are respectively

```
v0 : (963,154,542)/1000
v39: (77,193,1146)/1000.
```

Let S=diag(1,-1,1). For any full-dimensional convex body L⊆B retaining v0, every interior centre c has S(c-v0) strictly positive componentwise, and S(x-v0) is nonnegative and nonzero for every x≠v0 in L. Consequently

```
(v0-c)ᵀG(x-v0)<0
```

whenever G is positive definite and SGS is entrywise nonnegative. The same proof applies to v39, using -S. Thus:

**Every full-dimensional convex body inside B retaining both v0 and v39 has at least two strict U equilibria at every interior reference centre for every positive-definite metric with G12≤0, G13≥0 and G23≤0.**

This includes the entire positive diagonal metric cone, not merely a small neighborhood of I. It is an elementary geometric proof from the literal coordinates, independent of a numerical optimizer or a centroid approximation. It is not a full-SPD exclusion.

The constructive implication is specific. RN44 has removed v39 but retained v0. Restoring the full old corner v39 as ballast, while retaining v0 and staying inside B, necessarily restores a second U throughout this metric cone. A mass repair outside BROAD need not restore that corner, and material outside B or a metric outside the cone is not covered.

## 6. Finite release attempts and the next construction chart

After the envelope calculation, numerical work tried actual removal of old v0, including a third cap on MID and free-coordinate/support motion from deletion starts. No exact110 endpoint was obtained. The selected third-cap nomination is recoverable without its search history:

```
RN45_THIRD_CAP = MID ∩ {(-577,332,-746)·x≤1345075521/1000000}.
```

This is a genuine material-envelope exit. At old v0 the new inequality is violated by exactly

```
591985479/1000000 > 0.
```

On Y minus{0}, its maximum is `532431/1000`, attained at old v10, so all32 other complementary vertices are retained. The complete old P7 packet remains absent because the body is a subset of MID. The four retained vertices[9,14,23,26] have nonzero affine determinant `44308759/1000000000`, proving full dimensionality. MID has75 maximal facets, so this one additional cut gives F≤76 and E≤222.

Its saved numerical nomination was V86/E160/F76 with S12/U13. **That is not an accepted exact mechanical class or a weak certificate.** Its exact audit is an optional recovery operation below, with no asserted output class or hash.

Deleting v0 also destroys the desired old stable triangle3. A more targeted finite next chart follows directly from the executed certificates:

```
RN45_RELEASE_9_10
= conv(vertices(MID) minus {old v9,old v10}).
```

This removes actual material from both certified inner envelopes. It destroys the extra retained stable triangle9 through removal of v9, destroys triangle43 and the protected additional U through removal of v10, while retaining the original triangle3 and corner v0. The original triangle3 remains a maximal facet, although its stability must be checked at the new actual centroid. Corner v0 remains strict U at every interior centre in the sign-compatible metric cone proved above.

Every remaining old MID vertex stays extreme under deletion of other vertices, so this body has exactly68 vertices and hence E≤198. It is full-dimensional, for example using retained vertices[2,14,23,26]. It is not an accepted mechanical endpoint: no complete new census is claimed for it. The recovery unit gives its exact generator and full audit call rather than treating release of the named obstructions as feasibility.

The other numerical coordinate/H-space endpoints were not preserved as readable exact checkpoints in the retained runtime. They are not promoted as durable successors, and their failures are not used as family exclusions. Later recovery/optimization calls without inspectable terminal returns likewise contribute no new exact class or PASS claim here.

The most useful continuation is therefore not another fixed two-offset scan. It is coordinated surgery on the real material supporting faces9/43 and U10, retaining triangle3 only when its actual mass remains compatible, or a deliberate addition outside BROAD that does not simply restore the opposite coordinate corner. Both complete landscapes must be recomputed after that release.

## 7. Recovery capsule and complete observed receipt bank

The source below is a **complete new replay patch to the two supplied literal parents**. It reconstructs their source units from their literal payloads, not from an old runtime directory. Both parent payloads must remain with this handoff. No additional archive source is required.

Save it as `RN45_REPLAY.py`. The two supplied journal files may be used directly as its parent-payload arguments:

```sh
python -B -S RN45_REPLAY.py \
  'research-journal(20260923-204034).md' \
  'research-journal(20260923-233310).md' \
  rn45_recovered
```

The first file contains the RN30 literal capsule; the second contains RN44. The decoder selects the exact inner dictionary by its complete SHA256, so other encoded payloads in a journal are not silently substituted.

The default operation reruns the executed RN44 source and compares all19 recorded receipts below. The additional wrapper comparison marker is an expected convenience marker, not a claimed second independent cold execution. The observed scientific terminal marker is the `RN44_PATCH_REPLAY_COMPLETE 5 19` run recorded above.

Optional exact audits of the two material-release constructions are requested explicitly:

```sh
python -B -S RN45_REPLAY.py \
  'research-journal(20260923-204034).md' \
  'research-journal(20260923-233310).md' \
  rn45_recovered --release
```

These optional outputs have no predeclared mechanical classes. The script prints their actual exact census and writes all maximal incidences, moments, mixed weak tests and complete P/Q landscapes. They are not included in the19 already observed receipts.

Exact dependency environment: CPython3.13.5 standard library, `C92_GMP=0`. The earlier numerical nominations used NumPy2.3.5, SciPy1.17.0 and Torch2.10.0+cpu, float64, one thread; they are not needed for this exact recovery.

```python
# RN45_REPLAY.py
# Complete replay patch to supplied literal parents:
# figure-0519
# 0949d6226b6c7e5bc6b8faade6bc3152fa888d44d07ed1cf4620b79ccab87bdc
# figure-0526
# ebc5d7126be28e7147420bef998a71c2b19848885d35f34ee946f498a3995018
import os
os.environ['C92_GMP'] = '0'
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[key] = '1'
import sys
import json
import base64
import lzma
import hashlib
import subprocess
from pathlib import Path
from fractions import Fraction as F
from functools import reduce
from itertools import combinations
from math import gcd, lcm

RAW_SHA = '223ee37c0175e1ea17f27f8a9505be12986827cf2a85571751c3a3577099d8b6'
XZ_SHA = '61a4fc21d9a8b7deb6c0f56809f1b0b563efd7182ba029be08301bb33aeb877c'
EXPECTED = {
 'RN36_RES02_G1000_audit.json': [65880,'46b4dda3151d5e6c2be950d4d129a6e6df9c1d731142af1c2b7cfc747f588aa5'],
 'RN44_CORE33.json': [1570,'ce0fe8bbbe55f36b5484e95a790e81fb9bb9ac4212c7d98e9cd6cf5cefc30a1d'],
 'RN44_CORE33_audit.json': [68680,'6fe828bdc4b554f0fcab0745ef608cca40c625ee0838fd6de9f8970a7e14a7bd'],
 'RN44_CORE33_independent.json': [614,'5d1c6d81e7d774a4e02b67ef607b4cf255991aa93c5e405bbc14c9111de4ef70'],
 'RN44_COVER.json': [1223,'979ebde931a30973bdd3f8c43436bdb7214662785eaf9e0cbd6f4f162c28cf0c'],
 'RN44_INNER.json': [35819,'8b2001bb4278787ede981e3f43e224a84ac9a9586c8985c750dbdc3dfcc09492'],
 'RN44_INNER_audit.json': [768845,'28cc3a42dcce8d1144928e693ff7e7920aab41da1c7ce597b7156c0ca5a23c71'],
 'RN44_INNER_independent.json': [4848,'49fafccf75691ea889b9796502ba2ab2cbbb7ecb6c29eb9ef5cc0868ee1d1726'],
 'RN44_OUTER.json': [29719,'081d6a035b4ebf3da3873556f1e9d6301a6de8ec46588253f77102dc7b652d36'],
 'RN44_OUTER_audit.json': [665594,'94656a7da34b5420dc27b71758abd998b21bb3be248007bd32dd029bdc5907ab'],
 'RN44_OUTER_independent.json': [4355,'d01825c3447a987c1f0e3f4e0e37a342b98ff3654be06e3c60edbb06a60077f3'],
 'RN44_MID.json': [39547,'a418944cd743d6704881db3ae9c62688d25e3089dcd38e5d7b0f54e16341566c'],
 'RN44_MID_audit.json': [824720,'14c43f672beff6b7435a82096f00ec06717e579f6b434ec91c8c98f8cf4a76ec'],
 'RN44_MID_independent.json': [5120,'ef8b107497d2393e7f036d5c2b342969a7438e007122272742e162fa55ebf90d'],
 'RN44_BROAD.json': [26807,'ad834c6c387c6e0ff787a84e0cd06191d34d1855cc2273d2cf02b786e6288bcc'],
 'RN44_BROAD_audit.json': [608198,'7bd98fa0d84c8e011c621683cb899422dae465676d1196124daf4657c1ff5778'],
 'RN44_BROAD_independent.json': [3952,'44171000d4720abe7fac9f0a0d83bed5db4fb6f7fb53cdc7e18af4e96f132783'],
 'RN44_U_ENVELOPE.json': [1127175,'f22af4e032d18bccb147a392d48e9170d602300cab0d933e33519c85000ebe4e'],
 'RN44_S_ENVELOPE.json': [247451,'42537e1400a524d6506eaa2f2755a39e02f840c1c9419fe9698ddfbaa5424865'],
}
TABLE = {
 'RN44_CORE33': (33,93,62,[18,8,24],7,17),
 'RN44_INNER':  (67,139,74,[13,14,25],13,12),
 'RN44_OUTER':  (62,135,75,[12,12,22],11,11),
 'RN44_MID':    (70,143,75,[12,13,23],12,11),
 'RN44_BROAD':  (62,137,77,[13,10,21],9,12),
}

def digest(path):
    b = Path(path).read_bytes()
    return [len(b),hashlib.sha256(b).hexdigest()]


def unpack_parent(text, out):
    needle = 'DATA=r' + chr(34)*3
    at = 0
    found = None
    while True:
        i = text.find(needle, at)
        if i < 0:
            break
        i += len(needle)
        j = text.find(chr(34)*3, i)
        if j < 0:
            break
        at = j + 3
        try:
            z = base64.b85decode(''.join(text[i:j].split()))
            raw = lzma.decompress(z)
        except Exception:
            continue
        if hashlib.sha256(raw).hexdigest() != RAW_SHA:
            continue
        assert len(z) == 49180
        assert hashlib.sha256(z).hexdigest() == XZ_SHA
        assert len(raw) == 207257
        found = json.loads(raw)
        break
    if found is None:
        raise ValueError('The supplied file lacks the exact RN30 literal capsule')
    assert len(found) == 46
    for name, source in found.items():
        assert Path(name).name == name and isinstance(source,str)
        (out/name).write_text(source,encoding='utf-8',newline='\n')
    return found


def unpack_rn44(text, out):
    needle = "'''RN44: exact two-cut"
    i = text.find(needle)
    if i < 0:
        raise ValueError('The supplied file lacks the literal RN44_PATCH source')
    j = text.find('\n```', i)
    if j < 0:
        raise ValueError('The literal RN44 source fence is incomplete')
    source = text[i:j] + '\n'
    (out/'RN44_PATCH.py').write_text(source,encoding='utf-8',newline='\n')


def corner_certificate(e, v):
    expected = [(0,(1,-1,1),(963,154,542)),
                (39,(-1,1,-1),(77,193,1146))]
    ans = []
    for root, signs, gaps in expected:
        actual = [min(signs[k]*(p[k]-v[root][k])
                      for i,p in enumerate(v) if i != root)
                  for k in range(3)]
        assert actual == [F(x,1000) for x in gaps]
        assert all(x > 0 for x in actual)
        directions = [(i,e.sub(p,v[root]))
                      for i,p in enumerate(v) if i != root]
        minimum = min((e.dot(a,b),i,j)
                      for i,a in directions for j,b in directions)
        assert minimum[0] > 0
        ans.append(dict(root=root,signs=list(signs),
                        coordinate_gaps=list(map(str,actual)),
                        minimum_direction_pair_dot=str(minimum[0]),
                        minimizing_pair=list(minimum[1:])))
    assert F(ans[0]['minimum_direction_pair_dot']) == F(1191221,500000)
    assert F(ans[1]['minimum_direction_pair_dot']) == F(2018491,1000000)
    return dict(
        box=[['-1517/1000','667/1000'],
             ['-634/1000','623/1000'],
             ['-1146/1000','1676/1000']],
        metric_condition='G positive definite; G12<=0,G13>=0,G23<=0',
        scope='Every interior centre of every full-dimensional convex L in box retaining both corners',
        roots=ans,
    )


def vertex_input(e, name, points):
    points = sorted(set(points))
    D = lcm(*(x.denominator for p in points for x in p))
    return dict(name=name,denominator=D,
                points=[[int(x*D) for x in p] for p in points])


def cut_one(e, r, old, normal, height, name):
    # Exact one-plane truncation of a certified maximal complex.
    v = r.raw_vertices(old)
    D0 = old['vertices'][0][3]
    H = [(tuple(p[:3]),F(p[3],D0)) for p in old['planes']]
    H.append((normal,height))
    points = {p for p in v if e.dot(normal,p) <= height}
    for i,j,*_ in old['edges']:
        d = e.sub(v[j],v[i])
        den = e.dot(normal,d)
        if not den:
            continue
        t = (height-e.dot(normal,v[i]))/den
        if 0 <= t <= 1:
            points.add(e.add(v[i],e.mul(t,d)))
    points = sorted(points)
    data = vertex_input(e,name,points)
    D = data['denominator']
    planes = []
    for n,h in H:
        ids = [i for i,p in enumerate(points) if e.dot(n,p)==h]
        if len(ids)<3:
            continue
        if not any(any(e.cross(e.sub(points[j],points[ids[0]]),
                               e.sub(points[k],points[ids[0]])))
                   for j,k in combinations(ids[1:],2)):
            continue
        L = lcm(*(F(x).denominator for x in n),F(h*D).denominator)
        ni = [int(F(x)*L) for x in n]
        hi = int(h*D*L)
        g = reduce(gcd,map(abs,ni))
        assert hi % g == 0
        planes.append(tuple([x//g for x in ni]+[hi//g]))
    return data,e.audit(data,True,planes)


def release_audits(e, r, parent, v):
    # These are optional NEW audits, not previously observed receipt claims.
    from verify_new import independent
    mid = json.loads(Path('RN44_MID_audit.json').read_text())
    normal = (-577,332,-746)
    height = F(1345075521,1000000)
    assert e.dot(normal,v[0])-height == F(591985479,1000000)
    Y = [i for i in range(40) if i not in r.X]
    assert max(e.dot(normal,v[i]) for i in Y if i!=0) == F(532431,1000)
    assert e.det(e.sub(v[14],v[9]),e.sub(v[23],v[9]),
                 e.sub(v[26],v[9])) == F(44308759,1000000000)
    data,a = cut_one(e,r,mid,normal,height,'RN45_THIRD_CAP')
    assert a['F']<=76 and a['E']<=222
    results = [(data,a)]

    points = [p for p in r.raw_vertices(mid) if p not in (v[9],v[10])]
    assert len(points)==68
    assert e.det(e.sub(v[23],v[14]),e.sub(v[26],v[14]),
                 e.sub(v[2],v[14])) != 0
    data = vertex_input(e,'RN45_RELEASE_9_10',points)
    a = e.audit(data,True)
    assert a['V']==68 and a['E']<=198
    results.append((data,a))

    manifest = {}
    for data,a in results:
        name = data['name']
        manifest[name+'.json'] = e.write(name+'.json',data)
        manifest[name+'_audit.json'] = e.write(name+'_audit.json',a)
        manifest[name+'_independent.json'] = e.write(
            name+'_independent.json',independent(a))
        print('RN45_OPTIONAL_RELEASE_AUDIT',name,a['V'],a['E'],a['F'],
              a['strict'],a['additional_weak'],
              len(a['physical']['positive_bars']),
              len(a['polar']['positive_bars']),flush=True)
    e.write('RN45_OPTIONAL_RELEASE_MANIFEST.json',manifest)


def main():
    if len(sys.argv)<4:
        raise SystemExit('usage: RN45_REPLAY.py RN30_parent.md RN44_parent.md output_dir [--release]')
    source30 = Path(sys.argv[1]).resolve().read_text(encoding='utf-8')
    source44 = Path(sys.argv[2]).resolve().read_text(encoding='utf-8')
    out = Path(sys.argv[3]).resolve()
    out.mkdir(parents=True,exist_ok=True)
    unpack_parent(source30,out)
    unpack_rn44(source44,out)
    os.chdir(out)
    sys.path.insert(0,str(out))
    subprocess.run([sys.executable,'-B','-S','REPLAY_RN30.py','lead','1'],check=True)
    import exact as e
    import RN44_PATCH as r
    r.main()
    for name,wanted in EXPECTED.items():
        actual = digest(name)
        assert actual==wanted,(name,actual,wanted)
    totalP = totalQ = 0
    for name,row in TABLE.items():
        a = json.loads(Path(name+'_audit.json').read_text())
        V,E,FF,counts,np_,nq_ = row
        assert (a['V'],a['E'],a['F'])==(V,E,FF)
        assert a['strict']==counts
        assert a['additional_weak']==[0,0,0]
        assert a['primitive_zero_P']==a['primitive_zero_Q']==0
        assert not a['boundary_face_feet']
        assert len(a['physical']['positive_bars'])==np_
        assert len(a['polar']['positive_bars'])==nq_
        totalP += np_
        totalQ += nq_
    assert (totalP,totalQ)==(52,63)
    u = json.loads(Path('RN44_U_ENVELOPE.json').read_text())
    assert all(t['passed'] for t in u)
    assert [t['epsilon'] for t in u]==['0','1/4096','1/1024','1/256']
    s = json.loads(Path('RN44_S_ENVELOPE.json').read_text())
    assert [t['certified_parent_faces'] for t in s]==[[3,9,43],[3,9],[3,9]]
    parent,v,H = r.load_parent()
    e.write('RN45_CORNER_CONE.json',corner_certificate(e,v))
    selected = ['exact.py','verify_new.py','RN44_PATCH.py',
                'RN36_RES02_G1000.json']
    e.write('RN45_SOURCE_MANIFEST.json',{name:digest(name) for name in selected})
    print('RN45_RECORDED_19_RECEIPTS_AND_115_BARS_MATCH',flush=True)
    if '--release' in sys.argv:
        release_audits(e,r,parent,v)

if __name__=='__main__':
    main()
```

## Handoff boundary

The five RN44 bodies, their115 complete positive bars, their full own-mass mechanics and the stated metric-envelope PASS results are observed exact results. The opposite-corner theorem is a direct proof from the literal coordinates and applies in its explicitly stated box/metric cone. The third cap and the targeted9/10 deletion have complete rational reconstruction recipes, but no additional full mechanical PASS is claimed for them here. They must not be relabeled own110, own121 or weak000 from their definitions or numerical nominations alone.
