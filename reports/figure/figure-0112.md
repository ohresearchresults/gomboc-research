# figure-0112

Historical AI scientific report · saved 2026-08-27 UTC. Claims below retain their original status and have not all been independently checked. The current retained construction is C622; the C<500 search remains open.

---

# Fixed-cover Santaló-plus-SPD search — literal resolved outcome

## Literal verdict

**NO CERTIFIED WINNER.** No strict open own-centroid `(S,U,H)=(1,1,0)` chamber was certified. The normative verdict field in the complete original `generator.json` is `no_gomboc_found_in_certified_metric_box`; the exact Euclidean Santaló audit is a certified nonwinner, and the only exact open SPD chamber published has class `(2,2,2)`, not `(1,1,0)`. The complete result explicitly says that no homogeneous polyhedral Gömböc was found in the certified metric region and that the unsampled SPD complement remains unexcluded. :contentReference[oaicite:0]{index=0}

The later wrapper artifacts were inconsistent only at the packaging layer: `/mnt/data/santalo_fixed_cover_status.json` was absent and the fallback wrapper recorded `artifact_status_missing`. The mathematical result is instead present in the complete original archive `projective_centered_4324_handoff.zip`. Its immutable SHA-256 is `b776fbee4903521019e58bb7cd5db0a5f0f7c2a3670c8d8e1139d28180dd4c85`; its original 28-file manifest verifies without mismatch. This resolves the earlier conditional handoff: **there was no winner hidden behind the links.**

## Exact fixed cover and unchanged lattice

The finite input is the complete integer table `Qint` with

```text
q_i = 2^-48 Qint_i,  i=0,...,4323.
```

Row `0` is the stable cap, rows `1..4320` are `120×36` ring rows, and rows `4321..4323` are the terminal unstable fan. The construction-centre body has

```text
H/maximal faces = 4,324
V                = 8,644
true edges        = 12,966
Euler             = 8,644 - 12,966 + 4,324 = 2
volume            = 4.201080076519371
centroid          = (0.0300026404266654, -8.36e-14, -7.20e-13)
class at origin   = (1,1,0).
```

The exhaustive irredundancy audit performed `37,350,724` inactive comparisons with `12` exact-integer fallbacks. Its exact minimum inactive gap is

```text
9880224288652231562241679609765 /
6726150261609921739138283930899980422605
= 1.4689270837501888e-9,
```

at primal vertex `7391`, inactive row `4298`, active triple `(4262,4263,4297)`. Translation of `Q` and the subsequent invertible map preserve this complete lattice. :contentReference[oaicite:1]{index=1}

## Unique Santaló point and exact own-centering

The isolated box is most compactly written as

```text
a_c = 2^-120 * (
 -39878490350125864373364388380978345,
  88581653811863381217051,
  819441514472273259270856)

X = a_c + [-2^-90,2^-90]^3.
```

Equivalently, its exact coordinate intervals are

```text
a_x in [-39878490350125864373364389454720169/2^120,
        -39878490350125864373364387307236521/2^120]
a_y in [88581653811862307475227/2^120,
        88581653811864454958875/2^120]
a_z in [819441514472272185529032/2^120,
        819441514472274333012680/2^120].
```

The unique root is approximately

```text
(-0.03000124168057219827924251765521362054304,
  0.00000000000006664142953109821117263769920,
  0.00000000000061647927749850686002592625519).
```

A strict three-coordinate Krawczyk inclusion isolates the root; positive definiteness of the first-moment Jacobian on `X`, together with strict convexity of polar volume on `int(Q)`, makes it globally unique. All projective denominators satisfy

```text
1-a·y_t in
[0.9713569933275344199096256271172583639201,
 1.031409201124487983220369657015503664311].
```

A fresh independent verifier enclosed

```text
volume in
[4.193528867075553663111323070806043506884,
 4.193528867075553663111323101358140187741]

Mx in [-7.707924869576991110871090095171686241187e-27,
        7.707924872089938268732491199587812440856e-27]
My in [-7.723515817831675699886598056125828611690e-27,
        7.723515815877086602510421549507542265057e-27]
Mz in [-7.724879342814636733872941690049356875799e-27,
        7.724879340153030466470049716444279155128e-27].
```

At the isolated root the three first moments vanish exactly, so `P=(Q-a_*)^circ` has exact ordinary centroid zero. :contentReference[oaicite:2]{index=2}

## Euclidean identity-metric audit

The exactly Santaló-centred body at the identity metric is a large, strict nonwinner:

```text
audited maximal faces       4,324
audited full vertex cones   8,644
audited full edge cones    12,966
zero-straddling intervals       0
(S,U,H) = (2799,2881,5678).
```

