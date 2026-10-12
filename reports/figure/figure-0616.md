# figure-0616

AI research report · 2026-09-29 UTC · [Export notes](../../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI report.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../../C622/README.md) passes the supplied exact checks; the search for C<500 remains open. See [verification status and source gaps](../../catalog/coverage.md).
<!-- historical-status:end -->

---

# Quiet Willow49 — finite physical mass improvement beyond the unchanged-hull reference-centre limit

Branch `[internal-source-reference]`; transaction `4cd2fdccbc3ef506fa873540`.

## Outcome and acceptance boundary

**No homogeneous own110/additionalweak000 body was obtained.** The strongest new result distinguishes physical improvement from auxiliary-centre fitting: an executed rational reference110 successor has normalized mass residual **.04154908946649722**, strictly below **24/25 of a proved lower bound for every reference-S1 centre on the unchanged old physical hull**. That old lower bound is approximately **.043445924318663294** and allows arbitrary reference roots and witness choices. Consequently, this finite improvement cannot be explained by selecting a better reference centre on the old body.

A separate construction replaces the entire polar landscape, closes its normalized physical mass numerically, and then checks the rounded rational bodies at their exact actual centroids. Its strongest clean endpoint is **78/140/64 own121**, with **P=[.5498128217216505] and Q=[]**, and a stable triangle avoiding both unstable vertices. Exact rational vertex release gives a distinct **78/228/152 own121** body with47-bit point fractions,188-bit centroid denominators and seven generic additional-point slots. Continuation from the clean actual-U1 H45 sibling gives exact simplicial V66/V67 own211 alternatives with19/18 additional-point slots.

These are different physical bodies. S1 from an own121 body and U1 from an own211 body do not combine into an own110 construction. The improved reference110 mass successor still has **28 positive P and18 positive Q bars at its actual centroid**.

### Delivery limitation

The complete intended handoff was created and validated as QW49H_RESULT.json: **192562 bytes**, SHA256 **`79eb0958e20abfb841425dca5f52e2fccf34027986a674f084e96272851b809c`**. Its `result_markdown` contains the complete63-unit executable capsule and the exhaustive20-body equilibrium/bar ledger. The corresponding Markdown handoff (`QW49H_RESULT.md`) is190255 bytes.

**This inline response does not reproduce that complete new coordinate/source capsule or the long positive-bar arrays of the fragmented controls. Under the research copy contract, the new computational bodies must therefore remain ephemeral in this inline handoff, rather than durable replacements of QW49G, unless the linked full payload is retained.** The computational work and exact audits were completed; the limitation here is the completeness of inline delivery. The scoped unchanged-parent theorem below is specified independently of any new coordinate array.

## 1. Input authority and reading

Direct immutable parent: `figure-0613`, SHA256 **`e15bba43b67e32afee950dda82e82b8eb9cbac6f806a3b4aec735938144e139f`**. Its complete QW49G source package was reused.

The supplied524629-byte journal, SHA256 **`768082ab87cfa9bcc3b58a84b2606ab48e1c921832c8038e1401242d31332625`**, was covered by reading its changed ranges and matching/reusing byte-identical previously read sections. The embedded computational parent was compared with the earlier supplied result and its decoded57-unit package. No missing source dependency was needed for the computations reported here.

The principal physical ancestor is **QW49G_APEX_MASS_RELAY_G10_COMPACT**,119/209/92, degree64 apex, actual strict(21,28,47), reference110 at

`c1=(405988057/5000000000,560382261/10000000000,-217267467/2000000000)`.

It is distinct from **QW49G_ROBUST_H45_G4**,86/129/45 own211. The former has20 additional through-apex or13 ordinary-support slots under its retained-apex bounds; the latter has40 ordinary-support slots, not40 point slots. These parent identities and their actual/reference distinctions are retained explicitly.

## 2. A whole-basin lower bound covering every reference-S1 centre of the unchanged parent

Let the literal compact common-apex parent be K, with exact uniform-volume centroid g and volume V. Its old actual polar basin contains the following22 facets, indexed in the compact exact audit ordering:

