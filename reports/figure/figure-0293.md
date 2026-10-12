# figure-0293

AI research report · 2026-09-04 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# Bright Lynx 17 — independent clean-room audit of orphan `J56_TB9_metric_cancel_belt24`

## Exact determination

**FALSIFIED.** The orphan is not a valid exact winner and must not be restored as a parent or completion ticket. The journal explicitly classified the recovered message as source evidence rather than an immutable accepted result, although its embedded report asserted strict `(S,U,H)=(1,1,0)`.

The reported determinant-one shear does put the parent residual 17-gon unstable primitive and closure-edge saddle primitive on zero simultaneously. However, an independently written exact-`Fraction` reconstruction finds this different strict packet already present at that same wall:

```text
stable:   2475, 5003
unstable: [2475,5000,5003], [5003,14001,14014]
saddles:  [5003,14003], [5003,14011]
```

At the exact rational point `alpha=alpha0+2^-30`, all **272** mechanics primitives of the unchanged 18-row lattice are nonzero and the class is strictly `(2,2,2)`, not `(1,1,0)`. Its minimum absolute primitive is greater than `2^-24`. This directly contradicts the orphan's statement that the first post-wall chamber is already a Gömböc and that no replacement feature is born. The exact shear equations and that no-birth claim appear in the recovered report.

This audit did not use or conflate the distinct immutable Bright Lynx `(2,2,2)` continuation.

## Literal authoritative parent and deterministic reconstruction

Authority:

```text
assignment: figure-0266
immutable result SHA-256: 49545ef8d787bb7886f19249253131f72ee0f35f1bb499c3bce73e75cbf23fd1
exact active-source SHA-256: ba6f45ae283e444a4ee92ff14e4987041ca4e442a181892675f6b8af00759fa3
```

Let `N=2^24`. In label order

```text
[14000,14001,14002,14003,14004,14005,14006,14007,
 2475,5000,14008,14009,14010,14011,14012,14013,14014,5003]
```

the first 17 raw support rows are `(X/N,Y/N,-1/140)` with:

```text
14000  11653197 -13937873
14001   5763878 -16027135
14002  16793753  -9690398
14003  20394447  -3554346
14004  21762407   3910885
14005  20408886  11892808
14006  16140728  19400855
14007   9124192  25373787
2475      -90148  28809026
5000    -9304549  25373787
14008  -16321192  19400855
14009  -20589485  11892808
14010  -21943151   3910885
14011  -20575324  -3554346
14012  -16974741  -9690398
14013  -11834262 -13937873
14014   -5944980 -16027135
```

and

```text
5003=(271080/N,-15609202/N,360000/N).
```

The verifier freshly enumerates all supporting triples using integer homogeneous determinants, solves every polar vertex exactly, constructs all maximal cycles and true edges, integrates signed tetrahedra, sets `c=M/V`, and applies

```text
q -> q/(1-q·c),
p -> p-c.
```

Coordinate-for-coordinate parity with the literal exact J55 source passes. The resulting dual/primal f-vector is `(18,34,18)`, all three centered first moments are exactly zero, and exhaustive mechanics reproduces strict J55 `(1,2,1)`:

```text
stable:   2475
unstable: full residual 17-gon; [2475,5000,5003]
saddle:   [14001,14014].
```

## Fatal exact shear countercheck

Let `n` be the centered primal vertex dual to the residual 17-gon, so `n·q_i=1` on those rows. Set

```text
a=q_14001,
b=q_14014,
e=b-a,
u=n×e
```

with sign chosen so `u·(q_i-a)<0` for every other polygon vertex, and `p0=n/(n·n)`. The orphan's shear is

```text
alpha0=-(n·n) u·(p0-a)/(u·u),
B(alpha)=I-alpha*u*n^T/(n·n).
```

Because `u·n=0`, `det B=1`, `B^-1=I+alpha*u*n^T/(n·n)`, and the centered primal map is `B^-T`. The clean-room reconstruction gives