Its minimum positive and closest excluded primitives are

```text
stable face:     +2.4395690249239911e-7 ; -1.0410708519194316e-7
unstable vertex: +6.1032645636054800e-5 ; -1.7482810607154846e-4
saddle edge:     +1.0533045298141923e-4 ; -1.7095879979851859e-4.
```

Thus exact Santaló centring preserves every incidence but does not preserve the construction-centre equilibrium gates. :contentReference[oaicite:3]{index=3}

## Exact published SPD representative and open chamber

The only exactified metric representative in the artifacts is the symmetric dyadic linear map

```text
           1  [ 4281  -1099   2522 ]
A_0 =   ----- [ -1099   2157   -388 ]
          4096 [ 2522   -388  10084 ].
```

The induced exact metric is

```text
G_0=A_0^T A_0
   =2^-24 *
     [ 25895246  -8053898   36654942
       -8053898    6010994  -7521186
       36654942   -7521186 108198084 ].
```

The exact leading principal minors of `A_0` are

```text
4281/4096,
2006579/4194304,
17181037455/17179869184,
```

so `A_0` is positive definite. Its determinant is approximately `1.000068002322223`.

The certificate varies all six independent symmetric entries simultaneously by

```text
|Delta A_ij| <= 2^-26
```

while varying the Santaló point over the full box `X`. The closed interval enclosure has strictly positive principal-minor intervals

```text
A11     in [1.04516600072383880615234375,
            1.04516603052616119384765625]
minor_2 in [0.47840568261744920164346694946289063,
            0.47840574545261915773153305053710938]
det A   in [1.0000678926476402885725747182732448,
            1.0000681119968048982116215483983979].
```

Its interior is therefore a genuine open SPD chamber. Every point in it has exact own centroid zero, unchanged `(4324,8644,12966)` combinatorics, zero interval straddles, and strict class

```text
(S,U,H)=(2,2,2).
```

The six positive blockers are

```text
stable rows:        1455, 2805
unstable vertices:  908  on rows (2675,2604,2639)
                    3539 on rows (1570,1641,1605)
saddle edge 2363:   endpoints (3580,5815), incident faces (776,811)
saddle edge 10407:  endpoints (6579,8565), incident faces (3457,3528).
```

The metric certificate itself has verdict `PASS`, but that verdict means the `(2,2,2)` exclusion chamber is rigorously certified; it does **not** mean a Gömböc was found. :contentReference[oaicite:4]{index=4}

## Decision-critical margins in the certified metric box

Face primitives:

```text
row 2805, minimum positive:
[ 0.0011027582725084432348910956633858405,
  0.0011028442781363121186211095903217938]

row 2840, closest negative guard:
[-0.00038560967221141557352906414912752098,
 -0.00038552340481854492550833901631790468].
```

Full three-cone vertex primitives:

```text
vertex 908, minimum positive:
[0.058280416878978620609519367690154468,
 0.058316522025747004331908129870498669]

vertex 907, closest negative guard:
[-0.050472507096726203223990836477241828,
 -0.050436760863160859380549538855120772].
```

The four full edge-cone components are ordered as the two normalized normal-cone coefficients, segment parameter `t`, and `1-t`. For saddle edge `2363` they are

```text
[0.44527643869154903688567515018803533,
 0.44840458275193323389729016525961924]
[0.42183521988718436501741848587698769,
 0.42486517167086956803245811897795647]
[0.88702903877672178989399753845646046,
 0.92958255970703818071854129811981693]
[0.070417440292961860914822125323553337,
 0.11297096122327825173936588498690980].
```

For saddle edge `10407` they are

```text
[0.17560567557939554816925920022185892,
 0.17875448225780118938210705437086290]
[0.68248333098533886520442592882318422,
 0.68828866562596147105068666860461235]
[0.87506382576576269283208375782123767,
 0.93430503272652121182773043983615935]
[0.065694967273478746538906136720470386,
 0.12493617423423730716791624217876233].
```

The closest excluded edge guard is edge `10513`; its first component is

```text
[-0.021109705099269553824070655423383869,
 -0.020888692700865487544836796018898895].
```

Consequently the certified global all-feature **sign clearance** of this box, in the certificate primitive scale, is at least

```text
m_box = 0.00038552340481854492550833901631790468.
```

This positive `m_box` certifies openness of the `(2,2,2)` chamber. It is not a positive Gömböc hard margin because four unwanted equilibrium features remain.

## Best observed search score versus exact certificate

The numerical search objective was

```text
w = max(second-largest stable primitive,
        second-largest unstable primitive,
        largest edge primitive),
```