```text
B=[29,30,31,32,33,34,35,36,57,58,59,60,61,62,63,64,85,86,87,88,89,90].
```

For normalized supports `n_i.x<=1`, write

`H_i(c)=1-n_i.c`,

`D_ij(c)=(n_i.n_j)H_i(c)-|n_i|²H_j(c)`.

Inside K, the sign of D_ij is the sign of the polar chord `q_i(c).(q_j(c)-q_i(c))`, where `q_i(c)=n_i/H_i(c)`. In particular,

`D_ij(c)=C_ij+A_ij.c`,

`C_ij=n_i.n_j-|n_i|²`,

`A_ij=|n_i|² n_j-(n_i.n_j)n_i`.

The executed rational checker verified all **1540 outward ordered chords** from B as strictly negative at g. Every one stays negative throughout a Euclidean ball whose limiting pair is **64→37**. Its radius is approximately

`r=.02756621594681341`.

The disjoint polar root24 retains all91 strict negative root guards on a larger ball, and the supporting distances remain positive on the stated ball.

At any centre in that ball, choose a maximum-radius polar vertex in B. Its chords to other B vertices are strictly negative because

`2 q_i.(q_j-q_i)=|q_j|²-|q_i|²-|q_j-q_i|²<0`.

The certified cut handles every vertex outside B. Thus B contains a strict polar unstable vertex, equivalently a strict stable physical facet. Root24 supplies another. This allows the identity of the stable facet inside B to change.

Therefore **every reference-S1 centre on this unchanged physical hull**, irrespective of its chosen root or coforest, satisfies

`|c-g|/V^(1/3) >= L`,

where **L≈.043445924318663294**.

This is a necessary lower bound, not an assertion that the nearest S1 centre attains it. It is not an exclusion of moved supports, altered incidence, added material or changed homogeneous mass.

The executed report is `QW49H_FIXED_HULL_ESCAPE_CERTIFICATE.json`,654928 bytes, SHA256 **`fa3ad622c57b9bd546d0b63b2dd4a6f9e8a623b3770088bb8ce897b31093f540`**. Its original complete producer is included in the full capsule as `fixedcut49h.py`.

### Independent compact reconstruction of the unchanged-parent certificate

The following complete standard-library unit reconstructs the exact lower-bound quantity from the already durable parent audit, whose full byte identity is checked. It is an alternative replay unit supplied here, **not an additional executed independent-verifier receipt**. The executed result above came from `fixedcut49h.py` in the full package.

Save as `verify_old_reference_S1_cut.py` beside the parent audit, reconstructed using the immutable QW49G capsule, and run `python verify_old_reference_S1_cut.py`. No new-body coordinates or numerical optimizer are required.