```text
alpha0 ≈ 191.5535846983706
reduced-fraction SHA-256:
2a20b3bda132e27113734807699c587f5adf5bb4c0f0853f498fefa2efdafad8
numerator/denominator decimal digits: 1721/1718
wall edge parameter ≈ 0.4922729513257965, strictly between 0 and 1.
```

The exact fraction itself is generated from the inline parent table by the displayed formula and is serialized in `source/audit_source.json`.

At `alpha0`, exactly two intended primitives vanish: one residual-vertex component and the closure-edge segment parameter `t`. The following compact sign certificate is verified by exact integer cross-multiplication; every denominator is positive:

```text
sigma(5003 -> 14001) > 14,
min_neighbor_tau([5003,14001,14014]) > 1,

edge [14003,5003]:
  t > 3/4,
  1-t > 1/5,
  beta_14003 > 4/5,
  beta_5003 > 1/5,

edge [14011,5003]:
  t > 1/4,
  1-t > 7/10,
  beta_14011 > 3/4,
  beta_5003 > 1/5.
```

Thus `5003` is a strict second stable face, `[5003,14001,14014]` is a strict second unstable vertex, and both listed edges are strict saddles at the alleged cancellation wall. Their strictness persists immediately beyond it. The wall ledger contains 272 primitives, exactly two zeros, and minimum absolute value among all other primitives `0.066188281659114598`.

### Saddle-cone convention

For a true primal edge with endpoints `A,B`, put `d=B-A`,

```text
t=-A·d/(d·d),
f=A+t d,
f=beta_i q_i+beta_j q_j.
```

It is a saddle iff `t,1-t,beta_i,beta_j` are all positive. Swapping edge endpoints or incident support rows only swaps paired components, so the decision is orientation-invariant.

## Why missing orphan files cannot rescue the claim

The recovered Markdown omits literal `alpha_star`, `epsilon_0`, `epsilon_1`, `epsilon_16`, perturbation radius `rho`, final exact support/vertex coordinates, and the reduced final volume. It merely says they were stored in an unavailable exact source. The named archive/source were absent from current mounted files and Library search.

This omission is not the falsification basis. Even were those files recovered, the claimed chronology says no primitive crosses between `alpha0` and `alpha_star` and that the unchanged lattice is already `(1,1,0)`. The strict wall packet above makes that impossible. A later unrelated event might conceivably create a winner, but it would not authenticate the orphan report's stated proof or death-before-birth chronology.

## Exact canonical member of the claimed nine-row belt family

To settle the reported `(21,43,24)` count, label order, true-edge, centering, perturbation, and mesh ambiguities, the package also materializes this completely specified member of the literal belt formula:

```text
alpha=192,
epsilon_0=epsilon_1=epsilon_16=1/4.
```

After shearing centered J55, define

```text
15000=3/4 q14000+1/4 q14001
15001=3/4 q14000+1/4 q14002
15002=3/4 q14000+1/4 q5003
15003=3/4 q14001+1/4 q14000
15004=3/4 q14001+1/4 q14014
15005=3/4 q14001+1/4 q5003
15006=3/4 q14014+1/4 q14001
15007=3/4 q14014+1/4 q14013
15008=3/4 q14014+1/4 q5003.
```

Retain the other 15 sheared parent rows. Supply old `14000,14001,14014` only as half-vectors, hence strictly inactive. Rebuild the polar, compute its exact raw centroid `c_B`, and recenter projectively as above. Active order is

```text
[14002,14003,14004,14005,14006,14007,2475,5000,
 14008,14009,14010,14011,14012,14013,5003,
 15000,15001,15002,15003,15004,15005,15006,15007,15008].
```

Fresh all-triples H enumeration and an independent all-triples V enumeration agree exactly:

```text
Q (V,E,F)=(24,43,21)
P (V,E,F)=(21,43,24)
Euler=2
exact centered moments=(0,0,0)
exact volume decimal=201.91783266732273
reduced volume-fraction SHA-256:
ff0beeeba56d6f2232452de395524c439fa30ce660fd0d614422de8e4d55e464
```

The exact volume is the reduced rational obtained from the inline generator by