so a strict `(1,1,0)` sample would require `w<0`; define the corresponding target hard margin as `h_G=-w`.

The best observed sample was sample `3894`:

```text
p = (-0.6736162994232959,
     -1.2159076846720733,
     -3.1951149929660950,
     -0.4866772513152145,
     -3.9942757428393314)
class = (2,2,2)
w     = +0.014314897998952183
h_G   = -0.014314897998952183.
```

This point is only floating-point search evidence. It was **not** exactified and has no interval chamber certificate. Conversely, `A_0` is the exact published representative with a rigorous open box, but the artifacts do not claim that it is the numerical or global optimum. Thus the precise artifact-supported statement is: exact certified representative `A_0`, class `(2,2,2)`, chamber sign clearance `m_box` above; best observed target hard margin `-0.014314897998952183`, noncertifying.

## Search scope and chamber crossings actually obtained

After quotienting the mechanically inert positive scalar, the SPD orbit was parameterized by five trace-zero symmetric-logarithm coordinates

```text
S(p) = [ p0  p2       p3
         p2  p1       p4
         p3  p4  -p0-p1 ],
C(p)=exp(S(p))=A^-1 A^-T.
```

The deterministic run used seed `202608275353`, attempted `10,000` radial-mixture samples with `||p||_2<=6`, and found no `(1,1,0)` sample. The minimum observed stable count was `2`, the minimum observed unstable count was `2`, and `3,148` samples had class `(2,2,2)`. The finite search therefore did not even produce a sampled `(2,1,1)` or `(1,2,1)` chamber. :contentReference[oaicite:5]{index=5}

**Certified metric wall crossings actually obtained: none.** No continuous crossing path, adjacent interval chamber, `(2,1,1)` chamber, `(1,2,1)` chamber, or `(1,1,0)` chamber was certified. The earlier conditional wording about crossing saved one-pair chambers was unsupported and is withdrawn.

The next four-wall target identified but not crossed is

```text
remove stable row 2805,
remove unstable vertex 908,
remove saddle edges 2363 and 10407,
preserve stable row 1455 and unstable vertex 3539,
```

with transfer guards row `2840`, vertex `907`, and edge `10513`. :contentReference[oaicite:6]{index=6}

## Precise remaining SPD gap

Certified finite evidence consists of the exact Santaló root box, the identity-metric nonwinner audit, and the single six-entry box around `A_0`. The `10,000` samples are not coverage.

The unexcluded region is the rest of the noncompact five-dimensional SPD shape quotient: the entire exterior `||p||_2>6` was not sampled, and even inside `||p||_2<=6` the continuum between the finite samples was not interval-covered. No global branch-and-bound, CAD, or complete chamber atlas across the four identified walls was performed. Therefore a strict `(1,1,0)` chamber elsewhere in the fixed lattice's SPD orbit remains possible; the result is **not** a metric-orbit obstruction theorem and does not justify refinement yet. The original result states this limitation explicitly. :contentReference[oaicite:7]{index=7}

## Independent verifier and mesh identity

A fresh run of `verification/verify_projective_centered.py` through `verify_all.py` returned `PASS`. It independently reconstructed from `generator.json`, imported neither the search/materializer code nor stored mechanics ledgers, and reproduced

```text
H=4324, V=8644, E=12966
Krawczyk strict inclusion: true
identity class: (2799,2881,5678)
metric-box class: (2,2,2)
metric entry radius: 2^-26
mesh vertices: 8644
mesh triangles: 17284
triangulated edges: 25926
triangle-edge multiplicity: 2.
```

The fresh verification completed in about `31.79 s`. The four matching watertight midpoint meshes are

```text
mesh/santalo_centered_midpoint.obj
mesh/santalo_centered_midpoint.stl
mesh/metric_A_midpoint.obj
mesh/metric_A_midpoint.stl.
```

They use the exact dyadic centre `a_c` of the isolated root box for finite mesh coordinates; the root and metric interval certificates prove that this replacement preserves every listed incidence and sign. The mesh certificate gives signed volumes `4.193528867075553` and `4.193814036776825`, `det(A_0)=1.000068002322223`, and volume-transform ratio `1.0000000000000002`. :contentReference[oaicite:8]{index=8} :contentReference[oaicite:9]{index=9}

## Immutable supplemental archive

[Complete authoritative 28-file archive](sandbox:/mnt/data/recovered_projective/projective_centered_4324_handoff.zip)

**Final disposition:** `no certified winner`; exact Santaló centring and lattice preservation are certified; one robust open `(2,2,2)` SPD chamber is certified; no `(1,1,0)` chamber or global SPD obstruction is certified.