```python
from fractions import Fraction as Q
from pathlib import Path
import hashlib, json, sys

sys.set_int_max_str_digits(0)
SOURCE = 'QW49G_APEX_MASS_RELAY_G10_COMPACT_AUDIT.json'
EXPECTED = '744b19bee57839bccb9cfcfa769a1a977d3f59a273e5e60f2f5ffd5b33535dc6'
B = [29,30,31,32,33,34,35,36,57,58,59,60,61,62,63,64,85,86,87,88,89,90]

def dot(a,b):
    return sum((x*y for x,y in zip(a,b)), Q(0))

def sub(a,b):
    return tuple(x-y for x,y in zip(a,b))

def cross(a,b):
    return (a[1]*b[2]-a[2]*b[1],
            a[2]*b[0]-a[0]*b[2],
            a[0]*b[1]-a[1]*b[0])

def main():
    raw = Path(SOURCE).read_bytes()
    assert hashlib.sha256(raw).hexdigest() == EXPECTED
    audit = json.loads(raw)
    assert [audit[k] for k in ('V','E','F')] == [119,209,92]
    X = [tuple(map(Q,p)) for p in audit['vertices']]
    g = tuple(map(Q,audit['centroid']))
    volume = Q(audit['volume'])
    N = []
    for face in audit['faces']:
        a,b,c = [X[i] for i in face[:3]]
        n = cross(sub(b,a),sub(c,a))
        h = dot(n,a)
        assert h != 0
        n = tuple(z/h for z in n)
        assert all(dot(n,x) <= 1 for x in X)
        assert {i for i,x in enumerate(X) if dot(n,x)==1} == set(face)
        N.append(n)
    assert len(N) == 92 and volume > 0
    Bset = set(B)
    assert 24 not in Bset

    def guard(i,j):
        ni,nj = N[i],N[j]
        aa,ab = dot(ni,ni),dot(ni,nj)
        A = tuple(aa*nj[k]-ab*ni[k] for k in range(3))
        C = ab-aa
        value = C+dot(A,g)
        assert value < 0, (i,j,value)
        norm2 = dot(A,A)
        return None if norm2 == 0 else value*value/norm2

    cut = []
    for i in B:
        for j in range(92):
            if j not in Bset:
                value = guard(i,j)
                if value is not None:
                    cut.append((value,i,j))
    assert len(B)*(92-len(B)) == 1540
    cut2,i,j = min(cut)
    assert (i,j) == (64,37)

    root_bounds = [guard(24,j) for j in range(92) if j != 24]
    root_bounds = [z for z in root_bounds if z is not None]
    interior_bounds = []
    for n in N:
        h = 1-dot(n,g)
        assert h > 0
        interior_bounds.append(h*h/dot(n,n))
    assert min(root_bounds) > cut2
    assert min(interior_bounds) > cut2

    lower6 = cut2**3/volume**2
    result = {
        'source_sha256': EXPECTED,
        'block': B,
        'all_outward_pairs': 1540,
        'separate_polar_root': 24,
        'limiting_pair': [i,j],
        'radius_squared': str(cut2),
        'normalized_lower_bound_sixth_power': str(lower6),
        'radius_display': float(cut2)**0.5,
        'normalized_lower_bound_display': float(lower6)**(1/6),
        'scope': 'Every reference S1 centre of this unchanged hull; not changed geometry.'
    }
    Path('OLD_REFERENCE_S1_LOWER_BOUND.json').write_text(
        json.dumps(result,sort_keys=True,separators=(',',':'))+'\n')
    print(json.dumps(result,sort_keys=True))
    print('OLD_FIXED_HULL_REFERENCE_S1_LOWER_BOUND_PASS')

if __name__ == '__main__':
    main()
```

## 3. Finite physical geometry beats that whole unchanged-hull bound

The new **QW49H_IMPLICIT_MASS_G14** body has **143/233/92**, degree40 apex, actual strict **(19,29,46)**, additionalweak000 and primitive000. Its exact rational reference point is

`c=(7763867539159,5638985727413,-10533685433411)/10^14`.

At this reference it is exactly strict110, weak000, P=[],Q=[]. Its actual homogeneous quantities are approximately

```text
V=.2565381608846945
g=(.06065720846926766,.052544287405985525,-.0854917584476799)
|g-c|/V^(1/3)=.04154908946649722.
```

The complete exact comparison uses sixth powers, avoiding numerical square or cube roots:

`m(K,c)^6=(sum_k(g_k-c_k)^2)^3/V²`.

The executed certificate verifies **m_new < (24/25)L** exactly. Its displayed ratio to L is approximately .9563403269256436. Both the material geometry and compatible reference point changed; this is more than a4% improvement beyond what any reference-S1 centre could achieve on the old unchanged geometry.

The reference stable carrier also changes its relation to the unstable apex. New reference S24 is the14-gon

```text
[5,141,89,92,73,98,88,107,105,52,50,54,57,12],
```

which **avoids reference U66**, the retained degree40 apex. The parent’s reference stable14-gon contained its reference U40. This is genuine carrier detachment, not a relabelled centre.

The new body nevertheless has28 actual positive P and18 actual positive Q bars. It is not own110, and no weak-free continuous path between the endpoints is claimed. Under the retained-apex bound it has eight more through-apex or five ordinary-support slots, not the H45 sibling’s forty ordinary slots.