```text
V=(1/6) Σ det(v0,v1,v2)
```

over the outward fan triangulations of the maximal cycles below; its full numerator and denominator are in the exact source. Exact safety margins are:

```text
minimum raw nonincidence       0.032108263413666176
minimum centered nonincidence  0.032180248511463963
minimum projective denominator 0.99769675545504044
minimum inactive-row slack     0.48995649190148394.
```

### All 21 maximal Q facets / all 21 primal vertices

Canonical primal vertex indices are the line numbers below:

```text
00: 5003,14002,14003
01: 5003,14002,15001,15002
02: 2475,5000,14002,14003,14004,14005,14006,14007,14008,14009,
    14010,14011,14012,14013,15000,15001,15003,15004,15006,15007
03: 5003,14003,14004
04: 5003,14004,14005
05: 5003,14005,14006
06: 5003,14006,14007
07: 2475,5003,14007
08: 2475,5000,5003
09: 5000,5003,14008
10: 5003,14008,14009
11: 5003,14009,14010
12: 5003,14010,14011
13: 5003,14011,14012
14: 5003,14012,14013
15: 5003,14013,15007,15008
16: 5003,15000,15002,15003,15005
17: 5003,15004,15005,15006,15008
18: 15000,15001,15002
19: 15003,15004,15005
20: 15006,15007,15008
```

The long line `02` is one 20-gonal Q facet, not twenty facets. This resolves the apparent mismatch between 21 primal vertices and the longer incidence list. The orphan's claimed active/supplied counts are recorded in the journal.

### All 43 true edges

```text
14002-14003, 5003-14002, 14002-15001,
14003-14004, 5003-14003,
14004-14005, 5003-14004,
14005-14006, 5003-14005,
14006-14007, 5003-14006,
2475-14007, 5003-14007,
2475-5000, 2475-5003,
5000-14008, 5000-5003,
14008-14009, 5003-14008,
14009-14010, 5003-14009,
14010-14011, 5003-14010,
14011-14012, 5003-14011,
14012-14013, 5003-14012,
5003-14013, 14013-15007,
5003-15002, 5003-15005, 5003-15008,
15000-15001, 15000-15002, 15000-15003, 15001-15002,
15003-15004, 15003-15005, 15004-15005, 15004-15006,
15006-15007, 15006-15008, 15007-15008.
```

### All 24 maximal P-face cycles

```text
14002: 0,1,2
14003: 0,2,3
14004: 2,4,3
14005: 2,5,4
14006: 2,6,5
14007: 2,7,6
2475:  2,8,7
5000:  2,9,8
14008: 2,10,9
14009: 2,11,10
14010: 2,12,11
14011: 2,13,12
14012: 2,14,13
14013: 2,15,14
5003:  0,3,4,5,6,7,8,9,10,11,12,13,14,15,17,16,1
15000: 2,18,16
15001: 1,18,2
15002: 1,16,18
15003: 2,16,19
15004: 2,19,17
15005: 16,17,19
15006: 2,17,20
15007: 2,20,15
15008: 15,20,17
```

No display diagonal is included in the true-edge ledger.

## Corrected mechanics, open chamber, and mesh

Exhaustive exact evaluation of 24 face rows, 21 complete vertex cones, and `43×4=172` edge-cone components gives the canonical member strict `(2,2,2)`:

```text
stable:   2475, 5003
unstable: [2475,5000,5003], [5003,15004,15005,15006,15008]
saddles:  [5003,14003], [5003,14011].
```

Across all 344 mechanics primitives, the smallest positive component is `0.059346247207164457`; the closest negative component is `-0.012600103541392354`.

For

```text
A(s,t)=[[1,s,t],[0,1,0],[0,0,1]],
P -> A(s,t)P,
Q -> A(s,t)^(-T)Q,
```

the entire exact square `|s|,|t|<=1/16` retains this incidence and class. Covariance preserves centroid zero and all incidence equalities; exact sparse bivariate coefficient-sum bounds certify all 344 mechanics polynomials, with worst remaining positive slack greater than `1/1024`. This independently establishes an open **nonwinner** chamber. The absent orphan radius `rho` itself cannot be authenticated.