Exact new input:8700 bytes, SHA256 **`ebe9550c5b2f0c98aee1e491805f731dbb47d1e3ba2c1eadce95b697a7f1eada`**. Exact audit:7525942 bytes, SHA256 **`281cd6ea97bb110f13f1605212286f487199d528c68208d38bd8ca21ba702f31`**. The full literal input and all46 positive bars are in the complete linked handoff/package; they are not reconstructed from these displays.

## 4. What the reference-centre KKT calculation established

Two selected closed rational reference cells were constructed by retaining half of every initial exact guard, with the stated L1 coefficient normalization. Each cell includes every selected nonroot positive chord, all required strict root guards and interiority. Their nearest-centre points were certified by exact feasibility, nonnegative multipliers, complementarity and stationarity with three active rows.

For the old common-apex parent, the510-row cell with physical/polar roots40/24 projects to normalized distance **.04429196436746768**, compared with the supplied reference distance **.044291982863602655**. The active guards are Q90→35, P57→98 and Q89→63. Auxiliary-centre adjustment in this selected cell accounts for almost none of the subsequent physical improvement.

For the moved intermediate body, a558-row cell with roots66/24 projects to **.04155770785589886**, compared with **.041557707877308586** at its starting reference. Its active guards are Q37→91, Q34→89 and Q36→64.

These are global projections onto the **specified individual cells**, not onto the union of all coforest/root cells. The stronger old-hull bound in section2 is a different whole-basin certificate and does cover arbitrary reference-S1 roots on that unchanged body.

`implicitcenter49h.py` then physically moves the supporting normals and apex while solving three current polar-form midpoint-margin equations for the auxiliary centre. Complete reference forests are revalidated on every admitted finite hull. The executed28-record prefix accepted15 steps. A fresh producer replay matched its saved binary64 endpoint; the requested300-step tail was not executed or claimed.

## 5. Degree-dependent contact release and completed prefixes

For M submitted supports and K supports through a feasible rank-three apex, the retained-apex bound is

`E<=3M-K-3`.

Releasing one existing apex contact while retaining the row costs at most one edge in this bound; adding an ordinary support costs at most three. These are different operations.

Two exact controls release24 or40 of the original64 contacts by the specified factor `(10^9+1)/10^9`, while retaining the old exact apex and c1. They have **143/233/92** and **159/249/92**, respectively. Both retain reference110 and actual strict(21,28,47), but their actual mass and bars are recomputed. The24-contact release, retaining40 apex contacts, is the ancestor of the improved mass chain; the40-contact release is a separate E249 control.

The principal numerical prefixes were: RELEASE_FLOW40,90 records/90 accepted; LINEAR40,200/195; MOVING_APEX,198/183 of a400 request; IMPLICIT,28/15 of a300 request. A separate264-record LINEAR40_B run is not the promoted ancestry. Exact endpoint definitions do not depend on completing any unexecuted tails.

## 6. Actual whole-Q cancellation and clean nonwinning endpoints

A second route builds a complete positive forest of **actual material polar points**, rather than supplying a virtual witness outside the hull. For a through-apex child q, write `q.u=1` and `k=u/|u|²`. Its allowed tangent disk inside the parent’s diameter ball gives a positive polar chord. The complete forest excludes every nonroot polar equilibrium on a valid bounded hull.

Actual uniform mass is rebuilt and adjusted through the geometry. The rational freezes have small but **nonzero** actual centroids; their own classes are established by exact census, not by declaring the numerical residual zero.

The following table gives the entire positive P/Q lists for all twelve clean new bodies. All names have prefix `QW49H_`; all have additionalweak000 and primitive000.

| Body | True V/E/F | Actual S/U/H | Entire P | Entire Q |
|---|---:|---:|---|---|
|DETACHED_S1_G12|86/152/68|1/2/1|[.6994403857145557]|[]|
|DETACHED_SMALL_G12|85/150/67|1/2/1|[.6992965196803752]|[]|
|S1P2_G12|83/147/66|1/2/1|[.6992933616422187]|[]|
|PCAP55_G12|78/140/64|1/2/1|[.5498128217216505]|[]|
|PCAP60_G12|78/140/64|1/2/1|[.5990230235897358]|[]|
|RELEASED_S1_V78_G14|78/228/152|1/2/1|[.5498128217216706]|[]|
|RELEASED_S1_BUFFER_V78_G14|78/228/152|1/2/1|[.5990230235897263]|[]|
|RELEASED_V67_G6|67/195/130|2/1/1|[]|[.31754950172080637]|
|RELEASED_V67_G7|67/195/130|2/1/1|[]|[.3175495001026439]|
|RELEASED_V66_G6|66/192/128|2/1/1|[]|[.3235596462814982]|
|RELEASED_V66_G7|66/192/128|2/1/1|[]|[.3235597898459906]|
|REPAIRED_V65_G8|65/189/126|2/1/1|[]|[.59898397505407]|

These displayed depths are approximations to positive exact fractions. The full exact birth/death/depth data are retained in the linked payload.

### PCAP55: detached stable triangle and a new whole-P obstacle

PCAP55 has a degree49 apex, S63 triangle **[37,51,52]**, U43/46, H26–43. The triangle avoids both unstable vertices. Its actual volume is approximately .14522695465696564 and actual centroid approximately

`(3.490331707321523e-14,1.9068036228865513e-13,3.905941281169488e-13)`.

Its complete physical positive-chord complement is **all78 vertices except37 and43**:76 vertices,50 true crossings and152 strictly negative outward ordered chords. Thus Q is actually cancelled, but a new whole-P basin remains. No low-stable-carrier-below-P-death claim is made.

PCAP60 has S63 hexagon **[37,39,73,50,46,74]**, U45/48, H1–45, actual volume approximately .13214698269520042. Its complete physical complement is **all78 vertices except37,39,45**:75 vertices,49 true crossings and225 negative outward ordered chords. It trades deeper P for larger selected physical nonroot margins; it is not an unconditional improvement over PCAP55.

Both initially submit93 H rows,29 of which are exactly inactive. Their compact64-row/49-through-apex representations are the **same bodies**, with complete lattice, mass and census equality checked. The compact retained-apex bound permits54 additional through-apex or36 ordinary supports at E<=248. That budget cannot be assigned to all93 potentially reactivated raw rows.

### Simplicial arithmetic alternatives

Exact rational rounding of PCAP55/60’s exact vertices to denominator10^14 gives two distinct78/228/152 own121 bodies. All maximal facets are triangles. The main released body has S151 triangle **[0,65,60]**, U43/76, H1–43; the buffer sibling has S150 triangle **[0,54,57]**, U45/76, H3–45. Each stable triangle avoids both U.

The main released body has47-bit point fractions and188-bit centroid denominators, compared with much larger common-apex arithmetic. Its actual volume is approximately .1452269546569666 and its actual centroid remains nonzero, approximately

`(3.5751576434889493e-14,1.9095932924347558e-13,3.9137890073010944e-13)`.

Seven generic points fit the V85/E249 bound. This was an executed rational release, not an automatic application of the coordinator’s separate simple-polyhedron theorem to a nonsimple body.

### Clean actual-U1 material-point alternatives

Retirement and correlated small point motion from the literal H45 sibling give V66/V67 own211 bodies. RELEASED_V67_G6 has stable triangles **[2,22,20]** and **[9,60,19]**, both avoiding U3, with H11–43. Its point/centroid-denominator maximum bit counts are20/83. Its new whole-Q complement has78 polar vertices and38 true crossings; all4056 outgoing ordered global chords are negative.

RELEASED_V66_G7 has stable triangles **[11,16,15]** and **[2,58,21]**, both avoiding U4, H12–43, and24/97-bit arithmetic. The distinct G6 freeze has a different carrier-incidence relation; it must not inherit the G7 detachment statement.

## 7. Other exact controls and complete-ledger location