The canonical P has 23 triangular maximal faces and one 17-gon. Triangulating only that 17-gon adds 14 nonphysical diagonals:

```text
vertices=21
triangles=38
mesh edges=57
true edges=43
triangulation diagonals=14
Euler=21-57+38=2.
```

Every mesh edge has multiplicity two; OBJ and STL triangle streams agree exactly and are coherently outward oriented.

## Independent replay and final hashes

The verifier is independent Python standard-library code using `fractions.Fraction`; it does not read orphan certificates, orphan coordinates, or an orphan mesh. A clean extraction of the final archive passed its SHA-256 manifest before execution, reran the entire exact reconstruction in about 2m49s, regenerated byte-identical outputs, and passed the same manifest afterward.

```text
exact audit source SHA-256:
bac5ca373846851ce790b9191b064e33ca6b117f73cc2b450f26fb6125eca18d

independent verifier SHA-256:
1c18220fc13e1a86e94bc57cabda4e101752d2ca48a9334c76ee139671ada046

archive bytes: 7,435,104
archive SHA-256:
037f14055c94d7bb681dd66b410926b352a6a8347331992318f39f16c7dd5b52

standalone report SHA-256:
bc6b3e9ee1239ab9ca57ae941037d49dadad72a8af22446131095b8f5b1e8b41

verification receipt SHA-256:
4f66663f71b3945f37b686ad4deb2d854a091cce3610f63233bbb0cc5b6a847c

internal manifest SHA-256:
acee7aa650faa7c09dec5c132a88bcf4b5ca6ee4af0738bceff8453cc64f0fbb

final clean-replay SHA-256:
2fdfbd583989125a7264393a9a3840ffa8cd97a298218f1090c9b7e01726dd4b

OBJ SHA-256:
d39d9ad5e7b73520a35b0acb708796507ec632dda73b7e29b5b3b11030ff33a2

STL SHA-256:
004128d34944acdd771c97181be249a366f90f2f1ab3f09e73c7cc6a62188f2f
```

Run:

```bash
bash run_all.sh
```

Artifacts:

- Final portable falsification archive (`J56_TB9_orphan_cleanroom_FALSIFICATION.zip`)
- Archive SHA-256 companion (`J56_TB9_orphan_cleanroom_FALSIFICATION.zip.sha256`)
- Final clean-extraction replay (`J56_TB9_orphan_cleanroom_CLEAN_REPLAY.txt`)
- Clean-replay SHA-256 companion (`J56_TB9_orphan_cleanroom_CLEAN_REPLAY.txt.sha256`)
- Standalone report (`RESULT.md`)
- Verification receipt (`VERIFICATION_RECEIPT.json`)
- Internal hash manifest (`SHA256SUMS.txt`)
- Independent exact verifier (`audit_orphan_j56.py`)
- Exact source (`audit_source.json`)
- Fatal wall ledger (`wall_exact_mechanics.json`)
- Immediate post-wall ledger (`post_wall_exact_mechanics.json`)
- Canonical belt ledger (`canonical_belt_exact_mechanics.json`)
- Perturbation certificate (`canonical_belt_perturbation_square.json`)
- Watertight OBJ (`J56_TB9_canonical_exact_NONWINNER.obj`)
- Watertight STL (`J56_TB9_canonical_exact_NONWINNER.stl`)

## Integration boundary

Do not admit `J56_TB9_metric_cancel_belt24` as a Gömböc, immutable parent, or completion ticket. Its reported `(21,43,24)` lattice is combinatorially plausible, but the decisive shear-stage mechanics and death-before-birth chronology are exactly false.

The strongest exact object materialized by this audit is the canonical `alpha=192`, `epsilon_i=1/4` member of the stated belt family: primal `(21,43,24)`, uniform-density exact own centroid, strict `(2,2,2)`, full exact H/V/E mechanics, an exact two-parameter open square, and a watertight mesh. It is a corrected nonwinner and topology fixture, not a homogeneous polyhedral Gömböc.