Eight additional distinct bodies have larger actual classes:

| Body | V/E/F | Actual S/U/H | Reference status |
|---|---:|---:|---|
|RELEASE24_EXACT|143/233/92|21/28/47|exact110 at c1|
|RELEASE40_EXACT|159/249/92|21/28/47|exact110 at c1|
|OFFSET_MASS_G12|143/233/92|20/29/47|exact110|
|MOVING_MASS_G12|143/233/92|19/29/46|exact110|
|IMPLICIT_MASS_G14|143/233/92|19/29/46|exact110|
|FREE60_REF_G12|116/174/60|18/27/43|exact110|
|FREE59_REF_G12|109/166/59|23/28/49|exact110|
|SFOREST_MASS_G12|94/168/76|1/10/9|actual Q=[]; nine actual P|

Every row has additionalweak000 and primitive000. None is promoted as own110. Four compact representations—FREE59, FREE60, PCAP55 and PCAP60—are exact identical-body reductions, not four more constructions.

The full **twenty-body** actual root/saddle and positive-bar arrays, plus separate reference arrays, are repeated in the complete linked Markdown handoff. They also appear in `LEDGER49H.json`,48251 bytes, SHA256 **`2fbdca80cdcc49f22f9528b388a011d68d0580c53e3bdb4c6f53ef256ac1a658`**. Their omission from this shorter inline response is part of the delivery limitation stated above; no omitted small positive bar is being treated as zero.

## 8. A finite outward family preserving the whole reference-S1 forest

A useful exact family was certified on the MOVING body, at its fixed recorded reference centre. The following33-node subset is predecessor-closed for its selected91-arrow polar forest:

```text
[0,1,2,4,5,10,11,17,18,26,29,30,31,32,33,34,35,36,37,
 57,58,59,60,61,62,63,64,85,86,87,88,89,90].
```

For every epsilon>=0, shrink the corresponding centred polar points by `1/(1+epsilon)`. In physical H coordinates this changes

`h_i -> h_i+epsilon*(h_i-n_i.c)`.

After multiplication by `(1+epsilon)^2`, every selected forest guard has a polynomial with certified positive coefficients. For internal edges it is the original score; for an exit it is the original score plus epsilon times `q_i.q_j`; for outside edges it is the original score times `(1+epsilon)^2`. Predecessor closure prevents an uncontrolled outside-to-inside case.

Thirty unchanged through-apex rows and an exact positive normal-cone combination on54/67/82 retain the apex as a strict reference U, with E<=243. Thus **the entire finite family has referenceS1 and no weak S**, and retains that strict reference U. It does **not** certify that this is the only reference U, and it does not certify the actual-centroid class or adequate mass capacity.

Fourteen tested uniform offsets moved mass in the wrong direction or regrew U. Two completed independently variable33-offset scouts stayed in the selected reference-S1 cell but had referenceU18. The lower-residual one reached approximately .04141539156358716 with actual S19/U27, not reference110 or own110. Its smaller scalar residual is therefore not an improvement of the reference110 frontier. Both full producing recipes are retained as numerical controls, not universal exclusions.

The exact family report is41114 bytes, SHA256 **`f3eef4651de514a71125d4372dc7a12764be51dd299ed0991653bf1e73a473cc`**. The complete `family(epsilon)` generator and checker are in `subtree_certificate49h.py` in the full capsule.

## 9. Recovery package and observed execution

The full self-contained package is available as:

Complete decoder (`RECOVER_QW49H.py`)

Complete structured handoff, including its inline63-unit capsule (`QW49H_RESULT.json`)

Complete Markdown handoff (`QW49H_RESULT.md`)

All research sources, numerical states, logs and exact reports (`QW49H_COMPLETE_RESEARCH.zip`)

Confirmed decoder identity: **138833 bytes**, SHA256 **`70a4bb96e83bc04490ad6fe2a61a8fd1abf1b2407161fe36cb7305937d098b61`**. It decodes **63 units /399500 bytes**, dictionary SHA256 **`7f8fc10557b459cbc2bee9d72c32dd7a79b33dded6df7264a81cf760595f1d69`**. The ZIP is41475402 bytes, SHA256 **`1bba07452618d8e56058165aea0f27d88b0a4bfd2c41418870fcd3eb4c82816c`**; its634 entries passed the archive integrity check.

The capsule includes all54 complete producing/verifying source units and their local helper closure,27 exact input reconstructions,15 literal numerical checkpoints, bounded-prefix recipes, per-file source identities and109 expected full output receipts. Exact body recovery needs no optimizer and no earlier sandbox.

```sh
python RECOVER_QW49H.py QW49H_RECOVERED
cd QW49H_RECOVERED
python REPLAY49H.py --all --jobs 3
# Following an interruption, reuse only complete hash-matching outputs:
python REPLAY49H.py --all --resume --jobs 3
python INPUTS49H.py
python PRODUCE49H.py
```

Observed markers include:

```text
QW49H_LITERAL_SOURCE_RECOVERY_PASS 63 7f8fc10557b459cbc2bee9d72c32dd7a79b33dded6df7264a81cf760595f1d69
QW49H_COMPLETE_EXACT_INPUT_RECOVERY_PASS 27
QW49H_LITERAL_NUMERICAL_GEOMETRY_RECOVERY_PASS 15
QW49H_GLOBAL_FIXED_HULL_S1_DISTANCE_AND_FINITE_GEOMETRY_ESCAPE_EXACT_PASS
QW49H_ENTIRE_REFERENCE_S1_OUTWARD_FAMILY_EXACT_PASS_NOT_OWN_CLASS 33 91 243
QW49H_TWENTY_DISTINCT_BODIES_FOUR_IDENTICAL_REPRESENTATIONS_FULL_EXACT_PASS_NO_110
QW49H_THREE_PRODUCERS_FOUR_LITERAL_GEOMETRIES_REPLAY_PASS
```

A fresh directory regenerated the three necessary parent audits and all24 new representations without copying old audits. Own/reference reports and exact input/H/output hashes matched. Four same-body lattice/mass/census/bar equalities, both KKT certificates, the old-cut/new-geometry comparison and the current basin diagnostics were checked. The last-added subtree checker was cold-executed separately; the updated aggregate wrapper then completed by hash-checked resumption of those already cold-built outputs.

Three numerical producer replays—implicit-centre flow, detached P-cap repair and point retirement—matched four complete binary64 output arrays. **The entire floating optimization history was not independently cold-replayed.** The exact mechanics uses one inherited C++ engine with two mass formulas and direct/global predicate crosschecks, not two independently developed physics verifiers.

Observed environment: CPython3.13.5, NumPy2.3.5, SciPy1.17.0, Torch2.10.0+cpu, float64 and one numerical thread; g++14.2.0, C++17, GMP/GMPXX. Exact replay needs standard-library Python plus C++17/GMP, with assertions enabled.

## 10. Continuation that follows from the evidence

The common-apex route now has a certified improvement beyond **every** reference-S1 centre of its old unchanged geometry. Continue from the physically changed IMPLICIT input, not by refitting c on the old parent. Its remaining actual28P/18Q cannot be ignored, and its retained-apex support budget is limited. The implicit active-guard chart and outward reference-S1 family provide concrete, executed directions, but neither establishes mass capacity or absence of new physical U.

The clean alternative is PCAP55 or its simpler78-point simplicial release. There the **entire actual Q landscape is cancelled**, but the new76-node physical basin remains. Seven material-point slots on the simplicial release, or the larger degree-dependent H reserve on the compact common-apex version, offer different construction freedoms. The V66/V67 own211 bodies preserve the opposite one-sided completion with substantially simpler arithmetic and18/19 point slots.

No fixed-cut certificate above excludes these future changed geometries. No finite failed scout is promoted into a family-wide impossibility. The exact new bodies, their complete positive bars and their complete source recovery remain available in the validated full handoff; until that full payload is retained, this inline result preserves the analytic mechanism and evidence summary but not a durable new computational checkpoint.
